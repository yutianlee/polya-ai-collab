# Independent Audit: Real-Order Annulus Phase Bounds for 3D Shells

Date: 2026-07-12

## Question

Do the published Bessel-phase and annulus estimates apply to the shell orders

$$
\nu=\ell+\frac12
$$

and provide a rigorous one-sided enclosure through the inner transition $\rho k\sim\nu$?

## Sources independently checked

1. Filonov–Levitin–Polterovich–Sher, *Uniform enclosures for the phase and zeros of Bessel functions and their derivatives*, SIAM J. Math. Anal. 56 (2024), Theorem 1.4.
2. Filonov–Levitin–Polterovich–Sher, *Pólya’s conjecture for Dirichlet eigenvalues of annuli*, JLMS 113 (2026), Lemma 4.1, Theorem 5.1, and Lemma 5.2.
3. DLMF 10.5.2, 10.18.8, and 10.9.30.
4. Guo–Jiang–Wang–Yang, *Bessel functions and Weyl’s law for balls and spherical shells*, Lemma 2.3, Corollary 2.16, and Theorem 2.20.

Two independent audits and a direct extraction of the published/preprint texts agreed on the formulas and scope below.

## Verified transfer

Use the phase branch

$$
J_\nu(x)+iY_\nu(x)=M_\nu(x)e^{i\theta_\nu(x)},
\qquad \theta_\nu(0+)=-\frac\pi2.
$$

For every real $\nu\ge0$, Nicholson’s formula makes $M_\nu^2$ strictly decreasing, and therefore

$$
\Psi_{\nu,\rho}'(k)
=\frac{2}{\pi k}
\left(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2}\right)>0.
$$

FLPS annuli Lemma 5.2 is stated for real $0\le z\le\lambda$. Substitution

$$
(\lambda,\mu,z)=(k,\rho k,\nu)
$$

is therefore valid for half-integer order. Globally, for $0\le\nu\le k$,

$$
\frac{\Psi_{\nu,\rho}(k)}\pi
<G_k(\nu)-F_{\rho k}(\nu)
\le G_k(\nu)+\frac14.
$$

When $\nu\le\rho k$, including equality at the inner turning interface,

$$
G_k(\nu)-G_{\rho k}(\nu)
<\frac{\Psi_{\nu,\rho}(k)}\pi
<G_k(\nu)-G_{\rho k}(\nu)+\frac14.
$$

On the mixed evanescent side $\rho k<\nu\le k$, only the global one-sided bound is imported; the sharper correlated two-sided estimate does not apply.

## Sign and endpoint checks

- The repository determinant is the negative of the annulus paper’s determinant. Their zero sets agree, but the displayed sine factor changes sign.
- The phase branch is $-\pi/2$ at zero; only the phase difference tends to zero.
- The annulus paper uses a non-strict spectral count. The project’s strict count must remain

$$
\#\{n\ge1:n\pi<\Psi_{\nu,\rho}(K)\}
$$

at spectral endpoints.
- The $H_{\rho k}$ correction diverges at $\nu=\rho k$. The uniform $+1/4$ statement, not a naive $H$ subtraction, is the valid interface bound.

## What remains open

The transfer is a special-function result only. It does not show that the additive $1/4$ normalized phase slack survives summation with multiplicity $2\ell+1$. It may also be too coarse as $\rho\to1$.

Guo–Jiang–Wang–Yang provide Airy-profile asymptotics on both sides of the transition, but their $O(\cdot)$ constants and sufficiently-large thresholds are not explicit enough for certification. A new explicit Airy enclosure should be commissioned only if the weighted lattice calculation proves the FLPS $1/4$ margin insufficient.

## Verdict

The real-order annulus phase-difference lemma transfers to half-integer shell orders. The next primary analytic test is the multiplicity-weighted lattice inequality, not a new Airy derivation.
