# General dimension, Round 5: finite first-floor wall exhaustion

Date: 18 July 2026  
Scope: the ordinary first-floor branch (F_0=1, p<n), on the wall
(A(r+p)=3/4), in the finite sector

\[
 r\ge \frac32,\qquad s=n-p-1\in\{0,1\},\qquad x=r+p<100.
\]

Status: **proved** by a 384-bit directed-rounding Arb certificate and
replayed independently at 512 bits.  Together with the already certified
large ray (x\ge100), this closes the whole sector
(r\ge3/2, s\in\{0,1\}).  It does not address (s\ge2) or the two
small starts (r=1/2,1).

The verifier is

`scripts/general_d_first_floor_finite_verify.py`.

Its SHA-256 digest is

`9F7C35279FD1E3FC47BF53C26A7D8681527703FE092BC3AA0831BD160609598D`.

## 1. The stronger true-interface certificate

Write

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}\pi,
 \qquad A=G_K-G_\mu,
\]

and put

\[
 x=r+p,\qquad q=r+n=x+s+1,
 \qquad \mu=q+\alpha,\qquad 0\le\alpha\le1.
\]

For an actual chamber one has \(0\le\alpha<1\).  The endpoint
\(\alpha=1\) is included as a closed chamber limit; the same integral
decomposition and count bound remain valid there.

At the wall define

\[
 a=A(r),\qquad b=A(x)=\frac34,\qquad
 u=A(q),\qquad h=G_K(\mu),\qquad
 c=\frac1\pi\arccos\frac\mu K.
\]

In an actual ordinary first-floor chamber, the samples from (r) through
(x) have floor one and the sample at (x+1) has floor zero.  Since (A)
is strictly decreasing, every later sample also has floor zero.  Thus the
post-crossing wall limit of the complete strict tail count is (1+2p).
At the wall itself the strict bracket can only be smaller, so the
post-crossing value is the wall-safe one to estimate.

On the inner side,

\[
 A''(z)=\frac1{\pi\sqrt{K^2-z^2}}
        -\frac1{\pi\sqrt{\mu^2-z^2}}<0.
\]

The concave trapezoid inequality on the three successive intervals gives

\[
 2\int_r^x A\ge p(a+b),
\]

\[
 2\int_x^q A\ge(n-p)(b+u),
\]

and

\[
 2\int_q^\mu A\ge\alpha(u+h).
\]

On the outer side (A=G_K).  The function (G_K) is decreasing and
convex, starts at (h), and its slope at (mu) is (-c).  Its tangent
triangle therefore gives

\[
 2\int_\mu^K G_K(z)\,dz\ge\frac{h^2}{c}.
\]

Consequently the true tail defect is bounded below by

\[
 \boxed{
 \mathcal C=
 p(a+b)+(n-p)(b+u)+\alpha(u+h)+\frac{h^2}{c}-(1+2p).}
 \tag{1}
\]

For completeness, this wall is the correct minimum at fixed \(\mu\).
Before setting \(b=3/4\), every sampled action in the right side of (1)
is strictly increasing with \(K\).  The remaining outer term is increasing
as well.  Indeed, if \(\theta=\arccos(\mu/K)\), then

\[
 \frac{h^2}{c}
 =\frac{\mu^2}{\pi}\frac{(\tan\theta-\theta)^2}{\theta},
\]

and this is strictly increasing in \(\theta\), hence in \(K\), because

\[
 \tan\theta-\theta=\int_0^\theta\tan^2v\,dv
 <\theta\tan^2\theta.
\]

Thus the certificate is smallest in the post-crossing limit at
\(A(x)=3/4\).  At the wall itself the strict bracket can only decrease the
discrete count.  This is the stronger certificate used earlier on the ten
small-start chambers, and it is valid throughout the ordinary first-floor
branch; no terminal-envelope relaxation is involved.

## 2. Correlated monotonicity along the implicit wall

For fixed (x), put

\[
 f_z(R)=\sqrt{1-\frac{z^2}{R^2}}.
\]

The wall equation is

\[
 \int_\mu^{K(\mu)}f_x(R)\,dR=\frac{3\pi}{4}.
 \tag{2}
\]

It has a unique root (K(\mu)>\mu), and implicit differentiation gives

\[
 K'(\mu)=\frac{f_x(\mu)}{f_x(K)}\in(0,1).
 \tag{3}
\]

For a fixed sample (z), differentiation along the wall gives

\[
 \frac d{d\mu}A(z)
 =\frac{f_x(\mu)}\pi
 \left(\frac{f_z(K)}{f_x(K)}
       -\frac{f_z(\mu)}{f_x(\mu)}\right).
 \tag{4}
\]

Moreover,

\[
 \left(\frac{f_z(R)}{f_x(R)}\right)^2
 =\frac{R^2-z^2}{R^2-x^2},
\]

whose derivative with respect to (R^2) has the sign of (z^2-x^2).
It follows that, along the wall,

\[
 A(r)\ \hbox{is nonincreasing},
 \qquad A(q)\ \hbox{is strictly increasing}.
 \tag{5}
\]

The first assertion is an equality only when (p=0), so (r=x).

Put \(\rho=\mu/K\).  Since \(K'<1\),

\[
 \rho'=\frac{K-\mu K'}{K^2}>0,
\]

and hence

\[
 c=\frac{\arccos\rho}{\pi}
 \quad\hbox{is strictly decreasing}.
 \tag{6}
\]

Finally let \(h(\mu)=G_{K(\mu)}(\mu)\), set
\(\theta=\arccos\rho\), and write \(a_0=x/\mu<1\).  Equations (3) and the
two partial derivatives of \(G\) give

\[
 \pi h'
 =\sqrt{1-\rho^2}
   \frac{\sqrt{1-a_0^2}}{\sqrt{1-a_0^2\rho^2}}
   -\theta
 <\sin\theta-\theta<0.
 \tag{7}
\]

Thus (h) is strictly decreasing as well.

## 3. A rigorous lower bound on each alpha panel

Let (0\le\alpha_0<\alpha_1\le1), put
(mu_i=q+\alpha_i), and let

\[
 K_i^-<K(\mu_i)<K_i^+
\]

be strict rational wall brackets.  The monotonicities above give the
one-sided quantities

\[
 a_-=G_{K_1^-}(r)-G_{\mu_1}(r)\le a,
\]

\[
 u_-=G_{K_0^-}(q)-G_{\mu_0}(q)\le u,
\]

\[
 h_-=G_{K_1^-}(\mu_1)\le h,
 \qquad
 c_+=\frac1\pi\arccos\frac{\mu_0}{K_0^+}\ge c.
\]

Since all these actions are positive, (1) has the rigorous panel lower
bound

\[
 \boxed{
 \mathcal C\ge
 p\left(a_-+\frac34\right)
 +(n-p)\left(\frac34+u_-\right)
 +\alpha_0(u_-+h_-)
 +\frac{h_-^2}{c_+}-(1+2p).}
 \tag{8}
\]

This endpoint construction retains the wall correlation that a natural
four-variable interval evaluation would lose.

The verifier isolates each endpoint root by 110 steps of exact rational
bisection.  Every wall sign and every sign in (8) is evaluated with Arb
directed rounding.  Binary floating point is used only to print a
human-readable midpoint after a strict Arb sign has already been proved.

## 4. Exact half-grid coverage

The discrete enumeration is

\[
 r=\frac m2,\quad 3\le m\le199,
 \qquad p\in\mathbb Z_{\ge0},\quad r+p<100,
 \qquad s\in\{0,1\}.
\]

For each fixed (s), the half-integral starts contribute
(99+98+\cdots+1=4950) chambers and the integral starts contribute
(98+97+\cdots+1=4851), for exactly

\[
 9801\quad\hbox{chambers per }s,
 \qquad 19602\quad\hbox{chambers in total}.
\]

Every chamber is first tested on the single panel ([0,1]).  Precisely
four chambers require subdivision:

\[
 (r,s,p)=\left(\frac32,0,4\right),
 \left(\frac32,0,5\right),
 \left(\frac32,0,6\right),
 \left(\frac32,0,7\right).
\]

Each is resolved by the two panels ([0,1/2]) and ([1/2,1]).  No deeper
subdivision occurs.

At both 384-bit and 512-bit precision the exact output counts are

```text
PASS s=0
  chambers=9801, processed-panels=9809, accepted-leaves=9805,
  isolated-roots=19606, max-depth=1

PASS s=1
  chambers=9801, processed-panels=9801, accepted-leaves=9801,
  isolated-roots=19602, max-depth=0

CERTIFIED
  chambers=19602, processed-panels=19610, accepted-leaves=19606,
  isolated-roots=39208, max-depth=1
```

The smallest printed midpoint of an accepted Arb interval is
(0.00430626804492\ldots).  This decimal is diagnostic only; the proof is
the strict positive Arb lower endpoint on every accepted leaf.

Reproduction commands are

```text
python scripts/general_d_first_floor_finite_verify.py --precision 384
python scripts/general_d_first_floor_finite_verify.py --precision 512
```

## 5. Consequence and remaining first-floor sectors

The present finite certificate proves

\[
 r\ge\frac32,\qquad s\in\{0,1\},\qquad x<100.
\]

The independently audited large-ray certificate proves the complementary
range (x\ge100) under the same (r,s) hypotheses.  Hence the combined
result is

\[
 \boxed{r\ge\frac32,\quad s\in\{0,1\}
 \quad\Longrightarrow\quad
 \text{the ordinary first-floor first-drop wall is positive}.}
\]

The remaining ordinary first-floor exhaustion consists of

1. the unbounded cone (s\ge2);
2. the two small starts (r=1/2) and (r=1), outside the already
   certified ten exceptional chambers and their proved true-interface
   closures.
