# Round 22 proof-free theorem packet: Dirichlet Polya for 3D spherical shells

Date: 2026-07-15

Status: **FROZEN CLAIM CANDIDATE / NOT YET PROMOTED**

Primary obligations:

- `SHELL-rho-compact`;
- `SHELL-rho-uniformity`; and
- `TARGET-shell-d3`.

This packet states the theorem, exact domains, permitted dependencies, and
review obligations. It contains no proof and does not change graph status.

## 1. Counting convention and unit-shell claim

For a bounded Dirichlet domain, use the strict counting convention

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

with eigenvalues repeated according to multiplicity. For

$$
A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},
\qquad 0<\rho<1,
$$

the claim to reconstruct is

$$
\boxed{
N_D(A_{\rho,1},\Lambda)
\le \frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}
\qquad(\Lambda\ge0).
}
\tag{T1}
$$

Equivalently, with $K=\sqrt\Lambda$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le W(\rho,K):=\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge0).
}
\tag{T2}
$$

At $K=0$, both sides must be shown to equal zero. No continuity argument
from $K>0$ may replace this check.

## 2. Exact ratio partition and seam owners

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The reconstruction must use the disjoint partition

$$
\boxed{
(0,1)
=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}
[7/8,1).
}
\tag{T3}
$$

Here $\rho=\rho_*$ is owned by the small-hole theorem, and $\rho=7/8$ is
owned by the thin-shell theorem. The proof must establish
$0<\rho_*<7/8$ exactly. The compact-middle reconstruction must also audit
every inherited internal seam, including

$$
\rho_0=\frac1{\sqrt{337}},\qquad
\rho_c=\frac1{1+2\pi},\qquad
\frac{39}{50},
$$

and all moving frequency faces. Those internal overlaps do not change the
three disjoint outer owners in (T3).

## 3. Permitted proved inputs

The theorem reconstruction may use only the following promoted obligations
and their authenticated positive evidence:

1. `CONV-strict-counting`;
2. `SHELL-sturm-liouville-completeness`, including positivity of the
   Dirichlet spectrum and exact multiplicities;
3. `SHELL-rho-zero-endpoint`, exactly on
   $0<\rho\le\rho_*$ and $K\ge0$;
4. `SHELL-rho-compact-analytic-envelope`, including the complete accepted
   compact cover through Round 20 and `SHELL-exact-d20-closure` with
   $\mathcal D_{21}=\varnothing$; and
5. `SHELL-rho-one-endpoint`, exactly on
   $7/8\le\rho<1$ and $K\ge0$.

For the compact-middle input, the Round 21 finite/analytic boundary is fixed:

- 10,580 compact certificate leaves own only
  $7/51\le\rho\le39/50$, $12\le K\le200$;
- 1,286 aggregate certificate boxes own only base predicates at $K=200$;
- the universal aggregate conclusion for $K\ge200$ is analytic; and
- the exact residual split assigns $K=200$ to the compact subtraction owner.

The guard $k_{11}(\rho)>12$ may be used only for
$\rho_c\le\rho<1$. Superseded unscoped, stale-hash, and cache-vulnerable
Round 21 artifacts are forbidden as positive inputs.

Elementary Euclidean volume, the standard value
$\omega_3=4\pi/3$, and unitary dilation of the Dirichlet Laplacian may be
rederived in the theorem proof. No Weyl remainder, tiling theorem, numerical
experiment, or new Bessel-zero assertion is permitted.

## 4. Required unit-shell reconstruction

The proof must separately establish:

1. $K=0$: positivity and strict counting give
   $N_D(A_{\rho,1},0)=0=W(\rho,0)$;
2. $K>0$, $0<\rho\le\rho_*$: apply only the promoted small-hole endpoint;
3. $K>0$, $\rho_*<\rho<7/8$: reconstruct the complete accepted compact
   cover and use empty $\mathcal D_{21}$, without substituting a historical
   residual or a larger certificate domain;
4. $K>0$, $7/8\le\rho<1$: apply only the promoted thin endpoint; and
5. the three cases exhaust the domain with the seam owners in (T3).

At every eigenvalue or phase wall, the proof must retain the strict endpoint
rule. It must not replace a strict channel count by an ordinary floor when
the phase is an integer multiple of $\pi$.

## 5. Weyl normalization

The theorem proof must rederive

$$
L_3=\frac{\omega_3}{(2\pi)^3}=\frac1{6\pi^2},
\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
$$

and hence

$$
\boxed{
L_3|A_{\rho,1}|
=\frac{2}{9\pi}(1-\rho^3).
}
\tag{T4}
$$

Thus (T1) is exactly the three-dimensional Dirichlet Polya inequality, not a
different normalization or a two-term Weyl estimate.

## 6. Arbitrary-radius corollary

For

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},
\qquad 0<r<R,
$$

put $\rho=r/R$. The proof must derive, not merely assert,

$$
A_{r,R}=R A_{\rho,1},
\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}),
$$

so that

$$
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda).
\tag{T5}
$$

Together with

$$
|A_{r,R}|=\frac{4\pi}{3}(R^3-r^3),
$$

the required corollary is

$$
\boxed{
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2}
\qquad(\Lambda\ge0).
}
\tag{T6}
$$

## 7. Mandatory falsification cases

- $K=0$ and the first positive eigenfrequency;
- $\rho=\rho_*$ from both adjacent descriptions;
- $\rho=7/8$ from both adjacent descriptions;
- the internal faces $\rho=\rho_0$, $\rho=\rho_c$, and $\rho=39/50$;
- $K=200$ and both sides of that face;
- every inherited high-frequency and moving staircase wall;
- a shell eigenvalue shared by several angular channels;
- an integer phase wall, where the strict channel count is one less than the
  ordinary floor;
- $\Lambda=0$ under the change $K=\sqrt\Lambda$;
- arbitrary $R\ne1$, including $R<1$ and $R>1$;
- the limits $r\downarrow0$ and $r\uparrow R$, neither of which is a member
  of the bounded shell class at equality; and
- any accidental replacement of $R^2\Lambda$ by $R^{-2}\Lambda$ in (T5).

## 8. Scope and promotion rule

This packet claims only the spectral inequality for three-dimensional
spherical shells and its dilation corollary. It does not prove that shells
are non-tiling, does not solve the ellipse or certificate-family tracks, and
makes no novelty or publication-priority claim.

Before promotion, the frozen bytes must pass:

1. an independent packet-scope and dependency audit;
2. a fresh clean-room theorem reconstruction that does not read an incumbent
   proof;
3. an independent assembly/provenance audit;
4. a distinct adversarial referee instructed to assume (T1) false; and
5. a separately audited State Patch.

Program-target promotion additionally requires a separate non-tiling theorem,
adversarial geometry review, scoped graph obligation, and program-scope audit.
