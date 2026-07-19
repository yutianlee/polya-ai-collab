# Round 22 proof-free geometry packet: spherical shells do not tile

Date: 2026-07-15

Status: **FROZEN GEOMETRY CLAIM / NOT YET GRAPH STATE**

Proposed obligation: `SHELL-spherical-shell-nontiling`.

This packet states only a geometric theorem and its review requirements. It
contains no proof, proves no spectral inequality, and makes no novelty or
publication-priority claim.

## 1. Exact claim and tiling convention

For $0<r<R$, let

$$
S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}.
$$

Prove that no family of congruent copies of $S_{r,R}$ can satisfy both:

1. the interiors of distinct indexed copies are pairwise disjoint; and
2. their union covers $\mathbb R^3$ up to a set of three-dimensional
   Lebesgue measure zero.

This rules out exact coverage as a special case. The conclusion must also
cover the convention in which closed shells cover exactly or almost
everywhere while their interiors are disjoint: the countable union of tile
boundaries must be removed explicitly.

Every rigid motion is allowed, including rotations and reflections. Because
the shell is radial, the proof must reduce every congruent copy to a
translation without restricting the tiling convention.

## 2. Permitted inputs

Only elementary Euclidean geometry, Lebesgue measure, the surface measure of
a sphere, and basic compactness/local-finiteness arguments are permitted.
The spectral theorem, the Pólya inequality, literature searches, and any
classification theorem for tiling domains are forbidden as proof inputs.

The existing Round 21 incumbent route and clean-room reconstruction may be
authenticated and compared by later auditors, but a fresh adversarial
geometry referee must form its verdict independently.

## 3. Required reconstruction

Any proof must establish all of the following.

1. Scale to $R=1$ with $\alpha=r/R\in(0,1)$ and show that scaling preserves
   disjoint interiors and exact or almost-everywhere coverage.
2. Reduce congruent copies of
   $S_{\alpha,1}$ to translates $a+S_{\alpha,1}$.
3. Derive a positive uniform separation of distinct centers from an explicit
   ball contained in each shell. Use it to prove local finiteness and
   countability; do not assume either property from the word "tiling".
4. Show that the union of all tile boundaries is null. Calibrate exact
   closed-shell coverage to almost-everywhere coverage by open interiors.
5. Fix one outer boundary sphere $\Sigma$. For every $p\in\Sigma$, approach
   from outside the chosen tile through points lying in other tile interiors.
   Use local finiteness to pass to one fixed neighboring tile, and prove that
   $p$ lies on its boundary rather than in its interior.
6. Prove that only finitely many neighboring boundary spheres can meet
   $\Sigma$.
7. Prove that the intersection of $\Sigma$ with any distinct sphere is
   empty, a point, or a circle and therefore has zero surface measure on
   $\Sigma$. A finite union cannot cover $\Sigma$.
8. Exclude the identical-sphere cases: an outer sphere identical to
   $\Sigma$ forces a duplicate center and overlapping interiors, while an
   inner sphere cannot be identical because $0<\alpha<1$.
9. Scale the contradiction back to every $0<r<R$.

## 4. Mandatory falsification cases

- an uncountable family of copies;
- infinitely many centers accumulating near the chosen sphere;
- coverage points lying only on tile boundaries;
- almost-everywhere coverage rather than exact coverage;
- an exact tiling formulated with closed copies;
- duplicate indexed copies with the same center;
- rotations, reflections, and orientation-reversing rigid motions;
- a neighboring sphere tangent to the chosen outer sphere;
- a neighboring inner or outer sphere coincident with it;
- the possibility that a limit point lies inside the neighboring shell;
- the excluded degeneracies $r=0$ and $r=R$; and
- scaling with $R<1$ as well as $R>1$.

## 5. Scope and promotion rule

The conclusion is exactly that every bounded genuine three-dimensional
spherical shell $0<r<R$ is non-tiling under the convention above. It does not
assert that the class is the first known non-tiling Pólya class, that the
result is absent from the literature, or that any other domain family is
settled.

Before graph promotion, require:

1. an independent scope audit of this frozen packet;
2. authentication of the Round 21 incumbent and clean-room geometry proof;
3. a fresh adversarial geometry referee instructed to assume the claim false;
4. a program-scope audit pairing the geometric theorem with the separately
   reviewed spectral shell theorem; and
5. an independently audited State Patch that creates a scoped proved
   non-tiling obligation and makes `POLYA-program-target` depend on it.
