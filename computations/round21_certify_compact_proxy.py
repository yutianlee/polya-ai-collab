#!/usr/bin/env python3
"""Finite Arb certificate for the Round 21 compact shell rectangle.

This program proves, using only the three hash-gated shell packets named in
``PACKETS`` and the permitted definition of ``G`` from ``sources/annuli_polya.md``,
that the coarse integer proxy is strictly below the three-dimensional Weyl
term on

    7/51 <= rho <= 39/50,    12 <= K <= 200.

All geometry and all branch decisions are exact ``Fraction`` operations.
Arb supplies outward transcendental enclosures.  Floating-point numbers are
used only to choose between two legal subdivision directions and for display;
they never decide whether a box passes.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover - exercised only on a bad host
    raise SystemExit("python-flint is required for the Round 21 certificate") from exc


SCHEMA = "round21-compact-proxy-v2-half-open-faces"
MIN_PRECISION_BITS = 192
DEFAULT_PRECISION_BITS = 256
DEFAULT_MAX_DEPTH = 30
DEFAULT_MAX_BOXES = 100_000

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = REPO_ROOT / "state" / "lemma_packets"
PACKETS: Mapping[str, str] = {
    "SHELL-sturm-liouville-completeness.md":
        "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "SHELL-phase-enclosures.md":
        "96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf",
    "SHELL-weighted-lattice-fractional.md":
        "a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c",
}


class CertificateError(RuntimeError):
    """The first rigorous certificate condition that failed."""


class HashGateError(CertificateError):
    """A dependency packet did not have its accepted digest."""


@dataclass(frozen=True, order=True)
class Box:
    rho_lo: Fraction
    rho_hi: Fraction
    k_lo: Fraction
    k_hi: Fraction

    def area(self) -> Fraction:
        return (self.rho_hi - self.rho_lo) * (self.k_hi - self.k_lo)


ROOT_BOX = Box(Fraction(7, 51), Fraction(39, 50), Fraction(12), Fraction(200))


@dataclass(frozen=True)
class FloorUpper:
    count: int
    ceiling: int
    wall_straddle: bool


@dataclass(frozen=True)
class ProxyUpper:
    value: int
    comparisons: int
    wall_straddles: int


@dataclass(frozen=True)
class BoxEvaluation:
    proxy_upper: int
    comparison: arb
    passed: bool

    def subdivision_score(self) -> float:
        """A non-proof heuristic; PASS never depends on this float."""

        return float(self.comparison.mid())


@dataclass(frozen=True)
class Leaf:
    box: Box
    depth: int
    proxy_upper: int


@dataclass(frozen=True)
class Certificate:
    leaves: tuple[Leaf, ...]
    max_depth: int
    precision_bits: int
    min_gap_display: float
    packet_hashes: tuple[tuple[str, str], ...]
    digest: str
    generated_proxy_corners: int
    generated_floor_comparisons: int
    generated_wall_straddles: int


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_to_arb(value: Fraction) -> arb:
    return arb(fmpq(value.numerator, value.denominator))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_packet_hashes(
    packet_dir: Path = PACKET_DIR,
    expected: Mapping[str, str] = PACKETS,
) -> tuple[tuple[str, str], ...]:
    """Apply the three accepted-packet hash gates before doing mathematics."""

    observed: list[tuple[str, str]] = []
    for name, wanted in expected.items():
        path = packet_dir / name
        if not path.is_file():
            raise HashGateError(f"missing dependency packet: {path}")
        got = file_sha256(path)
        if got.lower() != wanted.lower():
            raise HashGateError(
                f"hash mismatch for {name}: expected {wanted.lower()}, got {got.lower()}"
            )
        observed.append((name, got.lower()))
    return tuple(observed)


def active_channel_count(k: Fraction) -> int:
    """Number of half-integers nu=ell+1/2 satisfying the strict cutoff nu<K."""

    shifted = k - Fraction(1, 2)
    if shifted <= 0:
        return 0
    return (shifted.numerator + shifted.denominator - 1) // shifted.denominator


def g_arb(a: Fraction, nu: Fraction) -> arb:
    r"""Outward Arb enclosure of the permitted source identity ``G_a(nu)``.

    Exact rational comparisons own both interfaces.  In particular, ``nu=a``
    returns exact zero and never asks Arb to resolve ``sqrt(0)`` or ``acos(1)``.
    """

    if a <= 0 or nu < 0:
        raise ValueError("G requires a>0 and nu>=0")
    if nu >= a:
        return arb(0)
    aa = fraction_to_arb(a)
    vv = fraction_to_arb(nu)
    radicand = aa * aa - vv * vv
    if not (radicand > 0):
        raise CertificateError(f"Arb failed to prove positive G radicand at a={a}, nu={nu}")
    return (radicand.sqrt() - vv * (vv / aa).acos()) / arb.pi()


def proxy_argument_arb(rho: Fraction, k: Fraction, nu: Fraction) -> arb:
    """Outward enclosure of A_{rho,K}(nu)+1/4 at one rational point."""

    if not (0 < rho < 1 and k > 0 and nu >= 0):
        raise ValueError("proxy point is outside 0<rho<1, K>0, nu>=0")
    inner = rho * k
    # g_arb owns nu=inner and nu=k by exact comparisons.
    return g_arb(k, nu) - g_arb(inner, nu) + fraction_to_arb(Fraction(1, 4))


def strict_count_upper_from_arb(value: arb) -> FloorUpper:
    r"""Certify an upper bound for ``[value]_<`` by an Arb/integer comparison.

    If Arb proves ``value <= M``, then every positive integer strictly below
    ``value`` is at most ``M-1``.  This is sharp at an exact integer: for
    example, exact ``value=3`` returns 2.  If an inexact ball straddles an
    integer wall, the next integer is used, producing a safe one-unit
    overestimate rather than making an uncertified floor decision.
    """

    if not value.is_finite():
        raise CertificateError("non-finite Arb proxy argument")
    if not (value > 0):
        raise CertificateError(f"Arb failed to prove positive proxy argument: {value}")
    ceiling_ball = value.upper().ceil()
    ceiling_fmpz = ceiling_ball.unique_fmpz()
    if ceiling_fmpz is None:
        raise CertificateError(f"could not extract an exact integer ceiling from {value}")
    ceiling = int(ceiling_fmpz)
    # This is the proof-producing comparison.  The ceiling extraction merely
    # proposes M; no floor/float result is trusted without this check.
    if not (value <= arb(ceiling)):
        raise CertificateError(f"Arb did not certify proxy argument <= {ceiling}: {value}")
    count = max(0, ceiling - 1)
    wall_straddle = count > 0 and value.contains(count) and not value.is_exact()
    return FloorUpper(count=count, ceiling=ceiling, wall_straddle=wall_straddle)


def coarse_proxy_upper(rho: Fraction, k: Fraction) -> ProxyUpper:
    r"""Certify ``P_coarse(rho,k)`` from outward per-channel Arb enclosures."""

    total = 0
    comparisons = 0
    wall_straddles = 0
    for ell in range(active_channel_count(k)):
        nu = Fraction(2 * ell + 1, 2)
        if not (nu < k):
            raise CertificateError("strict active-channel enumeration included nu=K")
        bound = strict_count_upper_from_arb(proxy_argument_arb(rho, k, nu))
        total += (2 * ell + 1) * bound.count
        comparisons += 1
        wall_straddles += int(bound.wall_straddle)
    return ProxyUpper(total, comparisons, wall_straddles)


def weyl_arb(rho: Fraction, k: Fraction) -> arb:
    r"""Outward Arb enclosure of 2(1-rho^3)K^3/(9*pi)."""

    rr = fraction_to_arb(rho)
    kk = fraction_to_arb(k)
    return arb(2) * (arb(1) - rr**3) * kk**3 / (arb(9) * arb.pi())


class Certifier:
    """Cached 256-bit (or stronger) corner evaluator and adaptive prover."""

    def __init__(
        self,
        precision_bits: int = DEFAULT_PRECISION_BITS,
        max_depth: int = DEFAULT_MAX_DEPTH,
        max_boxes: int = DEFAULT_MAX_BOXES,
    ) -> None:
        if precision_bits < MIN_PRECISION_BITS:
            raise CertificateError(
                f"precision {precision_bits} is below the required {MIN_PRECISION_BITS} bits"
            )
        if max_depth < 1 or max_boxes < 1:
            raise ValueError("max_depth and max_boxes must be positive")
        self.precision_bits = precision_bits
        self.max_depth = max_depth
        self.max_boxes = max_boxes
        self._proxy_cache: dict[tuple[Fraction, Fraction], ProxyUpper] = {}
        self._weyl_cache: dict[tuple[Fraction, Fraction], arb] = {}

    def proxy_upper(self, rho: Fraction, k: Fraction) -> ProxyUpper:
        key = (rho, k)
        if key not in self._proxy_cache:
            with ctx.workprec(self.precision_bits):
                self._proxy_cache[key] = coarse_proxy_upper(rho, k)
        return self._proxy_cache[key]

    def weyl(self, rho: Fraction, k: Fraction) -> arb:
        key = (rho, k)
        if key not in self._weyl_cache:
            with ctx.workprec(self.precision_bits):
                self._weyl_cache[key] = weyl_arb(rho, k)
        return self._weyl_cache[key]

    def evaluate(self, box: Box) -> BoxEvaluation:
        """Use the two monotone corners and accept only a certain Arb inequality."""

        proxy = self.proxy_upper(box.rho_lo, box.k_hi)
        with ctx.workprec(self.precision_bits):
            # lower() is itself outward: this explicitly implements the test
            # requested in the certificate specification, W_lower - integer > 0.
            w_lower = self.weyl(box.rho_hi, box.k_lo).lower()
            comparison = w_lower - proxy.value
            passed = bool(comparison > 0)
        return BoxEvaluation(proxy.value, comparison, passed)

    @staticmethod
    def _split_rho(box: Box) -> tuple[Box, Box]:
        mid = (box.rho_lo + box.rho_hi) / 2
        return (
            Box(box.rho_lo, mid, box.k_lo, box.k_hi),
            Box(mid, box.rho_hi, box.k_lo, box.k_hi),
        )

    @staticmethod
    def _split_k(box: Box) -> tuple[Box, Box]:
        mid = (box.k_lo + box.k_hi) / 2
        return (
            Box(box.rho_lo, box.rho_hi, box.k_lo, mid),
            Box(box.rho_lo, box.rho_hi, mid, box.k_hi),
        )

    @staticmethod
    def _split_score(evaluations: Sequence[BoxEvaluation]) -> tuple[int, float, float]:
        # Floats select only a subdivision direction.  Each eventual leaf is
        # independently accepted by BoxEvaluation.passed, an Arb predicate.
        displays = tuple(item.subdivision_score() for item in evaluations)
        return (sum(item.passed for item in evaluations), min(displays), sum(displays))

    def build(self, root: Box = ROOT_BOX) -> tuple[Leaf, ...]:
        if not (Fraction(0) < root.rho_lo < root.rho_hi < Fraction(1)):
            raise ValueError("root rho interval must lie strictly inside (0,1)")
        if not (Fraction(0) < root.k_lo < root.k_hi):
            raise ValueError("root K interval must be positive and nondegenerate")

        stack: list[tuple[Box, int]] = [(root, 0)]
        leaves: list[Leaf] = []
        while stack:
            box, depth = stack.pop()
            evaluation = self.evaluate(box)
            if evaluation.passed:
                leaves.append(Leaf(box, depth, evaluation.proxy_upper))
                continue
            if depth >= self.max_depth:
                raise CertificateError(
                    f"depth limit {self.max_depth} at failed box {box}; "
                    f"comparison={evaluation.comparison}"
                )
            if len(leaves) + len(stack) + 2 > self.max_boxes:
                raise CertificateError(
                    f"box-count limit {self.max_boxes} before splitting failed box {box}"
                )

            rho_children = self._split_rho(box)
            k_children = self._split_k(box)
            rho_evaluations = tuple(self.evaluate(child) for child in rho_children)
            k_evaluations = tuple(self.evaluate(child) for child in k_children)
            if self._split_score(rho_evaluations) > self._split_score(k_evaluations):
                chosen = rho_children
            else:
                chosen = k_children
            # Reverse push makes the lower child the deterministic next item.
            for child in reversed(chosen):
                stack.append((child, depth + 1))
        return tuple(leaves)

    @property
    def proxy_corner_count(self) -> int:
        return len(self._proxy_cache)

    @property
    def floor_comparison_count(self) -> int:
        return sum(item.comparisons for item in self._proxy_cache.values())

    @property
    def wall_straddle_count(self) -> int:
        return sum(item.wall_straddles for item in self._proxy_cache.values())


def coordinate_owned(value: Fraction, lo: Fraction, hi: Fraction, root_hi: Fraction) -> bool:
    """Lower-closed/upper-open ownership, closing only the root's upper face."""

    return lo <= value and (value < hi or (value == root_hi and hi == root_hi))


def box_owns(root: Box, box: Box, rho: Fraction, k: Fraction) -> bool:
    """Unique shared-face ownership convention used by the finite partition."""

    return coordinate_owned(rho, box.rho_lo, box.rho_hi, root.rho_hi) and coordinate_owned(
        k, box.k_lo, box.k_hi, root.k_hi
    )


def _check_owned_vertical_face(root: Box, leaves: Sequence[Leaf], rho: Fraction) -> None:
    """Check exact, unique K-tiling by the leaves that own this rho face."""

    intervals = sorted(
        (leaf.box.k_lo, leaf.box.k_hi)
        for leaf in leaves
        if coordinate_owned(rho, leaf.box.rho_lo, leaf.box.rho_hi, root.rho_hi)
    )
    if not intervals:
        raise CertificateError(f"uncovered vertical face rho={rho}")
    cursor = root.k_lo
    for lo, hi in intervals:
        if lo < cursor:
            raise CertificateError(f"owned-face overlap at rho={rho}, K={lo}..{cursor}")
        if lo > cursor:
            raise CertificateError(f"gap on vertical face rho={rho} at K={cursor}..{lo}")
        cursor = hi
    if cursor != root.k_hi:
        raise CertificateError(f"vertical face rho={rho} ends at K={cursor}, not {root.k_hi}")


def validate_partition(root: Box, leaves: Sequence[Leaf]) -> None:
    """Exact full-coverage/disjoint-interior sweep for the rational rectangles."""

    if not leaves:
        raise CertificateError("empty leaf list")
    for index, leaf in enumerate(leaves):
        box = leaf.box
        if not (
            root.rho_lo <= box.rho_lo < box.rho_hi <= root.rho_hi
            and root.k_lo <= box.k_lo < box.k_hi <= root.k_hi
        ):
            raise CertificateError(f"leaf {index} lies outside or degenerates in root: {box}")

    rho_faces = sorted(
        {root.rho_lo, root.rho_hi}
        | {leaf.box.rho_lo for leaf in leaves}
        | {leaf.box.rho_hi for leaf in leaves}
    )
    for rho_lo, rho_hi in zip(rho_faces, rho_faces[1:]):
        intervals = sorted(
            (leaf.box.k_lo, leaf.box.k_hi)
            for leaf in leaves
            if leaf.box.rho_lo <= rho_lo and rho_hi <= leaf.box.rho_hi
        )
        cursor = root.k_lo
        for k_lo, k_hi in intervals:
            if k_lo < cursor:
                raise CertificateError(
                    f"positive-area overlap in rho slab {rho_lo}..{rho_hi} at K={k_lo}"
                )
            if k_lo > cursor:
                raise CertificateError(
                    f"coverage gap in rho slab {rho_lo}..{rho_hi}: K={cursor}..{k_lo}"
                )
            cursor = k_hi
        if cursor != root.k_hi:
            raise CertificateError(
                f"rho slab {rho_lo}..{rho_hi} ends at K={cursor}, not {root.k_hi}"
            )

    # Area is a second, independent exact coverage invariant.
    if sum((leaf.box.area() for leaf in leaves), Fraction(0)) != root.area():
        raise CertificateError("exact sum of leaf areas differs from root area")

    # The proof bounds each closed box, but the partition assigns every shared
    # face to exactly one child: lower closed / upper open, except that the
    # root's upper faces are closed.  Checking all exact rho faces, together
    # with the open-slab sweep above, proves full pointwise coverage and true
    # nonoverlap (not merely disjoint interiors).
    for rho in rho_faces:
        _check_owned_vertical_face(root, leaves, rho)


def canonical_certificate_bytes(
    root: Box,
    leaves: Iterable[Leaf],
    precision_bits: int,
    packet_hashes: Sequence[tuple[str, str]],
) -> bytes:
    rows = [
        SCHEMA,
        f"precision_bits={precision_bits}",
        "root=" + ",".join(
            fraction_text(value)
            for value in (root.rho_lo, root.rho_hi, root.k_lo, root.k_hi)
        ),
    ]
    rows.extend(f"packet={name}:{digest}" for name, digest in packet_hashes)
    for leaf in sorted(leaves, key=lambda item: item.box):
        box = leaf.box
        rows.append(
            "leaf="
            + ",".join(
                fraction_text(value)
                for value in (box.rho_lo, box.rho_hi, box.k_lo, box.k_hi)
            )
            + f",depth={leaf.depth},P={leaf.proxy_upper}"
        )
    return ("\n".join(rows) + "\n").encode("ascii")


def certificate_digest(
    root: Box,
    leaves: Iterable[Leaf],
    precision_bits: int,
    packet_hashes: Sequence[tuple[str, str]],
) -> str:
    return hashlib.sha256(
        canonical_certificate_bytes(root, leaves, precision_bits, packet_hashes)
    ).hexdigest()


def validate_leaves(certifier: Certifier, leaves: Sequence[Leaf]) -> float:
    """Replay all proof predicates; return only a display approximation to min gap."""

    display_gaps: list[float] = []
    for index, leaf in enumerate(leaves):
        evaluation = certifier.evaluate(leaf.box)
        if evaluation.proxy_upper != leaf.proxy_upper:
            raise CertificateError(
                f"leaf {index} proxy tampering/mismatch: stored {leaf.proxy_upper}, "
                f"recomputed {evaluation.proxy_upper}"
            )
        if not evaluation.passed:
            raise CertificateError(
                f"leaf {index} fails certain Arb comparison: {evaluation.comparison}"
            )
        display_gaps.append(evaluation.subdivision_score())
    return min(display_gaps)


def build_certificate(
    precision_bits: int = DEFAULT_PRECISION_BITS,
    max_depth: int = DEFAULT_MAX_DEPTH,
    max_boxes: int = DEFAULT_MAX_BOXES,
    packet_dir: Path = PACKET_DIR,
) -> Certificate:
    packet_hashes = verify_packet_hashes(packet_dir)
    certifier = Certifier(precision_bits, max_depth, max_boxes)
    leaves = certifier.build(ROOT_BOX)
    validate_partition(ROOT_BOX, leaves)
    min_gap_display = validate_leaves(certifier, leaves)
    digest = certificate_digest(ROOT_BOX, leaves, precision_bits, packet_hashes)
    return Certificate(
        leaves=leaves,
        max_depth=max(leaf.depth for leaf in leaves),
        precision_bits=precision_bits,
        min_gap_display=min_gap_display,
        packet_hashes=packet_hashes,
        digest=digest,
        generated_proxy_corners=certifier.proxy_corner_count,
        generated_floor_comparisons=certifier.floor_comparison_count,
        generated_wall_straddles=certifier.wall_straddle_count,
    )


def tampered_leaf(leaf: Leaf) -> Leaf:
    """Small public helper used by the adversarial unit test."""

    return replace(leaf, proxy_upper=leaf.proxy_upper + 1)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision-bits", type=int, default=DEFAULT_PRECISION_BITS)
    parser.add_argument("--max-depth", type=int, default=DEFAULT_MAX_DEPTH)
    parser.add_argument("--max-boxes", type=int, default=DEFAULT_MAX_BOXES)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        certificate = build_certificate(
            precision_bits=args.precision_bits,
            max_depth=args.max_depth,
            max_boxes=args.max_boxes,
        )
    except Exception as exc:
        print("ROUND21_COMPACT_PROXY FAIL")
        print(f"first_issue={type(exc).__name__}: {exc}")
        return 1

    print("ROUND21_COMPACT_PROXY PASS")
    for name, digest in certificate.packet_hashes:
        print(f"packet_sha256[{name}]={digest}")
    print(f"precision_bits={certificate.precision_bits}")
    print("root_rho=[7/51,39/50]")
    print("root_K=[12,200]")
    print(f"leaf_boxes={len(certificate.leaves)}")
    print(f"max_depth={certificate.max_depth}")
    print("coverage=PASS (exact rational slab/face sweep and exact area)")
    print("nonoverlap=PASS (exact half-open shared-face ownership)")
    print(f"generated_proxy_corners={certificate.generated_proxy_corners}")
    print(f"generated_floor_comparisons={certificate.generated_floor_comparisons}")
    print(f"generated_wall_straddles={certificate.generated_wall_straddles}")
    print(f"min_gap_lower_display={certificate.min_gap_display:.17g}")
    print(f"certificate_sha256={certificate.digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
