# Round 17 Judge

Date: 2026-07-14

## Decision

**PASS. First unsupported implication: none.**

Promote the independently reconstructed first-angular-band theorem

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
\frac{\pi}{1-\rho}\le K
\le\sqrt{\left(\frac{\pi}{1-\rho}\right)^2+6}
}
$$

with strict shell counting on every displayed frequency face. Also promote the
independently checked face-connected certificate on

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

The certificate remains local regression evidence: the exact analytic audit
proves $B_1\subset\mathcal C_{17}$, so it supplies no additional subtraction
after the analytic promotion. The full shell theorem is not proved.

Baseline graph: `state/proof_obligations.yml`, SHA-256
`dc2552091ff79f5ab39de896b4d97cf22ccc234f3842ee9734d54d123c5f2379`.

All three independent proof gates returned PASS:

1. isolated A3 clean-room reconstruction at
   `rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md`;
2. A4 exact-constant and set-membership audit at
   `rounds/polya-main/round_017/exploration/analytic-constant-audit.md`;
3. a fresh adversarial referee at
   `rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md`
   reporting no unsupported implication.

## Fixed evidence hashes

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round17.md` | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| `rounds/polya-main/round_017/exploration/residual-mask-freeze.md` | `23bfee8cddd64d0d9d956b8d1a288c6263095a2a04cc42052c4ace08ca36152a` |
| `computations/round17_residual_mask.py` | `b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b` |
| `computations/tests/test_round17_residual_mask.py` | `de43ee6b54d57b41db647f8b2c0cb2a79609069e59d0b2a50d335730a413dcc8` |
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `rounds/polya-main/round_017/exploration/analytic-candidate-freeze.md` | `ffb2f4b80ad701d7f67414f6683ae3c05d61841a2c14495c3e7b4254ad97a8eb` |
| `rounds/polya-main/round_017/responses/analytic-compression-incumbent.md` | `345e76cbc2f7868db0c78d803edb8c1c5eaabdc8a7189a3f8580d36b08514375` |
| `rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md` | `9e75cd74df11ad903b26e5f6ccc367ab86d5d2eec080e0ddda4a4817765e05b7` |
| `rounds/polya-main/round_017/exploration/analytic-constant-audit.md` | `7fb22f516db763cc4f8fce6abf7aaa7b804fc88cd544c44589e41e3b37798be0` |
| `computations/round17_verify_candidate_c17_constants.py` | `b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469` |
| `computations/tests/test_round17_candidate_c17_constants.py` | `533620b5fadd9b7b13ff1d21ca9282bfd3d1ed778e7ecda970a3fb027ce3955c` |
| `rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md` | `a13a05294af7957e817d3ca77440084c466c35334adaf5c1aa6cf610009c687b` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `rounds/polya-main/round_017/certification/pilot-extension-feasibility.md` | `f19e265ce4b01994ab204097132f1f51828e3018e4efaa288f8c0ed19da81e19` |
| `computations/round17_pilot_extension_certificate.py` | `38362dd192c7918a3895eb4b13a1afdd076eaae28a650eb8bed31d517314a2a7` |
| `computations/round17_verify_pilot_extension_certificate.py` | `40a814e2a3557363d1d958f10c38c295ac0af894e4e8b441ea7dbd0c968991df` |
| `computations/tests/test_round17_pilot_extension_certificate.py` | `71b79d96ff8b7f30cd9b74ed433c4e8b5182fc3e0270db0ad0a5d3f0d3b912a9` |
| `rounds/polya-main/round_017/certification/pilot-extension-upward.json` | `858c55e832b3ca92f3b077dd7ea55f7ef6c4f7456de786c7264f178fcdf77b5b` |
| `rounds/polya-main/round_017/certification/pilot-extension-upward-check.json` | `e3bddf0b1488812e7572c318888f7f4721148b78c5e9ff98f7dabe7b19351d3f` |
| `rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md` | `5234c6071941b7657a83925e41c35e49a8d18b9c08ac69872608a37f5ef220f7` |

## Exact post-promotion set bookkeeping

Let

$$
z_\rho=\frac{\pi}{1-\rho},\qquad
k_2(\rho)=\sqrt{z_\rho^2+6},\qquad
\rho_c=\frac1{1+2\pi}.
$$

The promoted analytic band is

$$
\overline{\mathcal C}_{17}
=\{(\rho,K):\rho_c\le\rho\le7/8,\ z_\rho\le K\le k_2(\rho)\},
$$

and its genuinely new part is

$$
\mathcal C_{17}
=\{(\rho,K):\rho_c\le\rho<7/8,\ z_\rho<K\le k_2(\rho)\}.
$$

The new analytic cover and exact surviving residual are

$$
\mathcal A_{17}=\mathcal A_{16}\cup\overline{\mathcal C}_{17},
\qquad
\boxed{\mathcal D_{17}=\mathcal D_{16}\setminus\mathcal C_{17}}.
$$

Equivalently, with the exact upper floor $U(\rho)$ from the frozen
Round 17 residual packet,

$$
\mathcal D_{17}
=\left\{\rho_*<\rho<\rho_c,\ \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\le\rho<\frac78,\ k_2(\rho)<K<U(\rho)\right\}.
$$

Neither formula says that $\mathcal D_{17}$ is empty. The audited set
relations are

$$
B_0\subset\mathcal C_{17},\qquad
B_1\subset\mathcal C_{17},
$$

where

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

Thus both certified boxes remain valid independent evidence but are
analytically redundant after C17 promotion, and the theorem-wise uncovered
set is exactly $\mathcal U_{17}=\mathcal D_{17}$.

## Proof and certification basis

The direct-sum Sturm--Liouville theorem and min--max principle give

$$
\lambda_{\ell,n}\ge n^2z_\rho^2+\ell(\ell+1),
\qquad
\lambda_{0,n}=n^2z_\rho^2.
$$

On $z_\rho\le K\le k_2(\rho)$ this excludes every $n\ge2$ and every
$\ell\ge2$. Strict counting at the two angular walls therefore gives the
complete caps $0$, $1$, and $4$, with multiplicities $1$ and $3$ for the
only possible channels. The Weyl payment is already greater than $1$ at the
lower wall. At the first angular wall it is increasing in $\rho$ and has the
exact lower bound

$$
W(\rho_c,k_1(\rho_c))
>4+\frac{49061}{269500}>4.
$$

The isolated proof reconstructed these facts without the incumbent or any
certificate. The exact ledger checked 28 finite identities, the fresh
referee reconstructed the spectral and set arguments, and both found no
unsupported implication. In particular, the complete $B_1$ upper face lies
strictly below $k_2$ with squared rational reserve

$$
\frac{668749071}{10020010000}>0.
$$

The Arb producer and independent exact-Fraction checker separately certify
the strict count $4$ and positive Weyl margin throughout $B_1$; the
persistent independent audit reproduces their hashes, outputs, and six
focused tests. The parent computation remains `diagnostic_only` because one
certified box is not residual closure.

Immediately above $k_2$, the same coarse multiplicity cap jumps from $4$ to
$9$, while its Weyl payment is below $9$ at $\rho_c$. This is an obstruction
to that coarse proof mechanism, not a counterexample. Round 18 must use a
sharper angular staircase or a genuinely new estimate on the exact
$\mathcal D_{17}$.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-first-angular-bands",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "First angular bands above the compact zero-count wall",
        "status": "proved_internal",
        "statement_tex": "Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), and k_2(rho)=sqrt(z_rho^2+6). For every rho_c<=rho<=7/8 and z_rho<=K<=k_2(rho), the strict shell count satisfies N_D(A_{rho,1},K^2)<(2/(9 pi))(1-rho^3)K^3. The lower frequency face and rho=7/8 are included; strict spectral counting is used at K=z_rho, sqrt(z_rho^2+2), and k_2(rho).",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/exploration/analytic-candidate-freeze.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "computations/round17_verify_candidate_c17_constants.py",
            "computations/tests/test_round17_candidate_c17_constants.py",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "criticality": "bottleneck",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "fresh-referee",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness"
        ],
        "falsification_cases": [
          "rho=rho_c and rho=7/8, with the old analytic face owner retained",
          "K=z_rho, K=sqrt(z_rho^2+2), and K=k_2(rho), with strict endpoint exclusion",
          "rho=1/2 and rho=5/6 from both adjacent mask formulas",
          "the first two radial indices and ell=0,1,2 with multiplicities 1,3,5",
          "every radial index n>=2 and angular order ell>=2 on the complete band",
          "accidental cross-order eigenvalue coincidence cannot exceed the direct-sum multiplicity cap",
          "monotonicity of the Weyl payment and its exact minimum at rho=rho_c",
          "all pi bounds, denominators, square roots, squarings, and strict inequality directions",
          "the closed faces of B0 and B1 when analytic containment is asserted",
          "the third-angular-band product-cap failure treated only as a method obstruction",
          "no Bessel-root certificate, phase enclosure, sampled plot, or desired conclusion used as an analytic input"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "frozen_claim": "c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77",
          "candidate_freeze": "ffb2f4b80ad701d7f67414f6683ae3c05d61841a2c14495c3e7b4254ad97a8eb",
          "incumbent": "345e76cbc2f7868db0c78d803edb8c1c5eaabdc8a7189a3f8580d36b08514375",
          "clean_room": "9e75cd74df11ad903b26e5f6ccc367ab86d5d2eec080e0ddda4a4817765e05b7",
          "constant_audit": "7fb22f516db763cc4f8fce6abf7aaa7b804fc88cd544c44589e41e3b37798be0",
          "constant_verifier": "b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469",
          "constant_tests": "533620b5fadd9b7b13ff1d21ca9282bfd3d1ed778e7ecda970a3fb027ce3955c",
          "adversarial_referee": "a13a05294af7957e817d3ca77440084c466c35334adaf5c1aa6cf610009c687b",
          "spectral_packet": "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8"
        },
        "reason_for_promotion": "All three PASS gates are satisfied: the isolated A3 proof reconstructs the complete band without incumbent or certificate access; A4 verifies the finite theorem constants, C17 subset D16, and B0 subset C17; and a fresh adversarial referee finds no unsupported implication and proves B1 subset C17. The proof uses only the strict convention, the separated Sturm-Liouville spectrum, min-max, and exact elementary inequalities.",
        "next_action": "Use the lemma only through its exact closed band. Attack D_17 above k_2(rho) or the unchanged rho<rho_c part; do not extend through the ell=2 wall using the failed coarse multiplicity payment."
      },
      {
        "id": "COMP-certified-bessel-pilot-round17",
        "type": "computation",
        "track": "certified_computation",
        "title": "Independently checked face-connected Round 17 shell certificate",
        "status": "certified",
        "statement_tex": "For every rho in [999/2000,1001/2000] and K in [168/25,673/100], the exact strict shell count is N_D(A_{rho,1},K^2)=4 and is strictly smaller than (2/(9 pi))(1-rho^3)K^3; the strict Weyl margin exceeds 39657181883797/2685546875000.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-cross-product-formula",
          "SHELL-sturm-liouville-completeness",
          "SHELL-angular-cutoff",
          "SHELL-thin-width-phase-zero",
          "SHELL-fixed-rho-high-energy",
          "COMP-certified-bessel-pilot-round8"
        ],
        "implies": [
          "COMP-certified-bessel"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
            "rounds/polya-main/round_017/certification/pilot-extension-upward.json",
            "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json",
            "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md",
            "computations/round17_pilot_extension_certificate.py",
            "computations/round17_verify_pilot_extension_certificate.py",
            "computations/tests/test_round17_pilot_extension_certificate.py"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "criticality": "standard",
        "lead_author": "A4",
        "adversarial_reviewer": "B1-independent-auditor",
        "review_independence": "independent",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-cross-product-formula",
          "SHELL-sturm-liouville-completeness",
          "SHELL-angular-cutoff",
          "SHELL-thin-width-phase-zero",
          "SHELL-fixed-rho-high-energy",
          "COMP-certified-bessel-pilot-round8"
        ],
        "falsification_cases": [
          "rho and K on every closed B1 face",
          "the complete shared face B0 intersect B1 at K=168/25",
          "strict membership of the complete B1 in D_16",
          "ell=0 and ell=1 root brackets and determinant signs on all parameter faces",
          "ell>=2 and second-radial-mode Sturm exclusions at the worst width and frequency",
          "strict count four with full multiplicities and no spectral wall in B1",
          "the true Weyl worst corner rho=1001/2000 and K=168/25",
          "tampered count, determinant sign, packet hash, or producer/checker provenance",
          "B1 subset C17 recorded only after the independent analytic set audit"
        ],
        "evidence_class": "interval_certified",
        "software_version": "python-flint 0.8.0 Arb producer; Python standard-library Fraction independent checker",
        "reproduction_command": "python computations/round17_pilot_extension_certificate.py --output rounds/polya-main/round_017/certification/pilot-extension-upward.json && python computations/round17_verify_pilot_extension_certificate.py --input rounds/polya-main/round_017/certification/pilot-extension-upward.json --report rounds/polya-main/round_017/certification/pilot-extension-upward-check.json && python -m pytest computations/tests/test_round17_pilot_extension_certificate.py -q",
        "coverage_statement": "Exactly the closed box B1=[999/2000,1001/2000] x [168/25,673/100], attached to the complete upper face of B0; no other residual point is certified. The exact Round 17 analytic audit gives B1 subset C17, so this certificate is retained as independent regression evidence but contributes no separate subtraction from D_17.",
        "artifact_hashes": {
          "producer": "38362dd192c7918a3895eb4b13a1afdd076eaae28a650eb8bed31d517314a2a7",
          "independent_checker": "40a814e2a3557363d1d958f10c38c295ac0af894e4e8b441ea7dbd0c968991df",
          "tests": "71b79d96ff8b7f30cd9b74ed433c4e8b5182fc3e0270db0ad0a5d3f0d3b912a9",
          "frozen_residual_packet": "eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e",
          "residual_freeze": "23bfee8cddd64d0d9d956b8d1a288c6263095a2a04cc42052c4ace08ca36152a",
          "parent_B0_certificate": "f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00",
          "parent_B0_check": "02b12e13ad329e77035d8438ec359b6be4dd35571c384543f3890d67c132e6cc",
          "certificate": "858c55e832b3ca92f3b077dd7ea55f7ef6c4f7456de786c7264f178fcdf77b5b",
          "checker_report": "e3bddf0b1488812e7572c318888f7f4721148b78c5e9ff98f7dabe7b19351d3f",
          "human_report": "f19e265ce4b01994ab204097132f1f51828e3018e4efaa288f8c0ed19da81e19",
          "independent_audit": "5234c6071941b7657a83925e41c35e49a8d18b9c08ac69872608a37f5ef220f7"
        },
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md"
        ],
        "certification_artifacts": [
          "rounds/polya-main/round_017/certification/pilot-extension-upward.json",
          "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json",
          "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
          "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md"
        ],
        "reason_for_promotion": "The single face-connected B1 certificate has outward Arb determinant signs, independently reconstructed exact-Fraction determinant bounds, exact Sturm exclusions, strict multiplicity counting, exact residual membership, a strict Weyl margin at the true worst corner, authenticated provenance, and an independent checker PASS. It remains a one-box result and is analytically redundant after C17 promotion.",
        "next_action": "Retain B1 as an independent regression certificate. Do not use it to enlarge the analytic mask or promote the parent computation; any later certificate must target an exact face-connected subset of D_17."
      }
    ],
    "update": [
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Retain the complete Round 16 analytic cover A_16, its exact residual D_16, the all-ratio theorem for K>=295^2=87025, and both endpoint theorems. Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), k_2(rho)=sqrt(z_rho^2+6), and C_17={rho_c<=rho<7/8, z_rho<K<=k_2(rho)}. The promoted closed first-angular-band lemma enlarges the analytic cover to A_17=A_16 union {rho_c<=rho<=7/8, z_rho<=K<=k_2(rho)}. The exact surviving analytic residual is D_17=D_16 setminus C_17, equivalently {rho_*<rho<rho_c, 1/(2 rho)<K<U(rho)} union {rho_c<=rho<7/8, k_2(rho)<K<U(rho)}, where U is the exact frozen Round 17 upper floor. Both B0 and B1 are contained in C_17, so the theorem-wise uncovered set is U_17=D_17. No claim that D_17 is empty is made.",
        "dependencies_added": [
          "SHELL-first-angular-bands"
        ],
        "permitted_dependencies_added": [
          "SHELL-first-angular-bands"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round17.md",
            "rounds/polya-main/round_017/exploration/residual-mask-freeze.md",
            "computations/round17_residual_mask.py",
            "computations/tests/test_round17_residual_mask.py",
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/exploration/analytic-candidate-freeze.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "computations/round17_verify_candidate_c17_constants.py",
            "computations/tests/test_round17_candidate_c17_constants.py",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "rho=rho_c with both old lower walls and the new k_2 lower residual wall",
          "K=z_rho, K=sqrt(z_rho^2+2), and K=k_2(rho) with exact face ownership",
          "rho=1/2, rho=5/6, and rho=7/8 from both adjacent formulas",
          "C17 subset D16 checked against every active H0, K0, seam, endpoint, and global face",
          "the exact subtraction D17=D16 setminus C17 rather than a rectangular replacement",
          "the first D17 piece uses rho_*<rho<rho_c and the second uses rho_c<=rho<7/8",
          "B0 subset C17 and B1 subset C17 on every closed box face",
          "B0 and B1 retained as certified evidence but not subtracted again from D17",
          "D17 or U17 incorrectly declared empty",
          "the ell=2 coarse-payment obstruction misreported as a target counterexample"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "residual_packet": "eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e",
          "residual_freeze": "23bfee8cddd64d0d9d956b8d1a288c6263095a2a04cc42052c4ace08ca36152a",
          "residual_classifier": "b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b",
          "residual_tests": "de43ee6b54d57b41db647f8b2c0cb2a79609069e59d0b2a50d335730a413dcc8",
          "frozen_claim": "c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77",
          "candidate_freeze": "ffb2f4b80ad701d7f67414f6683ae3c05d61841a2c14495c3e7b4254ad97a8eb",
          "incumbent": "345e76cbc2f7868db0c78d803edb8c1c5eaabdc8a7189a3f8580d36b08514375",
          "clean_room": "9e75cd74df11ad903b26e5f6ccc367ab86d5d2eec080e0ddda4a4817765e05b7",
          "constant_audit": "7fb22f516db763cc4f8fce6abf7aaa7b804fc88cd544c44589e41e3b37798be0",
          "constant_verifier": "b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469",
          "constant_tests": "533620b5fadd9b7b13ff1d21ca9282bfd3d1ed778e7ecda970a3fb027ce3955c",
          "adversarial_referee": "a13a05294af7957e817d3ca77440084c466c35334adaf5c1aa6cf610009c687b"
        },
        "reason_for_promotion": "Round 16's endpoint and high-frequency conclusions are unchanged. All Round 17 PASS gates are satisfied, so the independently proved C17 band is added with exact old-face ownership, exact containment in D16, and exact residual subtraction; no certified box or sampled point is used to prove the analytic band.",
        "next_action": "Treat C17 as discharged and work only on D_17=D_16 setminus C17. Preserve the two exact D17 pieces and their strict walls; do not claim compact closure or replace D17 by a rectangle."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "status": "certified",
        "coverage_statement": "Exactly the closed box B0=[999/2000,1001/2000] x [67/10,168/25]; no other compact residual point is claimed. The exact promoted Round 17 analytic set proof gives B0 subset C17, so B0 remains independently certified regression evidence but contributes no separate subtraction from D17.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "every closed B0 face in the exact proof B0 subset C17",
          "the original B0 certificate retained without changing its bytes, count, or evidence class",
          "B0 incorrectly subtracted from D17 after analytic subsumption"
        ],
        "next_action": "Retain B0 unchanged as an independent certified regression artifact. It is analytically redundant after C17 promotion and must not be counted as an additional reduction of D17."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "dependencies_added": [
          "COMP-certified-bessel-pilot-round17"
        ],
        "evidence_added": {
          "positive": [
            "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
            "rounds/polya-main/round_017/certification/pilot-extension-upward.json",
            "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json",
            "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md",
            "computations/round17_pilot_extension_certificate.py",
            "computations/round17_verify_pilot_extension_certificate.py",
            "computations/tests/test_round17_pilot_extension_certificate.py"
          ]
        },
        "certification_artifacts_added": [
          "rounds/polya-main/round_017/certification/pilot-extension-upward.json",
          "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json",
          "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
          "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md"
        ],
        "falsification_cases_added": [
          "B1 is one exact face-connected box, not a sweep or residual component",
          "B1 subset C17 makes it analytically redundant after promotion",
          "a certified child does not promote the diagnostic_only parent",
          "any future certificate must lie in the exact surviving D17 rather than D16 or a coarse rectangle"
        ],
        "next_action": "Keep the parent diagnostic_only. B0 and B1 are valid local certificates but are analytically redundant after C17 promotion. Any new finite certificate must be an exact face-connected subset of D17 and must pass an independent checker before graph use."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round17.md",
            "rounds/polya-main/round_017/exploration/residual-mask-freeze.md",
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md",
            "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
            "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json",
            "rounds/polya-main/round_017/reviews/pilot-extension-independent-audit.md"
          ]
        },
        "falsification_cases_added": [
          "the exact two-piece D17 rather than D16 or a rectangular proxy",
          "the shared rho=rho_c face and inclusive K=k_2(rho) analytic owner",
          "B0 and B1 analytically subsumed but independently certified",
          "nonemptiness of the surviving residual not confused with theorem closure"
        ],
        "next_action": "Keep this obligation open. Close exactly D17=D16 setminus C17: the unchanged strip rho_*<rho<rho_c above 1/(2 rho), and the strip rho_c<=rho<7/8 above k_2(rho), both below the frozen upper floor U(rho)."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "C17 is a strict compact-band compression, not compact all-frequency closure",
          "D17 remains the exact blocker after both endpoint theorems"
        ],
        "next_action": "Both endpoint neighborhoods and all ratios at K>=295^2 remain proved, and C17 is analytically discharged. Keep this obligation open until the exact surviving compact residual D17 is closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-first-angular-bands-round17-claim.md",
            "rounds/polya-main/round_017/responses/analytic-compression-incumbent.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md",
            "rounds/polya-main/round_017/exploration/analytic-constant-audit.md",
            "rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md",
            "rounds/polya-main/round_017/certification/pilot-extension-feasibility.md",
            "rounds/polya-main/round_017/certification/pilot-extension-upward-check.json"
          ]
        },
        "falsification_cases_added": [
          "D17 remains nonempty and prevents theorem promotion",
          "B0 and B1 provide no extra coverage outside promoted C17",
          "the final theorem still requires complete D17 closure and fresh theorem-level review"
        ],
        "next_action": "The strict shell inequality retains both endpoint theorems, the all-ratio K>=295^2 range, and the promoted C17 band. Complete exact coverage of D17, then run fresh theorem-level clean-room and adversarial audits before changing this status."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "The complete small-hole endpoint and its inclusive rho_* face are unchanged."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The complete all-frequency endpoint 7/8<=rho<1 and its inclusive lower face are unchanged."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "The fixed-rho theorem and K_0(rho) upper branch are unchanged."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "reason": "The accepted seam and its exact rho=5/6 and K=54/(1-rho)^2 faces are unchanged."
      },
      {
        "id": "SHELL-thin-width-phase-zero",
        "reason": "The zero-count theorem and its inclusive wall K=pi/(1-rho) are unchanged."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "reason": "It remains proved_internal; Round 17 enlarges its analytic cover and replaces D16 by the exact smaller residual D17 without claiming closure."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "Its certificate remains certified and byte-unchanged; only its analytic redundancy B0 subset C17 is recorded."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "One additional certified child does not promote the diagnostic_only parent."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "C17 shrinks the residual to D17 but does not close it."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The surviving compact residual D17 still blocks ratio-uniform closure."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The full theorem remains open on D17 and still requires theorem-level final review after closure."
      },
      {
        "id": "POLYA-program-target",
        "reason": "The program target remains open because TARGET-shell-d3 remains open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "All proof-audit gates passed. Round 17 freezes the exact D16 mask, proves one nontrivial first-angular-band analytic compression C17, replaces the residual by the exact strict subset D17, and certifies one face-connected box B1. B0 and B1 are both analytically subsumed, while D17 remains nonempty and the full shell theorem remains open."
  }
}
```

## Application gate

All of the following are required before the one-time State Patch application:

1. each fixed hash above still matches current bytes;
2. A3 says PASS on the frozen claim before incumbent access;
3. A4 verifies the exact C17 theorem constants, `C17 subset D16`, and
   `B0 subset C17`;
4. the fresh referee says PASS, identifies no unsupported implication, and
   proves `B1 subset C17` on every closed box face;
5. the B1 independent checker remains `PASS` and all provenance hashes match;
6. the full computation suite passes;
7. this final judge patch validates against the untouched baseline graph.

Apply only through the normal validator with `--round-index 17` and a
`judge-017.md` reference. The patch engine must set
`last_updated_round=17` and the final `last_updated_at` timestamp on every
created or updated object. This prevents a placeholder timestamp from
entering the graph.

## Dependency and status audit

Dependency direction after the patch is:

~~~text
CONV-strict-counting + SHELL-sturm-liouville-completeness
    -> SHELL-first-angular-bands
    -> SHELL-rho-compact-analytic-envelope
    -> SHELL-rho-compact
    -> SHELL-rho-uniformity
    -> TARGET-shell-d3

foundational spectral lemmas + COMP-certified-bessel-pilot-round8
    -> COMP-certified-bessel-pilot-round17
    -> COMP-certified-bessel
~~~

Here arrows point from prerequisites to consumers. The `implies` fields are
the reverse metadata corresponding to `dependencies`; they are not extra
dependency edges. No new dependency points from a foundational lemma back
to an envelope, target, or computation consumer.

The intended status result is exactly:

- new `SHELL-first-angular-bands`: `proved_internal`;
- new `COMP-certified-bessel-pilot-round17`: `certified`;
- `SHELL-rho-compact-analytic-envelope`: remains `proved_internal`;
- `COMP-certified-bessel-pilot-round8`: remains `certified`;
- `COMP-certified-bessel`: remains `diagnostic_only`;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target`: remain `open`;
- both endpoint theorems remain `proved_internal` with unchanged statements.

The graph must therefore remain acyclic on `dependencies`, and no theorem
status is promoted merely because B1 is certified.
