# Source Card: Uniform Bessel Phase and Zero Enclosures

Status: audited on 2026-07-12. The source statements below are verified; they do **not** by themselves prove the shell theorem.

## Primary source

N. Filonov, M. Levitin, I. Polterovich, and D. A. Sher, “Uniform enclosures for the phase and zeros of Bessel functions and their derivatives,” *SIAM Journal on Mathematical Analysis* **56** (2024), no. 6, 7644–7682.

- DOI: [10.1137/24M1642032](https://doi.org/10.1137/24M1642032)
- Open preprint: [arXiv:2402.06956v3](https://arxiv.org/abs/2402.06956)
- Version audited: v3, 1 November 2024.

Authoritative supporting formulas are in the [NIST DLMF, §10.18](https://dlmf.nist.gov/10.18) and [Nicholson’s integral, DLMF 10.9.30](https://dlmf.nist.gov/10.9.E30).

## Phase and branch convention

For real order $\nu\ge0$ and $x>0$, define

$$
M_\nu(x)=\sqrt{J_\nu(x)^2+Y_\nu(x)^2}>0,
$$

and choose the continuous phase $\theta_\nu$ by

$$
J_\nu(x)+iY_\nu(x)=M_\nu(x)e^{i\theta_\nu(x)},
\qquad
\lim_{x\to0+}\theta_\nu(x)=-\frac{\pi}{2}.
$$

This is FLPS (2024), §1.1, and DLMF 10.18.1–10.18.4. It fixes the additive multiple of $2\pi$ and must be retained when phases are subtracted.

For $C_{\nu,\tau}(x)=J_\nu(x)\cos(\pi\tau)+Y_\nu(x)\sin(\pi\tau)$, $\tau\in(0,1]$,

$$
C_{\nu,\tau}(x)=M_\nu(x)\cos(\theta_\nu(x)-\pi\tau).
$$

FLPS equation (1.3) then locates its $k$th positive zero by the inverse phase, with the first-zero qualification recorded in Corollary 1.6(iii).

## Derivative and monotonicity

DLMF 10.18.8 and FLPS Lemma 2.3 give

$$
\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}>0,
\qquad x>0, \nu\ge0.
$$

The sign follows from the standard Wronskian

$$
W\{J_\nu,Y_\nu\}=J_\nu Y_\nu'-J_\nu'Y_\nu=\frac{2}{\pi x}.
$$

Nicholson’s integral states

$$
M_\nu(x)^2
=\frac{8}{\pi^2}\int_0^\infty
\cosh(2\nu t)K_0(2x\sinh t)\,dt.
$$

For real $\nu\ge0$ and $x>0$, $K_0$ is positive and strictly decreasing. Hence $M_\nu(x)^2$ is strictly decreasing in $x$. This is the argument used explicitly in FLPS annuli, Lemma 4.1.

Consequently, for $0<\rho<1$,

$$
\Psi_{\nu,\rho}'(k)
=\theta_\nu'(k)-\rho\theta_\nu'(\rho k)
=\frac{2}{\pi k}
\left(\frac1{M_\nu(k)^2}-\frac1{M_\nu(\rho k)^2}\right)>0.
$$

Together with the branch condition and the large-$x$ phase expansion, this gives

$$
\Psi_{\nu,\rho}(0+)=0,
\qquad
\Psi_{\nu,\rho}(k)=(1-\rho)k+O(k^{-1})\to\infty.
$$

## Explicit uniform phase enclosure

For $x>\nu\ge0$, set

$$
U_\nu(x)
=\sqrt{x^2-\nu^2}-\nu\arccos\!\left(\frac{\nu}{x}\right)-\frac{\pi}{4},
$$

$$
L_\nu^{\rm raw}(x)
=U_\nu(x)-\frac{3x^2+2\nu^2}{24(x^2-\nu^2)^{3/2}},
\qquad
L_\nu(x)=\max\left\{L_\nu^{\rm raw}(x),-\frac{\pi}{2}\right\}.
$$

FLPS Theorem 1.4 states the strict enclosure

$$
L_\nu(x)<\theta_\nu(x)<U_\nu(x)
\qquad (x>\nu\ge0).
$$

It is uniform in nonnegative real order and argument in this domain. Corollaries 1.6 and 1.7 convert it into inverse-function zero enclosures and Bessel-zero counting bounds. The first zero of a general cylinder function has the exception described in Corollary 1.6(iii); the $J_\nu$ and $Y_\nu$ cases themselves are covered for every positive zero.

## Turning-point interpretation and limitation

Theorem 1.4 remains valid arbitrarily close to $x=\nu$ from the oscillatory side, but it is not an Airy-scale expansion with a bounded explicit remainder in the variable $(x-\nu)/\nu^{1/3}$. Its raw lower correction diverges as $x\downarrow\nu$ and is replaced by the cap $-\pi/2$.

Therefore this paper alone does **not** provide the proposed shell lemma in the form “Airy approximation plus explicit signed error on both sides of $x=\nu$.” Classical Debye–Olver or Airy asymptotics with unspecified $O(\cdot)$ constants must not be treated as certified one-sided enclosures.

## Can the phase bounds be differenced?

When both $k>\nu$ and $\rho k>\nu$, logically safe subtraction gives

$$
L_\nu(k)-U_\nu(\rho k)
<\Psi_{\nu,\rho}(k)
<U_\nu(k)-L_\nu(\rho k).
$$

This is valid, but its width is the sum of the two enclosure widths; no cancellation may be assumed. Near $\rho k\sim\nu$, independently subtracting the two bounds can lose the margin needed for lattice counting.

The sharper and globally organized result is FLPS annuli (2026), Theorem 5.1 and Lemma 5.2, audited separately in `sources/annuli_polya.md`. Those statements extend the elementary bounds to $x\le\nu$ and package the subtraction with explicit constants.

## Applicability to three-dimensional shells

- All definitions and Theorem 1.4 allow real $\nu\ge0$, so half-integer orders $\nu=\ell+\tfrac12$ are included.
- The modulus positivity, phase derivative, Nicholson monotonicity, and safe-differencing logic transfer without a dimension restriction.
- These sources control special-function phases; they do not address the $3$D spherical-harmonic weight $2\ell+1$.
- No result here certifies a finite shell eigenvalue window.

## Audit conclusion

The phase convention, derivative identity, modulus monotonicity, and uniform oscillatory-side enclosure are verified external dependencies. The source also exposes an important limitation: a separate explicit Airy lemma is unnecessary only if the global annulus phase-difference bound supplies enough margin for the new weighted lattice argument. That implication must be checked at the lattice stage rather than assumed.
