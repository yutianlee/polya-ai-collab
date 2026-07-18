"""Regression checks for Round 22 history and the live shell program."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from math_collab.proof_obligations import (
    dump_graph,
    extract_state_patch,
    generate_reading_packet,
    parse_structured_text,
    validate_patch_against_graph,
)


ROOT = Path(__file__).resolve().parents[2]
GRAPH_SHA256 = "c11958f81da30cadb08c46421b60769fec3a40c7345aa13f9c22a9f86069af65"
FINAL_JUDGE = "rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md"
FINAL_JUDGE_SHA256 = "8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2"
PREAPPLICATION_AUDIT = (
    "rounds/polya-main/round_022/reviews/"
    "state-patch-final-audit-source-utf8-final.md"
)
PREAPPLICATION_AUDIT_SHA256 = (
    "3d0952f7a0c3aac820427f90249e9f8d5ece5d6f20e1d0bdcc2e9af11f5adc69"
)
APPLICATION_AUDIT = (
    "rounds/polya-main/round_022/reviews/"
    "state-patch-application-audit-source-utf8-final.md"
)
APPLICATION_AUDIT_SHA256 = (
    "79a46f1e6398cb5887a98dc56142470a3b656b4153f969eec8db07df7604df58"
)
SCOPE_REPLACEMENT = (
    "rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md"
)
SCOPE_REPLACEMENT_SHA256 = (
    "0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2"
)

THEOREM_ARTIFACTS = {
    "state/lemma_packets/TARGET-shell-d3-round22-theorem.md":
        "8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228",
    "rounds/polya-main/round_022/exploration/theorem-claim-freeze.md":
        "6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d",
    "rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md":
        "b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6",
    "rounds/polya-main/round_022/responses/shell-theorem-incumbent.md":
        "4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b",
    "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md":
        "9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12",
    "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md":
        "2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56",
    "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md":
        "6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458",
    "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md":
        "a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9",
}

GEOMETRY_ARTIFACTS = {
    "state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md":
        "d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f",
    "rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md":
        "c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a",
    "rounds/polya-main/round_022/reviews/nontiling-claim-scope-audit.md":
        "96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7",
    "rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md":
        "67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca",
    "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md":
        "6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6",
    "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md":
        "8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55",
    "rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md":
        "bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53",
}

FAILED_PROVENANCE_ARTIFACTS = {
    "rounds/polya-main/round_022/reviews/program-target-scope-audit.md":
        "d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5",
    "rounds/polya-main/round_022/judge/judge-022.md":
        "a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576",
    "rounds/polya-main/round_022/reviews/state-patch-final-audit.md":
        "b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573",
    "rounds/polya-main/round_022/judge/judge-022-replacement.md":
        "c6a440e9b064bf36925b66e6aea188cce1a624a706da76d9bd74daf417f2d415",
    "rounds/polya-main/round_022/reviews/state-patch-final-audit-replacement.md":
        "ce36df00ec78daca0771bb3e29d5281531beec5d41f22ce07dce15747364eb8d",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _graph() -> dict[str, object]:
    return json.loads((ROOT / "state/proof_obligations.yml").read_text("utf-8"))


def _by_id() -> dict[str, dict[str, object]]:
    return {item["id"]: item for item in _graph()["proof_obligations"]}


def _closure(
    by_id: dict[str, dict[str, object]], root: str, relation: str
) -> set[str]:
    seen: set[str] = set()
    stack = list(by_id[root].get(relation, []))
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(by_id[current].get(relation, []))
    return seen


def _assert_acyclic(
    by_id: dict[str, dict[str, object]], relation: str
) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(obligation_id: str) -> None:
        if obligation_id in visited:
            return
        assert obligation_id not in visiting, (
            f"cycle in {relation} through {obligation_id}"
        )
        visiting.add(obligation_id)
        for neighbor in by_id[obligation_id].get(relation, []):
            visit(neighbor)
        visiting.remove(obligation_id)
        visited.add(obligation_id)

    for obligation_id in by_id:
        visit(obligation_id)


def test_final_graph_identity_and_promoted_boundary_are_exact() -> None:
    graph_path = ROOT / "state/proof_obligations.yml"
    assert _sha256(graph_path) == GRAPH_SHA256
    graph_bytes = graph_path.read_bytes()
    assert b"\r" not in graph_bytes
    assert graph_bytes.endswith(b"\n")
    graph = _graph()
    assert dump_graph(graph).encode("utf-8") == graph_bytes
    obligations = graph["proof_obligations"]
    assert len(obligations) == 63
    assert len({item["id"] for item in obligations}) == 63
    assert graph["round_selection"]["target_obligations"] == []
    assert "Revision-1 analytic simplification" in graph["round_selection"][
        "round_rule"
    ]

    by_id = _by_id()
    for obligation_id in (
        "SHELL-spherical-shell-nontiling",
        "SHELL-analytic-retained-remainder-closure",
        "SHELL-rho-compact",
        "SHELL-rho-uniformity",
        "TARGET-shell-d3",
        "POLYA-program-target",
    ):
        assert by_id[obligation_id]["status"] == "proved_internal"
        assert by_id[obligation_id]["blockers"] == []


def test_promoted_dependencies_and_permissions_are_exact() -> None:
    by_id = _by_id()
    expected_dependencies = {
        "SHELL-spherical-shell-nontiling": [],
        "SHELL-analytic-retained-remainder-closure": [
            "SHELL-phase-enclosures",
            "SHELL-count-floor-identity",
            "SHELL-sturm-liouville-completeness",
        ],
        "SHELL-rho-compact": [
            "SHELL-phase-enclosures",
            "SHELL-lattice-count",
            "SHELL-fixed-rho-high-energy",
            "SHELL-analytic-retained-remainder-closure",
        ],
        "SHELL-rho-uniformity": [
            "SHELL-analytic-retained-remainder-closure",
            "SHELL-rho-one-endpoint",
        ],
        "TARGET-shell-d3": [
            "CONV-strict-counting",
            "SHELL-cross-product-formula",
            "SHELL-phase-enclosures",
            "SHELL-rho-uniformity",
            "SHELL-sturm-liouville-completeness",
        ],
        "POLYA-program-target": [
            "CONV-strict-counting",
            "TARGET-shell-d3",
            "SHELL-spherical-shell-nontiling",
        ],
    }
    expected_permissions = {
        **expected_dependencies,
        "TARGET-shell-d3": [
            "CONV-strict-counting",
            "SHELL-cross-product-formula",
            "SHELL-phase-enclosures",
            "SHELL-lattice-count",
            "SHELL-fixed-rho-high-energy",
            "SHELL-rho-uniformity",
            "SHELL-sturm-liouville-completeness",
        ],
    }
    for obligation_id, dependencies in expected_dependencies.items():
        assert by_id[obligation_id]["dependencies"] == dependencies
        assert by_id[obligation_id]["permitted_dependencies"] == (
            expected_permissions[obligation_id]
        )
    expected_implies = {
        "SHELL-spherical-shell-nontiling": ["POLYA-program-target"],
        "SHELL-analytic-retained-remainder-closure": [
            "SHELL-rho-uniformity",
            "SHELL-rho-compact-analytic-envelope",
            "SHELL-rho-compact",
        ],
        "SHELL-rho-compact": [],
        "SHELL-rho-uniformity": ["TARGET-shell-d3"],
        "TARGET-shell-d3": ["POLYA-program-target"],
        "POLYA-program-target": [],
    }
    for obligation_id, consequences in expected_implies.items():
        assert by_id[obligation_id]["implies"] == consequences


def test_final_judge_patch_ledger_and_replay_refusal_are_exact() -> None:
    judge_text = (ROOT / FINAL_JUDGE).read_text("utf-8")
    patch_text = extract_state_patch(judge_text)
    assert patch_text is not None
    patch = parse_structured_text(patch_text, source=FINAL_JUDGE)
    operations = patch["proof_obligations"]
    assert [item["id"] for item in operations["create"]] == [
        "SHELL-spherical-shell-nontiling"
    ]
    assert [item["id"] for item in operations["update"]] == [
        "SHELL-phase-enclosures",
        "SHELL-lattice-count",
        "SHELL-fixed-rho-high-energy",
        "SHELL-sturm-liouville-completeness",
        "SHELL-rho-zero-endpoint",
        "SHELL-rho-one-endpoint",
        "SHELL-rho-compact-analytic-envelope",
        "SHELL-exact-d20-closure",
        "SHELL-rho-compact",
        "SHELL-rho-uniformity",
        "TARGET-shell-d3",
        "POLYA-program-target",
    ]
    assert operations["reject"] == []
    assert [item["id"] for item in operations["no_change"]] == [
        "COMP-certified-bessel",
        "COMP-certified-bessel-pilot-round8",
        "COMP-certified-bessel-pilot-round17",
        "ELLIPSE-near-circular",
        "CERT-certificate-family",
        "SRC-mathieu-ellipse",
    ]
    assert validate_patch_against_graph(_graph(), patch) == [
        "create entry duplicates existing obligation: "
        "SHELL-spherical-shell-nontiling"
    ]


def test_every_live_spine_edge_is_reciprocal_and_both_graphs_are_acyclic() -> None:
    by_id = _by_id()
    final_pairs = (
        (
            "SHELL-phase-enclosures",
            "SHELL-analytic-retained-remainder-closure",
        ),
        (
            "SHELL-count-floor-identity",
            "SHELL-analytic-retained-remainder-closure",
        ),
        (
            "SHELL-sturm-liouville-completeness",
            "SHELL-analytic-retained-remainder-closure",
        ),
        (
            "SHELL-analytic-retained-remainder-closure",
            "SHELL-rho-uniformity",
        ),
        ("SHELL-rho-one-endpoint", "SHELL-rho-uniformity"),
        ("CONV-strict-counting", "TARGET-shell-d3"),
        ("SHELL-cross-product-formula", "TARGET-shell-d3"),
        ("SHELL-phase-enclosures", "TARGET-shell-d3"),
        ("SHELL-rho-uniformity", "TARGET-shell-d3"),
        ("SHELL-sturm-liouville-completeness", "TARGET-shell-d3"),
        ("TARGET-shell-d3", "POLYA-program-target"),
        ("SHELL-spherical-shell-nontiling", "POLYA-program-target"),
        ("CONV-strict-counting", "POLYA-program-target"),
    )
    for premise, consequence in final_pairs:
        assert premise in by_id[consequence]["dependencies"]
        assert consequence in by_id[premise]["implies"]
    _assert_acyclic(by_id, "dependencies")
    _assert_acyclic(by_id, "implies")


def test_target_and_program_dependency_closures_are_fully_discharged() -> None:
    by_id = _by_id()
    discharged = {"proved_internal", "proved_external_dependency", "certified"}
    target_closure = {
        "TARGET-shell-d3",
        "CONV-strict-counting",
        "SHELL-analytic-retained-remainder-closure",
        "SHELL-annulus-phase-transfer",
        "SHELL-count-floor-identity",
        "SHELL-cross-product-formula",
        "SHELL-exact-phase-rep",
        "SHELL-phase-enclosures",
        "SHELL-phase-monotonicity",
        "SHELL-rho-one-endpoint",
        "SHELL-rho-uniformity",
        "SHELL-sturm-liouville-completeness",
        "SRC-annuli",
        "SRC-bessel-phase",
    }
    assert _closure(by_id, "TARGET-shell-d3", "dependencies") | {
        "TARGET-shell-d3"
    } == target_closure
    program_closure = target_closure | {
        "SHELL-spherical-shell-nontiling",
        "POLYA-program-target",
    }
    assert _closure(by_id, "POLYA-program-target", "dependencies") | {
        "POLYA-program-target"
    } == program_closure
    for closure in (target_closure, program_closure):
        assert {by_id[item]["status"] for item in closure} <= discharged


def test_geometry_and_spectral_routes_meet_only_at_program_target() -> None:
    by_id = _by_id()
    geometry_descendants = _closure(
        by_id, "SHELL-spherical-shell-nontiling", "implies"
    )
    spectral_descendants = _closure(by_id, "TARGET-shell-d3", "implies")
    assert geometry_descendants & spectral_descendants == {"POLYA-program-target"}


def test_program_evidence_preserves_positive_and_negative_chronology() -> None:
    by_id = _by_id()
    replacement = SCOPE_REPLACEMENT
    failures = set(FAILED_PROVENANCE_ARTIFACTS)
    final_judge = FINAL_JUDGE
    for obligation_id in (
        "SHELL-spherical-shell-nontiling",
        "POLYA-program-target",
    ):
        evidence = by_id[obligation_id]["evidence"]
        assert replacement in evidence["positive"]
        assert failures <= set(evidence["negative"])
    assert final_judge in by_id["SHELL-spherical-shell-nontiling"]["evidence"][
        "inconclusive"
    ]

    final_patch_text = extract_state_patch((ROOT / FINAL_JUDGE).read_text("utf-8"))
    assert final_patch_text is not None
    final_patch = parse_structured_text(final_patch_text, source=FINAL_JUDGE)
    operations = final_patch["proof_obligations"]
    changed_ids = [item["id"] for item in operations["create"] + operations["update"]]
    paths: set[str] = set()
    for obligation_id in changed_ids:
        item = by_id[obligation_id]
        for bucket in item["evidence"].values():
            paths.update(bucket)
        paths.update(item.get("clean_room_artifacts", []))
        paths.update(item.get("adversarial_review_artifacts", []))
    assert {
        FINAL_JUDGE,
        SCOPE_REPLACEMENT,
        *THEOREM_ARTIFACTS,
        *GEOMETRY_ARTIFACTS,
        *FAILED_PROVENANCE_ARTIFACTS,
    } <= paths
    assert all((ROOT / path).is_file() for path in paths)

    literature_note = "rounds/polya-main/round_021/exploration/literature-scope-note.md"
    expected_locations = {
        SCOPE_REPLACEMENT: {
            ("SHELL-spherical-shell-nontiling", "positive"),
            ("POLYA-program-target", "positive"),
        },
        literature_note: {
            ("SHELL-spherical-shell-nontiling", "inconclusive"),
            ("POLYA-program-target", "inconclusive"),
        },
        FINAL_JUDGE: {
            ("SHELL-spherical-shell-nontiling", "inconclusive"),
        },
    }
    for failure in failures:
        expected_locations[failure] = {
            ("SHELL-spherical-shell-nontiling", "negative"),
            ("POLYA-program-target", "negative"),
        }
    for path, expected in expected_locations.items():
        actual = {
            (obligation_id, bucket)
            for obligation_id, item in by_id.items()
            for bucket, entries in item.get("evidence", {}).items()
            if path in entries
        }
        assert actual == expected


def test_diagnostic_parent_is_detached_and_parallel_tracks_are_unchanged() -> None:
    by_id = _by_id()
    diagnostic = by_id["COMP-certified-bessel"]
    assert diagnostic["status"] == "diagnostic_only"
    assert diagnostic["blockers"] == []
    assert diagnostic["implies"] == []
    for obligation_id in (
        "SHELL-rho-compact",
        "SHELL-rho-uniformity",
        "TARGET-shell-d3",
        "POLYA-program-target",
    ):
        assert "COMP-certified-bessel" not in by_id[obligation_id]["dependencies"]
        assert "COMP-certified-bessel" not in by_id[obligation_id]["blockers"]

    assert by_id["ELLIPSE-near-circular"]["status"] == "open"
    assert by_id["ELLIPSE-near-circular"]["dependencies"] == [
        "SRC-mathieu-ellipse"
    ]
    assert by_id["ELLIPSE-near-circular"]["blockers"] == ["SRC-mathieu-ellipse"]
    assert by_id["ELLIPSE-near-circular"]["implies"] == ["POLYA-program-target"]
    assert by_id["CERT-certificate-family"]["status"] == "open"
    assert by_id["CERT-certificate-family"]["dependencies"] == ["SRC-jiang-lin"]
    assert by_id["CERT-certificate-family"]["blockers"] == ["SRC-jiang-lin"]
    assert by_id["CERT-certificate-family"]["implies"] == ["POLYA-program-target"]
    assert by_id["SRC-mathieu-ellipse"]["implies"] == ["ELLIPSE-near-circular"]
    assert by_id["SRC-jiang-lin"]["implies"] == ["CERT-certificate-family"]


def test_final_roles_timestamps_and_all_references_are_exact() -> None:
    by_id = _by_id()
    metadata = {
        "SHELL-spherical-shell-nontiling": (
            ("A2", "A3", "A4"), 22, "2026-07-15T14:47:52"
        ),
        "SHELL-analytic-retained-remainder-closure": (
            ("A1", "A3", "A4"), 25, "2026-07-17T17:00:00"
        ),
        "SHELL-rho-compact": (
            ("A1", "A3", "A4"), 23, "2026-07-17T00:00:00"
        ),
        "SHELL-rho-uniformity": (
            ("A1", "A3", "A4"), 25, "2026-07-17T17:00:00"
        ),
        "TARGET-shell-d3": (
            ("A1", "A3", "A2"), 23, "2026-07-17T00:00:00"
        ),
        "POLYA-program-target": (
            ("A1", "A3", "A4"), 22, "2026-07-15T14:47:52"
        ),
    }
    for obligation_id, expected in metadata.items():
        expected_roles, expected_round, expected_at = expected
        item = by_id[obligation_id]
        actual_roles = (
            item["lead_author"],
            item["clean_room_reviewer"],
            item["adversarial_reviewer"],
        )
        assert actual_roles == expected_roles
        assert item["review_independence"] == "clean_room"
        assert item["last_updated_round"] == expected_round
        assert item["last_updated_at"] == expected_at

    for obligation_id, item in by_id.items():
        for relation in (
            "dependencies",
            "permitted_dependencies",
            "implies",
        ):
            for reference in item.get(relation, []):
                assert reference in by_id, (
                    f"{obligation_id}.{relation} has missing reference {reference}"
                )


def test_round22_artifact_bytes_and_graph_hash_fields_are_immutable() -> None:
    immutable = {
        FINAL_JUDGE: FINAL_JUDGE_SHA256,
        PREAPPLICATION_AUDIT: PREAPPLICATION_AUDIT_SHA256,
        APPLICATION_AUDIT: APPLICATION_AUDIT_SHA256,
        SCOPE_REPLACEMENT: SCOPE_REPLACEMENT_SHA256,
        **THEOREM_ARTIFACTS,
        **GEOMETRY_ARTIFACTS,
        **FAILED_PROVENANCE_ARTIFACTS,
    }
    for relative_path, expected_hash in immutable.items():
        assert _sha256(ROOT / relative_path) == expected_hash

    by_id = _by_id()
    theorem_hashes = by_id["TARGET-shell-d3"]["artifact_hashes"]
    assert theorem_hashes["packet"] == THEOREM_ARTIFACTS[
        "state/lemma_packets/TARGET-shell-d3-round22-theorem.md"
    ]
    assert theorem_hashes["adversarial_referee"] == THEOREM_ARTIFACTS[
        "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
    ]
    program_hashes = by_id["POLYA-program-target"]["artifact_hashes"]
    assert program_hashes["program_scope_audit"] == SCOPE_REPLACEMENT_SHA256
    assert program_hashes["failed_utf8_replacement_judge"] == (
        FAILED_PROVENANCE_ARTIFACTS[
            "rounds/polya-main/round_022/judge/judge-022-replacement.md"
        ]
    )
    target_hashes = by_id["TARGET-shell-d3"]["artifact_hashes"]
    geometry_hashes = by_id["SHELL-spherical-shell-nontiling"]["artifact_hashes"]
    assert len(target_hashes) == 8
    assert len(geometry_hashes) == 13
    assert len(program_hashes) == 12
    all_embedded_hashes = [
        *target_hashes.values(),
        *geometry_hashes.values(),
        *program_hashes.values(),
    ]
    assert len(all_embedded_hashes) == 33
    assert len(set(all_embedded_hashes)) == 21


def test_graph_unicode_is_clean_and_polya_spelling_survives_decoding() -> None:
    graph_bytes = (ROOT / "state/proof_obligations.yml").read_bytes()
    raw_text = graph_bytes.decode("utf-8", errors="strict")
    assert "\ufffd" not in raw_text
    assert "\u8d38" not in raw_text
    assert graph_bytes.count(b"\\u00f3") == 10
    assert "\u00f3" not in raw_text
    canonical = json.dumps(_graph(), ensure_ascii=False, sort_keys=True)
    assert canonical.count("\u00f3") == 10
    assert "\u8d38" not in canonical
    assert "\ufffd" not in canonical
    by_id = _by_id()
    assert "P\u00f3lya" in by_id["TARGET-shell-d3"]["title"]
    assert "P\u00f3lya" in by_id["POLYA-program-target"]["title"]
    assert "P\u00f3lya" in by_id["TARGET-shell-d3"]["next_action"]

    final_judge = (ROOT / FINAL_JUDGE).read_text("utf-8", errors="strict")
    failed_judge = (
        ROOT / "rounds/polya-main/round_022/judge/judge-022-replacement.md"
    ).read_text("utf-8", errors="strict")
    assert (
        final_judge.count("\u00f3"),
        final_judge.count("\u8d38"),
        final_judge.count("\u2014"),
        final_judge.count("\ufffd"),
    ) == (4, 0, 1, 0)
    assert (
        failed_judge.count("\u00f3"),
        failed_judge.count("\u8d38"),
        failed_judge.count("\u2014"),
        failed_judge.count("\ufffd"),
    ) == (0, 4, 1, 0)


def test_reading_packet_generation_uses_live_completed_state() -> None:
    packet = generate_reading_packet(
        _graph(),
        run_id="round22-final-regression",
        round_index=22,
        patch_summary="Final graph already applied exactly once.",
    )
    assert "Target completed internally" in packet
    assert "## Completed Shell Target" in packet
    assert "`TARGET-shell-d3`: proved_internal." in packet
    assert "Current blockers:\n- none" in packet
    assert "does not solve the general P\u00f3lya conjecture" in packet
    assert "no literature-novelty or publication-priority claim" in packet
    assert "Do not claim literature novelty, priority, or publication readiness" in packet
    assert "ratio-sharp tangent-envelope theorem" in packet
    assert "no longer a proof blocker" in packet
    assert "D_16" not in packet
    assert "no complete all-rho" not in packet
    assert "The full theorem remains open" not in packet


def test_derived_state_records_the_final_internal_scope() -> None:
    hash_paths = (
        "state/current_state.md",
        "state/gap_register.md",
        "state/next_round_prompts.md",
        "manifests/reading_packet.md",
    )
    for relative_path in hash_paths:
        text = (ROOT / relative_path).read_text("utf-8")
        assert GRAPH_SHA256 in text
        assert "\u8d38" not in text
        assert "\ufffd" not in text

    current = (ROOT / "state/current_state.md").read_text("utf-8")
    assert "## Revision 2 reviewed proof" in current
    assert "`round_selection.target_obligations` is empty" in current
    assert "SHELL-analytic-retained-remainder-closure" in current
    assert "not a proof of" in current
    assert "the general P" in current

    gaps = (ROOT / "state/gap_register.md").read_text("utf-8")
    assert "There is no open mathematical obligation" in gaps
    assert "The following are not live gaps" in gaps

    prompts = (ROOT / "state/next_round_prompts.md").read_text("utf-8")
    assert "no selected proof-changing target" in prompts
    assert "Reconstruct the ratio-sharp global closure" in prompts
    assert "Do not rely on numerical" in prompts
    assert "sampling as proof" in prompts

    packet = (ROOT / "manifests/reading_packet.md").read_text("utf-8")
    assert "no selected proof-changing target" in packet
    assert "ratio-sharp angular payment" in packet

    lemma_bank = (ROOT / "state/lemma_bank.md").read_text("utf-8")
    assert "## Ratio-sharp global closure" in lemma_bank
    assert "no edge into the" in lemma_bank
    assert "Revision 2 theorem chain" in lemma_bank

    proof = (ROOT / "state/best_proof_draft.md").read_text("utf-8")
    assert "## 2. Exact defect and ratio-sharp angular payment" in proof
    assert "This cover is disjoint and exhaustive" in proof
    assert "No finite staircase" in proof

    report = (ROOT / "state/last_validation_report.md").read_text("utf-8")
    assert "Revision-1" in report
    assert "\\mathcal D_{21}" in report
    assert GRAPH_SHA256 in report
