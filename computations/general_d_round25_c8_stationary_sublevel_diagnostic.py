#!/usr/bin/env python3
"""Round 25 diagnostics for the delicate C8 stationary cell.

This is a double-precision falsification/theorem-design aid, not a proof
certificate.  It checks the exact stationary identity and the rigorous
alpha-free lower bound stated in the Round 25 note.  The final example shows
that the listed necessary conditions, without the full shelf inequalities,
are not sufficient to prove the lower bound nonnegative.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import general_d_round24_c8_wall_diagnostic as r24  # noqa: E402


PI = math.pi


def psi_of(P: float) -> float:
    """Positive root of p^2(2p+3)=P."""
    hi = max(2.0, P ** (1.0 / 3.0) + 2.0)
    while hi * hi * (2.0 * hi + 3.0) < P:
        hi *= 2.0
    return brentq(lambda p: p * p * (2.0 * p + 3.0) - P, 0.0, hi)


def reduced_data(B: int, m: int, t: float, u: float) -> dict[str, float]:
    H = math.tan(t) - t
    z = math.tan(t / 2.0)
    mu = PI * (B + u) / H
    L = 4.0 * u * (B + u) * math.tan(t) ** 2 / H
    R = m / PI + B * PI / (2.0 * t * t) - L
    P = 3.0 * PI * PI * (B + u) * R / (H * math.sin(t))
    psi = psi_of(P) if P > 0.0 else float("nan")
    interface_bound = mu - m - 1.0
    pmax = min(interface_bound, psi)
    M = 0.5 - t / PI + z / PI
    N = PI / (2.0 * t) - 1.0 + PI * z / (2.0 * t * t)
    F = M * m + N * B + 2.0 * u * u - z * L - 0.125 - pmax / 2.0
    delta = 0.75 - u
    first_drop_tangent = (
        (1.0 - math.cos(t))
        * (m - 1.0)
        * (2.0 * mu - m + 1.0)
        / (2.0 * PI * mu)
    )
    return {
        "H": H,
        "z": z,
        "mu": mu,
        "L": L,
        "R": R,
        "P": P,
        "psi": psi,
        "interface_bound": interface_bound,
        "pmax": pmax,
        "F": F,
        "delta": delta,
        "lower_wall_upper": (m + 1.0) * t / PI,
        "first_drop_tangent": first_drop_tangent,
    }


def check_feasible_witness() -> None:
    rec = r24.minimize_tuple(1.0, 5, 5, 2, 0.999999)
    assert rec is not None
    B = rec.b0
    mu = rec.r + rec.p + rec.m + rec.alpha
    W = r24.interface_action(mu, rec.t)
    u = W - B
    dat = reduced_data(B, rec.m, rec.t, u)
    C0 = rec.p * rec.p * (3.0 * rec.r + 2.0 * rec.p) / (3.0 * PI * mu)
    derivative = (
        C0 * math.sin(rec.t)
        - rec.m / PI
        - B * PI / (2.0 * rec.t * rec.t)
        + 4.0 * u * mu * math.tan(rec.t) ** 2 / PI
    )
    z = dat["z"]
    M = 0.5 - rec.t / PI + z / PI
    N = PI / (2.0 * rec.t) - 1.0 + PI * z / (2.0 * rec.t * rec.t)
    identity_value = (
        M * rec.m
        + N * B
        - rec.p / 2.0
        - 0.125
        + 2.0 * u * u
        - z * dat["L"]
    )
    print("feasible stationary witness")
    print(rec)
    print(f"u={u:.15g}")
    print(f"C8_t residual={derivative:.6g}")
    print(f"stationary identity value={identity_value:.15g}")
    print(f"direct C8={rec.value:.15g}")
    print(f"alpha-free lower F={dat['F']:.15g}")
    print(
        "m-bounds:",
        dat["first_drop_tangent"],
        "<", dat["delta"], "<", dat["lower_wall_upper"],
    )


def check_relaxed_obstruction() -> None:
    B, m, t, u = 1, 11, 0.2, 0.001
    dat = reduced_data(B, m, t, u)
    print("relaxed necessary-condition obstruction (not asserted shelf-feasible)")
    print(f"B={B} m={m} t={t} u={u}")
    for key in (
        "mu", "R", "psi", "interface_bound", "pmax", "F",
        "first_drop_tangent", "delta", "lower_wall_upper",
    ):
        print(f"{key}={dat[key]:.15g}")
    assert dat["R"] > 0.0
    assert dat["interface_bound"] > 1.0
    assert dat["first_drop_tangent"] < dat["delta"] < dat["lower_wall_upper"]
    assert dat["F"] < 0.0


if __name__ == "__main__":
    check_feasible_witness()
    check_relaxed_obstruction()
