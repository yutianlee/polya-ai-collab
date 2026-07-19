# General dimension round 04b: high-floor cutoff and the critical thin ray

Date: 18 July 2026  
Scope: the terminal-shelf scalar when the first ordinary floor
\(F_0=f\ge2\)  
Status: two rigorous automatic sectors and a rigorous nonnegative
critical scaling limit, with strict overpayment of every negative
leading prefix; no uniform cutoff in \(f\) has yet been proved at the
thin endpoint.

Use

\[
 \varepsilon=1-\rho,\qquad
 a=\varepsilon K=K-\mu,\qquad
 h=f-\frac14.
\]

The active high-floor condition gives

\[
 a>\pi h.                                             \tag{1}
\]

As before,

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad
 m=n-p,\qquad d=\frac{2\arcsin\rho}{\pi},
\]

and the exact scalar is

\[
 \mathscr S=D_A(q)+R_p+\frac d2m.                    \tag{2}
\]

The case \(p=0\) is automatic.  Ordinary floors define the shelf;
strict brackets define the terminal count.  Thus the statements below
retain the favorable strict convention at every action wall.

## 1. A completely explicit cutoff away from the thin endpoint

Recall the fixed-ratio threshold from Proposition 5.6 of the general
dimension manuscript:

\[
 K_0(\rho)=
 \frac{\alpha_\rho+2\eta_\rho C_*
 +\sqrt{\alpha_\rho^2+4\alpha_\rho\eta_\rho C_*+\eta_\rho^2}}
 {2\eta_\rho^2},
\]

where

\[
 \alpha_\rho=\frac{2\pi\rho}{1-\rho},\qquad
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 C_*=\frac12+\frac{8\sqrt2}{15}.
\]

### Proposition 1.1

If

\[
 0<\rho\le\frac{99}{100},
 \qquad
 f\ge 2\,358\,517\,285,
                                                        \tag{3}
\]

then the shifted-tail inequality is already covered by the fixed-ratio
high-energy theorem.

### Proof

For \(\rho\le99/100\), monotonicity of \(G_1\) gives

\[
 \eta_\rho\ge G_1(99/100).
\]

The turning lower bound

\[
 G_1(1-t)\ge\frac{2\sqrt2}{3\pi}t^{3/2}
\]

and

\[
 \sqrt2>\frac75,\qquad \pi<\frac{22}{7}
\]

give

\[
 \eta_\rho>\frac{49}{165000}=:\eta_0.                \tag{4}
\]

Also

\[
 \alpha_\rho<623,\qquad C_*<\frac{13}{10},
 \qquad \eta_\rho<\frac13.
\]

The radicand in the formula for \(K_0\) is smaller than

\[
 623^2+4\cdot623\cdot\frac13\cdot\frac{13}{10}
 +\frac19<624^2.
\]

Consequently

\[
 K_0(\rho)
 <\frac{624}{\eta_0^2}
 =\frac{16\,988\,400\,000\,000}{2401}
 =:\overline K.                                      \tag{5}
\]

For the integer in (3), the exact rational comparison is

\[
 3\left(2\,358\,517\,285-\frac14\right)-\overline K
 =\frac{8217}{9604}>0.
\]

Since \(\pi>3\), (1) now gives

\[
 K>a>\pi(f-\tfrac14)>\overline K>K_0(\rho).
\]

The fixed-ratio theorem proves the tail.

The numerical size of (3) is not intended to be sharp.  Its point is
that every possible unbounded high-floor obstruction is rigorously
confined to \(\rho\uparrow1\).

## 2. A quantitative finite-shell transfer from the product shelf

Define the scaled exact shell action

\[
 \mathcal A_{\varepsilon,a}(y)
 :=A_{1-\varepsilon,a/\varepsilon}(y/\varepsilon),
\]

and the product profile

\[
 B_a(y)=\frac{\sqrt{a^2-y^2}}{\pi}.
\]

The exact radius-average formula gives, for
\(0\le y\le a\rho\),

\[
 \boxed{
 \mathcal A_{\varepsilon,a}(y)
 \ge\frac12B_a(y)+\frac1{2\rho}B_{a\rho}(y).}         \tag{6}
\]

### Lemma 2.1: a quantitative truncated product margin

Let \(f\ge3\), \(h=f-1/4\), and \(a>\pi h\).  Put

\[
 y_b=\sqrt{a^2-\pi^2h^2}.
\]

For every \(0\le y_0\le s\le y_b\),

\[
 \boxed{
 2\int_{y_0}^{s}B_a(y)\,dy
 -2f(s-y_0)+\frac{a-s}{2}
 \ge\frac{f^2}{4a}.}                                 \tag{7}
\]

### Proof

As a function of \(s\), the left side of (7) is concave.  Its minimum
on \([y_0,y_b]\) is therefore at an endpoint.

At \(s=y_0\), its value is

\[
 \frac{a-y_0}{2}\ge\frac{a-y_b}{2}
 \ge\frac{\pi^2h^2}{4a}>\frac{f^2}{4a}.              \tag{8}
\]

At \(s=y_b\), it is the product first-shelf functional from Round 3.
Here is a quantitative replay, so that no unspecified strict margin is
being used.  Write

\[
 R=\frac a\pi.
\]

It remains to minimize this endpoint functional over \(y_0\).  Its
derivative is

\[
 2\bigl(f-B_a(y_0)\bigr).
\]

Hence the minimum occurs at the unique point \(B_a(y_0)=f\) when
\(R\ge f\), and at \(y_0=0\) when \(h\le R<f\).  These are precisely
the two cases treated next.

If \(R\ge f\), put

\[
 u=\sqrt{R^2-h^2},\qquad v=\sqrt{R^2-f^2}.
\]

The chord argument in that proof, followed by

\[
 u\le R-\frac{h^2}{2R},\qquad
 v\ge R-\frac{f^2}{R},
\]

gives

\[
 \frac1\pi\mathcal L_{a,f}
 >\frac{2R-3u+v}{4}
 \ge\frac{\frac32h^2-f^2}{4R}.                     \tag{9}
\]

Since \(\pi^2>9\), the last member exceeds
\(f^2/(4\pi^2R)\).  Indeed, after subtraction of
\(f^2/(36R)\), the numerator is

\[
 \frac{112f^2-216f+27}{1152},
\]

which is positive at \(f=3\) and increasing for \(f\ge3\).

If \(h\le R<f\), write \(R=h+t\), \(0\le t<1/4\).  The squared
comparison in the product proof gives

\[
 \frac1\pi\mathcal L_{a,f}
 \ge\frac{P(h,t)}{6R},                              \tag{10}
\]

where

\[
 P(h,t)
 =(h+t)^2-4(1-t)^2t(2h+t)
 \ge h^2-2h-\frac14.
\]

Indeed, the chord estimate is
\(\mathcal L_{a,f}/\pi>
[R-2(1-t)\sqrt{R^2-h^2}]/2\).  The difference of squares of
the two terms in brackets is \(P(h,t)>0\); rationalizing gives
the stronger lower bound \(P(h,t)/(4R)\).

The last inequality follows simply from \(t\le1/4\): the subtracted
term is at most \(2h+1/4\).  Moreover

\[
 18\left(h^2-2h-\frac14\right)-3f^2
 =15f^2-45f+\frac{45}{8}>0
\]

at \(f=3\), and its derivative is positive thereafter.  Thus (10) and
\(\pi^2>9\) again imply

\[
 \mathcal L_{a,f}\ge\frac{f^2}{4a}.
\]
This proves (7).

### Proposition 2.2: an explicit ultra-thin automatic sector

If

\[
 f\ge3,\qquad
 \boxed{\varepsilon a^4\le\frac{f^3}{144},}           \tag{11}
\]

then

\[
 \boxed{
 R_p+\frac d2m>0,}                                   \tag{12}
\]

and hence the scalar (2) is positive without using any terminal reserve.
More precisely,

\[
 \varepsilon\left(R_p+\frac d2m\right)
 \ge\frac{f^2}{8a}.                                  \tag{13}
\]

### Proof

Set

\[
 y_0=\varepsilon r,\qquad
 s=\varepsilon(r+p),\qquad
 y_q=\varepsilon q.
\]

Since \(A(r+p)\ge h\) and \(\mathcal A_{\varepsilon,a}\le B_a\),

\[
 0\le y_0\le s\le y_b.
\]

Also \(s\le a\rho\), and

\[
 y_q\ge a\rho-\varepsilon.
\]

Condition (11), (1), and \(f\ge3\) imply

\[
 \rho>\frac{99}{100},
 \qquad
 y_b\le a\rho.                                       \tag{14}
\]

For completeness, (11) and \(a>\pi h\), with
\(h\ge11f/12\), give \(\varepsilon<1/100\).  They also give

\[
 1-\rho^2<2\varepsilon
 \le\frac{f^3}{72a^4}
 <\frac{\pi^2h^2}{a^2},
\]

which is exactly the second assertion in (14).

To estimate the loss in (6), put

\[
 \lambda=\frac{\pi h}{a}.
\]

For \(0\le y\le y_b\), with \(t=y/a\),

\[
 \begin{aligned}
 B_a(y)-\rho^{-1}B_{a\rho}(y)
 &=
 \frac a\pi
 \frac{t^2(\rho^{-2}-1)}
 {\sqrt{1-t^2}+\sqrt{1-t^2/\rho^2}}\\
 &\le
 \frac a{\pi\lambda}t^2(\rho^{-2}-1).
 \end{aligned}
\]

Therefore

\[
 E:=
 \int_0^{y_b}
 \left(B_a-\rho^{-1}B_{a\rho}\right)\,dy
 \le\frac{a^3(\rho^{-2}-1)}{3\pi^2h}.                \tag{15}
\]

Since \(\rho>99/100\), \(h\ge11f/12\), and \(\pi^2>9\),

\[
 E<\frac{\varepsilon a^3}{11f}
 \le\frac{f^2}{1584a}.                               \tag{16}
\]

Explicitly,
\(\rho^{-2}-1<20000\varepsilon/9801\) and
\(3\pi^2h>99f/4\); the resulting coefficient
\(80000/970299\) is smaller than \(1/11\).

The exact scaled shelf identity is

\[
 \varepsilon\left(R_p+\frac d2m\right)
 =
 2\int_{y_0}^{s}\mathcal A_{\varepsilon,a}(y)\,dy
 -2f(s-y_0)+\frac d2(y_q-s).                         \tag{17}
\]

The terminal-coordinate difference from the product expression obeys

\[
 d(y_q-s)-(a-s)
 \ge-(1-d)a-\varepsilon(a+1).                        \tag{18}
\]

If \(\theta=\arccos\rho\), then

\[
 \varepsilon=2\sin^2(\theta/2)
 \ge\frac{2\theta^2}{\pi^2},
\]

and hence

\[
 1-d=\frac{2\theta}{\pi}\le\sqrt{2\varepsilon}.      \tag{19}
\]

Condition (11) now gives

\[
 \frac{(1-d)a}{2}\le\frac{f^2}{24a},
 \qquad
 \frac{\varepsilon(a+1)}2\le\frac{f^2}{24a}.         \tag{20}
\]

For the first inequality use
\(\sqrt\varepsilon a^2\le f^{3/2}/12\) and \(f\ge2\).
For the second, multiply (11) by \((a+1)/(2a^4)\) and use
\(a>\pi h>f>1\), which implies
\(f(a+1)<2a^2<12a^3\).

Combining (6)--(7) and (15)--(20) gives

\[
 \varepsilon\left(R_p+\frac d2m\right)
 \ge
 \frac{f^2}{4a}
 -\frac{f^2}{1584a}
 -\frac{f^2}{12a}
 >\frac{f^2}{8a}.
\]

This proves (12)--(13).  All inequalities remain favorable at ordinary
and strict shelf walls.

## 3. The critical unbounded thin scaling

The sector (11) does not contain the potentially critical ray

\[
 \rho=1-\varepsilon,\qquad
 K\sim\kappa\varepsilon^{-3/2},\qquad
 n\sim N\varepsilon^{-1/2}.                          \tag{21}
\]

Here

\[
 a\sim\kappa\varepsilon^{-1/2}\longrightarrow\infty.
\]

Nevertheless, the exact-angle terminal reserve strictly beats the
leading shelf/head loss on this ray.

Put

\[
 c_0=\frac{2\sqrt2}{3\pi},
 \qquad
 X=(\mu-z)\sqrt\varepsilon.
\]

The turning expansion of the two ball actions gives the local limit

\[
 \boxed{
 H_\kappa(X)
 =\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right).}             \tag{22}
\]

Its interface height is

\[
 w=H_\kappa(0)=c_0\kappa.                            \tag{23}
\]

Let

\[
 B=\left[w+\frac14\right]_<.
\]

For the ball level \(\tau_k=k-1/4\), the exact angle
\(\theta_k\) in the terminal reserve satisfies

\[
 \sqrt\varepsilon\,\frac{\pi}{2\theta_k}
 \longrightarrow
 \frac{\pi}{2\sqrt2}
 w^{1/3}\tau_k^{-1/3}.                               \tag{24}
\]

The finite \(Q\)-term and the one-interface cap vanish after
multiplication by \(\sqrt\varepsilon\).  Thus the exact-angle theorem
gives the following safe limiting lower reserve:

\[
 \boxed{
 \liminf_{\varepsilon\downarrow0}\sqrt\varepsilon\,D_A(q)
 \ge \mathcal T(w):=
 \frac{\pi}{2\sqrt2}
 w^{1/3}
 \sum_{k=1}^{B}(k-\tfrac14)^{-1/3}.}                 \tag{25}
\]

At a strict action wall the finite sequence can acquire the next level
from one side; this only increases the right side of (25), so the
strict-wall value of \(B\) is the wall-safe choice.

The fractional-top refinement from Round 4c also survives at this
scale.  Away from a level wall it adds

\[
 \frac{\pi}{\sqrt2}(w-B)_+^2                         \tag{25a}
\]

to the right side of (25).  At a wall, the safe statement is the lower
of the two one-sided expressions, because the fractional top is
exchanged for the newly active complete level.  We do not need (25a)
below: the complete-level part (25) already pays every possible negative
leading prefix.  Thus the refinement strengthens the critical result
but does not, by itself, furnish the missing uniform finite-
\(\varepsilon\) estimate in Section 4.

We now compare (25) with the worst shelf/head loss.

### Theorem 3.1: no negative leading obstruction on the critical ray

For every fixed limiting first-floor level \(f\ge2\), every limiting
no-drop or first-drop configuration in (21) has a nonnegative leading
scalar after the exact-angle terminal reserve is included.  Whenever
the shelf/head prefix is negative, the terminal reserve exceeds its
magnitude strictly.

### Proof

Write \(X=\kappa u\) and introduce

\[
 t=\sqrt{1+u}-\sqrt u\in(0,1].
\]

Direct algebra gives the exact formulas

\[
 \frac{H_\kappa(X)}w
 =F(t):=\frac{3/t+t^3}{4},
\qquad
 u=\frac{(1-t^2)^2}{4t^2},
\qquad
 H_\kappa'(X)=\frac{3c_0}{2}t.                       \tag{26}
\]

Suppose first that the shelf drops before the interface.  Let \(M\)
be its lower-wall point,

\[
 H_\kappa(M)=h=f-\frac14,
\]

and let \(N\ge M\) be the point at which \(H_\kappa(N)=f\).  Any
start beyond \(N\) only adds positive shelf area, so the worst scaled
prefix is

\[
 \mathcal L
 =
 -2\int_M^N(f-H_\kappa(X))\,dX+\frac M2.             \tag{27}
\]

On \([M,N]\),

\[
 0\le f-H_\kappa\le\frac14.
\]

If \(\mathcal L<0\), then \(N>2M\).  In the \(u\)-coordinate this says

\[
 u_f>2u_h.                                           \tag{28}
\]

We claim that (28) forces

\[
 w>\frac34,\qquad t_f>\frac14.                       \tag{29}
\]

Here \(t_h,t_f\) are the parameters in (26) at levels \(h,f\).
The proof is elementary but important.  Since

\[
 \frac hf\ge\frac78,\qquad \frac fh\le\frac87,
\]

the formula for \(F\) controls the ratio \(t_h/t_f\).

If \(w\le3/4\), then \(F(t_f)=f/w\ge8/3\), so
\(t_f<3/10\).  The bounds

\[
 \frac3{4t}\le F(t)\le\frac1t
\]

first give \(t_h<1/2\), and then the exact formula for \(F\) gives

\[
 \frac{t_h}{t_f}
 =\frac fh\frac{3+t_h^4}{3+t_f^4}
 \le\frac76.
\]

Consequently

\[
 \frac{u_f}{u_h}
 \le
 \left(\frac76\right)^2
 \left(\frac{400}{351}\right)^2
 =\frac{1960000}{1108809}<2,
\]

contrary to (28).  Hence \(w>3/4\).

Likewise, if \(t_f\le1/4\), the same two-step estimate gives

\[
 t_h<\frac25,\qquad \frac{t_h}{t_f}<\frac65,
\]

and therefore

\[
 \frac{u_f}{u_h}
 <
 \left(\frac65\right)^2
 \left(\frac{100}{91}\right)^2
 =\frac{14400}{8281}<2,
\]

again contradicting (28).  This proves (29).

Since \(H_\kappa'\) decreases along \([M,N]\), (26) and (29) give

\[
 N-M
 <\frac{1/4}{(3c_0/2)(1/4)}
 =\frac{2}{3c_0}.
\]

Equation (27) consequently gives

\[
 -\mathcal L
 <\frac{N-M}{2}
 <\frac1{3c_0}
 =\frac{\pi}{2\sqrt2}.                               \tag{30}
\]

On the other hand, \(w>3/4\) implies \(B\ge1\), and (25) gives

\[
 \mathcal T(w)
 \ge
 \frac{\pi}{2\sqrt2}
 w^{1/3}(3/4)^{-1/3}
 >\frac{\pi}{2\sqrt2}.                               \tag{31}
\]

Thus the terminal reserve strictly exceeds the head loss.

In the no-drop branch, \(M=0\) and \(h\le w\).  If \(w\ge f\), the
shelf prefix is already nonnegative.  If \(h\le w<f\), then

\[
 F(t_f)=\frac fw\le\frac fh\le\frac87,
\]

which directly gives \(t_f>1/4\).  The same estimates
(30)--(31) apply.  This proves the theorem.

The equality of the comparison constants

\[
 \frac1{3c_0}=\frac{\pi}{2\sqrt2}
\]

is the sharp feature of this scaling calculation.  The inequalities
are strict because a negative prefix forces \(w>3/4\) and \(t_f>1/4\).

### Corollary 3.2: a uniform no-drop gap for \(f=2,3\)

Suppose a no-drop sequence has the critical scaling (21), with limiting
first floor \(f\in\{2,3\}\).  Then

\[
 \boxed{
 \liminf_{\varepsilon\downarrow0}
 \sqrt\varepsilon\,\mathscr S
 \ge\gamma_0:=
 \frac{\pi}{2\sqrt2}
 \left[\left(\frac73\right)^{1/3}-1\right]
 >\frac13.}                                         \tag{31a}
\]

Indeed, no-drop gives \(w\ge h=f-1/4\ge7/4\).  If its shelf prefix is
negative, (30) bounds its magnitude by
\(\pi/(2\sqrt2)\), whereas the first complete terminal level alone gives

\[
 \mathcal T(w)\ge
 \frac{\pi}{2\sqrt2}
 \left(\frac{w}{3/4}\right)^{1/3}
 \ge
 \frac{\pi}{2\sqrt2}\left(\frac73\right)^{1/3}.
\]

If the prefix is nonnegative, the bound is stronger.  Finally,
\(\pi/(2\sqrt2)>15/14\) and
\((7/3)^{1/3}>59/45\), so \(\gamma_0>1/3\).

The global exhaustion theorem in
[`general-d-round-04-no-drop-exhaustion.md`](general-d-round-04-no-drop-exhaustion.md)
proves that any escaping no-drop counterexample sequence is already
reduced to \(f=2\) or \(3\), \(K\asymp n^3\), and
\(K-\mu\asymp n\).  Such a sequence is impossible: after taking a
convergent scaled subsequence, (31a) contradicts \(\mathscr S<0\).
This makes the residual no-drop problem finite in \(n\) at the
qualitative level.  The present argument does not give an explicit
numerical \(n\)-cutoff; that would require uniform, fully quantified
remainders in the turning expansions (22) and (24).

## 4. Exact remaining wedge

Combine the new results with the already proved thin high-energy theorem.
For

\[
 f\ge2\,358\,517\,285,
\]

every still-unresolved high-floor tail must lie in the explicit wedge

\[
 \boxed{
 \begin{gathered}
 0<\varepsilon<\frac1{100},\qquad
 a>\pi(f-\tfrac14),\\
 \varepsilon a<\frac{125}{8},\qquad
 \varepsilon a^4>\frac{f^3}{144}.
 \end{gathered}}                                     \tag{32}
\]

Indeed:

- Proposition 1.1 removes \(\varepsilon\ge1/100\);
- the thin high-energy theorem removes
  \(\varepsilon a=K\varepsilon^2\ge125/8\);
- Proposition 2.2 removes
  \(\varepsilon a^4\le f^3/144\).

The critical ray (21) lies inside (32):

\[
 \varepsilon a\longrightarrow0,\qquad
 \varepsilon a^4\longrightarrow\infty.
\]

Theorem 3.1 proves that this ray has no negative leading-order
obstruction.  What remains missing is a uniform finite-\(\varepsilon\)
error estimate that transfers its strict limiting comparison throughout
the unbounded wedge (32).

Accordingly, this round does **not** prove a global floor cutoff
\(F_0\ge f_*\).  It proves:

1. a finite explicit cutoff on every ratio range
   \(\rho\le99/100\);
2. the explicit finite-shell sector (11);
3. nonnegativity on the unbounded critical thin ray, with strict
   overpayment of every negative leading prefix and matching constants.

The obstruction is now quantitative rather than heuristic: a global
cutoff requires controlling the next finite-\(\varepsilon\) term in
(22)--(25), uniformly as both \(a\) and the first floor vary.
