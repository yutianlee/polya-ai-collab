# Next Round Prompts

Date: 2026-07-15

Phase: post-completion handoff for the internal spherical-shell program.

## Authoritative boundary

Read `state/proof_obligations.yml` first. It has 61 obligations and SHA-256
`b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`.
The Round 22 patch has already been applied exactly once. Do not replay it or
route new work from the graph's historical top-level `round_selection` prose.

The source-final judge and both independent application gates are:

- `rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`,
  SHA-256 `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2`;
- `rounds/polya-main/round_022/reviews/state-patch-final-audit-source-utf8-final.md`,
  SHA-256 `3d0952f7a0c3aac820427f90249e9f8d5ece5d6f20e1d0bdcc2e9af11f5adc69`,
  **PASS** before application; and
- `rounds/polya-main/round_022/reviews/state-patch-application-audit-source-utf8-final.md`,
  SHA-256 `79a46f1e6398cb5887a98dc56142470a3b656b4153f969eec8db07df7604df58`,
  **PASS** after application.

## Completed internal result

For every genuine bounded three-dimensional spherical shell

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R,
$$

and the strict Dirichlet count

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

the internally reviewed theorem is

$$
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad \Lambda\ge0,
$$

where $L_3=1/(6\pi^2)$. A separate internally reviewed theorem proves that
no shell in the same complete $0<r<R$ family tiles $\mathbb R^3$ by congruent
rigid-motion copies with pairwise-disjoint interiors and exact or
almost-everywhere coverage. It also covers the corresponding closed-copy
formulation after removal of the countable null boundary union.

Accordingly, `SHELL-spherical-shell-nontiling`, `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target` are
`proved_internal` with empty blockers. This closes the project-internal shell
program only. It does not prove the general Pólya conjecture and makes no
claim of literature novelty, priority, firstness, or publication readiness.

## Scope that must remain fixed

- `CERT-round21-compact-proxy` certifies exactly 10,580 rational leaves on
  $[7/51,39/50]\times[12,200]$.
- `CERT-round21-aggregate-tail` certifies exactly 1,286 base boxes on
  $7/51\le\rho\le39/50$ at the single frequency $K=200$; it makes no proof
  decision for $K>200$. The tail on
  $\rho_c\le\rho\le39/50$, $K\ge200$, is analytic.
- `COMP-certified-bessel` remains `diagnostic_only` and detached from the
  theorem path.
- Strict eigenvalue walls, the $\Lambda=0$ case, the shell volume, and the
  scaling identity
  $N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda)$ remain part of the theorem.

## Next work: pre-publication, not proof blockers

These tasks do not reopen the proved-internal nodes unless they expose a
specific mathematical defect.

### Human reconstruction

Reconstruct every bottleneck lemma line by line from its accepted premises.
In particular, check strict counting at integer walls, all ratio and frequency
seams, the empty $\mathcal D_{21}$ set arithmetic, the analytic $K\ge200$
propagation, $\Lambda=0$, Weyl normalization, arbitrary-radius scaling, and
the rigid-motion non-tiling argument. Record the first concrete defect, if
any; agreement or test output alone is not verification.

### Manuscript assembly and audit

Turn the authenticated theorem and geometry lifecycles into one coherent
manuscript. Keep computational certificates at their exact scopes, separate
the spectral and geometric proofs until their conjunction, and commission a
fresh manuscript-level referee after the exposition is frozen.

### Current literature search

Run an independent, up-to-date search for prior results covering the exact
strict inequality and the exact shell class. Until that search and a human
comparison are complete, make no novelty or priority statement. Literature
status is a publication question, not a dependency of the proved-internal
mathematical graph.

### Optional parallel tracks

`ELLIPSE-near-circular` and `CERT-certificate-family` remain open independent
tracks. They may be pursued in parallel, but success, failure, or delay on
either track must not change the completed shell statuses. The legacy Bessel
framework may be used for diagnostics or regression tests only.

## Preserved negative chronology

Do not cite the failed scope-line or encoding cycles as positive evidence.
The first combined program-scope cycle misstated a 300-line geometry report
as 299 lines; its first judge was never applied. A later replacement judge
contained four `U+8D38` substitutions for intended `U+00F3` in “Pólya”; it
also failed its gate and was never applied. Only the source-UTF-8 final judge
and the two PASS audits listed above authorize the current graph.

## Non-negotiable handoff rules

- Do not reapply the Round 22 State Patch.
- Do not describe the internal shell result as the general Pólya conjecture.
- Do not infer novelty, priority, or publication readiness from graph status.
- Do not broaden either Round 21 certificate or promote diagnostic evidence.
- Do not let optional ellipse or certificate-family work alter shell status.
- If a genuine defect is found, freeze its exact claim and provenance before
  proposing any graph change.
