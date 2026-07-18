# General dimension round 02: exact finite-wall certificate

Date: 18 July 2026  
Scope: Proposition 6.5 of `manuscript/spherical-shell-polya-general-d.tex`  
Status: the residual one-interface case is proved.

The standalone verifier is

`scripts/general_d_finite_wall_fraction_verify.py`.

It has no nonstandard dependency and performs no floating-point or
transcendental evaluation. Running

```text
python scripts/general_d_finite_wall_fraction_verify.py
```

prints

```text
PASS: 628 exact integer/Fraction checks
walls=11; shifts=9; controlling wall G_K(r+1)=3/4 for r<=4
uniform positive-count margin E_r(K)>3/20 for r<=4
r=9/2 endpoint lower bound: 1253/555
```

## 1. Continuous wall function

Put

\[
 H_r(K)=2\int_r^K G_K(z)\,dz-G_K(r)-\frac14.
\]

If

\[
 M_r(K)=\sum_{j\ge1}\left[G_K(r+j)+\frac14\right]_<,
\]

then the ball reserve in Proposition 6.5 is exactly

\[
 E_r(K)=H_r(K)-2M_r(K).
\]

For \(x=r/K\),

\[
 H_r(K)
 =\frac A2-
 \frac{A\arcsin x+B\sqrt{1-x^2}}{\pi}-\frac14,
\]

where

\[
 A=\frac{K^2}{2}+r^2+r,
 \qquad
 B=K\left(\frac{3r}{2}+1\right).
\]

The derivative calculation in the manuscript proves that \(H_r\) is
strictly increasing throughout the positive-count residual region (for
\(r\ge1\), already from \(K=2r\); for \(r=1/2\), from before its first
activation wall onward).

## 2. Rational envelopes

For \(0\le x\le13/20\), set

\[
 a_m=\frac{\binom{2m}{m}}{4^m(2m+1)},
 \qquad
 b_m=\frac{\binom{2m}{m}}{4^m(2m-1)},
\]

and

\[
 \begin{aligned}
 L(x)&=\sum_{m=0}^6a_mx^{2m+1},&
 U(x)&=L(x)+\frac{x^{15}}{1-x^2},\\
 V(x)&=1-\sum_{m=1}^6b_mx^{2m},&
 W(x)&=V(x)-\frac{x^{14}}{1-x^2}.
 \end{aligned}
\]

The positive series coefficients are below one, so

\[
 L\le\arcsin x\le U,
 \qquad
 W\le\sqrt{1-x^2}\le V.
\]

Machin's formula, evaluated by exact alternating rational sums in the
verifier, proves

\[
 \frac{333}{106}<\pi<\frac{355}{113}.
\]

Consequently

\[
 \underline G(K,z)
 =K\left[\frac{113}{355}(W+xL)-\frac x2\right]
 \le G_K(z)
 \le
 K\left[\frac{106}{333}(V+xU)-\frac x2\right]
 =\overline G(K,z),
\]

with \(x=z/K\), and

\[
 \underline H_r(K)
 =\frac A2-\frac{106}{333}(AU+BV)-\frac14
 \le H_r(K)
 \le
 \frac A2-\frac{113}{355}(AL+BW)-\frac14
 =\overline H_r(K).
\]

All quantities in these formulas are rational at the certificate points.

## 3. Complete wall list

Let \(k_n(z)\) be the unique solution of

\[
 G_K(z)=n-\frac14.
\]

Exact substitution gives the following pairwise disjoint brackets:

| wall | rigorous bracket |
|---|---:|
| \(k_1(3/2)\) | \((22/5,9/2)\) |
| \(k_1(2)\) | \((5,26/5)\) |
| \(k_1(5/2)\) | \((57/10,29/5)\) |
| \(k_1(3)\) | \((63/10,32/5)\) |
| \(k_1(7/2)\) | \((69/10,7)\) |
| \(k_1(4)\) | \((15/2,38/5)\) |
| \(k_2(3/2)\) | \((77/10,39/5)\) |
| \(k_1(9/2)\) | \((81/10,41/5)\) |
| \(k_2(2)\) | \((83/10,17/2)\) |
| \(k_1(5)\) | \((87/10,44/5)\) |
| \(k_2(5/2)\) | \((9,227/25)\) |

The rational bounds for \(\sqrt3\) and \(\pi\) also give

\[
 \frac{227}{25}<\frac1{\omega_0}<\frac{459}{50}.
\]

At \(K=459/50\), the exact upper envelope proves

\[
 \overline G_K(11/2)<\frac{18}{25}<\frac34,
\]

\[
 \overline G_K(3)<\frac85<\frac74,
 \qquad
 \overline G_K(3/2)<\frac94<\frac{11}{4}.
\]

Monotonicity in \(K\) and \(z\) therefore excludes every omitted wall:

- level \(3/4\) with \(z\ge11/2\);
- level \(7/4\) with \(z\ge3\);
- level \(11/4\) and every higher level.

The disjoint brackets exclude simultaneous later-sample walls.

## 4. Local wall order

At a post-crossing right limit, \(M\) is the event number in the following
list:

\[
\begin{array}{c|l}
r&(z,n;M)\\ \hline
\frac12&(\frac32,1;1),(\frac52,1;2),(\frac72,1;3),
(\frac32,2;4),(\frac92,1;5),(\frac52,2;6)\\
1&(2,1;1),(3,1;2),(4,1;3),(2,2;4),(5,1;5)\\
\frac32&(\frac52,1;1),(\frac72,1;2),(\frac92,1;3),(\frac52,2;4)\\
2&(3,1;1),(4,1;2),(5,1;3)\\
\frac52&(\frac72,1;1),(\frac92,1;2)\\
3&(4,1;1),(5,1;2)\\
\frac72&(\frac92,1;1)\\
4&(5,1;1)\\
\frac92&\varnothing.
\end{array}
\]

Every wall raises one later-sample bracket by one, including a level
\(7/4\) wall. First-sample walls do not enter this table because their jump
in \(D_K\) cancels the jump in the remainder \(e\); equivalently,
\(E=H-2M\) is continuous there.

## 5. Positivity and the controlling wall

For \(r\le4\), the first later wall is

\[
 G_K(r+1)=\frac34.
\]

Exact evaluation of \(\underline H\) and \(\overline H\) gives:

| \(r\) | first-wall lower | first-wall upper | activation/endpoint lower | every other later wall lower |
|---:|---:|---:|---:|---:|
| \(1/2\) | \(3/20\) | \(8/25\) | \(11/25\) | \(13/20\) |
| \(1\) | \(17/100\) | \(1/2\) | \(14/25\) | \(7/10\) |
| \(3/2\) | \(9/25\) | \(53/100\) | \(69/100\) | \(37/50\) |
| \(2\) | \(2/5\) | \(29/50\) | \(37/50\) | \(39/50\) |
| \(5/2\) | \(23/50\) | \(63/100\) | \(22/25\) | \(81/100\) |
| \(3\) | \(13/25\) | \(69/100\) | \(47/50\) | \(17/20\) |
| \(7/2\) | \(29/50\) | \(19/25\) | \(109/100\) | -- |
| \(4\) | \(33/50\) | \(83/100\) | \(163/100\) | -- |

The inequalities in the lower columns are strict. Each first-wall upper is
below both competing lower bounds. Since \(H_r\) increases between later
walls, the first later wall is the unique controlling right-hand wall for
every \(r\le4\). Its value is always greater than \(3/20\).

For \(r\le3\), the ball tail is zero before the first-sample activation
wall. For \(r=7/2,4\), the lower endpoint already has one first-sample
count, and direct exact bounds give the endpoint entries in the table.

For \(r=9/2\), there is no later wall. At the open lower endpoint \(K=9\),

\[
 E_{9/2}(9)
 =\frac{43}{2}-\frac{279\sqrt3}{8\pi}
 >\frac{1253}{555}>0,
\]

and \(E_{9/2}\) increases thereafter.

It follows that throughout the residual family

\[
 T_K(r)>0\quad\Longrightarrow\quad E_r(K)>0.
\]

If \(T_K(r)=0\), the shifted-tail inequality is immediate. Combining this
with \(2\delta_\mu(r)<e\) proves the remaining one-interface case.
