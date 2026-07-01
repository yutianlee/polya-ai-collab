# Detailed report: Pólya’s conjecture for new non-tiling Euclidean domain classes

According to the three reports uploaded on **June 30, 2026**, the right framing is: **full Pólya for arbitrary Euclidean domains is a long-horizon problem, but exact Pólya inequalities for new rigid non-tiling families are a strong near-term research target**. The reports consistently identify the modern opening as the Filonov–Levitin–Polterovich–Sher analytic–lattice method, plus rigorous computer-assisted verification; the GPT report also points to quantitative Pólya/$\varepsilon$-loss methods as a bridge to broader classes.

## 1. Problem setting

Let $\Omega\subset\mathbb R^d$ be a bounded Euclidean domain of finite volume. Let

$$
0<\lambda_1^D(\Omega)\le \lambda_2^D(\Omega)\le\cdots
$$

be the Dirichlet Laplace eigenvalues, and let

$$
0=\lambda_0^N(\Omega)\le \lambda_1^N(\Omega)\le\lambda_2^N(\Omega)\le\cdots
$$

be the Neumann Laplace eigenvalues. Define the counting functions, using the strict convention to avoid ambiguity at jumps,

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
$$

$$
N_N(\Omega,\Lambda)=\#\{j:\lambda_j^N(\Omega)<\Lambda\}.
$$

Weyl’s law says

$$
N_{D/N}(\Omega,\Lambda)
\sim
L_d|\Omega|\Lambda^{d/2},
\qquad
L_d=\frac{\omega_d}{(2\pi)^d},
$$

where $\omega_d$ is the volume of the unit ball in $\mathbb R^d$.

**Pólya’s conjecture** asserts the pointwise, all-energy strengthening

$$
N_D(\Omega,\Lambda)\le L_d|\Omega|\Lambda^{d/2},
$$

and

$$
N_N(\Omega,\Lambda)\ge L_d|\Omega|\Lambda^{d/2},
$$

for every $\Lambda\ge0$. Equivalently, in eigenvalue form, the Dirichlet eigenvalues should be no smaller than the semiclassical prediction, while the Neumann eigenvalues should be no larger, up to the usual indexing convention.

In two dimensions this becomes

$$
N_D(\Omega,\Lambda)\le \frac{|\Omega|}{4\pi}\Lambda,
\qquad
N_N(\Omega,\Lambda)\ge \frac{|\Omega|}{4\pi}\Lambda.
$$

The problem is scaling invariant: replacing $\Omega$ by $t\Omega$ sends eigenvalues to $t^{-2}\lambda_j$ and volume to $t^d|\Omega|$, so the inequality is unchanged.

The key distinction is between:

1. **Full Pólya:** prove the conjecture for every bounded Euclidean domain. This is still very hard.

2. **Class Pólya:** prove it for a new natural non-tiling class, such as ellipses, spherical shells, product/cylinder families, thin domains, or perturbative families around solved domains.

For a research program, the second version is the right first target.

## 2. Background and why the conjecture is hard

Pólya proved the conjecture for tiling domains. The modern literature records that Pólya’s proof covered planar tiling domains, with extensions to higher-dimensional tiling situations; Jiang–Lin’s 2026 version summarizes this as the classical baseline. ([arXiv][1])

The conjecture is much stronger than Weyl’s law. Weyl’s law says only that

$$
N(\Lambda)=L_d|\Omega|\Lambda^{d/2}+o(\Lambda^{d/2}),
$$

whereas Pólya asks for the **correct sign of the entire remainder** at every spectral level:

$$
R_D(\Lambda):=N_D(\Lambda)-L_d|\Omega|\Lambda^{d/2}\le0,
$$

$$
R_N(\Lambda):=N_N(\Lambda)-L_d|\Omega|\Lambda^{d/2}\ge0.
$$

This is difficult because $N(\Lambda)$ is a discontinuous staircase function. Oscillations from boundary geometry, periodic rays, low eigenvalues, and multiplicities all matter. Averaged spectral inequalities are much easier. The Berezin–Li–Yau inequality and Kröger-type inequalities control Riesz means or eigenvalue sums, but they do not imply the sharp $\gamma=0$ counting-function inequality. Frank–Larson recently pushed semiclassical Riesz-mean inequalities for convex domains below the classical $\gamma\ge1$ regime, but this still falls short of full Pólya at $\gamma=0$. ([arXiv][2])

So the core obstruction is:

$$
\text{Weyl asymptotic control} \quad \not\Rightarrow \quad \text{pointwise sign control}.
$$

That is why exact proofs so far exploit additional structure: tiling, separation of variables, Bessel phase functions, product decompositions, or certified finite computations.

## 3. Recent progress

### 3.1 The disk/ball breakthrough

Filonov, Levitin, Polterovich, and Sher proved Pólya’s conjecture for the disk, making it the first non-tiling planar domain for which the conjecture was verified. They also proved it for arbitrary planar sectors and, in the Dirichlet case, for balls in every dimension. Their paper appeared in *Inventiones Mathematicae* in 2023. ([arXiv][3])

The essential innovation was not just asymptotics of Bessel zeros. They developed uniform links between spectral counting functions for the disk and corresponding lattice-counting problems, with bounds valid at finite spectral parameter. Their proof is analytic except for a rigorous computer-assisted argument needed for a short Neumann-disk interval. ([arXiv][3])

This is the methodological template for the current program.

### 3.2 Annuli

The same authors later proved the Dirichlet Pólya conjecture for annular domains. The final published version is listed in *Journal of the London Mathematical Society*, volume 113, issue 2, e70425, in 2026. The proof combines variational bounds, Bessel phase-function estimates, refined lattice-point counting, and rigorous computer-assisted analysis; it also yields a two-term upper bound for the disk’s Dirichlet counting function. ([arXiv][4])

This is important because annuli are the first non-simply-connected planar non-tiling class in this line.

### 3.3 $\varepsilon$-loss and quantitative Weyl methods

Jiang and Lin proved an $\varepsilon$-loss version for bounded Lipschitz domains: for each $\varepsilon\in(0,1)$, sufficiently high Dirichlet eigenvalues satisfy

$$
k\le (1+\varepsilon)
\frac{|\Omega|\omega_d}{(2\pi)^d}
\lambda_k(\Omega)^{d/2},
$$

with an explicit threshold $\Lambda(\varepsilon,\Omega)$. Their result reduces the $\varepsilon$-loss version to a computational problem and gives explicit quantitative Weyl remainders. They also prove that strip-tiling domains, including triangles, satisfy better estimates than Pólya’s original bound. The final version is listed as “to appear in CPAM.” ([arXiv][5])

This is a different route from the Bessel/lattice method. It suggests a broader “certificate” strategy: prove a sharp enough explicit remainder bound, then verify the finite low-energy range rigorously.

### 3.4 Thin products and product domains

He and Wang proved Pólya’s conjecture for thin products of the form

$$
(a\Omega_1)\times\Omega_2
$$

when (a) is small enough. They also extend the result to cases where $\Omega_2$ is replaced by a Riemannian manifold, producing thin Riemannian manifolds with boundary satisfying Pólya-type inequalities. ([arXiv][6])

This indicates that product degeneration is a useful solvable regime. The eigenvalue-counting problem becomes close to a convolution of spectra, with one factor dominating.

### 3.5 Non-tiling families by partition/replication methods

Freitas and Salavessa constructed families of non-tiling domains satisfying Pólya’s conjecture in any dimension. Their argument uses the idea that if a domain satisfies Pólya eventually and can be partitioned into arbitrarily many isometric subdomains, then sufficiently fine subdomains inherit Pólya. They apply this to sectors of domains of revolution and thin cylinders, among other examples.

This is less “iconic” than proving Pólya for ellipses, but strategically valuable: it produces domain families without requiring a complete special-function analysis.

### 3.6 Spherical shells and Bessel cross-products

A 2024 paper by Guo, Jiang, Wang, and Yang studies zeros of cross-products of Bessel functions and derivatives of ultraspherical Bessel functions, with applications to Weyl laws for balls and spherical shells in $\mathbb R^d$. The paper obtains new upper bounds for Weyl remainders in Dirichlet and Neumann cases and uses modern lattice-counting input connected to the Gauss circle problem and decoupling. ([arXiv][7])

This does not by itself settle Pólya for spherical shells, but it supplies exactly the kind of zero-counting technology needed for a shell project.

### 3.7 Neumann convex-domain progress: useful but not full Pólya

Filonov proved that for planar convex domains,

$$
N_N(\Omega,\Lambda)
\ge
(2\sqrt 3,j_0^2)^{-1}|\Omega|\Lambda,
$$

where $j_0$ is the first zero of $J_0$. This is a meaningful universal Neumann lower bound, but it is **not** the full Neumann Pólya conjecture, because the Pólya constant in two dimensions is $1/(4\pi)$, which is larger. ([arXiv][8])

This matters for planning: the Neumann convex problem has serious partial progress, but Dirichlet remains the better first target for exact class results.

### 3.8 Recent cylinder/ball improvements

A 2025 preprint by Guo, Miao, Wang, and Zhan builds on the ball/annulus work, improves parts of the analytic regime for the disk, obtains improved Pólya-type estimates for disks, balls, and cylinders, and claims the Neumann Pólya conjecture for cylinders in $\mathbb R^3$. Treat this as provisional until fully refereed, but it is a useful indicator of where the frontier is moving. ([arXiv][9])

## 4. Which problem to attack first?

Do not start with “all convex domains.” That target is too broad. Choose one of the following three subtargets.

| Subtarget                                                             |      Impact | Solvability | My assessment                                                                                                                  |
| --------------------------------------------------------------------- | ----------: | ----------: | ------------------------------------------------------------------------------------------------------------------------------ |
| **Dirichlet Pólya for spherical shells in $\mathbb R^d$, $d\ge3$**    |        High | High-medium | Best first project. Closest to disk/annulus methods; Bessel cross-product technology already exists.                           |
| **Dirichlet Pólya for ellipses**                                      |   Very high |  Medium-low | More prestigious, but Mathieu functions make it substantially harder. Start with near-circular or fixed-eccentricity ellipses. |
| **Exact Dirichlet Pólya for a new strip/product/perturbative family** | Medium-high |        High | Best low-risk route. Less iconic than ellipses, but publishable if the family is natural and genuinely non-tiling.             |

My recommendation: **start with spherical shells or a controlled product/strip family**, while building tools that later transfer to ellipses. Ellipses are attractive, but they are not the easiest first theorem.

## 5. Solving strategy

### Strategy A: special-function + lattice-counting route

This is the route used for disks, sectors, balls, and annuli.

The template is:

1. **Separate variables.**
   Express eigenvalues as zeros of a one-dimensional special-function equation.

2. **Index eigenvalues by angular momentum and radial quantum number.**
   For balls and shells, this gives sums of the form

$$
   N_D(\Omega,\Lambda)
   =
   \sum_{\ell\ge0} m_{\ell,d}\,
   n_\ell(\sqrt{\Lambda}),
$$

   where $m_{\ell,d}$ is the spherical harmonic multiplicity and $n_\ell$ counts radial zeros.

3. **Introduce a phase function.**
   For Bessel-type equations, one replaces raw zeros by a monotone phase condition

$$
   \Phi_\nu(k)\approx \pi n.
$$

   The inequality then becomes a lattice-point estimate in a curvilinear region.

4. **Compare lattice count with phase-space volume.**
   The leading area/volume of the lattice region should equal

$$
   L_d|\Omega|\Lambda^{d/2}.
$$

   The work is to prove the correct one-sided finite inequality, not merely an asymptotic.

5. **Control transition regimes.**
   The hardest region is usually the Airy/turning-point zone, where angular momentum and radial frequency are comparable.

6. **Certify the remaining compact range.**
   Once the analytic estimates prove Pólya for $\Lambda\ge\Lambda_0$, use rigorous eigenvalue enclosures and interval arithmetic for $0\le\Lambda\le\Lambda_0$.

This route is especially plausible for **spherical shells**, because the eigenvalue equations are still Bessel-type. In a shell

$$
A_{\rho,R}=\{x\in\mathbb R^d:\rho<|x|<R\},
$$

Dirichlet radial eigenvalues are zeros of a Bessel cross-product of the schematic form

$$
J_\nu(k\rho)Y_\nu(kR)-Y_\nu(k\rho)J_\nu(kR)=0,
$$

with $\nu=\ell+(d-2)/2$. The multiplicities are explicit spherical harmonic dimensions. This is exactly the kind of structure the shell Weyl/Bessel paper develops.

### Strategy B: quantitative Weyl remainder + finite verification

This route is better for domains without exact special-function zeros.

For Dirichlet problems, the expected two-term behavior in smooth planar domains is

$$
N_D(\Omega,\Lambda)
=
\frac{|\Omega|}{4\pi}\Lambda
-
\frac{|\partial\Omega|}{4\pi}\Lambda^{1/2}
+
\text{lower-order terms}.
$$

The negative boundary term suggests that Dirichlet Pólya should hold eventually for many smooth domains. The challenge is to make “eventually” explicit.

A viable proof structure is:

$$
N_D(\Omega,\Lambda)
\le
\frac{|\Omega|}{4\pi}\Lambda
-
c_1|\partial\Omega|\Lambda^{1/2}
+
C_\Omega \Lambda^\alpha,
$$

with $\alpha<1/2$ or with constants small enough beyond a computable $\Lambda_0$. Then certify the finite interval $[0,\Lambda_0]$.

This is where Jiang–Lin’s quantitative remainder philosophy is useful: it turns asymptotic Pólya-type statements into a finite, verifiable problem. ([arXiv][5])

### Strategy C: embedding into a better-than-Pólya comparison domain

Suppose $\Omega\subset T$, where (T) is a domain for which one has a strict improvement

$$
N_D(T,\Lambda)
\le
L_d|T|\Lambda^{d/2}-M_T(\Lambda).
$$

If $T\setminus\Omega$ has enough spectral mass, Dirichlet bracketing can convert the excess margin $M_T$ into the desired estimate for $\Omega$:

$$
N_D(\Omega,\Lambda)
\le
L_d|\Omega|\Lambda^{d/2}.
$$

This is the logic behind the “larger strip-tiling domain plus complement estimate” approach in Jiang–Lin. They explicitly describe using a larger domain, refined estimates for strip-tiling/product domains, lower bounds on the complement, and Dirichlet monotonicity/bracketing to prove Pólya for new classes. ([arXiv][1])

This is promising for constructing non-tiling families that are not fully separable.

### Strategy D: perturbative stability around solved domains

A natural route to ellipses is to view them as perturbations of the disk. Let

$$
E_e
$$

be an area-normalized ellipse with eccentricity (e). At $e=0$, Pólya is known. For small (e), one can attempt to prove the inequality by combining:

$$
\lambda_j(E_e)=\lambda_j(D)+e^2 a_j+O(e^4),
$$

with spectral-gap estimates, shape derivatives, and rigorous control of eigenvalue crossings.

The limitation is that disk eigenvalues have multiplicities, so perturbation theory must handle splitting. Also, one needs uniform control over infinitely many eigenvalues. A practical proof would combine:

1. perturbation theory for low and moderate eigenvalues;
2. explicit Weyl-remainder bounds for high eigenvalues;
3. interval arithmetic over an eccentricity grid.

This is feasible for **near-circular ellipses** before all ellipses.

## 6. Techniques involved

### 6.1 Variational spectral theory

The min–max principle is used constantly:

$$
\lambda_k^D(\Omega)=
\min_{\dim V=k}
\max_{u\in V\setminus\{0\}}
\frac{\int_\Omega |\nabla u|^2}{\int_\Omega |u|^2}.
$$

Core tools:

* Dirichlet domain monotonicity.
* Dirichlet and Neumann bracketing.
* Mixed boundary comparisons.
* Riesz means and Legendre transforms.
* Variational bounds for separated radial operators.

Dirichlet is usually cleaner than Neumann because Dirichlet eigenvalues are monotone under domain inclusion. Neumann eigenvalues lack such simple monotonicity for arbitrary domains.

### 6.2 Weyl asymptotics and Tauberian methods

The key object is the Weyl expansion

$$
N(\Lambda)=L_d|\Omega|\Lambda^{d/2}+R(\Lambda),
$$

The task is to obtain explicit one-sided bounds for $R(\Lambda)$. Riesz means are smoother:

$$
R_\gamma^D(\Lambda)
=
\sum_j(\Lambda-\lambda_j^D)_+^\gamma,
$$

and satisfy sharper universal inequalities. But Pólya corresponds to the singular endpoint $\gamma=0$, so one needs Tauberian conversion or additional structure.

Frank–Larson’s convex-domain work is relevant here because it studies semiclassical inequalities for Dirichlet and Neumann Riesz means and explains what a convex-domain failure of Pólya would imply at the level of Riesz means. ([arXiv][2])

### 6.3 Special functions

For disks, balls, annuli, and shells:

* Bessel functions $J_\nu,Y_\nu$.
* Derivatives $J_\nu'$ for Neumann problems.
* Ultraspherical Bessel functions in higher dimensions.
* Cross-products for annular/shell boundary conditions.
* Uniform Debye–Olver asymptotics.
* Airy transition asymptotics near turning points.
* Monotonicity and convexity of phase functions.

For ellipses:

* Angular Mathieu functions.
* Radial Mathieu functions.
* Characteristic values.
* Coupled dependence of the separation constant and spectral parameter.
* Uniform asymptotics in eccentricity and mode number.

The ellipse is harder precisely because the spectral parameter and separation parameter are intertwined; the Bessel phase plane is replaced by a two-parameter Mathieu problem. Gemini’s report correctly identifies this as the main technical barrier for the ellipse.

### 6.4 Lattice-point counting

The disk and ball method turns spectral counting into counting integer lattice points in a curved region. Techniques include:

* Euler–Maclaurin summation.
* Van der Corput estimates.
* Gauss circle problem inputs.
* Poisson summation.
* Convex lattice-region estimates.
* Boundary correction terms.
* Multiplicity-weighted lattice counts in higher dimensions.

Recent shell-related work explicitly links Bessel zero estimates with modern progress on lattice counting and decoupling. ([arXiv][7])

### 6.5 Rigorous computation

This is not optional. The modern exact proofs often reduce the problem to a finite spectral interval after analytic estimates handle high energy.

Necessary tools:

* Interval arithmetic.
* Certified root isolation.
* Validated Newton/Krawczyk methods.
* Arb/MPFI-style ball arithmetic.
* Certified Bessel/Mathieu function evaluation.
* Method of Particular Solutions or boundary integral eigenvalue enclosures.
* Temple–Kato or Lehmann–Goerisch-type eigenvalue validation, if using finite elements.

The disk proof needed rigorous computation only for a short Neumann interval, but annuli required a more systematic computer-assisted component. ([arXiv][3]) ([arXiv][4])

### 6.6 Shape perturbation and parameter control

For ellipses, superellipses, near-disks, or near-annuli:

* Hadamard shape derivative formula.
* Analytic perturbation theory for multiple eigenvalues.
* Eigenvalue crossing control.
* Uniform Lipschitz estimates in shape parameters.
* Certified parameter subdivision.

The goal is to prove statements over a continuum of domains, not merely for one numerical instance.

## 7. Recommended research plan

### Phase 1: Reproduce the solved examples

Start with the FLPS disk/ball paper, then the annulus paper. Your first internal milestone should be to reproduce the proof architecture:

$$
\text{special-function zeros}
\to
\text{phase estimates}
\to
\text{lattice count}
\to
\text{finite certified range}.
$$

Do this before choosing ellipses. The reports correctly identify this analytic–lattice method as the main current engine for the problem.

### Phase 2: Choose a first theorem

I recommend one of the following.

#### Theorem A: Dirichlet Pólya for spherical shells in $\mathbb R^d$

Target statement:

$$
N_D(A_{\rho,R},\Lambda)
\le
L_d|A_{\rho,R}|\Lambda^{d/2},
\qquad
A_{\rho,R}=\{\rho<|x|<R\}.
$$

Start with fixed $d=3$, then general $d$. Use scaling to set $R=1$, so the parameter is $\rho\in(0,1)$.

Why this is attractive:

* It is a genuinely non-tiling class.
* It generalizes planar annuli.
* It remains Bessel-based.
* There is recent Bessel/shell Weyl technology.
* It is more tractable than ellipses.

Main difficulty:

* Uniformity in the shell ratio $\rho/R$, especially as $\rho\to0$ and $\rho\to R$.
* Bessel cross-products are harder than single Bessel zeros.
* Multiplicity growth in higher dimensions must be handled cleanly.

#### Theorem B: Dirichlet Pólya for near-circular ellipses

Target statement:

$$
N_D(E_e,\Lambda)
\le
\frac{|E_e|}{4\pi}\Lambda
$$

for $0\le e\le e_0$, with explicit $e_0>0$.

Why this is attractive:

* Ellipses are the iconic next target.
* The result would be highly visible.
* It creates a bridge from disk Pólya to non-rotational convex domains.

Main difficulty:

* Mathieu functions.
* Splitting of disk eigenvalue multiplicities.
* Uniform control over all modes.
* Parameter-continuum certification.

This is a better second project than first project.

#### Theorem C: A new smooth non-tiling family from strip/product comparison

Target statement:

Construct an explicit smooth family $\Omega_\eta$ that does not tile $\mathbb R^d$ and prove

$$
N_D(\Omega_\eta,\Lambda)
\le
L_d|\Omega_\eta|\Lambda^{d/2}
$$

for a quantified parameter range.

Why this is attractive:

* Jiang–Lin’s machinery is designed for this.
* It can produce publishable results without special functions.
* It builds a toolkit for broader convex-domain attacks.

Main difficulty:

* The family must be natural enough to be interesting.
* The proof must be more than a direct corollary of existing strip-tiling results.
* Smoothing corners while preserving certified estimates is delicate.

## 8. Specific technical route for spherical shells

For the shell $A_{\rho,1}\subset\mathbb R^d$, separation gives angular momentum $\ell=0,1,2,\dots$, order

$$
\nu=\ell+\frac{d-2}{2},
$$

and multiplicity

$$
m_{\ell,d}
=
\binom{\ell+d-1}{d-1}
-
\binom{\ell+d-3}{d-1}.
$$

The radial Dirichlet eigenvalues are zeros in $k=\sqrt{\Lambda}$ of

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k).
$$

Then

$$
N_D(A_{\rho,1},\Lambda)
=
\sum_{\ell\ge0}
m_{\ell,d}
\#\{k>0:F_{\nu,\rho}(k)=0,\ k^2<\Lambda\}.
$$

The proof should aim to build a phase function $\Phi_{\nu,\rho}(k)$ such that radial zeros are trapped by

$$
\Phi_{\nu,\rho}(k)=\pi n+O(\text{controlled error}).
$$

Then the counting problem becomes a weighted lattice problem in ($\ell,n$). The leading integral should equal the phase-space volume

$$
L_d|A_{\rho,1}|\Lambda^{d/2}.
$$

The work is to show that the discrete count never exceeds this volume.

Break the proof into regimes:

1. **Oscillatory region:** $k\rho>\nu+\nu^{1/3+\delta}$.
   Use classical oscillatory Bessel expansions.

2. **Outer turning-point region:** $k\sim\nu$.
   Use Airy-type uniform asymptotics.

3. **Inner-boundary transition:** $k\rho\sim\nu$.
   This is shell-specific and likely the hardest part.

4. **Evanescent region:** $k\rho<\nu-\nu^{1/3+\delta}$.
   Show there are few or no relevant zeros.

5. **Low-energy compact region:** certify by interval arithmetic.

A successful proof for $d=3$ would already be a serious result. General (d) introduces higher multiplicity weights but not a fundamentally different special-function equation.

## 9. Specific technical route for ellipses

For an ellipse

$$
E_{a,b}=\left\{(x,y):\frac{x^2}{a^2}+\frac{y^2}{b^2}<1\right\},
$$

use elliptic coordinates. The Helmholtz equation separates into angular and radial Mathieu equations. The eigenvalues are determined by compatibility between angular characteristic values and radial boundary conditions.

A realistic program is:

1. **Normalize area:** set $|E_{a,b}|=\pi$, so the disk is $a=b=1$.

2. **Parameterize by eccentricity:** $e=\sqrt{1-b^2/a^2}$.

3. **Prove high-energy Pólya:** use explicit remainder estimates or ellipse-specific two-term asymptotics to show

$$
   N_D(E_e,\Lambda)\le\frac{|E_e|}{4\pi}\Lambda
$$

   for $\Lambda\ge\Lambda_0(e)$.

4. **Certify low-energy range:** compute rigorous enclosures for all eigenvalues below $\Lambda_0(e)$.

5. **Make the proof uniform in (e):** subdivide $e\in[0,e_0]$ or $e\in[0,1-\delta]$ into intervals and use derivative bounds for Mathieu characteristic values.

6. **Handle limiting regimes separately:**

   * $e\to0$: disk degeneracies and perturbation theory.
   * $e\to1$: thin-domain asymptotics.

A full all-eccentricity ellipse theorem would be high-impact. A near-circular ellipse theorem is a credible first milestone.

## 10. Main risks

The principal risks are technical, not conceptual.

First, asymptotics are insufficient. A theorem of the form

$$
N_D(\Lambda)
=
L_d|\Omega|\Lambda^{d/2}
-
c|\partial\Omega|\Lambda^{(d-1)/2}
+
o(\Lambda^{(d-1)/2})
$$

does not by itself prove Pólya unless the remainder is explicit enough to identify a finite threshold.

Second, low eigenvalues can ruin plausible asymptotic arguments. Exact finite verification must be rigorous, not numerical evidence.

Third, parameter-uniform statements are much harder than fixed-domain statements. “The ellipse” means a continuum of domains.

Fourth, Neumann should probably not be the initial target. The Neumann inequality has the opposite sign, less domain monotonicity, a zero eigenvalue, and more delicate boundary behavior. The disk Neumann proof itself required computer assistance for a short interval. ([arXiv][3])

## 11. Recommended first-year work plan

A good concrete sequence is:

| Stage | Goal                                                                     | Output                                                                |
| ----- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| 1     | Reproduce FLPS disk estimates                                            | Internal notes; verified understanding of Bessel phase/lattice method |
| 2     | Reproduce annulus proof architecture                                     | Identify which estimates generalize to shells                         |
| 3     | Build certified Bessel-zero/cross-product code                           | Validation infrastructure                                             |
| 4     | Prove high-energy shell estimate for fixed $\rho$                        | First analytic proposition                                            |
| 5     | Make $\rho$-uniform over compact intervals ([\rho_0,\rho_1]\subset(0,1)) | Main technical step                                                   |
| 6     | Treat $\rho\to0$ and $\rho\to1$ separately                               | Complete shell-family proof                                           |
| 7     | Write the theorem for $d=3$, then general (d)                            | Publishable manuscript                                                |

For a lower-risk route, replace stages 4–7 with a Jiang–Lin-style construction of a new smooth non-tiling family. For a higher-impact route, replace them with near-circular ellipses.

## Bottom line

The best near-term project is **not full Pólya for arbitrary domains**. It is:

$$
\boxed{\text{Exact Dirichlet Pólya for one new natural non-tiling class.}}
$$

My preferred first target is **spherical shells in dimensions $d\ge3$**, starting with $d=3$. The strongest longer-term target is **ellipses**, preferably first in a perturbative near-disk regime. The lowest-risk route is a **strip/product/comparison family** using Jiang–Lin’s quantitative framework.

The technical core will be a combination of **special-function asymptotics, lattice-point counting, variational bracketing, explicit Weyl remainders, and rigorous interval computation**. This is one of the rare classical spectral conjectures where a well-designed computer-assisted analytic proof is not a fallback; it is part of the central method.

[1]: https://arxiv.org/html/2507.04307v4 "Pólya’s conjecture up to ϵ-loss and quantitative estimates for the remainder of Weyl’s law 2020 Mathematics Subject Classification. Primary 35P15; Secondary 35P20, 42B37. Key words and phrases: Dirichlet eigenvalue, Weyl law, Pólya conjecture"
[2]: https://arxiv.org/abs/2410.04769?utm_source=chatgpt.com "Semiclassical inequalities for Dirichlet and Neumann Laplacians on convex domains"
[3]: https://arxiv.org/abs/2203.07696 "[2203.07696] Pólya's conjecture for Euclidean balls"
[4]: https://arxiv.org/abs/2505.21737 "[2505.21737] Pólya's conjecture for Dirichlet eigenvalues of annuli"
[5]: https://arxiv.org/abs/2507.04307 "[2507.04307] Pólya's conjecture up to $ε$-loss and quantitative estimates for the remainder of Weyl's law"
[6]: https://arxiv.org/abs/2402.12093 "[2402.12093] Pólya's conjecture for thin products"
[7]: https://arxiv.org/abs/2412.14059?utm_source=chatgpt.com "Bessel functions and Weyl's law for balls and spherical shells"
[8]: https://arxiv.org/abs/2309.01432 "[2309.01432] On the Pólya conjecture for the Neumann problem in planar convex domains"
[9]: https://arxiv.org/html/2511.17050v1 "Improvement of Pólya’s conjecture for balls and cylinders"
