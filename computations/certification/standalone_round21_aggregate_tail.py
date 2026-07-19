#!/usr/bin/env python3
"""Standalone outward-Arb certificate for aggregate-tail positivity.

The proof-sign decisions use only exact ``Fraction``/``fmpq`` data and
python-flint ``arb`` interval comparisons.  Decimal lower bounds in the
command-line output are display-only diagnostics.  The program reads no
files and has no dependency other than Python's standard library and
python-flint.

Run with

    python standalone_round21_aggregate_tail.py --precision 192
"""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Sequence

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover - exercised only on a bad host
    raise SystemExit("python-flint is required for this certificate") from exc


SCHEMA = "standalone-round21-aggregate-tail-v1"
MIN_PRECISION_BITS = 192
K0 = 200
LOWER_RHO = Fraction(7, 51)
SPLIT_RHO = Fraction(1, 2)
UPPER_RHO = Fraction(39, 50)
MAX_BOX_WIDTH = Fraction(1, 2000)
EXPECTED_BOX_COUNT = 1286


class VerificationError(RuntimeError):
    """Raised when an exact-partition or interval proof obligation fails."""


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
    digest: str
    display_minima: Mapping[str, DisplayMinimum]


def build_boxes() -> tuple[RationalBox, ...]:
    """Build the exact rational partition, split at rho=1/2."""

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
    """Prove exact coverage, adjacency, widths, and regime ownership."""

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
    # These proof checks ensure the rounded Arb representation covers both
    # exact-rational endpoint enclosures.
    if not enclosure.contains(arb_of_fraction(box.lo)):
        raise VerificationError(f"Arb box misses exact lower endpoint {box.lo}")
    if not enclosure.contains(arb_of_fraction(box.hi)):
        raise VerificationError(f"Arb box misses exact upper endpoint {box.hi}")
    return enclosure


def g_one(z: arb, pi: arb) -> arb:
    """Return (sqrt(1-z^2)-z*acos(z))/pi with outward Arb arithmetic."""

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
    """Apply every outward-Arb wall on every exact rational box."""

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
            # Selection and decimal conversion are never proof decisions.
            approximate_lower = float(value.lower())
            current = minima.get(name)
            if current is None or approximate_lower < current.approximate_lower:
                minima[name] = DisplayMinimum(approximate_lower, box, value)
    return minima


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def canonical_certificate_bytes(
    boxes: Iterable[RationalBox], precision_bits: int
) -> bytes:
    """Canonical ASCII serialization of the exact finite partition."""

    rows = [
        SCHEMA,
        f"precision_bits={precision_bits}",
        f"K0={K0}",
        f"rho={_fraction_text(LOWER_RHO)},{_fraction_text(UPPER_RHO)}",
        f"split_rho={_fraction_text(SPLIT_RHO)}",
        f"max_box_width={_fraction_text(MAX_BOX_WIDTH)}",
    ]
    rows.extend(
        "box="
        + f"{_fraction_text(box.lo)},{_fraction_text(box.hi)},{box.eta_regime}"
        for box in boxes
    )
    return ("\n".join(rows) + "\n").encode("ascii")


def certificate_digest(boxes: Iterable[RationalBox], precision_bits: int) -> str:
    return hashlib.sha256(
        canonical_certificate_bytes(boxes, precision_bits)
    ).hexdigest()


def run_certificate(precision_bits: int = MIN_PRECISION_BITS) -> CertificateResult:
    if precision_bits < MIN_PRECISION_BITS:
        raise ValueError(
            f"precision must be at least {MIN_PRECISION_BITS} bits, got {precision_bits}"
        )
    ctx.prec = precision_bits
    boxes = build_boxes()
    minima = verify_boxes(boxes)
    low_count = sum(box.eta_regime == "rho_le_half" for box in boxes)
    high_count = len(boxes) - low_count
    return CertificateResult(
        precision_bits=precision_bits,
        box_count=len(boxes),
        low_regime_boxes=low_count,
        high_regime_boxes=high_count,
        digest=certificate_digest(boxes, precision_bits),
        display_minima=minima,
    )


def print_result(result: CertificateResult) -> None:
    print("STANDALONE_AGGREGATE_TAIL PASS")
    print(f"precision_bits={result.precision_bits}")
    print(f"box_count={result.box_count}")
    print(f"low_regime_boxes={result.low_regime_boxes}")
    print(f"high_regime_boxes={result.high_regime_boxes}")
    print("coverage=PASS (exact rational adjacency and endpoints)")
    print("proof_sign_checks=B(rho,200)>0, B_K(rho,200)>0, F(rho)>0")
    print(f"certificate_sha256={result.digest}")
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
        print(f"STANDALONE_AGGREGATE_TAIL FAIL: {exc}")
        return 1
    print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
