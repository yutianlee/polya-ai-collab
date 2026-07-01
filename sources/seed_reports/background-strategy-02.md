# Strategic blueprint: Dirichlet Pólya for the ellipse

Because Nikolay Filonov recently resolved the Neumann case for all planar convex domains (*Comm. Pure Appl. Math.*, 2025), the **Dirichlet case for the ellipse** is now the premier immediate target in this direction. Resolving it would provide a concrete blueprint for the Dirichlet problem on arbitrary smooth convex domains.

---

## 1. Problem setting

**The domain.**
Let $\Omega \subset \mathbb{R}^2$ be a planar ellipse with semi-major axis $a$ and semi-minor axis $b$ (where $a > b > 0$). The area of the ellipse is $|\Omega| = \pi a b$.

**The spectral problem.**
Consider the Dirichlet eigenvalue problem for the negative Laplace operator, which physically models the vibrational frequencies of an elliptical drumhead:
$$ -\Delta u = \lambda u \quad \text{in } \Omega, \quad \text{with } u = 0 \text{ on } \partial\Omega $$
This operator possesses a discrete spectrum of strictly positive eigenvalues: $0 < \lambda_1 \le \lambda_2 \le \lambda_3 \le \dots \to \infty$.

**The counting function and Weyl's law.**
The Dirichlet eigenvalue counting function is defined as $N_D(\lambda) = \#\{k \mid \lambda_k \le \lambda\}$.
In 1912, Hermann Weyl proved that the asymptotic distribution of these eigenvalues is dictated entirely by the phase-space volume of the domain. In two dimensions, Weyl's Law states that the leading term is:
$$ N_D(\lambda) \sim \mathcal{W}(\lambda) := \frac{|\Omega|}{4\pi}\lambda = \frac{a b}{4}\lambda \quad \text{as } \lambda \to \infty $$

**Pólya’s conjecture (1954).**
George Pólya hypothesized that this asymptotic limit is actually a pointwise universal upper bound for all $\lambda > 0$, not just as $\lambda \to \infty$. Specifically, for the Dirichlet ellipse, the conjecture states:
$$ N_D(\lambda) \le \frac{ab}{4}\lambda \quad \text{for all } \lambda > 0 $$
Equivalently, expressed in terms of individual eigenvalues, this requires bounding every single eigenvalue from below: $\lambda_k \ge \frac{4k}{ab}$.

---

## 2. Background and recent progress

**The historical stagnation (1961–2022).**
In 1961, Pólya proved his conjecture for "tiling" domains (squares, rectangles, equilateral triangles, and hexagons). By exploiting translation invariance, he embedded these domains into a periodic lattice and used the orthogonality of Fourier bases to prove the bound. For over 60 years, the pointwise conjecture remained entirely open for *non-tiling* domains. The best available results were the Berezin–Li–Yau inequalities (1983), which proved the conjecture only "on average" (i.e., the Riesz means of the eigenvalues), but not pointwise.

**The paradigm shift (2023–2025).**
Recent progress has changed the landscape through a hybrid analytical-computational methodology introduced by Filonov, Levitin, Polterovich, and Sher:

* **The Disk (2023):** The team published a landmark paper in *Inventiones Mathematicae* proving the Dirichlet conjecture for the Euclidean disk—making it the first non-tiling domain in history to be solved.
* **The Annulus (2025):** The same authors extended the proof to the annulus, marking the first multiply-connected domain to be solved.
* **Convex Neumann Resolved (2025):** Filonov independently proved the Neumann case for all planar convex domains (*CPAM*).

**Why the Dirichlet ellipse matters.**
The disk and annulus proofs relied heavily on the fact that those domains possess continuous rotational ($S^1$) symmetry. This symmetry allows the 2D PDE to separate cleanly into 1D Bessel equations, making the eigenvalues dependent on a single variable (the radius).

The ellipse is the simplest convex domain that breaks continuous rotational symmetry. Solving the ellipse requires moving from single-variable Bessel functions to multi-parameter **Mathieu functions**. Proving the conjecture here would show that the modern machinery can survive anisotropic geometry and continuous eccentricity, and it would establish a template for the Dirichlet case on smooth convex domains.

---

## 3. Solving strategy

A workable proof should use an **analytic-numeric divide** adapted to elliptical coordinates. The spectrum is split into a **high-energy asymptotic regime** and a **low-energy certified-computation regime**.

### Step A: Separation in elliptic coordinates

Define elliptic coordinates $(\mu, \nu)$, where $x = c \cosh \mu \cos \nu$ and $y = c \sinh \mu \sin \nu$. The focal distance is $2c = 2\sqrt{a^2-b^2}$. The boundary of the ellipse is defined by a constant radial coordinate $\mu = \mu_0$. The Helmholtz equation $-\Delta u = \lambda u$ separates into two coupled ordinary differential equations:

1. **Angular Mathieu Equation:** $\Theta''(\nu) + (\alpha - 2q \cos 2\nu)\Theta(\nu) = 0$
2. **Radial (Modified) Mathieu Equation:** $R''(\mu) - (\alpha - 2q \cosh 2\mu)R(\mu) = 0$

Here, $q = \frac{c^2 \lambda}{4}$ is the spectral parameter, and $\alpha$ is the separation constant (characteristic value).

### Step B: High-energy regime

For large $\lambda$ (large $q$), numerics alone cannot support a proof; analytic estimates must control the tail.

1. **Phase Enclosures:** The eigenvalues are determined by the simultaneous roots of the radial and angular Mathieu functions. One must establish explicit upper and lower algebraic curves (phase enclosures) for the roots of these Mathieu functions.
2. **Lattice Point Counting:** Map the eigenvalues into a 2D phase-space $(\alpha, q)$. The counting function $N_D(\lambda)$ transforms into the geometric problem of counting integer lattice points inside a region bounded by the Mathieu phase enclosures.
3. **Area-to-Lattice Bounds:** Prove that for $\lambda > \lambda_{\text{cutoff}}$, the number of lattice points enclosed by the Mathieu curves is strictly less than or equal to the continuous area integral corresponding to Weyl's term $\mathcal{W}(\lambda)$.

### Step C: Low-energy regime

Because asymptotic phase bounds have error terms, they do not guarantee the inequality at low energies. For all eigenvalues below the calculated threshold, for instance $\lambda \le \lambda_{\text{cutoff}}$, the conjecture must be verified by certified computation.

* Compute the first $N$ eigenvalues of the ellipse.
* Because standard floating-point computation has rounding error and is not proof-grade by itself, use **computer-assisted rigorous interval arithmetic** to guarantee that the true eigenvalue satisfies $\lambda_k \ge 4k/(ab)$.

---

## 4. Techniques involved

Executing this strategy requires a highly multidisciplinary synthesis of classical PDE analysis, geometric number theory, and rigorous computer science.

### 4.1 Asymptotics of Mathieu functions

Unlike Bessel functions $J_n(r)$, Mathieu functions depend on the interlocking parameters $(\alpha, q)$.

* **Technique:** Use uniform asymptotic expansions (WKB / Liouville-Green approximations) for the characteristic values of the Mathieu equation.
* **Obstacle:** Standard $\mathcal{O}(q^{-1/2})$ remainder terms are not enough. To construct the bounding box for lattice counting, one needs *strictly explicit* error bounds with computable constants, such as $\text{error} \le C q^{-1/2}$ with known $C$. This requires F.W.J. Olver’s uniform asymptotic theory for turning points.

### 4.2 Exact lattice-point counting

The analytical half of the proof reduces to a problem akin to the Gauss Circle Problem.

* **Technique:** Use Euler-Maclaurin summation to convert discrete sums to integrals, along with Fourier-analytic bounds on the fractional parts of curves (stationary phase / van der Corput lemmas for oscillatory integrals).
* **Obstacle:** Prove that the geometric "bulges" in the phase-space curves generated by the ellipse's eccentricity do not capture more integer lattice points than a perfect circle of the same area would.

### 4.3 Rigorous computer-assisted proofs

The low-frequency verification requires computational methods that constitute a formal mathematical theorem.

* **Method of Particular Solutions (MPS):** To compute eigenvalues without the meshing errors of finite element methods, approximate eigenfunctions as linear combinations of exact solutions to the Helmholtz equation (Mathieu modes or Fourier-Bessel modes) and minimize the residual error strictly on the boundary.
* **Interval Arithmetic (IA):** All calculations must be wrapped in IA libraries (like the **Arb** C-library or Julia's `IntervalArithmetic.jl`). IA represents numbers as strict intervals (e.g., $[2.1145, 2.1146]$) to account for all truncation and round-off errors.
* **A-posteriori Error Bounds:** Apply Newton-Kantorovich theorems, such as Moler–Payne bounds, which guarantee that if a function has small boundary error, a true eigenvalue exists within a computable radius of the approximated $\lambda$.

### 4.4 The eccentricity continuum

An ellipse is a 1-parameter family defined by its eccentricity $e \in (0, 1)$. The proof must be stitched together uniformly across all eccentricities.

* **Technique:** For near-circles ($e \approx 0$), use domain monotonicity ($\Omega_1 \subset \Omega_2 \implies \lambda_k(\Omega_1) \ge \lambda_k(\Omega_2)$) to piggyback on the known proof for the disk. For highly eccentric ellipses ($e \to 1$), the domain behaves like a thin strip where the 1D approximation holds. The main challenge is stitching the analytic bounds across intermediate eccentricities without allowing the error terms to explode.
