# Round 6 Judge: Analytic Closure of the Thin-Shell Endpoint

## Verdict

Round 6 closes the complete $\rho\uparrow1$ endpoint analytically.

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le2^{-18}=\frac1{262144}.
$$

Then, for every $K\ge0$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Equivalently, the strict Dirichlet Pólya inequality holds uniformly for

$$
1-2^{-18}\le\rho<1.
$$

No Bessel-root certificate is needed in this endpoint neighborhood.

The proof has two new radius-sensitive components.

1. The exact scaled action, compared below the inner interface with a
   mean-square-radius semicircle and corrected explicitly on the
   whispering-gallery strip, proves the shell bound through

   $$
   K\le\frac1{8\varepsilon^{5/2}}.
   $$

   Its continuous coefficient is exactly

   $$
   \varepsilon^{-1}\int_{1-\varepsilon}^1r^2\,dr
   =1-\varepsilon+\frac{\varepsilon^2}{3}.
   $$

2. A local first-plateau estimate in the Round 3 shifted-tail proof improves
   the high-thin threshold from order $\varepsilon^{-4}$ to

   $$
   K\ge\frac{64}{\varepsilon^2}.
   $$

The two ranges overlap exactly when

$$
\frac{64}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
\varepsilon\le2^{-18}.
$$

At the limiting endpoint both thresholds equal $2^{42}$ and both component
theorems include equality.  Round 5 covers the remaining lower frequencies.

## Evidence gates

- Frozen packet:
  `state/lemma_packets/SHELL-thin-curvature-intermediate.md`
- Integrated incumbent:
  `rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md`
- Aggregate-action incumbent:
  `rounds/polya-main/round_006/exploration/phase-aggregate.md`
- Local-plateau incumbent:
  `rounds/polya-main/round_006/exploration/local-plateau-high-thin.md`
- Aggregate-action isolated clean-room review:
  `rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md`
- Local-plateau isolated clean-room PASS:
  `rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md`
- Aggregate-action adversarial PASS:
  `rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md`
- Combined constants and overlap PASS:
  `rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md`
- Independent analytic alternative and obstruction audit:
  `rounds/polya-main/round_006/exploration/radial-bracketing.md`
- Reproducible diagnostics, explicitly non-certifying:
  `rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md`,
  `computations/thin_scaled_action_round6_diagnostic.py`, and
  `computations/tests/test_thin_scaled_action_round6_diagnostic.py`

The clean-room and adversarial reviews verify the normalization, strict
layer cake, shifted deficit, Jensen support, whispering-gallery payment,
local-slope estimate, no-drop branch, and exact overlap.  Floating scans are
not used in either proof.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-thin-action-aggregate",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Mean-square-radius aggregate action bound for thin shells",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/100 and a=epsilon K. If pi/(4 epsilon)<=a<=1/(8 epsilon^(3/2)), then the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. Equivalently, this radius-sensitive range is pi/(4 epsilon^2)<=K<=1/(8 epsilon^(5/2)).",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures"
        ],
        "implies": [
          "SHELL-thin-curvature-intermediate",
          "SHELL-rho-one-endpoint"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/exploration/phase-aggregate.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
            "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md",
            "computations/thin_scaled_action_round6_diagnostic.py",
            "computations/tests/test_thin_scaled_action_round6_diagnostic.py"
          ]
        },
        "owner": "A2",
        "criticality": "standard",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures"
        ],
        "falsification_cases": [
          "a=pi/(4 epsilon)",
          "a=1/(8 epsilon^(3/2))",
          "action plus one quarter on a positive integer wall",
          "effective radial level n-1/4 on the endpoint",
          "angular half-integer wall",
          "y=rho a inner interface",
          "positive whispering-gallery strip where the effective action vanishes"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
          "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
        ],
        "reason_for_promotion": "The exact scaled normalization, mean-square-radius Jensen comparison, strict layer cake, shifted radial deficit, angular ceiling, quarter-disk estimate, and explicit outer-strip payment passed an isolated clean-room reconstruction and two adversarial audits. The proof recovers the exact shell mean cross-section and uses no numerical evidence.",
        "next_action": "Use this theorem with Round 5 below and the local-plateau high-thin theorem above. Do not extend the effective-radius comparison pointwise through the outer strip."
      },
      {
        "id": "SHELL-thin-local-plateau-high",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Uniform local-plateau high-energy bound for thin shells",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/100. Then the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=64/epsilon^2.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "implies": [
          "SHELL-thin-curvature-intermediate",
          "SHELL-rho-one-endpoint"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/exploration/local-plateau-high-thin.md",
            "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md",
            "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md"
          ]
        },
        "owner": "A2",
        "criticality": "standard",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "falsification_cases": [
          "K=64/epsilon^2",
          "no floor drop p=n",
          "immediate floor drop p=0",
          "degenerate head n=0",
          "q=rho K",
          "K eta on an integer wall",
          "tail start x0 on either side of K/2"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
        ],
        "reason_for_promotion": "The local-slope proof reduces the dangerous first-floor plateau to O(epsilon^(-1/2)), while the convex-tail gain is uniformly larger at K>=64/epsilon^2. An isolated reconstruction obtained an independent stronger plateau constant, and the combined audit checked every exceptional branch and wall.",
        "next_action": "Use this theorem as the uniform high-frequency half of the thin endpoint; the older K_0(1-epsilon) threshold is no longer needed near rho=1."
      }
    ],
    "update": [
      {
        "id": "SHELL-thin-curvature-intermediate",
        "status": "proved_internal",
        "statement_tex": "For rho=1-epsilon with 0<epsilon<=2^(-18)=1/262144, the strict shell Polya estimate holds for every K>=0. Round 5 and the mean-square-radius aggregate theorem cover K<=1/(8 epsilon^(5/2)); the local-plateau theorem covers K>=64/epsilon^2; these ranges overlap exactly because epsilon<=2^(-18).",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_006/exploration/phase-aggregate.md",
            "rounds/polya-main/round_006/exploration/local-plateau-high-thin.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
            "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
            "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
          ],
          "inconclusive": [
            "rounds/polya-main/round_006/exploration/radial-bracketing.md",
            "rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md"
          ]
        },
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
          "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
          "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
        ],
        "reason_for_promotion": "Two independently reviewed radius-sensitive theorems overlap explicitly at epsilon=2^(-18), with Round 5 covering the lower endpoint. The combined constants audit verifies that all K>=0 are covered and every joining endpoint is included.",
        "next_action": "Use this proved overlap to discharge SHELL-rho-one-endpoint. No thin-shell Bessel certificate remains necessary."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "status": "proved_internal",
        "statement_tex": "For every 1-2^(-18)<=rho<1 and every K>=0, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. The lower rho endpoint is included and rho=1 is excluded as the degenerate zero-width limit.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high",
          "SHELL-thin-curvature-intermediate"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
            "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md",
            "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
            "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
          ],
          "inconclusive": [
            "rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md"
          ]
        },
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high",
          "SHELL-thin-curvature-intermediate"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
          "rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
          "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
        ],
        "reason_for_promotion": "The exact overlap theorem proves one fixed rho-neighborhood of 1 for every frequency. The two analytic components passed separate clean-room and adversarial gates, so no finite certification assumption remains in the thin endpoint.",
        "next_action": "Treat this endpoint as discharged. Continue with the small-hole endpoint and compact-rho finite certification."
      },
      {
        "id": "SHELL-rho-uniformity",
        "blockers_removed": [
          "SHELL-rho-one-endpoint"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md"
          ]
        },
        "next_action": "The thin endpoint is discharged. Close SHELL-rho-zero-endpoint and SHELL-rho-compact, then assemble the all-rho theorem."
      },
      {
        "id": "SHELL-rho-compact",
        "next_action": "Use rho<=1-2^(-18) as the compact side of the proved thin split. Bound K_0 uniformly on the selected compact interval and certify only the resulting bounded finite window."
      },
      {
        "id": "SHELL-rho-zero-endpoint",
        "next_action": "This is now the primary analytic endpoint. Prove a quantitative small-hole theorem with explicit overlap to compact rho; do not infer uniformity from pointwise convergence to the ball."
      },
      {
        "id": "COMP-certified-bessel",
        "evidence_added": {
          "inconclusive": [
            "computations/thin_scaled_action_round6_diagnostic.py",
            "computations/tests/test_thin_scaled_action_round6_diagnostic.py",
            "rounds/polya-main/round_006/exploration/scaled-action-diagnostic.md"
          ]
        },
        "next_action": "No thin-endpoint certificate is needed. Restrict certification to bounded residual boxes left by the small-hole and compact-rho arguments, preserving strict determinant, phase, and floor walls."
      },
      {
        "id": "TARGET-shell-d3",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-curvature-intermediate.md",
            "rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md"
          ]
        },
        "next_action": "The exact spectrum, fixed-rho high energy, and complete thin endpoint are proved. The remaining theorem blockers are small-hole/compact-rho uniformity and bounded certified closure, followed by a final theorem audit."
      }
    ],
    "reject": [
      {
        "id": "raw-midpoint-action-quadrature-proves-thin-range",
        "reason": "Reject replacing the strict action staircase by its raw midpoint sum. The Round 6 diagnostic gives an exact family for every 0<epsilon<=1/10 at K=1 where the raw midpoint action contribution already exceeds the complete continuous Weyl integral, while the strict floor count is zero."
      },
      {
        "id": "single-volume-matched-effective-radius-is-global-majorant",
        "reason": "Reject a global pointwise comparison with one volume-matched effective radius. Its action vanishes at y=a sqrt(1-epsilon+epsilon^2/3)<a, while the exact shell action remains positive throughout the outer whispering-gallery strip up to y=a."
      },
      {
        "id": "fixed-finite-neumann-sublayers-close-thin-shell",
        "reason": "Reject any fixed finite Neumann-sublayer majorant as a global proof. Its right-endpoint step radii have a strictly larger cubic coefficient than the exact shell mean, so the majorant exceeds the desired Weyl term for all sufficiently large K."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "Round 6 did not prove the small-hole endpoint."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "Round 6 did not certify the compact-rho finite window."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "The new computations are diagnostic only; no interval-certified finite window was produced."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The thin endpoint is now proved, but the small-hole endpoint, compact-rho closure, and final theorem audit remain open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "Two independently reviewed radius-sensitive estimates overlap and prove the entire rho-to-one endpoint for all frequencies. This removes a theorem-level bottleneck, while the small-hole endpoint, compact-rho certification, and final shell theorem remain open."
  }
}

## State boundary after Round 6

The shell theorem is now unconditional for every

$$
1-2^{-18}\le\rho<1
$$

and every $K\ge0$.  The global theorem remains open only because the
small-hole endpoint and the intervening compact-$\rho$ finite window have
not yet been closed and audited.
