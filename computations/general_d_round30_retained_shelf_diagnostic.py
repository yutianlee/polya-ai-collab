#!/usr/bin/env python3
"""Diagnostic scan for the Round 30 retained-E lower-shelf scalar.

The proved reduction is analytic.  This program samples its remaining
discrete scalar on a finite relaxed domain and replays the seven observed
alpha=0 small-phase patterns.  It has no infinite-q coverage and is not a
certificate for high-floor CST.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq


PI = math.pi


def action(radius: float, z: float | np.ndarray) -> float | np.ndarray:
    values = np.asarray(z, dtype=float)
    theta = np.arccos(values / radius)
    result = radius / PI * (np.sin(theta) - theta * np.cos(theta))
    return float(result) if np.ndim(z) == 0 else result


def integral(radius: float, z: float) -> float:
    theta = math.acos(z / radius)
    cosine, sine = math.cos(theta), math.sin(theta)
    return radius**2 / (4 * PI) * (
        theta * (1 + 2 * cosine**2) - 3 * sine * cosine
    )


def inverse_angle(q: float, displacement: int) -> float:
    level = 3 * PI / (4 * (q + displacement))
    return brentq(
        lambda theta: math.tan(theta) - theta - level,
        1.0e-12,
        1.4,
        xtol=2.0e-14,
        rtol=2.0e-14,
    )


@dataclass(frozen=True)
class BandData:
    theta2: float
    k2: float
    k3: float
    terminal: float
    dmin: float


def band_data(q: float) -> BandData:
    theta2 = inverse_angle(q, 2)
    theta3 = inverse_angle(q, 3)
    k2 = (q + 2) / math.cos(theta2)
    k3 = (q + 3) / math.cos(theta3)
    beta2 = math.acos(q / k2) / PI
    jmax = 2 * integral(q + 1, q)
    top_lower = max(0.0, 2 * theta2 / PI - 0.25) ** 2 / beta2
    terminal = PI / (2 * theta2) - 1 - jmax + top_lower
    dmin = 1 - 2 * math.acos(q / k3) / PI
    return BandData(theta2, k2, k3, terminal, dmin)


def fixture_value(q: float, r: float, p: int, m: int) -> float:
    data = band_data(q)
    x = q - m
    emin = (
        action(data.k2, r)
        - action(data.k2, x)
        - action(q + 1, r)
        + action(q + 1, x)
    )
    k4 = (
        ((q + 1) ** -1 - data.k2**-1) * (x**2 - r**2) / (2 * PI)
        + ((q + 1) ** -3 - data.k2**-3) * (x**4 - r**4) / (24 * PI)
    )
    a_p = p**2 / (3 * (2 * r + p))
    return data.terminal + a_p * k4 + p * (emin - 0.5) + m * data.dmin / 2


def scan(
    limit: int,
) -> tuple[int, int, tuple[float, tuple[float, ...]], tuple[float, ...]]:
    retained = 0
    nonpositive = 0
    best: tuple[float, tuple[float, ...]] = (math.inf, ())
    active_q: set[float] = set()

    for offset, rmin in ((0.0, 1.0), (0.5, 1.5)):
        q = rmin + 2
        while q <= limit + offset + 1.0e-12:
            data = band_data(q)
            max_m = int(math.floor(q - rmin - 1 + 1.0e-12))
            for m in range(1, max_m + 1):
                x = q - m

                # Necessary lower-shelf feasibility from Round 30.
                if action(data.k3, x) - action(q, x) < 1.75:
                    continue

                p_lo = max(1, int(math.floor(data.dmin * m + 1.0e-12)) + 1)
                p_hi = int(math.floor(x - rmin + 1.0e-12))
                if p_lo > p_hi:
                    continue

                p_values = np.arange(p_lo, p_hi + 1, dtype=float)
                r_values = x - p_values
                emin = (
                    action(data.k2, r_values)
                    - action(data.k2, x)
                    - action(q + 1, r_values)
                    + action(q + 1, x)
                )

                # Necessary hard-sector condition.
                hard = emin < 0.5 - data.dmin * m / (2 * p_values)
                if not np.any(hard):
                    continue
                p_values = p_values[hard]
                r_values = r_values[hard]
                emin = emin[hard]

                k4 = (
                    ((q + 1) ** -1 - data.k2**-1)
                    * (x**2 - r_values**2)
                    / (2 * PI)
                    + ((q + 1) ** -3 - data.k2**-3)
                    * (x**4 - r_values**4)
                    / (24 * PI)
                )
                a_p = p_values**2 / (3 * (2 * r_values + p_values))
                values = (
                    data.terminal
                    + a_p * k4
                    + p_values * (emin - 0.5)
                    + m * data.dmin / 2
                )
                retained += len(values)
                active_q.add(float(q))
                nonpositive += int(np.count_nonzero(values <= 0))

                index = int(np.argmin(values))
                if values[index] < best[0]:
                    best = (
                        float(values[index]),
                        (
                            q,
                            float(r_values[index]),
                            float(p_values[index]),
                            float(m),
                            data.terminal,
                            float(emin[index]),
                            float(k4[index]),
                            data.dmin,
                        ),
                    )
            q += 1

    return retained, nonpositive, best, tuple(sorted(active_q))


def alpha_zero_patterns() -> tuple[float, list[tuple[float, ...]]]:
    rows: list[tuple[float, ...]] = []
    for r in (15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5):
        p = m = 2
        q = r + p + m
        x = r + p
        t = brentq(
            lambda phase: action(q / math.cos(phase), x) - action(q, x) - 1.75,
            1.0e-8,
            PI / 2 - 1.0e-8,
            xtol=2.0e-14,
            rtol=2.0e-14,
        )
        outer = q / math.cos(t)
        theta = brentq(
            lambda angle: outer / PI * (
                math.sin(angle) - angle * math.cos(angle)
            )
            - 0.75,
            1.0e-10,
            PI / 2 - 1.0e-10,
        )
        y1 = outer * math.cos(theta) - q
        eta = y1 - 2
        d = 1 - 2 * t / PI
        h_value = 3 * PI / (32 * (1 - math.cos(t))) * max(
            1.0, 4 * (1 + d) ** 3 / (27 * d)
        )
        residual = 1 + 2 * eta - h_value
        rows.append((r, t, y1, h_value, residual))
    return min(row[-1] for row in rows), rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--limit",
        type=int,
        default=300,
        help="largest q on each parity grid in the finite diagnostic scan",
    )
    args = parser.parse_args()

    fixture = fixture_value(5.0, 1.0, 3, 1)
    retained, nonpositive, best, active_q = scan(args.limit)
    alpha_min, alpha_rows = alpha_zero_patterns()

    print("ROUND 30 RETAINED-E SHELF SCAN (DIAGNOSTIC ONLY)")
    print(f"qLimit={args.limit}")
    print(f"fixtureF_q5_r1_p3_m1={fixture:.15g}")
    print(f"retainedRelaxedRecords={retained}")
    print(f"activeQCount={len(active_q)}")
    print(f"activeQRange={(active_q[0], active_q[-1]) if active_q else None}")
    print(f"nonpositiveRecords={nonpositive}")
    print(f"minimumRecord={best}")
    print(f"alphaZeroMinimumResidual={alpha_min:.15g}")
    print(f"alphaZeroRows={alpha_rows}")
    print("infiniteQCoverage=False")
    print("diagnosticOnly=True")

    if abs(fixture - 0.3009031466912554) > 5.0e-12:
        raise ArithmeticError("Round 30 fixture changed")
    if nonpositive or best[0] <= 0 or alpha_min <= 0:
        raise ArithmeticError("Round 30 finite diagnostic gate failed")
    print("round30RetainedShelfDiagnosticOK=True")


if __name__ == "__main__":
    main()
