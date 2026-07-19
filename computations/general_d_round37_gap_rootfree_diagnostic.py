#!/usr/bin/env python3
"""Diagnostic-only search for the Round 37 root-free gap gate.

This imports the exact owner/wall sampler used in Round 27 and checks the
Round 37 synchronized interface count and projected gap scalars.  Ordinary
double precision and finite sampling provide theorem-design evidence only;
they do not certify a continuum sign.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import random
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUND27_PATH = (
    ROOT / "computations" / "general_d_round27_exact_phi_hard_sector_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location("round27_gap_gate", ROUND27_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND27_PATH}")
R27 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R27
SPEC.loader.exec_module(R27)


@dataclass(frozen=True)
class GapGate:
    record: object
    b0: int
    action_deficit: int
    lam: float
    exact_cap_gate: float
    seventh_gate: float
    actual_projection: float
    exact_shelf_gate: float
    phi_delta_plus: float


def evaluate_gate(record: object) -> GapGate:
    r, p, m, f = record.r, record.p, record.m, record.f
    alpha, t = record.alpha, record.t
    q = r + p + m
    mu = q + alpha
    outer = mu / math.cos(t)
    c = t / math.pi
    d = 1 - 2 * c

    w = mu / math.pi * (math.tan(t) - t)
    lam = f - 0.25 - w
    b0 = R27.strict_floor(w + 0.25)
    action_deficit = f - record.B
    if b0 != record.B - 1:
        raise ArithmeticError("Round 37 interface count synchronization failed")
    tolerance = 2.0e-8
    if not (
        action_deficit - tolerance <= lam < action_deficit + 1 + tolerance
    ):
        raise ArithmeticError("Round 37 lambda band failed")

    x = m + alpha
    stretch = math.sqrt(
        1 + p * (2 * r + p) / (x * (x + 2 * r + 2 * p))
    )
    a_p = p * p / (3 * (2 * r + p))
    j_cap = 2 * R27.ball_integral(mu, q)
    exact_cap_gate = (
        b0 * d / (2 * c)
        + 1
        - j_cap
        + (p + a_p) * (stretch - 1) * lam
        - (p - d * m) / 2
    )
    seventh_gate = (
        b0 * d / (2 * c)
        + 6 / 7
        + (p + a_p) * (stretch - 1) * lam
        - (p - d * m) / 2
    )

    shell_r = R27.shell_action(mu, t, r)
    shell_x = R27.shell_action(mu, t, r + p)
    e0 = shell_r + 0.25 - f
    ep = shell_x + 0.25 - f
    e_sum = e0 + ep
    tau = (stretch - 1) / (stretch + 1)
    elastic = tau * (e_sum + 2 * lam)
    outer_curvature = (
        (mu ** (-1) - outer ** (-1))
        * ((r + p) ** 2 - r**2)
        / (2 * math.pi)
        + (mu ** (-3) - outer ** (-3))
        * ((r + p) ** 4 - r**4)
        / (24 * math.pi)
    )
    m4 = max(elastic, outer_curvature)
    e_star = (p - d * m) / (2 * p)

    v = R27.ball_action(outer, q)
    beta = math.acos(q / outer) / math.pi
    top = max(v - record.B, 0.0) ** 2 / beta if record.B else 0.0
    terminal_without_top = record.LT - top
    actual_projection = terminal_without_top + a_p * m4 + p * (e_sum - e_star)

    delta = e0 - ep
    zeta = d / (2 * c)
    frac_lam = lam - action_deficit
    g = stretch - 1
    a_star = (p + a_p) * g
    shelf_elastic = (f - 1) * min(zeta, a_star) + a_star * (
        frac_lam + ep
    )
    shelf_curvature = zeta + (p + a_p) * outer_curvature
    x = r + p
    u_r = math.sqrt(mu * mu - r * r)
    u_x = math.sqrt(mu * mu - x * x)
    u_q = math.sqrt(mu * mu - q * q)
    # Rationalize both small square-root differences.  This is algebraically
    # identical to (u_r-u_x)/(u_x-u_q), but remains stable when r is large.
    adjacent_ratio = (
        (x * x - r * r) * (u_x + u_q)
        / ((q * q - x * x) * (u_r + u_x))
    )
    adjacent_star = (p + a_p) * adjacent_ratio
    shelf_adjacent = (f - 1) * min(zeta, adjacent_star) + adjacent_star * ep
    shelf_payment = b0 * zeta + (p + a_p) * delta
    exact_shelf_gate = (
        1
        - j_cap
        + max(shelf_elastic, shelf_curvature, shelf_adjacent)
        + 2 * p * ep
        - (p - d * m) / 2
    )
    phi_delta_plus = record.PhiMax

    comparison_tolerance = 3.0e-7 * max(
        1.0, abs(actual_projection), abs(phi_delta_plus)
    )
    if actual_projection + comparison_tolerance < exact_cap_gate:
        raise ArithmeticError("root-free gate exceeded the actual projection")
    if exact_cap_gate + comparison_tolerance < seventh_gate:
        raise ArithmeticError("cap-relaxed gate exceeded the exact-cap gate")
    if phi_delta_plus + comparison_tolerance < exact_shelf_gate:
        raise ArithmeticError("exact-shelf gate exceeded Phi_delta_plus")
    if delta + comparison_tolerance < g * (lam + ep):
        raise ArithmeticError("exact shelf elasticity failed")
    if shelf_payment + comparison_tolerance < shelf_elastic:
        raise ArithmeticError("elastic shelf payment exceeded its source")
    if shelf_payment + comparison_tolerance < shelf_curvature:
        raise ArithmeticError("quartic shelf payment exceeded its source")
    if shelf_payment + comparison_tolerance < shelf_adjacent:
        raise ArithmeticError("adjacent-action shelf payment exceeded its source")

    return GapGate(
        record,
        b0,
        action_deficit,
        lam,
        exact_cap_gate,
        seventh_gate,
        actual_projection,
        exact_shelf_gate,
        phi_delta_plus,
    )


def summarize(name: str, records: list[GapGate], key) -> None:
    best = min(records, key=key)
    rec = best.record
    d = 1 - 2 * rec.t / math.pi
    print(
        f"min {name}={key(best):.15g} at "
        f"r={rec.r:g} p={rec.p} m={rec.m} f={rec.f} "
        f"alpha={rec.alpha:g} t={rec.t:.15g} "
        f"B={rec.B} Q={rec.Q} B0={best.b0} j={best.action_deficit} "
        f"lambda={best.lam:.12g} p-dm={rec.p-d*rec.m:.12g}"
    )


def run(limit: int, random_count: int, wall_limit: int) -> None:
    random.seed(20260737)
    results: list[GapGate] = []
    alphas = (
        0.0,
        1.0e-6,
        1.0e-4,
        1.0e-3,
        1 / 16,
        0.25,
        0.5,
        0.75,
        0.9,
        0.99,
        0.999999,
    )
    radii = list(range(1, limit + 1)) + [
        20,
        50,
        100,
        1000,
        10000,
        1.0e6,
        1.0e8,
    ]
    shelf_lengths = list(range(1, min(limit, 10) + 1)) + [12, 20, 32, 48, 80]
    gaps = (1, 2, 3, 4, 6, 10, 20)
    floors = (2, 3, 4, 6, 10, 16)

    def add_tuple(r: float, p: int, m: int, f: int, alpha: float) -> None:
        try:
            candidates = R27.hard_candidates(r, p, m, f, alpha, wall_limit)
        except (ArithmeticError, OverflowError, ValueError, ZeroDivisionError):
            return
        for record in candidates:
            d = 1 - 2 * record.t / math.pi
            if record.B != record.Q + 1 or p - d * m <= 12 / 7:
                continue
            results.append(evaluate_gate(record))

    for offset in (0.0, 0.5):
        for radius in radii:
            r = float(radius) + offset
            if offset and r < 1.5:
                continue
            for p in shelf_lengths:
                for m in gaps:
                    for f in floors:
                        for alpha in alphas:
                            add_tuple(r, p, m, f, alpha)

    for _ in range(random_count):
        half_grid = random.choice((False, True))
        r = float(max(1, round(math.exp(random.uniform(0, math.log(1.0e8))))))
        if half_grid:
            r += 0.5
        p = max(1, round(math.exp(random.uniform(0, math.log(300)))))
        m = max(1, round(math.exp(random.uniform(0, math.log(100)))))
        f = random.choice((2, 2, 3, 4, 6, 10, 16))
        alpha = random.choice(alphas + (random.random(),))
        add_tuple(r, p, m, f, alpha)

    if not results:
        raise RuntimeError("no residual gap record was retained")

    print("ROUND 37 ROOT-FREE GAP SCAN (NON-CERTIFIED)")
    print(f"retained evaluations={len(results)}")
    print("arithmetic=ordinary_double_precision")
    print("coverage=finite_owner_wall_samples_only")
    summarize("F_J", results, lambda item: item.exact_cap_gate)
    summarize("F_7", results, lambda item: item.seventh_gate)
    summarize("actual_projection", results, lambda item: item.actual_projection)
    summarize("H_Delta", results, lambda item: item.exact_shelf_gate)
    summarize("Phi_delta_plus", results, lambda item: item.phi_delta_plus)
    print(
        "nonpositive counts: "
        f"F_J={sum(item.exact_cap_gate <= 0 for item in results)} "
        f"F_7={sum(item.seventh_gate <= 0 for item in results)} "
        f"actual={sum(item.actual_projection <= 0 for item in results)} "
        f"H_Delta={sum(item.exact_shelf_gate <= 0 for item in results)} "
        f"Phi={sum(item.phi_delta_plus <= 0 for item in results)}"
    )
    print(f"B0ZeroCount={sum(item.b0 == 0 for item in results)}")
    print("round37InterfaceSynchronizationOK=True")
    print("scanCertification=diagnostic_only")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--random", type=int, default=500)
    parser.add_argument("--wall-limit", type=int, default=50)
    args = parser.parse_args()
    run(args.limit, args.random, args.wall_limit)


if __name__ == "__main__":
    main()
