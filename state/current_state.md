# Current State

Initialized for the Pólya AI collaboration.

The authoritative graph is `state/proof_obligations.yml`. The primary target is exact Dirichlet Pólya for 3D spherical shells.

Next run id: `polya-main`.

## Current theorem boundary

The repository proves the exact separated spectrum, the shell inequality at
high energy uniformly for all $0<\rho<1$, and both complete uniform endpoint
neighborhoods

$$
\rho\in(0,\rho_*]\cup[99/100,1),
\qquad K\ge0.
$$

Here

$$
\rho_*
=\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}
=0.0310668242700667\ldots.
$$

On the intervening compact interval

$$
I_{14}=[\rho_*,99/100],
$$

the shell inequality is now also proved uniformly for every
$K\ge550^2$. Combining this compact result with the two endpoint theorems
gives the global analytic high-frequency theorem for every
$0<\rho<1$ and $K\ge550^2$. Round 14 lowers the Round 13 ceiling by the
exact factor $900^2/550^2=324/121>2$. The exact strict count is
independently interval-certified
on the closed central residual box

$$
\frac{999}{2000}\le\rho\le\frac{1001}{2000},
\qquad
\frac{67}{10}\le K\le\frac{168}{25}.
$$

The all-frequency shell theorem is not yet proved. Its active blockers are
exact coverage of the rest of the compact residual set below $550^2$ and
the final theorem-level audit. The next analytic target is a separately
proved central--thin seam extension to $\varepsilon\le1/6$ with candidate
$K\ge54/\varepsilon^2$, moved seam $\rho=5/6$, and separate target
$K_0(5/6)<295^2$. These are unproved Round 15 planning targets. The
prospective all-ratio ceiling is $K\ge200000$, because the retained
far-thin Round 10 zone would then dominate. Preliminary values
$d_0=5/8$, $\overline q=159/400$, and $B=14/3$ are planning evidence only.
The current $\kappa=53$ and $Y=294$ route obstructions are not disproofs of
either stronger statement. The parent certification obligation remains
`diagnostic_only`; any expansion is restricted to bounded, face-connected
extensions of the existing certified pilot.

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

## Round 8 Update

Date: 2026-07-13

See `rounds/polya-main/round_008/judge/judge-008.md`.

Round 8 proves a piecewise analytic envelope on the complete remaining
compact ratio interval. The left, central, and thin zone thresholds are
bounded respectively by $64$, $2^{35}$, and $2^{42}$, so

$$
\boxed{
\rho\in[\rho_*,1-2^{-18}],
\quad K\ge2^{42}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The analytic proof passed isolated reconstruction and adversarial review.
The certificate specification now distinguishes the closed planning
envelope $\mathcal E$ from the actual unproved set
$\mathcal D=(I_*\times[0,\infty))\setminus\mathcal A$, assigns analytic
faces explicitly, and permits safe monotone-corner bounds in place of
literal wall subdivision.

The first genuine residual certificate covers

$$
\rho\in[999/2000,1001/2000],
\qquad K\in[67/10,168/25].
$$

Arb determinant enclosures and an independent standard-library rational
checker prove the exact strict count is $4$, with Weyl margin greater than
$14.6073$. A separate audit reproduced the artifacts bit for bit and rejected
14 decisive tamper mutations. This local computation is certified, but the
parent compact computation remains `diagnostic_only` because the rest of
$\mathcal D$ is not covered.

## Round 9 Update

Date: 2026-07-13

See `rounds/polya-main/round_009/judge/judge-009.md`.

Round 9 replaces the Round 6 high-thin constant $64$ by the independently
reconstructed, self-consistent constant $125/8$. For
$0<\varepsilon\le1/100$, the shell inequality now holds whenever

$$
K\ge\frac{125}{8\varepsilon^2}.
$$

The proof controls the actual uncompensated plateau loss
$R=p-dm$ and establishes the strict bound
$R<361/(80\sqrt\varepsilon)$ without importing any estimate proved under
the old $C=64$ hypothesis. It passed isolated reconstruction, targeted
adversarial wall review, and a dependency audit.

The improved high range overlaps the aggregate-action range
$K\le1/(8\varepsilon^{5/2})$ exactly when
$\varepsilon\le1/15625$. Equality is included in both components and their
common threshold is $125^5/8$. Hence the complete thin endpoint enlarges to

$$
\boxed{
1-\frac1{15625}\le\rho<1,
\quad K\ge0.
}
$$

On the updated compact interval

$$
I_9=\left[\rho_*,1-\frac1{15625}\right],
$$

the left and central residual ceilings remain $64$ and $2^{35}$, while the
thin residual ceiling is

$$
\frac{125^5}{8}<2^{32}.
$$

Therefore the shell inequality holds for every $0<\rho<1$ when
$K\ge2^{35}$. The certified central pilot remains valid but local; the
parent compact certification, the remaining compact residual below
$2^{35}$, and the final all-frequency shell theorem remain open.

## Round 10 Update

Date: 2026-07-13

See `rounds/polya-main/round_010/judge/judge-010.md`.

Round 10 rederives the local-plateau argument on the enlarged domain
$0<\varepsilon\le1/25$ and proves

$$
K\ge\frac{20}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
$$

The proof passed frozen-dependency, isolated clean-room, and adversarial
review. It moves the central--thin seam to $\rho=24/25$. At that face the
fixed-ratio threshold satisfies

$$
K_0(24/25)<6000^2,
$$

while on $24/25\le\rho\le99/100$ the new high threshold is at most
$200000$. On the ultra-thin strip retain the sharper Round 9 threshold
$125/[8(1-\rho)^2]$. These closed zones yield the new global theorem

$$
\boxed{
0<\rho<1,
\quad K\ge\frac{125^5}{8}<2^{32}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Since $2^{35}>9(125^5/8)$, this is more than a ninefold reduction of the
Round 9 all-ratio ceiling. Round 10 does not enlarge the complete thin
endpoint: combining $C=20$ with the aggregate range overlaps only for
$\varepsilon\le1/25600$, so the stronger existing all-frequency statement
remains exactly $\varepsilon\le1/15625$.

The all-frequency theorem remains open on the compact residual below
$125^5/8$. Round 11 should first target the dominant ultra-thin gap

$$
\frac1{15625}<\varepsilon\le\frac1{100},
\qquad
\frac1{8\varepsilon^{5/2}}
<K<
\frac{125}{8\varepsilon^2},
$$

aiming to lower its ceiling below $6000^2$.

## Round 11 Update

Date: 2026-07-13

See `rounds/polya-main/round_011/judge/judge-011.md`.

Round 11 proves the direct complementary-action theorem

$$
0<\varepsilon\le\frac1{100},
\qquad
a=\varepsilon K\ge\frac1{8\varepsilon^{3/2}}.
$$

Writing $F=R^2$ for the squared inverse exact action, the incumbent controls
the shifted radial discrepancy by the U-shaped derivative magnitude and a
periodic sawtooth. After exact half-integer angular ceilings it retains the
strict normalized reserve $61/1400$. An isolated clean-room proof obtains
the different reserve

$$
D\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}
$$

and the exact margin
$4119252993/17500000000>0$. Both proofs preserve radial, angular, proxy,
interface, and strict spectral walls.

The accepted product and aggregate ranges cover the complementary closed
range, so

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

This enlarges the thin endpoint width in $\varepsilon$ by the exact factor
$625/4$. Combined with the Round 10 seam and
$K_0(24/25)<6000^2$, it yields

$$
\boxed{
0<\rho<1,
\qquad K\ge6000^2.
}
$$

The global ceiling is now more than $105$ times below $125^5/8$ and more
than $954$ times below $2^{35}$. The compact all-frequency residual below
$6000^2$, the parent Bessel certification, uniformity, and the final shell
target remain open.

## Round 12 Update

Date: 2026-07-13

See `rounds/polya-main/round_012/judge/judge-012.md`.

Round 12 rederives the local-plateau theorem on the enlarged domain

$$
0<\varepsilon\le\frac1{20},
\qquad
K\ge\frac{24}{\varepsilon^2},
$$

including threshold equality. The incumbent proves the scaled loss bound
$R<23/(5\sqrt\varepsilon)$; an isolated clean-room reconstruction instead
proves $R<5/\sqrt\varepsilon$ by excluding a complete rectangle in the
synthetic variables. A third independent finite-constant route also closes.
All exceptional branches, strict walls, and shared faces passed adversarial
review and exact-ledger reproduction.

At the moved seam $\rho=19/20$, the defining fixed-ratio quadratic has

$$
K_0(19/20)<3300^2,
$$

with exact positive margin $32985481/7422975$ at its square-root test point.
The closed analytic union therefore proves

$$
\boxed{
0<\rho<1,
\qquad K\ge3300^2.
}
$$

The complete all-frequency endpoint remains exactly
$99/100\le\rho<1$. The compact residual below $3300^2$, the parent Bessel
certification, uniformity, and the final shell target remain open.

## Round 13 Update

Date: 2026-07-14

See `rounds/polya-main/round_013/judge/judge-013.md`.

Round 13 rederives the local-plateau theorem on the enlarged domain

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2},
$$

including threshold equality. The incumbent and independent constant
inventory prove

$$
d>\frac23,
\qquad
\widehat q<\frac37,
\qquad
R<\frac{14}{3\sqrt\varepsilon},
$$

with exact synthetic endpoint reserve
$2376966388822/5818105805625$ and payment reserve
$170244091/27217575$. The strictly isolated reconstruction uses a different
direct localization and affine synthetic path, with exact derivative reserve
$229/2646$. All exceptional branches, strict walls, and shared faces passed
fresh adversarial review and exact-ledger reproduction.

At the moved seam $\rho=9/10$, the defining fixed-ratio quadratic has

$$
K_0(9/10)<900^2,
$$

with exact positive margin $6897151/18725$ at its square-root test point.
The closed five-zone analytic union therefore proves

$$
\boxed{
0<\rho<1,
\qquad K\ge900^2.
}
$$

The complete all-frequency endpoint remains exactly
$99/100\le\rho<1$. The compact residual below $900^2$, the parent Bessel
certification, uniformity, and the final shell target remain open.

## Round 14 Update

Date: 2026-07-14

See `rounds/polya-main/round_014/judge/judge-014.md`.

Round 14 proves the enlarged local-plateau theorem

$$
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2},
$$

including threshold equality. The sharper Round 13 threshold
$24/\varepsilon^2$ remains authoritative for
$0<\varepsilon\le1/10$, and the still sharper Round 10 threshold
$20/\varepsilon^2$ remains authoritative for
$0<\varepsilon\le1/25$. At the moved seam $\rho=7/8$, the defining
fixed-ratio threshold satisfies

$$
K_0(7/8)<550^2.
$$

The tested attempt to retain $\kappa=24$ proves only
$x_0/K>173/384$, while $173/384<1/2$; hence this lower bound does not
localize beyond $1/2$. This is a route obstruction, not a rejection or
counterexample to a stronger seam theorem.

On

$$
I_{14}=[\rho_*,99/100],
$$

the closed six-zone analytic union has respective residual ceilings below
$64$, below $K_0(\rho)\le K_0(7/8)<550^2$, below $3200$, below $9600$,
below $15000$, and below $200000$. Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge550^2
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

This lowers the Round 13 global ceiling by the exact factor
$900^2/550^2=324/121>2$. The complete all-frequency endpoint remains
exactly $99/100\le\rho<1$. The compact residual below $550^2$, the parent
Bessel certification, uniformity, and the final shell target remain open;
the existing certificate remains diagnostic only.
