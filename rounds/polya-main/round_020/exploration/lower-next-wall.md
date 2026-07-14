# Round 20 Lower-Ratio Next-Wall Exploration

Date: 2026-07-14.

Status: **exploratory analytic note only; not frozen, reviewed, judged, or
promoted**.

This note works only on the prospective post-Round-19 component

$$
\mathcal D_{19}^{\rm L,+}
=\left\{(\rho,K):
\frac1{\sqrt{337}}<\rho<\rho_c,
\quad d<K<U(\rho)\right\},
\qquad
d=\frac{\sqrt{337}}2.
\tag{1}
$$

No Round 19 frozen claim, review, or state file is changed.  The purpose is
to identify the next rigorously payable lower-ratio band and the first
obstruction met by the same full-multiplicity cap method.

## 1. Result of the exploration

Put

$$
z_\rho=\frac{\pi}{1-\rho},
\qquad
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3,
\tag{2}
$$

and define the two new algebraic faces

$$
c_{42}=\frac{\sqrt{7073}}8,
\qquad
c_7=\sqrt{114}.
\tag{3}
$$

The exact order of all fixed faces used below is

$$
d<10<\frac{81}{8}<\frac{21}{2}
<c_{42}<c_7.
\tag{4}
$$

For the last two comparisons, the squared margins are respectively
$7073-7056=17$ and $7296-7073=223$.

The strongest complete band obtained here is

$$
\boxed{
\mathcal C_{20}^{\rm L}
=\left\{(\rho,K):
\frac1{\sqrt{337}}<\rho<\rho_c,
\quad d<K\leq\sqrt{114}\right\}.}
\tag{5}
$$

For every point of (5), the argument below gives

$$
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{6}
$$

For completeness, the inherited lower-ratio ceiling satisfies
$U(\rho)>63/4$.  Indeed, on this interval $\eta_\rho=\omega_0$, where

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\quad
C_*=\frac12+\frac{8\sqrt2}{15},
\quad
C_0=1+\frac{8\sqrt2}{15}.
$$

With $\rho_*=\omega_0/(1+2C_*)$, every eligible
$H_0(\rho)=C_*/(\omega_0-\rho)$ branch obeys
$H_0(\rho)>H_0(\rho_*)=C_0/\omega_0$.  Also, for $a_\rho>0$,

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\omega_0C_0}}
{2\omega_0}
\right)^2
>\frac{C_0}{\omega_0}.
$$

The exact inequalities
$C_0>7/4$ and $\omega_0<1/9$ follow respectively from
$32\sqrt2>45$ and

$$
25\left(\frac{333}{106}\right)^2-243
=\frac{41877}{11236}>0.
$$

Thus every active branch of the inherited minimum is greater than
$63/4$.  Since $c_7<11<63/4$, (5) is wholly contained in (1).  If this
exploratory band were later frozen, independently reconstructed, and
promoted, exact subtraction would replace (1) by

$$
\left\{(\rho,K):
\frac1{\sqrt{337}}<\rho<\rho_c,
\quad \sqrt{114}<K<U(\rho)\right\}.
\tag{7}
$$

The endpoint $\rho=1/\sqrt{337}$ is deliberately not claimed here, in
accordance with the assigned residual component.

## 2. Variational comparisons

Write

$$
b_{\ell,n}=j_{\ell+1/2,n}
\tag{8}
$$

for the unit-ball frequency in angular channel $\ell$ and radial index
$n$.  Extension by zero from $(\rho,1)$ to $(0,1)$ and fixed-channel
min--max give

$$
k_{\ell,n}^{\rm shell}(\rho)\geq b_{\ell,n}.
\tag{9}
$$

The transformed ball forms have common domain $H_0^1(0,1)$; Hardy's
inequality controls the inverse-square term.  Thus, for $p>\ell$,

$$
q_p[u]-q_\ell[u]
=\bigl(p(p+1)-\ell(\ell+1)\bigr)
\int_0^1\frac{|u|^2}{r^2}\,dr
\geq
\bigl(p(p+1)-\ell(\ell+1)\bigr)\|u\|_2^2.
$$

Min--max at the same radial index therefore yields the internal comparison

$$
\boxed{
b_{p,n}^2\geq b_{\ell,n}^2+
p(p+1)-\ell(\ell+1).}
\tag{10}
$$

Neither (9) nor (10) is attributed to Lorch or DLMF.

The interval Poincare estimate will also be used in the form

$$
\bigl(k_{\ell,n}^{\rm shell}(\rho)\bigr)^2
\geq n^2z_\rho^2+\ell(\ell+1).
\tag{11}
$$

## 3. The exact Lorch seed and the tempting cap-58 wall

The authenticated Round 19 specialization gives the full strict lower
square

$$
b_{5,1}^2>A_5,
\qquad
A_5=\frac{507(\sqrt{77}-1)}{52}.
\tag{12}
$$

Using (10) once gives

$$
b_{6,1}^2>B_6,
\qquad
B_6=A_5+12
=\frac{507\sqrt{77}+117}{52}.
\tag{13}
$$

Exact positive squaring gives

$$
87<B_6<88;
$$

the two margins are
$507^2\cdot77-4407^2=371124$ and
$4459^2-507^2\cdot77=89908$.

This explains both the opportunity and the trap at the first apparent new
wall.  The old shifted estimate $b_{3,2}^2>87$ allows the second
$\ell=3$ mode before $\sqrt{B_6}$.  Charging that multiplicity would make
the cap $45+7+13=65$, which the wall cannot pay.  In fact, $B_6<88$ gives

$$
\mathcal W(\rho,\sqrt{B_6})
<\frac{2}{27}\,88\sqrt{88}<65,
$$

where the last positive-squaring margin is
$1755^2-176^2\cdot88=354137$.  One must not treat the $\ell=6$ entry as
an isolated jump.

If the $\ell=3$ second mode is delayed independently, however, the exact
Lorch value really does pay the isolated cap $45+13=58$.  For example, set

$$
q=\frac{46851}{5000}.
\tag{14}
$$

Then $B_6>q^2$: after isolating the positive radical, the exact squared
margin is

$$
507^2\cdot77-
\left(52q^2-117\right)^2
=\frac{94969543244664231}{39062500000000}>0,
\tag{15}
$$

where $52q^2-117=27803960613/6250000>0$.  Moreover

$$
\frac{38}{539}q^3
=58+\frac{1232176081}{687500000000}>58.
\tag{16}
$$

The next sections prove stronger internal zero delays, so the final band
does not stop at $\sqrt{B_6}$.

## 4. Internal proof that $b_{6,1}>10$

The spherical-Bessel recurrence gives

$$
\mathsf j_6(x)
=\frac{P(x)\sin x-M(x)\cos x}{x^7},
\tag{17}
$$

where, with $t=x^2$,

$$
P(x)=10395-4725t+210t^2-t^3,
$$

$$
M(x)=10395x-1260x^3+21x^5
=21x(t^2-60t+495).
\tag{18}
$$

On $9\leq x\leq10$, $P$ is positive.  Indeed,

$$
\frac{dP}{dt}=-3(t^2-140t+1575)>0
\qquad(81\leq t\leq100),
$$

and $P(9)=474039$.  The same interval has $M>0$.

Let $D=M-P$ and $s=x-9$.  Direct expansion gives

$$
\begin{aligned}
D(x)={}&-58995+220104s+120150s^2+22770s^3\\
&+1950s^4+75s^5+s^6.
\end{aligned}
\tag{19}
$$

Thus $D$ is strictly increasing for $x\geq9$.  At the rational point (14),

$$
D(q)=
\frac{627284566220625775871723601}
{15625000000000000000000}>0.
\tag{20}
$$

Consequently $M/P>1$ throughout $[q,10]$.  A zero in this interval would
have to satisfy

$$
\tan x=\frac{M(x)}{P(x)}>1.
\tag{21}
$$

The point $q$ lies in $(5\pi/2,3\pi)$: the upper comparison has exact
margin $999/106-q=14397/265000>0$, while

$$
q-\frac{55}{7}=\frac{52957}{35000}>0
$$

and $5\pi/2<55/7$.  Hence the tangent is negative on $[q,3\pi)$.  On
$(3\pi,10]$, put $y=x-3\pi$.  The bound

$$
10-3\pi<\frac\pi4
$$

is equivalent to $\pi>40/13$, and
$333/106-40/13=89/1378>0$.  Hence $\tan x=\tan y<1$, again contradicting
(21).

By (13)--(15), the first positive zero $b_{6,1}$ is already strictly to
the right of $q$.  The zero-free interval just proved therefore yields

$$
\boxed{b_{6,1}>10.}
\tag{22}
$$

This is an internal half-integer calculation.  No new Lorch order is
imported.

## 5. Two radial delays

### 5.1 The second $\ell=3$ zero

The explicit formula

$$
\mathsf j_3(x)
=\frac{(15-6x^2)\sin x+(x^3-15x)\cos x}{x^4}
\tag{23}
$$

shows that, for $x>\sqrt{15}$, its zeros solve

$$
\tan x=R(x),
\qquad
R(x)=\frac{x(x^2-15)}{6x^2-15}>0.
\tag{24}
$$

Furthermore

$$
R'(x)=
\frac{6x^4+45x^2+225}{(6x^2-15)^2}<1,
\tag{25}
$$

because the denominator minus the numerator is
$15x^2(2x^2-15)>0$.  Hence $\tan x-R(x)$ is strictly increasing on every
positive-tangent half-period.  It has exactly one zero on each of
$(2\pi,5\pi/2)$ and $(3\pi,7\pi/2)$, and none on the negative-tangent
half-period between them.  The accepted first-zero bound
$b_{3,1}>13/2$, together with $2\pi<44/7<13/2$, identifies these as the
first and second positive zeros.

Set $x_0=81/8$.  It lies in $(3\pi,7\pi/2)$.  With
$y=x_0-3\pi$, the inequality $y<\pi/4$ is equivalent to
$\pi>81/26$, and

$$
\frac{333}{106}-\frac{81}{26}=\frac{18}{689}>0.
$$

Thus $\tan x_0<1$, whereas

$$
x_0(x_0^2-15)-(6x_0^2-15)
=\frac{146433}{512}>0,
$$

so $R(x_0)>1$.  The unique second zero lies to the right of $x_0$:

$$
\boxed{b_{3,2}>\frac{81}{8}.}
\tag{26}
$$

### 5.2 The third $\ell=1$ zero

The positive zeros of
$\mathsf j_1(x)=(\sin x-x\cos x)/x^2$ solve $\tan x=x$, with exactly one
zero in each $(n\pi,n\pi+\pi/2)$ for $n\geq1$.  Thus $b_{1,3}$ is the
unique zero in $(3\pi,7\pi/2)$.

At $x_1=21/2$, let $y=x_1-3\pi$.  The exact lower bound
$\pi>28/9$ gives $y<3\pi/8$, since

$$
\frac{333}{106}-\frac{28}{9}=\frac{29}{954}>0.
$$

Consequently

$$
\tan x_1=\tan y
<\tan\frac{3\pi}{8}=1+\sqrt2
<\frac52<\frac{21}{2}=x_1.
$$

The unique root is to the right of $x_1$:

$$
\boxed{b_{1,3}>\frac{21}{2}.}
\tag{27}
$$

## 6. Exhaustive inventory through $K=\sqrt{114}$

The three new internal bounds propagate through (10) as follows:

$$
b_{7,1}^2\geq b_{6,1}^2+14>114,
\tag{28}
$$

$$
b_{4,2}^2\geq b_{3,2}^2+8
>\frac{7073}{64}=c_{42}^2,
\tag{29}
$$

$$
b_{5,2}^2\geq b_{3,2}^2+18
>\frac{7713}{64}>114,
\tag{30}
$$

and

$$
b_{2,3}^2\geq b_{1,3}^2+4
>\frac{457}{4}>114.
\tag{31}
$$

Therefore, through the included face $K=c_7$:

- only first modes $0\leq\ell\leq6$ can occur;
- only second modes $0\leq\ell\leq4$ can occur;
- only third modes $\ell=0,1$ can occur;
- no fourth or higher radial mode can occur, because
  $k_{\ell,n}^{\rm shell}\geq nz_\rho>4\pi>12>c_7$ for $n\geq4$.

The $\ell=0$ third frequency is the exact moving wall

$$
k_{0,3}=3z_\rho=\frac{3\pi}{1-\rho}.
\tag{32}
$$

It lies strictly above the old face $d$, since

$$
9\left(\frac{333}{106}\right)^2-\frac{337}{4}
=\frac{12842}{2809}>0.
\tag{33}
$$

At $K=3z_\rho$ the mode is excluded by strict counting.  Its exact
crossing with any fixed face $c$ is
$\rho=1-3\pi/c$ when that ratio lies in the active interval.  The ledger
below never assumes a fixed order between (32) and the faces above: it
splits the first row at (32) and conservatively includes $(0,3)$ in every
later cap.

The exhaustive strict-count caps are therefore

| frequency range | possible inventory | cap |
|---|---|---:|
| $d<K\leq10$, $K\leq3z_\rho$ | first $\ell=0,\ldots,5$; second $\ell=0,1,2$ | $45$ |
| $d<K\leq10$, $K>3z_\rho$ | preceding inventory plus $(0,3)$ | $46$ |
| $10<K\leq81/8$ | first $\ell=0,\ldots,6$; second $\ell=0,1,2$; possible $(0,3)$ | $59$ |
| $81/8<K\leq21/2$ | preceding inventory plus $(3,2)$ | $66$ |
| $21/2<K\leq c_{42}$ | preceding inventory plus $(1,3)$ | $69$ |
| $c_{42}<K\leq c_7$ | preceding inventory plus $(4,2)$ | $78$ |

For example, the last cap is

$$
\sum_{\ell=0}^{6}(2\ell+1)
+\sum_{\ell=0}^{4}(2\ell+1)
+\sum_{\ell=0}^{1}(2\ell+1)
=49+25+4=78.
\tag{34}
$$

Every lower threshold in the table is open.  At equality, the newly
listed mode remains excluded and the preceding row owns the face.

## 7. Exact Weyl payments

As in the Round 19 lower-ratio calculation, $\rho<\rho_c<1/7$ and
$\pi<22/7$ imply, for fixed $c>0$,

$$
\mathcal W(\rho,c)>\frac{38}{539}c^3.
\tag{35}
$$

The first two rows are paid without making any assumption about the moving
wall.  Since $d>9$,

$$
\mathcal W(\rho,K)>\frac{38}{539}\,9^3
=\frac{27702}{539}>46
\qquad(d<K\leq10).
\tag{36}
$$

Alternatively, on the subrow $K>3z_\rho$, the exact identity
$\mathcal W(\rho,3z_\rho)=27\mathcal W(\rho,z_\rho)>54$ pays the extra
radial multiplicity directly.

For the next three open lower faces,

$$
\frac{38}{539}\,10^3
=\frac{38000}{539}
=59+\frac{6199}{539}>59,
\tag{37}
$$

$$
\frac{38}{539}\left(\frac{81}{8}\right)^3
=\frac{10097379}{137984}
=66+\frac{990435}{137984}>66,
\tag{38}
$$

and

$$
\frac{38}{539}\left(\frac{21}{2}\right)^3
=\frac{3591}{44}
=69+\frac{555}{44}>69.
\tag{39}
$$

Finally,

$$
\frac{38}{539}c_{42}^3
=\frac{38\cdot7073\sqrt{7073}}{539\cdot512}>78.
\tag{40}
$$

Both sides of the last comparison are positive, and its exact squared
margin is

$$
(38\cdot7073)^2\,7073
-(78\cdot539\cdot512)^2
=47602399882532>0.
\tag{41}
$$

Equations (36)--(41), strict monotonicity in $K$, the exhaustive inventory,
and equality ownership prove (6).

## 8. The first obstruction above the new face

At $K=c_7$, (28) strictly excludes the first $\ell=7$ mode, so the
included face is owned by the cap-$78$ row.  The present explicit lower
bound supplies no quantified continuation above this face; a conservative
continuation must therefore allow the mode.  Charging its full multiplicity
$15$ raises the cap to

$$
78+15=93.
\tag{42}
$$

No uncharged second or third radial entry was hidden below this wall:
(30)--(31) put the next such propagated bounds strictly above $c_7$, and
the moving $(0,3)$ mode has already been charged in $78$.

The cap-$93$ jump cannot be paid at this wall even by a deliberately
generous uniform upper bound:

$$
\mathcal W(\rho,c_7)
<\frac{2}{27}c_7^3
=\frac{76}{9}\sqrt{114}<93.
\tag{43}
$$

The final comparison is exact positive squaring:

$$
837^2-76^2\cdot114=42105>0.
\tag{44}
$$

Thus the first unsupported continuation of this exact cap ledger is the
full $\ell=7$ multiplicity immediately above $K=\sqrt{114}$.  This is a
method obstruction, not a counterexample to the shell Polya inequality.
A continuation needs a sharper internal or independently sourced delay for
$b_{7,1}$ (or a shell-specific delay), or a payment that avoids charging
the whole angular multiplicity at the first conservative wall.

## 9. Face ownership and non-claim

- The old face $K=d$ remains owned by Round 19 and is excluded from (5).
- The new face $K=\sqrt{114}$ is included; strict counting and (28) exclude
  the next first mode there.
- The moving face $K=3z_\rho$ belongs to the lower-count side.
- The endpoints $\rho=1/\sqrt{337}$ and $\rho=\rho_c$ are not claimed.
- The inherited ceiling $K=U(\rho)$ is excluded and remains owned by its
  inherited proof.
- Equality at every ball lower bound or shell spectral entry is assigned
  according to strict spectral counting.

The remainder (7), both other Round 19 residual components, and the full
shell Polya conjecture remain open.  This note is not a State Patch and
does not authorize promotion without a proof-free freeze, independent
reconstruction, exact-constant audit, and face-by-face residual check.
