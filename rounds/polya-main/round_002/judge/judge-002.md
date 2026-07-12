# Round 2 Synthesis: Source Audit and Diagnostic Prerequisites

## Selected main route

Import the published real-order annulus phase-difference bound before developing new Airy estimates. Test its explicit $+1/4$ normalized phase slack against the $3$D multiplicity-weighted lattice sum.

## Useful evidence

- `sources/bessel_phase_enclosures.md` records the exact phase convention, derivative, Nicholson monotonicity, and FLPS 2024 enclosure.
- `sources/annuli_polya.md` records the real-order global difference bound, its transition scope, and the planar/non-planar transfer boundary.
- `rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md` independently checks the half-integer substitution, signs, strict-count endpoints, and limitations.
- `computations/results/bessel_cross_product_rho_half.md` is a reproducible floating-point diagnostic only.

## Rejected or risky ideas

- Do not commission a new explicit Airy proof before testing the published $1/4$ phase margin.
- Do not apply the sharper correlated bound on the evanescent side $\rho k<\nu$.
- Do not import the planar trapezoidal count with multiplicity $\kappa_m$ into the $2\ell+1$-weighted shell problem.
- Do not call the new numerical brackets certified.

## Known gaps

The decisive unresolved point is whether the explicit global phase bound closes the weighted lattice count. Compact-$\rho$ uniformity, the thin-shell limit, and certified finite-window coverage remain open.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-annulus-phase-transfer",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Real-order annulus phase bounds specialized to 3D shell orders",
        "status": "proved_internal",
        "statement_tex": "Let 0<rho<1, K>0, and nu=ell+1/2 with ell>=0 and 0<=nu<=K. With mu=rho K and the audited branch of theta_nu, the normalized shell phase gamma=(theta_nu(K)-theta_nu(mu))/pi satisfies the FLPS annulus Lemma 5.2 bounds after the substitution (lambda,mu,z)=(K,rho K,nu): globally gamma<G_K(nu)-F_mu(nu)<=G_K(nu)+1/4; when nu<=mu, Phi_{K,mu}(nu)<gamma<Phi_{K,mu}(nu)+1/4. On mu<nu<=K only the global one-sided bound is asserted.",
        "dependencies": [
          "SRC-bessel-phase",
          "SRC-annuli",
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity"
        ],
        "implies": [
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-inner-turning"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "sources/bessel_phase_enclosures.md",
            "sources/annuli_polya.md",
            "rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "Use the transferred bounds as hypotheses in the 2ell+1 weighted lattice inequality; do not infer that the additive 1/4 slack is sufficient without proving the weighted sum."
      }
    ],
    "update": [
      {
        "id": "SRC-bessel-phase",
        "status": "proved_external_dependency",
        "evidence_added": {
          "positive": [
            "sources/bessel_phase_enclosures.md",
            "rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md"
          ]
        },
        "reason_for_promotion": "The primary SIAM paper, DLMF formulas, exact validity ranges, branch convention, constants, differencing rule, and limitations have been audited.",
        "next_action": "Use the audited formulas through SHELL-annulus-phase-transfer; reopen the source audit only if a sharper explicit Airy margin is shown to be necessary."
      },
      {
        "id": "SRC-annuli",
        "status": "proved_external_dependency",
        "implies_added": ["SHELL-annulus-phase-transfer"],
        "evidence_added": {
          "positive": [
            "sources/annuli_polya.md",
            "rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md"
          ]
        },
        "reason_for_promotion": "The published annulus theorem, real-order phase bounds, lattice lemmas, computation method, counting convention, and exact transfer boundary have been audited.",
        "next_action": "Use only the real-order phase results directly; rebuild the multiplicity-weighted lattice and finite-certificate components for 3D shells."
      },
      {
        "id": "SHELL-exact-phase-rep",
        "status": "proved_internal",
        "dependencies": ["SRC-bessel-phase"],
        "evidence_added": {
          "positive": [
            "sources/bessel_phase_enclosures.md",
            "sources/annuli_polya.md",
            "rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md"
          ]
        },
        "reason_for_promotion": "The factorization is a direct algebraic substitution into the audited positive-modulus phase convention; determinant sign and zero-set invariance were independently checked.",
        "next_action": "Use the fixed sign convention and branch in every shell count; spectral completeness remains a separate obligation."
      },
      {
        "id": "SHELL-phase-monotonicity",
        "status": "proved_internal",
        "dependencies": ["SHELL-exact-phase-rep", "SRC-bessel-phase"],
        "evidence_added": {
          "positive": [
            "sources/bessel_phase_enclosures.md",
            "sources/annuli_polya.md",
            "rounds/polya-main/round_002/reviews/phase-source-transfer-audit.md"
          ]
        },
        "reason_for_promotion": "DLMF 10.18.8 and Nicholson 10.9.30 give an explicit positive derivative for the phase difference for every real nu>=0; endpoint limits were checked with the fixed branch.",
        "next_action": "Use global monotonicity to index cross-product roots after Sturm-Liouville completeness is discharged."
      },
      {
        "id": "SHELL-phase-enclosures",
        "dependencies": [
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity",
          "SHELL-annulus-phase-transfer"
        ],
        "blockers": ["SHELL-annulus-phase-transfer"],
        "next_action": "Run the configured clean-room and adversarial review on the transferred global bound and its strict-count use. Do not require separate regime proofs unless the weighted lattice test exposes insufficient margin."
      },
      {
        "id": "SHELL-inner-turning",
        "status": "proposed",
        "dependencies_added": ["SRC-annuli", "SHELL-annulus-phase-transfer"],
        "blockers": [],
        "next_action": "Defer a new Airy enclosure. First test whether FLPS annuli Lemma 5.2, including the global bound on rho K<nu<=K and the correlated 1/4 bound on nu<=rho K, closes the weighted lattice estimate."
      },
      {
        "id": "SHELL-phase-oscillatory",
        "status": "proposed",
        "next_action": "Treat as a fallback sharpening obligation only if the transferred annulus phase bound lacks sufficient weighted-lattice margin."
      },
      {
        "id": "SHELL-phase-outer-turning",
        "status": "proposed",
        "next_action": "Treat as a fallback sharpening obligation only if the transferred annulus phase bound lacks sufficient weighted-lattice margin."
      },
      {
        "id": "SHELL-phase-evanescent",
        "status": "proposed",
        "next_action": "Use the global one-sided annulus bound first; seek a sharper evanescent estimate only if the weighted-lattice margin fails."
      },
      {
        "id": "SHELL-phase-overlap",
        "status": "proposed",
        "next_action": "The transferred global bound removes regime-coverage gaps at the present precision. Reactivate only if fallback regime sharpenings are introduced."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "dependencies_removed": ["SHELL-inner-turning"],
        "blockers_removed": ["SHELL-inner-turning"],
        "dependencies_added": ["SHELL-annulus-phase-transfer"],
        "next_action": "Insert the transferred phase bound into the strict 2ell+1 weighted count and determine explicitly whether the 1/4 slack is absorbed by the phase-space margin."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "dependencies_added": ["SHELL-annulus-phase-transfer"],
        "next_action": "Formulate and prove or falsify the exact 2ell+1 weighted inequality using G_K-F_{rho K}; isolate the total contribution of the additive 1/4 slack and stress-test rho->1."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "evidence_class": "floating_point_experiment",
        "evidence_added": {
          "inconclusive": [
            "computations/bessel_cross_product_diagnostic.py",
            "computations/results/bessel_cross_product_rho_half.md",
            "computations/tests/test_bessel_cross_product_diagnostic.py"
          ]
        },
        "next_action": "Design the certified successor with interval or ball arithmetic, monotone phase/root bracketing, rigorous coverage of the omitted small-k interval, software versions, deterministic command, and artifact hashes."
      },
      {
        "id": "SHELL-spherical-bessel-algebraic",
        "evidence_added": {
          "inconclusive": [
            "computations/bessel_cross_product_diagnostic.py",
            "computations/results/bessel_cross_product_rho_half.md"
          ]
        },
        "next_action": "Promote only after the all-ell recurrence identity and its numerical-conditioning domain are proved; current low-order tests remain diagnostic."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "TARGET-shell-d3",
        "reason": "Source prerequisites improved, but the weighted lattice bound, spectral completeness, rho-uniformity, and certified finite window remain open."
      },
      {
        "id": "SHELL-lattice-count",
        "reason": "The phase input is sharper, but no 2ell+1 weighted inequality was proved."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 4,
    "idea_quality_score": 8,
    "state_evidence_score": 8,
    "calibration_score": 9,
    "reason": "Two source audits and two foundational phase identities are discharged, a published real-order transfer lemma is isolated, and a reproducible diagnostic is added; the theorem-level weighted count remains open."
  }
}
```

## Next-cycle prompts

### For A1

Prepare the exact `SHELL-weighted-lattice-fractional` packet using the transferred $G_K-F_{\rho K}$ bound.

### For A2

Derive the incumbent $2\ell+1$ weighted sum and isolate the full contribution of the $1/4$ phase slack.

### For A3

Independently attempt or falsify the same weighted inequality without seeing A2’s derivation.

### For A4

Adversarially compare the frozen weighted-count attempts and separately design, but do not overclaim, the interval-arithmetic successor to the diagnostic script.

## Confidence

High for the source transfer and diagnostic classification; low-to-moderate that the published $1/4$ slack alone closes the weighted lattice inequality.
