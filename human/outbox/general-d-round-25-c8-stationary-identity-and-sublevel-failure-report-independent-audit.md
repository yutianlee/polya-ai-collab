# Independent audit of Round 25 stationary identity and sublevel failure report

Date: 19 July 2026  
Verdict: **PASS**

Audited artifacts:

- `human/outbox/general-d-round-25-c8-stationary-identity-and-sublevel-failure-report.md`
  
  SHA-256 `022192057330cb560164828d4b3cbd296ef3234275750ceacdc385cbbfc56bbb`
- `computations/general_d_round25_c8_stationary_sublevel_diagnostic.py`
  
  SHA-256 `377cc0209ac62352cfd738ddcce431aafb0049b840e6c11a827d6d863545dbd3`

The verdict covers the stationary identity, its signs, the two strict shelf
consequences, the \(P\)- and interface-based upper bounds for \(p\), and the
one-sided implication \(\mathcal C _8\geq\mathcal F\). It does not certify
\(\mathcal F\geq0\) on the exact projected shelf image, \(\mathcal C _8\geq0\),
CST-H, or the general-dimensional Polya theorem. Those statements remain
open exactly as the source says.

## 1. Exact stationary identity and signs

On the open quadratic cell, fixed-\(\mu\) differentiation of the audited
Round 23 scalar gives

\[
 D_t\mathcal C _8=
 {p^2(3r+2p)\sin t\over3\pi\mu}
 -{m\over\pi}-{B\pi\over2t^2}
 +{4u\mu\tan^2t\over\pi}.
\]

Since

\[
 \mu={\pi(B+u)\over H},\qquad H=\tan t-t,
\]

the last term is exactly

\[
 {4u\mu\tan^2t\over\pi}
 ={4u(B+u)\tan^2t\over H}=L.
\]

At a stationary point, therefore,

\[
 {p^2(3r+2p)\sin t\over3\pi\mu}
 ={m\over\pi}+{B\pi\over2t^2}-L=R.
\]

The left side is strictly positive because \(p\geq1\), \(r\geq1\),
\(0<t<\pi/2\), and \(\mu>0\). Thus the conclusion \(R>0\) is valid and is
not an extra assumption. Substituting for \(\mu\) gives precisely

\[
 {p^2(3r+2p)H\sin t\over3\pi^2(B+u)}=R.
\]

The curvature value in \(\mathcal C _8\) is the curvature derivative above
times

\[
 {1-\cos t\over\sin t}=\tan(t/2)=z.
\]

It is consequently \(zR\). Expanding \(zR\) in the original scalar and
collecting the \(m\)- and \(B\)-terms gives

\[
\begin{aligned}
 \mathcal C _8={}&m\left({1\over2}-{t\over\pi}+{z\over\pi}\right)
 +B\left({\pi\over2t}-1+{\pi z\over2t^2}\right)\\
 &-{p\over2}-{1\over8}+2u^2-zL,
\end{aligned}
\]

including the direction-sensitive sign \(-zL\). A fresh Mathematica 15.0
kernel replay returned zero for each of the terminal-action substitution,
the half-angle identity, and the difference between this expression and the
stationary expansion.

## 2. Convex shelf kernel and the strict \(m\)-window

Put

\[
 g(y)=\arccos(y\cos t)-\arccos y,\qquad 0<y<1.
\]

Then \(g(0)=0\), \(g'(0)=1-\cos t\), and direct differentiation gives

\[
 g''(y)=y\left{
 (1-y^2)^{-3/2}
 -\cos^3t\,(1-y^2\cos^2t)^{-3/2}
 \right}>0.
\]

The last inequality follows after taking the positive \(2/3\) power: it is
equivalent to \(1>\cos^2t\). Strict convexity therefore puts \(g\) strictly
above its tangent at zero, and hence

\[
 \sigma(s)={g(s/\mu)\over\pi}
 >{(1-\cos t)s\over\pi\mu}.
\]

The other elementary bound is \(0<\sigma(s)<t/\pi\) for
\(0<s<\mu\). Its limiting equality at the single endpoint \(s=\mu\) has no
effect on either integral.

Because \(\mu-x=m+\alpha<m+1\), the retained lower shelf relation gives

\[
 \delta\leq\int_x^\mu\sigma(s)\,ds
 <{(m+1)t\over\pi}.
\]

For the first-drop relation, the interval

\[
 [\mu-(m-1),\mu]\subseteq[x+1,\mu]
\]

has the correct inclusion direction. Integrating the tangent lower bound on
that subinterval gives

\[
 { (1-\cos t)(m-1)(2\mu-m+1)\over2\pi\mu}.
\]

When \(m>1\), strict convexity makes the comparison with the full first-drop
integral strict. When \(m=1\), the displayed subinterval has zero length and
the desired strict inequality reduces to \(0<\delta\), which follows from
\(0<u<1/\sqrt2<3/4\) (and also from the strict first-drop integral itself).
Thus both inequalities in (1.3), including all strict signs, are correct.

## 3. The \(P\), \(\psi\), and interface bounds

Rearranging the exact stationary equation yields

\[
 P={3\pi^2(B+u)R\over H\sin t}=p^2(3r+2p).
\]

In particular \(P>0\). Since both owner grids have \(r\geq1\),

\[
 P\geq p^2(2p+3).
\]

The function \(s\mapsto s^2(2s+3)\) has derivative
\(6s(s+1)>0\) for \(s>0\), so its positive inverse is well defined and
\(p\leq\psi(P)\). Independently,

\[
 \mu=r+p+m+\alpha,\qquad r\geq1,\quad\alpha\geq0,
\]

gives \(p\leq\mu-m-1\). Therefore

\[
 p\leq p_{\max}=\min\{\mu-m-1,\psi(P)\}.
\]

The only \(p\)-term in the exact stationary identity is \(-p/2\). Because
\(p_{\max}\geq p\), replacing it by \(-p_{\max}/2\) lowers the right-hand
side. The claimed direction

\[
 \mathcal C _8\geq\mathcal F
\]

is therefore correct. No sign of the still-open scalar is smuggled into this
step.

## 4. Equality faces and projection scope

The face assignments are consistent.

- The ordinary lower shelf equality is retained, so the first integral is
  weakly bounded below by \(\delta\).
- The first-drop equality is excluded and supplies the strict upper bound on
  the second integral.
- The interface face \(\alpha=0\) is included, while \(\alpha=1\) is only a
  limit. The bound \(p\leq\mu-m-1\) remains valid on the included face.
- The action faces \(u=0\) and \(u=1/\sqrt2\) are outside the open cell.
- \(R=0\) is impossible because it equals a strictly positive curvature
  derivative.
- Every shelf location is at most \(x+1\leq\mu<K\), including the possible
  equality \(x+1=\mu\); no outer turning face is hidden.

The phrase *full projected shelf image* must be read as an existence
projection of the retained exact problem: there must exist an allowed owner
grid, integers \(r,p,m,B\), and \(\alpha\in[0,1)\) satisfying the complete
Round 24 shelf conditions (including the start wall), interface identity,
activity and cell conditions, together with stationarity. The at-most-two
owner rule is a shorthand reduction inside that existence problem, not an
independent continuous constraint. With this reading, proving
\(\mathcal F\geq0\) on the image, or on any rigorously described superset of
it, would indeed close every interior stationary candidate on this cell.

Conversely, the relaxed conditions (1.1), (1.3), the interface upper bound,
activity, and (1.5) do not characterize that image. A relaxed point need not
possess any discrete stationary owner or satisfy the full shelf integrals.
Thus the obstruction below falsifies only that continuous relaxation; it
does not falsify \(\mathcal F\) on the exact image or \(\mathcal C _8\).

## 5. Relaxed obstruction and diagnostic replay

The advertised relaxed point is

\[
 (B,m,t,u)=\left(1,11,{1\over5},{1\over1000}\right).
\]

In addition to the ordinary double-precision replay, I checked it with
80-decimal Arb ball arithmetic. The resulting certified margins include

\[
\begin{aligned}
 R&>42.71,\\
 (\mu-m-1)-100&>1048.40,\\
 P-100^2(2\cdot100+3)&>321175,\\
 \delta-\delta_{\rm tangent}&>0.6858,\\
 {(m+1)t\over\pi}-\delta&>0.0149.
\end{aligned}
\]

The activity gap remains greater than \(1.377\times10^6\) even with the
larger half-integer constant \(\gamma=2\). Monotonicity of
\(s^2(2s+3)\) makes the third line imply \(\psi(P)>100\); the second line
then gives \(p_{\max}>100\). If \(\mathcal F_0\) denotes (1.7) before the
term \(-p_{\max}/2\), Arb gives

\[
 \mathcal F_0-50<-34.18.
\]

Consequently \(\mathcal F<-34.18<0\) rigorously on the displayed relaxed
point. The source's much sharper double-precision value
\(\mathcal F\approx-36.70727529\) is consistent with this certification.

Fresh command:

```text
python -B computations/general_d_round25_c8_stationary_sublevel_diagnostic.py
```

The replay returned exit code zero. It reproduced the feasible numerical
witness at

\[
 (r,p,m,f,\alpha)=(1,5,5,2,0.999999),
\]

with derivative residual \(8.21\times10^{-8}\), direct value
\(\mathcal C _8\approx0.367089577306233\), stationary-identity value
\(0.367089540314934\), and lower scalar
\(\mathcal F\approx0.367089574766956\). These differences are within the
stated minimization tolerance. It also reproduced the relaxed value
\(\mathcal F\approx-36.7072752909976\) and both strict shelf-window margins.

The feasible witness is ordinary double-precision theorem-design evidence,
not a certified stationary point; the PASS verdict does not rely on it.

**Final verdict: PASS.** The stationary reduction and all one-sided
inequalities have the stated directions, the equality faces are safe, and
the relaxed obstruction is correctly scoped. The exact projected-image sign
and the C8/general theorem remain open.
