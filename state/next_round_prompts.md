# Next Round Prompts

These are the canonical Round 19 instructions. Round 19 works on the exact
post-Round-18 residual \(\mathcal D_{18}\). It must not revert to
\(\mathcal D_{17}\), replace either component by a rectangle, or infer a
uniform staircase from sampled ratios.

## Accepted boundary after Round 18

Retain

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*},
\qquad
\rho_c=\frac1{1+2\pi}.
$$

The complete endpoint and all-ratio high-frequency theorems remain

$$
0<\rho\leq\rho_*,\quad K\geq0,
\qquad
\frac78\leq\rho<1,\quad K\geq0,
$$

and

$$
0<\rho<1,\qquad K\geq295^2=87025.
$$

Set

$$
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
$$

Round 18 proved the closed angular staircase

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_5(\rho).
}
$$

Its genuinely new part was

$$
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)
\right\}.
$$

The proof is analytic. It uses the separated spectrum, strict counting,
fixed-channel shell-to-ball min--max comparison, three audited first-zero
bounds, exact angular multiplicities, and exact Weyl payments. No Round 18
finite-window certificate was promoted.

The Lorch source dependency is qualified and narrow. It supplies only

$$
j_{5/2,1}>\frac{51}{10},
\qquad
j_{7/2,1}>\frac{13}{2},
\qquad
j_{9/2,1}>\frac{15}{2},
$$

together with the audited first-positive-zero convention and parameter
scope. The spherical-Bessel identity comes from DLMF. Shell-to-ball
comparison, shell cross-product zeros, higher radial exclusions,
multiplicities, and Weyl payments are internal steps. Round 19 may not
extrapolate the Lorch card to new orders. Any new external theorem requires
its own completed source card before it becomes a proof dependency.

## Exact current residual

For \(\rho_*<\rho<7/8\), retain

$$
U(\rho)=
\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\geq\frac56\right\}
\right),
$$

where

$$
H_0(\rho)=\frac{C_*}{\omega_0-\rho}
\quad(\rho<\omega_0).
$$

Equivalently,

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\leq\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\leq\rho<7/8,
\end{cases}
$$

with \(H_0(\rho_{HK})=K_0(\rho_{HK})\).

After the Round 18 promotion, exact subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)
\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
$$

Every displayed frequency inequality in \(\mathcal D_{18}\) is strict.
The lower face \(K=1/(2\rho)\), the staircase face \(K=k_5(\rho)\), the
upper face \(K=U(\rho)\), and the complete endpoint faces
\(\rho=\rho_*\) and \(\rho=7/8\) already have analytic owners. At
\(\rho=\rho_c\), the residual uses the second formula and begins strictly
above \(k_5(\rho_c)\).

The residual is nonempty. The accepted exact audit places
\((\rho,K)=(1/2,30)\) in its high-ratio component. Consequently
SHELL-rho-compact, SHELL-rho-uniformity, TARGET-shell-d3, and the program
target remain open.

The certified boxes \(B_0\) and \(B_1\) remain valid independent regression
artifacts, but both lie inside the older analytic region
\(\mathcal C_{17}\). They are not subtracted again.

## Method boundary for Round 19

The high-ratio lead route is a **combined radial-entry/angular staircase**
strictly above \(k_5\). It must account simultaneously for at least:

- the possible first \(\ell=5\) entry immediately above \(k_5\), with its
  full multiplicity;
- the exact second radial \(\ell=0\) wall \(K=2z_\rho\);
- the next crude angular wall \(K=k_6(\rho)\);
- the ordering, equality, and one-sided traces of \(2z_\rho\) and
  \(k_6(\rho)\) on every ratio interval claimed;
- every later radial or angular entry needed by the proposed domain.

The accepted Round 18 audit proves only the local ordering

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
$$

It does not grant a global ordering or a Round 19 crossing threshold.
Any ratio split, crossing point, root enclosure, or new spectral entry
threshold used in Round 19 must be stated exactly and proved on its full
domain before it enters a candidate claim.

In particular, no worker may carry the one-radial-mode count above
\(2z_\rho\), or continue a crude angular cap through \(k_6(\rho)\), without
adding the newly admissible channels with their true multiplicities and
showing that the Weyl term pays the resulting count. This is the mandatory
radial-entry wall, not evidence against Pólya.

The lower-ratio component

$$
\rho_*<\rho<\rho_c,
\qquad
\frac1{2\rho}<K<U(\rho)
$$

remains unchanged from earlier rounds and must be treated as a separate
proof problem. The Round 18 staircase cannot be extended into this component
by notation or continuity. A common lemma may be used only after its exact
domain is independently proved to cover both pieces.

## Round 19 objectives

The primary objective is exact analytic closure of all of
\(\mathcal D_{18}\). The lead high-ratio route is the combined staircase
above. A separate lower-ratio route is mandatory.

If full closure is not achieved, promote only a rigorously proved analytic
domain contained in \(\mathcal D_{18}\), with exact face ownership and an
exactly recomputed strict residual. Do not announce or freeze a numerical
threshold merely because exploration suggests it.

The secondary objective is optional: at most one predeclared,
face-connected certified subset proved genuinely inside
\(\mathcal D_{18}\). It is local evidence and cannot substitute for the
analytic program.

## For A1: exact-mask architect and lead synthesis

Before A2, A3, or certification work begins, freeze and hash a Round 19
residual packet. It must be derived from the post-Round-18 obligation graph
and authenticated Round 18 classifier, not rewritten from memory. It must
contain:

1. the exact definitions of \(\mathcal A_{18}\), \(\mathcal C_{18}\),
   \(\mathcal D_{18}\), and the theorem-wise uncovered set;
2. an exact machine-checkable membership predicate for
   \(\mathcal D_{18}\);
3. the two-piece residual formula with every strict and closed side;
4. the complete piecewise \(U(\rho)\) formula and all inherited ratio
   interfaces;
5. the accepted owner of every lower, upper, vertical, radial, angular,
   and staircase face;
6. an exact regression check that \(B_0\) and \(B_1\) are already absorbed
   and are not subtracted again;
7. the known \(k_5\), \(2z_\rho\), and \(k_6\) method boundary, carefully
   separating proved facts from Round 19 questions;
8. a manifest of SHA-256 hashes recorded before any Round 19 proof is
   released.

Inventory the lower-ratio and high-ratio components separately. For the
high-ratio component, record the walls \(k_5\), \(2z_\rho\), \(k_6\), and
\(U\) without assuming their global ordering. For the lower-ratio
component, retain \(1/(2\rho)\) as the true lower wall.

After A2 identifies a candidate, A1 must freeze a separate **proof-free
claim packet** before A3 or A4 sees the incumbent proof. The packet may
contain only:

- the exact candidate theorem and genuinely new set;
- permitted accepted dependencies and source cards;
- exact constants and parameter domains;
- strict-count and multiplicity conventions;
- every face assignment;
- falsification cases;
- the exact claimed post-candidate residual.

Do not include A2 prose, derivations, ledgers, plots, or conclusions in
A3's initial packet. A1 remains responsible for final implication synthesis,
exact subtraction, and the one-time State Patch.

## For A2: incumbent analytic developer

Start only from the frozen \(\mathcal D_{18}\) packet. On the high-ratio
component, develop a combined radial-entry/angular staircase rather than a
one-radial continuation. At minimum:

1. derive every new spectral entry bound rather than naming an expected
   threshold;
2. order \(2z_\rho\), \(k_6(\rho)\), and every new wall on each exact ratio
   cell used;
3. include the \(\ell=5,n=1\), \(\ell=0,n=2\), and all subsequently
   admissible channels with multiplicity \(2\ell+1\);
4. handle accidental cross-channel coincidences and equality at every
   spectral wall using strict counting;
5. prove that the Weyl payment covers the exact cumulative count on each
   cell;
6. prove every monotonicity, radical, denominator, squaring, and endpoint
   condition on the whole claimed domain;
7. prove that the candidate is contained in \(\mathcal D_{18}\) and lies
   strictly below \(U(\rho)\);
8. provide an executable exact ledger for finite algebra while listing the
   analytic hypotheses that the ledger does not prove.

Develop the lower-ratio component as a separate lemma or explicitly report
the first obstruction. Its lower wall is \(1/(2\rho)\). No result proved
only for \(\rho\geq\rho_c\) may be imported there.

If a new ball-zero, Sturm comparison, Hardy--Poincaré, Prüfer, or special
function theorem is needed, either prove it internally or complete a
source audit with exact hypotheses. The qualified Lorch obligation does not
authorize new Bessel orders.

Return the strongest exact candidate actually proved, its exact subtraction
from \(\mathcal D_{18}\), and the first unsupported implication if complete
closure fails.

## For A3: strictly isolated clean-room reconstruction

Receive only the frozen Round 19 residual packet, the proof-free candidate
claim, and the explicitly permitted accepted dependency packets. Before
the initial verdict, do not inspect A2's proof, ledgers, exploratory
notebooks, plots, cross-comparison, A4 audit, certification work, or judge
draft.

Reconstruct the implication independently and attempt to falsify it at:

- \(\rho=\rho_*,\rho_c,1/2,5/6,7/8\), every inherited \(U\)-interface,
  every proposed ratio split, and every one-sided trace;
- \(K=1/(2\rho)\), \(K=k_5(\rho)\), \(K=2z_\rho\),
  \(K=k_6(\rho)\), every proposed entry or payment wall, and
  \(K=U(\rho)\);
- both possible orderings and any claimed equality of \(2z_\rho\) and
  \(k_6(\rho)\);
- the first two radial indices and all angular orders that can enter on the
  claimed domain, with exact multiplicities;
- strict equality and accidental cross-order coincidence at every spectral
  threshold;
- every extremal substitution used to uniformize a constant;
- empty cells, reversed intervals, improper traces, inverse endpoints,
  dropped nonnegative terms, and unproved denominator signs;
- exact candidate containment in \(\mathcal D_{18}\) and exact residual
  subtraction.

Return PASS or FAIL and name the first unsupported implication. A matching
conclusion without a complete independent proof is not a PASS.

## For A4: independent exact audit and optional bounded certificate

After the proof-free candidate freeze, independently reproduce every finite
constant, wall comparison, ratio split, monotonicity reduction, Weyl
payment, and set inclusion. Use an implementation independent of A2's
ledger. Authenticate all input and output hashes and list every analytic
hypothesis not proved by execution.

A4's exact audit validates only the executed finite algebra. It does not
prove a spectral lemma, replace A3, or satisfy the fresh-referee gate.

Only after the exact \(\mathcal D_{18}\) mask is frozen, A4 may open at most
one optional certified subset. It must:

1. be predeclared before determinant or interval results are inspected;
2. be one connected manifest whose multiple cells, if any, meet along
   complete shared faces fixed in advance;
3. be proved by exact arithmetic to lie genuinely inside
   \(\mathcal D_{18}\), with positive margins to all open faces;
4. use exact outer endpoints and explicit boundary ownership;
5. use outward-rounded interval or ball arithmetic for every required root;
6. uniformly exclude every uncounted radial and angular channel;
7. check the strict Weyl inequality at its true worst point;
8. pass an independent implementation and tamper checks;
9. preserve a reproducible dependency lock, precision policy, transcript,
   artifact manifest, and test suite.

No adaptive second region, disconnected tile, or post-result expansion is
allowed. One certificate remains local evidence and does not promote
COMP-certified-bessel beyond diagnostic_only.

## Cross-comparison and fresh referee

Only after A3 and A4 have returned their independent initial verdicts may A1
compare them with A2. Resolve every discrepancy explicitly and update the
candidate only by issuing a new proof-free freeze and repeating affected
independent gates.

Then commission a fresh referee who participated in neither the incumbent
proof nor the clean-room reconstruction. The referee must assume the claim
false, reconstruct every displayed identity and inequality direction,
audit source scope and face ownership, and identify the first unsupported
implication. Promotion requires a fresh-referee PASS.

## Mandatory promotion gates

Promote a Round 19 analytic result only if:

1. the exact \(\mathcal D_{18}\) packet and classifier were frozen and
   hashed before proof work;
2. the candidate was frozen proof-free before A3 and A4 inspected the
   incumbent;
3. A2 proved the claimed radial/angular staircase and did not cross
   \(2z_\rho\) or \(k_6(\rho)\) with a stale cap;
4. the lower-ratio component was handled separately or left explicitly in
   the residual;
5. A3 completed a strictly isolated reconstruction;
6. A4 independently reproduced the finite constants and exact set
   arithmetic without analytic overclaim;
7. a fresh adversarial referee found no unsupported implication;
8. exact subtraction produced the surviving residual with every face
   assigned;
9. every external dependency had a complete, scope-correct source card;
10. the graph remained acyclic, all evidence paths and hashes resolved, and
    the judge's State Patch validated and was applied exactly once.

If the residual becomes empty, do not close TARGET-shell-d3 immediately.
A separate fresh theorem-level clean-room proof and theorem-level
adversarial audit must first pass.

## Explicit do-not-claim rules

- Do not call the shell theorem proved while
  \(\mathcal D_{18}\neq\varnothing\).
- Do not replace \(\mathcal D_{18}\) by \(\mathcal D_{17}\), a rectangle,
  a coarse envelope, or a sampled grid.
- Do not subtract \(B_0\) or \(B_1\) again.
- Do not continue a one-radial-mode cap above \(2z_\rho\).
- Do not assume a global ordering or crossing threshold for
  \(2z_\rho\) and \(k_6(\rho)\).
- Do not extend the Round 18 staircase below \(\rho_c\) without a new proof.
- Do not extrapolate the qualified Lorch source to unaudited Bessel orders
  or shell cross-product claims.
- Do not infer an analytic spectral inequality from a finite ledger,
  interval roots on one subset, sampled numerics, or agent agreement.
- Do not call one certified subset a curved band, residual component, or
  theorem closure.
- Do not promote COMP-certified-bessel beyond diagnostic_only in the
  optional bounded pilot.
- Do not close SHELL-rho-compact, SHELL-rho-uniformity, TARGET-shell-d3,
  or POLYA-program-target before exact residual closure and the required
  theorem-level audits.
