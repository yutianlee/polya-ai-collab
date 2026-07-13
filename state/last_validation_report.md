# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 10

## State patch

- Source: `rounds/polya-main/round_010/judge/judge-010.md`.
- The Round 10 patch creates `SHELL-central-thin-seam-compression` as
  `proved_internal`, with

  $$
  0<\varepsilon\le\frac1{25},
  \qquad
  K\ge\frac{20}{\varepsilon^2}.
  $$

- The Round 9 optimized theorem remains authoritative on
  $0<\varepsilon\le1/100$, where its sharper threshold is
  $125/(8\varepsilon^2)$.
- `SHELL-rho-compact-analytic-envelope` is strengthened on
  $I_{10}=[\rho_*,1-1/15625]$ to the uniform threshold
  $K\ge125^5/8<2^{32}$.
- The complete all-frequency thin endpoint is unchanged:
  $\varepsilon\le1/15625$.
- `SHELL-rho-compact`, the parent `COMP-certified-bessel`,
  `SHELL-rho-uniformity`, and `TARGET-shell-d3` retain their open or
  diagnostic statuses. No new certification claim is made.
- No route is newly rejected. Round score: 6.

## Analytic review gates

- Frozen dependency packet: PASS.
- Incumbent enlarged-domain proof with $C=20$: PASS.
- Isolated clean-room reconstruction with distinct intermediate constants:
  PASS.
- Adversarial constants, dependency, branch, wall, and seam-face audit:
  PASS after a dependency-boundary wording correction.
- Exact finite rational seam-and-ceiling ledger: PASS.
- Updated global corollary with independent endpoint and left-zone
  dependencies: PASS.
- Post-promotion graph, narrative, dependency, status, and provenance
  integration audit: PASS.

The accepted enlarged-domain theorem is

$$
\boxed{
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The incumbent proof obtains

$$
\widehat q<\frac{21}{80},
\qquad
R<\frac{73}{16\sqrt\varepsilon},
$$

with exact positive no-drop and gain-payment margins. The clean-room proof
uses different constants and reaches the same theorem.

## Moved seam and global ceiling

The new seam is

$$
\rho_s=\frac{24}{25}.
$$

At its central face,

$$
K_0(24/25)<6000^2=36000000.
$$

On the enlarged seam strip $24/25\le\rho\le99/100$, the $C=20$ high
threshold is at most $200000$. On the ultra-thin strip the sharper Round 9
threshold remains in force. Thus

$$
\boxed{
0<\rho<1,
\qquad
K\ge\frac{125^5}{8}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact comparisons are

$$
6000^2<\frac{125^5}{8}<2^{32}<2^{35},
\qquad
2^{35}>9\frac{125^5}{8}.
$$

Hence $125^5/8$ is the new all-ratio analytic ceiling, more than nine times
smaller than the former $2^{35}$ ceiling.

## Unchanged all-frequency endpoint

Round 10 does not enlarge the all-frequency thin endpoint. The new theorem
overlaps the aggregate-action range only when

$$
\frac{20}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{25600},
$$

which is weaker than the retained Round 9 endpoint
$\varepsilon\le1/15625$. Therefore

$$
1-\frac1{15625}\le\rho<1,
\qquad K\ge0
$$

remains the exact complete thin neighborhood currently proved.

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 10 changes no producer, checker,
certificate, or provenance hash. This remains evidence for one local box
only; the parent compact certification remains `diagnostic_only`.

## Mechanical validation

- Applied proof-obligation graph validation: PASS.
- Exact Round 10 seam-and-ceiling ledger: PASS.
- Complete computation suite: 32 passed.
- Round 8 independent certificate checker: PASS; the provenance-locked
  compact packet retains SHA-256
  `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
- No Round 8 producer, checker, certificate, or frozen packet changed.
- Control-character and Markdown whitespace checks for the narrative state
  files: PASS.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge125^5/8<2^{32}$. The full
all-frequency theorem remains open on the compact residual

$$
\mathcal D=(I_{10}\times[0,\infty))\setminus\mathcal A
$$

below the new ceiling. Round 11 should first compress the dominant
ultra-thin aggregate-to-plateau gap

$$
\frac1{15625}<\varepsilon\le\frac1{100},
\qquad
\frac1{8\varepsilon^{5/2}}
<K<\frac{125}{8\varepsilon^2},
$$

aiming to bring its ceiling below $6000^2$ before any large certification
manifest. After the compact piece closes, a fresh theorem-level clean-room
reconstruction and adversarial audit remain mandatory before promotion of
the final target.
