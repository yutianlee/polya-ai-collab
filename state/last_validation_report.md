# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 8

## State patch

- Source: `rounds/polya-main/round_008/judge/judge-008.md`.
- The embedded State Patch was dry-validated before application and applied
  exactly once at round index 8.
- Created `SHELL-rho-compact-analytic-envelope` as `proved_internal`.
- Created `COMP-certified-bessel-pilot-round8` as `certified` for one exact
  closed central box.
- Kept `SHELL-rho-compact`, the parent `COMP-certified-bessel`,
  `SHELL-rho-uniformity`, and `TARGET-shell-d3` open.
- Rejected literal wall-by-wall enumeration of the current coarse compact
  envelope as a scalable closure strategy.

## Analytic review gates

- Frozen compact packet and incumbent proof: PASS.
- Isolated clean-room reconstruction: PASS.
- Independent adversarial constants, switches, and endpoint audit: PASS.
- Post-correction audit of the $\mathcal E/\mathcal D$ distinction,
  monotone-corner rule, face ownership, and exact cover manifest: PASS.

The accepted analytic theorem is

$$
\boxed{
\rho\in[\rho_*,1-2^{-18}],
\qquad K\ge2^{42}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The left, central, and thin planning envelopes lie below $64$, $2^{35}$,
and $2^{42}$ respectively. All switch and threshold equalities are included.

## Certified pilot gates

- Scope:

  $$
  \rho\in[999/2000,1001/2000],
  \qquad K\in[67/10,168/25].
  $$

- Arb 256-bit producer: PASS.
- Independent standard-library `Fraction` checker: PASS.
- Exact strict count: $4$.
- Certified Weyl lower bound: greater than
  $18.60731553544245607556$.
- Certified margin: greater than $14.60731553544245607556$.
- Current producer, checker, packet, and certificate hashes: PASS.
- Bit-for-bit reproduction of certificate and check report: PASS.
- Fourteen decisive tamper mutations: all rejected.
- Independent mathematical/code audit: PASS for this single box only.

## Mechanical validation

- Round 8 State Patch validation before and after application: PASS.
- Proof-obligation graph: PASS.
- Full Python regression suite: 28 passed.
- Python compile check: PASS.
- Git whitespace check: PASS.

## Authoritative boundary

Both endpoint neighborhoods remain proved for all frequencies. The complete
compact ratio interval is proved above $K=2^{42}$, and one genuine residual
box is certified. The global shell theorem remains open because the rest of

$$
\mathcal D=(I_*\times[0,\infty))\setminus\mathcal A
$$

has no exact checked cover.

At $\varepsilon=2^{-17}$, one present thin residual slice crosses more than
$2^{38}$ angular half-integer walls. Round 9 therefore targets analytic or
symbolic compression, beginning with a self-consistent optimization of the
Round 6 local-plateau constant, rather than brute-force enumeration.
