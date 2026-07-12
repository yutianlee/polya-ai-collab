# Architecture and Workflow: Pólya AI Collaboration

The durable architectural rule is:

```text
claims, dependencies, and certificates—not transcripts or consensus—are the unit of progress.
```

`state/proof_obligations.yml` is authoritative. Work artifacts are evidence. A project lead may propose state changes, but only the validator may apply them.

## Research Architecture

The whole Pólya program is coordinated as a graph of bounded workstreams:

1. Bessel cross-product phase and zero estimates;
2. oscillatory, turning-point, inner-boundary, and evanescent regimes;
3. multiplicity-weighted lattice counting;
4. compact-parameter and endpoint analysis as $\rho\to0,1$;
5. certified finite-window verification;
6. independent clean-room and adversarial review;
7. coherent manuscript assembly.

The first theorem target remains exact Dirichlet Pólya for spherical shells in $\mathbb R^3$. The ellipse/Mathieu program remains the flagship parallel track, and a Jiang–Lin-style comparison family remains the fallback publication track.

## Obligation-Centered Assignment

The old fixed-panel assumption is retired. A cycle does not require every agent to attack and review every output. Instead, the selected obligation declares the roles it requires:

- a lead author;
- a clean-room reviewer for bottlenecks;
- an adversarial reviewer for bottlenecks;
- a computational verifier when finite certification is relevant;
- a project lead for integration.

Independent workstreams may run concurrently. Barriers exist only at actual dependency boundaries: an adversarial audit waits for frozen proof attempts, manuscript assembly waits for its component obligations, and theorem promotion waits for required certificates and reviews.

## Shell Phase Decomposition

`SHELL-phase-enclosures` is an integration obligation, not a single indivisible lemma. It depends on separate regime obligations for oscillatory behavior, the outer turning point, the inner-boundary transition, evanescent exclusion, and global overlap compatibility. Parameter uniformity and the two endpoint limits remain separate downstream obligations.

This structure prevents a proof in one asymptotic regime from being mistaken for a global phase enclosure.

## Independence Boundary

A bottleneck's clean-room reviewer receives an exact lemma packet but not the incumbent proof. After both attempts are frozen, an adversarial reviewer receives both and searches for the first unsupported implication. Agent agreement is logged as evidence only.

The graph records `lead_author`, `clean_room_reviewer`, `adversarial_reviewer`, `review_independence`, `clean_room_artifacts`, and `adversarial_review_artifacts`. These roles must be distinct for bottleneck and theorem obligations.

## Certification Boundary

Computational work uses four evidence classes:

```text
floating_point_experiment
symbolic_sanity_check
interval_certified
formal_verified
```

Only the last two may produce a `certified` computation obligation. Certification must be deterministic and reproducible and must state exactly which finite parameter window it covers. A certified computation discharges only the computation dependency named in the graph; it does not silently prove an analytic theorem.

## Proof Assembly and Final Review

Once component obligations are discharged, one lead assembles a linear manuscript proof with stable notation, explicit constants, complete parameter coverage, and obligation IDs attached to claims. A fresh final referee then receives a clean manuscript/dependency packet and conducts an independent adversarial audit.

The validator promotes a bottleneck or theorem only when the graph contains the explicit proof evidence, clean-room reconstruction, adversarial report, discharged dependencies, and any required certified computation.

## Runner Direction

The orchestration layer should support obligation-specific `reasoning_agents` and `review_assignments` rather than assuming universal participation. Clean-room prompts must omit incumbent proof drafts and prior reviews. Existing all-agent rounds remain historical evidence, not the default future workflow.

See [protocol.md](protocol.md) for stage rules and [docs/proof-obligation-workflow.md](docs/proof-obligation-workflow.md) for patch and validation mechanics.
