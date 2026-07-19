# Round 19 Residual-Mask Independent Audit

Date: 2026-07-14

Verdict: **PASS**.

First issue: **none**.

This is an independent pre-freeze audit of exactly these three artifacts:

- `computations/round19_residual_mask.py`;
- `computations/tests/test_round19_residual_mask.py`;
- `state/lemma_packets/SHELL-rho-compact-round19.md`.

The audited files were not edited. The comparison baseline was the committed
post-Round-18 state at
`15e4d61db885bfff00a674fd7f37e4cffda70d0c`, including the accepted graph,
Round 18 judge, Round 18 residual classifier, and canonical Round 19 prompts.

## 1. Observed artifact hashes

| artifact | observed SHA-256 |
|---|---|
| `computations/round19_residual_mask.py` | `bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6` |
| `computations/tests/test_round19_residual_mask.py` | `41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787` |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |

The baseline commit recorded by both the packet and executable manifest is
the actual current `HEAD`.

Every inherited hash used by the packet or executable manifest was recomputed
directly from bytes and matched:

| inherited artifact | observed SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` |
| `state/next_round_prompts.md` | `7d05055b4b884b052f3970bd7b08335dfe63bca25b5ac5a9db8704f6a88db2f7` |
| `rounds/polya-main/round_018/judge/judge-018.md` | `73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61` |
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `rounds/polya-main/round_018/exploration/residual-mask-freeze.md` | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| `computations/round18_residual_mask.py` | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| `computations/tests/test_round18_residual_mask.py` | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| `state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md` | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| `rounds/polya-main/round_018/exploration/candidate-claim-freeze.md` | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |

## 2. Independent set reconstruction

Write the accepted closed Round 18 staircase as

$$
\overline{\mathcal C}_{18}
=\left\{\rho_c\leq\rho\leq\frac78,
\quad z_\rho\leq K\leq k_5(\rho)\right\}.
$$

Starting from the authenticated post-Round-17 predicate, direct union gives

$$
\mathcal A_{18}
=\mathcal A_{17}^{\mathrm{frozen}}
\cup\overline{\mathcal C}_{18}.
$$

The overlap with the old closed angular band is through $K=k_2$, and the old
$\rho=7/8$ endpoint owns that full slice. Therefore the genuinely new set is
exactly

$$
\mathcal C_{18}
=\left\{\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)\right\}.
$$

Subtracting this from the two-piece $\mathcal D_{17}$ leaves the lower-ratio
piece unchanged and replaces the strict $K>k_2$ lower face in the other piece
by the strict $K>k_5$ face:

$$
\mathcal D_{18}
=\left\{\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\leq\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)\right\}.
$$

Thus $\rho=\rho_c$ belongs to the post-$k_5$ branch, while every displayed
frequency face is excluded from the residual. This agrees exactly with the
Round 18 judge, graph statement, canonical Round 19 prompt, packet, manifest,
and executable predicate. The accepted point $(1/2,30)$ remains in the second
piece, so the freeze does not imply theorem closure.

## 3. Face, tri-state, and branch checks

An independent exhaustive truth-table script checked 1,792 cases:

- 128 cases for the closed staircase conjunction;
- 128 cases for the genuinely new $\mathcal C_{18}$ conjunction;
- 1,536 cases for the normalized two-branch $\mathcal D_{18}$ predicate.

The checks included every combination of positive, zero, negative, and
unresolved irrational signs, together with both states of the rational ratio
gate. The implementation correctly has the following behavior:

- all faces of $\overline{\mathcal C}_{18}$ are closed;
- $K=k_2$ is excluded from genuinely new $\mathcal C_{18}$, while $K=k_5$
  is included;
- $K=1/(2\rho)$, $K=k_5$, and $K=U$ are excluded from $\mathcal D_{18}$;
- a false conjunction factor suppresses an irrelevant unresolved sign;
- a material unresolved sign returns `indeterminate`;
- the unresolved mandatory $\rho_*$ compact-domain gate is not overridden;
- an unresolved old $K=k_2$ attribution does not hide decisive coverage by
  the larger closed Round 18 staircase.

The piecewise upper floor was checked against its inherited definition. The
classifier selects $H_0$ below the certified $H_0=K_0$ switch, $K_0$ at and
above that switch until $5/6$, and the seam value $54/(1-\rho)^2$ inclusively
at $\rho=5/6$. If the switch sign is unresolved, it checks both possible
upper values and returns a side only when the minimum has a certified side.
No upper face is incorrectly admitted to the residual.

An independent 100-decimal reconstruction of $\rho_*$, $\rho_c$, $K_0$,
$H_0$, $U$, $z_\rho$, and $k_5$ was compared with the executable classifier
on 182 rational points spanning all active ratio branches, both residual
components, the endpoint regions, the seam, and the all-ratio high-frequency
owner. Every status and residual-piece label agreed.

## 4. Regressions and method walls

All four corners of each closed box $B_0$ and $B_1$ were checked, for eight
corner checks total. Every corner is in the old closed $\mathcal C_{17}$
band, is analytically covered by $\mathcal A_{18}$, and is outside
$\mathcal D_{18}$. The monotone worst faces are also the accepted ones:
the $z_\rho$ lower comparison is weakest at largest $\rho$ and smallest $K$,
while the $k_2$ upper comparison is weakest at smallest $\rho$ and largest
$K$. Hence the full boxes, not merely sampled corners, are absorbed. Their
certificate labels remain regression evidence and neither box is subtracted
again. Consequently $\mathcal U_{18}=\mathcal D_{18}$.

The signs of $k_5$, $2z_\rho$, and $k_6$ are computed independently. An
independent rational bracket crossed each of the $2z_\rho$ and $k_6$ walls at
$\rho=1/2$; both sides remained decisively in the same post-$k_5$ residual
piece. The accepted local signs at $\rho_c$ independently returned

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
$$

Neither method wall participates in membership, and no global ordering or
crossing threshold is encoded.

## 5. Executed validation

~~~text
python computations/round19_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round19_residual_mask.py -q
python -m compileall -q computations/round19_residual_mask.py computations/tests/test_round19_residual_mask.py
independent exhaustive truth-table and point/face script
independent B0/B1 eight-corner script
~~~

Results:

- classifier self-check: **PASS**, 13 checks;
- focused tests: **PASS**, 37 tests;
- bytecode compilation: **PASS**;
- independent truth tables: **PASS**, 1,792 cases;
- independent rational-point comparison: **PASS**, 182 points;
- exact inherited faces and both box absorptions: **PASS**;
- irrelevant $2z_\rho$ and $k_6$ wall crossings: **PASS**.

## 6. Scope conclusion

The three artifacts are a faithful residual freeze and nothing more. They
contain no Round 19 proof candidate, new spectral estimate, new Bessel-zero
dependency, proposed threshold, global wall ordering, finite-window
certificate, or target-status promotion. They satisfy the canonical A1
pre-candidate gate and are suitable for hashing into the Round 19 freeze
record.
