# Source Card: Bessel Functions and the Dirichlet Spectrum of a Spherical Shell

Status: the structural spectrum component was audited on 2026-07-13. A
shell-uniform Weyl remainder and the finite-window certificate remain source
audit required.

## Scope

This card separates two logically different inputs:

1. the exact separation-of-variables description of the three-dimensional
   Dirichlet shell spectrum; and
2. quantitative shell Weyl-remainder estimates.

Only the first component is discharged here. No asymptotic remainder is being
promoted by this audit.

## Authoritative special-function references

For real order and positive argument, the following NIST DLMF sections are the
special-function references used in the structural proof:

- [DLMF 10.5, Wronskians and cross-products](https://dlmf.nist.gov/10.5);
- [DLMF 10.7, limiting forms](https://dlmf.nist.gov/10.7);
- [DLMF 10.18, modulus and phase functions](https://dlmf.nist.gov/10.18).

In particular,

$$
J_\nu(x)Y_\nu'(x)-J_\nu'(x)Y_\nu(x)=\frac{2}{\pi x},
$$

so $J_\nu$ and $Y_\nu$ do not vanish simultaneously at one positive
argument. For $\nu>0$, the small-argument formulas give

$$
F_{\nu,\rho}(k)
:=
J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k)
\longrightarrow
\frac{\rho^{-\nu}-\rho^\nu}{\pi\nu}>0
$$

as $k\downarrow0$. Thus the phase level zero at the limiting endpoint is not a
positive determinant root.

## Exact three-dimensional structural statement

Let

$$
\Omega_\rho=\{x\in\mathbb R^3:\rho<|x|<1\},
\qquad 0<\rho<1.
$$

After spherical-harmonic decomposition and the unitary substitution
$u(r)=rR(r)$,

$$
-\Delta_{\Omega_\rho}^D
\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}
L_\ell,
\qquad
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
$$

with $D(L_\ell)=H^2(\rho,1)\cap H_0^1(\rho,1)$. The exact direct-sum form and
operator domains are stated in
state/lemma_packets/SHELL-sturm-liouville-completeness.md.

Each radial block has a positive, simple, discrete spectrum. Compactness of
the full direct sum is not inferred merely block by block: since
$L_\ell\ge\ell(\ell+1)$, the resolvent norms of the angular tail tend to zero,
and the full resolvent is a norm limit of finite compact truncations.

For $\nu=\ell+\tfrac12$, a Wronskian-normalized solution satisfying the inner
Dirichlet condition is

$$
s_\ell(r,k)
=
\frac{\pi\sqrt\rho}{2}\sqrt r
\left[
J_\nu(\rho k)Y_\nu(kr)
-Y_\nu(\rho k)J_\nu(kr)
\right].
$$

It satisfies $s_\ell(\rho,k)=0$, $\partial_rs_\ell(\rho,k)=1$, and

$$
s_\ell(1,k)=\frac{\pi\sqrt\rho}{2}F_{\nu,\rho}(k).
$$

Therefore the positive roots of $F_{\nu,\rho}$ are exactly the radial
eigenfrequencies. Their simplicity also follows directly from

$$
\partial_rs_\ell(1,k)\,\partial_ks_\ell(1,k)
=2k\int_\rho^1s_\ell(r,k)^2\,dr>0
$$

at a positive root.

The channel $\ell$ has angular multiplicity $2\ell+1$. Frequencies belonging
to different angular channels may coincide; the Hilbert direct sum then adds
their multiplicities. No non-degeneracy across different $\ell$ is assumed.

## Phase-count consequence

With the branch convention in sources/bessel_phase_enclosures.md,

$$
\Psi_{\nu,\rho}(k)=\theta_\nu(k)-\theta_\nu(\rho k)
$$

is strictly increasing from $0$ to infinity, and the positive roots are the
unique solutions of

$$
\Psi_{\nu,\rho}(k)=n\pi,\qquad n=1,2,\ldots.
$$

Consequently the strict radial count below $K$ is

$$
\#\{n:k_{\ell,n}<K\}
=
\left\lceil\frac{\Psi_{\nu,\rho}(K)}{\pi}\right\rceil-1.
$$

This endpoint-aware formula, together with the direct-sum multiplicity rule,
is an exact identity rather than an asymptotic statement.

## Internal audit record

The full proof obligation, falsification tests, and promotion rule are in
state/lemma_packets/SHELL-sturm-liouville-completeness.md. The incumbent proof
is in
rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md.

These internal records must pass clean-room reconstruction and adversarial
review before the corresponding graph obligations are promoted.

## Unresolved source scope

The following remain open under SRC-shell-weyl:

- a Weyl-remainder statement with its precise spectral convention;
- uniformity as $\rho\to0$ and $\rho\to1$;
- explicit one-sided constants strong enough for the target inequality;
- a rigorous finite-window certificate where analytic estimates do not close.

Classical asymptotic formulas with unspecified error terms do not discharge
those items.
