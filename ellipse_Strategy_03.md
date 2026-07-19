# A2 Strategy Memo — Dirichlet Pólya for the Ellipse

*Role: analytic proof-surgeon / conservative referee. This memo sharpens the repo's Phase 4–5 skeleton (`Strategy.md`) into an auditable obligation graph, repairs two overbroad claims into checkable lemmas, and records the true crux. No statement below is promoted to **proved** for the ellipse.*

Throughout I use the repo conventions from `polya_conjecture.md`: strict open counting
$$N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},\qquad L_2=\frac{\omega_2}{(2\pi)^2}=\frac{1}{4\pi}.$$

**Target.** For $E_{a,b}=\{x^2/a^2+y^2/b^2<1\}$, $a\ge b>0$, $|E_{a,b}|=\pi ab$:
$$
\boxed{\,N_D(E_{a,b},\Lambda)\le \frac{ab}{4}\,\Lambda\quad(\forall\Lambda\ge0)\,}
\qquad\Longleftrightarrow\qquad \lambda_k^D(E_{a,b})\ge \frac{4k}{ab}.
$$
By scale invariance fix $c^2:=a^2-b^2$ and parametrize by eccentricity $e=c/a\in[0,1)$; area-normalize when comparing across $e$.

---

## 1. Exact reduction to Mathieu phase-counting

This is the analog of the disk's Bessel-zero correspondence and must be nailed down *before* any estimate is used as a dependency.

### 1.1 Separation and quantization — Lemma R1

Elliptic coordinates $x=c\cosh\mu\cos\nu$, $y=c\sinh\mu\sin\nu$, $\mu\in[0,\mu_0]$, $\nu\in[0,2\pi)$, with boundary
$$\cosh\mu_0=\tfrac{a}{c},\quad \sinh\mu_0=\tfrac{b}{c},\quad \mu_0=\operatorname{arctanh}(b/a).$$
Writing $u=R(\mu)\Phi(\nu)$, the Helmholtz equation $-\Delta u=\Lambda u$ separates with **spectral-slaved coupling parameter**
$$q=\frac{c^2\Lambda}{4}\;\ge 0$$
into the **angular Mathieu** and **radial modified-Mathieu** equations
$$\Phi''+(\alpha-2q\cos2\nu)\Phi=0,\qquad R''-(\alpha-2q\cosh2\mu)R=0 .$$
$2\pi$-periodicity selects $\alpha\in\{a_m(q)\}_{m\ge0}$ (even, $ce_m$) or $\alpha\in\{b_m(q)\}_{m\ge1}$ (odd, $se_m$). Regularity on the interfocal segment $\mu=0$ selects the modified-Mathieu functions of the first kind $\mathrm{Ce}_m(\cdot,q),\ \mathrm{Se}_m(\cdot,q)$ (the $J_m$-analogs). Dirichlet quantization:
$$\mathrm{Ce}_m(\mu_0,q)=0\ \ (\text{even mode }m\ge0),\qquad \mathrm{Se}_m(\mu_0,q)=0\ \ (\text{odd mode }m\ge1).$$

**Status.** *Classical* (Morse–Feshbach / McLachlan / DLMF §28.20–28.32). **Confidence: very high.**
**Dependency cards required before use:**
- (D-completeness) The product eigenfunctions $\{\mathrm{Ce}_m\!\cdot ce_m,\ \mathrm{Se}_m\!\cdot se_m\}$ are a *complete* orthonormal system for the Dirichlet Laplacian on $E_{a,b}$ — i.e. separation captures **all** eigenvalues with correct multiplicity, none missed, none spurious. This is standard but is a genuine external theorem, not an automatic consequence of producing separated solutions.
- (D-transversality) For fixed mode label, $q\mapsto \mathrm{Ce}_m(\mu_0,q)$ has only *simple, transversal* zeros, each in bijection with one eigenvalue branch. Needs a Sturm/oscillation argument (see §4).

### 1.2 The counting identity — Lemma R2

Define the radial oscillation (Prüfer/phase) count. By Sturm theory, at energy $\Lambda$ the number of zeros of the regular radial solution in $(0,\mu_0)$ equals the accumulated phase, so
$$
N^{ce}_m(\Lambda)=\#\{\text{Dirichlet even eigenvalues }\le\Lambda\text{ in mode }m\}
=\Big\lfloor \tfrac1\pi\,\Theta^{ce}_m(\mu_0;q(\Lambda))+\varkappa^{ce}_m\Big\rfloor,
$$
with the analogous $N^{se}_m$, where $\Theta$ is the *exact* modified-Mathieu phase (defined via the Milne amplitude–phase pair of $\mathrm{Ce}_m,\mathrm{Mc}^{(2)}_m$) and $\varkappa$ is a fixed **Maslov/regularity constant** collecting the segment behavior at $\mu=0$. Then
$$
\boxed{\,N_D(E_{a,b},\Lambda)=\sum_{m\ge0}N^{ce}_m(\Lambda)+\sum_{m\ge1}N^{se}_m(\Lambda)\,}.
$$

**Status.** *Conditional* on R1 + (D-transversality). **Confidence: high** for the identity's *form*; **the constants $\varkappa$ are a gap** (§4, O4).

**This is the structural payoff and it is better than the repo's framing.** The problem is *not* a free two-parameter $(\alpha,q)$ lattice. It is a **single-parameter family of 1-D phase problems** indexed by the mode label: $\alpha$ is slaved to the mode ($=a_m(q)$ or $b_m(q)$) and $q$ is slaved to $\Lambda$. The count is a **sum of one-dimensional floor functions in the single variable $q$** — exactly the disk architecture. The only genuinely two-parameter feature is that each mode's phase $\Theta_m(\cdot;q)$ depends on a characteristic value $a_m(q)$ that *itself drifts with $q$*. That drift is the whole difficulty; it is not a lattice-dimension increase.

### 1.3 Multiplicity split and the disk limit (grid geometry)

| | Disk (radius $R$) | Ellipse $E_{a,b}$ |
|---|---|---|
| Mode label | $m\ge0$ | $ce_m$ ($m\ge0$) **and** $se_m$ ($m\ge1$) |
| Multiplicity | $2$ for $m\ge1$, $1$ for $m=0$ | generically $1$ each |
| Quantizer | $J_m(\sqrt\Lambda R)=0$ | $\mathrm{Ce}_m(\mu_0,q)=0$ / $\mathrm{Se}_m(\mu_0,q)=0$ |

**Verified disk limit (auditable).** As $c\to0$ with $r:=c\cosh\mu\to\tfrac{c}{2}e^\mu$ fixed, $q=c^2\Lambda/4$, $\alpha\to m^2$, the substitution $\tfrac{d}{d\mu}=r\tfrac{d}{dr}$ turns the radial equation into
$$r^2R_{rr}+rR_r+(\Lambda r^2-m^2)R=0,$$
i.e. **Bessel of order $m$, argument $\sqrt\Lambda\,r$**. So $\mathrm{Ce}_m,\mathrm{Se}_m\to J_m$ and the ellipse's split pair $(a_m,b_m)$ coalesces into the disk's doubly-degenerate eigenvalue. **Consequence:** $q\to0$ is a *regular* limit in this scaling — the near-circular regime is a genuine perturbation of the FLPS disk proof (relevant to §6). **Confidence: very high** (direct computation).

**Weyl consistency check (must be audited by A4).** The separated action integrals compute the classical phase-space volume
$$\frac{1}{(2\pi)^2}\operatorname{Vol}\{(x,\xi):|\xi|^2\le\Lambda,\ x\in E\}=\frac{|E|\,\Lambda}{4\pi}=\frac{ab}{4}\Lambda,$$
so the leading term is automatically correct. Pólya is the statement that the **discrete floor-sum in R2 never overshoots this volume**, at *every* $\Lambda$ — not asymptotically.

---

## 2. Anatomy of the obstruction

What transfers from FLPS, and what does not:

- **Transfers (in principle):** the spectral→floor-sum reduction (R1–R2); the strategy of *analytic high-energy bound + certified finite window*; Sturm oscillation counting.
- **Does not transfer for free:**
  1. **Bessel-zero inequalities have no Mathieu analog at the required rigor.** FLPS leans on sharp, *certified*, uniform-in-order bounds for $j_{m,n}$ and the Bessel phase (McMahon, Olver, monotonicity/convexity of $m\mapsto j_{m,n}$). The corresponding statements for $\mathrm{Ce}_m,\mathrm{Se}_m,a_m(q),b_m(q)$ — uniform in order **and** in $q$ **and** across the turning point, with two-sided error control — are **not available in the literature**. This is the rate-limiting external input, consistent with the repo's own diagnosis (Phase 5.1).
  2. **The characteristic-value drift $a_m(q)$.** In the disk the "grid line" for mode $m$ is straight (order fixed). Here the effective transverse quantum number moves with energy, warping the counting curve.
  3. **The true crux is sign-definiteness of the pointwise excess, not a two-term asymptotic.** Weyl-with-remainder gives $N-\tfrac{ab}{4}\Lambda=-\tfrac{|\partial E|}{4\pi}\sqrt\Lambda+o(\sqrt\Lambda)$ (perimeter $|\partial E|$ = complete elliptic integral $4aE(e)$). The *negative* second term is why Pólya is even plausible. But Pólya demands the excess $\le0$ **at every energy including the low staircase**, which requires converting an asymptotic sign into an *exact integer inequality*. FLPS achieve this by exploiting exact Bessel-zero convexity; the ellipse needs an exact-inequality substitute. **This, not the two-parameter bookkeeping, is where a proof will live or die.**

---

## 3. Recorded dead-ends and one overclaim repair

### 3.1 Domain-monotonicity sandwich — **fails, quantified**

$B_b\subset E_{a,b}\subset B_a$ gives $N_{B_b}\le N_{E}\le N_{B_a}$. Disk Pólya gives $N_{B_a}(\Lambda)\le\frac{a^2}{4}\Lambda$, but the target is $\frac{ab}{4}\Lambda$. Since $a>b$, the sandwich overshoots by the multiplicative factor $a/b=1/\sqrt{1-e^2}$, which $\to\infty$ as $e\to1$. **Monotonicity alone can never prove ellipse Pólya.** (Record in `gap_register.md` as a closed negative result — it certifies that the Mathieu machinery is genuinely necessary.)

### 3.2 "Near-circular = perturbation only" — **overbroad; repair**

`Strategy.md` Phase 4 proposes $\lambda_j(E_e)=\lambda_j(D)+e^2a_j+O(e^4)$ and certification over an eccentricity grid. **Hidden gap:** this expansion is uniform in $e$ only for *fixed* $j$. The shape-derivative coefficients $a_j$ and the $O(e^4)$ constant grow with $j$ (the $j$-th eigenfunction's boundary sensitivity grows), so **for any fixed $e>0$ the high-energy tail $\Lambda\to\infty$ escapes perturbation theory.** A perturbative argument therefore *cannot* close Pólya for all $\Lambda$, even at small $e$.

**Repair (checkable lemma structure).** Split at a *mode-dependent* threshold, not an energy-independent one:
$$
N_D(E_e,\Lambda)=\underbrace{\sum_{\text{modes with }q\le q_\star}(\cdots)}_{\text{finite window: perturbation + certified numerics}}+\underbrace{\sum_{\text{modes with }q> q_\star}(\cdots)}_{\text{high-energy: Mathieu phase enclosure at small }q}.
$$
So Phase 4 **secretly requires the Phase 5 high-energy machinery, restricted to a neighborhood of $q=0$.** The good news (from §1.3): near $q=0$ the modified-Mathieu phase is a controlled perturbation of the Bessel phase, so the small-$q$ enclosure should inherit FLPS constants with an $O(q)$ correction — plausibly the *easiest* corner of the full analytic problem. Phase 4 is real and worthwhile, but it is "FLPS + small-$q$ Mathieu correction + finite window," **not** "perturbation theory."

---

## 4. Regime decomposition and analytic obligations

For mode with characteristic value $\alpha$, the radial coefficient is $2q\cosh2\mu-\alpha$. Turning point $\mu_t$: $\cosh2\mu_t=\alpha/(2q)$ (real iff $\alpha>2q$). At the boundary, using $\cosh2\mu_0=(a^2+b^2)/c^2$,
$$2q\cosh2\mu_0=\frac{(a^2+b^2)\Lambda}{2},$$
so a mode is **oscillatory at the wall** iff $\alpha<\tfrac{(a^2+b^2)\Lambda}{2}$.

- **O1 — Oscillatory phase enclosure** ($\mu_t<\mu<\mu_0$). Establish
 $$\Theta_m(\mu_0;q)=\int_{\mu_t}^{\mu_0}\sqrt{2q\cosh2\mu-\alpha}\,d\mu+\text{(explicit correction)}$$
 with *certified two-sided error* uniform in $(m,q,e)$. Liouville–Green with quantitative remainder; the drift $\alpha=a_m(q)$ enters parametrically. **Gap: uniform-in-$q$ error bound missing.**
- **O2 — Turning-point (Airy) uniformization.** Near $\mu_t$, an Olver-type Airy expansion for modified Mathieu with sign-controlled remainder. **This is the least-developed input**; DLMF/Wong give asymptotics but not the certified uniform enclosures needed. Publishable in isolation (repo Phase 5.1).
- **O3 — Evanescent control** ($0<\mu<\mu_t$). Show the regular solution is nonvanishing and log-monotone there (no zeros below the turning point) with exponential lower bounds — needed so that the phase count is exactly the oscillatory contribution.
- **O4 — Interfocal/Maslov constant $\varkappa$.** Pin down the *exact* small-$\mu$ connection at the segment and the resulting fixed offset in R2. Because Pólya is a sharp **integer** inequality, an off-by-one in $\varkappa$ is fatal. This must be proven exactly (not fitted numerically), separately for even/odd classes and for the $m=0$ special case.
- **O5 — Characteristic-value envelopes.** Certified two-sided bounds $a_m^\pm(q)$, $b_m^\pm(q)$ uniform in $q$, plus **monotonicity/interlacing** ($a_0<b_1\le a_1<b_2\le\cdots$, strict for $q>0$; $a_m(0)=b_m(0)=m^2$) and the sign of $\partial_q a_m$. Continued-fraction / tridiagonal recurrence with validated Newton. This feeds both the phase (O1) and the lattice geometry (§5).
- **O6 — Branch monotonicity / Sturm transversality** (backs D-transversality). Prove $q\mapsto\mathrm{Ce}_m(\mu_0,q)$ crosses zero simply and that eigenvalue branches are strictly increasing in the mode's radial index, so the floor-sum in R2 is exact.

---

## 5. The lattice-counting crux

With O1–O5, Pólya reduces to a **floor-sum inequality**:
$$
\sum_{\text{modes}}\Big\lfloor\tfrac1\pi\Theta_{\text{mode}}(\mu_0;q(\Lambda))+\varkappa\Big\rfloor\ \le\ \frac{ab}{4}\Lambda=\sum_{\text{modes}}\tfrac1\pi\Theta_{\text{mode}}+\text{(area remainder)}.
$$
Two mechanisms must combine with the correct sign:

1. **Rounding** $\lfloor x\rfloor\le x$ gives the leading term for free but must not be swamped by the accumulated fractional parts $\sum_{\text{modes}}\{\cdots\}$.
2. **Curve convexity.** The number of lattice points under the mode-vs-radial-index counting curve is controlled by an Euler–Maclaurin / trapezoidal-floor estimate whose error sign is fixed by the **convexity of the phase curve** $m\mapsto \Theta_m(\mu_0;q)$ (equivalently of the inverse "eigenvalue-in-mode" curve). 

**Key obligation O7 (decisive).** Determine the convexity/concavity of the Mathieu phase-counting curve, uniformly in $e$. If it is *concave* in the FLPS-favorable sense, the trapezoidal-floor estimate yields excess $\le -\,c\,\sqrt\Lambda$ matching the negative perimeter term, and Pólya closes. If it is convex, the boundary correction flips sign and Pólya must be rescued entirely by the second-term budget — a much more delicate accounting. In the disk this is exactly the role of Bessel-zero convexity; **the ellipse analog is open and is the single highest-value analytic target.** Note the disk limit (§1.3) forces the leading convexity to *agree* with Bessel at $q=0$, which is a strong prior that the favorable sign persists for small $q$ — but not a proof for all $e$.

**Second-term audit O8.** Make the negative correction explicit and *uniform*: the effective boundary budget is $\sim\frac{|\partial E|}{4\pi}\sqrt\Lambda=\frac{aE(e)}{\pi}\sqrt\Lambda$. Confirm it dominates all positive rounding/curvature contributions above threshold, with constants tracked in $e$.

---

## 6. Eccentricity uniformity and endpoints

- **$e\to0$ (disk corner, $q\to0$): regular, tractable.** By §1.3 the whole apparatus degenerates smoothly to FLPS. Obligation: show all constants in O1–O7 are $C_{\text{disk}}+O(q)$, giving Pólya on a full neighborhood $e\in[0,e_0]$ by inheriting the disk sign. **This is Phase 4, correctly stated.** **Confidence: moderate–high** *conditional on O2* (turning-point uniformity is still needed even at small $q$, for high modes where $\alpha\sim m^2\gg q$).
- **$e\to1$ (needle corner, $q\to\infty$, $\mu_0\to0$): genuinely singular.** The domain collapses to a segment; both sides of Pólya $\to0$ and their ratio is delicate. The turning-point/segment structure degenerates ($\mu_t,\mu_0\to0$ together), so any bound relying on $\mu_0$ bounded below **breaks**. Likely needs a *separate thin-domain analysis* (adiabatic/1-D reduction transverse to the segment) rather than the uniform enclosure. **Confidence: low.** Flag as the principal uniformity risk; consider proving $[0,e_0]$ and $[e_1,1)$ by different methods and closing the middle by the certified window.

---

## 7. Certified finite-window closure over a **2-D** region

Unlike the disk (one domain), ellipse Pólya must certify a compact region in $(\Lambda,e)$:
$$\{\,0\le\Lambda\le\Lambda_0(e),\ e\in[e_-,e_+]\,\}.$$
Obligations:
- **C1** Validated evaluation of $a_m(q),b_m(q)$ (interval arithmetic on the tridiagonal recurrence / continued fractions) with rigorous error.
- **C2** Certified zero enclosures of $\mathrm{Ce}_m(\mu_0,q),\mathrm{Se}_m(\mu_0,q)$ in $q$ (validated Newton–Kantorovich / Moler–Payne, or MPS with a-posteriori bounds — repo Phase 5.4).
- **C3** **Lipschitz-in-$e$ control** so a finite $e$-grid certifies the continuum: bound $|\partial_e\lambda_k|$ (Hadamard shape derivative) uniformly on the window, then interval-cover $e$. Without C3 the window is only sampled, and **sampling is not proof** (repo Non-Claim Rule; do not let numerics masquerade as certification).
- **C4** Match the analytic threshold: prove $\Lambda\ge\Lambda_0(e)\Rightarrow$ Pólya from §5, with $\Lambda_0(e)$ *explicit and integrable against the $e$-cover*, especially as $e\to1$ where $\Lambda_0$ may blow up.

---

## 8. Neumann note (kept separate)

Neumann Pólya is the *reverse* inequality $N_N\ge\frac{ab}{4}\Lambda$, quantized by $\partial_\mu\mathrm{Ce}_m(\mu_0,q)=0$ (and $\partial_\mu\mathrm{Se}_m$), with the extra zero mode $\lambda_0^N=0$. The reversed inequality means the floor-sum sign requirements *flip*, so O7's favorable-convexity direction is the opposite one; Filonov's convex-Neumann result is (per the repo's flagged disagreement) a **non-sharp** lower bound and does **not** settle it. Recommend: **do not couple** the Neumann track to the Dirichlet proof; treat it as a parallel obligation set once O1–O5 exist.

---

## 9. Ranked obligation register

| ID | Obligation | Type | Depends on | Risk | Confidence it holds |
|---|---|---|---|---|---|
| R1 | Separation + quantization | reduction | D-completeness, O6 | low | very high |
| R2 | Floor-sum counting identity | reduction | R1, O4, O6 | low–med | high (form); gap (const) |
| **O7** | **Phase-curve convexity sign, uniform in $e$** | **analytic** | **O1,O2,O5** | **high** | **open — decisive** |
| O2 | Certified Airy turning-point enclosure | special-fn | O5 | high | open (literature gap) |
| O1 | Oscillatory phase enclosure, uniform in $q$ | special-fn | O5 | med–high | plausible |
| O5 | Certified $a_m(q),b_m(q)$ envelopes + monotonicity | special-fn | — | med | high |
| O4 | Exact Maslov/segment constant $\varkappa$ | analytic | R1 | med (fatal if wrong) | plausible |
| O8 | Uniform negative second-term budget | analytic | O1,O2,O7 | med | plausible |
| §6b | $e\to1$ thin-domain uniformity | analytic | separate method | high | low |
| §6a | $e\to0$ neighborhood (Phase 4) | analytic | O1,O2,O5 (small $q$) | med | moderate–high |
| C1–C4 | Certified 2-D $(\Lambda,e)$ window incl. Lipschitz-$e$ | computation | O5 | med (engineering) | high if resourced |
| D-comp | Completeness of Mathieu eigenfunctions | source card | — | low | very high |

**Overall assessment.** Ellipse Dirichlet Pólya is a realistic **multi-paper** program. The reduction (R1–R2) is essentially classical and high-confidence. The bottleneck is **not** the two-parameter bookkeeping (which collapses to a 1-parameter family of 1-D phase problems, §1.3) but (i) the **missing certified uniform Mathieu turning-point analysis** (O2) and (ii) the **undetermined sign of the phase-curve convexity** (O7), which together decide whether the FLPS floor-sum mechanism reproduces here. The $e\to1$ corner is a distinct, genuinely singular risk. I would **not** endorse any "near-circular" theorem framed as perturbation theory (§3.2) — it must be stated as FLPS-plus-small-$q$-correction-plus-certified-window.

---

## 10. Concrete next steps and division of labor

1. **A2 (me) + A4 — Mathieu-enclosure paper (O5 → O1 → O2).** Start with O5 (certified $a_m(q),b_m(q)$ via validated continued fractions), since it is self-contained, publishable, and unblocks everything. Then O1, then the hard O2. Deliverable card: "uniform two-sided modified-Mathieu phase enclosures with certified error," explicitly as functions of $(m,q,e)$.
2. **A1 — source cards** for: FLPS disk (exact statement of the Bessel-zero convexity lemma they use), the annulus lattice-counting lemma, Mathieu completeness (D-completeness), and Meixner–Schäfke/DLMF §28 asymptotics. We need the *precise* FLPS convexity statement to know what O7 must replicate.
3. **A3 — obstruction pass on O7 and §6b.** Independently attempt to *disprove* favorable convexity of the Mathieu phase curve for moderate $e$, and stress-test the $e\to1$ corner. If O7's sign fails anywhere, the program pivots to the second-term-budget route (O8) early.
4. **A4 — Weyl-constant audit** of the separated action integrals ($=\frac{ab}{4}\Lambda$) and a **diagnostic-only** numerical scan of $N_D(E_e,\Lambda)-\frac{ab}{4}\Lambda$ across $(\Lambda,e)$ to locate the tightest energies (guides where $\Lambda_0(e)$ and the finite window must be sharp). Label explicitly as non-certifying.
5. **Immediate exact task (O4):** compute the interfocal connection constant $\varkappa$ in closed form for even/odd/$m{=}0$ classes — cheap, decisive for R2's integer accounting, and a good early correctness gate.

*Nothing here should be entered into `proof_obligations.yml` above **conditional/plausible** status. O7 and O2 are the gates; until both are closed with certified errors, no ellipse Pólya statement — near-circular or full — may be promoted.*