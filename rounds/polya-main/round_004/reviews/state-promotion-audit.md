# Round 4 state-promotion audit

## Verdict and audit limitation

The Round 4 spectral theorem passed all required gates:

- frozen packet: `state/lemma_packets/SHELL-sturm-liouville-completeness.md`;
- incumbent: `rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md`;
- isolated clean-room review: `rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md` (PASS);
- adversarial review: `rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md` (PASS).

The maximal conservative consequence is to promote the three bundled spectral obligations and the two fixed-$\rho$ results that were conditional only on them. It is **not** sufficient to promote the finite certificate, the $\rho$-uniform theorem, the shell theorem, or the quantitative Weyl source audit.

Three files requested for this audit do not exist in the workspace:

- `state/claim_ledger.md`;
- `state/dependency_graph.md`;
- `state/assumption_register.md`.

Accordingly, their synchronization could not be checked. The recommendations below are based on `state/proof_obligations.yml`, the frozen packet, the incumbent, both Round 4 theorem reviews, and the Round 2/3 judge and review record. If those three ledgers are required state artifacts, they should be restored or regenerated and validated against the accepted patch.

## Maximal conservative promotion table

| Obligation | Current status | Recommended status | Required scope/blocker action | Recommended next action |
|---|---|---|---|---|
| `SHELL-sturm-liouville-completeness` | `open` | `proved_internal` | No blocker removal is needed; add the four Round 4 proof artifacts as positive evidence. | Treat the unitary decomposition, exact domains, compact resolvent, radial completeness/simplicity, zero-energy exclusion, and multiplicity rule as discharged. |
| `SHELL-cross-product-formula` | `open` | `proved_internal`, **after restricting its statement to $d=3$** | Remove blocker `SHELL-sturm-liouville-completeness`. The frozen proof establishes $u=rR$, $\nu=\ell+1/2$, and multiplicity $2\ell+1$ only. | Use the proved positive-zero determinant characterization in the strict count and certified finite-window work. If a general-$d$ statement is desired, retain it as a separate open obligation requiring the transform $u=r^{(d-1)/2}R$. |
| `SHELL-count-floor-identity` | `derived_under_assumptions` | `proved_internal` | Remove blocker `SHELL-sturm-liouville-completeness`; retain dependencies on the now-proved $d=3$ determinant, exact phase representation, and phase monotonicity. | Use the endpoint-safe identity unconditionally; at $\Psi(K)=m\pi$ the channel count remains $m-1$. |
| `SHELL-lattice-count` | `derived_under_assumptions` | `proved_internal` | Remove blocker `SHELL-sturm-liouville-completeness`; sharpen the statement to the proved $d=3$, fixed-$\rho$, $K\ge K_0(\rho)$ analytic range. | Treat the high-energy spectral lattice bound as proved; do not extend it to the finite window or a uniform endpoint theorem. |
| `SHELL-fixed-rho-high-energy` | `derived_under_assumptions` | `proved_internal` | Remove blocker `SHELL-sturm-liouville-completeness`. All remaining dependencies are already proved/audited. | Use the explicit $K_0(\rho)$ theorem as the analytic high-energy half of the shell program; finite and endpoint-uniform closure remain separate. |

The $d=3$ restriction on `SHELL-cross-product-formula` is necessary for this promotion. The current general-$d$ formula is standard and plausible, but it is not the theorem reconstructed in Round 4. It must not be silently promoted from a three-dimensional proof.

## Downstream blocker cleanup

After the five promotions above, the following blocker removals are justified:

| Obligation | Remove blockers | Keep blockers / status |
|---|---|---|
| `TARGET-shell-d3` | `SHELL-lattice-count`, `SHELL-fixed-rho-high-energy` | Keep status `open`; keep `COMP-certified-bessel` and `SHELL-rho-uniformity`. |
| `SHELL-rho-compact` | `SHELL-lattice-count`, `SHELL-fixed-rho-high-energy` | Keep status `open`; keep `COMP-certified-bessel`. |
| `POLYA-program-target` | `SHELL-lattice-count` | Keep status `open`; keep `COMP-certified-bessel` and the open theorem dependency. |

No other current blocker list contains the newly discharged spectral bridge or either promoted high-energy obligation.

## Next-action-only updates

The following statuses should not change, but their current next actions become stale once the spectral bridge is accepted:

- `SHELL-exact-phase-rep`: remove the warning that spectral completeness is still separate; use the fixed sign convention in the now-proved spectral count and certificate.
- `SHELL-phase-monotonicity`: root indexing is now unconditional in the $d=3$ shell.
- `SHELL-weighted-lattice-fractional`: combine the already-proved proxy with the proved strict spectral identity; retain the explicit prohibition on finite-window or $\rho$-uniform extrapolation.
- `SHELL-thin-width-phase-zero`: through the proved count identity, $(1-\rho)K\le\pi$ now implies the actual strict shell spectral count is zero, not merely the phase proxy. The phase lemma itself need not acquire a new dependency or status.
- `SHELL-rho-one-endpoint`: describe the lower optical-width region as a proved spectral zero region; widths above $\pi$ and certified overlap remain open.
- `SHELL-rho-compact`: take an explicit compact-$\rho$ bound on $K_0(\rho)$ and concentrate on the interval certificate.
- `COMP-certified-bessel`: use the proved determinant spectrum, root simplicity, angular cutoff, and strict endpoint identity to design the certificate; retain `diagnostic_only` until every required interval artifact exists.
- `TARGET-shell-d3`: state that the spectral bridge and fixed-$\rho$ high-energy theorem are discharged; prioritize certified finite closure and $\rho$-uniformity.

## Obligations that must not be promoted

### `COMP-certified-bessel`

Keep `diagnostic_only`. Round 4 proves what must be counted, but supplies no interval script, command, root-enclosure report, coverage table, software metadata, or certificate. Its empty certification-artifact list is decisive.

### `TARGET-shell-d3`

Keep `open`. Round 4 removes a structural blocker only. The target still lacks a certified finite window and a uniform treatment of $\rho\to0,1$.

### `SRC-shell-weyl`

Keep `source_audit_required`. The new `sources/shell_weyl_bessel.md` discharges only the exact structural spectrum/DLMF component. The card explicitly leaves open:

- a one-sided Weyl remainder with exact convention and constants;
- uniformity at both $\rho$ endpoints;
- constants strong enough for Pólya;
- the finite-window certificate.

Add the source card and Round 4 reviews as positive evidence for the structural component, and change the next action to focus solely on these remaining quantitative items. Do not mark the whole source obligation proved.

### Other unchanged obligations

`SHELL-low-interface-shifted-tails` remains open as an all-$K$ strengthening; Round 3 proved only the fixed-$\rho$ high-energy substitute. `SHELL-rho-uniformity`, its three component obligations, and `SHELL-spherical-bessel-algebraic` also remain at their current statuses.

## Rejected claims to record

### 1. Cross-channel nondegeneracy from centrifugal ordering

Record a rejected claim such as `distinct-centrifugal-potentials-preclude-cross-ell-degeneracy`:

> Reject the assertion that different centrifugal potentials prohibit equality of eigenvalues from different angular channels. The Round 4 incumbent and adversarial review prove, by continuity in $\rho$, that $\lambda_{0,2}(\rho)=\lambda_{7,1}(\rho)$ for at least one $\rho\in(1/10,4/5)$. Orthogonal direct-sum multiplicities must be added at such coincidences.

This is a genuinely false claim, not merely an unproved shortcut.

### 2. Blockwise compactness alone

It is also prudent to reject the proof route `blockwise-compact-resolvent-implies-compact-infinite-direct-sum`:

> Compactness of every radial block does not by itself imply compactness of the infinite direct-sum resolvent. The shell proof additionally needs $\|(L_\ell+1)^{-1}\|\to0$, supplied here by $L_\ell\ge\ell(\ell+1)$.

## Final state boundary

After these recommendations, the strongest theorem-level conclusion is:

> For every fixed $0<\rho<1$, the strict $d=3$ shell counting function satisfies the Pólya bound for every $K\ge K_0(\rho)$.

No all-$K$, $\rho$-uniform, or certified shell Pólya theorem follows yet.

