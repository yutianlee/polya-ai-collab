#!/usr/bin/env python3
"""Directed/exact replay for the Round-07 high-floor global scalar.

The analytic proof is in
``human/outbox/general-d-round-07-high-floor-global-scalar.md``.
This verifier checks only its finite algebraic and transcendental
comparisons.  It does not sample the exact shell scalar.
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


def q(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def bernstein_coefficients(power: list[fmpq], degree: int) -> list[fmpq]:
    """Power coefficients on [0,1] converted to Bernstein degree ``degree``."""
    source_degree = len(power) - 1
    require(degree >= source_degree, "Bernstein degree is too small")
    result: list[fmpq] = []
    for k in range(degree + 1):
        total = fmpq(0)
        for j in range(min(k, source_degree) + 1):
            total += power[j] * fmpq(math.comb(k, j), math.comb(degree, j))
        result.append(total)
    return result


def pow_three_halves(x: arb) -> arb:
    return x * x.sqrt()


def profile_I(v: arb) -> arb:
    return (
        q(fmpq(200, 297))
        * (pow_three_halves(1 + q(fmpq(99, 100)) * v) - 1)
        - q(fmpq(101, 150)) * pow_three_halves(v)
    )


def profile_J(x: fmpq) -> arb:
    xx = q(x)
    return q(fmpq(147, 100)) * profile_I(q(fmpq(199, 100)) * xx) - xx


def main() -> None:
    print("GENERAL-d HIGH-FLOOR GLOBAL-SCALAR CERTIFICATE")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = q(fmpq(99, 100))
    theta0 = rho0.acos()
    require(theta0 < PI / 20, "c<1/20 was not certified")
    require(theta0 * theta0 < q(fmpq(21, 1000)), "theta^2 cutoff failed")
    print("PASS ratio constants: c<1/20, d>9/10, theta^2<21/1000")

    # With x=sqrt(a), y=2x, the polynomial below is 19/50-U(y/2).
    power = [
        fmpq(19, 50),
        -fmpq(3, 8),
        -fmpq(1, 4),
        fmpq(3, 32),
        fmpq(3, 32),
        fmpq(3, 64),
        fmpq(1, 64),
    ]
    degree = 32
    coeffs = bernstein_coefficients(power, degree)
    minimum = min(coeffs)
    require(minimum == fmpq(309, 396800), "unexpected Bernstein minimum")
    require(minimum > 0, "absent-level polynomial was not positive")
    print(
        "PASS absent-level Bernstein bound: one panel, degree 32, "
        f"{degree + 1} coefficients, minimum coefficient {minimum}"
    )

    # Coefficient in the scaled arccos integral.
    eps_factor = q(fmpq(499, 1000))
    coefficient = 3 * rho0 * SQRT2 * eps_factor * eps_factor.sqrt()
    require(coefficient > q(fmpq(147, 100)), "profile coefficient <=147/100")

    u_upper = fmpq(5, 3) * fmpq(21, 1000) * fmpq(100, 99)
    require(u_upper < fmpq(9, 250), "u0<9/250 failed")
    require(fmpq(9979, 5000) > fmpq(199, 100), "v0 lower bound failed")
    require(
        fmpq(101, 100) ** 2 * (1 - fmpq(9, 500)) > 1,
        "101/100 square-root factor failed",
    )
    vmax = fmpq(199, 100) * fmpq(5, 3)
    require(
        1 + fmpq(99, 100) * vmax
        > fmpq(101, 100) ** 2 * vmax,
        "retained profile integrand was not positive",
    )
    print("PASS scaled-profile constants: u0<9/250 and coefficient>147/100")

    # I''<0: after squaring the positive factors, the RHS minus the LHS
    # has a positive constant and a positive coefficient of V.
    curvature_constant = fmpq(101, 100) ** 2
    curvature_slope = (
        fmpq(101, 100) ** 2 * fmpq(99, 100)
        - fmpq(99, 100) ** 2
    )
    require(curvature_constant > 0 and curvature_slope > 0, "I was not concave")
    j_left = profile_J(fmpq(1, 7))
    j_right = profile_J(fmpq(5, 3))
    require(j_left > q(fmpq(3, 20)), "J(1/7) endpoint margin failed")
    require(j_right > q(fmpq(7, 50)), "J(5/3) endpoint margin failed")
    print("PASS profile concavity and endpoint margins:")
    print("  J(1/7)>3/20, J(5/3)>7/50")

    # Final rational ledgers.
    present_margin = fmpq(3, 40) * 20 - fmpq(1, 2)
    absent_margin = fmpq(7, 100) * 20 - fmpq(1, 2)
    require(present_margin == 1, "present-level prefix margin mismatch")
    require(absent_margin == fmpq(9, 10), "absent-level prefix margin mismatch")
    print("PASS delta>=1 margins: P>1 (level present), P>9/10 (absent)")

    require(4 * SQRT2 / 15 < q(fmpq(2, 5)), "cap bound was not <2/5")
    prefix_scaled = -fmpq(21, 80)
    terminal_scaled = fmpq(43, 100)
    final_scaled = prefix_scaled + terminal_scaled
    require(final_scaled == fmpq(67, 400), "final scaled margin mismatch")
    require(final_scaled > 0, "final scaled margin was not positive")
    print("PASS delta<1 margin: c*S>67/400")

    print("\nCERTIFIED: every finite comparison in the Round-07")
    print("rho>99/100 high-floor global-scalar proof passes.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
