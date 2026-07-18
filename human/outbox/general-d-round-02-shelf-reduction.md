# General dimension, Round 2: first-shelf reduction for arbitrary inner tails

Date: 18 July 2026

Status: rigorous reduction.  The arbitrary inner-tail theorem is reduced to
one explicit scalar inequality involving a one-interface ball defect and one
first-shelf reserve.  The scalar inequality is not yet proved globally.

## 1. Notation

Put

\[
 G_a(z)=\frac1\pi\left(\sqrt{a^2-z^2}-z\arccos\frac za\right),
 \qquad
 A(z)=G_K(z)-G_\mu(z),
 \qquad \mu=\rho K,
\]

with zero extension, and let

\[
 D_A(x)=2\int_x^K A(z)\,dz-
 \left(Q_0(x)+2\sum_{j\geq1}Q_j(x)\right),
 \qquad
 Q_j(x)=\left[A(x+j)+\frac14\right]_<.
\]

Fix an inner start \(r<\mu\), where \(r\in\frac12\mathbb N\), and set

\[
 n=\lfloor\mu-r\rfloor,
 \qquad q=r+n,
 \qquad \eta=\mu-q\in[0,1),
\]

\[
 c_\rho=\frac{\arccos\rho}{\pi},
 \qquad
 d_\rho=1-2c_\rho=\frac{2\arcsin\rho}{\pi}>0.
\]

For the concave head use the **ordinary** floors

\[
 F_j=\left\lfloor A(r+j)+\frac14\right\rfloor,
 \qquad 0\leq j\leq n.
\]

Let \(p\) be the last index of the first ordinary-floor shelf:

\[
 F_0=F_p>F_{p+1}\quad\hbox{if a drop occurs},
 \qquad p=n\quad\hbox{if no drop occurs}.
\]

Finally define the exact first-shelf reserve

\[
 \boxed{
 R_p(r):=2\int_r^{r+p}A(z)\,dz-2pF_0.}
 \tag{1}
\]

The use of ordinary floors only defines the shelf and licenses the published
concave theorem.  The tail defect \(D_A\) remains the strict defect.

## 2. Exact first-shelf reduction

### Theorem 2.1

For every \(0<\rho<1\), \(K>0\), and positive integer or half-integer
start \(r<\mu\),

\[
 \boxed{
 D_A(r)\geq
 D_A(q)+R_p(r)+\frac{d_\rho}{2}(n-p).}
 \tag{2}
\]

This statement is valid at every strict or ordinary floor wall.

### Proof

Write \(h(t)=A(r+t)+1/4\).  At half-tail scale, split the strict
trapezoidal sum at \(p\) and \(n\).  On \([0,p]\), all ordinary floors
equal \(F_0\), while every strict bracket is at most the corresponding
ordinary floor.  Thus the first block is at most \(pF_0\).

If \(p<n\), the ordinary floor drops immediately after the left endpoint
of \([p,n]\).  The FLPS concave first-shelf theorem, applied only to this
second block, gives

\[
 \mathbf T_{<}(h;p,n)
 \leq \int_p^n A(r+t)\,dt
 +\frac{n-p}{4}-\frac{1-c_\rho}{2}(n-p)
 =\int_p^n A(r+t)\,dt-\frac{d_\rho}{4}(n-p).
\]

When \(p=n\), this block is absent.  The remaining half-tail beginning at
\(q\) is exactly one half of the strict tail defining \(D_A(q)\).  Hence

\[
 \frac{T_A(r)}2
 \leq pF_0+\int_{r+p}^{q}A(z)\,dz
 -\frac{d_\rho}{4}(n-p)+\frac{T_A(q)}2.
\]

Subtracting from \(\int_r^K A\) and multiplying by two proves (2).
At an integral proxy wall a strict bracket is smaller than its ordinary
floor, so the same proof only gains reserve.  This proves wall safety.

## 3. Exact and lower-bound forms of the first-shelf reserve

Put

\[
 \varepsilon_j=A(r+j)+\frac14-F_j\in[0,1),
\]

and

\[
 \mathcal C_p=
 2\int_r^{r+p}A(z)\,dz
 -p\bigl(A(r)+A(r+p)\bigr).
\]

Concavity gives the exact nonnegative curvature representation

\[
 \mathcal C_p
 =-\int_0^p u(p-u)A''(r+u)\,du\geq0.
\]

Since \(F_0=F_p\), (1) becomes

\[
 \boxed{
 R_p=\mathcal C_p+p\left(\varepsilon_0+\varepsilon_p-\frac12\right).}
 \tag{3}
\]

In particular, the old coarse estimate is

\[
 R_p\geq-\frac p2.
 \tag{4}
\]

There is a stronger shell-specific lower bound.  Put

\[
 \sigma(z)=-A'(z),
 \qquad
 \kappa=\frac{1-\rho}{\pi\rho K}.
\]

On the inner branch, \(\sigma'=-A''\geq\kappa\).  Since
\(F_0=F_p\leq A(r+p)+1/4\),

\[
\begin{aligned}
 R_p
 &\geq -\frac p2+
 2\int_r^{r+p}\bigl(A(z)-A(r+p)\bigr)\,dz\\
 &=-\frac p2+2\int_0^p u\,\sigma(r+u)\,du\\
 &\geq-\frac p2+\sigma(r)p^2+\frac{2\kappa}{3}p^3.
\end{aligned}
 \tag{5}
\]

Combining (2) and (5) yields the completely explicit lower bound

\[
 D_A(r)\geq D_A(q)+\frac{d_\rho n}{2}
 -\frac{1+d_\rho}{2}p
 +2\int_0^p u\,\sigma(r+u)\,du.
 \tag{6}
\]

## 4. Optimized bounds for the shelf length

Equality of the endpoint ordinary floors implies

\[
 0\leq A(r)-A(r+p)<1.
\]

Since \(\sigma(0)=0\) and \(\sigma'\geq\kappa\),

\[
 1>\int_r^{r+p}\sigma(z)\,dz
 \geq\frac\kappa2\bigl((r+p)^2-r^2\bigr).
\]

Consequently

\[
 \boxed{
 p<\sqrt{r^2+a_\rho K}-r,
 \qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.}
 \tag{7}
\]

This strictly improves the archived estimate \(p<\sqrt{a_\rho K}\).
Using the actual initial slope gives the still sharper bound

\[
 \boxed{
 p<
 \frac{\sqrt{\sigma(r)^2+2\kappa}-\sigma(r)}{\kappa}.}
 \tag{8}
\]

There is also an exact floor-level cap.  Let \(m=F_0\).  If \(m=0\),
the strict tail is zero whenever \(A(r)+1/4\leq1\), so the desired
inequality is immediate.  For \(m\geq1\), define

\[
 U_m=\sup\left\{u\in[0,n]:A(r+u)\geq m-\frac14\right\}.
 \tag{9}
\]

Thus \(U_m=n\) if \(A(q)\geq m-1/4\); otherwise \(U_m\) is the unique
root of \(A(r+U_m)=m-1/4\).  The shelf definition gives

\[
 p\leq U_m.
 \tag{10}
\]

The cap (10) is often much stronger than (7)--(8), especially for thin
shells.

Define

\[
 \psi(u)=-\frac{1+d_\rho}{2}u
 +2\int_0^u v\,\sigma(r+v)\,dv.
 \tag{11}
\]

Then

\[
 \psi'(u)=-\frac{1+d_\rho}{2}+2u\sigma(r+u),
 \qquad
 \psi''(u)=2\sigma(r+u)+2u\sigma'(r+u)>0.
\]

Hence \(\psi\) has at most one interior minimizer, determined by

\[
 4u\sigma(r+u)=1+d_\rho.
 \tag{12}
\]

Equations (6), (10), and convexity give a floor-free uniform version of
the reduction:

\[
 \boxed{
 D_A(r)\geq D_A(q)+\frac{d_\rho n}{2}
 +\min_{0\leq u\leq U_m}\psi(u).}
 \tag{13}
\]

The minimum is the value at the point from (12), clamped to
\([0,U_m]\).  Replacing \(\sigma(r+u)\) by
\(\sigma(r)+\kappa u\) gives a closed cubic lower bound whose minimizer is

\[
 u_*=
 \frac{\sqrt{\sigma(r)^2+\kappa(1+d_\rho)}-\sigma(r)}{2\kappa},
\]

again clamped to the permitted interval.

## 5. Exact one-interface and terminal reserve

The point \(q\) has at most one inner cell.  Define the strict ball defect

\[
 D_K(q)=2\int_q^K G_K(z)\,dz-
 \left(
 \left[G_K(q)+\frac14\right]_<
 +2\sum_{j\geq1}\left[G_K(q+j)+\frac14\right]_<
 \right),
\]

the floor loss

\[
 \lambda_q=
 \left[G_K(q)+\frac14\right]_<
 -\left[G_K(q)-G_\mu(q)+\frac14\right]_<\geq0,
\]

and

\[
 \delta_q=\int_q^\mu G_\mu(z)\,dz.
\]

Then, including the case \(q=\mu\),

\[
 \boxed{D_A(q)=D_K(q)+\lambda_q-2\delta_q.}
 \tag{14}
\]

For \(0\leq x<a\), put

\[
 I_a(x)=\int_x^aG_a(z)\,dz
 =\frac{a^2}{4\pi}
 \left[
 \left(1+2\frac{x^2}{a^2}\right)\arccos\frac xa
 -3\frac xa\sqrt{1-\frac{x^2}{a^2}}
 \right].
 \tag{15}
\]

Thus \(\delta_q=I_\mu(q)\) exactly.  The turning estimate also gives

\[
 0\leq2\delta_q<\frac{4\sqrt2}{15}.
\]

For a pure outer start \(s\), let

\[
 t=\max\{s,K/2\}.
\]

The following quantitative terminal reserves are proved:

1. for every \(s\),
   \[
   D_K(s)\geq\frac12\lfloor G_K(t)\rfloor;
   \tag{16}
   \]
2. if \(G_K(s)\leq3/4\), every strict sample is zero and
   \[
   D_K(s)=2I_K(s);
   \tag{17}
   \]
3. if \(s\geq K/2\) and \(3/4<G_K(s)<1\), the low-action
   \(1/3\)-Lipschitz lemma gives
   \[
   D_K(s)>\frac{11}{16}.
   \tag{18}
   \]

When \(0<\eta<1\), put \(s=q+1\), zero-extend \(G_K\), and define the
first ball-cell increment

\[
 L_K(q)=2\int_q^{q+1}G_K(z)\,dz
 -\left[G_K(q)+\frac14\right]_<
 -\left[G_K(q+1)+\frac14\right]_<.
 \tag{19}
\]

Then \(D_K(q)=L_K(q)+D_K(q+1)\).  Therefore (16)--(18) can be used at the
true outer terminal start \(s\), rather than discarding its reserve.

Let \(R_{\rm term}(K,s)\) be the largest applicable right-hand side among
(16)--(18), and put

\[
 \mathcal B_K(q)=
 \max\left\{
 \frac12\lfloor G_K(\max\{q,K/2\})\rfloor,
 \ L_K(q)+R_{\rm term}(K,q+1)
 \right\}
 \tag{20}
\]

when \(0<\eta<1\).  For \(\eta=0\), use the terminal reserve directly at
\(q\).  Combining (2), (14), and (20) gives the fully proved certificate

\[
 \boxed{
 D_A(r)\geq
 R_p+\frac{d_\rho}{2}(n-p)
 +\mathcal B_K(q)+\lambda_q-2\delta_q.}
 \tag{21}
\]

The zero-count terminal reserve (17) is essential: it is much stronger
than (16) near the turning edge.

## 6. Comparison with the archived fixed-rho theorem

If (3) is weakened to \(R_p\geq-p/2\), (14) is bounded using only (16),
\(G_K(\max\{q,K/2\})\geq K\eta_\rho\), and \(\lambda_q\geq0\), then
(2) becomes exactly the archived estimate

\[
 D_A(r)\geq
 \frac12\left(
 \lfloor K\eta_\rho\rfloor+d_\rho(n-p)-p
 \right)-2\delta_q.
\]

Thus Theorem 2.1 strictly contains the fixed-rho high-energy packet.

The optimized shelf bound also improves its explicit threshold.  Since
\(r\geq1/2\), (7) gives

\[
 p<\sqrt{a_\rho K+\frac14}-\frac12.
\]

Consequently it is sufficient that

\[
 K\eta_\rho-\sqrt{a_\rho K+\frac14}
 \geq C_*:=\frac12+\frac{8\sqrt2}{15}.
 \tag{22}
\]

The positive root in \(K\) is

\[
 \boxed{
 K_{\rm new}(\rho)=
 \frac{
 a_\rho+2\eta_\rho C_*
 +\sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}
 }{2\eta_\rho^2}.}
 \tag{23}
\]

This is strictly smaller than the packet's threshold obtained from
\(p<\sqrt{a_\rho K}\).

## 7. The sharp remaining scalar

The strongest concise target furnished by this round is

\[
 \boxed{
 \mathfrak S(\rho,K,r)
 :=D_A(q)+R_p(r)+\frac{d_\rho}{2}(n-p)\geq0.}
 \tag{24}
\]

By Theorem 2.1, (24) proves the shifted-tail theorem at \(r\).  Substituting
(14) makes every term explicit:

\[
 \mathfrak S=
 D_K(q)+\lambda_q-2I_\mu(q)
 +2\int_r^{r+p}A(z)\,dz-2pF_0
 +\frac{d_\rho}{2}(n-p).
 \tag{25}
\]

Alternatively, the floor-level uniform scalar is

\[
 \boxed{
 D_A(q)+\frac{d_\rho n}{2}
 +\min_{0\leq u\leq U_m}\psi(u)\geq0.}
 \tag{26}
\]

Equation (26) has only one continuous minimization, whose minimizer is
specified by (12), followed by the one-interface defect (14).  Proving
(24), or the slightly stronger sufficient condition (26), is the next
global analytic obligation.

### 7.1 Automatic long-head region after the one-interface theorem

Assume only that the one-interface case has been completed, so that
\(D_A(q)\geq0\).  The coarse consequence of (2) and (4) is

\[
 D_A(r)\geq\frac12\bigl(d_\rho(n-p)-p\bigr).
\]

Therefore every tail satisfying

\[
 \boxed{
 n\geq\frac{1+d_\rho}{d_\rho}\,p}
 \tag{27}
\]

is already proved.  Combining (27) with (7), every unresolved tail must
lie in the explicit interface band

\[
 \boxed{
 n<\frac{1+d_\rho}{d_\rho}
 \left(\sqrt{r^2+a_\rho K}-r\right).}
 \tag{28}
\]

The sharper bound (8), or the exact floor cap (9), may replace the final
factor in (28).  In particular, if \(\rho\geq1/2\), then
\(d_\rho\geq1/3\), and the residual band simplifies to

\[
 n<4\left(\sqrt{r^2+a_\rho K}-r\right).
 \tag{29}
\]

Thus arbitrary long inner heads do not remain: after the one-interface
theorem, only a quantitatively specified neighborhood of the interface
needs the terminal reserve.

### 7.2 A genuinely compact residual for \(0<\rho\leq1/2\)

On \(0<\rho\leq1/2\), one has

\[
 \eta_\rho=\omega_0:=\frac{\sqrt3}{2\pi}-\frac16,
 \qquad a_\rho\leq2\pi.
\]

The right side of (23) is increasing in \(a_\rho\).  Hence all tails in
this ratio range with

\[
 K\geq K_*:=
 \frac{
 2\pi+2\omega_0 C_*
 +\sqrt{4\pi^2+8\pi\omega_0C_*+\omega_0^2}
 }{2\omega_0^2}
 \tag{30}
\]

are proved by (22).  Numerically, only for orientation,
\(K_*=551.6769\ldots\).  A residual low-interface tail has
\(1/2\leq r<\rho K\leq K/2\).  Consequently the unproved region for
\(0<\rho\leq1/2\) is contained in the compact set

\[
 \boxed{
 1<K<K_*,\qquad
 \frac1{2K_*}<\rho\leq\frac12,\qquad
 r\in\left\{\frac j2:j\in\mathbb N,\ j<K_*\right\}.}
 \tag{31}
\]

This is a finite-shift, compact two-parameter residual.  No numerical
verification of (31) is asserted here.

For bookkeeping, (31) also implies

\[
 q=r+n<\frac{K_*}{2},
 \qquad 0\leq n<\frac{K_*}{2},
 \qquad
 0\leq m\leq
 \left\lfloor\frac{K_*}{\pi}+\frac14\right\rfloor.
 \tag{31a}
\]

Thus the wall list in this compact sector is genuinely finite: at most
\(\lceil K_*\rceil-1\) positive half-grid starts,
\(\lceil K_*/2\rceil\) inner lengths for each compatible start, and
\(1+\lfloor K_*/\pi+1/4\rfloor\) possible ordinary action levels before
the elementary geometric constraints are imposed.  The displayed decimal
value of \(K_*\) gives 551, 276, and 176, respectively, but these decimal
counts are orientation rather than premises.

### 7.3 Coupling to the one-interface action

There are two useful explicit couplings between the first-shelf loss and
the terminal one-interface reserve.

First suppose that the strict tail beginning at \(q\) has zero count, or
equivalently

\[
 a_q:=A(q)\leq\frac34.
\]

The shell action is globally \(c_\rho\)-Lipschitz on \([q,K]\), decreases
from \(a_q\) to zero, and is nonnegative.  Therefore it lies above the
maximal-slope triangle

\[
 A(q+x)\geq(a_q-c_\rho x)_+.
\]

As the discrete tail is zero, this gives the quantitative bound

\[
 \boxed{
 D_A(q)=2\int_q^K A(z)\,dz\geq\frac{a_q^2}{c_\rho}.}
 \tag{32}
\]

If \(U_m<n\), then \(A(r+U_m)=m-1/4\).  Since
\(\sigma=-A'\) is increasing and convex on the inner branch,

\[
 \sigma''(z)=\frac z\pi\left(
 (\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}
 \right)>0,
\]

its graph lies below its endpoint chord on \([r+U_m,q]\).  Consequently

\[
 \boxed{
 a_q\geq m-\frac14-
 \frac{n-U_m}{2}
 \bigl(\sigma(r+U_m)+\sigma(q)\bigr).}
 \tag{33}
\]

The cruder bound obtained by replacing both slopes by \(c_\rho\) is also
valid.  In the zero-count chamber, (32)--(33) turn (26) into a smooth
inequality involving only \(U_m\), the two endpoint slopes, and the convex
minimum (12).

For a nonzero one-interface count, the exact floor loss in (14) can also
be written without a difference of strict brackets.  Put

\[
 B=G_K(q)+\frac14=M+e,
 \qquad M=[B]_<,
 \qquad e\in(0,1],
 \qquad h=G_\mu(q).
\]

Since \(B-h=A(q)+1/4>0\), strict-floor arithmetic gives

\[
 \boxed{\lambda_q=1+\lfloor h-e\rfloor.}
 \tag{34}
\]

Thus the refined one-interface lower bound is the explicit expression

\[
 D_A(q)\geq
 \frac12\lfloor G_K(\max\{q,K/2\})\rfloor
 +1+\lfloor h-e\rfloor-2I_\mu(q).
 \tag{35}
\]

Equations (32) and (35) are complementary: (32) retains the full terminal
area in the zero-count chamber, whereas (35) retains the integer ball
reserve and the exact first-sample loss in active chambers.

### 7.4 Monotonic reduction in the fractional interface

For fixed grid data \((r,n)\), write

\[
 q=r+n,
 \qquad \mu=q+\eta,
 \qquad K=\frac{q+\eta}{\rho},
 \qquad 0\leq\eta<1.
 \tag{36}
\]

This parametrizes every configuration having the same last inner grid
point.  For fixed \(\rho\) and every fixed \(z\), differentiation gives

\[
 \partial_\eta A(z)=
 \begin{cases}
 \displaystyle
 \frac1{\pi\rho}
 \sqrt{1-\frac{\rho^2z^2}{(q+\eta)^2}}
 -\frac1\pi
 \sqrt{1-\frac{z^2}{(q+\eta)^2}},&z<q+\eta,\\[3mm]
 \displaystyle
 \frac1{\pi\rho}
 \sqrt{1-\frac{\rho^2z^2}{(q+\eta)^2}},&z\geq q+\eta.
 \end{cases}
 \tag{37}
\]

The first line is positive after squaring, because \(0<\rho<1\), and the
second is manifestly positive.  Hence \(A(z)\) is strictly increasing in
\(\eta\).

Consider a combinatorial chamber in which all strict tail brackets, the
ordinary first floor \(m\), and its shelf endpoint \(p\) are fixed.  In
that chamber (24) has derivative

\[
 \boxed{
 \partial_\eta\mathfrak S
 =2\int_q^K\partial_\eta A(z)\,dz
 +2\int_r^{r+p}\partial_\eta A(z)\,dz>0.}
 \tag{38}
\]

Boundary terms at \(K\) vanish because \(A(K)=0\).  Thus, for fixed
\(\rho\), the sharp scalar is strictly increasing between floor walls.
When \(\eta\) crosses a floor wall upward, a strict bracket jumps only
immediately to the right of the wall.  It follows that the minimum over a
half-open \(\eta\)-cell occurs at either

- \(\eta=0\);
- the right-hand limit after a shell or ball strict-bracket wall; or
- the exact wall value **and** its right-hand limit when an ordinary floor
  defining \(m\) or \(p\) changes.

The last distinction is necessary: an ordinary floor takes its new value
at the integral wall, whereas the strict bracket still takes its old value
there.  Theorem 2.1 is valid for this mixed ownership, but the exact wall
must not be silently identified with either open chamber.

This reduces each compact two-parameter residual to one-dimensional
inequalities in \(\rho\) along an explicit finite wall list.

For completeness, at fixed \(\eta\) and inside a floor chamber,

\[
 \partial_\rho A(z)=
 -\frac{\mu}{\pi\rho^2}
 \sqrt{1-\frac{\rho^2z^2}{\mu^2}},
 \qquad \mu=q+\eta,
\]

and hence

\[
 \boxed{
 \partial_\rho\mathfrak S=
 -\frac{2\mu}{\pi\rho^2}
 \left(
 \int_q^K\sqrt{1-\frac{\rho^2z^2}{\mu^2}}\,dz
 +\int_r^{r+p}\sqrt{1-\frac{\rho^2z^2}{\mu^2}}\,dz
 \right)
 +\frac{n-p}{\pi\sqrt{1-\rho^2}}.}
 \tag{39}
\]

All integrals in (39) have the elementary primitive

\[
 \int\sqrt{1-\alpha^2z^2}\,dz
 =\frac z2\sqrt{1-\alpha^2z^2}
 +\frac{\arcsin(\alpha z)}{2\alpha}.
\]

For a nonhorizontal wall, write its elementary defining equation as

\[
 H(\rho,\eta)=N,
\]

where \(H\) is one of the shell or ball sample actions (or an endpoint
action defining a shelf change).  Since \(\partial_\eta H>0\), the wall is
locally a graph and

\[
 \eta_H'(\rho)=-\frac{\partial_\rho H}{\partial_\eta H}.
 \tag{40}
\]

The derivative of the right-hand wall limit is therefore

\[
 \boxed{
 \frac d{d\rho}\mathfrak S(\rho,\eta_H(\rho)^+)
 =\partial_\rho\mathfrak S
 -\partial_\eta\mathfrak S\,
 \frac{\partial_\rho H}{\partial_\eta H}.}
 \tag{41}
\]

All terms in (41) are given by (37)--(39) and elementary action
derivatives.  Thus, after the monotone \(\eta\)-reduction, every remaining
wall problem is a one-variable elementary inequality.  On the horizontal
boundary \(\eta=0\), candidate interior extrema are the zeros of (39).  On
a nonhorizontal wall, they are the zeros of (41).  The other required
checks are the wall endpoints.  This is the promised low-dimensional
monotone formulation.

Diagnostic sampling found no violation of (24) or (26).  This is not part
of the proof.  The proved terminal certificate (21) closes nearly all
sampled long tails; the remaining failures of that *certificate* occur in
small low-action ball shelves and do not violate (24).

## 8. False stronger statements

Several tempting simplifications are false.

1. **The concave prefix need not have nonnegative defect.**  At
   \[
   (\rho,K,r)=\left(\frac1{10},\frac{1099}{40},\frac12\right),
   \quad q=\frac52,
   \]
   one finds
   \[
   D_A(r)-D_A(q)=-0.0862293637\ldots.
   \]
   Here the first constant floor shelf together with its next floor-drop
   cell is already negative.

2. **Even the complete inner part plus the interface cell need not be
   nonnegative.**  At
   \[
   (\rho,K,r)=\left(\frac35,\frac{149}{20},\frac12\right),
   \quad \mu=4.47,
   \]
   the cumulative increment through the interface is
   \(-0.4013073106\ldots\).  The true outer zero-count reserve is
   \(D_K(4.5)=1.3343321474\ldots\), restoring positivity.

3. **There is no uniform action-proportional terminal reserve.**  For
   \(K=11\), \(s=10.5\),
   \[
   G_K(s)=0.0320645917\ldots,
   \qquad
   D_K(s)=0.0128174316\ldots
   <\frac12G_K(s).
   \]
   More generally, with \(h=K-s\downarrow0\),
   \[
   \frac{D_K(s)}{G_K(s)}\sim\frac45h\longrightarrow0.
   \]

4. **The \(11/16\) low-action reserve cannot be used before the
   \(1/3\)-Lipschitz point.**  For \(K=1551/500\), \(s=1/2<K/2\),
   \[
   G_K(s)=0.7502520578\ldots,
   \qquad
   D_K(s)=0.5389225474\ldots<\frac{11}{16}.
   \]

These examples show why (24) must retain both the exact first shelf and a
quantitative terminal ball reserve.

## 9. Next proof step

The next round should attack (26) directly.  The variables are now:

- the shell parameters \((\rho,K)\);
- the positive grid start \(r\);
- the integer \(n=\lfloor\mu-r\rfloor\);
- the first ordinary floor level \(m\);
- one continuous minimizer \(u\), fixed by (12) or an endpoint;
- the one-interface fractional part \(\eta=\mu-q\).

There is no longer a many-cell floor-dynamics problem.  High energy is
already covered by (22)--(23); exact zero-count terminal tails are covered
by (17); and all strict/ordinary wall ownership is explicit in (2) and
(14).  What remains is a scalar comparison between the one-interface ball
reserve and the possible negative first-shelf value in (11).
