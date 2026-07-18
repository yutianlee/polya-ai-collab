# Pólya AI Collaboration

This repository is a public-memory workflow for multi-AI research on Pólya's conjecture for new non-tiling Euclidean domains.

The workflow is claim-centered: `state/proof_obligations.yml` is the authoritative mathematical state, while `rounds/` contains audit evidence. Web conversation memory is useful for continuity, but the GitHub repository is the durable record.

## Target

The first theorem target is exact Dirichlet Pólya for spherical shells, starting in dimension 3:

```text
A_{rho,1} = { x in R^3 : rho < |x| < 1 }, 0 < rho < 1.
```

With the strict counting convention,

```text
N_D(Omega, Lambda) = #{ j : lambda_j^D(Omega) < Lambda },
```

the target inequality is

```text
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
```

for all `Lambda >= 0`.  The full three-dimensional shell family has now been
closed internally by the purely analytic route described below; the active
work is proof simplification, reconstruction, and external review.

The parallel flagship track is the Dirichlet ellipse / Mathieu-function program. A lower-risk backup track is a Jiang-Lin-style certificate theorem for a smooth non-tiling comparison family.

## Current shell result

As of 17 July 2026, the repository contains a project-internal purely
analytic proof of the three-dimensional spherical-shell target. The
computer-assisted proof is retained as a regression baseline, but no
executable truth value or interval enclosure is a premise of the analytic
argument. The review artifacts are:

- [main paper](manuscript/spherical-shell-polya-proof.tex);
- [analytic support-volume master](manuscript/spherical-shell-polya-analytic-supplement.tex);
- [modular analytic sources and audits](manuscript/analytic/);
- [release main PDF](output/pdf/spherical-shell-polya-proof-analytic.pdf);
- [release analytic supplement](output/pdf/spherical-shell-polya-analytic-supplement.pdf);
- [flattened Revision 2 review bundle](output/submission/spherical-shell-polya-revision2/);
- [response to the two referee reports](human/outbox/response-to-referees.md);
  and
- [evaluation of the three revised strategies](human/outbox/strategy-evaluation-and-revised-approach.md).

This status is restricted to the spherical-shell class and is an internal
proof claim. It is not a claim of literature novelty, priority, or external
publication acceptance.

## Functional Roles

- `A1`: project lead, proof-obligation mapper, integrator, and State Patch author.
- `A2`: incumbent proof author for the selected analytic bottleneck.
- `A3`: clean-room solver working from a reduced packet without the incumbent proof.
- `A4`: adversarial referee, formula checker, and certified-computation engineer.

A1, A2, and A3 are semi-manual: paste prompts into persistent web conversations and save copied Markdown responses into `handoff/`. A4 is automatic when `DEEPSEEK_API_KEY` is configured.

These are configurable functional roles, not a permanent mathematical hierarchy. For a bottleneck obligation, lead author, clean-room reviewer, and adversarial reviewer must be distinct.

## Obligation Protocol

Each cycle is organized around one primary proof obligation and at most one independent secondary obligation:

1. The project lead prepares an exact obligation packet and assigns only needed roles.
2. The incumbent author and clean-room solver work independently.
3. The adversarial reviewer audits the frozen attempts and identifies the first unsupported implication.
4. Codex-style computation work produces diagnostic or certified artifacts under an explicit evidence class.
5. One lead integrates discharged obligations and writes a machine-readable `State Patch`.
6. The validator applies accepted changes and regenerates the reading packet.
7. A fresh final referee audits an assembled theorem before promotion.

The Revision 2 reviewed release uses the exact layer cake as its explanatory spine and
has no live finite owner graph.  Its disjoint cover is: no mode for
`K <= pi/(1-rho)`; one ratio-sharp analytic defect theorem for larger `K` and
`0 < rho < 39/50`; and the optical theorem for larger `K` and
`39/50 <= rho < 1`.  The `rho = 39/50` face is optical-owned and the threshold
frequency face is no-mode-owned.

The old `rho_*` split, staircases through `k_11`, 38-state theorem, residual
sets, 611-row allocation, and executable certificates are detached historical
or regression evidence.  The live graph edge is
`SHELL-analytic-retained-remainder-closure -> SHELL-rho-uniformity`.

Barriers are enforced only at genuine mathematical dependencies. The configured workflow currently gives A1 an integration review of A2/A3/A4 and gives A4 an adversarial review of the frozen A2/A3 attempts; A2 and A3 do not perform universal cross-reviews.

## Layout

```text
problems/
  polya_conjecture.md
protocol.md
config/
  agents.example.json
  agents.web-polya.json
math_collab/
  orchestrator.py
  proof_obligations.py
  validate_state_patch.py
  validate_round.py
  human.py
  normalize_markdown.py
state/
  proof_obligations.yml
  next_round_prompts.md
  last_validation_report.md
  current_state.md
  lemma_bank.md
  gap_register.md
  best_proof_draft.md
sources/
  seed_reports/
human/
  current_directives.md
  goals.md
  ideas.md
  references.md
  inbox/
manifests/
  reading_packet.md
rounds/
  <run-id>/
handoff/
  <run-id>/
```

`rounds/` is the public archive. `handoff/` is ignored by Git and is used for temporary web prompts and copied web responses. The reading packet is generated from the proof-obligation graph rather than from transcript history.

## Quick Start

Validate the proof-obligation graph:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
```

Smoke test the file layout without external API calls:

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --rounds 1 --dry-run --run-id smoke --no-state-update
```

Configure DeepSeek for the automatic A4 agent:

```powershell
Copy-Item .env.example .env
notepad .env
```

Then fill in:

```text
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-pro
```

Smoke test A4:

```powershell
python -m math_collab.api_smoke --config config/agents.web-polya.json --agents A4
```

Generate or advance a mixed manual-web/API research round:

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --run-id polya-main --start-round 1 --rounds 1 --skip-missing-api
```

For the guided runner:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId polya-main -StartRound 1 -Rounds 1
```

Add `-SubmitPrompts` if you want the helper to press Enter after pasting prompts. Add `-NoAutoPublish` to apply Stage D locally without committing/pushing to GitHub.

## Current Focus

- Preserve the revised purely analytic theorem and its strict wall ownership.
- Independently reconstruct the ratio-sharp angular, radial/ball, and scalar
  arguments line by line.
- Keep all finite ledgers and numerical programs detached as regression
  evidence.
- Obtain conventional peer review and a current literature/novelty search
  before any publication claim.

## Human Steering

Edit these files before the next stage or round:

- `human/current_directives.md`: active steering instructions.
- `human/goals.md`: current research and workflow goals.
- `human/ideas.md`: mathematical ideas to try.
- `human/references.md`: papers, links, theorem names, citations, or notes.
- `human/inbox/`: timestamped human notes.

You can also add a note from the command line:

```powershell
python -m math_collab.human --kind idea --title "Check shell phase" --text "Assign a lead proof, a clean-room reconstruction, and an adversarial audit for the shell phase bottleneck." --activate
```

## Safety Rules

Every agent must separate:

- proved statements,
- plausible claims,
- gaps,
- counterexample attempts,
- dependencies,
- confidence.

External theorems need source cards before they are used as proof dependencies. Computations can provide diagnostics and certification evidence, but they do not by themselves prove an analytic theorem unless the proof obligation explicitly states a certified finite verification target.
