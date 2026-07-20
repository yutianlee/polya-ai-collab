#!/usr/bin/env python3
"""Round 43 theorem-design diagnostic; this is not a proof or certificate.

The script reuses the retained exact-endpoint sample generator from Round 39
and measures the sharp radical envelope introduced in Round 43.  All
calculations use ordinary binary64 arithmetic and SciPy root finding.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUND39_PATH = ROOT / "computations" / "general_d_round39_outer_face_diagnostic.py"
SPEC = importlib.util.spec_from_file_location("round39_round43", ROUND39_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND39_PATH}")
R39 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R39
SPEC.loader.exec_module(R39)


def measures(item: object) -> tuple[float, float, float]:
    """Return H/H_lower, the reduced lower scalar, and T42."""

    r = item.r
    p = item.p
    m = item.m
    b0 = item.b0
    mu = r + p + m + 1
    x = r + p
    q = x + m
    t = item.t
    d = 1 - 2 * t / math.pi
    zeta = math.pi / (2 * t) - 1

    ur = math.sqrt(mu * mu - r * r)
    ux = math.sqrt(mu * mu - x * x)
    uq = math.sqrt(mu * mu - q * q)
    ap = p * p / (3 * (2 * r + p))
    r1 = (ur - ux) / (ux - uq)
    h_capital = (p + ap) * r1

    h_lower = (p + ap) * p * (2 * r + p) / (m * (2 * x + m)) * min(
        ux / ur, math.sqrt(uq / ur)
    )
    cap_lower = uq**3 / (3 * math.pi * mu * mu)
    reduced = (
        0.9
        + b0 * min(zeta, h_lower)
        + h_lower * cap_lower
        - (p - d * m) / 2
    )
    t42 = (
        0.9
        + b0 * min(zeta, h_capital)
        + h_capital * item.h
        - (p - d * m) / 2
    )
    return h_capital / h_lower, reduced, t42


def point_text(item: object) -> str:
    return (
        f"r={item.r:g} p={item.p} m={item.m} f={item.f} "
        f"B={item.B} B0={item.b0} j={item.j} t={item.t:.15g}"
    )


def main() -> None:
    values = R39.upper_outer_faces(R39.bounded_tuples())
    if not values:
        raise SystemExit("no retained Round 39 upper endpoints")

    rows = [(measures(item), item) for item in values]
    ratio_row = min(rows, key=lambda row: row[0][0])
    reduced_row = min(rows, key=lambda row: row[0][1])
    t42_row = min(rows, key=lambda row: row[0][2])

    print(f"diagnostic_only retained_endpoint_count={len(values)}")
    print(
        "diagnostic_only min_H_over_Hlower="
        f"{ratio_row[0][0]:.17g} at {point_text(ratio_row[1])}"
    )
    print(
        "diagnostic_only min_reduced_R43="
        f"{reduced_row[0][1]:.17g} at {point_text(reduced_row[1])}"
    )
    print(
        "diagnostic_only min_T42="
        f"{t42_row[0][2]:.17g} at {point_text(t42_row[1])}"
    )
    print("round43DiagnosticOnly=True")


if __name__ == "__main__":
    main()
