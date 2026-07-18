#!/usr/bin/env python3
"""Deterministic shard launcher for the frozen f>=4 no-drop wrapper.

Pairs are sorted lexicographically and assigned by ``ordinal % shard_count``.
All three phases of a pair stay in the same shard.  The launcher is pinned to
the audited wrapper/core hashes and emits a normalized coverage SHA-256.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import general_d_no_drop_high_floor_compact_verify as high  # noqa: E402


WRAPPER_SHA256 = "5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F"
CORE_SHA256 = "EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE"


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def normalized_ledger(rows: list[tuple[int, int, int, str]]) -> str:
    return "".join(
        f"{ordinal},{f},{n},{phase}\n"
        for ordinal, f, n, phase in sorted(rows)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-count", type=int, required=True)
    parser.add_argument("--shard-index", type=int)
    parser.add_argument("--precision", type=int, default=384)
    parser.add_argument("--max-boxes", type=int, default=500_000)
    parser.add_argument("--sigma-panels", type=int, default=16)
    parser.add_argument("--alpha-panels", type=int, default=8)
    parser.add_argument("--plan-only", action="store_true")
    args = parser.parse_args()

    require(args.shard_count >= 1, "--shard-count must be positive")
    if not args.plan_only:
        require(args.shard_index is not None, "--shard-index is required")
    if args.shard_index is not None:
        require(
            0 <= args.shard_index < args.shard_count,
            "--shard-index must lie in 0..shard-count-1",
        )

    wrapper_path = SCRIPT_DIR / "general_d_no_drop_high_floor_compact_verify.py"
    core_path = SCRIPT_DIR / "general_d_no_drop_compact_verify.py"
    require(file_sha256(wrapper_path) == WRAPPER_SHA256, "wrapper hash changed")
    require(file_sha256(core_path) == CORE_SHA256, "core hash changed")

    central, outer = high.certified_pair_lists()
    pairs = sorted(central | outer)
    require(len(pairs) == 610, "retained pair count changed")

    assignments = [
        [(ordinal, f, n) for ordinal, (f, n) in enumerate(pairs)
         if ordinal % args.shard_count == index]
        for index in range(args.shard_count)
    ]
    flattened = [row for shard in assignments for row in shard]
    require(len(flattened) == 610, "shard plan lost a pair")
    require(len(set(flattened)) == 610, "shard plan duplicated a pair")
    require(sorted(flattened) == [(i, f, n) for i, (f, n) in enumerate(pairs)],
            "shard union does not equal the retained list")

    if args.plan_only:
        for index, shard in enumerate(assignments):
            text = "".join(f"{o},{f},{n}\n" for o, f, n in shard)
            digest = hashlib.sha256(text.encode("ascii")).hexdigest().upper()
            print(
                f"PLAN shard={index}/{args.shard_count}; pairs={len(shard)}; "
                f"cases={3 * len(shard)}; assignment-sha256={digest}"
            )
        print("PASS: deterministic high-floor shard plan covers 610 pairs / 1830 cases")
        return

    assert args.shard_index is not None
    selected = assignments[args.shard_index]
    high.configure(args.precision, False, args.max_boxes)

    ledger: list[tuple[int, int, int, str]] = []
    boxes = positives = 0
    max_depth = 0
    smallest = float("inf")
    for ordinal, f, n in selected:
        for phase in high.PHASES:
            result = high.verify_high_case(
                f, n, phase, args.sigma_panels, args.alpha_panels
            )
            row = (ordinal, f, n, phase)
            require(row not in ledger, f"duplicate coverage row: {row}")
            ledger.append(row)
            boxes += int(result["processed"])
            positives += int(result["positive"])
            max_depth = max(max_depth, int(result["max-depth"]))
            smallest = min(smallest, float(result["smallest-margin"]))
            print(
                f"CASE ordinal={ordinal} f={f} n={n} phase={phase} "
                f"boxes={result['processed']} positive={result['positive']} "
                f"pruned={result['pruned']} depth={result['max-depth']} "
                f"smallest={result['smallest-margin']}",
                flush=True,
            )

    require(len(ledger) == 3 * len(selected), "shard phase count changed")
    digest = hashlib.sha256(normalized_ledger(ledger).encode("ascii")).hexdigest().upper()
    print(
        f"PASS shard={args.shard_index}/{args.shard_count}; "
        f"pairs={len(selected)}; cases={len(ledger)}; boxes={boxes}; "
        f"positive={positives}; max-depth={max_depth}; smallest={smallest}; "
        f"coverage-sha256={digest}"
    )


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError, ZeroDivisionError) as exc:
        print(f"SHARD FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
