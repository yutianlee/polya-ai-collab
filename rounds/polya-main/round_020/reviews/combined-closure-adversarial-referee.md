# Round 20 Combined-Closure Adversarial Referee

Date: 2026-07-15.

Verdict: **PASS / AUTHORIZE A JUDGE ONLY**.

First unsupported implication: **none**.

I began from the contrary hypothesis that the frozen combined-closure
candidate is false. I participated in neither the incumbent development nor
the isolated A3 reconstruction. I re-authenticated the released objects,
reconstructed the form comparisons and zero registry, challenged every lower,
staircase, and optical branch, reran the exact verifier and tests, and then
reperformed the residual subtraction. This PASS does not promote a theorem or
change state; it only releases the exact frozen candidate to a judge.

## 1. Authentication and review boundary

The requested review objects reproduce exactly:

| role | artifact | SHA-256 |
|---|---|---|
| frozen candidate | `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| external freeze | `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| replacement final-byte audit | `rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md` | `01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c` |
| isolated A3 | `rounds/polya-main/round_020/reviews/combined-closure-clean-room.md` | `7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb` |
| A3 corrective addendum | `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md` | `7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c` |
| independent zero audit | `rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md` | `2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8` |
| final A4 verifier | `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| final A4 tests | `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |
| final A4 report | `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95` |
| final A4 re-audit | `rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md` | `6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae` |
| cross-comparison | `rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md` | `4b7a7810a12177002f24a16ef60a206669e07fa29e80c3018d2b85add5d1099b` |

I independently extracted every path/hash pair printed in the candidate and
cross-comparison. There are 49 unique paths. All 49 exist and all 49 current
byte streams equal their displayed SHA-256; there is no missing, stale, or
silently replaced dependency. In particular, this includes:

- all five accepted residual artifacts, beginning with
  `SHELL-rho-compact-round20.md` at `a6222250...` and the residual classifier
  and tests at `5d33e0f2...` and `d261c89d...`;
- all ten permitted foundational packets/source cards, at the exact hashes
  `6fde758c...`, `96d0d466...`, `a4f56f86...`, `07133516...`,
  `5886997f...`, `95163883...`, `27ec69e8...`, `85f9a00...`,
  `ce035399...`, and `e1cbdef3...`;
- the five lower incumbent/cross-check artifacts at `f1e5ab1c...`,
  `94099e85...`, `0baea820...`, `ffde9721...`, and `d44e05b4...`;
- the complete high/zero chain at `d7bb5855...`, `30aea82a...`,
  `9ad5b481...`, `d12b7389...`, `b31a7b4d...`, `0e6fdadc...`,
  `9ec17b81...`, `9faa7b75...`, `515b57f7...`, `2534c1cb...`,
  `8a8dae42...`, `a0ac0c44...`, and `eee1ff26...`;
- the optical chain at `bbfc40bc...`, `06f3b9ef...`, `6e6eb668...`, and
  `d7a92ae4...`.

The replacement final-byte audit also establishes that the failed first
candidate release changed only its circular lifecycle prose. No theorem,
constant, cap, face, source scope, or falsification obligation changed in the
released candidate reviewed here.

## 2. Form domains, index directions, and zero provenance

For fixed angular channel, separation gives the one-dimensional form

$$
\mathfrak a_\ell[u]
=\int_\rho^1\left(|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak a_\ell)=H_0^1(\rho,1).
$$

The interval Poincare inequality and `r^{-2}>=1` give, at the same radial
index,

$$
q_{\ell,n}^2\ge n^2z_\rho^2+\ell(\ell+1),
\qquad q_{0,n}=nz_\rho.
$$

Zero extension maps this fixed-channel shell form domain into the unit-ball
fixed-channel domain `H_0^1(0,1)`. Min--max therefore has the required
direction

$$q_{\ell,n}^2\ge j_{\ell+1/2,n}^2,$$

without mixing angular channels or radial indices. Comparing the two ball
forms on their common domain gives, again at the same `n`,

$$
j_{p+1/2,n}^2\ge j_{\ell+1/2,n}^2
+p(p+1)-\ell(\ell+1),\qquad p\ge\ell.
$$

Hardy's inequality controls the singular ball form. These are form-domain
statements, not an invocation of unlabelled global domain monotonicity.

I reconstructed the eight internal half-integer bounds from the spherical
Bessel identity, explicit sine/cosine recurrence, tangent-cell signs, and
interlacing. Positive zeros are simple by ODE uniqueness. The zero at the
origin is never counted. The rational wall lies in the enumerated cell and on
the pre-root sign side in every row:

| bound | enumerated cell and conclusion |
|---|---|
| `j_(3/2,2)>77/10` | second `j_1` cell `(2 pi,5 pi/2)` |
| `j_(5/2,2)>9` | second `j_2` cell `(5 pi/2,3 pi)` |
| `j_(7/2,2)>103/10` | second `j_3` cell `(3 pi,7 pi/2)` |
| `j_(11/2,2)>129/10` | second `j_5` cell `(4 pi,9 pi/2)` |
| `j_(3/2,3)>21/2` | third `j_1` cell `(3 pi,7 pi/2)` |
| `j_(5/2,3)>61/5` | third `j_2` cell `(7 pi/2,4 pi)` |
| `j_(13/2,1)>10` | no `j_6` zero before the wall in `(3 pi,7 pi/2)` |
| `j_(15/2,1)>23/2` | no `j_7` zero before the wall in `(7 pi/2,4 pi)` |

The recurrence numerators are nonzero at every tangent endpoint, so a tangent
pole does not create or lose a root. Exact rational sine/cosine enclosures
give strict wall signs. The remaining first-zero bounds

$$
j_{17/2,1}>\frac{71}{6},\qquad
j_{19/2,1}>\frac{64}{5},\qquad
j_{21/2,1}>\frac{69}{5}
$$

follow from the qualified Lorch `(L2)` statement by positive-side radical
comparisons. Lorch is used only for first positive unit-ball zeros. It supplies
no higher radial zero, shell cross-product zero, angular propagation,
multiplicity, or payment. The labelled DLMF locations supply identities and
recurrences only, not zero locations. Thus every use stays inside the frozen
source boundary.

For the lower ledger, the stronger `103/10` wall implies `81/8`, and angular
propagation proves exactly the advertised exclusions through the included
`sqrt(114)` face: first modes `ell>=7`, second modes `ell>=5`, third modes
`ell>=2`, and every `n>=4` mode.

## 3. Lower closure

### 3.1 Shifted-tail wedge

For a low start `x_r=r+1/2<mu=rho K`, put

$$
n_r=\lfloor\mu-r-1/2\rfloor,
\qquad p=\lfloor\omega_0K\rfloor.
$$

The permitted concave/convex split, including the `n_r=0` case where the
concave block is absent, gives

$$
\frac{\mathcal T_r}{2}
\le \int_{x_r}^{K}A_{\rho,K}(z)\,dz
+\delta_r-\frac{p-n_r}{4},
$$

with

$$
0\le\delta_r\le
\frac{2(\mu-q_r)^{5/2}}{15\sqrt\mu}<\frac14.
$$

Exact threshold arithmetic gives `omega_0 d>1`. If `rho<=sigma=3
omega_0/4`, `K>d`, and `rho K>1/2`, then

$$
p-n_r\ge
\lfloor\omega_0K\rfloor-
\lfloor\rho K-r-1/2\rfloor\ge1.
$$

Hence every low tail is strict. This covers the complete first lower
component and the continuation `rho_0<=rho<=sigma, K>d`. At `rho=rho_0`,
`L=d`; strict `K>L` supplies `K>d` and `rho K>1/2`. The whole `rho_0` fiber
therefore belongs to and is removed with the first lower component.

### 3.2 Finite lower inventory

The complete inventories through `sqrt(114)` reproduce the candidate caps

$$45,\quad46,\quad59,\quad66,\quad69,\quad78.$$

They are full multiplicity sums. The exact open lower walls are `d`, `10`,
`81/8`, `21/2`, and `sqrt(7073)/8`; the final upper face `sqrt(114)` is
included. The moving `3z_rho` face excludes `(0,3)` at equality and assigns it
only to the high side. The propagated identity

$$
\left(\frac{81}{8}\right)^2+8=\frac{7073}{64}
$$

creates the advertised `(4,2)` wall. Evaluating the decreasing-in-`rho`,
increasing-in-`K` Weyl lower bound at the relevant strict lower corners pays
all six caps. No moving/fixed-wall ordering change reverses a payment.

### 3.3 Aggregate floor cells and the exceptional cap

For `sigma<rho<rho_c`, `K>sqrt(114)`, set

$$p=\lfloor\omega_0K\rfloor,
\qquad m=\lfloor\rho K-1/2\rfloor.$$

Here `p>=1`. If `p>=2`, the exact inequality `rho_c/omega_0<3/2` gives
`rho K<2p+1/2`, hence `m<=2p-1`. For `p=1`, the same criterion fails only
when `rho K>=5/2`. Thus the unique omitted floor cell is exactly

$$
\mathcal B=\left\{\sigma<\rho<\rho_c, K>\sqrt{114},
\ \rho K\ge\frac52, K<\frac2{\omega_0}\right\}.
$$

At a half-integer interface, the interface start is assigned to the high
side and its remainder is zero. The face `rho K=5/2` is exceptional-owned;
`K=2/omega_0` has `p=2` and is aggregate-owned. Away from a half-integer,
the summed floor gain is positive against the common remainder; on a
half-integer, strictness remains in the nonzero high convex tail. No floor
wall is uncovered.

On `B`, `K<367/20`. The all-domain strict phase proxy gives exactly

$$
(6,5,5,4,4,3,3,3,2,2,1,1,1,1,0)
$$

for `ell=0,...,14`. Its weighted sum is `395`; the zero row at `ell=14`
and monotonicity remove the entire angular tail. Since `rho K>=5/2` and
`rho<rho_c`, the exact corner payment is strictly greater than `395` (in
fact greater than `424`). Thus the exceptional cell is closed.

The exact disjoint lower allocation is consequently

$$
\begin{aligned}
\mathcal D_{19}^{\rm low}={}&
\{\rho_*<\rho\le\rho_0,L<K<U\}\dot\cup
\{\rho_0<\rho\le\sigma,d<K<U\}\\
&\dot\cup\{\sigma<\rho<\rho_c,d<K\le\sqrt{114}\}\\
&\dot\cup\{\sigma<\rho<\rho_c,\sqrt{114}<K<U\}.
\end{aligned}
$$

The wedge owns `rho=sigma`, and the finite ledger owns `K=sqrt(114)`. This
proves the complete lower claim; no lower residual survives.

## 4. High staircase through `k_11`

### 4.1 Complete inventories and caps

I first reconstructed the closed base `z_rho<=K<=k_6` rather than treating
the residual packet as a spectral proof. The same strict channel/ball proxy
has no mode at `K=z_rho`; at each subsequent fixed or moving event I added the
entire angular multiplicity before payment. The tight base event has cap `9`,
`K>51/10`, and `rho<3/10`, and is paid with the exact positive reserve
`1387329/11000000`. Every remaining base event is separately paid with a
positive reserve, and the channel `ell=6,n=1` is excluded at `K=k_6`. Thus
the closed base of the displayed theorem is independently recovered, not
imported from set bookkeeping.

Combining the channel and ball lower bounds gives the complete checkpoint
inventories:

| checkpoint | possible modes |
|---|---|
| `k_7` | first `ell=0,...,6`; second `ell=0,1`; no `n>=3` |
| `k_8` | first `ell=0,...,7`; second `ell=0,...,3`; no `n>=3` |
| `k_9` | first `ell=0,...,8`; second `ell=0,...,4`; no `n>=3` |
| `k_10` | first `ell=0,...,9`; second `ell=0,...,5`; third `ell=0,1`; no `n>=4` |
| `k_11` | first `ell=0,...,10`; second `ell=0,...,4`; third `ell=0,1`; no `n>=4` |

At `K=k_m`, channel `ell=m,n=1` is at its lower equality wall and is not
strictly counted. The fixed and moving bounds overlap at the algebraic faces
`z^2=16`, `68/3`, and `34`, so no omitted angular or radial tail lies between
the two exclusion mechanisms.

I recomputed every printed cap as a full square-block sum. The `k_8` rows are

$$
(64,65,68,73,80),\ (49,50,53,-,-),\
(36,37,40,45,52),\ (25,26,29,34,41),
$$

and the `k_9` rows are

$$
(81,-,-,-,-,-),\ (64,65,68,73,-,-),\
(49,50,53,58,65,74),\
(36,37,40,45,52,61),\ (25,26,29,34,41,50).
$$

The `k_10` cap sequence is

$$100;\ 81,97;\ 64,80,89,100;\ 74,69,78,85,89,$$

and the `k_11` sequence is

$$121;\ 100,125;\ 106,110;\ 93.$$

At `k_7`, the complete first-mode blocks are `25,36,49`, and the two
possible second modes add the full weights `1+3`. These reproduce every
`k_7` cap used by the payment split.

The marked impossible `k_8` cells follow from the incompatible necessary
walls `z^2>28` and `z^2<22`. At `k_9`, `H=8` forces
`z^2>1801/36>30`, excluding every second mode; `H=7` with `h>=3` is
similarly impossible. At `k_10`, the first-mode walls for `H=9,8,7` give
the stated second/third-mode restrictions. At `k_11`, `H=10` forces
`z^2>1461/25>44`, and `H=9` forces `z^2>796/25>33/2`. These prove the
incompatibilities rather than reading them back from the cap table.

### 4.2 Localization, payment, and the cap-74 correction

I checked the expected side, not merely non-equality, at all seventeen named
rational ratios

$$
\frac15,\frac3{10},\frac13,\frac38,\frac25,\frac5{12},
\frac37,\frac12,\frac{107}{200},\frac8{15},\frac35,
\frac{16}{25},\frac{13}{20},\frac23,\frac4{25},
\frac14,\frac7{20}.
$$

Each sign is the sign of the actual channel difference

$$m(m+1)-\ell(\ell+1)-(n^2-1)z_\rho^2.$$

The defining equality excludes the mode. In particular, any second mode at
`k_11` forces `rho<8/15`, any third mode forces `rho<1/4`, `H=10`
excludes every higher radial mode, and `H=9` excludes every third mode. The
algebraic face `z^2=16` lies on the possible side for `k_11,(1,3)`, while
`68/3` and `34` are exact excluded equality faces for `k_10,(6,2)` and
`k_11,(5,2)`.

For a moving event `K^2=sz^2+d`, the derivative of the Weyl payment has the
sign of

$$
s\pi^2\frac{1+\rho}{(1-\rho)^2}-\rho^2d;
$$

a constant event decreases with `rho`. Splitting at the finite
constant/moving and ratio crossings therefore reduces every cell to an exact
endpoint comparison. Recalculation of the incumbent case ledgers and the A4
interval ledger gives a positive reserve in every realizable cell, with all
coincident events charged at their combined multiplicity.

The A3 summary sentence claiming that every unprinted cell had a *larger*
reserve was false for the candidate's conservative `k_9,H=6,h=4` cap-74
row. I do not use that sentence. The immutable addendum supplies both valid
closures. First, full propagation gives

$$
j_{9/2,2}^2>\left(\frac{103}{10}\right)^2+8
=\frac{11409}{100}.
$$

If `(4,2)` were counted at `k_9`, the ball wall would force
`z^2>2409/100`, while the channel wall forces `z^2<70/3`; these are
incompatible. Thus the full proxy makes the row empty. If the printed
conservative cap is retained, the weaker wall still forces

$$K>\frac{207}{20},\qquad \rho<\frac7{20},$$

and exact arithmetic gives

$$
\mathcal W\left(\frac7{20},\frac{207}{20}\right)
>\frac{52823261673}{704000000}
=74+\frac{727261673}{704000000}>74.
$$

This directly pays the candidate table exactly as printed. It also explains
why the addendum corrects prose but does not change the theorem verdict.

All five new checkpoint faces are therefore paid. Together with the
independently reconstructed lower bands through `k_6`, this proves

$$
\rho_c\le\rho\le\frac78,qquad z_\rho\le K\le k_{11}(\rho)
\quad\Longrightarrow\quad N_D<\mathcal W.
$$

The face `k_6` remains predecessor-owned for residual subtraction; `k_11`
is newly owned. The proof itself is valid at `rho=7/8`, although that ratio
face is already outside the live residual.

## 5. All-frequency optical theorem

Put `epsilon=1-rho`, `a=epsilon K`. The requested ratio range is exactly

$$0<\varepsilon\le\frac{11}{50}.$$

The low and high pieces `a<=c/epsilon` and `a>=c/epsilon`, with
`c=1126/625`, are both inclusive. Their common face is above `2pi` even at
`epsilon=11/50`, so it lies in the proved deficit regime.

### 5.1 Product screen

For `a>pi`, strict radial counting gives the unique convention

$$\frac a\pi=N+t,\qquad N\ge1,\qquad0<t\le1,$$

with `(N,t)=(m-1,1)` at `a=m pi`. Exact summation gives

$$
\frac{D(a)}{\pi^2}=\frac{N^2}{2}
+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
$$

For `C_D=1382/3125`, the difference from `C_D(N+t)^2` increases with
`N`; at `N=1` its derivative is `2(t-C_D)(t+1)`. Its exact minimum is

$$\frac{1822532}{91552734375}>0.$$

Hence `D(a)>C_D a^2` on every radial cell. The product min--max majorant,
strict angular ceiling, and quarter-circle sum reduce the low piece to

$$
C_D-\left(\frac{2cq}{3}+\frac{\varepsilon}{4}
+\varepsilon^2q^2\right)>0,
\qquad q=\frac{106}{333}>\frac1\pi.
$$

The cost increases with `epsilon`, and at `11/50` the exact reserve is

$$R_L=\frac{39569}{2772225000}>0.$$

For `0<=a<=pi`, the strict count is zero, including `a=pi`. Thus the low
piece is strict for every `K>0` and owns the common face.

### 5.2 Complementary-action screen

For the exact action inverse, put `F=R^2`, `g=-F'`, and `T=a/pi`. Direct
differentiation gives `g` decreasing before the actual ungridded inner
interface `tau` and increasing after it, with

$$F(\tau)=\rho^2a^2,\qquad F(T)=0,\qquad g(T)=2\pi\rho a.$$

For the shifted strict sawtooth, `W>=0` and

$$-\frac1{32}\le W(t)-\frac t4\le\frac3{32}.$$

Splitting the Stieltjes integral at the actual `tau`, without assuming
`tau>1` or aligning it to a grid point, gives

$$
D_{\rm rad}\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
$$

The exact half-integer layer count obeys

$$
\varepsilon^2M_\varepsilon(x)^2<(x+\varepsilon/2)^2
$$

even at a half-integer wall. The complete angular error is therefore
strictly less than

$$
E=\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
$$

On `a>=c/epsilon`, the radial lower screen decreases and the angular upper
screen increases with `epsilon` on the whole required interval. Exact
evaluation at `11/50` gives

$$R_H=\frac{14817541}{472867032960000}>0.$$

Thus `D_rad>E`, the action sum is strictly below its continuous integral,
and the all-domain phase transfer gives `N_D<W` for every `K>0`. At `K=0`
both sides are zero. The radial walls, angular half-integer walls,
phase-proxy integer walls, common optical face, and `epsilon=11/50` face are
all owned. The limit `epsilon=0` (`rho=1`) is not treated as a shell in the
domain. No Round 16 endpoint conclusion has been extrapolated; only its
domain-free identities were used and every `epsilon<=11/50` sign was
re-established.

Consequently

$$
\frac{39}{50}\le\rho<1,\qquad K\ge0
\quad\Longrightarrow\quad N_D\le\mathcal W,
$$

with equality only at `K=0` and strict comparison for `K>0`.

## 6. Thresholds, upper floors, and exact subtraction

Exact interval arithmetic reproduces

$$
\rho_*<\rho_0<\sigma<\rho_c<\frac{39}{50}<\frac78.
$$

For `rho>=rho_c`, `a_rho>=1` and
`eta_rho<=G_1(1/2)=omega_0<1/8`. The positive-root identity for `K_0`
therefore gives `K_0>64`. On `rho<7/8`, `z_rho<8pi`, hence
`k_11<28<64`. If the seam branch is eligible, it is at least `1944`.
The `H_0` branch is ineligible because `rho_c>omega_0`. Therefore

$$k_{11}(\rho)<U(\rho)\qquad(\rho_c\le\rho<7/8).$$

On `rho_c<=rho<39/50`, `H_0` is ineligible and `39/50<5/6`, so the seam
is also ineligible. Hence

$$U(\rho)=K_0(\rho)$$

on exactly the proposed remaining ratio interval.

The inherited-owner faces also survive both one-sided traces. The lower
spectral proofs do not depend on which of `H_0` or `K_0` realizes `U`, so the
`H_0=K_0` interface is harmless and the inherited rule owns equality.
Eligibility ends at `rho=omega_0`; the active minimum is already `K_0`.
The formula interface at `rho=1/2` is continuous. At `rho=5/6`, the seam
begins inclusively, but `k_11` is below both competing floors. The optical
theorem is all-frequency across all of these interfaces.

Starting from

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,L<K<U\}\\
&\cup\{\rho_0<\rho<\rho_c,d<K<U\}\\
&\cup\{\rho_c\le\rho<7/8,k_6<K<U\},
\end{aligned}
$$

the lower theorem removes the first two disjuncts, including the complete
`rho_0` fiber. Since `k_11<U`, the staircase removes exactly
`k_6<K<=k_11` and leaves `k_11<K<U`. The optical theorem removes exactly
the ratios `39/50<=rho<7/8`, including `rho=39/50`. Thus

$$
\boxed{
\mathcal D_{19}\setminus
(\mathcal D_{19}^{\rm low}\cup\mathcal C_{20}^{\rm stair}
\cup\mathcal C_{20}^{\rm opt})
=\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

The `rho_c` face survives only above the newly owned `k_11` face;
`rho=39/50` is optical-owned. `K=k_6` is predecessor-owned, `K=k_11` is
staircase-owned, and `K=U` remains excluded. The certified boxes `B_0` and
`B_1` were already subsets of the predecessor cover and are not subtracted a
second time.

## 7. A4 failure chronology and executable re-audit

Both rejected A4 cycles remain preserved and supply no positive evidence:

1. `combined-closure-constants-adversarial-audit.md`, SHA-256
   `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd`,
   returned **FAIL** because the original verifier paid only 73 in the live
   cap-74 row and contained tautological or disconnected labels.
2. `combined-closure-constants-replacement-audit.md`, SHA-256
   `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31`,
   returned **FAIL** because the first replacement report contained an actual
   `0x08` byte, localization semantics survived an expected-output mutation,
   the cap-74 wrong-wall gate was insufficient, and skip-hash output appeared
   authenticated.

The original immutable A4 report remains at
`4b5429f9e51e55d7a00635a58115fb417441e23eec5ba253346f54bee9aa9afe`.
Git history retains the first failure at `964a421` and the second at
`fe63903`; the final repair and its audit are later commits. Neither FAIL was
overwritten or reinterpreted.

The final verifier contains a thirteen-check cap-74 path, independently
connected expected-side calculations at all seventeen rational faces, a
wrong-wall equality test, semantic mutation tests, control-byte scans, and an
explicitly unauthenticated skip-hash mode. I reran:

```text
python -B computations/round20_verify_combined_closure.py
PASS
first issue: none
exact finite checks: 587
substantive checks: 488
bookkeeping identities: 65
authentication gates: 34
candidate sha256: e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
freeze sha256: aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
analytic assumptions remaining for A3: 8
```

```text
python -B -m pytest -p no:cacheprovider -q \
  computations/tests/test_round20_verify_combined_closure.py
17 passed
```

```text
python -B -m pytest -p no:cacheprovider -q
271 passed, 1 xfailed, 10 subtests passed
```

The expected failure is pre-existing and expected; no test failed. The A4
PASS remains correctly limited to finite arithmetic and byte integrity. The
eight analytic assumptions are supplied by the independently reconstructed
arguments above, not promoted by the script.

## 8. Final decision

The attempt to falsify the frozen candidate found no unsupported implication.
The lower closure, closed staircase through `k_11`, all-frequency optical
theorem, source boundary, form/index directions, zero enumeration, every cap
and payment including cap 74, equality ownership, upper-floor normalization,
and exact `D19` to `D20` subtraction all survive reconstruction.

**PASS; first unsupported implication: none.** This report authorizes a fresh
judge and nothing further. Promotion and state mutation remain forbidden
until the judge and State Patch gates succeed.
