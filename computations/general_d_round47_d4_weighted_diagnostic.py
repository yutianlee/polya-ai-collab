#!/usr/bin/env python3
"""Round 47 lead diagnostic for the literal d=4 weighted aggregate.

This program is a diagnostic/replay aid, not a positive coverage
certificate.  It builds the strict proxy and the branching side
independently, checks the L3/L4 identities numerically, extracts maximal
negative components, and probes deliberately difficult walls.

The strict bracket is always evaluated literally as max(0, ceil(x)-1).
Near-wall records are printed with their distance to the nearest integer and
must not be interpreted as directed certificates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


mp.mp.dps = 80


def ball_action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Zero-extended G_radius(z)."""
    radius = mp.mpf(radius)
    z = mp.mpf(z)
    if z >= radius:
        return mp.mpf(0)
    x = z / radius
    return radius * (mp.sqrt(1 - x * x) - x * mp.acos(x)) / mp.pi


def ball_tail_integral(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Exact integral of G_radius from z to radius."""
    radius = mp.mpf(radius)
    z = mp.mpf(z)
    if z >= radius:
        return mp.mpf(0)
    x = z / radius
    return (
        radius**2
        * ((1 + 2 * x * x) * mp.acos(x) - 3 * x * mp.sqrt(1 - x * x))
        / (4 * mp.pi)
    )


def shell_action(rho: mp.mpf, K: mp.mpf, z: mp.mpf) -> mp.mpf:
    return ball_action(K, z) - ball_action(rho * K, z)


def shell_tail_integral(rho: mp.mpf, K: mp.mpf, z: mp.mpf) -> mp.mpf:
    return ball_tail_integral(K, z) - ball_tail_integral(rho * K, z)


def minus_shell_derivative(rho: mp.mpf, K: mp.mpf, z: mp.mpf) -> mp.mpf:
    """The nonnegative density -A'(z), with zero extension."""
    mu = rho * K
    if z >= K:
        return mp.mpf(0)
    if z < mu:
        return (mp.acos(z / K) - mp.acos(z / mu)) / mp.pi
    return mp.acos(z / K) / mp.pi


def strict_bracket(x: mp.mpf) -> int:
    """[x]_< = #{n in N: n < x}; exact convention at integer walls."""
    return max(0, int(mp.ceil(x)) - 1)


def delta4(z: mp.mpf) -> mp.mpf:
    """The continuous d=4 discrepancy primitive."""
    z = mp.mpf(z)
    if z < 1:
        return -(z**3) / 6
    a = int(mp.floor(z))
    x = z - a
    return -mp.mpf(a) / 6 + mp.mpf(a) * x * (1 - x) / 2 - x**3 / 6


def cell_minimum(a: int) -> mp.mpf:
    if a == 0:
        return mp.mpf(0)
    aa = mp.mpf(a)
    return aa * (aa + 1) / (12 * (aa + mp.mpf("0.5") + mp.sqrt(aa * (aa + 1))))


def triangular(a: int) -> int:
    return a * (a + 1) // 2


@dataclass
class Evaluation:
    rho: mp.mpf
    K: mp.mpf
    mu: mp.mpf
    q: list[int]
    A_integer: list[mp.mpf]
    D: list[mp.mpf]
    L: list[mp.mpf]
    W4: mp.mpf
    P4: mp.mpf
    bonus: mp.mpf
    master: mp.mpf
    recurrence_error: mp.mpf
    summation_error: mp.mpf
    direct_master_error: mp.mpf
    components: list[tuple[int, int]]
    min_wall_distance: mp.mpf

    @property
    def WT4(self) -> mp.mpf:
        return self.W4 - self.P4


def q_sequence(rho: mp.mpf, K: mp.mpf, terminal: int) -> tuple[list[int], list[mp.mpf], mp.mpf]:
    q = [0] * (terminal + 2)
    values = [mp.mpf(0)] * (terminal + 2)
    wall_distance = mp.inf
    for a in range(1, terminal + 2):
        value = shell_action(rho, K, a)
        values[a] = value
        shifted = value + mp.mpf(1) / 4
        q[a] = strict_bracket(shifted)
        wall_distance = min(wall_distance, abs(shifted - mp.nint(shifted)))
    return q, values, wall_distance


def bonus_cell(rho: mp.mpf, K: mp.mpf, a: int) -> mp.mpf:
    left = mp.mpf(a)
    right = min(mp.mpf(a + 1), K)
    if right <= left:
        return mp.mpf(0)
    mu = rho * K
    breaks = [left]
    if left < mu < right:
        breaks.append(mu)
    breaks.append(right)
    return 2 * mp.fsum(
        mp.quad(lambda z: minus_shell_derivative(rho, K, z) * (-delta4(z)), [x, y])
        for x, y in zip(breaks[:-1], breaks[1:])
    )


def evaluate(rho_value: str | float | mp.mpf, K_value: str | float | mp.mpf) -> Evaluation:
    rho = mp.mpf(rho_value)
    K = mp.mpf(K_value)
    mu = rho * K
    terminal = int(mp.ceil(K)) + 2
    q, A_integer, min_wall_distance = q_sequence(rho, K, terminal)

    suffix = [0] * (terminal + 3)
    for a in range(terminal + 1, 0, -1):
        suffix[a] = suffix[a + 1] + q[a]

    D = [mp.mpf(0)] * (terminal + 2)
    L = [mp.mpf(0)] * (terminal + 2)
    for a in range(1, terminal + 1):
        D[a] = 2 * shell_tail_integral(rho, K, a) - q[a] - 2 * suffix[a + 1]
        L[a] = (
            2 * (shell_tail_integral(rho, K, a) - shell_tail_integral(rho, K, a + 1))
            - q[a]
            - q[a + 1]
        )

    recurrence_error = max(abs(D[a] - D[a + 1] - L[a]) for a in range(1, terminal))
    weighted_D = mp.fsum(mp.mpf(a) * D[a] for a in range(1, terminal + 1))
    weighted_L = mp.fsum(mp.mpf(triangular(a)) * L[a] for a in range(1, terminal + 1))
    summation_error = abs(weighted_D - weighted_L)

    W4 = (K**4 - mu**4) / 64
    P4 = mp.fsum(mp.mpf(a * a * q[a]) for a in range(1, terminal + 1))
    bonus_cells = [bonus_cell(rho, K, a) for a in range(0, int(mp.ceil(K)))]
    bonus = mp.fsum(bonus_cells)
    master = bonus + weighted_D
    direct_master_error = abs((W4 - P4) - master)

    negative = [a for a in range(1, terminal + 1) if a < K and D[a] < 0]
    components: list[tuple[int, int]] = []
    if negative:
        u = v = negative[0]
        for a in negative[1:]:
            if a == v + 1:
                v = a
            else:
                components.append((u, v))
                u = v = a
        components.append((u, v))

    return Evaluation(
        rho=rho,
        K=K,
        mu=mu,
        q=q,
        A_integer=A_integer,
        D=D,
        L=L,
        W4=W4,
        P4=P4,
        bonus=bonus,
        master=master,
        recurrence_error=recurrence_error,
        summation_error=summation_error,
        direct_master_error=direct_master_error,
        components=components,
        min_wall_distance=min_wall_distance,
    )


def component_identity(ev: Evaluation, u: int, v: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    lhs = mp.fsum(mp.mpf(a) * ev.D[a] for a in range(u, v + 1))
    boundary_weight = triangular(v) - triangular(u - 1)
    rhs = mp.mpf(boundary_weight) * ev.D[v + 1]
    rhs += mp.fsum(
        mp.mpf(triangular(j) - triangular(u - 1)) * ev.L[j]
        for j in range(u, v + 1)
    )
    return lhs, rhs, abs(lhs - rhs)


def coarse_bonus_lower(ev: Evaluation) -> mp.mpf:
    return mp.fsum(ev.A_integer[j] for j in range(1, len(ev.A_integer)) if j < ev.K) / 12


def active_wall(rho: mp.mpf) -> mp.mpf:
    return mp.sqrt(mp.pi**2 / (1 - rho) ** 2 + mp.mpf(3) / 4)


def fmt(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def compact_record(ev: Evaluation) -> dict[str, object]:
    records = []
    for u, v in ev.components:
        lhs, rhs, err = component_identity(ev, u, v)
        records.append(
            {
                "u": u,
                "v": v,
                "weighted_charge": fmt(lhs),
                "identity_error": fmt(err, 8),
                "right_boundary": fmt(ev.D[v + 1]),
            }
        )
    return {
        "rho": fmt(ev.rho),
        "K": fmt(ev.K),
        "mu": fmt(ev.mu),
        "active_margin": fmt(ev.K**2 - active_wall(ev.rho) ** 2),
        "W4": fmt(ev.W4),
        "P4": fmt(ev.P4),
        "WT4": fmt(ev.WT4),
        "bonus": fmt(ev.bonus),
        "coarse_bonus_lower": fmt(coarse_bonus_lower(ev)),
        "master": fmt(ev.master),
        "recurrence_error": fmt(ev.recurrence_error, 8),
        "summation_error": fmt(ev.summation_error, 8),
        "direct_master_error": fmt(ev.direct_master_error, 8),
        "min_action_wall_distance": fmt(ev.min_wall_distance, 10),
        "negative_components": records,
    }


def named_cases() -> Iterable[tuple[str, str, str]]:
    cases: list[tuple[str, mp.mpf, mp.mpf]] = []
    for name, rho, factor in (
        ("small-rho-near-activity", mp.mpf("0.0001"), mp.mpf("1.00000001")),
        ("moderate-near-activity", mp.mpf("0.5"), mp.mpf("1.000001")),
        ("thin-near-activity", mp.mpf("0.99"), mp.mpf("1.000001")),
    ):
        cases.append((name, rho, active_wall(rho) * factor))
    cases.extend(
        [
            ("integer-K-and-mu", mp.mpf(9) / 10, mp.mpf(40)),
            ("integer-K", mp.mpf("0.731"), mp.mpf(50)),
            ("near-integer-K-left", mp.mpf("0.731"), mp.mpf("49.99999999")),
            ("near-integer-K-right", mp.mpf("0.731"), mp.mpf("50.00000001")),
        ]
    )
    for name, rho, K in cases:
        yield name, fmt(rho, 40), fmt(K, 40)


def random_stress(seed: int, samples: int) -> dict[str, object]:
    """Fast direct-proxy sweep; no integral/bonus quadrature is used here."""
    rng = random.Random(seed)
    best: tuple[mp.mpf, tuple[mp.mpf, mp.mpf, mp.mpf] | None] = (mp.inf, None)
    negative = None
    evaluated = 0
    for _ in range(samples):
        selector = rng.random()
        if selector < 0.25:
            rho = mp.mpf(10) ** mp.mpf(rng.uniform(-6, -0.05))
        elif selector < 0.55:
            rho = 1 - mp.mpf(10) ** mp.mpf(rng.uniform(-3, -0.05))
        else:
            rho = mp.mpf(rng.random())
        wall = active_wall(rho)
        K = wall * (1 + mp.mpf(10) ** mp.mpf(rng.uniform(-9, 1.3)))
        if K > 5000:
            continue
        terminal = int(mp.ceil(K)) + 1
        P4 = mp.mpf(0)
        min_wall = mp.inf
        for a in range(1, terminal + 1):
            shifted = shell_action(rho, K, a) + mp.mpf(1) / 4
            P4 += a * a * strict_bracket(shifted)
            min_wall = min(min_wall, abs(shifted - mp.nint(shifted)))
        W4 = (K**4 - (rho * K) ** 4) / 64
        WT4 = W4 - P4
        evaluated += 1
        if WT4 < best[0]:
            best = (WT4, (rho, K, min_wall))
        if WT4 < 0:
            negative = (rho, K, WT4, min_wall)
            break
    rho, K, wall_distance = best[1] if best[1] else (mp.nan, mp.nan, mp.nan)
    return {
        "seed": seed,
        "requested": samples,
        "evaluated": evaluated,
        "negative_literal_WT4_found": negative is not None,
        "smallest_WT4": fmt(best[0]),
        "smallest_rho": fmt(rho),
        "smallest_K": fmt(K),
        "smallest_record_wall_distance": fmt(wall_distance, 12),
        "positive_coverage_certificate": False,
    }


def symbolic_numeric_launch_checks() -> dict[str, object]:
    minimum_errors = []
    strict_gaps = []
    for a in range(1, 100):
        aa = mp.mpf(a)
        xstar = mp.sqrt(aa * (aa + 1)) - aa
        value = -(-aa / 6 + aa * xstar * (1 - xstar) / 2 - xstar**3 / 6)
        exact = cell_minimum(a)
        minimum_errors.append(abs(value - exact))
        strict_gaps.append(exact - aa / 24)
    return {
        "max_L1_minimum_formula_error_a_1_to_99": fmt(max(minimum_errors), 10),
        "min_L1_gap_over_a_div_24_a_1_to_99": fmt(min(strict_gaps)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=1500)
    parser.add_argument("--seed", type=int, default=470047)
    parser.add_argument("--quick", action="store_true", help="skip expensive named master-identity quadratures")
    args = parser.parse_args()

    output: dict[str, object] = {
        "classification": "diagnostic_only",
        "literal_target": "WT4 = (K^4-(rho K)^4)/64 - sum_{a>=1} a^2 [A(a)+1/4]_<",
        "launch_checks": symbolic_numeric_launch_checks(),
        "random_stress": random_stress(args.seed, args.samples),
        "positive_coverage_certificate": False,
    }
    if not args.quick:
        output["named_cases"] = []
        for name, rho, K in named_cases():
            ev = evaluate(rho, K)
            rec = compact_record(ev)
            rec["name"] = name
            output["named_cases"].append(rec)

        # A deliberately false over-local comparison.  It is not a component
        # theorem: at rho=9/10, K=40, a=29 is not a negative D component.
        ev = evaluate(mp.mpf(9) / 10, 40)
        a = 29
        false_route = bonus_cell(ev.rho, ev.K, a) + triangular(a) * ev.L[a]
        output["falsification_probe"] = {
            "name": "cell-self-charge",
            "rho": "9/10",
            "K": "40",
            "a": a,
            "B_cell_plus_Ta_La": fmt(false_route),
            "literal_WT4": fmt(ev.WT4),
            "classification": "sufficient_route_counterexample_if_directed_certified",
            "component_claimed": False,
        }

    encoded = json.dumps(output, indent=2, sort_keys=True)
    print(encoded)
    print("output_sha256:", hashlib.sha256((encoded + "\n").encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
