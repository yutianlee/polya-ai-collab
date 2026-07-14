# Round 13 Judge

Date: 2026-07-14

## Decision

Promote the enlarged central--thin seam theorem

$$
\boxed{
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2}.
}
$$

It proves

$$
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

throughout that closed parameter domain, including threshold equality. On
$0<\varepsilon\le1/25$, the sharper retained Round 10 threshold
$20/\varepsilon^2$ remains authoritative.

The separately audited fixed-ratio calculation proves

$$
\boxed{K_0(9/10)<900^2}.
$$

Therefore the central--thin seam moves from $\rho=19/20$ to $\rho=9/10$,
and the all-ratio analytic ceiling becomes

$$
\boxed{
0<\rho<1,
\qquad K\ge900^2.
}
$$

This is a high-frequency theorem. It does not enlarge the complete
all-frequency endpoint $99/100\le\rho<1$ and does not close the compact
residual below the new ceiling.

## Independent proof routes

The incumbent rederives the complete enlarged-domain local-plateau proof
with

$$
d>\frac23,
\qquad
\widehat q<\frac37,
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

Its complete fixed-$r=B$ synthetic path has derivative reserve

$$
6-\frac{1572142117}{270000000}
=\frac{47857883}{270000000}>0,
$$

endpoint reserve

$$
\frac{2376966388822}{5818105805625}>0,
$$

and dangerous payment reserve

$$
\frac{170244091}{27217575}>0.
$$

An independently isolated finite-constant inventory reconstructs that
entire chain before inspecting the executable ledger.

The strictly isolated clean-room proof uses a different direct localization

$$
\frac{x_0}{K}>
\frac{8663}{16800}
=\frac{18}{35}+\frac{23}{16800},
$$

and a distinct affine path

$$
L(X)=\frac52X-7,
\qquad
F(X)=X^2(1-h_X)^2-2\pi^2Q_X.
$$

It proves

$$
F(B)>\frac{12760228}{48234375}>0,
\qquad
F'(X)>\frac{229}{2646}>0,
$$

on the complete path and obtains the independent payment reserve $307/55$.
Both analytic routes include the no-drop endpoint, the first positive-loss
branch, and the full possible unit floor loss.

## Exact central endpoint and closed union

At $\rho=9/10$,

$$
a_\rho=18\pi<8^2,
\qquad
\eta_\rho>\frac1{107},
\qquad
C_0<\frac{307}{175}.
$$

For $Y=900$, the defining quadratic has exact positive margin

$$
\frac1{107}Y^2-8Y-\frac{307}{175}
=\frac{6897151}{18725}>0.
$$

Its unique positive root is therefore below $900$, proving the stated
$K_0$ bound.

The closed analytic zones after promotion are:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,9/10]$ has
   $K<K_0(9/10)<900^2$;
3. on $[9/10,19/20]$, the new seam threshold is at most $9600$;
4. on $[19/20,24/25]$, the retained Round 12 threshold is at most $15000$;
5. on $[24/25,99/100]$, the sharper Round 10 threshold is at most $200000$;
6. every frequency on $[99/100,1)$ is already proved.

All shared faces are closed. Since

$$
64<9600<15000<200000<900^2,
$$

these zones prove the all-ratio result. Relative to Round 12, the global
ceiling falls by the exact factor

$$
\frac{3300^2}{900^2}=\frac{121}{9}>13.
$$

## Review gates

- Corrected frozen dependency packet: PASS.
- Incumbent enlarged-domain proof: PASS.
- Independently isolated finite-constant inventory: PASS.
- Strictly isolated clean-room proof with a distinct affine synthetic path:
  PASS.
- Fresh adversarial constants, path, branch, dependency, wall, face, and
  global-union audit: PASS; first unsupported implication: none.
- Permanent exact ledger for both analytic paths: PASS.
- Embedded incumbent ledger: PASS.
- Focused Round 13 tests: 5 passed.
- Complete computation suite: 45 passed.
- Proof-graph, evidence-path, Markdown whitespace, and diff checks: PASS.

No Bessel-root region was added. The Round 13 ledger is exact symbolic
analytic evidence, not interval spectral certification.

## State Patch

{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-central-thin-seam-compression",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon. For 0<epsilon<=1/10, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=24/epsilon^2. In addition, on 0<epsilon<=1/25 the sharper retained threshold K>=20/epsilon^2 remains valid. Threshold equality is included in both statements.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round13.md",
            "rounds/polya-main/round_013/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_013/exploration/seam-extension-constant-inventory.md",
            "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md",
            "computations/round13_verify_seam_extension.py",
            "computations/tests/test_round13_seam_extension.py"
          ]
        },
        "falsification_cases": [
          "epsilon=1/100, 1/25, 1/20, and 1/10",
          "K=20/epsilon^2 on the retained Round 10 range and K=24/epsilon^2 on the enlarged range",
          "rho=99/100, 24/25, 19/20, and 9/10 from both adjacent regimes",
          "no-drop p=n, immediate-drop p=0, degenerate head n=0, sign wall R=0, and the first R>0 branch",
          "the wall mu-x_0 in Z, both adjacent beta cells, q=mu, and the low/high interface x_0=mu",
          "the complete synthetic P-comparison path, including P=r=B=14/3",
          "every monotonicity used to place a worst case at epsilon=1/10 or kappa=24",
          "ordinary-floor, coarse-proxy, gain, interface, threshold, angular-cutoff, and strict spectral walls",
          "K=K_0(9/10) and K=900^2",
          "any inference that the all-frequency endpoint extends below rho=99/100"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md"
        ],
        "reason_for_promotion": "The enlarged-domain local-plateau theorem was independently reconstructed on the full epsilon<=1/10 domain. The incumbent and constant inventory close the fixed-r=B=14/3 comparison, while the isolated clean-room proof uses a distinct affine synthetic path. All exceptional branches, strict walls, the exact central endpoint, and the closed global union passed adversarial review and executable exact-ledger reproduction.",
        "next_action": "Retain the sharper K>=20/epsilon^2 theorem on epsilon<=1/25 and use the proved K>=24/epsilon^2 theorem only through epsilon=1/10. Any further seam extension requires a separately frozen full-domain proof and endpoint calculation; no Round 13 estimate may be extrapolated."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_13=[rho_*,99/100]. On [rho_*,1/16], every possible residual has K<64. On [1/16,9/10], every possible residual has K<K_0(9/10)<900^2. On [9/10,19/20], every possible residual has K<24/(1-rho)^2<=9600. On [19/20,24/25], every possible residual has K<24/(1-rho)^2<=15000. On [24/25,99/100], the sharper retained seam leaves K<20/(1-rho)^2<=200000. Consequently the strict shell Polya inequality holds for rho in I_13 and K>=900^2; with the unchanged endpoint lemmas it holds for every 0<rho<1 and K>=900^2.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round13.md",
            "rounds/polya-main/round_013/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_013/exploration/seam-extension-constant-inventory.md",
            "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md",
            "computations/round13_verify_seam_extension.py",
            "computations/tests/test_round13_seam_extension.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=9/10",
          "rho=19/20",
          "rho=24/25",
          "rho=99/100",
          "K equal to every component threshold",
          "K=K_0(9/10) and K=900^2",
          "K=24/(1-rho)^2 and K=20/(1-rho)^2 on their closed seam domains",
          "exact comparisons 64<9600<15000<200000<900^2 and 3300^2/900^2=121/9>13",
          "the all-frequency endpoint beginning, unchanged, at rho=99/100",
          "closed five-zone planning envelope confused with the true residual certification target"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md"
        ],
        "reason_for_promotion": "The audited enlarged seam moves the central switch to rho=9/10. The exact endpoint estimate K_0(9/10)<900^2 dominates the seam ceilings 9600, 15000, and 200000, while the all-frequency endpoint remains rho>=99/100; hence the complete all-ratio high-frequency ceiling is 900^2.",
        "next_action": "Use I_13 and K<900^2 as the compact planning boundary, but certify or prove only the true residual complement of the accepted five-zone analytic cover. Do not replace that piecewise complement by a rectangular sweep."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round13.md",
            "rounds/polya-main/round_013/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes the true residual on I_13 below K=900^2. Do not replace the piecewise complement of the accepted five-zone cover by a rectangular sweep."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_13 with K<900^2; the Round 13 exact rational ledgers are symbolic analytic evidence, not Bessel-root certificates."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round13.md",
            "rounds/polya-main/round_013/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "Both all-frequency endpoint neighborhoods and the all-ratio range K>=900^2 are proved. Keep this obligation open until the compact residual below that ceiling is exactly closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round13.md",
            "rounds/polya-main/round_013/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_013/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_013/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is proved for every ratio when K>=900^2. Complete exact compact coverage below that ceiling, then run fresh theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The complete all-frequency thin endpoint remains exactly 99/100<=rho<1; Round 13 is high-frequency only."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "Its fixed-rho theorem and formula K_0(rho) are unchanged; Round 13 only supplies a new exact evaluation at rho=9/10."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "The residual ceiling is lower, but the residual below it is not closed."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No new Bessel-root region was certified; the executable ledger is exact symbolic analytic evidence."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "All-ratio high energy is improved, but compact all-frequency closure remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The theorem remains open below K=900^2 and still requires final theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 13 moves the central--thin seam from rho=19/20 to rho=9/10 and lowers the complete all-ratio high-frequency ceiling from 3300^2 to 900^2 by the exact factor 121/9>13, but supplies no new certified residual coverage and does not enlarge the all-frequency endpoint."
  }
}

## State boundary after Round 13

The strict shell Pólya inequality is proved for every frequency in

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1,
$$

and for every ratio whenever $K\ge900^2$. The full all-frequency theorem
remains open on the true compact residual below that ceiling. Any Round 14
seam extension requires a separately frozen full-domain proof; no Round 13
estimate may be extrapolated.
