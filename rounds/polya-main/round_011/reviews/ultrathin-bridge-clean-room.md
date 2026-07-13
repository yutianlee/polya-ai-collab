# Round 11 Isolated Clean-Room Reconstruction

## Verdict

**PASS.**

The reviewer inspected only the frozen packet and its permitted prior
dependencies.  No Round 11 response, exploration, computation, review, or
other agent output was inspected.  The reconstruction below is independent
of the incumbent proof and obtains a different, stronger radial reserve.

**First unsupported implication: none found.**

## 1. Exact action and curvature switch

Write

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{100},
\qquad
a\ge\frac1{8\varepsilon^{3/2}}.
$$

For $0\le y\le a$, set

$$
J_r(y)=\sqrt{a^2r^2-y^2}
-y\arccos\frac{y}{ar}.
$$

Then

$$
\mathcal A(y)=
\begin{cases}
\dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
&0\le y\le\rho a,\\[6pt]
\dfrac{J_1(y)}{\pi\varepsilon},
&\rho a\le y\le a.
\end{cases}
$$

In particular,

$$
T=\mathcal A(0)=\frac a\pi,
\qquad
\tau=\mathcal A(\rho a).
$$

Let $R$ be the decreasing inverse, $F=R^2$, and $g=-F'>0$.  For
$y=R(t)$,

$$
F'(t)=\frac{2y}{\mathcal A'(y)},
\qquad
F''(t)=
\frac{2(\mathcal A'(y)-y\mathcal A''(y))}
{\mathcal A'(y)^3}.
$$

On $\rho a<y<a$,

$$
\mathcal A'(y)
=-\frac{\arccos(y/a)}{\pi\varepsilon},
\qquad
\mathcal A''(y)
=\frac1{\pi\varepsilon\sqrt{a^2-y^2}}>0.
$$

Hence $F''>0$ on $0<t<\tau$, so $g$ decreases there.

For $0<y<\rho a$, put $u=y/a$ and

$$
L(u)=\arccos u-\arccos\frac u\rho.
$$

Then

$$
\mathcal A'(y)=-\frac{L(u)}{\pi\varepsilon},
\qquad
\mathcal A''(y)=-\frac{L'(u)}{\pi\varepsilon a}.
$$

Moreover,

$$
L'(u)=\frac1{\sqrt{\rho^2-u^2}}
-\frac1{\sqrt{1-u^2}},
$$

and $L''(u)>0$.  Therefore

$$
\frac d{du}\bigl(uL'(u)-L(u)\bigr)=uL''(u)>0,
$$

while $uL'(u)-L(u)=0$ at $u=0$.  Thus

$$
\mathcal A'(y)-y\mathcal A''(y)
=\frac{uL'(u)-L(u)}{\pi\varepsilon}>0.
$$

Since $\mathcal A'<0$, this gives $F''<0$ on $\tau<t<T$, and $g$
increases there.

The endpoint values needed below are

$$
F(0)=a^2,
\qquad
F(\tau)=\rho^2a^2,
\qquad
F(T)=0,
$$

and

$$
g(T)=2\pi\rho a.
\tag{1}
$$

Indeed, $L'(0)=1/\rho-1=\varepsilon/\rho$, and hence

$$
g(T)
=\lim_{y\downarrow0}\frac{2\pi\varepsilon y}{L(y/a)}
=2\pi\rho a.
$$

At $t=0$, $g$ is singular but harmless.  If $y=a\cos\theta$, then

$$
t=\frac{a}{\pi\varepsilon}
(\sin\theta-\theta\cos\theta),
\qquad
g(t)=\frac{2\pi\varepsilon a\cos\theta}{\theta}.
$$

Thus $t=O(\theta^3)$ and $g=O(\theta^{-1})$; the sawtooth boundary product
used below tends to zero.

## 2. Shifted radial sawtooth

Let

$$
C(t)=\#\{n\ge1:n-1/4<t\},
\qquad
w(t)=t-C(t),
\qquad
W(t)=\int_0^t w(s)\,ds.
$$

Almost everywhere,

$$
C(t)=\left\lfloor t+\frac14\right\rfloor,
\qquad
w(t)=t-\left\lfloor t+\frac14\right\rfloor.
$$

The function $w$ is one-periodic with mean $1/4$.  If

$$
\Psi(t)=W(t)-\frac t4,
$$

then direct calculation over one period gives

$$
-\frac1{32}\le\Psi(t)\le\frac3{32},
\qquad
W(t)\ge0.
\tag{2}
$$

For example, on $0\le u\le1$,

$$
W(u)=
\begin{cases}
u^2/2,&0\le u\le3/4,\\[2pt]
u^2/2-u+3/4,&3/4\le u\le1,
\end{cases}
$$

and $W(k+u)=k/4+W(u)$.

Strict Stieltjes summation gives

$$
\begin{aligned}
D
&:=\int_0^T F(t)\,dt-\sum_{x_n<T}F(x_n)\\
&=\int_0^T w(t)g(t)\,dt.
\end{aligned}
\tag{3}
$$

This identity remains valid at every radial wall $x_n=T$: the wall is
excluded by the strict inequality, and $F(T)=0$.

Split the integral at the actual real number $\tau$; no grid alignment is
assumed.  Since $g$ decreases on $(0,\tau)$, $W\ge0$, and the boundary term
at zero vanishes,

$$
\int_0^\tau wg
\ge W(\tau)g(\tau).
$$

On $(\tau,T)$, $g$ increases and

$$
W(t)\le\frac t4+\frac3{32}.
$$

Consequently,

$$
\begin{aligned}
D
&\ge W(T)g(T)
-\int_\tau^T\left(\frac t4+\frac3{32}\right)\,dg(t)\\
&=
\left(W(T)-\frac T4-\frac3{32}\right)g(T)
+\left(\frac\tau4+\frac3{32}\right)g(\tau)
+\frac14\int_\tau^Tg(t)\,dt.
\end{aligned}
$$

Using

$$
W(T)-\frac T4\ge-\frac1{32},
\qquad
\int_\tau^Tg(t)\,dt=F(\tau)=\rho^2a^2,
$$

and dropping the nonnegative $g(\tau)$ term yields the independent radial
reserve

$$
\boxed{
D\ge\frac{\rho^2a^2}{4}-\frac{g(T)}8
=\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
}
\tag{4}
$$

## 3. Exact half-integer angular ceiling

For $z=x/\varepsilon>0$,

$$
M_\varepsilon(x)
=\max\left\{0,\left\lceil z-\frac12\right\rceil\right\}.
$$

At an angular wall $z=m+1/2$, this equals $m$, so the equality channel is
correctly excluded.  In all cases,

$$
M_\varepsilon(x)<z+\frac12.
$$

Therefore, for every $x_n<T$,

$$
\varepsilon^2M_\varepsilon(R(x_n))^2
<F(x_n)+\varepsilon R(x_n)+\frac{\varepsilon^2}{4}.
$$

Let

$$
J=\#\{n:x_n<T\}.
$$

Strict radial counting gives

$$
J<T+\frac14=\frac a\pi+\frac14.
$$

Also $R(x_n)<a$, because every $x_n>0$.  Hence

$$
\varepsilon\sum_{x_n<T}R(x_n)+\frac{\varepsilon^2J}{4}
<E:=
\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\tag{5}
$$

## 4. Exact endpoint constants

The bridge hypotheses imply

$$
\rho\ge\frac{99}{100},
\qquad
a\ge125.
$$

Using $3<\pi<22/7$, (4) gives

$$
\frac D{a^2}
\ge\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
>
\frac{9801}{40000}-\frac{11}{1750}
=\boxed{\frac{66847}{280000}}.
\tag{6}
$$

From (5),

$$
\frac E{a^2}
<
\frac\varepsilon\pi
+\frac\varepsilon{4a}
+\frac{\varepsilon^2}{4\pi a}
+\frac{\varepsilon^2}{16a^2}.
$$

At $\varepsilon=1/100$, $a=125$, the elementary bounds give

$$
\frac E{a^2}
<
\frac1{300}+rac1{50000}
+\frac1{15000000}+rac1{2500000000}
=\boxed{\frac{8383501}{2500000000}}.
\tag{7}
$$

The exact normalized margin is

$$
\boxed{
\frac{66847}{280000}
-\frac{8383501}{2500000000}
=\frac{4119252993}{17500000000}>0.
}
\tag{8}
$$

Thus $D>E$ throughout the entire closed domain, including
$\varepsilon=1/100$ and $a=1/(8\varepsilon^{3/2})$.

By strict layer cake and the angular estimate,

$$
\begin{aligned}
2P_{\mathcal A}
&=\varepsilon^2
\sum_{x_n<T}M_\varepsilon(R(x_n))^2\\
&<\sum_{x_n<T}F(x_n)+E\\
&<\int_0^T F(t)\,dt
=2I.
\end{aligned}
$$

Therefore

$$
\boxed{P_{\mathcal A}<I.}
\tag{9}
$$

## 5. Conversion to the shell inequality

Tonelli gives the exact continuous action

$$
I=
\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
$$

The permitted strict phase transfer now yields

$$
\begin{aligned}
N_D(A_{\rho,1},K^2)
&\le\frac{2P_{\mathcal A}}{\varepsilon^2}\\
&<\frac{2I}{\varepsilon^2}\\
&=\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
\end{aligned}
$$

This proves the frozen complementary-action theorem, including threshold
equality.

## 6. Complete endpoint

The accepted ranges are

$$
0\le a\le\frac{\pi}{4\varepsilon},
$$

$$
\frac{\pi}{4\varepsilon}
\le a\le\frac1{8\varepsilon^{3/2}},
$$

and the new bridge

$$
a\ge\frac1{8\varepsilon^{3/2}}.
$$

The middle interval is nonempty because

$$
2\pi\sqrt\varepsilon
\le\frac\pi5<\frac{22}{35}<1.
$$

All joining inequalities are closed.  Hence

$$
\boxed{
0<\varepsilon\le\frac1{100},
\qquad K\ge0,
}
$$

or equivalently

$$
\boxed{\frac{99}{100}\le\rho<1.}
$$

## 7. Wall audit

- At a radial wall $x_n=T$, the layer is excluded by $x_n<T$; $F(T)=0$,
  and the Stieltjes identity remains valid.
- At an angular wall $R(x_n)/\varepsilon=m+1/2$, one has
  $M_\varepsilon=m$, excluding equality.
- At a proxy wall $\mathcal A(y_\ell)+1/4=m$, the strict bracket gives
  $q_\ell=m-1$; equivalently the layer condition is
  $x_n<\mathcal A(y_\ell)$.
- The Stieltjes integral is split at the actual ungridded $\tau$.
- The permitted phase transfer retains the strict positive-integer count at
  a spectral wall.
- No global semicircle majorant and no continuous-mass-only inference is
  used.
- Every constant remains strict at $\varepsilon=1/100$ and $a=125$.

## 8. The $K\ge6000^2$ corollary

The permitted closed Round 10 left/central assembly and
$K_0(24/25)<6000^2$ cover $0<\rho\le24/25$ at $K\ge6000^2$.

For

$$
\frac{24}{25}\le\rho\le\frac{99}{100},
\qquad
\frac1{100}\le\varepsilon\le\frac1{25},
$$

the Round 10 seam threshold satisfies

$$
\frac{20}{\varepsilon^2}
\le200000<6000^2.
$$

For $99/100\le\rho<1$, the new endpoint holds for every $K\ge0$.  The
faces $\rho=24/25$ and $\rho=99/100$ belong to both adjacent closed regimes,
and threshold equality is included.  Thus

$$
\boxed{0<\rho<1,\qquad K\ge6000^2}
$$

is proved.

The compact residual below $6000^2$ remains open, as do
`SHELL-rho-compact`, `COMP-certified-bessel`, `SHELL-rho-uniformity`, and
`TARGET-shell-d3`.

## Separate determination

**PASS.**  This artifact supplies the isolated clean-room gate only;
promotion still requires the adversarial, exact-ledger, and judge gates.
