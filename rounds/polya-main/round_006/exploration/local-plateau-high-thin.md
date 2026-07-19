# Round 6 exploration: a uniform local-plateau high-thin theorem

## Verdict

Put

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le\frac1{100}.
$$

The fixed-$\rho$ shifted-tail proof can be sharpened by retaining the
location of the first floor plateau.  The resulting explicit theorem is

$$
\boxed{
K\ge\frac{64}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

This improves the previous thin asymptotic threshold from order
$\varepsilon^{-4}$ to order $\varepsilon^{-2}$.  It is radius-sensitive:
the proof uses the exact derivative of
$A_{\rho,K}=G_K-G_{\rho K}$ and cannot be recovered from the rejected
constant-potential comparison $r^{-2}\ge1$.

This report is a proof candidate for independent review.  It does not edit
the authoritative state.

## 1. The audited shifted-tail reduction

Let

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
$$

and

$$
\eta=G_1(\rho).
$$

For a tail beginning at the half-integer $x_0=r+1/2<\mu$, set

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\xi=\mu-q\in[0,1).
$$

Let $p$ be the last sample in the initial constant-floor plateau of

$$
A(x_0+j)+\frac14,
\qquad 0\le j\le n;
$$

if there is no drop before the interface, set $p=n$.  Put

$$
m=n-p.
$$

The already-audited concave-head/convex-tail decomposition, before its final
fixed-$\rho$ estimate, gives

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta-\frac M4,
\tag{2}
$$

where

$$
0\le\delta=\int_q^\mu G_\mu(z)\,dz
<\frac{2\sqrt2}{15},
\tag{3}
$$

and

$$
M=\lfloor K\eta\rfloor+d(n-p)-p
=\lfloor K\eta\rfloor+dm-p.
\tag{4}
$$

Here $\rho>1/2$, so the convex-tail gain may be bounded from below by
$\lfloor G_K(\mu)\rfloor=\lfloor K\eta\rfloor$.  The same decomposition
also proves the unconditional plateau estimate

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{5}
$$

For $n=0$ take $p=m=0$; the purely convex tail is already included in
(2)--(4).  Tails beginning at or above $\mu$ are covered by the audited
convex shifted-tail theorem.

It remains to prove $M>4\delta$ uniformly under the hypotheses of (1).

## 2. A location-sensitive plateau estimate

Define the possible loss

$$
R=p-dm.
\tag{6}
$$

If $R\le0$, equation (4) has no plateau loss.  Assume henceforth that
$R>0$.  Since

$$
\rho\ge\frac{99}{100}>\frac{\sqrt3}{2},
$$

one has

$$
c<\frac16,
\qquad
d>\frac23.
\tag{7}
$$

Thus $m<p/d<3p/2$.  With

$$
u:=\mu-x_0=p+m+\xi,
$$

this gives

$$
u<\frac52p+1.
\tag{8}
$$

### 2.1. The plateau must begin in the outer half

We first prove

$$
\boxed{x_0\ge\frac K2.}
\tag{9}
$$

If instead $x_0<K/2$, then

$$
u=\mu-x_0>
\left(\frac12-\varepsilon\right)K
\ge\frac{49}{100}K.
$$

Since $K\ge64\varepsilon^{-2}>100$, (8) would imply

$$
p>
\frac25\left(\frac{49}{100}K-1\right)
>\frac{24}{125}K.
\tag{10}
$$

On the other hand, (5) and $\pi<4$ give

$$
p^2<\frac{8K}{\varepsilon}.
$$

Combining this with (10) would give

$$
K<\frac{125000}{576\varepsilon}<\frac{218}{\varepsilon}.
$$

But the assumed threshold and $\varepsilon\le1/100$ give
$K\ge6400/\varepsilon$, a contradiction.  This proves (9).

### 2.2. Exact local slope

For $0<z<\mu$, put $\sigma(z)=-A'(z)$.  Then

$$
\sigma(z)
=\frac1\pi
\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
\tag{11}
$$

For fixed $z$, differentiation in the radius variable gives

$$
\arccos\frac zK-\arccos\frac z\mu
=\int_\mu^K
\frac{z}{R\sqrt{R^2-z^2}}\,dR.
$$

The integrand decreases in $R$, and $K-\mu=\varepsilon K$.  Hence

$$
\boxed{
\sigma(z)
\ge
\frac{\varepsilon z}{\pi\sqrt{K^2-z^2}}.
}
\tag{12}
$$

The floor is constant from $0$ through $p$, so for $p>0$,

$$
A(x_0)-A(x_0+p)<1.
$$

Since $\sigma$ is increasing,

$$
1>\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
$$

Using (9) and (12), and noting that
$K-x_0=\varepsilon K+u$, yields

$$
\begin{aligned}
p^2\varepsilon^2\frac{K^2}{4}
&<\pi^2(K^2-x_0^2)\\
&\le2\pi^2K(\varepsilon K+u).
\end{aligned}
$$

Therefore

$$
p^2
<\frac{8\pi^2}{\varepsilon^2}
\left(\varepsilon+\frac uK\right).
\tag{13}
$$

Equations (8), (13), and $K\ge64\varepsilon^{-2}$ give

$$
p^2
<\frac{8\pi^2}{\varepsilon}
+\frac{5\pi^2}{16}p
+\frac{\pi^2}{8}.
\tag{14}
$$

Let $P=10/\sqrt\varepsilon$.  The quadratic polynomial obtained by moving
the right side of (14) to the left is increasing for $p\ge P$, and, using
$\pi^2<10$ and $1/\sqrt\varepsilon\ge10$, its value at $P$ is larger than

$$
\frac{20}{\varepsilon}
-\frac{125}{4\sqrt\varepsilon}
-\frac54>0.
$$

Thus (14) forces

$$
\boxed{p<\frac{10}{\sqrt\varepsilon}.}
\tag{15}
$$

Together with (6), this gives the uniform loss bound

$$
R<\frac{10}{\sqrt\varepsilon}.
\tag{16}
$$

## 3. The convex gain pays for the local plateau

Since $G_1'(x)=-\pi^{-1}\arccos x$ and $G_1(1)=0$,

$$
\eta
=\frac1\pi\int_0^\varepsilon
\arccos(1-v)\,dv.
$$

The elementary inequality $\cos x\ge1-x^2/2$ implies
$\arccos(1-v)\ge\sqrt{2v}$.  Consequently,

$$
\boxed{
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
}
\tag{17}
$$

Using $\lfloor x\rfloor>x-1$, (4), (16), (17), and
$K\ge64\varepsilon^{-2}$ gives

$$
\begin{aligned}
M
&>K\eta-1-\frac{10}{\sqrt\varepsilon}\\
&\ge
\left(\frac{128\sqrt2}{3\pi}-10\right)
\frac1{\sqrt\varepsilon}-1\\
&>
\frac{2}{3\sqrt\varepsilon}-1
\ge\frac{17}{3}.
\end{aligned}
\tag{18}
$$

The strict penultimate inequality uses only $\sqrt2>1$ and $\pi<4$.
Since

$$
4\delta<\frac{8\sqrt2}{15}<\frac{16}{15}<\frac{17}{3},
$$

equations (2) and (18) prove every low-interface shifted tail.

The already-proved convex theorem handles every tail beginning at or above
$\mu$.  The multiplicity-to-tail scaffold therefore gives

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{19}
$$

The strict transferred phase proxy is no larger than this ordinary-floor
coarse proxy.  The exact separated spectral identity then proves (1),
including all spectral and floor walls.

## 4. Consequences and remaining gap

In optical width $a=\varepsilon K$, theorem (1) begins at

$$
a\ge\frac{64}{\varepsilon}.
$$

Thus the former high threshold of order $\varepsilon^{-3}$ in $a$ is
replaced by a threshold of order $\varepsilon^{-1}$.  This has the correct
scale to turn the remaining thin problem into a constant-width gap after
the rescaling $C=\varepsilon^2K=\varepsilon a$.

The proof does not claim that the constant $64$ is optimal.  The local
slope estimate deliberately sacrifices constants in order to establish the
uniform exponent cleanly.  Promotion requires an isolated reconstruction
of (8)--(18), an adversarial audit of the $p=n$ no-drop case, and a check of
the imported decomposition (2)--(4).

## Classification

- **Proved in this report:** the local plateau estimate (15) and the
  high-thin theorem (1), subject to the already-audited shifted-tail
  decomposition and exact spectral bridge.
- **Not claimed:** closure below $64\varepsilon^{-2}$, optimality of the
  constant, or any conclusion from floating-point diagnostics.
