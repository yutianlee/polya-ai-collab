# Response to referees

**Manuscript:** *A Dirichlet Pólya Inequality for Three-Dimensional Spherical Shells*  
**Revision date:** 16 July 2026

We thank both referees for their detailed audits.  The revision addresses
every theorem-critical and reproducibility request.  The live proof is now a
purely analytic proof for the three-dimensional spherical-shell class.  It
does not claim the general Pólya conjecture, novelty, priority, or external
acceptance.

## Response to Referee 1

### 1. High-staircase event exhaustion

We replaced the former assertion of event exhaustion by an explicit
order-free theorem in Lemma 4.6 of the main paper.  The revision now:

- proves all five checkpoint inventories by printed first-excluded-mode
  inequalities, including the second-, third-, and higher-radial-channel
  tails;
- defines half-open bands
  \(\mathcal B_m=\{k_{m-1}\leq K<k_m\}\), so every checkpoint has a unique
  owner;
- gives a disjoint and exhaustive 38-row post-event state-to-payment table;
- inserts the full multiplicity of coincident events before assigning the
  resulting state;
- proves every row by one of the displayed global, localized, or bridge
  payment rules; and
- treats the final face \(K=k_{11}\) with the original strict proxy, which
  omits the \((11,1)\) equality channel.

The bridge implication is now displayed explicitly as
\(F_j(r)=W(r,k_j(r))>W(r,c)>C\).  Part III of the supplement prints all 14
localization witnesses, 22 localized payment margins, 12 bridge \(P,Q\)
pairs, and four global checkpoint payments.  An independent exhaustive audit
confirmed 38 disjoint/exhaustive rows (6, 7, 7, 11, and 7 by band), valid caps,
and correct equality/coincidence ownership.

### 2. Bessel sign ledger and exact zero indices

The new Lemma 4.2 states the adjacent-order interlacing relation
\[
 j_{\nu,n}<j_{\nu+1,n}<j_{\nu,n+1}
\]
in the required half-integer cases and cites DLMF equation (10.21.2).  It
derives the two possible successive zero counts and resolves the choice by
the sign parity of the spherical Bessel function.  The resulting table gives
the complete count vector for all eight rational walls, rather than merely a
target sign.

All intermediate tangent/sign certificates are printed in Part I of the
supplement, including the walls \(10\), \(103/10\), \(23/2\), and \(129/10\).
The \(\tan x=x\) existence argument now includes both endpoint signs and the
monotonicity interval.  The Lorch first-zero estimate is cited by its two
published abstract formulas, with the range \(-1<\nu<\infty\), and every
specialization is shown.  The formerly compressed \(\ell=5\) check now
includes
\[
 975^2\,77-8544^2=198189>0.
\]

### 3. Self-contained source package

All ten component TeX sources and their compiled PDFs are now supplied in
`manuscript/analytic`.  The master supplement includes only those ten live
components.  `manuscript/analytic/build.ps1` rebuilds Parts I--X, then the
supplement, then the main paper.  `manuscript/analytic/MANIFEST.md` records
the numerical build order, role, exact logical status, and release hashes.

### 4. Minimal dependency boundary

Section 4.7 of the main paper and the opening page of the supplement now give
the requested dependency table.  Its status column uses only “used in final
proof” and “optional cross-check.”  The historical 611-row census is kept for
traceability, but the live high-event implication is the separate 38-state
theorem.  The retired seam, \(K=200\), aggregate-tail proof, executable
registry, and interval certificates are explicitly outside the theorem's
dependency graph.

### 5. Strict versus non-strict counting

Immediately after Theorem 1.1, the paper now proves
\[
 N_D^{\leq}(\Omega,\Lambda)
 =\lim_{\varepsilon\downarrow0}N_D(\Omega,\Lambda+\varepsilon)
\]
and passes the Weyl bound to the limit.  Thus the wall-sensitive strict
convention yields the standard non-strict Pólya formulation with the same
constant.

### 6. Smaller corrections

- Shell eigenfrequencies are now denoted \(k_{\ell,n}\); \(q_\ell\) is
  reserved for floor samples.
- The relation between the strict \(P_{\rm coarse}\) proxy and the ordinary
  floor sum \(S_{\rho,K}\) is stated at the definition.
- The first \(J_{3/2}\) wall and all tangent comparisons have exact rational
  proofs.
- Imported phase, floor-sum, interlacing, and first-zero results have precise
  theorem/equation locators.
- Every \(\beta_{\ell,n}\) is explicitly distinguished from the actual zero;
  equality at a rational proxy wall is not spectral equality.
- The manuscript is labelled “Anonymous for peer review,” and scope/status
  material is concentrated in the opening status paragraph and the
  reproducibility subsection.

## Response to Referee 2

The revision also implements the second report's requested refinements:

- Lemma 2.8 now states the aggregate weighted-scaffold hypothesis explicitly.
- The optical proof displays its product deficit, radial deficit, angular
  error, and both screen reserves in the main paper.
- The external Lorch source card is closed by the official published
  abstract, including both strict inequalities and their validity range.
- The exact checker replays all 611 historical ledger predicates; the live
  proof remains independent of that executable replay.
- The stale thin-seam reference has been removed from the live Packet E.
- The use of \(17/2\) is identified as a deliberate conservative weakening of
  the sharper \(87/10\) wall.
- The rational enclosure \(333/106<\pi<22/7\) is proved, and each delicate
  payment states which side is used.  In particular, the cap-74 row records
  the exact \(1/\pi>7/22\) reserve.
- The scalar module prints its exact secant and Bernstein margins rather than
  relying on decimal evidence.

## Release verification

The revised package passed the following checks:

| Check | Result |
|---|---|
| exact analytic-ledger replay | 611/611 checks pass (553 core + 58 supplemental) |
| independent high-event audit | 38/38 states exhaustive and paid |
| independent Bessel/Lorch audit | all eight count vectors and all specializations pass |
| high-event derivation replay | 205 critical points, 1,460 fine rows, 58 merged rows; pass |
| strict-staircase test suite | 24/24 tests pass |
| LaTeX release build | Parts I--X, 69-page supplement, and 44-page main paper compile |
| static reference audit | no missing/duplicate labels and no missing/unused citations |
| rendered-page inspection | title, dependency, zero-index, event-table, seam, and final pages pass |

These checks guard against arithmetic and transcription errors.  They are not
premises of the analytic proof and do not substitute for external peer review.
