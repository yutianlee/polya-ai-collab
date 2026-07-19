# General dimension, Round 19: Jensen closure of the action face

Date: 19 July 2026

Status: **the remaining action-face derivative is proved globally**.  On the
strict action boundary

\[
A(a-1)=\frac34,\qquad K-a>\pi,
\]

this note proves

\[
\boxed{\frac{dF}{da}>0.}
\]

Together with Round 16's two boundary reductions and Round 18's exact
simultaneous-wall reserve, this closes the enlarged geometric lemma
\(F\ge1/2\).  It therefore supplies the missing analytic input for the hard
\(B=1\), first-floor endpoint branch.  Formal promotion of WP2 is left to the
end-to-end integration audit; the high-floor CST and the all-dimensional
theorem remain open.

## 1. Action-face notation and exact derivative

Retain

\[
G_b(y)=\frac{\sqrt{b^2-y^2}-y\arccos(y/b)}{\pi},
\qquad
J_b(y)=\int_y^bG_b(v)\,dv,
\]

\[
A=G_K-G_a,\qquad A(x)=1,\qquad G_K(z)=\frac34,
\]

and

\[
F=J_K(x)-J_a(x)-(z-x).
\]

On the strict action face put

\[
t=a-1,
\qquad
\gamma=\arccos\frac{t}{K},
\qquad
\phi=\arccos\frac{t}{a},
\]

\[
k:=K'(a)=\frac{\gamma+\sin\phi-\phi}{\sin\gamma},
\qquad
s:=\frac Ka,
\qquad
g:=G_a(x).
\tag{1.1}
\]

Let \(\theta\) be determined by

\[
\frac K\pi(\sin\theta-\theta\cos\theta)=\frac34.
\]

Round 16's exact tangential derivative is

\[
\boxed{
D:=\frac{dF}{da}
=k\left(P_K(x)-\frac{\sin\theta}{\theta}\right)-P_a(x),}
\tag{1.2}
\]

where \(P_b=\partial_bJ_b\).

The action equality is equivalently

\[
(\tan\gamma-\gamma)-(\tan\phi-\phi)
=\frac{3\pi}{4(a-1)}.
\tag{1.3}
\]

Two elementary consequences used throughout are

\[
k-1
=\frac{(\gamma-\sin\gamma)-(\phi-\sin\phi)}{\sin\gamma}>0,
\tag{1.4}
\]

and the Round 17 speed identity

\[
\boxed{
s-k=\frac{3\pi/4-\gamma+\phi}{a\sin\gamma}>0.}
\tag{1.5}
\]

## 2. One-radius Jensen reduction

Define

\[
h(u)=\sin u-u\cos u.
\]

For \(0\le c<K/\pi\), let \(\tau(c)\in[0,\pi/2)\) satisfy

\[
\frac K\pi h(\tau(c))=c,
\qquad
U(c)=\frac{\sin\tau(c)}{\tau(c)}.
\tag{2.1}
\]

Round 16 proved that \(U\) is decreasing and strictly convex, and Round 17
proved the quantile primitive

\[
P_K(y)=\int_0^{G_K(y)}U(c)\,dc.
\tag{2.2}
\]

Scaling the radius in the level equation gives the exact identity

\[
U_a(c)=U_K(sc)=U(sc).
\tag{2.3}
\]

Put

\[
p=g+1,\qquad q=sg,\qquad c_0=\frac34.
\tag{2.4}
\]

At the point \(x\), write

\[
\beta=\arccos(x/K),\qquad \psi=\arccos(x/a).
\]

Since \(x>0\) on the strict face, \(\beta>\psi\).  Hence

\[
p=\frac K\pi h(\beta),
\qquad
q=\frac K\pi h(\psi),
\qquad
0<q<p.
\tag{2.5}
\]

Substitution of (2.2)--(2.4) into (1.2) gives

\[
D
=k\left\{\int_0^pU(c)\,dc-U(c_0)\right\}
-\frac1s\int_0^qU(c)\,dc,
\]

or

\[
\boxed{
D=\left(k-\frac1s\right)\int_0^qU
+k\int_q^pU-kU(c_0).}
\tag{2.6}
\]

Both integral weights are positive by \(k>1\) and \(s>1\).  Define

\[
\mathcal T
:=\left(k-\frac1s\right)q+k(p-q)
=kp-g
=k+g(k-1)>0,
\tag{2.7}
\]

\[
m
:=\frac{
  (k-1/s)q(q/2)+k(p-q)(p+q)/2
}{\mathcal T}
=\frac{kp^2-sg^2}{2\mathcal T}.
\tag{2.8}
\]

Jensen first on each interval and then between their two midpoint masses
gives

\[
\left(k-\frac1s\right)\int_0^qU+k\int_q^pU
\ge \mathcal T U(m).
\]

Thus

\[
\boxed{D\ge \mathcal T U(m)-kU(c_0).}
\tag{2.9}
\]

If \(m\le c_0\), monotonicity of \(U\) immediately gives

\[
D\ge(\mathcal T-k)U(c_0)
=g(k-1)U(c_0)>0.
\tag{2.10}
\]

It remains to consider \(m>c_0\).  Put

\[
f_0:=-U'(c_0)>0,
\qquad
E(u):=\left(\frac{h(u)}{u\sin u}\right)^2.
\tag{2.11}
\]

The tangent inequality for the convex function \(U\) gives

\[
U(m)\ge U(c_0)-f_0(m-c_0).
\]

Exact algebra gives

\[
4\mathcal T(m-c_0)=H,
\qquad
H:=2(k-s)g^2+(k+3)g-k.
\tag{2.12}
\]

Differentiating (2.1) at \(c_0\) gives

\[
f_0=\frac{\pi h(\theta)}{K\theta^3\sin\theta},
\qquad
\frac{U(c_0)}{f_0}=\frac{3}{4E(\theta)}.
\tag{2.13}
\]

Consequently

\[
\boxed{
D\ge\frac{f_0}{4}
\left\{\frac{3g(k-1)}{E(\theta)}-H\right\}.}
\tag{2.14}
\]

The action face is therefore closed once the following two intrinsic
inequalities are proved:

\[
\boxed{E(\theta)<k-1,}
\tag{I}
\]

\[
\boxed{H<3g.}
\tag{II}
\]

Indeed, their substitution in (2.14) is strict.

## 3. Location and monotonicity along the action face

Let \(a_*\) be the unique simultaneous-wall point from Round 18.  For fixed
\(a\), the shell action \(G_K(a-1)-G_a(a-1)\) increases strictly with
\(K\).  Round 18 also proved that its value at \(K=a+\pi\) decreases through
\(3/4\) at \(a_*\).  Hence the strict action face \(K-a>\pi\) is exactly the
part with

\[
a>a_*,
\qquad
\frac{11}{2}<a_*<\frac{45}{8}.
\tag{3.1}
\]

### 3.1 The angle \(\gamma\) decreases

Since

\[
\phi'=-\frac1{a^2\sin\phi}<0,
\]

differentiating (1.3) gives

\[
\boxed{
\gamma'
=\frac{\tan^2\phi\,\phi'-(3\pi/4)/(a-1)^2}
       {\tan^2\gamma}<0.}
\tag{3.2}
\]

### 3.2 The inner level \(g\) decreases

Differentiating \(A(x)=1\) gives

\[
x'=\frac{k\sin\beta-\sin\psi}{\beta-\psi}.
\tag{3.3}
\]

Therefore

\[
g'
=\frac{\sin\psi-\psi x'}\pi
=-\frac{\psi\beta}{\pi(\beta-\psi)}
 \left\{k\frac{\sin\beta}{\beta}
       -\frac{\sin\psi}{\psi}\right\}.
\tag{3.4}
\]

The expression in braces is positive.  For completeness, if
\(u(v)=\sin v/v\), Round 17's endpoint comparison is

\[
k u(\beta)>u(\psi).
\tag{3.5}
\]

It follows from the monotonicity in the spatial variable of
\(u(\phi_y)/u(\gamma_y)\).  At \(y=t\),

\[
ku(\gamma)
=1-\frac{\phi-\sin\phi}{\gamma}
>1-\frac{\phi-\sin\phi}{\phi}
=u(\phi),
\]

and \(x<t\) because \(A(x)=1>A(t)=3/4\).  Thus (3.5) is strict, and

\[
\boxed{g'(a)<0.}
\tag{3.6}
\]

These two global monotonicities replace any subdivision of the action face.

## 4. Proof of intrinsic inequality (I)

### 4.1 A uniform angle separation

The function

\[
E(u)=\left(\frac1u-\cot u\right)^2
\]

is strictly increasing on \((0,\pi/2)\), because

\[
\left(\frac1u-\cot u\right)'
=\frac1{\sin^2u}-\frac1{u^2}>0.
\tag{4.1}
\]

Moreover, the action equality gives

\[
G_K(t)=\frac34+G_a(t)>\frac34=G_K(z).
\]

Since \(G_K\) decreases in its spatial argument, \(z>t\), and therefore

\[
\theta<\gamma,
\qquad
E(\theta)<E(\gamma).
\tag{4.2}
\]

We next prove the stronger geometric separation

\[
\boxed{\frac\phi\gamma<\frac35.}
\tag{4.3}
\]

From (3.1),

\[
\cos\phi=1-\frac1a>\frac9{11}.
\]

The alternating cosine remainder gives

\[
\frac9{11}
-\left\{1-\frac{(613/1000)^2}{2}
+\frac{(613/1000)^4}{24}\right\}
=\frac{48282245029}{264000000000000}>0.
\tag{4.4}
\]

Hence \(\phi<613/1000\).

Suppose instead that \(\gamma\le5\phi/3\).  Since
\(a=t\sec\phi\), \(K=t\sec\gamma\), and
\(t=(\sec\phi-1)^{-1}\),

\[
K-a
\le R(\phi)
:=\frac{\sec(5\phi/3)-\sec\phi}{\sec\phi-1}.
\tag{4.5}
\]

Here \(5\phi/3<613/600<\pi/2\).  The function \(R\) is strictly
increasing.  Indeed, write

\[
\sec v=\sum_{n\ge0}c_nv^{2n},\qquad c_n>0.
\]

Then \(R(v)\) is the weighted mean of the strictly increasing sequence
\((5/3)^{2n}-1\), \(n\ge1\), with weights \(c_nv^{2n}\).  Increasing
\(v\) exponentially tilts these weights toward larger \(n\).  More
explicitly, for the normalized weights \(w_n\) and
\(r_n=(5/3)^{2n}-1\),

\[
vR'(v)=2\operatorname{Cov}_{w}(n,r_n)>0,
\]

because both \(n\) and \(r_n\) increase strictly.  Thus \(R\) increases
strictly.

At the rational endpoint, (4.4) gives
\(\sec(613/1000)>11/9\).  The lower cosine polynomial gives

\[
1-\frac{(613/600)^2}{2}
+\frac{(613/600)^4}{24}
-\frac{(613/600)^6}{720}
-\frac{25}{48}
=\frac{36367360087918391}
       {33592320000000000000}>0,
\tag{4.6}
\]

so \(\sec(613/600)<48/25\).  Therefore

\[
R(\phi)
<\frac{48/25-11/9}{11/9-1}
=\frac{157}{50}
<\frac{333}{106}
<\pi.
\tag{4.7}
\]

The middle exact margin is \(2/1325\).  This contradicts \(K-a>\pi\) and
proves (4.3).

### 4.2 Comparing \(\gamma-\sin\gamma\) and
\(\phi-\sin\phi\)

Put

\[
e(u)=u-\sin u.
\]

The function \(e(u)/u^{5/2}\) is strictly increasing on
\((0,\pi/2)\).  Its derivative has the sign of

\[
N(u)=5\sin u-3u-2u\cos u.
\]

Now

\[
N'(u)=2\sin(u/2)
\{2u\cos(u/2)-3\sin(u/2)\}>0.
\tag{4.8}
\]

For \(y=u/2<\pi/4\), the increasing function \(\tan y/y\) satisfies

\[
\frac{\tan y}{y}<\frac4\pi<\frac43,
\]

which gives the last sign in (4.8).  Since \(N(0)=0\), the claimed
monotonicity follows.  With (4.3),

\[
\frac{e(\phi)}{e(\gamma)}
<\left(\frac35\right)^{5/2}
<\frac27.
\tag{4.9}
\]

The last comparison is exact after squaring:
\(243\cdot49=11907<12500=4\cdot3125\).

### 4.3 A sharp enough Cauchy estimate for \(E\)

Since

\[
h(u)=\int_0^u v\sin v\,dv,
\qquad
e(u)=\int_0^u(1-\cos v)\,dv,
\]

Cauchy--Schwarz gives

\[
h(u)^2
\le e(u)I(u),
\qquad
I(u):=\int_0^u v^2(1+\cos v)\,dv.
\tag{4.10}
\]

For \(0<u\le\pi/2\),

\[
\boxed{I(u)<\frac57u^2\sin u.}
\tag{4.11}
\]

Indeed, (4.11) is equivalent to

\[
J(u):=14h(u)-\frac73u^3-2u^2\sin u>0.
\]

Here

\[
J'(u)=u^2f(u),
\qquad
f(u)=10\frac{\sin u}{u}-7-2\cos u.
\]

The function \(f\) is strictly decreasing, because

\[
f'(u)<0
\quad\Longleftrightarrow\quad
u^2\sin u<5h(u),
\]

and

\[
\{5h(u)-u^2\sin u\}'
=u\{3\sin u-u\cos u\}>0.
\]

Thus \(J'\) has at most one sign change, from positive to negative.
Since \(J(0)=0\), \(f(0)=1\), and

\[
J(\pi/2)
=14-\frac{7\pi^3}{24}-\frac{\pi^2}{2}
>14-\frac7{24}\left(\frac{22}{7}\right)^3
 -\frac12\left(\frac{22}{7}\right)^2
=\frac1{147}>0,
\tag{4.12}
\]

one gets \(J(u)>0\) throughout the interval.

Equations (4.10)--(4.11) imply

\[
E(\gamma)
=\frac{h(\gamma)^2}{\gamma^2\sin^2\gamma}
<\frac57\frac{e(\gamma)}{\sin\gamma}.
\tag{4.13}
\]

On the other hand, (1.4) and (4.9) give

\[
k-1
=\frac{e(\gamma)-e(\phi)}{\sin\gamma}
>\frac57\frac{e(\gamma)}{\sin\gamma}.
\tag{4.14}
\]

Combining (4.2), (4.13), and (4.14) proves

\[
\boxed{E(\theta)<E(\gamma)<k-1,}
\]

which is intrinsic inequality (I).

## 5. Exact checkpoint: \(g(8)<1\)

The proof of (II) needs one finite threshold.  It is certified here with
exact rational arithmetic, without solving the action equation numerically.

For \(0<x<1\), put

\[
T_n(x)=\sum_{j=0}^{n-1}\frac{(-1)^jx^{2j+1}}{2j+1}.
\tag{5.1}
\]

Then

\[
T_{2m}(x)<\arctan x<T_{2m+1}(x).
\tag{5.2}
\]

Use the Round 18 Machin-certified bounds

\[
p_-:=\frac{333}{106}<\pi<\frac{355}{113}=:p_+.
\tag{5.3}
\]

Set

\[
a_0=8,\qquad t_0=7,\qquad
K_0=\frac{229}{20},\qquad w_0=\frac{73}{20}.
\tag{5.4}
\]

At \(t_0\), exact squaring gives

\[
\frac{9061}{1000}
<\sqrt{K_0^2-t_0^2}
<\frac{9062}{1000},
\]

\[
\frac{3872}{1000}
<\sqrt{8^2-t_0^2}
<\frac{3873}{1000}.
\tag{5.5}
\]

The four positive square margins, in the order lower outer, upper outer,
lower inner, upper inner, are

\[
\frac{779}{10^6},\qquad
\frac{271}{15625},\qquad
\frac{119}{15625},\qquad
\frac{129}{10^6}.
\tag{5.6}
\]

Define

\[
\begin{aligned}
C_A:={}&\frac{9062}{1000}-\frac{3872}{1000}
-\frac{7p_-}{2}\\
&+7\left\{
T_7\!\left(\frac{7}{9061/1000}\right)
+T_7\!\left(\frac{3873/1000}{7}\right)
\right\}.
\end{aligned}
\tag{5.7}
\]

The angle identities

\[
\arccos\frac{t_0}{K_0}
=\frac\pi2-\arctan\frac{t_0}{\sqrt{K_0^2-t_0^2}},
\]

\[
\arccos\frac{t_0}{8}
=\arctan\frac{\sqrt{8^2-t_0^2}}{t_0}
\]

and (5.2)--(5.6) give

\[
\pi\{G_{K_0}(t_0)-G_8(t_0)\}<C_A.
\]

The exact rational comparison is

\[
\boxed{\frac{3p_-}{4}-C_A>\frac1{100}.}
\tag{5.8}
\]

Hence the shell action at \((K_0,8)\) is less than \(3/4\).  Since it
increases strictly with the outer radius, the actual action-face radius
\(K_8\) satisfies

\[
K_8>K_0.
\tag{5.9}
\]

At \(w_0\), exact squaring similarly gives

\[
\frac{10852}{1000}
<\sqrt{K_0^2-w_0^2}
<\frac{10853}{1000},
\]

\[
\frac{7118}{1000}
<\sqrt{8^2-w_0^2}
<\frac{7119}{1000},
\tag{5.10}
\]

with square margins

\[
\frac{881}{62500},\qquad
\frac{7609}{10^6},\qquad
\frac{1447}{125000},\qquad
\frac{2661}{10^6}.
\tag{5.11}
\]

Define

\[
C_B:=\frac{7119}{1000}-\frac{w_0p_-}{2}
+w_0T_5\!\left(\frac{w_0}{7118/1000}\right),
\tag{5.12}
\]

\[
C_C:=\frac{10852}{1000}-\frac{w_0p_+}{2}
+w_0T_4\!\left(\frac{w_0}{10853/1000}\right).
\tag{5.13}
\]

All arctangent arguments in (5.7), (5.12), and (5.13) lie in \((0,1)\).
Equations (5.2), (5.3), and (5.10) give

\[
\pi G_8(w_0)<C_B,
\qquad
\pi G_{K_0}(w_0)>C_C.
\]

The two exact margins are

\[
\boxed{p_--C_B>\frac1{50},}
\qquad
\boxed{C_C-2p_+>\frac1{60}.}
\tag{5.14}
\]

Thus

\[
G_8(w_0)<1,
\qquad
G_{K_0}(w_0)>2.
\tag{5.15}
\]

Let \(w\) be the unique point with \(G_8(w)=1\).  The first inequality in
(5.15) gives \(w<w_0\).  Combining this with (5.9) and the second inequality
in (5.15),

\[
G_{K_8}(w)>G_{K_0}(w)>G_{K_0}(w_0)>2.
\]

Hence \(A(w)>1=A(x)\).  Since \(A\) decreases and \(G_8\) decreases,

\[
x>w,
\qquad
\boxed{g(8)=G_8(x)<G_8(w)=1.}
\tag{5.16}
\]

## 6. Proof of intrinsic inequality (II)

By (2.12), (II) is equivalent to

\[
\boxed{
3g-H
=2(s-k)g^2+k(1-g)>0.}
\tag{6.1}
\]

We first record three global bounds.

At the simultaneous wall,

\[
\cos\gamma_*
=\frac{a_*-1}{a_*+\pi}
>\frac{9/2}{11/2+22/7}
=\frac{63}{121}>\frac12.
\]

Here the ratio \((a-1)/(a+\pi)\) increases in \(a\), and (3.1) was used.
Since \(\gamma\) decreases along the strict face,

\[
\boxed{\gamma<\frac\pi3.}
\tag{6.2}
\]

The function \(e(u)/\sin u\) is strictly increasing because its derivative
has numerator \(h(u)>0\).  Therefore

\[
k-1
<\frac{e(\gamma)}{\sin\gamma}
<\frac{e(\pi/3)}{\sin(\pi/3)}
=\frac{2\pi}{3\sqrt3}-1
<\frac14.
\]

The last sign follows from

\[
8\pi<\frac{176}{7}<15\sqrt3,
\qquad
675-\left(\frac{176}{7}\right)^2=\frac{2099}{49}>0.
\]

Thus

\[
\boxed{1<k<\frac54.}
\tag{6.3}
\]

At the simultaneous wall, \(x=0\), so \(g_*=a_*/\pi\).  By (3.6), the
Round 18 upper bracket, and \(p_->25/8\),

\[
\boxed{0<g<g_*<\frac{45/8}{25/8}=\frac95.}
\tag{6.4}
\]

If \(g\le1\), (6.1) follows immediately from \(s-k>0\) and \(k>0\).

Suppose \(g>1\).  Since \(g\) decreases and (5.16) holds, necessarily
\(a<8\).  Hence

\[
\cos\phi=1-\frac1a<\frac78<\cos\frac12,
\qquad
\phi>\frac12.
\tag{6.5}
\]

The middle strict sign follows from
\(\cos u>1-u^2/2\) at \(u=1/2\).

Using \(\gamma<\pi/2\), \(a<8\), \(\sin\gamma<1\), (1.5), and (6.3),

\[
\begin{aligned}
\frac{s-k}{k}
&=\frac{3\pi/4-\gamma+\phi}{a\sin\gamma\,k}\\
&>\frac{(\pi+2)/4}{8(5/4)}
=\frac{\pi+2}{40}
>\frac18.
\end{aligned}
\tag{6.6}
\]

The last comparison is exact from (5.3):

\[
\frac{p_-+2}{40}-\frac18=\frac3{848}>0.
\]

On \(1<g<9/5<2\), the function \((g-1)/(2g^2)\) increases.  Thus

\[
\frac{g-1}{2g^2}
<\frac{10}{81}
<\frac18,
\qquad
\frac18-\frac{10}{81}=\frac1{648}>0.
\tag{6.7}
\]

Combining (6.6)--(6.7),

\[
\frac{s-k}{k}>\frac{g-1}{2g^2},
\]

which is exactly (6.1).  This proves intrinsic inequality (II) globally.

## 7. Derivative and geometric closure

If \(m\le3/4\), positivity follows from (2.10).  If \(m>3/4\), intrinsic
inequalities (I) and (II) in (2.14) give

\[
\frac{3g(k-1)}{E(\theta)}>3g>H,
\]

and therefore

\[
\boxed{\frac{dF}{da}>0}
\]

at every point of the strict action face.

The boundary calculus now has a single minimum:

1. Round 16 proved \(F_K>0\), so fixed-\(a\) minimization reaches either
   \(K=a+\pi\) or the action face.
2. On \(K=a+\pi\), Round 16 proved \(dF/da<0\), so that face decreases
   toward the simultaneous wall.
3. On the action face, the present result proves \(dF/da>0\), so that face
   increases away from the simultaneous wall.
4. Round 18 proved at the wall

   \[
   F>\frac12+\frac{1443}{449440}>\frac12.
   \]

Thus the enlarged geometric lemma from Round 16 is closed:

\[
\boxed{F(K,a)\ge\frac12}
\]

on the whole endpoint domain; in fact the boundary comparison is strict.
Round 16's exact reduction then gives

\[
D_{A_\alpha}(r)>
\Omega_{\rm end}
\ge2F-1+2\eta>0
\]

for the hard \(B=1\), first-floor endpoint branch.

## 8. Equality and wall audit

1. The derivative proof is made only on the strict face \(K-a>\pi\), hence
   \(a>a_*\), \(x>0\), and \(q<p\).  The simultaneous equality
   \(K-a=\pi\) is not silently inserted into an open-face formula; it is
   handled by Round 18.
2. As the simultaneous wall is approached, \(x\to0\) and \(q\to p\).
   No strict two-interval Jensen assertion is needed at that endpoint.
3. The internal equality \(m=3/4\) belongs to the first case (2.10), where
   the reserve \(g(k-1)U(3/4)\) is still strict.
4. The checkpoint \(g(8)<1\) uses only strict monotonicity and displayed
   rational inequalities.  No decimal approximation to \(K_8\), \(x\), or
   \(g(8)\) enters the proof.
5. The inverse-level convention \(G_K(z)=3/4\), the one-sided action wall,
   and the floor/shelf ownership conventions are unchanged.  No literal
   lower action wall is identified with its open-side endpoint.
6. The first-floor conclusion is a consequence of the already-proved Round
   16 reduction.  It does not settle or import any high-floor CST claim.

## 9. Dependency and loss ledger

- **Imported from Round 16:** the enlarged endpoint domain, the functional
  \(F\), the exact derivative (1.2), convexity and monotonicity of the
  quantile profile, \(F_K>0\), the radial-face derivative, and the endpoint
  reduction with reserve \(2\eta\).
- **Imported from Round 17:** the quantile primitive and scaling formula,
  the speed identity (1.5), and the endpoint sinc comparison used in the
  proof of \(g'<0\).  The former chord scalar \(\mathcal S\) is bypassed.
- **Imported from Round 18:** uniqueness and the bracket
  \(11/2<a_*<45/8\), the Machin-certified bounds
  \(333/106<\pi<355/113\), and the exact simultaneous-wall reserve.
- **Proved here:** the exact Jensen reduction (2.9)--(2.14), intrinsic
  inequalities (I) and (II), global decrease of \(\gamma\) and \(g\), the
  exact checkpoint \(g(8)<1\), and the strict action-face derivative.
- **Deliberate one-sided losses:** two Jensen steps, one tangent bound at
  level \(3/4\), replacement of \(E(\theta)\) by \(E(\gamma)\), the coarse
  global bounds \(\gamma<\pi/3\), \(k<5/4\), \(g<9/5\), and the rational
  radical/angle brackets at \(a=8\).  Every loss is followed by a strict
  analytic or exact rational margin.
- **Not used:** interval subdivision, a ratio ladder, floating-point root
  certification, the Round 17 numerical chord values, or asymptotic
  numerics.

The accompanying Wolfram Language replay
`computations/general_d_round19_action_face_jensen_replay.wl` checks the
Jensen algebra, slope identity, all finite rational margins, and the complete
\(a=8\) certificate exactly.  It also prints one separate high-precision
diagnostic at \(a=8\); that diagnostic is not a premise of the proof.

## 10. Gate decision

The continuous geometric obligation left open in Rounds 16--18 is now
proved.  The appropriate next step is an end-to-end audit inserting the
geometric lemma into the first-floor workflow before changing WP2 status.
The high-floor CST and the general all-dimensional theorem remain separate
open obligations.
