# Round 7 Judge: Analytic Closure of the Small-Hole Endpoint

## Verdict

Round 7 closes the complete $\rho\downarrow0$ endpoint analytically.

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
$$

and define

$$
\boxed{
\rho_*=
\frac{\omega_0}{1+2C_*}
=
\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}
=0.0310668242700667\ldots .
}
$$

Then, for every $0<\rho\le\rho_*$ and every $K\ge0$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

No ball-limit argument or Bessel-root certificate is needed.

The proof uses the exact inner scale $\mu=\rho K$.

1. If $\mu\le1/2$, every shifted-tail start is at least $1/2$ and hence
   lies at or above the inner interface. The already-proved convex
   high-angular tail theorem controls every tail.
2. If $\mu>1/2$, then $K>1/(2\rho)$. For $\rho\le\rho_*$,

   $$
   K(\omega_0-\rho)
   >\frac{\omega_0-\rho}{2\rho}
   \ge C_*,
   $$

   so the independently reviewed small-hole low-interface theorem controls
   every tail below the interface, while the high-angular theorem controls
   the rest.

The two regimes meet exactly because

$$
\frac{C_*}{\omega_0-\rho}
\le\frac1{2\rho}
\quad\Longleftrightarrow\quad
\rho\le\rho_*.
$$

At $\rho=\rho_*$ the joining frequency is

$$
K_*=\frac1{2\rho_*}
=16.0943389531371\ldots,
$$

and both component ranges include equality. The weighted scaffold and exact
strict spectral bridge then give the stated shell inequality.

## Evidence gates

- Frozen packet:
  `state/lemma_packets/SHELL-rho-zero-endpoint.md`
- Frozen incumbent:
  `rounds/polya-main/round_007/responses/small-hole-incumbent.md`
- Isolated clean-room reconstruction:
  `rounds/polya-main/round_007/reviews/small-hole-clean-room.md`
- Independent adversarial constants, walls, and route audit:
  `rounds/polya-main/round_007/reviews/small-hole-adversarial.md`
- Final dependency and integration audit:
  `rounds/polya-main/round_007/reviews/small-hole-integrated-audit.md`
- Previously frozen low-interface theorem and reviews:
  `state/lemma_packets/SHELL-low-interface-small-hole.md`,
  `rounds/polya-main/round_003/responses/low-interface-small-hole-incumbent.md`,
  `rounds/polya-main/round_003/reviews/low-interface-small-hole-clean-room.md`,
  and
  `rounds/polya-main/round_003/reviews/low-interface-small-hole-adversarial.md`

The clean-room and adversarial reports verify $K=0$, the exact endpoint
$\rho=\rho_*$, the interface wall $\mu=1/2$, $x_r=\mu$, the inclusive
high-energy threshold, strict phase/eigenvalue walls, and ordinary-floor
proxy walls. They also show that the apparent small-hole certification box is
empty.

## Rejected shortcuts

Pointwise convergence of shell roots to ball roots is not uniform in the
radial index. Bare domain monotonicity loses the factor $1-\rho^3$, and
subtracting two ball Pólya bounds would require monotonicity of the ball Weyl
deficit, which fails across spectral jumps. None of these shortcuts is used.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-low-interface-small-hole",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Uniform low-interface shifted tails in the small-hole sector",
        "status": "proved_internal",
        "statement_tex": "Let omega_0=sqrt(3)/(2 pi)-1/6 and C_*=1/2+8 sqrt(2)/15. If 0<rho<omega_0, K(omega_0-rho)>=C_*, and x_r=r+1/2<rho K, then the ordinary-floor shifted tail T_r of A_{rho,K}+1/4 satisfies T_r<=2 int_{x_r}^K A_{rho,K}(z) dz.",
        "dependencies": [
          "SHELL-weighted-lattice-scaffold",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "implies": [
          "SHELL-rho-zero-endpoint"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-low-interface-small-hole.md",
            "rounds/polya-main/round_003/responses/low-interface-small-hole-incumbent.md",
            "rounds/polya-main/round_003/reviews/low-interface-small-hole-clean-room.md",
            "rounds/polya-main/round_003/reviews/low-interface-small-hole-adversarial.md",
            "rounds/polya-main/round_007/reviews/small-hole-clean-room.md",
            "rounds/polya-main/round_007/reviews/small-hole-adversarial.md"
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
          "SHELL-weighted-lattice-scaffold",
          "SRC-annuli",
          "SRC-FLPS-balls"
        ],
        "falsification_cases": [
          "n=0 with no concave block",
          "q=rho K at the inner interface",
          "rho K immediately above a half-integer",
          "rho K immediately below the next half-integer",
          "K(omega_0-rho)=C_*",
          "ordinary-floor integer walls"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_003/reviews/low-interface-small-hole-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_003/reviews/low-interface-small-hole-adversarial.md"
        ],
        "reason_for_promotion": "The frozen Round 3 proof passed an isolated reconstruction and a separate adversarial audit of the split weights, n=0 branch, interface loss, improved convex margin, exact threshold, and every floor wall. Round 7 re-audited this theorem as the low-interface input to the endpoint proof.",
        "next_action": "Use this theorem with the high-angular shifted-tail theorem. Do not replace it by pointwise convergence to ball roots."
      }
    ],
    "update": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "status": "proved_internal",
        "statement_tex": "Let omega_0=sqrt(3)/(2 pi)-1/6, C_*=1/2+8 sqrt(2)/15, and rho_*=omega_0/(1+2 C_*). For every 0<rho<=rho_* and every K>=0, the strict shell count satisfies N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. The endpoint rho=rho_* is included; rho=0 is not part of the domain family.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole"
        ],
        "blockers": [],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-zero-endpoint.md",
            "rounds/polya-main/round_007/responses/small-hole-incumbent.md",
            "rounds/polya-main/round_007/reviews/small-hole-clean-room.md",
            "rounds/polya-main/round_007/reviews/small-hole-adversarial.md",
            "rounds/polya-main/round_007/reviews/small-hole-integrated-audit.md"
          ]
        },
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-scaffold",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole"
        ],
        "falsification_cases": [
          "K=0",
          "rho=rho_*",
          "rho K=1/2",
          "x_r=rho K",
          "K(omega_0-rho)=C_*",
          "strict phase and eigenvalue walls",
          "ordinary-floor action walls",
          "nonuniformity of pointwise ball-root convergence"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_007/reviews/small-hole-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_007/reviews/small-hole-adversarial.md",
          "rounds/polya-main/round_007/reviews/small-hole-integrated-audit.md"
        ],
        "reason_for_promotion": "The exact split at rho K=1/2 leaves no finite residual: below it every shifted tail is already high-angular, while above it rho<=rho_* forces the reviewed small-hole threshold. The all-K proof passed isolated clean-room, adversarial constants/wall, and final dependency audits and uses no computation.",
        "next_action": "Treat the small-hole endpoint as discharged. Begin the compact-rho residual interval at the inclusive endpoint rho=rho_*; no small-hole certificate is needed."
      },
      {
        "id": "SHELL-rho-uniformity",
        "blockers_removed": [
          "SHELL-rho-zero-endpoint"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-zero-endpoint.md",
            "rounds/polya-main/round_007/responses/small-hole-incumbent.md",
            "rounds/polya-main/round_007/reviews/small-hole-integrated-audit.md"
          ]
        },
        "next_action": "Both rho endpoints are discharged. Close SHELL-rho-compact on [rho_*,1-2^(-18)], then assemble the all-rho theorem."
      },
      {
        "id": "SHELL-rho-compact",
        "next_action": "Use the explicit compact interval [rho_*,1-2^(-18)], where rho_*=omega_0/(1+2 C_*). Make the analytic high-energy threshold uniform and certify only the resulting bounded residual window, with inclusive overlap at both endpoints."
      },
      {
        "id": "COMP-certified-bessel",
        "next_action": "Neither endpoint needs certification. Restrict interval certification to the bounded residual window on rho in [rho_*,1-2^(-18)], preserving every determinant, phase, angular, floor, and strict spectral wall."
      },
      {
        "id": "TARGET-shell-d3",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-zero-endpoint.md",
            "rounds/polya-main/round_007/responses/small-hole-incumbent.md"
          ]
        },
        "next_action": "The exact spectrum, fixed-rho high energy, and both rho endpoints are proved. The remaining theorem blocker is compact-rho bounded closure with certified computation, followed by a final theorem audit."
      }
    ],
    "reject": [
      {
        "id": "pointwise-ball-root-convergence-proves-uniform-small-hole-endpoint",
        "reason": "Reject upgrading fixed-index shell-to-ball root convergence to an all-K uniform theorem. Already for ell=0, k_{n,0}(rho)-n pi=n pi rho/(1-rho), which is not uniform in the radial index n."
      },
      {
        "id": "domain-monotonicity-plus-ball-polya-pays-shell-volume",
        "reason": "Reject the bare implication N_shell<=N_ball<(2/(9 pi))K^3 as a proof of the smaller shell target. It does not pay the missing cubic amount (2/(9 pi))(rho K)^3."
      },
      {
        "id": "subtract-two-ball-polya-bounds-to-prove-shell",
        "reason": "Reject subtracting one-sided ball Polya inequalities. It would require monotonicity of the ball Weyl deficit across spectral jumps; an interval crossing the first ball frequency gives a ball-count jump of one while its Weyl-volume difference is strictly less than one."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-rho-compact",
        "reason": "Round 7 proves the small-hole endpoint but does not close the intervening compact-rho finite window."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "No interval-certified compact-rho computation was produced."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "Both endpoints are proved, but compact-rho closure remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "The small-hole endpoint is now proved, but compact-rho closure and the final theorem audit remain open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "An exact overlap of two already-reviewed shifted-tail regimes proves the complete rho-to-zero endpoint for all frequencies with an explicit endpoint rho_*. This removes the second analytic endpoint bottleneck and leaves only compact-rho bounded closure and the final shell theorem audit."
  }
}

## State boundary after Round 7

The shell theorem is unconditional for every

$$
0<\rho\le\rho_*
$$

and for every

$$
1-2^{-18}\le\rho<1,
$$

at all frequencies $K\ge0$. The global theorem remains open only on the
explicit compact interval

$$
\rho_*\le\rho\le1-2^{-18},
$$

where a uniform analytic threshold, bounded certification, and the final
theorem-level audit are still required.
