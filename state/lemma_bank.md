# Lemma Bank

The authoritative statements and evidence are in state/proof_obligations.yml.

Validated shell lemmas now include:

- the exact $d=3$ separated Dirichlet spectrum with exact direct-sum domains,
  compact resolvent, complete simple radial blocks, and multiplicity
  $2\ell+1$;
- the sign-normalized Bessel cross-product characterization, simple positive
  roots, harmless cross-$\ell$ coincidences, and exact strict phase-count
  identity;
- exact monotone shell phase representation and the global phase enclosure;
- the exact strict phase-level counting convention;
- the exact weighted Weyl integral;
- the $2\ell+1$ multiplicity-to-shifted-tail reduction;
- high-angular shifted-tail bounds for starts at or above $\rho K$;
- fixed-$\rho$ high-energy shifted-tail bounds for starts below $\rho K$,
  with explicit $K_0(\rho)$;
- the complete fixed-$\rho$ high-energy weighted coarse, strict, and optimized
  phase proxies;
- the unconditional fixed-$\rho$ high-energy shell Pólya theorem for
  $K\ge K_0(\rho)$;
- $\theta'_{\ell+1/2}\le1$ and zero strict shell spectral count when
  $(1-\rho)K\le\pi$;
- the uniform thin-shell theorem
  \[
  0<\varepsilon=1-\rho\le1/100,\qquad
  K\le\pi/(4\varepsilon^2),
  \]
  proved by an exact strict product-index comparison.

The next primary packet is SHELL-thin-curvature-intermediate. It must retain
the radial dependence of $\ell(\ell+1)/r^2$ strongly enough to match the mean
shell cross-section

$$
\frac1\varepsilon\int_{1-\varepsilon}^1r^2\,dr
=1-\varepsilon+\frac{\varepsilon^2}{3}.
$$

An independent packet should audit SHELL-rho-zero-endpoint. Only after those
endpoint results produce bounded residual boxes should COMP-certified-bessel
move beyond design work.
