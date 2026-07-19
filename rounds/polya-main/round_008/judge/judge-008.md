# Round 8 Judge: Compact Analytic Envelope and Certified Pilot

## Verdict

Round 8 proves a uniform analytic high-energy envelope on the complete
remaining compact ratio interval and produces the first independently
checked interval certificate on a genuine residual box.

It does **not** close `SHELL-rho-compact`, `COMP-certified-bessel`, or the
global shell theorem.

Let

$$
I_*=[\rho_*,1-2^{-18}],
\qquad
\rho_*=\frac{\omega_0}{1+2C_*},
$$

where

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15}.
$$

Then Round 8 proves

$$
\boxed{
\rho\in I_*,\quad K\ge2^{42}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

The proof is the exact union of three analytic zones.

1. For $\rho_*\le\rho\le1/16$, the only possible gap lies between

   $$
   \frac1{2\rho}
   \quad\hbox{and}\quad
   H_0(\rho)=\frac{C_*}{\omega_0-\rho},
   $$

   and $H_0(1/16)<64$.
2. For $1/16\le\rho\le99/100$, the only possible gap lies between

   $$
   \frac\pi{1-\rho}
   \quad\hbox{and}\quad K_0(\rho).
   $$

   The positive-root formula defining $K_0$ is increasing in $\rho$, and

   $$
   K_0(99/100)<180000^2<2^{35}.
   $$
3. With $\varepsilon=1-\rho$ and
   $2^{-18}\le\varepsilon\le1/100$, the proved thin estimates cover

   $$
   K\le L(\varepsilon)=\frac1{8\varepsilon^{5/2}}
   \quad\hbox{and}\quad
   K\ge U(\varepsilon)=\frac{64}{\varepsilon^2}.
   $$

   At $\varepsilon=2^{-18}$,

   $$
   L(2^{-18})=U(2^{-18})=2^{42}.
   $$

All analytic threshold equalities are included.  The two endpoint ratio
faces are already completely analytic.

## Exact certificate target

The closed union

$$
\mathcal E=\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T
$$

is a bounded planning envelope, not the literal unproved set.  If
$\mathcal A$ is the union of all permitted analytic regions, the true
certificate target is

$$
\mathcal D=
\bigl(I_*\times[0,\infty)\bigr)\setminus\mathcal A,
\qquad
\mathcal D\subseteq\mathcal E.
$$

The first adversarial pass identified a contradiction between numerically
certifying every point of the closed over-cover and excluding already
analytic faces.  The packet was corrected to distinguish $\mathcal E$ from
$\mathcal D$, assign analytic masks and face owners, and require the exact
cover equation

$$
\mathcal E\setminus
\bigl(\mathcal A\cup\text{certified boxes}\bigr)=\varnothing.
\tag{2}
$$

Both clean-room and adversarial reviewers re-audited this correction and
returned PASS.

The corrected format permits either exact wall subdivision or a proved
monotone corner majorant.  For

$$
B=[\rho_-,\rho_+]\times[K_-,K_+],
$$

the safe corner mechanism is

$$
N_D(A_{\rho,1},K^2)
\le
\#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}=:C_B
$$

and

$$
\frac{2}{9\pi}(1-\rho^3)K^3
\ge
\frac{2}{9\pi}(1-\rho_+^3)K_-^3=:W_B.
$$

Thus $C_B\le W_B$ proves the complete closed box, absorbing every internal
spectral and angular wall.  The non-strict upper-corner count safely includes
a possible eigenvalue on the upper frequency face.

## Certified central pilot

The interval producer and independent rational checker certify

$$
\boxed{
\frac{999}{2000}\le\rho\le\frac{1001}{2000},
\qquad
\frac{67}{10}\le K\le\frac{168}{25}.
}
\tag{3}
$$

The entire closed box lies strictly inside the central residual region.
Outward-rounded Arb recurrence proves uniform determinant sign changes in

$$
\ell=0: \left[\frac{31}{5},\frac{63}{10}\right],
\qquad
\ell=1: \left[\frac{13}{2},\frac{33}{5}\right].
$$

The independent checker imports neither Arb nor the producer.  It
reconstructs

$$
R_0(\rho,k)=\sin((1-\rho)k)
$$

and

$$
R_1(\rho,k)=
\left(1+\frac1{\rho k^2}\right)\sin((1-\rho)k)
-\frac{1-\rho}{\rho k}\cos((1-\rho)k)
$$

with exact `Fraction` arithmetic, a Machin enclosure of $\pi$, and
alternating Taylor remainders.  The Poincare--Sturm bound

$$
\lambda_{n,\ell}
\ge\left(\frac{n\pi}{1-\rho}\right)^2+\ell(\ell+1)
$$

proves that the two displayed channels contain at most one root and that
every $\ell\ge2$ channel is empty.  Hence the exact strict count is

$$
N_D(A_{\rho,1},K^2)=1+3=4
$$

throughout (3).  The independently certified Weyl lower bound is

$$
18.60731553544245607556\ldots,
$$

giving margin greater than
$14.60731553544245607556$.

The checker reconstructs the exact endpoints, verifies current SHA-256
hashes of the producer, itself, and the frozen packet, and rejects count,
sign, and provenance-hash tampering.
This is a certified local result, not a certificate of the full compact
region.

## Feasibility boundary

Boundedness alone is not a scalable computation plan.  At the exact slice
$\varepsilon=2^{-17}$, the current thin planning envelope has width

$$
2^{39}(2-\sqrt2)>2^{38}+1,
$$

so literal subdivision crosses more than $2^{38}$ angular half-integer
walls before determinant walls are considered.  The corrected monotone-box
format removes the requirement to split those walls, but computing or
aggregating the high-frequency corner spectrum is still open.

The next round must sharpen the central and thin analytic envelopes or prove
a symbolic/aggregate certified count.  Scaling the low-channel pilot by raw
enumeration is rejected.

## Evidence gates

- Corrected compact packet:
  `state/lemma_packets/SHELL-rho-compact.md`
- Incumbent analytic proof:
  `rounds/polya-main/round_008/responses/compact-envelope-incumbent.md`
- Clean-room reconstruction and post-correction audit:
  `rounds/polya-main/round_008/reviews/compact-envelope-clean-room.md`
- Adversarial audit and post-correction verdict:
  `rounds/polya-main/round_008/reviews/compact-envelope-adversarial.md`
- Exact cover design:
  `rounds/polya-main/round_008/exploration/certificate-cover-design.md`
- Certificate schema and pilot report:
  `rounds/polya-main/round_008/certification/certificate-design.md`,
  `rounds/polya-main/round_008/certification/pilot-report.md`
- Machine-readable certificate and independent PASS report:
  `rounds/polya-main/round_008/certification/pilot-central-box.json`,
  `rounds/polya-main/round_008/certification/pilot-central-box-check.json`
- Independent final pilot audit:
  `rounds/polya-main/round_008/reviews/certified-pilot-independent-audit.md`

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Explicit analytic envelope on the remaining compact shell-ratio interval",
        "status": "proved_internal",
        "statement_tex": "Let rho_*=omega_0/(1+2 C_*) and I_*=[rho_*,1-2^(-18)]. On [rho_*,1/16], the possible residual lies between 1/(2 rho) and C_*/(omega_0-rho) and has K<64. On [1/16,99/100], it lies between pi/(1-rho) and K_0(rho) and has K<2^35. On [99/100,1-2^(-18)], with epsilon=1-rho, it lies between 1/(8 epsilon^(5/2)) and 64/epsilon^2 and has K<=2^42. Consequently the strict shell Polya inequality holds for every rho in I_* and K>=2^42.",
        "dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high"
        ],
        "implies": [
          "SHELL-rho-compact"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact.md",
            "rounds/polya-main/round_008/responses/compact-envelope-incumbent.md",
            "rounds/polya-main/round_008/reviews/compact-envelope-clean-room.md",
            "rounds/polya-main/round_008/reviews/compact-envelope-adversarial.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint",
          "SHELL-high-angular-shifted-tails",
          "SHELL-low-interface-small-hole",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy",
          "SHELL-thin-product-low-optical",
          "SHELL-thin-action-aggregate",
          "SHELL-thin-local-plateau-high"
        ],
        "falsification_cases": [
          "rho=rho_*",
          "rho=1/16",
          "rho=1/2",
          "rho=99/100",
          "rho=1-2^(-18)",
          "K equal to every component threshold",
          "L(2^(-18))=U(2^(-18))",
          "closed planning envelope confused with the true certification target"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_008/reviews/compact-envelope-clean-room.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_008/reviews/compact-envelope-adversarial.md"
        ],
        "reason_for_promotion": "The three exact zones cover the complete compact ratio interval, all endpoint and threshold equalities were independently reconstructed, K_0 monotonicity was checked, and the corrected E/D cover specification passed post-correction clean-room and adversarial audits.",
        "next_action": "Use this envelope as the analytic boundary for compact certification. Improve the central and thin thresholds before attempting a full exact cover."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "type": "computation",
        "track": "certified_computation",
        "title": "Independently checked shell-determinant certificate on one central residual box",
        "status": "certified",
        "statement_tex": "For every rho in [999/2000,1001/2000] and K in [67/10,168/25], the exact strict shell count is N_D(A_{rho,1},K^2)=4 and is strictly smaller than (2/(9 pi))(1-rho^3)K^3; the certified Weyl margin exceeds 14.607315535442456.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-cross-product-formula",
          "SHELL-sturm-liouville-completeness",
          "SHELL-angular-cutoff",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy"
        ],
        "implies": [
          "COMP-certified-bessel"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/polya-main/round_008/certification/pilot-report.md",
            "rounds/polya-main/round_008/certification/pilot-central-box.json",
            "rounds/polya-main/round_008/certification/pilot-central-box-check.json",
            "rounds/polya-main/round_008/reviews/certified-pilot-independent-audit.md",
            "computations/round8_compact_box_certificate.py",
            "computations/round8_verify_compact_box_certificate.py",
            "computations/tests/test_round8_compact_box_certificate.py"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "criticality": "standard",
        "lead_author": "A4",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A2",
        "review_independence": "independent",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-cross-product-formula",
          "SHELL-sturm-liouville-completeness",
          "SHELL-angular-cutoff",
          "SHELL-thin-width-zero-count",
          "SHELL-fixed-rho-high-energy"
        ],
        "falsification_cases": [
          "rho and K on every closed pilot face",
          "ell=0 determinant root on a bracket face",
          "ell=1 determinant root on a bracket face",
          "ell=2 first radial level below K",
          "second radial root below K",
          "angular cutoff at ell+1/2=K",
          "tampered count, determinant sign, or provenance hash"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_008/reviews/certified-pilot-independent-audit.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_008/reviews/certified-pilot-independent-audit.md"
        ],
        "evidence_class": "interval_certified",
        "software_version": "python-flint 0.8.0 Arb producer; Python standard-library Fraction independent checker",
        "reproduction_command": "python computations/round8_compact_box_certificate.py --output rounds/polya-main/round_008/certification/pilot-central-box.json && python computations/round8_verify_compact_box_certificate.py --input rounds/polya-main/round_008/certification/pilot-central-box.json --report rounds/polya-main/round_008/certification/pilot-central-box-check.json",
        "coverage_statement": "Exactly the closed box rho in [999/2000,1001/2000], K in [67/10,168/25]; no other compact residual point is claimed.",
        "artifact_hashes": {
          "producer": "8902a0fd4ff7db4b1443ca02326151d4d6e4b9b92b697c68220eb85454c4ec7e",
          "independent_checker": "2ab1a31d8a22c6f1d5f7def2e33d2e3f0fb710fdb5cae50f8389d82f5b0475d5",
          "frozen_packet": "8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7",
          "certificate": "f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00"
        },
        "certification_artifacts": [
          "rounds/polya-main/round_008/certification/pilot-central-box.json",
          "rounds/polya-main/round_008/certification/pilot-central-box-check.json",
          "rounds/polya-main/round_008/certification/pilot-report.md"
        ],
        "reason_for_promotion": "Arb outward-rounded determinant signs, exact Sturm truncation, strict multiplicity counting, and the Weyl margin are all independently reconstructed by a checker sharing no producer or Flint code; current provenance hashes and tamper rejection pass.",
        "next_action": "Use this only as a validated schema and local pilot. Extend through an exact face-connected manifest only after analytic compression makes the remaining corner spectra tractable."
      }
    ],
    "update": [
      {
        "id": "SHELL-rho-compact",
        "dependencies_added": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact.md",
            "rounds/polya-main/round_008/responses/compact-envelope-incumbent.md",
            "rounds/polya-main/round_008/reviews/compact-envelope-clean-room.md",
            "rounds/polya-main/round_008/reviews/compact-envelope-adversarial.md",
            "rounds/polya-main/round_008/certification/pilot-report.md"
          ]
        },
        "next_action": "The analytic envelope is proved and one central box is certified. Keep this obligation open until an exact manifest covers D; first compress the central and thin high-frequency corner spectra rather than enumerating the present 2^35/2^42 bounds."
      },
      {
        "id": "COMP-certified-bessel",
        "dependencies_added": [
          "COMP-certified-bessel-pilot-round8"
        ],
        "evidence_added": {
          "positive": [
            "rounds/polya-main/round_008/certification/certificate-design.md",
            "rounds/polya-main/round_008/certification/pilot-report.md",
            "rounds/polya-main/round_008/certification/pilot-central-box.json",
            "rounds/polya-main/round_008/certification/pilot-central-box-check.json",
            "rounds/polya-main/round_008/reviews/certified-pilot-independent-audit.md"
          ]
        },
        "certification_artifacts_added": [
          "rounds/polya-main/round_008/certification/pilot-central-box.json",
          "rounds/polya-main/round_008/certification/pilot-central-box-check.json"
        ],
        "next_action": "The local Arb/Fraction pipeline is validated, but the parent remains diagnostic_only. Build an exact E-minus-A cover manifest only after a symbolic or analytic aggregation reduces the high-frequency central and thin corner counts."
      },
      {
        "id": "SHELL-rho-uniformity",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact.md",
            "rounds/polya-main/round_008/responses/compact-envelope-incumbent.md"
          ]
        },
        "next_action": "Both endpoints and the compact high-energy envelope are proved. The sole remaining blocker is exact certified coverage of the true compact residual D."
      },
      {
        "id": "TARGET-shell-d3",
        "evidence_added": {
          "positive": [
            "rounds/polya-main/round_008/responses/compact-envelope-incumbent.md",
            "rounds/polya-main/round_008/certification/pilot-report.md"
          ]
        },
        "next_action": "The theorem is analytic above K=2^42 on the remaining compact ratio interval and one residual box is certified. Complete the exact compact cover, then run final theorem-level clean-room and adversarial audits."
      }
    ],
    "reject": [
      {
        "id": "literal-wall-enumeration-closes-round8-compact-envelope",
        "reason": "Reject raw wall-by-wall certification of the present coarse envelope as a scalable route. At epsilon=2^(-17), one thin residual slice alone crosses more than 2^38 angular half-integer walls; a symbolic, monotone, or analytic aggregation is required."
      }
    ],
    "no_change": [
      {
        "id": "SHELL-rho-compact",
        "reason": "The high-energy envelope and one local box are proved, but the true residual D is not covered."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "One independently checked pilot does not certify the full compact residual family."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "Compact certified closure remains open."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "Most compact residual points and the final theorem audit remain open."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "reason": "Round 8 proves a finite piecewise analytic envelope with uniform threshold 2^42, repairs the exact certificate-domain specification under independent review, and validates the first genuine residual shell-determinant box with independent arithmetic. The compact theorem remains open because the full residual is not covered and the coarse high-frequency families are not computationally scalable."
  }
}

## State boundary after Round 8

The complete shell inequality is analytically proved in both endpoint
neighborhoods and, on the remaining compact interval, for every
$K\ge2^{42}$.  One closed central residual box is interval-certified with an
independent checker.

The global theorem remains open on the rest of $\mathcal D$.  The next
mathematical bottleneck is scalable aggregation of the central and thin
corner spectra, followed by an exact cover manifest and final theorem audit.
