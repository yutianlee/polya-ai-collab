# Lemma Packet: Imported Global Shell Phase Enclosure

Obligation: `SHELL-phase-enclosures`

## Exact statement to verify

Fix

$$
0<\rho<1,\qquad \nu\ge0,
$$

and regard $K>0$ as the variable in item 1. For items 2–6, additionally assume

$$
\ell\in\mathbb N_0,\qquad
\nu=\ell+\frac12\le K,\qquad \mu=\rho K.
$$

Use the branch

$$
J_\nu(x)+iY_\nu(x)=M_\nu(x)e^{i\theta_\nu(x)},
\qquad \theta_\nu(0+)=-\frac\pi2,
$$

and define

$$
\Psi_{\nu,\rho}(K)=\theta_\nu(K)-\theta_\nu(\rho K),
\qquad
\gamma_{K,\mu}(\nu)=\frac1\pi\Psi_{\nu,\rho}(K).
$$

With $G$, $F$, $H$, and $\Phi$ exactly as defined in `sources/annuli_polya.md`, prove:

1. $\Psi_{\nu,\rho}$ is strictly increasing in $K$, tends to zero as $K\to0+$, and tends to infinity as $K\to\infty$.
2. Globally for $0\le\nu\le K$,

$$
0<\gamma_{K,\mu}(\nu)
<G_K(\nu)-F_\mu(\nu)
\le G_K(\nu)+\frac14.
$$

3. If $\nu\le\mu$, including equality, then

$$
\Phi_{K,\mu}(\nu)
<\gamma_{K,\mu}(\nu)
<\Phi_{K,\mu}(\nu)+\frac14.
$$

4. On $\mu<\nu\le K$, assert only the global one-sided bound in item 2; do not extend item 3.
5. For the repository determinant

$$
F_{\nu,\rho}(K)
=J_\nu(\rho K)Y_\nu(K)-Y_\nu(\rho K)J_\nu(K),
$$

verify its sign relative to the annulus convention and prove that its positive zeros are exactly the levels $\Psi_{\nu,\rho}(K)\in\pi\mathbb N$.
6. Under strict counting, the radial count below $K$ is

$$
\#\{n\ge1:n\pi<\Psi_{\nu,\rho}(K)\};
$$

do not replace this by an exact floor at phase endpoints.

## Permitted dependencies

- `CONV-strict-counting`
- `SRC-bessel-phase`
- `SRC-annuli`
- `SHELL-exact-phase-rep`
- `SHELL-phase-monotonicity`
- `sources/bessel_phase_enclosures.md`
- `sources/annuli_polya.md`

No incumbent proof or previous review may be used by the clean-room solver.

## Falsification cases

- $\nu=\rho K$ exactly;
- mixed region $\rho K<\nu\le K$;
- $\nu=K$;
- $K$ equal to a cross-product zero;
- determinant sign reversal between repository and annulus conventions;
- $\rho\to1$, where the main phase difference shrinks but the $1/4$ allowance does not;
- accidental use of the divergent $H_\mu$ correction at $\nu=\mu$.

## Scope

This lemma supplies a rigorous phase enclosure. It does not assert that the $+1/4$ slack is small enough after summation with weight $2\ell+1$, and it does not prove the shell theorem.
