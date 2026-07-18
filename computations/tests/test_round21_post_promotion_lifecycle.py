"""Historical Round 21 checks against the current Revision-1 graph."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRAPH_SHA256 = "c11958f81da30cadb08c46421b60769fec3a40c7345aa13f9c22a9f86069af65"
APPLICATION_AUDIT_SHA256 = (
    "c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef"
)
SCOPED_PACKET = "state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md"
SCOPED_PACKET_SHA256 = (
    "d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _graph() -> dict[str, object]:
    return json.loads((ROOT / "state/proof_obligations.yml").read_text("utf-8"))


def _obligations_by_id() -> dict[str, dict[str, object]]:
    graph = _graph()
    return {item["id"]: item for item in graph["proof_obligations"]}


def test_round21_nodes_survive_in_authenticated_revision1_graph() -> None:
    path = ROOT / "state/proof_obligations.yml"
    assert _sha256(path) == GRAPH_SHA256
    obligations = _graph()["proof_obligations"]
    assert len(obligations) == 63
    assert len({item["id"] for item in obligations}) == 63


def test_round21_created_statuses_and_empty_residual_are_exact() -> None:
    obligations = _obligations_by_id()
    certificate_ids = (
        "CERT-round21-compact-proxy",
        "CERT-round21-aggregate-tail",
    )
    for certificate_id in certificate_ids:
        certificate = obligations[certificate_id]
        assert certificate["status"] == "certified"
        assert certificate["implies"] == ["SHELL-exact-d20-closure"]

    closure = obligations["SHELL-exact-d20-closure"]
    assert closure["status"] == "proved_internal"
    assert closure["implies"] == []
    assert set(certificate_ids) <= set(closure["dependencies"])
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


def test_frozen_round21_artifacts_record_empty_d21_without_promotion() -> None:
    packet = ROOT / SCOPED_PACKET
    assert _sha256(packet) == SCOPED_PACKET_SHA256
    assert "\\boxed{\\mathcal D_{21}=\\varnothing}" in packet.read_text("utf-8")

    audit = (
        ROOT
        / "rounds/polya-main/round_021/reviews/"
        "state-patch-lemma-application-audit.md"
    ).read_text("utf-8")
    assert "the realized successor D21 is empty" in audit
    assert "Empty D21 did not promote" in audit
