#!/usr/bin/env python3
"""Non-certified diagnostics for the weighted shell phase enclosure.

This script deliberately separates:

1. the continuous G_K(nu)-F_mu(nu) phase upper surrogate;
2. its strict-integer envelope ceil(G-F)-1; and
3. a floating-point count obtained by integrating the exact Bessel phase rate.

Nothing produced here is an interval-arithmetic certificate.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import asdict, dataclass
from typing import Iterable

import numpy as np
from scipy.integrate import quad
from scipy.special import hankel1, spherical_jn, spherical_yn


PI = math.pi


def G(lam: float, z: float) -> float:
    """Audited G_lam(z), with a stable turning-point evaluation."""
    if z > lam:
        return 0.0
    if z == lam:
        return 0.0
    t = max(0.0, min(1.0, z / lam))
    beta = math.acos(t)
    if beta < 1.0e-3:
        b2 = beta * beta
        shape = beta**3 * (1.0 / 3.0 - b2 / 30.0 + b2 * b2 / 840.0)
    else:
        shape = math.sin(beta) - beta * math.cos(beta)
    return lam * shape / PI


def H(mu: float, z: float) -> float:
    """Audited H_mu(z), only called for z < mu."""
    gap = mu * mu - z * z
    if gap <= 0.0:
        return math.inf
    return (3.0 * mu * mu + 2.0 * z * z) / (24.0 * PI * gap**1.5)


def F_lower(mu: float, z: float) -> float:
    """Audited F_mu(z)."""
    if z >= mu:
        return -0.25
    return max(G(mu, z) - H(mu, z), -0.25)


def strict_integer_envelope(x: float) -> int:
    """Number of positive integers n satisfying n < x (floating evaluation)."""
    return max(0, math.ceil(x) - 1)


def ordinary_floor_envelope(x: float) -> int:
    """Conservative floating surrogate for max(0, floor(x))."""
    return max(0, math.floor(x + 1.0e-12))


def integral_G_tail(lam: float, start: float) -> float:
    """Closed-form integral of G_lam(z) from start to lam."""
    if start >= lam:
        return 0.0
    if start <= 0.0:
        return lam * lam / 8.0
    beta = math.acos(max(0.0, min(1.0, start / lam)))
    if beta < 0.05:
        b2 = beta * beta
        shape = beta**5 * (
            1.0 / 15.0
            - 4.0 * b2 / 315.0
            + b2 * b2 / 945.0
            - 8.0 * b2 * b2 * b2 / 155925.0
        )
    else:
        shape = beta / 2.0 + beta * math.cos(2.0 * beta) / 4.0 - 3.0 * math.sin(2.0 * beta) / 8.0
    return lam * lam * shape / PI


def integral_action_tail(K: float, mu: float, start: float) -> float:
    """Integral of G_K-G_mu from start to K."""
    return integral_G_tail(K, start) - integral_G_tail(mu, start)


def _phase_rate_spherical(x: float, ell: int) -> float:
    """theta'_{ell+1/2}(x) = 1/[x^2(j_ell^2+y_ell^2)]."""
    if ell == 0:
        return 1.0
    j = float(spherical_jn(ell, x))
    y = float(spherical_yn(ell, x))
    scale = max(abs(j), abs(y))
    if math.isinf(scale):
        return 0.0
    if not math.isfinite(scale) or scale == 0.0:
        raise FloatingPointError(f"bad spherical Bessel scale at ell={ell}, x={x}")
    js = j / scale
    ys = y / scale
    inv_sum = (1.0 / scale) ** 2 / (js * js + ys * ys)
    return inv_sum / (x * x)


def gamma_exact_float(rho: float, K: float, ell: int) -> tuple[float, float]:
    """Floating phase difference divided by pi, plus quad's error estimate."""
    mu = rho * K
    if ell == 0:
        return (K - mu) / PI, 0.0
    nu = ell + 0.5
    points = [nu] if mu < nu < K else None
    value, error = quad(
        lambda x: _phase_rate_spherical(x, ell),
        mu,
        K,
        points=points,
        epsabs=2.0e-11,
        epsrel=2.0e-11,
        limit=250,
    )
    return value / PI, error / PI


def strict_count_from_float(gamma: float, endpoint_tol: float = 2.0e-9) -> tuple[int, bool]:
    """Strict phase count, flagging values numerically indistinguishable from endpoints."""
    nearest = round(gamma)
    at_endpoint = nearest >= 1 and abs(gamma - nearest) <= endpoint_tol * max(1.0, gamma)
    if at_endpoint:
        return int(nearest) - 1, True
    return max(0, math.floor(gamma)), False


def angular_mode_count(K: float) -> int:
    """Number of half-integers nu=ell+1/2 satisfying the strict cutoff nu < K."""
    return max(0, math.ceil(K - 0.5 - 2.0e-13))


def shell_weyl(rho: float, K: float) -> float:
    return 2.0 * (1.0 - rho**3) * K**3 / (9.0 * PI)


@dataclass
class Diagnostic:
    rho: float
    K: float
    width: float
    modes: int
    weyl: float
    quarter_slack: float
    quarter_over_weyl: float
    baseline_sum: float
    quarter_surrogate_sum: float
    gf_surrogate_sum: float
    gf_over_weyl: float
    gf_integer_envelope: int
    coarse_integer_envelope: int
    min_shifted_tail_margin: float
    min_inner_tail_margin: float | None
    shifted_tail_violations: int
    actual_phase_sum: float | None
    actual_count: int | None
    actual_over_weyl: float | None
    endpoint_channels: str
    max_quad_error: float
    continuous_gf_proves: bool
    integer_gf_proves: bool
    floating_actual_below_weyl: bool | None


def analyze(rho: float, K: float, compute_actual: bool = True) -> Diagnostic:
    if not (0.0 < rho < 1.0 and K > 0.0):
        raise ValueError("require 0 < rho < 1 and K > 0")
    mu = rho * K
    modes = angular_mode_count(K)
    weyl = shell_weyl(rho, K)

    baseline_sum = 0.0
    gf_sum = 0.0
    gf_integer = 0
    coarse_values: list[int] = []
    actual_phase_sum = 0.0
    actual_count = 0
    endpoint_channels: list[str] = []
    max_error = 0.0

    for ell in range(modes):
        nu = ell + 0.5
        weight = 2 * ell + 1
        g_outer = G(K, nu)
        baseline = g_outer - G(mu, nu) if nu <= mu else g_outer
        gf = g_outer - F_lower(mu, nu)
        baseline_sum += weight * baseline
        gf_sum += weight * gf
        gf_integer += weight * strict_integer_envelope(gf)
        coarse_values.append(ordinary_floor_envelope(baseline + 0.25))

        if compute_actual:
            gamma, error = gamma_exact_float(rho, K, ell)
            q, endpoint = strict_count_from_float(gamma)
            actual_phase_sum += weight * gamma
            actual_count += weight * q
            max_error = max(max_error, error)
            if endpoint:
                endpoint_channels.append(f"ell={ell}:gamma~{gamma:.12g}")

    quarter_slack = modes * modes / 4.0
    quarter_sum = baseline_sum + quarter_slack
    coarse_integer = sum((2 * ell + 1) * value for ell, value in enumerate(coarse_values))
    minimum_tail_margin = math.inf
    minimum_inner_margin = math.inf
    tail_violations = 0
    later_sum = 0
    for r in range(modes - 1, -1, -1):
        tail_count = coarse_values[r] + 2 * later_sum
        later_sum += coarse_values[r]
        start = r + 0.5
        margin = 2.0 * integral_action_tail(K, mu, start) - tail_count
        minimum_tail_margin = min(minimum_tail_margin, margin)
        if start < mu:
            minimum_inner_margin = min(minimum_inner_margin, margin)
        if margin < -1.0e-9:
            tail_violations += 1
    if modes == 0:
        minimum_tail_margin = 0.0
    actual_phase_value = actual_phase_sum if compute_actual else None
    actual_count_value = actual_count if compute_actual else None
    actual_ratio = actual_count / weyl if compute_actual else None
    actual_below = actual_count < weyl if compute_actual else None

    return Diagnostic(
        rho=rho,
        K=K,
        width=(1.0 - rho) * K,
        modes=modes,
        weyl=weyl,
        quarter_slack=quarter_slack,
        quarter_over_weyl=quarter_slack / weyl,
        baseline_sum=baseline_sum,
        quarter_surrogate_sum=quarter_sum,
        gf_surrogate_sum=gf_sum,
        gf_over_weyl=gf_sum / weyl,
        gf_integer_envelope=gf_integer,
        coarse_integer_envelope=coarse_integer,
        min_shifted_tail_margin=minimum_tail_margin,
        min_inner_tail_margin=None if math.isinf(minimum_inner_margin) else minimum_inner_margin,
        shifted_tail_violations=tail_violations,
        actual_phase_sum=actual_phase_value,
        actual_count=actual_count_value,
        actual_over_weyl=actual_ratio,
        endpoint_channels=";".join(endpoint_channels),
        max_quad_error=max_error,
        continuous_gf_proves=gf_sum <= weyl,
        integer_gf_proves=gf_integer < weyl,
        floating_actual_below_weyl=actual_below,
    )


def print_markdown(rows: Iterable[Diagnostic]) -> None:
    print(
        "| rho | K | dK | M | W | Q/W | S_GF/W | U_GF | N_float | "
        "cont.? | integer? | endpoint |"
    )
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|:---|")
    for d in rows:
        actual = "-" if d.actual_count is None else str(d.actual_count)
        print(
            f"| {d.rho:.9g} | {d.K:.9g} | {d.width:.9g} | {d.modes} | "
            f"{d.weyl:.9g} | {d.quarter_over_weyl:.6g} | {d.gf_over_weyl:.6g} | "
            f"{d.gf_integer_envelope} | {actual} | "
            f"{'yes' if d.continuous_gf_proves else 'no'} | "
            f"{'yes' if d.integer_gf_proves else 'no'} | "
            f"{d.endpoint_channels or '-'} |"
        )


def representative_cases() -> list[tuple[float, float]]:
    endpoint_K = PI / 0.1
    return [
        (0.20, 20.0),
        (0.50, 20.0),
        (0.80, 20.0),
        (0.90, 20.0),
        (0.99, 100.0),
        (0.995, 200.0),
        (0.90, endpoint_K * (1.0 - 1.0e-7)),
        (0.90, endpoint_K),
        (0.90, endpoint_K * (1.0 + 1.0e-7)),
        (0.50, 20.4999999),
        (0.50, 20.5),
        (0.50, 20.5000001),
    ]


def self_test() -> None:
    for rho, K in [(0.2, 4.0), (0.9, 20.0), (0.99, 100.0)]:
        gamma, error = gamma_exact_float(rho, K, 0)
        assert error == 0.0
        assert abs(gamma - (1.0 - rho) * K / PI) < 2.0e-14
    for K in [0.49, 0.5, 0.500001, 1.49, 1.5, 1.500001, 20.499999, 20.5, 20.500001]:
        expected = sum(1 for ell in range(100) if ell + 0.5 < K)
        assert angular_mode_count(K) == expected
    for x, expected in [(0.2, 0), (1.0, 0), (1.2, 1), (2.0, 1), (2.2, 2)]:
        assert strict_integer_envelope(x) == expected
    d = analyze(0.9, 20.0, compute_actual=True)
    assert d.actual_count == 0  # width=2 < pi and theta' <= 1 for half-integer orders.
    # Independent phase-unwrapping spot checks against the derivative integral.
    for rho, K, ell in [(0.5, 20.0, 10), (0.9, PI / 0.1, 15), (0.99, 100.0, 99)]:
        gamma, _ = gamma_exact_float(rho, K, ell)
        xs = np.linspace(rho * K, K, 4001)
        phases = np.unwrap(np.angle(hankel1(ell + 0.5, xs)))
        unwrapped = float((phases[-1] - phases[0]) / PI)
        assert abs(gamma - unwrapped) < 5.0e-12
    print("self-test: ok")


def scan_surrogate_failures(limit: int) -> list[Diagnostic]:
    # First scan only inexpensive surrogate quantities.
    candidates: list[Diagnostic] = []
    rhos = [0.05, 0.10, 0.20, 0.35, 0.50, 0.65, 0.75, 0.80, 0.85, 0.90, 0.95, 0.98, 0.99]
    Ks = np.arange(0.5, 80.0001, 0.25)
    for rho in rhos:
        for K in Ks:
            d = analyze(rho, float(K), compute_actual=False)
            if not d.integer_gf_proves:
                candidates.append(d)
    # Prioritize the smallest relative integer-bound gap, where actual counting can matter.
    candidates.sort(key=lambda d: (d.gf_integer_envelope / d.weyl, d.K))
    checked: list[Diagnostic] = []
    for d in candidates[: max(5 * limit, 30)]:
        full = analyze(d.rho, d.K, compute_actual=True)
        if full.floating_actual_below_weyl:
            checked.append(full)
            if len(checked) >= limit:
                break
    return checked


def print_grid_summary() -> None:
    """Dense, non-certified scan of fractional and integerized surrogates."""
    rhos = list(np.arange(0.01, 1.0, 0.01)) + [0.999]
    Ks = np.concatenate([np.linspace(0.05, 2.0, 196), np.arange(2.05, 100.0001, 0.05)])
    active = 0
    baseline_at_or_above = 0
    gf_at_or_above = 0
    integer_proves = 0
    min_gf_ratio = math.inf
    max_gf_ratio = 0.0
    tail_cases_with_violation = 0
    min_tail_margin = math.inf
    min_inner_tail_margin = math.inf
    for rho in rhos:
        for K in Ks:
            d = analyze(float(rho), float(K), compute_actual=False)
            if d.modes == 0:
                continue
            active += 1
            baseline_at_or_above += d.baseline_sum >= d.weyl
            gf_at_or_above += d.gf_surrogate_sum >= d.weyl
            integer_proves += d.integer_gf_proves
            min_gf_ratio = min(min_gf_ratio, d.gf_over_weyl)
            max_gf_ratio = max(max_gf_ratio, d.gf_over_weyl)
            tail_cases_with_violation += d.shifted_tail_violations > 0
            min_tail_margin = min(min_tail_margin, d.min_shifted_tail_margin)
            if d.min_inner_tail_margin is not None:
                min_inner_tail_margin = min(min_inner_tail_margin, d.min_inner_tail_margin)
    print(f"active_grid_cases={active}")
    print(f"baseline_sum_ge_weyl={baseline_at_or_above}")
    print(f"gf_sum_ge_weyl={gf_at_or_above}")
    print(f"integer_gf_envelope_lt_weyl={integer_proves}")
    print(f"min_gf_over_weyl={min_gf_ratio:.12g}")
    print(f"max_gf_over_weyl={max_gf_ratio:.12g}")
    print(f"cases_with_shifted_tail_violation={tail_cases_with_violation}")
    print(f"min_shifted_tail_margin={min_tail_margin:.12g}")
    print(f"min_inner_tail_margin={min_inner_tail_margin:.12g}")


def print_random_summary(samples: int, seed: int) -> None:
    """Deterministic random stress test of the shifted-tail surrogate."""
    generator = random.Random(seed)
    violations = 0
    minimum_tail = math.inf
    minimum_inner = math.inf
    active = 0
    for index in range(samples):
        selector = index % 3
        if selector == 0:
            rho = generator.random()
        elif selector == 1:
            rho = 1.0 - 10.0 ** generator.uniform(-5.0, -0.01)
        else:
            rho = 10.0 ** generator.uniform(-5.0, -0.01)
        K = 10.0 ** generator.uniform(-1.2, 3.1)
        diagnostic = analyze(rho, K, compute_actual=False)
        if diagnostic.modes == 0:
            continue
        active += 1
        violations += diagnostic.shifted_tail_violations > 0
        minimum_tail = min(minimum_tail, diagnostic.min_shifted_tail_margin)
        if diagnostic.min_inner_tail_margin is not None:
            minimum_inner = min(minimum_inner, diagnostic.min_inner_tail_margin)
    print(f"seed={seed}")
    print(f"requested_samples={samples}")
    print(f"active_samples={active}")
    print(f"cases_with_shifted_tail_violation={violations}")
    print(f"min_shifted_tail_margin={minimum_tail:.12g}")
    print(f"min_inner_tail_margin={minimum_inner:.12g}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rho", type=float)
    parser.add_argument("--K", type=float)
    parser.add_argument("--no-actual", action="store_true")
    parser.add_argument("--representative", action="store_true")
    parser.add_argument("--scan", type=int, metavar="N", help="show N integer-surrogate failures")
    parser.add_argument("--grid-summary", action="store_true")
    parser.add_argument("--random-summary", type=int, metavar="N")
    parser.add_argument("--seed", type=int, default=20260712)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--dict", action="store_true", help="print full dictionaries")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.grid_summary:
        print_grid_summary()
        return
    if args.random_summary is not None:
        if args.random_summary <= 0:
            parser.error("--random-summary requires a positive sample count")
        print_random_summary(args.random_summary, args.seed)
        return
    if args.scan is not None:
        rows = scan_surrogate_failures(args.scan)
    elif args.representative:
        rows = [analyze(rho, K, not args.no_actual) for rho, K in representative_cases()]
    elif args.rho is not None and args.K is not None:
        rows = [analyze(args.rho, args.K, not args.no_actual)]
    else:
        parser.error("choose --representative, --scan N, or both --rho and --K")

    if args.dict:
        for row in rows:
            print(asdict(row))
    else:
        print_markdown(rows)


if __name__ == "__main__":
    main()
