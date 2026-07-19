# Round 12 independent enlarged-seam constant inventory

## Scope and verdict

This is an independent feasibility audit of the proposed constants

$$
0<\varepsilon\le\frac1{20},
\qquad
\kappa=K\varepsilon^2\ge24,
\tag{1}
$$

and of the central endpoint target

$$
K_0(19/20)<3300^2.
\tag{2}
$$

Only accepted pre-Round-12 shifted-tail inputs and the audited Round 9--10
local-slope framework were used.  No Round 12 incumbent, clean-room proof,
or referee output was inspected.

**Verdict: PASS.**  The exact endpoint ledger closes with

$$
d_0=\frac34,
\qquad
\bar q=\frac{11}{40},
\qquad
B=\frac{23}{5}.
\tag{3}
$$

Thus the proposed constants do not encounter a finite-constant obstruction.
There is no failed inequality to report.  This inventory verifies the
constant chain; promotion still requires the complete analytic proof and
the prescribed independent theorem-level reviews.

## 1. Frozen reduction

Put

$$
y=\sqrt\varepsilon,
\qquad
\rho=1-y^2,
\qquad
\kappa=Ky^4.
$$

In the dangerous low-interface branch let

$$
R=p-dm>0,
\qquad
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y,
$$

where

$$
d=1-\frac2\pi\arccos\rho.
$$

The accepted decomposition is

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,
\qquad
0\le\delta<\frac{2\sqrt2}{15},
\tag{4}
$$

and the unconditional shelf estimate is

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{5}
$$

The exact local-slope argument gives

$$
P^2<H(P,r)
:=
\frac{2\pi^2Q}{(1-\widehat q)^2},
\tag{6}
$$

where

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1).
\tag{7}
$$

The task is to make every bound in this reduction uniform on (1).

## 2. Enlarged-domain geometry

The identity

$$
\cos^2\frac\pi8=\frac{2+\sqrt2}{4}
$$

and $\sqrt2<3/2$ give

$$
\cos^2\frac\pi8<\frac78
<\left(\frac{19}{20}\right)^2,
\qquad
\left(\frac{19}{20}\right)^2-\frac78
=\frac{11}{400}>0.
$$

Hence $\arccos\rho<\pi/8$ and

$$
\boxed{d>\frac34}.
\tag{8}
$$

If $R>0$, then $m<p/d<4p/3$, so

$$
S<\frac73P.
\tag{9}
$$

This estimate also retains the no-drop geometry $m=0$, where $P=r$.

## 3. Displacement and localization

Let $t=x_0/(\rho K)$.  From (5), (7), and (9),

$$
1-t
<\widehat q
<
\frac{y^4}{\kappa\rho}
+\frac73y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{10}
$$

Both endpoint expressions increase with $y$ and decrease with $\kappa$.
At $y^2=1/20$, $\rho=19/20$, and $\kappa=24$, the first term is $1/9120$,
while

$$
y\sqrt{\frac{2\pi}{\kappa\rho}}
=\sqrt{\frac\pi{228}}
<\frac{47}{400}.
$$

Indeed, using $\pi<1571/500$,

$$
\left(\frac{47}{400}\right)^2
-\frac{1571}{114000}
=\frac{233}{9120000}>0.
$$

Therefore

$$
\widehat q
<\frac1{9120}+\frac{329}{1200}
=\frac{4169}{15200}
<\frac{11}{40},
$$

with exact reserve

$$
\frac{11}{40}-\frac{4169}{15200}
=\frac{11}{15200}>0.
\tag{11}
$$

Consequently

$$
t>\frac{29}{40},
\qquad
\frac{x_0}{K}=\rho t
>\frac{19}{20}\frac{29}{40}
=\frac{551}{800}>\frac12.
\tag{12}
$$

Thus every use of the outer-region slope is preceded by a uniform
localization on the enlarged domain.

## 4. Derivative self-consistency

Since

$$
S=P+\frac{P-r}{d},
$$

$H$ decreases with $r$.  Along a synthetic path with fixed $r=B$, use
$y<9/40$, which follows from $(9/40)^2-1/20=1/1600$.  Then

$$
\frac{\partial Q}{\partial P}
=\frac y\kappa\left(1+\frac1d\right)
<\frac7{320},
\qquad
\frac{y^2}{\rho}\le\frac1{19}.
$$

Together with $\widehat q<11/40$, the exact derivative formula gives

$$
\frac{\partial H}{\partial P}
<
2\left(\frac{1571}{500}\right)^2
\frac7{320}
\frac{1+11/40+2/19}{(1-11/40)^3}
=\frac{18122825063}{11584775000}
<\frac85.
\tag{13}
$$

The last margin is

$$
\frac85-
\frac{18122825063}{11584775000}
=\frac{412814937}{11584775000}>0.
$$

For $B=23/5$,

$$
2B-\frac85=\frac{38}{5}>0,
\tag{14}
$$

so $P^2-H(P,B)$ is strictly increasing on the complete path $P\ge B$.
Every intermediate point retains the original shelf ceiling because its
$P$ coordinate does not increase, and (9) remains valid there.

## 5. Endpoint contradiction and scaled loss

At $P=r=B$, one has $S=B$.  Majorizing $y$ by $9/40$ gives

$$
Q
<1+\frac1{480}+\frac{(9/40)(23/5)}{24}
=\frac{5017}{4800},
$$

and hence

$$
\widehat q
<\frac1{19}\left(\frac{5017}{4800}-1\right)
=\frac{217}{91200}.
$$

The decisive endpoint margin is

$$
\left(\frac{23}{5}\right)^2
-2\left(\frac{1571}{500}\right)^2
\frac{5017/4800}{(1-217/91200)^2}
=
\frac{2196261729217}{5173691430625}>0.
\tag{15}
$$

If $r\ge B$, monotonicity in $r$, (13)--(15), and the synthetic path
contradict (6).  Therefore

$$
\boxed{
R<\frac{23}{5\sqrt\varepsilon}.
}
\tag{16}
$$

The no-drop branch $p=n>0$ has $m=0$ and is the endpoint geometry in (15).

## 6. Action-gain payment and branches

The accepted action estimate is

$$
K\eta
\ge
\frac{2\sqrt2\,\kappa}{3\pi y}.
$$

Using $\sqrt2>140/99$, $\pi<1571/500$, and $\kappa\ge24$ gives

$$
K\eta>
\frac{1120000}{155529}\frac1y.
\tag{17}
$$

Moreover $1/y\ge\sqrt{20}>40/9$, with exact square margin $20/81$.
In the dangerous branch, (16), (17), and
$\lfloor x\rfloor>x-1$ yield

$$
M>
\frac{40}{9}\left(
\frac{1120000}{155529}-\frac{23}{5}
\right)-1
=\frac{14782903}{1399761}.
$$

Since

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
$$

the full payment reserve is

$$
\frac{14782903}{1399761}-\frac{132}{175}
=\frac{2402239573}{244958175}>0.
\tag{18}
$$

If $R\le0$, then

$$
M\ge\lfloor K\eta\rfloor>K\eta-1
>\frac{43400239}{1399761},
$$

and its reserve over $132/175$ is

$$
\frac{7410273373}{244958175}>0.
\tag{19}
$$

Thus the sign wall $R=0$, immediate-drop branch $p=0$, and degenerate head
$n=0$ all close in the safe branch.  The no-drop branch is covered by the
dangerous endpoint.  The ordinary-floor inequality stays strict at integer
walls, the gain inequality stays strict after the possible unit floor loss,
and the interface wall has $\delta=0$.

## 7. Exact central endpoint

At $\rho=19/20$,

$$
a_\rho=38\pi
<38\frac{22}{7}
=\frac{836}{7}<11^2,
$$

where $121-836/7=11/7$.  Also

$$
\eta_\rho
\ge
\frac{2\sqrt2}{3\pi}\left(\frac1{20}\right)^{3/2}
>
\frac{14000}{4199283}.
\tag{20}
$$

For (20), use $\sqrt2>140/99$, $\pi<1571/500$, and
$\sqrt{20}<9/2$.  Finally

$$
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
$$

The positive root $\sqrt{K_0(\rho)}$ solves

$$
F(Y)=\eta_\rho Y^2-\sqrt{a_\rho}\,Y-C_0=0.
$$

At $Y=3300$,

$$
F(3300)
>
\frac{14000}{4199283}(3300)^2
-11(3300)-\frac{307}{175}
=\frac{32985481}{7422975}>0.
\tag{21}
$$

Since $F(0)<0$ and the quadratic has one positive root, (21) proves

$$
\boxed{K_0(19/20)<3300^2=10890000.}
\tag{22}
$$

On the moved strip $1/100\le\varepsilon\le1/20$, the proposed high curve
has endpoint values

$$
\frac{24}{(1/20)^2}=9600,
\qquad
\frac{24}{(1/100)^2}=240000<3300^2.
$$

Thus the central ceiling, not the enlarged-seam curve, is the dominant
quantity in the proposed global union.

## 8. Executable certificate

Every finite comparison above is reproduced with exact rational arithmetic
by

`computations/round12_verify_enlarged_seam.py`, with focused tests in
`computations/tests/test_round12_enlarged_seam.py`.
