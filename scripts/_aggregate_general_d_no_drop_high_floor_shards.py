#!/usr/bin/env python3
"""Aggregate the frozen eight-shard f>=4 no-drop certificate.

The production shards emit one ``CASE`` row for every retained
``(ordinal, f, n, phase)`` tuple and one final ``PASS`` row.  This checker
reconstructs the audited assignment from the frozen wrapper, verifies every
row and footer, checks the binary-forest identity for every case, and proves
that the eight ledgers form an exact partition of all 610 pairs / 1830
phases.

It reads existing logs only; it never reruns or mutates a shard.
"""

from __future__ import annotations

import hashlib
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
LOG_DIR = ROOT / "human" / "outbox" / "no-drop-high-floor-shards"

HELPER_PATH = SCRIPT_DIR / "_general_d_no_drop_high_floor_shard.py"
WRAPPER_PATH = SCRIPT_DIR / "general_d_no_drop_high_floor_compact_verify.py"
CORE_PATH = SCRIPT_DIR / "general_d_no_drop_compact_verify.py"
EXHAUSTION_PATH = SCRIPT_DIR / "general_d_no_drop_exhaustion_verify.py"

HELPER_SHA256 = "A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092"
WRAPPER_SHA256 = "5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F"
CORE_SHA256 = "EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE"
EXHAUSTION_SHA256 = "81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A"

SHARD_COUNT = 8
PHASES = ("corner", "lower", "open")
MAX_DEPTH = 72
MAX_BOXES_PER_CASE = 500_000

UINT_RE = r"(?:0|[1-9][0-9]*)"

CASE_RE = re.compile(
    rf"^CASE ordinal=(?P<ordinal>{UINT_RE}) "
    rf"f=(?P<f>{UINT_RE}) n=(?P<n>{UINT_RE}) "
    rf"phase=(?P<phase>corner|lower|open) boxes=(?P<boxes>{UINT_RE}) "
    rf"positive=(?P<positive>{UINT_RE}) pruned=(?P<pruned>{UINT_RE}) "
    rf"depth=(?P<depth>{UINT_RE}) smallest=(?P<smallest>inf|[-+0-9.eE]+)$"
)

PASS_RE = re.compile(
    rf"^PASS shard=(?P<index>{UINT_RE})/(?P<count>{UINT_RE}); "
    rf"pairs=(?P<pairs>{UINT_RE}); cases=(?P<cases>{UINT_RE}); "
    rf"boxes=(?P<boxes>{UINT_RE}); positive=(?P<positive>{UINT_RE}); "
    rf"max-depth=(?P<depth>{UINT_RE}); smallest=(?P<smallest>inf|[-+0-9.eE]+); "
    r"coverage-sha256=(?P<digest>[0-9A-F]{64})$"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def parse_float(token: str) -> float:
    if token == "inf":
        return float("inf")
    value = float(token)
    require(math.isfinite(value), f"nonfinite numeric token: {token}")
    require(token == str(value), f"noncanonical numeric token: {token}")
    return value


def same_float(left: float, right: float) -> bool:
    if math.isinf(left) or math.isinf(right):
        return left == right
    return left == right


@dataclass(frozen=True)
class Row:
    ordinal: int
    f: int
    n: int
    phase: str
    boxes: int
    positive: int
    pruned: int
    depth: int
    smallest: float

    @property
    def key(self) -> tuple[int, int, int, str]:
        return self.ordinal, self.f, self.n, self.phase


def normalized_ledger(keys: list[tuple[int, int, int, str]]) -> str:
    return "".join(
        f"{ordinal},{f},{n},{phase}\n"
        for ordinal, f, n, phase in sorted(keys)
    )


def expected_assignments() -> list[list[tuple[int, int, int, str]]]:
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    import general_d_no_drop_high_floor_compact_verify as high

    central, outer = high.certified_pair_lists()
    pairs = sorted(central | outer)
    require(len(pairs) == 610, "retained pair count changed")
    return [
        [
            (ordinal, f, n, phase)
            for ordinal, (f, n) in enumerate(pairs)
            if ordinal % SHARD_COUNT == index
            for phase in PHASES
        ]
        for index in range(SHARD_COUNT)
    ]


def read_shard(index: int) -> tuple[list[Row], re.Match[str], str]:
    path = LOG_DIR / f"shard-{index}-of-{SHARD_COUNT}.log"
    require(path.is_file(), f"missing shard log: {path}")
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        text = raw.decode("utf-16")
    else:
        text = raw.decode("utf-8-sig")
    require(text.endswith("\n"), f"unterminated final line in {path.name}")
    lines = text.splitlines()
    require(lines, f"empty shard log: {path.name}")

    rows: list[Row] = []
    footer: re.Match[str] | None = None
    for line_number, line in enumerate(lines, start=1):
        case_match = CASE_RE.fullmatch(line)
        if case_match is not None:
            require(footer is None, f"CASE after PASS in {path.name}:{line_number}")
            data = case_match.groupdict()
            rows.append(
                Row(
                    ordinal=int(data["ordinal"]),
                    f=int(data["f"]),
                    n=int(data["n"]),
                    phase=data["phase"],
                    boxes=int(data["boxes"]),
                    positive=int(data["positive"]),
                    pruned=int(data["pruned"]),
                    depth=int(data["depth"]),
                    smallest=parse_float(data["smallest"]),
                )
            )
            continue
        pass_match = PASS_RE.fullmatch(line)
        require(pass_match is not None, f"unrecognized line in {path.name}:{line_number}")
        require(footer is None, f"duplicate PASS footer in {path.name}")
        footer = pass_match

    require(footer is not None, f"missing PASS footer in {path.name}")
    require(lines[-1].startswith("PASS "), f"PASS is not final in {path.name}")
    return rows, footer, hashlib.sha256(raw).hexdigest().upper()


def audit_row(row: Row, shard_index: int) -> None:
    require(row.ordinal % SHARD_COUNT == shard_index, f"misassigned row: {row.key}")
    require(row.positive <= row.positive + row.pruned, f"negative leaf count: {row.key}")
    require(row.depth <= MAX_DEPTH, f"depth cap exceeded: {row.key}")
    require(row.boxes <= MAX_BOXES_PER_CASE, f"box cap exceeded: {row.key}")

    if row.boxes == 0:
        require(
            row.positive == 0 and row.pruned == 1 and row.depth == 0
            and row.smallest == float("inf"),
            f"invalid empty-range disposition: {row.key}",
        )
        return

    roots = 2 * (row.positive + row.pruned) - row.boxes
    expected_roots = 16 if row.phase == "corner" else 128
    require(
        roots == expected_roots,
        f"binary-forest identity failed for {row.key}: {roots} != {expected_roots}",
    )
    if row.positive == 0:
        require(
            row.smallest == float("inf"),
            f"finite margin without positive leaf: {row.key}",
        )
    else:
        require(
            math.isfinite(row.smallest) and row.smallest > 0,
            f"nonpositive accepted margin: {row.key}",
        )


def main() -> None:
    for path, expected in (
        (HELPER_PATH, HELPER_SHA256),
        (WRAPPER_PATH, WRAPPER_SHA256),
        (CORE_PATH, CORE_SHA256),
        (EXHAUSTION_PATH, EXHAUSTION_SHA256),
    ):
        actual = sha256(path)
        require(actual == expected, f"frozen source hash changed: {path.name} {actual}")

    assignments = expected_assignments()
    all_rows: list[Row] = []
    log_hashes: list[str] = []

    for index, expected in enumerate(assignments):
        rows, footer, log_hash = read_shard(index)
        data = footer.groupdict()
        keys = [row.key for row in rows]
        require(keys == expected, f"ordered coverage mismatch in shard {index}")
        require(len(keys) == len(set(keys)), f"duplicate row in shard {index}")
        for row in rows:
            audit_row(row, index)

        boxes = sum(row.boxes for row in rows)
        positive = sum(row.positive for row in rows)
        pruned = sum(row.pruned for row in rows)
        max_depth = max(row.depth for row in rows)
        smallest = min(row.smallest for row in rows)
        coverage = hashlib.sha256(
            normalized_ledger(keys).encode("ascii")
        ).hexdigest().upper()

        require(int(data["index"]) == index, f"footer shard index changed: {index}")
        require(int(data["count"]) == SHARD_COUNT, f"footer shard count changed: {index}")
        require(int(data["pairs"]) == len(expected) // 3, f"footer pair count changed: {index}")
        require(int(data["cases"]) == len(expected), f"footer case count changed: {index}")
        require(int(data["boxes"]) == boxes, f"footer box total changed: {index}")
        require(int(data["positive"]) == positive, f"footer positive total changed: {index}")
        require(int(data["depth"]) == max_depth, f"footer depth changed: {index}")
        require(
            same_float(parse_float(data["smallest"]), smallest),
            f"footer minimum margin changed: {index}",
        )
        require(data["digest"] == coverage, f"footer coverage digest changed: {index}")

        stderr_path = LOG_DIR / f"shard-{index}-of-{SHARD_COUNT}.stderr.log"
        require(stderr_path.is_file(), f"missing stderr log: {stderr_path.name}")
        require(stderr_path.read_bytes() == b"", f"nonempty stderr: {stderr_path.name}")

        # The first two production runs predated explicit stderr capture.
        # Their later pinned-source replays must reproduce stdout byte for
        # byte and supply independent empty stderr evidence.
        if index in (0, 1):
            replay_path = LOG_DIR / f"shard-{index}-of-{SHARD_COUNT}.replay.log"
            replay_stderr_path = (
                LOG_DIR / f"shard-{index}-of-{SHARD_COUNT}.replay.stderr.log"
            )
            require(replay_path.is_file(), f"missing replay log: {replay_path.name}")
            require(
                replay_path.read_bytes()
                == (LOG_DIR / f"shard-{index}-of-{SHARD_COUNT}.log").read_bytes(),
                f"replay stdout mismatch: shard {index}",
            )
            require(
                replay_stderr_path.is_file(),
                f"missing replay stderr: {replay_stderr_path.name}",
            )
            require(
                replay_stderr_path.read_bytes() == b"",
                f"nonempty replay stderr: {replay_stderr_path.name}",
            )

        all_rows.extend(rows)
        log_hashes.append(log_hash)
        print(
            f"PASS shard={index}/{SHARD_COUNT}; pairs={len(expected) // 3}; "
            f"cases={len(expected)}; boxes={boxes}; positive={positive}; "
            f"pruned={pruned}; max-depth={max_depth}; smallest={smallest}; "
            f"coverage-sha256={coverage}; log-sha256={log_hash}"
        )

    all_keys = [row.key for row in all_rows]
    expected_union = [key for assignment in assignments for key in assignment]
    require(len(all_keys) == 1830, "global phase count changed")
    require(len(set(all_keys)) == 1830, "global shard overlap detected")
    require(sorted(all_keys) == sorted(expected_union), "global shard gap detected")
    require(len({(row.f, row.n) for row in all_rows}) == 610, "global pair count changed")

    boxes = sum(row.boxes for row in all_rows)
    positive = sum(row.positive for row in all_rows)
    pruned = sum(row.pruned for row in all_rows)
    max_depth = max(row.depth for row in all_rows)
    smallest = min(row.smallest for row in all_rows)
    coverage = hashlib.sha256(
        normalized_ledger(all_keys).encode("ascii")
    ).hexdigest().upper()
    log_set = hashlib.sha256(("\n".join(log_hashes) + "\n").encode("ascii")).hexdigest().upper()

    print(
        "PASS exact union: pairs=610; cases=1830; "
        f"boxes={boxes}; positive={positive}; pruned={pruned}; "
        f"max-depth={max_depth}; smallest={smallest}; "
        f"coverage-sha256={coverage}; log-set-sha256={log_set}"
    )
    print("CERTIFIED: all retained f>=4 no-drop phases form one exact exhaustive ledger")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, UnicodeError, ValueError) as exc:
        print(f"AGGREGATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
