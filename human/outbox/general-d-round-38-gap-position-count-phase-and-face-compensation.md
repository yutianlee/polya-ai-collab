# General dimension, Round 38: gap position, count--phase compensation, and face compensation

Date: 20 July 2026

Status: mixed.  The gap-position theorem, the count--phase lemma, the
closure of every residual one-level gap with \(p\leq2\), and the unified
\(\chi\)-compensation and root-free lower bounds are proved below.  The
remaining \(p\geq3\) sign is a structural reduction, not a completed
theorem.  The selected high-floor first-drop obligation and the
all-dimensional Pólya theorem remain open.  The completed note and both
computational companions passed the independent audit in
`human/outbox/general-d-round-38-independent-audit.md`.

## 0. Theorem boundary and dependencies

The authoritative obligation graph is
`state/proof_obligations.yml`, with SHA-256

`a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.

The selected obligation remains
`SHELL-general-d-high-floor-first-drop-CST`.  The exact general-dimensional
branching backbone remains `derived_under_assumptions`; this note does not
promote it.  No status in the obligation graph is changed in Round 38.

The proof uses only the following promoted local inputs.

1. Round 28 supplies the exact shelf projection, the inequalities
   \(\Delta\geq\tau(E+2\lambda)\),
   \(\Delta>\mathcal K_4\), and the implication from the selected scalar
   to the shifted defect.
2. Rounds 34--35 supply the normalized lower-\(Q\) contradiction and the
   common-radial-parameter adjacent-action estimate.
3. Round 36 supplies the hard one-level gap decomposition, the cap bound
   \(J<1/7\), the terminal formula, and the already proved \(p=1\)
   closure.
4. Round 37 supplies the synchronization
   \(B_0=Q=B-1\geq1\), the exact inverse decomposition, and the selected
   projected scalar.  The ownership and loss-language corrections made
   below supersede the corresponding Round 37 prose.
5. The binding methodology is
   `human/inbox/general-d_simplified_analytic_strategy.md`; the Round 38
   route is fixed by `human/inbox/general-d-strategy_r2.md`.

Throughout this note

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
 \qquad b_a(z)=\frac1\pi\arccos\frac za,
\]

\[
 A(z)=G_K(z)-G_\mu(z),\qquad q=r+p+m,\qquad
 \mu=q+\alpha,\qquad K=\frac\mu{\cos t},
\]

with \(0<t<\pi/2\), \(0<\alpha<1\), and

\[
  W=G_K(\mu)=\frac\mu\pi(\tan t-t),\qquad
 h=G_\mu(q),\qquad v=G_K(q).
\]

The hard sector has \(E<E_*=(p-dm)/(2p)\), hence \(p>dm\).  The exact
endpoint scalar is

\[
 \Phi_\delta^+
 =1-J+\Omega+B_0\zeta+(p+a_p)\Delta+2pe_p
   -\frac{p-dm}{2},
 \qquad
 \zeta=\frac d{2c}=\frac\pi{2t}-1,
\tag{0.1}
\]

where \(c=t/\pi\), \(d=1-2c\), and

\[
 a_p=\frac{p^2}{3(2r+p)}.
\]

No ratio ladder, count ladder, extra chamber, or second compressed
certificate is introduced.

## 1. Gap-position coordinate

Work first at a literal positive-\(\alpha\) hard one-level gap point:

\[
 B=Q+1,\qquad B_0=Q=B-1\geq1.
\tag{1.1}
\]

Put

\[
 j=f-B,\qquad u=\lambda-j,\qquad
 S_q=A(q)-W,\qquad \chi=u-S_q.
\tag{1.2}
\]

### Theorem 1.1 (sharp gap position)

Every literal positive-\(\alpha\) gap point, including its literal
\(Q\)-wall owner, satisfies

\[
 \boxed{
 0<S_q\leq u<S_q+h<\frac\alpha2,
 \qquad 0\leq\chi<h,
 \qquad 0<u<\frac\alpha2<\frac12.}
\tag{R38.1}
\]

It also has the exact coordinates

\[
 \boxed{W=B-\frac14-u,}
\tag{R38.2}
\]

\[
 \boxed{
 A(q)=B-\frac14-\chi,
 \qquad
 v=B-\frac14+h-\chi,}
\tag{R38.3}
\]

\[
 \boxed{\xi:=A(q)+\frac14-Q=1-\chi,}
\tag{R38.4}
\]

and, for \(x=r+p\),

\[
 \boxed{A(x)-A(q)=j+e_p+\chi.}
\tag{R38.5}
\]

#### Proof

Since \(G_a'(z)=-b_a(z)\), \(G_\mu(\mu)=0\), and \(K>\mu\),

\[
 \begin{aligned}
 S_q
 &=G_K(q)-G_\mu(q)-G_K(\mu)\\
 &=\int_q^\mu\{b_K(z)-b_\mu(z)\}\,dz>0.
 \end{aligned}
\tag{1.3}
\]

Moreover,

\[
 S_q+h=v-W=\int_q^\mu b_K(z)\,dz.
\tag{1.4}
\]

Here \(0<b_K(z)<1/2\), and the interval has length \(\alpha\), so

\[
 0<S_q<S_q+h<\frac\alpha2.
\tag{1.5}
\]

Round 37 gives \(B_0=[f-\lambda]_< =B-1\).  With \(j=f-B\), literal
strict ownership therefore gives

\[
 B-1<f-\lambda\leq B,
 \qquad j\leq\lambda<j+1.
\tag{1.6}
\]

Thus \(u=\lambda-j\) and

\[
 W=f-\frac14-\lambda=B-\frac14-u,
\]

which proves (R38.2).  The terminal count \(Q=B-1\) gives
\(A(q)\leq B-1/4\).  Hence

\[
 S_q=A(q)-W\leq u.
\tag{1.7}
\]

The outer count \(B=[v+1/4]_<\) gives \(v>B-1/4\).  Equations
(1.4) and (R38.2) then give

\[
 S_q+h=v-W>u.
\tag{1.8}
\]

Consequently \(0\leq\chi=u-S_q<h\).  Combining (1.5), (1.7), and
(1.8) proves all of (R38.1), including \(u>0\).  In particular

\[
 j<\lambda<j+\frac12.
\tag{1.9}
\]

Finally, \(S_q=u-\chi\) in \(A(q)=W+S_q\) proves the first identity in
(R38.3), while \(v=A(q)+h\) proves the second.  Since \(Q=B-1\), this
also proves (R38.4).  The first-shelf coordinate
\(A(x)=f-1/4+e_p=B+j-1/4+e_p\) then proves (R38.5).  \(\square\)

The strict inequalities in (R38.1) are statements about positive-
\(\alpha\) gap owners.  At the gap-side outer-\(B\) closure one has the
limiting equality \(u=S_q+h\) and \(\chi=h\).  At the lower gap limit all
four quantities \(S_q,u,h,\chi\) tend to zero.  Those closures are recorded
with their correct one-sided labels in Section 6.

### Corollary 1.2 (no positive-alpha integer-λ wall)

There is no finite integer-\(\lambda\) wall in the positive-\(\alpha\)
gap.  Indeed, (1.9) places \(\lambda\) strictly between \(j\) and
\(j+1/2\).  The only finite gap-side integer limit is
\(\alpha\downarrow0\), where \(u\downarrow0\) and
\(\lambda\downarrow j^+\).  The Round 37 discussion of a gap-owned
\(\lambda\to N^-\) face applies only to generic strict-floor arithmetic
outside this gap owner and is not used here.

### Corollary 1.3 (the \(B_0=0\) sublevel is excluded)

If a hard gap had \(B_0=0\), synchronization would give
\((B,Q)=(1,0)\).  The exact inherited hypotheses are

\[
 \boxed{
 W<\frac34,
 \qquad A(x)-A(q)\geq1,
 \qquad P>dM,}
\tag{1.10}
\]

where \(P=p/\mu\) and \(M=m/\mu\).  The first two follow from

\[
 W<A(q)\leq\frac34,
 \qquad
 A(x)-A(q)\geq f-1+e_p\geq1.
\]

These inequalities, not the literal equality \(A(q)=3/4\), are exactly
what place the tuple in the normalized Round 34 domain.  The Round 34
common-radial-parameter and Jensen estimates give
\(\Delta>C(z,P,M,t)\), and the Round 35 sign on that domain gives
\(C>E_*\).  Hence \(E\geq\Delta>E_*\), contrary to the hard-sector
hypothesis \(E<E_*\).  Thus \(B_0\geq1\), as used in (1.1).

## 2. Refined selected normal form and its loss boundary

Let

\[
 \mathfrak s=
 \sqrt{1+\frac{p(2r+p)}{X(X+2r+2p)}},
 \qquad X=m+\alpha,
\]

\[
 g=\mathfrak s-1,
 \qquad
 \tau=\frac{\mathfrak s-1}{\mathfrak s+1}=\frac g{g+2},
\]

and retain the Round 28 projected shelf payment

\[
 M_4=\max\{\tau(E+2\lambda),\mathcal K_4\}.
\]

Round 28 gives \(\Delta\geq M_4\).  Define

\[
 \widehat\Xi:=\Delta-M_4\geq0.
\tag{2.1}
\]

Since \(E=\Delta+2e_p\),

\[
 \boxed{\Xi:=E-M_4=2e_p+\widehat\Xi.}
\tag{R38.6}
\]

Substitution in the exact Round 37 normal form gives

\[
 \boxed{
 \begin{aligned}
 \Gamma_{\rm gap}
 ={}&1-J+B_0\zeta+\Omega
 +(p+a_p)M_4+2pe_p+p\widehat\Xi\\
 &-\frac{p-dm}{2}.
 \end{aligned}}
\tag{R38.7}
\]

This identity is exact, hence lossless, **for the selected projected
scalar \(\Gamma_{\rm gap}\) only**.  It is not lossless relative to
\(\Phi_\delta^+\) or \(D_A(r)\).

There is also a sharper elasticity retained by \(M_4\).  Indeed,

\[
 M_4\geq\tau(E+2\lambda)
 \geq\tau\{M_4+2e_p+2\lambda\}.
\]

Therefore

\[
 (1-\tau)M_4\geq2\tau(\lambda+e_p).
\]

Since \(2\tau/(1-\tau)=g\),

\[
 \boxed{M_4\geq g(\lambda+e_p).}
\tag{R38.8}
\]

The exact projection loss at this step is visible:

\[
 \boxed{
 \Phi_\delta^+-\Gamma_{\rm gap}
 =a_p(\Delta-M_4)=a_p\widehat\Xi\geq0.}
\tag{2.2}
\]

Thus \(\Gamma_{\rm gap}\geq0\), including equality, is sufficient for
the projected gate.  A genuine obstruction to the universal selected
sign must have \(\Gamma_{\rm gap}<0\); its Round 37 failure inequality is
then strict.  The separate inequality
\(\Phi_\delta^+>\mathcal H_\Delta\) remains strict on the positive-
\(\alpha\) gap and on its directly evaluated gap-side closures.  It is not
asserted at the distinct literal equal-count \(\alpha=0\) corner.

## 3. Count--phase compensation

The position coordinate immediately gives

\[
 W=B_0+\frac34-u.
\tag{3.1}
\]

Hence, at every positive-\(\alpha\) gap point and every finite gap-side
closure,

\[
 B_0+\frac14<W\leq B_0+\frac34.
\tag{R38.10}
\]

The left inequality is strict because \(u<1/2\); the right one allows the
lower gap limit \(u\downarrow0\).

### Lemma 3.1 (R38-CP)

Every hard gap point and every finite gap-side endpoint satisfies

\[
 \boxed{B_0\zeta>\frac15.}
\tag{R38.9}
\]

#### Proof

First suppose \(\zeta\geq1/5\).  Since \(B_0\geq1\), one has
\(B_0\zeta\geq1/5\).  Equality would force \(B_0=1\) and
\(\zeta=1/5\), hence \(t=5\pi/12\).  Since \(q\geq3\) and
\(\mu\geq q\),

\[
 \begin{aligned}
 W
 &=\frac\mu\pi\left(\tan\frac{5\pi}{12}
                    -\frac{5\pi}{12}\right)\\
 &\geq\frac3\pi\left(2+\sqrt3-\frac{5\pi}{12}\right)
 >\frac3\pi\left(\pi-\frac{5\pi}{12}\right)
 =\frac74.
 \end{aligned}
\]

Here \(2+\sqrt3>\pi\).  This contradicts (R38.10), which gives
\(W\leq7/4\) when \(B_0=1\).  Thus the desired inequality is strict in
this case.

Now suppose \(0<\zeta<1/5\), and put

\[
 x=\frac\pi2-t
   =\frac{\pi\zeta}{2(1+\zeta)}.
\tag{3.2}
\]

For \(0<x<\pi/2\), set

\[
 F(x)=x\cos x-(1-x^2)\sin x.
\]

Then \(F(0)=0\) and

\[
 F'(x)=x^2\cos x+x\sin x>0.
\]

Consequently \(F(x)>0\), and division by \(x\sin x>0\) gives

\[
 \boxed{\cot x>\frac1x-x.}
\tag{R38.11}
\]

Since \(t=\pi/2-x\),

\[
 \tan t-t=\cot x-\frac\pi2+x>\frac1x-\frac\pi2.
\tag{3.3}
\]

Because \(\zeta<1/5\), (3.2) gives \(x<\pi/12\), and hence
\(1/x-\pi/2>12/\pi-\pi/2>0\).  Thus the right-hand side is positive
before \(\mu\) is replaced by its lower bound.  Using \(\mu\geq3\),
(R38.10), and (3.3),

\[
 B_0\geq W-\frac34
 >\frac3{\pi x}-\frac94.
\tag{3.4}
\]

Multiplication by \(\zeta>0\) and (3.2) yield

\[
 B_0\zeta>
 \frac{6(1+\zeta)}{\pi^2}-\frac{9\zeta}{4}
 =:L(\zeta).
\tag{3.5}
\]

The affine function \(L\) is decreasing because
\(6/\pi^2-9/4<0\).  Hence, for \(0<\zeta<1/5\),

\[
 L(\zeta)>L\!\left(\frac15\right)
 =\frac{36}{5\pi^2}-\frac9{20}
 >\frac{36}{50}-\frac9{20}
 =\frac{27}{100}>\frac15,
\]

where \(\pi^2<10\) was used.  This completes both cases.  \(\square\)

### Corollary 3.2 (R38-CP2: complete \(p\leq2\) gap closure)

Round 36 gives \(J<1/7\), while
\(\Omega>0\), \(M_4\geq0\), \(e_p\geq0\), and
\(\widehat\Xi\geq0\).  Equations (R38.7) and (R38.9) therefore give

\[
 \boxed{
 \Gamma_{\rm gap}>
 \frac67+\frac15-\frac{p-dm}{2}
 =\frac{37}{35}-\frac{p-dm}{2}.}
\tag{R38.12}
\]

Consequently every gap with

\[
 \boxed{p-dm\leq\frac{74}{35}}
\tag{R38.13}
\]

has \(\Gamma_{\rm gap}>0\), hence
\(\Phi_\delta^+\geq\Gamma_{\rm gap}>0\) and \(D_A(r)>0\) through the
inherited implication chain.  In particular, if \(p=2\), then
\(p-dm<2<74/35\).  Thus every residual \(p=2\) one-level gap is closed.
The \(p=1\) gap was closed in Round 36.  All remaining one-level gap work
therefore has

\[
 \boxed{p\geq3.}
\tag{3.6}
\]

This is the new analytic sign theorem of Round 38.  It does not close the
remaining \(p\geq3\) faces or any equal-count class.

## 4. Unified \(Q\)-wall/outer-\(B\) compensation

For \(p\geq3\), put

\[
 \beta=b_K(q)=\frac1\pi\arccos\frac qK
\]

and split

\[
 \Omega=\Omega_-+\omega_B,
\tag{4.1}
\]

where

\[
 \Omega_-=
 \sum_{k=1}^{B_0}
 \left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right),
\]

\[
 \omega_B=\frac\pi{2\theta_B}-1+2y_B.
\]

Here \(G_K(q+y_B)=B-1/4\).  The gap coordinates give

\[
 \boxed{
 h-\chi=v-\left(B-\frac14\right)
 =\int_q^{q+y_B}b_K(z)\,dz.}
\tag{R38.14}
\]

Because \(b_K\) is decreasing and \(\beta=b_K(q)\),

\[
 h-\chi\leq\beta y_B,
 \qquad
 \boxed{y_B\geq\frac{h-\chi}{\beta}.}
\tag{R38.15}
\]

Also

\[
 \theta_B=\pi b_K(q+y_B)\leq\pi\beta.
\]

Therefore

\[
 \boxed{
 \omega_B\geq
 \frac1{2\beta}-1+\frac{2(h-\chi)}{\beta}.}
\tag{R38.16}
\]

The Round 34 common-radial-parameter proof, before its lower-\(Q\)
specialization, writes

\[
 \frac{\Delta}{A(x)-A(q)}
\]

as a positive weighted average of radial ratios strictly exceeding
\(R_1\).  Applying that proof to the actual action drop (R38.5), including
directly on each finite endpoint closure, gives

\[
 \boxed{\Delta>R_1(j+e_p+\chi).}
\tag{R38.17}
\]

Set

\[
 H_*=(p+a_p)R_1,
 \qquad n=f-1,
 \qquad B_0=n-j.
\tag{4.2}
\]

Then

\[
 \begin{aligned}
 B_0\zeta+(p+a_p)\Delta
 &>(n-j)\zeta+H_*(j+e_p+\chi)\\
 &\geq n\min\{\zeta,H_*\}+H_*e_p+H_*\chi.
 \end{aligned}
\]

Thus

\[
 \boxed{
 B_0\zeta+(p+a_p)\Delta
 >n\min\{\zeta,H_*\}+H_*e_p+H_*\chi.}
\tag{R38.18}
\]

For completeness, if \(H_*\geq\zeta\), the residual in the second line
is \(j(H_*-\zeta)\geq0\); if \(H_*\leq\zeta\), it is
\((n-j)(\zeta-H_*)\geq0\).  This is one sharp minimum inequality, not a
new theorem split.

For \(0\leq\chi\leq h\), the remaining two payments form a convex
combination:

\[
 H_*\chi+\frac{2(h-\chi)}\beta
 =h\left\{
 \frac\chi h H_*+\left(1-\frac\chi h\right)\frac2\beta
 \right\}.
\]

The \(h=0\) closure is immediate.  Hence

\[
 \boxed{
 H_*\chi+\frac{2(h-\chi)}\beta
 \geq h\min\left\{H_*,\frac2\beta\right\}.}
\tag{R38.19}
\]

Substituting (R38.16), (R38.18), and (R38.19) into (0.1) cancels the
initial \(1\) against the \(-1\) in (R38.16) and proves

\[
 \boxed{
 \begin{aligned}
 \Phi_\delta^+>{}&
 \frac1{2\beta}-J+\Omega_-\\
 &+(f-1)\min\{\zeta,H_*\}+H_*e_p\\
 &+h\min\left\{H_*,\frac2\beta\right\}
 +2pe_p-\frac{p-dm}{2}.
 \end{aligned}}
\tag{R38.20}
\]

The strict sign is inherited from (R38.17), whose weighted-average proof
applies directly at the finite closures; it is not inferred merely by
taking a limit of a strict inequality.

Equation (R38.20) is a proof-level lower bound inside the existing proof,
not a new global scalar or certificate.  If its right-hand side is
nonnegative, then \(\Phi_\delta^+>0\).  Positivity here does not imply that
the older, smaller \(\mathcal H_\Delta\) is nonnegative.  Conversely, a
negative right-hand side does not falsify \(\Phi_\delta^+\).

The compensation is continuous in the exact gap position.  At the
\(Q\)-wall, \(\chi=0\), so the newest inverse displacement pays.  At the
gap-side outer-\(B\) closure, \(\chi=h\), so \(y_B=0\) and the adjacent
action pays.  The interior interpolates between these payments.  All old
inverse fractions remain inside \(\Omega_-\).

## 5. Optional root-free lower bound for \(\Omega_-\)

For \(1\leq k\leq B_0\), (3.1) gives

\[
 \delta_k:=W-\left(k-\frac14\right)=B_0-k+1-u>0.
\tag{R38.21}
\]

Let

\[
 F(\theta)=G_K(K\cos\theta)
 =\frac K\pi(\sin\theta-\theta\cos\theta).
\]

Then

\[
 F'(\theta)=\frac K\pi\theta\sin\theta.
\tag{5.1}
\]

The old root has \(\theta_k<t\), and
\(\theta\sin\theta\) is strictly increasing on \((0,\pi/2)\).  Therefore

\[
 \delta_k=F(t)-F(\theta_k)
 \leq\frac K\pi t\sin t\,(t-\theta_k).
\tag{5.2}
\]

Also

\[
 \frac\pi{2\theta_k}-\frac\pi{2t}
 =\frac{\pi(t-\theta_k)}{2t\theta_k}
 \geq\frac{\pi(t-\theta_k)}{2t^2}.
\tag{5.3}
\]

Combining (5.2)--(5.3), adding \(2\eta_k\geq0\), and summing gives

\[
 \boxed{
 \Omega_-\geq
 \frac{\pi^2}{2Kt^3\sin t}
 \left\{\frac{B_0(B_0+1)}2-B_0u\right\}.}
\tag{R38.22}
\]

Indeed,

\[
 \sum_{k=1}^{B_0}\delta_k
 =\frac{B_0(B_0+1)}2-B_0u.
\]

Since \(0<u<1/2\), the primary bound implies the coarser corollary

\[
 \boxed{
 \Omega_->\frac{\pi^2B_0^2}{4Kt^3\sin t}.}
\tag{R38.23}
\]

The \(u\)-retaining form (R38.22) is primary.  Equation (R38.23) is used
only when an exact transported endpoint cannot retain the inverse roots.

## 6. Strict ownership and endpoint dictionary

| face | literal owner and exact gap-side data | permitted use |
|---|---|---|
| \(Q\)-wall | \(\chi=0\), \(A(q)+1/4=B\), and \([B]_< =B-1=Q\) | genuinely gap-owned; \(\xi=1\) and the newest inverse displacement is active |
| gap interior | \(0<\chi<h\), \(0<y_B<\alpha\) | use all exact gap labels |
| outer-\(B\) wall | literal count is \(B-1\); gap-side label is \(B^+=B\), with \(\chi=h\), \(y_B=0\), \(\theta_B=\pi\beta\), and \(\eta_B=0\) | formulas retaining level \(B\) are one-sided gap formulas, not literal-wall formulas |
| lower alpha limit | \(\alpha\downarrow0\), \(h,S_q,\chi,u,y_B\to0\) | gap-side limit only; the literal endpoint has \(B=Q\) and is a separate equal-count corner |
| upper alpha endpoint | \(\alpha\uparrow1^-\) | retain the one-sided gap labels; do not reindex it as the next chart's literal \(\alpha=0\) point |
| old inverse wall | literal \(\eta_k=1\); adverse side \(\eta_k\downarrow0\) | both stay inside \(\Omega_-\); the newest level is not an old inverse wall |
| integer-λ wall | none for \(0<\alpha<1\) | only \(\lambda\downarrow j^+\) at the lower gap limit occurs |
| hard wall | \(p=dm\) | belongs to the automatic sector, not the live residual |

For positive \(\alpha\), the angle order is

\[
 \theta_k<t<\theta_B\leq\pi\beta
 \qquad(1\leq k\leq B_0),
\]

with the right equality at the outer-\(B\) closure.  The newest
\(y_B=0\) event is the outer-action jump and must not be charged as a
second inverse jump.

The order for further endpoint work is therefore:

1. outer-\(B\) plus lower shelf
   \((\chi=h,y_B=0,e_p=0)\);
2. outer-\(B\) plus \(\alpha\uparrow1^-\), retaining the exact cap;
3. \(Q\)-wall endpoints \((\chi=0)\);
4. generic old inverse literal/adverse faces;
5. the gap-side lower-alpha limit, excluding the literal equal-count
   corner.

At the upper alpha endpoint, the exact retained formulas are

\[
 h=
 \frac{\sqrt{2q+1}-q\arccos(q/(q+1))}{\pi},
\tag{6.1}
\]

\[
 J=
 \frac{((q+1)^2+2q^2)\arccos(q/(q+1))
       -3q\sqrt{2q+1}}{2\pi},
\tag{6.2}
\]

and \(W=(q+1)(\tan t-t)/\pi\).  No sign beyond (R38.20) is claimed for
this endpoint in Round 38.

## 7. Loss ledger

The exact levels must not be conflated:

\[
 D_A(r)
 \ \geq\ \mathscr S
 \ \geq\ \Phi_\delta^+
 \ \geq\ \Gamma_{\rm gap}
\]

is an implication/lower-bound chain, not a chain of identities at every
step.

| passage | status | reserve discarded or retained |
|---|---|---|
| rewrite of \(\Gamma_{\rm gap}\) as (R38.7) | exact identity | retains \(J,B_0\zeta,\Omega,M_4,e_p,\widehat\Xi\); lossless only for this selected projected scalar |
| \(\Phi_\delta^+\to\Gamma_{\rm gap}\) | exact known difference | discards \(a_p\widehat\Xi\), by (2.2) |
| \(\mathscr S\to\Phi_\delta^+\) | inherited lower bound | discards the exact terminal inverse-tangent surplus and exact shelf-curvature/trapezoid surplus |
| \(D_A(r)\to\mathscr S\) | inherited first-shelf reduction | retains only the reduced tail \(D_A(q)+R_p+dm/2\); its nonnegative reduction slack is separate |
| (0.1) to (R38.20) | one proof-level lower bound | retains \(J,\Omega_-,e_p,h,\beta,\zeta,H_*\), but replaces the newest-root and adjacent-action payments by their correlated minimum |
| (R38.22) to (R38.23) | optional coarse corollary | discards the exact fractional coordinate \(u\) |

In particular, a feasible \(\Gamma_{\rm gap}<0\) point would falsify only
the universal sign of the selected projection.  A negative right-hand side
in (R38.20) would falsify only that lower bound.  Neither event would
falsify \(\Phi_\delta^+\), \(\mathscr S\), \(D_A(r)\), CST, or Pólya.

## 8. Diagnostic-only falsification report

The finite search in
`computations/general_d_round38_gap_face_diagnostic.py` is explicitly
`diagnostic_only`.  It targets \(p\geq3\) one-level gap records on both
integer and half-integer start grids, excludes literal \(\alpha=0\)
equal-count corners, retains literal strict brackets, and samples both
literal and adverse old-inverse ownership.  It checks the gap coordinates,
\(B_0\zeta>1/5\), \(\Gamma_{\rm gap}\),
\(\mathcal H_\Delta\), and the right-hand side of (R38.20).  For every
sampled negative \(\Gamma_{\rm gap}\), it also reports the available exact
shifted-tail loss ledger.

Finite minima, scan cutoffs, and floating-point values in that output are
theorem-design evidence only.  They are not interval certificates and are
not used anywhere in Sections 1--5.  A reproducible modest run

`python -B computations/general_d_round38_gap_face_diagnostic.py --limit 5 --random 200 --wall-limit 50`

retained 1,354 evaluations from 626 feasible tuples: 703 integer-grid
evaluations, 651 half-integer-grid evaluations, and 1,198 records beyond
the proved threshold (R38.13).  It covered 50 literal and 57 adverse old
inverse samples.  The observed minima were

\[
 \min\Gamma_{\rm gap}=1.97221024700173\ldots,
\]

\[
 \min\mathcal H_\Delta=0.996771560326323\ldots,
\]

\[
 \min\operatorname{RHS}(\mathrm{R38.20})
 =1.86292572734470\ldots.
\]

All three occurred at the sampled outer-\(B\), upper-alpha-side tuple
\(r=1,p=3,m=1,f=2,\alpha=0.999999\).  No sampled negative value of any
of the three targets was found.  The smallest sampled
\(B_0\zeta-1/5\) was \(0.244103179304456\ldots\).  These figures are
ordinary binary64 output, not certified lower bounds; no decimal margin is
promoted into the proof.

The companion Mathematica file
`computations/general_d_round38_gap_position_replay.wl` checks the displayed
algebra, derivative identities, and the upper-alpha integral formula.
It prints `round38GapPositionReplayOK=True` under Mathematica 15.0 on
Windows.  Mathematica does not own a strict bracket, wall label, or sign
proof.

## 9. Round 38 outcome and Gate A/B/C decision

### Proved

1. The sharp position coordinate (R38.1)--(R38.5), including the absence
   of positive-\(\alpha\) integer-λ walls.
2. The refined selected normal form (R38.6)--(R38.8) and its exact
   projection-loss qualification.
3. The count--phase lemma \(B_0\zeta>1/5\).
4. The sign (R38.12), hence complete closure of every residual one-level
   gap with \(p\leq2\).
5. The unified face compensation (R38.14)--(R38.20) and the optional
   root-free bound (R38.22)--(R38.23).

### Structural reduction

The remaining one-level gap is confined to \(p\geq3\) and carries the
single correlated lower bound (R38.20).  No intrinsic continuous endpoint
inequality has yet signed all transported \(p\geq3\) faces.  The most
dangerous feasible pattern must determine \(t\) from

\[
 W=\frac\mu\pi(\tan t-t),
\]

and cannot impose the infeasible combination \(B_0=1\),
\(t\uparrow\pi/2\).

### Diagnostic

The directed search is nonproof.  It found no sampled negative value of
\(\Gamma_{\rm gap}\), \(\mathcal H_\Delta\), or (R38.20), so it supplies
no diagnostic reason to stop Gate A.  Its only role is to decide whether
the remaining compressed targets deserve another analytic endpoint pass
and, if one is negative, to identify exactly which discarded reserve must
be restored.

### Decision

**Gate A remains active, but only for one intrinsic \(p\geq3\) endpoint
inequality using \(u,\chi,J,W,\Omega_-,e_p,M_4,\widehat\Xi\).**  The
count--phase and compensation mechanisms have made genuine progress and do
not require a forbidden partition.  A certified exact feasible
\(\Gamma_{\rm gap}<0\) point will immediately stop the universal
\(\Gamma_{\rm gap}\geq0\) target.  The next and only pointwise projection
attempt would then be \(\mathcal H_\Delta\) or the exact
\(\Phi_\delta^+\) through (R38.20); it stops if certified false or if its
proof requires a ratio/count/chamber family.

**Gate B is prepared but not activated by the analytic results of this
round.**  If Gate A stops, restore

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

with the exact terminal and shelf surpluses.  **Gate C is not active.**  It
is reached only if a certified feasible point has \(\mathscr S<0\), or if
the negative support of \(\mathscr S\) cannot be localized by one intrinsic
shelf--terminal theorem without a forbidden split.

The selected high-floor obligation, the equal-count classes, pointwise CST
assembly, the branching-backbone audit, and the all-dimensional theorem all
remain open.
