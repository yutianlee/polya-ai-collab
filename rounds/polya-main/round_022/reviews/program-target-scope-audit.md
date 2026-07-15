# Round 22 Program-Target Scope Audit

Date: 2026-07-15

Role: fresh independent program-scope auditor

## Verdict

**PASS.**

**First unsupported implication:** none.

At the theorem-and-evidence level, the separately reviewed spectral theorem
and the separately reviewed geometric theorem have exactly the same domain
class and jointly satisfy the existing `POLYA-program-target`: every bounded
genuine three-dimensional spherical shell

$$
A_{r,R}=S_{r,R}={x\in\mathbb R^3:r<|x|<R},
\qquad 0<r<R,
$$

satisfies the strict Dirichlet Pólya inequality for every
$\Lambda\geq0$, and no member tiles $\mathbb R^3$ under the frozen
rigid-motion, pairwise-disjoint-interior, exact/almost-everywhere open/closed
coverage convention.

Here `new` is calibrated only as **new to this program's proved class**. This
audit makes no assertion that the class or either theorem is new in the
literature, first, unpublished, or entitled to publication priority.

This report is not a State Patch. The authoritative graph remains unchanged,
the relevant nodes remain open, and the proposed geometry node does not yet
exist. The PASS authorizes a later judge and independently audited patch to
represent conclusions already established by the frozen lifecycles; it does
not itself promote them.

## 1. Authentication and audit boundary

The authoritative graph authenticates as follows:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/proof_obligations.yml` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 |

The canonical validator reports `Graph OK`. Independent parsing gives 60
obligations with 60 unique identifiers. In the authenticated graph:

- `POLYA-program-target` is `open` and currently depends on
  `CONV-strict-counting` and `TARGET-shell-d3`;
- `TARGET-shell-d3` is `open`;
- `CONV-strict-counting` is `proved_internal`;
- no node named `SHELL-spherical-shell-nontiling` exists; and
- the ellipse and certificate-family targets remain open and are not used in
  this audit.

The spectral lifecycle reproduces exactly:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | 6,568 | 244 |
| `rounds/polya-main/round_022/exploration/theorem-claim-freeze.md` | `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d` | 2,157 | 60 |
| `rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md` | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` | 8,228 | 205 |
| `rounds/polya-main/round_022/responses/shell-theorem-incumbent.md` | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` | 6,141 | 290 |
| `rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md` | `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12` | 18,000 | 655 |
| `rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md` | `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56` | 14,726 | 361 |
| `rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md` | `6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458` | 5,514 | 161 |
| `rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md` | `a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9` | 20,124 | 680 |

The geometric lifecycle reproduces exactly:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md` | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` | 4,703 | 105 |
| `rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md` | `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a` | 992 | 30 |
| `rounds/polya-main/round_022/reviews/nontiling-claim-scope-audit.md` | `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7` | 11,679 | 234 |
| `rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md` | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` | 3,199 | 92 |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md` | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` | 7,245 | 241 |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md` | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` | 1,816 | 45 |
| `rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md` | `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53` | 13,290 | 299 |

I did not inspect or rely on a future Round 22 judge or State Patch. No
statement in this report depends on the exploratory literature-scope note;
that note is not part of the authenticated proof set and cannot serve as a
novelty certificate.

## 2. Exact program conjunction

The graph statement is

$$
N_D(\Omega,\Lambda)\leq L_d|\Omega|\Lambda^{d/2}
\qquad(\Lambda\geq0)
$$

for at least one natural non-tiling Euclidean domain class, with Dirichlet
boundary conditions and a fixed counting convention. For the current shell
route, this separates into four obligations:

1. identify one and the same natural Euclidean class in the spectral and
   geometric arguments;
2. prove the exact Dirichlet inequality on every member for every threshold;
3. prove that every member is non-tiling under the stated convention; and
4. avoid converting the internal program word `new` into an external
   literature or priority assertion.

The two frozen lifecycles meet all four obligations. Their conjunction is
not agent consensus: the theorem lifecycle contains isolated reconstruction,
independent provenance replay, cross-comparison, and a fresh adversarial
referee; the geometry lifecycle contains an independent clean-room proof and
a later fresh referee that formed its provisional verdict before reading the
incumbent and clean-room geometry proofs.

## 3. Class identity and naturality

There is no notational or topological mismatch. The spectral theorem uses

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},
$$

while the geometric theorem uses

$$
S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}.
$$

Thus $A_{r,R}=S_{r,R}$ literally, not merely up to closure, measure zero,
or congruence. Both quantify over exactly $0<r<R$. Each member is a bounded,
connected, open Euclidean domain with two smooth spherical boundary
components. The family is defined by the two elementary radii, is invariant
under orthogonal motions, and is closed under positive dilation. These
intrinsic properties supply the program-level descriptive qualification
`natural`; no literature classification is needed.

The spectral Dirichlet Laplacian is taken on the open shell. The geometry
proof first rules out a tiling by those same open shells and then, as a
strictly stronger convention check, also handles coverage formulated using
their closures. The latter calibration does not replace the spectral domain
by a closed set.

The endpoint class is also identical on both tracks:

- $r=0$ is excluded;
- $r=R$ is excluded;
- every $0<r<R$ is included;
- $R$ is automatically positive; and
- both scaling arguments work for $R<1$, $R=1$, and $R>1$.

No limiting ball or degenerate sphere is silently added to the program
class.

## 4. Spectral theorem, strict counting, and all endpoints

The fixed convention is

$$
N_D(\Omega,\Lambda)
=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

with eigenvalues repeated according to multiplicity. The theorem lifecycle
preserves the strict inequality at every spectral and phase wall. At a
threshold eigenvalue, all equal copies are excluded; at a cross-channel
coincidence, the full orthogonal multiplicity enters only above the wall; at
an integer radial phase wall the strict channel count is $m-1$, not the
ordinary floor $m$.

For the unit shell, the proof covers the exact disjoint ratio partition

$$
(0,1)
=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}
[7/8,1).
$$

It proves $0<\rho_*<7/8$ exactly, assigns $\rho=\rho_*$ to the small-hole
theorem and $\rho=7/8$ to the thin-shell theorem, and reconstructs every
internal compact seam, including

$$
\rho_0=1/\sqrt{337},\qquad
\rho_c=1/(1+2\pi),\qquad
39/50,
$$

all moving staircase and high-frequency faces, and the final $K=200$ split.
The compact subtraction owns $K=200$; the aggregate subtraction is open
there. The 10,580 compact leaves are used only on their finite rectangle,
the 1,286 aggregate boxes only for base predicates at $K=200$, and analytic
propagation owns the universal $K\geq200$ conclusion. The exact successor
residual is empty.

At $K=0$, positivity of the Dirichlet spectrum gives directly

$$
N_D(A_{\rho,1},0)=0,
$$

and the cubic right-hand side is also zero. Therefore $\Lambda=0$ is not
inferred by continuity from positive frequency. For every
$0<\rho<1$ and $\Lambda\geq0$, the reviewed unit-shell conclusion is

$$
N_D(A_{\rho,1},\Lambda)
\leq \frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}.
\tag{4.1}
$$

## 5. Weyl normalization and arbitrary-radius scaling

The theorem lifecycle rederives, rather than assumes from a remainder
formula,

$$
L_3=\frac{\omega_3}{(2\pi)^3}
=\frac{4\pi/3}{8\pi^3}
=\frac1{6\pi^2}.
$$

For the unit shell,

$$
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\qquad
L_3|A_{\rho,1}|
=\frac{2}{9\pi}(1-\rho^3).
$$

Thus (4.1) is exactly the one-term three-dimensional Dirichlet Pólya
inequality required by the program target, not a two-term Weyl estimate or a
differently normalized bound.

For arbitrary $0<r<R$, put $\rho=r/R$. Unitary dilation gives

$$
A_{r,R}=R A_{\rho,1},
\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}),
$$

and strict comparison of thresholds gives the correct counting direction

$$
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda).
$$

Together with

$$
|A_{r,R}|=\frac{4\pi}{3}(R^3-r^3),
$$

this yields, for every $0<r<R$ and $\Lambda\geq0$,

$$
\boxed{
N_D(A_{r,R},\Lambda)
\leq\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2}.}
\tag{5.1}
$$

The proof uses only $R>0$, so (5.1) has no hidden restriction to dilations
larger than one.

## 6. Geometric non-tiling and all coverage conventions

For completeness of the program implication, I independently checked the
scope-critical geometry chain authenticated by the lifecycle.

After scaling to $R=1$ with $\alpha=r/R\in(0,1)$, radial invariance turns
every rigid-motion copy, including reflections and orientation-reversing
motions, into a translate $a+S_{\alpha,1}$. An explicit positive-radius
ball contained in each shell gives a positive uniform separation of distinct
centers. Duplicate centers would give identical nonempty interiors and are
forbidden. Uniform separation implies both local finiteness and countability;
neither is assumed from the word `tiling`.

Countability makes the union of all inner and outer spherical boundaries a
three-dimensional null set. Hence exact or almost-everywhere coverage by
closed shells reduces to almost-everywhere coverage by their open interiors.
Exact open-shell coverage is already a special case.

Fix one outer boundary sphere $\Sigma$. For every $p\in\Sigma$, positive-
volume neighborhoods exterior to the chosen tile contain interior-covered
points, even if the null exceptional set is dense. Local finiteness passes a
sequence of such points to one fixed neighboring tile. The limit $p$ lies on
that tile's boundary: if it lay in its interior, a sufficiently small inward
radial point would lie in both tile interiors.

Only finitely many neighboring centers can contribute a boundary sphere at
$\Sigma$. The intersection of $\Sigma$ with any distinct neighboring sphere
is empty, a tangent point, or a circle, and therefore has zero surface
measure on $\Sigma$. No finite union of such intersections covers the
positive-area sphere $\Sigma$. The coincident cases do not escape this
argument: coincident outer spheres force a duplicate center, while an inner
sphere cannot coincide with $\Sigma$ because $0<\alpha<1$.

This contradiction rules out every family of congruent copies having
pairwise-disjoint interiors and exact or almost-everywhere coverage, for
both the open-shell and closed-shell formulations. Scaling back is valid for
every $0<r<R$, including $R<1$. Therefore every domain in (5.1) is
non-tiling under the frozen convention.

## 7. Program semantics and excluded claims

The conjunction of Sections 3--6 supplies one complete natural non-tiling
Euclidean class to the program. The word `new` is used only as a ledger
statement: this is the class newly entering the program's proved set when the
later audited patch is applied. It is not a mathematical inference from a
literature search.

In particular, this PASS does not assert:

- that spherical-shell Pólya or non-tiling results are absent from the
  literature;
- that this is the first known non-tiling Pólya class;
- novelty, publishability, precedence, or priority;
- a theorem for $r=0$, $r=R$, another dimension, or another boundary
  condition;
- the near-circular or full ellipse target; or
- the fallback certificate-family target.

No exploratory literature note, source search, or agent count is needed for
the exact internal program implication.

## 8. Minimal graph relationship

The mathematically minimal new relationship is a conjunction at the program
target:

$$
\texttt{TARGET-shell-d3}
\longrightarrow
\texttt{POLYA-program-target}
\longleftarrow
\texttt{SHELL-spherical-shell-nontiling}.
$$

Accordingly, a later independently audited State Patch should:

1. create `SHELL-spherical-shell-nontiling` with status
   `proved_internal` and with a statement retaining exactly $0<r<R$, all
   congruent rigid motions, pairwise-disjoint interiors, and exact or
   almost-everywhere open/closed coverage;
2. add `SHELL-spherical-shell-nontiling` to
   `POLYA-program-target.dependencies`;
3. add `POLYA-program-target` to the new node's `implies` list; and
4. leave the two proof tracks independent below that conjunction.

There must be no geometry-to-spectral or spectral-to-geometry edge. In
particular:

- the geometry node must neither depend on nor imply `TARGET-shell-d3`;
- `TARGET-shell-d3` must neither depend on nor imply the geometry node; and
- elementary geometry, not the spectral theorem, remains the proof basis of
  non-tiling.

The existing reciprocal relation between `TARGET-shell-d3` and
`POLYA-program-target` is retained. The direct strict-counting dependency of
the program target may also remain. The ellipse and certificate-family nodes
are untouched and contribute nothing to this shell-specific promotion.

Because the current graph still records the compact assembly, uniformity,
spectral target, and program target as open, the later patch must reconcile
their already reviewed logical chain rather than merely relabel the program
node. This report proposes only the minimal cross-track relationship and
does not prescribe or apply the rest of that patch.

## Final determination

**PASS. First unsupported implication: none.** The authenticated spectral
and geometric lifecycles prove, on exactly the same full shell family, the
two conjuncts required by `POLYA-program-target`. With `new` read only as
new to this program and with no novelty or priority inference, the program
target is mathematically satisfied. Graph satisfaction remains pending the
later judge, reciprocal dependency update, theorem-status reconciliation,
and independently audited State Patch.
