# Architecture And Workflow: Pólya AI Collaboration

This repository adapts the Gauss open-circle workflow to a new mathematical target: Pólya's conjecture for non-tiling Euclidean domains.

The central architectural rule is:

```text
claims, not transcripts, are the unit of progress.
```

`state/proof_obligations.yml` is the durable mathematical state. Rounds are evidence. A judge synthesis may propose state changes, but only the validator may apply them.

## Project-Specific Changes From Gauss

- The first theorem target is Dirichlet Pólya for spherical shells in `R^3`.
- The flagship parallel track is the Dirichlet ellipse / Mathieu-function program.
- The fallback publication track is a certified Jiang-Lin-style smooth non-tiling comparison family.
- A1/A2/A3 are WebUI agents.
- A4 is the Deepseek API agent.
- Round 1 is a setup and target-audit round, not a theorem-proving round.

## Proof-Obligation Graph

The graph contains theorem targets, normalization conventions, source audits, analytic lemmas, computation targets, and rejected claims.

Every open-like obligation must have:

- an exact statement,
- a status from the allowed vocabulary,
- an owner,
- dependencies and blockers,
- evidence lists,
- a concrete `next_action`.

Computations are allowed to be `diagnostic_only` or to certify explicitly finite windows. Computations may not silently promote an infinite analytic theorem.

## Round 1 Design

Round 1 target obligations:

- `CONV-strict-counting`
- `TARGET-shell-d3`
- `SRC-FLPS-balls`
- `SRC-annuli`
- `SHELL-cross-product-formula`
- `SHELL-lattice-count`
- `COMP-certified-bessel`

Agent split:

- A1 writes the target theorem memo and source-audit priorities.
- A2 identifies shell-route blockers and missing lemmas.
- A3 compares shell, ellipse, and certificate-family route risks.
- A4 audits formulas, multiplicities, and the computation plan.

Expected outcome: a cleaner graph and sharper next-round prompts. No theorem should be promoted.

## Runner Adaptations

The scripts use:

```text
config/agents.web-polya.json
problems/polya_conjecture.md
run id: polya-main
```

Manual WebUI response files:

```text
handoff/<run-id>/round_XXX/responses/A1.md
handoff/<run-id>/round_XXX/responses/A2.md
handoff/<run-id>/round_XXX/responses/A3.md
handoff/<run-id>/round_XXX/reviews/A1.md
handoff/<run-id>/round_XXX/reviews/A2.md
handoff/<run-id>/round_XXX/reviews/A3.md
```

API files:

```text
rounds/<run-id>/round_XXX/responses/A4-XXX.md
rounds/<run-id>/round_XXX/reviews/A4.md
```

## Validation Policy

The validator rejects:

- unknown statuses,
- missing owners or next actions on open-like obligations,
- source obligations without source cards,
- computations promoted as proof,
- proof promotions without positive evidence and a reason.

The reading packet is regenerated from the graph so prompts stay compact as the archive grows.
