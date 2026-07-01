# Report: Research program for Pólya’s conjecture in new non-tiling Euclidean domains

## Executive conclusion

The correct working target is not the full arbitrary-domain Pólya conjecture. The better research program is:

$$
\boxed{\text{Prove exact Dirichlet Pólya for one new natural non-tiling Euclidean domain class.}}
$$

The uploaded reports converge on this point: full Pólya is too broad as an initial target, while rigid non-tiling families—spherical shells, product/strip families, and eventually ellipses—are realistic entry points. The cleanest first theorem is likely **Dirichlet Pólya for spherical shells**, starting in $d=3$. The higher-impact flagship is **Dirichlet Pólya for ellipses**, first near-circular and later all eccentricities. The lower-risk fallback is a **Jiang–Lin-style certificate theorem** for a smooth strip/product/comparison family.

One caveat: the uploaded reports disagree on the precise status of the Neumann planar convex case. One report treats Filonov’s convex Neumann result as resolving all planar convex Neumann Pólya, while another describes it as a meaningful but non-sharp lower bound, not the full Pólya constant. For this research plan, that disagreement does not affect the main recommendation: **start with the Dirichlet side**, where all reports agree the hard open target lies.

---

## 1. Problem setting

Let $\Omega\subset\mathbb R^d$ be a bounded Euclidean domain. Let

$$
0<\lambda_1^D(\Omega)\le \lambda_2^D(\Omega)\le\cdots
$$

be the Dirichlet Laplace eigenvalues, and let

$$
0=\lambda_0^N(\Omega)\le \lambda_1^N(\Omega)\le\cdots
$$

be the Neumann eigenvalues. Define counting functions

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
\qquad
N_N(\Omega,\Lambda)=\#\{j:\lambda_j^N(\Omega)<\Lambda\}.
$$

Weyl’s law gives

$$
N_{D/N}(\Omega,\Lambda)\sim L_d|\Omega|\Lambda^{d/2},
\qquad
L_d=\frac{\omega_d}{(2\pi)^d}.
$$

Pólya’s conjecture strengthens this asymptotic statement to a pointwise all-energy inequality:

$$
N_D(\Omega,\Lambda)\le L_d|\Omega|\Lambda^{d/2},
$$

$$
N_N(\Omega,\Lambda)\ge L_d|\Omega|\Lambda^{d/2}.
$$

In two dimensions this is

$$
N_D(\Omega,\Lambda)\le \frac{|\Omega|}{4\pi}\Lambda,
\qquad
N_N(\Omega,\Lambda)\ge \frac{|\Omega|}{4\pi}\Lambda.
$$

The problem is scale-invariant. Replacing $\Omega$ by $t\Omega$ rescales eigenvalues by $t^{-2}$ and volume by $t^d$, leaving the inequality unchanged.

For the ellipse $E_{a,b}\subset\mathbb R^2$,

$$
E_{a,b}=\left\{(x,y):\frac{x^2}{a^2}+\frac{y^2}{b^2}<1\right\},
\qquad |E_{a,b}|=\pi ab,
$$

the Dirichlet conjecture becomes

$$
N_D(E_{a,b},\lambda)\le \frac{ab}{4}\lambda
\qquad \text{for all }\lambda>0,
$$

or equivalently

$$
\lambda_k^D(E_{a,b})\ge \frac{4k}{ab}.
$$

This is the most iconic non-rotational convex-domain target, but it is not the easiest first theorem.

### Why this is difficult

Pólya is much stronger than Weyl’s law. Weyl gives only

$$
N(\Lambda)=L_d|\Omega|\Lambda^{d/2}+o(\Lambda^{d/2}),
$$

while Pólya asks for the **correct sign** of the entire spectral remainder at every energy:

$$
R_D(\Lambda)\le0,
\qquad
R_N(\Lambda)\ge0.
$$

This is hard because $N(\Lambda)$ is a staircase function. Low eigenvalues, multiplicities, boundary geometry, and arithmetic oscillations of lattice counts can all matter. Averaged inequalities such as Berezin–Li–Yau and Kröger control Riesz means, but they do not prove the sharp $\gamma=0$ counting-function inequality.

The reports therefore distinguish:

1. **Full Pólya:** all bounded Euclidean domains. This is long-horizon.
2. **Class Pólya:** a new natural non-tiling family. This is the viable research target.

---

## 2. Current methodological baseline

The modern template is the Filonov–Levitin–Polterovich–Sher method. The reports describe the breakthrough sequence as follows: Pólya was classical for tiling domains; then FLPS proved it for the disk, sectors, and Dirichlet balls; later work extended the Dirichlet case to annuli; and newer directions include spherical shells, thin products, $\varepsilon$-loss quantitative Weyl results, and computer-assisted verification frameworks.

The FLPS machine has four structural components.

First, an **exact spectral-to-lattice correspondence**: in the disk, eigenvalues are Bessel zeros $j_{n,k}^2$, and the Bessel phase function converts the eigenvalue count into a weighted lattice-point count under an explicit curve. This is exact, not merely asymptotic.

Second, one needs **uniform phase enclosures**: explicit two-sided estimates for the relevant special-function phase, uniform in order and spectral parameter.

Third, one needs **explicit lattice-counting inequalities**, including convex/concave curve bounds and trapezoidal floor-sum estimates.

Fourth, one needs a **computer-assisted finite-window closure**: analytic estimates prove the result beyond a threshold, and interval/rational arithmetic verifies the compact low-energy range.

The key lesson is that computer assistance is not cosmetic here. The exact proofs reduce an infinite spectral problem to a finite interval after the analytic part is complete.

---

## 3. Recommended global research strategy

Organize the project into **seven phases**. The phases are cumulative, but Phases 3A, 3B, and 4 can be pursued in parallel depending on taste and available collaborators.

---

### Phase 0 — Fix the target and conventions

#### Objective

Choose a theorem whose statement is strong enough to matter but rigid enough to be provable.

The recommended initial target is:

$$
\boxed{
N_D(A_{\rho,R},\Lambda)
\le
L_d|A_{\rho,R}|\Lambda^{d/2}
}
$$

for spherical shells

$$
A_{\rho,R}=\{x\in\mathbb R^d:\rho<|x|<R\},
$$

starting with $d=3$ and then general (d).

The stronger but harder target is:

$$
\boxed{
N_D(E_e,\Lambda)\le \frac{|E_e|}{4\pi}\Lambda
}
$$

for area-normalized ellipses $E_e$, first for $0\le e\le e_0$, then for all $e\in(0,1)$. The uploaded reports explicitly rank spherical shells as the better first project, ellipses as the prestigious longer-term target, and strip/product/comparison families as the lowest-risk route.

#### Methodology

Use the following decision rule.

If the goal is a first theorem, choose **spherical shells** or a **strip/product/comparison family**. If the goal is a flagship result, choose **near-circular ellipses** first, not all ellipses. If the goal is a full program over multiple papers, run the shell/product route while developing Mathieu-function tools for ellipses.

#### Deliverable

A two-page “target theorem memo” containing:

$$
\text{domain class},\quad
\text{boundary condition},\quad
\text{parameter range},\quad
\text{counting convention},\quad
\text{verification plan}.
$$

Use strict or non-strict counting consistently. The reports use both conventions in places; the proof must not depend on ambiguity at eigenvalue jumps.

---

### Phase 1 — Reproduce the solved machine

#### Objective

Reconstruct the disk/ball/annulus proof architecture until it becomes operational.

The internal milestone should be:

$$
\text{special-function zeros}
\to
\text{phase estimates}
\to
\text{lattice count}
\to
\text{finite certified range}.
$$

The uploaded strategy explicitly recommends reproducing the FLPS disk/ball and annulus arguments before moving to ellipses.

#### Methodology

Study the proof as a four-part pipeline.

First, express the spectrum by separated variables. For disks and balls, this means Bessel zeros. For annuli/shells, this means Bessel cross-products.

Second, build or reproduce the phase map. One wants inequalities of the form

$$
\Phi_\nu(k)\approx \pi n
$$

with explicit one-sided errors.

Third, turn the eigenvalue-counting problem into lattice counting. The analytic target is not merely

$$
N_D(\Lambda)=L_d|\Omega|\Lambda^{d/2}+o(\Lambda^{d/2}),
$$

but the sharp one-sided inequality

$$
N_D(\Lambda)\le L_d|\Omega|\Lambda^{d/2}
$$

for every $\Lambda$.

Fourth, close the low-energy range by rigorous computation.

#### Deliverable

A verified notebook or codebase that reproduces the disk/annulus counting argument on a small test range and records every analytic inequality needed for the final comparison.

---

### Phase 2 — Build certified numerical infrastructure

#### Objective

Develop a reusable verification framework for finite spectral windows.

This is necessary because the reports emphasize that asymptotics do not by themselves prove Pólya: a two-term Weyl expansion is insufficient unless it gives a computable threshold beyond which the sign is guaranteed, and the remaining compact interval must be certified rather than numerically guessed.

#### Methodology

Build three components.

First, implement **certified special-function evaluation** for Bessel functions, Bessel cross-products, and eventually Mathieu functions.

Second, implement **certified eigenvalue enclosures**. For separable domains, use interval root isolation for the special-function equations. For ellipses, use the Method of Particular Solutions or boundary-integral eigenvalue enclosures, wrapped in interval arithmetic.

Third, implement **certified counting verification**. For every eigenvalue enclosure below $\Lambda_0$, verify the equivalent eigenvalue inequality

$$
\lambda_k^D(\Omega)\ge C_\Omega k^{2/d}
$$

or the counting inequality

$$
N_D(\Omega,\Lambda)\le L_d|\Omega|\Lambda^{d/2}.
$$

The relevant computational tools listed in the reports include interval arithmetic, certified root isolation, Newton/Krawczyk validation, Arb/MPFI-style ball arithmetic, certified Bessel/Mathieu evaluation, MPS, boundary-integral enclosures, and finite-element eigenvalue validation methods such as Temple–Kato or Lehmann–Goerisch.

#### Deliverable

A verification package satisfying:

$$
\text{input: domain parameters and } \Lambda_0
\quad\Rightarrow\quad
\text{certified Pólya check for }0\le \Lambda\le \Lambda_0.
$$

For publication, this package should be deterministic, reproducible, and based on interval/rational arithmetic wherever possible.

---

### Phase 3A — First theorem route: spherical shells

#### Objective

Prove Dirichlet Pólya for spherical shells, ideally first in $\mathbb R^3$:

$$
A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},
\qquad
0<\rho<1.
$$

The reports identify shells as attractive because they are genuinely non-tiling, generalize annuli, remain Bessel-based, and are more tractable than ellipses.

#### Methodology

Separate variables. For $A_{\rho,1}\subset\mathbb R^d$, angular momentum $\ell=0,1,2,\dots$ gives order

$$
\nu=\ell+\frac{d-2}{2}.
$$

The radial Dirichlet eigenvalues are zeros of the Bessel cross-product

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k).
$$

Thus

$$
N_D(A_{\rho,1},\Lambda)
=
\sum_{\ell\ge0}
m_{\ell,d}
\#\{k>0:F_{\nu,\rho}(k)=0,\ k^2<\Lambda\}.
$$

The proof should construct a phase function

$$
\Phi_{\nu,\rho}(k)
$$

whose level sets trap zeros:

$$
\Phi_{\nu,\rho}(k)=\pi n+O(\text{controlled error}).
$$

Then the problem becomes a multiplicity-weighted lattice count in ($\ell,n$), whose leading integral must match

$$
L_d|A_{\rho,1}|\Lambda^{d/2}.
$$

The task is to prove that the discrete weighted count never exceeds this phase-space volume.

Break the analysis into regimes:

| Regime                                   | Objective                           | Methodology                             |
| ---------------------------------------- | ----------------------------------- | --------------------------------------- |
| Oscillatory region                       | Control ordinary Bessel oscillation | Classical oscillatory Bessel expansions |
| Outer turning point $k\sim \nu$          | Control Airy transition             | Debye–Olver/Airy asymptotics            |
| Inner-boundary transition $k\rho\sim\nu$ | Handle shell-specific difficulty    | Cross-product phase analysis            |
| Evanescent region                        | Show few/no relevant zeros          | Exponential Bessel estimates            |
| Low-energy compact range                 | Close finite window                 | Interval arithmetic                     |

These are exactly the regimes identified in the shell route.

#### Deliverables

A practical sequence is:

1. Fixed $d=3$, fixed $\rho$.
2. Fixed $d=3$, $\rho\in[\rho_0,\rho_1]\subset(0,1)$.
3. Endpoint regimes $\rho\to0$ and $\rho\to1$.
4. General (d), with multiplicity-weighted lattice estimates.

The uploaded first-year plan gives a similar sequence: reproduce disk estimates, reproduce annuli, build certified Bessel cross-product code, prove fixed-$\rho$ high-energy shell estimates, make $\rho$-uniform, treat $\rho\to0$ and $\rho\to1$, then write the $d=3$ and general-$d$ theorem.

---

### Phase 3B — Lower-risk route: certificate theorem for a non-tiling strip/product/comparison family

#### Objective

Construct a smooth non-tiling family $\Omega_\eta$ and prove

$$
N_D(\Omega_\eta,\Lambda)
\le
L_d|\Omega_\eta|\Lambda^{d/2}
$$

for a quantified parameter range.

This is less iconic than ellipses but more controllable. The reports describe Jiang–Lin’s $\varepsilon$-loss and quantitative Weyl approach as a way to turn asymptotic estimates into a finite verification problem.

#### Methodology

Use a high-energy/finite-window split.

For smooth planar Dirichlet domains, one expects

$$
N_D(\Omega,\Lambda)
=
\frac{|\Omega|}{4\pi}\Lambda
-
\frac{|\partial\Omega|}{4\pi}\Lambda^{1/2}
+
\text{lower-order terms}.
$$

The negative boundary term suggests eventual Dirichlet Pólya. But “eventual” must be explicit. A viable proof has the form

$$
N_D(\Omega,\Lambda)
\le
\frac{|\Omega|}{4\pi}\Lambda
-
c_1|\partial\Omega|\Lambda^{1/2}
+
C_\Omega\Lambda^\alpha
$$

with either $\alpha<1/2$ or constants strong enough beyond a computable threshold $\Lambda_0$. Then one verifies the finite interval $[0,\Lambda_0]$.

A second mechanism is comparison with a better-than-Pólya tiling or strip-tiling domain (T). If

$$
N_D(T,\Lambda)
\le
L_d|T|\Lambda^{d/2}-M_T(\Lambda),
$$

then Dirichlet bracketing and lower bounds on $T\setminus \Omega$ may convert the surplus margin $M_T$ into

$$
N_D(\Omega,\Lambda)
\le
L_d|\Omega|\Lambda^{d/2}.
$$

The reports explicitly identify this as the logic behind the larger-domain/strip-tiling comparison route.

#### Deliverables

A good first theorem would be a new smooth family that is:

* non-tiling;
* parametrized by one or two geometric parameters;
* close enough to a tiling/product/strip family to inherit explicit estimates;
* nontrivial enough not to be a direct corollary of existing strip-tiling results.

This phase can run in parallel with the shell route. It provides a lower-risk publication path and builds the verification/certificate infrastructure needed later.

---

### Phase 4 — Near-circular ellipses

#### Objective

Prove Dirichlet Pólya for area-normalized ellipses $E_e$ for a nonzero eccentricity interval:

$$
0\le e\le e_0,
\qquad
N_D(E_e,\Lambda)\le \frac{|E_e|}{4\pi}\Lambda
\quad
\forall \Lambda.
$$

The uploaded reports describe near-circular ellipses as a credible first ellipse milestone, while warning that all-eccentricity ellipses are harder because the proof must be uniform over a continuum of domains.

#### Methodology

Use a perturbative stability program around the disk.

Let $E_e$ be area-normalized with $E_0=D$. Since Pólya is known for the disk, attempt to prove stability for small (e) using shape perturbation:

$$
\lambda_j(E_e)=\lambda_j(D)+e^2 a_j+O(e^4).
$$

The reports identify the required ingredients: spectral-gap estimates, shape derivatives, control of eigenvalue splitting, and interval arithmetic over an eccentricity grid.

The proof should split the spectrum into three regions.

For low modes, use certified eigenvalue enclosures and perturbative shape derivatives.

For intermediate modes, use a hybrid of perturbation bounds and numerical certification over a grid in (e).

For high modes, use explicit Weyl-remainder bounds or ellipse-specific two-term estimates to show that Pólya holds for $\Lambda\ge \Lambda_0(e)$.

The final obstacle is uniformity in (e). One must subdivide $e\in[0,e_0]$, bound the derivative of relevant spectral data with respect to (e), and certify that no spectral crossing invalidates the inequality.

#### Deliverable

A theorem of the form:

$$
\exists e_0>0
\quad
\text{such that}
\quad
N_D(E_e,\Lambda)\le \frac{|E_e|}{4\pi}\Lambda
\quad
\forall \Lambda\ge0,\quad 0\le e\le e_0.
$$

This would be a strong bridge from disk Pólya to genuinely anisotropic convex domains.

---

### Phase 5 — Full Dirichlet ellipse

#### Objective

Prove Dirichlet Pólya for all planar ellipses.

After normalization $|E_{a,b}|=\pi$, this means proving

$$
N_D(E_e,\Lambda)\le \frac{1}{4}\Lambda
$$

for every eccentricity $e\in(0,1)$ and every $\Lambda>0$.

#### Methodology

This requires the full ellipse separation theory.

In elliptic coordinates ($\mu,\nu$),

$$
x=c\cosh\mu\cos\nu,
\qquad
y=c\sinh\mu\sin\nu,
$$

and the ellipse boundary is $\mu=\mu_0$. The Helmholtz equation separates into an angular Mathieu equation

$$
\Theta''(\nu)+(\alpha-2q\cos 2\nu)\Theta(\nu)=0
$$

and a radial modified Mathieu equation

$$
R''(\mu)-(\alpha-2q\cosh 2\mu)R(\mu)=0,
$$

where $q=c^2\lambda/4$ and $\alpha$ is the separation constant.

The high-energy analytic part should establish explicit phase enclosures for the radial and angular Mathieu data, map the spectral count into a two-parameter ($\alpha,q$) lattice problem, and compare the resulting lattice count with the Weyl area.

The low-energy part should compute certified enclosures for all eigenvalues below the threshold. The report emphasizes that floating point alone is insufficient: the proof needs computer-assisted interval arithmetic guaranteeing the true eigenvalue inequality.

The main analytic bottleneck is that Mathieu functions depend on coupled parameters ($\alpha,q$), unlike the single-variable Bessel zero problem. The reports therefore identify the missing technical paper as: **uniform two-sided enclosures for Mathieu characteristic values (a_n(q),b_n(q)) and the modified-Mathieu radial phase, with certified errors**.

#### Subphases

**Phase 5.1 — Mathieu enclosure paper.**
Prove explicit, computable, uniform WKB/Liouville–Green bounds for angular and radial Mathieu phases. This is publishable independently. The reports identify special-function asymptotics with certified error bounds as the rate-limiting expertise.

**Phase 5.2 — Two-parameter lattice counting.**
Reformulate the eigenvalue count as a weighted lattice problem in $(n,m)$ or $(\alpha,q)$. Extend floor-sum/trapezoidal estimates from the annulus setting to implicitly defined Mathieu phase curves.

**Phase 5.3 — Eccentricity-uniform proof.**
Normalize area, parameterize by $e=\sqrt{1-b^2/a^2}$, prove high-energy Pólya above $\Lambda_0(e)$, certify low energy, then make all constants uniform in $e$. Treat $e\to0$ by disk degeneracy/perturbation theory and $e\to1$ by thin-domain asymptotics.

**Phase 5.4 — Certified finite verification.**
Use MPS or boundary-integral methods with interval arithmetic. The reports specifically mention MPS, interval arithmetic, and a posteriori Newton–Kantorovich/Moler–Payne-type error bounds for rigorous eigenvalue validation.

#### Deliverable

A full theorem:

$$
N_D(E_{a,b},\Lambda)\le \frac{ab}{4}\Lambda
\qquad
\forall a>b>0,\quad \forall \Lambda>0.
$$

This would be the flagship result of the program.

---

### Phase 6 — General planar convex domains

#### Objective

Move beyond separable domains and attack

$$
N_D(\Omega,\Lambda)\le \frac{|\Omega|}{4\pi}\Lambda
$$

for smooth planar convex $\Omega$.

This is the prize beyond the ellipse. The reports describe this as the stage where the problem stops being “extend the machine” and requires a new idea.

#### Methodology

There are two main routes.

First, try to remove the $\varepsilon$ from the Jiang–Lin framework. Their $\varepsilon$-loss result reduces high-energy control to quantitative Weyl remainders and finite computation; the remaining gap is the exact pointwise sign at the endpoint.

Second, seek a Filonov-type convex-domain argument for the Dirichlet upper bound. This would require a convex-geometric test-function or averaging method that works in the upper-counting direction.

A third supporting line is Riesz means. Since Riesz means are averaged versions of the pointwise problem, strengthening second-term and remainder estimates for convex/Lipschitz domains may not solve Pólya directly, but can supply constants, thresholds, and rigidity information for the counting-function problem.

#### Deliverable

Do not aim immediately for all smooth convex domains. Aim first for one of:

$$
\text{convex domains close to ellipses},
$$

$$
\text{uniformly curved convex domains with controlled billiard geometry},
$$

$$
\text{convex domains admitting certified quantitative Weyl remainders},
$$

$$
\text{convex perturbations of solved separable domains}.
$$

---

## 4. Practical phase table

| Phase | Main objective                 | Methodology                                                                   | Concrete output                                         |
| ----: | ------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------- |
|     0 | Fix theorem and conventions    | Choose domain class, boundary condition, counting convention, parameter range | Target theorem memo                                     |
|     1 | Reproduce FLPS/annulus machine | Bessel zeros, phase functions, lattice counting, finite verification          | Internal reconstruction and code                        |
|     2 | Build certified numerics       | Interval arithmetic, root isolation, MPS, validated counting                  | Reusable verification package                           |
|    3A | Prove shell theorem            | Bessel cross-products, weighted lattice counts, turning-point analysis        | Dirichlet Pólya for $A_{\rho,1}$, first $d=3$           |
|    3B | Low-risk certificate family    | Quantitative Weyl remainder plus finite verification                          | New smooth non-tiling strip/product/comparison family   |
|     4 | Near-circular ellipses         | Shape perturbation, spectral-gap control, parameter subdivision               | Dirichlet Pólya for $0\le e\le e_0$                     |
|     5 | Full ellipse                   | Mathieu phase enclosures, two-parameter lattice counting, certified numerics  | Dirichlet Pólya for all ellipses                        |
|     6 | Planar convex domains          | Remove $\varepsilon$-loss; convex geometry; Riesz means                       | Restricted convex theorem; eventual full convex program |

---

## 5. Technical toolkit to build

The core toolkit should be organized around five pillars.

**Special functions.** For disks, balls, annuli, and shells: Bessel functions, derivatives, ultraspherical Bessel functions, cross-products, Debye–Olver asymptotics, Airy transition analysis, and monotonicity of phase functions. For ellipses: angular Mathieu functions, radial Mathieu functions, characteristic values, coupled spectral/separation parameters, and eccentricity-uniform asymptotics.

**Lattice counting.** Needed tools include Euler–Maclaurin summation, floor sums, trapezoidal floor sums, van der Corput estimates, convex/concave lattice-region estimates, boundary corrections, and multiplicity-weighted counts.

**Variational spectral theory.** Use min–max, Dirichlet domain monotonicity, bracketing, Riesz means, Legendre transforms, and comparison domains. The reports emphasize that Dirichlet is usually the cleaner first target because Dirichlet eigenvalues have useful monotonicity under inclusion.

**Explicit Weyl remainders.** Develop one-sided estimates strong enough to produce a computable threshold $\Lambda_0$. This is essential because asymptotic Weyl expansions alone do not imply Pólya.

**Rigorous computation.** Use interval/ball arithmetic, certified special-function evaluation, root enclosures, MPS or boundary-integral validation, and finite-window verification.

---

## 6. Recommended immediate next steps

Start by reproducing the FLPS disk/ball argument, then the annulus argument, and run or fork the available verification scripts. In parallel, begin a self-contained Mathieu-enclosure project, because that is the bottleneck for ellipses and is potentially publishable even before the full Pólya theorem. The uploaded report explicitly recommends reading FLPS balls, the Bessel-phase paper, the annulus paper, Filonov’s convex Neumann paper, and Jiang–Lin, then starting the Mathieu enclosure paper and sanity-checking ellipse numerics with MPS and interval arithmetic.

My concrete recommendation is:

$$
\boxed{
\text{Main first theorem: Dirichlet Pólya for spherical shells in } \mathbb R^3.
}
$$

$$
\boxed{
\text{Parallel flagship preparation: certified Mathieu phase enclosures for ellipses.}
}
$$

$$
\boxed{
\text{Fallback route: Jiang–Lin-style certified theorem for a smooth non-tiling comparison family.}
}
$$

This gives a balanced portfolio: one tractable theorem, one high-impact flagship path, and one lower-risk certificate route.
