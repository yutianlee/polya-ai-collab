# Round 11 Judge

Date: 2026-07-13

## Decision

Promote the ultra-thin complementary-action bridge

$$
\boxed{
0<\varepsilon\le\frac1{100},
\qquad
a=\varepsilon K\ge\frac1{8\varepsilon^{3/2}}.
}
$$

It proves the strict shell estimate

$$
N_D(A_{1-\varepsilon,1},K^2)
<\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

throughout that closed parameter domain.  The accepted product and aggregate
ranges cover the complementary closed range.  Therefore

$$
\boxed{
0<\varepsilon\le\frac1{100},
\qquad K\ge0,
}
$$

or equivalently

$$
\boxed{\frac{99}{100}\le\rho<1},
$$

is now a complete all-frequency endpoint.

## Two independent radial proofs

The incumbent writes $F=R^2$ for the squared inverse exact action and
$g=-F'$.  The mixed curvature makes $g$ decrease up to the ungridded inner
interface and increase after it.  A shifted radial sawtooth and
Riemann--Stieltjes integration give

$$
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a.
$$

After the exact half-integer angular ceiling, the remaining normalized
reserve is

$$
\boxed{\frac{61}{1400}>0}.
$$

The isolated clean-room reviewer did not inspect the incumbent and found a
different proof.  If $W$ is the primitive of the uncentered shifted radial
sawtooth, then $W\ge0$ and

$$
-\frac1{32}
\le W(t)-\frac t4
\le\frac3{32}.
$$

Splitting only at the actual real interface yields the stronger direct
reserve

$$
D\ge
\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
$$

After its independent angular estimate, the exact normalized margin is

$$
\boxed{
\frac{4119252993}{17500000000}>0.
}
$$

Both proofs include $\varepsilon=1/100$, the joining face
$a=1/(8\varepsilon^{3/2})$, radial walls, half-integer angular walls, proxy
integer walls, the ungridded curvature interface, and strict spectral walls.

## Complete endpoint and global ceiling

The old endpoint was $\varepsilon\le1/15625$.  The new endpoint expands its
width in $\varepsilon$ by the exact factor

$$
\frac{1/100}{1/15625}=\frac{625}{4}.
$$

The newly discharged radius strip has width

$$
\left(1-\frac1{15625}\right)-\frac{99}{100}
=\frac{621}{62500}.
$$

Using the Round 10 central--thin seam gives the following closed union:

1. Every possible residual on $[\rho_*,1/16]$ has $K<64$.
2. Every possible residual on $[1/16,24/25]$ has
   $K<K_0(24/25)<6000^2$.
3. Every possible residual on $[24/25,99/100]$ has
   $K<20/(1-\rho)^2\le200000$.
4. Every frequency on $[99/100,1)$ is now proved.

All shared faces are closed.  Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge6000^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The reduction from the Round 10 ceiling is more than a factor $105$, and the
reduction from the former $2^{35}$ ceiling is more than a factor $954$:

$$
\frac{125^5/8}{6000^2}
=\frac{1953125}{18432}>105,
\qquad
\frac{2^{35}}{6000^2}
=\frac{134217728}{140625}>954.
$$

## Review gates

- Frozen dependency packet: PASS.
- Incumbent direct inverse-action proof: PASS.
- Isolated clean-room reconstruction with a distinct radial reserve: PASS.
- Adversarial curvature, Stieltjes, constants, dependency, walls, and faces
  audit: PASS.
- Exact rational ledger for both proof paths and the global ceiling: PASS.
- Focused Round 11 tests: 4 passed.
- Complete computation suite: 36 passed.
- Round 8 independent certificate checker and provenance hashes: PASS.

No Bessel-root region was added.  The Round 11 ledger is exact symbolic
analytic evidence, not interval spectral certification.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-ultrathin-intermediate-bridge",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Ultra-thin complementary-action bridge above the aggregate face",
        "status": "proved_internal",
        "statement_tex": "Let rho=1-epsilon with 0<epsilon<=1/100 and a=epsilon K. If a>=1/(8 epsilon^(3/2)), then N_D(A_{rho,1},K^2)<(2/(9 pi))(1-rho^3)K^3, including threshold equality.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-thin-action-aggregate"
        ],
        "implies": [
          "SHELL-thin-curvature-intermediate",
          "SHELL-rho-one-endpoint",
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md",
            "computations/round11_verify_ultrathin_bridge.py",
            "computations/tests/test_round11_ultrathin_bridge.py"
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
          "SHELL-thin-action-aggregate"
        ],
        "falsification_cases": [
          "epsilon=1/100",
          "a=1/(8 epsilon^(3/2))",
          "tau not lying on any radial or integer grid",
          "radial wall x_n=T",
          "angular wall R(x_n)/epsilon in Z+1/2",
          "proxy wall A(y_l)+1/4 in Z",
          "improper trace g(0+)",
          "terminal trace g(T)=2 pi rho a",
          "curvature switch at t=tau",
          "strict spectral walls",
          "any use of the false global comparison A<=B",
          "any use of the Round 9 local-plateau conclusion"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
        ],
        "reason_for_promotion": "The direct inverse-square proof and a distinct clean-room sawtooth-primitive proof both close the complementary range. The U-shaped derivative magnitude, ungridded curvature interface, improper outer trace, terminal trace, half-integer angular ceilings, strict radial and proxy walls, exact reserves 61/1400 and 4119252993/17500000000, and dependency boundary passed adversarial review and executable-ledger reproduction.",
        "next_action": "Use this theorem as the complementary closed range above a=1/(8 epsilon^(3/2)). Do not extrapolate it beyond epsilon=1/100 without a new proof of the claimed larger-domain union."
      }
    ],
    "update": [
      {
        "id": "SHELL-thin-action-aggregate",
        "implies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "next_action": "Use its exact action calculus and accepted closed range through a=1/(8 epsilon^(3/2)); the complementary range is discharged by SHELL-ultrathin-intermediate-bridge."
      },
      {
        "id": "SHELL-thin-local-plateau-optimized",
        "implies_removed": [
          "SHELL-thin-curvature-intermediate",
          "SHELL-rho-one-endpoint",
          "SHELL-rho-compact-analytic-envelope"
        ],
        "next_action": "Retain this as a valid standalone high-frequency theorem and historical independent cross-check. It is no longer needed for endpoint closure or the current compact envelope."
      },
      {
        "id": "SHELL-thin-curvature-intermediate",
        "status": "proved_internal",
        "statement_tex": "For rho=1-epsilon with 0<epsilon<=1/100, the strict shell Polya estimate holds for every K>=0. With a=epsilon K, the proved product and aggregate ranges cover 0<=a<=1/(8 epsilon^(3/2)), while SHELL-ultrathin-intermediate-bridge covers a>=1/(8 epsilon^(3/2)); both include the common face.",
        "dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "permitted_dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "permitted_dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md",
            "computations/round11_verify_ultrathin_bridge.py",
            "computations/tests/test_round11_ultrathin_bridge.py"
          ]
        },
        "falsification_cases": [
          "epsilon=1/100",
          "a=pi/(4 epsilon)",
          "a=1/(8 epsilon^(3/2))",
          "closed ownership of the aggregate-to-bridge face",
          "radial, angular, proxy, and strict spectral walls",
          "using the Round 9 local-plateau theorem as an endpoint dependency"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
        ],
        "reason_for_promotion": "The accepted low union and independently audited complementary-action bridge meet on the same inclusive optical face and cover every K for every 0<epsilon<=1/100.",
        "next_action": "Treat the all-frequency epsilon<=1/100 theorem as discharged. Any larger epsilon domain requires a separately audited extension of every range needed for the claimed union."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "status": "proved_internal",
        "statement_tex": "For every 99/100<=rho<1 and every K>=0, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. The lower rho endpoint is included and rho=1 is excluded as the degenerate zero-width limit.",
        "dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "permitted_dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "permitted_dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
          ]
        },
        "falsification_cases": [
          "rho=99/100",
          "rho tending to 1",
          "a=1/(8 epsilon^(3/2))",
          "product-to-aggregate and aggregate-to-bridge faces",
          "radial, angular, proxy, and strict spectral walls"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
        ],
        "reason_for_promotion": "The accepted product and aggregate ranges and audited complementary-action theorem cover every optical frequency for 0<epsilon<=1/100, including the exact lower ratio face rho=99/100.",
        "next_action": "Treat 99/100<=rho<1 as completely discharged and preserve its inclusive lower face in every compact residual definition."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "next_action": "Use this theorem on 24/25<=rho<=99/100. The right face is now owned by the complete all-frequency thin endpoint; the Round 9 ultra-thin theorem remains valid but is no longer needed by the active envelope."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_11=[rho_*,99/100]. On [rho_*,1/16], every possible residual has K<64. On [1/16,24/25], every possible residual has K<K_0(24/25)<6000^2. On [24/25,99/100], every possible residual has K<20/(1-rho)^2<=200000. Consequently the strict shell Polya inequality holds for rho in I_11 and K>=6000^2; with the two endpoint lemmas it holds for every 0<rho<1 and K>=6000^2.",
        "dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "permitted_dependencies_removed": [
          "SHELL-thin-local-plateau-optimized"
        ],
        "permitted_dependencies_added": [
          "SHELL-ultrathin-intermediate-bridge"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md",
            "computations/round11_verify_ultrathin_bridge.py",
            "computations/tests/test_round11_ultrathin_bridge.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=24/25",
          "rho=99/100",
          "K equal to every component threshold",
          "K=K_0(24/25) and K=6000^2",
          "K=20/(1-rho)^2 on the central-thin seam",
          "the all-frequency endpoint beginning at rho=99/100",
          "exact comparisons 200000<6000^2<125^5/8<2^32",
          "closed planning envelope confused with the true certification target"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
        ],
        "reason_for_promotion": "The complete thin endpoint now begins at rho=99/100, eliminating the former ultra-thin residual. The Round 10 seam is below 200000 and the fixed-ratio central endpoint is below 6000^2, so the latter is the new complete all-ratio ceiling.",
        "next_action": "Use I_11 and K<6000^2 as the exact compact residual boundary. The next analytic target is the central endpoint controlling K_0(24/25)."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes the true residual on I_11 below K=6000^2. Concentrate next on the central fixed-ratio endpoint rather than the discharged ultra-thin strip."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Redefine any future E-minus-A manifest on I_11 with K<6000^2; the Round 11 rational ledger is analytic symbolic evidence, not a Bessel-root certificate."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
          ]
        },
        "next_action": "Both endpoint neighborhoods and the all-ratio range K>=6000^2 are proved. Keep this obligation open until the compact residual below that ceiling is exactly closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-ultrathin-intermediate-bridge.md",
            "rounds/polya-main/round_011/responses/ultrathin-bridge-incumbent.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-clean-room.md",
            "rounds/polya-main/round_011/reviews/ultrathin-bridge-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is now proved for every ratio when K>=6000^2. Complete exact compact coverage below that ceiling, then run final theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-thin-action-aggregate",
        "reason": "Its proved statement is unchanged; Round 11 uses its exact calculus and endpoint as input."
      },
      {
        "id": "SHELL-thin-local-plateau-optimized",
        "reason": "The theorem remains valid and proved_internal, but is no longer an active endpoint or envelope dependency."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "The residual ceiling is drastically lower, but the residual below it is not closed."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No new Bessel-root region was certified."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "All-ratio high energy and both endpoints are proved, but compact all-frequency closure remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The theorem remains open below K=6000^2 and still requires theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "Round 11 replaces the narrow epsilon<=1/15625 endpoint by the complete epsilon<=1/100 endpoint and lowers the all-ratio high-frequency ceiling from 125^5/8 to 6000^2 by a factor greater than 105. The score remains below complete because no compact residual region was newly certified and the final theorem remains open."
  }
}

## State boundary after Round 11

The strict shell Pólya inequality is now proved for every frequency in

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1,
$$

and for every ratio whenever $K\ge6000^2$.  The full all-frequency theorem
remains open on the compact residual below that ceiling.  Round 12 should
target the central fixed-ratio boundary and may use a bounded, face-connected
certificate pilot only as secondary evidence.
