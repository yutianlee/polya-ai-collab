# Round 5 Incumbent: Thin-Shell Product Range and Its Obstruction

## Verdict

Let

$$
\rho=1-\varepsilon,\qquad
0<\varepsilon\le\frac1{100},\qquad
a=\varepsilon K.
$$

Then the exact separated radial operator comparison proves

$$
\boxed{
0\le a\le\frac{\pi}{4\varepsilon}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

This is a genuine uniform thin-shell range. The same product comparison
cannot close the endpoint: its own leading coefficient is too large, and it
fails at exact radial walls of order $a\asymp\varepsilon^{-1}$, far below the
existing fixed-$\rho$ high-energy threshold of order
$a\asymp\varepsilon^{-3}$.

## 1. Operator comparison and strict product count

The Round 4 direct-sum theorem identifies the radial blocks as

$$
L_\ell
=
-\frac{d^2}{dr^2}
+\frac{\ell(\ell+1)}{r^2}
$$

on $(1-\varepsilon,1)$ with Dirichlet endpoints. Since $r\le1$,

$$
L_\ell
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1)
$$

in the form sense. The min--max principle therefore gives

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
\tag{2}
$$

If $\lambda_{\ell,n}<K^2$, then

$$
n\pi<a
$$

and

$$
\ell(\ell+1)
<
\frac{a^2-n^2\pi^2}{\varepsilon^2}.
\tag{3}
$$

Define the strict radial count

$$
N=
\max\left\{
0,\left\lceil\frac a\pi\right\rceil-1
\right\}.
\tag{4}
$$

At $a=m\pi$, formula (4) gives $N=m-1$, so the endpoint radial mode is
excluded.

For $1\le n\le N$, set

$$
b_n=\sqrt{a^2-n^2\pi^2},
\qquad
T_n=\frac{b_n}{\varepsilon}.
$$

The number of allowed nonnegative angular indices is

$$
\begin{aligned}
M_n
&=
\#\{\ell\ge0:\ell(\ell+1)<T_n^2\}\\
&=
\left\lceil
\sqrt{T_n^2+\frac14}-\frac12
\right\rceil.
\end{aligned}
\tag{5}
$$

If $T_n^2=p(p+1)$, the strict inequality permits
$\ell=0,\ldots,p-1$, and (5) gives $M_n=p$. Thus (5) is also correct at
every angular wall.

The exact angular multiplicity sum is

$$
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2.
$$

Summing the necessary condition (3), with all eigenvalues counted according
to the proved direct sum, gives

$$
\boxed{
N_D(A_{1-\varepsilon,1},K^2)
\le
\mathcal P_\varepsilon(a)
:=
\sum_{n=1}^{N}M_n^2.
}
\tag{6}
$$

No reordering or nondegeneracy assumption is used.

## 2. Exact angular-rounding bounds

For $T>0$, put

$$
\alpha(T)=\sqrt{T^2+\frac14}-\frac12,
\qquad
M(T)=\lceil\alpha(T)\rceil.
$$

Since the top included angular index is $M-1$,

$$
(M-1)M<T^2.
$$

Hence

$$
M^2<T^2+M
<
T^2+\sqrt{T^2+\frac14}+\frac12
<
T^2+T+1.
\tag{7}
$$

For the lower bound, $M\ge\alpha(T)\ge T-1/2$. When $T\ge1$ this gives
$M^2\ge T^2-T$, while for $0<T<1$ the right side is nonpositive. Therefore

$$
\boxed{
T^2-T\le M(T)^2<T^2+T+1.
}
\tag{8}
$$

Define

$$
S_0(a)=\sum_{n=1}^{N}b_n^2,
\qquad
B(a)=\sum_{n=1}^{N}b_n.
$$

The upper half of (8) gives

$$
\mathcal P_\varepsilon(a)
<
\frac{S_0(a)}{\varepsilon^2}
+\frac{B(a)}{\varepsilon}+N.
\tag{9}
$$

For $N\ge1$, the lower half is strict and gives

$$
\mathcal P_\varepsilon(a)
>
\frac{S_0(a)}{\varepsilon^2}
-\frac{B(a)}{\varepsilon}.
\tag{10}
$$

When $N=0$, both sides of (10) are zero, so only the non-strict version
holds. Every later use of the strict form has $N\ge1$.

## 3. Exact radial lattice margin

Let

$$
I(a)=\frac{2a^3}{3\pi},
\qquad
D(a)=I(a)-S_0(a).
$$

For $a>0$, write the strict radial remainder as

$$
\frac a\pi=N+t,\qquad 0<t\le1.
\tag{11}
$$

At a radial wall $a=m\pi$, this means $N=m-1$, $t=1$.

Using

$$
S_0(a)
=
Na^2-\frac{\pi^2N(N+1)(2N+1)}6
$$

and substituting (11) gives

$$
\boxed{
D(a)
=
\pi^2\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
}
\tag{12}
$$

The formula is continuous when $a$ crosses a radial wall because the new
summand enters with value zero. Between walls,

$$
D'(a)=2at>0.
$$

Consequently,

$$
D(a)\ge D(\pi)=\frac{2\pi^2}{3}
\qquad(a\ge\pi).
\tag{13}
$$

Also $N\ge a/\pi-1$, so

$$
D(a)\ge\frac{\pi^2N^2}{2}
\ge\frac{(a-\pi)^2}{2}.
\tag{14}
$$

Because $x\mapsto\sqrt{a^2-\pi^2x^2}$ is decreasing,

$$
B(a)
\le
\int_0^{a/\pi}\sqrt{a^2-\pi^2x^2}\,dx
=
\frac{a^2}{4}.
\tag{15}
$$

Finally,

$$
N\le\frac a\pi.
\tag{16}
$$

## 4. Comparison with the shell Weyl term

The exact target is

$$
\begin{aligned}
W_\varepsilon(a)
&=
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)
\frac{a^3}{\varepsilon^3}\\
&=
\frac{I(a)}{\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\end{aligned}
\tag{17}
$$

Using $S_0=I-D$ in (9), it is sufficient that

$$
D(a)
\ge
\varepsilon\bigl(I(a)+B(a)\bigr)
+\varepsilon^2
\left(N-\frac{I(a)}3\right).
\tag{18}
$$

Dropping the favorable term $-\varepsilon^2I/3$ and using
(15)--(16), it is enough to prove

$$
\boxed{
D(a)
\ge
\varepsilon\left(
\frac{2a^3}{3\pi}+\frac{a^2}{4}
\right)
+\frac{\varepsilon^2a}{\pi}.
}
\tag{19}
$$

## 5. Proof of the explicit positive range

If $0\le a\le\pi$, then (4) gives $N=0$, and both the product majorant and
the strict shell count are zero.

Assume next

$$
\pi<a\le4\pi.
$$

The right side of (19) is increasing in both $a$ and $\varepsilon$. At
$a=4\pi$ and $\varepsilon=1/100$, it is at most

$$
\frac1{100}
\left(
\frac{128\pi^2}{3}+4\pi^2
\right)
+\frac4{10000}
=
\frac{7\pi^2}{15}+\frac1{2500}
<
\frac{2\pi^2}{3}.
\tag{20}
$$

Together with (13), this proves (19) on the entire first range, including
arbitrarily close to $a=\pi$ and at $a=4\pi$.

Finally suppose

$$
4\pi\le a\le\frac{\pi}{4\varepsilon}.
$$

Then

$$
D(a)\ge\frac{(a-\pi)^2}{2}\ge\frac{9a^2}{32}.
\tag{21}
$$

After dividing the right side of (19) by $a^2$,

$$
\begin{aligned}
\frac{2\varepsilon a}{3\pi}
+\frac{\varepsilon}{4}
+\frac{\varepsilon^2}{\pi a}
&\le
\frac16+\frac1{400}+\frac1{40000\pi^2}\\
&<
\frac9{32}.
\end{aligned}
\tag{22}
$$

Thus (19) holds. The three ranges prove (1), including both outer equality
values $\varepsilon=1/100$ and $a=\pi/(4\varepsilon)$.

## 6. Exact obstruction to global product coverage

Fix $0<\varepsilon<1$ and an integer

$$
Q>\frac9{4\varepsilon},
$$

and put $a=Q\pi$. Strict radial counting gives $N=Q-1$. Formula (12) gives

$$
D_Q
=
\pi^2\left(\frac{Q^2}{2}+\frac Q6\right),
\qquad
S_0=I-D_Q,
\tag{23}
$$

where

$$
I=\frac{2\pi^2Q^3}{3}.
$$

The crude but sufficient bound

$$
B(Q\pi)
=
\pi\sum_{n=1}^{Q-1}\sqrt{Q^2-n^2}
<
\pi Q(Q-1)
\tag{24}
$$

combined with (10) and (17) yields

$$
\begin{aligned}
\varepsilon^2
\bigl(\mathcal P_\varepsilon-W_\varepsilon\bigr)
>
&\frac{2\pi^2}{3}
\varepsilon\left(1-\frac{\varepsilon}{3}\right)Q^3\\
&-\pi^2\left(\frac{Q^2}{2}+\frac Q6\right)
-\varepsilon\pi Q(Q-1).
\end{aligned}
\tag{25}
$$

After division by $\pi^2Q$, the first term is strictly larger than

$$
\frac49\varepsilon Q^2>Q.
$$

The sum of the remaining positive quantities to be subtracted is smaller
than

$$
\frac Q2+\frac16+\frac{Q-1}{3}
=
\frac{5Q}{6}-\frac16
<
Q.
$$

Therefore

$$
\boxed{
\mathcal P_\varepsilon(Q\pi)>W_\varepsilon(Q\pi).
}
\tag{26}
$$

There are infinitely many such walls for every fixed $\varepsilon>0$.
Failure of this upper majorant says nothing negative about the true shell
count.

There is also an exact arbitrarily thin family. For every integer $Q\ge4$,

$$
\varepsilon=\frac1Q,\qquad a=Q\pi
$$

satisfies

$$
\mathcal P_{1/Q}(Q\pi)>W_{1/Q}(Q\pi).
\tag{27}
$$

Indeed, with $n=1,\ldots,Q-1$ and

$$
x_n=\pi^2Q^2(Q^2-n^2),
$$

the lower angular bound gives

$$
\mathcal P
>
\sum_{n=1}^{Q-1}x_n
-\pi Q^2(Q-1).
$$

The exact polynomial difference between the first sum and $W$ is

$$
\frac{\pi^2Q^3(3Q-7)}{18}.
$$

Thus

$$
\mathcal P-W
>
\pi Q^2
\left(
\frac{\pi Q(3Q-7)}{18}-(Q-1)
\right)>0
$$

for $Q\ge4$, using only $\pi>3$.

## 7. No overlap with the existing high-energy theorem

For $0<\varepsilon\le1/2$, put $\rho=1-\varepsilon$. The existing
threshold satisfies

$$
K_0(\rho)>
\frac{A_\rho}{\eta_\rho^2},
\qquad
A_\rho=\frac{2\pi(1-\varepsilon)}{\varepsilon},
\qquad
\eta_\rho=G_1(1-\varepsilon).
$$

Since

$$
\eta_\rho
=
\frac1\pi
\int_0^\varepsilon\arccos(1-v)\,dv
<
\frac{\varepsilon^{3/2}}3,
$$

where

$$
\arccos(1-v)
=
2\arcsin\sqrt{\frac v2}
\le
\frac{2\pi}{3}\sqrt{\frac v2}
\qquad(0\le v\le1/2),
$$

and integration gives the displayed estimate. Therefore

$$
\varepsilon K_0(1-\varepsilon)
>
\frac{18\pi(1-\varepsilon)}{\varepsilon^3}
\ge
\frac{9\pi}{\varepsilon^3}.
\tag{28}
$$

On the other hand, let

$$
Q_*=\left\lfloor\frac9{4\varepsilon}\right\rfloor+1.
$$

Then $Q_*>9/(4\varepsilon)$, so (26) applies, and

$$
\pi Q_*
\le
\pi\left(\frac9{4\varepsilon}+1\right)
<
\frac{9\pi}{\varepsilon^3}
\qquad(0<\varepsilon\le1/2).
\tag{29}
$$

Thus an exact product-proxy failure occurs before the current fixed-rho
high-energy theorem begins. The positive product range and that theorem do
not form a covering.

## Scope

The proved range (1) is an actual shell theorem in its stated two-parameter
window. Equations (26)--(29) prove that the outer-minimum product comparison
cannot close the thin-shell endpoint. A radius-sensitive comparison or a
substantially improved high-energy threshold is still required.
