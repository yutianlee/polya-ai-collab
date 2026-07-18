# Adversarial audit: Packet F

Date: 2026-07-16

## Verdict

**PASS**

Packet F replaces all sixty-eight predicates in
verify_exact_subtraction: the \(9\times7=63\) state evaluations and the
five separately asserted boundary/ownership predicates.

## Audited artifact and hashes

- manuscript/analytic/ledger-packet-F.tex
  - SHA-256:
    **b137fde7b974f55dd8efd7d90501611939f291cac80437c6f707c3cbc483e26e**
- compiled manuscript/analytic/ledger-packet-F.pdf
  - SHA-256:
    **45383929e0705ec5335c7690575d4b2cecdd4fa4d80364ef69b29a93bc90cd7d**
- comparison executable
  computations/certification/verify_analytic_ledgers.py
  - SHA-256:
    **41691116e0e3e5453b9b209acb93ff784724c3a95b83c94bbdf7f6760616e716**
  - authenticated combined-registry digest:
    **afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1**

## Sources compared

1. The exact definition of \(\mathcal D_{19}\), the closed high staircase,
   the inclusive optical owner, \(\mathcal D_{20}\), and
   \(\mathcal D_{21}=\varnothing\) in
   manuscript/spherical-shell-polya-proof.tex.
2. The embedded verify_exact_subtraction registry in Supplement S1,
   manuscript/spherical-shell-polya-supplement.tex.
3. The standalone copy of verify_exact_subtraction in
   computations/certification/verify_analytic_ledgers.py.
4. The 68-row decomposition in
   manuscript/analytic/exact-ledger-inventory.md.

No modification to Packet F was necessary.

## Set-by-set comparison

Packet F reproduces the three components of \(\mathcal D_{19}\) with the
correct open and closed ratio faces:

- \(\rho_*<\rho\le\rho_0\) for the first lower component;
- \(\rho_0<\rho<\rho_c\) for the second lower component;
- \(\rho_c\le\rho<7/8\) for the high component.

It also preserves both strict frequency inequalities inherited from
\(\mathcal D_{19}\): the lower wall is strict, and \(K=U(\rho)\) is
excluded.

The three subtracted owners have the correct closure conventions:

- the lower owner equals the union of the two lower components;
- the staircase owns \(k_6(\rho)<K\le k_{11}(\rho)\), including
  \(K=k_{11}\);
- the optical owner includes \(\rho=39/50\).

The subtraction is formal:
\[
\begin{aligned}
\mathcal D_{19}\setminus L_{\rm own}
 &=D_{\rm high},\\
D_{\rm high}\setminus S_{\rm own}
 &=\{\rho_c\le\rho<7/8:\ k_{11}(\rho)<K<U(\rho)\},\\
(\cdots)\setminus O_{\rm own}
 &=\{\rho_c\le\rho<39/50:\ k_{11}(\rho)<K<U(\rho)\}
 =\mathcal D_{20}.
\end{aligned}
\]
This calculation does not require an assumed ordering of \(k_{11}\) and
\(U\): if \(k_{11}\ge U\), both the displayed surviving fibre and the
actual set difference are empty.

## Reconciliation of the 63 state rows

The executable partitions the ratio axis into

    rho_star, low1, rho0, low2, rho_c,
    pre_opt, opt_face, post_opt, rho_7_8

and the frequency axis into

    below_k6, k6, stair, k11, post_k11, U, above_U.

Packet F replaces this grid symbolically:

- rho_star and rho_7_8 are excluded by the open outer ratio faces;
- low1, rho0, and low2 are removed by the lower owner;
- on every high-ratio state, below_k6 and k6 are excluded by \(k_6<K\);
- stair and k11 are removed by the closed staircase;
- U and above_U are excluded by \(K<U\);
- post_k11 survives only on rho_c and pre_opt;
- opt_face and post_opt are removed by the inclusive optical owner.

An independent Boolean enumeration of these memberships returned
**63/63** equalities with the stated \(\mathcal D_{20}\) classifier.
The enumeration authenticated the set proof but is not its premise.

## Audit of the five separate interface predicates

1. **\(\rho=\rho_0\).**
   Since \(d=(2\rho_0)^{-1}\), the prospective second lower fibre has the
   same lower wall as the first. The first component includes the ratio
   face, the second excludes it, and the lower owner removes it exactly
   once.
2. **\(\rho=\rho_c\).**
   The high component includes the face. The optical owner begins only at
   \(39/50\), so the post-\(k_{11}\) fibre at \(\rho_c\) survives.
3. **\(\rho=39/50\).**
   The optical theorem includes this ratio face, so it is removed and is
   absent from \(\mathcal D_{20}\).
4. **\(K=k_{11}\) and \(K=U\).**
   The first is staircase-owned; the second never belonged to
   \(\mathcal D_{19}\).
5. **Interior pre-optical post-\(k_{11}\) cell.**
   It belongs to \(\mathcal D_{19}\), belongs to none of the three removed
   owners, and is exactly the interior of \(\mathcal D_{20}\).

These are precisely the five labels following the 63-row loop in
verify_exact_subtraction.

## Final compact/tail split

The additional split
\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}
\]
is correct and disjoint. It assigns \(K=200\) only to the compact part,
independently of the location of \(U(\rho)\), and proves
\[
\mathcal D_{20}\setminus
(\mathcal C_{21}\cup\mathcal T_{21})=\varnothing.
\]
This is consistent with the main manuscript but is additional to the 68
verify_exact_subtraction predicates.

## Compilation

Compilation used the LaTeX skill workflow with bundled Tectonic:

    compile_latex.py ledger-packet-F.tex --compiler tectonic --json

Status: **PASS**, exit code 0. Tectonic performed the necessary rerun and
produced a three-page PDF. The final pass had resolved references and no
box warning.

## Residual findings

None. Packet F is a valid symbolic replacement for the brute-force state
enumeration and preserves every delicate equality owner.

