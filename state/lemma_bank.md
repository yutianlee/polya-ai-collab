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
  proved by an exact strict product-index comparison;
- the exact scaled-action identity and weighted integral

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds,
\qquad
\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right),
$$

  together with the mean-square-radius comparison and explicit
  whispering-gallery payment proving the shell inequality for
  $K\le1/(8\varepsilon^{5/2})$ after combination with the product range;
- the local first-plateau estimate $p<10/\sqrt\varepsilon$ and the uniform
  high-thin theorem $K\ge64/\varepsilon^2$;
- the exact overlap

$$
\frac{64}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le2^{-18},
$$

  with equality included; and hence the complete endpoint theorem

$$
1-2^{-18}\le\rho<1,
\qquad K\ge0.
$$

- the audited small-hole low-interface theorem with

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
$$

  valid when
  $0<\rho<\omega_0$ and $K(\omega_0-\rho)\ge C_*$;
- the exact small-hole overlap

$$
\frac{C_*}{\omega_0-\rho}
\le\frac1{2\rho}
\quad\Longleftrightarrow\quad
\rho\le\rho_*:=\frac{\omega_0}{1+2C_*},
$$

  and hence the complete endpoint theorem

$$
0<\rho\le\rho_*,
\qquad K\ge0.
$$

The next primary packet is `SHELL-rho-compact`. It must derive a practical
uniform analytic threshold on
$[\rho_*,1-2^{-18}]$ and reduce the remaining all-$K$ problem to explicit
bounded boxes. `COMP-certified-bessel` may certify only those boxes; both
endpoint neighborhoods are analytically discharged and excluded from the
certificate.
