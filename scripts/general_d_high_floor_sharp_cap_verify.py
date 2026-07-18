#!/usr/bin/env python3
"""Directed/exact certificate for the Round-08D sharp-cap extension.

The proof is in human/outbox/general-d-round-08d-sharp-cap-terminal.md.
This certificate depends on the frozen Round-08C helper implementation,
whose source hash is checked before import.  It proves a ratio interval
and does not certify the residual fixed-ratio walls below rho=93/100.
"""

from __future__ import annotations

import hashlib
import math
import os
import sys
from pathlib import Path

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


BASE_PATH = Path(__file__).with_name(
    "general_d_high_floor_active_width_verify.py"
)
BASE_SHA256 = "267900ED39C17C02D1BBDEB17B5F36AB616601DEE8127D98E50A9646BCEDCAB5"
actual_base_hash = hashlib.sha256(BASE_PATH.read_bytes()).hexdigest().upper()
if actual_base_hash != BASE_SHA256:  # pragma: no cover
    raise SystemExit(
        f"Round-08C helper hash mismatch: {actual_base_hash} != {BASE_SHA256}"
    )

import general_d_high_floor_active_width_verify as base  # noqa: E402


ctx.prec = int(os.environ.get("GENERAL_D_ARB_PREC", "512"))
PI = arb.pi()
SQRT2 = arb(2).sqrt()

RHO_MIN = fmpq(93, 100)
RHO_MAX = fmpq(477, 500)
C_BAR = fmpq(1199, 10000)
THETA_SQ_BAR = fmpq(71, 500)
COEFFICIENT_FLOOR = fmpq(1389, 1000)
W_FLOOR = fmpq(7, 20)
CAP_UPPER = fmpq(1, 5)
SERIES_Z_BAR = fmpq(7, 30)
SERIES_QUADRATIC_UPPER = fmpq(9, 368)
SERIES_INTEGRATED_UPPER = fmpq(9, 1288)
PANELS = 64


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def g_radius(radius: arb, z: arb) -> arb:
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / PI


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
    print("GENERAL-d HIGH-FLOOR SHARP-CAP CERTIFICATE (ROUND 08D)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print(f"Round-08C helper SHA256={actual_base_hash}")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    theta0 = rho0.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 < 71/500 failed")
    require(theta0 / PI < A(C_BAR), "c < 1199/10000 failed")
    print("PASS ratio endpoint: theta^2<71/500 and c<1199/10000")

    power = [
        fmpq(19, 50),
        -fmpq(3, 8),
        -fmpq(1, 4),
        fmpq(3, 32),
        fmpq(3, 32),
        fmpq(3, 64),
        fmpq(1, 64),
    ]
    coeffs = base.bernstein_coefficients(power, 32)
    require(min(coeffs) == fmpq(309, 396800), "Bernstein minimum changed")
    require(C_BAR < fmpq(3, 25), "common prefix gamma is not positive")
    print("PASS common-prefix ledgers: Bernstein minimum and gamma>0")

    # Round 8C's active-width comparison applies throughout this band.
    require(
        fmpq(8, 9) * fmpq(23, 500) > fmpq(1, 25),
        "active-width lambda >1/5 failed",
    )
    require(fmpq(7, 4) * fmpq(1, 5) == W_FLOOR, "W floor changed")
    require(2 * W_FLOOR > fmpq(3, 25), "zero-face monotonicity failed")
    print("PASS inherited active-width ledger: W>7/20")

    # Since p<n, one has n>=1 and q=r+n>=3/2.
    # The analytic proof shows G_{q+1}(q) is decreasing; certify its endpoint.
    cap_endpoint = g_radius(A(fmpq(5, 2)), A(fmpq(3, 2)))
    require(cap_endpoint < A(CAP_UPPER), "G_(5/2)(3/2) < 1/5 failed")
    print("PASS sharp terminal cap: G_(5/2)(3/2)<1/5")

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
        "scaled integral coefficient <=1389/1000",
    )

    u_upper = fmpq(5, 3) * tbar / RHO_MIN
    require(u_upper == fmpq(71, 279), "unexpected t0/mu upper bound")
    require(u_upper < fmpq(51, 200), "t0/mu <51/200 failed")
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
    require(first_copy_z == fmpq(91, 300), "first-copy z bound changed")
    require(first_copy_z < 1, "positive arccos series left its domain")
    print("PASS retuned arccos constants:")
    print("  coefficient>1389/1000, u0<51/200")
    print("  subtracted z<=7/30; tail=9/368; integrated=9/1288")
    print("  positive first-copy argument <=91/300")

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

    b0_positive = fmpq(31, 50) - fmpq(39, 10) * C_BAR + C_BAR**2
    q_zero = (
        (fmpq(3, 25) - C_BAR) * (fmpq(7, 4) - W_FLOOR)
        - C_BAR / 2
        + C_BAR**2
        + W_FLOOR**2
    )
    q_one_upper = fmpq(273, 400) - fmpq(5, 2) * C_BAR + C_BAR**2
    q_one_lower = fmpq(273, 400) - fmpq(119, 50) * C_BAR - C_BAR**2
    small_delta = fmpq(5, 16) - fmpq(27, 10) * C_BAR + C_BAR**2

    require(b0_positive == fmpq(16676601, 100000000), "B0>=1 mismatch")
    require(q_zero == fmpq(7706601, 100000000), "B0=Q=0 mismatch")
    require(q_one_upper == fmpq(39712601, 100000000), "Q=1 upper mismatch")
    require(q_one_lower == fmpq(38276199, 100000000), "Q=1 lower mismatch")
    require(
        small_delta == fmpq(314601, 100000000),
        "sharp-cap small-delta mismatch",
    )
    require(
        min(b0_positive, q_zero, q_one_upper, q_one_lower, small_delta) > 0,
        "scalar ledger failed",
    )
    print("PASS exact scalar ledgers:")
    print(f"  delta>=1, B0>=1: c*S > {b0_positive}")
    print(f"  delta>=1, B0=0, Q=0: c*S > {q_zero}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4: > {q_one_upper}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4-c: > {q_one_lower}")
    print(f"  0<delta<1 with cap<1/5: c*S > {small_delta}")

    eta0 = base.g(rho0)
    require(eta0 > A(fmpq(1, 180)), "eta(rho0)>1/180 failed")
    require(base.g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(2) * fmpq(355, 113) * fmpq(93, 7)
    require(a_upper == fmpq(66030, 791), "a upper bound changed")
    combined = a_upper + fmpq(13, 45)
    require(combined == fmpq(2981633, 35595), "numerator sum changed")
    require(combined < 84, "fixed-ratio numerator bound failed")
    cutoff = 84 * 180**2
    require(cutoff == 2721600, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/180, eta<1/9, a+2*eta*C_*<84")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 5443199, "2r range arithmetic failed")
    require(cutoff - 1 == 2721599, "n range arithmetic failed")
    f_upper = fmpq(cutoff, 3) + fmpq(1, 4)
    require(
        fmpq(907200) < f_upper < fmpq(907201),
        "f,B range arithmetic failed",
    )
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("93/100 <= rho <= 477/500; Round 08B covers larger rho.")
    print("Residual fixed-ratio walls with rho<93/100 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
