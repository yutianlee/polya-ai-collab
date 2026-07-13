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
- the optimized local-plateau estimate for the actual uncompensated loss

$$
R=p-dm<\frac{361}{80\sqrt\varepsilon},
$$

  obtained self-consistently without importing the old $C=64$ hypothesis,
  and the uniform high-thin theorem
  $K\ge125/(8\varepsilon^2)$ for $0<\varepsilon\le1/100$;
- the enlarged local-plateau seam theorem

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2},
$$

  proved by rederiving every domain-dependent estimate, with threshold
  equality included. The sharper constant $125/8$ remains authoritative on
  the overlap $0<\varepsilon\le1/100$;
- the complementary exact-action bridge: with
  $a=\varepsilon K$, the strict shell estimate holds on

$$
0<\varepsilon\le\frac1{100},
\qquad
a\ge\frac1{8\varepsilon^{3/2}},
$$

  including the threshold face. The incumbent radial argument leaves the
  exact normalized reserve $61/1400$, while an isolated reconstruction using
  a different sawtooth primitive leaves
  $4119252993/17500000000$;
- the accepted product and aggregate ranges cover the complementary closed
  range $0\le a\le1/(8\varepsilon^{3/2})$. Together with the new bridge this
  gives the complete endpoint theorem

$$
\frac{99}{100}\le\rho<1,
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

- the compact-ratio analytic envelope: on

$$
I_{11}=\left[\rho_*,\frac{99}{100}\right],
$$

  the possible residual families lie below $64$ on
  $[\rho_*,1/16]$, below $K_0(24/25)<6000^2$ on
  $[1/16,24/25]$, and below $200000$ on $[24/25,99/100]$.
  Therefore

$$
K\ge6000^2
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(\rho\in I_{11});
$$

- combining the compact envelope with both endpoint theorems gives the
  global analytic high-frequency result

$$
0<\rho<1,
\qquad K\ge6000^2.
$$

  The exact comparisons
  $(125^5/8)/6000^2=1953125/18432>105$ and
  $2^{35}/6000^2=134217728/140625>954$ quantify the reduction from the
  Round 10 and former global ceilings;

- the independently checked certified pilot

$$
\rho\in\left[\frac{999}{2000},\frac{1001}{2000}\right],
\qquad
K\in\left[\frac{67}{10},\frac{168}{25}\right],
$$

  where the exact strict count is $4$ and the certified Weyl margin exceeds
  $14.6073155354$. The Arb producer and independent rational checker are
  local evidence only; they do not certify the rest of the compact residual.

`SHELL-rho-compact` remains open. Round 11 has reduced the exact compact
residual to $I_{11}$ below $K=6000^2$, but it does not certify that residual.
The next analytic target is the central--thin seam: rederive the seam theorem
on $0<\varepsilon\le1/20$ with a target such as
$K\ge24/\varepsilon^2$, move the interface to $\rho=19/20$, and seek the
separate exact bound $K_0(19/20)<3300^2$. These are Round 12 goals, not
proved statements. Certification may expand only through an exact
face-connected manifest for the true residual $\mathcal D$; further analytic
aggregation or safe monotone-corner certification is still required. The
parent compact certification and final theorem remain open.
