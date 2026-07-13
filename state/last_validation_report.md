# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 7

## State patch

- Source: `rounds/polya-main/round_007/judge/judge-007.md`.
- The embedded State Patch was validated before application and applied
  exactly once at round index 7.
- Created `SHELL-low-interface-small-hole` as `proved_internal`, recording
  the independently reviewed Round 3 shifted-tail theorem explicitly in the
  graph.
- Promoted `SHELL-rho-zero-endpoint` to `proved_internal`.
- Removed the small-hole endpoint from the blockers of
  `SHELL-rho-uniformity`; its sole remaining blocker is `SHELL-rho-compact`.
- Kept `SHELL-rho-compact`, `COMP-certified-bessel`,
  `SHELL-rho-uniformity`, and `TARGET-shell-d3` open.
- Rejected pointwise ball-root convergence, bare ball domain monotonicity,
  and subtraction of one-sided ball Pólya estimates as substitute proofs.

## Review gates

- Frozen small-hole endpoint proof: PASS.
- Isolated clean-room reconstruction from the reduced packet: PASS.
- Independent adversarial constants, walls, and route audit: PASS.
- Final dependency and integration audit: PASS.
- Historical low-interface incumbent, clean-room review, and adversarial
  review rechecked as permitted inputs: PASS.

## Mechanical validation

- Proof-obligation graph after application and Round 8 routing update: PASS.
- Python regression suite: 22 passed.
- Python compile check: PASS.
- Git diff whitespace check: PASS.
- No computation is used in the Round 7 theorem.

## Authoritative theorem boundary

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}
=0.0310668242700667\ldots .
$$

Round 7 proves

$$
\boxed{
0<\rho\le\rho_*,
\qquad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The low-$\mu$ range $\rho K\le1/2$ and the reviewed high-energy range
$K\ge C_*/(\omega_0-\rho)$ overlap exactly when $\rho\le\rho_*$. At the
endpoint they meet at

$$
K_*=\frac1{2\rho_*}=16.0943389531371\ldots,
$$

with equality included on both sides. The apparent small-hole certification
box is empty.

Together with Round 6, both endpoint neighborhoods are now proved for all
$K$:

$$
\rho\in(0,\rho_*]\cup[1-2^{-18},1).
$$

The global all-$\rho$ shell theorem remains open only on the explicit compact
interval $[\rho_*,1-2^{-18}]$, where a uniform analytic threshold, bounded
certification, and the final theorem-level audit are still required.
