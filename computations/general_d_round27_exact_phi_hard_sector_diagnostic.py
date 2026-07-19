#!/usr/bin/env python3
"""Round 27 diagnostic for the exact high-floor first-drop scalars.

This script has two purposes.

* It replays the proposed large tuple

      (r,p,m,f,alpha,t)=(4036,32,1,2,1/16,79/500)

  with the Round 20 definitions of the exact reduced scalar ``S`` and the
  raw terminal/shelf surrogate ``Phi_delta``.  The complete terminal and
  shelf loss ledger is printed.
* It runs a non-certified adversarial double-precision scan in the only
  sector not covered by the elementary ``max(0,L_T)`` argument,

      p > d*m,   e0+ep < 1/2-d*m/(2p).

  The scan keeps the two owner grids, exact shelf/activity correlations,
  ordinary versus strict floors, inverse-root fractions, terminal action
  walls, and the bad (right) sides of inverse spatial walls.  It also tests
  the exact-cap/full-``L0`` scalar ``R_J`` and its final-cap relaxation
  ``Cmax8``.

No positive output from this program is a proof.  If a negative ``S`` or
``Phi_delta`` is ever found, it must be moved to a separate directed-
rounding Arb certificate before it may be promoted.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass

import mpmath as mp

try:
    from scipy.optimize import brentq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("SciPy is required for the diagnostic scan") from exc


PI = math.pi
WALL_TOL = 5.0e-10


def strict_floor(x: float) -> int:
    """Literal [x]_<, with the integer wall owned by the lower count."""

    nearest = round(x)
    if abs(x - nearest) <= WALL_TOL:
        return max(0, nearest - 1)
    return max(0, math.ceil(x) - 1)


def ordinary_floor(x: float) -> int:
    """Literal ordinary floor, including its integer wall."""

    nearest = round(x)
    if abs(x - nearest) <= WALL_TOL:
        return max(0, nearest)
    return max(0, math.floor(x))


def ball_action(radius: float, z: float) -> float:
    if z >= radius:
        return 0.0
    theta = math.acos(z / radius)
    return radius / PI * (math.sin(theta) - theta * math.cos(theta))


def ball_integral(radius: float, z: float) -> float:
    if z >= radius:
        return 0.0
    theta = math.acos(z / radius)
    c, s = math.cos(theta), math.sin(theta)
    return radius * radius / (4 * PI) * (
        theta * (1 + 2 * c * c) - 3 * s * c
    )


def outer_radius(mu: float, t: float) -> float:
    return mu / math.cos(t)


def shell_action(mu: float, t: float, z: float) -> float:
    return ball_action(outer_radius(mu, t), z) - ball_action(mu, z)


def activity_margin(mu: float, t: float, gamma: float) -> float:
    c = math.cos(t)
    return (mu / c) ** 2 - PI * PI / (1 - c) ** 2 - gamma


def increasing_root(function, level: float = 0.0) -> float:
    lo, hi = 1.0e-7, PI / 2 - 1.0e-7
    f_lo, f_hi = function(lo) - level, function(hi) - level
    if not (f_lo <= 0 <= f_hi):
        raise ValueError("increasing root is not bracketed")
    return brentq(
        lambda value: function(value) - level,
        lo,
        hi,
        xtol=2.0e-14,
        rtol=2.0e-14,
        maxiter=120,
    )


def inverse_angle(radius: float, level: float) -> float:
    return brentq(
        lambda theta: radius
        / PI
        * (math.sin(theta) - theta * math.cos(theta))
        - level,
        1.0e-14,
        PI / 2,
        xtol=1.0e-14,
        rtol=1.0e-14,
    )


def top_payment(lam: float) -> float:
    if not 0 < lam < 1:
        return 0.0
    return min(1.0, 2 * max(0.0, 0.75 - lam) ** 2)


@dataclass(frozen=True)
class Record:
    r: float
    p: int
    m: int
    f: int
    alpha: float
    t: float
    S: float
    Phi: float
    PhiMax: float
    R_J: float
    Cmax8: float
    LT: float
    terminal_loss: float
    shelf_loss: float
    epsilon_sum: float
    automatic_threshold: float
    B: int
    Q: int
    min_eta: float


def evaluate(r: float, p: int, m: int, f: int, alpha: float, t: float) -> Record:
    q = r + p + m
    mu = q + alpha
    x = r + p
    K = outer_radius(mu, t)
    d = 1 - 2 * t / PI

    ar = shell_action(mu, t, r)
    ax = shell_action(mu, t, x)
    ax1 = shell_action(mu, t, x + 1)
    aq = shell_action(mu, t, q)
    e0, ep = ar + 0.25 - f, ax + 0.25 - f
    epsilon_sum = e0 + ep

    # Literal ownership checks.  Monotonicity between the displayed
    # endpoints gives the complete first shelf.
    if ordinary_floor(mu - r) != p + m:
        raise ValueError("ordinary interface floor changed")
    if ordinary_floor(ar + 0.25) != f or ordinary_floor(ax + 0.25) != f:
        raise ValueError("first shelf changed owner")
    if ordinary_floor(ax1 + 0.25) == f:
        raise ValueError("the first drop has not occurred")

    gamma = 0.75 if r.is_integer() else 2.0
    if activity_margin(mu, t, gamma) <= 0:
        raise ValueError("owner activity failed")

    v = ball_action(K, q)
    B = strict_floor(v + 0.25)
    Q = strict_floor(aq + 0.25)
    beta = math.acos(q / K) / PI
    delta = ball_integral(mu, q)

    angles: list[float] = []
    inverse_displacements: list[float] = []
    etas: list[float] = []
    for level_index in range(1, B + 1):
        theta = inverse_angle(K, level_index - 0.25)
        y = K * math.cos(theta) - q
        angles.append(theta)
        inverse_displacements.append(y)
        etas.append(y - strict_floor(y))

    top = max(v - B, 0.0) ** 2 / beta if B else 0.0
    LT = (
        PI / 2 * sum(1 / theta for theta in angles)
        + 2 * sum(etas)
        - Q
        - 2 * delta
        + top
    )
    Dq = (
        2 * (ball_integral(K, q) - ball_integral(mu, q))
        - Q
        - 2 * sum(strict_floor(y) for y in inverse_displacements)
    )

    Rp = 2 * (
        ball_integral(K, r)
        - ball_integral(mu, r)
        - ball_integral(K, x)
        + ball_integral(mu, x)
    ) - 2 * p * f
    Cp = 2 * (
        ball_integral(K, r)
        - ball_integral(mu, r)
        - ball_integral(K, x)
        + ball_integral(mu, x)
    ) - p * (ar + ax)
    a_p = p * p / (3 * (2 * r + p))
    Cp_lower = a_p * (e0 - ep)

    S = Dq + Rp + d * m / 2
    shelf_part = Cp_lower + p * (epsilon_sum - 0.5) + d * m / 2
    Phi = LT + shelf_part
    PhiMax = max(0.0, LT) + shelf_part

    X = m + alpha
    stretch = math.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p)))
    W = mu / PI * (math.tan(t) - t)
    lam = f - 0.25 - W
    B0 = strict_floor(W + 0.25)
    elastic = (stretch - 1) * lam
    curvature = (1 - math.cos(t)) / (PI * mu) * p * (2 * r + p) / 2
    L0 = max(elastic, curvature)
    J = 2 * ball_integral(mu, q)
    R_J = (
        (p + a_p) * L0
        - p / 2
        + d * m / 2
        + B0 * d / (2 * (t / PI))
        - J
        + top_payment(lam)
    )
    Cmax8 = R_J + J - 0.125
    threshold = 0.5 - d * m / (2 * p)

    ledger = (Dq - LT) + (Cp - Cp_lower)
    if abs((S - Phi) - ledger) > 2.0e-6 * max(1.0, abs(S)):
        raise ArithmeticError("Round 20 loss ledger did not close")

    return Record(
        r,
        p,
        m,
        f,
        alpha,
        t,
        S,
        Phi,
        PhiMax,
        R_J,
        Cmax8,
        LT,
        Dq - LT,
        Cp - Cp_lower,
        epsilon_sum,
        threshold,
        B,
        Q,
        min(etas) if etas else 1.0,
    )


def feasible_interval(
    r: float, p: int, m: int, f: int, alpha: float
) -> tuple[float, float, float, float] | None:
    q = r + p + m
    mu = q + alpha
    x = r + p
    h = f - 0.25
    gamma = 0.75 if r.is_integer() else 2.0
    lo = max(
        increasing_root(lambda t: shell_action(mu, t, x), h),
        increasing_root(lambda t: activity_margin(mu, t, gamma)),
    )
    hi = min(
        increasing_root(lambda t: shell_action(mu, t, x + 1), h),
        increasing_root(lambda t: shell_action(mu, t, r), h + 1),
    )
    return (lo, hi, mu, q) if lo < hi else None


def hard_gap(r: float, p: int, m: int, f: int, alpha: float, t: float) -> float:
    mu = r + p + m + alpha
    epsilon_sum = (
        shell_action(mu, t, r)
        + shell_action(mu, t, r + p)
        + 0.5
        - 2 * f
    )
    d = 1 - 2 * t / PI
    return epsilon_sum - (0.5 - d * m / (2 * p))


def hard_candidates(
    r: float,
    p: int,
    m: int,
    f: int,
    alpha: float,
    wall_limit: int,
) -> list[Record]:
    interval = feasible_interval(r, p, m, f, alpha)
    if interval is None:
        return []
    lo, hi, mu, q = interval

    d_lo = 1 - 2 * lo / PI
    if not (p > d_lo * m and hard_gap(r, p, m, f, alpha, lo) < 0):
        return []
    hard_hi = hi
    if hard_gap(r, p, m, f, alpha, hi) >= 0:
        hard_hi = brentq(
            lambda t: hard_gap(r, p, m, f, alpha, t),
            lo,
            hi,
            xtol=2.0e-14,
            rtol=2.0e-14,
        )
    if not lo < hard_hi:
        return []

    span = hard_hi - lo
    points = [
        lo,
        lo + span * 1.0e-7,
        lo + span * 0.1,
        lo + span * 0.25,
        lo + span * 0.5,
        lo + span * 0.75,
        lo + span * (1 - 1.0e-7),
    ]
    walls: list[float] = []
    K_lo, K_hi = outer_radius(mu, lo), outer_radius(mu, hard_hi)

    for level_index in range(1, f + 1):
        level = level_index - 0.25

        # Outer terminal-action and shell terminal-action walls.
        for function in (
            lambda t, level=level: ball_action(outer_radius(mu, t), q) - level,
            lambda t, level=level: shell_action(mu, t, q) - level,
        ):
            if function(lo) <= 0 <= function(hard_hi):
                walls.append(brentq(function, lo, hard_hi))

        # Every inverse spatial wall y_k=j is equivalently
        # G_K(q+j)=k-1/4.  Enumerate all such walls when short, and both
        # ends plus a uniform interior sample when the interval is long.
        if ball_action(K_hi, q) < level:
            continue
        theta_hi = inverse_angle(K_hi, level)
        y_hi = K_hi * math.cos(theta_hi) - q
        if ball_action(K_lo, q) >= level:
            theta_lo = inverse_angle(K_lo, level)
            y_lo = K_lo * math.cos(theta_lo) - q
        else:
            y_lo = 0.0
        j0, j1 = max(1, math.ceil(y_lo)), math.floor(y_hi)
        if j1 < j0:
            continue
        if j1 - j0 + 1 <= wall_limit:
            spatial_indices = list(range(j0, j1 + 1))
        else:
            edge = max(1, wall_limit // 3)
            spatial_indices = list(range(j0, j0 + edge))
            spatial_indices += list(range(max(j0, j1 - edge + 1), j1 + 1))
            spatial_indices += [
                round(j0 + (j1 - j0) * index / 20) for index in range(1, 20)
            ]
            spatial_indices = sorted(set(spatial_indices))

        for spatial_index in spatial_indices:
            function = lambda t, j=spatial_index, level=level: (
                ball_action(outer_radius(mu, t), q + j) - level
            )
            if function(lo) <= 0 <= function(hard_hi):
                walls.append(brentq(function, lo, hard_hi))

    # The literal wall and its bad right side are distinct records.
    right_offset = max(1.0e-9, span * 1.0e-6)
    points.extend(walls)
    points.extend(wall + right_offset for wall in walls if wall + right_offset < hard_hi)

    records: list[Record] = []
    for t in sorted(set(points)):
        if not lo <= t < hard_hi:
            continue
        try:
            record = evaluate(r, p, m, f, alpha, t)
        except (ArithmeticError, ValueError, ZeroDivisionError):
            continue
        if p > (1 - 2 * t / PI) * m and record.epsilon_sum < record.automatic_threshold:
            records.append(record)
    return records


def mp_ball_action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    return radius / mp.pi * (mp.sin(theta) - theta * mp.cos(theta))


def mp_ball_integral(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    c, s = mp.cos(theta), mp.sin(theta)
    return radius**2 / (4 * mp.pi) * (theta * (1 + 2 * c**2) - 3 * s * c)


def high_precision_fixed_replay() -> None:
    """Independent high-precision replay of the proposed large tuple."""

    mp.mp.dps = 90
    r, p, m, f = mp.mpf(4036), 32, 1, 2
    alpha, t = mp.mpf(1) / 16, mp.mpf(79) / 500
    q, mu = r + p + m, r + p + m + alpha
    K = mu / mp.cos(t)
    d = 1 - 2 * t / mp.pi

    def shell(z: mp.mpf) -> mp.mpf:
        return mp_ball_action(K, z) - mp_ball_action(mu, z)

    ar, ax, ax1, aq = shell(r), shell(r + p), shell(r + p + 1), shell(q)
    e0, ep = ar + mp.mpf(1) / 4 - f, ax + mp.mpf(1) / 4 - f
    v = mp_ball_action(K, q)
    B, Q = int(mp.floor(v + mp.mpf(1) / 4)), int(mp.floor(aq + mp.mpf(1) / 4))
    beta = mp.acos(q / K) / mp.pi
    delta = mp_ball_integral(mu, q)
    angles, ys, etas = [], [], []
    for index in range(1, B + 1):
        level = mp.mpf(index) - mp.mpf(1) / 4
        theta = mp.findroot(
            lambda value: K
            / mp.pi
            * (mp.sin(value) - value * mp.cos(value))
            - level,
            (mp.mpf("0.01"), mp.mpf("0.3")),
        )
        y = K * mp.cos(theta) - q
        angles.append(theta)
        ys.append(y)
        etas.append(y - mp.floor(y))

    top = max(v - B, 0) ** 2 / beta
    LT = (
        mp.pi / 2 * sum(1 / value for value in angles)
        + 2 * sum(etas)
        - Q
        - 2 * delta
        + top
    )
    Dq = (
        2 * (mp_ball_integral(K, q) - mp_ball_integral(mu, q))
        - Q
        - 2 * sum(mp.floor(y) for y in ys)
    )
    x = r + p
    common = 2 * (
        mp_ball_integral(K, r)
        - mp_ball_integral(mu, r)
        - mp_ball_integral(K, x)
        + mp_ball_integral(mu, x)
    )
    Rp = common - 2 * p * f
    Cp = common - p * (ar + ax)
    a_p = mp.mpf(p * p) / (3 * (2 * r + p))
    Cp_lower = a_p * (e0 - ep)
    S = Dq + Rp + d * m / 2
    Phi = LT + Cp_lower + p * (e0 + ep - mp.mpf(1) / 2) + d * m / 2

    # Exact-cap/full-L0 comparison, to expose why it is not a global target
    # without the automatic-sector split.
    X = m + alpha
    stretch = mp.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p)))
    W = mu / mp.pi * (mp.tan(t) - t)
    lam = f - mp.mpf(1) / 4 - W
    B0 = int(mp.floor(W + mp.mpf(1) / 4))
    elastic = (stretch - 1) * lam
    curvature = (1 - mp.cos(t)) / (mp.pi * mu) * p * (2 * r + p) / 2
    L0 = max(elastic, curvature)
    J = 2 * mp_ball_integral(mu, q)
    payment = min(1, 2 * max(0, mp.mpf(3) / 4 - lam) ** 2) if 0 < lam < 1 else 0
    R_J = (
        (p + a_p) * L0
        - p / 2
        + d * m / 2
        + B0 * d / (2 * (t / mp.pi))
        - J
        + payment
    )
    Cmax8 = R_J + J - mp.mpf(1) / 8
    threshold = mp.mpf(1) / 2 - d * m / (2 * p)

    def show(name: str, value: mp.mpf) -> None:
        print(f"{name}={mp.nstr(value, 45)}")

    print("ROUND 27 PROPOSED LARGE-TUPLE REPLAY (90-digit mpmath)")
    print("data: r=4036 p=32 m=1 f=2 alpha=1/16 t=79/500")
    show("K", K)
    show("rho", mp.cos(t))
    print(f"ordinary owners: n={p+m} f={f} p={p}; terminal B={B} Q={Q}")
    show("start margin", mp.mpf(11) / 4 - ar)
    show("lower shelf margin", ax - mp.mpf(7) / 4)
    show("first-drop margin", mp.mpf(7) / 4 - ax1)
    show("epsilon sum", e0 + ep)
    show("automatic threshold", threshold)
    show("inverse y1", ys[0])
    show("inverse eta1", etas[0])
    show("D_q", Dq)
    show("L_T", LT)
    show("terminal loss", Dq - LT)
    show("R_p", Rp)
    show("C_p", Cp)
    show("C_p lower", Cp_lower)
    show("shelf loss", Cp - Cp_lower)
    show("S", S)
    show("Phi_delta", Phi)
    show("ledger residual", S - Phi - (Dq - LT) - (Cp - Cp_lower))
    show("R_J", R_J)
    show("Cmax8", Cmax8)
    print("automaticSector=True")
    print("fixedReplayOK=True")


def round20_edge_fixture() -> None:
    """Replay the known eta1-down, ep=0 hard-sector intersection."""

    mp.mp.dps = 90
    # A visible one-sided displacement is used before conversion to the
    # double evaluator.  Sending 1e-30 through binary64 would round y1 back
    # to the literal wall, whose strict fraction is 1 rather than 0.
    epsilon = mp.mpf("1e-8")
    K = mp.findroot(
        lambda value: mp_ball_action(value, 7 + epsilon) - mp.mpf(3) / 4,
        (11, 11.1),
    )
    mu = mp.findroot(
        lambda value: mp_ball_action(K, 3)
        - mp_ball_action(value, 3)
        - mp.mpf(7) / 4,
        (5.03, 5.05),
    )
    t = mp.acos(mu / K)
    # The double evaluator is used only after the high-precision defining
    # equations have selected the point.
    rec = evaluate(1.0, 2, 2, 2, float(mu - 5), float(t))
    print("ROUND 20 HARD-EDGE REGRESSION")
    print(f"K={mp.nstr(K, 40)}")
    print(f"mu={mp.nstr(mu, 40)}")
    print(f"alpha={mp.nstr(mu-5, 40)}")
    print(f"t={mp.nstr(t, 40)}")
    print(f"S={rec.S:.15g}")
    print(f"Phi_delta={rec.Phi:.15g}")
    print(f"terminal loss={rec.terminal_loss:.15g}")
    print(f"shelf loss={rec.shelf_loss:.15g}")
    print(f"R_J={rec.R_J:.15g}")
    print(f"Cmax8={rec.Cmax8:.15g}")
    print("hardSector=True")


def summarize(name: str, records: list[Record], key) -> None:
    best = min(records, key=key)
    print(
        f"min {name}={key(best):.15g} at "
        f"r={best.r:g} p={best.p} m={best.m} f={best.f} "
        f"alpha={best.alpha:g} t={best.t:.15g} "
        f"E={best.epsilon_sum:.12g} threshold={best.automatic_threshold:.12g} "
        f"B={best.B} Q={best.Q} minEta={best.min_eta:.6g}"
    )


def run_scan(random_count: int, wall_limit: int) -> None:
    random.seed(20260719)
    records: list[Record] = []
    feasible_tuples = 0

    alphas = (0.0, 1 / 16, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999999)
    radii = list(range(1, 16)) + [20, 30, 50, 100, 300, 1000, 3000, 10000]
    shelf_lengths = list(range(1, 13)) + [16, 24, 32, 48, 64]
    gaps = (1, 2, 3, 4, 6, 8, 12)
    floors = (2, 3, 4, 6)

    for offset in (0.0, 0.5):
        for radius in radii:
            r = radius + offset
            if offset and r < 1.5:
                continue
            for p in shelf_lengths:
                for m in gaps:
                    for f in floors:
                        for alpha in alphas:
                            try:
                                found = hard_candidates(r, p, m, f, alpha, wall_limit)
                            except (OverflowError, ValueError, ZeroDivisionError):
                                continue
                            if found:
                                feasible_tuples += 1
                                records.extend(found)

    for _ in range(random_count):
        half_grid = random.choice((False, True))
        r = round(math.exp(random.uniform(0, math.log(1.0e6))))
        r = float(r) + (0.5 if half_grid else 0.0)
        if half_grid and r < 1.5:
            r = 1.5
        p = max(1, round(math.exp(random.uniform(0, math.log(1000)))))
        m = max(1, round(math.exp(random.uniform(0, math.log(200)))))
        f = random.choice((2, 2, 2, 3, 4, 6, 10, 16))
        alpha = random.choice(alphas + (random.random(),))
        try:
            found = hard_candidates(r, p, m, f, alpha, wall_limit)
        except (OverflowError, ValueError, ZeroDivisionError):
            continue
        if found:
            feasible_tuples += 1
            records.extend(found)

    if not records:
        raise RuntimeError("the hard-sector scan retained no records")

    print("ROUND 27 EXACT-DOMAIN HARD-SECTOR SCAN (NON-CERTIFIED)")
    print(f"feasible tuples={feasible_tuples}; retained evaluations={len(records)}")
    print("grids=integer+half-integer; random ranges r<=1e6 p<=1000 m<=200")
    print("terminal walls=literal+right side; inverse fractions=retained")
    summarize("S", records, lambda rec: rec.S)
    summarize("Phi_delta", records, lambda rec: rec.Phi)
    summarize("PhiMax", records, lambda rec: rec.PhiMax)
    summarize("R_J", records, lambda rec: rec.R_J)
    summarize("Cmax8", records, lambda rec: rec.Cmax8)
    print(f"negative S records={sum(rec.S < 0 for rec in records)}")
    print(f"negative Phi_delta records={sum(rec.Phi < 0 for rec in records)}")
    print(f"negative PhiMax records={sum(rec.PhiMax < 0 for rec in records)}")
    print(f"negative R_J records={sum(rec.R_J < 0 for rec in records)}")
    print(f"negative Cmax8 records={sum(rec.Cmax8 < 0 for rec in records)}")
    print("scanCertification=diagnostic_only")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", type=int, default=10_000)
    parser.add_argument("--wall-limit", type=int, default=120)
    parser.add_argument("--fixed-only", action="store_true")
    args = parser.parse_args()

    high_precision_fixed_replay()
    round20_edge_fixture()
    if not args.fixed_only:
        run_scan(args.random, args.wall_limit)


if __name__ == "__main__":
    main()
