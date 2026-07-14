# Round 21 Lemma Judge: Exact Closure of D20

Date: 2026-07-15

## Decision

**PASS. First unsupported implication: none.**

This is a lemma-only decision. It accepts two narrowly scoped interval
certificates and the mathematical lemma that closes the exact Round 20
residual. It does not promote `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, or `POLYA-program-target`.
Those obligations still require a coherent theorem assembly, a theorem-level
clean-room reconstruction, a separate fresh theorem referee, and a separate
program-scope audit.

The accepted residual is

\[
\mathcal D_{20}=\left\{(\rho,K):
\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\]

The compact theorem proves the strict inequality on

\[
[7/51,39/50]\times[12,200],
\]

and the aggregate theorem proves it on

\[
[\rho_c,39/50]\times[200,\infty).
\]

The aggregate finite certificate owns only its base predicates at `K=200`.
The universal step is the A3 analytic proof of the exact derivative chain
and two integrations. The exact guards

\[
7/51<\rho_c,\qquad
k_{11}(\rho)>12\quad(\rho_c\le\rho<1)
\]

put every point of D20 in one of the two theorem domains. With `K=200`
assigned to the compact subtraction owner,

\[
\mathcal D_{20}
=\bigl(\mathcal D_{20}\cap\{K\le200\}\bigr)
\mathbin{\dot\cup}
\bigl(\mathcal D_{20}\cap\{K>200\}\bigr),
\]

so the exact successor residual is empty.

## Evidence separation

The proof roles remain distinct:

- A3 independently reconstructed the compact spectral bridge, aggregate
  reserve, every derivative, all-frequency propagation, rational guards,
  and exact set split without reading the incumbent or executable evidence.
- A4 authenticated and replayed the compact 10,580-leaf certificate at 256
  and 384 bits and the 1,286-box aggregate base certificate at 192 and 384
  bits. Its hardened wrapper explicitly refuses an all-frequency finite-box
  claim.
- The replacement cross-comparison rechecked the analytic/computational
  boundary and the active Machin branch mutations.
- A fresh child assumed the claim false and returned PASS. Its artifact-write
  turn stalled after the completed review, so the lead transparently sealed
  the handoff. The original child directly confirmed the corrected
  transcription, and a separate provenance audit passed.

The negative chronology is retained. It includes the initial ambiguous
candidate isolation, the initial aggregate-route failure, the implicit
Machin-branch failure, the lifecycle-incomplete second A4 cycle, the first
fresh referee that missed that lifecycle defect, and the first inaccurate
lead transcription. None is positive evidence.

## Certificate scope

`CERT-round21-compact-proxy` is interval-certified only for the exact closed
rectangle and its finite leaf predicates. `CERT-round21-aggregate-tail` is
interval-certified only for the exact rational ratio superset at the single
base frequency `K=200`. The mathematical obligation
`SHELL-exact-d20-closure` combines those finite predicates with the separately
proved analytic bridges.

The legacy `COMP-certified-bessel` obligation remains `diagnostic_only`.
Its Bessel-root pilot boxes remain useful regression evidence, but they are
not the computation used to close D20. Obsolete direct dependencies and
blockers on that diagnostic parent are removed without broadening it.

## State Patch

```json
{
  "proof_obligations": {
    "create": [
      {
        "id": "CERT-round21-compact-proxy",
        "type": "computation",
        "track": "certified_computation",
        "title": "Round 21 compact coarse-proxy interval certificate",
        "status": "certified",
        "statement_tex": "On the exact closed rectangle 7/51<=rho<=39/50 and 12<=K<=200, a deterministic outward-Arb certificate partitions the domain into 10580 exact rational leaves and proves on every leaf that the strict multiplicity-weighted coarse proxy is strictly below W(rho,K)=(2/(9 pi))(1-rho^3)K^3. The computation certifies the finite leaf, strict-wall, interface, corner, and coverage predicates; the separately proved analytic bridge transfers them to the spectral inequality.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SRC-annuli"
        ],
        "implies": [
          "SHELL-exact-d20-closure"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/certificate_contracts/ROUND21-compact-proxy-contract.md",
            "computations/round21_certify_compact_proxy.py",
            "computations/tests/test_round21_certify_compact_proxy.py",
            "rounds/polya-main/round_021/certification/compact-proxy-rectangle.md",
            "rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md",
            "computations/round21_verify_exact_d20_closure.py",
            "computations/tests/test_round21_verify_exact_d20_closure.py",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit-replacement.md"
          ],
          "negative": [
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-initial-lifecycle-miss.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit.md"
          ],
          "inconclusive": []
        },
        "owner": "A4",
        "criticality": "standard",
        "lead_author": "A4",
        "adversarial_reviewer": "independent-cross-checker",
        "review_independence": "independent",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SRC-annuli"
        ],
        "falsification_cases": [
          "all four closed root faces and all four vertices",
          "strict half-integer active-channel cutoffs",
          "nu=rho K and nu=K zero-extension interfaces",
          "exact integer proxy walls where strict count is M-1",
          "reversal of either monotone corner",
          "any gap, overlap, area mismatch, or double-owned shared face",
          "precision below 192 bits or a changed canonical digest",
          "tampered packet, leaf endpoint, proxy bound, count, or code byte"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
        ],
        "evidence_class": "interval_certified",
        "software_version": "Python 3.14.4; python-flint 0.8.0 Arb; frozen 256-bit and higher-precision 384-bit replays",
        "reproduction_command": "python -B computations/round21_certify_compact_proxy.py && python -B -m pytest -p no:cacheprovider -q computations/tests/test_round21_certify_compact_proxy.py && python -B -m computations.round21_verify_exact_d20_closure --high-precision 384",
        "coverage_statement": "Exactly the closed rectangle [7/51,39/50] x [12,200], tiled by 10580 exact rational leaves with closed analytic estimates and exact half-open shared-face ownership. No point outside this rectangle is certified by this obligation.",
        "artifact_hashes": {
          "contract": "1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe",
          "producer": "2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856",
          "tests": "29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36",
          "report": "c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293",
          "adversarial_audit": "aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca",
          "canonical_certificate": "96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631",
          "hardened_wrapper": "4868dcc3251fe30aff4d8ef362cdd8924fe69d95cafa8d597fa9c88560780ff8",
          "hardened_tests": "6716ff1beaaf4053092f8e7baa4d77b95acf38f3fc3d467f15ec76e545271da7",
          "hardened_report": "d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56",
          "replacement_cross_comparison": "e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e",
          "hardened_referee": "c0a5239cae460ba961d911b384a9f2d2afac605865c72b4d2c604c0f4aa54a9c",
          "referee_provenance_audit": "48b259a94a0fd91a37ac2b606a22e1e4ca593f45bc2ef4392b7dd61dd359a5ab"
        },
        "certification_artifacts": [
          "state/certificate_contracts/ROUND21-compact-proxy-contract.md",
          "rounds/polya-main/round_021/certification/compact-proxy-rectangle.md",
          "rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md"
        ],
        "reason_for_promotion": "Every exact leaf, strict wall, interface, monotone corner, coverage invariant, input hash, and precision gate passes at the frozen precision and at 384 bits. The analytic bridge was independently reconstructed and the fresh referee found no unsupported implication.",
        "next_action": "Retain this certificate with its exact closed rectangle and immutable digest. Use it only through SHELL-exact-d20-closure; do not broaden it into a Bessel-root or all-frequency certificate."
      },
      {
        "id": "CERT-round21-aggregate-tail",
        "type": "computation",
        "track": "certified_computation",
        "title": "Round 21 aggregate-tail base-face interval certificate",
        "status": "certified",
        "statement_tex": "On the exact rational ratio superset 7/51<=rho<=39/50 at the single base frequency K=200, 1286 outward Arb boxes prove B(rho,200)>0, B_K(rho,200)>0, F(rho)>0, all base guards, and the stated base derivative-consistency predicates. This computation makes no proof decision at K>200; the separately proved analytic curvature and integration chain supplies the universal tail theorem.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-fixed-rho-high-energy",
          "SRC-annuli"
        ],
        "implies": [
          "SHELL-exact-d20-closure"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/certificate_contracts/ROUND21-aggregate-tail-contract.md",
            "rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md",
            "computations/round21_verify_aggregate_tail.py",
            "computations/tests/test_round21_verify_aggregate_tail.py",
            "rounds/polya-main/round_021/certification/aggregate-tail-global.md",
            "rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md",
            "computations/round21_verify_exact_d20_closure.py",
            "computations/tests/test_round21_verify_exact_d20_closure.py",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit-replacement.md"
          ],
          "negative": [
            "rounds/polya-main/round_021/exploration/aggregate-low-interface-adversarial-audit.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-initial-lifecycle-miss.md"
          ],
          "inconclusive": []
        },
        "owner": "A4",
        "criticality": "standard",
        "lead_author": "A4",
        "adversarial_reviewer": "independent-cross-checker",
        "review_independence": "independent",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-fixed-rho-high-energy",
          "SRC-annuli"
        ],
        "falsification_cases": [
          "both ratio endpoints and every consecutive exact box face",
          "the two eta branches and their common rho=1/2 value",
          "all 11 finite sign families on every box",
          "outward containment of both rational endpoints",
          "base guards mu>3/2, 200 eta_rho>1, and S>Rbar>200 rho",
          "any changed factor or sign in B, B_K, I_KK, E_KK, B_KK, or F",
          "precision below 192 bits or any partition gap or overlap",
          "any attempted finite-box claim at K>200"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
        ],
        "evidence_class": "interval_certified",
        "software_version": "Python 3.14.4; python-flint 0.8.0 Arb; frozen 192-bit and higher-precision 384-bit replays",
        "reproduction_command": "python -B computations/round21_verify_aggregate_tail.py --precision 192 && python -B -m unittest computations.tests.test_round21_verify_aggregate_tail -v && python -B -m computations.round21_verify_exact_d20_closure --high-precision 384",
        "coverage_statement": "Exactly rho in [7/51,39/50] at K=200, split into 1286 exact rational boxes at rho=1/2. The certified predicates are base signs, guards, and consistency checks only; no K>200 point is certified by finite boxes.",
        "artifact_hashes": {
          "contract": "06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d",
          "analytic_route": "61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0",
          "verifier": "fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952",
          "tests": "50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91",
          "report": "0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6",
          "adversarial_audit": "aa12d25d71091cfd01a116bc2777afa8669248a13441be391cf3da0b48c9a894",
          "hardened_wrapper": "4868dcc3251fe30aff4d8ef362cdd8924fe69d95cafa8d597fa9c88560780ff8",
          "hardened_tests": "6716ff1beaaf4053092f8e7baa4d77b95acf38f3fc3d467f15ec76e545271da7",
          "hardened_report": "d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56",
          "replacement_cross_comparison": "e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e",
          "hardened_referee": "c0a5239cae460ba961d911b384a9f2d2afac605865c72b4d2c604c0f4aa54a9c",
          "referee_provenance_audit": "48b259a94a0fd91a37ac2b606a22e1e4ca593f45bc2ef4392b7dd61dd359a5ab"
        },
        "certification_artifacts": [
          "state/certificate_contracts/ROUND21-aggregate-tail-contract.md",
          "rounds/polya-main/round_021/certification/aggregate-tail-global.md",
          "rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md"
        ],
        "reason_for_promotion": "Every base sign, guard, consistency predicate, branch, endpoint containment, partition invariant, input hash, and precision gate passes at 192 and 384 bits. The wrapper and independent reviews explicitly preserve the finite K=200 scope.",
        "next_action": "Retain this certificate as the K=200 base face only. Use its signs through the analytic propagation in SHELL-exact-d20-closure; never cite it as a finite-box proof at K>200."
      },
      {
        "id": "SHELL-exact-d20-closure",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Round 21 exact closure of the final compact-shell residual",
        "status": "proved_internal",
        "statement_tex": "Let rho_c=1/(1+2 pi), z_rho=pi/(1-rho), k_11(rho)=sqrt(z_rho^2+132), and W(rho,K)=(2/(9 pi))(1-rho^3)K^3. The strict shell inequality N_D(A_(rho,1),K^2)<W(rho,K) holds on the closed compact rectangle 7/51<=rho<=39/50, 12<=K<=200, and on rho_c<=rho<=39/50, K>=200. The exact guards 7/51<rho_c and k_11(rho)>12 for rho_c<=rho<1 imply that D20={rho_c<=rho<39/50, k_11(rho)<K<U(rho)=K_0(rho)} is the disjoint union of its K<=200 and K>200 parts, with K=200 assigned to the compact owner. Hence the exact successor residual D21 is empty. The faces rho=39/50, K=k_11, and K=U remain outside D20 and are not subtracted again.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-fixed-rho-high-energy",
          "SRC-annuli",
          "SHELL-combined-closure",
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail"
        ],
        "implies": [
          "SHELL-rho-compact-analytic-envelope"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "state/lemma_packets/SHELL-rho-compact-round21.md",
            "computations/round21_residual_mask.py",
            "computations/tests/test_round21_residual_mask.py",
            "rounds/polya-main/round_021/exploration/residual-mask-freeze.md",
            "rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md",
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "state/certificate_contracts/ROUND21-compact-proxy-contract.md",
            "state/certificate_contracts/ROUND21-aggregate-tail-contract.md",
            "rounds/polya-main/round_021/exploration/exact-d20-closure.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-addendum.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit-replacement.md"
          ],
          "negative": [
            "rounds/polya-main/round_021/reviews/candidate-final-byte-isolation-audit.md",
            "rounds/polya-main/round_021/exploration/aggregate-low-interface-adversarial-audit.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-initial-branch-gap.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-initial-lifecycle-miss.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit.md"
          ],
          "inconclusive": []
        },
        "owner": "A2",
        "criticality": "bottleneck",
        "lead_author": "A2",
        "clean_room_reviewer": "A3",
        "adversarial_reviewer": "fresh-hardened-referee",
        "review_independence": "clean_room",
        "permitted_dependencies": [
          "CONV-strict-counting",
          "SHELL-sturm-liouville-completeness",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional",
          "SHELL-low-interface-fixed-rho-high-energy",
          "SRC-annuli",
          "SHELL-combined-closure",
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail"
        ],
        "falsification_cases": [
          "rho=7/51, rho=rho_c, rho=1/2, and rho=39/50 from both sides",
          "K=12, K=k_11(rho), K=200, and K=U(rho) from both sides",
          "strict integer phase walls and half-integer active-channel walls",
          "both zero-extension interfaces and all compact vertices",
          "tau=0, half-integer mu walls, integer K eta_rho walls, and the rho=1/2 eta branch",
          "all exact Q and B identities, derivative signs, universal guards, and both integrations",
          "loss of the lower Machin range bound, upper range bound, or principal-branch conclusion",
          "finite K=200 signs incorrectly promoted to an all-K box claim",
          "all three orderings U<200, U=200, and U>200",
          "double subtraction or omission of the K=200 face",
          "inclusion of rho=39/50, K=k_11, or K=U in D20",
          "promotion of any compact, uniform, theorem, program, or legacy Bessel computation status"
        ],
        "clean_room_artifacts": [
          "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-addendum.md"
        ],
        "adversarial_review_artifacts": [
          "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md",
          "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit-replacement.md"
        ],
        "artifact_hashes": {
          "residual_packet": "fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5",
          "residual_classifier": "1f6254b699519212ae8bd835b789b1002db78318d30bf347d8a0f60a14cbaa38",
          "residual_tests": "6703899a0ba89021089c6f3407a836e3cfcfb54960f81c4e0261c5b5fdf57477",
          "residual_freeze": "92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5",
          "residual_audit": "0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08",
          "candidate": "415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3",
          "candidate_freeze": "75afe7f0ea6ca2da4106510f6e90fb64a13a83fd83f023361d3433493d64558c",
          "candidate_isolation": "d4aaf2676c9056721b919f5b24341e39e77178b27a49bfaa5b54a8e77eb6c57e",
          "compact_contract": "1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe",
          "aggregate_contract": "06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d",
          "incumbent": "e04b8199783188f0d90b6c033abe031d7c9ecd54ee1a5cdfd198f3517e98d039",
          "clean_room": "0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc",
          "clean_room_addendum": "d003d105038e78a0b95137b9fecb0ca5758a804dac17cbea1e6eea155f50b257",
          "hardened_wrapper": "4868dcc3251fe30aff4d8ef362cdd8924fe69d95cafa8d597fa9c88560780ff8",
          "hardened_tests": "6716ff1beaaf4053092f8e7baa4d77b95acf38f3fc3d467f15ec76e545271da7",
          "hardened_report": "d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56",
          "replacement_cross_comparison": "e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e",
          "hardened_referee": "c0a5239cae460ba961d911b384a9f2d2afac605865c72b4d2c604c0f4aa54a9c",
          "referee_provenance_audit": "48b259a94a0fd91a37ac2b606a22e1e4ca593f45bc2ef4392b7dd61dd359a5ab",
          "preserved_branch_failure": "3d234405e5776b31dea29fbff8ee2803d0f54052cab851240b81546e9ac1b7f2",
          "preserved_lifecycle_failure": "11672110bdc1169c40b46247832c19b9187df3112ab67f28324f6784a2f552a6",
          "preserved_initial_referee": "0466a240861de32b60819f9a5cd3b48106b230839c3fae07f4f67cbd59588e74",
          "preserved_referee_miss": "af1761a2426ad22f2cf93ea765e3b98af1314f4587730b654ed4eb36e37106ba",
          "preserved_provenance_failure": "5b7c0938f39860dc060594090c50c168e71993ed284b0c8f45470df1aa00d0d4"
        },
        "reason_for_promotion": "The A3 proof reconstructs both spectral bridges and the universal aggregate propagation; the interval certificates discharge every finite premise; the hardened branch and mutation cycle closes the exact-constant lifecycle; exact set arithmetic gives a disjoint exhaustive subtraction; and the corrected fresh referee plus provenance audit find no unsupported implication. D21 is empty, but theorem-level obligations remain deliberately open.",
        "next_action": "Use this lemma only through the complete Round 21 cover with its exact face ownership. Assemble the full shell theorem, verify K=0, strict counting, endpoint overlap, volume normalization, and scaling, then run separate theorem-level clean-room and adversarial audits before promoting any higher obligation."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "implies_added": [
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SHELL-sturm-liouville-completeness",
        "implies_added": [
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SHELL-phase-enclosures",
        "implies_added": [
          "CERT-round21-compact-proxy",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "implies_added": [
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SHELL-low-interface-fixed-rho-high-energy",
        "implies_added": [
          "CERT-round21-aggregate-tail",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SRC-annuli",
        "implies_added": [
          "CERT-round21-compact-proxy",
          "CERT-round21-aggregate-tail",
          "SHELL-exact-d20-closure"
        ]
      },
      {
        "id": "SHELL-combined-closure",
        "implies_added": [
          "SHELL-exact-d20-closure"
        ],
        "next_action": "Treat D20 as the authenticated input to SHELL-exact-d20-closure. Do not reuse the Round 20 lemma outside its stated lower, staircase, and optical domains."
      },
      {
        "id": "SHELL-rho-compact-analytic-envelope",
        "status": "proved_internal",
        "statement_tex": "Retain the complete accepted cover through Round 20, both endpoint theorems, and the all-ratio high-frequency theorem. Round 21 adds the strict compact theorem on 7/51<=rho<=39/50 and 12<=K<=200 and the strict aggregate theorem on rho_c<=rho<=39/50 and K>=200. Exact guards put every point of D20={rho_c<=rho<39/50, k_11(rho)<K<U(rho)=K_0(rho)} in their disjoint K<=200 or K>200 subtraction owners, with K=200 compact-owned. Thus the exact residual D21 is empty. All inherited faces remain with their prior owners; the Round 21 theorem domains may overcover the residual without double subtraction. B0 and B1 remain analytically redundant regression certificates.",
        "dependencies_added": [
          "SHELL-exact-d20-closure"
        ],
        "permitted_dependencies_added": [
          "SHELL-exact-d20-closure"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-addendum.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened-provenance-audit-replacement.md"
          ]
        },
        "falsification_cases_added": [
          "D21 declared empty without both the compact and aggregate theorem domains",
          "K=200 omitted or subtracted twice",
          "finite K=200 boxes confused with universal aggregate propagation",
          "any assumed ordering of U with 200",
          "rho=39/50, K=k_11, or K=U subtracted again",
          "empty residual confused with theorem-level promotion"
        ],
        "reason_for_update": "The independently proved compact and aggregate theorems cover the exact D20 by an exhaustive disjoint K split. Every finite premise and analytic implication passed hardened review, so the successor residual is exactly empty.",
        "next_action": "Treat D21 as empty. Keep higher obligations open until a coherent all-rho theorem assembly passes separate clean-room and fresh adversarial review."
      },
      {
        "id": "SHELL-rho-compact",
        "status": "open",
        "dependencies_removed": [
          "COMP-certified-bessel"
        ],
        "permitted_dependencies_removed": [
          "COMP-certified-bessel"
        ],
        "blockers_removed": [
          "COMP-certified-bessel"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
          ]
        },
        "falsification_cases_added": [
          "an empty residual is promoted without a theorem-level assembly",
          "legacy Bessel pilot certificates are treated as the D20 closure",
          "compact interval uniformity is inferred without checking endpoint overlap and all K faces"
        ],
        "next_action": "The exact analytic residual is empty and the obsolete diagnostic Bessel dependency is removed. Keep this obligation open for the separate theorem-level assembly and independent final reviews."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
          ]
        },
        "falsification_cases_added": [
          "D21 empty but endpoint and compact owners not assembled coherently",
          "rho=rho_* or rho=7/8 lost at an endpoint seam",
          "the full theorem promoted before fresh theorem review"
        ],
        "next_action": "The endpoint theorems and empty compact residual now provide all mathematical pieces. Keep this obligation open until the full all-rho assembly passes theorem-level clean-room and adversarial audits."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "dependencies_removed": [
          "COMP-certified-bessel"
        ],
        "permitted_dependencies_removed": [
          "COMP-certified-bessel"
        ],
        "blockers_removed": [
          "COMP-certified-bessel"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
          ]
        },
        "falsification_cases_added": [
          "D21 empty but K=0, volume normalization, strict counting, or scaling omitted",
          "unit outer radius proved but arbitrary shell radii not scaled",
          "the theorem promoted without a fresh theorem clean-room and final referee"
        ],
        "next_action": "The last residual is mathematically closed and the obsolete diagnostic computation dependency is removed. Keep the theorem open while assembling K=0, all ratio seams, Weyl normalization, and scaling, then run fresh theorem-level reviews."
      },
      {
        "id": "POLYA-program-target",
        "status": "open",
        "blockers_removed": [
          "COMP-certified-bessel"
        ],
        "evidence_added": {
          "positive": [
            "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md",
            "rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md"
          ]
        },
        "falsification_cases_added": [
          "shell theorem pieces complete but theorem-level review not passed",
          "non-tiling geometry or scaling omitted",
          "publication novelty inferred from a limited literature search"
        ],
        "next_action": "Keep the program target open. Complete the shell theorem assembly and audits, prove the full shell family is non-tiling, and run a separate program-scope audit without making a publication-priority claim."
      },
      {
        "id": "COMP-certified-bessel",
        "status": "diagnostic_only",
        "implies_removed": [
          "TARGET-shell-d3"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md"
          ]
        },
        "falsification_cases_added": [
          "the scoped proxy and aggregate certificates are relabelled as cross-product root isolation",
          "B0 or B1 is subtracted again after analytic subsumption",
          "diagnostic_only status is promoted by transitive association"
        ],
        "next_action": "Retain this parent as diagnostic_only with B0 and B1 unchanged. The new Round 21 certificates have their own exact obligations and do not broaden or promote this legacy framework."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "SHELL-rho-zero-endpoint",
        "reason": "The complete small-hole endpoint theorem and its included rho_* face are unchanged."
      },
      {
        "id": "SHELL-rho-one-endpoint",
        "reason": "The complete thin-shell endpoint theorem and its included rho=7/8 face are unchanged."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "reason": "The fixed-ratio high-energy theorem and K_0 upper owner are unchanged."
      },
      {
        "id": "SHELL-combined-closure",
        "reason": "Its Round 20 theorem remains proved_internal; only reverse dependency metadata and its next action are refreshed."
      },
      {
        "id": "COMP-certified-bessel-pilot-round8",
        "reason": "B0 remains a certified but analytically redundant regression box."
      },
      {
        "id": "COMP-certified-bessel-pilot-round17",
        "reason": "B1 remains a certified but analytically redundant regression box."
      },
      {
        "id": "COMP-certified-bessel",
        "reason": "The legacy parent remains diagnostic_only and is no longer a direct theorem dependency."
      },
      {
        "id": "SHELL-rho-compact",
        "reason": "The exact residual is empty, but the separate theorem-level assembly and audits have not yet occurred."
      },
      {
        "id": "SHELL-rho-uniformity",
        "reason": "All mathematical cover pieces exist, but theorem-level assembly and review remain pending."
      },
      {
        "id": "TARGET-shell-d3",
        "reason": "No theorem status changes in this lemma-only patch."
      },
      {
        "id": "POLYA-program-target",
        "reason": "No program status changes before theorem and non-tiling scope audits."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 10,
    "reason": "Round 21 closes the exact final residual D20. The compact and aggregate certificate scopes are explicit, the all-frequency aggregate step is analytically reconstructed, every face and strict wall is preserved, failed review cycles remain negative evidence, and D21 is exactly empty. Higher theorem and program obligations remain open for their distinct final-review gates."
  }
}
```

## Application gate

This judge does not apply its patch. Before application:

1. authenticate every hash in the patch;
2. validate the current graph and embedded patch;
3. rerun the residual classifier and exact-D20 wrapper;
4. rerun the focused hardened tests and complete suite;
5. obtain an independent State Patch audit confirming that no higher target
   is promoted and that the legacy diagnostic computation is only detached,
   not broadened.

The reproduction commands are:

```text
python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml
python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/polya-main/round_021/judge/judge-021-lemma.md
python -B computations/round21_residual_mask.py
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round21_residual_mask.py
python -B -m computations.round21_verify_exact_d20_closure --high-precision 384
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round21_verify_exact_d20_closure.py
python -B -m pytest -p no:cacheprovider -q
```

If every gate passes, apply exactly once with `--round-index 21` and
`--judge-ref rounds/polya-main/round_021/judge/judge-021-lemma.md`.
