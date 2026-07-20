#!/usr/bin/env python3
"""Round 46C independent exact-owner falsification search for (R45.18).

Independence boundary
---------------------
This program imports only the audited independent Round-45 definition
engine ``general_d_round45_independent_support_search``.  It never imports a
Round-46 lead evaluator.  The inherited engine supplies the exact owner,
direct strict terminal count, shelf payment, and Round-44/45 support ledgers.
This file adds the *literal* right-minus-left margin of (R45.18):

    p R1 (A(x)-A(q))
      + pi^2 B0/(K t^3 sin(t)) (W/2-B0/4+1/48)
      + B0 zeta + 9/(16 beta) - J + top + curvature
      - (p-d m)/2.

Binary64 and mpmath searches are diagnostic.  Every emitted classification
is reconstructed with directed Arb arithmetic on a rationally bracketed,
unique outer-wall root and separately bracketed, unique inverse roots.  A
finite positive sample is never promoted to coverage.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import os
import random
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

import mpmath as mp

import general_d_round45_independent_support_search as r45

try:
    from flint import arb, ctx, fmpq
except ImportError:  # pragma: no cover - repository runtime supplies flint
    arb = ctx = fmpq = None


r44 = r45.r44
SEARCH_SEED = 4603
DEFAULT_DPS = int(os.environ.get("GENERAL_D_ROUND46_DPS", "90"))
DEFAULT_ARB_BITS = int(os.environ.get("GENERAL_D_ROUND46_ARB_BITS", "768"))
EXPECTED_BASE = "3ad6a78d9cb2b81d316bcf0c171ad7cce9f4fee1"
EXPECTED_ROUND45_SUPPORT_COMMIT = "cdfa6a6770207f29b603e18b34526aec1cc8feab"
EXPECTED_OBLIGATION_HASH = "a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4"
EXPECTED_R45_ENGINE_HASH = "66e52bbb4e52aafd633f656723e896659f5b090392ca950b68f85a2d263afaf2"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


@dataclass(frozen=True)
class Screen46:
    inherited: r45.Screen
    margin: float
    action_drop: float
    action_term: float
    old_7_48: float
    omega_old_aggregate: float

    @property
    def candidate(self) -> r44.FloatCandidate:
        return self.inherited.candidate

    @property
    def key(self) -> tuple[int, int, int, int]:
        return self.candidate.key


@dataclass
class Record46:
    inherited: r45.Record
    metrics: dict[str, object]

    @property
    def hp(self) -> r44.HPRecord:
        return self.inherited.hp

    @property
    def key(self) -> tuple[int, int, int, int]:
        return self.hp.key

    @property
    def margin(self) -> mp.mpf:
        return self.metrics["R45_18_margin"]  # type: ignore[return-value]

    @property
    def S(self) -> mp.mpf:
        return self.hp.S

    @property
    def M30(self) -> mp.mpf:
        return self.inherited.M30

    @property
    def M31(self) -> mp.mpf:
        return self.inherited.M31

    @property
    def M45(self) -> mp.mpf:
        return self.metrics["Round45_support_margin"]  # type: ignore[return-value]


def screen46(candidate: r44.FloatCandidate) -> Screen46:
    """Binary64 proposal metric; no sign here is a certificate."""

    inherited = r45.screen_metrics(candidate)
    r = candidate.r2 / 2.0
    p, m, B = candidate.p, candidate.m, candidate.B
    x, q = r + p, r + p + m
    t = candidate.t
    mu = q + 1.0
    K = mu / math.cos(t)
    beta = math.acos(q / K) / math.pi
    d = 1.0 - 2.0 * t / math.pi
    zeta = math.pi / (2.0 * t) - 1.0
    shell = lambda z: r44.ball_action_f(K, z) - r44.ball_action_f(mu, z)
    action_drop = shell(x) - shell(q)
    Ur = math.sqrt(mu * mu - r * r)
    Ux = math.sqrt(mu * mu - x * x)
    Uq = math.sqrt(mu * mu - q * q)
    R1 = (Ur - Ux) / (Ux - Uq)
    B0 = B - 1
    W = r44.ball_action_f(K, mu)
    J = 2.0 * r44.ball_cap_f(mu, q)
    c0 = math.pi**2 / (K * t**3 * math.sin(t))
    old_7_48 = 7.0 * B0 * c0 / 48.0
    omega_old = B0 * c0 * (W / 2.0 - B0 / 4.0 + 1.0 / 48.0)
    top = 9.0 / (64.0 * math.pi * math.sqrt(K * K - q * q) * beta**3)
    curv = p**3 / (6.0 * math.pi) * (
        1.0 / math.sqrt(mu * mu - r * r)
        - 1.0 / math.sqrt(K * K - r * r)
    )
    lhs = (p - d * m) / 2.0
    action_term = p * R1 * action_drop
    margin = action_term + omega_old + B0 * zeta + 9.0 / (16.0 * beta) - J + top + curv - lhs
    return Screen46(inherited, margin, action_drop, action_term, old_7_48, omega_old)


def enrich46(inherited: r45.Record) -> Record46:
    """Add the literal R45.18 and its exact four-payment loss ledger."""

    hp = inherited.hp
    d = hp.data
    p = mp.mpf(hp.p)
    m = mp.mpf(hp.m)
    r, x, q = d["r"], d["x"], d["q"]
    mu, K, t = d["mu"], d["K"], d["t"]
    beta = d["beta"]
    B0 = mp.mpf(d["B0"])
    shell = lambda z: r44.ball_action(K, z) - r44.ball_action(mu, z)
    action_drop_direct = shell(x) - shell(q)
    action_drop_owner = d["j"] + d["ep"] + d["h"]
    R1 = inherited.metrics["R1"]
    action_term = p * R1 * action_drop_direct
    c0 = mp.pi**2 / (K * t**3 * mp.sin(t))
    old_7_48 = 7 * B0 * c0 / 48
    omega_primary = inherited.metrics["Omega_primary_R38_lb"]
    omega_old = B0 * c0 * (d["W"] / 2 - B0 / 4 + mp.mpf(1) / 48)
    J = inherited.metrics["J"]
    top = inherited.metrics["top_bregman_9_over_64"]
    curv = d["curvature_reserve"]
    terminal_skeleton = B0 * d["zeta"] + 9 / (16 * beta) - J
    lhs = (p - d["d"] * m) / 2
    rhs = action_term + omega_old + terminal_skeleton + top + curv
    margin = rhs - lhs

    # Exact relation between the unprojected target and the sufficient
    # R45.18 margin.  Each listed restoration is independently nonnegative
    # on the fixed owner; no reserve is reused.
    omega_slack = inherited.metrics["Omega_minus"] - omega_primary
    old_top_slack = d["R_tan_zero"] - top - old_7_48
    shelf_slack = d["C_p"] - curv
    action_slack = p * (d["E"] - R1 * action_drop_direct)
    restoration = omega_slack + old_top_slack + shelf_slack + action_slack
    M45 = inherited.M30 - old_7_48

    sx1 = shell(x + 1) + mp.mpf(1) / 4
    shelf_seam = min(
        d["e0"], d["ep"], 1 - d["e0"], 1 - d["ep"], mp.mpf(d["f"]) - sx1
    )
    inverse_adverse = min((row["eta_adverse"] for row in d["inverse_rows"]), default=mp.mpf(1))
    inverse_literal = min((1 - row["eta_adverse"] for row in d["inverse_rows"]), default=mp.mpf(1))
    wall_residual = r44.ball_action(K, q) - (mp.mpf(hp.B) - mp.mpf(1) / 4)
    metrics: dict[str, object] = {
        "R45_18_lhs": +lhs,
        "R45_18_rhs": +rhs,
        "R45_18_margin": +margin,
        "action_drop_direct": +action_drop_direct,
        "action_drop_owner_identity": +action_drop_owner,
        "action_drop_identity_residual": +(action_drop_direct - action_drop_owner),
        "p_R1_action_drop": +action_term,
        "c0": +c0,
        "old_7_over_48_aggregate": +old_7_48,
        "Omega_primary_plus_old_aggregate": +omega_old,
        "aggregate_identity_residual": +(omega_old - omega_primary - old_7_48),
        "terminal_skeleton": +terminal_skeleton,
        "top_bregman_9_over_64": +top,
        "shelf_curvature_reserve": +curv,
        "D_A_direct": +d["D_A"],
        "C_p_exact": +d["C_p"],
        "S_exact": +hp.S,
        "M30": +inherited.M30,
        "M31": +inherited.M31,
        "Round45_support_margin": +M45,
        "restoration_Omega": +omega_slack,
        "restoration_old_top_Bregman": +old_top_slack,
        "restoration_shelf_curvature": +shelf_slack,
        "restoration_adjacent_action": +action_slack,
        "restoration_total": +restoration,
        "S_minus_margin_ledger_residual": +(hp.S - margin - restoration),
        "threshold_excess": +(d["p_minus_dm"] - mp.mpf(11) / 5),
        "hard_margin": +d["hard_margin"],
        "ep_distance": +abs(d["ep"]),
        "shelf_seam_distance": +shelf_seam,
        "activity_margin": +d["activity"],
        "inverse_adverse_distance": +inverse_adverse,
        "inverse_literal_distance": +inverse_literal,
        "outer_wall_residual": +wall_residual,
        "first_drop_value": +sx1,
    }
    return Record46(inherited, metrics)


def proposal_stream(random_count: int, quick: bool) -> Iterable[tuple[str, int, int, int, int]]:
    """Mandatory Round-45 box, then independent edge/asymptotic stresses."""

    if quick:
        r2_values = list(range(2, 17, 2)) + list(range(3, 18, 2))
        p_stop, m_stop, B_stop = 13, 8, 8
    else:
        # Exactly 31*38*20*19 = 447,640 proposals on both parity grids.
        r2_values = list(range(2, 33, 2)) + list(range(3, 32, 2))
        p_stop, m_stop, B_stop = 41, 21, 21
    for r2 in r2_values:
        for p in range(3, p_stop):
            for m in range(1, m_stop):
                for B in range(2, B_stop):
                    yield ("mandatory_baseline", r2, p, m, B)

    if quick:
        edge_r2 = [2, 3, 10, 11, 200, 201, 2000, 2001, 20000, 20001]
        edge_p = [3, 4, 6, 10, 20, 40, 80]
        edge_m = [1, 2, 4, 8, 16, 32]
        edge_B = [2, 3, 4, 8, 16, 32, 64, 96]
        for r2 in edge_r2:
            for p in edge_p:
                for m in edge_m:
                    for B in edge_B:
                        yield ("quick_stress", r2, p, m, B)
    else:
        # The audited Round-44 independent stream supplies a wider compact
        # block, deterministic large-radius/large-p/large-B edges, and a
        # logarithmic asymptotic sample.  It is a proposal source only.
        for source, r2, p, m, B in r44.proposal_stream(random_count):
            yield (f"stress_{source}", r2, p, m, B)

        # Explicit outer-level and t-end stresses, including values beyond
        # those in the mandatory box.  Failed owner proposals remain useful
        # evidence that the exact inequalities, rather than loose ranges,
        # perform the filtering.
        edge_r2 = [2, 3, 4, 5, 20, 21, 200, 201, 2000, 2001, 20000, 20001, 200000, 200001, 2000000, 2000001]
        edge_p = [3, 4, 6, 10, 20, 40, 80, 160]
        edge_m = [1, 2, 4, 8, 16, 32, 64]
        edge_B = [2, 3, 4, 8, 16, 32, 64, 96, 128, 256, 512]
        for r2 in edge_r2:
            for p in edge_p:
                for m in edge_m:
                    for B in edge_B:
                        yield ("explicit_asymptotic", r2, p, m, B)

        # A second deterministic random stream is intentionally independent
        # of the Round-44 seed and biases toward B0=1, high levels, m=1,
        # large p, and large radius.
        rng = random.Random(SEARCH_SEED)
        B_pool = [2, 3, 4, 8, 16, 32, 64, 96, 128, 256, 512]
        for _ in range(max(2000, random_count // 2)):
            r = max(1, round(math.exp(rng.uniform(0, math.log(2_000_000)))))
            r2 = 2 * r + rng.randrange(2)
            p = max(3, round(math.exp(rng.uniform(math.log(3), math.log(3000)))))
            m = max(1, round(math.exp(rng.uniform(0, math.log(1000)))))
            for B in sorted({2, rng.choice(B_pool), rng.randint(2, 32)}):
                yield ("independent_random", r2, p, m, B)

    # Named regressions are forced into every run.
    yield ("regression_round44_min", 2, 3, 1, 2)
    yield ("regression_r45_cf_lead", 2, 6, 11, 19)
    yield ("regression_r45_cf_clean", 3, 6, 7, 5)
    yield ("regression_r45_cf_extended", 33128, 19, 1, 2)


def mp_text(value: object, digits: int = 36) -> object:
    return r45.mp_text(value, digits)


def full_ledger(record: Record46) -> dict[str, object]:
    ledger = r45.full_ledger(record.inherited)
    ledger["Round46"] = record.metrics
    return ledger


def print_ledger(label: str, record: Record46, digits: int = 40) -> None:
    print(f"FULL_LEDGER {label}=" + json.dumps(mp_text(full_ledger(record), digits), sort_keys=True))


def decimal_hull(value: mp.mpf, digits: int) -> tuple[fmpq, fmpq]:
    return r45.decimal_hull(value, digits)


def arb_hull(lo: fmpq, hi: fmpq) -> arb:
    return r45.arb_hull(lo, hi)


def directed_certificate(record: Record46, digits: int = 60) -> dict[str, object]:
    """Directed exact-owner enclosure of R45.18, D_A, C_p, S, and support.

    The outer wall has a unique root because

        d/dt G_{mu sec t}(q) = sqrt(K^2-q^2) tan(t)/pi > 0.

    Every inverse root is unique because z -> G_K(z) has derivative
    -acos(z/K)/pi < 0.  Rational endpoint signs and strict integer-cell
    containment therefore certify the direct strict count.
    """

    require(arb is not None and ctx is not None and fmpq is not None, "python-flint unavailable")
    ctx.prec = DEFAULT_ARB_BITS
    hp, d = record.hp, record.hp.data
    tlo, thi = decimal_hull(d["t"], digits + 8)
    if tlo == thi:
        thi += fmpq(1, 10 ** (digits + 8))
    r_q = fmpq(hp.r2, 2)
    p_q, m_q = fmpq(hp.p), fmpq(hp.m)
    x_q, q_q = r_q + p_q, r_q + p_q + m_q
    mu_q = q_q + 1
    mu = arb(mu_q)
    pi = arb.pi()
    target = fmpq(hp.B) - fmpq(1, 4)

    def action_at_t(tq: fmpq, zq: fmpq) -> arb:
        tt = arb(tq)
        radius = mu / tt.cos()
        return r44.arb_ball_action(radius, zq)

    wall_flo = action_at_t(tlo, q_q) - target
    wall_fhi = action_at_t(thi, q_q) - target
    require(wall_flo < 0 and wall_fhi > 0, "directed wall bracket signs")
    t = arb_hull(tlo, thi)
    require(t > 0 and t < pi / 2, "directed t domain")
    K = mu / t.cos()
    wall_derivative = (K * K - q_q * q_q).sqrt() * t.tan() / pi
    require(wall_derivative > 0, "directed wall-root uniqueness")

    def action(radius: arb, zq: fmpq) -> arb:
        return r44.arb_ball_action(radius, zq)

    def cap(radius: arb, zq: fmpq) -> arb:
        return r44.arb_ball_cap(radius, zq)

    def shell(zq: fmpq) -> arb:
        return action(K, zq) - action(mu, zq)

    f = int(d["f"])
    sr = shell(r_q) + fmpq(1, 4)
    sx = shell(x_q) + fmpq(1, 4)
    sx1 = shell(x_q + 1) + fmpq(1, 4)
    require(f < sr < f + 1, "directed first-shelf left floor")
    require(f < sx < f + 1, "directed first-shelf right floor")
    require(sx1 < f, "directed literal first drop")
    e0, ep = sr - f, sx - f
    E, Delta = e0 + ep, e0 - ep
    d_rho = 1 - 2 * t / pi
    Estar = (p_q - d_rho * m_q) / (2 * p_q)
    require(E >= 0 and E < Estar and Estar < fmpq(1, 2), "directed hard E owner")
    require(p_q >= 3 and m_q >= 1 and q_q >= 5, "directed discrete owner")
    require(p_q - d_rho * m_q > fmpq(11, 5), "directed p-dm threshold")
    gamma = fmpq(3, 4) if hp.r2 % 2 == 0 else fmpq(2)
    activity = K * K - pi * pi / (1 - t.cos()) ** 2 - gamma
    require(activity > 0, "directed strict dimension activity")

    beta = (arb(q_q) / K).acos() / pi
    h = action(mu, q_q)
    W = action(K, mu_q)
    B0_i = hp.B - 1
    B0 = fmpq(B0_i)
    v_q = fmpq(hp.B) - fmpq(1, 4)
    u = v_q - W
    require(h > 0 and u > h and beta > u and beta < fmpq(1, 2), "directed endpoint correlation")
    require(u < fmpq(1, 2), "directed upper-alpha owner")
    aq_cell = shell(q_q) + fmpq(1, 4)
    require(B0 < aq_cell and aq_cell < hp.B, "directed endpoint strict count")
    require(f - hp.B >= 0, "directed synchronized count j>=0")

    omega = arb(0)
    spatial_sum = 0
    inverse_brackets: list[dict[str, object]] = []
    for row in d["inverse_rows"]:
        k = int(row["k"])
        ylo, yhi = decimal_hull(row["y"], digits)
        ulp = fmpq(1, 10**digits)
        ylo, yhi = ylo - ulp, yhi + ulp
        level = fmpq(4 * k - 1, 4)
        Flo = action(K, q_q + ylo) - level
        Fhi = action(K, q_q + yhi) - level
        require(Flo > 0 and Fhi < 0, f"directed inverse bracket k={k}")
        inverse_derivative = -((arb(q_q + ylo) / K).acos()) / pi
        require(inverse_derivative < 0, f"directed inverse uniqueness k={k}")
        count = int(row["count_adverse"])
        require(count < ylo and yhi < count + 1, f"directed inverse cell k={k}")
        y = arb_hull(ylo, yhi)
        theta = ((arb(q_q) + y) / K).acos()
        eta = y - count
        omega += pi / (2 * theta) - pi / (2 * t) + 2 * eta
        spatial_sum += count
        inverse_brackets.append(
            {
                "k": k,
                "lo": str(ylo),
                "hi": str(yhi),
                "F_lo": str(Flo),
                "F_hi": str(Fhi),
                "cell": [count, count + 1],
                "unique": True,
            }
        )

    terminal_count = B0_i + 2 * spatial_sum
    DA = 2 * (cap(K, q_q) - cap(mu, q_q)) - terminal_count
    Cp = 2 * (cap(K, r_q) - cap(K, x_q) - cap(mu, r_q) + cap(mu, x_q)) - p_q * (shell(r_q) + shell(x_q))
    loss = p_q * (Estar - E)
    S = DA + Cp - loss
    J = 2 * cap(mu, q_q)
    zeta = pi / (2 * t) - 1
    top = fmpq(9, 64) / (pi * (K * K - q_q * q_q).sqrt() * beta**3)
    curv = p_q**3 / (6 * pi) * (
        1 / (mu * mu - r_q * r_q).sqrt() - 1 / (K * K - r_q * r_q).sqrt()
    )
    Lzero = omega + B0 * zeta + fmpq(9, 16) / beta - J
    Lplus = omega + B0 * zeta + fmpq(1, 2) / beta - J
    Rzero, Rplus = DA - Lzero, DA - Lplus
    M30 = loss - (Lzero + top + curv)
    M31 = loss - (fmpq(49, 40) + top + curv)

    Ur = (mu * mu - r_q * r_q).sqrt()
    Ux = (mu * mu - x_q * x_q).sqrt()
    Uq = (mu * mu - q_q * q_q).sqrt()
    R1 = (Ur - Ux) / (Ux - Uq)
    action_drop = shell(x_q) - shell(q_q)
    action_identity = (f - hp.B) + ep + h
    action_identity_residual = action_drop - action_identity
    require(action_identity_residual.contains(0), "directed action-drop identity")
    action_adjacent = Delta - R1 * action_drop
    require(action_adjacent > 0, "directed Round42 adjacent action")

    c0 = pi**2 / (K * t**3 * t.sin())
    old_7_48 = fmpq(7, 48) * B0 * c0
    omega_primary = c0 / 2 * (B0 * (B0 + 1) / 2 - B0 * u)
    omega_old = B0 * c0 * (W / 2 - B0 / 4 + fmpq(1, 48))
    aggregate_identity = omega_old - omega_primary - old_7_48
    require(aggregate_identity.contains(0), "directed aggregate identity")
    lhs = (p_q - d_rho * m_q) / 2
    rhs = p_q * R1 * action_drop + omega_old + B0 * zeta + fmpq(9, 16) / beta - J + top + curv
    margin = rhs - lhs
    CF = p_q * R1 * h + fmpq(49, 40) + top + curv - lhs
    M45 = M30 - old_7_48

    omega_slack = omega - omega_primary
    old_top_slack = Rzero - top - old_7_48
    shelf_slack = Cp - curv
    action_slack = p_q * (E - R1 * action_drop)
    require(omega_slack > 0, "directed primary Omega lower bound")
    require(old_top_slack > 0, "directed 7/48 old plus 9/64 top reserve")
    require(shelf_slack > 0, "directed shelf curvature reserve")
    require(action_slack > 0, "directed adjacent-action payment")
    loss_residual = S - margin - omega_slack - old_top_slack - shelf_slack - action_slack
    require(loss_residual.contains(0), "directed R45.18 loss ledger")
    reconciliation = Rplus - Rzero - 1 / (16 * beta)
    require(reconciliation.contains(0), "directed 1/(16 beta) reconciliation")

    signs = {
        "R45_18_positive": bool(margin > 0),
        "R45_18_negative": bool(margin < 0),
        "S_positive": bool(S > 0),
        "S_negative": bool(S < 0),
        "M30_positive": bool(M30 > 0),
        "M31_positive": bool(M31 > 0),
        "Round45_support_margin_positive": bool(M45 > 0),
        "Round45_CF_negative": bool(CF < 0),
        "r45_18_route_counterexample": bool(margin < 0 and S > 0),
        "support_entry_witness": bool(M30 > 0),
        "gate_trigger_certificate": bool(S < 0),
    }
    return {
        "bits": ctx.prec,
        "wall": {
            "lo": str(tlo),
            "hi": str(thi),
            "F_lo": str(wall_flo),
            "F_hi": str(wall_fhi),
            "derivative": str(wall_derivative),
            "unique": True,
        },
        "owner_all_strict": True,
        "side_vector": "all old inverse roots certified in generic cells; literal=adverse",
        "inverse_brackets": inverse_brackets,
        "R45_18_margin": str(margin),
        "Round45_CF_margin": str(CF),
        "D_A": str(DA),
        "C_p": str(Cp),
        "S": str(S),
        "M30": str(M30),
        "M31": str(M31),
        "Round45_support_margin": str(M45),
        "action_drop_identity_residual": str(action_identity_residual),
        "aggregate_identity_residual": str(aggregate_identity),
        "loss_ledger_residual": str(loss_residual),
        "reconciliation_residual": str(reconciliation),
        "restorations": {
            "Omega": str(omega_slack),
            "old_top_Bregman": str(old_top_slack),
            "shelf_curvature": str(shelf_slack),
            "adjacent_action": str(action_slack),
        },
        "signs": signs,
        "directed": True,
    }


def fixed_record(source: str, r2: int, p: int, m: int, B: int, dps: int) -> Record46:
    candidate = r45.fixed_candidate(source, r2, p, m, B)
    hp = r44.evaluate_hp(candidate, dps)
    return enrich46(r45.enrich(hp))


def candidate_from_record(record: Record46) -> r44.FloatCandidate:
    return r45.candidate_from_record(record.inherited, source="round46-one-sided")


def one_sided_rows(record: Record46, dps: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    candidate = candidate_from_record(record)
    for exponent in (3, 6, 9, 12, 18):
        alpha = mp.mpf(1) - mp.power(10, -exponent)
        hp = r44.evaluate_hp(candidate, dps, alpha=alpha)
        enriched = enrich46(r45.enrich(hp))
        rows.append(
            {
                "s": exponent,
                "alpha": alpha,
                "t_resolved": hp.data["t"],
                "K": hp.data["K"],
                "owner": hp.owner,
                "reasons": hp.reasons,
                "R45_18_margin": enriched.margin,
                "D_A": hp.data["D_A"],
                "C_p": hp.data["C_p"],
                "S": hp.S,
                "M30": enriched.M30,
                "M31": enriched.M31,
            }
        )
    return rows


def regression_bundle(records: list[Record46], dps: int) -> tuple[dict[str, object], dict[str, Record46]]:
    round44_min = fixed_record("round44-min", 2, 3, 1, 2, dps)
    expected = mp.mpf("2.694565278900355025629332914750280")
    require(round44_min.hp.owner, "Round44 minimum owner")
    require(abs(round44_min.S - expected) < mp.power(10, -32), "Round44 minimum value")

    cf_lead = fixed_record("r45-cf-lead", 2, 6, 11, 19, dps)
    cf_clean = fixed_record("r45-cf-clean", 3, 6, 7, 5, dps)
    cf_extended = fixed_record("r45-cf-extended", 33128, 19, 1, 2, dps)
    for label, row in (("lead", cf_lead), ("clean", cf_clean), ("extended", cf_extended)):
        require(row.hp.owner, f"Round45 CF {label} exact owner")
        require(row.inherited.CF < 0 and row.S > 0, f"Round45 CF {label} classification")

    r43 = r44.evaluate_hp(r44.round43_candidate(dps), dps)
    require(r43.data["E"] > r43.data["Estar"], "Round43 hard-owner rejection")
    require([reason for reason in r43.reasons if reason != "hard E owner fails"] == [], "Round43 sole rejection")
    r27 = r44.round27_regression(dps)
    r27_directed = r44.round27_arb_check()
    require(r27["automatic_rejection"] and r27["large_positive_S"], "Round27 regression")

    moment = (Fraction(1, 4) ** 3 - Fraction(-3, 4) ** 3) / 3
    require(moment == Fraction(7, 48), "7/48 old-level coefficient")
    max_reconciliation = max(abs(row.inherited.metrics["reconciliation_residual"]) for row in records)
    top_coeff_error = max(abs(row.inherited.metrics["top_coefficient_replay"] - mp.mpf(9) / 64) for row in records)
    min_top_slack = min(row.hp.data["R_tan_zero"] - row.inherited.metrics["top_bregman_9_over_64"] for row in records)
    min_omega_slack = min(row.inherited.metrics["Omega_primary_R38_slack"] for row in records)
    min_adjacent = min(row.inherited.metrics["adjacent_action_margin"] for row in records)
    max_action_identity = max(abs(row.metrics["action_drop_identity_residual"]) for row in records)
    max_aggregate_identity = max(abs(row.metrics["aggregate_identity_residual"]) for row in records)
    max_loss_ledger = max(abs(row.metrics["S_minus_margin_ledger_residual"]) for row in records)
    require(max_reconciliation < mp.power(10, -(dps - 12)), "1/(16 beta) reconciliation")
    require(top_coeff_error < mp.power(10, -(dps - 12)), "9/64 top coefficient")
    require(min_top_slack > 0, "9/64 top reserve")
    require(min_omega_slack > 0, "primary Omega lower bound")
    require(min_adjacent > 0, "Round42 adjacent action")
    require(max_action_identity < mp.power(10, -(dps - 12)), "action-drop identity")
    require(max_aggregate_identity < mp.power(10, -(dps - 12)), "Omega plus 7/48 identity")
    require(max_loss_ledger < mp.power(10, -(dps - 12)), "R45.18 loss ledger")

    data: dict[str, object] = {
        "round44_minimum": {
            "tuple": "(r,p,m,f,B,j)=(1,3,1,2,2,0)",
            "S": round44_min.S,
            "R45_18_margin": round44_min.margin,
            "difference_from_audited": round44_min.S - expected,
        },
        "round45_cf_lead": {
            "tuple": "(1,6,11,21,19,2)",
            "CF_margin": cf_lead.inherited.CF,
            "R45_18_margin": cf_lead.margin,
            "S": cf_lead.S,
        },
        "round45_cf_clean": {
            "tuple": "(3/2,6,7,6,5,1)",
            "CF_margin": cf_clean.inherited.CF,
            "R45_18_margin": cf_clean.margin,
            "S": cf_clean.S,
        },
        "round45_cf_extended": {
            "tuple": "(16564,19,1,2,2,0)",
            "CF_margin": cf_extended.inherited.CF,
            "R45_18_margin": cf_extended.margin,
            "S": cf_extended.S,
        },
        "round43_rejected": {
            "tuple": "(1,9,9,4,3,1)",
            "E_minus_Estar": r43.data["E"] - r43.data["Estar"],
            "sole_rejection": True,
        },
        "round27_automatic": r27,
        "round27_directed": r27_directed,
        "old_level_moment_exact": str(moment),
        "max_reconciliation_residual": max_reconciliation,
        "top_coefficient_max_error": top_coeff_error,
        "min_Rtan0_minus_top": min_top_slack,
        "min_Omega_primary_slack": min_omega_slack,
        "min_adjacent_action_margin": min_adjacent,
        "max_action_drop_identity_residual": max_action_identity,
        "max_aggregate_identity_residual": max_aggregate_identity,
        "max_R45_18_loss_ledger_residual": max_loss_ledger,
    }
    fixed = {
        "round44_minimum": round44_min,
        "round45_cf_lead": cf_lead,
        "round45_cf_clean": cf_clean,
        "round45_cf_extended": cf_extended,
    }
    return data, fixed


def owner_summary(record: Record46) -> str:
    h, d = record.hp, record.hp.data
    return (
        f"r={mp.nstr(d['r'], 14)} p={h.p} m={h.m} f={d['f']} B={h.B} j={d['j']} "
        f"grid={h.grid} t={mp.nstr(d['t'], 14)} R45.18={mp.nstr(record.margin, 26)} "
        f"D_A={mp.nstr(d['D_A'], 20)} C_p={mp.nstr(d['C_p'], 20)} "
        f"S={mp.nstr(record.S, 24)} M30={mp.nstr(record.M30, 20)} M45={mp.nstr(record.M45, 20)}"
    )


def min_by(records: list[Record46], key: str) -> Record46:
    return min(records, key=lambda row: row.metrics[key])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--random", type=int, default=15000)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--skip-directed", action="store_true")
    args = parser.parse_args()
    dps = max(80, args.dps)
    mp.mp.dps = dps

    print("ROUND46C INDEPENDENT EXACT-OWNER R45.18 SEARCH")
    print("round46_lead_evaluator_imported=False")
    print("audited_round45_independent_definition_engine_reused=True")
    print("literal_R45_18_margin=True; projected_repair_scalar=False")
    print("classification=diagnostic sweep; directed named classifications only")
    print(f"dps={dps}; arb_bits={DEFAULT_ARB_BITS}; seed={SEARCH_SEED}; quick={args.quick}")
    print(
        f"pinned_base={EXPECTED_BASE}; round45_support_commit={EXPECTED_ROUND45_SUPPORT_COMMIT}; "
        f"obligation_hash={EXPECTED_OBLIGATION_HASH}; r45_engine_hash={EXPECTED_R45_ENGINE_HASH}"
    )

    seen: set[tuple[int, int, int, int]] = set()
    screens: list[Screen46] = []
    source_proposals: collections.Counter[str] = collections.Counter()
    for source, r2, p, m, B in proposal_stream(args.random, args.quick):
        key = (r2, p, m, B)
        if key in seen:
            continue
        seen.add(key)
        source_proposals[source] += 1
        candidate = r44.float_candidate(source, r2, p, m, B)
        if candidate is not None:
            screens.append(screen46(candidate))
    print(f"binary64_distinct_proposals={len(seen)}")
    print(f"proposal_sources={json.dumps(dict(sorted(source_proposals.items())), sort_keys=True)}")
    if not args.quick:
        print("mandatory_baseline_proposals=447640")
    print(f"binary64_owner_candidates={len(screens)}")
    print(f"binary64_R45_18_negative={sum(row.margin < 0 for row in screens)}")
    print(f"binary64_S_negative={sum(row.candidate.S < 0 for row in screens)}")
    print(f"binary64_M30_positive={sum(row.inherited.M30 > 0 for row in screens)}")

    records: list[Record46] = []
    rejected: list[r44.HPRecord] = []
    for screen in screens:
        hp = r44.evaluate_hp(screen.candidate, dps)
        if hp.owner:
            records.append(enrich46(r45.enrich(hp)))
        else:
            rejected.append(hp)
    require(records, "no high-precision exact owner")
    print(f"high_precision_exact_owners={len(records)}")
    print(f"high_precision_rejected={len(rejected)}")
    print(f"high_precision_R45_18_negative={sum(row.margin < 0 for row in records)}")
    print(f"high_precision_S_negative={sum(row.S < 0 for row in records)}")
    print(f"high_precision_M30_positive={sum(row.M30 > 0 for row in records)}")
    print(f"high_precision_M31_positive={sum(row.M31 > 0 for row in records)}")
    print(f"high_precision_Round45_support_margin_positive={sum(row.M45 > 0 for row in records)}")
    owner_ranges = {
        "r": [min(row.hp.data["r"] for row in records), max(row.hp.data["r"] for row in records)],
        "p": [min(row.hp.p for row in records), max(row.hp.p for row in records)],
        "m": [min(row.hp.m for row in records), max(row.hp.m for row in records)],
        "B": [min(row.hp.B for row in records), max(row.hp.B for row in records)],
        "t": [min(row.hp.data["t"] for row in records), max(row.hp.data["t"] for row in records)],
    }
    print("OWNER_RANGES=" + json.dumps(mp_text(owner_ranges, 32), sort_keys=True))

    integer = [row for row in records if row.hp.grid == "integer"]
    half = [row for row in records if row.hp.grid == "half-integer"]
    baseline = [row for row in records if row.hp.source == "mandatory_baseline"]
    stress_counts = {
        "integer": len(integer),
        "half_integer": len(half),
        "mandatory_baseline": len(baseline),
        "B0_equals_1": sum(row.hp.B == 2 for row in records),
        "large_B0_B_ge_32": sum(row.hp.B >= 32 for row in records),
        "m_equals_1": sum(row.hp.m == 1 for row in records),
        "large_p_p_ge_20": sum(row.hp.p >= 20 for row in records),
        "large_radius_r_ge_10000": sum(row.hp.data["r"] >= 10000 for row in records),
        "small_t_t_lt_0_1": sum(row.hp.data["t"] < mp.mpf("0.1") for row in records),
        "large_t_t_gt_1_4": sum(row.hp.data["t"] > mp.mpf("1.4") for row in records),
        "near_threshold_excess_lt_0_1": sum(row.metrics["threshold_excess"] < mp.mpf("0.1") for row in records),
        "near_Estar_lt_0_01": sum(row.metrics["hard_margin"] < mp.mpf("0.01") for row in records),
        "near_ep_zero_lt_0_01": sum(row.metrics["ep_distance"] < mp.mpf("0.01") for row in records),
        "near_shelf_seam_lt_0_01": sum(row.metrics["shelf_seam_distance"] < mp.mpf("0.01") for row in records),
        "near_activity_lt_1": sum(row.metrics["activity_margin"] < 1 for row in records),
        "near_inverse_adverse_lt_0_01": sum(row.metrics["inverse_adverse_distance"] < mp.mpf("0.01") for row in records),
        "near_inverse_literal_lt_0_01": sum(row.metrics["inverse_literal_distance"] < mp.mpf("0.01") for row in records),
        "outer_wall_exact_by_construction": len(records),
    }
    print("STRESS_COUNTS=" + json.dumps(stress_counts, sort_keys=True))

    extrema: dict[str, Record46] = {
        "minimum_R45_18": min(records, key=lambda row: row.margin),
        "minimum_S": min(records, key=lambda row: row.S),
        "maximum_M30": max(records, key=lambda row: row.M30),
        "maximum_M31": max(records, key=lambda row: row.M31),
        "maximum_Round45_support_margin": max(records, key=lambda row: row.M45),
        "near_Estar": min_by(records, "hard_margin"),
        "near_ep_zero": min_by(records, "ep_distance"),
        "near_shelf_seam": min_by(records, "shelf_seam_distance"),
        "near_activity": min_by(records, "activity_margin"),
        "near_inverse_adverse": min_by(records, "inverse_adverse_distance"),
        "near_inverse_literal": min_by(records, "inverse_literal_distance"),
        "near_p_minus_dm_threshold": min_by(records, "threshold_excess"),
        "small_t": min(records, key=lambda row: row.hp.data["t"]),
        "large_t": max(records, key=lambda row: row.hp.data["t"]),
        "large_B0": max(records, key=lambda row: (row.hp.B, -float(row.margin))),
        "large_p": max(records, key=lambda row: (row.hp.p, -float(row.margin))),
        "large_radius": max(records, key=lambda row: (row.hp.data["r"], -row.margin)),
    }
    if integer:
        extrema["minimum_R45_18_integer"] = min(integer, key=lambda row: row.margin)
    if half:
        extrema["minimum_R45_18_half_integer"] = min(half, key=lambda row: row.margin)
    if baseline:
        extrema["minimum_R45_18_mandatory_baseline"] = min(baseline, key=lambda row: row.margin)
    B1 = [row for row in records if row.hp.B == 2]
    if B1:
        extrema["minimum_R45_18_B0_equals_1"] = min(B1, key=lambda row: row.margin)
    large_B = [row for row in records if row.hp.B >= 32]
    if large_B:
        extrema["minimum_R45_18_large_B0"] = min(large_B, key=lambda row: row.margin)
    m1 = [row for row in records if row.hp.m == 1]
    if m1:
        extrema["minimum_R45_18_m_equals_1"] = min(m1, key=lambda row: row.margin)
    for label, row in extrema.items():
        print(f"diagnostic_extremum {label} " + owner_summary(row))

    regressions, fixed = regression_bundle(records, dps)
    print("MANDATORY_REGRESSIONS=" + json.dumps(mp_text(regressions, 44), sort_keys=True))

    # New Round-46 classifications are created only after a directed replay.
    named: list[tuple[str, Record46]] = []
    route_rows = [row for row in records if row.margin < 0 and row.S >= 0]
    gate_rows = [row for row in records if row.S < 0]
    support_rows = [row for row in records if row.M30 > 0]
    if route_rows:
        named.append(("r45_18_route_counterexample", min(route_rows, key=lambda row: row.margin)))
    if gate_rows:
        named.append(("gate_trigger_certificate", min(gate_rows, key=lambda row: row.S)))
    if support_rows:
        named.append(("support_entry_witness", max(support_rows, key=lambda row: row.M30)))

    # Positive extrema are explicitly diagnostics, while the prior Round-45
    # CF failures are mandatory directed regressions, not new classifications.
    named.extend(
        [
            ("minimum_R45_18_diagnostic", extrema["minimum_R45_18"]),
            ("round45_cf_regression_lead", fixed["round45_cf_lead"]),
            ("round45_cf_regression_clean", fixed["round45_cf_clean"]),
            ("round45_cf_regression_extended", fixed["round45_cf_extended"]),
        ]
    )
    emitted: set[tuple[str, tuple[int, int, int, int]]] = set()
    for label, row in named:
        marker = (label, row.key)
        if marker in emitted:
            continue
        print_ledger(label, row)
        if not args.skip_directed:
            certificate = directed_certificate(row)
            print(f"DIRECTED_CERTIFICATE {label}=" + json.dumps(certificate, sort_keys=True))
            print(
                f"DIRECTED_SUMMARY {label} R45_18={certificate['R45_18_margin']} "
                f"S={certificate['S']} M30={certificate['M30']} M45={certificate['Round45_support_margin']}"
            )
            signs = certificate["signs"]
            if label == "r45_18_route_counterexample":
                require(signs["r45_18_route_counterexample"], "directed R45.18 route classification")
            elif label == "gate_trigger_certificate":
                require(signs["gate_trigger_certificate"], "directed Gate trigger classification")
            elif label == "support_entry_witness":
                require(signs["support_entry_witness"], "directed support classification")
            elif label.startswith("round45_cf_regression"):
                require(signs["Round45_CF_negative"] and signs["S_positive"], "directed Round45 CF regression signs")
            elif label == "minimum_R45_18_diagnostic":
                require(signs["R45_18_positive"] and signs["S_positive"], "directed positive diagnostic")
        emitted.add(marker)

    one_sided_targets: dict[tuple[int, int, int, int], tuple[str, Record46]] = {}
    for label, row in (
        ("minimum_R45_18", extrema["minimum_R45_18"]),
        ("round45_cf_lead", fixed["round45_cf_lead"]),
        ("round45_cf_clean", fixed["round45_cf_clean"]),
        ("near_inverse_adverse", extrema["near_inverse_adverse"]),
        ("near_inverse_literal", extrema["near_inverse_literal"]),
    ):
        one_sided_targets[row.key] = (label, row)
    for label, row in one_sided_targets.values():
        print(f"ONE_SIDED {label}=" + json.dumps(mp_text(one_sided_rows(row, dps), 42), sort_keys=True))

    print(f"r45_18_route_counterexample_found={bool(route_rows and not args.skip_directed)}")
    print(f"support_entry_witness_found={bool(support_rows and not args.skip_directed)}")
    print(f"gate_trigger_certificate_found={bool(gate_rows and not args.skip_directed)}")
    print("positive_coverage_certificate=False")
    if gate_rows:
        print("conclusion=directed exact-target candidate processed; Gate classification requires final audit")
    elif route_rows:
        print("conclusion=directed R45.18 sufficient-route candidate processed; full S classification printed; no repair surrogate")
    else:
        print("conclusion=no R45.18 reverse or negative exact S found in finite diagnostics; no coverage claim")


if __name__ == "__main__":
    main()
