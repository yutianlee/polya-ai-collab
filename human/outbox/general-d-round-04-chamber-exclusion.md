# General dimension, Round 4: first-floor chamber reduction

Date: 18 July 2026  
Scope: the weakened first-drop/terminal-envelope certificate in the
ordinary first-floor branch (F_0=1, p<n)  
Status: exact wall reduction and several global necessary conditions are
proved.  All ten previously listed chambers are now rigorously shown to be
genuine failures of the weakened certificate, and the stronger
true-interface certificate is already rigorously positive on them.  The
claim that these ten chambers exhaust every weakened-certificate failure is
**not yet proved**.

## 1. The weakened certificate

Put

\[
 A=G_K-G_\mu,\qquad \mu=\rho K,
 \qquad n=\lfloor\mu-r\rfloor,
 \qquad q=r+n,
\]

and suppose that the first ordinary floor is one and drops before the
interface.  Thus, if (p) is the last index on the first shelf,

\[
 A(r+j)\ge\frac34\quad(0\le j\le p),
 \qquad A(r+p+1)<\frac34,
 \qquad p<n.
\]

Write

\[
 x=r+p,\qquad y=x+1,
 \qquad a=A(r),\quad b=A(x),\quad v=A(y),
\]

and

\[
 \lambda=\frac{1-\rho}{\pi\rho}
        =\frac{K-\mu}{\pi\mu},
 \qquad c=\frac{\arccos(\mu/K)}\pi,
 \qquad S_z=\sqrt{\mu^2-z^2}.
\]

The slope bound

\[
 -A'(z)\le \lambda\frac z{S_z},\qquad z<\mu,
\]

gives the pointwise profile

\[
 A(z)\ge v-\lambda(S_y-S_z),\qquad y\le z\le\mu.
\]

Its integrated terminal payment can be written without cases as

\[
 \mathcal E_{\mu,K}(y,v)
 =2\int_y^\mu
   \bigl[v-\lambda(S_y-S_z)\bigr]_+\,dz
 +\frac{(v-\lambda S_y)_+^2}{c}.
 \tag{1}
\]

This is exactly formulas (27)--(28) of the Round 2 terminal-reserve note.
Concavity on the first shelf and its first drop cell therefore proves the
tail whenever

\[
 \boxed{
 W:=p(a+b)+(b+v)+\mathcal E_{\mu,K}(y,v)-(1+2p)\ge0.}
 \tag{2}
\]

## 2. Exact reduction to the first-shelf wall

Fix ((\mu,r,p)).  Every term in (2) is strictly increasing in (K).
The sampled actions (a,b,v) are increasing because

\[
 \partial_KG_K(z)=\frac1\pi\sqrt{1-\frac{z^2}{K^2}}>0.
\]

It remains to justify the same assertion for (1).  Put

\[
 t(K)=\frac{v(K)}{\lambda(K)}.
\]

Since

\[
 v(K)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{y^2}{s^2}}\,ds,
\]

(t) is (mu) times the running average of a strictly increasing
function.  Hence both (t) and (lambda) are strictly increasing.  The
integral in (1) is

\[
 2\lambda\int_y^\mu[t-S_y+S_z]_+\,dz
\]

and is therefore increasing.

For the outer term, write

\[
 \theta=\arccos(\mu/K),\qquad
 h_0=v-\lambda S_y.
\]

On the branch (h_0>0), differentiation gives

\[
 \frac{dh_0}{d\theta}
 =\frac{\mu\sec\theta\tan\theta}{\pi}
 \left(
 \sqrt{1-\frac{y^2}{\mu^2}\cos^2\theta}
 -\sqrt{1-\frac{y^2}{\mu^2}}
 \right).
\]

The right side is increasing in \(\theta\).  Thus \(h_0\) is convex,
\(h_0(0)=0\), and \(h_0/\theta\) is increasing.  Consequently

\[
 \frac{h_0^2}{c}
 =\pi\theta\left(\frac{h_0}{\theta}\right)^2
\]

is increasing as well.  This proves the assertion.

It follows that the minimum of (W) in a fixed first-shelf chamber is the
post-crossing limit at the unique wall

\[
 \boxed{A(x)=\frac34.}
 \tag{3}
\]

Existence and uniqueness follow from strict (K)-monotonicity, since the
left side is zero at (K=\mu) and tends to infinity with (K).  Thus the
two continuous parameters have been reduced exactly to one.

## 3. Exact discrete reindexing

Define

\[
 s=n-p-1\in\mathbb Z_{\ge0}.
\]

Then

\[
 \boxed{
 x=r+p,\qquad q=x+s+1,
 \qquad q\le\mu<q+1.}
 \tag{4}
\]

Hence a chamber is equivalently indexed by

\[
 (r,p,s),\qquad
 r\in\tfrac12\mathbb N,\qquad p,s\in\mathbb Z_{\ge0},
\]

with (x) and (q) given by (4).  This reindexing makes the diagnostic
pattern transparent: the ten candidates have only

\[
 r\in\left\{\frac12,1\right\},qquad
 s\in\{0,1\},qquad x<8.
\]

This last statement is, at present, a description of the certified list,
not a proved global exclusion.

## 4. Necessary conditions for a wall failure

At the wall put

\[
 \Delta=A(r)-\frac34.
\]

Since

\[
 \frac34-v=\int_x^{x+1}(-A'(z))\,dz<c<\frac12,
\]

one has (v>1/4).  Formula (2) becomes exactly

\[
 \boxed{
 W=p\left(\Delta-\frac12\right)
   +v-\frac14+\mathcal E_{\mu,K}(y,v).}
 \tag{5}
\]

It follows immediately that a failure (W<0) must satisfy

\[
 \boxed{p\ge1,\qquad 0<\Delta<\frac12,
 \qquad \frac34<A(r)<\frac54.}
 \tag{6}
\]

In particular, (p=0) and every wall with
(A(r)\ge5/4) are rigorously excluded.

There are further global constraints.  Put

\[
 \sigma(z)=-A'(z)
 =\frac1\pi\int_\mu^K
 \frac{z}{a\sqrt{a^2-z^2}}\,da.
\]

Then (sigma(z)/z) is increasing.  Weighted-average comparison on
([0,r]), ([r,x]), and ([x,q]) gives

\[
 \boxed{
 \Delta\ge
 \bigl(A(0)-\tfrac34\bigr)
 \left(1-\frac{r^2}{x^2}\right),}
 \tag{7}
\]

and, with (u=A(q)\ge0),

\[
 \boxed{
 \Delta\le
 \frac34\frac{x^2-r^2}{q^2-x^2}.}
 \tag{8}
\]

Indeed, if (F(z)=\sigma(z)/z), then

\[
 \int_0^r zF(z)\,dz:
 \int_r^x zF(z)\,dz
 \le r^2:(x^2-r^2),
\]

which proves (7), while

\[
 \int_x^qzF(z)\,dz
 \ge\Delta\frac{q^2-x^2}{x^2-r^2}
\]

proves (8).

On the dimension-independent active spectral sector (A(0)>1), (7)--(8)
have the particularly simple consequence

\[
 \boxed{q<2x.}
 \tag{9}
\]

Indeed, (7) gives
\(\Delta>\frac14(x^2-r^2)/x^2\), and comparison with (8) yields
\(q^2-x^2<3x^2\).  Thus even before interval arithmetic, the
\(A(0)>1\) sub-sector of the failure set satisfies

\[
 s+1=q-x<x.
\]

Finally, (6)--(7) give the explicit wall-width bound

\[
 A(0)<\frac34+\frac{x^2}{2(x^2-r^2)},
 \qquad K-\mu=\pi A(0).
 \tag{10}
\]

## 5. Root-free lower certificate for future interval work

The wall root can be eliminated in favor of

\[
 A_0=A(0)=\frac{K-\mu}{\pi},qquad
 \lambda=\frac{A_0}{\mu},qquad K=\mu+\pi A_0.
\]

Since \(A(x)=A_0\) times the running average of
\(\sqrt{1-x^2/a^2}\) over \(a\in[\mu,K]\), and the wall value is
\(A(x)=3/4\), one has the strict feasibility
bounds

\[
 \frac{3/4}{\sqrt{1-x^2/K^2}}<A_0
 <\frac{3\mu}{4S_x}.
 \tag{11}
\]

Put

\[
 h_0=\frac34-\lambda S_x>0,
 \qquad
 v_0=h_0+\lambda S_y,
\]

and

\[
 J_\mu(z)=\frac12\left(
 z\sqrt{\mu^2-z^2}+\mu^2\arcsin\frac z\mu
 \right).
\]

The slope envelope anchored at the wall gives \(v\ge v_0\), and hence

\[
 \mathcal E_{\mu,K}(y,v)
 \ge
 2\left[
 h_0(\mu-y)+\lambda\bigl(J_\mu(\mu)-J_\mu(y)\bigr)
 \right]+\frac{h_0^2}{c}.
\]

Together with (7), this yields the entirely root-free lower bound

\[
\begin{aligned}
 W\ge{}&p\left[
 \left(A_0-\frac34\right)\left(1-\frac{r^2}{x^2}\right)-\frac12
 \right]+v_0-\frac14\\
 &+2\left[
 h_0(\mu-y)+\lambda\bigl(J_\mu(\mu)-J_\mu(y)\bigr)
 \right]+\frac{h_0^2}{c}.
 \tag{12}
\end{aligned}
\]

For each discrete \((r,p,s)\), (12) is only a two-variable elementary
inequality in

\[
 q\le\mu<q+1,qquad A_0\text{ satisfying (10)--(11)}.
\]

This is the cleanest rigorous starting point found in this round for an
eventual global interval exhaustion.  A coarse natural-interval use of
(12) is not yet sharp enough to prove the small positive margin near
(r=3/2); correlations in the exact wall equation still matter there.

## 6. What the Arb verifier now proves

The script

`scripts/general_d_first_shelf_wall_verify.py`

now performs two independent directed-rounding checks at 384-bit
precision.

1. As before, it proves that the stronger true-interface certificate is
   positive on all (2560) wall boxes covering the ten listed chambers.
2. It now also proves that every listed chamber contains a rational
   \(\mu\)-slice whose rigorously isolated (generally transcendental) wall
   point has strictly negative weakened certificate (2).

The negative witnesses are:

| ((n,p,r)) | (alpha=\mu-q) | certified (W), midpoint display |
|---|---:|---:|
| ((4,3,1/2)) | (67/256) | (-0.053585357) |
| ((5,4,1/2)) | (41/128) | (-0.145906535) |
| ((5,4,1)) | (85/256) | (-0.059114477) |
| ((6,5,1/2)) | (101/256) | (-0.173827216) |
| ((6,5,1)) | (105/256) | (-0.075985346) |
| ((7,6,1/2)) | (63/128) | (-0.147883846) |
| ((7,6,1)) | (131/256) | (-0.040566792) |
| ((8,6,1/2)) | (0) | (-0.023315996) |
| ((8,7,1/2)) | (79/128) | (-0.077536333) |
| ((9,7,1/2)) | (0) | (-0.015674695) |

The signs, not the displayed decimals, are the certified assertions.
Thus none of the ten chambers is a sampling artifact.

## 7. Remaining gap

A broad independent wall scan again found exactly the same ten chambers.
In the reindexing (4), every sampled failure had

\[
 r\in\{1/2,1\},\qquad s\in\{0,1\},\qquad x<8.
\]

The smallest sampled positive margin in the proposed exclusion
(r\ge3/2) was only about (0.003) under continuous relaxation (about
(0.007) on the half-grid), so a loose analytic estimate cannot safely
certify it.  The following statements therefore remain diagnostic and are
**not** used as theorems:

\[
 r\ge\frac32\Longrightarrow W\ge0,
 \qquad s\ge2\Longrightarrow W\ge0,
 \qquad
 \begin{cases}
 r=1/2,\ x\ge17/2,\\
 r=1,\ x\ge8
 \end{cases}
 \Longrightarrow W\ge0.
\]

Proving these four wall inequalities, preferably with an Arb
branch-and-bound that retains the exact implicit wall rather than the
relaxation (12), would make the ten-chamber manifest exhaustive.  Until
then the correct claim is:

> the ten chambers are rigorously genuine and rigorously closed by the
> stronger certificate, but their global exhaustiveness is still open.
