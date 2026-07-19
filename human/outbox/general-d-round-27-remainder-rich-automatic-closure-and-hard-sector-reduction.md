# General dimension, Round 27: remainder-rich automatic closure and the exact hard-sector reduction

Date: 19 July 2026  
Status: analytic reduction proved; residual hard-sector sign open

## 0. Scope and theorem boundary

This note returns to the intrinsic trichotomy required by the revised
strategy.  It proves that every high-floor first-drop tuple is automatic
unless its two exact first-shelf endpoint remainders lie in one explicit
remainder-poor sector.  No ratio threshold, new continuous owner, or compact
certificate is introduced.

The result does **not** prove the remaining hard sector, high-floor CST, or
the all-dimensional theorem.  It identifies the first exact residual
inequality and a stronger root-free sufficient target for the next round.

## 1. Definitions and dependencies

Work on the exact high-floor first-drop domain

\[
 f\geq2,\qquad p\geq1,\qquad m=n-p\geq1,
\]

on either extension grid.  Retain the Round 21 notation

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(r+p)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad
 \Delta=e_0-e_p,\qquad
 a_p=\frac{p^2}{3(2r+p)},\qquad
 d=1-\frac{2t}{\pi}.
\]

Ordinary-floor ownership and spatial monotonicity give

\[
 0\leq e_p\leq e_0<1,\qquad
 0\leq\Delta\leq E.
\tag{1.1}
\]

Let \(L_T\) be the complete fractional terminal lower bound in Round 10,
including every inverse fraction, the exact local cap, and the top interval.
Round 10 proves the wall-safe variant

\[
 D_A(r)\geq\Phi_\delta^+,
\tag{1.2}
\]

where

\[
 \boxed{
 \Phi_\delta^+
 =\max\{0,L_T\}
 +a_p\Delta
 +p\left(E-\frac12\right)
 +\frac{dm}{2}.}
\tag{1.3}
\]

The only analytic dependencies are:

1. the proved first-shelf reduction and curvature inequality from
   (S1)--(S3);
2. the strengthened terminal theorem and the
   \(\max\{0,L_T\}\) variant from Round 10;
3. the exact Round 21 elasticity inequality
   \[
    \Delta\geq(s-1)(\lambda+e_p),
    \qquad
    s=\sqrt{1+\frac{p(2r+p)}
      {X(X+2r+2p)}},\quad X=m+\alpha.
   \tag{1.4}
   \]

No Round 23--27 sign conjecture is used.

## 2. Automatic remainder-rich sector

### Proposition 2.1

Define

\[
 E_*=\frac12-\frac{dm}{2p}
     =\frac{p-dm}{2p}.
\tag{2.1}
\]

Every exact high-floor first-drop tuple satisfying either

\[
 p\leq dm
\tag{2.2}
\]

or

\[
 E\geq E_*
\tag{2.3}
\]

has \(D_A(r)\geq0\).  Consequently the only open pointwise sector is

\[
 \boxed{
 p>dm,\qquad
 0\leq E<E_*=\frac{p-dm}{2p}<\frac12.}
\tag{2.4}
\]

### Proof

The first two terms on the right side of (1.3) are nonnegative.  The
remaining shelf/post-drop pair is exactly

\[
 p\left(E-\frac12\right)+\frac{dm}{2}
 =p(E-E_*).
\tag{2.5}
\]

If \(p\leq dm\), then \(E_*\leq0\), and (1.1) gives
\(E\geq0\geq E_*\).  If \(p>dm\), condition (2.3) makes (2.5)
nonnegative.  In either case (1.3) is nonnegative, and (1.2) proves the
claim.  Negating these alternatives gives exactly (2.4). \(\square\)

This is the strategy's remainder-rich case in its sharp algebraic form.
It is stronger than the cruder condition \(E\geq1/2\), and it closes every
tuple with \(p\leq dm\) without using a terminal estimate.

## 3. Exact form of the hard-sector obligation

On (2.4), equation (1.3) becomes

\[
 \boxed{
 \max\{0,L_T\}+a_p\Delta
 \geq p(E_*-E).}
\tag{3.1}
\]

This is the first exact remaining shelf--terminal inequality.  Its two
sides retain the correlations that the failed global intrinsic scalars
discarded:

- the right side is the actual remainder deficit, not \(-p/2\);
- the left side keeps the actual curvature difference \(\Delta\), every
  terminal inverse fraction, the exact cap, and the top interval.

Proving (3.1) on the exact domain (2.4) proves high-floor CST.

There is also a sharper algebraic form of the wall transport.  Put

\[
 g=s-1>0,\qquad
 \tau=\frac{g}{g+2}=\frac{s-1}{s+1}.
\]

Using \(e_p=(E-\Delta)/2\) in (1.4) gives

\[
 \Delta\geq
 g\left(\lambda+\frac{E-\Delta}{2}\right).
\]

Therefore

\[
 \boxed{
 \Delta\geq\tau(E+2\lambda).}
\tag{3.2}
\]

Combining (3.2) with \(\Delta\leq E\) recovers, without loss,

\[
 E\geq(s-1)\lambda.
\tag{3.3}
\]

The curvature member of Round 21 gives independently

\[
 \Delta\geq L_{\rm curv}.
\]

Hence every hard-sector tuple obeys the strict simultaneous restrictions

\[
 \boxed{
 L_0\leq\Delta\leq E<E_*,
 \qquad
 (s-1)\lambda<E_*,
 \qquad
 L_{\rm curv}<E_*.}
\tag{3.4}
\]

These are consequences of the exact poor-remainder hypothesis, not a ratio
partition.

## 4. Stronger root-free target on only the hard sector

Rounds 22--23 give the exact accounting identity

\[
 \mathcal R_J
 =\mathcal C_{\max,8}+\left(\frac18-J\right),
\tag{4.1}
\]

where

\[
 \mathcal C_{\max,8}
 :=\mathcal C_8+(p+a_p)(L_0-L_{\rm curv})
\tag{4.2}
\]

and \(J<1/8\).  They also prove

\[
 \Phi_\delta>\mathcal R_J.
\tag{4.3}
\]

Thus the conditional statement

\[
 \boxed{
 \mathcal C_{\max,8}\geq0
 \quad\hbox{on the exact hard sector (2.4)}}
\tag{4.4}
\]

is a sufficient, but strictly stronger, next target.  It must not be called
equivalent to (3.1), and \(\mathcal C_{\max,8}\) itself does not contain the
cap \(J\).  The cap is retained only through (4.1).

The literal maximum requires two cells:

\[
 L_0=L_{\rm curv}
 \quad\hbox{or}\quad
 L_0=L_{\rm elast}.
\]

On the curvature cell, (4.2) is simply \(\mathcal C_8\).  On the elasticity
cell it restores
\((p+a_p)(L_{\rm elast}-L_{\rm curv})\).  The formulas agree on the switch
wall, but any convexity or stationary-point argument must be reproved on
each side.

## 5. Why the global intrinsic signs failed

The companion Round 27 directed-Arb certificate uses

\[
 (r,p,m,f,\alpha,\mu,t)
 =\left(4036,32,1,2,\frac1{16},
        \frac{65105}{16},\frac{79}{500}\right).
\tag{5.1}
\]

It certifies the complete paired shelves, integer parity, activity, literal
\(B_0=1\) saturated payment cell, and elasticity-owned \(L_0\), together
with

\[
 \mathcal C_{\max,8}<-\frac43,
 \qquad
 \mathcal R_J<-\frac65.
\tag{5.2}
\]

At the same point it certifies

\[
 \mathscr S>47,\qquad
 \Phi_\delta>40.
\tag{5.3}
\]

The compression from \(\Phi_\delta\) to \(\mathcal R_J\) discards more than
14 units of terminal reserve and more than 27 units of shelf reserve.
In particular,

\[
 E=1.001824\ldots,
 \qquad
 E_*=0.485946\ldots,
\]

so (5.1) lies far inside Proposition 2.1 and is not in the hard sector.
The global failure of \(\mathcal R_J\) is therefore a counterexample to the
compressed sufficient sign, not to the remainder-rich branch or to CST.

The Round 26b \(\mathcal C_8\)-negative witness has the same diagnosis:

\[
 E=1.001964\ldots>E_*=0.410905\ldots.
\]

Thus both known negative intrinsic-scalar witnesses are excluded before
the hard-sector estimate begins.

## 6. Equality-face audit

1. **Shelf floor wall.**  The ordinary-floor convention assigns
   \(e_j=0\) at an integer action wall.  Equations (1.1)--(3.4) remain
   non-strict and valid.
2. **Automatic/hard seam.**  Equality \(E=E_*\) is owned by the automatic
   sector.  Equation (2.5) vanishes and the two retained terms in (1.3)
   are nonnegative.
3. **Post-drop seam.**  Equality \(p=dm\) is automatic because \(E_*=0\).
4. **Interface and spatial walls.**  Round 10's strict inverse convention
   and the replacement \(L_T\mapsto\max\{0,L_T\}\) are wall-safe.  No
   continuity assertion is used here.
5. **Elasticity/curvature switch.**  The maximum \(L_0\) is continuous and
   both formulas in (4.2) agree.  Derivatives are not asserted across the
   switch.
6. **Top-payment walls.**  Proposition 2.1 does not use the top payment.
   Any proof of (4.4) must retain its literal one-sided convention.

## 7. Loss ledger

The automatic proof discards only the following nonnegative quantities:

\[
 \max\{0,L_T\},\qquad
 a_p\Delta,\qquad
 p(E-E_*)\ \hbox{when }E\geq E_*.
\]

No shelf remainder is replaced by an independent worst case.

The optional hard-sector target (4.4) is more lossy.  Relative to (3.1), it
still compresses:

1. the actual endpoint pair \((E,\Delta)\) to \(L_0\);
2. the complete fractional terminal reserve to the \(B_0\), top-payment,
   and exact-cap expression.

The Round 27 witness proves these losses cannot be declared harmless outside
(2.4).

## 8. Counterexample search

The companion certified replay proves (5.1)--(5.3) with directed Arb
arithmetic.  A separate diagnostic hard-sector sweep covers both parity
grids, exact shelf/activity tests, inverse-spatial wall sides, structured
small tuples, and mixed log-scale tuples.  It finds no negative
\(\mathscr S\), \(\Phi_\delta\), or hard-sector
\(\mathcal C_{\max,8}\).

The sharp sampled hard-sector value remains

\[
 \mathcal C_{\max,8}\approx0.01286457
\]

near

\[
 (r,p,m,f,\alpha)=(1,3,2,2,1^-),
\]

on the curvature-owned quadratic cell.  This is theorem-design evidence
only.  It supplies no continuum coverage and is not used in the proof of
Proposition 2.1.

## 9. Failure report and next round

The exact residual is (3.1).  The next analytic round should first try the
stronger branchwise target (4.4), now restricted to (2.4), using (3.2)--(3.4)
and the exact paired shelf integrals.  It must treat the curvature and
elasticity cells separately and use all Round 26--27 witnesses as regression
gates.

If (4.4) fails on the hard sector, do not repair it by another scalar ladder.
Return immediately to the exact residual (3.1), then to the exact reduced
scalar \(\mathscr S\) or the strategy-approved weighted aggregate.

The high-floor first-drop theorem and the all-dimensional theorem remain
open.
