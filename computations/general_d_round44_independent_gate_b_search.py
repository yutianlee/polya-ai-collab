#!/usr/bin/env python3
"""Independent Round 44 Gate-B exact-scalar falsification search.

This file does not import any Round 44 evaluator.  A broad binary64 screen is
used only to propose records.  Every retained record is rebuilt with mpmath at
high precision from

    S = D_A(q) + C_p + p (E-E_*).

The terminal count in D_A(q) is the direct strict count.  It is evaluated by
interchanging the finite spatial/level counts: if y_k is the inverse
displacement for level k-1/4, then the number of positive spatial samples at
that level is [y_k]_<.  No tangent lower bound is used for D_A.

All continuum minima are diagnostic.  Arb is used only for explicitly marked
directed checks (the selected wall brackets, the Round 27 regression, and, if
one is ever found, a negative exact-owner candidate).
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
import os
import random
from dataclasses import dataclass
from typing import Callable, Iterable

import mpmath as mp
from scipy.optimize import brentq

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError:  # pragma: no cover - the repository runtime has flint
    flint = None
    arb = ctx = fmpq = None


PI_F = math.pi
QUARTER_F = 0.25
SEARCH_SEED = 4403
DEFAULT_DPS = int(os.environ.get("GENERAL_D_ROUND44_DPS", "90"))
DEFAULT_ARB_BITS = int(os.environ.get("GENERAL_D_ROUND44_ARB_BITS", "512"))


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def ball_action_f(a: float, z: float) -> float:
    if z >= a:
        return 0.0
    return (math.sqrt((a - z) * (a + z)) - z * math.acos(z / a)) / PI_F


def ball_cap_f(a: float, z: float) -> float:
    """Integral of G_a from z to a."""

    if z >= a:
        return 0.0
    v = z / a
    return a * a / (4 * PI_F) * (
        (1 + 2 * v * v) * math.acos(v) - 3 * v * math.sqrt(1 - v * v)
    )


def shell_action_f(mu: float, t: float, z: float) -> float:
    return ball_action_f(mu / math.cos(t), z) - ball_action_f(mu, z)


_WALL_FLOAT_CACHE: dict[tuple[int, int, int], float | None] = {}


def wall_float(q2: int, B: int, alpha_code: int = 1) -> float | None:
    """Binary64 proposal root; alpha_code=1 denotes the exact alpha=1 limit."""

    key = (q2, B, alpha_code)
    if key in _WALL_FLOAT_CACHE:
        return _WALL_FLOAT_CACHE[key]
    q = q2 / 2.0
    alpha = float(alpha_code)
    mu = q + alpha
    target = B - QUARTER_F

    def residual(t: float) -> float:
        return ball_action_f(mu / math.cos(t), q) - target

    lo = 0.0
    hi = PI_F / 2 - 1.0e-10
    try:
        if residual(lo) >= 0 or residual(hi) <= 0:
            root = None
        else:
            root = brentq(residual, lo, hi, xtol=5.0e-15, rtol=1.0e-14)
    except (ArithmeticError, ValueError, OverflowError):
        root = None
    _WALL_FLOAT_CACHE[key] = root
    return root


def inverse_angle_f(K: float, q: float, beta: float, level: float) -> float:
    def residual(theta: float) -> float:
        return K / PI_F * (math.sin(theta) - theta * math.cos(theta)) - level

    return brentq(residual, 1.0e-14, PI_F * beta, xtol=5.0e-15, rtol=1.0e-14)


@dataclass(frozen=True)
class FloatCandidate:
    source: str
    r2: int
    p: int
    m: int
    B: int
    f: int
    t: float
    S: float
    E: float
    Estar: float
    ep: float
    activity: float
    min_eta: float
    max_eta: float

    @property
    def grid(self) -> str:
        return "integer" if self.r2 % 2 == 0 else "half-integer"

    @property
    def key(self) -> tuple[int, int, int, int]:
        return (self.r2, self.p, self.m, self.B)


def float_candidate(source: str, r2: int, p: int, m: int, B: int) -> FloatCandidate | None:
    """Loose binary64 owner screen followed by a direct-count S proposal."""

    r = r2 / 2.0
    x = r + p
    q = x + m
    q2 = r2 + 2 * (p + m)
    if p < 3 or m < 1 or q < 5 or B < 2:
        return None
    t = wall_float(q2, B)
    if t is None:
        return None
    mu = q + 1.0
    K = mu / math.cos(t)
    if not (0 < t < PI_F / 2 and K > mu > q > x > r > 0):
        return None

    ar = shell_action_f(mu, t, r)
    ax = shell_action_f(mu, t, x)
    ax1 = shell_action_f(mu, t, x + 1)
    sr, sx, sx1 = ar + QUARTER_F, ax + QUARTER_F, ax1 + QUARTER_F
    fr, fx = math.floor(sr), math.floor(sx)
    tol = 2.0e-7
    if fr == fx:
        f = fr
    else:
        # Retain possible shelf-wall records for the high-precision pass.
        nearest = round(sx)
        if abs(sx - nearest) > tol or abs(sr - nearest) >= 1 + tol:
            return None
        f = nearest
    if f < B or (math.floor(sx1) == f and abs(sx1 - f) > tol):
        return None
    e0, ep = sr - f, sx - f
    if min(e0, ep) < -tol or max(e0, ep) >= 1 + tol:
        return None
    E = e0 + ep
    d = 1 - 2 * t / PI_F
    Estar = (p - d * m) / (2 * p)
    if p - d * m <= 11 / 5 - tol or E >= Estar + tol:
        return None
    activity_gamma = 0.75 if r2 % 2 == 0 else 2.0
    activity = K * K - PI_F * PI_F / (1 - math.cos(t)) ** 2 - activity_gamma
    if activity <= -tol:
        return None
    h = ball_action_f(mu, q)
    v = B - QUARTER_F
    W = ball_action_f(K, mu)
    u = v - W
    beta = math.acos(q / K) / PI_F
    if not (-tol < h < u + tol and u < beta + tol and beta < 0.5 + tol):
        return None

    counts = []
    etas = []
    for k in range(1, B):
        try:
            theta = inverse_angle_f(K, q, beta, k - QUARTER_F)
        except (ArithmeticError, ValueError):
            return None
        y = K * math.cos(theta) - q
        n = math.floor(y)
        eta = y - n
        # Binary64 cannot decide an exact inverse wall.  Either adjacent cell
        # is admitted to the high-precision shortlist by using the ordinary
        # right-side proposal here.
        counts.append(n)
        etas.append(eta)
    Q = B - 1
    terminal_count = Q + 2 * sum(counts)
    Dq = 2 * (ball_cap_f(K, q) - ball_cap_f(mu, q)) - terminal_count
    seg = (
        ball_cap_f(K, r)
        - ball_cap_f(K, x)
        - ball_cap_f(mu, r)
        + ball_cap_f(mu, x)
    )
    Cp = 2 * seg - p * (ar + ax)
    S = Dq + Cp + p * (E - Estar)
    return FloatCandidate(
        source,
        r2,
        p,
        m,
        B,
        f,
        t,
        S,
        E,
        Estar,
        ep,
        activity,
        min(etas, default=1.0),
        max(etas, default=0.0),
    )


def proposal_stream(random_count: int) -> Iterable[tuple[str, int, int, int, int]]:
    """Structured compact, edge, and logarithmic proposals on both grids."""

    # Exhaustive compact block.  q is shared heavily, so wall roots are cached.
    for r2 in list(range(2, 41, 2)) + list(range(3, 42, 2)):
        for p in range(3, 49):
            for m in range(1, 25):
                for B in range(2, 13):
                    yield ("compact", r2, p, m, B)

    edge_r2 = [2, 3, 4, 5, 6, 7, 10, 11, 20, 21, 100, 101, 1000, 1001, 8072, 8073, 20000, 20001]
    edge_p = list(range(3, 21)) + [24, 32, 48, 64, 96, 128, 256, 512, 1024, 3000]
    edge_m = list(range(1, 13)) + [16, 24, 32, 64, 128, 256, 1000]
    edge_B = list(range(2, 13)) + [16, 24, 32, 48, 64, 96]
    for r2 in edge_r2:
        for p in edge_p:
            for m in edge_m:
                for B in edge_B:
                    yield ("edge", r2, p, m, B)

    rng = random.Random(SEARCH_SEED)
    B_pool = list(range(2, 17)) + [20, 24, 32, 48, 64, 96, 128, 256]
    for _ in range(random_count):
        r = max(1, round(math.exp(rng.uniform(0, math.log(1_000_000)))))
        r2 = 2 * r + rng.randrange(2)
        if r2 == 1:
            r2 = 2
        p = max(3, round(math.exp(rng.uniform(math.log(3), math.log(3000)))))
        m = max(1, round(math.exp(rng.uniform(0, math.log(1000)))))
        choices = {2, 3, 4, rng.choice(B_pool)}
        for B in sorted(choices):
            yield ("random", r2, p, m, B)


def shortlist(candidates: list[FloatCandidate], hp_limit: int) -> list[FloatCandidate]:
    """Stratified adversarial shortlist; every float negative is retained."""

    chosen: dict[tuple[int, int, int, int], FloatCandidate] = {}

    def take(rows: Iterable[FloatCandidate], count: int, key: Callable[[FloatCandidate], float]) -> None:
        for item in heapq.nsmallest(count, rows, key=key):
            chosen[item.key] = item

    negatives = [x for x in candidates if x.S < 0]
    for item in negatives:
        chosen[item.key] = item
    take(candidates, 600, lambda z: z.S)
    take((z for z in candidates if z.grid == "integer"), 250, lambda z: z.S)
    take((z for z in candidates if z.grid == "half-integer"), 250, lambda z: z.S)
    take((z for z in candidates if z.B == 2), 250, lambda z: z.S)
    take(candidates, 200, lambda z: z.Estar - z.E)
    take(candidates, 200, lambda z: abs(z.ep))
    take(candidates, 200, lambda z: z.min_eta)
    take(candidates, 200, lambda z: 1 - z.max_eta)
    take(candidates, 150, lambda z: z.activity)
    take((z for z in candidates if z.m <= 2), 200, lambda z: z.S)
    take(candidates, 150, lambda z: -z.p / z.m)
    for source in ("compact", "edge", "random"):
        take((z for z in candidates if z.source == source), 100, lambda z: z.S)

    rows = list(chosen.values())
    if len(rows) <= hp_limit or hp_limit <= 0:
        return sorted(rows, key=lambda z: (z.S, z.key))
    forced = {z.key: z for z in negatives}
    for z in heapq.nsmallest(max(0, hp_limit - len(forced)), rows, key=lambda x: x.S):
        forced[z.key] = z
    return sorted(forced.values(), key=lambda z: (z.S, z.key))


def ball_action(a: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= a:
        return mp.mpf(0)
    return (mp.sqrt((a - z) * (a + z)) - z * mp.acos(z / a)) / mp.pi


def ball_cap(a: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= a:
        return mp.mpf(0)
    v = z / a
    return a * a / (4 * mp.pi) * (
        (1 + 2 * v * v) * mp.acos(v) - 3 * v * mp.sqrt(1 - v * v)
    )


_WALL_HP_CACHE: dict[tuple[int, int, str, int], tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = {}


def solve_wall_hp(q2: int, alpha: mp.mpf, B: int, guess: float, dps: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """High-precision root plus a sign-verified (non-directed) bracket."""

    alpha_key = mp.nstr(alpha, 40)
    key = (q2, B, alpha_key, dps)
    if key in _WALL_HP_CACHE:
        return _WALL_HP_CACHE[key]
    with mp.workdps(dps):
        q = mp.mpf(q2) / 2
        mu = q + alpha
        target = mp.mpf(B) - mp.mpf(1) / 4

        def residual(t: mp.mpf) -> mp.mpf:
            return ball_action(mu / mp.cos(t), q) - target

        g = mp.mpf(guess)
        tol = mp.power(10, -(dps - 15))
        root = mp.findroot(residual, (g * (1 - mp.mpf("1e-8")), g * (1 + mp.mpf("1e-8"))), tol=tol, maxsteps=80)
        radius = mp.power(10, -(dps - 25))
        for _ in range(30):
            lo, hi = root - radius, root + radius
            flo, fhi = residual(lo), residual(hi)
            if flo < 0 < fhi:
                result = (+root, +lo, +hi, +flo, +fhi)
                _WALL_HP_CACHE[key] = result
                return result
            radius *= 10
        raise ArithmeticError("could not sign-bracket high-precision wall root")


def inverse_hp(K: mp.mpf, q: mp.mpf, theta_q: mp.mpf, k: int, B: int, dps: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    level = mp.mpf(k) - mp.mpf(1) / 4

    def residual(theta: mp.mpf) -> mp.mpf:
        return K / mp.pi * (mp.sin(theta) - theta * mp.cos(theta)) - level

    theta = theta_q * mp.power(mp.mpf(k) / B, mp.mpf(1) / 3)
    tiny = mp.power(10, -(dps - 10))
    for _ in range(30):
        value = residual(theta)
        deriv = K / mp.pi * theta * mp.sin(theta)
        new = theta - value / deriv
        if not (tiny < new < theta_q):
            new = (theta + (tiny if new <= tiny else theta_q)) / 2
        if abs(new - theta) < mp.power(10, -(dps - 18)):
            theta = new
            break
        theta = new
    radius = mp.power(10, -(dps - 25))
    for _ in range(30):
        lo, hi = theta - radius, theta + radius
        if residual(lo) < 0 < residual(hi):
            y = K * mp.cos(theta) - q
            return (+theta, +y, +lo, +hi)
        radius *= 10
    raise ArithmeticError("could not bracket inverse angle")


def floor_ambiguous(value: mp.mpf, dps: int) -> bool:
    return abs(value - mp.nint(value)) < mp.power(10, -(dps // 2))


@dataclass
class HPRecord:
    source: str
    r2: int
    p: int
    m: int
    B: int
    alpha: mp.mpf
    owner: bool
    reasons: list[str]
    data: dict[str, object]

    @property
    def key(self) -> tuple[int, int, int, int]:
        return (self.r2, self.p, self.m, self.B)

    @property
    def S(self) -> mp.mpf:
        return self.data["S"]  # type: ignore[return-value]

    @property
    def grid(self) -> str:
        return "integer" if self.r2 % 2 == 0 else "half-integer"


def evaluate_hp(candidate: FloatCandidate, dps: int, alpha: mp.mpf | None = None) -> HPRecord:
    """Reconstruct an endpoint record and its full exact loss ledger."""

    with mp.workdps(dps):
        alpha = mp.mpf(1) if alpha is None else mp.mpf(alpha)
        r = mp.mpf(candidate.r2) / 2
        p, m, B = candidate.p, candidate.m, candidate.B
        x = r + p
        q = x + m
        q2 = candidate.r2 + 2 * (p + m)
        root, wall_lo, wall_hi, wall_flo, wall_fhi = solve_wall_hp(q2, alpha, B, candidate.t, dps)
        mu = q + alpha
        K = mu / mp.cos(root)
        A = lambda z: ball_action(K, z) - ball_action(mu, z)
        ar, ax, ax1, aq = A(r), A(x), A(x + 1), A(q)
        sr, sx, sx1 = ar + mp.mpf(1) / 4, ax + mp.mpf(1) / 4, ax1 + mp.mpf(1) / 4
        reasons: list[str] = []
        if floor_ambiguous(sr, dps) or floor_ambiguous(sx, dps) or floor_ambiguous(sx1, dps):
            reasons.append("unresolved shelf integer wall")
        fr, fx, fx1 = int(mp.floor(sr)), int(mp.floor(sx)), int(mp.floor(sx1))
        f = fr
        if fr != fx:
            reasons.append("common shelf fails")
        if fx1 == f:
            reasons.append("literal first drop fails")
        if f < B:
            reasons.append("j=f-B<0")
        e0, ep = sr - f, sx - f
        E = e0 + ep
        Delta = e0 - ep
        d = 1 - 2 * root / mp.pi
        zeta = mp.pi / (2 * root) - 1
        Estar = (p - d * m) / (2 * p)
        if p < 3:
            reasons.append("p<3")
        if m < 1:
            reasons.append("m<1")
        if q < 5:
            reasons.append("q<5")
        if not (p > d * m):
            reasons.append("p<=d m")
        if not (p - d * m > mp.mpf(11) / 5):
            reasons.append("p-d m<=11/5")
        if not (0 <= E < Estar < mp.mpf(1) / 2):
            reasons.append("hard E owner fails")
        gamma = mp.mpf(3) / 4 if candidate.r2 % 2 == 0 else mp.mpf(2)
        activity = K * K - mp.pi * mp.pi / (1 - mp.cos(root)) ** 2 - gamma
        if not (activity > 0):
            reasons.append("dimension-labelled activity fails")

        v = mp.mpf(B) - mp.mpf(1) / 4
        h = ball_action(mu, q)
        W = ball_action(K, mu)
        u = v - W
        beta = mp.acos(q / K) / mp.pi
        if not (0 < h < u < beta < mp.mpf(1) / 2):
            reasons.append("0<h<u<beta<1/2 fails")
        if not (u < alpha / 2):
            reasons.append("u<alpha/2 fails")
        B0 = B - 1
        j = f - B
        if B0 < 1:
            reasons.append("B0<1")
        if f - 1 != B0 + j:
            reasons.append("synchronized count identity fails")
        Q = B0
        q_count_cell = aq + mp.mpf(1) / 4
        if not (B0 < q_count_cell < B):
            reasons.append("direct shell endpoint count Q=B0 fails")

        theta_q = mp.pi * beta
        inverse_rows: list[dict[str, object]] = []
        omega = mp.mpf(0)
        spatial_count_sum = 0
        count_margin = mp.inf
        possible_collision = False
        for k in range(1, B):
            theta, y, theta_lo, theta_hi = inverse_hp(K, q, theta_q, k, B, dps)
            nearest = int(mp.nint(y))
            distance = abs(y - nearest)
            collision_tol = mp.power(10, -(dps // 2))
            if distance < collision_tol:
                possible_collision = True
                # Outer-gap ownership is the adverse side.  At an exact old
                # inverse wall it has count nearest and eta=0.  The literal
                # value is recorded separately below.
                count = nearest
                eta = mp.mpf(0)
                side = "unresolved-exact-collision: adverse-owner-used"
                literal_count = nearest - 1
                literal_eta = mp.mpf(1)
                count_margin = mp.mpf(0)
            else:
                count = int(mp.floor(y))
                eta = y - count
                literal_count = count
                literal_eta = eta
                count_margin = min(count_margin, eta, 1 - eta)
                side = "adverse-near" if eta < mp.mpf("1e-12") else ("literal-near" if 1 - eta < mp.mpf("1e-12") else "interior")
            spatial_count_sum += count
            omega += mp.pi / (2 * theta) - mp.pi / (2 * root) + 2 * eta
            inverse_rows.append(
                {
                    "k": k,
                    "theta": +theta,
                    "theta_lo": +theta_lo,
                    "theta_hi": +theta_hi,
                    "y": +y,
                    "count_adverse": count,
                    "eta_adverse": +eta,
                    "count_literal": literal_count,
                    "eta_literal": +literal_eta,
                    "side": side,
                }
            )
        if possible_collision:
            reasons.append("old-inverse equality unresolved at finite precision")

        terminal_count = Q + 2 * spatial_count_sum
        Dq = 2 * (ball_cap(K, q) - ball_cap(mu, q)) - terminal_count
        # Literal simultaneous-inverse value differs only at exact collisions.
        literal_spatial_sum = sum(int(row["count_literal"]) for row in inverse_rows)
        Dq_literal = 2 * (ball_cap(K, q) - ball_cap(mu, q)) - (Q + 2 * literal_spatial_sum)

        segment = ball_cap(K, r) - ball_cap(K, x) - ball_cap(mu, r) + ball_cap(mu, x)
        Cp = 2 * segment - p * (ar + ax)
        ap = mp.mpf(p * p) / (3 * (2 * r + p))
        rhs = p * (Estar - E)
        shelf_payment = p * (E - Estar)
        S = Dq + Cp + shelf_payment
        Rp = Cp + p * (E - mp.mpf(1) / 2)
        S_alt = Dq + Rp + d * m / 2
        curvature_reserve = p**3 / (6 * mp.pi) * (
            1 / mp.sqrt(mu * mu - r * r) - 1 / mp.sqrt(K * K - r * r)
        )
        J = 2 * ball_cap(mu, q)
        Lplus = omega + B0 * zeta + 1 / (2 * beta) - J
        Lzero = omega + B0 * zeta + mp.mpf(9) / (16 * beta) - J
        Rplus = Dq - Lplus
        Rzero = Dq - Lzero
        phi = Lplus + ap * Delta + shelf_payment
        ledger_rhs = Rplus + (Cp - ap * Delta)
        ledger_rhs_zero = 1 / (16 * beta) + Rzero + (Cp - ap * Delta)
        terminal_relation = Rplus - Rzero - 1 / (16 * beta)
        scalar_relation = S - phi - ledger_rhs
        scalar_relation_zero = S - phi - ledger_rhs_zero
        literal_omega = sum(
            mp.pi / (2 * row["theta"]) - mp.pi / (2 * root) + 2 * row["eta_literal"]  # type: ignore[operator]
            for row in inverse_rows
        )
        literal_Lplus = literal_omega + B0 * zeta + 1 / (2 * beta) - J
        literal_Lzero = literal_omega + B0 * zeta + mp.mpf(9) / (16 * beta) - J

        data: dict[str, object] = {
            "r": +r,
            "x": +x,
            "q": +q,
            "mu": +mu,
            "K": +K,
            "t": +root,
            "wall_lo": +wall_lo,
            "wall_hi": +wall_hi,
            "wall_flo": +wall_flo,
            "wall_fhi": +wall_fhi,
            "wall_width": +(wall_hi - wall_lo),
            "d": +d,
            "zeta": +zeta,
            "f": f,
            "B0": B0,
            "j": j,
            "n_count": f - 1,
            "e0": +e0,
            "ep": +ep,
            "E": +E,
            "Delta": +Delta,
            "Estar": +Estar,
            "hard_margin": +(Estar - E),
            "p_minus_dm": +(p - d * m),
            "activity": +activity,
            "activity_gamma": +gamma,
            "h": +h,
            "W": +W,
            "u": +u,
            "beta": +beta,
            "Q": Q,
            "B_lit": B0,
            "direct_terminal_count": terminal_count,
            "direct_terminal_count_literal_collision": Q + 2 * literal_spatial_sum,
            "count_cell_margin": +count_margin,
            "inverse_rows": inverse_rows,
            "D_A": +Dq,
            "D_A_literal_collision": +Dq_literal,
            "L_T_plus": +Lplus,
            "L_T_zero": +Lzero,
            "R_tan_plus": +Rplus,
            "R_tan_zero": +Rzero,
            "C_p": +Cp,
            "a_p": +ap,
            "a_p_Delta": +(ap * Delta),
            "curvature_reserve": +curvature_reserve,
            "curvature_reserve_slack": +(Cp - curvature_reserve),
            "shelf_trapezoid_slack": +(Cp - ap * Delta),
            "p_Estar_minus_E": +rhs,
            "p_E_minus_Estar": +shelf_payment,
            "R_p": +Rp,
            "Phi_delta_plus": +phi,
            "S": +S,
            "S_alt": +S_alt,
            "S_alt_residual": +(S - S_alt),
            "terminal_relation_residual": +terminal_relation,
            "scalar_ledger_residual": +scalar_relation,
            "scalar_ledger_zero_residual": +scalar_relation_zero,
            "literal_L_T_plus": +literal_Lplus,
            "literal_L_T_zero": +literal_Lzero,
            "possible_inverse_collision": possible_collision,
            "alpha_label": "upper-alpha one-sided" if alpha == 1 else "alpha=1-10^-j diagnostic",
        }
        return HPRecord(candidate.source, candidate.r2, p, m, B, +alpha, not reasons, reasons, data)


def mp_text(value: object, digits: int = 30) -> object:
    if isinstance(value, mp.mpf):
        return mp.nstr(value, digits)
    if isinstance(value, list):
        return [mp_text(x, digits) for x in value]
    if isinstance(value, dict):
        return {str(k): mp_text(v, digits) for k, v in value.items()}
    return value


LEDGER_KEYS = (
    "r",
    "p_placeholder",
    "x",
    "q",
    "mu",
    "K",
    "t",
    "f",
    "B0",
    "j",
    "d",
    "e0",
    "ep",
    "E",
    "Estar",
    "hard_margin",
    "p_minus_dm",
    "activity",
    "h",
    "u",
    "beta",
    "Q",
    "B_lit",
    "direct_terminal_count",
    "D_A",
    "L_T_plus",
    "L_T_zero",
    "R_tan_plus",
    "R_tan_zero",
    "C_p",
    "a_p_Delta",
    "curvature_reserve",
    "curvature_reserve_slack",
    "shelf_trapezoid_slack",
    "p_Estar_minus_E",
    "Phi_delta_plus",
    "S",
    "terminal_relation_residual",
    "scalar_ledger_residual",
    "scalar_ledger_zero_residual",
    "wall_lo",
    "wall_hi",
    "wall_flo",
    "wall_fhi",
    "wall_width",
    "count_cell_margin",
    "possible_inverse_collision",
)


def ledger_dict(record: HPRecord) -> dict[str, object]:
    result: dict[str, object] = {
        "source": record.source,
        "grid": record.grid,
        "r2": record.r2,
        "p": record.p,
        "m": record.m,
        "B": record.B,
        "alpha": record.alpha,
        "owner": record.owner,
        "reasons": record.reasons,
    }
    for key in LEDGER_KEYS:
        if key == "p_placeholder":
            continue
        result[key] = record.data[key]
    rows = record.data["inverse_rows"]
    if rows:
        adverse_row = min(rows, key=lambda row: row["eta_adverse"])
        literal_row = min(rows, key=lambda row: 1 - row["eta_adverse"])
        result["inverse_summary"] = {
            "level_count": len(rows),
            "spatial_count_sum": sum(int(row["count_adverse"]) for row in rows),
            "nearest_adverse": adverse_row,
            "nearest_literal": literal_row,
            "all_rows": rows if len(rows) <= 8 else "retained internally; omitted from stdout when B0>8",
        }
    else:
        result["inverse_summary"] = {"level_count": 0, "spatial_count_sum": 0, "all_rows": []}
    return result


def print_ledger(label: str, record: HPRecord, digits: int = 34) -> None:
    print(f"LEDGER {label}=" + json.dumps(mp_text(ledger_dict(record), digits), sort_keys=True))


def curvature_kernel_check(record: HPRecord, dps: int) -> tuple[mp.mpf, mp.mpf]:
    with mp.workdps(dps):
        r = record.data["r"]
        p = mp.mpf(record.p)
        mu = record.data["mu"]
        K = record.data["K"]

        def integrand(s: mp.mpf) -> mp.mpf:
            z = r + s
            return s * (p - s) / mp.pi * (
                1 / mp.sqrt(mu * mu - z * z) - 1 / mp.sqrt(K * K - z * z)
            )

        kernel = mp.quad(integrand, [0, p / 2, p])
        return +kernel, +(kernel - record.data["C_p"])


def exact_decimal_q(value: mp.mpf, digits: int, lower: bool) -> fmpq:
    scale = 10**digits
    scaled = value * scale
    integer = int(mp.floor(scaled) if lower else mp.ceil(scaled))
    return fmpq(integer, scale)


def arb_ball_action(radius: arb, z_exact: fmpq | int) -> arb:
    z = arb(z_exact)
    if radius < z:
        return arb(0)
    require(radius > z, "Arb turning equality unresolved")
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / arb.pi()


def arb_ball_cap(radius: arb, z_exact: fmpq | int) -> arb:
    z = arb(z_exact)
    if radius < z:
        return arb(0)
    require(radius > z, "Arb cap turning equality unresolved")
    v = z / radius
    return radius * radius / (4 * arb.pi()) * (
        (1 + 2 * v * v) * v.acos() - 3 * v * (1 - v * v).sqrt()
    )


def arb_wall_bracket(record: HPRecord, digits: int = 60) -> dict[str, object]:
    """Directed verification of a selected endpoint wall bracket."""

    require(flint is not None, "python-flint unavailable")
    ctx.prec = DEFAULT_ARB_BITS
    lo_q = exact_decimal_q(record.data["t"], digits, True)
    hi_q = exact_decimal_q(record.data["t"], digits, False)
    if lo_q == hi_q:
        hi_q += fmpq(1, 10**digits)
    q_exact = fmpq(record.r2 + 2 * (record.p + record.m), 2)
    if record.alpha == 1:
        alpha_exact = fmpq(1)
    else:
        alpha_exact = fmpq(str(mp.nstr(record.alpha, 80)))
    mu_exact = q_exact + alpha_exact
    target = fmpq(record.B) - fmpq(1, 4)

    def residual(tq: fmpq) -> arb:
        t = arb(tq)
        K = arb(mu_exact) / t.cos()
        return arb_ball_action(K, q_exact) - target

    flo, fhi = residual(lo_q), residual(hi_q)
    require(flo < 0 and fhi > 0, "directed wall bracket signs failed")
    return {
        "bits": ctx.prec,
        "lo": str(lo_q),
        "hi": str(hi_q),
        "F_lo": str(flo),
        "F_hi": str(fhi),
        "directed": True,
    }


def round27_regression(dps: int) -> dict[str, object]:
    """Independent high-precision reconstruction of the automatic witness."""

    with mp.workdps(dps):
        r, p, m, f = mp.mpf(4036), 32, 1, 2
        alpha = mp.mpf(1) / 16
        q = r + p + m
        mu = q + alpha
        t = mp.mpf(79) / 500
        K = mu / mp.cos(t)
        x = r + p
        A = lambda z: ball_action(K, z) - ball_action(mu, z)
        d = 1 - 2 * t / mp.pi
        e0 = A(r) - mp.mpf(7) / 4
        ep = A(x) - mp.mpf(7) / 4
        E = e0 + ep
        Estar = (p - d * m) / (2 * p)
        # Direct strict count: endpoint 1; doubled samples j=1,...,21 each 1.
        Dq = 2 * (ball_cap(K, q) - ball_cap(mu, q)) - 43
        Rp = 2 * (
            ball_cap(K, r) - ball_cap(K, x) - ball_cap(mu, r) + ball_cap(mu, x)
        ) - 2 * p * f
        S = Dq + Rp + d * m / 2
        W = mu / mp.pi * (mp.tan(t) - t)
        u = W - 1
        lam = mp.mpf(3) / 4 - u
        ap = mp.mpf(p * p) / (3 * (2 * r + p))
        X = m + alpha
        stretch = mp.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p)))
        elastic = (stretch - 1) * lam
        curvature = (1 - mp.cos(t)) / (2 * mp.pi * mu) * p * (2 * r + p)
        L0 = max(elastic, curvature)
        capJ = 2 * ball_cap(mu, q)
        c = t / mp.pi
        cmax8 = (p + ap) * L0 - p / 2 + d * m / 2 + d / (2 * c) + 1 - mp.mpf(1) / 8
        rj = cmax8 + mp.mpf(1) / 8 - capJ
        return {
            "r": r,
            "p": p,
            "m": m,
            "f": f,
            "alpha": alpha,
            "t": t,
            "E": E,
            "Estar": Estar,
            "E_minus_Estar": E - Estar,
            "D_A": Dq,
            "R_p": Rp,
            "S": S,
            "Cmax8": cmax8,
            "R_J": rj,
            "negative_rejected_scalars": cmax8 < 0 and rj < 0,
            "automatic_rejection": E > Estar,
            "large_positive_S": S > 47,
        }


def round27_arb_check() -> dict[str, object]:
    require(flint is not None, "python-flint unavailable")
    ctx.prec = DEFAULT_ARB_BITS
    pi = arb.pi()
    r, p, m, f = 4036, 32, 1, 2
    q = 4069
    alpha = fmpq(1, 16)
    mu_q = fmpq(65105, 16)
    t_q = fmpq(79, 500)
    mu, t = arb(mu_q), arb(t_q)
    K = mu / t.cos()
    x = r + p
    shell = lambda z: arb_ball_action(K, z) - arb_ball_action(mu, z)
    cap = lambda z: arb_ball_cap(K, z) - arb_ball_cap(mu, z)
    require(1 < shell(q) + fmpq(1, 4) < 2, "Round27 endpoint count")
    require(1 < shell(q + 21) + fmpq(1, 4) < 2, "Round27 last tail count")
    require(shell(q + 22) + fmpq(1, 4) < 1, "Round27 first zero tail count")
    Dq = 2 * cap(q) - 43
    Rp = 2 * (cap(r) - cap(x)) - 2 * p * f
    d = 1 - 2 * t / pi
    S = Dq + Rp + d * m / 2
    e0 = shell(r) - fmpq(7, 4)
    ep = shell(x) - fmpq(7, 4)
    E = e0 + ep
    Estar = (p - d * m) / (2 * p)
    W = mu * (t.tan() - t) / pi
    u = W - 1
    lam = fmpq(3, 4) - u
    ap = fmpq(p * p, 3 * (2 * r + p))
    X = arb(m) + alpha
    stretch = (1 + arb(p * (2 * r + p)) / (X * (X + 2 * r + 2 * p))).sqrt()
    elastic = (stretch - 1) * lam
    curvature = (1 - t.cos()) / (2 * pi * mu) * p * (2 * r + p)
    require(elastic > curvature, "Round27 L0 branch")
    capJ = 2 * arb_ball_cap(mu, q)
    c = t / pi
    cmax8 = (p + arb(ap)) * elastic - fmpq(p, 2) + d * m / 2 + d / (2 * c) + 1 - fmpq(1, 8)
    rj = cmax8 + fmpq(1, 8) - capJ
    require(cmax8 < fmpq(-4, 3), "Round27 Cmax8 directed sign")
    require(rj < fmpq(-6, 5), "Round27 R_J directed sign")
    require(S > 47, "Round27 S directed sign")
    require(E > Estar, "Round27 automatic-sector directed sign")
    return {
        "bits": ctx.prec,
        "Cmax8": str(cmax8),
        "R_J": str(rj),
        "S": str(S),
        "E_minus_Estar": str(E - Estar),
        "directed": True,
    }


def round43_candidate(dps: int) -> FloatCandidate:
    r2, p, m, B = 2, 9, 9, 3
    t = wall_float(r2 + 2 * (p + m), B)
    require(t is not None, "Round43 wall root missing")
    # It deliberately fails only the hard E owner, so bypass the screen.
    return FloatCandidate("round43-regression", r2, p, m, B, 4, t, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def owner_summary(record: HPRecord) -> str:
    return (
        f"r={mp.nstr(record.data['r'], 12)} p={record.p} m={record.m} "
        f"f={record.data['f']} B={record.B} B0={record.data['B0']} j={record.data['j']} "
        f"grid={record.grid} S={mp.nstr(record.S, 24)}"
    )


def convergence_rows(best: HPRecord, dps: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    base = FloatCandidate(
        "convergence",
        best.r2,
        best.p,
        best.m,
        best.B,
        int(best.data["f"]),
        float(best.data["t"]),
        float(best.S),
        float(best.data["E"]),
        float(best.data["Estar"]),
        float(best.data["ep"]),
        float(best.data["activity"]),
        0,
        0,
    )
    for exponent in (3, 6, 9, 12):
        alpha = mp.mpf(1) - mp.power(10, -exponent)
        rec = evaluate_hp(base, dps, alpha=alpha)
        rows.append(
            {
                "exponent": exponent,
                "alpha": alpha,
                "t_solved_separately": rec.data["t"],
                "K": rec.data["K"],
                "owner": rec.owner,
                "reasons": rec.reasons,
                "S": rec.data["S"],
                "S_minus_endpoint": rec.data["S"] - best.data["S"],
                "wall_width": rec.data["wall_width"],
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--random", type=int, default=3500)
    parser.add_argument("--hp-limit", type=int, default=2200)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    dps = max(70, args.dps)
    random_count = 300 if args.quick else args.random
    hp_limit = 350 if args.quick else args.hp_limit
    mp.mp.dps = dps

    print("ROUND44 INDEPENDENT GATE-B EXACT-SCALAR FALSIFICATION")
    print("lead_round44_evaluator_imported=False")
    print("search_target=S=D_A(q)+C_p+p(E-Estar)")
    print("projected_scalar_substitution=False")
    print("finite_search_classification=diagnostic_only")
    print(f"mpmath_dps={dps}; random_seed={SEARCH_SEED}; quick={args.quick}")

    seen: set[tuple[int, int, int, int]] = set()
    candidates: list[FloatCandidate] = []
    proposals = 0
    for source, r2, p, m, B in proposal_stream(random_count):
        key = (r2, p, m, B)
        if key in seen:
            continue
        seen.add(key)
        proposals += 1
        item = float_candidate(source, r2, p, m, B)
        if item is not None:
            candidates.append(item)
    selected = shortlist(candidates, hp_limit)
    print(f"binary64_proposals={proposals}")
    print(f"binary64_owner_candidates={len(candidates)}")
    print(f"binary64_negative_S_candidates={sum(x.S < 0 for x in candidates)}")
    print(f"high_precision_shortlist={len(selected)}")

    hp_records: list[HPRecord] = []
    rejected_hp = 0
    for item in selected:
        record = evaluate_hp(item, dps)
        if record.owner:
            hp_records.append(record)
        else:
            rejected_hp += 1
    print(f"high_precision_exact_owner_records={len(hp_records)}")
    print(f"high_precision_rejected_after_exact_recheck={rejected_hp}")
    if not hp_records:
        raise SystemExit("no exact-owner record survived the high-precision recheck")

    hp_records.sort(key=lambda z: z.S)
    negatives = [z for z in hp_records if z.S < 0]
    print(f"high_precision_negative_owner_records={len(negatives)}")
    print("gate_trigger_certificate_found=False" if not negatives else "gate_trigger_candidate_found=True")
    print(
        "high_precision_owner_ranges "
        f"r=[{mp.nstr(min(z.data['r'] for z in hp_records), 12)},"
        f"{mp.nstr(max(z.data['r'] for z in hp_records), 12)}] "
        f"p=[{min(z.p for z in hp_records)},{max(z.p for z in hp_records)}] "
        f"m=[{min(z.m for z in hp_records)},{max(z.m for z in hp_records)}] "
        f"B=[{min(z.B for z in hp_records)},{max(z.B for z in hp_records)}]"
    )
    print(
        "high_precision_owner_counts "
        f"integer={sum(z.grid == 'integer' for z in hp_records)} "
        f"half_integer={sum(z.grid == 'half-integer' for z in hp_records)} "
        f"B0_equals_1={sum(z.B == 2 for z in hp_records)} "
        f"compact={sum(z.source == 'compact' for z in hp_records)} "
        f"edge={sum(z.source == 'edge' for z in hp_records)} "
        f"random={sum(z.source == 'random' for z in hp_records)}"
    )

    best = hp_records[0]
    print("diagnostic_only global_min " + owner_summary(best))
    for grid in ("integer", "half-integer"):
        rows = [z for z in hp_records if z.grid == grid]
        if rows:
            print(f"diagnostic_only {grid}_min " + owner_summary(min(rows, key=lambda z: z.S)))
    b01 = [z for z in hp_records if z.B == 2]
    if b01:
        print("diagnostic_only B0_equals_1_min " + owner_summary(min(b01, key=lambda z: z.S)))
    m1 = [z for z in hp_records if z.m == 1]
    if m1:
        print("diagnostic_only m_equals_1_min " + owner_summary(min(m1, key=lambda z: z.S)))
    large_p = [z for z in hp_records if z.p >= 20]
    if large_p:
        print("diagnostic_only p_at_least_20_min " + owner_summary(min(large_p, key=lambda z: z.S)))
        print("diagnostic_only largest_p_record " + owner_summary(max(large_p, key=lambda z: z.p)))
    for field in ("D_A", "C_p", "R_tan_plus", "R_tan_zero", "curvature_reserve_slack", "shelf_trapezoid_slack"):
        row = min(hp_records, key=lambda z, field=field: z.data[field])
        print(
            f"diagnostic_only min_{field}={mp.nstr(row.data[field], 24)} at "
            + owner_summary(row)
        )

    labels: list[tuple[str, HPRecord]] = [("global_min", best)]
    for name, rows, key in (
        ("near_Estar", hp_records, lambda z: z.data["hard_margin"]),
        ("near_ep_zero", hp_records, lambda z: abs(z.data["ep"])),
        ("near_adverse_inverse", hp_records, lambda z: min((row["eta_adverse"] for row in z.data["inverse_rows"]), default=mp.mpf(1))),
        ("near_literal_inverse", hp_records, lambda z: min((1 - row["eta_adverse"] for row in z.data["inverse_rows"]), default=mp.mpf(1))),
        ("curvature_tight", hp_records, lambda z: z.data["curvature_reserve_slack"]),
    ):
        labels.append((name, min(rows, key=key)))
    if large_p:
        labels.append(("large_p_min", min(large_p, key=lambda z: z.S)))
    emitted: set[tuple[int, int, int, int]] = set()
    for label, record in labels:
        if record.key not in emitted:
            print_ledger(label, record)
            emitted.add(record.key)

    kernel, kernel_residual = curvature_kernel_check(best, dps)
    print("CURVATURE_KERNEL_CHECK=" + json.dumps(mp_text({"kernel_integral": kernel, "C_p": best.data["C_p"], "residual": kernel_residual, "reserve": best.data["curvature_reserve"], "reserve_slack": best.data["curvature_reserve_slack"]}, 40), sort_keys=True))
    print("ARB_SELECTED_WALL_BRACKET=" + json.dumps(arb_wall_bracket(best), sort_keys=True))

    r43 = evaluate_hp(round43_candidate(dps), dps)
    print("ROUND43_REGRESSION=" + json.dumps(mp_text({
        "tuple": "(r,p,m,f,B,j)=(1,9,9,4,3,1)",
        "common_shelf": r43.data["f"] == 4,
        "first_drop_floor": int(mp.floor(ball_action(r43.data["K"], r43.data["x"] + 1) - ball_action(r43.data["mu"], r43.data["x"] + 1) + mp.mpf(1) / 4)),
        "E": r43.data["E"],
        "Estar": r43.data["Estar"],
        "E_minus_Estar": r43.data["E"] - r43.data["Estar"],
        "rejected_because_E_gt_Estar": r43.data["E"] > r43.data["Estar"],
        "other_reasons": [x for x in r43.reasons if x != "hard E owner fails"],
        "S_diagnostic": r43.data["S"],
        "wall_bracket": arb_wall_bracket(r43),
    }, 40), sort_keys=True))

    r27 = round27_regression(dps)
    print("ROUND27_REGRESSION=" + json.dumps(mp_text(r27, 40), sort_keys=True))
    print("ROUND27_DIRECTED_CHECK=" + json.dumps(round27_arb_check(), sort_keys=True))

    print("ALPHA_CONVERGENCE=" + json.dumps(mp_text(convergence_rows(best, dps), 38), sort_keys=True))

    if negatives:
        # A floating/high-precision negative is not promoted.  Emit all data
        # loudly and fail so that a directed interval audit is mandatory.
        for index, record in enumerate(negatives[:20], 1):
            print_ledger(f"NEGATIVE_OWNER_CANDIDATE_{index}", record, digits=50)
        print("gate_trigger_certificate_found=False")
        print("negative_status=high_precision_diagnostic_requires_directed_full-owner_certificate")
        raise SystemExit(2)

    print("negative_owner_witness_found=False")
    print("positive_coverage_certificate=False")
    print("conclusion=finite_positive_diagnostic_only; Gate-B universal sign remains open")


if __name__ == "__main__":
    main()
