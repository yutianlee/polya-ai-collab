# Round 3 Judge: Weighted Lattice Gate

## Verdict

The full obligation `SHELL-weighted-lattice-fractional` remains open. The incumbent and clean-room attempts independently agree, and the adversarial audit confirms, that the first unsupported implication is the shifted-tail inequality below the inner interface.

Round 3 nevertheless proves three reusable sublemmas:

1. the exact strict proxy, Weyl integral, square formulation, multiplicity-to-tail reduction, and the implication from all shifted tails to the weighted bound;
2. every shifted tail whose starting order is at or above $\rho K$, by the audited FLPS convex theorem;
3. the exact phase-level zero count when $(1-\rho)K\le\pi$.

The floating diagnostic strongly supports the remaining low-tail inequality but is not certification or promotion evidence. No shell Pólya theorem is proved.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-weighted-lattice-scaffold",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Exact weighted shell lattice scaffold and tail reduction",
        "status": "proved_internal",
        "statement_tex": "For A_{rho,K}=G_K-G_{rho K}, the strict coarse proxy has an exact square-level formulation and an exact 2ell+1 multiplicity-to-shifted-tail decomposition. If every ordinary-floor shifted tail T_r is at most 2 int_{r+1/2}^K A_{rho,K}, then the complete weighted coarse proxy is at most int_0^K 2z A_{rho,K}(z) dz = (2/(9 pi))(1-rho^3)K^3.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-annulus-phase-transfer",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-shifted-tails"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-weighted-lattice-fractional.md",
            "rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "clean_room_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
        ],
        "reason_for_promotion": "The incumbent derivation, independent clean-room reconstruction, and adversarial audit agree on every algebraic identity, strict endpoint, integral, and inequality direction in the conditional tail reduction.",
        "next_action": "Use the scaffold only through an explicitly proved shifted-tail estimate; do not infer the missing low-interface tails from diagnostics."
      },
      {
        "id": "SHELL-high-angular-shifted-tails",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Shifted shell tails above the inner interface",
        "status": "proved_internal",
        "statement_tex": "For every integer r>=0 with r+1/2>=rho K, the ordinary-floor tail of A_{rho,K}(r+j+1/2)+1/4 is at most 2 int_{r+1/2}^K A_{rho,K}(z) dz.",
        "dependencies": [
          "SHELL-weighted-lattice-scaffold",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-weighted-lattice-fractional"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "sources/flps_balls.md",
            "rounds/polya-main/round_003/reviews/flps-ball-weight-transfer-audit.md",
            "rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "clean_room_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
        ],
        "reason_for_promotion": "Above the inner interface A_{rho,K}=G_K; the translated function satisfies every hypothesis of the audited FLPS ball convex 1/2-Lipschitz floor-sum theorem.",
        "next_action": "Treat these tails as discharged and concentrate analytic work on starts below rho K."
      },
      {
        "id": "SHELL-low-interface-shifted-tails",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Shifted shell tails crossing the inner interface",
        "status": "open",
        "statement_tex": "For every integer r>=0 with r+1/2<rho K, prove that the ordinary-floor tail of A_{rho,K}(r+j+1/2)+1/4 is at most 2 int_{r+1/2}^K A_{rho,K}(z) dz, or prove the corresponding optimized-envelope bound if the coarse statement fails.",
        "dependencies": [
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-weighted-lattice-fractional"
        ],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md",
            "computations/SHELL-weighted-lattice-fractional-diagnostic.md"
          ]
        },
        "owner": "A2",
        "criticality": "bottleneck",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "falsification_cases": [
          "rho K equal to a half-integer grid point",
          "tail start immediately below rho K",
          "coarse proxy on an integer wall",
          "rho approaching zero",
          "rho approaching one with fixed optical width",
          "loss of floor margin when splitting at a nonintegral inner interface"
        ],
        "clean_room_artifacts": [],
        "adversarial_review_artifacts": [],
        "next_action": "Prove the concave-to-convex shifted-tail inequality using horizontal-level blocks or an audited annulus floor-sum refinement; if it fails, locate an exact counterexample and retry with the optimized H_mu cap."
      },
      {
        "id": "SHELL-thin-width-phase-zero",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Zero strict radial phase count at shell width at most pi",
        "status": "proved_internal",
        "statement_tex": "For every half-integer nu>=1/2, theta_nu'(x)<=1 and Psi_{nu,rho}(K)<=(1-rho)K. Hence every strict radial phase count is zero whenever (1-rho)K<=pi, including the equality endpoint.",
        "dependencies": [
          "CONV-strict-counting",
          "SRC-bessel-phase",
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity"
        ],
        "implies": [
          "SHELL-rho-one-endpoint",
          "SHELL-weighted-lattice-fractional"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-width-zero-count.md",
            "rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "clean_room_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
        ],
        "reason_for_promotion": "Nicholson's positive integral compares M_nu to the explicit half-order modulus, giving theta_nu'<=1; strict endpoint counting then gives zero radial levels at width pi.",
        "next_action": "Use this exact phase-level result in the thin-shell split. Do not state a full spectral zero theorem without the separate completeness/count dependency."
      }
    ],
    "update": [
      {
        "id": "SRC-FLPS-balls",
        "status": "proved_external_dependency",
        "evidence_added": {
          "positive": [
            "sources/flps_balls.md",
            "rounds/polya-main/round_003/reviews/flps-ball-weight-transfer-audit.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
          ]
        },
        "reason_for_promotion": "The published theorem, counting convention, uniform zero comparison, convex shifted floor theorem, dimension reduction, exact integral, computation boundary, and shell transfer limitations have been audited from the primary source.",
        "next_action": "Use only the audited convex-tail and multiplicity components; do not transfer the ball theorem across the shell inner interface."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "statement_tex": "For fixed 0<rho<1, prove an explicit high-energy bound for the strict 2ell+1 weighted proxy derived from U_{rho,K}=G_K-G_{rho K}+s_{rho K}, with exact endpoint counting and Weyl target (2/(9 pi))(1-rho^3)K^3.",
        "dependencies_added": [
          "SRC-FLPS-balls",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-shifted-tails",
          "SHELL-thin-width-phase-zero"
        ],
        "blockers": [
          "SHELL-low-interface-shifted-tails"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-weighted-lattice-fractional.md"
          ],
          "inconclusive": [
            "rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md",
            "computations/SHELL-weighted-lattice-fractional-diagnostic.md"
          ]
        },
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
        ],
        "next_action": "Close SHELL-low-interface-shifted-tails. The continuous phase sum and blanket quarter-slack estimates are rejected proof routes; retain strict integerization."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "dependencies_added": [
          "SHELL-thin-width-phase-zero"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-width-zero-count.md",
            "rounds/polya-main/round_003/reviews/weighted-lattice-adversarial.md"
          ]
        },
        "next_action": "Split the endpoint analysis at optical width (1-rho)K=pi. The lower-width region has zero radial phase count; control widths above pi and overlap with compact-rho estimates."
      },
      {
        "id": "FLPS-disk-ball-reproduction",
        "blockers_removed": [
          "SRC-FLPS-balls"
        ],
        "next_action": "Reproduce only the remaining proof infrastructure needed by active obligations; the FLPS ball source card is now audited."
      },
      {
        "id": "SHELL-rho-zero-endpoint",
        "blockers_removed": [
          "SRC-FLPS-balls"
        ],
        "next_action": "Use the audited ball limit together with certified computation; the FLPS ball source audit is discharged."
      },
      {
        "id": "COMP-certified-bessel",
        "evidence_added": {
          "inconclusive": [
            "computations/shell_weighted_lattice_fractional_diagnostic.py",
            "computations/SHELL-weighted-lattice-fractional-diagnostic.md",
            "computations/tests/test_shell_weighted_lattice_fractional_diagnostic.py"
          ]
        },
        "next_action": "Retain diagnostic_only. Design rigorous wall handling and interval evaluation for the finite shell window after the analytic low-interface tail range is explicit."
      }
    ],
    "reject": [
      {
        "id": "floor-free-weighted-phase-sum",
        "reason": "Reject replacing strict integer counts by the continuous phase or G-F sum. At K=1 and rho K=1/4 the strict proxy is zero while the floor-free sampled bound already exceeds the Weyl target."
      },
      {
        "id": "blanket-quarter-slack-as-uniform-lower-order-error",
        "reason": "Reject uniform absorption of the accumulated 1/4 slack. In fixed optical-width scaling its ratio to the Weyl term tends to 3 pi/(8a)."
      },
      {
        "id": "floating-shifted-tail-grid-as-proof",
        "reason": "Reject promotion from the finite floating grid. Floor walls, endpoint classification, quadrature, and the reported margins are not interval-certified."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-lattice-count",
        "reason": "The parent lattice obligation remains open until the low-interface shifted tails are proved."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "The fixed-rho high-energy theorem remains open because the weighted lattice obligation is incomplete."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "No shell Pólya theorem is proved."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 4,
    "reason": "The weighted target remains open, but exact reductions, all high-angular tails, and the thin-width phase-zero region passed incumbent, clean-room, and adversarial gates; the low inner-interface tails are now the sole weighted bottleneck."
  }
}
