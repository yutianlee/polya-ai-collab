# Round 18 Lorch Source Audit

Date: 2026-07-14

## Audit question

Does Lee Lorch's 1993 paper supply rigorous lower bounds strong enough to prove

$$
j_{5/2,1}>\frac{51}{10},\qquad
j_{7/2,1}>\frac{13}{2},\qquad
j_{9/2,1}>\frac{15}{2},
$$

and what additional work is required before these ordinary-Bessel bounds can be used for Dirichlet spherical-shell angular channels?

## Primary-source evidence

The primary publisher page is Lee Lorch, “Some Inequalities for the First Positive Zeros of Bessel Functions,” *SIAM J. Math. Anal.* 24(3) (1993), 814–823, [doi:10.1137/0524050](https://epubs.siam.org/doi/10.1137/0524050).

The SIAM abstract explicitly identifies $j_{\nu,1}$ as the first positive zero of $J_\nu$ and, for $-1<\nu<\infty$, prints the two strict inequalities

$$
j_{\nu,1}^2>(\nu+1)(\nu+5)
$$

and

$$
j_{\nu,1}^2>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
$$

All three required half-integer orders lie strictly inside that scope.

The spherical-Bessel conversion was checked separately against [NIST DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3):

$$
\mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
$$

so positive zeros coincide.

## Exact arithmetic audit

| Angular channel | Order | Lorch input | Exact lower bound for $j_{\nu,1}^2$ | Target-square check | Verdict |
| --- | ---: | --- | --- | --- | --- |
| $\ell=2$ | $5/2$ | first inequality | $105/4$ | $105/4-(51/10)^2=6/25>0$ | $j_{5/2,1}>51/10$ |
| $\ell=3$ | $7/2$ | second inequality | $(81\sqrt5-9)/4$ | $81^2\cdot5-178^2=1121>0$ | $j_{7/2,1}>13/2$ |
| $\ell=4$ | $9/2$ | second inequality | $(363\sqrt{15}-121)/22$ | $66^2\cdot15-247^2=4331>0$ | $j_{9/2,1}>15/2$ |

The denominators used in the last two rows are, respectively,

$$
6(\sqrt5-1)>0,
\qquad
4(\sqrt{15}-2)>0,
$$

so the rationalizations do not reverse an inequality or cross a singularity. Each conclusion from a squared inequality is legitimate because $j_{\nu,1}$ is the *positive* first zero.

## Provenance boundary

The logical chain must be recorded as follows:

1. **External, Lorch:** the three lower bounds for ordinary Bessel zeros above.
2. **External reference identity, DLMF:** positive spherical-Bessel zeros in channel $\ell$ coincide with those of $J_{\ell+1/2}$.
3. **Existing project input:** the unit-ball first Dirichlet frequency in channel $\ell$ is $j_{\ell+1/2,1}$.
4. **Internal lemma still required in the Round 18 proof:** extension by zero from the shell to the ball, followed by min–max in the fixed angular subspace, gives

   $$
   k^{\mathrm{shell}}_{\ell,1}(\rho)
   \ge j_{\ell+1/2,1}.
   $$

5. **Internal counting consequence:** only after step 4 may the three rational thresholds be used to exclude the first $\ell=2,3,4$ shell modes.

Lorch's result concerns zeros of $J_\nu$, not zeros of the shell Bessel cross-product. It neither states nor proves step 4. A global domain-monotonicity slogan is insufficient for the channel-labelled claim unless the invariant angular-subspace min–max argument is made explicit.

## Access limitation

The exact statements needed here are visible in the primary SIAM abstract. The full article is access-controlled in the audited environment, so this audit did not inspect Lorch's proof, article-internal theorem numbering, or any qualifications that might be discussed only in the body. The publisher abstract itself gives the definition, strict inequalities, and complete stated parameter range needed for the three substitutions.

Accordingly, the result is a **qualified positive source audit at statement level**, not an independent proof reconstruction.

## Verdict

**PASS, with an explicit provenance condition.** The primary source justifies all three proposed rational first-zero bounds by exact arithmetic. Round 18 may cite those bounds as an external dependency, provided it proves and separately labels the fixed-channel shell-to-ball variational comparison. The source must not be cited for shell cross-product zeros, higher radial modes, multiplicity counts, or Weyl estimates.
