#!/usr/bin/env python3
"""Round 6 diagnostics for the exact thin-shell scaled action.

ALL FLOATING-POINT OUTPUT FROM THIS SCRIPT IS DIAGNOSTIC ONLY.  In
particular, the wall detector is not interval arithmetic and the scans are
not certificates.  The exact formulas documented here are useful for
reproducing the exploration, but their floating evaluation does not promote
any proof obligation.

With rho=1-epsilon, a=epsilon*K, and y=epsilon*nu, the exact action is

    A(epsilon,a;y) = (G_a(y)-G_{rho*a}(y))/epsilon,

where

    G_R(y) = (sqrt(R^2-y^2)-y*acos(y/R))/pi

on 0 <= y < R and is zero for y >= R.  The dimensionless coarse proxy is

    epsilon * sum_y y [A(epsilon,a;y)+1/4]_<,

and its target is

    a^3/(3*pi) * (1-epsilon+epsilon^2/3).

The script also evaluates the optimized H-capped shift, action-only floors,
shifted-tail margins, selected radial walls, and the existing K_0 threshold.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from typing import Iterable

import mpmath as mp
import numpy as np


WALL_TOLERANCE = 1.0e-10


def _G_numpy(radius: float, y: np.ndarray) -> np.ndarray:
    """Vectorized G_radius, evaluated in ordinary double precision."""
    result = np.zeros_like(y, dtype=float)
    active = y < radius
    if not np.any(active):
        return result
    yy = y[active]
    ratio = np.clip(yy / radius, 0.0, 1.0)
    result[active] = (
        np.sqrt(np.maximum(0.0, radius * radius - yy * yy))
        - yy * np.arccos(ratio)
    ) / math.pi
    return result


def G_mp(radius: mp.mpf, y: mp.mpf) -> mp.mpf:
    """High-precision scalar G_radius."""
    if y >= radius:
        return mp.mpf("0")
    if y <= 0:
        return radius / mp.pi
    return (mp.sqrt(radius * radius - y * y) - y * mp.acos(y / radius)) / mp.pi


def scaled_action_numpy(epsilon: float, a: float, y: np.ndarray) -> np.ndarray:
    """Exact closed form, evaluated in ordinary double precision."""
    rho = 1.0 - epsilon
    return (_G_numpy(a, y) - _G_numpy(rho * a, y)) / epsilon


def scaled_action_mp(epsilon: mp.mpf, a: mp.mpf, y: mp.mpf) -> mp.mpf:
    """Exact closed form, evaluated with the current mpmath precision."""
    rho = 1 - epsilon
    return (G_mp(a, y) - G_mp(rho * a, y)) / epsilon


def _integral_G_tail_numpy(radius: float, y: np.ndarray) -> np.ndarray:
    """Integral of G_radius(z) from y to radius, in double precision."""
    result = np.zeros_like(y, dtype=float)
    active = y < radius
    if not np.any(active):
        return result
    yy = np.maximum(0.0, y[active])
    beta = np.arccos(np.clip(yy / radius, 0.0, 1.0))
    shape = (
        beta / 2.0
        + beta * np.cos(2.0 * beta) / 4.0
        - 3.0 * np.sin(2.0 * beta) / 8.0
    )
    result[active] = radius * radius * shape / math.pi
    return result


def target_integral(epsilon: float, a: float) -> float:
    """Exact integral int_0^a y*A(y)dy, evaluated in double precision."""
    return (
        a**3
        / (3.0 * math.pi)
        * (1.0 - epsilon + epsilon * epsilon / 3.0)
    )


def active_channel_count(epsilon: float, a: float) -> int:
    """Number of half-integers nu satisfying nu < K=a/epsilon.

    Inputs that are numerically indistinguishable from an angular wall must
    be handled separately in a certificate.  This routine is diagnostic.
    """
    K = a / epsilon
    return max(0, int(math.ceil(K - 0.5)))


def optimized_shift_numpy(
    epsilon: float, a: float, y: np.ndarray
) -> np.ndarray:
    """The scaled H-capped shift from the audited phase enclosure."""
    rho = 1.0 - epsilon
    shift = np.full_like(y, 0.25, dtype=float)
    inner = y < rho * a
    if np.any(inner):
        yy = y[inner]
        radius_squared = (rho * a) ** 2
        gap = radius_squared - yy * yy
        H = epsilon * (3.0 * radius_squared + 2.0 * yy * yy) / (
            24.0 * math.pi * gap**1.5
        )
        shift[inner] = np.minimum(H, 0.25)
    return shift


def _strict_floor_diagnostic(
    values: np.ndarray, tolerance: float = WALL_TOLERANCE
) -> tuple[np.ndarray, np.ndarray]:
    """Floating strict floors with explicit near-wall flags.

    A positive integer is assigned m-1, as required by [x]_<.  Values within
    ``tolerance`` of a positive integer are treated as walls and reported as
    ambiguous.  A rigorous computation must isolate rather than round them.
    """
    nearest = np.rint(values)
    near_wall = (nearest >= 1.0) & (np.abs(values - nearest) <= tolerance)
    counts = np.floor(values).astype(np.int64)
    counts[near_wall] = nearest[near_wall].astype(np.int64) - 1
    np.maximum(counts, 0, out=counts)
    return counts, near_wall


@dataclass(frozen=True)
class CaseDiagnostic:
    status: str
    epsilon: float
    c_epsilon_a_over_pi: float
    a: float
    K: float
    active_channels: int
    target: float
    action_floor_ratio: float
    optimized_proxy_ratio: float
    coarse_proxy_ratio: float
    raw_midpoint_ratio: float
    coarse_edge_ratio: float
    raw_edge_ratio: float
    edge_channels: int
    closest_positive_integer_distance: float
    near_wall_channels: int
    shifted_tail_violations: int
    minimum_scaled_tail_margin: float
    minimum_scaled_inner_tail_margin: float | None
    minimum_inner_tail_y_over_rho_a: float | None


def analyze_case(
    epsilon: float,
    c: float,
    *,
    wall_tolerance: float = WALL_TOLERANCE,
) -> CaseDiagnostic:
    """Evaluate one point with a=c*pi/epsilon.

    The parameter c is exactly the transition coordinate epsilon*a/pi used
    in the Round 5 product obstruction.
    """
    if not (0.0 < epsilon < 1.0):
        raise ValueError("epsilon must lie in (0,1)")
    if c <= 0.0:
        raise ValueError("c must be positive")

    rho = 1.0 - epsilon
    a = c * math.pi / epsilon
    K = a / epsilon
    channel_count = active_channel_count(epsilon, a)
    ell = np.arange(channel_count, dtype=float)
    y = epsilon * (ell + 0.5)
    action = scaled_action_numpy(epsilon, a, y)
    target = target_integral(epsilon, a)

    action_counts, action_walls = _strict_floor_diagnostic(
        action, wall_tolerance
    )
    optimized_values = action + optimized_shift_numpy(epsilon, a, y)
    optimized_counts, optimized_walls = _strict_floor_diagnostic(
        optimized_values, wall_tolerance
    )
    coarse_values = action + 0.25
    coarse_counts, coarse_walls = _strict_floor_diagnostic(
        coarse_values, wall_tolerance
    )

    def scaled_sum(values: np.ndarray) -> float:
        return epsilon * float(np.sum(y * values, dtype=np.float64))

    action_ratio = scaled_sum(action_counts) / target
    optimized_ratio = scaled_sum(optimized_counts) / target
    coarse_ratio = scaled_sum(coarse_counts) / target
    raw_midpoint_ratio = scaled_sum(action) / target

    edge = y >= rho * a
    edge_channels = int(np.count_nonzero(edge))
    coarse_edge_ratio = scaled_sum(
        np.where(edge, coarse_counts, 0)
    ) / target
    raw_edge_ratio = scaled_sum(np.where(edge, action, 0.0)) / target

    positive = coarse_values >= 0.5
    if np.any(positive):
        distances = np.abs(coarse_values[positive] - np.rint(coarse_values[positive]))
        closest_distance = float(np.min(distances))
    else:
        closest_distance = math.inf

    # The shifted-tail inequality T_r <= 2 int_{nu_r}^K A is equivalent to
    # epsilon*T_r/2 <= int_{y_r}^a mathcal A.  Compute every tail at once.
    suffix_inclusive = np.cumsum(coarse_counts[::-1], dtype=np.int64)[::-1]
    suffix_later = suffix_inclusive - coarse_counts
    tail_counts = coarse_counts + 2 * suffix_later
    action_tail_integrals = (
        _integral_G_tail_numpy(a, y)
        - _integral_G_tail_numpy(rho * a, y)
    ) / epsilon
    scaled_tail_margins = (
        action_tail_integrals - epsilon * tail_counts.astype(float) / 2.0
    )
    tail_violations = int(np.count_nonzero(scaled_tail_margins < -1.0e-8))
    minimum_tail = (
        float(np.min(scaled_tail_margins)) if channel_count else 0.0
    )
    inner = y < rho * a
    if np.any(inner):
        inner_indices = np.flatnonzero(inner)
        local_index = int(np.argmin(scaled_tail_margins[inner]))
        global_index = int(inner_indices[local_index])
        minimum_inner = float(scaled_tail_margins[global_index])
        inner_location = float(y[global_index] / (rho * a))
    else:
        minimum_inner = None
        inner_location = None

    all_walls = action_walls | optimized_walls | coarse_walls
    return CaseDiagnostic(
        status="diagnostic_only_not_interval_certified",
        epsilon=epsilon,
        c_epsilon_a_over_pi=c,
        a=a,
        K=K,
        active_channels=channel_count,
        target=target,
        action_floor_ratio=action_ratio,
        optimized_proxy_ratio=optimized_ratio,
        coarse_proxy_ratio=coarse_ratio,
        raw_midpoint_ratio=raw_midpoint_ratio,
        coarse_edge_ratio=coarse_edge_ratio,
        raw_edge_ratio=raw_edge_ratio,
        edge_channels=edge_channels,
        closest_positive_integer_distance=closest_distance,
        near_wall_channels=int(np.count_nonzero(all_walls)),
        shifted_tail_violations=tail_violations,
        minimum_scaled_tail_margin=minimum_tail,
        minimum_scaled_inner_tail_margin=minimum_inner,
        minimum_inner_tail_y_over_rho_a=inner_location,
    )


def K0_diagnostic(epsilon: str, dps: int = 80) -> dict[str, str]:
    """Evaluate the existing fixed-rho threshold and its thin asymptotic."""
    mp.mp.dps = dps
    e = mp.mpf(epsilon)
    if not (0 < e < 1):
        raise ValueError("epsilon must lie in (0,1)")
    rho = 1 - e
    eta = (mp.sqrt(1 - rho * rho) - rho * mp.acos(rho)) / mp.pi
    arho = 2 * mp.pi * rho / e
    C0 = 1 + 8 * mp.sqrt(2) / 15
    K0 = (
        (mp.sqrt(arho) + mp.sqrt(arho + 4 * eta * C0)) / (2 * eta)
    ) ** 2
    optical = e * K0
    leading = 9 * mp.pi**3 / (4 * e**3)
    transition_c = e * optical / mp.pi
    generic_fractional_margin_scale = 3 * mp.pi / (8 * optical)
    return {
        "status": "high_precision_diagnostic_only",
        "epsilon": mp.nstr(e, 30),
        "K0": mp.nstr(K0, 30),
        "a_HE_epsilon_K0": mp.nstr(optical, 30),
        "a_HE_over_leading_9pi3_over_4epsilon3": mp.nstr(
            optical / leading, 30
        ),
        "c_HE_epsilon_a_HE_over_pi": mp.nstr(transition_c, 30),
        "heuristic_generic_floor_margin_3pi_over_8a_HE": mp.nstr(
            generic_fractional_margin_scale, 30
        ),
    }


def coarse_radial_wall_probe(
    epsilon: str,
    ell: int,
    radial_integer: int,
    dps: int = 80,
) -> dict[str, object]:
    """Locate A(epsilon,a;y_ell)+1/4=m and probe its strict jump.

    The root is high-precision but is not interval isolated, so the result is
    still diagnostic.  The target channel is manually assigned m-1 at the
    wall and m immediately to its right, matching strict counting.
    """
    if ell < 0 or radial_integer < 1:
        raise ValueError("ell must be nonnegative and radial_integer positive")
    mp.mp.dps = dps
    e = mp.mpf(epsilon)
    y_mp = e * (ell + mp.mpf("0.5"))
    m = mp.mpf(radial_integer)

    def residual(a_mp: mp.mpf) -> mp.mpf:
        return scaled_action_mp(e, a_mp, y_mp) + mp.mpf("0.25") - m

    lower = y_mp
    upper = max((radial_integer + 1) * mp.pi, y_mp + mp.pi)
    while residual(upper) <= 0:
        upper *= 2
    for _ in range(4 * dps):
        middle = (lower + upper) / 2
        if residual(middle) <= 0:
            lower = middle
        else:
            upper = middle
    root = (lower + upper) / 2

    # Whole-proxy values are ordinary-double diagnostics.  Override the
    # selected channel rather than asking floating arithmetic to recognize
    # the high-precision equality.
    ef = float(e)
    af = float(root)
    rho = 1.0 - ef
    channel_count = active_channel_count(ef, af)
    y = ef * (np.arange(channel_count, dtype=float) + 0.5)
    action = scaled_action_numpy(ef, af, y)
    counts = np.floor(action + 0.25).astype(np.int64)
    np.maximum(counts, 0, out=counts)
    counts[ell] = radial_integer - 1
    target = target_integral(ef, af)
    wall_scaled = ef * float(np.sum(y * counts, dtype=np.float64))
    jump_scaled = ef * y[ell]

    return {
        "status": "diagnostic_root_not_interval_isolated",
        "epsilon": epsilon,
        "ell": ell,
        "radial_integer": radial_integer,
        "a_wall": mp.nstr(root, 40),
        "c_wall_epsilon_a_over_pi": mp.nstr(e * root / mp.pi, 30),
        "residual": mp.nstr(residual(root), 8),
        "strict_wall_proxy_ratio": wall_scaled / target,
        "immediate_right_proxy_ratio": (wall_scaled + jump_scaled) / target,
        "relative_jump": jump_scaled / target,
    }


def exact_symbolic_observations() -> dict[str, object]:
    """Machine-readable statements whose proofs are in the Round 6 report."""
    return {
        "status": "symbolic_statements_require_human_proof_check",
        "continuous_identity": (
            "int_0^a y*A(y)dy = a^3(1-epsilon+epsilon^2/3)/(3*pi)"
        ),
        "raw_midpoint_counterexample_family": {
            "parameters": "0<epsilon<=1/10, K=1, y_0=epsilon/2",
            "claim": (
                "epsilon*y_0*A(y_0) exceeds the complete continuous target"
            ),
            "elementary_certificate": (
                "A(y_0)>=epsilon*(2*sqrt(14)/9)/pi, "
                "sqrt(14)>3, and 1-epsilon+epsilon^2/3<1"
            ),
        },
        "single_effective_radius_obstruction": (
            "R_eff=sqrt(1-epsilon+epsilon^2/3)<1 matches the cubic integral, "
            "but its flat action vanishes for y>R_eff*a while A(y)>0 for y<a"
        ),
        "strict_wall_rule": (
            "at A(y_ell)+1/4=m the channel count is m-1; immediately right it is m"
        ),
    }


def _parse_wall_probe(text: str) -> tuple[str, int, int]:
    pieces = text.split(":")
    if len(pieces) != 3:
        raise argparse.ArgumentTypeError("wall probe must be epsilon:ell:m")
    return pieces[0], int(pieces[1]), int(pieces[2])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--epsilons",
        nargs="+",
        type=float,
        default=[0.1, 0.05, 0.02, 0.01],
    )
    parser.add_argument(
        "--cs",
        nargs="+",
        type=float,
        default=[0.25, 0.75, 2.0, 10.0],
        help="values of c=epsilon*a/pi",
    )
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--wall-probe",
        action="append",
        type=_parse_wall_probe,
        default=[],
        metavar="EPSILON:ELL:M",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases: list[CaseDiagnostic] = []
    for epsilon in args.epsilons:
        for c in args.cs:
            cases.append(analyze_case(epsilon, c))

    wall_probes = [
        coarse_radial_wall_probe(e, ell, m, args.dps)
        for e, ell, m in args.wall_probe
    ]
    output = {
        "warning": (
            "floating/high-precision diagnostics only; no interval certificate "
            "and no proof-obligation promotion"
        ),
        "symbolic_observations": exact_symbolic_observations(),
        "cases": [asdict(case) for case in cases],
        "K0_thresholds": [
            K0_diagnostic(str(epsilon), args.dps) for epsilon in args.epsilons
        ],
        "radial_wall_probes": wall_probes,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
