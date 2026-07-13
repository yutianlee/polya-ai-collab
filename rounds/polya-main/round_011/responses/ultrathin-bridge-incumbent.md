# Round 11 Incumbent: Direct Ultra-Thin Complementary Action Bridge

## Result

Let

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le\frac1{100},
\qquad a=\varepsilon K.
$$

Then

$$
\boxed{
a\ge\frac1{8\varepsilon^{3/2}}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

The accepted product and aggregate theorems cover the complementary closed
range

$$
0\le a\le\frac1{8\varepsilon^{3/2}}.
$$

Thus the strict shell Pólya inequality holds for every $K\ge0$ whenever

$$
\boxed{0<\varepsilon\le\frac1{100}},
$$

or equivalently throughout the complete thin endpoint

$$
\boxed{\frac{99}{100}\le\rho<1.}
\tag{2}
$$

Combined with the Round 10 central--thin seam, this lowers the all-ratio
analytic high-frequency ceiling from $125^5/8$ to

$$
\boxed{6000^2=36{,}000{,}000.}
\tag{3}
$$

## 1. Exact proxy and inverse action

Define

$$
\mathcal A(y)=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds,
\qquad
T=\mathcal A(0)=\frac a\pi.
\tag{4}
$$

Let $R(t)$ be its decreasing inverse and put

$$
F(t)=R(t)^2,
\qquad 0\le t\le T.
$$

Then $F(0)=a^2$, $F(T)=0$, and exact layer cake gives

$$
I:=\int_0^a y\mathcal A(y)\,dy
=\frac12\int_0^T F(t)\,dt.
\tag{5}
$$

On the strict half-integer mesh set

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad
q_\ell=[\mathcal A(y_\ell)+1/4]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_\ell y_\ell q_\ell.
$$

For

$$
x_n=n-\frac14,
\qquad
M_\varepsilon(x)=
\#\left\{\ell\ge0:\varepsilon(\ell+1/2)<x\right\},
$$

the exact strict layer-cake identity is

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{x_n<T}M_\varepsilon(R(x_n))^2.
\tag{6}
$$

The radial condition is strict.  If $x_n=T$, that layer is excluded.

The accepted phase enclosure gives

$$
N_D(A_{\rho,1},K^2)
\le\frac{2P_{\mathcal A}}{\varepsilon^2}.
\tag{7}
$$

Also, with

$$
m_\varepsilon=1-\varepsilon+\frac{\varepsilon^2}{3},
$$

Fubini gives

$$
I=\frac{m_\varepsilon a^3}{3\pi},
\qquad
\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{8}
$$

It remains to prove $P_{\mathcal A}<I$.

## 2. U-shaped derivative magnitude

Let

$$
\tau=\mathcal A(\rho a).
$$

The exact action derivatives imply

$$
F''(t)>0\quad(0<t<\tau),
\qquad
F''(t)<0\quad(\tau<t<T).
\tag{9}
$$

For completeness, if $y=R(t)$, then

$$
F''(t)=
\frac{2(\mathcal A'(y)-y\mathcal A''(y))}
{\mathcal A'(y)^3}.
$$

On the outer side the numerator is negative.  On the inner side its sign is
controlled by

$$
h(x)=\arccos x+\frac{x}{\sqrt{1-x^2}},
\qquad
h'(x)=\frac{x^2}{(1-x^2)^{3/2}}>0.
$$

Therefore

$$
g(t):=-F'(t)
$$

decreases on $(0,\tau)$ and increases on $(\tau,T)$.  The first derivative
of the action is continuous and nonzero at the inner interface, so $g$ is
continuous there.

The interface height has the exact representation

$$
\tau=\frac a{\pi\varepsilon}
\int_0^\varepsilon\arccos(1-v)\,dv.
$$

Since $\arccos(1-v)\ge\sqrt{2v}$,

$$
\tau\ge\frac{2\sqrt2}{3\pi}a\sqrt\varepsilon.
$$

Using $a\ge1/(8\varepsilon^{3/2})$, $\sqrt2>7/5$, and
$\pi<22/7$ gives

$$
\tau>
\frac{49}{1320\varepsilon}
\ge\frac{245}{66}>1.
\tag{10}
$$

Thus both $3/4$ and $1$ lie strictly in the decreasing branch of $g$.

## 3. Exact shifted radial discrepancy

Put

$$
\mathcal N(t)=\#\{n\ge1:x_n<t\},
\qquad
u(t)=t-\mathcal N(t).
$$

Since $F(x)=\int_x^Tg(t)\,dt$, Tonelli gives

$$
D:=\int_0^T F(t)\,dt-\sum_{x_n<T}F(x_n)
=\int_0^T u(t)g(t)\,dt.
\tag{11}
$$

On a unit cell $t=j+r$, $0\le r<1$,

$$
u(j+r)=
\begin{cases}
r,&0\le r\le3/4,\\
r-1,&3/4<r<1.
\end{cases}
\tag{12}
$$

At the strict radial wall $r=3/4$, the new layer is excluded and the first
line applies.

Set $v=u-1/4$ and let $V$ be its continuous periodic primitive normalized by
$V(j)=0$ on the integers.  Direct integration of (12) gives

$$
-\frac1{32}\le V(t)\le\frac3{32}.
\tag{13}
$$

The integral over the first cell is interpreted improperly at $t=0$ if
necessary.  Its positive part may be discarded; on $(3/4,1)$, $g$ is
decreasing.  Hence

$$
\int_0^1u(t)g(t)\,dt
\ge-\frac1{16}g(3/4).
\tag{14}
$$

Riemann--Stieltjes integration by parts on $[1,\tau]$, where $g$ decreases,
and on $[\tau,T]$, where it increases, gives

$$
\int_1^\tau v(t)g(t)\,dt
\ge-\frac1{32}g(1),
\qquad
\int_\tau^T v(t)g(t)\,dt
\ge-\frac18g(T).
\tag{15}
$$

The $V(\tau)g(\tau)$ interface terms are retained with opposite signs and
cancel; no grid location for $\tau$ is assumed.  Since $g(1)\le g(3/4)$,
(11)--(15) yield

$$
\boxed{
D\ge\frac14F(1)-\frac3{32}g(3/4)-\frac18g(T).
}
\tag{16}
$$

## 4. Three exact endpoint estimates

For $0<t<\tau$, write

$$
R(t)=a\cos\theta.
$$

The outer action formula gives

$$
t=\frac a{\pi\varepsilon}
(\sin\theta-\theta\cos\theta),
\qquad
g(t)=\frac{2\pi\varepsilon a\cos\theta}{\theta}.
\tag{17}
$$

Because

$$
\sin\theta-\theta\cos\theta
=\int_0^\theta s\sin s\,ds
\le\frac{\theta^3}{3},
$$

one has

$$
g(t)
\le
\frac{2\pi}{(3\pi)^{1/3}}
\varepsilon^{2/3}a^{4/3}t^{-1/3}.
$$

The coefficient is less than $3$ because $8\pi^2<80<81$.  Also
$(4/3)^{1/3}<4/3$.  Therefore

$$
g(3/4)<4\varepsilon^{2/3}a^{4/3}.
\tag{18}
$$

At $t=1$, the chord bound

$$
\sin s\ge\frac{2s}{\pi}
\qquad(0\le s\le\pi/2)
$$

in (17) yields

$$
\theta^3\le\frac{3\pi^2\varepsilon}{2a}.
$$

Since $\cos^2\theta\ge1-\theta^2$ and
$(3\pi^2/2)^{2/3}<7$,

$$
F(1)>a^2-7\varepsilon^{2/3}a^{4/3}.
\tag{19}
$$

Finally, the expansion at the regular endpoint $y=0$ is

$$
\mathcal A'(y)\sim-\frac{y}{\pi\rho a}.
$$

Thus

$$
g(T)=2\pi\rho a<\frac{44}{7}a.
\tag{20}
$$

Substitution of (18)--(20) into (16) proves

$$
\boxed{
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a.
}
\tag{21}
$$

## 5. Angular half-integer ceilings

For every $x\ge0$, including an equality wall,

$$
M_\varepsilon(x)<\frac{x}{\varepsilon}+\frac12.
$$

Consequently

$$
\varepsilon^2M_\varepsilon(x)^2
<x^2+\varepsilon x+\frac{\varepsilon^2}{4}.
\tag{22}
$$

Let $N=\#\{n:x_n<T\}$.  The hypotheses imply $a\ge125$.  Since
$\pi>3$,

$$
N<T+\frac14<\frac a3+\frac14<\frac a2,
\qquad
\sum_{x_n<T}R(x_n)<Na<\frac{a^2}{2}.
\tag{23}
$$

Equations (5)--(6) and (21)--(23) now give

$$
I-P_{\mathcal A}
>
\frac D2-\frac{\varepsilon a^2}{4}
-\frac{\varepsilon^2a}{16}.
$$

After division by $a^2$,

$$
\frac{I-P_{\mathcal A}}{a^2}
>
\frac18
-\frac{17}{16}\left(\frac\varepsilon a\right)^{2/3}
-\frac{11}{28a}
-\frac\varepsilon4
-\frac{\varepsilon^2}{16a}.
\tag{24}
$$

The lower bound on $a$ implies

$$
\left(\frac\varepsilon a\right)^{2/3}
\le4\varepsilon^{5/3},
\qquad
\frac1a\le8\varepsilon^{3/2}.
$$

Therefore

$$
\frac{I-P_{\mathcal A}}{a^2}
>
\frac18
-\frac{17}{4}\varepsilon^{5/3}
-\frac{22}{7}\varepsilon^{3/2}
-\frac\varepsilon4
-\frac12\varepsilon^{7/2}.
\tag{25}
$$

For $0<\varepsilon\le1/100$,

$$
\varepsilon^{2/3}<\frac1{20},
\qquad
\sqrt\varepsilon\le\frac1{10},
\qquad
\varepsilon^{5/2}\le\frac1{100000}.
$$

The total coefficient charged against $\varepsilon$ is at most

$$
\frac{17}{80}+\frac{11}{35}+\frac14+\frac1{200000}
=\frac{1087507}{1400000}
<\frac{57}{7}.
$$

It follows that

$$
\frac{I-P_{\mathcal A}}{a^2}
>
\frac18-\frac{57}{7}\varepsilon
\ge\frac18-\frac{57}{700}
=\boxed{\frac{61}{1400}>0}.
\tag{26}
$$

This proves $P_{\mathcal A}<I$, including the two parameter endpoints in
(1).  Equations (7)--(8) prove the claimed strict shell estimate.

## 6. Closed faces and complete thin endpoint

The accepted low union is

$$
0\le a\le\frac1{8\varepsilon^{3/2}}.
$$

The new theorem is the complementary closed range

$$
\frac1{8\varepsilon^{3/2}}\le a<\infty.
$$

The common face belongs to both proofs.  Therefore every $a\ge0$, hence
every $K\ge0$, is covered for $0<\varepsilon\le1/100$.

At $\varepsilon=1/100$, the new lower threshold is $a=125$, and the explicit
margin (26) is still positive.  The face $\rho=99/100$ belongs both to this
complete endpoint and to the Round 10 seam zone.  The old endpoint face
$\varepsilon=1/15625$ lies strictly inside the new all-frequency domain.

The wall conventions are unchanged:

1. $x_n=T$ is excluded by the strict radial layer condition.
2. $R(x_n)/\varepsilon=\ell+1/2$ is excluded by the exact definition of
   $M_\varepsilon$.
3. $\mathcal A(y_\ell)+1/4=n$ excludes the $n$th proxy layer.
4. The curvature switch $t=\tau$ is not assigned to a discrete side; its
   continuous integration-by-parts terms cancel.
5. The final spectral phase is only majorized, so a strict eigenvalue wall
   is never inserted.

## 7. Global ceiling and residual reduction

Use the following closed analytic zones.

1. On $(0,\rho_*]$, the small-hole endpoint proves every frequency.
2. On $[\rho_*,1/16]$, every possible residual has $K<64$.
3. On $[1/16,24/25]$, the fixed-ratio threshold is bounded by
   $K_0(24/25)<6000^2$.
4. On $[24/25,99/100]$, the Round 10 theorem starts at
   $K=20/(1-\rho)^2\le200000$.
5. On $[99/100,1)$, (2) proves every frequency.

All shared faces belong to both adjacent closed zones.  Hence

$$
\boxed{
0<\rho<1,\qquad K\ge6000^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{27}
$$

The exact comparisons with the previous ceilings are

$$
\frac{125^5/8}{6000^2}=\frac{1953125}{18432}>105,
\qquad
\frac{2^{35}}{6000^2}=\frac{134217728}{140625}>954.
$$

Equivalently,

$$
\frac{125^5}{8}-6000^2=\frac{30229578125}{8},
\qquad
2^{35}-6000^2=34323738368.
$$

The newly discharged radius strip has exact width

$$
\left(1-\frac1{15625}\right)-\frac{99}{100}
=\frac{621}{62500}.
$$

The unresolved compact problem now has the single uniform bound

$$
K<6000^2.
$$

This is an analytic planning envelope, not a Bessel-root certificate.  The
compact all-frequency theorem and final target remain open below (3).
