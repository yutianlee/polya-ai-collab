# Round 22 Theorem-Claim Scope Audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

The frozen packet is a coherent proof-free theorem claim with an exact,
noncircular input boundary. It preserves the Round 21 finite/analytic split,
states every theorem-assembly seam and normalization obligation, and makes no
theorem, non-tiling, program, novelty, or publication-priority promotion.
This report audits only identity, scope, dependencies, and claim bookkeeping;
it is not an incumbent proof or a theorem verdict.

## 1. Authentication

The packet reproduces the identity declared by the freeze exactly:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | 6,568 | 244 |

The file is strict UTF-8 without a BOM, has LF endings and one terminal LF,
and has no tab, trailing-whitespace line, replacement character, or forbidden
control byte. The 244-line count is therefore unambiguous.

The accompanying freeze currently has SHA-256
`6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d`,
2,157 bytes, and 60 physical lines. Its declared baseline resolves exactly to
current `HEAD`:

`07df801fe031e55d53a46c25e3ae98d27a8ad8e4`.

The other authenticated inputs reproduce as follows:

| artifact | reproduced SHA-256 |
| --- | --- |
| `state/proof_obligations.yml` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` |
| `rounds/polya-main/round_021/judge/judge-021-lemma.md` | `a620175fc43591cd80fcc9f50165d7b21596b077d92fbc4450167d21a4eca9aa` |
| `rounds/polya-main/round_021/reviews/state-patch-lemma-application-audit.md` | `c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef` |

The graph, judge, and application audit working bytes equal their `HEAD`
blobs. The graph parses with 60 unique obligations, and the canonical graph
validator reports `Graph OK`. Thus the graph hash frozen by Round 22 is the
current post-Round-21 authority, not a pre-application or stale-hash graph.

## 2. Exact dependency and status boundary

The packet permits exactly five direct promoted mathematical inputs:

| whitelisted input | current status |
| --- | --- |
| `CONV-strict-counting` | `proved_internal` |
| `SHELL-sturm-liouville-completeness` | `proved_internal` |
| `SHELL-rho-zero-endpoint` | `proved_internal` |
| `SHELL-rho-compact-analytic-envelope` | `proved_internal` |
| `SHELL-rho-one-endpoint` | `proved_internal` |

The only extra derivable facts allowed are elementary Euclidean volume,
`omega_3=4 pi/3`, and unitary dilation of the Dirichlet Laplacian. None of the
three primary outputs is assumed as an input. In particular, the current
statuses remain:

| obligation not available as a premise | current status |
| --- | --- |
| `SHELL-rho-compact` | `open` |
| `SHELL-rho-uniformity` | `open` |
| `TARGET-shell-d3` | `open` |
| `POLYA-program-target` | `open` |

The mention of `SHELL-exact-d20-closure` inside item 4 is a scope-qualified
component of the promoted analytic-envelope input, not a sixth open theorem
premise. That component is itself `proved_internal`. Its two finite
certificate obligations have status `certified`, while the obsolete parent
`COMP-certified-bessel` remains `diagnostic_only`. The packet does not use
that diagnostic parent, either pilot box, a numerical experiment, a Weyl
remainder, a tiling theorem, or a new Bessel-zero assertion.

The phrase "authenticated positive evidence" is also correctly bounded by
the current graph classification. The Round 21 unscoped, stale-hash, and
cache-vulnerable cycles remain negative evidence and are expressly forbidden
by the packet. No failed or superseded artifact is silently revived.

## 3. D20 closure, D21, and the certificate/analytic seam

The packet's compact-middle scope agrees with both the final Round 21 judge
and the applied graph:

\[
\mathcal D_{20}=\{\rho_c\leq\rho<39/50,\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

The source-execution boundary is preserved exactly:

- the 10,580 compact certificate leaves own finite proxy predicates only on
  the closed rectangle
  `[7/51,39/50] x [12,200]`;
- the 1,286 aggregate boxes own base predicates only on the exact rational
  ratio superset `[7/51,39/50]` at the single frequency `K=200`;
- the spectral bridges and the universal aggregate propagation for
  `K>=200` are analytic, not an all-frequency finite-box certificate;
- the guard `k_11(rho)>12` is available only for
  `rho_c<=rho<1`; and
- the subtraction owners are `D20 intersect {K<=200}` and
  `D20 intersect {K>200}`, with the shared theorem face `K=200` subtracted
  only by the compact owner.

This handles all three possible orderings of `U(rho)` relative to 200 and
leaves the exact successor residual `D21` empty without omission or double
subtraction. Empty `D21` promotes no higher obligation: the compact
assembly, uniformity, shell theorem, and program target all remain open for
their distinct Round 22 gates.

## 4. Domain partition and seam ownership

The outer partition is exact and disjoint:

\[
(0,1)=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}[7/8,1).
\]

The definitions give a positive, nondegenerate `rho_*` strictly below
`7/8`, and the packet explicitly requires those inequalities to be derived
exactly in the reconstruction. The owner assignments are unambiguous:

- `rho=rho_*` belongs to the promoted small-hole endpoint;
- `rho=7/8` belongs to the promoted thin-shell endpoint; and
- the open middle ratio interval is supplied only by reconstruction of the
  complete accepted compact cover with empty `D21`.

The inherited internal ratio faces `rho_0=1/sqrt(337)`,
`rho_c=1/(1+2 pi)`, and `39/50` are retained as audit seams, as are every
moving frequency, high-frequency, staircase, eigenvalue, and phase wall.
Their overlaps do not alter the three outer owners. The mandatory
falsification list checks both descriptions at each outer seam and both
sides of `K=200` rather than converting overlap into double ownership.

## 5. Counting, zero frequency, and normalization

The packet fixes the strict convention

\[
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}
\]

with multiplicity. It separately assigns `K=0`: positivity of the
Dirichlet spectrum gives a zero strict count, and the cubic Weyl-volume side
is also zero. This avoids inference by continuity from `K>0`. It also
retains the strict exclusion at shell eigenvalues, adds multiplicities for
cross-channel coincidences, and records that an integer phase wall has count
one less than an ordinary floor. No endpoint convention is weakened.

The three-dimensional normalization is correct:

\[
L_3=\frac{\omega_3}{(2\pi)^3}=\frac1{6\pi^2},\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\]

so

\[
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3).
\]

The packet requires this computation to be rederived and does not substitute
a two-term Weyl estimate or remainder theorem.

## 6. Dilation direction and theorem scope

For `rho=r/R`, the packet uses the correct geometric and spectral
directions:

\[
A_{r,R}=R A_{\rho,1},\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}),
\]

and therefore

\[
N_D(A_{r,R},\Lambda)=N_D(A_{\rho,1},R^2\Lambda).
\]

The resulting factor is `R^3(1-rho^3)=R^3-r^3`, giving exactly
`L_3 |A_{r,R}| Lambda^(3/2)` for every `Lambda>=0`. The falsification cases
explicitly include `R<1`, `R>1`, `Lambda=0`, and the wrong
`R^{-2} Lambda` counting argument.

Finally, the packet claims only the spectral inequality for
three-dimensional spherical shells and its dilation corollary. It expressly
denies a non-tiling theorem, program-target completion, ellipse or
certificate-family completion, novelty, and publication priority. It also
keeps the endpoint limits `r=0` and `r=R` outside the claimed shell class.

## Final determination

**PASS. First issue: none.** The exact frozen packet bytes pass the
independent Round 22 claim-scope and dependency gate. This PASS authorizes
only the next isolated reconstruction/review stages named by the packet; it
does not prove the theorem, promote any obligation, or satisfy the separate
non-tiling and program-scope gates.
