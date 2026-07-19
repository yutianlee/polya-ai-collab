#!/usr/bin/env python3
"""Non-rigorous diagnostics for the Round 23 C8 scalar.

The script minimizes C8 on the exact fixed-alpha feasible interval, split at
every terminal-action and top-payment wall.  It is a falsification and theorem-
design aid only; ordinary double precision is not a proof certificate.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

from scipy.optimize import brentq, minimize_scalar


PI = math.pi


def g(radius: float, z: float) -> float:
    if z >= radius:
        return 0.0
    theta = math.acos(z / radius)
    return radius * (math.sin(theta) - theta * math.cos(theta)) / PI


def shell_action(mu: float, t: float, z: float) -> float:
    return g(mu / math.cos(t), z) - g(mu, z)


def interface_action(mu: float, t: float) -> float:
    return mu * (math.tan(t) - t) / PI


def strict_bracket(y: float) -> int:
    nearest = round(y)
    if abs(y - nearest) <= 2.0e-12 * max(1.0, abs(y)):
        return int(nearest) - 1
    return math.floor(y)


def top_payment(lam: float) -> float:
    if not (0.0 < lam < 1.0):
        return 0.0
    return min(1.0, 2.0 * max(0.0, 0.75 - lam) ** 2)


def c8(r: float, p: int, m: int, f: int, alpha: float, t: float) -> float:
    mu = r + p + m + alpha
    w = interface_action(mu, t)
    b0 = strict_bracket(w + 0.25)
    return (
        p * p * (3.0 * r + 2.0 * p) * (1.0 - math.cos(t)) / (3.0 * PI * mu)
        - p / 2.0
        + m * (1.0 - 2.0 * t / PI) / 2.0
        + b0 * (PI / (2.0 * t) - 1.0)
        + top_payment(f - 0.25 - w)
        - 0.125
    )


def monotone_root(fun, level: float) -> float:
    lo = 1.0e-12
    hi = PI / 2.0 - 1.0e-10
    return brentq(lambda t: fun(t) - level, lo, hi, xtol=2.0e-14, rtol=2.0e-14)


def activity_root(mu: float, gamma: float) -> float:
    def gap(t: float) -> float:
        return mu * mu / math.cos(t) ** 2 - PI * PI / (1.0 - math.cos(t)) ** 2 - gamma

    # The claimed activity monotonicity applies on the relevant crossing.
    grid = [1.0e-6 + j * (PI / 2.0 - 2.0e-6) / 2000 for j in range(2001)]
    old_t = grid[0]
    old = gap(old_t)
    for t in grid[1:]:
        new = gap(t)
        if old <= 0.0 < new:
            return brentq(gap, old_t, t, xtol=2.0e-14, rtol=2.0e-14)
        old_t, old = t, new
    raise ValueError("no activity crossing")


@dataclass(frozen=True)
class Record:
    value: float
    r: float
    p: int
    m: int
    f: int
    alpha: float
    t: float
    lower_wall: float
    boundary: str
    b0: int
    lam: float


def minimize_tuple(r: float, p: int, m: int, f: int, alpha: float) -> Record | None:
    mu = r + p + m + alpha
    x = r + p
    h = f - 0.25
    at = lambda z: lambda t: shell_action(mu, t, z)
    lower_wall = monotone_root(at(x), h)
    upper_drop = monotone_root(at(x + 1.0), h)
    upper_start = monotone_root(at(r), h + 1.0)
    gamma = 0.75 if float(r).is_integer() else 2.0
    try:
        lower_activity = activity_root(mu, gamma)
    except ValueError:
        return None
    lo = max(lower_wall, lower_activity)
    hi = min(upper_drop, upper_start)
    if not lo < hi:
        return None

    wlo = interface_action(mu, lo)
    whi = interface_action(mu, hi)
    walls: list[tuple[float, str]] = [(lo, "left"), (hi, "right-limit")]
    # W+1/4 integer walls.
    for k in range(math.floor(wlo + 0.25) - 1, math.ceil(whi + 0.25) + 2):
        target = k - 0.25
        if wlo < target < whi:
            walls.append((monotone_root(lambda t: interface_action(mu, t), target), "action"))
    # lambda walls, including the literal lambda -> 0+ boundary.
    for lam, name in [
        (1.0, "lambda=1"),
        (0.75, "lambda=3/4"),
        (0.75 - 1.0 / math.sqrt(2.0), "saturation"),
        (0.0, "lambda=0+"),
    ]:
        target = h - lam
        if wlo < target < whi:
            walls.append((monotone_root(lambda t: interface_action(mu, t), target), name))
    walls.sort()

    candidates: list[tuple[float, str]] = []
    for t, name in walls:
        # Evaluate action walls literally from the left, and strict upper walls
        # as one-sided limits.  A visible offset avoids losing the lambda -> 0+
        # payment to cancellation in W(t).
        side_t = t - 1.0e-10 if name in {"action", "right-limit", "lambda=0+"} else t
        candidates.append((side_t, name))
    for (a, _), (b, _) in zip(walls, walls[1:]):
        aa = math.nextafter(a, math.inf)
        bb = math.nextafter(b, -math.inf)
        if aa >= bb:
            continue
        opt = minimize_scalar(lambda t: c8(r, p, m, f, alpha, t), bounds=(aa, bb), method="bounded", options={"xatol": 2.0e-13})
        candidates.append((opt.x, "stationary-or-cell-end"))

    t, name = min(candidates, key=lambda item: c8(r, p, m, f, alpha, item[0]))
    w = interface_action(mu, t)
    return Record(c8(r, p, m, f, alpha, t), r, p, m, f, alpha, t, lower_wall, name, strict_bracket(w + 0.25), h - w)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--floors", type=int, default=6)
    args = parser.parse_args()
    alphas = [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999999]
    records: list[Record] = []
    for half in (False, True):
        for ri in range(1, args.limit + 1):
            r = float(ri) if not half else ri + 0.5
            if half and r < 1.5:
                continue
            for p in range(1, args.limit + 1):
                for m in range(1, args.limit + 1):
                    for f in range(2, args.floors + 1):
                        for alpha in alphas:
                            rec = minimize_tuple(r, p, m, f, alpha)
                            if rec is not None:
                                records.append(rec)
    records.sort(key=lambda rec: rec.value)
    print(f"retained={len(records)}")
    for name in sorted({rec.boundary for rec in records}):
        subset = [rec for rec in records if rec.boundary == name]
        print(f"boundary={name!r} count={len(subset)} minimum={min(subset, key=lambda rec: rec.value)}")
    for floor in sorted({rec.f for rec in records}):
        subset = [rec for rec in records if rec.f == floor]
        print(f"floor={floor} count={len(subset)} minimum={min(subset, key=lambda rec: rec.value)}")
    print("alpha-direction witness (C8 rises):")
    print(minimize_tuple(1.0, 1, 4, 2, 0.5))
    print(minimize_tuple(1.0, 1, 4, 2, 0.9))
    print("alpha-direction witness (C8 falls):")
    print(minimize_tuple(1.0, 3, 2, 2, 0.5))
    print(minimize_tuple(1.0, 3, 2, 2, 0.9))
    stationary_witness = minimize_tuple(1.0, 5, 5, 2, 0.999999)
    print("direct lower-wall dominance witness:")
    print(stationary_witness)
    if stationary_witness is not None:
        print(
            "lower-wall value=",
            c8(
                stationary_witness.r,
                stationary_witness.p,
                stationary_witness.m,
                stationary_witness.f,
                stationary_witness.alpha,
                stationary_witness.lower_wall,
            ),
        )
    for rec in records[:30]:
        print(rec)


if __name__ == "__main__":
    main()
