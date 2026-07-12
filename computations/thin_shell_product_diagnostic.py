#!/usr/bin/env python3
"""Diagnostic and exact checks for the thin-shell product proxy.

FLOATING-POINT OUTPUT FROM THIS SCRIPT IS DIAGNOSTIC ONLY. It is not an
interval certificate. The function rational_counterexample_certificate is
different: it verifies the counterexample (epsilon, a) = (1/4, 11) using
only Fraction arithmetic and the classical rational bracket

    333/106 < pi < 22/7.

The event sweep evaluates the limiting ratio immediately to the right of
radial/angular walls. At a wall itself the new lattice contribution is
excluded by the strict inequalities in the proxy.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math

import mpmath as mp


@dataclass(frozen=True)
class ProxyResult:
    epsilon: str
    a: str
    radial_modes: int
    product: int
    weyl: str
    ratio: str


def angular_q_from_x(x: mp.mpf) -> int:
    """Return L+1 when L(L+1) < x, preserving equality at angular walls."""
    if x <= 0:
        raise ValueError("x must be positive")
    root = (mp.sqrt(1 + 4 * x) - 1) / 2
    return int(mp.ceil(root))


def strict_radial_mode_count(a: mp.mpf) -> int:
    """Number of positive integers n satisfying n*pi < a."""
    return max(0, int(mp.ceil(a / mp.pi) - 1))


def product_proxy(epsilon: mp.mpf, a: mp.mpf) -> tuple[int, list[int]]:
    """Compute P with high-precision floating evaluation of the walls."""
    if not (0 < epsilon <= 1):
        raise ValueError("epsilon must lie in (0, 1]")
    if a <= 0:
        raise ValueError("a must be positive")
    mode_count = strict_radial_mode_count(a)
    total = 0
    qs: list[int] = []
    for n in range(1, mode_count + 1):
        x = (a * a - (n * mp.pi) ** 2) / (epsilon * epsilon)
        q = angular_q_from_x(x)
        qs.append(q)
        total += q * q
    return total, qs


def product_at_radial_wall(epsilon: mp.mpf, m: int) -> tuple[int, list[int]]:
    """Compute P at a=m*pi, explicitly excluding the n=m radial mode."""
    if m < 1:
        raise ValueError("m must be positive")
    a = m * mp.pi
    total = 0
    qs: list[int] = []
    for n in range(1, m):
        x = (a * a - (n * mp.pi) ** 2) / (epsilon * epsilon)
        q = angular_q_from_x(x)
        qs.append(q)
        total += q * q
    return total, qs


def weyl_proxy(epsilon: mp.mpf, a: mp.mpf) -> mp.mpf:
    return (
        mp.mpf(2)
        / (9 * mp.pi)
        * (1 - (1 - epsilon) ** 3)
        * a**3
        / epsilon**3
    )


def evaluate(epsilon: str, a: str, dps: int = 80) -> ProxyResult:
    mp.mp.dps = dps
    e = mp.mpf(epsilon)
    aa = mp.mpf(a)
    product, qs = product_proxy(e, aa)
    w = weyl_proxy(e, aa)
    return ProxyResult(
        epsilon=mp.nstr(e, 30),
        a=mp.nstr(aa, 30),
        radial_modes=len(qs),
        product=product,
        weyl=mp.nstr(w, 30),
        ratio=mp.nstr(product / w, 30),
    )


def first_radial_wall_failure(
    epsilon: str, max_m: int, dps: int = 80
) -> dict[str, object] | None:
    """Diagnostic scan at exact radial walls a=m*pi."""
    mp.mp.dps = dps
    e = mp.mpf(epsilon)
    for m in range(2, max_m + 1):
        product, _ = product_at_radial_wall(e, m)
        a = m * mp.pi
        w = weyl_proxy(e, a)
        if product > w:
            return {
                "m": m,
                "a_over_pi": m,
                "scaled_width_epsilon_a_over_pi": mp.nstr(e * m, 30),
                "product": product,
                "weyl": mp.nstr(w, 30),
                "ratio": mp.nstr(product / w, 30),
            }
    return None


def event_sweep(
    epsilon: float, c_max: float = 0.82, max_events: int = 5_000_000
) -> dict[str, object]:
    """Diagnostic sweep of every wall with epsilon*a/pi <= c_max.

    Each event (n, ell) occurs at

        a^2 = n^2*pi^2 + epsilon^2*ell*(ell+1).

    ell=0 is a radial wall with jump 1. ell>=1 is an angular wall with
    immediate-right jump 2*ell+1.
    """
    if not (0 < epsilon <= 1):
        raise ValueError("epsilon must lie in (0, 1]")
    a_max = c_max * math.pi / epsilon
    events: list[tuple[float, int, int, int]] = []
    n_max = int(a_max / math.pi)
    for n in range(1, n_max + 1):
        base = (n * math.pi) ** 2
        remainder = (a_max * a_max - base) / (epsilon * epsilon)
        if remainder < 0:
            continue
        ell_max = int((math.sqrt(1 + 4 * remainder) - 1) / 2)
        if len(events) + ell_max + 1 > max_events:
            return {
                "status": "skipped_event_cap",
                "epsilon": epsilon,
                "c_max": c_max,
                "event_cap": max_events,
                "events_before_skip": len(events),
            }
        for ell in range(ell_max + 1):
            a_squared = base + epsilon * epsilon * ell * (ell + 1)
            events.append((a_squared, 2 * ell + 1, n, ell))

    events.sort(key=lambda item: item[0])
    product = 0
    first_failure: dict[str, object] | None = None
    maximum = {"ratio": 0.0}
    index = 0
    while index < len(events):
        a_squared = events[index][0]
        jump = 0
        labels: list[tuple[int, int]] = []
        while index < len(events) and events[index][0] == a_squared:
            _, event_jump, n, ell = events[index]
            jump += event_jump
            labels.append((n, ell))
            index += 1

        # Equality excludes this jump at the wall. The following product is
        # the limiting value immediately to its right.
        product += jump
        a = math.sqrt(a_squared)
        w = (
            2
            / (9 * math.pi)
            * (1 - (1 - epsilon) ** 3)
            * a**3
            / epsilon**3
        )
        ratio = product / w
        record = {
            "a": a,
            "a_over_pi": a / math.pi,
            "scaled_width_epsilon_a_over_pi": epsilon * a / math.pi,
            "product_immediate_right": product,
            "weyl_at_wall": w,
            "ratio_immediate_right": ratio,
            "jump": jump,
            "wall_labels_n_ell": labels,
        }
        if first_failure is None and ratio > 1:
            first_failure = record
        if ratio > float(maximum["ratio"]):
            maximum = {"ratio": ratio, "record": record}

    return {
        "status": "diagnostic_only",
        "epsilon": epsilon,
        "c_max": c_max,
        "event_count": len(events),
        "first_immediate_right_failure": first_failure,
        "maximum_immediate_right_ratio": maximum,
    }


def rational_counterexample_certificate() -> dict[str, object]:
    """Exact Fraction certificate for (epsilon, a)=(1/4, 11)."""
    pi_lower = Fraction(333, 106)
    pi_upper = Fraction(22, 7)
    epsilon = Fraction(1, 4)
    a = Fraction(11)

    radial_modes_verified = 3 * pi_upper < a and 4 * pi_lower > a

    expected_q = {1: 42, 2: 36, 3: 23}
    angular_checks: dict[int, bool] = {}
    for n, q in expected_q.items():
        # x=16(121-n^2*pi^2) decreases with pi.
        x_lower = 16 * (a * a - n * n * pi_upper * pi_upper)
        x_upper = 16 * (a * a - n * n * pi_lower * pi_lower)
        angular_checks[n] = (
            Fraction((q - 1) * q) < x_lower
            and x_upper <= Fraction(q * (q + 1))
        )

    product = sum(q * q for q in expected_q.values())
    # W=98494/(9*pi); use pi>333/106 for a rational upper bound.
    weyl_upper = Fraction(98_494 * 106, 9 * 333)
    inequality_verified = Fraction(product) > weyl_upper

    return {
        "status": "exact_fraction_certificate",
        "epsilon": str(epsilon),
        "a": str(a),
        "pi_bracket": ["333/106", "22/7"],
        "radial_modes_are_1_2_3": radial_modes_verified,
        "angular_q": expected_q,
        "angular_checks": angular_checks,
        "product": product,
        "weyl_exact_expression": "98494/(9*pi)",
        "weyl_rational_upper_bound": str(weyl_upper),
        "product_exceeds_weyl": inequality_verified,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--epsilons",
        nargs="+",
        default=["0.1", "0.05", "0.02", "0.01"],
        help="epsilon values for radial-wall and event scans",
    )
    parser.add_argument("--radial-max", type=int, default=1000)
    parser.add_argument("--c-max", type=float, default=0.82)
    parser.add_argument("--max-events", type=int, default=5_000_000)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--skip-events", action="store_true", help="run only exact/radial checks"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output: dict[str, object] = {
        "warning": "floating scans are diagnostic only, not certified",
        "exact_rational_counterexample": rational_counterexample_certificate(),
        "radial_wall_scans": {},
        "event_sweeps": {},
    }
    radial_scans = output["radial_wall_scans"]
    event_scans = output["event_sweeps"]
    assert isinstance(radial_scans, dict)
    assert isinstance(event_scans, dict)
    for epsilon in args.epsilons:
        radial_scans[epsilon] = first_radial_wall_failure(
            epsilon, args.radial_max, args.dps
        )
        if not args.skip_events:
            event_scans[epsilon] = event_sweep(
                float(epsilon), args.c_max, args.max_events
            )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
