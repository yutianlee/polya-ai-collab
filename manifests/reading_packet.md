# Reading Packet

Run: `polya-main`

Current phase: internally completed spherical-shell theorem; human
reconstruction, conventional review, and literature comparison.

## Authority

The authoritative graph is `state/proof_obligations.yml`, with 63 unique
obligations, no selected proof-changing target, and frozen SHA-256
`c11958f81da30cadb08c46421b60769fec3a40c7345aa13f9c22a9f86069af65`.

The Round 22 State Patch is historical and must not be replayed. The current
top-level `round_selection`, the Round 25 proof artifacts, and the Revision 2
referee repairs control the live proof.

## Exact claim

For every genuine three-dimensional spherical shell
\(A_{r,R}=\{x:r<|x|<R\}\), \(0<r<R\), and \(\Lambda\geq0\), the internal
theorem proves

\[
N_D(A_{r,R},\Lambda)
\leq L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.
\]

It uses strict counting internally. This is not a result for general domains
and carries no novelty, priority, or publication claim.

## Minimal reading order

1. `human/inbox/revision_2.md` and `human/inbox/revision_2_2.md` for the
   line-by-line referee recommendations and verification-boundary audit.
2. `human/inbox/revision_1.md` for the two simplifying estimates.
3. `rounds/polya-main/round_025/reviews/revision1-independent-audit.md` for
   corrections and independent checks.
4. `manuscript/spherical-shell-polya-proof.tex` for the assembled proof.
5. `manuscript/analytic/ratio-sharp-global-closure-body.tex` for every detail
   of the new low/middle-ratio theorem.
6. `manuscript/spherical-shell-polya-analytic-supplement.tex` for the compiled
   support-volume wrapper.
7. `output/submission/spherical-shell-polya-revision2/` for the flattened,
   self-contained review handoff.
8. `state/proof_obligations.yml` for authoritative dependency metadata.

## Live proof spine

The phase enclosure gives \(N_D\leq P\), and the exact layer cake compares
\(P\) with the Weyl action \(W\). The disjoint parameter cover is:

- \(K\leq\pi/(1-\rho)\): no mode;
- \(K>\pi/(1-\rho)\), \(0<\rho<39/50\): ratio-sharp angular payment,
  tangent-envelope radial reserve, ball quarter-layer, and scalar convexity;
- \(K>\pi/(1-\rho)\), \(39/50\leq\rho<1\): optical theorem.

The first frequency face is no-mode-owned and \(\rho=39/50\) is
optical-owned. Dilation gives all \(A_{r,R}\).

The former small-hole split, finite staircases, 38-state theorem, residual
sets, finite ledgers, and certificates are historical or optional regression
material only.

## Release identification

| Artifact | TeX SHA-256 | PDF SHA-256 |
|---|---|---|
| Main paper | `e456265c7e0c30a0ea0b56f1f8b9742548d2d6c0296671bd22ec60df5ad19fd4` | `fc5afa529e7a797e89509c40f6be05cd7bf4c61462fddf826476f3ce7ea1c63f` |
| Analytic supplement | `58c3d303bfe1b17a21cd31445fd6f8b52a52384817dbfdc2fec4ba00ca3c3706` | `cd6974ea1e1fa9e61a7dff21c664b175bb4ca0321240f5fdb3b22a1bd53bb294` |

The main paper is 23 pages and the supplement is 9 pages. The full component
manifest is `manuscript/analytic/MANIFEST.md`.

## Verification boundary

The Revision 2 release passed independent angular, radial/ball, scalar,
source-reference, packaging, and exact-fraction audits. Exact-rational and
outward-rounded interval checks are regression checks only, not proof premises.

Before external publication, require a human line-by-line reconstruction,
conventional referee review, and a current literature/novelty search.

## Do-not-claim rules

- Do not call this a proof for general domains.
- Do not claim novelty, priority, firstness, or publication acceptance.
- Do not reintroduce finite or numerical artifacts as premises of the analytic
  theorem.
- Do not omit strict walls, \(\Lambda=0\), or arbitrary-radius scaling.
