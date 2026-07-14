# Gap Register

The authoritative statuses are in state/proof_obligations.yml.

## Active shell gaps

- Close the exact Round 17 compact residual on
  $I_{16}=[\rho_*,7/8]$, where

  $$
  \rho_*=\frac{\frac{\sqrt3}{2\pi}-\frac16}
  {2+\frac{16\sqrt2}{15}}.
  $$

  Define

  $$
  \rho_c=\frac1{1+2\pi},
  \qquad
  z_\rho=\frac{\pi}{1-\rho},
  \qquad
  k_2(\rho)=\sqrt{z_\rho^2+6}.
  $$

  The promoted closed band
  $\rho_c\le\rho\le7/8$, $z_\rho\le K\le k_2(\rho)$ removes exactly its
  genuinely new portion $\mathcal C_{17}$ from the prior residual. Hence

  $$
  \mathcal D_{17}
  =\mathcal D_{16}\setminus\mathcal C_{17}
  =\left\{\rho_*<\rho<\rho_c,
  \ \frac1{2\rho}<K<U(\rho)\right\}
  \cup
  \left\{\rho_c\le\rho<\frac78,
  \ k_2(\rho)<K<U(\rho)\right\}.
  $$

  Here $U(\rho)$ is the exact frozen upper floor: $H_0(\rho)$ below
  $\rho_{HK}$, $K_0(\rho)$ from $\rho_{HK}$ to $5/6$, and
  $54/(1-\rho)^2$ from $5/6$ to $7/8$. The two pieces are nonempty;
  closing $\mathcal D_{17}$ is the sole shell blocker. It is not admissible
  to substitute $\mathcal D_{16}$, the four-zone over-cover, or a rectangle.

- The Round 8 box $B_0$ and its face-connected Round 17 extension
  $B_1=[999/2000,1001/2000]\times[168/25,673/100]$ are independently
  certified, with exact strict count $4$ on each. Both boxes lie inside
  $\mathcal C_{17}$ and are therefore analytically redundant after
  promotion. `COMP-certified-bessel` remains `diagnostic_only`; any future
  certificate must be bounded, face-connected, and contained in the exact
  $\mathcal D_{17}$, with rigorous truncation, provenance hashes, and an
  independent checker.

- The first direct continuation above $k_2(\rho)$ is unresolved. The same
  coarse min--max comparison changes its multiplicity cap from $4$ to $9$
  when the $\ell=2$ channel becomes available, while the Weyl term at
  $(\rho_c,k_2(\rho_c))$ is strictly below $9$. A next step therefore needs
  a sharper $\ell=2$ eigenvalue estimate, a ratio-dependent staircase, or a
  different action/tail argument. This is a method obstruction only.

- The stretch endpoint screens at $\rho=6/7$ and $\rho=23/27$ remain
  unproved. The negative screens at $\rho=17/20$ and $\rho=5/6$ are
  obstructions only to the tested extension routes, not counterexamples to
  the shell theorem and not new shell blockers.

- After $\mathcal D_{17}$ closes, perform a fresh theorem-level
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
- The ultra-thin complementary-action bridge: for
  $0<\varepsilon\le1/100$, $a=\varepsilon K$, and
  $a\ge1/(8\varepsilon^{3/2})$, the strict shell estimate holds, including
  the threshold face. Independent radial arguments leave exact positive
  reserves $61/1400$ and $4119252993/17500000000$.
- The optimized uniform local-plateau high-thin range
  $K\ge125/[8(1-\rho)^2]$ for $1-\rho\le1/100$, proved without importing
  estimates conditional on the old constant $64$.
- The enlarged local-plateau seam range
  $K\ge20/(1-\rho)^2$ for $1-\rho\le1/25$, proved by rederiving every
  domain-dependent estimate. On the common domain $1-\rho\le1/100$, the
  sharper constant $125/8$ remains authoritative.
- The Round 12 enlarged seam range
  $K\ge24/(1-\rho)^2$ for $1-\rho\le1/20$, proved by complete independent
  rederivations. The sharper Round 10 threshold remains authoritative for
  $1-\rho\le1/25$.
- The Round 13 enlarged seam range
  $K\ge24/(1-\rho)^2$ for $1-\rho\le1/10$, proved by complete independent
  rederivations. The incumbent and independent inventory close a fixed-$r$
  path with $B=14/3$; the isolated proof uses a distinct affine path.
- The Round 14 enlarged seam range
  $K\ge32/(1-\rho)^2$ for $1-\rho\le1/8$, including threshold equality.
  The sharper Round 13 threshold $24/(1-\rho)^2$ remains authoritative for
  $1-\rho\le1/10$, and the sharper Round 10 threshold
  $20/(1-\rho)^2$ remains authoritative for $1-\rho\le1/25$. The attempted
  $\kappa=24$ continuation proves only $x_0/K>173/384$, while
  $173/384<1/2$; hence the lower bound does not localize beyond $1/2$ in the
  current route. This is not a rejection of a stronger theorem.
- The Round 15 enlarged seam range
  $K\ge54/(1-\rho)^2$ for $1-\rho\le1/6$, including threshold equality.
  The retained sharper thresholds are $32/(1-\rho)^2$ for
  $1-\rho\le1/8$, $24/(1-\rho)^2$ for $1-\rho\le1/10$, and
  $20/(1-\rho)^2$ for $1-\rho\le1/25$. The moved seam is $\rho=5/6$,
  where the separately checked fixed-ratio threshold satisfies
  $K_0(5/6)<295^2=87025$. The selected $\kappa=53$ localization proxy
  misses by $14293/15900000$, while the selected $Y=294$ central proxy is
  $-307/175$; these are route obstructions only.
- The historical Round 11 thin-shell endpoint
  $99/100\le\rho<1$ for every $K\ge0$, obtained by joining the accepted
  product and aggregate ranges to the complementary-action bridge at the
  inclusive face $a=1/(8\varepsilon^{3/2})$.
- The stronger Round 16 complete thin-shell endpoint
  $7/8\le\rho<1$ for every $K\ge0$. With $a=\varepsilon K$, the product
  low piece and complementary-action high piece both own their shared face
  $a=\pi/(4\varepsilon)$ and retain exact reserves $577/2880$ and
  $143/4096$. The face $\rho=7/8$ is included, $\rho=1$ is open, $K=0$
  gives equality, and the proof comparison is strict for $K>0$ before the
  final non-strict theorem statement.
- The small-hole low-interface shifted-tail theorem for
  $0<\rho<\omega_0$ and
  $K(\omega_0-\rho)\ge C_*$.
- The complete small-hole endpoint
  $0<\rho\le\rho_*$ for every $K\ge0$, obtained by splitting exactly at
  $\rho K=1/2$. The apparent finite small-hole residual is empty.
- The Round 16 four-zone compact-ratio analytic envelope and uniform theorem
  $K\ge295^2=87025$ on $I_{16}=[\rho_*,7/8]$, including equality. The
  residual ceilings are below $64$ on $[\rho_*,1/16]$, below
  $K_0(\rho)\le K_0(5/6)<87025$ on $[1/16,5/6]$, below
  $54/(1-\rho)^2\le3456$ on $[5/6,7/8]$, and empty on $[7/8,1)$ because
  the endpoint theorem holds at every frequency.
- The global analytic high-frequency shell theorem for
  $0<\rho<1$ and $K\ge295^2=87025$, including equality, obtained by
  combining the compact envelope with the two complete endpoint theorems.
  The exact reduction factor from the Round 15 ceiling is
  $200000/295^2=8000/3481>2$.
- The Round 17 first-angular-band theorem

  $$
  \rho_c\le\rho\le\frac78,
  \qquad
  \frac{\pi}{1-\rho}\le K
  \le\sqrt{\left(\frac{\pi}{1-\rho}\right)^2+6},
  $$

  including every frequency and ratio face. The proof combines the exact
  $\ell=0$ interval spectrum with the radial min--max bound, strict spectral
  counting, full multiplicities, and exact Weyl payments. It passed isolated
  reconstruction, exact finite-constant audit, and fresh adversarial review.
- One independently checked interval-certified central residual box,
  $\rho\in[999/2000,1001/2000]$ and
  $K\in[67/10,168/25]$, with exact strict count $4$.
- Its independently checked face-connected Round 17 extension,
  $\rho\in[999/2000,1001/2000]$ and
  $K\in[168/25,673/100]$, also with exact strict count $4$. Both certified
  boxes are contained in the promoted analytic band and are retained as
  independent regression evidence rather than additional residual coverage.

## Rejected shell routes

- Replacing $r^{-2}$ by its outer-boundary minimum $1$ cannot close the full
  thin-shell endpoint. The resulting product majorant has exact failures at
  optical width of order $(1-\rho)^{-1}$.
- The Round 5 product range alone does not overlap the old
  $K_0(1-\varepsilon)$ threshold. Round 6 supersedes that failed two-piece
  route with aggregate-action and local-plateau estimates.
- Combining the enlarged Round 10 constant $C=20$ with the aggregate-action
  range overlaps only for $\varepsilon\le1/25600$. It therefore does not
  enlarge the then-proved all-frequency endpoint
  $\varepsilon\le1/15625$; Round 11 supersedes this two-range obstruction
  with a separate complementary-action bridge.
- A single volume-matched effective radius is not a global pointwise action
  majorant: it vanishes inside the positive whispering-gallery strip.
- Any fixed finite Neumann-sublayer majorant has the wrong cubic coefficient
  at sufficiently large $K$.
- Pointwise shell-to-ball root convergence is not uniform in the radial
  index and cannot prove an all-$K$ small-hole theorem.
- Bare domain monotonicity to the ball does not pay the missing volume factor
  $1-\rho^3$. Subtracting two one-sided ball Pólya bounds is also invalid
  across ball spectral jumps.

- Literal wall-by-wall certification of the Round 8 coarse compact envelope
  was not a scalable route. At $\varepsilon=2^{-17}$, one former thin
  residual slice crossed more than $2^{38}$ angular half-integer walls.
  By the close of Round 15 the all-ratio ceiling had fallen to $200000$;
  Round 16 supersedes that historical boundary with $295^2=87025$ and the
  smaller residual $\mathcal D_{16}$. Round 17 further replaces it by
  $\mathcal D_{17}=\mathcal D_{16}\setminus\mathcal C_{17}$, but its
  closure still requires monotone-corner, symbolic, or analytic aggregation.
- Paying the entire first $\ell=2$ multiplicity immediately above
  $k_2(\rho)$ cannot uniformly continue the Round 17 coarse channel cap:
  the cap becomes $9$, while the Weyl term is below $9$ at the left ratio
  face. This rejects only that coarse continuation, not the target
  inequality or a sharper third-angular-band lemma.

## Parallel-track gaps

- Mathieu-function source audit for the ellipse track.
- Jiang--Lin source audit for the certificate-family fallback.
