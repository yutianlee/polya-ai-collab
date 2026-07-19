# Round 18 independent exact audit of Candidate C18

Status: **PASS**.

First unsupported implication: **none**.

Scope: this is an independent analytic reconstruction plus an exact finite
constant ledger.  The executable ledger checks rational algebra; it does not
pretend to execute the functional-analytic min--max arguments, the external
Lorch theorem, or the accepted Round 17 theorem.  Those inputs and the exact
division of responsibilities are made explicit below.

The audit began only after authenticating the proof-free candidate as
`354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9`
and its external freeze record as
`b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c`.
No Round 18 incumbent proof, source-audit review, certificate, judge draft,
or other constant ledger was consulted.

## 1. Authenticated input boundary

| permitted input | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md` | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| `rounds/polya-main/round_018/exploration/candidate-claim-freeze.md` | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `rounds/polya-main/round_018/exploration/residual-mask-freeze.md` | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |

The ledger reconstructs a Machin-series enclosure with exact fractions and
independently verifies

$$
\frac{333}{106}<\pi<\frac{22}{7}.
\tag{1}
$$

No floating-point approximation enters a PASS decision.

## 2. Shell lower bound and the first radial barrier

Put

$$
w=1-\rho,
\qquad z=\frac{\pi}{w}.
$$

In angular order $\ell$, the authenticated separation theorem gives the
one-dimensional Dirichlet form

$$
\mathfrak a_\ell^\rho[u]
=\int_\rho^1\left(|u'|^2+
\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak a_\ell^\rho)=H_0^1(\rho,1).
\tag{2}
$$

Because $r\le1$ and the $n$th eigenvalue of the Dirichlet interval
Laplacian on $(\rho,1)$ is $n^2z^2$, form ordering and min--max give

$$
\boxed{
\lambda_{\ell,n}^{\rm shell}(\rho)
\ge n^2z^2+\ell(\ell+1).
}
\tag{3}
$$

The direction is important: replacing $r^{-2}$ by $1$ lowers the form and
therefore lowers every ordered eigenvalue.  For $\ell=0$, (3) is exact.

On $\rho\ge\rho_c$, one has

$$
z\ge z_{\rho_c}=\pi+\frac12>\frac72.
$$

Consequently

$$
4z^2-k_5^2=3z^2-30
>3\left(\frac72\right)^2-30
=\frac{27}{4}>0.
\tag{4}
$$

Thus every radial index $n\ge2$, in every angular channel, is absent for
$K\le k_5$.  This includes the face $K=k_5$ and uses the strict spectral
count.  The attempted wall $K=2z$ is strictly above $k_5$ by (4).  At
$K=2z$ the exact $\ell=0,n=2$ frequency is itself excluded by strict
counting, but immediately beyond it a second radial state may enter; no
extension to that region is claimed.

Similarly, for $\ell\ge5$ and $n=1$,

$$
\lambda_{\ell,1}\ge z^2+\ell(\ell+1)
\ge z^2+30=k_5^2.
\tag{5}
$$

Hence only the first radial modes with $\ell=0,1,2,3,4$ can contribute.
The attempted angular wall $k_6$ is outside the claim because

$$
k_6^2-k_5^2=42-30=12>0.
$$

Nothing here excludes the $\ell=5$ channel once $K>k_5$.

The cumulative multiplicities are exact:

$$
\sum_{\ell=0}^{m-1}(2\ell+1)=m^2,
\qquad m=1,2,3,4,5,6.
\tag{6}
$$

They give $1,4,9,16,25,36$.  Possible eigenvalue coincidences between
different angular orders do not invalidate (6): the orthogonal channel
dimensions add, and the strict endpoint decision is made within every
channel before summation.

## 3. Fixed-channel shell-to-ball comparison

This step is not imported from Lorch and cannot be justified by an
unlabelled appeal to global domain monotonicity.

For a fixed pair $(\ell,m)$, the unit-ball radial transform has form

$$
\mathfrak a_\ell^0[v]
=\int_0^1\left(|v'|^2+
\frac{\ell(\ell+1)}{r^2}|v|^2\right)dr.
\tag{7}
$$

Its domain is $H_0^1(0,1)$ with the displayed potential finite.  For
$\ell\ge1$ this finiteness follows from the one-dimensional Hardy
inequality; for $\ell=0$ the potential vanishes.  If
$u\in H_0^1(\rho,1)$, define

$$
(Eu)(r)=
\begin{cases}
0,&0<r\le\rho,\\
u(r),&\rho<r<1.
\end{cases}
$$

The zero trace of $u$ at $r=\rho$ gives $Eu\in H_0^1(0,1)$.  Extension
preserves both the norm and form:

$$
\|Eu\|_{L^2(0,1)}=\|u\|_{L^2(\rho,1)},
\qquad
\mathfrak a_\ell^0[Eu]=\mathfrak a_\ell^\rho[u].
\tag{8}
$$

In physical variables it sends
$u(r)r^{-1}Y_{\ell m}(\omega)$ to the same angular factor, extended by zero
on the inner ball.  It therefore preserves the fixed angular subspace and
does not mix orders.

The shell trial space is consequently a subspace of the ball trial space.
Taking first Rayleigh infima gives the required direction

$$
j_{\ell+1/2,1}^2
=\lambda_{\ell,1}^{\rm ball}
\le\lambda_{\ell,1}^{\rm shell}(\rho).
\tag{9}
$$

No strict domain-monotonicity theorem is needed: the strict rational
exclusions below follow from strict Lorch bounds after the non-strict
comparison (9).

## 4. Exact Bessel-zero thresholds and source scope

The Lorch source defines $j_{\nu,1}$ as the first positive zero of $J_\nu$
and states its inequalities for $-1<\nu<\infty$.  The orders
$5/2,7/2,9/2$ all lie in that scope.  The spherical-Bessel identity

$$
\mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
\qquad x>0,
$$

has a positive prefactor, so its positive zeros agree with those of the
ordinary Bessel function.

For $\nu=5/2$, Lorch's first displayed inequality gives

$$
j_{5/2,1}^2>\frac{105}{4},
\qquad
\frac{105}{4}-\left(\frac{51}{10}\right)^2
=\frac6{25}>0.
\tag{10}
$$

For $\nu=7/2$, the second bound simplifies to

$$
j_{7/2,1}^2>\frac{81\sqrt5-9}{4}>\frac{169}{4},
$$

where the denominator $6(\sqrt5-1)$ is positive and the last comparison is
certified by

$$
5-\left(\frac{178}{81}\right)^2
=\frac{1121}{6561}>0.
\tag{11}
$$

For $\nu=9/2$, it simplifies to

$$
j_{9/2,1}^2>
\frac{363\sqrt{15}-121}{22}>\frac{225}{4},
$$

where $4(\sqrt{15}-2)>0$ and

$$
15-\left(\frac{247}{66}\right)^2
=\frac{4331}{4356}>0.
\tag{12}
$$

All frequencies are positive, so taking positive square roots in
(10)--(12), then using (9), yields

$$
\begin{aligned}
\sqrt{\lambda_{2,1}^{\rm shell}}&>c_2=\frac{51}{10},\\
\sqrt{\lambda_{3,1}^{\rm shell}}&>c_3=\frac{13}{2},\\
\sqrt{\lambda_{4,1}^{\rm shell}}&>c_4=\frac{15}{2}.
\end{aligned}
\tag{13}
$$

Thus the relevant channel is excluded even at $K=c_m$.  Lorch is not used
for a shell cross-product zero, a higher radial mode, multiplicity, or a
Weyl estimate.  The source card notes that the publisher proof is
access-controlled; this is not an unsupported implication here because the
three strict zero bounds are explicitly permitted external inputs of the
frozen claim.

## 5. Monotonic moving-wall payments

Let

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3,
\qquad
F_m(\rho)=\mathcal W(\rho,k_m(\rho)).
$$

With $S=1+\rho+\rho^2$, $w=1-\rho$, and $c=m(m+1)$,

$$
F_m(\rho)
=\frac{2}{9\pi}\frac{S}{w^2}
\left(\pi^2+cw^2\right)^{3/2}.
\tag{14}
$$

Every factor is positive.  Multiplying the logarithmic derivative by the
positive quantity $Sw(\pi^2+cw^2)$ gives exactly

$$
3\left[\pi^2(1+\rho)-c\rho^2(1-\rho)^2\right].
\tag{15}
$$

For $m\le5$, $c\le30$, and
$\rho^2(1-\rho)^2\le1/16$.  From $\pi>3$, the bracket in (15) is strictly
larger than

$$
9-\frac{30}{16}=\frac{57}{8}>0.
\tag{16}
$$

Therefore every $F_m$, $m=1,2,3,4,5$, is strictly increasing.  This proves
the derivative sign with all denominators and radicals controlled.

The base cap $4$ is also independently paid on the new region.  At
$\rho_c$, use $\rho_c<1/7$, $z_{\rho_c}>193/53$, and
$2/(9\pi)>7/99$.  Positivity makes squaring reversible, and the exact
margin is

$$
\left[\frac7{99}\frac{342}{343}
\left(\left(\frac{193}{53}\right)^2+2\right)^{3/2}
\right]^2-4^2
=\frac{88584210264668}{53216631070729}>0.
\tag{17}
$$

Thus $F_1(\rho)>4$ throughout $\rho\ge\rho_c$.  In particular, whenever
$K>k_2>k_1$, one has $\mathcal W(\rho,K)>4$.

## 6. Exact split bridges

The fixed-ratio lower bounds use $2/(9\pi)>7/99$.  They are

$$
\begin{aligned}
\mathcal W\left(\frac3{10},\frac{51}{10}\right)
&>\frac{100387329}{11000000}
=9+\frac{1387329}{11000000},\\
\mathcal W\left(\frac12,\frac{13}{2}\right)
&>\frac{107653}{6336}
=16+\frac{6277}{6336},\\
\mathcal W\left(\frac12,\frac{15}{2}\right)
&>\frac{18375}{704}
=25+\frac{775}{704}.
\end{aligned}
\tag{18}
$$

The moving walls lie strictly above the corresponding fixed thresholds at
the splits.  Using $\pi>333/106$ gives

$$
\begin{aligned}
k_2(3/10)^2-c_2^2
&>\frac{1802859}{13764100}>0,\\
k_3(1/2)^2-c_3^2
&>\frac{103667}{11236}>0,\\
k_4(1/2)^2-c_4^2
&>\frac{36251}{11236}>0.
\end{aligned}
\tag{19}
$$

For $(m,r_m)=(2,3/10),(3,1/2),(4,1/2)$, suppose the $\ell=m$
channel can contribute.  Both lower bounds (3) and (13) then force

$$
K>k_m(\rho),
\qquad K>c_m.
\tag{20}
$$

If $\rho\le r_m$, then $1-\rho^3\ge1-r_m^3$ and

$$
\mathcal W(\rho,K)>
\mathcal W(\rho,c_m)\ge\mathcal W(r_m,c_m)>(m+1)^2.
\tag{21}
$$

If $\rho\ge r_m$, monotonicity, (19), and (20) give

$$
\mathcal W(\rho,K)>F_m(\rho)
\ge F_m(r_m)>
\mathcal W(r_m,c_m)>(m+1)^2.
\tag{22}
$$

Both arguments are valid at the split itself, so there is no one-sided
gap at $3/10$ or $1/2$.

Equations (20)--(22) also dispose of every empty or degenerate band caused
by the ordering of $c_m$ and $k_m(\rho)$:

- if $k_m(\rho)<c_m$, the interval
  $k_m<K\le c_m$ retains the lower count because (13) still excludes the
  channel;
- if $k_m(\rho)>c_m$, that interval is empty in the opposite ordering and
  any possible entry already satisfies the moving-wall side of the bridge;
- if $k_m(\rho)=c_m$, the equality point is excluded by strict counting,
  and every point above it satisfies both strict inequalities in (20).

No numerical crossing location is needed.

## 7. Completion of the strict-count staircase

The promoted Round 17 theorem owns the closed band
$z\le K\le k_2$.  It remains to prove the genuinely new region
$k_2<K\le k_5$.

By (4)--(5), at most one radial mode in each of the five orders
$\ell=0,1,2,3,4$ can occur.  If none of $\ell=2,3,4$ can occur, the count
is at most $1+3=4$, which is strictly paid by (17).  Otherwise let $q$ be
the largest one of $2,3,4$ whose first mode can occur.  Equations (3) and
(13) force (20) with $m=q$, while all orders above $q$ are absent.  Hence

$$
N_D(A_{\rho,1},K^2)
\le\sum_{\ell=0}^{q}(2\ell+1)=(q+1)^2
<\mathcal W(\rho,K)
\tag{23}
$$

by the corresponding bridge (21) or (22).  This proves the desired strict
inequality throughout the new band.

At $K=k_3$ or $K=k_4$, the newly indexed angular channel is excluded if
its lower bound is an equality, because the spectral count uses
$\lambda<K^2$.  At $K=k_5$, the $\ell=5$ channel is likewise excluded,
so the proposed upper face is included.  At each $K=c_m$, (13) is strict
and excludes that channel.  Accidental cross-order coincidences are already
covered by the multiplicity sum in (23).

Combining (23) with the accepted Round 17 band proves Candidate C18 on the
complete closed set

$$
\rho_c\le\rho\le\frac78,
\qquad z_\rho\le K\le k_5(\rho).
$$

At $K=z_\rho$, the exact first $\ell=0$ frequency equals $z_\rho$, so the
strict count is zero and the positive Weyl term pays it.  At $K=k_2$ the
accepted Round 17 owner remains in force.  The spectral argument above is
uniform at $\rho=\rho_c$ and $\rho=7/8$; theorem validity on the latter
face is distinct from residual ownership.

## 8. Strict comparison with every active upper floor

First, the frozen locator gives
$\rho_{HK}<94071/10^6<1/10$.  On the other hand, (1) gives

$$
\rho_c>\frac7{51}>\frac1{10},
\qquad
\frac7{51}-\frac1{10}=\frac{19}{510}>0.
\tag{24}
$$

Therefore $H_0$ is never active on the C18 ratio range: the active branch
is $K_0$ below $5/6$ and the seam floor at and above $5/6$.

The ball action in the permitted source card gives

$$
G_1(x)=\frac1\pi
\left(\sqrt{1-x^2}-x\arccos x\right),
\qquad
G_1'(x)=-\frac1\pi\arccos x.
$$

Hence

$$
G_1(x)=\frac1\pi\int_x^1\arccos t\,dt.
\tag{25}
$$

For $\rho\le1/2$, $\eta_\rho=G_1(1/2)=\omega_0$.  Since
$\sqrt3<7/4$ (squared margin $1/16$) and $\pi>3$,

$$
0<\eta_\rho=\frac{\sqrt3}{2\pi}-\frac16<\frac18.
\tag{26}
$$

For $\rho\ge1/2$, (25) and $0\le\arccos t\le\pi/2$ give

$$
0<\eta_\rho=G_1(\rho)\le\frac{1-\rho}{2}=\frac w2.
\tag{27}
$$

Write $a=2\pi\rho/w$.  Positivity of $\eta,C_0,a$ shows directly from
the frozen positive-root formula that

$$
K_0
=\left(\frac{\sqrt a+\sqrt{a+4\eta C_0}}{2\eta}\right)^2
>\frac a{\eta^2}.
\tag{28}
$$

For $\rho_c\le\rho\le1/2$, $a\ge1$ and (26) yields $K_0>64$.
For $1/2\le\rho<5/6$, (27) yields

$$
K_0>\frac{4a}{w^2}
=\frac{8\pi\rho}{w^3}>96.
\tag{29}
$$

The last inequality uses $\pi>3$, $\rho\ge1/2$, and $w\le1/2$.

On the whole closed ratio band, $w\ge1/8$ and $\pi<22/7$, so

$$
26^2-k_5^2
>26^2-\left[\left(\frac{176}{7}\right)^2+30\right]
=\frac{678}{49}>0.
\tag{30}
$$

Thus $k_5<26<64<K_0$ on every active $K_0$ branch.  At
$5/6\le\rho<7/8$,

$$
\frac{54}{w^2}\ge1944>26>k_5.
\tag{31}
$$

This is strict at the inclusive seam $\rho=5/6$ and remains strict on its
right trace.  Finally,

$$
k_5<26<295^2=87025,
$$

so the candidate also stays below the old global face.  At $\rho=7/8$ the
old endpoint theorem owns the ratio face; the same bound (30) remains valid.

## 9. Exact inclusion, subtraction, and face ownership

The frozen second component of $\mathcal D_{17}$ is

$$
\left\{\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K<U(\rho)\right\}.
$$

Equations (30)--(31) and (28)--(29) prove $k_5<U$ against every active
branch.  Therefore

$$
\boxed{\mathcal C_{18}\subset\mathcal D_{17}}.
\tag{32}
$$

Exact interval subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}}
\tag{33}
$$

The lower face $K=k_5$ is covered by C18 and is therefore strict in the
new residual.  The face $K=k_2$ retains its Round 17 owner.  The upper face
$K=U$ retains its old owner.  The $\rho_c$ slice belongs to the second
piece, while $\rho=7/8$ retains its complete old endpoint owner.  The
certified boxes $B_0$ and $B_1$ were already proved to lie in the promoted
Round 17 band; they are regression provenance and are not subtracted again.

## 10. Mandatory-wall verdict table

| wall | result |
|---|---|
| $\rho=\rho_c$ | included; base cap 4 and all low-split bridges are uniform |
| $\rho=3/10$ | both $m=2$ bridge inequalities overlap; (18)--(19) are strict |
| $\rho=1/2$ | both $m=3,4$ bridges overlap; $G_1(1/2)=\omega_0$ matches the two $\eta$ descriptions |
| $\rho=5/6$ | seam begins inclusively and has reserve at least $1944-26$ |
| $\rho=7/8$ | spectral theorem closed; residual ownership remains old |
| $K=z$ | strict count zero; accepted lower-band owner |
| $K=k_2$ | accepted Round 17 owner; C18 begins strictly above |
| $K=k_3,k_4$ | next angular equality excluded by strict counting |
| $K=k_5$ | included; $\ell=5$ equality excluded by strict counting |
| $K=c_2,c_3,c_4$ | corresponding shell eigenfrequency is strictly larger |
| $K=2z$ | strictly outside C18 by the $27/4$ squared margin |
| $K=k_6$ | strictly outside C18 by squared gap $12$ |
| $K=U$ | strictly above $k_5$ and owned by old coverage |
| $n=1,2$ | $n=1$ counted by angular caps; all $n\ge2$ excluded by (4) |
| $\ell=0,\ldots,5$ | $0$--$4$ counted with full multiplicity; $\ell\ge5$ excluded through $k_5$ |
| cross-order coincidence | dimensions add; no simplicity across distinct $\ell$ is assumed |
| $B_0,B_1$ | already absorbed by C17; never subtracted again |

Every prescribed face and both one-sided split traces pass.

## 11. Executable evidence and reproduction

~~~powershell
python computations/round18_verify_angular_staircase.py --self-check --manifest
python -m pytest computations/tests/test_round18_verify_angular_staircase.py -q
python -m compileall -q computations/round18_verify_angular_staircase.py computations/tests/test_round18_verify_angular_staircase.py
~~~

The ledger returns **PASS**, 40 exact checks, and first issue `null`.

| output | SHA-256 |
|---|---|
| `computations/round18_verify_angular_staircase.py` | `c3d480cb85f65c9038a61aebfe411e18622b4224d7770e1c074f110330e5ea8f` |
| `computations/tests/test_round18_verify_angular_staircase.py` | `2a267c01568bbf069dc93efcc2119a75d454e33dc28b59315faf63ac58a41b50` |

Final verdict: **PASS** for Candidate C18, conditional only on the explicitly
permitted and hash-authenticated external Bessel-zero statements and the
already-promoted Round 17 band.  The finite ledger PASS is supporting
evidence, not a replacement for the analytic reconstruction above.
