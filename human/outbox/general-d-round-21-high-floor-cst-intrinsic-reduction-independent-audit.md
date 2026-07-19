# Independent audit: Round 21 intrinsic high-floor CST reduction

Date: 19 July 2026  
Audited source: `human/outbox/general-d-round-21-high-floor-cst-intrinsic-reduction.md`  
Audited source SHA-256: `C58A6C15E2A56035BF606B71035795546CD334B4C1817C43DB281B06D4FEFDF1`  
Verdict: **PASS**

The conditional reduction is mathematically valid.  The current audited
source incorporates the two local strictness/notation repairs checked in
Section 7 below.  This audit does not prove \(\mathcal R\geq0\), does not
prove CST-H, and does not promote the general-dimensional theorem.

## 1. Local-cap bound

On the new extension grids, \(p<n\) implies \(n\geq1\), while the least
integer and half-integer shifts are respectively \(1\) and \(3/2\).
Therefore \(q=r+n\geq2\).  Monotonicity in the ball radius gives

\[
 J=2\int_q^\mu G_\mu<2I_{q+1}(q).
\]

After \(z=q+x\), \(R=q+y\), radius averaging gives exactly

\[
 I_{q+1}(q)=\frac1\pi\int_{0\leq x\leq y\leq1}
 \sqrt{1-\left(\frac{q+x}{q+y}\right)^2}\,dy\,dx.
\]

For \(x<y\), the inner quotient has derivative
\((y-x)/(q+y)^2>0\), so the integral decreases with \(q\).  Direct
integration at \(q=2\) reproduces

\[
 2I_3(2)=\frac{17\arccos(2/3)-6\sqrt5}{2\pi}.
\]

The rational ledger in the source is exact:

\[
 5-\left(\frac{682}{305}\right)^2=\frac1{93025}>0,
\]

\[
 \arccos\frac23
 =\frac\pi4+\arctan(9-4\sqrt5)
 <\frac{3593}{4270},
\]

\[
 17\frac{3593}{4270}-6\frac{682}{305}
 =\frac{3793}{4270},\qquad
 \frac{333}{371}-\frac{3793}{4270}
 =\frac{2101}{226310}>0.
\]

Since \(333/371=(2/7)(333/106)<2\pi/7\), the strict bound
\(J<1/7\) follows.  The completed \(r=1/2\) three-dimensional owner is
correctly excluded from this extension-grid claim.

## 2. Strict interface count and complete-level transport

Write \(h=f-1/4\), \(W=G_K(\mu)=h-\lambda\).  The first drop occurs no
later than \(r+p+1\leq q\); because \(A\) is decreasing on the inner
branch, \(A(q)<h\).  Since \(W=A(\mu)\leq A(q)\), this proves
\(\lambda>0\).

The ordinary terminal count obeys \(Q\leq f-1\), while \(v\geq A(q)\)
and \(v\geq W\) give \(B\geq Q\) and \(B\geq B_0\).  If
\(k\leq B_0=[W+1/4]_<\), strict counting gives \(k-1/4<W\).  Since
\(G_K(K\cos\theta)\) increases with \(\theta\),

\[
 \theta_k<\arccos\rho=\pi c,
 \qquad \frac1{2\beta_k}>\frac1{2c}.
\]

For the remaining complete levels, their inverse points lie strictly beyond
\(q>0\), hence \(\beta_k<1/2\) and \(1/(2\beta_k)>1\).  Dropping only
nonnegative terms from the raw terminal bound and using \(J<1/7\) yields

\[
 L_T>\frac{B_0}{2c}+(B-B_0)-Q-\frac17
 =\frac{B_0(1-2c)}{2c}+(B-Q)-\frac17,
\]

which proves (2.2).  No inverse fractional reserve is used, so the estimate
is safe on the bad side of a spatial wall.

## 3. Top-interval dichotomy

When \(0<\lambda<1\), strict counting gives \(B_0=f-1\), and monotonicity
after the first drop gives \(Q\leq B_0\).  If \(B\geq B_0+1\), then
\(B-Q\geq1\).  If \(B=B_0\) and \(\lambda<3/4\), then

\[
 v-B_0\geq W-B_0=\frac34-\lambda>0,
 \qquad \beta<\frac12,
\]

so the top interval is strictly larger than
\(2(3/4-\lambda)^2\).  If instead \(\lambda\geq3/4\), then
\(\mathcal E(\lambda)=0\), and the already proved general estimate (2.2)
is sufficient.  Thus the stated bound (2.3) is correct on every face,
including action walls.  The current source includes exactly this
qualification.

## 4. Shelf elasticity and curvature

The coordinate identities are exact:

\[
 r+p=\mu-X,\qquad r=\mu-(X+p),\qquad
 H(X)-W=\lambda+e_p,\quad H(X+p)-W=\lambda+e_0.
\]

The previously proved shell-increment elasticity theorem applies because
\(0<X<X+p\leq\mu\), and gives

\[
 \lambda+e_0\geq s(\lambda+e_p),\qquad
 s^2=\frac{V(X+p)}{V(X)}
 =1+\frac{p(2r+p)}{X(X+2r+2p)}.
\]

Since \(e_p\geq0\) on the first shelf,

\[
 \Delta=e_0-e_p\geq(s-1)(\lambda+e_p)
 \geq(s-1)\lambda.
\]

Independently,

\[
 \sigma'(z)=\frac1{\pi\sqrt{\mu^2-z^2}}
 -\frac1{\pi\sqrt{K^2-z^2}}
\]

is increasing on the inner branch and

\[
 \sigma'(0)=\frac{1-\rho}{\pi\rho K}=\kappa.
\]

Thus \(\sigma(z)\geq\kappa z\), and integration gives exactly

\[
 \Delta\geq\frac\kappa2p(2r+p).
\]

Consequently \(\Delta\geq L_0\).  Also
\(E-\Delta=2e_p\geq0\), so the lower-surrogate shelf term itself satisfies

\[
 a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}
 \geq(p+a_p)L_0-\frac p2+\frac{dm}{2}. \tag{A}
\]

The exact shelf identity plus (S3) also gives the same displayed lower bound
with \(R_p+dm/2\) on the left.  Formula (A), rather than only that latter
consequence, is the statement needed for \(\Phi_\delta\).

## 5. Intrinsic elimination and final implication

For \(\theta=\pi c\in(0,\pi/2)\) and
\(\varphi(\theta)=\sin\theta-\theta\cos\theta>0\), direct substitution
reproduces

\[
 K=\frac{\pi W}{\varphi(\theta)},\qquad
 \mu=\frac{\pi W\cos\theta}{\varphi(\theta)},
\]

\[
 \kappa=\frac{(1-\cos\theta)\varphi(\theta)}
 {\pi^2\cos\theta\,W},\qquad
 W=f-\frac14-\lambda,
\]

and

\[
 \alpha=\mu-r-p-m
 =\frac{\pi(f-\frac14-\lambda)\cos\theta}
 {\varphi(\theta)}-r-p-m\in[0,1).
\]

This is an exact necessary correlation and exactly eliminates
\(K,\mu,\kappa\).  It is not, by itself, a complete characterization of a
first-drop tuple: the contextual grid, integrality, action, activity, and
shelf constraints remain part of the word “feasible” in Theorem 4.1.

Adding Proposition 2.1 to (A) gives, without assuming any sign for
\(\mathcal R\),

\[
 \Phi_\delta>\mathcal R.
\]

Only the additional, still-open assertion \(\mathcal R\geq0\) would imply
\(\Phi_\delta>0\), hence the exact CST scalar is positive.  The source
correctly does not make that assertion.

## 6. Corrected spatial-wall calibration

An independent 70-digit reconstruction gives

\[
 G_{K_0}(7)=\frac34,qquad
 K_0=11.04926798504801089907798018\ldots,
\]

not \(G_{K_0}(6)=3/4\).  With \(\mu=5.0380000005\), it reproduces

\[
 \rho=0.455957807097943\ldots,\quad
 \lambda=0.379541122330352\ldots,\quad B_0=B=Q=1.
\]

On the right-hand spatial-wall limit \(y_1\downarrow2^+\), so
\(\eta_1\downarrow0\), the independently recomputed pieces are

\[
 \frac\pi{2\theta_1}-1=0.775524602820\ldots,\qquad
 \frac{(v-1)^2}{\beta}=0.420135638672\ldots,\qquad
 J=0.0000301169413\ldots,
\]

\[
 L_{T,+}=1.195630124551\ldots,qquad
 a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}
 =-0.357364051041\ldots,
\]

\[
 \Phi_{\delta,+}=0.838266073510\ldots.
\]

The root-free bound gives

\[
 \frac d{2c}+\mathcal E(\lambda)-\frac17
 =0.563069877584\ldots,
\]

leaving reserve \(0.205705826543\ldots\) against the displayed shelf
lower bound.  At the literal wall itself \(\eta_1=1\), so its literal
\(L_T\) is larger by exactly \(2\); the source's displayed value is correctly
interpreted as the bad-side limit, not the wall value.

## 7. Revision checks and boundary verdict

1. The current proof of Proposition 2.1 claims the strict top payment only
   for \(\lambda<3/4\), and uses its nonnegative zero payment for
   \(\lambda\geq3/4\).  This is the correct split.
2. The current source states the direct lower-surrogate inequality as (3.8)
   and Theorem 4.1 cites (3.8), not merely the companion \(R_p\) inequality
   (3.7).  This closes the former notation/citation gap without changing
   \(\mathcal R\) or (4.5).

All strict outer-support, interface, action-count, and inverse-spatial wall
directions otherwise check.  The corrected Round 20 wall is reproduced.
The proper result is therefore a valid conditional intrinsic reduction,
with the sign of \(\mathcal R\) and CST-H still open.
