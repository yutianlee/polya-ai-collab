#!/usr/bin/env python3
"""Temporary logged shard driver for the audited f=3 no-drop replay.

This does not edit the shared verifier.  It performs the two audited
in-memory predicate replacements and runs a closed inclusive n-range.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import time
import types
from pathlib import Path


OLD = 'f == 2 and n >= 8 and box.phase in {"lower", "open"}'
NEW = (
    '((f == 2 and n >= 8) or (f == 3 and n >= 7)) '
    'and box.phase in {"lower", "open"}'
)
RUNTIME_SHA256 = "4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F"


def load_runtime_module():
    verifier = Path(__file__).with_name("general_d_no_drop_compact_verify.py")
    source = verifier.read_text(encoding="utf-8")
    if source.count(OLD) != 2:
        raise AssertionError("shared verifier no longer has the frozen predicate topology")
    source = source.replace(OLD, NEW)
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest().upper()
    if digest != RUNTIME_SHA256:
        raise AssertionError(f"runtime hash mismatch: {digest}")
    module = types.ModuleType("general_d_no_drop_f3_runtime")
    module.__file__ = str(verifier) + "::<runtime-f3-series>"
    sys.modules[module.__name__] = module
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n0", type=int, required=True)
    parser.add_argument("--n1", type=int, required=True)
    parser.add_argument("--precision", type=int, default=512)
    args = parser.parse_args()
    if not (2 <= args.n0 <= args.n1 <= 379):
        raise SystemExit("require 2 <= n0 <= n1 <= 379")
    if args.precision < 256:
        raise SystemExit("precision must be at least 256 bits")

    module = load_runtime_module()
    module.ctx.prec = args.precision
    module.PI = module.arb.pi()
    module.exact_constant_checks()

    expected = 3 * (args.n1 - args.n0 + 1)
    phase_stats = {
        phase: {
            "cases": 0,
            "boxes": 0,
            "positive": 0,
            "pruned": 0,
            "depth": 0,
            "smallest": float("inf"),
        }
        for phase in ("corner", "lower", "open")
    }
    total_boxes = 0
    total_positive = 0
    total_pruned = 0
    max_depth = 0
    smallest = float("inf")
    cases = 0
    started = time.time()
    print(
        "START "
        f"pid={os.getpid()} f=3 n={args.n0}..{args.n1} precision={args.precision} "
        f"runtime_sha256={RUNTIME_SHA256} root_steps={module.ROOT_STEPS} "
        f"panels={module.PANELS} angle_steps={module.ANGLE_STEPS} "
        f"max_depth={module.MAX_DEPTH} max_boxes={module.MAX_BOXES_PER_CASE}",
        flush=True,
    )
    for n in range(args.n0, args.n1 + 1):
        for phase in ("corner", "lower", "open"):
            case_started = time.time()
            try:
                result = module.verify_case(3, n, phase)
            except Exception as exc:
                print(
                    f"FAIL f=3 n={n} phase={phase} "
                    f"type={type(exc).__name__} message={exc}",
                    flush=True,
                )
                raise
            elapsed = time.time() - case_started
            cases += 1
            boxes = int(result["processed"])
            positive = int(result["positive"])
            pruned = int(result["pruned"])
            depth = int(result["max-depth"])
            margin = float(result["smallest-margin"])
            total_boxes += boxes
            total_positive += positive
            total_pruned += pruned
            max_depth = max(max_depth, depth)
            smallest = min(smallest, margin)
            stats = phase_stats[phase]
            stats["cases"] += 1
            stats["boxes"] += boxes
            stats["positive"] += positive
            stats["pruned"] += pruned
            stats["depth"] = max(stats["depth"], depth)
            stats["smallest"] = min(stats["smallest"], margin)
            print(
                f"CASE f=3 n={n} phase={phase} boxes={boxes} "
                f"positive={positive} pruned={pruned} depth={depth} "
                f"smallest={margin} seconds={elapsed:.6f}",
                flush=True,
            )

    if cases != expected:
        raise AssertionError(f"coverage mismatch: {cases} != {expected}")
    print(
        f"PASS f=3 n={args.n0}..{args.n1} cases={cases} boxes={total_boxes} "
        f"positive={total_positive} pruned={total_pruned} depth={max_depth} "
        f"smallest={smallest} seconds={time.time() - started:.6f}",
        flush=True,
    )
    for phase in ("corner", "lower", "open"):
        stats = phase_stats[phase]
        print(
            f"PHASE {phase} cases={stats['cases']} boxes={stats['boxes']} "
            f"positive={stats['positive']} pruned={stats['pruned']} "
            f"depth={stats['depth']} smallest={stats['smallest']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
