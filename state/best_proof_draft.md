# Best Proof Draft

No complete shell Pólya proof exists.

The fixed-$\rho$ high-energy weighted lattice step is now proved. Its frozen artifacts are:

- `state/lemma_packets/SHELL-weighted-lattice-fractional.md`;
- `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md`;
- `rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md`;
- `rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md`;
- the corresponding clean-room and adversarial reviews.

For

$$
A_{\rho,K}=G_K-G_{\rho K},
$$

the multiplicity scaffold reduces the coarse proxy to shifted tails. High-angular tails are controlled directly by the convex theorem. For tails crossing the inner interface, the first constant-floor plateau on the concave head has length

$$
p<\sqrt{\frac{2\pi\rho}{1-\rho}K}.
$$

The sharpened concave theorem and the convex-tail gain then prove every low-interface tail once

$$
K\ge K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
$$

where

$$
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
\eta_\rho=G_1\!\left(\max\{\rho,1/2\}\right),\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

Consequently,

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge K_0(\rho)).
$$

The strict and optimized phase proxies are no larger.

This file must not be cited as a shell theorem proof. The remaining gates are:

- separated Sturm--Liouville completeness and the unconditional strict phase-count identity;
- a $\rho$-uniform covering, especially near $\rho\to1$, because $K_0(\rho)$ diverges;
- certified closure of the residual finite parameter region and every eigenvalue/floor wall.
