# A2 — Simplification & Alternatives Survey for the Shell Proof

Having audited the manuscript end-to-end last round, I can now map precisely where its complexity lives and which parts are intrinsic versus removable. The complexity budget is roughly: **(i)** the strict-counting bracket machinery threaded through everything; **(ii)** the five-owner regional fragmentation with its complementation algebra (𝒟₁₆ → 𝒟₁₉ → 𝒟₂₀); **(iii)** the ~611-row finite ledger behind the staircase lemmas (Parts I–IV); **(iv)** the scalar-positivity module of the middle certificate (Part IX); and **(v)** the optical lemma's 3×10⁻⁸ hairline margins (Part V), which are a *symptom* of where the seam at ρ = 39/50 was pinned. Below: simplifications inside the current architecture (ranked by cost/benefit), then genuinely alternative architectures with an honest account of why most fail, then negative results worth recording so the panel stops revisiting them.

---

## 1. Simplifications within the current architecture

### 1.1 Switch to the non-strict counting convention (zero mathematical cost, large notational payoff)

The manuscript's strict convention N_D(Λ) = #{λ_j < Λ} forces the bracket [x]_< = max{0, ⌈x⌉−1}, wall-exclusion clauses ("at K = k_m the (m,1) mode is on its product equality wall and is excluded"), and equality-case caveats in every regional owner. But the two conventions are *equivalent for the target inequality*: W is continuous and increasing, so

$$N_<(\Lambda) \le W(\Lambda)\ \ \forall \Lambda \iff N_\le(\Lambda)\le W(\Lambda)\ \ \forall\Lambda,$$

by N_≤(Λ) = lim_{δ↓0} N_<(Λ+δ) ≤ lim W(Λ+δ) = W(Λ). With the non-strict convention the exact count becomes the plain N_≤ = Σ(2ℓ+1)⌊Ψ/π⌋, matching FLPS notation verbatim. Crucially, **no ledger payment changes**: the manuscript already pays cap C_m at the wall via W(k_m) > C_m with strictly positive reserves, which is exactly what the non-strict convention requires on the half-open interval [k_m, k_{m+1}). I checked this against the payment structure cell by cell during the audit; the arithmetic is identical, only the bookkeeping prose disappears. This is the cheapest structural cleanup available and it removes a whole class of wall-coincidence caveats that currently must be re-audited in every lemma.

### 1.2 Move the seam from 39/50 to ~4/5 and detune the optical lemma (largest robustness gain)

The optical lemma's reserves (1.43×10⁻⁵ product screen, 3.13×10⁻⁸ complementary-action screen) look alarming, but they are not intrinsic to the thin-shell regime — they are the price of the seam location. The seam ρ = 39/50 is pinned by **Part IX**, not Part V: the monotonicity cubic p(ρ) = (1−ρ)(26/189 + 4ρ² + 3ρ/8) − 11ρ/14 has p(39/50) ≈ 0.017, nearly zero, and goes negative around ρ ≈ 0.79. Meanwhile the optical deficit L(ε) − A(ε) has slope ≈ −[(1−ε)/2 + q] ≈ −0.75 in ε near ε₀ = 11/50. So shifting the seam by just 1/50 (ε₀: 11/50 → 1/5) multiplies the optical reserve from 3×10⁻⁸ to roughly 1.5×10⁻², **six orders of magnitude**, after which Part V collapses: π < 22/7 everywhere, the quartic terms in A(ε) become unnecessary, and the tuned (N,t)-minimization in the product screen can be replaced by cruder one-line bounds.

The cost is strengthening Part IX near ρ = 0.8, and the audit identified exactly where the slack was discarded: the term Y(1+Y)/(2(1+2Y)²) was crushed to 3ρ/8 via 2π/θ ≥ 4, and the loss integral was majorized generously away from the turning point. Recovering these two discards should buy the ~0.02–0.08 needed for p(ρ) > 0 on [7/51, 4/5], with the Bernstein window widened from [7/15, 14/15] to [√(1/5)·(1−δ), 14/15] — note the current window containment margin is itself hairline (11/50 > 49/225 by 1/450), and this rebalancing fixes that fragility too. Net effect: one harder polynomial certificate in Part IX in exchange for a drastically simpler Part V and the removal of the two most fragile numbers in the whole proof.

### 1.3 Exploit d = 3 fully: elementary half-integer phases (kills the Lorch dependency, compresses Parts I–II)

The single most underused structural asset is that in d = 3 every order is half-integer, so **every radial object is elementary**. Writing j_ℓ, y_ℓ through the manuscript's own P_ℓ-recurrence, one has exactly

$$\theta_{\ell+1/2}(x) = x - \tfrac{(\ell+1)\pi}{2} + \eta_\ell(x),\qquad \tan\text{-representation of }\eta_\ell \text{ rational of degree } \ell \text{ in } 1/x,$$

with η_ℓ(0⁺) = ℓπ/2, η_ℓ(∞) = 0 (the manuscript already uses the ℓ = 0 case θ_{1/2} = x − π/2). Hence the cross-product phase is *exactly*

$$\Psi_{\ell+1/2,\rho}(k) = (1-\rho)k + \eta_\ell(k) - \eta_\ell(\rho k),$$

i.e., the product bound plus an explicit elementary correction. Every ledger row — zero-registry sign, Lorch wall, checkpoint exclusion — is then a monotone trig-rational inequality at a rational point, provable by the same tangent bounds Part I already deploys, but organized once through a single lemma family on η_ℓ instead of ad hoc per-row derivations. Two concrete consequences: **(a)** the ten Lorch walls β_{ℓ,1} become internal one-line statements, removing the last outstanding source-audit item entirely (I verified during the audit that all ten walls hold with comfortable numerical margins, so internalization is guaranteed to succeed); **(b)** Parts I–II should compress substantially, since the 48 Z-rows currently re-derive fragments of the η_ℓ calculus row by row.

Complementary ledger compression: the audit found many KI inventory cells are conservative (e.g., (3,2) at k₈ is listed possible but is actually excluded) and most cap reserves are ≥ 0.3. Restructure as *coarse product-only caps first* — (L+1)² + (h+1)² from the product bound alone — invoking the registry only where the coarse cap fails. I estimate this cuts the registry-dependent rows from ~48 to ~10.

### 1.4 Merge the low-ρ owners into one wedge theorem

The small-hole theorem (ρ ≤ ρ*), the lower-closure wedge (ρ ≤ σ = 3ω₀/4, K > d, ρK > 1/2), and primitive-owner items 3–4 all run the same mechanism: low tails pay interface loss δ ≤ 2√2/15 against first-shelf reserves. Their statements differ only in how the reserve is sourced (per-tail ⌊ω₀K⌋ − n versus the aggregated (1/4)(p − m/2)). A single theorem "N_D ≤ W for all ρ ≤ σ and all K", with the aggregated-reserve scaffold as the official statement (the restatement I already recommended), plus one short mode inventory for the residual pocket {ρ* < ρ ≤ σ, small ρK}, would replace three owners and most of the lower-d table. This also simplifies the complementation algebra: 𝒟₁₆'s lower components disappear from the bookkeeping.

### 1.5 Lower the middle-certificate base curve

Part IX's base curve sits at K = k₁₁(ρ) because the scalar gap S needs K large enough; but ∂_K S was proven positive with visible room (13/1134 + ρ²/3 per unit K above K = 12). If the aggregated certificate is strengthened by injecting a first-shelf reserve (annuli Thm 1.4 applied to the concave head *inside* Part VII's decomposition — currently the certificate uses only the coarse γ < A + 1/4 majorant), the base curve can plausibly drop to k₉ or k₈, deleting the k₉–k₁₁ bands of the ledger (the LOC family, 47 rows, plus the top KI cells). This is quantitative work with a clear success criterion, well-suited to A4.

---

## 2. Alternative architectures

**2.1 The honest big one: FLPS-style verified rational sweep.** The manuscript's ledger + middle certificate exist solely to keep the proof computer-free at a standard *stricter* than the published annuli paper, which closes its own compact residual with a Mathematica sweep (8,473 rational trapezoidal-sum evaluations). The shell proxy P_coarse(ρ,K) = Σ2ν⌊A(ν)+1/4⌋ has exactly the monotonicity structure (non-decreasing in K, non-increasing in ρ via ∂G_K/∂K > 0, the same functions G, H, F) that drives annuli Lemma 8.4. A rectangle-covering sweep of the compact residual {ρ* < ρ < 39/50, L(ρ) < K < U(ρ)} in exact rational arithmetic would replace Parts I–IV *and* possibly VII–IX with ~2 pages plus a script. If the panel accepts the published-annuli verification standard, this is a 60-page reduction; if the purely analytic claim is the point, this becomes the *presentation* recommendation instead: restructure so Tier 1 is the clean analytic proof outside the residual and Tier 2 offers both closure routes, making the heavy ledger optional for readers who accept certified computation.

**2.2 Reduction to 2D annulus Pólya via superposition — fails, instructively.** The scaffold identity is exactly the balls-paper dimension reduction: N₃ = Σ_r 𝒯_r, a superposition of shifted 2D-type counts at half-integer offsets. One hopes to identify each tail with an actual 2D annulus count and cite the published annuli theorem wholesale (Laptev-style). This fails twice over: the shell's radial operators sit at *half-integer* orders — spectrally, the flux-½ Aharonov–Bohm annulus, for which Pólya is published only for the disk (FLPS 2024, J. Spectr. Theory), not annuli — and the tails Σ_{ℓ≥r} are order-truncated counts that are not the counting function of any domain. The interlacing q_{ℓ,n}(2D, m=ℓ+1) ≤ q(shell, ℓ) ≤ q(2D, m=ℓ) is clean but cannot control linearly-weighted sums with the right constant. Worth recording as a checked dead end; the AB-annulus Pólya conjecture is, however, a natural companion obligation if anyone wants a citable superposition route in the future.

**2.3 Thin shells via thin-product technology.** He–Wang (arXiv:2402.12093) prove Pólya for thin Euclidean products Ω×(0,ε); the thin shell is a warped product with curvature corrections that are precisely the manuscript's radial-deficit analysis. Adapting the thin-product argument to the warped metric might yield a thin-shell theorem with an explicit ε-threshold, potentially replacing both optical screens with one comparison. Research-grade, not drop-in; assign a literature pass. Same for GJWY (Adv. Math. 484 (2026) 110715, "Bessel functions and Weyl's law for balls and spherical shells"): their two-term asymptotics cannot give an all-Λ statement (remainders ineffective/non-uniform, as FLPS themselves note for annuli), but they set up the identical multiplicity-weighted lattice count and may contain importable lemmas — A1 should read it against Parts VII–VIII.

---

## 3. Negative results worth recording (so we stop re-deriving them)

**Heat-kernel / Berezin–Li–Yau / Chernoff bounds cannot close any region at this precision.** I tested the sharpest cheap version on the hardest low-K cell (ρ = ρ_c, K ≈ z_ρ): N ≤ e^{tK²}·θ(tz²)·Z_{S²}(t) optimized over t gives ≈ 3.7 against W ≈ 3.17 — the intrinsic factor-e (or (1+2/d)^{d/2} for Riesz–Legendre) loss is fatal against a sharp-constant target. The mode-inventory character of the low-K region is intrinsic to *any* approach; simplification means shrinking that region from above (§1.5) and compressing its bookkeeping (§1.3), never replacing it with spectral-function bounds. **Plain ball monotonicity** N(shell) ≤ N(ball) < W_ball can never produce the (1−ρ³) factor; even with the published two-term ball improvements it covers only ρ ≲ K^{−1/3}, which is not one of the missing regions. **Neumann bracketing** upper bounds need Neumann Pólya for the pieces — open in 3D. **The pure product/cylinder comparison** (the 3D analogue of annuli Region II, which I verified is exactly the manuscript's product bound) overcounts by the factor 3/(1+ρ+ρ²), sharp only at ρ = 1 — which is *why* the thin-shell regime needs the discreteness accounting of the optical screens and why no soft comparison can extend it downward.

---

## 4. Proposed obligations

In protocol terms: **SIMP-CONVENTION** (non-strict count rewrite; open, trivial, high leverage), **SIMP-SEAM-SHIFT** (strengthen Part IX to ρ = 4/5, detune Part V; open, assign A2/A4 jointly — I can supply the recovered-term inequalities, A4 the new Bernstein certificate), **SIMP-ELEMENTARY-PHASE** (η_ℓ calculus; kills SRC-LORCH-1993 as a side effect; open), **SIMP-OWNER-MERGE** (wedge unification; open), **SIMP-BASE-CURVE** (k₁₁ → k₉ feasibility; diagnostic first), **ALT-RATIONAL-SWEEP** (proposed; decision needed from the human on the verification standard), **LIT-GJWY-HEWANG** (assign A1). My ranking by (benefit)/(risk to a currently gap-free proof): 1.1 > 1.2 > 1.3 > 1.4 ≈ 1.5 > 2.1 (standard-dependent) > 2.3.

**Confidence:** high (~0.9) that 1.1 and 1.3 are pure wins with no hidden cost, since both were stress-checked against the audited payment structure; moderate (~0.6) that the seam shift to 4/5 closes with the identified discarded terms alone — if it stalls at 0.79, even a seam at 79/100 already buys four orders of magnitude of optical margin.