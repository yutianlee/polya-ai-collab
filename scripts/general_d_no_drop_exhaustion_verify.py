#!/usr/bin/env python3
"""Arb replay for the global high-floor no-drop exhaustion.

This script certifies the finite numerical comparisons used in
``human/outbox/general-d-round-04-no-drop-exhaustion.md``.  The analytic
part of that note reduces every unresolved no-drop tail to one of two
sets of necessary inequalities.  Outward Arb arithmetic then proves:

* the central set has no pair with f >= 50 and every surviving pair has
  f <= 49, n <= 48;
* outside the two asymptotic floors f=2,3, the outer set has no pair with
  f >= 9 and every surviving pair has f <= 8, n <= 39; and
* the limiting coefficient comparison permits escape precisely for
  f=2,3, and excludes it for every f >= 4.

No floating-point value is used in an assertion.  Run from the repository
root with

    python scripts/general_d_no_drop_exhaustion_verify.py
"""

from __future__ import annotations

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this Arb certificate") from exc


ctx.prec = 256
PI = arb.pi()
HALF = arb(fmpq(1, 2))
QUARTER = arb(fmpq(1, 4))
CSTAR = 4 * arb(2).sqrt() / 15
C0 = (PI / 12).root(3)


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(statement: bool, message: str) -> None:
    if not statement:
        raise AssertionError(message)


def build_sums(limit: int) -> list[arb]:
    sums = [arb(0)]
    for k in range(1, limit + 1):
        sums.append(sums[-1] + arb(fmpq(4 * k - 1, 4)) ** fmpq(-1, 3))
    return sums


MAX_CENTRAL_F = 34595
S = build_sums(MAX_CENTRAL_F)


def cutoff(n: int, q_level: int) -> arb:
    """The weak (B=Q) no-drop cutoff K_nd(n,Q)."""

    numerator = A(q_level) + A(n) / 2 + CSTAR
    return (numerator / (C0 * S[q_level])) ** 3


def d_central(n: int, f: int) -> arb:
    numerator = A(f) + HALF + A(fmpq(1, 4 * n))
    denominator = 1 / PI - A(fmpq(1, 4 * n))
    return numerator / denominator


def u_action(delta: arb, f: int) -> arb:
    b = A(f) - QUARTER
    return 2 * delta * delta * (delta + 1) / (PI * PI * b * b)


def central_excluded_by_geometry(n: int, f: int) -> bool:
    b = A(f) - QUARTER
    left = b * n * (n + 1)
    right = u_action(d_central(n, f), f) ** 2
    return left >= right


def cutoff_excluded(n: int, f: int, q_level: int) -> bool:
    lower_k = PI * (A(f) - QUARTER) + n + HALF
    return lower_k >= cutoff(n, q_level)


# Integral lower bound S_Q >= (5/4) Q^(2/3): its normalized integral
# lower bound is increasing, so the single Q=7 check is sufficient.
q = 7
integral_lower = A(fmpq(3, 2)) * (
    A(fmpq(4 * q + 3, 4)) ** fmpq(2, 3)
    - A(fmpq(3, 4)) ** fmpq(2, 3)
)
require(
    integral_lower >= A(fmpq(5, 4)) * A(q) ** fmpq(2, 3),
    "failed the S_Q >= (5/4)Q^(2/3) base check",
)


# The normalized automatic-cutoff inequality is increasing on the left and
# decreasing on the right, so checking f=16 certifies the analytic claim
# that a residual pair with f>=16 must have n>f/6.
f = 16
b = A(f) - QUARTER
left = A(fmpq(5, 4)) * (PI * PI / 12) ** fmpq(1, 3)
left *= (b / f) ** fmpq(1, 3) * A(fmpq(f - 1, f)) ** fmpq(2, 3)
right = A(fmpq(13, 12)) + CSTAR / f
require(left > right, "failed the f=16 automatic-cutoff base check")


# Central branch: for f>=50 the cutoff obstruction holds throughout
# 1<=n<=f-2.  For fixed f,Q, cutoff(n,Q)-[pi*b+n+1/2] is convex in n,
# so checking both endpoints suffices.  Geometry excludes n>=f-1 because
# its left side increases and its right side decreases with n.
central_checks = 0
for f in range(50, MAX_CENTRAL_F + 1):
    require(
        central_excluded_by_geometry(f - 1, f),
        f"central geometry did not exclude f={f}, n=f-1",
    )
    for q_level in (f - 1, f):
        require(
            cutoff_excluded(1, f, q_level),
            f"central cutoff endpoint n=1 failed at f={f}, Q={q_level}",
        )
        require(
            cutoff_excluded(f - 2, f, q_level),
            f"central cutoff endpoint n=f-2 failed at f={f}, Q={q_level}",
        )
        central_checks += 2


# Enumerate the remaining small central range until the monotone geometry
# obstruction begins.  A pair is retained if at least one endpoint value Q
# is not excluded by the weak cutoff.
central_pairs: list[tuple[int, int]] = []
for f in range(2, 50):
    n = 1
    while not central_excluded_by_geometry(n, f):
        if any(not cutoff_excluded(n, f, q_level) for q_level in (f - 1, f)):
            central_pairs.append((f, n))
        n += 1

require(central_pairs, "central enumeration unexpectedly empty")
require(max(f for f, _ in central_pairs) == 49, "central maximum f is not 49")
require(max(n for _, n in central_pairs) == 48, "central maximum n is not 48")


def c_floor(f: int) -> arb:
    b = A(f) - QUARTER
    return ((1 + b * b).sqrt() - 1) / 2


def outer_lower(n: int, f: int) -> tuple[arb, bool]:
    """L_{n,f}; second return says delta_min=c_f*n-1 is active."""

    c = c_floor(f)
    active = c * n - 1 >= PI * (A(f) - QUARTER)
    delta_min = c * n - 1 if active else PI * (A(f) - QUARTER)
    value = delta_min * delta_min * n * n
    value /= 2 * PI * PI * (delta_min + n + 1)
    return value, active


def outer_excluded(n: int, f: int, q_level: int) -> tuple[bool, bool]:
    lower, active = outer_lower(n, f)
    return lower >= cutoff(n, q_level), active


# Limiting comparison.  gamma_f is increasing in f, whereas beta_B is
# decreasing in B.  The three assertions prove that escape is allowed by
# these necessary bounds for f=2,3 and forbidden for every f>=4.
def gamma(f: int) -> arb:
    c = c_floor(f)
    return c * c / (2 * PI * PI * (c + 1))


def beta(levels: int) -> arb:
    return 1 / (8 * (C0 * S[levels]) ** 3)


require(gamma(2) < beta(2), "f=2 limiting ray was unexpectedly excluded")
require(gamma(3) < beta(3), "f=3 limiting ray was unexpectedly excluded")
require(gamma(4) > beta(3), "f=4 limiting ray was not excluded")


# The analytic coarse estimate in the note excludes f>=67 in the outer
# branch.  For 4<=f<=66, scan until both Q choices have failed after the
# c_f*n-1 branch becomes active.  Dividing by n^3 then makes the lower side
# increasing and the cutoff side decreasing, so failure persists forever.
outer_pairs: list[tuple[int, int]] = []
outer_checks = 0
for f in range(4, 67):
    q_levels = (f - 1, f)
    done = {q_level: False for q_level in q_levels}
    n = 1
    while not all(done.values()):
        retained = False
        for q_level in q_levels:
            excluded, active = outer_excluded(n, f, q_level)
            outer_checks += 1
            if excluded and active:
                done[q_level] = True
            if not excluded and not cutoff_excluded(n, f, q_level):
                retained = True
        if retained:
            outer_pairs.append((f, n))
        n += 1
        require(n < 10000, f"outer monotone tail was not reached for f={f}")

require(outer_pairs, "outer finite enumeration unexpectedly empty")
require(max(f for f, _ in outer_pairs) == 8, "outer finite maximum f is not 8")
require(max(n for _, n in outer_pairs) == 39, "outer finite maximum n is not 39")


print("PASS: global high-floor no-drop exhaustion certified with Arb")
print(f"precision: {ctx.prec} bits")
print(f"central endpoint comparisons: {central_checks}")
print(f"central retained necessary pairs: {len(central_pairs)}")
print("central box: 2 <= f <= 49, 1 <= n <= 48")
print(f"outer comparisons: {outer_checks}")
print(f"outer retained finite necessary pairs: {len(set(outer_pairs))}")
print("outer finite box: 4 <= f <= 8, 1 <= n <= 39")
print("only noncompact limiting floors: f=2,3")
