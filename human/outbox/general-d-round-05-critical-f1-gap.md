# General dimension, Round 5: the missing critical (f=1) gap

Date: 18 July 2026

Status: rigorous critical-limit theorem.  It closes the analytic comparison
between the first-drop prefix and the zero-level/fractional terminal reserve
on the ordinary first floor.  No numerical premise or interval computation
is used.

This is a limiting theorem.  It does not by itself prove that every
unbounded exact first-floor chamber enters this scaling, and it does not
enumerate any of the remaining finite chambers.

## 1. Statement

Put

\[
 c_0=\frac{2\sqrt2}{3\pi},\qquad
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right),\qquad
 w=H_\kappa(0)=c_0\kappa.
 \tag{1}
\]

On the ordinary first floor, (f=1) and (h=3/4).  In the first-drop
branch one has (0<w<3/4).  Let

\[
 H_\kappa(M)=\frac34,\qquad H_\kappa(N)=1,
 \qquad 0<M<N,
 \tag{2}
\]

and let the worst limiting first-drop prefix be

\[
 \mathcal L
 =-2\int_M^N(1-H_\kappa(X))\,dX+\frac M2.
 \tag{3}
\]

Because the complete terminal level is absent when (w<3/4), the
zero-level triangle (equivalently, the fractional-top reserve with
(B=0)) has the critical limit

\[
 \mathcal Z(w)=\frac\pi{\sqrt2}w^2.
 \tag{4}
\]

The result is the uniform estimate

\[
 \boxed{
 \mathcal L+\mathcal Z(w)>
 \frac\pi{8\sqrt2}
 \qquad(0<w<3/4).}
 \tag{5}
\]

In fact the proof gives a slightly larger explicit constant:

\[
 \mathcal L+\mathcal Z(w)
 \geq \frac\pi{\sqrt2}
 \left(\frac18+\frac{85469}{51518208}\right).
 \tag{6}
\]

The limiting action wall (w=3/4) is also harmless.  At exact equality the
strict bracket is (B=[1]_< =0), so the zero-level expression is the exact
strict-bracket branch value.  A transfer statement must also allow the terminal top action
to approach the wall from above; on that side (B=1), and the smaller
one-sided limiting bound is the first complete-level value
(\pi/(2\sqrt2)).  Section 5 uses this lower semicontinuous wall-safe
envelope and still gives a gap larger than (\pi/(8\sqrt2)).

## 2. A convex-chord lower bound for the prefix

Differentiating (1) gives

\[
 H_\kappa''(X)=\frac{3c_0}{4\sqrt\kappa}
 \left(\frac1{\sqrt{\kappa+X}}-\frac1{\sqrt X}\right)<0.
 \tag{7}
\]

Thus (g(X)=1-H_\kappa(X)) is convex on ([M,N]), with

\[
 g(M)=\frac14,\qquad g(N)=0.
\]

A convex function lies below its endpoint chord, so

\[
 \int_M^N(1-H_\kappa(X))\,dX
 \leq\frac{N-M}{8}.
\]

Consequently

\[
 \boxed{\mathcal L\geq\frac{3M-N}{4}.}
 \tag{8}
\]

This elementary chord estimate is the main simplification special to the
(f=1) problem.

## 3. Exact (t)-coordinates

Write

\[
 X=\kappa u(t),\qquad
 t=\sqrt{1+u}-\sqrt u\in(0,1],
\]

so that

\[
 \frac{H_\kappa(X)}w=F(t):=\frac{3/t+t^3}{4},
 \qquad
 u(t)=\frac{(1-t^2)^2}{4t^2}
 =\frac{t^{-2}-2+t^2}{4}.
 \tag{9}
\]

Let (a) and (b) be the (t)-coordinates at (M) and (N),
respectively.  Then (0<b<a\leq1), and the two level equations are

\[
 w=\frac{3a}{3+a^4}=\frac{4b}{3+b^4}.
 \tag{10}
\]

In particular,

\[
 a=w\left(1+\frac{a^4}{3}\right),
 \qquad b=\frac{3w}{4}+\frac{wb^4}{4}\geq\frac{3w}{4}.
 \tag{11}
\]

Moreover

\[
 M=\frac w{c_0}u(a),\qquad
 N=\frac w{c_0}u(b),\qquad
 \frac1{c_0}=\frac32\frac\pi{\sqrt2}.
\]

Combining these identities with (4) and (8) gives

\[
 \mathcal L+\mathcal Z(w)
 \geq\frac\pi{\sqrt2}E(w,a,b),
 \tag{12}
\]

where

\[
 E(w,a,b)
 :=w^2+\frac{3w}{8}\bigl(3u(a)-u(b)\bigr).
 \tag{13}
\]

It remains only to prove (E>1/8).

The function (u) is decreasing on ((0,1]), since

\[
 u'(t)=\frac{t-t^{-3}}2\leq0.
 \tag{14}
\]

Fix (d=3/4).  Whenever (a\leq cw\leq1), equations
(11) and (14) imply

\[
 u(a)\geq u(cw),\qquad u(b)\leq u(dw).
\]

Hence

\[
 E(w,a,b)\geq E_c(w)
 :=\frac{3A_c}{32w}+w^2-\frac{3w}{8}
   +\frac{3B_cw^3}{32},
 \tag{15}
\]

where

\[
 A_c=\frac3{c^2}-\frac1{d^2},
 \qquad B_c=3c^2-d^2.
 \tag{16}
\]

Both choices of (c) below have (A_c>0) and (B_c>0).

## 4. The ranges (0<w\leq2/3)

### 4.1. The range (0<w\leq1/2)

Here

\[
 F(a)=\frac{3}{4w}\geq\frac32,
 \qquad F\left(\frac23\right)=\frac{259}{216}<\frac32.
\]

Since (F) is decreasing, (a<2/3).  Equation (11) therefore gives

\[
 a\leq c_1w,
 \qquad c_1=1+\frac{(2/3)^4}{3}=\frac{259}{243},
 \qquad c_1w<1.
\]

For this value,

\[
 A_{c_1}=\frac{521027}{603729}.
\]

Discarding the positive (B_{c_1})-term in (15), using (1/w\geq2),
and completing the square gives

\[
\begin{aligned}
 E(w,a,b)
 &\geq \frac{3A_{c_1}}{16}
       +\left(w^2-\frac{3w}{8}\right)\\
 &\geq \frac{3A_{c_1}}{16}-\frac9{256}\\
 &=\frac18+\frac{85469}{51518208}.
\end{aligned}
 \tag{17}
\]

### 4.2. The range (1/2\leq w\leq2/3)

Now

\[
 F(a)=\frac{3}{4w}\geq\frac98,
 \qquad F\left(\frac34\right)=\frac{283}{256}<\frac98,
\]

so (a<3/4).  Thus

\[
 a\leq c_2w,
 \qquad c_2=1+\frac{(3/4)^4}{3}=\frac{283}{256},
 \qquad c_2w<1,
\]

and

\[
 A_{c_2}=\frac{488048}{720801}.
\]

On this interval, (1/w\geq3/2), while
(w^2-3w/8\geq1/16).  Formula (15) yields

\[
\begin{aligned}
 E(w,a,b)
 &\geq\frac{9A_{c_2}}{64}+\frac1{16}\\
 &=\frac18+\frac{41923}{1281424}.
\end{aligned}
 \tag{18}
\]

## 5. The range (2/3\leq w<3/4) and the level wall

From (11), (b\geq3w/4\geq1/2).  Thus

\[
 u(a)\geq0,
 \qquad u(b)\leq u(1/2)=\frac9{16}.
\]

Equations (13) and (w<3/4) give

\[
\begin{aligned}
 E(w,a,b)
 &\geq w^2-\frac{3w}{8}\frac9{16}\\
 &\geq\frac49-\frac{81}{512}
 =\frac18+\frac{743}{4608}.
\end{aligned}
 \tag{19}
\]

The smallest of the three explicit margins in (17)--(19) is the one in
(17).  Substitution in (12) proves (5)--(6).

At exact equality (w=3/4), the strict bracket is (B=0), and the zero-level
bound has normalized value (9/16).  If the terminal top action approaches
the same limiting wall from above, then (B=1) and the limiting first
complete-level bound has normalized value (1/2).  Thus the smaller
one-sided, transfer-safe terminal lower bound is

\[
 \mathcal Z_{\rm wall}=\frac\pi{2\sqrt2}
 =\frac\pi{\sqrt2}\frac12.
\]

Relative to (4), this lowers the normalized terminal by
(9/16-1/2=1/16).  The right side of (19) therefore remains at least

\[
 \frac49-\frac{81}{512}-\frac1{16}
 =\frac18+\frac{455}{4608}>\frac18.
 \tag{20}
\]

Thus the same claimed gap is valid at the wall in the wall-safe sense.

## 6. Exact scope of the result

The theorem removes the analytic obstruction that was left when the
(f\geq2) uniform critical-gap argument forced a complete terminal level.
For (f=1), that complete level is absent, but the zero-level/fractional
triangle pays the prefix with the same convenient uniform gap
(\pi/(8\sqrt2)).

Consequently, any exact first-floor first-drop sequence for which

1. the rescaled shell action converges to (1),
2. the rescaled shelf/head term has lower limit (3), and
3. the zero-level or wall-safe terminal estimate converges as above,

cannot remain negative.

What is **not** proved here is equally important.  The estimate does not
show that every unbounded part of the residual cone
(s=n-p-1\geq2) has this critical scaling; it supplies no uniform
finite-thickness error estimate outside a compact critical parameter set;
and it does not close the finite (s=0,1, x<100) chambers or the
small-start cases (r=1/2,1).  Those are separate exhaustion and transfer
tasks.  In particular, this note is not an exact finite-(s) chamber
certificate.
