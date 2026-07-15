# Reading Packet

Run: `polya-main`

Current phase: completed internal spherical-shell program; pre-publication
reconstruction, manuscript preparation, and literature review.

## Authority

The authoritative graph is `state/proof_obligations.yml`, with 61 obligations
and SHA-256
`b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`.
Its Round 22 State Patch has already been applied exactly once. Current
obligation records override the preserved historical `round_selection` text.

The final application chain is:

1. source-final judge:
   `rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`,
   SHA-256 `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2`;
2. independent pre-application audit, **PASS**:
   `rounds/polya-main/round_022/reviews/state-patch-final-audit-source-utf8-final.md`,
   SHA-256 `3d0952f7a0c3aac820427f90249e9f8d5ece5d6f20e1d0bdcc2e9af11f5adc69`;
3. independent post-application audit, **PASS**:
   `rounds/polya-main/round_022/reviews/state-patch-application-audit-source-utf8-final.md`,
   SHA-256 `79a46f1e6398cb5887a98dc56142470a3b656b4153f969eec8db07df7604df58`.

Do not reapply the patch.

## Exact completed claim

For

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R,
$$

with strict counting

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

the internal theorem proves, for every $\Lambda\ge0$,

$$
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.
$$

The separately reviewed geometry theorem proves that every shell in exactly
the same $0<r<R$ class fails to tile $\mathbb R^3$ by congruent rigid-motion
copies with pairwise-disjoint interiors and exact or almost-everywhere
coverage. The closed-copy formulation follows after removing the countable
null union of boundaries.

The graph therefore records `SHELL-spherical-shell-nontiling`,
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` as `proved_internal` with empty blockers. This is an
internal result for genuine three-dimensional spherical shells only. It is
not the general Pólya conjecture and carries no literature-novelty, priority,
first-proof, or publication-readiness claim.

## Minimal canonical reading order

1. Applied authority: `state/proof_obligations.yml`.
2. Spectral statement:
   `state/lemma_packets/TARGET-shell-d3-round22-theorem.md`, SHA-256
   `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228`.
3. Spectral reconstruction and adversarial review:
   `rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md`,
   `rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md`, and
   `rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md`.
4. Geometry statement:
   `state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md`, SHA-256
   `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f`.
5. Geometry reconstruction and adversarial review:
   `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md`,
   its `spherical-shell-nontiling-clean-room-addendum.md`, and
   `rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md`.
6. Same-class conjunction and scope:
   `rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md`.
7. Source-final judge and the two PASS audits in the authority section.

Read older artifacts only when reconstructing a cited premise or its failure
chronology. They do not supersede this order.

## Proof and certificate boundary

The unit-shell theorem includes $\Lambda=0$, strict phase/eigenvalue walls,
all ratio and frequency seams, the exact empty successor residual
$\mathcal D_{21}=\varnothing$, Weyl normalization, and

$$
N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda).
$$

The computational scope is deliberately narrower than the theorem:

- `CERT-round21-compact-proxy` is `certified` only on
  $[7/51,39/50]\times[12,200]$, with 10,580 exact rational leaves;
- `CERT-round21-aggregate-tail` is `certified` only for 1,286 base boxes on
  $7/51\le\rho\le39/50$ at the single frequency $K=200$ and makes no proof
  decision for $K>200$; analytic curvature and integration prove the tail on
  $\rho_c\le\rho\le39/50$, $K\ge200$; and
- `COMP-certified-bessel` remains `diagnostic_only`, detached from the
  theorem path.

Tests, displayed decimals, and agent agreement are not substitutes for the
accepted analytic bridges.

## Negative chronology to preserve

Two failed Round 22 gates remain negative evidence only:

1. the first combined program-scope cycle described the hash-matching
   geometry referee as 299 lines although the authenticated file has 300;
   the associated first judge was never applied; and
2. a subsequent replacement judge changed four intended `U+00F3` characters
   in “Pólya” to `U+8D38`; its audit failed and that judge was never applied.

The source-final judge repaired both provenance issues. Only it and the PASS
pre- and post-application audits authorize graph hash `b17b173e…`.

## What remains

The remaining work is pre-publication quality control, not an open theorem
dependency:

- a human line-by-line reconstruction of every bottleneck lemma;
- conversion of the accepted evidence into a coherent manuscript followed
  by an independent manuscript-level referee; and
- a separate current literature search and human comparison before any
  novelty or priority language is considered.

If this work finds a concrete mathematical error, freeze the exact disputed
claim and evidence before proposing a new audited graph patch. Otherwise, do
not reopen or downgrade the completed shell nodes merely because publication
work is unfinished.

## Independent optional tracks

`ELLIPSE-near-circular` and `CERT-certificate-family` remain open and may run
in parallel. They are neither premises nor blockers of the shell theorem.
Their progress must not alter `TARGET-shell-d3` or `POLYA-program-target`.
Use `COMP-certified-bessel` only for diagnostics or regression checking.

## Do-not-claim rules

- Do not call this a proof of the general Pólya conjecture.
- Do not claim literature novelty, priority, firstness, or readiness for
  publication from internal graph status.
- Do not broaden either Round 21 certificate to an all-frequency numerical
  proof.
- Do not omit strict counting, $\Lambda=0$, or arbitrary-radius scaling.
- Do not promote diagnostic or optional-track evidence into the shell path.
- Do not reapply the Round 22 State Patch.
