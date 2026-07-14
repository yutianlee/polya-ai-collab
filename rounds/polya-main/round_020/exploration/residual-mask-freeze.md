# Round 20 Exact Residual-Mask Freeze

Status: **FROZEN / PASS**.

Baseline commit:
`658674117632d60990ac9b9046aa0fcff9e91a62`.

This record freezes only the pre-candidate set bookkeeping obtained by
adding the accepted Round 19 cover to the opaque accepted Round 18
classifier. It contains no Round 20 proof claim and was prepared without
using any Round 20 exploratory proof note.

## Frozen bytes

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |

The three artifacts above are immutable for this release. Any correction
requires replacement hashes and a replacement freeze record.

## Baseline and live-state authentication

At freeze time, both mutable live state paths were byte-for-byte identical
to their baseline Git blobs:

| artifact | baseline blob SHA-256 | live SHA-256 | equal |
|---|---|---|---|
| `state/proof_obligations.yml` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` | yes |
| `state/next_round_prompts.md` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` | yes |

Permanent tests authenticate these two identities from commit
`658674117632d60990ac9b9046aa0fcff9e91a62`, not from mutable live paths.
All other authenticated Round 19 artifacts are immutable committed files
and are checked directly. The authenticated chain includes the Round 19
residual packet/classifier/audit, candidate claim and freeze, clean-room and
constant reviews, cross-comparison, final adversarial referee, corrected
judge, State-Patch audit, and final derived-state audit.

## Exact accepted operation

The classifier imports `computations.round19_residual_mask.py` as the
opaque $\mathcal A_{18}$ base and adds exactly

$$
\left\{\rho_0<\rho<\rho_c,
\quad L(\rho)<K\le d\right\}
$$

and

$$
\left\{\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_6(\rho)\right\},
$$

where

$$
\rho_0=\frac1{\sqrt{337}},
\quad
\rho_c=\frac1{1+2\pi},
\quad
L(\rho)=\frac1{2\rho},
\quad
d=\frac{\sqrt{337}}2.
$$

No prospective Round 20 band, zero bound, threshold, or proof is encoded.

## Exact frozen residual

The complement calculation and an independent normalized predicate agree
on

$$
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0, L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c, d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8, k_6(\rho)<K<U(\rho)\}.
\end{aligned}
}
$$

Face assignments are exact:

- $\rho=\rho_0$ belongs to the first residual piece; $L(\rho_0)=d$ and
  the accepted lower-band fiber is empty there.
- $\rho=\rho_c$ belongs to the high piece; the accepted high band includes
  all frequencies through $K=k_6(\rho_c)$.
- $K=L$, $K=d$, $K=k_6$, and $K=U$ are excluded from the residual.
- $\rho=\rho_*$ and $\rho=7/8$ retain complete endpoint owners.
- $B_0$ and $B_1$ remain absorbed in $\mathcal A_{18}$ and are not
  subtracted again, so $\mathcal U_{19}=\mathcal D_{19}$.

The exact retained witness $(1/2,30)$ is classified in the third piece, so
the residual is nonempty and no theorem status changes.

## Tri-state and exact-arithmetic checks

For rational query points, the signs of

$$
337\rho^2-1,
\qquad
2\rho K-1,
\qquad
337-4K^2
$$

are exact. The inherited Arb escalation evaluates the irrational
$\rho_c$, $z_\rho$, $k_6$, and upper-floor signs. False factors suppress
irrelevant unresolved signs; mandatory unresolved compact gates remain
indeterminate. When the side of $\rho_c$ is unresolved, equal truth values
from the adjacent $K>d$ and $K>k_6$ tests settle membership; differing
truth values remain indeterminate.

The permanent truth tables check every included or strict face, rational
brackets around $\rho_0$ and $d$, B0/B1 absorption, all three residual
pieces, and deliberate indeterminacy at material irrational faces.

## Executed verification

~~~text
python -m py_compile computations/round20_residual_mask.py \
  computations/tests/test_round20_residual_mask.py
PASS

python -m computations.round20_residual_mask --self-check
PASS: 10 distinct checks

python -m pytest computations/tests/test_round20_residual_mask.py -q
46 passed

python -m pytest -q
241 passed, 1 xfailed, 10 subtests passed
~~~

A byte scan found no forbidden control characters or trailing whitespace in
the packet, classifier, or tests.

## Independent audit and release

The independent pre-freeze audit is
`rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md`,
SHA-256
`b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f`.
It did not use a Round 20 proof candidate. It reproduced every authenticated
hash and baseline blob, 4,608 candidate-cover truth rows, 648 normalized
residual rows, all mandatory tri-state cases, and 3,000 independent
100-digit rational/fuzz comparisons. It also reproduced B0/B1 absorption,
the nonempty witness, 46 focused tests, the complete lifecycle-aware suite,
graph validation, and byte hygiene. Its verdict is **PASS; first issue:
none**.

This exact residual mask is therefore released for a separately frozen
Round 20 candidate. The classification itself supplies no spectral proof.
