"""Post-promotion authentication for the immutable Round 19 residual freeze."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess

from computations import round19_residual_mask as r19


ROOT = Path(__file__).resolve().parents[2]
MUTABLE_STATE_INPUTS = {
    "state/proof_obligations.yml",
    "state/next_round_prompts.md",
}
FROZEN_TEST_SHA256 = (
    "41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787"
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git_blob(commit: str, relative_path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{relative_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def test_round19_freeze_inputs_survive_state_promotion() -> None:
    """Authenticate mutable inputs at the baseline and immutable ones in place."""

    inputs = r19._mask_manifest()["authenticated_inputs"]
    baseline = inputs["baseline_commit"]
    assert baseline == "15e4d61db885bfff00a674fd7f37e4cffda70d0c"

    for relative_path, expected in inputs.items():
        if relative_path == "baseline_commit":
            continue
        if relative_path in MUTABLE_STATE_INPUTS:
            observed = _sha256(_git_blob(baseline, relative_path))
        else:
            observed = _sha256((ROOT / relative_path).read_bytes())
        assert observed == expected, relative_path


def test_original_round19_freeze_test_bytes_remain_immutable() -> None:
    path = ROOT / "computations/tests/test_round19_residual_mask.py"
    assert _sha256(path.read_bytes()) == FROZEN_TEST_SHA256


def test_live_state_has_advanced_past_the_round19_freeze() -> None:
    inputs = r19._mask_manifest()["authenticated_inputs"]
    for relative_path in sorted(MUTABLE_STATE_INPUTS):
        assert _sha256((ROOT / relative_path).read_bytes()) != inputs[relative_path]
