# General dimension, Round 21: intrinsic high-floor CST reduction

Date: 19 July 2026  
Status: rigorous reduction; high-floor CST remains open

## 0. Scope and theorem boundary

This note attacks only the high-floor first-drop branch

\[
 f=F_0\geq2,\qquad p<n,\qquad m:=n-p\geq1.
\]

It follows the simplified analytic strategy: the exact reduced scalar

\[
 \mathscr S=D_A(q)+R_p+\frac{d_\rho m}{2}
\]

and the correlated lower scalar \(\Phi_\delta\) are kept distinct.  No
ratio partition and no compact certificate is introduced.

The following are proved below.

1. On the extension grids, the local inner cap has the uniform exact bound
   \(2\int_q^\mu G_\mu<1/7\).
2. The complete ball levels already present at the interface give the
   terminal payment \(B_0d_\rho/(2c)\), where
   \(c=\arccos\rho/\pi\).
3. When the interface lies within one action unit of the first-shelf wall,
   the retained top interval gives an additional intrinsic payment.  This
   is safe when an inverse displacement approaches an integer from the
   bad side and its fractional reserve tends to zero.
4. Shell-increment elasticity and shell curvature give two simultaneous
   lower bounds for the shelf remainder difference.  Combining them with
   the terminal payment reduces CST to one explicit intrinsic scalar.

The final sign of that scalar is **not** proved here.  Thus neither CST-H
nor the all-dimensional Polya theorem is promoted by this note.

Throughout, put

\[
 c=\frac{\arccos\rho}{\pi},\qquad d=d_\rho=1-2c,
 \qquad h=f-\frac14,
\]

\[
 W=G_K(\mu),\qquad \lambda=h-W>0,
 \qquad B_0=[W+\tfrac14]_<=[f-\lambda]_<.
\]

The strict inequality \(\lambda>0\) follows from the first drop: the
sample \(r+p+1\leq q\leq\mu\) is below the \(f\)-wall, and the shell
action is decreasing.

Write

\[
 \alpha=\mu-q\in[0,1),\qquad X=m+\alpha=\mu-(r+p).
\]

On the first shelf, use

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(r+p)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p\geq0,
 \qquad a_p=\frac{p^2}{3(2r+p)}.
\]

The lower scalar from Round 10 is

\[
 \Phi_\delta=L_T+a_p\Delta+p(E-\tfrac12)+\frac{dm}{2},                 \tag{0.1}
\]

where \(L_T\) is the raw fractional terminal lower bound.  Equation
(0.1), unlike \(\mathscr S\), contains the tangent and curvature losses.

The case \(p=0\) is automatic from \(D_A(q)\geq0\) and \(dm/2>0\).
Hence only \(p\geq1\) is considered below.

## 1. A uniform local-cap bound on the extension grids

### Lemma 1.1

For a high-floor first drop on the new integer or half-integer extension
grids,

\[
 q\geq2,
 \qquad
 J:=2\int_q^\mu G_\mu(z)\,dz<\frac17.                                \tag{1.1}
\]

### Proof

The integer extension begins at \(r=1\), the half-integer extension at
\(r=3/2\), and \(n\geq1\).  Thus \(q=r+n\geq2\).  Since
\(q\leq\mu<q+1\) and the ball cap increases with its radius,

\[
 J<2I_{q+1}(q),\qquad I_a(x)=\int_x^aG_a(z)\,dz.
\]

The function \(q\mapsto I_{q+1}(q)\) is decreasing.  Indeed, using the
radius-average representation and writing \(z=q+x\), \(R=q+y\),

\[
 I_{q+1}(q)=\frac1\pi\int_{0\leq x\leq y\leq1}
 \sqrt{1-\left(\frac{q+x}{q+y}\right)^2}\,dy\,dx.
\]

For fixed \(0\leq x<y\leq1\), the quotient \((q+x)/(q+y)\) increases
with \(q\), so the integrand decreases.  Therefore

\[
 J<2I_3(2)=\frac{17\arccos(2/3)-6\sqrt5}{2\pi}.                       \tag{1.2}
\]

For a fully rational check, use

\[
 \arccos\frac23=\frac\pi4+\arctan(9-4\sqrt5)
 <\frac{11}{14}+9-4\frac{682}{305}
 =\frac{3593}{4270}.
\]

Here \(\pi<22/7\), \(\arctan u<u\) for \(u>0\), and
\((682/305)^2<5\).  Also \(\pi>333/106\).  Hence

\[
 17\arccos\frac23-6\sqrt5
 <\frac{3793}{4270}
 <\frac{333}{371}<\frac{2\pi}{7};
\]

the middle difference is \(2101/226310>0\).  Substitution in (1.2)
proves (1.1).  The completed three-dimensional \(r=1/2\) base case is
not a new extension-grid obligation.

## 2. Interface complete levels and the top-interval transport

At the terminal point put

\[
 v=G_K(q),\qquad B=[v+\tfrac14]_<,
 \qquad Q=[A(q)+\tfrac14]_<,
 \qquad \beta=\frac{\arccos(q/K)}\pi.
\]

For \(1\leq k\leq B\), let

\[
 \beta_k=\frac{\theta_k}{\pi},\qquad
 G_K(K\cos\theta_k)=k-\frac14.
\]

The Round 10 terminal bound is

\[
 L_T=\sum_{k=1}^{B}\frac1{2\beta_k}
      +2\sum_{k=1}^{B}\eta_k-Q-J
      +\frac{(v-B)_+^2}{\beta}.                                      \tag{2.1}
\]

### Proposition 2.1 (interface-level transport)

Every high-floor first drop satisfies

\[
 \boxed{L_T>\frac{B_0d}{2c}-\frac17.}                                \tag{2.2}
\]

If \(0<\lambda<1\), then \(B_0=f-1\), and the stronger bound

\[
 \boxed{
 L_T>\frac{(f-1)d}{2c}+\mathcal E(\lambda)-\frac17,
 \qquad
 \mathcal E(\lambda)=
 \min\left\{1,\,2(\tfrac34-\lambda)_+^2\right\}.}                 \tag{2.3}
\]

holds.  Neither estimate uses a fractional inverse displacement.

### Proof

First drop and monotonicity give \(Q\leq f-1\).  Also \(v\geq A(q)\),
so \(B\geq Q\), and \(v\geq W\), so \(B\geq B_0\).

For \(k\leq B_0\), strict counting gives

\[
 k-\frac14<W=G_K(\mu).
\]

The corresponding outer inverse therefore lies strictly beyond \(\mu\),
so

\[
 \theta_k<\arccos\rho=\pi c,
 \qquad \frac1{2\beta_k}>\frac1{2c}.
\]

For every remaining complete level, \(q>0\) gives
\(\beta_k<1/2\) and hence \(1/(2\beta_k)>1\).  Dropping the nonnegative
fractional and top terms in (2.1), and using Lemma 1.1, yields

\[
 L_T>\frac{B_0}{2c}+(B-B_0)-Q-\frac17
 =\frac{B_0d}{2c}+(B-Q)-\frac17,
\]

which proves (2.2).

If \(0<\lambda<1\), then

\[
 B_0=[f-\lambda]_< =f-1,
 \qquad Q\leq B_0.
\]

When \(B\geq B_0+1\), the term \(B-Q\) supplies at least one.  When
\(B=B_0\), one has

\[
 v-B_0\geq W-B_0=\frac34-\lambda,
 \qquad \beta<\frac12,
\]

so the top interval in (2.1) supplies

\[
 \frac{(v-B_0)_+^2}{\beta}>
 2(\tfrac34-\lambda)^2
\]

when \(\lambda<3/4\).  If \(\lambda\geq3/4\), the required lower
payment is zero and follows from nonnegativity of the top interval.

Taking the smaller payment valid on the two faces proves (2.3).  At an
inverse spatial wall the term \(\eta_k\) may jump from one to zero on the
bad side; it was not used.  At an action wall the literal strict values of
\(B_0\), \(B\), and \(Q\) used above give the stated ownership.

## 3. Elasticity and curvature on the same shelf

Let

\[
 H(t)=A(\mu-t),\qquad V(t)=t(2\mu-t).
\]

At the last point of the first shelf and at its start,

\[
 H(X)-W=\lambda+e_p,
 \qquad
 H(X+p)-W=\lambda+e_0.                                                \tag{3.1}
\]

The exact shell-increment elasticity theorem therefore gives

\[
 \frac{\lambda+e_0}{\lambda+e_p}
 \geq \sqrt{\frac{V(X+p)}{V(X)}}
 =:s>1.                                                              \tag{3.2}
\]

Since \(\mu=r+p+X\), the ratio is the intrinsic expression

\[
 s=\sqrt{
  1+\frac{p(2r+p)}{X(X+2r+2p)} } .                                  \tag{3.3}
\]

It follows from (3.2) that

\[
 \boxed{\Delta=e_0-e_p
 \geq(s-1)(\lambda+e_p)
 \geq(s-1)\lambda.}                                                  \tag{3.4}
\]

There is a second, independent curvature payment.  On the inner branch,

\[
 \sigma=-A',\qquad \sigma(0)=0,qquad
 \sigma'\geq\kappa,qquad
 \kappa=\frac{1-\rho}{\pi\rho K}.
\]

Consequently

\[
 \boxed{
 \Delta=A(r)-A(r+p)
 =\int_r^{r+p}\sigma(z)\,dz
 \geq\frac\kappa2p(2r+p).}                                         \tag{3.5}
\]

Define the simultaneous wall/curvature payment

\[
 L_0:=\max\left\{
 (s-1)\lambda,
 \frac\kappa2p(2r+p)
 \right\}.                                                          \tag{3.6}
\]

Since \(E\geq\Delta\geq L_0\), the exact shelf identity and the
scale-free curvature estimate give

\[
\boxed{
 R_p+\frac{dm}{2}
 \geq(p+a_p)L_0-\frac p2+\frac{dm}{2}.}                              \tag{3.7}
\]

The surrogate shelf combination appearing in \(\Phi_\delta\) obeys the
same lower bound directly:

\[
 \boxed{
 a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}
 \geq(p+a_p)L_0-\frac p2+\frac{dm}{2}.}                              \tag{3.8}
\]

Indeed, both (3.7) and (3.8) use only \(E\geq\Delta\geq L_0\), with
(3.7) additionally using \(\mathcal C_p\geq a_p\Delta\).

This is the desired intrinsic trichotomy in compressed form:

- large \(E\) pays through the remainder term;
- large \(\Delta\) pays through \(a_p\Delta\) and (3.5);
- when both are small, (3.4) transports the interface wall gap into a
  quantitative lower bound for \(\Delta\).

No ratio endpoint occurs in (3.4)--(3.7).

## 4. The remaining intrinsic scalar

The raw parameters can be eliminated exactly.  Put

\[
 \theta=\pi c,\qquad
 \varphi(\theta)=\sin\theta-\theta\cos\theta.
\]

Since \(W=K\varphi(\theta)/\pi\) and \(\rho=\cos\theta\),

\[
 K=\frac{\pi W}{\varphi(\theta)},qquad
 \mu=\frac{\pi W\cos\theta}{\varphi(\theta)},                      \tag{4.1}
\]

\[
 \kappa=
 \frac{(1-\cos\theta)\varphi(\theta)}
      {\pi^2\cos\theta\,W},
 \qquad W=f-\frac14-\lambda.                                       \tag{4.2}
\]

The exact feasibility relation is

\[
 \boxed{
 \alpha=\frac{\pi(f-\frac14-\lambda)\cos\theta}
                  {\varphi(\theta)}-r-p-m\in[0,1),
 \qquad X=m+\alpha.}                                                 \tag{4.3}
\]

This correlation is essential; treating \((r,p,m,c,\lambda,f)\) as
independent creates false abstract negative tuples that no shell realizes.

Combining (0.1), Propositions 2.1, and (3.7) proves the following exact
sufficient reduction.

### Theorem 4.1 (conditional intrinsic closure)

For every feasible high-floor first-drop tuple satisfying (4.3), define

\[
 \boxed{
 \begin{aligned}
 \mathcal R={}&(p+a_p)L_0-\frac p2+\frac{dm}{2}
 +\frac{B_0d}{2c}-\frac17\\
 &+\mathbf 1_{\{0<\lambda<1\}}
 \min\left\{1,\,2(\tfrac34-\lambda)_+^2\right\}.
 \end{aligned}}                                                     \tag{4.4}
\]

Then

\[
 \boxed{\Phi_\delta>\mathcal R.}                                   \tag{4.5}
\]

In particular, proving \(\mathcal R\geq0\) on the intrinsic feasible
domain (4.3) proves the high-floor CST lower surrogate and hence CST-H.

### Proof

Equation (3.8) bounds the shelf and post-drop part of (0.1).  Equation
(2.2) bounds its terminal part for every \(\lambda>0\), and (2.3) adds
the final term of (4.4) when \(0<\lambda<1\).  This gives (4.5).

### Current obstruction

The sign

\[
 \boxed{\mathcal R\geq0\quad\text{under (4.3)}}                     \tag{4.6}
\]

is the first genuine remaining inequality in this route.  It is much
smaller than the original floor problem: it contains no terminal roots,
no inverse fractions, and no shell or ball floor variables other than the
single strict interface count \(B_0=[f-\lambda]_<\).  Nevertheless, a
proof of (4.6) still has to use the exact feasibility relation (4.3).
The elasticity inequality alone, with that relation discarded, is not
strong enough: it permits large formal shelves with small wall gap that
are incompatible with the shell radius fixed by \((c,W)\).

A non-rigorous double-precision stress sweep found no negative value of
the weaker version obtained by replacing \(X=m+\alpha\) in (3.3) by
\(m+1\); the smallest sampled value was about \(0.0495\).  This is
theorem-design evidence only and is not used in (4.5).

## 5. Strict spatial-wall calibration

The relevant hard diagnostic is the corrected wall

\[
 G_{K_0}(7)=\frac34,qquad
 K_0=11.0492679850480\ldots,qquad q=5.
\]

On the right side of this wall, the first inverse displacement satisfies
\(y_1\downarrow2^+\), so \(\eta_1\downarrow0\).  A representative
high-floor point has

\[
 r=1,\quad n=4,\quad p=2,\quad m=2,
 \quad \rho=0.4559578071\ldots,
 \quad \alpha=0.0380000005\ldots.
\]

There

\[
 f=2,\quad B_0=B=Q=1,\quad
 \lambda=0.3795411223\ldots,
\]

and the terminal pieces on the bad side are approximately

\[
 \frac\pi{2\theta_1}-1=0.775524603,qquad
 2\eta_1\longrightarrow0,qquad
 \frac{(v-1)^2}{\beta}=0.420135639,qquad
 J=0.000030117.
\]

Thus

\[
 L_T=1.195630125\ldots,qquad
 a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}
 =-0.357364051\ldots,
\]

\[
 \Phi_\delta=0.838266073\ldots.
\]

At this particular face, the exact tangent excess already pays the
negative shelf bound.  In the root-free uniform reduction (2.3), however,
the tangent excess is weakened to \(d/(2c)\) and the cap to \(1/7\); the
top-interval term is then load-bearing.  Indeed, (2.3) still gives the
terminal lower bound

\[
 \frac d{2c}+\mathcal E(\lambda)-\frac17
 =0.563069878\ldots,
\]

which pays the displayed shelf bound with reserve about \(0.2057\).
The fractional inverse term is not used at all.  Hence the strict spatial
wall is covered by the proposed intrinsic mechanism rather than by a
one-sided continuity assertion.

## 6. Next analytic step

The next round should prove or falsify (4.6) directly.  The natural order
is:

1. use (4.3) to eliminate \(\lambda\) or \(c\) on each fixed discrete
   tuple, retaining literal strict walls;
2. prove monotonicity in the interface count \(B_0\) or the floor \(f\),
   if valid, so that the observed hard face \(f=2\), \(B_0=1\) is the
   analytic endpoint rather than a numerical guess;
3. use the maximum in (3.6) as the remainder/curvature dichotomy, not a
   ratio subdivision;
4. if (4.6) is false, return to the exact scalar \(\mathscr S\) or the
   weighted aggregate theorem.  Do not add another ratio ladder.
