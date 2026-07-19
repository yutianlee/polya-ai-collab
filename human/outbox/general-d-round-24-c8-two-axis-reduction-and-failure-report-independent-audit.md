# Independent audit of Round 24 two-axis reduction

Date: 19 July 2026  
Verdict: **PASS**

Audited source:

- `human/outbox/general-d-round-24-c8-two-axis-reduction-and-failure-report.md`
- SHA-256 `1ac4917c6c6d42a1853e1ad226ab80dbc50d397ff6ae15373c21dcf47f9aefcf`

The verdict covers the exact fixed-\(x\) reduction, the specialized
elimination of \(\alpha\), the lower-shelf-wall transport calculation, and
the stated equality conventions. It does not certify
\(\mathcal C_8\geq0\), \(\widehat{\mathcal C}_8\geq0\), CST-H, or the
general-dimensional Polya theorem. Those signs remain open exactly as the
source says.

## 1. Fixed-\(x\) feasible prefix

Fix a parity grid and \((x,m,\alpha,f,t)\), and write \(r=x-p\). Then

\[
 q=x+m,\qquad \mu=x+m+\alpha
\]

are independent of \(p\). Consequently the lower shelf wall, the first-drop
wall, \(W\), \(\lambda\), \(B_0\), and the owner activity inequality are all
fixed. The activity constant \(\gamma\) is fixed because the parity grid is
fixed. The only remaining \(p\)-dependent shelf condition is

\[
 A_t(x-p)<h+1,
\]

together with the grid lower bound on \(r=x-p\).

Direct spatial differentiation gives

\[
 \partial_z A_t(z)
 =\frac{\arccos(z/\mu)-\arccos(z\cos t/\mu)}{\pi}<0.
\]

Thus lowering \(p\) raises \(r\), decreases \(A_t(r)\), and preserves the
strict start inequality; it also preserves the lower bound on \(r\). Once
one positive integer \(p\) is feasible, every smaller positive integer is
feasible. The feasible set is therefore exactly \(\{1,\ldots,P\}\), with
\(P\) bounded jointly by the strict start wall and the grid endpoint. This
also verifies the source's corrected equality-face description: either bound
may own \(P\), and equality at the start wall is never assigned to this
branch.

## 2. Strict convexity and the \(p_*\) cases

At fixed intrinsic data, the complete \(p\)-dependent contribution is

\[
 S(p)=kp^2(3x-p)-\frac p2,
 \qquad k=\frac{1-\cos t}{3\pi\mu}>0.
\]

Exact differentiation gives

\[
 S'(p)=3kp(2x-p)-\frac12,
 \qquad S''(p)=6k(x-p)=6kr>0
\]

throughout the feasible real interval. A fresh Wolfram 15 symbolic replay
returned these same two expressions. Hence \(S'\) is strictly increasing on
\([1,P]\).

- If \(6kx^2\leq1\), then \(S'(p)<0\) for \(p<x\), so the minimum is at
  \(P\).
- Independently, if \(S'(P)\leq0\), monotonicity makes \(S\) nonincreasing
  on the prefix, again giving \(P\).
- If \(S'(1)\geq0\), the minimum is at \(1\).
- In the remaining case the unique zero in \((1,P)\) is

  \[
   p_*=x-\sqrt{x^2-\frac1{6k}},
  \]

  and the discrete minimum lies at its floor or ceiling within the prefix.

This proves the claimed at-most-two-owner rule without a ratio partition.
The source correctly states that it is a coupled coordinatewise rule:
\(P\) and \(p_*\) depend on \(t\), while a \(t\)-cell stationary point
depends on \(p\). It is not an independently precomputed Cartesian list.

## 3. Exact elimination of \(\alpha\) on the delicate cell

On the stated cell let \(B=B_0=f-1\) and

\[
 u=W-B=\frac34-\lambda,
 \qquad 0<u<\frac1{\sqrt2}.
\]

Since \(1/\sqrt2<3/4\), this open interval crosses no terminal-action wall;
the literal bracket remains \(B_0=B\). The payment is exactly
\(\mathcal E=2u^2\). From

\[
 W=\frac\mu\pi(\tan t-t)=B+u
\]

one obtains, with no inequality,

\[
 \mu=\frac{\pi(B+u)}{\tan t-t}.
\]

The condition \(\mu=r+p+m+\alpha\), \(0\leq\alpha<1\), is exactly

\[
 r+p+m\leq\frac{\pi(B+u)}{\tan t-t}<r+p+m+1.
\]

Substitution of \(1/\mu=(\tan t-t)/[\pi(B+u)]\) into the curvature term
gives precisely the first term of (3.5), including its factor
\(3\pi^2(B+u)\). All other displayed terms agree, so (3.5) is an exact
reparametrization. At the included lower shelf wall,

\[
 A_t(x)=h=B+\frac34,
\]

and subtraction of \(W=B+u\) gives both balances in (3.6). The retained
domain must include \(B=f-1\in\mathbb N\), the open \(u\)-cell, the strict
activity wall, the shelf inequalities, and the interface strip. The source
now lists all of them.

## 4. Lower-shelf-wall transport

Let \(y=x/\mu\),

\[
 U=\sqrt{\sec^2t-y^2},\qquad V=\sqrt{1-y^2}.
\]

Here \(0<y<1\), since \(\mu=x+m+\alpha>x\). Differentiating
\(G_{\mu/\cos t}(x)-G_\mu(x)\) at fixed \(x\) gives exactly

\[
 \mathcal A_\mu=\frac{U-V}{\pi}>0,
 \qquad
 \mathcal A_t=\frac{\mu\tan t\,U}{\pi}>0.
\]

Implicit differentiation along \(\mathcal A=h\) therefore yields

\[
 t_\mu=-\frac{U-V}{\mu\tan t\,U}<0.
\]

Using this in \(W=\mu(\tan t-t)/\pi\) simplifies to

\[
 W_\mu=\frac1\pi\left(
 \frac{\sin t\sqrt{1-y^2}}{\sqrt{1-y^2\cos^2t}}-t
 \right).
\]

The square-root quotient is strictly below one, while
\(0<\sin t<t\); hence \(W_\mu<0\), and
\(\lambda_\mu=-W_\mu>0\).

Termwise differentiation of \(\mathcal C_8\) gives (4.5). Its curvature
contribution is strictly negative, its \(m\)-contribution is strictly
positive, and its \(B_0\)-contribution is nonnegative (strictly positive
only for \(B_0>0\)). On the open quadratic cell,
\(\mathcal E_\lambda=-4(3/4-\lambda)<0\), so the payment contribution is
strictly negative; it vanishes on constant cells. These competing signs
indeed prevent any global conclusion that \(\alpha\uparrow1\) is always
worst.

## 5. Equality faces and theorem boundary

- \(A_t(x)=h\) is included by the ordinary-floor convention.
- \(A_t(x+1)=h\) and \(A_t(r)=h+1\) are excluded and enter only as
  admissible one-sided endpoints.
- At \(W+1/4\in\mathbb Z\), the strict bracket takes the lower integer.
  No such wall lies inside \(0<u<1/\sqrt2\).
- The interface strip includes \(\alpha=0\) and excludes \(\alpha=1\).
- The face \(\lambda=0\) is excluded by first-drop feasibility; its
  admissible one-sided payment tends to \(1\).
- Every sampled shelf position is at most \(x+1\leq\mu<K\), so no outer
  turning face \(r+j=K\) is hidden.

Round 23's strict convexity in each fixed-\(p\) action cell and Lemma 2.1's
strict convexity at fixed \(t\) supply coupled necessary candidate
conditions for a joint minimum or one-sided infimum. They do not prove the
candidate values nonnegative. Moreover, (3.3)--(3.5) specialize only the
cell

\[
 B=f-1\in\mathbb N,\qquad 0<u<1/\sqrt2.
\]

All other action/payment cells retain the original
\(\mathcal C_8\geq0\) obligation. The source states these limitations
explicitly and does not promote CST-H or the general theorem.

## 6. Diagnostic replay

Diagnostic artifact:

- `computations/general_d_round24_c8_wall_diagnostic.py`
- SHA-256 `c9257c1297f8b668cddb826754649d2829c6ab6d32d9583e2e2bf77714f94442`

Fresh command:

```text
python -B computations/general_d_round24_c8_wall_diagnostic.py --limit 8 --floors 6
```

The replay retained 40,569 feasible tuples and reproduced the reported
minimum

\[
 \mathcal C_8\approx0.012864572067208951
\]

at \((r,p,m,f,B_0,\alpha)=(1,3,2,2,1,0.999999)\). It also reproduced the
interior witness

\[
 \mathcal C_8\approx0.36708957730623326
 <0.3680202070581289,
\]

the latter being its lower-wall value, and reproduced both opposite sampled
\(\alpha\)-directions. No negative value appeared in the sweep.

This replay uses ordinary double precision, tolerance-based wall ownership,
and SciPy minimization. It is only falsification and theorem-design evidence;
none of its numerical output is used to establish the PASS verdict.

**Final verdict: PASS.** The two exact reductions and the wall-transport
lemma are correct, all strict/equality faces are assigned consistently, and
the remaining theorem boundary is stated without promotion.
