# Proof-Obligation Workflow

This workflow makes mathematical claims, not transcripts, the unit of progress.

## Core Files

- `state/proof_obligations.yml`: authoritative claim graph.
- `manifests/reading_packet.md`: compact generated packet for agents.
- `state/next_round_prompts.md`: extracted judge prompts for A1, A2, A3, and A4.
- `state/last_validation_report.md`: latest patch validation result.
- `sources/*.md`: source cards required before external theorem use.

## Round Flow

1. Select one primary track and at most one secondary track in `state/proof_obligations.yml`.
2. Stage A agents attack the selected target obligations.
3. Stage B agents review proposed graph mutations: creates, updates, rejections, dependencies, blockers, evidence, and no-change claims.
4. Stage C judge writes narrative synthesis plus `## State Patch`.
5. Stage D validates the patch, applies accepted graph changes, extracts next prompts, regenerates the reading packet, and commits/pushes the completed round unless `-NoAutoPublish` is set.

## Patch Rules

Use JSON-compatible YAML under `## State Patch`. JSON is valid YAML, and this keeps the validator dependency-free when PyYAML is unavailable.

```json
{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-phase-enclosures",
        "status": "open",
        "evidence_added": {
          "inconclusive": ["rounds/polya-main/round_001/responses/A2-001.md"]
        },
        "next_action": "Split the phase problem into oscillatory, turning-point, inner-boundary, and evanescent regimes."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "TARGET-shell-d3",
        "reason": "Round 1 refined the route but supplied no theorem-level proof."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 1,
    "reason": "A blocker was sharpened; no theorem was promoted."
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
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId polya-main -StartRound 1 -Rounds 1
```

Validate a judge output before applying it:

```powershell
python -m math_collab.validate_round rounds/polya-main/round_001/judge/judge-001.md
```

Apply a validated judge patch:

```powershell
python -m math_collab.validate_round rounds/polya-main/round_001/judge/judge-001.md --apply --round-index 1
```

## Safety Rules

- Computation can only add diagnostic evidence unless the obligation is explicitly a certified finite-window proof.
- External theorem obligations need source cards.
- Open or proposed obligations need owners and concrete next actions.
- Round 1 must not promote the shell theorem, ellipse theorem, or certificate-family theorem.
- A round with no valid graph change may still be useful as evidence, but it should receive a low progress score.
