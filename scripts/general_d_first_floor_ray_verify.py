#!/usr/bin/env python3
"""Rigorous Arb certificate for the large first-floor wall ray.

The script proves positivity of the weakened first-drop certificate on the
continuous relaxation

    x >= 100,  r >= 3/2,  s in {0,1},  alpha in [0,1],

at the implicit wall A(x)=3/4.  The actual half-integral/integral chamber
parameters are a subset of this relaxation.  It uses only directed-rounding
``python-flint`` Arb arithmetic; binary floating point appears only in
diagnostic output and in the heuristic choice of a subdivision coordinate.

The compact variables are

    t=x^(-1/3),  kappa=t(K-mu),  P=tp,  beta=mu-x=s+1+alpha.

The wall root is never evaluated numerically.  Composite two-panel
trapezoid and midpoint bounds for the concave radius profile enclose it.
Every accepted box is proved either to miss the wall, to have A(r)>=5/4,
or to have a strictly positive scaled certificate tW.
"""

from __future__ import annotations

import heapq
import itertools
import sys
from dataclasses import dataclass
from functools import lru_cache

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


ctx.prec = 384
PI = arb.pi()
Q0 = arb(0)
Q1 = arb(1)
QUARTER = arb(fmpq(1, 4))
THREE_QUARTERS = arb(fmpq(3, 4))
FIVE_QUARTERS = arb(fmpq(5, 4))

# A rational enlargement of 100^(-1/3).  It corresponds to
# x >= 99.9992606..., so a certificate on this box covers x>=100.
T_MAX = fmpq(53861, 250000)

# Safe rational consequences of the exact wall integral; checked below.
KAPPA_MIN = fmpq(22, 25)       # 0.88
KAPPA_MAX = fmpq(731, 250)     # 2.924
P_MAX = fmpq(41)

MAX_DEPTH = 80
MAX_BOXES = 2_000_000


def A(q: fmpq | int) -> arb:
    return arb(q)


def interval_ball(lo: fmpq, hi: fmpq) -> arb:
    """Return an Arb ball containing the exact rational interval [lo,hi]."""

    if hi < lo:
        raise AssertionError("reversed interval")
    if lo == hi:
        return A(lo)
    mid, rad = (lo + hi) / 2, (hi - lo) / 2
    out = arb(str(mid), str(rad))
    if not out.contains(A(lo)) or not out.contains(A(hi)):
        raise AssertionError("interval constructor lost an endpoint")
    return out


def lower(x: arb) -> arb:
    return x.lower()


def upper(x: arb) -> arb:
    return x.upper()


def semipositive_sqrt(x: arb) -> arb:
    """Square root when the exact expression is known nonnegative.

    A symmetric Arb hull for an interval with exact lower endpoint zero can
    protrude by one radius ulp below zero.  In that sole situation ordinary
    ``sqrt`` returns ``nan``.  The hull [0,sqrt(upper(x))] is the rigorous
    interval extension dictated by the proved nonnegativity.
    """

    if x >= 0:
        return x.sqrt()
    if upper(x) < 0:
        raise ArithmeticError("negative semipositive radicand")
    return arb(0).union(upper(x).sqrt())


def phi(t: arb, w: arb) -> arb:
    """Stable f_x/t at a radius node w=t(R-x)."""

    t2 = t * t
    return semipositive_sqrt(w * (2 + t2 * w)) / (1 + t2 * w)


def psi(t: arb, P: arb, w: arb) -> arb:
    """Stable f_r/t, where r=x-p and P=tp."""

    t2 = t * t
    radicand = (w + P) * (2 + t2 * (w - P))
    return semipositive_sqrt(radicand) / (1 + t2 * w)


def chi(t: arb, beta: arb, kappa: arb, xi: fmpq) -> arb:
    """Stable f_y/t, where y=x+1."""

    X = A(xi)
    w = beta * t + X * kappa
    minus = (beta - 1) * t + X * kappa
    plus = (beta + 1) * t + X * kappa
    t2 = t * t
    radicand = minus * (2 + t2 * plus)
    return semipositive_sqrt(radicand) / (1 + t2 * w)


def node_w(t: arb, beta: arb, kappa: arb, xi: fmpq) -> arb:
    return beta * t + A(xi) * kappa


def trap_phi(t: arb, beta: arb, kappa: arb) -> arb:
    f0 = phi(t, node_w(t, beta, kappa, fmpq(0)))
    fm = phi(t, node_w(t, beta, kappa, fmpq(1, 2)))
    f1 = phi(t, node_w(t, beta, kappa, fmpq(1)))
    return (f0 + 2 * fm + f1) / 4


def mid_phi(t: arb, beta: arb, kappa: arb) -> arb:
    f1 = phi(t, node_w(t, beta, kappa, fmpq(1, 4)))
    f2 = phi(t, node_w(t, beta, kappa, fmpq(3, 4)))
    return (f1 + f2) / 2


def trap_psi(t: arb, beta: arb, kappa: arb, P: arb) -> arb:
    f0 = psi(t, P, node_w(t, beta, kappa, fmpq(0)))
    fm = psi(t, P, node_w(t, beta, kappa, fmpq(1, 2)))
    f1 = psi(t, P, node_w(t, beta, kappa, fmpq(1)))
    return (f0 + 2 * fm + f1) / 4


def trap_chi(t: arb, beta: arb, kappa: arb) -> arb:
    f0 = chi(t, beta, kappa, fmpq(0))
    fm = chi(t, beta, kappa, fmpq(1, 2))
    f1 = chi(t, beta, kappa, fmpq(1))
    return (f0 + 2 * fm + f1) / 4


@dataclass(frozen=True)
class Box:
    t0: fmpq
    t1: fmpq
    b0: fmpq
    b1: fmpq
    p0: fmpq
    p1: fmpq
    k0: fmpq
    k1: fmpq
    depth: int = 0

    def split(self, coordinate: str) -> tuple["Box", "Box"]:
        lo = getattr(self, coordinate + "0")
        hi = getattr(self, coordinate + "1")
        mid = (lo + hi) / 2
        left = self.__dict__.copy()
        right = self.__dict__.copy()
        left[coordinate + "1"] = mid
        right[coordinate + "0"] = mid
        left["depth"] = self.depth + 1
        right["depth"] = self.depth + 1
        return Box(**left), Box(**right)


def scaled_width(lo: fmpq, hi: fmpq, scale: float) -> float:
    return float(A(hi - lo)) / scale


def choose_split(box: Box, reason: str) -> str:
    """Heuristic only; it cannot affect the validity of accepted boxes."""

    widths = {
        "t": scaled_width(box.t0, box.t1, float(A(T_MAX))),
        "b": scaled_width(box.b0, box.b1, 1.0),
        "p": scaled_width(box.p0, box.p1, float(A(P_MAX))),
    }
    if reason == "wall":
        widths["p"] *= 0.10
    elif reason == "certificate":
        widths["p"] *= 2.0
    return max(widths, key=widths.get)


@lru_cache(maxsize=None)
def wall_kappa_enclosure(
    t0: fmpq, t1: fmpq, b0: fmpq, b1: fmpq
) -> tuple[fmpq, fmpq] | None:
    """Enclose every wall root over one (t,beta) box.

    The lower search uses the midpoint upper bound: if even its upper
    endpoint is below 3/4, every true wall root is larger.  The upper search
    uses the trapezoid lower bound analogously.  Failure to obtain the upper
    test asks the outer branch-and-bound to split (t,beta).
    """

    t = interval_ball(t0, t1)
    beta = interval_ball(b0, b1)
    lo, hi = KAPPA_MIN, KAPPA_MAX

    # Largest certified common lower bound.
    a, b = lo, hi
    for _ in range(18):
        m = (a + b) / 2
        km = A(m)
        value = km * mid_phi(t, beta, km) / PI
        if upper(value) < THREE_QUARTERS:
            a = m
        else:
            b = m
    root_lo = a

    # Smallest certified common upper bound.
    a, b = root_lo, hi
    endpoint = A(b) * trap_phi(t, beta, A(b)) / PI
    if not (lower(endpoint) > THREE_QUARTERS):
        return None
    for _ in range(18):
        m = (a + b) / 2
        km = A(m)
        value = km * trap_phi(t, beta, km) / PI
        if lower(value) > THREE_QUARTERS:
            b = m
        else:
            a = m
    return root_lo, b


def exact_cone_checks() -> None:
    """Certify the rational compact cone used by the branch-and-bound."""

    C = ((9 * PI * arb(2).sqrt()) / 8).root(3) ** 2
    if not (C < A(KAPPA_MAX)):
        raise AssertionError(f"upper delta constant unresolved: C={C}")

    B = C + 3 * A(T_MAX)
    B_BAR = A(fmpq(3571, 1000))
    if not (B < B_BAR):
        raise AssertionError(f"B upper bound unresolved: B={B}")

    D = (3 * PI / 4) / (2 * B).sqrt()
    if not (D > A(KAPPA_MIN)):
        raise AssertionError(f"lower delta constant unresolved: D={D}")

    CK = 1 + B_BAR * A(T_MAX) ** 2
    CK_BAR = A(fmpq(583, 500))
    if not (CK < CK_BAR):
        raise AssertionError(f"K/x bound unresolved: CK={CK}")

    # Under Delta<1/2, monotonicity of P/sqrt(P+B) gives
    # D0 P < pi CK0 sqrt((CK0+1)(P+B0)).  At P=41 the
    # reverse strict inequality holds, hence every possible failure has P<41.
    P0 = A(P_MAX)
    lhs = A(KAPPA_MIN) * P0
    rhs = PI * CK_BAR * ((CK_BAR + 1) * (P0 + B_BAR)).sqrt()
    if not (lhs > rhs):
        raise AssertionError(f"P=41 exclusion unresolved: lhs={lhs}, rhs={rhs}")

    # The rational t enlargement really covers x>=100.
    if not (A(T_MAX) > 1 / arb(100).root(3)):
        raise AssertionError("T_MAX does not cover 100^(-1/3)")

    # Positivity used in the factored compact profile Phi_r.
    if not (2 - A(P_MAX) * A(T_MAX) ** 2 > 0):
        raise AssertionError("compact Phi_r radicand factor is unresolved")

    print("PASS compact-cone constants (all Arb-directed):")
    print(f"  C={float(C.mid()):.12f} < {float(A(KAPPA_MAX)):.12f}")
    print(f"  D={float(D.mid()):.12f} > {float(A(KAPPA_MIN)):.12f}")
    print(f"  B={float(B.mid()):.12f}, K/x<{float(CK_BAR):.12f}, P<41")


def assess(box: Box) -> tuple[str, float]:
    """Assess a box; return (status, diagnostic_margin)."""

    t = interval_ball(box.t0, box.t1)
    beta = interval_ball(box.b0, box.b1)
    P = interval_ball(box.p0, box.p1)

    # The asserted ray has r>=3/2.  Since
    # r=t^(-3)-P/t, this is 1-Pt^2-(3/2)t^3>=0.
    domain = 1 - P * t * t - A(fmpq(3, 2)) * t * t * t
    if upper(domain) < 0:
        return "invalid", float(lower(-domain))

    bracket = wall_kappa_enclosure(box.t0, box.t1, box.b0, box.b1)
    if bracket is None:
        return "wall", float("-inf")
    k0, k1 = bracket
    kappa = interval_ball(k0, k1)

    try:
        ar = kappa * trap_psi(t, beta, kappa, P) / PI
        vy = kappa * trap_chi(t, beta, kappa) / PI
    except ArithmeticError:
        return "certificate", float("-inf")

    ar_lo = lower(ar)
    if ar_lo >= FIVE_QUARTERS:
        return "automatic", float(ar_lo - FIVE_QUARTERS)

    # From the wall and -A'(z)<=lambda*z/S_z,
    #   h=v-lambda*S_y >= 3/4-lambda*S_x =: H.
    # The following formulas are stable at t=0.
    t3 = t * t * t
    denom = 1 + beta * t3
    lambda_sx = (
        kappa
        * semipositive_sqrt(t)
        * semipositive_sqrt(beta * (2 + beta * t3))
        / (PI * denom)
    )
    H = THREE_QUARTERS - lambda_sx
    H_lo = lower(H)
    if not (H_lo > 0):
        return "certificate", float(H_lo)

    # c/t <= Q follows from acos(1/(1+u))=atan(sqrt((1+u)^2-1))
    # and atan(z)<=z.  Therefore t*h^2/c >= H^2/Q.
    vpar = kappa / denom
    Q = semipositive_sqrt(vpar * (2 + t * t * vpar)) / PI
    Q_hi = upper(Q)
    if not (Q_hi > 0):
        return "certificate", float("-inf")

    v_lo = lower(vy)
    L_lo = A(box.b0 - 1)
    terminal_bracket = v_lo - QUARTER + 2 * L_lo * H_lo

    # Bound the possibly negative P(A(r)-5/4) with the far P endpoint.
    defect = ar_lo - FIVE_QUARTERS
    p_term = A(box.p1) * defect if defect < 0 else A(box.p0) * defect

    # On this branch bracket is expected positive.  Use the correct t endpoint
    # in either sign, retaining rigor if a coarse box straddles zero.
    if terminal_bracket >= 0:
        t_term = A(box.t0) * terminal_bracket
    else:
        t_term = A(box.t1) * terminal_bracket
    outer = H_lo * H_lo / Q_hi
    cert = p_term + t_term + outer
    if cert > 0:
        return "positive", float(lower(cert))
    return "certificate", float(lower(cert))


def verify_sector(s: int) -> dict[str, int | float]:
    initial = Box(
        fmpq(0), T_MAX,
        fmpq(s + 1), fmpq(s + 2),
        fmpq(0), P_MAX,
        KAPPA_MIN, KAPPA_MAX,
    )

    counter = itertools.count()
    heap: list[tuple[float, int, Box]] = [(0.0, next(counter), initial)]
    counts: dict[str, int | float] = {
        "processed": 0,
        "invalid": 0,
        "miss-high": 0,
        "miss-low": 0,
        "automatic": 0,
        "positive": 0,
        "smallest-positive-margin": float("inf"),
        "max-depth": 0,
    }

    while heap:
        _, _, box = heapq.heappop(heap)
        counts["processed"] = int(counts["processed"]) + 1
        counts["max-depth"] = max(int(counts["max-depth"]), box.depth)
        if int(counts["processed"]) > MAX_BOXES:
            raise AssertionError(f"s={s}: exceeded MAX_BOXES")
        if int(counts["processed"]) % 250000 == 0:
            print(
                f"  progress s={s}: processed={counts['processed']}, "
                f"queued={len(heap)}, depth={counts['max-depth']}"
            )

        status, margin = assess(box)
        if status in ("invalid", "miss-high", "miss-low", "automatic", "positive"):
            counts[status] = int(counts[status]) + 1
            if status == "positive":
                counts["smallest-positive-margin"] = min(
                    float(counts["smallest-positive-margin"]), margin
                )
            continue

        if box.depth >= MAX_DEPTH:
            raise AssertionError(
                f"s={s}: unresolved depth-{box.depth} box {box}; "
                f"reason={status}, diagnostic margin={margin}"
            )
        coordinate = choose_split(box, status)
        left, right = box.split(coordinate)
        # Hard boxes (more negative diagnostic margin) are visited first.
        heapq.heappush(heap, (margin, next(counter), left))
        heapq.heappush(heap, (margin, next(counter), right))

    return counts


def main() -> None:
    print("GENERAL-d FIRST-FLOOR LARGE-RAY CERTIFICATE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print("All sign decisions are directed-rounding Arb decisions.\n")
    exact_cone_checks()

    grand_total = 0
    for s in (0, 1):
        counts = verify_sector(s)
        grand_total += int(counts["processed"])
        print(f"\nPASS s={s}, beta in [{s+1},{s+2}]")
        print(
            "  processed={processed}, miss-low={miss-low}, "
            "miss-high={miss-high}, invalid={invalid}, automatic={automatic}, "
            "positive={positive}, max-depth={max-depth}".format(**counts)
        )
        print(
            "  smallest accepted scaled-certificate lower endpoint "
            f"(diagnostic only) ~{counts['smallest-positive-margin']:.9g}"
        )

    print(
        "\nCERTIFIED: W>0 on the implicit first-floor wall for the "
        "continuous large-ray relaxation x>=100, r>=3/2, s=0,1."
    )
    print(f"Total branch-and-bound boxes processed: {grand_total}")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
