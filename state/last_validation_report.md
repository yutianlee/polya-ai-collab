# Last Validation Report

Date: 2026-07-14

Round: `polya-main` / round 17

## Promotion decision

- Judge: `rounds/polya-main/round_017/judge/judge-017.md`.
- Judge SHA-256:
  `769dc256aa97dc8da093bdead8a020033904c115ff256ae60a708a31f90dbadd`.
- Decision: **PASS**. First unsupported implication: none.
- State Patch validation: **PASS** against the untouched Round 16 graph.
- The patch was applied exactly once with `round_index=17`; it must not be
  replayed against the promoted graph.
- Round score: 6.

The one-time patch created `SHELL-first-angular-bands` as
`proved_internal` and `COMP-certified-bessel-pilot-round17` as `certified`.
It updated the compact analytic envelope to the exact Round 17 cover while
retaining `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
and `POLYA-program-target` as `open`. The parent
`COMP-certified-bessel` remains `diagnostic_only`.

The durable graph hashes are:

- untouched Round 16 baseline:
  `dc2552091ff79f5ab39de896b4d97cf22ccc234f3842ee9734d54d123c5f2379`;
- immediately after the one-time Round 17 State Patch:
  `cbd15b3ab3c73f326321052019de9c2a8a2877c6ec84a668d1a5a35ffe13ebd5`;
- after the initial Round 18 target-selection rule update:
  `aca527f8b947f9a14f94e531ce4e659660cc93bc05bb902276b6f155e4eb4e18`;
- final graph after the deterministic-LF provenance repair described below:
  `3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c`.

## Promoted analytic band

Set

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
$$

The accepted closed theorem band is

$$
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_2(\rho).
$$

The spectral caps $0$, $1$, and $4$ follow from the complete separated
spectrum, min--max, strict endpoint counting, and angular multiplicities
$1$ and $3$. The exact Weyl reserve at the second payment wall exceeds
$49061/269500$.

The isolated clean-room proof, exact finite ledger, and fresh adversarial
referee all returned PASS. Provenance is exact: A4's finite audit checks the
theorem constants, $\mathcal C_{17}\subset\mathcal D_{16}$, and
$B_0\subset\mathcal C_{17}$; the fresh referee separately proves
$B_1\subset\mathcal C_{17}$ with squared upper-face reserve

$$
\frac{668749071}{10020010000}>0.
$$

## Exact surviving residual

The new analytic part is

$$
\mathcal C_{17}
=\{\rho_c\le\rho<7/8,\ z_\rho<K\le k_2(\rho)\}.
$$

The exact surviving residual is

$$
\boxed{
\begin{aligned}
\mathcal D_{17}
=&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\ k_2(\rho)<K<U(\rho)\right\}.
\end{aligned}}
$$

Both certified boxes satisfy
$B_0,B_1\subset\mathcal C_{17}$. They remain independent regression
evidence but provide no additional subtraction, so
$\mathcal U_{17}=\mathcal D_{17}$. The full theorem remains open.

## Certified pilot extension

The closed face-connected box

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right]
$$

has exact strict count $4$ and a positive certified Weyl margin. The Arb
producer, independent exact-Fraction checker, tamper tests, and persistent
independent audit all pass. This promotes only the bounded child
computation; its parent remains `diagnostic_only`.

## Validation ledger

- State Patch validator before application: `Patch OK`.
- Independent read-only in-memory application audit: PASS after one
  provenance correction and a complete re-audit.
- State Patch validator after application: graph OK.
- Fixed judge evidence: 20 of 20 hashes match current bytes.
- Patch evidence paths and hashes: complete; no missing references.
- Dependency graph: acyclic; no missing obligation references.
- Full Python suite: `97 passed`.
- The staging audit found that the new JSON writers inherited Windows CRLF
  translation while Git stores the artifacts with LF. Both writers now set
  `newline="\n"`; the certificate and checker report were regenerated, their
  complete provenance chain was rehashed, and committed bytes now reproduce
  the authenticated bytes exactly.
- A fresh read-only post-repair audit confirmed LF-only byte regeneration,
  all internal and external provenance hashes, 20/20 judge hash rows,
  index/worktree equality for every authenticated artifact, checker PASS,
  and 6/6 focused certificate tests.
- `git diff --check`: PASS.
- UTF-8, control-character, whitespace, final-newline, Markdown-fence, and
  math-delimiter hygiene: PASS.

The next round must work only on the exact $\mathcal D_{17}$. The crude
post-$k_2$ multiplicity cap $9$ is a method obstruction at $\rho_c$, not a
counterexample; a sharper next-angular staircase or a new estimate is
required.
