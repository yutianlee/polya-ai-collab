# Clean-Room Reconstruction: Imported Global Shell Phase Enclosure

## Independence

The reviewer read only state/lemma_packets/SHELL-phase-enclosures.md and the two permitted source cards sources/bessel_phase_enclosures.md and sources/annuli_polya.md. It did not inspect drafts, rounds, reviews, agent state, or the incumbent proof.

## Reconstruction

For fixed $\rho\in(0,1)$ and $\nu\ge0$,

$$
\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}.
$$

Nicholson’s integral makes $M_\nu^2$ strictly decreasing, so

$$
\Psi_{\nu,\rho}'(K)
=\frac{2}{\pi K}
\left(M_\nu(K)^{-2}-M_\nu(\rho K)^{-2}\right)>0.
$$

The fixed branch gives $\Psi(0+)=0$, and the large-argument expansion gives

$$
\Psi(K)=(1-\rho)K+O(K^{-1})\to\infty.
$$

For $\mu=\rho K$ and $0\le\nu\le K$, the permitted annulus result gives

$$
\gamma_{K,\mu}(\nu)<G_K(\nu)-F_\mu(\nu).
$$

Together with $\gamma>0$ and $F_\mu\ge-\tfrac14$,

$$
0<\gamma_{K,\mu}(\nu)
<G_K(\nu)-F_\mu(\nu)
\le G_K(\nu)+\frac14.
$$

If $\nu\le\mu$, including equality,

$$
\Phi_{K,\mu}(\nu)
<\gamma_{K,\mu}(\nu)
<\Phi_{K,\mu}(\nu)+\frac14.
$$

At $\nu=\mu$, this uses the inclusive equation (5.8), not $H_\mu$. If $\mu<\nu\le K$, only the global bound is available. At $\nu=K$, it reads $0<\gamma<\tfrac14$.

The repository determinant is

$$
F_{\nu,\rho}(K)
=M_\nu(\rho K)M_\nu(K)\sin\Psi_{\nu,\rho}(K),
$$

the negative of the annulus convention. Hence its positive zeros are exactly the unique levels $\Psi(K_n)=n\pi$, $n\ge1$, and strict counting gives

$$
\#\{n\ge1:n\pi<\Psi_{\nu,\rho}(K)\}.
$$

At a phase endpoint this is not the floor.

## Correction and verdict

The original packet needed only a quantifier clarification: item 1 fixes $\rho,\nu$ before taking $K\to0+$, while $\nu\le K$ applies to the enclosure claims. The packet has been corrected.

Verdict: PASS. No mathematical counterexample or unsupported implication was found. No uniform relative-error statement as $\rho\to1-$ is implied.
