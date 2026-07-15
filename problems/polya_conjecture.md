# Pólya Conjecture Collaboration Problem Statement

## Working Target and Current Internal Status

The project target was exact Dirichlet Pólya for a natural non-tiling
Euclidean domain class. Round 22 completes that target internally for the
full family of genuine bounded three-dimensional spherical shells. Here
`new` means newly completed within this project, not novel in the literature.

The unit-shell normalization is:

```text
A_{rho,1} = { x in R^3 : rho < |x| < 1 }, 0 < rho < 1.
```

With Dirichlet boundary conditions, let

```text
0 < lambda_1^D <= lambda_2^D <= ...
```

be the eigenvalues of the negative Laplacian on `A_{rho,1}`.

Use the strict counting convention:

```text
N_D(Omega,Lambda) = #{ j : lambda_j^D(Omega) < Lambda }.
```

The internally proved inequality is:

```text
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
```

for every `Lambda >= 0`, where

```text
L_3 = omega_3 / (2*pi)^3 = 1/(6*pi^2).
```

Equivalently, for every

```text
A_{r,R} = { x in R^3 : r < |x| < R }, 0 < r < R,
```

and every `Lambda >= 0`, the reviewed theorem proves

```text
N_D(A_{r,R}, Lambda)
<= (2/(9*pi)) (R^3-r^3) Lambda^(3/2)
= L_3 |A_{r,R}| Lambda^(3/2).
```

The scaling identity is

```text
N_D(A_{r,R}, Lambda) = N_D(A_{r/R,1}, R^2 Lambda).
```

A separate reviewed theorem proves that the same complete `0 < r < R`
family does not tile `R^3` by congruent rigid-motion copies with
pairwise-disjoint interiors and exact or almost-everywhere coverage. The
audited conclusion also covers the corresponding closed-copy convention
after removal of the countable null boundary union.

The authoritative application is commit `d8fe505`, and the graph SHA-256 is
`b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`.
The source-final judge and application audit are
`rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md` and
`rounds/polya-main/round_022/reviews/state-patch-application-audit-source-utf8-final.md`.

## Audited Shell Spectral Formula

For `A_{rho,1} subset R^d`, angular momentum `ell=0,1,2,...` gives

```text
nu = ell + (d-2)/2.
```

The Dirichlet radial eigenvalues are the positive zeros in
`k=sqrt(Lambda)` of

```text
F_{nu,rho}(k) =
J_nu(rho k) Y_nu(k) - Y_nu(rho k) J_nu(k).
```

The multiplicity is the dimension of spherical harmonics of degree `ell`; in dimension 3 this is

```text
m_{ell,3} = 2 ell + 1.
```

The audited counting function is

```text
N_D(A_{rho,1}, Lambda)
= sum_{ell >= 0} m_{ell,3}
  #{ k > 0 : F_{ell+1/2,rho}(k)=0, k^2 < Lambda }.
```

Round 1 audited this formula before it was used as a proof dependency. The
completed theorem retains the strict counting convention at every spectral
wall and treats `Lambda=0` by positive spectrum.

## Completed Shell Strategy and Open Parallel Tracks

The shell route completed in Rounds 1--22 was:

1. Reproduce the FLPS disk/ball proof architecture.
2. Audit the annulus proof, especially Bessel cross-products and lattice-counting estimates.
3. Build shell-specific Bessel cross-product phase enclosures.
4. Convert the shell count into a multiplicity-weighted lattice-count problem.
5. Prove high-energy estimates analytically.
6. Close the finite low-energy window with certified interval arithmetic.

Parallel tracks:

- Dirichlet ellipses through Mathieu-function phase enclosures remain open.
- A Jiang-Lin-style exact certificate theorem for a smooth non-tiling
  comparison family remains open.

`COMP-certified-bessel` remains `diagnostic_only` and detached from the
completed theorem path. Its two certified pilots remain regression evidence.

## Non-Claim Rules

- The graph records an internal proof for the spherical-shell class only. It
  does not settle the general Pólya conjecture.
- No literature novelty, publication priority, first-proof, or
  publication-readiness claim follows from the internal status. Human
  reconstruction of every bottleneck lemma, manuscript-level checking, and
  an independent current literature search remain required before external
  publication claims.
- Floating-point numerics are diagnostic only unless wrapped in a certified finite-window proof obligation.
- External theorems require source cards with exact statements and hypotheses.
