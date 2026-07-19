#!/usr/bin/env python3
"""Directed/exact certificate for the Round-08A high-floor ratio band.

The analytic proof is in
``human/outbox/general-d-round-08-high-floor-fixed-ratio.md``.
This script certifies the finite rational, Bernstein, and directed-Arb
comparisons used there.  It does not sample the original shell scalar and
does not certify the residual ``rho < 603/625`` compact walls.
"""

from __future__ import annotations

import math
import os
import sys

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = int(os.environ.get("GENERAL_D_ARB_PREC", "512"))
PI = arb.pi()
SQRT2 = arb(2).sqrt()

RHO_MIN = fmpq(603, 625)
RHO_MAX = fmpq(99, 100)
C_BAR = fmpq(339, 4000)
THETA_SQ_BAR = fmpq(71, 1000)
COEFFICIENT_FLOOR = fmpq(36, 25)
PANELS = 16


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def interval_ball(lo: fmpq, hi: fmpq) -> arb:
    if hi < lo:
        raise AssertionError("reversed interval")
    if lo == hi:
        return A(lo)
    mid, rad = (lo + hi) / 2, (hi - lo) / 2
    out = arb(str(mid), str(rad))
    require(out.contains(A(lo)) and out.contains(A(hi)), "lost endpoint")
    return out


def lower(value: arb) -> arb:
    return value.lower()


def odd_half_power(value: arb, odd_numerator: int) -> arb:
    """Return value**(odd_numerator/2) for positive ``value``."""
    require(odd_numerator in {3, 5, 7}, "unsupported half power")
    return value.sqrt() * value ** ((odd_numerator - 1) // 2)


def g(value: arb) -> arb:
    return ((1 - value * value).sqrt() - value * value.acos()) / PI


def bernstein_coefficients(power: list[fmpq], degree: int) -> list[fmpq]:
    source_degree = len(power) - 1
    require(degree >= source_degree, "Bernstein degree is too small")
    result: list[fmpq] = []
    for k in range(degree + 1):
        total = fmpq(0)
        for j in range(min(k, source_degree) + 1):
            total += power[j] * fmpq(math.comb(k, j), math.comb(degree, j))
        result.append(total)
    return result


def series_integral_lower(rho: arb, x: fmpq) -> arb:
    """Lower integral after u=(1-rho)v, retained through V=2x."""
    eps = 1 - rho
    v = A(2 * x)
    one_plus = 1 + rho * v

    result = A(fmpq(2, 3)) / rho * (odd_half_power(one_plus, 3) - 1)
    result += eps / (30 * rho) * (odd_half_power(one_plus, 5) - 1)
    result += (
        A(fmpq(3, 560))
        * eps
        * eps
        / rho
        * (odd_half_power(one_plus, 7) - 1)
    )
    result -= A(fmpq(2, 3)) * odd_half_power(v, 3)
    result -= eps / 30 * odd_half_power(v, 5)
    result -= A(fmpq(3, 490)) * eps * eps * odd_half_power(v, 7)
    return result


def main() -> None:
    print("GENERAL-d HIGH-FLOOR FIXED-RATIO CERTIFICATE (ROUND 08A)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    theta0 = rho0.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 < 71/1000 failed")
    require(theta0 / PI < A(C_BAR), "c < 339/4000 failed")
    print("PASS ratio endpoint: theta^2<71/1000 and c<339/4000")

    # The absent-level algebra is the Round-07 degree-32 Bernstein check.
    power = [
        fmpq(19, 50),
        -fmpq(3, 8),
        -fmpq(1, 4),
        fmpq(3, 32),
        fmpq(3, 32),
        fmpq(3, 64),
        fmpq(1, 64),
    ]
    coeffs = bernstein_coefficients(power, 32)
    require(min(coeffs) == fmpq(309, 396800), "Bernstein minimum changed")
    print("PASS absent-level Bernstein minimum: 309/396800")

    # t -> (1/2-t/24)^(3/2)/(1/3-t/30+t^2/840) is decreasing.
    # Its logarithmic derivative is negative because
    # 1260 D(t)-2(14-t)(12-t)=84+10t-t^2/2 > 0.
    tbar = THETA_SQ_BAR
    monotonicity_gap = 84 + 10 * tbar - tbar * tbar / 2
    require(monotonicity_gap > 0, "coefficient monotonicity failed")
    numerator = A(fmpq(1, 2) - tbar / 24)
    denominator = A(fmpq(1, 3) - tbar / 30 + tbar * tbar / 840)
    coefficient_lower = (
        rho0 * SQRT2 * odd_half_power(numerator, 3) / denominator
    )
    require(
        coefficient_lower > A(COEFFICIENT_FLOOR),
        "scaled integral coefficient <= 36/25",
    )

    u_upper = fmpq(5, 3) * tbar / RHO_MIN
    require(u_upper < fmpq(1, 8), "t0/mu < 1/8 failed")
    eps_max = 1 - RHO_MIN
    z_upper = eps_max * fmpq(10, 3)
    require(z_upper == fmpq(44, 375), "unexpected retained z upper bound")
    require(z_upper < fmpq(1, 8), "arccos series upper domain failed")
    print("PASS refined arccos constants: coefficient>36/25, u0<1/8")
    print("  retained upper-series argument z<=44/375<1/8")

    # Concavity of the exact scaled increment reduces x to the two endpoints.
    smallest = float("inf")
    smallest_integral = float("inf")
    for endpoint in (fmpq(1, 7), fmpq(5, 3)):
        for panel in range(PANELS):
            lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, PANELS)
            hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, PANELS)
            rho = interval_ball(lo, hi)
            integral = series_integral_lower(rho, endpoint)
            margin = A(COEFFICIENT_FLOOR) * integral - A(endpoint)
            require(lower(integral) > 0, "series integral was not positive")
            require(lower(margin) > 0, "level-distance endpoint failed")
            smallest_integral = min(smallest_integral, float(lower(integral)))
            smallest = min(smallest, float(lower(margin)))
    print(
        "PASS level-distance band: 32 directed endpoint panels; "
        f"minimum lower margin={smallest:.12g}"
    )
    print(f"  minimum retained-integral lower bound={smallest_integral:.12g}")

    present = fmpq(1, 8) / C_BAR - fmpq(3, 2) + C_BAR
    absent = fmpq(3, 25) / C_BAR - fmpq(3, 2) + C_BAR
    small_delta = fmpq(5, 16) - fmpq(29, 10) * C_BAR + C_BAR**2
    require(present == fmpq(80921, 1356000), "present margin mismatch")
    require(absent == fmpq(307, 452000), "absent margin mismatch")
    require(small_delta == fmpq(1182521, 16000000), "small-delta mismatch")
    require(present > 0 and absent > 0 and small_delta > 0, "ledger failed")
    print("PASS exact scalar ledgers:")
    print(f"  delta>=1 present > {present}")
    print(f"  delta>=1 absent  > {absent}")
    print(f"  0<delta<1: c*S > {small_delta}")

    eta0 = g(rho0)
    require(eta0 > A(fmpq(1, 504)), "eta(rho0)>1/504 failed")
    require(g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper bound failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(2) * fmpq(355, 113) * fmpq(603, 22)
    combined = a_upper + fmpq(13, 45)
    require(combined < 173, "fixed-ratio numerator bound failed")
    cutoff = 173 * 504**2
    require(cutoff == 43944768, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/504, eta<1/9, a+2*eta*C_*<173")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 87889535, "2r range arithmetic failed")
    require(cutoff - 1 == 43944767, "n range arithmetic failed")
    require(cutoff // 3 == 14648256, "f,B range arithmetic failed")
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("603/625 <= rho <= 99/100; Round 07 covers rho>99/100.")
    print("Residual fixed-ratio walls with rho<603/625 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
