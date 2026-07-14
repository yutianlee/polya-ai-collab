#!/usr/bin/env python3
"""Certified point classifier for the promoted Round 16 analytic mask.

The mathematical mask is the exact Boolean union recorded in the frozen
Round 17 packet.  Rational comparisons are performed exactly.  Comparisons
against pi, omega_0, rho_*, H_0, and K_0 use Arb balls with precision
escalation and are accepted only when the sign is certified.  An unresolved
ball produces ``indeterminate`` rather than a guessed classification.

This module classifies parameter points.  It does not prove a new analytic
lemma, certify a spectral count, or infer topology from sampled points.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Callable, Iterable

try:
    from flint import arb, ctx
except ImportError as exc:  # pragma: no cover - CLI dependency message
    raise SystemExit(
        "python-flint is required; install computations/requirements-round8-certified.txt"
    ) from exc


SCHEMA = "polya-shell-round17-residual-mask-v0.1"
PRECISIONS = (128, 256, 512, 1024, 2048)

RHO_COARSE = Fraction(1, 16)
RHO_HALF = Fraction(1, 2)
RHO_SEAM = Fraction(5, 6)
RHO_THIN = Fraction(7, 8)
GLOBAL_K = Fraction(295**2)

B0_RHO_LO = Fraction(999, 2000)
B0_RHO_HI = Fraction(1001, 2000)
B0_K_LO = Fraction(67, 10)
B0_K_HI = Fraction(168, 25)


class IndeterminateComparison(RuntimeError):
    """Raised only when a caller explicitly requires a decided sign."""


@dataclass(frozen=True)
class SignRecord:
    label: str
    sign: int | None
    precision_bits: int
    enclosure: str


@dataclass(frozen=True)
class PointClassification:
    schema: str
    rho: str
    K: str
    status: str
    analytic_reasons: tuple[str, ...]
    certified_reasons: tuple[str, ...]
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[SignRecord, ...]


def qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid rational {text!r}") from exc


def qball(value: Fraction | int) -> arb:
    return arb(qtext(Fraction(value)))


def g1(value: arb) -> arb:
    return ((1 - value * value).sqrt() - value * value.acos()) / arb.pi()


def constants() -> tuple[arb, arb, arb, arb]:
    pi = arb.pi()
    sqrt2 = qball(2).sqrt()
    omega0 = qball(3).sqrt() / (2 * pi) - qball(Fraction(1, 6))
    c_star = qball(Fraction(1, 2)) + 8 * sqrt2 / 15
    c0 = qball(1) + 8 * sqrt2 / 15
    rho_star = omega0 / (1 + 2 * c_star)
    return omega0, c_star, c0, rho_star


def k0_ball(rho: Fraction) -> arb:
    if not (0 < rho < 1):
        raise ValueError("K_0 requires 0 < rho < 1")
    _, _, c0, _ = constants()
    r = qball(rho)
    eta_argument = qball(max(rho, RHO_HALF))
    eta = g1(eta_argument)
    a = 2 * arb.pi() * r / (1 - r)
    y = (a.sqrt() + (a + 4 * eta * c0).sqrt()) / (2 * eta)
    return y * y


def h0_ball(rho: Fraction) -> arb:
    omega0, c_star, _, _ = constants()
    return c_star / (omega0 - qball(rho))


def hk_switch_polynomial_ball(rho: Fraction) -> arb:
    """Cubic whose unique root in (rho_*, omega_0) has H_0=K_0.

    After substituting H_0=C_*/(omega_0-rho) into the fixed-ratio root
    equation and squaring on rho>rho_*, the equality H_0=K_0 becomes

        (1-rho)(C_0 rho-omega_0/2)^2
        -2 pi C_* rho(omega_0-rho)=0.

    The packet records the sign condition and strict-convexity proof that
    make this transformation reversible and the root unique.
    """

    omega0, c_star, c0, _ = constants()
    r = qball(rho)
    return (1 - r) * (c0 * r - omega0 / 2) ** 2 - (
        2 * arb.pi() * c_star * r * (omega0 - r)
    )


def certified_sign(label: str, builder: Callable[[], arb]) -> SignRecord:
    previous_precision = ctx.prec
    try:
        last: arb | None = None
        for precision in PRECISIONS:
            ctx.prec = precision
            value = builder()
            last = value
            if value > 0:
                return SignRecord(label, 1, precision, value.str(20, radius=True))
            if value < 0:
                return SignRecord(label, -1, precision, value.str(20, radius=True))
        assert last is not None
        return SignRecord(label, None, PRECISIONS[-1], last.str(30, radius=True))
    finally:
        ctx.prec = previous_precision


def _inside_b0(rho: Fraction, k: Fraction) -> bool:
    return B0_RHO_LO <= rho <= B0_RHO_HI and B0_K_LO <= k <= B0_K_HI


def _mask_manifest() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "ratio_interval": ["rho_*", "7/8"],
        "frequency_domain": "K>=0",
        "analytic_rules": [
            {
                "id": "rho-star-endpoint",
                "condition": "rho=rho_*",
                "faces": "all K>=0; included",
            },
            {
                "id": "rho-one-endpoint-round16",
                "condition": "rho=7/8",
                "faces": "all K>=0; included",
            },
            {
                "id": "high-angular",
                "condition": "2*rho*K<=1",
                "faces": "equality included",
            },
            {
                "id": "phase-zero",
                "condition": "(1-rho)*K<=pi",
                "faces": "equality included",
            },
            {
                "id": "small-hole-low-interface",
                "condition": "rho<omega_0 and K*(omega_0-rho)>=C_*",
                "faces": "K threshold included; rho=omega_0 excluded",
            },
            {
                "id": "fixed-rho-high-energy",
                "condition": "K>=K_0(rho)",
                "faces": "equality included; eta formula switches at rho=1/2",
            },
            {
                "id": "central-thin-seam-54",
                "condition": "0<1-rho<=1/6 and K*(1-rho)^2>=54",
                "faces": "all equalities included",
            },
            {
                "id": "retained-seam-32",
                "condition": "0<1-rho<=1/8 and K*(1-rho)^2>=32",
                "faces": "inside I16 only at rho=7/8; included",
            },
            {
                "id": "retained-seam-24",
                "condition": "0<1-rho<=1/10 and K*(1-rho)^2>=24",
                "faces": "empty intersection with I16",
            },
            {
                "id": "retained-seam-20",
                "condition": "0<1-rho<=1/25 and K*(1-rho)^2>=20",
                "faces": "empty intersection with I16",
            },
            {
                "id": "round16-global-envelope",
                "condition": "K>=295^2=87025",
                "faces": "equality included; redundant in primitive union",
            },
        ],
        "analytic_residual": {
            "name": "D16",
            "formula": "(I16 x [0,infinity)) minus A16",
            "normalized": "rho_*<rho<7/8 and L(rho)<K<U(rho)",
            "lower": "L=max(1/(2rho),pi/(1-rho))",
            "upper": (
                "U=min(K0(rho), H0(rho) when rho<omega0, "
                "54/(1-rho)^2 when rho>=5/6)"
            ),
        },
        "certified_overlay": {
            "name": "B0",
            "rho": ["999/2000", "1001/2000"],
            "K": ["67/10", "168/25"],
            "faces": "closed",
            "uncovered_formula": "U16=D16 minus B0",
        },
        "interfaces": [
            "rho=rho_*",
            "rho=1/16 (coarse only)",
            "rho=rho_HK, unique H0=K0 switch in (9407/100000,94071/1000000)",
            "rho=omega_0 (small-hole open face)",
            "rho=1/(1+2*pi) (lower-wall crossover)",
            "rho=1/2 (K0 formula interface)",
            "rho=5/6 (seam begins inclusively)",
            "rho=7/8 (complete endpoint)",
        ],
    }


def classify_point(rho: Fraction, k: Fraction) -> PointClassification:
    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    records: list[SignRecord] = []
    unresolved: list[str] = []
    analytic: list[str] = []
    certified: list[str] = []

    rho_star_sign = certified_sign(
        "rho-rho_*", lambda: qball(rho) - constants()[3]
    )
    records.append(rho_star_sign)
    if rho_star_sign.sign == -1 or rho > RHO_THIN:
        return PointClassification(
            SCHEMA,
            qtext(rho),
            qtext(k),
            "outside_I16",
            tuple(),
            tuple(),
            tuple(unresolved),
            tuple(records),
        )
    if rho_star_sign.sign is None:
        # Membership in I16 is a mandatory conjunction, so a true analytic
        # disjunct cannot override an unresolved lower-interval comparison.
        # Fail closed before evaluating the coverage union.
        unresolved.append(rho_star_sign.label)
        return PointClassification(
            SCHEMA,
            qtext(rho),
            qtext(k),
            "indeterminate",
            tuple(),
            tuple(),
            tuple(unresolved),
            tuple(records),
        )

    if rho_star_sign.sign == 0:
        analytic.append("rho-star-endpoint")

    if rho == RHO_THIN:
        analytic.append("rho-one-endpoint-round16")

    if 2 * rho * k <= 1:
        analytic.append("high-angular")

    zero_sign = certified_sign(
        "pi-(1-rho)K",
        lambda: arb.pi() - qball((1 - rho) * k),
    )
    records.append(zero_sign)
    if zero_sign.sign == 1:
        analytic.append("phase-zero")
    elif zero_sign.sign is None:
        unresolved.append(zero_sign.label)

    omega_sign = certified_sign(
        "rho-omega_0", lambda: qball(rho) - constants()[0]
    )
    records.append(omega_sign)
    if omega_sign.sign == -1:
        small_sign = certified_sign(
            "K(omega_0-rho)-C_*",
            lambda: qball(k) * (constants()[0] - qball(rho)) - constants()[1],
        )
        records.append(small_sign)
        if small_sign.sign == 1:
            analytic.append("small-hole-low-interface")
        elif small_sign.sign is None:
            unresolved.append(small_sign.label)
    elif omega_sign.sign is None:
        unresolved.append(omega_sign.label)

    fixed_sign = certified_sign(
        "K-K_0(rho)", lambda: qball(k) - k0_ball(rho)
    )
    records.append(fixed_sign)
    if fixed_sign.sign == 1:
        analytic.append("fixed-rho-high-energy")
    elif fixed_sign.sign is None:
        unresolved.append(fixed_sign.label)

    epsilon = 1 - rho
    scaled = k * epsilon * epsilon
    if 0 < epsilon <= Fraction(1, 6) and scaled >= 54:
        analytic.append("central-thin-seam-54")
    if 0 < epsilon <= Fraction(1, 8) and scaled >= 32:
        analytic.append("retained-seam-32")
    if 0 < epsilon <= Fraction(1, 10) and scaled >= 24:
        analytic.append("retained-seam-24")
    if 0 < epsilon <= Fraction(1, 25) and scaled >= 20:
        analytic.append("retained-seam-20")
    if k >= GLOBAL_K:
        analytic.append("round16-global-envelope")

    if _inside_b0(rho, k):
        certified.append("round8-certified-pilot-B0")

    if analytic:
        status = "analytic_covered"
    elif unresolved:
        status = "indeterminate"
    elif certified:
        status = "certified_only"
    else:
        status = "analytic_residual_uncovered"

    return PointClassification(
        SCHEMA,
        qtext(rho),
        qtext(k),
        status,
        tuple(analytic),
        tuple(certified),
        tuple(unresolved),
        tuple(records),
    )


def _require_status(rho: Fraction, k: Fraction, status: str) -> None:
    result = classify_point(rho, k)
    if result.status != status:
        raise AssertionError(
            f"({qtext(rho)}, {qtext(k)}): expected {status}, obtained "
            f"{result.status}; analytic={result.analytic_reasons}; "
            f"unresolved={result.unresolved_comparisons}"
        )


def self_check() -> list[str]:
    passed: list[str] = []

    result = classify_point(Fraction(1, 16), Fraction(8))
    assert result.status == "analytic_covered" and "high-angular" in result.analytic_reasons
    passed.append("inclusive high-angular face at rho=1/16")

    _require_status(Fraction(1, 16), Fraction(9), "analytic_residual_uncovered")
    passed.append("small-hole coarse-band interior residual")

    result = classify_point(Fraction(1, 16), Fraction(27))
    assert "small-hole-low-interface" in result.analytic_reasons
    passed.append("H0 branch continues through rho=1/16")

    _require_status(Fraction(1, 10), Fraction(80), "analytic_residual_uncovered")
    passed.append("H0/K0 overlap gap diagnostic point")

    result = classify_point(Fraction(1, 10), Fraction(90))
    assert "fixed-rho-high-energy" in result.analytic_reasons
    passed.append("fixed-rho upper ray")

    left_switch = certified_sign(
        "P_HK(9407/100000)",
        lambda: hk_switch_polynomial_ball(Fraction(9407, 100000)),
    )
    right_switch = certified_sign(
        "P_HK(94071/1000000)",
        lambda: hk_switch_polynomial_ball(Fraction(94071, 1000000)),
    )
    left_in_domain = certified_sign(
        "9407/100000-rho_*",
        lambda: qball(Fraction(9407, 100000)) - constants()[3],
    )
    right_in_domain = certified_sign(
        "omega_0-94071/1000000",
        lambda: constants()[0] - qball(Fraction(94071, 1000000)),
    )
    assert left_switch.sign == -1 and right_switch.sign == 1
    assert left_in_domain.sign == 1 and right_in_domain.sign == 1
    passed.append("certified rational bracket for unique H0=K0 switch")

    _require_status(Fraction(1, 2), Fraction(67, 10), "certified_only")
    passed.append("Round 8 pilot is certified overlay, not analytic mask")

    _require_status(Fraction(5, 6), Fraction(1943), "analytic_residual_uncovered")
    passed.append("point immediately below seam threshold")

    result = classify_point(Fraction(5, 6), Fraction(1944))
    assert "central-thin-seam-54" in result.analytic_reasons
    passed.append("inclusive rho=5/6 seam threshold")

    result = classify_point(Fraction(7, 8), Fraction(0))
    assert "rho-one-endpoint-round16" in result.analytic_reasons
    passed.append("complete rho=7/8 endpoint")

    result = classify_point(Fraction(3, 4), GLOBAL_K)
    assert "round16-global-envelope" in result.analytic_reasons
    passed.append("inclusive K=295^2 global face")

    _require_status(Fraction(1, 100), Fraction(1), "outside_I16")
    passed.append("outside lower residual interval")
    return passed


def _point_argument(text: str) -> tuple[Fraction, Fraction]:
    try:
        rho_text, k_text = text.split(",", maxsplit=1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("point must be RHO,K") from exc
    return parse_fraction(rho_text), parse_fraction(k_text)


def _serialize(result: PointClassification) -> dict[str, object]:
    data = asdict(result)
    data["sign_records"] = [asdict(record) for record in result.sign_records]
    return data


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--point", action="append", type=_point_argument, default=[])
    args = parser.parse_args(list(argv) if argv is not None else None)

    payload: dict[str, object] = {"schema": SCHEMA}
    if args.manifest:
        payload["manifest"] = _mask_manifest()
    if args.self_check or (not args.manifest and not args.point):
        passed = self_check()
        payload["self_check"] = {"status": "PASS", "checks": passed}
    if args.point:
        payload["points"] = [_serialize(classify_point(rho, k)) for rho, k in args.point]
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
