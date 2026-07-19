# General dimension, Round 29: complete-terminal phase and constant-K wall monotonicity, with primary inverse-cell closure

Date: 19 July 2026  
Status: three analytic reductions proved; high-floor CST remains open

## 0. Scope and theorem boundary

This note continues from the exact Round 28 hard sector

\[
 p>d(t)m,\qquad 0\leq E(t)<E_*(t)
 =\frac12-\frac{d(t)m}{2p}<\frac12,
\qquad d(t)=1-\frac{2t}{\pi}.
\tag{0.1}
\]

It proves three new statements.

1. For every fixed discrete/interface tuple, the complete-terminal scalar
   \(\Psi^{L_T}_{4,E}\) is strictly increasing in \(t\) on every literal
   terminal count cell.  Thus it has no interior stationary point.  Only
   the lower feasible endpoint and the bad right sides of discrete count
   walls remain as fixed-\(\alpha\) candidates.
2. On every fixed-\(K\), fixed-\(Q\) segment of an inverse wall or a
   complete-terminal outer-\(B\) wall, the same scalar is strictly
   decreasing in \(\mu\).  Such wall faces have no interior stationary
   point; their only remaining candidates are endpoint collisions with
   nonconstant-\(K\) shelf, \(Q\), activity, hard-sector, or \(\alpha\) faces.
3. The complete maximal literal cell abutting the Round 28 primary face
   \[
    (r,p,m,f)=(1,2,2,2),\qquad
    \alpha=0,\qquad y_1\downarrow2^+
   \]
   is positive by a direct analytic estimate:
   \[
    \Psi^{L_T}_{4,E}>
    \frac{371}{15840}+2\eta_1+2E>0.
   \tag{0.2}
   \]

The proof retains the complete inverse fraction, exact cap, top interval,
actual \(E\), and the curvature/elasticity maximum.  It introduces no ratio
threshold, compact certificate, or numerical premise.

The nonconstant-\(K\) shelf, \(Q\), and activity intersections are not
closed.  Consequently high-floor CST, pointwise assembly, and the
all-dimensional theorem remain open.

Use the Round 28 notation

\[
 x=r+p,\qquad q=r+p+m,\qquad
 \mu=q+\alpha,\qquad K=\mu\sec t,
\]

\[
 E=A_t(r)+A_t(x)+\frac12-2f,\qquad
 a_p=\frac{p^2}{3(2r+p)},
\]

\[
 \lambda=f-\frac14-W,\qquad
 W=G_K(\mu)=\frac{\mu}{\pi}(\tan t-t),
\]

\[
 \tau=\frac{s-1}{s+1},\qquad
 s=\sqrt{1+\frac{p(2r+p)}
 {(m+\alpha)(m+\alpha+2r+2p)}}.
\]

Define

\[
 U=\tau(E+2\lambda),\qquad
 M_4=\max\{U,\mathcal K_4\},
\tag{0.3}
\]

where

\[
 \mathcal K_4
 =\frac{(x^2-r^2)(1-\cos t)}{2\pi\mu}
 +\frac{(x^4-r^4)(1-\cos^3t)}{24\pi\mu^3}.
\tag{0.4}
\]

The selected scalar is

\[
 \boxed{
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*).}
\tag{0.5}
\]

## 1. Proposition: strict phase monotonicity on every terminal count cell

### 1.1 Statement

Fix \((r,p,m,f,\alpha)\) and vary \(t\) in its exact feasible hard
interval.  Put

\[
 v=G_K(q),\qquad
 B=[v+\tfrac14]_<,\qquad
 Q=[A_t(q)+\tfrac14]_<.
\]

For \(1\leq k\leq B\), define \(\theta_k\) and \(y_k\) by

\[
 \frac K\pi(\sin\theta_k-\theta_k\cos\theta_k)
 =k-\frac14,\qquad
 y_k=K\cos\theta_k-q,
\]

\[
 \eta_k=y_k-[y_k]_<.
\]

Let

\[
 \beta=\frac{\arccos(q/K)}{\pi},\qquad
 J=2\int_q^\mu G_\mu(z)\,dz.
\]

A terminal count cell is an open interval on which \(B,Q\), and every
\([y_k]_<\) are constant.  On such a cell,

\[
 L_T=
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 +2\sum_{k=1}^{B}\eta_k-Q-J
 +\frac{(v-B)_+^2}{\beta}.
\tag{1.1}
\]

**Proposition 1.**  The function
\(\Psi^{L_T}_{4,E}(t)\) is strictly increasing on every terminal count
cell.  It remains increasing through the continuous top-activation seam,
the \(L_T=0\) seam, and the maximum switch in (0.3).  In particular, it has
no interior stationary point.

### 1.2 Dependencies

The proof uses only:

1. the Round 10 exact complete-terminal formula (1.1);
2. the Round 28 endpoint derivative and hard-gap monotonicity;
3. the Round 28 definitions (0.3)--(0.5); and
4. elementary implicit differentiation.

No terminal lower compression and no Cmax sign is used.

### 1.3 Shelf and projected-payment derivatives

For fixed \(\mu\), direct differentiation gives

\[
 P_z:=\frac{d}{dt}A_t(z)
 =\frac{\mu\sin t}{\pi\cos^2t}
 \sqrt{1-\left(\frac{z\cos t}{\mu}\right)^2}.
\tag{1.2}
\]

Because \(r,x<\mu\), both square roots in (1.2) are strictly larger than
\(\sin t\).  Therefore

\[
 P_r>W',\qquad P_x>W',\qquad
 W'=\frac{\mu}{\pi}\tan^2t,
\tag{1.3}
\]

and

\[
 E'=P_r+P_x>2W'.
\tag{1.4}
\]

The factor \(\tau\) is fixed when \(\alpha\) is fixed, while
\(\lambda'=-W'\).  Hence

\[
 U'=\tau(E'-2W')>0.
\tag{1.5}
\]

Also,

\[
 \mathcal K_4'
 =\frac{(x^2-r^2)\sin t}{2\pi\mu}
 +\frac{(x^4-r^4)\cos^2t\sin t}{8\pi\mu^3}>0.
\tag{1.6}
\]

Both members of the maximum (0.3) are strictly increasing, so \(M_4\) is
strictly increasing, including through their continuous switch.

Round 28 proves that

\[
 H(t):=E(t)-E_*(t)
\tag{1.7}
\]

is strictly increasing on \(p>d(t)m\).  For reference,

\[
 E_*'=\frac{m}{p\pi}.
\]

The activity wall gives \(W'>1+\sec t\), while
\(\cos t<\pi d\) and \(p>dm\) give

\[
 \frac{m}{p\pi}<\frac1{\pi d}<\sec t.
\]

Together with (1.4), this yields \(H'>0\).

### 1.4 Inverse-level derivatives

Put

\[
 \phi(\theta)=\sin\theta-\theta\cos\theta.
\]

Since \(K'/K=\tan t\) and
\(\phi'(\theta)=\theta\sin\theta\), implicit differentiation gives

\[
 \boxed{
 \theta_k'
 =-\tan t\,
 \frac{\sin\theta_k-\theta_k\cos\theta_k}
 {\theta_k\sin\theta_k}<0.}
\tag{1.8}
\]

Consequently

\[
\begin{aligned}
 y_k'
 &=K\tan t\cos\theta_k-K\sin\theta_k\,\theta_k'\\
 &=\boxed{
 K\tan t\,\frac{\sin\theta_k}{\theta_k}>0.}
\end{aligned}
\tag{1.9}
\]

On a fixed inverse-floor cell,

\[
 \eta_k'=y_k'>0,
\tag{1.10}
\]

and

\[
 \left(\frac{\pi}{2\theta_k}\right)'
 =\frac{\pi\tan t}{2}
 \frac{\sin\theta_k-\theta_k\cos\theta_k}
 {\theta_k^3\sin\theta_k}>0.
\tag{1.11}
\]

### 1.5 Top-interval derivative

Let

\[
 \vartheta=\arccos(q/K)=\pi\beta,\qquad
 v=\frac q\pi(\tan\vartheta-\vartheta).
\]

Then

\[
 v_\vartheta=\frac q\pi\tan^2\vartheta
\]

and

\[
 \vartheta v_\vartheta-v
 =\frac q\pi
 \left(\vartheta\sec^2\vartheta-\tan\vartheta\right)>0,
\tag{1.12}
\]

because the bracket vanishes at zero and has derivative

\[
 2\vartheta\sec^2\vartheta\tan\vartheta>0.
\]

When \(v>B\), the top term is

\[
 T=\frac{(v-B)^2}{\beta}
 =\frac{\pi(v-B)^2}{\vartheta},
\]

so

\[
 \frac{dT}{d\vartheta}
 =\frac{\pi(v-B)}{\vartheta^2}
 \left(2\vartheta v_\vartheta-(v-B)\right)>0.
\tag{1.13}
\]

When \(v\leq B\), \(T=0\).  At \(v=B\), it is continuous with zero
one-sided derivative.

On a terminal count cell, \(Q\) and \(J\) are constant.  Equations
(1.8)--(1.13) show that \(L_T\) is strictly increasing.  If \(B=0\), its
top triangle is strictly increasing; if \(B\geq1\), the inverse-level terms
already give strict increase.

Therefore \(\max\{0,L_T\}\) is nondecreasing, \(a_pM_4\) is increasing,
and \(pH\) is strictly increasing.  This proves Proposition 1.

### 1.6 Exact count-wall audit

The proposition is cellwise, not a claim of global continuity.

1. **Inverse spatial wall.**  At \(y_k=j\in\mathbb N\), literal ownership
   has \([y_k]_< =j-1\) and \(\eta_k=1\).  Immediately right,
   \(\eta_k\downarrow0\).  Hence
   \[
    L_T^+-L_T^-=-2.
   \tag{1.14}
   \]
2. **Terminal shell-action wall.**  At
   \(A_t(q)+1/4=N\), \(Q\) changes from \(N-1\) to \(N\), so
   \[
    L_T^+-L_T^-=-1.
   \tag{1.15}
   \]
3. **Outer action wall.**  At \(v+1/4=N\), the literal count is
   \(B^-=N-1\).  The old top term is \(9/(16\beta)\).  Immediately right,
   the new level has \(\theta_N\to\pi\beta\), \(y_N\downarrow0^+\), and
   \(\eta_N\downarrow0\), while the new top term is zero.  Thus
   \[
    L_T^+-L_T^-=
    \frac1{2\beta}-\frac9{16\beta}
    =-\frac1{16\beta}.
   \tag{1.16}
   \]
   This uses the exact Round 10 top triangle also for the first
   \(B=0\to1\) wall.  The frozen Round 27--28 diagnostic implementation
   set that top term to zero when \(B=0\), producing a weaker diagnostic
   lower bound on those records; it is not the definition used here.
4. If \(\alpha=0\), then \(q=\mu\) and a \(B\)-wall may coincide with a
   \(Q\)-wall.  Their combined jump is
   \[
    -1-\frac1{16\beta}.
   \]
   Each simultaneous old inverse wall contributes another \(-2\).
5. The top activation \(v=B\), the maximum switch, and the seam \(L_T=0\)
   are continuous and create no new candidate.
6. At \(E=E_*\),
   \[
    \Psi^{L_T}_{4,E}
    =\max\{0,L_T\}+a_pM_4
    \geq a_p\mathcal K_4>0.
   \]
   Equality belongs to the automatic sector.

If \(L_T\) has a downward jump of size \(c_0\), then

\[
 \max(0,L_T-c_0)-\max(0,L_T)\in[-c_0,0].
\]

Thus the exact right-side value, not an assumed full jump of
\(\Psi^{L_T}_{4,E}\), is the candidate.

For fixed \((r,p,m,f,\alpha)\), every infimum is now reduced to:

- the included lower shelf endpoint or excluded activity right limit;
- the bad right side of an inverse wall;
- the bad right side of a \(Q\)-wall;
- the bad right side of a \(B\)-wall; or
- a coincident combination of these walls.

There are no stationary, top-payment, or maximum-switch candidates.

## 1A. Proposition: strict monotonicity on constant-\(K\) wall faces

### 1A.1 Statement

Fix \((r,p,m,f)\), put \(x=r+p\), \(q=x+m\), and let

\[
 \mu=q+\alpha,\qquad t=\arccos(\mu/K)
\]

vary along a connected exact hard-sector wall arc with \(K\) fixed.  Split
the arc whenever \(Q=[A(q)+1/4]_<\) or an ordinary shelf owner changes, and
fix the selected literal or one-sided terminal labels.

The inherited high-floor extension-grid domain has

\[
 p,m\geq1,\qquad
 r\geq1\ \hbox{on the integer grid},\qquad
 r\geq\frac32\ \hbox{on the half-integer grid},
\]

\[
 0<r<x<q\leq\mu<K,\qquad 0<t<\frac\pi2.
\tag{K.0}
\]

In particular all divisions by \(z\), \(\cos\chi_z\), and the square-root
radii below are legitimate, and \(q\geq3\).  This proposition makes no
claim about an extraneous \(r=0\) or \(p=0\) extension.

Inverse walls have this form because

\[
 G_K(q+j)=k-\frac14
\]

fixes \(K\).  Complete-terminal outer \(B\)-walls also have this form because

\[
 G_K(q)=N-\frac14
\]

fixes \(K\).  A \(Q\)-wall, shelf wall, or activity wall does not generally
fix \(K\).

**Proposition 1A.**  On every constant-\(K\), fixed-\(Q\) inverse- or
\(B\)-wall segment, the complete scalar \(\Psi^{L_T}_{4,E}\) is strictly
decreasing in \(\mu\).  Hence no stationary point occurs on such a wall.

The dependencies are the exact Round 10 terminal formula, the Round 21
shell-increment elasticity theorem, the Round 28 exact projected scalar,
and elementary differentiation of the ball action.  No diagnostic sign or
finite search is used.

### 1A.2 A normalized fixed-\(K\) comparison

For \(z=r,x\), write

\[
 \chi_z=\arccos(z/\mu),\qquad
 \psi_z=\arccos(z/K),\qquad
 u_z=\sqrt{\mu^2-z^2},
\]

and define

\[
 A(z):=A_t(z),\qquad
 e_z:=A(z)+\frac14-f,
 \qquad
 \mathfrak b_z:=A(z)-W=\lambda+e_z>0,
 \qquad W=G_K(\mu).
\tag{K.1}
\]

At fixed \(K\),

\[
 \frac{d}{d\mu}G_\mu(z)=\frac{\sin\chi_z}{\pi},
 \qquad
 \frac{d}{d\mu}G_K(\mu)=-\frac t\pi,
\]

so

\[
 \mathfrak b_z'=\frac{t-\sin\chi_z}{\pi}.
\tag{K.2}
\]

The radius-average identity gives

\[
 \mathfrak b_z
 =\frac{u_z^2}{\pi}
 \int_\mu^K
 \frac{da}
 {a\{\sqrt{a^2-z^2}+\sqrt{a^2-\mu^2}\}}.
\tag{K.3}
\]

Put \(I_z=\mathfrak b_z/u_z^2\).  Since
\((u_z^2)'=2\mu\),

\[
 I_z'
 =\frac{u_z^2\mathfrak b_z'-2\mu\mathfrak b_z}{u_z^4}.
\tag{K.4}
\]

If \(t\leq\sin\chi_z\), equations (K.1)--(K.2) immediately give
\(I_z'<0\).  Suppose \(t>\sin\chi_z\).  Because

\[
 \sqrt{a^2-\mu^2}<\sqrt{a^2-z^2}
 \qquad(\mu<a<K),
\]

(K.3) implies

\[
 \mathfrak b_z>
 \frac{u_z^2}{2\pi}
 \int_\mu^K\frac{da}{a\sqrt{a^2-z^2}}
 =\frac{u_z^2(\psi_z-\chi_z)}{2\pi z}.
\tag{K.5}
\]

The angles obey

\[
 \cos\psi_z=\cos t\cos\chi_z
\]

and the elementary inequality

\[
 \frac{\psi_z-\chi_z}{\cos\chi_z}
 \geq t-\sin\chi_z.
\tag{K.6}
\]

To prove (K.6), put

\[
 F(t,\chi)=
 \psi-\chi-\cos\chi(t-\sin\chi).
\]

Then

\[
 F_t=\cos\chi\left(\frac{\sin t}{\sin\psi}-1\right)\leq0.
\]

At \(t=\pi/2\),

\[
 F=\frac\pi2-\chi-\cos\chi\left(\frac\pi2-\sin\chi\right).
\]

This vanishes at \(\chi=0,\pi/2\), and its derivative is

\[
 \sin\chi\left(\frac\pi2-2\sin\chi\right).
\]

It rises once and then falls once, so it is nonnegative.  This proves
(K.6).  Since \(z=\mu\cos\chi_z\), (K.5)--(K.6) give

\[
 2\mu\mathfrak b_z>
 \frac{u_z^2(t-\sin\chi_z)}{\pi}
 =u_z^2\mathfrak b_z'.
\]

Thus

\[
 \boxed{I_z'<0}
\tag{K.7}
\]

in all cases.

### 1A.3 Both \(M_4\) owners decrease

Put

\[
 u=u_r,\qquad v=u_x,\qquad
 P=u^2-v^2=x^2-r^2=p(2r+p).
\]

The exact shelf identities give

\[
 \mathfrak b_r+\mathfrak b_x=E+2\lambda.
\]

The Round 21 elasticity theorem is equivalent to

\[
 \frac{\mathfrak b_r}{\mathfrak b_x}\geq\frac uv.
\tag{K.8}
\]

Moreover,

\[
 \tau=\frac{u-v}{u+v}=\frac{P}{(u+v)^2}.
\]

With

\[
 \omega=\frac{u}{u+v},\qquad
 \bar\omega=\frac{v}{u+v},
\]

the elasticity member becomes

\[
 M_{\rm el}
 =\tau(\mathfrak b_r+\mathfrak b_x)
 =P\{\omega^2I_r+\bar\omega^2I_x\}.
\tag{K.9}
\]

Equation (K.8) gives

\[
 \omega I_r\geq\bar\omega I_x.
\]

Also,

\[
 \omega'
 =\frac{\mu(v/u-u/v)}{(u+v)^2}<0,
 \qquad \bar\omega'=-\omega'.
\]

Differentiating (K.9),

\[
 \frac{M_{\rm el}'}P
 =\omega^2I_r'+\bar\omega^2I_x'
 +2\omega'(\omega I_r-\bar\omega I_x)<0
\tag{K.10}
\]

by (K.7).

The curvature member has the fixed-\(K\) form

\[
 M_{\rm curv}
 =b_1(\mu^{-1}-K^{-1})
 +b_3(\mu^{-3}-K^{-3}),
\]

\[
 b_1=\frac{x^2-r^2}{2\pi}>0,\qquad
 b_3=\frac{x^4-r^4}{24\pi}>0.
\]

Therefore

\[
 M_{\rm curv}'=-\frac{b_1}{\mu^2}
 -\frac{3b_3}{\mu^4}<0.
\tag{K.11}
\]

The maximum \(M_4=\max\{M_{\rm el},M_{\rm curv}\}\) is strictly decreasing,
including through its continuous switch.

### 1A.4 The hard gap decreases

At fixed \(K\),

\[
 E'=-\frac{\sin\chi_r+\sin\chi_x}{\pi},
\]

\[
 E_*=\frac12-\frac{m}{2p}+\frac{mt}{p\pi},
 \qquad
 t'=-\frac1{K\sin t}.
\]

Hence

\[
 H':=(E-E_*)'
 =-\frac{\sin\chi_r+\sin\chi_x}{\pi}
 +\frac{m}{p\pi K\sin t}.
\tag{K.12}
\]

Let \(X=\mu-x=m+\alpha\geq1\).  Then

\[
 \sin\chi_x=\frac{\sqrt{X(2\mu-X)}}{\mu},
 \qquad
 \frac1{K\sin t}=\frac{\cot t}{\mu}.
\]

Since \(p>dm\) and

\[
 X(2\mu-X)>\mu,
\]

it is enough to prove

\[
 d^2\mu\geq\cot^2t.
\tag{K.13}
\]

If \(0<t\leq\pi/3\), activity gives

\[
 \mu>\frac{\pi\cos t}{1-\cos t}.
\]

The function

\[
 F(t)=\frac{\pi d^2(1+\cos t)}{\cos t}
\]

is decreasing there, because

\[
 (\log F)'
 =-\frac4{\pi d}
 +\frac{\sin t}{\cos t(1+\cos t)}
 \leq-\frac4\pi+\frac2{\sqrt3}<0.
\]

Thus

\[
 F(t)\geq F(\pi/3)=\frac\pi3>1,
\]

which proves (K.13).

If \(\pi/3\leq t<\pi/2\), put
\(\varepsilon=\pi/2-t\leq\pi/6\).  Monotonicity of
\(\tan\varepsilon/\varepsilon\) gives

\[
 \cot t=\tan\varepsilon
 \leq\frac{2\sqrt3}{\pi}\varepsilon
 =\sqrt3\,d.
\]

The extension grids have \(\mu\geq q\geq3\), so (K.13) follows again.
Consequently

\[
 p\sqrt{X(2\mu-X)}>m\cot t,
\]

and (K.12) gives the strict estimate

\[
 \boxed{H'<-\frac{\sin\chi_r}{\pi}<0.}
\tag{K.14}
\]

### 1A.5 Terminal part and wall orientation

On a constant-\(K\), fixed-\(Q\) segment, the complete Round 10 expression
is

\[
 L_T=\mathcal U(K)-Q-J(\mu),
\tag{K.15}
\]

where \(\mathcal U(K)\) contains every inverse and top term with its selected
literal or one-sided labels.  This includes the top triangle when \(B=0\).
Furthermore,

\[
 J'(\mu)
 =\frac{\mu}{\pi}
 \{\chi_q-\sin\chi_q\cos\chi_q\}\geq0.
\tag{K.16}
\]

Thus \(\max\{0,L_T\}\) is nonincreasing.  Equations
(K.10)--(K.11) and (K.14) now prove Proposition 1A.  At \(\alpha=0\),
\(J'=0\), but (K.14) remains strict.  The face \(\alpha=1\) is excluded;
its one-sided limit is an endpoint candidate.

Along \(K=\mathrm{const}\), \(A(q)\) strictly decreases with \(\mu\).
At \(A(q)+1/4=N\), strict ownership has \(Q=N-1\) at equality and \(Q=N\)
immediately to the left.  Hence \(-Q\) and \(L_T\) jump upward by one as
\(\mu\) increases through the wall.  The clipping
\(L_T\mapsto\max(0,L_T)\) makes the complete scalar jump weakly upward, by
an amount in \([0,1]\).  This statement concerns an isolated \(Q\)-wall
with the shelf labels fixed.  Each \(Q\)-fixed segment must be split there,
and its infimum is at its largest-\(\mu\) endpoint; at a coincident shelf,
activity, hard-sector, or \(\alpha\) endpoint all feasible one-sided values
remain candidates.  At an isolated \(Q\)-intersection the bad candidate is
the left limit.

Therefore inverse and outer-\(B\) wall faces have no \(\alpha\)-stationary
points.  Their remaining candidates are endpoint collisions with shelf,
\(Q\), activity, hard-sector, or \(\alpha\) faces.

## 2. Proposition: analytic closure of the primary inverse cell

### 2.1 Exact cell

Set

\[
 (r,p,m,f)=(1,2,2,2),\qquad
 q=5,\qquad \mu=5+\alpha,\qquad 0\leq\alpha<1.
\]

Then

\[
 a_p=\frac13,\qquad E_*=c:=\frac t\pi.
\tag{2.1}
\]

Let \(\mathcal C_+\) be the maximal connected exact hard-sector literal
cell whose closure contains \(\alpha=0,\ y_1\downarrow2^+\), and on which

\[
 B=Q=1,\qquad 2<y_1<3.
\tag{2.2}
\]

Write

\[
 \theta=\theta_1,\qquad
 y_1=K\cos\theta-5,\qquad
 \eta=y_1-2\in(0,1).
\]

On this cell the complete terminal formula is exactly

\[
 L_T=
 \frac{\pi}{2\theta}+2\eta-1-J
 +\frac{(v-1)^2}{\beta}.
\tag{2.3}
\]

### 2.2 The inverse-wall constants

Let \(K_0\) be defined by

\[
 G_{K_0}(7)=\frac34
\]

and put \(\theta_0=\arccos(7/K_0)\).  Then

\[
 \tan\theta_0-\theta_0=\frac{3\pi}{28}.
\tag{2.4}
\]

Exact alternating Taylor bounds give

\[
 \boxed{\frac45<\theta_0<\frac{2\pi}{7}.}
\tag{2.5}
\]

For the lower bound, a rational sine/cosine enclosure at \(4/5\) puts
\(\tan(4/5)-4/5\) strictly below \(3\pi/28\).  For the upper bound, the
positive tangent series at \(2\pi/7\) puts
\(\tan(2\pi/7)-2\pi/7\) strictly above \(3\pi/28\).
This series use is legitimate because \(2\pi/7<\pi/2\), inside its radius
of convergence.  The alternating sine/cosine quotients used in the exact
replay also lie below \(\pi/2\), and their displayed cosine denominators
are positive.
The exact residuals are replayed in
computations/general_d_round29_primary_face_rational_replay.py.

Also,

\[
 \cos\frac45
 <1-\frac12\left(\frac45\right)^2
 +\frac1{24}\left(\frac45\right)^4
 =\frac{1307}{1875}<\frac7{10}.
\]

Therefore

\[
 \boxed{K_0=\frac7{\cos\theta_0}>10.}
\tag{2.6}
\]

On \(\mathcal C_+\), \(y_1>2\) implies \(K>K_0\), so
\(\theta<\theta_0\).  Moreover,

\[
\begin{aligned}
 G_{K_0}(5)-\frac34
 &=\int_5^7\frac{\arccos(z/K_0)}{\pi}\,dz\\
 &>\frac{2\theta_0}{\pi}>\frac12.
\end{aligned}
\]

Since \(v=G_K(5)>G_{K_0}(5)\),

\[
 \boxed{\theta<\frac{2\pi}{7},\qquad v>\frac54.}
\tag{2.7}
\]

### 2.3 Terminal angle and exact cap

Because \(B=1\), strict counting gives \(v\leq7/4\).  If
\(\beta\geq2/5\), then

\[
 \tan(\pi\beta)-\pi\beta
 \geq\tan\frac{2\pi}{5}-\frac{2\pi}{5}
 >\frac{7\pi}{20}.
\]

Indeed,

\[
 \tan\frac{2\pi}{5}>
 \tan\frac{3\pi}{8}=1+\sqrt2>\frac{3\pi}{4}.
\]

It would follow that

\[
 v=\frac5\pi\{\tan(\pi\beta)-\pi\beta\}>\frac74,
\]

a contradiction.  Hence

\[
 \boxed{\beta<\frac25.}
\tag{2.8}
\]

Since \(\mu\geq q=5\),

\[
 c=\frac{\arccos(\mu/K)}{\pi}
 \leq\frac{\arccos(5/K)}{\pi}
 =\beta<\frac25.
\tag{2.9}
\]

The cap has the exact double-integral representation

\[
 J=\frac2\pi
 \int_{0\leq x\leq y\leq\alpha}
 \sqrt{1-\left(\frac{5+x}{5+y}\right)^2}\,dy\,dx.
\]

Since

\[
 1-\left(\frac{5+x}{5+y}\right)^2
 \leq\frac{2(y-x)}5,
\]

\[
 J\leq
 \frac8{15\pi}\sqrt{\frac25}\,\alpha^{5/2}
 <\frac19.
\tag{2.10}
\]

The last comparison follows, for example, from
\(\pi^2>49/5\):

\[
 \frac1{81}-\frac{128}{11025}
 =\frac{73}{99225}>0.
\]

### 2.4 Curvature and final positivity

Equations (2.2) and (2.6) give \(K>K_0>10\).  Since \(\mu<6\),

\[
 \cos t=\frac{\mu}{K}<\frac35.
\]

The exact quartic member therefore satisfies

\[
 \boxed{
 \mathcal K_4>
 \frac4{15\pi}>
 \frac{14}{165}.}
\tag{2.11}
\]

No owner decision is required because \(M_4\geq\mathcal K_4\).

From (2.3), (2.7), (2.8), and (2.10),

\[
\begin{aligned}
 L_T
 &>
 \frac74+2\eta-1-J+\frac{(1/4)^2}{2/5}\\
 &=\frac{29}{32}+2\eta-J\\
 &>\frac{229}{288}+2\eta>0.
\end{aligned}
\tag{2.12}
\]

Thus the maximum in (0.5) is literally \(L_T\).  Retaining both \(E\) and
\(\eta\), and using \(E\geq0\),

\[
\begin{aligned}
 \Psi^{L_T}_{4,E}
 &>
 \frac{29}{32}+2\eta-J
 +\frac{14}{495}+2E-\frac45\\
 &=\frac{2131}{15840}+2\eta+2E-J\\
 &>\boxed{
 \frac{371}{15840}+2\eta+2E>0.}
\end{aligned}
\tag{2.13}
\]

This closes the whole component \(\mathcal C_+\), not just its
\(\alpha=0\) boundary.

### 2.5 Equality-face audit

1. At \(\alpha=0\), \(J=0\); the face is included.
2. The face \(\alpha=1\) is excluded, but its one-sided limit obeys the same
   positive estimate.
3. The inequality \(2\theta_0/\pi>1/2\) used in (2.7) follows from
   \(\theta_0>4/5\) and \(\pi<16/5\).
4. At the literal wall \(y_1=2\),
   \([2]_< =1\) and \(\eta_1=1\).  Its scalar is exactly two units stronger
   than the bad-right limit \(y_1\downarrow2^+\).
5. At \(y_1=3\), \([3]_< =2\) and \(\eta_1=1\).  The literal wall is owned
   from the left; its bad-right side belongs to the next inverse cell.
6. At the distinguished \(\alpha=0\) face, \(q=\mu\), so \(B=Q\).
   First-drop feasibility gives \(\lambda>0\), hence \(v<7/4\); together
   with (2.7), this gives \(B=Q=1\).
7. On the connected component, \(B=Q=1\) are literal cell labels.  Their
   strict action walls terminate the component.
8. The top interval is strictly active because \(v>5/4\).

The proof uses neither activity nor curvature ownership.  Shelf data enter
only through the exact domain and \(E\geq0\).

## 3. Symbolic and exact-rational replays

The Mathematica file

computations/general_d_round29_cell_derivatives.wl

simplifies twelve phase/fixed-\(K\) derivative and wall identities and four
primary-face arithmetic identities to zero.  It prints

\[
 \text{round29CellDerivativeReplayOK=True}.
\]

The exact-rational file

computations/general_d_round29_primary_face_rational_replay.py

uses Fraction arithmetic, alternating Taylor bounds, and the classical
enclosure

\[
 \frac{333}{106}<\pi<\frac{22}{7}.
\]

It verifies every rational sign used in (2.5)--(2.13) and prints

\[
 \text{round29PrimaryFaceRationalReplayOK=True}.
\]

These replays check the printed analytic argument.  They are not searches
or compact residual certificates.

## 4. Adaptive cusp diagnostic

The coarse Round 28 \(\alpha\)-mesh placed its smallest sampled value at
\(\alpha=0,\ y_1\downarrow2^+\).  Adaptive wall intersection reveals a
smaller positive cusp.  It is defined exactly by

\[
 G_{K_0}(7)=\frac34,\qquad
 G_{K_0}(3)-G_{\mu_0}(3)=\frac74.
\tag{4.1}
\]

High-precision evaluation gives

\[
 \alpha_0=\mu_0-5
 =0.0384220378954707335\ldots,
\]

\[
 t_0=1.0973053056881178222\ldots,
\]

and, on the bad side \(y_1\downarrow2^+\),

\[
 \boxed{
 \Psi^{L_T}_{4,E}
 \longrightarrow
 0.8374553251557668081\ldots.}
\tag{4.2}
\]

The literal corner is exactly two units higher.  Along the inverse face the
diagnostic derivative with respect to \(\alpha\) is approximately

\[
 -1.09106001298,
\]

whereas along the lower shelf after the intersection it is approximately

\[
 1.93953359750.
\]

Thus global \(\alpha\)-monotonicity is false: the point is a wall--wall cusp
of the lower envelope.  This does not affect Proposition 2, whose rational
margin is uniform.

The reproducible diagnostic is

computations/general_d_round29_adaptive_cusp_diagnostic.py.

Its decimals are theorem-design evidence only.

## 5. Loss ledger

1. Proposition 1 differentiates the exact Round 28 selected scalar.  It
   introduces no new loss.
2. Proposition 1A differentiates the exact fixed-\(K\) scalar.  It discards
   no terminal term; the only inequalities are the audited Round 21
   elasticity comparison and lower bounds used solely to prove strict
   derivative signs.
3. Proposition 2 uses \(M_4\geq\mathcal K_4\), the strict cap bound
   \(J<1/9\), \(c<2/5\), and \(E\geq0\).
4. The actual \(\eta\), \(E\), and \(J\) remain visible through the decisive
   inequality before the final uniform constant.
5. No root-free scalar, Cmax sign, ratio owner, or finite diagnostic enters
   any implication chain.

## 6. Failure report and next lemma

The stationary-point part of the Round 28 target is now closed in stronger
form: there are no interior stationary points on any terminal count cell.
There are also no interior minima on fixed-\(Q\) inverse- or outer-\(B\)
wall segments, and the previously observed sharp inverse cell is closed
analytically with the uniform margin (2.13).

The remaining obstruction is an endpoint-intersection theorem.  After the
cell and constant-\(K\) reductions, one must prove positivity at:

\[
 \text{lower shelf/activity endpoint},\qquad
 Q\text{-wall intersections},\qquad
 \alpha\text{-faces},\qquad
 \text{simultaneous inverse/}B\text{ endpoint collisions},
\tag{6.1}
\]

on the nonconstant-\(K\) shelf, \(Q\), activity, and hard-sector faces.
The next analytic target should generalize the mechanism of Proposition 2
to the \(B=Q=1\) first inverse band, beginning with the next observed small
families such as

\[
 (r,p,m,f)=(1,4,3,2)
 \quad\hbox{and}\quad
 (3/2,2,2,2).
\]

If a uniform wall theorem fails, return to the exact scalar
\(\mathscr S\) and then the weighted aggregate.  Do not introduce a new
ratio ladder or compressed global sign.

## 7. Gate decision

The Round 29 phase-cell monotonicity, constant-\(K\) wall monotonicity, and
primary inverse-cell closure may be promoted as analytic lemmas.  High-floor
CST remains open because the nonconstant-\(K\) endpoint family (6.1) is not
yet positive on the continuum.  Pointwise assembly and the all-dimensional
theorem therefore remain open.
