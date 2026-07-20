# Approach Registry

This file is workflow metadata for portfolio discovery.  It is not a source of
mathematical status and cannot override `state/proof_obligations.yml`.

## Current discovery target

Resolve the literal four-dimensional weighted aggregate on the complete strict
active domain:

$$
\mathrm{WT}_4
=W_4-P_4^{<}
=\mathcal B_4(A)+\sum_{a\ge1}aD_A(a)\ge0.
$$

A resolution is either a complete proof or an exact counterexample.  A
discovery wave may also return a genuinely new bounded lemma or mechanism, but
that does not change the status of the aggregate.

## Disposition meanings

- `unexplored`: no current artifact develops the mechanism.
- `active`: an independent attempt is currently justified.
- `promising`: a new bounded lemma or mechanism survived initial falsification.
- `blocked`: the route repeats a theorem-strength gap or loses a load-bearing
  correlation; reopen only with a materially new mechanism.
- `falsified_route`: a sufficient reduction in this family has an exact
  counterexample; this does not falsify the literal target unless stated.
- `promoted_to_obligation`: the route supplied a bounded claim accepted into
  the proof-obligation certification pipeline.

## Registry

| ID | Mechanism | Disposition | Strongest current artifact | First gap or next falsification test |
|---|---|---|---|---|
| `WT4-DIRECT-LAYER` | Direct layer-cake or inverse-level-set comparison of $W_4$ and $P_4^{<}$ | active | Exact identity $P_4^{<}=\sum a^2q_a$ | Seek a monotone transport or moment comparison that never introduces shifted-tail signs |
| `WT4-POINTWISE-D` | Prove or falsify the stronger statement $D_A(a)\ge0$ in $d=4$ | active | Round 47 diagnostics found no resolved negative $D_A(a)$ | Derive an analytic sign mechanism or an exact negative record; finite positive searches are not proof |
| `WT4-COMPONENT-U` | Charge maximal negative $D_A$ components with neighboring bonus and positive tails | active | Round 47 exact component identity, lead allocation, and structural-pass final audit | Prove the correlated component inequality without independently worst-casing shelf, terminal, and action-drop data |
| `WT4-BONUS-KERNEL` | Integral-kernel or total-positivity comparison using the common action-drop measure | unexplored | Exact cell polynomial and integration-by-parts identities | Identify a signed integrated kernel or variation-diminishing statement |
| `WT4-DISCRETE-MAJOR` | Discrete convexity, majorization, summation by parts, or transport between action cells | unexplored | Exact adjacent recurrence and weighted summation identity | Find a global transport invariant that permits compensation across cells |
| `WT4-GENERATING` | Generating functions or harmonic-branching representations | unexplored | Exact $d=4$ branching weights and positive bonus | Produce a coefficientwise, moment, or transform positivity statement |
| `WT4-ALT-SPECTRAL` | Direct spectral or geometric counting formulation avoiding the shifted-tail decomposition | unexplored | Audited shell phase proxy and strict count | State an exact alternative count with all wall and multiplicity conventions preserved |
| `WT4-FALSIFICATION` | Exact adversarial search against the literal target and every proposed stronger lemma | active | No literal negative in Round 47; cell-self-charge route exactly falsified | Target action walls, thin shells, moderate frequency, interfaces, and any new route-specific equality face |

## Frozen route counterexamples

- The cell-self-charge inequality
  $\mathcal B_{4,a}+a(a+1)L_a/2\ge0$ is a `falsified_route` at
  $(\rho,K,a)=(9/10,40,29)$ while the literal aggregate is positive.
- Negative values of a sufficient surrogate are never classified as literal
  aggregate counterexamples unless the exact implication is proved.

## Registry update rule

After each independent wave, the root records for every attempted family:

1. the frozen artifact;
2. the new mechanism, if any;
3. the first unsupported implication;
4. literal and route-specific falsification outcomes; and
5. whether to continue, block, redirect, or promote the family.

Do not replace this table with a single favored route.  Once a route is
promoted, its mathematical work continues under `state/proof_obligations.yml`.
