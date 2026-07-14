# Current State

Initialized for the Pólya AI collaboration.

The authoritative graph is `state/proof_obligations.yml`. The primary target is exact Dirichlet Pólya for 3D spherical shells.

Next run id: `polya-main`.

## Current theorem boundary (Round 19)

The authoritative graph is the already-applied Round 19 graph, SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.
The exact separated spectrum, both endpoint theorems, and the global
high-frequency theorem from earlier rounds remain in force. Round 19 adds a
two-sided low-frequency staircase. Put

$$
\rho_c=\frac1{1+2\pi},\qquad
\rho_0=\frac1{\sqrt{337}},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},\qquad
d=\frac{\sqrt{337}}2,
\qquad
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The repository now proves both closed-frequency conclusions

$$
\boxed{\rho_c\le\rho\le\frac78,\quad z_\rho\le K\le k_6(\rho)}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K),
$$

and

$$
\boxed{\rho_0<\rho<\rho_c,\quad L(\rho)<K\le d}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K).
$$

Relative to the historical Round 18 cover, the genuinely new set is

$$
\mathcal C_{19}=
\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}
\cup
\{\rho_c\le\rho<7/8,\ k_5(\rho)<K\le k_6(\rho)\}.
$$

Thus the live analytic cover and the exact live residual are

$$
\boxed{\begin{aligned}
\mathcal A_{19}=\mathcal A_{18}
&\cup\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}\\
&\cup\{\rho_c\le\rho\le7/8,\ z_\rho\le K\le k_6(\rho)\},
\end{aligned}}
$$

and

$$
\boxed{\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

The split at $\rho=\rho_0$ is exact: $L(\rho_0)=d$, so the candidate
fiber is empty and that ratio slice stays in the first component. The faces
$K=d$ and $K=k_6$ are covered; $K=U$, $\rho=\rho_*$, and $\rho=7/8$
retain their inherited owners, while $\rho=\rho_c$ belongs to the high
band. The already absorbed boxes $B_0,B_1$ remain regression evidence and
are not subtracted again.

The external source increment is deliberately narrow. The qualified
obligation `SRC-ROUND19-BESSEL-ZEROS` supplies only Lorch's strict
specialization

$$
j_{11/2,1}>\frac{17}{2}
$$

and the positive spherical/ordinary Bessel identification. The exact
reduction has reserve
$507^2\cdot77-4264^2=1611077>0$. The bounds
$j_{3/2,2}>77/10$ and $j_{5/2,2}>9$ are reconstructed internally. So are
fixed-channel zero extension and shell-to-ball min--max,

$$
q_{\ell,n}^{\rm shell}(\rho)\ge j_{\ell+1/2,n},
$$

the ball angular shift

$$
j_{p+1/2,n}^2\ge j_{\ell+1/2,n}^2+p(p+1)-\ell(\ell+1),
\qquad p>\ell,
$$

and all shell exclusions, multiplicities, and Weyl payments. No shell
cross-product zero is imported. The high-band caps are
$4,9,16,25,26,29,36$; the lower-band caps are
$1,4,9,10,16,17,26,29,40,45$.

The residual is demonstrably nonempty. At $\rho=1/2$,

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2),
$$

so $(1/2,30)\in\mathcal D_{19}$. Consequently
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` remain `open`; `COMP-certified-bessel` remains
`diagnostic_only`.

All Round 19 promotion gates passed: 13 exact residual checks, 245 exact
staircase checks, 37 residual-focused and 24 staircase-focused tests, the
pre-application suite at 193 tests plus 10 subtests, 50-file source
compilation, graph validation, and `git diff --check`.  After promotion, the
current suite passes 195 tests and 10 subtests with one strict expected
failure: the immutable freeze test deliberately compares the now-advanced
live state paths with their pre-promotion hashes.  Three lifecycle tests
authenticate those hashes from the baseline Git objects instead. Round 20
must freeze this exact $\mathcal D_{19}$ before freezing or reviewing any
candidate.

## Historical boundary through Round 18

The repository proves the exact separated spectrum, the shell inequality at
high energy uniformly for all $0<\rho<1$, and both complete uniform endpoint
neighborhoods

$$
\rho\in(0,\rho_*]\cup[7/8,1),
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
I_{16}=[\rho_*,7/8],
$$

the shell inequality is proved uniformly for every
$K\ge295^2=87025$, including equality. Combining this compact result with
the two endpoint theorems gives the global analytic high-frequency theorem
for every $0<\rho<1$ and $K\ge295^2$. Relative to the Round 15 ceiling, the
exact reduction factor is

$$
\frac{200000}{295^2}=\frac{8000}{3481}>2.
$$

The new thin endpoint uses $\varepsilon=1-\rho$ and
$a=\varepsilon K$. Its product low piece and complementary-action high
piece meet inclusively at

$$
a=\frac{\pi}{4\varepsilon}.
$$

Both pieces own this shared face and retain the exact reserves $577/2880$
and $143/4096$, respectively.
The lower face $\rho=7/8$ is included, the limiting face $\rho=1$ is open,
$K=0$ gives equality, and the proof comparison is strict for $K>0$ before
the final non-strict theorem statement.

The Round 16 four-zone integration remains the high-energy envelope. Rounds
17--18 added the historical low-frequency angular staircase. Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}\quad(m\in\mathbb N_0).
$$

By the end of Round 18, the strict shell inequality was proved on the band

$$
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_5(\rho).
$$

The lower frequency face and the face $\rho=7/8$ retain their previous
analytic owners; $K=k_2(\rho)$ retains its Round 17 owner, and the new
$K=k_5(\rho)$ face is included. The genuinely new Round 18 portion is

$$
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K\le k_5(\rho)
\right\}.
$$

It lies inside the exact Round 17 analytic residual. If $\mathcal A_{17}$
is that historical cover, the Round 18 cover and historical post-Round-18
residual were

$$
\mathcal A_{18}
=\mathcal A_{17}\cup
\left\{\rho_c\le\rho\le\frac78,
\ z_\rho\le K\le k_5(\rho)\right\},
\qquad
\mathcal D_{18}=\mathcal D_{17}\setminus\mathcal C_{18},
$$

or, equivalently,

$$
\boxed{\mathcal D_{18}
=\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\le\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.}
$$

where the exact upper floor retained from the frozen residual is

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\le\rho<7/8.
\end{cases}
$$

The Round 18 proof keeps the shell-specific steps internal. In particular,
zero extension in a fixed angular subspace and min--max give the first
inequality, while the audited unit-ball separation identifies the endpoint:

$$
\lambda_{\ell,1}^{\rm shell}(\rho)
\ge\lambda_{\ell,1}^{\rm ball}=j_{\ell+1/2,1}^2,
$$

while Lorch supplies only the audited external bounds

$$
j_{5/2,1}>\frac{51}{10},\qquad
j_{7/2,1}>\frac{13}{2},\qquad
j_{9/2,1}>\frac{15}{2}.
$$

The publisher abstract exposes those strict statements and their scope
$\nu>-1$, but the full paper was access-controlled; no shell cross-product,
channel comparison, radial exclusion, multiplicity, or Weyl estimate is
attributed to Lorch. Together with
$\lambda_{\ell,n}^{\rm shell}\ge n^2z_\rho^2+\ell(\ell+1)$, these delayed
entries give the cumulative strict-count caps $4,9,16,25$. The ratio splits are
$3/10,1/2,1/2$, with exact lower Weyl reserves

$$
\frac{100387329}{11000000}>9,\qquad
\frac{107653}{6336}>16,\qquad
\frac{18375}{704}>25.
$$

The moving-wall payments are strictly increasing. The upper-floor audit
gives $k_5<26<64<K_0$ on the active $K_0$ branch and
$k_5<26<1944\le54/(1-\rho)^2$ on the seam branch, so $k_5<U$ everywhere
on the new ratio interval.

Both closed central boxes

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right],
\qquad
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right]
$$

are independently certified with exact strict count $4$. They satisfy
$B_0\cup B_1\subset\mathcal C_{17}$, so they remain valuable independent
regression evidence but provide no additional subtraction from
$\mathcal D_{18}$. The parent certification obligation remains
`diagnostic_only`.

At the end of Round 18, the all-frequency shell theorem was not proved and
its shell blocker was the nonempty two-piece set $\mathcal D_{18}$.
This is historical bookkeeping, superseded by the live $\mathcal D_{19}$.
The then-used witness was

$$
k_5(1/2)<26<30<64<K_0(1/2)=U(1/2),
$$

so $(1/2,30)\in\mathcal D_{18}$. The same targets remain open now for the
strictly smaller live residual $\mathcal D_{19}$.

At the left ratio face,

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
$$

The exact $\ell=0,n=2$ frequency enters immediately above $2z_{\rho_c}$.
Thus the one-radial-mode cap could not simply be continued to $k_6$; this
was the Round 18 method boundary, not a counterexample. Round 19 has now
resolved that wall and also reduced the lower-ratio component.

The stretch endpoint screens at $\rho=6/7$ and $\rho=23/27$ are unproved.
The negative screens at $\rho=17/20$ and $\rho=5/6$ obstruct only their
tested proof routes, not the shell inequality or any accepted theorem.

Round 15 also records two proof-route obstructions: the selected
$\kappa=53$ localization proxy misses by $14293/15900000$, and the selected
$Y=294$ central proxy equals $-307/175$. Neither is a counterexample to the
accepted seam theorem or to a stronger endpoint statement.

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

## Round 15 Update

Date: 2026-07-14

See `rounds/polya-main/round_015/judge/judge-015.md`.

Round 15 proves the enlarged central--thin seam theorem

$$
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2},
$$

including threshold equality. The sharper retained thresholds are
$32/\varepsilon^2$ for $0<\varepsilon\le1/8$,
$24/\varepsilon^2$ for $0<\varepsilon\le1/10$, and
$20/\varepsilon^2$ for $0<\varepsilon\le1/25$. At the moved seam
$\rho=5/6$, the fixed-ratio threshold satisfies

$$
K_0(5/6)<295^2=87025.
$$

On $I_{15}=[\rho_*,99/100]$, the closed seven-zone analytic union has
residual ceilings below $64$ on $[\rho_*,1/16]$, below
$K_0(\rho)\le K_0(5/6)<87025$ on $[1/16,5/6]$, below $3456$ on
$[5/6,7/8]$, below $3200$ on $[7/8,9/10]$, below $9600$ on
$[9/10,19/20]$, below $15000$ on $[19/20,24/25]$, and below $200000$ on
$[24/25,99/100]$. Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge200000
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

This lowers the Round 14 global ceiling by the exact factor
$550^2/200000=121/80>1$. The complete all-frequency endpoint remains
exactly $99/100\le\rho<1$. The true nonrectangular residual
$\mathcal D_{15}$ below the analytic cover, the parent Bessel
certification, uniformity, and the final shell target remain open; replacing
$\mathcal D_{15}$ by the rectangle $I_{15}\times[0,200000)$ would be an
invalid enlargement of the certification target.

At the close of Round 15, the next round was to test the then-unproved
endpoint extension
$7/8\le\rho<1$ using a two-piece split at
$a=\pi/(4\varepsilon)$. The candidate reserves are $577/2880$ and
$143/4096$. If the endpoint theorem passes independent reconstruction and
audit, the conditional global ceiling is $295^2$, an exact improvement
factor $8000/3481$ over $200000$.

## Round 16 Update

Date: 2026-07-14

See `rounds/polya-main/round_016/judge/judge-016.md`.

Round 16 proves the complete thin endpoint

$$
\boxed{
\frac78\le\rho<1,
\qquad K\ge0.
}
$$

With $\varepsilon=1-\rho$ and $a=\varepsilon K$, the proof joins a product
low piece to a complementary-action high piece at
$a=\pi/(4\varepsilon)$, with both pieces owning the shared face. The exact
reserves are $577/2880$ and $143/4096$.
The lower face $\rho=7/8$ is included, $\rho=1$ remains open, $K=0$ is an
equality case, and the proof comparison is strict for $K>0$ before the final
non-strict theorem statement.

On $I_{16}=[\rho_*,7/8]$, the four-zone analytic union has residual ceilings
below $64$ on $[\rho_*,1/16]$, below
$K_0(\rho)\le K_0(5/6)<295^2$ on $[1/16,5/6]$, below
$54/(1-\rho)^2\le3456$ on $[5/6,7/8]$, and no residual on
$[7/8,1)$. Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge295^2=87025
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Threshold equality is included, and the exact reduction from the Round 15
ceiling is $200000/295^2=8000/3481>2$. The sole remaining shell blocker is
the true nonrectangular set
$\mathcal D_{16}=(I_{16}\times[0,\infty))\setminus\mathcal A_{16}$, not the
rectangle $I_{16}\times[0,87025)$. `COMP-certified-bessel` remains
`diagnostic_only`, and the Round 8 certified pilot remains unchanged and
local.

## Round 17 Update

Date: 2026-07-14

See `rounds/polya-main/round_017/judge/judge-017.md`.

Round 17 freezes the exact Round 16 mask and proves the first-angular-band
compression

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
\frac{\pi}{1-\rho}\le K
\le\sqrt{\left(\frac{\pi}{1-\rho}\right)^2+6},
\qquad
\rho_c=\frac1{1+2\pi}.
}
$$

The proof uses the radial min--max bound

$$
\lambda_{\ell,n}
\ge n^2\left(\frac{\pi}{1-\rho}\right)^2+\ell(\ell+1)
$$

and the exact $\ell=0$ interval spectrum. Strict counting gives count $0$
on the lower wall, count $1$ through the first angular wall, and count at
most $4$ through the inclusive $\ell=2$ comparison wall. Exact Weyl
payments exceed $1$ and $4$, respectively. The frozen claim passed an
isolated reconstruction, an independent exact-constant audit, and a fresh
adversarial referee review.

The genuinely new band $\mathcal C_{17}$ is an exact subset of
$\mathcal D_{16}$ and contains both independently certified boxes $B_0$
and $B_1$. Thus the theorem-wise uncovered set is exactly

$$
\mathcal U_{17}=\mathcal D_{17}
=\mathcal D_{16}\setminus\mathcal C_{17},
$$

with its historical two-piece formula retained in the Round 17 state and
judge artifacts.
The full shell theorem, compact-ratio uniformity, and
`SHELL-rho-compact` remain open.

Immediately above $k_2(\rho)$, the same coarse comparison must allow the
$\ell=2$ multiplicity, so its cap jumps from $4$ to $9$. At
$\rho=\rho_c$ the Weyl term at $k_2(\rho_c)$ is strictly below $9$.
This was the historical Round 17 obstruction to the coarse payment method,
not a counterexample to the shell inequality. Round 18 resolves it through
$k_5$ by delaying the first $\ell=2,3,4$ entries; it is not a current gap.

## Round 18 Update

Date: 2026-07-14

See `rounds/polya-main/round_018/judge/judge-018.md`.

Round 18 promotes the independently reconstructed closed staircase

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad z_\rho\le K\le k_5(\rho),
\qquad k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
}
$$

Its new portion is exactly
$\mathcal C_{18}=\{\rho_c\le\rho<7/8,
k_2(\rho)<K\le k_5(\rho)\}\subset\mathcal D_{17}$. Fixed-channel zero
extension gives the internal shell-to-ball comparison. The only new
external input is the statement-level Lorch dependency at orders
$5/2,7/2,9/2$; the access-controlled proof is not claimed and no
shell-specific conclusion is imported. Delayed entry thresholds
$51/10,13/2,15/2$, ratio splits $3/10,1/2,1/2$, caps $4,9,16,25$, and the
exact payments recorded in the current theorem boundary prove the strict
comparison through the inclusive $K=k_5$ face. The audit also proves
$k_5<U$ on every active upper-floor branch.

Exact subtraction gave the historical post-Round-18 uncovered set
$\mathcal U_{18}=\mathcal D_{18}$ displayed above. The boxes $B_0,B_1$
remain valid regression certificates inside $\mathcal C_{17}$ and are not
subtracted again. The witness $(1/2,30)$ proved that this historical
$\mathcal D_{18}$ was nonempty. Round 19 supersedes this routing by the
live $\mathcal D_{19}$. At $\rho_c$ the ordering
$k_5<2z<k_6$ marked the historical Round 18 radial-entry method boundary;
it was not a spectral counterexample, and Round 19 resolves it through
$k_6$.

## Round 19 Update

Date: 2026-07-14

See `rounds/polya-main/round_019/judge/judge-019.md` and
`rounds/polya-main/round_019/reviews/state-patch-final-audit.md`.

Round 19 promotes `SRC-ROUND19-BESSEL-ZEROS` at
`proved_external_dependency` and `SHELL-two-sided-staircase` at
`proved_internal`. The source obligation contributes only
$j_{11/2,1}>17/2$ and the positive spherical/ordinary identification.
The second-zero bounds $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$, both
variational comparisons, the angular shifts, inventories, multiplicities,
and strict Weyl payments are internal.

The promoted theorem bands are

$$
\rho_c\le\rho\le7/8,\qquad z_\rho\le K\le k_6(\rho),
$$

and

$$
1/\sqrt{337}<\rho<\rho_c,\qquad
1/(2\rho)<K\le\sqrt{337}/2.
$$

Their exact new part is $\mathcal C_{19}$, and exact subtraction gives the
three-piece $\mathcal D_{19}$ in the live boundary above. The strict witness

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2)
$$

keeps every theorem-level target open and keeps the parent computation
obligation diagnostic. Independent reconstruction, exact arithmetic, source
audit, cross-comparison, and a fresh adversarial referee all passed. The
post-application graph is authoritative; Round 20 begins by freezing
$\mathcal D_{19}$ and may not promote any current exploratory note without
a proof-free claim freeze and the complete A3/A4/fresh-referee gate.
