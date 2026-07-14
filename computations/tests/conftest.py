"""Pytest lifecycle rules for immutable round-freeze tests.

Residual-freeze tests authenticate the live state files before a round is
promoted.  Once that round's State Patch advances those files, the original
pre-promotion assertion must fail by design.  We retain the immutable test
bytes and mark only that obsolete live-path assertion as an expected failure;
``test_round19_post_promotion_lifecycle.py`` rechecks the same hashes against
the recorded baseline Git objects.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
ROUND19_PRE_PROMOTION_GRAPH = (
    "24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e"
)
ROUND19_LIVE_PATH_TEST = (
    "computations/tests/test_round19_residual_mask.py::"
    "TestManifest::test_authenticated_inputs_match_the_committed_bytes"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Retire exactly one pre-promotion live-path assertion after promotion."""

    current = _sha256(ROOT / "state/proof_obligations.yml")
    if current == ROUND19_PRE_PROMOTION_GRAPH:
        return

    for item in items:
        nodeid = item.nodeid.replace("\\", "/")
        if nodeid == ROUND19_LIVE_PATH_TEST:
            item.add_marker(
                pytest.mark.xfail(
                    strict=True,
                    reason=(
                        "Round 19 freeze authenticated pre-promotion state; "
                        "the applied State Patch intentionally advanced those "
                        "live paths, whose baseline Git objects are checked by "
                        "the post-promotion lifecycle test"
                    ),
                )
            )
