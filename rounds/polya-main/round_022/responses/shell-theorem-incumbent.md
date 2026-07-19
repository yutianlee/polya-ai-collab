# Round 22 incumbent: the three-dimensional spherical-shell theorem

Date: 2026-07-15

Status: **INCUMBENT RECONSTRUCTION / NOT YET PROMOTED**

Frozen claim:
`state/lemma_packets/TARGET-shell-d3-round22-theorem.md`, SHA-256
`8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228`.

## Theorem

For

$$
A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},
\qquad 0<\rho<1,
$$

and the strict Dirichlet count

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

one has

$$
N_D(A_{\rho,1},\Lambda)
\le \frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}
\qquad(\Lambda\ge0).
\tag{1}
$$

Consequently, for every $0<r<R$,

$$
N_D(A_{r,R},\Lambda)
\le L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.
\tag{2}
$$

## 1. The outer ratio partition is nondegenerate

Retain the promoted small-hole constant

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
\tag{3}
$$

The elementary strict bounds

$$
\frac53<\sqrt3<2,
\qquad 3<\pi<\frac{22}{7}<5
\tag{4}
$$

give $3\sqrt3>5>\pi$ and hence $\omega_0>0$. They also give

$$
\frac{\sqrt3}{2\pi}<\frac13,
\qquad 0<\omega_0<\frac16.
$$

Since $C_*>0$, the denominator in (3) is greater than one. Therefore

$$
0<\rho_*<\omega_0<\frac16<\frac78.
\tag{5}
$$

Thus

$$
(0,1)
=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}
[7/8,1)
\tag{6}
$$

is an exact disjoint partition. The first seam is assigned to the small-hole
owner and the second to the thin-shell owner.

## 2. Zero frequency

Fix $0<\rho<1$. The promoted Sturm--Liouville decomposition gives a positive
Dirichlet spectrum; in fact every radial block satisfies

$$
\lambda_{\ell,n}\ge\frac{\pi^2}{(1-\rho)^2}>0.
$$

Under strict counting no eigenvalue lies below zero, so

$$
N_D(A_{\rho,1},0)=0
=\frac{2}{9\pi}(1-\rho^3)0^3.
\tag{7}
$$

This proves the required equality at $K=0$ directly.

## 3. Positive frequencies on the three ratio owners

Let $K>0$.

### 3.1 Small-hole owner

If $0<\rho\le\rho_*$, the promoted obligation
`SHELL-rho-zero-endpoint` gives, on its exact closed upper face,

$$
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3.
\tag{8}
$$

No limit at $\rho=0$ is used.

### 3.2 Compact-middle owner

Suppose $\rho_*<\rho<7/8$. Let $\mathcal A_{21}$ denote the complete
accepted compact cover retained by
`SHELL-rho-compact-analytic-envelope`. Its exact complement in the compact
ratio-frequency domain is the successor residual $\mathcal D_{21}$. Round 21
proved

$$
\mathcal D_{21}=\varnothing.
\tag{9}
$$

Hence $(\rho,K)$ belongs to an accepted theorem owner; where a theorem uses a
scoped certificate, its promoted analytic bridge supplies the spectral
transfer. Every such theorem owner proves

$$
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3.
\tag{10}
$$

For clarity, (9) includes the following exact final subtraction. The
historical Round 20 residual was

$$
\mathcal D_{20}
=\{\rho_c\le\rho<39/50,
\ k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
$$

Its $K\le200$ part is compact-owned and its $K>200$ part is
aggregate-owned; $K=200$ is assigned only to the compact subtraction owner.
The compact computation supplies 10,580 finite leaves. The aggregate
computation supplies 1,286 base boxes at $K=200$ only, while the universal
$K\ge200$ conclusion is the promoted analytic propagation. The guard
$k_{11}(\rho)>12$ is used only on $\rho_c\le\rho<1$.

The inherited faces are consistent: $\rho=\rho_0$ was removed with the
complete lower closure, $\rho=\rho_c$ is included on the required strict
frequency side, $\rho=39/50$ is optical-owned, $K=k_{11}(\rho)$ is
staircase-owned, and $K=U(\rho)$ is high-energy-owned. Thus no internal seam
is omitted or subtracted twice.

### 3.3 Thin-shell owner

If $7/8\le\rho<1$, the promoted obligation `SHELL-rho-one-endpoint` gives

$$
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3.
\tag{11}
$$

The lower face $\rho=7/8$ is included and the degenerate face $\rho=1$ is
not part of the shell family.

By (6), equations (8), (10), and (11) exhaust every $0<\rho<1$ for $K>0$.
Together with (7),

$$
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge0).
\tag{12}
$$

No floor is recomputed in this assembly. Every input uses the same strict
count. At a shell eigenfrequency the threshold eigenvalue is excluded, and
if several angular channels share that eigenvalue their multiplicities add
inside the same strict count.

## 4. Convert to the Polya normalization

In dimension three,

$$
\omega_3=\frac{4\pi}{3},
\qquad
L_3=\frac{\omega_3}{(2\pi)^3}
=\frac{4\pi/3}{8\pi^3}
=\frac1{6\pi^2}.
\tag{13}
$$

The unit shell has volume

$$
|A_{\rho,1}|
=\frac{4\pi}{3}(1-\rho^3),
$$

so

$$
L_3|A_{\rho,1}|
=\frac1{6\pi^2}\frac{4\pi}{3}(1-\rho^3)
=\frac{2}{9\pi}(1-\rho^3).
\tag{14}
$$

For $\Lambda\ge0$, take $K=\sqrt\Lambda$. Then
$K^3=\Lambda^{3/2}$, and (12)--(14) prove (1).

## 5. Scale to every bounded spherical shell

Let $0<r<R$, put $\rho=r/R$, and write $D_Ru(x)=R^{-3/2}u(x/R)$ for the
unitary dilation from $L^2(A_{\rho,1})$ to $L^2(A_{r,R})$. The Dirichlet
quadratic form transforms by

$$
\int_{A_{r,R}}|\nabla D_Ru|^2,dx
=R^{-2}\int_{A_{\rho,1}}|\nabla u|^2,dx.
$$

Thus

$$
A_{r,R}=R A_{\rho,1},
\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}).
\tag{15}
$$

The strict inequality defining the count is preserved exactly:

$$
\lambda_j^D(A_{r,R})<\Lambda
\Longleftrightarrow
\lambda_j^D(A_{\rho,1})<R^2\Lambda.
$$

Therefore

$$
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda).
\tag{16}
$$

Applying (1) at $R^2\Lambda$ gives

$$
\begin{aligned}
N_D(A_{r,R},\Lambda)
&\le\frac{2}{9\pi}(1-\rho^3)(R^2\Lambda)^{3/2}\\
&=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}\\
&=L_3|A_{r,R}|\Lambda^{3/2}.
\end{aligned}
\tag{17}
$$

This derivation is valid for every $R>0$, including $R<1$; no monotonicity in
$R$ is used.

## Scope

This incumbent reconstructs the spectral theorem and its scaling corollary
only. It does not promote any graph node, prove non-tiling, establish novelty
or priority, or resolve another project track. Its conclusion must still pass
a clean-room reconstruction, independent provenance audit, and fresh
adversarial theorem referee.
