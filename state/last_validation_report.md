# Last Validation Report

Date: 2026-07-15

Round: 20 post-promotion synchronization

## Promotion decision

**PASS. First unsupported implication: none.**

The Round 20 State Patch was applied exactly once at commit `aaa9e4a`. The
authoritative graph is `state/proof_obligations.yml`, SHA-256
`313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd`.
It contains 57 unique obligation IDs and validates with no dangling or
duplicate relationship, impermissible dependency, or graph cycle.

Created obligations:

- `SRC-ROUND20-BESSEL-ZEROS`: `proved_external_dependency`;
- `SHELL-combined-closure`: `proved_internal`.

No existing mathematical status changed. In particular,
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` remain `open`; `COMP-certified-bessel` remains
`diagnostic_only`.

## Promoted source boundary

The new source obligation contributes only Lorch's qualified strict
first-positive-zero specialization

$$
j_{21/2,1}>\frac{69}{5},
$$

together with the labelled DLMF spherical/ordinary identity, explicit
half-integer formulas, and recurrences. Exact positive-side algebra verifies
the Lorch consequence. The same source formula implies the displayed
order-$17/2$ and order-$19/2$ bounds, but both have independent internal
derivations from $j_{15/2,1}>23/2$ and same-index angular min--max.

Every $n\ge2$ zero, the strengthened first-zero bounds at orders $13/2$ and
$15/2$, root enumeration, ODE simplicity, shell-to-ball comparison, angular
propagation, inventory, multiplicity cap, Weyl payment, and residual
subtraction is internal. No source supplies a shell cross-product zero.

## Promoted analytic closure

Let

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

Round 20 proves strict Pólya on the complete lower part

$$
\mathcal D_{19}^{\rm low}=
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}
\cup
\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\},
$$

on the closed staircase

$$
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_{11}(\rho),
$$

and at every frequency for

$$
\frac{39}{50}\le\rho<1,
$$

with equality only at $K=0$ and strict comparison for $K>0$. The genuinely
new set is

$$
\boxed{\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K\le k_{11}(\rho)\}\\
&\cup\{39/50\le\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

## Exact surviving residual

The historical $\mathcal D_{19}$ is superseded. Exact subtraction gives

$$
\boxed{
\mathcal D_{20}=
\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

The face $\rho=\rho_c$ is included; $\rho=39/50$ is optical-owned. The
face $K=k_{11}$ is staircase-owned; $K=K_0=U$ is excluded. On this ratio
interval the $H_0$ and seam branches are ineligible, so $U=K_0$ exactly.
The inherited boxes $B_0,B_1$ remain regression evidence and are not
subtracted again.

The strict witness

$$
k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2)
$$

puts $(1/2,30)$ in $\mathcal D_{20}$. Therefore the residual is nonempty and
no theorem-level target closes in Round 20.

## Complete gate chronology

The exact residual freeze and independent mask audit passed. The proof-free
candidate scope audit also passed, but the first released bytes then failed
final-byte review because their lifecycle text was circular. The corrected
claim and freeze passed a replacement final-byte audit.

The isolated A3 reconstruction passed. Its sole false statement said every
other high cap cell had a larger reserve; the immutable addendum proves the
cap-$74$ cell empty under full propagation and also pays it directly. The
theorem verdict was unchanged.

The first A4 verifier failed because it did not pay that live cap-$74$ cell
and contained disconnected or tautological checks. Its first replacement
failed because of an actual control byte, mutation-insensitive localization,
an insufficient wrong-wall test, and authenticated-looking skip output. Only
the second repaired bundle is positive A4 evidence: 587 exact checks
(488 substantive, 65 bookkeeping, 34 authentication) and 17 focused tests.

The independent zero-provenance audit, final A4 re-audit,
cross-comparison, fresh adversarial referee, judge, and independent
State-Patch audit all returned PASS. Both failed A4 cycles and the failed
candidate release remain negative chronology, not promotion support.

## Post-promotion validation ledger

Final derived-state reproduction passed:

- authoritative graph SHA-256: unchanged at
  `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd`;
- graph validator: **PASS**;
- focused Round 19 lifecycle, Round 20 residual, and Round 20 lifecycle
  tests: **51 passed**;
- complete repository suite: **273 passed, 1 strict expected xfail,
  10 subtests passed**;
- the expected xfail is only the immutable Round 19 freeze's obsolete
  live-path comparison;
- the Round 20 manifest's baseline-aware authentication remains a running
  PASS against commit `658674117632d60990ac9b9046aa0fcff9e91a62`;
- the new Round 20 lifecycle checks authenticate the immutable original test
  bytes and prove both mutable state inputs advanced;
- in-memory Python source compilation: **PASS, 62 files**;
- strict UTF-8 and C0/DEL scan of every changed derived artifact: **PASS**;
- `git diff --check`: **PASS**.

## Next method boundary

Round 21 begins by freezing the accepted one-piece $\mathcal D_{20}$ and
auditing that classifier before any candidate release. Two independently
audited but unpromoted routes are available: a compact coarse-proxy
certificate on
$[7/51,39/50]\times[12,200]$ and an aggregate tail theorem on
$[\rho_c,39/50]\times[200,\infty)$.

Their next admissible use is through proof-free certificate contracts and a
new proof-free closure claim. Isolated A3 must not receive the incumbent
reports, code, tests, prior audits, or exploratory synthesis. A candidate-
specific A4 audit, cross-comparison, fresh lemma referee, judge, and State
Patch audit remain mandatory. No empty residual is accepted yet.

If later promotion is justified, use scoped
`CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail` obligations;
do not broaden `COMP-certified-bessel`. Any obsolete diagnostic-parent
blocker on the theorem path must be removed explicitly while the parent
stays `diagnostic_only`. Only after exact $\mathcal D_{20}$ closure is
promoted may separate theorem-level clean-room, theorem adversarial, and
program-scope audits begin.
