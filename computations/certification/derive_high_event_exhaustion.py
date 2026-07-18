#!/usr/bin/env python3
"""Derive exact table data for the printed high-staircase event exhaustion.

This utility is a development/replay aid, not a premise of the analytic
proof.  All event locations and order comparisons are performed with
``fractions.Fraction``.  Floating point is used only to choose convenient
rational witnesses; every emitted witness is then checked exactly.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from math import ceil, floor, sqrt


PI_LO = Q(333, 106)
WEYL_COEFF_LO = Q(7, 99)
X_LO = Q(13)
X_HI = Q(205)


@dataclass(frozen=True, order=True)
class Mode:
    ell: int
    radial: int
    beta_sq: Q

    @property
    def slope(self) -> Q:
        return Q(self.radial * self.radial)

    @property
    def intercept(self) -> Q:
        return Q(self.ell * (self.ell + 1))

    @property
    def weight(self) -> int:
        return 2 * self.ell + 1

    def moving(self, x: Q) -> Q:
        return self.slope * x + self.intercept

    def event(self, x: Q) -> Q:
        return max(self.moving(x), self.beta_sq)

    def branch(self, x: Q) -> str:
        return "M" if self.moving(x) >= self.beta_sq else "F"


FIRST = (
    Q(0),
    Q(4) ** 2,
    Q(51, 10) ** 2,
    Q(13, 2) ** 2,
    Q(15, 2) ** 2,
    Q(87, 10) ** 2,
    Q(10) ** 2,
    Q(23, 2) ** 2,
    Q(71, 6) ** 2,
    Q(64, 5) ** 2,
    Q(69, 5) ** 2,
)
SECOND = (
    Q(0),
    Q(77, 10) ** 2,
    Q(9) ** 2,
    Q(103, 10) ** 2,
    Q(11409, 100),
)
THIRD = (Q(0), Q(21, 2) ** 2)

MODES = tuple(
    [Mode(ell, 1, beta) for ell, beta in enumerate(FIRST)]
    + [Mode(ell, 2, beta) for ell, beta in enumerate(SECOND)]
    + [Mode(ell, 3, beta) for ell, beta in enumerate(THIRD)]
)


@dataclass(frozen=True)
class FineRow:
    mode: Mode
    lo: Q
    hi: Q
    branch: str
    band: int
    cap: int


@dataclass(frozen=True)
class Row:
    mode: Mode
    lo: Q
    hi: Q
    branch: str
    band: int
    cap: int
    x_star: Q
    rho_upper: Q
    k_lower: Q
    reserve: Q


def root(a1: Q, d1: Q, a2: Q, d2: Q) -> Q | None:
    if a1 == a2:
        return None
    return (d2 - d1) / (a1 - a2)


def critical_points() -> list[Q]:
    points = {X_LO, X_HI}
    components: dict[Mode, tuple[tuple[Q, Q], ...]] = {
        mode: ((mode.slope, mode.intercept), (Q(0), mode.beta_sq))
        for mode in MODES
    }
    for mode in MODES:
        value = root(mode.slope, mode.intercept, Q(0), mode.beta_sq)
        if value is not None and X_LO < value < X_HI:
            points.add(value)
        for m in range(6, 12):
            boundary = (Q(1), Q(m * (m + 1)))
            for component in components[mode]:
                value = root(*component, *boundary)
                if value is not None and X_LO < value < X_HI:
                    points.add(value)
    for left, right in combinations(MODES, 2):
        for c_left in components[left]:
            for c_right in components[right]:
                value = root(*c_left, *c_right)
                if value is not None and X_LO < value < X_HI:
                    points.add(value)
    return sorted(points)


def following_band(event: Q, x: Q) -> int | None:
    for upper in range(7, 12):
        lower_sq = x + (upper - 1) * upper
        upper_sq = x + upper * (upper + 1)
        if lower_sq <= event < upper_sq:
            return upper
    if event == x + 132:
        return 11
    return None


def post_cap(mode: Mode, x: Q) -> int:
    event = mode.event(x)
    return sum(other.weight for other in MODES if other.event(x) <= event)


def fine_rows() -> list[FineRow]:
    points = critical_points()
    rows: list[FineRow] = []
    for lo, hi in zip(points, points[1:]):
        mid = (lo + hi) / 2
        for mode in MODES:
            event = mode.event(mid)
            band = following_band(event, mid)
            if band is None:
                continue
            rows.append(
                FineRow(mode, lo, hi, mode.branch(mid), band, post_cap(mode, mid))
            )
    return rows


def closure_cap(mode: Mode, lo: Q, hi: Q, interior_cap: int) -> int:
    return max(interior_cap, post_cap(mode, lo), post_cap(mode, hi))


def rational_witnesses(x_star: Q, event_sq: Q, cap: int) -> tuple[Q, Q, Q]:
    # Start with three decimal places, then refine until the exact reserve passes.
    for denominator in (1000, 10000, 100000):
        # Use the proved lower bound for pi, not a decimal approximation to pi,
        # so that the subsequently squared location witness is guaranteed to pass.
        rho_approx = 1.0 - float(PI_LO) / sqrt(float(x_star))
        rho_upper = Q(ceil(rho_approx * denominator), denominator)
        k_approx = sqrt(float(event_sq))
        k_lower = Q(floor(k_approx * denominator), denominator)
        if k_lower * k_lower >= event_sq:
            k_lower -= Q(1, denominator)
        if not (PI_LO * PI_LO > (1 - rho_upper) ** 2 * x_star):
            continue
        if not (k_lower * k_lower < event_sq):
            continue
        reserve = WEYL_COEFF_LO * (1 - rho_upper**3) * k_lower**3 - cap
        if reserve > 0:
            return rho_upper, k_lower, reserve
    raise RuntimeError(
        f"no rational payment witness for x={x_star}, event={event_sq}, cap={cap}"
    )


def merge_rows() -> list[Row]:
    fine = fine_rows()
    by_mode: dict[Mode, list[FineRow]] = {mode: [] for mode in MODES}
    for item in fine:
        by_mode[item.mode].append(item)

    emitted: list[Row] = []
    for mode in MODES:
        pieces = by_mode[mode]
        index = 0
        while index < len(pieces):
            first = pieces[index]
            lo = first.lo
            hi = first.hi
            branch = first.branch
            band = first.band
            cap = closure_cap(mode, lo, hi, first.cap)
            last_good = (index, hi, cap)

            cursor = index + 1
            while cursor < len(pieces):
                nxt = pieces[cursor]
                if nxt.lo != hi or nxt.branch != branch or nxt.band != band:
                    break
                trial_hi = nxt.hi
                trial_cap = max(cap, closure_cap(mode, nxt.lo, trial_hi, nxt.cap))
                x_star = lo if branch == "M" else trial_hi
                try:
                    rational_witnesses(x_star, mode.event(x_star), trial_cap)
                except RuntimeError:
                    break
                hi, cap = trial_hi, trial_cap
                last_good = (cursor, hi, cap)
                cursor += 1

            end_index, hi, cap = last_good
            x_star = lo if branch == "M" else hi
            event_sq = mode.event(x_star)
            rho_upper, k_lower, reserve = rational_witnesses(x_star, event_sq, cap)
            emitted.append(
                Row(
                    mode,
                    lo,
                    hi,
                    branch,
                    band,
                    cap,
                    x_star,
                    rho_upper,
                    k_lower,
                    reserve,
                )
            )
            index = end_index + 1
    return emitted


def qtext(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    rows = merge_rows()
    print(f"critical_points={len(critical_points())}")
    print(f"fine_rows={len(fine_rows())}")
    print(f"merged_rows={len(rows)}")
    print("mode | x-cell | br | band | cap | x* | r | t | reserve")
    for row in rows:
        print(
            f"({row.mode.ell},{row.mode.radial}) | "
            f"[{qtext(row.lo)},{qtext(row.hi)}] | {row.branch} | "
            f"B{row.band} | {row.cap} | {qtext(row.x_star)} | "
            f"{qtext(row.rho_upper)} | {qtext(row.k_lower)} | {qtext(row.reserve)}"
        )


if __name__ == "__main__":
    main()
