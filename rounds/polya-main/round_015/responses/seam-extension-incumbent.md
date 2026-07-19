# Round 15 incumbent: central--thin seam at $\rho=5/6$

## Verdict and input integrity

**PASS.**  I used the frozen packet
`state/lemma_packets/SHELL-central-thin-seam-compression-round15.md` and
verified its SHA-256 digest to be

```
c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7
```

before beginning the reconstruction.  No Round 15 clean-room,
exploration, adversarial, or judge artifact was inspected.

Both frozen targets close with strict exact reserves.  If

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac16,
$$

then, including threshold equality,

$$
\boxed{
K\ge\frac{54}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

This is a fresh derivation on the whole displayed domain.  Its genuinely
new open-sided slab is $1/8<\varepsilon\le1/6$; on overlaps the accepted
constants $20$, $24$, and $32$ remain sharper on their stated domains.
Independently,

$$
\boxed{K_0(5/6)<295^2=87025.}
\tag{2}
$$

Only after proving both (1) and (2), the seven-zone union gives

$$
\boxed{0<\rho<1,\qquad K\ge200000.}
\tag{3}
$$

This is an all-ratio high-frequency theorem, not the full all-frequency
shell theorem.  The complete endpoint remains exactly
$99/100\le\rho<1$.

## 1. Low-interface reduction and exact domain

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

For a low-interface shifted tail beginning at
$x_0=r_0+1/2<\mu$, use the packet's definitions

$$
n=\lfloor\mu-x_0\rfloor,
\quad
q=x_0+n,
\quad
\beta=\mu-q\in[0,1),
$$

$$
h_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor,
$$

and let $p$ be the last index of the initial plateau, with $p=n$ in the
no-drop branch.  Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{4}
$$

For $n=0$ use $p=m=R=0$.  The permitted audited decomposition is

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

and

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{7}
$$

It is therefore enough to prove $M>4\delta$.  Only $R>0$ requires a new
plateau-loss cap.

Scale by

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4,
\qquad
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{8}
$$

The complete target domain, with all equality faces retained, is

$$
0<y\le\frac1{\sqrt6},
\qquad
\rho=1-y^2\ge\frac56,
\qquad
\kappa\ge54.
\tag{9}
$$

## 2. Fresh rational and radical bounds

Machin's identity, established by the tangent addition formula, and the
alternating arctangent series give the strict upper bound

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
\tag{10}
$$

The exact last two margins are

$$
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=\frac{2736890694763}{6719303882812500}>0,
\qquad
\frac{22}{7}-\frac{1571}{500}=\frac3{3500}>0.
$$

The lower alternating truncation needed only for the route obstruction in
Section 11 is

$$
\pi>
16\left(
\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}
-\frac1{7\cdot5^7}
\right)-\frac4{239}
=\frac{1231847548}{392109375}
>\frac{333}{106},
\tag{11}
$$

with final margin $3418213/41563593750$.

Positive squaring yields

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

It also gives

$$
\sqrt3<\frac{97}{56},
\qquad
\left(\frac{97}{56}\right)^2-3=\frac1{3136}>0.
\tag{13}
$$

The endpoint proxy for $y$ is strict even when $y=1/\sqrt6$:

$$
y<\frac{49}{120},
\qquad
\left(\frac{49}{120}\right)^2-\frac16
=\frac1{14400}>0,
\qquad
\frac1y>\frac{120}{49}.
\tag{14}
$$

Finally, from (10),

$$
2\pi\rho<2\pi<\frac{1571}{250}<\frac{169}{25},
\qquad
\frac{169}{25}-\frac{1571}{250}=\frac{119}{250}>0,
$$

so the permitted shelf estimate also has the reconstructed form

$$
p<\frac{13}{5}\sqrt{\frac K\varepsilon}.
\tag{15}
$$

## 3. Angular factor and dangerous-branch geometry

First,

$$
2-\left(\frac75\right)^2=\frac1{25}>0,
$$

so $\sqrt2>7/5$ and hence $2-\sqrt2<3/5$.  Also

$$
\left(\frac79\right)^2-\frac35=\frac2{405}>0.
$$

Thus

$$
\cos\frac{3\pi}{8}
=\frac12\sqrt{2-\sqrt2}<\frac7{18},
$$

and the half-angle identity gives

$$
\cos^2\frac{3\pi}{16}
=\frac{1+\cos(3\pi/8)}2
<\frac{1+7/18}{2}=\frac{25}{36}.
$$

All terms are positive, so

$$
\cos\frac{3\pi}{16}<\frac56\le\rho.
$$

Since arccos is strictly decreasing,

$$
\arccos\rho<\frac{3\pi}{16},
\qquad
\boxed{d>\frac58.}
\tag{16}
$$

This remains strict at $\rho=5/6$.

Suppose now that $R>0$.  Then $p>0$, and (4) gives

$$
p>dm,
\qquad
m<\frac pd<\frac85p,
\qquad
S<\frac{13}{5}P.
\tag{17}
$$

The last inequality includes the no-drop case $m=0$, where $S=P$.

## 4. Dangerous localization before any outer slope

Define

$$
t=\frac{x_0}{\rho K},
\qquad
w=1-t=\frac{U}{\rho K}.
$$

Since $U=p+m+\beta<1+p+m$ for every $0\le\beta<1$, including
$\beta=0$,

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{18}
$$

The shelf estimate (7) becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Using (17),

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac{13}{5}y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{19}
$$

For fixed $\kappa$, both $y^4/(1-y^2)$ and
$y/\sqrt{1-y^2}$ increase for $y>0$; both terms decrease with
$\kappa$.  Thus their closed proxy maxima occur at
$y^2=1/6$, $\rho=5/6$, and $\kappa=54$.  At that point

$$
\frac{y^4}{\kappa\rho}\le\frac1{1620},
\qquad
y\sqrt{\frac{2\pi}{\kappa\rho}}
\le\sqrt{\frac\pi{135}}<\frac{763}{5000}.
\tag{20}
$$

The last strict inequality follows from (10) by positive squaring, with

$$
\left(\frac{763}{5000}\right)^2
-\frac{1571}{67500}
=\frac{8563}{675000000}>0.
\tag{21}
$$

Consequently

$$
\widehat q
<\frac1{1620}+\frac{13}{5}\frac{763}{5000}
=\frac{804689}{2025000}
<\frac{159}{400},
\tag{22}
$$

and the exact displacement reserve is

$$
\frac{159}{400}-\frac{804689}{2025000}
=\frac{497}{4050000}>0.
\tag{23}
$$

Thus $1-\widehat q>241/400>0$, and, before any outer-region slope is
used,

$$
\boxed{
\frac{x_0}{K}=\rho t
>\frac56\left(1-\frac{159}{400}\right)
=\frac{241}{480}
=\frac12+\frac1{480}.
}
\tag{24}
$$

## 5. Ordinary-floor implication and actual self-consistency

For $0<z<\mu$, direct differentiation of $G_a$ gives

$$
\sigma(z):=-A'(z)
=\frac1\pi\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
$$

Moreover,

$$
\sigma'(z)
=\frac1\pi\left(
\frac1{\sqrt{\mu^2-z^2}}
-\frac1{\sqrt{K^2-z^2}}
\right)>0.
$$

At $x_0=\mu t$ this yields

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{25}
$$

Define the actual quantities

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho},
\qquad
\widehat q=a(Q-1).
\tag{26}
$$

On (9), $Q>1$ and

$$
0<a\le\frac{1/6}{5/6}=\frac15,
\qquad
0\le\widehat q<\frac{159}{400}<1.
\tag{27}
$$

Also

$$
1-\rho t
=\varepsilon+\frac UK
<y^2+\frac{y^4+y^3S}{\kappa}
=y^2Q.
$$

Because $0<\rho t<1$, every radicand is positive and

$$
1-\rho^2t^2
=(1-\rho t)(1+\rho t)
<2y^2Q.
\tag{28}
$$

In the dangerous branch $p>0$.  The plateau definition, including the
no-drop branch, gives

$$
\left\lfloor A(x_0)+\frac14\right\rfloor
=
\left\lfloor A(x_0+p)+\frac14\right\rfloor.
$$

Two real numbers with the same ordinary floor differ by strictly less
than one, including when either one lies on an integer wall.  Since $A$
is decreasing,

$$
A(x_0)-A(x_0+p)<1.
\tag{29}
$$

Equations (25), (28), and monotonicity of $\sigma$ give

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0)
>\frac{Pt}{\pi\sqrt{2Q}}.
$$

All quantities being squared are positive.  Since
$t>1-\widehat q>0$, squaring preserves direction and gives the actual
self-consistency inequality

$$
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.
\tag{30}
$$

No denominator, radicand, or squaring wall is crossed.

## 6. Actual-to-synthetic comparison

From (4) and (8),

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d},
\qquad
0<r\le P.
\tag{31}
$$

By (16),

$$
S\le P+\frac85(P-r)
=S_*(P,r)=\frac{13P-8r}{5}.
\tag{32}
$$

Equality in (32) can occur only in the harmless $m=0$ case
$P=r$, because $d>5/8$.  Define

$$
Q_*=1+\frac{y^2}{\kappa}+\frac{yS_*}{\kappa},
\qquad
q_*=a(Q_*-1).
$$

Since $r>0$, $S_*<13P/5$.  Repeating (19)--(23) with $S_*$ gives,
uniformly at the actual point,

$$
0\le\widehat q\le q_*<\frac{159}{400}<1,
\qquad
Q\le Q_*.
\tag{33}
$$

For fixed $a\ge0$, the function

$$
F(Q)=\frac{2\pi^2Q}{(1-a(Q-1))^2}
$$

has, wherever $a(Q-1)<1$,

$$
F'(Q)=2\pi^2
\frac{1+a(Q-1)+2a}{(1-a(Q-1))^3}>0.
\tag{34}
$$

Therefore (30)--(34) establish the required actual-to-synthetic
implication

$$
\boxed{
P^2<H(P,r):=
\frac{2\pi^2Q_*(P,r)}{(1-q_*(P,r))^2}.
}
\tag{35}
$$

## 7. The complete fixed-$r=B$ path

Let

$$
B=\frac{14}{3}.
$$

Suppose for contradiction that $r\ge B$.  Then $P\ge r\ge B$.
Because $Q_*$ decreases with $r$ and $F$ in (34) increases with $Q$,

$$
H(P,r)\le H(P,B).
\tag{36}
$$

For every point $P'\in[B,P]$, freeze $r=B$.  Since $P'\le P$, the
original shelf ceiling remains valid.  Also

$$
S_*(P',B)=\frac{13P'-8B}{5}<\frac{13}{5}P',
$$

so (33), $a\le1/5$, and all positive denominator bounds hold at every
point of the path, not merely its endpoints.  Along this entire path,

$$
\frac{\partial Q_*}{\partial P'}
=\frac{13y}{5\kappa}
<\frac{13}{5\cdot54}\frac{49}{120}
=\frac{637}{32400}.
\tag{37}
$$

Differentiating $H$ and using (10), (27), (33), and (37) gives uniformly

$$
\begin{aligned}
\frac{\partial H}{\partial P'}
&=2\pi^2\frac{\partial Q_*}{\partial P'}
\frac{1+q_*+2a}{(1-q_*)^3}\\
&<2\left(\frac{1571}{500}\right)^2
\frac{637}{32400}
\frac{1+159/400+2/5}{(1-159/400)^3}\\
&=\frac{2260740364246}{708624500625}
<\frac{16}{5}.
\end{aligned}
\tag{38}
$$

The exact derivative reserve is

$$
\frac{16}{5}
-\frac{2260740364246}{708624500625}
=\frac{6858037754}{708624500625}>0.
\tag{39}
$$

Hence, everywhere on the path,

$$
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2B-\frac{16}{5}
=\frac{92}{15}>0.
\tag{40}
$$

At the initial endpoint $P'=r=B$, one has $S_*=B$.  From (9) and
(14),

$$
Q_*(B,B)
<1+\frac1{6\cdot54}
+\frac{(49/120)(14/3)}{54}
=\frac{10093}{9720},
$$

and

$$
q_*(B,B)
<\frac15\left(\frac{10093}{9720}-1\right)
=\frac{373}{48600}.
$$

Thus the initial endpoint has the strict exact reserve

$$
\begin{aligned}
B^2-H(B,B)
&>
B^2-2\left(\frac{1571}{500}\right)^2
\frac{10093/9720}{(1-373/48600)^2}\\
&=\frac{2505132463469}{2616573970125}>0.
\end{aligned}
\tag{41}
$$

Equations (36), (40), and (41) contradict (35).  The proof controls every
intermediate point of the path and therefore yields

$$
\boxed{R<\frac{14}{3\sqrt\varepsilon}.}
\tag{42}
$$

## 8. Action gain, full floor loss, and every plateau branch

For $0\le v\le1$, put $x=\arccos(1-v)\ge0$.  The elementary inequality
$\cos x\ge1-x^2/2$ gives

$$
\arccos(1-v)\ge\sqrt{2v}.
$$

Using the exact action identity,

$$
\eta
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{43}
$$

On (9), (10), and (12) imply

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
\ge\frac{36\sqrt2}{\pi y}
>\frac{280000}{17281}\frac1y.
\tag{44}
$$

The gain above $B$ is

$$
\frac{280000}{17281}-\frac{14}{3}
=\frac{598066}{51843}>0.
\tag{45}
$$

If $R>0$, the universally strict floor inequality
$\lfloor x\rfloor>x-1$, valid also when $x$ is an integer, together
with (14), (42), and (44), gives

$$
M
=\lfloor K\eta\rfloor-R
>\left(\frac{280000}{17281}-B\right)\frac1y-1
>\frac{3296553}{120967}.
\tag{46}
$$

From (6) and (12),

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175}.
$$

The dangerous-branch payment reserve is therefore

$$
\boxed{
M-4\delta>
\left(\frac{598066}{51843}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{80132733}{3024175}>0.
}
\tag{47}
$$

If $R\le0$, no localization or plateau cap is needed.  Here
$M\ge\lfloor K\eta\rfloor$, whence

$$
\boxed{
M-4\delta>
\frac{280000}{17281}\frac{120}{49}
-1-\frac{132}{175}
=\frac{114694733}{3024175}>0.
}
\tag{48}
$$

These two cases own all exceptional branches:

* if $p=n>0$, then $m=0$ and $R=p>0$, so the complete dangerous path,
  including its $P=r$ endpoint, applies;
* if $p=0<n$, then $R=-dn<0$, so the immediate-drop branch is safe;
* if $n=0$, then $p=m=R=0$, so the degenerate head is safe;
* the wall $R=0$ belongs to the safe branch from either side;
* the first discrete branch with $R>0$ is covered without a positive
  lower bound on $R$.

Substitution of (47)--(48) into (5) gives

$$
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^K A(z)\,dz
$$

for every low-interface shifted tail.  The permitted high-interface
shifted-tail result, high-angular result, strict-to-ordinary-floor
transfer, exact spectrum, and weighted multiplicity scaffold now give
(1).

## 9. Discrete, interface, spectral, and threshold walls

The proof above owns the complete domain, not only generic cells.

1. If $\mu-x_0\in\mathbb Z$, then $\beta=0$ and
   $U=p+m<1+p+m$.  In both adjacent cells $0\le\beta<1$, so the same
   strict estimate holds as $\beta\to1^-$.  No estimate freezes $n$
   across the wall.
2. At $q=\mu$, one has $\beta=0$ and $\delta=0$.  At $x_0=\mu$, the
   permitted high-interface theorem owns equality; the $n=0$ low-side
   limit is already safe.
3. At every ordinary-floor wall, equal ordinary floors still imply the
   strict difference (29).  A change in $p$ at a neighboring floor or
   coarse-proxy wall only selects one of the already-covered branches.
4. At $K\eta\in\mathbb Z$, $\lfloor K\eta\rfloor>K\eta-1$ remains
   strict.  Equations (46)--(48) pay the entire possible unit loss.
5. Before division or squaring, (22), (27), and (33) place every
   denominator strictly above zero; $0<\rho t<1$ places every radicand
   above zero.  The rational proxy and gain walls have the positive
   reserves (23), (39), (41), (45), and (47).
6. The proof assumes $\kappa\ge54$, not $\kappa>54$.  Hence
   $K=54/\varepsilon^2$ is included throughout (9), including
   $(\varepsilon,K)=(1/6,1944)$ and
   $(1/8,3456)$.  Strictness comes from the displayed angular, radical,
   localization, endpoint, derivative, gain, floor, and payment
   reserves.
7. The strict spectral convention and the angular cutoff $\nu=K$ are
   exactly those of the permitted phase, high-angular, and shifted-tail
   inputs.  No strict spectral bracket is silently replaced by an
   unshifted ordinary floor.

The requested epsilon faces are explicit.  At $\varepsilon=1/100$ the
complete endpoint owns all $K$; at $1/25$ the accepted $\kappa=20$
theorem is sharpest; at $1/20$ and $1/10$ the accepted $\kappa=24$
theorem is sharpest; at $1/8$ the accepted $\kappa=32$ theorem is
sharpest; and at $1/6$ the new $\kappa=54$ theorem includes equality.
The values $\kappa=20,24,32$ are used only on their accepted domains;
(1) independently covers every one of these epsilon faces when
$\kappa\ge54$.

## 10. Independent proof that $K_0(5/6)<295^2$

This section uses neither (1) nor any plateau estimate.  At $\rho=5/6$,

$$
a_{5/6}=10\pi.
$$

By (10),

$$
10\pi<\frac{220}{7}<36,
\qquad
36-\frac{220}{7}=\frac{32}{7}>0,
$$

and therefore

$$
\sqrt{a_{5/6}}<6.
\tag{49}
$$

At $\varepsilon=1/6$, the action estimate (43) simplifies exactly to

$$
\eta_{5/6}\ge\frac1{9\pi\sqrt3}.
$$

Equations (10) and (13) give

$$
49-9\left(\frac{1571}{500}\right)
\left(\frac{97}{56}\right)
=\frac{517}{28000}>0.
$$

Hence $9\pi\sqrt3<49$ and

$$
\eta_{5/6}>\frac1{49}.
\tag{50}
$$

Furthermore, (12) gives

$$
C_0=1+\frac{8\sqrt2}{15}
<1+\frac8{15}\frac{99}{70}
=\frac{307}{175}.
\tag{51}
$$

At $Y=295$, (49)--(51) yield

$$
\begin{aligned}
\eta_{5/6}Y^2-\sqrt{a_{5/6}}Y-C_0
&>\frac1{49}295^2-6\cdot295-\frac{307}{175}\\
&=\frac{5226}{1225}>0.
\end{aligned}
\tag{52}
$$

The number $X=\sqrt{K_0(5/6)}$ in the permitted formula is the positive
root of

$$
\eta_{5/6}X^2-\sqrt{a_{5/6}}X-C_0=0.
$$

Its leading coefficient is positive and its constant term is negative,
so its two roots have opposite signs and the positive root is unique.
Equation (52) places that root strictly below $295$, proving (2).  The
fixed-ratio theorem itself includes $K=K_0(5/6)$.

## 11. Exact route obstructions are not counterexamples

The selected displacement majorant does not certify $\kappa=53$.  From
the independently derived lower bound (11),

$$
\frac{2\pi}{265}>\frac{333}{14045}.
$$

Positive squaring gives

$$
\frac{333}{14045}
-\left(\frac{3079}{20000}\right)^2
=\frac{10003031}{1123600000000}>0,
$$

so

$$
\sqrt{\frac{2\pi}{265}}>\frac{3079}{20000}.
$$

At the selected endpoint proxy,

$$
\frac1{1590}+\frac{13}{5}\frac{3079}{20000}
=\frac25+\frac{14293}{15900000}>\frac25.
\tag{53}
$$

Thus this particular coarse majorant cannot deliver the
$\widehat q<2/5$ localization needed beyond $K/2$ when $\kappa=53$.
It says nothing about the truth of a theorem with constant $53$ and is
not a spectral counterexample.

Likewise, the selected central proxies give

$$
\frac1{49}294^2-6\cdot294-\frac{307}{175}
=-\frac{307}{175}<0.
\tag{54}
$$

This only says that these proxies do not certify $Y=294$; it does not
prove $K_0(5/6)\ge294^2$.

## 12. Closed seven-zone union and every shared face

Only now that (1) and (2) are independently proved, assemble the accepted
global inputs.

1. On $[\rho_*,1/16]$, every possible residual has $K<64$.
2. On $[1/16,5/6]$, monotonicity of $K_0$ and (2) leave only
   $K<K_0(\rho)\le K_0(5/6)<87025$.
3. On $[5/6,7/8]$, (1) leaves only
   $$K<\frac{54}{(1-\rho)^2}\le3456.$$
4. On $[7/8,9/10]$, the accepted constant-$32$ theorem leaves only
   $$K<\frac{32}{(1-\rho)^2}\le3200.$$
5. On $[9/10,19/20]$, the accepted constant-$24$ theorem leaves only
   $$K<\frac{24}{(1-\rho)^2}\le9600.$$
6. On $[19/20,24/25]$, the same theorem leaves only $K<15000$.
7. On $[24/25,99/100]$, the accepted constant-$20$ theorem leaves only
   $K<200000$.
8. Every frequency on $[99/100,1)$ is already proved at every $K$.

Thus all finite residual ceilings are strictly below or equal to the last
open-sided ceiling, and equality $K=200000$ is covered everywhere.  This
proves (3).  The exact improvement over the accepted Round 14 ceiling is

$$
\frac{550^2}{200000}=\frac{121}{80}
=1+\frac{41}{80}>1.
\tag{55}
$$

Face ownership is as follows.

* At $\rho=\rho_*$ the complete small-hole theorem owns every $K$; at
  $\rho=1/16$ the two accepted central regimes meet and retain their
  $K=64$ face.
* At $\rho=5/6$, (1) includes $K=54\cdot6^2=1944$.  The fixed-ratio
  theorem separately owns $K=K_0(5/6)$, and (2) makes $K=295^2=87025$
  a strict-above-threshold value.  The energy $K=294^2=86436$ is owned on
  this seam by (1); (54) is not used to claim a uniform central ceiling
  at $294^2$.
* At $\rho=7/8$, the accepted constant-$32$ theorem owns the sharper
  equality $K=32\cdot8^2=2048$, and hence also the coarser new-seam face
  $K=54\cdot8^2=3456$.
* At $\rho=9/10$, the accepted constant-$24$ theorem owns the sharper
  $K=24\cdot10^2=2400$, and hence the constant-$32$ coarse face
  $K=3200$.
* At $\rho=19/20$, the constant-$24$ theorem includes $K=9600$.
  At $\rho=24/25$, the constant-$20$ theorem owns the sharper
  $K=12500$, and hence the left-zone coarse face $K=15000$.
* At $\rho=99/100$, the complete endpoint owns every energy, including
  $K=200000$.  The central fixed-ratio theorem includes its exact
  threshold, all seam theorems include their threshold equality, and no
  ratio or energy face is left open.

The adjacent coarse ceilings $3456$ and $3200$ are intentionally not
ordered: at and beyond $\rho=7/8$, the accepted constant-$32$ theorem is
sharper.  These seven zones are coarse enclosures of the exact complement,
not a rectangular certification target.  The remaining compact residual
below the analytic cover stays open.

## 13. Executable standard-library exact ledger

The following ledger verifies the frozen packet digest and every finite
rational comparison used above.  It is not a Bessel-root certificate and
does not replace the symbolic branch proof.

```python
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

packet = Path(
    "state/lemma_packets/"
    "SHELL-central-thin-seam-compression-round15.md"
)
assert sha256(packet.read_bytes()).hexdigest() == (
    "c35243cb98c842692f9cfa8c98d03164"
    "a8b8b710952e5aa6161205b1951ccbe7"
)

# Machin upper and lower bounds.
machin_upper = F(5277328977275528, 1679825970703125)
assert F(1571, 500) - machin_upper == F(
    2736890694763, 6719303882812500
)
assert F(22, 7) - F(1571, 500) == F(3, 3500)
machin_lower = F(1231847548, 392109375)
assert machin_lower - F(333, 106) == F(
    3418213, 41563593750
)

# Elementary radicals, angular route, shelf, and y endpoint.
assert F(2) - F(140, 99) ** 2 == F(2, 9801)
assert F(99, 70) ** 2 - F(2) == F(1, 4900)
assert F(97, 56) ** 2 - 3 == F(1, 3136)
assert F(2) - F(7, 5) ** 2 == F(1, 25)
assert F(7, 9) ** 2 - F(3, 5) == F(2, 405)
assert F(169, 25) - 2 * F(1571, 500) == F(119, 250)
assert F(49, 120) ** 2 - F(1, 6) == F(1, 14400)
assert 6 - F(120, 49) ** 2 == F(6, 2401)

# Displacement and localization.
assert F(763, 5000) ** 2 - F(1571, 67500) == F(
    8563, 675000000
)
q_proxy = F(1, 1620) + F(13, 5) * F(763, 5000)
assert q_proxy == F(804689, 2025000)
assert F(159, 400) - q_proxy == F(497, 4050000)
assert F(5, 6) * (1 - F(159, 400)) == F(241, 480)
assert F(241, 480) - F(1, 2) == F(1, 480)

# Complete fixed-r=B synthetic path.
dQ = F(637, 32400)
path_derivative = (
    2
    * F(1571, 500) ** 2
    * dQ
    * (1 + F(159, 400) + F(2, 5))
    / (1 - F(159, 400)) ** 3
)
assert path_derivative == F(2260740364246, 708624500625)
assert F(16, 5) - path_derivative == F(
    6858037754, 708624500625
)
B = F(14, 3)
assert 2 * B - F(16, 5) == F(92, 15)
Q0 = 1 + F(1, 324) + F(49, 120) * B / 54
q0 = F(1, 5) * (Q0 - 1)
assert Q0 == F(10093, 9720)
assert q0 == F(373, 48600)
endpoint_reserve = (
    B**2
    - 2 * F(1571, 500) ** 2 * Q0 / (1 - q0) ** 2
)
assert endpoint_reserve == F(
    2505132463469, 2616573970125
)

# Action gain, full floor loss, and both payment branches.
gain = 36 * F(140, 99) / F(1571, 500)
assert gain == F(280000, 17281)
assert gain - B == F(598066, 51843)
dangerous_M = (gain - B) * F(120, 49) - 1
safe_M = gain * F(120, 49) - 1
assert dangerous_M == F(3296553, 120967)
assert safe_M == F(4679033, 120967)
delta_cap = F(8, 15) * F(99, 70)
assert delta_cap == F(132, 175)
assert dangerous_M - delta_cap == F(80132733, 3024175)
assert safe_M - delta_cap == F(114694733, 3024175)

# Independent endpoint rho=5/6.
assert F(36) - 10 * F(22, 7) == F(32, 7)
assert 49 - 9 * F(1571, 500) * F(97, 56) == F(517, 28000)
assert 1 + F(8, 15) * F(99, 70) == F(307, 175)
assert (
    F(1, 49) * 295**2 - 6 * 295 - F(307, 175)
) == F(5226, 1225)

# Exact route obstructions, not theorem counterexamples.
assert F(333, 14045) - F(3079, 20000) ** 2 == F(
    10003031, 1123600000000
)
assert (
    F(1, 1590) + F(13, 5) * F(3079, 20000) - F(2, 5)
) == F(14293, 15900000)
assert (
    F(1, 49) * 294**2 - 6 * 294 - F(307, 175)
) == -F(307, 175)

# Closed-zone thresholds and high-frequency reduction.
assert 54 * 6**2 == 1944
assert 32 * 8**2 == 2048
assert 24 * 10**2 == 2400
assert 32 * 10**2 == 3200
assert 54 * 8**2 == 3456
assert 24 * 20**2 == 9600
assert 20 * 25**2 == 12500
assert 24 * 25**2 == 15000
assert 20 * 100**2 == 200000
assert 294**2 == 86436
assert 295**2 == 87025
assert 200000 - 64 == 199936
assert 200000 - 87025 == 112975
assert 200000 - 3456 == 196544
assert 200000 - 3200 == 196800
assert 200000 - 9600 == 190400
assert 200000 - 15000 == 185000
assert 550**2 - 200000 == 102500
assert F(550**2, 200000) == F(121, 80)
assert F(121, 80) - 1 == F(41, 80)

print("all exact Round 15 incumbent ledger checks passed")
```

## Final assessment

No candidate implication failed.  The narrowest principal reserves are
$497/4050000$ in the displacement proxy,
$2505132463469/2616573970125$ at the synthetic-path endpoint,
$6858037754/708624500625$ in the path derivative cap, and
$5226/1225$ in the independent central-endpoint comparison.  Every
exceptional branch, threshold equality, denominator, radicand, squaring
wall, interface wall, spectral wall, and shared union face is owned.
The fresh seam theorem, independent endpoint comparison, and prospective
seven-zone union therefore pass the incumbent gate.
