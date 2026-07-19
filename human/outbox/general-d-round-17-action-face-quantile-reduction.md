# General dimension, Round 17: quantile reduction on the action boundary

Date: 18 July 2026

Status: Round 16 reduces the hard one-level endpoint problem to the geometric
inequality \(F(K,a)\ge1/2\), proves \(F_K>0\), and therefore moves every
fixed-\(a\) point to either \(K=a+\pi\) or
\(A(a-1)=3/4\).  The radial boundary is already monotone toward the
intersection.  This note rewrites the derivative on the remaining action
boundary as one positive quantile reserve plus the integral of a strictly
increasing, strictly concave function.  The final endpoint payment is not yet
proved, so the first-floor branch and the all-dimensional theorem remain
open.

## 1. Action-boundary notation

Retain

\[
 G_b(s)=\frac{\sqrt{b^2-s^2}-s\arccos(s/b)}{\pi},
 \qquad
 J_b(s)=\int_s^bG_b(u)\,du,
\]

with both functions extended by zero past \(b\).  Put

\[
 A=G_K-G_a,\qquad
 A(x)=1,\qquad
 G_K(z)=\frac34,
\]

and consider the boundary

\[
 t=a-1,\qquad A(t)=\frac34,\qquad K-a>\pi.
 \tag{1.1}
\]

Write

\[
 \gamma=\arccos\frac{t}{K},\qquad
 \phi=\arccos\frac{t}{a}.
\]

Round 16 gives

\[
 K'(a)=\frac{\gamma+\sin\phi-\phi}{\sin\gamma}
 \tag{1.2}
\]

and

\[
 \frac{dF}{da}
 =K'\left(P_K(x)-\frac{\sin\theta}{\theta}\right)-P_a(x),
 \tag{1.3}
\]

where

\[
 P_b(s)=\frac{\partial J_b(s)}{\partial b},
 \qquad
 \theta=\arccos(z/K).
\]

The goal of this round is to expose the exact structure of (1.3), not to
replace it by a lossy bound.

## 2. Level quantiles

Define

\[
 h(\tau)=\sin\tau-\tau\cos\tau.
\]

For \(0\le c<b/\pi\), let \(\tau_b(c)\in[0,\pi/2)\) be determined by

\[
 \frac b\pi h(\tau_b(c))=c,
\]

and put

\[
 U_b(c)=\frac{\sin\tau_b(c)}{\tau_b(c)},
 \qquad U_b(0)=1.
 \tag{2.1}
\]

### Lemma 2.1 (exact quantile primitive)

For \(0\le s<b\),

\[
 \boxed{P_b(s)=\int_0^{G_b(s)}U_b(c)\,dc.}
 \tag{2.2}
\]

Indeed, if \(\beta=\arccos(s/b)\), then

\[
 P_b(s)
 =\frac1\pi\int_s^b\sqrt{1-\frac{u^2}{b^2}}\,du
 =\frac b\pi\int_0^\beta\sin^2\tau\,d\tau.
\]

Under \(c=bh(\tau)/\pi\), one has
\(dc=b\tau\sin\tau\,d\tau/\pi\), and (2.2) follows.

Let

\[
 g=G_a(x).
\]

Since \(A(x)=1\),

\[
 G_K(x)=g+1.
 \tag{2.3}
\]

Also \(\sin\theta/\theta=U_K(3/4)\).  Substitution of (2.2)--(2.3) into
(1.3) gives the exact decomposition

\[
 \boxed{
 \frac{dF}{da}
 =K'B_K+\int_0^g Q(c)\,dc,}
 \tag{2.4}
\]

where

\[
 B_K:=\int_0^1U_K(c)\,dc-U_K(3/4),
 \tag{2.5}
\]

\[
 Q(c):=K'U_K(c+1)-U_a(c).
 \tag{2.6}
\]

The first term is strictly positive.  The convex-quantile argument in Round
16 says that \(U_K\) is strictly convex and decreasing, so Jensen gives

\[
 \int_0^1U_K(c)\,dc>U_K(1/2)>U_K(3/4),
 \qquad B_K>0.
 \tag{2.7}
\]

Thus the previously opaque derivative consists of the same level-\(1\)
reserve that proved \(F_K>0\), plus one correlated comparison integral.

## 3. Exact boundary-speed inequality

The action wall in (1.1) is equivalent to

\[
 (\tan\gamma-\gamma)-(\tan\phi-\phi)
 =\frac{3\pi}{4t}.
 \tag{3.1}
\]

Using \(t=a\cos\phi=K\cos\gamma\), direct algebra gives the exact identity

\[
 \boxed{
 \frac Ka-K'
 =\frac{3\pi/4-\gamma+\phi}{a\sin\gamma}>0.}
 \tag{3.2}
\]

The sign follows from \(0<\phi<\gamma<\pi/2\).  In particular,

\[
 \frac{K'}K<\frac1a.
 \tag{3.3}
\]

This strict comparison is the dimensional factor needed to compare the two
quantile derivatives below.

## 4. The comparison integrand is strictly increasing

For \(0\le c\le g\), abbreviate

\[
 \beta(c)=\tau_K(c+1),\qquad
 \psi(c)=\tau_a(c).
\]

### Lemma 4.1 (paired-angle ordering)

On the strict action face,

\[
 \boxed{\beta(c)>\psi(c)\quad(0\le c\le g).}
 \tag{4.1}
\]

At \(c=0\), \(\beta>0=\psi\).  At \(c=g\), these are the angles of the
same spatial point \(x\) in the radii \(K>a\), so \(\beta>\psi\).  If an
interior equality occurred, then

\[
 \beta'(c)-\psi'(c)
 =\frac{\pi}{\beta\sin\beta}\left(\frac1K-\frac1a\right)<0.
\]

Every zero would therefore cross only from positive to negative.  Starting
and ending positive rules out such a zero.  On the simultaneous closure
\(K-a=\pi\), the ordering stays strict for \(c<g\) and becomes equality at
\(c=g\), where \(x=0\).  All derivative conclusions below remain strict
there because \(K'/K<1/a\).

Put

\[
 V(\tau)=\frac{h(\tau)}{\tau^3\sin\tau}.
\]

Round 16's convex-quantile calculation proves that \(V\) is strictly
decreasing.  Explicitly, after clearing positive factors,

\[
 V'(\tau)<0
 \quad\Longleftrightarrow\quad
 R(\tau):=3\sin^2\tau-\tau\sin(2\tau)-\tau^2>0,
\]

and

\[
 R(0)=0,\qquad
 R'(\tau)=4\cos\tau\,(\sin\tau-\tau\cos\tau)>0.
 \tag{4.2}
\]

Differentiating (2.1) gives

\[
 U_b'(c)=-\frac{\pi}{b}V(\tau_b(c)).
 \tag{4.3}
\]

Equations (3.3), (4.1), and the strict decrease of \(V\) now yield

\[
 \begin{aligned}
 Q'(c)
 &=\pi\left\{\frac{V(\psi(c))}{a}
 -\frac{K'V(\beta(c))}{K}\right\}\\
 &>0.
 \end{aligned}
 \tag{4.4}
\]

Thus

\[
 \boxed{Q\text{ is strictly increasing on }[0,g].}
 \tag{4.5}
\]

It has at most one zero.  If \(Q(0)\ge0\), then (2.4), (2.7), and (4.5)
prove \(dF/da>0\) immediately.

### Lemma 4.2 (strict concavity)

The same comparison function also satisfies

\[
 \boxed{Q''(c)<0\quad(0<c<g).}
 \tag{4.6}
\]

Differentiating (4.3) once more gives

\[
 U_b''(c)=\left(\frac{\pi}{b}\right)^2W(\tau_b(c)),
 \qquad
 W(\tau)=\frac{R(\tau)}{\tau^5\sin^3\tau}.
 \tag{4.7}
\]

The function \(W\) is strictly decreasing.  Its derivative has the desired
sign precisely when

\[
 (5\sin\tau+3\tau\cos\tau)R(\tau)
 >4\tau\sin\tau\cos\tau\,h(\tau).
 \tag{4.8}
\]

First,

\[
 R(\tau)-\tau\cos\tau\,h(\tau)
 =\sin\tau\{3h(\tau)-\tau^2\sin\tau\}>0,
\]

because the expression in braces vanishes at zero and has derivative
\(\tau h(\tau)>0\).  Multiplying this strict lower bound by
\(5\sin\tau+3\tau\cos\tau>4\sin\tau\) proves (4.8).

Now let \(s=K/a>1\) and \(k=K'\).  Equation (3.2) gives \(k<s<s^2\);
(4.1) and the decrease of \(W\) give \(W(\beta)<W(\psi)\).  Therefore

\[
 Q''(c)
 =\frac{\pi^2}{a^2}
 \left\{\frac{k}{s^2}W(\beta(c))-W(\psi(c))\right\}<0,
\]

which proves (4.6).

### Lemma 4.3 (positive upper endpoint)

At the critical point,

\[
 \boxed{Q(g)>0.}
 \tag{4.9}
\]

For a spatial variable \(s\in(0,a)\), put

\[
 \gamma_s=\arccos(s/K),\qquad
 \phi_s=\arccos(s/a),
\]

and \(u(\tau)=\sin\tau/\tau\).  Direct differentiation gives

\[
 \frac d{ds}\log\frac{u(\phi_s)}{u(\gamma_s)}
 =\frac{L(\phi_s)-L(\gamma_s)}s,
\qquad
 L(\tau)=\frac{\cot\tau}{\tau}-\cot^2\tau.
 \tag{4.10}
\]

The function \(L\) is strictly decreasing.  After clearing positive factors,
\(L'(\tau)<0\) is equivalent to

\[
 \tau\tan\tau+\sin^2\tau-2\tau^2>0.
\]

Indeed, \(\tan\tau>\tau+\tau^3/3\), while
\(\sin\tau>\tau-\tau^3/6>0\) gives
\(\tau^2-\sin^2\tau<\tau^4/3\).  Hence

\[
 \tau\tan\tau-\tau^2>
 \tau^2-\sin^2\tau.
\]

Since \(\phi_s<\gamma_s\), (4.10) proves that
\(u(\phi_s)/u(\gamma_s)\) is increasing in \(s\).  Now \(x<t=a-1\).
At \(s=t\), (1.2) gives

\[
 K'u(\gamma)
 =1-\frac{\phi-\sin\phi}{\gamma}
 >1-\frac{\phi-\sin\phi}{\phi}
 =u(\phi).
\]

Therefore

\[
 \frac{u(\psi(g))}{u(\beta(g))}
 <\frac{u(\phi)}{u(\gamma)}<K',
\]

which is precisely (4.9).  The simultaneous radial/action wall follows by
continuity; directly, both sinc factors there equal \(2/\pi\) and \(K'>1\).

## 5. The sole remaining endpoint payment

Concavity places \(Q\) above its endpoint chord, so

\[
 \int_0^gQ(c)\,dc
 \ge\frac g2\{Q(0)+Q(g)\}.
 \tag{5.1}
\]

Consequently the single scalar inequality

\[
 \boxed{
 \mathcal S:=
 K'B_K+\frac g2
 \left\{
 K'U_K(1)-1+
 K'U_K(g+1)-U_a(g)
 \right\}>0}
 \tag{5.2}
\]

proves \(dF/da>0\) on the whole action face.  This is now the selected
analytic payment.

For comparison, the only potentially unfavorable subcase has

\[
 Q(0)=K'U_K(1)-1<0.
\]

Let

\[
 c_-:=\sup\{c\in[0,g]:Q(c)<0\}.
\]

By (4.9), \(c_-\) is the unique zero.  Discarding the nonnegative part of
the \(Q\)-integral in (2.4), it is enough to prove

\[
 \boxed{
 K'B_K\ge\int_0^{c_-}\{-Q(c)\}\,dc.}
 \tag{5.3}
\]

There is also an exact one-radius form.  With \(\lambda=K/a\), the level
equations give

\[
 U_a(c)=U_K(\lambda c).
 \tag{5.4}
\]

Hence (2.4) is equivalently

\[
 \boxed{
 \frac{dF}{da}
 =K'\left\{\int_0^{g+1}U_K(c)\,dc-U_K(3/4)\right\}
 -\frac1\lambda\int_0^{\lambda g}U_K(c)\,dc.}
 \tag{5.5}
\]

Formulas (2.4) and (5.5) are exact.  Formula (5.2) discards only the positive
concavity area above the endpoint chord, while (5.3) instead discards the
nonnegative tail of \(Q\).  They retain the correlation among the boundary
speed, level-\(1\) reserve, and inner level range; bounding those pieces
independently would discard the mechanism being exposed.

## 6. Falsification status and gate

High-precision searches on the action face found \(dF/da>0\) from the
two-wall intersection through \(a=10^5\), with the derivative tending to
zero from above.  They also found the predicted pattern: \(Q(0)\) can be
negative, \(Q\) crosses at most once, and the positive reserve \(K'B_K\)
pays the negative initial area.  The chord scalar \(\mathcal S\) stayed
positive as well: approximately \(0.0854\) near the simultaneous wall,
\(0.0574\) at \(a=6\), and \(0.00708\) at \(a=100\), tending to zero from
above.  This is floating-point theorem-design evidence, not an interval
enclosure or a premise of Lemmas 2.1, 4.1, 4.2, or 4.3, or identity (3.2).

The next analytic round should prove \(\mathcal S>0\) in (5.2), or derive a
direct lower bound from the exact form (5.5).  It should not split by
\(\rho\), \(K\), or a list of
numerical intervals.  Once the action-face derivative and the transcendental
two-wall value are certified, Round 16's geometric lemma closes the hard
\(B=1\) first-floor branch.  The high-floor CST and the all-dimensional
theorem remain separate open obligations.
