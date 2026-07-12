# Best Proof Draft

No complete all-$K$, all-$\rho$ shell Pólya proof exists.

## Exact spectral bridge

For every fixed $0<\rho<1$, spherical-harmonic expansion followed by
$u=rR$ gives

$$
-\Delta_{A_{\rho,1}}^D
\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}
\left(
-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
\right).
$$

The exact form and operator domains are recorded in
state/lemma_packets/SHELL-sturm-liouville-completeness.md. Compactness of the
full resolvent uses the angular-tail estimate

$$
\|(L_\ell+1)^{-1}\|
\le
\frac1{1+\ell(\ell+1)}
\longrightarrow0,
$$

not merely blockwise compactness.

Each radial block has a positive simple complete spectrum. For
$\nu=\ell+\tfrac12$, its eigenfrequencies are exactly the positive simple
roots of

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)
-Y_\nu(\rho k)J_\nu(k).
$$

With the audited phase convention,

$$
\Psi_{\nu,\rho}(k)
=
\theta_\nu(k)-\theta_\nu(\rho k)
$$

is strictly increasing from zero to infinity, and the positive roots satisfy

$$
\Psi_{\nu,\rho}(k_{\ell,n})=n\pi,
\qquad n=1,2,\ldots.
$$

Thus strict counting is exactly

$$
N_D(A_{\rho,1},K^2)
=
\sum_{\ell=0}^{\infty}(2\ell+1)
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
$$

At a phase wall $\Psi(K)=m\pi$, the channel contribution is $m-1$.
Accidental equality across different $\ell$ channels is allowed and the
orthogonal multiplicities add.

## Fixed-rho high-energy theorem

For

$$
A_{\rho,K}=G_K-G_{\rho K},
$$

the multiplicity scaffold reduces the coarse proxy to shifted tails. The
Round 3 high- and low-interface estimates prove

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge K_0(\rho)),
$$

where

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
$$

$$
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
\eta_\rho=G_1\!\left(\max\{\rho,1/2\}\right),\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

The strict phase proxy is no larger. Combining it with the now-proved exact
spectral bridge gives the unconditional theorem

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\quad\text{for every fixed }0<\rho<1
\text{ and }K\ge K_0(\rho).
}
$$

Also,

$$
(1-\rho)K\le\pi
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)=0.
$$

## Uniform low-optical thin-shell theorem

Put

$$
\varepsilon=1-\rho,\qquad a=\varepsilon K.
$$

Since

$$
L_\ell
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1)
$$

on the interval of length $\varepsilon$, min--max gives

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
$$

Counting the resulting product levels with strict radial and angular walls
and the exact multiplicity sum yields

$$
\boxed{
0<\varepsilon\le\frac1{100},
\quad
0\le K\le\frac{\pi}{4\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The proof and exact lattice margin are recorded in
state/lemma_packets/SHELL-thin-product-low-optical.md.

This comparison cannot be extrapolated. Its majorant exceeds the shell Weyl
target at exact walls of order $a\asymp\varepsilon^{-1}$, including an exact
family with $\varepsilon\downarrow0$. The current high-energy theorem begins
only at

$$
\varepsilon K_0(1-\varepsilon)
\asymp
\frac{9\pi^3}{4}\varepsilon^{-3}.
$$

The two ranges therefore leave a genuine radius-sensitive intermediate gap.

## Remaining gates

This file must not be cited as a proof of the full shell theorem. The open
gates are:

- a radius-sensitive thin-shell estimate between
  $K=\pi/[4(1-\rho)^2]$ and $K_0(\rho)$ near $\rho=1$;
- a quantitative small-hole endpoint and explicit compact-$\rho$ overlap;
- interval-certified closure of the bounded residual parameter set,
  including every determinant, phase, floor, and strict spectral wall;
- a fresh final theorem-level clean-room reconstruction and adversarial
  review.
