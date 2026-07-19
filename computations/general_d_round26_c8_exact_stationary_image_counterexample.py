#!/usr/bin/env python3
"""Round 26 exact-image counterexample to the Round 25 lower scalar F.

This script has two deliberately separate parts.

1. The default run uses directed-rounding python-flint Arb arithmetic to
   certify an actual stationary point on the complete delicate Round 24
   shelf domain.  At that point the Round 25 scalar F is strictly negative.
2. ``--scan`` runs a non-rigorous double-precision adversarial search over
   actual feasible stationary roots.  It is only a way to find and compare
   candidate families; it is not used by the certification.

The counterexample is to F >= 0 on the exact projected stationary image.  It
is not a counterexample to C8 >= 0, CST-H, or the Polya theorem: the exact C8
value at the certified point is strongly positive.  The failure comes from
replacing the exact owner p by p_max in the negative term -p/2.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for the certified replay") from exc


ctx.prec = int(os.environ.get("GENERAL_D_ROUND26_ARB_PREC", "512"))
PI = arb.pi()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def A(value: int | fmpq) -> arb:
    return arb(value)


def ball_from_rational_endpoints(lo: fmpq, hi: fmpq) -> arb:
    """Return an Arb ball containing the exact closed interval [lo, hi]."""

    require(lo < hi, "invalid interval")
    return arb((lo + hi) / 2, (hi - lo) / 2)


def g_ball(radius: arb, z: int) -> arb:
    """Ball action G_radius(z), on a box already certified to have z < R."""

    Z = A(z)
    require(radius > Z, f"turning branch reached at z={z}")
    return ((radius * radius - Z * Z).sqrt() - Z * (Z / radius).acos()) / PI


def certify_counterexample() -> None:
    # Exact discrete/interface data.
    r, p, m, B = 12, 4, 5, 1
    alpha = fmpq(1, 2)
    f = B + 1
    q = r + p + m
    mu_q = fmpq(43, 2)
    x = r + p
    h = fmpq(7, 4)

    require(mu_q == q + alpha, "interface identity failed")
    require(0 <= alpha < 1, "alpha is outside [0,1)")

    # A rational bracket around the unique stationary root.
    t_lo = fmpq(7_257_007, 10_000_000)
    t_hi = fmpq(7_257_008, 10_000_000)
    T = ball_from_rational_endpoints(t_lo, t_hi)
    mu = A(mu_q)

    require(T > 0, "t is not positive")
    require(T < PI / 2, "t reaches pi/2")

    def terminal_action(t: arb) -> arb:
        return mu * (t.tan() - t) / PI

    def derivative(t: arb) -> arb:
        W = terminal_action(t)
        u = W - B
        C0 = fmpq(p * p * (3 * r + 2 * p), 3) / (PI * mu)
        return (
            C0 * t.sin()
            - A(m) / PI
            - B * PI / (2 * t * t)
            + 4 * u * mu * t.tan() ** 2 / PI
        )

    d_lo = derivative(A(t_lo))
    d_hi = derivative(A(t_hi))
    require(d_lo < 0, "stationary derivative is not negative at left bracket")
    require(d_hi > 0, "stationary derivative is not positive at right bracket")

    W = terminal_action(T)
    u = W - B
    Wp = mu * T.tan() ** 2 / PI
    Wpp = 2 * mu * T.tan() / (PI * T.cos() ** 2)
    C0 = fmpq(p * p * (3 * r + 2 * p), 3) / (PI * mu)
    dprime = C0 * T.cos() + B * PI / T**3 + 4 * (Wp**2 + u * Wpp)
    require(dprime > 100, "stationary derivative is not certified increasing")

    # IVT plus dprime>0 certifies one and only one stationary t in T.
    K = mu / T.cos()
    require(K > mu, "outer radius is not above the interface")
    require(mu > x + 1, "shelf samples do not lie below the interface")

    def shell(z: int) -> arb:
        return g_ball(K, z) - g_ball(mu, z)

    lower_margin = shell(x) - A(h)
    drop_margin = A(h) - shell(x + 1)
    start_margin = A(h + 1) - shell(r)
    require(lower_margin > 0, "lower shelf relation failed")
    require(drop_margin > 0, "strict first-drop relation failed")
    require(start_margin > 0, "strict start relation failed")

    require(u > 0, "u is not in the open quadratic cell")
    require(u < 1 / A(2).sqrt(), "u reaches the saturation wall")
    lam = fmpq(3, 4) - u
    require(lam > 0, "lambda is not positive")
    require(W + fmpq(1, 4) > 1, "literal B0 is below one")
    require(W + fmpq(1, 4) < 2, "literal B0 is above one")

    activity = (
        K * K
        - PI * PI / (1 - T.cos()) ** 2
        - fmpq(3, 4)
    )
    require(activity > 0, "integer-owner activity failed")

    # At the exact stationary root, Round 25 gives
    # P=p^2(3r+2p)=704.  Bound its positive inverse psi exactly.
    P_exact = p * p * (3 * r + 2 * p)
    require(P_exact == 704, "unexpected exact stationary product")

    def owner_poly(s: fmpq) -> fmpq:
        return s * s * (2 * s + 3)

    psi_lo = fmpq(659, 100)
    psi_hi = fmpq(33, 5)
    require(owner_poly(psi_lo) < P_exact, "psi lower bracket failed")
    require(owner_poly(psi_hi) > P_exact, "psi upper bracket failed")
    interface_bound = mu_q - m - 1
    require(interface_bound > psi_hi, "p_max is not the psi branch")
    psi_box = ball_from_rational_endpoints(psi_lo, psi_hi)

    z = (T / 2).tan()
    H = T.tan() - T
    L = 4 * u * (B + u) * T.tan() ** 2 / H
    M = fmpq(1, 2) - T / PI + z / PI
    N = PI / (2 * T) - 1 + PI * z / (2 * T * T)
    F_box = (
        m * M
        + B * N
        + 2 * u * u
        - z * L
        - fmpq(1, 8)
        - psi_box / 2
    )
    require(F_box < -fmpq(1, 100), "F is not certified below -1/100")

    C8_box = (
        fmpq(p * p * (3 * r + 2 * p), 3)
        * (1 - T.cos())
        / (PI * mu)
        - fmpq(p, 2)
        + fmpq(m, 2) * (1 - 2 * T / PI)
        + B * (PI / (2 * T) - 1)
        + 2 * u * u
        - fmpq(1, 8)
    )
    require(C8_box > 1, "C8 is not certified positive")

    owner_loss = (psi_box - p) / 2
    require(owner_loss > 1, "owner relaxation loss is unexpectedly small")

    R = A(m) / PI + B * PI / (2 * T * T) - L
    require(R > 0, "stationary R is not positive")

    print("GENERAL-d ROUND 26 EXACT STATIONARY-IMAGE COUNTEREXAMPLE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print("All certified sign decisions use directed-rounding Arb arithmetic.")
    print("exact data: r=12 p=4 m=5 B=1 f=2 alpha=1/2 mu=43/2")
    print(f"stationary t bracket=[{t_lo}, {t_hi}]")
    print(f"D(left)={d_lo}")
    print(f"D(right)={d_hi}")
    print(f"Dprime(T)={dprime}")
    print(f"u(T)={u}")
    print(f"lower shelf margin={lower_margin}")
    print(f"first-drop margin={drop_margin}")
    print(f"start margin={start_margin}")
    print(f"activity margin={activity}")
    print(f"psi bracket=[{psi_lo}, {psi_hi}]")
    print(f"owner relaxation loss (p_max-p)/2={owner_loss}")
    print(f"F(T)={F_box}")
    print(f"C8(T)={C8_box}")
    print("PASS exact stationary point satisfies the full shelf image")
    print("PASS F < -1/100")
    print("PASS C8 > 1")
    print("counterexampleScope=round25_F_only")
    print("c8OrCSTCounterexample=False")


@dataclass(frozen=True)
class ScanRecord:
    F: float
    C8: float
    r: float
    p: int
    m: int
    alpha: float
    t: float
    u: float
    lower_margin: float
    drop_margin: float
    start_margin: float


def run_double_scan(limit: int) -> None:
    """Non-certified search over actual feasible stationary roots, with B=1."""

    try:
        from scipy.optimize import brentq
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("SciPy is required for --scan") from exc

    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here))
    import general_d_round24_c8_wall_diagnostic as r24

    pi = math.pi
    eps = 1.0e-8

    def root(fun, level):
        return brentq(lambda t: fun(t) - level, eps, pi / 2 - eps)

    def activity_root(mu, gamma):
        return brentq(
            lambda t: (
                mu * mu / math.cos(t) ** 2
                - pi * pi / (1 - math.cos(t)) ** 2
                - gamma
            ),
            1.0e-5,
            pi / 2 - eps,
        )

    def psi(P):
        return brentq(
            lambda s: s * s * (2 * s + 3) - P,
            0.0,
            P ** (1 / 3) + 3.0,
        )

    def stationary_record(r, p, m, alpha):
        B = 1
        mu = r + p + m + alpha
        x = r + p
        h = B + 0.75
        gamma = 0.75 if float(r).is_integer() else 2.0
        try:
            lo = max(
                root(lambda t: r24.shell_action(mu, t, x), h),
                activity_root(mu, gamma),
                root(lambda t: r24.interface_action(mu, t), B),
            )
            hi = min(
                root(lambda t: r24.shell_action(mu, t, x + 1), h),
                root(lambda t: r24.shell_action(mu, t, r), h + 1),
                root(
                    lambda t: r24.interface_action(mu, t),
                    B + 1 / math.sqrt(2),
                ),
            )
        except (ValueError, ZeroDivisionError):
            return None
        if not lo < hi:
            return None

        C0 = p * p * (3 * r + 2 * p) / (3 * pi * mu)

        def derivative(t):
            u = r24.interface_action(mu, t) - B
            return (
                C0 * math.sin(t)
                - m / pi
                - B * pi / (2 * t * t)
                + 4 * u * mu * math.tan(t) ** 2 / pi
            )

        if not derivative(lo) < 0 < derivative(hi):
            return None
        t = brentq(derivative, lo, hi)
        W = r24.interface_action(mu, t)
        u = W - B
        z = math.tan(t / 2)
        H = math.tan(t) - t
        L = 4 * u * (B + u) * math.tan(t) ** 2 / H
        pmax = min(mu - m - 1, psi(p * p * (3 * r + 2 * p)))
        M = 0.5 - t / pi + z / pi
        N = pi / (2 * t) - 1 + pi * z / (2 * t * t)
        F = m * M + B * N + 2 * u * u - z * L - 0.125 - pmax / 2
        C8 = r24.c8(r, p, m, B + 1, alpha, t)
        return ScanRecord(
            F,
            C8,
            r,
            p,
            m,
            alpha,
            t,
            u,
            r24.shell_action(mu, t, x) - h,
            h - r24.shell_action(mu, t, x + 1),
            h + 1 - r24.shell_action(mu, t, r),
        )

    records = []
    for half_grid in (False, True):
        for ri in range(1, limit + 1):
            r = float(ri) + (0.5 if half_grid else 0.0)
            for p in range(1, 7):
                for m in range(1, 8):
                    for alpha in (0.0, 0.5, 0.9, 0.99):
                        rec = stationary_record(r, p, m, alpha)
                        if rec is not None:
                            records.append(rec)

    records.sort(key=lambda rec: rec.F)
    negative = [rec for rec in records if rec.F < 0]
    print("DOUBLE-PRECISION EXACT-DOMAIN SEARCH (NON-CERTIFIED)")
    print(f"owner limit={limit}; retained stationary roots={len(records)}")
    print(f"negative F records={len(negative)}")
    for rec in records[:10]:
        print(rec)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan",
        action="store_true",
        help="also run the non-certified adversarial exact-domain scan",
    )
    parser.add_argument("--limit", type=int, default=16)
    args = parser.parse_args()
    certify_counterexample()
    if args.scan:
        run_double_scan(args.limit)


if __name__ == "__main__":
    main()
