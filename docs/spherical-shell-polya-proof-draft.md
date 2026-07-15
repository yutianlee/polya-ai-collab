# A Dirichlet Pólya Inequality for Three-Dimensional Spherical Shells

Working proof draft — 15 July 2026

## Status of this draft

This document reorganizes the internally validated proof into manuscript
form. It proves a theorem for the class of genuine three-dimensional
spherical shells. It does not claim the general Pólya conjecture, literature
novelty, priority, or publication readiness.

The final theorem assembly and the non-tiling argument are written out. The
long compact-middle argument is presented as a sequence of precise lemmas,
with exact domains, seams, constants, and links to the audited detailed
proofs. A journal submission must move those detailed arguments and the
computer-assisted contracts into conventional appendices rather than cite
repository workflow language.

## Abstract

For \(0<r<R\), let

\[
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}.
\]

We prove, with the strict Dirichlet counting convention, that

\[
N_D(A_{r,R},\Lambda)
\le L_3|A_{r,R}|\Lambda^{3/2},
\qquad
L_3=\frac1{6\pi^2},
\qquad \Lambda\ge0.
\]

The proof separates variables, converts the radial spectrum into a strict
multiplicity-weighted phase count, and combines analytic endpoint estimates,
finite angular/radial mode inventories, and a rigorously certified final
compact window. We also give an elementary proof that no genuine spherical
shell tiles \(\mathbb R^3\) by congruent rigid-motion copies with disjoint
interiors, under either exact or almost-everywhere coverage.

## 1. Main results and conventions

The eigenvalues of the Dirichlet Laplacian on a bounded domain \(\Omega\) are
listed with multiplicity as

\[
0<\lambda_1^D(\Omega)\le\lambda_2^D(\Omega)\le\cdots.
\]

Throughout we use the strict counting function

\[
N_D(\Omega,\Lambda)
:=\#\{j:\lambda_j^D(\Omega)<\Lambda\}.
\tag{1.1}
\]

This convention matters at every spectral wall.
We write \(\mathbb N=\{1,2,3,\ldots\}\) and
\(\mathbb N_0=\{0,1,2,\ldots\}\).

### Theorem 1.1 — spectral inequality

For every \(0<r<R\) and every \(\Lambda\ge0\),

\[
\boxed{
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.}
\tag{1.2}
\]

### Theorem 1.2 — non-tiling

For every \(0<r<R\), no family of congruent rigid-motion copies of
\(A_{r,R}\) has pairwise-disjoint interiors and covers \(\mathbb R^3\)
exactly or up to a three-dimensional Lebesgue-null set. The same conclusion
holds when coverage is formulated using closed shells.

The two theorems concern literally the same complete shell family. Theorem
1.2 is logically independent of the spectral proof.

## 2. Separation of variables and strict phase counting

We first normalize the outer radius to one and write

\[
A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},
\qquad 0<\rho<1.
\]

### Proposition 2.1 — exact separated spectrum

Under spherical-harmonic decomposition and the unitary radial substitution
\(u(r)=rR(r)\), the Dirichlet Laplacian is the orthogonal sum

\[
-\Delta_{A_{\rho,1}}^D
\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}L_\ell,
\qquad
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\tag{2.1}
\]

where \(L_\ell\) acts on \(H^2(\rho,1)\cap H_0^1(\rho,1)\). Each radial
block has a positive, simple, complete spectrum. The full resolvent is
compact because

\[
\|(L_\ell+1)^{-1}\|
\le \frac1{1+\ell(\ell+1)}\longrightarrow0.
\tag{2.2}
\]

Put \(\nu=\ell+\tfrac12\). The positive eigenfrequencies of the \(\ell\)-th
block are exactly the positive zeros of

\[
F_{\nu,\rho}(k)
=J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k).
\tag{2.3}
\]

For \(K>0\), choose the continuous Bessel phase by

\[
J_\nu(x)+iY_\nu(x)=M_\nu(x)e^{i\theta_\nu(x)},
\qquad \theta_\nu(0+)=-\frac\pi2,
\]

and define

\[
\Psi_{\nu,\rho}(K)=\theta_\nu(K)-\theta_\nu(\rho K),
\qquad
\gamma_{\rho,K}(\nu)=\frac{\Psi_{\nu,\rho}(K)}\pi.
\tag{2.4}
\]

The function \(K\mapsto\Psi_{\nu,\rho}(K)\) is strictly increasing from
zero to infinity, and

\[
F_{\nu,\rho}(K)=0
\quad\Longleftrightarrow\quad
\Psi_{\nu,\rho}(K)\in\pi\mathbb N.
\tag{2.5}
\]

Consequently,

\[
N_D(A_{\rho,1},K^2)
=\sum_{\nu_\ell<K}2\nu_\ell
[\gamma_{\rho,K}(\nu_\ell)]_<,
\qquad \nu_\ell=\ell+\frac12,
\tag{2.6}
\]

where

\[
[x]_<:=\#\{n\in\mathbb N:n<x\}
=\max\{0,\lceil x\rceil-1\}.
\tag{2.7}
\]

In particular, \([m]_< =m-1\) when \(m\in\mathbb N\). If several angular
channels share an eigenfrequency, all equal-threshold modes are excluded at
that wall and enter above it with the sum of their multiplicities.

The exact reconstruction statement is recorded in
[the separated-spectrum lemma](../state/lemma_packets/SHELL-sturm-liouville-completeness.md).
The accepted proof evidence consists of the
[incumbent proof](../rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md),
[independent reconstruction](../rounds/polya-main/round_004/reviews/sturm-liouville-clean-room.md),
and [adversarial audit](../rounds/polya-main/round_004/reviews/sturm-liouville-adversarial.md).

### Proposition 2.2 — phase-to-lattice reduction

Let \(K>0\). For \(a>0\), set

\[
G_a(z)=\frac1\pi
\left(\sqrt{a^2-z^2}-z\arccos\frac za\right),
\quad 0\le z\le a,
\tag{2.8}
\]

and \(G_a(z)=0\) for \(z>a\). Put \(\mu=\rho K\) and

\[
A_{\rho,K}(z)=G_K(z)-G_\mu(z).
\tag{2.9}
\]

For \(0\le z<\mu\), define

\[
H_\mu(z)=
\frac{3\mu^2+2z^2}{24\pi(\mu^2-z^2)^{3/2}},
\]

and define the auxiliary function—denoted \(F_\mu\) in the annulus
source, but written \(\mathcal F_\mu\) here to distinguish it from the
Bessel determinant—by

\[
\mathcal F_\mu(z)=
\begin{cases}
\max\{G_\mu(z)-H_\mu(z),-1/4\},&0\le z<\mu,\\
-1/4,&z\ge\mu.
\end{cases}
\]

Finally, \(\Phi_{K,\mu}(z)=G_K(z)-G_\mu(z)=A_{\rho,K}(z)\) on
\(0\le z\le\mu\).

The global phase enclosure gives, for \(0\le\nu\le K\),

\[
0<\gamma_{\rho,K}(\nu)
<G_K(\nu)-\mathcal F_\mu(\nu)
\le G_K(\nu)+\frac14,
\tag{2.10}
\]

and, when \(\nu\le\mu\), the sharper two-sided action enclosure

\[
\Phi_{K,\mu}(\nu)
<\gamma_{\rho,K}(\nu)
<\Phi_{K,\mu}(\nu)+\frac14.
\tag{2.11}
\]

Set

\[
s_\mu(\nu)=
\begin{cases}
\min\{H_\mu(\nu),1/4\},&0\le\nu<\mu,\\
1/4,&\mu\le\nu\le K,
\end{cases}
\qquad
P_{\rho,K}(\nu)=A_{\rho,K}(\nu)+s_\mu(\nu).
\]

Combining the two phase bounds gives

\[
\gamma_{\rho,K}(\nu)<P_{\rho,K}(\nu)
\le A_{\rho,K}(\nu)+\frac14.
\]

Thus the strict spectral count is bounded by the optimized proxy, and in
particular by the coarse proxy

\[
S_{\rho,K}
=\sum_{\nu_\ell<K}2\nu_\ell
\left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<.
\tag{2.12}
\]

The continuous target is exact:

\[
\int_0^\infty2zA_{\rho,K}(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{2.13}
\]

The problem is therefore to show that strict floor losses, phase slack, and
the half-integer multiplicity mesh do not exceed the margin in (2.13). The
exact reconstruction contracts are
[the phase lemma](../state/lemma_packets/SHELL-phase-enclosures.md) and
[the lattice lemma](../state/lemma_packets/SHELL-weighted-lattice-fractional.md).
Accepted proof evidence is supplied by the
[phase incumbent](../rounds/polya-main/round_002/responses/phase-enclosure-incumbent.md),
[phase clean-room proof](../rounds/polya-main/round_002/reviews/phase-enclosure-clean-room.md),
[phase adversarial review](../rounds/polya-main/round_002/reviews/phase-enclosure-adversarial.md),
[low-interface incumbent](../rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md),
[low-interface clean-room proof](../rounds/polya-main/round_003/reviews/low-interface-fixed-rho-clean-room.md),
and [low-interface adversarial review](../rounds/polya-main/round_003/reviews/low-interface-fixed-rho-adversarial.md).

For later use, write

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{2.14}
\]

## 3. The two ratio endpoints

Define

\[
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
\tag{3.1}
\]

### Lemma 3.1 — small-hole endpoint

For \(0<\rho\le\rho_*\) and \(K\ge0\),

\[
N_D(A_{\rho,1},K^2)\le W(\rho,K).
\tag{3.2}
\]

#### Proof

The multiplicity identity rewrites (2.12) as a sum of shifted tails, one
for each \(r\in\mathbb N_0\) and beginning at \(x_r=r+\tfrac12\). The
ordinary-floor tail majorant is legitimate because
\([x]_<\le\lfloor x\rfloor\) for every \(x\ge0\). Every tail beginning at or
above the inner interface \(\mu=\rho K\) is controlled by the convex
high-angular theorem.

The separately proved low-interface estimate controls a tail beginning
below \(\mu\) whenever

\[
0<\rho<\omega_0,
\qquad K(\omega_0-\rho)\ge C_*.
\tag{3.3}
\]

If \(\mu\le\tfrac12\), then every \(x_r\ge\tfrac12\ge\mu\), so only the
high-angular case occurs. If \(\mu>\tfrac12\) and
\(0<\rho\le\rho_*\), then

\[
K(\omega_0-\rho)
>\frac{\omega_0-\rho}{2\rho}
\ge\frac{\omega_0-\rho_*}{2\rho_*}=C_*.
\tag{3.4}
\]

Hence every tail is controlled. Summing the tail integrals gives (2.13),
which proves (3.2). The face \(\rho=\rho_*\) is included. At \(K=0\) both
sides vanish. \(\square\)

The exact statement and shifted-tail inequalities are in
[the small-hole packet](../state/lemma_packets/SHELL-rho-zero-endpoint.md).
The proof and its independent checks are the
[incumbent proof](../rounds/polya-main/round_007/responses/small-hole-incumbent.md),
[clean-room proof](../rounds/polya-main/round_007/reviews/small-hole-clean-room.md),
and [adversarial review](../rounds/polya-main/round_007/reviews/small-hole-adversarial.md).

### Lemma 3.2 — thin-shell endpoint

For \(7/8\le\rho<1\) and \(K\ge0\),

\[
N_D(A_{\rho,1},K^2)\le W(\rho,K).
\tag{3.5}
\]

#### Proof outline with exact closing margins

Put \(\varepsilon=1-\rho\in(0,1/8]\) and \(a=\varepsilon K\). The proof has
two inclusive pieces.

On \(0\le a\le\pi/(4\varepsilon)\), the radial form comparison has the
correct upper-count direction. Strict radial counting gives the number of
active one-dimensional radial levels as

\[
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\}.
\]

Define

\[
I(a)=\frac{2a^3}{3\pi},\qquad
S_0(a)=\sum_{n=1}^{N}(a^2-n^2\pi^2),\qquad
D(a)=I(a)-S_0(a).
\]

For \(a>\pi\), write \(a/\pi=N+t\), \(N\ge1\), \(0<t\le1\), using
\((N,t)=(m-1,1)\) at \(a=m\pi\). The exact product deficit satisfies

\[
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3},
\qquad D(a)>\frac25a^2.
\tag{3.6}
\]

The angular-ceiling and quarter-disk cost is at most

\[
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
\]

At \(\varepsilon=1/8\), the remaining reserve is

\[
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
\tag{3.7}
\]

On \(a\ge\pi/(4\varepsilon)\), let \(\mathcal A:[0,a]\to[0,T]\),
\(T=a/\pi\), be the exact decreasing shell action from the phase reduction,
let \(R_{\mathcal A}:[0,T]\to[0,a]\) be its decreasing inverse, and put
\(F_{\mathcal A}=R_{\mathcal A}^2\) and \(g=-F_{\mathcal A}'\). Splitting at the actual ungridded
curvature interface, shifted-sawtooth Stieltjes integration gives the radial
deficit

\[
D_{\rm rad}:=
\int_0^T F_{\mathcal A}(t)\,dt
-\sum_{\substack{n\ge1\\n-1/4<T}}F_{\mathcal A}(n-1/4)
\]

and the bound

\[
D_{\rm rad}
\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4},
\tag{3.8}
\]

whereas strict half-integer angular counting costs at most

\[
E=\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\tag{3.9}
\]

The relevant lower screen decreases and the upper screen increases on
\(0<\varepsilon\le1/8\). At the closed endpoint,

\[
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
\]

so

\[
D_{\rm rad}-E>\frac{143}{4096}a^2>0.
\tag{3.10}
\]

Both arguments include the common face \(a=\pi/(4\varepsilon)\), all radial
and angular integer walls, and the face \(\rho=7/8\). Together they cover
every \(a\ge0\) and prove (3.5). \(\square\)

The frozen exact statement is
[the thin-endpoint packet](../state/lemma_packets/SHELL-rho-one-endpoint-round16.md);
that packet is a contract, not the proof. The complete argument is in the
[incumbent proof](../rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md),
with an [independent reconstruction](../rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md)
and [adversarial audit](../rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md).

## 4. The compact-middle theorem

This section compresses the longest part of the proof into exact regional
lemmas. Each lemma has an analytic proof or a rigorously certified finite
part in the linked record.

Set

\[
\rho_0=\frac1{\sqrt{337}},
\qquad
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac\pi{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
\qquad
d=\frac{\sqrt{337}}2.
\tag{4.1}
\]

To make the upper-frequency wall explicit, set

\[
C_0=1+\frac{8\sqrt2}{15},\qquad
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
\eta_\rho=G_1\!\left(\max\left\{\rho,\frac12\right\}\right),
\]

\[
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
\qquad
H_0(\rho)=\frac{C_*}{\omega_0-\rho}\quad(\rho<\omega_0),
\]

and

\[
U(\rho)=\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right).
\]

Thus \(U\) is precisely the upper-frequency owner obtained from the
fixed-ratio, small-hole, and seam high-energy thresholds. On the final live
interval \(\rho_c\le\rho<39/50\), it is exactly \(K_0(\rho)\).

### Lemma 4.1 — primitive compact envelope

The zero-count, small-hole, fixed-ratio high-energy, and thin-shell estimates
cover every compact-middle point except the exact nonrectangular set

\[
\mathcal D_{16}
=\left\{\rho_*<\rho<\frac78:
L(\rho)<K<U(\rho)\right\},
\tag{4.2}
\]

where

\[
L(\rho)=\max\left\{\frac1{2\rho},\frac\pi{1-\rho}\right\}.
\]

In particular the accepted analytic envelope already gives the global
high-frequency theorem

\[
0<\rho<1,\qquad K\ge295^2
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)\le W(\rho,K).
\tag{4.3}
\]

The precursor estimates are collected in
[the compact envelope](../state/lemma_packets/SHELL-rho-compact.md), and the
exact formula (4.2), including its open faces and the definition of \(U\),
is proved in the
[Round 17 compact record](../state/lemma_packets/SHELL-rho-compact-round17.md).

### Lemma 4.2 — finite angular and radial staircase

The strict inequality \(N_D(A_{\rho,1},K^2)<W(\rho,K)\) holds on each of
the following regions:

1. \(\rho_c\le\rho\le7/8\) and
   \(z_\rho\le K\le k_2(\rho)\);
2. \(\rho_c\le\rho\le7/8\) and
   \(k_2(\rho)<K\le k_5(\rho)\);
3. \(\rho_0<\rho<\rho_c\) and
   \(1/(2\rho)<K\le d\);
4. \(\rho_c\le\rho\le7/8\) and
   \(k_5(\rho)<K\le k_6(\rho)\).

They follow from the one-dimensional lower bound

\[
q_{\ell,n}^2\ge n^2z_\rho^2+\ell(\ell+1),
\tag{4.4}
\]

where \(q_{\ell,n}\) is the \(n\)-th positive radial eigenfrequency in
angular channel \(\ell\), together with
fixed-channel shell-to-ball min--max comparison, exact Bessel-zero
inequalities, exhaustive multiplicity inventories, and strict Weyl payments
at every fixed or moving entry wall. The corresponding residual is

\[
\begin{aligned}
\mathcal D_{19}={}&
\left\{\rho_*<\rho\le\rho_0,
\frac1{2\rho}<K<U(\rho)\right\}\\
&\cup\left\{\rho_0<\rho<\rho_c,
d<K<U(\rho)\right\}\\
&\cup\left\{\rho_c\le\rho<\frac78,
k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}
\tag{4.5}
\]

At \(\rho=\rho_0\), the candidate lower fiber is empty because
\(1/(2\rho_0)=d\). All frequency inequalities in (4.5) are strict.

The proof-free
[first-band packet](../state/lemma_packets/SHELL-first-angular-bands-round17-claim.md),
[delayed-staircase packet](../state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md),
and [two-sided staircase packet](../state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md)
fix the exact statements; they are not proofs. The complete evidence is:

- Round 17:
  [incumbent proof](../rounds/polya-main/round_017/responses/analytic-compression-incumbent.md),
  [clean-room proof](../rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md),
  and [adversarial review](../rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md);
- Round 18:
  [incumbent proof](../rounds/polya-main/round_018/responses/angular-staircase-incumbent.md),
  [clean-room proof](../rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md),
  [constant audit](../rounds/polya-main/round_018/reviews/angular-staircase-constants.md),
  [cross-comparison](../rounds/polya-main/round_018/reviews/angular-staircase-cross-comparison.md),
  and [adversarial review](../rounds/polya-main/round_018/reviews/angular-staircase-adversarial-referee.md);
- Round 19:
  the [high-ratio incumbent](../rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md),
  [lower-ratio incumbent](../rounds/polya-main/round_019/exploration/lower-ratio-route.md),
  [clean-room proof](../rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md),
  [constant audit](../rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md),
  and [adversarial review](../rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md).

### Lemma 4.3 — combined lower, high-staircase, and optical closure

The inequality is strict on both lower components of (4.5) and on

\[
\rho_c\le\rho\le\frac78,
\qquad z_\rho\le K\le k_{11}(\rho),
\tag{4.6}
\]

It also holds for every frequency on

\[
\frac{39}{50}\le\rho<1,
\qquad K\ge0,
\tag{4.7}
\]

and is strict there when \(K>0\). Exact subtraction leaves

\[
\boxed{
\mathcal D_{20}
=\left\{\rho_c\le\rho<\frac{39}{50},
\quad k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.}
\tag{4.8}
\]

The face \(\rho=39/50\) belongs to (4.7), \(K=k_{11}(\rho)\) belongs to
(4.6), and \(K=U(\rho)\) belongs to the inherited high-frequency theorem.

The exact statement is fixed by the proof-free
[Round 20 claim](../state/lemma_packets/SHELL-combined-closure-round20-claim.md).
The [high-route](../rounds/polya-main/round_020/exploration/high-global-route.md)
and [lower-route](../rounds/polya-main/round_020/exploration/lower-remaining-gap.md)
notes are exploratory precursors, not promoted evidence. The complete
accepted evidence, including the conservative cap-\(74\) cell, is the
[clean-room reconstruction](../rounds/polya-main/round_020/reviews/combined-closure-clean-room.md),
[mandatory cap-\(74\) addendum](../rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md),
[cross-comparison](../rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md),
and [adversarial referee report](../rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md).

### Lemma 4.4 — exact closure of the final residual

Two final estimates hold:

\[
\frac7{51}\le\rho\le\frac{39}{50},
\quad 12\le K\le200
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K),
\tag{4.9}
\]

and

\[
\rho_c\le\rho\le\frac{39}{50},
\quad K\ge200
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K).
\tag{4.10}
\]

The exact guards are

\[
\frac7{51}<\rho_c,
\qquad
k_{11}(\rho)>12
\quad(\rho_c\le\rho<1).
\tag{4.11}
\]

The restriction \(\rho<1\) in the second guard is essential.

Define

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\tag{4.12}
\]

Every point of \(\mathcal C_{21}\) lies in the rectangle (4.9), and every
point of \(\mathcal T_{21}\) lies in (4.10). The sets are disjoint and
exhaust \(\mathcal D_{20}\), with \(K=200\) assigned only to the compact
subtraction owner. Defining the successor residual by

\[
\mathcal D_{21}
:=\mathcal D_{20}\setminus(\mathcal C_{21}\cup\mathcal T_{21}),
\]

we therefore have

\[
\boxed{\mathcal D_{21}=\varnothing.}
\tag{4.13}
\]

The exact scoped statement is in the
[Round 21 closure packet](../state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md),
which is not by itself a proof. Accepted evidence consists of the
[incumbent closure proof](../rounds/polya-main/round_021/exploration/exact-d20-closure.md),
[clean-room proof](../rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md),
[domain addendum](../rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-domain-addendum.md),
[source-executed certificate review](../rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-source-exec-replacement.md),
and [fresh adversarial review](../rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-source-exec.md).

### Certificate boundary for Lemma 4.4

The finite part of (4.9) is an outward-rounded Arb ball-arithmetic partition
into 10,580 exact rational leaves. It certifies strict proxy inequalities, interfaces,
integer walls, corners, and exact coverage only on

\[
[7/51,39/50]\times[12,200].
\]

It does not certify Bessel roots; the spectral transfer is Proposition 2.2.

For (4.10), 1,286 outward-rounded Arb boxes certify only the base predicates
at \(K=200\). Let \(\mathcal B\) be the aggregate reserve and \(F\) its
one-variable curvature lower screen, with the exact definitions (A13)--(A22)
in the linked aggregate-tail contract. On
\(7/51\le\rho\le39/50\), the boxes prove precisely

\[
\mathcal B(\rho,200)>0,
\qquad
\mathcal B_K(\rho,200)>0,
\qquad
F(\rho)>0,
\]

together with the stated domain guards. The universal conclusion for
\(K>200\) is analytic: on the same ratio interval and for every \(K\ge200\),

\[
\mathcal B_{KK}(\rho,K)>F(\rho)>0,
\]

and hence

\[
\mathcal B_K(\rho,K)
=\mathcal B_K(\rho,200)
+\int_{200}^{K}\mathcal B_{KK}(\rho,s)\,ds>0,
\]

\[
\mathcal B(\rho,K)
=\mathcal B(\rho,200)
+\int_{200}^{K}\mathcal B_K(\rho,s)\,ds>0.
\tag{4.14}
\]

The two positive base premises displayed above are what make these
integrations strict; positivity of \(\mathcal B_{KK}\) alone would not
suffice. Thus no finite-box decision is extrapolated beyond its certified domain.
The exact contracts are
[the compact certificate contract](../state/certificate_contracts/ROUND21-compact-proxy-contract.md)
and [the aggregate-tail contract](../state/certificate_contracts/ROUND21-aggregate-tail-contract.md).

### Proposition 4.5 — compact-middle theorem

For every \(\rho_*<\rho<7/8\) and \(K\ge0\),

\[
N_D(A_{\rho,1},K^2)\le W(\rho,K).
\tag{4.15}
\]

#### Proof

The primitive cover of Lemma 4.1, the successive closed staircase regions
of Lemma 4.2, and the three regions of Lemma 4.3 leave exactly
\(\mathcal D_{20}\). Lemma 4.4 partitions and closes that entire final
residual. Equation (4.13) says that no uncovered point remains. All shared
faces have a unique declared subtraction owner, while overlapping theorem
domains merely give redundant proofs. This proves (4.15). \(\square\)

## 5. Proof of the spectral theorem

We now assemble the regional results without importing any new estimate.

First, elementary bounds give

\[
3\sqrt3>5>\pi,
\]

and hence \(\omega_0>0\). Also \(\sqrt3<2\) and \(\pi>3\) give
\(\omega_0<1/6\). Since \(C_*>0\),

\[
0<\rho_*<\omega_0<\frac16<\frac78.
\tag{5.1}
\]

Therefore

\[
(0,1)
=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}
[7/8,1).
\tag{5.2}
\]

Fix \(0<\rho<1\). At \(K=0\), positivity in Proposition 2.1 gives

\[
N_D(A_{\rho,1},0)=0=W(\rho,0).
\tag{5.3}
\]

Let \(K>0\). If \(0<\rho\le\rho_*\), apply Lemma 3.1. If
\(\rho_*<\rho<7/8\), apply Proposition 4.5. If \(7/8\le\rho<1\), apply
Lemma 3.2. The three cases in (5.2) are disjoint and exhaustive, so

\[
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge0).
\tag{5.4}
\]

Now

\[
\omega_3=\frac{4\pi}{3},
\qquad
L_3=\frac{\omega_3}{(2\pi)^3}=\frac1{6\pi^2},
\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\]

so

\[
L_3|A_{\rho,1}|
=\frac{2}{9\pi}(1-\rho^3).
\tag{5.5}
\]

Taking \(K=\sqrt\Lambda\) in (5.4) proves the unit-shell form of Theorem
1.1 for every \(\Lambda\ge0\).

For arbitrary \(0<r<R\), put \(\rho=r/R\). The unitary dilation

\[
(D_Ru)(x)=R^{-3/2}u(x/R)
\]

maps \(L^2(A_{\rho,1})\) onto \(L^2(A_{r,R})\), and its Dirichlet form
scales by \(R^{-2}\). Hence

\[
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}),
\]

and the strict threshold transforms as

\[
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda).
\tag{5.6}
\]

Applying the unit-shell result at \(R^2\Lambda\),

\[
\begin{aligned}
N_D(A_{r,R},\Lambda)
&\le\frac{2}{9\pi}(1-\rho^3)(R^2\Lambda)^{3/2}\\
&=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}\\
&=L_3|A_{r,R}|\Lambda^{3/2}.
\end{aligned}
\]

This proves Theorem 1.1 for every \(R>0\), including \(R<1\). \(\square\)

## 6. Proof that spherical shells do not tile

We prove Theorem 1.2 independently of the spectral argument.

Set \(\alpha=r/R\in(0,1)\) and scale by \(1/R\). It suffices to consider

\[
T=A_{\alpha,1}=\{x:\alpha<|x|<1\}.
\]

Every rigid motion has the form \(x\mapsto Qx+a\), with \(Q\) orthogonal.
Because \(T\) is radial, \(Q(T)=T\), so every congruent copy is a translate

\[
T_a=a+T=\{x:\alpha<|x-a|<1\}.
\]

Assume for contradiction that \(\{T_a:a\in A\}\) has pairwise-disjoint
interiors and covers almost everywhere. Duplicate centers are impossible,
because they give the same nonempty open tile.

Fix a unit vector \(e\) and put

\[
c=\frac{1+\alpha}{2}e,
\qquad
\delta=\frac{1-\alpha}{2}.
\]

Then \(B(c,\delta)\subset T\). Therefore \(T_a\) contains
\(B(a+c,\delta)\), and disjointness implies

\[
|a-b|\ge1-\alpha
\qquad(a\ne b).
\tag{6.1}
\]

Thus the centers are locally finite: a bounded set cannot contain infinitely
many points with fixed positive separation. They are also countable, since

\[
A=\bigcup_{m\ge1}(A\cap\overline B(0,m))
\]

is a countable union of finite sets.

Each tile boundary is a union of two spheres and is three-dimensional null.
The countable union

\[
B=\bigcup_{a\in A}\partial T_a
\]

is therefore null. Exact open-shell coverage is already a special case of
almost-everywhere coverage. If closed shells cover exactly or almost
everywhere, removing \(B\) shows that their open interiors still cover
almost everywhere. Hence it is enough to assume

\[
\left|\mathbb R^3\setminus\bigcup_{a\in A}T_a\right|=0.
\tag{6.2}
\]

Choose one tile \(T_{a_0}\) and its outer sphere

\[
\Sigma=\{x:|x-a_0|=1\}.
\]

Fix \(p\in\Sigma\) and put \(u=p-a_0\). For \(n\ge1\), let

\[
U_n=B\left(p+\frac2n u,\frac1n\right).
\]

Every \(U_n\) lies outside \(T_{a_0}\), is open, and has positive volume.
By (6.2), choose \(x_n\in U_n\cap T_{a_n}\) with \(a_n\ne a_0\). Since
\(x_n\to p\) and \(|x_n-a_n|<1\), the centers \(a_n\) eventually lie in a
fixed bounded set. Local finiteness lets us pass to a subsequence with one
fixed center \(a\ne a_0\). Thus \(p\in\overline{T_a}\).

The point \(p\) is not in \(T_a\). Otherwise some \(B(p,\varepsilon)\) lies
in \(T_a\). Choose

\[
0<t<\min\{\varepsilon,1-\alpha\}.
\]

Then \(p-tu\in T_{a_0}\cap T_a\), contradicting disjoint interiors.
Therefore every \(p\in\Sigma\) belongs to the boundary of a neighboring
tile.

If \(p\in\Sigma\cap\partial T_a\), then \(|p-a|\in\{\alpha,1\}\), hence
\(|a-a_0|\le2\). Only finitely many centers satisfy this bound. Consequently
\(\Sigma\) is covered by finitely many neighboring inner or outer boundary
spheres.

Translate so that \(a_0=0\). The intersection of \(\Sigma\) with a
neighboring sphere \(\{x:|x-a|=s\}\), \(s\in\{\alpha,1\}\), satisfies

\[
|x|^2=1,
\qquad |x-a|^2=s^2,
\]

and hence

\[
2a\cdot x=|a|^2+1-s^2.
\tag{6.3}
\]

Because \(a\ne0\), (6.3) is a genuine plane. Its intersection with
\(\Sigma\) is empty, a tangent point, or a circle, and therefore has zero
surface measure on \(\Sigma\). A finite union of such sets cannot cover
\(\Sigma\), whose area is \(4\pi\).

There is no coincident-sphere exception. A neighboring outer sphere equals
\(\Sigma\) only when it has the same center, which is the original tile or a
forbidden duplicate. A neighboring inner sphere cannot equal \(\Sigma\)
because \(\alpha<1\). We have reached a contradiction. Scaling back proves
Theorem 1.2. \(\square\)

## 7. Logical dependency and evidence boundary

The proof has four logically distinct layers:

1. **Exact analysis:** operator decomposition, phase representation,
   strict counting, weighted-lattice identities, endpoint estimates, and
   analytic propagation.
2. **Finite mode analysis:** explicit radial/angular inventories and exact
   Weyl payments through \(k_{11}\).
3. **Certified finite computation:** only the rectangle and \(K=200\) base
   predicates stated after Lemma 4.4.
4. **Elementary geometry:** the non-tiling proof, which uses none of the
   spectral work.

The legacy numerical Bessel experiments are not proof inputs. External
Lorch inequalities are used only for explicitly stated first-positive-zero
bounds; the shell variational comparison, radial-index preservation,
multiplicity counts, and Weyl payments are internal arguments. The audited
environment reconstructed the exact specializations from the published
statement but did not have access to the article's full proof, so a
submission must either cite that theorem conventionally or replace those
bounds by self-contained proofs. The source cards are
[Lorch bounds](../sources/lorch_bessel_zeros.md),
[Round 19 zero bounds](../sources/round19_bessel_zero_bounds.md), and
[Round 20 zero bounds](../sources/round20_bessel_zero_bounds.md).

The final graph and validation records are
[the proof-obligation graph](../state/proof_obligations.yml),
[the validation report](../state/last_validation_report.md), and
[the independent final audit](../rounds/polya-main/round_022/reviews/derived-state-final-audit.md).

## 8. Work required before external submission

This draft is mathematically complete only relative to the linked detailed
lemmas and certified supplements. Before external submission it should be
expanded as follows:

1. move the full proofs of Propositions 2.1 and 2.2 into analytic appendices;
2. replace internal packet language in Lemmas 3.1–4.4 with conventional
   numbered propositions and complete proofs;
3. print the Round 17–20 mode inventories, zero exclusions, fixed/moving
   payments, and the corrected cap-\(74\) argument;
4. provide a computer-assisted-proof supplement containing the exact
   algorithms, rational partitions, environment, hashes, digest, and replay
   instructions;
5. give conventional bibliographic citations for the FLPS, annulus, DLMF,
   and Lorch inputs, respecting their exact statement-level scopes;
6. run an independent human line-by-line reconstruction; and
7. perform a current literature comparison before using any novelty or
   priority language.

These tasks concern exposition, external verification, and scholarly scope.
They do not broaden Theorem 1.1 to general domains.
