"""Targeted tests for the independent Round 20 exact-constant verifier."""

from __future__ import annotations

import ast
from fractions import Fraction as Q
from pathlib import Path
import subprocess
import sys

import pytest

from computations import round20_verify_combined_closure as verify


ROOT = Path(__file__).resolve().parents[2]


def test_all_frozen_input_hashes_are_gated() -> None:
    ledger = verify.Ledger()
    actual = verify.verify_hashes(ROOT, ledger=ledger)
    assert actual == verify.EXPECTED_HASHES
    assert actual[verify.CANDIDATE_PATH] == verify.CANDIDATE_SHA256
    assert actual[verify.FREEZE_PATH] == verify.FREEZE_SHA256
    assert len(actual) == 17


def test_hash_mismatch_fails_at_the_gate(tmp_path: Path) -> None:
    relative = "candidate.md"
    (tmp_path / relative).write_bytes(b"tampered")
    with pytest.raises(verify.VerificationError, match="SHA-256 gate"):
        verify.verify_hashes(tmp_path, {relative: "0" * 64})


def test_no_floating_point_literal_can_support_pass() -> None:
    source_path = ROOT / "computations/round20_verify_combined_closure.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    float_literals = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    assert float_literals == []
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    assert imported.isdisjoint({"decimal", "mpmath", "numpy", "scipy"})
    unconditional_passes = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "require"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value is True
    ]
    assert unconditional_passes == []


def test_machin_pi_and_threshold_chain_are_exact() -> None:
    ledger = verify.Ledger()
    verify.verify_pi(ledger)
    constants = verify.verify_thresholds(ledger)
    assert verify.PI.lo > Q(333, 106)
    assert verify.PI.hi < Q(22, 7)
    assert constants["rho_star"].hi < constants["rho0"].lo
    assert constants["rho0"].hi < constants["sigma"].lo
    assert constants["sigma"].hi < constants["rho_c"].lo
    assert constants["omega"].lo * constants["d"].lo > 1


def test_all_zero_specializations_have_exact_wall_signs() -> None:
    ledger = verify.Ledger()
    registry = verify.verify_zero_specializations(ledger)
    expected_keys = {
        (1, 2), (2, 2), (3, 2), (5, 2),
        (1, 3), (2, 3),
        (6, 1), (7, 1), (8, 1), (9, 1), (10, 1),
    }
    assert set(registry) == expected_keys
    assert registry[(1, 2)] == Q(77, 10) ** 2
    assert registry[(10, 1)] == Q(69, 5) ** 2
    assert all("tangent-cell" in label or "zero" in label or "Lorch" in label
               or "third-mode" in label or "81/8" in label
               for label in ledger.labels)


def test_lower_inventory_cap395_and_payments() -> None:
    ledger = verify.Ledger()
    constants = verify.verify_thresholds(ledger)
    verify.verify_lower_inventories_and_payments(ledger, constants)
    assert any("exactly 395" in label for label in ledger.labels)
    assert any("payment exceeds 395" in label for label in ledger.labels)
    assert any("ell=14" in label for label in ledger.labels)


def test_every_high_inventory_cap_localization_and_payment() -> None:
    ledger = verify.Ledger()
    constants = verify.verify_thresholds(ledger)
    verify.verify_checkpoint_inventories(ledger, constants)
    verify.verify_cap_tables_and_payments(ledger, constants)
    verify.verify_localizations(ledger, constants)
    for checkpoint in range(7, 12):
        assert any(f"k{checkpoint}" in label for label in ledger.labels)
    assert any("k11 second mode forces rho<8/15" == label for label in ledger.labels)
    assert any("z^2=34 defines" in label for label in ledger.labels)


def test_optical_reserves_product_minimum_and_monotonicity() -> None:
    ledger = verify.Ledger()
    verify.verify_optical_constants(ledger)
    assert "exact low optical endpoint reserve" in ledger.labels
    assert "exact high optical endpoint reserve" in ledger.labels
    assert "exact product-deficit minimum" in ledger.labels
    assert "D(a)>1382/3125 a^2 for all N,t" in ledger.labels


def test_u_branch_k11_containment_and_exact_subtraction() -> None:
    ledger = verify.Ledger()
    constants = verify.verify_thresholds(ledger)
    verify.verify_u_and_k11(ledger, constants)
    verify.verify_exact_subtraction(ledger)
    assert "U=K0 on rho_c<=rho<39/50" in ledger.labels
    assert "k11<U on rho_c<=rho<7/8" in ledger.labels
    assert "rho=39/50 optical face is removed inclusively" in ledger.labels
    assert "B0 and B1 are not subtracted a second time" in ledger.labels


def test_full_verifier_and_cli_pass() -> None:
    result = verify.run_all(ROOT)
    assert result["verdict"] == "PASS"
    assert result["first_issue"] is None
    assert result["exact_checks"] >= 2000
    assert len(result["analytic_assumptions"]) == 8

    completed = subprocess.run(
        [sys.executable, str(ROOT / "computations/round20_verify_combined_closure.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert completed.stdout.startswith("PASS\nfirst issue: none\n")
    assert "candidate sha256: " + verify.CANDIDATE_SHA256 in completed.stdout
    assert "freeze sha256: " + verify.FREEZE_SHA256 in completed.stdout
