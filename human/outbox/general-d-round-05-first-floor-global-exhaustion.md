# General dimension, Round 5: global exhaustion of the ordinary first floor

Date: 18 July 2026  
Scope: the universal spectral active region, the ordinary first floor
\(F_0=1\), and a first drop before the interface, \(p<n\)  
Status: rigorous qualitative global exhaustion. Every negative first-floor
first-drop scalar is confined to a compact parameter set. Consequently only
bounded discrete data can remain, but the compact residual chambers have not
been certified.

This note does not edit either manuscript. It closes the noncompact part of
the residual integer cone \(n-p-1\geq2\), including the previously delicate
ray on which the critical thickness parameter tends to zero. It does not
claim that the ten known weakened-certificate failures exhaust the compact
set, and it does not replace the stronger true-interface certificate used on
those ten chambers.

## 1. Exact first-floor setup

Put

\[
 \varepsilon=1-\rho,\qquad \tau=\sqrt\varepsilon,\qquad
 a=K-\mu=\varepsilon K,\qquad \kappa=\tau a=\tau^3K,
 \tag{1}
\]

and

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad
 \alpha=\mu-q\in[0,1),\qquad m=n-p.
 \tag{2}
\]

The integer \(n-p-1=m-1\) is the residual cone coordinate denoted by
\(s\) in the earlier first-floor wall notes. The letter \(\tau\) is used
here for \(\sqrt{1-\rho}\) so that the two quantities cannot be confused.

Let

\[
 A=G_K-G_\mu,\qquad x=r+p,\qquad
 d=d_\rho=\frac{2\arcsin\rho}{\pi}.
\]

On the ordinary first floor, followed by a first drop, one has

\[
 A(r+j)\geq\frac34\quad(0\leq j\leq p),\qquad
 A(x+1)<\frac34,\qquad p<n.
 \tag{3}
\]

The reduced scalar is

\[
 \mathcal S
 =D_A(q)+R_p+\frac d2m,
 \qquad
 R_p=2\int_r^x A(z)\,dz-2p.
 \tag{4}
\]

The completed one-interface theorem gives

\[
 D_A(q)\geq0.                                      \tag{5}
\]

If \(p=0\), then \(R_0=0\), and (4)--(5) make the scalar strictly
positive. Thus every negative candidate has \(p\geq1\).

Write distance from the interface as

\[
 \mathscr H(t)=A(\mu-t),\qquad 0\leq t\leq\mu,
 \qquad W=\mathscr H(0)=G_K(\mu).
\]

Since \(x+1\leq q\leq\mu\), (3) gives

\[
 W<\frac34.                                        \tag{6}
\]

The elementary lower turning bound therefore implies

\[
 c_0\kappa<\frac34,
 \qquad c_0=\frac{2\sqrt2}{3\pi}.                 \tag{7}
\]

Let \(M\) be the physical distance at which
\(\mathscr H(M)=3/4\). The shelf inequalities give

\[
 M\leq\mu-x<M+1.                                  \tag{8}
\]

If \(A(x)\geq1\), then \(A\geq1\) on \([r,x]\), so \(R_p\geq0\)
and the scalar is positive. Hence a negative candidate necessarily has

\[
 A(x)<1.                                           \tag{9}
\]

When the level one exists, let \(T\) be its physical distance from the
interface. The negative part of the first shelf is then contained between
\(\mu-x\) and \(T\), and

\[
 R_p\geq-\frac{T-(\mu-x)}2.                       \tag{10}
\]

Equations (5), (8), and \(m=\mu-x-\alpha\) in particular show that a
negative candidate must satisfy

\[
 T>(1+d)M-d.                                      \tag{11}
\]

The proof below uses the sharper integral form behind (10), rather than
only (11).

The general-dimensional spectral argument needs (4) only in the universal
active region

\[
 K>\frac\pi{1-\rho},\qquad\text{equivalently }a>\pi. \tag{12}
\]

In this region \(A(0)=a/\pi>1\), so the level one used in
(10)--(11) exists for every candidate, including arbitrarily close to the
active boundary.

The complementary region is already a no-mode region. No standalone
shifted-tail assertion below (12) is made here.

## 2. The only possible escape and an exact shell profile

We use the following already proved exhaustion facts.

1. On every ratio interval bounded away from \(\rho=1\), the fixed-ratio
   high-energy theorem confines a negative scalar to bounded \(K\).
2. On every bounded active optical interval \(\pi<a\leq A_*\), the
   compact-optical product theorem closes (4) for all sufficiently small
   \(\varepsilon\).
3. The thin high-energy theorem closes the sector
   \(\varepsilon a\geq125/8\).

These theorems control the reduced scalar (4), not merely a detached shelf
term.  To make this point explicit, put

\[
 \delta_q=\int_q^\mu G_\mu(z)\,dz.
\]

In the fixed-ratio proof take
\(L_K=\lfloor K\eta_\rho\rfloor\), and in the thin-high-energy proof take
\(L_K=\lfloor KG_1(\rho)\rfloor\).  The convex ball suffix and the exact
one-interface identity give

\[
 D_A(q)\geq\frac{L_K}{2}-2\delta_q,
 \qquad R_p\geq-\frac p2,
\]

and hence

\[
 \mathcal S\geq
 \frac12\bigl(L_K+d(n-p)-p\bigr)-2\delta_q.       \tag{12a}
\]

The corresponding thresholds make the parenthesis in (12a) strictly
larger than \(4\delta_q\).  The compact-optical theorem directly proves
\(R_p+d(n-p)/2>0\), after which (5) applies.  Thus all three imported
sectors really exclude a negative value of (4).

It follows that any sequence of negative candidates leaving every compact
parameter set must satisfy

\[
 \tau\longrightarrow0,\qquad
 a\longrightarrow\infty,\qquad
 \tau\kappa=\varepsilon a<\frac{125}{8}.          \tag{13}
\]

By (7), \(\kappa\) remains bounded. After taking a subsequence, there is
therefore a limit

\[
 \kappa\longrightarrow\kappa_0,
 \qquad 0\leq\kappa_0\leq\frac{3}{4c_0}.          \tag{14}
\]

The endpoint \(\kappa_0=0\) cannot be treated by an additive turning
error on a fixed \(X\)-window. The following exact, non-cancelling
representation treats both cases at once. Put

\[
 X=\tau(\mu-z),\qquad
 \mathcal H_{\tau,\kappa}(X)
 =A\left(\mu-\frac X\tau\right).
\]

Changing variables \(R=K-u/\tau\) in the radius-average formula gives,
at every physical point,

\[
 \boxed{
 \mathcal H_{\tau,\kappa}(X)
 =\frac1\pi\int_0^\kappa
 \frac{\sqrt{(\kappa+X-u)
 [2\kappa-(\kappa+X+u)\tau^2]}}
 {\kappa-u\tau^2}\,du.}                           \tag{15}
\]

Its critical profile is

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right).           \tag{16}
\]

The ratio of the integrand in (15) to that in (16) is

\[
 \mathcal R(u,X)
 =\frac{\sqrt{1-y(u,X)}}{1-z(u)},
 \quad
 y(u,X)=\frac{\kappa+X+u}{2\kappa}\tau^2,
 \quad z(u)=\frac u\kappa\tau^2.                 \tag{17}
\]

The level-one existence can also be read directly along (13) from

\[
 A(0)=\frac a\pi\longrightarrow\infty.            \tag{18}
\]

Let \(X_1=\tau T\) be its exact turning coordinate. The radius-average
lower bound

\[
 A(\mu-t)\geq
 \frac a\pi\sqrt{\frac t\mu}
 =\frac{\sqrt{\kappa X}}{\pi\sqrt{1-\tau^2}}
\]

gives

\[
 X_1\leq\frac{\pi^2(1-\tau^2)}\kappa.             \tag{19}
\]

On the entire possible negative head, \(0\leq X\leq\pi^2/\kappa\),
(17) satisfies

\[
 0\leq y(u,X)\leq
 \tau^2+\frac{\pi^2}{2a^2},
 \qquad 0\leq z(u)\leq\tau^2.                   \tag{20}
\]

Since \(1-Y\leq\sqrt{1-Y}\leq1\), equations (13) and (20) imply the
multiplicative convergence

\[
 \boxed{
 \sup_{0\leq X\leq\pi^2/\kappa}
 \left|\frac{\mathcal H_{\tau,\kappa}(X)}
 {H_\kappa(X)}-1\right|\longrightarrow0,}         \tag{21}
\]

where the supremum is restricted to physical points. Formula (21) is the
reason the regime \(\kappa\to0\) is still controllable: its error is
governed by \(a^{-2}\), not by an unstable subtraction of two ball
actions.

## 3. The critical first-floor gap

We record the limiting inequality in the precise form needed below. For
\(0<w<3/4\), put \(w=c_0\kappa\), let

\[
 H_\kappa(M_*)=\frac34,\qquad H_\kappa(N_*)=1,
\]

and define

\[
 \mathcal L(w)
 =-2\int_{M_*}^{N_*}(1-H_\kappa(X))\,dX+\frac{M_*}{2},
 \qquad
 \mathcal Z(w)=\frac\pi{\sqrt2}w^2.               \tag{22}
\]

### Lemma 3.1: first-floor critical gap

One has

\[
 \boxed{
 \mathcal L(w)+\mathcal Z(w)>
 \frac\pi{8\sqrt2}\qquad(0<w<3/4).}              \tag{23}
\]

At the limiting wall \(w=3/4\), replace \(\mathcal Z\) by the smaller
wall-safe terminal value \(\pi/(2\sqrt2)\). The same strict lower bound
in (23) remains valid.

### Proof

The function \(1-H_\kappa\) is convex on \([M_*,N_*]\), with endpoint
values \(1/4\) and zero. Its integral is at most the endpoint chord area,
so

\[
 \mathcal L(w)\geq\frac{3M_*-N_*}{4}.             \tag{24}
\]

Write

\[
 X=\kappa u(t),\qquad
 u(t)=\frac{(1-t^2)^2}{4t^2},\qquad
 \frac{H_\kappa(X)}w=F(t)=\frac{3/t+t^3}{4}.
\]

If \(\xi\) and \(\eta\) are the parameters at \(M_*\) and \(N_*\),
then \(0<\eta<\xi\leq1\) and

\[
 w=\frac{3\xi}{3+\xi^4}
  =\frac{4\eta}{3+\eta^4}.                        \tag{25}
\]

Since \(1/c_0=3\pi/(2\sqrt2)\), (24)--(25) give

\[
 \mathcal L(w)+\mathcal Z(w)
 \geq\frac\pi{\sqrt2}E(w,\xi,\eta),
\]

where

\[
 E=w^2+\frac{3w}{8}\bigl(3u(\xi)-u(\eta)\bigr).  \tag{26}
\]

The function \(u\) is decreasing. From (25),
\(\eta\geq3w/4\), while

\[
 \begin{array}{c|c|c}
 \text{range of }w&\text{upper bound for }\xi&\text{resulting bound}\cr
 0<w\leq1/2&(259/243)w&
 E\geq\displaystyle\frac18+\frac{85469}{51518208}\cr
 1/2\leq w\leq2/3&(283/256)w&
 E\geq\displaystyle\frac18+\frac{41923}{1281424}\cr
 2/3\leq w<3/4&1&
 E\geq\displaystyle\frac18+\frac{743}{4608}.
 \end{array}                                      \tag{27}
\]

For completeness, the first two upper bounds follow respectively from
\(F(2/3)<3/2\), \(F(3/4)<9/8\), and
\(\xi=w(1+\xi^4/3)\). Substitution in (26), followed only by completing
the square, gives the displayed rational margins. In the third range,
\(\eta\geq1/2\), so \(u(\eta)\leq9/16\), which gives the last line.

At \(w=3/4\), approaching the top action wall from the side with one
complete ball level replaces the normalized zero-level value \(9/16\)
by \(1/2\). Subtracting this \(1/16\) from the last line in (27) still
leaves

\[
 \frac18+\frac{455}{4608}>\frac18.
\]

This proves both assertions. \(\square\)

## 4. Nondegenerate critical limits, \(\kappa_0>0\)

Assume first that the subsequential limit in (14) is positive and put

\[
 w=c_0\kappa_0\in(0,3/4].
\]

Equations (19)--(21) now give uniform convergence of the exact profile to
\(H_{\kappa_0}\) on a fixed \(X\)-interval. Let \(M_j^X\) and \(N_j^X\)
be the exact \(X\)-coordinates of the levels \(3/4\) and one. Then

\[
 M_j^X\longrightarrow M_*,\qquad
 N_j^X\longrightarrow N_*.                        \tag{28}
\]

Put

\[
 X_x=\tau(\mu-x),\qquad X_r=\tau(\mu-r).
\]

Equation (8) says \(0\leq X_x-M_j^X<\tau\). Discarding only the
nonnegative part of the shelf beyond the level one gives

\[
 \tau R_p
 =2\int_{X_x}^{X_r}(\mathcal H_{\tau,\kappa}-1)\,dX
 \geq-2\int_{X_x}^{N_j^X}
 (1-\mathcal H_{\tau,\kappa})\,dX.                \tag{29}
\]

Moreover

\[
 \tau m=X_x-\tau\alpha\longrightarrow M_*.
\]

Thus

\[
 \liminf\tau\left(R_p+\frac d2m\right)
 \geq\mathcal L(w).                               \tag{30}
\]

It remains to transfer the terminal reserve without losing an action
wall. Put

\[
 B=\left[G_K(q)+\frac14\right]_<,
 \qquad Q=\left[A(q)+\frac14\right]_<.
\]

The first-drop inequality gives \(Q=0\) exactly. Also
\(G_K(q)-G_K(\mu)\to0\), because \(0\leq\mu-q<1\) and the ball slope on
that interval tends to zero. Finally

\[
 W=G_K(\mu)\longrightarrow w,
 \qquad
 \frac{\tau}{\arccos\rho/\pi}\longrightarrow
 \frac\pi{\sqrt2}.                                \tag{31}
\]

If \(w<3/4\), then \(B=0\) eventually. The zero-level tangent triangle
therefore yields

\[
 \liminf\tau D_A(q)
 \geq\lim\frac{\tau W^2}{\arccos\rho/\pi}
 =\frac\pi{\sqrt2}w^2=\mathcal Z(w).              \tag{32}
\]

Suppose instead that \(w=3/4\). On every subsequence with \(B=0\), (32)
gives \(9\pi/(16\sqrt2)\). On every subsequence with \(B=1\), retain the
first complete exact-angle level. If \(\theta_1\) is defined by

\[
 \frac K\pi(\sin\theta_1-\theta_1\cos\theta_1)=\frac34,
\]

then the exact-angle terminal theorem, the bounded inner cap, and \(Q=0\)
give

\[
 \liminf\tau D_A(q)
 \geq\lim\frac{\pi\tau}{2\theta_1}
 =\frac\pi{2\sqrt2}.                              \tag{33}
\]

Here \(\sin\theta-\theta\cos\theta=\theta^3/3+O(\theta^5)\),
\(K=\kappa/\tau^3\), and \(c_0\kappa_0=3/4\). Equations (32)--(33)
therefore give the smaller wall-safe value in Lemma 3.1 even if the strict
bracket alternates across the wall.

Combining (23), (30), and (32)--(33) gives

\[
 \liminf\tau\mathcal S>\frac\pi{8\sqrt2}>0,
\]

contradicting negativity of every scalar in the escaping sequence.

## 5. The degenerate critical ray, \(\kappa_0=0\)

The remaining case is not covered by convergence on a fixed
\(X\)-interval, because the two relevant levels have \(X\)-size
\(1/\kappa\). Introduce the second turning coordinate

\[
 Y=\kappa X,
 \qquad
 \widehat{\mathcal H}_{\tau,\kappa}(Y)
 =\mathcal H_{\tau,\kappa}(Y/\kappa).
\]

The critical profile becomes

\[
 \begin{aligned}
 \widehat H_\kappa(Y)
 &=H_\kappa(Y/\kappa)\\
 &=\frac{c_0}{\kappa^2}
 \left((Y+\kappa^2)^{3/2}-Y^{3/2}\right)\\
 &=\frac{3c_0}{2}\int_0^1\sqrt{Y+t\kappa^2}\,dt.
 \end{aligned}                                    \tag{34}
\]

Consequently, uniformly for \(0\leq Y\leq\pi^2\),

\[
 \widehat H_\kappa(Y)\longrightarrow
 H_0(Y):=\frac{\sqrt2}{\pi}\sqrt Y,               \tag{35}
\]

and the error in (35) is at most \(c_0\kappa\). On the same interval,
(20)--(21) give

\[
 \widehat{\mathcal H}_{\tau,\kappa}
 \longrightarrow H_0
 \quad\text{uniformly}.                            \tag{36}
\]

The whole displayed interval is eventually physical. Indeed, the physical
endpoint in the \(Y\)-coordinate is

\[
 Y_{\rm phys}=\kappa\tau\mu=(1-\tau^2)a^2
 \longrightarrow\infty.                          \tag{36a}
\]

The bound (19) places the exact level one inside this interval. Since
\(H_0\) is strictly increasing, the exact rescaled level coordinates
converge to

\[
 Y_{3/4}=\left(\frac{3\pi}{4\sqrt2}\right)^2
 =\frac{9\pi^2}{32},
 \qquad
 Y_1=\left(\frac\pi{\sqrt2}\right)^2
 =\frac{\pi^2}{2}.                                 \tag{37}
\]

Also \(Y_x=\kappa X_x\to Y_{3/4}\), because the one-cell uncertainty in
(8) has \(Y\)-size at most \(\kappa\tau\to0\). Multiplying the exact
shelf and head payment by \(\kappa\tau\), using (29), and changing
variables from \(X\) to \(Y\) gives

\[
 \begin{aligned}
 \liminf\kappa\tau
 \left(R_p+\frac d2m\right)
 &\geq
 -2\int_{Y_{3/4}}^{Y_1}(1-H_0(Y))\,dY
 +\frac{Y_{3/4}}2\\
 &=\frac{3Y_{3/4}}2-\frac{2Y_1}{3}\\
 &=\boxed{\frac{17\pi^2}{192}>0}.                 \tag{38}
 \end{aligned}
\]

The second equality uses
\(H_0(Y_{3/4})=3/4\) and \(H_0(Y_1)=1\). By (5),
\(\kappa\tau D_A(q)\geq0\). Hence (38) implies

\[
 \liminf\kappa\tau\mathcal S
 \geq\frac{17\pi^2}{192}>0,
\]

again contradicting negativity. Notice that no terminal asymptotic is
needed on this endpoint ray: the prefix-plus-head term itself has a
growing positive critical gap of order \(1/\kappa\) in the original
\(\tau\)-scaled variables.

## 6. Global exhaustion theorem and remaining work

Sections 2, 4, and 5 exclude every possible escaping sequence. We have
therefore proved the following.

For clarity about the topology in this conclusion, the fixed-ratio bound is
uniform on every ratio range bounded away from one, including as
\(\rho\downarrow0\). On the two shift grids which occur in the dimension
reduction one has \(r\geq1/2\); hence \(r<\rho K\) prevents
\(\rho\downarrow0\) when \(K\) is bounded. The compact-optical theorem and
Sections 4--5 exclude \(\rho\uparrow1\) for a negative sequence. Thus the
closure of the negative set is compact in the natural
\((\rho,K,r)\)-parameter space, not merely bounded in one chosen scaling.

### Theorem 6.1

In the universal active region \(K>\pi/(1-\rho)\), the set of ordinary
first-floor first-drop configurations

\[
 F_0=1,\qquad p<n,
 \qquad
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)<0
\]

is relatively compact in the exact shell parameter space. In particular,
there exist finite, although not presently explicit, bounds for all
discrete data \((r,n,p,Q,B)\) on which the scalar could fail. The case
\(p=0\) is automatic, and the conclusion includes the whole residual cone
\(n-p-1\geq2\).

This is a qualitative exhaustion, not a finite chamber certificate.
Compactness bounds the discrete labels but does not assert that the
remaining analytic wall set has finitely many connected components. The
remaining first-floor work is therefore confined to a bounded parameter
set and consists of certifying the exact scalar there. The existing
large-ray certificate and the stronger true-interface certificates for the
ten known weakened-envelope failures remain valid complementary inputs;
neither is used to overstate the compactness conclusion proved here.
