# Round 10 Judge

Date: 2026-07-13

## Decision

Promote the new central--thin seam lemma with

$$
\boxed{
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
}
$$

The proof rederives every estimate whose Round 9 version used
$\varepsilon\le1/100$.  It does not extrapolate the Round 9 theorem.

The incumbent proof establishes

$$
\widehat q<\frac{21}{80},
\qquad
R<\frac{73}{16\sqrt\varepsilon},
$$

with exact positive no-drop and payment margins.  The isolated clean-room
proof uses different constants,

$$
\widehat q<\frac{13}{50},
\qquad
R<\frac{23}{5\sqrt\varepsilon},
$$

and reaches the same theorem.  The adversarial audit passes after a
dependency-boundary wording correction: the global corollary reconstructs
the endpoint and left zones from their proved component lemmas rather than
using the compact envelope it is strengthening.

## Exact seam consequence

The new seam is

$$
\rho_s=\frac{24}{25}.
$$

The fixed-ratio threshold satisfies

$$
\boxed{
K_0(24/25)<6000^2=36000000.
}
$$

On the enlarged seam strip

$$
\frac{24}{25}\le\rho\le\frac{99}{100},
$$

the new high threshold is at most $200000$.  On the ultra-thin strip retain
the sharper Round 9 threshold.  Therefore the prior thin residual ceiling
becomes the global dominant ceiling:

$$
\boxed{
0<\rho<1,
\qquad
K\ge\frac{125^5}{8}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The comparisons are exact:

$$
6000^2<\frac{125^5}{8}<2^{32}<2^{35},
\qquad
2^{35}>9\frac{125^5}{8}.
$$

The moved seam removes a radius strip of width

$$
\frac{99}{100}-\frac{24}{25}=\frac3{100}
$$

from the former central plan above the explicit new high curve.

## Endpoint boundary

Round 10 does not enlarge the all-frequency thin endpoint.  Combining the
new $C=20$ theorem with the aggregate-action range would overlap only when

$$
\frac{20}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{25600},
$$

which is weaker than the already-proved endpoint
$\varepsilon\le1/15625$.  The Round 9 $C=125/8$ theorem remains authoritative
on their common domain.

## Review gates

- Frozen dependency packet: PASS.
- Incumbent enlarged-domain proof: PASS.
- Isolated clean-room reconstruction with distinct constants: PASS.
- Adversarial constants, dependency, branches, walls, and faces audit:
  PASS after the documented wording correction.
- Exact rational ledger: PASS.
- Focused Round 10 tests: PASS.
- Complete computation suite: 32 passed.

No certified Bessel-root region was added.  The exact rational ledger is
analytic verification, not interval certification.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-central-thin-seam-compression",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Central--thin seam compression by an enlarged local-plateau bound",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/25. Then the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=20/epsilon^2, including threshold equality.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression.md",
            "rounds/polya-main/round_010/exploration/parametric-domain-inventory.md",
            "rounds/polya-main/round_010/responses/central-thin-seam-incumbent.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md",
            "computations/round10_verify_seam_constants.py",
            "computations/tests/test_round10_seam_constants.py"
          ],
          "negative": [],
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
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "falsification_cases": [
          "epsilon=1/15625, 1/100, and 1/25",
          "K=125/(8 epsilon^2) and K=20/epsilon^2",
          "rho=24/25 approached from central and seam regimes",
          "rho=99/100 and ownership of the sharper Round 9 threshold",
          "no-drop p=n, immediate-drop p=0, and n=0 branches",
          "R=0 and the first R>0 branch",
          "complete synthetic comparison path",
          "ordinary-floor, gain, interface, threshold, and strict spectral walls",
          "K=K_0(24/25) and K=6000^2",
          "exact ordering of 6000^2, 125^5/8, 2^32, and 2^35",
          "any extrapolation of a Round 9 estimate proved only for epsilon<=1/100"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md"
        ],
        "reason_for_promotion": "The enlarged-domain local-plateau proof was independently reconstructed with different constants. Its dependency boundary, synthetic path, exceptional branches, exact endpoint extrema, wall ownership, and central endpoint comparison passed adversarial review, and every incumbent rational margin was reproduced by the executable ledger.",
        "next_action": "Use this theorem on 24/25<=rho<=99/100. Retain the sharper Round 9 threshold 125/(8 epsilon^2) when epsilon<=1/100; do not infer an enlarged all-frequency thin endpoint."
      }
    ],
    "update": [
      {
        "id": "SHELL-thin-local-plateau-optimized",
        "next_action": "Retain the sharper threshold 125/(8 epsilon^2) on 0<epsilon<=1/100 and use it on the ultra-thin compact strip. Do not replace it by the weaker C=20 threshold on their overlap."
      },
      {
        "id": "SHELL-thin-action-aggregate",
        "next_action": "Round 11 should enlarge the aggregate range or prove a separate intermediate bridge across the remaining aggregate-to-plateau gap for 1/15625<epsilon<=1/100, targeting a residual ceiling below 6000^2."
      },
      {
        "id": "SHELL-thin-curvature-intermediate",
        "next_action": "The all-frequency conclusion remains exactly 0<epsilon<=1/15625. Use its aggregate/high overlap as the lower side of the Round 11 ultra-thin gap problem."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "next_action": "Treat 1-1/15625<=rho<1 as discharged. Round 10 does not enlarge this all-frequency endpoint."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_10=[rho_*,1-1/15625]. On [rho_*,1/16], every possible residual has K<64. On [1/16,24/25], every possible residual has K<K_0(24/25)<6000^2. On [24/25,99/100], every possible residual has K<20/(1-rho)^2<=200000. On [99/100,1-1/15625], with epsilon=1-rho, every possible residual lies below 125/(8 epsilon^2)<=125^5/8. Consequently the strict shell Polya inequality holds for rho in I_10 and K>=125^5/8; with the two endpoint lemmas it holds for every 0<rho<1 and K>=125^5/8<2^32.",
        "dependencies_added": [
          "SHELL-central-thin-seam-compression"
        ],
        "permitted_dependencies_added": [
          "SHELL-central-thin-seam-compression"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression.md",
            "rounds/polya-main/round_010/exploration/parametric-domain-inventory.md",
            "rounds/polya-main/round_010/responses/central-thin-seam-incumbent.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md",
            "computations/round10_verify_seam_constants.py",
            "computations/tests/test_round10_seam_constants.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=24/25",
          "rho=99/100",
          "rho=1-1/15625",
          "K equal to every component threshold",
          "K=K_0(24/25) and K=6000^2",
          "K=20/(1-rho)^2 on the enlarged seam",
          "thin joining frequency and new global ceiling K=125^5/8",
          "exact comparisons 6000^2<125^5/8<2^32<2^35",
          "closed planning envelope confused with the true certification target"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md"
        ],
        "reason_for_promotion": "The audited enlarged-domain theorem moves the fixed-ratio switch from rho=99/100 to rho=24/25. The exact endpoint estimate K_0(24/25)<6000^2 and the retained Round 9 ultra-thin theorem make 125^5/8 the dominant complete all-ratio ceiling.",
        "next_action": "Use I_10 and K<125^5/8 as the exact residual boundary. Round 11 should first compress the dominant ultra-thin aggregate-to-plateau gap."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression.md",
            "rounds/polya-main/round_010/responses/central-thin-seam-incumbent.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes the true residual on I_10 below K=125^5/8. Target the dominant ultra-thin gap before attempting a large manifest."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Redefine any future E-minus-A manifest using I_10 and K<125^5/8; the Round 10 rational ledger is not a Bessel-root certificate."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression.md",
            "rounds/polya-main/round_010/responses/central-thin-seam-incumbent.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md"
          ]
        },
        "next_action": "Both endpoint neighborhoods and the all-ratio range K>=125^5/8 are proved. Keep this obligation open until the remaining compact residual below that ceiling is exactly closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression.md",
            "rounds/polya-main/round_010/responses/central-thin-seam-incumbent.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-clean-room.md",
            "rounds/polya-main/round_010/reviews/central-thin-seam-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is now proved for every ratio when K>=125^5/8<2^32. Complete exact coverage below that ceiling, then run final theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-thin-local-plateau-optimized",
        "reason": "Its C=125/8 theorem remains sharper on the common epsilon<=1/100 domain."
      },
      {
        "id": "SHELL-thin-action-aggregate",
        "reason": "Round 10 does not strengthen its upper range."
      },
      {
        "id": "SHELL-thin-curvature-intermediate",
        "reason": "Combining C=20 with the existing aggregate range overlaps only for epsilon<=1/25600, which is weaker than the existing epsilon<=1/15625 endpoint."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The all-frequency thin endpoint remains 1-1/15625<=rho<1."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "The analytic ceiling is reduced, but the residual below it is not closed."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "The exact rational ledger is symbolic analytic evidence, not certified Bessel-root coverage."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "All-ratio high energy is proved, but uniform all-frequency closure still depends on the compact residual."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The theorem remains open below K=125^5/8 and still requires theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 10 moves the central--thin seam to rho=24/25 and lowers the complete all-ratio high-energy ceiling by a factor greater than nine, from 2^35 to 125^5/8<2^32, but supplies no new certified residual coverage."
  }
}

## State boundary after Round 10

The strict shell Pólya inequality is analytically proved for every
$0<\rho<1$ whenever $K\ge125^5/8<2^{32}$.  It remains proved for every
frequency in the two endpoint neighborhoods

$$
0<\rho\le\rho_*,
\qquad
1-\frac1{15625}\le\rho<1.
$$

The all-frequency theorem remains open on the compact residual below the
new ceiling.  Round 11 should first compress the dominant ultra-thin gap

$$
\frac1{15625}<\varepsilon\le\frac1{100},
\qquad
\frac1{8\varepsilon^{5/2}}
<K<
\frac{125}{8\varepsilon^2},
$$

aiming to bring its ceiling below $6000^2$ before any large certification
manifest is attempted.
