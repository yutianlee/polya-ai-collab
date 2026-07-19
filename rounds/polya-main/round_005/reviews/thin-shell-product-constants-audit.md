# Thin-shell product constants audit

## Verdict

**FAIL as written, for two localized strict-endpoint assertions in the
incumbent.** The packet's main positive theorem, all numerical constants,
the exact wall obstruction, the \(\epsilon=1/Q\) family, and the lower
bound for \(\epsilon K_0\) are algebraically correct. The two defects do
not invalidate those conclusions, but an endpoint audit cannot pass the
incumbent verbatim:

1. Incumbent (10) claims
   \[
   \mathcal P_\epsilon(a)>
   \frac{S_0(a)}{\epsilon^2}-\frac{B(a)}{\epsilon}
   \]
   without restricting to \(N\ge1\). For \(0\le a\le\pi\), \(N=0\)
   and both sides are zero. Globally the sign must be \(\ge\), or the
   strict version must be stated only for a nonempty radial sum. Every
   later use of the strict version has \(N>0\), so the wall obstruction
   is unaffected.
2. If
   \[
   Q_*=\min\{Q\in\mathbb N:Q>9/(4\epsilon)\},
   \]
   then
   \[
   Q_*\le \frac9{4\epsilon}+1,
   \]
   not always strictly less. Equality occurs whenever
   \(9/(4\epsilon)\) is an integer. The corrected comparison
   \[
   \pi Q_*
   \le\pi\left(\frac9{4\epsilon}+1\right)
   <\frac{9\pi}{\epsilon^3}
   <\epsilon K_0(1-\epsilon)
   \]
   still proves the claimed non-overlap for
   \(0<\epsilon\le1/2\).

A further harmless scope qualification is that
\(a/\pi=N+t\), \(0<t\le1\), is only available for \(a>0\);
at \(a=0\), one has \(N=t=0\). The proof already treats \(a=0\)
separately.

## Audited constants

### 1. Exact \(D(a)\), walls, and monotonicity

With \(a/\pi=N+t\), \(0<t\le1\),

\[
S_0
=Na^2-\frac{\pi^2N(N+1)(2N+1)}6,
\qquad
I=\frac{2a^3}{3\pi}.
\]

Direct expansion gives

\[
D=I-S_0
=\pi^2\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
\]

At \(a=m\pi\), strict counting uses \(N=m-1,t=1\). The wall
value is

\[
\frac{D(m\pi)}{\pi^2}
=\frac{m^2}{2}+\frac m6,
\]

which is also the right limit obtained from \(N=m,t\downarrow0\).
Thus \(D\) is continuous across every wall. Between walls,

\[
D'(a)
=\frac{2a^2}{\pi}-2Na
=2at>0.
\]

Hence \(D\) is strictly increasing for \(a\ge\pi\),

\[
D(a)\ge\frac{2\pi^2}{3},
\]

and, since \(N\ge a/\pi-1\),

\[
D(a)\ge\frac{\pi^2N^2}{2}
\ge\frac{(a-\pi)^2}{2}.
\]

All these identities and endpoint conventions are correct.

### 2. The quarter-disk bound for \(B\)

For

\[
f(x)=\sqrt{a^2-\pi^2x^2},
\]

monotonicity gives

\[
\sum_{n=1}^{N}f(n)
\le\int_0^Nf(x)\,dx
\le\int_0^{a/\pi}f(x)\,dx
=\frac{a^2}{4}.
\]

Therefore \(B(a)\le a^2/4\), including radial walls where the
zero endpoint term is excluded.

### 3. The explicit \(\epsilon\le1/100\) split

The sufficient inequality

\[
D(a)\ge
\epsilon\left(\frac{2a^3}{3\pi}+\frac{a^2}{4}\right)
+\frac{\epsilon^2a}{\pi}
\]

is correct.

For \(\pi<a\le4\pi\), its right side is maximized at
\((a,\epsilon)=(4\pi,1/100)\), where it equals

\[
\frac1{100}
\left(\frac{128\pi^2}{3}+4\pi^2\right)
+\frac4{10000}
=\frac{7\pi^2}{15}+\frac1{2500}
<\frac{2\pi^2}{3}.
\]

For \(4\pi\le a\le\pi/(4\epsilon)\),

\[
D(a)\ge\frac{9a^2}{32},
\]

while the normalized right side is at most

\[
\frac{2\epsilon a}{3\pi}
+\frac\epsilon4+\frac{\epsilon^2}{\pi a}
\le
\frac16+\frac1{400}
+\frac1{40000\pi^2}
<\frac9{32}.
\]

The inequalities remain strict at
\(\epsilon=1/100\), \(a=4\pi\), and
\(a=\pi/(4\epsilon)\). For \(0\le a\le\pi\), the strict radial
count is zero, including \(a=\pi\). Thus the packet's positive range is
valid with all advertised endpoints.

### 4. Exact radial-wall obstruction

At \(a=Q\pi\), strict counting gives \(N=Q-1\), and

\[
D_Q=\pi^2\left(\frac{Q^2}{2}+\frac Q6\right),
\qquad
I=\frac{2\pi^2Q^3}{3}.
\]

Also

\[
B(Q\pi)
=\pi\sum_{n=1}^{Q-1}\sqrt{Q^2-n^2}
<\pi Q(Q-1).
\]

For a nonempty sum, the lower angular inequality is strict, so

\[
\begin{aligned}
\epsilon^2(\mathcal P_\epsilon-W_\epsilon)
>{}&
\frac{2\pi^2}{3}
\epsilon\left(1-\frac\epsilon3\right)Q^3\\
&-\pi^2\left(\frac{Q^2}{2}+\frac Q6\right)
-\epsilon\pi Q(Q-1).
\end{aligned}
\]

After division by \(\pi^2Q\), if
\(0<\epsilon<1\) and \(Q>9/(4\epsilon)\), the positive term is

\[
>\frac49\epsilon Q^2>Q,
\]

whereas the quantities subtracted total less than

\[
\frac Q2+\frac16+\frac{Q-1}{3}
=\frac{5Q}{6}-\frac16<Q.
\]

Hence

\[
\mathcal P_\epsilon(Q\pi)>W_\epsilon(Q\pi).
\]

The constant \(9/4\), the strict \(Q\)-condition, and the obstruction
itself are correct.

### 5. The exact \(\epsilon=1/Q\) family

For \(Q\ge4\), \(\epsilon=1/Q\), \(a=Q\pi\), one has

\[
T_n^2=x_n=\pi^2Q^2(Q^2-n^2),
\qquad 1\le n\le Q-1.
\]

The lower angular estimate and
\(\sum T_n<\pi Q^2(Q-1)\) give

\[
\mathcal P>
\sum_{n=1}^{Q-1}x_n-\pi Q^2(Q-1).
\]

Direct finite summation verifies

\[
\sum_{n=1}^{Q-1}x_n-W_{1/Q}(Q\pi)
=\frac{\pi^2Q^3(3Q-7)}{18}.
\]

Therefore

\[
\mathcal P-W
>
\pi Q^2
\left[
\frac{\pi Q(3Q-7)}{18}-(Q-1)
\right].
\]

Using \(\pi>3\), the bracket is greater than

\[
\frac{3Q^2-13Q+6}{6}>0
\qquad(Q\ge4).
\]

Thus the arbitrarily thin family is correct, including its first value
\(Q=4\).

### 6. Lower bound for \(\epsilon K_0\)

For \(0<\epsilon\le1/2\),

\[
\eta_{1-\epsilon}
=\frac1\pi\int_0^\epsilon\arccos(1-v)\,dv.
\]

Since

\[
\arccos(1-v)
=2\arcsin\sqrt{\frac v2}
\le\frac{2\pi}{3}\sqrt{\frac v2},
\]

integration gives the sharper intermediate bound

\[
\eta_{1-\epsilon}
\le\frac{4}{9\sqrt2}\epsilon^{3/2}
<\frac{\epsilon^{3/2}}3.
\]

The explicit positive-root formula implies

\[
K_0(\rho)>
\frac{A_\rho}{\eta_\rho^2},
\qquad
A_\rho=\frac{2\pi(1-\epsilon)}{\epsilon}.
\]

Consequently

\[
\epsilon K_0(1-\epsilon)
>
\frac{18\pi(1-\epsilon)}{\epsilon^3}
\ge\frac{9\pi}{\epsilon^3}.
\]

This lower bound and its constants are correct. With the non-strict
integer-ceiling correction identified in the verdict, it still places
an exact product-wall failure strictly before the current high-energy
threshold.

## Final re-audit after endpoint corrections

**PASS.** The corrected frozen packet and incumbent now resolve every
issue identified in the initial audit:

- the representation
  \[
  a/\pi=N+t,\qquad 0<t\le1,
  \]
  is explicitly scoped to \(a>0\);
- the strict lower product estimate is explicitly scoped to \(N\ge1\),
  while the \(N=0\) case is correctly recorded as equality with only a
  non-strict bound;
- with
  \[
  Q_*=\left\lfloor\frac9{4\epsilon}\right\rfloor+1,
  \]
  the wall comparison now uses the endpoint-correct inequality
  \[
  \pi Q_*
  \le
  \pi\left(\frac9{4\epsilon}+1\right)
  <
  \frac{9\pi}{\epsilon^3}.
  \]

The last chain combines with
\(\epsilon K_0(1-\epsilon)>9\pi/\epsilon^3\) to retain a strict
separation between the product-wall failure and the high-energy
threshold, including when \(9/(4\epsilon)\) is an integer.

All constants and remaining endpoints were already verified above and
are unchanged. The initial FAIL verdict is superseded by this final
**PASS**.
