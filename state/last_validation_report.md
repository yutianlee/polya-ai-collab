# Last State Patch Validation

Round: 3 fixed-$\rho$ continuation

Run: `polya-main`

Judge: `rounds/polya-main/round_003/judge/judge-003-fixed-rho.md`

Date: 2026-07-12

Status: applied.

Graph hygiene: `rounds/polya-main/round_003/judge/judge-003-fixed-rho-cleanup.md` removed the conditional spectral-count dependency from the pure lattice proxy and refreshed the fixed-$\rho$ theorem statement. No verdict changed.

Created:

- `SHELL-low-interface-fixed-rho-high-energy` — `proved_internal`.

Promoted:

- `SHELL-weighted-lattice-fractional` — `proved_internal` for every fixed $0<\rho<1$ and $K\ge K_0(\rho)$;
- `SHELL-lattice-count` — `derived_under_assumptions`, pending separated-spectrum completeness;
- `SHELL-fixed-rho-high-energy` — `derived_under_assumptions` for the same reason.

Still open or diagnostic:

- `SHELL-sturm-liouville-completeness`;
- `SHELL-rho-uniformity` and its compact/endpoint components;
- `COMP-certified-bessel`.

Rejected proof route:

- a generic $C^1$, concave-to-convex, $\operatorname{Lip}_{<1/2}$ tail theorem without shell-specific curvature; an exact counterexample is recorded in the adversarial review.

Round score: 7/10. The main fixed-$\rho$ high-energy weighted analytic bottleneck is solved with an explicit threshold, but no full shell Pólya theorem is proved.
