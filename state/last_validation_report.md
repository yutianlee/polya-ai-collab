# Last Validation Report

Date: 2026-07-14

Round: `polya-main` / round 13

## State patch

- Source: `rounds/polya-main/round_013/judge/judge-013.md`.
- `SHELL-central-thin-seam-compression` remains `proved_internal` and is
  strengthened to

  $$
  0<\varepsilon\le\frac1{10},
  \qquad
  K\ge\frac{24}{\varepsilon^2}.
  $$

- The sharper Round 10 threshold $K\ge20/\varepsilon^2$ is retained on
  $0<\varepsilon\le1/25$.
- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`; the
  central--thin seam moves to $\rho=9/10$, the exact central endpoint is
  $K_0(9/10)<900^2$, and the all-ratio analytic ceiling becomes
  $K\ge900^2$.
- The complete all-frequency thin endpoint remains exactly
  $99/100\le\rho<1$.
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` remain
  open. `COMP-certified-bessel` remains `diagnostic_only`.
- No route is newly rejected. Round score: 6.

The judge State Patch validated before application and was applied exactly
once. Subsequent checks use the promoted graph rather than replaying the
Round 13 patch.

## Analytic review gates

- Frozen enlarged-seam dependency packet: PASS.
- Incumbent proof on the full enlarged domain: PASS.
- Independent constant-inventory derivation: PASS.
- Strictly isolated clean-room reconstruction with a different localization
  and path argument: PASS.
- Adversarial constants, branches, dependencies, walls, and closed-face
  audit: PASS. First unsupported implication: none.
- Exact executable ledger for both proof architectures: PASS.

The incumbent route and independent inventory prove

$$
d>\frac23,
\qquad
\widehat q<\frac37,
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

Its complete fixed-$r=B$ comparison path has derivative cap

$$
\frac{1572142117}{270000000}<6
$$

with reserve $47857883/270000000>0$. Its no-drop endpoint and action-payment
reserves are, respectively,

$$
\frac{2376966388822}{5818105805625}>0,
\qquad
\frac{170244091}{27217575}>0.
$$

The strictly isolated reconstruction does not reuse that finite comparison.
It proves directly

$$
\frac{x_0}{K}>
\frac{8663}{16800}
=\frac{18}{35}+\frac{23}{16800},
$$

and follows the affine path

$$
L(X)=\frac52X-7,
\qquad
F(X)=X^2(1-h_X)^2-2\pi^2Q_X.
$$

On the complete path it obtains

$$
F(B)>\frac{12760228}{48234375},
\qquad
F'(X)>\frac{229}{2646},
$$

with payment reserve $307/55>0$. Both architectures own the no-drop,
immediate-drop, degenerate-head, and $R=0$ branches, together with the
ordinary-floor, gain, interface, threshold, and strict spectral walls.

## Accepted Round 13 theorem

Including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

At the moved central endpoint, the exact quadratic reserve is

$$
\frac{6897151}{18725}>0,
$$

which proves

$$
\boxed{K_0(9/10)<900^2.}
$$

## Closed global union

The accepted analytic zones are:

1. on $[\rho_*,1/16]$, every possible residual has $K<64$;
2. on $[1/16,9/10]$, every possible residual has
   $K<K_0(9/10)<900^2$;
3. on $[9/10,19/20]$, every possible residual has
   $K<24/(1-\rho)^2\le9600$;
4. on $[19/20,24/25]$, every possible residual has
   $K<24/(1-\rho)^2\le15000$;
5. on $[24/25,99/100]$, every possible residual has
   $K<20/(1-\rho)^2\le200000$.

The complete thin endpoint owns $[99/100,1)$ at every frequency. All shared
ratio and threshold faces are owned. Since

$$
64<9600<15000<200000<900^2,
$$

the complete high-frequency conclusion is

$$
\boxed{
0<\rho<1,
\qquad K\ge900^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reduction from the Round 12 ceiling is

$$
\frac{3300^2}{900^2}=\frac{121}{9}>13.
$$

## Complete thin endpoint

Round 13 does not enlarge the all-frequency endpoint. The accepted product,
aggregate, and complementary-action ranges still prove exactly

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

The Round 13 seam theorem is high-frequency only.

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad
K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 13 changes no producer, checker,
certificate, or protected packet. The independent checker reproduces the
provenance-locked packet hash
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
This remains evidence for one local box only; the parent compact
certification remains `diagnostic_only`.

## Mechanical validation

- Judge State Patch validation before application: PASS.
- State Patch applied exactly once: PASS.
- Applied proof-obligation graph and dependency DAG validation: PASS.
- Independent post-promotion graph, narrative, evidence-path, face, and
  provenance audit: PASS.
- Embedded and standalone exact Round 13 seam ledgers: PASS.
- Focused Round 13 tests: 5 passed.
- Complete computation suite: 45 passed.
- Round 8 independent certificate and provenance checker: PASS.
- Python compilation, reading-packet idempotence, Markdown whitespace, and
  diff checks: PASS.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge900^2$. The full all-frequency
theorem remains open on the exact compact residual

$$
\mathcal D=(I_{13}\times[0,\infty))\setminus\mathcal A
$$

below that ceiling, where $I_{13}=[\rho_*,99/100]$ and $\mathcal A$ is the
complete accepted analytic cover, including all threshold faces.

Round 14 may separately test

$$
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2},
\qquad
\rho_s=\frac78,
\qquad
K_0(7/8)<550^2.
$$

These are unproved planning targets. No Round 13 estimate may be
extrapolated to them. After the compact residual closes, fresh theorem-level
clean-room and adversarial audits remain mandatory before promotion of the
final target.
