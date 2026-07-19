# General dimension, Round 34: activity excision and correlated quadrature reduction

Date: 19 July 2026  
Status: activity is eliminated analytically; every lower-\(Q\) counterexample
is transported to the intrinsic \(Q\to1^-\) face and a finite stationary
alternative

## 0. Scope and theorem boundary

This note follows
`human/inbox/general-d_simplified_analytic_strategy.md`.  It keeps the exact
first-drop action and the preceding shelf variation in the same estimate.  It
introduces no ratio owner, no chamber certificate, and no new empirical
constant.

The setting is the high-floor first-drop branch

\[
 f\geq2,\qquad x=r+p,\qquad q=x+m,\qquad
 \mu=q+\alpha,\qquad 0<\alpha<1,
\tag{0.1}
\]

on the lower-\(Q\) wall

\[
 A(q)=\frac34,\qquad K=\mu\sec t,\qquad
 d=1-\frac{2t}{\pi}.
\tag{0.2}
\]

Put

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(x)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad
 \Delta=e_0-e_p=A(r)-A(x),\qquad
 E_*=\frac{p-dm}{2p}.
\tag{0.3}
\]

The automatic sector is \(p\leq dm\) or \(E\geq E_*\).  Thus the only
candidate considered below has

\[
 p>dm,\qquad 0\leq E<E_*.
\tag{0.4}
\]

The proved results are:

1. activity is automatic on every inherited high-floor first shelf, not just
   on (0.2);
2. an exact adjacent-action lemma retains the whole common radial parameter;
3. on (0.2), the implication \(\Delta>E_*\) is reduced first to (3.15), then
   rigorously to the face residual (3.30) and the stationary alternatives
   (3.33), (3.38).

The signs in the last line of (3.38) and on the \(z=z_0\) boundary are not
proved in this note.  Therefore lower-\(Q\), high-floor CST, pointwise
assembly, and the all-dimensional theorem remain open.

## 1. Activity is automatic on the whole high-floor first shelf

### 1.1 Statement and dependencies

Let

\[
 c=\frac\mu K=\cos t,\qquad
 \delta=K-\mu=K(1-c),
\]

and let \(\gamma=3/4\) on the integer inherited grid or \(\gamma=2\) on
the half-integer inherited grid.  On every high-floor first shelf,

\[
 \boxed{
 K^2-\frac{\pi^2}{(1-c)^2}-\gamma>\frac1{16}.}
\tag{1.1}
\]

The only dependencies are

\[
 x<\mu<K,\qquad
 \partial_R G_R(x)=\frac1\pi\sqrt{1-\frac{x^2}{R^2}},
\tag{1.2}
\]

and first-shelf ownership

\[
 A(x)\geq f-\frac14\geq\frac74.
\tag{1.3}
\]

No hard-sector, terminal, curvature, or lower-\(Q\) premise is used.

### 1.2 Proof

Equations (1.2)--(1.3) give, strictly,

\[
 \frac74\leq A(x)
 =\int_\mu^K\partial_R G_R(x)\,dR
 <\frac{K-\mu}{\pi}=\frac\delta\pi.
\tag{1.4}
\]

Hence \(\delta>7\pi/4\).  Since \(0<1-c<1\) and \(\gamma\leq2\),

\[
 \begin{aligned}
 K^2-\frac{\pi^2}{(1-c)^2}-\gamma
 &=\frac{\delta^2-\pi^2}{(1-c)^2}-\gamma\\
 &>\frac{33\pi^2}{16(1-c)^2}-\gamma\\
 &>\frac{33}{16}-2=\frac1{16}.
 \end{aligned}
\tag{1.5}
\]

This proves (1.1).  In particular, the activity equality cannot intersect
even the closure of a high-floor first-shelf cell.  The activity exit listed
in Round 33 is removed; its increasing-\(\mu\) list now contains only the
included lower shelf and \(\alpha\to1^-\).

## 2. Exact adjacent-action lemma

### 2.1 Statement

Put

\[
 U_z=\sqrt{\mu^2-z^2}.
\tag{2.1}
\]

Every lower-\(Q\) high-floor first-drop tuple satisfies

\[
 \boxed{
 \Delta>(f-1)\frac{U_r-U_x}{U_x-U_q}.}
\tag{2.2}
\]

This is an exact correlated comparison of the preceding shelf interval and
the terminal action interval.  It is not an independent curvature bound.

### 2.2 Proof

For \(c=\cos t\) and \(s\in[c,1]\), define

\[
 B_s(z)=\sqrt{\mu^2-s^2z^2}.
\tag{2.3}
\]

The shell slope is

\[
 \sigma(z)=-A'(z)
 =\frac1\pi\int_c^1\frac{z}{B_s(z)}\,ds.
\tag{2.4}
\]

Fubini therefore gives, for \(0<a<b<\mu\),

\[
 \int_a^b\sigma(z)\,dz
 =\frac1\pi\int_c^1
 \frac{B_s(a)-B_s(b)}{s^2}\,ds.
\tag{2.5}
\]

Let

\[
 R_s=\frac{B_s(r)-B_s(x)}{B_s(x)-B_s(q)}.
\tag{2.6}
\]

Rationalization gives

\[
 R_s=
 \frac{p(2r+p)}{m(2x+m)}
 \frac{B_s(x)+B_s(q)}{B_s(r)+B_s(x)}.
\tag{2.7}
\]

Direct differentiation gives

\[
 \frac{d}{ds}\log R_s
 =\frac{\mu^2}{sB_s(x)}
 \left(\frac1{B_s(r)}-\frac1{B_s(q)}\right)<0.
\tag{2.8}
\]

Thus \(R_s>R_1\) for \(c\leq s<1\).  Equation (2.5) says that
\(\Delta/(A(x)-A(q))\) is the positive weighted average of the \(R_s\).
On the lower-\(Q\) wall,

\[
 A(x)-A(q)=f-1+e_p\geq f-1.
\tag{2.9}
\]

Since \(R_1=(U_r-U_x)/(U_x-U_q)\), equations (2.5)--(2.9) prove
(2.2), strictly.

## 3. One correlated quadrature scalar for the remaining lower-\(Q\) face

### 3.1 Upper action and lower shelf quadratures

For fixed \(z\), the integrand in (2.4) is strictly convex as a function
of \(s\).  Hence the strict trapezoid inequality gives

\[
 \sigma(z)<\frac{1-c}{2\pi}z
 \left(\frac1{U_z}+\frac1{V_z}\right),
 \qquad
 V_z=\sqrt{\mu^2-c^2z^2}.
\tag{3.1}
\]

Consequently the retained action (2.9) implies

\[
 1\leq A(x)-A(q)
 <T:=\frac{1-c}{2\pi}
 \left\{U_x-U_q+\frac{V_x-V_q}{c^2}\right\}
\tag{3.2}
\]

The possible equality \(f=2,e_p=0\) occurs only in the weak left
inequality; the trapezoid comparison on the right remains strict.  More
generally, the left side may be replaced by \(f-1\).

A slightly stronger lower quadrature than the midpoint rule follows by
applying Jensen to the strictly convex function

\[
 y\longmapsto
 \frac{z/\mu}{\sqrt{1-yz^2/\mu^2}}
\]

and using

\[
 a^2=\frac1{1-c}\int_c^1s^2\,ds
 =\frac{1+c+c^2}{3}.
\tag{3.3}
\]

With

\[
 B_z=\sqrt{\mu^2-a^2z^2},
\]

one obtains

\[
 \sigma(z)>
 \frac{1-c}{\pi}\frac{z}{B_z},
\tag{3.4}
\]

and therefore

\[
 \boxed{
 \Delta>
 \frac{1-c}{\pi a^2}(B_r-B_x)
 =\frac{(1-c)p(2r+p)}{\pi(B_r+B_x)}.}
\tag{3.5}
\]

Both (3.2) and (3.5) come from the same radial-parameter integral (2.4).

### 3.2 Exact normalized domain

Normalize by \(\mu\):

\[
 z=\frac r\mu,\qquad P=\frac p\mu,\qquad
 M=\frac m\mu,\qquad X=z+P,\qquad Q=X+M<1.
\tag{3.6}
\]

Write

\[
 u(y)=\sqrt{1-y^2},\qquad
 v(y)=\sqrt{1-c^2y^2},\qquad
 b(y)=\sqrt{1-a^2y^2},
\tag{3.7}
\]

and

\[
 D=u(X)-u(Q)+\frac{v(X)-v(Q)}{c^2},
 \qquad F(t)=\tan t-t.
\tag{3.8}
\]

Equation (3.2) gives

\[
 \mu>\frac{2\pi}{(1-c)D}.
\tag{3.9}
\]

Round 33 proved

\[
 W=\frac{\mu F(t)}\pi<\frac34,
\tag{3.10}
\]

so

\[
 \mu<\frac{3\pi}{4F(t)}.
\tag{3.11}
\]

Combining (3.9)--(3.11) preserves their common scale and yields the strict
correlation

\[
 \boxed{3(1-c)D>8F(t).}
\tag{3.12}
\]

Also, both inherited grids have \(r\geq1\).  Combining this literal radial
lower bound with (3.11) gives

\[
 \boxed{z>\frac{4F(t)}{3\pi}.}
\tag{3.13}
\]

Finally, (3.5) and (3.9) imply

\[
 \boxed{
 \Delta>C(z,P,M,t):=
 \frac{2P(2z+P)}{\{b(z)+b(X)\}D}.}
\tag{3.14}
\]

Thus the lower-\(Q\) hard sector is empty if the following single intrinsic
inequality holds:

\[
 \boxed{
 C(z,P,M,t)>
 \frac{P-d(t)M}{2P}}
\tag{3.15}
\]

under exactly

\[
 \begin{gathered}
 0<t<\frac\pi2,\qquad z,P,M>0,\qquad z+P+M<1,\\
 P>d(t)M,\qquad
 3(1-\cos t)D>8(\tan t-t),\qquad
 z>\frac{4(\tan t-t)}{3\pi}.
 \end{gathered}
\tag{3.16}
\]

There are no floor variables, inverse roots, parity interpolation, raw scale,
or ratio-owner seams in (3.15)--(3.16).

For orientation only, one also has

\[
 0<D<1+\frac1{1+\sin t}<2.
\tag{3.17}
\]

Hence feasibility forces the elementary trigonometric restriction

\[
 4(\tan t-t)<3(1-\cos t).
\tag{3.18}
\]

### 3.3 Rigorous transport to the interface face

The four-variable scalar has one further exact monotonicity.  Put

\[
 \rho=\frac MP,\qquad
 h(y)=\frac{y}{b(y)},\qquad
 g(y)=\frac{y}{u(y)}+\frac{y}{v(y)}.
\tag{3.19}
\]

Then

\[
 N:=\int_z^Xh(y)\,dy,\qquad
 D=\int_X^Qg(y)\,dy,\qquad C=\frac{2N}{D}.
\tag{3.20}
\]

Fix \((t,z,\rho)\) and vary \(P\), so

\[
 X=z+P,\qquad Q=z+(1+\rho)P.
\tag{3.21}
\]

The hard target

\[
 \frac{P-dM}{2P}=\frac{1-d\rho}{2}
\]

is fixed under this motion.  Rationalization gives

\[
 N=\frac{P(X+z)}{b(z)+b(X)},
\tag{3.22}
\]

\[
 D=\rho P(X+Q)L,\qquad
 L=\frac1{u(X)+u(Q)}+\frac1{v(X)+v(Q)}.
\tag{3.23}
\]

Consequently

\[
 \begin{aligned}
 \frac{d}{dP}\log\frac DN
 ={}&\frac{2+\rho}{X+Q}-\frac1{X+z}
 +\frac{L'}L\\
 &-\frac{a^2X}{b(X)\{b(z)+b(X)\}}.
 \end{aligned}
\tag{3.24}
\]

The difference of the first two terms is

\[
 \frac{2z(1+\rho)}{(X+Q)(X+z)}>0.
\]

For \(k\in\{1,c\}\), put

\[
 w_k(y)=\sqrt{1-k^2y^2},\qquad
 L_k=\frac1{w_k(X)+w_k(Q)}.
\]

Direct differentiation and \(Q>X\) give

\[
 \frac{L_k'}{L_k}>
 \frac{Xk^2}{2(1-k^2X^2)}.
\tag{3.25}
\]

Now \(L_1>L_c\), and

\[
 y\longmapsto\frac{y}{1-X^2y}
\]

is increasing and convex.  Since

\[
 \frac{1+c^2}{2}\geq\frac{1+c+c^2}{3}=a^2,
\]

the weighted average defining \(L'/L\) satisfies

\[
 \frac{L'}L>
 \frac{a^2X}{2b(X)^2}
 >
 \frac{a^2X}{b(X)\{b(z)+b(X)\}},
\tag{3.26}
\]

where the last strict inequality uses \(b(z)>b(X)\).  Equations
(3.24)--(3.26) prove

\[
 \boxed{\frac{d}{dP}\log\frac DN>0,\qquad
 \frac{dC}{dP}<0.}
\tag{3.27}
\]

Meanwhile \(D=\int_X^Qg\) strictly increases with \(P\).  Therefore any
counterexample to (3.15) transports, at fixed \((t,z,\rho)\), to the
one-sided face

\[
 \boxed{Q\to1^-.}
\tag{3.28}
\]

The action condition (3.12) remains feasible during this transport.

On \(Q=1\), use \(X\) instead of \(\rho\).  Then

\[
 P=X-z,\qquad M=1-X,\qquad
 D_1(X)=u(X)+\frac{v(X)-\sin t}{c^2}.
\tag{3.29}
\]

The exact residual becomes

\[
 \boxed{
 \mathcal R(t,z,X)=
 \frac{2\{b(z)-b(X)\}}{a^2D_1(X)}
 -\frac{(1+d)X-z-d}{2(X-z)}.}
\tag{3.30}
\]

Put

\[
 z_0(t)=\frac{4(\tan t-t)}{3\pi},\qquad
 D_0(t)=\frac{8(\tan t-t)}{3(1-\cos t)},
\]

\[
 X_h(t,z)=\frac{z+d}{1+d}.
\tag{3.31}
\]

Since \(D_1\) is strictly decreasing, there is at most one
\(X_D(t)\) with \(D_1(X_D)=D_0\).  A transported candidate forces
\[
 D_0<D_1(0)=1+\frac1{1+\sin t},
\]
so this root exists and belongs to \((0,1)\).  If that existence inequality
fails, the transported domain is empty.  Every transported hard candidate
therefore lies in the exact domain

\[
 \boxed{
 z>z_0(t),\qquad X_h(t,z)<X<X_D(t).}
\tag{3.32}
\]

Thus the first unsupported sign is no longer the four-variable statement
(3.15): it is precisely

\[
 \boxed{\mathcal R(t,z,X)>0\quad\hbox{on (3.32)}.}
\tag{3.33}
\]

For theorem design only, and under the root-existence condition just stated,
the simultaneous boundary is explicit.  Let

\[
 S=\sin t,\qquad L_0=S+c^2D_0,
\]

\[
 U_D=
 \frac{\sqrt{L_0^2-S^4}-cL_0}{cS^2},\qquad
 X_D=\sqrt{1-U_D^2}.
\tag{3.34}
\]

Substituting \(z=z_0\) and \(X=X_D\) in (3.30) gives a one-variable
residual.  Positivity of that boundary residual alone is not yet sufficient:
one must first prove that (3.30) has no smaller interior value in \(z\) or
\(X\).

### 3.4 Exact stationary alternative in \(z\)

There is a final proof-level reduction of the \(z\)-dependence.  For fixed
\((t,X)\),

\[
 \mathcal R_z=
 -\frac{2z}{b(z)D_1}
 +\frac{d(1-X)}{2(X-z)^2}.
\tag{3.35}
\]

An interior stationary point therefore satisfies

\[
 \boxed{
 \frac{z(X-z)^2}{b(z)}
 =\frac{d(1-X)D_1}{4}.}
\tag{3.36}
\]

The derivative of the left side has the sign of

\[
 X-3z+2a^2z^3.
\tag{3.37}
\]

This expression starts positive, ends at
\(-2X(1-a^2X^2)<0\), and its derivative has at most one turn before an
endpoint value that is still negative.  Hence (3.37) crosses zero exactly
once.  The left side of (3.36) has one strict maximum, so (3.36) has at most
two roots.  When both exist, the first is a local maximum of
\(\mathcal R\) and the second is a local minimum.

The \(z\)-minimum on (3.32) is therefore reduced to exactly:

1. the radius boundary \(z=z_0(t)\);
2. the hard boundary \(z=(1+d)X-d\), where the right side of (3.30)
   vanishes and \(\mathcal R=C>0\); or
3. the unique second stationary root of (3.36).

At a stationary root, substitution of (3.36) gives the exact simpler
residual

\[
 \boxed{
 \mathcal R_{\rm stat}=
 \frac2{D_1}
 \left\{
 \frac{b(z)-b(X)}{a^2}
 +\frac{z(X-z)}{b(z)}
 \right\}
 -\frac12.}
\tag{3.38}
\]

Thus the remaining analytic work is sharply separated: prove
\(\mathcal R_{\rm stat}>0\) at the possible second root, then prove the
\(z=z_0\) boundary sign in \(X\).  This is an intrinsic stationary
alternative, not a parameter partition.

## 4. Equality-face audit

1. **Ordinary shelf wall.**  The wall \(e_p=0\) is included.  Equations
   (2.2), (3.2), and (3.5) remain strict because the radial-parameter
   comparisons are strict.
2. **Lower-\(Q\) wall.**  Literal strict-floor ownership assigns
   \(A(q)=3/4\) to \(Q=0\).  The continuous action identity (2.9) is the
   common one-sided wall value and is not rounded independently.
3. **Activity wall.**  It is disjoint from the complete high-floor first
   shelf by (1.1), including simultaneous shelf or terminal intersections.
4. **Hard walls.**  The face \(p=dm\) has \(E_*=0\), and the face
   \(E=E_*\) belongs to the automatic sector.  Equation (3.15) treats only
   their strict complement.
5. **Interface walls.**  The derivation assumes \(0<\alpha<1\), hence
   \(Q<1\).  The diagnostic limiting pattern \(Q\to1^-\) is not silently
   substituted as an owned \(\alpha=0\) point.
6. **Inherited grids.**  Only the common fact \(r\geq1\) is used in
   (3.13).  The half-integer grid actually has \(r\geq3/2\), so no parity
   interpolation or adverse extension to \(r=1/2\) occurs.
7. **Turning walls.**  All radii in (0.1) lie strictly below \(\mu\).
   Turning and zero-tail equality owners are unchanged.

## 5. Loss ledger

1. In (1.4), the factor \(\sqrt{1-x^2/R^2}\) is replaced by one.  The
   discarded integral is positive.  Equation (1.5) then replaces
   \(A(x),\gamma,(1-c)^2\) by their adverse allowed values; the exact
   reserve still exceeds \(1/16\).
2. Equation (2.2) discards \(e_pR_1\geq0\) only after the exact weighted
   average has been formed.
3. Equation (3.1) replaces the common radial-parameter integral by its
   strict trapezoid upper bound.  Equation (3.4) uses its Jensen lower
   bound with the exact second moment (3.3).  They are not worst-cased
   independently: the scale \(\mu\) is eliminated only after both are
   retained in (3.9)--(3.14).
4. Equation (3.10) uses only the proved direction \(W<3/4\).  No false
   lower bound for \(W\) is introduced.
5. Equation (3.13) uses the weaker common radius \(r\geq1\), discarding the
   extra half-grid reserve.

No terminal fraction, actual \(E\), or branching bonus is discarded in order
to assert a final theorem: the face and stationary signs (3.33), (3.38) are
explicitly still open.

## 6. Counterexample search and theorem-design diagnostics

The exact full-owner tuple

\[
 (r,p,m,\alpha)=\left(1,21,17,\frac{11}{100}\right),\qquad q=39,
\tag{6.1}
\]

has lower-\(Q\) root

\[
 t=0.538423011584849\ldots,
\]

and is a literal \(f=2\) first-drop owner.  It gives

\[
 E_*=0.233978630862725\ldots,
\]

while the older elasticity projections fail:

\[
 s-1=0.209106786371297\ldots<E_*,
\]

\[
 (s-1)(A(x)-W)=0.212834527231817\ldots<E_*.
\tag{6.2}
\]

The new correlated quadrature scalar retains a positive reserve at the same
tuple:

\[
 C=0.275302450145112\ldots>E_*.
\tag{6.3}
\]

Thus (6.1) is a scope regression against returning to elasticity alone; it
does not falsify (3.15).

A non-rigorous differential-evolution search on the continuous domain
(3.16) found no violation.  Its smallest observed value was

\[
 C-E_*\approx0.014074
\]

near

\[
 z\approx0.038662,\quad P\approx0.496526,\quad
 M\approx0.464811,\quad t\approx0.614416,\quad Q\to1^-.
\tag{6.4}
\]

Both inequalities in (3.12)--(3.13) were nearly active.  This is
theorem-design evidence only and is not a proof premise or a proposed
universal margin.

At possible second stationary roots of (3.36), a separate diagnostic search
found

\[
 \mathcal R_{\rm stat}\gtrsim0.175
\]

near \(t\approx0.531,z\approx0.260,X\approx0.706\).  This is again only a
guide to the next analytic estimate; it is not a promoted lower bound.

## 7. Exact failure report and gate decision

The four-variable sign (3.15) has now been transported rigorously to (3.33).
After the exact \(z\)-critical-point analysis, the unsupported alternatives
are precisely:

1. \(\mathcal R_{\rm stat}>0\) at the possible second root of (3.36);
2. \(\mathcal R(t,z_0(t),X)>0\) for
   \(X_h(t,z_0)<X<X_D(t)\).

The hard \(z=(1+d)X-d\) endpoint is already strictly positive.  The extremal
pattern (6.4) says that a successful proof of the two surviving alternatives
must preserve simultaneously:

- the action-to-interface scale relation (3.12);
- the literal inner-radius relation (3.13);
- the hard excess \(P-dM\); and
- the same radical sums in \(C\) and \(D\).

Worst-casing any of these separately recreates the loss exhibited by (6.2).
The next analytic pass should prove the stationary sign and the
\(z=z_0\) boundary sign, using the adjacent-action lemma where it is stronger.
Only after an analytic \(X\)-reduction may the simultaneous boundary in (6.4)
be treated as a one-variable target.  If this intrinsic proof fails, the
revised strategy requires moving to the weighted aggregate \(WT\), not adding
a ratio ladder or a second pointwise certificate.

## 8. Mathematica replay

The companion file

`computations/general_d_round34_activity_and_quadrature_replay.wl`

checks the activity identity, the exact rational reserve, both convexity
derivatives, the quadrature primitives, rationalization of (3.5), the
scale-elimination identity behind (3.12), the transport derivatives, the
\(Q=1\) residual identities, and the quadratic defining \(X_D\).  It is a
symbolic replay, not a sign certificate.  Mathematica 15 prints

```text
activityMarginIdentityResidual=0
rationalGap=1/16
safeGapUsingPiGreater1=1/16
adjacentActionLogDerivativeResidual=0
quadraturePrimitiveResiduals={0, 0, 0, 0}
normalizedCorrelationResidual=0
transportIdentityResiduals={0, 0, 0}
qOneResiduals={0, 0}
xDRootPolynomialResidual=0
round34ActivityAndQuadratureReplayOK=True
```

Reproduction:

```powershell
wolframscript -file computations/general_d_round34_activity_and_quadrature_replay.wl
```
