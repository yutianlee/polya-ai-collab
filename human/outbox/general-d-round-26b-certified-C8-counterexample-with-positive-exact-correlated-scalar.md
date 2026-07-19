# General dimension, Round 26b: certified C8 counterexample with positive exact correlated scalar

Date: 19 July 2026  
Status: certified counterexample to \(\mathcal C_8\geq0\); \(\mathcal R_J\) and \(\Phi_\delta\) remain positive at the witness

## 0. Scope and theorem boundary

Round 23 proved

\[
 \mathcal R_J>\mathcal C _8
\]

and proposed \(\mathcal C_8\geq0\) as a sufficient high-floor target. This
note gives an exact feasible half-integer-owner tuple with

\[
 \boxed{\mathcal C _8<-7.}
\]

It also certifies a nearby unique interior stationary point with the same
negative sign. Thus the C8 sign target is false on the exact domain, not
only on a relaxed projection.

The failure is nevertheless fully contained. At the same point, the exact
maximum in \(L_0\) is the elasticity branch, not the curvature branch used
by C8, and the exact cap is far below \(1/8\). Restoring both correlated
reserves gives

\[
 \boxed{\mathcal R_J>20.}
\]

The audited Round 22 implication \(\Phi_\delta>\mathcal R_J\) therefore
gives \(\Phi_\delta>20\) at this witness. This is not a counterexample to
\(\mathcal R_J\), \(\Phi_\delta\), CST-H, or the general-dimensional Polya
theorem.

## 1. Exact tuple and phase

Take

\[
 \boxed{
 r={57755\over2},\quad p=80,\quad m=15,\quad f=2,
 \quad\alpha={1\over2},\quad\mu=28973,
 \quad t={7801\over100000}.}                              \tag{1.1}
\]

Then

\[
 q=r+p+m={57945\over2},\qquad \mu=q+\alpha,
\]

so this is the allowed half-integer owner with \(0\leq\alpha<1\). Put

\[
 x=r+p={57915\over2},\qquad h=f-{1\over4}={7\over4},
\]

\[
 K={\mu\over\cos t},\qquad
 A_t(z)=G_K(z)-G_\mu(z),\qquad
 W={\mu\over\pi}(\tan t-t).
\]

All quantities in (1.1) are exact rationals; only their transcendental
images are enclosed with directed-rounding Arb balls.

## 2. Complete shelf and activity certification

At (1.1), Arb certifies

\[
 A_t(x)-h
 >0.00667018,                                             \tag{2.1}
\]

\[
 h-A_t(x+1)
 >0.00994425,                                             \tag{2.2}
\]

\[
 h+1-A_t(r)
 >0.00470557.                                             \tag{2.3}
\]

It also certifies \(A_t(x+1)>h-1\), so the first drop is exactly from
floor \(f=2\) to floor \(f-1=1\), not a skipped lower floor. Since \(A_t\)
is decreasing in its spatial argument, (2.1)--(2.3) give the complete first
shelf from \(r\) through \(x\) and the strict drop at \(x+1\).

For the half-integer activity constant \(\gamma=2\), the exact activity
margin is larger than

\[
 8.4349\times10^8.                                       \tag{2.4}
\]

Thus the tuple is very far from the no-mode boundary.

The terminal action is

\[
 W=1.462957340149395\ldots,\qquad
 u=W-1=0.462957340149395\ldots.                           \tag{2.5}
\]

Consequently

\[
 1<W+{1\over4}<2,\qquad
 B_0=[W+\tfrac14]_< =1,                                  \tag{2.6}
\]

and

\[
 0<u<{1\over\sqrt2},\qquad
 \lambda={3\over4}-u=0.287042659850604\ldots>0.          \tag{2.7}
\]

This is strictly inside the delicate quadratic cell, with exact top
payment \(2u^2\). All shelf samples lie below \(\mu<K\), so no turning or
literal-bracket equality is hidden.

## 3. Certified negative C8 value

On this cell,

\[
\begin{aligned}
 \mathcal C _8={}&
 {p^2(3r+2p)(1-\cos t)\over3\pi\mu}-{p\over2}
 +{m\over2}\left(1-{2t\over\pi}\right)\\
 &+B_0\left({\pi\over2t}-1\right)+2u^2-{1\over8}.
\end{aligned}                                             \tag{3.1}
\]

Directed rounding gives

\[
 \boxed{
 \mathcal C _8=
 -7.2464375575772737935\ldots<-7.}                        \tag{3.2}
\]

The rational point is close to, but not exactly at, the fixed-\(\mu\)
stationary point. Its derivative is

\[
 D(t)=-0.0106732390608746\ldots.                          \tag{3.3}
\]

This distinction does not affect (3.2): one exact feasible point already
falsifies the proposed global C8 sign.

There is also a stronger stationary corollary. Arb proves that \(D\) changes
sign on

\[
 {1950261\over25000000}<t_*
 <{1560209\over20000000},                                 \tag{3.4}
\]

that is,

\[
 0.07801044<t_*<0.07801045.
\]

On this interval,

\[
 D'(t)>24000.                                             \tag{3.5}
\]

Hence \(t_*\) exists and is unique. The complete shelf, activity, action,
and bracket conditions remain strict throughout (3.4), and interval
evaluation certifies

\[
 \boxed{\mathcal C _8(t_*)<-7.}                           \tag{3.6}
\]

Thus the failure also occurs on the exact interior stationary branch
treated in Round 25.

## 4. Exact correlated scalar and failure ledger

Retain the Round 21 definitions

\[
 a_p={p^2\over3(2r+p)},
\]

\[
 L_0=\max\left\{(s-1)\lambda,
 {\kappa\over2}p(2r+p)\right\},
\]

where

\[
 s=\sqrt{1+{p(2r+p)\over X(X+2r+2p)}},\qquad
 X=\mu-r-p,\qquad
 \kappa={1-\cos t\over\pi\mu}.
\]

At the exact rational point, the two branches are

\[
 (s-1)\lambda
 =0.424960961326777\ldots,                                \tag{4.1}
\]

\[
 {\kappa\over2}p(2r+p)
 =0.0772961205283187\ldots.                               \tag{4.2}
\]

Thus the literal maximum is the elasticity branch. The exact local cap is

\[
 J=2I_\mu(q)
 =0.0002493402544746077\ldots.                            \tag{4.3}
\]

The two reserves discarded in passing from \(\mathcal R_J\) to
\(\mathcal C_8\) are therefore

\[
 (p+a_p)(L_0-L_{\rm curv})
 =27.8260114186913\ldots,                                 \tag{4.4}
\]

\[
 {1\over8}-J
 =0.124750659745525\ldots.                                \tag{4.5}
\]

They obey the exact accounting identity

\[
 \boxed{
 \mathcal R_J
 =\mathcal C _8
 +(p+a_p)(L_0-L_{\rm curv})
 +\left({1\over8}-J\right).}                             \tag{4.6}
\]

Substitution gives

\[
 \boxed{
 \mathcal R_J
 =20.704324520859566\ldots>20.}                           \tag{4.7}
\]

The same positive bound holds throughout the stationary box (3.4).
Therefore the audited implication

\[
 \Phi_\delta>\mathcal R_J
\]

proves \(\Phi_\delta>20\) at both the rational witness and its stationary
corollary. No negative exact correlated scalar has been found here.

## 5. Reproduction

Certified artifact:

`computations/general_d_round26b_c8_exact_feasible_counterexample.py`

Run

```text
python -B computations/general_d_round26b_c8_exact_feasible_counterexample.py
```

The script independently checks the interface, all shelf relations, the
post-drop lower floor, half-integer activity, literal \(B_0\), quadratic
cell, direct C8 sign, nearby stationary root, literal \(L_0\) branch, exact
cap, both reserves, and \(\mathcal R_J\). All transcendental sign decisions
use directed-rounding Arb arithmetic.

## 6. Consequence for the workflow

The exact-domain target

\[
 \boxed{\mathcal C _8\geq0}
\]

is false and must be rejected. Rounds 24 and 25 contain valid reductions
of that scalar, but no refinement of their shelf projection can prove its
false sign. In particular, the failure is not caused by the Round 25
\(p_{\max}\) substitution: (3.2) is the direct C8 value with the exact
owner \(p=80\).

The load-bearing loss is the Round 23 replacement

\[
 L_0\longmapsto L_{\rm curv},
\]

with the cap replacement \(J\mapsto1/8\) contributing a smaller additional
loss. The next analytic round should return to the exact maximum in \(L_0\)
and retain \(J\), or use the strategy-approved weighted aggregate theorem.
Another continuous owner or ratio partition is not indicated.

The sign of \(\mathcal R_J\) and the general theorem remain open globally.
