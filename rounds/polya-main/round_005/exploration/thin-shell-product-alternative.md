# Thin-shell product alternative from the separated operator bound

## Outcome

The operator estimate

\[
\lambda_{\ell,n}\ge
\left(\frac{n\pi}{\epsilon}\right)^2+\ell(\ell+1)
\]

does give a clean analytic thin-shell range when its angular count is
handled exactly. For example, the argument below proves the shell Weyl
bound from this estimate alone whenever

\[
0<\epsilon\le\frac1{100},
\qquad
a:=\epsilon K\le\frac{\pi}{4\epsilon}.
\]

More generally, for every fixed \(c<3\pi/4\), it works uniformly up to
\(a\le c/\epsilon\) once \(\epsilon\) is sufficiently small.

There is, however, a structural obstruction to using this product bound
to overlap the existing fixed-\(\rho\) high-energy theorem. The exact
product majorant itself crosses above the shell Weyl term at the sharp
scale

\[
a\sim\frac{3\pi}{4\epsilon}.
\]

In contrast, the existing explicit threshold, with
\(\rho=1-\epsilon\), begins at

\[
\epsilon K_0(1-\epsilon)
\sim\frac{9\pi^3}{4}\epsilon^{-3}.
\]

Thus the two ranges are separated by two powers of \(\epsilon\). The
failure is not caused by the angular ceiling estimate: using the exact
\(\ell(\ell+1)\) count changes only a lower-order term. It comes from
replacing \(r^{-2}\) by its outer-boundary minimum \(1\), which gives
the product comparison the outer-sphere cross-section instead of the
smaller mean shell cross-section.

This report derives the exact majorant, a rigorous sufficient
inequality, an explicit range split, and the asymptotic non-overlap.

## 1. Strict product majorant

Put

\[
\rho=1-\epsilon,\qquad 0<\epsilon<1,
\qquad a=\epsilon K.
\]

For a strict eigenvalue below \(K^2\), the assumed lower bound implies

\[
\left(\frac{n\pi}{\epsilon}\right)^2+\ell(\ell+1)<K^2.
\]

The radial indices therefore satisfy

\[
n\pi<a.
\]

For \(a>0\), define the strict radial count

\[
N=\#\{n\ge1:n\pi<a\}
=\left\lceil\frac a\pi\right\rceil-1.
\]

At a wall \(a=m\pi\), this gives \(N=m-1\), so the radial level equal to
the spectral endpoint is correctly excluded.

For \(1\le n\le N\), set

\[
b_n=\sqrt{a^2-n^2\pi^2}>0,
\qquad
T_n=\frac{b_n}{\epsilon}.
\]

The allowed angular momenta are exactly those with

\[
\ell(\ell+1)<T_n^2.
\]

Solving the quadratic inequality and preserving equality at an angular
wall gives the exact number of allowed nonnegative integers:

\[
\begin{aligned}
M_n
&=\#\{\ell\in\mathbb N_0:\ell(\ell+1)<T_n^2\}\\
&=
\left\lceil
\sqrt{T_n^2+\frac14}-\frac12
\right\rceil.
\end{aligned}
\]

This ceiling is important. If

\[
T_n^2=p(p+1)
\]

for an integer \(p\), then the allowed values are
\(\ell=0,\ldots,p-1\), so \(M_n=p\), exactly as the ceiling formula
states.

Since

\[
\sum_{\ell=0}^{M-1}(2\ell+1)=M^2,
\]

the separated operator estimate gives the multiplicity majorant

\[
\boxed{
N_D(A_{1-\epsilon,1},K^2)
\le
\mathcal P_\epsilon(a)
:=\sum_{n=1}^{N}M_n^2.
}
\]

If \(0\le a\le\pi\), then \(N=0\) and
\(\mathcal P_\epsilon(a)=0\). In particular the equality wall
\(a=\pi\) is part of the exact zero region under strict spectral
counting.

## 2. Exact angular estimate from \(\ell(\ell+1)\)

For \(T>0\), write

\[
\alpha(T)=\sqrt{T^2+\frac14}-\frac12,
\qquad M(T)=\lceil\alpha(T)\rceil.
\]

The top included angular momentum is \(M-1\), hence

\[
(M-1)M<T^2.
\]

Consequently

\[
M^2<T^2+M
<T^2+\sqrt{T^2+\frac14}+\frac12
<T^2+T+1.
\]

There is also a matching lower estimate. Since

\[
M\ge\alpha(T)\ge T-\frac12,
\]

and the assertion is trivial when \(T\le1\),

\[
M^2\ge T^2-T
\qquad(T\ge0).
\]

Thus the exact centrifugal count satisfies the useful two-sided bound

\[
\boxed{
T^2-T\le M(T)^2<T^2+T+1.
}
\]

This is twice as sharp in its linear term as the loose replacement

\[
M^2<(T+1)^2=T^2+2T+1.
\]

The improvement matters for a finite explicit range, though it will be
lower order at the eventual obstruction scale.

Define

\[
S_0(a)=\sum_{n=1}^{N}b_n^2,
\qquad
B(a)=\sum_{n=1}^{N}b_n.
\]

Summing the angular estimate gives

\[
\boxed{
\frac{S_0(a)}{\epsilon^2}
-\frac{B(a)}{\epsilon}
\le\mathcal P_\epsilon(a)
<
\frac{S_0(a)}{\epsilon^2}
+\frac{B(a)}{\epsilon}+N.
}
\tag{2.1}
\]

No shifted square \((T_n+1)^2\) is used.

## 3. Exact radial quadratic sum and its lattice margin

The quadratic part is elementary:

\[
S_0(a)
=Na^2-\frac{\pi^2N(N+1)(2N+1)}6.
\]

Its continuum comparison is

\[
I(a)
:=\int_0^{a/\pi}(a^2-\pi^2x^2)\,dx
=\frac{2a^3}{3\pi}.
\]

Let

\[
D(a)=I(a)-S_0(a).
\]

To encode strict radial endpoints, write

\[
\frac a\pi=N+t,
\qquad 0<t\le1.
\]

At \(a=m\pi\), the convention is \(N=m-1\), \(t=1\), not
\(N=m\), \(t=0\). Direct expansion yields the exact margin

\[
\boxed{
D(a)=\pi^2
\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
}
\tag{3.1}
\]

Equivalently,

\[
\begin{aligned}
D(a)
={}&\frac{a^2}{2}
+\pi a\left(t^2-t+\frac16\right)\\
&+\pi^2
\left(\frac{t^2}{2}-\frac{t^3}{3}-\frac t6\right).
\end{aligned}
\tag{3.2}
\]

In particular,

\[
D(a)=\frac{a^2}{2}+O(a)
\qquad(a\to\infty),
\tag{3.3}
\]

uniformly in the strict remainder \(t\).

The formula is continuous at every radial wall: the new summand in
\(S_0\) enters with value zero. Between walls,

\[
D'(a)
=\frac{2a^2}{\pi}-2Na
=2at>0.
\]

Therefore

\[
D(a)\ge D(\pi)=\frac{2\pi^2}{3}
\qquad(a\ge\pi).
\tag{3.4}
\]

Two further elementary bounds will be useful. Since
\(N\ge a/\pi-1\),

\[
D(a)\ge\frac{\pi^2N^2}{2}
\ge\frac{(a-\pi)^2}{2}.
\tag{3.5}
\]

Also \(x\mapsto\sqrt{a^2-\pi^2x^2}\) is decreasing, so a left-rectangle
comparison gives

\[
\begin{aligned}
B(a)
&\le
\int_0^{a/\pi}\sqrt{a^2-\pi^2x^2}\,dx\\
&=\frac{a^2}{4}.
\end{aligned}
\tag{3.6}
\]

This is the quarter-disk integral. Finally,

\[
N\le\frac a\pi.
\tag{3.7}
\]

## 4. Comparison with the exact shell Weyl term

The three-dimensional shell Weyl term is

\[
\begin{aligned}
W_\epsilon(a)
&=\frac{2}{9\pi}
\left(1-(1-\epsilon)^3\right)K^3\\
&=
\frac{I(a)}{\epsilon^2}
\left(1-\epsilon+\frac{\epsilon^2}{3}\right).
\end{aligned}
\tag{4.1}
\]

Using the upper half of (2.1) and \(S_0=I-D\), it is enough that

\[
I-D+\epsilon B+\epsilon^2N
\le
I\left(1-\epsilon+\frac{\epsilon^2}{3}\right).
\]

The exact sufficient condition is therefore

\[
\boxed{
D(a)\ge
\epsilon\bigl(I(a)+B(a)\bigr)
+\epsilon^2
\left(N-\frac{I(a)}3\right).
}
\tag{4.2}
\]

A simpler, slightly stronger condition follows from
(3.6)--(3.7):

\[
\boxed{
D(a)\ge
\epsilon\left(\frac{2a^3}{3\pi}+\frac{a^2}{4}\right)
+\frac{\epsilon^2a}{\pi}.
}
\tag{4.3}
\]

This is a fully explicit analytic test. The left side is the exact
strict radial lattice margin (3.1); no numerical spectral information
is involved.

## 5. An explicit thin-shell range

Here is one convenient concrete split. Assume

\[
0<\epsilon\le\frac1{100}.
\]

### 5.1. Zero and near-first-mode range

For \(0\le a\le\pi\), the strict product count is zero.

For

\[
\pi<a\le4\pi,
\]

monotonicity (3.4) gives

\[
D(a)\ge\frac{2\pi^2}{3}.
\]

The right side of (4.3) is increasing in \(a\), and at \(a=4\pi\)
it is at most

\[
\frac1{100}\left(
\frac{128\pi^2}{3}+4\pi^2
\right)
+\frac{4}{10000}
=\frac{7\pi^2}{15}+\frac1{2500}
<\frac{2\pi^2}{3}.
\]

Hence (4.3) holds throughout this interval.

In particular, the boundary layer just above \(a=\pi\) causes no
problem. More explicitly, for

\[
\pi<a\le2\pi
\]

there is exactly one radial index,

\[
N=1,\qquad
S_0=a^2-\pi^2,
\]

and

\[
M_1
=
\left\lceil
\sqrt{\frac{a^2-\pi^2}{\epsilon^2}+\frac14}
-\frac12
\right\rceil.
\]

At \(a=\pi\) this mode is absent, while immediately above the wall it
is included with the exact angular ceiling. The margin \(D\) tends to
\(2\pi^2/3\), so it remains macroscopic even if
\(a-\pi\) tends to zero with \(\epsilon\).

### 5.2. Larger product range

Now suppose

\[
4\pi\le a\le\frac{\pi}{4\epsilon}.
\]

By (3.5),

\[
D(a)\ge\frac{(a-\pi)^2}{2}
\ge\frac{9a^2}{32}.
\]

After division by \(a^2\), the right side of (4.3) is at most

\[
\frac{2\epsilon a}{3\pi}
+\frac{\epsilon}{4}
+\frac{\epsilon^2}{\pi a}
\le
\frac16+\frac1{400}
+\frac1{40000\pi^2}
<\frac9{32}.
\]

Thus (4.3) holds here as well.

Combining the subranges proves the explicit statement

\[
\boxed{
0<\epsilon\le\frac1{100},
\quad
0\le a\le\frac{\pi}{4\epsilon}
\quad\Longrightarrow\quad
\mathcal P_\epsilon(a)\le W_\epsilon(a).
}
\tag{5.1}
\]

Equivalently, the separated operator bound proves the shell Weyl
inequality in this regime for

\[
K\le\frac{\pi}{4\epsilon^2}.
\]

The constants \(1/100\) and \(\pi/4\) are deliberately simple rather
than optimized.

## 6. Sharp scale of this product method

The preceding explicit constant can be pushed much farther. The exact
large-\(a\) behavior also shows where the method must stop.

From (2.1),

\[
\left|
\epsilon^2\mathcal P_\epsilon(a)-S_0(a)
\right|
\le\epsilon B(a)+\epsilon^2N.
\tag{6.1}
\]

Fix \(c>0\) and take

\[
a=\frac c\epsilon.
\]

Then (3.2), (3.6), and (3.7) give

\[
\begin{aligned}
D(a)
&=\frac{c^2}{2\epsilon^2}+O(\epsilon^{-1}),\\
\epsilon B(a)+\epsilon^2N
&=O(\epsilon^{-1}),\\
I(a)
&=\frac{2c^3}{3\pi\epsilon^3}.
\end{aligned}
\]

Since

\[
\epsilon^2W_\epsilon(a)
=I(a)\left(1-\epsilon+\frac{\epsilon^2}{3}\right),
\]

equation (6.1) gives

\[
\boxed{
\epsilon^2
\left(\mathcal P_\epsilon(a)-W_\epsilon(a)\right)
=
\frac1{\epsilon^2}
\left(
\frac{2c^3}{3\pi}-\frac{c^2}{2}
\right)
+O(\epsilon^{-1}).
}
\tag{6.2}
\]

The leading coefficient changes sign exactly at

\[
\boxed{c_*=\frac{3\pi}{4}.}
\]

Consequences:

- For every \(c<3\pi/4\), condition (4.3), combined with a compact
  \(a\)-interval argument, proves
  \(\mathcal P_\epsilon(a)\le W_\epsilon(a)\) uniformly for
  \(a\le c/\epsilon\) once \(\epsilon\) is sufficiently small.
- For every \(c>3\pi/4\),
  \[
  \mathcal P_\epsilon(c/\epsilon)>W_\epsilon(c/\epsilon)
  \]
  for all sufficiently small \(\epsilon\).

The second statement concerns the product majorant, not the true shell
count. It proves that no rearrangement or Euler--Maclaurin sharpening
of this same majorant can establish the desired inequality throughout
the larger-\(a\) region.

The exact angular ceiling only contributes the error

\[
O\left(\frac{B(a)}{\epsilon}+N\right).
\]

At \(a=c/\epsilon\), this is \(O(\epsilon^{-3})\), whereas the
competition between the shell-volume correction and the radial lattice
margin is \(O(\epsilon^{-4})\). Hence even a perfect treatment of the
angular fractional parts cannot move the leading transition
\(3\pi/(4\epsilon)\).

## 7. Comparison with the fixed-\(\rho\) threshold

For the existing fixed-\(\rho\) theorem, write its auxiliary constant
as

\[
A_\rho=\frac{2\pi\rho}{1-\rho}
\]

to avoid confusing it with the optical width \(a=\epsilon K\). Its
threshold is

\[
K_0(\rho)
=
\left(
\frac{\sqrt{A_\rho}
+\sqrt{A_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
\]

where, for \(\rho=1-\epsilon>1/2\),

\[
\eta_\rho
=G_1(1-\epsilon)
=\frac1\pi
\left[
\sqrt{2\epsilon-\epsilon^2}
-(1-\epsilon)\arccos(1-\epsilon)
\right].
\]

As \(\epsilon\downarrow0\),

\[
\eta_{1-\epsilon}
=\frac{2\sqrt2}{3\pi}\epsilon^{3/2}
\left(1+\frac{\epsilon}{20}+O(\epsilon^2)\right),
\]

and

\[
A_{1-\epsilon}
=\frac{2\pi(1-\epsilon)}{\epsilon}.
\]

Because

\[
\frac{4\eta_\rho C_0}{A_\rho}
=O(\epsilon^{5/2}),
\]

the positive-root formula gives

\[
K_0(1-\epsilon)
=\frac{A_{1-\epsilon}}{\eta_{1-\epsilon}^2}
\left(1+O(\epsilon^{5/2})\right)
=\frac{9\pi^3}{4}\epsilon^{-4}
\left(1+O(\epsilon)\right).
\]

In the optical-width variable, the high-energy theorem therefore starts
at

\[
\boxed{
a_{\mathrm{high}}(\epsilon)
:=\epsilon K_0(1-\epsilon)
=\frac{9\pi^3}{4}\epsilon^{-3}
\left(1+O(\epsilon)\right).
}
\tag{7.1}
\]

By contrast, the maximal leading scale accessible to the product
majorant is

\[
a_{\mathrm{prod}}(\epsilon)
\sim\frac{3\pi}{4}\epsilon^{-1}.
\tag{7.2}
\]

Their ratio is

\[
\frac{a_{\mathrm{high}}}{a_{\mathrm{prod}}}
\sim3\pi^2\epsilon^{-2}\longrightarrow\infty.
\]

Thus the natural four-way split is

\[
\begin{array}{c|c}
\text{optical-width range}&\text{available conclusion}\\
\hline
0\le a\le\pi&\text{exact strict zero count}\\
\pi<a\lesssim(3\pi/4)\epsilon^{-1}
&\text{product majorant can prove the Weyl bound}\\
(3\pi/4)\epsilon^{-1}\lesssim a<
\epsilon K_0(1-\epsilon)
&\text{not covered by either argument}\\
a\ge\epsilon K_0(1-\epsilon)
&\text{existing fixed-\(\rho\) theorem}
\end{array}
\]

There is no overlap. In fact the product majorant is already on the
wrong side of the Weyl term long before the existing \(K_0\) range.

## 8. What would be needed to bridge the gap

The leading product sum corresponds to replacing

\[
\frac{\ell(\ell+1)}{r^2}
\]

by

\[
\ell(\ell+1),
\]

its minimum at the outer boundary. This produces a cylindrical
cross-section factor \(1\). The shell Weyl term instead contains

\[
\frac1\epsilon\int_{1-\epsilon}^1r^2\,dr
=1-\epsilon+\frac{\epsilon^2}{3}.
\]

That relative \(O(\epsilon)\) discrepancy is exactly the term
\(\epsilon I(a)\) in (4.2), and it dominates the lattice margin once
\(\epsilon a\) exceeds \(3\pi/4\).

An approach capable of overlapping the current high-energy theorem must
therefore retain radial information in the centrifugal potential. At a
semiclassical level, a replacement

\[
\ell(\ell+1)
\longmapsto
c_\epsilon\,\ell(\ell+1)
\]

would need

\[
c_\epsilon^{-1}
\approx1-\epsilon+\frac{\epsilon^2}{3},
\qquad
c_\epsilon=1+\epsilon+O(\epsilon^2).
\]

A uniform pointwise potential bound cannot supply this, because
\(\min r^{-2}=1\). Possible refinements would have to couple radial
kinetic energy and angular momentum, for example through:

- a joint one-dimensional comparison retaining \(r^{-2}\);
- radial sublayer bracketing with different angular coefficients;
- an averaged lower bound for \(r^{-2}\) paid for by radial kinetic
  energy;
- or a substantially improved fixed-\(\rho\) threshold.

The exact \(\ell(\ell+1)\) ceiling is worthwhile and gives the clean
finite range (5.1), but the missing average-radius correction is the
first-order obstruction to completing the thin-shell window from the
stated product bound alone.
