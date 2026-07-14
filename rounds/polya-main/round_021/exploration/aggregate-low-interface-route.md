# Round 21 exploration: aggregate low-interface compensation

Status: **EXACT CONDITIONAL LEMMA; GLOBAL POSITIVITY NOT YET CERTIFIED**.

Date: 2026-07-15.

This note records a route for the high-frequency part of the prospective
Round 20 residual.  Its new point is to sum the errors of all low-interface
shifted tails before asking for a sign.  The accepted fixed-ratio proof
forces every tail to be nonpositive separately and therefore discards a
positive triangular term.  That loss is responsible for much of the large
threshold `K_0(rho)`.

The exact aggregate lemma below is analytic.  The subsequent observation
that its continuous reserve appears positive for `K>=200` is diagnostic
only and is not a theorem until an outward interval certificate and an
independent checker pass.

## 1. Authenticated inputs

| artifact | SHA-256 | use |
|---|---|---|
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` | accepted one-tail decomposition, curvature, convex-tail gain, and interface loss |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | exact dimension-reduction identity and Weyl normalization |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | accepted separated completeness, multiplicity, and strict phase-count identity |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | qualified trapezoidal-floor inequalities and the inner-interface integral bound |

No Bessel root, incumbent Round 20 proof, or floating-point spectral count
is used.

## 2. Low-tail cells

Retain the accepted notation

\[
 \mu=\rho K,
 \qquad
 \eta_\rho=G_1\!\left(\max\{\rho,1/2\}\right),
 \qquad
 d_\rho=\frac{2\arcsin\rho}{\pi},
 \tag{1}
\]

and define

\[
 \rho_c=\frac1{1+2\pi}.
\]

and put

\[
 C=\frac{2\pi\rho K}{1-\rho}.
 \tag{2}
\]

Assume `mu>1/2`.  Write

\[
 \mu-\frac12=J+\tau,
 \qquad J\in\mathbb N_0,
 \qquad 0\leq\tau<1.
 \tag{3}
\]

The low-interface tails are exactly the half-integer starting points

\[
 x_r=r+\frac12<\mu.
\]

Their number is

\[
 R=
 \begin{cases}
 J,&\tau=0,\\
 J+1,&0<\tau<1.
 \end{cases}
 \tag{4}
\]

For the accepted split

\[
 n_r=\lfloor\mu-x_r\rfloor,
 \qquad q_r=x_r+n_r,
\]

one has the exact identities

\[
 \sum_{r=0}^{R-1}n_r=\frac{J(J+1)}2,
 \qquad
 \mu-q_r=\tau
 \quad(0\leq r<R).
 \tag{5}
\]

Thus the interface loss is the same for every low tail:

\[
 \delta_\tau
 :=\int_{\mu-\tau}^{\mu}G_\mu(z)\,dz
 \leq\frac{2\tau^{5/2}}{15\sqrt\mu}.
 \tag{6}
\]

At `tau=0`, both sides of (6) are zero.

## 3. Refined shelf-length sum

For each low tail, let `p_r` be the last point of the first constant-floor
shelf, with the no-drop convention from the accepted fixed-ratio packet.
That proof gives

\[
 A(x_r)-A(x_r+p_r)<1
\]

and

\[
 A(x_r)-A(x_r+p_r)
 \geq\frac{\kappa}{2}
 \left((x_r+p_r)^2-x_r^2\right),
 \qquad
 \kappa=\frac{1-\rho}{\pi\rho K}.
\]

Consequently

\[
 p_r^2+2x_rp_r<C,
 \qquad
 \boxed{p_r<\sqrt{x_r^2+C}-x_r.}
 \tag{7}
\]

This is strictly stronger than the tailwise bound `p_r<sqrt(C)` away from
the first angular channel.

Define

\[
 P_C(x)=\sqrt{x^2+C}-x.
\]

Since

\[
 P_C''(x)=\frac{C}{(x^2+C)^{3/2}}>0,
\]

the midpoint form of Hermite--Hadamard, applied on every unit interval,
gives

\[
 \sum_{r=0}^{R-1}p_r
 <\sum_{r=0}^{R-1}P_C\!\left(r+\frac12\right)
 \leq\int_0^R P_C(x)\,dx
 =:\mathcal I(C,R),
 \tag{8}
\]

where

\[
 \boxed{
 \mathcal I(C,R)
 =\frac12\left[
 R\sqrt{R^2+C}
 +C\operatorname{arsinh}\!\left(\frac{R}{\sqrt C}\right)
 -R^2
 \right].}
 \tag{9}
\]

The first inequality in (8) is strict.

## 4. Exact aggregate compensation lemma

The accepted one-tail estimate is

\[
 \frac{\mathcal T_r}{2}
 \leq\int_{x_r}^{K}A_{\rho,K}(z)\,dz
 +\delta_\tau-\frac{M_r}{4},
 \tag{10}
\]

with

\[
 M_r=\lfloor K\eta_\rho\rfloor
 +d_\rho(n_r-p_r)-p_r.
 \tag{11}
\]

Summing (11) and using (5) yields the term that the tailwise proof drops:

\[
 \sum_{r=0}^{R-1}M_r
 =R\lfloor K\eta_\rho\rfloor
 +d_\rho\frac{J(J+1)}2
 -(1+d_\rho)\sum_{r=0}^{R-1}p_r.
 \tag{12}
\]

Combining (6), (8), and (12) first proves a strict bound for the coarse
weighted phase proxy.  The weighted-lattice packet identifies that proxy,
and the completeness packet supplies the previously conditional separated
strict-count identity.  Hence the accepted phase upper bound gives

\[
 N_D(A_{\rho,1},K^2)\leq\mathcal P_{\rm coarse}.
\]

The resulting sufficient condition is

\[
\boxed{
\begin{aligned}
 \mathcal Q(\rho,K):={}&
 R\lfloor K\eta_\rho\rfloor
 +d_\rho\frac{J(J+1)}2
 -(1+d_\rho)\mathcal I(C,R)\\
 &-\frac{8R\tau^{5/2}}{15\sqrt\mu}
 \geq0
\end{aligned}}
 \quad\Longrightarrow\quad
 \boxed{
 N_D(A_{\rho,1},K^2)
 <\frac{2}{9\pi}(1-\rho^3)K^3.}
 \tag{13}
\]

Indeed, (13) implies

\[
 \sum_{r<R}M_r>4R\delta_\tau.
\]

After summing (10), all low-tail aggregate errors are therefore strictly
negative.  Every tail with `x_r>=mu` is controlled by the already accepted
convex shifted-tail theorem.  The exact dimension-reduction identity and
integration by parts give the strict coarse-proxy comparison, and the
accepted completeness/count bridge transfers it to `N_D`.  Strictness
follows from (7)--(8), including the cell `tau=0` where the interface loss
vanishes.

Equation (13) is an aggregate theorem: no individual low tail is required
to satisfy `M_r>4 delta_tau`.

## 5. A floor-free continuous reserve

For a rectangular certificate it is convenient to remove all `mu` and
`K eta_rho` walls.  Assume `K eta_rho>1` and define

\[
 \overline R=\mu+\frac12,
 \qquad
 \overline{\mathcal I}=\mathcal I(C,\overline R).
\]

The elementary bounds

\[
 R\geq\mu-\frac12,
 \quad
 J\geq\mu-\frac32,
 \quad
 R\leq\overline R,
 \quad
 \lfloor K\eta_\rho\rfloor>K\eta_\rho-1,
 \tag{14}
\]

and monotonicity of `I(C,R)` in `R` give the continuous lower reserve

\[
\boxed{
\begin{aligned}
 \mathcal B(\rho,K):={}&
 \left(\mu-\frac12\right)(K\eta_\rho-1)
 +\frac{d_\rho}{2}
 \left(\mu-\frac32\right)
 \left(\mu-\frac12\right)\\
 &-(1+d_\rho)\overline{\mathcal I}
 -\frac{8(\mu+1/2)}{15\sqrt\mu}.
\end{aligned}}
 \tag{15}
\]

Therefore

\[
 \boxed{\mathcal B(\rho,K)\geq0}
 \quad\Longrightarrow\quad
 \boxed{\mathcal Q(\rho,K)>0}
 \quad\Longrightarrow\quad
 \boxed{\text{strict Polya at }(\rho,K).}
 \tag{16}
\]

Unlike `K_0(rho)`, the reserve (15) retains the positive triangular term
and bounds all shelf lengths collectively.

## 6. Diagnostic frontier and required certificate

Direct high-precision evaluation of (15), used only to choose a target,
gave the following approximate first persistent positive frequencies:

| `rho` | diagnostic threshold for `B>0` |
|---:|---:|
| `rho_c` | 63 |
| `1/5` | 70 |
| `3/10` | 78 |
| `2/5` | 84 |
| `1/2` | 90 |
| `3/5` | 117 |
| `13/20` | 132 |
| `39/50` | 187 |

On a dense diagnostic grid over the finite rectangle

\[
 \rho_c\leq\rho\leq\frac{39}{50},
 \qquad 200\leq K\leq2000,
\]

using 1,001 equally spaced ratio samples and every integer frequency from
200 through 2,000, the smallest displayed reserve was approximately `381.4` at
`(rho,K)=(rho_c,200)`.  This is **not** certification: no grid can establish
the signs or monotonicity between sample points, and the frequency domain is
unbounded.

The next bounded obligation is to produce two independent artifacts:

1. an outward Arb subdivision proving `B(rho,K)>0` on
   `rho_c<=rho<=39/50`, `200<=K<=K_tail`;
2. an exact analytic tail proving `B(rho,K)>0` for `K>=K_tail`, with an
   overlap at the complete face `K=K_tail`.

The checker must rederive (3)--(16), authenticate all source hashes, test
`tau=0`, half-integer `mu` walls, integer `K eta_rho` walls, `rho=1/2`,
both ratio endpoints, and the overlap face.  Until those obligations pass,
no part of the prospective residual is subtracted.

## 7. Current verdict

The aggregate compensation identity and the implications

\[
 \mathcal B\geq0\Longrightarrow\mathcal Q>0
 \Longrightarrow\text{strict Polya}
\]

are established analytically from accepted inputs.  The proposed global
positivity region `K>=200` remains an uncertified but strongly separated
target.  This route is complementary to the low-frequency product band:
if certified, it would replace the very large upper floor `K_0(rho)` by a
uniform frontier near `200`, leaving a genuinely finite middle window.
