# Lemma Packet: Uniform Small-Hole Endpoint

Obligation: `SHELL-rho-zero-endpoint`.

## Exact theorem to reconstruct

Define

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
$$

and

$$
\boxed{
\rho_*:=\frac{\omega_0}{1+2C_*}
=\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}.
}
$$

Prove, with strict spectral counting, that

$$
\boxed{
0<\rho\le\rho_*,
\qquad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

The endpoint $\rho=\rho_*$ must be included. No limiting argument at
$\rho=0$ is permitted or needed.

## Definitions

For

$$
\mu=\rho K,
\qquad
G_a(z)=\frac1\pi
\left(\sqrt{a^2-z^2}-z\arccos\frac za\right)
\quad(0\le z\le a),
$$

with $G_a(z)=0$ for $z>a$, and put

$$
A_{\rho,K}(z)=G_K(z)-G_\mu(z),
\qquad
\nu_\ell=\ell+\frac12,
$$

and define the coarse ordinary-floor proxy

$$
S_{\rho,K}
=\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor.
\tag{2}
$$

For each $r\ge0$, let $x_r=r+1/2$ and

$$
\mathcal T_r
=\left\lfloor A_{\rho,K}(x_r)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A_{\rho,K}(x_r+j)+\frac14\right\rfloor.
\tag{3}
$$

## Permitted proved inputs

1. **Exact spectrum and strict phase majorant.** The audited spectral bridge
   and phase enclosure give

   $$
   N_D(A_{\rho,1},K^2)\le S_{\rho,K}.
   \tag{4}
   $$

   The true phase count is strict; (2) is only the already-audited coarse
   ordinary-floor upper proxy.

2. **Multiplicity-to-tail scaffold.** The exact identity

   $$
   S_{\rho,K}=\sum_{r\ge0}\mathcal T_r
   \tag{5}
   $$

   and the implication

   $$
   \left[
   \mathcal T_r\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz
   \text{ for every }r
   \right]
   \Longrightarrow
   S_{\rho,K}\le
   \frac{2}{9\pi}(1-\rho^3)K^3
   \tag{6}
   $$

   are proved in the weighted-lattice scaffold.

3. **High-angular shifted tails.** For every start at or above the inner
   interface,

   $$
   x_r\ge\mu
   \quad\Longrightarrow\quad
   \mathcal T_r\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz.
   \tag{7}
   $$

   Equality $x_r=\mu$ is included.

4. **Audited small-hole low-interface theorem.** The proof and adversarial
   audit in `state/lemma_packets/SHELL-low-interface-small-hole.md` and
   `rounds/polya-main/round_003/reviews/low-interface-small-hole-adversarial.md`
   establish

   $$
   \left.
   \begin{array}{c}
   0<\rho<\omega_0,\\
   K(\omega_0-\rho)\ge C_*,\\
   x_r<\mu
   \end{array}
   \right\}
   \Longrightarrow
   \mathcal T_r\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz.
   \tag{8}
   $$

No pointwise convergence to the ball, Bessel-root computation, floating-point
scan, asymptotic expansion, or interval certificate may be used.

## Required reconstruction

Split only at the exact interface scale

$$
\mu=\rho K=\frac12.
$$

Show that (7) handles every tail on one side of this split. On the other side,
derive the hypotheses of (8) uniformly from $0<\rho\le\rho_*$. Verify the
identity defining $\rho_*$ exactly, including every strict/non-strict
inequality at $\rho=\rho_*$. Then invoke (5)--(6) and (4).

## Falsification cases

- $K=0$;
- $\rho=\rho_*$;
- $\mu=1/2$ exactly;
- the branch $\mu>1/2$ with $\rho=\rho_*$;
- $x_0=\mu$ and $x_0$ immediately below $\mu$;
- $K(\omega_0-\rho)=C_*$;
- true phase on an integer wall;
- $A_{\rho,K}(\nu_\ell)+1/4$ on an integer wall;
- accidental replacement of the ordinary-floor proxy by the strict phase
  count;
- an unjustified appeal to continuity of shell roots at $\rho=0$.

## Promotion rule

Promote only after an isolated clean-room reconstruction verifies (1) from
the four permitted inputs and a separate adversarial audit verifies the
constant, the two $\mu$ branches, and all endpoint conventions. If promoted,
the small-hole endpoint requires no finite Bessel certificate.
