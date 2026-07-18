# General dimension, Round 5: global exhaustion of the high-floor first-drop branch

Date: 18 July 2026  
Scope: \(F_0=f\ge2\) and the first ordinary-floor shelf drops before the
interface, \(p<n\)  
Status: rigorous qualitative global exhaustion. Every possible negative
first-drop scalar is confined to a compact parameter set, and hence to
finitely many possible discrete data tuples. The compact residual set has
not yet been certified, and the bounds produced here are not numerical.

This note treats only the first-drop branch. It does not edit or replace
either manuscript. Ordinary floors define the shelf and strict brackets
define the terminal count throughout.

## 1. Exact setup and the interface restriction

Write

\[
 \epsilon=1-\rho,\qquad s=\sqrt\epsilon,\qquad
 a=K-\mu=\epsilon K,\qquad \kappa=sa=s^3K,
\]

and

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad
 \alpha=\mu-q\in[0,1),\qquad m=n-p.
\]

Let the first ordinary floor be \(F_0=\cdots=F_p=f\ge2\), put

\[
 h=f-\frac14,\qquad x=r+p,\qquad
 d=d_\rho=\frac{2\arcsin\rho}{\pi},
\]

and assume \(p<n\). The reduced scalar is

\[
 \mathcal S=D_A(q)+R_p+\frac d2m,\qquad
 R_p=2\int_r^x A(z)\,dz-2pf.                    \tag{1}
\]

The first-drop assumption immediately gives the useful strict interface
bound requested in the strategy. Indeed, \(p+1\le n\), and the ordinary
floor at \(x+1\) is at most \(f-1\). Hence

\[
 A(x+1)<h.
\]

Since \(x+1\le q\le\mu\) and \(A\) is decreasing,

\[
 \boxed{W:=G_K(\mu)=A(\mu)<h=f-\frac14.}          \tag{2}
\]

The turning lower bound

\[
 G_K(K(1-\epsilon))\ge
 c_0K\epsilon^{3/2},\qquad
 c_0=\frac{2\sqrt2}{3\pi},
\]

therefore also gives the exact necessary condition

\[
 \boxed{c_0a\sqrt\epsilon=c_0\kappa<h.}           \tag{3}
\]

This is special to the first-drop branch and is the main new input below.

## 2. An exact level-geometry reduction

Use distance from the inner interface,

\[
 H(t)=A(\mu-t),\qquad 0\le t\le\mu.
\]

Thus \(H(0)=W\), \(H\) is increasing, and

\[
 0\le H'(t)\le c_\rho:=\frac{\arccos\rho}{\pi}.
\]

Let \(M\in(0,\mu]\) be the unique point \(H(M)=h\). It exists by
(2) and the shelf condition. The two shelf inequalities at \(x,x+1\)
give

\[
 M\le \mu-x<M+1.                                  \tag{4}
\]

If \(H(\mu)\ge f\), let \(T\) be the unique point \(H(T)=f\). If
\(H(\mu)<f\), put \(T=\mu\). In either case

\[
 H(T)\le f.                                        \tag{5}
\]

If \(A(x)\ge f\), then every point of the first shelf has action at least
\(f\), so \(R_p\ge0\) and (1) is positive. A negative candidate must
therefore have \(A(x)<f\). Its negative shelf portion is contained between
the distances \(\mu-x\) and \(T\), where \(0\le f-H\le1/4\). Consequently

\[
 R_p\ge-\frac{T-(\mu-x)}2.                         \tag{6}
\]

Since

\[
 \mu-x=\alpha+m,\qquad m\ge \mu-x-1,
\]

(4)--(6) imply the exact prefix bound

\[
 \boxed{
 R_p+\frac d2m\ge
 \frac{(1+d)M-T-d}{2}.}                            \tag{7}
\]

The one-interface theorem gives \(D_A(q)\ge0\). Hence every negative
scalar in (1) necessarily satisfies

\[
 \boxed{T>(1+d)M-d.}                               \tag{8}
\]

No asymptotic approximation has entered (2)--(8).

## 3. The shell-increment elasticity lemma

The key point is that (8) forces the interface action to lie within a
universal additive constant of the first floor.

### Lemma 3.1

Put

\[
 V(t)=t(2\mu-t).
\]

For \(0<t_1<t_2\le\mu\),

\[
 \boxed{
 \frac{H(t_2)-W}{H(t_1)-W}
 \ge\sqrt{\frac{V(t_2)}{V(t_1)}}.}                 \tag{9}
\]

### Proof

The exact radius-average formula is

\[
 H(t)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{(\mu-t)^2}{R^2}}\,dR.
\]

For fixed \(R\in[\mu,K]\), put

\[
 b_R=1-\frac{\mu^2}{R^2},\qquad
 \phi_R(V)=\sqrt{b_R+\frac V{R^2}}-\sqrt{b_R}.
\]

At \(V>0\), direct differentiation gives

\[
 \frac{V\phi_R'(V)}{\phi_R(V)}
 =\frac12\left(1+
 \frac{\sqrt{b_R}}{\sqrt{b_R+V/R^2}}\right)
 \ge\frac12.
\]

Thus \(\phi_R(V)/\sqrt V\) is nondecreasing. The same comparison can be
integrated over \(R\), with positive measure, and (9) follows.

### Proposition 3.2: universal interface pinning

Consider any sequence of negative first-drop scalars for which
\(\rho\to1\). Then

\[
 \boxed{
 f-W\le 1+\frac{\sqrt3}{2}+o(1).}                  \tag{10}
\]

### Proof

After passing to a subsequence, either \(M\) remains bounded or
\(M\to\infty\). In the first case,

\[
 0<h-W=H(M)-H(0)\le c_\rho M=o(1),
\]

so \(f-W=1/4+o(1)\), which is stronger than (10).

Suppose instead that \(M\to\infty\). Since \(d\to1\), (8) gives

\[
 \liminf\frac TM\ge2.                              \tag{11}
\]

Also \(T\le\mu\). Writing \(r_*=T/M\) and \(u=M/\mu\), an elementary
calculation gives

\[
 \frac{V(T)}{V(M)}
 =r_*\frac{2-r_*u}{2-u},\qquad 0\le u\le\frac1{r_*}.
\]

For every \(0<\eta<1\), (11) gives \(r_*\ge2-\eta>1\) eventually.  For
fixed \(r_*>1\), the displayed expression decreases on
\(0\le u\le1/r_*\), so it is at least \(r_*^2/(2r_*-1)\).  Hence

\[
 \liminf\frac{V(T)}{V(M)}
 \ge\lim_{\eta\downarrow0}
 \frac{(2-\eta)^2}{3-2\eta}
 =\frac43.                                         \tag{12}
\]

Apply (9) at \(M,T\). By (5),

\[
 \sqrt{\frac{V(T)}{V(M)}}
 \le\frac{H(T)-W}{h-W}
 \le\frac{f-W}{f-W-1/4}.                           \tag{13}
\]

Equations (12)--(13) give

\[
 \liminf\frac{f-W}{f-W-1/4}\ge\frac2{\sqrt3}.
\]

Solving this scalar inequality yields

\[
 \limsup(f-W)
 \le\frac1{2(2-\sqrt3)}
 =1+\frac{\sqrt3}{2},
\]

which is (10).

The argument includes the case in which the level \(f\) is not reached:
then \(T=\mu\), and the second inequality in (13) is strict.

## 4. Reduction of every escaping candidate to turning coordinates

We now import only three automatic results already proved in the
general-dimension development.

1. On every ratio range bounded away from \(\rho=1\), the fixed-ratio
   high-energy theorem confines a negative candidate to bounded \(K\).
2. On a bounded optical interval \(a=K-\mu\), the compact-optical product
   theorem closes the shifted tail for all sufficiently small
   \(\epsilon\).
3. The thin high-energy theorem closes the region

   \[
   \epsilon a=K\epsilon^2\ge\frac{125}{8}.          \tag{14}
   \]

These results exclude a negative reduced scalar itself.  Put
\(\delta_q=\int_q^\mu G_\mu(z)\,dz\).  In the
fixed-ratio proof put \(L_K=\lfloor K\eta_\rho\rfloor\), and in the
thin-high-energy proof put \(L_K=\lfloor KG_1(\rho)\rfloor\).  The convex
suffix and one-interface identity give

\[
 D_A(q)\ge\frac{L_K}{2}-2\delta_q,
\]

while \(R_p\ge-p/2\).  Consequently

\[
 \mathcal S\ge
 \frac12\bigl(L_K+d(n-p)-p\bigr)-2\delta_q.        \tag{14a}
\]

The respective thresholds prove
\(L_K+d(n-p)-p>4\delta_q\).  The compact-optical theorem directly proves
\(R_p+d(n-p)/2>0\).  Thus all three imported sectors control
\(\mathcal S\), not merely a separate tail term.

Consequently, any sequence of negative first-drop scalars leaving every
compact parameter set must satisfy

\[
 \epsilon\to0,\qquad a\to\infty,\qquad
 s\kappa=\epsilon a<\frac{125}{8}.                 \tag{15}
\]

The elementary turning bounds at the interface give, uniformly under
(15),

\[
 W=G_K(K(1-s^2))=c_0\kappa+O(\kappa s^2)
 =c_0\kappa+o(1),                                  \tag{16}
\]

because \(\kappa s^2=s(s\kappa)\to0\). Combining (2), (10), and
(16) gives the decisive two-sided pinning

\[
 \boxed{
 f-1-\frac{\sqrt3}{2}-o(1)
 \le c_0\kappa
 \le f-\frac14+o(1).}                              \tag{17}
\]

In particular, \(\kappa\asymp f\), uniformly even when the floor varies.
The lower constant is positive already at \(f=2\).

Equation (17) also gives \(\kappa/f\asymp1\).  Therefore

\[
 \frac{A(0)}f
 =\frac{a}{\pi f}
 =\frac{\kappa}{\pi sf}
 \asymp\frac1s\longrightarrow\infty.              \tag{17a}
\]

Thus every escaping sequence eventually reaches the level \(f\).  The
earlier convention \(T=\mu\) remains necessary for the interface-pinning
argument, but no missing-level case remains in the turning limit.

For later use, introduce the exact turning coordinate

\[
 X=s(\mu-z),\qquad
 \mathcal H_{s,\kappa}(X)=A\left(\mu-\frac Xs\right),
\]

and the critical profile

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \bigl((\kappa+X)^{3/2}-X^{3/2}\bigr).             \tag{18}
\]

Let \(X_f=sT\) when the level \(f\) exists. The radius-average formula
also gives

\[
 f\ge
 \frac{\sqrt{\kappa X_f}}{\pi\sqrt{1-s^2}},\qquad
 X_f\le\pi^2(1-s^2)\frac{f^2}{\kappa}.             \tag{19}
\]

By (17), \(X_f/\kappa\) is bounded by a universal constant. On every such
range, the two ball turning estimates give

\[
 \sup_{0\le X\le X_f}
 \left|\mathcal H_{s,\kappa}(X)-H_\kappa(X)\right|
 =O(\kappa s^2)=o(1).                              \tag{20}
\]

For completeness, the two turning parameters are

\[
 y_K=s^2\left(1+\frac X\kappa\right),\qquad
 y_\mu=\frac{s^2X}{\kappa(1-s^2)}.
\]

Both are \(O(s^2)\) under (19), the leading ball terms are \(O(\kappa)\),
and the extra inner factor \((1-s^2)^{-1/2}\) differs from one by
\(O(s^2)\). This proves (20) with no assumption that \(f\) is fixed.

Moreover, (10), (16), (18)--(20), and the positive lower bound for

\[
 H_\kappa'(X)=\frac{3c_0}{2}
 \left(\sqrt{1+X/\kappa}-\sqrt{X/\kappa}\right)
\]

on the bounded range in (19) show that in fact

\[
 \boxed{X_f=O(1)}                                   \tag{21}
\]

uniformly along every escaping negative sequence. Thus (10) does exactly
what is needed: it forces the entire dangerous level band into a bounded
turning window.

## 5. Floors tending to infinity are automatic

Suppose first that \(f\to\infty\). Then (17) gives

\[
 \frac\kappa f\longrightarrow\frac1{c_0}.          \tag{22}
\]

Also \(A(0)=a/\pi=\kappa/(\pi s)>f\) for all sufficiently large indices,
so the level \(f\) used in (19)--(21) exists. Equations (6) and (21) give
a uniform lower bound

\[
 s\left(R_p+\frac d2m\right)\ge-O(1).              \tag{23}
\]

The root-free exact-angle terminal estimate is

\[
 D_A(q)\ge C_0K^{1/3}S_B-Q-2\int_q^\mu G_\mu(z)\,dz,
\quad
 C_0=\left(\frac\pi{12}\right)^{1/3},              \tag{24}
\]

where

\[
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<,\qquad
 S_B=\sum_{k=1}^B(k-\tfrac14)^{-1/3}.
\]

Here \(q\le\mu\), so \(G_K(q)\ge W\), and therefore, including a strict
bracket wall,

\[
 B\ge W-\frac34=f-O(1).                             \tag{25}
\]

On the other hand, \(q\ge x+1\) and \(A(x+1)<h\), so

\[
 Q\le f-1.                                          \tag{26}
\]

Multiplying (24) by \(s\), using \(sK^{1/3}=\kappa^{1/3}\), and using
the universal cap bound gives

\[
 sD_A(q)\ge
 C_0\kappa^{1/3}S_B-s(f-1)-O(s).                   \tag{27}
\]

By (22), (25), and the integral lower bound

\[
 S_B\ge\sum_{k=1}^B k^{-1/3}
 \ge\frac32\bigl((B+1)^{2/3}-1\bigr),
\]

the first term on the right of (27) grows linearly in \(f\). The negative
term is bounded, since (15) and (22) give

\[
 sf=(s\kappa)\frac f\kappa=O(1).
\]

Thus

\[
 sD_A(q)\longrightarrow+\infty.                   \tag{28}
\]

Equations (23) and (28) contradict \(\mathcal S<0\). Therefore an
escaping negative first-drop sequence cannot have unbounded first floor.

## 6. Bounded floors and the uniform critical gap

It remains to consider bounded \(f\). Pass to a subsequence on which the
integer \(f\) is fixed. Equation (17) confines \(\kappa\) to a compact
subinterval of \((0,\infty)\); pass again so that \(\kappa\to\kappa_0\).
The level \(f\) exists for all large indices, (20) is uniform on a fixed
compact interval, and the shelf endpoint in (4) converges in \(X\)-scale to
the level \(M_0\) of \(h\) for \(H_{\kappa_0}\). The level \(f\) converges
to \(N_0\).  Here is the exact passage to the prefix limit.  Put

\[
 X_x=s(\mu-x),\qquad X_r=s(\mu-r).
\]

The shelf inequalities imply

\[
 0\le A(x)-h<A(x)-A(x+1)\le c_\rho\longrightarrow0,
\]

so \(X_x\to M_0\); likewise \(sT\to N_0\).  Discarding only
nonnegative shelf area gives

\[
 sR_p
 =2\int_{X_x}^{X_r}(\mathcal H_{s,\kappa}-f)\,dX
 \ge-2\int_{X_x}^{sT}(f-\mathcal H_{s,\kappa})\,dX.
\]

Finally, \(sm=s(\mu-x)-s\alpha\to M_0\) and \(d\to1\). Hence

\[
 \liminf s\left(R_p+\frac d2m\right)
 \ge \mathcal L:=-2\int_{M_0}^{N_0}
 (f-H_{\kappa_0}(X))\,dX+\frac{M_0}{2}.             \tag{29}
\]

The wall-safe exact-angle limit gives

\[
 \liminf sD_A(q)\ge\mathcal T(w),
\]

where \(w=c_0\kappa_0\),

\[
 \mathcal T(w)=\frac\pi{2\sqrt2}w^{1/3}
 \sum_{k=1}^{[w+1/4]_<}(k-\tfrac14)^{-1/3}.         \tag{30}
\]

The fractional-top reserve

\[
 \frac\pi{\sqrt2}\bigl(w-[w+1/4]_<\bigr)_+^2
\]

is nonnegative away from a level wall (and is replaced by the smaller
wall-safe one-sided expression at a wall). It may therefore be retained as
extra room, but it is not needed here.

The negative exact prefixes satisfy (8). After multiplication by \(s\)
and passage to the limit, this gives

\[
 N_0\ge2M_0.                                        \tag{31}
\]

The uniform critical-gap theorem gives the precise conclusion needed here.
For reference, write \(X=\kappa_0u\) and

\[
 t=\sqrt{1+u}-\sqrt u,\qquad
 \frac{H_{\kappa_0}(X)}w=\frac{3/t+t^3}{4}.
\]

If \(\mathcal L<0\), then \(N_0>2M_0\), and the elementary parameter
calculation forces \(t_f>1/3\). It follows that

\[
 -\mathcal L<\frac{3\pi}{8\sqrt2},\qquad
 \mathcal T(w)>\frac\pi{2\sqrt2},
\]

and therefore

\[
 \boxed{\mathcal L+\mathcal T(w)>
 \frac\pi{8\sqrt2}.}                              \tag{32}
\]

The calculation \(t_f>1/3\) is uniform in every \(f\ge2\): under the
contrary assumption, \(h/f\ge7/8\) gives \(t_h<2/5\) and

\[
 \frac{N_0}{M_0}
 <\left(\frac{15128}{13125}\right)^2
  \left(\frac{25}{21}\right)^2
 =\frac{228856384}{121550625}<2.
\]

If \(\mathcal L\ge0\), (31) and the same parameter comparison force
\(w>3/4\) (with \(M_0=0\) giving \(w=h\) directly), so the first complete
level in (30) is present and \(\mathcal T(w)>0\). In either case

\[
 \mathcal L+\mathcal T(w)>0.                        \tag{33}
\]

Equations (29)--(33) contradict \(s\mathcal S<0\). Thus an escaping
negative first-drop sequence cannot have bounded floors either.

## 7. Global exhaustion theorem and exact remaining work

Combining Sections 4--6 proves:

### Theorem 7.1

The set of high-floor first-drop configurations

\[
 F_0=f\ge2,\qquad p<n,\qquad
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)<0
\]

is relatively compact in the exact shell parameter space. Consequently
there exist finite (not presently explicit) bounds for all discrete data

\[
 (f,n,p,Q,B)
\]

on which the high-floor first-drop scalar could fail.  This is a bounded
integer-data conclusion; compactness alone does not assert that the
remaining analytic wall set has finitely many connected components.

This is a qualitative global exhaustion, not a certification of the
remaining compact chambers. It proves, rigorously:

1. the exact first-drop interface restriction (2)--(3);
2. the exact prefix geometry (7)--(8);
3. the shell-increment elasticity inequality (9);
4. the universal interface pinning (10);
5. exclusion of both possible escaping regimes: \(f\to\infty\) by the
   root-free terminal reserve, and bounded \(f\) by the uniform critical
   gap.

The next step is now compact with bounded integer data: extract numerical
bounds from the compactness proof (or prove a direct monotone wall
reduction), enumerate the remaining tuples, and certify the exact-angle
scalar on the residual analytic wall sets.
Until that is done, the full high-floor first-drop branch and hence the
general-\(d\) theorem remain open.
