Exit code: 0
Wall time: 0.2 seconds
Output:
# Round 22 Final Theorem and Program Judge — Provenance Replacement

Date: 2026-07-15

## Supersession and repaired provenance

This replacement preserves the first judge and its failed audit as negative
chronology. The first combined program-scope report, SHA-256
`d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5`, correctly passed the mathematics but incorrectly described
the hash-matching geometry referee as having 299 physical lines. The exact
file has 13,290 bytes, 300 LF bytes, a terminal LF, 300 lines under
`ReadAllLines`, and last numbered line 300 under `rg -n`; PowerShell
`Get-Content` alone returned the misleading count 299.

The independent replacement scope audit is
`rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md`, SHA-256
`0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2`. It reauthenticated every theorem and geometry input without
reading either judge and returned PASS with first unsupported implication
none. The first judge, SHA-256 `a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576`, was never applied. Its
independent FAIL report, SHA-256 `b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573`, found only the line
metadata defect and confirmed that the mathematics and simulated graph delta
otherwise passed. The authoritative graph therefore remains at the unchanged
60-node baseline before this replacement patch.

## Decision

**PASS. First unsupported implication: none.**

This decision closes the internal shell program target, not the general P贸lya
conjecture. The proved class is the complete family of genuine bounded
three-dimensional spherical shells

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R.
$$

For the strict Dirichlet count

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

the reviewed theorem proves

$$
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad \Lambda\ge0,
$$

where $L_3=1/(6\pi^2)$. A separate reviewed geometric theorem proves that
no member of the same class tiles $\mathbb R^3$ by congruent rigid-motion
copies with pairwise-disjoint interiors and exact or almost-everywhere
coverage; the conclusion also covers the corresponding closed-copy
formulations after removal of the countable null boundary union.

The word `new` in the historical program target is read only as newly
completed within this project. This judge makes no claim of literature
novelty, priority, first proof, or readiness for publication.

## Theorem assembly

The unit-shell proof uses the exact disjoint ratio partition

$$
(0,1)=(0,\rho_*]\mathbin{\dot\cup}(\rho_*,7/8)
\mathbin{\dot\cup}[7/8,1).
$$

The small-hole theorem owns $\rho=\rho_*$, the thin-shell theorem owns
$\rho=7/8$, and the complete compact-middle envelope owns the open interval
between them. The Round 21 closure gives the exact successor residual
$\mathcal D_{21}=\varnothing$. Its finite/analytic boundary remains fixed:
10,580 compact leaves certify only
$[7/51,39/50]\times[12,200]$; 1,286 aggregate boxes certify only base
predicates at $K=200$; and the universal $K\ge200$ tail is analytic. The
compact subtraction owns the shared $K=200$ face.

The theorem reviews independently checked $K=0$, every inherited ratio and
frequency seam, strict phase and eigenvalue walls, angular multiplicity,
the normalization

$$
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3),
$$

and the dilation identity

$$
N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda).
$$

The direct use of `SHELL-sturm-liouville-completeness` for spectral
positivity at $K=0$ is made explicit in the patch rather than hidden behind
the cross-product theorem.

## Independent evidence

The authenticated theorem lifecycle is:

- frozen packet `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228`;
- claim freeze `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d`;
- claim-scope audit `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6`;
- incumbent proof `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b`;
- isolated clean-room proof `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12`;
- assembly/provenance audit `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56`;
- cross-comparison `6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458`;
- fresh adversarial referee `a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9`.

The authenticated geometry lifecycle is:

- frozen packet `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f`;
- claim freeze `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a`;
- claim-scope audit `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7`;
- incumbent route `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca`;
- isolated clean-room proof `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6`;
- typography-only addendum `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55`;
- fresh adversarial referee `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53`.

The fresh combined program-scope audit has SHA-256
`0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2`.
It verifies that the spectral and geometric results quantify over literally
the same $0<r<R$ class and that no literature inference enters the proof.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-spherical-shell-nontiling",
        "type": "theorem",
        "track": "target_conventions",
        "title": "Three-dimensional spherical shells do not tile Euclidean space",
        "status": "proved_internal",
        "statement_tex": "For every 0<r<R, the open spherical shell A_{r,R}={x in R^3:r<|x|<R} admits no tiling of R^3 by congruent rigid-motion copies with pairwise-disjoint interiors and either exact or almost-everywhere coverage. The same conclusion holds when coverage is formulated using the closed copies, after the countable null boundary union is removed.",
        "dependencies": [],
        "implies": [
          "POLYA-program-target"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md",
            "rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md",
            "rounds/polya-main/round_022/reviews/nontiling-claim-scope-audit.md",
            "rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md",
            "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md",
            "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md",
            "rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md",
            "rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md"
          ],
          "negative": [
            "rounds/polya-main/round_022/reviews/program-target-scope-audit.md"
          ],
          "inconclusive": [
            "rounds/polya-main/round_021/exploration/literature-scope-note.md"
          ]
        },
        "owner": "A1",
        "criticality": "theorem",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies": [],
        "falsification_cases": [
          "an initially uncountable indexed family or accumulating centers",
          "coverage supplied only by tile boundaries",
          "almost-everywhere rather than exact coverage",
          "closed-copy coverage",
          "duplicate centers or orientation-reversing rigid motions",
          "a limit point lying in the neighboring shell interior",
          "tangent or coincident neighboring boundary spheres",
          "the excluded endpoints r=0 or r=R",
          "scaling with R<1 as well as R>1"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md",
          "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "packet": "d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f",
          "freeze": "c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a",
          "scope_audit": "96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7",
          "incumbent": "67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca",
          "clean_room": "6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6",
          "typography_addendum": "8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55",
          "adversarial_referee": "bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53",
          "program_scope_audit": "0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2",
          "superseded_program_scope_audit": "d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5",
          "failed_first_judge": "a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576",
          "failed_first_state_patch_audit": "b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573"
        },
        "reason_for_promotion": "The exact frozen geometry claim passed an independent scope audit, an isolated clean-room proof, and a fresh adversarial reconstruction covering local finiteness, countability, boundary removal, fixed-neighbor extraction, the finite sphere-cover contradiction, coincident-sphere cases, and scaling.",
        "next_action": "Use this theorem only as the geometric dependency of POLYA-program-target. Do not infer a spectral inequality, literature novelty, priority, or a claim about another domain family from it."
      }
    ],
    "update": [
      {
        "id": "SHELL-phase-enclosures",
        "implies_added": [
          "SHELL-rho-compact"
        ]
      },
      {
        "id": "SHELL-lattice-count",
        "implies_added": [
          "SHELL-rho-compact"
        ]
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "implies_added": [
          "SHELL-rho-compact"
        ],
        "next_action": "Retain this theorem as the discharged fixed-ratio high-frequency input to the completed compact and shell theorems; do not broaden its own threshold or ratio scope."
      },
      {
        "id": "SHELL-sturm-liouville-completeness",
        "implies_added": [
          "TARGET-shell-d3"
        ]
      },
      {
        "id": "SHELL-rho-zero-endpoint",
        "next_action": "Retain this theorem as the completed small-hole owner on 0<rho<=rho_*, including the rho=rho_* seam."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "next_action": "Retain this theorem as the completed thin-shell owner on 7/8<=rho<1, including the rho=7/8 seam."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "next_action": "Retain the complete accepted compact-middle cover with D21 empty as the discharged analytic input to SHELL-rho-compact. Preserve every finite/analytic evidence boundary."
      },
      {
        "id": "SHELL-exact-d20-closure",
        "next_action": "Retain the exact D20 split and empty D21 conclusion with K=200 compact-owned. Do not broaden either finite certificate or reuse superseded evidence."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "proved_internal",
        "statement_tex": "For rho_*<rho<7/8 and every K>0, the complete accepted compact-middle cover through the exact empty residual D21 proves N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3. Every inherited seam and strict spectral or phase wall retains its proved owner.",
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies_added": [
          "SHELL-phase-enclosures",
          "SHELL-lattice-count",
          "SHELL-fixed-rho-high-energy",
          "SHELL-rho-compact-analytic-envelope"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/TARGET-shell-d3-round22-theorem.md",
            "rounds/polya-main/round_022/exploration/theorem-claim-freeze.md",
            "rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md",
            "rounds/polya-main/round_022/responses/shell-theorem-incumbent.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
          ]
        },
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
        ],
        "falsification_cases_added": [
          "rho_* or 7/8 assigned to the compact-middle owner",
          "K=0 inferred from a positive-frequency compact argument",
          "a historical residual substituted for exact empty D21",
          "finite compact or K=200 aggregate evidence used outside its certified scope"
        ],
        "reason_for_promotion": "The complete compact-middle cover has exact empty successor residual D21, and the isolated theorem reconstruction, assembly audit, cross-comparison, and fresh adversarial referee independently verified every inherited seam, strict wall, and finite-versus-analytic boundary.",
        "next_action": "Use this as the discharged positive-frequency compact-middle theorem. Preserve the exact seam owners and certificate scopes; no compact residual remains."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "proved_internal",
        "statement_tex": "For every 0<rho<1 and K>0, the small-hole theorem on 0<rho<=rho_*, the compact-middle theorem on rho_*<rho<7/8, and the thin-shell theorem on 7/8<=rho<1 form an exact disjoint cover and prove N_D(A_{rho,1},K^2)<=(2/(9 pi))(1-rho^3)K^3.",
        "blockers_removed": [
          "SHELL-rho-compact"
        ],
        "criticality": "bottleneck",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "permitted_dependencies_added": [
          "SHELL-rho-compact",
          "SHELL-rho-zero-endpoint",
          "SHELL-rho-one-endpoint"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/TARGET-shell-d3-round22-theorem.md",
            "rounds/polya-main/round_022/exploration/theorem-claim-freeze.md",
            "rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md",
            "rounds/polya-main/round_022/responses/shell-theorem-incumbent.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
          ]
        },
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
        ],
        "falsification_cases_added": [
          "rho=rho_* omitted or owned twice",
          "rho=7/8 omitted or owned twice",
          "the compact-middle open interval replaced by a closed interval",
          "K=0 silently absorbed into a positive-frequency theorem"
        ],
        "reason_for_promotion": "The two promoted endpoint theorems and the newly promoted compact-middle theorem give an exact disjoint ratio partition for every positive frequency, and the theorem-level clean-room and adversarial audits found no seam or uniformity gap.",
        "next_action": "Use this as the discharged all-ratio positive-frequency theorem. The K=0 check, Weyl normalization, Lambda formulation, and arbitrary-radius scaling are recorded in TARGET-shell-d3."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "proved_internal",
        "statement_tex": "With strict counting N_D(Omega,Lambda)=#{j:lambda_j^D(Omega)<Lambda}, for every unit shell A_{rho,1}, 0<rho<1, and Lambda>=0, N_D(A_{rho,1},Lambda)<=(2/(9 pi))(1-rho^3)Lambda^(3/2). Equivalently, for every 0<r<R, N_D(A_{r,R},Lambda)<=(2/(9 pi))(R^3-r^3)Lambda^(3/2)=L_3|A_{r,R}|Lambda^(3/2), where L_3=1/(6 pi^2).",
        "dependencies_added": [
          "SHELL-sturm-liouville-completeness"
        ],
        "permitted_dependencies_added": [
          "SHELL-sturm-liouville-completeness"
        ],
        "blockers_removed": [
          "SHELL-rho-uniformity"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/TARGET-shell-d3-round22-theorem.md",
            "rounds/polya-main/round_022/exploration/theorem-claim-freeze.md",
            "rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md",
            "rounds/polya-main/round_022/responses/shell-theorem-incumbent.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
          ]
        },
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md",
          "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md",
          "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md"
        ],
        "artifact_hashes": {
          "packet": "8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228",
          "freeze": "6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d",
          "scope_audit": "b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6",
          "incumbent": "4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b",
          "clean_room": "9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12",
          "assembly_audit": "2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56",
          "cross_comparison": "6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458",
          "adversarial_referee": "a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9"
        },
        "falsification_cases_added": [
          "K=0 inferred by continuity rather than positivity and strict counting",
          "L_3 or shell volume normalized incorrectly",
          "R^2 Lambda replaced by R^(-2) Lambda in the count scaling",
          "the unit-shell theorem asserted without the arbitrary-radius corollary",
          "publication novelty inferred from the theorem proof"
        ],
        "reason_for_promotion": "The exact all-ratio assembly is complete, K=0 follows from the directly recorded positive-spectrum theorem, Weyl normalization and dilation were rederived, and isolated clean-room, provenance, cross-comparison, and fresh adversarial reviews all passed with no unsupported implication.",
        "next_action": "Use this as the proved strict Dirichlet P贸lya theorem for all genuine three-dimensional spherical shells. External dissemination still requires a human line-by-line proof audit and a separate current literature search."
      },
      {
        "id": "POLYA-program-target",
        "title": "Program target: exact Dirichlet P贸lya for non-tiling three-dimensional spherical shells",
        "status": "proved_internal",
        "statement_tex": "For every genuine three-dimensional spherical shell A_{r,R}={x in R^3:r<|x|<R}, 0<r<R, and every Lambda>=0, the strict Dirichlet count satisfies N_D(A_{r,R},Lambda)<=L_3|A_{r,R}|Lambda^(3/2). No member of this same class tiles R^3 by congruent rigid-motion copies with pairwise-disjoint interiors and exact or almost-everywhere coverage. This is a program-internal witness and makes no literature novelty or priority claim.",
        "dependencies_added": [
          "SHELL-spherical-shell-nontiling"
        ],
        "permitted_dependencies_added": [
          "CONV-strict-counting",
          "TARGET-shell-d3",
          "SHELL-spherical-shell-nontiling"
        ],
        "criticality": "theorem",
        "lead_author": "A1",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "A4",
        "review_independence": "clean_room",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/TARGET-shell-d3-round22-theorem.md",
            "rounds/polya-main/round_022/responses/shell-theorem-incumbent.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md",
            "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md",
            "state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md",
            "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md",
            "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md",
            "rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md",
            "rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md"
          ],
          "negative": [
            "rounds/polya-main/round_022/reviews/program-target-scope-audit.md",
            "rounds/polya-main/round_022/reviews/state-patch-final-audit.md"
          ],
          "inconclusive": [
            "rounds/polya-main/round_021/exploration/literature-scope-note.md"
          ]
        },
        "clean_room_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md",
          "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md",
          "rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md"
        ],
        "adversarial_review_artifacts_added": [
          "rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md",
          "rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md",
          "rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md"
        ],
        "artifact_hashes": {
          "theorem_packet": "8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228",
          "theorem_clean_room": "9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12",
          "theorem_adversarial_referee": "a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9",
          "geometry_packet": "d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f",
          "geometry_clean_room": "6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6",
          "geometry_adversarial_referee": "bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53",
          "program_scope_audit": "0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2",
          "superseded_program_scope_audit": "d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5",
          "failed_first_judge": "a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576",
          "failed_first_state_patch_audit": "b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573"
        },
        "falsification_cases_added": [
          "the spectral and geometric results concern different domain classes",
          "a shell endpoint r=0 or r=R is silently included",
          "strict counting, Lambda=0, volume normalization, or scaling is omitted",
          "non-tiling is proved only for translations but not all rigid motions",
          "an exact, almost-everywhere, or closed-copy tiling convention survives",
          "the word new is promoted into a literature novelty or priority assertion"
        ],
        "reason_for_promotion": "The separately reviewed spectral theorem and separately reviewed non-tiling theorem hold for literally the same complete 0<r<R shell family. The independent program-scope audit verified the conjunction, normalization, scaling, tiling conventions, track separation, and no-novelty boundary.",
        "next_action": "Treat the internal shell program target as complete. Preserve the no-novelty boundary; before external publication, require human reconstruction of every bottleneck lemma, manuscript-level checking, and an independent current literature search."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "COMP-certified-bessel",
        "reason": "The legacy Bessel framework remains diagnostic_only, detached from the theorem path, and unchanged by theorem completion."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "The first pilot remains a certified but analytically redundant regression box."
      },
      {
        "id": "COMP-certified-bessel-pilot-round17",
        "reason": "The second pilot remains a certified but analytically redundant regression box."
      },
      {
        "id": "ELLIPSE-near-circular",
        "reason": "The independent ellipse track remains open and is not used in the shell theorem."
      },
      {
        "id": "CERT-certificate-family",
        "reason": "The fallback certificate-family track remains open and is not used in the shell theorem."
      },
      {
        "id": "SRC-mathieu-ellipse",
        "reason": "The ellipse source-audit obligation remains unchanged."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 10,
    "reason": "Round 22 assembles and independently verifies the exact strict Dirichlet P贸lya theorem for every genuine three-dimensional spherical shell, proves the same full class non-tiling, and closes the internal program target without a literature novelty claim."
  }
}
```

## Application gate

Do not apply this patch until an independent auditor has authenticated this
judge, replayed every artifact hash, simulated the patch in memory, checked
all new and changed dependency/implies reciprocity plus global acyclicity,
confirmed 61 unique
obligations, verified all five relevant statuses as `proved_internal`, and
confirmed that `COMP-certified-bessel` and the parallel tracks are unchanged.
