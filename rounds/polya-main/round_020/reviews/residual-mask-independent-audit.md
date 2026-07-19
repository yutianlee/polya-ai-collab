# Round 20 Residual-Mask Independent Audit

Verdict: **PASS**.

This was a strict pre-candidate audit of only the frozen residual packet,
classifier, and tests named below. No Round 20 proof
candidate or proof-exploration note was inspected or used. The audit releases
this exact residual mask for a separately frozen Round 20 candidate; it proves
no new spectral estimate and changes no theorem status.

## 1. Frozen-byte and baseline authentication

The three supplied SHA-256 identities were reproduced from current bytes:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |

The declared baseline is the extant commit
`658674117632d60990ac9b9046aa0fcff9e91a62`; it is an ancestor of the
current `HEAD`. I independently enumerated all 19 authenticated Round 19
input paths in the executable manifest. Every path is tracked, every live
SHA-256 equals its declared SHA-256, and every blob read with
`git show 658674117632d60990ac9b9046aa0fcff9e91a62:<path>` has the same
SHA-256. In particular, the two intentionally mutable state identities are

| mutable state path | baseline blob SHA-256 | live SHA-256 |
|---|---|---|
| `state/proof_obligations.yml` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` |
| `state/next_round_prompts.md` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` |

Thus the permanent Git-blob authentication policy is effective and the live
state also matched the release baseline during this audit.

## 2. Independent set reconstruction

The authenticated Round 18 residual is

$$
\mathcal D_{18}
=\{\rho_*<\rho<\rho_c,\ L(\rho)<K<U(\rho)\}
\cup
\{\rho_c\leq\rho<7/8,\ k_5(\rho)<K<U(\rho)\}.
$$

The accepted Round 19 cover added to the opaque $\mathcal A_{18}$ is exactly

$$
\mathcal P_{19}^{\rm low}
=\{\rho_0<\rho<\rho_c,\ L(\rho)<K\leq d\},
$$

$$
\overline{\mathcal P}_{19}^{\rm high}
=\{\rho_c\leq\rho\leq7/8,\ z_\rho\leq K\leq k_6(\rho)\}.
$$

The high cover overlaps the old cover through $k_5$ and meets the already
complete $\rho=7/8$ endpoint. Consequently its genuinely new high part is
$\rho_c\leq\rho<7/8$, $k_5<K\leq k_6$. The lower cover is genuinely new in
full. Therefore

$$
\mathcal A_{19}=\mathcal A_{18}\cup\mathcal P_{19}^{\rm low}
\cup\overline{\mathcal P}_{19}^{\rm high}
$$

and exact subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

Here

$$
\rho_0=1/\sqrt{337},\qquad
\rho_c=1/(1+2\pi),\qquad
L(\rho)=1/(2\rho),\qquad
d=\sqrt{337}/2,
$$

and the independently evaluated threshold order is
$\rho_*<\rho_0<\rho_c<7/8$. For $\rho>\rho_0$, $L(\rho)<d$, so deleting the
closed interval $L<K\leq d$ leaves precisely $d<K<U$. At
$\rho=\rho_0$, $L(\rho_0)=d$ and the added lower fiber is empty because its
ratio condition is strict; the ratio face therefore stays in the first
piece, with its frequency condition still strict. At $\rho=\rho_c$, the
closed high cover owns all frequencies through $k_6$, so that ratio face is
assigned to the third piece. The faces $K=L$, $K=d$, $K=k_6$, and $K=U$ are
all excluded from the residual, as required.

## 3. Upper floor, absorbed boxes, and nonemptiness

The executable does not replace or weaken the inherited upper floor. It
delegates to the authenticated classifier for

$$
U(\rho)=\min\left(
\{K_0(\rho)\}\cup
\{H_0(\rho):\rho<\omega_0\}\cup
\{54/(1-\rho)^2:\rho\geq5/6\}
\right).
$$

Independent high-precision comparisons agreed with the implementation on
the $H_0$, $K_0$, and inclusive seam branches. Targeted checks selected
`H0` at $\rho=9/100$, `K0` at $\rho=1/10$ and $1/2$, and `seam-54` at
$\rho=5/6$. At the exact seam, $K=1943$ is below $U=1944$, while
$K=1944=U$ is excluded. The inherited shared $H_0=K_0$ handling and all
other upper faces were also exercised by the full regression suite.

Because

$$
B_0\subset\mathcal A_{18}\subset\mathcal A_{19},\qquad
B_1\subset\mathcal A_{18}\subset\mathcal A_{19},
$$

adjoining or subtracting either regression box again cannot alter the
complement. Hence the theorem-wise uncovered set is exactly
$\mathcal U_{19}=\mathcal D_{19}$. All eight closed corners of $B_0$ and
$B_1$ were independently classified as analytically covered with their
original certificate labels retained.

The exact point $(\rho,K)=(1/2,30)$ was classified in the third residual
piece. In particular, $\rho_c<1/2<7/8$, $k_6(1/2)<30$, and the certified
upper-floor comparison gives $30<U(1/2)$. Thus $\mathcal D_{19}$ is
nonempty and the freeze makes no theorem-closure claim.

## 4. Independent executable audit

I did not rely only on the supplied examples.

- An independently written strong-Kleene evaluator matched
  `c19_membership_from_signs` on all **4,608** combinations of definite and
  unresolved ratio/band signs and the thin-endpoint flag.
- A direct three-disjunct evaluator matched
  `d19_membership_from_signs` on all **648** concrete sign rows compatible
  with $\rho_*<\rho_0<\rho_c<7/8$.
- All nine combinations of the two adjacent frequency tests at an
  unresolved $\rho_c$ were checked. Equal middle/high truth values settle
  the answer; differing values return `indeterminate`. Four additional
  mandatory-gate cases confirmed that an unresolved $\rho_*$ or $U$ gate
  is not overridden, while a definite false outer gate suppresses
  irrelevant unknowns.
- The exact rational signs $337\rho^2-1$, $2\rho K-1$, and
  $337-4K^2$ were rederived from positivity and agreed with the code.
- A deterministic independent **3,000-point** rational fuzz run used a
  separately coded 100-decimal-digit implementation of $\rho_*$,
  $\rho_0$, $\rho_c$, $L$, $d$, $z_\rho$, $k_6$, and every eligible branch
  of $U$. It compared the accepted Round 19 addition, normalized
  $\mathcal D_{19}$ predicate, full complement classification, and
  theorem-wise uncovered predicate. All comparisons passed. The resulting
  status distribution was 2,089 residual, 472 covered, and 439 outside the
  compact interval.

The complement classifier and the independently normalized predicate
therefore agree on decided points, equality ownership is correct, and no
material unknown sign is guessed.

## 5. Executed verification and hygiene

The following commands were rerun against the frozen bytes:

~~~text
python -m py_compile computations/round20_residual_mask.py \
  computations/tests/test_round20_residual_mask.py
PASS

python -m computations.round20_residual_mask --self-check
PASS: 10 distinct checks

python -m pytest computations/tests/test_round20_residual_mask.py -q
46 passed

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
Graph OK

python -m pytest -q
241 passed, 1 xfailed, 10 subtests passed
~~~

A strict UTF-8 byte scan of all three frozen artifacts found no forbidden
control byte, replacement character, BOM, or trailing whitespace; every
file has a final newline. `git diff --check` also passed.

## Final decision

**PASS.** The supplied hashes authenticate one coherent, proof-free Round
20 residual freeze. It exactly represents
$\mathcal A_{19}=\mathcal A_{18}\cup\mathcal C_{19}$ and the three-piece
$\mathcal D_{19}$ above, preserves every required face and tri-state rule,
retains $B_0/B_1$ only as absorbed regression evidence, and retains a
nonempty witness. A Round 20 proof candidate may now be frozen only against
these exact bytes and this exact residual.
