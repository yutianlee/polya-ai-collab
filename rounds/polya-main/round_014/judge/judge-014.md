# Round 14 Judge

Date: 2026-07-14

## Decision

Promote the enlarged central--thin seam theorem

$$
\boxed{
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2}.
}
$$

It proves

$$
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

throughout that closed parameter domain, including threshold equality. The
sharper retained threshold $24/\varepsilon^2$ remains authoritative on
$0<\varepsilon\le1/10$, and $20/\varepsilon^2$ remains authoritative on
$0<\varepsilon\le1/25$.

The separately audited fixed-ratio calculation proves

$$
\boxed{K_0(7/8)<550^2}.
$$

Therefore the central--thin seam moves from $\rho=9/10$ to $\rho=7/8$,
and the all-ratio analytic ceiling becomes

$$
\boxed{
0<\rho<1,
\qquad K\ge550^2.
}
$$

This is a high-frequency theorem. It does not enlarge the complete
all-frequency endpoint $99/100\le\rho<1$ and does not close the compact
residual below the new ceiling.

## Independent proof routes

The incumbent and independent constant inventory rederive the complete
enlarged-domain local-plateau proof with

$$
d>\frac23,
\qquad
\widehat q<\frac{17}{40},
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

The incumbent's complete fixed-$r=B$ synthetic path has derivative reserve

$$
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0,
$$

endpoint reserve

$$
\frac{49714811804}{82306584375}>0,
$$

and dangerous payment reserve

$$
\frac{98646127309}{8083619775}>0.
$$

The strictly isolated clean-room proof first derives $P<9$ and then uses
the distinct affine majorant

$$
\overline S(P)=\frac52P-7.
$$

It obtains the independent endpoint and full-path derivative reserves

$$
\frac{3627793}{7225344}>0,
\qquad
\frac{1178207}{150528}>0,
$$

and the independent dangerous payment reserve $3229/275>0$. Both proof
architectures include the no-drop endpoint, the first positive-loss branch,
and the full possible unit floor loss.

The value

$$
\frac{173}{384}<\frac12
$$

is only the lower localization bound produced by the current architecture
when $\kappa=24$ at $\varepsilon=1/8$. It is not a counterexample and does
not reject a possible stronger constant-$24$ theorem.

## Exact central endpoint and closed union

At $\rho=7/8$,

$$
a_\rho=14\pi<7^2,
\qquad
\eta_\rho>\frac1{76},
\qquad
C_0<\frac{307}{175}.
$$

For $Y=550$, the defining quadratic has exact positive margin

$$
\frac1{76}Y^2-7Y-\frac{307}{175}
=\frac{427292}{3325}>0.
$$

Its unique positive root is therefore below $550$, proving the stated
$K_0$ bound.

The closed analytic zones after promotion are:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,7/8]$ has
   $K<K_0(\rho)\le K_0(7/8)<550^2$;
3. on $[7/8,9/10]$, the new seam threshold is at most $3200$;
4. on $[9/10,19/20]$, the retained Round 13 threshold is at most $9600$;
5. on $[19/20,24/25]$, the retained constant-$24$ threshold is at most
   $15000$;
6. on $[24/25,99/100]$, the sharper Round 10 threshold is at most $200000$;
7. every frequency on $[99/100,1)$ is already proved.

All moving and shared faces are closed. Since

$$
64<3200<9600<15000<200000<550^2,
$$

these zones prove the all-ratio result. Relative to Round 13, the global
ceiling falls by the exact factor

$$
\frac{900^2}{550^2}=\frac{324}{121}>2.
$$

## Review gates

- Frozen dependency packet and its SHA-256: PASS.
- Incumbent enlarged-domain proof and embedded exact ledger: PASS.
- Independently isolated finite-constant inventory: PASS.
- Strictly isolated clean-room proof with a distinct affine synthetic path:
  PASS.
- Separate read-only incumbent proof check: PASS; first unsupported
  implication: none.
- Fresh adversarial constants, path, branch, dependency, wall, face, and
  global-union audit: PASS; first unsupported implication: none.
- Permanent exact ledger for both analytic paths: PASS.
- Focused Round 14 tests: 6 passed.
- Complete computation suite: 51 passed.
- Proof graph, dependency DAG, 530 referenced evidence paths, protected
  Round 8 certificate, Markdown whitespace, and diff checks: PASS.

No Bessel-root region was added. The Round 14 ledger is exact symbolic
analytic evidence, not interval spectral certification.

## State Patch

{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-central-thin-seam-compression",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon. For 0<epsilon<=1/8, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3 for every K>=32/epsilon^2. On 0<epsilon<=1/10 the sharper retained threshold K>=24/epsilon^2 remains valid, and on 0<epsilon<=1/25 the still sharper retained threshold K>=20/epsilon^2 remains valid. Threshold equality is included in all three statements.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round14.md",
            "rounds/polya-main/round_014/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_014/exploration/seam-extension-constant-inventory.md",
            "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md",
            "computations/round14_verify_seam_extension.py",
            "computations/tests/test_round14_seam_extension.py"
          ]
        },
        "falsification_cases": [
          "epsilon=1/100, 1/25, 1/20, 1/10, and 1/8",
          "K=20/epsilon^2 on the retained Round 10 range, K=24/epsilon^2 on the retained Round 13 range, and K=32/epsilon^2 on the enlarged range",
          "rho=99/100, 24/25, 19/20, 9/10, and 7/8 from both adjacent regimes",
          "no-drop p=n, immediate-drop p=0, degenerate head n=0, sign wall R=0 from both sides, and the first R>0 branch",
          "the wall mu-x_0 in Z, both adjacent beta cells, q=mu, and the low/high interface x_0=mu",
          "every ordinary-floor, coarse-proxy, gain, interface, threshold, angular-cutoff, and strict spectral wall",
          "every denominator, radicand, and squaring condition in the self-consistency inequality",
          "both complete synthetic paths, including P=r=B=14/3 and the clean-room range B<=P<9",
          "every monotonicity used to place a worst case at epsilon=1/8 or kappa=32",
          "K=K_0(7/8), K=550^2, and every shared global-union face",
          "the value 173/384<1/2 treated only as a kappa=24 route obstruction",
          "any inference that the all-frequency endpoint extends below rho=99/100"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md"
        ],
        "reason_for_promotion": "The Round 14 local-plateau theorem was independently reconstructed on the full epsilon<=1/8, kappa>=32 domain. The incumbent and independent constant inventory close the fixed-r=B=14/3 comparison, while the strictly isolated clean-room proof uses a distinct affine comparison path. The exact K_0(7/8) endpoint, every exceptional branch, strict wall, overlap face, and the closed global union passed fresh adversarial review and executable exact-ledger reproduction.",
        "next_action": "Use the sharpest accepted thresholds piecewise: K>=20/epsilon^2 through epsilon=1/25, K>=24/epsilon^2 through epsilon=1/10, and K>=32/epsilon^2 on the newly covered range through epsilon=1/8. Any further extension or improvement requires a separately frozen full-domain proof. The kappa=24 localization value 173/384<1/2 is only an obstruction in the current route, not a disproof of a constant-24 theorem."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_14=[rho_*,99/100]. On [rho_*,1/16], every possible residual has K<64. On [1/16,7/8], every possible residual has K<K_0(rho)<=K_0(7/8)<550^2. On [7/8,9/10], every possible residual has K<32/(1-rho)^2<=3200. On [9/10,19/20], every possible residual has K<24/(1-rho)^2<=9600. On [19/20,24/25], every possible residual has K<24/(1-rho)^2<=15000. On [24/25,99/100], the sharper retained seam leaves K<20/(1-rho)^2<=200000. Consequently the strict shell Polya inequality holds for rho in I_14 and K>=550^2; with the unchanged endpoint lemmas it holds for every 0<rho<1 and K>=550^2.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round14.md",
            "rounds/polya-main/round_014/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_014/exploration/seam-extension-constant-inventory.md",
            "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md",
            "computations/round14_verify_seam_extension.py",
            "computations/tests/test_round14_seam_extension.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=7/8",
          "rho=9/10",
          "rho=19/20",
          "rho=24/25",
          "rho=99/100",
          "K=64, 2048, 2400, 3200, 9600, 12500, 15000, and 200000",
          "K=K_0(rho), K=K_0(7/8), and K=550^2",
          "K=32/(1-rho)^2, K=24/(1-rho)^2, and K=20/(1-rho)^2 on their exact closed domains",
          "exact comparisons 64<3200<9600<15000<200000<550^2 and 900^2/550^2=324/121>2",
          "the all-frequency endpoint beginning, unchanged, at rho=99/100",
          "closed six-zone planning envelope confused with the true residual certification target"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md"
        ],
        "reason_for_promotion": "The audited Round 14 seam moves the central switch to rho=7/8. The exact endpoint estimate K_0(7/8)<550^2 dominates the finite seam ceilings 3200, 9600, 15000, and 200000, while the complete all-frequency endpoint remains exactly rho>=99/100. Hence the complete all-ratio high-frequency ceiling is 550^2.",
        "next_action": "Use I_14 and K<550^2 as the compact planning boundary, but prove or certify only the true residual complement of the accepted six-zone analytic cover. Do not replace that piecewise complement by a rectangular sweep."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round14.md",
            "rounds/polya-main/round_014/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes the true residual on I_14 below K=550^2. Do not replace the piecewise complement of the accepted six-zone cover by a rectangular sweep."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_14 with K<550^2; the Round 14 exact rational ledgers are symbolic analytic evidence, not Bessel-root certificates."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round14.md",
            "rounds/polya-main/round_014/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "Both complete all-frequency endpoint neighborhoods and the all-ratio range K>=550^2 are proved. Keep this obligation open until the compact residual below that ceiling is exactly closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-central-thin-seam-compression-round14.md",
            "rounds/polya-main/round_014/responses/seam-extension-incumbent.md",
            "rounds/polya-main/round_014/reviews/seam-extension-clean-room.md",
            "rounds/polya-main/round_014/reviews/seam-extension-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is proved for every ratio when K>=550^2. Complete exact compact coverage below that ceiling, then run fresh theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "The complete all-frequency small-hole endpoint is unchanged."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The complete all-frequency thin endpoint remains exactly 99/100<=rho<1; Round 14 is high-frequency only."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "Its fixed-rho theorem and formula K_0(rho) are unchanged; Round 14 only supplies a new exact evaluation at rho=7/8."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "The protected single-box certificate and its provenance are unchanged."
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
        "reason": "The theorem remains open below K=550^2 and still requires final theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 14 moves the central--thin seam from rho=9/10 to rho=7/8 and lowers the complete all-ratio high-frequency ceiling from 900^2 to 550^2 by the exact factor 324/121>2, but supplies no new certified residual coverage and does not enlarge the all-frequency endpoint."
  }
}

## State boundary after Round 14

The strict shell Pólya inequality is proved for every frequency in

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1,
$$

and for every ratio whenever $K\ge550^2$. The full all-frequency theorem
remains open on the true compact residual below that ceiling. Any further
seam extension requires a separately frozen full-domain proof; no Round 14
estimate may be extrapolated.
