#!/usr/bin/env python3
"""Round 49 lead diagnostic for the clipped interface-to-top suffix.

This evaluator is deliberately diagnostic.  It computes the literal d=4
aggregate, the canonical suffix, its outer-reserve fallback, complete cells,
and the terminal top row.  The suffix is evaluated independently in
inverse-height and clipped-spatial forms.  Finite positive output is never
reported as continuum coverage.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass

import mpmath as mp


mp.mp.dps = 80


def strict_bracket(x: mp.mpf) -> int:
    """[x]_< = max(0, ceil(x)-1), including positive integer walls."""
    return max(0, int(mp.ceil(x)) - 1)


def sum_squares(n: int) -> int:
    return n * (n + 1) * (2 * n + 1) // 6


def ball_action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf("0")
    if z <= 0:
        return radius / mp.pi
    return (
        mp.sqrt(radius * radius - z * z)
        - z * mp.acos(z / radius)
    ) / mp.pi


def shell_action(K: mp.mpf, mu: mp.mpf, z: mp.mpf) -> mp.mpf:
    return ball_action(K, z) - ball_action(mu, z)


def ball_moment_primitive(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Integral_0^z u^3 acos(u/R)/pi du, constantly extended at R."""
    if z <= 0:
        return mp.mpf("0")
    if z >= radius:
        return 3 * radius**4 / 64
    root = mp.sqrt(radius * radius - z * z)
    return (
        3 * radius**4 * mp.asin(z / radius)
        - z * root * (3 * radius * radius + 2 * z * z)
        + 8 * z**4 * mp.acos(z / radius)
    ) / (32 * mp.pi)


def shell_moment_primitive(K: mp.mpf, mu: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Integral_0^z u^3 sigma(u) du for sigma=-A'."""
    return ball_moment_primitive(K, z) - ball_moment_primitive(mu, z)


def inverse_action(K: mp.mpf, mu: mp.mpf, level: mp.mpf) -> mp.mpf:
    H = shell_action(K, mu, mp.mpf("0"))
    if level <= 0:
        return K
    if level >= H:
        return mp.mpf("0")
    lo = mp.mpf("0")
    hi = K
    for _ in range(280):
        mid = (lo + hi) / 2
        if shell_action(K, mu, mid) > level:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def inverse_supply(
    K: mp.mpf, mu: mp.mpf, low: mp.mpf, high: mp.mpf
) -> mp.mpf:
    """Integral_low^high xi(t)^3/3 dt from the exact spatial primitive."""
    if high <= low:
        return mp.mpf("0")
    x_low = inverse_action(K, mu, low)
    x_high = inverse_action(K, mu, high)
    return (
        shell_moment_primitive(K, mu, x_low)
        - shell_moment_primitive(K, mu, x_high)
    ) / 3


def nearest_integer_distance(x: mp.mpf) -> mp.mpf:
    return abs(x - mp.nint(x))


def q_one_crossing(K: mp.mpf, mu: mp.mpf) -> mp.mpf:
    """Numerically locate the unique zero proved analytically in Round 49."""
    rho = mu / K

    def phi(u: mp.mpf) -> mp.mpf:
        return 2 * mp.asin(u) - u / mp.sqrt(1 - u * u)

    def g(x: mp.mpf) -> mp.mpf:
        return phi(x) - phi(rho * x)

    lo = 1 / mp.sqrt(2)
    hi = mp.mpf("1") - mp.mpf("1e-50")
    for _ in range(280):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return mu * (lo + hi) / 2


@dataclass
class Ledger:
    rho: str
    K: str
    mu: str
    active_slack: str
    H: str
    tau: str
    b: int
    Hhat: str
    q: int
    alpha: str
    R: str
    B_mu: str
    suffix_inverse: str
    suffix_spatial: str
    suffix_form_gap: str
    outer_reserve: str
    fallback: str
    WT4: str
    WT4_inverse: str
    WT4_form_gap: str
    min_action_wall_distance: str
    curvature_zero: str
    complete_cells: list[dict[str, object]]
    top: dict[str, object]


def evaluate(rho_value: mp.mpf | str, K_value: mp.mpf | str) -> Ledger:
    rho = mp.mpf(rho_value)
    K = mp.mpf(K_value)
    mu = rho * K
    H = (K - mu) / mp.pi
    tau = ball_action(K, mu)
    b = int(mp.floor(tau))
    Hhat = H - b
    q = int(mp.floor(Hhat))
    alpha = Hhat - q
    R = inverse_action(K, mu, mp.mpf(b))
    B_mu = tau - b

    # Inverse-height suffix ledger.
    suffix_supply = inverse_supply(K, mu, mp.mpf(b), H)
    suffix_cost = 0
    node_rows: list[dict[str, object]] = []
    k = 1
    while mp.mpf(k) - mp.mpf(1) / 4 < Hhat:
        level = mp.mpf(b + k) - mp.mpf(1) / 4
        eta = inverse_action(K, mu, level)
        M = strict_bracket(eta)
        suffix_cost += sum_squares(M)
        node_rows.append(
            {
                "k": k,
                "node": mp.nstr(mp.mpf(k) - mp.mpf(1) / 4, 30),
                "eta": mp.nstr(eta, 30),
                "M": M,
                "S2": sum_squares(M),
            }
        )
        k += 1
    suffix_inverse = suffix_supply - suffix_cost

    # Clipped-spatial form, independently summing the radial strict bracket.
    spatial_cost = 0
    wall_distances: list[mp.mpf] = []
    for a in range(1, int(mp.ceil(R))):
        if mp.mpf(a) >= R:
            continue
        B_a = max(mp.mpf("0"), shell_action(K, mu, mp.mpf(a)) - b)
        x = B_a + mp.mpf(1) / 4
        spatial_cost += a * a * strict_bracket(x)
        wall_distances.append(nearest_integer_distance(x))
    suffix_spatial = shell_moment_primitive(K, mu, R) / 3 - spatial_cost

    cells: list[dict[str, object]] = []
    outer_reserve = mp.mpf("0")
    for n in range(1, b + 1):
        r = inverse_action(K, mu, mp.mpf(n) - mp.mpf(1) / 4)
        N = strict_bracket(r)
        reserve = mp.mpf(19 * N) / 48 + mp.mpf(27) / 128
        outer_reserve += reserve

    for k in range(1, q + 1):
        low = mp.mpf(b + k - 1)
        high = mp.mpf(b + k)
        supply = inverse_supply(K, mu, low, high)
        r = inverse_action(K, mu, mp.mpf(b + k) - mp.mpf(1) / 4)
        M = strict_bracket(r)
        cells.append(
            {
                "k": k,
                "supply": mp.nstr(supply, 30),
                "M": M,
                "cost": sum_squares(M),
                "L": mp.nstr(supply - sum_squares(M), 30),
                "branch": (
                    "interface"
                    if k == 1 and B_mu > 0
                    else "inner"
                ),
            }
        )

    top_supply = inverse_supply(K, mu, mp.mpf(b + q), H)
    top_has_node = alpha > mp.mpf(3) / 4
    if top_has_node:
        top_eta = inverse_action(
            K, mu, mp.mpf(b + q) + mp.mpf(3) / 4
        )
        top_M = strict_bracket(top_eta)
        top_cost = sum_squares(top_M)
    else:
        top_eta = mp.mpf("0")
        top_M = 0
        top_cost = 0
    top = {
        "alpha": mp.nstr(alpha, 30),
        "node_included": top_has_node,
        "eta": mp.nstr(top_eta, 30),
        "M": top_M,
        "supply": mp.nstr(top_supply, 30),
        "cost": top_cost,
        "T_top": mp.nstr(top_supply - top_cost, 30),
    }

    # Literal aggregate and independent all-height inverse form.
    literal_cost = 0
    for a in range(1, int(mp.ceil(K))):
        if mp.mpf(a) >= K:
            continue
        x = shell_action(K, mu, mp.mpf(a)) + mp.mpf(1) / 4
        literal_cost += a * a * strict_bracket(x)
        wall_distances.append(nearest_integer_distance(x))
    WT4 = (K**4 - mu**4) / 64 - literal_cost

    inverse_total_cost = 0
    n = 1
    while mp.mpf(n) - mp.mpf(1) / 4 < H:
        r = inverse_action(K, mu, mp.mpf(n) - mp.mpf(1) / 4)
        inverse_total_cost += sum_squares(strict_bracket(r))
        n += 1
    WT4_inverse = inverse_supply(K, mu, mp.mpf("0"), H) - inverse_total_cost

    active_slack = K**2 - mp.pi**2 / (1 - rho) ** 2 - mp.mpf(3) / 4
    minimum_wall = min(wall_distances) if wall_distances else mp.inf

    return Ledger(
        rho=mp.nstr(rho, 30),
        K=mp.nstr(K, 30),
        mu=mp.nstr(mu, 30),
        active_slack=mp.nstr(active_slack, 30),
        H=mp.nstr(H, 30),
        tau=mp.nstr(tau, 30),
        b=b,
        Hhat=mp.nstr(Hhat, 30),
        q=q,
        alpha=mp.nstr(alpha, 30),
        R=mp.nstr(R, 30),
        B_mu=mp.nstr(B_mu, 30),
        suffix_inverse=mp.nstr(suffix_inverse, 30),
        suffix_spatial=mp.nstr(suffix_spatial, 30),
        suffix_form_gap=mp.nstr(suffix_inverse - suffix_spatial, 12),
        outer_reserve=mp.nstr(outer_reserve, 30),
        fallback=mp.nstr(outer_reserve + suffix_inverse, 30),
        WT4=mp.nstr(WT4, 30),
        WT4_inverse=mp.nstr(WT4_inverse, 30),
        WT4_form_gap=mp.nstr(WT4 - WT4_inverse, 12),
        min_action_wall_distance=mp.nstr(minimum_wall, 12),
        curvature_zero=mp.nstr(q_one_crossing(K, mu), 30),
        complete_cells=cells,
        top=top,
    )


def active_wall(rho: mp.mpf) -> mp.mpf:
    return mp.sqrt(mp.pi**2 / (1 - rho) ** 2 + mp.mpf(3) / 4)


def stress_records(seed: int, random_records: int) -> dict[str, object]:
    candidates: list[tuple[mp.mpf, mp.mpf, str]] = []
    rho_values = [
        mp.mpf("0.001"),
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("0.75"),
        mp.mpf("0.9"),
        mp.mpf("0.97"),
        mp.mpf("0.99"),
    ]
    for rho in rho_values:
        wall = active_wall(rho)
        for factor in ("1.000001", "1.01", "1.1", "1.5", "2", "4"):
            candidates.append((rho, wall * mp.mpf(factor), "active_factor"))

        # Force H modulo one near the terminal ownership walls.
        min_H = wall * (1 - rho) / mp.pi
        base_q = max(1, int(mp.ceil(min_H)))
        for frac in ("0.000001", "0.249999", "0.250001", "0.749999", "0.750001", "0.999999"):
            H = base_q + mp.mpf(frac)
            K = mp.pi * H / (1 - rho)
            if K > wall:
                candidates.append((rho, K, "terminal_wall"))

        # Force tau near an integer, hence B(mu) near 0 or 1.
        tau_scale = (
            mp.sqrt(1 - rho * rho) - rho * mp.acos(rho)
        ) / mp.pi
        if tau_scale > 0:
            m0 = max(1, int(mp.ceil(wall * tau_scale)))
            for delta in ("-0.000001", "0", "0.000001"):
                K = (m0 + mp.mpf(delta)) / tau_scale
                if K > wall:
                    candidates.append((rho, K, "interface_wall"))

    rng = random.Random(seed)
    for _ in range(random_records):
        rho = mp.mpf(str(10 ** rng.uniform(-3, -0.0005)))
        rho = min(rho, mp.mpf("0.995"))
        factor = mp.mpf(str(math.exp(rng.uniform(math.log(1.000001), math.log(8)))))
        candidates.append((rho, active_wall(rho) * factor, "random"))

    best_suffix: tuple[mp.mpf, Ledger, str] | None = None
    best_fallback: tuple[mp.mpf, Ledger, str] | None = None
    best_wt4: tuple[mp.mpf, Ledger, str] | None = None
    suffix_negative: tuple[Ledger, str] | None = None
    fallback_negative: tuple[Ledger, str] | None = None
    wt4_negative: tuple[Ledger, str] | None = None
    evaluated = 0
    for rho, K, tag in candidates:
        ledger = evaluate(rho, K)
        evaluated += 1
        suffix = mp.mpf(ledger.suffix_inverse)
        fallback = mp.mpf(ledger.fallback)
        wt4 = mp.mpf(ledger.WT4)
        if best_suffix is None or suffix < best_suffix[0]:
            best_suffix = (suffix, ledger, tag)
        if best_fallback is None or fallback < best_fallback[0]:
            best_fallback = (fallback, ledger, tag)
        if best_wt4 is None or wt4 < best_wt4[0]:
            best_wt4 = (wt4, ledger, tag)
        if suffix < 0 and suffix_negative is None:
            suffix_negative = (ledger, tag)
        if fallback < 0 and fallback_negative is None:
            fallback_negative = (ledger, tag)
        if wt4 < 0 and wt4_negative is None:
            wt4_negative = (ledger, tag)

    def packed(record: tuple[mp.mpf, Ledger, str] | None) -> object:
        if record is None:
            return None
        value, ledger, tag = record
        return {"value": mp.nstr(value, 30), "tag": tag, "ledger": asdict(ledger)}

    def negative_packed(record: tuple[Ledger, str] | None) -> object:
        if record is None:
            return None
        ledger, tag = record
        return {"tag": tag, "ledger": asdict(ledger)}

    return {
        "classification": "diagnostic_only",
        "evaluated_records": evaluated,
        "first_suffix_negative": negative_packed(suffix_negative),
        "first_fallback_negative": negative_packed(fallback_negative),
        "first_WT4_negative": negative_packed(wt4_negative),
        "smallest_suffix": packed(best_suffix),
        "smallest_fallback": packed(best_fallback),
        "smallest_WT4": packed(best_wt4),
        "positive_coverage_certificate": False,
    }


def round48_regression() -> dict[str, object]:
    K = mp.mpf(2485744973967441) / 20_000_000
    mu = mp.mpf(1412489996090409) / 10**12
    n = 39_561_154
    left = inverse_action(K, mu, n - 1)
    node = inverse_action(K, mu, mp.mpf(n) - mp.mpf(1) / 4)
    right = inverse_action(K, mu, n)
    supply = (
        shell_moment_primitive(K, mu, left)
        - shell_moment_primitive(K, mu, right)
    ) / 3
    continuous = node * (node + 1) * (2 * node + 1) / 6
    M = strict_bracket(node)
    return {
        "K": mp.nstr(K, 30),
        "mu": mp.nstr(mu, 30),
        "n": n,
        "interface_height": mp.nstr(ball_action(K, mu), 30),
        "continuous_margin": mp.nstr(supply - continuous, 30),
        "discrete_M": M,
        "discrete_QCL_margin": mp.nstr(supply - sum_squares(M), 30),
        "classification": "regression_of_interval_certified_Round48_record",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho", default=None)
    parser.add_argument("--K", default=None)
    parser.add_argument("--seed", type=int, default=4901)
    parser.add_argument("--random-records", type=int, default=40)
    parser.add_argument("--skip-search", action="store_true")
    args = parser.parse_args()

    result: dict[str, object] = {
        "evidence_class": "diagnostic_only",
        "round48_regression": round48_regression(),
        "positive_coverage_certificate": False,
    }
    if args.rho is not None or args.K is not None:
        if args.rho is None or args.K is None:
            raise SystemExit("--rho and --K must be supplied together")
        result["single_record"] = asdict(evaluate(args.rho, args.K))
    if not args.skip_search:
        result["stress_search"] = stress_records(args.seed, args.random_records)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
