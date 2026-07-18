# Verdict

| Question                                        | Assessment                                                                                                                                                                                   |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Were the proposed simplifications incorporated? | **All substantive mathematical simplifications were incorporated.** Some source-level and editorial cleanup remains.                                                                         |
| Is the spectral proof rigorous?                 | **I found no fatal gap in the proof of the Dirichlet Pólya inequality.** The live implication chain is coherent, equality walls are handled correctly, and the critical constants check out. |
| Is the complete submitted package ready?        | **Not quite.** The PDF and TeX are not synchronized, the uploaded source tree is not self-contained, and several references to retired material remain.                                      |


I treated `spherical-shell-polya-proof(3).tex/.pdf` and the nine-page updated analytic supplement as the current version.

---

# 1. Inclusion of the simplification recommendations

## Substantive mathematical recommendations: included

The updated proof now has exactly the simplified structure proposed previously:

[
N_D\le P,\qquad
W-P=D_{\mathrm{rad}}-E_{\mathrm{ang}},
]

followed by:

[
\begin{array}{c|c|c}
\text{frequency} & \text{ratio} & \text{owner}\ \hline
0\le K\le \pi/(1-\rho) & 0<\rho<1 & \text{no-mode comparison}\
K>\pi/(1-\rho) & 0<\rho<39/50 & \text{global defect theorem}\
K>\pi/(1-\rho) & 39/50\le\rho<1 & \text{optical theorem}.
\end{array}
]

The manuscript explicitly removes the finite staircase, 38-state theorem, and 611-row ledger from the live implication chain. 

More specifically, the updated supplement contains all four proposed analytic improvements:

1. the ratio-dependent slope cap
   [
   -A'(z)\le \frac{\arccos\rho}{\pi};
   ]

2. the ratio-sharp angular-block payment
   [
   E_{\mathrm{ang}}
   <
   \frac{1-\rho^2}{6}K^2
   ---------------------

   N\left(\frac{3\pi}{8\arccos\rho}-\frac14\right);
   ]

3. the tangent-envelope minorant
   [
   L_\sharp(t)=
   \begin{cases}
   t^2/2,&t\le1/4,\
   t/4-1/32,&t\ge1/4;
   \end{cases}
   ]

4. reduction of the radial payment to the universal ball quarter-layer
   [
   B_0(K)=\int_0^{1/4}R_B(t)^2,dt,
   ]
   followed by the elementary scalar convexity closure.

The supplement itself describes precisely this live chain and states that the old finite machinery is now only historical audit material.  The main paper summarizes the same estimates, including the degree-nine base inequality and the positive (K)-convexity bound. 

The no-mode argument is also now the clean one-dimensional comparison: the strict count vanishes up to and including (K=\pi/(1-\rho)), with the equality level excluded by the strict convention. 

## Recommendations only partially incorporated

The compiled paper is mathematically much shorter, but the source has not yet been fully cleaned.

### 1. Retired proofs remain inside the main TeX source

The old small-hole, compact-middle, staircase, zero-registry, and residual-subtraction material is still present inside three large `\iffalse ... \fi` blocks. It does not affect the compiled theorem, but the source remains approximately as large and difficult to maintain as the previous proof.

For the final repository, those blocks should be moved to an archival file or deleted from the submission branch.

### 2. The uploaded source package does not compile standalone

The main source invokes

```tex
\input{analytic/ratio-sharp-global-closure-summary.tex}
```

and the supplement invokes

```tex
\includepdf{analytic/compiled/ratio-sharp-global-closure.pdf}
```

but neither referenced file is present in the uploaded package. The mathematical content exists in the compiled PDFs, but the source submission is not reproducible as uploaded.

### 3. There are stale internal references

The proof map still refers to “Part VII of the supplement,” whereas the updated supplement has only one substantive part, labelled Part I. Compare the old wording in the proof map with the new supplement dependency graph.  

### 4. Appendix A is inherited from the retired proof

The current Appendix A still lists:

* contiguous-order zero interlacing;
* the annulus floor-sum inequalities;
* Lorch’s first-zero bounds;

as external inputs to “the proof above.” These were inputs to the retired finite staircase, but they are no longer used by the live simplified proof. The active spectral argument now uses only:

* standard spherical harmonics and regular Sturm–Liouville theory;
* standard Bessel identities, Nicholson’s formula and limiting formulas;
* the FLPS real-order phase enclosure and the annular phase-difference estimate.

The current Appendix therefore overstates the external dependency set. 

### 5. The optional editorial separation was not made

The non-tiling theorem remains in the main spectral paper. This is not mathematically problematic, but it was one optional recommendation: the non-tiling argument is logically independent and could be moved to an appendix or short separate note.

---

# 2. Rigor of the current proof

## Spectral theorem

I found **no fatal gap** in the proof of Theorem 1.1.

I checked the following parts in detail.

### Exact separation and phase enumeration

The unitary transformation (R(r)\mapsto u(r)=rR(r)), the block operator

[
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
]

the spherical-harmonic multiplicities (2\ell+1), compactness of the full resolvent, and completeness of the separated eigenfunctions are correctly handled.

The determinant

[
D_{\nu,\rho}(k)
===============

J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k)
]

is factored with the correct sign as

[
D_{\nu,\rho}(k)
===============

M_\nu(\rho k)M_\nu(k)
\sin!\left(\theta_\nu(k)-\theta_\nu(\rho k)\right).
]

The proof that the phase difference is strictly increasing uses

[
\frac{d}{dk}
\bigl(\theta_\nu(k)-\theta_\nu(\rho k)\bigr)
============================================

\frac{2}{\pi k}
\left(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2}\right)>0,
]

which follows from the strict decrease of (M_\nu(x)^2). Root simplicity and strict spectral-wall bookkeeping are also correct.

### Phase-to-proxy bridge

The published phase estimates are applied in the correct direction. In particular, the manuscript correctly distinguishes:

* an actual phase wall, where the radial integer on the wall is excluded;
* a proxy wall, where retaining the ordinary floor still gives an upper bound;
* an angular half-integer wall, where the equality channel is excluded.

The imported annulus estimates are stated for real Bessel order, so using them at half-integer orders requires no interpolation. This is consistent with the published annulus machinery. 

### Exact layer cake

The identity

[
P=\sum_{x_n<T}M(R(x_n))^2,
\qquad x_n=n-\frac14,
]

correctly follows by interchanging two finite strict counts. The equality case

[
R(x_n)=m+\frac12
]

is handled correctly: the strict angular count is (m), not (m+1).

### Ratio-sharp angular theorem

The estimate

[
x_n-t
=====

\int_{r_n}^{R(t)}q(s),ds
\le
\frac{\arccos\rho}{\pi}(R(t)-r_n)
]

has the correct orientation. The left blocks are disjoint and lie in ([0,T]), and the final inverse-area identity

[
\int_0^T R(t),dt
================

# \int_0^K A(z),dz

\frac{1-\rho^2}{8}K^2
]

is correct.

### Stieltjes signs and the tangent envelope

The signs in the retained-remainder argument are correct:

* (dg<0) on ((0,\tau));
* (dg>0) on ((\tau,T));
* therefore replacing the sawtooth primitive by (L_\sharp\le\mathcal W) on the decreasing branch gives a lower bound in the stated direction.

The interface cancellation and the resulting (g(\tau)/8) payment are also correct.

### Ball quarter-layer and scalar algebra

The inverse turning estimate

[
R_B(t)\ge K-CK^{1/3}t^{2/3},
\qquad C=\frac{(3\pi)^{2/3}}2,
]

and the integrated coefficients (\alpha,\beta) check out.

I also independently recalculated the exact reserves occurring in the two scalar closures. In particular, the values

[
\frac{39569}{2772225000}>0,
\qquad
\frac{14817541}{472867032960000}>0,
\qquad
\frac{47447}{443682}>0
]

are arithmetically correct. The optical low and high screens overlap on their common equality face, so there is no frequency gap. 

### Final parameter assembly

The three owners are exhaustive, and the dilation step

[
N_D(A_{r,R},\Lambda)
====================

N_D(A_{r/R,1},R^2\Lambda)
]

produces exactly

[
\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
====================================

L_3|A_{r,R}|\Lambda^{3/2}.
]

No uncovered ratio or frequency face remains.

## Issues that should be corrected before submission

### 1. The compiled PDF and the TeX source disagree in the non-tiling proof

The provided PDF says:

> “Thus (p\in T_a). The point (p) is not in (T_a).”

The limiting argument only proves

[
p\in\overline{T_a}.
]

The next paragraph then proves (p\notin T_a), hence (p\in\partial T_a). As written in the PDF, the two consecutive sentences are contradictory. 

The uploaded `.tex` source already contains the correct statement

```tex
Thus \(p\in\overline{T_a}\).
```

so this is a stale-PDF problem rather than an unresolved mathematical problem. Recompilation will fix it. It does not affect the spectral theorem.

### 2. Prove or cite the lower turning estimate

The supplement uses

[
G_1(s)\ge
\frac{2\sqrt2}{3\pi}(1-s)^{3/2}
]

without giving its derivation. One line is sufficient:

[
\arccos u\ge\sqrt{2(1-u)}
]

because (1-\cos t\le t^2/2), and integration over ([s,1]) gives the result.

### 3. Justify the rational bounds on (\pi)

The scalar closure invokes

[
\frac{157}{50}<\pi<\frac{22}{7}
]

without proof or citation. This is not a substantive gap, but the supplement advertises an exact, self-contained rational argument. A short lemma or reference should therefore be included.

### 4. Expand two terse monotonicity statements

For example, the proof says that

[
\frac{z}{\arccos(z/K)}
]

increases with (z). This is true, but a derivative calculation would remove a possible reviewer objection. The same applies to one or two of the scalar derivative comparisons.

## Rigor conclusion

The correct assessment is:

[
\boxed{\text{No fatal gap found in the spectral theorem.}}
]

The non-tiling theorem has an obvious closure typo in the supplied PDF, already corrected in the TeX source. The remaining issues concern self-containedness, stale references, and reproducible packaging rather than the central mathematical implication.