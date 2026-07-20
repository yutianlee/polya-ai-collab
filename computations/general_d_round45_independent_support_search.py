#!/usr/bin/env python3
"""Round 45C independent exact-owner support and route search.

This evaluator imports only the audited *independent* Round 44 definition
engine, never a Round 45 lead evaluator.  It retains the direct strict
terminal count and augments that engine with the exact Round 45 quantities

    S     = D_A(q) + C_p + p(E-E_*),
    M30   = p(E_*-E) - RHS(R45-S30),
    M31   = p(E_*-E) - RHS(R45-S31),
    CF    = RHS(R45-CF) - (p-dm)/2.

Thus CF < 0 falsifies only the count-free sufficient route, M30 > 0 is only
a support-entry witness, and only a directed exact-owner enclosure S < 0 can
be a Gate-B trigger.  Binary64 and mpmath searches are diagnostic.  Every
reported classification witness is rebuilt with directed Arb arithmetic.
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

import general_d_round44_independent_gate_b_search as r44

try:
    from flint import arb, ctx, fmpq
except ImportError:  # pragma: no cover
    arb = ctx = fmpq = None


SEARCH_SEED = 4503
DEFAULT_DPS = int(os.environ.get("GENERAL_D_ROUND45_DPS", "90"))
DEFAULT_ARB_BITS = int(os.environ.get("GENERAL_D_ROUND45_ARB_BITS", "640"))
EXPECTED_BASE = "52738525ab0ee360c54f237a5a4fe314caa51e79"
EXPECTED_R44_ARTIFACT = "2a0e51ecbb1534eeea94615ab94717fa126c0c5d"
EXPECTED_OBLIGATION_HASH = "a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


@dataclass(frozen=True)
class Screen:
    candidate: r44.FloatCandidate
    M30: float
    M31: float
    CF: float
    omega: float
    adjacent_margin: float

    @property
    def key(self) -> tuple[int, int, int, int]:
        return self.candidate.key


@dataclass
class Record:
    hp: r44.HPRecord
    metrics: dict[str, object]

    @property
    def key(self) -> tuple[int, int, int, int]:
        return self.hp.key

    @property
    def S(self) -> mp.mpf:
        return self.hp.S

    @property
    def M30(self) -> mp.mpf:
        return self.metrics["M30"]  # type: ignore[return-value]

    @property
    def M31(self) -> mp.mpf:
        return self.metrics["M31"]  # type: ignore[return-value]

    @property
    def CF(self) -> mp.mpf:
        return self.metrics["CF_margin"]  # type: ignore[return-value]


def screen_metrics(candidate: r44.FloatCandidate) -> Screen:
    """Binary64 proposal values; no sign here receives a classification."""

    r = candidate.r2 / 2.0
    p, m, B = candidate.p, candidate.m, candidate.B
    x, q = r + p, r + p + m
    t = candidate.t
    mu = q + 1.0
    K = mu / math.cos(t)
    beta = math.acos(q / K) / math.pi
    d = 1.0 - 2.0 * t / math.pi
    zeta = math.pi / (2.0 * t) - 1.0
    h = r44.ball_action_f(mu, q)
    W = r44.ball_action_f(K, mu)
    u = B - 0.25 - W
    omega = 0.0
    for k in range(1, B):
        theta = r44.inverse_angle_f(K, q, beta, k - 0.25)
        y = K * math.cos(theta) - q
        eta = y - math.floor(y)
        omega += math.pi / (2.0 * theta) - math.pi / (2.0 * t) + 2.0 * eta
    J = 2.0 * r44.ball_cap_f(mu, q)
    top = 9.0 / (64.0 * math.pi * math.sqrt(K * K - q * q) * beta**3)
    curv = p**3 / (6.0 * math.pi) * (
        1.0 / math.sqrt(mu * mu - r * r) - 1.0 / math.sqrt(K * K - r * r)
    )
    loss = p * (candidate.Estar - candidate.E)
    rhs30 = omega + (B - 1) * zeta + 9.0 / (16.0 * beta) - J + top + curv
    M30 = loss - rhs30
    M31 = loss - 49.0 / 40.0 - top - curv
    Ur = math.sqrt(mu * mu - r * r)
    Ux = math.sqrt(mu * mu - x * x)
    Uq = math.sqrt(mu * mu - q * q)
    R1 = (Ur - Ux) / (Ux - Uq)
    cf = p * R1 * h + 49.0 / 40.0 + top + curv - (p - d * m) / 2.0
    A = lambda z: r44.ball_action_f(K, z) - r44.ball_action_f(mu, z)
    f = candidate.f
    Delta = (A(r) + 0.25 - f) - (A(x) + 0.25 - f)
    ep = A(x) + 0.25 - f
    adjacent = Delta - R1 * (f - B + ep + h)
    require(u > h, "screen endpoint correlation")
    return Screen(candidate, M30, M31, cf, omega, adjacent)


def proposal_stream(random_count: int, quick: bool) -> Iterable[tuple[str, int, int, int, int]]:
    """Mandatory baseline followed by focused seam/large-p proposals."""

    # Both exact grids, r <= 16, p <= 40, m <= 20, B <= 20.
    # Integer r starts at 1; half-integer r starts at 3/2.
    r2_values = list(range(2, 33, 2)) + list(range(3, 32, 2))
    p_stop = 15 if quick else 41
    m_stop = 9 if quick else 21
    B_stop = 9 if quick else 21
    for r2 in r2_values:
        for p in range(3, p_stop):
            for m in range(1, m_stop):
                for B in range(2, B_stop):
                    yield ("baseline", r2, p, m, B)

    # Focused one-sided and seam stress: B0=1, small m, large p, and both
    # parities.  These points are extra diagnostics, not finite coverage.
    edge_r2 = [2, 3, 4, 5, 6, 7, 10, 11, 20, 21, 32, 33, 64, 65, 200, 201, 2000, 2001]
    edge_p = list(range(3, 17)) + [20, 24, 32, 40, 48, 64, 96, 128]
    edge_m = list(range(1, 9)) + [10, 12, 16, 20, 32]
    edge_B = list(range(2, 9)) + [10, 12, 16, 20, 32]
    for r2 in edge_r2:
        for p in edge_p:
            for m in edge_m:
                for B in edge_B:
                    yield ("focused", r2, p, m, B)

    rng = random.Random(SEARCH_SEED)
    for _ in range(150 if quick else random_count):
        r2 = rng.choice([2 * rng.randint(1, 20000), 2 * rng.randint(1, 20000) + 1])
        if r2 == 1:
            r2 = 2
        p = rng.choice([rng.randint(3, 40), rng.randint(41, 256)])
        m = rng.choice([rng.randint(1, 5), rng.randint(1, 64)])
        for B in sorted({2, rng.randint(2, 20), rng.choice([3, 4, 8, 16, 32, 64])}):
            yield ("random", r2, p, m, B)


def enrich(hp: r44.HPRecord) -> Record:
    """Compute all Round 45 exact margins from one fixed side vector."""

    d = hp.data
    p = mp.mpf(hp.p)
    r = d["r"]
    x = d["x"]
    q = d["q"]
    mu = d["mu"]
    K = d["K"]
    t = d["t"]
    beta = d["beta"]
    B0 = mp.mpf(d["B0"])
    omega = mp.fsum(
        mp.pi / (2 * row["theta"]) - mp.pi / (2 * t) + 2 * row["eta_adverse"]
        for row in d["inverse_rows"]
    )
    J = 2 * r44.ball_cap(mu, q)
    top = 9 / (64 * mp.pi * mp.sqrt(K * K - q * q) * beta**3)
    curv = d["curvature_reserve"]
    loss = d["p_Estar_minus_E"]
    rhs30 = omega + B0 * d["zeta"] + 9 / (16 * beta) - J + top + curv
    rhs31 = mp.mpf(49) / 40 + top + curv
    M30 = loss - rhs30
    M31 = loss - rhs31
    Ur = mp.sqrt(mu * mu - r * r)
    Ux = mp.sqrt(mu * mu - x * x)
    Uq = mp.sqrt(mu * mu - q * q)
    R1 = (Ur - Ux) / (Ux - Uq)
    adjacent_rhs = R1 * (d["j"] + d["ep"] + d["h"])
    adjacent_margin = d["Delta"] - adjacent_rhs
    E_R1h_margin = d["E"] - R1 * d["h"]
    cf_lhs = (p - d["d"] * hp.m) / 2
    cf_rhs = p * R1 * d["h"] + mp.mpf(49) / 40 + top + curv
    cf_margin = cf_rhs - cf_lhs
    omega_lb = mp.pi**2 / (2 * K * t**3 * mp.sin(t)) * (
        B0 * (B0 + 1) / 2 - B0 * d["u"]
    )
    terminal_beyond_cf = d["D_A"] - mp.mpf(49) / 40 - top
    shelf_beyond_curv = d["C_p"] - curv
    adjacent_beyond_R1h = p * E_R1h_margin
    support_restoration30 = (d["R_tan_zero"] - top) + shelf_beyond_curv
    support_restoration31 = terminal_beyond_cf + shelf_beyond_curv
    metrics: dict[str, object] = {
        "Omega_minus": +omega,
        "J": +J,
        "top_bregman_9_over_64": +top,
        "top_coefficient_replay": +(top * mp.pi * mp.sqrt(K * K - q * q) * beta**3),
        "RHS_S30": +rhs30,
        "RHS_S31": +rhs31,
        "M30": +M30,
        "M31": +M31,
        "R1": +R1,
        "adjacent_rhs": +adjacent_rhs,
        "adjacent_action_margin": +adjacent_margin,
        "E_minus_R1h": +E_R1h_margin,
        "CF_lhs": +cf_lhs,
        "CF_rhs": +cf_rhs,
        "CF_margin": +cf_margin,
        "Omega_primary_R38_lb": +omega_lb,
        "Omega_primary_R38_slack": +(omega - omega_lb),
        "terminal_beyond_count_free": +terminal_beyond_cf,
        "shelf_beyond_curvature": +shelf_beyond_curv,
        "actual_E_beyond_R1h_payment": +adjacent_beyond_R1h,
        "support_restoration_M30": +support_restoration30,
        "support_restoration_M31": +support_restoration31,
        "M30_ledger_residual": +(hp.S + M30 - support_restoration30),
        "M31_ledger_residual": +(hp.S + M31 - support_restoration31),
        "CF_ledger_residual": +(
            hp.S - cf_margin - terminal_beyond_cf - shelf_beyond_curv - adjacent_beyond_R1h
        ),
        "reconciliation": +(1 / (16 * beta)),
        "reconciliation_residual": +d["terminal_relation_residual"],
        "side_vector": "resolved generic: literal and adverse conventions coincide",
    }
    return Record(hp, metrics)


def mp_text(value: object, digits: int = 34) -> object:
    if isinstance(value, mp.mpf):
        return mp.nstr(value, digits)
    if isinstance(value, dict):
        return {str(k): mp_text(v, digits) for k, v in value.items()}
    if isinstance(value, list):
        return [mp_text(v, digits) for v in value]
    return value


def full_ledger(record: Record) -> dict[str, object]:
    hp = record.hp
    ledger = r44.ledger_dict(hp)
    ledger["Round45"] = record.metrics
    ledger["inverse_side_vector"] = [
        {
            "k": row["k"],
            "theta": row["theta"],
            "y": row["y"],
            "count": row["count_adverse"],
            "eta": row["eta_adverse"],
            "literal_count_if_exact_wall": row["count_literal"],
            "literal_eta_if_exact_wall": row["eta_literal"],
            "resolved_side": row["side"],
        }
        for row in hp.data["inverse_rows"]
    ]
    return ledger


def print_ledger(label: str, record: Record, digits: int = 38) -> None:
    print(f"FULL_LEDGER {label}=" + json.dumps(mp_text(full_ledger(record), digits), sort_keys=True))


def decimal_hull(value: mp.mpf, digits: int) -> tuple[fmpq, fmpq]:
    return r44.exact_decimal_q(value, digits, True), r44.exact_decimal_q(value, digits, False)


def arb_hull(lo: fmpq, hi: fmpq) -> arb:
    require(lo <= hi, "invalid rational hull")
    return arb((lo + hi) / 2, (hi - lo) / 2)


def directed_certificate(record: Record, digits: int = 52) -> dict[str, object]:
    """Directed enclosure of owner, four signs, and both exact ledgers.

    The old inverse roots are enclosed independently by signed action
    brackets.  Requiring each root hull to stay in its asserted integer cell
    certifies the direct strict count.  Generic points simultaneously realize
    the literal and adverse conventions; exact collision points would require
    separate one-sided certificates and are not silently admitted here.
    """

    require(arb is not None, "python-flint unavailable")
    ctx.prec = DEFAULT_ARB_BITS
    hp = record.hp
    d = hp.data
    wall = r44.arb_wall_bracket(hp, digits=digits + 6)
    # The imported wall helper uses its own audited default.  Restore this
    # script's stronger working precision for the full-owner enclosure.
    ctx.prec = DEFAULT_ARB_BITS
    tlo, thi = decimal_hull(d["t"], digits + 6)
    t = arb_hull(tlo, thi)
    r_q = fmpq(hp.r2, 2)
    p_q, m_q = fmpq(hp.p), fmpq(hp.m)
    x_q, q_q = r_q + p_q, r_q + p_q + m_q
    if hp.alpha == 1:
        alpha_q = fmpq(1)
    else:
        alpha_q = fmpq(str(mp.nstr(hp.alpha, 80)))
    mu_q = q_q + alpha_q
    mu = arb(mu_q)
    K = mu / t.cos()
    pi = arb.pi()

    def action(radius: arb, z: fmpq) -> arb:
        return r44.arb_ball_action(radius, z)

    def cap(radius: arb, z: fmpq) -> arb:
        return r44.arb_ball_cap(radius, z)

    def shell(z: fmpq) -> arb:
        return action(K, z) - action(mu, z)

    f = int(d["f"])
    sr, sx, sx1 = shell(r_q) + fmpq(1, 4), shell(x_q) + fmpq(1, 4), shell(x_q + 1) + fmpq(1, 4)
    require(f < sr < f + 1, "directed first-shelf left floor")
    require(f < sx < f + 1, "directed first-shelf right floor")
    require(sx1 < f, "directed literal first drop")
    e0, ep = sr - f, sx - f
    E, Delta = e0 + ep, e0 - ep
    d_rho = 1 - 2 * t / pi
    Estar = (p_q - d_rho * m_q) / (2 * p_q)
    require(E >= 0 and E < Estar and Estar < fmpq(1, 2), "directed hard E owner")
    require(p_q - d_rho * m_q > fmpq(11, 5), "directed p-dm owner")
    gamma = fmpq(3, 4) if hp.r2 % 2 == 0 else fmpq(2)
    activity = K * K - pi * pi / (1 - t.cos()) ** 2 - gamma
    require(activity > 0, "directed dimension activity")

    beta = (arb(q_q) / K).acos() / pi
    h = action(mu, q_q)
    W = action(K, mu_q)
    v_q = fmpq(hp.B) - fmpq(1, 4)
    u = v_q - W
    require(h > 0 and u > h and beta > u and beta < fmpq(1, 2), "directed endpoint correlation")

    omega = arb(0)
    spatial_sum = 0
    inverse_brackets: list[dict[str, object]] = []
    for row in d["inverse_rows"]:
        k = int(row["k"])
        ylo, yhi = decimal_hull(row["y"], digits)
        # Widen one decimal ulp to dominate the independent t/K enclosure.
        ulp = fmpq(1, 10**digits)
        ylo, yhi = ylo - ulp, yhi + ulp
        level = fmpq(4 * k - 1, 4)
        Flo = action(K, q_q + ylo) - level
        Fhi = action(K, q_q + yhi) - level
        require(Flo > 0 and Fhi < 0, f"directed inverse bracket k={k}")
        count = int(row["count_adverse"])
        require(count < ylo and yhi < count + 1, f"resolved generic inverse cell k={k}")
        y = arb_hull(ylo, yhi)
        theta = ((arb(q_q) + y) / K).acos()
        eta = y - count
        omega += pi / (2 * theta) - pi / (2 * t) + 2 * eta
        spatial_sum += count
        inverse_brackets.append({"k": k, "lo": str(ylo), "hi": str(yhi), "F_lo": str(Flo), "F_hi": str(Fhi), "cell": [count, count + 1]})

    Q = hp.B - 1
    terminal_count = Q + 2 * spatial_sum
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
    Lzero = omega + (hp.B - 1) * zeta + fmpq(9, 16) / beta - J
    Lplus = omega + (hp.B - 1) * zeta + fmpq(1, 2) / beta - J
    Rzero, Rplus = DA - Lzero, DA - Lplus
    M30 = loss - (Lzero + top + curv)
    M31 = loss - (fmpq(49, 40) + top + curv)
    Ur = (mu * mu - r_q * r_q).sqrt()
    Ux = (mu * mu - x_q * x_q).sqrt()
    Uq = (mu * mu - q_q * q_q).sqrt()
    R1 = (Ur - Ux) / (Ux - Uq)
    CF = p_q * R1 * h + fmpq(49, 40) + top + curv - (p_q - d_rho * m_q) / 2
    adjacent = Delta - R1 * ((f - hp.B) + ep + h)
    require(adjacent > 0, "directed Round42 adjacent-action regression")
    reconciliation = Rplus - Rzero - 1 / (16 * beta)
    require(reconciliation.contains(0), "directed reconciliation enclosure")
    omega_lb = pi**2 / (2 * K * t**3 * t.sin()) * (
        fmpq((hp.B - 1) * hp.B, 2) - (hp.B - 1) * u
    )
    require(omega > omega_lb, "directed primary Round38 Omega bound")
    require(Rzero > top, "directed top-Bregman reserve")
    require(Cp > curv, "directed curvature reserve")
    return {
        "bits": ctx.prec,
        "wall": wall,
        "owner_all_strict": True,
        "side_vector": "all inverse roots certified inside generic cells; literal=adverse",
        "inverse_brackets": inverse_brackets,
        "S": str(S),
        "M30": str(M30),
        "M31": str(M31),
        "CF_margin": str(CF),
        "adjacent_action_margin": str(adjacent),
        "reconciliation_residual": str(reconciliation),
        "Omega_minus": str(omega),
        "Omega_primary_lb": str(omega_lb),
        "R_tan_zero": str(Rzero),
        "top_bregman": str(top),
        "C_p": str(Cp),
        "curvature_reserve": str(curv),
        "signs": {
            "S_positive": bool(S > 0),
            "S_negative": bool(S < 0),
            "M30_positive": bool(M30 > 0),
            "M31_positive": bool(M31 > 0),
            "CF_negative": bool(CF < 0),
        },
        "directed": True,
    }


def candidate_from_record(record: Record, source: str = "one-sided") -> r44.FloatCandidate:
    h = record.hp
    d = h.data
    return r44.FloatCandidate(source, h.r2, h.p, h.m, h.B, int(d["f"]), float(d["t"]), float(h.S), float(d["E"]), float(d["Estar"]), float(d["ep"]), float(d["activity"]), 0.0, 0.0)


def one_sided_rows(record: Record, dps: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    candidate = candidate_from_record(record)
    for exponent in (3, 6, 9, 12, 18):
        alpha = mp.mpf(1) - mp.power(10, -exponent)
        hp = r44.evaluate_hp(candidate, dps, alpha=alpha)
        enriched = enrich(hp)
        rows.append({
            "s": exponent,
            "alpha": alpha,
            "t_resolved": hp.data["t"],
            "K": hp.data["K"],
            "owner": hp.owner,
            "reasons": hp.reasons,
            "S": hp.S,
            "M30": enriched.M30,
            "M31": enriched.M31,
            "CF_margin": enriched.CF,
            "side_vector": enriched.metrics["side_vector"],
        })
    return rows


def fixed_candidate(source: str, r2: int, p: int, m: int, B: int, f: int = 0) -> r44.FloatCandidate:
    t = r44.wall_float(r2 + 2 * (p + m), B)
    require(t is not None, f"missing fixed wall {source}")
    return r44.FloatCandidate(source, r2, p, m, B, f, t, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def regression_bundle(records: list[Record], dps: int) -> dict[str, object]:
    r44_min = enrich(r44.evaluate_hp(fixed_candidate("round44-min", 2, 3, 1, 2, 2), dps))
    expected = mp.mpf("2.694565278900355025629332914750280")
    require(r44_min.hp.owner, "Round44 minimizing tuple owner")
    require(abs(r44_min.S - expected) < mp.power(10, -32), "Round44 minimum value regression")
    r43 = r44.evaluate_hp(r44.round43_candidate(dps), dps)
    require(r43.data["E"] > r43.data["Estar"], "Round43 E>E* regression")
    require([x for x in r43.reasons if x != "hard E owner fails"] == [], "Round43 sole rejection regression")
    r27 = r44.round27_regression(dps)
    r27_directed = r44.round27_arb_check()
    require(r27["automatic_rejection"] and r27["large_positive_S"], "Round27 automatic regression")
    max_reconciliation = max(abs(z.metrics["reconciliation_residual"]) for z in records)
    min_top_slack = min(z.hp.data["R_tan_zero"] - z.metrics["top_bregman_9_over_64"] for z in records)
    min_omega_slack = min(z.metrics["Omega_primary_R38_slack"] for z in records)
    min_adjacent = min(z.metrics["adjacent_action_margin"] for z in records)
    top_coeff_error = max(abs(z.metrics["top_coefficient_replay"] - mp.mpf(9) / 64) for z in records)
    require(max_reconciliation < mp.power(10, -(dps - 12)), "1/(16 beta) regression")
    require(min_top_slack > 0, "9/64 top reserve regression")
    require(min_omega_slack > 0, "Round38 primary Omega regression")
    require(min_adjacent > 0, "Round42 adjacent-action regression")
    require(top_coeff_error < mp.power(10, -(dps - 12)), "top coefficient replay")
    return {
        "round44_minimum": {"tuple": "(r,p,m,f,B,j)=(1,3,1,2,2,0)", "S": r44_min.S, "difference_from_audited": r44_min.S - expected},
        "round43_rejected": {"tuple": "(r,p,m,f,B,j)=(1,9,9,4,3,1)", "E": r43.data["E"], "Estar": r43.data["Estar"], "E_minus_Estar": r43.data["E"] - r43.data["Estar"], "sole_rejection": True},
        "round27_automatic": r27,
        "round27_directed": r27_directed,
        "max_reconciliation_residual": max_reconciliation,
        "min_Rtan0_minus_top": min_top_slack,
        "top_coefficient_max_error": top_coeff_error,
        "min_Omega_primary_slack": min_omega_slack,
        "min_adjacent_action_margin": min_adjacent,
    }


def owner_summary(record: Record) -> str:
    h, d = record.hp, record.hp.data
    return (
        f"r={mp.nstr(d['r'], 12)} p={h.p} m={h.m} f={d['f']} B={h.B} j={d['j']} "
        f"grid={h.grid} S={mp.nstr(h.S, 24)} M30={mp.nstr(record.M30, 24)} "
        f"M31={mp.nstr(record.M31, 24)} CF={mp.nstr(record.CF, 24)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--random", type=int, default=2500)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--skip-directed", action="store_true")
    args = parser.parse_args()
    dps = max(80, args.dps)
    mp.mp.dps = dps

    print("ROUND45C INDEPENDENT EXACT-OWNER SUPPORT SEARCH")
    print("lead_round45_evaluator_imported=False")
    print("audited_round44_independent_definition_engine_reused=True")
    print("projected_scalar_substitution=False")
    print("classification=diagnostic sweep; directed witnesses only")
    print(f"dps={dps}; arb_bits={DEFAULT_ARB_BITS}; seed={SEARCH_SEED}; quick={args.quick}")
    print(f"pinned_base={EXPECTED_BASE}; round44_artifact={EXPECTED_R44_ARTIFACT}; obligation_hash={EXPECTED_OBLIGATION_HASH}")

    seen: set[tuple[int, int, int, int]] = set()
    screens: list[Screen] = []
    proposals = 0
    for source, r2, p, m, B in proposal_stream(args.random, args.quick):
        key = (r2, p, m, B)
        if key in seen:
            continue
        seen.add(key)
        proposals += 1
        candidate = r44.float_candidate(source, r2, p, m, B)
        if candidate is not None:
            screens.append(screen_metrics(candidate))
    print(f"binary64_distinct_proposals={proposals}")
    if not args.quick:
        print("mandatory_baseline_proposals=447640")
    print(f"binary64_owner_candidates={len(screens)}")
    print(f"binary64_negative_S={sum(z.candidate.S < 0 for z in screens)}")
    print(f"binary64_M30_positive={sum(z.M30 > 0 for z in screens)}")
    print(f"binary64_M31_positive={sum(z.M31 > 0 for z in screens)}")
    print(f"binary64_CF_negative={sum(z.CF < 0 for z in screens)}")

    records: list[Record] = []
    rejected: list[r44.HPRecord] = []
    for screen in screens:
        hp = r44.evaluate_hp(screen.candidate, dps)
        if hp.owner:
            records.append(enrich(hp))
        else:
            rejected.append(hp)
    require(records, "no high-precision exact owner")
    print(f"high_precision_exact_owners={len(records)}")
    print(f"high_precision_rejected={len(rejected)}")
    print(f"high_precision_negative_S={sum(z.S < 0 for z in records)}")
    print(f"high_precision_M30_positive={sum(z.M30 > 0 for z in records)}")
    print(f"high_precision_M31_positive={sum(z.M31 > 0 for z in records)}")
    print(f"high_precision_CF_negative={sum(z.CF < 0 for z in records)}")
    print(
        "owner_counts "
        f"integer={sum(z.hp.grid == 'integer' for z in records)} "
        f"half_integer={sum(z.hp.grid == 'half-integer' for z in records)} "
        f"B0_equals_1={sum(z.hp.B == 2 for z in records)} "
        f"baseline={sum(z.hp.source == 'baseline' for z in records)} "
        f"focused={sum(z.hp.source == 'focused' for z in records)} "
        f"random={sum(z.hp.source == 'random' for z in records)}"
    )

    extrema: dict[str, Record] = {
        "minimum_S": min(records, key=lambda z: z.S),
        "maximum_M30": max(records, key=lambda z: z.M30),
        "maximum_M31": max(records, key=lambda z: z.M31),
        "minimum_CF": min(records, key=lambda z: z.CF),
        "near_ep_zero": min(records, key=lambda z: abs(z.hp.data["ep"])),
        "near_Estar": min(records, key=lambda z: z.hp.data["hard_margin"]),
        "near_adverse_inverse": min(records, key=lambda z: min((row["eta_adverse"] for row in z.hp.data["inverse_rows"]), default=mp.mpf(1))),
        "near_literal_inverse": min(records, key=lambda z: min((1 - row["eta_adverse"] for row in z.hp.data["inverse_rows"]), default=mp.mpf(1))),
        "minimum_adjacent_margin": min(records, key=lambda z: z.metrics["adjacent_action_margin"]),
    }
    baseline_records = [z for z in records if z.hp.source == "baseline"]
    integer_records = [z for z in records if z.hp.grid == "integer"]
    half_records = [z for z in records if z.hp.grid == "half-integer"]
    if baseline_records:
        extrema["minimum_CF_baseline"] = min(baseline_records, key=lambda z: z.CF)
    if integer_records:
        extrema["minimum_CF_integer"] = min(integer_records, key=lambda z: z.CF)
    if half_records:
        extrema["minimum_CF_half_integer"] = min(half_records, key=lambda z: z.CF)
    for label, row in extrema.items():
        print(f"diagnostic_extremum {label} " + owner_summary(row))

    regressions = regression_bundle(records, dps)
    print("MANDATORY_REGRESSIONS=" + json.dumps(mp_text(regressions, 42), sort_keys=True))

    # Only extrema are promoted to named witnesses.  All other signs remain
    # high-precision diagnostic candidates, avoiding an unsupported claim of
    # globally directed maximization or positive finite coverage.
    named: list[tuple[str, Record]] = [("minimum_S_diagnostic", extrema["minimum_S"])]
    if extrema["maximum_M30"].M30 > 0:
        named.append(("support_entry_witness", extrema["maximum_M30"]))
    if extrema["minimum_CF"].CF < 0:
        named.append(("count_free_route_counterexample", extrema["minimum_CF"]))
    if "minimum_CF_baseline" in extrema and extrema["minimum_CF_baseline"].CF < 0:
        named.append(("count_free_route_counterexample_baseline", extrema["minimum_CF_baseline"]))
    if "minimum_CF_half_integer" in extrema and extrema["minimum_CF_half_integer"].CF < 0:
        named.append(("count_free_route_counterexample_half_integer", extrema["minimum_CF_half_integer"]))
    if extrema["maximum_M31"].M31 > 0:
        named.append(("count_free_support_entry_witness", extrema["maximum_M31"]))
    if any(z.S < 0 for z in records):
        named.append(("gate_trigger_candidate", min((z for z in records if z.S < 0), key=lambda z: z.S)))
    named.append(("near_adverse_inverse_diagnostic", extrema["near_adverse_inverse"]))
    named.append(("near_literal_inverse_diagnostic", extrema["near_literal_inverse"]))

    emitted: set[tuple[str, tuple[int, int, int, int]]] = set()
    for label, row in named:
        marker = (label, row.key)
        if marker in emitted:
            continue
        print_ledger(label, row)
        if not args.skip_directed:
            certificate = directed_certificate(row)
            print(f"DIRECTED_CERTIFICATE {label}=" + json.dumps(certificate, sort_keys=True))
            signs = certificate["signs"]
            if label == "support_entry_witness":
                require(signs["M30_positive"] and signs["S_positive"], "support witness directed classification")
            elif label.startswith("count_free_route_counterexample"):
                require(signs["CF_negative"] and signs["S_positive"], "CF witness directed classification")
            elif label == "count_free_support_entry_witness":
                require(signs["M31_positive"] and signs["S_positive"], "M31 witness directed classification")
            elif label == "gate_trigger_candidate":
                require(signs["S_negative"], "Gate trigger directed sign")
            elif label.startswith("near_") or label == "minimum_S_diagnostic":
                require(signs["S_positive"], "directed positive diagnostic sign")
        emitted.add(marker)

    one_sided_targets: dict[tuple[int, int, int, int], tuple[str, Record]] = {}
    for label in ("minimum_S", "maximum_M30", "minimum_CF", "near_adverse_inverse", "near_literal_inverse"):
        row = extrema[label]
        one_sided_targets[row.key] = (label, row)
    for label in ("minimum_CF_baseline", "minimum_CF_half_integer"):
        if label in extrema:
            row = extrema[label]
            one_sided_targets[row.key] = (label, row)
    for label, row in one_sided_targets.values():
        print(f"ONE_SIDED {label}=" + json.dumps(mp_text(one_sided_rows(row, dps), 40), sort_keys=True))

    negative = [z for z in records if z.S < 0]
    support = [z for z in records if z.M30 > 0]
    route = [z for z in records if z.CF < 0]
    print(f"gate_trigger_certificate_found={bool(negative and not args.skip_directed)}")
    print(f"support_entry_witness_found={bool(support)}")
    print(f"count_free_route_counterexample_found={bool(route)}")
    print("positive_coverage_certificate=False")
    if negative:
        print("conclusion=directed negative processed above; Gate-B classification requires audit")
    elif route:
        print("conclusion=count-free sufficient route is false on a directed exact owner; full S remains positive there; Gate B not stopped")
    elif support:
        print("conclusion=localized support is entered but full S remains positive on named witness; Gate B not stopped")
    else:
        print("conclusion=no route failure, support entry, or negative S found in finite diagnostics; no coverage claim")


if __name__ == "__main__":
    main()
