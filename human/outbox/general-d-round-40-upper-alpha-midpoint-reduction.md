# General-dimensional spherical-shell Pólya project
## Round 40: upper-alpha midpoint reduction

**Date:** 20 July 2026  
**Status:** structural reduction; the final continuum sign is open

## 0. Theorem boundary and dependencies

This note treats only the remaining gap-side endpoint

\[
 \chi=h,\qquad y_B=0,\qquad \alpha\uparrow1^-
\]

on the one-level gap-side outer-\(B\) face. It does **not** prove the
high-floor first-drop CST, the complete one-level-gap theorem, or the
all-dimensional Pólya theorem. It does not edit or promote any obligation in
`state/proof_obligations.yml`.

The dependencies are the following.

1. The authoritative obligation graph has expected SHA-256
   `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.
2. `human/inbox/general-d_simplified_analytic_strategy.md` is binding.
3. `human/inbox/general-d-strategy_r2.md` supplies the Gate A/B/C rules and
   the one-sided endpoint convention.
4. Rounds 34 and 38 supply the adjacent-action and elasticity estimates,
   the sharp gap coordinates, count--phase compensation, and the
   nonnegative old-level reserve.
5. Round 39 supplies the exact outer-\(B\) identity, the exact loss ledger
   relative to \(F_{\rm OB}\), and the cap bound \(J<1/10\). It also closes
   the separate outer-\(B\)/lower-shelf endpoint.

No ratio ladder, theorem family indexed by \(B\) or \(j\), new chamber, or
compact certificate is introduced below. The reduction is a single
intrinsic continuous inequality.

Throughout,

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
 \qquad b_a(z)=\frac1\pi\arccos\frac za,
\]

\[
 A(z)=G_K(z)-G_\mu(z),\qquad x=r+p,\qquad q=x+m,
 \qquad \mu=q+1,
\]

\[
 K=\mu\sec t,\qquad 0<t<\frac\pi2,
 \qquad d=1-\frac{2t}{\pi},
 \qquad \zeta=\frac d{1-d}=\frac\pi{2t}-1,
\]

\[
 W=G_K(\mu)=\frac\mu\pi(\tan t-t),\qquad
 v=G_K(q),\qquad h=G_\mu(q),
\]

and

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 a_p=\frac{p^2}{3(2r+p)},\qquad
 \beta=\frac1\pi\arccos\frac qK.
\]

The inherited grid ranges are \(r\geq1\) on the integer grid and
\(r\geq3/2\) on the half-integer grid. In both cases \(p,m\geq1\). The
residual sector has

\[
 p\geq3,\qquad q\geq5,\qquad p>dm.
\tag{0.1}
\]

At the one-sided outer wall,

\[
 v=B-\frac14=B_0+\frac34,
 \qquad B_0=B-1\geq1,
\tag{0.2}
\]

where \(B\) is the gap-side label. The literal strict bracket at the wall is
\(B-1\). At \(\alpha\uparrow1^-\), these labels are retained; the endpoint
is not relabelled as an \(\alpha=0\) point in the next chart.

## 1. Exact selected scalar at the endpoint

Round 39 gives the exact selected-scalar identity

\[
 \boxed{
 \Gamma_{\rm OB}=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +p\Delta+a_pM_4+2pe_p-\frac{p-dm}{2}.}
\tag{R40.1}
\]

Here

\[
 \Delta=A(r)-A(x),
\]

\(\Omega_-\geq0\) is the complete old-level reserve, \(M_4\geq0\), and
\(e_p\geq0\). Formula (R40.1) is exact for the selected projection. The
earlier losses between the shifted defect, \(\Phi_\delta^+\), and
\(\Gamma_{\rm OB}\) remain exactly those recorded in Rounds 37--39.

The Round 39 cap proof remains valid at the one-sided endpoint:

\[
 \boxed{J<\frac1{10}.}
\tag{R40.2}
\]

Indeed, at \(\mu=q+1\), monotonicity gives
\(J=2I_{q+1}(q)\leq2I_6(5)<1/10\).

## 2. A midpoint lower bound for the exact radial action

Define on \((0,\mu)\)

\[
 \mathcal D(z):=b_K(z)-b_\mu(z).
\tag{2.1}
\]

### Lemma 2.1 (strict midpoint convexity)

The function \(\mathcal D\) is strictly increasing and strictly convex:

\[
 \mathcal D'(z)=\frac1\pi
 \left(\frac1{\sqrt{\mu^2-z^2}}-
       \frac1{\sqrt{K^2-z^2}}\right)>0,
\tag{2.2}
\]

\[
 \mathcal D''(z)=\frac z\pi
 \left((\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}\right)>0.
\tag{2.3}
\]

Consequently, with

\[
 y=r+\frac p2,
\tag{2.4}
\]

one has

\[
 \boxed{\Delta>p\mathcal D(y).}
\tag{R40.3}
\]

#### Proof

Since \(K=\mu\sec t>\mu\), both signs in (2.2)--(2.3) are strict. Also

\[
 A'(z)=b_\mu(z)-b_K(z)=-\mathcal D(z),
\]

and hence

\[
 \Delta=A(r)-A(x)=\int_r^x\mathcal D(z)\,dz.
\]

Strict Hermite--Hadamard midpoint convexity on the interval of length
\(p>0\) gives

\[
 \frac1p\int_r^x\mathcal D(z)\,dz>\mathcal D\!\left(\frac{r+x}{2}\right)
 =\mathcal D(y).
\]

This is (R40.3). \(\square\)

### Lemma 2.2 (root-free angular chord)

Put

\[
 \vartheta=\arccos\frac y\mu,
 \qquad
 \varphi=\arccos\frac yK
 =\arccos\left(\frac y\mu\cos t\right).
\]

Then \(0<\vartheta<\varphi<\pi/2\), and

\[
 \boxed{
 \mathcal D(y)>\delta_y:=
 \frac{y(1-\cos t)}{
 \pi\sqrt{\mu^2-y^2\cos^2t}}.}
\tag{R40.4}
\]

#### Proof

The mean-value theorem applied to cosine gives a
\(\xi\in(\vartheta,\varphi)\) such that

\[
 \cos\vartheta-\cos\varphi
 =\sin\xi\,(\varphi-\vartheta).
\]

The left side is \(y(1-\cos t)/\mu\). Since sine is strictly increasing on
\((0,\pi/2)\), \(\sin\xi<\sin\varphi\). Thus

\[
 \varphi-\vartheta>
 \frac{(y/\mu)(1-\cos t)}
 {\sqrt{1-(y/\mu)^2\cos^2t}}.
\]

Divide by \(\pi\). \(\square\)

Combining (R40.3)--(R40.4) gives the intrinsic exact-action payment

\[
 \boxed{p\Delta>p^2\delta_y.}
\tag{R40.5}
\]

Substitution in (R40.1) yields

\[
 \Gamma_{\rm OB}>\mathcal U_{\rm mid}:=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +p^2\delta_y+a_pM_4+2pe_p-\frac{p-dm}{2}.
\tag{R40.6}
\]

Only now discard the explicitly nonnegative reserves:

\[
 \boxed{
 \Gamma_{\rm OB}>\mathcal U_0:=
 \frac1{2\beta}-J+B_0\zeta+p^2\delta_y
 -\frac{p-dm}{2}.}
\tag{R40.7}
\]

This route starts from the exact \(\Gamma_{\rm OB}\) identity. It does not
replace or silently combine the distinct Round 39 losses in
\(F_{\rm OB}\).

## 3. Count interpolation and the single continuous target

Set

\[
 N:=\mu-y=\frac p2+m+1,
 \qquad \rho:=\frac N\mu\in(0,1),
 \qquad L_0(t):=\frac{\tan t-t}{\pi}.
\tag{3.1}
\]

Then

\[
 \delta_y=
 \frac{(1-\rho)(1-\cos t)}
 {\pi\sqrt{1-(1-\rho)^2\cos^2t}}.
\]

Moreover,

\[
 \begin{aligned}
 &\sin^2t+2\rho-
 \{1-(1-\rho)^2\cos^2t\}\\
 &\hspace{2cm}=\rho\{2\sin^2t+\rho\cos^2t\}>0.
 \end{aligned}
\]

Therefore

\[
 \boxed{
 \delta_y>C(\rho,t):=
 \frac{(1-\rho)(1-\cos t)}
 {\pi\sqrt{\sin^2t+2\rho}}.}
\tag{R40.8}
\]

On the outer wall,

\[
 W=B_0+\frac34-u.
\tag{3.2}
\]

At \(\alpha=1\),

\[
 u=G_K(q)-G_K(q+1)=\int_q^{q+1}b_K(z)\,dz
 <b_K(q)=\beta<\frac12.
\]

Thus

\[
 \boxed{W>B_0+\frac14\geq\frac54.}
\tag{R40.9}
\]

The two inequalities \(B_0\geq1\) and \(B_0>W-3/4\) can be interpolated
without a count split. For every \(0<k\leq1\),

\[
 B_0>(1-k)+k\left(W-\frac34\right)
 =kW+1-\frac{7k}{4}.
\tag{3.3}
\]

Take the fixed intrinsic weight \(k=1/4\). Then

\[
 \boxed{B_0>\frac W4+\frac9{16}.}
\tag{R40.10}
\]

Using \(1/(2\beta)>1\), (R40.2), (R40.8), (R40.10), and
\(W=\mu L_0(t)\), equation (R40.7) gives

\[
 \boxed{\Gamma_{\rm OB}>\mathcal R(\mu,p,m,t),}
\tag{R40.11}
\]

where

\[
 \boxed{
 \begin{aligned}
 \mathcal R(\mu,p,m,t):={}&
 \frac9{10}+\frac9{16}\zeta
 +\frac14\zeta\mu L_0(t)\\
 &+p^2 C\!\left(\frac{p/2+m+1}{\mu},t\right)
 -\frac{p-dm}{2}.
 \end{aligned}}
\tag{R40.12}
\]

### Lemma 3.1 (elimination of the outer radius)

For fixed \((p,m,t)\), \(\mathcal R\) is strictly increasing in \(\mu\).
Every feasible endpoint satisfies

\[
 \mu\geq p+m+2,
 \qquad
 \mu>\frac5{4L_0(t)}.
\tag{3.4}
\]

Consequently it is sufficient to prove the single continuum sign

\[
 \boxed{\mathcal R_*(p,m,t)>0,}
\tag{R40.13}
\]

where

\[
 \boxed{
 \mathcal R_*(p,m,t):=
 \mathcal R\!\left(
 \max\left\{p+m+2,\frac5{4L_0(t)}\right\},p,m,t
 \right).}
\tag{R40.14}
\]

The domain of this target is

\[
 p\geq3,\qquad m\geq1,\qquad p>dm,
 \qquad 0<t<\frac\pi2.
\tag{R40.15}
\]

#### Proof

Write \(A_t=(1-\cos t)/\pi>0\) and \(S_t=\sin^2t\). Direct
differentiation gives

\[
 \frac{\partial C}{\partial\rho}
 =-A_t\frac{S_t+\rho+1}{(S_t+2\rho)^{3/2}}<0.
\tag{3.5}
\]

Since \(\rho=N/\mu\) decreases strictly with \(\mu\), the \(C\)-term in
(R40.12) increases strictly with \(\mu\). The term
\(\zeta\mu L_0/4\) also increases strictly. This proves monotonicity.

The first inequality in (3.4) is \(\mu=r+p+m+1\geq p+m+2\). The second
is (R40.9) and \(W=\mu L_0\). Monotonicity then proves the reduction to
(R40.13)--(R40.14). \(\square\)

Equation (R40.13) is a proof target, not a proved sign and not a new
permanent certificate.

## 4. Exact two-branch convex reduction

The maximum in (R40.14) has two analytic branches. This is the ordinary
two-line evaluation of one continuous maximum, not a ratio-, count-, or
floor-indexed theorem family.

Put

\[
 L(t):=\zeta L_0(t),\qquad
 A_t:=\frac{1-\cos t}{\pi},\qquad
 S_t:=2+\sin^2t.
\tag{4.1}
\]

### 4.1. Geometric branch

Suppose

\[
 (p+m+2)L_0(t)\geq\frac54.
\tag{4.2}
\]

Then \(\mu_*=p+m+2\). Put

\[
 a:=\frac{p/2+1}{p+m+2}=1-\rho.
\tag{4.3}
\]

The conditions \(m\geq1\), (4.2), and \(p>dm\) become

\[
 a_h<a\leq a_I^+,
\tag{4.4}
\]

where

\[
 a_h=\frac{d(p+2)}{2\{p+d(p+2)\}},
\tag{4.5}
\]

\[
 a_I^+=\min\left\{
 \frac{p+2}{2(p+3)},\frac{2(p+2)L_0(t)}5
 \right\}.
\tag{4.6}
\]

Substitution of

\[
 m=\frac{p+2}{2a}-p-2
\]

in (R40.12) gives the exact branch formula

\[
 \boxed{
 \begin{aligned}
 \mathcal R_I(p,t,a)={}&
 \frac9{10}+\frac9{16}\zeta
 -\frac{p(1+d)}2-d\\
 &+\frac{X_I}{a}
 +\frac{p^2A_ta}{\sqrt{S_t-2a}},
 \end{aligned}}
\tag{R40.16}
\]

with

\[
 X_I=\frac{(p+2)\{L(t)+2d\}}8.
\tag{4.7}
\]

The \(a\)-dependent part is strictly convex. Indeed,

\[
 \frac{d}{da}\left(
 \frac{X_I}{a}+\frac{p^2A_ta}{\sqrt{S_t-2a}}
 \right)
 =-\frac{X_I}{a^2}
 +p^2A_t\frac{S_t-a}{(S_t-2a)^{3/2}},
\tag{4.8}
\]

\[
 \frac{d^2}{da^2}\left(
 \frac{X_I}{a}+\frac{p^2A_ta}{\sqrt{S_t-2a}}
 \right)
 =\frac{2X_I}{a^3}
 +p^2A_t\frac{2S_t-a}{(S_t-2a)^{5/2}}>0.
\tag{R40.17}
\]

Thus the branch minimum is at the unique root of (4.8), clamped to the
interval (4.4). This removes \(m\) without an integer or ratio subdivision.

### 4.2. Phase branch

Suppose

\[
 (p+m+2)L_0(t)<\frac54.
\tag{4.9}
\]

Put

\[
 \mu_0=\frac5{4L_0(t)},
 \qquad
 a:=1-\frac{p/2+m+1}{\mu_0}.
\tag{4.10}
\]

The exact interval is

\[
 a_{II}^-<a\leq a_{II}^+.
\tag{4.11}
\]

For lower-bound minimization we use its closure
\([a_{II}^-,a_{II}^+]\), where

\[
 a_{II}^-=
 \max\left\{
 0,\frac{p/2+1}{\mu_0},
 1-\frac{p(1+d/2)+d}{d\mu_0}
 \right\},
\tag{4.12}
\]

\[
 a_{II}^+=1-\frac{p/2+2}{\mu_0}.
\tag{4.13}
\]

In particular, \(0<a\leq a_{II}^+<1\), so
\(S_t-2a>0\) throughout the phase branch.

The third term in (4.12) is the hard inequality \(p>dm\). The geometric
entry is also strict because (4.9) is strict; Branch I owns the equality
seam. Passing to the closure can only decrease the infimum. Substitution of

\[
 m=\mu_0(1-a)-\frac p2-1
\]

gives

\[
 \boxed{
 \begin{aligned}
 \mathcal R_{II}(p,t,a)={}&
 \frac9{10}+\frac78\zeta+\frac{d\mu_0}{2}
 -\frac{p(2+d)}4-\frac d2\\
 &+\frac{p^2A_ta}{\sqrt{S_t-2a}}
 -\frac{d\mu_0a}{2}.
 \end{aligned}}
\tag{R40.18}
\]

Again the \(a\)-dependent part is strictly convex:

\[
 \frac d{da}\left(
 \frac{p^2A_ta}{\sqrt{S_t-2a}}-
 \frac{d\mu_0a}{2}
 \right)
 =p^2A_t\frac{S_t-a}{(S_t-2a)^{3/2}}
 -\frac{d\mu_0}{2},
\tag{4.14}
\]

\[
 \boxed{
 \frac {d^2}{da^2}\left(
 \frac{p^2A_ta}{\sqrt{S_t-2a}}-
 \frac{d\mu_0a}{2}
 \right)
 =p^2A_t\frac{2S_t-a}{(S_t-2a)^{5/2}}>0.}
\tag{R40.19}
\]

The two formulas agree on the seam
\((p+m+2)L_0=5/4\). Hence the final obstruction is a pair of convex
representations of one continuous scalar, not a seam gap.

## 5. Explicit weaker two-variable projections

The convex formulas already identify a rigorous route to a two-variable
sign check.

On branch I, let

\[
 D_h=\sqrt{S_t-2a_h}.
\]

For \(a\geq a_h\),

\[
 \frac{p^2A_ta}{\sqrt{S_t-2a}}
 \geq\frac{p^2A_ta}{D_h}.
\]

The resulting elementary convex function has minimizer

\[
 a_0=\sqrt{\frac{X_ID_h}{p^2A_t}},
\]

clamped to \([a_h,a_I^+]\). Substitution leaves one explicit inequality in
\((p,t)\).

On branch II, put

\[
 D_-=\sqrt{S_t-2a_{II}^-}.
\]

Then

\[
 \frac{p^2A_ta}{\sqrt{S_t-2a}}-\frac{d\mu_0a}{2}
 \geq a\left(\frac{p^2A_t}{D_-}-\frac{d\mu_0}{2}\right).
\]

The right side is minimized at \(a_{II}^-\) or \(a_{II}^+\) according to
the sign of its displayed coefficient. This also leaves one explicit
inequality in \((p,t)\).

For a future exact sign proof, all trigonometric quantities can be enclosed
without interval subdivision by the global bounds already used in Round 39,
together with

\[
 1-\cos t>\frac{t^2}{2}-\frac{t^4}{24},
 \qquad
 \sin t<t-\frac{t^3}{6}+\frac{t^5}{120}.
\tag{5.1}
\]

The refined tangent majorant from Round 39 gives, with \(s=1-d=2t/\pi\),

\[
 L_0(t)<\frac{121}{294}\frac{s^3}{1-s^2}.
\tag{5.2}
\]

Together with \(333/106<\pi<22/7\), these turn the weaker branch targets
into algebraic radical inequalities in \((p,d)\). Squaring only positive
quantities and eliminating the unique convex critical point is a plausible
single Sturm/resultant completion. That exact elimination has not been
performed in this round; no decimal margin below is promoted into its
place.

## 6. Loss and ownership ledger

| transition | type | retained or lost quantity |
|---|---|---|
| shifted defect to \(\Phi_\delta^+\) | inherited sufficient projection | unchanged from Rounds 28 and 37 |
| \(\Phi_\delta^+\) to \(\Gamma_{\rm OB}\) | inherited selected projection | Round 39 records the exact \(a_p\widehat\Xi\) reserve |
| (R40.1) to (R40.6) | strict midpoint/chord bound | loss is \(p\{\Delta-p\delta_y\}>0\) |
| (R40.6) to (R40.7) | nonnegative deletion | drops \(\Omega_-+a_pM_4+2pe_p\geq0\) only after printing it |
| (R40.7) to (R40.11) | strict cap/count/angular bound | uses \(J<1/10\), \(1/(2\beta)>1\), (R40.8), and fixed \(k=1/4\) |
| (R40.12) to (R40.14) | monotone elimination | retains exact \(p,m,t\) correlation and both lower bounds on \(\mu\) |
| branch formulas to Section 5 | optional weaker projection | exact loss is the displayed denominator replacement; no sign is claimed |

In particular,

\[
 \Gamma_{\rm OB}-\mathcal U_0
 =p\Delta-p^2\delta_y+\Omega_-+a_pM_4+2pe_p>0.
\tag{6.1}
\]

The strictness comes already from midpoint convexity and the angular chord.

The ownership table is:

| locus | owner used here | status |
|---|---|---|
| outer-\(B\) wall | one-sided gap label \(B^+=B\); literal strict count is \(B-1\) | exact |
| upper alpha endpoint | \(\alpha\uparrow1^-\), \(\mu=q+1\), labels retained | exact one-sided limit |
| next chart's \(\alpha=0\) point | not used | distinct owner |
| lower-shelf/outer-\(B\) endpoint | Round 39 | already closed; not reproved |
| old inverse walls | retained in \(\Omega_-\) until its proved nonnegativity is invoked | no fractional term silently deleted |
| \(A(r+j)+1/4\in\mathbb Z\) | inherited one-sided action-floor label | equality is retained; the later deletion of \(e_p\geq0\) is wall-safe |
| \(r+j=\mu\) | inner turning wall | the midpoint interval is strictly below it because \(\mu-x=m+1>0\) |
| \(r+j=K\) | outer turning wall | likewise outside \([r,x]\), since \(x<\mu<K\); the inherited terminal reserve remains wall-safe |
| \(\mu-r\in\mathbb Z\) | upper-alpha endpoint, since \(\mu-r=p+m+1\) | owned as \(\alpha\uparrow1^-\), not reindexed as the next chart's \(\alpha=0\) point |

## 7. Diagnostic-only falsification report

All numerical statements in this section are theorem-design evidence only.
They use ordinary binary64 SciPy searches or noninterval multiprecision
replays. They do not prove a continuum sign.

The existing bounded upper-face dataset in
`computations/general_d_round39_outer_face_diagnostic.py` has 406 feasible
upper-alpha roots. On those roots the midpoint scalar (R40.7) had observed
minimum approximately

\[
 1.0298384740
\]

at \((r,p,m,B_0)=(1,3,1,1)\). A relaxed continuous search of
(R40.14), deliberately larger than the endpoint image, found no negative
value. In the final seeded \(80{,}000\)-point companion run, its observed
branch minima were about \(0.2701\) on branch I and \(0.4159\) on branch II.
None of these numbers is load-bearing.

The directed companion
`computations/general_d_round40_upper_face_diagnostic.py` separately tests
the exact and root-free Round 39 scalars and deliberately over-deleted
variants. In particular, the floor-free adjacent-action candidates

\[
 \begin{aligned}
 Q_{\rm exact}={}&\frac\pi{2\psi}-J+
 \left(v-\frac34\right)\zeta
 +pR_1\{A(x)-A(q)\}-\frac{p-dm}{2},\\
 Q_0={}&\frac\pi{2\psi}-J+
 \left(v-\frac34\right)\zeta
 +\frac{pP(\psi-a)}\pi-\frac{p-dm}{2},
 \end{aligned}
\tag{7.1}
\]

where

\[
 a=\arccos(q/\mu),\quad \psi=\pi\beta,\quad
 P=\frac{(U_r-U_x)U_q}{q},
\]

become negative on the fully relaxed family
\(v=7/4\), \(m=1\), \(r=n^6\), \(p=n^3\). Those points have
\(\Delta\gg1/2\) and fail the same-floor/hard-\(E\) conditions. This
rejects the two auxiliary universal lower targets only. It does not give a
negative \(\Gamma_{\rm OB}\), \(F_{\rm OB}\), shifted tail, CST value, or
Pólya defect. The midpoint payment is large and positive on the same
large-radius scale.

## 8. Symbolic replay

The companion
`computations/general_d_round40_upper_midpoint_replay.wl` checks:

1. the two derivatives of \(\mathcal D\);
2. the normalized angular denominator identity and its positive slack;
3. the count interpolation at general \(k\) and at \(k=1/4\);
4. the derivative sign formula for \(C(\rho,t)\);
5. both exact branch substitutions;
6. both convexity derivatives; and
7. the selected-scalar loss identity.

Mathematica owns no strict bracket, one-sided endpoint label,
Hermite--Hadamard strictness, or continuum sign.

## 9. Round 40 result and Gate A decision

### Proved in this note

1. The strict midpoint-convexity payment
   \(p\Delta>p^2\delta_y\).
2. Its root-free normalized form (R40.8).
3. The fixed, non-indexed count interpolation
   \(B_0>W/4+9/16\).
4. The strict implication
   \(\Gamma_{\rm OB}>\mathcal R(\mu,p,m,t)\).
5. Monotone elimination of \(\mu\) to the single intrinsic target
   \(\mathcal R_*>0\).
6. Exact convex reductions (R40.16) and (R40.18), including their seam.

### Still open

No analytic proof of

\[
 \mathcal R_*(p,m,t)>0
\]

on (R40.15) is claimed. Therefore the gap-side outer-\(B\),
\(\alpha\uparrow1^-\) endpoint remains open, as do the other unowned
one-level-gap faces and the high-floor CST.

### Gate decision

**Gate A remains active.** Exactly one intrinsic continuous sign remains,
and Sections 4--5 reduce it to convex two-variable algebraic targets without
a \(B\)-, \(j\)-, or ratio-indexed theorem family. The endpoint projection
has therefore not met the revised strategy's stop criterion.

The next proof attempt should perform the global rational enclosure and
single Sturm/resultant elimination indicated in Section 5. If that exact
sign is false, or if its proof requires forbidden count/ratio/chamber
proliferation, Gate A stops and Gate B must restore the exact shifted-tail
scalar \(\mathscr S\). No new compact certificate is authorized.
