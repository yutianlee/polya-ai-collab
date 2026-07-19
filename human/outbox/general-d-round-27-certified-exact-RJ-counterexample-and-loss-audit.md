# General dimension, Round 27: certified exact-RJ counterexample and loss audit

Date: 19 July 2026  
Status: certified counterexample to both \(\mathcal C_{\max,8}\geq0\) and \(\mathcal R_J\geq0\); the exact Round 20 scalars are positive at the witness

## 0. Scope and theorem boundary

Round 26b showed that replacing the exact maximum in \(L_0\) by its
curvature member can change the sign.  The natural repair was

\[
 \mathcal C_{\max,8}
 :=(p+a_p)L_0-\frac p2+\frac{dm}{2}
   +\frac{B_0d}{2c}+\mathcal E(\lambda)-\frac18,
\]

with

\[
 L_0=\max\{L_{\rm el},L_{\rm curv}\}.
\]

The exact-cap scalar then obeys the identity

\[
 \mathcal R_J=\mathcal C_{\max,8}+\left(\frac18-J\right).
\]

This note gives an exact rational point on the complete integer-owner
high-floor first-drop domain for which directed-rounding Arb arithmetic
proves

\[
 \boxed{\mathcal C_{\max,8}<-\frac43},\qquad
 \boxed{\mathcal R_J<-\frac65}.
\]

Thus neither sign is a valid global sufficient target.  This failure is
still fully contained: at the same point Arb reconstructs the earlier
Round 20 quantities and proves

\[
 \boxed{\mathscr S>47},\qquad
 \boxed{\Phi_\delta>40}.
\]

The witness is therefore not a counterexample to \(\Phi_\delta\),
\(\mathscr S\), CST-H, or the general-dimensional Polya theorem.

## 1. Exact tuple and discrete ownership

Take

\[
 \boxed{
 r=4036,\quad p=32,\quad m=1,\quad f=2,\quad
 \alpha=\frac1{16},\quad \mu=\frac{65105}{16},\quad
 t=\frac{79}{500}.}
 \tag{1.1}
\]

Then

\[
 n=p+m=33,\qquad q=r+n=4069,\qquad
 \mu=q+\alpha,
\]

so \(n=\lfloor\mu-r\rfloor\) under the ordinary convention and
\(0\leq\alpha<1\).  This is the integer extension owner, with first owner
dimension \(d_{\rm owner}=4\) and activity constant \(\gamma=3/4\).

Put

\[
 x=r+p=4068,\quad h=f-\frac14=\frac74,\quad
 K=\frac{\mu}{\cos t},
\]

\[
 A_t(z)=G_K(z)-G_\mu(z),\qquad
 W=\frac\mu\pi(\tan t-t).
\]

All data in (1.1) are exact rationals.  Every transcendental comparison
below is made with an Arb interval.

## 2. Complete paired-shelf, activity, and literal-cell certificate

The complete first shelf and exact one-floor drop are certified by

\[
 A_t(x)-h
 =0.0186591114384661\ldots>0,
 \tag{2.1}
\]

\[
 h-A_t(x+1)
 =0.0268300019758468\ldots>0,
 \tag{2.2}
\]

\[
 A_t(x+1)-(h-1)
 =0.973169998024153\ldots>0.
 \tag{2.3}
\]

At the start of the shelf,

\[
 A_t(r)-h=0.983165669219125\ldots>0,
\]

\[
 h+1-A_t(r)=0.0168343307808744\ldots>0.
 \tag{2.4}
\]

Since \(A_t\) is decreasing in its spatial argument, (2.1)--(2.4)
certify floor \(f=2\) at every sample from \(r\) through \(x\), followed
by exactly floor \(f-1=1\) at \(x+1=q\).  No lower floor is skipped, and
all paired-shelf samples lie strictly below \(\mu<K\).

The integer-owner activity margin is

\[
 K^2-\frac{\pi^2}{(1-\cos t)^2}-\frac34
 >1.69\times10^7.
 \tag{2.5}
\]

The terminal interface action is

\[
 W=1.720099239251986\ldots,
\]

so

\[
 1<W+\frac14<2,\qquad B_0=[W+\tfrac14]_< =1.
 \tag{2.6}
\]

Writing \(u=W-1\), one has

\[
 u=0.720099239251986\ldots>\frac1{\sqrt2},
\]

\[
 \lambda=\frac34-u
 =0.0299007607480139\ldots>0.
 \tag{2.7}
\]

Thus this is strictly inside the saturated top-payment cell, with the
literal payment

\[
 \mathcal E(\lambda)=1.
\]

No action, top-payment, interface, activity, or turning equality is used.

## 3. The literal maximum and the two negative scalars

Retain the exact Round 21 definitions

\[
 a_p=\frac{p^2}{3(2r+p)},
\]

\[
 s=\sqrt{1+\frac{p(2r+p)}{X(X+2r+2p)}},
 \qquad X=m+\alpha,
\]

\[
 L_{\rm el}=(s-1)\lambda,\qquad
 L_{\rm curv}=\frac{1-\cos t}{2\pi\mu}p(2r+p).
\]

At (1.1), Arb gives

\[
 L_{\rm el}=0.136566936312753\ldots,
 \tag{3.1}
\]

\[
 L_{\rm curv}=0.126344311950842\ldots.
 \tag{3.2}
\]

Hence the literal maximum is the elasticity branch.  Substitution into
the exact-maximum scalar gives

\[
 \boxed{
 \mathcal C_{\max,8}
 =-1.357650017320433\ldots<-\frac43.}
 \tag{3.3}
\]

The exact local cap is

\[
 J=2I_\mu(q)
 =0.00000367550446259192\ldots.
 \tag{3.4}
\]

Consequently

\[
 \boxed{
 \mathcal R_J
 =\mathcal C_{\max,8}+\frac18-J
 =-1.232653692824895\ldots<-\frac65.}
 \tag{3.5}
\]

The exact maximum and exact cap therefore do not repair this tuple.  The
Round 22 target \(\mathcal R_J\geq0\), not merely its later C8 and F
relaxations, is false globally.

## 4. Reconstruction of the exact Round 20 scalars

To fix the scope, the certificate reconstructs both \(\mathscr S\) and
\(\Phi_\delta\), including the literal terminal inverse fraction.

At \(q\), the terminal endpoint count is one.  In the doubled tail sum,
the strict count is one for \(j=1,\ldots,21\) and zero thereafter.  This
complete finite count is certified from the two adjacent endpoint actions
and monotonicity.  It gives the exact terminal defect

\[
 D_A(q)=27.8281712062501517\ldots.
\]

The first-shelf remainder is

\[
 R_p=18.8613090158389951\ldots.
\]

Therefore

\[
 \boxed{
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
 =47.1391872600721079\ldots>47.}
 \tag{4.1}
\]

For the Round 20 terminal lower bound, the outer and shell counts are both
one.  The unique inverse angle is isolated by

\[
 0.1197675550878<\theta_1<0.1197675550879,
\]

using the strictly increasing equation

\[
 \frac K\pi(\sin\theta-\theta\cos\theta)=\frac34.
\]

Its inverse displacement satisfies

\[
 21<K\cos\theta_1-q<22,
\]

and is enclosed near \(21.8696047259185\).  Thus its strict fractional
part is unambiguous.  With the exact cap and top interval retained, Arb
gives

\[
 L_T=24.2489233336113\ldots.
\]

Let

\[
 e_0=A_t(r)-h,\qquad e_p=A_t(x)-h,\qquad
 \Delta=e_0-e_p.
\]

Using the Round 20 formula

\[
 \Phi_\delta
 =L_T+a_p\Delta+p(e_0+e_p-\tfrac12)+\frac{dm}{2},
\]

the interval replay proves

\[
 \boxed{
 \Phi_\delta=40.7976475182825\ldots>40.}
 \tag{4.2}
\]

Equations (4.1)--(4.2) certify, rather than merely suggest, that the new
counterexample is confined to the later sufficient lower scalars.

## 5. Exact loss diagnosis

The witness is strongly remainder-rich:

\[
 \mathscr E:=e_0+e_p
 =1.001824780657591\ldots.
 \tag{5.1}
\]

The automatic-sector threshold is

\[
 \frac12-\frac{dm}{2p}
 =0.485946655063032\ldots.
 \tag{5.2}
\]

Hence (1.1) is far outside the genuinely hard small-remainder sector.  In
fact,

\[
 p(\mathscr E-\tfrac12)+\frac{dm}{2}
 =16.5081000190258\ldots>16.
 \tag{5.3}
\]

Because \(\max\{0,L_T\}\geq0\) and \(a_p\Delta\geq0\), (5.3) already
makes the max-terminal version of \(\Phi_\delta\) positive without any
use of \(\mathcal R_J\).

The exact loss ledger separates the two compressions in passing from
\(\Phi_\delta\) to \(\mathcal R_J\).  At the witness,

\[
 L_T-\left(\frac{B_0d}{2c}-J+\mathcal E(\lambda)\right)
 =14.3071781053506\ldots>14,
 \tag{5.4}
\]

while

\[
 \begin{aligned}
 &\left[a_p\Delta+p(\mathscr E-\tfrac12)+\frac{dm}{2}\right]\\
 &\quad-
 \left[(p+a_p)L_0-\frac p2+\frac{dm}{2}\right]
 =27.7231231057567\ldots>27.
 \end{aligned}
 \tag{5.5}
\]

Their sum is exactly

\[
 \Phi_\delta-\mathcal R_J
 =42.0303012111074\ldots>42.
 \tag{5.6}
\]

Thus the sign failure is not caused by another cap relaxation or by
choosing the wrong member of \(L_0\).  It is caused by using the wall and
curvature lower bounds as substitutes for the much larger actual shelf and
terminal reserves.  The shelf compression (5.5) is the larger loss, and
the terminal compression (5.4) is also independently sign-relevant.

## 6. The genuinely hard sector: separate diagnostic

There is a clean exact split before any use of \(\mathcal R_J\).  If

\[
 p\leq dm,
\]

then the nonnegative terms in the max-terminal surrogate already close the
shelf contribution.  If \(p>dm\), the same happens whenever

\[
 \mathscr E=e_0+e_p
 \geq\frac12-\frac{dm}{2p}.
 \tag{6.1}
\]

The only residual sector is therefore

\[
 \boxed{
 p>dm,\qquad
 \mathscr E<\frac12-\frac{dm}{2p}.}
 \tag{6.2}
\]

The counterexample (1.1) is excluded by (6.1), with a margin larger than
\(0.51\).

The rigorous proof of this split, its equality-face audit, and the exact
residual obligation are recorded independently in
`human/outbox/general-d-round-27-remainder-rich-automatic-closure-and-hard-sector-reduction.md`.

The frozen non-certified diagnostic
`computations/general_d_round27_exact_phi_hard_sector_diagnostic.py` was run
specifically on (6.2).  Its structured and seeded random replay retained
14,106 feasible hard-sector tuples and evaluated 118,528 exact-domain scalar
records across both owner grids, the literal and right inverse-spatial walls,
and every implemented top-payment cell.  It found no negative
\(\mathscr S\), \(\Phi_\delta\), \(\Phi_+\), \(\mathcal R_J\), or
\(\mathcal C_{\max,8}\).  The smallest sampled
\(\mathcal C_{\max,8}\) was \(0.0128645720672\ldots\) at
\((r,p,m,f,\alpha)=(1,3,2,2,0.999999)\); the curvature branch owns the
maximum there.

This sweep uses ordinary high-precision evaluation and is theorem-design
evidence only.  It provides no continuum coverage and does not prove a sign
on (6.2).  Its source, command, scope, and limitations are recorded in
`human/outbox/general-d-round-27-hard-sector-diagnostic.md`.

## 7. Sharpened analytic subproblem

The failed global target should not simply be replaced by another global
scalar.  The precise next route is:

1. close the automatic sector by \(p\leq dm\) or (6.1), directly in the
   max-terminal form of \(\Phi_\delta\);
2. prove
   \[
    \boxed{\mathcal C_{\max,8}\geq0\quad\text{only on the residual sector
    (6.2)}};
   \]
   this suffices because \(\mathcal R_J>\mathcal C_{\max,8}\) and
   \(\Phi_\delta>\mathcal R_J\);
3. retain the exact endpoint coupling.  The elasticity inequality
   \((\lambda+e_0)/(\lambda+e_p)\geq s\) is equivalently strengthened to
   \[
    \Delta\geq\frac{s-1}{s+1}(\mathscr E+2\lambda),
   \]
   which should be used together with the upper bound on \(\mathscr E\) in
   (6.2), rather than discarded into the coarse global \(L_0\);
4. if the restricted sign still fails, return to the exact
   \(\Phi_\delta\) or \(\mathscr S\) ledger on (6.2).  The
   strategy-approved fallback after that is the weighted aggregate theorem,
   not another ratio ladder.

The general theorem remains open.

## 8. Certified reproduction

The directed-rounding artifact is

`computations/general_d_round27_exact_RJ_counterexample.py`.

Run, for example,

```powershell
$env:GENERAL_D_ROUND27_ARB_PREC='512'
python -B computations/general_d_round27_exact_RJ_counterexample.py
```

The script independently checks the exact interface and parity identities,
the full paired shelves, exact one-floor drop, activity, literal \(B_0\),
saturated top-payment cell, both members of \(L_0\), exact cap, both
negative scalar signs, the complete terminal count, the unique inverse
angle and strict inverse fraction, \(\mathscr S\), \(\Phi_\delta\), the
automatic-sector classification, and the loss identity.  All sign decisions
use directed-rounding Arb arithmetic.
