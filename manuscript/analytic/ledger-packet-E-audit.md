# Adversarial audit: Packet E

Date: 2026-07-16

## Verdict

**PASS**

The audited version eliminates the logical dependence on all eight
verify_u_and_k11 predicates and all fifty verify_optical_constants
predicates. The executable remains useful as an authentication replay, but
none of its decisions is a premise of Packet E.

## Audited artifact and hashes

- manuscript/analytic/ledger-packet-E.tex
  - SHA-256:
    **03259745fbf8d67930045b4f996ddf9f61a2f5a74e72cf7a95064351e59a6123**
- compiled manuscript/analytic/ledger-packet-E.pdf
  - SHA-256:
    **3074a7fcf5163f9c6fe17458eb370b327d07f518fd869cfe93ae066202f3d7ae**
- comparison executable
  computations/certification/verify_analytic_ledgers.py
  - SHA-256:
    **41691116e0e3e5453b9b209acb93ff784724c3a95b83c94bbdf7f6760616e716**
  - authenticated combined-registry digest:
    **afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1**

The TeX hash is for the post-audit version, including the corrections
listed below.

## Sources compared

1. manuscript/spherical-shell-polya-proof.tex, especially the primitive
   upper-owner formula, the piecewise formula for \(U\), the all-frequency
   optical theorem, and the construction of \(\mathcal D_{20}\).
2. Supplement S1 in
   manuscript/spherical-shell-polya-supplement.tex, which embeds the same
   upper-owner and optical predicate families.
3. computations/certification/verify_analytic_ledgers.py, functions
   verify_u_and_k11, verify_optical_constants, and
   verify_product_deficit.
4. manuscript/analytic/exact-ledger-inventory.md, for the intended
   Packet-E scope and row counts.

The executable was used to enumerate predicates, not to prove the
displayed inequalities. Every nontrivial fraction below was independently
recomputed with exact rational arithmetic.

## Corrections made during this audit

The first stable candidate had two small omissions and one layout defect.
They were reported before modification and corrected in the audited hash.

1. The common-face union claimed
   \[
   \{\pi<a\le c/\varepsilon\}\cup\{a\ge c/\varepsilon\}
   =\{a>\pi\}
   \]
   without displaying \(c/\varepsilon>\pi\). Packet E now prints
   \[
   \frac c\varepsilon\ge\frac c{\varepsilon_0}
   =\frac{2252}{275}>\frac{22}{7}>\pi,\qquad
   \frac{2252}{275}-\frac{22}{7}=\frac{9714}{1925}>0.
   \]
2. The scope comparison \(\rho_c<39/50<5/6\) was only implicit in the
   displayed assumptions. Packet E now prints
   \[
   \rho_c<\frac17<\frac{39}{50}<\frac56,
   \]
   using \(\pi>3\).
3. The final registry name caused an overfull box. The prose was reflowed;
   this did not alter any mathematical statement.

No other TeX change was needed.

## Audit of the eight upper-owner predicates

| row | executable predicate | analytic disposition |
|---:|---|---|
| 1 | \(\eta k_{11}<C_0\) at \(\rho=1/2\) | Superseded by the stronger direct estimate \(K_0>64>k_{11}\); the endpoint predicate is no longer needed. |
| 2 | \(\sqrt{1+\rho}<\sqrt2\) reduction | Superseded by the same direct estimate; no monotonic endpoint reduction is used. |
| 3 | positive-root identity gives \(K_0>C_0/\eta\) | Packet E uses the exact positive-root formula and the stronger inequality \(\sqrt{K_0}>\sqrt{a_\rho}/\eta_\rho\). |
| 4 | \(k_{11}\) below the seam-54 branch | \(k_{11}<64\), whereas \(54/(1-\rho)^2\ge1944\) for \(5/6\le\rho<7/8\). |
| 5 | final \(K_0\)-only interval avoids the seam | The corrected chain \(\rho_c<1/7<39/50<5/6\) proves this exactly. |
| 6 | final interval avoids \(H_0\) | \(\omega_0<1/8<\rho_c\), with both strict inequalities proved from the displayed rational bounds. |
| 7 | \(U=K_0\) on \(\rho_c\le\rho<39/50\) | Follows from rows 5--6 and the piecewise upper-owner formula. |
| 8 | \(k_{11}<U\) on \(\rho_c\le\rho<7/8\) | Below \(5/6\), \(U=K_0>64\); at and above \(5/6\), \(U=54/(1-\rho)^2\ge1944\); throughout, \(k_{11}<64\). |

The key direct bounds are valid:

- \(a_{\rho_c}=1\) and \(a_\rho\) is increasing;
- \(0<\eta_\rho<1/8\);
- the positive-root formula gives
  \(\sqrt{K_0}>\sqrt{a_\rho}/\eta_\rho>8\);
- \(z_\rho<8\pi<176/7<26\), hence
  \(k_{11}^2<26^2+132=808<64^2\).

Thus the packet does not merely reproduce the original eight-check route;
it replaces its first three checks by a simpler stronger argument and
proves the same required owner conclusions.

## Audit of the fifty optical predicates

The exact count is \(14+12+1+5+18=50\):

| executable rows | count | analytic replacement |
|---|---:|---|
| endpoint reserves, monotonicity, scaling, and common face | 1--14 | complete low/high screen lemma |
| angular ceiling blocks \(j=0,\ldots,11\) | 15--26 | \(\sum_{\ell=0}^{m-1}(2\ell+1)=m^2\) for every \(m\) |
| radial equality convention | 27 | strict exclusion of the newly proposed radial layer |
| structural product-deficit checks | 28--32 | symbolic \(N,t\) formula, increment, derivative, and exact minimum |
| sampled product expansions | 33--50 | one polynomial identity valid for all \(N,t\), making the eighteen samples redundant |

### Product deficit

With \(C_D=1382/3125\),
\[
\frac12-C_D=\frac{361}{6250}>0.
\]
The exact lower bound for the \(N\)-increment is
\[
3\left(\frac12-C_D\right)+\frac16-C_D^2
=\frac{4229603}{29296875}>0.
\]
At \(N=1\), differentiation gives
\[
F'(t)=2(t-C_D)(t+1),
\]
and \(0<C_D<1\), so the unique minimum occurs at \(t=C_D\). Direct
substitution gives
\[
F(C_D)=\frac{1822532}{91552734375}>0.
\]
Expansion of
\[
\frac23(N+t)^3-N(N+t)^2+
\frac{N(N+1)(2N+1)}6
\]
gives the printed product-deficit identity for arbitrary \(N,t\). It
therefore replaces all eighteen sample evaluations.

### Low optical screen

The scaling is in the correct direction:

- \(a\le c/\varepsilon\) and \(q>1/\pi\) give
  \(2\varepsilon a/(3\pi)<2cq/3\);
- \(a>\pi\) gives
  \(\varepsilon^2/(\pi a)<\varepsilon^2/\pi^2
  <\varepsilon_0^2q^2\);
- the remaining cost terms increase with
  \(0<\varepsilon\le\varepsilon_0\).

The endpoint subtraction recomputes exactly as
\[
C_D-\left(\frac{2cq}{3}+\frac{\varepsilon_0}{4}
+\varepsilon_0^2q^2\right)
=\frac{39569}{2772225000}>0.
\]

### High optical screen

Expansion of the angular error gives exactly
\[
\frac E{a^2}
=\frac{\varepsilon}{\pi}
+\frac{\varepsilon^2}{4\pi a}
+\frac{\varepsilon}{4a}
+\frac{\varepsilon^2}{16a^2}.
\]
For \(a\ge c/\varepsilon\), every inverse power of \(a\) is bounded in
the direction printed in Packet E. The radial lower screen uses
\(\pi<22/7\), also in the correct direction. Moreover,
\[
L'(\varepsilon)<0,\qquad A'(\varepsilon)>0
\quad(0<\varepsilon\le11/50<1/2).
\]
The endpoint difference independently recomputes to
\[
L(11/50)-A(11/50)
=\frac{14817541}{472867032960000}>0.
\]
The corrected \(c/\varepsilon>\pi\) witness proves that the common face
belongs to both pieces, including the low piece.

## Scope and equality audit

- The upper-owner result covers the full strip
  \(\rho_c\le\rho<7/8\), not merely the final
  \(\rho<39/50\) residual.
- The seam face \(\rho=5/6\) is assigned to the seam branch, as in the
  piecewise formula in the main manuscript.
- The low optical screen includes \(a=c/\varepsilon\); the high screen
  includes the same face.
- The strict radial convention handles \(a=m\pi\), while
  \(0\le a\le\pi\) is zero-count owned.
- \(K=a=0\) is handled separately with equality on both sides.
- Overlap at the common optical face is intentional and harmless.

## Compilation

Compilation used the LaTeX skill workflow with bundled Tectonic:

    compile_latex.py ledger-packet-E.tex --compiler tectonic --json

Status: **PASS**, exit code 0. Tectonic performed the necessary rerun and
produced a five-page PDF. The final pass had resolved references and no
overfull or underfull box warning.

## Residual findings

None. Packet E assumes the analytic channel, product, radial-deficit, and
angular-error reductions already proved in the main manuscript; it
replaces exactly their former finite arithmetic/scope ledger, which is the
declared Packet-E task.
