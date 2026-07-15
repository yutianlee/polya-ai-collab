# Round 22 replacement program-target scope audit

Date: 2026-07-15

Role: independent combined spectral/geometry scope audit

## Verdict

**PASS. First unsupported implication: none.**

The authenticated spectral lifecycle proves the strict Dirichlet Pólya
inequality at every spectral parameter for every bounded three-dimensional
spherical shell. The authenticated geometry lifecycle proves that every
member of exactly that same shell family is non-tiling under the stated
rigid-motion, disjoint-interior, exact/almost-everywhere open/closed coverage
conventions. The two proofs are logically independent and meet only at the
program target.

This PASS uses `new` only in the internal sense **new to this program's proved
class**. It makes no assertion of publication novelty, priority, firstness,
or absence from the literature. It changes no graph status and authorizes
only the separately audited State-Patch gate.

I reconstructed this scope comparison from the frozen theorem and geometry
lifecycles. I did not inspect either Round 22 judge file or any Round 22 State
Patch.

## 1. Replacement provenance and preserved failure chronology

The original combined report remains immutable at
`rounds/polya-main/round_022/reviews/program-target-scope-audit.md` with:

- SHA-256
  `d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5`;
- 15,538 bytes;
- 381 LF bytes; and
- a terminal LF.

It is superseded for one clerical reason only: its authentication table called
the geometry adversarial referee a 299-physical-line file. The exact referee
file
`rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md`
has:

- SHA-256
  `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53`;
- 13,290 bytes;
- exactly 300 bytes equal to LF (`0x0a`);
- a terminal LF;
- 300 entries under `.NET File.ReadAllLines`; and
- last numbered nonempty line `300:of this verdict.` under `rg -n '^'`.

On these exact bytes, PowerShell `(Get-Content -LiteralPath $p).Count`
misleadingly returns 299. That API result caused the earlier metadata error;
it is not the line metric used here. Every `LF count` below means the number
of raw `0x0a` bytes, and `terminal LF` reports whether the final byte is
`0x0a`. The earlier report's mathematical PASS is not repudiated, but this
replacement alone supplies corrected metadata and the current combined
scope verdict. The original report was not used as a premise in this audit.

## 2. Exact authentication

### 2.1 Spectral lifecycle

| artifact | SHA-256 | bytes | LF count | terminal LF |
| --- | --- | ---: | ---: | :---: |
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | 6,568 | 244 | yes |
| `rounds/polya-main/round_022/exploration/theorem-claim-freeze.md` | `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d` | 2,157 | 60 | yes |
| `rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md` | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` | 8,228 | 205 | yes |
| `rounds/polya-main/round_022/responses/shell-theorem-incumbent.md` | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` | 6,141 | 290 | yes |
| `rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md` | `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12` | 18,000 | 655 | yes |
| `rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md` | `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56` | 14,726 | 361 | yes |
| `rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md` | `6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458` | 5,514 | 161 | yes |
| `rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md` | `a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9` | 20,124 | 680 | yes |

### 2.2 Geometry lifecycle

| artifact | SHA-256 | bytes | LF count | terminal LF |
| --- | --- | ---: | ---: | :---: |
| `state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md` | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` | 4,703 | 105 | yes |
| `rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md` | `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a` | 992 | 30 | yes |
| `rounds/polya-main/round_022/reviews/nontiling-claim-scope-audit.md` | `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7` | 11,679 | 234 | yes |
| `rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md` | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` | 3,199 | 92 | yes |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md` | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` | 7,245 | 241 | yes |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md` | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` | 1,816 | 45 | yes |
| `rounds/polya-main/round_021/exploration/literature-scope-note.md` | `31a8bbb71c002daf77690591bd67114e943b3cb869484c517e35036042e52c23` | 2,620 | 50 | yes |
| `rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md` | `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53` | 13,290 | 300 | yes |

### 2.3 Shared graph authority

The shared pre-promotion graph
`state/proof_obligations.yml` authenticates as:

| SHA-256 | bytes | LF count | terminal LF |
| --- | ---: | ---: | :---: |
| `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 | yes |

It parses with 60 obligations and 60 unique identifiers. At this audit
boundary, `CONV-strict-counting` is `proved_internal`, while
`TARGET-shell-d3` and `POLYA-program-target` are `open`; the proposed
`SHELL-spherical-shell-nontiling` node is not yet present. Thus none of the
review artifacts has silently changed theorem state.

## 3. Independent spectral disposition

The frozen spectral claim uses

\[
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
\]

with multiplicities. Its independently reconstructed unit-shell conclusion
is

\[
N_D(A_{\rho,1},\Lambda)
\leq \frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}
\quad(0<\rho<1,\ \Lambda\geq0).
\tag{3.1}
\]

The outer ratio owners

\[
(0,\rho_*],\qquad(\rho_*,7/8),\qquad[7/8,1)
\]

are disjoint and exhaustive because the lifecycle derives
`0<rho_*<7/8` exactly. The first seam is small-hole-owned and the second is
thin-shell-owned. The middle proof reconstructs all inherited internal faces
and the exact final residual

\[
\mathcal D_{20}
=\{\rho_c\leq\rho<39/50,\ k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

It then uses the disjoint subtraction owners

\[
\mathcal D_{20}\cap\{K\leq200\},\qquad
\mathcal D_{20}\cap\{K>200\},
\]

with `K=200` compact-owned. The finite evidence remains scoped: 10,580
compact leaves own the bounded proxy predicates, 1,286 aggregate boxes own
only base predicates at `K=200`, and the universal `K>=200` conclusion is
analytic. The scoped guard `k_11(rho)>12` is used only for
`rho_c<=rho<1`. This makes `D_21` empty without extrapolating either finite
certificate.

The separate zero-frequency step is indispensable and is present:
positivity of the Dirichlet spectrum gives

\[
N_D(A_{\rho,1},0)=0,
\]

while the right side of (3.1) is also zero. At every positive eigenvalue or
integer phase wall, the strict `<Lambda` convention is retained; no ordinary
floor replaces the strict channel count, and shared angular eigenvalues keep
their full multiplicities.

The normalization is exactly three-dimensional:

\[
L_3=\frac{\omega_3}{(2\pi)^3}
=\frac{4\pi/3}{8\pi^3}=\frac1{6\pi^2},
\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\]

so

\[
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3).
\]

This is the one-term Dirichlet Pólya inequality for all spectral parameters,
not an asymptotic or two-term estimate.

## 4. Arbitrary-radius shell and exact scaling direction

For every `0<r<R`, put `rho=r/R`. Then `rho` lies in exactly `(0,1)` and

\[
A_{r,R}=R A_{\rho,1},\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}).
\]

Because `R^2>0`, strict thresholds are equivalent in the correct direction:

\[
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda).
\tag{4.1}
\]

Applying (3.1) at `R^2 Lambda`, and using `R>0`, gives

\[
\begin{aligned}
N_D(A_{r,R},\Lambda)
&\leq \frac{2}{9\pi}
\left(1-\frac{r^3}{R^3}\right)(R^2\Lambda)^{3/2}\\
&=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}\\
&=L_3|A_{r,R}|\Lambda^{3/2}.
\end{aligned}
\tag{4.2}
\]

Equation (4.1) uses `R^2 Lambda`, not `R^{-2} Lambda`. The argument is
unchanged for `R<1`, `R=1`, or `R>1`, and its `Lambda=0` case is the direct
zero-frequency equality. The excluded geometric endpoints `r=0` and `r=R`
are not added by a limiting argument.

## 5. Independent geometry disposition

The geometry lifecycle concerns

\[
S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad0<r<R.
\]

After scaling by `1/R`, write `alpha=r/R in (0,1)` and
`T=S_{alpha,1}`. Every rigid motion has the form `x -> Qx+a`; radial
invariance gives `Q(T)=T` for rotations, reflections, and
orientation-reversing orthogonal maps. Thus all congruent copies reduce to
translates without narrowing the theorem convention.

The proof derives, rather than assumes, countability and local finiteness.
For a unit vector `e`, set

\[
c=\frac{1+\alpha}{2}e,
\qquad
\delta=\frac{1-\alpha}{2}.
\]

The open ball `B(c,delta)` lies in `T`. Hence every translated shell
contains the correspondingly translated ball, and disjoint shell interiors
force distinct centers to be separated by at least `1-alpha>0`. Only
finitely many separated centers lie in a bounded set; tiles meeting a
compact set have centers in its bounded one-unit enlargement. The family is
therefore locally finite and countable.

Each shell boundary is the union of two spheres and is three-dimensionally
null. Countability makes the union of all tile boundaries null. Consequently
exact or almost-everywhere coverage by closed shells reduces to
almost-everywhere coverage by the open interiors. Exact open-shell coverage
is already a special case.

Fix one outer boundary sphere `Sigma`. At each `p in Sigma`, a
positive-volume exterior neighborhood contains a point of another tile
interior even when the uncovered null set is dense. Local finiteness passes
an approaching sequence to one fixed neighbor. The limit cannot lie in that
neighbor's interior, since a small inward radial point would then lie in both
tile interiors. Thus every `p` lies on a neighboring tile boundary.

Only finitely many neighboring centers can contribute a boundary sphere
meeting `Sigma`. A distinct sphere meets `Sigma` in the empty set, a tangent
point, or a circle, each of zero surface measure on `Sigma`. An outer sphere
identical to `Sigma` forces the same center and hence a forbidden duplicate;
an inner sphere cannot be identical because `alpha<1`. A finite union of the
remaining surface-null intersections cannot cover the positive-area sphere
`Sigma`. This contradiction proves non-tiling.

Scaling back preserves disjoint interiors, exact coverage, and null-set
coverage for every `R>0`. Thus the geometry conclusion covers exactly every
`0<r<R`, including both `R<1` and `R>1`, and all four open/closed,
exact/almost-everywhere conventions. Neither endpoint degeneration is
silently included.

## 6. Exact family match

The notations differ, but the underlying open sets are identical:

\[
A_{r,R}=S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}.
\]

| scope item | spectral lifecycle | geometry lifecycle | match |
| --- | --- | --- | :---: |
| ambient dimension | `R^3` | `R^3` | yes |
| parameter class | every `0<r<R` | every `0<r<R` | yes |
| endpoint degeneracies | excludes `r=0,R` | excludes `r=0,R` | yes |
| scale | every `R>0` via `R^2 Lambda` | every `R>0` via dilation | yes |
| domain | bounded open spherical shell | same open spherical shell | yes |
| conclusion | strict Dirichlet Pólya for all `Lambda>=0` | no congruent tiling under the stated conventions | complementary |

There is no ratio subfamily left unmatched: the spectral outer partition
covers all `0<rho<1`, and the geometry normalization uses exactly
`alpha=r/R in (0,1)`. Therefore the combined program claim is not obtained
by pairing a spectral theorem for one subfamily with non-tiling for another.
It holds for the entire bounded genuine three-dimensional spherical-shell
class.

## 7. Cross-track separation and graph boundary

The spectral lifecycle uses no tiling or non-tiling theorem. The geometry
lifecycle uses only elementary Euclidean geometry, measure, and compactness;
it uses neither the shell spectrum nor the Pólya inequality. Neither track
depends on the other, so their agreement is not circular.

The only correct future graph meeting point is
`POLYA-program-target`. A scoped geometry node
`SHELL-spherical-shell-nontiling` may be created as `proved_internal` only
through the separately audited State Patch. That node must retain the exact
`0<r<R`, rigid-motion, pairwise-disjoint-interior, and
exact/almost-everywhere coverage scope. The future reciprocal edge must be:

- add `SHELL-spherical-shell-nontiling` to
  `POLYA-program-target.dependencies`; and
- add `POLYA-program-target` to the geometry node's `implies` list.

The geometry node must not depend on or imply `TARGET-shell-d3`.
Conversely, `TARGET-shell-d3` must not depend on the geometry node. The two
proved results meet only at the program target, together with the already
fixed strict-counting convention. This audit does not itself create the node,
add the edge, clear blockers, or promote any theorem.

## 8. Literature and novelty boundary

The literature-scope note was rehashed because it is part of the preserved
geometry lifecycle, but none of its search results is a proof premise here.
The spectral proof is authenticated by its mathematical lifecycle; the
non-tiling proof is elementary and independently reconstructed above. The
combined conclusion therefore has no dependence on a claim that a search was
exhaustive or that no paper already contains the result.

The existing program title and statement use `new`. For any future graph
promotion that word must mean only that spherical shells are a newly proved
class **within this program**. It must not be read as `new to mathematics`,
`first known`, `previously unknown`, or a publication-priority claim. The
authenticated literature note itself says it is not a novelty certificate,
so it cannot support any stronger wording.

## Final determination

**PASS. First unsupported implication: none.** The spectral and geometry
lifecycles establish complementary theorems on exactly the same full family
of bounded three-dimensional spherical shells. Strict counting, the
`Lambda=0` face, the three-dimensional Weyl normalization, the
`R^2 Lambda` scaling direction, all exact/almost-everywhere open/closed
tiling conventions, cross-track separation, and the no-novelty boundary are
all preserved. The earlier 299-line metadata statement remains in the
failure chronology and is corrected here to the exact 300-LF identity.
