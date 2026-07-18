# General dimension round 04: the high first-floor branch

Date: 18 July 2026  
Scope: the residual scalar in Proposition 7.1 when \(F_0\ge 2\)  
Status: new rigorous shelf and terminal estimates; the uniform high-floor
closure is not yet proved.

Write

\[
 \mu=\rho K,\qquad \delta=K-\mu,\qquad
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,
\]

and let \(p\) be the last index of the first ordinary-floor shelf,
\(F_0=F_p=f\).  Put

\[
 m=n-p,\qquad d=d_\rho=\frac{2\arcsin\rho}{\pi},\qquad
 R_p=2\int_r^{r+p}A(z)\,dz-2pf.
\]

The scalar to prove is

\[
 \mathscr S=D_A(q)+R_p+\frac d2m\ge0.                 \tag{1}
\]

All floors defining \(F_j\) are ordinary floors.  Strict brackets are
retained in \(D_A(q)\).  Thus an ordinary action wall has fractional
remainder zero on the shelf side and the favorable one-unit drop on the
strict-count side; none of the estimates below is obtained by an
unjustified limiting argument.

If \(p=0\), then \(R_0=0\), and (1) is automatic from the completed
one-interface theorem:

\[
 \mathscr S=D_A(q)+\frac d2n\ge0.
\]

Accordingly, Sections 2--5 assume \(p\ge1\).

## 1. Active coordinates and the immediate high-floor restriction

The universal spectral active condition has the particularly simple
form

\[
 K>\frac\pi{1-\rho}
 \quad\Longleftrightarrow\quad
 \boxed{\delta>\pi}.                                 \tag{2}
\]

Moreover \(A(0)=\delta/\pi\), and \(A\) is strictly decreasing on the
inner branch.  If \(f=F_0\ge2\), then

\[
 A(r)\ge f-\frac14,
 \qquad
 \boxed{\delta>\pi\left(f-\frac14\right)
              \ge\frac{7\pi}{4}.}                   \tag{3}
\]

Thus the active assumption is redundant in the high-floor branch once
(3) is imposed.

## 2. Three consequences of convexity of the inner slope

Set

\[
 \sigma=-A',\qquad
 \Delta=A(r)-A(r+p),qquad x=r+p.
\]

On \([0,\mu]\), \(\sigma\) is nonnegative, increasing, and convex, with
\(\sigma(0)=0\).  Hence \(\sigma(z)/z\) is nondecreasing.  This gives the
following rigorous estimates.

First,

\[
 \boxed{A(0)-A(r)\le \frac{r\Delta}{2p}.}             \tag{4}
\]

Indeed, \(\sigma(z)\le z\sigma(r)/r\) on \([0,r]\), while
\(\Delta\ge p\sigma(r)\).

Second, if \(x<q\), then

\[
 \boxed{
 A(x)-A(q)\ge
 \frac{\Delta}{p}\frac{q^2-x^2}{2x}.}               \tag{5}
\]

Here \(\sigma(x)\ge\Delta/p\), and
\(\sigma(z)\ge z\sigma(x)/x\) for \(z\ge x\).

Third, the shelf curvature reserve

\[
 \mathcal C_p
 =2\int_r^{r+p}A(z)\,dz-p\bigl(A(r)+A(r+p)\bigr)
 =\int_0^p(2t-p)\sigma(r+t)\,dt
\]

satisfies the scale-free bound

\[
 \boxed{
 \mathcal C_p\ge
 \frac{p^2}{3(2r+p)}\,\Delta.}                       \tag{6}
\]

To prove (6), use the positive hinge representation of a nonnegative
convex function vanishing at zero:

\[
 \sigma(z)=az+\int_{[0,\infty)}(z-s)_+\,d\nu(s),
 \qquad a\ge0,\quad \nu\ge0.
\]

It is enough to compare the two linear functionals in (6) on each
generator.  For the linear generator \(z\), their ratio is

\[
 \frac{p^3/6}{p(r+p/2)}
 =\frac{p^2}{3(2r+p)}.
\]

For a hinge with \(s\le r\), the ratio is

\[
 \frac{p^3/6}{p(r-s+p/2)}
 \ge\frac{p^2}{3(2r+p)}.
\]

For \(r<s<r+p\), put \(L=r+p-s\).  The ratio is

\[
 p-\frac{2L}{3}\ge\frac p3
 \ge\frac{p^2}{3(2r+p)};
\]

hinges to the right contribute zero.  Positive superposition proves
(6).

If

\[
 \varepsilon_j=A(r+j)+\frac14-F_j\in[0,1),
\]

then

\[
 R_p=\mathcal C_p+p\left(\varepsilon_0+\varepsilon_p-\frac12\right),
 \qquad \Delta=\varepsilon_0-\varepsilon_p.          \tag{7}
\]

Consequently \(R_p<0\) forces

\[
 \varepsilon_0+\varepsilon_p<\frac12,
 \qquad 0\le\Delta<\frac12,                         \tag{8}
\]

and (6)--(7) give the strengthened explicit shelf bound

\[
 \boxed{
 R_p\ge
 \frac{p^2\Delta}{3(2r+p)}
 +p\left(\varepsilon_0+\varepsilon_p-\frac12\right).} \tag{9}
\]

The inequalities (4)--(6) use only convexity of \(\sigma\), and are
therefore independent of the shell-specific lower curvature constant.

## 3. A quantitative convex-tail defect lemma

The main new estimate is a level-by-level reserve for a convex tail.

**Lemma.**  Let \(g\) be nonnegative, strictly decreasing, convex, and
continuously differentiable on \([0,L)\), with \(g(L)=0\), and extend it
by zero.  Put

\[
 T_g=[g(0)+\tfrac14]_<
       +2\sum_{j\ge1}[g(j)+\tfrac14]_<,
 \qquad
 D_g=2\int_0^L g(s)\,ds-T_g.
\]

Let \(v=g(0)\), \(B=[v+1/4]_<\), and
\(\tau_k=k-1/4\) for \(1\le k\le B\).  If \(y_k\) is determined by
\(g(y_k)=\tau_k\), and \(c_k=-g'(y_k)>0\), then

\[
 \boxed{D_g\ge\sum_{k=1}^{B}
       \left(\frac1{2c_k}-1\right).}                 \tag{10}
\]

**Proof.**  Let \(y(t)\) be the inverse level length,
\(g(y(t))=t\), and extend \(y\) by zero for \(t\ge v\).  Since \(g\)
is decreasing and convex, its inverse is decreasing and convex: at
smooth points

\[
 y'(t)=\frac1{g'(y(t))}<0,\qquad
 y''(t)=-\frac{g''(y(t))}{g'(y(t))^3}\ge0.
\]

The same conclusion follows from one-sided slopes in the nonsmooth
case.  At \(t=v\), adjoining the constant branch \(y=0\) replaces the
negative left slope by the right slope zero.  Slopes therefore remain
nondecreasing, so the zero extension is still convex.  Layer cake and
strict counting give

\[
 2\int_0^L g=2\int_0^v y(t)\,dt,
\]

while level \(\tau_k\) contributes exactly

\[
 1+2\#\{j\ge1:j<y(\tau_k)\}
 =2\lceil y(\tau_k)\rceil-1
 \le2y(\tau_k)+1.                                   \tag{11}
\]

The formula remains exact when \(y(\tau_k)\) is an integer, so later
sample walls cause no problem.  Convexity and the tangent at
\(\tau_k=k-1/4\) imply

\[
 \int_{k-1}^{k}y(t)\,dt
 \ge y(\tau_k)-\frac14y'(\tau_k)
 =y(\tau_k)+\frac1{4c_k}.                            \tag{12}
\]

If \(v<B\), the zero extension justifies the part of (12) above \(v\);
if \(v>B\), the unused integral from \(B\) to \(v\) is nonnegative.
Summing (12), multiplying by two, and subtracting (11) proves (10).

The strict convention is essential only in deciding which levels are
present: at the wall \(v+1/4\in\mathbb N\), the top equality level is
absent, exactly as required.

## 4. Application to the terminal ball tail

Apply (10) to

\[
 g(s)=G_K(q+s).
\]

Let

\[
 B=\left[G_K(q)+\frac14\right]_<,
 \qquad
 Q=\left[A(q)+\frac14\right]_<,
\]

and, for \(1\le k\le B\), let \(\theta_k\in(0,\pi/2]\) be the unique
solution of

\[
 \frac K\pi\bigl(\sin\theta_k-\theta_k\cos\theta_k\bigr)
 =k-\frac14.                                         \tag{13}
\]

At this level the ball slope has magnitude \(c_k=\theta_k/\pi\).
Therefore

\[
 D_K(q)\ge\sum_{k=1}^{B}
 \left(\frac\pi{2\theta_k}-1\right).                \tag{14}
\]

The exact one-interface identity is

\[
 D_A(q)=D_K(q)+(B-Q)-2\delta_\mu(q),
 \qquad
 \delta_\mu(q)=\int_q^\mu G_\mu(z)\,dz.             \tag{15}
\]

Combining (14)--(15), and also retaining the already proved
nonnegativity of \(D_A(q)\), yields the rigorous terminal reserve

\[
 \boxed{
 D_A(q)\ge
 \max\left\{0,
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\delta_\mu(q)\right\}.}                        \tag{16}
\]

This is substantially stronger in shallow-slope regimes than the
existing half-floor reserve.

There is also a root-free version.  Since

\[
 \sin\theta-\theta\cos\theta
 =\int_0^\theta s\sin s\,ds
 \ge\frac{2\theta^3}{3\pi}
 \qquad(0\le\theta\le\pi/2),
\]

equation (13) gives

\[
 \frac\pi{2\theta_k}
 \ge C_0K^{1/3}(k-\tfrac14)^{-1/3},
 \qquad
 C_0=\frac\pi2\left(\frac{2}{3\pi^2}\right)^{1/3}. \tag{17}
\]

Thus, with

\[
 S_B=\sum_{k=1}^{B}(k-\tfrac14)^{-1/3},
\]

one has the fully explicit bound

\[
 \boxed{
 D_A(q)\ge
 \max\{0,C_0K^{1/3}S_B-Q-2\delta_\mu(q)\}.}          \tag{18}
\]

The cap term in (16) and (18) is explicit from the ball-action
antiderivative.  In particular it need not be replaced by the much
larger uniform bound \(4\sqrt2/15\).

## 5. A rigorous strengthened certificate for the high-floor scalar

Equations (1) and (16) show that every high-floor tail is proved as soon
as

\[
 \boxed{
 \Phi:=R_p+\frac d2m+
 \max\left\{0,
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\delta_\mu(q)\right\}\ge0.}                    \tag{19}
\]

Replacing the sum in (19) by \(C_0K^{1/3}S_B\) gives a weaker but
root-free sufficient certificate.  The shelf term \(R_p\) may in turn
be bounded by (9).  All quantities in (19) are explicit functions of
\((\mu,K)\) once the discrete chamber

\[
 (r,n,p,f,Q,B)
\]

is fixed.  Hence (19) is well suited to a wall-monotonicity argument or
a rigorous interval certificate.  This note does **not** claim that
(19) has yet been proved nonnegative on every admissible chamber.

## 6. Diagnostics, not proof

Several broad floating-point scans were used only to assess (19).

- No counterexample to the exact scalar (1) was found in the sampled
  high-floor region.  In an initial 180,000-point log-scale scan, its
  smallest sampled value was about \(1.40\).
- A 500,000-point log-scale scan restricted to the genuinely dangerous
  conditions \(R_p<0\) and \(p>d(n-p)\) found no failure of the stronger
  certificate (19); its smallest sampled value was about \(0.157\).
- If the exact angles and exact cap in (19) are weakened to the cubic
  estimate (17) and the uniform cap bound, sampled failures remain.
  In one 800,000-point scan they occurred only at \(f=2\), in fourteen
  sampled integer patterns with \(n\le8\).  Using the exact angles but
  still the uniform cap reduced those diagnostics to the three patterns
  \((n,p,Q,B)=(2,1,1,1),(3,2,1,1),(4,2,1,1)\).
  Restoring the exact cap removed those sampled failures.

These observations do not prove that \(f\ge3\) is automatic, that the
listed patterns are exhaustive, or that (19) is globally nonnegative.
They identify a much sharper proof target and show why replacing the
terminal cap by its universal turning bound loses the last small
chambers.

## 7. Exact remaining status

The high-floor branch has not been closed uniformly.  What is now proved
is:

1. the scale-free shelf curvature estimate (6), together with (4), (5),
   and the wall-safe remainder consequences (8)--(9);
2. the quantitative inverse-level convex-tail lemma (10);
3. the exact-angle terminal reserve (16), its explicit cubic corollary
   (18), and the sufficient scalar certificate (19).

The next rigorous step should be either:

- prove (19) directly from (3)--(9), separating the no-drop case
  \(p=n\) from \(p<n\); or
- derive an analytic exhaustion of the discrete chambers on which the
  weaker version of (19) can fail, then certify those chambers with the
  exact-angle and exact-cap expression.
