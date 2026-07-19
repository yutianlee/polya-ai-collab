# Clean-room review: thin-shell product comparison

## Verdict

**PASS.**  The claimed low-optical-width theorem and the claimed obstruction to the product-majorant route both follow from the permitted dependencies.  The radial and angular walls are treated with the strict convention throughout, all three positive-range estimates close with room to spare, and the product range does not overlap the already-proved fixed-\(\rho\) high-energy threshold as \(\rho\uparrow1\).

There is one harmless scope point in the displayed angular upper estimate: the strict inequality
\[
\mathcal P_\varepsilon(a)<S_0(a)/\varepsilon^2+B(a)/\varepsilon+N
\]
is used only when \(N\ge1\).  If \(N=0\), both sides are zero, and the range \(0\le a\le\pi\) is instead handled by the exact zero count.  Also, \(a/\pi=N+t\) is used only for \(a>0\); \(a=0\) is separate, as stated in the packet.

## 1. Product comparison and all strict walls

Put \(\rho=1-\varepsilon\), so the radial interval has length \(\varepsilon\).  In angular channel \(\ell\), the proved separated operator is
\[
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}.
\]
Because \(r\le1\), its quadratic form is at least that of
\[
-\frac{d^2}{dr^2}+\ell(\ell+1)
\]
with the same Dirichlet form domain.  The min--max direction is therefore
\[
\lambda_{\ell,n}\ge \left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
\]
Thus an actual eigenvalue strictly below \(K^2\) can occur only if
\[
n^2\pi^2+\varepsilon^2\ell(\ell+1)<a^2,
\qquad a=\varepsilon K.
\]
This is a necessary condition, so counting the comparison levels gives an upper, not a lower, bound for the shell count.

The admissible radial indices are exactly
\[
1\le n\le N,
\qquad
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\}.
\]
In particular, at \(a=m\pi\) one has \(N=m-1\): the level \(n=m\) is on the threshold and is excluded.  For a fixed such \(n\), set
\[
b_n=(a^2-n^2\pi^2)^{1/2},\qquad T_n=b_n/\varepsilon.
\]
If
\[
x(T)=\sqrt{T^2+\frac14}-\frac12,
\]
then \(\ell(\ell+1)<T^2\) is equivalent to \(\ell<x(T)\).  Hence the number of admissible nonnegative integers is
\[
M(T)=\lceil x(T)\rceil.
\]
At an angular wall \(T^2=p(p+1)\), one has \(x(T)=p\), hence \(M(T)=p\), and the allowed indices are \(0,\ldots,p-1\).  The endpoint channel \(\ell=p\) is therefore correctly excluded.

The separated-spectrum multiplicity in channel \(\ell\) is \(2\ell+1\).  Consequently
\[
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2,
\]
and the exact product majorant is
\[
N_D(A_{1-\varepsilon,1},K^2)
\le \mathcal P_\varepsilon(a)
:=\sum_{n=1}^{N}M_n^2.
\]
Accidental equality between different \(\ell\)-channels does not alter this: their orthogonal multiplicities add, exactly as in this sum.

For later use, the angular envelope can in fact be made strict on both sides.  From
\[
M-1<x(T)\le M,
\qquad T^2=x(T)(x(T)+1),
\]
one gets
\[
M(M-1)<T^2\le M(M+1).
\]
If \(T\le M\), then \(T^2-T<M^2\).  If \(T>M\), then
\(T^2-M^2\le M<T\), giving the same conclusion.  Also
\(M^2<T^2+M<T^2+T+1\), because \(M<x(T)+1<T+1\).  Therefore
\[
T^2-T<M(T)^2<T^2+T+1 \qquad(T>0).
\]
For \(N\ge1\), summing the upper side gives
\[
\mathcal P_\varepsilon(a)
<\frac{S_0(a)}{\varepsilon^2}+\frac{B(a)}{\varepsilon}+N,
\]
where \(S_0=\sum b_n^2\) and \(B=\sum b_n\).  Summing the lower side will give the strict obstruction in Section 4.

## 2. Exact radial deficit and elementary bounds

For \(a>0\), strict radial counting gives the unique representation
\[
\frac a\pi=N+t,
\qquad 0<t\le1.
\]
At \(a=m\pi\), this means \(N=m-1\), \(t=1\), rather than \(N=m\), \(t=0\).  The finite-square sum gives
\[
S_0=Na^2-\pi^2\frac{N(N+1)(2N+1)}6.
\]
With \(I(a)=2a^3/(3\pi)\), direct expansion yields
\[
\begin{aligned}
D(a):=I(a)-S_0(a)
=\pi^2\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
\end{aligned}
\]
At a radial wall, the left formula \((N,t)=(m-1,1)\) and the right limit \((N,t)=(m,0)\) both give
\(\pi^2(m^2/2+m/6)\).  Thus \(D\) is continuous.  Between walls,
\[
D'(a)=\frac{2a^2}{\pi}-2Na=2at>0,
\]
so it is increasing on \([\pi,\infty)\).  In particular,
\[
D(a)\ge D(\pi)=\frac{2\pi^2}{3}.
\]
The exact formula also gives \(D\ge\pi^2N^2/2\).  Since
\(N\ge a/\pi-1\) for \(a\ge\pi\),
\[
D(a)\ge\frac{(a-\pi)^2}{2}.
\]

For the linear sum, let \(f(x)=\sqrt{a^2-\pi^2x^2}\).  It is decreasing on \([0,a/\pi]\), and the strict radial cutoff has \(N<a/\pi\) for \(a>0\).  Hence
\[
B(a)=\sum_{n=1}^N f(n)
\le\int_0^{a/\pi}f(x)\,dx
=\frac{a^2}{4}.
\]
Also \(N\le a/\pi\).  Both statements are trivial at \(a=0\).

The target Weyl expression is exactly
\[
\begin{aligned}
W_\varepsilon(a)
&=\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)
\left(\frac a\varepsilon\right)^3\\
&=\frac{I(a)}{\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\end{aligned}
\]
For \(N\ge1\), write
\[
U=\frac{I-D}{\varepsilon^2}+\frac B\varepsilon+N.
\]
Then
\[
W_\varepsilon-U
=\frac D{\varepsilon^2}-\frac{I+B}{\varepsilon}
+\frac I3-N.
\]
Consequently the packet's sufficient condition
\[
D\ge\varepsilon\left(I+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}
\tag{*}
\]
indeed implies
\[
W_\varepsilon-U
\ge \frac{a^2/4-B}{\varepsilon}
+\left(\frac a\pi-N\right)+\frac I3\ge0.
\]
Since \(\mathcal P_\varepsilon<U\) when \(N\ge1\), condition (*) proves the desired comparison in that region.

## 3. Verification of the three positive subranges

1. If \(0\le a\le\pi\), then no positive integer satisfies \(n\pi<a\).  Thus \(N=0\) and
   \(N_D\le\mathcal P_\varepsilon=0\le W_\varepsilon\).  This includes both \(a=0\) and the exact wall \(a=\pi\).

2. Suppose \(\pi<a\le4\pi\) and \(0<\varepsilon\le1/100\).  The right side of (*) is increasing in both positive variables, so
\[
\begin{aligned}
\varepsilon\left(I+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}
&\le \frac1{100}\left(\frac{128\pi^2}{3}+4\pi^2\right)
+\frac4{10000}\\
&=\frac{7\pi^2}{15}+\frac1{2500}.
\end{aligned}
\]
On the other hand, \(D\ge2\pi^2/3\), and the difference is
\[
\frac{2\pi^2}{3}-\left(\frac{7\pi^2}{15}+\frac1{2500}\right)
=\frac{\pi^2}{5}-\frac1{2500}>0.
\]
This verifies the endpoint \(\varepsilon=1/100\), the wall \(a=4\pi\), and the limit immediately above \(a=\pi\).

3. Suppose \(4\pi\le a\le\pi/(4\varepsilon)\).  Then
\[
D\ge\frac{(a-\pi)^2}{2}\ge\frac{9a^2}{32}.
\]
The upper endpoint gives \(\varepsilon a\le\pi/4\), while
\(\varepsilon\le1/100\) and \(a\ge4\pi\) give
\[
\varepsilon I=\frac{2\varepsilon a^3}{3\pi}\le\frac{a^2}{6},
\qquad
\frac{\varepsilon a^2}{4}\le\frac{a^2}{400},
\qquad
\frac{\varepsilon^2a}{\pi}
\le\frac{\varepsilon^2a^2}{4\pi^2}
\le\frac{a^2}{40000\pi^2}.
\]
Finally,
\[
\frac9{32}-\frac16-\frac1{400}=\frac{269}{2400}
>\frac1{40000\pi^2}.
\]
Thus the right side of (*) is strictly below \(9a^2/32\le D\), including \(a=\pi/(4\varepsilon)\).

Combining the three ranges proves
\[
N_D(A_{1-\varepsilon,1},K^2)
\le \frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3
\]
for \(0<\varepsilon\le1/100\) and
\(0\le a=\varepsilon K\le\pi/(4\varepsilon)\), equivalently
\(0\le K\le\pi/(4\varepsilon^2)\).

## 4. Exact wall obstruction to the product method

Fix \(0<\varepsilon<1\), and let \(Q\) be an integer satisfying
\[
Q>\frac9{4\varepsilon}.
\]
Then \(Q\ge3\).  At the exact radial wall \(a=Q\pi\), strict counting gives
\(N=Q-1\), and the deficit formula with \((N,t)=(Q-1,1)\) gives
\[
D_Q=\pi^2\left(\frac{Q^2}{2}+\frac Q6\right),
\qquad S_0=I-D_Q,
\qquad I=\frac{2\pi^2Q^3}{3}.
\]
The strict lower angular envelope proved in Section 1 gives
\[
\mathcal P_\varepsilon(Q\pi)
>\frac{S_0}{\varepsilon^2}-\frac{B(Q\pi)}{\varepsilon}.
\tag{1}
\]
There are \(Q-1\) summands in \(B\), and each is strictly less than \(\pi Q\), so
\[
B(Q\pi)<\pi Q(Q-1)<\pi Q^2.
\tag{2}
\]
Since \(\varepsilon<1\), (2), the hypothesis on \(Q\), and \(Q\ge3\) yield
\[
\begin{aligned}
\varepsilon\left[\left(1-\frac\varepsilon3\right)I-B\right]
&>\varepsilon\left(\frac23I-\pi Q^2\right)\\
&=\pi^2Q^2\left(\frac{4\varepsilon Q}{9}-\frac\varepsilon\pi\right)\\
&>\pi^2Q^2\left(1-\frac\varepsilon\pi\right)\\
&>\pi^2Q^2\left(1-\frac1\pi\right)\\
&>\frac59\pi^2Q^2\\
&\ge\pi^2Q^2\left(\frac12+\frac1{6Q}\right)=D_Q.
\end{aligned}
\]
Here \(1-1/\pi>5/9\) follows already from \(\pi>3\).  Rearranging the strict inequality gives
\[
I-D_Q-\varepsilon B
>I\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\]
After division by \(\varepsilon^2\), (1) therefore implies
\[
\boxed{\mathcal P_\varepsilon(Q\pi)>W_\varepsilon(Q\pi)}.
\]
There are infinitely many such integers \(Q\) for every fixed \(\varepsilon>0\).  This says only that the one-sided upper majorant is too large; it does **not** reverse the actual shell inequality.

There is also an explicit arbitrarily thin obstructed family.  For integers \(j\ge101\), take
\[
\varepsilon_j=\frac1j,
\qquad Q_j=3j,
\qquad a_j=3\pi j,
\qquad K_j=3\pi j^2.
\]
Then \(\rho_j=1-1/j\uparrow1\), \(Q_j>9/(4\varepsilon_j)\), and
\(\mathcal P_{\varepsilon_j}(a_j)>W_{\varepsilon_j}(a_j)\).

## 5. Fixed-\(\rho\) threshold and non-overlap

The already-proved high-energy theorem uses
\[
\eta_\rho=G_1(\rho),
\qquad
\alpha_\rho=\frac{2\pi\rho}{1-\rho},
\qquad
K_0(\rho)=
\left(
\frac{\sqrt{\alpha_\rho}+\sqrt{\alpha_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
\]
for \(\rho>1/2\), where
\[
G_1(s)=\frac1\pi\left(\sqrt{1-s^2}-s\arccos s\right).
\]
For \(\rho=1-\varepsilon\), elementary endpoint expansion gives
\[
\eta_{1-\varepsilon}
=\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}(1+O(\varepsilon)),
\qquad
\alpha_{1-\varepsilon}
=\frac{2\pi}{\varepsilon}(1+O(\varepsilon)).
\]
The \(4\eta C_0\) term is lower order relative to \(\alpha\), hence
\[
K_0(1-\varepsilon)
\sim\frac{\alpha_{1-\varepsilon}}{\eta_{1-\varepsilon}^2}
=\frac{9\pi^3}{4}\varepsilon^{-4},
\qquad
\varepsilon K_0(1-\varepsilon)
\sim\frac{9\pi^3}{4}\varepsilon^{-3}.
\]
This can also be separated from the positive product range without relying only on asymptotics.  Since
\[
G_1(\rho)=\frac1\pi\int_\rho^1\arccos s\,ds
<\frac{1-\rho}{2}=\frac\varepsilon2
\quad(\rho>0),
\]
the exact threshold formula gives
\[
K_0(1-\varepsilon)
>\frac{\alpha_{1-\varepsilon}}{\eta_{1-\varepsilon}^2}
>\frac{8\pi(1-\varepsilon)}{\varepsilon^3}
>\frac{\pi}{4\varepsilon^2}
\]
for every \(0<\varepsilon\le1/100\).  Thus the proved product interval ends strictly before the fixed-\(\rho\) high-energy theorem begins.  The first guaranteed obstructing walls can be chosen with \(Q=O(\varepsilon^{-1})\), hence at optical width \(a=Q\pi=O(\varepsilon^{-1})\), whereas the high-energy optical threshold is of order \(\varepsilon^{-3}\).  No endpoint-uniform closure follows, so `SHELL-rho-one-endpoint` and the global shell target must remain open.
