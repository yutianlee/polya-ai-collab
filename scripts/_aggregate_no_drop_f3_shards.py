#!/usr/bin/env python3
"""Audit-only aggregator for the segmented f=3 no-drop replay."""

from __future__ import annotations

import hashlib
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOGDIR = ROOT / "human" / "outbox" / "no-drop-f3-shards"
SLICES = (
    ("f3-002-026.log", 2, 26),
    ("f3-027-101.log", 27, 36),
    ("f3-037-058.log", 37, 42),
    ("f3-043-050.log", 43, 50),
    ("f3-051-058.log", 51, 58),
    ("f3-059-080.log", 59, 80),
    ("f3-081-101.log", 81, 101),
    ("f3-102-240.log", 102, 240),
    ("f3-241-379.log", 241, 379),
)
PHASES = ("corner", "lower", "open")
CASE_RE = re.compile(
    r"^CASE f=(?P<f>\d+) n=(?P<n>\d+) phase=(?P<phase>\w+) "
    r"boxes=(?P<boxes>\d+) positive=(?P<positive>\d+) "
    r"pruned=(?P<pruned>\d+) depth=(?P<depth>\d+) "
    r"smallest=(?P<smallest>\S+) seconds=(?P<seconds>\S+)$"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    chosen: dict[tuple[int, str], dict[str, object]] = {}
    print("SLICES")
    for filename, lo, hi in SLICES:
        path = LOGDIR / filename
        assert path.is_file(), path
        print(f"{filename} sha256={sha256(path)} selected={lo}..{hi}")
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = CASE_RE.match(line)
            if match is None:
                continue
            row: dict[str, object] = match.groupdict()
            row["f"] = int(row["f"])
            row["n"] = int(row["n"])
            row["boxes"] = int(row["boxes"])
            row["positive"] = int(row["positive"])
            row["pruned"] = int(row["pruned"])
            row["depth"] = int(row["depth"])
            row["smallest"] = float(row["smallest"])
            row["seconds"] = float(row["seconds"])
            assert row["f"] == 3, (path, line_no, row)
            assert row["phase"] in PHASES, (path, line_no, row)
            if not lo <= row["n"] <= hi:
                continue
            key = (row["n"], row["phase"])
            assert key not in chosen, ("duplicate", key, path, line_no)
            row["source"] = filename
            row["line"] = line_no
            chosen[key] = row

    expected = {(n, phase) for n in range(2, 380) for phase in PHASES}
    assert set(chosen) == expected, (
        "coverage mismatch",
        sorted(expected - set(chosen))[:20],
        sorted(set(chosen) - expected)[:20],
    )
    assert len(chosen) == 1_134

    phase_stats: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "cases": 0,
            "boxes": 0,
            "positive": 0,
            "pruned": 0,
            "depth": 0,
            "smallest": math.inf,
            "seconds": 0.0,
        }
    )
    total = {
        "cases": 0,
        "boxes": 0,
        "positive": 0,
        "pruned": 0,
        "depth": 0,
        "smallest": math.inf,
        "seconds": 0.0,
    }
    for row in chosen.values():
        for stats in (total, phase_stats[row["phase"]]):
            stats["cases"] += 1
            stats["boxes"] += row["boxes"]
            stats["positive"] += row["positive"]
            stats["pruned"] += row["pruned"]
            stats["depth"] = max(stats["depth"], row["depth"])
            stats["smallest"] = min(stats["smallest"], row["smallest"])
            stats["seconds"] += row["seconds"]

    assert total["cases"] == 1_134
    assert all(phase_stats[p]["cases"] == 378 for p in PHASES)
    # Each search is a full binary tree whose leaves are either positive
    # certificates or necessary-condition prunes.  This is an independent
    # check that no unresolved/capped leaf is hidden in a recorded CASE row.
    assert all(
        row["boxes"] == 2 * (row["positive"] + row["pruned"]) - 1
        for row in chosen.values()
    )

    print("COVERAGE exact f=3 n=2..379 phases=corner,lower,open cases=1134 duplicates=0 gaps=0")
    print(
        "TOTAL "
        + " ".join(f"{key}={value}" for key, value in total.items())
    )
    for phase in PHASES:
        print(
            f"PHASE {phase} "
            + " ".join(f"{key}={value}" for key, value in phase_stats[phase].items())
        )
    print("ASSERT every_case_terminal_leaf_identity=PASS")
    for err in sorted(LOGDIR.glob("*.err.log")):
        assert err.stat().st_size == 0, err
        print(f"STDERR {err.name} bytes=0 sha256={sha256(err)}")
    print("AGGREGATE PASS")


if __name__ == "__main__":
    main()
