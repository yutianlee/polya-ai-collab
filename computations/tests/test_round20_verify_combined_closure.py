"""Targeted tests for the independent Round 20 exact-constant verifier."""

from __future__ import annotations

import ast
import copy
from fractions import Fraction as Q
from pathlib import Path
import subprocess
import sys

import pytest

from computations import round20_verify_combined_closure as verify


ROOT = Path(__file__).resolve().parents[2]
AUDITED_ARTIFACTS = (
    ROOT / "computations/round20_verify_combined_closure.py",
    ROOT / "computations/tests/test_round20_verify_combined_closure.py",
    ROOT / "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md",
)


def _ledger_predicate_issues(source: str) -> list[str]:
    tree = ast.parse(source)
    parents = {
        child: parent
        for parent in ast.walk(tree)
        for child in ast.iter_child_nodes(parent)
    }

    def enclosing_function(node: ast.AST) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
        current = parents.get(node)
        while current is not None and not isinstance(
            current, (ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            current = parents.get(current)
        return current

    def local_assignments(scope: ast.AST | None) -> dict[str, ast.AST]:
        if scope is None:
            return {}
        return {
            target.id: node.value
            for node in ast.walk(scope)
            if isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance((target := node.targets[0]), ast.Name)
        }

    def resolved(
        node: ast.AST,
        assignments: dict[str, ast.AST],
        seen: frozenset[str] = frozenset(),
    ) -> ast.AST:
        class AliasResolver(ast.NodeTransformer):
            def visit_Name(self, item: ast.Name) -> ast.AST:
                if item.id in assignments and item.id not in seen:
                    return resolved(assignments[item.id], assignments, seen | {item.id})
                return copy.deepcopy(item)

        return AliasResolver().visit(copy.deepcopy(node))

    issues: list[str] = []
    require_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "require"
        and node.args
    ]
    for call in require_calls:
        condition = resolved(call.args[0], local_assignments(enclosing_function(call)))
        if isinstance(condition, ast.Constant) and condition.value is True:
            issues.append(f"literal-true:{call.lineno}")
        for comparison in (node for node in ast.walk(condition) if isinstance(node, ast.Compare)):
            left = comparison.left
            for right in comparison.comparators:
                if ast.dump(left, include_attributes=False) == ast.dump(
                    right, include_attributes=False
                ):
                    issues.append(f"same-or-disconnected-AST:{call.lineno}")
                left = right
            if (
                any(isinstance(op, (ast.In, ast.NotIn)) for op in comparison.ops)
                and any(
                    isinstance(item, ast.Constant) and isinstance(item.value, str)
                    for item in ast.walk(comparison)
                )
            ):
                issues.append(f"string-membership:{call.lineno}")
    return issues


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


def test_all_three_artifacts_are_free_of_disallowed_c0_bytes() -> None:
    for path in AUDITED_ARTIFACTS:
        bad = [
            (offset, byte)
            for offset, byte in enumerate(path.read_bytes())
            if (byte < 0x20 and byte not in {0x09, 0x0A, 0x0D}) or byte == 0x7F
        ]
        assert bad == [], f"{path}: {bad}"


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


def test_no_trivial_or_disconnected_ledger_predicates() -> None:
    source_path = ROOT / "computations/round20_verify_combined_closure.py"
    assert _ledger_predicate_issues(source_path.read_text(encoding="utf-8")) == []

    synthetic_bad = """
def bad(ledger, a):
    screen = a + 1
    ledger.require(True, "literal")
    ledger.require((a + 1) == (a + 1), "same AST")
    ledger.require(screen == a + 1, "disconnected alias label")
    ledger.require("B0" not in ("lower", "stair"), "string absence")
"""
    issues = _ledger_predicate_issues(synthetic_bad)
    assert any(issue.startswith("literal-true") for issue in issues)
    assert sum(issue.startswith("same-or-disconnected-AST") for issue in issues) == 2
    assert any(issue.startswith("string-membership") for issue in issues)


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
    expected_side_labels = [label for label in ledger.labels if label.startswith("rho=")]
    assert len(expected_side_labels) == len(verify.LOCALIZATION_EXPECTATIONS)
    assert {item.rho for item in verify.LOCALIZATION_EXPECTATIONS} == set(
        verify.LOCALIZATION_RATIOS
    )


def test_localization_registry_and_sides_are_hard_coded_and_input_connected() -> None:
    hard_coded = (
        (Q(1, 5), 11, 3, 1, 1),
        (Q(3, 10), 8, 2, 3, -1),
        (Q(1, 3), 8, 2, 2, -1),
        (Q(3, 8), 9, 2, 3, 1),
        (Q(2, 5), 9, 2, 2, 1),
        (Q(5, 12), 9, 2, 1, 1),
        (Q(3, 7), 9, 2, 0, -1),
        (Q(1, 2), 10, 2, 0, -1),
        (Q(107, 200), 11, 2, 0, -1),
        (Q(8, 15), 11, 2, 0, -1),
        (Q(3, 5), 8, 2, 0, -1),
        (Q(16, 25), 9, 2, 0, -1),
        (Q(13, 20), 10, 2, 0, -1),
        (Q(2, 3), 11, 2, 0, -1),
        (Q(4, 25), 10, 3, 0, -1),
        (Q(1, 4), 11, 3, 0, -1),
        (Q(7, 20), 9, 2, 4, -1),
    )
    observed_registry = tuple(
        (item.rho, item.checkpoint, item.radial, item.ell, item.expected_sign)
        for item in verify.LOCALIZATION_EXPECTATIONS
    )
    assert observed_registry == hard_coded

    for item, expected in zip(verify.LOCALIZATION_EXPECTATIONS, hard_coded):
        rho, checkpoint, radial, ell, expected_sign = expected
        x = verify.x_at_ratio(rho)
        independent = (
            verify.Interval.point(checkpoint * (checkpoint + 1) - ell * (ell + 1))
            - (radial * radial - 1) * x
        )
        ledger = verify.Ledger()
        connected = verify.verify_localization_expectation(ledger, item)
        assert connected == independent
        assert connected.lo > 0 if expected_sign > 0 else connected.hi < 0


def test_localization_semantics_change_under_perturbed_x() -> None:
    item = verify.LOCALIZATION_EXPECTATIONS[-1]  # hard-coded k9,n=2,ell=4 negative side
    ledger = verify.Ledger()
    at_24 = verify.verify_localization_expectation(
        ledger, item, x_override=verify.Interval.point(Q(24))
    )
    at_25 = verify.verify_localization_expectation(
        ledger, item, x_override=verify.Interval.point(Q(25))
    )
    assert at_24 == verify.Interval.point(Q(-2))
    assert at_25 == verify.Interval.point(Q(-5))
    assert at_24.lo - at_25.lo == 3


def test_k9_h6_h4_cap74_path_is_decisive_and_connected() -> None:
    ledger = verify.Ledger()
    facts = verify.verify_k9_h6_h4_path(ledger)
    assert facts["base_square"] == Q(10609, 100)
    assert facts["propagated_square"] == Q(11409, 100) > 108
    assert facts["channel_wall"] == Q(70, 3)
    assert facts["equality_delta"] == verify.Interval.point(0)
    assert facts["rho_face"] == Q(7, 20)
    assert facts["frequency_wall"] == Q(207, 20)
    assert facts["frequency_wall"] ** 2 < 108
    assert facts["coarse_payment"] == Q(52823261673, 704000000) > 74
    assert facts["payment"].lo > facts["coarse_payment"]
    assert len(ledger.labels) == 13
    assert all(label.startswith("k9 H=6,h=4 cap74:") for label in ledger.labels)
    assert ledger.kinds[-1] == "bookkeeping"
    assert all(kind == "substantive" for kind in ledger.kinds[:-1])


def test_k9_cap74_wrong_channel_wall_fails_at_equality_gate() -> None:
    correct = verify.verify_k9_h6_h4_channel_equality(
        verify.Ledger(), Q(70, 3)
    )
    assert correct == verify.Interval.point(0)
    with pytest.raises(
        verify.VerificationError,
        match="defining k9 ell=4,n=2 equality",
    ):
        verify.verify_k9_h6_h4_channel_equality(verify.Ledger(), Q(71, 3))


def test_optical_reserves_product_minimum_and_monotonicity() -> None:
    ledger = verify.Ledger()
    verify.verify_optical_constants(ledger)
    assert "exact low optical endpoint reserve" in ledger.labels
    assert "exact high optical endpoint reserve" in ledger.labels
    assert "exact product-deficit minimum" in ledger.labels
    assert "D(a)>1382/3125 a^2 for all N,t" in ledger.labels
    assert "full high angular ceiling-error screen at a=c/epsilon" in ledger.labels
    assert "full high radial-deficit screen at a=c/epsilon" in ledger.labels


def test_u_branch_k11_containment_and_exact_subtraction() -> None:
    ledger = verify.Ledger()
    constants = verify.verify_thresholds(ledger)
    verify.verify_u_and_k11(ledger, constants)
    verify.verify_exact_subtraction(ledger)
    assert "U=K0 on rho_c<=rho<39/50" in ledger.labels
    assert "k11<U on rho_c<=rho<7/8" in ledger.labels
    assert "rho=39/50 optical face is removed inclusively" in ledger.labels
    assert "pre-optical post-k11 cell survives exactly as D20" in ledger.labels


def test_full_verifier_and_cli_pass() -> None:
    result = verify.run_all(ROOT)
    assert result["verdict"] == "PASS"
    assert result["first_issue"] is None
    assert result["exact_checks"] == 587
    assert result["substantive_checks"] == 488
    assert result["bookkeeping_checks"] == 65
    assert result["authentication_checks"] == 34
    assert len(result["analytic_assumptions"]) == 8

    completed = subprocess.run(
        [sys.executable, "-B", str(ROOT / "computations/round20_verify_combined_closure.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert completed.stdout.startswith("PASS\nfirst issue: none\n")
    assert "substantive checks: 488" in completed.stdout
    assert "candidate sha256: " + verify.CANDIDATE_SHA256 in completed.stdout
    assert "freeze sha256: " + verify.FREEZE_SHA256 in completed.stdout


def test_skip_hash_cli_is_unambiguously_unauthenticated() -> None:
    result = verify.run_all(ROOT, check_hashes=False)
    assert result["verdict"] == "UNAUTHENTICATED_ARITHMETIC_PASS"
    assert result["authentication_checks"] == 0
    assert result["hashes"] == {}

    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            str(ROOT / "computations/round20_verify_combined_closure.py"),
            "--skip-hash-gates",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert completed.stdout.startswith("UNAUTHENTICATED ARITHMETIC-ONLY RESULT: PASS\n")
    assert "hash gates: SKIPPED" in completed.stdout
    assert "\nPASS\n" not in completed.stdout
    assert "sha256" not in completed.stdout.lower()
    assert verify.CANDIDATE_SHA256 not in completed.stdout
    assert verify.FREEZE_SHA256 not in completed.stdout
