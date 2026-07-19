#!/usr/bin/env python3
"""Directed/exact certificate for the Round-08E refined-cap extension.

The proof is in human/outbox/general-d-round-08e-refined-cap-terminal.md.
This certificate depends on the frozen Round-08D verifier, whose source
hash is checked before import.  It proves a ratio interval and does not
certify the residual fixed-ratio walls below rho=927/1000.
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
    "general_d_high_floor_sharp_cap_verify.py"
)
PRIOR_SHA256 = "8E025183DC6F2AFCE4E51F404F5AC7830185FCA1B22B2DF0184D1204E4D91BF6"
actual_prior_hash = hashlib.sha256(PRIOR_PATH.read_bytes()).hexdigest().upper()
if actual_prior_hash != PRIOR_SHA256:  # pragma: no cover
    raise SystemExit(
        f"Round-08D verifier hash mismatch: {actual_prior_hash} != {PRIOR_SHA256}"
    )

import general_d_high_floor_sharp_cap_verify as prior  # noqa: E402


base = prior.base
ctx.prec = int(os.environ.get("GENERAL_D_ARB_PREC", "512"))
PI = arb.pi()
SQRT2 = arb(2).sqrt()

RHO_MIN = fmpq(927, 1000)
RHO_MAX = fmpq(93, 100)
C_BAR = fmpq(49, 400)
THETA_SQ_BAR = fmpq(37, 250)
COEFFICIENT_FLOOR = fmpq(173, 125)
ABSENT_CHORD_COEFFICIENT = fmpq(377, 1000)
COMMON_PREFIX_CONSTANT = fmpq(123, 1000)
LAMBDA_FLOOR = fmpq(249, 1000)
W_FLOOR = fmpq(1743, 4000)
CAP_UPPER = fmpq(1, 6)
SERIES_Z_BAR = fmpq(73, 300)
SERIES_QUADRATIC_UPPER = fmpq(45, 1816)
SERIES_INTEGRATED_UPPER = fmpq(45, 6356)
PANELS = 64


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def series_integral_lower(rho: arb, x: fmpq) -> arb:
    """Lower retained integral after u=(1-rho)v and V=2x."""
    eps = 1 - rho
    v = A(2 * x)
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
    print("GENERAL-d HIGH-FLOOR REFINED-CAP CERTIFICATE (ROUND 08E)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print(f"Round-08D verifier SHA256={actual_prior_hash}")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    theta0 = rho0.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 < 37/250 failed")
    require(theta0 / PI < A(C_BAR), "c < 49/400 failed")
    require(C_BAR < COMMON_PREFIX_CONSTANT, "common prefix is not positive")
    print("PASS ratio endpoint: theta^2<37/250 and c<49/400<123/1000")

    # For a in [0,1/4], sharpen the absent-level endpoint chord from
    # 19/50 to 377/1000.  With a=y/4, the following is the exact power
    # polynomial for
    #   b(a)^2-(1/2-a)^2(1+a)^2*a*(2+a),
    # where b=377/1000-(1/2-a)(2a+a^2).
    absent_gap_power = [
        fmpq(142129, 1000000),
        -fmpq(627, 2000),
        fmpq(2881, 16000),
        -fmpq(123, 32000),
        -fmpq(1, 256),
    ]
    absent_coeffs = base.bernstein_coefficients(absent_gap_power, 48)
    require(
        min(absent_coeffs) == fmpq(7422203, 77832000000),
        "refined absent-level Bernstein minimum changed",
    )
    b_at_quarter = fmpq(377, 1000) - fmpq(1, 4) + fmpq(3, 32) + fmpq(1, 64)
    require(b_at_quarter == fmpq(1891, 8000), "b(1/4) changed")
    require(b_at_quarter > 0, "squaring sign for absent chord failed")
    require(fmpq(1, 8) > COMMON_PREFIX_CONSTANT, "present prefix comparison failed")
    print("PASS refined absent-level chord:")
    print("  coefficient<377/1000; degree-48 Bernstein minimum")
    print(f"  {min(absent_coeffs)}; common prefix=(123/1000-c)*delta-cd/2")

    # On this band epsilon>=7/100.  The elementary active-width lower
    # bound lambda>(2 sqrt(2)/3)sqrt(epsilon) gives lambda>249/1000.
    lambda_square_gap = (
        fmpq(8, 9) * fmpq(7, 100) - LAMBDA_FLOOR * LAMBDA_FLOOR
    )
    require(
        lambda_square_gap == fmpq(1991, 9000000),
        "active-width lambda square gap changed",
    )
    require(lambda_square_gap > 0, "active-width lambda >249/1000 failed")
    require(fmpq(7, 4) * LAMBDA_FLOOR == W_FLOOR, "W floor changed")
    print("PASS active-width ledger: lambda>249/1000 and W>1743/4000")

    # A negative candidate cannot have p=0.  Hence p>=1, n>=2, and
    # q=r+n>=5/2.  The analytic proof shows G_{q+1}(q) decreases in q.
    cap_endpoint = prior.g_radius(A(fmpq(7, 2)), A(fmpq(5, 2)))
    require(cap_endpoint < A(CAP_UPPER), "G_(7/2)(5/2) < 1/6 failed")
    print("PASS refined terminal cap: G_(7/2)(5/2)<1/6")

    tbar = THETA_SQ_BAR
    monotonicity_gap = 84 + 10 * tbar - tbar * tbar / 2
    require(monotonicity_gap > 0, "coefficient monotonicity failed")
    numerator = A(fmpq(1, 2) - tbar / 24)
    denominator = A(fmpq(1, 3) - tbar / 30 + tbar * tbar / 840)
    coefficient_lower = (
        rho0 * SQRT2 * base.odd_half_power(numerator, 3) / denominator
    )
    require(
        coefficient_lower > A(COEFFICIENT_FLOOR),
        "scaled integral coefficient <=173/125",
    )

    u_upper = fmpq(5, 3) * tbar / RHO_MIN
    require(u_upper == fmpq(740, 2781), "unexpected t0/mu upper bound")
    require(u_upper < fmpq(267, 1000), "t0/mu <267/1000 failed")
    eps_max = 1 - RHO_MIN
    z_upper = eps_max * fmpq(10, 3)
    require(z_upper == SERIES_Z_BAR, "subtracted z upper bound changed")
    tail_upper = fmpq(3, 160) / (1 - SERIES_Z_BAR)
    require(
        tail_upper == SERIES_QUADRATIC_UPPER,
        "quadratic arccos tail coefficient changed",
    )
    require(
        SERIES_QUADRATIC_UPPER * fmpq(2, 7)
        == SERIES_INTEGRATED_UPPER,
        "integrated arccos tail coefficient changed",
    )
    first_copy_z = eps_max * fmpq(13, 3)
    require(first_copy_z == fmpq(949, 3000), "first-copy z bound changed")
    require(first_copy_z < 1, "positive arccos series left its domain")
    print("PASS retuned arccos constants:")
    print("  coefficient>173/125, u0<267/1000")
    print("  subtracted z<=73/300; tail=45/1816; integrated=45/6356")
    print("  positive first-copy argument <=949/3000")

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

    beta = COMMON_PREFIX_CONSTANT - C_BAR
    dbar = 1 - 2 * C_BAR
    require(beta == fmpq(1, 2000), "endpoint common-prefix coefficient changed")
    require(2 * W_FLOOR > COMMON_PREFIX_CONSTANT, "Q=0 W monotonicity failed")

    b0_positive = (
        beta + (fmpq(1, 2) - C_BAR)
        - fmpq(7, 6) * C_BAR
        - C_BAR * dbar / 2
    )
    q_zero = (
        beta * (fmpq(7, 4) - W_FLOOR)
        - C_BAR / 2
        + C_BAR**2
        + W_FLOOR**2
    )
    q_one_upper = fmpq(1371, 2000) - fmpq(5, 2) * C_BAR + C_BAR**2
    q_one_lower = fmpq(1371, 2000) - fmpq(2377, 1000) * C_BAR - C_BAR**2
    small_delta = fmpq(5, 16) - fmpq(8, 3) * C_BAR + C_BAR**2

    require(b0_positive == fmpq(90643, 480000), "B0>=1 mismatch")
    require(q_zero == fmpq(2308663, 16000000), "B0=Q=0 mismatch")
    require(q_one_upper == fmpq(63081, 160000), "Q=1 upper mismatch")
    require(q_one_lower == fmpq(303449, 800000), "Q=1 lower mismatch")
    require(small_delta == fmpq(403, 480000), "small-delta mismatch")
    require(
        min(b0_positive, q_zero, q_one_upper, q_one_lower, small_delta) > 0,
        "scalar ledger failed",
    )
    print("PASS exact scalar ledgers at c=49/400:")
    print(f"  delta>=1, B0>=1: c*S > {b0_positive}")
    print(f"  delta>=1, B0=0, Q=0: c*S > {q_zero}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4: > {q_one_upper}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4-c: > {q_one_lower}")
    print(f"  0<delta<1 with cap<1/6: c*S > {small_delta}")

    eta0 = base.g(rho0)
    require(eta0 > A(fmpq(1, 169)), "eta(rho0)>1/169 failed")
    require(base.g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(2) * fmpq(355, 113) * fmpq(927, 73)
    require(a_upper == fmpq(658170, 8249), "a upper bound changed")
    combined = a_upper + fmpq(13, 45)
    require(combined == fmpq(29724887, 371205), "numerator sum changed")
    require(combined < 81, "fixed-ratio numerator bound failed")
    cutoff = 81 * 169**2
    require(cutoff == 2313441, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/169, eta<1/9, a+2*eta*C_*<81")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 4626881, "2r range arithmetic failed")
    require(cutoff - 1 == 2313440, "n range arithmetic failed")
    f_upper = fmpq(cutoff, 3) + fmpq(1, 4)
    require(
        fmpq(771147) < f_upper < fmpq(771148),
        "f,B range arithmetic failed",
    )
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("927/1000 <= rho <= 93/100; Round 08D covers larger rho.")
    print("Residual fixed-ratio walls with rho<927/1000 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
