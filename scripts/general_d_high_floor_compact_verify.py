#!/usr/bin/env python3
"""Directed-rounding audit for the quantitative high-floor transfer.

This script checks the finite numerical comparisons used in
``human/outbox/general-d-round-06-high-floor-compact.md``.  The analytic
part of that note proves that a negative high-floor first-drop scalar is
impossible when

    s = sqrt(1-rho) <= 1/10000.

Together with the already proved thin high-energy and fixed-ratio
theorems, this gives the explicit global cutoff

    K < 156250000000000000.

Every transcendental comparison below is made with python-flint Arb ball
arithmetic.  The remaining comparisons are exact rational inequalities.
Floating point is not used for a sign decision.
"""

from __future__ import annotations

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

S0 = fmpq(1, 10_000)
ETA0 = fmpq(1, 1_000)
K_STAR = 156_250_000_000_000_000
F_STAR = 52_083_333_333_333_333
N_STAR = K_STAR - 1


def q(x: int | fmpq) -> arb:
    return arb(x)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    print("GENERAL-d HIGH-FLOOR COMPACT TRANSFER CERTIFICATE")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print("All transcendental signs use directed-rounding Arb arithmetic.\n")

    # Large-M interface pinning.  For M>100, c<s and d=1-2c imply
    # T/M > 1 + (1-2s)(1-1/100).  Its elasticity factor is >23/20.
    r0 = fmpq(1) + (fmpq(1) - 2 * S0) * fmpq(99, 100)
    require(
        r0 * r0 * 400 > fmpq(529) * (2 * r0 - 1),
        "elasticity factor was not >23/20",
    )
    print("PASS elasticity pinning: r/sqrt(2r-1) > 23/20")

    # The small-M case gives W>h-1/100.  With the 1/1000 profile-ratio
    # enclosure its critical level ratio is safely below F(1/3).
    small_ratio = fmpq(100, 87) * fmpq(1000, 999) ** 2
    require(small_ratio < fmpq(6, 5), "small-M level ratio cutoff failed")
    require(fmpq(6, 5) < fmpq(61, 27), "F(1/3) comparison failed")
    print("PASS small-M level localization: F(t_f)<6/5<F(1/3)")

    # Robust replay of the t-parameter contradiction in the large-M case.
    require(
        fmpq(7, 8) * fmpq(999, 1001) > fmpq(6, 7),
        "lower profile-ratio comparison failed",
    )
    require(fmpq(27, 14) > fmpq(1891, 1000), "t_h<2/5 failed")
    t_ratio = fmpq(8, 7) * fmpq(1001, 999) * fmpq(1891, 1875)
    require(t_ratio < fmpq(7, 6), "t_h/t_f bound failed")
    u_ratio = fmpq(7, 6) ** 2 * fmpq(25, 21) ** 2
    require(u_ratio < 2, "turning-coordinate ratio was not <2")
    prefix_ratio = 1 + 2 * (1 - 2 * S0) * fmpq(99, 100)
    require(prefix_ratio > fmpq(5, 2), "negative-prefix geometry was not >5/2")

    print("PASS large-M t-parameter bounds: t_f>1/3")

    # Global localization before the sharp profile comparison.  The exact
    # shell/product sandwich gives H(T)/w < (3 sqrt(2)/2)*25 <54.
    require(3 * SQRT2 * 25 / 2 < 54, "global critical ratio was not <54")
    require(54 * 4 * fmpq(1, 72) >= 3, "t>1/72 arithmetic failed")
    print("PASS global turning window: t_f>1/72 and X_f/kappa<1296")

    # On u<1296 the exact non-cancelling integrand ratio is in
    # [1-eta_0,1+eta_0].
    require(649 * S0 * S0 < ETA0, "lower integrand-ratio error too large")
    require(
        fmpq(1, 1) / (1 - S0 * S0) < 1 + ETA0,
        "upper integrand-ratio error too large",
    )
    print("PASS exact/critical profile ratio: |R-1|<1/1000")

    # Exact derivative transfer.  y_mu<1/50000, and the loss from the two
    # square-root factors is less than 1/5000 after multiplying by sqrt(u).
    y_mu = fmpq(1296) * S0 * S0 / (1 - S0 * S0)
    require(y_mu < fmpq(1, 50_000), "inner turning parameter too large")
    factor_loss = S0 * S0 + y_mu / 2 + S0 * S0 * y_mu / 2
    require(factor_loss < fmpq(1, 90_000), "slope factor loss too large")
    require(SQRT2 / PI < fmpq(1, 2), "sqrt(2)/pi upper bound failed")
    require(SQRT2 / (3 * PI) > fmpq(49, 330), "critical slope lower bound failed")
    require(
        fmpq(49, 330) - fmpq(1, 5000) > fmpq(7, 50),
        "transferred slope was not >7/50",
    )
    print("PASS exact level-band slope: H_s'(X)>7/50")

    # Terminal first-level payment and the final conditional contradiction.
    w_lower = fmpq(54_000, 61_061)
    require(w_lower > fmpq(19, 20) ** 3, "w lower bound too small")
    require(
        fmpq(999, 1000) * fmpq(19, 20) ** 3 > fmpq(3, 4),
        "first complete ball level was not forced",
    )
    require(PI * PI / (6 * SQRT2) > 1, "root-free angle coefficient <=1")
    require(4 * SQRT2 / 15 < fmpq(2, 5), "cap bound was not <2/5")
    final_gap = (
        fmpq(19, 20)
        - fmpq(25, 56)
        - (fmpq(7, 5) + fmpq(1, 2)) * S0
    )
    require(
        final_gap > fmpq(1, 2),
        "conditional scaled-scalar contradiction was not >1/2",
    )
    print("PASS conditional contradiction: a putative negative candidate")
    print("  would have s*S > 1/2 for 0<s<=1/10000")

    # Fixed-ratio and thin-high-energy global numerical boxes.
    eta_fixed = fmpq(49, 165_000)
    k_bar = fmpq(16_988_400_000_000, 2401)
    radicand_upper = (
        fmpq(623) ** 2
        + 4 * fmpq(623) * fmpq(1, 3) * fmpq(13, 10)
        + fmpq(1, 9)
    )
    require(radicand_upper < fmpq(624) ** 2, "fixed-ratio radicand bound failed")
    require(
        fmpq(623) + 2 * fmpq(1, 3) * fmpq(13, 10) + fmpq(624)
        < 2 * fmpq(624),
        "fixed-ratio numerator bound failed",
    )
    require(fmpq(624) / (eta_fixed * eta_fixed) == k_bar,
            "fixed-ratio rational K bound mismatch")
    require(k_bar < K_STAR, "fixed-ratio K bound exceeds global cutoff")
    require(
        fmpq(125, 8) / (S0 * S0) ** 2 == K_STAR,
        "thin high-energy cutoff arithmetic failed",
    )
    floor_supremum = fmpq(K_STAR, 3) + fmpq(1, 4)
    require(F_STAR < floor_supremum, "reported floor cutoff is too large")
    require(floor_supremum < F_STAR + 1, "reported floor cutoff is too small")
    require(N_STAR == K_STAR - 1, "reported n cutoff mismatch")
    print(f"PASS global cutoff: K < {K_STAR}")
    print(f"PASS discrete bounds: f,B <= {F_STAR}; n <= {N_STAR}")

    print("\nCERTIFIED: all numerical constants in the explicit high-floor")
    print(f"compact reduction pass at {ctx.prec}-bit directed-rounding precision.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
