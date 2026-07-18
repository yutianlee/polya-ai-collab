# Structural simplification review of the frozen main manuscript

## Scope and baseline

This reviews proof strategy and organization in
manuscript/spherical-shell-polya-proof.tex. It does not edit or re-prove the
frozen manuscript. Line references are to the 4,332-line source with SHA-256
84D079A9FD3A6001C7F00A528F7EAF40799D6850E87537BDC3819A98A9F6D982.
The compiled paper is 52 pages.

The paper currently serves three roles at once: journal article, technical
supplement, and exact-arithmetic audit ledger. The main opportunities are
therefore to remove duplicated proof owners, expose a shorter dependency
spine, and move proof-critical arithmetic to stable support exhibits.

The most important new finding is now independently audited: Parts VII--IX
prove the compact inequality for every K >= k_11(rho), not merely K <= 200.
The upper cutoff occurs only in declared domains. After widening those
statements, the aggregate-Q route and the split at K = 200 are mathematically
unnecessary.

The page estimates below overlap. A realistic first target is 42--45 pages
using only deduplication and the all-K compact extension. Moving standard
derivations and long exact tables to a referee-visible supplement can bring
the main paper to roughly 36--40 pages. The more aggressive optical reordering
described below can reduce it further, but requires a complete owner-face
audit.

## Classification

- E (editorial): safe compression, relocation, or reordering; no proof change.
- G (proof-graph): no new estimate, but theorem domains or owner dependencies
  must be rewritten and re-audited.
- M (new mathematics): a genuinely new uniform bound or argument is required.

## Concrete revisions

| Current lines | Revision | Main-paper saving | Risk | Type |
|---|---|---:|---|---|
| 199--497 | Keep concise statements of radial separation, multiplicity, the Bessel determinant, strict phase enumeration, and finiteness. Move the form-domain/direct-sum proof and standard determinant/root details to the supplement. | 2.5--3 pages | Low | E |
| 516--735 | State the coarse phase proxy and exact action integral directly. The refined H_a, F_a, U construction and fractional budget ending at eq:sc-fractional-budget have no downstream use. Move or delete that diagnostic refinement. | 1--1.5 pages | Low/medium | E |
| 737--1181 and 2111--2247 | Consolidate the multiplicity-tail identity, weighted scaffold, action integral, high-interface bound, low-interface payment, and small-hole owner. The compact primitive-owner section re-proves the earlier machinery. | 1.5--3 pages | Low | E |
| 1271--1315, 1347--1386, 1537--1602, 1651--1735, 1767--1839 | Retain statements and decisive chains for the product, inverse-action, layer-cake, and Stieltjes lemmas. Move their elementary derivations to stable support exhibits. | 2.5--3.5 pages | Low/medium | E |
| 1388--1484 and 1841--2018 | After promoting the optical theorem to the large-hole owner, remove the specialized thin-shell low/high assemblies and endpoint theorem. The optical proof uses the generic tools above, not these propositions. | 2.5--3.5 pages | High integration | G |
| 2022--2064 | Remove repeated definitions of the strict count, W, G_a, A, omega_0, C_*, and rho_*. Keep only genuinely new compact-middle notation. | 0.3--0.5 page | Low | E |
| 2329--2469 | Once the optical theorem is applied for rho >= 39/50, remove the seam owner entirely: its domain rho >= 5/6 is a strict subset of the optical domain. | 1--1.5 pages | High integration | G |
| 2546--2626 | Remove the exact rational locator for rho_HK. Existence and uniqueness at 2522--2545 are operative; the decimal bracket is not used in an analytic implication. | 0.8--1 page | Low | E |
| 2551--2626, 2731--2889, 3187--3241 | Consolidate repeated pi, radical, and rational constant checks into one exact-constants lemma. The tight Machin calculation disappears with the unused switch locator. | 0.4--0.7 page | Low | E |
| 2699--2729 versus 2084--2110 | Introduce the fixed-channel min--max, product, ball, and angular-propagation comparisons before the primitive-owner proposition. They are currently used before being introduced. | negligible | Low | E |
| 2731--2889 | Keep the final zero-wall conclusions and propagation table. Move Bessel-polynomial expansions and exact sign certificates to Parts I--II, using stable exhibit references. | 1.4--1.8 pages | Low/medium | E |
| 2899--3056 versus 3066--3121 | Remove or relocate the separate first-bands and k_5 lemmas and residuals D_17, D_18. The k_6 lemma already covers the closed range z <= K <= k_6 and repeats their complete entry/payment inventory. | 1.8--2.2 pages | Low/medium | E |
| 2948--2965 | Delete the historical former-pilot-rectangle discussion. | 0.2 page | Low | E |
| 3072--3120, 3129--3161, 3186--3241, 3289--3395, 3432--3542 | Keep staircase statements, completeness, monotone payment, strict-wall ownership, and the exceptional cap-74 correction. Move complete numerator lists, cap tables, and routine exact comparisons to Parts I--VI. | 3.5--4.5 pages | Medium | E, but proof-critical relocation |
| 3677--3738 | Widen the compact theorem to rho_c <= rho <= 39/50 and K >= k_11(rho). Compress its main proof to the angular bound, scalar reserve, structural implication, and phase bridge. | 0.4 page inside the lemma | Medium | G; audited mathematically |
| 3740--4008 | Delete the aggregate-Q construction, aggregate-tail theorem, and C_21/T_21 split after adopting the all-K compact theorem. | about 3--3.5 pages | Medium | G; audited mathematically |
| Support Parts X--XIII; Part XIV | Parts X--XIII total 18 support pages and become optional alternative evidence. Replace the current two-page split assembly in Part XIV by a direct all-K compact closure, or remove it if the main assembly is self-contained. | 18--19 support pages | Medium | G |
| 4041--4079 | Replace the full dependency/census ledger by one paragraph and leave detailed allocation in the supplement preface. | 0.4--0.5 page | Low | E |
| 4164--4269 | Put the independent non-tiling theorem in an appendix, or in the supplement if the target journal wants a shorter spectral paper. | 0 in an appendix; about 1.2 pages if moved out | Low | E |

Also define the strict bracket once rather than at both 169--181 and
1186--1193. Cite, rather than restate, the phase input at 1209--1230. Move the
dependency remark at 2002--2013 to the final proof-map paragraph.

## Independent audit: extension of Parts VII--IX to all K

### Verdict

PASS mathematically; statement amendments are required.

For

rho_c <= rho <= 39/50,  K >= k_11(rho),

the existing arguments in Parts VII--IX prove

N_D(A_{rho,1}, K^2) < W(rho,K).

There is no hidden use of K <= 200.

### Part VII: structural implication

- compact-structural.tex, lines 53--58, defines the action for every
  0 < rho < 1 and K > 0.
- Its exact layer cake is global at lines 161--194.
- The retained radial-deficit identity is global at lines 270--359.
- The primitive minorant and sufficient implication
  E_ang < H implies P < W are global at lines 367--461.
- The only occurrence of K <= 200 is the contextual residual definition at
  lines 75--86. No subsequent estimate invokes the upper endpoint.

### Part VIII: angular estimate

- compact-angular-block.tex, lines 288--330, proves the one-layer paired
  block without a compact-frequency assumption.
- Lines 332--379 prove the global strict estimate
  E_ang < (1-rho^2)K^2/6 - N/2 for every K > 0 with N >= 1.
- For K >= k_11(rho), lines 400--406 give T > 1 and hence N >= 1. This
  argument uses only the lower frequency bound.
- The sole upper cutoff is the declared region at lines 392--398.

### Part IX: scalar monotonicity

- compact-scalar-positive.tex, lines 124--195, bounds the loss derivative
  for every K > 12. The beta majorant decreases as K^(-2/3), so it improves
  when K increases.
- Lines 212--288 prove dS/dK > 0. The K coefficient in the lower bound is
  positive, and the remaining Bernstein sign check depends only on rho.
  Thus the monotonicity direction is exactly the direction needed for
  extension to larger K.
- Lines 293--410 prove the uniform loss estimate using only
  K >= k_11(rho) > 241/20. Its turning-point coefficient increases with K.
  The number 17/200 at lines 465--471 is half of a dimensionless 17/100
  loss bound; it is not a frequency ceiling.
- Lines 527--635 prove positivity on the base curve K = k_11(rho), with no
  upper-frequency premise.
- Lines 637--643 then use
  S(rho,K) >= S(rho,k_11(rho)) > 0. That integration is valid for every
  finite K >= k_11(rho).

The current textual obstruction is only the definition of R_c at
compact-scalar-positive.tex, lines 55--61. The theorem and region-scoped
statements at lines 86--93, 197--210, 293--307, and 637--643 must be widened.
Parallel statement edits are needed in compact-angular-block.tex, lines
392--417, and in the main manuscript at 3677--3692 and 3710--3729.

After those amendments, the extended compact theorem owns every point of
D_20 directly. The main aggregate route at 3740--4008 is redundant. The
corresponding final split in ledger-packet-F.tex, lines 144--169, and
final-analytic-closure.tex, lines 88--116 and 158--200, must be replaced by
the direct owner.

No mathematical lemma needs strengthening. This is a quantifier and
dependency-graph correction, followed by a fresh compile and clean-room audit.

## Independent audit: optical theorem versus thin-shell and seam owners

The all-frequency optical theorem at 3558--3655 covers rho >= 39/50 for every
K. This strictly contains both the thin-shell endpoint rho >= 7/8 and the seam
domain rho >= 5/6.

The optical proof cites only generic tools:

- the fixed-channel product comparison at 2705--2711;
- action geometry at 1507--1602;
- the strict layer cake at 1604--1735;
- the shifted Stieltjes deficit at 1737--1839.

None of those lemma statements assumes epsilon <= 1/8 or rho >= 7/8. The
specialized low-action proposition at 1388--1484 and high-action proposition
at 1841--1967 are not used by the optical proof. The thin-shell theorem is
used only as a final regional owner at 1969--2018 and 4109--4113.

Likewise, the seam proof at 2329--2469 owns

1-rho <= 1/6 and K(1-rho)^2 >= 54,

so rho >= 5/6 > 39/50. It becomes empty after the optical owner is subtracted.

Therefore the specialized thin endpoint and seam proof can be removed without
a new estimate. This is nevertheless a high-integration proof-graph edit:
the generic tools must be moved ahead of the optical theorem, primitive masks
and U(rho) must be simplified, and every equality face must be re-audited.
The clean ratio partition then becomes

(0,rho_*],  (rho_*,39/50),  [39/50,1).

## Recommended concise dependency spine

1. Exact radial separation and strict Bessel-phase enumeration give
   N_D <= P_coarse.
2. The exact action identity identifies the continuum payment with W.
3. A single common toolkit supplies the weighted-tail identity, product
   comparison, inverse-action geometry, layer cake, and Stieltjes deficit.
4. The small-hole theorem owns (0,rho_*]; the optical theorem owns
   [39/50,1) at every frequency.
5. On the remaining ratio interval, primitive high-frequency owners and
   fixed-channel zero walls reduce the problem to one finite staircase
   residual.
6. The k_6, lower-wedge, and k_11 owners exhaust the low-frequency portion;
   their exact arithmetic resides in cited support exhibits.
7. Parts VII--IX prove the last scalar/angular inequality for every
   K >= k_11, so no aggregate K = 200 bridge is needed.
8. A short owner partition and scaling complete the shell theorem.
9. The independent non-tiling theorem appears as an appendix.

This spine eliminates legacy residual stages D_17 and D_18 and the final
D_20-to-D_21 frequency split. Renaming surviving residuals by mathematical
role rather than round number would improve readability, though it is a
medium-risk cross-reference edit.

## Recommended section order

1. Results, strict conventions, and a one-page proof map.
2. Spectral separation and coarse phase reduction.
3. Common tail/product/inverse-action/Stieltjes toolkit.
4. Small-hole and all-frequency optical owners.
5. Fixed-channel comparisons, zero registry, and finite staircase owners.
6. All-K analytic compact closure from Parts VII--IX.
7. Owner assembly and scaling.
8. Non-tiling appendix.

The complementary action should be defined immediately after the normalized
variables at 1194--1207, rather than used at 1220--1223 and introduced only at
1486--1505.

## Changes that really require new mathematics

The following are not editorial or proof-graph simplifications:

- replacing the finite zero-wall and staircase registry by one uniform
  analytic inequality;
- eliminating the remaining exact cap/payment tables instead of relocating
  them to a support exhibit;
- proving a sharper universal floor-discrepancy estimate that replaces all
  low/high branch bookkeeping;
- extending the theorem from concentric spherical shells to general domains;
- dropping strict-wall or exceptional cap-74 analysis without a new reserve.

By contrast, the all-K compact extension and optical subsumption require no
new estimate: their work is statement repair, reordering, and coverage audit.

## Recommended implementation sequence

1. Widen Parts VII--IX and the main compact theorem to all K >= k_11; compile
   and independently re-audit the strengthened statements.
2. Remove the main aggregate-Q route and K = 200 split; archive Parts X--XIII
   as optional alternative evidence and simplify Part XIV.
3. Promote the generic action/layer-cake/Stieltjes lemmas and the optical
   theorem; remove the specialized thin endpoint and seam owner; run a full
   equality-face and owner-subtraction audit.
4. Remove orphan diagnostics and locators, consolidate duplicate small-hole
   machinery, and collapse the first-band/k_5/k_6 repetition.
5. Give every retained exact table a stable support label, move standard or
   mechanical details out of the main paper, recompile, and perform a final
   dependency and reference audit.

