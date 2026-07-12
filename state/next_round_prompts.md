# Next Cycle Role Prompts

Workflow revised after round 1. These are obligation-specific role assignments, not universal panel tasks.

## For A1

Role: project lead and integrator.

Prepare exact obligation packets for `SHELL-phase-oscillatory`, `SHELL-phase-outer-turning`, `SHELL-inner-turning`, and `SHELL-phase-evanescent`. Each packet must state quantifiers, parameter region, permitted dependencies, explicit constants required, inequality direction, overlap boundary, and falsification cases.

Maintain `SHELL-phase-overlap` as a separate bottleneck. Do not integrate the phase enclosure until all regime statements exist. Review A2, A3, and A4 only for state-promotable evidence, then author the sole `State Patch`. Continue the necessary Bessel and annulus source-card audits in parallel.

## For A2

Role: incumbent analytic proof author.

Develop the incumbent fixed-$\rho$ phase-enclosure package. Treat the following as distinct obligations:

1. ordinary oscillatory regime;
2. outer Airy turning point $k-\nu=O(\nu^{1/3})$;
3. inner-boundary Airy transition $\rho k-\nu=O(\nu^{1/3})$;
4. mixed and fully evanescent regimes.

Give explicit one-sided constants, track the loss from subtracting phase bounds, and declare the overlap intervals. Do not claim `SHELL-phase-enclosures` merely from asymptotic formulas. Freeze the incumbent attempt before adversarial review.

## For A3

Role: clean-room solver.

Use only the reduced clean-room packet. Do not consult `state/best_proof_draft.md`, previous reviews, or the incumbent A2 response. Explicitly confirm this independence.

Independently reconstruct the selected bottleneck phase lemma from its exact statement and permitted source dependencies. Attempt falsification at both Airy layers, in the mixed evanescent/oscillatory region, and at every proposed overlap. Return a complete proof, counterexample, first failure point, or sharper replacement statement. Do not work on the weighted lattice problem during this cycle unless the project lead explicitly changes the selected obligation.

## For A4

Role: adversarial referee and computation engineer.

After the A2 and A3 attempts are frozen, compare only those two assigned outputs. Reconstruct every displayed identity, check inequality directions, quantifier order, branch normalization, uniformity, and regime overlap. Identify the first unsupported implication; do not average scores into a correctness judgment.

Separately, continue `COMP-certified-bessel`. Label outputs as `floating_point_experiment`, `symbolic_sanity_check`, `interval_certified`, or `formal_verified`. A diagnostic prototype remains `diagnostic_only`. Any future certification must include software/version, deterministic command, coverage statement, code/input hashes, root-enclosure artifacts, and limitations.

## Promotion constraint

No Pólya theorem may be promoted in this cycle. A bottleneck may be promoted only with explicit proof evidence, a clean-room artifact, an adversarial-review artifact, discharged source dependencies, and any computation certificate the statement actually requires.
