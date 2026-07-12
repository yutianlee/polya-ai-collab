# Reading Packet

Generated after round 1 in run `polya-main`.

## Current Theorem Target

Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

Current status: initialization/audit only. No new Pólya theorem has been proved.

## Current Route

Prove N_D(Omega,Lambda) <= L_d |Omega| Lambda^{d/2} for all Lambda >= 0 for at least one new natural non-tiling Euclidean domain class, with Dirichlet boundary conditions and a fixed counting convention.

## Active Bottleneck

`TARGET-shell-d3`: open.

For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9 pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for all K>=0.

Current blockers:
- `SHELL-phase-enclosures` (open): Uniform phase enclosures for Bessel cross-product zeros
- `SHELL-lattice-count` (open): Multiplicity-weighted lattice count below shell phase curves
- `COMP-certified-bessel` (diagnostic_only): Certified finite-window verification for Bessel cross-products
- `SHELL-rho-uniformity` (open): Uniformity in shell ratio rho
- `SHELL-fixed-rho-high-energy` (open): Fixed-rho high-energy shell Polya estimate

## Round Target Obligations

- `CONV-strict-counting` (proved_internal, owner `A1`): Strict Dirichlet counting convention
  Next action: Use this endpoint rule in all imported source statements, phase-count identities, eigenvalue formulations, and certified finite-window checks.
- `TARGET-shell-d3` (open, owner `A1`): First theorem target: Dirichlet Pólya for 3D spherical shells
  Next action: Keep the theorem open. First prove the fixed-rho high-energy estimate and a certified finite window; defer compact rho-uniformity and endpoint regimes.
- `SRC-FLPS-balls` (source_audit_required, owner `A1`): Source audit: FLPS Euclidean balls proof
  Next action: Create the source card for FLPS balls, disks, and sectors: theorem statements, boundary conditions, counting convention, Bessel phase definitions, lattice-counting lemmas, and computer-assisted components to reproduce before shell transfer.
- `SRC-annuli` (source_audit_required, owner `A1`): Source audit: Dirichlet Pólya for annuli
  Next action: Extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal and convex/concave floor-sum lemmas, finite verification strategy, and exactly which lemmas are dimension-independent versus planar-multiplicity dependent.
- `SHELL-cross-product-formula` (open, owner `A4`): Dirichlet shell spectral decomposition and Bessel cross-product formula
  Next action: Complete the Sturm-Liouville and spherical-harmonic proof; do not require absence of accidental equality across ell, only correct multiplicity summation.
- `SHELL-lattice-count` (open, owner `A3`): Multiplicity-weighted lattice count below shell phase curves
  Next action: Replace the broad lattice target with a precise black-box theorem: assuming explicit one-sided phase bounds, prove the 2ell+1 weighted count is below (2/(9 pi))(1-rho^3)K^3 in the fixed-rho high-energy range.
- `COMP-certified-bessel` (diagnostic_only, owner `A4`): Certified finite-window verification for Bessel cross-products
  Next action: Implement a minimal diagnostic root-isolation prototype for rho=1/2, ell=0,1,2, 0<k<20. Compare raw Bessel interval evaluation against phase-based, recurrence-scaled, and spherical-Bessel algebraic evaluation. Add exact-root signed-defect, thin-shell, small-hole, and stability diagnostics, but treat all outputs as diagnostic.

## Do-Not-Claim Rules

- Do not claim the shell theorem, ellipse theorem, or certificate-family theorem has been proved.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use external theorems as proof dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3/A4 tasks.

Default target split:
- `A1`: target theorem memo, source-card discipline, synthesis, and State Patch authoring.
- `A2`: conservative shell-route proof surgery and obstruction analysis.
- `A3`: route comparison and independent obstruction search.
- `A4`: API formula audit and certified-computation planning.

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

created: SHELL-sturm-liouville-completeness, SHELL-exact-phase-rep, SHELL-phase-monotonicity, SHELL-count-floor-identity, SHELL-angular-cutoff, SHELL-inner-turning, SHELL-fixed-rho-high-energy, SHELL-weighted-lattice-fractional, SHELL-spherical-bessel-algebraic; updated: CONV-strict-counting, TARGET-shell-d3, SHELL-cross-product-formula, SRC-bessel-phase, SRC-annuli, SRC-shell-weyl, SRC-FLPS-balls, FLPS-disk-ball-reproduction, SHELL-phase-enclosures, SHELL-lattice-count, COMP-certified-bessel, SHELL-rho-uniformity, ELLIPSE-near-circular, CERT-certificate-family; rejected: A3-proposed-blocked-statuses, toy-weighted-fractional-test, raw-floating-point-computation-as-proof, bare-two-term-weyl-proof, judge1-progress-score-7; no_change: POLYA-program-target, SRC-mathieu-ellipse, SRC-jiang-lin; round score: 3; Structural de-risking only: exact monotone phase scaffold, a proved angular cutoff, and a proved counting convention; no shell Polya theorem and both quantitative blockers, inner-turning enclosure and 2D weighted lattice control, remain open. The final synthesis adopts judge2 calibration while importing judge1 completeness and diagnostic coverage.

## Active Obligation Briefs

### TARGET-shell-d3: First theorem target: Dirichlet Pólya for 3D spherical shells

- Status: `open`
- Track: `shell_analytic`
- Owner: `A1`
- Blockers: `SHELL-phase-enclosures`, `SHELL-lattice-count`, `COMP-certified-bessel`, `SHELL-rho-uniformity`, `SHELL-fixed-rho-high-energy`
- Next action: Keep the theorem open. First prove the fixed-rho high-energy estimate and a certified finite window; defer compact rho-uniformity and endpoint regimes.

### SRC-FLPS-balls: Source audit: FLPS Euclidean balls proof

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Create the source card for FLPS balls, disks, and sectors: theorem statements, boundary conditions, counting convention, Bessel phase definitions, lattice-counting lemmas, and computer-assisted components to reproduce before shell transfer.

### SRC-annuli: Source audit: Dirichlet Pólya for annuli

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal and convex/concave floor-sum lemmas, finite verification strategy, and exactly which lemmas are dimension-independent versus planar-multiplicity dependent.

### SHELL-cross-product-formula: Dirichlet shell spectral decomposition and Bessel cross-product formula

- Status: `open`
- Track: `shell_analytic`
- Owner: `A4`
- Blockers: `SHELL-sturm-liouville-completeness`
- Next action: Complete the Sturm-Liouville and spherical-harmonic proof; do not require absence of accidental equality across ell, only correct multiplicity summation.

### SHELL-lattice-count: Multiplicity-weighted lattice count below shell phase curves

- Status: `open`
- Track: `shell_analytic`
- Owner: `A3`
- Blockers: `SHELL-phase-enclosures`, `SHELL-weighted-lattice-fractional`
- Next action: Replace the broad lattice target with a precise black-box theorem: assuming explicit one-sided phase bounds, prove the 2ell+1 weighted count is below (2/(9 pi))(1-rho^3)K^3 in the fixed-rho high-energy range.

### COMP-certified-bessel: Certified finite-window verification for Bessel cross-products

- Status: `diagnostic_only`
- Track: `certified_computation`
- Owner: `A4`
- Blockers: `SHELL-phase-enclosures`
- Next action: Implement a minimal diagnostic root-isolation prototype for rho=1/2, ell=0,1,2, 0<k<20. Compare raw Bessel interval evaluation against phase-based, recurrence-scaled, and spherical-Bessel algebraic evaluation. Add exact-root signed-defect, thin-shell, small-hole, and stability diagnostics, but treat all outputs as diagnostic.

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
- Blockers: `SRC-FLPS-balls`, `SRC-bessel-phase`
- Next action: Draft a reproduction checklist with formulas, theorem dependencies, and verification scripts to import or reimplement; keep it as infrastructure until source cards exist.

### POLYA-program-target: Program target: exact Dirichlet Pólya for a new non-tiling Euclidean class

- Status: `open`
- Track: `target_conventions`
- Owner: `A1`
- Blockers: `SHELL-phase-enclosures`, `SHELL-lattice-count`, `COMP-certified-bessel`
- Next action: Keep the global program target open while Round 1 sharpens the first theorem statement and proof-obligation graph.

### SHELL-fixed-rho-high-energy: Fixed-rho high-energy shell Polya estimate

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-phase-enclosures`, `SHELL-inner-turning`, `SHELL-weighted-lattice-fractional`
- Next action: State the first black-box fixed-rho theorem with exact phase hypotheses, lattice hypotheses, and a computable analytic threshold K_0(rho).

### SHELL-inner-turning: Inner-boundary turning regime for shell phase differences

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`, `SRC-shell-weyl`
- Next action: Formulate the Airy-scale statement precisely and test whether FLPS single-Bessel Airy bounds survive subtraction in theta_nu(k)-theta_nu(rho k).

### SHELL-phase-enclosures: Uniform phase enclosures for Bessel cross-product zeros

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`, `SRC-annuli`, `SRC-shell-weyl`, `SHELL-inner-turning`
- Next action: For fixed rho, formulate quantitative one-sided enclosures for Psi_{nu,rho}(k) in oscillatory, outer-turning, inner-turning, mixed evanescent/oscillatory, and fully evanescent regimes; explicitly track differencing loss.

### SHELL-rho-uniformity: Uniformity in shell ratio rho

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-phase-enclosures`, `COMP-certified-bessel`
- Next action: Keep rho-uniformity deferred. After fixed-rho high-energy and finite-window methods are formulated, separately plan compact rho intervals, rho->0 small-hole behavior, and rho->1 thin-shell behavior.

### SHELL-spherical-bessel-algebraic: Elementary spherical-Bessel form of half-integer shell cross-products

- Status: `open`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Derive ell=0,1,2 explicitly; check whether only sin((1-rho)k) and cos((1-rho)k) remain after cancellation; estimate coefficient growth and conditioning.

### SHELL-sturm-liouville-completeness: Sturm-Liouville completeness for the separated shell spectrum

- Status: `open`
- Track: `shell_analytic`
- Owner: `A4`
- Next action: Write the full separation-of-variables and regular Sturm-Liouville proof, including no k=0 eigenvalue, positivity of roots, radial simplicity, and harmless cross-ell degeneracy.

### SHELL-weighted-lattice-fractional: Multiplicity-weighted lattice bound for the 3D shell phase count

- Status: `open`
- Track: `shell_analytic`
- Owner: `A3`
- Blockers: `SHELL-phase-enclosures`, `SRC-annuli`
- Next action: Formulate the weighted inequality abstractly under black-box phase hypotheses; identify minimal monotonicity, convexity, and error assumptions; audit which annulus lemmas survive the 2ell+1 weight.

### SRC-bessel-phase: Source audit: uniform Bessel phase and zero enclosures

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Audit Bessel phase definitions, modulus positivity, Wronskian sign, theta_nu'=2/(pi z M_nu^2), Nicholson's formula and strict decrease of M_nu^2, validity for nu>=1/2 and z>0, Airy transition constants, and whether independent phase bounds can be safely differenced for shell cross-products.

### SRC-jiang-lin: Source audit: Jiang-Lin epsilon-loss and certificate strategy

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Create a source card before using Jiang-Lin as a proof dependency.

### SRC-mathieu-ellipse: Source audit: Mathieu-function tools for Dirichlet ellipses

- Status: `source_audit_required`
- Track: `ellipse_parallel`
- Owner: `A1`
- Next action: Keep this as a parallel source-audit track until the shell Round 1 target theorem memo is stable.
