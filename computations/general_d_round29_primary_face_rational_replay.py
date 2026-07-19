#!/usr/bin/env python3
"""Exact rational replay for the Round 29 primary inverse-wall cell.

The analytic note reduces every transcendental comparison below to an
alternating Taylor bound plus the classical rational enclosure

    333/106 < pi < 22/7.

This file performs only exact Fraction arithmetic.  It is a reproducibility
check for the printed analytic proof, not a finite search over the theorem
domain.
"""

from __future__ import annotations

from fractions import Fraction as F


PI_LO = F(333, 106)
PI_HI = F(22, 7)


def sin_lower_7(x: F) -> F:
    return x - x**3 / 6 + x**5 / 120 - x**7 / 5040


def sin_upper_5(x: F) -> F:
    return x - x**3 / 6 + x**5 / 120


def cos_lower_6(x: F) -> F:
    return 1 - x**2 / 2 + x**4 / 24 - x**6 / 720


def cos_upper_8(x: F) -> F:
    return 1 - x**2 / 2 + x**4 / 24 - x**6 / 720 + x**8 / 40320


def tan_lower(x: F) -> F:
    return sin_lower_7(x) / cos_upper_8(x)


def tan_upper(x: F) -> F:
    return sin_upper_5(x) / cos_lower_6(x)


def positive(name: str, value: F) -> None:
    if value <= 0:
        raise ArithmeticError(f"{name} failed: {value}")
    print(f"{name}={value} (~{float(value):.15g})")


def zero(name: str, value: F) -> None:
    if value != 0:
        raise ArithmeticError(f"{name} failed: {value}")
    print(f"{name}=0")


def main() -> None:
    # theta_0 is defined by tan(theta_0)-theta_0=3*pi/28.
    theta_lo = F(4, 5)
    positive(
        "thetaLowerResidual",
        F(3, 28) * PI_LO - (tan_upper(theta_lo) - theta_lo),
    )
    positive(
        "K0CosResidual",
        F(7, 10) - (1 - theta_lo**2 / 2 + theta_lo**4 / 24),
    )

    theta_hi_probe = F(2, 7) * PI_LO
    positive(
        "thetaUpperResidual",
        tan_lower(theta_hi_probe) - F(11, 28) * PI_HI,
    )

    # If beta>=2/5, then v exceeds 7/4, contradicting B=1.
    beta_probe = F(2, 5) * PI_LO
    positive(
        "betaResidual",
        tan_lower(beta_probe) - F(3, 4) * PI_HI,
    )

    # sqrt(2/5)<16/25 and hence the exact cap coefficient is <1/9.
    positive("capSqrtResidual", F(16, 25) ** 2 - F(2, 5))
    cap_upper = F(8, 15) * F(16, 25) / PI_LO
    positive("capResidual", F(1, 9) - cap_upper)

    # K_4 is larger than its quadratic member.  K>10 and mu<6 give
    # cos(t)<3/5, so 4(1-cos(t))/(pi*mu)>14/165.
    curvature_lower = F(4) * F(2, 5) / (PI_HI * 6)
    zero("curvatureBoundaryIdentity", curvature_lower - F(14, 165))

    # Complete-terminal lower arithmetic on B=Q=1 and 2<y_1<3.
    terminal_constant = F(7, 4) - 1 + F(5, 32)
    zero("terminalBeforeCapIdentity", terminal_constant - F(29, 32))
    zero("terminalAfterCapIdentity", F(29, 32) - F(1, 9) - F(229, 288))

    projected_before_cap = F(29, 32) + F(14, 495) - F(4, 5)
    zero(
        "projectedBeforeCapIdentity",
        projected_before_cap - F(2131, 15840),
    )
    projected_after_cap = F(2131, 15840) - F(1, 9)
    zero(
        "projectedAfterCapIdentity",
        projected_after_cap - F(371, 15840),
    )
    positive("finalPrimaryFaceMargin", F(371, 15840))
    print("round29PrimaryFaceRationalReplayOK=True")


if __name__ == "__main__":
    main()
