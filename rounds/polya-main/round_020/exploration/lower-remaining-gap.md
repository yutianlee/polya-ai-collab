# Round 20 Lower-Ratio Remaining-Gap Exploration

Date: 2026-07-14.

Status: **PASS for the assigned component; exploratory analytic note only;
not frozen, independently reconstructed, judged, or promoted**.

This note assumes only the prospective Round 19 lower staircase and the two
completed Round 20 explorations named below.  Its assigned component is

$$
\mathcal R_{20}^{\rm L}
=\left\{(\rho,K):
\sigma<\rho<\rho_c,
\quad \sqrt{114}<K<U(\rho)\right\},
\tag{1}
$$

where

$$
\omega _0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
\sigma=\frac{3\omega _0}{4},
\qquad
\rho_c=\frac1{1+2\pi}.
\tag{2}
$$

The result is that **all of (1) is provable**.  The proof first aggregates
the exact integer gains of all low-interface tails.  That argument misses
only one explicitly described floor cell.  A direct strict-phase proxy cap
closes that cell with full angular multiplicities.

No frozen Round 19 artifact, state file, or other Round 20 file is changed.

## 1. Scoped inputs

| artifact | SHA-256 | use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/small-hole-wedge.md` | `f1e5ab1c3671e82257a78cd2855581f326e4df98385539a69dc4b1a295a7f43b` | reconstructed master inequality, exact constants, and the inherited face $\rho=\sigma$ |
| `rounds/polya-main/round_020/exploration/lower-next-wall.md` | `94099e852274ac697fa8c60563fbcdb0c4bb91a40c3de2c0af7556cbf7754e0a` | included face $K=\sqrt{114}$ and the prospective remaining component |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` | audited low-interface split before its published sufficient threshold |
| `rounds/polya-main/round_003/judge/judge-003.md` | `33e292530e644896b00470a92848f2763c3c337c874a32c0f7bb79aac3b7aca9` | multiplicity-to-tail scaffold and high-interface tails |
| `rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md` | `ef3796a9de3a394f39f34190a25b4daa97d908c123c688146dfa0b308104b375` | exact strict spectral proxy and Weyl integral |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` | convex shifted-tail theorem, including its equality characterization |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | strict radial count below the ordinary-floor proxy |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` | exact inherited ceiling $U$ and its branch ownership |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | turning estimate for $G$ |

The authenticated elementary enclosure

$$
\frac{333}{106}<\pi<\frac{355}{113}
\tag{3}
$$

is used only in exact rational comparisons.  No new Bessel-zero source is
introduced.

## 2. Stronger local theorem and exact decomposition

Write

$$
\mu=\rho K,
\qquad
A_{\rho,K}(z)=G_K(z)-G_\mu(z),
\qquad
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{4}
$$

The proof below does not use the upper ceiling.  It proves the stronger
statement

$$
\boxed{
\sigma<\rho<\rho_c,
\quad K>\sqrt{114}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{5}
$$

The only exceptional floor cell for the aggregated-tail route is

$$
\boxed{
\mathcal B=\left\{(\rho,K):
\sigma<\rho<\rho_c,
\quad K>\sqrt{114},
\quad \rho K\geq\frac52,
\quad K<\frac2{\omega _0}
\right\}.}
\tag{6}
$$

Thus (5) is proved by the exact disjoint decomposition

$$
\left\{\sigma<\rho<\rho_c, K>\sqrt{114}\right\}
=\mathcal B\ \dot\cup\ \mathcal B^c,
\tag{7}
$$

where $\mathcal B^c$ is understood relative to the set on the left.  The
aggregated-tail proof treats $\mathcal B^c$, and the finite proxy cap treats
$\mathcal B$.

The constants already proved in the small-hole exploration give

$$
\omega _0>\frac{1184}{10863},
\qquad
d=\frac{\sqrt{337}}2>\frac{257}{28},
\qquad
\omega _0d>\frac{76072}{76041}>1.
\tag{8}
$$

Since

$$
114-\frac{337}{4}=\frac{119}{4}>0,
\tag{9}
$$

every point considered in (5) has $\omega _0K>1$.

## 3. The exact low-interface ledger

For an integer $r\geq0$, put

$$
x_r=r+\frac12,
\qquad
\mathcal T_r=
\left\lfloor A_{\rho,K}(x_r)+\frac14\right\rfloor
+2\sum_{j\geq1}
\left\lfloor A_{\rho,K}(x_r+j)+\frac14\right\rfloor.
\tag{10}
$$

If $x_r<\mu$, set

$$
n_r=\lfloor\mu-x_r\rfloor,
\qquad
q_r=x_r+n_r.
\tag{11}
$$

The audited split gives, including the case $n_r=0$,

$$
\frac{\mathcal T_r}{2}
\leq
\int_{x_r}^{K}A_{\rho,K}(z)\,dz
+\delta_r
-\frac{\lfloor\omega _0K\rfloor-n_r}{4},
\tag{12}
$$

where

$$
\delta_r=\int_{q_r}^{\mu}G_\mu(z)\,dz,
\qquad
0\leq\delta_r
\leq\frac{2}{15\sqrt\mu}(\mu-q_r)^{5/2}<\frac14.
\tag{13}
$$

The point of this note is not to demand that each individual integer gain
in (12) be positive.  Instead, all low-interface tails are summed before
the sign is tested.

Define the two exact floor indices

$$
p=\lfloor\omega _0K\rfloor,
\qquad
m=\left\lfloor\mu-\frac12\right\rfloor,
\tag{14}
$$

and write

$$
\mu=m+\frac12+t,
\qquad 0\leq t<1.
\tag{15}
$$

By (8)--(9), $p\geq1$.

### 3.1 Non-half-integer interface: $0<t<1$

The low-interface starts are exactly $r=0,\ldots,m$.  For every one of
them,

$$
n_r=m-r,
\qquad
q_r=m+\frac12,
\qquad
\delta_r=\delta
:=\int_{m+1/2}^{\mu}G_\mu(z)\,dz.
\tag{16}
$$

Hence the exact sum of the integer gains is

$$
\sum_{r=0}^{m}(p-n_r)
=(m+1)\left(p-\frac m2\right)
=\frac{m+1}{2}(2p-m).
\tag{17}
$$

Summing (12) over all low starts gives

$$
\sum_{r=0}^{m}\frac{\mathcal T_r}{2}
\leq
\sum_{r=0}^{m}\int_{x_r}^{K}A_{\rho,K}(z)\,dz
+(m+1)\left(\delta-\frac{2p-m}{8}\right).
\tag{18}
$$

Suppose

$$
m\leq2p-1.
\tag{19}
$$

If $2p-m\geq2$, then (13) gives
$\delta<1/4\leq(2p-m)/8$.  If $2p-m=1$, then
$m=2p-1\geq1$ and (15) gives $\mu>3/2$.  Therefore

$$
\delta<\frac{2}{15\sqrt{3/2}}<\frac18,
\tag{20}
$$

where the last positive-squaring comparison is $512<675$.  Thus (18) is
strictly no larger than the sum of its integrals whenever (19) holds.

### 3.2 Half-integer interface: $t=0$

Here the point $x_m=\mu$ belongs to the high-interface side.  The low
starts are exactly $r=0,\ldots,m-1$; when $m=0$ there are none.  For every
low start,

$$
n_r=m-r,
\qquad q_r=\mu,
\qquad \delta_r=0.
\tag{21}
$$

The exact gain sum is now

$$
\sum_{r=0}^{m-1}(p-n_r)
=\frac m2(2p-m-1).
\tag{22}
$$

Condition (19) makes (22) nonnegative.  Therefore the complete low-tail
sum is again at most the corresponding sum of integrals.  This separate
calculation is essential: adding the interface start $r=m$ to the low side
would give the wrong floor ledger.

### 3.3 Strictness after aggregation

The high-interface theorem controls every $x_r\geq\mu$.  Its source states
that equality in the convex shifted-tail theorem is possible only for the
zero function.  In the present range there is always a nonzero high tail.
Indeed, with

$$
r_h=\left\lceil\mu-\frac12\right\rceil,
\qquad x_h=r_h+\frac12,
\tag{23}
$$

one has $\mu\leq x_h<\mu+1$.  Also $\rho<\rho_c<1/7$ and
$K>\sqrt{114}>10$, so

$$
K-\mu=(1-\rho)K>\frac67\,10>1.
\tag{24}
$$

Thus $x_h<K$, and the translated $G_K$ tail is nonzero.  At least this one
high-interface inequality is strict.

Combining the low aggregate with all high tails and the promoted
multiplicity identity therefore yields, under (19),

$$
\begin{aligned}
\sum_{\ell\geq0}(2\ell+1)
\left\lfloor A_{\rho,K}(\ell+1/2)+\frac14\right\rfloor
&=\sum_{r\geq0}\mathcal T_r\\
&<2\int_0^K f_3(z)A_{\rho,K}(z)\,dz\\
&\leq\int_0^K2zA_{\rho,K}(z)\,dz\\
&=\mathcal W(\rho,K).
\end{aligned}
\tag{25}
$$

The strict phase enclosure puts the strict spectral count at most the first
quantity in (25), so (5) follows whenever (19) holds.

## 4. Exhaustive audit of the $(p,m)$ floor cells

It remains to determine exactly when (19) can fail.

First, the ratio bound

$$
\frac{\rho_c}{\omega _0}<\frac32
\tag{26}
$$

is elementary.  Indeed $\rho_c<1/7$, while (8) gives

$$
\frac{3\omega _0}{2}-\frac17
>\frac32\frac{1184}{10863}-\frac17
=\frac{523}{25347}>0.
\tag{27}
$$

If $p\geq2$, the definition of $p$ gives

$$
K<\frac{p+1}{\omega _0},
\qquad
\mu<\frac{\rho_c}{\omega _0}(p+1)
<\frac32(p+1)\leq2p+\frac12.
\tag{28}
$$

The last inequality is valid for every $p\geq2$, with equality only in the
discarded middle bound at $p=2$.  Hence

$$
m=\left\lfloor\mu-\frac12\right\rfloor\leq2p-1.
\tag{29}
$$

If $p=1$, condition (19) is simply $m\leq1$, equivalently
$\mu<5/2$.  Since $p=1$ is equivalent here to
$K<2/\omega _0$, the exact failure set is precisely (6).  There are no
other floor cells to audit.

For orientation, put

$$
\tau=\frac{5\omega _0}{4}.
\tag{30}
$$

The cell $\mathcal B$ can occur only for $\rho>\tau$: if
$\rho\leq\tau$, then $\rho K<\tau(2/\omega _0)=5/2$.  At the face
$\rho=\tau$, the two conditions $\rho K\geq5/2$ and
$K<2/\omega _0$ are incompatible.  Thus no hidden equality fiber is lost.

Integer walls are assigned exactly as follows:

- at $\omega _0K\in\mathbb Z$, the new value of $p$ is used, so the gain
  jumps upward;
- at $\mu\in\mathbb Z+1/2$, the interface tail is placed on the high side
  and (22), not (17), is the applicable sum;
- the face $\mu=5/2$ belongs to $\mathcal B$ when $p=1$;
- the face $K=2/\omega _0$ has $p=2$ and belongs to the aggregated branch.

## 5. Direct proxy cap on the exceptional cell

No Bessel-zero inventory is needed on $\mathcal B$.  The strict phase
enclosure gives, with $z_\ell=\ell+1/2$,

$$
N_D(A_{\rho,1},K^2)
\leq
\sum_{\ell\geq0}(2\ell+1)a_\ell,
\qquad
a_\ell=\left\lfloor
A_{\rho,K}(z_\ell)+\frac14\right\rfloor.
\tag{31}
$$

Since $0\leq A_{\rho,K}\leq G_K$, the turning estimate gives, for
$0<z<K$,

$$
A_{\rho,K}(z)
\leq G_K(z)
<\frac{(K-z)^{3/2}}{3\sqrt K}.
\tag{32}
$$

The lower bound in (8) is slightly stronger than the convenient rational
comparison

$$
\omega _0>\frac{40}{367},
\qquad
\frac{1184}{10863}-\frac{40}{367}
=\frac8{3986721}>0.
\tag{33}
$$

Consequently, throughout $\mathcal B$,

$$
K<\frac2{\omega _0}<R:=\frac{367}{20}.
\tag{34}
$$

For fixed $z>0$, the square of the right side of (32),
$(K-z)^3/(9K)$, is strictly increasing for $K>z$.  Thus it is enough to
test $K=R$.  If a proposed cap is $c_\ell$, the sufficient comparison is

$$
\frac{(R-z_\ell)^3}{9R}
<\left(c_\ell+\frac34\right)^2.
\tag{35}
$$

Because

$$
\frac{(R-z_\ell)^3}{9R}
=\frac{(357-20\ell)^3}{1321200},
\tag{36}
$$

the numerator of the positive difference in (35), over the common
denominator $1321200$, is

$$
M_\ell=(4c_\ell+3)^2\,82575-(357-20\ell)^3.
\tag{37}
$$

The complete exact table is

| $\ell$ | cap $c_\ell$ for $a_\ell$ | $M_\ell$ |
|---:|---:|---:|
| 0 | 6 | 14697882 |
| 1 | 5 | 5409422 |
| 2 | 5 | 11827162 |
| 3 | 4 | 3611502 |
| 4 | 4 | 8555642 |
| 5 | 3 | 1604782 |
| 6 | 3 | 5267322 |
| 7 | 3 | 8361062 |
| 8 | 2 | 2346202 |
| 9 | 2 | 4446342 |
| 10 | 1 | 176282 |
| 11 | 1 | 1474822 |
| 12 | 1 | 2444562 |
| 13 | 1 | 3133502 |
| 14 | 0 | 286642 |

Every entry is strictly positive.  The $\ell=14$ row shows
$G_K(14+1/2)<3/4$; monotonicity in $z$ gives $a_\ell=0$ for every
$\ell\geq14$ with $z_\ell<K$, while $z_\ell\geq K$ is already zero.
Therefore the full multiplicity cap is

$$
\begin{aligned}
\sum_{\ell\geq0}(2\ell+1)a_\ell
&\leq
1\cdot6+3\cdot5+5\cdot5+7\cdot4+9\cdot4\\
&\quad+11\cdot3+13\cdot3+15\cdot3
+17\cdot2+19\cdot2\\
&\quad+21+23+25+27\\
&=395.
\end{aligned}
\tag{38}
$$

This table is an exhaustive strict-phase proxy inventory; no angular or
radial multiplicity is omitted.

It remains to pay 395.  From (3),

$$
11+22\pi>11+22\frac{333}{106}
=80+\frac6{53},
$$

so

$$
\rho<\rho_c<\frac{11}{80}.
\tag{39}
$$

On $\mathcal B$, $K\geq5/(2\rho)$.  Hence, using the upper bound on
$\pi$ in (3),

$$
\begin{aligned}
\mathcal W(\rho,K)
&\geq\frac{125}{36\pi}(\rho^{-3}-1)\\
&>\frac{125}{36}\frac{113}{355}
\left[\left(\frac{80}{11}\right)^3-1\right]\\
&=\frac{160293325}{378004}\\
&=395+\frac{10981745}{378004}>395.
\end{aligned}
\tag{40}
$$

Equations (31), (38), and (40) prove (5) on all of $\mathcal B$,
including its lower face $\mu=5/2$.

## 6. Inherited faces and the ceiling branches

The assigned set (1) preserves all inherited face ownership.

- The face $\rho=\sigma$ is already covered by the small-hole wedge and is
  excluded here.
- The face $K=\sqrt{114}$ is included in `lower-next-wall.md` and is
  excluded here.
- The face $\rho=\rho_c$ remains assigned to the separate high-ratio
  component and is not claimed here.
- The face $K=U(\rho)$ is inherited covered and excluded from (1).  The
  stronger theorem (5) overlaps it, but this note does not reassign its
  owner.

There are exactly two active ceiling branches on the present ratio range.
The accepted switch satisfies

$$
\sigma<\frac1{12}<\frac{9407}{100000}<\rho_{HK}
<\frac{94071}{1000000}<\frac18<\rho_c.
\tag{41}
$$

The last comparison follows from $\pi<355/113<7/2$.  Therefore

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\sigma<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\leq\rho<\rho_c.
\end{cases}
\tag{42}
$$

At $\rho_{HK}$ the common value is selected by the $K_0$ branch.  The
$H_0$ eligibility face $\rho=\omega _0$ occurs after this switch and does
not change the active minimum.  The inherited estimate
$U(\rho)>63/4>11>\sqrt{114}$ shows that every ratio fiber in (1) is
nonempty.  Neither proof branch above uses a continuity assumption at the
switch or at $\rho=\omega _0$.

## 7. Exact covered set, residual, and verdict

The aggregate branch proves

$$
\left\{\sigma<\rho<\rho_c, K>\sqrt{114}\right\}
\setminus\mathcal B,
\tag{43}
$$

and the cap-395 branch proves $\mathcal B$.  Hence the exact face-connected
covered set requested in this exploration is all of (1):

$$
\boxed{
\mathcal C_{20}^{\rm L,rem}
=\left\{(\rho,K):
\sigma<\rho<\rho_c,
\quad \sqrt{114}<K<U(\rho)\right\}.}
\tag{44}
$$

Its residual inside the assigned component is

$$
\boxed{
\mathcal R_{20}^{\rm L}\setminus
\mathcal C_{20}^{\rm L,rem}=\varnothing.}
\tag{45}
$$

Combining (44) with the two PASS notes named in Section 1 would therefore
close the complete prospective post-Round-19 lower-ratio component, with
all old frequency and ratio faces retained.  That union is prospective
only: proof-free freezing, isolated reconstruction, exact-constant review,
adversarial review, and a judge are still required before promotion.

**Verdict: PASS.**  The first unsupported implication is **none within the
assigned set**.  The apparent obstruction from the failed uniform
one-unit shortcut is removed by summing the exact floor gains.  Its sole
remaining floor cell is closed independently by the exact cap $395$ and
the Weyl lower payment $>424$.
