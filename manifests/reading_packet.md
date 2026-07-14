# Reading Packet

Run: `polya-main`

Current round: 20

## Authoritative state

Read `state/proof_obligations.yml` first. Its SHA-256 is
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.
Round 19 is applied. The live analytic cover is $\mathcal A_{19}$ and the
live residual is $\mathcal D_{19}$. Every $\mathcal D_{18}$ reference in
older artifacts is historical.

The all-frequency shell theorem remains open. The statuses
`SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, and `POLYA-program-target` are `open`;
`COMP-certified-bessel` is `diagnostic_only`.

## Accepted Round 19 result

Define

$$
\rho_c=\frac1{1+2\pi},\qquad
\rho_0=\frac1{\sqrt{337}},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},\qquad
d=\frac{\sqrt{337}}2.
$$

The accepted two-sided staircase proves

$$
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_6(\rho),
$$

and

$$
\rho_0<\rho<\rho_c,\qquad L(\rho)<K\le d.
$$

The only new external payload is the audited strict specialization
$j_{11/2,1}>17/2$ and the positive spherical/ordinary identification. The
bounds $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$, fixed-channel shell-to-ball
min--max, ball angular shifts, inventories, multiplicities, and Weyl
payments are internal.

The genuinely new set is

$$
\mathcal C_{19}
=\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}
\cup
\{\rho_c\le\rho<7/8,\ k_5(\rho)<K\le k_6(\rho)\}.
$$

## Exact current residual

$$
\boxed{\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

At $\rho=\rho_0$, $L=d$ and the candidate fiber is empty. The faces $K=d$
and $K=k_6$ are covered; $K=U$, $\rho=\rho_*$, and $\rho=7/8$ retain
their inherited owners, and $\rho=\rho_c$ belongs to the high component.
The boxes $B_0,B_1$ remain regression evidence and are not subtracted
again.

The residual is nonempty:

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2).
$$

## Mandatory Round 19 artifacts

Read these before beginning Round 20:

### State and decision

- `state/current_state.md`
- `state/best_proof_draft.md`
- `state/lemma_bank.md`
- `state/gap_register.md`
- `state/next_round_prompts.md`
- `state/last_validation_report.md`
- `rounds/polya-main/round_019/judge/judge-019.md`
- `rounds/polya-main/round_019/reviews/state-patch-final-audit.md`

### Exact residual and proof-free freezes

- `state/lemma_packets/SHELL-rho-compact-round19.md`
- `rounds/polya-main/round_019/exploration/residual-mask-freeze.md`
- `computations/round19_residual_mask.py`
- `computations/tests/test_round19_residual_mask.py`
- `rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md`
- `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md`
- `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md`

### Source, proofs, and reviews

- `sources/round19_bessel_zero_bounds.md`
- `rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md`
- `rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md`
- `rounds/polya-main/round_019/exploration/lower-ratio-route.md`
- `rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md`
- `computations/round19_verify_two_sided_staircase.py`
- `computations/tests/test_round19_verify_two_sided_staircase.py`
- `rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md`
- `rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md`
- `rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md`

## Reproduced validation

The accepted final bytes passed:

- 13 exact residual checks;
- 245 exact staircase checks;
- 37 residual-focused tests;
- 24 staircase-focused tests;
- 193 pre-application repository tests plus 10 subtests;
- 195 current post-application tests plus 10 subtests, with one strict
  expected xfail for the superseded live-path hash assertion and three
  passing Git-baseline lifecycle checks;
- compilation of 52 Python files;
- graph validation and `git diff --check`.

## Canonical Round 20 order

1. Freeze the exact three-piece $\mathcal D_{19}$ before any candidate.
2. Independently audit the residual classifier and every strict face.
3. Route the low, middle, and high components separately.
4. Audit every new external zero input as a narrow source obligation.
5. Synthesize and freeze one proof-free candidate with an exact proposed
   subtraction.
6. Run strictly isolated A3 reconstruction.
7. Run independent A4 exact verification and focused tests.
8. Cross-compare the incumbent, A3, A4, and source audit.
9. Run a fresh adversarial referee who participated in neither development
   nor A3.
10. Only then draft, audit, validate, and apply a State Patch once.

Current Round 20 small-hole shifted-tail, lower-staircase, and high-$k_8$
notes are exploratory only. They may suggest routes after the residual
freeze, but they are not accepted claims, proof-free freezes, independent
reconstructions, or promotion evidence.

## Do-not-claim rules

- Do not substitute historical $\mathcal D_{18}$, a rectangle, or a coarse
  over-cover for the live $\mathcal D_{19}$.
- Do not blur strict/inclusive ownership at $L,d,k_6,U$ or the ratio faces.
- Do not attribute internal tangent, min--max, angular-shift, shell-zero,
  multiplicity, or Weyl arguments to Lorch, DLMF, or FLPS.
- Do not call sampled floating-point roots or plots certified.
- Do not promote theorem-level targets while $\mathcal D_{19}$ is nonempty.
- Do not treat agreement among agents as mathematical verification.
