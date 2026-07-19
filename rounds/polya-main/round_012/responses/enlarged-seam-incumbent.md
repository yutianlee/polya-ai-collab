# Round 12 incumbent: enlarged central--thin seam

## Verdict and theorem

**PASS.** The proposed constant $24$ is sufficient; no replacement is
needed. Let

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le\frac1{20}.
$$

Then, including threshold equality,

$$
\boxed{
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

The proof is a new derivation on the whole enlarged domain. In particular,
none of the Round 10 estimates whose proof stopped at
$\varepsilon=1/25$ is extrapolated.

The same calculation also proves

$$
\boxed{K_0(19/20)<3300^2},
\tag{2}
$$

and the closed analytic union therefore gives

$$
\boxed{
0<\rho<1,
\qquad K\ge3300^2.
}
\tag{3}
$$

This is an all-ratio high-frequency theorem, not the all-frequency shell
theorem.

## 1. Frozen shifted-tail reduction

Put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
d=1-\frac2\pi\arccos\rho,
\qquad
\eta=G_1(\rho).
$$

For a low-interface shifted tail beginning at
$x_0=r_0+1/2<\mu$, write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
U=\mu-x_0=n+\beta,
\qquad 0\le\beta<1.
$$

Let $p$ be the length of the initial constant ordinary-floor plateau and
set

$$
m=n-p,
\qquad
R=p-dm.
\tag{4}
$$

For $n=0$, the prescribed convention is $p=m=0$. The audited Round 3
input is

$$
\frac{\mathcal T_{r_0}}2
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,
\qquad
0\le\delta<\frac{2\sqrt2}{15},
\tag{5}
$$

together with the unconditional shelf bound

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{6}
$$

It is enough to prove $M>4\delta$. Only $R>0$ requires a plateau-loss
estimate.

Use the scaled variables

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4.
\tag{7}
$$

The candidate domain is exactly

$$
0<y\le\frac1{\sqrt{20}},
\qquad
\rho=1-y^2\ge\frac{19}{20},
\qquad
\kappa\ge24.
\tag{8}
$$

In the branch $R>0$, define

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{9}
$$

## 2. Elementary bounds

We use

$$
3<\pi<\frac{22}{7},
\qquad
\frac75<\sqrt2<\frac32.
\tag{10}
$$

For completeness, the eight-term lower geometric sum for
$\pi/4=\int_0^1(1+x^2)^{-1}\,dx$ is

$$
\frac{33976}{45045}
=\frac34+\frac{769}{180180}>\frac34,
$$

while the standard positive Dalzell integral gives $\pi<22/7$. The
radical bounds in (10) follow by squaring:

$$
2-\left(\frac75\right)^2=\frac1{25}>0,
\qquad
\left(\frac32\right)^2-2=\frac14>0.
$$

Two further algebraic bounds used below are

$$
\frac1{\sqrt{20}}<\frac9{40},
\qquad
\sqrt{20}>\frac{22}{5},
\tag{11}
$$

with squared margins (1/1600) and (16/25), respectively.

## 3. A new lower bound for $d$

For $0<x<1$, the alternating cosine expansion gives

$$
1-\cos x>\frac{x^2}{2}-\frac{x^4}{24},
$$

and the expression on the right is increasing there. Since
$11\pi/100>33/100$,

$$
\frac{(33/100)^2}{2}-\frac{(33/100)^4}{24}-\frac1{20}
=\frac{3164693}{800000000}>0.
$$

Thus

$$
\cos\frac{11\pi}{100}<\frac{19}{20}\le\rho,
$$

so

$$
\arccos\rho<\frac{11\pi}{100},
\qquad
\boxed{d>\frac{39}{50}}.
\tag{12}
$$

If $R>0$, then $p>0$, and (4) gives

$$
m<\frac pd<\frac{50}{39}p,
\qquad
S<\frac{89}{39}P.
\tag{13}
$$

This also covers the no-drop geometry $p=n>0$, for which $m=0$.

## 4. Dangerous-plateau localization

Let

$$
t=\frac{x_0}{\rho K},
\qquad
w=1-t=\frac U{\rho K}.
$$

Because $U=n+\beta<1+p+m$,

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{14}
$$

The shelf estimate (6) becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Consequently, by (13),

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac{89}{39}y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{15}
$$

Both terms increase with $y$ and decrease with $\kappa$. At the endpoint
of (8),

$$
\frac{y^4}{\kappa\rho}\le\frac1{9120},
\qquad
y\sqrt{\frac{2\pi}{\kappa\rho}}
\le\sqrt{\frac\pi{228}}
<\sqrt{\frac{11}{798}}<\frac{47}{400},
$$

where

$$
\left(\frac{47}{400}\right)^2-\frac{11}{798}
=\frac{1391}{63840000}>0.
$$

Therefore

$$
\widehat q
<\frac1{9120}+\frac{89}{39}\frac{47}{400}
=\frac{159019}{592800}
<\frac{27}{100},
\tag{16}
$$

with exact final margin

$$
\frac{27}{100}-\frac{159019}{592800}
=\frac{1037}{592800}>0.
$$

It follows that

$$
t>\frac{73}{100},
\qquad
\frac{x_0}{K}=\rho t
>\frac{19}{20}\frac{73}{100}
=\frac{1387}{2000}
=\frac12+\frac{387}{2000}.
\tag{17}
$$

Thus every use of the outer-region slope is made only after the required
localization has been proved.

## 5. Local slope and self-consistency

For $0<z<\mu$, define

$$
\sigma(z)=-A'(z)
=\frac1\pi
\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
$$

The function $\sigma$ is increasing. At $x_0=\mu t$,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{18}
$$

Put

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa}.
\tag{19}
$$

Then

$$
\widehat q=\frac{y^2}{\rho}(Q-1),
\qquad
1-\rho t=\varepsilon+\frac UK<y^2Q,
$$

and hence

$$
1-\rho^2t^2<2y^2Q.
\tag{20}
$$

By definition of the plateau, $A(x_0)$ and $A(x_0+p)$ have the same
ordinary floor. Even if either sample is an integer, this implies the
strict inequality

$$
A(x_0)-A(x_0+p)<1.
$$

Since $p>0$ in the dangerous branch, monotonicity of $\sigma$ gives

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
$$

Using (18)--(20), $t>1-\widehat q>0$, and squaring only positive
quantities yields

$$
\boxed{
P^2<H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{21}
$$

The denominator is positive by (16).

## 6. Complete synthetic path and loss bound

From (4) and (9),

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{22}
$$

Thus $0<r\le P$. For fixed $y,\kappa,d$, $Q$, and therefore $H$,
decreases with $r$. Let

$$
a=\frac{y^2}{\rho}\le\frac1{19}.
$$

Along a path on which (r) is fixed,

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q}{\partial P}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
\tag{23}
$$

Choose

$$
B=\frac{23}{5}.
$$

Suppose $r\ge B$. Then $P\ge r$, and

$$
H(P,r)\le H(P,B).
$$

For every synthetic point $P'\in[B,P]$, set

$$
S'=P'+\frac{P'-B}{d}<\frac{89}{39}P'.
$$

Because $P'\le P$, the original shelf ceiling remains valid at every
synthetic point. Therefore (16) holds on the complete path. Moreover, using
(11), (12), and $\kappa\ge24$,

$$
\frac{\partial Q}{\partial P'}
=\frac y\kappa\left(1+\frac1d\right)
<\frac{89}{4160}.
$$

Equations (10), (16), and (23) give the exact pathwise estimate

$$
\frac{\partial H}{\partial P'}
<
2\left(\frac{22}{7}\right)^2
\frac{89}{4160}
\frac{1+27/100+2/19}{(1-27/100)^3}
=\frac{541142250}{362174827}
<\frac32,
\tag{24}
$$

where

$$
\frac32-\frac{541142250}{362174827}
=\frac{4239981}{724349654}>0.
$$

Hence

$$
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2B-\frac32=\frac{77}{10}>0.
\tag{25}
$$

At $P'=r=B$, (22) gives $S=B$ exactly. From (8) and (11),

$$
Q<1+\frac1{480}+\frac{3B}{320}
=\frac{5017}{4800},
\qquad
\widehat q<\frac1{19}\left(\frac{5017}{4800}-1\right)
=\frac{217}{91200}.
$$

The exact no-drop endpoint margin is

$$
B^2
-2\left(\frac{22}{7}\right)^2
\frac{5017/4800}{(1-217/91200)^2}
=\frac{4189934997169}{10140435204025}>0.
\tag{26}
$$

Combining (25)--(26),

$$
P^2-H(P,r)
\ge P^2-H(P,B)
\ge B^2-H(B,B)>0,
$$

contradicting (21). Therefore

$$
\boxed{
R<\frac{23}{5\sqrt\varepsilon}.
}
\tag{27}
$$

The no-drop branch $p=n>0$ has $m=0$, hence $P=r$, and is precisely
the endpoint geometry controlled in (26).

## 7. Action payment and exceptional branches

The exact action identity and
$\arccos(1-v)\ge\sqrt{2v}$ give

$$
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
$$

Using (8) and (10),

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
>\frac{392}{55y}.
\tag{28}
$$

If $R>0$, then (27), (28), and the universally strict floor estimate
$\lfloor x\rfloor>x-1$ imply

$$
M
>\left(\frac{392}{55}-\frac{23}{5}\right)\frac1y-1
>\left(\frac{392}{55}-\frac{23}{5}\right)\frac{22}{5}-1
=\frac{253}{25}.
\tag{29}
$$

On the other hand,

$$
4\delta<\frac{8\sqrt2}{15}<\frac45,
$$

so the dangerous-branch payment margin is

$$
M-4\delta>\frac{253}{25}-\frac45
=\frac{233}{25}>0.
\tag{30}
$$

If $R\le0$, then no dangerous localization is used, and

$$
M\ge\lfloor K\eta\rfloor
>K\eta-1
>\frac{392}{55}\frac{22}{5}-1
=\frac{759}{25}.
$$

Thus the safe-branch margin is

$$
M-4\delta>\frac{759}{25}-\frac45
=\frac{739}{25}>0.
\tag{31}
$$

This explicitly owns every exceptional branch:

- if $p=n>0$, then $m=0$ and the dangerous proof, including (26),
  applies;
- if $p=0<n$, then $R=-dn<0$, so this immediate-drop branch is safe;
- if $n=0$, then $p=m=R=0$, so the degenerate head is safe;
- the exact sign wall $R=0$ belongs to the safe branch.

Substitution of (30)--(31) into (5) yields

$$
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^K A(z)\,dz
$$

for every low-interface shifted tail. The permitted high-interface theorem
and weighted multiplicity scaffold complete (1).

## 8. Floor, interface, threshold, and spectral walls

All walls remain owned:

1. The defining floor for $n$ gives $0\le\beta<1$, so
   $U<1+p+m$ is strict even when $\mu-x_0$ is an integer.
2. Equal ordinary floors give
   $A(x_0)-A(x_0+p)<1$, including when either sampled value is integral.
3. At a gain wall, $\lfloor K\eta\rfloor>K\eta-1$ is still strict.
4. At the low/high interface wall, the interface remainder is
   $\delta=0$; the high-interface theorem owns $x_0=\mu$.
5. The proof uses non-strict $\kappa\ge24$, so
   $K=24/\varepsilon^2$ is included. Strictness is supplied by the
   elementary, floor, and action margins, not by excluding the threshold.
6. The strict phase proxy and strict spectral-count transfer are unchanged;
   no eigenvalue wall is replaced by an ordinary-floor identity.

On the retained Round 10 domain $0<\varepsilon\le1/25$, the sharper
theorem $K\ge20/\varepsilon^2$ remains authoritative. Thus its threshold
face $\kappa=20$ is not altered by the new proof.

## 9. Exact central endpoint at $19/20$

For this endpoint only, use the sharper elementary certificates

$$
\pi<\frac{1571}{500},
\qquad
\frac{140}{99}<\sqrt2<\frac{99}{70},
\qquad
\sqrt5<\frac94.
\tag{32}
$$

The alternating arctangent bounds in Machin's identity give

$$
\pi<
\frac{5277328977275528}{1679825970703125}
<\frac{1571}{500},
$$

with final rational margin

$$
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=\frac{2736890694763}{6719303882812500}>0.
$$

The radical bounds follow from

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801},
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900},
\qquad
\left(\frac94\right)^2-5=\frac1{16}.
$$

At $\rho=19/20$,

$$
a_\rho=38\pi<38\frac{22}{7}<11^2,
\qquad
11^2-38\frac{22}{7}=\frac{11}{7}>0.
\tag{33}
$$

Moreover, the action estimate gives

$$
\eta_\rho
\ge\frac{2\sqrt2}{3\pi}\left(\frac1{20}\right)^{3/2}
>\frac{140000}{466587}\frac1{90}
=\frac{14000}{4199283},
\tag{34}
$$

where
$(1/20)^{3/2}=1/(40\sqrt5)>1/90$. Also

$$
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
\tag{35}
$$

Let

$$
F(Y)=\eta_\rho Y^2-\sqrt{a_\rho}\,Y-C_0.
$$

The positive zero of $F$ is exactly $\sqrt{K_0(\rho)}$. At $Y=3300$,
(33)--(35) yield the strict exact comparison

$$
F(3300)
>
\frac{14000}{4199283}3300^2
-11\cdot3300-\frac{307}{175}
=\frac{32985481}{7422975}>0.
\tag{36}
$$

Since $F(0)=-C_0<0$ and an upward-opening quadratic with negative
constant term has a unique positive zero, (36) places that zero below
$3300$. Hence (2) follows. The fixed-ratio theorem itself includes its
threshold $K=K_0(19/20)$; (36) merely locates that threshold strictly
below $3300^2$.

## 10. Closed all-ratio union

Use the following accepted closed zones and the two results just proved.

1. The small-hole endpoint proves every frequency on $0<\rho\le\rho_*$.
   On $[\rho_*,1/16]$, every possible residual has $K<64$.
2. On $[1/16,19/20]$, the already-audited monotonicity of $K_0(\rho)$
   and (2) give $K_0(\rho)\le K_0(19/20)<3300^2$.
3. On $[19/20,24/25]$, theorem (1) applies. Here
   $24/\varepsilon^2\le15000$.
4. On $[24/25,99/100]$, retain the sharper Round 10 theorem
   $K\ge20/\varepsilon^2$, whose threshold is at most $200000$.
5. The complete Round 11 endpoint owns every frequency on
   $[99/100,1)$.

The finite comparisons are

$$
3300^2-200000=10690000>0,
\qquad
3300^2-15000=10875000>0.
$$

All faces are included. At $\rho=19/20$, the fixed-ratio and new seam
theorems both apply. At $\rho=24/25$, the Round 10 theorem supplies the
sharper threshold while both seam theorems own the face. At
$\rho=99/100$, the Round 10 theorem meets the all-frequency endpoint.
The face $K=3300^2$ lies strictly above the central threshold and above
both thin thresholds. This proves (3).

## 11. Executable exact rational ledger

The following standard-library-only ledger reproduces every finite margin
used above. It is a rational constants ledger, not a Bessel-root
certificate.

```python
from fractions import Fraction as F

# Elementary and d bounds.
assert F(33976, 45045) - F(3, 4) == F(769, 180180)
assert (
    F(33, 100) ** 2 / 2
    - F(33, 100) ** 4 / 24
    - F(1, 20)
) == F(3164693, 800000000)
assert F(9, 40) ** 2 - F(1, 20) == F(1, 1600)
assert F(20) - F(22, 5) ** 2 == F(16, 25)

# Dangerous-plateau localization.
assert F(47, 400) ** 2 - F(11, 798) == F(1391, 63840000)
q = F(1, 9120) + F(89, 39) * F(47, 400)
assert q == F(159019, 592800)
assert F(27, 100) - q == F(1037, 592800)
assert F(19, 20) * F(73, 100) == F(1387, 2000)
assert F(1387, 2000) - F(1, 2) == F(387, 2000)

# Complete synthetic-path derivative.
D = (
    2 * F(22, 7) ** 2 * F(89, 4160)
    * (1 + F(27, 100) + F(2, 19))
    / F(73, 100) ** 3
)
assert D == F(541142250, 362174827)
assert F(3, 2) - D == F(4239981, 724349654)

# No-drop endpoint.
B = F(23, 5)
Q = F(5017, 4800)
q0 = F(217, 91200)
endpoint = B**2 - 2 * F(22, 7) ** 2 * Q / (1 - q0) ** 2
assert endpoint == F(4189934997169, 10140435204025)

# Dangerous and safe payments after the floor loss and interface cap.
assert (F(392, 55) - B) * F(22, 5) - 1 == F(253, 25)
assert F(253, 25) - F(4, 5) == F(233, 25)
assert F(392, 55) * F(22, 5) - 1 == F(759, 25)
assert F(759, 25) - F(4, 5) == F(739, 25)

# Sharper constants and the central endpoint.
machin_upper = F(5277328977275528, 1679825970703125)
assert F(1571, 500) - machin_upper == F(
    2736890694763, 6719303882812500
)
assert F(2) - F(140, 99) ** 2 == F(2, 9801)
assert F(99, 70) ** 2 - F(2) == F(1, 4900)
assert F(9, 4) ** 2 - F(5) == F(1, 16)
eta = F(14000, 4199283)
assert F(140000, 466587) * F(1, 90) == eta
assert F(121) - F(38) * F(22, 7) == F(11, 7)
assert (
    eta * 3300**2 - F(11) * 3300 - F(307, 175)
) == F(32985481, 7422975)

# Closed union.
assert 3300**2 - 200000 == 10690000
assert 3300**2 - 15000 == 10875000

print("all exact Round 12 incumbent ledger checks passed")
```

## Final assessment

The first potential enlarged-domain obstruction was the old bound
$d>4/5$, which is false at the new endpoint and has not been reused. The
replacement $d>39/50$, together with the higher gain at
$\kappa=24$, closes the entire proof with positive exact margins. The
local theorem, every exceptional branch and wall, the central endpoint, and
the closed global union all pass.
