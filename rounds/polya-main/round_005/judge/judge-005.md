# Round 5 Judge: Thin-Shell Product Range

## Verdict

The outer-radius product comparison proves a genuine, uniform part of the
thin-shell endpoint. If

$$
\rho=1-\varepsilon,\qquad
0<\varepsilon\le\frac1{100},
$$

then

$$
\boxed{
0\le K\le\frac{\pi}{4\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The proof uses the exact Round 4 direct sum and the min--max comparison

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1),
$$

followed by an exact strict radial/angular lattice count. The frozen proof
passed an isolated clean-room reconstruction, an adversarial audit, and a
separate constants audit after two endpoint wording corrections.

The same round proves that this flat product majorant cannot close the entire
thin-shell endpoint. It exceeds the shell Weyl target at infinitely many
exact radial walls for every fixed positive $\varepsilon$, and along an exact
family with $\varepsilon\downarrow0$. These are counterexamples to the
majorant only, not to the shell Pólya inequality.

An exact failure wall occurs before the existing fixed-$\rho$ high-energy
threshold begins. Therefore the new low-optical range and the Round 4
high-energy range do not overlap. A new radius-sensitive intermediate
estimate is required.

## Evidence gates

- Frozen packet: state/lemma_packets/SHELL-thin-product-low-optical.md
- Frozen incumbent: rounds/polya-main/round_005/responses/thin-shell-product-incumbent.md
- Clean-room PASS: rounds/polya-main/round_005/reviews/thin-shell-product-clean-room.md
- Adversarial PASS: rounds/polya-main/round_005/reviews/thin-shell-product-adversarial.md
- Corrected constants PASS: rounds/polya-main/round_005/reviews/thin-shell-product-constants-audit.md
- Independent analytic explorations:
  rounds/polya-main/round_005/exploration/thin-shell-product-analytic.md and
  rounds/polya-main/round_005/exploration/thin-shell-product-alternative.md
- Exact and diagnostic falsification record:
  rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-thin-product-low-optical",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Thin-shell product comparison at low optical width",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/100. Then the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every 0<=K<=pi/(4 epsilon^2). Equivalently, with a=epsilon K, the result holds for 0<=a<=pi/(4 epsilon).",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-angular-cutoff"
        ],
        "implies": [
          "SHELL-rho-one-endpoint",
          "SHELL-thin-curvature-intermediate"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-product-low-optical.md",
            "rounds/polya-main/round_005/responses/thin-shell-product-incumbent.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-clean-room.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-adversarial.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-constants-audit.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-analytic.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-alternative.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md",
            "computations/thin_shell_product_diagnostic.py",
            "computations/tests/test_thin_shell_product_diagnostic.py"
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
          "SHELL-angular-cutoff"
        ],
        "falsification_cases": [
          "a=0",
          "a=m pi under strict radial counting",
          "ell(ell+1) at an angular wall",
          "epsilon=1/100",
          "a=4 pi",
          "a=pi/(4 epsilon)",
          "direction of the min-max comparison",
          "angular multiplicity M_n^2"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_005/reviews/thin-shell-product-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_005/reviews/thin-shell-product-adversarial.md",
          "rounds/polya-main/round_005/reviews/thin-shell-product-constants-audit.md"
        ],
        "reason_for_promotion": "The exact product-index majorant, angular ceiling, strict radial deficit, quarter-disk bound, and all three parameter subranges passed an isolated clean-room proof, adversarial review, and corrected constants audit. Round 4 spectral completeness makes the min-max comparison an actual shell count theorem.",
        "next_action": "Use this theorem as the low-optical part of the thin-shell endpoint. Do not extend the flat product majorant beyond the stated range."
      },
      {
        "id": "SHELL-thin-curvature-intermediate",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Radius-sensitive intermediate thin-shell estimate",
        "status": "open",
        "statement_tex": "For rho=1-epsilon with epsilon sufficiently small, prove the shell Polya estimate throughout the intermediate optical-width region left between K=pi/(4 epsilon^2) and K=K_0(1-epsilon), or improve the low- and high-energy bounds until they overlap. The proof must retain enough r-dependence in ell(ell+1)/r^2 to recover the mean shell cross-section; replacing r^{-2} by 1 is insufficient.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-thin-product-low-optical",
          "SHELL-fixed-rho-high-energy"
        ],
        "implies": [
          "SHELL-rho-one-endpoint"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-product-low-optical.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-clean-room.md"
          ],
          "negative": [
            "rounds/polya-main/round_005/responses/thin-shell-product-incumbent.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-analytic.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-alternative.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md"
          ],
          "inconclusive": []
        },
        "owner": "A2",
        "criticality": "bottleneck",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-thin-product-low-optical",
          "SHELL-fixed-rho-high-energy"
        ],
        "falsification_cases": [
          "epsilon a/pi near 3/4",
          "exact product-proxy failure walls",
          "epsilon tending to zero with a proportional to epsilon^{-1}",
          "whispering-gallery angular modes near the outer boundary",
          "failure to overlap epsilon K_0(1-epsilon)",
          "using a pointwise potential minimum as an averaged radius correction"
        ],
        "clean_room_artifacts": [],
        "adversarial_review_artifacts": [],
        "next_action": "Develop a curvature-corrected comparison or a thin-scaled aggregate phase-lattice estimate. It must match the factor epsilon^{-1} int_{1-epsilon}^1 r^2 dr=1-epsilon+epsilon^2/3 and explicitly overlap either the proved low-optical range or K_0."
      }
    ],
    "update": [
      {
        "id": "SHELL-rho-one-endpoint",
        "dependencies_added": [
          "SHELL-thin-product-low-optical",
          "SHELL-thin-curvature-intermediate"
        ],
        "blockers_added": [
          "SHELL-thin-curvature-intermediate"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-product-low-optical.md",
            "rounds/polya-main/round_005/responses/thin-shell-product-incumbent.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-clean-room.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-adversarial.md",
            "rounds/polya-main/round_005/reviews/thin-shell-product-constants-audit.md"
          ],
          "negative": [
            "rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md"
          ]
        },
        "next_action": "The actual shell inequality is proved for epsilon<=1/100 and K<=pi/(4 epsilon^2), while fixed-rho high energy starts only at K_0(1-epsilon). Close the radius-sensitive intermediate gap; the flat product majorant is rejected as a global route."
      },
      {
        "id": "SHELL-rho-uniformity",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-product-low-optical.md"
          ],
          "negative": [
            "rounds/polya-main/round_005/exploration/thin-shell-product-analytic.md",
            "rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md"
          ]
        },
        "next_action": "The thin endpoint now has a proved low-optical range but an explicit unbounded intermediate gap. Close SHELL-thin-curvature-intermediate, then combine it with compact-rho and small-hole coverage."
      },
      {
        "id": "SHELL-rho-compact",
        "next_action": "Use rho<=0.99 as the compact side of the new thin split. Bound K_0 on the chosen compact interval and formulate its bounded interval certificate; COMP-certified-bessel remains open."
      },
      {
        "id": "COMP-certified-bessel",
        "evidence_added": {
          "inconclusive": [
            "computations/thin_shell_product_diagnostic.py",
            "computations/tests/test_thin_shell_product_diagnostic.py",
            "rounds/polya-main/round_005/exploration/thin-shell-product-diagnostic.md"
          ]
        },
        "next_action": "Do not attempt to certify the unbounded thin intermediate region. First close SHELL-thin-curvature-intermediate and the small-hole endpoint, then certify the resulting bounded residual boxes with strict root and floor walls."
      },
      {
        "id": "TARGET-shell-d3",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-product-low-optical.md"
          ]
        },
        "next_action": "The fixed-rho high-energy theorem and a uniform low-optical thin-shell range are proved. The radius-sensitive thin intermediate region, small-hole endpoint, compact certification, and final theorem audit remain open."
      }
    ],
    "reject": [
      {
        "id": "flat-product-majorant-closes-thin-shell-endpoint",
        "reason": "Reject the outer-minimum comparison r^{-2}>=1 as a global thin-shell proof. The exact product majorant exceeds the shell Weyl target at infinitely many radial walls for every fixed epsilon>0 and for an exact family epsilon=1/Q tending to zero. This rejects the majorant, not the shell inequality."
      },
      {
        "id": "flat-product-majorant-overlaps-current-fixed-rho-threshold",
        "reason": "Reject a two-piece covering by the flat product range below and K>=K_0(1-epsilon) above. Exact product-majorant failure occurs at optical width of order epsilon^{-1}, whereas epsilon K_0(1-epsilon) is of order epsilon^{-3}; an intermediate radius-sensitive estimate is necessary."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The parent endpoint remains open because the new low-optical theorem and existing high-energy theorem do not overlap."
      },
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "Round 5 did not address the small-hole endpoint."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "No all-K, all-rho shell theorem is proved."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 5,
    "reason": "A rigorously reviewed uniform thin-shell window is proved and a tempting global product route is exactly falsified. The endpoint remains open because a radius-sensitive intermediate range is still uncovered."
  }
}

## State boundary after Round 5

For $0<1-\rho\le1/100$, the shell theorem is now proved through
$K=\pi/[4(1-\rho)^2]$ and again above the pointwise threshold
$K_0(\rho)$. The interval between those ranges is not covered.
