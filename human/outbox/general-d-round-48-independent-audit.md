# Round 48 fresh state and scope audit

Verdict: **PASS on the final Round 48 tree.**

The audit independently checked the human target packet, protocol, both lemma
packets, all lead/clean-room/adversarial artifacts, the interval
counterexample and symbolic replays, the proof-obligation graph, and the
approach registry.

## Bounded promotions

Both new `proved_internal` nodes have distinct lead, clean-room, and
adversarial roles.

- For the full-outer cell, the kernel split, monotonicity directions,
  coefficients, (h_0\le1/2), literal (N<r), and
  (Q_N(N)=19N/48+27/128) reconstruct exactly, including (N=0), integer
  (r), (n=1), and the interface endpoint.
- For the deep-inner cell, the shell-mixture and independent
  (phi)-monotonicity curvature proofs, tangent estimates, endpoint
  extension, and strict-ceiling arithmetic reconstruct exactly, including
  (n-1=A(\mu/\sqrt2)) and a cell ending at (A(0)).

The inverse-layer exchange produces (S_2(N_n)) with
(N_n=\lceil\xi(n-1/4)\rceil-1); no multiplicity, bonus, or endpoint term is
duplicated.

## Scope

The graph correctly separates the scoped
`SHELL-general-d-weighted-aggregate-d4` node from the all-dimensional
`SHELL-general-d-weighted-aggregate` node.  The scoped node remains
`proposed` and has no theorem implication.  The all-dimensional aggregate and
`TARGET-shell-general-d` remain `proposed`.

The first unsupported global implication is explicitly open: the two cell
lemmas do not imply global QCL or \(\mathrm{WT}_4\) without signing or
compensating the shallow-inner, interface-straddling, truncated, and
unused-top residuals.

## Computation and state checks

The corrected moment primitive differentiates exactly and has endpoint value
(3R^4/64).  Directed Arb reproduces a negative continuous quarter-node
margin and a positive literal QCL margin at the exact rational point.  The
artifact uses the protocol class `interval_certified`, separately labels the
claim as a route counterexample, and records reproducible code and payload
hashes.

All relevant IDs are unique, every referenced Round 48 evidence path exists,
the graph validator passes, and the synchronized Round 48 TeX sources contain
no control-character corruption.

No further state correction or status change is authorized by this audit.
