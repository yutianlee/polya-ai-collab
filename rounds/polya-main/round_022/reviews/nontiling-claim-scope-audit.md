# Round 22 Spherical-Shell Non-Tiling Claim-Scope Audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

The frozen packet states exactly the geometry claim needed for the full family
of bounded three-dimensional spherical shells, with the required tiling
conventions, reconstruction checkpoints, falsification cases, and promotion
boundary. It is consistent in scope with the authenticated Round 21 route,
clean-room proof, typography addendum, and literature-scope note. It neither
proves nor imports the spectral theorem and makes no novelty or
publication-priority claim.

This is an identity, claim-scope, and proposed-dependency audit only. It does
not assess whether any incumbent or future proof establishes the required
steps, and it does not promote an obligation.

## 1. Authentication

The packet reproduces every identity frozen in
`rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md`:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md` | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` | 4,703 | 105 |

The packet is strict UTF-8 without a BOM, uses LF endings with a terminal LF,
and stores `Pólya` with `U+00F3`; it has neither `U+8D38` nor `U+FFFD`.
The freeze itself currently has SHA-256
`c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a`,
992 bytes, and 30 physical lines. Its baseline commit equals current `HEAD`:

`96fc9a1ec25efc45e430ed6e807b509e96cfcf3b`.

The authoritative graph reproduces the frozen SHA-256 exactly:

`a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`.

It parses with 60 unique obligations, and the canonical validator reports
`Graph OK`. There is no current obligation named
`SHELL-spherical-shell-nontiling`. `POLYA-program-target` remains `open` and
currently depends only on `CONV-strict-counting` and `TARGET-shell-d3`;
`TARGET-shell-d3` also remains `open`. Thus the packet and freeze have changed
no graph state or dependency.

The Round 21 comparison inputs reproduce as follows:

| artifact | reproduced SHA-256 |
| --- | --- |
| `rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md` | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md` | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md` | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` |
| `rounds/polya-main/round_021/exploration/literature-scope-note.md` | `31a8bbb71c002daf77690591bd67114e943b3cb869484c517e35036042e52c23` |

The addendum's embedded authentication of the clean-room report agrees with
the reproduced clean-room hash.

## 2. Exact class and tiling conventions

The frozen claim has no domain drift:

- it quantifies over every real pair `0<r<R`, hence automatically `R>0`;
- after dilation by `1/R`, it uses exactly `alpha=r/R in (0,1)`;
- it scales the contradiction back to arbitrary `R`, including `R<1`,
  `R=1`, and `R>1`; and
- it excludes, rather than silently incorporates, the degeneracies `r=0`
  and `r=R`.

The motion and packing conventions are also exact. Every Euclidean rigid
motion is allowed, including rotations, reflections, and all
orientation-reversing orthogonal parts. Radial invariance is required to
reduce each copy to a translate; the packet does not assume a
translation-only tiling at the theorem boundary. Distinct indexed copies must
have pairwise-disjoint interiors, and duplicate copies with the same center
are an explicit falsification case.

The coverage conventions are complete and mutually calibrated:

1. open copies covering up to a three-dimensional Lebesgue-null set are the
   primary convention;
2. exact coverage by open copies is a special case;
3. exact or almost-everywhere coverage by closed shells is also covered when
   their interiors are pairwise disjoint; and
4. the passage from closed shells to open interiors may occur only after
   countability is proved and the countable union of spherical boundaries is
   shown null.

Accordingly, neither boundary-only coverage nor an initially uncountable
family is discarded by definition.

## 3. Required reconstruction scope

The packet requires every scope-critical geometric step visible in the Round
21 clean-room reconstruction:

- dilation must preserve disjoint interiors, exact coverage, and null-set
  coverage;
- an explicit positive-radius ball contained in each normalized shell must
  yield a uniform separation of distinct centers;
- that separation must be used to derive local finiteness and then
  countability, rather than importing either from the word `tiling`;
- countability must precede removal of the full boundary union;
- for every point of one fixed outer sphere, exterior approach points must be
  selected in other tile interiors;
- local finiteness must reduce the approaching sequence to one fixed
  neighboring tile, and the limit point must be shown to lie on its boundary,
  not in its interior;
- only finitely many neighboring inner or outer boundary spheres may be
  available at the chosen outer sphere;
- the intersection with each distinct sphere must be classified as empty, a
  tangent point, or a circle and shown to have zero surface measure on the
  chosen sphere;
- coincident-sphere exceptions must be eliminated separately for neighboring
  outer and inner spheres; and
- the normalized contradiction must be transported back to every `0<r<R`.

This checklist is stated at the correct level for a proof-free packet. The
claim does not treat local finiteness, countability, boundary nullity, or the
finite sphere cover as implicit conventions.

## 4. Mandatory falsification coverage

The packet expressly forces review of all material adversarial cases:

- an uncountable index family and centers accumulating near the chosen
  sphere;
- coverage furnished only by tile boundaries;
- almost-everywhere coverage, exact open-shell coverage, and exact or
  almost-everywhere closed-shell coverage;
- duplicate indexed copies;
- rotations, reflections, and orientation-reversing rigid motions;
- tangent neighboring spheres and coincident neighboring inner or outer
  spheres;
- the possibility that an exterior limit lies inside a neighboring shell;
- both excluded endpoint degeneracies; and
- scaling in both directions, `R<1` and `R>1`.

The tangent case is retained in the zero-surface-measure intersection list,
while the coincident cases are not incorrectly treated as ordinary circle
intersections.

## 5. Scope comparison with Round 21

The Round 21 incumbent route claims the same `0<r<R` family, congruent tiling
notion, pairwise-disjoint interiors, and almost-everywhere coverage. It derives
local finiteness and countability, removes the countable boundary union,
approaches an outer sphere from another tile, obtains a finite boundary-sphere
cover, and excludes coincident inner and outer spheres. Its closing boundary
already says geometry only, with no spectral or priority conclusion.

The Round 22 packet does not broaden that claim. It makes several conventions
that were terse in the incumbent explicit: reflections and
orientation-reversing motions, closed-shell exact and almost-everywhere
coverage, duplicate indexed copies, the explicit contained-ball separation
route, tangent intersections, and scaling for both small and large `R`.

The clean-room report has exactly the same theorem domain and all four
coverage conventions. Its Sections 1--6 supply the same rigid-motion
reduction, separation/local-finiteness/countability chain, boundary removal,
pointwise exterior approach, finite neighboring-sphere set, surface-measure
contradiction, duplicate and coincident-sphere exclusions, and scale-back.
The Round 22 packet faithfully converts those scope-sensitive points into
review requirements without importing the proof as an allowed premise.

The typography addendum changes only the two displayed spellings of `Pólya`
and explicitly preserves every mathematical and scope conclusion. The Round
22 packet uses the intended UTF-8 spelling and preserves its geometry-only,
no-novelty boundary.

Finally, the literature-scope note is exploratory and explicitly not a
novelty certificate. It distinguishes three-dimensional spherical shells
from balls, planar annuli, asymptotic shell remainders, and other non-tiling
classes; it also warns against `new`, `first`, and `previously unknown`
without a full human search. The packet correctly imports none of those
search results as proof and makes no claim of absence from the literature.

There is therefore no claim-class, tiling-convention, or scope contradiction
between the frozen packet and the four Round 21 artifacts.

## 6. Spectral and novelty boundary

The proposed obligation is geometry only. The packet expressly says that it
contains no proof, proves no spectral inequality, and does not use the
spectral shell theorem, the Pólya inequality, a tiling-classification theorem,
or a literature search as a proof input. It does not promote
`TARGET-shell-d3`, `POLYA-program-target`, or any other domain family.

Its conclusion is limited to non-tiling of the full bounded
three-dimensional spherical-shell family under the stated convention. It
does not say that this is the first known non-tiling Pólya class, that the
result is absent from the literature, or that it has publication priority.

## 7. Proposed graph-dependency workflow

The packet's future workflow is directionally and logically correct against
the authenticated graph:

1. this scope audit itself changes no status;
2. the incumbent and clean-room artifacts must be authenticated, and a fresh
   adversarial geometry referee must independently test the geometric claim;
3. a separate program-scope audit must pair a proved geometry obligation with
   the separately reviewed spectral theorem for the same full shell family;
   and
4. only an independently audited State Patch may create the narrowly stated
   `SHELL-spherical-shell-nontiling` node and add it as a direct dependency of
   `POLYA-program-target`.

For graph reciprocity, the eventual patch must record the same edge in both
directions: add `SHELL-spherical-shell-nontiling` to
`POLYA-program-target.dependencies` and add `POLYA-program-target` to the new
node's `implies` list. The geometry node should not depend on or imply
`TARGET-shell-d3`; the two independent results meet only at the program
target. The new node may be created as `proved_internal` only after the
geometry lifecycle passes, and its statement must retain the exact `0<r<R`,
rigid-motion, pairwise-disjoint-interior, and exact/almost-everywhere coverage
scope.

The later program-scope audit and State Patch must also calibrate the existing
word `new` in `POLYA-program-target` as new to this program's proved class,
not as a novelty or publication-priority assertion. Adding the non-tiling
edge alone cannot prove or promote the program target: the spectral target
and all other program gates must independently pass. These are future patch
requirements, not status changes authorized by this packet.

## Final determination

**PASS. First issue: none.** The exact frozen packet bytes pass the independent
Round 22 non-tiling claim-scope gate. This PASS authorizes only the subsequent
geometry authentication, adversarial review, program-scope audit, and
independently audited State-Patch stages named above; it is not a geometry
proof verdict and does not change the authoritative graph.
