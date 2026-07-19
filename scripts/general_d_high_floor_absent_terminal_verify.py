#!/usr/bin/env python3
"""Directed/exact certificate for the Round-08B high-floor ratio band.

The analytic proof is in
human/outbox/general-d-round-08b-high-floor-absent-terminal.md.
The script certifies the rational ledgers and the directed-Arb interval
comparisons used there.  It does not sample the original shell scalar and
does not certify the residual rho < 477/500 compact walls.
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

RHO_MIN = fmpq(477, 500)
RHO_MAX = fmpq(99, 100)
C_BAR = fmpq(97, 1000)
THETA_SQ_BAR = fmpq(93, 1000)
COEFFICIENT_FLOOR = fmpq(7, 5)
SERIES_Z_BAR = fmpq(23, 150)
SERIES_QUADRATIC_UPPER = fmpq(45, 2032)
SERIES_INTEGRATED_UPPER = fmpq(45, 7112)
PANELS = 32


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
    """Return value**(odd_numerator/2) for positive value."""
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
    result -= (
        A(SERIES_INTEGRATED_UPPER)
        * eps
        * eps
        * odd_half_power(v, 7)
    )
    return result


def main() -> None:
    print("GENERAL-d HIGH-FLOOR ABSENT-TERMINAL CERTIFICATE (ROUND 08B)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    theta0 = rho0.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 < 93/1000 failed")
    require(theta0 / PI < A(C_BAR), "c < 97/1000 failed")
    print("PASS ratio endpoint: theta^2<93/1000 and c<97/1000")

    # The common absent-level coefficient uses the exact Round-07
    # degree-32 Bernstein comparison.
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

    # The coefficient Taylor quotient is decreasing on this larger interval.
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
        "scaled integral coefficient <= 7/5",
    )

    u_upper = fmpq(5, 3) * tbar / RHO_MIN
    require(u_upper < fmpq(1, 6), "t0/mu < 1/6 failed")
    eps_max = 1 - RHO_MIN
    z_upper = eps_max * fmpq(10, 3)
    require(z_upper == SERIES_Z_BAR, "unexpected retained z upper bound")
    require(SERIES_Z_BAR < 1, "arccos upper-series domain failed")
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
    print("PASS refined arccos constants:")
    print("  coefficient>7/5, u0<1/6, retained z<=23/150")
    print("  series upper z^2 coefficient=45/2032; integrated=45/7112")

    # Exact concavity reduces x to its two endpoints.  Each rho value below
    # is a full Arb interval covering one closed rational panel.
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
        "PASS level-distance band: 64 directed endpoint panels; "
        f"minimum lower margin={smallest:.12g}"
    )
    print(f"  minimum retained-integral lower bound={smallest_integral:.12g}")

    # Common delta>=1 prefix coefficient gamma=3/25-c.  Present level has
    # the larger coefficient 1/8-c, by exactly 1/200.
    require(fmpq(1, 8) - fmpq(3, 25) == fmpq(1, 200), "prefix gap changed")
    b0_positive = fmpq(31, 50) - fmpq(39, 10) * C_BAR + C_BAR**2
    q_zero = fmpq(129, 625) - fmpq(219, 100) * C_BAR + fmpq(3, 4) * C_BAR**2
    q_one_upper = fmpq(273, 400) - fmpq(5, 2) * C_BAR + C_BAR**2
    q_one_lower = fmpq(273, 400) - fmpq(119, 50) * C_BAR - C_BAR**2
    small_delta = fmpq(5, 16) - fmpq(29, 10) * C_BAR + C_BAR**2

    require(b0_positive == fmpq(251109, 1000000), "B0>=1 ledger mismatch")
    require(q_zero == fmpq(4107, 4000000), "B0=Q=0 ledger mismatch")
    require(q_one_upper == fmpq(449409, 1000000), "Q=1 upper endpoint mismatch")
    require(q_one_lower == fmpq(442231, 1000000), "Q=1 lower endpoint mismatch")
    require(small_delta == fmpq(40609, 1000000), "small-delta ledger mismatch")
    require(
        min(b0_positive, q_zero, q_one_upper, q_one_lower, small_delta) > 0,
        "scalar ledger failed",
    )
    print("PASS exact scalar ledgers:")
    print(f"  delta>=1, B0>=1: c*S > {b0_positive}")
    print(f"  delta>=1, B0=0, Q=0: c*S > {q_zero}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4: > {q_one_upper}")
    print(f"  delta>=1, B0=0, Q=1 at W=3/4-c: > {q_one_lower}")
    print(f"  0<delta<1: c*S > {small_delta}")

    eta0 = g(rho0)
    require(eta0 > A(fmpq(1, 338)), "eta(rho0)>1/338 failed")
    require(g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper bound failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(2) * fmpq(355, 113) * fmpq(477, 23)
    require(a_upper == fmpq(338670, 2599), "a upper bound changed")
    combined = a_upper + fmpq(13, 45)
    require(combined < 131, "fixed-ratio numerator bound failed")
    cutoff = 131 * 338**2
    require(cutoff == 14965964, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/338, eta<1/9, a+2*eta*C_*<131")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 29931927, "2r range arithmetic failed")
    require(cutoff - 1 == 14965963, "n range arithmetic failed")
    f_upper = fmpq(cutoff, 3) + fmpq(1, 4)
    require(
        fmpq(4988654) < f_upper < fmpq(4988655),
        "f,B range arithmetic failed",
    )
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("477/500 <= rho <= 99/100; Round 07 covers rho>99/100.")
    print("Residual fixed-ratio walls with rho<477/500 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
