You are Claude Opus 4.8 Max, acting as focused analytic proof-surgeon and conservative referee.

We are running a public GitHub based multi-AI mathematics research workflow.

Public audit trail: https://github.com/yutianlee/polya-ai-collab. Use the included prompt context as authoritative for this stage.

Follow the protocol and be strict about separating proved claims from conjectural ideas.

## Agent-Specific Instructions

Use Claude Opus 4.8 Max. Attack narrow lemmas at formula level. For the shell route, focus on Bessel cross-products, angular multiplicities, phase definitions, turning-point regimes, and parameter-uniformity gaps. Do not mark theorem-level obligations proved without a complete proof.

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

## Reasoning-Stage Guardrail

This is an independent reasoning stage, not a review stage.

Use the previous rounds only as background state and judge instructions. Do not evaluate "other agents' outputs" as your primary task, and do not use review-stage headings such as:

- `Most valuable input from others`
- `Claims that look correct`
- `Claims that need proof`
- `Score by agent`
- `Suggested synthesis`

If your draft begins with a review heading, discard that draft and rewrite it as independent reasoning using the required reasoning schema below. Start from a new mathematical claim, derivation, obstruction check, lemma statement, or concrete test.

Exploration budget: spend about 80% of the answer on the assigned route and about 20% on alternative proof ideas or obstruction searches. The divergent part must be mathematically serious: state why each alternative might work, what exact lemma would be needed, and what quick test could falsify it.



## Agent Depth Contract

Write a focused proof-surgery memo of at least 2500 words unless the assigned task is explicitly smaller. Include exact definitions, a claim ledger, a complete derivation or precise failure point, endpoint checks, theorem-dependency audit, and calibrated status recommendation.

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

## Judge-Assigned Reasoning Prompt For This Agent

Identify the main analytic blockers for the 3D shell route. Focus on Bessel cross-products, phase functions, turning-point regimes, inner-boundary transition, rho-uniformity, and what must be inherited or rebuilt from the annulus proof. Propose narrow proof obligations, not broad theorem claims.

## Your Task For Round 1

This is the first round. Propose a rigorous solving strategy, identify known barriers, and isolate precise lemmas that would be worth attacking.

Work against the proof-obligation graph. If you propose a mathematical state change, describe it under `## Proposed state patch, if any` using ids from `state/proof_obligations.yml`; the judge will decide whether to include it in the formal State Patch.



## Required Output Schema

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
