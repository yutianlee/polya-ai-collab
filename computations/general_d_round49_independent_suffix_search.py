#!/usr/bin/env python3
"""Independent Round 49 adversarial evaluator.

This file intentionally does not import the Prompt-A evaluator.  It uses an
independently coded action/inverse ledger and an alternative trigonometric
moment primitive.  The structured sweep is diagnostic.  The embedded Arb
replay certifies only the already named Round 48 auxiliary-route
counterexample, at two independent precisions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from flint import arb, ctx, fmpq
import flint


mp.mp.dps = 70


def sb(x: mp.mpf) -> int:
    return max(0, int(mp.ceil(x)) - 1)


def s2(m: int) -> int:
    return m * (m + 1) * (2 * m + 1) // 6


def g(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf("0")
    if z <= 0:
        return radius / mp.pi
    return (
        mp.sqrt((radius - z) * (radius + z))
        - z * mp.acos(z / radius)
    ) / mp.pi


def action(rho: mp.mpf, K: mp.mpf, z: mp.mpf) -> mp.mpf:
    return g(K, z) - g(rho * K, z)


def inv(rho: mp.mpf, K: mp.mpf, t: mp.mpf) -> mp.mpf:
    H = K * (1 - rho) / mp.pi
    if t <= 0:
        return K
    if t >= H:
        return mp.mpf("0")
    a = mp.mpf("0")
    b = K
    for _ in range(250):
        c = (a + b) / 2
        if action(rho, K, c) > t:
            a = c
        else:
            b = c
    return (a + b) / 2


def alt_ball_moment(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Alternative exact primitive of z^3 acos(z/R)/pi."""
    if z <= 0:
        return mp.mpf("0")
    if z >= radius:
        return 3 * radius**4 / 64
    theta = mp.asin(z / radius)
    trig = (
        3 * theta / 8
        - mp.sin(2 * theta) / 4
        + mp.sin(4 * theta) / 32
    )
    return (
        z**4 * mp.acos(z / radius) / (4 * mp.pi)
        + radius**4 * trig / (4 * mp.pi)
    )


def shell_moment(rho: mp.mpf, K: mp.mpf, z: mp.mpf) -> mp.mpf:
    mu = rho * K
    return alt_ball_moment(K, z) - alt_ball_moment(mu, z)


def supply(rho: mp.mpf, K: mp.mpf, lo: mp.mpf, hi: mp.mpf) -> mp.mpf:
    x0 = inv(rho, K, lo)
    x1 = inv(rho, K, hi)
    return (shell_moment(rho, K, x0) - shell_moment(rho, K, x1)) / 3


def spatial_clipped_supply(
    rho: mp.mpf, K: mp.mpf, b: int, R: mp.mpf
) -> mp.mpf:
    mu = rho * K
    cuts = [mp.mpf("0")]
    if 0 < mu < R:
        cuts.append(mu)
    cuts.append(R)
    return mp.fsum(
        mp.quad(
            lambda z: z * z * max(mp.mpf("0"), action(rho, K, z) - b),
            [left, right],
        )
        for left, right in zip(cuts[:-1], cuts[1:])
        if right > left
    )


def evaluate(rho_s: str | mp.mpf, K_s: str | mp.mpf, verify_quad: bool) -> dict[str, object]:
    rho = mp.mpf(rho_s)
    K = mp.mpf(K_s)
    mu = rho * K
    H = K * (1 - rho) / mp.pi
    tau = g(K, mu)
    b = int(mp.floor(tau))
    Hhat = H - b
    q = int(mp.floor(Hhat))
    alpha = Hhat - q
    R = inv(rho, K, mp.mpf(b))

    # Inverse-node cost.
    inverse_cost = 0
    rows: list[dict[str, object]] = []
    k = 1
    while k - mp.mpf(1) / 4 < Hhat:
        eta = inv(rho, K, b + k - mp.mpf(1) / 4)
        M = sb(eta)
        inverse_cost += s2(M)
        rows.append({"k": k, "M": M, "eta": mp.nstr(eta, 24)})
        k += 1
    suffix_height = shell_moment(rho, K, R) / 3 - inverse_cost

    # Direct radial strict-bracket cost.
    spatial_cost = 0
    min_wall = mp.inf
    for a in range(1, int(mp.ceil(R))):
        if a >= R:
            continue
        x = max(mp.mpf("0"), action(rho, K, a) - b) + mp.mpf(1) / 4
        spatial_cost += a * a * sb(x)
        min_wall = min(min_wall, abs(x - mp.nint(x)))
    spatial_supply = (
        spatial_clipped_supply(rho, K, b, R)
        if verify_quad
        else shell_moment(rho, K, R) / 3
    )
    suffix_spatial = spatial_supply - spatial_cost

    literal_cost = 0
    for a in range(1, int(mp.ceil(K))):
        if a >= K:
            continue
        x = action(rho, K, a) + mp.mpf(1) / 4
        literal_cost += a * a * sb(x)
        min_wall = min(min_wall, abs(x - mp.nint(x)))
    WT4 = (K**4 - mu**4) / 64 - literal_cost

    total_inverse_cost = 0
    n = 1
    while n - mp.mpf(1) / 4 < H:
        total_inverse_cost += s2(sb(inv(rho, K, n - mp.mpf(1) / 4)))
        n += 1
    WT4_inverse = (K**4 - mu**4) / 64 - total_inverse_cost

    R_out = mp.mpf("0")
    prefix: list[dict[str, object]] = []
    for n in range(1, b + 1):
        N = sb(inv(rho, K, n - mp.mpf(1) / 4))
        reserve = mp.mpf(19 * N) / 48 + mp.mpf(27) / 128
        R_out += reserve
        prefix.append({"n": n, "N": N, "reserve": mp.nstr(reserve, 20)})

    complete: list[dict[str, object]] = []
    for k in range(1, q + 1):
        I = supply(rho, K, b + k - 1, b + k)
        M = sb(inv(rho, K, b + k - mp.mpf(1) / 4))
        complete.append(
            {
                "k": k,
                "M": M,
                "supply": mp.nstr(I, 24),
                "cell": mp.nstr(I - s2(M), 24),
            }
        )

    top_supply = supply(rho, K, b + q, H)
    if alpha > mp.mpf(3) / 4:
        top_M = sb(inv(rho, K, b + q + mp.mpf(3) / 4))
        top_cost = s2(top_M)
    else:
        top_M = 0
        top_cost = 0
    top = top_supply - top_cost

    active = K**2 - mp.pi**2 / (1 - rho) ** 2 - mp.mpf(3) / 4
    return {
        "rho": mp.nstr(rho, 24),
        "K": mp.nstr(K, 24),
        "mu": mp.nstr(mu, 24),
        "active_slack": mp.nstr(active, 24),
        "H": mp.nstr(H, 24),
        "tau": mp.nstr(tau, 24),
        "b": b,
        "B_mu": mp.nstr(tau - b, 24),
        "Hhat": mp.nstr(Hhat, 24),
        "q": q,
        "alpha": mp.nstr(alpha, 24),
        "R": mp.nstr(R, 24),
        "suffix_height": mp.nstr(suffix_height, 24),
        "suffix_spatial": mp.nstr(suffix_spatial, 24),
        "suffix_two_form_gap": mp.nstr(suffix_height - suffix_spatial, 12),
        "R_out": mp.nstr(R_out, 24),
        "fallback": mp.nstr(R_out + suffix_height, 24),
        "WT4": mp.nstr(WT4, 24),
        "WT4_inverse": mp.nstr(WT4_inverse, 24),
        "WT4_two_form_gap": mp.nstr(WT4 - WT4_inverse, 12),
        "min_action_wall_distance": mp.nstr(min_wall, 12),
        "rows": rows,
        "prefix": prefix,
        "complete_cells": complete,
        "top": {
            "node_included": alpha > mp.mpf(3) / 4,
            "M": top_M,
            "supply": mp.nstr(top_supply, 24),
            "value": mp.nstr(top, 24),
        },
    }


def active_wall(rho: mp.mpf) -> mp.mpf:
    return mp.sqrt(mp.pi**2 / (1 - rho) ** 2 + mp.mpf(3) / 4)


def stress_points(seed: int, random_count: int) -> list[tuple[mp.mpf, mp.mpf, str]]:
    points: list[tuple[mp.mpf, mp.mpf, str]] = []
    rhos = [
        mp.mpf("0.0001"),
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.5"),
        mp.mpf("0.9"),
        mp.mpf("0.99"),
    ]
    for rho in rhos:
        wall = active_wall(rho)
        points.extend(
            [
                (rho, wall * mp.mpf("1.0000001"), "activity"),
                (rho, wall * mp.mpf("1.05"), "moderate"),
                (rho, wall * 4, "large"),
            ]
        )
        # Terminal Hhat walls: 0, 1/4, 3/4, 1 modulo integers.
        min_H = wall * (1 - rho) / mp.pi
        base = max(1, int(mp.ceil(min_H)))
        for frac in ("0.00001", "0.24999", "0.25001", "0.74999", "0.75001", "0.99999"):
            K = mp.pi * (base + mp.mpf(frac)) / (1 - rho)
            if K > wall:
                points.append((rho, K, "terminal"))

        # tau and B(mu) just below/on/above an integer.
        scale = (
            mp.sqrt(1 - rho * rho) - rho * mp.acos(rho)
        ) / mp.pi
        m = max(1, int(mp.ceil(wall * scale)))
        for delta in ("-0.00001", "0", "0.00001"):
            K = (m + mp.mpf(delta)) / scale
            if K > wall:
                points.append((rho, K, f"interface_{delta}"))

        # Integer K and integer mu whenever strict activity allows it.
        Ki = int(mp.ceil(wall)) + 2
        points.append((rho, mp.mpf(Ki), "integer_K"))
        mui = max(1, int(mp.floor(rho * Ki)))
        rho_i = mp.mpf(mui) / Ki
        if 0 < rho_i < 1 and Ki > active_wall(rho_i):
            points.append((rho_i, mp.mpf(Ki), "integer_mu"))

    points.extend(
        [
            (mp.mpf("0.9"), mp.mpf("40"), "round47_counterexample"),
            (mp.mpf("0.5"), mp.mpf("20"), "round48_row_cone_record"),
        ]
    )
    rng = random.Random(seed)
    for _ in range(random_count):
        rho = mp.mpf(str(rng.uniform(0.0001, 0.995)))
        factor = mp.mpf(str(math.exp(rng.uniform(math.log(1.000001), math.log(12)))))
        points.append((rho, active_wall(rho) * factor, "random"))
    return points


def sweep(seed: int, random_count: int) -> dict[str, object]:
    minima: dict[str, tuple[mp.mpf, mp.mpf, mp.mpf, str]] = {}
    first: dict[str, dict[str, object] | None] = {
        "A_literal": None,
        "B_suffix": None,
        "C_fallback": None,
    }
    points = stress_points(seed, random_count)
    for rho, K, tag in points:
        r = evaluate(rho, K, verify_quad=False)
        suffix = mp.mpf(r["suffix_height"])
        fallback = mp.mpf(r["fallback"])
        wt4 = mp.mpf(r["WT4"])
        # Constructed exact interface walls can make the positive suffix
        # arbitrarily small by support collapse.  They remain in the
        # falsification search, but are not promoted as named near-zero
        # records without a separate directed bracket certificate.
        if not tag.startswith("interface_"):
            for key, value in (("suffix", suffix), ("fallback", fallback), ("WT4", wt4)):
                old = minima.get(key)
                if old is None or value < old[0]:
                    minima[key] = (value, rho, K, tag)
        if wt4 < 0 and first["A_literal"] is None:
            first["A_literal"] = r
        if suffix < 0 <= wt4 and first["B_suffix"] is None:
            first["B_suffix"] = r
        if fallback < 0 <= wt4 and first["C_fallback"] is None:
            first["C_fallback"] = r

    selected: dict[str, object] = {}
    for key, (value, rho, K, tag) in minima.items():
        selected[key] = {
            "value": mp.nstr(value, 24),
            "tag": tag,
            "record": evaluate(rho, K, verify_quad=True),
        }
    return {
        "classification": (
            "A" if first["A_literal"] is not None
            else "B" if first["B_suffix"] is not None
            else "C" if first["C_fallback"] is not None
            else "E"
        ),
        "evaluated_records": len(points),
        "first_negative_by_class": first,
        "selected_non_degenerate_minima": selected,
        "stress_classes": [
            "tau below/on/above integer",
            "B(mu) down to 0/up to 1",
            "interface-straddling first normalized row",
            "shallow inner band",
            "deep/shallow seam",
            "Hhat modulo 0,1/4,3/4,1",
            "terminal node appear/disappear",
            "integer and near-integer K,mu,R probes",
            "activity equality approach",
            "rho down to 0/up to 1",
            "moderate frequency",
            "large K/row count",
            "Round47-48 route-counterexample regressions",
        ],
        "positive_coverage_certificate": False,
    }


def fq(x: Fraction | int) -> fmpq:
    y = Fraction(x)
    return fmpq(y.numerator, y.denominator)


def ball_from_interval(lo: Fraction, hi: Fraction) -> arb:
    return arb((fq(lo) + fq(hi)) / 2, (fq(hi) - fq(lo)) / 2)


def arb_action(R: arb, z: arb) -> arb:
    return ((R * R - z * z).sqrt() - z * (z / R).acos()) / arb.pi()


def arb_alt_moment(R: arb, z: arb) -> arb:
    theta = (z / R).asin()
    trig = 3 * theta / 8 - (2 * theta).sin() / 4 + (4 * theta).sin() / 32
    return z**4 * (z / R).acos() / (4 * arb.pi()) + R**4 * trig / (4 * arb.pi())


def arb_cap(R: arb, z_value: int) -> arb:
    """Integral_z^R G_R(u) du."""
    z = arb(z_value)
    theta = (z / R).acos()
    c = z / R
    s = (1 - c * c).sqrt()
    return R**2 * (theta * (1 + 2 * c * c) - 3 * s * c) / (4 * arb.pi())


def directed_bonus_cell(bits: int, pieces: int) -> arb:
    """Independent interval Riemann enclosure for B_{4,29} at (9/10,40)."""
    ctx.prec = bits
    K = arb(40)
    mu = arb(36)
    total = arb(0)
    width = Fraction(1, pieces)
    for j in range(pieces):
        lo = Fraction(29) + j * width
        hi = lo + width
        z = ball_from_interval(lo, hi)
        x = z - 29
        minus_delta = arb(29) / 6 - arb(29) * x * (1 - x) / 2 + x**3 / 6
        slope = ((z / K).acos() - (z / mu).acos()) / arb.pi()
        total += 2 * arb(fq(width)) * slope * minus_delta
    return total


def directed_round47(bits: int, pieces: int) -> dict[str, object]:
    """Certify the Round 47 cell-self-charge failure and positive WT4."""
    ctx.prec = bits
    K = arb(40)
    mu = arb(36)
    q_values: list[int] = []
    for a in range(1, 40):
        z = arb(a)
        inner = arb_action(mu, z) if a < 36 else arb(0)
        shifted = arb_action(K, z) - inner + fmpq(1, 4)
        candidate = max(0, math.ceil(float(shifted)) - 1)
        if not (shifted > candidate and shifted < candidate + 1):
            raise AssertionError(f"uncertified strict action wall a={a}")
        q_values.append(candidate)
    P = sum((a + 1) ** 2 * q_values[a] for a in range(39))
    WT4 = Fraction(40**4 - 36**4, 64) - P

    def cap(index: int) -> arb:
        outer = arb_cap(K, index) if index < 40 else arb(0)
        inner = arb_cap(mu, index) if index < 36 else arb(0)
        return outer - inner

    a = 29
    D_a = 2 * cap(a) - q_values[a - 1] - 2 * sum(q_values[a:])
    D_next = 2 * cap(a + 1) - q_values[a] - 2 * sum(q_values[a + 1 :])
    L_a = D_a - D_next
    bonus = directed_bonus_cell(bits, pieces)
    self_charge = bonus + 435 * L_a
    if not (L_a < 0 and self_charge < 0 and WT4 == 4301):
        raise AssertionError("Round 47 directed regression failed")
    return {
        "bits": bits,
        "pieces": pieces,
        "rho": "9/10",
        "K": "40",
        "mu": "36",
        "a": 29,
        "L_29": str(L_a),
        "B_cell_29": str(bonus),
        "cell_self_charge": str(self_charge),
        "literal_WT4_exact": str(WT4),
        "strict_floor_ledger": q_values,
        "classification": "D_auxiliary_route_counterexample_with_literal_WT4_positive",
    }


def directed_main_positive(bits: int) -> dict[str, object]:
    """Directed class-E pressure record with a near suffix action wall."""
    ctx.prec = bits
    rho_q = Fraction(1, 100)
    K_q = Fraction(2_532_821, 25_000)
    mu_q = rho_q * K_q
    K = arb(fq(K_q))
    mu = arb(fq(mu_q))
    actions: list[arb] = []
    q_values: list[int] = []
    for a in range(1, math.ceil(K_q)):
        z = arb(a)
        inner = arb_action(mu, z) if Fraction(a) < mu_q else arb(0)
        A = arb_action(K, z) - inner
        shifted = A + fmpq(1, 4)
        candidate = max(0, math.ceil(float(shifted)) - 1)
        if not (shifted > candidate and shifted < candidate + 1):
            raise AssertionError(f"main record strict action wall a={a}")
        actions.append(A)
        q_values.append(candidate)

    P = sum((a + 1) ** 2 * q_values[a] for a in range(len(q_values)))
    W_q = (K_q**4 - mu_q**4) / 64
    WT4 = arb(fq(W_q - P))
    active = K**2 - arb.pi() ** 2 / (1 - fmpq(1, 100)) ** 2 - fmpq(3, 4)
    tau = arb_action(K, mu)
    if not (active > 0 and tau > 31 and tau < 32 and WT4 > 0):
        raise AssertionError("main record global ownership")

    R_lo = Fraction("2.517673351476663788910721007538815186134201064374167257624888797")
    R_hi = Fraction("2.517673351476663788910721007538815186134201064374167257624888798")
    f_lo = arb_action(K, arb(fq(R_lo))) - 31
    f_hi = arb_action(K, arb(fq(R_hi))) - 31
    if not (f_lo > 0 and f_hi < 0):
        raise AssertionError("main record R bracket")
    R = ball_from_interval(R_lo, R_hi)
    suffix_supply = arb_alt_moment(K, R) / 3 - mu**4 / 64

    suffix_q: list[int] = []
    for a in (1, 2):
        shifted = actions[a - 1] - 31 + fmpq(1, 4)
        candidate = max(0, math.ceil(float(shifted)) - 1)
        if not (shifted > candidate and shifted < candidate + 1):
            raise AssertionError(f"main suffix wall a={a}")
        suffix_q.append(candidate)
    suffix_cost = sum((a + 1) ** 2 * suffix_q[a] for a in range(2))
    suffix = suffix_supply - suffix_cost

    N_values: list[int] = []
    R_out = arb(0)
    for n in range(1, 32):
        target = arb(n) - fmpq(1, 4)
        N = 0
        for A in actions:
            if A > target:
                N += 1
            elif not (A < target):
                raise AssertionError(f"main inverse wall n={n}")
        N_values.append(N)
        R_out += fmpq(19 * N, 48) + fmpq(27, 128)
    fallback = R_out + suffix
    if not (suffix > 0 and fallback > 0 and suffix_q == [1, 0]):
        raise AssertionError("main record suffix classification")
    return {
        "bits": bits,
        "rho": "1/100",
        "K": "2532821/25000",
        "mu": "2532821/2500000",
        "active_slack": str(active),
        "tau": str(tau),
        "b": 31,
        "R_bracket": [str(R_lo), str(R_hi)],
        "literal_q": q_values,
        "P4": P,
        "W4_exact": str(W_q),
        "WT4": str(WT4),
        "suffix_q": suffix_q,
        "suffix_supply": str(suffix_supply),
        "suffix": str(suffix),
        "prefix_N": N_values,
        "R_out": str(R_out),
        "fallback": str(fallback),
        "classification": "E_positive_single_point_record_only",
    }


def directed_round48(bits: int, digits: int = 28) -> dict[str, object]:
    """Two-precision independent replay of the mandatory Round 48 record."""
    ctx.prec = bits
    K_q = Fraction(2485744973967441, 20_000_000)
    mu_q = Fraction(1412489996090409, 10**12)
    n = 39_561_154
    K = arb(fq(K_q))
    mu = arb(fq(mu_q))
    levels = {
        "left": Fraction(n - 1),
        "node": Fraction(n) - Fraction(1, 4),
        "right": Fraction(n),
    }
    centers = {
        "left": Fraction("1413.979671055732002322146911"),
        "node": Fraction("1412.479643374752690037848886"),
        "right": Fraction("1411.973732381506573189400456"),
    }
    brackets: dict[str, tuple[Fraction, Fraction]] = {}
    target_width = Fraction(2, 10**digits)
    for name, center in centers.items():
        lo = center - Fraction(1, 10**20)
        hi = center + Fraction(1, 10**20)
        target = arb(fq(levels[name]))
        while hi - lo > target_width:
            mid = (lo + hi) / 2
            z = arb(fq(mid))
            inner = arb_action(mu, z) if mid < mu_q else arb(0)
            value = arb_action(K, z) - inner - target
            if value.contains(0):
                raise ArithmeticError("indeterminate directed bisection sign")
            if value > 0:
                lo = mid
            else:
                hi = mid
        brackets[name] = (lo, hi)

    left = ball_from_interval(*brackets["left"])
    node = ball_from_interval(*brackets["node"])
    right = ball_from_interval(*brackets["right"])
    outer = arb_alt_moment(K, left) - arb_alt_moment(K, right)
    inner = 3 * mu**4 / 64 - arb_alt_moment(mu, right)
    I = (outer - inner) / 3
    pnode = node * (node + 1) * (2 * node + 1) / 6
    continuous_margin = I - pnode
    discrete_margin = I - fq(939_385_950)
    active = K**2 - arb.pi() ** 2 / (1 - mu / K) ** 2 - fmpq(3, 4)
    interface = arb_action(K, mu)
    if not (continuous_margin < 0 and discrete_margin > 0 and active > 0):
        raise AssertionError("directed classification failed")
    return {
        "bits": bits,
        "inverse_radius_digits": digits,
        "active_slack": str(active),
        "interface_height": str(interface),
        "continuous_margin": str(continuous_margin),
        "discrete_QCL_margin": str(discrete_margin),
        "classification": "D_auxiliary_route_counterexample_with_parent_positive",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=4902)
    parser.add_argument("--random-records", type=int, default=60)
    parser.add_argument("--skip-sweep", action="store_true")
    args = parser.parse_args()
    result: dict[str, object] = {
        "evaluator_independence": "does_not_import_Prompt_A",
        "software": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
        },
        "directed_Round48_regression": [
            directed_round48(768),
            directed_round48(1408),
        ],
        "directed_Round47_regression": [
            directed_round47(384, 1024),
            directed_round47(768, 2048),
        ],
        "directed_main_positive_record": [
            directed_main_positive(768),
            directed_main_positive(1280),
        ],
        "positive_coverage_certificate": False,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if not args.skip_sweep:
        result["sweep"] = sweep(args.seed, args.random_records)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
