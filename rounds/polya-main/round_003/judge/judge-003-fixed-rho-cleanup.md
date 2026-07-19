# Round 3 Fixed-Rho Graph Cleanup

This patch separates the proved pure lattice inequality from the still-conditional spectral bridge and replaces the stale candidate-mechanism wording in the fixed-$\rho$ theorem obligation. It changes no mathematical verdict.

## State Patch

```json
{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "SHELL-weighted-lattice-fractional",
        "dependencies_removed": [
          "SHELL-count-floor-identity"
        ],
        "permitted_dependencies_removed": [
          "SHELL-count-floor-identity"
        ],
        "next_action": "Use this unconditional lattice-proxy inequality inside the separately conditional strict spectral count. Do not extend it to the finite window or a rho-uniform theorem without separate evidence."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "statement_tex": "For fixed 0<rho<1, let eta_rho=G_1(max{rho,1/2}), a_rho=2 pi rho/(1-rho), C_0=1+8 sqrt(2)/15, and K_0(rho)=((sqrt(a_rho)+sqrt(a_rho+4 eta_rho C_0))/(2 eta_rho))^2. Derive N_D(A_{rho,1},K^2) <= (2/(9 pi))(1-rho^3)K^3 for K>=K_0(rho) from the proved phase enclosure and weighted proxy, conditional on separated Sturm-Liouville completeness and the strict count identity.",
        "next_action": "Prove SHELL-sturm-liouville-completeness and promote the strict count bridge; do not call the conditional result a shell theorem before then."
      },
      {
        "id": "SHELL-count-floor-identity",
        "next_action": "The phase representation and monotonicity inputs are proved. Discharge SHELL-sturm-liouville-completeness, then promote this strict endpoint-aware count identity."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "TARGET-shell-d3",
        "reason": "No theorem status changes in this graph-hygiene patch."
      }
    ]
  }
}
```
