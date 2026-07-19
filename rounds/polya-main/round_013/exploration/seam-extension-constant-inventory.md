# Round 13 seam-extension constant inventory

## Verdict and isolation statement

**PASS.** There is no failed inequality in the frozen Round 13 constant
chain. In particular, the complete fixed-$r=B$ comparison, including its
no-drop endpoint $P=r=B=14/3$, is strictly positive. The first exact failed
inequality is therefore: **none**.

This reconstruction was made from the corrected frozen packet and its
listed proved inputs. No Round 13 incumbent response, clean-room proof, or
review artifact was inspected. Only after deriving the chain below was it
compared with `computations/round13_verify_seam_extension.py`. The script
reproduces the fractions recorded here and returns `PASS`. This is an exact
constant audit, not a Bessel-root certificate.

Throughout,

$$
y=\sqrt\varepsilon,
\qquad
0<y\le\frac1{\sqrt{10}},
\qquad
\rho=1-y^2\ge\frac9{10},
\qquad
\kappa=Ky^4\ge24.
$$

The rational estimate $\pi<1571/500$ used below follows independently from
Machin's identity

$$
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}
$$

by taking the five-term alternating upper sum for $\arctan(1/5)$ and the
two-term alternating lower sum for $\arctan(1/239)$. The remaining exact
gap to $1571/500$ is

$$
\frac{2736890694763}{6719303882812500}>0.
\tag{A}
$$

In particular, $\pi<1571/500<22/7$.

## 1. The $d$ bound and the displacement bound

Since

$$
\left(\frac9{10}\right)^2-\frac34=\frac3{50}>0,
$$

we have $\rho\ge9/10>\sqrt3/2=\cos(\pi/6)$. Hence

$$
\arccos\rho<\frac\pi6,
\qquad
d=1-\frac{2\arccos\rho}{\pi}>\frac23.
\tag{1}
$$

Assume now that $R=p-dm>0$. Then $p>0$ and

$$
m<\frac pd<\frac32p,
\qquad
n+1=p+m+1<\frac52p+1.
\tag{2}
$$

Because $S=(p+m)y=ny$ and $K=\kappa/y^4$, the definition of $Q$ gives the
exact identity

$$
\widehat q
=\frac{y^2}{\rho}(Q-1)
=\frac{n+1}{\rho K}.
\tag{3}
$$

Combining (2) with the unconditional shelf estimate gives

$$
\widehat q
<\frac1{\rho K}
 +\frac52\sqrt{\frac{2\pi}{\rho K\varepsilon}}.
\tag{4}
$$

On the frozen domain,

$$
\frac1{\rho K}=\frac{y^4}{\rho\kappa}\le\frac1{2160},
\qquad
\frac{2\pi}{\rho K\varepsilon}
=\frac{2\pi y^2}{\rho\kappa}
<\frac{1571/500}{108}.
$$

Moreover,

$$
\left(\frac{171}{1000}\right)^2
-\frac{1571/500}{108}
=\frac{4007}{27000000}>0.
$$

Consequently,

$$
\widehat q
<\frac1{2160}+\frac52\frac{171}{1000}
=\frac{2311}{5400}
=\frac37-\frac{23}{37800}
<\frac37.
\tag{5}
$$

This identifies the advertised displacement reserve exactly.

Since $U=n+\beta<n+1=\rho K\widehat q$, (5) also yields

$$
\frac{x_0}{K}
=\rho-\frac UK
>\rho(1-\widehat q)
>\frac9{10}\frac47
=\frac{18}{35}
=\frac12+\frac1{70}.
\tag{6}
$$

Thus every dangerous plateau is uniformly inside the required localized
region.

## 2. Ordinary floors and self-consistency

On $R>0$ one has $p>0$. By the definition of the first drop, including the
no-drop convention $p=n$, the two ordinary floors at indices $0$ and $p$
are equal. Two real numbers with the same ordinary floor differ by strictly
less than one, even when either number lies on an integer wall. Since $A$ is
strictly decreasing here,

$$
0<A(x_0)-A(x_0+p)<1.
\tag{7}
$$

For $x_0\le z\le x_0+p\le\mu$,

$$
-A'(z)
=\frac1\pi\left(\arccos\frac zK-\arccos\frac z\mu\right).
$$

The integral representation of the arccosine difference gives

$$
\arccos\frac zK-\arccos\frac z\mu
=\int_{z/K}^{z/\mu}\frac{dt}{\sqrt{1-t^2}}.
\tag{8}
$$

The interval in (8) has length

$$
\frac z\mu-\frac zK
=\frac{z}{K}\frac{y^2}{\rho}
>y^2(1-\widehat q),
\tag{9}
$$

because $z/K\ge x_0/K>\rho(1-\widehat q)$. Also

$$
1-\frac{x_0}{K}
=y^2+\frac UK
<y^2+\rho\widehat q
=y^2Q.
$$

Hence, for the lower endpoint $t=z/K$ of (8),

$$
\sqrt{1-t^2}
<y\sqrt{2Q}.
\tag{10}
$$

The integrand in (8) is increasing. Equations (8)--(10), followed by
integration over an interval of length $p$, therefore imply

$$
A(x_0)-A(x_0+p)
>\frac{py(1-\widehat q)}{\pi\sqrt{2Q}}
=\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
$$

Here $Q>1$, $P>0$, and $1-\widehat q>4/7>0$. Combining this strict lower
bound with (7), and squaring only positive quantities, gives

$$
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.
\tag{11}
$$

This derivation remains valid when $x_0+p=\mu$: the endpoint singularity in
(8) is integrable and has measure zero in the subsequent $z$-integration.

## 3. Complete fixed-$r=B$ comparison

Set

$$
B=\frac{14}{3}.
$$

Suppose for contradiction that $r\ge B$. The exact relation among the
scaled variables is

$$
S=P+\frac{P-r}{d}.
\tag{12}
$$

Fix the actual values of $y,\kappa,d$ and, for every $X\in[B,P]$, define the
synthetic fixed-$r=B$ path

$$
S_B(X)=X+\frac{X-B}{d},
$$

$$
Q_B(X)=1+\frac{y^2}{\kappa}+\frac{yS_B(X)}{\kappa},
\qquad
a=\frac{y^2}{\rho},
\qquad
\theta_B(X)=a(Q_B(X)-1),
$$

and

$$
H_B(X)=\frac{2\pi^2Q_B(X)}{(1-\theta_B(X))^2},
\qquad
F_B(X)=X^2-H_B(X).
\tag{13}
$$

At $X=P$, (12) and $r\ge B$ give $S\le S_B(P)$, so the right-hand side of
(11) is at most $H_B(P)$.

The displacement bound controls the *whole* synthetic path, not merely its
endpoint. Indeed, $d>2/3$, $B>0$, and $X\le P=py$ imply

$$
\frac{S_B(X)}y
<\frac52\frac Xy
\le\frac52p.
$$

Using the exact analogue of (3) for the synthetic variables and then (4)--(5),

$$
\theta_B(X)
=\frac{1+S_B(X)/y}{\rho K}
<\frac37
\qquad(B\le X\le P).
\tag{14}
$$

This observation is essential: it prevents an unjustified endpoint-only
comparison.

The rational proxy

$$
\frac1{\sqrt{10}}<\frac8{25},
\qquad
\left(\frac8{25}\right)^2-\frac1{10}=\frac3{1250}>0,
$$

together with (1), gives

$$
Q_B'(X)
=\frac y\kappa\left(1+\frac1d\right)
<\frac1{30}.
\tag{15}
$$

For $D=1-a(Q_B-1)=1-\theta_B$, direct differentiation gives

$$
\frac{dH_B}{dX}
=2\pi^2Q_B'(X)
  \frac{1+2a+\theta_B}{(1-\theta_B)^3}.
\tag{16}
$$

Since $a\le1/9$, (14)--(16), and $\pi<1571/500$ give the uniform exact cap

$$
\frac{dH_B}{dX}
<\frac{1572142117}{270000000}
=6-\frac{47857883}{270000000}
<6.
\tag{17}
$$

It follows throughout the complete path that

$$
F_B'(X)>2X-6\ge2B-6=\frac{10}{3}>0.
\tag{18}
$$

At the path endpoint $X=B$ one has $S_B(B)=B$, including the actual no-drop
configuration $P=r=B$. The endpoint bounds are

$$
Q_B(B)
<1+\frac{1/10}{24}+\frac{(8/25)(14/3)}{24}
=\frac{3839}{3600},
$$

$$
a(Q_B(B)-1)<\frac19\left(\frac{3839}{3600}-1\right)
=\frac{239}{32400}.
$$

The function $2\pi^2Q/(1-a(Q-1))^2$ is increasing in $\pi,Q,$ and $a$ on
this positive domain. Therefore

$$
F_B(B)
>
B^2-
\frac{2(1571/500)^2(3839/3600)}{(1-239/32400)^2}
=\frac{2376966388822}{5818105805625}>0.
\tag{19}
$$

By (18)--(19), $F_B(P)>0$. But (11) and the comparison at $X=P$ require
$F_B(P)<0$, a contradiction. Hence

$$
\boxed{r<\frac{14}{3}},
\qquad
\boxed{R<\frac{14}{3\sqrt\varepsilon}}.
\tag{20}
$$

The comparison includes every $P$ between the endpoint and the actual
plateau; no finite sampling or assumption that the worst case occurs at
$P=B$ has been used.

## 4. Action payment and all discrete branches

From the supplied action identity and
$\arccos(1-v)\ge\sqrt{2v}$,

$$
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
\tag{21}
$$

The exact rational bounds

$$
\frac{140}{99}<\sqrt2<\frac{99}{70},
$$

follow from

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0.
$$

Thus, using $\kappa\ge24$ and (A),

$$
K\eta>\frac gy,
\qquad
g=\frac{2(140/99)24}{3(1571/500)}
=\frac{1120000}{155529},
$$

and

$$
g-B=\frac{394198}{155529}>0.
\tag{22}
$$

Also

$$
\frac1y\ge\sqrt{10}>\frac{79}{25},
\qquad
10-\left(\frac{79}{25}\right)^2=\frac9{625}>0.
\tag{23}
$$

On the dangerous branch $R>0$, (20)--(23) and
$\lfloor t\rfloor>t-1$ give

$$
M=\lfloor K\eta\rfloor-R
>\frac{g-B}{y}-1
>\frac{27253417}{3888225}.
$$

Since $\delta<2\sqrt2/15$,

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
$$

and the exact payment reserve is

$$
\frac{27253417}{3888225}-\frac{132}{175}
=\frac{170244091}{27217575}>0.
\tag{24}
$$

On the safe branch $R\le0$,

$$
M\ge\lfloor K\eta\rfloor
>\frac gy-1,
$$

and the corresponding reserve over $132/175$ is even larger:

$$
\left(\frac{79}{25}g-1\right)-\frac{132}{175}
=\frac{571612597}{27217575}>0.
\tag{25}
$$

Thus $M>4\delta$ on both sign branches. In the pre-threshold estimate this
makes $\delta-M/4<0$.

The discrete cases are all included:

- if $p=0$, then $R=-dm\le0$;
- if $n=0$, then $p=m=R=0$;
- the wall $R=0$ is in the safe branch;
- every first branch with $R>0$ is covered by (20) and (24);
- if $p=n$ and $p>0$, then $m=0$, $r=P$, and the complete path above covers
  it, including $P=r=B$;
- if $q=\mu$ then $\delta=0$, which only strengthens the payment;
- $\lfloor K\eta\rfloor>K\eta-1$ remains strict even when $K\eta$ is an
  integer.

The ordinary-floor wall was handled in (7), and $U=n+\beta<n+1$ remains
strict for both $\beta=0$ and values arbitrarily close to $1$. All estimates
use $\kappa\ge24$ and $\varepsilon\le1/10$ with their equality faces
included. Hence the finite constant chain proves the frozen local seam
claim through the permitted shifted-tail scaffold.

## 5. Exact central endpoint

At $\rho=9/10$,

$$
a_{9/10}=18\pi<18\frac{22}{7}=\frac{396}{7}<8^2,
\qquad
8^2-\frac{396}{7}=\frac{52}{7}>0.
\tag{26}
$$

The action bound gives

$$
\eta_{9/10}\ge\frac1{15\pi\sqrt5}>\frac1{107},
$$

because

$$
\sqrt5<\frac94,
\qquad
107-15\frac{22}{7}\frac94=\frac{13}{14}>0.
\tag{27}
$$

Also

$$
C_0=1+\frac{8\sqrt2}{15}<1+\frac8{15}\frac{99}{70}
=\frac{307}{175}.
\tag{28}
$$

Let $f(X)=\eta_{9/10}X^2-\sqrt{a_{9/10}}X-C_0$. At $X=900$,

$$
f(900)
>\frac{900^2}{107}-8\cdot900-\frac{307}{175}
=\frac{6897151}{18725}>0.
\tag{29}
$$

The quadratic $f$ has one negative root and one positive root, because its
leading coefficient is positive and $f(0)=-C_0<0$. Positivity at the
positive number $900$ therefore places its unique positive root below
$900$. Formula (13) in the packet is the square of that root, so

$$
\boxed{K_0(9/10)<900^2=810000}.
\tag{30}
$$

## 6. Five finite residual zones and the closed union

The five finite residual zones are now exactly as follows.

| Closed ratio zone | Input | Possible residual satisfies |
| --- | --- | ---: |
| $[\rho_*,1/16]$ | proved low-ratio result | $K<64$ |
| $[1/16,9/10]$ | central monotonicity and (30) | $K<K_0(9/10)<900^2$ |
| $[9/10,19/20]$ | new constant-$24$ seam | $K<9600$ |
| $[19/20,24/25]$ | Round 12 constant-$24$ seam | $K<15000$ |
| $[24/25,99/100]$ | Round 10 constant-$20$ seam | $K<200000$ |

The three seam ceilings are exact:

$$
\frac{24}{(1/20)^2}=9600,
\qquad
\frac{24}{(1/25)^2}=15000,
\qquad
\frac{20}{(1/100)^2}=200000.
\tag{31}
$$

Moreover,

$$
64<9600<15000<200000<810000.
\tag{32}
$$

The already-proved small-hole endpoint owns ratios below $\rho_*$, and the
already-proved all-frequency endpoint owns $[99/100,1)$. The shared faces
$\rho_*,1/16,9/10,19/20,24/25,$ and $99/100$ are each owned by both adjacent
closed regimes. Threshold equality is also owned: the seam theorems include
$\kappa=20$ or $24$, the central theorem includes $K=K_0(\rho)$, and
$K=900^2$ is strictly above every finite ceiling in (32), including
$K_0(9/10)$.

It follows that

$$
\boxed{0<\rho<1,\qquad K\ge900^2}
$$

is covered. The exact reduction from the Round 12 ceiling is

$$
\frac{3300^2}{900^2}=\frac{121}{9}>13.
$$

This does not enlarge the complete all-frequency endpoint beyond
$[99/100,1)$ and does not close the compact residual below $900^2$.
