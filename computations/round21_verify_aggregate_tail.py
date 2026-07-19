"""Outward-Arb certificate for the Round 21 aggregate tail reserve.

The proof-sign decisions in this module use only exact ``Fraction``/``fmpq``
data and python-flint ``arb`` interval comparisons.  Decimal lower bounds in
the command-line output are explicitly display-only diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, Mapping, Sequence

from flint import arb, ctx, fmpq


MIN_PRECISION_BITS = 192
K0 = 200
LOWER_RHO = Fraction(7, 51)
SPLIT_RHO = Fraction(1, 2)
UPPER_RHO = Fraction(39, 50)
MAX_BOX_WIDTH = Fraction(1, 2000)
EXPECTED_BOX_COUNT = 1286

EXPECTED_HASHES: Mapping[str, str] = {
    "rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md":
        "61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0",
    "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md":
        "0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f",
    "state/lemma_packets/SHELL-weighted-lattice-fractional.md":
        "a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c",
    "state/lemma_packets/SHELL-sturm-liouville-completeness.md":
        "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "sources/annuli_polya.md":
        "951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57",
}


class VerificationError(RuntimeError):
    """Raised when an authenticated or interval proof obligation fails."""


@dataclass(frozen=True)
class RationalBox:
    lo: Fraction
    hi: Fraction
    eta_regime: str

    @property
    def width(self) -> Fraction:
        return self.hi - self.lo


@dataclass(frozen=True)
class DisplayMinimum:
    """A nonproof decimal summary of already-proved positive Arb balls."""

    approximate_lower: float
    box: RationalBox
    ball: arb


@dataclass(frozen=True)
class CertificateResult:
    precision_bits: int
    box_count: int
    low_regime_boxes: int
    high_regime_boxes: int
    authenticated_hashes: Mapping[str, str]
    display_minima: Mapping[str, DisplayMinimum]


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def authenticate_inputs(
    root: Path | None = None,
    expected_hashes: Mapping[str, str] = EXPECTED_HASHES,
) -> Dict[str, str]:
    root = repository_root() if root is None else Path(root)
    observed: Dict[str, str] = {}
    for relative, expected in expected_hashes.items():
        path = root / relative
        if not path.is_file():
            raise VerificationError(f"missing authenticated input: {relative}")
        actual = sha256_file(path)
        if actual.lower() != expected.lower():
            raise VerificationError(
                f"SHA-256 mismatch for {relative}: expected {expected}, got {actual}"
            )
        observed[relative] = actual
    return observed


def build_boxes() -> tuple[RationalBox, ...]:
    boxes: list[RationalBox] = []
    segments = (
        (LOWER_RHO, SPLIT_RHO, "rho_le_half"),
        (SPLIT_RHO, UPPER_RHO, "rho_ge_half"),
    )
    for start, stop, regime in segments:
        lo = start
        while lo < stop:
            hi = min(lo + MAX_BOX_WIDTH, stop)
            boxes.append(RationalBox(lo, hi, regime))
            lo = hi
    validate_partition(boxes)
    return tuple(boxes)


def validate_partition(boxes: Sequence[RationalBox]) -> None:
    if len(boxes) != EXPECTED_BOX_COUNT:
        raise VerificationError(
            f"wrong box count: expected {EXPECTED_BOX_COUNT}, got {len(boxes)}"
        )
    if boxes[0].lo != LOWER_RHO or boxes[-1].hi != UPPER_RHO:
        raise VerificationError("box partition has the wrong outer endpoints")
    for index, box in enumerate(boxes):
        if not (Fraction(0) < box.width <= MAX_BOX_WIDTH):
            raise VerificationError(f"invalid exact width in box {index}: {box.width}")
        if index and boxes[index - 1].hi != box.lo:
            raise VerificationError(f"gap or overlap before box {index}")
        if box.eta_regime == "rho_le_half":
            if box.hi > SPLIT_RHO:
                raise VerificationError(f"low-eta box {index} crosses rho=1/2")
        elif box.eta_regime == "rho_ge_half":
            if box.lo < SPLIT_RHO:
                raise VerificationError(f"high-eta box {index} crosses rho=1/2")
        else:
            raise VerificationError(f"unknown eta regime in box {index}")
    low_count = sum(box.eta_regime == "rho_le_half" for box in boxes)
    high_count = sum(box.eta_regime == "rho_ge_half" for box in boxes)
    if (low_count, high_count) != (726, 560):
        raise VerificationError(
            f"wrong split counts: expected (726, 560), got {(low_count, high_count)}"
        )


def arb_of_fraction(value: Fraction) -> arb:
    return arb(fmpq(value.numerator, value.denominator))


def arb_box(box: RationalBox) -> arb:
    """Return an outward Arb ball covering the exact rational box."""

    midpoint = (box.lo + box.hi) / 2
    radius = (box.hi - box.lo) / 2
    enclosure = arb(
        fmpq(midpoint.numerator, midpoint.denominator),
        fmpq(radius.numerator, radius.denominator),
    )
    # These are proof checks that the rounded Arb representation still covers
    # both exact-rational endpoint enclosures.
    if not enclosure.contains(arb_of_fraction(box.lo)):
        raise VerificationError(f"Arb box misses exact lower endpoint {box.lo}")
    if not enclosure.contains(arb_of_fraction(box.hi)):
        raise VerificationError(f"Arb box misses exact upper endpoint {box.hi}")
    return enclosure


def g_one(z: arb, pi: arb) -> arb:
    return ((arb(1) - z * z).sqrt() - z * z.acos()) / pi


def evaluate_at_k0(rho: arb, eta_regime: str) -> Mapping[str, arb]:
    """Evaluate all base-face and K-convexity quantities on one rho ball."""

    one = arb(1)
    two = arb(2)
    half = one / two
    k = arb(K0)
    pi = arb.pi()

    if eta_regime == "rho_le_half":
        eta = g_one(half, pi)
    elif eta_regime == "rho_ge_half":
        eta = g_one(rho, pi)
    else:
        raise VerificationError(f"unknown eta regime: {eta_regime}")

    d = two * rho.asin() / pi
    b = two * pi * rho / (one - rho)
    mu = rho * k
    c = b * k
    radius = mu + half
    s = (radius * radius + c).sqrt()
    p = s - radius
    asinh_term = (radius / c.sqrt()).asinh()
    integral = (radius * s + c * asinh_term - radius * radius) / two

    reserve = (
        (mu - half) * (k * eta - one)
        + (d / two) * (mu - arb(3) / two) * (mu - half)
        - (one + d) * integral
        - arb(8) * (mu + half) / (arb(15) * mu.sqrt())
    )

    integral_k = rho * p + (b / two) * asinh_term
    reserve_k = (
        rho * (k * eta - one)
        + (mu - half) * eta
        + d * rho * (mu - one)
        - (one + d) * integral_k
        - two * rho * (two * mu - one) / (arb(15) * mu * mu.sqrt())
    )

    integral_kk = (
        rho * rho * (radius / s - one)
        + rho * b / (two * s)
        + b * (two * rho * k - one) / (arb(8) * k * s)
    )
    integral_kk_bound = arb(3) * b / (arb(4) * k)
    interface_kk = (
        rho * rho * (two * mu - arb(3))
        / (arb(15) * mu * mu * mu.sqrt())
    )
    curvature_floor = (
        two * rho * eta
        + d * rho * rho
        - arb(3) * (one + d) * b / arb(800)
    )
    reserve_kk = (
        two * rho * eta + d * rho * rho
        - (one + d) * integral_kk + interface_kk
    )

    return {
        "eta": eta,
        "b": b,
        "mu": mu,
        "R": radius,
        "S": s,
        "B200": reserve,
        "BK200": reserve_k,
        "F": curvature_floor,
        "I_KK": integral_kk,
        "I_KK_bound": integral_kk_bound,
        "interface_KK": interface_kk,
        "B_KK": reserve_kk,
    }


def _require_positive(name: str, value: arb, box: RationalBox) -> None:
    if not (value > 0):
        raise VerificationError(
            f"could not prove {name}>0 on [{box.lo}, {box.hi}] "
            f"({box.eta_regime}): {value.str(30)}"
        )


def _require_less(name: str, left: arb, right: arb, box: RationalBox) -> None:
    if not (left < right):
        raise VerificationError(
            f"could not prove {name} on [{box.lo}, {box.hi}] "
            f"({box.eta_regime}): left={left.str(30)}, right={right.str(30)}"
        )


def verify_boxes(boxes: Iterable[RationalBox]) -> Mapping[str, DisplayMinimum]:
    minima: Dict[str, DisplayMinimum] = {}
    for box in boxes:
        rho = arb_box(box)
        values = evaluate_at_k0(rho, box.eta_regime)

        _require_positive("1-rho", arb(1) - rho, box)
        _require_positive("mu-3/2", values["mu"] - arb(3) / arb(2), box)
        _require_positive("K*eta-1", arb(K0) * values["eta"] - arb(1), box)
        _require_positive("S-R", values["S"] - values["R"], box)
        _require_positive("R-rho*K", values["R"] - rho * arb(K0), box)
        _require_less(
            "I_KK < 3b/(4K)", values["I_KK"], values["I_KK_bound"], box
        )
        _require_positive("interface_KK", values["interface_KK"], box)
        _require_less("F < B_KK", values["F"], values["B_KK"], box)

        for name in ("B200", "BK200", "F"):
            value = values[name]
            _require_positive(name, value, box)
            # Selection and decimal conversion are not used by any proof
            # decision.  They only reproduce human-readable diagnostics.
            approximate_lower = float(value.lower())
            current = minima.get(name)
            if current is None or approximate_lower < current.approximate_lower:
                minima[name] = DisplayMinimum(approximate_lower, box, value)
    return minima


def run_certificate(
    precision_bits: int = MIN_PRECISION_BITS,
    *,
    authenticate: bool = True,
    root: Path | None = None,
) -> CertificateResult:
    if precision_bits < MIN_PRECISION_BITS:
        raise ValueError(
            f"precision must be at least {MIN_PRECISION_BITS} bits, got {precision_bits}"
        )
    ctx.prec = precision_bits
    observed = authenticate_inputs(root) if authenticate else {}
    boxes = build_boxes()
    minima = verify_boxes(boxes)
    low_count = sum(box.eta_regime == "rho_le_half" for box in boxes)
    high_count = len(boxes) - low_count
    return CertificateResult(
        precision_bits=precision_bits,
        box_count=len(boxes),
        low_regime_boxes=low_count,
        high_regime_boxes=high_count,
        authenticated_hashes=observed,
        display_minima=minima,
    )


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def print_result(result: CertificateResult) -> None:
    print("PASS round21 aggregate-tail global positivity")
    print(f"precision_bits={result.precision_bits}")
    print(f"box_count={result.box_count}")
    print(f"low_regime_boxes={result.low_regime_boxes}")
    print(f"high_regime_boxes={result.high_regime_boxes}")
    print("proof_sign_checks=B(rho,200)>0, B_K(rho,200)>0, F(rho)>0")
    for relative, digest in result.authenticated_hashes.items():
        print(f"authenticated_sha256 {digest}  {relative}")
    print("display_only_decimal_lower_bounds (not used for proof):")
    for name in ("B200", "BK200", "F"):
        minimum = result.display_minima[name]
        box = minimum.box
        display = minimum.ball.lower().str(16, radius=False)
        print(
            f"  {name}: {display} on intended rational box "
            f"[{_fraction_text(box.lo)}, {_fraction_text(box.hi)}]"
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--precision",
        type=int,
        default=MIN_PRECISION_BITS,
        help=f"Arb midpoint precision in bits (minimum {MIN_PRECISION_BITS})",
    )
    args = parser.parse_args(argv)
    try:
        result = run_certificate(args.precision)
    except (VerificationError, ValueError) as exc:
        print(f"FAIL round21 aggregate-tail global positivity: {exc}")
        return 1
    print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
