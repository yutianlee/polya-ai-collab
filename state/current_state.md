# Current State

Initialized for the Pólya AI collaboration.

The authoritative graph is `state/proof_obligations.yml`. The primary target is exact Dirichlet Pólya for 3D spherical shells.

Next run id: `polya-main`.

## Current theorem boundary

The repository proves the exact separated spectrum, the shell inequality at
high energy for every fixed $0<\rho<1$, and both complete uniform endpoint
neighborhoods

$$
\rho\in(0,\rho_*]\cup[1-2^{-18},1),
\qquad K\ge0.
$$

Here

$$
\rho_*
=\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}
=0.0310668242700667\ldots.
$$

The all-$\rho$ shell theorem is not yet proved. Its active blockers are the
intervening compact-$\rho$ finite window, bounded certified closure, and the
final theorem-level audit.

## Round 1 Update

Timestamp: 2026-07-12 19:52:28

See `rounds/polya-main/round_001/judge/judge-001.md`.

State patch validation: created: SHELL-sturm-liouville-completeness, SHELL-exact-phase-rep, SHELL-phase-monotonicity, SHELL-count-floor-identity, SHELL-angular-cutoff, SHELL-inner-turning, SHELL-fixed-rho-high-energy, SHELL-weighted-lattice-fractional, SHELL-spherical-bessel-algebraic; updated: CONV-strict-counting, TARGET-shell-d3, SHELL-cross-product-formula, SRC-bessel-phase, SRC-annuli, SRC-shell-weyl, SRC-FLPS-balls, FLPS-disk-ball-reproduction, SHELL-phase-enclosures, SHELL-lattice-count, COMP-certified-bessel, SHELL-rho-uniformity, ELLIPSE-near-circular, CERT-certificate-family; rejected: A3-proposed-blocked-statuses, toy-weighted-fractional-test, raw-floating-point-computation-as-proof, bare-two-term-weyl-proof, judge1-progress-score-7; no_change: POLYA-program-target, SRC-mathieu-ellipse, SRC-jiang-lin; round score: 3; Structural de-risking only: exact monotone phase scaffold, a proved angular cutoff, and a proved counting convention; no shell Polya theorem and both quantitative blockers, inner-turning enclosure and 2D weighted lattice control, remain open. The final synthesis adopts judge2 calibration while importing judge1 completeness and diagnostic coverage.

## Round 2 Update

Date: 2026-07-12

See `rounds/polya-main/round_002/judge/judge-002.md`.

The Bessel-phase and annulus source audits are complete. The real-order annulus phase-difference estimate transfers to half-integer shell orders, with a global one-sided bound and a correlated $+1/4$ bound when $\nu\le\rho K$. A floating-point diagnostic prototype was added and remains non-certified. The next primary target is the $2\ell+1$ weighted lattice inequality; no Pólya theorem has been proved.

### Round 2 amendment

See `rounds/polya-main/round_002/judge/judge-002-amendment.md`.

The imported global phase enclosure passed incumbent, strictly isolated clean-room, and adversarial review and is now `proved_internal`. Its absolute $1/4$ slack remains untested under the $2\ell+1$ weighted sum, particularly as $\rho\to1$. This is now the primary analytic bottleneck.

The final graph-hygiene patch is recorded in `rounds/polya-main/round_002/judge/judge-002-cleanup.md`; it removes discharged prerequisites from blocker lists without changing any mathematical status.

## Round 3 Update

Date: 2026-07-12

See `rounds/polya-main/round_003/judge/judge-003.md`.

The exact weighted proxy, Weyl integral, square formulation, and $2\ell+1$ multiplicity-to-tail reduction passed incumbent, independent clean-room, and adversarial review. Every shifted tail beginning at or above the inner interface $\rho K$ is proved by the audited FLPS convex theorem. Nicholson's formula also gives the exact phase-level zero region $(1-\rho)K\le\pi$.

The full weighted lattice obligation remains open. Its sole active analytic blocker is now the shifted-tail inequality for starts below $\rho K$, where the shell action changes from concave to convex. The floating grid found no counterexample but remains diagnostic only. No shell Pólya theorem has been proved.

### Round 3 fixed-rho continuation

See `rounds/polya-main/round_003/judge/judge-003-fixed-rho.md`.

The low-interface bottleneck is closed in the fixed-$\rho$ high-energy range for every $0<\rho<1$. The proof bounds the initial constant-floor plateau by $O_\rho(\sqrt K)$ using the shell action's quantitative curvature, then uses the sharpened concave and convex trapezoidal estimates to obtain an $O_\rho(K)$ compensating margin. This gives an explicit $K_0(\rho)$ and promotes `SHELL-weighted-lattice-fractional` to `proved_internal`.

The eigenvalue-level fixed-$\rho$ result remains `derived_under_assumptions` because `SHELL-sturm-liouville-completeness` is open. The threshold is not uniform as $\rho\to1$, and the remaining parameter region is not certified. No shell Pólya theorem has been proved.

## Round 4 Update

Date: 2026-07-13

See rounds/polya-main/round_004/judge/judge-004.md.

The exact three-dimensional separated shell spectrum passed a frozen
incumbent proof, isolated clean-room reconstruction, and adversarial audit.
The Dirichlet Laplacian is now rigorously identified with the orthogonal
direct sum of the regular radial operators, including exact form and operator
domains, compactness of the infinite direct-sum resolvent, Bessel
cross-product normalization, positive-root simplicity, angular multiplicity,
cross-channel coincidences, and strict spectral endpoints.

Consequently the Round 3 weighted lattice theorem now gives an unconditional
eigenvalue result: for every fixed $0<\rho<1$, the shell Pólya inequality
holds for every $K\ge K_0(\rho)$. The full all-$K$, all-$\rho$ theorem remains
open because endpoint uniformity and interval-certified closure of the
residual finite region are not proved.

## Round 5 Update

Date: 2026-07-13

See rounds/polya-main/round_005/judge/judge-005.md.

Writing $\varepsilon=1-\rho$, the exact product comparison proves the actual
shell Pólya estimate uniformly for

$$
0<\varepsilon\le\frac1{100},
\qquad
0\le K\le\frac{\pi}{4\varepsilon^2}.
$$

The proof passed isolated clean-room, adversarial, and corrected constants
audits. It preserves strict radial and angular walls and uses the exact
$2\ell+1$ multiplicities.

The same round exactly disproves the flat product majorant as a global
thin-shell route. That majorant exceeds the shell Weyl target at infinitely
many parameter walls, including an exact family with
$\varepsilon\downarrow0$. This is not a counterexample to the shell theorem.

The remaining thin-shell gap is now explicit: a radius-sensitive estimate
must bridge the new low-optical theorem to the pointwise high-energy threshold
$K_0(1-\varepsilon)$. Small-hole analysis and interval certification also
remain open.

## Round 6 Update

Date: 2026-07-13

See `rounds/polya-main/round_006/judge/judge-006.md`.

Round 6 closes the entire $\rho\uparrow1$ endpoint analytically. The exact
scaled-action argument proves the shell inequality through

$$
K\le\frac1{8\varepsilon^{5/2}},
\qquad \varepsilon=1-\rho,
$$

while the local first-plateau argument proves it for

$$
K\ge\frac{64}{\varepsilon^2}.
$$

The ranges overlap exactly when $\varepsilon\le2^{-18}$; equality is included
on both sides. Therefore

$$
\boxed{
1-2^{-18}\le\rho<1,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Both components passed isolated clean-room reconstruction and adversarial
constants/wall review. No Bessel-root certificate is needed in this endpoint
neighborhood. The next primary analytic target is `SHELL-rho-zero-endpoint`;
the remaining compact interval and its bounded certificate are secondary.

## Round 7 Update

Date: 2026-07-13

See `rounds/polya-main/round_007/judge/judge-007.md`.

Round 7 closes the entire $\rho\downarrow0$ endpoint analytically. Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

If $\mu=\rho K\le1/2$, every shifted angular tail starts at or above the
inner interface and the proved convex-tail theorem applies. If $\mu>1/2$ and
$\rho\le\rho_*$, then

$$
K(\omega_0-\rho)
>\frac{\omega_0-\rho}{2\rho}
\ge C_*,
$$

so the previously reviewed small-hole low-interface theorem applies to all
remaining tails. The two regimes meet exactly at
$K_*=1/(2\rho_*)$ when $\rho=\rho_*$. Therefore

$$
\boxed{
0<\rho\le\rho_*,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The theorem passed isolated clean-room, adversarial constants/walls, and
integrated dependency audits. No ball-limit argument or small-hole Bessel
certificate is needed. Both endpoint obligations are now discharged; the
next target is the explicit compact interval
$[\rho_*,1-2^{-18}]$.
