#!/usr/bin/env python3
"""Arb chamber certificate for the residual no-drop floors ``f >= 4``.

The global exhaustion certificate leaves 595 central pairs and 60 outer
pairs in these floors, with 45 overlaps.  Thus 610 distinct ``(f,n)``
pairs, and three one-sided action phases for each pair, remain.  This
driver reuses the exact shell/root and terminal-angle machinery in
``general_d_no_drop_compact_verify.py``.

Unlike the exceptional ``f=2,3`` rows, no small-sigma transfer is used.
The failed root-free cutoff itself supplies a positive lower sigma bound,
while physicality supplies an upper bound below one.  Consequently the
interval audit covers the whole range ``0 < sigma < 1``.

This file is a certificate driver, not a floating-point sampler.
"""

from __future__ import annotations

import argparse
import contextlib
import heapq
import io
import itertools
import runpy
import sys
from pathlib import Path

from flint import arb, ctx, fmpq


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import general_d_no_drop_compact_verify as core  # noqa: E402


PHASES = ("corner", "lower", "open")
SIGMA_BISECTIONS = 40
ORIGINAL_ACTION_BOUNDS = core.action_bounds


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def certified_pair_lists() -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    """Replay the exhaustion certificate and return its retained lists."""

    exhaustion = SCRIPT_DIR / "general_d_no_drop_exhaustion_verify.py"
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        data = runpy.run_path(str(exhaustion))
    transcript = captured.getvalue()
    require(
        "PASS: global high-floor no-drop exhaustion certified with Arb" in transcript,
        "the prerequisite exhaustion certificate did not pass",
    )
    central_all = set(data["central_pairs"])
    outer_all = set(data["outer_pairs"])
    require(len(central_all) == 649, "central prerequisite count changed")
    require(len(outer_all) == 60, "outer prerequisite count changed")

    central = {(f, n) for f, n in central_all if f >= 4 and n >= 2}
    outer = {(f, n) for f, n in outer_all if f >= 4 and n >= 2}
    require(len(central) == 595, "high-floor central count changed")
    require(len(outer) == 60, "high-floor outer count changed")
    require(len(central & outer) == 45, "central/outer overlap changed")
    require(len(central | outer) == 610, "high-floor union count changed")
    return central, outer


def kappa_max(f: int) -> fmpq:
    """Strict rational ceiling for kappa < 3*pi*f/2."""

    return fmpq(33 * f, 7)


def full_sigma_interval(f: int, n: int, phase: str) -> tuple[fmpq, fmpq] | None:
    """Localize every residual root without a small-sigma hypothesis."""

    cutoff = core.cutoff_arb(n, core.phase_Q(f, phase))

    # If K=kappa/sigma^3 is below the root-free cutoff and
    # kappa>=21/8, then cutoff*sigma^3>=21/8.  Retain a one-sided overlap
    # with the already-positive cutoff face by returning the last point
    # at which the strict reverse inequality is certified.
    lo, hi = fmpq(0), fmpq(1)
    if core.upper(cutoff) < A(core.KAPPA_MIN):
        return None
    for _ in range(SIGMA_BISECTIONS):
        mid = (lo + hi) / 2
        if core.upper(cutoff * A(mid) ** 3) < A(core.KAPPA_MIN):
            lo = mid
        else:
            hi = mid
    s0 = lo

    # Physicality requires mu>=n+1/2.  Even the a priori kappa ceiling
    # violates this near sigma=1.  Again keep the first certified
    # impossible point as a harmless overlap endpoint.
    lo, hi = s0, fmpq(1)
    threshold = A(fmpq(2 * n + 1, 2))
    require(
        core.upper(A(kappa_max(f)) * (1 - A(hi) ** 2) / A(hi) ** 3)
        < threshold,
        "sigma=1 did not exclude physicality",
    )
    for _ in range(SIGMA_BISECTIONS):
        mid = (lo + hi) / 2
        possible_mu = A(kappa_max(f)) * (1 - A(mid) ** 2) / A(mid) ** 3
        if core.upper(possible_mu) < threshold:
            hi = mid
        else:
            lo = mid
    s1 = hi
    if s1 <= s0:
        return None
    return s0, s1


def exact_action_bounds(
    sigma: arb,
    kappa: arb,
    shift: arb,
) -> tuple[arb, arb]:
    """Use the noncancelling positive series on every high-floor face."""

    value = core.exact_shell_at_shift(sigma, kappa, shift)
    return value, value


def root_action_bounds(
    sigma: arb,
    kappa: arb,
    alpha: arb,
) -> tuple[arb, arb]:
    """Intersect two independent rigorous enclosures of ``A(q)``.

    The exact positive-gap primitives are sharp on small boxes, while the
    noncancelling trapezoid/midpoint integral is much sharper on some wide
    high-floor seed boxes.  Taking the larger directed lower endpoint and
    smaller directed upper endpoint preserves rigor and avoids making the
    root localization depend on either representation's conditioning.
    """

    lows: list[arb] = []
    highs: list[arb] = []
    try:
        exact = core.exact_shell_at_q(sigma, kappa, alpha)
        if exact.is_finite():
            lows.append(core.lower(exact))
            highs.append(core.upper(exact))
    except (ArithmeticError, ZeroDivisionError):
        pass
    try:
        trap, midpoint = ORIGINAL_ACTION_BOUNDS(sigma, kappa, alpha)
        if trap.is_finite() and midpoint.is_finite():
            lows.append(core.lower(trap))
            highs.append(core.upper(midpoint))
    except (ArithmeticError, ZeroDivisionError):
        pass
    if not lows:
        raise ArithmeticError("both root-action enclosures failed")
    lo = max(lows)
    hi = min(highs)
    if lo > hi:
        raise ArithmeticError("independent root-action bounds are disjoint")
    return lo, hi


def exact_root_enclosure(
    f: int,
    s0: fmpq,
    s1: fmpq,
    a0: fmpq,
    a1: fmpq,
    e0: fmpq,
    e1: fmpq,
    _use_series: bool,
) -> tuple[str, fmpq | None, fmpq | None]:
    """Enclose every high-floor root from a certified interior seed.

    The low-floor core starts at kappa=21/8.  On a wide high-sigma box this
    can put q at or below zero even though every relevant floor root lies
    much higher.  The positive gap series is intentionally undefined there,
    and repeatedly splitting the parameter box merely traces that irrelevant
    boundary.

    Here ``13(f-1/4)/6`` is only a deterministic *candidate* seed.  It is
    used iff outward Arb arithmetic proves on the whole parameter box that
    its exact action is strictly below the target.  Thus no numerical
    conjecture about the root is imported into the certificate.  Subsequent
    bisections are the same monotone-kappa argument as in the core routine.
    """

    sigma = core.interval_ball(s0, s1)
    alpha = core.interval_ball(a0, a1)
    target = A(f) - A(fmpq(1, 4)) + core.interval_ball(e0, e1)
    seed = fmpq(13 * (4 * f - 1), 24)
    hi = core.KAPPA_MAX[f]
    if not (core.KAPPA_MIN < seed < hi):
        return "split", None, None
    # The gap formulas used below are invoked only where q=mu-alpha is
    # strictly positive.  Since mu decreases with sigma, this single exact
    # endpoint test covers the whole parameter box.
    seed_mu_at_s1 = A(seed) * (1 - A(s1) ** 2) / A(s1) ** 3
    hi_mu_at_s1 = A(hi) * (1 - A(s1) ** 2) / A(s1) ** 3
    if not (
        core.lower(seed_mu_at_s1 - A(a1)) > 0
        and core.lower(hi_mu_at_s1 - A(a1)) > 0
    ):
        return "split", None, None

    try:
        seed_lo, seed_hi = root_action_bounds(sigma, A(seed), alpha)
        hi_lo, hi_hi = root_action_bounds(sigma, A(hi), alpha)
    except (ArithmeticError, ZeroDivisionError):
        return "split", None, None

    # The seed is accepted only as a common strict lower bound for all
    # roots in the parameter box.  Failure merely requests subdivision.
    if not (seed_hi < core.lower(target)):
        return "split", None, None
    if hi_hi < core.lower(target):
        return "none", None, None

    a, b = seed, hi
    for _ in range(core.ROOT_STEPS):
        m = (a + b) / 2
        try:
            _, value_hi = root_action_bounds(sigma, A(m), alpha)
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if value_hi < core.lower(target):
            a = m
        else:
            b = m
    root_lo = a

    # If the common upper endpoint does not lie strictly above the target,
    # the a priori ceiling remains a safe upper enclosure for every root
    # that actually exists in the box.
    if not (hi_lo > core.upper(target)):
        return "ok", root_lo, hi
    a, b = root_lo, hi
    for _ in range(core.ROOT_STEPS):
        m = (a + b) / 2
        try:
            value_lo, _ = root_action_bounds(sigma, A(m), alpha)
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if value_lo > core.upper(target):
            b = m
        else:
            a = m
    return "ok", root_lo, b


def configure(precision: int, verbose: bool, max_boxes: int) -> None:
    require(precision >= 256, "precision must be at least 256 bits")
    ctx.prec = precision
    core.ctx.prec = precision
    core.PI = arb.pi()
    core.REPORT_PROGRESS = verbose
    core.MAX_BOXES_PER_CASE = max_boxes
    core.KAPPA_MAX.update({f: kappa_max(f) for f in range(4, 50)})
    core.initial_sigma_interval = full_sigma_interval
    # The low-floor core keeps a coarse quadrature path for most ordinary
    # cases.  On f>=4 the same exact positive gap series is both simpler
    # and substantially sharper, so expose it through the common
    # lower/upper-bound interface used by roots and endpoint actions.
    core.action_bounds = exact_action_bounds
    core.root_kappa_enclosure = exact_root_enclosure

    require(core.PI < A(fmpq(22, 7)), "pi<22/7 failed")
    for f in range(4, 50):
        require(
            A(core.KAPPA_MAX[f]) > 3 * core.PI * f / 2,
            f"kappa ceiling failed at f={f}",
        )


def verify_high_case(
    f: int,
    n: int,
    phase: str,
    sigma_panels: int,
    alpha_panels: int,
) -> dict[str, int | float]:
    """Run one case with a deterministic exact-rational seed grid."""

    sigma_range = full_sigma_interval(f, n, phase)
    if sigma_range is None:
        return {
            "processed": 0,
            "positive": 0,
            "pruned": 1,
            "max-depth": 0,
            "smallest-margin": float("inf"),
        }
    s0, s1 = sigma_range
    s_edges = [s0 + (s1 - s0) * fmpq(j, sigma_panels) for j in range(sigma_panels + 1)]
    if phase == "corner":
        a_edges = [fmpq(0), fmpq(0)]
    else:
        a_edges = [fmpq(j, alpha_panels) for j in range(alpha_panels + 1)]

    initial: list[core.Box] = []
    for j in range(sigma_panels):
        if phase == "corner":
            initial.append(
                core.Box(f, n, phase, s_edges[j], s_edges[j + 1], fmpq(0), fmpq(0), fmpq(0), fmpq(0))
            )
        else:
            for k in range(alpha_panels):
                initial.append(
                    core.Box(
                        f,
                        n,
                        phase,
                        s_edges[j],
                        s_edges[j + 1],
                        a_edges[k],
                        a_edges[k + 1],
                        fmpq(0),
                        fmpq(0),
                    )
                )

    counter = itertools.count()
    heap: list[tuple[float, int, core.Box]] = [
        (0.0, next(counter), box) for box in initial
    ]
    heapq.heapify(heap)
    out: dict[str, int | float] = {
        "processed": 0,
        "positive": 0,
        "pruned": 0,
        "max-depth": 0,
        "smallest-margin": float("inf"),
    }
    terminal = {
        "root-miss",
        "physical",
        "cutoff",
        "active",
        "upper-geometry",
        "slope-geometry",
        "width-geometry",
        "central-box",
        "outer-width",
        "outer-slope",
        "endpoint-floor",
        "endpoint-phase",
        "curvature-prune",
        "positive",
    }
    status_counts: dict[str, int] = {}
    while heap:
        _, _, box = heapq.heappop(heap)
        out["processed"] = int(out["processed"]) + 1
        out["max-depth"] = max(int(out["max-depth"]), box.depth)
        if int(out["processed"]) > core.MAX_BOXES_PER_CASE:
            raise AssertionError(
                f"box limit exceeded: f={f}, n={n}, phase={phase}; "
                f"queued={len(heap)}; statuses={status_counts}"
            )
        status, margin = core.assess(box)
        status_counts[status] = status_counts.get(status, 0) + 1
        if status in terminal:
            if status == "positive":
                out["positive"] = int(out["positive"]) + 1
                out["smallest-margin"] = min(float(out["smallest-margin"]), margin)
            else:
                out["pruned"] = int(out["pruned"]) + 1
            continue
        if box.depth >= core.MAX_DEPTH:
            raise AssertionError(
                f"unresolved depth {box.depth}: {box}; status={status}; margin={margin}"
            )
        coordinate = core.choose_split(box, "root" if status == "root" else "scalar")
        left, right = box.split(coordinate)
        heapq.heappush(heap, (margin, next(counter), left))
        heapq.heappush(heap, (margin, next(counter), right))
    return out


def audit_root_seed_grid(
    candidates: set[tuple[int, int]],
    phases: tuple[str, ...],
    sigma_panels: int,
    alpha_panels: int,
) -> None:
    """Certify the high-floor root seed on every requested seed box.

    This is a useful standalone replay of the localization handoff.  Once a
    parent seed box proves the strict inequality, every mathematical child
    is covered by it; the production root routine nevertheless repeats the
    directed test locally and never relies on this diagnostic summary.
    """

    checked = skipped = 0
    smallest = float("inf")
    smallest_q = float("inf")
    for f, n in sorted(candidates):
        target = A(f) - A(fmpq(1, 4))
        seed = fmpq(13 * (4 * f - 1), 24)
        for phase in phases:
            if phase == "corner":
                continue
            sigma_range = full_sigma_interval(f, n, phase)
            if sigma_range is None:
                skipped += 1
                continue
            s0, s1 = sigma_range
            s_edges = [
                s0 + (s1 - s0) * fmpq(j, sigma_panels)
                for j in range(sigma_panels + 1)
            ]
            a_edges = [fmpq(j, alpha_panels) for j in range(alpha_panels + 1)]
            for j in range(sigma_panels):
                sigma = core.interval_ball(s_edges[j], s_edges[j + 1])
                for k in range(alpha_panels):
                    alpha = core.interval_ball(a_edges[k], a_edges[k + 1])
                    seed_mu = A(seed) * (1 - A(s_edges[j + 1]) ** 2)
                    seed_mu /= A(s_edges[j + 1]) ** 3
                    q_margin = core.lower(seed_mu - A(a_edges[k + 1]))
                    require(
                        q_margin > 0,
                        f"root seed left q>0 at f={f}, n={n}, "
                        f"phase={phase}, sigma-panel={j}, alpha-panel={k}",
                    )
                    _, value_hi = root_action_bounds(sigma, A(seed), alpha)
                    margin = core.lower(target) - value_hi
                    require(
                        margin > 0,
                        f"root seed failed at f={f}, n={n}, phase={phase}, "
                        f"sigma-panel={j}, alpha-panel={k}",
                    )
                    # Also certify that the exact series is defined at the
                    # common a priori upper endpoint used by the bisection.
                    root_action_bounds(sigma, A(core.KAPPA_MAX[f]), alpha)
                    checked += 1
                    smallest = min(smallest, float(margin))
                    smallest_q = min(smallest_q, float(q_margin))
    print("PASS: requested high-floor root seed grid certified")
    print(
        f"precision={ctx.prec}; checked-seed-boxes={checked}; "
        f"skipped-empty-phases={skipped}; smallest-seed-margin={smallest}; "
        f"smallest-seed-q={smallest_q}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--f", type=int)
    parser.add_argument("--n", type=int)
    parser.add_argument("--phase", choices=PHASES)
    parser.add_argument("--precision", type=int, default=512)
    parser.add_argument("--max-boxes", type=int, default=500_000)
    parser.add_argument("--sigma-panels", type=int, default=16)
    parser.add_argument("--alpha-panels", type=int, default=8)
    parser.add_argument("--seed-audit", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    central, outer = certified_pair_lists()
    candidates = central | outer
    if args.f is not None:
        require(4 <= args.f <= 49, "--f must lie in 4..49")
        candidates = {(f, n) for f, n in candidates if f == args.f}
    if args.n is not None:
        require(2 <= args.n <= 48, "--n must lie in 2..48")
        candidates = {(f, n) for f, n in candidates if n == args.n}
    require(candidates, "selected scope contains no retained pair")
    require(args.sigma_panels >= 1, "--sigma-panels must be positive")
    require(args.alpha_panels >= 1, "--alpha-panels must be positive")

    configure(args.precision, args.verbose, args.max_boxes)
    phases = (args.phase,) if args.phase is not None else PHASES

    if args.seed_audit:
        audit_root_seed_grid(
            candidates, phases, args.sigma_panels, args.alpha_panels
        )
        return

    cases = boxes = positives = 0
    max_depth = 0
    smallest = float("inf")
    for f, n in sorted(candidates):
        for phase in phases:
            result = verify_high_case(
                f, n, phase, args.sigma_panels, args.alpha_panels
            )
            cases += 1
            boxes += int(result["processed"])
            positives += int(result["positive"])
            max_depth = max(max_depth, int(result["max-depth"]))
            smallest = min(smallest, float(result["smallest-margin"]))
            if args.verbose:
                print(
                    f"CASE f={f} n={n} phase={phase} "
                    f"boxes={result['processed']} positive={result['positive']} "
                    f"pruned={result['pruned']} depth={result['max-depth']} "
                    f"smallest={result['smallest-margin']}"
                )

    full = args.f is None and args.n is None and args.phase is None
    if full:
        require(cases == 1830, "full phase count changed")
        print("PASS: all residual f>=4 no-drop chambers certified")
    else:
        print("PASS: requested residual f>=4 no-drop scope certified")
    print(
        f"precision={ctx.prec}; pairs={len(candidates)}; cases={cases}; "
        f"boxes={boxes}; positive={positives}; max-depth={max_depth}; "
        f"smallest={smallest}"
    )


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError, ZeroDivisionError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
