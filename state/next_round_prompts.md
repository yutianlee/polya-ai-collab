# Next Round Prompts

Generated after round 1 in run `polya-main`.

Source judge synthesis: `rounds/polya-main/round_001/judge/judge-001.md`.

## For A1

Build the Round 2 source-card foundation. Prioritize `SRC-bessel-phase`, `SRC-annuli`, `SRC-shell-weyl`, and `SRC-FLPS-balls`.

For `SRC-bessel-phase`, record exact statements for the Bessel phase/modulus convention, Wronskian sign, `theta_nu'(z)=2/(pi z M_nu(z)^2)`, Nicholson's formula, strict decrease of `M_nu(z)^2=J_nu(z)^2+Y_nu(z)^2`, validity ranges in `nu` and `z`, and Airy transition enclosures. State whether individual phase bounds can be differenced in the shell cross-product without losing the needed one-sided direction.

For `SRC-annuli`, extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal/floor-sum lemmas, finite verification strategy, and exactly which lemmas rely on planar multiplicity rather than a `2ell+1` weight.

For `SRC-shell-weyl`, record the shell cross-product zero-counting and Weyl-remainder statements, including explicitness, one-sidedness, boundary conditions, and dimension range.

Do not claim any shell, ellipse, or certificate-family theorem.

## For A2

Formalize the shell phase scaffold. Write a lemma package for:

1. `SHELL-exact-phase-rep`;
2. `SHELL-phase-monotonicity` conditional on Nicholson;
3. `SHELL-count-floor-identity` with strict endpoint rule;
4. `SHELL-inner-turning`.

For the phase-count identity, do not state equality with the floor at endpoints. Use the strict count `#{n>=1: n pi < Psi_{ell+1/2,rho}(K)}`.

For `SHELL-inner-turning`, state a precise Airy-scale proposition for `rho k - nu = O(nu^{1/3})` and identify exactly which constants and one-sided errors must be inherited or rebuilt from the Bessel phase source card. End with a fixed-rho high-energy proposition template that separates phase hypotheses from lattice hypotheses.

Do not claim the high-energy Polya estimate yet.

## For A3

Attack `SHELL-weighted-lattice-fractional` and refine `SHELL-lattice-count`.

Assume a black-box phase-count formula and explicit one-sided bounds for `Psi_{ell+1/2,rho}(K)`. Formulate the exact weighted discrete inequality needed to prove

`sum_{ell>=0}(2ell+1) #{n>=1: n pi < Psi_{ell+1/2,rho}(K)} <= (2/(9 pi))(1-rho^3)K^3`

for fixed `rho` and large `K`.

Audit which annulus floor-sum lemmas transfer and which fail because of the weight `2ell+1`. Compare two possible high-energy mechanisms: fractional-part lower bounds versus a floor-free phase-sum bound with an explicit negative boundary margin. Reject toy diagnostics that do not use the shell phase.

Also run the exact-root signed-defect scan for `rho` in `{0.1, 0.5, 0.9}` and report whether the worst defect drifts to the inner-transition band. Keep ellipse/certificate parallel, not blocked.

## For A4

Complete the formula/computation audit in executable form.

First, write the proof skeleton for `SHELL-sturm-liouville-completeness`: spherical-harmonic decomposition, radial regular Sturm-Liouville problem on `[rho,1]`, determinant zeros, positive roots, no `k=0` eigenvalue, radial simplicity, and harmless cross-ell degeneracy.

Second, implement a diagnostic root-isolation prototype for `rho=1/2`, `ell=0,1,2`, and `0<k<20`. Compare raw Bessel interval evaluation with at least one stabilized method: phase representation, recurrence-scaled spherical Bessel evaluation, or the finite trigonometric-rational form. Output a script path, exact command, root intervals if available, counting table if available, and limitations.

Third, derive the spherical-Bessel algebraic form for `ell=0,1,2` and assess coefficient growth and conditioning. Treat all computation as diagnostic unless root-exclusion and root-isolation certificates are rigorous.

## Round Assessment

Round 1 succeeded as a target-formation and blocker-isolation round. It did not prove any Polya theorem and did not justify promoting `TARGET-shell-d3`. It did establish a more coherent shell route:

- the theorem target is now explicit and normalized;
- strict counting is fixed;
- the shell spectral formula has strong audit support but still needs completeness proof;
- the exact phase representation is the most valuable new structural scaffold;
- Nicholson monotonicity is the key source-card item for phase monotonicity;
- the inner turning point and the `2ell+1` weighted lattice count are the two central analytic blockers;
- certified computation requirements are clear and remain diagnostic.

Split scores in prose:

- **A1: idea 8, state evidence 8.5, calibration 9.** Best state-promotable output: strict-counting equivalence, endpoint discipline, source prioritization, and the correction that cross-ell degeneracy must not be required.
- **A2: idea 9, state evidence 8, calibration 9.** The round's key structural scaffold: exact phase, Nicholson monotonicity, floor identity, angular cutoff, midpoint quadrature, and the floor-free high-energy mechanism. No theorem overclaim.
- **A3: idea 8, state evidence 4.5, calibration 5.** The spherical-Bessel elementary form and 2D-weight risk isolation are valuable, but the Stage A blocked statuses and toy fractional-part diagnostic are rejected. A3's Stage B review was better calibrated.
- **A4: idea 8, state evidence 7, calibration 8.5.** Rigorous formula confirmation, completeness requirement, and scoped computation target. Deductions only for patch-level formatting defects and over-broad overwrite attempts.

The proof-graph-safe `mathematical_progress_score` is 3/10. The idea quality is much higher than the theorem progress, which is exactly why the state patch creates obligations rather than promotes the main theorem.
