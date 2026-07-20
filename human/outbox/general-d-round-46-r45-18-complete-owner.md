# General-dimensional spherical-shell Pólya project
## Round 46 lead attempt: complete-owner sign of (R45.18)

**Date:** 21 July 2026  
**Role:** Prompt A lead analytic closure  
**Selected obligation:** SHELL-general-d-high-floor-first-drop-CST  
**Authoritative status:** open

## 1. Decision and exact scope

Round 46 does not prove the complete-owner sign of (R45.18), and it finds no
counterexample to it. The exact progress is:

1. a unique intrinsic outer-wall normalization and a closed formula for the
   cap \(J\);
2. the exact derivative of the full (R45.18) margin along a fixed
   \((p,m,B_0)\) wall, with several genuine one-signed components but no sign
   for the complete derivative;
3. a strict inverse-action quotient theorem which keeps the outer angle,
   inner angle, and radial displacement correlated;
4. the strict sufficient reduction
   \[
   \mathcal M_{45.18}>F_{\rm strong};
   \tag{R46.3}
   \]
5. a clean identification of the first unrepaired implication:
   \(F_{\rm strong}\ge0\) on the complete exact owner.

The final implication is not proved. Positive finite searches are not used as
a theorem. Under the hard decision rule in the Round-46 packet, the lead
status is

~~~text
INCOMPLETE — SWITCH TO WEIGHTED AGGREGATE
~~~

This is an unfinished derivation, not a proof of architectural impossibility
and not a falsification of either (R45.18) or the exact unprojected target.
No proof-obligation status is changed.

## 2. Repository gate, sources, and conflicts

All mandatory checks passed before mathematical work.

| item | verified value |
|---|---|
| repository | yutianlee/polya-ai-collab |
| pinned HEAD | 3ad6a78d9cb2b81d316bcf0c171ad7cce9f4fee1 |
| branch | codex/general-d-round-46-r45-18-complete-owner |
| Round-45 support commit | cdfa6a6770207f29b603e18b34526aec1cc8feab, ancestral |
| selected status | SHELL-general-d-high-floor-first-drop-CST : open |
| proof-obligation SHA-256 | a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4 |

The finalized Round-45 lead, clean-room, adversarial, and independent-audit
artifacts were present, tracked, and unchanged. Their SHA-256 hashes at
preflight were, respectively:

~~~text
a93c10ed13fbbc83e995562fd845cf39242e0a8b987442d756d744dfd8a0c2c0
a07f537ca8e29a8cf7d57ecc108bce7d94fdf3d1ca475e638f2c65c546c60a59
929b56f1af67ff800a69d9d85e2dab947941ad3ab2ba7422713e166f5309b669
206b68dbc4243fe9320fcbc9ea5ff48e50a433b59ef60889deede6759fa38cbf
~~~

The sources were applied in the packet's precedence order: authoritative
statuses, the simplified analytic strategy, the newest audited Round-45
artifacts, exact Round-44 and Round-38/42 inheritance, current directives and
state ledgers, and only then narrative manuscript material.

There is one known conflict. The narrative next-action and blocker prose in
state/proof_obligations.yml still describe the older Round-37 route. Its
status remains authoritative; the later audited Round-45 decision and the
Round-46 packet control this local calculation. No incompatible mathematical
versions were combined. The separate A2 three-dimensional maintenance review
was not used in this general-dimensional round.

## 3. Exact owner and normalization ledger

### 3.1 Fixed owner and literal target

Put

\[
x=r+p,\qquad q=x+m,\qquad \mu=q+1,\qquad K=\mu\sec t,
\]

\[
d_\rho=1-\frac{2t}{\pi},\qquad
\zeta=\frac\pi{2t}-1,\qquad
G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,\qquad
A=G_K-G_\mu.
\]

The one-sided upper-\(\alpha\), outer-\(B\) wall is

\[
G_K(q)=B_0+\frac34,\qquad B_0=B-1\ge1.
\tag{R46.4}
\]

Retain both parity grids, the common first shelf, literal first drop, one fixed
old-inverse side vector, strict dimension-labelled activity, the old chart's
\(\alpha\uparrow1^-\) label, and every inherited branch/action condition. In
particular,

\[
p\ge3,\quad m\ge1,\quad q\ge5,\quad
p-d_\rho m>\frac{11}{5},\quad 0\le E<E_*<\frac12,\qquad
E_*:=\frac{p-d_\rho m}{2p}.
\tag{R46.5}
\]

Activity equality is a no-mode owner. Define

\[
h=G_\mu(q),\quad W=G_K(\mu),\quad
v=B_0+\frac34,\quad u=v-W,\quad
\beta=\frac1\pi\arccos\frac qK,\quad 0<h<u<\beta<\frac12,
\]

\[
U_z=\sqrt{\mu^2-z^2},\qquad
R_1=\frac{U_r-U_x}{U_x-U_q}>0,\qquad
J=2\int_q^\mu G_\mu(z)\,dz.
\]

On this owner only, \(A(x)-A(q)=j+e_p+h\). It is never transported through a
floor wall.

Let \(\mathcal M\) denote the literal right side of (R45.18) minus its left
side:

\[
\boxed{\begin{aligned}
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
\tag{R46.6}
\]

Thus the sole target is exactly \(\mathcal M\ge0\), not a renamed relaxed
scalar.

### 3.2 Intrinsic wall angle and unique root

Introduce

\[
\phi:=\arccos\frac qK=\pi\beta,\qquad
a:=\arccos\frac q{q+1}.
\]

The wall and the relation between its two angles become

\[
\boxed{q(\tan\phi-\phi)=\pi v,\qquad
K=q\sec\phi=(q+1)\sec t,\qquad
\cos t=\frac{\cos\phi}{\cos a}.}
\tag{R46.7}
\]

For fixed \((q,B_0)\), the derivative of
\(q(\tan\phi-\phi)\) is \(q\tan^2\phi>0\); its endpoint values are \(0\)
and \(+\infty\). Hence (R46.7) has exactly one
\(\phi\in(0,\pi/2)\). At \(\phi=a\), the left wall action is \(h\), and
\(h<1/2<v\); hence \(a<\phi<\pi/2\). Equation (R46.7) then determines
exactly one \(0<t<\phi\). This proves wall-root uniqueness without a count,
floor, or chamber split.

The normalized quantities are

\[
r=q-m-p,\quad x=q-m,\quad \mu=q+1,\quad K=q\sec\phi,\quad
\beta=\frac\phi\pi,
\]

\[
h=\frac{\sqrt{2q+1}-qa}{\pi},\qquad
W=\frac{q+1}{\pi}(\tan t-t),
\tag{R46.8}
\]

\[
R_1=
\frac{\sqrt{(q+1)^2-(q-m-p)^2}
      -\sqrt{(q+1)^2-(q-m)^2}}
     {\sqrt{(q+1)^2-(q-m)^2}-\sqrt{2q+1}}.
\tag{R46.9}
\]

An exact antiderivative is

\[
\mathfrak I_b(z)=
\frac{3z\sqrt{b^2-z^2}+b^2\arcsin(z/b)-2z^2\arccos(z/b)}{4\pi},
\qquad \mathfrak I_b'(z)=G_b(z).
\]

Therefore

\[
\boxed{J=
\frac{\{(q+1)^2+2q^2\}a-3q\sqrt{2q+1}}{2\pi}.}
\tag{R46.10}
\]

The action drop is retained exactly as

\[
\begin{aligned}
\mathcal D:=A(x)-A(q)=\frac1\pi\bigl[&
 \sqrt{K^2-x^2}-\sqrt{\mu^2-x^2}
-\sqrt{K^2-q^2}+\sqrt{\mu^2-q^2}\\
&-x\arccos(x/K)+x\arccos(x/\mu)
+q\arccos(q/K)-q\arccos(q/\mu)\bigr].
\end{aligned}
\tag{R46.11}
\]

The old-level aggregate, top reserve, and shelf-curvature reserve are

\[
\mathcal O=\frac{\pi^2B_0}{Kt^3\sin t}
 \left(\frac W2-\frac{B_0}{4}+\frac1{48}\right),
\]

\[
\mathcal T=\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},\qquad
\mathcal C=\frac{p^3}{6\pi}
 \left(\frac1{U_r}-\frac1{\sqrt{K^2-r^2}}\right).
\tag{R46.12}
\]

Every square root and denominator above is positive because
\(0<r<x<q<\mu<K\). All inverse-trigonometric arguments lie in \((0,1)\).
Also \(u<1/2\) gives

\[
\frac W2-\frac{B_0}{4}+\frac1{48}
>\frac{B_0}{4}+\frac7{48}>0.
\tag{R46.13}
\]

Thus \(\mathcal O,\mathcal T,\mathcal C>0\).

### 3.3 Dependency ledger

| inherited item | use here | source/scope |
|---|---|---|
| strict counting and owner labels | literal \(B_0\), first shelf/drop, parity and wall assignments | frozen exact definitions |
| upper-\(\alpha\), outer-\(B\) specialization | \(0<h<u<\beta\), action identity and strict adjacent action | audited Round 42 |
| exact terminal ledger | \(J\), \(9/(16\beta)\), \(\mathcal C_p\), direct \(D_A(q)\) | audited Round 44 |
| primary \(u\)-retaining \(\Omega_-\) bound | old-level combination \(\mathcal O\) | audited Round 38/45 |
| old inverse Bregman theorem | \(7/48\) per old interval | proved in Round 45 |
| top Bregman theorem | \(9/64\) reserve \(\mathcal T\) | audited Round 44/45 |
| shelf curvature | \(\mathcal C_p\ge\mathcal C\) | audited Round 44/45 |
| \(J<1/10\) for \(q\ge5\) | phase estimate in Section 6 | inherited exact endpoint estimate; checked against (R46.10) |
| simplified analytic strategy | forbids indexed families, ratio ladders, chambers, and a second certificate | binding method |

No rejected global sign, R45-CF, shell-ratio ladder, asymptotic replacement,
or compact certificate is used.

## 4. Route A: exact wall calculus

Hold symbolic \((p,m,B_0)\) fixed and differentiate along the unique wall,
inside one fixed open owner component. A prime denotes \(d/dq\). From
(R46.7),

\[
\boxed{\phi'=-\frac{\tan\phi-\phi}{q\tan^2\phi}<0,\qquad
K'=\frac\phi{\sin\phi}>0,\qquad
t'=\frac{\phi-\pi v}{q(q+1)\tan\phi\tan t}<0.}
\tag{R46.14}
\]

It follows that \(\beta'<0\), \(\zeta'>0\), and \(d_\rho'>0\).
For the wall interval,

\[
u=\frac1\pi\int_0^1\arccos\frac{q+s}{K}\,ds.
\]

Exact differentiation before sign relaxation gives

\[
W'=-u'=\frac1\pi\int_0^1
\frac{K-(q+s)K'}{K\sqrt{K^2-(q+s)^2}}\,ds>0.
\tag{R46.15a}
\]

Indeed, the numerator is bounded below by
\(K-(q+1)K'>0\), and the final inequality is equivalent to
\(\pi v>\phi\). The exact cap derivative is

\[
J'=\frac2\pi\int_0^1(\sin\psi_s-\psi_s)\,ds<0,\qquad
\psi_s:=\arccos\frac{q+s}{q+1}.
\tag{R46.15}
\]

Using the wall equation,

\[
\mathcal T=\frac{9\pi}{64v}H(\phi),\qquad
H(\phi):=\frac{1-\phi\cot\phi}{\phi^3},
\]

\[
H'(\phi)=
\frac{\phi^2\csc^2\phi+2\phi\cot\phi-3}{\phi^4}<0.
\tag{R46.15b}
\]

The derivative of the final factor is negative. After multiplication by the
positive factor \(\phi^4\sin^2\phi\), the opposite sign is equivalent to

\[
3\sin^2\phi-\phi^2-2\phi\sin\phi\cos\phi>0.
\]

Its derivative is
\(4\cos\phi(\sin\phi-\phi\cos\phi)>0\), and it vanishes at zero. Since
\(\phi'<0\), \(\mathcal T'>0\).

For completeness, put \(c=p+m\), and for a radial shift \(s\ge0\) define

\[
U_s=\sqrt{2(s+1)q+1-s^2},\quad
V_s=\sqrt{K^2-(q-s)^2},\quad
\theta_s=\arccos\frac{q-s}{K}.
\]

Then \(U_c=U_r,U_m=U_x,U_0=U_q\), and

\[
\chi_s:=\arccos\frac{q-s}{q+1},
\]

\[
R_1'=
\frac{\left(\frac{c+1}{U_c}-\frac{m+1}{U_m}\right)(U_m-U_0)
-(U_c-U_m)\left(\frac{m+1}{U_m}-\frac1{U_0}\right)}
{(U_m-U_0)^2},
\tag{R46.16}
\]

\[
\mathcal D'=\frac1\pi\left[
K'(\sin\theta_m-\sin\theta_0)-(\theta_m-\theta_0)
-(\sin\chi_m-\sin\chi_0)+(\chi_m-\chi_0)\right].
\tag{R46.17}
\]

Let

\[
c_0=\frac{\pi^2}{Kt^3\sin t}
=\frac{\pi^2}{(q+1)t^3\tan t},\qquad
P=\frac W2-\frac{B_0}{4}+\frac1{48}.
\]

The remaining exact derivatives are

\[
\frac{c_0'}{c_0}=-\frac1{q+1}
-t'\left(\frac3t+\frac1{\sin t\cos t}\right),\qquad P'=\frac{W'}2,
\tag{R46.18}
\]

\[
\mathcal C'=\frac{p^3}{6\pi}
\left[-\frac{c+1}{U_c^3}
+\frac{KK'-(q-c)}{V_c^3}\right].
\tag{R46.19}
\]

Substitution into the literal margin gives

\[
\boxed{\begin{aligned}
\mathcal M'={}&p(R_1'\mathcal D+R_1\mathcal D')
+B_0(c_0'P+c_0W'/2)\\
&-\frac{B_0\pi t'}{2t^2}
-\frac{9\pi\phi'}{16\phi^2}-J'+\mathcal T'+\mathcal C'
-\frac{mt'}\pi.
\end{aligned}}
\tag{R46.20}
\]

The explicitly isolated phase/root/top terms in the second line, apart from
\(\mathcal C'\), are positive. The correlated action derivative,
\(\mathcal C'\), and the complete old-level derivative do not have inherited
uniform signs. Evaluation on the continuous exact wall with only the basic
radial geometry gives

\[
\mathcal M'(q=5,p=3,m=1,B_0=1)=0.22182656\ldots,
\]

but

\[
\mathcal M'(q=100,p=20,m=1,B_0=1)=-0.01078180\ldots.
\]

The latter is not asserted to be a complete owner and is not a counterexample;
it shows only that wall geometry alone cannot justify the desired
monotonicity. No exact-owner hypothesis was converted into a uniform sign for
(R46.20). A shelf, inverse, activity, or parity wall cannot be crossed by
continuity. Route A therefore stops at the unsigned full derivative.

## 5. Correlated convexity/Jensen audit

One direct Jensen attempt keeps the action and shelf curvature under the same
radius integral. Fix \((q,m,t,B_0)\), put \(x=q-m\), let \(p=x-r\), and write
\(V_b(z)=\sqrt{b^2-z^2}\). Then

\[
\frac{\mathcal D}{U_x-U_q}
=\frac1\pi\int_\mu^K C_b\,db,\qquad
C_b:=\frac{U_x+U_q}{b\{V_b(x)+V_b(q)\}}>0,
\tag{R46.21}
\]

\[
\mathcal C=\frac{p^3}{6\pi}\int_\mu^K
\frac{b}{(b^2-r^2)^{3/2}}\,db.
\tag{R46.22}
\]

For \(\mathcal P(p)=pR_1\mathcal D+\mathcal C\), exact differentiation gives

\[
\mathcal P''(p)=\frac1\pi\int_\mu^K\left[
C_b\left(\frac{2r}{U_r}-\frac{p\mu^2}{U_r^3}\right)
+\frac{pbQ_b}{2(b^2-r^2)^{7/2}}\right]db,
\tag{R46.23}
\]

where

\[
Q_b=2(b^2-r^2)^2-6pr(b^2-r^2)+p^2(b^2+4r^2)>0.
\]

The last sign follows because the discriminant of this quadratic in \(p\) is
\(4(b^2-r^2)^2(r^2-2b^2)<0\). The action bracket can nevertheless be
negative. The first missing correlated kernel estimate is

\[
C_b\left(\frac{p\mu^2}{U_r^3}-\frac{2r}{U_r}\right)
\le \frac{pbQ_b}{2(b^2-r^2)^{7/2}},\qquad \mu\le b\le K,
\tag{R46.24}
\]

or a signed integrated replacement. Neither is proved. Even if (R46.24)
supplied convexity, a uniform endpoint or stationary-point sign for the full
margin would still be required. Thus this Jensen route is exact but does not
close a continuous degree of freedom.

## 6. Strict inverse-action reduction and first unrepaired sign

The strongest elementary reduction found in the lead attempt comes from an
exact monotone quotient, not from independently worst-casing the wall data.
Since

\[
\mathcal D=\frac1\pi\int_x^q
\left(\arccos\frac zK-\arccos\frac z\mu\right)dz,\qquad
U_x-U_q=\int_x^q\frac z{\sqrt{\mu^2-z^2}}\,dz,
\]

their ratio is a weighted average of

\[
Q(z)=\frac{\left(\arccos(z/K)-\arccos(z/\mu)\right)
\sqrt{\mu^2-z^2}}{\pi z}.
\]

Set \(z=\mu\cos y\) and \(\lambda=\mu/K\). Then

\[
\pi Q(\mu\cos y)=\sin y\int_\lambda^1
\frac{ds}{\sqrt{1-s^2\cos^2y}},
\]

and differentiation under the integral gives

\[
\frac d{dy}\{\pi Q(\mu\cos y)\}
=\cos y\int_\lambda^1
\frac{1-s^2}{(1-s^2\cos^2y)^{3/2}}\,ds>0.
\tag{R46.25}
\]

Thus \(Q\) is strictly decreasing in \(z\). Because \(m=q-x>0\),

\[
\boxed{\frac{\mathcal D}{U_x-U_q}>Q(q)
=\frac{(\phi-a)\tan a}{\pi}.}
\tag{R46.26}
\]

Consequently

\[
pR_1\mathcal D>
\frac{p(U_r-U_x)(\phi-a)\tan a}{\pi}.
\tag{R46.27}
\]

The phase/root combination is reduced on the same wall. Since
\(t<\phi\), \(J<1/10\), and \(\beta=\phi/\pi\),

\[
\begin{aligned}
B_0\zeta+\frac9{16\beta}-J
&>B_0\left(\frac\pi{2\phi}-1\right)
+\frac{9\pi}{16\phi}-\frac1{10}\\
&=\frac{q(\tan\phi-\phi)(\pi-2\phi)}{2\pi\phi}
+\frac{3\pi}{16\phi}+\frac{13}{20}\\
&>\frac{q(\tan\phi-\phi)(\pi-2\phi)}{2\pi\phi}
+\frac{41}{40}.
\end{aligned}
\tag{R46.28}
\]

The final slack is exactly \(3(\pi-2\phi)/(16\phi)>0\). Equations
(R46.27)--(R46.28) keep \(q,\phi,a,t,r,p,m\) linked by the exact wall.
Dropping only the proved positive terms
\(\mathcal O,\mathcal T,\mathcal C\) yields

\[
\boxed{\begin{aligned}
\mathcal M>F_{\rm strong}:={}&
\frac{p(U_r-U_x)(\phi-a)\tan a}{\pi}\\
&+\frac{q(\tan\phi-\phi)(\pi-2\phi)}{2\pi\phi}
+\frac{d_\rho m}{2}-\frac p2+\frac{41}{40}.
\end{aligned}}
\tag{R46.29}
\]

This is a strict sufficient lower reduction, not an equivalent reformulation
of (R45.18). It is also the first unrepaired implication:

\[
\boxed{F_{\rm strong}\ge0\quad\hbox{on every complete exact owner}.}
\tag{R46.30}
\]

No analytic sign for (R46.30) was obtained. Its exact-owner constraints are
essential. On the larger domain retaining the exact outer wall and basic
radial/hard inequalities but omitting the common shelf and hard-\(E\)
conditions,

\[
(r,p,m,B_0)=(8{,}886{,}110,2935,254,1),\qquad q=8{,}889{,}299,
\]

gives \(F_{\rm strong}=-224.405313\ldots\) while
\(p-d_\rho m>11/5\). This point is not an owner and is not a counterexample
to (R45.18); it proves only that the broader hard geometry is insufficient
after all omitted owner correlations are discarded. The present derivation
found no way to use those correlations without
resolving indexed faces, which this round forbids. This observation is not a
proof that every conceivable pointwise argument must do so, and no
architectural-impossibility claim is made.

## 7. Exact loss ledger and no-double-counting audit

The literal starting identity is

\[
\mathscr S=\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p+pE
-\frac{p-d_\rho m}{2}.
\tag{R46.31}
\]

Let

\[
\Omega_{\rm lb}=\frac{c_0}{2}
\left(\frac{B_0(B_0+1)}2-B_0u\right),\qquad
R_{\rm old}=\frac{7B_0c_0}{48},\qquad
c_0=\frac{\pi^2}{Kt^3\sin t}.
\]

Then

\[
\Omega_{\rm lb}+R_{\rm old}
=B_0c_0\left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)=\mathcal O,
\]

and the complete ledger is

\[
\boxed{\begin{aligned}
\mathscr S-\mathcal M={}&(\Omega_--\Omega_{\rm lb})\\
&+(\mathcal R_{\rm tan}^0-\mathcal T-R_{\rm old})\\
&+(\mathcal C_p-\mathcal C)
+p\{E-R_1\mathcal D\}.
\end{aligned}}
\tag{R46.32}
\]

The prescribed weakening order and discarded signs are:

| step | weakening | discarded quantity |
|---:|---|---|
| 1 | exact \(\mathcal C_p\to\mathcal C\) | \(\mathcal C_p-\mathcal C\ge0\) |
| 2 | exact old Bregman areas to \(7/48\) each | sum of old strong-convexity residuals, nonnegative |
| 3 | exact top interval to \(9/64\) | top Bregman residual, nonnegative |
| 4 | exact \(\Omega_-\to\Omega_{\rm lb}\), then combine only with Step 2 | \(\Omega_--\Omega_{\rm lb}\ge0\) |
| 5 | exact \(pE\to pR_1\mathcal D\) | \(p(\Delta-R_1\mathcal D)+2pe_p>0\) |
| 6 | \(\mathcal M\to F_{\rm strong}\) | quotient slack, phase slack, \(\mathcal O,\mathcal T,\mathcal C\), all signed above |

Step 5 uses strict adjacent action and \(e_p\ge0\). The shelf hinge
\(a_p\Delta\) is not added to \(\mathcal C\). Old unit intervals and the
literal top interval are disjoint. The newest \(y_B=0\) event is top/outer
data, not an old inverse collision. The \(1/(16\beta)\) identity reconciles
gap-side and literal ledgers; it is checked but not added as a reserve.
Thus the hinge, shelf curvature, old areas, top area, adjacent action, and
reconciliation are each counted once.

In particular, \(\mathscr S>\mathcal M>F_{\rm strong}\) on the fixed owner.
Neither converse is valid.

## 8. Equality, wall, and strictness audit

| face/event | fixed assignment |
|---|---|
| \(A(r+s)+1/4\in\mathbb Z\) | literal ordinary-floor owner; do not continue the action identity through the jump |
| \(G_K(q)+1/4=B\) | one-sided outer-\(B\) label, but literal strict count \(B_0=B-1\) |
| \(A(q)+1/4\in(B-1,B)\) | \(A(q)+1/4=B-h\), so \(Q=B_0\) |
| old inverse collision | retain one fixed literal/adverse side vector; the root-free lower bound is uniform on either resolved side |
| newest \(y_B=0\) | counted once by the top interval/outer event, never as an old inverse root |
| \(e_p=0\) | allowed; strict adjacent action still makes Step 5 strict |
| \(E=E_*\) | automatic-sector face; excluded from the resisting \(E<E_*\) owner |
| \(B_0=1\) | all normalization, \(7/48\), \(9/64\), and quotient formulas remain valid |
| parity | integer \(r\ge1\) and half-integer \(r\ge3/2\) grids retained separately |
| activity equality | no-mode owner, excluded by strict activity |
| support boundary \(\mathcal M=0\) | sufficient nonnegative side; then \(\mathscr S>0\) by (R46.32) |
| reduced boundary \(F_{\rm strong}=0\) | implies \(\mathcal M>0\); it is not an equality face of the literal margin |
| \(\alpha\uparrow1^-\) | old-chart one-sided endpoint; never relabelled as next-chart \(\alpha=0\) |

No proof step crosses a shelf, inverse, outer-count, activity, parity, or
owner jump by continuity.

## 9. Falsification and regression results

### 9.1 Lead diagnostics

The lead Python evaluator imports the audited Round-44/45 definition engine
and reconstructs the literal margin independently from its payment ledger.
A 60,480-proposal compact sweep produced 30 high-precision exact owners and
no negative margin. Its observed minimum was

\[
\mathcal M(1,3,1,2)
=1.70914550684517353565515496215\ldots,
\]

and its observed minimum reduced scalar was

\[
F_{\rm strong}(1,4,1,2)
=0.805262048195380415074009708467\ldots.
\]

These finite values are diagnostics only. The program also reproduces the
opposite wall-derivative signs in Section 4 and the non-owner negative
\(F_{\rm strong}\) probe in Section 6.

The installed Mathematica runtime exactly replays the wall derivatives,
antiderivative and closed \(J\), quotient-kernel derivative, phase algebra,
and coefficients \(7/48\), \(9/64\), and \(1/(16\beta)\). Its final flag is

~~~text
round46R4518ReplayOK=True
~~~

### 9.2 Independent Prompt-C search

The independent evaluator imports only the audited independent Round-45
definition engine. Its frozen run covered 886,225 distinct proposals,
including the mandatory 447,640-proposal box. It reconstructed 833 exact
owners at 90 decimals:

| classification | count |
|---|---:|
| literal \(\mathcal M<0\) | 0 |
| exact unprojected \(\mathscr S<0\) | 0 |
| support margin \(M_{30}>0\) | 0 |
| localized Round-45 support margin \(>0\) | 0 |

The exact owners include both parity grids, \(B_0=1\), \(B\ge32\), \(m=1\),
large \(p\), radii up to \(1{,}919{,}213\), \(B\) up to 512, small and large
\(t\), and approaches to the hard-\(E\), \(e_p=0\), shelf, inverse, and
\(p-d_\rho m=11/5\) faces. No sampled point approached activity equality
within one unit; that is explicitly a search limitation.

At the sampled minimum \((r,p,m,f,B,j)=(1,3,1,2,2,0)\), a 768-bit directed
replay gives

\[
\mathcal M=1.7091455068451735356551549621486\ldots>0,\qquad
\mathscr S=2.6945652789003550256293329147503\ldots>0.
\]

This certifies only that point, not a global minimum. Both audited R45-CF
counterexamples still have R45-CF \(<0\) but directed
\(\mathcal M>0\) and \(\mathscr S>0\); hence they do not falsify (R45.18).
The Round-27 automatic-sector witness, Round-43 rejected hard-\(E\) record,
Round-44 minimum, \(1/(16\beta)\) reconciliation, \(9/64\) top reserve,
\(7/48\) old-level coefficient, primary \(\Omega_-\) bound, Round-42
adjacent action, and Round-45 ledger identities all replay successfully.

The exact classifications are

~~~text
r45_18_route_counterexample : NOT FOUND
support_entry_witness        : NOT FOUND
gate_trigger_certificate     : NOT FOUND
positive_coverage_certificate: FALSE
~~~

## 10. Final determination and next obligation

What is proved is the exact normalization, wall calculus, quotient theorem,
loss/equality ledgers, and strict sufficient reduction
\(\mathcal M>F_{\rm strong}\). What is not proved is (R46.30), and therefore
(R45.18) is not proved on the complete owner. No sufficient inequality is
reported as equivalent, and no finite positive sweep is promoted to coverage.

The first logical gap is using the exact common-shelf, hard-\(E\), and
activity correlations to sign \(F_{\rm strong}\) uniformly without creating
a forbidden floor/count/chamber family. The Round-46 packet forbids another
pointwise round after an unsigned terminal reduction. Gate B therefore stops
by the Round-46 hard rule, not by falsification.

The next single mathematical obligation is the weighted aggregate

\[
\mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m)\ge0,
\]

starting with \(d=4\), preserving exact branching weights and introducing no
ratio ladder. The final independent audit must specify the Round-47 launch
and any proposed state patch. Until that audit, and absent a separate status
update, the selected high-floor CST, branching backbone, weighted aggregate,
and all-dimensional theorem retain their current statuses.

## 11. Files modified

Prompt A created only:

~~~text
human/outbox/general-d-round-46-r45-18-complete-owner.md
computations/general_d_round46_r45_18_replay.wl
computations/general_d_round46_r45_18_diagnostic.py
~~~

No state, proof graph, manuscript, completed three-dimensional proof, or
Round-45 artifact was edited.
