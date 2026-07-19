# Incumbent Proof: Imported Global Shell Phase Enclosure

The lemma packet’s quantifiers are understood as follows: item 1 fixes $\nu\ge0$ and $\rho\in(0,1)$ while $K$ varies over $(0,\infty)$; items 2–6 additionally impose $\nu=\ell+\tfrac12\le K$.

From

$$
\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}
$$

and the strict decrease of $M_\nu^2$ from Nicholson’s integral,

$$
\Psi_{\nu,\rho}'(K)
=\frac{2}{\pi K}
\left(M_\nu(K)^{-2}-M_\nu(\rho K)^{-2}\right)>0.
$$

The branch normalization gives $\Psi_{\nu,\rho}(0+)=0$, and the large-argument expansion gives

$$
\Psi_{\nu,\rho}(K)=(1-\rho)K+O(K^{-1})\to\infty.
$$

Set $\mu=\rho K$ and suppose $0\le\nu\le K$. FLPS annuli Lemma 5.2, under $(\lambda,\mu,z)=(K,\rho K,\nu)$, gives

$$
\gamma_{K,\mu}(\nu)<G_K(\nu)-F_\mu(\nu).
$$

Since $F_\mu(\nu)\ge-\tfrac14$ and $\theta_\nu(K)>\theta_\nu(\rho K)$,

$$
0<\gamma_{K,\mu}(\nu)
<G_K(\nu)-F_\mu(\nu)
\le G_K(\nu)+\frac14.
$$

When $0\le\nu\le\mu$, including $\nu=\mu$, equation (5.8) gives

$$
\Phi_{K,\mu}(\nu)
<\gamma_{K,\mu}(\nu)
<\Phi_{K,\mu}(\nu)+\frac14.
$$

At $\nu=\mu$, $G_\mu(\mu)=0$; the divergent $H_\mu(\mu)$ is not used. On $\mu<\nu\le K$, $F_\mu(\nu)=-\tfrac14$, so only

$$
0<\gamma_{K,\mu}(\nu)<G_K(\nu)+\frac14
$$

is asserted. In particular, $\nu=K$ gives $0<\gamma(K)<\tfrac14$.

Direct substitution into the repository determinant gives

$$
\begin{aligned}
F_{\nu,\rho}(K)
&=J_\nu(\rho K)Y_\nu(K)-Y_\nu(\rho K)J_\nu(K)\\
&=M_\nu(\rho K)M_\nu(K)\sin\Psi_{\nu,\rho}(K).
\end{aligned}
$$

The annulus determinant is its negative. Positivity of the moduli and strict monotonicity of $\Psi$ show that positive zeros are uniquely indexed by

$$
\Psi_{\nu,\rho}(K_n)=n\pi,\qquad n\ge1.
$$

Therefore

$$
K_n<K\iff n\pi<\Psi_{\nu,\rho}(K),
$$

and the strict radial count is

$$
\#\{n\ge1:n\pi<\Psi_{\nu,\rho}(K)\}
=\left\lceil\frac{\Psi_{\nu,\rho}(K)}{\pi}\right\rceil-1.
$$

At a phase endpoint this is one smaller than the floor. As $\rho\to1-$, the main phase difference shrinks while the $1/4$ allowance need not; no uniform relative-error conclusion is claimed.

Verdict: proved from the permitted dependencies, subject to the quantifier clarification now incorporated into the lemma packet.
