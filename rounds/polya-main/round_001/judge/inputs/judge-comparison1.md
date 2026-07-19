Use **`judge2-001.md` as the better base**, but merge in two pieces from `judge-001.md`.

The main reason: **judge2 is better calibrated**. It keeps the shell route primary, identifies the exact monotone phase representation as the real Round 1 structural advance, and keeps the proof-graph-safe `mathematical_progress_score` at **3/10**, explicitly because the two quantitative blockers remain untouched. That is more accurate than `judge-001.md`, which assigns `mathematical_progress_score: 7` despite also saying no theorem proof exists and the inner-turning and weighted-lattice blockers remain open.

### Verdict

**Better file: `judge2-001.md`.**

### Why `judge2-001.md` is stronger

`judge2-001.md` gives a cleaner strategic decomposition:

1. **Layer 1:** exact phase factorization and monotonicity of
$$
   \Psi_{\nu,\rho}(k)=\theta_\nu(k)-\theta_\nu(\rho k)
$$
   as the qualitative scaffold.
2. **Layer 2:** the two hard quantitative blockers:
   `SHELL-inner-turning` and `SHELL-weighted-lattice-fractional`.

That structure is sharper than `judge-001.md`'s broader list of obligations. It also explicitly says ellipse and certificate-family tracks remain open/source-audit, not blocked, which matches the project strategy.

It also gives better next-round prompts. A1 gets a source-card task centered on Nicholson and annulus floor-sum hypotheses; A2 gets the phase scaffold and inner-turning task; A3 gets the actual weighted-lattice theorem and exact-root defect scan; A4 gets Sturm--Liouville completeness plus stabilized computation. These are concrete and well assigned.

Most importantly, `judge2-001.md` is more honest about progress. It says Round 1 made "real, checkable" but foundational progress and keeps mathematical progress low because the quantitative blockers are still open. That is the right calibration for this project.

### Where `judge-001.md` is still useful

`judge-001.md` has a more complete **validator-style State Patch** in one respect: it creates `SHELL-sturm-liouville-completeness` as a separate lemma, with a good statement requiring the separated spectral decomposition, positivity/simple radial roots, and harmless cross-$\ell$ degeneracy. That obligation should be kept.

It also gives a conservative `SHELL-fixed-rho-high-energy` statement that avoids leaning too hard on the floor-free/midpoint-quadrature mechanism. That formulation is safer as an obligation statement than judge2's more speculative "primary mechanism" phrasing.

### Main weakness of `judge-001.md`

The biggest flaw is over-scoring: `mathematical_progress_score: 7` is too high for a round that produced no theorem proof, no source cards, no certified computation, and no quantitative high-energy bound.

It is also somewhat over-expanded. It creates many obligations at once, which is useful for memory but less clean than judge2's layer split.

### Main weakness of `judge2-001.md`

`judge2-001.md` is slightly too assertive in phrases like "Layer 1 -- now provable." The exact phase factorization is elementary, but monotonicity still depends on source-carding Nicholson's formula, branch normalization, and Sturm--Liouville completeness. Its own confidence section correctly gates this on Nicholson and completeness, so the wording should be softened to "structurally reducible / conditionally provable."

It also should import `SHELL-sturm-liouville-completeness` from `judge-001.md`; otherwise the proof-obligation graph under-specifies the legal path from the cross-product formula to the phase-count identity.

### Recommended final choice

Use **`judge2-001.md` as the accepted judge synthesis**, with these edits before applying the patch:

1. Add `SHELL-sturm-liouville-completeness` from `judge-001.md`.
2. Replace "Layer 1 -- now provable" with "Layer 1 -- structurally isolated; provable after source-card and completeness checks."
3. Keep `mathematical_progress_score: 3`, not 7.
4. Keep `SHELL-angular-cutoff` as `proved_internal` only if the Rayleigh proof is included directly in the patch or lemma bank.
5. Keep `SHELL-spherical-bessel-algebraic` open/proposed unless the $\ell\le2$ verification is actually present in the round artifacts.
6. Preserve judge2's next-round prompts; they are better scoped.

So the practical answer is: **adopt `judge2-001.md`, but graft in the missing Sturm--Liouville completeness obligation and soften a few "proved/verified" phrasings.**
