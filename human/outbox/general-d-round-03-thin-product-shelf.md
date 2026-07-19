# General dimension, Round 3: the active thin-product shelf lemma

Date: 18 July 2026

Status: rigorous limiting theorem and exact finite-shell reduction.  The
thin-product first-shelf scalar is strictly positive throughout the closure
of the dimension-independent active region.  Its margin is not uniform as
the optical thickness tends to infinity, so a separate finite-thickness
comparison is still required before this can be promoted to an exact shell
shifted-tail theorem.

## 1. Active scaling

Put

\[
 \varepsilon=1-\rho,
 \qquad
 a=\varepsilon K=K-\mu.
\]

The dimension-independent no-mode theorem says that the shifted-tail or
aggregate estimate is needed only when

\[
 a>\pi.
\]

In the thin-product scaling, keep \(a\) fixed, let
\(\varepsilon\downarrow0\), and write \(y=\varepsilon z\).  Homogeneity of
the ball action gives, on the inner branch,

\[
 A_{\varepsilon,a}(y/\varepsilon)
 =\frac a\varepsilon\left[
 G_1(y/a)-(1-\varepsilon)
 G_1\!\left(\frac{y}{a(1-\varepsilon)}\right)
 \right].
\]

Consequently

\[
 A_{\varepsilon,a}(y/\varepsilon)
 \longrightarrow
 B_a(y):=\frac{\sqrt{a^2-y^2}}\pi,
 \qquad 0\le y<a.
\]

Also \(d_\rho=2\arcsin(\rho)/\pi\to1\).  Thus the leading first-shelf
scalar is the one studied below.

## 2. The product shelf functional

Fix an ordinary floor level \(m\ge1\), and put

\[
 b=m-\frac14,
 \qquad
 y_b=\sqrt{a^2-\pi^2b^2}.
\]

The shelf exists only if \(a\ge\pi b\).  Let \(y_0\in[0,y_b]\) be a
permitted starting point, meaning

\[
 b\le B_a(y_0)<m+\frac34.
\]

Define

\[
 \boxed{
 \mathcal L_{a,m}(y_0)
 =2\int_{y_0}^{y_b}B_a(y)\,dy
 -2m(y_b-y_0)+\frac{a-y_b}{2}.}
 \tag{1}
\]

The first two terms are the scaled exact first-shelf reserve.  The final
term is the limiting concave-head payment
\(d_\rho(n-p)/2\).  For a stable non-wall family with
\(\varepsilon r\to y_0\), one has

\[
 \varepsilon\left(R_p+\frac{d_\rho}{2}(n-p)\right)
 \longrightarrow \mathcal L_{a,m}(y_0).
\]

The one-interface term has lower order for fixed \(a\): the terminal
distance is \(a+O(1)\), its action is \(O(\sqrt\varepsilon)\), and hence
\(\varepsilon D_A(q)\to0\).

## 3. Strict positivity

### Theorem 3.1

For every

\[
 a\ge\pi,
 \qquad m\ge1,
 \qquad a\ge\pi\left(m-\frac14\right),
\]

and every permitted \(y_0\), one has

\[
 \boxed{\mathcal L_{a,m}(y_0)>0.}
 \tag{2}
\]

### Proof

Differentiating (1) gives

\[
 \mathcal L_{a,m}'(y_0)=2\bigl(m-B_a(y_0)\bigr).
 \tag{3}
\]

There are two cases.

#### Case 1: \(a\ge\pi m\)

Set

\[
 y_m=\sqrt{a^2-\pi^2m^2}.
\]

Equation (3) shows that the minimum occurs at \(y_0=y_m\).  On
\([y_m,y_b]\), the function

\[
 f(y)=m-B_a(y)
\]

is strictly convex, with endpoint values \(0\) and \(1/4\).  Therefore it
lies strictly below its endpoint chord and

\[
 \int_{y_m}^{y_b}f(y)\,dy<\frac{y_b-y_m}{8}.
\]

It follows that

\[
 \mathcal L_{a,m}(y_m)
 =\frac{a-y_b}{2}
 -2\int_{y_m}^{y_b}f(y)\,dy
 >\frac{2a-3y_b+y_m}{4}.
 \tag{4}
\]

It remains to prove

\[
 2a+y_m\ge3y_b.
 \tag{5}
\]

Divide by \(\pi\), and write

\[
 s=\frac a\pi,
 \quad
 u=\sqrt{s^2-b^2},
 \quad
 v=\sqrt{s^2-m^2}.
\]

Thus (5) is \(2s+v\ge3u\).  If the first squaring has a nonpositive
right-hand side, the assertion is immediate.  Otherwise it reduces to

\[
 6uv\ge 6s^2-(9b^2+m^2).
 \tag{6}
\]

If the right side of (6) is nonpositive, there is again nothing to prove.
When it is positive, a second squaring is legitimate.  The difference
between the two squared sides is

\[
 24s^2(3b^2-m^2)
 -(81b^4-18b^2m^2+m^4).
 \tag{7}
\]

The positivity assumption in (6) gives

\[
 s^2>\frac{9b^2+m^2}{6}.
\]

Moreover

\[
 \frac{b^2}{m^2}
 =\left(1-\frac1{4m}\right)^2
 \ge\frac9{16}>\frac59.
\]

Using the lower bound for \(s^2\) in (7), its right side is strictly larger
than

\[
 27b^4-6b^2m^2-5m^4
 =m^4\left(27t^2-6t-5\right),
 \qquad t=\frac{b^2}{m^2}.
\]

The roots of \(27t^2-6t-5\) are \(-1/3\) and \(5/9\), so this is positive.
This proves (5), and (4) is strictly positive.

#### Case 2: \(\pi b\le a<\pi m\)

Now \(B_a(0)=a/\pi<m\), so (3) shows that the minimum occurs at
\(y_0=0\).  Write

\[
 s=\frac a\pi=b+\delta,
 \qquad 0\le\delta<\frac14,
 \qquad
 u=\frac{y_b}{\pi}=\sqrt{s^2-b^2}.
\]

On \([0,y_b]\), the same strictly convex function \(f=m-B_a\) has
endpoint values \(1/4-\delta\) and \(1/4\).  Its chord therefore gives

\[
 \mathcal L_{a,m}(0)
 >\frac\pi2\left[s-2(1-\delta)u\right].
 \tag{8}
\]

Both sides in the desired comparison
\(s\ge2(1-\delta)u\) are nonnegative.  After squaring, its difference is

\[
 E(b,\delta)
 =(b+\delta)^2
 -4(1-\delta)^2\bigl((b+\delta)^2-b^2\bigr).
\]

For \(b\ge3/4\) and \(0\le\delta\le1/4\), this expression is increasing in
\(b\), because

\[
 \partial_bE
 =2(b+\delta)-8\delta(1-\delta)^2>0.
\]

At \(b=3/4\), direct expansion gives

\[
 E\left(\frac34,\delta\right)
 =9\left(\delta-\frac14\right)^2
 +2\delta^3(1-2\delta)>0.
\]

Thus the bracket in (8) is positive.  This completes the proof.

## 4. The margin degenerates at large optical thickness

For fixed \(m\) and \(a\to\infty\), the minimizing point is \(y_m\).  The
expansion

\[
 \sqrt{a^2-\pi^2t^2}
 =a-\frac{\pi^2t^2}{2a}+O(a^{-3})
\]

in (1) gives

\[
 \boxed{
 \mathcal L_{a,m}^{\min}
 =\frac{\pi^2}{a}
 \frac{48m^2-36m+5}{192}
 +O(a^{-3}).}
 \tag{9}
\]

The coefficient is positive for every \(m\ge1\), but the margin tends to
zero.  Therefore Theorem 3.1 cannot be converted into an exact finite-shell
theorem by citing an unspecified uniform \(O(\varepsilon)\) perturbation.
One must either retain a signed next-order term or split off a large-\(a\)
sector using a quantitative terminal ball reserve.

## 5. Exact shell-to-product comparison

The product profile also gives a pointwise finite-shell comparison.  Put
\(a=K-\mu\), and, for \(0\le z\le\mu\), define

\[
 \mathcal E_{a,K}(z)
 =\frac a\pi\sqrt{1-\frac{z^2}{K^2}}.
\]

Differentiation of the ball action with respect to its radius gives the
exact identity

\[
 A(z)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{z^2}{s^2}}\,ds.
\]

Since the integrand increases with \(s\), one immediately has
\(A\le\mathcal E_{a,K}\).  For the reverse comparison, put
\(h=\mu-z\).  For \(\mu\le s\le K\), direct factorization gives

\[
 \frac{\sqrt{1-z^2/s^2}}{\sqrt{1-z^2/K^2}}
 \ge\sqrt{\frac{s-z}{K-z}}.
\]

Integrating this inequality yields the exact sandwich

\[
 \boxed{
 \Gamma\!\left(\frac{\mu-z}{a}\right)
 \mathcal E_{a,K}(z)
 \le A(z)\le\mathcal E_{a,K}(z),}
 \tag{10}
\]

where

\[
 \Gamma(x)=\frac23(1+x)
 \left[1-\left(\frac{x}{1+x}\right)^{3/2}\right].
\]

In particular,

\[
 \frac23\mathcal E_{a,K}(z)\le A(z)\le\mathcal E_{a,K}(z).
\]

Indeed,
\((1+x)-x^{3/2}/\sqrt{1+x}\ge1\), so \(\Gamma(x)\ge2/3\);
and differentiation, followed by
\(x(3+2x)^2<4(1+x)^3\), shows that \(\Gamma\) is increasing.  Also
\(\Gamma(x)\to1\) as \(x\to\infty\).  Thus the only possible
one-third loss is at the inner interface, while the comparison becomes
asymptotically exact deeper in the concave head.

## 6. Exact compact-optical consequence

Although the margin is not uniform for all \(a\), Theorem 3.1 does give a
genuine exact shell theorem on every bounded optical interval.

### Proposition 6.1

For every finite \(A_*>\pi\), there exists
\(\varepsilon_*(A_*)>0\) with the following property.  If

\[
 0<\varepsilon=1-\rho<\varepsilon_*(A_*),
 \qquad
 \pi\le a=\varepsilon K\le A_*,
\]

then the shifted-tail inequality holds for every
\(r\in\tfrac12\mathbb N\).

### Proof

The scaled actions converge uniformly on compact optical intervals:

\[
 \sup_{\substack{\pi\le a\le A_*\\0\le y\le a}}
 \left|
 A_{\varepsilon,a}(y/\varepsilon)-B_a(y)
 \right|\longrightarrow0.
 \tag{11}
\]

To verify (11), use the homogeneity formula in Section 1 on
\(y\le a(1-\varepsilon)\) and the outer formula
\((a/\varepsilon)G_1(y/a)\) above that point.  On a compact subinterval
away from \(y=a\), the mean-value theorem gives uniform convergence.  In a
fixed terminal neighborhood, the elementary turning bound
\(G_1(1-h)\ll h^{3/2}\) bounds both the scaled shell action and \(B_a\) by
a common quantity tending to zero with the neighborhood width.  This proves
(11).

Suppose the proposition were false.  There would be a sequence
\(\varepsilon_j\downarrow0\), optical thicknesses
\(a_j\in[\pi,A_*]\), and inner shifts \(r_j<\mu_j\) for which the
first-shelf scalar is nonpositive.  Pass to a subsequence with
\(a_j\to a\).  If the first ordinary floor is zero, every strict sample is
zero and there is nothing to prove.  Hence write that floor as \(m_j\ge1\).
Since

\[
 A_{\varepsilon_j,a_j}(0)=\frac{a_j}{\pi},
\]

the integers \(m_j\) range over a finite set; pass to a further subsequence
with \(m_j=m\).

Put

\[
 y_{0,j}=\varepsilon_jr_j,
 \qquad
 y_{p,j}=\varepsilon_j(r_j+p_j).
\]

After another subsequence, both have limits.  At the last inner grid point
\(q_j\), one has \(\varepsilon_jq_j\to a\).  Equation (11) therefore gives
\(A(q_j)\to B_a(a)=0\).  Since \(m\ge1\), the first shelf must leave before
\(q_j\), so \(p_j<n_j\) for all large \(j\).  The two shelf inequalities

\[
 A(r_j+p_j)\ge m-\frac14,
 \qquad
 A(r_j+p_j+1)<m-\frac14
\]

and (11) force

\[
 y_{p,j}\longrightarrow
 y_b=\sqrt{a^2-\pi^2(m-1/4)^2}.
\]

Also

\[
 \varepsilon_j n_j\longrightarrow a-y_0,
 \qquad
 \varepsilon_jp_j\longrightarrow y_b-y_0,
 \qquad
 d_{\rho_j}\longrightarrow1.
\]

Changing variables in the exact shelf reserve now gives

\[
 \varepsilon_j\left(
 R_{p_j}+\frac{d_{\rho_j}}2(n_j-p_j)
 \right)
 \longrightarrow \mathcal L_{a,m}(y_0)>0.
\]

Here a possible limiting upper floor wall
\(B_a(y_0)=m+3/4\) is harmless: the proof of Theorem 3.1 is unchanged on
the closure of the permitted starting set.  The displayed positive limit
contradicts nonpositivity of the sequence.  Thus the shelf scalar is
positive for all sufficiently small \(\varepsilon\), uniformly for
\(a\in[\pi,A_*]\).  The one-interface theorem gives \(D_A(q)\ge0\), and
the exact first-shelf reduction completes the shifted-tail proof.

The proposition is qualitative: it does not provide an explicit formula
for \(\varepsilon_*(A_*)\).  Its substantive conclusion is that the only
thin-shell residual has unbounded optical thickness \(a\to\infty\).

## 7. Exact finite-shell \(m=1\) reduction

There is nevertheless a useful exact inequality before taking the limit.
Assume the first ordinary floor is \(m=1\) and drops before the interface,
so \(p<n\).  Put

\[
 a_0=A(r),\qquad a_p=A(r+p),\qquad a_q=A(q),
 \qquad c_\rho=\frac{\arccos\rho}{\pi}.
\]

Every strict sample after \(p\) is zero, so the full strict count is at
most \(2p+1\).  Concavity on the two inner intervals gives

\[
 2\int_r^qA
 \ge p(a_0+a_p)+(n-p)(a_p+a_q).
\]

The full shell action is \(c_\rho\)-Lipschitz and nonnegative, hence the
terminal tangent triangle gives

\[
 2\int_q^KA\ge\frac{a_q^2}{c_\rho}.
\]

Therefore

\[
 \boxed{
 D_A(r)\ge
 p(a_0+a_p)+(n-p)(a_p+a_q)
 +\frac{a_q^2}{c_\rho}-(2p+1).}
 \tag{12}
\]

This exact scalar is positive in extensive active-region diagnostics, but a
uniform proof of (12)'s right-hand side has not yet been obtained.

The terminal term cannot simply be discarded even in the active region.
For example,

\[
 K=200,\qquad \mu=190,\qquad \rho=\frac{19}{20},
 \qquad r=185
\]

has \(K-\mu=10>\pi\), \(n=5\), \(p=4\), and first floor \(m=1\), but

\[
 R_p+\frac{d_\rho}{2}(n-p)
 =-0.5508937446\ldots.
\]

The one-interface reserve is

\[
 D_A(q)=5.3780962976\ldots,
\]

so the sharp shelf scalar remains positive.  This is an active-region
counterexample to every proof that tries to establish nonnegativity of the
concave prefix without coupling it to the terminal reserve.

## 8. Remaining exact obligation

The thin-product limit rules out a negative leading-order obstruction at
the no-mode boundary.  The next exact step is one of the following:

1. prove a signed finite-\(\varepsilon\) comparison between the shell scalar
   and \(\mathcal L_{a,m}\), retaining the first nonzero correction from the
   one-interface ball tail; or
2. prove (12) directly for \(m=1\), then extend its chord-plus-terminal
   argument one floor level at a time.

The asymptotic formula (9) shows that either route must be quantitative in
the large-\(a\), fixed-\(m\) corner.
