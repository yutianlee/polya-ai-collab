#!/usr/bin/env python3
"""Directed Round 48 counterexample to the continuous quarter-node route.

This script certifies one explicit failure of

    p(X(n-1/4)) <= integral_{n-1}^n X(t)^3/3 dt,

where p(x)=x(x+1)(2x+1)/6.  It also certifies that the literal discrete
QCL cell is positive at the same parameters.  Therefore the output rejects
only the continuous strengthening, not QCL, WT4, or the spectral theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx, fmpq
import flint


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fq(value: Fraction | int) -> fmpq:
    value = Fraction(value)
    return fmpq(value.numerator, value.denominator)


def qdec(value: str) -> Fraction:
    return Fraction(value)


def arb_hull(lo: Fraction, hi: Fraction) -> arb:
    require(lo <= hi, "rational interval orientation")
    return arb((fq(lo) + fq(hi)) / 2, (fq(hi) - fq(lo)) / 2)


def ball_action(radius: arb, z: arb) -> arb:
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / arb.pi()


def shell_action_at_rational(K: arb, mu: arb, mu_q: Fraction, z_q: Fraction) -> arb:
    z = arb(fq(z_q))
    outer = ball_action(K, z)
    inner = ball_action(mu, z) if z_q < mu_q else arb(0)
    return outer - inner


def ball_moment_primitive(radius: arb, z: arb) -> arb:
    """Integral from 0 to z of u^3 acos(u/R)/pi du for 0<=z<=R."""
    root = (radius * radius - z * z).sqrt()
    return (
        3 * radius**4 * (z / radius).asin()
        - z * root * (3 * radius * radius + 2 * z * z)
        + 8 * z**4 * (z / radius).acos()
    ) / (32 * arb.pi())


def p_poly(x: arb) -> arb:
    return x * (x + 1) * (2 * x + 1) / 6


def certify(bits: int, radius_digits: int) -> dict[str, object]:
    ctx.prec = bits
    K_q = Fraction(12428724869837205, 10**8)
    mu_q = Fraction(1412489996090409, 10**12)
    n = 39_561_154
    K = arb(fq(K_q))
    mu = arb(fq(mu_q))

    centers = {
        "n_minus_1": qdec("1413.979671055732002322146911"),
        "n_minus_quarter": qdec("1412.479643374752690037848886"),
        "n": qdec("1411.973732381506573189400456"),
    }
    seed_rad = Fraction(1, 10**20)
    target_width = Fraction(2, 10**radius_digits)
    levels = {
        "n_minus_1": Fraction(n - 1),
        "n_minus_quarter": Fraction(n) - Fraction(1, 4),
        "n": Fraction(n),
    }
    intervals: dict[str, arb] = {}
    brackets: dict[str, dict[str, str]] = {}
    for name, center in centers.items():
        lo = center - seed_rad
        hi = center + seed_rad
        target = arb(fq(levels[name]))
        f_lo = shell_action_at_rational(K, mu, mu_q, lo) - target
        f_hi = shell_action_at_rational(K, mu, mu_q, hi) - target
        require(f_lo > 0, f"{name}: lower inverse endpoint must lie left of root")
        require(f_hi < 0, f"{name}: upper inverse endpoint must lie right of root")
        while hi - lo > target_width:
            mid = (lo + hi) / 2
            f_mid = shell_action_at_rational(K, mu, mu_q, mid) - target
            require(not f_mid.contains(0), f"{name}: bisection sign indeterminate")
            if f_mid > 0:
                lo = mid
                f_lo = f_mid
            else:
                hi = mid
                f_hi = f_mid
        intervals[name] = arb_hull(lo, hi)
        brackets[name] = {
            "lo": str(lo),
            "hi": str(hi),
            "action_at_lo_minus_level": str(f_lo),
            "action_at_hi_minus_level": str(f_hi),
        }

    x_left = intervals["n_minus_1"]
    x_node = intervals["n_minus_quarter"]
    x_right = intervals["n"]
    require(intervals["n"] < mu and intervals["n_minus_1"] > mu, "cell must straddle mu")

    # Integral z^3 sigma(z) dz / 3 across the cell.  The inner action is
    # present only from x_right up to mu.
    outer_part = ball_moment_primitive(K, x_left) - ball_moment_primitive(K, x_right)
    inner_at_mu = 3 * mu**4 / 64
    inner_part = inner_at_mu - ball_moment_primitive(mu, x_right)
    supply = (outer_part - inner_part) / 3
    continuous_cost = p_poly(x_node)
    continuous_margin = supply - continuous_cost
    require(continuous_margin < 0, "continuous quarter-node route must be negative")

    m = 1412
    require(x_node > m and x_node < m + 1, "strict discrete cutoff must be m=1412")
    s2 = Fraction(m * (m + 1) * (2 * m + 1), 6)
    qcl_margin = supply - fq(s2)
    require(qcl_margin > 0, "literal QCL cell must remain positive")

    active = K * K - arb.pi() ** 2 / (1 - mu / K) ** 2 - fmpq(3, 4)
    require(active > 0, "strict active condition")
    t_mu = ball_action(K, mu)
    require(t_mu > n - 1 and t_mu < n, "interface height must straddle the cell")

    result = {
        "classification": "interval_certified",
        "claim_type": "route_counterexample",
        "software": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "arb_precision_bits": bits,
        },
        "parameters": {
            "K": str(K_q),
            "mu": str(mu_q),
            "n": n,
            "inverse_target_radius": str(Fraction(1, 10**radius_digits)),
        },
        "inverse_brackets": brackets,
        "active_slack": str(active),
        "interface_height": str(t_mu),
        "cell_supply": str(supply),
        "continuous_cost": str(continuous_cost),
        "continuous_margin": str(continuous_margin),
        "discrete_cutoff": m,
        "discrete_S2": str(s2),
        "discrete_QCL_margin": str(qcl_margin),
        "scope": "rejects continuous p(X) strengthening only; QCL and WT4 remain open",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    payload = json.dumps(result, indent=2, sort_keys=True)
    result["payload_sha256"] = hashlib.sha256((payload + "\n").encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, default=1400)
    parser.add_argument("--inverse-radius-digits", type=int, default=32)
    args = parser.parse_args()
    require(args.bits >= 256, "use at least 256 Arb bits")
    require(24 <= args.inverse_radius_digits <= 40, "unsupported inverse bracket radius")
    print(json.dumps(certify(args.bits, args.inverse_radius_digits), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
