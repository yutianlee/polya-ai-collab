# Proof-Obligation Workflow

This workflow makes mathematical claims, independent reconstructions, and certified artifacts the units of progress.

## Core Files

- `state/proof_obligations.yml`: authoritative claim graph.
- `manifests/reading_packet.md`: compact graph-derived packet.
- `state/next_round_prompts.md`: role-specific next tasks.
- `state/last_validation_report.md`: latest patch-validation result.
- `state/best_proof_draft.md`: incumbent proof, excluded from clean-room prompts.
- `sources/*.md`: source cards required before external theorem use.
- `rounds/*`: attempts, reviews, certificates, and audit trail.

## Cycle Flow

1. Select one primary obligation and at most one independent secondary obligation.
2. Split broad bottlenecks before assigning proof attempts.
3. Create an exact obligation packet and assign distinct roles.
4. Run the lead proof attempt and clean-room reconstruction independently.
5. Freeze both and run an adversarial audit.
6. Run certified computation only for an explicitly finite computation obligation.
7. Let the project lead assemble accepted components and propose a `State Patch`.
8. Validate the patch, update the graph, and regenerate the reading packet.
9. When the target theorem is assembled, run a fresh final referee audit before promotion.

Independent obligations need not wait for one another. Barrier synchronization is limited to genuine dependencies.

## Bottleneck Fields

A bottleneck or theorem obligation must include:

```json
{
  "criticality": "bottleneck",
  "lead_author": "A2",
  "clean_room_reviewer": "A3",
  "adversarial_reviewer": "A4",
  "review_independence": "clean_room",
  "permitted_dependencies": ["SRC-bessel-phase"],
  "falsification_cases": ["rho*k ~ nu", "rho -> 0"],
  "clean_room_artifacts": [],
  "adversarial_review_artifacts": []
}
```

The three roles must be distinct. A promoted bottleneck additionally requires nonempty clean-room and adversarial artifact lists.

## Computation Evidence

Computation obligations declare `evidence_class`. Floating-point experiments and symbolic checks remain `diagnostic_only`. A status of `certified` requires `interval_certified` or `formal_verified` evidence plus:

- `software_version`;
- `reproduction_command`;
- `coverage_statement`;
- `artifact_hashes`;
- `certification_artifacts`.

The coverage statement must connect the certified finite window to the exact analytic threshold and counting convention.

## Patch Example

Use JSON-compatible YAML under `## State Patch`:

```json
{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-phase-outer-turning",
        "status": "open",
        "evidence_added": {
          "inconclusive": ["rounds/polya-main/round_002/responses/A2-002.md"]
        },
        "next_action": "State the Airy-scale one-sided enclosure with explicit constants and overlap bounds."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "TARGET-shell-d3",
        "reason": "No theorem-level proof was supplied."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 1,
    "reason": "A bottleneck was sharpened; no theorem was promoted."
  }
}
```

## Validation Commands

Validate the graph:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
```

Run the guided workflow:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId polya-main -StartRound 2 -Rounds 1
```

Validate a lead synthesis before applying it:

```powershell
python -m math_collab.validate_round rounds/polya-main/round_002/judge/judge-002.md
```

Apply a validated patch:

```powershell
python -m math_collab.validate_round rounds/polya-main/round_002/judge/judge-002.md --apply --round-index 2
```

## Promotion Rules

- Exact mathematical statements, dependencies, and caveats are mandatory.
- External results require completed source cards.
- Computation cannot use mathematical proof statuses.
- Only interval or formal evidence may be `certified`.
- Bottleneck and theorem promotions require independent clean-room and adversarial artifacts.
- Regime integration requires explicit overlap coverage.
- A useful cycle may make no state change; it should then receive a low mathematical-progress score.
