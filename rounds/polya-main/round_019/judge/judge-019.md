# Round 19 Judge

Date: 2026-07-14

## Decision

**PASS. First unsupported implication: none.**

Promote the independently reconstructed two-sided staircase. Put

$$
\rho_c=\frac1{1+2\pi},\qquad
\rho_0=\frac1{\sqrt{337}},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},\qquad
d=\frac{\sqrt{337}}2,
$$

and

$$
\mathcal W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

Then both of the following analytic conclusions hold:

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\quad z_\rho\leq K\leq k_6(\rho)
}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K)},
$$

and

$$
\boxed{
\rho_0<\rho<\rho_c,
\quad L(\rho)<K\leq d
}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K)}.
$$

Relative to the accepted Round 18 cover, the genuinely new set is

$$
\boxed{
\begin{aligned}
\mathcal C_{19}={}&
\left\{\rho_0<\rho<\rho_c,
\ L(\rho)<K\leq d\right\}\\
&\cup
\left\{\rho_c\leq\rho<\frac78,
\ k_5(\rho)<K\leq k_6(\rho)\right\}.
\end{aligned}}
$$

This is an exact subset of the frozen residual $\mathcal D_{18}$. The full
shell Pólya theorem is **not proved**: the exact post-promotion residual
$\mathcal D_{19}$ displayed below is nonempty.

Baseline graph: `state/proof_obligations.yml`, SHA-256
`24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e`.

All mandatory gates passed. The Round 18 residual and the proof-free Round
19 candidate were frozen before review; the two analytic workstreams supplied
complete incumbents; A3 reconstructed both bands in strict isolation; A4
reproduced every finite constant and face with exact arithmetic; the new-zero
audit separated external provenance from internal zero arguments; the
cross-comparison found no mathematical discrepancy; and a fresh referee
assumed the candidate false, reconstructed every dependency and face, and
found no unsupported implication.

## Fixed evidence hashes

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `rounds/polya-main/round_019/exploration/residual-mask-freeze.md` | `0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9` |
| `computations/round19_residual_mask.py` | `bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6` |
| `computations/tests/test_round19_residual_mask.py` | `41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787` |
| `rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md` | `9e7dedaab08425166998a5c766bdb32d3787d9f35b6c4bf4b7d6be07009c9b43` |
| `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |
| `rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md` | `ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718` |
| `rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md` | `b9a86f1411a8e63c30b6ae5e2b3a65e167426f0b72a4447d15d4e833c5df6983` |
| `rounds/polya-main/round_019/exploration/lower-ratio-route.md` | `1a4cd1eb93c286816346ead50edef0f151f8b1a287186ba3b20e37336c16b681` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md` | `24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17` |
| `computations/round19_verify_two_sided_staircase.py` | `4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23` |
| `computations/tests/test_round19_verify_two_sided_staircase.py` | `1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md` | `fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md` | `fe46d95718e4e070bdea18ee1c2fbcfc89d5eb3c53b5346d712c72715f667365` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md` | `6e290b70bf2bdaf9785f67fcef4a284a48b08ccce0c0951e72f0322406e58148` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |

## Proof basis and source boundary

In a fixed angular channel, the transformed radial form and one-dimensional
Dirichlet min--max give

$$
q_{\ell,n}^2\geq n^2z_\rho^2+\ell(\ell+1),
\qquad q_{0,n}=nz_\rho.
$$

Zero extension from $H_0^1(\rho,1)$ to $H_0^1(0,1)$ preserves the form,
norm, and angular channel. Hardy's inequality controls the ball centrifugal
term, so fixed-channel min--max has the direction

$$
q_{\ell,n}^{\rm shell}(\rho)\geq j_{\ell+1/2,n}.
$$

On the ball, comparison of the common angular-channel form domains also
gives, for $p>\ell$,

$$
j_{p+1/2,n}^2
\geq j_{\ell+1/2,n}^2+p(p+1)-\ell(\ell+1).
$$

These three comparisons are internal. The old `SRC-LORCH` obligation
supplies only the first-positive-zero bounds at orders $5/2$, $7/2$, and
$9/2$. The new external payload is narrower still: the published Lorch
inequality at $\nu=11/2$ implies

$$
j_{11/2,1}>\frac{17}{2},
$$

and DLMF identifies the corresponding positive spherical and ordinary
Bessel zeros. The exact reduction has positive sides and

$$
507^2\cdot77-4264^2=1611077>0.
$$

The bound $j_{3/2,2}>77/10$ is **internal**, reconstructed from the second
positive solution of $\tan x=x$; it is not part of the external payload.
Likewise, the complete tangent-cell proof of $j_{5/2,2}>9$, every shell
comparison, every higher-order ball shift, all multiplicities, and all Weyl
payments are internal. No source is used for a shell cross-product zero.

For the high-ratio band, the exhaustive inventory through $k_6$ is:

- for $\rho_c\leq\rho\leq1/4$, first modes $0\leq\ell\leq4$ and only the
  possible second modes $(0,2)$ and $(1,2)$;
- for $1/4\leq\rho\leq7/8$, only first modes $0\leq\ell\leq5$.

The strict-count caps are consequently

$$
4,9,16,25,26,29,36.
$$

The fixed/moving bridges at $3/10$, $1/2$, $1/2$, $1/5$, and $13/25$
all have strict exact reserves. At $K=2z_\rho$ the exact $(0,2)$ mode is
excluded, and the proof never uses the false shortcut
$\mathcal W(\rho,k_5)>25$ near $\rho_c$. The independently reproduced
finite ledger checks all delayed entries, both order changes
$p_1=k_6$ and $2z_\rho=k_6$, and every equality face.

For $\rho_0<\rho<\rho_c$, all $n\geq3$ modes, all first modes
$\ell\geq6$, and all second modes $\ell\geq3$ are absent through $K=d$.
The exhaustive strict caps are

$$
1,4,9,10,16,17,26,29,40,45,
$$

with every fixed threshold open and the moving $2z_\rho$ face owned by the
lower-count side. The exact ordering

$$
4<\frac{51}{10}<\frac{13}{2}<\frac{15}{2}
<\frac{77}{10}<\frac{17}{2}<9<d
$$

and the internally proved ball shifts make the inventory exhaustive. The
lower fixed-threshold payments, the payment at the true lower wall $L$, and
both sides of $2z_\rho$ are all strict. A4 reproduced 245 exact checks,
including 50 lower-cap cases, 63 residual-face cases, and every dependency
hash; its 24 focused tests pass.

Finally, directed elementary bounds prove

$$
d<U(\rho)\quad(\rho_*<\rho<\rho_c),
\qquad
k_6(\rho)<U(\rho)\quad(\rho_c\leq\rho<7/8).
$$

Thus both promoted pieces lie strictly below the inherited upper floor.

## Exact post-promotion bookkeeping

The promoted analytic cover is

$$
\boxed{
\begin{aligned}
\mathcal A_{19}=\mathcal A_{18}
&\cup\left\{\rho_0<\rho<\rho_c,
\ L(\rho)<K\leq d\right\}\\
&\cup\left\{\rho_c\leq\rho\leq\frac78,
\ z_\rho\leq K\leq k_6(\rho)\right\}.
\end{aligned}}
$$

Only the part above $k_5$ of the second displayed band is new. Exact
subtraction from $\mathcal D_{18}$ gives

$$
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\left\{\rho_*<\rho\leq\frac1{\sqrt{337}},
\ L(\rho)<K<U(\rho)\right\}\\
&\cup
\left\{\frac1{\sqrt{337}}<\rho<\rho_c,
\ d<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\leq\rho<\frac78,
\ k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}}
$$

At $\rho=1/\sqrt{337}$ one has $L=d$, so the candidate fiber is empty and
the entire inherited slice remains in the first component. The faces $K=d$
and $K=k_6$ are newly covered; $K=U$, $\rho=\rho_*$, and $\rho=7/8$
retain their inherited owners. The $\rho=\rho_c$ slice belongs to the high
band. The already absorbed certificates $B_0$ and $B_1$ remain regression
evidence and are not subtracted again.

The residual is nonempty. At $\rho=1/2$, the inherited upper floor is
$U=K_0>64$, while $\pi<22/7$ gives

$$
k_6(1/2)^2=4\pi^2+42<\frac{3994}{49}<100.
$$

Hence

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2),
$$

so $(1/2,30)\in\mathcal D_{19}$. Therefore `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target`
remain `open`, while `COMP-certified-bessel` remains `diagnostic_only`.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SRC-ROUND19-BESSEL-ZEROS",
        "type": "source_audit",
        "track": "source_audit",
        "title": "Source audit: Round 19 exact-order Bessel zero input",
        "status": "proved_external_dependency",
        "statement_tex": "The new external payload is only this: Lorch's published strict first-positive-zero inequality, specialized at nu=11/2, implies j_(11/2,1)>17/2, and DLMF 10.47.3 identifies that positive ordinary-Bessel zero with the corresponding spherical-Bessel zero. The bound j_(3/2,2)>77/10 is reconstructed internally from tan x=x and is not an external dependency. No shell-to-ball comparison, shell cross-product zero, higher radial exclusion, multiplicity, or Weyl payment is imported.",
        "dependencies": [],
        "implies": [
          "SHELL-two-sided-staircase"
        ],
        "blockers": [],
        "source_card": "sources/round19_bessel_zero_bounds.md",
        "evidence": {
          "positive": [
            "sources/round19_bessel_zero_bounds.md",
            "rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "criticality": "standard",
        "artifact_hashes": {
          "source_card": "7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f",
          "source_audit": "ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718"
        },
        "reason_for_promotion": "The primary Lorch statement has the required order, radial index, strict direction, positive-zero convention, and scope; exact algebra proves the 17/2 consequence. DLMF supplies only the spherical/ordinary identity. The second-zero 77/10 bound is explicitly separated as an internal tangent-equation argument.",
        "next_action": "Use this obligation only for j_(11/2,1)>17/2 and the positive spherical/ordinary Bessel identification. Keep j_(3/2,2)>77/10, j_(5/2,2)>9, every variational comparison, and every shell-specific conclusion internal."
      },
      {
        "id": "SHELL-two-sided-staircase",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Round 19 two-sided radial-entry and angular staircase",
        "status": "proved_internal",
        "statement_tex": "Let rho_c=1/(1+2 pi), rho_0=1/sqrt(337), z_rho=pi/(1-rho), L(rho)=1/(2 rho), d=sqrt(337)/2, and k_m(rho)=sqrt(z_rho^2+m(m+1)). First, for rho_c<=rho<=7/8 and z_rho<=K<=k_6(rho), N_D(A_(rho,1),K^2)<(2/(9 pi))(1-rho^3)K^3. Second, for rho_0<rho<rho_c and L(rho)<K<=d, the same strict inequality holds. The genuinely new C19 is {rho_0<rho<rho_c, L(rho)<K<=d} union {rho_c<=rho<7/8, k_5(rho)<K<=k_6(rho)}, is contained in D18, and leaves exactly D19={rho_*<rho<=rho_0, L(rho)<K<U(rho)} union {rho_0<rho<rho_c, d<K<U(rho)} union {rho_c<=rho<7/8, k_6(rho)<K<U(rho)}. The faces K=d and K=k_6 are included; no claim is made on D19.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-next-angular-staircase",
          "SRC-LORCH",
          "SRC-FLPS-balls",
          "SRC-ROUND19-BESSEL-ZEROS"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round19.md",
            "rounds/polya-main/round_019/exploration/residual-mask-freeze.md",
            "computations/round19_residual_mask.py",
            "computations/tests/test_round19_residual_mask.py",
            "rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md",
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/exploration/candidate-claim-freeze.md",
            "sources/round19_bessel_zero_bounds.md",
            "rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md",
            "rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md",
            "rounds/polya-main/round_019/exploration/lower-ratio-route.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md",
            "computations/round19_verify_two_sided_staircase.py",
            "computations/tests/test_round19_verify_two_sided_staircase.py",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
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
          "SHELL-next-angular-staircase",
          "SRC-LORCH",
          "SRC-FLPS-balls",
          "SRC-ROUND19-BESSEL-ZEROS"
        ],
        "falsification_cases": [
          "rho=rho_*, 1/sqrt(337), rho_c, 1/5, 1/4, 3/10, 1/2, 13/25, 5/6, and 7/8, with both traces at every interior split",
          "K=L(rho), z_rho, k_2 through k_6, 2z_rho, p_1(rho), d, U(rho), and every fixed threshold, including empty and degenerate subbands",
          "radial indices n=1,2,3 and angular orders ell=0 through 6, all remaining-mode exclusions, full multiplicities, and cross-order coincidences",
          "the exact ell=0 frequencies nz_rho, strict ownership at K=2z_rho, and exclusion of every n>=3 mode",
          "the complete tangent-cell proof of j_(5/2,2)>9 and the internal tan x=x proof of j_(3/2,2)>77/10",
          "the fixed-channel zero-extension form domain, Hardy finiteness, angular preservation, min-max direction, and the ball angular-shift comparison",
          "the exact source scope, order, radial index, strict direction, and positive-zero convention of every Bessel statement",
          "all high caps 4,9,16,25,26,29,36 and lower caps 1,4,9,10,16,17,26,29,40,45 paid strictly on both sides of every moving or fixed split",
          "the false uniform payment W(rho,k_5)>25 near rho_c explicitly rejected",
          "all monotonicities, derivative signs, denominators, radicals, positive squarings, inverse steps, and extremal substitutions",
          "d<U and k_6<U against every active H0, K0, seam, endpoint, and interface branch",
          "C19 subset D18 and the exact three-piece D19 subtraction, including the empty fiber L=d at rho=1/sqrt(337)",
          "B0 and B1 retained as inherited covered regression artifacts and not subtracted again",
          "D19 nonempty and no compact, uniform, theorem, program, or certified-computation status promoted",
          "no executable ledger, sampled root, plot, source overreach, or agent agreement used as a substitute for analytic proof"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "baseline_graph": "24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e",
          "residual_packet": "33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50",
          "residual_freeze": "0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9",
          "residual_classifier": "bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6",
          "residual_tests": "41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787",
          "residual_audit": "9e7dedaab08425166998a5c766bdb32d3787d9f35b6c4bf4b7d6be07009c9b43",
          "frozen_claim": "87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db",
          "candidate_freeze": "7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff",
          "new_zero_source_card": "7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f",
          "new_zero_source_audit": "ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718",
          "high_incumbent": "b9a86f1411a8e63c30b6ae5e2b3a65e167426f0b72a4447d15d4e833c5df6983",
          "low_incumbent": "1a4cd1eb93c286816346ead50edef0f151f8b1a287186ba3b20e37336c16b681",
          "clean_room": "24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17",
          "constant_verifier": "4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23",
          "constant_tests": "1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08",
          "constant_review": "fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7",
          "cross_comparison": "fe46d95718e4e070bdea18ee1c2fbcfc89d5eb3c53b5346d712c72715f667365",
          "adversarial_referee": "6e290b70bf2bdaf9785f67fcef4a284a48b08ccce0c0951e72f0322406e58148",
          "spectral_packet": "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
          "lorch_source_card": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
          "flps_source_card": "27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38"
        },
        "reason_for_promotion": "Every mandatory gate passed. The incumbents and isolated A3 independently proved both analytic bands, all spectral exclusions and multiplicity caps, strict Weyl payments, upper-floor containment, and exact subtraction. A4 reproduced 245 exact checks and every face. The new source scope is narrow and explicit. The fresh referee reconstructed the implication adversarially and found no unsupported step.",
        "next_action": "Use this lemma only through the included K=d and K=k_6 faces. Freeze D19 and close its exact three components; do not infer anything for K>d in the middle-ratio component or K>k_6 in the high-ratio component."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "implies_added": [
          "SHELL-two-sided-staircase"
        ]
      },
      {
        "id": "SHELL-sturm-liouville-completeness",
        "implies_added": [
          "SHELL-two-sided-staircase"
        ]
      },
      {
        "id": "SHELL-next-angular-staircase",
        "status": "proved_internal",
        "implies_added": [
          "SHELL-two-sided-staircase"
        ],
        "next_action": "Retain the exact closed Round 18 band through k_5 as a dependency of SHELL-two-sided-staircase. Its statement and proof are unchanged; subsequent high-ratio work begins strictly above k_6."
      },
      {
        "id": "SRC-LORCH",
        "implies_added": [
          "SHELL-two-sided-staircase"
        ],
        "next_action": "Retain only the three audited first-zero bounds at orders 5/2, 7/2, and 9/2. The new order-11/2 dependency is owned separately by SRC-ROUND19-BESSEL-ZEROS."
      },
      {
        "id": "SRC-FLPS-balls",
        "implies_added": [
          "SHELL-two-sided-staircase"
        ]
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Retain the complete Round 18 analytic cover A18, both endpoint theorems, and the all-ratio theorem for K>=295^2. Let rho_c=1/(1+2 pi), rho_0=1/sqrt(337), z_rho=pi/(1-rho), L(rho)=1/(2 rho), d=sqrt(337)/2, and k_6(rho)=sqrt(z_rho^2+42). The promoted cover is A19=A18 union {rho_0<rho<rho_c, L(rho)<K<=d} union {rho_c<=rho<=7/8, z_rho<=K<=k_6(rho)}. The exact residual is D19={rho_*<rho<=rho_0, L(rho)<K<U(rho)} union {rho_0<rho<rho_c, d<K<U(rho)} union {rho_c<=rho<7/8, k_6(rho)<K<U(rho)}. B0 and B1 remain inside the previously promoted cover and are not subtracted again. No claim that D19 is empty is made.",
        "dependencies_added": [
          "SHELL-two-sided-staircase"
        ],
        "permitted_dependencies_added": [
          "SHELL-two-sided-staircase"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round19.md",
            "rounds/polya-main/round_019/exploration/residual-mask-freeze.md",
            "computations/round19_residual_mask.py",
            "computations/tests/test_round19_residual_mask.py",
            "rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md",
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/exploration/candidate-claim-freeze.md",
            "rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md",
            "rounds/polya-main/round_019/exploration/lower-ratio-route.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "the exact three-piece D19 rather than D18 or a rectangular proxy",
          "the empty candidate fiber L=d at rho=1/sqrt(337) and retention of that whole inherited slice",
          "the rho=rho_c slice assigned to the high band, with K=d and K=k_6 newly covered",
          "d<U and k_6<U against every active upper-floor branch and interface",
          "B0 and B1 retained as analytically redundant certificates and not subtracted again",
          "nonemptiness of D19, including the exact witness rho=1/2 and K=30, not confused with theorem closure"
        ],
        "reason_for_update": "The independently proved lower and high staircase bands are added by exact set union and exact subtraction. All inherited endpoint, seam, high-frequency, and certificate owners remain unchanged.",
        "next_action": "Treat C19 as discharged. Close exactly D19: the low-ratio component through rho=1/sqrt(337), the middle component above d, and the high component strictly above k_6, all below U."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md",
            "rounds/polya-main/round_019/exploration/lower-ratio-route.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D19 remains nonempty, including rho=1/2 and K=30",
          "the rho<=1/sqrt(337) component receives no new lower-ratio coverage",
          "the middle component above d and high component above k_6 require new arguments"
        ],
        "next_action": "Keep this obligation open. Freeze and close the exact three-piece D19 while preserving every strict and inclusive face."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "C19 is a two-sided compact-band compression, not compact all-frequency closure",
          "the exact nonempty D19 remains the blocker after both endpoint theorems"
        ],
        "next_action": "Both endpoint neighborhoods, all ratios at K>=295^2, C17, C18, and C19 are proved. Keep this obligation open until exact D19 is closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md",
            "rounds/polya-main/round_019/exploration/lower-ratio-route.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D19 remains nonempty and prevents theorem promotion",
          "B0 and B1 provide no coverage outside the already promoted analytic region",
          "the full theorem still requires complete D19 closure and fresh theorem-level review"
        ],
        "next_action": "The strict shell inequality now includes both endpoints, the all-ratio high-frequency range, C17, C18, and C19. Complete exact D19 coverage, then run fresh theorem-level clean-room and adversarial audits before changing this status."
      },
      {
        "id": "POLYA-program-target",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "TARGET-shell-d3 remains open on the exact nonempty residual D19",
          "a two-sided finite-band lemma cannot promote the program theorem"
        ],
        "next_action": "Keep the program target open. First close D19, certify any genuinely uncovered finite remainder if required, and pass theorem-level clean-room and adversarial review for TARGET-shell-d3."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "computations/round19_verify_two_sided_staircase.py",
            "computations/tests/test_round19_verify_two_sided_staircase.py",
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md"
          ]
        },
        "falsification_cases_added": [
          "the Round 19 exact constant ledger is analytic support, not interval-certified spectral computation",
          "B0 and B1 remain valid but analytically redundant inside the promoted cover",
          "no Round 19 certified subset is promoted"
        ],
        "next_action": "Keep the parent diagnostic_only. B0 and B1 remain regression certificates inside the analytic cover. Any later finite certificate must be a predeclared face-connected subset of exact D19 and pass an independent checker."
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
        "reason": "The fixed-ratio high-frequency theorem and K0 upper branch are unchanged."
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
        "reason": "The exact closed Round 17 band and proved_internal status are unchanged."
      },
      {
        "id": "SHELL-next-angular-staircase",
        "reason": "Its Round 18 theorem statement and proved_internal status are unchanged; only reverse dependency metadata and its next action are refreshed."
      },
      {
        "id": "SRC-LORCH",
        "reason": "Its three Round 18 specializations and proved_external_dependency status are unchanged; the new order-11/2 source is kept separate."
      },
      {
        "id": "SRC-FLPS-balls",
        "reason": "Its audited external statement and status are unchanged; only reverse dependency metadata is added."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "reason": "It remains proved_internal; A19 replaces A18 as the recorded cover and D19 replaces D18 as the exact residual."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "The B0 certificate remains certified, byte-unchanged, and analytically redundant inside the promoted cover."
      },
      {
        "id": "COMP-certified-bessel-pilot-round17",
        "reason": "The B1 certificate remains certified, byte-unchanged, and analytically redundant inside the promoted cover."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No Round 19 interval certificate was produced; the parent remains diagnostic_only."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "C19 shrinks both inherited ratio components but does not close the exact nonempty D19."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The exact D19 still blocks ratio-uniform closure."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The full shell theorem remains open on D19 and still requires theorem-level final review after closure."
      },
      {
        "id": "POLYA-program-target",
        "reason": "The program target remains open because TARGET-shell-d3 remains open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 8,
    "reason": "All promotion gates passed. Round 19 proves two independent analytic extensions: the high-ratio staircase through k_6, including the first radial entry, and the lower-ratio staircase through d. It audits the only new external first-zero specialization, reconstructs the remaining zero bounds internally, and replaces D18 by the exact strict subset D19. D19 is explicitly nonempty, so no compact or theorem-level target is closed."
  }
}
```

## Application gate and status audit

Before applying this patch, every fixed hash above must still match, the
Round 19 exact verifier and focused tests must remain PASS, and the complete
test suite must pass. The patch must be applied once through the validator
with `--round-index 19`; this judge does not apply it.

The new dependency direction is

~~~text
SRC-ROUND19-BESSEL-ZEROS + SRC-LORCH + SRC-FLPS-balls
    + CONV-strict-counting + SHELL-sturm-liouville-completeness
    + SHELL-next-angular-staircase
        -> SHELL-two-sided-staircase
        -> SHELL-rho-compact-analytic-envelope
        -> SHELL-rho-compact
        -> SHELL-rho-uniformity
        -> TARGET-shell-d3
~~~

The graph remains acyclic. `SHELL-two-sided-staircase` is the only new
internal lemma, and `SRC-ROUND19-BESSEL-ZEROS` is the only new external
source obligation. No target status is promoted, no certified computation is
created, and both inherited certificates retain their existing status and
scope.
