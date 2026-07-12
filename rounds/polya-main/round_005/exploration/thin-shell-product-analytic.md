# Thin-shell product comparison: a rigorous low-width range and an exact obstruction

## Verdict

Let $0<\epsilon<1$, $a=\epsilon K>\pi$, and

\[
P(\epsilon,a)=\sum_{n\pi<a}(L_n+1)^2,
\qquad
L_n=\max\left\{\ell\in\mathbb Z_{\ge0}:
\ell(\ell+1)<\frac{a^2-n^2\pi^2}{\epsilon^2}\right\}.
\]

The desired product comparison is

\[
P(\epsilon,a)\le W_\epsilon(a),
\qquad
W_\epsilon(a):=
\frac{2}{9\pi}\bigl(1-(1-\epsilon)^3\bigr)
\frac{a^3}{\epsilon^3}.
\tag{1}
\]

There is a nontrivial explicit range in which (1) is true:

\[
\boxed{
0<\epsilon\le \frac1{16},\quad
\pi<a\le \frac{\pi}{8\epsilon}
\quad\Longrightarrow\quad
P(\epsilon,a)<W_\epsilon(a).}
\tag{2}
\]

However, the product comparison cannot cover all $a>\pi$, for any positive
choice of $\epsilon_0$. More precisely, for every $0<\epsilon<1$ and every
integer

\[
Q>\frac{2}{\epsilon},
\]

the exact radial wall $a=Q\pi$ satisfies the strict reverse inequality

\[
\boxed{P(\epsilon,Q\pi)>W_\epsilon(Q\pi).}
\tag{3}
\]

Thus there are infinitely many counterexamples for every fixed $\epsilon>0$.
The exact sufficient wall threshold derived below is asymptotic to
$3/(4\epsilon)$, so the sharp transition scale of the product proxy is
$a\sim3\pi/(4\epsilon)$.
This is an obstruction to this product proxy, not a counterexample to the shell
Polya conjecture itself.

The obstruction also occurs strictly below the existing fixed-$\rho$
high-energy threshold $K_0(\rho)$ when $\rho=1-\epsilon$. Consequently, the
two estimates cannot be joined as "product comparison below, Round 3 theorem
above"; a third estimate or a certified intermediate region is necessary.

## Spectral promotion of the positive range

The proved Round 4 direct-sum decomposition makes the positive proxy result a
genuine shell counting result. Indeed, on the Dirichlet interval
$(1-\epsilon,1)$, the radial block is

\[
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}.
\]

Since $r^{-2}\ge1$, its quadratic form satisfies

\[
L_\ell\ge
-\frac{d^2}{dr^2}+\ell(\ell+1).
\]

The comparison operator has eigenvalues
$(n\pi/\epsilon)^2+\ell(\ell+1)$. The min--max principle therefore gives,
with radial eigenvalues indexed increasingly inside each angular channel,

\[
\lambda_{\ell,n}(1-\epsilon)
\ge
\left(\frac{n\pi}{\epsilon}\right)^2+\ell(\ell+1).
\]

Consequently, preserving the strict spectral endpoint,

\[
\begin{aligned}
N_D(A_{1-\epsilon,1},K^2)
&=\sum_{\ell\ge0}\sum_{n\ge1}(2\ell+1)
\mathbf 1_{\{\lambda_{\ell,n}<K^2\}}\\
&\le
\sum_{\ell\ge0}\sum_{n\ge1}(2\ell+1)
\mathbf 1_{\{(n\pi/\epsilon)^2+\ell(\ell+1)<K^2\}}\\
&=P(\epsilon,\epsilon K).
\end{aligned}
\]

The last equality follows by summing first over $\ell$:
$\sum_{\ell=0}^{L_n}(2\ell+1)=(L_n+1)^2$. Accidental coincidences between
different angular channels cause no issue, because the Round 4 orthogonal
direct sum adds their multiplicities.

Thus (2), together with the exact zero region $0\le a\le\pi$, proves the
actual shell Polya inequality for

\[
0<\epsilon\le\frac1{16},
\qquad
0\le \epsilon K\le\frac{\pi}{8\epsilon}.
\]

Only the reverse inequality (3) is proxy-specific: $P>W_\epsilon$ says that
this comparison method has failed, not that the true shell count violates the
Polya bound.

## 1. Strict walls and exact angular rounding

Put

\[
t=\frac a\pi,
\qquad
N=\#\{n\in\mathbb Z_{\ge1}:n<t\}=\lceil t\rceil-1,
\qquad
\delta=t-N\in(0,1].
\tag{4}
\]

The convention $\delta=1$ when $t$ is an integer is important: at the wall
$a=Q\pi$, the strict condition $n\pi<a$ gives $N=Q-1$, not $Q$.

For $1\le n\le N$, write

\[
B_n=\frac{a^2-n^2\pi^2}{\epsilon^2}>0,
\qquad M_n=L_n+1.
\]

Solving the quadratic inequality with its strict endpoint gives the exact
formula

\[
M_n=
\left\lceil \sqrt{B_n+\frac14}-\frac12\right\rceil.
\tag{5}
\]

In particular, if $B_n=\ell(\ell+1)$, then (5) gives $M_n=\ell$, as it
must: the value $\ell$ is excluded by the strict inequality defining $L_n$.

For arbitrary $B>0$, set

\[
M(B)=\left\lceil \sqrt{B+\frac14}-\frac12\right\rceil,
\qquad R=\sqrt{B+\frac14}.
\]

Then

\[
R-\frac12\le M(B)<R+\frac12,
\qquad
0<R-\sqrt B<\frac12.
\]

Squaring and using the second strict inequality yields the endpoint-safe bounds

\[
\boxed{B-\sqrt B<M(B)^2<B+\sqrt B+1.}
\tag{6}
\]

Define

\[
S_0=\sum_{n=1}^N(a^2-n^2\pi^2),
\qquad
S_1=\sum_{n=1}^N\sqrt{a^2-n^2\pi^2},
\qquad
C=\frac{2a^3}{3\pi}=\frac{2\pi^2t^3}{3}.
\tag{7}
\]

Summing (6) gives the strict two-sided enclosure

\[
\boxed{
\frac{S_0}{\epsilon^2}-\frac{S_1}{\epsilon}
<P(\epsilon,a)<
\frac{S_0}{\epsilon^2}+\frac{S_1}{\epsilon}+N.}
\tag{8}
\]

Meanwhile the right side of (1) is

\[
W_\epsilon(a)
=\frac{C}{\epsilon^2}
\left(1-\epsilon+\frac{\epsilon^2}{3}\right).
\tag{9}
\]

## 2. Exact radial deficit

The quadratic sum is elementary:

\[
S_0
=\pi^2\left(
Nt^2-\frac{N(N+1)(2N+1)}6
\right).
\tag{10}
\]

Substituting $t=N+\delta$, including the wall convention in (4), gives the
exact deficit

\[
\begin{aligned}
D:=C-S_0
&=\pi^2\left[
\frac{N^2}{2}
+N\left(\delta^2+\frac16\right)
+\frac{2\delta^3}{3}
\right] \\
&\ge \frac{\pi^2N^2}{2}.
\end{aligned}
\tag{11}
\]

The square-root sum has the simple integral bound

\[
\begin{aligned}
S_1
&=\pi\sum_{n=1}^N\sqrt{t^2-n^2} \\
&\le \pi\int_0^t\sqrt{t^2-x^2}\,dx
=\frac{\pi^2t^2}{4}.
\end{aligned}
\tag{12}
\]

Indeed $x\mapsto\sqrt{t^2-x^2}$ is decreasing, so each right-endpoint term
is bounded by the integral over its unit interval; extending the resulting
integral to $[0,t]$ only increases it.

## 3. Proof of the explicit positive range

Assume throughout this section that

\[
0<\epsilon\le\frac1{16},
\qquad 1<t\le\frac1{8\epsilon}.
\tag{13}
\]

This is exactly the range in (2).

### 3.1. The first radial band: $1<t\le2$

Here the strict radial count is $N=1$, including at $t=2$. From (8),

\[
P(\epsilon,a)
<\frac{\pi^2(t^2-1)}{\epsilon^2}
+\frac{\pi\sqrt{t^2-1}}{\epsilon}+1
\le
\frac{\pi^2(t^2-1)}{\epsilon^2}
+\frac{\pi t}{\epsilon}+1.
\]

Therefore, using (9) and discarding the positive $\epsilon^2/3$ contribution
in its coefficient,

\[
\begin{aligned}
\epsilon^2(W_\epsilon-P)
&>\pi^2\left[
\frac{2t^3}{3}\left(1-\epsilon+\frac{\epsilon^2}{3}\right)
-(t^2-1)
\right]-\epsilon\pi t-\epsilon^2 \\
&\ge
\pi^2\left(\frac{2t^3}{3}-t^2+1\right)
-\epsilon\left(\frac{2\pi^2t^3}{3}+\pi t\right)-\epsilon^2.
\end{aligned}
\tag{14}
\]

The function $2t^3/3-t^2+1$ is increasing on $[1,2]$ and has value
$2/3$ at $t=1$. Thus (14), $t\le2$, and $\epsilon\le1/16$ give

\[
\begin{aligned}
\epsilon^2(W_\epsilon-P)
&>\frac{2\pi^2}{3}
-\epsilon\left(\frac{16\pi^2}{3}+2\pi\right)-\epsilon^2 \\
&\ge \frac{\pi^2}{3}-\frac\pi8-\frac1{256}>0.
\end{aligned}
\tag{15}
\]

The final positivity already follows from $3<\pi<4$.

### 3.2. All later bands under $\epsilon t\le1/8$

Suppose $t\ge2$. Then $N\ge t/2$, so (11) gives

\[
D\ge\frac{\pi^2t^2}{8}.
\tag{16}
\]

Combining (8), (9), and $S_0=C-D$,

\[
\epsilon^2(W_\epsilon-P)
>D-C\epsilon\left(1-\frac\epsilon3\right)
-\epsilon S_1-\epsilon^2N.
\tag{17}
\]

The assumptions $\epsilon t\le1/8$, $\epsilon\le1/16$, together with
(12) and $N<t$, imply

\[
C\epsilon\le\frac{\pi^2t^2}{12},
\qquad
\epsilon S_1\le\frac{\pi^2t^2}{64},
\qquad
\epsilon^2N<\epsilon^2t.
\tag{18}
\]

Consequently,

\[
\epsilon^2(W_\epsilon-P)
>\pi^2t^2\left(\frac18-\frac1{12}-\frac1{64}\right)
-\epsilon^2t
=\frac{5\pi^2t^2}{192}-\epsilon^2t>0.
\tag{19}
\]

For example, the last inequality follows immediately from $t\ge2$,
$\pi>3$, and $\epsilon\le1/16$. Since $1/(8\epsilon)\ge2$, the two
subsections cover all of (13), proving (2), with every radial and angular wall
treated by the strict conventions above.

## 4. Exact obstruction at radial walls

Fix any $0<\epsilon<1$, let $Q$ be a positive integer, and set

\[
a=Q\pi.
\]

Strict radial counting gives $n=1,\ldots,Q-1$. Equations (10)--(11) specialize
to

\[
S_0=C-D_Q,
\qquad
C=\frac{2\pi^2Q^3}{3},
\qquad
D_Q=\pi^2\left(\frac{Q^2}{2}+\frac Q6\right).
\tag{20}
\]

The integral estimate (12) is sharper here:

\[
S_1
=\pi\sum_{n=1}^{Q-1}\sqrt{Q^2-n^2}
\le\frac{\pi^2Q^2}{4}.
\tag{21}
\]

Use now the lower, rather than upper, half of (8). From (9), (20), and (21),

\[
\begin{aligned}
\epsilon^2(P-W_\epsilon)
&>C\epsilon\left(1-\frac\epsilon3\right)-D_Q-\epsilon S_1 \\
&>\frac{2\pi^2}{3}\epsilon\left(1-\frac\epsilon3\right)Q^3
-\pi^2\left(\frac{Q^2}{2}+\frac Q6\right)
-\frac{\epsilon\pi^2Q^2}{4}.
\end{aligned}
\tag{22}
\]

After division by $\pi^2Q$, positivity of the final line follows if

\[
\frac23\epsilon\left(1-\frac\epsilon3\right)Q^2
>
\left(\frac12+\frac\epsilon4\right)Q+\frac16.
\tag{23}
\]

Define the exact positive root of the quadratic equality in (23) by

\[
q_*(\epsilon)=
\frac{
\frac12+\frac\epsilon4+
\sqrt{\left(\frac12+\frac\epsilon4\right)^2+
\frac49\epsilon\left(1-\frac\epsilon3\right)}
}{
\frac43\epsilon\left(1-\frac\epsilon3\right)
}.
\tag{24}
\]

Thus every integer $Q>q_*(\epsilon)$ satisfies the strict reverse inequality
(3). This exact sufficient threshold has

\[
q_*(\epsilon)=\frac{3}{4\epsilon}+O(1)
\qquad(\epsilon\downarrow0).
\tag{25}
\]

For the simpler universal threshold stated in the verdict, note that the left
side of (23) is strictly larger than $(4/9)\epsilon Q^2$. If
$Q>2/\epsilon$, it is therefore larger than $8Q/9$. The right side is smaller
than $3Q/4+1/6<5Q/6$, because then $Q>2$. This proves (3) in particular for
every integer $Q>2/\epsilon$, and also shows from the quadratic sign that
$q_*(\epsilon)<2/\epsilon$.

It follows that no $\epsilon_0>0$ can make (1) valid for all
$0<\epsilon\le\epsilon_0$ and all $a>\pi$.

The mechanism is visible already at the level of orders. The leading product
volume is $C/\epsilon^2$, whereas (9) asks for

\[
\frac{C}{\epsilon^2}
\left(1-\epsilon+\frac{\epsilon^2}{3}\right).
\]

The missing shell-volume term is of order $a^3/\epsilon$. Eventually it
dominates both the radial discretization saving, of order $a^2/\epsilon^2$,
and angular rounding, of order $a^2/\epsilon$. Thus the obstruction is
structural rather than an artifact of a loose ceiling estimate.

The transition constant can also be read directly from (8). Rewriting (11)
in terms of $a$ and $\delta$ gives

\[
D=
\frac{a^2}{2}
+\pi a\left(\delta^2-\delta+\frac16\right)
+\pi^2\left(\frac{\delta^2}{2}-\frac{\delta^3}{3}-\frac\delta6\right)
=\frac{a^2}{2}+O(a),
\tag{26}
\]

uniformly for $0<\delta\le1$. Moreover, (8), (9), (12), and $N\le a/\pi$
show that, for fixed $c>0$ and $a=c/\epsilon$,

\[
\boxed{
\epsilon^2\bigl(P(\epsilon,c/\epsilon)-W_\epsilon(c/\epsilon)\bigr)
=
\frac1{\epsilon^2}
\left(\frac{2c^3}{3\pi}-\frac{c^2}{2}\right)
+O(\epsilon^{-1}).}
\tag{27}
\]

The leading coefficient changes sign exactly at

\[
\boxed{c_*=\frac{3\pi}{4}.}
\tag{28}
\]

Hence for each fixed $c>3\pi/4$, the product proxy is strictly above the
target at $a=c/\epsilon$ once $\epsilon$ is sufficiently small; for fixed
$c<3\pi/4$ it is strictly below there. Angular rounding contributes only to
the lower-order remainder and cannot move this leading transition.

## 5. No overlap with the existing $K_0(1-\epsilon)$ theorem

For $0<\epsilon\le1/2$, put $\rho=1-\epsilon$. The explicit Round 3
high-energy threshold has

\[
A_\rho=\frac{2\pi(1-\epsilon)}{\epsilon},
\qquad
\eta_\rho=G_1(1-\epsilon),
\qquad
C_0=1+\frac{8\sqrt2}{15},
\]

and

\[
K_0(\rho)=
\left(
\frac{\sqrt{A_\rho}+\sqrt{A_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2.
\tag{29}
\]

In particular,

\[
K_0(\rho)>\frac{A_\rho}{\eta_\rho^2}.
\tag{30}
\]

Here a convenient elementary estimate on $\eta_\rho$ is

\[
\eta_\rho<\frac{\epsilon^{3/2}}3.
\tag{31}
\]

For completeness, $G_1'(x)=-\pi^{-1}\arccos x$ and $G_1(1)=0$, so

\[
G_1(1-\epsilon)
=\frac1\pi\int_0^\epsilon\arccos(1-v)\,dv.
\]

For $0\le v\le1/2$,

\[
\arccos(1-v)=2\arcsin\sqrt{v/2}
\le\frac{2\pi}{3}\sqrt{v/2}.
\]

The inequality uses convexity of $\arcsin y$ on $0\le y\le1/2$ and the
secant from $(0,0)$ to $(1/2,\pi/6)$. Integration gives

\[
\eta_\rho\le\frac{2\sqrt2}{9}\epsilon^{3/2}
<\frac13\epsilon^{3/2},
\]

which proves (31).

Since $a=\epsilon K$, the high-energy theorem begins at

\[
\begin{aligned}
a_{\mathrm{HE}}
:=\epsilon K_0(1-\epsilon)
&>\epsilon\frac{A_\rho}{\eta_\rho^2} \\
&>\frac{18\pi(1-\epsilon)}{\epsilon^3}
\ge\frac{9\pi}{\epsilon^3}.
\end{aligned}
\tag{32}
\]

Now choose the first integer wall covered by the exact root criterion,

\[
Q_\epsilon=\lfloor q_*(\epsilon)\rfloor+1,
\qquad
a_{\mathrm F}=\pi Q_\epsilon.
\tag{33}
\]

Then $Q_\epsilon>q_*(\epsilon)$, so (3) holds at $a=a_{\mathrm F}$. Since
$q_*(\epsilon)<2/\epsilon$,

\[
a_{\mathrm F}
<\pi\left(\frac2\epsilon+1\right)
<\frac{9\pi}{\epsilon^3}
<a_{\mathrm{HE}}
\qquad(0<\epsilon\le1/2),
\tag{34}
\]

where the middle inequality is equivalent to
$2\epsilon^2+\epsilon^3<9$. Therefore an exact failure of the product
comparison occurs strictly before the existing analytic high-energy theorem
applies.

The scales delivered by the explicit estimates are thus

\[
\underbrace{a\le\frac{\pi}{8\epsilon}}_{\text{proved product range}},
\qquad
\underbrace{a_{\mathrm F}\sim\frac{3\pi}{4\epsilon}}_{\text{guaranteed proxy failure}},
\qquad
\underbrace{a_{\mathrm{HE}}>\frac{9\pi}{\epsilon^3}}_{\text{existing theorem threshold}}.
\]

Hence neither all-$a$ product coverage nor a two-piece overlap with
$K\ge K_0(1-\epsilon)$ is available from these ingredients.
