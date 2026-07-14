# Round 19 Lower-Ratio Route

Date: 2026-07-14.

Status: **incumbent analytic exploration; not frozen, reviewed, judged, or
promoted**.

This note treats only the unchanged lower-ratio component of the frozen
post-Round-18 residual,

$$
\mathcal D_{18}^{\rm low}
=\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}.
\tag{1}
$$

No estimate valid only for $\rho\geq\rho_c$ is continued across the
$\rho=\rho_c$ face.  The result below is a separate fixed-channel
shell-to-ball argument.

## 1. Candidate compression

Put

$$
L(\rho)=\frac1{2\rho},
\qquad
\rho_c=\frac1{1+2\pi},
\qquad
d=\frac{\sqrt{337}}2.
\tag{2}
$$

The strongest band closed by the exact staircase developed here is

$$
\boxed{
\mathcal C_{19}^{\rm low}
=\left\{(\rho,K):
\frac1{\sqrt{337}}<\rho<\rho_c,
\quad L(\rho)<K\leq d\right\}.
}
\tag{3}
$$

Equivalently, because $L(\rho)<d$ exactly when
$\rho>1/\sqrt{337}$,

$$
\mathcal C_{19}^{\rm low}
=\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad L(\rho)<K\leq d\right\}.
\tag{4}
$$

For every point in (3), the argument below gives

$$
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{5}
$$

This is a candidate for later proof-free freezing and independent review,
not a promoted theorem.  In particular, it does not close (1), does not
touch the high-ratio component, and makes no assertion for $K>d$.

## 2. Fixed-channel comparison and the only zero inputs

For angular order $\ell$, write the transformed radial form as

$$
q_{\rho,\ell}[u]
=\int_\rho^1
\left(|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2\right)\,dr,
\qquad u\in H_0^1(\rho,1).
\tag{6}
$$

Extension by zero across $(0,\rho)$ maps this form domain into the
corresponding unit-ball fixed-$\ell$ form domain.  Min--max, at each radial
index $n$, therefore gives

$$
k_{\ell,n}^{\rm shell}(\rho)
\geq b_{\ell,n}:=j_{\ell+1/2,n}.
\tag{7}
$$

This is the internal channel-preserving comparison; no shell cross-product
zero is being attributed to a ball-zero source.

On the ball, the transformed fixed-angular form domains agree (Hardy's
inequality controls $r^{-2}$), and hence for $p>\ell$,

$$
b_{p,n}^2
\geq b_{\ell,n}^2+
\bigl(p(p+1)-\ell(\ell+1)\bigr).
\tag{8}
$$

The three already accepted Round 18 first-zero facts are

$$
b_{2,1}>\frac{51}{10},
\qquad
b_{3,1}>\frac{13}{2},
\qquad
b_{4,1}>\frac{15}{2}.
\tag{9}
$$

The narrow Round 19 source record
`sources/round19_bessel_zero_bounds.md`, together with its independent
audit, supplies exactly

$$
b_{5,1}>\frac{17}{2},
\qquad
b_{1,2}>\frac{77}{10}.
\tag{10}
$$

The first statement in (10) is the declared $\nu=11/2$ specialization of
Lorch's published inequality.  The second is an internal proof from
$\mathsf j_1(x)=(\sin x-x\cos x)/x^2$ and $\tan x=x$.  No other new
external Bessel order is used below.

For completeness, the first order-one zero also satisfies $b_{1,1}>4$.
Indeed, its root is in $(\pi,3\pi/2)$; with
$y=3\pi/2-4>1/2$, one has
$\tan4=\cot y<2<4$.

We also need one wholly internal second-zero estimate:

$$
\boxed{b_{2,2}>9.}
\tag{11}
$$

To prove it, use

$$
\mathsf j_2(x)
=\frac{(3-x^2)\sin x-3x\cos x}{x^3}.
\tag{12}
$$

For $x>3$ on each negative-tangent half-period, its zeros solve
$\tan x=-3x/(x^2-3)$.  The derivative comparison

$$
\sec^2x>
\frac{3(x^2+3)}{(x^2-3)^2},
\qquad
(x^2-3)^2-3(x^2+3)=x^2(x^2-9)>0,
\tag{13}
$$

shows that the left-hand side of
$\tan x+3x/(x^2-3)=0$ is strictly increasing on each negative-tangent
half-period.  It tends from $-\infty$ to a positive value on both
$(3\pi/2,2\pi)$ and $(5\pi/2,3\pi)$, so each interval contains exactly one
zero.  The accepted first-zero bound in (9), together with
$3\pi/2<51/10$, excludes every earlier positive zero, and the
positive-tangent half-period between these two intervals contains none.
Thus the zero in $(5\pi/2,3\pi)$ is $b_{2,2}$.

On that interval put

$$
g(x)=\tan(3\pi-x)-\frac{3x}{x^2-3}.
$$

The same calculation makes $g$ strictly decreasing.  The elementary
bounds $5\pi/2<9<3\pi$ put $9$ in this interval, and $333/106<\pi$
gives

$$
3\pi-9>\frac{45}{106}>\frac9{26}
=\frac{27}{78},
$$

and hence

$$
g(9)>\left(3\pi-9\right)-\frac{27}{78}>0.
$$

The unique zero is therefore strictly to the right of $9$, proving (11).

Two consequences of (8), (10), and (11) are

$$
b_{6,1}^2>b_{5,1}^2+12>\frac{337}{4}=d^2,
\tag{14}
$$

and

$$
b_{3,2}^2>b_{2,2}^2+6>87>d^2.
\tag{15}
$$

Thus, through the included face $K=d$, every first mode with $\ell\geq6$
and every second mode with $\ell\geq3$ is absent.  Also
$3z_\rho>3\pi>d$, since

$$
36\left(\frac{333}{106}\right)^2-337
=\frac{51368}{2809}>0,
\tag{16}
$$

so all third and higher radial modes are absent.  For $\ell=0$, the exact
shell frequencies are $nz_\rho$, where

$$
z_\rho=\frac\pi{1-\rho}.
\tag{17}
$$

More generally, the interval Poincare bound in (6) gives

$$
\bigl(k_{\ell,n}^{\rm shell}(\rho)\bigr)^2
\geq n^2z_\rho^2+\ell(\ell+1),
$$

which justifies the same exclusion for every $\ell$.

## 3. Exact multiplicity staircase

Let

$$
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{18}
$$

Since $\rho<\rho_c<1/7$ and $\pi<22/7$, every fixed $c>0$ obeys

$$
W(\rho,c)
>\frac{38}{539}c^3.
\tag{19}
$$

The strict-count caps below include full multiplicities $2\ell+1$.  At
$K=2z_\rho$ the second $\ell=0$ mode is excluded, so equality belongs to
the $K\leq2z_\rho$ row.

| candidate frequency range | possible modes | cap | exact payment |
|---|---|---:|---:|
| $L<K\leq4$ | $(0,1)$ | $1$ | $W(K)>W(z_\rho)>2$ |
| $4<K\leq51/10$ | first modes $\ell=0,1$ | $4$ | $W(4)>2432/539>4$ |
| $51/10<K\leq13/2$, $K\leq2z_\rho$ | first modes $\ell=0,1,2$ | $9$ | $W(51/10)>2520369/269500>9$ |
| $51/10<K\leq13/2$, $K>2z_\rho$ | preceding modes plus $(0,2)$ | $10$ | $W(K)>W(2z_\rho)>17$ |
| $13/2<K\leq15/2$, $K\leq2z_\rho$ | first modes $\ell=0,1,2,3$ | $16$ | $W(13/2)>41743/2156>16$ |
| $13/2<K\leq15/2$, $K>2z_\rho$ | preceding modes plus $(0,2)$ | $17$ | $W(K)>W(2z_\rho)>17$ |
| $15/2<K\leq77/10$ | first modes $\ell=0,\ldots,4$ plus $(0,2)$ | $26$ | $W(15/2)>64125/2156>26$ |
| $77/10<K\leq17/2$ | preceding modes plus $(1,2)$ | $29$ | $W(77/10)>16093/500>29$ |
| $17/2<K\leq9$ | preceding modes plus $(5,1)$ | $40$ | $W(17/2)>93347/2156>40$ |
| $9<K\leq d$ | preceding modes plus $(2,2)$ | $45$ | $W(9)>27702/539>45$ |

Here

$$
W(2z_\rho)
=\frac{16\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}
>\frac{49284}{2809}
=17+\frac{1531}{2809}.
\tag{20}
$$

Also $L(\rho)>z_\rho$ for $\rho<\rho_c$, so the first-row payment follows
from $K>L>z_\rho$ and

$$
W(\rho,z_\rho)
=\frac{2\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}>2.
\tag{21}
$$

Every lower threshold in the table is open.  At the threshold itself the
new mode is still excluded by strict counting and the preceding row owns
the face.  The upper face $K=d$ is included, and (14)--(16) exclude the
next possible modes there.  Thus every cap is strictly smaller than the
corresponding Weyl payment, proving (5).

## 4. The candidate really lies inside the frozen residual

On the whole lower-ratio interval, $\eta_\rho=\omega_0$.  On the $H_0$
branch,

$$
H_0(\rho)>H_0(\rho_*)
=\frac1{2\rho_*}=\frac{C_0}{\omega_0},
$$

while the defining formula for $K_0$ gives, because $a_\rho>0$,

$$
K_0(\rho)>\frac{C_0}{\omega_0}.
\tag{22}
$$

Exact elementary bounds give $C_0>7/4$ and $\omega_0<1/9$.  The first is
equivalent to $\sqrt2>45/32$ and follows by squaring.  For the latter,
$9\sqrt3<5\pi$ follows by positive squaring from

$$
25\left(\frac{333}{106}\right)^2-243
=\frac{41877}{11236}>0.
$$

Consequently

$$
U(\rho)>\frac{C_0}{\omega_0}>\frac{63}{4}>d
\qquad(\rho_*<\rho<\rho_c).
\tag{23}
$$

The identity $1/(2\rho_*)=C_0/\omega_0$ and the same strict bound imply
$\rho_*<2/63$.  Moreover $2/63<1/\sqrt{337}<\rho_c$; the first comparison
is $4\cdot337<63^2$, and $1/\sqrt{337}<1/8<\rho_c$.  Hence (3) is nonempty
and is wholly contained in (1).

If (3) is later promoted, exact subtraction leaves the lower-ratio
residual

$$
\boxed{
\begin{aligned}
&\left\{\rho_*<\rho\leq\frac1{\sqrt{337}},
\quad L(\rho)<K<U(\rho)\right\}\\
{}\cup{}&
\left\{\frac1{\sqrt{337}}<\rho<\rho_c,
\quad d<K<U(\rho)\right\}.
\end{aligned}}
\tag{24}
$$

Equivalently, it is
$\{\rho_*<\rho<\rho_c,\ \max\{L(\rho),d\}<K<U(\rho)\}$.
The slice $\rho=1/\sqrt{337}$ belongs to the first row of (24): there
$L=d$, and the candidate fiber $L<K\leq d$ is empty.

## 5. Crossing ledger for the true lower wall

For

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
$$

the function $L(\rho)^2-k_m(\rho)^2$ is strictly decreasing.  Thus each
sign change below gives a unique crossing.  With

$$
Q_m(r;p)=(1-r)^2-4p^2r^2
-4m(m+1)r^2(1-r)^2,
\tag{25}
$$

the left signs use the upper bound $p=355/113$ and the right signs use the
lower bound $p=333/106$.  All denominators displayed below are positive.

| wall | exact bracket for its crossing with $L$ | directed exact signs |
|---|---|---|
| $k_1$ | $129/1000<\rho_1<13/100$ | $1092040039511/1596125000000000>0$; $-441813249/35112500000<0$ |
| $k_2$ | $23/200<\rho_2<117/1000$ | $31992023413/2553800000000>0$; $-5919382249867/351125000000000<0$ |
| $k_3$ | $101/1000<\rho_3<51/500$ | $7779186345393/798062500000000>0$; $-77021496827/10972656250000<0$ |
| $k_4$ | $11/125<\rho_4<89/1000$ | $6696891136/623486328125>0$; $-304612112969/35112500000000<0$ |
| $k_5$ | $77/1000<\rho_5<39/500$ | $3744821245413/319225000000000>0$; $-47047654307/4389062500000<0$ |
| $k_6$ | $17/250<\rho_6<69/1000$ | $140918469867/12469726562500>0$; $-5078264998669/351125000000000<0$ |

The $z_\rho=k_0(\rho)$ crossing is exact:

$$
L(\rho)=z_\rho
\quad\Longleftrightarrow\quad
\rho=\rho_c.
\tag{26}
$$

The second radial wall has the exact crossing

$$
L(\rho)=2z_\rho
\quad\Longleftrightarrow\quad
\rho=\rho_{2z}:=\frac1{1+4\pi},
\tag{27}
$$

and directed rational signs give

$$
\frac{73}{1000}<\rho_{2z}<\frac{37}{500}
$$

with margins $1091/113000>0$ and $-103/26500<0$ in
$1-r-4\pi r$.  At this crossing
$z=\pi+1/4$ and

$$
k_5<2z<k_6.
\tag{28}
$$

Indeed, using the directed bounds on $\pi$,

$$
3z^2-30>\frac{202563}{44944}>0,
\qquad
42-3z^2>\frac{1530501}{204304}>0.
$$

Therefore

$$
\rho_6<\rho_{2z}<\rho_5<\rho_4<\rho_3<\rho_2<\rho_1<\rho_c.
\tag{29}
$$

For the last comparison, $\rho_1<13/100<7/51<\rho_c$, where
$7/51<\rho_c$ follows from $\pi<22/7$.

The fixed staircase faces meet the true lower wall at the exact ratios

$$
\begin{array}{c|ccccccc}
c&4&51/10&13/2&15/2&77/10&17/2&9\\ \hline
L(\rho)=c
&1/8&5/51&1/13&1/15&5/77&1/17&1/18.
\end{array}
\tag{30}
$$

The final candidate face meets it at
$\rho=1/\sqrt{337}$.  Empty subbands created by these crossings are simply
empty; no continuity from the high-ratio staircase is used to fill them.

For comparison with the requested method wall, throughout
$\rho<\rho_c$ one has $z_\rho<\pi+1/2<51/14$, and hence

$$
k_6(\rho)^2<\left(\frac{51}{14}\right)^2+42,
\qquad
d^2-k_6(\rho)^2>\frac{1420}{49}>0.
\tag{31}
$$

Thus (3) crosses and strictly surpasses the complete $k_6$ wall; it does
not merely stop there.

## 6. First obstruction above the proposed face

Immediately above $K=d$, the information used here no longer excludes the
first $\ell=6$ channel.  Before that entry the conservative cap is $45$;
allowing it adds multiplicity $13$ and raises the cap to $58$.

The Weyl payment cannot pay that crude jump at the wall.  Uniformly in
$\rho$,

$$
W(\rho,d)
<\frac{2}{27}d^3
=\frac{337\sqrt{337}}{108}<58,
\tag{32}
$$

where the final exact comparison follows by positive squaring:

$$
6264^2-337^3=964943>0.
$$

This is the first unsupported implication of a continuation of the present
cap method.  It is **not** a counterexample to the shell Pólya inequality.
A continuation needs at least one of: a sharper independently sourced or
internally proved $\ell=6$ first-zero delay, a shell-specific delay beyond
the unit-ball comparison, or a weighted payment that does not charge the
entire multiplicity jump at once.

## 7. Face ownership and non-overclaim

- $\rho=\rho_*$ remains the complete inherited endpoint and is not in
  (3).
- $\rho=1/\sqrt{337}$ has an empty candidate fiber and belongs to the
  first remaining-residual row in (24).
- $\rho=\rho_c$ is not claimed here; its ownership remains with the
  separate post-$k_5$ high-ratio workstream.
- $K=L(\rho)$ is inherited covered boundary and is excluded from (3).
- $K=d$ is included in (3); the remaining lower residual begins strictly
  above it when $\rho>1/\sqrt{337}$.
- $K=U(\rho)$ stays covered by its inherited $H_0$ or $K_0$ owner and is
  excluded from both (3) and (24).
- Equality at every spectral entry is assigned to the lower-count side by
  strict spectral counting.

The high-ratio residual and both pieces of (24) remain open.  No full
Pólya theorem is claimed.
