"""Lifecycle checks for the Revision-1 purely analytic shell proof."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "state/proof_obligations.yml"
GRAPH_SHA256 = "c11958f81da30cadb08c46421b60769fec3a40c7345aa13f9c22a9f86069af65"
GRAPH_SIZE = 267_331
LIVE_CLOSURE = "SHELL-analytic-retained-remainder-closure"

EXPECTED_CLOSURE = {
    "TARGET-shell-d3",
    "CONV-strict-counting",
    "SRC-annuli",
    "SRC-bessel-phase",
    "SHELL-exact-phase-rep",
    "SHELL-sturm-liouville-completeness",
    "SHELL-phase-monotonicity",
    "SHELL-cross-product-formula",
    "SHELL-annulus-phase-transfer",
    "SHELL-count-floor-identity",
    "SHELL-phase-enclosures",
    LIVE_CLOSURE,
    "SHELL-rho-one-endpoint",
    "SHELL-rho-uniformity",
}

SPINE_PAIRS = (
    ("SHELL-phase-enclosures", LIVE_CLOSURE),
    ("SHELL-count-floor-identity", LIVE_CLOSURE),
    ("SHELL-sturm-liouville-completeness", LIVE_CLOSURE),
    (LIVE_CLOSURE, "SHELL-rho-uniformity"),
    ("SHELL-rho-one-endpoint", "SHELL-rho-uniformity"),
    ("SHELL-rho-uniformity", "TARGET-shell-d3"),
)

ARTIFACTS = {
    "main_source": "manuscript/spherical-shell-polya-proof.tex",
    "main_pdf": "manuscript/spherical-shell-polya-proof.pdf",
    "supplement_source": "manuscript/spherical-shell-polya-analytic-supplement.tex",
    "supplement_pdf": "manuscript/spherical-shell-polya-analytic-supplement.pdf",
    "ratio_sharp_body": "manuscript/analytic/ratio-sharp-global-closure-body.tex",
    "ratio_sharp_pdf": "manuscript/analytic/compiled/ratio-sharp-global-closure.pdf",
    "revision1_audit": "rounds/polya-main/round_025/reviews/revision1-independent-audit.md",
    "scalar_regression": "computations/certification/verify_ratio_sharp_scalar.py",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _graph() -> dict[str, object]:
    return json.loads(GRAPH.read_text("utf-8"))


def _by_id() -> dict[str, dict[str, object]]:
    return {item["id"]: item for item in _graph()["proof_obligations"]}


def _dependency_closure(
    by_id: dict[str, dict[str, object]], root: str
) -> set[str]:
    seen: set[str] = set()
    stack = [root]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(by_id[current].get("dependencies", []))
    return seen


def _assert_acyclic(
    by_id: dict[str, dict[str, object]], relation: str
) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            raise AssertionError(f"cycle in {relation} at {node}")
        if node in visited:
            return
        visiting.add(node)
        for child in by_id[node].get(relation, []):
            visit(child)
        visiting.remove(node)
        visited.add(node)

    for node in by_id:
        visit(node)


def test_graph_identity_and_revision1_selection_are_frozen() -> None:
    assert _sha256(GRAPH) == GRAPH_SHA256
    assert GRAPH.stat().st_size == GRAPH_SIZE
    graph = _graph()
    obligations = graph["proof_obligations"]
    assert len(obligations) == 63
    assert len({item["id"] for item in obligations}) == 63
    assert graph["round_selection"]["target_obligations"] == []


def test_exact_live_closure_has_only_accepted_unblocked_nodes() -> None:
    by_id = _by_id()
    closure = _dependency_closure(by_id, "TARGET-shell-d3")
    assert closure == EXPECTED_CLOSURE
    accepted = {"proved_internal", "proved_external_dependency", "certified"}
    for node in closure:
        assert by_id[node]["status"] in accepted
        assert by_id[node].get("blockers", []) == []
        permitted = by_id[node].get("permitted_dependencies")
        if permitted is not None:
            assert set(by_id[node].get("dependencies", [])) <= set(permitted)


def test_revision1_spine_edges_are_reciprocal() -> None:
    by_id = _by_id()
    for premise, consequence in SPINE_PAIRS:
        assert premise in by_id[consequence]["dependencies"]
        assert consequence in by_id[premise]["implies"]


def test_owner_faces_are_disjoint_and_retired_nodes_are_detached() -> None:
    by_id = _by_id()
    analytic = by_id[LIVE_CLOSURE]["statement_tex"]
    optical = by_id["SHELL-rho-one-endpoint"]["statement_tex"]
    uniformity = by_id["SHELL-rho-uniformity"]["statement_tex"]
    assert "0<rho<39/50" in analytic
    assert "K>K_0(rho)" in analytic
    assert "39/50<=rho<1" in optical
    assert "K<=K_0" in uniformity
    assert "K>K_0" in uniformity

    closure = _dependency_closure(by_id, "TARGET-shell-d3")
    for forbidden in (
        "SHELL-rho-zero-endpoint",
        "SHELL-rho-compact",
        "SHELL-next-angular-staircase",
        "SHELL-two-sided-staircase",
        "SHELL-combined-closure",
        "SHELL-exact-d20-closure",
        "CERT-round21-compact-proxy",
        "CERT-round21-aggregate-tail",
        "SHELL-low-interface-shifted-tails",
        "SHELL-weighted-double-sawtooth-simplification",
    ):
        assert forbidden not in closure

    shifted = by_id["SHELL-low-interface-shifted-tails"]
    assert shifted["status"] == "proposed"
    assert "no longer a proof blocker" in shifted["next_action"]
    diagnostic = by_id["SHELL-weighted-double-sawtooth-simplification"]
    assert diagnostic["status"] == "diagnostic_only"
    assert diagnostic["implies"] == []


def test_revision1_artifact_hashes_and_release_copies_match() -> None:
    hashes = _by_id()[LIVE_CLOSURE]["artifact_hashes"]
    assert set(hashes) == set(ARTIFACTS)
    for key, relative in ARTIFACTS.items():
        assert hashes[key] == _sha256(ROOT / relative)

    assert (ROOT / "manuscript/spherical-shell-polya-proof.pdf").read_bytes() == (
        ROOT / "output/pdf/spherical-shell-polya-proof-analytic.pdf"
    ).read_bytes()
    assert (
        ROOT / "manuscript/spherical-shell-polya-analytic-supplement.pdf"
    ).read_bytes() == (
        ROOT / "output/pdf/spherical-shell-polya-analytic-supplement.pdf"
    ).read_bytes()


def test_graph_relations_are_acyclic() -> None:
    by_id = _by_id()
    _assert_acyclic(by_id, "dependencies")
    _assert_acyclic(by_id, "implies")


def test_current_handoff_files_name_the_frozen_graph() -> None:
    for relative in (
        "state/current_state.md",
        "state/gap_register.md",
        "state/next_round_prompts.md",
        "manifests/reading_packet.md",
    ):
        text = (ROOT / relative).read_text("utf-8")
        assert GRAPH_SHA256 in text
        assert "ratio-sharp" in text.lower()
