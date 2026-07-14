# Round 19 Residual-Mask Freeze

Date: 2026-07-14

Decision: **FROZEN / PASS**.

This record releases the exact post-Round-18 residual packet for Round 19
incumbent proof work. It freezes set bookkeeping only; it is not a new
analytic or certified theorem and contains no Round 19 proof candidate.

Baseline commit:
`15e4d61db885bfff00a674fd7f37e4cffda70d0c`.

## Frozen artifacts

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `computations/round19_residual_mask.py` | `bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6` |
| `computations/tests/test_round19_residual_mask.py` | `41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787` |
| independent pre-freeze audit | `9e7dedaab08425166998a5c766bdb32d3787d9f35b6c4bf4b7d6be07009c9b43` |

The independent audit is
`rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md`.
It reconstructed the set arithmetic without editing the three frozen
artifacts and returned **PASS; first issue: none**.

## Authenticated inherited inputs

| artifact | SHA-256 |
|---|---|
| accepted graph `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` |
| canonical Round 19 prompts | `7d05055b4b884b052f3970bd7b08335dfe63bca25b5ac5a9db8704f6a88db2f7` |
| accepted Round 18 judge | `73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61` |
| frozen pre-Round-18 packet | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| Round 18 residual freeze | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| frozen Round 18 classifier | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| Round 18 classifier tests | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| Round 18 proof-free claim | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| Round 18 candidate freeze | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |

Every inherited hash was recomputed from committed bytes by both the main
validation pass and the independent audit.

## Derivation lock

The classifier imports the frozen Round 18 predicate and applies only

$$
\mathcal A_{18}
=\mathcal A_{17}^{\mathrm{frozen}}
\cup\overline{\mathcal C}_{18},
$$

where

$$
\overline{\mathcal C}_{18}
=\left\{\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_5(\rho)\right\}.
$$

Its genuinely new set is exactly

$$
\mathcal C_{18}
=\left\{\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K\le k_5(\rho)\right\}.
$$

The classifier independently cross-checks the normalized complement

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}
}
$$

Every displayed frequency face is strict. The $\rho=\rho_c$ slice is
assigned to the post-$k_5$ piece. The complete piecewise upper floor is

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\le\rho<7/8,
\end{cases}
$$

with $H_0(\rho_{HK})=K_0(\rho_{HK})$. All inherited interfaces and every
lower, upper, vertical, radial, angular, staircase, endpoint, and global
face have an explicit assignment in the frozen packet.

The certificates on $B_0$ and $B_1$ remain independent regression
evidence, but

$$
B_0\subset\mathcal C_{17}\subset\mathcal A_{18},
\qquad
B_1\subset\mathcal C_{17}\subset\mathcal A_{18}.
$$

Neither is subtracted again, and the theorem-wise uncovered set is exactly
$\mathcal U_{18}=\mathcal D_{18}$. The witness
$(1/2,30)\in\mathcal D_{18}$ is retained, so the theorem remains open.

## Method-wall lock

The packet inventories

$$
k_5(\rho),\qquad 2z_\rho,\qquad k_6(\rho),\qquad U(\rho),
$$

without changing residual membership. It carries only the accepted local
ordering

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
$$

No global ordering, crossing threshold, one-radial continuation, or stale
angular cap is encoded. Indeterminate signs on the $2z_\rho$ and
$k_6(\rho)$ method walls cannot make a decisively classified residual point
indeterminate.

## Validation transcript

~~~powershell
python computations/round19_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round19_residual_mask.py -q
python -m pytest -q
python -m compileall -q computations math_collab
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
git diff --check
~~~

Results:

- classifier self-check: **PASS**, 13 checks;
- focused suite: **PASS**, 37 tests;
- full suite: **PASS**, 169 tests and 10 subtests;
- bytecode compilation: **PASS**;
- obligation graph validation: **PASS**, 53 obligations and acyclic;
- diff hygiene: **PASS**;
- independent tri-state truth tables: **PASS**, 1,792 cases;
- independent rational-point comparison: **PASS**, 182 points;
- exact $B_0/B_1$ absorption: **PASS**, all eight corners plus monotone
  full-box faces;
- irrelevant $2z_\rho$ and $k_6(\rho)$ wall crossings: **PASS**.

## Release rule

The packet, classifier, and tests in the first three rows are immutable for
this round. Any correction requires a replacement packet, classifier,
tests, and freeze record with new hashes.

Round 19 incumbent proof work may begin only from these frozen bytes. Once
an incumbent identifies a candidate, a separate proof-free claim packet
must be frozen before an isolated reconstruction or independent
exact-constant audit sees the incumbent proof. This freeze authorizes no
candidate theorem by itself.
