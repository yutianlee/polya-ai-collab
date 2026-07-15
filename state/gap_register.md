# Gap Register

The authoritative statuses are in state/proof_obligations.yml.

## Active shell gaps

- The exact compact residual is closed. Round 21 proves

  $$
  \mathcal D_{20}=
  \{\rho_c\le\rho<39/50,\ k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}
  $$

  is the disjoint union of its compact-owned $K\le200$ part and its
  aggregate-owned $K>200$ part. The exact guards are
  $7/51<\rho_c$ and $k_{11}(\rho)>12$ only for
  $\rho_c\le\rho<1$. Consequently the accepted successor residual is

  $$
  \boxed{\mathcal D_{21}=\varnothing.}
  $$

  `CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail` are
  `certified`; `SHELL-exact-d20-closure` is `proved_internal`.

- The active mathematical gap is theorem assembly, not another residual
  estimate. `SHELL-rho-compact`, `SHELL-rho-uniformity`,
  `TARGET-shell-d3`, and `POLYA-program-target` remain `open`. A coherent
  proof must reconstruct the complete unit-shell cover from the promoted
  graph and explicitly check the seams at $\rho_*$, $\rho_c$, $39/50$, and
  $7/8$, all frequency faces, the equality case $K=0$, and strict positive
  counts at eigenvalue walls.

- The theorem assembly must rederive the normalization

  $$
  L_3=\frac1{6\pi^2},\qquad
  |A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),\qquad
  L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3),
  $$

  and then scale from $A_{\rho,1}$ to
  $A_{r,R}=R A_{r/R,1}$ using volume scaling by $R^3$ and eigenvalue
  scaling by $R^{-2}$.

- A fresh clean-room theorem reviewer must reconstruct the global implication
  without the incumbent proof draft. A separate adversarial referee must
  assume `TARGET-shell-d3` false and identify the first unsupported seam,
  convention, normalization, or scaling step. Only after both pass may a
  theorem judge propose promoting the compact, uniformity, and shell-target
  obligations.

- Before `POLYA-program-target` can be promoted, a separate program-scope
  audit must verify that the full family of three-dimensional spherical
  shells is a natural non-tiling Euclidean class and that no ellipse or
  certificate-family side track is silently claimed as solved. The result
  must make no publication-priority or novelty claim. The final graph should
  represent the non-tiling premise with a scoped proved obligation and an
  explicit dependency, rather than leaving it only in narrative prose.

- The Round 8 box $B_0$ and face-connected Round 17 box $B_1$ remain
  independent regression evidence inside $\mathcal C_{17}$. They subtract
  nothing from empty $\mathcal D_{21}$. `COMP-certified-bessel` remains
  `diagnostic_only` and is now detached from the theorem path. The scoped
  Round 21 certificates carry the accepted executable evidence.

- The stretch endpoint screens at $\rho=6/7$ and $\rho=23/27$ remain
  unproved. The negative screens at $\rho=17/20$ and $\rho=5/6$ are
  obstructions only to the tested extension routes, not counterexamples to
  the shell theorem and not new shell blockers.

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
- The Round 18 next-angular-staircase theorem

  $$
  \rho_c\le\rho\le\frac78,
  \qquad
  z_\rho\le K\le k_5(\rho),
  $$

  including the complete $K=k_5$ face. Fixed-channel zero extension and
  min--max internally prove
  $\lambda_{\ell,1}^{\rm shell}\ge\lambda_{\ell,1}^{\rm ball}$, and the
  audited ball separation identifies the latter as $j_{\ell+1/2,1}^2$;
  this comparison is not attributed to Lorch. The audited statement-level
  Lorch dependency is
  restricted to
  $j_{5/2,1}>51/10$, $j_{7/2,1}>13/2$, and
  $j_{9/2,1}>15/2$. Its publisher abstract is accessible, but its proof was
  access-controlled. The delayed entries give cumulative caps
  $4,9,16,25$ at ratio splits $3/10,1/2,1/2$, with exact payments
  $100387329/11000000>9$, $107653/6336>16$, and
  $18375/704>25$. The upper-floor audit gives $k_5<26<64<K_0$ on the
  active fixed-ratio branch and $k_5<26<1944\le54/(1-\rho)^2$ on the seam
  branch. Isolated reconstruction, an exact constants audit, source audit,
  cross-comparison, and fresh adversarial review all passed.
- The Round 19 two-sided staircase theorem

  $$
  \rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_6(\rho),
  $$

  together with

  $$
  \frac1{\sqrt{337}}<\rho<\rho_c,\qquad
  \frac1{2\rho}<K\le\frac{\sqrt{337}}2.
  $$

  The only new external payload is the audited
  $j_{11/2,1}>17/2$ specialization. The bounds
  $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$, both variational comparisons,
  angular shifts, exhaustive caps, multiplicities, and Weyl payments are
  internal. The 245-check exact verifier, 24 focused tests, isolated
  reconstruction, cross-comparison, and fresh adversarial referee passed.
- The Round 20 combined-closure theorem. It closes both lower components of
  $\mathcal D_{19}$, extends the strict high staircase through
  $k_{11}(\rho)$, and proves the all-frequency optical theorem on
  $39/50\le\rho<1$. The only indispensable new external zero is the
  qualified $j_{21/2,1}>69/5$ specialization; every higher-radial zero,
  strengthened lower-order first zero, shell comparison, angular
  propagation, cap, and payment is internal. The residual and proof-free
  claim freezes, isolated A3 reconstruction and corrective addendum,
  zero-provenance audit, final repaired 587-check A4 ledger, cross-comparison,
  fresh referee, judge, and State-Patch audit passed. The initial candidate
  release and the first two A4 bundles remain preserved failure history, not
  positive evidence.
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
  $\mathcal D_{17}=\mathcal D_{16}\setminus\mathcal C_{17}$, and Round 18
  replaces that by
  the historical
  $\mathcal D_{18}=\mathcal D_{17}\setminus\mathcal C_{18}$. Round 19 then
  replaces it by historical
  $\mathcal D_{19}=\mathcal D_{18}\setminus\mathcal C_{19}$. Round 20
  replaced that set by the one-piece
  $\mathcal D_{20}=\mathcal D_{19}\setminus\mathcal C_{20}$. Round 21 has
  now closed it, after the full proof-free, isolated, executable-provenance,
  adversarial, judge, and State-Patch lifecycle, so the accepted residual is
  $\mathcal D_{21}=\varnothing$.
- Paying the entire first $\ell=2$ multiplicity immediately above
  $k_2(\rho)$ cannot uniformly continue the Round 17 coarse channel cap:
  the cap becomes $9$, while the Weyl term is below $9$ at the left ratio
  face. This rejects only that coarse continuation, not the target
  inequality. Round 18 overcame this historical obstruction through $k_5$;
  Round 19 then crossed the radial-entry wall through $k_6$. Neither is the
  present boundary.

## Parallel-track gaps

- Mathieu-function source audit for the ellipse track.
- Jiang--Lin source audit for the certificate-family fallback.
