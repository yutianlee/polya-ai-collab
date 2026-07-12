# Lemma Packet: Multiplicity-Weighted Shell Lattice Bound

Obligation: `SHELL-weighted-lattice-fractional`

## Parameters and notation

Fix

$$
0<\rho<1,\qquad K>0,\qquad \mu=\rho K,
\qquad \nu_\ell=\ell+\frac12.
$$

Write $\mathcal F_\mu$ for the audited FLPS auxiliary function called $F_\mu$ in `sources/annuli_polya.md`; this avoids confusion with the repository's Bessel cross-product determinant.

For $x>0$, define the strict positive-integer count and strict remainder by

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}
=\max\{0,\lceil x\rceil-1\},
$$

$$
\langle x\rangle_<:=x-[x]_<\in(0,1].
$$

Thus $\langle m\rangle_<=1$ at every positive integer $m$.

Extend $G_a(\nu)$ by zero for $\nu>a$ and set

$$
A_{\rho,K}(\nu):=G_K(\nu)-G_\mu(\nu).
$$

Define the optimized transferred slack

$$
s_\mu(\nu)=
\begin{cases}
\min\{H_\mu(\nu),\tfrac14\},&0\le\nu<\mu,\\
\tfrac14,&\mu\le\nu\le K,
\end{cases}
$$

and

$$
U_{\rho,K}(\nu):=A_{\rho,K}(\nu)+s_\mu(\nu).
$$

At $\nu=\mu$, use $s_\mu(\mu)=1/4$; never evaluate the divergent expression $H_\mu(\mu)$.

## Exact target

For each fixed $0<\rho<1$, exhibit an explicit $K_0(\rho)$ and prove, for all $K\ge K_0(\rho)$,

$$
\boxed{
\sum_{\nu_\ell<K}
2\nu_\ell[U_{\rho,K}(\nu_\ell)]_<
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The finite range $0<K<K_0(\rho)$ belongs to `COMP-certified-bessel`; this lemma must not silently absorb it.

A stronger and cleaner target may be attempted first:

$$
\boxed{
\sum_{\nu_\ell<K}
2\nu_\ell[A_{\rho,K}(\nu_\ell)+\tfrac14]_<
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The optimized proxy is no larger than this coarse proxy. Failure of the coarse inequality would therefore not falsify the optimized target.

## Spectral bridge and strict cutoff

The proved phase enclosure gives

$$
\gamma_{\rho,K}(\nu):=\frac{\Psi_{\nu,\rho}(K)}{\pi}
<U_{\rho,K}(\nu),
\qquad 0\le\nu\le K.
$$

For $0\le\nu<\mu$, this follows by taking the better of

$$
\gamma<G_K-\mathcal F_\mu
=A+(G_\mu-\mathcal F_\mu)
$$

and $\gamma<A+1/4$, since

$$
G_\mu-\mathcal F_\mu
=\min\{H_\mu,G_\mu+\tfrac14\}.
$$

For $\mu\le\nu\le K$, it is the global bound $\gamma<G_K+1/4$.

Assuming the still-conditional spectral completeness/count identity,

$$
N_D(A_{\rho,1},K^2)
=\sum_{\ell\ge0}2\nu_\ell[\gamma_{\rho,K}(\nu_\ell)]_<.
$$

No radial root contributes when $K\le\nu$. Hence the sharp active cutoff is $\nu_\ell<K$, and the number of active channels is

$$
m_K=\max\{0,\lceil K-\tfrac12\rceil\}.
$$

At a shell eigenfrequency, $[\gamma]_<$ is one less than the ordinary floor. Do not replace the displayed strict count by an equality with $\lfloor\gamma\rfloor$.

## Exact Weyl integral and error budget

For $a>0$,

$$
\int_0^\infty2\nu G_a(\nu)\,d\nu=\frac{2a^3}{9\pi}.
$$

Therefore

$$
\boxed{
\int_0^\infty2\nu A_{\rho,K}(\nu)\,d\nu
=\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Define

$$
E_0(a)=\sum_{\nu_\ell<a}2\nu_\ell G_a(\nu_\ell)-\frac{2a^3}{9\pi},
$$

$$
E_{\rm mp}(\rho,K)=E_0(K)-E_0(\mu),
$$

and let $r_\mu=\max\{0,\lceil\mu-1/2\rceil\}$. The optimized phase-slack contribution is

$$
E_{\rm ph}
=\sum_{\ell=0}^{r_\mu-1}(2\ell+1)
\min\{H_\mu(\nu_\ell),\tfrac14\}
+\frac{m_K^2-r_\mu^2}{4}.
$$

In particular, the blanket quarter-slack cost is exactly

$$
E_{1/4}=\frac14\sum_{\ell=0}^{m_K-1}(2\ell+1)=\frac{m_K^2}{4}.
$$

For the optimized integer proxy $\mathcal P_\rho(K)$, define

$$
E_{\rm frac}
=\sum_{\nu_\ell<K}2\nu_\ell
\langle U_{\rho,K}(\nu_\ell)\rangle_<.
$$

Then the exact bookkeeping identity is

$$
\boxed{
\mathcal P_\rho(K)-\frac{2}{9\pi}(1-\rho^3)K^3
=E_{\rm mp}+E_{\rm ph}-E_{\rm frac}.
}
$$

Thus it is insufficient to call $m_K^2/4$ lower order. The required inequality is

$$
E_{\rm frac}\ge E_{\rm mp}+E_{\rm ph}.
$$

For fixed optical width $a=(1-\rho)K$,

$$
\frac{m_K^2/4}{\frac{2}{9\pi}(1-\rho^3)K^3}
\longrightarrow\frac{3\pi}{8a},
$$

so a blanket treatment of the quarter slack is especially invalid in the thin-shell scaling.

## Dimension-reduction route

For a finitely supported nonnegative integer sequence $(q_\ell)$,

$$
\sum_{\ell\ge0}(2\ell+1)q_\ell
=\sum_{r\ge0}\left(q_r+2\sum_{\ell>r}q_\ell\right).
$$

For the coarse proxy, set

$$
q_\ell=[A_{\rho,K}(\nu_\ell)+\tfrac14]_<
$$

and define the ordinary-floor tail majorant

$$
\mathcal T_r
=\left\lfloor A_{\rho,K}(r+\tfrac12)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A_{\rho,K}(r+j+\tfrac12)+\frac14\right\rfloor.
$$

The proposed shifted-tail sublemma is

$$
\boxed{
\mathcal T_r
\le2\int_{r+1/2}^{K}A_{\rho,K}(z)\,dz
\qquad(r\in\mathbb N_0).
}
$$

If it holds for every $r$, summing and introducing

$$
f_3(z)=\#\{r\ge0:r+\tfrac12\le z\}
$$

gives

$$
\sum_{\nu_\ell<K}2\nu_\ell q_\ell
\le2\int_0^K f_3(z)A_{\rho,K}(z)\,dz.
$$

The primitive $F_3(z)=\int_0^z f_3(t)dt$ satisfies $F_3(z)\le z^2/2$. Since $A_{\rho,K}$ is decreasing and vanishes at $K$, integration by parts yields

$$
2\int_0^K f_3A_{\rho,K}
\le\int_0^K2zA_{\rho,K}(z)\,dz,
$$

which is exactly the Weyl target.

The FLPS convex theorem proves the shifted-tail sublemma whenever

$$
r+\frac12\ge\mu,
$$

because that tail is $G_K$ alone. The unresolved tails start below $\mu$ and cross the concave/convex interface of $A_{\rho,K}$.

## Thin-width exact zero region

For every half-integer order $\nu\ge1/2$, Nicholson's formula and $\cosh(2\nu t)\ge\cosh t$ give

$$
M_\nu(x)^2\ge M_{1/2}(x)^2=\frac{2}{\pi x}.
$$

Hence

$$
0<\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}\le1
$$

and

$$
\Psi_{\nu,\rho}(K)\le(1-\rho)K.
$$

Therefore the actual strict shell count is zero whenever

$$
(1-\rho)K\le\pi.
$$

At equality, the $\ell=0$ phase is exactly $\pi$ and is excluded by strict counting.

## Permitted dependencies

- `CONV-strict-counting`
- `SHELL-count-floor-identity`, with its current completeness caveat
- `SHELL-phase-enclosures`
- `SHELL-annulus-phase-transfer`
- `SRC-annuli`
- `SRC-bessel-phase`
- `SRC-FLPS-balls`
- `sources/annuli_polya.md`
- `sources/bessel_phase_enclosures.md`
- `sources/flps_balls.md`

## Falsification cases

- $K<1/2$: empty active sum;
- $K\in1/2+\mathbb Z$: strict cutoff equality $\nu=K$;
- $\mu\in1/2+\mathbb Z$: sampled inner interface, where $H_\mu(\mu)$ is forbidden;
- $U_{\rho,K}(\nu_\ell)\in\mathbb N$: strict proxy equals $U-1$;
- $K$ equal to a shell eigenfrequency;
- $\mu<1/2$: every active tail begins at or above the inner interface;
- tails with $r+1/2$ immediately below and immediately above $\mu$;
- $\rho\to1$ with $(1-\rho)K=O(1)$;
- $\rho\to0$;
- walls $A_{\rho,K}(\nu_\ell)+1/4\in\mathbb N$;
- any use of the Rayleigh cutoff $\ell(\ell+1)<K^2$ as though it were the sharp phase cutoff $\nu_\ell<K$.

## Promotion rule

Do not promote `SHELL-weighted-lattice-fractional` from diagnostics or from the continuous phase sum. Promotion requires either a complete proof of all shifted tails or a different complete weighted-floor proof, followed by an independent clean-room reconstruction and adversarial audit. The exact thin-width zero lemma and the algebraic dimension reduction may be promoted separately if their own proof gates pass.
