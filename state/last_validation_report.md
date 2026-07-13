# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 9

## State patch

- Source: `rounds/polya-main/round_009/judge/judge-009.md`.
- The Round 9 patch promotes `SHELL-thin-local-plateau-optimized` as
  `proved_internal`, with primary constant $C=125/8$. The independently
  verified $C=18$ argument is retained only as fallback evidence.
- The already-proved `SHELL-thin-curvature-intermediate` and
  `SHELL-rho-one-endpoint` are strengthened to the exact endpoint
  $\varepsilon\le1/15625$.
- The already-proved `SHELL-rho-compact-analytic-envelope` is strengthened
  to the interval $[\rho_*,1-1/15625]$ and uniform threshold $K\ge2^{35}$.
- `SHELL-rho-compact`, the parent `COMP-certified-bessel`,
  `SHELL-rho-uniformity`, and `TARGET-shell-d3` retain their previous open or
  diagnostic statuses. No new certification claim is made.
- No route is newly rejected. Round score: 6.

## Analytic review gates

- Independent clean-room reconstruction of the optimized plateau theorem:
  PASS with exact constant $C=125/8$.
- Targeted adversarial review of rational constants, exceptional branches,
  ordinary-floor walls, interface and gain walls, threshold equality, and
  strict spectral walls: PASS.
- Parametric dependency audit excluding circular use of estimates proved
  under the old $C=64$ hypothesis: PASS.
- Exact finite rational constant ledger: PASS.
- Updated thin-envelope corollary and all endpoint equalities: PASS.
- Post-promotion integration and provenance audit: PASS.

The accepted optimized high-thin theorem is

$$
\boxed{
0<\varepsilon\le\frac1{100},
\qquad
K\ge\frac{125}{8\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

Its proof estimates the actual uncompensated plateau loss as

$$
R=p-dm<\frac{361}{80\sqrt\varepsilon},
$$

without importing an estimate conditional on $C=64$.

## Enlarged endpoint and compact envelope

The optimized high range and the aggregate-action range overlap exactly
when

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{15625}.
$$

At equality both thresholds are $125^5/8$, and both component theorems
include equality. Therefore

$$
\boxed{
1-\frac1{15625}\le\rho<1,
\qquad K\ge0
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

On

$$
I_9=\left[\rho_*,1-\frac1{15625}\right],
$$

the left and central residual ceilings remain $64$ and $2^{35}$, while the
thin residual ceiling becomes

$$
\frac{125^5}{8}<2^{32}.
$$

Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge2^{35}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 9 changes no producer, checker, certificate,
or provenance hash. This remains evidence for one local box only; the parent
compact certification remains `diagnostic_only`.

## Mechanical validation

- Round 9 judge patch schema and transition validation: PASS.
- Full in-memory patch application followed by graph validation: PASS.
- Exact-constant and narrative cross-checks: PASS.
- Complete computation suite: 30 passed.
- Round 8 independent certificate checker: PASS; the provenance-locked
  compact packet retains SHA-256
  `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
- Control-character and Markdown whitespace checks for the narrative state
  files: PASS.
- No certified-computation code or certificate artifact changed in Round 9.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved globally for $K\ge2^{35}$. The full all-frequency shell
theorem remains open because the remaining compact residual

$$
\mathcal D=(I_9\times[0,\infty))\setminus\mathcal A
$$

below $2^{35}$ has no exact checked cover. Further analytic aggregation or a
face-connected monotone-corner certificate is required. After the compact
piece closes, a fresh theorem-level clean-room reconstruction and adversarial
audit are still mandatory before promoting the final target.
