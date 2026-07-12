## Selected main route

The accepted Round 1 judge synthesis uses `judge2-001.md` as the base, with targeted imports from `judge-001.md`.

The reason is calibration. All three comparison reports prefer `judge2-001.md`: it keeps the 3D shell route primary, identifies the exact monotone phase representation as the real Round 1 structural advance, and keeps `mathematical_progress_score` at 3/10 because no theorem was proved and the two quantitative blockers remain open. By contrast, `judge-001.md` is broader but over-scores proof progress at 7/10, contains web citation artifacts, and in one place makes a proved node depend on an open completeness node.

The final synthesis therefore adopts the `judge2-001.md` Layer 1 / Layer 2 architecture:

- Layer 1: exact shell phase representation, Nicholson-based monotonicity, strict endpoint floor-counting, angular cutoff, and Sturm-Liouville completeness as the formal spectral bridge.
- Layer 2: the fixed-rho high-energy estimate, driven by one-sided inner-turning phase control and the multiplicity-weighted lattice/floor-sum problem.

The following pieces are imported from `judge-001.md`: a standalone `SHELL-sturm-liouville-completeness` obligation, explicit next actions for `ELLIPSE-near-circular` and `CERT-certificate-family`, and the diagnostic checklist covering exact-root signed defects, thin-shell behavior, small-hole behavior, and stable root-isolation methods.

No Dirichlet Polya theorem is claimed or promoted in Round 1.

## Useful fragments by source

**A1.** A1 gives the safest target-theorem framing: strict counting, the 3D shell constant, source-audit ordering, and the warning that cross-ell degeneracy is harmless when multiplicities are summed in the orthogonal direct-sum decomposition. A1's broader obligation list is useful, but not all of it should be promoted at once.

**A2.** A2 supplies the key structural advance: the shell cross-product can be represented by a phase difference

`Psi_{nu,rho}(k) = theta_nu(k) - theta_nu(rho k)`,

and Nicholson monotonicity should make this phase difference globally increasing after the source card fixes conventions. A2 also identifies the midpoint-quadrature advantage of half-integer orders `nu=ell+1/2`, which is a promising route to the fixed-rho high-energy estimate.

**A3.** A3 correctly warns that the annulus floor-sum does not transfer automatically to the 3D shell because the factor `2ell+1` turns the sum into a genuine multiplicity-weighted two-parameter problem. A3 also proposes exploiting elementary spherical-Bessel formulas in dimension 3. Those ideas are valuable, but A3's proposed `blocked` statuses are rejected as premature.

**A4.** A4 confirms the shell eigenvalue equation, multiplicity, Weyl normalization, and the need for a certified finite-window plan. A4 also correctly insists that computation remains diagnostic until it produces a script, exact command, root enclosures, a counting table, and limitations. The old A4 review was rerun after the updated A3 response, so the final comparison uses the refreshed A4 review.

**Judge comparisons.** The comparison files converge on the same decision: adopt `judge2-001.md`, keep progress conservative, add the missing completeness obligation from `judge-001.md`, keep ellipse and certificate tracks open, and soften any wording that suggests Layer 1 is already fully proved before source-card and completeness checks.

## Rejected or risky ideas

- Reject A3's proposed `blocked` status for `SHELL-lattice-count`, `ELLIPSE-near-circular`, and `CERT-certificate-family`. The risks are real, but no impossibility or counterexample was proved.
- Reject the toy fractional-part proxy that replaces the actual shell phase by a simpler expression. It is not proof-relevant unless it is tied to a rigorously stated WKB phase with explicit error.
- Reject any use of raw floating-point root tables as proof.
- Reject naive interval evaluation of the Bessel cross-product as the default certified-computation path. It may suffer catastrophic cancellation at large order.
- Reject a bare two-term Weyl-law threshold argument without explicit one-sided constants and a certified compact-window closure.
- Reject the inflated Round 1 progress score of 7/10 from `judge-001.md`; the proof-graph-safe score is 3/10.

## Known gaps

1. `SHELL-sturm-liouville-completeness` is not yet written. The project still needs the formal separated-spectrum proof: angular decomposition, radial regular Sturm-Liouville problem on `[rho,1]`, determinant zeros, positivity of roots, no `k=0` eigenvalue, radial simplicity, and harmless cross-ell degeneracy.
2. `SRC-bessel-phase` is not carded. Nicholson's formula, the modulus/phase convention, Wronskian sign, phase derivative, validity range, and branch normalization must be documented before monotonicity is promoted.
3. `SHELL-inner-turning` is the hardest special-function region. Independent single-Bessel phase enclosures may lose one-sided control when differenced.
4. `SHELL-weighted-lattice-fractional` is genuinely open. The `2ell+1` weight is the central analytic obstruction.
5. `SHELL-fixed-rho-high-energy` remains a plan, not a proof. The midpoint-quadrature and negative-boundary-term mechanism is promising but must be made quantitative.
6. `COMP-certified-bessel` is diagnostic only. No certified finite-window computation has been committed.
7. Ellipse and certificate tracks remain useful parallel tracks but have not yet produced proof dependencies.

## New lemmas to add

The graph should add the following shell obligations:

- `SHELL-sturm-liouville-completeness`
- `SHELL-exact-phase-rep`
- `SHELL-phase-monotonicity`
- `SHELL-count-floor-identity`
- `SHELL-angular-cutoff`
- `SHELL-inner-turning`
- `SHELL-fixed-rho-high-energy`
- `SHELL-weighted-lattice-fractional`
- `SHELL-spherical-bessel-algebraic`

The most important dependency correction is that `SHELL-angular-cutoff` is proved by a direct Rayleigh quotient estimate and should not depend on the open Sturm-Liouville completeness obligation.

## Counterexample and diagnostic checks

Round 2 should run diagnostics only where they sharpen analytic obligations:

1. Exact-root signed-defect scans for `rho` in `{0.1, 0.5, 0.9}` over growing `K`, using the true shell phase or exact roots, not the toy proxy.
2. A scan of where the worst defect occurs: low ell, the inner-transition band `rho K ~= ell+1/2`, or near the angular cutoff.
3. Thin-shell diagnostics for `rho=1-h`, compared against the expected product-like behavior.
4. Small-hole diagnostics for `rho=0.1, 0.01, 0.001`, compared against the ball limit and volume loss.
5. Stability diagnostics comparing raw cross-product evaluation against phase/modulus, recurrence-scaled spherical-Bessel, and elementary trigonometric-rational forms.

These diagnostics do not prove the theorem. Their role is to expose likely failure modes and guide which inequalities must be made rigorous.

## Research strategy adjustment

Keep the shell theorem as the primary Round 2 target, but narrow the work to separately testable obligations. A1 should close source-card gaps. A2 should formalize the phase scaffold and attack the inner-turning estimate. A3 should make the weighted lattice problem precise under black-box phase hypotheses. A4 should write the completeness proof skeleton and build a minimal diagnostic computation.

Do not broaden the search in Round 2. Ellipse and certificate-family tracks remain alive, but only as source-audit and fallback tracks until the shell Layer 2 blockers have been tested.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-sturm-liouville-completeness",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Sturm-Liouville completeness for the separated shell spectrum",
        "status": "open",
        "statement_tex": "For A_{rho,1} in R^3, the Dirichlet Laplacian decomposes into spherical-harmonic angular momentum channels. In each ell channel the regular radial Sturm-Liouville problem on [rho,1] has positive simple radial eigenvalues exactly given by positive zeros of F_{ell+1/2,rho}(k). Accidental equality of eigenvalues across different ell is harmless because multiplicities are summed over the orthogonal direct-sum decomposition.",
        "dependencies": ["CONV-strict-counting"],
        "implies": ["SHELL-cross-product-formula", "SHELL-count-floor-identity", "COMP-certified-bessel"],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/responses/A4-001.md", "rounds/polya-main/round_001/reviews/A1.md"]
        },
        "owner": "A4",
        "next_action": "Write the full separation-of-variables and regular Sturm-Liouville proof, including no k=0 eigenvalue, positivity of roots, radial simplicity, and harmless cross-ell degeneracy."
      },
      {
        "id": "SHELL-exact-phase-rep",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Exact Bessel cross-product phase factorization",
        "status": "derived_under_assumptions",
        "statement_tex": "For a fixed Bessel phase/modulus convention J_nu=M_nu cos(theta_nu), Y_nu=M_nu sin(theta_nu), with M_nu(z)>0 for z>0, the shell determinant satisfies F_{nu,rho}(k)=M_nu(rho k) M_nu(k) sin(theta_nu(k)-theta_nu(rho k)), up to the fixed sign convention. Hence positive zeros of F_{nu,rho} occur exactly when Psi_{nu,rho}(k):=theta_nu(k)-theta_nu(rho k) lies in pi Z.",
        "dependencies": ["SHELL-cross-product-formula", "SRC-bessel-phase"],
        "implies": ["SHELL-count-floor-identity", "SHELL-phase-monotonicity", "SHELL-phase-enclosures"],
        "blockers": ["SRC-bessel-phase"],
        "evidence": {
          "positive": ["rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/reviews/A2.md"],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "next_action": "Source-card the phase/modulus definitions and Wronskian sign convention; then promote only after the convention is fixed."
      },
      {
        "id": "SHELL-phase-monotonicity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Global strict monotonicity of the shell phase difference",
        "status": "derived_under_assumptions",
        "statement_tex": "For nu>=1/2 and 0<rho<1, Psi_{nu,rho} is strictly increasing on (0,infty), using theta_nu'(z)=2/(pi z M_nu(z)^2) and strict decrease of M_nu(z)^2=J_nu(z)^2+Y_nu(z)^2 from Nicholson's formula. The branch normalization must also give Psi_{nu,rho}(0+)=0 and Psi_{nu,rho}(k)->infty.",
        "dependencies": ["SHELL-exact-phase-rep", "SRC-bessel-phase"],
        "implies": ["SHELL-count-floor-identity", "SHELL-phase-enclosures"],
        "blockers": ["SRC-bessel-phase"],
        "evidence": {
          "positive": ["rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/reviews/A4.md"],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/reviews/A1.md"]
        },
        "owner": "A2",
        "next_action": "Card Nicholson's integral, validity range in nu and z, differentiation under the integral, sign convention for theta_nu', and the branch normalization."
      },
      {
        "id": "SHELL-count-floor-identity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Strict phase-count identity for shell eigenvalues",
        "status": "derived_under_assumptions",
        "statement_tex": "With strict counting and K=sqrt(Lambda), N_D(A_{rho,1},K^2)=sum_{ell>=0}(2ell+1) #{n>=1: n pi < Psi_{ell+1/2,rho}(K)}. The floor expression floor(Psi_{ell+1/2,rho}(K)/pi) is an upper bound but must not be asserted as exact at spectral endpoints.",
        "dependencies": ["CONV-strict-counting", "SHELL-sturm-liouville-completeness", "SHELL-cross-product-formula", "SHELL-exact-phase-rep", "SHELL-phase-monotonicity"],
        "implies": ["SHELL-lattice-count", "SHELL-weighted-lattice-fractional", "SHELL-fixed-rho-high-energy"],
        "blockers": ["SHELL-sturm-liouville-completeness", "SHELL-phase-monotonicity"],
        "evidence": {
          "positive": ["rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/reviews/A2.md"],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "next_action": "After monotonicity and completeness are promoted, upgrade; preserve the strict endpoint rule n pi < Psi(K)."
      },
      {
        "id": "SHELL-angular-cutoff",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "A priori angular-momentum cutoff",
        "status": "proved_internal",
        "statement_tex": "For d=3, angular momentum ell contributes no Dirichlet eigenvalue below K^2 whenever ell(ell+1)>=K^2. Proof: the radial Rayleigh quotient on (rho,1) with weight r^2 dr contains ell(ell+1)/r^2 >= ell(ell+1) for r<=1, and the radial kinetic term is nonnegative. Therefore the ell-sum is finite with ell(ell+1)<K^2.",
        "dependencies": ["CONV-strict-counting"],
        "implies": ["COMP-certified-bessel"],
        "blockers": [],
        "evidence": {
          "positive": ["rounds/polya-main/round_001/responses/A1-001.md", "rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/responses/A4-001.md", "rounds/polya-main/round_001/reviews/A4.md"],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "next_action": "Record the one-paragraph Rayleigh quotient proof in the lemma bank and use the cutoff in finite-window planning."
      },
      {
        "id": "SHELL-inner-turning",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Inner-boundary turning regime for shell phase differences",
        "status": "open",
        "statement_tex": "For fixed 0<rho<1, construct explicit one-sided control of theta_nu(rho k) and Psi_{nu,rho}(k) when rho k lies within the Airy scale of nu, for example rho k-nu=O(nu^{1/3}), with constants and error direction strong enough for the shell counting upper bound.",
        "dependencies": ["SHELL-exact-phase-rep", "SHELL-phase-monotonicity", "SRC-bessel-phase", "SRC-shell-weyl"],
        "implies": ["SHELL-phase-enclosures", "SHELL-fixed-rho-high-energy"],
        "blockers": ["SRC-bessel-phase", "SRC-shell-weyl"],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/responses/A3-001.md"]
        },
        "owner": "A2",
        "next_action": "Formulate the Airy-scale statement precisely and test whether FLPS single-Bessel Airy bounds survive subtraction in theta_nu(k)-theta_nu(rho k)."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Fixed-rho high-energy shell Polya estimate",
        "status": "open",
        "statement_tex": "For each fixed 0<rho<1, prove an explicit K_0(rho) such that N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3) K^3 for all K>=K_0(rho), using the strict phase-count identity, one-sided shell phase enclosures, and the multiplicity-weighted lattice estimate. Candidate primary mechanism: the floor-free phase sum should capture the negative Dirichlet boundary term, while half-integer orders nu=ell+1/2 give a midpoint-quadrature advantage; this mechanism remains to be proved.",
        "dependencies": ["SHELL-count-floor-identity", "SHELL-phase-enclosures", "SHELL-inner-turning", "SHELL-weighted-lattice-fractional", "SRC-annuli"],
        "implies": ["TARGET-shell-d3"],
        "blockers": ["SHELL-phase-enclosures", "SHELL-inner-turning", "SHELL-weighted-lattice-fractional"],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/reviews/A2.md", "rounds/polya-main/round_001/reviews/A4.md"]
        },
        "owner": "A2",
        "next_action": "State the first black-box fixed-rho theorem with exact phase hypotheses, lattice hypotheses, and a computable analytic threshold K_0(rho)."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Multiplicity-weighted lattice bound for the 3D shell phase count",
        "status": "open",
        "statement_tex": "Given explicit one-sided phase bounds for Psi_{ell+1/2,rho}(K), prove the 2ell+1 weighted floor or phase-sum estimate needed to bound the fixed-rho high-energy shell count by (2/(9 pi))(1-rho^3) K^3. Annulus floor-sum lemmas must be audited because planar multiplicity does not transfer directly to the 2ell+1 weight.",
        "dependencies": ["SHELL-count-floor-identity", "SHELL-phase-enclosures", "SRC-annuli"],
        "implies": ["SHELL-lattice-count", "SHELL-fixed-rho-high-energy"],
        "blockers": ["SHELL-phase-enclosures", "SRC-annuli"],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/responses/A3-001.md", "rounds/polya-main/round_001/reviews/A1.md", "rounds/polya-main/round_001/reviews/A2.md"]
        },
        "owner": "A3",
        "next_action": "Formulate the weighted inequality abstractly under black-box phase hypotheses; identify minimal monotonicity, convexity, and error assumptions; audit which annulus lemmas survive the 2ell+1 weight."
      },
      {
        "id": "SHELL-spherical-bessel-algebraic",
        "type": "lemma",
        "track": "certified_computation",
        "title": "Elementary spherical-Bessel form of half-integer shell cross-products",
        "status": "open",
        "statement_tex": "In d=3, attempt to express F_{ell+1/2,rho}(k) in finite trigonometric-rational form P_ell(k,rho) sin((1-rho)k)+Q_ell(k,rho) cos((1-rho)k), with P_ell and Q_ell rational in k and rho. Low-ell cases are diagnostic evidence; the all-ell form and conditioning remain open.",
        "dependencies": ["SHELL-cross-product-formula"],
        "implies": ["COMP-certified-bessel", "SHELL-phase-enclosures"],
        "blockers": [],
        "evidence": {
          "positive": ["rounds/polya-main/round_001/reviews/A2.md"],
          "negative": [],
          "inconclusive": ["rounds/polya-main/round_001/responses/A3-001.md", "rounds/polya-main/round_001/responses/A4-001.md"]
        },
        "owner": "A4",
        "next_action": "Derive ell=0,1,2 explicitly; check whether only sin((1-rho)k) and cos((1-rho)k) remain after cancellation; estimate coefficient growth and conditioning."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "status": "proved_internal",
        "statement_tex": "Use N_D(Omega,Lambda)=#{j: lambda_j^D(Omega)<Lambda}. Under this strict convention, N_D(Omega,Lambda)<=C Lambda^{d/2} for all Lambda>=0 is equivalent to lambda_j^D(Omega)>=(j/C)^{2/d} for all j>=1, with eigenvalues repeated according to multiplicity.",
        "reason_for_promotion": "Round 1 fixed this as a project convention and no mathematical theorem is being promoted by adopting the endpoint normalization.",
        "evidence_added": {
          "positive": ["rounds/polya-main/round_001/responses/A1-001.md", "rounds/polya-main/round_001/reviews/A1.md"]
        },
        "next_action": "Use this endpoint rule in all imported source statements, phase-count identities, eigenvalue formulations, and certified finite-window checks."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "statement_tex": "For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9 pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for all K>=0.",
        "dependencies_added": ["SHELL-fixed-rho-high-energy"],
        "blockers_added": ["SHELL-fixed-rho-high-energy"],
        "evidence_added": {
          "inconclusive": ["rounds/polya-main/round_001/judge/judge-001.md"]
        },
        "next_action": "Keep the theorem open. First prove the fixed-rho high-energy estimate and a certified finite window; defer compact rho-uniformity and endpoint regimes."
      },
      {
        "id": "SHELL-cross-product-formula",
        "status": "open",
        "dependencies_added": ["SHELL-sturm-liouville-completeness"],
        "blockers_added": ["SHELL-sturm-liouville-completeness"],
        "evidence_added": {
          "positive": ["rounds/polya-main/round_001/responses/A2-001.md", "rounds/polya-main/round_001/responses/A3-001.md", "rounds/polya-main/round_001/responses/A4-001.md"]
        },
        "next_action": "Complete the Sturm-Liouville and spherical-harmonic proof; do not require absence of accidental equality across ell, only correct multiplicity summation."
      },
      {
        "id": "SRC-bessel-phase",
        "status": "source_audit_required",
        "next_action": "Audit Bessel phase definitions, modulus positivity, Wronskian sign, theta_nu'=2/(pi z M_nu^2), Nicholson's formula and strict decrease of M_nu^2, validity for nu>=1/2 and z>0, Airy transition constants, and whether independent phase bounds can be safely differenced for shell cross-products."
      },
      {
        "id": "SRC-annuli",
        "status": "source_audit_required",
        "next_action": "Extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal and convex/concave floor-sum lemmas, finite verification strategy, and exactly which lemmas are dimension-independent versus planar-multiplicity dependent."
      },
      {
        "id": "SRC-shell-weyl",
        "status": "source_audit_required",
        "next_action": "Audit shell-specific Bessel cross-product zero counts, Weyl-remainder bounds, dimension and boundary-condition assumptions, and whether any estimates are one-sided and explicit enough for Polya."
      },
      {
        "id": "SRC-FLPS-balls",
        "status": "source_audit_required",
        "next_action": "Create the source card for FLPS balls, disks, and sectors: theorem statements, boundary conditions, counting convention, Bessel phase definitions, lattice-counting lemmas, and computer-assisted components to reproduce before shell transfer."
      },
      {
        "id": "FLPS-disk-ball-reproduction",
        "status": "open",
        "next_action": "Draft a reproduction checklist with formulas, theorem dependencies, and verification scripts to import or reimplement; keep it as infrastructure until source cards exist."
      },
      {
        "id": "SHELL-phase-enclosures",
        "status": "open",
        "dependencies_added": ["SHELL-exact-phase-rep", "SHELL-phase-monotonicity", "SHELL-inner-turning"],
        "blockers_added": ["SHELL-inner-turning"],
        "next_action": "For fixed rho, formulate quantitative one-sided enclosures for Psi_{nu,rho}(k) in oscillatory, outer-turning, inner-turning, mixed evanescent/oscillatory, and fully evanescent regimes; explicitly track differencing loss."
      },
      {
        "id": "SHELL-lattice-count",
        "status": "open",
        "dependencies_added": ["SHELL-count-floor-identity", "SHELL-weighted-lattice-fractional"],
        "blockers_added": ["SHELL-weighted-lattice-fractional"],
        "evidence_added": {
          "inconclusive": ["rounds/polya-main/round_001/responses/A3-001.md", "rounds/polya-main/round_001/reviews/A4.md"]
        },
        "next_action": "Replace the broad lattice target with a precise black-box theorem: assuming explicit one-sided phase bounds, prove the 2ell+1 weighted count is below (2/(9 pi))(1-rho^3)K^3 in the fixed-rho high-energy range."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "dependencies_added": ["SHELL-sturm-liouville-completeness", "SHELL-angular-cutoff", "SHELL-spherical-bessel-algebraic"],
        "required_output": ["script", "exact command", "root-enclosure report", "counting verification table", "limitations"],
        "evidence_added": {
          "inconclusive": ["rounds/polya-main/round_001/responses/A4-001.md", "rounds/polya-main/round_001/reviews/A4.md"]
        },
        "next_action": "Implement a minimal diagnostic root-isolation prototype for rho=1/2, ell=0,1,2, 0<k<20. Compare raw Bessel interval evaluation against phase-based, recurrence-scaled, and spherical-Bessel algebraic evaluation. Add exact-root signed-defect, thin-shell, small-hole, and stability diagnostics, but treat all outputs as diagnostic."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "next_action": "Keep rho-uniformity deferred. After fixed-rho high-energy and finite-window methods are formulated, separately plan compact rho intervals, rho->0 small-hole behavior, and rho->1 thin-shell behavior."
      },
      {
        "id": "ELLIPSE-near-circular",
        "status": "open",
        "next_action": "Keep as a parallel flagship track. Do not mark blocked. Next useful action is source-auditing Mathieu characteristic values, small-eccentricity perturbation, and certified eigenvalue enclosures after the shell Round 2 core tasks are assigned."
      },
      {
        "id": "CERT-certificate-family",
        "status": "open",
        "next_action": "Keep as a fallback route. Do not mark blocked. First complete SRC-jiang-lin before proposing a concrete family or exact certificate theorem."
      }
    ],
    "reject": [
      {
        "id": "A3-proposed-blocked-statuses",
        "reason": "Reject marking SHELL-lattice-count, ELLIPSE-near-circular, or CERT-certificate-family as blocked. The correct status is open or source-audit-dependent, not blocked by a proved obstruction."
      },
      {
        "id": "toy-weighted-fractional-test",
        "reason": "Reject the proxy sum using sqrt(Lambda-ell(ell+1)) as a proof-relevant diagnostic. It does not use the shell phase, actual roots, or a stated WKB phase with explicit error."
      },
      {
        "id": "raw-floating-point-computation-as-proof",
        "reason": "Reject any use of floating-point root tables as proof. Computation remains diagnostic until certified interval or ball arithmetic outputs all required artifacts."
      },
      {
        "id": "bare-two-term-weyl-proof",
        "reason": "Reject a bare two-term Weyl threshold argument without explicit one-sided constants and certified compact-window closure."
      },
      {
        "id": "judge1-progress-score-7",
        "reason": "Reject the inflated mathematical_progress_score=7 from the first candidate judge response. Round 1 produced structural de-risking, not theorem-level progress."
      }
    ],
    "no_change": [
      {
        "id": "POLYA-program-target",
        "reason": "No theorem-level program claim is proved or promoted."
      },
      {
        "id": "SRC-mathieu-ellipse",
        "reason": "Still source-audit-required for the parallel ellipse track."
      },
      {
        "id": "SRC-jiang-lin",
        "reason": "Still source-audit-required before certificate-family work can be used as a dependency."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 3,
    "idea_quality_score": 8,
    "state_evidence_score": 7,
    "calibration_score": 8,
    "reason": "Structural de-risking only: exact monotone phase scaffold, a proved angular cutoff, and a proved counting convention; no shell Polya theorem and both quantitative blockers, inner-turning enclosure and 2D weighted lattice control, remain open. The final synthesis adopts judge2 calibration while importing judge1 completeness and diagnostic coverage."
  }
}
```

## Next-round prompts by agent

### For A1

Build the Round 2 source-card foundation. Prioritize `SRC-bessel-phase`, `SRC-annuli`, `SRC-shell-weyl`, and `SRC-FLPS-balls`.

For `SRC-bessel-phase`, record exact statements for the Bessel phase/modulus convention, Wronskian sign, `theta_nu'(z)=2/(pi z M_nu(z)^2)`, Nicholson's formula, strict decrease of `M_nu(z)^2=J_nu(z)^2+Y_nu(z)^2`, validity ranges in `nu` and `z`, and Airy transition enclosures. State whether individual phase bounds can be differenced in the shell cross-product without losing the needed one-sided direction.

For `SRC-annuli`, extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal/floor-sum lemmas, finite verification strategy, and exactly which lemmas rely on planar multiplicity rather than a `2ell+1` weight.

For `SRC-shell-weyl`, record the shell cross-product zero-counting and Weyl-remainder statements, including explicitness, one-sidedness, boundary conditions, and dimension range.

Do not claim any shell, ellipse, or certificate-family theorem.

### For A2

Formalize the shell phase scaffold. Write a lemma package for:

1. `SHELL-exact-phase-rep`;
2. `SHELL-phase-monotonicity` conditional on Nicholson;
3. `SHELL-count-floor-identity` with strict endpoint rule;
4. `SHELL-inner-turning`.

For the phase-count identity, do not state equality with the floor at endpoints. Use the strict count `#{n>=1: n pi < Psi_{ell+1/2,rho}(K)}`.

For `SHELL-inner-turning`, state a precise Airy-scale proposition for `rho k - nu = O(nu^{1/3})` and identify exactly which constants and one-sided errors must be inherited or rebuilt from the Bessel phase source card. End with a fixed-rho high-energy proposition template that separates phase hypotheses from lattice hypotheses.

Do not claim the high-energy Polya estimate yet.

### For A3

Attack `SHELL-weighted-lattice-fractional` and refine `SHELL-lattice-count`.

Assume a black-box phase-count formula and explicit one-sided bounds for `Psi_{ell+1/2,rho}(K)`. Formulate the exact weighted discrete inequality needed to prove

`sum_{ell>=0}(2ell+1) #{n>=1: n pi < Psi_{ell+1/2,rho}(K)} <= (2/(9 pi))(1-rho^3)K^3`

for fixed `rho` and large `K`.

Audit which annulus floor-sum lemmas transfer and which fail because of the weight `2ell+1`. Compare two possible high-energy mechanisms: fractional-part lower bounds versus a floor-free phase-sum bound with an explicit negative boundary margin. Reject toy diagnostics that do not use the shell phase.

Also run the exact-root signed-defect scan for `rho` in `{0.1, 0.5, 0.9}` and report whether the worst defect drifts to the inner-transition band. Keep ellipse/certificate parallel, not blocked.

### For A4

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

## Confidence

High confidence: strict target normalization, Weyl constant, shell volume, endpoint convention, and the need for source-card discipline.

High confidence: the cross-product formula is algebraically correct, pending a formal Sturm-Liouville completeness proof.

Medium-high confidence: the exact phase representation is correct once phase/modulus conventions are recorded.

Medium confidence: Nicholson monotonicity will prove global shell phase monotonicity, but it remains an external dependency until source-carded.

Medium-low confidence: the weighted lattice estimate can be proved with existing annulus methods; new discrete estimates are likely needed.

Low confidence: endpoint uniformity in `rho` and any full theorem-level shell Polya claim at this stage.

No Dirichlet Polya theorem for shells, ellipses, or a certificate family is claimed.
