# General-dimensional spherical-shell Pólya project
## Round 46 clean-room derivation for (R45.18)

**Date:** 21 July 2026  
**Role:** Prompt B clean-room analytic reviewer  
**Freeze boundary:** Sections 1--5 below were written before reading any
Round-46 lead or adversarial artifact. They are frozen for later comparison.

## 1. Independence boundary, preflight, and exact owner

### 1.1 Sources and repository gate

Before this freeze I read only the seven sources authorized by Prompt B:

```text
state/proof_obligations.yml
human/inbox/general-d_simplified_analytic_strategy.md
human/current_directives.md
human/outbox/general-d-round-42-stronger-upper-alpha-phi-specialization.md
human/outbox/general-d-round-44-independent-audit.md
human/outbox/general-d-round-45-independent-audit.md
computations/general_d_round45_independent_support_search.py
```

I did not read a Round-46 lead, adversarial, replay, diagnostic, or draft
clean-room output. No parameter search was performed. One exact symbolic
expansion used below was checked with the installed Mathematica runtime; the
expanded identity is printed, so the runtime is not a proof premise.

The repository gate at the start of this derivation was

```text
branch: codex/general-d-round-46-r45-18-complete-owner
HEAD:   3ad6a78d9cb2b81d316bcf0c171ad7cce9f4fee1
state/proof_obligations.yml SHA-256:
a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4
SHELL-general-d-high-floor-first-drop-CST: open
```

The proof graph's `next_action` text still describes the older Round-37
route. Its status is authoritative, while the later audited Round-45
directive controls this local task. This is a narrative conflict only.

### 1.2 Complete fixed owner

Set

\[
 x=r+p,\qquad q=x+m,\qquad \mu=q+1,\qquad
 K=\mu\sec t,\qquad 0<t<\frac\pi2,
\]

\[
 d_\rho=1-\frac{2t}{\pi},\qquad
 \zeta=\frac\pi{2t}-1,
\]

and

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,
 \qquad A=G_K-G_\mu.
\]

The two inherited grids and radial bounds are

\[
 r\in\mathbb N,\ r\ge1,
 \qquad\hbox{or}\qquad
 r\in\mathbb N_0+\frac12,\ r\ge\frac32,
\]

with \(p,m\in\mathbb N\), \(p\ge3\), and \(q=r+p+m\ge5\).
The fixed one-sided upper-\(\alpha\), outer-\(B\) owner has

\[
 G_K(q)=B_0+\frac34,\qquad B_0=B-1=Q\ge1.
\tag{CR46.1}
\]

The symbol \(B\) is the old-chart one-sided label. The literal strict count
at (CR46.1) is \(B_{\rm lit}=B_0\), not \(B\). Put

\[
 h=G_\mu(q),\qquad W=G_K(\mu),\qquad
 v=B_0+\frac34,\qquad u=v-W,
\]

\[
 \beta=\frac1\pi\arccos\frac qK,
 \qquad 0<h<u<\beta<\frac12.
\tag{CR46.2}
\]

On the common first shelf let \(f\) be the literal ordinary floor and write

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(x)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p=A(r)-A(x),
 \qquad j=f-B\ge0.
\]

The literal first drop, both strict grids, fixed inverse side vector, all
inherited action/branch conditions, and the dimension-labelled strict
activity inequality remain imposed. In particular,

\[
 p-d_\rho m>\frac{11}{5},\qquad
 0\le E<E_*<\frac12,
 \qquad E_*:=\frac{p-d_\rho m}{2p}.
\tag{CR46.3}
\]

Activity equality belongs to the no-mode owner. The endpoint is evaluated
at \(\mu=q+1\) with the old chart's label
\(\alpha\uparrow1^-\); it is not relabelled as a next-chart
\(\alpha=0\) point. On this fixed owner only,

\[
 \boxed{A(x)-A(q)=j+e_p+h.}
\tag{CR46.4}
\]

No use below transports (CR46.4) across an ordinary-floor wall.

### 1.3 Literal target and its logical strength

Define

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 R_1=\frac{U_r-U_x}{U_x-U_q}>0,
\]

\[
 J=2\int_q^\mu G_\mu(z)\,dz.
\]

The clean-room right-minus-left margin is

\[
\boxed{
\begin{aligned}
\mathcal M={}&pR_1\{A(x)-A(q)\}
+\frac{\pi^2B_0}{Kt^3\sin t}
 \left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)\\
&+B_0\zeta+\frac9{16\beta}-J
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
 \left(\frac1{\sqrt{\mu^2-r^2}}
       -\frac1{\sqrt{K^2-r^2}}\right)
-\frac{p-d_\rho m}{2}.
\end{aligned}}
\tag{CR46.5}
\]

Thus (R45.18) is exactly \(\mathcal M\ge0\). It is a sufficient
condition for positivity of the exact unprojected support scalar; it is not
an identity equivalent to that scalar.

## 2. Exact normalization to \((q,p,m,t,B_0)\)

### 2.1 The outer wall and its unique root

Introduce the outer angle

\[
 \gamma:=\arccos\frac qK=\pi\beta.
\]

Since \(K\cos\gamma=q\), the wall (CR46.1) is exactly

\[
 \boxed{q(\tan\gamma-\gamma)=\pi v,
 \qquad v=B_0+\frac34.}
\tag{CR46.6}
\]

It also gives

\[
 K=q\sec\gamma=(q+1)\sec t,
 \qquad
 \boxed{\cos t=\frac{q+1}{q}\cos\gamma.}
\tag{CR46.7}
\]

For fixed \((q,B_0)\), the function
\(\gamma\mapsto q(\tan\gamma-\gamma)\) has derivative
\(q\tan^2\gamma>0\), starts at zero, and tends to infinity as
\(\gamma\uparrow\pi/2\). Hence (CR46.6) has exactly one
\(\gamma\in(0,\pi/2)\).

Let \(\gamma_0=\arccos(q/(q+1))\). Then

\[
 h=\frac q\pi(\tan\gamma_0-\gamma_0)<\frac12<v.
\]

Consequently the wall root satisfies \(\gamma>\gamma_0\), so the right
side of (CR46.7) lies strictly in \((0,1)\) and determines one
\(t\in(0,\pi/2)\). Equivalently, at fixed \(q\),

\[
 \frac{\partial}{\partial t}
 G_{(q+1)\sec t}(q)
 =\frac{K\tan t\sin\gamma}{\pi}>0,
\]

and the endpoint values lie respectively below and above \(v\). This gives
the required wall-root uniqueness without a count or chamber split.

### 2.2 Closed formulas

The exact normalized quantities are

\[
 r=q-m-p,\qquad x=q-m,\qquad \mu=q+1,
 \qquad K=(q+1)\sec t,
\]

\[
 \beta=\frac1\pi
 \arccos\!\left(\frac{q\cos t}{q+1}\right),
\]

\[
 h=\frac{\sqrt{2q+1}
 -q\arccos(q/(q+1))}{\pi},
 \qquad
 W=\frac{q+1}{\pi}(\tan t-t),
\tag{CR46.8}
\]

and

\[
 R_1=
 \frac{
 \sqrt{(q+1)^2-(q-m-p)^2}
 -\sqrt{(q+1)^2-(q-m)^2}}
 {
 \sqrt{(q+1)^2-(q-m)^2}-\sqrt{2q+1}}.
\tag{CR46.9}
\]

An antiderivative needed for the cap is

\[
 \mathfrak I_a(z)=\frac{1}{4\pi}
 \left[
 3z\sqrt{a^2-z^2}+a^2\arcsin\frac za
 -2z^2\arccos\frac za
 \right],
 \qquad \mathfrak I_a'(z)=G_a(z).
\]

Therefore

\[
 \boxed{
 J=\frac{\bigl((q+1)^2+2q^2\bigr)
 \arccos(q/(q+1))-3q\sqrt{2q+1}}{2\pi}.}
\tag{CR46.10}
\]

For later differentiation, the action drop can be kept in the exact closed
form

\[
\begin{aligned}
\mathcal D:=A(x)-A(q)=\frac1\pi\bigl[&
 \sqrt{K^2-x^2}-\sqrt{\mu^2-x^2}
 -\sqrt{K^2-q^2}+\sqrt{\mu^2-q^2}\\
&-x\arccos(x/K)+x\arccos(x/\mu)\\
&+q\arccos(q/K)-q\arccos(q/\mu)
\bigr].
\end{aligned}
\tag{CR46.11}
\]

The other three exact payments in (CR46.5) are

\[
 \mathcal O=\frac{\pi^2B_0}{Kt^3\sin t}
 \left(\frac W2-\frac{B_0}{4}+\frac1{48}\right),
\]

\[
 \mathcal T=\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},
 \qquad
 \mathcal C=\frac{p^3}{6\pi}
 \left(\frac1{U_r}-\frac1{\sqrt{K^2-r^2}}\right).
\tag{CR46.12}
\]

Every displayed square root is positive because

\[
 0<r<x<q<\mu<K.
\]

The inverse trigonometric arguments lie strictly in \((0,1)\),
\(U_r>U_x>U_q>0\), and hence the denominator of (CR46.9) is positive.
Also \(t,\sin t,\beta,K\), and \(\sqrt{K^2-q^2}\) are nonzero. Finally,
from \(u<1/2\),

\[
 W=v-u>B_0+\frac14,
 \qquad
 \frac W2-\frac{B_0}{4}+\frac1{48}
 >\frac{B_0}{4}+\frac7{48}>0.
\tag{CR46.13}
\]

## 3. Route A: exact wall calculus

### 3.1 Wall derivatives

In this section a prime denotes \(d/dq\) at fixed symbolic
\((p,m,B_0)\) along the unique wall. From (CR46.6)--(CR46.7),

\[
 \boxed{
 \gamma'=-\frac{\tan\gamma-\gamma}{q\tan^2\gamma}<0,
 \qquad K'=\frac{\gamma}{\sin\gamma}>0,}
\tag{CR46.14}
\]

and

\[
 \boxed{
 t'=\frac{\gamma-\pi v}
 {q(q+1)\tan\gamma\tan t}<0.}
\tag{CR46.15}
\]

The last sign uses \(v\ge7/4\) and \(0<\gamma<\pi/2\). Therefore
\(\beta'<0\), \(d_\rho'=-2t'/\pi>0\), and

\[
 \zeta'=-\frac{\pi t'}{2t^2}>0.
\]

There are two further exact monotonicities. Write

\[
 u=\frac1\pi\int_0^1
 \arccos\frac{q+s}{K}\,ds.
\]

For the integrand angle \(\theta_s\),

\[
 \theta_s'=\frac{(q+s)K'-K}
 {K\sqrt{K^2-(q+s)^2}}<0,
\]

because even at \(s=1\),

\[
 \frac{(q+1)K'}K=\frac{(q+1)\gamma}{q\tan\gamma}<1
 \iff \pi v>\gamma.
\]

Thus \(u'<0\) and

\[
 \boxed{W'=-u'>0.}
\tag{CR46.16}
\]

Similarly, with
\(\phi_s=\arccos((q+s)/(q+1))\), differentiation under the fixed
interval gives

\[
 \boxed{
 J'=\frac2\pi\int_0^1(\sin\phi_s-\phi_s)\,ds<0.}
\tag{CR46.17}
\]

The top term is also increasing along the wall. Using
\(q(\tan\gamma-\gamma)=\pi v\),

\[
 \mathcal T=\frac{9\pi}{64v}
 \frac{1-\gamma\cot\gamma}{\gamma^3}.
\]

If \(H(\gamma)=(1-\gamma\cot\gamma)/\gamma^3\), then

\[
 H'(\gamma)=
 \frac{\gamma^2\csc^2\gamma+2\gamma\cot\gamma-3}{\gamma^4}<0.
\]

Indeed the opposite numerator after multiplication by \(\sin^2\gamma\)
is

\[
 3\sin^2\gamma-\gamma^2-2\gamma\sin\gamma\cos\gamma,
\]

whose derivative is
\(4\cos\gamma(\sin\gamma-\gamma\cos\gamma)>0\) and whose value at
zero is zero. Since \(\gamma'<0\), \(\mathcal T'>0\).

### 3.2 Exact derivative of the complete margin

For \(a\ge0\), define

\[
 U_a=\sqrt{2(a+1)q+1-a^2},
 \quad V_a=\sqrt{K^2-(q-a)^2},
\]

\[
 \theta_a=\arccos\frac{q-a}{K},
 \qquad \phi_a=\arccos\frac{q-a}{q+1},
 \qquad c=m+p.
\]

Thus \(U_c=U_r\), \(U_m=U_x\), \(U_0=U_q\), and

\[
 R_1=\frac{U_c-U_m}{U_m-U_0},\qquad
 U_a'=\frac{a+1}{U_a}.
\]

Consequently

\[
 R_1'=
 \frac{
 \left(\frac{c+1}{U_c}-\frac{m+1}{U_m}\right)(U_m-U_0)
 -(U_c-U_m)\left(\frac{m+1}{U_m}-\frac1{U_0}\right)}
 {(U_m-U_0)^2},
\tag{CR46.18}
\]

and direct differentiation of (CR46.11) yields

\[
\mathcal D'=\frac1\pi\left[
 K'(\sin\theta_m-\sin\theta_0)
 -(\theta_m-\theta_0)
 -(\sin\phi_m-\sin\phi_0)
 +(\phi_m-\phi_0)
\right].
\tag{CR46.19}
\]

Put

\[
 c_0=\frac{\pi^2}{Kt^3\sin t}
     =\frac{\pi^2}{(q+1)t^3\tan t},
 \qquad
 P=\frac W2-\frac{B_0}{4}+\frac1{48}.
\]

Then

\[
 \frac{c_0'}{c_0}=-\frac1{q+1}
 -t'\left(\frac3t+\frac1{\sin t\cos t}\right),
 \qquad P'=\frac{W'}2,
\tag{CR46.20}
\]

while

\[
 \mathcal C'=\frac{p^3}{6\pi}
 \left[-\frac{c+1}{U_c^3}
 +\frac{KK'-(q-c)}{V_c^3}\right].
\tag{CR46.21}
\]

Combining all exact derivatives gives

\[
\boxed{
\begin{aligned}
\mathcal M'={}&p(R_1'\mathcal D+R_1\mathcal D')
 +B_0(c_0'P+c_0W'/2)\\
&-\frac{B_0\pi t'}{2t^2}
 -\frac{9\pi\gamma'}{16\gamma^2}
 -J'+\mathcal T'+\mathcal C'
 -\frac{m t'}\pi.
\end{aligned}}
\tag{CR46.22}
\]

The second line except \(\mathcal C'\) is strictly positive. Equations
(CR46.18)--(CR46.21), however, do not give uniform signs for the correlated
action derivative, shelf-curvature derivative, or the full old-level factor.
The first unrepaired implication in Route A is therefore

\[
\boxed{
 p(R_1'\mathcal D+R_1\mathcal D')+\mathcal C'
 +B_0(c_0'P+c_0W'/2)
 \ge -\left(
 -\frac{B_0\pi t'}{2t^2}
 -\frac{9\pi\gamma'}{16\gamma^2}
 -J'+\mathcal T'-\frac{m t'}\pi
 \right).}
\tag{CR46.23}
\]

No authorized inherited lemma proves (CR46.23). Worst-casing its action,
cap, inverse aggregate, and shelf terms separately would violate the required
correlation. Thus exact wall calculus gives genuine wall directions but does
not prove monotonicity of the complete margin.

Moreover, (CR46.22) is used only on an open fixed-owner component. A shelf,
inverse, outer-count, or activity wall cannot be crossed by continuity of an
owner label. A global sign of (CR46.22) on the larger continuous geometric
domain would bypass that issue, but such a sign has not been obtained.

## 4. Route B and the audit ledgers

### 4.1 One correlated convexity/Jensen attempt

Fix \((q,m,t,B_0)\), put \(x=q-m\), and relax
\(p=x-r\) continuously inside one fixed owner component. Let

\[
 U=\sqrt{\mu^2-r^2},\qquad
 V_a(z)=\sqrt{a^2-z^2}.
\]

The action drop has the exact radius-integral representation

\[
 \mathcal D=\frac1\pi\int_\mu^K
 \frac{V_a(x)-V_a(q)}a\,da.
\]

Since

\[
 \frac{V_a(x)-V_a(q)}{U_x-U_q}
 =\frac{U_x+U_q}{V_a(x)+V_a(q)},
\]

we get the correlated identity

\[
 \frac{\mathcal D}{U_x-U_q}
 =\frac1\pi\int_\mu^K C_a\,da,
 \qquad
 C_a:=\frac{U_x+U_q}{a\{V_a(x)+V_a(q)\}}>0.
\tag{CR46.24}
\]

The curvature payment is simultaneously

\[
 \mathcal C=\frac{p^3}{6\pi}\int_\mu^K
 \frac{a}{(a^2-r^2)^{3/2}}\,da.
\tag{CR46.25}
\]

Thus the complete \(p\)-dependent geometric payment

\[
 \mathcal P(p)=pR_1\mathcal D+\mathcal C
\]

has the exact second derivative

\[
\boxed{
 \mathcal P''(p)=\frac1\pi\int_\mu^K
 \left[
 C_a\left(\frac{2r}{U}-\frac{p\mu^2}{U^3}\right)
 +\frac{paQ_a}{2(a^2-r^2)^{7/2}}
 \right]da,}
\tag{CR46.26}
\]

where, with \(D_a=a^2-r^2\),

\[
 Q_a=2D_a^2-6prD_a+p^2(a^2+4r^2)>0.
\]

The last sign is exact: as a quadratic in \(p\), its leading coefficient is
\(a^2+4r^2>0\) and its discriminant is

\[
 4D_a^2(r^2-2a^2)<0.
\]

Hence the shelf-curvature term is strictly convex. The action term changes
convexity at

\[
 p\mu^2=2r(\mu^2-r^2).
\]

If the left side does not exceed the right side, (CR46.26) is positive. In
the other case a successful Jensen closure requires the single correlated
kernel domination

\[
\boxed{
 C_a\left(\frac{p\mu^2}{U^3}-\frac{2r}{U}\right)
 \le \frac{paQ_a}{2(a^2-r^2)^{7/2}}
 \quad(\mu\le a\le K),}
\tag{CR46.27}
\]

or an integrated version of it.

There is nontrivial endpoint evidence for (CR46.27), obtained analytically.
At \(a=\mu\), multiply the difference of the right and left sides by the
positive factor \(2\mu U^7\), and put
\(s=m+1\), so \(\mu=r+p+s\). The result is

\[
\begin{aligned}
&p^3(p^4+2p^3r+10p^2r^2+30pr^3+25r^4)\\
&+4p^2(p+r)(p^3+2p^2r+15pr^2+21r^3)s\\
&+2p(3p^4+18p^3r+89p^2r^2+129pr^3+48r^4)s^2\\
&+4(p+r)(p^3+14p^2r+40pr^2+8r^3)s^3\\
&+(p^3+54p^2r+120pr^2+48r^3)s^4
 +24r(p+r)s^5+4rs^6>0.
\end{aligned}
\tag{CR46.28}
\]

At \(a\to\infty\), the integrand in (CR46.26) is

\[
 \frac{p+(U_x+U_q)(2r/U-p\mu^2/U^3)/2}{a^2}
 +O(a^{-4}),
\]

with positive leading coefficient. If the action bracket is negative, use
\(U_x+U_q<2U\) and

\[
 U^2=(p+s)(2r+p+s)>2pr
\]

to bound that coefficient strictly below by neither zero nor a discarded
constant, but strictly above

\[
 p+U\left(\frac{2r}{U}-\frac{p\mu^2}{U^3}\right)
 =r\left(2-\frac{pr}{U^2}\right)>0.
\]

The unresolved point is the interior \(\mu<a<K\). The endpoint-positive
kernel ratio has a derivative whose exact polynomial is not manifestly
one-signed under only the complete-owner inequalities. Proving (CR46.27),
or proving its integrated form without separating \(C_a\) from \(Q_a\), is
the first unrepaired implication in this Jensen route. Even a proof of
convexity would still require a uniform endpoint or stationary-point sign
for \(\mathcal P(p)-p/2\); no such sign is established here. Therefore
Route B does not remove a continuous degree of freedom or close (R45.18).

### 4.2 Dependency ledger

| item used | exact scope in this report | source and status |
|---|---|---|
| authoritative selected status | high-floor first-drop CST remains `open` | `state/proof_obligations.yml` |
| no ratio/count/chamber/second-certificate rule | controls both attempted routes | simplified analytic strategy and current directives |
| fixed upper-\(\alpha\), outer-\(B\) action relation | (CR46.4), strict adjacent-action input | audited Round 42 specialization as summarized by the Round 45 audit |
| exact literal Gate-B terminal and shelf ledger | owner labels, \(9/(16\beta)\), cap \(J\), shelf \(\mathcal C_p\) | Round 44 independent audit |
| old-level inverse curvature | \(7/48\) per old level | Round 45 independent audit |
| primary \(u\)-retaining \(\Omega_-\) bound | combined old-level term \(\mathcal O\) | Round 45 independent audit, inherited from Round 38 |
| top Bregman curvature | coefficient \(9/64\) | Round 44/45 independent audits |
| elementary shelf curvature | \(\mathcal C\) in (CR46.12) | Round 44/45 independent audits |
| Round-45 independent evaluator | notation and fixed-side owner definition only | diagnostic code; no numerical result used here |

No rejected scalar, global \(\alpha\)-monotonicity, count-free R45-CF
sign, ratio ladder, or finite certificate is used.

### 4.3 Loss ledger and no-double-counting audit

The exact literal starting identity is

\[
\begin{aligned}
\mathscr S={}&\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p+pE
-\frac{p-d_\rho m}{2}.
\end{aligned}
\tag{CR46.29}
\]

The route to (CR46.5) makes exactly these weakenings, in order.

| step | weakening | discarded term and sign |
|---:|---|---|
| 1 | \(\mathcal C_p\to\mathcal C\) | \(\mathcal C_p-\mathcal C\ge0\) |
| 2 | each exact old Bregman area \(\mathcal R_k\to7\pi^2/(48Kt^3\sin t)\) | sum of the old strong-convexity residuals, \(\ge0\) |
| 3 | exact literal top area \(\to\mathcal T\) | top Bregman residual, \(\ge0\) |
| 4 | exact \(\Omega_-\) to its primary \(u\)-retaining lower bound and combine it only with Step 2 | \(\Omega_- -\Omega_{\rm primary}\ge0\); this produces \(\mathcal O\) |
| 5 | \(pE\to pR_1\mathcal D\) | \(p(\Delta-R_1\mathcal D)+2pe_p>0\), by strict adjacent action and \(e_p\ge0\) |
| 6 | wall normalization and calculus | exact substitutions only; no loss |

The shelf hinge \(a_p\Delta\) is not added to the elementary shelf
curvature. Old unit intervals and the top interval are disjoint. The
\(1/(16\beta)\) term reconciles the gap-side and literal terminal ledgers;
it is not an additional reserve and is not present in (CR46.29). The newest
\(y_B=0\) event is not counted as an old inverse collision. Thus the hinge,
shelf curvature, old areas, top area, and terminal reconciliation each occur
at most once.

In particular,

\[
 \mathscr S>\mathcal M.
\tag{CR46.30}
\]

The strictness comes from Step 5. Therefore \(\mathcal M\ge0\), including
equality, would imply \(\mathscr S>0\). The converse is not valid.

### 4.4 Equality and strict-wall ledger

| face | fixed assignment and effect |
|---|---|
| \(A(r+s)+1/4\in\mathbb Z\) | literal ordinary-floor owner; do not continue (CR46.4) through the jump |
| \(G_K(q)+1/4=B\) | literal strict ball count is \(B_0=B-1\); \(B\) remains only the one-sided label |
| \(A(q)+1/4\) | equals \(B-h\in(B-1,B)\), so \(Q=B_0\) |
| old inverse collision | fix one literal or adverse componentwise side vector in the exact ledger; the root-free lower bound is uniform because it uses only the audited nonnegative displacement contribution |
| newest \(y_B=0\) | owned once by the literal top interval/outer-action event, never as an old inverse wall |
| \(e_p=0\) | permitted; adjacent action remains strict, so (CR46.30) remains strict |
| \(E=E_*\) | belongs to the already automatic sector; the resisting owner has \(E<E_*\) |
| \(B_0=1\) | all wall, \(7/48\), and \(9/64\) formulas remain valid |
| activity equality | no-mode owner; excluded from the strict active owner |
| support boundary \(\mathcal M=0\) | nonnegative side of the sufficient route and in fact \(\mathscr S>0\) by (CR46.30) |
| two parity grids | retained separately with starts \(r=1\) and \(r=3/2\); no interpolation between them |
| \(\alpha\uparrow1^-\) | old-chart one-sided endpoint; no relabelling as literal \(\alpha=0\) |

No argument in Sections 1--4 uses continuity across a count, shelf, inverse,
activity, or owner jump.

## 5. Frozen provisional determination

### 5.1 What was proved in this clean-room attempt

The following statements are exact and independent of Round-46 lead work:

1. the complete normalization (CR46.6)--(CR46.12), including a unique wall
   root and a closed elementary formula for \(J\);
2. the genuine wall directions
   \(\gamma'<0\), \(t'<0\), \(K'>0\), \(W'>0\), \(J'<0\), and
   \(\mathcal T'>0\);
3. the exact full wall derivative (CR46.22), with its first unsigned
   correlated inequality (CR46.23);
4. the single-radius integral coupling (CR46.24)--(CR46.26), strict
   convexity of the shelf-curvature component, and positive lower-radius and
   asymptotic endpoint kernels for the Jensen attempt;
5. the exact dependency, loss, strictness, and no-double-counting ledgers.

### 5.2 First unrepaired implication and classification

Neither attempted route proves \(\mathcal M\ge0\) on the complete exact
owner. Route A first fails at the sign of the complete correlated derivative
(CR46.23). Route B first fails at the interior kernel domination
(CR46.27), before any endpoint reduction is obtained. These are not
counterexamples to (R45.18), \(\mathscr S\), CST, or the theorem.

No broad or finite positive search was made before this freeze, and no
negative owner is certified here. The failure is therefore an **unfinished
mathematical derivation**. It is not a proved architectural obstruction and
does not establish that every possible pointwise proof would require a
forbidden family or a second certificate.

Under the Round-46 hard rule, however, another unsigned pointwise reduction
does not authorize a Round 47 pointwise attempt. The provisional clean-room
verdict is

```text
INCOMPLETE — SWITCH TO WEIGHTED AGGREGATE
```

The next recommended single obligation is

\[
 \mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m)\ge0,
\]

starting with \(d=4\), retaining the exact branching weights and introducing
no ratio ladder. No proof-obligation status should change from this
clean-room result.

### 5.3 File scope and freeze

This derivation created only

```text
human/outbox/general-d-round-46-clean-room-r45-18.md
```

Sections 1--5 are now frozen. A post-freeze comparison may be appended only
after the Round-46 lead artifact is independently frozen; these sections
must not be rewritten during that comparison.

## 6. Post-freeze comparison with Prompt A

### 6.1 Comparison gate

Sections 1--5 above remained byte-for-byte frozen during this comparison.
Their pre-comparison SHA-256 was

    af88daa4a96593822c64b36c1d2f0192927870f75142ab41051284b5e444a926

Prompt A was read only after its reported freeze. I independently verified
the lead report

    human/outbox/general-d-round-46-r45-18-complete-owner.md

at SHA-256

    1f3719f043616ce9877adb132fa789ab60ac84dd0aa10f27a30c7787aa9d3be1.

No Prompt-C report or Round-46 lead script was needed for this analytic
comparison.

### 6.2 Exact agreements

The two derivations agree exactly, up to the notation
\(\gamma_{\rm clean}=\phi_{\rm lead}\).

| subject | comparison |
|---|---|
| owner | Same one-sided upper-\(\alpha\), outer-\(B\) owner; same literal \(B_0=B-1=Q\), grids, first drop, hard-\(E\), activity, and fixed-side hypotheses. |
| wall normalization | Both obtain \(q(\tan\phi-\phi)=\pi(B_0+3/4)\), \(K=q\sec\phi=(q+1)\sec t\), and \(\cos t=(q+1)\cos\phi/q\). |
| uniqueness | Both prove a unique \(\phi\), then a unique \(t\), without a count, floor, ratio, or chamber split. |
| closed formulas | The formulas for \(h,W,\beta,R_1,J\), the antiderivative, action drop, old aggregate, top reserve, and shelf curvature coincide term by term. |
| wall calculus | Equations (R46.14)--(R46.20) in Prompt A agree with clean-room (CR46.14)--(CR46.22), including \(\phi'<0,t'<0,K'>0,W'>0,J'<0\) and \(\mathcal T'>0\). |
| monotonicity failure | Both stop the direct wall route at the unsigned correlated action/old-level/shelf derivative. The lead's opposite-sign derivative probes are consistent with, and do not alter, the clean-room analytic stopping point. |
| Jensen route | Prompt-A (R46.21)--(R46.24) is identical to clean-room (CR46.24)--(CR46.27): same radius coupling, same \(Q_b\), same negative discriminant, and the same unresolved interior kernel domination. |
| literal loss ledger | Prompt-A (R46.31)--(R46.32) expands the same exact identity as clean-room (CR46.29)--(CR46.30). |
| gate decision | Both independently reach INCOMPLETE — SWITCH TO WEIGHTED AGGREGATE, with no status promotion and no counterexample claim. |

There is no mathematical discrepancy in the common formulas.

### 6.3 Audit of the lead's additional inverse-action reduction

Prompt A goes beyond the frozen clean-room attempt by proving a strict
inverse-action quotient theorem. This additional step is valid.

Let

\[
 \mathcal D=A(x)-A(q),\qquad
 Q(z)=\frac{\{\arccos(z/K)-\arccos(z/\mu)\}
 \sqrt{\mu^2-z^2}}{\pi z}.
\]

The ratio \(\mathcal D/(U_x-U_q)\) is the weighted average of \(Q(z)\) on
\([x,q]\) with positive weight \(z/\sqrt{\mu^2-z^2}\). With
\(z=\mu\cos y\) and \(\lambda=\mu/K\),

\[
 \pi Q(\mu\cos y)
 =\sin y\int_\lambda^1
 \frac{ds}{\sqrt{1-s^2\cos^2y}}.
\]

Differentiating before estimating gives exactly

\[
 \frac d{dy}\{\pi Q(\mu\cos y)\}
 =\cos y\int_\lambda^1
 \frac{1-s^2}{(1-s^2\cos^2y)^{3/2}}\,ds>0.
\]

Thus \(Q\) is strictly decreasing in \(z\). Since \(x<q\), the weighted
average is strictly greater than its right-endpoint value:

\[
 \frac{\mathcal D}{U_x-U_q}>
 Q(q)=\frac{(\phi-a)\tan a}{\pi},
 \qquad a=\arccos\frac q{q+1}.
\]

Multiplication by the positive factor \(p(U_r-U_x)\) proves lead
(R46.27), with the strict direction preserved.

The lead's phase algebra also checks exactly. From \(t<\phi\),
\(J<1/10\), \(\beta=\phi/\pi\), and
\(B_0=q(\tan\phi-\phi)/\pi-3/4\),

\[
\begin{aligned}
B_0\zeta+\frac9{16\beta}-J
>{}&\frac{q(\tan\phi-\phi)(\pi-2\phi)}
{2\pi\phi}
+\frac{3\pi}{16\phi}+\frac{13}{20}\\
>{}&\frac{q(\tan\phi-\phi)(\pi-2\phi)}
{2\pi\phi}+\frac{41}{40}.
\end{aligned}
\]

The second strict slack is
\(3(\pi-2\phi)/(16\phi)>0\). Dropping only the already proved positive
\(\mathcal O,\mathcal T,\mathcal C\) therefore gives

\[
 \boxed{\mathcal M>F_{\rm strong}}
\]

with \(F_{\rm strong}\) exactly as printed in lead (R46.29).

This reduction is **sufficient only**. It is not equivalent to
\(\mathcal M\ge0\), (R45.18), or \(\mathscr S\ge0\), and Prompt A reports
that distinction correctly. Its non-owner negative probe consequently
falsifies neither (R45.18) nor the exact target. Under the packet's hard
rule, \(F_{\rm strong}\) is a printed failure inequality, not a new
pointwise obligation for Round 47.

The lead's additional theorem refines the route-specific location of the
first gap: after its valid strict reduction, the missing implication is

\[
 F_{\rm strong}\ge0
 \quad\hbox{on the complete exact owner}.
\]

This does not contradict the frozen clean-room identification of
(CR46.23) and (CR46.27); those remain the first gaps in the two routes
attempted there. The lead found a third exact route around them, but that
route also remains unsigned.

### 6.4 Strictness, endpoints, and double counting

No strictness or endpoint error was found.

1. The quotient inequality is strict because \(m=q-x>0\), the averaging
   weight is positive, and \(Q\) is strictly decreasing.
2. The phase reduction is strict at both \(t<\phi\) and its final
   \(3(\pi-2\phi)/(16\phi)\) slack. The inherited \(J<1/10\) is used only
   on its audited \(q\ge5\) scope.
3. Hence \(F_{\rm strong}=0\) implies \(\mathcal M>0\), while
   \(\mathcal M=0\) implies \(\mathscr S>0\) through strict adjacent action.
   Neither boundary is misreported as an equality face of the preceding
   literal scalar.
4. Literal ordinary-floor equality, the outer-\(B\) strict bracket,
   \(A(q)+1/4=B-h\), old inverse side vectors, newest \(y_B=0\),
   \(e_p=0\), \(E=E_*\), \(B_0=1\), both parity grids, activity equality,
   and \(\alpha\uparrow1^-\) receive the same owners in both reports.
5. Prompt-A (R46.32) shows every payment exactly once:

\[
\begin{aligned}
\mathscr S-\mathcal M={}&
(\Omega_--\Omega_{\rm lb})
+(\mathcal R_{\rm tan}^0-\mathcal T-R_{\rm old})\\
&+(\mathcal C_p-\mathcal C)
+p(E-R_1\mathcal D).
\end{aligned}
\]

The old and top Bregman intervals are disjoint; the shelf hinge is not added
to \(\mathcal C\); adjacent action is used only in the \(pE\) payment; and
\(1/(16\beta)\) remains an owner reconciliation, not a reserve. There is no
double counting.

The lead also labels its wall-derivative probes, non-owner
\(F_{\rm strong}\) probe, and positive finite searches as non-load-bearing
diagnostics. This comparison did not replay those searches, but no
computational claim is needed for the analytic verdict.

### 6.5 Final post-comparison verdict

The lead's additional quotient theorem and \(F_{\rm strong}\) reduction are
mathematically sound, genuinely stricter than the clean-room's pre-freeze
progress, and accurately classified as a sufficient route. They do not
prove the complete-owner sign.

The post-comparison verdict therefore remains

    INCOMPLETE — SWITCH TO WEIGHTED AGGREGATE

The failure is an unfinished derivation, not a directed falsification and
not a proof of architectural impossibility. By the Round-46 hard rule, Gate
B stops without another pointwise round. No proof-obligation status should
change. The next single obligation is

\[
 \mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m)\ge0,
\]

starting with \(d=4\), preserving the exact branching weights and adding no
ratio ladder.
