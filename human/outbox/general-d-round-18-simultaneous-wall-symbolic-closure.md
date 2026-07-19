# General dimension, Round 18: symbolic closure of the simultaneous wall

Date: 19 July 2026

Status: **proved at the simultaneous radial/action wall**.  This note proves,
without decimal root certification or interval subdivision, that

\[
F(K,a)>\frac12
\]

at the unique point satisfying

\[
K=a+\pi,\qquad A(a-1)=\frac34.
\]

This closes the remaining transcendental value at the intersection of the
two geometric boundary faces from Round 16.  It does **not** prove the
Round 17 action-face scalar \(\mathcal S>0\), close WP2, close the
first-floor branch, or prove the all-dimensional theorem.

## 1. Simultaneous-wall scalar

Retain

\[
G_b(s)=
\frac{\sqrt{b^2-s^2}-s\arccos(s/b)}{\pi},
\qquad
A=G_K-G_a.
\]

On the simultaneous wall put

\[
K=a+\pi,\qquad t=a-1,\qquad
H(a):=G_{a+\pi}(a-1)-G_a(a-1).
\tag{1.1}
\]

The action equality is \(H(a)=3/4\).  The radial equality gives

\[
A(0)=\frac{K-a}{\pi}=1.
\]

Since \(A\) is decreasing, the critical solution of \(A(x)=1\) is
literally

\[
x=0.
\tag{1.2}
\]

Let \(z\) be determined by \(G_K(z)=3/4\).  Round 16's definition of
\(F\) then becomes

\[
F=\frac{K^2-a^2}{8}-z
=\frac{a\pi}{4}+\frac{\pi^2}{8}-z.
\tag{1.3}
\]

It is enough to prove a lower bound for \(a\) and an upper bound for \(z\).

## 2. Strict monotonicity and uniqueness of the wall point

Write

\[
\gamma=\arccos\frac{a-1}{a+\pi},
\qquad
\phi=\arccos\frac{a-1}{a}.
\]

For \(s<b\),

\[
\partial_bG_b(s)=\frac1\pi\sqrt{1-\frac{s^2}{b^2}},
\qquad
\partial_sG_b(s)=-\frac1\pi\arccos\frac{s}{b}.
\]

Both the radius and the spatial argument in (1.1) have derivative one.
Consequently

\[
H'(a)
=\frac{(\sin\gamma-\gamma)-(\sin\phi-\phi)}{\pi}.
\tag{2.1}
\]

Here \(0<\phi<\gamma<\pi/2\).  The function
\(\sin u-u\) is strictly decreasing on \((0,\pi/2)\), so

\[
H'(a)<0.
\tag{2.2}
\]

Thus the simultaneous wall has at most one point.  The rational endpoint
certificates below prove

\[
H\!\left(\frac{11}{2}\right)>\frac34,
\qquad
H\!\left(\frac{45}{8}\right)<\frac34.
\tag{2.3}
\]

Continuity and (2.2) therefore give a unique solution \(a_*\), with

\[
\boxed{\frac{11}{2}<a_*<\frac{45}{8}.}
\tag{2.4}
\]

## 3. Exact elementary certificate machinery

### 3.1 Alternating arctangent bounds

For \(0<x<1\), define

\[
T_n(x):=\sum_{j=0}^{n-1}
\frac{(-1)^j x^{2j+1}}{2j+1}.
\tag{3.1}
\]

The alternating-series remainder gives

\[
T_{2m}(x)<\arctan x<T_{2m+1}(x).
\tag{3.2}
\]

Only \(T_5,T_6,T_7\) will be needed below.

### 3.2 Self-contained rational bounds for \(\pi\)

Put

\[
p_-:=\frac{333}{106},
\qquad
p_+:=\frac{355}{113}.
\tag{3.3}
\]

Machin's identity

\[
\frac{\pi}{4}
=4\arctan\frac15-\arctan\frac1{239}
\tag{3.4}
\]

follows from the tangent addition formula, with the resulting angle in
\((0,\pi/2)\).  Define

\[
M_-:=4T_6(1/5)-T_1(1/239),
\qquad
M_+:=4T_7(1/5)-T_2(1/239).
\]

By (3.2),

\[
M_-<\frac\pi4<M_+.
\]

The remaining comparisons are exact rational arithmetic:

\[
M_--\frac{p_-}{4}
=
\frac{71255393653}{3428996484375000}
>\frac1{100000},
\tag{3.5}
\]

\[
\frac{p_+}{4}-M_+
=
\frac{4525115621373289}
{67860769651479492187500}
>\frac1{100000000}.
\tag{3.6}
\]

Hence

\[
\boxed{p_-<\pi<p_+.}
\tag{3.7}
\]

### 3.3 A common angle formula

For a fixed \(a\), set

\[
t=a-1,\qquad
R(a):=\sqrt{(a+\pi)^2-t^2},
\qquad
I(a):=\sqrt{a^2-t^2}=\sqrt{2a-1}.
\]

The two angles satisfy

\[
\gamma=\frac\pi2-\arctan\frac{t}{R(a)},
\qquad
\phi=\arctan\frac{I(a)}{t}.
\]

Therefore

\[
\boxed{
\pi H(a)
=R(a)-I(a)-\frac{t\pi}{2}
+t\left\{
\arctan\frac{t}{R(a)}
+\arctan\frac{I(a)}{t}
\right\}.}
\tag{3.8}
\]

Every argument of \(\arctan\) used below lies strictly between zero and
one.

## 4. The lower endpoint \(a=11/2\)

Put

\[
a_-=\frac{11}{2},\qquad t_-=\frac92,
\]

\[
r_-=\frac{7377}{1000},\quad
r_+=\frac{7378}{1000},\quad
i_-=\frac{3162}{1000},\quad
i_+=\frac{3163}{1000}.
\tag{4.1}
\]

Here

\[
R(a_-)^2=\pi^2+11\pi+10,
\qquad
I(a_-)^2=10.
\]

The following square checks are exact:

\[
p_-^2+11p_-+10-r_-^2
=\frac{15607639}{2809000000}>0,
\tag{4.2}
\]

\[
r_+^2-(p_+^2+11p_++10)
=\frac{24758449}{3192250000}>0,
\tag{4.3}
\]

\[
10-i_-^2=\frac{439}{250000}>0,
\qquad
i_+^2-10=\frac{4569}{1000000}>0.
\tag{4.4}
\]

Together with (3.7), these prove

\[
r_-<R(a_-)<r_+,
\qquad
i_-<I(a_-)<i_+.
\tag{4.5}
\]

Define the exact rational lower certificate

\[
\begin{aligned}
C_-:={}&
r_- -i_+ -\frac{t_-p_+}{2}\\
&+t_-\left\{
T_6\!\left(\frac{t_-}{r_+}\right)
+T_6\!\left(\frac{i_-}{t_-}\right)
\right\}.
\end{aligned}
\tag{4.6}
\]

Formula (3.8), monotonicity of \(\arctan\), (3.2), and (4.5) give

\[
\pi H(a_-)>C_-.
\tag{4.7}
\]

Exact rational evaluation gives the strict margin

\[
\boxed{
C_--\frac{3p_+}{4}>\frac1{150}.}
\tag{4.8}
\]

Since \(p_+>\pi\), (4.7)--(4.8) imply

\[
\pi H(a_-)>\frac{3\pi}{4},
\qquad
H(11/2)>\frac34.
\tag{4.9}
\]

No numerical approximation to the wall root is used.

## 5. The upper endpoint \(a=45/8\)

Put

\[
a_+=\frac{45}{8},\qquad t_+=\frac{37}{8},
\]

\[
\rho_-=\frac{7447}{1000},\quad
\rho_+=\frac{7448}{1000},\quad
\iota_-=\frac{3201}{1000},\quad
\iota_+=\frac{3202}{1000}.
\tag{5.1}
\]

Now

\[
R(a_+)^2=(a_++\pi)^2-t_+^2,
\qquad
I(a_+)^2=\frac{41}{4}.
\]

The exact square checks are

\[
(a_++p_-)^2-t_+^2-\rho_-^2
=\frac{9139519}{2809000000}>0,
\tag{5.2}
\]

\[
\rho_+^2-\{(a_++p_+)^2-t_+^2\}
=\frac{2030584}{199515625}>0,
\tag{5.3}
\]

\[
\frac{41}{4}-\iota_-^2
=\frac{3599}{1000000}>0,
\qquad
\iota_+^2-\frac{41}{4}
=\frac{701}{250000}>0.
\tag{5.4}
\]

Thus

\[
\rho_-<R(a_+)<\rho_+,
\qquad
\iota_-<I(a_+)<\iota_+.
\tag{5.5}
\]

Define the exact rational upper certificate

\[
\begin{aligned}
C_+:={}&
\rho_+-\iota_- -\frac{t_+p_-}{2}\\
&+t_+\left\{
T_7\!\left(\frac{t_+}{\rho_-}\right)
+T_7\!\left(\frac{\iota_+}{t_+}\right)
\right\}.
\end{aligned}
\tag{5.6}
\]

The upper halves of (3.2), (3.7), and (5.5) give

\[
\pi H(a_+)<C_+.
\tag{5.7}
\]

Exact rational evaluation gives

\[
\boxed{
\frac{3p_-}{4}-C_+>\frac1{600}.}
\tag{5.8}
\]

Since \(p_-<\pi\), it follows that

\[
\pi H(a_+)<\frac{3\pi}{4},
\qquad
H(45/8)<\frac34.
\tag{5.9}
\]

This completes the proof of the wall bracket (2.4).

## 6. A rational upper bound for \(z\)

Let

\[
K_0:=\frac{45}{8}+\pi,
\qquad
s_0:=\frac{101}{20},
\qquad
R_0:=\sqrt{K_0^2-s_0^2}.
\]

Use

\[
\sigma_-:=\frac{7165}{1000},
\qquad
\sigma_+:=\frac{7167}{1000}.
\tag{6.1}
\]

The exact square checks

\[
\left(\frac{45}{8}+p_-\right)^2-s_0^2-\sigma_-^2
=\frac{336031}{28090000}>0,
\tag{6.2}
\]

\[
\sigma_+^2-
\left\{\left(\frac{45}{8}+p_+\right)^2-s_0^2\right\}
=\frac{48642129}{3192250000}>0
\tag{6.3}
\]

give

\[
\sigma_-<R_0<\sigma_+.
\tag{6.4}
\]

Since

\[
\arccos\frac{s_0}{K_0}
=\frac\pi2-\arctan\frac{s_0}{R_0},
\]

one has

\[
\pi G_{K_0}(s_0)
=R_0-\frac{s_0\pi}{2}
+s_0\arctan\frac{s_0}{R_0}.
\tag{6.5}
\]

Define

\[
C_z:=
\sigma_+-\frac{s_0p_-}{2}
+s_0T_5\!\left(\frac{s_0}{\sigma_-}\right).
\tag{6.6}
\]

Equations (3.2), (3.7), and (6.4) imply

\[
\pi G_{K_0}(s_0)<C_z.
\]

The exact rational margin is

\[
\boxed{
\frac{3p_-}{4}-C_z>\frac1{100}.}
\tag{6.7}
\]

Therefore

\[
G_{K_0}(s_0)<\frac34.
\tag{6.8}
\]

At the actual wall point, (2.4) gives

\[
K_*=a_*+\pi<K_0.
\]

For fixed \(s\),

\[
\partial_KG_K(s)
=\frac1\pi\sqrt{1-\frac{s^2}{K^2}}>0.
\]

Hence

\[
G_{K_*}(s_0)<G_{K_0}(s_0)<\frac34.
\]

Because \(G_{K_*}\) is strictly decreasing in its spatial argument and
\(G_{K_*}(z)=3/4\),

\[
\boxed{z<\frac{101}{20}.}
\tag{6.9}
\]

## 7. Final exact reserve

Substitute (2.4) and (6.9) into (1.3):

\[
F>
\frac{11\pi}{8}+\frac{\pi^2}{8}-\frac{101}{20}.
\]

Using only \(\pi>p_-\),

\[
\begin{aligned}
F-\frac12
&>
\frac{p_-^2+11p_--222/5}{8}\\
&=
\boxed{\frac{1443}{449440}}>0.
\end{aligned}
\tag{7.1}
\]

Thus

\[
\boxed{F(a_*+\pi,a_*)>\frac12.}
\tag{7.2}
\]

## 8. Equality and wall audit

1. The relations \(K-a=\pi\) and \(A(a-1)=3/4\) are literal simultaneous
   equalities, not open-cell substitutions.
2. At the radial equality, \(A(0)=1\), so \(x=0\) is the exact critical
   point.  No assertion \(x>0\) from the strict face is imported.
3. The signs in (4.9), (5.9), and (6.8) have explicit positive rational
   margins.  Thus the derived inequalities \(11/2<a_*<45/8\) and
   \(z<101/20\) are strict.
4. The inverse level \(G_K(z)=3/4\) is used with the strict spatial
   monotonicity of \(G_K\); no inverse-wall ownership convention is changed.
5. This simultaneous radial/action wall is distinct from Round 16's
   one-sided hard \(q=3\) face.  No floor count or shelf label is transferred
   between them.

## 9. Dependency and loss ledger

- **Imported:** the Round 16 definition of \(F\), its reduction to the two
  boundary faces, and the identification \(x=0\) on \(K-a=\pi\).
- **Proved here:** uniqueness and the rational bracket for the simultaneous
  wall, the rational upper bound for \(z\), and the exact positive reserve
  (7.1).
- **Elementary inputs:** differentiation of \(G_b\), the alternating
  arctangent series, Machin's identity, and exact rational square
  comparisons.
- **Deliberate losses:** \(a_*\) is replaced by \(11/2\) in the favorable
  term, \(K_*\) by \(45/8+\pi\) when bounding \(z\), and \(z\) by \(101/20\).
  Every loss is one-sided and followed by a displayed exact rational margin.
- **Not used:** a decimal approximation to \(a_*\), interval arithmetic,
  interval subdivision, or the Round 17 numerical action-face search.

The accompanying Wolfram Language replay
computations/general_d_round18_simultaneous_wall_symbolic_replay.wl
checks all finite rational identities exactly and prints a separate
high-precision diagnostic root.  The replay is an audit convenience, not a
premise of the proof.

## 10. Gate decision

The simultaneous two-wall value required by Round 16 is now certified:

\[
F_{\rm two\text{-}wall}>\frac12.
\]

The remaining low-floor geometric obligation is the Round 17 action-face
payment \(\mathcal S>0\) in (5.2), or an equivalent proof of
\(dF/da>0\) on that face.  Until that payment is proved, WP2, the hard
\(B=1\) first-floor branch, and the all-dimensional theorem remain open.
The high-floor CST remains a separate open obligation.
