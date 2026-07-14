# Round 21 Exact Residual-Mask Freeze

Date: 2026-07-15

Status: **FROZEN FOR INDEPENDENT AUDIT / IMPLEMENTATION PASS**.

Baseline commit:
`e739a1cfcc5ce6647d70f2ddbc09598da4f496aa`.

This record freezes only the pre-candidate set bookkeeping obtained by
adding the accepted Round 20 cover to the opaque accepted Round 19
classifier. It contains no Round 21 certificate, route proof, candidate
theorem, proposed successor residual, or empty-residual claim.

## Frozen bytes

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `computations/round21_residual_mask.py` | `1f6254b699519212ae8bd835b789b1002db78318d30bf347d8a0f60a14cbaa38` |
| `computations/tests/test_round21_residual_mask.py` | `6703899a0ba89021089c6f3407a836e3cfcfb54960f81c4e0261c5b5fdf57477` |

The three artifacts above are immutable for this freeze. Any correction
requires replacement bytes and a replacement freeze record.

## Baseline authentication

At freeze time, the synchronized graph and next-round prompt matched their
Git blobs at the accepted baseline:

| artifact | baseline/live SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd` |
| `state/next_round_prompts.md` | `61341748ef07a6e937f752140b407a83576ae69c62061c1c28ae488acf43e4d2` |

The repaired Round 20 derived-state audit is
`rounds/polya-main/round_020/reviews/derived-state-replacement-audit.md`,
SHA-256
`671cee8be91964efe0294eba01494cf11065ddbafdad1cc8e9885520ff3e353c`,
with verdict **PASS; first issue: none**. The earlier failure remains
preserved at SHA-256
`9c7a0dc453eea72bc571b99a11743d23ab42d1910f18e2b20c1dd0780eb752f9`.

The executable manifest also authenticates the accepted Round 20 residual
packet, classifier, independent mask audit, proof-free claim and release
audits, isolated reconstruction and addendum, zero audit, final repaired
constant verifier and audit, both preserved A4 failures, cross-comparison,
fresh referee, judge, and State-Patch audit. Permanent tests read mutable
graph and prompt identities from the baseline Git commit and check all
immutable evidence against its live bytes.

## Exact accepted operation

The classifier imports `computations/round20_residual_mask.py` as the opaque
$\mathcal A_{19}$ base and adds only the three accepted Round 20 domains:

$$
\mathcal D_{19}^{\rm low},
$$

$$
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_{11}(\rho),
$$

and

$$
\frac{39}{50}\le\rho<1,
\qquad
K\ge0.
$$

The exact genuinely new subset of $\mathcal D_{19}$ is

$$
\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K\le k_{11}(\rho)\}\\
&\cup\{39/50\le\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}
$$

No prospective Round 21 result is imported or encoded.

## Exact frozen residual

On the live ratio interval, the accepted branch inequalities

$$
\rho\ge\rho_c>\omega_0,
\qquad
\rho<\frac{39}{50}<\frac56
$$

exclude the $H_0$ and seam branches, so $U(\rho)=K_0(\rho)$ exactly.
Independent complement and normalized predicates agree on

$$
\boxed{
\mathcal D_{20}
=\left\{\rho_c\le\rho<\frac{39}{50},
\quad k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

Face assignments are exact:

- $\rho=\rho_c$ is included only strictly above $k_{11}$.
- $\rho=39/50$ is optical-owned and excluded.
- $K=k_{11}(\rho)$ is staircase-owned and excluded.
- $K=K_0(\rho)=U(\rho)$ is inherited-high-energy-owned and excluded.
- $\rho=\rho_*$ and $\rho=7/8$ retain their complete endpoint owners.
- $K=295^2$ retains the Round 16 all-ratio high-frequency owner.
- $B_0$ and $B_1$ remain absorbed in the older analytic cover and are not
  subtracted again, so $\mathcal U_{20}=\mathcal D_{20}$.

The strict witness

$$
k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2)
$$

keeps $(1/2,30)$ in $\mathcal D_{20}$. The residual is nonempty in this
freeze, and every theorem-level target remains open.

## Exact signs and indeterminacy

For rational query points, $50\rho-39$ decides the optical face exactly.
The accepted precision-escalated Arb policy evaluates

$$
\rho(1+2\pi)-1,
\qquad
\pi^2+(132-K^2)(1-\rho)^2,
\qquad
K_0(\rho)-K.
$$

The normalized classifier applies strong-Kleene conjunction to the four
strict/inclusive conditions defining $\mathcal D_{20}$. A false face
suppresses irrelevant unknowns; otherwise a material unresolved irrational
comparison returns `indeterminate`. On every decided live-ratio query, the
inherited upper-floor classifier is independently required to select `K0`
and agree with the direct $K_0-K$ sign.

## Executed verification

~~~text
python -m py_compile computations/round21_residual_mask.py \
  computations/tests/test_round21_residual_mask.py
PASS

python -m computations.round21_residual_mask --self-check --manifest
PASS: 11 distinct checks; all 31 authenticated file identities reproduced

python -m pytest computations/tests/test_round21_residual_mask.py -q
47 passed

python -m pytest -q
320 passed, 1 xfailed, 10 subtests passed
~~~

The focused suite exhausts the pure $\mathcal D_{20}$ tri-state table and
checks all requested faces, the exact rational witness, deliberate
indeterminacy at $\rho_*$, $\rho_c$, $z_\rho$, $k_{11}$, and $K_0$, optical
short-circuiting, inherited owners, B0/B1 absorption, and a rational
complement-versus-normalized grid.

## Independent-audit gate

This record freezes the three hashed implementation artifacts for a fresh
independent residual-mask audit. It does not itself release a proof
candidate. The auditor must authenticate all four supplied files, reproduce
the accepted-state manifest and exact subtraction without using any Round 21
route proof, and return **PASS** or **FAIL** with the first issue.

Only a later PASS audit may release these exact bytes for a separately
frozen proof-free candidate. The classification itself supplies no spectral
proof.
