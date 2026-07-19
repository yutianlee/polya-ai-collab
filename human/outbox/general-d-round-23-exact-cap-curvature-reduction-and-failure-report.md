# General dimension, Round 23: exact-cap curvature reduction and failure report

Date: 19 July 2026  
Status: rigorous reduction; the sign of the reduced scalar remains open

## 0. Scope and theorem boundary

This note continues only the high-floor first-drop branch

\[
 f\geq2,\qquad p<n,\qquad m:=n-p\geq1.
\]

Round 22 proved

\[
 \Phi_\delta>\mathcal R_J,
\]

where

\[
\begin{aligned}
 \mathcal R_J={}&(p+a_p)L_0-\frac p2+\frac{d m}{2}
 +\frac{B_0d}{2c}-J+\mathcal E(\lambda),\\
 a_p={}&\frac{p^2}{3(2r+p)},\qquad
 J=2I_\mu(q),
\end{aligned}                                                    \tag{0.1}
\]

and

\[
 \mathcal E(\lambda)=
 \mathbf 1_{\{0<\lambda<1\}}
 \min\{1,2(3/4-\lambda)_+^2\}.
\]

The main result below is a simpler sufficient scalar which retains all
correlations until the final cap comparison.  Its sign is not proved.
Consequently this note proves neither \(\mathcal R_J\geq0\), CST-H, nor the
general-dimensional Polya theorem.

## 1. Intrinsic parametrization and exact shelf domain

Put

\[
 t=\arccos\rho\in(0,\pi/2),\qquad
 c=\frac t\pi,\qquad d=1-\frac{2t}{\pi},
\]

\[
 q=r+p+m,\qquad \mu=q+\alpha,\qquad 0\leq\alpha<1.
\]

Then

\[
 K=\frac\mu{\cos t},\qquad
 W=G_K(\mu)=\frac\mu\pi(\tan t-t),                         \tag{1.1}
\]

\[
 \lambda=f-\frac14-W>0,\qquad
 B_0=[W+\tfrac14]_<,
\]

and the curvature constant simplifies to

\[
 \kappa=\frac{1-\cos t}{\pi\mu}.                            \tag{1.2}
\]

For \(x=r+p\) and \(h=f-1/4\), exact first-shelf feasibility is

\[
 h\leq A_t(x),\qquad A_t(r)<h+1,\qquad A_t(x+1)<h,           \tag{1.3}
\]

where

\[
 A_t(z)=G_{\mu/\cos t}(z)-G_\mu(z).
\]

Monotonicity of \(A\) in the spatial variable makes (1.3) equivalent to
the complete first-shelf floor conditions.  Since \(x+1\leq\mu\), the last
inequality and monotonicity also give \(W<h\), hence \(\lambda>0\).

The owner activity condition is

\[
 \frac{\mu^2}{\cos^2t}>
 \frac{\pi^2}{(1-\cos t)^2}+\gamma,                          \tag{1.4}
\]

with \(\gamma=3/4\) on the integer owner \(r\geq1\), and \(\gamma=2\)
on the half-integer owner \(r\geq3/2\).

## 2. The cap is below \(1/8\) on this branch

### Lemma 2.1

Every extension-grid high-floor first drop with \(p\geq1\) satisfies

\[
 \boxed{J<\frac18.}                                           \tag{2.1}
\]

### Proof

Here \(p,m\geq1\).  Thus \(q=r+p+m\geq3\) on the integer grid and
\(q\geq7/2\) on the half-integer grid.  As in Round 21, radius monotonicity
and \(\mu<q+1\) give

\[
 J<2I_{q+1}(q)\leq2I_4(3).
\]

The cap monotonicity in \(q\) follows from

\[
 I_{q+1}(q)=\frac1\pi\int_{0\leq u\leq v\leq1}
 \sqrt{1-\left(\frac{q+u}{q+v}\right)^2}\,dv\,du:
\]

the displayed integrand decreases pointwise with \(q\).

The endpoint value is

\[
 2I_4(3)=\frac{34\arccos(3/4)-9\sqrt7}{2\pi}.
\]

Use \(\arccos(3/4)=2\arctan(1/\sqrt7)\) and the alternating-series
upper bound

\[
 \arctan u<u-\frac{u^3}{3}+\frac{u^5}{5}\qquad(0<u<1).
\]

Then

\[
 34\arccos(3/4)-9\sqrt7
 <\frac{1499}{735\sqrt7}
 <\frac{20986}{27195}
 <\frac{333}{424}<\frac\pi4.
\]

The second inequality uses \(\sqrt7>37/14\); the third has positive
cross-difference \(157871\); the last uses \(\pi>333/106\).  This proves
(2.1).

## 3. Curvature-only sufficient scalar

The curvature member of the Round 21 maximum is

\[
 L_{\rm curv}=\frac\kappa2p(2r+p).
\]

Using (1.2), its complete coefficient in (0.1) is exactly

\[
 (p+a_p)L_{\rm curv}
 =\frac{p^2(3r+2p)(1-\cos t)}{3\pi\mu}.                      \tag{3.1}
\]

Define

\[
\boxed{
\begin{aligned}
 \mathcal C_8(t)={}&
 \frac{p^2(3r+2p)(1-\cos t)}{3\pi\mu}-\frac p2
 +\frac m2\left(1-\frac{2t}{\pi}\right)\\
 &+B_0\left(\frac\pi{2t}-1\right)
 +\mathcal E(\lambda)-\frac18.
\end{aligned}}                                                  \tag{3.2}
\]

### Proposition 3.1

On the exact domain (1.3)--(1.4),

\[
 \boxed{\mathcal R_J>\mathcal C_8.}                            \tag{3.3}
\]

Hence \(\mathcal C_8\geq0\) is sufficient for high-floor CST-H.

### Proof

Round 21 gives \(L_0\geq L_{\rm curv}\), and Lemma 2.1 gives
\(-J>-1/8\).  Substitute these two inequalities into (0.1), use
\(d/(2c)=\pi/(2t)-1\), and then apply (3.1).  No cap constant is used
before this final comparison.

## 4. Convex one-variable reduction

Fix \((r,p,m,f,\alpha)\), hence \(\mu\).  Both \(A_t(z)\) and \(W(t)\)
are strictly increasing in \(t\).  Indeed,
\(\partial_R G_R(z)=\sqrt{1-z^2/R^2}/\pi>0\), while
\(R=\mu/\cos t\) increases.  The activity left-minus-right side in (1.4)
also increases strictly.  Therefore the feasible \(t\)-set is a single
interval, with endpoints among

\[
 A_t(x)=h,\quad A_t(x+1)=h,\quad A_t(r)=h+1,
 \quad\text{and the owner activity wall}.                       \tag{4.1}
\]

Split that interval only at intrinsic action walls

\[
 W+\frac14\in\mathbb Z                                      \tag{4.2}
\]

and at the three top-payment walls

\[
 \lambda=\frac34,qquad
 \lambda=\frac34-\frac1{\sqrt2},qquad
 \lambda=1.                                                   \tag{4.3}
\]

On every resulting open cell, \(B_0\) is constant and the top payment is
either constant or

\[
 \mathcal E=2\bigl(W-(f-1)\bigr)^2.
\]

Write

\[
 C_0=\frac{p^2(3r+2p)}{3\pi\mu},\qquad
 W'=\frac\mu\pi\tan^2t,qquad
 W''=\frac{2\mu}\pi\tan t\sec^2t.
\]

Direct differentiation of (3.2) gives

\[
 \mathcal C_8'
 =C_0\sin t-\frac m\pi-\frac{B_0\pi}{2t^2}
 +\mathcal E',                                                \tag{4.4}
\]

where \(\mathcal E'=0\) on a constant branch and

\[
 \mathcal E'=4\bigl(W-(f-1)\bigr)W'
\]

on the quadratic branch.  Moreover

\[
 \mathcal C_8''=C_0\cos t+\frac{B_0\pi}{t^3}+\mathcal E''>0, \tag{4.5}
\]

because \(\mathcal E''=0\) on a constant branch, while

\[
 \mathcal E''=4\{(W')^2+(W-(f-1))W''\}>0
\]

on the quadratic branch.  Thus each cell has at most one stationary point,
and its minimum is at that point or at a boundary from (4.1)--(4.3).

At (4.2), increasing \(t\) raises \(B_0\) by one and hence raises
\(\mathcal C_8\) by \(\pi/(2t)-1>0\).  The literal strict value at the
wall is the lower, left-hand value.  At the saturation wall
\(\lambda=3/4-1/\sqrt2\), the derivative jumps downward from the quadratic
branch to the constant branch, so that wall cannot create a new local
minimum.  This is a boundary reduction, not a ratio partition.

The exact remaining analytic obligation is therefore

\[
\boxed{
 \mathcal C_8\geq0
 \quad\text{under (1.3)--(1.4), at the boundaries (4.1)--(4.3)
 or the unique root of (4.4).}}                                  \tag{4.6}
\]

## 5. Equality-face audit

1. **Ordinary lower shelf wall.**  Equality \(A_t(x)=h\) belongs to the
   first shelf under the ordinary floor convention and is included.
2. **First-drop wall.**  Equality \(A_t(x+1)=h\) is not in the first-drop
   branch; it is used only as a one-sided upper endpoint.
3. **Start upper wall.**  Equality \(A_t(r)=h+1\) belongs to the next floor
   and is likewise only a one-sided endpoint.
4. **Activity wall.**  Activity is strict.  Its equality belongs to the
   no-mode theorem and is only a limiting endpoint here.
5. **Interface wall \(\alpha=0\).**  The ordinary definition gives
   \(q=\mu\) and \(J=0\).  No continuity across a change of \(q\) is used.
6. **Terminal action wall.**  The literal bracket is
   \([k]_< =k-1\); hence the wall has the lower value of \(B_0\), exactly
   as used above.
7. **The face \(\lambda\downarrow0\).**  It is not part of a first drop.
   On the admissible side, however,
   \(\mathcal E(\lambda)\to1\).  Substituting the inadmissible value
   \(\lambda=0\) into the indicator would incorrectly remove this unit
   payment.  An exploratory endpoint evaluation made precisely this error;
   all apparent negative values on that face disappeared after the
   one-sided convention was restored.
8. **The faces \(r+j=K\).**  They do not occur in (1.3):
   \(r+j\leq x+1\leq\mu<K\).

## 6. Loss ledger

Only two positive quantities are discarded in Proposition 3.1.

1. The elasticity member of \(L_0\) is discarded by
   \(L_0\geq L_{\rm curv}\).
2. The exact cap reserve \(1/8-J>0\) is discarded at the last line.

The top payment, literal \(B_0\), exact shelf walls, owner activity wall,
and the exact relation \(\mu=r+p+m+\alpha\) are retained.  No inverse-root
fraction, ratio ladder, or compact certificate is introduced.

## 7. Counterexample search and failure report

A non-rigorous double-precision falsification sweep minimized (3.2) on
each convex cell described above for

\[
\begin{gathered}
 r=1,\ldots,10\quad\text{or}\quad r=3/2,\ldots,21/2,\\
 1\leq p,m\leq10,\qquad 2\leq f\leq6,\\
 \alpha\in\{0,.1,.25,.5,.75,.9,.99,.999999\}.
\end{gathered}
\]

There were 77,391 retained feasible fixed-\(\alpha\) cells.  No negative
value was found.  The smallest sampled value was

\[
 \mathcal C_8\approx0.0128645729
\]

at

\[
 (r,p,m,f,B_0)=(1,3,2,2,1),\qquad A(r+p)=7/4,qquad
 \alpha=0.999999.
\]

The limiting pattern \(\alpha\uparrow1\) has

\[
 t=1.005008958418235\ldots,qquad
 \lambda=0.480629613415452\ldots,
\]

\[
 \mathcal C_8=0.012864451980857\ldots,qquad
 \mathcal R_J\text{ with the curvature member only}
 =0.046649621533640\ldots.
\]

These numbers are theorem-design evidence only.  The search is not a proof
of (4.6).

Thus Round 23 ends with one precise inequality, (4.6), and one extremal
pattern.  Neither \(\mathcal R_J\) nor \(\Phi_\delta\) was falsified.  The
next analytic step is to compare the unique convex-cell minimum with the
lower shelf wall in (4.1), and then prove monotonicity in the discrete data;
if that comparison fails, the strategy-approved fallback is the weighted
aggregate theorem, not another ratio decomposition.
