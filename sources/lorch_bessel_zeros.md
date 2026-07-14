# Source Card: Lorch Lower Bounds for First Positive Bessel Zeros

Status: statement-level audit completed on 2026-07-14 for the three rational lower bounds used in the Round 18 low-angular-channel argument. The publisher exposes the exact inequalities in the article abstract, but the full proof is access-controlled; this card therefore does not claim a proof-level reconstruction of Lorch's paper.

## Primary source

Lee Lorch, “Some Inequalities for the First Positive Zeros of Bessel Functions,” *SIAM Journal on Mathematical Analysis* **24**(3) (May 1993), 814–823.

- Publisher article and abstract: [https://epubs.siam.org/doi/10.1137/0524050](https://epubs.siam.org/doi/10.1137/0524050)
- DOI: [10.1137/0524050](https://doi.org/10.1137/0524050)
- Publisher metadata: volume 24, issue 3, pages 814–823; submitted 24 March 1992 and accepted 17 August 1992.

The SIAM page identifies $j=j_{\nu,1}$ as the first positive zero of $J_\nu(x)$ and states the parameter range $-1<\nu<\infty$. The rendered abstract uses both $v$ and $\nu$ typographically for the order; the formulas and the standard notation $j_{\nu,1}$ make clear that they denote the same parameter.

## Exact source statements used

For $-1<\nu<\infty$, the publisher abstract states

$$
j_{\nu,1}^{\,2}>(\nu+1)(\nu+5),
\tag{L1}
$$

and

$$
j_{\nu,1}^{\,2}>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
\tag{L2}
$$

The abstract says more about monotonicity of the difference in (L1), but Round 18 uses only the displayed strict lower bounds (L1) and (L2). No theorem number is assigned here because the accessible abstract does not expose the article's internal numbering.

## Exact specialization at $\nu=5/2$

Applying (L1),

$$
j_{5/2,1}^{\,2}>
\left(\frac72\right)\left(\frac{15}{2}\right)
=\frac{105}{4}.
$$

The target rational threshold satisfies

$$
\frac{105}{4}-\left(\frac{51}{10}\right)^2
=\frac{2625-2601}{100}
=\frac6{25}>0.
$$

Since $j_{5/2,1}$ is positive by definition,

$$
\boxed{j_{5/2,1}>\frac{51}{10}}.
$$

## Exact specialization at $\nu=7/2$

For $\nu=7/2$, the denominator in (L2) is

$$
1-7+\sqrt{10\cdot18}=6(\sqrt5-1)>0.
$$

The right-hand side of (L2) simplifies exactly to

$$
\frac{486}{6(\sqrt5-1)}-\frac{45}{2}
=\frac{81\sqrt5-9}{4}.
$$

Moreover,

$$
81\sqrt5>178,
$$

because both sides are positive and

$$
81^2\cdot5-178^2=32805-31684=1121>0.
$$

Consequently

$$
\frac{81\sqrt5-9}{4}>\frac{169}{4}
=\left(\frac{13}{2}\right)^2,
$$

and hence

$$
\boxed{j_{7/2,1}>\frac{13}{2}}.
$$

## Exact specialization at $\nu=9/2$

For $\nu=9/2$, the denominator in (L2) is

$$
1-9+\sqrt{12\cdot20}=4(\sqrt{15}-2)>0.
$$

The right-hand side of (L2) simplifies exactly to

$$
\frac{726}{4(\sqrt{15}-2)}-\frac{77}{2}
=\frac{363\sqrt{15}-121}{22}
=\frac{11}{2}(3\sqrt{15}-1).
$$

The comparison with the target threshold reduces to

$$
\frac{11}{2}(3\sqrt{15}-1)>\frac{225}{4}
\quad\Longleftrightarrow\quad
66\sqrt{15}>247.
$$

Both sides are positive, and

$$
66^2\cdot15-247^2=65340-61009=4331>0.
$$

Thus

$$
\boxed{j_{9/2,1}>\frac{15}{2}}.
$$

## Spherical-Bessel identification

NIST DLMF 10.47.3 gives the standard identity

$$
\mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
\qquad \ell\in\mathbb N_0,\quad x>0.
$$

See [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3). The prefactor is positive for $x>0$, so the positive zeros of the spherical Bessel function $\mathsf j_\ell$ are exactly the positive zeros of $J_{\ell+1/2}$. This identifies the three audited orders with angular channels $\ell=2,3,4$.

## What the source supplies to the shell argument

Lorch supplies only the three strict numerical facts

$$
j_{5/2,1}>\frac{51}{10},\qquad
j_{7/2,1}>\frac{13}{2},\qquad
j_{9/2,1}>\frac{15}{2}.
$$

Together with the independently audited ball separation formula, these are lower bounds for the first unit-ball Dirichlet frequency in angular channels $\ell=2,3,4$.

To turn them into shell-channel exclusions, the project must separately prove the channel-preserving variational comparison

$$
k^{\mathrm{shell}}_{\ell,1}(\rho)
\ge j_{\ell+1/2,1}.
$$

The intended internal proof extends a shell radial test function by zero across the inner ball and applies the min–max principle within the fixed $\ell$ spherical-harmonic subspace. Ordinary unlabelled domain monotonicity is not, by itself, a proof of a fixed-channel comparison unless this invariant-subspace argument is written down.

Subject to that internal lemma, the first $\ell=2,3,4$ shell modes are absent, respectively, throughout

$$
K\le\frac{51}{10},\qquad
K\le\frac{13}{2},\qquad
K\le\frac{15}{2}.
$$

## What does not transfer from Lorch

The paper does not provide any of the following shell-specific steps:

- a bound for zeros of the shell cross-product of $J_\nu$ and $Y_\nu$;
- shell-to-ball domain monotonicity, either globally or within a fixed angular channel;
- exclusion of the second or any higher shell radial mode;
- multiplicity-weighted counting, Weyl-volume estimates, or endpoint bookkeeping;
- a certified numerical computation for shell eigenfrequencies.

No one of these statements should be attributed to Lorch.

## Access limitation and audit conclusion

The primary SIAM publisher page exposes the complete two inequalities, their strict direction, the meaning of $j_{\nu,1}$, and the scope $-1<\nu<\infty$. The full article is offered only through subscription or purchase in the audited environment, so its derivations and any hypotheses appearing only in the body were not independently reconstructed. For the exact statements printed in the abstract, the source dependency is verified; for proof-level provenance, this remains a qualified audit.

The three rational consequences used in Round 18 follow by exact algebra, with no floating-point input. They are valid external inputs once the manuscript clearly labels the shell-to-ball fixed-channel comparison as a separate internal variational lemma.
