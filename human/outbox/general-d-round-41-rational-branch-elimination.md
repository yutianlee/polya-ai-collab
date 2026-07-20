# General-dimensional spherical-shell Pólya project
## Round 41: rational enclosure and Bernstein candidate for the upper-alpha midpoint target

**Date:** 20 July 2026  
**Status:** exact computer-assisted candidate for the Round 40
selected-scalar endpoint; the 4,405-sign Bernstein certificate is not an
authorized analytic closure under the revised strategy; selected
\(\Gamma_{\rm OB}\to\mathcal R_*\) projection exhausted; no CST or
theorem-status promotion

## 0. Theorem boundary and dependencies

This note treats only the intrinsic continuum target left by Round 40 at the
gap-side outer-\(B\), upper-alpha endpoint. Round 40 proved the strict
implication

\[
 \Gamma_{\rm OB}>\mathcal R_*(p,m,t)
\tag{0.1}
\]

and reduced the desired sign of \(\mathcal R_*\) to two convex analytic
branches. The exact wall ownership, selected-scalar loss ledger, and
one-sided \(\alpha\uparrow1^-\) convention remain those printed in
`human/outbox/general-d-round-40-upper-alpha-midpoint-reduction.md`.
They are not rederived or altered here.

The domain is

\[
 p\geq3,\qquad m\geq1,\qquad p>dm,
 \qquad 0<t<\frac\pi2,
 \qquad d=1-\frac{2t}{\pi}.
\tag{0.2}
\]

No new theorem-owner subdivision by \(B_0\), \(j\), a shell ratio, or an
integer floor is introduced. The only theorem alternatives below are the
two analytic branches of the single maximum already present in Round 40,
followed by the ordinary endpoint/critical-point alternatives for one
convex function. The rational subintervals in Section 4 are finite
verification cells only, not new theorem owners or geometric chambers.

The exploratory real-algebraic companion is

`computations/general_d_round41_rational_branch_obstruction.wl`.

The final fixed-cell sign replay is

`computations/general_d_round41_bernstein_sign_replay.wl`.

The latter uses exact rational arithmetic only. It makes no
`Resolve`/`Reduce`/CAD call and does not use numerical sampling. Mathematica
does not own a strict bracket or endpoint label, but it does own the finite
coefficient-sign audit in Section 4. That load-bearing role is why the
result is classified as a computer-assisted candidate rather than an
analytic closure.

## 1. Global rational trigonometric enclosure

Put

\[
 s:=\frac{2t}{\pi}=1-d,
 \qquad 0<s<1,
 \qquad
 L_0(t)=\frac{\tan t-t}{\pi}.
\tag{1.1}
\]

Define

\[
 \ell_-(s):=\frac{49s^3}{121(1-s^2)},
 \qquad
 \ell_+(s):=\frac{121s^3}{294(1-s^2)}.
\tag{1.2}
\]

### Lemma 1.1

For \(0<s<1\),

\[
 \boxed{\ell_-(s)<L_0(t)<\ell_+(s).}
\tag{R41.1}
\]

#### Proof

The partial-fraction expansion of the tangent gives

\[
 \tan\frac{\pi s}{2}
 =\frac{4s}{\pi}
 \sum_{n\geq1}
 \frac1{(2n-1)^2-s^2}.
\tag{1.3}
\]

Using \(\sum_{n\geq1}(2n-1)^{-2}=\pi^2/8\), subtracting
\(\pi s/2\), and dividing by \(\pi\) yields the positive expansion

\[
 L_0(t)=\frac{4s^3}{\pi^2}
 \sum_{n\geq1}
 \frac1{(2n-1)^2\{(2n-1)^2-s^2\}}.
\tag{1.4}
\]

Keeping only the \(n=1\) term and using \(\pi<22/7\) gives

\[
 L_0(t)>
 \frac{4s^3}{\pi^2(1-s^2)}
 >\frac{49s^3}{121(1-s^2)}.
\tag{1.5}
\]

For the upper bound, use the global tangent majorant retained from Round 39,

\[
 \tan x<
 \frac{x\{\pi^2+(\pi^2/3-4)x^2\}}
      {\pi^2-4x^2},
 \qquad 0<x<\frac\pi2.
\tag{1.6}
\]

After subtracting \(x\), dividing by \(\pi\), and putting
\(x=\pi s/2\), this gives

\[
 L_0(t)<\frac{\pi^2s^3}{24(1-s^2)}
 <\frac{121s^3}{294(1-s^2)},
\tag{1.7}
\]

where the last inequality again uses \(\pi<22/7\). \(\square\)

Next define the rational functions

\[
 \mathsf A_-(s):=
 \frac{333s^2}{848}-\frac{1331s^4}{16464},
\tag{1.8}
\]

\[
 T(s):=\frac{11s}{7},
 \qquad
 P_5(T):=T-\frac{T^3}{6}+\frac{T^5}{120},
 \qquad
 \mathsf S_+(s):=2+P_5(T(s))^2.
\tag{1.9}
\]

### Lemma 1.2

For \(0<s<1\),

\[
 \boxed{
  0<\mathsf A_-(s)<\frac{1-\cos t}{\pi},
  \qquad
  2+\sin^2t<\mathsf S_+(s).}
\tag{R41.2}
\]

#### Proof

The global Taylor inequality from Round 40 gives

\[
 \frac{1-\cos t}{\pi}>
 \frac{t^2/2-t^4/24}{\pi}
 =\frac{\pi s^2}{8}-\frac{\pi^3s^4}{384}.
\tag{1.10}
\]

Now use \(333/106<\pi<22/7\). The positive quadratic coefficient is
replaced downward and the subtracted quartic coefficient upward:

\[
 \frac{\pi s^2}{8}-\frac{\pi^3s^4}{384}
 >\frac{333s^2}{848}
  -\frac{(22/7)^3s^4}{384}
 =\mathsf A_-(s).
\tag{1.11}
\]

Moreover,

\[
 \mathsf A_-(s)>
 s^2\left(\frac{333}{848}-\frac{1331}{16464}\right)
 =\frac{136057}{436296}s^2>0.
\tag{1.12}
\]

For the sine term,

\[
 \sin t<t-\frac{t^3}{6}+\frac{t^5}{120}.
\tag{1.13}
\]

The polynomial on the right is positive and strictly increasing on
\([0,11/7]\), because its derivative is
\(1-x^2/2+x^4/24>0\) there. Since \(t<11s/7=T(s)\),

\[
 0<\sin t<P_5(T(s)),
\]

which proves the second inequality. \(\square\)

All denominators in (1.2), (1.8), and (1.9) are positive on
\(0<s<1\). These facts will be used explicitly before every squaring.

## 2. Branch I: rational convex envelope

On the geometric branch,

\[
 (p+m+2)L_0(t)\geq\frac54,
\tag{2.1}
\]

Round 40 uses

\[
 a=\frac{p/2+1}{p+m+2},
 \qquad
 a_h=\frac{d(p+2)}{2\{p+d(p+2)\}}.
\tag{2.2}
\]

The exact domain satisfies

\[
 a>a_h,
 \qquad
 a\leq\frac{2(p+2)L_0(t)}5.
\tag{2.3}
\]

Define the rational upper endpoint

\[
 u_I:=\frac{2(p+2)\ell_+(s)}5.
\tag{2.4}
\]

By (R41.1), every feasible point satisfies

\[
 0<a_h<a<u_I.
\tag{2.5}
\]

Also put

\[
 H_I^-:=2d+\frac{49s^2}{121(1+s)},
 \qquad
 X_I^-:=\frac{(p+2)H_I^-}{8},
\tag{2.6}
\]

\[
 D_I^+:=\mathsf S_+(s)-2a_h,
 \qquad
 Y_I^-:=\frac{p^2\mathsf A_-(s)}{\sqrt{D_I^+}},
\tag{2.7}
\]

and

\[
 c_I:=\frac9{10}+\frac{9d}{16s}
      -\frac{p(2-s)}2-d.
\tag{2.8}
\]

The exact coefficient in Round 40 is

\[
 X_I=\frac{p+2}{8}\{\zeta L_0(t)+2d\}.
\]

Since \(\zeta=d/s\), (R41.1) gives

\[
 \zeta L_0(t)>
 \frac ds\ell_-(s)
 =\frac{49s^2}{121(1+s)},
\]

and therefore \(X_I>X_I^-\).

Next, \(a>a_h\), (R41.2), and denominator monotonicity give

\[
 \begin{aligned}
 \frac{p^2(1-\cos t)a}
      {\pi\sqrt{2+\sin^2t-2a}}
 &>
 \frac{p^2\mathsf A_-(s)a}
      {\sqrt{\mathsf S_+(s)-2a_h}}\\
 &=Y_I^-a.
 \end{aligned}
\tag{2.9}
\]

There is no hidden denominator sign here: \(a_h<1/2\), hence

\[
 D_I^+>2-2a_h>1.
\tag{2.10}
\]

Thus the exact Branch-I scalar satisfies

\[
 \boxed{
 \mathcal R_I>
 c_I+\frac{X_I^-}{a}+Y_I^-a,
 \qquad a_h<a<u_I.}
\tag{R41.3}
\]

Let

\[
 a_0:=\sqrt{\frac{X_I^-}{Y_I^-}}.
\tag{2.11}
\]

The function \(X_I^-/a+Y_I^-a\) is strictly convex. Only two lower
envelopes are required.

### Case I-A: \(a_0\leq u_I\)

AM--GM gives

\[
 \frac{X_I^-}{a}+Y_I^-a
 \geq2\sqrt{X_I^-Y_I^-}.
\tag{2.12}
\]

Because all factors are positive,

\[
 a_0\leq u_I
 \quad\Longleftrightarrow\quad
 \mathsf K_I:=
 p^4\mathsf A_-^2u_I^4-(X_I^-)^2D_I^+\geq0.
\tag{2.13}
\]

If \(c_I\geq0\), (R41.3) is already positive. If \(c_I<0\), both sides
of

\[
 2\sqrt{X_I^-Y_I^-}>-c_I
\]

are positive. Squaring twice is therefore reversible and gives

\[
 \mathsf P_{I,A}:=
 16(X_I^-)^2p^4\mathsf A_-^2-c_I^4D_I^+>0.
\tag{2.14}
\]

### Case I-B: \(a_0\geq u_I\)

The convex function is decreasing up to \(a_0\). Hence, for every
\(a<u_I\),

\[
 \frac{X_I^-}{a}+Y_I^-a
 \geq\frac{X_I^-}{u_I}+Y_I^-u_I.
\tag{2.15}
\]

This case is \(\mathsf K_I\leq0\). Put

\[
 E_I:=c_I+\frac{X_I^-}{u_I}.
\tag{2.16}
\]

If \(E_I\geq0\), positivity is immediate. If \(E_I<0\), the remaining
comparison has positive sides and one reversible squaring gives

\[
 \mathsf P_{I,B}:=
 p^4\mathsf A_-^2u_I^2-E_I^2D_I^+>0.
\tag{2.17}
\]

Consequently a nonpositive Branch-I rational envelope would give a real
solution of

\[
 \begin{aligned}
 \mathfrak C_I:\quad
 &0<s<1,\quad p\geq3,\quad a_h<u_I,\\
 &\bigl(
   \mathsf K_I\geq0,\ c_I<0,\ \mathsf P_{I,A}\leq0
  \bigr)\\
 &\quad\text{or}\quad
 \bigl(
   \mathsf K_I\leq0,\ E_I<0,\ \mathsf P_{I,B}\leq0
  \bigr).
 \end{aligned}
\tag{R41.4}
\]

Every denominator occurring in (R41.4) is positive by
\(0<s<1\), \(p\geq3\), and (2.10). Clearing those denominators therefore
does not reverse a sign. The three Branch-I numerator bidegrees printed by
the replay are \((21,9)\), \((21,7)\), and \((23,7)\); their componentwise
maximum is \((23,9)\).

## 3. Branch II: two lower walls and a linear envelope

On the phase branch,

\[
 (p+m+2)L_0(t)<\frac54,
 \qquad
 \mu_0=\frac5{4L_0(t)},
\tag{3.1}
\]

and Round 40 uses

\[
 a=1-\frac{p/2+m+1}{\mu_0},
 \qquad 0<a<1.
\tag{3.2}
\]

Rewrite its exact scalar as

\[
 \mathcal R_{II}=c_{II}
 +M_{II}(1-a)
 +\frac{p^2(1-\cos t)a}
       {\pi\sqrt{2+\sin^2t-2a}},
\tag{3.3}
\]

where

\[
 c_{II}:=\frac9{10}+\frac{7d}{8s}
 -\frac{p(3-s)}4-\frac d2,
 \qquad
 M_{II}:=\frac{5d}{8L_0(t)}.
\tag{3.4}
\]

Define

\[
 g:=\frac{4\ell_-(s)(p/2+1)}5,
\tag{3.5}
\]

\[
 h:=1-
 \frac{4\ell_+(s)\{p(1+d/2)+d\}}{5d},
 \qquad
 b:=\max\{g,h\},
\tag{3.6}
\]

and

\[
 M^-:=\frac{5d}{8\ell_+(s)}.
\tag{3.7}
\]

The strict phase inequality in (3.1) gives

\[
 a>\frac{p/2+1}{\mu_0}
 =\frac{4L_0(t)(p/2+1)}5>g.
\tag{3.8}
\]

The strict hard inequality \(p>dm\) gives

\[
 a>
 1-\frac{p(1+d/2)+d}{d\mu_0}
 =1-\frac{4L_0(t)\{p(1+d/2)+d\}}{5d}>h.
\tag{3.9}
\]

The last direction is correct because the subtracted coefficient is
positive and \(L_0<\ell_+\). Thus

\[
 0<b<a<1.
\tag{3.10}
\]

Also \(M_{II}>M^-\). Define

\[
 D_b^+:=\mathsf S_+(s)-2b,
 \qquad
 Y_b^-:=\frac{p^2\mathsf A_-(s)}{\sqrt{D_b^+}}.
\tag{3.11}
\]

Because \(b<1\) and \(\mathsf S_+>2\),

\[
 D_b^+>2-2b>0.
\tag{3.12}
\]

Exactly as in (2.9), the action term is strictly larger than \(Y_b^-a\).
Since \(1-a>0\), replacing \(M_{II}\) by \(M^-\) is also a lower bound.
Therefore

\[
 \boxed{
 \mathcal R_{II}>
 c_{II}+M^-(1-a)+Y_b^-a,
 \qquad b<a<1.}
\tag{R41.5}
\]

The right side is affine in \(a\). Write

\[
 Y_b^-:=\frac{p^2\mathsf A_-}{\sqrt{D_b^+}},
 \qquad
 E_b:=c_{II}+M^-(1-b).
\tag{3.13}
\]

Its slope is \(Y_b^--M^-\). If this slope is nonnegative, the lower
endpoint gives the envelope. When \(E_b<0\), the sign-safe squared
comparison is

\[
 \mathsf P_b^+:=
 p^4\mathsf A_-^2b^2-E_b^2D_b^+\geq0.
\tag{3.14}
\]

For the nonpositive-slope case retain more of the actual domain than the
coarse endpoint \(a=1\). From \(m\geq1\), (3.2), and
\(L_0>\ell_-\),

\[
 a<u_P:=1-\frac{2\ell_-(s)(p+4)}5.
\tag{3.15}
\]

Also, (3.1) gives

\[
 (p+3)\ell_-<\frac54,
 \qquad
 p<p_M:=\frac5{4\ell_-}-3.
\tag{3.16}
\]

Thus \(u_P>u_P(p_M)>5/12\). If the affine slope is nonpositive,
its value at the actual \(a<u_P\) is at least its value at \(u_P\). Put

\[
 e_U:=c_{II}+M^-(1-u_P),
\tag{3.17}
\]

and, for \(b=g\) or \(h\),

\[
 \mathsf P_b^U:=
 p^4\mathsf A_-^2u_P^2-e_U^2D_b^+.
\tag{3.18}
\]

If \(e_U\geq0\), positivity at \(u_P\) is immediate. If \(e_U<0\),
then \(\mathsf P_b^U\geq0\) is exactly the sign-safe squared comparison
\(Y_b^-u_P\geq-e_U\). All quantities squared here are nonnegative, and
\(D_b^+>0\), \(u_P>0\).

Finally the phase domain lies in the fixed strip

\[
 0<s<\frac23.
\tag{3.19}
\]

Indeed, \(\ell_-\) is strictly increasing because

\[
 \ell_-'(s)=\frac{49s^2(3-s^2)}{121(1-s^2)^2}>0,
\]

whereas \((p+3)\ell_-<5/4\) and \(p\geq3\) give
\(\ell_-<5/24\), while

\[
 \ell_-(2/3)-\frac5{24}=\frac{37}{4840}>0.
\]

## 4. Fixed exact Bernstein sign certificate

The final sign computation uses the following finite rule. If
\(P(\alpha+(\beta-\alpha)z)=\sum_{j=0}^n a'_jz^j\), define

\[
 b_k=\sum_{j=0}^k
 a'_j\frac{\binom{k}{j}}{\binom{n}{j}}.
\tag{4.1}
\]

Then

\[
 P=\sum_{k=0}^n b_k\binom nk z^k(1-z)^{n-k}.
\tag{4.2}
\]

Thus nonnegative \(b_k\) prove \(P\geq0\) on the cell. Applying (4.1)
in both variables gives

\[
 b_{k\ell}=\sum_{i\leq k}\sum_{j\leq\ell}
 a'_{ij}
 \frac{\binom{k}{i}}{\binom{n}{i}}
 \frac{\binom{\ell}{j}}{\binom{m}{j}}.
\tag{4.3}
\]

The tensor Bernstein basis is again nonnegative. Equations (4.1)--(4.3)
follow by expanding monomials in the fixed-degree Bernstein basis.

### 4.1 Branch I-B: cubic discriminant

The identity

\[
 a_h-\frac{d}{2(1+d)}
 =\frac{d}{(1+d)\{p+d(p+2)\}}>0
\]

gives

\[
 D_I^+<D_0:=\mathsf S_+-\frac{d}{1+d}.
\tag{4.4}
\]

Put

\[
 \begin{aligned}
 E&:=\frac9{10}+\frac{9d}{16s}-d
      +\frac{5H_I^-}{16\ell_+},&
 C&:=\frac{2-s}{2},\\
 K&:=\frac{2\ell_+\mathsf A_-}{5},&
 k&:=\frac{K}{\sqrt{D_0}}.
 \end{aligned}
\tag{4.5}
\]

The Case-I-B endpoint in (2.15) is strictly larger than

\[
 f_s(p):=E-Cp+kp^2(p+2).
\tag{4.6}
\]

Moreover,

\[
 \frac9{10}+\frac{9d}{16s}-d-\frac{67}{80}
 =\frac{(4s-3)^2}{16s}\geq0,
\tag{4.7}
\]

so \(E>0\). Define

\[
 Q:=4C^2-36CE-27E^2.
\tag{4.8}
\]

Since \(0<C<1\) and \(E\geq67/80\),
\(Q<4-27(67/80)^2<0\). Direct expansion gives

\[
 \operatorname{Disc}_p(f_s)
 =k\{4C^3+kQ-32k^2E\}.
\tag{4.9}
\]

The rational function

\[
 Z:=K^2Q^2-16C^6D_0
\tag{4.10}
\]

has denominator \(C_Z(s-1)^2s^2(1+s)^2>0\) and a degree-22
numerator. All 23 Bernstein coefficients of that numerator are positive
on each of

\[
 [0,1/3],\qquad[1/3,2/3],\qquad[2/3,1].
\tag{4.11}
\]

Thus \(Z>0\), equivalently \(k(-Q)>4C^3\), and (4.9) is negative.
The cubic has one real root. Since \(f_s(0)=E>0\) and its leading
coefficient is positive, that root is negative. Hence \(f_s(p)>0\)
for every \(p\geq0\).

### 4.2 Branch I-A: two unbounded-\(p\) charts

Define

\[
 \mathsf P_{A,0}:=
 \frac{(H_I^-)^2\mathsf A_-^2p^4(p+2)^2}{4}
 -c_I^4D_0.
\tag{4.12}
\]

By (4.4), \(\mathsf P_{I,A}\geq\mathsf P_{A,0}\) globally, with
strict inequality in the countercase \(c_I<0\). A hypothetical
Case-I-A counterexample has \(a_0\leq u_I\) and
\(2\sqrt{X_I^-Y_I^-}\leq-c_I\). Hence

\[
 -c_I\geq2\sqrt{X_I^-Y_I^-}
 \geq\frac{2X_I^-}{u_I}
 =\frac{5H_I^-}{8\ell_+},
\tag{4.13}
\]

so

\[
 p\geq p_0(s):=
 \frac{c_I|_{p=0}+5H_I^-/(8\ell_+)}{C}.
\tag{4.14}
\]

For \(0<s\leq2/3\), substitute \(p=p_0+x\), \(x\geq0\), in
\(\mathsf P_{A,0}\). Its denominator is a positive constant times
\((s-2)^6s^{14}(1+s)^2\). The result is degree six in \(x\);
the coefficient-polynomial degrees are
\((32,33,34,35,36,32,32)\). Their aggregate Bernstein counts are

\[
\begin{array}{c|c}
s\text{-cell}&(\#+,\#0,\#-)\\ \hline
[0,1/3]&(178,63,0)\\
[1/3,2/3]&(241,0,0).
\end{array}
\tag{4.15}
\]

For \(2/3\leq s<1\), put \(p=3+x\). The denominator is a positive
constant times \((s-2)s^4(1+s)^2<0\). After multiplying the numerator
by \(-1\), all 146 coefficient-level Bernstein entries on
\([2/3,1]\) are positive. Thus the exact table gives
\(\mathsf P_{A,0}\geq0\) on the necessary domain.

### 4.3 Branch II: nonnegative slope

If \(h\) owns the lower wall, then

\[
 E_h=c_{II}+M^-(1-h)
 =\frac9{10}+\frac{7d}{8s}>0.
\tag{4.16}
\]

Suppose \(g\) owns. If its endpoint were nonpositive while
\(Y_g^--M^-\geq0\), then

\[
 c_{II}+M^-=E_g+M^-g
 \leq E_g+Y_g^-g\leq0.
\tag{4.17}
\]

The left side is decreasing affine in \(p\), so

\[
 p\geq p_C(s):=
 \frac{7350-7350s-3115s^2+5051s^3+2420s^4}
 {1210(3-s)s^3}.
\tag{4.18}
\]

After \(p=p_C+x\), \(x\geq0\), the denominator of
\(\mathsf P_g^+\) is a positive constant times
\((s-3)^6(s-1)^2s^8(1+s)^2\). The numerator is degree six in
\(x\), with coefficient-polynomial degrees
\((28,29,30,28,28,28,28)\), and aggregate counts

\[
\begin{array}{c|c}
s\text{-cell}&(\#+,\#0,\#-)\\ \hline
[0,1/3]&(143,63,0)\\
[1/3,2/3]&(206,0,0).
\end{array}
\tag{4.19}
\]

Thus the table gives \(\mathsf P_g^+\geq0\).

### 4.4 Branch II: nonpositive slope at \(u_P\)

The affine function \(e_U\) is strictly decreasing in \(p\), because

\[
 4\,\partial_pe_U=-(3-s)+(1-s)\frac{\ell_-}{\ell_+}<-2.
\tag{4.20}
\]

Let \(p_E\) be its zero and \(p_X\) the unique solution of \(g=h\).
Here

\[
 p_E=\frac{512435+298061s-283420s^2}
 {10s(29517-235s)}.
\tag{4.21}
\]

Since \(g-h\) is strictly increasing in \(p\), hard-wall ownership means
\(p\leq p_X\), and geometric-wall ownership means \(p\geq p_X\).

For hard-wall ownership, a nontrivial endpoint comparison requires

\[
 p_E<p\leq p_X.
\tag{4.22}
\]

Map this interval by \(p=p_E+v(p_X-p_E)\), \(0\leq v\leq1\).
The normalized numerator of \(\mathsf P_h^U\) has bidegree \((36,6)\).
Its tensor Bernstein counts are

\[
\begin{array}{c|c|c}
s\text{-cell}&v\text{-cell}&(\#+,\#0,\#-)\\ \hline
[0,1/3]&[0,1/2]&(239,20,0)\\
[0,1/3]&[1/2,1]&(259,0,0)\\
[1/3,1/2]&[0,1/2]\text{ or }[1/2,1]&(259,0,0)\\
[1/2,27/50]&[0,1/2]\text{ or }[1/2,1]&(259,0,0).
\end{array}
\tag{4.23}
\]

Its denominator is a positive constant times

\[
 (s-1)^2s^8(1+s)^2(235s-29517)^6(29047s-58329)^6.
\tag{4.24}
\]

The remainder is empty. Exactly,

\[
 p_X-p_E=
 \frac{F(s)}
 {10s^3(235s-29517)(29047s-58329)},
\tag{4.25}
\]

where the denominator is positive on \(0<s<2/3\), and

\[
\begin{aligned}
F(s)={}&26250943950-26459941200s-55931767815s^2\\
&+6811434596s^3+42264512677s^4-8369021640s^5.
\end{aligned}
\tag{4.26}
\]

All six Bernstein coefficients of \(-F\) on \([27/50,2/3]\) are
positive, so (4.22) is impossible there.

For geometric-wall ownership, a nontrivial comparison satisfies

\[
 \max\{p_X,p_E\}<p<p_M.
\tag{4.27}
\]

For \(0<s\leq1/2\), map the containing interval
\(p=p_X+v(p_M-p_X)\). For \(1/2\leq s<2/3\), use
\(p=p_E+v(p_M-p_E)\). The normalized numerator of
\(\mathsf P_g^U\) has bidegree \((30,6)\). On each of the eight cells

\[
\begin{aligned}
&[0,1/3]\times[0,1/2],\quad [0,1/3]\times[1/2,1],\\
&[1/3,1/2]\times[0,1/2],\quad [1/3,1/2]\times[1/2,1],\\
&[1/2,3/5]\times[0,1/2],\quad [1/2,3/5]\times[1/2,1],\\
&[3/5,2/3]\times[0,1/2],\quad [3/5,2/3]\times[1/2,1],
\end{aligned}
\tag{4.28}
\]

all 217 tensor coefficients are positive. The two chart denominators are
positive constants times
\((s-1)^2s^8(1+s)^2(29047s-58329)^6\) and
\((s-1)^2s^8(1+s)^2(235s-29517)^6\), respectively.
Thus the table gives \(\mathsf P_g^U\geq0\).

### 4.5 Exact replay and strategy classification

The fixed replay prints

\[
 \mathtt{round41BernsteinSignReplayOK=True}.
\tag{4.29}
\]

It prints every denominator factor, degree, cell, and sign count reported
above. In total the proof uses 4,405 load-bearing Bernstein coefficient
signs: 4,259 positive and 146 zero. The zeros occur in cells touching
\(s=0\), so they do not impair the computer-assisted implication. If this
finite certificate were admitted, the strict inequalities (R41.3) and
(R41.5) would yield

\[
 \mathcal R_I>0,\qquad
 \mathcal R_{II}>0,\qquad
 \mathcal R_*(p,m,t)>0.
\tag{R41.C}
\]

It is not, however, an authorized analytic closure under the revised
strategy. Aggregate sign counts for 4,405 coefficients are not the short
hand-checkable wall algebra allowed by the Section 11.6 exception; they are
a new finite computer certificate. Therefore (R41.C) is recorded only as
an exact computer-assisted candidate and is not promoted.

## 5. Scope, audit, and next gate

Round 41 analytically exhausts the selected
\(\Gamma_{\rm OB}\to\mathcal R_*\) projection: after the rational
enclosures and structural reductions, its remaining sign is precisely the
unauthorized certificate in Section 4. This does not close the Round 40
endpoint analytically, any other unowned one-level-gap face, the high-floor
CST, the branching aggregate, or the all-dimensional Pólya theorem. No
state file or proof-obligation status is changed by this note.

The revised-strategy next step is the one permitted stronger exact attempt
through \(\mathcal H_\Delta\) or \(\Phi_\delta^+\), using the Round 38 formula
(R38.20). Gate B is triggered only if that stronger sign is false or again
requires a forbidden partition or finite certificate. The successful
replay remains useful as structural evidence and as an audit target, but
must not be cited as a strategy-compliant analytic proof.
