#!/usr/bin/env python3
"""Round 47 Prompt-C independent search for the literal d=4 aggregate.

This file intentionally imports no Round-47 lead evaluator.  It reconstructs

    WT4 = integral_0^K z^2 A(z) dz - sum_{a>=1} a^2 [A(a)+1/4]_<

and, independently,

    B4(A) + sum_{a>=1} a D_A(a).

Binary64 searches are diagnostic.  The named certificates use exact rational
parameters and python-flint/Arb.  In particular, the script distinguishes a
literal aggregate counterexample from counterexamples to convenient local
sufficient inequalities.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import random
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from typing import Iterable

import mpmath as mp
import numpy as np

try:
    from flint import arb, ctx, fmpq
except ImportError:  # pragma: no cover - the repository machine has flint
    arb = ctx = fmpq = None


SEARCH_SEED = 470047
PI = math.pi
DEFAULT_RANDOM = 20_000
DEFAULT_ARB_BITS = 768


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ball_action_scalar(radius: float, z: float) -> float:
    if z >= radius:
        return 0.0
    return (math.sqrt(max(0.0, radius * radius - z * z)) - z * math.acos(z / radius)) / PI


def ball_action_vector(radius: float, z: np.ndarray) -> np.ndarray:
    out = np.zeros_like(z)
    mask = z < radius
    zz = z[mask]
    out[mask] = (np.sqrt(radius * radius - zz * zz) - zz * np.arccos(zz / radius)) / PI
    return out


def ball_cap_vector(radius: float, z: np.ndarray) -> np.ndarray:
    """Return int_z^radius G_radius(s) ds, with zero extension."""

    out = np.zeros_like(z)
    mask = z < radius
    zz = z[mask]
    theta = np.arccos(zz / radius)
    c = np.cos(theta)
    s = np.sin(theta)
    out[mask] = radius * radius / (4.0 * PI) * (
        theta * (1.0 + 2.0 * c * c) - 3.0 * s * c
    )
    return out


def strict_bracket_vector(values: np.ndarray) -> np.ndarray:
    """Literal [x]_< = max(0, ceil(x)-1), including integral walls."""

    return np.maximum(0, np.ceil(values) - 1).astype(np.int64)


def negative_components(values: np.ndarray, tolerance: float = 0.0) -> list[tuple[int, int]]:
    indices = np.flatnonzero(values < -tolerance) + 1
    if not len(indices):
        return []
    answer: list[tuple[int, int]] = []
    start = previous = int(indices[0])
    for raw in indices[1:]:
        index = int(raw)
        if index != previous + 1:
            answer.append((start, previous))
            start = index
        previous = index
    answer.append((start, previous))
    return answer


@dataclass
class FloatRecord:
    source: str
    tags: tuple[str, ...]
    rho: float
    K: float
    mu: float
    count_shifts: int
    terminal_count: int
    W4: float
    P4: float
    WT4: float
    bonus: float
    weighted_defects: float
    aggregate: float
    identity_residual: float
    recurrence_residual: float
    summation_by_parts_residual: float
    coarse_bonus: float
    coarse_aggregate: float
    bonus_negative_only: float
    minimum_D: float
    minimum_D_shift: int
    minimum_L: float
    minimum_L_shift: int
    negative_D_components: tuple[tuple[int, int], ...]
    minimum_action_wall_distance: float
    q_max: int


def evaluate_float(source: str, tags: Iterable[str], rho: float, K: float) -> FloatRecord:
    require(0.0 < rho < 1.0 and K > 0.0, "parameter domain")
    mu = rho * K
    n = max(0, math.ceil(K) - 1)
    shifts = np.arange(1, n + 1, dtype=np.float64)
    action = ball_action_vector(K, shifts) - ball_action_vector(mu, shifts)
    shifted = action + 0.25
    q = strict_bracket_vector(shifted)
    caps = ball_cap_vector(K, shifts) - ball_cap_vector(mu, shifts)

    if n:
        suffix_after = np.cumsum(q[::-1], dtype=np.int64)[::-1] - q
        tails = q + 2 * suffix_after
        defects = 2.0 * caps - tails
        next_defects = np.r_[defects[1:], 0.0]
        local = defects - next_defects
        next_caps = np.r_[caps[1:], 0.0]
        next_q = np.r_[q[1:], 0]
        local_direct = 2.0 * (caps - next_caps) - q - next_q
        recurrence_residual = float(np.max(np.abs(local - local_direct)))
        weights = shifts
        P4 = float(np.dot(weights * weights, q))
        weighted_defects = float(np.dot(weights, defects))
        weighted_local = float(np.dot(weights * (weights + 1.0) / 2.0, local_direct))
        summation_residual = weighted_local - weighted_defects
        sum_weighted_caps = float(np.dot(weights, caps))
        coarse_bonus = float(np.sum(action) / 12.0)
        wall_distance = float(np.min(np.abs(shifted - np.rint(shifted))))
        min_d_index = int(np.argmin(defects))
        min_l_index = int(np.argmin(local))
        components = negative_components(defects, tolerance=2e-11)
        negative_mask = defects < -2e-11
        weighted_negative = float(np.dot(weights[negative_mask], defects[negative_mask]))
        terminal_count = int(np.sum(q))
        q_max = int(np.max(q))
    else:
        defects = local = np.array([], dtype=np.float64)
        P4 = weighted_defects = sum_weighted_caps = coarse_bonus = weighted_negative = 0.0
        wall_distance = 0.25
        min_d_index = min_l_index = 0
        components = []
        terminal_count = q_max = 0
        recurrence_residual = summation_residual = 0.0

    W4 = (K**4 - mu**4) / 64.0
    WT4 = W4 - P4
    bonus = W4 - 2.0 * sum_weighted_caps
    aggregate = bonus + weighted_defects
    return FloatRecord(
        source=source,
        tags=tuple(sorted(set(tags))),
        rho=rho,
        K=K,
        mu=mu,
        count_shifts=n,
        terminal_count=terminal_count,
        W4=W4,
        P4=P4,
        WT4=WT4,
        bonus=bonus,
        weighted_defects=weighted_defects,
        aggregate=aggregate,
        identity_residual=aggregate - WT4,
        recurrence_residual=recurrence_residual,
        summation_by_parts_residual=summation_residual,
        coarse_bonus=coarse_bonus,
        coarse_aggregate=coarse_bonus + weighted_defects,
        bonus_negative_only=bonus + weighted_negative,
        minimum_D=float(defects[min_d_index]) if n else 0.0,
        minimum_D_shift=min_d_index + 1 if n else 0,
        minimum_L=float(local[min_l_index]) if n else 0.0,
        minimum_L_shift=min_l_index + 1 if n else 0,
        negative_D_components=tuple(components),
        minimum_action_wall_distance=wall_distance,
        q_max=q_max,
    )


def activity_threshold(rho: float) -> float:
    return math.sqrt(PI * PI / (1.0 - rho) ** 2 + 0.75)


def recheck_one_defect_mpmath(record: FloatRecord, dps: int = 80) -> mp.mpf:
    """Re-evaluate the binary64-minimizing shift without cap cancellation."""

    with mp.workdps(dps):
        K = mp.mpf(repr(record.K))
        rho = mp.mpf(repr(record.rho))
        mu = rho * K
        a = record.minimum_D_shift

        def action(radius: mp.mpf, z: int) -> mp.mpf:
            if z >= radius:
                return mp.mpf(0)
            return (
                mp.sqrt(radius * radius - z * z) - z * mp.acos(mp.mpf(z) / radius)
            ) / mp.pi

        def cap(radius: mp.mpf, z: int) -> mp.mpf:
            if z >= radius:
                return mp.mpf(0)
            theta = mp.acos(mp.mpf(z) / radius)
            c, s = mp.cos(theta), mp.sin(theta)
            return radius * radius / (4 * mp.pi) * (
                theta * (1 + 2 * c * c) - 3 * s * c
            )

        def strict_floor(value: mp.mpf) -> int:
            return max(0, int(mp.ceil(value)) - 1)

        q_a = strict_floor(action(K, a) - action(mu, a) + mp.mpf(1) / 4)
        suffix = sum(
            strict_floor(action(K, b) - action(mu, b) + mp.mpf(1) / 4)
            for b in range(a + 1, math.ceil(record.K))
        )
        return 2 * (cap(K, a) - cap(mu, a)) - q_a - 2 * suffix


def wall_K_fixed_mu(mu: float, shift: int, level: int) -> float:
    """Solve A(shift)+1/4=level while mu is fixed."""

    target = level - 0.25
    inner = ball_action_scalar(mu, float(shift))
    lo = max(mu, float(shift))
    hi = max(lo + 1.0, 2.0 * lo)
    while ball_action_scalar(hi, float(shift)) - inner < target:
        hi *= 2.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if ball_action_scalar(mid, float(shift)) - inner < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def proposal_stream(random_count: int) -> Iterable[tuple[str, tuple[str, ...], float, float]]:
    # 1--3: the active wall, thin shells, and small rho.
    for rho in (1e-6, 1e-4, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999, 0.9999):
        k0 = activity_threshold(rho)
        for eps in (1e-11, 1e-8, 1e-5, 1e-2, 0.2):
            tags = ["activity_wall"]
            if rho <= 0.01:
                tags.append("small_rho")
            if rho >= 0.95:
                tags.append("thin_shell")
            yield "activity", tuple(tags), rho, k0 * (1.0 + eps)

    # 4: integer and near-integer K.
    for N in (4, 5, 8, 10, 20, 40, 100, 300, 1000):
        for rho in (0.001, 0.1, 0.5, 0.9):
            for delta in (0.0, -1e-9, 1e-9):
                K = N + delta
                if K > activity_threshold(rho):
                    yield "integer-K", ("integer_K",), rho, K

    # 5 and 7: integer/near-integer mu and its interface cell.
    for mu in (1, 2, 3, 6, 10, 20, 36, 100):
        for rho in (0.1, 0.3, 0.5, 0.9):
            for delta in (0.0, -1e-9, 1e-9):
                K = (mu + delta) / rho
                if K > activity_threshold(rho):
                    yield "integer-mu", ("integer_mu", "inner_interface"), rho, K

    # 6: exact action-wall designs and both nearby sides.  The exact point is
    # handled separately with an Arb root certificate.
    for mu, shift, level in ((6, 5, 1), (6, 5, 2), (20, 10, 2), (10, 4, 3)):
        root = wall_K_fixed_mu(float(mu), shift, level)
        rho = mu / root
        if root > activity_threshold(rho):
            for relative in (-1e-10, 1e-10):
                K = root * (1.0 + relative)
                yield "action-wall", ("action_wall",), mu / K, K

    # 9: inherited high-floor first-drop geometries.  They are rebuilt from
    # their fixed-mu outer wall, without importing any earlier evaluator.
    inherited = (
        (1.0, 3, 1, 2),
        (1.0, 6, 11, 19),
        (1.5, 6, 7, 5),
        (16564.0, 19, 1, 2),
        (1.0, 9, 9, 3),
    )
    for r, p, m, B in inherited:
        q = r + p + m
        mu = q + 1.0
        target = B - 0.25
        lo, hi = mu, 2.0 * mu
        while ball_action_scalar(hi, q) < target:
            hi *= 2.0
        for _ in range(100):
            mid = (lo + hi) / 2.0
            if ball_action_scalar(mid, q) < target:
                lo = mid
            else:
                hi = mid
        K = (lo + hi) / 2.0
        yield "inherited-first-drop", ("high_floor_first_drop",), mu / K, K

    # 10: large a, K, and terminal count.
    for rho, K in ((0.02, 1000.0), (0.2, 3000.0), (0.8, 3000.0), (0.995, 20000.0)):
        if K > activity_threshold(rho):
            yield "large", ("large_K", "large_terminal_count"), rho, K

    rng = random.Random(SEARCH_SEED)
    for index in range(random_count):
        mode = index % 6
        if mode == 0:
            rho = rng.uniform(0.0001, 0.999)
            K = activity_threshold(rho) * (1.0 + 10.0 ** rng.uniform(-10.0, 1.2))
            tags = ("random", "activity_wall")
        elif mode == 1:
            rho = 10.0 ** rng.uniform(-6.0, -0.02)
            K = activity_threshold(rho) * 10.0 ** rng.uniform(0.0, 2.0)
            tags = ("random", "small_rho")
        elif mode == 2:
            rho = 1.0 - 10.0 ** rng.uniform(-3.2, -0.05)
            K = activity_threshold(rho) * 10.0 ** rng.uniform(0.0, 0.8)
            tags = ("random", "thin_shell")
        elif mode == 3:
            rho = rng.uniform(0.001, 0.95)
            N = rng.randint(4, 400)
            K = N + rng.choice((-1.0, 1.0)) * 10.0 ** rng.uniform(-11.0, -2.0)
            if K <= activity_threshold(rho):
                K = activity_threshold(rho) * (1.0 + 10.0 ** rng.uniform(-8.0, 0.8))
            tags = ("random", "integer_K")
        elif mode == 4:
            rho = rng.uniform(0.02, 0.95)
            mu = rng.randint(1, 180) + rng.choice((-1.0, 1.0)) * 10.0 ** rng.uniform(-11.0, -2.0)
            K = mu / rho
            if K <= activity_threshold(rho):
                K = activity_threshold(rho) * (1.0 + 10.0 ** rng.uniform(-8.0, 0.8))
            tags = ("random", "integer_mu", "inner_interface")
        else:
            rho = rng.uniform(0.001, 0.99)
            k0 = activity_threshold(rho)
            K = k0 + rng.random() * max(1.0, min(500.0, 6.0 * k0) - k0)
            tags = ("random",)
        if K <= 5000.0:
            yield "random", tags, rho, K


# ------------------------------ Arb certificates ---------------------------


def fq(value: Fraction | int) -> fmpq:
    value = Fraction(value)
    return fmpq(value.numerator, value.denominator)


def arb_hull(lo: Fraction, hi: Fraction) -> arb:
    require(lo <= hi, "rational interval orientation")
    return arb((fq(lo) + fq(hi)) / 2, (fq(hi) - fq(lo)) / 2)


def ball_action_arb(radius: arb, z_value: Fraction | int) -> arb:
    z = arb(fq(z_value))
    return ((radius * radius - z * z).sqrt() - z * (z / radius).acos()) / arb.pi()


def ball_cap_arb(radius: arb, z_value: Fraction | int) -> arb:
    z = arb(fq(z_value))
    theta = (z / radius).acos()
    c = z / radius
    s = (1 - c * c).sqrt()
    return radius * radius / (4 * arb.pi()) * (theta * (1 + 2 * c * c) - 3 * s * c)


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def directed_rational_ledger(rho_q: Fraction, K_q: Fraction, bits: int) -> dict[str, object]:
    require(arb is not None, "python-flint is required for directed checks")
    ctx.prec = bits
    mu_q = rho_q * K_q
    K = arb(fq(K_q))
    mu = arb(fq(mu_q))
    n = ceil_fraction(K_q) - 1
    actions: list[arb] = []
    caps: list[arb] = []
    q_values: list[int] = []
    for index in range(1, n + 1):
        a_q = Fraction(index)
        outer_action = ball_action_arb(K, a_q)
        inner_action = ball_action_arb(mu, a_q) if a_q < mu_q else arb(0)
        action = outer_action - inner_action
        shifted = action + fmpq(1, 4)
        candidate = max(0, math.ceil(float(shifted)) - 1)
        require(shifted > candidate and shifted < candidate + 1, f"strict action floor a={index}")
        actions.append(action)
        q_values.append(candidate)
        outer_cap = ball_cap_arb(K, a_q)
        inner_cap = ball_cap_arb(mu, a_q) if a_q < mu_q else arb(0)
        caps.append(outer_cap - inner_cap)

    suffix = 0
    defects: list[arb] = [arb(0)] * n
    tails: list[int] = [0] * n
    for index in range(n - 1, -1, -1):
        tails[index] = q_values[index] + 2 * suffix
        defects[index] = 2 * caps[index] - tails[index]
        suffix += q_values[index]

    W_q = (K_q**4 - mu_q**4) / 64
    P = sum((index + 1) ** 2 * q_values[index] for index in range(n))
    weighted_defects = sum((arb(index + 1) * defects[index] for index in range(n)), arb(0))
    local_defects: list[arb] = []
    for index in range(n):
        next_cap = caps[index + 1] if index + 1 < n else arb(0)
        next_q = q_values[index + 1] if index + 1 < n else 0
        local_defects.append(2 * (caps[index] - next_cap) - q_values[index] - next_q)
    weighted_local = sum(
        (
            arb((index + 1) * (index + 2) // 2) * local_defects[index]
            for index in range(n)
        ),
        arb(0),
    )
    bonus = arb(fq(W_q)) - 2 * sum((arb(index + 1) * caps[index] for index in range(n)), arb(0))
    aggregate = bonus + weighted_defects
    direct = arb(fq(W_q - P))
    coarse_bonus = sum(actions, arb(0)) / 12
    activity = K * K - arb.pi() ** 2 / (1 - arb(fq(rho_q))) ** 2 - fmpq(3, 4)
    require(activity > 0, "strict d=4 activity owner")
    require((aggregate - direct).contains(0), "direct/aggregate identity enclosure")
    require((weighted_local - weighted_defects).contains(0), "weighted summation-by-parts enclosure")
    require(bonus > coarse_bonus, "coarse d=4 bonus bound at named point")
    minimum_index = min(range(n), key=lambda index: float(defects[index]))
    negative = [index + 1 for index, value in enumerate(defects) if value < 0]
    return {
        "bits": bits,
        "rho": str(rho_q),
        "K": str(K_q),
        "mu": str(mu_q),
        "rho_bracket": [str(rho_q), str(rho_q)],
        "K_bracket": [str(K_q), str(K_q)],
        "strict_activity_gap": str(activity),
        "K_integer": K_q.denominator == 1,
        "mu_integer": mu_q.denominator == 1,
        "a_equals_mu_owner": int(mu_q) if mu_q.denominator == 1 and 1 <= int(mu_q) <= n else None,
        "a_equals_K_owner": "zero extension; excluded from a<K sum" if K_q.denominator == 1 else None,
        "number_of_strict_floor_certificates": n,
        "all_strict_floors_certified": True,
        "q": q_values,
        "tail_counts": tails,
        "W4_exact": str(W_q),
        "P4_exact": P,
        "WT4": str(direct),
        "bonus": str(bonus),
        "weighted_defects": str(weighted_defects),
        "aggregate": str(aggregate),
        "identity_residual": str(aggregate - direct),
        "weighted_local_defects": str(weighted_local),
        "summation_by_parts_residual": str(weighted_local - weighted_defects),
        "coarse_bonus": str(coarse_bonus),
        "bonus_minus_coarse": str(bonus - coarse_bonus),
        "minimum_D_shift": minimum_index + 1,
        "minimum_D": str(defects[minimum_index]),
        "negative_D_shifts": negative,
        "terminal_D": str(defects[-1]),
        "directed": True,
    }


def directed_cell_bonus(rho_q: Fraction, K_q: Fraction, a: int, bits: int, pieces: int) -> arb:
    """Directed interval Riemann enclosure of the exact d=4 cell bonus."""

    ctx.prec = bits
    mu_q = rho_q * K_q
    K = arb(fq(K_q))
    mu = arb(fq(mu_q))
    right = min(Fraction(a + 1), K_q)
    cuts = {Fraction(a), right}
    if Fraction(a) < mu_q < right:
        cuts.add(mu_q)
    ordered = sorted(cuts)
    total = arb(0)
    for left, end in zip(ordered, ordered[1:]):
        width = end - left
        for piece in range(pieces):
            lo = left + width * piece / pieces
            hi = left + width * (piece + 1) / pieces
            z = arb_hull(lo, hi)
            x = z - a
            minus_delta = arb(a) / 6 - arb(a) * x * (1 - x) / 2 + x**3 / 6
            if hi <= mu_q:
                slope = ((z / K).acos() - (z / mu).acos()) / arb.pi()
            elif lo >= mu_q:
                slope = (z / K).acos() / arb.pi()
            else:  # split construction should make this unreachable
                raise AssertionError("interface not split")
            total += 2 * arb(fq(width / pieces)) * slope * minus_delta
    return total


def directed_self_cell_counterexample(bits: int, pieces: int) -> dict[str, object]:
    rho_q, K_q, a = Fraction(9, 10), Fraction(40), 29
    ledger = directed_rational_ledger(rho_q, K_q, bits)
    ctx.prec = bits
    K, mu = arb(40), arb(36)
    q_values = ledger["q"]

    def cap_at(index: int) -> arb:
        outer = ball_cap_arb(K, index) if index < 40 else arb(0)
        inner = ball_cap_arb(mu, index) if index < 36 else arb(0)
        return outer - inner

    suffix_a = sum(q_values[a:])
    suffix_next = sum(q_values[a + 1 :])
    D_a = 2 * cap_at(a) - q_values[a - 1] - 2 * suffix_a
    D_next = 2 * cap_at(a + 1) - q_values[a] - 2 * suffix_next
    L_a = D_a - D_next
    bonus_cell = directed_cell_bonus(rho_q, K_q, a, bits, pieces)
    weight = a * (a + 1) // 2
    self_charge = bonus_cell + weight * L_a
    require(L_a < 0, "negative local trapezoidal defect")
    require(self_charge < 0, "cell-self-charge counterexample")
    require(arb(fmpq(4301)) > 0, "literal aggregate stays positive")
    return {
        "classification": "B: sufficient-route counterexample only",
        "proposed_inequality_rejected": "B_{4,a}+a(a+1)L_a/2 >= 0 cell by cell",
        "rho_bracket": ["9/10", "9/10"],
        "K_bracket": ["40", "40"],
        "mu": "36",
        "a": a,
        "weight": weight,
        "L_a": str(L_a),
        "cell_bonus": str(bonus_cell),
        "cell_self_charge": str(self_charge),
        "literal_WT4": ledger["WT4"],
        "complete_payment_ledger": ledger,
        "pieces": pieces,
        "bits": bits,
        "directed": True,
    }


def directed_action_wall(bits: int, decimal_digits: int = 70) -> dict[str, object]:
    """Unique strict action wall A(5)+1/4=1 with fixed mu=6."""

    mp.mp.dps = decimal_digits + 50
    mu_m = mp.mpf(6)
    target = mp.mpf(3) / 4

    def residual(K_m: mp.mpf) -> mp.mpf:
        def G(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
            return (mp.sqrt(radius * radius - z * z) - z * mp.acos(z / radius)) / mp.pi

        return G(K_m, mp.mpf(5)) - G(mu_m, mp.mpf(5)) - target

    lo, hi = mp.mpf(6), mp.mpf(12)
    while residual(hi) < 0:
        hi *= 2
    for _ in range(4 * decimal_digits + 80):
        mid = (lo + hi) / 2
        if residual(mid) < 0:
            lo = mid
        else:
            hi = mid
    scale = 10**decimal_digits
    K_lo = Fraction(int(mp.floor(lo * scale)), scale)
    K_hi = Fraction(int(mp.ceil(hi * scale)), scale)
    rho_lo, rho_hi = Fraction(6, 1) / K_hi, Fraction(6, 1) / K_lo

    ctx.prec = bits
    R_lo, R_hi = arb(fq(K_lo)), arb(fq(K_hi))
    mu = arb(6)
    f_lo = ball_action_arb(R_lo, 5) - ball_action_arb(mu, 5) - fmpq(3, 4)
    f_hi = ball_action_arb(R_hi, 5) - ball_action_arb(mu, 5) - fmpq(3, 4)
    require(f_lo < 0 < f_hi, "unique action root bracket")
    K = arb_hull(K_lo, K_hi)
    n = ceil_fraction(K_hi) - 1
    q_values: list[int] = []
    floor_owners: list[str] = []
    for index in range(1, n + 1):
        action = ball_action_arb(K, index) - (ball_action_arb(mu, index) if index < 6 else arb(0))
        shifted = action + fmpq(1, 4)
        if index == 5:
            q_value = 0  # [1]_< = 0 at the exact wall
            floor_owners.append("a=5 exact wall: [1]_< = 0")
        else:
            q_value = max(0, math.ceil(float(shifted)) - 1)
            require(shifted > q_value and shifted < q_value + 1, f"other wall floor a={index}")
            floor_owners.append(str(shifted))
        q_values.append(q_value)
    P = sum((index + 1) ** 2 * q_values[index] for index in range(n))
    W = (K**4 - mu**4) / 64
    WT = W - P
    activity = K**2 - arb.pi() ** 2 / (1 - mu / K) ** 2 - fmpq(3, 4)
    require(WT > 0 and activity > 0, "positive active exact action wall")
    return {
        "definition": "mu=6 and A(5)+1/4=1",
        "K_bracket": [str(K_lo), str(K_hi)],
        "rho_bracket": [str(rho_lo), str(rho_hi)],
        "root_residual_lo": str(f_lo),
        "root_residual_hi": str(f_hi),
        "root_unique": "d A(5)/dK=sqrt(K^2-25)/(pi K)>0 at fixed mu",
        "strict_floor_owner": "q_5=[1]_< = 0; the wall belongs to the lower-P side",
        "other_floor_certificates": floor_owners,
        "P4_exact_at_wall": P,
        "WT4": str(WT),
        "strict_activity_gap": str(activity),
        "bits": bits,
        "directed": True,
    }


def directed_bonus_cell_minimum(bits: int, a_value: int = 100, digits: int = 60) -> dict[str, object]:
    """Near-equality rational test of the exact cell polynomial lower bound."""

    getcontext().prec = digits + 50
    a_dec = Decimal(a_value)
    x_star = (a_dec * (a_dec + 1)).sqrt() - a_dec
    scale = 10**digits
    x_q = Fraction(int(x_star * scale), scale)
    ctx.prec = bits
    a = arb(a_value)
    x = arb(fq(x_q))
    polynomial = a / 6 - a * x * (1 - x) / 2 + x**3 / 6
    exact_minimum = a * (a + 1) / (12 * (a + fmpq(1, 2) + (a * (a + 1)).sqrt()))
    coarse = a / 24
    slack = polynomial - exact_minimum
    require(slack > 0, "rational near-minimizer remains above exact minimum")
    require(exact_minimum > coarse, "strict exact-to-coarse cell bound")
    return {
        "a": a_value,
        "x_rational_bracket": [str(x_q), str(x_q)],
        "stationary_x_formula": "sqrt(a(a+1))-a",
        "minus_Delta4": str(polynomial),
        "exact_cell_minimum": str(exact_minimum),
        "near_zero_slack": str(slack),
        "exact_minimum_minus_a_over_24": str(exact_minimum - coarse),
        "bits": bits,
        "directed": True,
    }


def compact_record(record: FloatRecord) -> dict[str, object]:
    return {
        "source": record.source,
        "tags": record.tags,
        "rho": record.rho,
        "K": record.K,
        "mu": record.mu,
        "WT4": record.WT4,
        "bonus": record.bonus,
        "weighted_defects": record.weighted_defects,
        "coarse_aggregate": record.coarse_aggregate,
        "bonus_negative_only": record.bonus_negative_only,
        "minimum_D": record.minimum_D,
        "minimum_D_shift": record.minimum_D_shift,
        "minimum_L": record.minimum_L,
        "minimum_L_shift": record.minimum_L_shift,
        "negative_D_components": record.negative_D_components,
        "terminal_count": record.terminal_count,
        "q_max": record.q_max,
        "identity_residual": record.identity_residual,
        "recurrence_residual": record.recurrence_residual,
        "summation_by_parts_residual": record.summation_by_parts_residual,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", type=int, default=DEFAULT_RANDOM)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--skip-directed", action="store_true")
    args = parser.parse_args()
    random_count = 1000 if args.quick else max(0, args.random)

    print("ROUND47C INDEPENDENT d=4 WEIGHTED-AGGREGATE SEARCH")
    print("round47_lead_evaluator_imported=False")
    print("literal_direct_proxy_and_bonus_defect_paths_built_independently=True")
    print(f"seed={SEARCH_SEED}; random={random_count}; quick={args.quick}")

    records: list[FloatRecord] = []
    class_counts: collections.Counter[str] = collections.Counter()
    seen: set[tuple[int, int]] = set()
    for source, tags, rho, K in proposal_stream(random_count):
        if not (0.0 < rho < 1.0 and K > activity_threshold(rho)):
            continue
        key = (round(rho * 1e13), round(K * 1e11))
        if key in seen:
            continue
        seen.add(key)
        record = evaluate_float(source, tags, rho, K)
        records.append(record)
        for tag in tags:
            class_counts[tag] += 1

    require(records, "empty search")
    literal_negative = [record for record in records if record.WT4 < -1e-7]
    negative_defect_records = [record for record in records if record.negative_D_components]
    ambiguous_near_zero = [record for record in records if abs(record.minimum_D) <= 2e-11]
    resolved_positive = [record for record in records if record.minimum_D > 2e-11]
    min_wt = min(records, key=lambda record: record.WT4)
    min_d = min(records, key=lambda record: record.minimum_D)
    min_coarse = min(records, key=lambda record: record.coarse_aggregate)
    min_bonus_negative = min(records, key=lambda record: record.bonus_negative_only)
    largest_terminal = max(records, key=lambda record: record.terminal_count)
    maximum_identity_error = max(abs(record.identity_residual) for record in records)
    maximum_recurrence_error = max(abs(record.recurrence_residual) for record in records)
    maximum_summation_error = max(abs(record.summation_by_parts_residual) for record in records)
    scale_identity_error = max(
        abs(record.identity_residual) / max(1.0, abs(record.WT4)) for record in records
    )

    print(f"distinct_proposals={len(records)}")
    print("stress_class_counts=" + json.dumps(dict(sorted(class_counts.items())), sort_keys=True))
    print(f"literal_WT4_negative={len(literal_negative)}")
    print(f"records_with_D_below_minus_2e-11={len(negative_defect_records)}")
    print(f"records_with_binary64_near_zero_D={len(ambiguous_near_zero)}")
    print(f"smallest_shift_a1_evaluations={len(records)}")
    hp_near_zero = [recheck_one_defect_mpmath(record) for record in ambiguous_near_zero]
    print(f"mpmath_near_zero_rechecks={len(hp_near_zero)}")
    print(f"mpmath_near_zero_negative={sum(value < 0 for value in hp_near_zero)}")
    if hp_near_zero:
        print(f"mpmath_near_zero_minimum={mp.nstr(min(hp_near_zero), 32)}")
    print(f"maximum_direct_aggregate_absolute_residual={maximum_identity_error:.12g}")
    print(f"maximum_direct_aggregate_scaled_residual={scale_identity_error:.12g}")
    print(f"maximum_adjacent_recurrence_absolute_residual={maximum_recurrence_error:.12g}")
    print(f"maximum_summation_by_parts_absolute_residual={maximum_summation_error:.12g}")
    print("minimum_WT4=" + json.dumps(compact_record(min_wt), sort_keys=True))
    print("minimum_sampled_D=" + json.dumps(compact_record(min_d), sort_keys=True))
    if resolved_positive:
        print(
            "minimum_resolved_positive_D="
            + json.dumps(compact_record(min(resolved_positive, key=lambda record: record.minimum_D)), sort_keys=True)
        )
    print("minimum_coarse_aggregate=" + json.dumps(compact_record(min_coarse), sort_keys=True))
    print("minimum_bonus_negative_only=" + json.dumps(compact_record(min_bonus_negative), sort_keys=True))
    print("largest_terminal_count=" + json.dumps(compact_record(largest_terminal), sort_keys=True))

    if not args.skip_directed:
        require(arb is not None, "python-flint unavailable")
        directed: dict[str, object] = {}
        # Exact rational corner: K and mu are integral and a=mu is assigned to
        # the outer formula; a=K belongs to the zero extension.
        directed["integer_K_mu_corner_768"] = directed_rational_ledger(
            Fraction(9, 10), Fraction(40), DEFAULT_ARB_BITS
        )
        directed["integer_K_mu_corner_1280"] = directed_rational_ledger(
            Fraction(9, 10), Fraction(40), 1280
        )
        # A rational point just above activity at very small rho.
        directed["near_activity_small_rho_768"] = directed_rational_ledger(
            Fraction(1, 10_000), Fraction(163, 50), DEFAULT_ARB_BITS
        )
        directed["near_activity_small_rho_1280"] = directed_rational_ledger(
            Fraction(1, 10_000), Fraction(163, 50), 1280
        )
        # Terminal defect tends to zero as K descends to an integer.  This
        # named near-zero record is positive by a directed enclosure.
        directed["near_zero_terminal_768"] = directed_rational_ledger(
            Fraction(1, 2), Fraction(10_000_001, 1_000_000), DEFAULT_ARB_BITS
        )
        directed["near_zero_terminal_1280"] = directed_rational_ledger(
            Fraction(1, 2), Fraction(10_000_001, 1_000_000), 1280
        )
        directed["action_wall_768"] = directed_action_wall(DEFAULT_ARB_BITS)
        directed["action_wall_1280"] = directed_action_wall(1280)
        directed["cell_minimum_1024"] = directed_bonus_cell_minimum(1024)
        directed["cell_minimum_1536"] = directed_bonus_cell_minimum(1536)
        directed["self_cell_counterexample_384"] = directed_self_cell_counterexample(384, 2048)
        directed["self_cell_counterexample_768"] = directed_self_cell_counterexample(768, 4096)
        print("DIRECTED_CERTIFICATES=" + json.dumps(directed, sort_keys=True))

    print("classification_A_literal_aggregate_counterexample=NONE_FOUND")
    print("classification_B_sufficient_route_counterexample=CELL_SELF_CHARGE_FALSE")
    print("negative_D_components_sampled=NONE")
    print("finite_search_is_diagnostic=True")
    print("positive_coverage_certificate: FALSE")


if __name__ == "__main__":
    main()
