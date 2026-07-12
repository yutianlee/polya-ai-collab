# FLPS Ball Weight-Transfer Audit

Source audited: Filonov–Levitin–Polterovich–Sher, *Invent. Math.* 234 (2023), 129–169, [doi:10.1007/s00222-023-01198-1](https://doi.org/10.1007/s00222-023-01198-1), arXiv:2203.07696v4.

## Verified source statements

1. In dimension three, the spherical-harmonic multiplicity is $\kappa_{3,m}=2m+1$ and the Bessel order is $m+1/2$.
2. The Dirichlet ball zero count is bounded by $\lfloor G_K(\nu)+1/4\rfloor$ for every real $\nu\ge0$.
3. Theorem 5.1 applies to any nonnegative decreasing convex $1/2$-Lipschitz function $g$ on $[0,b]$ with $g(b)=0$; the endpoint $b$ need not be an integer.
4. The higher-dimensional proof decomposes multiplicity weights into shifted unweighted tail counts.
5. The primitive of the resulting $d=3$ step function is bounded by $z^2/2$, and the exact action integral is $2K^3/(9\pi)$.
6. The Dirichlet ball proof is analytic. Its result does not depend on the paper's computer-assisted Neumann disk calculation.

## Valid shell transfer

For

$$
A_{\rho,K}(z)=G_K(z)-G_{\rho K}(z),
$$

the multiplicity decomposition and final step-function integration argument are purely algebraic and transfer. A shifted tail beginning at $r\ge\rho K$ has

$$
A_{\rho,K}(r+t)=G_K(r+t),
$$

so the abstract convex theorem applies after translation and proves that tail's required integral bound.

## Invalid shell transfer

A tail beginning below $\rho K$ is concave before the inner interface and convex afterwards. The ball theorem assumes convexity on the whole interval. It cannot be invoked across this interface, and two already-proved ball inequalities cannot simply be subtracted through the floor operation.

## Audit verdict

The FLPS ball source discharges the external source dependency for the multiplicity algebra, convex shifted tails, step-function primitive, and exact weighted integral. It does **not** discharge the new inner-interface shifted-tail inequality or the complete shell weighted lattice obligation.
