#!/usr/bin/env python3
"""Exact Fraction certificate for the general-d finite ball-wall lemma.

This verifier uses only integers and ``fractions.Fraction``.  It certifies
the finite-wall proof in Proposition 6.5 of
``manuscript/spherical-shell-polya-general-d.tex``:

* the rational Taylor enclosures for ``asin`` and ``sqrt``;
* the complete list of eleven possible later-sample walls;
* separation of all wall brackets and exclusion of omitted walls;
* the local wall order and post-crossing integer M for every half-shift;
* positivity at the first later wall, every later wall, every activation
  point, and every relevant lower endpoint; and
* that the first later wall is the controlling wall for r <= 4.

No floating-point or transcendental evaluation occurs.  The analytic inputs
are the power series with alternating/geometric remainder bounds and Machin's
identity for pi.  Run from the repository root with

    python scripts/general_d_finite_wall_fraction_verify.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb


class Ledger:
    """Small assertion ledger with useful failure labels."""

    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        self.count += 1


ledger = Ledger()


# ---------------------------------------------------------------------------
# Rational pi and sqrt(3) inputs
# ---------------------------------------------------------------------------


def atan_reciprocal_bounds(inv: int, pairs: int = 4) -> tuple[Q, Q]:
    """Alternating-series bounds for atan(1/inv).

    A partial sum with an even number of terms is a lower bound; adding the
    next positive term gives an upper bound.
    """

    def partial(term_count: int) -> Q:
        total = Q(0)
        for k in range(term_count):
            term = Q(1, (2 * k + 1) * inv ** (2 * k + 1))
            total += term if k % 2 == 0 else -term
        return total

    return partial(2 * pairs), partial(2 * pairs + 1)


# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
atan5_lo, atan5_hi = atan_reciprocal_bounds(5)
atan239_lo, atan239_hi = atan_reciprocal_bounds(239)
pi_series_lo = 16 * atan5_lo - 4 * atan239_hi
pi_series_hi = 16 * atan5_hi - 4 * atan239_lo

PI_LO = Q(333, 106)
PI_HI = Q(355, 113)
ledger.require(PI_LO < pi_series_lo, "Machin series proves 333/106 < pi")
ledger.require(pi_series_hi < PI_HI, "Machin series proves pi < 355/113")

SQRT3_LO = Q(265, 153)
SQRT3_HI = Q(26, 15)
ledger.require(SQRT3_LO * SQRT3_LO < 3, "265/153 < sqrt(3)")
ledger.require(3 < SQRT3_HI * SQRT3_HI, "sqrt(3) < 26/15")

OMEGA_LO = SQRT3_LO / (2 * PI_HI) - Q(1, 6)
OMEGA_HI = SQRT3_HI / (2 * PI_LO) - Q(1, 6)
ledger.require(OMEGA_LO == Q(1184, 10863), "exact lower omega_0 bound")
ledger.require(OMEGA_HI == Q(1091, 9990), "exact upper omega_0 bound")

# If K_* = 1/omega_0, these are strict lower and upper bounds for K_*.
KSTAR_LO = 1 / OMEGA_HI
KSTAR_HI = 1 / OMEGA_LO
ledger.require(Q(227, 25) < KSTAR_LO, "9.08 < 1/omega_0")
ledger.require(KSTAR_HI < Q(459, 50), "1/omega_0 < 9.18")


# ---------------------------------------------------------------------------
# Rational Taylor envelopes
# ---------------------------------------------------------------------------


ASIN_COEFF = tuple(Q(comb(2 * m, m), 4**m * (2 * m + 1)) for m in range(7))
SQRT_COEFF = (Q(0),) + tuple(
    Q(comb(2 * m, m), 4**m * (2 * m - 1)) for m in range(1, 7)
)


def elementary_envelopes(x: Q) -> tuple[Q, Q, Q, Q]:
    """Return L <= asin <= U and W <= sqrt(1-x^2) <= V.

    The omitted positive coefficients are all below one, hence their tails
    are bounded by geometric series.  Every call in the certificate has
    0 <= x <= 13/20.
    """

    ledger.require(Q(0) <= x <= Q(13, 20), f"Taylor range for x={x}")
    x2 = x * x
    lower_asin = sum(
        (ASIN_COEFF[m] * x ** (2 * m + 1) for m in range(7)), Q(0)
    )
    upper_asin = lower_asin + x**15 / (1 - x2)
    upper_sqrt = 1 - sum(
        (SQRT_COEFF[m] * x2**m for m in range(1, 7)), Q(0)
    )
    lower_sqrt = upper_sqrt - x2**7 / (1 - x2)
    ledger.require(lower_sqrt > 0, f"positive square-root lower bound at x={x}")
    return lower_asin, upper_asin, lower_sqrt, upper_sqrt


def g_bounds(k: Q, z: Q) -> tuple[Q, Q]:
    """Rational lower/upper bounds for G_k(z)."""

    ledger.require(k > z >= 0, f"G domain k={k}, z={z}")
    x = z / k
    asin_lo, asin_hi, sqrt_lo, sqrt_hi = elementary_envelopes(x)
    lower = k * (Q(113, 355) * (sqrt_lo + x * asin_lo) - x / 2)
    upper = k * (Q(106, 333) * (sqrt_hi + x * asin_hi) - x / 2)
    ledger.require(lower < upper, f"ordered G bounds at k={k}, z={z}")
    return lower, upper


def h_bounds(k: Q, r: Q) -> tuple[Q, Q]:
    r"""Bounds for H_r(k)=2 int_r^k G_k-G_k(r)-1/4."""

    ledger.require(k > 2 * r, f"H is in residual range at k={k}, r={r}")
    x = r / k
    asin_lo, asin_hi, sqrt_lo, sqrt_hi = elementary_envelopes(x)
    a = k * k / 2 + r * r + r
    b = k * (3 * r / 2 + 1)
    lower = a / 2 - Q(106, 333) * (a * asin_hi + b * sqrt_hi) - Q(1, 4)
    upper = a / 2 - Q(113, 355) * (a * asin_lo + b * sqrt_lo) - Q(1, 4)
    ledger.require(lower < upper, f"ordered H bounds at k={k}, r={r}")
    return lower, upper


# ---------------------------------------------------------------------------
# Complete wall list
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class WallBracket:
    z: Q
    level: int
    k_lo: Q
    k_hi: Q
    left_gap: Q
    right_gap: Q

    @property
    def target(self) -> Q:
        return Q(self.level) - Q(1, 4)

    @property
    def key(self) -> tuple[Q, int]:
        return self.z, self.level


WALLS = (
    WallBracket(Q(3, 2), 1, Q(22, 5), Q(9, 2), Q(1, 100), Q(1, 100)),
    WallBracket(Q(2), 1, Q(5), Q(26, 5), Q(1, 50), Q(1, 50)),
    WallBracket(Q(5, 2), 1, Q(57, 10), Q(29, 5), Q(1, 125), Q(1, 50)),
    WallBracket(Q(3), 1, Q(63, 10), Q(32, 5), Q(1, 100), Q(1, 100)),
    WallBracket(Q(7, 2), 1, Q(69, 10), Q(7), Q(1, 100), Q(1, 100)),
    WallBracket(Q(4), 1, Q(15, 2), Q(38, 5), Q(1, 100), Q(1, 100)),
    WallBracket(Q(3, 2), 2, Q(77, 10), Q(39, 5), Q(1, 500), Q(1, 50)),
    WallBracket(Q(9, 2), 1, Q(81, 10), Q(41, 5), Q(1, 100), Q(1, 100)),
    WallBracket(Q(2), 2, Q(83, 10), Q(17, 2), Q(3, 100), Q(3, 100)),
    WallBracket(Q(5), 1, Q(87, 10), Q(44, 5), Q(1, 125), Q(3, 200)),
    WallBracket(Q(5, 2), 2, Q(9), Q(227, 25), Q(1, 50), Q(1, 2000)),
)

for wall in WALLS:
    _, g_left_upper = g_bounds(wall.k_lo, wall.z)
    g_right_lower, _ = g_bounds(wall.k_hi, wall.z)
    ledger.require(
        wall.target - g_left_upper > wall.left_gap,
        f"left sign/gap at wall {wall.key}",
    )
    ledger.require(
        g_right_lower - wall.target > wall.right_gap,
        f"right sign/gap at wall {wall.key}",
    )
    ledger.require(wall.k_hi < KSTAR_LO, f"wall {wall.key} lies below K_*")

for left, right in zip(WALLS, WALLS[1:]):
    ledger.require(
        left.k_hi < right.k_lo,
        f"disjoint ordered wall brackets {left.key}, {right.key}",
    )

expected_complete_keys = {
    *((Q(k, 2), 1) for k in range(3, 11)),
    *((Q(k, 2), 2) for k in range(3, 6)),
}
ledger.require(
    {wall.key for wall in WALLS} == expected_complete_keys,
    "eleven-wall key set",
)

# Exclude every unlisted wall by monotonicity in K and z.
k_cap = Q(459, 50)
_, absent_level1 = g_bounds(k_cap, Q(11, 2))
_, absent_level2 = g_bounds(k_cap, Q(3))
_, absent_level3 = g_bounds(k_cap, Q(3, 2))
ledger.require(absent_level1 < Q(18, 25) < Q(3, 4), "no level-1 wall for z>=11/2")
ledger.require(absent_level2 < Q(8, 5) < Q(7, 4), "no level-2 wall for z>=3")
ledger.require(absent_level3 < Q(9, 4) < Q(11, 4), "no level-3-or-higher wall")


# ---------------------------------------------------------------------------
# Local event lists and M classifications
# ---------------------------------------------------------------------------


R_VALUES = tuple(Q(k, 2) for k in range(1, 10))

EXPECTED_LOCAL = {
    Q(1, 2): ((Q(3, 2), 1), (Q(5, 2), 1), (Q(7, 2), 1), (Q(3, 2), 2), (Q(9, 2), 1), (Q(5, 2), 2)),
    Q(1): ((Q(2), 1), (Q(3), 1), (Q(4), 1), (Q(2), 2), (Q(5), 1)),
    Q(3, 2): ((Q(5, 2), 1), (Q(7, 2), 1), (Q(9, 2), 1), (Q(5, 2), 2)),
    Q(2): ((Q(3), 1), (Q(4), 1), (Q(5), 1)),
    Q(5, 2): ((Q(7, 2), 1), (Q(9, 2), 1)),
    Q(3): ((Q(4), 1), (Q(5), 1)),
    Q(7, 2): ((Q(9, 2), 1),),
    Q(4): ((Q(5), 1),),
    Q(9, 2): (),
}


def local_walls(r: Q) -> tuple[WallBracket, ...]:
    result = []
    for wall in WALLS:
        offset = wall.z - r
        if offset.denominator == 1 and offset >= 1:
            ledger.require(wall.k_lo > 2 * r, f"local wall {wall.key} above 2r for r={r}")
            result.append(wall)
    return tuple(result)


LOCAL_WALLS: dict[Q, tuple[WallBracket, ...]] = {}
for r in R_VALUES:
    events = local_walls(r)
    LOCAL_WALLS[r] = events
    ledger.require(tuple(w.key for w in events) == EXPECTED_LOCAL[r], f"local wall list r={r}")

    # At K=2r every later sample is below its first count wall.  Thus each
    # crossed wall raises exactly one later-sample bracket by one, and M is
    # the number of crossed local events.  The dictionary also checks that
    # the levels for each individual sample are consecutive.
    crossed: dict[Q, int] = {}
    for index, wall in enumerate(events, start=1):
        previous = crossed.get(wall.z, 0)
        ledger.require(wall.level == previous + 1, f"consecutive sample levels r={r}, z={wall.z}")
        crossed[wall.z] = wall.level
        m_value = sum(crossed.values())
        ledger.require(m_value == index, f"post-wall M={index} at r={r}, wall={wall.key}")

    k_endpoint = 2 * r
    z_first_later = r + 1
    if r <= 3:
        # The first sample itself is below 3/4 at K=2r (checked below),
        # and G is decreasing in z, so every later sample has zero count.
        ledger.require(z_first_later > r, f"later samples follow first sample r={r}")
    elif z_first_later < k_endpoint:
        _, endpoint_later_upper = g_bounds(k_endpoint, z_first_later)
        ledger.require(endpoint_later_upper < Q(3, 4), f"M starts at zero for r={r}")
    else:
        ledger.require(z_first_later >= k_endpoint, f"zero-extended first later sample r={r}")


# First-sample state at the lower endpoint.
for r in R_VALUES:
    if r <= 3:
        ledger.require(2 * r * OMEGA_HI < Q(3, 4), f"zero endpoint count for r={r}")
    else:
        ledger.require(2 * r * OMEGA_LO > Q(3, 4), f"positive endpoint count for r={r}")
        ledger.require(2 * r * OMEGA_HI < Q(7, 4), f"endpoint first count equals one for r={r}")


# ---------------------------------------------------------------------------
# Positivity, activation, endpoint, and minimum comparisons
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FirstWallClaim:
    r: Q
    lower: Q
    upper: Q


FIRST_CLAIMS = (
    FirstWallClaim(Q(1, 2), Q(3, 20), Q(8, 25)),
    FirstWallClaim(Q(1), Q(17, 100), Q(1, 2)),
    FirstWallClaim(Q(3, 2), Q(9, 25), Q(53, 100)),
    FirstWallClaim(Q(2), Q(2, 5), Q(29, 50)),
    FirstWallClaim(Q(5, 2), Q(23, 50), Q(63, 100)),
    FirstWallClaim(Q(3), Q(13, 25), Q(69, 100)),
    FirstWallClaim(Q(7, 2), Q(29, 50), Q(19, 25)),
    FirstWallClaim(Q(4), Q(33, 50), Q(83, 100)),
)

first_upper_claim: dict[Q, Q] = {}
for claim in FIRST_CLAIMS:
    first = LOCAL_WALLS[claim.r][0]
    ledger.require(first.key == (claim.r + 1, 1), f"first later wall is G_K(r+1)=3/4 for r={claim.r}")
    h_lo, _ = h_bounds(first.k_lo, claim.r)
    _, h_hi = h_bounds(first.k_hi, claim.r)
    ledger.require(h_lo - 2 > claim.lower, f"positive first-wall lower bound r={claim.r}")
    ledger.require(h_hi - 2 < claim.upper, f"first-wall upper comparison r={claim.r}")
    ledger.require(claim.lower >= Q(3, 20), f"uniform 3/20 first-wall margin r={claim.r}")
    first_upper_claim[claim.r] = claim.upper


# For r <= 3, T_K(r)=0 before the first-sample activation wall.  At the
# listed rational point G_k(r)<3/4, so the activation wall lies to its right;
# monotonicity of H gives the displayed positive lower bound there.
ACTIVATION = {
    Q(1, 2): (Q(3), Q(11, 25)),
    Q(1): (Q(37, 10), Q(14, 25)),
    Q(3, 2): (Q(22, 5), Q(69, 100)),
    Q(2): (Q(5), Q(37, 50)),
    Q(5, 2): (Q(57, 10), Q(22, 25)),
    Q(3): (Q(63, 10), Q(47, 50)),
}

for r, (k_test, activation_claim) in ACTIVATION.items():
    ledger.require(k_test > 2 * r, f"activation test lies in residual range r={r}")
    _, g_upper = g_bounds(k_test, r)
    ledger.require(g_upper < Q(3, 4), f"activation wall is right of test point r={r}")
    h_lower, _ = h_bounds(k_test, r)
    ledger.require(h_lower > activation_claim, f"activation lower bound r={r}")
    ledger.require(first_upper_claim[r] < activation_claim, f"first later wall below activation candidate r={r}")


# Every wall after the first is evaluated at the rational left endpoint of
# its bracket.  The following common lower bound is valid for all such walls
# at the given shift.
OTHER_LATER_CLAIM = {
    Q(1, 2): Q(13, 20),
    Q(1): Q(7, 10),
    Q(3, 2): Q(37, 50),
    Q(2): Q(39, 50),
    Q(5, 2): Q(81, 100),
    Q(3): Q(17, 20),
}

# Some comparison margins use a sharper rational point inside the coarse
# wall-isolation bracket.  Its being left of the wall is certified again by
# the same exact G upper envelope.
WALL_EVAL_LEFT = {
    (Q(5, 2), 1): Q(143, 25),
    (Q(3), 1): Q(317, 50),
    (Q(7, 2), 1): Q(139, 20),
    (Q(4), 1): Q(151, 20),
    (Q(9, 2), 1): Q(407, 50),
    (Q(5), 1): Q(873, 100),
    (Q(3, 2), 2): Q(77, 10),
    (Q(2), 2): Q(839, 100),
    (Q(5, 2), 2): Q(907, 100),
}

for r, common_claim in OTHER_LATER_CLAIM.items():
    for m_value, wall in enumerate(LOCAL_WALLS[r][1:], start=2):
        eval_k = WALL_EVAL_LEFT.get(wall.key, wall.k_lo)
        ledger.require(
            wall.k_lo <= eval_k < wall.k_hi,
            f"wall evaluation point lies in left bracket r={r}, wall={wall.key}",
        )
        _, g_eval_upper = g_bounds(eval_k, wall.z)
        ledger.require(
            g_eval_upper < wall.target,
            f"wall evaluation point is left of root r={r}, wall={wall.key}",
        )
        h_lower, _ = h_bounds(eval_k, r)
        ledger.require(
            h_lower - 2 * m_value > common_claim,
            f"other later-wall lower bound r={r}, wall={wall.key}, M={m_value}: "
            f"got {h_lower - 2 * m_value}, need > {common_claim}",
        )
    ledger.require(first_upper_claim[r] < common_claim, f"first wall beats all later walls r={r}")


def endpoint_h_lower(r: Q) -> Q:
    """Lower bound for H_r(2r), using sqrt(3)<26/15 and pi>333/106."""

    return (
        r * r
        + r / 3
        - Q(1, 4)
        - (3 * r * r / 2 + r) * SQRT3_HI / PI_LO
    )


ENDPOINT_CLAIMS = {
    Q(7, 2): (Q(109, 100), Q(1096, 999)),
    Q(4): (Q(163, 100), Q(32653, 19980)),
    Q(9, 2): (Q(1253, 555), Q(1253, 555)),
}

for r, (claim, exact_lower) in ENDPOINT_CLAIMS.items():
    computed = endpoint_h_lower(r)
    ledger.require(computed == exact_lower, f"exact endpoint lower expression r={r}")
    if r < Q(9, 2):
        ledger.require(computed > claim, f"endpoint comparison r={r}")
        ledger.require(first_upper_claim[r] < claim, f"first wall beats endpoint r={r}")
    else:
        ledger.require(computed > 0, "positive r=9/2 endpoint")
        ledger.require(not LOCAL_WALLS[r], "r=9/2 has no later wall")


print(f"PASS: {ledger.count} exact integer/Fraction checks")
print("walls=11; shifts=9; controlling wall G_K(r+1)=3/4 for r<=4")
print("uniform positive-count margin E_r(K)>3/20 for r<=4")
print("r=9/2 endpoint lower bound: 1253/555")
