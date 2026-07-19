# Independent audit: finite first-floor wall exhaustion

Date: 18 July 2026  
Audited note: **human/outbox/general-d-round-05-first-floor-finite.md**  
Audited verifier: **scripts/general_d_first_floor_finite_verify.py**  
Verdict: **PASS**

Final audited SHA-256 digests are

~~~text
4976229FE3FFFE5892C477BAE5450C7CC8BC704B69031F26CD77225D9D4537A5  human/outbox/general-d-round-05-first-floor-finite.md
9F7C35279FD1E3FC47BF53C26A7D8681527703FE092BC3AA0831BD160609598D  scripts/general_d_first_floor_finite_verify.py
~~~

During the audit I patched the note, but not the verifier.  The patch repaired
two hidden control-character typos in \(\rho\) and \(\theta\), stated explicitly
that \(\alpha=1\) is a closed chamber endpoint, and inserted the fixed-\(\mu\)
argument showing that the post-crossing wall really is the minimum throughout
the chamber.  These changes make the note self-contained; they do not alter
the certificate or any computed result.  Both audited files contain no
forbidden control characters, and the verifier passes **py_compile**.

## 1. Independent derivation of the true-interface certificate

Let

\[
 A(z)=G_K(z)-G_\mu(z),\qquad
 x=r+p,\qquad q=r+n=x+s+1,\qquad \mu=q+\alpha .
\]

On the inner interval \(z<\mu\),

\[
 A'(z)=\frac{\arccos(z/\mu)-\arccos(z/K)}{\pi}<0
\]

and

\[
 A''(z)
 =\frac1{\pi\sqrt{K^2-z^2}}
  -\frac1{\pi\sqrt{\mu^2-z^2}}<0.
\]

Thus, conditional on the ordinary first-floor chamber, the samples
\(r,\ldots,x\) are the only nonzero strict samples.  The right-hand
post-crossing count is \(1+2p\); at equality \(A(x)=3/4\), the strict
bracket can only reduce this count.  Concavity and the chord inequality on
the consecutive intervals \([r,x]\), \([x,q]\), and \([q,\mu]\) give

\[
 2\int_r^\mu A
 \ge p(a+b)+(n-p)(b+u)+\alpha(u+h),
\]

where \(a=A(r)\), \(b=A(x)\), \(u=A(q)\), and \(h=G_K(\mu)\).

On \([\mu,K]\), \(G_K\) is decreasing and convex, with value \(h\) and
slope \(-c\) at \(\mu\), where

\[
 c=\frac{\arccos(\mu/K)}{\pi}>0.
\]

The positive part of its tangent has width \(h/c\).  Convexity and
\(G_K(K)=0\) imply \(h/c\le K-\mu\), so this whole tangent triangle lies
inside the outer interval.  Therefore

\[
 2\int_\mu^K G_K\ge\frac{h^2}{c}.
\]

Combining the inner and outer estimates yields the claimed wall-safe
certificate

\[
 \mathcal C=
 p(a+b)+(n-p)(b+u)+\alpha(u+h)+\frac{h^2}{c}-(1+2p).
\]

This derivation is valid throughout the actual ordinary first-floor branch.
The verifier checks a larger collection of walls without imposing the upper
first-floor condition \(A(r)<7/4\); proving positivity on this enlarged set
is conservative.

For fixed \(\mu\), every sampled action in \(\mathcal C\) increases with
\(K\).  The only coupled term also increases: with
\(\theta=\arccos(\mu/K)\),

\[
 \frac{h^2}{c}
 =\frac{\mu^2}{\pi}
  \frac{(\tan\theta-\theta)^2}{\theta},
\]

and

\[
 \tan\theta-\theta=\int_0^\theta\tan^2v\,dv
 <\theta\tan^2\theta
\]

makes its derivative strictly positive.  Hence the minimum in a fixed
first-floor chamber is the right-hand limit at its unique lower wall
\(A(x)=3/4\), exactly the wall used by the verifier.

## 2. Implicit wall and correlated monotonicities

For fixed \(x\), the wall equation is

\[
 \Psi(K,\mu)
 :=\frac1\pi\int_\mu^K
       \sqrt{1-\frac{x^2}{R^2}}\,dR-\frac34=0.
\]

At \(K=\mu\), \(\Psi=-3/4\); it tends to \(+\infty\) with \(K\), and its
\(K\)-derivative is positive.  The root \(K(\mu)>\mu\) therefore exists and
is unique.  Implicit differentiation gives

\[
 K'(\mu)=\frac{f_x(\mu)}{f_x(K)}\in(0,1),
 \qquad f_z(R)=\sqrt{1-\frac{z^2}{R^2}}.
\]

For fixed \(z\),

\[
 \frac d{d\mu}A(z)
 =\frac{f_x(\mu)}{\pi}
  \left(\frac{f_z(K)}{f_x(K)}
       -\frac{f_z(\mu)}{f_x(\mu)}\right).
\]

Moreover,

\[
 \left(\frac{f_z(R)}{f_x(R)}\right)^2
 =\frac{R^2-z^2}{R^2-x^2},
\]

whose derivative with respect to \(R^2\) has the sign of \(z^2-x^2\).
Since \(r\le x<q\), this proves that \(A(r)\) is nonincreasing (constant
only for \(p=0\)) and \(A(q)\) is strictly increasing along the wall.

Writing \(\rho=\mu/K\), the inequalities \(K'<1\) and \(\mu<K\) give

\[
 \rho'=\frac{K-\mu K'}{K^2}>0.
\]

Thus \(c=\arccos(\rho)/\pi\) is strictly decreasing.  Finally, with
\(a_0=x/\mu<1\) and \(\theta=\arccos\rho\),

\[
 \pi h'
 =\sqrt{1-\rho^2}
   \frac{\sqrt{1-a_0^2}}{\sqrt{1-a_0^2\rho^2}}
   -\theta
 <\sin\theta-\theta<0.
\]

So the four wall directions used by the code are all correct:
\(a\) down, \(u\) up, \(h\) down, and \(c\) down.

## 3. Audit of the panel lower bound

On an exact panel \(\alpha_0\le\alpha\le\alpha_1\), let
\(K_i^-<K(\mu_i)<K_i^+\), where \(\mu_i=q+\alpha_i\).  The code uses

\[
\begin{aligned}
 a_-&=G_{K_1^-}(r)-G_{\mu_1}(r),\\
 u_-&=G_{K_0^-}(q)-G_{\mu_0}(q),\\
 h_-&=G_{K_1^-}(\mu_1),\\
 c_+&=\pi^{-1}\arccos(\mu_0/K_0^+).
\end{aligned}
\]

The preceding monotonicities and monotonicity in \(K\) prove

\[
 a_-\le a,\qquad u_-\le u,\qquad h_-\le h,\qquad c_+\ge c.
\]

All quantities are positive, and \(\alpha\ge\alpha_0\), so

\[
 \mathcal C\ge
 p(a_-+3/4)+(n-p)(3/4+u_-)
 +\alpha_0(u_-+h_-)+\frac{h_-^2}{c_+}-(1+2p).
\]

This verifies the correlated endpoint construction.  In the implementation,
the symbols on the right are Arb balls enclosing these exact proxy values.
The decision **value > 0** is made only when the complete Arb interval has
strictly positive lower endpoint, so interval overhang cannot invalidate
the inequality.

Every wall bracket is obtained with exact **fmpq** bisection.  Strict Arb
signs at its two rational endpoints, together with uniqueness of the wall,
prove \(K^-<K(\mu)<K^+\).  Any undecidable sign raises an exception rather
than being guessed.

## 4. Exact discrete coverage and endpoint conventions

The loop is exactly

\[
 r=\frac m2,\quad 3\le m\le199,\qquad
 p\ge0,\quad r+p<100,\qquad s\in\{0,1\}.
\]

For each \(s\), the half-integral starts give

\[
 99+98+\cdots+1=4950
\]

chambers and the integral starts give

\[
 98+97+\cdots+1=4851.
\]

Thus there are \(9801\) chambers per \(s\) and exactly \(19602\) in all.
No half-grid start or admissible \(p\) is omitted.

For an actual chamber, \(\alpha=\mu-q\) lies in \([0,1)\).  Checking the
closed interval \([0,1]\) is conservative.  The endpoint \(\alpha=1\) is
the same geometric limiting interface as \(\alpha=0\) in the adjacent
\(n\)-chamber; the displayed integral decomposition and the count
\(1+2p\) remain valid there.  At \(\alpha=0\), \(q=\mu\) and the
\([q,\mu]\) term vanishes exactly.  Both endpoints are therefore covered
without a convention gap.

At \(A(x)=3/4\), the verifier deliberately pays the right-hand
post-crossing count \(1+2p\).  Since the spectral bracket is strict, its
exact wall count is no larger.  Thus inserting \(b=3/4\) and using the
post-crossing payment is wall-safe.

## 5. Independent executions

The published verifier was replayed from a clean process at 384 and
512 bits, with 110 rational bisections per endpoint.  A stronger stress
execution imported the same unchanged verifier, set **ROOT_STEPS=160**, and
ran all chambers at 768 bits.  All three runs completed with exit code zero.

| precision | root steps | chambers | panels | leaves | roots | max depth |
|---:|---:|---:|---:|---:|---:|---:|
| 384 | 110 | 19602 | 19610 | 19606 | 39208 | 1 |
| 512 | 110 | 19602 | 19610 | 19606 | 39208 | 1 |
| 768 | 160 | 19602 | 19610 | 19606 | 39208 | 1 |

The 768-bit stress run independently identified the only subdivided
chambers as

~~~text
(r,p,s)=(3/2,4,0)
(r,p,s)=(3/2,5,0)
(r,p,s)=(3/2,6,0)
(r,p,s)=(3/2,7,0)
~~~

Each uses exactly the two leaves \([0,1/2]\) and \([1/2,1]\); every other
chamber is accepted on \([0,1]\).  The smallest displayed midpoint in
all runs is

~~~text
0.0043062680449249...
~~~

This decimal is not used as evidence.  The evidence is the strict positive
lower endpoint of every directed-rounding Arb result.

## 6. Verdict and scope

**PASS.**  The analytic reduction, endpoint monotonicities, exact chamber
enumeration, strict-wall convention, and Arb implementation are sound.  The
certificate proves the complete finite sector

\[
 r\ge\frac32,\qquad s\in\{0,1\},\qquad r+p<100.
\]

Combined with the separately audited large-ray certificate, it closes
\(r\ge3/2\), \(s\in\{0,1\}\).  It does not prove the \(s\ge2\) cone or the
small starts \(r=1/2,1\).
