# Reading Packet

Run: `polya-main`

Current round: 21

## Authoritative state

Read `state/proof_obligations.yml` first. Its SHA-256 is
`313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd`.
Round 20 is applied. Every $\mathcal D_{19}$ reference in older artifacts is
historical. The live analytic cover is $\mathcal A_{20}$ and the live
residual is $\mathcal D_{20}$.

The all-frequency shell theorem remains open. `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target` are
`open`; `COMP-certified-bessel` remains `diagnostic_only`.

## Accepted Round 20 result

Define

$$
\rho_c=\frac1{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
$$

The accepted combined closure proves strict Pólya on both lower components
of $\mathcal D_{19}$ and on

$$
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_{11}(\rho).
$$

It also proves

$$
\frac{39}{50}\le\rho<1,\qquad K\ge0,
$$

with equality only at $K=0$ and strict comparison for $K>0$. Its exact new
set is

$$
\boxed{\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K\le k_{11}(\rho)\}\\
&\cup\{39/50\le\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

The only indispensable new external zero payload is the qualified
$j_{21/2,1}>69/5$ specialization. DLMF supplies only the labelled
spherical/ordinary and recurrence identities. Every higher-radial zero,
strengthened lower-order first zero, shell comparison, angular propagation,
inventory, multiplicity, and payment is internal.

## Exact current residual

$$
\boxed{
\mathcal D_{20}=
\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

The face $\rho=\rho_c$ is included; $\rho=39/50$ is optical-owned and
excluded. The face $K=k_{11}$ is staircase-owned and excluded; $K=K_0=U$
is also excluded. The residual is nonempty because

$$
k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2).
$$

The inherited boxes $B_0,B_1$ remain regression evidence and do not subtract
again.

## Mandatory accepted artifacts

Read these before beginning the Round 21 candidate lifecycle.

### State, judge, and patch audit

- `state/current_state.md`
- `state/best_proof_draft.md`
- `state/lemma_bank.md`
- `state/gap_register.md`
- `state/next_round_prompts.md`
- `state/last_validation_report.md`
- `rounds/polya-main/round_020/judge/judge-020.md`
- `rounds/polya-main/round_020/reviews/state-patch-final-audit.md`

### Residual and candidate freezes

- `state/lemma_packets/SHELL-rho-compact-round20.md`
- `computations/round20_residual_mask.py`
- `computations/tests/test_round20_residual_mask.py`
- `computations/tests/test_round20_post_promotion_lifecycle.py`
- `rounds/polya-main/round_020/exploration/residual-mask-freeze.md`
- `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md`
- `state/lemma_packets/SHELL-combined-closure-round20-claim.md`
- `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md`
- `rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md`
- `rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md`

### Accepted proof and source evidence

- `sources/lorch_bessel_zeros.md`
- `sources/round20_bessel_zero_bounds.md`
- `sources/round20_higher_radial_zero_bounds.md`
- `sources/round20_k10_zero_bounds.md`
- `sources/round20_k11_zero_bounds.md`
- `rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md`
- `rounds/polya-main/round_020/reviews/combined-closure-clean-room.md`
- `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md`
- `computations/round20_verify_combined_closure.py`
- `computations/tests/test_round20_verify_combined_closure.py`
- `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md`
- `rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md`
- `rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md`
- `rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md`

### Preserved failure chronology

- `rounds/polya-main/round_020/reviews/candidate-final-byte-audit.md`:
  failed circular candidate-freeze lifecycle;
- `rounds/polya-main/round_020/reviews/combined-closure-constants-adversarial-audit.md`:
  failed missing cap-74 payment and disconnected checks;
- `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md`:
  failed control-byte and mutation-sensitivity gates;
- `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md`:
  preserves and repairs the false comparative-reserve sentence without
  changing A3's theorem verdict.

These are chronology, not positive promotion evidence except for the
explicitly passing addendum.

## Round 21 route evidence, not graph state

The following artifacts have independent adversarial audits but are not
promoted obligations:

- `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md`
- `computations/round21_certify_compact_proxy.py`
- `computations/tests/test_round21_certify_compact_proxy.py`
- `rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md`
- `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md`
- `rounds/polya-main/round_021/certification/aggregate-tail-global.md`
- `computations/round21_verify_aggregate_tail.py`
- `computations/tests/test_round21_verify_aggregate_tail.py`
- `rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md`
- `rounds/polya-main/round_021/exploration/exact-d20-closure.md`

The compact theorem covers the closed rectangle

$$
\frac7{51}\le\rho\le\frac{39}{50},\qquad12\le K\le200,
$$

using 10,580 exact rational leaves. The aggregate theorem covers

$$
\rho_c\le\rho\le\frac{39}{50},\qquad K\ge200,
$$

using 1,286 outward ratio boxes plus an exact derivative argument. The
containments $7/51<\rho_c$ and $k_{11}(\rho)>12$ show the intended route,
but no accepted proof-free Round 21 claim or empty residual exists yet.

## Reproduced Round 20 validation

The accepted final bytes passed:

- Round 20 residual self-check: 10 checks;
- residual-focused tests: 46 passed;
- final exact combined-closure verifier: 587 checks
  (488 substantive, 65 bookkeeping, 34 authentication);
- final exact-verifier tests: 17 passed;
- source and graph validation, compilation, UTF-8/control-byte checks, and
  `git diff --check`;
- the complete pre-application suite recorded by the independent patch audit:
  271 passed, 1 strict expected xfail, and 10 subtests.

The current post-promotion suite is recorded in
`state/last_validation_report.md`. The sole expected xfail remains the
obsolete Round 19 live-path assertion. The Round 20 manifest's baseline-aware
authentication remains a running PASS; its post-promotion lifecycle tests
preserve the original test bytes and prove the live state advanced.

## Canonical Round 21 order

1. Freeze the accepted one-piece $\mathcal D_{20}$ with a new classifier.
2. Independently audit that freeze before reading any candidate proof.
3. Write proof-free compact and aggregate certificate contracts; do not give
   A3 incumbent reports, verifier code, tests, or prior audits.
4. Freeze one proof-free closure candidate with exact $K=200$ ownership.
5. Run isolated A3 reconstruction from only the contracts, residual freeze,
   and foundational whitelist.
6. Run a candidate-specific A4 audit of both certificates and the exact set
   subtraction, despite their existing adversarial audits.
7. Cross-compare and run a fresh lemma referee.
8. Judge and independently audit a Round 21 State Patch. If warranted, create
   scoped `CERT-round21-compact-proxy` and
   `CERT-round21-aggregate-tail` obligations; keep
   `COMP-certified-bessel` `diagnostic_only`.
9. If the exact residual is then promoted as empty, separately run fresh
   theorem-level clean-room and adversarial audits.
10. Run a program-scope audit before any program-target promotion. Remove any
    obsolete diagnostic-parent blocker from the theorem path explicitly,
    without changing the diagnostic parent's status.

## Do-not-claim rules

- Do not substitute historical $\mathcal D_{19}$ or a larger certificate
  rectangle for live $\mathcal D_{20}$.
- Do not claim an empty live residual before the full Round 21 lifecycle and
  applied State Patch.
- Do not double-subtract $K=200$.
- Do not blur ownership at $\rho_c$, $39/50$, $k_{11}$, or $K_0=U$.
- Do not expose incumbent proof/code artifacts to isolated A3; use proof-free
  contracts.
- Do not broaden `COMP-certified-bessel`; use scoped certificate obligations
  if later promotion is justified.
- Do not call decimal displays, sampled floats, tests, or agent agreement
  proof.
- Do not begin final theorem review until exact $\mathcal D_{20}$ closure is
  already promoted.
