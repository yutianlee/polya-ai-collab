#!/usr/bin/env python3
"""Directed/exact certificate for the Round-08F signed-prefix extension.

The proof is in human/outbox/general-d-round-08f-signed-prefix-terminal.md.
This certificate depends on the frozen Round-08E verifier, whose source
hash is checked before import.  It proves a ratio interval and does not
certify the residual fixed-ratio walls below rho=1847/2000.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


PRIOR_PATH = Path(__file__).with_name(
    "general_d_high_floor_refined_cap_verify.py"
)
PRIOR_SHA256 = "3360878C89DB842FD8695C74C211A3562DBFC84C3E1B4D3CA291DC36BCED39C5"
actual_prior_hash = hashlib.sha256(PRIOR_PATH.read_bytes()).hexdigest().upper()
if actual_prior_hash != PRIOR_SHA256:  # pragma: no cover
    raise SystemExit(
        f"Round-08E verifier hash mismatch: {actual_prior_hash} != {PRIOR_SHA256}"
    )

import general_d_high_floor_refined_cap_verify as prior  # noqa: E402


base = prior.base
ctx.prec = int(os.environ.get("GENERAL_D_ARB_PREC", "512"))
PI = arb.pi()
SQRT2 = arb(2).sqrt()

RHO_MIN = fmpq(1847, 2000)
RHO_MAX = fmpq(927, 1000)
C_BAR = fmpq(627, 5000)
THETA_SQ_BAR = fmpq(311, 2000)
COEFFICIENT_FLOOR = fmpq(689, 500)
LEVEL_DISTANCE_FACTOR = fmpq(149, 50)
RETAINED_RATIO_FLOOR = fmpq(7, 10)
RETAINED_SCALE = fmpq(1043, 500)
COMMON_PREFIX_CONSTANT = fmpq(123, 1000)
LAMBDA_FLOOR = fmpq(1, 4)
W_FLOOR = fmpq(7, 16)
RADIAL_RATIO_CEILING = fmpq(21)
CAP_UPPER = fmpq(1, 6)
SERIES_Z_BAR = fmpq(53193, 200000)
SERIES_QUADRATIC_UPPER = fmpq(3750, 146807)
SERIES_INTEGRATED_UPPER = fmpq(7500, 1027649)
PANELS = 64


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def series_integral_lower(rho: arb, x: fmpq) -> arb:
    """Lower retained integral with V=(149/50)(7/10)x."""
    eps = 1 - rho
    v = A(RETAINED_SCALE * x)
    one_plus = 1 + rho * v

    result = A(fmpq(2, 3)) / rho * (
        base.odd_half_power(one_plus, 3) - 1
    )
    result += eps / (30 * rho) * (
        base.odd_half_power(one_plus, 5) - 1
    )
    result += (
        A(fmpq(3, 560))
        * eps
        * eps
        / rho
        * (base.odd_half_power(one_plus, 7) - 1)
    )
    result -= A(fmpq(2, 3)) * base.odd_half_power(v, 3)
    result -= eps / 30 * base.odd_half_power(v, 5)
    result -= (
        A(SERIES_INTEGRATED_UPPER)
        * eps
        * eps
        * base.odd_half_power(v, 7)
    )
    return result


def main() -> None:
    print("GENERAL-d HIGH-FLOOR SIGNED-PREFIX CERTIFICATE (ROUND 08F)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print(f"Round-08E verifier SHA256={actual_prior_hash}")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    theta0 = rho0.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 <311/2000 failed")
    require(theta0 / PI < A(C_BAR), "c <627/5000 failed")
    require(THETA_SQ_BAR < fmpq(4, 25), "theta<2/5 reduction failed")
    print("PASS ratio endpoint: theta^2<311/2000, c<627/5000, theta<2/5")

    # Round 08E's p=0 reduction gives q>=5/2 on a negative candidate.
    cap_endpoint = prior.prior.g_radius(A(fmpq(7, 2)), A(fmpq(5, 2)))
    require(cap_endpoint < A(CAP_UPPER), "G_(7/2)(5/2)<1/6 failed")
    print("PASS inherited refined terminal cap: G_(7/2)(5/2)<1/6")

    # Since rho<=927/1000, epsilon>=73/1000.  The elementary lower
    # bound lambda>(2sqrt(2)/3)sqrt(epsilon) gives lambda>1/4.
    lambda_square_gap = (
        fmpq(8, 9) * fmpq(73, 1000) - LAMBDA_FLOOR**2
    )
    require(
        lambda_square_gap == fmpq(43, 18000),
        "lambda square gap changed",
    )
    require(lambda_square_gap > 0, "lambda>1/4 failed")
    require(fmpq(7, 4) * LAMBDA_FLOOR == W_FLOOR, "W floor changed")

    # R_rho=c*mu/W=theta*rho/(lambda*epsilon).  The rational endpoint
    # bounds make R_rho<7416/365<21.
    radial_upper = (
        fmpq(2, 5)
        * fmpq(927, 1000)
        / (LAMBDA_FLOOR * fmpq(73, 1000))
    )
    require(radial_upper == fmpq(7416, 365), "radial ratio changed")
    require(radial_upper < RADIAL_RATIO_CEILING, "radial ratio <21 failed")
    print("PASS active width and signed-prefix geometry:")
    print("  lambda>1/4, W>7/16, c*mu/W<7416/365<21")

    # For beta=123/1000-c>=0, use M>=delta/c.  The four terminal
    # ledgers decrease up to beta=0, c=123/1000.
    c_split = COMMON_PREFIX_CONSTANT
    beta_split = COMMON_PREFIX_CONSTANT - c_split
    d_split = 1 - 2 * c_split
    require(beta_split == 0, "positive-prefix split changed")
    positive_b0 = (
        beta_split
        + (fmpq(1, 2) - c_split)
        - fmpq(7, 6) * c_split
        - c_split * d_split / 2
    )
    positive_q0 = (
        beta_split * (fmpq(7, 4) - W_FLOOR)
        - c_split / 2
        + c_split**2
        + W_FLOOR**2
    )
    positive_q1_upper = (
        fmpq(1371, 2000) - fmpq(5, 2) * c_split + c_split**2
    )
    positive_q1_lower = (
        fmpq(1371, 2000)
        - fmpq(2377, 1000) * c_split
        - c_split**2
    )
    require(positive_b0 == fmpq(187129, 1000000), "positive B0 mismatch")
    require(positive_q0 == fmpq(580141, 4000000), "positive Q0 mismatch")
    require(
        positive_q1_upper == fmpq(393129, 1000000),
        "positive Q1 upper mismatch",
    )
    require(positive_q1_lower == fmpq(189, 500), "positive Q1 lower mismatch")
    require(
        min(positive_b0, positive_q0, positive_q1_upper, positive_q1_lower)
        > 0,
        "positive-prefix terminal ledger failed",
    )

    # For beta<0, M<=mu and c*mu/W<21 give
    # cP>21*beta*W-cd/2.  Use W<=B0+3/4 on B0>=1.
    beta_bar = COMMON_PREFIX_CONSTANT - C_BAR
    dbar = 1 - 2 * C_BAR
    require(beta_bar == -fmpq(3, 1250), "negative beta endpoint changed")
    b0_coefficient = (
        fmpq(1, 2) - C_BAR + RADIAL_RATIO_CEILING * beta_bar
    )
    require(b0_coefficient == fmpq(1621, 5000), "B0 coefficient changed")
    require(b0_coefficient > 0, "negative-prefix B0 coefficient failed")
    negative_b0 = (
        b0_coefficient
        + fmpq(3, 4) * RADIAL_RATIO_CEILING * beta_bar
        - fmpq(7, 6) * C_BAR
        - C_BAR * dbar / 2
    )
    negative_q0 = (
        W_FLOOR**2
        + RADIAL_RATIO_CEILING * beta_bar * W_FLOOR
        - C_BAR * dbar / 2
    )

    def negative_q1(width: fmpq) -> fmpq:
        return (
            fmpq(3, 2) * width
            - width**2
            - C_BAR
            + RADIAL_RATIO_CEILING * beta_bar * width
            - C_BAR * dbar / 2
        )

    negative_q1_upper = negative_q1(fmpq(3, 4))
    negative_q1_lower = negative_q1(fmpq(3, 4) - C_BAR)
    q0_derivative = (
        2 * W_FLOOR + RADIAL_RATIO_CEILING * beta_bar
    )
    require(q0_derivative == fmpq(4123, 5000), "Q0 derivative changed")
    require(q0_derivative > 0, "negative-prefix Q0 monotonicity failed")
    require(
        negative_b0 == fmpq(2328129, 25000000),
        "negative B0 mismatch",
    )
    require(
        negative_q0 == fmpq(12238141, 100000000),
        "negative Q0 mismatch",
    )
    require(
        negative_q1_upper == fmpq(8808129, 25000000),
        "negative Q1 upper mismatch",
    )
    require(
        negative_q1_lower == fmpq(2143251, 6250000),
        "negative Q1 lower mismatch",
    )
    require(
        min(negative_b0, negative_q0, negative_q1_upper, negative_q1_lower)
        > 0,
        "negative-prefix terminal ledger failed",
    )
    print("PASS signed delta>=1 terminal ledgers:")
    print(
        "  beta>=0 minima: "
        f"{positive_b0}, {positive_q0}, "
        f"{positive_q1_upper}, {positive_q1_lower}"
    )
    print(
        "  beta<0 minima: "
        f"{negative_b0}, {negative_q0}, "
        f"{negative_q1_upper}, {negative_q1_lower}"
    )

    # Improve the small-delta level distance from 3y/c to (149/50)y/c.
    # First certify kappa_rho=Phi/(theta*rho*epsilon)>7/10.
    tbar = THETA_SQ_BAR
    retained_numerator = fmpq(1, 3) - tbar / 30
    retained_denominator = fmpq(927, 1000) * (
        fmpq(1, 2) - tbar / 24 + tbar**2 / 720
    )
    retained_quotient = retained_numerator / retained_denominator
    require(
        retained_quotient == fmpq(105008000000, 146407982263),
        "retained-ratio quotient changed",
    )
    require(
        retained_quotient - RETAINED_RATIO_FLOOR
        == fmpq(25224124159, 1464079822630),
        "retained-ratio gap changed",
    )
    require(retained_quotient > RETAINED_RATIO_FLOOR, "retained ratio failed")
    require(
        tbar**2 - 20 * tbar - 60 < 0,
        "retained-ratio monotonicity failed",
    )

    coefficient_numerator = A(fmpq(1, 2) - tbar / 24)
    coefficient_denominator = A(
        fmpq(1, 3) - tbar / 30 + tbar**2 / 840
    )
    coefficient_lower = (
        rho0
        * SQRT2
        * base.odd_half_power(coefficient_numerator, 3)
        / coefficient_denominator
    )
    require(
        coefficient_lower > A(COEFFICIENT_FLOOR),
        "scaled integral coefficient <=689/500",
    )
    u_upper = (
        LEVEL_DISTANCE_FACTOR
        * fmpq(5, 9)
        * tbar
        / RHO_MIN
    )
    require(u_upper == fmpq(46339, 166230), "u0 upper changed")
    require(u_upper < fmpq(279, 1000), "u0<279/1000 failed")
    require(
        LEVEL_DISTANCE_FACTOR * RETAINED_RATIO_FLOOR
        == RETAINED_SCALE,
        "retained scale changed",
    )

    eps_max = 1 - RHO_MIN
    v_max = RETAINED_SCALE * fmpq(5, 3)
    require(v_max == fmpq(1043, 300), "retained V maximum changed")
    z_upper = eps_max * v_max
    require(z_upper == SERIES_Z_BAR, "subtracted z upper changed")
    tail_upper = fmpq(3, 160) / (1 - SERIES_Z_BAR)
    require(
        tail_upper == SERIES_QUADRATIC_UPPER,
        "quadratic arccos tail changed",
    )
    require(
        SERIES_QUADRATIC_UPPER * fmpq(2, 7)
        == SERIES_INTEGRATED_UPPER,
        "integrated arccos tail changed",
    )
    first_copy_z = eps_max * (1 + v_max)
    require(first_copy_z == fmpq(68493, 200000), "first-copy z changed")
    require(first_copy_z < 1, "positive arccos series left its domain")
    print("PASS improved level-distance constants:")
    print("  Phi/(theta*rho*epsilon)>7/10; T<(149/50)y/c")
    print("  coefficient>689/500, u0<279/1000")
    print(
        "  z<=53193/200000; tail=3750/146807; "
        "integrated=7500/1027649"
    )

    smallest = float("inf")
    smallest_integral = float("inf")
    for endpoint in (fmpq(1, 7), fmpq(5, 3)):
        for panel in range(PANELS):
            lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, PANELS)
            hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, PANELS)
            rho = base.interval_ball(lo, hi)
            integral = series_integral_lower(rho, endpoint)
            margin = A(COEFFICIENT_FLOOR) * integral - A(endpoint)
            require(base.lower(integral) > 0, "series integral was not positive")
            require(base.lower(margin) > 0, "level-distance endpoint failed")
            smallest_integral = min(
                smallest_integral, float(base.lower(integral))
            )
            smallest = min(smallest, float(base.lower(margin)))
    print(
        "PASS level-distance band: 128 directed endpoint panels; "
        f"minimum lower margin={smallest:.12g}"
    )
    print(f"  minimum retained-integral lower bound={smallest_integral:.12g}")

    small_delta = (
        fmpq(5, 4)
        - fmpq(5, 16) * LEVEL_DISTANCE_FACTOR
        - fmpq(8, 3) * C_BAR
        + C_BAR**2
    )
    require(
        small_delta == fmpq(1879, 25000000),
        "small-delta polynomial changed",
    )
    require(small_delta > 0, "small-delta ledger failed")
    print(f"PASS small-delta scalar ledger: c*S>{small_delta}")

    eta0 = base.g(rho0)
    require(eta0 > A(fmpq(1, 158)), "eta(rho0)>1/158 failed")
    require(base.g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(2) * fmpq(355, 113) * fmpq(1847, 153)
    require(a_upper == fmpq(1311370, 17289), "a upper changed")
    combined = a_upper + fmpq(13, 45)
    require(combined == fmpq(2193941, 28815), "numerator sum changed")
    require(combined < 77, "fixed-ratio numerator bound failed")
    cutoff = 77 * 158**2
    require(cutoff == 1922228, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/158, eta<1/9, a+2*eta*C_*<77")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 3844455, "2r range arithmetic failed")
    require(cutoff - 1 == 1922227, "n range arithmetic failed")
    f_upper = fmpq(cutoff, 3) + fmpq(1, 4)
    require(
        fmpq(640742) < f_upper < fmpq(640743),
        "f,B range arithmetic failed",
    )
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("1847/2000 <= rho <= 927/1000; Round 08E covers larger rho.")
    print("Residual fixed-ratio walls with rho<1847/2000 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
