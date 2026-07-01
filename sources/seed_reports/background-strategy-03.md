# Strategic note: Dirichlet Pólya for ellipses and convex domains

This note summarizes the current landscape around the ellipse and convex-domain versions of Pólya’s conjecture. The main point is that the natural open flagship is the **Dirichlet** ellipse problem: the Neumann planar convex direction is treated here as closed by Filonov’s 2025 result, while the Dirichlet side still requires the hard analytic–lattice machinery.

## A crucial reframing before anything else

The target "ellipse, convex bodies" needs a sharper split. That split identifies where the open problem lives:

- **Neumann Pólya for *all* planar convex domains is already a theorem** — Filonov, *On the Pólya conjecture for the Neumann problem in planar convex domains*, CPAM 78(3):537–544 (2025). The ellipse is convex, so **Neumann Pólya for the ellipse is done.**
- Therefore the open flagship is specifically the **Dirichlet upper bound for the ellipse**, then **Dirichlet Pólya for general planar convex domains**, then **convex bodies in $\mathbb{R}^d$, $d\ge 3$** (where even the Neumann side is open beyond balls/cylinders/shells).

So the project is not "Pólya for the ellipse" generically: it is the **Dirichlet** ellipse and the **Dirichlet** convex case. That distinction determines which machinery applies.

---

## 1. Problem setting

For a bounded domain $\Omega\subset\mathbb{R}^d$, let $N^D_\Omega(\lambda)=\#\{k:\lambda_k^D\le\lambda\}$ and $N^N_\Omega(\lambda)=\#\{k:\lambda_k^N\le\lambda\}$ be the Dirichlet and Neumann counting functions, and let
$$
w_\Omega(\lambda)=(2\pi)^{-d}\,\omega_d\,|\Omega|\,\lambda^{d/2},\qquad \omega_d=\frac{\pi^{d/2}}{\Gamma(\tfrac d2+1)},
$$
be the leading Weyl term. **Pólya's conjecture (1954):**
$$
N^D_\Omega(\lambda)\;\le\;w_\Omega(\lambda)\qquad\text{and}\qquad N^N_\Omega(\lambda)\;\ge\;w_\Omega(\lambda)\qquad\text{for all }\lambda>0.
$$

Two structural points are used constantly:

**Dual (eigenvalue) form.** Pólya is equivalent to the pointwise eigenvalue bounds
$$
\lambda_k^D(\Omega)\;\ge\;\frac{4\pi^2}{(\omega_d|\Omega|)^{2/d}}\,k^{2/d},\qquad \lambda_k^N(\Omega)\;\le\;\frac{4\pi^2}{(\omega_d|\Omega|)^{2/d}}\,k^{2/d}.
$$
The Berezin–Li–Yau and Kröger inequalities are the *averaged* (Riesz-mean / Cesàro) versions of exactly these, with the sharp Weyl constant but only on average — they give $\frac1k\sum_{j\le k}\lambda_j^D\ge \frac{d}{d+2}\cdot(\text{Pólya RHS})$. Pólya is the un-averaged, pointwise statement, which is strictly stronger and is what remains open.

**The Dirichlet/Neumann asymmetry.** The two halves are genuinely different problems. The Dirichlet half is an *upper* bound on a counting function, so one must show that eigenvalues do not accumulate too fast; the Neumann half is a *lower* bound, so eigenvalues must accumulate fast enough. Filonov's classical interlacing $\lambda_{k+1}^N(\Omega)<\lambda_k^D(\Omega)$ (2004) links them but closes neither. The recent pattern is that the **Neumann** side has proven more amenable on convex domains (Filonov 2025), while the **Dirichlet** side is where the hard lattice-counting lives — which is why the ellipse-Dirichlet problem is the real frontier.

**Why this is not "soft."** The Pólya inequality fails for the Dirichlet Laplacian with a constant magnetic field (Landau/Aharonov–Bohm setting): the Weyl term is unchanged but Landau-level degeneracy destroys the bound. Any proof must therefore exploit genuine structure of the Euclidean Laplacian, not just Weyl asymptotics — this rules out purely abstract approaches and is the reason the problem is hard.

---

## 2. Background and recent progress

**Classical era.** Pólya proved both inequalities for **tiling domains** (Dirichlet 1961; the Neumann tiling case is Kellner 1966), using translation invariance and Fourier modes. For ~60 years no non-tiling planar domain was settled. The averaged surrogates arrived via Berezin (1972), Li–Yau (1983) for Dirichlet, Kröger (1994) for Neumann, with geometric refinements by Geisinger–Laptev–Weidl (2011). Laptev (1997) gave the single most useful soft tool: **if $\Omega_1$ satisfies Dirichlet Pólya, so does $\Omega_1\times\Omega_2$ for any $\Omega_2$** (a Riesz-mean argument), which is how product/strip domains get settled.

**The FLPS breakthrough (2023–).** Filonov–Levitin–Polterovich–Sher, *Pólya's conjecture for Euclidean balls* (Invent. Math. 234, 2023), proved:
- the **disk** (Dirichlet **and** Neumann) — first non-tiling planar domain ever;
- **arbitrary planar sectors** (both);
- **balls in all dimensions** (Dirichlet).

The supporting technical paper, *Uniform enclosures for the phase and zeros of Bessel functions and their derivatives* (SIAM J. Math. Anal. 56(6):7644–7682, 2024), is the backbone — it's the piece you'd most directly need an analog of.

**The cascade since (this is the active frontier — most are 2024–2026):**

| Result | Who | Status |
|---|---|---|
| Dirichlet **annuli** + two-term disk bound | FLPS, arXiv:2505.21737 | JLMS 113:2 e70425 (2026) |
| Dirichlet **spherical shells**, Weyl law for balls/shells | Guo–Jiang–Wang–Yang, arXiv:2412.14059 | to appear, Adv. Math. |
| **Neumann, all planar convex domains** | Filonov | CPAM 78(3), 2025 |
| Improvements for disks/balls; **Neumann cylinders in $\mathbb{R}^3$**; extends non-computer-assisted regime | J. Guo, arXiv:2511.17050 | preprint (Nov 2025) |
| **Thin products** | He–Wang, arXiv:2402.12093 | preprint |
| $\varepsilon$-loss Pólya for **all Lipschitz domains** reduced to a finite computation; strip-tiling domains *beat* Pólya | Jiang–Lin, arXiv:2507.04307 | preprint (2025) |
| Improved **Berezin–Li–Yau & Kröger** (resolves Weidl's 2006 question); **infinitely many** Dirichlet eigenvalues satisfy Pólya for *any* bounded domain | Jiang–Lin, arXiv:2507.20330 | preprint (2025) |
| Riesz-means asymptotics & semiclassical inequalities, Dirichlet/Neumann **convex/Lipschitz** | Frank–Larson, arXiv:2407.11808, 2410.04769 | preprints |
| Optimal unions of scaled copies; non-tiling families | Freitas–Lagacé–Payette (Ark. Mat. 2021); Freitas–Salavessa (JMP 2023) | published |

**Net state of play for the target:**
- **Established:** tiling domains, disk, sectors, Dirichlet balls/shells, Dirichlet annuli, Neumann **all planar convex**, Neumann $\mathbb{R}^3$ cylinders, and product/strip/thin families.
- **Open:** **Dirichlet ellipse** to **Dirichlet general planar convex** to **convex bodies in $\mathbb{R}^d$ ($d\ge3$), both boundary conditions** to full Neumann Pólya in higher dimensions.
- **Reduction in hand:** Jiang–Lin make the $\varepsilon$-loss Dirichlet case a *finite computation* for any Lipschitz domain. Removing the $\varepsilon$ is the gap.

Crucially, **no one has yet attacked the ellipse with the FLPS machinery** — the obstruction (next section) is that the ellipse is not Bessel-separable. This is genuinely unclaimed territory with a clear (hard) path.

---

## 3. The FLPS machine, dissected (what you'd be extending)

The disk proof has four stages. Understanding each stage clarifies precisely what breaks for the ellipse.

**(i) Exact spectral-to-lattice correspondence.** Disk Dirichlet eigenvalues are $j_{n,k}^2$ (squared Bessel zeros), so $N^D(\lambda)=\#\{(n,k):j_{n,k}\le\sqrt\lambda\}$ with multiplicity 2 for $n\ge1$. The novel ingredient (Sher's observation) is that, via the **Bessel phase function** $\beta_n$ (the monotone function with $\beta_n(j_{n,k})=k\pi$-type values), this count equals a **weighted lattice-point count under an explicit curve — exactly, not just asymptotically.** The whole problem becomes: count integer points under a curve $y=f(x)$ defined through the inverse Bessel phase, and compare to the area (= Weyl term).

**(ii) Uniform two-sided phase enclosures.** To make (i) rigorous, the curve must be pinned between explicit elementary functions, uniformly in order $n$ and argument. This is the entire content of the SIAM 2024 paper: Olver-type uniform asymptotics for $J_\nu$, its zeros, and its phase, with *certified* error bounds.

**(iii) Lattice counting under convex/concave curves.** The combinatorial core: FLPS Theorem 5.1 bounds the number of lattice points under a non-negative decreasing **convex** curve with Lipschitz constant $\le \tfrac12$. The annulus paper's main new technical contribution is extending this to **concave** curves and **relaxing the Lipschitz-$\tfrac12$ restriction**, via "trapezoidal floor sum" estimates. This is a reusable ingredient for the ellipse program.

**(iv) Computer-assisted endgame.** The asymptotic estimates cover $\lambda$ outside a bounded window; inside it, a rigorous algorithm obeying two principles closes the gap — **(P1)** terminates in finitely many steps, **(P2)** uses only integer/rational arithmetic (interval/ball arithmetic, no floating point). The papers ship with published verification scripts.

---

## 4. Solving strategy

Stage the program by tractability, treating the early targets as real publications that build the toolkit for the prize. Honest framing: Targets 0–1 are tractable paper-sized projects, Target 2 (the ellipse) is the hard flagship with a concrete path, and Target 3 is the deeper convex-domain prize.

**Target 0 — warm-up, weeks not years (build fluency + a quick paper).** Reproduce and *extend the non-computer-assisted regime* in the spirit of Guo (2511.17050): sharpen the two-term Dirichlet disk/ball bounds, or push the analytic window for a case where the computer-assisted part currently dominates. This is a low-risk way to internalize stages (ii)–(iv) on machinery that already works.

**Target 1 — a new *separable* domain (tractable, genuinely new).** The FLPS method ports to any domain whose spectrum separates into special-function roots with a uniform large-parameter asymptotic theory:
- **Ellipsoids of revolution / elliptic cylinders / spheroidal domains** → **spheroidal wave functions**, which (unlike general Mathieu) have a well-developed uniform asymptotic theory (Dunster). This is the closest unclaimed analog of "balls/shells."
- This is the right intermediate step: it forces the project to build certified enclosures for a *two-parameter* special function (the separation constant couples the two ODEs), which is exactly the skill the ellipse demands, but in a setting with better existing asymptotics.

**Target 2 — the flagship: Dirichlet Pólya for the ellipse.** The ellipse separates in elliptic coordinates into the **angular Mathieu equation** ($\mathrm{ce}_n,\mathrm{se}_n$ with characteristic values $a_n(q),b_n(q)$) and the **radial modified Mathieu equation**, *sharing the same parameter* $q\propto\lambda$. The eigenvalue condition is that a modified Mathieu function vanishes on the boundary ellipse — a **coupled two-parameter root problem**, not the clean "$k$-th root of $J_n$" of the disk. Concrete program:
1. **Build the missing technical paper:** *uniform two-sided enclosures for Mathieu characteristic values $a_n(q),b_n(q)$ and the modified-Mathieu radial phase*, with certified error bounds — the exact analog of the FLPS Bessel-phase SIAM paper. Starting toolkit: Dunster's uniform asymptotic approximations of Mathieu functions (1994); the rigorous large-parameter Lamé–Mathieu eigenvalue asymptotics (e.g. arXiv:1507.04981/.04984); Meixner–Schäfke and DLMF Ch. 28; for the degenerate elongated limit, Borisov–Freitas thin-domain expansions. **This sub-result is itself publishable** (SIAM J. Math. Anal. / IMRN tier) and is the true bottleneck.
2. **Recast the count as a 2-parameter weighted lattice problem** and extend the trapezoidal-floor-sum counting from the annulus paper to the curves that arise; the loss of a single-variable phase means the relevant curve is defined implicitly by the $a_n(q)$ branch structure.
3. **Certified numerics for the low-energy window** via the **Method of Particular Solutions** (high-precision ellipse eigenvalues to locate the threshold) wrapped in interval arithmetic (Arb), respecting principles (P1)–(P2).

A clean win here (Dirichlet ellipse) is an *Inventiones*/JAMS-level result and the natural "blueprint for all convex domains," exactly as the disk was.

**Target 3 — the prize: Dirichlet Pólya for general planar convex domains.** Separation is gone, so this needs a non-separable idea. Two live routes:
- **(a) Kill the $\varepsilon$ in Jiang–Lin.** They already reduced $\varepsilon$-loss Dirichlet Pólya on Lipschitz domains to a finite computation and proved improved Berezin–Li–Yau/Kröger giving *infinitely many* eigenvalues on the nose. The gap is the low-frequency, $O(1)$-count regime. Combining their explicit Weyl-remainder constants with a Filonov-style convex-geometry input to control the bottom of the spectrum is the most plausible assault.
- **(b) A Filonov-type analytic argument for the Dirichlet upper bound on convex domains**, paralleling his Neumann proof — i.e., find the convex-domain test-function/averaging mechanism that works for the *upper* (Dirichlet) direction. That his method cracked Neumann-convex analytically is the strongest evidence this isn't hopeless.

Target 3 is where the problem stops being "extend a machine" and starts requiring a new idea. Treat it as the five- to seven-year horizon, with Targets 0–2 as deliverables along the way.

**Complementary line — Riesz means (lower risk, parallel track).** Frank–Larson's sharp Riesz-mean asymptotics on convex/Lipschitz domains are the averaged cousin; strengthening these (e.g., second-term/remainder control on convex bodies, or Pólya-type bounds for Riesz means $\gamma\ge 1$ where the inequality is more forgiving) yields steady CPAM/JST output and feeds intuition back into the pointwise problem.

---

## 5. Techniques and toolkit

Concretely, what to master (roughly in order of immediate need):

- **Special-function uniform asymptotics with *certified* error bounds.** Olver–Dunster theory; Bessel phase/modulus functions, monotonicity and interlacing of zeros (the engine of the exact correspondence); then **Mathieu / modified-Mathieu and spheroidal wave functions** (Dunster 1994; Meixner–Schäfke; DLMF Chs. 10, 28, 30). This is the rate-limiting expertise for the ellipse.
- **Lattice-point counting under convex/concave curves with explicit constants:** floor sums, trapezoidal floor sums, Lipschitz-constant control (FLPS Thm 5.1 and the annulus extension). Classical $\#$-of-lattice-points-under-a-curve technology (van der Corput, but here the *elementary, explicit-constant* versions are what's used).
- **Variational spectral bounds:** Dirichlet–Neumann bracketing, domain monotonicity, max–min / test-function constructions, Filonov's $\lambda_{k+1}^N<\lambda_k^D$, and the convex-domain monotonicity literature.
- **Berezin–Li–Yau / Kröger / Riesz-mean machinery:** Legendre transforms, the Berezin–Lieb inequality, coherent states; the improved-remainder versions (Geisinger–Laptev–Weidl; Frank–Larson; Jiang–Lin).
- **Laptev's product/Riesz-mean lifting trick** for products, strips, and thin domains.
- **Rigorous computer-assisted proof:** interval/ball arithmetic (Arb / Johansson's library), validated special-function root enclosures, the (P1)/(P2) discipline; plus the **Method of Particular Solutions** for high-precision ellipse eigenvalues to find the analytic/numeric crossover. The FLPS papers' published scripts are the scaffold to fork.

---

## Concrete first moves

1. Read, in order: FLPS *Euclidean balls* (Invent. 2023) → the Bessel-phase SIAM 2024 paper → the annulus paper (arXiv:2505.21737), focusing on §3 (trapezoidal floor sums) and §1.3 (ideas of proof) → Filonov's Neumann-convex CPAM 2025 → Jiang–Lin (2507.04307 and 2507.20330). Pull the FLPS verification scripts and run them.
2. Do **Target 0** to internalize the four-stage machine end-to-end.
3. Start the **Mathieu enclosure paper (Target 2, step 1)** in parallel — it's the bottleneck, it's self-contained, and it's publishable on its own even before the Pólya application lands.
4. Sanity-check the ellipse numerically first (MPS + interval arithmetic) to confirm Dirichlet Pólya *holds* with margin and locate the threshold $\lambda$; the goal is to know where the tight window is before investing in the analytic enclosures.

The natural people in this orbit are Levitin, Polterovich, Sher, Filonov, Frank, Larson, Jiang, Lin, and J. Guo. The subject is unusually collaborative, and the computational scaffolding is openly published, so this is a viable problem to enter from outside the original team.
