# Pólya Conjecture Collaboration Problem Statement

## Working Target

The project target is exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.

The first theorem target is the spherical shell in dimension 3:

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

The target inequality is:

```text
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
```

for every `Lambda >= 0`, where

```text
L_3 = omega_3 / (2*pi)^3 = 1/(6*pi^2).
```

Equivalently, after scaling, start with fixed `rho`, then compact intervals `rho in [rho_0,rho_1] subset (0,1)`, then endpoint regimes `rho -> 0` and `rho -> 1`.

## Shell Spectral Formula To Audit

For `A_{rho,1} subset R^d`, angular momentum `ell=0,1,2,...` gives

```text
nu = ell + (d-2)/2.
```

The Dirichlet radial eigenvalues are expected to be zeros in `k=sqrt(Lambda)` of

```text
F_{nu,rho}(k) =
J_nu(rho k) Y_nu(k) - Y_nu(rho k) J_nu(k).
```

The multiplicity is the dimension of spherical harmonics of degree `ell`; in dimension 3 this is

```text
m_{ell,3} = 2 ell + 1.
```

The counting function should therefore be audited in the form

```text
N_D(A_{rho,1}, Lambda)
= sum_{ell >= 0} m_{ell,3}
  #{ k > 0 : F_{ell+1/2,rho}(k)=0, k^2 < Lambda }.
```

Round 1 must audit this formula before using it as a proof dependency.

## Strategy

The intended route is:

1. Reproduce the FLPS disk/ball proof architecture.
2. Audit the annulus proof, especially Bessel cross-products and lattice-counting estimates.
3. Build shell-specific Bessel cross-product phase enclosures.
4. Convert the shell count into a multiplicity-weighted lattice-count problem.
5. Prove high-energy estimates analytically.
6. Close the finite low-energy window with certified interval arithmetic.

Parallel tracks:

- Dirichlet ellipses through Mathieu-function phase enclosures.
- A Jiang-Lin-style exact certificate theorem for a smooth non-tiling comparison family.

## Non-Claim Rules

- No agent may claim a proof of Dirichlet Pólya for shells without complete analytic estimates, source dependencies, parameter handling, and finite verification.
- Floating-point numerics are diagnostic only unless wrapped in a certified finite-window proof obligation.
- External theorems require source cards with exact statements and hypotheses.
