# General-dimensional Round 31: retained-\(E\) convexity and a shell-ratio-free large-\(q\) exclusion

Date: 19 July 2026

Status: proved analytic reduction, independently checked.  This note proves
that the Round 30 necessary lower-shelf/hard domain is empty for every real
\(q\ge1000\), and proves strict convexity in \(p\) of the retained-\(E\)
scalar.  It does not close the finite range \(q<1000\), the other endpoint
families, high-floor CST, or the all-dimensional theorem.

## 0. Statement

Use the exact Round 30 definitions

\[
 \tan\theta_j-\theta_j=\frac{3\pi}{4(q+j)},\qquad
 K_j(q)=\frac{q+j}{\cos\theta_j},\qquad j=2,3,
\]

\[
 x=q-m,\qquad r=x-p,
\]

\[
 E_{\min}
 =
 \{G_{K_2}(r)-G_{K_2}(x)\}
 -\{G_{q+1}(r)-G_{q+1}(x)\},
\]

\[
 d_{\min}
 =1-\frac2\pi\arccos\frac q{K_3}.
\]

The retained lower-shelf scalar is

\[
 \mathfrak F(q,r,p,m)
 =
 T(q)+a_p\mathcal K_{4,\min}
 +p\left(E_{\min}-\frac12\right)
 +\frac{m d_{\min}}2,
 \qquad
 a_p=\frac{p^2}{3(2r+p)}.
\tag{0.1}
\]

Round 30 proves

\[
 \Psi^{L_T}_{4,E}>\mathfrak F
\tag{0.2}
\]

and shows that any retained hard lower-shelf point must satisfy

\[
 G_{K_3}(q-m)-G_q(q-m)\ge\frac74,
\tag{0.3}
\]

\[
 p>d_{\min}m,\qquad
 E_{\min}<\frac12-\frac{d_{\min}m}{2p}.
\tag{0.4}
\]

This round proves:

1. for fixed \((q,m)\), the continuous profile
   \(p\mapsto\mathfrak F(q,q-m-p,p,m)\) is strictly convex on
   \(0<p<q-m\);
2. (0.3)--(0.4) have no solution for any real \(q\ge1000\), hence on
   neither inherited parity grid; and
3. after using \(E_{\min}>\mathcal K_{4,\min}\) and \(T(q)>7/10\), the
   resulting finite lower scalar has no interior minimum on the full
   \((p,r,m)\)-triangle and reduces to three one-dimensional convex edge
   problems for each fixed \(q\).

The third reduction is not used for \(q\ge1000\); it is recorded for the
remaining finite range.

## 1. Dependencies

Only the following proved results are used:

- the Round 28 exact quartic curvature payment;
- the Round 29 inherited-grid scope;
- the Round 30 definitions of \(K_2,K_3,T,E_{\min},
  \mathcal K_{4,\min},d_{\min}\);
- the Round 30 inequalities \(T(q)>7/10\), (0.2), and the necessary
  conditions (0.3)--(0.4); and
- the elementary formulas
  \[
   \frac{\partial}{\partial R}G_R(z)
   =\frac1\pi\sqrt{1-\frac{z^2}{R^2}},
   \qquad
   -\frac{\partial}{\partial z}G_R(z)
   =\frac1\pi\arccos\frac zR.
  \]

No diagnostic cutoff, ratio threshold, or certificate is a dependency.

## 2. Strict convexity of the full retained-\(E\) scalar

Fix \(q,m\), and put

\[
 M=q+1,\qquad K=K_2(q),\qquad x=q-m,\qquad r=x-p.
\]

Thus

\[
 0<r<x<M<K.
\tag{2.1}
\]

Set

\[
 H(z)=G_K(z)-G_M(z),
\]

\[
 \sigma(z)=-H'(z)
 =\frac1\pi\left\{
  \arccos\frac zK-\arccos\frac zM
 \right\}>0.
\]

Then

\[
 E_{\min}(p)=H(x-p)-H(x)
 =\int_{x-p}^{x}\sigma(z)\,dz.
\tag{2.2}
\]

Write

\[
 c_1=\frac{M^{-1}-K^{-1}}{2\pi},\qquad
 c_3=\frac{M^{-3}-K^{-3}}{24\pi}.
\]

Since \(x^2-r^2=p(2x-p)\),

\[
 a_p\mathcal K_{4,\min}
 =\frac{p^3}{3}\{c_1+c_3(x^2+r^2)\}.
\tag{2.3}
\]

Only

\[
 \mathcal S(p)
 =a_p\mathcal K_{4,\min}
 +p\left(E_{\min}-\frac12\right)
\]

depends on \(p\) in (0.1).  If \(C\) denotes the right side of (2.3),
then

\[
 \mathcal S''(p)=C''(p)+2\sigma(r)-p\sigma'(r).
\tag{2.4}
\]

Using

\[
 M^{-1}-K^{-1}=\int_M^K a^{-2}\,da,
\qquad
 M^{-3}-K^{-3}=3\int_M^K a^{-4}\,da,
\]

gives

\[
 C''(p)
 =\frac1\pi\int_M^K
 \left\{
  \frac p{a^2}
  +\frac{p(r^2/2+p^2/3)}{a^4}
 \right\}\,da.
\tag{2.5}
\]

Also

\[
 \sigma(r)
 =\frac1\pi\int_M^K
 \frac{r}{a\sqrt{a^2-r^2}}\,da,
\]

\[
 \sigma'(r)
 =\frac1\pi\int_M^K
 \frac{a}{(a^2-r^2)^{3/2}}\,da.
\tag{2.6}
\]

At a fixed integration radius \(a\), put

\[
 u=\frac ra,\qquad v=\frac pa.
\]

By (2.1),

\[
 u,v\ge0,\qquad u+v<1.
\tag{2.7}
\]

The integrand of \(\pi\mathcal S''\), after multiplication by \(a\),
is

\[
 D(u,v)
 =
 \frac{2u}{\sqrt{1-u^2}}
+v\left\{
 1+\frac{u^2}{2}+\frac{v^2}{3}
 -(1-u^2)^{-3/2}
\right\}.
\tag{2.8}
\]

Let

\[
 A(u)=(1-u^2)^{-3/2}-1-\frac{u^2}{2}\ge0.
\]

Indeed, the binomial lower bound
\((1-u^2)^{-3/2}\ge1+3u^2/2\) gives \(A(u)\ge u^2\).

Because \(v<1-u\),

\[
 D(u,v)\ge
 \frac{2u}{\sqrt{1-u^2}}-(1-u)A(u)+\frac{v^3}{3}.
\tag{2.9}
\]

For

\[
 t=\sqrt{\frac{1-u}{1+u}}\in(0,1],
\]

the first two terms on the right of (2.9) factor exactly as

\[
 \frac{(1-t)(1+t-t^2+t^3)
 (3+9t^2+6t^3+11t^4+2t^5+t^6)}
 {4t(1+t^2)^3}\ge0.
\tag{2.10}
\]

Every factor is positive for \(0<t<1\).  At \(u=0\), the term
\(v^3/3\) in (2.9) is positive.  Therefore \(D(u,v)>0\), and
(2.4)--(2.6) yield

\[
 \boxed{\mathfrak F_{pp}>0.}
\tag{2.11}
\]

Thus each fixed-\((q,m)\) continuous \(p\)-profile has at most one
stationary point.  If it exists, the discrete minimum lies at one or two
adjacent integers bracketing it; otherwise the minimum is at the
appropriate interval endpoint.

## 3. Uniform phase bounds for \(q\ge1000\)

Assume

\[
 q\ge1000,\qquad s=q^{1/3}\ge10.
\]

Put

\[
 K=K_2(q),\quad
 \Delta=K-(q+1),\quad
 \delta=K-q,
\]

\[
 \psi=\arccos\frac q{K_3},\qquad
 d=d_{\min}=1-\frac{2\psi}{\pi}.
\]

For \(0<\theta<\pi/2\),

\[
 \frac{\theta^3}{3}
 \le\tan\theta-\theta
 \le\frac{\theta^3}{3\cos^2\theta}.
\tag{3.1}
\]

The left inequality and \(\pi<22/7\) give

\[
 \theta_2,\theta_3<\frac{48}{25s},
\tag{3.2}
\]

because

\[
 \left(\frac{48}{25}\right)^3-\frac{99}{14}
 =\frac{1413}{218750}>0.
\]

At \(s\ge10\), (3.2) gives

\[
 \cos^2\theta_j>
 \left(\frac{15337}{15625}\right)^2
 >\frac{24}{25},
\]

where

\[
 \left(\frac{15337}{15625}\right)^2-\frac{24}{25}
 =\frac{848569}{244140625}>0.
\]

Using the right inequality in (3.1), \(\pi>3\), and
\(q+2\le(501/500)q\), one obtains

\[
 \theta_2>\frac{93}{50s},
\tag{3.3}
\]

because

\[
 \frac{3240}{501}-\left(\frac{93}{50}\right)^3
 =\frac{672381}{20875000}>0.
\]

The elementary inequality

\[
 \sec\theta-1>\frac{\theta^2}{2}
\tag{3.4}
\]

follows because the derivative of
\(\sec\theta-1-\theta^2/2\) is
\(\sec\theta\tan\theta-\theta>0\).  Equations (3.2)--(3.4) give

\[
 \boxed{\Delta>\frac{17}{10}s.}
\tag{3.5}
\]

The last rounding has the exact margin

\[
 \frac12\left(\frac{93}{50}\right)^2-\frac{17}{10}
 =\frac{149}{5000}>0.
\]

Conversely,

\[
 \sec\theta-1
 <\frac{\theta^2}{2\cos\theta}.
\]

Together with (3.2), \(2\le s/5\), and
\(q+2\le(501/500)q\), this gives

\[
 \delta<
 \frac{31925}{15337}s
 <\frac{21}{10}s,
\tag{3.6}
\]

where

\[
 \frac{21}{10}-\frac{31925}{15337}
 =\frac{2827}{153370}>0.
\]

In particular,

\[
 \boxed{K<\frac{103}{100}q.}
\tag{3.7}
\]

At \(s\ge10\), the final rounding has margin

\[
 \frac{103}{100}
 -\left(1+\frac{21}{1000}\right)
 =\frac9{1000}>0.
\]

For the \(K_3\)-angle,

\[
 \cos\psi=\frac{q\cos\theta_3}{q+3}.
\]

Hence

\[
 1-\cos\psi
 <\frac3q+\frac{\theta_3^2}{2}
 \le\frac{2679}{1250s^2}.
\tag{3.8}
\]

Now

\[
 \frac{191}{6144}-\frac{2679}{125000}
 =\frac{926903}{96000000}>0,
\]

and the alternating cosine estimate gives
\(1-\cos(1/4)>191/6144\).  Thus \(\psi<1/4\).  A second alternating
estimate yields

\[
 1-\cos\psi>\frac{191}{384}\psi^2.
\]

Combining this with (3.8) proves

\[
 \boxed{\psi<\frac{21}{10s},}
\tag{3.9}
\]

because

\[
 \frac{441}{100}
 -\frac{384}{191}\frac{2679}{1250}
 =\frac{48303}{477500}>0.
\]

Since \(\pi>3\) and \(s\ge10\),

\[
 \boxed{d>\frac{43}{50}.}
\tag{3.10}
\]

## 4. Shelf feasibility forces \(m>11s/10\)

By the definition of \(K_3\),

\[
 G_{K_3}(q+3)=\frac34.
\tag{4.1}
\]

The outer phase on \([q,q+3]\) is at most \(\psi\), and is strictly
smaller for \(z>q\), so

\[
 G_{K_3}(q)<\frac34+\frac{3\psi}{\pi}.
\tag{4.2}
\]

For \(z<q\), the phase difference

\[
 \arccos\frac z{K_3}-\arccos\frac zq
\]

increases with \(z\) and is bounded above by its value \(\psi\) at
\(z=q\).  Therefore, for \(x=q-m\),

\[
 G_{K_3}(x)-G_q(x)
 <\frac34+\frac{(m+3)\psi}{\pi}.
\tag{4.3}
\]

The necessary shelf condition (0.3) now implies

\[
 1<\frac{(m+3)\psi}{\pi}.
\]

Using \(\pi>3\) and (3.9),

\[
 m>\frac{10}{7}s-3>\frac{11}{10}s.
\tag{4.4}
\]

The final inequality has the exact endpoint margin

\[
 \left(\frac{10}{7}-\frac{11}{10}\right)10-3
 =\frac27>0.
\]

## 5. A retained-\(E\) lower bound

Let \(P=cm<x\), and let

\[
 r_P=x-P=q-(1+c)m.
\]

Define

\[
 b(z)=\frac1\pi\left\{
  \arccos\frac zK-\arccos\frac z{q+1}
 \right\}.
\]

Radial integration gives

\[
 b(z)
 =\frac1\pi\int_{q+1}^{K}
 \frac{z}{a\sqrt{a^2-z^2}}\,da.
\]

The integrand decreases with \(a\).  Moreover,

\[
 K^2-z^2<2K(K-z)
 \le2K\{\delta+(1+c)m\}
\]

on \(r_P\le z\le x\).  Consequently

\[
 E_{\min}(p)>E_{\min}(P)\ge B_c(m),
\tag{5.1}
\]

whenever \(P<p\), where

\[
 \boxed{
 B_c(m)
 =
 \frac{\Delta c m\{2q-(2+c)m\}}
 {2\pi K\sqrt{2K\{\delta+(1+c)m\}}}.}
\tag{5.2}
\]

This retains the exact \(E\)-kernel.  It is not the quartic truncation.

## 6. Removing the \(m\)-variable

For fixed \(c>0\), the \(m\)-dependent factor in (5.2) is

\[
 f_c(m)
 =
 \frac{m\{2q-(2+c)m\}}
 {\sqrt{\delta+(1+c)m}}.
\]

The sign of its derivative is the sign of

\[
 Q_c(m)
 =
 4q\delta
 +\{2(1+c)q-4(2+c)\delta\}m
 -3(2+c)(1+c)m^2.
\tag{6.1}
\]

This concave quadratic has one negative and one positive root.
Thus \(f_c\) has exactly one positive critical point, a maximum.
On the closure of

\[
 M_*=\frac{11}{10}s\le m<\frac q{1+c},
\]

the infimum is at one of the two endpoints.

The upper-to-lower endpoint ratio is strictly larger than

\[
 R(c)
 =
 \frac{50c}{11(1+c)^2}
 \sqrt{\frac{10(28+11c)}{103}}.
\tag{6.2}
\]

The derivative of \(R(c)^2\) has the sign of

\[
 56-23c-11c^2,
\]

so \(R\) has one interior maximum.  On
\(43/50\le c\le10\), its minimum occurs at an endpoint.  Exact
calculation gives

\[
 R(43/50)^2-1
 =\frac{3396674029937}{932297220063}>0,
\]

\[
 R(10)^2-1
 =\frac{162529217}{182470783}>0.
\]

Therefore

\[
 \boxed{B_c(m)\ge B_c(M_*)}
\tag{6.3}
\]

throughout this range.

## 7. Nine-step hard-sector bootstrap

Put

\[
 u=\frac{p}{dm}>1.
\]

Suppose inductively that \(u>\lambda\), where

\[
 \lambda\in
 \left\{
 1,\frac{25}{17},\frac53,2,\frac{25}{11},
 \frac52,3,4,10
 \right\}.
\]

Choose

\[
 P=\lambda d m=cm<p.
\]

Since \(43/50<d<1\),

\[
 \frac{43\lambda}{50}<c<\lambda\le10.
\]

In (5.2) at \(m=M_*\), use the lower bound for \(c\) only in
the favorable prefactor, and the upper bound \(c<\lambda\) separately
in the two adverse occurrences.  Equations (3.5)--(3.7) give

\[
 E_{\min}>C_\lambda
 =\frac{N_\lambda}{D\sqrt{R_\lambda}},
\tag{7.1}
\]

where

\[
 N_\lambda
 =
 \frac{17}{10}\frac{43\lambda}{50}\frac{11}{10}
 \left\{2-\frac{11(2+\lambda)}{1000}\right\},
\]

\[
 D=\frac{44}{7}\frac{103}{100},
\qquad
 R_\lambda=\frac{103(32+11\lambda)}{500}.
\]

All factors are positive.  For a positive rational \(h\),
\(C_\lambda>h\) is equivalent to the exact rational inequality

\[
 N_\lambda^2-h^2D^2R_\lambda>0.
\]

The complete comparison table is:

| \(\lambda\) | \(h\) | exact positive residual |
|---:|---:|---:|
| \(1\) | \(4/25\) | \(614330619919841/1225000000000000\) |
| \(25/17\) | \(1/5\) | \(395473621015143/80920000000000\) |
| \(5/3\) | \(1/4\) | \(1690109506680529/3969000000000000\) |
| \(2\) | \(7/25\) | \(1181252902401/390625000000\) |
| \(25/11\) | \(3/10\) | \(13049143106121/1960000000000\) |
| \(5/2\) | \(1/3\) | \(4446576884107303/1008000000000000\) |
| \(3\) | \(3/8\) | \(447338606701041/49000000000000\) |
| \(4\) | \(9/20\) | \(418992011999341/19140625000000\) |
| \(10\) | \(1/2\) | \(456264879163841/765625000000\) |

The hard upper bound (0.4) is

\[
 E_{\min}<\frac12\left(1-\frac1u\right).
\tag{7.2}
\]

Combining (7.1)--(7.2) successively gives

\[
 u>
 1,\frac{25}{17},\frac53,2,\frac{25}{11},
 \frac52,3,4,10.
\]

At the last step, (7.1) gives \(E_{\min}>C_{10}>1/2\),
while (7.2) gives \(E_{\min}<1/2\), a contradiction.  Hence

\[
 \boxed{\text{(0.3)--(0.4) have no solution for real }q\ge1000.}
\tag{7.3}
\]

This finite intrinsic implication bootstrap uses \(p/(dm)\), but it is
shell-ratio-free: it does not partition \(\rho\), \(K\), or \(q\).
It creates no new owner seam or proof case.

## 8. Finite lower-scalar reduction

For \(0<z<M<K\), the positive arcsine series gives

\[
 \arcsin\frac zM-\arcsin\frac zK
 =
 z(M^{-1}-K^{-1})
 +\frac{z^3}{6}(M^{-3}-K^{-3})
 +\sum_{n\ge2}c_nz^{2n+1}
  (M^{-2n-1}-K^{-2n-1}),
\]

where every \(c_n>0\).  Integration over the nonempty interval
\([r,x]\) shows that the first two terms give
\(\mathcal K_{4,\min}\), while the remainder is strictly positive.
Thus

\[
 E_{\min}>\mathcal K_{4,\min}.
\tag{8.1}
\]

Using \(T(q)>7/10\) in (0.1),

\[
 \mathfrak F>L_q(p,x),
\tag{8.2}
\]

where \(m=q-x,\ r=x-p\), and

\[
 L_q(p,x)
 =
 \frac7{10}
 +\frac23p^2(3x-p)
  \left[
   A+B\{x^2+(x-p)^2\}
  \right]
 -\frac p2+\frac{d(q-x)}2,
\tag{8.3}
\]

\[
 A=\frac{(q+1)^{-1}-K_2^{-1}}{2\pi},\qquad
 B=\frac{(q+1)^{-3}-K_2^{-3}}{24\pi}.
\]

For fixed \(q\), enlarge to the full real triangle

\[
 p\ge1,\qquad x-p\ge r_0,\qquad q-x\ge1,
\tag{8.4}
\]

where \(r_0=1\) on the integer grid and \(r_0=3/2\) on the
half-integer grid.

Direct differentiation gives

\[
 (L_q)_{pp}
 =
 \frac43\left[
  3Ar+B\{2p^3-6pr^2+6r^3\}
 \right]>0,
\tag{8.5}
\]

\[
 (L_q)_{xx}
 =\frac83Bp^2(9x-4p)>0.
\tag{8.6}
\]

For (8.5), put \(u=p/r\).  Then
\(2u^3-6u+6\ge2\) for \(u\ge0\).

The Hessian determinant is

\[
 -\frac{16p^2}{9}\mathcal Q,
\]

where

\[
 \begin{aligned}
 \mathcal Q={}&9A^2
 +AB(36p^2-66px+54x^2)\\
 &+B^2(20p^4-60p^3x+204p^2x^2
       -384px^3+216x^4).
 \end{aligned}
\]

Put \(u=p/x\in(0,1)\) and

\[
 \tau=\frac{Bx^2}{A}
 =\frac{x^2}{12}
 \{(q+1)^{-2}+((q+1)K_2)^{-1}+K_2^{-2}\}
 <\frac14.
\]

Then

\[
 \frac{\mathcal Q}{A^2}
 =
 9+\tau(36u^2-66u+54)
 +\tau^2(20u^4-60u^3+204u^2-384u+216).
\]

The middle polynomial is

\[
 36\left(u-\frac{11}{12}\right)^2+\frac{95}{4}.
\]

If \(P\) denotes the last
polynomial, then

\[
 P'(u)=4(20u^3-45u^2+102u-96)<0
 \quad(0\le u\le1),
\]

Its derivative is \(60u^2-90u+102>0\), so the cubic is increasing
and has value \(-19\) at \(u=1\).
Thus \(P(u)\ge P(1)=-4\).  Hence
\(\mathcal Q>35A^2/4>0\).  Every interior critical point is therefore
a saddle, not a minimum.

The minimum on (8.4) lies on one of three edges:

\[
 p=1,\qquad r=r_0,\qquad m=1.
\]

The first and third edges are strictly convex by (8.6) and (8.5).
On \(r=r_0\),

\[
 \frac{d^2}{dp^2}L_q(p,p+r_0)
 =
 \frac43\{
 6Ap+20Bp^3+3Ar_0+42Bp^2r_0
 +30Bpr_0^2+6Br_0^3
 \}>0.
\]

Thus the full finite \((p,r,m)\)-problem reduces analytically to three
one-variable convex inequalities per \(q\).  No enumeration of the
933 Round 30 diagnostic records is needed.

This lower scalar is intentionally not used asymptotically:
\(L_q\ge0\) is false globally because replacing \(E_{\min}\) by
\(\mathcal K_{4,\min}\) loses the boundary-phase reserve.

## 9. Equality-face and strict-wall audit

1. The proof of (7.3) is for all real \(q\ge1000\), so both inherited
   parity grids are covered without interpolation.
2. Shelf feasibility is allowed with equality in (0.3).  The phase
   upper bound (4.3) is strict, so (4.4) remains strict.
3. The hard wall \(p=dm\) belongs to the already proved automatic
   sector.  This note uses \(p>dm\), hence \(u>1\), exactly as required.
4. Every bootstrap choice \(P=\lambda dm\) satisfies \(P<p<x\).
   No artificial shelf endpoint is evaluated outside the actual interval.
5. The endpoint \(q=1000\) is included.  Every rounded constant used in
   Sections 3 and 7 has an explicit positive rational residual.
6. The \(K_2,K_3\) values are the limiting first-band radii already used
   in the Round 30 lower bound.  This note does not change inverse- or
   outer-\(B\)-wall ownership.
7. The finite triangle keeps the exact lower radii
   \(r_0=1\) and \(r_0=3/2\).  It does not extend the inherited-grid
   argument to \(r=0\) or \(r=1/2\).

## 10. Loss ledger

- Section 2 proves convexity of the full retained scalar and discards
  nothing.
- Section 4 upper-bounds the shelf action only to force a necessary lower
  bound on \(m\); the excess shelf action is discarded.
- Section 5 lowers the exact phase kernel by its outer-radius value and
  enlarges its square-root denominator.  The resulting \(B_c\) is weaker
  than the exact \(E_{\min}\) but retains enough correlation for the
  bootstrap.
- Sections 6--7 replace exact phase quantities by rational bounds valid
  uniformly for \(q\ge1000\).  Every replacement direction is adverse.
- Section 8 discards both \(T(q)-7/10\) and
  \(E_{\min}-\mathcal K_{4,\min}\).  The resulting scalar is used only
  as a finite-range design reduction; its positivity is not asserted
  globally.
- No inverse fraction, exact cap, or terminal interval is newly discarded
  in the proof of (7.3); those quantities entered earlier in the Round 30
  reduction to \(\mathfrak F\).

## 11. Falsification and replay

The exact replay

computations/general_d_round31_retained_shelf_replay.wl

checks:

- the curvature second derivative and the normalized convexity
  factorization;
- the lower-scalar Hessian identities;
- all six angle/phase rational margins;
- both endpoint-ratio margins; and
- all nine exact bootstrap comparisons.

On Mathematica 15.0 for Windows it returns

\[
 \texttt{round31RetainedShelfReplayOK=True}.
\]

The Round 30 finite diagnostic through \(q=1000\) retained 933 relaxed
necessary-condition records, found none above \(q=33\), and found no
nonpositive \(\mathfrak F\).  Those observations agree with (7.3) but
remain diagnostic only.

A separate high-precision falsification point

\[
 (q,m,p,r)=(100000,150,611,99239)
\]

has a strongly negative quartic-only finite scalar but
\(E_{\min}>1.7\), so it lies far outside the hard sector.  This rejects
using the Section 8 scalar globally and confirms that the retained
\(E_{\min}\) in Sections 5--7 is essential.

An unarchived exact-rational experiment checked the three Section 8 edges
for the 62 grid values \(q\le33.5\) and found a conservative lower
margin about \(0.01364\).  Because that experiment is not supplied here
as a self-contained certificate and because \(33.5<q<1000\) is still
open, it is theorem-design evidence only and is not used in any claim.

## 12. Exact remaining inequality and next action

The retained lower-shelf task is now confined to

\[
 q<1000
\]

under (0.3)--(0.4).  The diagnostic suggests the sharper exact cutoff

\[
 q\le33\quad\hbox{(integer grid)},\qquad
 q\le\frac{65}{2}\quad\hbox{(half-integer grid)},
\]

but this is not yet proved.

The next analytic target is to sharpen (7.3), preferably by proving that
the optimized continuous hard gap decreases for \(q\ge35\), with only
the first two lattice seams treated separately.  Once the exact cutoff
is proved, use the Section 8 three-edge reduction or a direct analytic
edge inequality to prove \(\mathfrak F>0\) on the remaining finite
range.  A compact certificate is not introduced at this stage.

Independently, the lower-\(Q\) hard arc, \(\alpha\uparrow1\), the
remaining \(\alpha=0\) small-phase face, other inverse bands, and
simultaneous inverse/\(B\) endpoints outside the exact Round 30 scope
remain live.

Therefore high-floor CST and the all-dimensional theorem remain open.
