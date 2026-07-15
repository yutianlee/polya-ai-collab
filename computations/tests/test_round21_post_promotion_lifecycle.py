"""Post-application checks for the audited Round 21 lemma State Patch."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRAPH_SHA256 = "b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29"
APPLICATION_AUDIT_SHA256 = (
    "c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef"
)
DERIVED_STATE_PATHS = (
    "state/current_state.md",
    "state/gap_register.md",
    "state/lemma_bank.md",
    "state/next_round_prompts.md",
    "state/best_proof_draft.md",
    "state/last_validation_report.md",
    "manifests/reading_packet.md",
)
HASH_AUTHORITY_PATHS = (
    "state/current_state.md",
    "state/next_round_prompts.md",
    "state/last_validation_report.md",
    "manifests/reading_packet.md",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _graph() -> dict[str, object]:
    return json.loads((ROOT / "state/proof_obligations.yml").read_text("utf-8"))


def _obligations_by_id() -> dict[str, dict[str, object]]:
    graph = _graph()
    return {item["id"]: item for item in graph["proof_obligations"]}


def test_round21_nodes_survive_in_authenticated_final_graph() -> None:
    path = ROOT / "state/proof_obligations.yml"
    assert _sha256(path) == GRAPH_SHA256
    obligations = _graph()["proof_obligations"]
    assert len(obligations) == 61
    assert len({item["id"] for item in obligations}) == 61


def test_round21_created_statuses_and_empty_residual_are_exact() -> None:
    obligations = _obligations_by_id()
    assert obligations["CERT-round21-compact-proxy"]["status"] == "certified"
    assert obligations["CERT-round21-aggregate-tail"]["status"] == "certified"
    closure = obligations["SHELL-exact-d20-closure"]
    assert closure["status"] == "proved_internal"
    statement = closure["statement_tex"]
    assert "rho_c<=rho<1" in statement
    assert "successor residual D21 is empty" in statement
    assert "K=200 assigned to the compact owner" in statement


def test_higher_nodes_are_now_proved_and_diagnostic_parent_stays_detached() -> None:
    obligations = _obligations_by_id()
    for obligation_id in (
        "SHELL-rho-compact",
        "SHELL-rho-uniformity",
        "TARGET-shell-d3",
        "POLYA-program-target",
    ):
        assert obligations[obligation_id]["status"] == "proved_internal"

    diagnostic = obligations["COMP-certified-bessel"]
    assert diagnostic["status"] == "diagnostic_only"
    assert "TARGET-shell-d3" not in diagnostic["implies"]
    for obligation_id in (
        "SHELL-rho-compact",
        "TARGET-shell-d3",
        "POLYA-program-target",
    ):
        item = obligations[obligation_id]
        assert "COMP-certified-bessel" not in item["dependencies"]
        assert "COMP-certified-bessel" not in item["blockers"]


def test_application_audit_is_immutable() -> None:
    path = (
        ROOT
        / "rounds/polya-main/round_021/reviews/"
        "state-patch-lemma-application-audit.md"
    )
    assert _sha256(path) == APPLICATION_AUDIT_SHA256


def test_derived_state_records_empty_d21_and_later_theorem_promotion() -> None:
    for relative_path in DERIVED_STATE_PATHS:
        text = (ROOT / relative_path).read_text("utf-8")
        assert "\\mathcal D_{21}" in text
    for relative_path in HASH_AUTHORITY_PATHS:
        text = (ROOT / relative_path).read_text("utf-8")
        assert "b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29" in text
    prompts = (ROOT / "state/next_round_prompts.md").read_text("utf-8")
    assert "post-completion handoff" in prompts
    assert "POLYA-program-target" in prompts
    assert "proved_internal" in prompts
