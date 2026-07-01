from __future__ import annotations

import copy
import json
import re
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_GRAPH_PATH = Path("state/proof_obligations.yml")

ALLOWED_STATUSES = {
    "proposed",
    "open",
    "blocked",
    "diagnostic_only",
    "source_audit_required",
    "derived_under_assumptions",
    "proved_internal",
    "proved_external_dependency",
    "rejected",
}

PROMOTED_STATUSES = {
    "derived_under_assumptions",
    "proved_internal",
    "proved_external_dependency",
}

OPEN_ACTION_STATUSES = {
    "proposed",
    "open",
    "blocked",
    "source_audit_required",
}

SOURCE_TYPES = {"external_theorem", "source_audit"}
NON_PROOF_TYPES = {"computation"}

REQUIRED_FIELDS = {"id", "type", "status", "title", "track", "next_action"}
LIST_FIELDS = {"dependencies", "implies", "blockers", "required_output"}


@dataclass(frozen=True)
class PatchResult:
    applied: bool
    created: list[str]
    updated: list[str]
    rejected: list[str]
    no_change: list[str]
    messages: list[str]


def _yaml_module() -> Any | None:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return None
    return yaml


def parse_structured_text(text: str, *, source: str) -> Any:
    """Parse JSON-compatible YAML, with PyYAML support when available."""
    stripped = text.strip()
    if not stripped:
        raise ValueError(f"{source} is empty")

    yaml = _yaml_module()
    if yaml is not None:
        try:
            return yaml.safe_load(stripped)
        except Exception as exc:  # pragma: no cover - depends on optional PyYAML
            raise ValueError(f"Could not parse YAML from {source}: {exc}") from exc

    try:
        return json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Could not parse {source}. PyYAML is not installed, so state patches "
            "must be JSON-compatible YAML, which is also valid JSON."
        ) from exc


def dump_graph(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n"


def load_graph(path: Path) -> dict[str, Any]:
    data = parse_structured_text(path.read_text(encoding="utf-8"), source=str(path))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping at the top level")
    return data


def write_graph(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_graph(data), encoding="utf-8", newline="\n")


def obligation_index(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    obligations = graph.get("proof_obligations", [])
    if not isinstance(obligations, list):
        return {}
    by_id: dict[str, dict[str, Any]] = {}
    for item in obligations:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            by_id[item["id"]] = item
    return by_id


def validate_graph(graph: dict[str, Any], *, root: Path | None = None) -> list[str]:
    issues: list[str] = []
    statuses = graph.get("allowed_statuses", sorted(ALLOWED_STATUSES))
    allowed_statuses = set(statuses if isinstance(statuses, list) else [])
    if not allowed_statuses:
        allowed_statuses = ALLOWED_STATUSES
    unknown_allowed = allowed_statuses - ALLOWED_STATUSES
    if unknown_allowed:
        issues.append(f"Unknown statuses declared: {', '.join(sorted(unknown_allowed))}")

    obligations = graph.get("proof_obligations")
    if not isinstance(obligations, list):
        return ["proof_obligations must be a list"]

    seen: set[str] = set()
    by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(obligations):
        if not isinstance(item, dict):
            issues.append(f"proof_obligations[{index}] must be a mapping")
            continue
        obligation_id = item.get("id")
        if not isinstance(obligation_id, str) or not obligation_id.strip():
            issues.append(f"proof_obligations[{index}] has no string id")
            continue
        if obligation_id in seen:
            issues.append(f"Duplicate obligation id: {obligation_id}")
        seen.add(obligation_id)
        by_id[obligation_id] = item

        missing = sorted(field for field in REQUIRED_FIELDS if not item.get(field))
        if missing:
            issues.append(f"{obligation_id}: missing required fields: {', '.join(missing)}")

        status = item.get("status")
        if status not in allowed_statuses:
            issues.append(f"{obligation_id}: unknown status {status!r}")

        for field in LIST_FIELDS:
            if field in item and not isinstance(item[field], list):
                issues.append(f"{obligation_id}: {field} must be a list")

        evidence = item.get("evidence")
        if evidence is not None:
            if not isinstance(evidence, dict):
                issues.append(f"{obligation_id}: evidence must be a mapping")
            else:
                for key in ("positive", "negative", "inconclusive"):
                    if key in evidence and not isinstance(evidence[key], list):
                        issues.append(f"{obligation_id}: evidence.{key} must be a list")

        if status in OPEN_ACTION_STATUSES and not str(item.get("next_action", "")).strip():
            issues.append(f"{obligation_id}: open-like obligations require next_action")

        if item.get("type") in NON_PROOF_TYPES and status in PROMOTED_STATUSES:
            issues.append(f"{obligation_id}: computation obligations may not be proof statuses")

        if item.get("type") in SOURCE_TYPES and status != "rejected":
            source_card = item.get("source_card")
            if not isinstance(source_card, str) or not source_card.strip():
                issues.append(f"{obligation_id}: source obligations require source_card")
            elif root is not None and not (root / source_card).exists():
                issues.append(f"{obligation_id}: source_card not found: {source_card}")

    return issues


def _normalize_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _append_unique(target: list[Any], values: Any) -> None:
    for value in _normalize_list(values):
        if value not in target:
            target.append(value)


def _ensure_evidence(obligation: dict[str, Any]) -> dict[str, list[Any]]:
    evidence = obligation.setdefault("evidence", {})
    if not isinstance(evidence, dict):
        evidence = {}
        obligation["evidence"] = evidence
    for key in ("positive", "negative", "inconclusive"):
        values = evidence.setdefault(key, [])
        if not isinstance(values, list):
            evidence[key] = _normalize_list(values)
    return evidence  # type: ignore[return-value]


def _merge_evidence(obligation: dict[str, Any], added: Any) -> None:
    if not isinstance(added, dict):
        _append_unique(_ensure_evidence(obligation)["inconclusive"], added)
        return
    evidence = _ensure_evidence(obligation)
    for key in ("positive", "negative", "inconclusive"):
        if key in added:
            _append_unique(evidence[key], added[key])


def _patch_ops(patch: dict[str, Any]) -> dict[str, list[Any]]:
    proof_patch = patch.get("proof_obligations", patch)
    if not isinstance(proof_patch, dict):
        raise ValueError("State patch must contain a proof_obligations mapping")
    ops: dict[str, list[Any]] = {}
    for key in ("create", "update", "reject", "no_change"):
        ops[key] = _normalize_list(proof_patch.get(key, []))
    return ops


def _has_new_evidence(update: dict[str, Any]) -> bool:
    for key in ("evidence_added", "evidence"):
        value = update.get(key)
        if isinstance(value, dict):
            if any(_normalize_list(value.get(bucket)) for bucket in ("positive", "negative", "inconclusive")):
                return True
        elif value:
            return True
    return False


def validate_patch_against_graph(graph: dict[str, Any], patch: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    by_id = obligation_index(graph)
    ops = _patch_ops(patch)

    for item in ops["create"]:
        if not isinstance(item, dict):
            issues.append("create entries must be mappings")
            continue
        obligation_id = item.get("id")
        if not obligation_id:
            issues.append("create entry is missing id")
        elif obligation_id in by_id:
            issues.append(f"create entry duplicates existing obligation: {obligation_id}")
        if item.get("status") in PROMOTED_STATUSES and not _has_new_evidence(item):
            issues.append(f"{obligation_id}: promoted created obligation requires evidence")

    for item in ops["update"]:
        if not isinstance(item, dict):
            issues.append("update entries must be mappings")
            continue
        obligation_id = item.get("id")
        if obligation_id not in by_id:
            issues.append(f"update entry references unknown obligation: {obligation_id}")
            continue
        old_status = by_id[obligation_id].get("status")
        new_status = item.get("status", old_status)
        if new_status in PROMOTED_STATUSES and old_status not in PROMOTED_STATUSES:
            reason = str(item.get("reason_for_promotion") or item.get("reason") or "").strip()
            if not reason:
                issues.append(f"{obligation_id}: promotion requires reason_for_promotion or reason")
            if not _has_new_evidence(item):
                issues.append(f"{obligation_id}: promotion requires evidence_added or evidence")

    for key in ("reject", "no_change"):
        for item in ops[key]:
            if isinstance(item, str):
                obligation_id = item
            elif isinstance(item, dict):
                obligation_id = item.get("id")
            else:
                issues.append(f"{key} entries must be ids or mappings")
                continue
            if key == "reject" and obligation_id not in by_id and isinstance(item, dict) and item.get("reason"):
                continue
            if obligation_id not in by_id:
                issues.append(f"{key} entry references unknown obligation: {obligation_id}")

    return issues


def apply_state_patch(
    graph: dict[str, Any],
    patch: dict[str, Any],
    *,
    round_index: int | None = None,
    judge_ref: str | None = None,
) -> tuple[dict[str, Any], PatchResult]:
    issues = validate_patch_against_graph(graph, patch)
    if issues:
        raise ValueError("\n".join(issues))

    updated_graph = copy.deepcopy(graph)
    obligations = updated_graph.setdefault("proof_obligations", [])
    if not isinstance(obligations, list):
        raise ValueError("proof_obligations must be a list")
    by_id = obligation_index(updated_graph)
    ops = _patch_ops(patch)

    created: list[str] = []
    updated: list[str] = []
    rejected: list[str] = []
    no_change: list[str] = []
    timestamp = datetime.now().isoformat(timespec="seconds")

    for item in ops["create"]:
        if not isinstance(item, dict):
            continue
        new_item = copy.deepcopy(item)
        if round_index is not None:
            new_item["last_updated_round"] = round_index
        new_item["last_updated_at"] = timestamp
        if judge_ref:
            _merge_evidence(new_item, {"inconclusive": [judge_ref]})
        obligations.append(new_item)
        by_id[new_item["id"]] = new_item
        created.append(new_item["id"])

    for item in ops["update"]:
        if not isinstance(item, dict):
            continue
        obligation = by_id[item["id"]]
        for key, value in item.items():
            if key == "id":
                continue
            if key.endswith("_added"):
                target_key = key[: -len("_added")]
                if target_key == "evidence":
                    _merge_evidence(obligation, value)
                else:
                    current = obligation.setdefault(target_key, [])
                    if not isinstance(current, list):
                        current = _normalize_list(current)
                        obligation[target_key] = current
                    _append_unique(current, value)
                continue
            if key.endswith("_removed"):
                target_key = key[: -len("_removed")]
                current = obligation.get(target_key, [])
                if isinstance(current, list):
                    remove_values = set(_normalize_list(value))
                    obligation[target_key] = [entry for entry in current if entry not in remove_values]
                continue
            if key == "evidence":
                _merge_evidence(obligation, value)
            else:
                obligation[key] = copy.deepcopy(value)
        if round_index is not None:
            obligation["last_updated_round"] = round_index
        obligation["last_updated_at"] = timestamp
        updated.append(item["id"])

    for item in ops["reject"]:
        obligation_id = item if isinstance(item, str) else item.get("id")
        if obligation_id not in by_id:
            rejected_claims = updated_graph.setdefault("rejected_claims", [])
            if not isinstance(rejected_claims, list):
                rejected_claims = []
                updated_graph["rejected_claims"] = rejected_claims
            claim_record = {
                "id": obligation_id,
                "reason": item.get("reason", "") if isinstance(item, dict) else "",
                "last_updated_at": timestamp,
            }
            if round_index is not None:
                claim_record["last_updated_round"] = round_index
            if judge_ref:
                claim_record["evidence"] = [judge_ref]
            rejected_claims.append(claim_record)
            rejected.append(str(obligation_id))
            continue
        obligation = by_id[obligation_id]
        obligation["status"] = "rejected"
        if isinstance(item, dict) and item.get("reason"):
            obligation["rejection_reason"] = item["reason"]
        if round_index is not None:
            obligation["last_updated_round"] = round_index
        obligation["last_updated_at"] = timestamp
        rejected.append(obligation_id)

    for item in ops["no_change"]:
        obligation_id = item if isinstance(item, str) else item.get("id")
        no_change.append(obligation_id)

    messages = []
    assessment = patch.get("round_assessment")
    if isinstance(assessment, dict):
        score = assessment.get("mathematical_progress_score")
        reason = assessment.get("reason")
        if score is not None:
            messages.append(f"round score: {score}")
        if reason:
            messages.append(str(reason))

    return updated_graph, PatchResult(
        applied=True,
        created=created,
        updated=updated,
        rejected=rejected,
        no_change=no_change,
        messages=messages,
    )


def extract_state_patch(markdown: str) -> str | None:
    matches = list(
        re.finditer(
            r"^\s*#{2,6}\s+State Patch\s*$",
            markdown,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    )
    if not matches:
        return None
    match = matches[-1]
    tail = markdown[match.end() :]
    fenced = re.search(r"```(?:yaml|yml|json)?\s*\n(.*?)\n```", tail, flags=re.IGNORECASE | re.DOTALL)
    if fenced:
        return textwrap.dedent(fenced.group(1)).strip()
    next_heading = re.search(r"^\s*#{2,6}\s+", tail, flags=re.MULTILINE)
    block = tail[: next_heading.start()] if next_heading else tail
    block = block.strip()
    return textwrap.dedent(block).strip() or None


def patch_result_summary(result: PatchResult | None) -> str:
    if result is None:
        return "No valid State Patch was applied; proof_obligations.yml is unchanged."
    parts = []
    if result.created:
        parts.append(f"created: {', '.join(result.created)}")
    if result.updated:
        parts.append(f"updated: {', '.join(result.updated)}")
    if result.rejected:
        parts.append(f"rejected: {', '.join(result.rejected)}")
    if result.no_change:
        parts.append(f"no_change: {', '.join(result.no_change)}")
    if result.messages:
        parts.extend(result.messages)
    return "; ".join(parts) if parts else "State Patch made no graph changes."


def active_obligations(graph: dict[str, Any]) -> list[dict[str, Any]]:
    obligations = graph.get("proof_obligations", [])
    if not isinstance(obligations, list):
        return []
    target_ids = graph.get("round_selection", {}).get("target_obligations", [])
    target_order = {obligation_id: index for index, obligation_id in enumerate(target_ids)}

    def sort_key(item: dict[str, Any]) -> tuple[int, int, str]:
        obligation_id = str(item.get("id", ""))
        if obligation_id in target_order:
            return (0, target_order[obligation_id], obligation_id)
        status = str(item.get("status", ""))
        active_rank = 1 if status in {"open", "proposed", "blocked", "source_audit_required"} else 2
        return (active_rank, 99, obligation_id)

    active = [
        item
        for item in obligations
        if isinstance(item, dict) and item.get("status") not in {"rejected", "proved_internal", "proved_external_dependency"}
    ]
    return sorted(active, key=sort_key)


def generate_reading_packet(
    graph: dict[str, Any],
    *,
    run_id: str,
    round_index: int,
    patch_summary: str,
    next_round_prompts_path: str = "state/next_round_prompts.md",
) -> str:
    by_id = obligation_index(graph)
    selection = graph.get("round_selection", {}) if isinstance(graph.get("round_selection"), dict) else {}
    targets = [str(item) for item in selection.get("target_obligations", [])]
    route = by_id.get("POLYA-program-target", {})
    target = by_id.get("TARGET-shell-d3", {})

    lines = [
        "# Reading Packet",
        "",
        f"Generated after round {round_index} in run `{run_id}`.",
        "",
        "## Current Theorem Target",
        "",
        "Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.",
        "",
        "Current status: initialization/audit only. No new Pólya theorem has been proved.",
        "",
        "## Current Route",
        "",
        str(route.get("statement_tex", "Program target statement missing from proof obligation graph.")),
        "",
        "## Active Bottleneck",
        "",
        f"`TARGET-shell-d3`: {target.get('status', 'unknown')}.",
        "",
        str(target.get("statement_tex", "Shell target statement missing from proof obligation graph.")),
        "",
        "Current blockers:",
    ]
    for blocker in target.get("blockers", []) if isinstance(target.get("blockers"), list) else []:
        blocker_item = by_id.get(blocker, {})
        title = blocker_item.get("title", "")
        status = blocker_item.get("status", "unknown")
        lines.append(f"- `{blocker}` ({status}): {title}")

    lines.extend(["", "## Round Target Obligations", ""])
    for obligation_id in targets:
        item = by_id.get(obligation_id)
        if not item:
            lines.append(f"- `{obligation_id}`: missing from graph")
            continue
        lines.append(
            f"- `{obligation_id}` ({item.get('status')}, owner `{item.get('owner', 'unassigned')}`): {item.get('title')}"
        )
        lines.append(f"  Next action: {item.get('next_action', 'none recorded')}")

    lines.extend(
        [
            "",
            "## Do-Not-Claim Rules",
            "",
            "- Do not claim the shell theorem, ellipse theorem, or certificate-family theorem has been proved.",
            "- Do not treat computation as proof; computation evidence is diagnostic only.",
            "- Do not use external theorems as proof dependencies without completed source cards.",
            "- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.",
            "",
            "## Agent Assignments",
            "",
            f"Use `{next_round_prompts_path}` for any judge-assigned A1/A2/A3/A4 tasks.",
            "",
            "Default target split:",
            "- `A1`: target theorem memo, source-card discipline, synthesis, and State Patch authoring.",
            "- `A2`: conservative shell-route proof surgery and obstruction analysis.",
            "- `A3`: route comparison and independent obstruction search.",
            "- `A4`: API formula audit and certified-computation planning.",
            "",
            "## Relevant Files",
            "",
            "- `state/proof_obligations.yml`",
            "- `state/next_round_prompts.md`",
            "- `state/best_proof_draft.md`",
            "- `problems/polya_conjecture.md`",
            "- `sources/flps_balls.md`",
            "- `sources/annuli_polya.md`",
            "- `sources/bessel_phase_enclosures.md`",
            "- `sources/shell_weyl_bessel.md`",
            "- `manifests/reading_packet.md`",
            "",
            "## Last State Patch",
            "",
            patch_summary,
            "",
            "## Active Obligation Briefs",
            "",
        ]
    )
    for item in active_obligations(graph)[:20]:
        obligation_id = item.get("id")
        lines.append(f"### {obligation_id}: {item.get('title')}")
        lines.append("")
        lines.append(f"- Status: `{item.get('status')}`")
        lines.append(f"- Track: `{item.get('track')}`")
        lines.append(f"- Owner: `{item.get('owner', 'unassigned')}`")
        blockers = item.get("blockers", [])
        if blockers:
            lines.append(f"- Blockers: {', '.join(f'`{blocker}`' for blocker in blockers)}")
        lines.append(f"- Next action: {item.get('next_action', 'none recorded')}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"
