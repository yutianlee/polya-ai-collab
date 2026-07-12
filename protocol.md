# Proof-Obligation Research Protocol

The project is organized around proof obligations, not fixed all-agent panels. Agents are assigned only when their role is needed for the selected obligation. Agreement is evidence; it is never mathematical verification.

## Authoritative State

`state/proof_obligations.yml` is the authoritative mathematical state. Round artifacts under `rounds/` are evidence and audit trail. Only a validated `State Patch` may mutate the graph.

Every open-like obligation must have an exact statement, dependencies, blockers, an owner, and a concrete next action. A bottleneck or theorem obligation must additionally identify three distinct roles:

- `lead_author`: develops and maintains the incumbent proof;
- `clean_room_reviewer`: attempts the lemma from its statement without seeing the incumbent proof;
- `adversarial_reviewer`: later audits the incumbent and clean-room arguments for the first unsupported implication.

## Selecting Work

Each cycle selects one primary obligation and at most one independent secondary obligation. Workstreams that do not depend on one another may proceed concurrently. A global barrier is used only where a genuine mathematical dependency requires it.

The project lead maintains the obligation graph and integrates results. The lead is not allowed to promote a claim merely because several agents agree.

## Obligation Packet

Before assigning a bottleneck lemma, prepare a compact packet containing:

1. the exact statement and all quantifiers;
2. definitions and notation;
3. the complete parameter domain;
4. permitted previous results and dependency IDs;
5. required explicit constants and error directions;
6. boundary, endpoint, and falsification cases;
7. the expected proof or certificate artifact.

The clean-room packet must exclude the incumbent proof, previous reviews of that proof, and judge commentary that reveals its argument. It may include audited source statements listed as permitted dependencies.

## Workflow Stages

### Stage A — Decomposition and assignment

The project lead selects obligations, checks their dependency boundaries, and assigns only the roles needed for the cycle. Large targets are split into bounded obligations before proof attempts begin.

For the shell phase problem, the minimum decomposition is:

- ordinary oscillatory regime;
- outer turning point $k\sim\nu$;
- inner-boundary transition $\rho k\sim\nu$;
- mixed and fully evanescent regimes;
- overlap and compatibility between the regime estimates;
- compact-$\rho$ uniformity;
- the endpoint limits $\rho\to0$ and $\rho\to1$.

### Stage B — Primary and clean-room attempts

The lead author develops the incumbent proof. Independently, the clean-room reviewer receives only the obligation packet and produces either:

- a complete reconstruction;
- a counterexample;
- a precise failure point;
- or a sharper replacement statement.

The clean-room reviewer must state which dependencies were used and confirm that the incumbent proof was not consulted.

### Stage C — Adversarial audit

After both attempts are frozen, the adversarial reviewer receives them and checks:

- every displayed identity and inequality direction;
- quantifier order and parameter uniformity;
- branch, endpoint, multiplicity, and counting conventions;
- transition and overlap regions;
- circular or undeclared dependencies;
- the first unsupported implication.

This is reconstruction and falsification, not a popularity vote or broad scorecard.

### Stage D — Certified computation

Use this stage only when the obligation genuinely contains a finite computational component. Computation evidence is classified as:

- `floating_point_experiment`;
- `symbolic_sanity_check`;
- `interval_certified`;
- `formal_verified`.

Only `interval_certified` and `formal_verified` evidence may give a computation obligation status `certified`. A certified artifact must record the software and version, deterministic reproduction command, precision or interval backend, parameter subdivision, coverage statement, code/input hashes, root-isolation or proof method, and limitations.

Floating-point plots, tables, and high-precision experiments remain diagnostic evidence even when they are persuasive.

### Stage E — Lead synthesis and manuscript assembly

One lead agent assembles accepted obligations into a single coherent proof. This stage must:

- normalize notation and strict-counting conventions;
- propagate constants and hypotheses through dependencies;
- prove that all parameter regimes and overlaps are covered;
- remove duplicated or incompatible assumptions;
- map every manuscript claim to an obligation ID.

Assembly does not repair missing lemmas by prose. Missing links return to Stage A as new obligations.

### Stage F — Fresh final referee audit

A fresh reviewer receives the assembled manuscript and an audited dependency packet, but not the development discussion. The referee reconstructs the bottleneck lemmas, checks all endpoint regimes, and identifies the first unsupported implication. Findings become graph evidence; the referee does not directly mutate state.

### Stage G — Validation and state update

The validator applies or rejects the lead's JSON-compatible YAML `State Patch`, regenerates the reading packet, and records the result. Promotion of a bottleneck or theorem requires explicit proof evidence, a clean-room artifact, an adversarial-review artifact, and all required certified computation.

## Role Guidance

Use the strongest whole-project work environment for obligation mapping, workstream coordination, and integration. Use a fresh high-capability chat for a single bottleneck lemma and a separate fresh chat for adversarial review. Use Codex for interval arithmetic, certified eigenvalue calculations, symbolic checks, reproducible scripts, tests, and formalization. Use a coherent single-agent pass for final manuscript assembly.

Roles are functional rather than permanently tied to A1–A4. The same agent must not be lead author and independent reviewer for the same bottleneck.

## State Patch Rules

The lead synthesis is the only artifact that may contain `## State Patch`. The patch may create, update, reject, or record no change for obligations. It must not promote a claim without exact evidence and a reason.

Allowed statuses are:

```text
proposed
open
blocked
diagnostic_only
source_audit_required
derived_under_assumptions
proved_internal
proved_external_dependency
certified
rejected
```

`certified` is reserved for computation obligations backed by interval or formal evidence. It is not a mathematical proof status.

## Mathematical Safety Rules

- Do not mark a claim proved unless the proof is explicit and its dependencies are discharged.
- Preserve failed attempts and counterexamples.
- Name every external theorem and verify its hypotheses in a source card.
- Require falsification tests for every new bottleneck lemma.
- Treat strict versus non-strict counting and eigenvalue multiplicities explicitly.
- Do not claim the shell, ellipse, or another new Pólya theorem until analytic reductions, parameter uniformity, regime overlaps, and finite verification are complete.
- A human must reconstruct every decisive bottleneck lemma before a public theorem claim.

## Public Record

Completed cycles should be committed and pushed unless the runner is invoked with `-NoAutoPublish`. Human directives in `human/` override earlier AI strategy while remaining subject to mathematical validation.
