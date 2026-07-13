# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 6

## State patch

- Source: `rounds/polya-main/round_006/judge/judge-006.md`.
- The embedded State Patch was validated before application and applied
  exactly once at round index 6.
- Created and promoted `SHELL-thin-action-aggregate` and
  `SHELL-thin-local-plateau-high` as `proved_internal`.
- Promoted `SHELL-thin-curvature-intermediate` and
  `SHELL-rho-one-endpoint` as `proved_internal`.
- Removed the thin endpoint from the blockers of `SHELL-rho-uniformity`.
- Kept `SHELL-rho-zero-endpoint`, `SHELL-rho-compact`,
  `COMP-certified-bessel`, and `TARGET-shell-d3` open.
- Rejected the raw midpoint-action proof route, a global one-radius action
  majorant, and fixed finite Neumann sublayers as global proofs.

## Review gates

- Aggregate-action isolated clean-room reconstruction: PASS.
- Local-plateau high-thin isolated clean-room reconstruction: PASS.
- Aggregate-action adversarial constants/wall audit: PASS.
- Combined overlap and endpoint audit: PASS.
- Independent audit of the complete Round 6 packet: PASS for every promoted
  claim. It corrected one overstatement only in the non-promoted
  `radial-bracketing.md` exploration; the correction does not enter the
  endpoint proof.

## Mechanical validation

- Proof-obligation graph after application and Round 7 routing update: PASS.
- Python regression suite: 22 passed.
- Python compile check: PASS.
- Git diff whitespace check: PASS.
- Round 6 diagnostics remain explicitly non-certifying.

## Authoritative theorem boundary

For every fixed $0<\rho<1$, the shell Pólya estimate is proved for
$K\ge K_0(\rho)$. In addition, Round 6 proves the complete uniform endpoint

$$
\boxed{
1-2^{-18}\le\rho<1,
\qquad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact lower and upper thin thresholds are

$$
K\le\frac1{8(1-\rho)^{5/2}}
\qquad\text{and}\qquad
K\ge\frac{64}{(1-\rho)^2},
$$

which meet at $1-\rho=2^{-18}$ and $K=2^{42}$. Both endpoints are included.
No Bessel-root certificate is needed for this thin neighborhood.

The all-$\rho$ shell theorem remains open. The next analytic target is the
small-hole endpoint, followed by compact-$\rho$ bounded certification and a
fresh final theorem-level audit.
