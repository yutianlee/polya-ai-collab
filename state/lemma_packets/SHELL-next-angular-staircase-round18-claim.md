# Frozen Candidate Claim: Next Angular Staircase Through the First Radial Barrier

Status: **FROZEN CLAIM ONLY / NOT PROVED / NOT PROMOTED**.

Round: 18.

Baseline commit:
`1caf24a0f0732038e9d162990dd3c2201daad85d`.

Frozen residual packet:
`state/lemma_packets/SHELL-rho-compact-round18.md`, SHA-256
`7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9`.

Permitted spectral packet:
`state/lemma_packets/SHELL-sturm-liouville-completeness.md`, SHA-256
`6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8`.

Permitted accepted Round 17 claim packet:
`state/lemma_packets/SHELL-first-angular-bands-round17-claim.md`, SHA-256
`c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77`.
Its promoted status is authenticated by the frozen residual packet; this
historical claim file is permitted only for its proof-free statement.

Permitted source cards:

- `sources/lorch_bessel_zeros.md`, SHA-256
  `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4`;
- `sources/flps_balls.md`, SHA-256
  `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38`.

This file contains only the candidate statement, proposed constants,
permitted inputs, and falsification walls. It contains no incumbent proof,
executable ledger, sampled computation, certificate, or review.

## Candidate C18

Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}
\quad(m=2,3,4,5).
\tag{1}
$$

Reconstruct or refute the following claim without consulting an incumbent
proof:

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_5(\rho)
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
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K\le k_5(\rho)
\right\}.
}
\tag{4}
$$

An initial PASS must independently prove (3) on the complete closed band
(2), the exact inclusion

$$
\mathcal C_{18}\subset\mathcal D_{17},
\tag{5}
$$

and the exact subtraction formula

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
\rho_c\le\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
\tag{6}
$$

Equations (5)--(6) are bookkeeping conclusions to be proved from the
frozen predicate, including the strict comparison $k_5(\rho)<U(\rho)$.
They are not permitted spectral inputs. The complete face $\rho=7/8$ and
the lower face $K=k_2(\rho)$ already have accepted owners; the proposed
new owner includes $K=k_5(\rho)$.

## Proposed staircase data

The only proposed rational first-entry thresholds are

$$
c_2=\frac{51}{10},
\qquad
c_3=\frac{13}{2},
\qquad
c_4=\frac{15}{2},
\tag{7}
$$

with proposed ratio splits

$$
r_2=\frac3{10},
\qquad
r_3=r_4=\frac12.
\tag{8}
$$

The proposed cumulative strict-count caps before the corresponding next
angular entry are

$$
4,qquad 9,qquad 16,qquad 25.
\tag{9}
$$

These constants and caps are part of the claim to be checked, not proved
facts supplied to the reviewer. No statement is proposed for
$K>k_5(\rho)$.

## Permitted inputs

Before the initial verdict, only the following may be used:

1. the five hash-authenticated packets and source cards listed above;
2. the strict counting convention in the spectral packet;
3. the externally sourced statements

   $$
   j_{5/2,1}>\frac{51}{10},
   \qquad
   j_{7/2,1}>\frac{13}{2},
   \qquad
   j_{9/2,1}>\frac{15}{2};
   $$

4. elementary one-dimensional Dirichlet Sturm--Liouville theory, the
   variational min--max principle, and extension by zero for $H_0^1$;
5. exact rational arithmetic and independently reconstructed elementary
   inequalities for $\pi$.

The fixed-angular-subspace comparison

$$
\lambda_{\ell,1}^{\mathrm{shell}}(\rho)
\ge j_{\ell+1/2,1}^{,2}
\tag{10}
$$

is **not** a permitted lemma. It must be proved internally, including the
form domains and the preservation of the angular channel under extension
by zero. The Lorch source must not be cited for shell cross-product zeros,
higher radial modes, multiplicity counts, or Weyl estimates.

No Round 18 incumbent response, Round 18 ledger, source-audit review,
certificate, sampled root, plot, floating-point margin, desired theorem
conclusion, or agent consensus is a permitted input.

## Mandatory falsification walls

The initial reconstruction must explicitly test:

- $\rho=\rho_c,3/10,1/2,5/6,7/8$ and both one-sided traces at every
  interior split;
- $K=z_\rho,k_2(\rho),k_3(\rho),k_4(\rho),k_5(\rho)$, including strict
  spectral endpoint conventions;
- $K=51/10,13/2,15/2$, including every empty or degenerate subband created
  by its ordering against the $k_m(\rho)$ walls;
- $K=2z_\rho$ and $K=k_6(\rho)$ as attempted counterexamples to the claimed
  radial and angular exclusions, without extending the theorem beyond
  $k_5$;
- radial indices $n=1,2$ and angular orders $\ell=0,1,2,3,4,5$, with full
  multiplicities $2\ell+1$, all remaining-mode exclusions, and possible
  cross-order coincidences;
- the form-domain proof and inequality direction in (10), rather than an
  unlabelled appeal to global domain monotonicity;
- the scope $\nu>-1$, strict direction, positive-zero convention, and
  spherical-Bessel identification behind all three sourced bounds;
- every Weyl-payment threshold corresponding to the proposed caps in (9),
  on both sides of each ratio split in (8);
- every monotonicity, derivative sign, denominator, square root, squaring,
  inverse, and extremal substitution used to make a constant uniform;
- the strict comparison $k_5<U$ against every active branch of $U$, the
  old $K=295^2$ face, and the exact inclusions and face assignments in
  (5)--(6);
- the fact that $B_0$ and $B_1$ were already absorbed by $\mathcal C_{17}$
  and are not subtracted again.

The reviewer must return **PASS** or **FAIL** and identify the first
unsupported implication before reading any incumbent proof, ledger,
source-audit review, certification artifact, or judge draft. Agreement with
the candidate is not verification.
