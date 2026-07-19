# Round 18 Residual-Mask Freeze

Date: 2026-07-14

Decision: **FROZEN / PASS**.

This record releases the exact post-Round-17 residual packet for Round 18
proof work. It freezes set bookkeeping only; it is not a new analytic or
certified theorem.

Baseline commit:
`1caf24a0f0732038e9d162990dd3c2201daad85d`.

## Frozen artifacts

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `computations/round18_residual_mask.py` | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| `computations/tests/test_round18_residual_mask.py` | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| accepted graph `state/proof_obligations.yml` | `3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c` |
| accepted Round 17 judge | `769dc256aa97dc8da093bdead8a020033904c115ff256ae60a708a31f90dbadd` |
| frozen Round 17 packet | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| frozen Round 17 classifier | `b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b` |

## Derivation lock

The classifier imports the frozen Round 17 predicate and applies only

$$
\mathcal A_{17}
=\mathcal A_{16}\cup\overline{\mathcal C}_{17},
$$

where

$$
\overline{\mathcal C}_{17}
=\left\{\rho_c\le\rho\le\frac78,
\ z_\rho\le K\le k_2(\rho)\right\}.
$$

It then cross-checks the exact normalized complement

$$
\mathcal D_{17}
=\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\le\rho<\frac78,
\ k_2(\rho)<K<U(\rho)\right\}.
$$

Every frequency face in this residual formula is strict. The
$\rho=\rho_c$ slice is assigned to the post-$k_2$ piece. The exact upper
floor and implicit $\rho_{HK}$ switch remain those authenticated by the
Round 17 packet.

The certificates on $B_0$ and $B_1$ remain independently valid regression
evidence, but the packet reproduces the exact closed-face proof that

$$
B_0\subset\mathcal C_{17},
\qquad
B_1\subset\mathcal C_{17}.
$$

Therefore neither box is subtracted again and
$\mathcal U_{17}=\mathcal D_{17}$.

The inequality

$$
\mathcal W(\rho_c,k_2(\rho_c))<9
$$

is frozen only as an obstruction to the uniform crude-cap-$9$ continuation.
It is not a counterexample and not a new spectral assertion.

## Validation transcript

~~~powershell
python computations/round18_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round18_residual_mask.py -q
python -m compileall -q computations/round18_residual_mask.py computations/tests/test_round18_residual_mask.py
~~~

Results:

- classifier self-check: **PASS**, 12 checks;
- focused suite: **PASS**, 24 tests and 10 subtests;
- bytecode compilation: **PASS**;
- 4096-bit near-face indeterminacy regressions: **PASS**;
- exact B0/B1 corner subsumption checks: **PASS**;
- normalized-complement inventory cross-check: **PASS**.

## Release rule

The three artifacts in the first three rows are immutable for this round.
Any correction requires a replacement packet, classifier, tests, and freeze
record with new hashes. Candidate work may cite these bytes only after
checking this record. An isolated reconstruction must not receive an
incumbent proof before its initial verdict.
