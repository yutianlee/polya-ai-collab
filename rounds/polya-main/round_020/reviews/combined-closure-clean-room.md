# Round 20 Combined-Closure Clean-Room Review

**Initial verdict: PASS.**

**First unsupported implication: none.**  The three spectral claims (5),
(7), and (9), the threshold assertions (11), and the exact subtraction
(12)--(13) all admit an independent reconstruction from the frozen input
set.  The proof below does not use agreement with an incumbent, a numerical
root sample, or a prospective constant ledger.

## 1. Isolation and authentication

I authenticated each local input before opening it.  The reproduced hashes
were:

| input | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/shell_weyl_bessel.md` | `ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade` |
| `sources/bessel_phase_enclosures.md` | `e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c` |

The only external pages consulted were the four exact identities authorized
by Section 7:

- `https://dlmf.nist.gov/10.47.E3`;
- `https://dlmf.nist.gov/10.49.i`;
- `https://dlmf.nist.gov/10.51.E1`;
- `https://dlmf.nist.gov/10.51.E2`.

I certify that I did not inspect any other Round 20 exploration, any
Round 20 zero card, any computation or constant ledger other than the two
accepted residual-classifier files above, any release audit, any incumbent
response, any other clean-room or cross-review, any judge draft, any Git
diff or log, or the Round 19 internal zero proof.  I did not receive or read
another agent's work.  All finite calculations used below reduce to exact
rational arithmetic, alternating-series enclosures, or explicit radical
comparisons.  No sampled computation is used as proof.

For repeated elementary estimates I used

$$
\frac{103993}{33102}<\pi<\frac{104348}{33215},
\qquad
\frac{333}{106}<\pi<\frac{22}{7}.
\tag{A1}
$$

Both follow directly from Machin's formula
$\pi=16\arctan(1/5)-4\arctan(1/239)$ and alternating arctangent sums
(eight terms for the first arctangent and three for the second already give
the stronger displayed enclosure).  Every radical comparison below is
between positive quantities and is therefore certified after squaring.

## 2. Common spectral and variational lemmas

Let $q_{\ell,n}(\rho)$ denote the $n$-th frequency of the fixed angular
channel.  Separation into the form

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad H_0^1(\rho,1),
$$

gives a simple radial spectrum and angular multiplicity $2\ell+1$.
Accidental equality between different angular channels is harmless: the
orthogonal multiplicities add.  The strict count is

$$
N_D(A_{\rho,1},K^2)
=\sum_{\ell\ge0}(2\ell+1)
  \#\{n:q_{\ell,n}(\rho)<K\}.
\tag{A2}
$$

The following three comparisons have the claimed directions and preserve
both angular channel and radial index:

$$
q_{\ell,n}^2\ge n^2z_\rho^2+\ell(\ell+1),
\qquad q_{0,n}=nz_\rho,
\tag{A3}
$$

$$
q_{\ell,n}^2\ge j_{\ell+1/2,n}^2,
\tag{A4}
$$

$$
j_{p+1/2,n}^2\ge j_{\ell+1/2,n}^2
 +p(p+1)-\ell(\ell+1) \quad(p\ge\ell).
\tag{A5}
$$

For (A3), the one-dimensional Dirichlet Poincare inequality on an interval
of length $1-\rho$ gives $n^2z_\rho^2$, while $r^{-2}\ge1$ gives the
constant angular term.  The $\ell=0$ potential vanishes, so equality is
exact.  For (A4), extend a shell radial form function by zero to $(0,1)$;
this is an isometry into the fixed-$\ell$ ball form domain, and min--max
gives shell frequency at least ball frequency.  For (A5), compare the two
ball forms on the same $H_0^1(0,1)$ domain and use
$r^{-2}\ge1$.  These arguments also prove that equality in an (A3)
threshold cannot create a strictly counted mode.

At $K=z_\rho$, (A3) excludes every mode.  At $K=k_m$, it excludes the
first mode in channel $\ell=m$.  Thus all checkpoint faces have the strict
ownership asserted in the candidate.

## 3. Independent reconstruction of the zero registry

DLMF 10.47.3 identifies positive zeros of $J_{\ell+1/2}$ with those of
the spherical function $\mathsf j_\ell$.  Put

$$
\mathsf j_\ell(x)=\frac{S_\ell(x)}{x^{\ell+1}},
\quad
S_0=\sin x,
\quad S_1=\sin x-x\cos x,
$$

$$
S_{\ell+1}=(2\ell+1)S_\ell-x^2S_{\ell-1}.
\tag{A6}
$$

This is exactly the DLMF recurrence.  ODE uniqueness makes every positive
zero simple.  The derivative recurrence, together with (A6), gives the
usual finite Sturm chain: signs at consecutive zeros alternate and there is
exactly one zero in each cell recorded below.  Starting from the zeros
$n\pi$ of $S_0$, the relevant positive-zero cells are:

| $\ell$ | positive-zero cells needed |
|---:|---|
| 1 | $(\pi,3\pi/2)$, $(2\pi,5\pi/2)$, $(3\pi,7\pi/2)$ |
| 2 | $(3\pi/2,2\pi)$, $(5\pi/2,3\pi)$, $(7\pi/2,4\pi)$ |
| 3 | $(2\pi,5\pi/2)$, $(3\pi,7\pi/2)$ |
| 5 | $(5\pi/2,3\pi)$, $(4\pi,9\pi/2)$ |
| 6 | $(3\pi,7\pi/2)$ |
| 7 | $(7\pi/2,4\pi)$ |

There is no zero at a tangent endpoint: substitution in (A6) gives a
nonzero polynomial multiple of $\sin x$ or $\cos x$.  The Sturm chain
therefore enumerates, rather than merely detects, the indicated positive
zero.  The convention is always the positive zero; the high-order zero at
$x=0$ is not in the enumeration.

For a fully rational sign check, expand sine and cosine through degree 80;
the Lagrange remainder on every displayed rational argument is at most
$x^{81}/81!$.  Substitution in (A6) gives:

| target | exact enclosure for $S_\ell$ at the target | conclusion |
|---|---:|---|
| $S_1(77/10)$ | $(-1/5,-19/100)$ | $j_{3/2,2}>77/10$ |
| $S_1(21/2)$ | $(411/100,103/25)$ | $j_{3/2,3}>21/2$ |
| $S_2(9)$ | $(-151/20,-377/50)$ | $j_{5/2,2}>9$ |
| $S_2(61/5)$ | $(1807/100,452/25)$ | $j_{5/2,3}>61/5$ |
| $S_3(103/10)$ | $(-125,-124)$ | $j_{7/2,2}>103/10$ |
| $S_5(129/10)$ | $(-22629,-22628)$ | $j_{11/2,2}>129/10$ |
| $S_6(10)$ | $(445013,445014)$ | $j_{13/2,1}>10$ |
| $S_7(23/2)$ | $(3664453,3664454)$ | $j_{15/2,1}>23/2$ |

In every row the target lies strictly inside the stated tangent cell and
has the same sign as its left endpoint, so the uniquely enumerated zero is
strictly to its right.

For the remaining first zeros, Lorch's (L2) simplifies at
$\nu=\ell+1/2$ to

$$
j_{\ell+1/2,1}^2>
\frac{3(2\ell+3)\sqrt{(\ell+2)(\ell+6)}-2\ell^2+\ell+6}{4}.
\tag{A7}
$$

After moving the rational term and squaring positive sides, the exact
integer residuals are:

| $\ell$ | rational target | positive squared residual |
|---:|---:|---:|
| 5 | $87/10$ | $198189$ |
| 8 | $71/6$ | $35171$ |
| 9 | $64/5$ | $6939644$ |
| 10 | $69/5$ | $12281264$ |

Thus (A7) proves, in particular, the last three first-zero obligations in
(27).  The source-card specializations give
$j_{5/2,1}>51/10$, $j_{7/2,1}>13/2$, and
$j_{9/2,1}>15/2$.  Equations (A5)--(A7) provide every same-radial-index
angular propagation used below.  This proves all eleven bounds in (27),
including their strict direction, without importing a zero location.

## 4. Lower closure

### 4.1 Shifted-tail wedge

For a low-interface tail starting at $x_0=r+1/2<\mu:=\rho K$, put

$$
n=\lfloor\mu-r-1/2\rfloor,
\qquad p=\lfloor\omega_0K\rfloor.
$$

The authenticated concave/convex split gives

$$
\frac{\mathcal T_r}{2}
<\int_{x_0}^{K}A_{\rho,K}(z)\,dz
\delta-\frac{p-n}{4},
\qquad
0\le\delta<\frac{2(\mu-q)^{5/2}}{15\sqrt\mu},
\tag{A8}
$$

where $q$ is the largest half-integer not exceeding $\mu$.  The head is
absent when $n=0$; (A8) then follows directly from the convex tail, so no
degenerate trapezoid is used.

The enclosure (A1) and elementary radical squaring give
$\omega_0d>1$.  If $0<\rho\le\sigma=3\omega_0/4$, $K>d$, and
$\rho K>1/2$, then, for every active low tail,

$$
p-n\ge
\lfloor\omega_0K\rfloor-
\lfloor\rho K-r-1/2\rfloor\ge1.
\tag{A9}
$$

Indeed, with $x=\omega_0K>1$ and $m=\lfloor x\rfloor$, the right floor
is at most $\lfloor3x/4-1/2\rfloor<m$.  Also
$\delta<2\sqrt2/15<1/4$.  Hence the error in (A8) is strictly negative.
The dimension-reduction identity and its strict phase bridge therefore
prove (14).

For $\rho_*<\rho\le\rho_0$, $K>L(\rho)$ implies both
$K>d$ and $\rho K>1/2$; for
$\rho_0\le\rho\le\sigma$, $K>d$ again implies
$\rho K>1/2$.  This proves the stated consequence (16), with
$(\rho_0,d)$ excluded exactly as claimed.

### 4.2 Finite lower staircase

For $\rho_0<\rho<\rho_c$ and $K\le\sqrt{114}$, (A3)--(A7) give the
following complete possibilities:

| open lower frequency face | newly possible modes | cumulative cap |
|---|---|---:|
| $d<K\le10$, $K\le3z_\rho$ | first $0{:}5$, second $0{:}2$ | 45 |
| $d<K\le10$, $K>3z_\rho$ | preceding plus $(0,3)$ | 46 |
| $10<K\le81/8$ | plus first $(6,1)$ and possible $(0,3)$ | 59 |
| $81/8<K\le21/2$ | plus $(3,2)$ | 66 |
| $21/2<K\le\sqrt{7073}/8$ | plus $(1,3)$ | 69 |
| $\sqrt{7073}/8<K\le\sqrt{114}$ | plus $(4,2)$ | 78 |

The numbers are full multiplicity sums.  For example, the first two radial
layers through $\ell=5$ and $\ell=2$ contribute $36+9=45$.
The threshold $\sqrt{7073}/8$ follows from
$(81/8)^2+[4\cdot5-3\cdot4]=7073/64$.

The omitted modes are genuinely absent: first modes $\ell\ge7$ follow
from $j_{13/2,1}>10$ and (A5); second modes $\ell\ge5$ follow from
$j_{11/2,2}>129/10$; third modes $\ell\ge2$ follow from
$j_{5/2,3}>61/5$; and $n\ge4$ is excluded already by
$q_{0,4}=4z_\rho>\sqrt{114}$.  Equality at every zero or propagation
wall is excluded by the strict count.  In particular the lower face of
each row is open and its upper face is included.

For a uniform payment, $\rho<\rho_c<1/7$ and $\pi<22/7$ give

$$
\mathcal W(\rho,K)>
\frac{2}{9(22/7)}\left(1-\frac1{7^3}\right)K^3.
\tag{A10}
$$

At the successive strict lower faces, the exact reserves over the relevant
caps are at least

$$
\frac{2908}{539},\quad
\frac{6199}{539},\quad
\frac{990435}{137984},\quad
\frac{555}{44},\quad
\frac{159}{44},
\tag{A11}
$$

where the first number even pays cap 46 using only $K>9$, and the last pays
cap 78 using only $K>21/2$.  Thus every row pays strictly, including
$K=\sqrt{114}$, and (18) follows.

### 4.3 Remaining lower frequencies

Assume $\sigma<\rho<\rho_c$ and $K>\sqrt{114}$.  Then
$p=\lfloor\omega_0K\rfloor\ge1$ and
$m=\lfloor\rho K-1/2\rfloor$.  Off the exceptional box (21):

- if $\rho K<5/2$, then $m\le1\le2p-1$;
- if $K\ge2/\omega_0$, then $p\ge2$, and
  $\rho_c<3\omega_0/2$ gives
  $\rho K-1/2<2p$.

Therefore

$$m\le2p-1$$

on the complete complement of $\mathcal B$.  Equality
$K=2/\omega_0$ is on the high side, as required.

For non-half-integral $\mu=\rho K$, all low-interface tails have the same
remainder $\delta$, and summing (A8) over $r=0,\ldots,m$ gives the average
floor reserve

$$
\frac14\left(p-\frac m2\right)\ge\frac18.
$$

If $m=0$, instead use $p\ge1$ and
$\delta<2\sqrt2/15<1/4$.  If $m\ge1$, then
$\mu>3/2$ and

$$
\delta<\frac{2}{15\sqrt{3/2}}<\frac18.
$$

At $\mu\in\mathbb Z+1/2$, assign the interface to the high side.  Then
$\delta=0$ and the summed floor reserve is nonnegative; strictness remains
in the nonzero convex tail/integration step.  This settles every floor wall
and both half-integer conventions.

On $\mathcal B$, $K<R=367/20$.  The global strict phase proxy gives the
radial caps

$$
(6,5,5,4,4,3,3,3,2,2,1,1,1,1,0,0,\ldots)
$$

for $\ell=0,1,\ldots$.  Exact evaluation of the monotone action at $R$
(alternating arctangent series after
$\arccos t=\arctan(\sqrt{1-t^2}/t)$) places each proxy strictly below its
next integer.  The multiplicity sum is exactly

$$
\sum_{\ell=0}^{13}(2\ell+1)c_\ell=395.
$$

The $\ell=14$ proxy is below one and monotonicity removes every omitted
angular tail.  Finally $\rho K\ge5/2$ and $\rho<\rho_c$ imply

$$
\mathcal W(\rho,K)>
\frac{125}{36\pi}(\rho_c^{-3}-1)
=\frac{125}{36}(6+12\pi+8\pi^2)
>395+\frac{520295}{16854}.
\tag{A12}
$$

This proves (20).  Combining the wedge, finite staircase, and remaining
frequency theorem proves (5) on both lower components, with the complete
$\rho=\rho_0$ fiber and every $d$, $\sqrt{114}$, and $U$ face assigned as
in the candidate.

## 5. High staircase through $k_{11}$

### 5.1 Exhaustive modes and cap tables

For $z=z_\rho$ define strict lower proxies

$$
b_{\ell,n}(z)^2=
\max\{n^2z^2+\ell(\ell+1),\ \beta_{\ell,n}^2\},
\tag{A13}
$$

where the needed rational ball bounds are

$$
\begin{array}{c|cccccccccc}
(\ell,1)&1&2&3&4&5&6&7&8&9&10\\
\beta_{\ell,1}&4&51/10&13/2&15/2&87/10&10&23/2&71/6&64/5&69/5,
\end{array}
$$

$$
\beta_{1,2}=77/10,
\quad\beta_{2,2}=9,
\quad\beta_{3,2}=103/10,
\quad\beta_{4,2}=\sqrt{11409}/10,
\quad\beta_{1,3}=21/2.
$$

The $\ell=0$ proxies are exact: $b_{0,n}=nz$.  By (A2)--(A5), a mode can
be counted only if $b_{\ell,n}(z)<K$.

At the five checkpoints, this proves exactly the candidate inventories:

- $k_7$: first $0{:}6$, second $0{:}1$, no $n\ge3$;
- $k_8$: first $0{:}7$, second $0{:}3$, no $n\ge3$;
- $k_9$: first $0{:}8$, second $0{:}4$, no $n\ge3$;
- $k_{10}$: first $0{:}9$, second $0{:}5$, third $0{:}1$, no $n\ge4$;
- $k_{11}$: first $0{:}10$, second $0{:}4$, third $0{:}1$, no $n\ge4$.

The $k_{10}$ allowance of $(5,2)$ is conservative; the stronger combined
bounds actually exclude it.  Keeping it cannot invalidate a cap.  At
$k_{11}$ it is excluded because a counted $(5,2)$ would require both
$z^2<34$ from (A3) and
$z^2>(129/10)^2-132=3441/100$.  First channel $\ell=11$ and every larger
channel are absent because their (A3) lower face is at least $k_{11}$.
Also $q_{0,4}=4z>k_{11}$ already at
$z\ge\pi+1/2$.  This checks radial indices 1--4 and every angular index
0--11 explicitly.

Writing $H$ for the highest possible first channel and $h$ for the highest
second channel, full multiplicity gives
$(H+1)^2+(h+1)^2$, with a further $1$ or $4$ for third modes.  Recalculation
of every proposed cap gives:

$$
\begin{array}{c|ccccc}
k_8&H\backslash h&\varnothing&0&1&2&3\\\hline
&7&64&65&68&73&80\\
&6&49&50&53&-&-\\
&5&36&37&40&45&52\\
&\le4&25&26&29&34&41
\end{array}
$$

and

$$
\begin{array}{c|cccccc}
k_9&H\backslash h&\varnothing&0&1&2&3&4\\\hline
&8&81&-&-&-&-&-\\
&7&64&65&68&73&-&-\\
&6&49&50&53&58&65&74\\
&5&36&37&40&45&52&61\\
&\le4&25&26&29&34&41&50.
\end{array}
$$

The marked impossible $k_8$ cells follow from $H=6\Rightarrow z^2>28$
and $h\ge2\Rightarrow z^2<22$.  The marked $k_9$ cells follow from
$H=8\Rightarrow z^2>1801/36$, whereas any second mode requires
$z^2<30$; $H=7,h\ge3$ is already contradicted by
$z^2>169/4$ and $z^2\le26$.  Thus every dash is justified, not inferred
from the table.

For $k_{10}$ the candidate cap list is

$$
100; 81,97; 64,80,89,100; 74,69,78,85,89,
$$

and for $k_{11}$ it is

$$121; 100,125; 106,110; 93.$$

Each is the corresponding square sum.  The restrictions follow from:

$$
\begin{array}{c|l}
k_{10},H=9&z^2>1346/25>110/3:\ \text{no second or third},\\
k_{10},H=8&z^2>1081/36>30:\ h\le3,\ \text{no third},\\
k_{10},H=7&z^2>89/4>110/8:\ \text{no third},\\
k_{11},H=10&z^2>1461/25>44:\ \text{no second or third},\\
k_{11},H=9&z^2>796/25>33/2:\ \text{no third},\\
k_{11},H=8&h\le4\ \text{by the }(5,2)\text{ contradiction above}.
\end{array}
$$

For $k_7$, the first sums $25,36,49$ and possible second contribution
$1+3$ reproduce every proposed cap.

### 5.2 Strict Weyl payment

Define the finite integer proxy

$$
C_z(K)=\sum_{(\ell,n)\text{ in (A13)}}(2\ell+1)
\mathbf 1_{\{b_{\ell,n}(z)<K\}}.
\tag{A14}
$$

The preceding inventory proves $N_D\le C_z$ through $k_{11}$.  Between
two proxy jumps, $C_z$ is constant and $\mathcal W$ strictly increases in
$K$, so it suffices to pay the right side of every jump.  This is a finite
analytic check, not a sampled one.  Squared proxy crossings are affine
equalities in $z^2$.  For a moving face
$K^2=sz^2+d$, differentiation gives the exact sign numerator

$$
s\pi^2\frac{1+\rho}{(1-\rho)^2}-\rho^2d;
\tag{A15}
$$

constant faces decrease with $\rho$.  Thus each event cell reduces to an
endpoint or a single constant/moving crossing.  Substitution of (A1) gives
the following worst event in each band; all other cap cells have a larger
exact rational reserve:

| frequency band | worst post-jump cap | certified lower data | exact reserve $\mathcal W-C_z$ |
|---|---:|---|---:|
| $z\le K\le k_6$ | 9 | $K>51/10$, $\rho<3/10$ | $>1387329/11000000$ |
| $k_6<K\le k_7$ | 29 | $K>77/10$, $\rho<1/5$ | $>849901/281250$ |
| $k_7<K\le k_8$ | 81 | $K>71/6$, $\rho<2/3$ | $>835355/577368$ |
| $k_8<K\le k_9$ | 81 | $K>71/6$, $\rho<2/3$ | $>835355/577368$ |
| $k_9<K\le k_{10}$ | 97 | $K>71/6$, $\rho<1/2$ | $>943655/171072$ |
| $k_{10}<K\le k_{11}$ | 106 | $K>71/6$, $\rho<3/7$ | $>507845/261954$ |

For example, the last line is simply

$$
\frac{2}{9(22/7)}
\left(1-(3/7)^3\right)(71/6)^3-106
=\frac{507845}{261954}>0.
$$

The finite reduction uses every proposed split ratio.  In increasing order
they are

$$
\frac15,\frac3{10},\frac13,\frac38,\frac25,
\frac5{12},\frac37,\frac12,\frac8{15},\frac{107}{200},
\frac35,\frac{16}{25},\frac{13}{20},\frac23,
$$

together with $4/25$, $1/4$, $7/20$ and the three algebraic faces
$z^2=16,68/3,34$.  Substitution on both sides of every face in (A13)--(A15)
gives the same or a strictly stronger reserve; at a defining equality the
indicator in (A14) is zero.  Thus no mode is acquired on the wrong side.

The advertised $k_{11}$ localizations follow immediately and strictly:

$$
(\ell,2)\text{ counted}\Rightarrow z^2<44
\Rightarrow\rho<\frac8{15},
$$

$$
(\ell,3)\text{ counted}\Rightarrow z^2<\frac{33}{2}
\Rightarrow\rho<\frac14.
$$

At $\rho=8/15$ and $1/4$, (A1) reverses the required strict $z^2$
inequality, so the defining mode is excluded.  Similarly, at $k_{10}$ a
third mode forces $\rho<4/25$; at $k_8$ a nonradial second mode forces
$\rho<7/20$.  The $H=10$ and $H=9$ exclusions were proved above.  Every
ratio and algebraic split therefore has both one-sided traces and its
equality owner.

At $K=z$ the count is zero; at every $K=k_m$, the channel-$m$ first mode
is excluded.  Coincident jumps add all $2\ell+1$ weights before payment,
as in (A14).  The strict reserves prove (7) on the entire closed staircase,
including $\rho=\rho_c$ and $\rho=7/8$.

## 6. Optical theorem

Put $\varepsilon=1-\rho$, $a=\varepsilon K$, and
$0<\varepsilon\le11/50$.  The low and high screens are both inclusive at
$a=c/\varepsilon$, where $c=1126/625$.

### 6.1 Product screen

From (A3), a counted mode must satisfy

$$n^2\pi^2+\varepsilon^2\ell(\ell+1)<a^2.$$

For $a\le\pi$ this has no solution; at $a=\pi$ the first radial wall is
excluded.  For $a>\pi$, write

$$
\frac a\pi=N+t,
\qquad N\ge1,
\qquad0<t\le1,
$$

using $(N,t)=(m-1,1)$ at $a=m\pi$.  The exact angular count is bounded by

$$
\mathcal P_\varepsilon(a)=\sum_{n=1}^N M_n^2,
\quad
M_n=\left\lceil
\sqrt{(b_n/\varepsilon)^2+\frac14}-\frac12
\right\rceil,
$$

because $\sum_{\ell=0}^{M-1}(2\ell+1)=M^2$.  At an angular equality the
strict inequality in $\ell(\ell+1)$ makes this same ceiling formula exact.

Direct summation gives

$$
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
\tag{A16}
$$

Let $C_D=1382/3125$.  For fixed $t$, the difference
$D/\pi^2-C_D(N+t)^2$ increases for $N\ge1$, because its $N$ derivative is
bounded below by

$$\frac{5074831}{58593750}>0.$$

At $N=1$ its derivative in $t$ is
$2(t-C_D)(t+1)$, so its minimum is at $t=C_D$, where it equals

$$\frac{1822532}{91552734375}>0.$$

Therefore

$$D(a)>\frac{1382}{3125}a^2$$

for every $a>\pi$, including both traces of every radial wall.

The elementary ceiling inequality and the quarter-circle integral give

$$
\varepsilon^2\mathcal P_\varepsilon
<S_0+\varepsilon\frac{a^2}{4}
 +\varepsilon^2\frac a\pi.
$$

Since the Weyl target after multiplication by $\varepsilon^2$ is
$I(a)(1-\varepsilon+\varepsilon^2/3)$, it is enough that

$$
D(a)\ge\varepsilon\left(I(a)+\frac{a^2}{4}\right)
 +\frac{\varepsilon^2a}{\pi}.
\tag{A17}
$$

On $a\le c/\varepsilon$, $a\ge\pi$, use
$q=106/333>1/\pi$ and $\varepsilon\le11/50$.  Dividing (A17) by $a^2$,
the exact remaining reserve is

$$
C_D-\left(\frac{2cq}{3}+\frac{11}{200}
 +\left(\frac{11}{50}\right)^2q^2\right)
=\frac{39569}{2772225000}=R_L>0.
\tag{A18}
$$

Thus the low screen is strict for $K>0$ and includes the common face.

### 6.2 Complementary-action screen

For the high screen, differentiation of the exact action (H1) gives a
strictly decreasing inverse $R$, $F=R^2$, and $g=-F'>0$.  Direct
differentiation on the two action branches gives

$$
g\text{ decreasing on }(0,\tau),
\qquad g\text{ increasing on }(\tau,T),
$$

$$
F(0)=a^2,quad F(\tau)=\rho^2a^2,quad F(T)=0,
\quad g(T)=2\pi\rho a.
\tag{A19}
$$

These statements remain valid when $\tau$ lies below, on, or above a
sawtooth node; no assumption $\tau>1$ enters.

For $C(t)=\#\{n:n-1/4<t\}$, let $w=t-C(t)$ and
$W(t)=\int_0^t w$.  A one-period calculation gives
$W\ge0$ and, with $\Psi=W-t/4$,
$-1/32\le\Psi\le3/32$.  Stieltjes integration, split at the actual
$\tau$, gives

$$
D_{\rm rad}
=\int_0^TF-\sum_{n-1/4<T}F(n-1/4)
\ge\frac{F(\tau)}4-\frac{g(T)}8
=\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\tag{A20}
$$

The improper trace at $t=0$ is obtained by monotone truncation; the terminal
term is (A19).  Every discarded Stieltjes term is nonnegative.

The exact half-integer layer count is

$$
M_\varepsilon(x)=\max\left\{0,
\left\lceil x/\varepsilon-1/2\right\rceil\right\}.
$$

It satisfies the strict inequality
$\varepsilon^2M_\varepsilon(x)^2<(x+\varepsilon/2)^2$ even on a
half-integer wall.  Since the number of radial layers is strictly less than
$a/\pi+1/4$, the complete angular error is strictly below

$$
E=\left(\frac a\pi+\frac14\right)
  \left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\tag{A21}
$$

For $a\ge c/\varepsilon$, (A20), $\pi<22/7$, and (A21) give

$$
\frac{D_{\rm rad}}{a^2}\ge
\frac{(1-\varepsilon)^2}{4}
-\frac{22(1-\varepsilon)\varepsilon}{28c},
$$

$$
\frac Ea^2\le
\varepsilon q+\frac{\varepsilon^2}{4c}
+\frac{\varepsilon^3q}{4c}
+\frac{\varepsilon^4}{16c^2}.
\tag{A22}
$$

The first side decreases and the second increases on
$0<\varepsilon\le11/50$.  At the closed endpoint their exact difference is

$$
\frac{14817541}{472867032960000}=R_H>0.
\tag{A23}
$$

Consequently the strict layer-cake sum is below the continuous action and
$P_{\mathcal A}<I$.  The phase bridge then proves
$N_D<\mathcal W$ throughout the high screen, including
$a=c/\varepsilon$.  At $K=0$, both sides are zero.  This proves (9), with
strict comparison for every $K>0$.

Every optical face in the candidate is now owned: $a=\pi$, all
$a=m\pi$, product angular equalities, action half-integer walls,
phase-proxy integer walls, the common face, and
$\varepsilon=11/50$.  The open limit $\varepsilon\downarrow0$ is not
treated as a shell in the domain.

## 7. Constants, upper floor, and exact subtraction

The enclosures (A1) and elementary radical bounds give

$$
0.0310<\rho_*<0.0311,
\quad0.05447<\rho_0<0.05448,
\quad0.08174<\sigma<0.08175,
\quad0.13730<\rho_c<0.13731.
$$

Hence

$$
\rho_*<\rho_0<\sigma<\rho_c<\frac{39}{50}<\frac78.
\tag{A24}
$$

For every $\rho\ge\rho_c$, the parameter
$a_\rho=2\pi\rho/(1-\rho)\ge1$.  Also
$\eta_\rho\le G_1(1/2)=\omega_0<1/8$.  Therefore

$$
K_0(\rho)>
\frac{a_\rho}{\eta_\rho^2}>64.
$$

On $\rho<7/8$, $z_\rho<8\pi$, so $k_{11}<64$.  For
$\rho\ge5/6$, the seam branch $54/(1-\rho)^2$ is greater than 1944.
Thus every eligible upper-floor branch is strictly above $k_{11}$ and

$$k_{11}(\rho)<U(\rho)\qquad(\rho_c\le\rho<7/8).$$

On $\rho_c\le\rho<39/50$, one has $\rho>\omega_0$ and
$\rho<5/6$, so neither $H_0$ nor the seam is eligible.  Hence

$$U(\rho)=K_0(\rho)$$

on exactly the required interval.

It remains only set algebra.  Removing $\mathcal D_{19}^{\rm low}$ deletes
the first two components of $\mathcal D_{19}$, including the
$\rho=\rho_0$ fiber.  In the third component, the staircase removes

$$k_6<K\le k_{11};$$

the $k_6$ face was already owned and the $k_{11}$ face is newly owned.
Because $k_{11}<U$, what remains is $k_{11}<K<U$.  The optical piece then
removes precisely the ratios $39/50\le\rho<7/8$, including the
$39/50$ face.  Thus

$$
\mathcal D_{19}\setminus
\bigl(\mathcal D_{19}^{\rm low}
 \cup\mathcal C_{20}^{\rm stair}
 \cup\mathcal C_{20}^{\rm opt}\bigr)
=\left\{\rho_c\le\rho<\frac{39}{50},
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

This is exactly (12)--(13).  $B_0$ and $B_1$ were already subsets of the
accepted predecessor and do not enter this subtraction a second time.

## 8. Mandatory face ledger and proof map

- Ratio faces: $\rho_*$ and $7/8$ retain inherited complete owners;
  $\rho_0$ is in the first lower component; $\sigma$ is owned by the
  wedge; $\rho_c$ is owned by the high staircase; $39/50$ is owned by the
  optical theorem; $\rho=1$ is only an open limit.  The $H_0=K_0$,
  $\omega_0$, $1/2$, and $5/6$ faces do not change any spectral estimate,
  and both upper-floor one-sided traces agree with the stated owner.
- Lower frequency faces: $L$ and $d$ are excluded from the residual pieces
  that begin above them; $3z$, $10$, $81/8$, $21/2$,
  $\sqrt{7073}/8$, $\sqrt{114}$, and $2/\omega_0$ have the open/lower and
  closed/upper assignments used in Sections 4.2--4.3; $U$ is never in a
  residual.  Moving/fixed-wall changes are paid on both sides by (A10)--(A12).
- High faces: $z$, every $k_m$ for $6\le m\le11$, every rational zero
  wall, every ratio and algebraic split, and $U$ have been checked above.
  Equality excludes the defining strict mode.
- Optical faces: $K=0$ has equality; every $K>0$ is strict.  The radial,
  angular, action, proxy, common, and endpoint walls are covered by
  (A16)--(A23).
- Indices and coincidences: $n=1,2,3,4$ and $\ell=0,\ldots,11$ were
  explicitly treated.  The variational comparisons remove every remaining
  high or finite-lower index; the global phase proxy removes the entire
  exceptional-box tail.  Cross-channel coincidences always add full
  multiplicities before payment.

The concise implication map is

$$
\text{separation/min--max}
\Longrightarrow (A3)\text{--}(A5)
\Longrightarrow
\begin{cases}
\text{wedge + finite ledger + floor aggregate} &\Rightarrow (5),\\
\text{zero registry + finite jump payment} &\Rightarrow (7),\\
\text{product deficit + action deficit} &\Rightarrow (9),
\end{cases}
$$

followed by (A24), $k_{11}<U$, and literal set subtraction to obtain
(11)--(13).  No implication in this chain is unsupported.

## Final decision

**PASS; first issue: none.**
