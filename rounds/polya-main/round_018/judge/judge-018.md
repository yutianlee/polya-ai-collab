# Round 18 Judge

Date: 2026-07-14

## Decision

**PASS. First unsupported implication: none.**

Promote the independently reconstructed angular staircase

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_5(\rho)
}
$$

where

$$
\rho_c=\frac1{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
$$

On this complete closed band,

$$
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The genuinely new part is

$$
\mathcal C_{18}
=\left\{\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)\right\}.
$$

It is an exact subset of the frozen residual $\mathcal D_{17}$. The full
shell theorem is not proved.

Baseline graph: `state/proof_obligations.yml`, SHA-256
`3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c`.

All mandatory gates passed: the residual and proof-free candidate were
frozen first; A2 gave a complete incumbent proof; A3 independently
reconstructed it in strict isolation; A4 reproduced the finite constants;
the source audit checked the exact external statements and their scope; and
a fresh referee reconstructed the proof adversarially and found no
unsupported implication.

## Fixed evidence hashes

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `rounds/polya-main/round_018/exploration/residual-mask-freeze.md` | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| `computations/round18_residual_mask.py` | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| `computations/tests/test_round18_residual_mask.py` | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| `state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md` | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| `rounds/polya-main/round_018/exploration/candidate-claim-freeze.md` | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `rounds/polya-main/round_018/reviews/lorch-source-audit.md` | `0b49af55a253d7ed7646d2c7b70b2225899c2159d5baa10bb719b3cd3ee785e4` |
| `rounds/polya-main/round_018/responses/angular-staircase-incumbent.md` | `bbb1be54d3b0861442ca56b87022ef6c616fae45359914141128d871f1c42032` |
| `rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md` | `d94ca00eb41e4d1b33635cb8ef6a569bcfa0a70ed81549e8b4e9907483016660` |
| `computations/round18_verify_angular_staircase.py` | `c3d480cb85f65c9038a61aebfe411e18622b4224d7770e1c074f110330e5ea8f` |
| `computations/tests/test_round18_verify_angular_staircase.py` | `2a267c01568bbf069dc93efcc2119a75d454e33dc28b59315faf63ac58a41b50` |
| `rounds/polya-main/round_018/reviews/angular-staircase-constants.md` | `0d6c38c0790fb492d177ea50546d5bcb5fe7aa0017b5544c9a55c89ab54110e5` |
| `rounds/polya-main/round_018/reviews/angular-staircase-cross-comparison.md` | `f324da8eef7b9754e4478bdd2bc3f8813b0547688d9ab3dff15600b1a7410bd5` |
| `rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md` | `dfec69ccaf048443afdfa5c4a02d55036ae54f92c0a43d5dd57f34e0608a2b48` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |

## Proof basis and source boundary

The separated radial form and min--max principle give

$$
\lambda_{\ell,n}^{\rm sh}
\geq n^2z_\rho^2+\ell(\ell+1).
$$

Zero extension from $H_0^1(\rho,1)$ to $H_0^1(0,1)$ preserves the norm,
form, and fixed angular subspace. Min--max in that same channel therefore
gives

$$
\lambda_{\ell,1}^{\rm sh}(\rho)
\geq j_{\ell+1/2,1}^2.
$$

This comparison is internal; it is not attributed to Lorch. The audited
external statements give only

$$
j_{5/2,1}>\frac{51}{10},\qquad
j_{7/2,1}>\frac{13}{2},\qquad
j_{9/2,1}>\frac{15}{2}.
$$

The SIAM abstract states the two strict inequalities used, the meaning of
$j_{\nu,1}$, and the scope $\nu>-1$. DLMF supplies the spherical-Bessel
identity. The full Lorch paper was access-controlled, so the new source
obligation is a qualified statement-level external dependency, not an
independent reconstruction of Lorch's proof.

Because $z_\rho>7/2$ on the claimed ratio interval, every $n\geq2$ mode
and every $\ell\geq5$ first mode is excluded through $K=k_5$. The possible
strict-count caps are consequently $4,9,16,25$. The delayed entries at
$51/10$, $13/2$, and $15/2$ bridge the failed crude cap-$9$ continuation.
At the ratio splits $3/10,1/2,1/2$, the exact Weyl reserves are

$$
\frac{100387329}{11000000}>9,\qquad
\frac{107653}{6336}>16,\qquad
\frac{18375}{704}>25.
$$

The moving-wall payments are strictly increasing, and every spectral
equality is assigned using the strict counting convention. The exact upper
floor audit gives $k_5<26<64<K_0$ on the active $K_0$ branch and
$k_5<26<1944\leq54/(1-\rho)^2$ on the seam branch. Thus $k_5<U$ on the
whole new ratio interval.

## Exact post-promotion bookkeeping

The promoted analytic cover is

$$
\mathcal A_{18}
=\mathcal A_{17}\cup
\left\{\rho_c\leq\rho\leq\frac78,
\ z_\rho\leq K\leq k_5(\rho)\right\}.
$$

Exact subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\leq\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}}
$$

Every displayed frequency inequality is strict. The faces $K=k_2$ and
$\rho=7/8$ retain their old owners; $K=k_5$ is newly covered. The certified
boxes $B_0$ and $B_1$ remain valid but were already absorbed by
$\mathcal C_{17}$ and are not subtracted again. In particular,
$\mathcal D_{18}$ is nonempty: at $\rho=1/2$, the audited bounds
$k_5<26<30<64<K_0=U$ put $(1/2,30)$ in its second component. Therefore
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and the
program target remain open, and `COMP-certified-bessel` remains
`diagnostic_only`.

At $\rho=\rho_c$,

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
$$

The exact $\ell=0,n=2$ mode enters immediately above $2z_{\rho_c}$, so the
one-radial-mode cap cannot simply be carried to $k_6$. This is the next
method boundary, not a counterexample. The next round should freeze
$\mathcal D_{18}$ and build a radial-entry/angular staircase while treating
the unchanged $\rho<\rho_c$ component separately.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SRC-LORCH",
        "type": "source_audit",
        "track": "source_audit",
        "title": "Source audit: Lorch lower bounds for first positive Bessel zeros",
        "status": "proved_external_dependency",
        "statement_tex": "For nu>-1, Lorch's published abstract gives the two strict lower bounds for j_(nu,1)^2 recorded in sources/lorch_bessel_zeros.md. At nu=5/2, 7/2, and 9/2 they imply j_(5/2,1)>51/10, j_(7/2,1)>13/2, and j_(9/2,1)>15/2. DLMF 10.47.3 identifies these positive ordinary-Bessel zeros with the corresponding spherical-Bessel zeros. No shell-to-ball comparison or shell cross-product assertion is imported.",
        "dependencies": [],
        "implies": [
          "SHELL-next-angular-staircase"
        ],
        "blockers": [],
        "source_card": "sources/lorch_bessel_zeros.md",
        "evidence": {
          "positive": [
            "sources/lorch_bessel_zeros.md",
            "rounds/polya-main/round_018/reviews/lorch-source-audit.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "criticality": "standard",
        "artifact_hashes": {
          "source_card": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
          "source_audit": "0b49af55a253d7ed7646d2c7b70b2225899c2159d5baa10bb719b3cd3ee785e4"
        },
        "reason_for_promotion": "The primary SIAM abstract states the exact strict inequalities, positive-zero convention, and scope used, while DLMF supplies the spherical-Bessel identity. Exact algebra verifies all three rational consequences. The access limitation is recorded, and the source boundary explicitly excludes every shell-specific variational, counting, and Weyl step.",
        "next_action": "Use this obligation only for the three stated first-positive-zero lower bounds and the spherical-Bessel identification. Prove every fixed-channel shell comparison internally and do not attribute shell cross-product zeros, radial exclusions, multiplicities, or Weyl payments to Lorch."
      },
      {
        "id": "SHELL-next-angular-staircase",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Next angular staircase through the first radial barrier",
        "status": "proved_internal",
        "statement_tex": "Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), and k_m(rho)=sqrt(z_rho^2+m(m+1)). For every rho_c<=rho<=7/8 and z_rho<=K<=k_5(rho), the strict shell count satisfies N_D(A_(rho,1),K^2)<(2/(9 pi))(1-rho^3)K^3. Its genuinely new part C_18={rho_c<=rho<7/8, k_2(rho)<K<=k_5(rho)} is contained in D_17 and removes exactly that interval from the second residual component. The face K=k_5 is included; no statement is made for K>k_5.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-first-angular-bands",
          "SRC-LORCH",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round18.md",
            "rounds/polya-main/round_018/exploration/residual-mask-freeze.md",
            "computations/round18_residual_mask.py",
            "computations/tests/test_round18_residual_mask.py",
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/exploration/candidate-claim-freeze.md",
            "sources/lorch_bessel_zeros.md",
            "rounds/polya-main/round_018/reviews/lorch-source-audit.md",
            "rounds/polya-main/round_018/responses/angular-staircase-incumbent.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md",
            "computations/round18_verify_angular_staircase.py",
            "computations/tests/test_round18_verify_angular_staircase.py",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-cross-comparison.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
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
          "SHELL-sturm-liouville-completeness",
          "SHELL-first-angular-bands",
          "SRC-LORCH",
          "SRC-FLPS-balls"
        ],
        "falsification_cases": [
          "rho=rho_c, 3/10, 1/2, 5/6, and 7/8, including both one-sided traces at every interior split",
          "K=z_rho, k_2(rho), k_3(rho), k_4(rho), and k_5(rho), with strict spectral endpoint exclusion",
          "K=51/10, 13/2, and 15/2, including reversed, coincident, empty, and degenerate subbands",
          "radial indices n=1,2 and all n>=2; angular orders ell=0 through 5 and all ell>=5; full multiplicities and accidental cross-order coincidences",
          "the fixed-channel zero-extension form domain, Hardy finiteness, angular preservation, and min-max direction",
          "the Lorch scope nu>-1, first-positive-zero convention, strict square-root direction, and spherical-Bessel identification",
          "all moving-wall derivatives, pi bounds, split payments, denominators, radicals, squarings, and strict inequality directions",
          "k_5<U against the K_0 branch, inclusive seam branch, old global face, and rho=7/8 endpoint face",
          "C18 subset D17 and exact D18 subtraction, with K=k_2 old-owned and K=k_5 newly owned",
          "B0 and B1 retained as certified regression evidence but not subtracted again",
          "K=2z_rho and K=k_6(rho) treated as a radial-entry method boundary outside the claim, not a counterexample",
          "no executable ledger, sampled root, plot, source overreach, or agent agreement used as a replacement for the analytic proof"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "baseline_graph": "3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c",
          "residual_packet": "7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9",
          "residual_freeze": "7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff",
          "residual_classifier": "75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da",
          "residual_tests": "ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103",
          "frozen_claim": "354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9",
          "candidate_freeze": "b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c",
          "lorch_source_card": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
          "lorch_source_audit": "0b49af55a253d7ed7646d2c7b70b2225899c2159d5baa10bb719b3cd3ee785e4",
          "incumbent": "bbb1be54d3b0861442ca56b87022ef6c616fae45359914141128d871f1c42032",
          "clean_room": "d94ca00eb41e4d1b33635cb8ef6a569bcfa0a70ed81549e8b4e9907483016660",
          "constant_verifier": "c3d480cb85f65c9038a61aebfe411e18622b4224d7770e1c074f110330e5ea8f",
          "constant_tests": "2a267c01568bbf069dc93efcc2119a75d454e33dc28b59315faf63ac58a41b50",
          "constant_review": "0d6c38c0790fb492d177ea50546d5bcb5fe7aa0017b5544c9a55c89ab54110e5",
          "cross_comparison": "f324da8eef7b9754e4478bdd2bc3f8813b0547688d9ab3dff15600b1a7410bd5",
          "adversarial_referee": "dfec69ccaf048443afdfa5c4a02d55036ae54f92c0a43d5dd57f34e0608a2b48",
          "spectral_packet": "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
          "round17_claim": "c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77",
          "flps_source_card": "27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38"
        },
        "reason_for_promotion": "Every mandatory gate passed. A3 reconstructed the fixed-channel variational comparison, delayed Bessel entries, radial cutoff, multiplicity caps, Weyl payments, upper-floor containment, and exact subtraction without incumbent access. A4 independently verified 40 exact finite checks. The fresh referee reconstructed the complete implication and found no unsupported step. The external source boundary is explicit and the shell-specific comparison remains internal.",
        "next_action": "Use the lemma only through the closed K=k_5 face. Freeze D18 and develop a combined angular and radial-entry staircase above k_5, explicitly resolving the relative walls 2z_rho and k_6(rho), while separately attacking the unchanged rho_*<rho<rho_c component."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "implies_added": [
          "SHELL-next-angular-staircase"
        ]
      },
      {
        "id": "SHELL-sturm-liouville-completeness",
        "implies_added": [
          "SHELL-next-angular-staircase"
        ]
      },
      {
        "id": "SHELL-first-angular-bands",
        "status": "proved_internal",
        "implies_added": [
          "SHELL-next-angular-staircase"
        ],
        "next_action": "Retain the exact closed Round 17 band as the lower-band dependency of SHELL-next-angular-staircase. Its statement and proof are unchanged; further work begins strictly above k_5, not above k_2."
      },
      {
        "id": "SRC-FLPS-balls",
        "implies_added": [
          "SHELL-next-angular-staircase"
        ]
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Retain the complete Round 17 analytic cover A_17, both endpoint theorems, and the all-ratio theorem for K>=295^2. Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), k_5(rho)=sqrt(z_rho^2+30), and C_18={rho_c<=rho<7/8, k_2(rho)<K<=k_5(rho)}. The promoted closed staircase enlarges the cover to A_18=A_17 union {rho_c<=rho<=7/8, z_rho<=K<=k_5(rho)}. The exact residual is D_18={rho_*<rho<rho_c, 1/(2 rho)<K<U(rho)} union {rho_c<=rho<7/8, k_5(rho)<K<U(rho)}. B0 and B1 remain inside C17 and are not subtracted again. No claim that D18 is empty is made.",
        "dependencies_added": [
          "SHELL-next-angular-staircase"
        ],
        "permitted_dependencies_added": [
          "SHELL-next-angular-staircase"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round18.md",
            "rounds/polya-main/round_018/exploration/residual-mask-freeze.md",
            "computations/round18_residual_mask.py",
            "computations/tests/test_round18_residual_mask.py",
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/exploration/candidate-claim-freeze.md",
            "rounds/polya-main/round_018/responses/angular-staircase-incumbent.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-cross-comparison.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "the exact two-piece D18 rather than D17 or a rectangular proxy",
          "the shared rho=rho_c slice, old K=k_2 owner, and newly covered K=k_5 face",
          "k_5<U against every active upper-floor branch and the old global face",
          "B0 and B1 retained as analytically redundant certificates and not subtracted again",
          "nonemptiness of D18 not confused with theorem closure",
          "the 2z_rho and k_6 ordering recorded only as a method boundary outside C18"
        ],
        "reason_for_update": "The independently proved C18 band is added by exact set union and exact subtraction. All old endpoint, seam, high-frequency, and certificate owners remain unchanged.",
        "next_action": "Treat C18 as discharged. Close exactly D18: the unchanged rho_*<rho<rho_c component above 1/(2 rho), and the rho_c<=rho<7/8 component strictly above k_5 and below U."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/responses/angular-staircase-incumbent.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D18 remains nonempty, including the exact witness rho=1/2 and K=30",
          "the lower-ratio D18 component is unchanged and cannot inherit the rho>=rho_c staircase",
          "the second-radial entry at 2z_rho prevents an unaudited continuation to k_6"
        ],
        "next_action": "Keep this obligation open. Close the exact two-piece D18, preserving all strict faces; start a radial-entry staircase above k_5 and a separate proof on rho_*<rho<rho_c."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "C18 is a compact-band compression, not compact all-frequency closure",
          "D18 remains the exact blocker after both endpoint theorems"
        ],
        "next_action": "Both endpoint neighborhoods, all ratios at K>=295^2, C17, and C18 are proved. Keep this obligation open until the exact residual D18 is closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/responses/angular-staircase-incumbent.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D18 remains nonempty and prevents theorem promotion",
          "B0 and B1 provide no coverage outside the already promoted analytic region",
          "the final theorem still requires complete D18 closure and fresh theorem-level review"
        ],
        "next_action": "The strict shell inequality now includes both endpoints, the all-ratio high-frequency range, C17, and C18. Complete exact D18 coverage, then run fresh theorem-level clean-room and adversarial audits before changing this status."
      },
      {
        "id": "POLYA-program-target",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md",
            "rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "TARGET-shell-d3 remains open on the exact nonempty residual D18",
          "a compact-band lemma cannot promote the program theorem"
        ],
        "next_action": "Keep the program target open. First close D18, certify any genuinely uncovered finite remainder if required, and pass theorem-level clean-room and adversarial review for TARGET-shell-d3."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "computations/round18_verify_angular_staircase.py",
            "computations/tests/test_round18_verify_angular_staircase.py",
            "rounds/polya-main/round_018/reviews/angular-staircase-constants.md"
          ]
        },
        "falsification_cases_added": [
          "the Round 18 exact constant ledger is analytic support, not an interval-certified spectral computation",
          "B0 and B1 remain valid but analytically redundant inside C17",
          "no Round 18 certified subset is promoted"
        ],
        "next_action": "Keep the parent diagnostic_only. B0 and B1 remain regression certificates inside C17. Any later finite certificate must be a predeclared face-connected subset of the exact D18 and pass an independent checker."
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
        "reason": "The fixed-ratio high-frequency theorem and K_0 upper branch are unchanged."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "reason": "The accepted seam and its exact rho=5/6 and K=54/(1-rho)^2 faces are unchanged."
      },
      {
        "id": "SHELL-thin-width-phase-zero",
        "reason": "The zero-count theorem and inclusive K=z_rho face are unchanged."
      },
      {
        "id": "SHELL-first-angular-bands",
        "reason": "Its theorem statement and proved_internal status are unchanged; only reverse dependency metadata and its next action are refreshed."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "reason": "It remains proved_internal; A18 replaces A17 as the recorded cover and D18 replaces D17 as the exact residual."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "The B0 certificate remains certified, byte-unchanged, and analytically redundant inside C17."
      },
      {
        "id": "COMP-certified-bessel-pilot-round17",
        "reason": "The B1 certificate remains certified, byte-unchanged, and analytically redundant inside C17."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No Round 18 interval certificate was produced; the parent remains diagnostic_only."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "C18 shrinks the residual but does not close the exact nonempty D18."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The exact D18 still blocks ratio-uniform closure."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The full shell theorem remains open on D18 and still requires theorem-level final review after closure."
      },
      {
        "id": "POLYA-program-target",
        "reason": "The program target remains open because TARGET-shell-d3 remains open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "All promotion gates passed. Round 18 converts the cap-9 obstruction into a rigorous three-entry angular staircase, enlarges the closed analytic band from k_2 through k_5, audits the necessary external first-zero statements, and replaces D17 by the exact strict subset D18. The lower-ratio component and the region above k_5 remain nonempty, so no compact or theorem-level target is closed."
  }
}
```

## Application gate and status audit

Before applying this patch, every fixed hash above must still match, both
focused ledgers must remain PASS, and the complete test suite must pass. The
patch must be applied once through the validator with `--round-index 18`;
this judge does not apply it.

The dependency direction introduced here is

~~~text
SRC-LORCH + SRC-FLPS-balls + CONV-strict-counting
    + SHELL-sturm-liouville-completeness
    + SHELL-first-angular-bands
        -> SHELL-next-angular-staircase
        -> SHELL-rho-compact-analytic-envelope
        -> SHELL-rho-compact
        -> SHELL-rho-uniformity
        -> TARGET-shell-d3
~~~

The graph stays acyclic. `SHELL-next-angular-staircase` is the only new
internal lemma. `SRC-LORCH` is the only new external source obligation.
No target status is promoted, no certified computation is created, and the
two old certificates retain their existing status and scope.
