# Round 14 incumbent: central--thin seam at $\rho=7/8$

## Verdict

**PASS.**  Both frozen Round 14 targets close with strict exact reserves.  If

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac18,
$$

then, including threshold equality,

$$
\boxed{
K\ge\frac{32}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

This is a fresh derivation on the whole displayed domain.  No
Round 13 intermediate estimate is extrapolated.  In the final piecewise
envelope, the genuinely new use of (1) is only
$1/10\le\varepsilon\le1/8$; Round 13 owns the face
$\varepsilon=1/10$ at the sharper threshold $24/\varepsilon^2$, and
Round 10 remains sharpest on $\varepsilon\le1/25$.

Independently,

$$
\boxed{K_0(7/8)<550^2.}
\tag{2}
$$

Consequently the closed six-zone union gives

$$
\boxed{0<\rho<1,\qquad K\ge550^2.}
\tag{3}
$$

Statement (3) is an all-ratio high-frequency theorem.  It is not a
complete all-frequency shell theorem, and it does not enlarge the complete
endpoint $99/100\le\rho<1$.

## 1. Shifted-tail reduction and exact domain

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
$x_0=r_0+1/2<\mu$, put

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1),
$$

and define $p$ from the ordinary shifted floors

$$
h_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor
$$

exactly as in the frozen packet.  Thus either
$h_0=h_p>h_{p+1}$ with $0\le p<n$, or $p=n$ when there is no drop.
Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{4}
$$

For $n=0$ use $p=m=0$.  The permitted audited decomposition is

$$
\frac{\mathcal T_{r_0}}2
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,
\tag{5}
$$

where

$$
\delta=\int_q^\mu G_\mu(z)\,dz,
\qquad
0\le\delta<\frac{2\sqrt2}{15},
\tag{6}
$$

and the unconditional shelf estimate is

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{7}
$$

Thus it is enough to prove $M>4\delta$.  Only $R>0$ needs a new
plateau-loss cap.

Scale by

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4.
\tag{8}
$$

The exact candidate domain is

$$
0<y\le\frac1{2\sqrt2},
\qquad
\rho=1-y^2\ge\frac78,
\qquad
\kappa\ge32.
\tag{9}
$$

In the branch $R>0$, define

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{10}
$$

## 2. Reconstructed rational and radical bounds

The only numerical comparisons used below are derived here.  Machin's
identity and the alternating arctangent series give

$$
\begin{aligned}
\pi
&=16\arctan\frac15-4\arctan\frac1{239}\\
&<16\left(
\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}
-\frac1{7\cdot5^7}+\frac1{9\cdot5^9}
\right)
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)\\
&=\frac{5277328977275528}{1679825970703125}
<\frac{1571}{500}<\frac{22}{7}.
\end{aligned}
\tag{11}
$$

The last two exact margins are

$$
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=\frac{2736890694763}{6719303882812500}>0,
\qquad
\frac{22}{7}-\frac{1571}{500}=\frac3{3500}>0.
$$

Squaring positive rationals gives

$$
\frac{140}{99}<\sqrt2<\frac{99}{70},
\tag{12}
$$

because

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0.
$$

In particular, including the endpoint in (9),

$$
y\le\frac1{2\sqrt2}<\frac{99}{280},
\qquad
\frac1y\ge2\sqrt2>\frac{280}{99}.
\tag{13}
$$

All quantities divided by below are positive: $y,\rho,\kappa,d,Q$ and
$1-\widehat q$.  The last two assertions are proved before they are used.

## 3. Angular factor and the $R>0$ geometry

At the worst angular endpoint,

$$
\left(\frac78\right)^2-\left(\frac{\sqrt3}{2}\right)^2
=\frac1{64}>0.
\tag{14}
$$

Hence

$$
\rho\ge\frac78>\frac{\sqrt3}{2}=\cos\frac\pi6.
$$

Since arccos is strictly decreasing,

$$
\arccos\rho<\frac\pi6,
\qquad
\boxed{d>\frac23.}
\tag{15}
$$

If $R>0$, then $p>0$, and (4) gives

$$
m<\frac pd<\frac32p,
\qquad
S<\frac52P.
\tag{16}
$$

This also includes the no-drop geometry $p=n>0$, for which $m=0$.

## 4. Dangerous-plateau localization before the outer slope

Define

$$
t=\frac{x_0}{\rho K},
\qquad
w=1-t=\frac{U}{\rho K}.
$$

Since $U=p+m+\beta<1+p+m$ for every $0\le\beta<1$,
including $\beta=0$,

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{17}
$$

The shelf estimate (7) becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Using (16),

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac52y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{18}
$$

For fixed $\kappa$, both $y^4/(1-y^2)$ and
$y/\sqrt{1-y^2}$ increase strictly for $y>0$; both terms in (18)
decrease with $\kappa$.  Thus their closed proxy maxima occur at
$y^2=1/8$, $\rho=7/8$, and $\kappa=32$.  There

$$
\frac{y^4}{\kappa\rho}\le\frac1{1792},
\qquad
y\sqrt{\frac{2\pi}{\kappa\rho}}
\le\sqrt{\frac\pi{112}}<\frac{67}{400}.
\tag{19}
$$

The last comparison follows by positive squaring from (11), with the
exact radical reserve

$$
\left(\frac{67}{400}\right)^2
-\frac{1571/500}{112}
=\frac3{1120000}>0.
\tag{20}
$$

Consequently

$$
\widehat q
<\frac1{1792}+\frac52\frac{67}{400}
=\frac{3757}{8960}
<\frac{17}{40},
\tag{21}
$$

and the displacement-proxy reserve is exactly

$$
\frac{17}{40}-\frac{3757}{8960}
=\frac{51}{8960}>0.
\tag{22}
$$

In particular, $1-\widehat q>23/40>0$.  Equations (17) and (21) give

$$
t=1-w>1-\widehat q>\frac{23}{40}.
$$

Therefore, before invoking any outer-region slope,

$$
\boxed{
\frac{x_0}{K}=\rho t
>\frac78\frac{23}{40}
=\frac{161}{320}
=\frac12+\frac1{320}.
}
\tag{23}
$$

## 5. Ordinary-floor wall and self-consistency

For $0<z<\mu$, put

$$
\sigma(z)=-A'(z)
=\frac1\pi\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
$$

Direct differentiation shows that $\sigma$ is increasing.  At
$x_0=\mu t$,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{24}
$$

Define

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho}.
\tag{25}
$$

Then

$$
Q>1,
\qquad
0<a\le\frac17,
\qquad
\widehat q=a(Q-1)<\frac{17}{40}.
\tag{26}
$$

Furthermore,

$$
1-\rho t
=\varepsilon+\frac UK
<y^2+\frac{y^4+y^3S}{\kappa}
=y^2Q.
$$

Since $0<\rho t<1$,

$$
1-\rho^2t^2
=(1-\rho t)(1+\rho t)
<2y^2Q.
\tag{27}
$$

In the dangerous branch $p>0$.  Its plateau definition gives

$$
\left\lfloor A(x_0)+\frac14\right\rfloor
=
\left\lfloor A(x_0+p)+\frac14\right\rfloor.
$$

Two real numbers having the same ordinary floor differ by strictly less
than one, including when either lies on an integer wall.  Since $A$ is
decreasing,

$$
A(x_0)-A(x_0+p)<1.
\tag{28}
$$

The monotonicity of $\sigma$ and (24)--(27) now yield

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0)
>\frac{Pt}{\pi\sqrt{2Q}}.
$$

Here $P,t,\pi,Q$ and $1-\widehat q$ are positive.  Squaring therefore
preserves direction, and $t>1-\widehat q$ gives the strict
self-consistency inequality

$$
\boxed{
P^2<H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{29}
$$

No denominator or squaring wall has been crossed.

## 6. Entire synthetic path and the uniform loss cap

From (4) and (10),

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{30}
$$

Thus $0<r\le P$.  For fixed $P,y,\kappa,d$, the quantity $Q$ decreases
with $r$.  Moreover, when $\widehat q=a(Q-1)<1$,

$$
\frac{\partial}{\partial Q}
\left(\frac{2\pi^2Q}{(1-a(Q-1))^2}\right)
=2\pi^2\frac{1+\widehat q+2a}{(1-\widehat q)^3}>0.
\tag{31}
$$

Hence $H(P,r)$ decreases with $r$.

Let

$$
B=\frac{14}{3}.
$$

Suppose for contradiction that $r\ge B$.  Since $r\le P$, also
$P\ge B$, and monotonicity in $r$ gives

$$
H(P,r)\le H(P,B).
\tag{32}
$$

For every synthetic point $P'\in[B,P]$, freeze $r=B$ and set

$$
S'=P'+\frac{P'-B}{d}<\frac52P'.
$$

Because $P'\le P$, the original shelf ceiling continues to hold along
the whole path.  Thus the uniform bounds
$\widehat q<17/40$ and $a\le1/7$ hold at every synthetic point, not only
at its two endpoints.  Along that path,

$$
\frac{\partial Q}{\partial P'}
=\frac y\kappa\left(1+\frac1d\right)
<\frac{99}{280}\frac1{32}\frac52
=\frac{99}{3584}.
\tag{33}
$$

Differentiating $H$ and using (11), (21), (26), and (33), uniformly on
the path, gives

$$
\begin{aligned}
\frac{\partial H}{\partial P'}
&=2\pi^2\frac{\partial Q}{\partial P'}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}\\
&<2\left(\frac{1571}{500}\right)^2
\frac{99}{3584}
\frac{1+17/40+2/7}{(1-17/40)^3}\\
&=\frac{117036972261}{23847320000}<5.
\end{aligned}
\tag{34}
$$

The exact derivative reserve is

$$
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0.
\tag{35}
$$

It follows on every point of the synthetic path that

$$
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2P'-5
\ge2B-5
=\frac{13}{3}>0.
\tag{36}
$$

At the initial endpoint $P'=r=B$ one has $S'=B$ exactly.  By
(9), (13), and $\kappa\ge32$,

$$
Q
<1+\frac1{256}
+\frac{(99/280)(14/3)}{32}
=\frac{1351}{1280},
$$

and hence

$$
\widehat q
<\frac17\left(\frac{1351}{1280}-1\right)
=\frac{71}{8960}.
$$

The exact initial endpoint reserve is

$$
\begin{aligned}
B^2
&-2\left(\frac{1571}{500}\right)^2
\frac{1351/1280}{(1-71/8960)^2}\\
&=\frac{49714811804}{82306584375}>0.
\end{aligned}
\tag{37}
$$

Equations (32), (36), and (37) imply

$$
P^2-H(P,r)
\ge P^2-H(P,B)
\ge B^2-H(B,B)>0,
$$

contradicting (29).  Thus the whole synthetic path, including its
no-drop endpoint $P=r=B$, proves

$$
\boxed{R<\frac{14}{3\sqrt\varepsilon}.}
\tag{38}
$$

## 7. Action gain, floor loss, and exceptional branches

For $0\le v\le1$, set $x=\arccos(1-v)\ge0$.  Since
$\cos x\ge1-x^2/2$,

$$
\arccos(1-v)\ge\sqrt{2v}.
$$

The exact action identity therefore gives

$$
\eta
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{39}
$$

On (9), using the freshly derived rational bounds (11)--(12),

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
\ge\frac{64\sqrt2}{3\pi y}
>\frac{4480000}{466587}\frac1y.
\tag{40}
$$

The coefficient exceeds $B$ by the exact amount

$$
\frac{4480000}{466587}-\frac{14}{3}
=\frac{2302594}{466587}>0.
\tag{41}
$$

If $R>0$, then the universally strict floor inequality
$\lfloor x\rfloor>x-1$, including at integer $x$, together with (13),
(38), and (40), gives

$$
\begin{aligned}
M
&=\lfloor K\eta\rfloor-R\\
&>\left(\frac{4480000}{466587}-\frac{14}{3}\right)\frac1y-1\\
&>\left(\frac{4480000}{466587}-\frac{14}{3}\right)
\frac{280}{99}-1
=\frac{598534207}{46192113}.
\end{aligned}
\tag{42}
$$

Meanwhile, (6) and the upper radical bound in (12) give

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175}.
$$

Thus the dangerous branch has the strict payment reserve

$$
\boxed{
M-4\delta>
\frac{598534207}{46192113}-\frac{132}{175}
=\frac{98646127309}{8083619775}>0.
}
\tag{43}
$$

If $R\le0$, then $M\ge\lfloor K\eta\rfloor$, and no localization or
plateau cap is needed.  Instead,

$$
M>\frac{4480000}{466587}\frac{280}{99}-1
=\frac{1208207887}{46192113},
$$

so the safe branch has reserve

$$
\boxed{
M-4\delta>
\frac{205339021309}{8083619775}>0.
}
\tag{44}
$$

This division owns every exceptional plateau branch:

* if $p=n>0$, then $m=0$ and $R=p>0$, so the full dangerous path,
  including $P=r=B$, applies;
* if $p=0<n$, then $R=-dn<0$, so the immediate-drop branch is safe;
* if $n=0$, then $p=m=R=0$, so the degenerate head is safe;
* the wall $R=0$ belongs to the safe branch from either side;
* the first discrete branch with $R>0$ is covered without assuming any
  positive lower bound on $R$.

Substitution of (43)--(44) into (5) gives

$$
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^K A(z)\,dz
$$

for every low-interface shifted tail.  The permitted high-interface
shifted-tail result, high-angular result, strict-to-ordinary-floor
transfer, and weighted multiplicity scaffold then give (1).

## 8. Discrete, interface, spectral, and threshold walls

The strict estimates above survive every required wall.

1. At $\mu-x_0\in\mathbb Z$, one has $\beta=0$ and
   $U=p+m<1+p+m$.  On either adjacent cell $0\le\beta<1$, so the same
   strict inequality holds as $\beta\to1^-$.  No estimate fixes $n$
   across this wall.
2. At $q=\mu$, $\beta=0$ and $\delta=0$.  At $x_0=\mu$, the permitted
   high-interface theorem owns equality; the $n=0$ low-interface limit is
   already in the safe branch.
3. At every ordinary-floor wall in the definition of $h_j$, equality of
   the two ordinary floors still implies the strict difference (28).
   When $p$ changes at a neighboring floor or coarse-proxy integer wall,
   it merely selects one of the already-covered branches.
4. At $K\eta\in\mathbb Z$, the relation
   $\lfloor K\eta\rfloor>K\eta-1$ remains strict.  Thus the entire
   possible unit floor loss is already paid in (42)--(44).
5. Every denominator in (17)--(34) is positive, and the only squaring is
   performed after positivity is shown.  The complete synthetic path is
   bounded uniformly; no sampled or endpoint-only monotonicity is used.
6. The local proof assumes $\kappa\ge32$, not $\kappa>32$.
   Therefore $K=32/\varepsilon^2$, including
   $(\varepsilon,K)=(1/8,2048)$, is covered.  Its strictness comes from
   the angular, radical, displacement, path, endpoint, floor, and payment
   reserves, not from an open energy assumption.
7. The strict spectral convention, the low/high interface transfer, and
   the angular cutoff $\nu=K$ are exactly those of the permitted phase and
   shifted-tail inputs.  No strict spectral bracket is replaced by an
   ordinary unshifted floor.

The theorem-overlap faces are also explicit.  At
$\varepsilon=1/100$ the complete endpoint begins; at $1/25$ Round 10
owns the sharper $\kappa=20$ face; at $1/20$ Rounds 12 and 13 own the
$\kappa=24$ face; at $1/10$ Round 13 owns the sharper $\kappa=24$ face;
and at $1/8$ the new theorem owns $\kappa=32$.  Equation (1) itself is
valid at all of these $\varepsilon$ faces when $\kappa\ge32$, but the
global envelope always uses the sharpest accepted theorem.  The current
architecture's failed $\kappa=24$ localization is not used and is not a
counterexample to any possible stronger theorem.

## 9. Independent exact endpoint $K_0(7/8)<550^2$

This section uses neither (1) nor any of its plateau estimates.  At
$\rho=7/8$, the action inequality (39) simplifies exactly to

$$
\eta_{7/8}\ge\frac1{24\pi}.
$$

By (11),

$$
24\pi<24\frac{1571}{500}=\frac{9426}{125}<76,
\qquad
76-\frac{9426}{125}=\frac{74}{125}>0.
$$

Thus

$$
\boxed{\eta_{7/8}>\frac1{76}.}
\tag{45}
$$

Also

$$
a_{7/8}=14\pi<14\frac{22}{7}=44<49,
$$

so, by positive square roots,

$$
\boxed{\sqrt{a_{7/8}}<7.}
\tag{46}
$$

Finally, (12) gives

$$
C_0=1+\frac{8\sqrt2}{15}
<1+\frac8{15}\frac{99}{70}
=\frac{307}{175}.
\tag{47}
$$

For $Y=550$, (45)--(47) imply the strict exact comparison

$$
\begin{aligned}
\eta_{7/8}Y^2-\sqrt{a_{7/8}}Y-C_0
&>\frac1{76}550^2-7\cdot550-\frac{307}{175}\\
&=\frac{427292}{3325}>0.
\end{aligned}
\tag{48}
$$

The number $X=\sqrt{K_0(7/8)}$ from the permitted formula is precisely
the positive root of

$$
\eta_{7/8}X^2-\sqrt{a_{7/8}}X-C_0=0.
$$

The constant term is negative and the leading coefficient is positive,
so the two roots have opposite signs and the positive root is unique.
Equation (48) therefore places that root strictly below $550$, proving
(2).  The fixed-ratio theorem includes the equality face
$K=K_0(7/8)$, while (48) puts that entire threshold strictly below
$550^2$.

## 10. Closed six-zone global union

Now, and only now that both (1) and (2) are proved, assemble the permitted
global inputs in the following six closed finite zones, followed by the
unchanged all-frequency endpoint.

1. On $[\rho_*,1/16]$, every possible residual satisfies $K<64$; the
   small-hole theorem owns $\rho=\rho_*$.
2. On $[1/16,7/8]$, monotonicity of $K_0$ and (2) give
   $K<K_0(7/8)<550^2$ for every possible residual.
3. On $[7/8,9/10]$, (1) leaves only
   $$K<\frac{32}{(1-\rho)^2}\le3200.$$
4. On $[9/10,19/20]$, Round 13 leaves only
   $$K<\frac{24}{(1-\rho)^2}\le9600.$$
5. On $[19/20,24/25]$, the retained constant-$24$ theorem leaves only
   $K<15000$.
6. On $[24/25,99/100]$, Round 10 leaves only $K<200000$.
7. Every frequency on $[99/100,1)$ is already proved by the complete
   endpoint theorem.

The finite comparisons are

$$
64<3200<9600<15000<200000<550^2,
\tag{49}
$$

with exact ceiling reserves

$$
550^2-64=302436,
\qquad
550^2-3200=299300,
$$

$$
550^2-9600=292900,
\qquad
550^2-15000=287500,
\qquad
550^2-200000=102500.
\tag{50}
$$

Every shared face is owned with the sharpest theorem.  The central
regimes meet at $\rho=1/16$.  At $\rho=7/8$, (1) includes
$K=32/(1/8)^2=2048$.  At $\rho=9/10$, Round 13 owns the sharper face
$K=24/(1/10)^2=2400$ (and hence also the coarse $K=3200$ face).  At
$\rho=19/20$, the constant-$24$ theorem includes $K=9600$.  At
$\rho=24/25$, Round 10 owns the sharper $K=12500$ face, while the
left-hand coarse bound reaches $15000$.  At $\rho=99/100$, the
all-frequency endpoint owns every $K$, including $200000$.  The
$K=64$ face is owned by its adjacent central theorem, and the strict
central bound (2) owns $K=550^2$.  Thus equality in (3) is included.

The exact improvement over the Round 13 ceiling is

$$
\frac{900^2}{550^2}=\frac{324}{121}
=2+\frac{82}{121}>2.
\tag{51}
$$

The compact residual below $550^2$ remains open.

## 11. Executable standard-library exact ledger

This ledger checks every finite rational comparison used above.  It is
not a Bessel-root certificate and does not replace the symbolic branch
proof.

```python
from fractions import Fraction as F

# Machin upper bound and elementary radicals.
machin_upper = F(5277328977275528, 1679825970703125)
assert F(1571, 500) - machin_upper == F(
    2736890694763, 6719303882812500
)
assert F(22, 7) - F(1571, 500) == F(3, 3500)
assert F(2) - F(140, 99) ** 2 == F(2, 9801)
assert F(99, 70) ** 2 - F(2) == F(1, 4900)

# Angular, radical, displacement, and localization reserves.
assert F(7, 8) ** 2 - F(3, 4) == F(1, 64)
assert F(67, 400) ** 2 - F(1571, 500) / 112 == F(
    3, 1120000
)
q_proxy = F(1, 1792) + F(5, 2) * F(67, 400)
assert q_proxy == F(3757, 8960)
assert F(17, 40) - q_proxy == F(51, 8960)
assert F(7, 8) * F(23, 40) == F(161, 320)
assert F(161, 320) - F(1, 2) == F(1, 320)

# Complete fixed-r synthetic path.
dQ = F(99, 3584)
path_derivative = (
    2
    * F(1571, 500) ** 2
    * dQ
    * (1 + F(17, 40) + 2 * F(1, 7))
    / (1 - F(17, 40)) ** 3
)
assert path_derivative == F(117036972261, 23847320000)
assert F(5) - path_derivative == F(2199627739, 23847320000)
assert 2 * F(14, 3) - 5 == F(13, 3)

B = F(14, 3)
Q0 = 1 + F(1, 256) + F(99, 280) * B / 32
q0 = F(1, 7) * (Q0 - 1)
assert Q0 == F(1351, 1280)
assert q0 == F(71, 8960)
endpoint_reserve = (
    B**2
    - 2 * F(1571, 500) ** 2 * Q0 / (1 - q0) ** 2
)
assert endpoint_reserve == F(49714811804, 82306584375)

# Action gain, full floor loss, and interface payment.
gain = 64 * F(140, 99) / (3 * F(1571, 500))
assert gain == F(4480000, 466587)
assert gain - B == F(2302594, 466587)
dangerous_M = (gain - B) * F(280, 99) - 1
safe_M = gain * F(280, 99) - 1
assert dangerous_M == F(598534207, 46192113)
assert safe_M == F(1208207887, 46192113)
delta_cap = F(8, 15) * F(99, 70)
assert delta_cap == F(132, 175)
assert dangerous_M - delta_cap == F(
    98646127309, 8083619775
)
assert safe_M - delta_cap == F(
    205339021309, 8083619775
)

# Independent central endpoint at rho=7/8.
assert 24 * F(1571, 500) == F(9426, 125)
assert F(76) - F(9426, 125) == F(74, 125)
assert F(49) - 14 * F(22, 7) == 5
assert 1 + F(8, 15) * F(99, 70) == F(307, 175)
assert (
    F(1, 76) * 550**2 - 7 * 550 - F(307, 175)
) == F(427292, 3325)

# Closed global union and exact ceiling reduction.
assert 550**2 - 64 == 302436
assert 550**2 - 3200 == 299300
assert 550**2 - 9600 == 292900
assert 550**2 - 15000 == 287500
assert 550**2 - 200000 == 102500
assert F(900**2, 550**2) == F(324, 121)
assert F(324, 121) - 2 == F(82, 121)

print("all exact Round 14 incumbent ledger checks passed")
```

## Final assessment

No candidate implication failed.  The first potentially dangerous signs
instead have the strict exact reserves $51/8960$ (uniform displacement),
$49714811804/82306584375$ (synthetic-path endpoint), and
$98646127309/8083619775$ (dangerous action payment).  The fresh local
seam proof, all exceptional branches and walls, the independent endpoint,
and the closed six-zone union therefore pass the incumbent gate.
