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
| `WT4-DIRECT-LAYER` | Direct layer-cake or inverse-level-set comparison of $W_4$ and $P_4^{<}$ | promising | Round 48 exact inverse-layer/QCL identity; full-outer and deep-inner cells certified positive | Sign complete shallow-inner cells, the interface cell, terminal truncation, and their compensation with the unused top interval |
| `WT4-POINTWISE-D` | Prove or falsify the stronger statement $D_A(a)\ge0$ in $d=4$ | active | Exact inverse sawtooth identity; complete slabs on the increasing branch of $1/\sigma$ are positive | The pointwise kernel is $1/\sigma$, not the QCL kernel $\xi^2/\sigma$; prove a literal pointwise sign or find an exact negative without transferring the slab lemma |
| `WT4-COMPONENT-U` | Charge maximal negative $D_A$ components with neighboring bonus and positive tails | active | Round 47 exact component identity, lead allocation, and structural-pass final audit | Prove the correlated component inequality without independently worst-casing shelf, terminal, and action-drop data |
| `WT4-BONUS-KERNEL` | Integral-kernel or total-positivity comparison using the common action-drop measure | promoted_to_obligation | Deep-inner convexity cell passed Round 48 certification; exact shell-mixture and phase recursion retained | Pure total positivity fails for atomic measures; seek a uniform-interval mechanism only in the residual shallow band |
| `WT4-DISCRETE-MAJOR` | Discrete convexity, majorization, summation by parts, or transport between action cells | promising | Exact row-cone reserve $\Theta$, positive row surplus, and fixed-$K$ adverse-wall reduction | Prove $\Theta$ or the safe weakened reserve on every adverse wall; keep the stronger-route/literal-target distinction exact |
| `WT4-GENERATING` | Generating functions or harmonic-branching representations | promoted_to_obligation | Full outer inverse-action cell passed Round 48 certification with an explicit $19N/48+27/128$ reserve | Determine whether any kernel comparison survives the shallow-inner curvature change |
| `WT4-ALT-SPECTRAL` | Direct spectral or geometric counting formulation avoiding the shifted-tail decomposition | falsified_route | Directed interval counterexample to the unrestricted continuous quarter-node polynomial comparison | Redirect only to the literal discrete QCL; the counterexample is interface-straddling and leaves QCL positive |
| `WT4-ACTION-FLOW` | Differentiate chamber supplies and audit action-wall jumps | promising | Exact upward-jump orientation, unique wall tangency, and finite adverse-face reduction on compact $K$ slabs | Tangential derivatives have mixed signs; find a face invariant for the shallow/interface/truncated residual |
| `WT4-FALSIFICATION` | Exact adversarial search against the literal target and every proposed stronger lemma | active | No literal, QCL, or row-cone negative in Round 48; continuous quarter-node route interval-falsified | Target the residual shallow-inner band, interface collision, terminal truncation, thin shells, and exact adverse wall limits |

## Frozen route counterexamples

- The cell-self-charge inequality
  $\mathcal B_{4,a}+a(a+1)L_a/2\ge0$ is a `falsified_route` at
  $(\rho,K,a)=(9/10,40,29)$ while the literal aggregate is positive.
- The unrestricted continuous quarter-node comparison
  $p(\xi(n-1/4))\le\int_{n-1}^n\xi(t)^3/3\,dt$ is a
  `falsified_route` at the exact rational Round 48 interface cell recorded in
  `rounds/polya-main/round_048/diagnostics/continuous-quarter-node-counterexample.md`.
  The literal discrete QCL margin is positive at the same point.
- A pure total-positivity implication for arbitrary positive atomic shell
  measures is false.  Any continuation must use the genuine uniform shell
  interval and may not cite generic TP as the missing sign.
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
