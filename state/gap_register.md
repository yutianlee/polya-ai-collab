# Gap Register

The authoritative statuses are in state/proof_obligations.yml.

## Active shell gaps

- Prove a quantitative small-hole endpoint: find an explicit $\rho_0>0$ and
  cover every $0<\rho\le\rho_0$ and $K\ge0$. Pointwise convergence of shell
  roots to ball roots is not a uniform proof; low angular orders, the regime
  $\rho K<1/2$, and strict phase walls require explicit control.
- Make the analytic high-energy threshold uniform on the intervening compact
  interval $[\rho_0,1-2^{-18}]$, then formulate the remaining finite parameter
  set as bounded boxes.
- Build interval-certified verification for those bounded boxes, including
  every determinant root, phase wall, floor wall, and strict spectral
  endpoint. No thin-endpoint certificate is required.
- After the small-hole and compact pieces close, perform a fresh theorem-level
  clean-room reconstruction and adversarial audit before promoting the global
  shell theorem.

## Closed shell prerequisites

- The exact spherical-harmonic/Sturm--Liouville direct-sum spectrum, including
  completeness, radial simplicity, angular multiplicity, and accidental
  cross-channel coincidences.
- The Bessel cross-product determinant and exact strict phase-count identity.
- The global half-integer Bessel cross-product phase enclosure.
- The exact weighted Weyl integral and multiplicity-to-shifted-tail scaffold.
- Every shifted tail starting at or above the inner interface.
- Every shifted tail starting below the inner interface for fixed $\rho$ and
  $K\ge K_0(\rho)$, with explicit $K_0$.
- The complete fixed-$\rho$ high-energy multiplicity-weighted phase proxy.
- The actual fixed-$\rho$ high-energy shell Pólya estimate for
  $K\ge K_0(\rho)$.
- The exact spectral zero-count region $(1-\rho)K\le\pi$.
- The uniform thin-shell product range
  $0<1-\rho\le1/100$ and
  $K\le\pi/[4(1-\rho)^2]$.
- The radius-sensitive mean-square-action range
  $K\le1/[8(1-\rho)^{5/2}]$ after combination with the product range.
- The uniform local-plateau high-thin range
  $K\ge64/(1-\rho)^2$ for $1-\rho\le1/100$.
- The complete thin-shell endpoint
  $1-2^{-18}\le\rho<1$ for every $K\ge0$, obtained from the exact overlap of
  the preceding low and high ranges.

## Rejected shell routes

- Replacing $r^{-2}$ by its outer-boundary minimum $1$ cannot close the full
  thin-shell endpoint. The resulting product majorant has exact failures at
  optical width of order $(1-\rho)^{-1}$.
- The Round 5 product range alone does not overlap the old
  $K_0(1-\varepsilon)$ threshold. Round 6 supersedes that failed two-piece
  route with aggregate-action and local-plateau estimates.
- A single volume-matched effective radius is not a global pointwise action
  majorant: it vanishes inside the positive whispering-gallery strip.
- Any fixed finite Neumann-sublayer majorant has the wrong cubic coefficient
  at sufficiently large $K$.

## Parallel-track gaps

- Mathieu-function source audit for the ellipse track.
- Jiang--Lin source audit for the certificate-family fallback.
