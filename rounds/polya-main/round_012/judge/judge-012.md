# Round 12 Judge

Date: 2026-07-13

## Decision

Promote the enlarged central--thin seam theorem

$$
\boxed{
0<\varepsilon\le\frac1{20},
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
\boxed{K_0(19/20)<3300^2}.
$$

Therefore the central--thin seam moves from $\rho=24/25$ to
$\rho=19/20$, and the all-ratio analytic ceiling becomes

$$
\boxed{
0<\rho<1,
\qquad K\ge3300^2.
}
$$

This is a high-frequency theorem. It does not enlarge the complete
all-frequency endpoint $99/100\le\rho<1$ and does not close the compact
residual below the new ceiling.

## Three independent finite-constant routes

The incumbent rederives the enlarged-domain local-plateau proof with

$$
d>\frac{39}{50},
\qquad
\widehat q<\frac{27}{100},
\qquad
R<\frac{23}{5\sqrt\varepsilon}.
$$

Its complete fixed-$r$ synthetic path leaves the exact endpoint reserve

$$
\frac{4189934997169}{10140435204025}>0,
$$

and the dangerous payment satisfies

$$
M-4\delta>\frac{233}{25}>0.
$$

The independent constant inventory instead uses

$$
d>\frac34,
\qquad
\widehat q<\frac{11}{40},
\qquad
R<\frac{23}{5\sqrt\varepsilon},
$$

with a different derivative bound and endpoint reserve

$$
\frac{2196261729217}{5173691430625}>0.
$$

The strictly isolated clean-room proof uses no fixed-$r$ derivative. It
first proves $P<10$, then excludes the complete rectangle
$5\le r\le P<10$, obtaining

$$
R<\frac5{\sqrt\varepsilon}.
$$

All three routes include the no-drop endpoint, the first positive-loss
branch, and the full possible unit floor loss.

## Exact central endpoint and closed union

At $\rho=19/20$,

$$
a_\rho=38\pi<11^2,
\qquad
\eta_\rho>\frac{14000}{4199283},
\qquad
C_0<\frac{307}{175}.
$$

For $Y=3300$, the defining quadratic has the exact positive margin

$$
\frac{14000}{4199283}Y^2
-11Y-\frac{307}{175}
=\frac{32985481}{7422975}>0.
$$

Its unique positive root is therefore below $3300$, proving the stated
$K_0$ bound.

The closed analytic zones after promotion are:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,19/20]$ has
   $K<K_0(19/20)<3300^2$;
3. on $[19/20,24/25]$, the new seam threshold is at most $15000$;
4. on $[24/25,99/100]$, the sharper retained threshold is at most $200000$;
5. every frequency on $[99/100,1)$ is already proved.

All shared faces are closed. Since both finite seam ceilings are below
$3300^2$, these zones prove the all-ratio result. Relative to Round 11, the
global ceiling falls by the exact factor

$$
\frac{6000^2}{3300^2}=\frac{400}{121}>3.
$$

## Review gates

- Frozen dependency packet: PASS.
- Incumbent enlarged-domain proof: PASS.
- Independent finite-constant inventory: PASS.
- Strictly isolated clean-room proof with the distinct $B=5$ rectangle
  argument: PASS.
- Adversarial constants, path, branch, dependency, wall, face, and global
  union audit: PASS.
- Permanent exact ledger for all three finite chains: PASS.
- Focused Round 12 tests: 4 passed.
- Complete computation suite: 40 passed.
- Markdown whitespace and diff checks: PASS.

No Bessel-root region was added. The Round 12 ledger is exact symbolic
analytic evidence, not interval spectral certification.

## State Patch

{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-central-thin-seam-compression",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon. For 0<epsilon<=1/20, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=24/epsilon^2. In addition, on 0<epsilon<=1/25 the sharper retained threshold K>=20/epsilon^2 remains valid. Threshold equality is included in both statements.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round12.md",
            "rounds/polya-main/round_012/responses/enlarged-seam-incumbent.md",
            "rounds/polya-main/round_012/exploration/enlarged-seam-constant-inventory.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md",
            "computations/round12_verify_enlarged_seam.py",
            "computations/tests/test_round12_enlarged_seam.py"
          ]
        },
        "falsification_cases": [
          "epsilon=1/100, 1/25, and 1/20",
          "K=20/epsilon^2 on the retained range and K=24/epsilon^2 on the enlarged range",
          "rho=99/100, 24/25, and 19/20 from both adjacent regimes",
          "no-drop p=n, immediate-drop p=0, degenerate head n=0, sign wall R=0, and the first R>0 branch",
          "the complete synthetic comparison path for each proof route",
          "ordinary-floor, gain, interface, threshold, and strict spectral walls",
          "K=K_0(19/20) and K=3300^2",
          "any inference that the all-frequency endpoint extends below rho=99/100"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md"
        ],
        "reason_for_promotion": "The enlarged-domain local-plateau theorem was independently reconstructed on the full epsilon<=1/20 domain. The incumbent/inventory loss cap B=23/5 and the distinct clean-room cap B=5, all exceptional branches, strict walls, the exact central endpoint, and the closed global union passed adversarial review and executable exact-ledger reproduction.",
        "next_action": "Retain the sharper K>=20/epsilon^2 theorem on epsilon<=1/25 and use K>=24/epsilon^2 only for the enlarged seam through epsilon=1/20. Round 13 may test a separately frozen extension to epsilon<=1/16 with candidate K>=32/epsilon^2; no Round 12 estimate may be extrapolated."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_12=[rho_*,99/100]. On [rho_*,1/16], every possible residual has K<64. On [1/16,19/20], every possible residual has K<K_0(19/20)<3300^2. On [19/20,24/25], every possible residual has K<24/(1-rho)^2<=15000. On [24/25,99/100], the sharper retained seam leaves K<20/(1-rho)^2<=200000. Consequently the strict shell Polya inequality holds for rho in I_12 and K>=3300^2; with the unchanged endpoint lemmas it holds for every 0<rho<1 and K>=3300^2.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round12.md",
            "rounds/polya-main/round_012/responses/enlarged-seam-incumbent.md",
            "rounds/polya-main/round_012/exploration/enlarged-seam-constant-inventory.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md",
            "computations/round12_verify_enlarged_seam.py",
            "computations/tests/test_round12_enlarged_seam.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=19/20",
          "rho=24/25",
          "rho=99/100",
          "K equal to every component threshold",
          "K=K_0(19/20) and K=3300^2",
          "K=24/(1-rho)^2 and K=20/(1-rho)^2 on their closed seam domains",
          "exact comparisons 15000<200000<3300^2<6000^2",
          "the all-frequency endpoint beginning, unchanged, at rho=99/100",
          "closed planning envelope confused with the true certification target"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md"
        ],
        "reason_for_promotion": "The audited enlarged seam moves the central switch to rho=19/20. The exact endpoint estimate K_0(19/20)<3300^2 dominates the seam ceilings 15000 and 200000, while the all-frequency endpoint remains rho>=99/100; hence the complete all-ratio high-frequency ceiling is 3300^2.",
        "next_action": "Use I_12 and K<3300^2 as the compact planning boundary, but certify or prove only the true residual complement of the accepted analytic cover. Round 13 may test a separately frozen seam at rho=15/16, with candidate epsilon<=1/16, K>=32/epsilon^2, and K_0(15/16)<2100^2."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round12.md",
            "rounds/polya-main/round_012/responses/enlarged-seam-incumbent.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes the true residual on I_12 below K=3300^2. Do not replace the piecewise complement of the accepted cover by a rectangular sweep."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_12 with K<3300^2; the Round 12 exact rational ledgers are symbolic analytic evidence, not Bessel-root certificates."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round12.md",
            "rounds/polya-main/round_012/responses/enlarged-seam-incumbent.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md"
          ]
        },
        "next_action": "Both all-frequency endpoint neighborhoods and the all-ratio range K>=3300^2 are proved. Keep this obligation open until the compact residual below that ceiling is exactly closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round12.md",
            "rounds/polya-main/round_012/responses/enlarged-seam-incumbent.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-clean-room.md",
            "rounds/polya-main/round_012/reviews/enlarged-seam-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is proved for every ratio when K>=3300^2. Complete exact compact coverage below that ceiling, then run fresh theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The complete all-frequency thin endpoint remains exactly 99/100<=rho<1; Round 12 is high-frequency only."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "Its fixed-rho theorem and formula K_0(rho) are unchanged; Round 12 only supplies a new exact evaluation at rho=19/20."
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
        "reason": "The theorem remains open below K=3300^2 and still requires final theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 12 moves the central--thin seam from rho=24/25 to rho=19/20 and lowers the complete all-ratio high-frequency ceiling from 6000^2 to 3300^2 by the exact factor 400/121>3, but supplies no new certified residual coverage and does not enlarge the all-frequency endpoint."
  }
}

## State boundary after Round 12

The strict shell Pólya inequality is proved for every frequency in

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1,
$$

and for every ratio whenever $K\ge3300^2$. The full all-frequency theorem
remains open on the true compact residual below that ceiling. Any Round 13
seam extension requires a separately frozen full-domain proof; no Round 12
estimate may be extrapolated.
