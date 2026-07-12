# Last State Patch Validation

Round: 3
Run: `polya-main`
Judge: `rounds/polya-main/round_003/judge/judge-003.md`
Date: 2026-07-12

Status: applied.

Created:

- `SHELL-weighted-lattice-scaffold` — `proved_internal`;
- `SHELL-high-angular-shifted-tails` — `proved_internal`;
- `SHELL-low-interface-shifted-tails` — `open` and the active bottleneck;
- `SHELL-thin-width-phase-zero` — `proved_internal`.

Updated:

- `SRC-FLPS-balls` — `proved_external_dependency`;
- `SHELL-weighted-lattice-fractional` — remains `open`, blocked only by the low-interface tails;
- `SHELL-rho-one-endpoint`, `FLPS-disk-ball-reproduction`, `SHELL-rho-zero-endpoint`, and `COMP-certified-bessel` — evidence and next actions refined.

Rejected proof routes:

- floor-free weighted phase summation;
- treating the blanket quarter slack as uniformly lower order;
- treating the floating shifted-tail grid as proof.

Round score: 4/10. Exact reductions, high-angular tails, and the thin-width phase-zero region are closed. The mixed-curvature low tails and every theorem-level shell claim remain open.
