# Last Validation Report

Date: 2026-07-14

Round: polya-main / round 18

## Promotion decision

- Judge: rounds/polya-main/round_018/judge/judge-018.md
- Judge SHA-256:
  73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61
- Decision: **PASS**.
- First unsupported implication: **none**.
- Mathematical progress score: 7.
- The Round 18 State Patch validated against its frozen baseline and the
  authoritative graph reflects its one-time application.

Round 18 created and promoted only:

- SRC-LORCH as a qualified proved_external_dependency;
- SHELL-next-angular-staircase as proved_internal.

No theorem-level target was closed and no Round 18 certified-computation
child was created.

## Promoted analytic staircase

Set

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
$$

The accepted closed theorem band is

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_5(\rho).
}
$$

The genuinely new Round 18 part is

$$
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)
\right\}.
$$

The isolated clean-room proof, independent exact-constant audit,
cross-comparison, and fresh adversarial referee all returned PASS. Strict
counting assigns every spectral equality to the lower count. Exact
subtraction assigns the old \(K=k_2\) face to its Round 17 owner and the
inclusive \(K=k_5\) face to the new Round 18 lemma.

## Exact surviving residual

Let \(U(\rho)\) retain its accepted piecewise definition from the frozen
compact-ratio mask. Exact subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)
\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
$$

All four displayed frequency inequalities are strict. The lower-ratio
component is unchanged; it does not inherit the
\(\rho\geq\rho_c\) staircase. The high-ratio component begins strictly
above \(k_5\). The exact witness \((\rho,K)=(1/2,30)\) lies in the second
component, so \(\mathcal D_{18}\) is nonempty.

The certified boxes \(B_0\) and \(B_1\) remain valid independent regression
artifacts, but both were already absorbed by \(\mathcal C_{17}\). They
produce no additional subtraction.

## Qualified Lorch source boundary

The source card sources/lorch_bessel_zeros.md has SHA-256
85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4.

The primary SIAM publisher abstract states the two strict lower
inequalities, the first-positive-zero convention, and the scope
\(\nu>-1\). DLMF supplies the spherical-Bessel identity. Exact
specialization supports only

$$
j_{5/2,1}>\frac{51}{10},
\qquad
j_{7/2,1}>\frac{13}{2},
\qquad
j_{9/2,1}>\frac{15}{2}.
$$

The full Lorch article proof was access-controlled in the audited
environment. Accordingly, SRC-LORCH is a qualified statement-level
external dependency, not an internal reconstruction. It does not supply
shell-to-ball comparison, shell cross-product zero bounds, higher-radial
exclusions, angular multiplicities, or Weyl payments. Those Round 18 steps
were proved internally.

## Graph status after promotion

The authoritative graph has 53 unique obligation IDs and validates with no
missing references, duplicate IDs, or dependency cycles. After the
canonical Round 19 round-selection update its SHA-256 is

$$
\texttt{24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e}.
$$

Relevant statuses are:

| Obligation | Status after Round 18 |
|---|---|
| SRC-LORCH | proved_external_dependency |
| SHELL-next-angular-staircase | proved_internal |
| SHELL-rho-compact-analytic-envelope | proved_internal |
| SHELL-rho-compact | open |
| SHELL-rho-uniformity | open |
| TARGET-shell-d3 | open |
| POLYA-program-target | open |
| COMP-certified-bessel | diagnostic_only |
| COMP-certified-bessel-pilot-round8 | certified |
| COMP-certified-bessel-pilot-round17 | certified |

The theorem remains open because the exact nonempty
\(\mathcal D_{18}\) is not covered.

## Validation ledger

- Round 18 judge fixed evidence: 18 of 18 hashes matched.
- State Patch final audit: PASS; first issue none.
- Residual-mask self-check: PASS, 12 checks.
- Angular-staircase exact ledger: PASS, 40 checks; first issue null.
- Complete repository suite:
  **132 passed, 10 subtests passed**.
- Round 18 bytecode compilation: PASS.
- Graph validation after the Round 19 selection update: PASS.
- Evidence paths and artifact hashes: complete.
- Dependency and implication graph: acyclic.
- git diff --check in the final audit: PASS.

## Next method boundary

Round 19 must first freeze the exact \(\mathcal D_{18}\) mask. Its
high-ratio lead route is a combined radial-entry/angular staircase above
\(k_5\), explicitly resolving the relative walls \(2z_\rho\) and
\(k_6(\rho)\). A crude one-radial-mode continuation is not authorized.
The lower-ratio component \(\rho_*<\rho<\rho_c\) remains a separate proof
problem. No unproved Round 19 threshold is recorded in this report.
