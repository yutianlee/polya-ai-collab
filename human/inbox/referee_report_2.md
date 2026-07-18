The protocol vocabulary is confirmed. All verification work is complete; here is the referee report in the Stage A schema.

---

# A2 Referee Report — Round Output

**Target:** full referee audit of `spherical-shell-polya-proof.tex` + analytic supplement (Dirichlet Pólya, 3D spherical shells, strict counting)

## Summary

I performed a full logical audit of the main manuscript (3285 lines, read in entirety), a detailed reading of supplement Parts V–IX with spot-reading of Parts I–IV, an exact-rational replay of roughly sixty of the highest-risk finite certificates (all match), and a source audit of the five imported FLPS results against the published papers (fetched arXiv:2505.21737 / JLMS 113 (2026) e70425 and arXiv:2203.07696 / Invent. Math. 234 (2023)). **I found no mathematical error.** The remaining obstacles to promoting the main theorem are not gaps in the argument but verification obligations: one outstanding source card (Lorch 1993), the mechanical replay of the ~450 not-yet-replayed ledger rows, and repository self-containedness (the supplement's LaTeX sources are absent). The theorem should move to `derived_under_assumptions` now, with a clear path to `proved_external_dependency`.

## Target proof obligation

The shell main theorem: for A_{r,R} = {r < |x| < R} ⊂ ℝ³ with strict Dirichlet counting N_D(Λ) = #{λ_j < Λ},

$$N_D(A_{r,R},\Lambda)\ \le\ \tfrac{2}{9\pi}\,(R^3-r^3)\,\Lambda^{3/2}\quad\text{for all }0<r<R,\ \Lambda>0,$$

together with the independent non-tiling statement (§6).

## Main claim or direction

The proof architecture is sound end-to-end. The exact strict phase count, the proxy reduction, the weighted multiplicity scaffold, the five regional owners (small hole, primitive owners, staircases, lower closure, optical), the all-frequency middle certificate on the residual compact rectangle, the complementation set algebra, and the scaling/assembly step all check out under independent derivation. Every printed rational certificate I replayed — including the four Bernstein tables recomputed *from definitions* rather than transcribed — reproduces exactly.

## Detailed reasoning

**Internal chain (verified by independent derivation).** The separation proposition (unitary u = rR substitution; the boundary-term cancellation ∫r²|R'|² = ∫|u'|² under zero traces is correct for complex u), the cross-product factorization D = M(ρk)M(k)·sin Ψ with Ψ' > 0 via Nicholson (M_ν² strictly decreasing), and the resulting exact strict count N_D = Σ_ℓ (2ℓ+1)[Ψ_{ν,ρ}(K)/π]_< with [x]_< = max{0, ⌈x⌉−1} are all correct, including the branch Ψ(0⁺) = 0 and the wall convention (roots at Ψ = nπ excluded at equality — strict counting handled consistently everywhere I checked). The z ≥ K inactivity argument needs only θ_z(μ)/π > −1/2 strict plus the published upper bound, so the λ = z edge of the phase enclosure carries no hidden exposure. The weighted scaffold's step primitive (s−1/2)²/2 and the exact action integral ∫2zA = (2/9π)(1−ρ³)K³ are re-derived; the small-hole theorem's interface bookkeeping (δ < 2√2/15, payment ⌊ω₀K⌋ − n > 8√2/15 = 4·(2√2/15)) is airtight, including the μ ≤ 1/2 face at K(ω₀−ρ) = C_*. The primitive-owners items 1–5 (including the K₀ root algebra and the c_ρ-Lipschitz first-shelf application, with the no-drop case correctly routed through the basic concave bound rather than the improved theorem) are correct. The moving-payment derivative criterion aπ²(1+ρ) > bρ²(1−ρ)² I re-derived from scratch; it matches the printed condition, and b/a ≤ 42 clears it with a factor ~3.5 of room. The lower-closure wedge (⌊3x/4 − 1/2⌋ < ⌊x⌋ for x > 1, the m ≤ 2p−1 casework, the exactly-critical corner ρ₀d = 1/2 saved by open conditions) and the 𝓑-cell turning-bound cap (395 < W with the (K−z)^{3/2}/√K monotonicity justifying evaluation at K = 367/20) are correct.

**Supplement Parts V, VII–IX (the genuinely novel analysis).** Part V resolves what initially looked like an error: the main text's optical high-screen rational 14817541/472867032960000 is not a pointwise deficit but the coefficient comparison L(ε₀) − A(ε₀) after the one-sided substitution 1/a ≤ ε/c, with L decreasing and A coefficientwise increasing in ε. Both screens are structurally valid and both reserves replay exactly. Part VII's retained-remainder identity (the −1/8 + 1/32 + 3/32 cancellation), the Stieltjes cell decomposition (g continuous at the turning point τ from both branches, boundary terms controlled), and the normalization 2I/ε² = W are verified. Part VIII's one-layer paired block r_n ≤ (4/3)∫R − 3/4 and the resulting 𝓔_ang < (1−ρ²)K²/6 − N/2 with N ≥ 1 on the rectangle are correct (the Euler common-jump lemma there is expository and unused — no dependency). Part IX's scalar module is the most delicate piece and it holds up: the ∂_K𝒥 cancellation, the beta-integral chain through π⁵/(59049√3) < (88/567)³, the K ≥ 12 monotonicity step (licensed by k₁₁ > 241/20), and the base-curve reduction through E(t), the secant quadrature, and the degree-9 Bernstein certificate on [7/15, 14/15] — whose containment of the t-range is itself one of the hairline checks (11/50 > 49/225 by 1/450).

**Exact-rational replay (diagnostic under protocol; the manuscript's own standard is hand-checkability).** All of the following reproduce exactly, in integer arithmetic, from definitions: both optical reserves; the product-screen minimum 1822532/91552734375 and N-step margin 4229603/29296875; the Part IX rational chain and both Bernstein tables (cubic and degree-9, recomputed from the displayed polynomials, all coefficients positive); the giant secant quadrature Q and 17/100 − Q > 0; an independent Simpson evaluation of the same loss integral (≈0.16700 < 0.17) as a sanity cross-check; the six k₆ moving-payment numerators (up to 24 digits); five k₆ fixed margins; seven lower-d margins; five lower-closure staircase reserves; the 𝓑-cell payment 160293325/378004 > 395; the cap-74 payment (which uses 1/π > 7/22, not 113/355 — my only initial mismatch, resolved as a bookkeeping ambiguity, not an error); the Machin truncation residual; and all hairline threshold residuals (111, 47711, 23, 1998482, 41877, 471/10000, 227/300, 1/450, 32/3825).

## Theorem-dependency audit

Source cards, all statements checked against the published texts this round:

| Import | Published source | Statement match | Status |
|---|---|---|---|
| Individual phase enclosure ℱ_a − 1/4 < θ_z(a)/π < G_a − 1/4, all real z ≥ 0, a > 0 | FLPS annuli, Thm 5.1 (JLMS 113 (2026) e70425) | verbatim; real order, no interpolation needed for ν = ℓ+1/2 | **closed** |
| Difference enclosures incl. two-sided G_K−G_μ < Γ < G_K−G_μ+1/4 up to z = μ | FLPS annuli, Lemma 5.2 (eqs. 5.5–5.8) | verbatim, including the z = μ endpoint | **closed** |
| Concave trapezoid T(g) ≤ ∫g | FLPS annuli, Prop 3.1 | verbatim | **closed** |
| First-shelf concave improvement, Lip_c, drop hypothesis, −(1−c)(β−p)/2 | FLPS annuli, Thm 1.4 | verbatim | **closed** |
| Improved convex bound, Lip_{1/2} + Lip_{1/3} on [t,b], −⌊g(t)⌋/4 | FLPS annuli, Thm 3.4 (+ Lemma 3.5 confirming the 1/3 constant) | verbatim | **closed** |
| Turning bound G_μ(z) < (μ−z)^{3/2}/(3√μ) | FLPS annuli, Lemma 6.2 (upper half) | verbatim; *also re-derived internally* via arccos t ≤ (π/2)√(1−t) | **closed, doubly covered** |
| Shifted convex tail ⌊g(0)+1/4⌋ + 2Σ⌊g(m)+1/4⌋ ≤ 2∫₀^b g, real b > 0 | FLPS balls, Thm 5.1 (Invent. Math. 234 (2023)) | verbatim — real b, so no integer-endpoint translation issue | **closed** |
| Nicholson's formula | DLMF 10.9.30 | standard | **closed** |
| First-zero bound j²_{ν,1} > 24(ν+1)²/(1−2ν+√((2ν+3)(2ν+11))) − 2(ν²−1) | Lorch, SIAM J. Math. Anal. 24 (1993) | specialization algebra R_ℓ re-derived; the seven derived rational walls all numerically true against actual Bessel zeros; **published statement not yet sighted** | **source_audit_required** |

Two structural points worth recording. First, all imported items come from the *analytic* sections of the FLPS papers; the shell manuscript does not touch their computer-assisted theorems (annuli Thm 8.2, balls Thm 4.4), so the "purely analytic modulo hand-checkable rational arithmetic" framing survives the audit — with the footnote that annuli Lemma 5.2's own proof uses Horsley's published phase-derivative bounds. Second, the FLPS convention is non-strict counting with ordinary floors; the shell manuscript uses strict counting with [·]_< and derives its exact enumeration internally, importing only convention-free inequalities. No conflict.

## Hidden assumptions and potential gaps

None mathematical, after the Part V resolution. The itemized flags:

1. **Self-containedness (major, presentational).** The main-text compact certificate lemma and the optical high screen cannot be verified from the main text alone; the content lives in supplement Parts V and VII–IX, whose LaTeX sources are absent from the repository (only compiled page bundles exist). The content is verified, but the sources must be committed and the main text should display L(ε), A(ε) rather than a bare rational.
2. **Scaffold restatement (trivial fix).** The weighted scaffold lemma is stated with a per-tail hypothesis but the lower-closure lemma applies it in aggregate. The proof only uses Σ_r 𝒯_r, so the aggregate form is valid; restate the lemma accordingly.
3. **Lorch source card** (above) — the one remaining external unknown. Repair path exists even in the worst case: the seven walls are re-derivable internally from the P_ℓ sign registry.
4. **Hairline margins to protect under any future revision:** ω₀d > 1 (residual 111/134689), the Bernstein window containment (1/450), the optical high screen (3.1×10⁻⁸), the low screen (1.4×10⁻⁵), the Part IX loss reserve (≈5.6×10⁻⁴), and √2 > 7/5. All verified exact; all fragile to convention changes.
5. **Cosmetic:** the "thin-seam wall" 54/(1−ρ)² in Part V references a retired owner absent from the main text (harmless since 39/50 < 5/6; excise or define); the k₆ lemma's use of 17/2 for the (5,1) wall where the registry has 87/10 is a deliberate conservative weakening and deserves a remark; payments should state which rational π-enclosure they use.
6. **Unreplayed ledger remainder** (~450 of 611 rows: most Z, KI, LOC, CP families). The method is verified and every row I sampled is correct — including one KI row, (3,2) at k₈, that is listed as possible but is actually excluded, i.e. slack in the safe direction — but full replay is the natural closing obligation.

## Counterexample or obstruction search

Stress tests run: all ten zero-registry walls against true Bessel zeros (all safe, tightest is j_{3/2,2} ≈ 7.7253 vs wall 77/10); the exactly-critical wedge corner ρ₀d = 1/2 (strictness recovered from open conditions); the N = 0 edge of Part VIII (excluded since T > 1 on the rectangle); the z = K wall (needs no strictness from the phase bound); the k₉ conservative cap-74 row (paid with reserve ≈1.03); Simpson cross-check of the Part IX loss integral. No obstruction found.

## Verification

Independent, this round: full read of main text; Parts V–IX read and re-derived; ~60 exact-rational replays, all matching; two published-source fetches closing seven of eight source cards. Everything replayed used integer/rational arithmetic only, consistent with the manuscript's own hand-checkability standard.

## Divergent alternatives and 20% exploration

Not exercised this round beyond noting that the internal arccos-derivation of the turning bound means the Lemma 6.2 dependency could be dropped entirely from the dependency graph with a one-paragraph edit — worth doing, as it shortens the external surface. A similar internalization of the Lorch walls via the P_ℓ registry is feasible if the source card stalls.

## Useful lemmas

The aggregate-form scaffold restatement (item 2 above) should be added as the official statement. The internal arccos t ≤ (π/2)√(1−t) derivation deserves promotion from a remark to a lemma so the turning bound is formally internal.

## What should be tested next

A4 should replay the remaining ledger rows (Z: 48, KI: 117 cells, LOC: 47, CP remainder, SUB/SUP) in exact rational arithmetic from the row definitions, not the printed values — the same discipline used here for the Bernstein tables. A1 or the human should pull the Lorch 1993 statement. The repository needs the supplement sources committed.

## Proposed state patch, if any

```yaml
patch:
  - id: SHELL-MAIN-THEOREM
    status: derived_under_assumptions
    evidence: "A2 full audit R-current: no mathematical error; internal chain verified; ~60 exact-rational replays all match"
    next_action: "close SRC-LORCH-1993 and LEDGER-REPLAY-FULL, then promote to proved_external_dependency"
  - id: SRC-FLPS-ANNULI-PHASE
    status: proved_external_dependency
    source_card: "FLPS, JLMS 113 (2026) e70425, Thm 5.1 + Lem 5.2; verbatim match incl. real order and z=mu endpoint"
  - id: SRC-FLPS-FLOOR-SUMS
    status: proved_external_dependency
    source_card: "FLPS annuli Prop 3.1, Thm 1.4, Thm 3.4 (Lem 3.5 confirms 1/3); FLPS balls Invent. Math. 234 (2023) Thm 5.1, real b>0; all verbatim"
  - id: SRC-FLPS-TURNING-BOUND
    status: proved_internal
    evidence: "annuli Lem 6.2 verbatim AND internal arccos derivation in manuscript; recommend dropping external edge"
  - id: SRC-LORCH-1993
    status: source_audit_required
    source_card: "Lorch, SIAM J. Math. Anal. 24 (1993); displayed inequality and nu>-1 hypothesis to be sighted"
    next_action: "obtain published statement; fallback: internalize seven walls via P_ell registry"
  - id: LEDGER-REPLAY-FULL
    status: open
    next_action: "A4: exact-rational replay of remaining ~450 rows from row definitions; A2 replayed ~60 highest-risk rows, all match"
  - id: REPO-SUPP-SOURCES
    status: open
    next_action: "commit analytic supplement LaTeX sources; only compiled page bundles present"
  - id: TEXT-EDITS-MINOR
    status: open
    next_action: "aggregate scaffold restatement; display L,A in optical lemma; excise thin-seam remnant; remark on 17/2 wall; state per-payment pi-enclosures"
```

## Confidence

High (≈0.9) that the proof contains no mathematical error, based on complete structural verification plus exact replay of every certificate examined. Moderate-high (≈0.75) that the remaining obligations close without incident: the ledger remainder is mechanical and the Lorch bound is classical with a known repair path. Per the safety rules, I do not claim the theorem proved; the correct present status is `derived_under_assumptions` with the patch above.