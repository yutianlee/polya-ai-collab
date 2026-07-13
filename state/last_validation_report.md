# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 12

## State patch

- Source: `rounds/polya-main/round_012/judge/judge-012.md`.
- `SHELL-central-thin-seam-compression` remains `proved_internal` and is
  strengthened to

  $$
  0<\varepsilon\le\frac1{20},
  \qquad
  K\ge\frac{24}{\varepsilon^2}.
  $$

- The sharper Round 10 threshold $K\ge20/\varepsilon^2$ is retained on
  $0<\varepsilon\le1/25$.
- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`; the
  central--thin seam moves to $\rho=19/20$, the exact central endpoint is
  $K_0(19/20)<3300^2$, and the all-ratio analytic ceiling becomes
  $K\ge3300^2$.
- The complete all-frequency thin endpoint remains exactly
  $99/100\le\rho<1$.
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` remain
  open. `COMP-certified-bessel` remains `diagnostic_only`.
- No route is newly rejected. Round score: 6.

## Analytic review gates

- Frozen enlarged-seam dependency packet: PASS.
- Incumbent proof on the full enlarged domain: PASS.
- Independent constant-inventory derivation: PASS.
- Strictly isolated clean-room reconstruction with a different loss proof:
  PASS.
- Adversarial constants, branches, dependencies, walls, and closed-face
  audit: PASS. First unsupported implication: none.
- Exact executable ledger for all three proof routes: PASS.

The incumbent route proves

$$
d>\frac{39}{50},
\qquad
\widehat q<\frac{27}{100},
\qquad
R<\frac{23}{5\sqrt\varepsilon}.
$$

Its no-drop endpoint and payment margins are, respectively,

$$
\frac{4189934997169}{10140435204025}>0,
\qquad
\frac{233}{25}>0.
$$

The independent constant inventory obtains

$$
d>\frac34,
\qquad
\widehat q<\frac{11}{40},
\qquad
R<\frac{23}{5\sqrt\varepsilon},
$$

with exact endpoint margin

$$
\frac{2196261729217}{5173691430625}>0.
$$

The isolated reconstruction uses a distinct rectangle proof: it first shows
$P<10$, excludes the complete path $5\le r\le P<10$, and concludes

$$
R<\frac5{\sqrt\varepsilon}.
$$

Every route owns the no-drop, immediate-drop, degenerate-head, and $R=0$
branches, together with ordinary-floor, gain, interface, threshold, and
strict spectral walls.

## Accepted Round 12 theorem

Including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac1{20},
\qquad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

At the moved central endpoint, all three routes reproduce the exact
quadratic reserve

$$
\frac{32985481}{7422975}>0,
$$

which proves

$$
\boxed{K_0(19/20)<3300^2.}
$$

## Closed global union

The accepted analytic zones are:

1. on $[\rho_*,1/16]$, every possible residual has $K<64$;
2. on $[1/16,19/20]$, every possible residual has
   $K<K_0(19/20)<3300^2$;
3. on $[19/20,24/25]$, every possible residual has
   $K<24/(1-\rho)^2\le15000$;
4. on $[24/25,99/100]$, every possible residual has
   $K<20/(1-\rho)^2\le200000$;
5. on $[99/100,1)$, every frequency is proved.

All shared ratio and threshold faces are owned. Since

$$
64<15000<200000<3300^2,
$$

the complete high-frequency conclusion is

$$
\boxed{
0<\rho<1,
\qquad K\ge3300^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reduction from the Round 11 ceiling is

$$
\frac{6000^2}{3300^2}=\frac{400}{121}>3.
$$

## Complete thin endpoint

Round 12 does not enlarge the all-frequency endpoint. The accepted product,
aggregate, and complementary-action ranges still prove exactly

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

The seam theorem is high-frequency only.

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad
K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 12 changes no producer, checker,
certificate, or protected packet. The independent checker reproduces the
provenance-locked packet hash
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
This remains evidence for one local box only; the parent compact
certification remains `diagnostic_only`.

## Mechanical validation

- Judge State Patch validation before application: PASS.
- State Patch applied exactly once: PASS.
- Applied proof-obligation graph validation: PASS.
- Independent post-promotion graph, narrative, evidence-path, face, and
  provenance audits: PASS.
- Exact Round 12 enlarged-seam ledger: PASS.
- Focused Round 12 tests: 4 passed.
- Complete computation suite: 40 passed.
- Round 8 independent certificate and provenance checker: PASS.
- Python compilation, evidence-path, Markdown whitespace, and diff checks:
  PASS.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge3300^2$. The full
all-frequency theorem remains open on the exact compact residual

$$
\mathcal D=(I_{12}\times[0,\infty))\setminus\mathcal A
$$

below that ceiling, where $\mathcal A$ is the complete accepted analytic
cover, including all threshold faces.

Round 13 may separately test

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2},
\qquad
\rho_s=\frac9{10},
\qquad
K_0(9/10)<900^2.
$$

These are unproved planning targets. No Round 12 estimate may be
extrapolated to them. After the compact residual closes, fresh theorem-level
clean-room and adversarial audits remain mandatory before promotion of the
final target.
