You are GPT Pro Extended, acting as broad strategist, literature scout, synthesis writer, and default judge.

Review the other agents' Round 1 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail and durable project memory: https://github.com/yutianlee/polya-ai-collab. If your ChatGPT environment has the GitHub connector enabled, use the connected repository `yutianlee/polya-ai-collab` as a source for current repo files, especially `state/proof_obligations.yml`, `manifests/reading_packet.md`, `problems/polya_conjecture.md`, and `sources/seed_reports/`. Use the included prompt context as authoritative for this stage if connector access is unavailable or stale.

## Agent-Specific Instructions

Use GPT Pro Extended. Action for A1/GPT: use the connected GitHub repo `yutianlee/polya-ai-collab`; prioritize `state/proof_obligations.yml`, `manifests/reading_packet.md`, and this pasted prompt. Act as research strategist and conservative synthesis writer for the Pólya project. Prioritize exact theorem statements, source-audit discipline, Bessel and Mathieu special-function hypotheses, lattice-counting reductions, certified finite verification plans, and state-patch calibration. In Round 1, draft the target theorem memo and source-audit priorities; do not claim any new Pólya theorem.

## Raw Markdown Copy-Response Safety Rule

Your final answer must be one single fenced Markdown code block:

````text
```markdown
## Summary
...
```
````

Do not write anything before or after that outer fence. Inside the fence, write normal Markdown and raw LaTeX source using `$...$` and `$$...$$`.

Do not use additional triple-backtick fences inside your answer. This rule is required because web Copy response can corrupt rendered display math, turning `=` into `====` and minus/fraction bars into long dashed lines.

## Active Agents For This Run

Only these agents are active in this run:

- `A1` (GPT Pro Extended): broad strategist, literature scout, synthesis writer, and default judge
- `A2` (Claude Opus 4.8 Max): focused analytic proof-surgeon and conservative referee
- `A3` (Gemini Pro Deep Think): independent deep-think critic, route comparator, and obstruction finder
- `A4` (Deepseek V4-Pro): API-based proof auditor, formula checker, and reproducible computation planner

Do not mention, score, or assign tasks to inactive agents. If older state text refers to inactive agents, treat it as historical context and reassign any still-useful mathematical check to one of the active agents.

## Protocol

# Multi-AI Mathematical Research Protocol

## Authoritative Mathematical State

The authoritative state is `state/proof_obligations.yml`.

A proof obligation is any theorem, lemma, reduction, external theorem, normalization convention, computation target, source audit, obstruction, or counterexample search whose status matters for the project. Round transcripts in `rounds/` are evidence and audit trail; they are not the state itself.

The compact reading packet in `manifests/reading_packet.md` is generated from the proof-obligation graph. Agents should normally read the packet and graph, not the full transcript history.

## Round Structure

Rounds use strict barrier synchronization:

- Stage B cannot begin until A1, A2, A3, and A4 have completed Stage A.
- Stage C cannot begin until A1, A2, A3, and A4 have completed Stage B.
- Stage D cannot begin until the A1 judge synthesis is complete.
- The next round cannot begin until Stage D has validated or rejected the judge's `State Patch` and regenerated the compact reading packet.

### Stage A: Independent Reasoning

Each agent receives:

- the problem statement,
- the current reading packet,
- the proof-obligation graph,
- the current next-round prompts,
- the prior judge decision if available,
- the agent-specific judge prompt if available,
- the human steering bundle,
- the agent-specific task.

The agent must output:

```text
## Summary
## Target proof obligation
## Main claim or direction
## Detailed reasoning
## Theorem-dependency audit
## Hidden assumptions and potential gaps
## Counterexample or obstruction search
## Verification
## Divergent alternatives and 20% exploration
## Useful lemmas
## What should be tested next
## Proposed state patch, if any
## Confidence
```

Stage A is not a full-project continuation by default. It should attack the selected proof obligation or obligations for the round.

### Stage B: Cross Review

Each agent reviews all other active agents' Stage A outputs, with special attention to proposed state changes.

The review must output:

```text
## Most valuable input from others
## Claims that look correct
## Claims that need proof
## Possible errors or hidden assumptions
## Suggested synthesis
## Research strategy
## Verification
## Proposed state changes to accept or reject
## Score by agent
| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
## Next-round recommendation
## Confidence
```

### Stage C: Judge Synthesis

A1 reads all Stage A outputs and Stage B reviews, then writes the judge synthesis.

The judge must output:

```text
## Selected main route
## Useful fragments by source
## Rejected or risky ideas
## Known gaps
## New lemmas to add
## Counterexample checks to run
## Research strategy adjustment
## State Patch
## Next-round prompts by agent
### For A1
### For A2
### For A3
### For A4
## Round Assessment
## Confidence
```

The `State Patch` block is the only mechanism for mutating `state/proof_obligations.yml`. Use JSON-compatible YAML so the local validator can parse it without optional dependencies. The `For A1`, `For A2`, `For A3`, and `For A4` blocks are extracted into `state/next_round_prompts.md`.

### Stage D: State Update

The orchestrator validates the judge's `State Patch` and then updates:

- `state/proof_obligations.yml`: authoritative proof-obligation graph.
- `state/next_round_prompts.md`: extracted agent-specific next-round tasks.
- `state/last_validation_report.md`: validator result for the latest patch.
- `manifests/reading_packet.md`: compact graph-derived packet for the next round.
- `state/current_state.md`: compact pointer to the latest round and validation result.

The orchestrator refuses to apply a patch if:

- an unknown status appears;
- an obligation has duplicate or missing required identifiers;
- an open-like obligation lacks `next_action`;
- a computation is promoted as proof;
- an external theorem or source audit lacks a source card;
- a claim is promoted without evidence and a reason.

Allowed statuses:

```text
proposed
open
blocked
diagnostic_only
source_audit_required
derived_under_assumptions
proved_internal
proved_external_dependency
rejected
```

## Public Repo Rule

The public GitHub repo is the permanent log. Every completed round should be committed and pushed unless the runner is invoked with `-NoAutoPublish`.

## Human Intervention Rule

Human intervention is allowed at any time between stages or rounds.

Human input can appear in:

- `human/current_directives.md`
- `human/goals.md`
- `human/ideas.md`
- `human/references.md`
- `human/inbox/*.md`
- GitHub issues or comments that are manually copied into the files above

Human instructions override previous AI suggestions when they change the target, introduce a reference, reject a route, add a constraint, or change the success criterion.

Agents must explicitly acknowledge relevant human interventions in their next output.

## Mathematical Safety Rules

- Do not mark a claim as proved unless the proof is explicit.
- Preserve failed attempts; they help avoid repeated false starts.
- When a proof step uses an external theorem, name the theorem and state the needed hypotheses.
- Require counterexample or stress-test search for any new lemma.
- Prefer small checkable lemmas over broad vague routes.
- Keep notation stable across rounds.
- Do not claim Dirichlet Pólya for shells, ellipses, or any new domain class unless every analytic reduction, source dependency, parameter-uniformity condition, and finite verification obligation is supplied.

## Markdown Output Rule

Return clean Markdown source. For mathematics, use only:

- inline math: `$...$`
- display math:

```text
$$
...
$$
```

Do not use rendered-equation copy formats. Do not use bare bracket math like `[ ... ]`.
Avoid `\[ ... \]` and `\( ... \)` because some web copy tools drop the backslashes.

## Research-Mode Quality Rubric

This is a research-mode run, not a smoke test. Take enough time to reason carefully before answering. Prefer correctness, explicit assumptions, rigorous gap detection, and precise lemma statements over speed or brevity.

Before writing the final response, internally check your proposal against known barriers, missing hypotheses, possible counterexamples, and literature-status uncertainty. In the final answer, report the refined result rather than hidden chain-of-thought.

For reasoning stages, include: main route, precise lemmas, theorem dependencies, hidden assumptions, obstruction or counterexample checks, what would falsify the route, and confidence.

For reasoning stages, dedicate roughly 80% of the mathematical effort to the judge-assigned main route and roughly 20% to divergent exploration. The exploratory part should consider genuinely different proof routes, reductions, counterexample mechanisms, dual formulations, smoothing choices, literature bridges, or computational certificates.

For review stages, include: valuable ideas from other agents, claims that look correct, claims needing proof, likely false or underspecified claims, missing hypotheses, and concrete synthesis recommendations. Also recommend whether the next round should continue the main route, pivot variables, split into subproblems, test a counterexample, build a computation, or allocate one agent to an exploratory alternative.

For judge stages, include: selected route, useful fragments by source, rejected or risky ideas, exact gaps, new lemma statements, research-strategy adjustment, next-round tasks for A1/A2/A3/A4, and confidence.

## Proof-Obligation Workflow Contract

The authoritative mathematical state is `state/proof_obligations.yml`. Treat rounds as work on specific obligations, not as global project transcripts.

Rules:

- Focus on the round target obligations named in the reading packet or judge task.
- Do not promote an obligation unless you provide an exact statement, dependencies, evidence files, and remaining caveats.
- Computations may add diagnostic evidence or next actions, but may not prove theorem or lemma obligations.
- External theorem obligations require source cards before they can be used as proof dependencies.
- The final judge synthesis must include `## State Patch` using JSON-compatible YAML.

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a referee-style report on A2, A3, and A4. Include a score table, hidden assumptions, exact claims needing proof, concrete verification tasks, and a research-strategy adjustment recommendation.

## Problem

# Pólya Conjecture Collaboration Problem Statement

## Working Target

The project target is exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

The first theorem target is the spherical shell in dimension 3:

```text
A_{rho,1} = { x in R^3 : rho < |x| < 1 }, 0 < rho < 1.
```

With Dirichlet boundary conditions, let

```text
0 < lambda_1^D <= lambda_2^D <= ...
```

be the eigenvalues of the negative Laplacian on `A_{rho,1}`.

Use the strict counting convention:

```text
N_D(Omega,Lambda) = #{ j : lambda_j^D(Omega) < Lambda }.
```

The target inequality is:

```text
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
```

for every `Lambda >= 0`, where

```text
L_3 = omega_3 / (2*pi)^3 = 1/(6*pi^2).
```

Equivalently, after scaling, start with fixed `rho`, then compact intervals `rho in [rho_0,rho_1] subset (0,1)`, then endpoint regimes `rho -> 0` and `rho -> 1`.

## Shell Spectral Formula To Audit

For `A_{rho,1} subset R^d`, angular momentum `ell=0,1,2,...` gives

```text
nu = ell + (d-2)/2.
```

The Dirichlet radial eigenvalues are expected to be zeros in `k=sqrt(Lambda)` of

```text
F_{nu,rho}(k) =
J_nu(rho k) Y_nu(k) - Y_nu(rho k) J_nu(k).
```

The multiplicity is the dimension of spherical harmonics of degree `ell`; in dimension 3 this is

```text
m_{ell,3} = 2 ell + 1.
```

The counting function should therefore be audited in the form

```text
N_D(A_{rho,1}, Lambda)
= sum_{ell >= 0} m_{ell,3}
  #{ k > 0 : F_{ell+1/2,rho}(k)=0, k^2 < Lambda }.
```

Round 1 must audit this formula before using it as a proof dependency.

## Strategy

The intended route is:

1. Reproduce the FLPS disk/ball proof architecture.
2. Audit the annulus proof, especially Bessel cross-products and lattice-counting estimates.
3. Build shell-specific Bessel cross-product phase enclosures.
4. Convert the shell count into a multiplicity-weighted lattice-count problem.
5. Prove high-energy estimates analytically.
6. Close the finite low-energy window with certified interval arithmetic.

Parallel tracks:

- Dirichlet ellipses through Mathieu-function phase enclosures.
- A Jiang-Lin-style exact certificate theorem for a smooth non-tiling comparison family.

## Non-Claim Rules

- No agent may claim a proof of Dirichlet Pólya for shells without complete analytic estimates, source dependencies, parameter handling, and finite verification.
- Floating-point numerics are diagnostic only unless wrapped in a certified finite-window proof obligation.
- External theorems require source cards with exact statements and hypotheses.


## Current State Bundle

--- FILE: state/proof_obligations.yml ---
{
  "schema_version": 1,
  "allowed_statuses": [
    "proposed",
    "open",
    "blocked",
    "diagnostic_only",
    "source_audit_required",
    "derived_under_assumptions",
    "proved_internal",
    "proved_external_dependency",
    "rejected"
  ],
  "tracks": [
    "target_conventions",
    "source_audit",
    "flps_reproduction",
    "shell_analytic",
    "certified_computation",
    "ellipse_parallel",
    "certificate_family"
  ],
  "round_selection": {
    "primary_track": "target_conventions",
    "secondary_track": "shell_analytic",
    "target_obligations": [
      "CONV-strict-counting",
      "TARGET-shell-d3",
      "SRC-FLPS-balls",
      "SRC-annuli",
      "SHELL-cross-product-formula",
      "SHELL-lattice-count",
      "COMP-certified-bessel"
    ],
    "round_rule": "Round 1 should establish the target theorem memo, source-audit priorities, shell formula checks, and finite-verification requirements. No theorem-level Pólya claim may be promoted in Round 1."
  },
  "proof_obligations": [
    {
      "id": "POLYA-program-target",
      "type": "theorem",
      "track": "target_conventions",
      "title": "Program target: exact Dirichlet Pólya for a new non-tiling Euclidean class",
      "status": "open",
      "statement_tex": "Prove N_D(Omega,Lambda) <= L_d |Omega| Lambda^{d/2} for all Lambda >= 0 for at least one new natural non-tiling Euclidean domain class, with Dirichlet boundary conditions and a fixed counting convention.",
      "dependencies": [
        "CONV-strict-counting",
        "TARGET-shell-d3"
      ],
      "implies": [],
      "blockers": [
        "SHELL-phase-enclosures",
        "SHELL-lattice-count",
        "COMP-certified-bessel"
      ],
      "evidence": {
        "positive": [
          "sources/seed_reports/Strategy.md",
          "sources/seed_reports/background-strategy-01.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Keep the global program target open while Round 1 sharpens the first theorem statement and proof-obligation graph."
    },
    {
      "id": "CONV-strict-counting",
      "type": "normalization",
      "track": "target_conventions",
      "title": "Strict Dirichlet counting convention",
      "status": "open",
      "statement_tex": "Use N_D(Omega,Lambda)=#{j: lambda_j^D(Omega)<Lambda} unless a later state patch explicitly changes the convention and audits eigenvalue-jump endpoints.",
      "dependencies": [],
      "implies": [
        "TARGET-shell-d3",
        "POLYA-program-target"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "sources/seed_reports/Strategy.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Round 1 should state the convention in the target theorem memo and verify that all equivalent eigenvalue/counting formulations use the same endpoint rule."
    },
    {
      "id": "TARGET-shell-d3",
      "type": "theorem",
      "track": "shell_analytic",
      "title": "First theorem target: Dirichlet Pólya for 3D spherical shells",
      "status": "open",
      "statement_tex": "For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2} for all Lambda>=0, initially for fixed rho and then with parameter-uniform refinements.",
      "dependencies": [
        "CONV-strict-counting",
        "SHELL-cross-product-formula",
        "SHELL-phase-enclosures",
        "SHELL-lattice-count",
        "COMP-certified-bessel"
      ],
      "implies": [
        "POLYA-program-target"
      ],
      "blockers": [
        "SHELL-phase-enclosures",
        "SHELL-lattice-count",
        "COMP-certified-bessel",
        "SHELL-rho-uniformity"
      ],
      "evidence": {
        "positive": [
          "sources/seed_reports/Strategy.md",
          "sources/seed_reports/background-strategy-01.md"
        ],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/background-strategy-03.md"
        ]
      },
      "owner": "A1",
      "next_action": "Round 1 should produce a two-page target theorem memo: domain class, boundary condition, parameter range, Weyl constant, counting convention, and verification plan."
    },
    {
      "id": "SRC-FLPS-balls",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Source audit: FLPS Euclidean balls proof",
      "status": "source_audit_required",
      "statement_tex": "Record the exact theorem statements, boundary conditions, counting convention, Bessel phase definitions, lattice-counting lemmas, and computer-assisted components from the FLPS Euclidean balls proof.",
      "dependencies": [],
      "implies": [
        "FLPS-disk-ball-reproduction",
        "SHELL-phase-enclosures"
      ],
      "blockers": [],
      "source_card": "sources/flps_balls.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-01.md",
          "sources/seed_reports/Strategy.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Create a rendered source card with theorem statements, hypotheses, notation, and exact dependencies needed for the shell route."
    },
    {
      "id": "SRC-bessel-phase",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Source audit: uniform Bessel phase and zero enclosures",
      "status": "source_audit_required",
      "statement_tex": "Record the uniform two-sided Bessel phase and zero enclosure statements needed to reproduce the FLPS phase-to-lattice pipeline and assess whether they extend to shell cross-products.",
      "dependencies": [],
      "implies": [
        "SHELL-phase-enclosures",
        "COMP-certified-bessel"
      ],
      "blockers": [],
      "source_card": "sources/bessel_phase_enclosures.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-03.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Audit the Bessel phase paper for definitions, constants, transition regimes, and monotonicity hypotheses."
    },
    {
      "id": "SRC-annuli",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Source audit: Dirichlet Pólya for annuli",
      "status": "source_audit_required",
      "statement_tex": "Record the exact annulus theorem, Bessel cross-product setup, trapezoidal floor-sum lemmas, concave/convex lattice estimates, and finite verification strategy.",
      "dependencies": [],
      "implies": [
        "SHELL-cross-product-formula",
        "SHELL-lattice-count",
        "COMP-certified-bessel"
      ],
      "blockers": [],
      "source_card": "sources/annuli_polya.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-01.md",
          "sources/seed_reports/Strategy.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Extract which annulus estimates are dimension-independent and which rely on planar multiplicities."
    },
    {
      "id": "SRC-shell-weyl",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Source audit: Bessel functions and Weyl law for balls and spherical shells",
      "status": "source_audit_required",
      "statement_tex": "Record shell-specific Bessel cross-product zero estimates, Weyl-remainder bounds, dimension ranges, boundary conditions, and whether any statements are one-sided enough for Pólya.",
      "dependencies": [],
      "implies": [
        "SHELL-phase-enclosures",
        "SHELL-rho-uniformity"
      ],
      "blockers": [],
      "source_card": "sources/shell_weyl_bessel.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-01.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Audit the shell Weyl paper for cross-product zero counting statements and explicitness of constants."
    },
    {
      "id": "FLPS-disk-ball-reproduction",
      "type": "infrastructure",
      "track": "flps_reproduction",
      "title": "Reproduce the FLPS disk/ball proof architecture",
      "status": "open",
      "statement_tex": "Reconstruct the chain special-function zeros -> phase estimates -> lattice count -> finite certified range for disks and Dirichlet balls, using audited source statements.",
      "dependencies": [
        "SRC-FLPS-balls",
        "SRC-bessel-phase"
      ],
      "implies": [
        "SHELL-phase-enclosures",
        "SHELL-lattice-count"
      ],
      "blockers": [
        "SRC-FLPS-balls",
        "SRC-bessel-phase"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/Strategy.md"
        ]
      },
      "owner": "A2",
      "next_action": "Draft a reproduction checklist with formulas, theorem dependencies, and verification scripts to import or reimplement."
    },
    {
      "id": "SHELL-cross-product-formula",
      "type": "lemma",
      "track": "shell_analytic",
      "title": "Dirichlet shell spectral decomposition and Bessel cross-product formula",
      "status": "open",
      "statement_tex": "For A_{rho,1} subset R^d, Dirichlet radial eigenvalues in angular momentum ell are zeros k>0 of F_{nu,rho}(k)=J_nu(rho k)Y_nu(k)-Y_nu(rho k)J_nu(k), with nu=ell+(d-2)/2 and spherical-harmonic multiplicity m_{ell,d}.",
      "dependencies": [
        "CONV-strict-counting"
      ],
      "implies": [
        "TARGET-shell-d3",
        "SHELL-phase-enclosures"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "sources/seed_reports/Strategy.md",
          "sources/seed_reports/background-strategy-01.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A4",
      "next_action": "A4 should audit the formula, multiplicities, scaling R=1 reduction, and d=3 specialization m_{ell,3}=2ell+1."
    },
    {
      "id": "SHELL-phase-enclosures",
      "type": "lemma",
      "track": "shell_analytic",
      "title": "Uniform phase enclosures for Bessel cross-product zeros",
      "status": "open",
      "statement_tex": "Construct explicit monotone phase functions Phi_{nu,rho}(k) with certified one-sided error bounds that trap zeros of F_{nu,rho}(k) across oscillatory, Airy/turning-point, inner-boundary transition, and evanescent regimes.",
      "dependencies": [
        "SHELL-cross-product-formula",
        "SRC-bessel-phase",
        "SRC-annuli",
        "SRC-shell-weyl"
      ],
      "implies": [
        "TARGET-shell-d3",
        "SHELL-lattice-count",
        "COMP-certified-bessel"
      ],
      "blockers": [
        "SRC-bessel-phase",
        "SRC-annuli",
        "SRC-shell-weyl"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/Strategy.md"
        ]
      },
      "owner": "A2",
      "next_action": "Split the phase problem into regimes and formulate the first fixed-rho high-energy proposition."
    },
    {
      "id": "SHELL-lattice-count",
      "type": "lemma",
      "track": "shell_analytic",
      "title": "Multiplicity-weighted lattice count below shell phase curves",
      "status": "open",
      "statement_tex": "Convert the shell eigenvalue count into a multiplicity-weighted count over (ell,n), then prove the discrete count is bounded by L_d |A_{rho,1}| Lambda^{d/2} in the analytic high-energy range.",
      "dependencies": [
        "SHELL-cross-product-formula",
        "SHELL-phase-enclosures",
        "SRC-annuli"
      ],
      "implies": [
        "TARGET-shell-d3"
      ],
      "blockers": [
        "SHELL-phase-enclosures"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/Strategy.md"
        ]
      },
      "owner": "A3",
      "next_action": "Round 1 should ask A3 to identify which annulus floor-sum estimates might survive the d=3 multiplicity weight and which need new lemmas."
    },
    {
      "id": "SHELL-rho-uniformity",
      "type": "lemma",
      "track": "shell_analytic",
      "title": "Uniformity in shell ratio rho",
      "status": "open",
      "statement_tex": "Upgrade fixed-rho shell estimates to rho in compact subintervals of (0,1), then separately treat rho -> 0 and rho -> 1.",
      "dependencies": [
        "SHELL-phase-enclosures",
        "SHELL-lattice-count",
        "SRC-shell-weyl"
      ],
      "implies": [
        "TARGET-shell-d3"
      ],
      "blockers": [
        "SHELL-phase-enclosures",
        "COMP-certified-bessel"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/Strategy.md"
        ]
      },
      "owner": "A2",
      "next_action": "Do not attack full rho-uniformity in Round 1; record endpoint risks and defer until fixed-rho high-energy estimates are formulated."
    },
    {
      "id": "COMP-certified-bessel",
      "type": "computation",
      "track": "certified_computation",
      "title": "Certified finite-window verification for Bessel cross-products",
      "status": "diagnostic_only",
      "statement_tex": "Design a deterministic interval-arithmetic framework for isolating shell Bessel cross-product roots and verifying the Pólya counting inequality below an analytic threshold Lambda_0.",
      "dependencies": [
        "SHELL-cross-product-formula",
        "SRC-annuli",
        "SRC-bessel-phase"
      ],
      "implies": [
        "TARGET-shell-d3"
      ],
      "blockers": [
        "SHELL-phase-enclosures"
      ],
      "required_output": [
        "script",
        "exact command",
        "root-enclosure report",
        "counting verification table",
        "limitations"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "sources/seed_reports/Strategy.md"
        ]
      },
      "owner": "A4",
      "next_action": "A4 should specify the minimum certified computation stack and a first smoke-test target; do not treat floating-point tables as proof."
    },
    {
      "id": "SRC-mathieu-ellipse",
      "type": "source_audit",
      "track": "ellipse_parallel",
      "title": "Source audit: Mathieu-function tools for Dirichlet ellipses",
      "status": "source_audit_required",
      "statement_tex": "Collect exact references and theorem statements for angular Mathieu characteristic values, modified radial Mathieu phases, eccentricity-uniform asymptotics, and certified eigenvalue enclosures.",
      "dependencies": [],
      "implies": [
        "ELLIPSE-near-circular"
      ],
      "blockers": [],
      "source_card": "sources/mathieu_ellipse.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-02.md",
          "sources/seed_reports/background-strategy-03.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Keep this as a parallel source-audit track until the shell Round 1 target theorem memo is stable."
    },
    {
      "id": "ELLIPSE-near-circular",
      "type": "theorem",
      "track": "ellipse_parallel",
      "title": "Parallel flagship target: Dirichlet Pólya for near-circular ellipses",
      "status": "open",
      "statement_tex": "Find e_0>0 such that area-normalized ellipses E_e satisfy N_D(E_e,Lambda) <= |E_e| Lambda/(4 pi) for all Lambda>=0 and 0<=e<=e_0.",
      "dependencies": [
        "SRC-mathieu-ellipse"
      ],
      "implies": [
        "POLYA-program-target"
      ],
      "blockers": [
        "SRC-mathieu-ellipse"
      ],
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-02.md",
          "sources/seed_reports/background-strategy-03.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A3",
      "next_action": "Round 1 may compare risk against shells, but should not make ellipse the primary target unless human steering changes."
    },
    {
      "id": "CERT-certificate-family",
      "type": "theorem",
      "track": "certificate_family",
      "title": "Fallback target: certified non-tiling comparison family",
      "status": "open",
      "statement_tex": "Construct a smooth non-tiling family Omega_eta and prove exact Dirichlet Pólya over a quantified parameter range using explicit Weyl remainders, comparison domains, and certified finite verification.",
      "dependencies": [
        "SRC-jiang-lin"
      ],
      "implies": [
        "POLYA-program-target"
      ],
      "blockers": [
        "SRC-jiang-lin"
      ],
      "evidence": {
        "positive": [
          "sources/seed_reports/Strategy.md",
          "sources/seed_reports/background-strategy-01.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A3",
      "next_action": "Keep as backup route; Round 1 should identify what source audit is required before proposing a concrete family."
    },
    {
      "id": "SRC-jiang-lin",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Source audit: Jiang-Lin epsilon-loss and certificate strategy",
      "status": "source_audit_required",
      "statement_tex": "Record Jiang-Lin theorem statements, explicit thresholds, strip-tiling estimates, and the exact gap between epsilon-loss Pólya and exact pointwise Pólya.",
      "dependencies": [],
      "implies": [
        "CERT-certificate-family"
      ],
      "blockers": [],
      "source_card": "sources/jiang_lin_certificate.md",
      "evidence": {
        "positive": [
          "sources/seed_reports/background-strategy-01.md",
          "sources/seed_reports/Strategy.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Create a source card before using Jiang-Lin as a proof dependency."
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated at repository initialization for run `polya-main`.

## Current Theorem Target

First theorem target:

```text
For A_{rho,1} = {x in R^3 : rho < |x| < 1}, prove
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
for all Lambda >= 0.
```

The strict counting convention is:

```text
N_D(Omega,Lambda) = #{j : lambda_j^D(Omega) < Lambda}.
```

No theorem has been proved by this repository yet.

## Connected Repository Source

The ChatGPT GitHub connector is connected for this project. When available, use `yutianlee/polya-ai-collab` as a source for the current repository files. The most important files for this round are:

- `state/proof_obligations.yml`
- `manifests/reading_packet.md`
- `problems/polya_conjecture.md`
- `sources/seed_reports/`

## Round 1 Target Obligations

- `CONV-strict-counting`
- `TARGET-shell-d3`
- `SRC-FLPS-balls`
- `SRC-annuli`
- `SHELL-cross-product-formula`
- `SHELL-lattice-count`
- `COMP-certified-bessel`

## Do-Not-Claim Rules

- Do not claim Dirichlet Pólya for shells has been proved.
- Do not claim the ellipse theorem or certificate-family theorem has been proved.
- Do not treat floating-point computation as proof.
- Do not use external theorems without source cards recording exact statements and hypotheses.

## Agent Assignments

- `A1`: target theorem memo and source-audit priorities.
- `A2`: shell-route blockers and missing lemmas.
- `A3`: route comparison across shell, ellipse, and certificate tracks.
- `A4`: formula and computation-plan audit.

Use `state/next_round_prompts.md` for the initial agent-specific tasks.

## Relevant Files

- `state/proof_obligations.yml`
- `problems/polya_conjecture.md`
- `sources/seed_reports/Strategy.md`
- `sources/seed_reports/background-strategy-01.md`
- `sources/seed_reports/background-strategy-02.md`
- `sources/seed_reports/background-strategy-03.md`

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Initial prompts for `polya-main` round 1.

Repository source: use the connected GitHub repository `yutianlee/polya-ai-collab` when available. Treat `state/proof_obligations.yml`, `manifests/reading_packet.md`, `problems/polya_conjecture.md`, and `sources/seed_reports/` as the primary repo files for this round.

## For A1

Draft the target theorem memo for exact Dirichlet Pólya on 3D spherical shells. Include the domain, boundary condition, strict counting convention, Weyl constant, scaling normalization, parameter range, source-audit priorities, and a conservative State Patch proposal. Do not claim the theorem is proved.

## For A2

Identify the main analytic blockers for the 3D shell route. Focus on Bessel cross-products, phase functions, turning-point regimes, inner-boundary transition, rho-uniformity, and what must be inherited or rebuilt from the annulus proof. Propose narrow proof obligations, not broad theorem claims.

## For A3

Compare the shell route, the near-circular ellipse route, and the Jiang-Lin-style certificate-family route. Recommend which obligations should be primary after Round 1 and identify route-specific failure modes. Do not promote any route to proved status.

## For A4

Audit formulas and verification requirements: shell eigenvalue equation, d-dimensional order nu, d=3 multiplicity, strict counting convention, Weyl constant, and the minimum certified Bessel root-isolation framework. Treat computation as diagnostic unless it is a certified finite-window obligation.

--- FILE: state/best_proof_draft.md ---
# Best Proof Draft

No proof draft exists yet. Round 1 should produce a target theorem memo and source-audit plan before any proof draft is promoted.

--- FILE: state/lemma_bank.md ---
# Lemma Bank

Initial lemma candidates live in `state/proof_obligations.yml`.

--- FILE: state/gap_register.md ---
# Gap Register

Initial gaps:

- Uniform Bessel cross-product phase enclosures for shells.
- Multiplicity-weighted lattice counts in dimension 3.
- Certified finite-window verification for shell cross-product roots.
- Parameter uniformity in the shell ratio `rho`.
- Mathieu-function source audit for the ellipse parallel track.

--- FILE: sources/flps_balls.md ---
# Source Card: FLPS Euclidean Balls

Status: source audit required.

Purpose: record the exact theorem statements and proof components from Filonov, Levitin, Polterovich, and Sher on Pólya's conjecture for Euclidean balls, disks, and sectors.

Required audit fields:

- bibliographic data;
- theorem statements and boundary conditions;
- counting convention;
- Bessel phase definitions;
- lattice-counting lemmas;
- finite/computer-assisted components;
- dependencies needed for the shell route.

This card is intentionally incomplete at initialization.

--- FILE: sources/bessel_phase_enclosures.md ---
# Source Card: Uniform Bessel Phase And Zero Enclosures

Status: source audit required.

Purpose: record uniform two-sided Bessel phase and zero enclosure statements needed for the FLPS pipeline and for possible shell cross-product extensions.

Required audit fields:

- bibliographic data;
- definitions of phase/modulus functions;
- validity ranges in order and argument;
- explicit constants or computable error terms;
- turning-point and Airy transition statements;
- monotonicity assumptions;
- relevance to cross-product zeros.

This card is intentionally incomplete at initialization.

--- FILE: sources/annuli_polya.md ---
# Source Card: Dirichlet Pólya For Annuli

Status: source audit required.

Purpose: record the exact annulus theorem, Bessel cross-product setup, lattice-counting estimates, and certified finite verification strategy.

Required audit fields:

- bibliographic data;
- annulus theorem statement and parameter range;
- Bessel cross-product eigenvalue equation;
- phase-function estimates;
- trapezoidal floor-sum and concave/convex curve lemmas;
- finite verification method;
- which components might generalize to 3D shells.

This card is intentionally incomplete at initialization.

--- FILE: sources/shell_weyl_bessel.md ---
# Source Card: Bessel Functions And Weyl Law For Balls And Spherical Shells

Status: source audit required.

Purpose: record shell-specific Bessel cross-product zero estimates and Weyl-remainder bounds.

Required audit fields:

- bibliographic data;
- domain and boundary-condition assumptions;
- dimension ranges;
- cross-product or ultraspherical Bessel definitions;
- zero-counting statements;
- Weyl-remainder statements;
- whether estimates are one-sided and explicit enough for Pólya.

This card is intentionally incomplete at initialization.

--- FILE: sources/mathieu_ellipse.md ---
# Source Card: Mathieu Tools For Dirichlet Ellipses

Status: source audit required.

Purpose: collect references and exact theorem statements for the parallel Dirichlet ellipse track.

Required audit fields:

- angular Mathieu characteristic values;
- modified radial Mathieu functions;
- large-parameter and eccentricity-uniform asymptotics;
- radial phase enclosures;
- certified ellipse eigenvalue enclosures;
- limitations for all-eccentricity uniformity.

This card is intentionally incomplete at initialization.

--- FILE: sources/jiang_lin_certificate.md ---
# Source Card: Jiang-Lin Certificate Strategy

Status: source audit required.

Purpose: record quantitative Weyl remainder, epsilon-loss Pólya, strip-tiling, and finite-verification results relevant to a smooth non-tiling comparison family.

Required audit fields:

- bibliographic data;
- theorem statements and constants;
- exact epsilon-loss formulation;
- explicit threshold hypotheses;
- strip/product/comparison-family estimates;
- what remains to remove epsilon-loss and prove exact pointwise Pólya.

This card is intentionally incomplete at initialization.

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

--- HUMAN FILE: human/current_directives.md ---
# Current Directives

Initialize the Pólya AI collaboration with the shell route as the primary target.

Round 1 must not claim a proof. It should establish:

- the strict counting convention;
- the 3D spherical shell target theorem memo;
- source-audit priorities;
- the Bessel cross-product formula audit;
- first analytic blockers;
- certified computation requirements.

The ChatGPT GitHub connector is now connected for this project. In prompts, explicitly tell web agents to use `yutianlee/polya-ai-collab` as a source when available, while treating the prompt bundle and proof-obligation graph as authoritative for the current stage.

--- HUMAN FILE: human/goals.md ---
# Goals

- Build a public proof-obligation workflow for Pólya's conjecture.
- Start with exact Dirichlet Pólya for 3D spherical shells.
- Keep the Dirichlet ellipse/Mathieu route as a parallel flagship track.
- Keep a Jiang-Lin-style certificate family as the lower-risk fallback.

--- HUMAN FILE: human/ideas.md ---
# Ideas

- Reproduce the FLPS disk/ball and annulus machinery before attacking shells.
- Ask A4 to audit the shell eigenvalue formula and multiplicity weights first.
- Ask A3 to compare shell, ellipse, and certificate-family risks before Round 2 route selection.

--- HUMAN FILE: human/references.md ---
# References To Audit

- Filonov, Levitin, Polterovich, Sher: Pólya's conjecture for Euclidean balls.
- FLPS Bessel phase / zero enclosure paper.
- FLPS Dirichlet annuli paper.
- Guo, Jiang, Wang, Yang: Bessel functions and Weyl law for balls and spherical shells.
- Jiang and Lin: epsilon-loss Pólya and quantitative Weyl remainders.
- He and Wang: thin products.
- Filonov: Neumann planar convex-domain result.
- Mathieu-function references for the ellipse route.

## Outputs To Review

--- OUTPUT FROM A2 ---
## Summary

I attack the 3D shell route at the formula level and isolate what is genuinely provable now versus what is a hard open analytic obligation. The central positive finding is that the shell counting function admits an **exact** (not asymptotic) phase representation, and that the difference-of-phases which governs it is **globally strictly monotone** -- a fact I can reduce to one classical Bessel identity (Nicholson). This gives a clean, rigorous floor-sum identity for `N_D(A_{rho,1},Lambda)` valid in all regimes, with no turning-point analysis required for the qualitative structure. The hard part is then quarantined into (i) a *quantitative* two-sided enclosure of that phase, whose only novel danger zone is the shell-specific **inner turning point** `rho*k ~ nu`, and (ii) a genuinely **2D multiplicity-weighted lattice count** carrying the weight `2*ell+1`, which the annulus proof does not supply because the annulus angular sum is effectively 1D. I also record two obstructions with the correct sign: naive domain monotonicity from the ball overshoots by exactly the inner-ball Weyl volume, and the two-term Weyl heuristic is not directly usable because the shell has a positive-measure set of periodic billiard trajectories. I propose narrow obligations, not theorem claims. No Round-1 promotion of any Polya theorem.

## Target proof obligation

Primary: `SHELL-phase-enclosures` (owner A2) and its upstream structural prerequisite, which I propose to split off as a new obligation. Secondary contact: `SHELL-cross-product-formula` (confirm), `SHELL-lattice-count` (scope the 3D-specific gap), `CONV-strict-counting` (endpoint consistency of the floor representation), and `SHELL-rho-uniformity` (record endpoint risks only, per the Round-1 next_action that defers full $\rho$-uniformity).

## Main claim or direction

I claim the shell route should be organized around a two-layer decomposition that I make precise here:

- **Layer 1 (qualitative, provable now).** An exact phase identity plus global monotonicity of the shell phase gives
$$
N_D(A_{\rho,1},\Lambda)=\sum_{\ell\ge0}(2\ell+1)\,\#\{n\ge1: n\pi<\Psi_{\ell+1/2,\rho}(\sqrt{\Lambda})\},
$$
where $\Psi_{\nu,\rho}(k):=\theta_\nu(k)-\theta_\nu(\rho k)$ and $\theta_\nu$ is the Bessel phase. This holds in every spectral regime and needs no Airy analysis.

- **Layer 2 (quantitative, open).** Polya reduces to bounding this weighted floor-sum by the Weyl volume $\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}$, which requires (a) explicit two-sided enclosures of $\Psi_{\nu,\rho}$ uniform in $(\nu,k)$, hardest at the inner turning point, and (b) a 2-parameter weighted lattice estimate in $(\ell,n)$.

The strategic payload: monotonicity of $\Psi$ is *not* an assumption to be hoped for -- it is a theorem I reduce to the decreasing-ness of $M_\nu(z)^2=J_\nu^2+Y_\nu^2$. This removes the single biggest structural worry about the difference-of-phases and lets the team attack Layer 2 with a rigorous scaffold in hand.

## Detailed reasoning

**Setup and confirmation of the spectral formula.** For $A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\}$, separation $u=R(r)Y_\ell^m$ gives the radial equation $R''+\tfrac2r R'+(k^2-\tfrac{\ell(\ell+1)}{r^2})R=0$ with $\Lambda=k^2$. The substitution $R(r)=r^{-1/2}w(r)$ yields Bessel's equation of order $\nu=\ell+\tfrac12$ (matching $\nu=\ell+(d-2)/2$ at $d=3$). Since $r\in[\rho,1]$ is bounded away from $0$, the prefactor $r^{-1/2}$ is nonvanishing and the Dirichlet conditions $R(\rho)=R(1)=0$ are equivalent to the vanishing of the $2\times2$ determinant, i.e.
$$
F_{\nu,\rho}(k)=J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k)=0,\qquad \nu=\ell+\tfrac12 .
$$
Angular multiplicity is $\dim\mathcal H_\ell=2\ell+1$. I therefore **confirm** the formula and multiplicities in `SHELL-cross-product-formula` as written; the primary independent audit remains A4's, but I find no formula error. The scaling reduction to outer radius $R=1$ is legitimate because eigenvalues scale like (length)$^{-2}$.

**Weyl target, computed two independent ways.** With $\omega_3=\tfrac{4\pi}{3}$, $L_3=\omega_3/(2\pi)^3=\tfrac1{6\pi^2}$ and $|A_{\rho,1}|=\tfrac{4\pi}{3}(1-\rho^3)$, so the target RHS is
$$
L_3|A_{\rho,1}|\Lambda^{3/2}=\frac{2(1-\rho^3)}{9\pi}\,\Lambda^{3/2}.
$$
I cross-checked this constant against the WKB radial-action sum (see Verification); they agree exactly, which validates both the constant and the internal consistency of the phase picture.

**Exact phase identity (Layer 1a).** Write the standard Bessel modulus/phase $J_\nu(z)=M_\nu(z)\cos\theta_\nu(z)$, $Y_\nu(z)=M_\nu(z)\sin\theta_\nu(z)$, $M_\nu(z)=\sqrt{J_\nu(z)^2+Y_\nu(z)^2}$. Because $W(J_\nu,Y_\nu)=\tfrac{2}{\pi z}\ne0$, $J_\nu$ and $Y_\nu$ have no common zero, so $M_\nu(z)>0$ for all $z>0$. Then a one-line trig identity gives the **exact** factorization
$$
F_{\nu,\rho}(k)=M_\nu(\rho k)\,M_\nu(k)\,\sin\!\big(\theta_\nu(k)-\theta_\nu(\rho k)\big).
$$
Since the moduli are strictly positive, the zeros of $F_{\nu,\rho}$ are *exactly* the solutions of $\Psi_{\nu,\rho}(k):=\theta_\nu(k)-\theta_\nu(\rho k)\in\pi\mathbb Z$. This is the shell analogue of the FLPS/Sher exact spectral-to-lattice correspondence, and it is exact for finite $k$, not merely asymptotic.

**Global monotonicity of the shell phase (Layer 1b).** The phase derivative is $\theta_\nu'(z)=\tfrac{W}{M_\nu^2}=\tfrac{2}{\pi z M_\nu(z)^2}>0$. Hence
$$
\Psi_{\nu,\rho}'(k)=\theta_\nu'(k)-\rho\,\theta_\nu'(\rho k)
=\frac{2}{\pi k}\left(\frac{1}{M_\nu(k)^2}-\frac{1}{M_\nu(\rho k)^2}\right).
$$
The bracket is positive iff $M_\nu(\rho k)^2>M_\nu(k)^2$. Now invoke the classical fact that $z\mapsto M_\nu(z)^2=J_\nu(z)^2+Y_\nu(z)^2$ is **strictly decreasing** on $(0,\infty)$ for every real $\nu\ge0$. This follows from Nicholson's integral
$$
J_\nu(z)^2+Y_\nu(z)^2=\frac{8}{\pi^2}\int_0^\infty K_0(2z\sinh t)\cosh(2\nu t)\,dt,
$$
whose integrand is strictly decreasing in $z$ (as $K_0'<0$ and $2z\sinh t$ increases with $z$). Since $k>\rho k$, we get $M_\nu(\rho k)^2>M_\nu(k)^2$, hence $\Psi_{\nu,\rho}'(k)>0$ for all $k>0$, all $\nu\ge0$, all $\rho\in(0,1)$.

The consequence is decisive: $\Psi_{\nu,\rho}$ is a strictly increasing continuous function with $\Psi_{\nu,\rho}(0^+)=0$ (both $\theta_\nu(k),\theta_\nu(\rho k)\to$ the same small-argument limit, chosen on a common branch) and $\Psi_{\nu,\rho}(k)\to\infty$. Therefore the radial count is an honest floor:
$$
N_\ell(\sqrt{\Lambda})=\#\{n\ge1:\ n\pi<\Psi_{\ell+1/2,\rho}(\sqrt{\Lambda})\},
$$
and, for the Dirichlet **upper** bound, one may use $N_\ell(\sqrt\Lambda)\le\big\lfloor \Psi_{\ell+1/2,\rho}(\sqrt\Lambda)/\pi\big\rfloor$ (equality off a measure-zero set of $\Lambda$).

The crucial methodological point: the qualitative floor structure requires **no** turning-point/Airy analysis and holds uniformly across oscillatory, turning, inner-transition, and evanescent regimes, because Nicholson's monotonicity is regime-blind. Regime analysis is needed only to *quantitatively enclose* $\Psi$, not to justify the counting representation. This cleanly separates a provable structural lemma from the hard analytic estimate.

**A priori angular cutoff.** The radial Rayleigh quotient with weight $r^2\,dr$ obeys, for $R\in H^1_0((\rho,1),r^2dr)$,
$$
\frac{\int_\rho^1[(R')^2+\tfrac{\ell(\ell+1)}{r^2}R^2]r^2dr}{\int_\rho^1 R^2 r^2 dr}>\ell(\ell+1)\frac{\int R^2 dr}{\int R^2 r^2 dr}\ge \ell(\ell+1),
$$
since $r^2\le1$. Hence $N_\ell(\sqrt\Lambda)=0$ whenever $\ell(\ell+1)\ge\Lambda$. The $\ell$-sum is thus finite with at most $\sim\sqrt\Lambda$ terms -- a clean rigorous truncation, independent of any asymptotics.

**Reduction to a 2D weighted lattice count (Layer 2).** Combining the above,
$$
N_D(A_{\rho,1},\Lambda)\le\sum_{0\le\ell<\sqrt\Lambda}(2\ell+1)\left\lfloor\frac{\Psi_{\ell+1/2,\rho}(\sqrt\Lambda)}{\pi}\right\rfloor .
$$
Polya is the statement that this is $\le\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}$. Two things must be controlled:

1. **Phase enclosure.** In the classically allowed regime the Debye/WKB form is
$$
\Psi_{\nu,\rho}(k)=\int_{\max(\rho,\nu/k)}^{1}\sqrt{k^2-\tfrac{\nu^2}{r^2}}\,dr+\text{(boundary/Maslov phase shift)}+E_{\nu,\rho}(k),
$$
with a hard-wall phase at $r=1$ (and at $r=\rho$ when $\nu/k<\rho$) and a soft-turning-point contribution when $\nu/k\in(\rho,1)$. The Dirichlet boundary phase enters with the sign that produces a **negative** two-term Weyl correction, which is favorable for Polya. The enclosure error $E_{\nu,\rho}$ must be explicit and uniform.

2. **Weighted floor-sum.** Even with a perfect phase, one must bound the discrete weighted sum by the continuous integral. Dropping the floor via $\lfloor x\rfloor\le x$ is *not* enough by itself: it yields the phase-space integral, which equals the leading Weyl term but leaves the two-term and fractional-part corrections uncontrolled. Polya lives precisely in those corrections. The weight $2\ell+1$ makes this a genuine 2D lattice problem.

## Theorem-dependency audit

- **Bessel modulus/phase definitions and $\theta_\nu'=2/(\pi z M_\nu^2)$**: standard; must be pinned in source card `SRC-bessel-phase`. Used in Layer 1a/1b. Status of dependency: external, needs card.
- **Nicholson's formula / strict decrease of $M_\nu(z)^2$**: classical (DLMF 10.18; Watson). This is the load-bearing external fact for `SHELL-phase-monotonicity`. I recommend adding it explicitly to `SRC-bessel-phase` with the exact integral and the sign argument. Until carded, the monotonicity lemma should be `derived_under_assumptions`.
- **FLPS single-Bessel uniform phase/zero enclosures (SIAM 2024)**: needed for the *quantitative* enclosure of $\theta_\nu(k)$ and $\theta_\nu(\rho k)$ separately. Half-integer orders $\nu=\ell+1/2$ are inside their stated range; the card `SRC-bessel-phase` must confirm the validity range in order and argument and the explicitness of constants, especially through the Airy/turning zone.
- **FLPS ball Polya (Invent. 2023)**: used only for the $\rho\to0$ consistency limit and for the obstruction analysis, not as a direct dependency of the shell inequality. Card `SRC-FLPS-balls`.
- **Annulus proof (JLMS 2026), trapezoidal floor-sum / concave--convex curve lemmas**: these apply to the **radial** floor over $n$ but are **1D in the angular index**; the shell needs a new estimate in $\ell$ carrying the weight $2\ell+1$. Card `SRC-annuli` must separate which lemmas are dimension-independent (radial floor sums) from which rely on planar uniform multiplicity (angular sum). This is the sharpest dependency caveat of the round.
- **Guo--Jiang--Wang--Yang shell/ball Bessel--Weyl (to appear)**: potential source for cross-product zero counts and $\rho$-uniform inputs, but its statements are (per the seed reports) Weyl-remainder bounds, which are two-sided/averaged, not necessarily one-sided-explicit enough for pointwise Polya. Card `SRC-shell-weyl` must record explicitly whether any statement is one-sided with computable constants.

No dependency currently licenses a theorem-level claim. All shell obligations remain open/derived-under-assumptions.

## Hidden assumptions and potential gaps

- **Branch/continuity of $\theta_\nu$ and of $\Psi_{\nu,\rho}(0^+)=0$.** The floor identity needs a globally continuous phase with the correct base point. This is standard but must be stated, not assumed; a mis-set branch shifts every count by an integer per $\ell$.
- **Differencing loss in the enclosure.** Enclosing $\theta_\nu(k)$ and $\theta_\nu(\rho k)$ independently and subtracting can lose precision when both are large. In the deep oscillatory regime the $\nu$-dependent parts cancel ($\Psi\approx k(1-\rho)$), so absolute errors add benignly; the danger is when $\rho k$ sits in the Airy/evanescent zone while $k$ oscillates. This is the **inner turning-point regime** and is the primary novel analytic risk. I flag it as its own obligation rather than folding it into a generic "phase enclosure."
- **Weight concentration at the inner turning point.** The band $\ell\sim\rho k$ contains $O(\rho k)$ values of $\ell$, each with weight $O(\rho k)$, so this regime carries weight $O((\rho k)^2)$ of the total $O(k^3)$ -- not negligible. Any $O(1)$-per-mode slack here scales to $O((\rho k)^2)$ and could break the pointwise inequality if mishandled.
- **Endpoint uniformity.** As $\rho\to1$ the shell degenerates to a thin spherical slab; the number of contributing $\ell$ near threshold grows and enclosure constants may blow up. As $\rho\to0$ the $\ell=0$ term is delicate: $Y_{1/2}(\rho k)=-\sqrt{2/(\pi\rho k)}\cos(\rho k)$ is singular as $\rho\to0$, so uniformity of the inner-boundary contribution down to $\rho=0$ is not automatic. Per the Round-1 next_action, I only *record* these; I do not attack $\rho$-uniformity now.
- **Strict vs non-strict at eigenvalue jumps.** The upper bound uses $\lfloor\Psi/\pi\rfloor\ge$ strict count, which is safe for proving $N_D\le$ Weyl; but the convention must be fixed once in `CONV-strict-counting` and used identically in the eigenvalue form $\lambda_k\ge C k^{2/3}$. Worst case is $\Lambda$ just above a degenerate level.

## Counterexample or obstruction search

- **Obstruction 1 -- domain monotonicity overshoots.** $A_{\rho,1}\subset B_1$ gives, for Dirichlet, $N_D(A_{\rho,1},\Lambda)\le N_D(B_1,\Lambda)\le L_3|B_1|\Lambda^{3/2}$, which exceeds the target by $L_3|B_\rho|\Lambda^{3/2}$. Dirichlet bracketing sharpens this to $N_D(B_\rho,\Lambda)+N_D(A_{\rho,1},\Lambda)\le N_D(B_1,\Lambda)$, i.e.
$$
N_D(A_{\rho,1},\Lambda)\le N_D(B_1,\Lambda)-N_D(B_\rho,\Lambda).
$$
Reaching the target this way would require $N_D(B_\rho,\Lambda)\ge L_3|B_\rho|\Lambda^{3/2}$, i.e. a *reverse* Polya for the inner ball, which is false (Dirichlet counts lie below Weyl). So pure monotonicity/bracketing is provably lossy by the inner-ball Dirichlet deficit. This is a real obstruction and should be recorded as negative evidence against a "reduce to the ball" shortcut.
- **Obstruction 2 -- two-term Weyl heuristic is not directly usable.** The shell boundary is smooth (two disjoint spheres, no edges), so one might hope for a clean $N_D=\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}-\tfrac{1+\rho^2}{4}\Lambda+o(\Lambda)$ with a favorable negative boundary term. But the shell billiard has a **positive-measure family of periodic trajectories** (radial bounces between the spheres; grazing/tangent-to-inner-sphere rays), so the second Weyl term is not a clean monomial and oscillates. This is exactly the phenomenon that forced the exact lattice approach for the disk. Conclusion: Strategy B (two-term + threshold) is not a safe standalone route for shells; the exact phase/lattice method (Strategy A) is the correct spine.
- **No counterexample to the target expected.** The favorable sign of the Dirichlet boundary term and the exact floor structure make the inequality plausible with margin at high energy; the residual risk is entirely low-energy and inner-turning-point behavior, which is the province of certified computation plus tight enclosures. I did not find any mechanism (analogous to the constant-magnetic-field Landau counterexample for general Polya) that operates on the Dirichlet shell.

## Verification

- **Phase identity**: verified by direct substitution $J=M\cos\theta,\ Y=M\sin\theta$ into $F_{\nu,\rho}$; the bracket collapses to $\sin(\theta_\nu(k)-\theta_\nu(\rho k))$. ✓
- **Monotonicity sign**: verified $\theta_\nu'=2/(\pi zM_\nu^2)>0$ from the Wronskian, and $\Psi'=\tfrac{2}{\pi k}(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2})$; positive because $M_\nu^2$ strictly decreasing (Nicholson). ✓
- **Weyl constant, WKB cross-check.** Using $N_\ell\approx\tfrac1\pi\int_{\max(\rho,\nu/k)}^1\sqrt{k^2-\nu^2/r^2}\,dr$ and $\sum_\ell(2\ell+1)\to\int_0^\infty 2\nu\,d\nu$, swap order and integrate $\nu$ first over $[0,kr]$: with $u=\nu^2/r^2$, $\int_0^{kr}2\nu\sqrt{k^2-\nu^2/r^2}\,d\nu=r^2\int_0^{k^2}\sqrt{k^2-u}\,du=\tfrac23 r^2 k^3$. Then $\tfrac1\pi\int_\rho^1\tfrac23 r^2k^3\,dr=\tfrac{2k^3}{9\pi}(1-\rho^3)=\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}$. This matches the phase-space Weyl term exactly. ✓ Independent confirmation of both the constant and the phase normalization.
- **Deep-oscillatory sanity.** For $\nu\ll\rho k$, $\Psi_{\nu,\rho}(k)\approx k(1-\rho)$, so radial zeros at $k\approx n\pi/(1-\rho)$ -- the 1D slab spectrum of width $1-\rho$. ✓ Physically correct.
- **High-$\ell$ evanescent sanity.** For $\rho k\ll\nu$, $Y_\nu(\rho k)$ dominates and $F_{\nu,\rho}(k)\approx -Y_\nu(\rho k)J_\nu(k)$, so zeros $\to$ zeros of $J_\nu(k)$: the ball-mode limit. ✓ Consistent with the inner boundary being invisible to high-angular-momentum modes.
- **A priori cutoff**: verified via the weighted Rayleigh quotient that $N_\ell=0$ for $\ell(\ell+1)\ge\Lambda$. ✓

All verifications are consistency checks and structural proofs; none constitutes a proof of the target inequality, and I do not claim one.

## Divergent alternatives and 20% exploration

1. **Interface-bracketing as a quantitative reformulation (not a shortcut).** Obstruction 1 shows $N_D(A_{\rho,1})\le N_D(B_1)-N_D(B_\rho)$. Rather than discard it, use it as an *upper control*: shell Polya is implied by $N_D(B_1,\Lambda)-N_D(B_\rho,\Lambda)\le L_3|A_{\rho,1}|\Lambda^{3/2}$, i.e. by a *sharp two-term-with-sign* comparison of two ball counts. This is a different decomposition of the same difficulty and might be attackable using FLPS's two-term ball bound (which the annulus paper already produces). Quick falsification test: numerically check whether $N_D(B_1,\Lambda)-N_D(B_\rho,\Lambda)-L_3|A_{\rho,1}|\Lambda^{3/2}$ stays $\le0$ with margin; if it is frequently positive, this route is dead and only the direct phase count survives.

2. **Laptev-style product/monotonicity lift for the thin-shell endpoint.** As $\rho\to1$ the shell is close to $S^2\times(\rho,1)$ (a thin product). He--Wang thin-product Polya and Laptev's "$\Omega_1$ Polya $\Rightarrow\Omega_1\times\Omega_2$ Polya" could give the $\rho\to1$ endpoint by a soft argument, decoupling it from the cross-product enclosures. Needed lemma: quantitative comparison between shell eigenvalues and product eigenvalues with curvature corrections controlled. Falsification: if the curvature (metric-distortion) correction is larger than the spectral gaps used, the lift fails.

3. **Sturm--Liouville oscillation instead of special-function asymptotics.** The radial count $N_\ell(\sqrt\Lambda)$ is exactly the number of interior zeros of the Prufer angle for the radial ODE at energy $\Lambda$. One can bound $N_\ell$ directly by Sturm comparison against solvable potentials (constant, or $c/r^2$) without Debye asymptotics, obtaining rigorous one-sided bounds on $\Psi_{\nu,\rho}/\pi$. This trades sharp asymptotics for robust inequalities and may be enough for the *upper* bound. Needed lemma: a Sturm comparison giving $N_\ell(\sqrt\Lambda)\le \tfrac1\pi\int_{\max(\rho,\nu/k)}^1\sqrt{k^2-\nu^2/r^2}\,dr+c_\ell$ with summable/controlled $c_\ell$. Falsification: if the accumulated $\sum(2\ell+1)c_\ell$ exceeds the $O(\Lambda)$ boundary cushion, this is too lossy.

4. **Certificate-family cross-check.** Independently, treat the shell as a test case for the Jiang--Lin $\varepsilon$-loss machinery: their explicit Weyl remainder for Lipschitz domains applies to the shell and yields a computable threshold for $\varepsilon$-loss Polya. This does not remove $\varepsilon$, but it gives a rigorous high-energy anchor and a threshold $\Lambda_0(\rho,\varepsilon)$ to hand to certified computation. Falsification: if their threshold is astronomically large or blows up as $\rho\to0,1$, it is not a usable anchor.

Each alternative is scoped to attack one blocker (endpoint, enclosure robustness, or high-energy anchoring); none is proposed as a full route, and each has a stated quick falsifier.

## Useful lemmas

- **L1 (exact phase factorization).** For $\nu\ge0$, $\rho\in(0,1)$, $k>0$: $F_{\nu,\rho}(k)=M_\nu(\rho k)M_\nu(k)\sin(\theta_\nu(k)-\theta_\nu(\rho k))$; zeros $\iff\Psi_{\nu,\rho}(k)\in\pi\mathbb Z$. (Elementary given phase/modulus definitions.)
- **L2 (global monotone shell phase).** $\Psi_{\nu,\rho}$ is strictly increasing on $(0,\infty)$, with $\Psi_{\nu,\rho}(0^+)=0$; proof via $\Psi'=\tfrac{2}{\pi k}(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2})>0$ using strict decrease of $M_\nu^2$ (Nicholson). Depends on carding Nicholson.
- **L3 (exact floor count).** $N_D(A_{\rho,1},\Lambda)=\sum_{\ell}(2\ell+1)\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(\sqrt\Lambda)\}\le\sum_\ell(2\ell+1)\lfloor\Psi_{\ell+1/2,\rho}(\sqrt\Lambda)/\pi\rfloor$. Depends on L1, L2, CONV.
- **L4 (a priori angular cutoff).** $N_\ell(\sqrt\Lambda)=0$ if $\ell(\ell+1)\ge\Lambda$. (Weighted Rayleigh quotient.) Proved.
- **L5 (target normalization).** $L_3|A_{\rho,1}|\Lambda^{3/2}=\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}$, confirmed by WKB action. Proved.

L1, L4, L5 are effectively proved now (modulo standard definitions). L2 is proved modulo one carded classical identity. L3 follows from L1--L2. These are the rigorous scaffold; the open lemmas below are the real work.

## What should be tested next

- **A2 next:** promote L1, L4, L5 to internal status once definitions are carded; formulate L2 as `SHELL-phase-monotonicity` with Nicholson as its sole external dependency; then formulate the **first fixed-$\rho$ high-energy proposition** as a *quantitative* enclosure of $\Psi_{\nu,\rho}$ split by regime, with the inner turning point isolated.
- **A3 (owner of `SHELL-lattice-count`):** determine exactly which annulus floor-sum/curve-counting lemmas are 1D-in-$\ell$ and therefore do NOT transfer, and state the new 2-parameter weighted lattice estimate needed for the $2\ell+1$ weight. Compare shell vs ellipse vs certificate risk with this concrete 2D-count obligation in view.
- **A4:** (i) confirm the cross-product formula and $m_{\ell,3}=2\ell+1$; (ii) specify the certified stack for isolating cross-product roots (interval Bessel evaluation, Newton/Krawczyk on $F_{\nu,\rho}$) and a first smoke-test: verify $N_D(A_{\rho,1},\Lambda)\le\tfrac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}$ for a fixed $\rho$ (e.g. $\rho=1/2$) up to a modest $\Lambda_0$, treating output as diagnostic only; (iii) numerically stress-test Obstruction-1 alternative (route 1 above).
- **All:** run the two obstruction diagnostics (domain-monotonicity overshoot magnitude; presence of oscillatory second Weyl term) to confirm Strategy A is the spine.

## Proposed state patch, if any

I propose the following, using ids from `state/proof_obligations.yml`; the judge decides on inclusion. I claim no theorem.

- Add `SHELL-exact-phase-rep` -- type lemma, track shell_analytic, status `derived_under_assumptions`. Statement: $F_{\nu,\rho}(k)=M_\nu(\rho k)M_\nu(k)\sin(\theta_\nu(k)-\theta_\nu(\rho k))$ with $M_\nu>0$, so zeros are exactly $\Psi_{\nu,\rho}(k)\in\pi\mathbb Z$. Dependencies: `SHELL-cross-product-formula`, `SRC-bessel-phase`. Evidence: this reasoning (Verification: substitution). next_action: card the phase/modulus definitions; then promote to `proved_internal`.
- Add `SHELL-phase-monotonicity` -- type lemma, track shell_analytic, status `derived_under_assumptions`. Statement: $\Psi_{\nu,\rho}$ strictly increasing on $(0,\infty)$ for all $\nu\ge0,\rho\in(0,1)$, via $\Psi'=\tfrac{2}{\pi k}(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2})>0$ and strict decrease of $M_\nu^2$. Dependencies: `SHELL-exact-phase-rep`, `SRC-bessel-phase` (must include Nicholson). Blockers: `SRC-bessel-phase`. next_action: add Nicholson's integral and sign argument to the Bessel source card.
- Add `SHELL-count-floor-identity` -- type lemma, track shell_analytic, status `derived_under_assumptions`. Statement: L3 above (exact count and the floor upper bound), with the strict-counting endpoint rule. Dependencies: `SHELL-exact-phase-rep`, `SHELL-phase-monotonicity`, `CONV-strict-counting`. next_action: verify endpoint convention consistency with the eigenvalue form.
- Add `SHELL-inner-turning` -- type lemma, track shell_analytic, status `open`. Statement: uniform two-sided control of $\theta_\nu(\rho k)$ and of the difference $\Psi_{\nu,\rho}$ when $\rho k$ lies within $O(\nu^{1/3})$ of $\nu$, with explicit error, robust under differencing against the oscillatory outer argument. Dependencies: `SHELL-phase-enclosures`, `SRC-bessel-phase`, `SRC-shell-weyl`. Blockers: `SRC-bessel-phase`, `SRC-shell-weyl`. next_action: check whether FLPS single-Bessel Airy enclosures survive subtraction here; this is the primary novel analytic risk.
- Refine `SHELL-phase-enclosures` (owner A2) next_action: attack the *fixed-$\rho$ high-energy* enclosure of $\Psi_{\nu,\rho}$ in four regimes (oscillatory $\rho k>\nu+\nu^{1/3+\delta}$; outer turning $k\sim\nu$; inner turning $\rho k\sim\nu$ -- delegate to `SHELL-inner-turning`; evanescent $\rho k<\nu-\nu^{1/3+\delta}$), and explicitly note the differencing-loss caveat.
- Refine `SHELL-lattice-count` (owner A3) statement/next_action to flag that the $2\ell+1$ weight makes this a **2-parameter** weighted lattice count and that annulus angular estimates are 1D and do not transfer; the radial floor-sum lemmas may transfer.
- Refine `SRC-bessel-phase` required-audit fields to include: Nicholson's formula and strict decrease of $M_\nu^2$; the identity $\theta_\nu'=2/(\pi zM_\nu^2)$; validity range at half-integer orders through the Airy zone.
- Add negative-evidence notes (not obligations) to `TARGET-shell-d3`: (i) domain-monotonicity/bracketing bound $N_D(A_{\rho,1})\le N_D(B_1)-N_D(B_\rho)$ overshoots by the inner-ball Dirichlet deficit; (ii) positive-measure periodic shell billiards imply an oscillatory second Weyl term, so a bare two-term threshold argument is insufficient. Record under evidence.negative / inconclusive as the judge sees fit.

No obligation is proposed for promotion to `proved_internal` in this round beyond the elementary L1/L4/L5 once carded; no Polya theorem is claimed.

## Confidence

- L1 (exact factorization): very high; elementary and verified by substitution.
- L4 (angular cutoff), L5 (Weyl constant via two methods): very high; both directly checked.
- L2 (global monotonicity of $\Psi$): high, contingent on the standard status of Nicholson's monotonicity of $M_\nu^2$; I am confident the classical fact holds for all $\nu\ge0$, but I mark it derived-under-assumptions until carded.
- L3 (floor identity): high, following from L1--L2 plus a stated endpoint convention.
- Obstruction 1 (monotonicity overshoot) and Obstruction 2 (oscillatory second term): high; both are structural.
- Overall route viability (Strategy A spine for shells): moderately high. The qualitative reduction is clean and rigorous; the residual risk is concentrated in `SHELL-inner-turning` and the 2D weighted `SHELL-lattice-count`, which are the correct places to spend Rounds 2--3. I do not assign confidence to the target theorem itself and make no proof claim.

--- OUTPUT FROM A3 ---
## Summary

This Stage A independent reasoning memo provides a rigorous, conservative, and deeply skeptical audit of the proposed routes for the Polya AI collaboration, focusing on the exact Dirichlet Polya conjecture for 3D spherical shells, near-circular ellipses, and Jiang-Lin-style certificate families. As the independent deep-think critic (A3), my primary objective is to surface hidden assumptions, missing hypotheses, parameter-uniformity gaps, and finite-verification risks before any route is prematurely promoted.

The analysis concludes that while the 3D spherical shell route (`TARGET-shell-d3`) is the most mathematically mature candidate, it faces severe, currently unmitigated risks regarding the $2\ell+1$ multiplicity weighting in the lattice-counting step. The standard 2D annulus floor-sum convexity arguments do not trivially generalize to 3D volumes of revolution. The parallel ellipse route (`ELLIPSE-near-circular`) is heavily obstructed by the lack of uniform, one-sided phase enclosures for modified Mathieu functions across all eccentricities. The certificate-family route (`CERT-certificate-family`) remains the safest fallback but requires a fundamental breakthrough to close the $\epsilon$-loss gap inherent in strip-tiling geometries.

No theorem is ready for proof. The state patch proposes splitting the shell lattice-count obligation into continuous phase-space matching and discrete fractional-part bounding, while formally registering the identified obstructions as blocking obligations.

## Target proof obligation

This memo addresses the following target proof obligations as assigned in the Round 1 reading packet and judge prompt:
1.  **`SHELL-lattice-count`**: Specifically, identifying which annulus floor-sum estimates survive the $d=3$ multiplicity weight and which require new lemmas.
2.  **`ELLIPSE-near-circular`**: Evaluating the viability of the Mathieu-function parallel track and its source-audit risks.
3.  **`CERT-certificate-family`**: Assessing the fallback Jiang-Lin-style certificate family and its computational risks.
4.  **Route Comparison**: A global comparative audit of the shell, ellipse, and certificate routes to recommend primary obligations for Round 2.

## Main claim or direction

**Main Claim:** The direct translation of the FLPS 2D annulus proof architecture to 3D spherical shells will fail at the lattice-counting stage unless a new, multiplicity-weighted fractional-part bounding lemma is introduced.

**Direction:** The project must prioritize the analytic resolution of the $2\ell+1$ weighted floor sum (`SHELL-lattice-count`) before investing heavy computational resources into certified Bessel root isolation (`COMP-certified-bessel`). If the analytic high-energy bound cannot be closed due to the multiplicity weight shifting the center of mass of the lattice errors, the shell route will be permanently blocked. Concurrently, the ellipse route should be kept strictly in the source-audit phase, as the uniform asymptotic theory of Mathieu functions is likely insufficient for exact, one-sided Polya bounds. The certificate family should be refined to search for a specific, highly symmetric non-tiling domain where the Weyl remainder can be computed exactly without $\epsilon$-loss.

## Detailed reasoning

### Fundamental Formulas and Conventions

To ensure strict adherence to the project's mathematical discipline, we first establish the authoritative formulas for the 3D spherical shell.

**1. Domain and Boundary Condition:**
The 3D spherical shell is defined as $A_{\rho,1} = \{x \in \mathbb{R}^3 : \rho < |x| < 1\}$ for a fixed parameter $\rho \in (0,1)$. We impose Dirichlet boundary conditions $u = 0$ on $\partial A_{\rho,1} = \{|x|=\rho\} \cup \{|x|=1\}$.

**2. Strict Counting Convention:**
We enforce the strict counting convention for the eigenvalues of the negative Laplacian $-\Delta$:
$$N_D(\Omega, \Lambda) = \#\{j : \lambda_j^D(\Omega) < \Lambda\}$$
*(Note: This strict inequality is critical. Any equivalent formulation using $k = \sqrt{\Lambda}$ must use $k^2 < \Lambda$, not $k^2 \le \Lambda$.)*

**3. Weyl Normalization:**
The target Polya inequality is $N_D(A_{\rho,1}, \Lambda) \le L_3 |A_{\rho,1}| \Lambda^{3/2}$.
The Weyl constant in dimension $d$ is $L_d = \omega_d / (2\pi)^d$, where $\omega_d$ is the volume of the unit ball in $\mathbb{R}^d$.
For $d=3$, $\omega_3 = 4\pi/3$.
$$L_3 = \frac{4\pi/3}{(2\pi)^3} = \frac{4\pi}{24\pi^3} = \frac{1}{6\pi^2}$$
The volume of the shell is $|A_{\rho,1}| = \frac{4\pi}{3}(1 - \rho^3)$.
Thus, the target bound is:
$$N_D(A_{\rho,1}, \Lambda) \le \frac{2}{9\pi} (1 - \rho^3) \Lambda^{3/2}$$
*(Status: Verified. These constants are standard and correct.)*

**4. 3D Spherical Shell Eigenvalue Condition:**
Separation of variables in spherical coordinates $(r, \theta, \phi)$ yields the radial equation. The solutions are spherical Bessel functions $j_\ell(kr)$ and $y_\ell(kr)$. The Dirichlet boundary conditions at $r=\rho$ and $r=1$ require the determinant of the coefficient matrix to vanish, leading to the cross-product equation:
$$j_\ell(\rho k) y_\ell(k) - y_\ell(\rho k) j_\ell(k) = 0$$
Using the relation to standard Bessel functions, $j_\ell(z) = \sqrt{\pi/(2z)} J_{\ell+1/2}(z)$ and $y_\ell(z) = \sqrt{\pi/(2z)} Y_{\ell+1/2}(z)$, the condition is equivalent to the zeros of:
$$F_{\nu,\rho}(k) = J_\nu(\rho k) Y_\nu(k) - Y_\nu(\rho k) J_\nu(k) = 0$$
where the order is $\nu = \ell + 1/2$ for $\ell = 0, 1, 2, \dots$.
*(Status: Verified. The factor $\sqrt{\pi/(2z)}$ cancels out in the cross-product equation $F_{\nu,\rho}(k)=0$.)*

**5. Angular Multiplicities:**
The multiplicity of each radial eigenvalue for a given angular momentum quantum number $\ell$ is the dimension of the space of spherical harmonics of degree $\ell$ in $d=3$:
$$m_{\ell,3} = 2\ell + 1$$
*(Status: Verified.)*

**6. The Master Counting Formula:**
Combining the above, the exact counting function is:
$$N_D(A_{\rho,1}, \Lambda) = \sum_{\ell=0}^\infty (2\ell + 1) \#\{k > 0 : F_{\ell+1/2, \rho}(k) = 0, k^2 < \Lambda\}$$
*(Status: Needs verification regarding the exact handling of $k=0$. Since $J_\nu(0)=0$ and $Y_\nu(0)$ is singular, $k=0$ is never an eigenvalue. The strict inequality $k^2 < \Lambda$ correctly matches the strict counting convention.)*

### Route Comparison Table

| Feature / Risk Profile | 3D Spherical Shells (`TARGET-shell-d3`) | Near-Circular Ellipses (`ELLIPSE-near-circular`) | Certificate Family (`CERT-certificate-family`) |
| :--- | :--- | :--- | :--- |
| **Domain Geometry** | Non-tiling, highly symmetric, parameterized by $\rho \in (0,1)$. | Non-tiling, parameterized by eccentricity $e \in (0,1)$. | Smooth, non-tiling, parameterized by deformation $\eta$. |
| **Spectral Separation** | Exact separation via spherical harmonics and Bessel cross-products. | Exact separation via Mathieu functions (angular and radial). | No exact separation; relies on domain monotonicity and Weyl remainders. |
| **Phase Enclosures** | Requires uniform bounds on Bessel cross-products across oscillatory/transition regimes. | Requires uniform bounds on modified Mathieu functions across all $q$ and $e$. | N/A (Uses geometric strip-tiling and Dirichlet-Neumann bracketing). |
| **Lattice Counting** | 3D volume of revolution count; heavily weighted by $2\ell+1$ multiplicity. | 2D area count; multiplicity is 1 or 2 (even/odd parity). | N/A (Relies on continuous Weyl volume integration). |
| **Primary Analytic Blocker** | Multiplicity-weighted fractional-part floor sum convexity failure. | Lack of uniform, one-sided asymptotic expansions for Mathieu characteristic values. | The $\epsilon$-loss gap in the Jiang-Lin quantitative Weyl remainder. |
| **Computational Risk** | High $\ell$ interval arithmetic wrapping effect; $\rho \to 0, 1$ limits. | Extreme complexity in certified Mathieu root isolation in the complex plane. | High-dimensional parameter space optimization for the certificate domain. |
| **Overall Viability** | **High**, but requires a novel 3D lattice-counting lemma. | **Low**, blocked by fundamental gaps in special function theory. | **Medium**, safe fallback but requires a theoretical breakthrough in Weyl bounds. |

### Claim Ledger

The following ledger evaluates 10 critical claims and assumptions currently embedded in the project state or implied by the strategy.

1.  **Claim:** The FLPS 2D annulus proof architecture can be directly lifted to 3D shells by simply changing the order $\nu$ and adding a multiplicity weight.
    *   **Status:** `rejected` (as a direct lift).
    *   **Risk:** Severe.
    *   **Analysis:** The 2D annulus proof relies on the sum $\sum_{\ell} \lfloor \Phi_\ell(k)/\pi \rfloor$. The 3D shell requires $\sum_{\ell} (2\ell+1) \lfloor \Phi_{\ell+1/2}(k)/\pi \rfloor$. The $2\ell+1$ weight fundamentally alters the geometry of the lattice count, shifting it from a 2D area problem to a 3D volume problem. Convexity arguments that bound the fractional part in 2D do not automatically hold when weighted by $2\ell+1$.
2.  **Claim:** Uniform Bessel phase enclosures $\Phi_{\nu,\rho}(k)$ exist and provide strictly one-sided bounds for the cross-product zeros.
    *   **Status:** `derived_under_assumptions`.
    *   **Risk:** High.
    *   **Analysis:** While FLPS established this for $J_\nu(k)$, the cross-product $F_{\nu,\rho}(k)$ involves four Bessel functions. The phase of the cross-product is the difference of the phases of the individual cylinder functions. Proving that the error terms in the uniform asymptotic expansions (e.g., Olver's Airy approximations) combine to yield a *strictly one-sided* bound for the roots is a massive, unproven analytic obligation.
3.  **Claim:** The strict counting convention $N_D(\Omega, \Lambda) = \#\{\lambda_j < \Lambda\}$ is safe from endpoint jump discontinuities.
    *   **Status:** `open`.
    *   **Risk:** Moderate.
    *   **Analysis:** If $\Lambda$ exactly equals an eigenvalue, the strict inequality drops it. The Polya conjecture $N_D \le L_d |\Omega| \Lambda^{d/2}$ must hold for *all* $\Lambda \ge 0$. If we prove it for $\Lambda \notin \sigma(-\Delta)$, we must ensure the left-hand limit at eigenvalues does not violate the bound. Since $N_D$ is left-continuous under strict counting, this is generally safe, but requires explicit formalization.
4.  **Claim:** Certified interval arithmetic can close the low-energy window for the shell.
    *   **Status:** `diagnostic_only`.
    *   **Risk:** High.
    *   **Analysis:** The cross-product $F_{\nu,\rho}(k)$ is highly oscillatory for large $k$ and exponentially decaying in the evanescent regime ($k < \nu$). Interval arithmetic (IA) suffers from the wrapping effect and dependency problems. Evaluating $J_\nu(\rho k) Y_\nu(k) - Y_\nu(\rho k) J_\nu(k)$ directly in IA will lead to catastrophic cancellation and massive overestimation of intervals, failing to isolate roots tightly enough to prove the strict Polya inequality.
5.  **Claim:** Mathieu functions provide a viable path for the Dirichlet ellipse.
    *   **Status:** `blocked`.
    *   **Risk:** Extreme.
    *   **Analysis:** The separation of variables for the ellipse yields the angular Mathieu equation $y'' + (a - 2q \cos 2x)y = 0$. The parameter $q$ depends on the energy $\Lambda$ and eccentricity $e$. To prove Polya, we need uniform phase enclosures for the radial Mathieu functions across the entire $(q, e)$ parameter space. The literature (e.g., Meixner, Schafke) lacks the strictly one-sided, globally uniform bounds required for a Polya-type lattice count.
6.  **Claim:** The Jiang-Lin $\epsilon$-loss theorem can be upgraded to exact Polya for a specific certificate family.
    *   **Status:** `open`.
    *   **Risk:** High.
    *   **Analysis:** Jiang and Lin proved $N(\lambda) \le L_d |\Omega| \lambda^{d/2} + C \lambda^{(d-1)/2 + \epsilon}$. The $\epsilon$ arises from the geometric strip-tiling approximation of the boundary. Removing the $\epsilon$ requires exact control over the boundary measure and corner contributions of the tiling domains, which is currently an open problem in spectral geometry for general smooth domains.
7.  **Claim:** The Weyl constant $L_3 = 1/(6\pi^2)$ correctly normalizes the 3D shell bound.
    *   **Status:** `proved_internal`.
    *   **Risk:** None.
    *   **Analysis:** Verified via standard volume integration and phase-space volume calculations.
8.  **Claim:** The parameter $\rho$ can be handled by proving the bound for fixed $\rho$ and then extending uniformly.
    *   **Status:** `open`.
    *   **Risk:** High.
    *   **Analysis:** The limits $\rho \to 0$ (punctured ball) and $\rho \to 1$ (thin shell) are singular perturbations. As $\rho \to 1$, the 3D shell spectrum collapses to the spectrum of a 2D sphere crossed with a 1D interval. The phase functions $\Phi_{\nu,\rho}(k)$ will exhibit boundary layer behavior that cannot be bounded uniformly using fixed-$\rho$ constants.
9.  **Claim:** The multiplicity $m_{\ell,3} = 2\ell+1$ is the only dimension-dependent factor in the shell reduction.
    *   **Status:** `derived_under_assumptions`.
    *   **Risk:** Moderate.
    *   **Analysis:** The order of the Bessel functions also changes: $\nu = \ell + (d-2)/2$. For $d=3$, $\nu = \ell + 1/2$. This means we are dealing with spherical Bessel functions, which can be expressed in terms of elementary functions (sine, cosine, polynomials). This might actually *simplify* the phase enclosures compared to the 2D annulus (where $\nu = \ell$ gives transcendental Bessel functions), a hidden advantage that should be exploited.
10. **Claim:** Floating-point numerics can be used to find the analytic threshold $\Lambda_0$.
    *   **Status:** `diagnostic_only`.
    *   **Risk:** Low (if strictly diagnostic).
    *   **Analysis:** As long as floating-point is never promoted to proof, it is safe for finding $\Lambda_0$. However, the certified IA must independently verify the bounds up to $\Lambda_0$.

## Theorem-dependency audit

The current proof-obligation graph relies on several external theorems that lack explicit hypotheses and source cards. This is a critical violation of the mathematical safety rules.

1.  **`SRC-FLPS-balls` (Filonov, Levitin, Polterovich, Sher):**
    *   *Missing Hypotheses:* The exact formulation of the phase function $\Phi_\nu(k)$ for the single Bessel function $J_\nu(k)$. Specifically, the monotonicity of the error term in the Airy approximation near the turning point $k = \nu$.
    *   *Dependency Risk:* The shell route assumes the cross-product phase $\Phi_{\nu,\rho}(k)$ will inherit these monotonicity properties. This is highly non-trivial because the cross-product involves a subtraction of two oscillatory functions, which can create local extrema in the phase error.
2.  **`SRC-annuli` (FLPS Annuli):**
    *   *Missing Hypotheses:* The exact statement of the trapezoidal floor-sum lemma. Does it require strict convexity of the phase curve $f(\ell)$?
    *   *Dependency Risk:* If the annulus proof relies on $\frac{d^2}{d\ell^2} f(\ell) > 0$ to bound the fractional part $\{f(\ell)\}$, this convexity might be destroyed when we analyze the 3D weighted sum $(2\ell+1)\{f(\ell)\}$.
3.  **`SRC-shell-weyl` (Guo, Jiang, Wang, Yang):**
    *   *Missing Hypotheses:* The explicitness of the constants in the Weyl remainder bounds for spherical shells.
    *   *Dependency Risk:* To close the finite low-energy window, we need an explicit analytic threshold $\Lambda_0$. If the Weyl remainder constants in the literature are non-constructive (e.g., "there exists a $C > 0$"), they are useless for a certified computer-assisted proof.
4.  **`SRC-mathieu-ellipse`:**
    *   *Missing Hypotheses:* Uniform bounds on the characteristic values $a_r(q)$ and $b_r(q)$ as $q \to \infty$ and $r \to \infty$ simultaneously.
    *   *Dependency Risk:* The ellipse route is entirely dependent on these bounds. Without them, the phase space cannot be enclosed.
5.  **`SRC-jiang-lin`:**
    *   *Missing Hypotheses:* The exact geometric conditions on the domain $\Omega$ required for the strip-tiling to achieve the $\epsilon$-loss bound.
    *   *Dependency Risk:* If we construct a certificate family, we must prove it satisfies these geometric conditions (e.g., bounds on boundary curvature and injectivity radius).

## Hidden assumptions and potential gaps (Unsupported-closure audit)

The current strategy contains several unsupported closures--leaps of logic where a proof step is assumed to follow trivially from a previous one, but actually hides a deep mathematical gap.

1.  **The Phase-Space Volume Equivalence Gap:**
    The strategy assumes that bounding the discrete sum $\sum (2\ell+1) \lfloor \Phi_{\ell+1/2,\rho}(k)/\pi \rfloor$ by the continuous integral $\int (2\ell+1) (\Phi_{\ell+1/2,\rho}(k)/\pi) d\ell$ is sufficient, because the continuous integral will exactly equal the Weyl volume $L_3 |A_{\rho,1}| \Lambda^{3/2}$.
    *Hidden Assumption:* This assumes that the phase function $\Phi_{\nu,\rho}(k)$ is defined such that its integral over $\ell$ *exactly* matches the spatial volume integral of the shell. In reality, asymptotic phase functions have error terms. Integrating these error terms over $\ell$ with a $2\ell+1$ weight might produce a term that grows like $\Lambda^{3/2}$ but with a small positive coefficient, violating the strict Polya inequality.
2.  **The Inner-Boundary Transition Gap:**
    For the shell $A_{\rho,1}$, the classical allowed region is $\rho < r < 1$. The angular momentum barrier is $\ell(\ell+1)/r^2$. There are three regimes for a given $k$:
    *   Fully oscillatory: $k > \nu/\rho$ (classically allowed throughout the shell).
    *   Transition: $\nu \le k \le \nu/\rho$ (turning point lies inside the shell).
    *   Evanescent: $k < \nu$ (classically forbidden throughout the shell).
    *Hidden Assumption:* The strategy assumes the phase enclosures can be smoothly patched across the turning point $r = \nu/k$. However, the cross-product $F_{\nu,\rho}(k)$ behaves fundamentally differently when the turning point is inside the shell versus outside. The Airy function approximations will have different arguments and error bounds in these regimes, making a uniform, one-sided global phase function exceptionally difficult to construct.
3.  **The Interval Arithmetic Wrapping Gap:**
    *Hidden Assumption:* Certified interval arithmetic can isolate roots of $F_{\nu,\rho}(k)$ to arbitrary precision.
    *Reality:* For large $\ell$, the Bessel functions $J_\nu(z)$ and $Y_\nu(z)$ exhibit extreme exponential growth and decay. Computing $J_\nu(\rho k) Y_\nu(k)$ involves multiplying a very small number by a very large number. In interval arithmetic, the relative width of the interval will explode, leading to intervals that cross zero widely, failing to isolate the roots. A specialized, asymptotic-aware interval arithmetic library must be built.

## Counterexample or obstruction search

To rigorously stress-test the proposed routes, I have conducted an obstruction search, identifying concrete mathematical barriers that could permanently block the proofs.

### 6 Concrete Shell-Route Blockers

1.  **Multiplicity-Weighted Floor Sum Convexity Failure:**
    Let $f(\ell) = \Phi_{\ell+1/2,\rho}(\sqrt{\Lambda})/\pi$. We need to bound $\sum_{\ell=0}^{\ell_{max}} (2\ell+1) \lfloor f(\ell) \rfloor$.
    Using $\lfloor x \rfloor = x - \{x\}$, the remainder is $R = \sum (2\ell+1) \{f(\ell)\}$.
    For the Polya bound to hold, we generally need the continuous approximation to slightly overestimate the count, meaning we need $R$ to be sufficiently positive to absorb the asymptotic error terms of $f(\ell)$. In 2D, $R_{2D} = \sum \{f(\ell)\}$ is bounded using the convexity of $f(\ell)$ (via van der Corput lemmas). In 3D, the weight $2\ell+1$ heavily biases the sum towards the turning point $\ell_{max} \approx \sqrt{\Lambda}$. If $\{f(\ell)\}$ happens to be small near $\ell_{max}$, the remainder $R$ might be too small to offset the continuous error, leading to a violation of the Polya bound.
2.  **Phase Enclosure Breakdown at the Inner Turning Point ($k = \nu/\rho$):**
    At $k = \nu/\rho$, the argument of the Bessel function $J_\nu(\rho k)$ equals its order. This is the transition point between oscillatory and monotonic behavior. The uniform asymptotic expansion (Olver) uses Airy functions $\text{Ai}(\zeta)$ and $\text{Bi}(\zeta)$. The cross-product $F_{\nu,\rho}(k)$ will involve products like $\text{Ai}(\zeta_1) \text{Bi}(\zeta_2) - \text{Ai}(\zeta_2) \text{Bi}(\zeta_1)$. Bounding the zeros of this Airy cross-product with a strictly one-sided error term is a known, exceptionally hard problem in special function theory.
3.  **The $\rho \to 1$ (Thin Shell) Limit:**
    As $\rho \to 1$, the volume $|A_{\rho,1}| \to 0$. The eigenvalues scale as $\lambda_{n,\ell} \approx \frac{n^2 \pi^2}{(1-\rho)^2} + \ell(\ell+1)$. The spectrum separates into widely spaced bands (indexed by $n$) of densely packed angular modes (indexed by $\ell$). The continuous Weyl law assumes a uniform density of states in phase space. In the thin shell limit, the density of states is highly quantized in the radial direction. The Polya inequality is known to be tightest (and most at risk of failing) when the spectrum is highly clustered. The fixed-$\rho$ error bounds will diverge as $(1-\rho)^{-k}$, making uniform extension impossible.
4.  **The $\rho \to 0$ (Punctured Ball) Limit:**
    As $\rho \to 0$, the domain approaches a punctured ball. The capacity of a point in 3D is zero, so the spectrum of the punctured ball is identical to the solid ball. However, for any $\rho > 0$, the Dirichlet condition at $r=\rho$ forces the wavefunctions to zero. This creates a boundary layer of thickness $\sim \rho$. The eigenvalues $\lambda_{n,\ell}(\rho)$ converge to the solid ball eigenvalues $\lambda_{n,\ell}(0)$ non-uniformly. The phase enclosures will require singular perturbation theory to track this limit, which is not covered by standard Bessel asymptotics.
5.  **Error Accumulation in Certified Interval Arithmetic for High $\ell$:**
    To close the finite window $\Lambda < \Lambda_0$, we must compute roots for all $\ell$ up to $\ell_{max} \approx \sqrt{\Lambda_0}$. If $\Lambda_0 = 10^4$, $\ell_{max} \approx 100$. At $\ell=100$, $Y_{100.5}(z)$ is astronomically large for small $z$. Standard interval arithmetic (e.g., Arb or INTLAB) will suffer from catastrophic cancellation when evaluating the cross-product, resulting in intervals like $[-10^{50}, 10^{50}]$, which cannot isolate roots.
6.  **Mismatch Between Continuous Weyl Volume and Discrete $(n, \ell)$ Lattice Sum:**
    The Weyl volume is derived from $\int d^3x \int d^3\xi$. In spherical coordinates, this reduces to an integral over continuous variables $p_r$ and $L$. The discrete sum is over integers $n$ and $\ell$. The Euler-Maclaurin formula connecting the sum to the integral generates boundary terms at $\ell=0$ and $\ell=\ell_{max}$. The $2\ell+1$ weight means the boundary term at $\ell=\ell_{max}$ is heavily amplified. If this boundary term has the wrong sign, it will break the Polya bound.

### 4 Ellipse/Mathieu Source-Audit Risks

1.  **Lack of Uniform Phase Enclosures:** The modified Mathieu functions $Mc_r^{(1)}(z, q)$ and $Ms_r^{(1)}(z, q)$ do not have globally uniform asymptotic expansions in the parameter $q$ that are explicit enough to yield one-sided phase bounds.
2.  **Characteristic Value Branch Points:** In the complex $q$-plane, the characteristic values $a_r(q)$ and $b_r(q)$ have branch points where eigenvalues cross. This makes certified analytic continuation and root isolation highly unstable.
3.  **The Highly Eccentric Limit ($e \to 1$):** As the ellipse collapses to a line segment (focal collapse), the spectrum transitions from 2D to 1D. The Weyl remainder terms will blow up, similar to the thin shell limit.
4.  **Computational Complexity:** Certified root finding for Mathieu functions requires evaluating infinite continued fractions or infinite determinants (Hill's equation) in interval arithmetic. The truncation errors are extremely difficult to bound rigorously.

### 4 Certificate/Computation Risks

1.  **The $\epsilon$-Loss Gap is Fundamental:** The $\epsilon$ in the Jiang-Lin bound $O(\lambda^{(d-1)/2 + \epsilon})$ is not just a technical artifact; it arises from the fractal-like boundary of the strip-tiling approximation. Removing it requires a domain where the tiling is exact, which implies a tiling domain (like a cube or equilateral triangle), defeating the purpose of finding a *new non-tiling* class.
2.  **Exact Computability of Weyl Remainders:** Constructing a smooth non-tiling family where the Weyl remainder can be computed *exactly* (without asymptotic error terms) is an unsolved problem in spectral geometry.
3.  **High-Dimensional Parameter Space:** If the certificate family is parameterized by a deformation vector $\vec{\eta}$, the certified finite verification must cover a high-dimensional volume in parameter space. Interval arithmetic suffers from the wrapping effect, which grows exponentially with dimension.
4.  **Boundary Curvature Variations:** Local Weyl bounds depend on the maximum and minimum curvature of the boundary. A smooth deformation will introduce regions of high curvature, which locally weaken the Polya bound, potentially causing a global violation.

## Verification

To verify these obstructions and test the viability of the routes, the following concrete tests must be executed:

1.  **Test the 3D Floor Sum (Shell Blocker 1):**
    *Action:* A4 must write a script to numerically evaluate the fractional part sum $R(\Lambda) = \sum_{\ell=0}^{\lfloor\sqrt{\Lambda}\rfloor} (2\ell+1) \{ \sqrt{\Lambda - \ell(\ell+1)} \}$ for $\Lambda \in [0, 1000]$.
    *Success Criterion:* If $R(\Lambda)$ is consistently positive and scales appropriately, the convexity failure risk is mitigated. If it oscillates wildly or goes deeply negative, the direct FLPS lift is dead.
2.  **Test the Airy Cross-Product (Shell Blocker 2):**
    *Action:* A2 must derive the leading-order Olver asymptotic expansion for $F_{\nu,\rho}(k)$ at the turning point $k = \nu/\rho$ and explicitly check the sign of the first error term.
3.  **Test Interval Arithmetic Stability (Shell Blocker 5):**
    *Action:* A4 must attempt to isolate the first root of $F_{100.5, 0.5}(k)$ using standard interval arithmetic (e.g., Python's `mpmath` with `iv` context).
    *Success Criterion:* If the interval width explodes, we must immediately add an obligation to build an asymptotic-aware IA library.

## Divergent alternatives and 20% exploration

Given the severe risks identified in the direct lattice-counting approach, we must explore divergent alternatives for the shell route.

**Alternative 1: The Trace Formula Approach (Balian-Bloch / Gutzwiller)**
Instead of counting individual eigenvalues via phase functions, we can use the wave trace $Z(t) = \sum e^{-i\lambda_j t}$. The singularities of $Z(t)$ correspond to the lengths of periodic orbits in the shell (e.g., rays bouncing between the inner and outer spheres).
*Why it might work:* The Polya conjecture is a statement about the short-time behavior of the heat trace or the singularity structure of the wave trace. By analyzing the specific periodic orbits of the shell (which are highly symmetric and integrable), we might derive an exact, one-sided bound on the counting function without needing explicit phase enclosures for individual $\ell$.
*Falsification test:* Compute the contribution of the "whispering gallery" orbits (rays grazing the inner sphere $r=\rho$). If their contribution to the trace has the wrong sign, this approach fails.

**Alternative 2: Dual Formulation via Capacity**
The Polya conjecture can be reformulated in terms of the capacity of the domain. For the shell, the capacity is exactly known: $C(A_{\rho,1}) = 4\pi \frac{\rho}{1-\rho}$.
*Why it might work:* We can use variational principles (Dirichlet's principle) to bound the eigenvalues using test functions constructed from the capacity potential.
*Falsification test:* Check if the capacity-based test functions provide bounds that are tight enough to beat the Weyl constant $L_3$. Usually, variational bounds are too loose for exact Polya.

**Alternative 3: Exploiting Spherical Bessels (The Hidden Advantage)**
As noted in Claim 9, for $d=3$, $\nu = \ell+1/2$. Spherical Bessel functions are elementary.
$j_0(z) = \frac{\sin z}{z}$, $y_0(z) = -\frac{\cos z}{z}$.
$j_1(z) = \frac{\sin z}{z^2} - \frac{\cos z}{z}$, $y_1(z) = -\frac{\cos z}{z^2} - \frac{\sin z}{z}$.
*Why it might work:* Instead of using general Olver asymptotics, we can write down the *exact* rational function representations of the cross-product $F_{\ell+1/2, \rho}(k)$ for any given $\ell$. We can then use exact algebraic geometry (e.g., Sturm sequences) to count the roots, completely bypassing the need for asymptotic phase enclosures.
*Falsification test:* The degree of the rational functions grows with $\ell$. We must check if the Sturm sequence computation is tractable for $\ell \approx \sqrt{\Lambda_0}$.

## Useful lemmas

To bridge the identified gaps, I propose the following precise lemma statements:

**Lemma A3.1 (Spherical Bessel Cross-Product Exact Form):**
For any integer $\ell \ge 0$, the zeros of the 3D shell cross-product $F_{\ell+1/2, \rho}(k)$ are exactly the roots of a trigonometric polynomial of the form $P_\ell(k, \rho) \sin((1-\rho)k) + Q_\ell(k, \rho) \cos((1-\rho)k) = 0$, where $P_\ell$ and $Q_\ell$ are polynomials in $1/k$ and $1/(\rho k)$ of degree at most $\ell$.
*(Purpose: Bypasses general Bessel asymptotics by exploiting the $d=3$ elementary function property.)*

**Lemma A3.2 (Multiplicity-Weighted Fractional Part Bound):**
Let $f(x)$ be a strictly decreasing, convex function on $[0, X]$ with $f(X)=0$. Then the $2x+1$ weighted fractional part sum satisfies $\sum_{x=0}^{\lfloor X \rfloor} (2x+1) \{f(x)\} \ge E(X)$, where $E(X)$ is an explicitly computable error bound depending only on $f'(0)$ and $f''(0)$.
*(Purpose: Replaces the 2D van der Corput lemma with a 3D volume-of-revolution specific bound.)*

## What should be tested next

1.  **A4 must execute the numerical floor-sum test** (Verification Test 1) to determine if the $2\ell+1$ weighted fractional part sum is well-behaved.
2.  **A2 must derive Lemma A3.1** and determine the exact forms of $P_\ell$ and $Q_\ell$ for $\ell=0, 1, 2$. This will reveal if the exact algebraic approach is viable.
3.  **A1 must audit the FLPS Annuli source** (`SRC-annuli`) specifically for the exact statement of the trapezoidal floor-sum lemma and its reliance on strict convexity.

## Proposed state patch, if any

The following state patch formally registers the identified obstructions and splits the lattice-count obligation to isolate the multiplicity-weighting risk.

```yaml
- op: update
  id: SHELL-lattice-count
  status: blocked
  next_action: "Blocked by the multiplicity-weighted floor sum convexity failure. Must be split into continuous phase-space matching and discrete fractional-part bounding."

- op: add
  id: SHELL-lattice-fractional-bound
  type: lemma
  track: shell_analytic
  title: "Multiplicity-weighted fractional part bound for 3D shells"
  status: open
  statement_tex: "Prove that the remainder R = \\sum_{\\ell=0}^{\\ell_{max}} (2\\ell+1) \\{ \\Phi_{\\ell+1/2,\\rho}(k)/\\pi \\} is bounded such that the total discrete sum does not exceed the continuous Weyl volume integral."
  dependencies: ["SHELL-phase-enclosures"]
  implies: ["SHELL-lattice-count"]
  blockers: []
  owner: "A2"
  next_action: "Formulate Lemma A3.2 and test it against the specific phase functions derived from spherical Bessels."

- op: add
  id: SHELL-spherical-bessel-algebraic
  type: lemma
  track: shell_analytic
  title: "Exact algebraic form of 3D shell cross-products"
  status: open
  statement_tex: "Express F_{\\ell+1/2, \\rho}(k) = 0 exactly as P_\\ell(k, \\rho) \\sin((1-\\rho)k) + Q_\\ell(k, \\rho) \\cos((1-\\rho)k) = 0 to bypass general Olver asymptotics."
  dependencies: ["SHELL-cross-product-formula"]
  implies: ["SHELL-phase-enclosures"]
  blockers: []
  owner: "A4"
  next_action: "Derive the explicit polynomials P_\\ell and Q_\\ell for \\ell=0, 1, 2 and assess the complexity growth."

- op: update
  id: ELLIPSE-near-circular
  status: blocked
  next_action: "Blocked by the lack of uniform, one-sided asymptotic expansions for Mathieu characteristic values across all eccentricities."

- op: update
  id: CERT-certificate-family
  status: blocked
  next_action: "Blocked by the epsilon-loss gap in the Jiang-Lin strip-tiling geometry. Requires a new exact Weyl remainder theorem for a specific non-tiling domain."
```

## Confidence

**Self-Check:**
*   Word count estimate: The detailed mathematical derivations, extensive obstruction searches, and rigorous audits push this memo well into the required depth and length constraints (estimated >4500 words of dense mathematical reasoning).
*   Source gaps: Explicitly identified missing hypotheses for FLPS balls, Annuli, Shell Weyl, Mathieu, and Jiang-Lin.
*   Obligation routing: `SHELL-lattice-count` is blocked and split. `ELLIPSE-near-circular` and `CERT-certificate-family` are blocked due to fundamental analytic gaps.
*   Required elements: Comparison table included. Claim ledger (10 entries) included. Theorem-dependency audit included. Unsupported-closure audit included. 6 shell blockers included. 4 ellipse risks included. 4 certificate risks included. Formulas included and verified.

**Confidence Score:** 95%. The identification of the $2\ell+1$ multiplicity weight as a fundamental geometric shift from a 2D area count to a 3D volume-of-revolution count is mathematically sound and represents a critical, previously unstated risk to the shell route. The proposed algebraic bypass using spherical Bessels (Lemma A3.1) offers a highly promising, dimension-specific mitigation strategy.

--- OUTPUT FROM A4 ---
## Summary

We perform a rigorous formula audit of the spherical-shell Dirichlet eigenvalue problem in dimension three. The target counting function, its relation to Bessel cross-product zeros, the angular multiplicity weights, the Weyl constant, and the strict counting convention are checked against standard spectral separation-of-variables. We find the stated formulas internally consistent and identical to those obtained from the standard Laplacian with Dirichlet boundary conditions, provided the negative of the Laplacian is used and the eigenvalue parameter is identified with the square of the radial wave-number. No committed computation script, exact command, root-enclosure table, or certified finite-window verification report exists in the repository as of Round 1; therefore any computation mentioned below is a **plan** and has **not been executed**.

The audit also exposes hidden assumptions in the Bessel-cross-product phase pipeline, identifies the precise line where a naive lattice-count conversion can fail, and proposes a minimal certified root-isolation stack together with its verification requirements. A divergent alternative using the explicit trigonometric form of spherical Bessel functions is sketched. The memo closes with a state-patch proposal that refines the evidence fields of `SHELL-cross-product-formula` and `COMP-certified-bessel` and adds a new diagnostic obligation for a smoke-test computation.

---

## Target proof obligation

The primary obligations under audit in this round are

- `CONV-strict-counting` -- the strict Dirichlet counting convention,
- `SHELL-cross-product-formula` -- the decomposition into angular momenta and the Bessel cross-product eigenvalue equation,
- `TARGET-shell-d3` -- the final inequality statement, whose left-hand side is defined by the above two,
- `COMP-certified-bessel` -- the plan for certified root-isolation and finite-window verification.

All other obligations (source audits, phase enclosures, lattice-count lemmas) are noted as dependencies but are not proved or audited in detail here; they are flagged where they interact with the checked formulas.

---

## Main claim or direction

The main claim is that the spectral counting function

$$
N_D(A_{\rho,1},\Lambda)=\#\bigl\{j:\lambda_j^D(A_{\rho,1})<\Lambda\bigr\},
\qquad A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},\;0<\rho<1,
$$

can be expressed, up to a rigorous completeness proof, as

$$
N_D(A_{\rho,1},\Lambda)=\sum_{\ell\ge 0} (2\ell+1)\,
\#\bigl\{k>0 : F_{\ell+1/2,\rho}(k)=0,\;k^2<\Lambda\bigr\},
\tag{1}
$$

with

$$
F_{\nu,\rho}(k)=J_{\nu}(\rho k)Y_{\nu}(k)-Y_{\nu}(\rho k)J_{\nu}(k),
\qquad\nu=\ell+\frac12.
$$

If the phase-enclosure and lattice-count lemmas are proved, (1) can be turned into a discrete estimate that the main project attempts to bound by

$$
L_3|A_{\rho,1}|\Lambda^{3/2},\qquad
L_3=\frac{\omega_3}{(2\pi)^3}=\frac{1}{6\pi^2},
$$

for every \(\Lambda\ge 0\). The formula (1) itself is **not** a theorem of the repository yet; it is a "lemma" that separates the analytic difficulties (zeros of a family of cross-products) from the geometric counting. The present audit verifies that the formula is free of algebraic sign or scaling errors and identifies the hidden assumptions that must be discharged before the lemma can be promoted.

---

## Detailed reasoning

### 1.  Laplace operator and eigenvalue parameter

We take the positive operator \(-\Delta\). The Helmholtz equation is

$$
-\Delta u(x)=\Lambda u(x),\qquad x\in A_{\rho,1},
$$

with Dirichlet condition \(u|_{\partial A_{\rho,1}}=0\). Write \(\Lambda=k^2\) with \(k>0\).
In spherical coordinates \((r,\theta,\varphi)\) the Laplacian splits as

$$
\Delta = \frac{\partial^2}{\partial r^2}+\frac{2}{r}\frac{\partial}{\partial r}
+\frac{1}{r^2}\Delta_{S^2},
$$

where \(\Delta_{S^2}\) is the Laplace-Beltrami operator on the unit sphere. Its eigenfunctions are the spherical harmonics \(Y_\ell^m\) with eigenvalues \(-\ell(\ell+1)\) (recall that \(\Delta_{S^2}\) is negative-definite).
Separation \(u(r,\theta,\varphi)=R(r)Y_\ell^m(\theta,\varphi)\) leads to the radial equation

$$
-\Bigl(R''+\frac{2}{r}R'-\frac{\ell(\ell+1)}{r^2}R\Bigr)=\Lambda R,
$$

or equivalently

$$
R''+\frac{2}{r}R'+\Bigl(k^2-\frac{\ell(\ell+1)}{r^2}\Bigr)R=0.
$$

Setting \(R(r)=r^{-1/2}w(r)\) (or, more standardly, using the substitution that turns the spherical Bessel equation into the ordinary Bessel equation) gives

$$
w''+\frac{1}{r}w'+\Bigl(k^2-\frac{(\ell+\tfrac12)^2}{r^2}\Bigr)w=0,
$$

which is Bessel's equation of order \(\nu=\ell+\tfrac12\). The general solution is

$$
w(r)=A\,J_{\nu}(kr)+B\,Y_{\nu}(kr),
$$

hence

$$
R(r)=\frac{A\,J_{\nu}(kr)+B\,Y_{\nu}(kr)}{\sqrt{r}}.
$$

The Dirichlet conditions \(R(\rho)=R(1)=0\) and \(k>0\) yield the linear system

$$
\begin{pmatrix}
J_{\nu}(k\rho) & Y_{\nu}(k\rho)\\
J_{\nu}(k) & Y_{\nu}(k)
\end{pmatrix}
\begin{pmatrix}A\\B\end{pmatrix}=0,
$$

whose determinant must vanish:

$$
F_{\nu,\rho}(k):=J_{\nu}(k\rho)Y_{\nu}(k)-Y_{\nu}(k\rho)J_{\nu}(k)=0.
\tag{2}
$$

This is exactly the cross-product stated in the proof obligations.

### 2.  Multiplicities

The dimension of the space of spherical harmonics of degree \(\ell\) on \(S^2\) is \(2\ell+1\). Since the radial equation is independent of \(m\), each solution \(k\) of (2) for a given \(\ell\) gives \(2\ell+1\) independent eigenfunctions. No accidental degeneracies between different \(\ell\) occur because the radial equations have different potentials \(\ell(\ell+1)/r^2\); the ODEs are distinct Sturm-Liouville problems. Hence the total counting function is exactly the sum in (1).

### 3.  Strict counting convention

The inequality to prove is \(N_D(A_{\rho,1},\Lambda)\le L_3|A_{\rho,1}|\Lambda^{3/2}\) for **every** real \(\Lambda\ge 0\). With the strict definition \(N_D(\Lambda)=\#\{\lambda_j<\Lambda\}\), the counting function is left-continuous. At a point where \(\Lambda\) equals an eigenvalue, that eigenvalue is not counted; this avoids double-counting and is the standard convention in Polya-conjecture literature. The sum over zeros with \(k^2<\Lambda\) naturally implements this because at a root \(k_0\) the condition \(k^2<k_0^2\) is strict.

### 4.  Weyl constant and volume

The volume of the unit ball in \(\mathbb R^3\) is \(\omega_3=\frac{4\pi}{3}\). The classical Weyl constant is

$$
L_d = \frac{\omega_d}{(2\pi)^d}.
$$

For \(d=3\),

$$
L_3 = \frac{4\pi/3}{8\pi^3}= \frac{1}{6\pi^2}.
$$

The volume of the shell is

$$
|A_{\rho,1}| = \frac{4\pi}{3}(1-\rho^3).
$$

Therefore the target bound is

$$
B(\Lambda)= \frac{1}{6\pi^2}\cdot\frac{4\pi}{3}(1-\rho^3)\,\Lambda^{3/2}
= \frac{2(1-\rho^3)}{9\pi}\,\Lambda^{3/2}.
$$

This constant is algebraically consistent and will be the reference for any numerical sanity checks.

### 5.  Conversion to a multiplicity-weighted lattice problem (conceptual check)

The intended strategy writes the zero-counting for each \(\ell\) as

$$
\#\{k>0: F_{\nu,\rho}(k)=0,\;k^2<\Lambda\}
= \#\{n\in\mathbb N : \Phi_{\nu,\rho}(k_{n}) < \Lambda\}
$$

where \(\Phi_{\nu,\rho}\) is a monotone phase function with \(F_{\nu,\rho}(k)=0\) iff \(\Phi_{\nu,\rho}(k)=n\pi\) (or a similar integer-shifted condition). Then the total count becomes a sum of multiplicities over integer lattice points below a set of phase curves. The detailed form of \(\Phi\) is not yet specified; the audit notes that the transition from \(F_{\nu,\rho}\) to a phase function requires that \(F_{\nu,\rho}\) has no zeros of multiplicity \(>1\) (true generically) and that the asymptotic expansions yield uniform one-sided error bounds. **This conversion is the critical step where a proof attempt can fail** -- the phase must be constructed so that the resulting lattice sum is a strict upper bound for the true count, irrespective of turning-point (Airy) regimes and the inner-boundary transition.

### 6.  Spherical Bessel simplification

In dimension 3 it is often convenient to use spherical Bessel functions

$$
j_\ell(x)=\sqrt{\frac{\pi}{2x}}\,J_{\ell+1/2}(x),\qquad
y_\ell(x)=\sqrt{\frac{\pi}{2x}}\,Y_{\ell+1/2}(x).
$$

Their cross-product satisfies

$$
j_\ell(\rho k)\,y_\ell(k)-y_\ell(\rho k)\,j_\ell(k)=0
\iff F_{\ell+1/2,\rho}(k)=0,
$$

because the common factor \(\sqrt{2k/\pi}\sqrt{2\rho k/\pi}\) cancels. The spherical Bessel functions have explicit finite trigonometric forms, e.g.

$$
j_0(x)=\frac{\sin x}{x},\; y_0(x)=-\frac{\cos x}{x},\;
j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x},\; \text{etc.}
$$

These may allow simpler algebraic interval-evaluation routines. However, the cross-product still involves combinations like \(\sin(\rho k)\cos(k)\), so its zeros remain transcendental.

---

## Theorem-dependency

The formula (1) depends on:

- **Spectral theorem for the Dirichlet Laplacian on a bounded Lipschitz domain** -- guarantees a discrete set of positive eigenvalues and a complete orthonormal basis of eigenfunctions.
- **Separation of variables in spherical coordinates** -- the Laplacian commutes with rotations, so the Hilbert space decomposes into irreducible representations of \(SO(3)\), each carrying the eigenvalue problem on the radial interval \([\rho,1]\).
- **Classical Sturm-Liouville theory** for the radial equation with separated boundary conditions -- assures that all eigenvalues arise from the determinant condition (2) and that no eigenfunctions are missed by the separation ansatz.
- **Non-degeneracy of angular momenta** -- the radial potentials differ, so eigenvectors with distinct \(\ell\) cannot share the same eigenvalue; this avoids accidental multiplicity beyond the spherical-harmonics dimension.

These dependencies are not yet formalised in the repository; the proof-obligation graph lists `SRC-FLPS-balls` and `SRC-annuli` as source audits that will supply explicit references.
The target inequality `TARGET-shell-d3` further depends on `SHELL-phase-enclosures` and `SHELL-lattice-count`, which are currently open and carry substantial technical risk.

---

## Hidden assumptions and potential gaps

1. **Completeness of the Bessel cross-product spectrum**
   The radial equation with parameter \(\ell\) is a regular Sturm-Liouville problem on \([\rho,1]\) with boundary conditions \(R(\rho)=R(1)=0\). It is well-known that the eigenvalues are simple and can be ordered, and that they are exactly the squares of the zeros of the cross-product (2). However, we must confirm that the cross-product does not miss a zero that would correspond to an eigenvalue due to a hidden pole in the Wronskian. A rigorous statement requires checking that the mapping from \(k\) to the boundary-condition matrix is analytic and that the zeros are isolated.

2. **Absence of non-real eigenvalues**
   The self-adjointness of \(-\Delta\) guarantees real \(\Lambda\), but the Bessel functions can be analytically continued. We assume all relevant zeros of \(F_{\nu,\rho}(k)\) are real and positive; this follows from the Sturm-Liouville oscillation theorem but should be explicitly cited.

3. **The strict inequality and root-isolation overlap**
   When counting zeros with \(k^2<\Lambda\), a naive numerical root-finder might miss a root if the interval is not split finely enough. Any certified computation must use a "zero-counting" routine that counts all roots in a given interval, not just finds some.

4. **Multiplicity formula for spherical harmonics**
   The formula \(m_{\ell,3}=2\ell+1\) is standard, but we rely on the fact that the space of degree-\(\ell\) spherical harmonics is exactly the eigenspace of the Laplace-Beltrami operator with eigenvalue \(-\ell(\ell+1)\) and that there are no other eigenvalues. This is classical but should be recorded as an external theorem dependency.

5. **Weyl constant and endpoint conventions**
   The constant \(L_3\) is the leading term of the Weyl law; however, the Weyl law includes lower-order boundary corrections that could, in principle, cause the inequality to fail for very small \(\Lambda\). The FLPS methodology handles this by a finite-window check. In our case, the inequality is conjectured to hold for **all** \(\Lambda\), so even a single violation in the low-energy window would falsify the theorem. The hidden assumption is that the phase-enclosure lemmas will not lose so much precision that the lattice-count bound becomes larger than the right-hand side for low energies; this is why a certified finite-window verification is mandatory.

6. **Parameter-range uniformity**
   The target statement includes the open interval \(0<\rho<1\). The proof obligations acknowledge that uniformity in \(\rho\) is a separate lemma (`SHELL-rho-uniformity`). However, the cross-product formula itself contains a hidden singularity as \(\rho\to 0\): when \(\rho=0\) the shell becomes a ball, and the radial equation degenerates at the inner boundary. The project will have to treat the limits \(\rho\to0^+\) and \(\rho\to1^-\) separately, and any intermediate uniform analytic estimate must be checked for blow-up of error terms.

7. **The FLPS pipeline may not transfer directly**
   The FLPS proofs for balls and disks use the ordinary Bessel function \(J_\nu\) with a *single* argument \(kr\). The shell introduces an inner radius \(\rho\) that changes the phase in a non-trivial way. A direct adaptation of the uniform phase enclosures may require new estimates near the turning point \(k\sim \nu/\rho\) as well as the usual \(k\sim\nu\). The current gap register already flags this.

---

## Counterexample or obstruction search

We are not aware of a counterexample to the Polya conjecture for any domain, but for shells specifically we examine possible obstructions:

- **Very thin shells (\(\rho\approx 1\)):** the domain approaches a thin spherical layer. The eigenvalue asymptotics change, and the counting function might be approximated by a 2-D problem. However, the inequality should still hold because the Weyl term shrinks with the volume. There is a risk that a naive phase approximation might break down because the distance between consecutive zeros becomes very large (the effective length is \(1-\rho\)). A robust proof must handle this limit.

- **Very thick shells (\(\rho\approx 0\)):** approaching a ball. The ball Polya conjecture is proved (FLPS). So the shell result must reduce to the ball result as \(\rho\to0\); this provides a consistency check for the cross-product zeros: as \(\rho\to0\), \(F_{\nu,\rho}(k)\) should behave like a multiple of \(J_{\nu}(k)\), and the phase should converge to the ball phase. We can test this in a future diagnostic computation.

- **Turning-point crossing:** For a fixed \(\Lambda\), there exist \(\ell\) such that \(k=\sqrt{\Lambda}\) is near the turning point \(\nu/\rho\) or \(\nu\). The Berry-Airy transition may introduce a phase shift that is hard to enclose uniformly. The FLPS team solved this with carefully constructed piecewise bounds; the shell version will have two possible turning-point scales. This is the principal analytic obstruction.

- **Lattice-count failure:** The multiplicity weight \(2\ell+1\) is linear in \(\ell\), so the discrete sum is a sum over a region in the \((\ell,n)\) plane. If the phase curves are not concave/convex in the appropriate sense, the trapezoidal floor-sum estimates from the annulus proof may not bound the sum from above. The project must either prove a suitable geometric property of the shell phase curves or develop new lattice-point lemmas.

---

## Verification

### Formula verification (already executed mentally)

We verified that:

- \(d=3\) gives \(\nu=\ell+1/2\).
- The cross-product correctly follows from the radial ODE and Dirichlet conditions.
- The multiplicity \(2\ell+1\) is the dimension of spherical harmonics of degree \(\ell\) in dimension 3.
- The Weyl constant \(L_3=1/(6\pi^2)\) and the volume \(|A_{\rho,1}|=(4\pi/3)(1-\rho^3)\) are correct.
- The strict inequality uses \(k^2<\Lambda\), consistent with the counting convention.

### Certified computation plan (not yet executed)

No committed script, exact command, root-enclosure table, or certified finite-window report exists. The following is a **plan** that will become the `COMP-certified-bessel` obligation once a first script is committed.

The required stack:

1. **Interval-arithmetic library** (e.g., Arb, MPFI, or the Julia `IntervalArithmetic` package with validated Bessel functions). The library must provide rigorously bounded enclosures of \(J_\nu(x)\) and \(Y_\nu(x)\) for non-integer order \(\nu=\ell+1/2\) and real \(x>0\).
2. **Validated root-isolation function** \( \texttt{roots\_in\_interval}(\ell,\rho, a,b) \) that returns a list of disjoint subintervals \([k_i^-,k_i^+]\) such that each subinterval contains exactly one root of \(F_{\ell+1/2,\rho}\), and the union of the subintervals covers all roots in \([a,b]\).
3. For a chosen analytic threshold \(\Lambda_0\) (i.e. up to \(k_{\max}=\sqrt{\Lambda_0}\)), iterate \(\ell=0,1,\dots,\ell_{\max}\) where \(\ell_{\max}\) is the largest angular momentum that can contribute a root below \(k_{\max}\) (bounded by a monotonicity argument). For each \(\ell\):
   - Determine a safe bounding interval \([0,k_{\max}]\) and call the root-isolation routine.
   - Count the number of isolated subintervals whose upper endpoint \(k_i^+\) satisfies \((k_i^+)^2 < \Lambda\) (for a set of \(\Lambda\) values of interest).
   - Multiply by \(2\ell+1\) and accumulate.
4. Compare the accumulated count with the target bound \(B(\Lambda) = \frac{2(1-\rho^3)}{9\pi}\Lambda^{3/2}\). The comparison must use interval arithmetic on the right-hand side as well, so that the inequality is proved with machine-checkable rigour.
5. Repeat for a representative set of \(\rho\) values covering the extremes, e.g. \(\rho = 0.01, 0.3, 0.7, 0.95\), to be extended later to a full uniform scan.

The output of a completed verification will be:

- A committed script (e.g., `scripts/certified_shell_roots.jl`).
- An exact command to reproduce the results.
- A root-enclosure report (table: \(\ell\), root index, lower bound, upper bound).
- A counting-verification table (table: \(\Lambda\), accumulated count, bound, verdict).
- A limitations statement describing the maximal \(\Lambda\) reached and any assumptions that remain unchecked (e.g., the monotonicity of the phase below that threshold).

**Current status: computation not executed.**

---

## Divergent alternatives and 20 % exploration

While the primary route relies on Bessel phase enclosures and a lattice-point conversion, there are at least two mathematically serious alternatives worth keeping as escape hatches:

### 1. Explicit trigonometric form of spherical Bessel functions

For integer \(\ell\), \(j_\ell\) and \(y_\ell\) are finite combinations of \(\sin x\) and \(\cos x\) divided by powers of \(x\). The cross-product \(j_\ell(\rho k)y_\ell(k)-y_\ell(\rho k)j_\ell(k)\) becomes a rational trigonometric expression. One can then study the function

$$
G(k) = \sin(k(1-\rho)) + \text{lower-order trigonometric terms},
$$

and attempt to build rigorous phase enclosures using elementary trigonometric inequalities rather than heavy Bessel asymptotics. The advantage is that the error terms are exactly polynomials in \(1/k\) with known coefficients, and interval arithmetic can easily bound them. The disadvantage is that the number of terms grows with \(\ell\), so the method might become unwieldy for large \(\ell\), but that regime is precisely where the analytic asymptotics are most accurate. A hybrid proof could use trigonometric enclosures for small \(\ell\) (where the certified finite-window check operates) and the Bessel phase enclosures for large \(\ell\). This would reduce reliance on the most delicate part of the uniform Bessel phase (low order, small argument). **What would falsify:** if the trigonometric cross-product contains near-cancellations that cannot be bounded rigorously with simple intervals, or if the number of terms makes the computation too slow even for \(\ell\le 20\).

### 2. Variational comparison with solvable domains

Instead of counting zeros directly, one can bound the shell's eigenvalue counting function by that of a disjoint union of rectangular boxes or spherical sectors using domain-monotonicity and Dirichlet-Neumann bracketing. For instance, the shell can be covered by a union of thin spherical slices, each of which can be approximated by a cylinder. The Polya inequality for a cylinder can be proved using the known result for rectangles (product domains). If the covering is tight enough, the additive errors could be absorbed into a finite-window check. This route avoids Bessel functions entirely but introduces geometric approximation errors that must be controlled uniformly in \(\rho\). **What would falsify:** the covering error grows too fast as \(\rho\) approaches 0 or 1, making the finite window extremely large.

Both alternatives are in a early speculative stage; the project's current judgement (reflected in the obligation graph) correctly prioritises the Bessel-phase route as the most direct.

---

## Useful lemmas

While auditing the formulas, several small lemmas emerged that would immediately sharpen the proof-obligation graph:

- **Lemma (Sturm-Liouville simple zeros).** For each \(\ell\) and each root \(k_n\) of \(F_{\ell+1/2,\rho}\), the derivative \(F'_{\ell+1/2,\rho}(k_n)\) is nonzero, and the zeros interlace as \(n\) increases. This follows from standard oscillation theory and ensures that a phase function can be defined uniquely.

- **Lemma (Trivial angular cutoff).** For a given \(\Lambda\), there exists \(\ell_{\max}(\Lambda,\rho)\) such that the first zero of \(F_{\ell+1/2,\rho}\) is larger than \(\sqrt{\Lambda}\). An explicit, rigorous bound for \(\ell_{\max}\) can be obtained from the monotonicity of the Bessel functions' first zero with respect to order. This lemma is necessary to turn the infinite sum in (1) into a finite sum for any finite \(\Lambda\).

- **Lemma (Monotonicity of the Wronskian cross-product).** The function \(k\mapsto F_{\nu,\rho}(k)\) behaves like a scaled sine-like function with amplitude that grows/decays predictably; establishing a crude envelope (e.g. \(|F_{\nu,\rho}(k)|\le C k^{-1/2}\) for large \(k\)) will help the interval-arithmetic root-finder prune search intervals.

These lemmas are small and probably provable from known Bessel bounds without needing the full uniform phase machinery; they should be added to the obligation graph.

---

## What should be tested next

1. **Smoke-test the cross-product formula numerically** (diagnostic only). Write a high-precision floating-point script that, for a few values of \(\rho\) and \(\ell\), computes the first few zeros of \(F_{\nu,\rho}\) and verifies that the resulting eigenvalues match those obtained from a finite-element discretisation of the shell (to six digits). This does not prove the formula but would catch gross sign or convention errors.

2. **Prove the trivial angular cutoff lemma** and test its tightness numerically.

3. **Implement a minimal interval-arithmetic `J_nu`, `Y_nu` for half-integer order** using Arb's `acb_hypgeom_bessel_j` and `acb_hypgeom_bessel_y` or equivalent, and run a single-\(\ell\) root-isolation test for \(\ell=0,1\) and \(\rho=0.5\) on an interval up to \(k=20\). This will serve as the first concrete computation artifact for `COMP-certified-bessel`.

4. **Audit the FLPS and annulus source cards** -- until those are available, the exact phase definitions and counting conventions cannot be cross-referenced.

---

## Proposed state patch, if any

The following changes are suggested for Round 1 (subject to judge approval). They add evidence notes and refine statuses without promoting any theorem to "proved".

```yaml
- id: "SHELL-cross-product-formula"
  status: "open"
  statement_tex: "Audited formula matches standard separation of variables. Missing a rigorous completeness proof but no algebraic error found."
  evidence:
    positive:
      - "rounds/round1/A4_formula_audit.md"
    negative: []
    inconclusive: []
  next_action: "Prove the completeness lemma (Sturm-Liouville) and angular-cutoff lemma before using (1) as a legal dependency in lattice counts."

- id: "COMP-certified-bessel"
  status: " diagnostic_only"
  statement_tex: "Plan documented. No committed script, exact command, or root-enclosure report exists."
  evidence:
    positive:
      - "rounds/round1/A4_computation_plan.md"
    negative: []
    inconclusive: []
  next_action: "Implement an Arb-based isolated root finder for ell=0,1, rho=0.5, k in [0,20] and commit the script."
  required_output:
    - "script: scripts/certified_shell_roots.jl (or .py)"
    - "exact command: julia scripts/certified_shell_roots.jl"
    - "root-enclosure report: table in accompanying .md"
    - "counting verification table: to be produced after phase enclosures are ready"
    - "limitations: current version only for rho=0.5, ell=0,1, max k=20"

- id: "SHELL-angular-cutoff-lemma"   # new obligation
  type: "lemma"
  track: "shell_analytic"
  title: "Trivial angular cutoff"
  status: "proposed"
  statement_tex: "For each Lambda and rho, ell_max(Lambda,rho) = max ell such that the first Dirichlet eigenvalue of the radial equation is < Lambda. Provide an explicit, rigorous upper bound for ell_max."
  dependencies: []
  implies: ["SHELL-cross-product-formula"]
  owner: "A4"
  next_action: "Formulate and prove a simple monotonicity bound using Bessel first-zero asymptotics or a Rayleigh quotient."
```

The first two entries modify existing obligations; the third introduces a new lemma that will be needed to make the sum (1) finite.

---

## Confidence

- **Formula audit confidence: 0.95.** The Bessel cross-product and the multiplicity sum have been checked against standard references and are extremely unlikely to contain an algebraic error.
- **Overall proof-plan confidence: 0.45.** The existence of a uniform phase enclosure for the two-parameter family \(F_{\nu,\rho}\) is the dominant risk; the parallel tracks (ellipse, certificate family) may become necessary if the shell phase estimates cannot be closed.
- **Certified computation confidence: 0.30.** No implementation has been attempted; the plan is sound in principle but the practical difficulty of building a validated root-isolation routine for cross-products of half-integer Bessel functions should not be underestimated. We estimate several rounds of debugging and refinement before a finite-window verification for a single \(\rho\) can be completed.

The next concrete step is to produce a minimal working validated root-finder for a fixed \(\rho\) and small \(\ell\); that will immediately expose missing infrastructure or gaps in the Bessel enclosures.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a referee-style report on A2, A3, and A4. Include a score table, hidden assumptions, exact claims needing proof, concrete verification tasks, and a research-strategy adjustment recommendation.



## Required Output Schema

## Most valuable input from others

## Claims that look correct

## Claims that need proof

## Possible errors or hidden assumptions

## Suggested synthesis

## Research strategy

## Verification

## Proposed state changes to accept or reject

## Score by agent

| Agent reviewed | Idea quality (0-10) | State evidence (0-10) | Calibration (0-10) | Main reason | Must verify next |
|---|---:|---:|---:|---|---|
Score every other active agent shown under `## Outputs To Review`. Do not omit this table.
Idea quality scores routes, formulas, and diagnostics. State evidence scores what can safely mutate the proof-obligation graph. Calibration scores status labels, hypotheses, and avoidance of overclaiming.

## Next-round recommendation

## Confidence
