# General dimension \(d\ge 3\): round 02

Date: 18 July 2026  
Primary strategy: `human/inbox/general-d_1.md`  
Status: the one-interface theorem and every fixed-ratio high-energy tail are proved; the arbitrary inner multi-cell tail remains open.

## 1. What is now proved

The exact dimension lift from round 01 is unchanged:

\[
 W_d-P_d^{<}
 =\mathcal B_d(A)+\sum_{m\ge0}c_{d,m}D_A(r_m),
 \qquad \mathcal B_d(A)\ge0.
\]

Thus the only analytic target is the dimension-free shifted-tail inequality

\[
 D_A(r)=2\int_r^K A(z)\,dz-T_A(r)\ge0,
 \qquad r\in\tfrac12\mathbb N.
\]

This round closes two substantial sectors of that target.

### One-interface tails

The shifted-tail inequality holds whenever

\[
 0<\mu-r<1,
\]

and also at \(r=\mu\).  The formerly unresolved residual is reduced to a
finite family

\[
 r\in\left\{\tfrac12,1,\tfrac32,2,\tfrac52,3,
 \tfrac72,4,\tfrac92\right\},\qquad K<1/\omega_0,
\]

and is certified by exact rational inequalities.  In the positive-count
cases the ball reserve satisfies

\[
 E_r(K)>\frac3{20}\quad(r\le4),
 \qquad
 E_{9/2}(K)>\frac{1253}{555}.
\]

The proof uses eleven rigorously bracketed later-sample walls, exact Taylor
envelopes for \(\arcsin\) and \(\sqrt{1-x^2}\), and rational bounds for
\(\pi\).  The standalone replay

`scripts/general_d_finite_wall_fraction_verify.py`

passes 628 exact integer/Fraction checks.  The independent
`scripts/general_d_wall_verify.py` audit also passes at 512-bit Arb
precision.

### Fixed-ratio high-energy tails

For every fixed \(0<\rho<1\), define

\[
 \eta_\rho=G_1\!\left(\max\{\rho,\tfrac12\}\right),
 \qquad a_\rho=\frac{2\pi\rho}{1-\rho},
 \qquad C_*=\frac12+\frac{8\sqrt2}{15},
\]

and

\[
 K_0(\rho)=
 \frac{a_\rho+2\eta_\rho C_*
 +\sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}}
 {2\eta_\rho^2}.
\]

Then every shifted tail is proved for \(K\ge K_0(\rho)\).  The proof
couples:

1. the quantitative concave trapezoidal-floor gain on the inner head;
2. the sharpened first-shelf estimate
   \[
   p<\sqrt{r^2+a_\rho K}-r
   \le\sqrt{a_\rho K+\tfrac14}-\tfrac12;
   \]
3. the quantitative convex reserve in the outer ball suffix; and
4. the uniform interface-cap bound \(\delta<2\sqrt2/15\).

There is also a uniform small-hole sector:

\[
 0<\rho<\omega_0,
 \qquad
 K(\omega_0-\rho)\ge\frac12+\frac{8\sqrt2}{15}.
\]

## 2. Exact remaining obstruction

Let

\[
 n=\lfloor\mu-r\rfloor,
 \qquad q=r+n,
 \qquad d_\rho=\frac{2\arcsin\rho}{\pi},
\]

and let \(p\) be the last index on the first ordinary-floor shelf of
\(A(r+j)+1/4\).  A wall-safe first-shelf reduction gives

\[
 D_A(r)\ge
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p),
\]

where

\[
 R_p=2\int_r^{r+p}A(z)\,dz-2pF_0
 =C_p+p(\varepsilon_0+\varepsilon_p-\tfrac12),
\]

and

\[
 C_p=-\int_0^p u(p-u)A''(r+u)\,du\ge0.
\]

Hence the precise scalar still to prove is

\[
 \boxed{
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\ge0.}
\]

The terminal term \(D_A(q)\) is a one-interface tail and is now known to
be nonnegative, but examples from round 01 show that mere nonnegativity is
not enough: the first inner shelf can borrow a strictly positive amount
from the terminal convex reserve.  The next round is devoted to a
quantitative coupling of exactly these two terms.

## 3. Artifacts and verification

The separate general-dimensional paper is

`manuscript/spherical-shell-polya-general-d.tex`.

Its verified 16-page PDF is

`output/pdf/spherical-shell-polya-general-d.pdf`.

All pages were rendered and visually inspected.  Text extraction reports
no unresolved references or undefined markers.  The original \(d=3\)
paper was not overwritten.

