# Round 9 Judge: Optimized Thin Plateau and Global High-Energy Ceiling

## Verdict

Round 9 proves the optimized high-frequency thin-shell theorem

$$
\boxed{
0<\varepsilon\le\frac1{100},\qquad
K\ge\frac{125}{8\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

The threshold equality is included.  The proof imports only the
pre-threshold Round 3 shifted-tail decomposition, its unconditional global
plateau estimate, and the already-promoted phase, weighted-scaffold,
high-interface-tail, and spectral bridge results.  It does not import the
old conclusion under $K\ge64\varepsilon^{-2}$.

The decisive clean-room improvement is to retain the compensated interface
loss

$$
R=p-dm
$$

instead of bounding $p$ after discarding $dm$.  With
$y=\sqrt\varepsilon$, $\kappa=K\varepsilon^2$,
$P=py$, and $r=Ry$, the proof shows

$$
R<\frac{361}{80\sqrt\varepsilon}.
\tag{2}
$$

The extremal comparison is the genuine no-drop geometry $m=0$.  Its exact
endpoint margin is

$$
\frac{72581986185449}{5925464687161600}>0,
$$

and the final gain-versus-interface margin is

$$
\frac{2829397}{3732696}-\frac{132}{175}
=\frac{2428603}{653221800}>0.
\tag{3}
$$

The synthetic comparison path, monotonicity in both scaled variables, the
no-drop, immediate-drop, and degenerate-head branches, and all interface,
ordinary-floor, gain, threshold, and strict spectral walls passed separate
dependency and targeted adversarial audits.

The direct incumbent theorem with $C=18$ also passed an isolated
reconstruction and exact rational checking.  It is retained as a simpler,
independently verified fallback, but it is not the promoted Round 9
constant because the separately reconstructed and adversarially audited
$C=125/8$ theorem is stronger.  Neither constant is claimed optimal.

## Enlarged thin endpoint

The already-proved aggregate-action theorem includes

$$
K\le\frac1{8\varepsilon^{5/2}}.
$$

Together with (1), the two inclusive ranges overlap exactly when

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
125\sqrt\varepsilon\le1
\iff
\varepsilon\le\frac1{15625}.
$$

At equality their common frequency is

$$
K_{\rm join}=\frac{125^5}{8}<2^{32}.
$$

Therefore the all-frequency thin endpoint is strengthened to

$$
\boxed{
1-\frac1{15625}\le\rho<1,\qquad K\ge0
\Longrightarrow\text{the strict shell Pólya inequality.}
}
\tag{4}
$$

The lower ratio face in (4) is included and $\rho=1$ remains excluded as
the degenerate zero-width limit.

## Updated compact and all-ratio envelope

Let

$$
I_9=\left[\rho_*,1-\frac1{15625}\right],
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The Round 8 left and central zones are unchanged:

1. on $[\rho_*,1/16]$, every possible residual has $K<64$;
2. on $[1/16,99/100]$, every possible residual has
   $K<K_0(99/100)<180000^2<2^{35}$.

On the new thin compact strip, with
$1/15625\le\varepsilon\le1/100$, a possible residual must satisfy

$$
\frac1{8\varepsilon^{5/2}}
<K<\frac{125}{8\varepsilon^2}
\le\frac{125^5}{8}<2^{32}.
$$

Thus

$$
\boxed{
\rho\in I_9,\qquad K\ge2^{35}
\Longrightarrow\text{the strict shell Pólya inequality.}
}
\tag{5}
$$

Combining (4), (5), and the already-proved all-frequency small-hole
endpoint gives the new global high-energy theorem

$$
\boxed{
0<\rho<1,\qquad K\ge2^{35}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{6}
$$

This lowers the previous uniform high-energy ceiling by the factor $2^7$.
It does not cover the remaining compact residual below $2^{35}$.

## Exact checks and evidence boundary

The executable checker uses `fractions.Fraction` and no floating-point
arithmetic.  It reproduces the finite rational ledgers for both $C=18$ and
$C=125/8$, including (3), the no-drop endpoint margin, the derivative bound
$673816/1366875<1/2$, both exact overlaps, and
$125^5/8<2^{32}$.  The focused tests exercise both ledgers.  These exact
checks corroborate the analytic monotonicity and branch proofs; they do not
replace them and are not a Bessel-root certificate.

The complete positive evidence set used for promotion is:

- frozen optimized packet:
  `state/lemma_packets/SHELL-thin-local-plateau-optimized.md`;
- direct $C=18$ fallback and optimized-envelope corollary:
  `rounds/polya-main/round_009/responses/thin-plateau-optimized-incumbent.md`,
  `rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md`;
- isolated $C=125/8$ clean-room reconstruction:
  `rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md`;
- dependency audit and post-update resolution:
  `rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md`;
- isolated fallback referee and targeted primary adversarial referee:
  `rounds/polya-main/round_009/reviews/thin-plateau-c18-isolated-referee.md`,
  `rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md`;
- exact-arithmetic report, checker, and tests:
  `rounds/polya-main/round_009/exploration/exact-constant-check.md`,
  `computations/round9_verify_thin_plateau_constants.py`,
  `computations/tests/test_round9_thin_plateau_constants.py`.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-thin-local-plateau-optimized",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Optimized uniform local-plateau high-energy bound for thin shells",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/100. Then the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=125/(8 epsilon^2), including threshold equality.",
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
          "SHELL-rho-one-endpoint",
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/thin-plateau-optimized-incumbent.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c18-isolated-referee.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md",
            "rounds/polya-main/round_009/exploration/exact-constant-check.md",
            "computations/round9_verify_thin_plateau_constants.py",
            "computations/tests/test_round9_thin_plateau_constants.py"
          ],
          "negative": [],
          "inconclusive": []
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
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-fixed-rho-high-energy"
        ],
        "falsification_cases": [
          "epsilon=1/100",
          "K=125/(8 epsilon^2)",
          "no floor drop p=n",
          "immediate floor drop p=0",
          "degenerate head n=0",
          "R=0 and first dangerous R>0",
          "synthetic P-prime comparison path and inherited shelf ceiling",
          "monotonicity of H in the scaled loss and plateau variables",
          "no-drop endpoint maxima Q_* and qhat_*",
          "interface, ordinary-floor, gain, and strict spectral walls",
          "any import of a conclusion proved only under K>=64 epsilon^(-2)"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
        ],
        "reason_for_promotion": "The C=125/8 scaled-loss proof was reconstructed without the old C=64 theorem, its synthetic path, exact endpoint extrema, exceptional branches, and wall strictness passed independent dependency and targeted adversarial audits, and every finite rational margin was reproduced exactly. The independently valid C=18 proof is retained only as fallback evidence.",
        "next_action": "Use this theorem in the enlarged thin endpoint and the compressed compact envelope. Do not claim optimality of 125/8 or use the theorem to close the uncaptured compact residual."
      }
    ],
    "update": [
      {
        "id": "SHELL-thin-curvature-intermediate",
        "status": "proved_internal",
        "statement_tex": "For rho=1-epsilon with 0<epsilon<=1/15625, the strict shell Polya estimate holds for every K>=0. The proved low and aggregate ranges cover K<=1/(8 epsilon^(5/2)); SHELL-thin-local-plateau-optimized covers K>=125/(8 epsilon^2); these inclusive ranges overlap exactly because epsilon<=1/15625.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md",
            "rounds/polya-main/round_009/exploration/exact-constant-check.md",
            "computations/round9_verify_thin_plateau_constants.py",
            "computations/tests/test_round9_thin_plateau_constants.py"
          ]
        },
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized"
        ],
        "falsification_cases": [
          "epsilon=1/15625",
          "equality of 1/(8 epsilon^(5/2)) and 125/(8 epsilon^2)",
          "threshold and strict spectral walls",
          "using the old 64/epsilon^2 theorem to justify the optimized overlap"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
          "rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
        ],
        "reason_for_promotion": "The new independently audited high-thin theorem overlaps the unchanged aggregate-action range exactly at epsilon=1/15625, and both components include the joining frequency.",
        "next_action": "Treat the strengthened all-frequency overlap as discharged evidence for the enlarged rho-to-one endpoint."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "status": "proved_internal",
        "statement_tex": "For every 1-1/15625<=rho<1 and every K>=0, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. The lower rho endpoint is included and rho=1 is excluded as the degenerate zero-width limit.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized",
          "SHELL-thin-curvature-intermediate"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
          ]
        },
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized",
          "SHELL-thin-curvature-intermediate"
        ],
        "falsification_cases": [
          "rho=1-1/15625",
          "rho tending to 1",
          "joining frequency K=125^5/8",
          "strict spectral and phase-proxy walls"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-clean-room.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_006/reviews/phase-aggregate-adversarial.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
        ],
        "reason_for_promotion": "The already-proved low and aggregate ranges and the optimized high-thin theorem cover every K at every 0<epsilon<=1/15625, including the exact lower ratio face.",
        "next_action": "Treat the enlarged thin endpoint as discharged; retain its exact inclusive boundary when defining the compact residual."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_9=[rho_*,1-1/15625]. On [rho_*,1/16], every possible residual has K<64. On [1/16,99/100], every possible residual has K<180000^2<2^35. On [99/100,1-1/15625], with epsilon=1-rho, every possible residual lies between 1/(8 epsilon^(5/2)) and 125/(8 epsilon^2), hence has K<125^5/8<2^32. Consequently the strict shell Polya inequality holds for rho in I_9 and K>=2^35; with the two endpoint lemmas it holds for all 0<rho<1 and K>=2^35.",
        "dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md",
            "rounds/polya-main/round_009/exploration/exact-constant-check.md"
          ]
        },
        "permitted_dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-optimized"
        ],
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=99/100",
          "rho=1-1/15625",
          "K equal to every component threshold",
          "thin joining frequency K=125^5/8",
          "uniform compact ceiling K=2^35",
          "closed planning envelope confused with the true certification target"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_008/reviews/compact-envelope-clean-room.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_008/reviews/compact-envelope-adversarial.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
          "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
        ],
        "reason_for_promotion": "The Round 8 left and central ceilings are unchanged, while the independently audited optimized thin theorem moves the inclusive endpoint to 1-1/15625 and bounds the remaining thin strip below 2^32. Therefore the central ceiling 2^35 now controls the complete compact interval and, with both endpoint theorems, all shell ratios.",
        "next_action": "Use I_9 and the 2^35 ceiling as the exact analytic boundary for the remaining compact certificate target."
      },
      {
        "id": "SHELL-rho-compact",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until an exact manifest covers the true residual on I_9 below K=2^35. The thin part now lies below 2^32, but no new residual box was certified in Round 9."
      },
      {
        "id": "COMP-certified-bessel",
        "next_action": "The parent remains diagnostic_only. Use the compressed I_9 residual and the 2^35 global ceiling to design an exact E-minus-A manifest; do not treat the Round 9 rational constant checker as a Bessel-root certificate."
      },
      {
        "id": "SHELL-rho-uniformity",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
          ]
        },
        "next_action": "Both endpoint neighborhoods and the all-ratio high-energy range K>=2^35 are proved. Keep this obligation open until exact certified coverage closes the remaining compact residual below 2^35."
      },
      {
        "id": "TARGET-shell-d3",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-thin-local-plateau-optimized.md",
            "rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md",
            "rounds/polya-main/round_009/reviews/thin-plateau-c125-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is now proved for every ratio when K>=2^35. Complete exact coverage of the compact residual below that ceiling, then run final theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-compact",
        "reason": "The analytic target is substantially compressed, but the true compact residual below K=2^35 is not exactly covered."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "Round 9 checks analytic constants exactly but supplies no new certified Bessel-root region; the parent remains diagnostic_only."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "All-ratio high energy is proved, but uniform all-frequency closure still depends on the open compact residual."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The theorem remains open below K=2^35 on uncaptured compact-ratio residual points and still requires its final audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 9 replaces the thin high-energy constant 64 by the independently reconstructed and adversarially audited constant 125/8, enlarges the all-frequency thin endpoint to epsilon=1/15625, and lowers the complete all-ratio high-energy ceiling from 2^42 to 2^35. The score remains conservative because no new Bessel-root box or exact compact manifest was certified and the full theorem remains open."
  }
}

## State boundary after Round 9

The strict shell Pólya inequality is now analytically proved for every
$0<\rho<1$ whenever $K\ge2^{35}$.  It is also proved for every frequency
in the enlarged endpoint neighborhoods
$0<\rho\le\rho_*$ and
$1-1/15625\le\rho<1$.

The global all-frequency theorem remains open only on the true compact
residual inside $I_9$ below $2^{35}$.  Round 9 produces no new Bessel-root
certificate, so `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` retain their prior statuses.
