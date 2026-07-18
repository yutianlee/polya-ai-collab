# Current State

Date: 17 July 2026

The authoritative mathematical state is `state/proof_obligations.yml`.
It contains 63 unique obligations and, after the Revision 2 review refresh,
has SHA-256 `c11958f81da30cadb08c46421b60769fec3a40c7345aa13f9c22a9f86069af65`.

## Theorem status

The repository records a project-internal proof of the sharp Dirichlet Pólya
inequality for every genuine three-dimensional spherical shell

\[
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R.
\]

With strict counting

\[
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
\]

the result is

\[
N_D(A_{r,R},\Lambda)
\leq \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.
\]

This is an internal result for the spherical-shell class. It is not a proof of
the general Pólya conjecture and is not a claim of novelty, priority, external
peer review, or publication readiness.

## Revision 2 reviewed proof

For the unit shell, write \(K=\sqrt\Lambda\). The exact disjoint cover is

\[
\begin{array}{ll}
K\leq\pi/(1-\rho):
  &N_D(A_{\rho,1},K^2)=0,\\[2mm]
K>\pi/(1-\rho),\quad 0<\rho<39/50:
  &N_D\leq P<W,\\[2mm]
K>\pi/(1-\rho),\quad 39/50\leq\rho<1:
  &N_D<W\quad\text{by the optical theorem}.
\end{array}
\]

The low/middle-ratio inequality is the ratio-sharp retained-remainder theorem.
It uses:

1. the strict phase-to-proxy bridge and exact layer cake;
2. the ratio-dependent angular cap
   \(q\leq\arccos(\rho)/\pi\);
3. the tangent minorant \(L_\sharp\leq\mathfrak W\);
4. reduction to the universal ball quarter-layer; and
5. exact base and derivative convexity proving \(W-P>0\).

The seam \(\rho=39/50\) is optical-owned. The face
\(K=\pi/(1-\rho)\) is no-mode-owned. Strict radial and angular walls remain
strict throughout.

## Dependency state

The live theorem chain is

\[
\begin{gathered}
\text{phase/count/Sturm--Liouville}
\longrightarrow
\texttt{SHELL-analytic-retained-remainder-closure},\\
\texttt{SHELL-analytic-retained-remainder-closure}
\quad+\quad
\texttt{SHELL-rho-one-endpoint}
\longrightarrow
\texttt{SHELL-rho-uniformity}
\longrightarrow
\texttt{TARGET-shell-d3}.
\end{gathered}
\]

`round_selection.target_obligations` is empty. The former \(\rho_*\) owner,
finite staircases, 38-state theorem, residual sets, zero/event registry,
611-row ledger, and interval or executable certificates have no live theorem
implication. They remain in the historical archive and as optional regression
material.

The proposed low-interface shifted-tail theorem is detached optional research,
not a blocker. The double-sawtooth/packing node remains diagnostic only.

## Evidence and remaining work

The current mathematical audits include
`rounds/polya-main/round_025/reviews/revision1-independent-audit.md`,
`human/inbox/revision_2.md`, and `human/inbox/revision_2_2.md`.
Independent passes reconstructed the angular, radial/ball, and scalar
components and found no mathematical failure. Exact rational and
outward-rounded interval scripts are optional transcription regressions only.

Before external dissemination, the remaining work is:

- human line-by-line reconstruction of every bottleneck lemma;
- conventional independent referee review of the assembled manuscript; and
- a current literature and novelty comparison.

The separately reviewed non-tiling theorem concerns the same complete
\(0<r<R\) shell family. The ellipse/Mathieu and certificate-family tracks
remain separate open programs.
