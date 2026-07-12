# Reading Packet

Generated after round 2 in run `polya-main`.

## Current Theorem Target

Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

Current status: initialization/audit only. No new Pólya theorem has been proved.

## Current Route

Prove N_D(Omega,Lambda) <= L_d |Omega| Lambda^{d/2} for all Lambda >= 0 for at least one new natural non-tiling Euclidean domain class, with Dirichlet boundary conditions and a fixed counting convention.

## Active Bottleneck

`TARGET-shell-d3`: open.

For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9 pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for all K>=0.

Current blockers:
- `SHELL-lattice-count` (open): Multiplicity-weighted lattice count below shell phase curves
- `COMP-certified-bessel` (diagnostic_only): Certified finite-window verification for Bessel cross-products
- `SHELL-rho-uniformity` (open): Uniformity in shell ratio rho
- `SHELL-fixed-rho-high-energy` (open): Fixed-rho high-energy shell Polya estimate

## Round Target Obligations

- `SHELL-weighted-lattice-fractional` (open, owner `A2`): Multiplicity-weighted lattice bound for the 3D shell phase count
  Next action: Prove or falsify the exact weighted inequality using G_K-F_{rho K}; compute the full weighted contribution of the 1/4 slack before attempting asymptotic simplification.
- `COMP-certified-bessel` (diagnostic_only, owner `A4`): Certified finite-window verification for Bessel cross-products
  Next action: Build an interval/ball root-isolation successor using the proved monotone phase structure; retain diagnostic_only until rigorous coverage and metadata gates pass.

## Do-Not-Claim Rules

- Do not claim the shell theorem, ellipse theorem, or certificate-family theorem has been proved.
- Floating-point and symbolic computation are diagnostic only; interval/formal certification discharges only an explicit finite computation obligation.
- Do not use external theorems as proof dependencies without completed source cards.
- Do not promote a bottleneck without exact proof evidence, a clean-room reconstruction, and an adversarial-review artifact.

## Obligation Roles

Use `state/next_round_prompts.md` for role-specific tasks selected from the graph.

Current functional split:
- `A1`: project lead, obligation mapping, proof integration, and State Patch authoring.
- `A2`: incumbent analytic proof author for the selected bottleneck.
- `A3`: clean-room reconstruction from a reduced packet with no incumbent proof.
- `A4`: adversarial referee and certified-computation engineer.
- Only assigned reviewers receive peer outputs; universal all-agent cross-review is not required.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `problems/polya_conjecture.md`
- `sources/flps_balls.md`
- `sources/annuli_polya.md`
- `sources/bessel_phase_enclosures.md`
- `sources/shell_weyl_bessel.md`
- `manifests/reading_packet.md`

## Last State Patch

Round 2 closed the Bessel phase prerequisite chain; the weighted lattice fractional-part estimate remains the primary bottleneck.

## Active Obligation Briefs

### SHELL-weighted-lattice-fractional: Multiplicity-weighted lattice bound for the 3D shell phase count

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Criticality: `bottleneck`
- Lead author: `A2`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Next action: Prove or falsify the exact weighted inequality using G_K-F_{rho K}; compute the full weighted contribution of the 1/4 slack before attempting asymptotic simplification.

### COMP-certified-bessel: Certified finite-window verification for Bessel cross-products

- Status: `diagnostic_only`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Build an interval/ball root-isolation successor using the proved monotone phase structure; retain diagnostic_only until rigorous coverage and metadata gates pass.

### CERT-certificate-family: Fallback target: certified non-tiling comparison family

- Status: `open`
- Track: `certificate_family`
- Owner: `A3`
- Blockers: `SRC-jiang-lin`
- Next action: Keep as a fallback route. Do not mark blocked. First complete SRC-jiang-lin before proposing a concrete family or exact certificate theorem.

### ELLIPSE-near-circular: Parallel flagship target: Dirichlet Pólya for near-circular ellipses

- Status: `open`
- Track: `ellipse_parallel`
- Owner: `A3`
- Blockers: `SRC-mathieu-ellipse`
- Next action: Keep as a parallel flagship track. Do not mark blocked. Next useful action is source-auditing Mathieu characteristic values, small-eccentricity perturbation, and certified eigenvalue enclosures after the shell Round 2 core tasks are assigned.

### FLPS-disk-ball-reproduction: Reproduce the FLPS disk/ball proof architecture

- Status: `open`
- Track: `flps_reproduction`
- Owner: `A2`
- Blockers: `SRC-FLPS-balls`
- Next action: Draft a reproduction checklist with formulas, theorem dependencies, and verification scripts to import or reimplement; keep it as infrastructure until source cards exist.

### POLYA-program-target: Program target: exact Dirichlet Pólya for a new non-tiling Euclidean class

- Status: `open`
- Track: `target_conventions`
- Owner: `A1`
- Blockers: `SHELL-lattice-count`, `COMP-certified-bessel`
- Next action: Keep the global program target open while Round 1 sharpens the first theorem statement and proof-obligation graph.

### SHELL-cross-product-formula: Dirichlet shell spectral decomposition and Bessel cross-product formula

- Status: `open`
- Track: `shell_analytic`
- Owner: `A4`
- Blockers: `SHELL-sturm-liouville-completeness`
- Next action: Complete the Sturm-Liouville and spherical-harmonic proof; do not require absence of accidental equality across ell, only correct multiplicity summation.

### SHELL-fixed-rho-high-energy: Fixed-rho high-energy shell Polya estimate

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-weighted-lattice-fractional`
- Next action: Await the weighted lattice gate; the phase enclosure is now discharged, but no high-energy Pólya inequality has been proved.

### SHELL-inner-turning: Inner-boundary turning regime for shell phase differences

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Defer a new Airy enclosure. First test whether FLPS annuli Lemma 5.2, including the global bound on rho K<nu<=K and the correlated 1/4 bound on nu<=rho K, closes the weighted lattice estimate.

### SHELL-lattice-count: Multiplicity-weighted lattice count below shell phase curves

- Status: `open`
- Track: `shell_analytic`
- Owner: `A3`
- Blockers: `SHELL-weighted-lattice-fractional`
- Next action: Treat SHELL-weighted-lattice-fractional as the sole active analytic blocker and preserve strict endpoint counting.

### SHELL-phase-evanescent: Mixed and fully evanescent shell phase control

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Use the global one-sided annulus bound first; seek a sharper evanescent estimate only if the weighted-lattice margin fails.

### SHELL-phase-oscillatory: Shell phase enclosure in the ordinary oscillatory regime

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Treat as a fallback sharpening obligation only if the transferred annulus phase bound lacks sufficient weighted-lattice margin.

### SHELL-phase-outer-turning: Shell phase enclosure at the outer turning point

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Treat as a fallback sharpening obligation only if the transferred annulus phase bound lacks sufficient weighted-lattice margin.

### SHELL-phase-overlap: Compatibility and complete coverage of shell phase regimes

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A1`
- Criticality: `bottleneck`
- Lead author: `A1`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Blockers: `SHELL-phase-oscillatory`, `SHELL-phase-outer-turning`, `SHELL-inner-turning`, `SHELL-phase-evanescent`
- Next action: The transferred global bound removes regime-coverage gaps at the present precision. Reactivate only if fallback regime sharpenings are introduced.

### SHELL-rho-compact: Uniform shell estimates on compact rho intervals

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-lattice-count`, `SHELL-fixed-rho-high-energy`, `COMP-certified-bessel`
- Next action: After the fixed-rho proof is explicit, identify every rho-dependent constant and formulate a finite subdivision and interval-Lipschitz certificate.

### SHELL-rho-one-endpoint: Thin-shell endpoint rho -> 1

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `COMP-certified-bessel`
- Next action: Choose thin-shell variables, derive the leading radial quantization with explicit remainder, and state the overlap with compact-rho estimates.

### SHELL-rho-uniformity: Uniformity in shell ratio rho

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-rho-compact`, `SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`
- Next action: Keep the integration obligation deferred until compact-rho, small-hole, and thin-shell obligations are separately discharged and their parameter intervals cover all 0<rho<1.

### SHELL-rho-zero-endpoint: Small-hole endpoint rho -> 0

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-FLPS-balls`, `COMP-certified-bessel`
- Next action: Derive an explicit small-hole comparison or phase limit and identify a rho_0 with a certifiable residual window.

### SHELL-spherical-bessel-algebraic: Elementary spherical-Bessel form of half-integer shell cross-products

- Status: `open`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Promote only after the all-ell recurrence identity and its numerical-conditioning domain are proved; current low-order tests remain diagnostic.

### SHELL-sturm-liouville-completeness: Sturm-Liouville completeness for the separated shell spectrum

- Status: `open`
- Track: `shell_analytic`
- Owner: `A4`
- Next action: Write the full separation-of-variables and regular Sturm-Liouville proof, including no k=0 eigenvalue, positivity of roots, radial simplicity, and harmless cross-ell degeneracy.
