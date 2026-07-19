#!/usr/bin/env python3
"""Independently verify the Round 8 compact-box pilot certificate.

The checker intentionally imports neither python-flint nor the producer
module.  All decisive comparisons use :class:`fractions.Fraction`:

* Machin's formula with alternating-series remainders encloses pi;
* rational Taylor remainders enclose sine and cosine near pi;
* the ell=0 and ell=1 Riccati determinants are reconstructed algebraically;
* Poincare--Sturm and Weyl comparisons are exact rational inequalities.

The checker is specialized to the pilot schema.  It is not a checker for an
arbitrary cover of the three Round 8 residual zones.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


SCHEMA = "polya-shell-compact-box-certificate-v0.1"


class VerificationError(RuntimeError):
    """Raised when any certificate assertion cannot be reconstructed."""


@dataclass(frozen=True)
class QInterval:
    """A closed interval with exact rational endpoints."""

    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("invalid rational interval")

    @classmethod
    def point(cls, value: Fraction | int) -> "QInterval":
        q = Fraction(value)
        return cls(q, q)

    def __add__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        other = _as_interval(other)
        return QInterval(self.lower + other.lower, self.upper + other.upper)

    __radd__ = __add__

    def __neg__(self) -> "QInterval":
        return QInterval(-self.upper, -self.lower)

    def __sub__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        return self + (-_as_interval(other))

    def __rsub__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        return _as_interval(other) - self

    def __mul__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        other = _as_interval(other)
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return QInterval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "QInterval":
        if self.lower <= 0 <= self.upper:
            raise ZeroDivisionError("interval contains zero")
        return QInterval(1 / self.upper, 1 / self.lower)

    def __truediv__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        return self * _as_interval(other).reciprocal()

    def __rtruediv__(self, other: "QInterval" | Fraction | int) -> "QInterval":
        return _as_interval(other) * self.reciprocal()

    def square(self) -> "QInterval":
        if self.lower >= 0:
            return QInterval(self.lower**2, self.upper**2)
        if self.upper <= 0:
            return QInterval(self.upper**2, self.lower**2)
        return QInterval(Fraction(0), max(self.lower**2, self.upper**2))

    @property
    def sign(self) -> str:
        if self.lower > 0:
            return "positive"
        if self.upper < 0:
            return "negative"
        return "contains_zero"


def _as_interval(value: QInterval | Fraction | int) -> QInterval:
    return value if isinstance(value, QInterval) else QInterval.point(value)


def _parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"invalid rational endpoint {text!r}") from exc


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _verify_provenance_hashes(data: dict[str, Any]) -> dict[str, str]:
    """Check the three source hashes embedded by the producer."""

    checker_path = Path(__file__).resolve()
    computations_dir = checker_path.parent
    repository_root = computations_dir.parent
    paths = {
        "producer": computations_dir / "round8_compact_box_certificate.py",
        "independent_checker": checker_path,
        "frozen_packet": repository_root
        / "state"
        / "lemma_packets"
        / "SHELL-rho-compact.md",
    }
    try:
        recorded = data["reproducibility"]["sha256"]
    except (KeyError, TypeError) as exc:
        raise VerificationError("missing reproducibility hashes") from exc
    actual: dict[str, str] = {}
    for label, path in paths.items():
        if not path.is_file():
            raise VerificationError(f"hashed input is missing: {path}")
        actual[label] = _sha256(path)
        _require(
            recorded.get(label) == actual[label],
            f"SHA-256 mismatch for {label}",
        )
    return actual


def _alternating_bounds(terms: list[Fraction], next_term: Fraction) -> QInterval:
    partial = sum(terms, Fraction(0))
    adjacent = partial + next_term
    return QInterval(min(partial, adjacent), max(partial, adjacent))


def _atan_reciprocal_bounds(q: int, count: int = 32) -> QInterval:
    """Enclose atan(1/q) by consecutive alternating partial sums."""

    x = Fraction(1, q)
    terms = [(-1) ** n * x ** (2 * n + 1) / (2 * n + 1) for n in range(count)]
    next_term = (-1) ** count * x ** (2 * count + 1) / (2 * count + 1)
    return _alternating_bounds(terms, next_term)


def machin_pi_bounds() -> QInterval:
    """Return a rigorous rational enclosure from pi=16 atan(1/5)-4 atan(1/239)."""

    return 16 * _atan_reciprocal_bounds(5) - 4 * _atan_reciprocal_bounds(239)


def _sin_point_bounds(x: Fraction, count: int = 20) -> QInterval:
    if not (0 <= x <= 1):
        raise VerificationError("small-angle sine called outside [0,1]")
    terms = [(-1) ** n * x ** (2 * n + 1) / _factorial(2 * n + 1) for n in range(count)]
    next_term = (-1) ** count * x ** (2 * count + 1) / _factorial(2 * count + 1)
    return _alternating_bounds(terms, next_term)


def _cos_point_bounds(x: Fraction, count: int = 20) -> QInterval:
    if not (0 <= x <= 1):
        raise VerificationError("small-angle cosine called outside [0,1]")
    terms = [(-1) ** n * x ** (2 * n) / _factorial(2 * n) for n in range(count)]
    next_term = (-1) ** count * x ** (2 * count) / _factorial(2 * count)
    return _alternating_bounds(terms, next_term)


def _factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def _small_angle_sin_cos(u: QInterval) -> tuple[QInterval, QInterval]:
    """Enclose sin and cos on a positive interval contained in [0,1]."""

    if not (0 <= u.lower <= u.upper <= 1):
        raise VerificationError("angle reduction did not reach [0,1]")
    sin_lower = _sin_point_bounds(u.lower).lower
    sin_upper = _sin_point_bounds(u.upper).upper
    cos_lower = _cos_point_bounds(u.upper).lower
    cos_upper = _cos_point_bounds(u.lower).upper
    return QInterval(sin_lower, sin_upper), QInterval(cos_lower, cos_upper)


def _sin_cos_near_pi(t: QInterval, pi: QInterval) -> tuple[QInterval, QInterval]:
    """Enclose sin(t), cos(t) when t is strictly on one side of pi."""

    if t.upper < pi.lower:
        u = pi - t
        sin_u, cos_u = _small_angle_sin_cos(u)
        return sin_u, -cos_u
    if t.lower > pi.upper:
        u = t - pi
        sin_u, cos_u = _small_angle_sin_cos(u)
        return -sin_u, -cos_u
    raise VerificationError("a trigonometric input interval crosses the pi wall")


def _determinant(ell: int, rho: QInterval, k: QInterval, pi: QInterval) -> QInterval:
    """Independent explicit formulas for the first two Riccati determinants."""

    t = (1 - rho) * k
    sin_t, cos_t = _sin_cos_near_pi(t, pi)
    if ell == 0:
        return sin_t
    if ell == 1:
        coefficient_sin = 1 + 1 / (rho * k.square())
        coefficient_cos = (1 - rho) / (rho * k)
        return coefficient_sin * sin_t - coefficient_cos * cos_t
    raise VerificationError(f"independent determinant formula unavailable for ell={ell}")


def _arb_serialized_interval(record: dict[str, Any]) -> QInterval:
    """Interpret the producer's exact ``mid_rad_10exp`` enclosure."""

    try:
        triple = record["enclosure"]["mid_rad_10exp"]
        midpoint = int(triple["midpoint_integer"])
        radius = int(triple["radius_integer"])
        exponent = int(triple["decimal_exponent"])
    except (KeyError, TypeError, ValueError) as exc:
        raise VerificationError("malformed serialized Arb ball") from exc
    if radius < 0:
        raise VerificationError("negative serialized Arb radius")
    scale = Fraction(10**exponent) if exponent >= 0 else Fraction(1, 10 ** (-exponent))
    return QInterval((midpoint - radius) * scale, (midpoint + radius) * scale)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def _decimal(value: Fraction, digits: int = 40) -> str:
    with localcontext() as decimal_context:
        decimal_context.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def _interval_summary(value: QInterval) -> dict[str, str]:
    return {
        "sign": value.sign,
        "lower_display": _decimal(value.lower),
        "upper_display": _decimal(value.upper),
        "display_note": "decimal display only; checker comparisons used exact Fraction endpoints",
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    """Verify the pilot certificate and return a machine-readable PASS report."""

    _require(data.get("schema") == SCHEMA, "unsupported certificate schema")
    verified_hashes = _verify_provenance_hashes(data)
    scope = data.get("scope", {})
    _require(scope.get("zone") == "R_C", "pilot must be an R_C box")
    _require(scope.get("closed_faces") is True, "all target faces must be closed")

    rho_lo, rho_hi = map(_parse_fraction, scope["rho"])
    k_lo, k_hi = map(_parse_fraction, scope["K"])
    _require(rho_lo < rho_hi and k_lo < k_hi, "pilot box must be nondegenerate")
    rho = QInterval(rho_lo, rho_hi)
    k_box = QInterval(k_lo, k_hi)
    pi = machin_pi_bounds()
    _require(Fraction(3) < pi.lower < pi.upper < Fraction(22, 7), "pi enclosure failed")

    # Exact membership in the central residual R_C.
    _require(Fraction(1, 16) <= rho_lo, "rho box lies left of R_C")
    _require(rho_hi <= Fraction(99, 100), "rho box lies right of R_C")
    zero_count_boundary_upper = pi.upper / (1 - rho_hi)
    _require(k_lo > zero_count_boundary_upper, "K box is not above pi/(1-rho)")
    # eta <= 1/pi < 1/2 gives K0 > 4*a_rho = 8*pi*rho/(1-rho).
    coarse_k0_lower = 8 * pi.lower * rho_lo / (1 - rho_lo)
    _require(k_hi < coarse_k0_lower, "K box is not proved below K0")

    angular = data.get("angular_cutoff", {})
    _require(angular.get("largest_possibly_active_ell") == 6, "bad angular maximum")
    _require(angular.get("first_excluded_ell") == 7, "bad angular cutoff")
    _require(Fraction(13, 2) < k_hi < Fraction(15, 2), "angular wall audit failed")

    width_max = 1 - rho_lo
    first_ell_two_lower = (pi.lower / width_max) ** 2 + 6
    second_ell_zero_lower = (2 * pi.lower / width_max) ** 2
    _require(first_ell_two_lower > k_hi**2, "ell>=2 exclusion failed")
    _require(second_ell_zero_lower > k_hi**2, "at-most-one-root bound failed")

    channels = data.get("channels")
    _require(isinstance(channels, list) and len(channels) == 2, "expected ell=0,1 records")
    independent_determinants: dict[str, dict[str, str]] = {}
    weighted_count = 0
    for expected_ell, channel in enumerate(channels):
        ell = channel.get("ell")
        _require(ell == expected_ell, "channels must be exactly ell=0,1 in order")
        multiplicity = channel.get("multiplicity")
        _require(multiplicity == 2 * ell + 1, f"bad multiplicity for ell={ell}")
        root_lower, root_upper = map(_parse_fraction, channel["uniform_root_bracket"])
        _require(root_lower < root_upper < k_lo, f"ell={ell} root bracket meets target box")

        lower_det = _determinant(ell, rho, QInterval.point(root_lower), pi)
        upper_det = _determinant(ell, rho, QInterval.point(root_upper), pi)
        target_det = _determinant(ell, rho, k_box, pi)
        _require(lower_det.sign == "positive", f"ell={ell} lower face sign failed")
        _require(upper_det.sign == "negative", f"ell={ell} upper face sign failed")
        _require(target_det.sign == "negative", f"ell={ell} target box crosses a wall")

        for key, exact_value, expected_sign in (
            ("determinant_lower_face", lower_det, "positive"),
            ("determinant_upper_face", upper_det, "negative"),
            ("determinant_on_target_box", target_det, "negative"),
        ):
            producer_record = channel[key]
            producer_interval = _arb_serialized_interval(producer_record)
            _require(
                producer_record.get("sign") == expected_sign,
                f"ell={ell} producer sign label mismatch",
            )
            _require(
                producer_interval.sign == expected_sign,
                f"ell={ell} serialized Arb enclosure is not {expected_sign}",
            )

        _require(
            channel.get("root_count_below_every_K_in_box") == 1,
            f"ell={ell} must report one root",
        )
        weighted_count += multiplicity
        independent_determinants[f"ell_{ell}_lower_face"] = _interval_summary(lower_det)
        independent_determinants[f"ell_{ell}_upper_face"] = _interval_summary(upper_det)
        independent_determinants[f"ell_{ell}_target_box"] = _interval_summary(target_det)

    strict_count = data.get("strict_count", {})
    _require(weighted_count == 4, "independent weighted count is not 4")
    _require(strict_count.get("weighted_count") == weighted_count, "reported count mismatch")
    _require(strict_count.get("spectral_wall_in_target_box") is False, "spectral wall flag mismatch")

    weyl_lower = 2 * (1 - rho_hi**3) * k_lo**3 / (9 * pi.upper)
    weyl_margin_lower = weyl_lower - weighted_count
    _require(weyl_margin_lower > 0, "Weyl margin is not strictly positive")
    producer_margin = data["weyl"]["right_hand_side_minus_strict_count"]
    _require(producer_margin.get("sign") == "positive", "producer margin label mismatch")
    _require(
        _arb_serialized_interval(producer_margin).sign == "positive",
        "serialized Arb Weyl margin is not positive",
    )

    return {
        "schema": "polya-shell-compact-box-check-report-v0.1",
        "status": "PASS",
        "independent_arithmetic": (
            "Python standard-library Fraction; Machin pi and alternating Taylor enclosures"
        ),
        "scope": scope,
        "checks": {
            "provenance_hashes_verified": True,
            "full_box_inside_R_C": True,
            "angular_cutoff_enforced": True,
            "all_possible_channels_resolved": True,
            "uniform_root_brackets_ell_0_1": True,
            "no_spectral_wall_in_target_box": True,
            "closed_faces_included": True,
        },
        "strict_weighted_count": weighted_count,
        "weyl_lower_display": _decimal(weyl_lower),
        "weyl_margin_lower_display": _decimal(weyl_margin_lower),
        "display_note": "decimal displays are non-decisive; all PASS tests used exact Fractions",
        "pi_enclosure_display": [_decimal(pi.lower), _decimal(pi.upper)],
        "determinant_enclosures": independent_determinants,
        "verified_sha256": verified_hashes,
        "limitations": [
            "PASS applies only to the single closed pilot box.",
            "The result does not cover R_C, R_L, or R_T globally.",
            "The result does not promote COMP-certified-bessel or SHELL-rho-compact.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw = args.input.read_bytes()
    data = json.loads(raw)
    report = verify_certificate(data)
    report["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"PASS; wrote {args.report}")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
