# Independent audit of Round 23 exact-cap curvature reduction

Date: 19 July 2026  
Verdict: **PASS**

Audited source:

- human/outbox/general-d-round-23-exact-cap-curvature-reduction-and-failure-report.md
- SHA-256 2534941b573a60f17ef79dc7fc28ca6627ca0358376c0625b459c2b0df1446aa

The verdict covers the rigorous reduction through (4.6), including its
strict-wall conventions. It does not promote the open sign
\(\mathcal C_8\geq0\), CST-H, or the general theorem. The reported search
is theorem-design evidence only.

## 1. Exact domain and wall ownership

Write \(R=\mu/\cos t\). Direct differentiation of

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi}
\]

gives

\[
 \partial_R G_R(z)=\frac1\pi\sqrt{1-z^2/R^2}>0,\qquad
 \partial_zG_R(z)=-\frac1\pi\arccos(z/R).
\]

Thus \(A_t(z)=G_R(z)-G_\mu(z)\) is strictly increasing in \(t\) and
strictly decreasing in \(z\) on \(0<z\leq\mu\). Also

\[
 W=A_t(\mu)=\frac{\mu}{\pi}(\tan t-t),\quad
 W'=\frac{\mu}{\pi}\tan^2t>0.
\]

Let \(x=r+p\) and \(h=f-1/4\). Since \(A_t\) decreases spatially, the
ordinary-floor statement that \(r,\ldots,x\) have floor \(f\), while
\(x+1\) is the first lower sample, is exactly

\[
 h\leq A_t(x),\qquad A_t(r)<h+1,\qquad A_t(x+1)<h.
\]

The weak first inequality owns the ordinary lower shelf wall. Equality
in either strict upper inequality belongs to the adjacent branch. Since
\(x+1\leq q\leq\mu\),

\[
 W=A_t(\mu)\leq A_t(x+1)<h,
\]

so \(\lambda=h-W>0\) follows without an extra assumption.

For fixed discrete data and \(\alpha\), each shelf inequality is a lower
or upper interval in \(t\). The activity function

\[
 \frac{\mu^2}{\cos^2t}
 -\frac{\pi^2}{(1-\cos t)^2}-\gamma
\]

is strictly increasing: both the derivative of the first term and that
of the negative reciprocal term are positive. Its strict positivity is
therefore another lower interval. Their intersection is one interval,
with the claimed shelf and activity endpoints. No disconnected feasible
component is omitted.

## 2. The exact \(J<1/8\) proof

Here \(p,m\geq1\), hence \(q=r+p+m\geq3\) on the integer owner and
\(q\geq7/2\) on the half-integer owner. Radius monotonicity and
\(\mu<q+1\) give

\[
 J=2I_\mu(q)<2I_{q+1}(q).
\]

In the double-integral representation, for \(0\leq u<v\leq1\),

\[
 \frac{d}{dq}\frac{q+u}{q+v}
 =\frac{v-u}{(q+v)^2}>0.
\]

The square-root integrand therefore decreases pointwise with \(q\), so
the endpoint is \(2I_4(3)\). Substitution in the closed cap formula gives

\[
 2I_4(3)=
 \frac{34\arccos(3/4)-9\sqrt7}{2\pi}.
\]

Every printed rational step checks as follows. With
\(u=1/\sqrt7\),

\[
 \arccos(3/4)=2\arctan u,\qquad
 \arctan u<u-\frac{u^3}{3}+\frac{u^5}{5},
\]

and exact simplification gives

\[
 68\left(u-\frac{u^3}{3}+\frac{u^5}{5}\right)-9\sqrt7
 =\frac{1499}{735\sqrt7}.
\]

Moreover

\[
 7-\left(\frac{37}{14}\right)^2=\frac3{196}>0,
\]

so the first comparison below follows by replacing \(1/\sqrt7\) with
\(14/37\):

\[
 \frac{1499}{735\sqrt7}
 <\frac{1499\cdot14}{735\cdot37}
 =\frac{20986}{27195}.
\]

The next cross-difference is

\[
 333\cdot27195-20986\cdot424=157871>0,
\]

and \(333/424<\pi/4\) is exactly the standard lower bound
\(333/106<\pi\). Hence the cap numerator is \(<\pi/4\), and division by
\(2\pi\) proves \(J<1/8\). All inequalities are strict, including
\(\alpha=0\), where \(J=0\).

## 3. Retained-cap comparison

The curvature member is

\[
 L_{\rm curv}
 =\frac{1-\cos t}{2\pi\mu}\,p(2r+p).
\]

Using \(a_p=p^2/[3(2r+p)]\) gives the exact identity

\[
 (p+a_p)L_{\rm curv}
 =\frac{p^2(3r+2p)(1-\cos t)}{3\pi\mu}.
\]

Also \(d/(2c)=\pi/(2t)-1\). Consequently the whole comparison reduces
to

\[
 \mathcal R_J-\mathcal C_8
 =(p+a_p)(L_0-L_{\rm curv})+\left(\frac18-J\right)>0.
\]

The first summand is nonnegative and the second is strictly positive.
This verifies Proposition 3.1 with no unlisted sign change. In
particular, \(\mathcal C_8\geq0\) is only a sufficient condition; it is
not asserted here.

## 4. Convex cells and all payment branches

Put \(a=3/4-1/\sqrt2\). On the admissible side \(\lambda>0\),

\[
 \mathcal E(\lambda)=
 \begin{cases}
 1,&0<\lambda\leq a,\\
 2(3/4-\lambda)^2,&a\leq\lambda\leq3/4,\\
 0,&\lambda\geq3/4.
 \end{cases}
\]

The overlapping endpoint formulas agree. On the quadratic branch,
\(3/4-\lambda=W-(f-1)>0\), so

\[
 \mathcal E'=4(W-(f-1))W',
\]

\[
 \mathcal E''=
 4\{(W')^2+(W-(f-1))W''\}>0,\qquad
 W''=\frac{2\mu}{\pi}\tan t\sec^2t>0.
\]

Differentiating the rest of \(\mathcal C_8\) gives exactly

\[
 \mathcal C_8'
 =C_0\sin t-\frac m\pi-\frac{B_0\pi}{2t^2}+\mathcal E',
\]

\[
 \mathcal C_8''
 =C_0\cos t+\frac{B_0\pi}{t^3}+\mathcal E''>0.
\]

Strict positivity remains true on a constant-payment cell even when
\(B_0=0\), because \(C_0\cos t>0\). Each open cell therefore has at
most one stationary point, and its infimum is at that point or an
admissible one-sided boundary.

As \(t\) increases, an action-wall crossing raises \(B_0\) by one. Its
jump is

\[
 \frac{\pi}{2t}-1>0,
\]

while the literal strict bracket at the wall retains the lower,
left-hand value. At \(\lambda=3/4\), the quadratic derivative is zero
and matches the zero branch. At \(\lambda=a\), increasing \(t\) moves
from the quadratic to the saturated branch, so the derivative jumps
downward; this can create a maximum but not a new minimum. At
\(\lambda=1\), the top payment is zero on both sides; the coincident
action wall is already owned by the literal lower value. These facts
justify the boundary list in (4.6).

One presentation convention is essential: at a strict excluded endpoint,
“boundary” in (4.6) means the admissible one-sided limit. In particular,
\(\lambda\downarrow0\) has \(\mathcal E\to1\); substituting the excluded
literal value \(\lambda=0\) into the indicator would be wrong. Section
5.7 of the source states this convention explicitly, so this is not a
blocking omission.

## 5. Remaining equality faces and scope

- \(A_t(x)=h\) is owned by the first shelf; \(A_t(x+1)=h\) and
  \(A_t(r)=h+1\) are one-sided adjacent-branch endpoints.
- Activity equality is excluded here and belongs to the no-mode result.
- If \(\alpha=0\), then \(q=\mu\) and \(J=0\) exactly. Spatial
  monotonicity remains valid when \(x+1=\mu\).
- The reported \(\alpha\uparrow1\) family is a one-sided limit of the
  fixed \(q=6\) cell, not an admissible \(\alpha=1\) tuple. The source
  labels it as a limiting pattern and uses it only diagnostically.
- Every relevant shelf sample satisfies \(r+j\leq x+1\leq\mu<K\), so no
  \(r+j=K\) face is hidden.
- Coincident shelf, action, or top-payment walls are covered by the same
  ordinary/strict and one-sided conventions above.

Only two positive terms are discarded: the elasticity alternative in
\(L_0\), and the final reserve \(1/8-J\). The exact shelf walls,
activity, \(B_0\), top payment, and relation
\(\mu=r+p+m+\alpha\) remain correlated. The rigorous endpoint is
therefore precisely (4.6); its sign remains open.

## 6. Independent Mathematica replay

Replay:

- computations/general_d_round23_curvature_cell_replay.wl
- SHA-256 0b64e5e56806aa9e5b18cc8057663cf3990a292950aa1500e1fe7b7f4a58b7a8
- Wolfram 15.0 command: math.exe -noinit -script
  computations/general_d_round23_curvature_cell_replay.wl

The fresh replay returned

    exactSymbolicOK=True
    capEndpointN=0.121149160634338540066475825322...
    hardDomainOK=True
    tHard=1.005008958418235371436088182895...
    lambdaHard=0.480629613415451621832363738338...
    C8Hard=0.0128644519808568087168795270768...
    RJCurvatureHard=0.0466496215336397339195592705706...
    hardValuesOK=True
    round23ReplayOK=True

The derivative and cap-chain checks are exact/symbolic. The hard-family
values are explicitly diagnostic arbitrary-precision checks and are not
a certificate for \(\mathcal C_8\geq0\).

**Final verdict: PASS.** No hidden sign error, omitted top-payment
branch, or wall-ownership blocker was found. The general theorem remains
open at the scalar obligation (4.6).
