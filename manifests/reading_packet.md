# Reading Packet

Generated after round 15 in run `polya-main`.

## Current Theorem Target

Target: exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

Current status: no complete all-rho Pólya theorem has been proved. The exact d=3 spectrum, fixed-rho high-energy theorem, both uniform rho-endpoint neighborhoods (with rho>=99/100 on the thin side), and the all-rho analytic range K>=200000 are proved. The central--thin seam is rho=5/6 with K_0(5/6)<295^2=87025. One central residual box is certified; exact coverage of the true nonrectangular compact residual and the final theorem audit remain open.

## Current Route

Prove N_D(Omega,Lambda) <= L_d |Omega| Lambda^{d/2} for all Lambda >= 0 for at least one new natural non-tiling Euclidean domain class, with Dirichlet boundary conditions and a fixed counting convention.

## Active Bottleneck

`TARGET-shell-d3`: open.

For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9 pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for all K>=0.

Current blockers:
- `COMP-certified-bessel` (diagnostic_only): Certified finite-window verification for Bessel cross-products
- `SHELL-rho-uniformity` (open): Uniformity in shell ratio rho

## Round Target Obligations

- `SHELL-rho-one-endpoint` (proved_internal, owner `A2`): Thin-shell endpoint rho -> 1
  Next action: Round 16 primary target, explicitly unproved: independently derive and audit a two-piece all-frequency endpoint proof on 7/8<=rho<1, split at a=pi/(4 epsilon), while retaining 99/100<=rho<1 as the only accepted endpoint until promotion. The product and complementary-action pieces must both own the common face; stretch screens below rho=7/8 remain planning evidence only.
- `SHELL-rho-compact` (open, owner `A2`): Uniform shell estimates on compact rho intervals
  Next action: Keep this obligation open until exact analytic or certified coverage closes the true residual on I_15 below K=200000. Do not replace the piecewise complement of the accepted seven-zone cover by a rectangular sweep.
- `COMP-certified-bessel` (diagnostic_only, owner `A4`): Certified finite-window verification for Bessel cross-products
  Next action: The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_15 with K<200000; the Round 15 exact rational ledgers are symbolic analytic evidence, not Bessel-root certificates.

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

updated: SHELL-central-thin-seam-compression, SHELL-rho-compact-analytic-envelope, SHELL-rho-compact, COMP-certified-bessel, SHELL-rho-uniformity, TARGET-shell-d3; no_change: SHELL-rho-zero-endpoint, SHELL-rho-one-endpoint, SHELL-fixed-rho-high-energy, COMP-certified-bessel-pilot-round8, SHELL-rho-compact, COMP-certified-bessel, SHELL-rho-uniformity, TARGET-shell-d3; round score: 6; Round 15 moves the central--thin seam from rho=7/8 to rho=5/6 and lowers the complete all-ratio high-frequency ceiling from 550^2 to 200000 by the exact factor 121/80>1, but supplies no new certified residual coverage and does not enlarge the all-frequency endpoint.

## Active Obligation Briefs

### SHELL-rho-compact: Uniform shell estimates on compact rho intervals

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `COMP-certified-bessel`
- Next action: Keep this obligation open until exact analytic or certified coverage closes the true residual on I_15 below K=200000. Do not replace the piecewise complement of the accepted seven-zone cover by a rectangular sweep.

### COMP-certified-bessel: Certified finite-window verification for Bessel cross-products

- Status: `diagnostic_only`
- Track: `certified_computation`
- Owner: `A4`
- Next action: The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_15 with K<200000; the Round 15 exact rational ledgers are symbolic analytic evidence, not Bessel-root certificates.

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

### SHELL-rho-uniformity: Uniformity in shell ratio rho

- Status: `open`
- Track: `shell_analytic`
- Owner: `A2`
- Blockers: `SHELL-rho-compact`
- Next action: Both complete all-frequency endpoint neighborhoods and the all-ratio range K>=200000 are proved. Keep this obligation open until the compact residual below that ceiling is exactly closed.

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

### TARGET-shell-d3: First theorem target: Dirichlet Pólya for 3D spherical shells

- Status: `open`
- Track: `shell_analytic`
- Owner: `A1`
- Criticality: `theorem`
- Lead author: `A1`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A2`
- Blockers: `COMP-certified-bessel`, `SHELL-rho-uniformity`
- Next action: The strict shell inequality is proved for every ratio when K>=200000. Complete exact compact coverage below that ceiling, then run fresh theorem-level clean-room and adversarial audits.

### COMP-certified-bessel-pilot-round8: Independently checked shell-determinant certificate on one central residual box

- Status: `certified`
- Track: `certified_computation`
- Owner: `A4`
- Criticality: `standard`
- Lead author: `A4`
- Clean-room reviewer: `A3`
- Adversarial reviewer: `A2`
- Next action: Use this only as a validated schema and local pilot. Extend through an exact face-connected manifest only after analytic compression makes the remaining corner spectra tractable.
