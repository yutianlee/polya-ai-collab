#!/usr/bin/env python3
"""Directed-rounding counterexample to the coarse Round 21 scalar R.

This script verifies one exact rational high-floor first-drop shell:

    K = 261/20,  mu = 699/100,  rho = 233/435,
    r = 1, n = 5, p = 3, m = 2, q = 6.

It proves with python-flint Arb arithmetic that the Round 21 scalar (4.4),
which replaces the local cap by 1/7, is negative.  It separately proves
that the same reduction with the exact cap J=2 I_mu(q) retained is
positive.  Therefore this is a counterexample only to the coarse scalar
R>=0, not to Phi_delta, CST, or the shifted-tail theorem.

Every transcendental sign decision uses directed-rounding Arb arithmetic.
"""

from __future__ import annotations

import os

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = int(os.environ.get("GENERAL_D_ROUND22_ARB_PREC", "512"))
PI = arb.pi()


def A(x: int | fmpq) -> arb:
    return arb(x)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def g(radius: fmpq, z: fmpq | int) -> arb:
    """Exact-point ball action G_radius(z)."""

    if radius <= z:
        return arb(0)
    R, Z = A(radius), A(z)
    return ((R * R - Z * Z).sqrt() - Z * (Z / R).acos()) / PI


def cap_i(radius: fmpq, z: fmpq | int) -> arb:
    """Exact-point cap integral I_radius(z)."""

    if radius <= z:
        return arb(0)
    R, Z = A(radius), A(z)
    u = Z / R
    return (
        R
        * R
        / (4 * PI)
        * ((1 + 2 * u * u) * u.acos() - 3 * u * (1 - u * u).sqrt())
    )


def main() -> None:
    K = fmpq(261, 20)
    mu = fmpq(699, 100)
    rho = fmpq(233, 435)
    r, n, p, m, q = 1, 5, 3, 2, 6
    f = 2

    require(mu / K == rho, "rho != mu/K")
    require(fmpq(5) < mu - r < fmpq(6), "n is not 5")
    require(fmpq(q) <= mu < fmpq(q + 1), "interface alpha is not in [0,1)")

    active_rhs = PI * PI / (1 - A(rho)) ** 2 + fmpq(3, 4)
    require(A(K) ** 2 > active_rhs, "integer-owner d=4 activity failed")

    def shell(z: int) -> arb:
        return g(K, z) - g(mu, z)

    # Ordinary-floor ownership: f=2 through z=4, then the first drop at z=5.
    for z in range(1, 5):
        sample = shell(z) + fmpq(1, 4)
        require(sample > 2, f"sample z={z} is not strictly above floor 2")
        require(sample < 3, f"sample z={z} reaches floor 3")
    drop = shell(5) + fmpq(1, 4)
    require(drop > 1, "drop sample is not strictly above floor 1")
    require(drop < 2, "first shelf does not drop at z=5")

    theta = A(rho).acos()
    c = theta / PI
    d = 1 - 2 * c
    phi = theta.sin() - theta * theta.cos()
    W = A(K) * phi / PI
    lam = fmpq(7, 4) - W

    require(lam > 0, "lambda is not positive")
    require(lam < fmpq(3, 4), "lambda is outside the top-payment branch")
    require(W + fmpq(1, 4) > 1, "literal B0 is below 1")
    require(W + fmpq(1, 4) < 2, "literal B0 is above 1")
    B0 = 1

    X = A(mu) - (r + p)
    kappa = (1 - A(rho)) / (PI * A(rho) * A(K))
    s = (
        1
        + fmpq(p * (2 * r + p))
        / (X * (X + 2 * r + 2 * p))
    ).sqrt()
    a_p = fmpq(p * p, 3 * (2 * r + p))

    elastic = (s - 1) * lam
    curvature = kappa * fmpq(p * (2 * r + p), 2)
    require(curvature > elastic, "the asserted curvature branch is not maximal")
    L0 = curvature

    top_payment = 2 * (fmpq(3, 4) - lam) ** 2
    require(top_payment < 1, "top payment should be below the alternate unit")

    coarse_R = (
        (p + a_p) * L0
        - fmpq(p, 2)
        + d * fmpq(m, 2)
        + B0 * d / (2 * c)
        - fmpq(1, 7)
        + top_payment
    )
    require(coarse_R < -fmpq(1, 300), "coarse R is not below -1/300")

    J = 2 * cap_i(mu, q)
    require(J < fmpq(1, 7), "exact cap does not satisfy the Round 21 cap bound")
    exact_cap_R = coarse_R + fmpq(1, 7) - J
    require(
        exact_cap_R > fmpq(1, 20),
        "exact-cap replacement is not above 1/20",
    )

    print("GENERAL-d ROUND 22 INTRINSIC-R COUNTEREXAMPLE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print("All sign decisions use directed-rounding Arb arithmetic.")
    print("PASS exact rational phase: integer owner, f=2, n=5, p=3, m=2")
    print("PASS literal interface count: B0=1")
    print(f"lambda={lam}")
    print(f"elastic lower={elastic}")
    print(f"curvature lower={curvature}")
    print(f"exact cap J={J}")
    print(f"coarse R={coarse_R}")
    print(f"exact-cap R={exact_cap_R}")
    print("PASS coarse Round 21 R < -1/300")
    print("PASS exact-cap replacement R_J > 1/20")
    print("counterexampleScope=coarse_R_only")
    print("phiOrCSTCounterexample=False")


if __name__ == "__main__":
    main()
