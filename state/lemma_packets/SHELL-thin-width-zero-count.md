# Lemma Packet: Exact Zero Count for Spectrally Thin Shells

Proposed obligation: `SHELL-thin-width-zero-count`

## Statement

Fix $0<\rho<1$ and $K>0$. For every half-integer order

$$
\nu=\ell+\frac12,\qquad \ell\in\mathbb N_0,
$$

prove

$$
0<\Psi_{\nu,\rho}(K)
=\theta_\nu(K)-\theta_\nu(\rho K)
\le(1-\rho)K.
$$

Consequently, if

$$
(1-\rho)K\le\pi,
$$

then

$$
\#\{n\ge1:n\pi<\Psi_{\nu,\rho}(K)\}=0
$$

for every $\ell$. Under the separated shell count, this gives

$$
N_D(A_{\rho,1},K^2)=0.
$$

At equality, the $\ell=0$ phase is exactly $\pi$ and the strict endpoint is not counted.

## Permitted dependencies

- `CONV-strict-counting`
- `SRC-bessel-phase`
- `SHELL-exact-phase-rep`
- `SHELL-phase-monotonicity`
- `sources/bessel_phase_enclosures.md`

## Required proof steps

1. Use Nicholson's representation

$$
M_\nu(x)^2=\frac8{\pi^2}\int_0^\infty
\cosh(2\nu t)K_0(2x\sinh t)\,dt.
$$

2. For $\nu\ge1/2$, use positivity of $K_0$ and

$$
\cosh(2\nu t)\ge\cosh t
$$

to obtain $M_\nu(x)^2\ge M_{1/2}(x)^2$.
3. Reconstruct from the elementary half-order formulas that

$$
M_{1/2}(x)^2=\frac{2}{\pi x}.
$$

4. Combine this with

$$
\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}
$$

to prove $0<\theta_\nu'(x)\le1$.
5. Integrate from $\rho K$ to $K$ and apply the strict phase-level count.

## Falsification cases

- $\nu=1/2$, where equality $\theta_{1/2}'=1$ holds;
- $(1-\rho)K=\pi$, where the first phase level is an excluded endpoint;
- orders $0\le\nu<1/2$, for which the comparison direction is not asserted;
- accidental replacement of strict $n\pi<\Psi$ by $n\pi\le\Psi$;
- any claim that this proves the entire $\rho\to1$ endpoint regime when $(1-\rho)K>\pi$.
