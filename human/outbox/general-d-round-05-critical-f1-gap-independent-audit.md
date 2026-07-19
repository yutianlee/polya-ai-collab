# Independent audit: Round 5 critical `(f=1)` gap

Date: 18 July 2026

## Verdict

**PASS after one non-mathematical wall-convention clarification.**

The theorem, the prefix coefficient and sign, the concavity/trapezoid
direction, the `(t)`-coordinate identities, all three rational splits, and
the stated uniform constant are correct.  The original text blurred the
exact strict-bracket value at `(w=3/4)` with the smaller one-sided value
needed for a limiting transfer.  I patched those two paragraphs to say
precisely:

* at exact equality, `[w+1/4]_<=[1]_< =0`, so the zero-level triangle is
  the exact strict-wall expression and has normalized value `9/16`;
* a sequence whose terminal top action approaches the same limiting wall
  from above has `B=1`, and its first complete-level limit has normalized
  value `1/2`;
* the transfer-safe lower envelope is therefore `1/2`.

No displayed estimate or claimed constant changed.

Audited source before the clarification:

`SHA256 021B29E46FD0E7762E383B7C46EEAD596C92A43EA8CAA70C1BBD401148C8D560`

Audited source after the clarification:

`SHA256 3CEB21D4C518935448606FAF59371C5DD7E683A31ECDAA8ACDFB3152D9337FA7`

The post-patch source has no non-whitespace ASCII control characters.

## 1. Critical profile and prefix

With

\[
 c_0=\frac{2\sqrt2}{3\pi},\qquad
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \bigl((\kappa+X)^{3/2}-X^{3/2}\bigr),
\]

direct substitution gives `H_kappa(0)=c_0 kappa=w`.  For `0<w<3/4`,
strict monotonicity of `H_kappa` gives unique levels

\[
 H_\kappa(M)=\frac34,\qquad H_\kappa(N)=1,qquad 0<M<N.
\]

The coefficient and orientation in the limiting prefix are correct.  If
`s=sqrt(epsilon)` and `X=s(mu-z)`, the negative shelf band is traversed
from `X=N` to `X=M`.  Consequently its worst scaled contribution is

\[
 sR_p\longrightarrow
 -2\int_M^N(1-H_\kappa(X))\,dX.
\]

Moreover `s m -> M` and `d_rho -> 1`, so the head term tends to `M/2`.
This reproduces

\[
 \mathcal L=-2\int_M^N(1-H_\kappa(X))\,dX+\frac M2.
\]

The zero-level coefficient is also correct.  The exact tangent-triangle
bound is `D_A(q)>=v^2/c`, while

\[
 c=\frac{\arccos\rho}{\pi}
   \sim\frac{\sqrt2}{\pi}s,qquad v\longrightarrow w.
\]

Thus `sD_A(q)` has lower limit

\[
 \frac\pi{\sqrt2}w^2=\mathcal Z(w).
\]

As a separate numerical check of the prefix, put

\[
 J(u)=(1+u)^{5/2}-u^{5/2},\qquad
 u_a=u(a),\quad u_b=u(b),\quad \kappa=\frac w{c_0}.
\]

Exact integration gives

\[
 \int_M^N(1-H_\kappa(X))\,dX
 =\kappa\left[u_b-u_a-
 \frac{2w}{5}\bigl(J(u_b)-J(u_a)\bigr)\right].
\]

At four independent test values, including a point within `10^-12` of
the upper wall, this antiderivative agreed with 100-decimal direct
quadrature to at least 99 decimal places.

## 2. Concavity and the chord direction

Twice differentiating gives

\[
 H_\kappa''(X)=\frac{3c_0}{4\sqrt\kappa}
 \left((\kappa+X)^{-1/2}-X^{-1/2}\right)<0.
\]

Therefore `g=1-H_kappa` is convex.  A convex graph lies **below** its
endpoint chord, so with `g(M)=1/4` and `g(N)=0`,

\[
 \int_M^N g\leq\frac{N-M}{8}.
\]

The note's conclusion follows with the correct direction:

\[
 \mathcal L\geq-\frac{N-M}{4}+\frac M2
 =\frac{3M-N}{4}.
\]

At the limiting wall `M=0`; `g` is continuous at zero and convex on
`(0,N]`, so the same chord inequality follows by taking `M downarrow 0`.

## 3. Exact `(t)` coordinates

For

\[
 t=\sqrt{1+u}-\sqrt u,
\]

one has

\[
 \sqrt{1+u}=\frac{t+t^{-1}}2,\qquad
 \sqrt u=\frac{t^{-1}-t}2,
\]

and hence

\[
 u(t)=\frac{(1-t^2)^2}{4t^2},\qquad
 \frac{H_\kappa(\kappa u(t))}{w}
 =F(t)=\frac{3/t+t^3}{4}.
\]

The function `F` is strictly decreasing on `(0,1)`, and

\[
 u'(t)=\frac{t-t^{-3}}2\leq0.
\]

At `M` and `N`, respectively, the level equations are therefore exactly

\[
 w=\frac{3a}{3+a^4},\qquad
 w=\frac{4b}{3+b^4},\qquad 0<b<a\leq1.
\]

They rearrange to

\[
 a=w\left(1+\frac{a^4}{3}\right),\qquad
 b=\frac{3w}{4}+\frac{wb^4}{4}\geq\frac{3w}{4}.
\]

Since `1/c_0=(3/2)(pi/sqrt(2))`, substitution into the prefix bound gives

\[
 \mathcal L+\mathcal Z(w)
 \geq\frac\pi{\sqrt2}
 \left[w^2+\frac{3w}{8}\bigl(3u(a)-u(b)\bigr)\right].
\]

This confirms every factor in equations (12)--(13).

If `d=3/4`, `a<=cw<=1`, and `b>=dw`, monotonicity of `u` gives
`u(a)>=u(cw)` and `u(b)<=u(dw)`.  Expanding `u` independently yields

\[
 E_c(w)=\frac{3A_c}{32w}+w^2-\frac{3w}{8}
       +\frac{3B_cw^3}{32},
\]

where

\[
 A_c=\frac3{c^2}-\frac1{d^2},\qquad
 B_c=3c^2-d^2.
\]

Thus the direction and all coefficients in equations (15)--(16) are
correct.

## 4. Exact replay of the three rational splits

### Split 1: `0<w<=1/2`

The quoted value

\[
 F(2/3)=\frac{259}{216}<\frac32
\]

forces `a<2/3`.  Hence

\[
 c_1=1+\frac{(2/3)^4}{3}=\frac{259}{243},
\]

and exact rational recomputation gives

\[
 A_{c_1}=\frac{521027}{603729},\qquad
 B_{c_1}=\frac{896149}{314928}>0.
\]

Using `1/w>=2` and
`w^2-3w/8=(w-3/16)^2-9/256` gives exactly

\[
 \frac{3A_{c_1}}{16}-\frac9{256}-\frac18
 =\frac{85469}{51518208}>0.
\]

### Split 2: `1/2<=w<=2/3`

Here

\[
 F(3/4)=\frac{283}{256}<\frac98
\]

forces `a<3/4`, and

\[
 c_2=\frac{283}{256},\qquad
 A_{c_2}=\frac{488048}{720801},\qquad
 B_{c_2}=\frac{203403}{65536}>0.
\]

On this interval, `1/w>=3/2` and
`w^2-3w/8>=1/16`.  Exact recomputation gives

\[
 \frac{9A_{c_2}}{64}+\frac1{16}-\frac18
 =\frac{41923}{1281424}>0.
\]

### Split 3: `2/3<=w<3/4`

The bound `b>=3w/4>=1/2` implies
`u(b)<=u(1/2)=9/16`, while `u(a)>=0`.  Therefore

\[
 E\geq w^2-\frac{27w}{128}
 \geq\frac49-\frac{81}{512}
 =\frac18+\frac{743}{4608}.
\]

The second inequality is deliberately weak but valid: use `w^2>=4/9`
and `w<3/4` separately.  The three margins are, in increasing order of
size at the minimum,

\[
 \frac{85469}{51518208},\qquad
 \frac{41923}{1281424},\qquad
 \frac{743}{4608}.
\]

Thus the global normalized lower bound is exactly

\[
 \frac18+\frac{85469}{51518208}
 =\frac{6525245}{51518208}
 =0.1266590056859120566\ldots>\frac18.
\]

## 5. Strict wall and one-sided transfer

At the exact strict wall `w=3/4`,

\[
 B=[w+1/4]_<=[1]_< =0,
\]

so the exact zero-level bound has normalized value `(3/4)^2=9/16`.
For terminal top actions just above the wall, `B=1`; the critical first
complete-level expression tends to

\[
 \frac\pi{2\sqrt2}
 \left(\frac{w}{3/4}\right)^{1/3}
 \longrightarrow\frac\pi{2\sqrt2},
\]

which has normalized value `1/2`.  Taking the smaller one-sided value
therefore loses `1/16` relative to the exact/below-wall zero-level value.
Subtracting this from the split-3 lower bound gives exactly

\[
 \frac49-\frac{81}{512}-\frac1{16}-\frac18
 =\frac{455}{4608}>0.
\]

This validates equation (20) and the transfer-safe wall conclusion.  It
also explains why calling the `1/2` value the *exact strict-wall bracket*
would have been inaccurate; it is instead the smaller one-sided envelope.

## 6. Independent numerical stress test

The numerical work is diagnostic only; the proof above is exact.

I solved the two monotone quartics for `a` and `b`, evaluated the exact
antiderivative from Section 1, and performed:

1. a 100,000-point scan over `0<w<3/4`;
2. an independent 4,095-point scan at 70 decimal digits; and
3. a 90-decimal golden-section refinement around the observed minimum.

The refined minimum was

\[
\begin{aligned}
 w_*&=0.4517686361045427125299360511707947\ldots,\\
 a_*&=0.4584189975650045467676216057529593\ldots,\\
 b_*&=0.3403418428378700850418967328477978\ldots,
\end{aligned}
\]

with

\[
 \mathcal L=0.22045191593126169048\ldots,
 \qquad
 \mathcal Z=0.45338487574881176625\ldots,
\]

and hence

\[
 \mathcal L+\mathcal Z
 =0.67383679168007345674\ldots,
\]

or, after normalization by `pi/sqrt(2)`,

\[
 0.30333312898826351752\ldots.
\]

For comparison, the note proves only

\[
 \frac\pi{\sqrt2}
 \left(\frac18+\frac{85469}{51518208}\right)
 =0.28136556766302108724\ldots.
\]

The 70-decimal whole-interval grid found normalized minimum
`0.30333313439249803465...` at its nearest grid point, consistent with
the refinement.  No numerical sample approached the analytic bound, and
no sign or wall discontinuity contrary to the proof was observed.

## 7. Scope check

The note correctly labels this as a critical-limit theorem.  It does not
claim the missing finite-thickness transfer, compactness of every residual
`s=n-p-1>=2` ray, or a finite chamber certificate.  The proved result is
exactly the uniform analytic payment on the critical `(f=1)` profile, and
that result passes the audit.
