# Reading Packet

Generated after round 5 in run `polya-main`.

## Current Theorem Target

Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

Current status: no complete Pólya theorem has been proved. The exact d=3 spectrum, fixed-rho high-energy theorem, and a uniform low-optical thin-shell window are proved; a radius-sensitive thin intermediate range, small-hole uniformity, and certified finite-window closure remain open.

## Current Route

Prove N_D(Omega,Lambda) <= L_d |Omega| Lambda^{d/2} for all Lambda >= 0 for at least one new natural non-tiling Euclidean domain class, with Dirichlet boundary conditions and a fixed counting convention.

## Active Bottleneck

`TARGET-shell-d3`: open.

For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9 pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for all K>=0.

Current blockers:
- `COMP-certified-bessel` (diagnostic_only): Certified finite-window verification for Bessel cross-products
- `SHELL-rho-uniformity` (open): Uniformity in shell ratio rho

## Round Target Obligations

- `SHELL-thin-curvature-intermediate` (open, owner `A2`): Radius-sensitive intermediate thin-shell estimate
  Next action: Develop a curvature-corrected comparison or a thin-scaled aggregate phase-lattice estimate. It must match the factor epsilon^{-1} int_{1-epsilon}^1 r^2 dr=1-epsilon+epsilon^2/3 and explicitly overlap either the proved low-optical range or K_0.
- `SHELL-rho-zero-endpoint` (open, owner `A2`): Small-hole endpoint rho -> 0
  Next action: Use the audited ball limit together with certified computation; the FLPS ball source audit is discharged.
- `COMP-certified-bessel` (diagnostic_only, owner `A4`): Certified finite-window verification for Bessel cross-products
  Next action: Do not attempt to certify the unbounded thin intermediate region. First close SHELL-thin-curvature-intermediate and the small-hole endpoint, then certify the resulting bounded residual boxes with strict root and floor walls.

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

Proved a uniform low-optical thin-shell window; exactly rejected the flat product majorant as a global endpoint route; created the radius-sensitive intermediate thin-shell bottleneck.

## Active Obligation Briefs

### SHELL-thin-curvature-intermediate: Radius-sensitive intermediate thin-shell estimate

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Criticality: `bottleneck`
- Lead author: `A2`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Next action: Develop a curvature-corrected comparison or a thin-scaled aggregate phase-lattice estimate. It must match the factor epsilon^{-1} int_{1-epsilon}^1 r^2 dr=1-epsilon+epsilon^2/3 and explicitly overlap either the proved low-optical range or K_0.

### SHELL-rho-zero-endpoint: Small-hole endpoint rho -> 0

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `COMP-certified-bessel`
- Next action: Use the audited ball limit together with certified computation; the FLPS ball source audit is discharged.

### COMP-certified-bessel: Certified finite-window verification for Bessel cross-products

- Status: `diagnostic_only`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Do not attempt to certify the unbounded thin intermediate region. First close SHELL-thin-curvature-intermediate and the small-hole endpoint, then certify the resulting bounded residual boxes with strict root and floor walls.

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
- Next action: Reproduce only the remaining proof infrastructure needed by active obligations; the FLPS ball source card is now audited.

### POLYA-program-target: Program target: exact Dirichlet Pólya for a new non-tiling Euclidean class

- Status: `open`
- Track: `target_conventions`
- Owner: `A1`
- Blockers: `COMP-certified-bessel`
- Next action: Keep the program target open until TARGET-shell-d3 passes rho-uniformity, finite certification, and final theorem-level clean-room review.

### SHELL-inner-turning: Inner-boundary turning regime for shell phase differences

- Status: `proposed`
- Track: `shell_analytic`
- Owner: `A2`
- Next action: Defer a new Airy enclosure. First test whether FLPS annuli Lemma 5.2, including the global bound on rho K<nu<=K and the correlated 1/4 bound on nu<=rho K, closes the weighted lattice estimate.

### SHELL-low-interface-shifted-tails: Shifted shell tails crossing the inner interface

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Criticality: `bottleneck`
- Lead author: `A2`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A4`
- Next action: The fixed-rho high-energy part is discharged and no longer blocks the weighted proxy. The unrestricted all-K strengthening remains open; finite theorem closure belongs to certified computation and endpoint analysis.

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
- Blockers: `COMP-certified-bessel`
- Next action: Use rho<=0.99 as the compact side of the new thin split. Bound K_0 on the chosen compact interval and formulate its bounded interval certificate; COMP-certified-bessel remains open.

### SHELL-rho-one-endpoint: Thin-shell endpoint rho -> 1

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `COMP-certified-bessel`, `SHELL-thin-curvature-intermediate`
- Next action: The actual shell inequality is proved for epsilon<=1/100 and K<=pi/(4 epsilon^2), while fixed-rho high energy starts only at K_0(1-epsilon). Close the radius-sensitive intermediate gap; the flat product majorant is rejected as a global route.

### SHELL-rho-uniformity: Uniformity in shell ratio rho

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-rho-compact`, `SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`
- Next action: The thin endpoint now has a proved low-optical range but an explicit unbounded intermediate gap. Close SHELL-thin-curvature-intermediate, then combine it with compact-rho and small-hole coverage.

### SHELL-spherical-bessel-algebraic: Elementary spherical-Bessel form of half-integer shell cross-products

- Status: `open`
- Track: `certified_computation`
- Owner: `A4`
- Next action: Promote only after the all-ell recurrence identity and its numerical-conditioning domain are proved; current low-order tests remain diagnostic.

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

### SRC-shell-weyl: Source audit: Bessel functions and Weyl law for balls and spherical shells

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: The structural spectrum component is audited. Audit only the unresolved quantitative Weyl remainder, endpoint-uniform constants, one-sided Polya-strength estimates, and finite-window certification scope.
