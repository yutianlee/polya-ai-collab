#!/usr/bin/env python3
"""Round 28 branchwise diagnostic for conditional Cmax8 on the hard sector.

This is a falsification/theorem-design program, not a certificate.  It uses
the frozen Round 27 exact-domain evaluator and retains its parity, shelf,
activity, strict-floor, cap, and terminal conventions.  For each retained
tuple it restricts the phase angle to

    p > d*m,  E < E_* = 1/2-d*m/(2*p),

then records separately the curvature-owned and elasticity-owned cells of

    L0 = max(L_elastic, L_curvature).

For each sampled alpha, the deterministic pass brackets t on a 25-point
mesh and applies bounded local minimization near the best sampled cell.  It
does not certify a global minimum.  The seeded mixed-scale pass is
deliberately adversarial but only samples t.  Positive minima printed here
have no theorem status.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass

from scipy.optimize import brentq, minimize_scalar

import general_d_round27_exact_phi_hard_sector_diagnostic as core


PI = math.pi


@dataclass(frozen=True)
class BranchRecord:
    owner: str
    cmax8: float
    terminal_only: float
    r: float
    p: int
    m: int
    f: int
    alpha: float
    t: float
    epsilon_sum: float
    threshold: float
    elastic: float
    curvature: float
    B0: int
    lam: float


def branch_record(
    r: float, p: int, m: int, f: int, alpha: float, t: float
) -> BranchRecord:
    rec = core.evaluate(r, p, m, f, alpha, t)
    mu = r + p + m + alpha
    X = m + alpha
    d = 1 - 2 * t / PI
    a_p = p * p / (3 * (2 * r + p))
    W = mu / PI * (math.tan(t) - t)
    lam = f - 0.25 - W
    B0 = core.strict_floor(W + 0.25)
    stretch = math.sqrt(
        1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p))
    )
    elastic = (stretch - 1) * lam
    curvature = (
        (1 - math.cos(t)) / (PI * mu) * p * (2 * r + p) / 2
    )
    owner = "elasticity" if elastic >= curvature else "curvature"
    E_star = 0.5 - d * m / (2 * p)
    terminal_only = B0 * (PI / (2 * t) - 1) - p * E_star - 0.125

    # Independent reconstruction of the branchwise maximum scalar.
    top = core.top_payment(lam)
    rebuilt = (
        (p + a_p) * max(elastic, curvature)
        - p * E_star
        + B0 * (PI / (2 * t) - 1)
        + top
        - 0.125
    )
    if abs(rebuilt - rec.Cmax8) > 2.0e-8 * max(1.0, abs(rebuilt)):
        raise ArithmeticError("branchwise Cmax8 reconstruction failed")

    return BranchRecord(
        owner,
        rec.Cmax8,
        terminal_only,
        r,
        p,
        m,
        f,
        alpha,
        t,
        rec.epsilon_sum,
        rec.automatic_threshold,
        elastic,
        curvature,
        B0,
        lam,
    )


def hard_interval(
    r: float, p: int, m: int, f: int, alpha: float
) -> tuple[float, float] | None:
    feasible = core.feasible_interval(r, p, m, f, alpha)
    if feasible is None:
        return None
    lo, hi, _, _ = feasible
    d_lo = 1 - 2 * lo / PI

    # If p <= d*m at the left endpoint, the seam p=d*m already has E_*=0;
    # the strictly increasing hard gap cannot enter the hard sector later.
    if p <= d_lo * m or core.hard_gap(r, p, m, f, alpha, lo) >= 0:
        return None

    hard_hi = hi
    if core.hard_gap(r, p, m, f, alpha, hi) >= 0:
        hard_hi = brentq(
            lambda value: core.hard_gap(r, p, m, f, alpha, value),
            lo,
            hi,
            xtol=2.0e-14,
            rtol=2.0e-14,
        )
    return (lo, hard_hi) if lo < hard_hi else None


def minimize_t(
    r: float, p: int, m: int, f: int, alpha: float
) -> BranchRecord | None:
    interval = hard_interval(r, p, m, f, alpha)
    if interval is None:
        return None
    lo, hi = interval
    # Keep away from an excluded right wall while retaining its one-sided
    # diagnostic value.  Literal included walls are also evaluated below.
    right = math.nextafter(hi, lo)
    points = [lo + (right - lo) * j / 24 for j in range(25)]

    def objective(value: float) -> float:
        try:
            return branch_record(r, p, m, f, alpha, value).cmax8
        except (ValueError, ArithmeticError):
            return 1.0e100

    values = [objective(value) for value in points]
    candidates = [points[min(range(len(values)), key=values.__getitem__)], lo, right]
    best_index = min(range(len(values)), key=values.__getitem__)
    for index in range(max(0, best_index - 2), min(24, best_index + 2)):
        result = minimize_scalar(
            objective,
            bounds=(points[index], points[index + 1]),
            method="bounded",
            options={"xatol": 2.0e-13},
        )
        candidates.append(float(result.x))

    records = []
    for value in candidates:
        try:
            records.append(branch_record(r, p, m, f, alpha, value))
        except (ValueError, ArithmeticError):
            pass
    return min(records, key=lambda item: item.cmax8) if records else None


def deterministic_scan(limit: int) -> list[BranchRecord]:
    records: list[BranchRecord] = []
    alphas = (0.0, 0.1, 0.5, 0.9, 0.99, 0.9999, 0.999999999)
    for half in (False, True):
        for index in range(1, limit + 1):
            r = float(index) + (0.5 if half else 0.0)
            for p in range(1, limit + 5):
                for m in range(1, limit + 1):
                    for f in range(2, min(6, limit + 2)):
                        for alpha in alphas:
                            record = minimize_t(r, p, m, f, alpha)
                            if record is not None:
                                records.append(record)
    return records


def random_scan(count: int, seed: int) -> list[BranchRecord]:
    rng = random.Random(seed)
    records: list[BranchRecord] = []
    floors = (2, 3, 4, 6, 8, 12, 20, 32)
    for _ in range(count):
        half = rng.random() < 0.5
        r = float(max(1, int(10 ** rng.uniform(0, 7)))) + (0.5 if half else 0.0)
        p = max(1, int(10 ** rng.uniform(0, 4)))
        m = max(1, int(10 ** rng.uniform(0, 3)))
        f = rng.choice(floors)
        alpha = rng.random()
        interval = hard_interval(r, p, m, f, alpha)
        if interval is None:
            continue
        lo, hi = interval
        for fraction in (0.0, rng.random(), 0.999999):
            value = lo + (hi - lo) * fraction
            try:
                records.append(branch_record(r, p, m, f, alpha, value))
            except (ValueError, ArithmeticError):
                pass
    return records


def limiting_edge() -> BranchRecord:
    # The observed hard family has r=1,p=3,m=2,f=2 and alpha -> 1-.  At
    # alpha=1 its limiting interface radius is mu=7, and the lower shelf
    # wall is A_t(4)=7/4.
    # Stay farther than the Round 27 diagnostic's 5e-10 wall tolerance from
    # the excluded alpha=1 face.
    r, p, m, f, alpha = 1.0, 3, 2, 2, 1.0 - 1.0e-7
    mu = r + p + m + alpha
    wall = brentq(
        lambda value: core.shell_action(mu, value, r + p) - 1.75,
        1.0e-7,
        PI / 2 - 1.0e-7,
        xtol=2.0e-14,
        rtol=2.0e-14,
    )
    return branch_record(r, p, m, f, alpha, wall)


def elasticity_regression() -> BranchRecord:
    """Fixed near-switch elasticity record found by the broad audit scan."""

    r, p, m, f, alpha = 50.0, 3, 1, 2, 0.75
    interval = hard_interval(r, p, m, f, alpha)
    if interval is None:
        raise RuntimeError("fixed elasticity regression left the hard sector")
    return branch_record(r, p, m, f, alpha, interval[0])


def show(label: str, record: BranchRecord) -> None:
    print(
        f"{label}: value={record.cmax8:.15g} owner={record.owner} "
        f"terminalOnly={record.terminal_only:.15g} "
        f"tuple=(r={record.r},p={record.p},m={record.m},f={record.f},"
        f"alpha={record.alpha:.12g},t={record.t:.15g}) "
        f"E={record.epsilon_sum:.15g} E*={record.threshold:.15g} "
        f"B0={record.B0} lambda={record.lam:.15g} "
        f"Lel={record.elastic:.15g} Lcurv={record.curvature:.15g}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--random", type=int, default=30000)
    parser.add_argument("--seed", type=int, default=20260728)
    args = parser.parse_args()

    edge = limiting_edge()
    show("limitingHardEdge", edge)

    fixed_elastic = elasticity_regression()
    show("fixedElasticityRegression", fixed_elastic)

    records = deterministic_scan(args.limit)
    records.append(fixed_elastic)
    records.extend(random_scan(args.random, args.seed))
    if not records:
        raise RuntimeError("no hard-sector records were retained")

    print(f"retainedHardRecords={len(records)}")
    for owner in ("curvature", "elasticity"):
        owned = [item for item in records if item.owner == owner]
        print(f"{owner}Records={len(owned)}")
        if owned:
            show(f"minimum{owner.title()}Cmax8", min(owned, key=lambda item: item.cmax8))
            show(
                f"minimum{owner.title()}TerminalOnly",
                min(owned, key=lambda item: item.terminal_only),
            )

    print(f"negativeCmax8Records={sum(item.cmax8 < 0 for item in records)}")
    elastic = [item for item in records if item.owner == "elasticity"]
    print(
        "negativeElasticTerminalOnlyRecords="
        f"{sum(item.terminal_only < 0 for item in elastic)}"
    )
    print("diagnosticOnly=True")


if __name__ == "__main__":
    main()
