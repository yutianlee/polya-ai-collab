# General dimension, Round 4c: the zero-level terminal reserve

Date: 18 July 2026

Status: rigorous auxiliary lemma.  This supplements the exact-angle
terminal estimate in the case where the translated ball tail has no active
integer action level.

Let

\[
 \mu=\rho K,\qquad q\leq\mu<q+1,
 \qquad A=G_K-G_\mu,
\]

and put

\[
 B=\left[G_K(q)+\frac14\right]_<,
 \qquad
 v=G_K(\mu),
 \qquad
 c=\frac{\arccos\rho}{\pi}.
\]

The level-by-level convex reserve used in Round 4 is strongest when
\(B\geq1\).  When \(B=0\), the following unused bottom triangle supplies
the missing quantitative payment.

## Proposition

If \(B=0\), then the shifted shell tail beginning at \(q\) has zero
discrete count and

\[
 \boxed{
 D_A(q)=2\int_q^K A(z)\,dz
 \geq 2\int_\mu^K G_K(z)\,dz
 \geq \frac{v^2}{c}.}
 \tag{1}
\]

Consequently, in the notation of the wall-safe first-shelf reduction,

\[
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\geq0
 \tag{2}
\]

whenever

\[
 \boxed{
 \frac{v^2}{c}\geq
 \frac{p-d_\rho(n-p)}2.}
 \tag{3}
\]

If the right side of (3) is nonpositive, the conclusion is already
automatic.

## Proof

The condition \(B=0\) is equivalent to \(G_K(q)\leq3/4\).  Since
\(A\leq G_K\) and both functions decrease, every strict bracket in the
tail beginning at \(q\) vanishes.  This proves the identity in (1).
Nonnegativity of \(A\) on \([q,\mu]\) and the identity
\(A=G_K\) on \([\mu,K]\) give its first inequality.

The ball action is decreasing and convex on \([\mu,K]\), with

\[
 G_K(\mu)=v,
 \qquad
 -G_K'(\mu)=c.
\]

It therefore lies above its tangent

\[
 z\longmapsto v-c(z-\mu).
\]

The zero of this tangent occurs no later than \(K\): this follows either
from convexity and \(G_K(K)=0\), or directly from
\(v\leq c(K-\mu)\).  Hence

\[
 2\int_\mu^K G_K(z)\,dz
 \geq 2\int_0^{v/c}(v-cs)\,ds
 =\frac{v^2}{c},
\]

which proves (1).  Finally, the first-shelf estimate gives
\(R_p\geq-p/2\).  Substitution in the reduced scalar proves (3).

All statements include the wall \(G_K(q)=3/4\): the strict bracket is
still zero there.

## A unified fractional-top refinement

The same observation strengthens the level-by-level convex reserve even
when active levels are present.  In the notation of that lemma, write

\[
 v=g(0),\qquad B=[v+\tfrac14]_<,
 \qquad c_v=-g'(0).
\]

Then

\[
 \boxed{
 D_g\geq
 \sum_{k=1}^{B}\left(\frac1{2c_k}-1\right)
 +\frac{(v-B)_+^2}{c_v}.}
 \tag{4}
\]

Indeed, the level intervals used in the earlier proof cover
\([0,B]\).  If \(v>B\), the inverse level length \(y(t)\) is convex and
its supporting tangent at the top endpoint \(t=v\) is

\[
 y(t)\geq\frac{v-t}{c_v}.
\]

The previously unused interval therefore contributes

\[
 2\int_B^v y(t)\,dt\geq\frac{(v-B)^2}{c_v}.
\]

If \(v\leq B\), the positive-part term vanishes and (4) is the earlier
lemma.  Thus (4) also contains the zero-level triangle when \(B=0\).

For the translated ball tail \(g(s)=G_K(q+s)\), put

\[
 v_q=G_K(q),\qquad
 \beta_q=\frac{\arccos(q/K)}\pi,
 \qquad
 B=\left[G_K(q)+\frac14\right]_<,
 \qquad
 Q=\left[A(q)+\frac14\right]_<.
\]

For \(1\le k\le B\), let \(\theta_k\) be the unique angle satisfying

\[
 \frac K\pi
 \bigl(\sin\theta_k-\theta_k\cos\theta_k\bigr)
 =k-\frac14.
\]

The exact one-interface identity consequently gives the refined terminal
certificate

\[
 \boxed{
 D_A(q)\geq
 \max\left\{0,
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\int_q^\mu G_\mu(z)\,dz
 +\frac{(v_q-B)_+^2}{\beta_q}
 \right\}.}
 \tag{5}
\]

Formula (5) preserves the exact terminal fraction instead of discarding
all action area above the last complete unit level.

## Use in the thin critical scaling

For \(\rho=1-\varepsilon\) and
\(K\asymp\varepsilon^{-3/2}\), one has

\[
 c\asymp\sqrt\varepsilon,
 \qquad v\asymp1.
\]

Thus the reserve \(v^2/c\) has the correct
\(\varepsilon^{-1/2}\) size.  It prevents the apparent loss obtained by
discarding the entire interval \(0<t<3/4\) when the active-level sum is
empty.  This observation is analytic; no numerical premise is used.
