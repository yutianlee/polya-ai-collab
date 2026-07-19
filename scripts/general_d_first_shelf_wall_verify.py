#!/usr/bin/env python3
"""Arb audit of the ten residual first-shelf wall chambers.

This script verifies the positive continuous certificate

    C = p(a+b) + (n-p)(b+u) + alpha(u+h) + h^2/c - (1+2p)

on the post-crossing wall b=A(r+p)=3/4 for the ten diagnostic chambers
listed in ``human/outbox/general-d-round-02-terminal-reserve.md``.  Here

    q=r+n, alpha=mu-q, a=A(r), u=A(q),
    h=G_K(mu), c=acos(mu/K)/pi, A=G_K-G_mu.

For fixed mu, the wall has a unique K and K(mu) is increasing.  Each exact
rational mu subinterval is therefore enclosed using independently isolated
roots at its two endpoints.  All transcendental evaluations and every sign
decision use python-flint Arb ball arithmetic.  Floating point is used only
for human-readable output.

The certificate applies to the F_0=1, p<n branch.  It intentionally says
nothing about p=n, whose outer samples belong to D_A(q).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = 384
PI = arb.pi()
THREE_QUARTERS = arb(fmpq(3, 4))
ROOT_STEPS = 110
SUBDIVISIONS = 256


def A(q: fmpq | int) -> arb:
    return arb(q)


def interval_ball(lo: fmpq, hi: fmpq) -> arb:
    if hi < lo:
        raise AssertionError("reversed interval")
    if lo == hi:
        return A(lo)
    mid, rad = (lo + hi) / 2, (hi - lo) / 2
    out = arb(str(mid), str(rad))
    if not out.contains(A(lo)) or not out.contains(A(hi)):
        raise AssertionError("interval constructor lost an endpoint")
    return out


def g_point(radius: fmpq, z: fmpq) -> arb:
    if radius < z:
        return arb(0)
    if radius == z:
        return arb(0)
    R, Z = A(radius), A(z)
    return ((R * R - Z * Z).sqrt() - Z * (Z / R).acos()) / PI


def g_fixed(radius: arb, z: fmpq) -> arb:
    Z = A(z)
    if not (radius > Z):
        raise AssertionError(f"radius interval is not above fixed z={z}")
    return ((radius * radius - Z * Z).sqrt() - Z * (Z / radius).acos()) / PI


def g_monotone_hull(radius_lo: fmpq, radius_hi: fmpq, z: fmpq) -> arb:
    """Range hull of G_radius(z), using monotonicity in the radius."""

    if radius_lo < z:
        raise AssertionError("radius hull starts below the fixed sample")
    return g_point(radius_lo, z).union(g_point(radius_hi, z))


def g_outer_at_inner(k: arb, mu: arb) -> arb:
    if not (k > mu):
        raise AssertionError("K interval is not strictly above mu interval")
    return ((k * k - mu * mu).sqrt() - mu * (mu / k).acos()) / PI


def wall_value(k: fmpq, mu: fmpq, x: fmpq) -> arb:
    return g_point(k, x) - g_point(mu, x) - THREE_QUARTERS


def isolate_wall(mu: fmpq, x: fmpq) -> tuple[fmpq, fmpq]:
    """Isolate the unique root of A(x)=3/4 at fixed exact mu."""

    lo = mu
    if not (wall_value(lo, mu, x) < 0):
        raise AssertionError("wall function is not negative at K=mu")
    hi = mu + 1
    while wall_value(hi, mu, x) < 0:
        hi += 1
        if hi > mu + 100:
            raise AssertionError("wall root was not found below mu+100")
    if not (wall_value(hi, mu, x) > 0):
        raise AssertionError("could not decide upper wall sign")

    for _ in range(ROOT_STEPS):
        mid = (lo + hi) / 2
        value = wall_value(mid, mu, x)
        if value < 0:
            lo = mid
        elif value > 0:
            hi = mid
        else:
            raise AssertionError("insufficient precision in wall isolation")

    if not (wall_value(lo, mu, x) < 0 and wall_value(hi, mu, x) > 0):
        raise AssertionError("root bracket lost its strict endpoint signs")
    return lo, hi


@dataclass(frozen=True)
class Chamber:
    n: int
    p: int
    r: fmpq

    @property
    def q(self) -> fmpq:
        return self.r + self.n

    @property
    def x(self) -> fmpq:
        return self.r + self.p

    @property
    def label(self) -> str:
        return f"(n,p,r)=({self.n},{self.p},{self.r})"


CHAMBERS = (
    Chamber(4, 3, fmpq(1, 2)),
    Chamber(5, 4, fmpq(1, 2)),
    Chamber(5, 4, fmpq(1)),
    Chamber(6, 5, fmpq(1, 2)),
    Chamber(6, 5, fmpq(1)),
    Chamber(7, 6, fmpq(1, 2)),
    Chamber(7, 6, fmpq(1)),
    Chamber(8, 6, fmpq(1, 2)),
    Chamber(8, 7, fmpq(1, 2)),
    Chamber(9, 7, fmpq(1, 2)),
)

# Rational wall points at which the deliberately weakened certificate from
# (27)--(28) is strictly negative.  These are witnesses that every chamber
# in CHAMBERS is genuinely needed; they do not assert global exhaustion.
WEAK_WITNESS_ALPHA = (
    fmpq(67, 256),
    fmpq(82, 256),
    fmpq(85, 256),
    fmpq(101, 256),
    fmpq(105, 256),
    fmpq(126, 256),
    fmpq(131, 256),
    fmpq(0),
    fmpq(158, 256),
    fmpq(0),
)


def J(mu: arb, z: fmpq) -> arb:
    """Primitive J_mu(z)=1/2(z sqrt(mu^2-z^2)+mu^2 asin(z/mu))."""

    Z = A(z)
    return (Z * (mu * mu - Z * Z).sqrt() + mu * mu * (Z / mu).asin()) / 2


def weak_certificate_witness(ch: Chamber, alpha: fmpq) -> arb:
    """Evaluate the weakened first-drop/envelope certificate at one wall."""

    mu_q = ch.q + alpha
    k_lo, k_hi = isolate_wall(mu_q, ch.x)
    k = interval_ball(k_lo, k_hi)
    mu = A(mu_q)
    y = ch.x + 1

    a = g_fixed(k, ch.r) - g_point(mu_q, ch.r)
    v = g_fixed(k, y) - g_point(mu_q, y)
    lam = (k - mu) / (PI * mu)
    sy = (mu * mu - A(y) * A(y)).sqrt()
    h0 = v - lam * sy
    if not (h0 > 0):
        raise AssertionError(
            f"weak witness did not lie in the positive-interface branch: "
            f"{ch.label}, alpha={alpha}, h0={h0}"
        )
    c = (mu / k).acos() / PI
    envelope = (
        2 * (h0 * (mu - A(y)) + lam * (PI * mu * mu / 4 - J(mu, y)))
        + h0 * h0 / c
    )
    b = THREE_QUARTERS
    return ch.p * (a + b) + (b + v) + envelope - (1 + 2 * ch.p)


def certificate(ch: Chamber, mu_lo: fmpq, mu_hi: fmpq,
                k_lo: fmpq, k_hi: fmpq) -> arb:
    """Natural interval extension of C on one wall segment."""

    mu = interval_ball(mu_lo, mu_hi)
    k = interval_ball(k_lo, k_hi)
    if not (k > mu):
        raise AssertionError("wall enclosure does not separate K from mu")

    # Endpoint hulls are tighter than natural interval evaluation and allow
    # the first mu box to own the exact endpoint mu=q, where G_mu(q)=0.
    a = (
        g_monotone_hull(k_lo, k_hi, ch.r)
        - g_monotone_hull(mu_lo, mu_hi, ch.r)
    )
    u = (
        g_monotone_hull(k_lo, k_hi, ch.q)
        - g_monotone_hull(mu_lo, mu_hi, ch.q)
    )
    h = g_outer_at_inner(k, mu)
    c = (mu / k).acos() / PI
    alpha = mu - A(ch.q)
    if not (c > 0):
        raise AssertionError("nonpositive slope interval")
    # The rational endpoints satisfy 0<=alpha<=1 exactly.  The Arb hull can
    # protrude by a rounding ulp at alpha=0 or 1; retaining that protrusion is
    # conservative in the certificate evaluation.

    b = THREE_QUARTERS  # exact on the isolated wall
    return (
        ch.p * (a + b)
        + (ch.n - ch.p) * (b + u)
        + alpha * (u + h)
        + h * h / c
        - (1 + 2 * ch.p)
    )


def main() -> None:
    print("GENERAL-d FIRST-SHELF WALL CERTIFICATE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print(f"mu subdivisions per chamber={SUBDIVISIONS}")
    print("All sign decisions below are directed-rounding Arb decisions.\n")

    total_boxes = 0
    global_seed = None
    for ch in CHAMBERS:
        endpoints = [ch.q + fmpq(j, SUBDIVISIONS) for j in range(SUBDIVISIONS + 1)]
        roots = [isolate_wall(mu, ch.x) for mu in endpoints]

        chamber_seed = float("inf")
        for j in range(SUBDIVISIONS):
            mu_lo, mu_hi = endpoints[j], endpoints[j + 1]
            # K(mu) is increasing: dK/dmu=-(partial_mu A)/(partial_K A)>0.
            k_lo = roots[j][0]
            k_hi = roots[j + 1][1]
            value = certificate(ch, mu_lo, mu_hi, k_lo, k_hi)
            if not (value > 0):
                raise AssertionError(
                    f"nonpositive/unresolved box {ch.label}, j={j}, "
                    f"mu=[{mu_lo},{mu_hi}], C={value}"
                )
            chamber_seed = min(chamber_seed, float(value.mid()))
            global_seed = chamber_seed if global_seed is None else min(global_seed, chamber_seed)
            total_boxes += 1

        print(
            f"PASS {ch.label:20s}: mu in [{ch.q},{ch.q + 1}], "
            f"wall A({ch.x})=3/4, smallest box midpoint ~{chamber_seed:.9f}"
        )

    print()
    print(
        f"CERTIFIED: C>0 on all {total_boxes} wall boxes in all "
        f"{len(CHAMBERS)} chambers."
    )
    print(f"Smallest interval midpoint seed (non-rigorous display only): {global_seed:.9f}")

    print("\nRigorous negative witnesses for the weakened terminal envelope:")
    for ch, alpha in zip(CHAMBERS, WEAK_WITNESS_ALPHA, strict=True):
        value = weak_certificate_witness(ch, alpha)
        if not (value < 0):
            raise AssertionError(
                f"weak certificate witness was not strictly negative: "
                f"{ch.label}, alpha={alpha}, W={value}"
            )
        print(
            f"PASS {ch.label:20s}: alpha={alpha}, "
            f"W midpoint ~{float(value.mid()):.9f}"
        )
    print(
        f"CERTIFIED: every one of the {len(CHAMBERS)} listed chambers has "
        "a strict weakened-certificate failure."
    )


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
