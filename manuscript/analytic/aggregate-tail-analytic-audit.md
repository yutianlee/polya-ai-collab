# Clean-room audit of `aggregate-tail-analytic.tex`

Date: 2026-07-16  
Audited source SHA-256: `B59D673E117611C81BABE4F8D7FE34AD0AFDFEF84BF2D8424128DE606F9C0BC9`  
Verdict: **PASS**

I froze the source at the digest above and reconstructed the aggregate-tail
argument independently. I checked its definitions against the main discrete
aggregate lemma and against the three already audited analytic base notes,
derived every displayed derivative, replayed every validity and curvature
inequality, and treated separately all floor and endpoint cases. No missing
factor, reversed inequality, integer-boundary error, or unreported numerical
dependency was found.

The theorem is purely analytic in the stated sense. Its only imported local
facts are the three hand-proved base inequalities, and its remaining imported
ingredient is the analytic discrete layer-cake implication from the main
paper. No aggregate interval certificate is used.

## 1. Frozen inputs and definition compatibility

The local analytic inputs used by the source are:

| source | SHA-256 | imported conclusion |
|---|---|---|
| `B-positive.tex` | `70222FE3523B3F71384ADF22E2751BE1390498AE6554A8875984330DCBF67808` | \(\mathcal B(\rho,200)>60\) |
| `BK-positive.tex` | `F303CD9659789391DAABDF2821B16DE99B04BA47D767996B8ECCFCAA9F4D6F03` | \(\mathcal B_K(\rho,200)>0\) |
| `F-positive.tex` | `D2305C221D89D2275A11B02F590A15FCA36EBE78AAD98DDBF5334FF41BDA064A` | \(F(\rho)>1549/84150\) |

Their clean-room audit files all record PASS. I also compared the definitions,
not merely the theorem names:

\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 d_\rho=\frac{2\arcsin\rho}{\pi},\qquad
 b_\rho=\frac{2\pi\rho}{1-\rho}
\]

are identical in all four notes. At \(K=200\), the aggregate source has

\[
 b_\rho K=\frac{400\pi\rho}{1-\rho},\quad
 \mu=200\rho,\quad \overline R=200\rho+\frac12,
\]

which are exactly the constants denoted by \(c,\mu,\overline R\) in
`B-positive.tex`. Its \(\overline{\mathcal I}\) and \(\mathcal B\) formulas
therefore specialize term for term to that audited base lemma. The derivative
formula used by `BK-positive.tex` and the function \(F\) used by
`F-positive.tex` are likewise identical to the definitions in the aggregate
source. There is no normalization or scaling mismatch at an import boundary.

## 2. Match with the main discrete aggregate lemma

The main paper defines

\[
 C=\frac{2\pi\rho K}{1-\rho}=b_\rho K,
\]

and uses exactly the same decomposition

\[
 \mu-\frac12=J+\tau,\qquad
 R=\begin{cases}J,&\tau=0,\\J+1,&0<\tau<1.\end{cases}
\]

Its discrete reserve is exactly

\[
 \mathcal Q
 =R\lfloor K\eta_\rho\rfloor
 +d_\rho\frac{J(J+1)}2
 -(1+d_\rho)\mathcal I(C,R)
 -\frac{8R\tau^{5/2}}{15\sqrt\mu},
\]

and its conclusion is exactly

\[
 \mathcal Q\ge0\Longrightarrow
 N_D(A_{\rho,1},K^2)<\frac{2(1-\rho^3)K^3}{9\pi}.
\]

Thus the aggregate note invokes the same strict counting convention and not
a nearby ordinary-floor variant.

For completeness, the integer arithmetic behind the main lemma checks in
both cases. With \(x_r=r+1/2\):

- if \(\tau=0\), then \(R=J\),
  \(\lfloor\mu-x_r\rfloor=J-r\) for \(0\le r<J\), and the sum is
  \(J+(J-1)+\cdots+1=J(J+1)/2\);
- if \(0<\tau<1\), then \(R=J+1\), the same formula holds for
  \(0\le r\le J\), and the additional last term is zero.

In both cases

\[
 q_r=x_r+\lfloor\mu-x_r\rfloor=J+\frac12,qquad
 \mu-q_r=\tau.
\]

At \(\tau=0\), the main lemma's interface remainder is exactly zero, and
the first tail on the convex side begins at \(x_R=\mu\). Hence the
half-integer \(\mu\) interface is neither omitted nor counted twice.

The shelf function

\[
 f_C(x)=\sqrt{x^2+C}-x
\]

is positive and strictly convex because

\[
 f_C''(x)=\frac{C}{(x^2+C)^{3/2}}>0.
\]

Thus its midpoint sum is bounded by its integral, while the accepted-shelf
inequality is itself strict. The multiplicity identity in the main proof is
also exact:

\[
 \sum_{r\ge0}\left(h_r+2\sum_{\ell>r}h_\ell\right)
 =\sum_{\ell\ge0}(2\ell+1)h_\ell.
\]

These observations confirm the stated strict implication, including
\(\tau=0\), half-integer \(\mu\), and integer proxy walls. The source does
not import any finite certificate through this lemma.

## 3. Continuous-to-discrete comparison, including all boundary cases

Let

\[
 x=\mu-\frac12=J+\tau>1,qquad y=K\eta_\rho>1.
\]

First, \(R\ge x\), with equality only when \(\tau=0\). For every real
\(y\), including every integer,

\[
 \lfloor y\rfloor>y-1.
\]

Because \(R\ge1\) and \(y-1>0\), this gives

\[
 R\lfloor y\rfloor>R(y-1)\ge x(y-1).
\]

There is no loss of strictness when \(y\in\mathbb Z\): then the first
comparison reads \(Ry>R(y-1)\).

For the quadratic term, \(u\mapsto u(u-1)\) is strictly increasing for
\(u>1\). If \(0<\tau<1\), then

\[
 x(x-1)< (J+1)J=J(J+1).
\]

If \(\tau=0\), then \(x=J\) and

\[
 J(J+1)-x(x-1)=2J>0.
\]

Since \(d_\rho>0\), the strict quadratic comparison in the source is valid
in both cases.

The integral identity

\[
 \mathcal I(C,R)=\int_0^R\bigl(\sqrt{u^2+C}-u\bigr)\,du
\]

follows from its displayed elementary antiderivative. The integrand is
strictly positive for \(C>0\). Moreover,

\[
 \overline R=\mu+\frac12=J+\tau+1>R
\]

for \(\tau=0\) and for \(\tau>0\), so

\[
 \mathcal I(C,R)<\mathcal I(C,\overline R)
 =\overline{\mathcal I}.
\]

Finally, if \(\tau=0\), then \(R\tau^{5/2}=0<\overline R\). If
\(0<\tau<1\), then

\[
 R\tau^{5/2}<R<\overline R.
\]

The coefficients \(d_\rho\), \(1+d_\rho\), and \(1/\sqrt\mu\) have the
needed positive signs. Substitution therefore gives, with all negative-term
directions reversed correctly,

\[
 \mathcal Q(\rho,K)>\mathcal B(\rho,K).
\]

This is stronger than the nonnegative hypothesis required by the main
discrete implication.

## 4. Independent derivation of the derivative identities

Fix \(\rho\), and abbreviate

\[
 U=\overline R=\rho K+\frac12,qquad
 C=b_\rho K,qquad
 S=\sqrt{U^2+C},\qquad P=S-U.
\]

The integral form

\[
 I(K)=\int_0^U(\sqrt{x^2+b_\rho K}-x)\,dx
\]

and Leibniz' rule give

\[
 I_K=\rho(S-U)+\frac{b_\rho}{2}
 \int_0^U\frac{dx}{\sqrt{x^2+b_\rho K}}
 =\rho P+\frac{b_\rho}{2}
 \operatorname{arsinh}\frac{U}{\sqrt{b_\rho K}}.
\]

Independently,

\[
 P_K=\rho\left(\frac US-1\right)+\frac{b_\rho}{2S}
\]

and

\[
 \frac{d}{dK}\operatorname{arsinh}
 \frac{U}{\sqrt{b_\rho K}}
 =\frac{2\rho K-1}{4KS}.
\]

Therefore

\[
 I_{KK}=\rho^2\left(\frac US-1\right)
 +\frac{\rho b_\rho}{2S}
 +\frac{b_\rho(2\rho K-1)}{8KS},
\]

exactly as printed.

Differentiating the other three pieces of \(\mathcal B\) gives

\[
\begin{aligned}
 \partial_K[(\mu-\tfrac12)(K\eta_\rho-1)]
 &=\rho(K\eta_\rho-1)+(\mu-\tfrac12)\eta_\rho,\\
 \partial_K\!\left[\frac{d_\rho}{2}
 (\mu-\tfrac32)(\mu-\tfrac12)\right]
 &=d_\rho\rho(\mu-1),\\
 \partial_K\!\left[-\frac{8(\mu+1/2)}{15\sqrt\mu}\right]
 &=-\frac{2\rho(2\mu-1)}{15\mu^{3/2}}.
\end{aligned}
\]

One further differentiation of the last line is

\[
 \frac{\rho^2(2\mu-3)}{15\mu^{5/2}}.
\]

Combining these identities reproduces both displayed formulas for
\(\mathcal B_K\) and \(\mathcal B_{KK}\). Also, direct differentiation of

\[
 G_1(s)=\frac{\sqrt{1-s^2}-s\arccos s}{\pi}
\]

gives \(G_1'(s)=-\arccos(s)/\pi\), so the monotonicity used later is valid.

## 5. Validity conditions on the full closed rational interval

For \(7/51\le\rho\le39/50\) and \(K\ge200\),

\[
 \mu=\rho K\ge\frac{1400}{51}
 =\frac32+\frac{2647}{102}>\frac32.
\]

Since \(\max\{\rho,1/2\}\le39/50\) and \(G_1\) is decreasing,

\[
 \eta_\rho\ge G_1(39/50).
\]

The elementary estimate

\[
 G_1(s)\ge\frac{2\sqrt2}{3\pi}(1-s)^{3/2}
\]

and \(\pi<22/7\) imply

\[
 200\eta_\rho>
 \frac{1400\sqrt2}{33}\left(\frac{11}{50}\right)^{3/2}.
\]

The exact square of the final positive quantity is

\[
 \left[\frac{1400\sqrt2}{33}
 \left(\frac{11}{50}\right)^{3/2}\right]^2
 =\frac{8624}{225}>1.
\]

Hence \(K\eta_\rho\ge200\eta_\rho>1\). The strict inequality remains
valid at both ratio endpoints; at \(\rho=39/50\), only the monotonicity
step becomes equality, while the rational lower estimate remains strict.

All square roots, inverse hyperbolic functions, and denominators in the
source are consequently valid. In particular,

\[
 S>\overline R>\rho K>0.
\]

## 6. Curvature estimate

In the exact formula for \(I_{KK}\), the first term is strictly negative
because \(0<U/S<1\). The other terms satisfy

\[
\begin{aligned}
 \frac{\rho b_\rho}{2S}
 +\frac{b_\rho(2\rho K-1)}{8KS}
 &<\frac{\rho b_\rho}{2S}
   +\frac{2\rho Kb_\rho}{8KS}\\
 &=\frac{3\rho b_\rho}{4S}
 <\frac{3b_\rho}{4K}
 \le\frac{3b_\rho}{800}.
\end{aligned}
\]

Every denominator and multiplier is positive. The first two inequalities
are strict; thus the conclusion remains strict at \(K=200\), where the last
comparison is equality. Also \(2\mu-3>0\), so the error curvature

\[
 E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}
\]

is strictly positive. Since \(1+d_\rho>0\), substitution has the correct
direction:

\[
 \mathcal B_{KK}
 >2\rho\eta_\rho+d_\rho\rho^2
 -\frac{3(1+d_\rho)b_\rho}{800}
 =F(\rho).
\]

The independently audited local theorem supplies

\[
 F(\rho)>\frac{1549}{84150}>0
\]

on the entire closed rational interval.

## 7. Integrations and endpoint ownership

For fixed \(\rho\), the displayed formulas make \(\mathcal B(\rho,K)\)
twice continuously differentiable for \(K>0\). Taylor's formula with
integral remainder is exactly

\[
 \mathcal B(\rho,K)=\mathcal B(\rho,200)
 +(K-200)\mathcal B_K(\rho,200)
 +\int_{200}^K(K-s)\mathcal B_{KK}(\rho,s)\,ds.
\]

For \(K>200\), the two audited strict base inequalities and the curvature
bound give

\[
 \mathcal B(\rho,K)>
 60+\frac12\frac{1549}{84150}(K-200)^2.
\]

At \(K=200\), the integral and linear terms vanish, but the independently
audited base inequality itself gives \(\mathcal B(\rho,200)>60\). Thus the
quantitative theorem includes its frequency endpoint without pretending to
integrate a strict inequality over an interval of zero length.

The three imported base results include \(\rho=7/51\), \(\rho=39/50\),
and both sides of the formula interface \(\rho=1/2\). Their definitions of
\(\eta_\rho\) agree at the interface, so there is no ratio gap or overlap
ambiguity.

## 8. The exact lower endpoint \(\rho_c\)

The strict elementary bound \(\pi<22/7\) gives

\[
 1+2\pi<\frac{51}{7},qquad
 \rho_c=\frac1{1+2\pi}>\frac7{51}.
\]

Positivity permits reciprocation with the stated direction. The elementary
bound \(\pi>3\) also gives

\[
 \rho_c<\frac17<\frac{39}{50},
 \qquad
 \frac{39}{50}-\frac17=\frac{223}{350}>0.
\]

Hence the complete closed interval
\([\rho_c,39/50]\) lies inside the rational superset. In particular the
endpoint \(\rho=\rho_c\) itself is covered, because it is strictly interior
to the lower rational bound, while \(\rho=39/50\) is owned by the closed
base interval.

On this domain the continuous reserve is strictly positive, so the
continuous-to-discrete lemma gives \(\mathcal Q>0\), and the main analytic
implication applies. This proves the strict Pólya inequality at every stated
ratio and frequency endpoint.

## 9. Verdict and dependency boundary

All derivative identities, validity conditions, integer-floor cases,
curvature estimates, integrations, and endpoint inclusions pass. The only
external mathematical inputs are precisely those declared by the source:

1. the three independently audited analytic base inequalities; and
2. the main paper's analytic discrete aggregate implication.

Neither input depends on the aggregate interval certificate. The source is
therefore a correct purely analytic replacement for that certificate.

## 10. Compilation

After writing the mathematical verdict, I compiled the frozen source with
the bundled Tectonic 0.16.9 workflow. The cross-reference rerun completed
successfully, the final pass had no unresolved reference or LaTeX error, and
the result is a five-page PDF.

Compiled PDF: `manuscript/analytic/aggregate-tail-analytic.pdf`  
PDF SHA-256: `99550843A60CACF376113B50608BF6FB4F0AF1D487B3574B19826018447D7CF4`
