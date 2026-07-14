Isolation declaration — I verified before proof work that the SHA-256 of
state/lemma_packets/SHELL-rho-one-endpoint-round16.md is
5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09.
That frozen packet was my sole Round 16 artifact. I did not inspect
state/next_round_prompts.md, an incumbent, exploration, computation, review,
judge file, another agent, or a future output. I used no Round 5, Round 6, or
Round 11 theorem conclusion.

**PASS.**

First unsupported implication — **none**. The five whitelisted prior facts are
identified below; every other implication needed for the frozen
$7/8\leq\rho<1$, $K\geq0$ claim is reconstructed here. This is a clean-room
proof verdict, not by itself a state promotion or satisfaction of review gates
assigned to other roles.

# Round 16 thin-endpoint clean-room reconstruction

## 1. Domain, convention, and dependency ledger

Put

$$
\varepsilon=1-\rho,\qquad a=\varepsilon K.
$$

Thus the frozen domain is

$$
0<\varepsilon\leq\frac18,\qquad a\geq0.
$$

The strict counting convention counts eigenvalues $\lambda<K^2$, not
$\lambda\leq K^2$. The five permitted inputs, and no others, enter as follows.

| Permitted input | Exact use in this reconstruction |
|---|---|
| CONV-strict-counting and the exact separated shell spectrum | The shell sectors are the one-dimensional Dirichlet operators $L_\ell=-d^2/dr^2+\ell(\ell+1)/r^2$ on $(\rho,1)$, with multiplicity $2\ell+1$. All spectral walls below are therefore excluded. |
| SHELL-sturm-liouville-completeness | Summing the separated sectors accounts for the entire Dirichlet spectrum, with no missing radial or angular branch. |
| The proved radial min--max comparison | It is used only after its direction is rechecked in Section 2: $L_\ell\geq-d^2/dr^2+\ell(\ell+1)$. |
| SHELL-phase-enclosures together with SHELL-annulus-phase-transfer | It is used only in the all-domain proxy transfer (N3), with direction $N_D\leq2P_{\mathcal A}/\varepsilon^2$. No old conclusion $P_{\mathcal A}<I$ is imported. |
| The domain-free action identities | (N1) and (N2), including the normalization integral, are independently derived in Section 3 rather than assumed. |

Every estimate involving $\varepsilon\leq1/8$ is new here: (P5)--(P9),
(H9)--(H12), and the two-piece union. The Round 15 facts recorded in the packet
are quarantined until the separate conditional audit in Section 8. The Round 6
aggregate theorem, its old domain, the old Round 5 product theorem, and the
Round 11 bridge and endpoint conclusions do not enter either proof piece. The
rejected pointwise semicircle majorant is nowhere used.

For $K=0$, $a=0$, strict nonnegative spectral counting gives $N_D(A_{\rho,1},0)=0$
and the proposed right side is also zero. Henceforth in the strict comparisons
$K>0$, equivalently $a>0$.

## 2. Low product piece

This section proves the claim on the inclusive piece

$$
0\leq a\leq\frac{\pi}{4\varepsilon}.
$$

### 2.1. Product comparison and (P1)

For $r\in(\rho,1)$,

$$
\frac{\ell(\ell+1)}{r^2}\geq\ell(\ell+1).
$$

The min--max direction is consequently

$$
\lambda_{\ell,n}(L_\ell)
\geq \left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1),
\qquad n\geq1.
$$

Thus $\lambda_{\ell,n}<K^2$ can hold only if

$$
n^2\pi^2+\varepsilon^2\ell(\ell+1)<a^2. \tag{2.1}
$$

The direction gives an upper, not a lower, spectral count. Define

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\},
\qquad b_n=\sqrt{a^2-n^2\pi^2}.
$$

Exactly the indices $1\leq n\leq N$ satisfy $n\pi<a$. For such an $n$, put
$c=b_n/\varepsilon>0$. The angular condition is

$$
\ell(\ell+1)<c^2
\iff
\ell<\sqrt{c^2+\frac14}-\frac12.
$$

The number of eligible $\ell\in\mathbb N_0$ is therefore

$$
M_n=
\left\lceil
\sqrt{\left(\frac{b_n}{\varepsilon}\right)^2+\frac14}-\frac12
\right\rceil.
$$

Their multiplicities add exactly to

$$
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2.
$$

Completeness and (2.1) now give the intended (P1), with its direction audited:

$$
N_D(A_{\rho,1},K^2)
\leq\mathcal P_\varepsilon(a):=\sum_{n=1}^N M_n^2. \tag{P1}
$$

At a product angular wall

$$
\frac{b_n^2}{\varepsilon^2}=L(L+1),
$$

the displayed square-root expression is the integer $L$, so $M_n=L$ and the
$\ell=L$ level is excluded. Just below the wall it is still excluded and just
above it $M_n=L+1$. The first active radial branch is $n=1$, only for $a>\pi$;
on that branch $\ell=0$ is immediately present because $b_1>0$. At $b_n=0$,
including a radial wall, even $\ell=0$ is excluded.

It follows at once that

$$
\mathcal P_\varepsilon(a)=0\qquad(0\leq a\leq\pi), \tag{2.2}
$$

including $a=0$ and the strict wall $a=\pi$. This proves the exact zero-count
range, rather than borrowing an old slab estimate.

### 2.2. The exact deficit, (P2)--(P6)

For $a>\pi$, strict radial counting gives uniquely

$$
\frac a\pi=N+t,\qquad N\geq1,\qquad0<t\leq1, \tag{P3}
$$

where at $a=m\pi$ one must take $(N,t)=(m-1,1)$. With

$$
I_0(a)=\frac{2a^3}{3\pi},\qquad
S_0(a)=\sum_{n=1}^N(a^2-n^2\pi^2),\qquad
D(a)=I_0(a)-S_0(a), \tag{P2}
$$

the finite-sum identity $\sum_{n=1}^Nn^2=N(N+1)(2N+1)/6$ gives

$$
\begin{aligned}
\frac{D(a)}{\pi^2}
&=\frac23(N+t)^3-N(N+t)^2
  +\frac{N(N+1)(2N+1)}6\\
&=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
\end{aligned} \tag{P4}
$$

Subtracting $\frac25(N+t)^2$ and completing the square yields the exact
screen

$$
\frac{D(a)}{\pi^2}-\frac25\left(\frac a\pi\right)^2
=
\frac{N^2}{10}
+N\left[\left(t-\frac25\right)^2+\frac1{150}\right]
+\frac{2t^3}{3}-\frac{2t^2}{5}. \tag{2.3}
$$

For

$$
h(t)=\frac{2t^3}{3}-\frac{2t^2}{5},
$$

one has $h'(t)=2t(t-2/5)$. Hence the unique interior minimum on
$0<t\leq1$ is

$$
h(2/5)=-\frac8{375}.
$$

Consequently

$$
\frac{D(a)}{\pi^2}-\frac25\left(\frac a\pi\right)^2
\geq\frac{N^2}{10}+\frac{N}{150}-\frac8{375}.
\tag{P6}
$$

The right side is increasing for integers $N\geq1$, and at $N=1$ it is

$$
\frac1{10}+\frac1{150}-\frac8{375}
=\frac{32}{375}>0.
$$

Thus, analytically and without sampling,

$$
D(a)>\frac25a^2\qquad(a>\pi). \tag{P5}
$$

At a radial wall $a=m\pi$, let $p=m-1$. The left limit and the wall use
$(N,t)=(p,1)$, while the right limit uses $(N,t)\to(p+1,0^+)$. Formula
(P4) gives on both sides

$$
\frac{p^2}{2}+\frac{7p}{6}+\frac23.
$$

Thus $D$ and (P4) are continuous at every radial wall. The strict product
count itself has the correct one-sided behavior: the $n=m,\ell=0$ term is
absent at the wall and appears immediately to its right.

### 2.3. Ceiling cost, (P7)--(P9)

For $z\geq0$, $\lceil z\rceil<z+1$. Applied to $M_n$ and then squared
(both sides are nonnegative), this gives

$$
\begin{aligned}
\varepsilon^2M_n^2
&<
\left(\sqrt{b_n^2+\frac{\varepsilon^2}{4}}+\frac\varepsilon2\right)^2\\
&\leq b_n^2+\varepsilon b_n+\varepsilon^2.
\end{aligned} \tag{2.4}
$$

The second inequality uses
$\sqrt{b_n^2+\varepsilon^2/4}\leq b_n+\varepsilon/2$; it is valid at every
ceiling wall and no equality can erase the first strict inequality.
Since $x\mapsto\sqrt{a^2-x^2}$ is decreasing,

$$
\pi\sum_{n=1}^N b_n
\leq\int_0^a\sqrt{a^2-x^2}\,dx
=\frac{\pi a^2}{4},
\qquad
N<\frac a\pi.
$$

Summing (2.4) therefore yields

$$
\varepsilon^2\mathcal P_\varepsilon(a)
<
S_0(a)+\frac{\varepsilon a^2}{4}
+\frac{\varepsilon^2a}{\pi}. \tag{2.5}
$$

It is sufficient that

$$
D(a)\geq
\varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}, \tag{P7}
$$

because (2.5) would then be strictly less than
$I_0(a)(1-\varepsilon)$.

On the low piece, for $a\geq\pi$,

$$
\frac{2\varepsilon a}{3\pi}\leq\frac16,
\qquad
\frac{\varepsilon^2}{\pi a}
\leq\frac{\varepsilon^2}{\pi^2}
<\frac{\varepsilon^2}{9},
$$

where the first inequality uses $a\leq\pi/(4\varepsilon)$ and the second
uses $\pi>3$. Hence

$$
\varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}
\leq
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
\tag{P8}
$$

The coefficient on the right increases with $\varepsilon$. At
$\varepsilon=1/8$ its reserve below $2/5$ is exactly

$$
\frac25-
\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0. \tag{P9}
$$

Thus (P5) proves (in fact strictly) the sufficient condition (P7) for
$a>\pi$ throughout the inclusive low piece. Combining (2.5)--(P9),

$$
\varepsilon^2\mathcal P_\varepsilon(a)
<I_0(a)(1-\varepsilon)
<I_0(a)\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right)
\qquad(a>\pi).
\tag{2.6}
$$

For $0<a\leq\pi$, (2.2) gives the same final strict comparison directly.
Together with (P1), the low piece proves

$$
N_D(A_{\rho,1},K^2)
<
\frac{2a^3}{3\pi\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right)
\qquad(K>0). \tag{2.7}
$$

All estimates in this subsection allow
$a=\pi/(4\varepsilon)$. Hence the low proof owns the common optical face.

## 3. High complementary-action piece

This section independently proves (2.7) on the inclusive piece

$$
a\geq\frac{\pi}{4\varepsilon}.
$$

In particular $a\geq2\pi$, so the radial proxy sum below is nonempty.

### 3.1. Exact action, inverse, curvature, and (H1)--(H3)

For $r\in\{\rho,1\}$,

$$
J_r(y)=\sqrt{a^2r^2-y^2}
-y\arccos\frac{y}{ar}
$$

satisfies

$$
J_r'(y)=-\arccos\frac{y}{ar}.
$$

Consequently the piecewise definition

$$
\mathcal A(y)=
\begin{cases}
\dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
&0\leq y\leq\rho a,\\[5pt]
\dfrac{J_1(y)}{\pi\varepsilon},
&\rho a\leq y\leq a
\end{cases} \tag{H1}
$$

is continuous, and its first derivatives agree at $y=\rho a$:

$$
\mathcal A'(\rho a\pm)
=-\frac{\arccos\rho}{\pi\varepsilon}.
$$

For $0<y<\rho a$, set

$$
\delta(y)=\arccos(y/a)-\arccos(y/(\rho a)).
$$

Then

$$
\delta'(y)=
\frac1{\sqrt{\rho^2a^2-y^2}}
-\frac1{\sqrt{a^2-y^2}}>0,
$$

and

$$
\delta''(y)=
\frac{y}{(\rho^2a^2-y^2)^{3/2}}
-\frac{y}{(a^2-y^2)^{3/2}}>0.
$$

Since $\delta(0)=0$,

$$
y\delta'(y)-\delta(y)
=\int_0^y s\delta''(s)\,ds>0. \tag{3.1}
$$

On the inner interval
$\mathcal A'=-\delta/(\pi\varepsilon)<0$ and
$\mathcal A''=-\delta'/(\pi\varepsilon)<0$. On the outer interval,

$$
\mathcal A'(y)=-\frac{\arccos(y/a)}{\pi\varepsilon}<0,
\qquad
\mathcal A''(y)=\frac1{\pi\varepsilon\sqrt{a^2-y^2}}>0.
$$

Thus $\mathcal A$ is strictly decreasing from

$$
T=\mathcal A(0)=\frac a\pi
$$

to $\mathcal A(a)=0$. It has a continuous decreasing inverse
$R:[0,T]\to[0,a]$. Put

$$
\tau=\mathcal A(\rho a),\qquad F(t)=R(t)^2,\qquad g(t)=-F'(t).
$$

If $t=\mathcal A(y)$, then

$$
g(t)=-\frac{2y}{\mathcal A'(y)}>0,
\qquad
\frac{dg}{dt}
=-\frac{2(\mathcal A'-y\mathcal A'')}{(\mathcal A')^3}. \tag{3.2}
$$

On the outer interval, $\mathcal A'-y\mathcal A''<0$, so $g$ decreases
for $0<t<\tau$. On the inner interval, (3.1) gives

$$
\mathcal A'-y\mathcal A''
=\frac{-\delta+y\delta'}{\pi\varepsilon}>0,
$$

so $g$ increases for $\tau<t<T$. This proves (H2) at the actual,
ungridded curvature interface:

$$
g\ \hbox{decreases on }(0,\tau),\qquad
g\ \hbox{increases on }(\tau,T). \tag{H2}
$$

The endpoint and interface values are

$$
F(0)=a^2,\qquad F(\tau)=\rho^2a^2,\qquad F(T)=0. \tag{3.3}
$$

As $y\downarrow0$,

$$
\delta(y)=\frac{\varepsilon}{\rho a}y+O(y^3),
\qquad
\mathcal A'(y)=-\frac{y}{\pi\rho a}+O(y^3),
$$

and therefore

$$
g(T)=2\pi\rho a. \tag{H3}
$$

At the interface
$g(\tau)=2\pi\varepsilon\rho a/\arccos\rho>0$. The second derivative may
have a one-sided singularity there, but $\mathcal A$, $\mathcal A'$, $R$,
$F$, and $g$ are continuous, which is exactly what the Stieltjes split uses.

At the improper outer endpoint, write $s=a-y$. Since

$$
\arccos(1-s/a)\sim\sqrt{2s/a},
\qquad
J_1(a-s)\sim\frac{2\sqrt2}{3\sqrt a}s^{3/2},
$$

one has $t\asymp s^{3/2}$ and $g(t)\asymp t^{-1/3}$. In particular $g$
is integrable at zero and, because $W(t)=t^2/2$ near zero,

$$
\lim_{t\downarrow0}W(t)g(t)=0. \tag{3.4}
$$

This is the required improper trace; no finite value for $g(0)$ is assumed.

### 3.2. Layer cake and the domain-free identities (N1)--(N3)

Extend $\mathcal A(y)=0$ for $y>a$, and put

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),\qquad
q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<.
$$

For $x_n=n-1/4$,

$$
q_\ell
=\#\{n\geq1:x_n<\mathcal A(y_\ell)\}.
$$

Thus the strict bracket excludes every phase-proxy wall
$\mathcal A(y_\ell)+1/4\in\mathbb Z$. The extension makes $q_\ell=0$
once $y_\ell\geq a$, including $y_\ell=a$, so all sums are finite. Define

$$
P_{\mathcal A}=\varepsilon\sum_{\ell\geq0}y_\ell q_\ell. \tag{N1}
$$

For $x>0$ the exact half-integer count is

$$
M_\varepsilon(x)
=\#\{\ell\geq0:\varepsilon(\ell+1/2)<x\}
=\max\left\{0,\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil\right\}.
\tag{H6}
$$

Swapping the two finite strict sums, using the monotonic equivalence
$x_n<\mathcal A(y_\ell)\iff y_\ell<R(x_n)$, and summing
$\sum_{\ell=0}^{M-1}(\ell+1/2)=M^2/2$, gives

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\geq1\\x_n<T}}
M_\varepsilon(R(x_n))^2. \tag{3.5}
$$

This rederives the discrete identity in (N2), including all strict walls.

For the continuous normalization, $t=\mathcal A(y)$ gives

$$
\begin{aligned}
\int_0^T F(t)\,dt
&=-\int_0^a y^2\mathcal A'(y)\,dy\\
&=\frac1{\pi\varepsilon}
\left[
\int_0^a y^2\arccos(y/a)\,dy
-\int_0^{\rho a}y^2\arccos(y/(\rho a))\,dy
\right].
\end{aligned}
$$

Integration by parts gives

$$
\int_0^1u^2\arccos u\,du=\frac29.
$$

Since $1-\rho^3=3\varepsilon-3\varepsilon^2+\varepsilon^3$,

$$
I:=\frac12\int_0^T F(t)\,dt
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right). \tag{N2}
$$

The only phase result used is the permitted all-domain transfer

$$
N_D(A_{\rho,1},K^2)\leq\frac{2P_{\mathcal A}}{\varepsilon^2}.
$$

Its normalization is independently checked:

$$
\frac{2I}{\varepsilon^2}
=\frac{2a^3}{3\pi\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right)
=\frac{2}{9\pi}(1-\rho^3)K^3. \tag{N3}
$$

No domain-sensitive estimate is contained in this transfer; the remaining
task is precisely $P_{\mathcal A}<I$.

### 3.3. Exact sawtooth and the ungridded Stieltjes split, (H4)--(H5)

Let

$$
C(t)=\#\{n\geq1:n-1/4<t\},\qquad
w(t)=t-C(t),\qquad W(t)=\int_0^t w(s)\,ds,
$$

and $\Psi(t)=W(t)-t/4$. On the first interval $0\leq t\leq3/4$,

$$
\Psi(t)=\frac{t^2}{2}-\frac t4
=\frac12\left(t-\frac14\right)^2-\frac1{32}.
$$

For $x_n=n-1/4$ and $t=x_n+u$, $0\leq u\leq1$,

$$
\Psi(t)=\frac12\left(u-\frac12\right)^2-\frac1{32}.
$$

These formulas agree at cell endpoints. Hence, globally,

$$
-\frac1{32}\leq\Psi(t)\leq\frac3{32},
\qquad W(t)\geq0. \tag{H4}
$$

At a sawtooth jump $x_n$, strict counting gives
$w(x_n)=w(x_n^-)=3/4$ and $w(x_n^+)=-1/4$; $W$ and $\Psi$ remain
continuous. Thus both sides of every jump, including a split point
$\tau=x_n$, are owned by the same formulas.

Define

$$
D_{\rm rad}
=\int_0^T F(t)\,dt
-\sum_{\substack{n\geq1\\x_n<T}}F(x_n).
$$

In Lebesgue--Stieltjes form, the atoms of $dC$ are the $x_n$. If
$x_n=T$, that atom is excluded by convention and would in any case carry
$F(T)=0$. Integration by parts therefore gives exactly

$$
D_{\rm rad}=\int_0^T w(t)g(t)\,dt.
$$

Apply Stieltjes integration by parts first on $[\eta,\tau]$ and
$[\tau,T]$, then let $\eta\downarrow0$. By (3.4), the improper boundary
term vanishes, and continuity at $\tau$ cancels the two interface terms:

$$
D_{\rm rad}
=W(T)g(T)
-\int_0^\tau W\,dg
-\int_\tau^T W\,dg. \tag{3.6}
$$

On $(0,\tau)$, $dg\leq0$ and $W\geq0$, so the first Stieltjes integral
appears with a nonnegative sign and may be dropped. This works whether
$\tau<1$, $\tau=1$, or $\tau>1$, and whether $\tau$ lies below, on, or
above any sawtooth grid point.

On $[\tau,T]$, use $W=t/4+\Psi$. Since $dg\geq0$,

$$
\begin{aligned}
W(T)g(T)-\int_\tau^T W\,dg
&=\frac{\rho^2a^2}{4}
+\frac{\tau g(\tau)}4+\Psi(T)g(T)
-\int_\tau^T\Psi\,dg\\
&\geq
\frac{\rho^2a^2}{4}
-\frac{g(T)}{32}
-\frac3{32}\bigl(g(T)-g(\tau)\bigr)
+\frac{\tau g(\tau)}4\\
&=
\frac{\rho^2a^2}{4}-\frac{g(T)}8
+g(\tau)\left(\frac\tau4+\frac3{32}\right)\\
&\geq
\frac{\rho^2a^2}{4}-\frac{g(T)}8.
\end{aligned}
$$

Here $\int_\tau^Tg\,dt=F(\tau)-F(T)=\rho^2a^2$ was used in the first
line. The two explicitly dropped nonnegative quantities are
$-\int_0^\tau W\,dg$ and
$g(\tau)(\tau/4+3/32)$. With (H3), this proves

$$
D_{\rm rad}
\geq\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}. \tag{H5}
$$

No first-cell argument and no assumption $\tau>1$ has entered.

### 3.4. Strict radial and angular errors, (H6)--(H8)

Let

$$
J_{\rm rad}=\#\{n\geq1:x_n<T\}.
$$

Since the number of positive integers strictly below $T+1/4$ is
$[T+1/4]_<$,

$$
J_{\rm rad}<T+\frac14=\frac a\pi+\frac14. \tag{H7}
$$

This is exact at every wall $x_n=T$ and uses no lower bound such as
$a\geq125$.

For every included $x_n<T$, put $x=R(x_n)>0$. Formula (H6) gives

$$
M_\varepsilon(x)<\frac{x}{\varepsilon}+\frac12.
$$

Both sides are nonnegative, so

$$
\varepsilon^2M_\varepsilon(x)^2
<x^2+\varepsilon x+\frac{\varepsilon^2}{4}
\leq x^2+\varepsilon a+\frac{\varepsilon^2}{4}. \tag{3.7}
$$

At a half-integer wall $x/\varepsilon=m+1/2$, (H6) gives $M=m$ and
excludes the wall; (3.7) remains strict. Since on the high piece
$T\geq2$, the radial sum is nonempty. Summing (3.7) and then using the
strict (H7) gives

$$
\varepsilon^2
\sum_{\substack{n\geq1\\x_n<T}}M_\varepsilon(R(x_n))^2
<
\sum_{\substack{n\geq1\\x_n<T}}F(x_n)+E, \tag{3.8}
$$

where the complete angular error is strictly bounded using

$$
E=
\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right). \tag{H8}
$$

### 3.5. Uniform high screens and (H9)--(H12)

Since $a\geq\pi/(4\varepsilon)$ and $\rho=1-\varepsilon$,

$$
\frac{D_{\rm rad}}{a^2}
\geq\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
\geq\frac{(1-\varepsilon)(1-5\varepsilon)}4. \tag{H9}
$$

The lower screen
$L(\varepsilon)=(1-\varepsilon)(1-5\varepsilon)/4$ has
$L'(\varepsilon)=(-6+10\varepsilon)/4<0$ on
$0<\varepsilon\leq1/8$. Hence

$$
L(\varepsilon)\geq L(1/8)=\frac{21}{256}.
$$

Expanding (H8) and using $1/a\leq4\varepsilon/\pi$ gives

$$
\frac{E}{a^2}
\leq
\frac\varepsilon\pi+\frac{\varepsilon^2}{\pi}
+\frac{\varepsilon^3}{\pi^2}+\frac{\varepsilon^4}{\pi^2}.
\tag{H10}
$$

This scaling is deliberately non-strict: all four substitutions are
equalities at $a=\pi/(4\varepsilon)$. Its right side is strictly increasing,
because its derivative is

$$
\frac{1+2\varepsilon}{\pi}
+\frac{3\varepsilon^2+4\varepsilon^3}{\pi^2}>0.
$$

At $\varepsilon=1/8$, $\pi>3$ yields the strict exact bound

$$
\frac9{64\pi}+\frac9{4096\pi^2}
<\frac3{64}+\frac1{4096}
=\frac{193}{4096}.
$$

The endpoint reserve is therefore

$$
\frac{21}{256}-\frac{193}{4096}
=\frac{143}{4096}>0. \tag{H11}
$$

Thus $D_{\rm rad}>E$ everywhere on the inclusive high piece, including
the common face and the closed $\varepsilon=1/8$ face. Combining this
strict inequality with (3.8) gives, rather than assumes,

$$
\varepsilon^2
\sum_{\substack{n\geq1\\x_n<T}}M_\varepsilon(R(x_n))^2
<
\sum_{\substack{n\geq1\\x_n<T}}F(x_n)+E
<
\int_0^T F(t)\,dt. \tag{H12}
$$

By (3.5), (N2), and (H12), $P_{\mathcal A}<I$. The permitted transfer
(N3) then proves (2.7) strictly for $K>0$ on the high piece.

## 4. Closed union and the frozen endpoint

For fixed $0<\varepsilon\leq1/8$, the two relative-closed sets

$$
\left[0,\frac{\pi}{4\varepsilon}\right],
\qquad
\left[\frac{\pi}{4\varepsilon},\infty\right)
$$

cover every $a\geq0$ and overlap at exactly the required optical face.
Both proofs include that face. At the corner

$$
(\varepsilon,a)=\left(\frac18,2\pi\right)
$$

the low proof uses the radial-wall convention $(N,t)=(1,1)$, while the
high proof allows equality in the scaling step (H10); both retain a strict
final reserve.

Since

$$
1-\rho^3=3\varepsilon-3\varepsilon^2+\varepsilon^3,
\qquad K=\frac a\varepsilon,
$$

(2.7) is exactly

$$
N_D(A_{\rho,1},K^2)
<
\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K>0).
$$

Together with equality $0=0$ at $K=0$, this proves the requested non-strict
inequality for

$$
\boxed{\frac78\leq\rho<1,\qquad K\geq0.}
$$

The lower ratio face $\rho=7/8$ is owned because
$\varepsilon=1/8$ is closed. The limit $\rho\uparrow1$ is covered for
every positive $\varepsilon$, but $\varepsilon=0$ is never inserted into a
denominator or treated as part of the domain.

## 5. Six dependency replacements

All six mandated replacements are explicit in the proof:

1. The Stieltjes argument uses global $W\geq0$ and splits at the actual
   $\tau$; it never assumes $\tau>1$ or invokes a special first cell.
2. The angular error uses the exact
   $J_{\rm rad}<a/\pi+1/4$; neither $a\geq125$ nor a count below $a/2$
   appears.
3. The high lower screen substitutes exactly
   $\rho=1-\varepsilon$, not $\rho\geq99/100$.
4. The high reserve is exactly $143/4096$, not the old $61/1400$.
5. The low proof uses the exact zero range $0\leq a\leq\pi$ and the
   uniform deficit $D>(2/5)a^2$, not an old three-slab estimate.
6. The two inclusive pieces themselves form the complete union. No Round 6
   aggregate theorem is quoted, extended, or concealed.

There is likewise no hidden use of $\varepsilon\leq1/100$,
$\rho\geq99/100$, $a\geq125$, or an old bridge scale.

## 6. Independent exact arithmetic ledger

The following calculations were performed symbolically.

1. Formula (P4) is the exact polynomial expansion

   $$
   \frac23(N+t)^3-N(N+t)^2+\frac{N(N+1)(2N+1)}6
   =
   \frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
   $$

2. The cubic remainder in (P6) has minimum
   $h(2/5)=-8/375$, and the $N=1$ lower bound is
   $32/375>0$.

3. The low endpoint reserve is

   $$
   \frac25-\frac16-\frac1{32}-\frac1{576}
   =\frac{577}{2880}.
   $$

4. The high lower endpoint is
   $(7/8)(3/8)/4=21/256$. The upper endpoint satisfies

   $$
   \frac9{64\pi}+\frac9{4096\pi^2}
   <\frac{192}{4096}+\frac1{4096}
   =\frac{193}{4096},
   $$

   and

   $$
   \frac{21}{256}-\frac{193}{4096}
   =\frac{143}{4096}.
   $$

For the planning screens, define the exact rational functions

$$
R_P(e)=\frac25-\frac16-\frac e4-\frac{e^2}{9},
$$

and, for a certified rational lower bound $p<\pi$,

$$
R_H(e;p)=
\frac{(1-e)(1-5e)}4
-\frac{e+e^2}{p}
-\frac{e^3+e^4}{p^2}.
$$

Then direct fraction reduction gives all of (S1)--(S4):

$$
R_P(1/7)=\frac{1723}{8820},
\qquad
R_H(1/7;3)=\frac{139}{21609};
$$

$$
R_P(4/27)=\frac{12719}{65610},
\qquad
R_H(4/27;333/106)
=\frac{162570113}{235723844196};
$$

$$
R_H(3/20;333/106)
=-\frac{44729}{20535000};
$$

and

$$
R_H(1/6;333/106)
=-\frac{3983743}{143712144}.
$$

The positive values are only planning arithmetic and are not promoted below
$\rho=7/8$. The negative values say only that this selected rational lower
screen no longer proves positivity; they are not spectral counterexamples or
endpoint impossibility results.

Finally,

$$
\frac{200000}{295^2}
=\frac{200000}{87025}
=\frac{8000}{3481}
=2+\frac{1038}{3481}>2.
$$

## 7. Branch, wall, endpoint, and legality ledger

- **$K=0$ and $K>0$.** At $K=a=0$ both sides vanish. For $K>0$ both
  piecewise arguments produce a strict comparison before the final
  non-strict theorem statement.
- **Zero range and radial walls.** The exact range $0\leq a\leq\pi$ has
  no radial branch. At every $a=m\pi$, the $n=m$ level is excluded,
  $(N,t)=(m-1,1)$, the two one-sided formulas for (P4) agree, and the new
  $n=m,\ell=0$ product branch appears only immediately to the right.
- **Product angular walls.** At
  $b_n^2/\varepsilon^2=L(L+1)$, the $\ell=L$ level is excluded and
  $M_n=L$. Both one-sided counts and the first $\ell=0$ branch are handled
  by the same ceiling formula.
- **Optical face and corner.** Both pieces own
  $a=\pi/(4\varepsilon)$. At $(1/8,2\pi)$ it is also a radial wall; the
  low convention is $(N,t)=(1,1)$ and the high scaling equalities remain
  compatible with the strict $143/4096$ reserve.
- **Ratio and test faces.** The face $\varepsilon=1/8$ (that is,
  $\rho=7/8$) is included. The test faces
  $\varepsilon=1/100,1/25,1/10,1/8$ all lie in the proved domain and are
  governed by the same monotone screens. Their optical-face values are,
  respectively, $25\pi$, $25\pi/4$, $5\pi/2$, and $2\pi$. The limit
  $\varepsilon\downarrow0$ is open.
- **Action radial walls.** A wall $x_n=n-1/4=T$ is excluded in (N2),
  (H7), and (H12). Its hypothetical discrepancy contribution is
  $F(T)=0$, so the Stieltjes endpoint convention is also consistent.
- **Half-integer angular walls.** At
  $R(x_n)/\varepsilon=m+1/2$, (H6) gives $M_\varepsilon=m$ and excludes
  the wall. Both sides of every such jump retain the strict bound (3.7).
- **Phase-proxy walls.** At
  $\mathcal A(y_\ell)+1/4=m$, the strict bracket gives $q_\ell=m-1$.
  Thus the corresponding radial proxy layer is excluded, exactly as
  required.
- **Outer cutoff and inner interface.** At $y=a$, $\mathcal A=0$ and
  $q_\ell=0$ if a half-grid point lands there; for $y>a$ the extension is
  zero. At $y=\rho a$, the two formulas for $\mathcal A$ and
  $\mathcal A'$ agree. The curvature change occurs at the actual
  $t=\tau$, not at a grid surrogate.
- **Sawtooth placement.** The global formulas (H4) cover $\tau$ below,
  on, or above every grid point. At each jump $w$ has the recorded
  $3/4$ to $-1/4$ transition while $W$ and $\Psi$ are continuous.
- **Improper and terminal traces.** At $t=0$, $g\asymp t^{-1/3}$ and
  $Wg\to0$. At $t=T$, $F(T)=0$ and $g(T)=2\pi\rho a$. The only discarded
  Stieltjes terms are the two nonnegative quantities identified after
  (3.6).
- **Domains and elementary operations.** The inverse has exact domain
  $R:[0,T]\to[0,a]$. All divisions by $\varepsilon$, $a$, $\rho$, or
  $\mathcal A'$ occur only where the denominator is positive or nonzero.
  In the inner open interval, both square-root radicands are positive and
  both arccosine arguments lie in $(0,1)$; at the interface and endpoints
  their limits are taken explicitly. In the outer open interval the same
  statements hold for $y/a$. Every squaring in the ceiling bounds is
  between nonnegative quantities. No inequality is reversed by an
  unrecorded sign.
- **Monotonic reductions.** The coefficient in (P8) increases with
  $\varepsilon$; the lower side of (H9) decreases; and the upper side of
  (H10) increases. Equality in the $a$-scaling of (H10) is retained at
  the common face.

The strongest exact domain proved is therefore the full frozen domain and
not a shifted one:

$$
0<\varepsilon\leq1/8,\quad a\geq0,
$$

equivalently $7/8\leq\rho<1$, $K\geq0$. No conclusion is asserted for a
smaller ratio.

## 8. Separate conditional-envelope audit

This section does not feed back into Sections 2--4. It uses the Round 15
boundary facts recorded in the packet only after the endpoint proof above.
Write

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,\qquad
C_*=\frac12+\frac{8\sqrt2}{15},\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

First, the interfaces are correctly ordered:

$$
0<\rho_*<\frac1{16}<\frac56<\frac78<\frac{99}{100}<1.
$$

For completeness, positivity of $\rho_*$ follows from the standard exact
bound $\pi<22/7<3\sqrt3$. Also
$\omega_0<1/6$ from $\pi>3$ and $\sqrt3<2$, while
$1+2C_*>46/15$ from $\sqrt2>1$; hence
$\rho_*<5/92<1/16$.

Conditioned on promotion of the new endpoint, the remaining coarse envelope
has the following exact ownership:

1. On $[\rho_*,1/16]$, the residual has $K<64$, so the equality
   $K=64$ is already covered.
2. On $[1/16,5/6]$, the residual has
   $K<K_0(5/6)<295^2=87025$. Therefore $K=295^2$, not merely larger
   $K$, is covered. The strict residual inequality also means that the
   threshold face $K=K_0(5/6)$ itself is covered.
3. On $[5/6,7/8]$, the accepted threshold includes equality and

   $$
   \frac{54}{(1-\rho)^2}\leq\frac{54}{(1/8)^2}=3456.
   $$

   Thus $K=3456$ is covered; at $\rho=5/6$ the same formula gives the
   smaller equality threshold $1944$.
4. On $[7/8,1)$, the newly proved endpoint supplies all frequencies,
   including both $K=0$ and all threshold faces.

The adjacent intervals deliberately overlap at
$\rho=\rho_*,1/16,5/6,7/8$. At $\rho=99/100$, the new endpoint and the
accepted old thin endpoint overlap. The accepted all-ratio face
$K=200000$ is preserved and becomes redundant for this conditional ceiling.
The sharper accepted equality faces remain on their exact domains:

$$
\varepsilon=\frac18,\ K=\frac{32}{\varepsilon^2}=2048;
\qquad
\varepsilon=\frac1{10},\ K=\frac{24}{\varepsilon^2}=2400;
\qquad
\varepsilon=\frac1{25},\ K=\frac{20}{\varepsilon^2}=12500.
$$

The general accepted threshold $K=54/\varepsilon^2$ also retains equality
on $0<\varepsilon\leq1/6$. None of these accepted faces was used to prove
the new endpoint.

Because $87025>64$ and $87025>3456$, and because the middle residual is
strictly below $K_0(5/6)<87025$, the equality face is owned in every
ratio band. Thus the separately audited implication is exactly the
conditional statement

$$
0<\rho<1,\qquad K\geq295^2=87025.
$$

Its reduction factor is the exact value $8000/3481>2$ calculated in
Section 6. This remains conditional on the external promotion gates; it
does not replace the true bounded residual by a rectangle, close
SHELL-rho-compact, SHELL-rho-uniformity, or TARGET-shell-d3, or promote
COMP-certified-bessel beyond diagnostic_only.
