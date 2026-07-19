#!/usr/bin/env python3
"""Directed-Arb certificate for the compact active f=1 no-drop wall.

The analytic reduction is recorded in
``human/outbox/general-d-round-09-no-drop-f1-level-wall-reduction.md``.
After the independent small-s theorem, the only remaining normalized data
obey

    0 <= rho <= 99/100,  0 < x < 1,
    a = a_rho(x) >= 7/44000,  a <= x/2,
    3(1-rho)/4 >= pi*a.

If u is the unique root a_rho(u)=4*a/3, the target is

    P1 = 9*j_rho(u)/16 - 3*a*(x-u)/2 - a**2 > 0.

All box enclosures use monotonicity in rho and the level coordinate.  The
pure-ball suffix u>=rho is discharged analytically by the strict one-level
convex reserve and is therefore a terminal prune, not a numerical sign.
"""

from __future__ import annotations

import argparse
import heapq
import itertools
from dataclasses import dataclass
from functools import lru_cache

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this certificate") from exc


RHO_MAX = fmpq(99, 100)
ACTION_MIN = fmpq(7, 44000)
B = fmpq(3, 4)
SERIES_TERMS = 12
ROOT_STEPS = 20
MAX_DEPTH = 80
MAX_BOXES = 2_000_000

PI = arb.pi()


def A(value: int | fmpq) -> arb:
    return arb(value)


def lower(value: arb) -> arb:
    return value.lower()


def upper(value: arb) -> arb:
    return value.upper()


def g_radius_x(radius: arb, x: fmpq) -> arb:
    """G_radius(radius-2*radius*x), by its positive x-series."""

    if x == 0:
        return arb(0)
    if x == fmpq(1, 2):
        return radius / PI
    xx = A(x)
    partial = arb(0)
    power = arb(1)
    coefficient = fmpq(1, 3)
    for m in range(SERIES_TERMS):
        partial += A(coefficient) * power
        power *= xx
        coefficient *= fmpq(
            (2 * m + 1) ** 2,
            2 * (m + 1) * (2 * m + 5),
        )
    first_omitted = A(coefficient) * power
    tail = arb(0).union(upper(first_omitted) / (1 - upper(xx)))
    return 8 * radius * xx * xx.sqrt() * (partial + tail) / PI


@lru_cache(maxsize=100_000)
def g_point(radius: fmpq, z: fmpq) -> arb:
    if z <= 0:
        return A(radius) / PI
    if z >= radius:
        return arb(0)
    gap_x = fmpq(radius - z, 2 * radius)
    if gap_x < fmpq(1, 16):
        return g_radius_x(A(radius), gap_x)
    rr, zz = A(radius), A(z)
    root = ((rr - zz) * (rr + zz)).sqrt()
    theta = (root / zz).atan()
    return (root - zz * theta) / PI


@lru_cache(maxsize=100_000)
def shell_action_point(rho: fmpq, x: fmpq) -> arb:
    """Exact outward enclosure of a_rho(x) at a rational point."""

    outer = g_point(fmpq(1), x)
    inner = g_point(rho, x) if x < rho else arb(0)
    return outer - inner


def j2_radius_x(radius: arb, x: fmpq) -> arb:
    """2*integral G_radius from radius-2*radius*x to radius."""

    if x == 0:
        return arb(0)
    if x == fmpq(1, 2):
        return radius * radius / 4
    xx = A(x)
    partial = arb(0)
    power = arb(1)
    coefficient = fmpq(1, 3)
    for m in range(SERIES_TERMS):
        integrated = coefficient / fmpq(2 * m + 5, 2)
        partial += A(integrated) * power
        power *= xx
        coefficient *= fmpq(
            (2 * m + 1) ** 2,
            2 * (m + 1) * (2 * m + 5),
        )
    integrated = coefficient / fmpq(2 * SERIES_TERMS + 5, 2)
    first_omitted = A(integrated) * power
    tail = arb(0).union(upper(first_omitted) / (1 - upper(xx)))
    return 32 * radius * radius * xx * xx * xx.sqrt() * (partial + tail) / PI


@lru_cache(maxsize=100_000)
def j2_point(radius: fmpq, z: fmpq) -> arb:
    if z <= 0:
        return A(radius) * A(radius) / 4
    if z >= radius:
        return arb(0)
    gap_x = fmpq(radius - z, 2 * radius)
    if gap_x < fmpq(1, 16):
        return j2_radius_x(A(radius), gap_x)
    rr, zz = A(radius), A(z)
    root = ((rr - zz) * (rr + zz)).sqrt()
    theta = (root / zz).atan()
    return ((rr * rr + 2 * zz * zz) * theta - 3 * zz * root) / (2 * PI)


@lru_cache(maxsize=100_000)
def terminal_area_point(rho: fmpq, u: fmpq) -> arb:
    """j_rho(u)=J_1(u)-J_rho(u), at a rational point."""

    if u == 0:
        return (1 - A(rho) * A(rho)) / 4
    outer = j2_point(fmpq(1), u)
    inner = j2_point(rho, u) if u < rho else arb(0)
    return outer - inner


@dataclass(frozen=True)
class Box:
    rho0: fmpq
    rho1: fmpq
    x0: fmpq
    x1: fmpq
    depth: int = 0

    def split(self, coordinate: str) -> tuple["Box", "Box"]:
        if coordinate == "rho":
            mid = (self.rho0 + self.rho1) / 2
            return (
                Box(self.rho0, mid, self.x0, self.x1, self.depth + 1),
                Box(mid, self.rho1, self.x0, self.x1, self.depth + 1),
            )
        if coordinate == "x":
            mid = (self.x0 + self.x1) / 2
            return (
                Box(self.rho0, self.rho1, self.x0, mid, self.depth + 1),
                Box(self.rho0, self.rho1, mid, self.x1, self.depth + 1),
            )
        raise ValueError(coordinate)


def action_bounds(box: Box) -> tuple[arb, arb]:
    """Monotone corner enclosure of a_rho(x)."""

    return (
        lower(shell_action_point(box.rho1, box.x1)),
        upper(shell_action_point(box.rho0, box.x0)),
    )


def root_u_bounds(
    box: Box,
    action_lo: arb,
    action_hi: arb,
) -> tuple[fmpq, fmpq] | None:
    """Common enclosure of active roots a_rho(u)=4*a_rho(x)/3."""

    target_lo = action_lo / A(B)
    target_hi = action_hi / A(B)
    # Every relevant root lies below x.  If dependency in the current
    # outer box does not yet prove that common fence, split the outer box.
    if not (upper(shell_action_point(box.rho0, box.x1)) < target_lo):
        return None

    # Find the largest common lower fence.  Failure of the one-sided
    # comparison merely moves the search endpoint; it must not terminate
    # the bisection, since the midpoint can lie inside the thin root tube.
    lo_u, hi_search = fmpq(0), box.x1
    for _ in range(ROOT_STEPS):
        mid = (lo_u + hi_search) / 2
        value_lo = lower(shell_action_point(box.rho1, mid))
        if value_lo > target_hi:
            lo_u = mid
        else:
            hi_search = mid

    # Independently find the smallest common upper fence.
    lo_search, hi_u = fmpq(0), box.x1
    for _ in range(ROOT_STEPS):
        mid = (lo_search + hi_u) / 2
        value_hi = upper(shell_action_point(box.rho0, mid))
        if value_hi < target_lo:
            hi_u = mid
        else:
            lo_search = mid
    return lo_u, hi_u


def assess(box: Box) -> tuple[str, float]:
    action_lo, action_hi = action_bounds(box)

    if action_hi < A(ACTION_MIN):
        return "small-action", 1.0
    # The no-drop row has y>=q>=3/2, hence a<=x/2.
    if action_lo > A(box.x1) / 2:
        return "no-drop", 1.0
    # Active width A(0)>=1 is 3(1-rho)/4 >= pi*a.
    if upper(A(B) * A(1 - box.rho0) - PI * action_lo) < 0:
        return "inactive", 1.0

    root = root_u_bounds(box, action_lo, action_hi)
    if root is None:
        return "root", -1.0
    u_lo, u_hi = root

    # If every possible root lies beyond the inner interface, the suffix
    # is a pure ball.  The one-level exact-angle reserve is then strictly
    # positive because theta_{3/4}<pi/2.
    if u_lo >= box.rho1:
        return "pure-ball", 1.0

    # j_rho(u) decreases in both variables, so its lower corner is exact.
    area_lo = lower(terminal_area_point(box.rho1, u_hi))
    distance_hi = A(box.x1 - u_lo)
    scalar = (
        A(B * B) * area_lo
        - 2 * A(B) * action_hi * distance_hi
        - action_hi * action_hi
    )
    margin = float(lower(scalar))
    if margin > 0:
        return "positive", margin
    return "scalar", margin


def verify(rho_panels: int, x_panels: int) -> None:
    terminal = {"small-action", "no-drop", "inactive", "pure-ball", "positive"}
    counter = itertools.count()
    heap: list[tuple[float, int, Box]] = []
    for i in range(rho_panels):
        rho0 = RHO_MAX * i / rho_panels
        rho1 = RHO_MAX * (i + 1) / rho_panels
        for j in range(x_panels):
            x0 = fmpq(j, x_panels)
            x1 = fmpq(j + 1, x_panels)
            heapq.heappush(heap, (0.0, next(counter), Box(rho0, rho1, x0, x1)))

    processed = positive = pruned = max_depth = 0
    smallest = float("inf")
    counts: dict[str, int] = {}
    while heap:
        _, _, box = heapq.heappop(heap)
        processed += 1
        max_depth = max(max_depth, box.depth)
        if processed > MAX_BOXES:
            raise AssertionError("box cap exceeded")
        status, margin = assess(box)
        counts[status] = counts.get(status, 0) + 1
        if processed % 10_000 == 0:
            print(
                f"progress: boxes={processed}; queued={len(heap)}; "
                f"depth={max_depth}; statuses={counts}",
                flush=True,
            )
        if status in terminal:
            if status == "positive":
                positive += 1
                smallest = min(smallest, margin)
            else:
                pruned += 1
            continue
        if box.depth >= MAX_DEPTH:
            raise AssertionError(
                f"unresolved depth {box.depth}: {box}; status={status}; margin={margin}"
            )
        rho_width = float(A(box.rho1 - box.rho0)) / float(A(RHO_MAX))
        x_width = float(A(box.x1 - box.x0))
        # A failed common root fence can be caused by dependency in either
        # outer coordinate.  Always split the wider normalized coordinate;
        # repeatedly forcing x leaves a wide rho tube and does not improve
        # that comparison.
        coordinate = "x" if x_width >= rho_width else "rho"
        left, right = box.split(coordinate)
        heapq.heappush(heap, (margin, next(counter), left))
        heapq.heappush(heap, (margin, next(counter), right))

    print("PASS: compact active f=1 no-drop level wall certified")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print(f"initial panels: rho={rho_panels}; x={x_panels}")
    print(
        f"processed boxes: {processed}; positive leaves: {positive}; "
        f"pruned leaves: {pruned}; max depth: {max_depth}"
    )
    print(f"smallest accepted P1 lower endpoint (diagnostic): {smallest}")
    print("status counts: " + ", ".join(f"{k}={counts[k]}" for k in sorted(counts)))


def main() -> None:
    global PI
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=384)
    parser.add_argument("--rho-panels", type=int, default=16)
    parser.add_argument("--x-panels", type=int, default=24)
    args = parser.parse_args()
    if args.precision < 256:
        raise SystemExit("precision must be at least 256 bits")
    if args.rho_panels < 1 or args.x_panels < 1:
        raise SystemExit("panel counts must be positive")
    ctx.prec = args.precision
    PI = arb.pi()
    verify(args.rho_panels, args.x_panels)


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError, ZeroDivisionError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=__import__("sys").stderr)
        raise SystemExit(1) from exc
