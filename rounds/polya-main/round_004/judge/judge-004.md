# Round 4 Judge: Separated Shell Spectrum

## Verdict

The separated three-dimensional Dirichlet shell spectrum and strict phase-count
bridge are proved.

The frozen incumbent passed an isolated clean-room reconstruction and a
line-by-line adversarial audit. The reviews verified the Hilbert-space and form
decomposition, exact global domains, compactness of the infinite direct sum,
regular radial completeness and simplicity, the Bessel determinant sign and
normalization, exclusion of zero energy, simple positive roots, angular
multiplicity, accidental cross-channel equality, and strict spectral
endpoints.

Combining this bridge with the already-proved Round 3 weighted lattice theorem
promotes the fixed-rho high-energy eigenvalue estimate from conditional to
proved. Precisely, for every fixed \(0<\rho<1\),

$$
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge K_0(\rho)).
$$

This is not the full shell theorem. The residual all-\(K\) parameter region,
uniform control as \(\rho\to0,1\), and interval-certified closure remain open.

The existing general-dimensional cross-product statement is narrowed to
\(d=3\), because that is the theorem reconstructed and reviewed in this
round. A general-\(d\) extension is not silently inferred.

## Evidence gates

- Frozen packet: state/lemma_packets/SHELL-sturm-liouville-completeness.md
- Incumbent: rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md
- Clean-room PASS: rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md
- Adversarial PASS: rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md
- Promotion-scope audit: rounds/polya-main/round_004/reviews/state-promotion-audit.md

## State Patch

{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-sturm-liouville-completeness",
        "status": "proved_internal",
        "statement_tex": "For every fixed 0<rho<1, the Dirichlet Laplacian on A_{rho,1} subset R^3 is unitarily equivalent to the orthogonal sum over ell>=0 and -ell<=m<=ell of L_ell=-d^2/dr^2+ell(ell+1)/r^2 on H^2(rho,1) cap H_0^1(rho,1), with the exact direct-sum form and graph domains. The full resolvent is compact, every radial block has a positive simple complete spectrum, its positive eigenfrequencies are exactly the positive roots of F_{ell+1/2,rho}, and cross-ell coincidences contribute the sum of the orthogonal angular multiplicities.",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md",
            "sources/shell_weyl_bessel.md"
          ]
        },
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity"
        ],
        "falsification_cases": [
          "infinite direct sum and angular multiplicity tail",
          "exact global form and operator domains",
          "ell=0 and k=0",
          "determinant sign and common endpoint zeros",
          "positive-root simplicity",
          "K at one or several eigenfrequencies",
          "accidental equality across distinct ell values"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
        ],
        "reason_for_promotion": "The frozen exact-domain proof passed an isolated clean-room reconstruction and an adversarial audit. Both reviews independently verified the unitary decomposition, form closure, direct-sum compactness tail, regular radial spectrum, determinant normalization, zero-energy exclusion, simple positive roots, multiplicity, cross-channel coincidences, and strict endpoints.",
        "next_action": "Use this result as the discharged structural spectrum theorem. Do not infer rho-uniformity, a finite-window inequality, or numerical certification from it."
      },
      {
        "id": "SHELL-cross-product-formula",
        "status": "proved_internal",
        "statement_tex": "For A_{rho,1} subset R^3, the Dirichlet radial eigenfrequencies in angular channel ell are exactly the positive simple zeros of F_{nu,rho}(k)=J_nu(rho k)Y_nu(k)-Y_nu(rho k)J_nu(k), with nu=ell+1/2. Each channel has spherical-harmonic multiplicity 2ell+1, and multiplicities add when eigenvalues from different ell channels coincide.",
        "blockers_removed": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md",
            "sources/shell_weyl_bessel.md"
          ]
        },
        "reason_for_promotion": "The d=3 determinant criterion, sign normalization, positive-root simplicity, angular multiplicity, and cross-channel multiplicity rule were reconstructed independently and passed adversarial review. The prior general-d wording is narrowed to the proved d=3 scope.",
        "next_action": "Use the exact d=3 determinant in the strict spectral count and certified finite-window design. Create a separate obligation before claiming a general-dimensional extension."
      },
      {
        "id": "SHELL-count-floor-identity",
        "status": "proved_internal",
        "blockers_removed": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
          ]
        },
        "reason_for_promotion": "The proved spectral decomposition, determinant formula, phase representation, and strict monotonicity show that the positive roots are exactly the phase levels n pi for n>=1. The clean-room and adversarial reviews verified the strict endpoint rule and simultaneous cross-channel walls.",
        "next_action": "Use the exact endpoint-safe identity unconditionally in d=3. At Psi(K)=m pi, retain channel count m-1 rather than the ordinary floor m."
      },
      {
        "id": "SHELL-lattice-count",
        "status": "proved_internal",
        "statement_tex": "For every fixed 0<rho<1 and K>=K_0(rho), the exact strict d=3 shell eigenvalue count is bounded by the multiplicity-weighted phase proxy and hence by (2/(9 pi))(1-rho^3)K^3. This statement covers the fixed-rho analytic high-energy range only.",
        "blockers_removed": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
          ]
        },
        "reason_for_promotion": "Round 3 proved the fixed-rho high-energy weighted proxy. Round 4 proves that this proxy is an unconditional upper bound for the exact strict d=3 eigenvalue count, including all multiplicities and spectral endpoints.",
        "next_action": "Treat the fixed-rho high-energy spectral lattice bound as proved. Do not extend it to the finite window or rho endpoints without separate evidence."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "status": "proved_internal",
        "blockers_removed": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
          ]
        },
        "reason_for_promotion": "The sole remaining assumption in the Round 3 fixed-rho theorem was the separated-spectrum and strict-count bridge. Round 4 proves that bridge with independent and adversarial review, so the explicit K_0(rho) eigenvalue estimate is unconditional.",
        "next_action": "Use the explicit K_0(rho) theorem as the analytic high-energy half of the shell program. The finite region and endpoint-uniform closure remain separate obligations."
      },
      {
        "id": "SHELL-exact-phase-rep",
        "next_action": "Use the fixed sign convention in the now-proved d=3 spectral count and in certified root or phase-wall calculations."
      },
      {
        "id": "SHELL-phase-monotonicity",
        "next_action": "Use strict monotonicity for unconditional d=3 root indexing and endpoint-safe phase counts."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "next_action": "Combine this unconditional lattice-proxy inequality with the now-proved strict spectral identity. Do not extrapolate it to the finite window or a rho-uniform theorem."
      },
      {
        "id": "SHELL-thin-width-phase-zero",
        "next_action": "Through the proved strict spectral identity, use (1-rho)K<=pi as an actual zero-eigenvalue-count region, including equality."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "next_action": "The lower optical-width region (1-rho)K<=pi now has zero actual strict shell count. Prove a uniform estimate for widths above pi and overlap it with compact-rho certification."
      },
      {
        "id": "SHELL-rho-compact",
        "blockers_removed": [
          "SHELL-lattice-count",
          "SHELL-fixed-rho-high-energy"
        ],
        "next_action": "Bound K_0(rho) explicitly on each compact rho interval and formulate the remaining bounded interval certificate. COMP-certified-bessel is the remaining blocker."
      },
      {
        "id": "COMP-certified-bessel",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
          ]
        },
        "next_action": "Use the proved determinant spectrum, root simplicity, angular cutoff, and strict endpoint identity to design interval root isolation and wall handling. Retain diagnostic_only until rho-uniformity yields bounded coverage and all certificate artifacts, commands, versions, and hashes exist."
      },
      {
        "id": "TARGET-shell-d3",
        "blockers_removed": [
          "SHELL-lattice-count",
          "SHELL-fixed-rho-high-energy"
        ],
        "evidence_added": {
          "positive": [
            "rounds/polya-main/round_004/judge/judge-004.md"
          ]
        },
        "next_action": "The exact spectral bridge and fixed-rho high-energy theorem are discharged. Prioritize rho-endpoint uniformity and interval-certified closure of the residual finite region; no all-K shell theorem is yet proved."
      },
      {
        "id": "POLYA-program-target",
        "blockers_removed": [
          "SHELL-lattice-count"
        ],
        "next_action": "Keep the program target open until TARGET-shell-d3 passes rho-uniformity, finite certification, and final theorem-level clean-room review."
      },
      {
        "id": "SRC-shell-weyl",
        "evidence_added": {
          "positive": [
            "sources/shell_weyl_bessel.md",
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md",
            "rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md"
          ]
        },
        "next_action": "The structural spectrum component is audited. Audit only the unresolved quantitative Weyl remainder, endpoint-uniform constants, one-sided Polya-strength estimates, and finite-window certification scope."
      }
    ],
    "reject": [
      {
        "id": "distinct-centrifugal-potentials-preclude-cross-ell-degeneracy",
        "reason": "Reject the assertion that different centrifugal potentials prohibit equality across angular channels. The Round 4 incumbent and adversarial review prove by continuity that lambda_{0,2}(rho)=lambda_{7,1}(rho) for at least one rho in (1/10,4/5). Orthogonal direct-sum multiplicities add at such coincidences."
      },
      {
        "id": "blockwise-compact-resolvent-implies-compact-infinite-direct-sum",
        "reason": "Reject compactness of every radial block as sufficient for compactness of the infinite direct sum. The shell proof also needs the angular-tail estimate ||(L_ell+1)^{-1}|| -> 0, obtained from L_ell>=ell(ell+1)."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-rho-uniformity",
        "reason": "The endpoint-uniform covering remains open."
      },
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "The small-hole endpoint and its certified overlap remain open."
      },
      {
        "id": "SHELL-low-interface-shifted-tails",
        "reason": "The unrestricted all-K strengthening remains open; only its fixed-rho high-energy substitute is proved."
      },
      {
        "id": "SHELL-spherical-bessel-algebraic",
        "reason": "Round 4 does not construct the exact algebraic interval-arithmetic representation needed for certification."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "reason": "The exact d=3 separated spectrum and strict phase count pass all review gates, making the fixed-rho high-energy shell Polya estimate unconditional. The all-K, rho-uniform, and certified theorem remains open."
  }
}

## State boundary after Round 4

The strongest proved theorem is the fixed-\(\rho\) high-energy estimate above.
The strongest forbidden claim remains the all-\(K\), all-\(\rho\) shell
theorem.
