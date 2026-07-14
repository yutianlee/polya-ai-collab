# Round 20 Judge

Date: 2026-07-15

## Decision

**PASS. First unsupported implication: none.**

Promote the frozen Round 20 combined closure. With

$$
\rho_c=\frac1{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
$$

and

$$
\mathcal W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3,
$$

the following three conclusions are proved.

First, the complete accepted lower part of the Round 19 residual is closed:

$$
\begin{aligned}
\mathcal D_{19}^{\rm low}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}
\end{aligned}
$$

implies

$$
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).
$$

Second, the closed high staircase is extended through $k_{11}$:

$$
\rho_c\leq\rho\leq\frac78,\qquad
z_\rho\leq K\leq k_{11}(\rho)
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).
$$

Third, the all-frequency optical theorem is extended to

$$
\frac{39}{50}\leq\rho<1,\qquad K\geq0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)\leq\mathcal W(\rho,K),
$$

with equality only at $K=0$ and strict comparison for $K>0$.

Relative to the accepted Round 19 cover, the genuinely new set is

$$
\boxed{
\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K\leq k_{11}(\rho)\}\\
&\cup\{39/50\leq\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

Exact subtraction leaves

$$
\boxed{
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

This residual is nonempty, so the full shell Pólya theorem is **not yet
proved**. `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
and `POLYA-program-target` remain `open`. `COMP-certified-bessel` remains
`diagnostic_only`.

The accepted baseline is commit
`658674117632d60990ac9b9046aa0fcff9e91a62`. Its applied Round 19 graph is
`state/proof_obligations.yml`, SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.

All mandatory gates passed: the residual and proof-free candidate were
frozen independently; A3 reconstructed the complete claim in isolation; the
zero/source reviewer independently rebuilt every zero obligation; the final
repaired A4 ledger passed an independent audit; the cross-comparison found no
remaining mathematical discrepancy; and a fresh adversarial referee assumed
the claim false, reconstructed every branch and face, and returned PASS.

## Fixed evidence hashes

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` |
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| `rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md` | `819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467` |
| `rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md` | `01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c` |
| `rounds/polya-main/round_020/reviews/combined-closure-clean-room.md` | `7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb` |
| `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md` | `7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c` |
| `rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md` | `2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8` |
| `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md` | `6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae` |
| `rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md` | `4b7a7810a12177002f24a16ef60a206669e07fa29e80c3018d2b85add5d1099b` |
| `rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md` | `acea3818e562a8bc27496f1c727835f7a08e70ce60aaa28946fb8999ddf6c9cc` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` |
| `sources/round20_k11_zero_bounds.md` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-adversarial-audit.md` | `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md` | `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31` |

The candidate and fresh referee additionally authenticate all ten permitted
foundational packets/source cards and every incumbent lower, staircase,
zero, and optical artifact. The referee checked 49 unique path/hash pairs;
all matched their current bytes.

## Proof basis and source boundary

For each angular channel, the interval comparison, fixed-channel zero
extension, and common-domain ball comparison give, at the same radial index,

$$
q_{\ell,n}^2\geq n^2z_\rho^2+\ell(\ell+1),\qquad
q_{\ell,n}^2\geq j_{\ell+1/2,n}^2,
$$

$$
j_{p+1/2,n}^2\geq j_{\ell+1/2,n}^2
+p(p+1)-\ell(\ell+1)\qquad(p\geq\ell).
$$

The form domains, min--max directions, angular channels, and radial indices
were independently reconstructed. Hardy's inequality controls the ball
centrifugal term.

The exact half-integer recurrences, tangent-cell enumeration, interlacing,
and ODE simplicity prove internally

$$
\begin{gathered}
j_{3/2,2}>77/10,\quad j_{5/2,2}>9,\quad
j_{7/2,2}>103/10,\quad j_{11/2,2}>129/10,\\
j_{3/2,3}>21/2,\quad j_{5/2,3}>61/5,\quad
j_{13/2,1}>10,\quad j_{15/2,1}>23/2.
\end{gathered}
$$

The only indispensable new external zero payload is the qualified Lorch
first-positive-zero inequality at order $21/2$, which exact positive-side
algebra turns into $j_{21/2,1}>69/5$. The same Lorch formula also gives the
stated $17/2$ and $19/2$ bounds, but those two have independent internal
derivations from $j_{15/2,1}>23/2$ and the same-index angular comparison.
DLMF supplies only the spherical/ordinary identity, explicit half-integer
formulas, and recurrences. No higher radial zero, shell cross-product zero,
angular propagation, multiplicity, or Weyl payment is imported.

For the lower closure, the shifted-tail wedge gains one full floor unit and
keeps the interface remainder below $1/4$. The finite ledger through
$\sqrt{114}$ has the exhaustive strict caps

$$45,46,59,66,69,78.$$

Above that wall, the aggregate floor inequality fails only on the exact cell

$$
\mathcal B=\{\sigma<\rho<\rho_c,\ K>\sqrt{114},\
\rho K\geq5/2,\ K<2/\omega_0\},
$$

where the strict phase-proxy vector has weighted sum $395$ and is strictly
paid. The wedge owns $\rho=\sigma$, the finite ledger owns
$K=\sqrt{114}$, the exceptional cell owns $\rho K=5/2$, and the aggregate
branch owns $K=2/\omega_0$. Hence no lower fiber survives.

For the high staircase, every complete inventory through $k_7,ldots,k_{11}$
was reconstructed with full multiplicity. The rational localization faces
and the algebraic faces $z^2=16,68/3,34$ were checked on their expected
sides, with equality excluding the defining mode. The A3 addendum corrects
its sole false comparative-reserve sentence: the conservative
$k_9,H=6,h=4$ cap-74 row is either empty under full zero propagation or is
directly paid by

$$
\mathcal W(7/20,207/20)
>74+\frac{727261673}{704000000}.
$$

This correction changes neither the frozen candidate nor the A3 theorem
verdict.

For the optical theorem, the product deficit satisfies

$$D(a)>\frac{1382}{3125}a^2\qquad(a>\pi).$$

The inclusive low and high screens meet at $a=c/\varepsilon$, with

$$
c=1126/625,\qquad q=106/333,
$$

and have exact positive endpoint reserves

$$
R_L=\frac{39569}{2772225000},\qquad
R_H=\frac{14817541}{472867032960000}.
$$

The complementary-action argument splits at the actual ungridded inner
interface and retains strict radial and angular walls. It re-establishes every
sign for $0<\varepsilon\leq11/50$; it does not extrapolate the Round 16
endpoint conclusion.

## Preserved A4 failure chronology

The two superseded A4 cycles are retained as negative evidence only.

1. `combined-closure-constants-adversarial-audit.md`, SHA-256
   `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd`,
   rejected the original verifier because it paid only $73$ in the live
   cap-74 row and contained tautological or disconnected labels.
2. `combined-closure-constants-replacement-audit.md`, SHA-256
   `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31`,
   rejected the first replacement because of an actual `0x08` byte,
   localization checks that survived an expected-output mutation, an
   insufficient wrong-wall test, and authenticated-looking skip-hash output.

Only the final repaired verifier at `086beb09...`, its tests at
`4936f4ef...`, its report at `df56599f...`, and the independent final audit
at `6322802e...` are positive A4 evidence. They report 587 passing checks
(488 substantive, 65 bookkeeping, and 34 authentication) and 17 focused
tests. The executable ledger is exact analytic support, not interval-certified
spectral computation.

## Exact post-promotion bookkeeping

The lower theorem removes the first two components of $\mathcal D_{19}$,
including the complete $\rho=\rho_0$ fiber. Since $k_{11}<U$, the staircase
removes exactly $k_6<K\leq k_{11}$ from the high component. The optical
theorem then removes every remaining high-component point with
$39/50\leq\rho<7/8$.

On $\rho_c\leq\rho<39/50$, one has $\rho_c>\omega_0$ and
$39/50<5/6$. Thus neither $H_0$ nor the seam branch is eligible and
$U=K_0$ exactly. The complete face assignment is:

| face | owner after Round 20 |
|---|---|
| $\rho=\rho_0$ | removed with the first lower component; $L=d$ there |
| $\rho=\sigma$ | lower shifted-tail wedge |
| $\rho=\rho_c$ | staircase through $k_{11}$; residual above $k_{11}$ |
| $\rho=39/50$ | optical theorem, all frequencies |
| $\rho=7/8$ | inherited thin endpoint and optical theorem |
| $K=L(\rho)$ | inherited predecessor, excluded from the old residual |
| $K=d$ | Round 19 predecessor |
| $K=\sqrt{114}$ | Round 20 finite lower ledger |
| $K=k_6(\rho)$ | Round 19 predecessor |
| $K=k_7,\ldots,k_{11}$ | Round 20 staircase; each upper face included |
| $K=K_0(\rho)=U(\rho)$ | inherited upper owner; excluded from $\mathcal D_{20}$ |
| $a=c/\varepsilon$ | both inclusive optical screens |
| $K=0$ | optical equality face |

The new residual is nonempty. Since
$\rho_c<1/2<39/50$ and $\pi<22/7$,

$$
k_{11}(1/2)^2=4\pi^2+132
<\frac{8404}{49}<196,
$$

so $k_{11}(1/2)<14<30$. The inherited exact upper-floor estimate gives
$K_0(1/2)>64$, and only the $K_0$ branch is eligible at $\rho=1/2$.
Therefore

$$
k_{11}(1/2)<30<K_0(1/2)=U(1/2),
$$

and $(1/2,30)\in\mathcal D_{20}$. The inherited certificates $B_0$ and
$B_1$ remain inside the already promoted cover and are not subtracted again.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SRC-ROUND20-BESSEL-ZEROS",
        "type": "source_audit",
        "track": "source_audit",
        "title": "Source audit: Round 20 exact-order Bessel zero input",
        "status": "proved_external_dependency",
        "statement_tex": "The only indispensable new external zero payload is Lorch's published strict first-positive-zero inequality specialized at nu=21/2, which implies j_(21/2,1)>69/5 by exact positive-side radical algebra. The same formula also yields the stated order-17/2 and order-19/2 bounds, but those two are independently recoverable internally from j_(15/2,1)>23/2 and same-index angular min-max. DLMF 10.47.3, 10.49(i), and 10.51.1--10.51.2 supply only the spherical/ordinary identity, explicit half-integer formulas, and recurrences. Every n>=2 zero, the strengthened first-zero bounds j_(13/2,1)>10 and j_(15/2,1)>23/2, root enumeration, ODE simplicity, shell-to-ball comparison, angular propagation, inventory, and payment is internal.",
        "dependencies": [],
        "implies": [
          "SHELL-combined-closure"
        ],
        "blockers": [],
        "source_card": "sources/round20_k11_zero_bounds.md",
        "evidence": {
          "positive": [
            "sources/lorch_bessel_zeros.md",
            "sources/round20_bessel_zero_bounds.md",
            "sources/round20_higher_radial_zero_bounds.md",
            "sources/round20_k10_zero_bounds.md",
            "sources/round20_k11_zero_bounds.md",
            "rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "criticality": "standard",
        "artifact_hashes": {
          "lorch_source_card": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
          "round20_lorch_card": "2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3",
          "higher_radial_internal_card": "8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7",
          "k10_mixed_card": "a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926",
          "k11_mixed_card": "eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240",
          "zero_provenance_audit": "2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8",
          "fresh_referee": "acea3818e562a8bc27496f1c727835f7a08e70ce60aaa28946fb8999ddf6c9cc"
        },
        "reason_for_promotion": "The qualified primary Lorch statement has the required positive-zero convention, order, radial index, strict direction, and scope; exact algebra proves the 69/5 consequence. The isolated zero audit and fresh referee independently separate this narrow external payload from every internal recurrence, higher-radial zero, variational comparison, count, and payment.",
        "next_action": "Use this obligation only for the qualified first-positive-zero payload at order 21/2 and the labelled DLMF identities. Keep every higher-radial zero, strengthened lower-order first zero, shell comparison, angular propagation, cap, and Weyl payment internal."
      },
      {
        "id": "SHELL-combined-closure",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Round 20 lower closure, k11 staircase, and optical extension",
        "status": "proved_internal",
        "statement_tex": "Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), k_m(rho)=sqrt(z_rho^2+m(m+1)), and W(rho,K)=(2/(9 pi))(1-rho^3)K^3. The strict Polya inequality holds on the complete accepted lower residual D19^low={rho_*<rho<=rho_0, L(rho)<K<U(rho)} union {rho_0<rho<rho_c, d<K<U(rho)}. It also holds for rho_c<=rho<=7/8 and z_rho<=K<=k_11(rho). Moreover, for 39/50<=rho<1 and K>=0, N_D(A_(rho,1),K^2)<=W(rho,K), with equality only at K=0 and strict comparison for K>0. The genuinely new C20 is D19^low union {rho_c<=rho<7/8, k_6(rho)<K<=k_11(rho)} union {39/50<=rho<7/8, k_11(rho)<K<U(rho)}. Exact subtraction leaves D20={rho_c<=rho<39/50, k_11(rho)<K<K_0(rho)=U(rho)}. The faces rho=rho_c and K=k_11 remain in the stated owners, rho=39/50 is optical-owned, K=U is excluded, and no claim is made on D20.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-small-hole",
          "SHELL-rho-one-endpoint",
          "SHELL-two-sided-staircase",
          "SRC-annuli",
          "SRC-FLPS-balls",
          "SRC-LORCH",
          "SRC-ROUND20-BESSEL-ZEROS"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round20.md",
            "computations/round20_residual_mask.py",
            "computations/tests/test_round20_residual_mask.py",
            "rounds/polya-main/round_020/exploration/residual-mask-freeze.md",
            "rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md",
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/exploration/candidate-claim-freeze.md",
            "rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md",
            "rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md",
            "rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md",
            "computations/round20_verify_combined_closure.py",
            "computations/tests/test_round20_verify_combined_closure.py",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md",
            "rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ],
          "negative": [
            "rounds/polya-main/round_020/reviews/combined-closure-constants-adversarial-audit.md",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md"
          ],
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
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-small-hole",
          "SHELL-rho-one-endpoint",
          "SHELL-two-sided-staircase",
          "SRC-annuli",
          "SRC-FLPS-balls",
          "SRC-LORCH",
          "SRC-ROUND20-BESSEL-ZEROS"
        ],
        "falsification_cases": [
          "rho=rho_*, rho_0, sigma, rho_c, 39/50, 1/2, 5/6, and 7/8, with both traces at every interior split",
          "K=L(rho), d, 10, 81/8, 21/2, sqrt(7073)/8, sqrt(114), 2/omega_0, z_rho, k_6 through k_11, K_0, H_0, the seam floor, and U",
          "the complete rho=rho_0 fiber, the wedge-owned rho=sigma face, the finite-ledger-owned sqrt(114) face, and the exceptional/aggregate ownership at rho K=5/2 and K=2/omega_0",
          "the unique exceptional lower floor cell B and the complete multiplicity-weighted proxy cap 395",
          "radial indices n=1,2,3,4 and angular orders ell=0 through 14, with full angular multiplicities and all remaining-mode exclusions",
          "fixed-channel form domains, Hardy finiteness, min-max directions, radial-index preservation, zero extension, angular propagation, and positive-zero conventions",
          "all internal half-integer zero enumerations and the exact external first-zero scope at order 21/2",
          "every k_7 through k_11 inventory, incompatibility, localization ratio, algebraic split, fixed/moving bridge, coincidence, and equality exclusion",
          "the conservative k_9 H=6 h=4 cap-74 cell, including both its full-propagation emptiness proof and its direct coarse payment",
          "the false A3 comparative-reserve sentence used nowhere and corrected only through the immutable addendum",
          "the optical product deficit, radial-cell integer convention, low/high inclusive common face, ungridded inner interface, sawtooth bounds, layer count, endpoint reserves, K=0 equality, and epsilon=11/50 face",
          "k_11<U on rho_c<=rho<7/8 and U=K_0 exactly on rho_c<=rho<39/50",
          "exact C20 subset D19 and exact subtraction to the one-piece D20 with every strict and included face",
          "D20 nonempty at rho=1/2 and K=30, with no compact, uniform, theorem, program, or computation status promoted",
          "both superseded A4 FAIL cycles retained as negative chronology and only the final repaired bundle used positively",
          "no executable ledger, sampled root, plot, source overreach, or agent agreement used as a substitute for the analytic proof"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
          "rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "baseline_graph": "ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187",
          "residual_packet": "a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8",
          "residual_classifier": "5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2",
          "residual_tests": "d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164",
          "residual_freeze": "172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7",
          "residual_audit": "b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f",
          "frozen_claim": "e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61",
          "candidate_freeze": "aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87",
          "proof_free_audit": "819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467",
          "final_byte_audit": "01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c",
          "clean_room": "7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb",
          "clean_room_addendum": "7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c",
          "zero_provenance": "2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8",
          "final_constant_verifier": "086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5",
          "final_constant_tests": "4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf",
          "final_constant_report": "df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95",
          "final_constant_audit": "6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae",
          "preserved_a4_failure_1": "4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd",
          "preserved_a4_failure_2": "52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31",
          "cross_comparison": "4b7a7810a12177002f24a16ef60a206669e07fa29e80c3018d2b85add5d1099b",
          "adversarial_referee": "acea3818e562a8bc27496f1c727835f7a08e70ce60aaa28946fb8999ddf6c9cc"
        },
        "reason_for_promotion": "Every mandatory gate passed. Independent analytic reconstructions close both lower residual components, extend the strict staircase through k_11, and prove the all-frequency optical theorem from rho=39/50. The zero/source boundary is exact, the final repaired A4 bundle verifies every finite constant and face, the cross-comparison finds no discrepancy, and the fresh referee reconstructs the complete implication adversarially. Exact subtraction leaves the explicitly nonempty D20, so no theorem-level target is promoted.",
        "next_action": "Use this lemma only on its stated closed lower, staircase, and optical domains. Freeze D20 and close exactly rho_c<=rho<39/50 with k_11(rho)<K<K_0(rho)=U(rho); do not infer anything on that open frequency strip."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-sturm-liouville-completeness",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-phase-enclosures",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-low-interface-small-hole",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SHELL-two-sided-staircase",
        "implies_added": [
          "SHELL-combined-closure"
        ],
        "next_action": "Treat the Round 19 bands and D19 bookkeeping as discharged predecessors. Use SHELL-combined-closure for the complete lower removal, staircase through k_11, and optical extension; do not reuse this predecessor outside its own stated faces."
      },
      {
        "id": "SRC-annuli",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SRC-FLPS-balls",
        "implies_added": [
          "SHELL-combined-closure"
        ]
      },
      {
        "id": "SRC-LORCH",
        "implies_added": [
          "SHELL-combined-closure"
        ],
        "next_action": "Retain the previously audited specializations at orders 5/2, 7/2, and 9/2. The indispensable new order-21/2 payload is owned separately by SRC-ROUND20-BESSEL-ZEROS; every higher-radial and strengthened first-zero bound remains internal."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Retain the complete Round 19 cover A19, both endpoint theorems, and the all-ratio theorem for K>=295^2. Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), and k_m(rho)=sqrt(z_rho^2+m(m+1)). Round 20 adds the complete D19 lower residual, the high band {rho_c<=rho<7/8, k_6(rho)<K<=k_11(rho)}, and the optical remainder {39/50<=rho<7/8, k_11(rho)<K<U(rho)}. Equivalently, the stronger optical theorem holds for 39/50<=rho<1 and every K>=0. The exact residual is D20={rho_c<=rho<39/50, k_11(rho)<K<K_0(rho)=U(rho)}. The rho=rho_c face remains in D20 only above k_11, rho=39/50 is optical-owned, K=k_11 is staircase-owned, and K=U is excluded. B0 and B1 remain inside the previously promoted cover and are not subtracted again. No claim that D20 is empty is made.",
        "dependencies_added": [
          "SHELL-combined-closure"
        ],
        "permitted_dependencies_added": [
          "SHELL-combined-closure"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round20.md",
            "rounds/polya-main/round_020/exploration/residual-mask-freeze.md",
            "rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md",
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md",
            "rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md",
            "rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "the exact one-piece D20 rather than D19 or a rectangular proxy",
          "rho=rho_c retained only above the included k_11 face and rho=39/50 removed inclusively by the optical theorem",
          "U=K_0 on the exact remaining ratio interval because H_0 and the seam branch are ineligible",
          "the strict open frequency strip k_11<K<K_0 with both boundary faces covered by their inherited owners",
          "B0 and B1 retained as analytically redundant certificates and not subtracted again",
          "nonemptiness of D20 at rho=1/2 and K=30 not confused with theorem closure"
        ],
        "reason_for_update": "The independently proved lower closure, k_11 staircase, and optical theorem are added by exact set union and subtraction. All inherited endpoint, seam, high-frequency, and certificate owners remain unchanged.",
        "next_action": "Treat C20 as discharged. Freeze and close exactly D20={rho_c<=rho<39/50, k_11(rho)<K<K_0(rho)=U(rho)} while preserving every strict and inclusive face."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md",
            "rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D20 remains nonempty at rho=1/2 and K=30",
          "the rho=rho_c slice remains open strictly above k_11",
          "the optical rho=39/50 face is covered but ratios immediately below it still contain the open strip"
        ],
        "next_action": "Keep this obligation open. Freeze and close the exact one-piece D20 while preserving rho=rho_c, excluding rho=39/50, and retaining the strict k_11 and K_0 frequency faces."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "the complete lower and optical closures do not cover the exact nonempty D20",
          "a k_11 staircase is not compact all-frequency closure below rho=39/50"
        ],
        "next_action": "Both endpoint neighborhoods, all ratios at K>=295^2, C17 through C20, and the full lower residual are proved. Keep this obligation open until exact D20 is closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "D20 remains nonempty and prevents theorem promotion",
          "the exact verifier is analytic support rather than a spectral interval certificate",
          "the full theorem still requires complete D20 closure and fresh theorem-level review"
        ],
        "next_action": "The strict shell inequality now includes both endpoints, the all-ratio high-frequency range, C17 through C20, and the complete lower and rho>=39/50 regions. Close exact D20, then run fresh theorem-level clean-room and adversarial audits before changing this status."
      },
      {
        "id": "POLYA-program-target",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md"
          ]
        },
        "falsification_cases_added": [
          "TARGET-shell-d3 remains open on exact nonempty D20",
          "a combined finite-band and optical extension cannot promote the program theorem while D20 survives"
        ],
        "next_action": "Keep the program target open. First close D20 and pass theorem-level clean-room and adversarial review for TARGET-shell-d3."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "computations/round20_verify_combined_closure.py",
            "computations/tests/test_round20_verify_combined_closure.py",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md"
          ]
        },
        "falsification_cases_added": [
          "the Round 20 exact constant ledger checks analytic arithmetic and bytes, not interval-certified shell eigenvalues",
          "B0 and B1 remain valid but analytically redundant inside the promoted cover",
          "no Round 20 certified spectral subset or computation obligation is promoted"
        ],
        "next_action": "Keep the parent diagnostic_only. B0 and B1 remain regression certificates inside the analytic cover. Any later certificate must be a predeclared face-connected subset of exact D20 and pass an independent checker."
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
        "reason": "Its accepted rho>=7/8 theorem is unchanged; only reverse dependency metadata records the separately proved optical extension."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "The fixed-ratio high-frequency theorem and K_0 upper branch are unchanged."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "reason": "The accepted seam and its rho=5/6 and seam-frequency faces are unchanged."
      },
      {
        "id": "SHELL-two-sided-staircase",
        "reason": "Its Round 19 theorem and proved_internal status are unchanged; only reverse dependency metadata and next action are refreshed."
      },
      {
        "id": "SRC-LORCH",
        "reason": "Its previously audited specializations and proved_external_dependency status are unchanged; the indispensable new order-21/2 payload is kept separate."
      },
      {
        "id": "SRC-FLPS-balls",
        "reason": "Its audited external statement and status are unchanged; only reverse dependency metadata is added."
      },
      {
        "id": "SRC-annuli",
        "reason": "Its audited source scope is unchanged; only reverse dependency metadata is added."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "reason": "It remains proved_internal; A20 replaces A19 as the recorded cover and D20 replaces D19 as the exact residual."
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
        "reason": "No Round 20 interval-certified spectral computation was produced; the parent remains diagnostic_only."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "C20 closes both lower pieces and the high ratios from 39/50, but it does not close exact nonempty D20."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The exact D20 still blocks ratio-uniform closure."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The full shell theorem remains open on D20 and still requires theorem-level final review after closure."
      },
      {
        "id": "POLYA-program-target",
        "reason": "The program target remains open because TARGET-shell-d3 remains open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 9,
    "reason": "All promotion gates passed. Round 20 closes both lower residual components, extends the strict angular staircase through k_11, and proves the all-frequency optical theorem down to rho=39/50. It isolates the only indispensable new external first-zero payload, reconstructs every other zero internally, preserves both failed A4 cycles while accepting only the final repaired bundle, and replaces D19 by the exact one-piece strict subset D20. D20 is explicitly nonempty, so no compact or theorem-level target is closed."
  }
}
```

## Application gate and status audit

This judge does **not** apply the patch. Before application, every fixed hash
above must still match, the graph and embedded patch must validate, the
Round 20 residual classifier and exact verifier must pass, and the complete
test suite must pass. The reproduction commands are:

```text
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/polya-main/round_020/judge/judge-020.md
python -B computations/round20_residual_mask.py
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round20_residual_mask.py
python -B computations/round20_verify_combined_closure.py
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round20_verify_combined_closure.py
python -B -m pytest -p no:cacheprovider -q
```

If those gates remain green, the patch may be applied exactly once with
`--round-index 20` and
`--judge-ref rounds/polya-main/round_020/judge/judge-020.md`. This file does
not perform that mutation.

The promoted dependency direction is

~~~text
SRC-ROUND20-BESSEL-ZEROS
    + CONV-strict-counting + SHELL-sturm-liouville-completeness
    + SHELL-phase-enclosures + SHELL-weighted-lattice-fractional
    + SHELL-low-interface-small-hole + SHELL-rho-one-endpoint
    + SHELL-two-sided-staircase + SRC-annuli + SRC-FLPS-balls + SRC-LORCH
        -> SHELL-combined-closure
        -> SHELL-rho-compact-analytic-envelope
        -> SHELL-rho-compact
        -> SHELL-rho-uniformity
        -> TARGET-shell-d3
~~~

The graph remains acyclic. `SHELL-combined-closure` is the only new internal
lemma and `SRC-ROUND20-BESSEL-ZEROS` is the only new external source
obligation. No target status is promoted, no certified computation is
created, and both inherited certificates retain their existing status and
scope.
