# Gap Register

The authoritative statuses are in state/proof_obligations.yml.

## Current shell status and remaining work

- There is no open mathematical obligation on the internal spherical-shell
  theorem path. In the authoritative post-Round-22 graph,
  `SHELL-spherical-shell-nontiling`, `SHELL-rho-compact`,
  `SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target` are
  all `proved_internal` with empty blockers. The graph was applied once in
  commit `d8fe505` and has SHA-256
  `b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`.

- The completed spectral theorem is

  $$
  N_D(A_{r,R},\Lambda)
  \le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
  =L_3|A_{r,R}|\Lambda^{3/2},
  \qquad 0<r<R,\quad\Lambda\ge0,
  $$

  for the strict count and $L_3=1/(6\pi^2)$. The complete review lifecycle
  checked $K=0$, the seams at $\rho_*$, $\rho_c$, $39/50$, and $7/8$, every
  inherited frequency face and strict wall, Weyl-volume normalization, and
  arbitrary-radius scaling.

- The separately reviewed non-tiling theorem covers the same complete
  $0<r<R$ class under congruent rigid motions, pairwise-disjoint interiors,
  exact or almost-everywhere coverage, and the corresponding closed-copy
  convention after removal of the countable null boundary union. The
  geometric node has no spectral premise; the two tracks meet only at
  `POLYA-program-target`.

- The source-final authority is
  `rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`. Its
  passing pre-application and post-application audits are
  `rounds/polya-main/round_022/reviews/state-patch-final-audit-source-utf8-final.md`
  and
  `rounds/polya-main/round_022/reviews/state-patch-application-audit-source-utf8-final.md`.
  Two earlier provenance gates remain negative chronology: the first
  judge/audit failed on a 299-versus-300 physical-line metadata statement,
  and the replacement judge/audit failed on four corrupted `Pólya` tokens.
  Neither failed patch was applied.

- The remaining work is external-validation work, not an internal theorem
  gap: human reconstruction of all bottleneck lemmas, manuscript-level
  checking, and an independent current literature audit. The internal result
  does not settle the general Pólya conjecture and makes no novelty,
  publication-priority, first-proof, or publication-readiness claim.

- The Round 8 box $B_0$ and face-connected Round 17 box $B_1$ remain
  independent regression evidence inside $\mathcal C_{17}$. They subtract
  nothing from empty $\mathcal D_{21}$. `COMP-certified-bessel` remains
  `diagnostic_only`, unchanged and detached from the theorem path. The scoped
  Round 21 certificates carry the accepted executable evidence.

- The stretch endpoint screens at $\rho=6/7$ and $\rho=23/27$ remain
  unproved, but they are obsolete exploratory extensions rather than theorem
  blockers. The negative screens at $\rho=17/20$ and $\rho=5/6$ obstruct only
  their tested routes and are not counterexamples.

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

- `ELLIPSE-near-circular` remains open; its Mathieu-function source audit is
  still a parallel-track gap.
- `CERT-certificate-family` remains open; its Jiang--Lin source audit is
  still a parallel-track gap.
