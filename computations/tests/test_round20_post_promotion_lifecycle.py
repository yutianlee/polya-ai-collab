"""Post-promotion authentication for the immutable Round 20 residual freeze."""

from __future__ import annotations

import hashlib
from pathlib import Path

from computations import round20_residual_mask as r20


ROOT = Path(__file__).resolve().parents[2]
MUTABLE_STATE_INPUTS = {
    "state/proof_obligations.yml",
    "state/next_round_prompts.md",
}
FROZEN_TEST_SHA256 = (
    "d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164"
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def test_original_round20_freeze_test_bytes_remain_immutable() -> None:
    path = ROOT / "computations/tests/test_round20_residual_mask.py"
    assert _sha256(path.read_bytes()) == FROZEN_TEST_SHA256


def test_live_state_has_advanced_past_the_round20_freeze() -> None:
    inputs = r20._mask_manifest()["authenticated_inputs"]
    assert inputs["baseline_commit"] == (
        "658674117632d60990ac9b9046aa0fcff9e91a62"
    )
    for relative_path in sorted(MUTABLE_STATE_INPUTS):
        assert _sha256((ROOT / relative_path).read_bytes()) != inputs[relative_path]
