# General dimension, Round 33: lower-\(Q\) hard-arc monotonicity and endpoint reduction

Date: 19 July 2026  
Status: analytic wall monotonicity proved; endpoint signs remain open

## 0. Scope and theorem boundary

Continue on the exact high-floor first-drop hard sector

\[
 f\geq2,\qquad p>d(t)m,\qquad
 0\leq E<E_*:=\frac12-\frac{d(t)m}{2p}<\frac12,
 \qquad d(t)=1-\frac{2t}{\pi},
\tag{0.1}
\]

with

\[
 x=r+p,\qquad q=x+m,\qquad
 \mu=q+\alpha,\qquad 0<\alpha<1,
 \qquad K=\mu\sec t.
\tag{0.2}
\]

This note treats only the open lower-\(Q\) wall

\[
 A(q)=\frac34.
\tag{0.3}
\]

It proves that the exact remainder gap

\[
 H(\mu):=E(\mu)-E_*(\mu)
\tag{0.4}
\]

is strictly decreasing as \(\mu\) increases along the wall, while the
same first-drop and activity cell remains feasible.  Consequently a
hypothetical hard component cannot terminate in the smooth lower-\(Q\)
interior: it persists to an included lower-shelf endpoint, an activity
endpoint, or the excluded limit \(\alpha\to1^-\).

This is not monotonicity of the complete projected scalar

\[
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*).
\]

Indeed, the lower-\(Q\) terminal term increases while the other pieces
move in opposing directions.  No endpoint sign, high-floor CST closure,
pointwise assembly, or all-dimensional theorem is asserted here.

## 1. Exact lower-\(Q\) geometry

Put

\[
 \phi=\arccos\frac q\mu,
 \qquad
 \psi=\arccos\frac qK,
 \qquad
 \kappa=\frac{dK}{d\mu}
 =\frac{\sin\phi}{\sin\psi}\in(0,1).
\tag{1.1}
\]

Let

\[
 W=G_K(\mu),\qquad
 h=G_\mu(q),\qquad
 v=G_K(q)=\frac34+h.
\tag{1.2}
\]

The outer phase is strictly larger than the inner phase on
\([q,\mu]\).  Hence

\[
 v-W=\int_q^\mu\frac{\arccos(z/K)}\pi\,dz
 >\int_q^\mu\frac{\arccos(z/\mu)}\pi\,dz=h,
\]

and therefore

\[
 \boxed{W<\frac34.}
\tag{1.3}
\]

At \(\alpha=0\), which is not part of the open wall, equality
\(W=3/4\) holds.  No lower bound of the form
\(3/4-t/\pi<W\) is used or valid here.

Since

\[
 W=\frac\mu\pi(\tan t-t),
\]

writing \(F(t)=\tan t-t\) gives

\[
 \boxed{\mu<\frac{3\pi}{4F(t)}.}
\tag{1.4}
\]

The exact first-drop action is retained.  If

\[
 e_p=A(x)+\frac14-f\geq0,
\]

then (0.3) gives

\[
 \boxed{A(x)-A(q)=f-1+e_p\geq1.}
\tag{1.5}
\]

This correlation is the input missing from the false bare-wall
projections discussed in Section 5.

## 2. Strict monotonicity of \(H=E-E_*\)

### 2.1 Wall derivatives

For \(z<q\), define

\[
 S_R(z)=\sqrt{1-\frac{z^2}{R^2}},
 \qquad
 D(z)=S_\mu(z)-\kappa S_K(z)>0.
\tag{2.1}
\]

The lower-\(Q\) transport identity is

\[
 \frac{dA(z)}{d\mu}=-\frac{D(z)}\pi.
\tag{2.2}
\]

Put

\[
 c=\cos t,\qquad a=1-\kappa c>0.
\tag{2.3}
\]

Differentiating \(c=\mu/K\) along the wall yields

\[
 -\tan t\,t'=\frac1\mu-\frac\kappa K
 =\frac a\mu,
 \qquad
 \boxed{-t'=\frac{a}{\mu\tan t}.}
\tag{2.4}
\]

Within a fixed ordinary-floor cell,

\[
 E=A(r)+A(x)+\frac12-2f,
 \qquad
 E_*'=\frac{m}{p\pi}t'.
\]

Consequently

\[
 \boxed{
 \pi H'=-D(r)-D(x)+\frac mp\frac{a}{\mu\tan t}.}
\tag{2.5}
\]

The hard orientation \(p>dm\) gives

\[
 \frac mp<\frac1d.
\tag{2.6}
\]

It therefore suffices to prove

\[
 D(x)>\frac{a}{d\mu\tan t}.
\tag{2.7}
\]

### 2.2 Exact factorization at \(x\)

Set

\[
 U_z=\sqrt{\mu^2-z^2},
 \qquad
 V_z=\sqrt{\mu^2-c^2z^2}.
\tag{2.8}
\]

Equation (1.1) is equivalently \(\kappa=U_q/V_q\), and

\[
 D(z)=\frac{U_z-\kappa V_z}{\mu}.
\tag{2.9}
\]

The wall relation gives the exact algebraic identity

\[
 U_z^2-\kappa^2V_z^2
 =(1-\kappa^2c^2)(q^2-z^2)
 =a(1+\kappa c)(q^2-z^2).
\tag{2.10}
\]

Rationalizing (2.9) at \(z=x\) therefore gives

\[
 D(x)=
 \frac{a(1+\kappa c)(q^2-x^2)}
 {\mu(U_x+\kappa V_x)}.
\tag{2.11}
\]

Since \(U_x<V_x\), \(0<\kappa<1\), and

\[
 2(1+\kappa c)-(1+\kappa)
 =1-\kappa+2\kappa c>0,
\]

we obtain the strict lower bound

\[
 \boxed{
 D(x)>
 \frac{a(q^2-x^2)}{2\mu V_x}.}
\tag{2.12}
\]

### 2.3 The retained action forces a radial gap

The shell slope has the exact integral representation

\[
 \begin{aligned}
 \sigma(z)
 &:=-A'(z)
 =\frac1\pi\left{
 \arccos\frac{cz}{\mu}-\arccos\frac z\mu\right}\\
 &=\frac1\pi\int_c^1
 \frac{z/\mu}{\sqrt{1-s^2z^2/\mu^2}}\,ds
 <\frac{(1-c)z}{\pi U_z}.
 \end{aligned}
\tag{2.13}
\]

Combining (1.5) and (2.13) gives

\[
 1\leq\int_x^q\sigma(z)\,dz
 <\frac{1-c}{\pi}(U_x-U_q),
\]

so

\[
 \boxed{U_x-U_q>\frac\pi{1-c}.}
\tag{2.14}
\]

Using

\[
 q^2-x^2=(U_x-U_q)(U_x+U_q)
\]

in (2.12), it is enough to control \((U_x+U_q)/V_x\).  Now

\[
 V_x^2=\mu^2\sin^2t+c^2U_x^2.
\tag{2.15}
\]

Equations (1.4), (2.14), and (2.15) imply

\[
 \frac{U_x+U_q}{V_x}
 >\frac{U_x}{V_x}
 >\frac{4F(t)}
 {\sqrt{16c^2F(t)^2+9(1-c)^2\sin^2t}}
 >R(t),
\tag{2.16}
\]

where

\[
 R(t):=
 \frac{4F(t)}
 {\sqrt{16F(t)^2+9(1-c)^2\sin^2t}}.
\tag{2.17}
\]

### 2.4 Two elementary trigonometric inequalities

For \(0<t<\pi/2\),

\[
 \boxed{R(t)>\sin t.}
\tag{2.18}
\]

After squaring positive quantities, (2.18) is equivalent to

\[
 4(\sin t-t\cos t)
 >3(1-\cos t)\sin^2t.
\tag{2.19}
\]

Put \(u=\tan(t/2)\in(0,1)\).  The alternating estimate

\[
 \arctan u<u-\frac{u^3}{3}+\frac{u^5}{5}
\]

reduces the positive difference in (2.19), after multiplication by a
positive factor, to

\[
 P(u)=20-45u+32u^2+7u^4-2u^6+3u^8.
\]

Since \(-2u^6>-2u^2\),

\[
 P(u)>
 20-45u+30u^2+7u^4+3u^8>0.
\]

The quadratic has discriminant

\[
 45^2-4\cdot30\cdot20=-375<0,
\]

which proves (2.18).

The second inequality is

\[
 \boxed{
 \sin t>\frac{2(1-\cos t)}{\pi d(t)\tan t}.}
\tag{2.20}
\]

Indeed, put \(\varepsilon=\pi/2-t\).  Then (2.20) reduces to

\[
 \sin\varepsilon
 <\varepsilon(1+\sin\varepsilon),
\]

which follows strictly from \(0<\sin\varepsilon<\varepsilon\).

### 2.5 Conclusion

Equations (2.12), (2.14), (2.16), and (2.18) give

\[
 D(x)>
 \frac{a\pi}{2\mu(1-c)}R(t)
 >\frac{a\pi\sin t}{2\mu(1-c)}.
\]

Equation (2.20) now yields (2.7).  Combining this with (2.5)--(2.6)
and \(D(r)>0\) proves

\[
 \boxed{H'(\mu)<0.}
\tag{2.21}
\]

No grid relaxation or computer-assisted sign enters this proof.

## 3. Endpoint consequence

Assume a point on the open lower-\(Q\) wall is hard, so \(H<0\).
While the same first-drop and activity cell persists toward increasing
\(\mu\), (2.21) keeps \(H\) strictly negative.  Moreover \(E\geq0\), so
\(H<0\) forces \(E_*>0\), equivalently \(p>dm\).  Thus a separate
hard-orientation seam cannot terminate the component.

Round 30 already excludes inverse-spatial and outer-\(B\) intersections
from this open wall.  In the increasing-\(\mu\) direction, the remaining
exits are therefore:

\[
 \boxed{
 e_p=0,\qquad
 \text{the activity wall},\qquad
 \alpha\to1^-.}
\tag{3.1}
\]

This is an exact endpoint localization of any hypothetical hard component.
It does not say that \(\Psi^{L_T}_{4,E}\) decreases along the wall, and it
does not prove the signs at the three endpoint families in (3.1).

## 4. Equality and ownership audit

1. The lower-\(Q\) wall itself has literal strict ownership \(Q=0\);
   the theorem concerns the bad phase-right \(Q=1\) candidate.
2. The theorem assumes \(0<\alpha<1\).  At \(\alpha=0\), one has
   \(W=3/4\); at \(\alpha=1\), only the excluded one-sided limit is used.
3. The included ordinary lower shelf \(e_p=0\) is an endpoint, not part of
   the open segment after it is reached.
4. Equality \(E=E_*\) belongs to the already proved automatic sector.
   A hard component has strict \(H<0\).
5. Equality \(p=dm\) gives \(E_*=0\) and hence \(H=E\geq0\); it cannot be
   the endpoint of a continuously negative hard component.
6. Activity is not declared automatic on this \(0<y_1<\alpha<1\) wall.
   Its endpoint remains explicitly in (3.1).

## 5. Failure ledger for over-strong bare-wall targets

The exact first-drop action (1.5) cannot be dropped.  For example, take

\[
 r=p=m=1,\qquad \alpha=\frac12,
 \qquad q=3,\quad \mu=\frac72,
\]

and let \(t_Q\) be the unique lower-\(Q\) solution.  At \(t=\pi/4\),
monotonicity in the outer radius gives

\[
 A(3)<\frac{K-\mu}{\pi}
 =\frac{7(\sqrt2-1)}{2\pi}<\frac34.
\]

Thus \(t_Q>\pi/4\), and

\[
 E_* =\frac{t_Q}{\pi}>\frac14,
 \qquad
 g=\sqrt{\frac{15}{11}}-1<\frac14.
\]

Hence the bare implication \(g\geq E_*\) is false.  The same example also
has

\[
 \mathcal K_4
 =\frac{3(1-\cos t_Q)}{7\pi}
  +\frac{5(1-\cos^3t_Q)}{343\pi}
 <\frac17+\frac5{1029}
 =\frac{152}{1029}<\frac14<E_*.
\]

It is not a high-floor first-drop owner: numerically \(A(x)<7/4\).
It therefore falsifies only the projections that discard (1.5), not CST
or the exact lower-\(Q\) theorem.

The preferred Round 28 scalar continues to retain the actual endpoint sum
\(E\).  No replacement of \(E\) by \(g\), \(\mathcal K_4\), or a new
ratio owner is licensed by this round.

## 6. Mathematica replay

The companion file

`computations/general_d_round33_lowerQ_monotonicity_replay.wl`

checks the exact wall factorization, the half-angle residual, the polynomial
lower comparison, and the elementary endpoint substitutions.  It is an
identity replay, not a sign certificate.  Mathematica 15 should print

\[
 \texttt{round33LowerQMonotonicityReplayOK=True}.
\]

Reproduction:

    & 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' -file computations/general_d_round33_lowerQ_monotonicity_replay.wl

## 7. Gate decision

The smooth lower-\(Q\) hard arc now has a proof-level intrinsic
monotonicity and endpoint localization.  The next round should prove the
complete correlated sign on the union of the lower-shelf, activity, and
\(\alpha\to1^-\) exits, then return to the remaining \(\alpha=0\), higher
\(Q\), and simultaneous inverse/outer-\(B\) endpoint families.

No additional certificate is authorized.  High-floor CST and the
all-dimensional theorem remain open.
