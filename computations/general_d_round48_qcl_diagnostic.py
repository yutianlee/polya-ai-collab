#!/usr/bin/env python3
"""Round 48 diagnostic falsifier for the direct-layer quarter-cell lemma.

This script is diagnostic only.  It locates scalar action walls

    A_{rho,K}(m) = n - 1/4

and evaluates the continuous right-wall limit of

    L_n = integral_{n-1}^n r(t)^3/3 dt - sum_{1 <= a < r(n-1/4)} a^2.

At the wall itself the strict count excludes m.  Immediately to its right it
includes m, so the dangerous limiting value subtracts S_2(m).  Decimal
positivity is not a continuum proof and decimal negativity is not an exact or
directed counterexample.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import mpmath as mp

from general_d_round47_d4_weighted_diagnostic import active_wall, shell_action


mp.mp.dps = 80


def sum_squares(m: int) -> int:
    return m * (m + 1) * (2 * m + 1) // 6


def inverse_action(rho: mp.mpf, K: mp.mpf, level: mp.mpf) -> mp.mpf:
    """Return r(level), with the natural zero/K endpoint extensions."""
    top = shell_action(rho, K, mp.mpf(0))
    if level <= 0:
        return K
    if level >= top:
        return mp.mpf(0)
    lo = mp.mpf(0)
    hi = K
    for _ in range(280):
        mid = (lo + hi) / 2
        if shell_action(rho, K, mid) > level:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def layer_supply(rho: mp.mpf, K: mp.mpf, n: int) -> mp.mpf:
    """Compute integral_{n-1}^n r(t)^3/3 dt by spatial layer cake."""
    low = mp.mpf(n - 1)
    high = mp.mpf(n)
    x_high = inverse_action(rho, K, high)
    x_low = inverse_action(rho, K, low)
    total = x_high**3 / 3
    if x_low <= x_high:
        return total
    mu = rho * K
    breaks = [x_high]
    if x_high < mu < x_low:
        breaks.append(mu)
    breaks.append(x_low)
    total += mp.fsum(
        mp.quad(lambda z: z * z * (shell_action(rho, K, z) - low), [a, b])
        for a, b in zip(breaks[:-1], breaks[1:])
    )
    return total


def wall_root(rho: mp.mpf, n: int, m: int) -> mp.mpf | None:
    target = mp.mpf(n) - mp.mpf(1) / 4
    lo = max(mp.mpf(m), active_wall(rho))
    if shell_action(rho, lo, mp.mpf(m)) >= target:
        return None
    hi = max(lo + 1, 2 * lo)
    while shell_action(rho, hi, mp.mpf(m)) <= target:
        hi *= 2
        if hi > mp.mpf("1e7"):
            return None
    for _ in range(260):
        mid = (lo + hi) / 2
        if shell_action(rho, mid, mp.mpf(m)) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


@dataclass
class Record:
    rho: mp.mpf
    n: int
    m: int
    K: mp.mpf
    margin: mp.mpf

    def to_json(self) -> dict[str, object]:
        return {
            "rho": mp.nstr(self.rho, 18),
            "n": self.n,
            "m": self.m,
            "K_wall": mp.nstr(self.K, 24),
            "right_wall_QCL_margin": mp.nstr(self.margin, 24),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--max-m", type=int, default=80)
    args = parser.parse_args()
    rho_values = [
        mp.mpf("0.0001"),
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("0.75"),
        mp.mpf("0.9"),
        mp.mpf("0.97"),
        mp.mpf("0.99"),
        mp.mpf("0.999"),
    ]
    best: Record | None = None
    evaluated = 0
    negative: Record | None = None
    for rho in rho_values:
        for n in range(1, args.max_n + 1):
            for m in range(1, args.max_m + 1):
                K = wall_root(rho, n, m)
                if K is None:
                    continue
                margin = layer_supply(rho, K, n) - sum_squares(m)
                record = Record(rho, n, m, K, margin)
                evaluated += 1
                if best is None or margin < best.margin:
                    best = record
                if margin < 0:
                    negative = record
                    break
            if negative is not None:
                break
        if negative is not None:
            break
    print(
        json.dumps(
            {
                "classification": "diagnostic_only",
                "evaluated_action_walls": evaluated,
                "negative_QCL_wall_found": negative is not None,
                "first_negative": negative.to_json() if negative else None,
                "smallest_record": best.to_json() if best else None,
                "positive_coverage_certificate": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
