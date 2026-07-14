# Round 16 Judge

Date: 2026-07-14

## Decision

**PASS. First unsupported implication: none.**

Promote the independently reconstructed thin-shell endpoint

$$
\boxed{
\frac78\le\rho<1,\qquad K\ge0,
\qquad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The lower face $\rho=7/8$ is included and $\rho=1$ is excluded. At $K=0$
both sides vanish. For every $K>0$, the product or phase-proxy comparison is
strict before the final non-strict theorem statement.

This decision also promotes the separately audited four-zone integration:

$$
\boxed{
0<\rho<1,\qquad K\ge295^2=87025
}
$$

including the equality face $K=295^2$. It does not prove the all-frequency
shell theorem. The true compact residual remains open, and no Bessel-root
certificate is promoted.

## Frozen evidence and independence

The frozen packet and final proof artifacts have SHA-256 values

| artifact | SHA-256 |
|---|---|
| state/lemma_packets/SHELL-rho-one-endpoint-round16.md | 5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09 |
| rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md | bc99a0e82bee9f55056e2122f053418b8b6f2586fad515dd115f6d29fb6878b0 |
| rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md | 5a4945c267c0f9d769bec6cf94ad6f7cb3d17c5af593d1837d27553cefb197d7 |
| rounds/polya-main/round_016/exploration/thin-endpoint-constant-inventory.md | 0aeb81f3186d7e8a3ef2d9623edc6bbfd6ab04744079dbc26bcc2b90e77df933 |
| rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md | 185369546a0d88c5d0fdc72ae3390167e67edeb1b4cdd03074a5f1611fdec5fd |
| computations/round16_verify_endpoint.py | 7be9208c5abdb233db18c15dbae87068b134121ee5efcd3825ee293f346afff5 |
| computations/tests/test_round16_endpoint.py | 4f372a5860ea33b19a80daadbb5ddd4382fb11be5e2f8f543a4fdd223a7d219c |

The clean-room proof was completed before seeing the incumbent or other
Round 16 artifacts. The final hostile referee reconstructed both pieces,
returned PASS with no unsupported implication, and then revalidated the two
editorial repairs byte-for-byte. The packet stayed byte-identical.

## Low product piece

Write $\rho=1-\varepsilon$, $a=\varepsilon K$, with
$0<\varepsilon\le1/8$. On

$$
0\le a\le\frac{\pi}{4\varepsilon},
$$

the form inequality

$$
-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1)
$$

has the correct upper-count direction. Strict radial counting gives

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\},
$$

and the exact angular multiplicity for the $n$th radial branch is $M_n^2$.
The range $0\le a\le\pi$ has zero count, including the wall $a=\pi$.

For $a>\pi$, write $a/\pi=N+t$, $N\ge1$, $0<t\le1$, using
$(N,t)=(m-1,1)$ at $a=m\pi$. The exact deficit is

$$
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3},
$$

and completing the square gives

$$
D(a)>\frac25a^2.
$$

The cubic remainder has exact minimum $-8/375$, while its $N=1$ lower
screen is $32/375>0$. The ceiling and quarter-disk costs are bounded by

$$
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
$$

At the closed endpoint the exact reserve is

$$
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
$$

Thus the low comparison is strict for $a>0$ and owns the common optical face.

## High complementary-action piece

On

$$
a\ge\frac{\pi}{4\varepsilon},
$$

the exact piecewise action has a decreasing inverse $R:[0,T]\to[0,a]$.
With $F=R^2$ and $g=-F'$, the incumbent and clean-room derivations
independently prove

$$
g\text{ decreases on }(0,\tau),
\qquad
g\text{ increases on }(\tau,T),
$$

at the actual ungridded interface. They also prove the improper trace at
$t=0$ and

$$
F(\tau)=\rho^2a^2,\qquad g(T)=2\pi\rho a.
$$

For the shifted radial sawtooth, exact one-period integration gives
$W\ge0$ and $-1/32\le\Psi\le3/32$. Splitting Stieltjes integration at the
actual $\tau$ yields

$$
D_{\rm rad}
\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
$$

The strict half-integer count and exact radial-layer count give the complete
angular error

$$
E=\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
$$

The lower screen decreases and the upper screen increases on the complete
domain. At $\varepsilon=1/8$,

$$
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
$$

so

$$
D_{\rm rad}-E>\frac{143}{4096}a^2>0.
$$

This gives the full strict chain $P_{\mathcal A}<I$, not merely an endpoint
reserve. The permitted all-domain phase transfer then proves the high piece.
Equality in the scaling step at $a=\pi/(4\varepsilon)$ is retained as
non-strict; the final reserve remains strict.

## Closed union, walls, and forbidden inputs

The two inclusive sets

$$
\left[0,\frac{\pi}{4\varepsilon}\right],
\qquad
\left[\frac{\pi}{4\varepsilon},\infty\right)
$$

cover every $a\ge0$ and both own their common face. At the corner
$(\varepsilon,a)=(1/8,2\pi)$ the face is also the radial wall with
$(N,t)=(1,1)$.

Every radial, product-angular, action-radial, half-integer, phase-proxy, and
sawtooth wall retains the strict counting convention. The action cutoffs,
the ungridded curvature interface, improper and terminal traces, inverse
domain, denominators, radicands, arccosine arguments, squarings, and
monotonic reductions were explicitly audited.

No conclusion from the Round 5 product theorem, Round 6 aggregate theorem,
or Round 11 bridge or endpoint enters either piece. There is no hidden use of
$\varepsilon\le1/100$, $\rho\ge99/100$, $a\ge125$, the old $61/1400$
reserve, or the rejected pointwise semicircle majorant.

## Four-zone integration

After endpoint promotion, let

$$
I_{16}=\left[\rho_*,\frac78\right].
$$

The exact remaining coarse envelope is:

1. $[\rho_*,1/16]$: possible residual only for $K<64$;
2. $[1/16,5/6]$: possible residual only for
   $K<K_0(\rho)\le K_0(5/6)<295^2=87025$;
3. $[5/6,7/8]$: possible residual only for
   $K<54/(1-\rho)^2\le3456$;
4. $[7/8,1)$: every frequency is covered.

Every adjacent ratio face is owned. Because the residual inequalities are
strict, $K=64$, $K=K_0(5/6)$, $K=3456$, and in particular
$K=295^2$ are covered faces. The exact reduction from the accepted Round 15
ceiling is

$$
\frac{200000}{295^2}=\frac{8000}{3481}>2.
$$

The true unresolved set is

$$
\mathcal D_{16}
=(I_{16}\times[0,\infty))\setminus\mathcal A_{16},
$$

where $\mathcal A_{16}$ is the complete accepted analytic cover with every
owned face. It is not the rectangle $I_{16}\times[0,87025)$.

## Review and executable gates

- Frozen packet and dependency audit: PASS.
- Incumbent proof and embedded exact ledger: PASS.
- Strictly isolated clean-room reconstruction: PASS.
- Independent exact-constant inventory: PASS.
- Fresh adversarial referee and post-repair audit: PASS; first unsupported
  implication: none.
- Standalone exact verifier: 111 finite-algebra checks passed.
- Focused tests: 11 passed.
- Complete computation suite before promotion: 69 passed.
- The finite checks explicitly do not claim to prove the analytic theorem.
- The Round 8 certified pilot is unchanged.

## State Patch

{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-rho-one-endpoint",
        "status": "proved_internal",
        "statement_tex": "For every 7/8<=rho<1 and every K>=0, the strict three-dimensional shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. The lower endpoint rho=7/8 is included, rho=1 is excluded as the degenerate zero-width limit, equality holds at K=0, and the proof comparison is strict for K>0.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-annulus-phase-transfer"
        ],
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-annulus-phase-transfer"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-one-endpoint-round16.md",
            "rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_016/exploration/thin-endpoint-constant-inventory.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md",
            "computations/round16_verify_endpoint.py",
            "computations/tests/test_round16_endpoint.py"
          ]
        },
        "falsification_cases": [
          "K=a=0 and every K=a>0",
          "the exact zero-count range 0<=a<=pi, including a=pi",
          "every radial wall a=m pi with (N,t)=(m-1,1), both one-sided limits, and the first positive branch",
          "every product angular wall b_n^2/epsilon^2=ell(ell+1) with strict exclusion",
          "the common face a=pi/(4 epsilon) from both pieces and the corner (epsilon,a)=(1/8,2 pi)",
          "rho=7/8, epsilon=1/8, the open rho->1 limit, and the test faces epsilon=1/100,1/25,1/10,1/8",
          "every action radial wall n-1/4=T, half-integer angular wall, and phase-proxy integer wall",
          "the outer cutoff y=a, inner interface y=rho a, and actual ungridded curvature interface t=tau",
          "tau below, on, and above a sawtooth grid point and both sides of every sawtooth jump",
          "the improper t=0 trace, terminal t=T trace, and every dropped nonnegative Stieltjes term",
          "the exact inverse domain, denominators, radicands, arccosine arguments, squarings, endpoint limits, and monotonic reductions",
          "the non-strict H10 equality at the common face and final strict reserve",
          "any hidden use of epsilon<=1/100, rho>=99/100, a>=125, an old bridge scale, or a Round 5, 6, or 11 conclusion",
          "the positive S1-S2 screens treated only as planning and the negative S3-S4 screens treated only as route obstructions"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md"
        ],
        "reason_for_promotion": "The frozen Round 16 endpoint was reconstructed through two independent complete proof routes. The low min-max product proof establishes the exact zero range, strict walls, D>(2/5)a^2, and reserve 577/2880. The complementary-action proof establishes the actual ungridded curvature split, improper Stieltjes trace, every strict proxy wall, P_A<I, and reserve 143/4096. Both pieces independently own their common face, use only the exact whitelist, and passed a fresh adversarial and post-repair audit with no unsupported implication.",
        "next_action": "Treat 7/8<=rho<1 as discharged. Any extension below rho=7/8 requires a separately frozen proof; S1-S2 remain planning screens and S3-S4 remain route obstructions only."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_16=[rho_*,7/8]. On [rho_*,1/16], every possible residual has K<64. On [1/16,5/6], every possible residual has K<K_0(rho)<=K_0(5/6)<295^2=87025. On [5/6,7/8], every possible residual has K<54/(1-rho)^2<=3456. On [7/8,1), every frequency is covered. Consequently the strict shell Polya inequality holds for every 0<rho<1 and K>=295^2=87025, including equality.",
        "dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-phase-zero",
          "SHELL-fixed-rho-high-energy",
          "SHELL-central-thin-seam-compression"
        ],
        "permitted_dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-phase-zero",
          "SHELL-fixed-rho-high-energy",
          "SHELL-central-thin-seam-compression"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-one-endpoint-round16.md",
            "rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_016/exploration/thin-endpoint-constant-inventory.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md",
            "computations/round16_verify_endpoint.py",
            "computations/tests/test_round16_endpoint.py"
          ]
        },
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=5/6",
          "rho=7/8",
          "rho=99/100 as a historical endpoint-overlap face",
          "K=64, K=K_0(rho), K=K_0(5/6), K=1944, K=2048, K=2400, K=3456, K=12500, K=295^2=87025, and K=200000",
          "threshold equality at 54/epsilon^2, 32/epsilon^2, 24/epsilon^2, and 20/epsilon^2 on their exact domains",
          "the strict comparison K_0(5/6)<295^2 and coverage of K=295^2 in every ratio band",
          "the four-zone envelope confused with the true nonrectangular residual D_16",
          "the Round 8 certified pilot overextended beyond its protected box",
          "the positive stretch screens below rho=7/8 treated as promoted endpoints"
        ],
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md"
        ],
        "reason_for_promotion": "The independently audited endpoint covers every frequency on [7/8,1). Combined only after promotion with the accepted small-hole, fixed-rho, and Round 15 seam theorems, the remaining four-zone envelope has largest strict residual ceiling K_0(5/6)<295^2=87025. Every shared face, including K=295^2, is owned, and the exact reduction from 200000 is 8000/3481>2.",
        "next_action": "Use I_16=[rho_*,7/8] and the exact nonrectangular D_16 below the complete four-zone analytic cover. Close only D_16 by analytic or certified means; do not replace it by I_16 x [0,87025)."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-one-endpoint-round16.md",
            "rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md"
          ]
        },
        "next_action": "Keep this obligation open until exact analytic or certified coverage closes D_16=(I_16 x [0,infinity)) minus A_16. Never replace the piecewise complement of the accepted four-zone cover by I_16 x [0,87025)."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "next_action": "The parent remains diagnostic_only. Any future E-minus-A manifest must be an exact face-connected subset of D_16; the Round 16 rational ledgers are symbolic analytic evidence, not Bessel-root certificates."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-one-endpoint-round16.md",
            "rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md"
          ]
        },
        "next_action": "Both complete endpoint neighborhoods and the all-ratio range K>=295^2=87025 are proved. Keep this obligation open until the exact compact residual D_16 is closed."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-one-endpoint-round16.md",
            "rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md",
            "rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md"
          ]
        },
        "next_action": "The strict shell inequality is proved for every ratio when K>=295^2=87025. Complete exact coverage of D_16, then run fresh theorem-level clean-room and adversarial audits."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "falsification_cases": [
          "epsilon=1/100, 1/25, 1/20, 1/10, 1/8, and 1/6",
          "K=20/epsilon^2 on the retained Round 10 range, K=24/epsilon^2 on the retained Round 13 range, K=32/epsilon^2 on the retained Round 14 range, and K=54/epsilon^2 on the enlarged range",
          "rho=99/100, 24/25, 19/20, 9/10, 7/8, and 5/6 from both adjacent regimes",
          "no-drop p=n, immediate-drop p=0, degenerate head n=0, sign wall R=0 from both sides, and the first R>0 branch",
          "the wall mu-x_0 in Z, both adjacent beta cells, q=mu, and the low/high interface x_0=mu",
          "every ordinary-floor, coarse-proxy, gain, interface, threshold, angular-cutoff, and strict spectral wall",
          "every denominator, radicand, and squaring condition in the self-consistency inequality",
          "the independently reconstructed complete fixed-r=B=14/3 paths, including P=r=B and every intermediate point B<=P'<=P",
          "every monotonicity used to place a worst case at epsilon=1/6 or kappa=54",
          "K=K_0(5/6), K=294^2, K=295^2, K=200000, and every shared global-union face",
          "the kappa=53 displacement failure treated only as a selected-route obstruction, not as a counterexample",
          "the Y=294 central-proxy failure treated only as a selected-route obstruction, not as a lower bound for K_0(5/6)",
          "any inference that an all-frequency endpoint extension follows from the Round 15 seam theorem alone"
        ]
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "The complete small-hole endpoint and its closed rho_* face are unchanged."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "The fixed-rho theorem and formula K_0(rho) are unchanged."
      },
      {
        "id": "SHELL-thin-product-low-optical",
        "reason": "Its historical epsilon<=1/100 theorem is unchanged; Round 16 rederives the needed product estimates on a new domain rather than extending this old obligation."
      },
      {
        "id": "SHELL-thin-action-aggregate",
        "reason": "The Round 6 aggregate theorem is unchanged and was not used in the Round 16 proof."
      },
      {
        "id": "SHELL-ultrathin-intermediate-bridge",
        "reason": "The Round 11 bridge is unchanged and was not used in the Round 16 proof."
      },
      {
        "id": "SHELL-central-thin-seam-compression",
        "reason": "The Round 15 seam theorem is mathematically unchanged; only a stale falsification phrase is qualified to distinguish it from the independent Round 16 endpoint."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "The protected one-box certificate and its provenance are unchanged."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "The residual shrinks to D_16, but it is not closed."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No new Bessel-root region was certified; the executable ledger checks finite analytic algebra only."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The high-frequency ceiling improves, but compact all-frequency closure remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The full theorem remains open on D_16 and still requires final theorem-level audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 8,
    "reason": "Round 16 independently proves the all-frequency endpoint 7/8<=rho<1, removes every far-thin finite residual zone, and lowers the complete all-ratio high-frequency ceiling from 200000 to 295^2=87025 by the exact factor 8000/3481>2. The true nonrectangular compact residual remains open, so the full shell theorem is not claimed."
  }
}

## State boundary after Round 16

The accepted all-frequency endpoint neighborhoods are now

$$
0<\rho\le\rho_*,
\qquad
\frac78\le\rho<1.
$$

For every ratio, the shell inequality is proved when $K\ge295^2=87025$.
The full all-frequency theorem remains open exactly on the nonrectangular
residual $\mathcal D_{16}$. The Round 8 certified pilot remains local, and
COMP-certified-bessel remains diagnostic only. The positive stretch screens
at $\rho=6/7$ and $\rho=23/27$ are not promoted.
