# Round 3 Fixed-Rho Continuation Judge

## Verdict

The fixed-$\rho$ high-energy multiplicity-weighted lattice obligation is proved for every $0<\rho<1$ with an explicit threshold. The new ingredient is a quantitative no-shelf estimate on the concave head: equality of the first and last floor on the initial plateau forces its length to be $O_\rho(\sqrt K)$. The sharpened concave trapezoidal theorem and the improved convex $G_K$ theorem then supply an $O_\rho(K)$ gain, which dominates the plateau and the sub-unit interface loss.

The exact threshold is

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
$$

where

$$
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
\eta_\rho=G_1\!\left(\max\{\rho,1/2\}\right),\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

The incumbent passed a clean-room reconstruction, a targeted independent falsification pass, and an adversarial audit. This proves the high-energy weighted proxy. It does not prove the full shell theorem: separated Sturm--Liouville completeness, the finite parameter region, and $\rho$-endpoint uniformity remain open.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-low-interface-fixed-rho-high-energy",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Fixed-rho high-energy shifted tails across the inner interface",
        "status": "proved_internal",
        "statement_tex": "Let eta_rho=G_1(max{rho,1/2}), a_rho=2 pi rho/(1-rho), C_0=1+8 sqrt(2)/15, and K_0(rho)=((sqrt(a_rho)+sqrt(a_rho+4 eta_rho C_0))/(2 eta_rho))^2. For every fixed 0<rho<1, every K>=K_0(rho), and every integer r>=0 with r+1/2<rho K, the coarse ordinary-floor shifted tail of A_{rho,K}+1/4 is at most 2 int_{r+1/2}^K A_{rho,K}(z) dz.",
        "dependencies": [
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-weighted-lattice-fractional",
          "SHELL-fixed-rho-high-energy"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            "rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md",
            "rounds/polya-main/round_003/reviews/low-interface-small-hole-adversarial.md",
            "sources/annuli_polya.md"
          ],
          "negative": [],
          "inconclusive": [
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
          "n=0",
          "no floor drop on the concave head",
          "immediate first floor drop",
          "rho K on a half-integer",
          "the split point on either side of K/2",
          "rho=1/2",
          "K eta_rho on an integer wall",
          "K=K_0(rho)",
          "rho approaching zero or one"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
        ],
        "reason_for_promotion": "The frozen proof passed a clean-room reconstruction, a separate targeted falsification pass, and an adversarial review. The reviews verified the first-floor-drop theorem, no-drop and n=0 branches, quantitative curvature bound, convex-tail theorem, interface estimate, compensation algebra, integer walls, and explicit positive-root threshold.",
        "next_action": "Use this lemma only for the fixed-rho high-energy proxy. The finite region, rho-endpoint uniformity, and separated spectral completeness remain separate obligations."
      }
    ],
    "update": [
      {
        "id": "SHELL-weighted-lattice-fractional",
        "status": "proved_internal",
        "dependencies_removed": [
          "SHELL-low-interface-shifted-tails"
        ],
        "dependencies_added": [
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "blockers_removed": [
          "SHELL-low-interface-shifted-tails"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            "rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
          ]
        },
        "permitted_dependencies_added": [
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy",
          "SRC-FLPS-balls"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
        ],
        "reason_for_promotion": "The exact weighted scaffold, all high-angular tails, and the new fixed-rho low-interface high-energy lemma together prove the coarse ordinary-floor proxy, hence also the strict and optimized phase proxies, for every fixed rho above the explicit K_0(rho). Independent and adversarial reviews passed.",
        "next_action": "Use the proved high-energy proxy in the conditional shell count. Do not extend it to the finite window or to a rho-uniform theorem without separate evidence."
      },
      {
        "id": "SHELL-low-interface-shifted-tails",
        "dependencies_added": [
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
          ]
        },
        "next_action": "The fixed-rho high-energy part is discharged and no longer blocks the weighted proxy. The unrestricted all-K strengthening remains open; finite theorem closure belongs to certified computation and endpoint analysis."
      },
      {
        "id": "SHELL-lattice-count",
        "status": "derived_under_assumptions",
        "blockers": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-weighted-lattice-fractional.md",
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            "rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
          ]
        },
        "reason_for_promotion": "The multiplicity-weighted proxy is proved in the fixed-rho high-energy range. Converting it into an eigenvalue count still uses the strict phase-count identity under the open separated-spectrum completeness assumption.",
        "next_action": "Discharge SHELL-sturm-liouville-completeness, then upgrade the conditional phase-count bridge."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "status": "derived_under_assumptions",
        "blockers": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            "rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md"
          ]
        },
        "reason_for_promotion": "For every fixed rho the phase enclosure and weighted lattice proxy now give the claimed high-energy Weyl bound with explicit K_0(rho), conditional only on the recorded separated-spectrum completeness/count bridge.",
        "next_action": "Prove SHELL-sturm-liouville-completeness and promote the strict count bridge; do not call the conditional result a shell theorem before then."
      },
      {
        "id": "COMP-certified-bessel",
        "next_action": "Use the explicit K_0(rho) to define the fixed-rho finite window. Before certification, combine it with rho-endpoint analysis because K_0(rho) is not uniform as rho approaches one; retain rigorous interval handling of all floor and eigenvalue walls."
      },
      {
        "id": "SHELL-rho-uniformity",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md"
          ]
        },
        "next_action": "Combine the explicit fixed-rho threshold with the exact zero region (1-rho)K<=pi and derive a compact covering near rho=0 and rho=1. The current K_0(rho) diverges as rho approaches one and is not a uniform endpoint argument."
      },
      {
        "id": "TARGET-shell-d3",
        "next_action": "The high-energy weighted analytic blocker is discharged. Prioritize separated Sturm-Liouville completeness, rho-endpoint uniformity, and certified closure of the remaining parameter region; no shell Polya theorem is yet proved."
      }
    ],
    "reject": [
      {
        "id": "abstract-s-shape-lipschitz-tail-theorem",
        "reason": "Reject deriving the shifted-tail inequality solely from nonnegativity, strict decrease, C1 regularity, one concave-to-convex transition, and Lipschitz constant below 1/2. The exact C1 counterexample in the adversarial review has shifted floor count 3 but twice its integral is 191/64<3. The successful shell proof requires the quantitative curvature/no-shelf bound."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-sturm-liouville-completeness",
        "reason": "This independent spectral bridge remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "No full shell theorem is proved; finite and endpoint-uniform closure remain open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "The principal fixed-rho high-energy weighted lattice bottleneck is solved with an explicit threshold after independent review. The result remains conditional at the spectral bridge and leaves an unbounded endpoint-sensitive finite region, so no shell Polya theorem is claimed."
  }
}
```
