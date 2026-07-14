# Round 21 Residual-Mask Independent Audit

Verdict: **PASS. First issue: none.**

This is a pre-candidate audit of the frozen accepted-Round-20 residual only.
No Round 21 route proof, certificate result, proof candidate, or proposed
empty-residual theorem was used to derive the set below. This audit releases
the exact frozen residual bookkeeping for a later, separately frozen Round 21
candidate; it proves no new spectral estimate and changes no obligation
status.

## 1. Frozen bytes and accepted baseline

The supplied bundle is commit
`4bff6b7c22be0784657e5e79a9b8d03f5d082e1e`. I reproduced all four frozen
SHA-256 identities both from that commit and from the current bytes:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `computations/round21_residual_mask.py` | `1f6254b699519212ae8bd835b789b1002db78318d30bf347d8a0f60a14cbaa38` |
| `computations/tests/test_round21_residual_mask.py` | `6703899a0ba89021089c6f3407a836e3cfcfb54960f81c4e0261c5b5fdf57477` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |

The manifest baseline is the extant ancestor commit
`e739a1cfcc5ce6647d70f2ddbc09598da4f496aa`. I independently enumerated all
31 authenticated input paths. The graph and prompt identities were computed
from their Git blobs at that baseline, as the permanent-test policy requires:

| mutable state path | reproduced baseline-blob SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd` |
| `state/next_round_prompts.md` | `61341748ef07a6e937f752140b407a83576ae69c62061c1c28ae488acf43e4d2` |

Every one of the other 29 immutable paths exists, is tracked, stays within
the repository root, and has live SHA-256 equal to its manifest value. The
two mutable live paths also happened to match the baseline during this audit,
but correctness does not depend on that coincidence. An in-memory simulated
future mutation changed each live hash while leaving the authenticated
baseline blob unchanged, confirming that the historical-byte policy is
implemented in the correct direction. All 31 one-nibble expected-hash
mutations were rejected.

The authenticated Round 20 judge says that the complete lower residual, the
closed staircase through $k_{11}$, and the all-frequency optical range from
$39/50$ were promoted, while the resulting residual remains nonempty. The
applied graph has the corresponding Round 20 evidence and keeps
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` open. It also keeps `COMP-certified-bessel`
`diagnostic_only`. Thus neither the graph nor the judge supplies a hidden
Round 21 promotion.

## 2. Independent exact subtraction

Before Round 20, the authenticated residual was

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
$$

The accepted Round 20 union adds exactly:

1. both lower components of $\mathcal D_{19}$;
2. the closed staircase
   $\rho_c\leq\rho\leq7/8$, $z_\rho\leq K\leq k_{11}(\rho)$;
3. the all-frequency optical theorem
   $39/50\leq\rho<1$, $K\geq0$.

Intersecting those theorems with the old complement shows that the genuinely
new subset is

$$
\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K\leq k_{11}(\rho)\}\\
&\cup\{39/50\leq\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}
$$

Therefore $\mathcal A_{20}=\mathcal A_{19}\cup\mathcal C_{20}$ and direct
set subtraction gives the single cell

$$
\boxed{
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

This agrees with both independently implemented paths in the frozen code:
the complement classifier that adds the three accepted Round 20 theorem
domains to opaque $\mathcal A_{19}$, and the direct normalized conjunction.
A deterministic independent 100-decimal-digit run compared them at 3,514
rational points. It found 2,155 covered, 1,284 residual, and 75 outside-scope
points, with no disagreement or unresolved sampled point.

## 3. Upper floor and sign directions

On the live ratio interval the inherited competing upper branches cannot be
eligible. A 256-bit outward Arb reconstruction gave

$$
\rho_c-\omega_0
\in[0.0283047806541836130574157432188\mathbin{+/-}3.13\cdot10^{-32}]>0,
$$

and the exact rational inequality is
$5/6-39/50=4/75>0$. Hence
$\rho\geq\rho_c>\omega_0$ excludes $H_0$, while
$\rho<39/50<5/6$ excludes the seam branch. The only eligible upper floor is
$K_0$, so $U=K_0$ exactly. The inherited branch selector and an independent
100-digit $K_0$ evaluation agreed on all 2,689 live-ratio probes.

The executable comparisons have the correct directions:

| expression | positive/negative meaning used by the residual |
|---|---|
| $\rho(1+2\pi)-1$ | nonnegative means $\rho\geq\rho_c$ |
| $50\rho-39$ | negative means $\rho<39/50$; zero is optical-owned |
| $\pi^2+(132-K^2)(1-\rho)^2$ | negative means $K>k_{11}(\rho)$ |
| $K_0(\rho)-K$ | positive means $K<K_0(\rho)$ |

Exact and outward-Arb probes on both sides of every expression passed. The
retained witness is also strict. At $\rho=1/2$, outward evaluation proves
$16-\pi^2>0$ and

$$
K_0(1/2)-64
\in[496.591285330709688552494261689\mathbin{+/-}1.97\cdot10^{-29}]>0.
$$

Consequently

$$
\rho_c<\frac12<\frac{39}{50},
\qquad k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2),
$$

and $(1/2,30)$ is classified in `one-piece-d20`. The residual frozen here is
therefore nonempty.

## 4. Faces, indeterminacy, and inherited owners

The complete face assignment is reproduced exactly:

| face | owner |
|---|---|
| $\rho=\rho_c$ | residual only strictly above $k_{11}$; staircase below and on $k_{11}$ |
| $\rho=39/50$ | inclusive all-frequency optical theorem |
| $K=k_{11}(\rho)$ | closed Round 20 staircase |
| $K=K_0(\rho)=U(\rho)$ | inherited fixed-ratio high-energy theorem |
| $\rho=\rho_*$ | inherited complete small-hole endpoint |
| $\rho=7/8$ | inherited complete thin endpoint, also overlapped by optical coverage |
| $K=295^2$ | inherited Round 16 all-ratio high-frequency theorem |
| $K=0$ on optical ratios | optical equality face |

I evaluated the accepted-cover predicate against an independently generated
supervaluation truth table on all 1,152 combinations of definite/unresolved
lower, ratio, staircase, optical, and thin-face inputs. I similarly evaluated
the normalized $\mathcal D_{20}$ conjunction on all 192 sign combinations.
Every row agreed. In particular, a definite false factor suppresses irrelevant
unknowns, while a material unresolved irrational comparison remains
`indeterminate`; no midpoint guess occurs.

All four closed corners of each of $B_0$ and $B_1$ remain analytically
covered and retain their original certificate labels. Since
$B_0,B_1\subset\mathcal A_{19}\subset\mathcal A_{20}$, neither box is
subtracted again and the theorem-wise uncovered set is exactly
$\mathcal U_{20}=\mathcal D_{20}$. Direct checks also retained the thin
endpoint, fixed-ratio high-energy owner, global $K=295^2$ owner, and optical
$K=0$ owner without relabelling an older owner when the old classifier had
already decided the point.

## 5. Scope and mutation audit

AST/import inspection found no Round 21 certificate or proof module imported
by the classifier: its only project dependency is the accepted Round 20
residual module. None of the compact-proxy, aggregate-tail, exploratory
closure, or certificate-report names occurs in the classifier source. The
manifest scope flags all four of `round21_certificate_encoded`,
`round21_candidate_encoded`, `successor_residual_proposed`, and
`new_spectral_estimate` as false, while recording the nonempty witness.
Thus the frozen bytes encode neither a candidate nor an empty successor
residual.

Five in-memory mutations, made without changing any supplied file, were each
rejected by a focused permanent test:

- a one-nibble baseline graph hash change;
- escalation of the candidate-scope flag;
- inclusion of the $K=k_{11}$ residual face;
- exclusion of the $\rho=39/50$ optical face;
- reversal of the $K_0-K$ sign.

Together with the 31 manifest-hash mutations and the simulated mutable-live
state changes, these tests exercise both authentication and the most
dangerous face/sign failures.

## 6. Executed verification and hygiene

The following checks were rerun against the frozen bytes:

~~~text
python -m py_compile computations/round21_residual_mask.py \
  computations/tests/test_round21_residual_mask.py
PASS

python -m computations.round21_residual_mask --self-check --manifest
PASS: 11 distinct self-checks; manifest emitted

python -m pytest computations/tests/test_round21_residual_mask.py -q
47 passed

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
Graph OK

python -m pytest -q
320 passed, 1 xfailed, 10 subtests passed
~~~

All manifest paths were unique under Windows case folding, relative,
repository-contained, and tracked. Strict UTF-8 decoding of the four frozen
artifacts found no BOM, replacement character, forbidden control byte,
trailing whitespace, or missing final newline. Compilation, path checks, and
`git diff --check` passed.

## Final decision

**PASS. First issue: none.** The exact frozen bytes correctly implement
$\mathcal A_{20}=\mathcal A_{19}\cup\mathcal C_{20}$ and the nonempty
one-piece residual $\mathcal D_{20}$ above. They preserve every ratio and
frequency face, inherited endpoint and high-energy owner, absorbed regression
box, and strong-Kleene rule. They contain no Round 21 proof or successor
claim. These exact bytes may be used as the independently audited residual
input to a separately frozen Round 21 candidate.
