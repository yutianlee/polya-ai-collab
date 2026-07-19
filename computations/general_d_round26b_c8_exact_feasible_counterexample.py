#!/usr/bin/env python3
"""Certified Round 26b counterexample to the C8 sufficient scalar.

The exact rational point

    r=57755/2, p=80, m=15, f=2, alpha=1/2,
    mu=28973, t=7801/100000

lies on the half-integer owner grid and satisfies the complete high-floor
first-drop shelf, activity, interface, and delicate quadratic-cell
conditions.  Directed-rounding Arb arithmetic proves C8 < -7.

The script also certifies a nearby unique stationary root with C8 < -7 and
evaluates the exact-cap, full-L0 correlated scalar R_J.  R_J > 20 because
the elasticity branch of L0 and the exact cap reserve repair the losses in
C8.  Consequently this is not a counterexample to R_J, Phi_delta, CST-H,
or the Polya theorem.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = int(os.environ.get("GENERAL_D_ROUND26B_ARB_PREC", "512"))
PI = arb.pi()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def A(value: int | fmpq) -> arb:
    return arb(value)


def ball_from_rational_endpoints(lo: fmpq, hi: fmpq) -> arb:
    require(lo < hi, "invalid rational interval")
    return arb((lo + hi) / 2, (hi - lo) / 2)


def g(radius: arb, z_exact: int | fmpq) -> arb:
    """Ball action G_radius(z) on the inner branch z < radius."""

    z = A(z_exact)
    require(radius > z, f"outer turning branch reached at z={z_exact}")
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / PI


def cap_i(radius_exact: fmpq, z_exact: fmpq) -> arb:
    """Exact-point local cap integral I_radius(z)."""

    radius = A(radius_exact)
    z = A(z_exact)
    require(radius > z, "cap endpoint does not lie inside radius")
    v = z / radius
    return (
        radius
        * radius
        / (4 * PI)
        * ((1 + 2 * v * v) * v.acos() - 3 * v * (1 - v * v).sqrt())
    )


@dataclass(frozen=True)
class Evaluation:
    t: arb
    u: arb
    lam: arb
    lower_margin: arb
    drop_margin: arb
    drop_lower_margin: arb
    start_margin: arb
    activity: arb
    derivative: arb
    c8: arb
    elastic: arb
    curvature: arb
    cap: arb
    elasticity_reserve: arb
    cap_reserve: arb
    rj: arb


def evaluate(t: arb) -> Evaluation:
    r = fmpq(57755, 2)
    p, m, B = 80, 15, 1
    mu_exact = fmpq(28973)
    q = r + p + m
    x = r + p
    h = fmpq(7, 4)
    mu = A(mu_exact)

    K = mu / t.cos()
    require(K > mu, "K is not above the interface radius")
    require(mu > A(x + 1), "shelf samples reach the interface")

    def shell(z: int | fmpq) -> arb:
        return g(K, z) - g(mu, z)

    lower_margin = shell(x) - A(h)
    drop_margin = A(h) - shell(x + 1)
    drop_lower_margin = shell(x + 1) - A(h - 1)
    start_margin = A(h + 1) - shell(r)

    W = mu * (t.tan() - t) / PI
    u = W - B
    lam = fmpq(3, 4) - u
    activity = K * K - PI * PI / (1 - t.cos()) ** 2 - 2

    coefficient = A(p * p) * A(3 * r + 2 * p) / (3 * PI * mu)
    derivative = (
        coefficient * t.sin()
        - A(m) / PI
        - B * PI / (2 * t * t)
        + 4 * u * mu * t.tan() ** 2 / PI
    )
    top_payment = 2 * u * u
    c8 = (
        coefficient * (1 - t.cos())
        - fmpq(p, 2)
        + fmpq(m, 2) * (1 - 2 * t / PI)
        + B * (PI / (2 * t) - 1)
        + top_payment
        - fmpq(1, 8)
    )

    X = mu - A(r + p)
    s = (
        1
        + A(p * (2 * r + p))
        / (X * (X + 2 * A(r) + 2 * p))
    ).sqrt()
    kappa = (1 - t.cos()) / (PI * mu)
    elastic = (s - 1) * lam
    curvature = kappa * A(p * (2 * r + p)) / 2
    require(elastic > curvature, "elasticity is not the literal L0 branch")
    L0 = elastic

    a_p = fmpq(p * p, 3 * (2 * r + p))
    c = t / PI
    d = 1 - 2 * c
    J = 2 * cap_i(mu_exact, q)
    rj = (
        (p + A(a_p)) * L0
        - fmpq(p, 2)
        + d * fmpq(m, 2)
        + B * d / (2 * c)
        - J
        + top_payment
    )
    elasticity_reserve = (p + A(a_p)) * (elastic - curvature)
    cap_reserve = fmpq(1, 8) - J

    # Exact domain and sign decisions, valid for both exact t and a t-box.
    require(lower_margin > 0, "lower shelf inequality failed")
    require(drop_margin > 0, "strict first-drop inequality failed")
    require(drop_lower_margin > 0, "first drop skips below floor f-1")
    require(start_margin > 0, "strict start inequality failed")
    require(activity > 0, "half-integer owner activity failed")
    require(u > 0, "u is below the delicate quadratic cell")
    require(u < 1 / A(2).sqrt(), "u reaches the saturation wall")
    require(lam > 0, "lambda is not positive")
    require(W + fmpq(1, 4) > 1, "literal B0 is below one")
    require(W + fmpq(1, 4) < 2, "literal B0 is above one")
    require(c8 < -7, "C8 is not certified below -7")
    require(J < fmpq(1, 8), "exact cap is not below 1/8")
    require(elasticity_reserve > 27, "elasticity reserve is too small")
    require(cap_reserve > fmpq(1, 10), "cap reserve is too small")
    require(rj > 20, "exact correlated scalar R_J is not above 20")

    return Evaluation(
        t,
        u,
        lam,
        lower_margin,
        drop_margin,
        drop_lower_margin,
        start_margin,
        activity,
        derivative,
        c8,
        elastic,
        curvature,
        J,
        elasticity_reserve,
        cap_reserve,
        rj,
    )


def main() -> None:
    r = fmpq(57755, 2)
    p, m = 80, 15
    alpha = fmpq(1, 2)
    q = r + p + m
    mu = fmpq(28973)
    require(mu == q + alpha, "interface identity failed")
    require(q <= mu < q + 1, "alpha is outside [0,1)")

    t_exact = fmpq(7801, 100000)
    exact = evaluate(A(t_exact))

    # The rational point is close to, but not equal to, the stationary root.
    require(exact.derivative < -fmpq(1, 100), "rational point derivative scope changed")

    root_lo = fmpq(1950261, 25000000)  # 0.07801044
    root_hi = fmpq(1560209, 20000000)  # 0.07801045
    d_lo = evaluate(A(root_lo)).derivative
    d_hi = evaluate(A(root_hi)).derivative
    require(d_lo < 0, "stationary derivative is not negative at left endpoint")
    require(d_hi > 0, "stationary derivative is not positive at right endpoint")

    T = ball_from_rational_endpoints(root_lo, root_hi)
    stationary = evaluate(T)
    mu_arb = A(mu)
    W = mu_arb * (T.tan() - T) / PI
    u = W - 1
    Wp = mu_arb * T.tan() ** 2 / PI
    Wpp = 2 * mu_arb * T.tan() / (PI * T.cos() ** 2)
    coefficient = A(p * p) * A(3 * r + 2 * p) / (3 * PI * mu_arb)
    dprime = (
        coefficient * T.cos()
        + PI / T**3
        + 4 * (Wp**2 + u * Wpp)
    )
    require(dprime > 24000, "stationary derivative is not increasing")

    print("GENERAL-d ROUND 26b EXACT FEASIBLE C8 COUNTEREXAMPLE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print("All sign decisions use directed-rounding Arb arithmetic.")
    print("exact data: r=57755/2 p=80 m=15 f=2 alpha=1/2 mu=28973")
    print("ownerGrid=half-integer; activityGamma=2")
    print(f"exact rational t={t_exact}")
    print(f"u={exact.u}")
    print(f"lambda={exact.lam}")
    print(f"lower shelf margin={exact.lower_margin}")
    print(f"first-drop margin={exact.drop_margin}")
    print(f"post-drop lower-floor margin={exact.drop_lower_margin}")
    print(f"start margin={exact.start_margin}")
    print(f"activity margin={exact.activity}")
    print(f"C8={exact.c8}")
    print(f"D(t)={exact.derivative}")
    print(f"elastic L0 branch={exact.elastic}")
    print(f"curvature branch={exact.curvature}")
    print(f"exact cap J={exact.cap}")
    print(f"elasticity reserve={exact.elasticity_reserve}")
    print(f"cap reserve={exact.cap_reserve}")
    print(f"R_J={exact.rj}")
    print(f"stationary bracket=[{root_lo}, {root_hi}]")
    print(f"D(stationary left)={d_lo}")
    print(f"D(stationary right)={d_hi}")
    print(f"Dprime(stationary box)={dprime}")
    print(f"C8(stationary box)={stationary.c8}")
    print(f"R_J(stationary box)={stationary.rj}")
    print("PASS exact rational feasible point has C8 < -7")
    print("PASS nearby unique exact stationary point has C8 < -7")
    print("PASS exact correlated scalar R_J > 20")
    print("counterexampleScope=C8_only")
    print("rjOrPhiCounterexample=False")


if __name__ == "__main__":
    main()
