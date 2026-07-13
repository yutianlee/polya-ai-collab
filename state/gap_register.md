# Gap Register

The authoritative statuses are in state/proof_obligations.yml.

## Active shell gaps

- Make the analytic high-energy threshold uniform on the explicit compact
  interval $[\rho_*,1-2^{-18}]$, then formulate the remaining finite parameter
  set as bounded boxes, where

  $$
  \rho_*=\frac{\frac{\sqrt3}{2\pi}-\frac16}
  {2+\frac{16\sqrt2}{15}}.
  $$

- Build interval-certified verification for those bounded boxes, including
  every determinant root, phase wall, floor wall, and strict spectral
  endpoint. Neither endpoint neighborhood requires certification.
- After the compact piece closes, perform a fresh theorem-level
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
- The small-hole low-interface shifted-tail theorem for
  $0<\rho<\omega_0$ and
  $K(\omega_0-\rho)\ge C_*$.
- The complete small-hole endpoint
  $0<\rho\le\rho_*$ for every $K\ge0$, obtained by splitting exactly at
  $\rho K=1/2$. The apparent finite small-hole residual is empty.

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
- Pointwise shell-to-ball root convergence is not uniform in the radial
  index and cannot prove an all-$K$ small-hole theorem.
- Bare domain monotonicity to the ball does not pay the missing volume factor
  $1-\rho^3$. Subtracting two one-sided ball Pólya bounds is also invalid
  across ball spectral jumps.

## Parallel-track gaps

- Mathieu-function source audit for the ellipse track.
- Jiang--Lin source audit for the certificate-family fallback.
