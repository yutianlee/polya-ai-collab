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

- `SHELL-phase-oscillatory` (open, owner `A2`): Shell phase enclosure in the ordinary oscillatory regime
  Next action: State a quantitative domain separated from both turning layers and derive the required one-sided differenced phase bound with explicit constants.
- `SHELL-phase-outer-turning` (open, owner `A2`): Shell phase enclosure at the outer turning point
  Next action: Formulate the Airy-scale outer-turning enclosure with explicit constants, error direction, and a declared finite small-order remainder.
- `SHELL-inner-turning` (open, owner `A2`): Inner-boundary turning regime for shell phase differences
  Next action: Formulate the Airy-scale statement precisely and test whether FLPS single-Bessel Airy bounds survive subtraction in theta_nu(k)-theta_nu(rho k).
- `SHELL-phase-evanescent` (open, owner `A2`): Mixed and fully evanescent shell phase control
  Next action: Prove a zero-exclusion or one-sided count bound in each evanescent subregion and state how it overlaps the Airy regimes.
- `SHELL-phase-overlap` (open, owner `A1`): Compatibility and complete coverage of shell phase regimes
  Next action: After the four regime lemmas are explicit, build a coverage table and give it independently to A3 before A4 audits both constructions.
- `SHELL-phase-enclosures` (open, owner `A2`): Uniform phase enclosures for Bessel cross-product zeros
  Next action: Integrate only after each regime obligation and the overlap obligation have explicit one-sided bounds. Give A3 a clean-room lemma packet without the incumbent proof, then give both frozen attempts to A4 for adversarial audit.
- `COMP-certified-bessel` (diagnostic_only, owner `A4`): Certified finite-window verification for Bessel cross-products
  Next action: Implement a minimal diagnostic root-isolation prototype for rho=1/2, ell=0,1,2, 0<k<20. Compare raw Bessel interval evaluation against phase-based, recurrence-scaled, and spherical-Bessel algebraic evaluation. Add exact-root signed-defect, thin-shell, small-hole, and stability diagnostics, but treat all outputs as diagnostic.

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

Workflow revised after round 1: obligation-specific roles, clean-room review, adversarial audit, and certification classes are now active. No mathematical claim was promoted.

## Active Obligation Briefs

### SHELL-phase-oscillatory: Shell phase enclosure in the ordinary oscillatory regime

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`
- Next action: State a quantitative domain separated from both turning layers and derive the required one-sided differenced phase bound with explicit constants.

### SHELL-phase-outer-turning: Shell phase enclosure at the outer turning point

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`
- Next action: Formulate the Airy-scale outer-turning enclosure with explicit constants, error direction, and a declared finite small-order remainder.

### SHELL-inner-turning: Inner-boundary turning regime for shell phase differences

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`, `SRC-shell-weyl`
- Next action: Formulate the Airy-scale statement precisely and test whether FLPS single-Bessel Airy bounds survive subtraction in theta_nu(k)-theta_nu(rho k).

### SHELL-phase-evanescent: Mixed and fully evanescent shell phase control

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SRC-bessel-phase`
- Next action: Prove a zero-exclusion or one-sided count bound in each evanescent subregion and state how it overlaps the Airy regimes.

### SHELL-phase-overlap: Compatibility and complete coverage of shell phase regimes

- Status: `open`
- Track: `shell_analytic`
- Owner: `A1`
- Criticality: `bottleneck`
- Lead author: `A1`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Blockers: `SHELL-phase-oscillatory`, `SHELL-phase-outer-turning`, `SHELL-inner-turning`, `SHELL-phase-evanescent`
- Next action: After the four regime lemmas are explicit, build a coverage table and give it independently to A3 before A4 audits both constructions.

### SHELL-phase-enclosures: Uniform phase enclosures for Bessel cross-product zeros

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Criticality: `bottleneck`
- Lead author: `A2`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Blockers: `SRC-bessel-phase`, `SRC-annuli`, `SRC-shell-weyl`, `SHELL-phase-oscillatory`, `SHELL-phase-outer-turning`, `SHELL-inner-turning`, `SHELL-phase-evanescent`, `SHELL-phase-overlap`
- Next action: Integrate only after each regime obligation and the overlap obligation have explicit one-sided bounds. Give A3 a clean-room lemma packet without the incumbent proof, then give both frozen attempts to A4 for adversarial audit.

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
- Blockers: `SHELL-phase-enclosures`, `SHELL-inner-turning`, `SHELL-weighted-lattice-fractional`
- Next action: State the first black-box fixed-rho theorem with exact phase hypotheses, lattice hypotheses, and a computable analytic threshold K_0(rho).

### SHELL-lattice-count: Multiplicity-weighted lattice count below shell phase curves

- Status: `open`
- Track: `shell_analytic`
- Owner: `A3`
- Blockers: `SHELL-phase-enclosures`, `SHELL-weighted-lattice-fractional`
- Next action: Replace the broad lattice target with a precise black-box theorem: assuming explicit one-sided phase bounds, prove the 2ell+1 weighted count is below (2/(9 pi))(1-rho^3)K^3 in the fixed-rho high-energy range.

### SHELL-rho-compact: Uniform shell estimates on compact rho intervals

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-phase-enclosures`, `SHELL-lattice-count`, `SHELL-fixed-rho-high-energy`, `COMP-certified-bessel`
- Next action: After the fixed-rho proof is explicit, identify every rho-dependent constant and formulate a finite subdivision and interval-Lipschitz certificate.

### SHELL-rho-one-endpoint: Thin-shell endpoint rho -> 1

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-phase-enclosures`, `COMP-certified-bessel`
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
- Blockers: `SHELL-phase-enclosures`, `SRC-FLPS-balls`, `COMP-certified-bessel`
- Next action: Derive an explicit small-hole comparison or phase limit and identify a rho_0 with a certifiable residual window.

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
