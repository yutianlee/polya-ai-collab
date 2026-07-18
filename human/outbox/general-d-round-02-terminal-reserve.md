# General dimension round 02: terminal-reserve reduction

Date: 18 July 2026  
Scope: arbitrary inner tails in the shifted-tail conjecture  
Status: the residual set is substantially localized, but the final scalar
inequality is not yet proved.

Write

\[
 \mu=\rho K,\qquad
 A=G_K-G_\mu,\qquad
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,
\]

and put

\[
 F_j=\left\lfloor A(r+j)+\frac14\right\rfloor
 \quad(0\le j\le n).
\]

Let (p) be the last index on the first ordinary-floor shelf,
(F_0=F_p); if there is no drop before (q), put (p=n).  Finally set

\[
 c=\frac{\arccos\rho}{\pi},\qquad
 d=1-2c=\frac{2\arcsin\rho}{\pi}.
\]

## 1. Exact shelf/terminal reduction

The wall-safe first-shelf reduction is

\[
 \boxed{
 D_A(r)\ge D_A(q)+R_p+\frac d2(n-p),
 }
 \tag{1}
\]

where

\[
 R_p=2\int_r^{r+p}A(z)\,dz-2pF_0.
 \tag{2}
\]

This is stronger than retaining only the generic loss (-p/2).  If

\[
 \epsilon_j=A(r+j)+\frac14-F_j,
\]

then, away from an ordinary-floor wall (with the wall values obtained by
the favorable strict convention),

\[
 R_p=C_p+p\left(\epsilon_0+\epsilon_p-\frac12\right),
 \tag{3}
\]

\[
 C_p=2\int_r^{r+p}A(z)\,dz
      -p\bigl(A(r)+A(r+p)\bigr)
 =-\int_0^p t(p-t)A''(r+t)\,dt\ge0.
 \tag{4}
\]

Consequently

\[
 R_p\ge-\frac p2.
 \tag{5}
\]

There are two useful strict localizations.

1. If (F_0=0), then (R_p=2\int_r^{r+p}A\ge0), so (1) is already
   nonnegative by the proved one-interface theorem at (q).
2. If (p\le d(n-p)), (5) pays the whole shelf loss.  Hence a genuinely
   dangerous tail must satisfy

   \[
    F_0\ge1,\qquad p>d(n-p).
    \tag{6}
   \]

The first condition in (6) implies

\[
 A(r)\ge\frac34,
 \qquad
 A(0)=\frac{K(1-\rho)}\pi>A(r),
\]

and therefore

\[
 \boxed{K(1-\rho)>\frac{3\pi}{4}.}
 \tag{7}
\]

Moreover, if (R_p<0), (3) implies

\[
 \epsilon_0+\epsilon_p<\frac12,
 \qquad
 A(r)-A(r+p)=\epsilon_0-\epsilon_p<\frac12.
 \tag{8}
\]

Thus a negative first-shelf reserve can occur only in the lower half of a
single floor bin; the earlier bound by a full unit loses a factor two in
precisely the active branch.

For reference, with

\[
 \kappa=\frac{1-\rho}{\pi\rho K},
\]

the exact shell curvature gives

\[
 C_p\ge\frac{\kappa p^3}{6},
 \qquad
 A(r)-A(r+p)\ge\frac\kappa2p(p+2r).
 \tag{9}
\]

## 2. An explicit terminal lower bound

Put (alpha=\mu-q\in[0,1)) and

\[
 n_0=
 \left[G_K(q)+\frac14\right]_<
 -\left[A(q)+\frac14\right]_<.
\]

The one-interface identity is

\[
 D_A(q)=D_K(q)+n_0-2\int_q^\mu G_\mu(z)\,dz.
 \tag{10}
\]

The refined convex ball theorem and the turning estimate give

\[
 D_A(q)\ge
 \frac12\left\lfloor
 G_K\!\left(\max\{q,K/2\}\right)
 \right\rfloor+n_0
 -\frac{4\alpha^{5/2}}{15\sqrt\mu}.
 \tag{11}
\]

In particular, since the one-interface theorem also gives (D_A(q)\ge0),

\[
 D_A(q)\ge
 \max\left\{0,
 \frac12\lfloor H_q\rfloor+n_0-\frac{4\sqrt2}{15}
 \right\},
 \quad
 H_q=G_K(\max\{q,K/2\}).
 \tag{12}
\]

Equations (1)--(2) and (11) are a completely explicit remaining scalar.
For example, the crude curvature-free version is automatically positive
whenever

\[
 \lfloor H_q\rfloor+2n_0
 \ge p-d(n-p)+\frac{8\alpha^{5/2}}{15\sqrt\mu}.
 \tag{13}
\]

Any residual tail must violate (13), in addition to (6)--(8).

## 3. A sharper thin-shell theorem

The optimized local-plateau argument used in the accepted three-dimensional
thin-shell packet is in fact an individual-tail argument before the tails
are summed.  In the present notation it gives the following strengthening
of the fixed-ratio high-energy proposition.

> **Thin high-energy shifted tails.**  Let
> \(\rho=1-\varepsilon\), \(0<\varepsilon\le1/100\).  If
> \[
>  K\ge\frac{125}{8\varepsilon^2},
> \]
> then (D_A(r)\ge0) for every (r\in\tfrac12\mathbb N).

Here is the constant ledger.  In the dangerous branch put

\[
 y=\sqrt\varepsilon,\quad
 \varkappa=K\varepsilon^2,\quad
 m=n-p,\quad
 R=p-dm,\quad
 P=py,\quad \mathfrak r=Ry,\quad S=(p+m)y.
\]

The same-floor geometry gives

\[
 R<\frac{361}{80y}.
 \tag{14}
\]

Also

\[
 G_1(1-\varepsilon)
 \ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\]

At \(\varkappa\ge125/8\), the exact rational estimates in the accepted
ledger yield

\[
 \lfloor K G_1(\rho)\rfloor-R
 >\frac{2829397}{3732696}
 >\frac{132}{175}
 >4\int_q^\mu G_\mu.
 \tag{15}
\]

This is precisely the strict payment needed in the concave-head/convex-tail
split.  It improves the asymptotic threshold of the current fixed-ratio
formula from order \(\varepsilon^{-4}\) to order \(\varepsilon^{-2}\).

Consequently, in the thin sector the remaining arbitrary-inner-tail region
is rigorously confined to

\[
 0<\varepsilon\le\frac1{100},\qquad
 \frac{3\pi}{4\varepsilon}<K<\frac{125}{8\varepsilon^2},
 \tag{16}
\]

together with (6), (8), and the failure of (13).  The left inequality in
(16) is strict.

## 4. First floor level and an ownership warning

Suppose (F_0=1).  If (p<n), monotonicity shows that every sample after
(r+p) has ordinary floor zero.  Hence

\[
 T_A(r)\le1+2p.
 \tag{17}
\]

Put

\[
 a=A(r),\quad b=A(r+p),\quad u=A(q),\quad
 h=A(\mu)=G_K(\mu),\quad \alpha=\mu-q.
\]

Concavity on the two inner blocks and the tangent triangle for the outer
convex ball action give

\[
 2\int_r^K A
 \ge p(a+b)+(n-p)(b+u)+\alpha(u+h)+\frac{h^2}{c}.
 \tag{18}
\]

Thus (18) compared with (17) is a useful sufficient scalar in the
(F_0=1, p<n) branch.  A two-million-point diagnostic scan in the active
region found a minimum surplus about (0.1308), but this is not a proof of
its nonnegativity.

The restriction (p<n) is essential.  If (p=n), the first shelf has not
dropped before (q), and samples (q+1,q+2,\ldots) on the outer ball may
still contribute.  In that no-drop branch one must use (1) with the full
terminal defect (D_A(q)); replacing the terminal block by the raw count
(1+2p) is not justified.

There is one more useful exact shape fact.  On the inner interval,

\[
 \sigma(z)=-A'(z)
 =\frac{\arccos(z/K)-\arccos(z/\mu)}\pi
\]

is increasing and convex, with (sigma(0)=0) and (sigma(\mu)=c).
Therefore

\[
 \boxed{\sigma(z)\le\frac{cz}{\mu}.}
 \tag{19}
\]

For (L=\mu-r-p), (19) gives the sharper endpoint relation

\[
 h\ge b-cL+\frac{cL^2}{2\mu}.
 \tag{20}
\]

This is the most promising analytic input for proving the scalar in
(18); the plain global Lipschitz triangle discards the positive last term
in (20).

There is also a pointwise form that retains this gain.  Let (y\le\mu),
(v=A(y)), and put

\[
 z_*=sqrt{y^2+\frac{2\mu v}{c}}.
\]

Equation (19) implies, for (y\le z\le\mu),

\[
 A(z)\ge
 \max\left\{v-\frac{c}{2\mu}(z^2-y^2),0\right\}.
 \tag{21}
\]

If (z_*\le\mu), integration gives the explicit terminal envelope

\[
 2\int_y^K A(z)\,dz
 \ge
 \frac{c(z_*-y)^2(2z_*+y)}{3\mu}.
 \tag{22}
\]

If (z_*>\mu), set

\[
 L=\mu-y,\qquad
 h_0=v-cL\left(1-\frac{L}{2\mu}\right)>0.
\]

Integrating (21) to the interface and then using the outer tangent
triangle yields

\[
 2\int_y^K A(z)\,dz
 \ge
 2vL-\frac{cL^2(\mu+2y)}{3\mu}+\frac{h_0^2}{c}.
 \tag{23}
\]

Unlike the global (v^2/c) triangle, (22)--(23) becomes large when the
current point is far from the interface and the locally admissible slope
is much smaller than (c).  It is therefore suited to the (p<n) branch
of (18), with (y=r+p+1) after the first floor drop.  It does not remove
the ownership warning in the no-drop branch.

For thin shells, the following alternative to (19) is much sharper away
from the interface.  Differentiating the shell action with respect to its
radius parameter gives

\[
 \sigma(z)=\int_\mu^K
 \frac{z}{\pi a\sqrt{a^2-z^2}}\,da
 \le
 \frac{1-\rho}{\pi\rho}
 \frac{z}{\sqrt{\mu^2-z^2}}.
 \tag{24}
\]

Writing (lambda=(1-\rho)/(\pi\rho)), integration from an inner point
(y) gives the pointwise lower envelope

\[
 A(z)\ge v-\lambda\left(sqrt{\mu^2-y^2}
                    -\sqrt{\mu^2-z^2}\right),
 \qquad y\le z\le\mu.
 \tag{25}
\]

Its positive part can be integrated in closed form using

\[
 J_\mu(z)=\frac12\left(
 z\sqrt{\mu^2-z^2}+\mu^2\arcsin\frac z\mu
 \right).
 \tag{26}
\]

Specifically, put (S_y=\sqrt{\mu^2-y^2}).  If
(v\le\lambda S_y), let

\[
 z_*=sqrt{\mu^2-(S_y-v/\lambda)^2};
\]

then

\[
 2\int_y^K A
 \ge2\left[(v-\lambda S_y)(z_*-y)
       +\lambda\bigl(J_\mu(z_*)-J_\mu(y)\bigr)\right].
 \tag{27}
\]

If (v>\lambda S_y), take (z_*=\mu) in the bracket and add the outer
tangent reserve

\[
 \frac{(v-\lambda S_y)^2}{c}.
 \tag{28}
\]

The bound (24) retains the shell thickness and is orders of magnitude
stronger than (19) in the long, thin first-shelf regime.  A large
diagnostic scan of the deliberately weakened certificate consisting only
of the first shelf, its first drop cell, and (27)--(28) left a narrow
central residual.  A targeted ten-million-point pass found only the
following discrete chambers:

\[
\begin{gathered}
 (n,p,r)=(4,3,\tfrac12),(5,4,\tfrac12),(5,4,1),
 (6,5,\tfrac12),(6,5,1),\\
 (7,6,\tfrac12),(7,6,1),(8,6,\tfrac12),
 (8,7,\tfrac12),(9,7,\tfrac12).
\end{gathered}
\tag{29}
\]

Every sampled failure in (29) lay in

\[
 0.6116<\rho<0.7471,\qquad
 7.555<K<12.751,\qquad
 0.909<A(0)<1.090,\qquad
 \frac34<A(r+p)<0.7621.
 \tag{30}
\]

The smallest weakened-certificate value was about (-0.1714).  On the
same sampled failure set, the fuller true-interface certificate (18) had
minimum greater than (0.53).  Thus (29)--(30) are a plausible target for
a small rational interval certificate.  They are diagnostic bounds only:
no rigorous claim is made here that (29)--(30) exhaust the continuous
failure set.  In particular, (24) is an endpoint estimate, not by itself
a proof of the first-floor branch.

There is, however, a rigorous dimension reduction for any finite
certificate of (18).  Use ((\mu,K)), rather than ((\rho,K)), as the
independent parameters.  Fix (r,n,p), and hence
(q=r+n), on a chamber with (p<n) and

\[
 q\le\mu<q+1.
\]

For fixed (mu), every sampled shell action is strictly increasing in
(K), because

\[
 \partial_K A(z)=\partial_KG_K(z)
 =\frac1\pi\sqrt{1-\frac{z^2}{K^2}}>0.
 \tag{31}
\]

The only non-obvious term in (18) is also increasing.  If

\[
 \theta=\arccos\frac\mu K,
\]

then

\[
 h=\frac\mu\pi(\tan\theta-\theta),\qquad
 c=\frac\theta\pi,\qquad
 \frac{h^2}{c}
 =\frac{\mu^2}{\pi}
  \frac{(\tan\theta-\theta)^2}{\theta}.
 \tag{32}
\]

This last expression is strictly increasing in \(\theta\), and hence in
(K).  Indeed,

\[
 \tan\theta-\theta=\int_0^\theta\tan^2s\,ds
 \le\theta\tan^2\theta,
\]

which makes the logarithmic derivative in (32) positive.

It follows that the complete right side of (18), with its count payment
subtracted, is strictly increasing in (K) on a fixed chamber.  Therefore
its minimum is the post-crossing limit at the unique first-shelf wall

\[
 \boxed{A(r+p)=\frac34.}
 \tag{33}
\]

Existence and uniqueness of this wall follow from (31).  At the wall
itself the strict bracket is favorable, so the value that must be checked
is the right-hand limit.  Thus every two-parameter chamber reduces to the
one-dimensional interval (q\le\mu<q+1) along the curve
(K=k_{r+p}(\mu)) defined by (33).  This is an exact finite-wall
reduction; what is not yet proved is the global analytic exclusion that
would leave only the diagnostic chamber list (29).

The independent Arb verifier

`scripts/general_d_first_shelf_wall_verify.py`

implements this reduction for all ten chambers in (29).  The exact wall
intervals are

| ((n,p,r)) | (mu)-interval | wall |
|---|---:|---:|
| ((4,3,1/2)) | ([9/2,11/2]) | (A(7/2)=3/4) |
| ((5,4,1/2)) | ([11/2,13/2]) | (A(9/2)=3/4) |
| ((5,4,1)) | ([6,7]) | (A(5)=3/4) |
| ((6,5,1/2)) | ([13/2,15/2]) | (A(11/2)=3/4) |
| ((6,5,1)) | ([7,8]) | (A(6)=3/4) |
| ((7,6,1/2)) | ([15/2,17/2]) | (A(13/2)=3/4) |
| ((7,6,1)) | ([8,9]) | (A(7)=3/4) |
| ((8,6,1/2)) | ([17/2,19/2]) | (A(13/2)=3/4) |
| ((8,7,1/2)) | ([17/2,19/2]) | (A(15/2)=3/4) |
| ((9,7,1/2)) | ([19/2,21/2]) | (A(15/2)=3/4) |

Each interval is divided into (256) exact rational subintervals.  The
wall root at every endpoint is isolated by (110) exact dyadic bisections,
and monotonicity of (K(\mu)) encloses the intervening wall segment.  At
(384)-bit precision the script reports

```text
CERTIFIED: C>0 on all 2560 wall boxes in all 10 chambers.
```

This is a rigorous certificate for the listed wall intervals, not a
certificate that (29) is exhaustive.  The missing analytic step remains
the exclusion of every other discrete chamber by (24)--(28) or a stronger
global envelope.

## 5. Falsified shortcuts

Two tempting terminal estimates are not valid proof routes.

1. Replacing (R_p) by (-p/2) can create a large artificial deficit even
   when the exact (R_p) is strongly positive.  For example, at
   \(\rho\approx0.9519543127\), \(K\approx220.9985998\), \(r=125.5\), one
   has (n=84,p=58,F_0=2).  The bound using (-p/2) is about
   (-12.33), whereas (R_p\approx37.83) and the exact scalar in (1) is
   about (54.49).
2. Even in the first-floor branch, the assertion that
   (A(0)>1) alone makes
   \[
    p\bigl(A(r)+A(r+p)\bigr)+\frac{A(q)^2}{c}\ge1+2p
   \]
   is false.  Take
   \[
    \rho=0.6347160656102075,\qquad
    K=\frac{\pi}{1-\rho}(1.0001),qquad r=\frac12.
   \]
   Then (A(0)=1.0001), (n=p=4), (F_0=1), and the displayed
   left side minus the right side is approximately
   (-0.00805869).  The failure occurs in a very narrow wedge immediately
   after the wall (A(q)=3/4), which explains why untargeted random scans
   miss it.  The actual shifted-tail defect is positive; this only
   falsifies the proposed lower certificate.

## 6. Remaining target

After the proved one-interface theorem, the fixed-ratio theorem, and the
thin strengthening above, the sole unresolved statement is (1) in the
active set

\[
 n\ge1,\quad F_0\ge1,\quad p>d(n-p),\quad R_p<0,
\]

subject to (7), (8), failure of (13), and (16) in the thin sector.  The
exact (R_p), not its generic lower bound, and the quantitative
one-interface terminal reserve (D_A(q)) must be kept together.  No
counterexample to their sum was found, but the present note does not claim
the global shifted-tail theorem.
