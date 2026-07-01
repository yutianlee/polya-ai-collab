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

for all `Lambda >= 0`, first for fixed `rho`, then uniformly over useful parameter ranges, and finally over the full shell family if the analytic and certified-computation components close.

The parallel flagship track is the Dirichlet ellipse / Mathieu-function program. A lower-risk backup track is a Jiang-Lin-style certificate theorem for a smooth non-tiling comparison family.

## Agents

- `A1`: GPT Pro Extended through the web UI. Broad strategist, literature scout, synthesis writer, and default judge.
- `A2`: Claude Opus 4.8 Max through the web UI. Focused analytic proof-surgeon and conservative referee.
- `A3`: Gemini Pro Deep Think through the web UI. Independent deep-think critic, route comparator, and obstruction finder.
- `A4`: Deepseek V4-Pro through the API. Automatic proof auditor, formula checker, and reproducible computation planner.

A1, A2, and A3 are semi-manual: paste prompts into persistent web conversations and save copied Markdown responses into `handoff/`. A4 is automatic when `DEEPSEEK_API_KEY` is configured.

## Round Protocol

Each round uses four synchronized stages:

1. Stage A: every active agent independently attacks selected proof obligations.
2. Stage B: every active agent reviews proposed state changes, blockers, evidence, and status claims from the other agents.
3. Stage C: A1 writes a judge synthesis, next-round prompts, and a machine-readable `State Patch`.
4. Stage D: the orchestrator validates the `State Patch`, applies accepted changes to `state/proof_obligations.yml`, regenerates the compact reading packet, and commits/pushes the completed round unless `-NoAutoPublish` is set.

The barrier is strict: reviews do not start until all four reasoning responses are present; judging does not start until all four reviews are present; state mutation does not happen until the judge synthesis has a valid patch.

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

## Round 1 Focus

Round 1 should produce a clean proof-obligation graph, not a theorem claim.

- A1 drafts the target theorem memo and source-audit priorities.
- A2 identifies shell-route blockers and missing lemmas.
- A3 reviews the graph and compares shell, ellipse, and certificate-family route risks.
- A4 audits formulas: shell eigenvalue equation, multiplicities, strict counting convention, and computation plan.

No Round 1 output may promote the shell theorem, the ellipse theorem, or a certificate-family theorem to proved status.

## Human Steering

Edit these files before the next stage or round:

- `human/current_directives.md`: active steering instructions.
- `human/goals.md`: current research and workflow goals.
- `human/ideas.md`: mathematical ideas to try.
- `human/references.md`: papers, links, theorem names, citations, or notes.
- `human/inbox/`: timestamped human notes.

You can also add a note from the command line:

```powershell
python -m math_collab.human --kind idea --title "Check shell phase" --text "Ask all agents to compare annulus cross-product phases with 3D shell multiplicity weights." --activate
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
