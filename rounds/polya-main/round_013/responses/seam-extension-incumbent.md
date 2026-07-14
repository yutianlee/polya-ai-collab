# Round 13 incumbent: central--thin seam at $\rho=9/10$

## Verdict

**PASS.** The frozen candidate constants close on the whole proposed domain.
Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{10}.
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

The proof below is a fresh derivation on $0<\varepsilon\le1/10$; it does
not extrapolate any Round 12 intermediate estimate.  In the final
piecewise envelope, (1) is used as new coverage only for
$1/20\le\varepsilon\le1/10$.  The promoted Round 12 result remains in
force for $\varepsilon\le1/20$, and the sharper Round 10 threshold
$20/\varepsilon^2$ remains in force for $\varepsilon\le1/25$.

The separate endpoint calculation also proves

$$
\boxed{K_0(9/10)<900^2},
\tag{2}
$$

so the closed global union gives

$$
\boxed{0<\rho<1,\qquad K\ge900^2.}
\tag{3}
$$

Statement (3) is an all-ratio high-frequency theorem, not the complete
all-frequency shell theorem.

## 1. Shifted-tail reduction and scaling

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

For a low-interface shifted tail beginning at $x_0=r_0+1/2<\mu$, write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1),
$$

and define $p$ exactly as in the frozen packet: for
$h_j=\lfloor A(x_0+j)+1/4\rfloor$, either
$h_0=h_p>h_{p+1}$ with $0\le p<n$, or $p=n$ if no drop occurs.  Thus
$p=0$ is the immediate-drop case.  Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{4}
$$

For $n=0$, the convention is $p=m=0$.  The audited pre-threshold
decomposition is

$$
\frac{\mathcal T_{r_0}}2
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,
\qquad
\delta=\int_q^\mu G_\mu(z)\,dz,
\qquad
0\le\delta<\frac{2\sqrt2}{15},
\tag{5}
$$

and the unconditional shelf estimate is

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{6}
$$

Thus it suffices to prove $M>4\delta$.  Only $R>0$ requires a new
plateau-loss estimate.

Use

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4.
\tag{7}
$$

The exact domain is

$$
0<y\le\frac1{\sqrt{10}},
\qquad
\rho=1-y^2\ge\frac9{10},
\qquad
\kappa\ge24.
\tag{8}
$$

In the branch $R>0$, put

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{9}
$$

## 2. Reconstructed elementary constants

We use the strict rational bounds

$$
\pi<\frac{1571}{500}<\frac{22}{7},
\qquad
\frac{140}{99}<\sqrt2<\frac{99}{70},
\qquad
\sqrt{10}>\frac{79}{25},
\qquad
\frac1{\sqrt{10}}<\frac8{25},
\qquad
\sqrt5<\frac94.
\tag{10}
$$

They are recorded here rather than imported from an earlier seam proof.
Machin's identity and the alternating arctangent series give

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
<\frac{1571}{500}.
\end{aligned}
\tag{11}
$$

The last margin is

$$
\frac{2736890694763}{6719303882812500}>0,
$$

and $22/7-1571/500=3/3500>0$.  All radical comparisons in (10) follow
by squaring positive quantities:

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801},
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900},
$$

$$
10-\left(\frac{79}{25}\right)^2=\frac9{625},
\qquad
10-\left(\frac{25}{8}\right)^2=\frac{15}{64},
\qquad
\left(\frac94\right)^2-5=\frac1{16}.
\tag{12}
$$

## 3. The angular factor: $d>2/3$

Since

$$
\left(\frac9{10}\right)^2-\left(\frac{\sqrt3}{2}\right)^2
=\frac3{50}>0,
$$

we have

$$
\rho\ge\frac9{10}>\frac{\sqrt3}{2}=\cos\frac\pi6.
$$

The arccosine is strictly decreasing, so

$$
\arccos\rho<\frac\pi6,
\qquad
\boxed{d>\frac23}.
\tag{13}
$$

If $R>0$, then $p>0$, and (4) gives

$$
m<\frac pd<\frac32p,
\qquad
S<\frac52P.
\tag{14}
$$

The no-drop geometry $p=n>0$ has $m=0$ and is included in (14).

## 4. Dangerous-plateau localization

Define

$$
t=\frac{x_0}{\rho K},
\qquad
w=1-t=\frac{U}{\rho K}.
$$

Because $U=n+\beta<1+p+m$, including when $\beta=0$,

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{15}
$$

The shelf estimate (6) becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Using (14),

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac52y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{16}
$$

For fixed $\kappa$, both $y^4/(1-y^2)$ and
$y/\sqrt{1-y^2}$ increase strictly with $y>0$; both terms in (16)
decrease with $\kappa$.  Thus the largest allowed proxies occur at
$y^2=1/10$ and $\kappa=24$.  There,

$$
\frac{y^4}{\kappa\rho}\le\frac1{2160},
\qquad
y\sqrt{\frac{2\pi}{\kappa\rho}}
\le\sqrt{\frac\pi{108}}
<\sqrt{\frac{11}{378}}
<\frac{171}{1000},
\tag{17}
$$

where the final squaring margin is

$$
\left(\frac{171}{1000}\right)^2-\frac{11}{378}
=\frac{26549}{189000000}>0.
$$

Consequently

$$
\widehat q
<\frac1{2160}+\frac52\frac{171}{1000}
=\frac{2311}{5400}
<\frac37,
\tag{18}
$$

with the advertised exact displacement reserve

$$
\frac37-\frac{2311}{5400}
=\frac{23}{37800}>0.
\tag{19}
$$

It follows that

$$
t=1-w>1-\widehat q>\frac47,
$$

and therefore every dangerous plateau is localized by

$$
\boxed{
\frac{x_0}{K}=\rho t
>\frac9{10}\frac47
=\frac{18}{35}
=\frac12+\frac1{70}.
}
\tag{20}
$$

In particular, the outer-region slope is not used before its localization
has been established.

## 5. The shifted-floor wall and self-consistency

For $0<z<\mu$, set

$$
\sigma(z)=-A'(z)
=\frac1\pi\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
$$

Direct differentiation shows that $\sigma$ is increasing.  Since
$x_0=\mu t$,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{21}
$$

Put

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho}.
\tag{22}
$$

Then

$$
\widehat q=a(Q-1),
\qquad
0<a\le\frac19.
\tag{23}
$$

Moreover,

$$
1-\rho t
=\varepsilon+\frac UK
<y^2+\frac{y^4+y^3S}{\kappa}
=y^2Q,
$$

so

$$
1-\rho^2t^2
=(1-\rho t)(1+\rho t)
<2y^2Q.
\tag{24}
$$

In the dangerous branch $p>0$.  By definition of the plateau,

$$
\left\lfloor A(x_0)+\frac14\right\rfloor
=
\left\lfloor A(x_0+p)+\frac14\right\rfloor.
$$

Two real numbers with the same ordinary floor differ by strictly less
than one, even if one of them lies on an integer wall.  Since $A$ is
decreasing,

$$
A(x_0)-A(x_0+p)<1.
\tag{25}
$$

Monotonicity of $\sigma$ and (21)--(24) now give

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0)
>\frac{Pt}{\pi\sqrt{2Q}}.
$$

Here $P>0$, $t>4/7$, $Q>1$, and $\pi>0$, so every quantity squared in
the next step is positive.  Squaring and then using
$t>1-\widehat q>4/7$ yields

$$
\boxed{
P^2<H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{26}
$$

Thus no sign is lost in the self-consistency squaring, and its denominator
is uniformly positive.

## 6. Complete synthetic path and the loss cap $B=14/3$

From (4) and (9),

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{27}
$$

Hence $0<r\le P$.  For fixed $P,y,\kappa,d$, the quantity $Q$ decreases
with $r$.  Also

$$
\frac{\partial}{\partial Q}
\left(\frac{2\pi^2Q}{(1-a(Q-1))^2}\right)>0
$$

whenever $a(Q-1)<1$.  This condition holds by (18), so $H$ decreases
with $r$.

Let

$$
B=\frac{14}{3}.
$$

Assume for contradiction that $r\ge B$.  Then

$$
H(P,r)\le H(P,B).
\tag{28}
$$

For every synthetic point $P'\in[B,P]$, keep $r=B$ and put

$$
S'=P'+\frac{P'-B}{d}<\frac52P'.
$$

Because $P'\le P$, the original shelf ceiling remains valid along the
whole path.  Hence (18) holds at every synthetic point, not merely at the
endpoint.  Along this path,

$$
\frac{\partial Q}{\partial P'}
=\frac y\kappa\left(1+\frac1d\right)
<\frac8{25}\frac1{24}\frac52
=\frac1{30}.
\tag{29}
$$

Since $\widehat q=a(Q-1)$,

$$
\frac{\partial H}{\partial P'}
=2\pi^2\frac{\partial Q}{\partial P'}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
\tag{30}
$$

All factors are positive.  Using (10), (18), (23), and (29) at every
point of the path gives

$$
\frac{\partial H}{\partial P'}
<2\left(\frac{1571}{500}\right)^2\frac1{30}
\frac{1+3/7+2/9}{(1-3/7)^3}
=\frac{1572142117}{270000000}
<6,
\tag{31}
$$

with exact margin

$$
6-\frac{1572142117}{270000000}
=\frac{47857883}{270000000}>0.
$$

Therefore the synthetic comparison function satisfies

$$
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2P'-6
\ge2B-6
=\frac{10}{3}>0.
\tag{32}
$$

It remains to check the complete path's initial endpoint $P'=r=B$.  At
that point $S=B$ exactly.  From (8), (10), and $\kappa\ge24$,

$$
Q
<1+\frac1{240}+\frac{(8/25)(14/3)}{24}
=\frac{3839}{3600},
$$

and, using $a\le1/9$,

$$
\widehat q
<\frac19\left(\frac{3839}{3600}-1\right)
=\frac{239}{32400}.
$$

The exact endpoint reserve is

$$
\begin{aligned}
B^2
&-2\left(\frac{1571}{500}\right)^2
\frac{3839/3600}{(1-239/32400)^2}\\
&=\frac{2376966388822}{5818105805625}>0.
\end{aligned}
\tag{33}
$$

Equations (28), (32), and (33) imply

$$
P^2-H(P,r)
\ge P^2-H(P,B)
\ge B^2-H(B,B)>0,
$$

contradicting (26).  Thus

$$
\boxed{R<\frac{14}{3\sqrt\varepsilon}.}
\tag{34}
$$

The proof controls every point of the possible synthetic path.  The
no-drop branch $p=n>0$ has $m=0$ and hence $P=r$; it is included, with
the synthetic point $P=r=B$ explicitly controlled by (33).

## 7. Action payment and all exceptional branches

For $0\le v\le1$, put $x=\arccos(1-v)$.  The elementary inequality
$\cos x\ge1-x^2/2$ gives

$$
\arccos(1-v)\ge\sqrt{2v}.
$$

Using the exact action identity,

$$
\eta
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{35}
$$

Consequently, on (8),

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
\ge\frac{16\sqrt2}{\pi y}
>\frac{1120000}{155529}\frac1y.
\tag{36}
$$

The last strict inequality is exactly the use of
$\sqrt2>140/99$ and $\pi<1571/500$.  Its coefficient exceeds $B$:

$$
\frac{1120000}{155529}-\frac{14}{3}
=\frac{394198}{155529}>0.
$$

If $R>0$, then (34), (36), and the universally strict inequality
$\lfloor x\rfloor>x-1$ give

$$
M
>\left(\frac{1120000}{155529}-\frac{14}{3}\right)\frac1y-1
>\left(\frac{1120000}{155529}-\frac{14}{3}\right)\frac{79}{25}-1
=\frac{27253417}{3888225}.
\tag{37}
$$

Meanwhile,

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175}.
$$

Therefore the exact dangerous-branch payment reserve is

$$
\boxed{
M-4\delta>
\frac{27253417}{3888225}-\frac{132}{175}
=\frac{170244091}{27217575}>0.
}
\tag{38}
$$

If $R\le0$, no localization or plateau cap is needed.  Instead,

$$
M\ge\lfloor K\eta\rfloor
>K\eta-1
>\frac{1120000}{155529}\frac{79}{25}-1
=\frac{3383671}{155529},
$$

and hence

$$
M-4\delta>
\frac{571612597}{27217575}>0.
\tag{39}
$$

This owns all exceptional branches:

- if $p=n>0$, then $m=0$ and $R=p>0$, so the complete dangerous path,
  including (33), applies;
- if $p=0<n$, then $R=-dn<0$, so the immediate-drop branch is safe;
- if $n=0$, then $p=m=R=0$, so the degenerate head is safe;
- the sign wall $R=0$ belongs to the safe branch;
- the first discrete branch with $R>0$ is covered by the same argument,
  which assumes no positive lower bound on $R$.

Substitution of (38)--(39) into (5) gives

$$
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^K A(z)\,dz
$$

for every low-interface shifted tail.  The permitted high-interface
shifted-tail theorem, high-angular theorem, strict-to-ordinary-floor
transfer, and weighted multiplicity scaffold then yield (1).

## 8. Discrete, interface, threshold, and spectral walls

The proof retains the required strictness at every wall.

1. If $\mu-x_0$ is an integer, then $\beta=0$ and
   $U=n=p+m<1+p+m$ remains strict.  On the adjacent cells
   $0\le\beta<1$, so the same strict inequality survives as
   $\beta\to1^-$.  No estimate assumes a fixed value of $n$ across that
   wall.
2. At $q=\mu$, one has $\beta=0$ and $\delta=0$.  At the low/high
   interface $x_0=\mu$, the permitted high-interface theorem owns the
   equality; the $n=0$ low-interface limit is already safe.
3. Equal values of
   $\lfloor A(x_0+j)+1/4\rfloor$ imply the strict difference (25), even
   when either shifted value is integral.  A change of $p$ at any proxy
   integer wall simply selects an adjacent branch already covered above.
4. At $K\eta\in\mathbb Z$, the strict inequality
   $\lfloor K\eta\rfloor>K\eta-1$ is still valid, with extra slack.
5. The local proof assumes $\kappa\ge24$, not $\kappa>24$.  Thus
   $K=24/\varepsilon^2$ is included; strictness comes from the rational,
   floor, and payment margins.  On $\varepsilon\le1/25$, the retained
   Round 10 face $\kappa=20$ remains owned by that sharper theorem.
6. The strict spectral convention, the low/high interface transfer, and
   the angular cutoff $\nu=K$ are exactly those of the permitted phase and
   shifted-tail inputs.  No strict spectral bracket is replaced by an
   equality or by an unshifted floor.

In particular, the faces $\varepsilon=1/100,1/25,1/20,1/10$ are all
covered.  At $1/20$, the closed Round 12 and Round 13 constant-$24$
theorems overlap; at $1/25$ and $1/100$, the sharper retained constant-$20$
theorem is used in the global envelope.

## 9. Exact fixed-ratio endpoint at $\rho=9/10$

At $\rho=9/10$,

$$
a_\rho=18\pi<18\frac{22}{7}<8^2,
\qquad
8^2-18\frac{22}{7}=\frac{52}{7}>0.
\tag{40}
$$

The action bound (35) at $\varepsilon=1/10$ simplifies exactly to

$$
\eta_{9/10}
\ge\frac1{15\pi\sqrt5}.
$$

By (10),

$$
15\pi\sqrt5
<15\frac{22}{7}\frac94
=\frac{1485}{14}
<107,
$$

where $107-1485/14=13/14>0$.  Hence

$$
\eta_{9/10}>\frac1{107}.
\tag{41}
$$

Also

$$
C_0=1+\frac{8\sqrt2}{15}
<1+\frac8{15}\frac{99}{70}
=\frac{307}{175}.
\tag{42}
$$

For $Y>0$, let

$$
F(Y)=\eta_{9/10}Y^2-\sqrt{a_{9/10}}Y-C_0.
$$

At $Y=900$, (40)--(42) give the strict exact comparison

$$
F(900)
>\frac1{107}900^2-8\cdot900-\frac{307}{175}
=\frac{6897151}{18725}>0.
\tag{43}
$$

The defining formula for $K_0$ says that $\sqrt{K_0(9/10)}$ is the
positive zero of $F$.  Indeed, $F(0)=-C_0<0$, its leading coefficient is
positive, and the product of its two roots is negative, so it has exactly
one positive root.  Positivity at $Y=900$ therefore places that root
strictly below $900$, proving (2).  The fixed-ratio theorem includes the
face $K=K_0(9/10)$; (43) locates that entire threshold below $900^2$.

## 10. Closed global union

Assemble the accepted endpoint and fixed-ratio results with (1)--(2) in
the following closed zones.

1. The small-hole endpoint proves every frequency on
   $0<\rho\le\rho_*$.  On $[\rho_*,1/16]$, every possible residual has
   $K<64$.
2. On $[1/16,9/10]$, the audited monotonicity of $K_0$ and (2) give
   $K<K_0(9/10)<900^2$ for every possible residual.
3. On $[9/10,19/20]$, use the new theorem only on
   $1/20\le\varepsilon\le1/10$.  Every possible residual satisfies
   $$K<\frac{24}{\varepsilon^2}\le9600.$$
4. On $[19/20,24/25]$, retain the Round 12 theorem.  Every possible
   residual satisfies $K<24/\varepsilon^2\le15000$.
5. On $[24/25,99/100]$, retain the sharper Round 10 theorem.  Every
   possible residual satisfies $K<20/\varepsilon^2\le200000$.
6. The complete Round 11 endpoint proves every frequency on
   $[99/100,1)$.

The exact finite comparisons are

$$
900^2-64=809936,
\qquad
900^2-9600=800400,
$$

$$
900^2-15000=795000,
\qquad
900^2-200000=610000.
\tag{44}
$$

Every shared ratio face is owned.  At $\rho=\rho_*$ the small-hole and
compact descriptions meet; at $\rho=1/16$ the two central descriptions
meet; at $\rho=9/10$ the fixed-ratio and new seam theorems meet; at
$\rho=19/20$ the two closed constant-$24$ seam theorems overlap; at
$\rho=24/25$ the sharper Round 10 theorem owns the assigned right-hand
zone; and at $\rho=99/100$ it meets the all-frequency endpoint.  The
frequency faces $K=64$, $K=9600$, $K=15000$, and $K=200000$ are proved
because the corresponding residual bounds are strict.  The face
$K=900^2$ is strictly above every finite threshold in (44) and above the
central threshold by (2).  This proves (3).

Relative to the Round 12 ceiling, the exact reduction factor is

$$
\frac{3300^2}{900^2}=\frac{121}{9}
=13+\frac49>13.
\tag{45}
$$

The compact residual below $900^2$ remains open, and the complete
all-frequency endpoint remains exactly $99/100\le\rho<1$.

## 11. Executable standard-library exact ledger

This is a finite rational constants ledger.  It is not a Bessel-root
certificate.

```python
from fractions import Fraction as F

# Machin upper bound and elementary constants.
machin_upper = F(5277328977275528, 1679825970703125)
assert F(1571, 500) - machin_upper == F(
    2736890694763, 6719303882812500
)
assert F(22, 7) - F(1571, 500) == F(3, 3500)
assert F(2) - F(140, 99) ** 2 == F(2, 9801)
assert F(99, 70) ** 2 - F(2) == F(1, 4900)
assert F(10) - F(79, 25) ** 2 == F(9, 625)
assert F(10) - F(25, 8) ** 2 == F(15, 64)
assert F(9, 4) ** 2 - F(5) == F(1, 16)

# d comparison and dangerous-plateau localization.
assert F(9, 10) ** 2 - F(3, 4) == F(3, 50)
assert F(171, 1000) ** 2 - F(11, 378) == F(
    26549, 189000000
)
qbar_proxy = F(1, 2160) + F(5, 2) * F(171, 1000)
assert qbar_proxy == F(2311, 5400)
assert F(3, 7) - qbar_proxy == F(23, 37800)
assert F(9, 10) * F(4, 7) == F(18, 35)
assert F(18, 35) - F(1, 2) == F(1, 70)

# Complete fixed-r synthetic path.
path_derivative = (
    2
    * F(1571, 500) ** 2
    * F(1, 30)
    * (1 + F(3, 7) + F(2, 9))
    / F(4, 7) ** 3
)
assert path_derivative == F(1572142117, 270000000)
assert F(6) - path_derivative == F(47857883, 270000000)
assert 2 * F(14, 3) - 6 == F(10, 3)

B = F(14, 3)
Q0 = F(3839, 3600)
q0 = F(239, 32400)
endpoint_reserve = (
    B**2
    - 2 * F(1571, 500) ** 2 * Q0 / (1 - q0) ** 2
)
assert endpoint_reserve == F(
    2376966388822, 5818105805625
)

# Action gain, full floor loss, and interface payment.
gain = F(1120000, 155529)
assert 16 * F(140, 99) / F(1571, 500) == gain
assert gain - B == F(394198, 155529)
dangerous_M = (gain - B) * F(79, 25) - 1
assert dangerous_M == F(27253417, 3888225)
assert dangerous_M - F(132, 175) == F(
    170244091, 27217575
)
safe_M = gain * F(79, 25) - 1
assert safe_M == F(3383671, 155529)
assert safe_M - F(132, 175) == F(
    571612597, 27217575
)

# Exact central endpoint at rho=9/10.
assert F(64) - 18 * F(22, 7) == F(52, 7)
assert 15 * F(22, 7) * F(9, 4) == F(1485, 14)
assert F(107) - F(1485, 14) == F(13, 14)
assert 1 + F(8, 15) * F(99, 70) == F(307, 175)
assert (
    F(1, 107) * 900**2 - 8 * 900 - F(307, 175)
) == F(6897151, 18725)

# Closed global union and exact ceiling reduction.
assert 900**2 - 64 == 809936
assert 900**2 - 9600 == 800400
assert 900**2 - 15000 == 795000
assert 900**2 - 200000 == 610000
assert F(3300**2, 900**2) == F(121, 9)
assert F(121, 9) - 13 == F(4, 9)

print("all exact Round 13 incumbent ledger checks passed")
```

## Final assessment

No candidate implication failed.  The exact endpoint reserves
$23/37800$, $2376966388822/5818105805625$, and
$170244091/27217575$ are all positive after reconstructing their full
inequality chains.  The enlarged local theorem, all exceptional branches,
all required floor and interface walls, the fixed-ratio endpoint, and the
closed global union therefore pass the incumbent gate.
