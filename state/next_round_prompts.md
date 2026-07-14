# Next Round Prompts

These are the canonical Round 18 instructions. The round is an exact
next-angular-staircase round. Its object is the surviving nonrectangular set
$\mathcal D_{17}$, not the old residual $\mathcal D_{16}$, not a rectangular
frequency window, and not a grid of sampled shell ratios.

## Accepted boundary after Round 17

Retain

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The complete small-hole and thin-shell endpoint theorems remain

$$
0<\rho\le\rho_*,\quad K\ge0,
\qquad\text{and}\qquad
\frac78\le\rho<1,\quad K\ge0.
$$

The all-ratio high-frequency theorem also remains

$$
0<\rho<1,\qquad K\ge295^2=87025.
$$

None of these statements is the full all-frequency shell theorem.

Set

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
$$

Round 17 proved the closed first-angular-band theorem

$$
\overline{\mathcal C}_{17}
=\left\{(\rho,K):
\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_2(\rho)
\right\}.
$$

Its genuinely new part in the old analytic residual was

$$
\mathcal C_{17}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad z_\rho<K\le k_2(\rho)
\right\}.
$$

The proof uses strict spectral counting, exact multiplicities, and the
separated radial lower bound. It is analytic. Neither the Round 8 nor the
Round 17 determinant certificate is an input to that theorem.

## Exact current residual

For $\rho_*<\rho<7/8$, retain the exact upper covered floor

$$
U(\rho)=
\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right),
$$

where

$$
H_0(\rho)=\frac{C_*}{\omega_0-\rho}
\quad(\rho<\omega_0)
$$

and $K_0(\rho)$ is the accepted fixed-ratio threshold from the frozen
Round 17 mask. Equivalently,

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\le\rho<7/8,
\end{cases}
$$

with the exact implicit switch $H_0(\rho_{HK})=K_0(\rho_{HK})$.

After adding $\overline{\mathcal C}_{17}$ to the accepted analytic cover,
the exact analytic residual is

$$
\boxed{
\begin{aligned}
\mathcal D_{17}
={}&\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)
\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
$$

Every displayed frequency inequality in $\mathcal D_{17}$ is strict. The
faces $K=1/(2\rho)$, $K=k_2(\rho)$, and $K=U(\rho)$ already have analytic
owners. The complete vertical faces $\rho=\rho_*$ and $\rho=7/8$ also have
old analytic owners. At $\rho=\rho_c$, the residual starts strictly above
$k_2(\rho_c)$; do not continue the lower formula through this face.

The retained certified boxes are

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right],
$$

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

Both certificates remain valid, but exact set arithmetic gives

$$
B_0\subset\mathcal C_{17},
\qquad
B_1\subset\mathcal C_{17}.
$$

They are therefore analytically redundant regression evidence. They are not
subtracted a second time, and the theorem-wise uncovered set is exactly

$$
\boxed{\mathcal U_{17}=\mathcal D_{17}.}
$$

## The obstruction that fixes the Round 18 method

Let

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

On the Round 17 ratio band, below and through $K=k_2(\rho)$, the proof pays
for at most the $\ell=0$ and $\ell=1$ first modes, with multiplicity cap
$1+3=4$.
Immediately above that face, the crude min--max bound must allow the first
$\ell=2$ mode and raises the cap to

$$
1+3+5=9.
$$

However, the exact Round 17 audit proves

$$
\mathcal W\bigl(\rho_c,k_2(\rho_c)\bigr)<9.
$$

Thus a uniform continuation obtained only by replacing the cap $4$ by the
cap $9$ cannot work. This is a method obstruction, not a counterexample to
Pólya. Round 18 must obtain a sharper ratio-dependent $\ell=2$ entry
threshold, a sharper count/payment staircase, or a different analytic
compression. No worker may cite the failed cap as evidence that the theorem
is false.

## Round 18 objective

The primary objective is exact analytic closure of all of
$\mathcal D_{17}$. The lead route is a next-angular-staircase argument that
goes beyond the crude cap $9$. If full closure is not reached, the round may
promote only a fully proved analytic domain whose exact subtraction leaves a
strictly smaller, explicitly stated residual with every face assigned.

The secondary objective is at most one predeclared, face-connected certified
subset lying genuinely inside $\mathcal D_{17}$. It is local evidence only
and is subordinate to the analytic route.

## For A1: exact-mask architect and lead synthesis

Before A2 or A3 begins proof work, freeze and hash a Round 18 residual packet.
It must authenticate the accepted Round 17 State Patch and contain:

1. the exact definitions of $\overline{\mathcal C}_{17}$,
   $\mathcal C_{17}$, $\mathcal A_{17}$, $\mathcal D_{17}$, and
   $\mathcal U_{17}$;
2. a machine-checkable exact membership predicate for $\mathcal A_{17}$ and
   $\mathcal D_{17}$, derived from the obligation graph and the frozen
   Round 17 predicate rather than rewritten from memory;
3. the two-piece formula for $\mathcal D_{17}$, including all strict sides
   and the special $\rho=\rho_c$ assignment;
4. the complete piecewise formula for $U(\rho)$ and the exact interfaces
   $\rho_*,\rho_{HK},\omega_0,\rho_c,1/2,5/6,7/8$;
5. the accepted owner of every lower, upper, vertical, spectral, and
   staircase face, especially $K=k_2(\rho)$;
6. exact proofs that $B_0,B_1\subset\mathcal C_{17}$ and hence
   $\mathcal U_{17}=\mathcal D_{17}$, while retaining both certificates as
   independent regression artifacts;
7. the exact crude-cap-$9$ obstruction and a statement of what it does and
   does not rule out;
8. a manifest with SHA-256 hashes recorded before the proof-free Round 18
   candidate claim is released.

Inventory the two displayed ratio pieces and their exact cells. For each
cell, record its open and closed faces, neighboring accepted theorem,
available spectral thresholds, and candidate staircase mechanism. Do not
infer set membership or connectivity from a plot.

After A2 selects a candidate, freeze a separate proof-free claim containing
only the exact statement, permitted dependencies, parameter domain,
constants, strict-count convention, and falsification cases. A1 must keep
the incumbent proof out of A3's initial packet. One lead author must perform
the final implication and set-subtraction synthesis; agent agreement is not
verification.

## For A2: next-angular-staircase proof developer

Start from the frozen $\mathcal D_{17}$ predicate. The preferred route is to
replace the failed uniform cap $9$ by an exact spectral staircase. A useful
candidate architecture, which must be derived rather than assumed, is:

1. prove a ratio-dependent lower entry threshold $q_2(\rho)$ for
   $\lambda_{2,1}^{1/2}$ that is strictly sharper where necessary than
   $\sqrt{z_\rho^2+6}$;
2. keep the cap $4$ through the exact $q_2$ face using strict counting;
3. compare the first point where an $\ell=2$ state can enter with the first
   point where $\mathcal W(\rho,K)$ can pay $9$;
4. continue through later angular or radial entries only with separately
   proved thresholds and their true multiplicities.

Possible tools include a sharp min--max comparison for the nonconstant
centrifugal potential, a ground-state transform, exact one-dimensional
Sturm comparison, a ratio-dependent Hardy--Poincaré or Prüfer estimate, or a
weighted count that avoids paying all five $\ell=2$ states too early. None
of these is a granted lemma. In particular, a claimed positive correction

$$
\lambda_{2,1}\ge z_\rho^2+6+\delta_2(\rho)
$$

must include an explicit $\delta_2$, its sign proof, its full domain, and all
endpoint and denominator checks.

Treat the two pieces of $\mathcal D_{17}$ separately until a common proof is
actually established. On $\rho_*<\rho<\rho_c$, the lower wall is
$1/(2\rho)$, not $z_\rho$ or $k_2(\rho)$. Do not import the Round 17 band
outside its proved ratio domain.

For every proposed lemma:

1. state an exact closed theorem domain and its genuinely new closed or
   half-open part, and prove that the new part is contained in
   $\mathcal D_{17}$;
2. list only accepted dependencies and derive every new spectral bound;
3. account for every radial index, angular order, multiplicity $2\ell+1$,
   accidental cross-order coincidence, and strict eigenvalue face;
4. prove all monotonicity, inverse, radicand, squaring, and denominator
   conditions on the complete domain;
5. give exact constants and an executable rational or symbolic ledger for
   finite algebra, while keeping analytic hypotheses outside that ledger;
6. assign the faces $\rho=\rho_c$, $K=k_2(\rho)$, every new threshold, and
   every meeting point with $U(\rho)$;
7. compute the surviving residual by exact set subtraction, not sampling;
8. name the first unsupported implication or method obstruction if closure
   fails.

Numerical root exploration may help choose $q_2$ or a ratio split, but
sampled roots, plots, floating-point margins, and finite symbolic ledgers do
not prove the analytic staircase.

## For A3: strictly isolated clean-room reconstruction

Receive only the frozen Round 18 residual packet, the proof-free candidate
claim, and the explicitly permitted accepted dependency packets. Before an
initial verdict, do not inspect A2's proof, notebooks, ledgers, plots,
cross-review, certification work, or judge draft.

Reconstruct the full implication independently and attempt to falsify it at:

- $\rho=\rho_*,\rho_{HK},\omega_0,\rho_c,1/2,5/6,7/8$ and every
  relevant one-sided trace;
- $K=1/(2\rho)$, $K=z_\rho$, $K=k_2(\rho)$,
  $K=\sqrt{z_\rho^2+12}$, $K=2z_\rho$, every proposed $q_2(\rho)$ or
  Weyl-payment threshold, and $K=U(\rho)$;
- the first two radial indices and at least $\ell=0,1,2,3$, with
  multiplicities $1,3,5,7$;
- strict equality at every spectral threshold and every possible
  cross-order eigenvalue coincidence;
- both sides of any ratio split introduced to repair the cap-$9$
  obstruction;
- every extremal substitution used to make a constant uniform;
- empty bands, degenerate intervals, improper traces, inverse endpoints,
  and dropped nonnegative terms;
- the exact claim that the candidate lies in $\mathcal D_{17}$ and the
  exact post-candidate residual formula.

Return `PASS` or `FAIL` and name the first unsupported implication before
cross-comparison. A matching conclusion is insufficient without a complete
independent proof on the exact domain.

After A2 and A3 are compared, commission a fresh adversarial referee that
participated in neither proof. Promotion requires that referee to assume the
candidate false, reconstruct every displayed identity and inequality
direction, and find no unsupported implication.

## For A4: exact audit and one bounded certification pilot

A4's mandatory task is an independent exact audit of the frozen analytic
candidate. Reproduce every finite constant identity, spectral threshold
comparison, endpoint substitution, monotonicity reduction, and set
inclusion in an implementation independent of A2's ledger. Authenticate all
input and output hashes. List every analytic hypothesis the executable audit
does not prove. A PASS validates only the executed finite algebra; it does
not prove the spectral lemma, replace A3, or satisfy the fresh-referee gate.

After the Round 18 mask and candidate are frozen, A4 may attempt at most one
predeclared closed certified subset $B_2$ with all of the following:

1. exact arithmetic proves $B_2\subset\mathcal D_{17}$, with strict
   positive margins to every open residual face;
2. $B_2$ is one connected manifest; if it has more than one cell, its
   cell-adjacency graph is frozen in advance and every adjacency is a
   complete shared face;
3. no adaptive subdivision, parameter sweep, second box, or disconnected
   tile is opened after seeing determinant results;
4. every outer endpoint is exact, preferably rational, and every boundary
   assignment is explicit;
5. outward-rounded interval or ball arithmetic isolates every determinant
   root needed for the strict count;
6. an exact Poincaré--Sturm or stronger analytic bound excludes every
   uncounted radial and angular mode uniformly;
7. the strict Weyl comparison is checked at its true worst point with a
   rigorous positive margin;
8. an independent implementation reconstructs determinant signs,
   truncation errors, root counts, exclusions, and target margin;
9. source, dependency lock, precision policy, transcript, artifacts, and
   tests are reproducible.

Because $B_0$ and $B_1$ lie inside the analytic set
$\mathcal C_{17}$, they are regression anchors rather than uncovered
starting boxes. Do not call $B_2$ an extension of either box unless exact
arithmetic proves the claimed complete shared face and all of $B_2$ still
lies in $\mathcal D_{17}$. A negative feasibility result is acceptable; do
not open another region.

One certificate remains local evidence. It does not add a branch to the
analytic cover, prove a curved band, close a residual component, or move
`COMP-certified-bessel` beyond `diagnostic_only`.

## Mandatory promotion gates

Promote a Round 18 analytic result only if all of the following pass:

1. the exact $\mathcal D_{17}$ packet and classifier are frozen and hashed
   before proof work;
2. the candidate claim is frozen proof-free, its genuinely new part is
   proved to lie in $\mathcal D_{17}$, and every shared or removed face is
   assigned;
3. A2 supplies a complete analytic proof that resolves, rather than ignores,
   the crude-cap-$9$ obstruction on its claimed domain;
4. A3 completes a strictly isolated reconstruction before seeing A2's
   proof;
5. A4 independently reproduces the finite constants and exact set
   arithmetic while making no analytic overclaim;
6. a fresh adversarial referee finds no unsupported implication;
7. the surviving residual is recomputed by exact subtraction and is not
   replaced by a rectangle or sampled approximation;
8. the obligation graph remains acyclic, all evidence paths and hashes
   resolve, and the accepted endpoint and Round 17 theorems remain
   unchanged;
9. the judge applies one validated State Patch exactly once;
10. if the residual becomes empty, a separate fresh theorem-level clean-room
    proof and adversarial audit pass before `TARGET-shell-d3` is closed.

A4's optional certificate may be recorded only after all certification
gates pass. It cannot promote an analytic obligation or alter the analytic
residual.

## Explicit do-not-claim rules

- Do not call the full shell theorem proved while
  $\mathcal D_{17}\ne\varnothing$.
- Do not replace $\mathcal D_{17}$ by $\mathcal D_{16}$, a rectangle, a
  coarse band union, or a grid.
- Do not subtract $B_0$ or $B_1$ again; both are already analytically
  subsumed by $\mathcal C_{17}$.
- Do not extend the Round 17 band above $k_2$ using only the crude cap $9$.
- Do not treat the cap-$9$ obstruction as a counterexample to Pólya.
- Do not infer an analytic spectral inequality from a finite ledger,
  interval roots on one box, sampled numerics, or agent consensus.
- Do not call one certified subset a curve, band, component, or residual
  cover.
- Do not promote `COMP-certified-bessel` beyond `diagnostic_only` in this
  bounded pilot.
- Do not close `SHELL-rho-compact`, `SHELL-rho-uniformity`, or
  `TARGET-shell-d3` before exact residual closure and the required final
  theorem-level audits.
