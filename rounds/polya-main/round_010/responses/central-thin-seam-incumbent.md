# Round 10 incumbent: exact central--thin seam compression

## Result

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{25}.
$$

Then

$$
\boxed{
K\ge\frac{20}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

Threshold equality is included.  Combining (1) with the sharper Round 9
constant $125/8$ on $\varepsilon\le1/100$ moves the central--thin seam from
$\rho=99/100$ to

$$
\boxed{\rho_s=\frac{24}{25}.}
$$

At that seam the existing fixed-ratio threshold obeys

$$
K_0(24/25)<6000^2<\frac{125^5}{8}.
$$

Consequently the shell Pólya inequality holds for every $0<\rho<1$ when

$$
\boxed{K\ge\frac{125^5}{8}<2^{32}.}
\tag{2}
$$

The previous uniform ceiling was $2^{35}$, so (2) lowers it by more than a
factor of nine.  It does not close the compact all-frequency residual.

## 1. Frozen shifted-tail input

Put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
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

and let $p$ be the length of the initial constant ordinary-floor plateau.
Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta.
$$

The audited Round 3 decomposition gives

$$
\frac{\mathcal T_{r_0}}2
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\tag{3}
$$

where

$$
0\le\delta<\frac{2\sqrt2}{15},
\qquad
M=L+dm-p,
\qquad
L=\lfloor K\eta\rfloor.
\tag{4}
$$

The same pre-threshold input supplies the unconditional shelf estimate

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{5}
$$

For $n=0$ the prescribed convention is $p=m=0$.  Define the actual
uncompensated loss

$$
R=p-dm.
\tag{6}
$$

Then $M=L-R$.  Only the branch $R>0$ requires a plateau estimate.

## 2. Scaled variables

Set

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4.
\tag{7}
$$

Under the hypothesis of (1),

$$
0<y\le\frac15,
\qquad
\rho=1-y^2\ge\frac{24}{25},
\qquad
\kappa\ge20.
\tag{8}
$$

In the dangerous branch $R>0$, put

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{9}
$$

Every estimate below is rederived under (8); no Round 9 inequality whose
domain ended at $y=1/10$ is extrapolated.

The elementary constants used below are certified without decimals.  The
alternating arctangent series in Machin's identity gives

$$
\pi
<\frac{5277328977275528}{1679825970703125}
<\frac{1571}{500}.
$$

The last margin is

$$
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=\frac{2736890694763}{6719303882812500}>0.
$$

The radical bounds used later follow from

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0,
$$

and

$$
\left(\frac94\right)^2-5=\frac1{16}>0.
$$

## 3. The enlarged-domain bound for $d$

The exact half-angle identity

$$
\cos^2\frac\pi{10}=\frac{5+\sqrt5}{8}
$$

and $\sqrt5<9/4$ give

$$
\cos^2\frac\pi{10}<\frac{29}{32}
<\left(\frac{24}{25}\right)^2,
$$

where the last exact margin is

$$
\left(\frac{24}{25}\right)^2-\frac{29}{32}
=\frac{307}{20000}>0.
$$

All quantities are positive, so

$$
\cos\frac\pi{10}<\frac{24}{25}\le\rho,
\qquad
\arccos\rho<\frac\pi{10}.
$$

Consequently

$$
\boxed{d>\frac45.}
\tag{10}
$$

If $R>0$, then $p>0$ and

$$
m<\frac p d<\frac54p,
\qquad
S<\frac94P,
\qquad
U<1+p+m.
\tag{11}
$$

This includes the no-drop branch $p=n$, where $m=0$.

## 4. Dangerous-plateau location

Define

$$
t=\frac{x_0}{\rho K},
\qquad
w=1-t=\frac U{\rho K}.
$$

Using (7), (9), and (11),

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{12}
$$

The shelf estimate (5) becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Therefore

$$
\widehat q
<
\frac{y^4}{\kappa\rho}
+\frac94y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{13}
$$

At the simultaneous worst endpoint in (8), the first term is at most
$1/12000$.  Moreover, using $\pi<1571/500$,

$$
y\sqrt{\frac{2\pi}{\kappa\rho}}
=\sqrt{\frac{2\pi y^2}{\kappa\rho}}
\le\sqrt{\frac{1571}{120000}}
<\frac{23}{200},
$$

because $(23/200)^2-1571/120000=1/7500$.

Consequently

$$
\widehat q
<\frac1{12000}+\frac{207}{800}
=\frac{1553}{6000}
<\frac{21}{80},
\tag{14}
$$

where the last exact margin is

$$
\frac{21}{80}-\frac{1553}{6000}
=\frac{11}{3000}>0.
$$

It follows that

$$
t>\frac{59}{80},
\qquad
\frac{x_0}{K}=\rho t
>\frac{24}{25}\frac{59}{80}
=\frac{177}{250}>\frac12.
\tag{15}
$$

Thus every localization used below is proved on the enlarged interval.

## 5. Exact local slope and self-consistency inequality

For $0<z<\mu$ define

$$
\sigma(z)=-A'(z)
=\frac1\pi
\left(
\arccos\frac zK-
\arccos\frac z\mu
\right).
$$

The function $\sigma$ is increasing.  At $x_0=\mu t$,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{16}
$$

Also

$$
1-\rho t=\varepsilon+\frac UK,
\qquad
1-\rho^2t^2\le2\left(\varepsilon+\frac UK\right).
$$

Put

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa}.
\tag{17}
$$

Then

$$
\widehat q=\frac{y^2}{\rho}(Q-1),
\qquad
\varepsilon+\frac UK<y^2Q.
\tag{18}
$$

The values at $x_0$ and $x_0+p$ have the same ordinary floor.  Hence, even
if one sampled value lies on an integer wall,

$$
A(x_0)-A(x_0+p)<1.
$$

Using monotonicity of $\sigma$,

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
$$

Equations (12), (16), and (18), followed only by squaring positive
quantities, give

$$
\boxed{
P^2<H(P,r)
:=\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{19}
$$

## 6. Scaled loss bound

From $R=p-dm$,

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{20}
$$

For fixed $y$, $\kappa$, and $d$, the function $H$ is decreasing in $r$.
Let $a=y^2/\rho$.  Its $P$ derivative is

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q}{\partial P}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
\tag{21}
$$

By (8), (10), and (14),

$$
\frac{\partial Q}{\partial P}
=\frac y\kappa\left(1+\frac1d\right)
<\frac9{400},
\qquad
a\le\frac1{24}.
$$

Thus

$$
\frac{\partial H}{\partial P}
<
2\left(\frac{1571}{500}\right)^2
\frac9{400}
\frac{1+21/80+2/24}{(1-21/80)^3}
=\frac{4783063458}{3209046875}
<\frac32.
\tag{22}
$$

Set

$$
B=\frac{73}{16}.
$$

Suppose that $r\ge B$.  Then $P\ge r\ge B$.  Since $H$ decreases in $r$,

$$
P^2-H(P,r)\ge P^2-H(P,B).
$$

Every $P'\in[B,P]$ retains the original shelf ceiling because $P'\le P$,
and (20) gives $S(P',B)<9P'/4$.  Hence (14) and (22) hold on the complete
synthetic comparison path.  Because

$$
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2B-\frac32>0,
$$

we obtain

$$
P^2-H(P,r)\ge B^2-H(B,B).
\tag{23}
$$

At $P=r=B$, equation (20) gives $S=B$ exactly.  Both $Q$ and
$\widehat q$ are largest at $y=1/5$ and $\kappa=20$, where

$$
Q_*=\frac{8381}{8000},
\qquad
\widehat q_*=\frac{127}{64000}.
$$

The endpoint margin is exact:

$$
B^2
-2\left(\frac{1571}{500}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=\frac{6451558662413}{130552324128000}>0.
\tag{24}
$$

This contradicts (19).  Therefore

$$
\boxed{
R<\frac{73}{16\sqrt\varepsilon}.
}
\tag{25}
$$

The no-drop branch $p=n>0$ has $m=0$, so $P=r$ and supplies exactly the
endpoint geometry tested in (24).

## 7. Action gain and every exceptional branch

The exact action formula and
$\arccos(1-v)\ge\sqrt{2v}$ give

$$
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
$$

Using

$$
\sqrt2>\frac{140}{99},
\qquad
\pi<\frac{1571}{500},
$$

we obtain, for $\kappa\ge20$,

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
>\frac{2800000}{466587y}.
\tag{26}
$$

In the dangerous branch, (25), (26), and
$\lfloor x\rfloor>x-1$ imply

$$
M=L-R
>
\left(\frac{2800000}{466587}-\frac{73}{16}\right)\frac1y-1
\ge\frac{46230353}{7465392}.
\tag{27}
$$

Meanwhile

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
$$

and

$$
\frac{46230353}{7465392}-\frac{132}{175}
=\frac{7104880031}{1306443600}>0.
\tag{28}
$$

Thus $M>4\delta$.

If $R\le0$, then

$$
M\ge L>K\eta-1
>\frac{5\cdot2800000}{466587}-1
=\frac{13533413}{466587}>1>4\delta.
$$

This directly covers the immediate-drop branch $p=0$ and the degenerate
head $n=0$.  The branch $R=0$ belongs here.  At an interface wall one has
$\delta=0$.  At a gain wall $L=K\eta$, while the strict universal bound
$L>K\eta-1$ remains valid.  The ordinary-floor inequality used in (19) is
strict at integer walls, and threshold equality $\kappa=20$ is included in
every non-strict parameter bound.  The final spectral transfer is the
already-audited strict phase proxy, so no strict eigenvalue wall is changed.

Substitution in (3) proves every low-interface shifted tail.  The permitted
high-interface theorem and multiplicity scaffold complete the proof of
(1).

## 8. Exact central endpoint

The fixed-ratio threshold $K_0(\rho)$ is increasing.  At
$\rho_s=24/25$,

$$
a_{\rho_s}=48\pi<\frac{1056}{7}<13^2.
\tag{29}
$$

Also

$$
\eta_{\rho_s}
\ge\frac{2\sqrt2}{375\pi}
>\frac{1120}{466587}
>\frac1{420},
\tag{30}
$$

where

$$
\frac{1120}{466587}-\frac1{420}
=\frac{1271}{65322180}>0.
$$

Finally $C_0=1+8\sqrt2/15<307/175$.  Let $Y=6000$.  The positive square root
of $K_0(\rho_s)$ is the unique positive root of

$$
F(y)=\eta_{\rho_s}y^2-\sqrt{a_{\rho_s}}y-C_0.
$$

Equations (29)--(30) give

$$
F(Y)
>
\frac{Y^2}{420}-13Y-\frac{307}{175}
=\frac{1349693}{175}>0.
$$

Since $F(0)<0$, its positive root lies below $Y$.  Hence

$$
\boxed{
K_0(24/25)<6000^2=36000000.
}
\tag{31}
$$

Moreover,

$$
\frac{125^5}{8}-6000^2
=\frac{30229578125}{8}>0.
\tag{32}
$$

## 9. Closed analytic union and new global ceiling

Use the following closed zones.

1. On $(0,\rho_*]$, `SHELL-rho-zero-endpoint` proves every $K\ge0$.
2. On $[\rho_*,1/16]$, the permitted high-angular theorem covers
   $K\le1/(2\rho)$ and `SHELL-low-interface-small-hole` covers
   $K\ge H_0(\rho)$.  The already-proved monotonicity and endpoint
   comparison $H_0(1/16)<64$ put every possible residual below $64$.
3. On $[1/16,24/25]$, monotonicity and (31) put the fixed-ratio threshold
   below $6000^2$.
4. On $[24/25,99/100]$, equivalently
   $1/100\le\varepsilon\le1/25$, theorem (1) starts at

   $$
   K=\frac{20}{\varepsilon^2}\le200000.
   $$

5. On $[99/100,1-1/15625]$, retain the sharper Round 9 threshold

   $$
   K=\frac{125}{8\varepsilon^2}
   \le\frac{125^5}{8}.
   $$

6. On $[1-1/15625,1)$, `SHELL-rho-one-endpoint` proves every $K\ge0$.

The faces $\rho=24/25$ and $\rho=99/100$ belong to both adjacent closed
zones.  The face $\rho=1-1/15625$ is owned by the complete endpoint theorem
and both low/high thin thresholds agree there.  All component high-frequency
theorems include equality, so no face or strict-count convention is lost.

The exact comparisons

$$
6000^2<\frac{125^5}{8},
\qquad
200000<\frac{125^5}{8},
$$

show that the thin Round 9 ceiling now dominates.  Therefore

$$
\boxed{
0<\rho<1,
\quad
K\ge\frac{125^5}{8}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Finally,

$$
2^{32}-\frac{125^5}{8}
=\frac{3842160243}{8}>0,
$$

and

$$
2^{35}-9\frac{125^5}{8}
=\frac{219703819}{8}>0.
$$

Thus the new ceiling is less than $2^{32}$ and is more than nine times
smaller than the previous $2^{35}$ ceiling.

## 10. Quantified residual reduction and scope

The moved seam removes the complete radius strip

$$
\frac{24}{25}\le\rho\le\frac{99}{100},
\qquad
\frac{99}{100}-\frac{24}{25}=\frac3{100},
$$

above the explicit curve $K=20/(1-\rho)^2$ from the central residual plan.
Globally, every still-unresolved point now has

$$
K<\frac{125^5}{8}
$$

instead of merely $K<2^{35}$.  The exact removed vertical height is

$$
2^{35}-\frac{125^5}{8}
=\frac{244360328819}{8}.
$$

These are analytic reductions only.  The compact residual below the new
ceiling still requires additional analytic closure or an exact
face-connected certificate, followed by theorem-level independent review.

All rational identities and margins in this proof are checked by
`computations/round10_verify_seam_constants.py`.
