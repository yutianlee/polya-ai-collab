#!/usr/bin/env python3
"""Certified Round 27 counterexample to Cmax8 and the exact-cap scalar R_J.

The exact rational integer-owner point

    r=4036, p=32, m=1, f=2, alpha=1/16,
    mu=65105/16, t=79/500

lies on the complete high-floor first-drop domain.  Directed-rounding Arb
arithmetic proves Cmax8 < -4/3 and R_J < -6/5, even though Cmax8 retains
the literal maximum of the elasticity and curvature branches and R_J also
retains the exact local cap.

For scope control, the same replay reconstructs the Round 20 exact reduced
scalar S and lower surrogate Phi_delta.  It certifies S > 47 and Phi_delta
> 40.  Thus the witness falsifies only these later sufficient lower scalars;
it is not a counterexample to Phi_delta, S, CST-H, or the Polya theorem.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = int(os.environ.get("GENERAL_D_ROUND27_ARB_PREC", "512"))
PI = arb.pi()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def A(value: int | fmpq) -> arb:
    return arb(value)


def interval_from_rational_endpoints(lo: fmpq, hi: fmpq) -> arb:
    require(lo < hi, "invalid rational interval")
    return arb((lo + hi) / 2, (hi - lo) / 2)


def ball_action(radius: arb, z_exact: int | fmpq) -> arb:
    """G_radius(z), with the turning branch decided by an exact sign."""

    z = A(z_exact)
    if radius < z:
        return A(0)
    require(radius > z, f"unresolved turning equality at z={z_exact}")
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / PI


def ball_cap(radius: arb, z_exact: int | fmpq) -> arb:
    """Integral from z to radius of G_radius, with its zero branch."""

    z = A(z_exact)
    if radius < z:
        return A(0)
    require(radius > z, f"unresolved cap equality at z={z_exact}")
    v = z / radius
    return (
        radius
        * radius
        / (4 * PI)
        * ((1 + 2 * v * v) * v.acos() - 3 * v * (1 - v * v).sqrt())
    )


@dataclass(frozen=True)
class Result:
    lower_margin: arb
    drop_margin: arb
    post_drop_margin: arb
    start_lower_margin: arb
    start_upper_margin: arb
    activity: arb
    W: arb
    lam: arb
    elastic: arb
    curvature: arb
    cap_J: arb
    cmax8: arb
    rj: arb
    exact_s: arb
    phi_delta: arb
    shelf_endpoint_sum: arb
    hard_branch_threshold: arb
    automatic_remainder_payment: arb
    terminal_reserve: arb
    shelf_reserve: arb
    total_reserve: arb
    inverse_angle: arb
    inverse_displacement: arb


def evaluate() -> Result:
    # Exact discrete/interface data.
    r, p, m, f = 4036, 32, 1, 2
    alpha = fmpq(1, 16)
    q = r + p + m
    mu_exact = fmpq(65105, 16)
    t_exact = fmpq(79, 500)
    x = r + p
    h = fmpq(7, 4)

    require(q == 4069, "q identity changed")
    require(mu_exact == q + alpha, "interface identity failed")
    require(q <= mu_exact < q + 1, "alpha is outside [0,1)")
    require(r >= 1 and p >= 1 and m >= 1 and f >= 2, "discrete phase failed")

    mu = A(mu_exact)
    t = A(t_exact)
    K = mu / t.cos()
    require(t > 0 and t < PI / 2, "t is outside (0,pi/2)")
    require(K > mu, "outer radius is not above the interface")
    require(mu > x + 1, "paired-shelf samples do not lie below the interface")

    def shell(z: int) -> arb:
        return ball_action(K, z) - ball_action(mu, z)

    def shell_cap(z: int) -> arb:
        return ball_cap(K, z) - ball_cap(mu, z)

    # Complete paired shelves: floor f from r through x, followed by exactly
    # floor f-1 at x+1.  Spatial monotonicity fills all intermediate samples.
    lower_margin = shell(x) - A(h)
    drop_margin = A(h) - shell(x + 1)
    post_drop_margin = shell(x + 1) - A(h - 1)
    start_lower_margin = shell(r) - A(h)
    start_upper_margin = A(h + 1) - shell(r)
    require(lower_margin > 0, "lower shelf inequality failed")
    require(drop_margin > 0, "strict first-drop inequality failed")
    require(post_drop_margin > 0, "first drop skips below floor f-1")
    require(start_lower_margin > 0, "first shelf starts below floor f")
    require(start_upper_margin > 0, "first shelf starts at floor f+1")

    # Integer-owner activity (first new owner dimension d=4, gamma=3/4).
    activity = K * K - PI * PI / (1 - t.cos()) ** 2 - fmpq(3, 4)
    require(activity > 16_000_000, "integer-owner activity failed")

    # Literal terminal count and saturated top-payment cell.
    W = mu * (t.tan() - t) / PI
    u = W - 1
    lam = fmpq(3, 4) - u
    require(W + fmpq(1, 4) > 1, "literal B0 is below one")
    require(W + fmpq(1, 4) < 2, "literal B0 is above one")
    require(lam > 0 and lam < 1, "lambda is outside the top-payment strip")
    require(u > 1 / A(2).sqrt(), "top payment has not saturated")
    require(u < fmpq(3, 4), "lambda is not positive")
    B0 = 1
    top_payment = A(1)

    # Literal L0=max(elasticity,curvature).
    X = m + A(alpha)
    s = (
        1
        + A(p * (2 * r + p))
        / (X * (X + 2 * A(r) + 2 * p))
    ).sqrt()
    elastic = (s - 1) * lam
    curvature = (
        (1 - t.cos()) / (PI * mu) * A(p * (2 * r + p)) / 2
    )
    require(elastic > curvature, "elasticity is not the literal L0 branch")
    L0 = elastic

    a_p = fmpq(p * p, 3 * (2 * r + p))
    c = t / PI
    d = 1 - 2 * c
    cap_J = 2 * ball_cap(mu, q)
    require(cap_J > 0 and cap_J < fmpq(1, 8), "exact cap range failed")

    cmax8 = (
        (p + A(a_p)) * L0
        - fmpq(p, 2)
        + d * fmpq(m, 2)
        + B0 * d / (2 * c)
        + top_payment
        - fmpq(1, 8)
    )
    rj = cmax8 + fmpq(1, 8) - cap_J
    require(cmax8 < fmpq(-4, 3), "Cmax8 is not below -4/3")
    require(rj < fmpq(-6, 5), "R_J is not below -6/5")

    # Round 20 exact reduced scalar S.  At q, the terminal endpoint count is
    # one.  The doubled tail count is one for j=1,...,21 and zero thereafter.
    # The following endpoint checks, together with monotonicity of shell(z),
    # certify the complete finite count without a floating floor operation.
    require(K - q > 51 and K - q < 52, "terminal jmax cell changed")
    require(shell(q) + fmpq(1, 4) > 1, "terminal endpoint count below one")
    require(shell(q) + fmpq(1, 4) < 2, "terminal endpoint count above one")
    require(shell(q + 21) + fmpq(1, 4) > 1, "last positive tail count failed")
    require(shell(q + 22) + fmpq(1, 4) < 1, "first zero tail count failed")
    dq = 2 * shell_cap(q) - 1 - 2 * 21

    eps0 = shell(r) - A(h)
    epsp = shell(x) - A(h)
    shelf_endpoint_sum = eps0 + epsp
    hard_branch_threshold = fmpq(1, 2) - d * m / (2 * p)
    automatic_remainder_payment = (
        p * (shelf_endpoint_sum - fmpq(1, 2)) + d * m / 2
    )
    require(shelf_endpoint_sum > 1, "witness is not remainder-rich")
    require(hard_branch_threshold < fmpq(1, 2), "hard threshold is not below 1/2")
    require(
        shelf_endpoint_sum > hard_branch_threshold,
        "witness unexpectedly enters the genuinely hard remainder branch",
    )
    require(
        automatic_remainder_payment > 16,
        "automatic remainder-rich payment is not above 16",
    )
    rp = 2 * (shell_cap(r) - shell_cap(x)) - 2 * p * f
    exact_s = dq + rp + d * m / 2
    require(exact_s > 47, "exact reduced scalar S is not above 47")

    # Round 20 terminal lower bound L_T.  Here the outer terminal count B and
    # shell count Q are both one, so there is exactly one inverse angle.  The
    # rational bracket plus strict monotonicity of
    # K/pi (sin(theta)-theta cos(theta)) isolates its unique root.
    theta_lo = fmpq(1_197_675_550_878, 10_000_000_000_000)
    theta_hi = fmpq(1_197_675_550_879, 10_000_000_000_000)

    def inverse_equation(theta: arb) -> arb:
        return K / PI * (theta.sin() - theta * theta.cos()) - fmpq(3, 4)

    require(inverse_equation(A(theta_lo)) < 0, "inverse bracket left sign failed")
    require(inverse_equation(A(theta_hi)) > 0, "inverse bracket right sign failed")
    theta = interval_from_rational_endpoints(theta_lo, theta_hi)
    require(theta > 0, "inverse angle is not positive")
    # Its derivative is K theta sin(theta)/pi > 0, proving uniqueness.
    require(K * theta * theta.sin() / PI > 0, "inverse equation is not increasing")

    v = ball_action(K, q)
    inner_h = ball_action(mu, q)
    Aq = v - inner_h
    require(v + fmpq(1, 4) > 1 and v + fmpq(1, 4) < 2, "terminal B is not one")
    require(Aq + fmpq(1, 4) > 1 and Aq + fmpq(1, 4) < 2, "terminal Q is not one")
    beta = (A(q) / K).acos() / PI
    delta = ball_cap(mu, q)
    inverse_displacement = K * theta.cos() - q
    require(inverse_displacement > 21 and inverse_displacement < 22, "inverse fraction cell changed")
    eta = inverse_displacement - 21
    require(v > 1, "terminal top interval is absent")
    top = (v - 1) ** 2 / beta
    LT = PI / (2 * theta) + 2 * eta - 1 - 2 * delta + top

    cp_lower = A(a_p) * (eps0 - epsp)
    phi_shelf = cp_lower + p * (eps0 + epsp - fmpq(1, 2)) + d * m / 2
    phi_delta = LT + phi_shelf
    require(phi_delta > 40, "Phi_delta is not above 40")

    # Exact loss audit from Phi_delta down to R_J.
    terminal_rj_bound = B0 * d / (2 * c) - cap_J + top_payment
    rj_shelf_bound = (
        (p + A(a_p)) * L0 - fmpq(p, 2) + d * m / 2
    )
    terminal_reserve = LT - terminal_rj_bound
    shelf_reserve = phi_shelf - rj_shelf_bound
    total_reserve = phi_delta - rj
    require(terminal_reserve > 14, "terminal compression reserve is not above 14")
    require(shelf_reserve > 27, "shelf compression reserve is not above 27")
    require(total_reserve > 42, "total Phi_delta-to-R_J reserve is not above 42")
    require(
        (terminal_reserve + shelf_reserve - total_reserve).contains(0),
        "loss ledger identity failed",
    )

    return Result(
        lower_margin,
        drop_margin,
        post_drop_margin,
        start_lower_margin,
        start_upper_margin,
        activity,
        W,
        lam,
        elastic,
        curvature,
        cap_J,
        cmax8,
        rj,
        exact_s,
        phi_delta,
        shelf_endpoint_sum,
        hard_branch_threshold,
        automatic_remainder_payment,
        terminal_reserve,
        shelf_reserve,
        total_reserve,
        theta,
        inverse_displacement,
    )


def main() -> None:
    result = evaluate()
    print("GENERAL-d ROUND 27 EXACT R_J COUNTEREXAMPLE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print("All sign decisions use directed-rounding Arb arithmetic.")
    print("exact data: r=4036 p=32 m=1 f=2 alpha=1/16 mu=65105/16 t=79/500")
    print("ownerGrid=integer; ownerDimension=4; activityGamma=3/4")
    print(f"lower shelf margin={result.lower_margin}")
    print(f"first-drop margin={result.drop_margin}")
    print(f"post-drop floor margin={result.post_drop_margin}")
    print(f"start lower margin={result.start_lower_margin}")
    print(f"start upper margin={result.start_upper_margin}")
    print(f"activity margin={result.activity}")
    print(f"W={result.W}")
    print(f"lambda={result.lam}")
    print("literalB0=1; topPaymentCell=saturated; topPayment=1")
    print(f"elastic L0 branch={result.elastic}")
    print(f"curvature branch={result.curvature}")
    print(f"exact cap J={result.cap_J}")
    print(f"Cmax8={result.cmax8}")
    print(f"R_J={result.rj}")
    print(f"inverse angle box={result.inverse_angle}")
    print(f"inverse displacement box={result.inverse_displacement}")
    print(f"exact reduced S={result.exact_s}")
    print(f"Phi_delta={result.phi_delta}")
    print(f"shelf endpoint sum e0+ep={result.shelf_endpoint_sum}")
    print(f"hard-branch threshold={result.hard_branch_threshold}")
    print(f"automatic remainder-rich payment={result.automatic_remainder_payment}")
    print("automaticSectorCertified=True; E>1>E*=1/2-dm/(2p)")
    print(f"terminal compression reserve={result.terminal_reserve}")
    print(f"shelf compression reserve={result.shelf_reserve}")
    print(f"total Phi_delta-to-R_J reserve={result.total_reserve}")
    print("PASS complete exact high-floor first-drop domain")
    print("PASS Cmax8 < -4/3 and R_J < -6/5")
    print("PASS exact reduced S > 47 and Phi_delta > 40")
    print("counterexampleScope=Cmax8_and_R_J_only")
    print("phiOrExactSOrCSTCounterexample=False")


if __name__ == "__main__":
    main()
