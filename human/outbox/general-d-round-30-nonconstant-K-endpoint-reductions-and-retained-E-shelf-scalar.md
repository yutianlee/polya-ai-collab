# General dimension, Round 30: nonconstant-\(K\) endpoint reductions and a retained-\(E\) shelf scalar

Date: 19 July 2026  
Status: three analytic face reductions proved; the retained-\(E\) shelf sign remains open

## 0. Scope and theorem boundary

Continue on the exact Round 28 hard sector

\[
 p>d(t)m,\qquad
 0\leq E<E_*:=\frac12-\frac{d(t)m}{2p}<\frac12,
 \qquad d(t)=1-\frac{2t}{\pi},
\tag{0.1}
\]

with

\[
 x=r+p,\qquad q=x+m,\qquad
 \mu=q+\alpha,\qquad K=\mu\sec t.
\tag{0.2}
\]

Round 29 removed terminal-cell interiors and constant-\(K\) inverse- and
outer-\(B\)-wall interiors.  This note treats the surviving nonconstant-\(K\)
faces.  It proves:

1. on the included lower shelf \(A(x)=f-\tfrac14\), the complete terminal
   term is strictly increasing in \(\mu\) throughout the
   \(B=Q=1,\ 2<y_1<3\) band and is uniformly larger than \(7/10\);
2. the full lower-shelf candidate reduces, without discarding the actual
   endpoint remainder \(E\), to one explicit scalar
   \(\mathfrak F(q,r,p,m)\);
3. the open lower \(Q\)-wall has \(0<y_1<\alpha<1\), no inverse or \(B\)
   intersection, and a positive strictly increasing complete terminal term;
4. every \(B=Q=1\) inverse band with \(y_1>1\), in particular the observed
   first band \(2<y_1<3\), has no noncorner lower-\(Q\)-wall endpoint; and
5. on the \(\alpha=0,\ f=2,\ B=Q=1,\ 2<y_1<3\) face, all candidates with
   \(4/5\leq t<13/10\) are positive by a uniform analytic estimate.

The lower-shelf obstruction treated in this note is concentrated especially
on

\[
 \alpha=0,\qquad 0<t<\frac45.
\tag{0.3}
\]

The sign \(\mathfrak F>0\) is not proved here.  Likewise, no monotonicity of
the *full* projected scalar along a lower shelf or a \(Q\)-wall is asserted.
Thus high-floor CST, pointwise assembly, and the all-dimensional theorem
remain open.

Throughout,

\[
 G_R(z)=\frac1\pi\left(\sqrt{R^2-z^2}
 -z\arccos\frac zR\right),\qquad 0\leq z<R,
\tag{0.4}
\]

and \(I_R(z)=\int_z^R G_R(u)\,du\).  The selected Round 28 scalar is

\[
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*),
 \qquad
 a_p=\frac{p^2}{3(2r+p)}.
\tag{0.5}
\]

## 1. The included lower shelf

### 1.0 Activity is automatic throughout the first inverse band

This preliminary fact does not require the shelf wall.  Assume only

\[
 B=Q=1,\qquad 2<y_1<3,
\]

and put \(z=q+y_1\).  Then \(z>q+2\geq5\).  If \(\theta\) is the first
inverse angle, then

\[
 \tan\theta-\theta=\frac{3\pi}{4z}<\frac{3\pi}{20},
\]

so the exact comparison used again in Section 1.4 gives \(\theta<1\).
Since the outer phase is strictly smaller than \(\theta/\pi\) after \(z\),

\[
 \frac34=G_K(z)
 <(K-z)\frac{\theta}{\pi}
 <\frac{K-z}{\pi}.
\]

Therefore

\[
 D:=K-\mu=(K-z)+(y_1-\alpha)
 >\frac{3\pi}{4}+1.
\]

The function \(4\pi/(4+3\pi)\) increases in \(\pi\), so \(\pi<22/7\)
gives

\[
 \frac{\pi}{D}
 <\frac{4\pi}{4+3\pi}<\frac{44}{47}.
\]

Also \(K>z>5\).  Hence

\[
 \begin{aligned}
 K^2-\frac{\pi^2}{(1-\mu/K)^2}
 &=K^2\left(1-\frac{\pi^2}{D^2}\right)\\
 &>
 25\left\{1-\left(\frac{44}{47}\right)^2\right\}
 =\frac{6825}{2209}>2.
 \end{aligned}
\tag{1.0}
\]

This exceeds both inherited activity constants.  Thus no activity endpoint
survives anywhere in the \(B=Q=1,\ 2<y_1<3\) band.

### 1.1 Exact transport identities

Put \(h=f-\tfrac14\), and impose the ordinary-floor wall

\[
 A_{K,\mu}(x)=G_K(x)-G_\mu(x)=h.
\tag{1.1}
\]

This is the included lower shelf, so \(e_p=0\) and

\[
 E=e_0=A(r)-A(x).
\tag{1.2}
\]

Write

\[
 \psi_z=\arccos\frac zK,\qquad
 \chi_z=\arccos\frac z\mu.
\]

Since

\[
 \partial_R G_R(z)=\frac{\sin(\arccos(z/R))}{\pi},
\tag{1.3}
\]

implicit differentiation of (1.1), with \(\mu\) as parameter, gives

\[
 \boxed{
 \kappa:=\frac{dK}{d\mu}
 =\frac{\sin\chi_x}{\sin\psi_x}\in(0,1).}
\tag{1.4}
\]

Consequently

\[
 \boxed{
 \frac{dt}{d\mu}
 =\frac{\kappa\cos t-1}{K\sin t}<0.}
\tag{1.5}
\]

The ratio

\[
 R(z):=\frac{\sin\chi_z}{\sin\psi_z}
 =\frac K\mu
 \sqrt{\frac{\mu^2-z^2}{K^2-z^2}}
\tag{1.6}
\]

is strictly decreasing in \(z\).  Since \(r<x\),
\(R(r)>R(x)=\kappa\), and therefore

\[
 \boxed{
 \frac{dE}{d\mu}
 =\frac{\kappa\sin\psi_r-\sin\chi_r}{\pi}<0.}
\tag{1.7}
\]

Finally, with \(W=G_K(\mu)\) and \(\lambda=h-W\),

\[
 \frac{dW}{d\mu}
 =\frac{\kappa\sin t-t}{\pi},
 \qquad
 \boxed{
 \frac{d\lambda}{d\mu}
 =\frac{t-\kappa\sin t}{\pi}>0.}
\tag{1.8}
\]

Thus a shelf face moves in the direction opposite to a constant-\(K\)
inverse wall: \(K\) increases, \(t\) and \(E\) decrease, and \(\lambda\)
increases.

### 1.2 Exact cap derivative

Let

\[
 \chi=\arccos\frac q\mu,\qquad J=2I_\mu(q).
\]

Then

\[
 \boxed{
 \frac{dJ}{d\mu}
 =\frac{\mu}{\pi}
 \{\chi-\sin\chi\cos\chi\}.}
\tag{1.9}
\]

For \(0<\chi<\pi/2\),

\[
 \chi-\sin\chi\cos\chi
 <
 \frac{2\sin^3\chi}{3\cos\chi},
\tag{1.10}
\]

because the difference on the right vanishes at zero and has derivative

\[
 \frac{2\sin^4\chi}{3\cos^2\chi}>0.
\]

Since \(x\leq q-1\), \(q\geq3\), and \(\mu=q+\alpha\),

\[
 \kappa>\sin\chi_x
 \geq
 \frac{\sqrt{(\alpha+1)(2q+\alpha-1)}}{\mu}.
\]

Equations (1.9)--(1.10) give

\[
 \frac{J'}{\kappa}
 <
 \frac{2[\alpha(2q+\alpha)]^{3/2}}
 {3\pi q\sqrt{(\alpha+1)(2q+\alpha-1)}}
 <
 \frac{14}{9\pi}\sqrt{\frac75}
 <
 \frac{28}{45}<1.
\tag{1.11}
\]

At \(\alpha=0\), \(J'=0\).  Hence, on the full shelf face,

\[
 \boxed{J'<\kappa.}
\tag{1.12}
\]

### 1.3 Strict terminal monotonicity

Assume now

\[
 B=Q=1,\qquad 2<y_1<3.
\tag{1.13}
\]

Let \(\theta\) solve

\[
 \frac K\pi(\sin\theta-\theta\cos\theta)=\frac34,
 \qquad
 y_1=K\cos\theta-q,
\]

and put \(\eta_1=y_1-2\).  The exact terminal expression is

\[
 L_T=
 \frac{\pi}{2\theta}+2\eta_1-1-J+
 \frac{(v-1)_+^2}{\beta},
 \qquad
 v=G_K(q),\quad
 \beta=\frac1\pi\arccos\frac qK.
\tag{1.14}
\]

At fixed \(q\),

\[
 \theta_K=
 -\frac{\sin\theta-\theta\cos\theta}
 {K\theta\sin\theta}<0,
 \qquad
 (y_1)_K=\frac{\sin\theta}{\theta}>0.
\tag{1.15}
\]

The inverse-angle and top-interval terms are nondecreasing in \(K\).  Since
\(\sin\theta/\theta>2/\pi\), (1.12) gives

\[
 \frac{dL_T}{d\mu}
 >
 2\kappa\frac{\sin\theta}{\theta}-J'
 >
 \frac{4\kappa}{\pi}-J'>0.
\tag{1.16}
\]

Thus

\[
 \boxed{
 L_T\ \hbox{is strictly increasing in \(\mu\) on every
 \(B=Q=1,\ 2<y_1<3\) lower-shelf segment}.}
\tag{1.17}
\]

This is a terminal statement.  The signs of \(E'\) and of the other
projected payments prevent promotion of (1.17) to monotonicity of the full
\(\Psi^{L_T}_{4,E}\).

### 1.4 Uniform terminal reserve

The same band satisfies

\[
 \boxed{L_T>\frac7{10}.}
\tag{1.18}
\]

Indeed, \(q+y_1>q+2\geq5\), and

\[
 \tan\theta-\theta
 =\frac{3\pi}{4(q+y_1)}
 <\frac{3\pi}{20}.
\]

Exact Taylor bounds give

\[
 \tan1-1>\frac7{13}>\frac{3\pi}{20},
\]

so \(\theta<1\).  Moreover,

\[
 v>\frac34+\frac{2\theta}{\pi},
 \qquad \beta<\frac12.
\]

After discarding \(2\eta_1\), the inverse-angle and top terms are therefore
at least

\[
 F(\theta):=
 \frac{\pi}{2\theta}-1+
 2\left(\frac{2\theta}{\pi}-\frac14\right)_+^2.
\tag{1.19}
\]

The function \(F\) is decreasing on \(0<\theta\leq1\), separately on the
two sides of its positive-part seam.  Below the seam this is immediate.
Above it,

\[
 F'(\theta)=
 -\frac{\pi}{2\theta^2}
 +\frac8\pi\left(\frac{2\theta}{\pi}-\frac14\right)<0;
\]

indeed \(\theta\leq1\) and \(3<\pi\) make the negative term larger in
magnitude than \(3/2\), while the positive term is smaller than \(10/9\).
Consequently

\[
 F(1)>
 \frac{121}{212}+
 2\left(\frac{17}{44}\right)^2
 =\frac{44599}{51304}.
\tag{1.20}
\]

The exact cap inequality \(J\leq\alpha G_\mu(q)\), followed by
\(\alpha<1\) and \(\mu<q+1\), gives

\[
 J<G_{q+1}(q)
 <\frac{(2q+1)^{3/2}}{3\pi q(q+1)}
 \leq\frac{7^{3/2}}{36\pi}.
\tag{1.21}
\]

The middle inequality follows from

\[
 \sin\phi-\phi\cos\phi
 <\frac{\sin^3\phi}{3\cos\phi},
 \qquad
 \phi=\arccos\frac q{q+1},
\]

To verify the strict trigonometric inequality, put \(s=\tan\phi\).  After
division by \(\cos\phi\), its difference is

\[
 H(s)=\frac{s^3}{3\sqrt{1+s^2}}-s+\arctan s.
\]

It vanishes at zero and

\[
 H'(s)=
 \frac{s^2(2\sqrt{1+s^2}-1)(\sqrt{1+s^2}-1)}
 {3(1+s^2)^{3/2}}>0.
\]

The last displayed \(q\)-function decreases for \(q\geq3\).  Using
\(\sqrt7<8/3\) and \(333/106<\pi\), the difference between the rational
lower bound in (1.20) and the resulting cap upper bound exceeds \(7/10\):

\[
 \frac{44599}{51304}
 -\frac{5936}{35964}
 -\frac7{10}
 =\frac{9812441}{2306371320}>0.
\]

This proves (1.18), so the clipping in (0.5) is inactive on this face.

## 2. A retained-\(E\) intrinsic lower-shelf scalar

For \(j=2,3\), define

\[
 \tan\theta_j-\theta_j=\frac{3\pi}{4(q+j)},
 \qquad
 K_j=\frac{q+j}{\cos\theta_j}.
\tag{2.1}
\]

The inverse band \(2<y_1<3\) is exactly

\[
 K_2<K<K_3.
\tag{2.2}
\]

Put

\[
 \beta_2=\frac1\pi\arccos\frac q{K_2},
 \qquad
 J_{\max}=2I_{q+1}(q),
\]

\[
 T(q)=
 \frac{\pi}{2\theta_2}-1-J_{\max}+
 \frac{\left(\frac{2\theta_2}{\pi}-\frac14\right)_+^2}{\beta_2}.
\tag{2.3}
\]

The positive part in (2.3) is essential for large \(q\).  Section 1.4
applies also to this endpoint expression: \(\theta_2<1\) and
\(\beta_2<1/2\) give the same strict \(F(\theta_2)>44599/51304\)
bound, while the unit-cap form of (T3) gives

\[
 J_{\max}=2I_{q+1}(q)<G_{q+1}(q)<\frac{5936}{35964}.
\]

Consequently

\[
 T(q)>\frac7{10}.
\tag{2.4}
\]

Let

\[
 E_{\min}=
 \{G_{K_2}(r)-G_{K_2}(x)\}
 -\{G_{q+1}(r)-G_{q+1}(x)\},
\tag{2.5}
\]

\[
 \begin{aligned}
 \mathcal K_{4,\min}={}&
 \frac{\{(q+1)^{-1}-K_2^{-1}\}(x^2-r^2)}{2\pi}\\
 &+
 \frac{\{(q+1)^{-3}-K_2^{-3}\}(x^4-r^4)}{24\pi},
 \end{aligned}
\tag{2.6}
\]

and

\[
 d_{\min}
 =1-\frac2\pi\arccos\frac q{K_3}.
\tag{2.7}
\]

The shell slope

\[
 \frac1\pi\left\{
 \arccos\frac zK-\arccos\frac z\mu\right\}
\]

increases with \(K\) and decreases with \(\mu\).  Since
\(K>K_2\), \(K<K_3\), \(q\leq\mu<q+1\), the actual lower-shelf quantities
satisfy

\[
 E\geq E_{\min},\qquad
 \mathcal K_4\geq\mathcal K_{4,\min},\qquad
 d\geq d_{\min}.
\tag{2.8}
\]

Also \(K>K_2\) makes the inverse-angle and top terms no smaller than their
\(K_2\) values, \(2\eta_1>0\), and \(J<J_{\max}\).  Therefore
\(L_T>T(q)\).  Using this fact and \(M_4\geq\mathcal K_4\) in (0.5) now
gives the proof-level reduction

\[
 \boxed{
 \Psi^{L_T}_{4,E}
 >
 \mathfrak F(q,r,p,m),}
\tag{2.9}
\]

where

\[
 \boxed{
 \mathfrak F(q,r,p,m):=
 T(q)+a_p\mathcal K_{4,\min}
 +p\left(E_{\min}-\frac12\right)
 +\frac{m d_{\min}}2.}
\tag{2.10}
\]

This reduction retains the actual endpoint remainder through
\(E\geq E_{\min}\).  It does not replace \(pE\) by \(p\mathcal K_4\).

There are two useful necessary domain conditions.  First, lower-shelf
feasibility implies

\[
 \boxed{
 G_{K_3}(x)-G_q(x)
 \geq f-\frac14\geq\frac74.}
\tag{2.11}
\]

Indeed, \(K_3\) and \(q\) maximize the shell action at \(x\) over (2.2)
and \(q\leq\mu<q+1\).  Since \(x=q-m\), (2.11) depends only on
\((q,m)\).  Second, hard-sector feasibility and (2.8) imply

\[
 p>d_{\min}m,\qquad
 E_{\min}<
 \frac12-\frac{d_{\min}m}{2p}.
\tag{2.12}
\]

After fixing \((q,m)\), the sole remaining continuous formula is
one-dimensional in the integer \(p\), with \(r=q-m-p\).  The identity

\[
 \boxed{K_3(q)=K_2(q+1)}
\tag{2.13}
\]

may be useful for the large-\(q\) comparison.

The sign

\[
 \mathfrak F(q,r,p,m)>0
\tag{2.14}
\]

on the exact parity grids and necessary domain (2.11)--(2.12) is the
principal unresolved retained-\(E\) lower-shelf inequality after this round.
Other endpoint families listed in Round 29 remain live unless they are
explicitly removed in Sections 3--4 below.

## 3. The lower \(Q\)-wall

### 3.1 Intrinsic parametrization and orientation

On the lower \(Q\)-wall,

\[
 A(q)=\frac34,\qquad 0<\alpha<1.
\tag{3.1}
\]

Put

\[
 \phi=\arccos\frac q\mu,\qquad
 \psi=\arccos\frac qK,\qquad
 F(u)=\tan u-u.
\]

Then

\[
 F(\psi)-F(\phi)=\frac{3\pi}{4q},
 \qquad
 \mu=q\sec\phi,\qquad K=q\sec\psi.
\tag{3.2}
\]

Implicit differentiation gives

\[
 \psi_\phi=\frac{\tan^2\phi}{\tan^2\psi},
 \qquad
 \boxed{
 \frac{dK}{d\mu}
 =\kappa_Q:=\frac{\sin\phi}{\sin\psi}\in(0,1),}
\tag{3.3}
\]

and

\[
 -\tan t\,\frac{dt}{d\mu}
 =\frac1\mu-\frac{\kappa_Q}{K}>0.
\tag{3.4}
\]

For \(z<q\), write

\[
 s_R(z)=\sqrt{1-\frac{z^2}{R^2}}.
\]

The ratio \(s_\mu(z)/s_K(z)\) decreases in \(z\) and equals
\(\kappa_Q\) at \(z=q\).  Hence

\[
 \boxed{
 \frac{dA(z)}{d\mu}
 =\frac{\kappa_Qs_K(z)-s_\mu(z)}{\pi}<0.}
\tag{3.5}
\]

Moreover

\[
 D(z):=s_\mu(z)-\kappa_Qs_K(z)
\]

strictly decreases in \(z\).  Therefore both \(E\) and
\(\Delta=e_0-e_p\) strictly decrease along the \(Q\)-wall.  The projected
curvature also decreases:

\[
 \frac{d\mathcal K_4}{d\mu}
 =
 b_1\{-\mu^{-2}+\kappa_QK^{-2}\}
 +3b_3\{-\mu^{-4}+\kappa_QK^{-4}\}<0,
\tag{3.6}
\]

where \(b_1,b_3>0\) are the coefficients from Round 29.  In contrast,
\(W'=(\kappa_Q\sin t-t)/\pi<0\), so \(\lambda\) increases.  These
opposing motions are why no full-\(\Psi\) monotonicity is asserted.

Equation (3.5) also proves that every shelf-action equation
\(A(z)=\text{constant}\) has at most one intersection with this \(Q\)-wall.

### 3.2 Exact count geometry

Let

\[
 h=G_\mu(q),\qquad v=G_K(q)=\frac34+h.
\]

Because \(q\geq3\), \(\alpha<1\), and \(q/\mu>3/4\),

\[
 h<\alpha\frac{\arccos(q/\mu)}{\pi}<\frac14.
\]

Thus

\[
 \frac34<v<1,\qquad B=1,
\tag{3.7}
\]

and the top interval is inactive.

Let \(\theta\) and \(y_1\) be the first inverse data:

\[
 G_K(q+y_1)=\frac34.
\]

The same number \(h\) has the two integral representations

\[
 h=\int_q^{q+y_1}\frac{\arccos(z/K)}{\pi}\,dz
   =\int_q^\mu\frac{\arccos(z/\mu)}{\pi}\,dz.
\tag{3.8}
\]

The outer phase is strictly larger than the inner phase wherever both are
defined.  Therefore

\[
 \boxed{0<y_1<\alpha<1.}
\tag{3.9}
\]

Consequently the open lower \(Q\)-wall contains no inverse spatial wall
and no outer-\(B\) wall.

### 3.3 Positive and increasing complete terminal term

On the bad \(Q=1\) side,

\[
 L_Q=\frac{\pi}{2\theta}+2y_1-1-J.
\tag{3.10}
\]

Here \(\theta<2\pi/5\).  Indeed,

\[
 \tan\theta-\theta
 =\frac{3\pi}{4(q+y_1)}<\frac{\pi}{4},
\]

whereas

\[
 \tan\frac{2\pi}{5}-\frac{2\pi}{5}
 >
 \tan\frac{3\pi}{8}-\frac{2\pi}{5}
 =1+\sqrt2-\frac{2\pi}{5}>\frac{\pi}{4}.
\]

The proved exact cap bound \(J<1/7\) now gives

\[
 \boxed{
 L_Q>\frac3{28}+2y_1>0.}
\tag{3.11}
\]

The term is also strictly increasing in \(\mu\).  Indeed,

\[
 \frac{dy_1}{d\mu}
 =\kappa_Q\frac{\sin\theta}{\theta}
 >
 \frac{\sin\phi}{\psi}
 >
 \frac{2\sin\phi}{\pi},
\tag{3.12}
\]

whereas

\[
 \frac{dJ}{d\mu}
 =\frac{\mu}{\pi}
 \{\phi-\sin\phi\cos\phi\}
 \leq\frac{2\alpha\sin\phi}{\pi}
 <\frac{2\sin\phi}{\pi}.
\tag{3.13}
\]

The inequality in (3.13) follows from

\[
 \phi-\sin\phi\cos\phi
 \leq2\sin\phi(1-\cos\phi).
\]

The difference between the right and left sides vanishes at zero and has
derivative \(2\cos\phi(1-\cos\phi)>0\).

The inverse-angle term in (3.10) also increases, so

\[
 \boxed{\frac{dL_Q}{d\mu}>0.}
\tag{3.14}
\]

Again, this is not a monotonicity theorem for the full projected scalar.

### 3.4 Ownership and intersections

At \(A(q)=3/4\), literal strict ownership has \(Q=0\); the phase-right
candidate has \(Q=1\) and the raw terminal jump is \(-1\).  At
\(\alpha=0\), also \(h=0\) and \(v=3/4\), so literal ownership is
\(B=Q=0\).  The phase-right combined jump is

\[
 -1-\frac1{16\beta},
\]

plus \(-2\) for each simultaneous inverse wall.  Here the first inverse
displacement is \(y_1=0\).

At the upper \(Q\)-wall \(A(q)=7/4\), the condition \(B=Q=1\) forces
\(\alpha=0\) and \(v=7/4\).  Literal ownership has \(B=Q=1\), and the
phase-right side has \(B=Q=2\), with the same combined jump formula.  The
literal upper corner has \(L_T>9/8\).

It follows that every \(B=Q=1\) inverse band

\[
 j<y_1<j+1,\qquad j\geq1,
\tag{3.15}
\]

has no noncorner \(Q\)-wall endpoint.  In particular the
\(2<y_1<3\) lower-shelf analysis in Sections 1--2 does not acquire an open
\(Q\)-wall endpoint.

The stronger diagnostic suggestion

\[
 \mathcal K_4\geq E_*
\quad\hbox{on the lower \(Q\)-wall}
\]

has not been proved and is not used.

## 4. The \(\alpha=0\) first inverse face

Assume in this section

\[
 \alpha=0,\qquad f=2,\qquad B=Q=1,\qquad 2<y_1<3.
\tag{4.1}
\]

Then

\[
 \mu=q,\qquad J=0,\qquad
 W=v=A(q),\qquad \frac34<W\leq\frac74.
\tag{4.2}
\]

### 4.1 Activity and the candidate set

The stronger result (1.0) makes activity automatic on the whole first
inverse band, hence in particular on this face.

At \(\alpha=0\), \(B=Q\).  The lower simultaneous \(B=Q\) wall
\(W=3/4\) has \(y_1=0\), so it cannot meet (4.1).  Round 29 phase
monotonicity therefore leaves only

\[
 y_1\downarrow2^+
 \qquad\hbox{or}\qquad
 A(x)=\frac74
\tag{4.5}
\]

as lower-\(t\) candidates.

### 4.2 A complete terminal bound

Let \(\theta=\theta_1\), \(\eta_1=y_1-2\), and put

\[
 \xi=\frac{2\theta}{\pi},\qquad c=\frac t\pi.
\]

The function

\[
 b(z)=\frac1\pi\arccos\frac zK
\]

is strictly concave.  Hence

\[
 W-\frac34
 =\int_q^{q+y_1}b(z)\,dz
 >
 \frac{y_1}{2}\left(c+\frac{\theta}{\pi}\right)
 >c+\frac{\theta}{\pi}.
\tag{4.6}
\]

If \(\xi<1/2\), then \(1/\xi-1>1\).  At \(\xi=1/2\), (4.6) gives
\(W>5/4\), so the inverse contribution equals one and the top interval is
strictly positive.  If \(\xi>1/2\), the top interval is active and

\[
 W-1>c+\frac{\xi}{2}-\frac14.
\]

Since \(c>\xi/2\), minimizing the resulting top payment over \(c\) gives

\[
 \frac{(W-1)^2}{c}>
 \frac{2(\xi-1/4)^2}{\xi}.
\]

Therefore

\[
 \frac1\xi-1+\frac{(W-1)^2}{c}
 >
 2\xi-2+\frac9{8\xi}\geq1.
\]

In both cases,

\[
 \boxed{L_T>1+2\eta_1.}
\tag{4.7}
\]

The strict estimate survives the bad limit \(y_1\downarrow2^+\).

### 4.3 Uniform curvature closure for \(t\geq4/5\)

On an ordinary first shelf, \(E\geq\Delta\geq M_4\geq\mathcal K_4\).
Retain only the quadratic member

\[
 K_1=\frac{(1-\cos t)p(2r+p)}{2\pi q}.
\]

Equations (0.5) and (4.7) give

\[
 \Psi^{L_T}_{4,E}
 >
 1+2\eta_1+(p+a_p)K_1-\frac{p-dm}{2}.
\tag{4.8}
\]

Normalize

\[
 R=\frac pm,\qquad u=\frac rm.
\]

Then

\[
 (p+a_p)K_1
 =
 m^2\frac{(1-\cos t)R^2(3u+2R)}
 {3\pi(u+R+1)}.
\tag{4.9}
\]

Minimization over the enlarged continuous domain \(m>0\) yields

\[
 (p+a_p)K_1-\frac{p-dm}{2}
 \geq
 -\frac{3\pi(u+R+1)(R-d)^2}
 {16(1-\cos t)R^2(3u+2R)}.
\]

Since

\[
 \frac{u+R+1}{3u+2R}
 <\frac{R+1}{2R},
\]

and

\[
 \sup_{R>d}
 \frac{(R+1)(R-d)^2}{R^3}
 =
 \max\left\{1,\frac{4(1+d)^3}{27d}\right\},
\]

we obtain

\[
 \boxed{
 \Psi^{L_T}_{4,E}
 >
 1+2\eta_1-H(t),}
\tag{4.10}
\]

where

\[
 H(t)=
 \frac{3\pi}{32(1-\cos t)}
 \max\left\{1,\frac{4(1+d)^3}{27d}\right\}.
\tag{4.11}
\]

The count \(B=1\) gives

\[
 \frac q\pi(\tan t-t)=W\leq\frac74.
\]

Since \(q\geq3\), exact Taylor bounds at \(13/10\) show

\[
 t<\frac{13}{10}.
\tag{4.12}
\]

More explicitly, the alternating bounds

\[
 \sin u>
 u-\frac{u^3}{6}+\frac{u^5}{120}-\frac{u^7}{5040},
 \qquad
 \cos u<
 1-\frac{u^2}{2}+\frac{u^4}{24}
\]

at \(u=13/10\), whose cosine denominator is positive, give

\[
 \tan\frac{13}{10}-\frac{13}{10}
 >
 \frac{30609129083}{13809810000}
 >\frac{11}{6}>\frac{7\pi}{12}.
\]

For \(4/5\leq t<13/10\), one has \(d<1/2\) and

\[
 H(t)=\frac{\pi(1+d)^3}{72d(1-\cos t)}.
\]

Its logarithmic derivative is

\[
 \frac{2(1-2d)}{\pi d(1+d)}-\cot\frac t2,
\tag{4.13}
\]

which is strictly increasing.  Thus \(H\) has at most one critical point,
necessarily a minimum.  For a transparent exact endpoint enclosure, rewrite
this branch as

\[
 H(t)=
 \frac{(\pi-t)^3}
 {9\pi(\pi-2t)(1-\cos t)}.
\]

Use

\[
 \frac{333}{106}<\pi<\frac{22}{7},
 \qquad
 1-\cos t>
 \frac{t^2}{2}-\frac{t^4}{24}.
\]

All denominator factors are positive on the present interval.  Direct
rational arithmetic gives

\[
 H\!\left(\frac45\right)
 <
 \frac{19359908900}{19876504599}<1,
\]

\[
 H\!\left(\frac{13}{10}\right)
 <
 \frac{357336260800}{634633671763}<1.
\]

Therefore

\[
 \boxed{
 \Psi^{L_T}_{4,E}>2\eta_1\geq0
 \qquad
 \left(\frac45\leq t<\frac{13}{10}\right).}
\tag{4.14}
\]

The bad limit \(\eta_1\downarrow0\) remains strict because \(H<1\).

## 5. Equality-face audit

1. The lower shelf \(e_p=0\) uses the ordinary floor and is included.
2. The face \(\alpha=0\) is included and has \(J=0\); \(\alpha=1\) is
   excluded.
3. At literal \(y_1=2\), strict inverse ownership gives \(\eta_1=1\).
   The candidate for the cell on its right is the excluded limit
   \(\eta_1\downarrow0\), exactly two units lower.
4. At literal \(y_1=3\), \(\eta_1=1\) and the wall is owned from the left.
   The bad-right side belongs to the next inverse band.
5. The lower \(Q\)-wall has literal \(Q=0\), not \(Q=1\).  The
   phase-right value is the relevant \(Q=1\) candidate.
6. At \(\alpha=0\), a simultaneous \(B/Q\) wall uses literal strict
   ownership for both counts.  All one-sided raw jumps in Section 3.4 are
   retained.
7. The seam \(E=E_*\) belongs to the automatic sector and is already
   positive.

## 6. Diagnostics and failure report

The intrinsic scalar (2.10) was scanned only as theorem-design evidence.
The reproducible program

computations/general_d_round30_retained_shelf_diagnostic.py

uses the positive part in (2.3), both parity grids, and both necessary
conditions (2.11)--(2.12).  Through \(q=300\), it retained 933 relaxed
discrete records and found no negative value.  Its smallest value was

\[
 \mathfrak F(5,1,3,1)
 =0.30090314669\ldots.
\tag{6.1}
\]

No retained record occurred above \(q=33\) in that finite scan; a separate
run through \(q=1000\) returned the same 933 records.  This suggests that
(2.11)--(2.12) may themselves yield a finite analytic reduction, but the
observation has no infinite-\(q\) coverage and is not a premise of any
result above.

On the unresolved \(\alpha=0,\ t<4/5\) lower-shelf face, the same program
replays the seven previously observed patterns

\[
 p=m=2,
\]

with

\[
 r=16,17,18
\]

on the integer grid and

\[
 r=\frac{31}{2},\frac{33}{2},\frac{35}{2},\frac{37}{2}
\]

on the half-grid.  It does not prove that this list is exhaustive.  The
smallest replayed value of
\(1+2\eta_1-H(t)\) exceeded \(1.72\).  This seven-pattern list is not a
proved finite reduction.

The exact live lower-shelf obstruction isolated here is:

\[
 \boxed{
 \mathfrak F(q,r,p,m)>0
 \quad\hbox{under (2.11)--(2.12)},}
\tag{6.2}
\]

or an equally strong direct proof on the remaining lower-shelf image.  A
proof should first exploit the one-dimensional \(p\)-structure and the
interlacing identity (2.13).  If this retained-\(E\) endpoint route fails,
the revised strategy requires returning to the exact scalar
\(\mathscr S\), then to the weighted aggregate; it does not authorize a new
ratio ladder or another globally compressed surrogate.

The Mathematica 15 replay

computations/general_d_round30_endpoint_derivatives.wl

returns seventeen zero symbolic residuals.  It checks the action
derivatives, shelf and \(Q\)-wall transport identities, cap derivatives,
normalized curvature product, continuous quadratic minimum, intrinsic
\(R\)-supremum, \(H\)-derivative, and the exact rational arithmetic used
above.  It prints

\[
 \texttt{round30EndpointDerivativeReplayOK=True}.
\]

This is an identity replay, not a sign certificate for (6.2).

## 7. Gate decision

The shelf transport theorem, the \(Q\)-wall geometry, and the
\(\alpha=0,\ t\geq4/5\) closure are proof-level analytic gains.  They
shrink the nonconstant-\(K\) endpoint family but do not close high-floor
CST.  The general-dimensional theorem therefore remains proposed.

## 8. Reproduction

    & 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' -file computations/general_d_round30_endpoint_derivatives.wl

    python -B computations/general_d_round30_retained_shelf_diagnostic.py --limit 300
