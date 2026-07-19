# Frozen Candidate Claim: First Angular Bands Above the Zero-Count Wall

Status: **FROZEN CLAIM ONLY / NOT PROVED / NOT PROMOTED**.

Round: 17.

Baseline commit:
`047c9ef5c4fe2329d73d3568c1ac48654dd18585`.

Frozen residual packet:
`state/lemma_packets/SHELL-rho-compact-round17.md`, SHA-256
`eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e`.

Permitted spectral packet:
`state/lemma_packets/SHELL-sturm-liouville-completeness.md`, SHA-256
`6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8`.

This file contains the exact candidate statement and falsification walls but
no incumbent proof, numerical exploration, executable ledger, or review.

## Candidate C17

Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_1(\rho)=\sqrt{z_\rho^2+2},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
\tag{1}
$$

Reconstruct or refute the following claim without consulting an incumbent
proof:

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_2(\rho)
}
\tag{2}
$$

implies

$$
\boxed{
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{3}
$$

The proposed genuinely new analytic portion is

$$
\boxed{
\mathcal C_{17}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad z_\rho<K\le k_2(\rho)
\right\}.
}
\tag{4}
$$

An initial PASS must independently prove both (3) on the complete closed
band (2) and the exact set relation

$$
\mathcal C_{17}\subset\mathcal D_{16}
\tag{5}
$$

using the frozen residual predicate. It must also report whether the complete
Round 8 box \(B_0\) is contained in \(\mathcal C_{17}\). These set statements
are bookkeeping consequences to be proved, not permitted spectral inputs.

## Permitted inputs

Only the following may be used before the initial verdict:

1. the two hash-authenticated packets listed above;
2. the strict counting convention recorded in the spectral packet;
3. elementary one-dimensional Dirichlet Sturm--Liouville theory and the
   min--max principle;
4. exact rational arithmetic and independently reconstructed elementary
   inequalities for \(\pi\).

No Bessel-root certificate, phase enclosure, incumbent Round 17 response,
Round 17 certification artifact, sampled plot, floating-point root, external
review, or desired theorem conclusion is a permitted input.

## Mandatory falsification walls

The initial reconstruction must explicitly test:

- \(\rho=\rho_c\) and \(\rho=7/8\), with the correct old face owner;
- \(K=z_\rho\), \(K=k_1(\rho)\), and \(K=k_2(\rho)\), including strict
  spectral endpoint conventions;
- \(\rho=1/2\) and \(\rho=5/6\), where formulas or old mask branches change;
- the first two radial indices and angular orders \(\ell=0,1,2\), with full
  multiplicities and possible cross-order eigenvalue coincidences;
- exclusion of every remaining radial and angular mode on the whole band;
- every monotonicity, denominator, square root, squaring, inverse, and
  rational bound used for a uniform constant;
- all active upper branches of the frozen mask and the global
  \(K=295^2\) face;
- every closed face of \(B_0\) if its containment is asserted.

The reviewer must return **PASS** or **FAIL** and identify the first
unsupported implication before reading any incumbent proof. Agreement with
the candidate is not verification.
