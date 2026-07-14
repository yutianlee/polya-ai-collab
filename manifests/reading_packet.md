# Reading Packet

Generated after round 17 in run `polya-main`.

## Current Theorem Target

Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain
class.

Current status: no complete all-ratio shell theorem has been proved. The
exact three-dimensional spectrum, fixed-ratio high-energy theorem, both
uniform ratio-endpoint neighborhoods, the all-ratio range
$K\ge295^2=87025$, and the Round 17 first-angular band are proved. The exact
surviving nonrectangular residual is

$$
\begin{aligned}
\mathcal D_{17}
={}&\left\{\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K<U(\rho)\right\},
\end{aligned}
$$

where

$$
\rho_c=\frac1{1+2\pi},
\qquad
k_2(\rho)=\sqrt{\left(\frac{\pi}{1-\rho}\right)^2+6}.
$$

The certified boxes $B_0$ and $B_1$ remain independently valid, but both
are contained in the promoted analytic band $\mathcal C_{17}$. They are
regression evidence, not additional residual coverage. Consequently the
theorem-wise uncovered set is exactly
$\mathcal U_{17}=\mathcal D_{17}$. Exact coverage of this set and the final
theorem-level audits remain open.

## Current Route

Prove
$N_D(\Omega,\Lambda)\le L_d|\Omega|\Lambda^{d/2}$ for all
$\Lambda\ge0$ for at least one new natural non-tiling Euclidean domain
class, with Dirichlet boundary conditions and a fixed strict-counting
convention.

For the shell target, attack the exact $\mathcal D_{17}$ by a sharper
next-angular spectral staircase. A continuation above $k_2$ cannot use only
the crude multiplicity cap $9$: at
$(\rho_c,k_2(\rho_c))$ the Weyl payment is strictly smaller than $9$.
Round 18 must sharpen the $\ell=2$ entry threshold or the count/payment
staircase itself.

## Active Bottleneck

`TARGET-shell-d3`: `open`.

For
$A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\}$,
$0<\rho<1$, prove

$$
N_D(A_{\rho,1},\Lambda)
\le\frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}
\qquad(\Lambda\ge0)
$$

using strict counting. Equivalently, with $K=\sqrt\Lambda$, prove the same
bound with right side
$\frac{2}{9\pi}(1-\rho^3)K^3$ for every $K\ge0$.

Current blockers:

- `COMP-certified-bessel` (`diagnostic_only`): certified finite-window
  verification for Bessel cross-products.
- `SHELL-rho-uniformity` (`open`): uniformity in the shell ratio $\rho$.

## Round Target Obligations

- `SHELL-rho-compact` (`open`, owner `A2`): Uniform shell estimates on
  compact ratio intervals.
  Next action: close exactly $\mathcal D_{17}$, preserving its two ratio
  pieces, strict frequency faces, and piecewise upper floor $U(\rho)$. Use a
  sharper next-angular staircase rather than the failed crude cap $9$.
- `COMP-certified-bessel` (`diagnostic_only`, owner `A4`): Certified
  finite-window verification for Bessel cross-products.
  Next action: retain $B_0$ and $B_1$ as analytically redundant regression
  certificates. Any Round 18 pilot must be one predeclared face-connected
  subset proved wholly inside $\mathcal D_{17}$; the parent remains
  `diagnostic_only`.

## Do-Not-Claim Rules

- Do not claim the shell theorem, ellipse theorem, or certificate-family
  theorem has been proved.
- Do not replace $\mathcal D_{17}$ by $\mathcal D_{16}$, a rectangle, a
  coarse envelope, or a sampled grid.
- Do not subtract $B_0$ or $B_1$ again; both are already analytically
  subsumed by $\mathcal C_{17}$.
- Floating-point and symbolic computation are diagnostic only. Interval or
  formal certification discharges only its explicit finite computation
  obligation and proves no analytic spectral statement.
- Do not use external theorems as proof dependencies without completed
  source cards.
- Do not promote a bottleneck without exact proof evidence, an isolated
  clean-room reconstruction, an independent exact audit, and a fresh
  adversarial-review artifact.
- Do not interpret the failed crude cap $9$ as a counterexample to Pólya.

## Obligation Roles

Use `state/next_round_prompts.md` for the canonical Round 18 role-specific
tasks selected from the graph.

Current functional split:

- `A1`: exact residual architecture, packet freezing, lead synthesis, and
  State Patch authoring.
- `A2`: incumbent analytic developer for the sharper next-angular
  staircase.
- `A3`: strictly isolated clean-room reconstruction from a reduced packet
  with no incumbent proof.
- `A4`: independent exact-constant and set auditor, plus at most one bounded
  certification pilot.
- A fresh referee that participated in neither proof performs the final
  adversarial candidate audit.
- Only assigned reviewers receive peer outputs; universal all-agent
  cross-review is not required.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `state/lemma_packets/SHELL-rho-compact-round17.md`
- `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md`
- `state/lemma_packets/SHELL-sturm-liouville-completeness.md`
- `rounds/polya-main/round_017/judge/judge-017.md`
- `rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md`
- `rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md`
- `rounds/polya-main/round_017/exploration/analytic-constant-audit.md`
- `rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md`
- `problems/polya_conjecture.md`
- `sources/flps_balls.md`
- `sources/annuli_polya.md`
- `sources/bessel_phase_enclosures.md`
- `sources/shell_weyl_bessel.md`
- `manifests/reading_packet.md`

## Last State Patch

Round 17 State Patch applied exactly once. It created
`SHELL-first-angular-bands` as `proved_internal` and
`COMP-certified-bessel-pilot-round17` as `certified`; enlarged the compact
analytic envelope by the exact closed band
$\overline{\mathcal C}_{17}$; and replaced $\mathcal D_{16}$ by the exact
strict subset $\mathcal D_{17}$. It retained `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target` as
`open`, and retained `COMP-certified-bessel` as `diagnostic_only`. The
certified boxes $B_0$ and $B_1$ are analytically redundant after promotion.
Round score: 6.

## Active Obligation Briefs

### SHELL-rho-compact: Uniform shell estimates on compact rho intervals

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `COMP-certified-bessel`
- Next action: Keep this obligation open. Close exactly
  $\mathcal D_{17}$: the strip $\rho_*<\rho<\rho_c$ above $1/(2\rho)$ and
  the strip $\rho_c\le\rho<7/8$ above $k_2(\rho)$, both strictly below
  $U(\rho)$.

### COMP-certified-bessel: Certified finite-window verification for Bessel cross-products

- Status: `diagnostic_only`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Keep the parent `diagnostic_only`. $B_0$ and $B_1$ are valid
  local certificates but are analytically redundant. Any new certificate
  must be a single predeclared face-connected subset proved wholly inside
  $\mathcal D_{17}$ and independently checked before graph use.

### CERT-certificate-family: Fallback target: certified non-tiling comparison family

- Status: `open`
- Track: `certificate_family`
- Owner: `A3`
- Blockers: `SRC-jiang-lin`
- Next action: Keep as a fallback route. Do not mark blocked. First complete
  `SRC-jiang-lin` before proposing a concrete family or exact certificate
  theorem.

### ELLIPSE-near-circular: Parallel flagship target: Dirichlet Pólya for near-circular ellipses

- Status: `open`
- Track: `ellipse_parallel`
- Owner: `A3`
- Blockers: `SRC-mathieu-ellipse`
- Next action: Keep as a parallel flagship track. Do not mark blocked. Next
  useful action is source-auditing Mathieu characteristic values,
  small-eccentricity perturbation, and certified eigenvalue enclosures after
  the shell Round 2 core tasks are assigned.

### FLPS-disk-ball-reproduction: Reproduce the FLPS disk/ball proof architecture

- Status: `open`
- Track: `flps_reproduction`
- Owner: `A2`
- Next action: Reproduce only the remaining proof infrastructure needed by
  active obligations; the FLPS ball source card is now audited.

### POLYA-program-target: Program target: exact Dirichlet Pólya for a new non-tiling Euclidean class

- Status: `open`
- Track: `target_conventions`
- Owner: `A1`
- Blockers: `COMP-certified-bessel`
- Next action: Keep the program target open until `TARGET-shell-d3` passes
  ratio uniformity, finite certification, and final theorem-level clean-room
  review.

### SHELL-inner-turning: Inner-boundary turning regime for shell phase differences

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Defer a new Airy enclosure. First test whether FLPS annuli
  Lemma 5.2, including the global bound on $\rho K<\nu\le K$ and the
  correlated $1/4$ bound on $\nu\le\rho K$, closes the weighted lattice
  estimate.

### SHELL-low-interface-shifted-tails: Shifted shell tails crossing the inner interface

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Criticality: `bottleneck`
- Lead author: `A2`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Next action: The fixed-ratio high-energy part is discharged and no longer
  blocks the weighted proxy. The unrestricted all-$K$ strengthening remains
  open; finite theorem closure belongs to certified computation and endpoint
  analysis.

### SHELL-phase-evanescent: Mixed and fully evanescent shell phase control

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Use the global one-sided annulus bound first; seek a sharper
  evanescent estimate only if the weighted-lattice margin fails.

### SHELL-phase-oscillatory: Shell phase enclosure in the ordinary oscillatory regime

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Treat as a fallback sharpening obligation only if the
  transferred annulus phase bound lacks sufficient weighted-lattice margin.

### SHELL-phase-outer-turning: Shell phase enclosure at the outer turning point

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Treat as a fallback sharpening obligation only if the
  transferred annulus phase bound lacks sufficient weighted-lattice margin.

### SHELL-phase-overlap: Compatibility and complete coverage of shell phase regimes

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A1`
- Criticality: `bottleneck`
- Lead author: `A1`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Blockers: `SHELL-phase-oscillatory`, `SHELL-phase-outer-turning`,
  `SHELL-inner-turning`, `SHELL-phase-evanescent`
- Next action: The transferred global bound removes regime-coverage gaps at
  the present precision. Reactivate only if fallback regime sharpenings are
  introduced.

### SHELL-rho-uniformity: Uniformity in shell ratio rho

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-rho-compact`
- Next action: Both endpoint neighborhoods, the all-ratio
  $K\ge295^2$ range, and $\overline{\mathcal C}_{17}$ are proved. Keep this
  obligation open until the exact surviving compact residual
  $\mathcal D_{17}$ is closed.

### SHELL-spherical-bessel-algebraic: Elementary spherical-Bessel form of half-integer shell cross-products

- Status: `open`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Promote only after the all-$\ell$ recurrence identity and its
  numerical-conditioning domain are proved; current low-order tests remain
  diagnostic.

### SRC-jiang-lin: Source audit: Jiang-Lin epsilon-loss and certificate strategy

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Create a source card before using Jiang-Lin as a proof
  dependency.

### SRC-mathieu-ellipse: Source audit: Mathieu-function tools for Dirichlet ellipses

- Status: `source_audit_required`
- Track: `ellipse_parallel`
- Owner: `A1`
- Next action: Keep this as a parallel source-audit track until the shell
  Round 1 target theorem memo is stable.

### SRC-shell-weyl: Source audit: Bessel functions and Weyl law for balls and spherical shells

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: The structural spectrum component is audited. Audit only the
  unresolved quantitative Weyl remainder, endpoint-uniform constants,
  one-sided Pólya-strength estimates, and finite-window certification scope.

### TARGET-shell-d3: First theorem target: Dirichlet Pólya for 3D spherical shells

- Status: `open`
- Track: `shell_analytic`
- Owner: `A1`
- Criticality: `theorem`
- Lead author: `A1`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A2`
- Blockers: `COMP-certified-bessel`, `SHELL-rho-uniformity`
- Next action: Retain both endpoint theorems, the all-ratio high-frequency
  theorem, and $\overline{\mathcal C}_{17}$. Complete exact coverage of
  $\mathcal D_{17}$, then run fresh theorem-level clean-room and adversarial
  audits before changing this status.

### COMP-certified-bessel-pilot-round17: Independently checked face-connected Round 17 shell certificate

- Status: `certified`
- Track: `certified_computation`
- Owner: `A4`
- Criticality: `standard`
- Lead author: `A4`
- Adversarial reviewer: `B1-independent-auditor`
- Next action: Retain $B_1$ as an independent regression certificate. Do
  not use it to enlarge the analytic mask or promote the parent computation;
  any later certificate must target an exact subset of $\mathcal D_{17}$.

### COMP-certified-bessel-pilot-round8: Independently checked shell-determinant certificate on one central residual box

- Status: `certified`
- Track: `certified_computation`
- Owner: `A4`
- Criticality: `standard`
- Lead author: `A4`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A2`
- Next action: Retain $B_0$ byte-unchanged as independently certified
  regression evidence. It is analytically redundant after Round 17 and must
  not be counted as an additional reduction of $\mathcal D_{17}$.
