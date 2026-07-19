# Clean-room review: multiplicity-weighted shell lattice bound

## Scope and independence

This review was reconstructed independently. Before being asked to write it, I read only

- `problems/polya_conjecture.md`,
- `sources/annuli_polya.md`,
- `sources/bessel_phase_enclosures.md`, and
- `state/proof_obligations.yml`.

For the formal integration pass I was additionally authorized to read

- `state/lemma_packets/SHELL-weighted-lattice-fractional.md`, and
- `sources/flps_balls.md`.

I did **not** read `rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md`, any other Round 3 response or review, `state/best_proof_draft.md`, `state/next_round_prompts.md`, or any incumbent artifact. The only workspace edit made in this pass is this review file; no state file was edited.

## Verdict

The exact weighted proxy and both proposed dimension reductions are correct. The FLPS ball convex theorem rigorously controls every shifted tail beginning at or above the inner interface. The Nicholson argument also proves the exact thin-width phase-level zero statement

$$
(1-\rho)K\le \pi \quad\Longrightarrow\quad [\gamma_{\rho,K}(\nu_\ell)]_<=0
\quad\text{for every }\ell.
$$

The full weighted lattice obligation is nevertheless still open. The first unsupported implication is exactly the shifted-tail inequality for a start below the interface,

$$
r+\frac12<\mu=\rho K.
$$

Such a tail crosses a strictly concave part of the shell action before entering its convex ball part, so FLPS Theorem 5.1 does not apply. Subtracting two ball inequalities or merely splitting at the generally nonintegral interface does not supply the missing floor margin.

## 1. Exact target and strict phase proxy

Put

$$
\mu=\rho K,\qquad \nu_\ell=\ell+\frac12,
\qquad A(\nu)=G_K(\nu)-G_\mu(\nu),
$$

with every $G_a$ extended by zero for $\nu>a$. For $x>0$, retain the strict integer-level operator

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}
=\max\{0,\lceil x\rceil-1\}.
$$

For $0\le \nu<\mu$, the two audited bounds give

$$
\gamma<G_K-\mathcal F_\mu
=A+\min\{H_\mu,G_\mu+\tfrac14\},
\qquad
\gamma<A+\frac14.
$$

Since $G_\mu+1/4\ge1/4$, their minimum is

$$
\gamma<A+\min\{H_\mu,\tfrac14\}.
$$

For $\mu\le\nu\le K$, one has $G_\mu=0$ and the global bound is

$$
\gamma<G_K+\frac14=A+\frac14.
$$

Thus the optimized slack in the lemma packet is correct:

$$
s_\mu(\nu)=
\begin{cases}
\min\{H_\mu(\nu),1/4\},&0\le\nu<\mu,\\
1/4,&\mu\le\nu\le K.
\end{cases}
$$

At $\nu=\mu$ the second line must be used; $H_\mu(\mu)$ is not defined. Monotonicity of $[\,\cdot\,]_<$ and the strict phase inequality give

$$
[\gamma_{\rho,K}(\nu_\ell)]_<
\le [A(\nu_\ell)+s_\mu(\nu_\ell)]_<.
$$

The active cutoff $\nu_\ell<K$ and

$$
m_K=\max\{0,\lceil K-\tfrac12\rceil\}
$$

are correct, including $K\in\tfrac12+\mathbb Z$. Consequently the exact analytic target is

$$
\sum_{\nu_\ell<K}2\nu_\ell
[A(\nu_\ell)+s_\mu(\nu_\ell)]_<
\le \frac{2}{9\pi}(K^3-\mu^3).
$$

The coarse target with $s_\mu$ replaced by $1/4$ is sufficient because the optimized proxy is pointwise no larger.

This is a proxy-to-spectrum conclusion only under the currently conditional shell completeness/count identity. The lattice statements themselves do not discharge that separate dependency.

## 2. Exact volume and the raw quarter-slack obstruction

Direct integration gives

$$
\int_0^\infty2\nu G_a(\nu)\,d\nu=\frac{2a^3}{9\pi},
$$

and hence

$$
\int_0^K2\nu A(\nu)\,d\nu
=\frac{2}{9\pi}(K^3-\mu^3)
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The error identity in the lemma packet is exact. If

$$
E_0(a)=\sum_{\nu_\ell<a}2\nu_\ell G_a(\nu_\ell)
-\frac{2a^3}{9\pi},
$$

then for the optimized proxy

$$
\mathcal P_\rho(K)-\frac{2}{9\pi}(K^3-\mu^3)
=E_{\rm mp}+E_{\rm ph}-E_{\rm frac}.
$$

Therefore the exact first margin in a direct midpoint argument is

$$
\boxed{E_{\rm frac}\ge E_{\rm mp}+E_{\rm ph}.}
$$

The blanket quarter cost is exactly

$$
\frac14\sum_{\ell=0}^{m_K-1}(2\ell+1)=\frac{m_K^2}{4};
$$

it cannot simply be absorbed into the Weyl integral uniformly. A concrete exact illustration is $K=1$, $\mu=1/4$. There is one active order, $\nu=1/2$, and

$$
A(1/2)+\frac14
=\frac{\sqrt3}{2\pi}+\frac1{12}<1.
$$

The strict proxy is therefore zero, while the corresponding floor-free sampled bound is the displayed positive number, which is already larger than the Weyl target

$$
\frac{2}{9\pi}\left(1-\frac1{64}\right)=\frac7{32\pi}.
$$

Thus the floor-free phase sum fails even in this elementary case; the strict fractional saving is essential. In the fixed optical-width scaling $a=(1-\rho)K$, the packet's ratio

$$
\frac{m_K^2/4}{\frac{2}{9\pi}(1-\rho^3)K^3}
\longrightarrow \frac{3\pi}{8a}
$$

is also correct and shows why the quarter term is not a uniform perturbative error.

## 3. Exact square (level-set) reduction

The coarse proxy admits another exact formulation that preserves all strict walls. Set

$$
T=A(0)=\frac{K-\mu}{\pi}.
$$

The function $A$ is continuous and strictly decreasing on $(0,K)$, with $A(K)=0$. Let $R(t)$ be its inverse cutoff for $0\le t<T$, so

$$
A(R(t))=t.
$$

Define the strict half-integer channel count

$$
M(x):=\#\{\ell\ge0:\ell+\tfrac12<x\}
=\max\{0,\lceil x-\tfrac12\rceil\}.
$$

For $t_n=n-1/4$,

$$
n<A(\nu_\ell)+\frac14
\quad\Longleftrightarrow\quad
\nu_\ell<R(t_n).
$$

The strict inequality remains correct when a sampled phase lies exactly on an integer wall. Since the first $M$ odd integers sum to $M^2$, exchanging the angular and radial sums gives the exact identity

$$
\boxed{
\sum_{\nu_\ell<K}2\nu_\ell[A(\nu_\ell)+\tfrac14]_<
=\sum_{\substack{n\ge1\\n-1/4<T}}M(R(n-1/4))^2.
}
$$

Layer cake gives the exact continuous counterpart

$$
\boxed{
\frac{2}{9\pi}(K^3-\mu^3)
=\int_0^T R(t)^2\,dt.
}
$$

Thus the coarse weighted problem is equivalently the staircase quadrature inequality

$$
\sum_{n-1/4<T}M(R(n-1/4))^2
\le\int_0^T R(t)^2\,dt.
$$

No audited source currently proves this mixed-curvature square inequality. It is a clean alternative statement of the same missing weighted margin, not a completed proof.

## 4. Exact shifted-tail reduction

For any finitely supported nonnegative integer sequence $(q_\ell)$,

$$
\sum_{\ell\ge0}(2\ell+1)q_\ell
=\sum_{r\ge0}\left(q_r+2\sum_{\ell>r}q_\ell\right).
$$

Indeed, $q_\ell$ occurs once as the initial term at $r=\ell$ and $\ell$ times with coefficient two for $0\le r<\ell$.

For

$$
q_\ell=[A(\nu_\ell)+1/4]_<,
$$

one has $q_\ell\le\lfloor A(\nu_\ell)+1/4\rfloor$, including at integer walls. Hence the ordinary-floor tail

$$
\mathcal T_r=
\left\lfloor A(r+\tfrac12)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A(r+j+\tfrac12)+\frac14\right\rfloor
$$

is a valid majorant of the corresponding strict tail.

If

$$
\mathcal T_r\le2\int_{r+1/2}^{K}A(z)\,dz
$$

holds for every $r$, summing gives

$$
\sum_{\nu_\ell<K}2\nu_\ell q_\ell
\le2\int_0^K f_3(z)A(z)\,dz,
$$

where

$$
f_3(z)=\#\{r\ge0:r+\tfrac12\le z\}.
$$

Its primitive $F_3(z)=\int_0^z f_3(t)\,dt$ obeys $F_3(z)\le z^2/2$. Since $A$ is decreasing and $A(K)=0$, integration by parts yields

$$
2\int_0^K f_3A
=-2\int_0^K F_3A'
\le-\int_0^Kz^2A'
=\int_0^K2zA(z)\,dz.
$$

This confirms that the proposed shifted-tail sublemma is sufficient for the exact Weyl target.

## 5. High tails are rigorously controlled

Let

$$
x_0=r+\frac12\ge\mu.
$$

For every $z\ge x_0$, $G_\mu(z)=0$, so $A(z)=G_K(z)$. Apply FLPS Theorem 5.1 to

$$
g(t)=G_K(x_0+t),\qquad 0\le t\le b:=K-x_0.
$$

The hypotheses hold:

$$
g'(t)=-\frac1\pi\arccos\frac{x_0+t}{K}\in[-1/2,0],
$$

$$
g''(t)=\frac1{\pi\sqrt{K^2-(x_0+t)^2}}>0,
$$

and $g$ is nonnegative with $g(b)=0$. The theorem gives exactly

$$
\mathcal T_r\le2\int_{x_0}^{K}G_K(z)\,dz
=2\int_{x_0}^{K}A(z)\,dz.
$$

There is no endpoint-integrality gap: FLPS Theorem 5.1 is explicitly translation-compatible and uses $\lfloor b\rfloor$; if $b$ itself is an integer, the endpoint term is $\lfloor1/4\rfloor=0$.

Therefore every shifted tail with $r+1/2\ge\mu$ is proved.

## 6. The first missing implication: low mixed-curvature tails

For $0<z<\mu$,

$$
A''(z)
=\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}<0.
$$

For $\mu<z<K$,

$$
A''(z)=\frac1{\pi\sqrt{K^2-z^2}}>0.
$$

Thus a tail beginning at $x_0=r+1/2<\mu$ is concave on $[x_0,\mu)$ and convex on $(\mu,K)$. It fails the global convexity hypothesis of FLPS Theorem 5.1.

Two tempting shortcuts are invalid:

1. One cannot subtract the two proved ball floor inequalities. The floor operation is nonlinear, and two upper bounds give no lower control on the term being subtracted.
2. Splitting at $\mu$ does not by itself prove the tail estimate. The interface is generally not a grid point, the concave head does not vanish at the interface, and the endpoint/fractional margins from separately estimated pieces have not been shown to cancel.

Consequently the first missing implication is precisely

$$
\boxed{
\mathcal T_r
\le2\int_{r+1/2}^{K}A(z)\,dz
\quad\text{for every integer }r\ge0
\text{ with }r+\tfrac12<\mu.
}
$$

Proving these low tails would complete the coarse weighted lattice inequality through the verified dimension reduction. Failure of the coarse low-tail statement would not by itself falsify the optimized target, because $s_\mu(\nu)\le1/4$.

## 7. Thin-width zero lemma

For every half-integer $\nu\ge1/2$, Nicholson's formula gives

$$
M_\nu(x)^2
=\frac8{\pi^2}\int_0^\infty
\cosh(2\nu t)K_0(2x\sinh t)\,dt.
$$

Since $K_0>0$ and $\cosh(2\nu t)\ge\cosh t$,

$$
M_\nu(x)^2\ge M_{1/2}(x)^2.
$$

The elementary half-order formulas give

$$
M_{1/2}(x)^2=J_{1/2}(x)^2+Y_{1/2}(x)^2
=\frac2{\pi x}.
$$

Therefore

$$
0<\theta_\nu'(x)
=\frac2{\pi xM_\nu(x)^2}\le1.
$$

Integrating on $[\rho K,K]$ proves

$$
\Psi_{\nu,\rho}(K)
=\int_{\rho K}^{K}\theta_\nu'(x)\,dx
\le(1-\rho)K.
$$

If $(1-\rho)K\le\pi$, then the normalized phase satisfies $\gamma\le1$, so

$$
[\gamma]_< =\#\{n\in\mathbb N:n<\gamma\}=0.
$$

The equality case is handled correctly: for $\nu=1/2$, $\theta'_{1/2}=1$ and a width exactly $\pi$ gives $\gamma=1$, which strict counting excludes. For $\nu>1/2$, Nicholson's comparison is strict and hence $\gamma<1$ at the same width.

Thus the thin-width phase-count lemma is proved exactly. Its promotion as a statement about the full shell spectrum retains the separate spectral-completeness dependency already recorded in the proof graph.

## Promotion assessment

- **Validated:** exact Weyl target; optimized phase slack; strict endpoint conventions; active half-integer cutoff; error-budget identity; square reduction; multiplicity-to-tail identity; step-function primitive comparison; all high tails $r+1/2\ge\mu$; thin-width zero lemma.
- **Not validated:** the low shifted-tail inequality for $r+1/2<\mu$, equivalently a complete proof of the mixed-curvature square quadrature.
- **Status recommendation:** keep `SHELL-weighted-lattice-fractional` open. The algebraic dimension reduction, high-tail sublemma, and thin-width phase-level zero lemma may be promoted separately, subject to the repository's ordinary review gates.
