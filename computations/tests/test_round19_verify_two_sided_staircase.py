from __future__ import annotations

import ast
import shutil
from fractions import Fraction as F

import pytest

from computations import round19_verify_two_sided_staircase as verifier


def test_exactly_six_whitelisted_inputs() -> None:
    assert len(verifier.WHITELISTED_INPUT_HASHES) == 6
    assert set(verifier.WHITELISTED_INPUT_HASHES).isdisjoint(verifier.CONTROL_HASHES)


def test_full_exact_audit_passes() -> None:
    audit = verifier.run_audit()
    assert audit.passed
    assert audit.first_failure is None
    assert len(audit.checks) >= 220


def test_every_category_passes() -> None:
    manifest = verifier.run_audit().manifest()
    assert manifest["verdict"] == "PASS"
    assert manifest["first_failed_obligation"] is None
    assert all(bucket["failed"] == 0 for bucket in manifest["categories"].values())


def test_machin_certificate_strictly_refines_pi_enclosure() -> None:
    lower, upper = verifier.machin_pi_bounds()
    assert verifier.PI_LO < lower < upper < verifier.PI_HI


@pytest.mark.parametrize(
    ("rho", "threshold", "cap"),
    [
        (F(3, 10), F(51, 10), 9),
        (F(1, 2), F(13, 2), 16),
        (F(1, 2), F(15, 2), 25),
        (F(13, 25), F(17, 2), 36),
        (F(1, 5), F(77, 10), 29),
    ],
)
def test_high_fixed_payments(rho: F, threshold: F, cap: int) -> None:
    assert verifier.w_fixed_lower(rho, threshold) > cap


@pytest.mark.parametrize(
    ("rho", "q", "cap"),
    [
        (F(3, 10), 6, 9),
        (F(1, 2), 12, 16),
        (F(1, 2), 20, 25),
        (F(13, 25), 30, 36),
    ],
)
def test_high_moving_payments(rho: F, q: int, cap: int) -> None:
    assert verifier.moving_payment_holds(rho, q, cap)


@pytest.mark.parametrize(
    ("threshold", "cap"),
    [
        (F(4), 4),
        (F(51, 10), 9),
        (F(13, 2), 16),
        (F(15, 2), 26),
        (F(77, 10), 29),
        (F(17, 2), 40),
        (F(9), 45),
    ],
)
def test_lower_fixed_payments(threshold: F, cap: int) -> None:
    assert verifier.w_at_rhoc_fixed_lower(threshold) > cap


def test_truth_tables_cover_faces_and_absorbed_boxes() -> None:
    metrics = verifier.run_audit().metrics
    assert metrics["residual_face_truth_cases"] == 63
    assert metrics["lower_cap_truth_cases"] >= 48
    assert metrics["absorbed_box_truth_cases"] == 10
    assert metrics["lower_L_crossing_faces"] == 8


def test_analytic_assumptions_are_explicit() -> None:
    assumptions = verifier.ANALYTIC_ASSUMPTIONS
    assert len(assumptions) >= 9
    assert any("Extension by zero" in item for item in assumptions)
    assert any("angular-shift" in item for item in assumptions)
    assert any("strict endpoint" in item for item in assumptions)


def test_verifier_contains_no_float_literals() -> None:
    tree = ast.parse(verifier.Path(verifier.__file__).read_text(encoding="utf-8"))
    floats = [node.value for node in ast.walk(tree)
              if isinstance(node, ast.Constant) and isinstance(node.value, float)]
    assert floats == []


def test_hash_failure_is_decisive_and_first(tmp_path) -> None:
    for rel in {**verifier.CONTROL_HASHES, **verifier.WHITELISTED_INPUT_HASHES}:
        source = verifier.REPO_ROOT / rel
        target = tmp_path / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    candidate = tmp_path / verifier.CANDIDATE_PATH
    candidate.write_bytes(candidate.read_bytes() + b"\nTAMPERED\n")

    audit = verifier.run_audit(tmp_path)
    assert not audit.passed
    assert audit.first_failure is not None
    assert audit.first_failure.name == f"hash {verifier.CANDIDATE_PATH}"
