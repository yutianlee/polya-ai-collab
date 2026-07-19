# General dimension, Round 17: independent audit of the action-face quantile reduction

Date: 19 July 2026

Verdict: **PASS**.  Every load-bearing identity, strict-face lemma, and wall-closure statement checks out.  At the simultaneous radial/action wall, the paired angles correctly become equal at the upper endpoint while the downstream derivative conclusions remain strict.  The endpoint scalar \(\mathcal S>0\) in (5.2), and hence the action-face derivative on the full boundary, remains unproved exactly as stated in the audited note.

## Frozen artifacts

- Audited note: human/outbox/general-d-round-17-action-face-quantile-reduction.md
- Audited-note SHA-256: ae546dc4929d806b54c02623a0e69d16e84c271361949efc3fa85b37a6d776e6
- Replayed evaluator: computations/general_d_round17_action_face_quantile_probe.wl
- Evaluator SHA-256: e5e99410b16df2e8a28ab64ba88f015c15de75c97d0f984c318a138f8db9855e

The audited note and evaluator were not edited during this audit.

## Domain and exact quantile primitive

On the strict action face,

\[
A(0)=\frac{K-a}{\pi}>1,\qquad A(x)=1,\qquad
A(t)=\frac34,\qquad t=a-1<a.
\]

Since \(A\) is strictly decreasing, \(0<x<t<a\).  Thus \(g=G_a(x)>0\), all angles used in the note lie in \((0,\pi/2)\), and the level ranges \(0\le c\le g\) and \(1\le c+1\le g+1\) lie inside the respective quantile domains.

For \(\beta=\arccos(s/b)\), direct differentiation under the integral gives

\[
P_b(s)=\frac1\pi\int_s^b\sqrt{1-\frac{u^2}{b^2}}\,du
       =\frac b\pi\int_0^\beta\sin^2\tau\,d\tau.
\]

The substitution \(c=bh(\tau)/\pi\), with
\(dc=b\tau\sin\tau\,d\tau/\pi\), converts the last integrand to
\(U_b(c)\,dc\).  Lemma 2.1,

\[
P_b(s)=\int_0^{G_b(s)}U_b(c)\,dc,
\]

is therefore exact, including the continuous value \(U_b(0)=1\).

## Derivative split and positive reserve

The identity \(A(x)=1\) gives \(G_K(x)=g+1\), while
\(G_K(z)=3/4\) gives \(U_K(3/4)=\sin\theta/\theta\).  Substitution into
the action-face derivative produces exactly

\[
\frac{dF}{da}
=K'B_K+\int_0^gQ(c)\,dc,
\]

with

\[
B_K=\int_0^1U_K(c)\,dc-U_K(3/4),\qquad
Q(c)=K'U_K(c+1)-U_a(c).
\]

No term or scale factor is missing.  The domain contains \([0,1]\) because
\(K>a+\pi>\pi\).  Strict convexity and decrease of \(U_K\) give

\[
\int_0^1U_K(c)\,dc>U_K(1/2)>U_K(3/4),
\]

so \(B_K>0\).  Also \(K'>0\), because
\(\gamma+\sin\phi-\phi=(\gamma-\phi)+\sin\phi>0\).

## Boundary speed

Writing \(t=a\cos\phi=K\cos\gamma\) converts the action wall to

\[
(\tan\gamma-\gamma)-(\tan\phi-\phi)=\frac{3\pi}{4t}.
\]

Combining this with \(t=a-1\), hence \(a(1-\cos\phi)=1\), gives

\[
\frac Ka-K'
=\frac{3\pi/4-\gamma+\phi}{a\sin\gamma}.
\]

The numerator exceeds \(\pi/4\), because
\(0<\gamma-\phi<\pi/2\).  Consequently \(0<K'<K/a\) and
\(K'/K<1/a\), exactly as required later.

## Paired-angle ordering and \(Q'>0\)

Let \(\delta(c)=\beta(c)-\psi(c)\).  On the strict face,
\(\delta(0)>0\) and \(\delta(g)>0\).  At any hypothetical interior zero,

\[
\delta'(c)=
\frac{\pi}{\beta\sin\beta}\left(\frac1K-\frac1a\right)<0.
\]

Every zero would therefore be a positive-to-negative crossing.  A function
starting and ending positive cannot have such a zero without a later
negative-to-positive crossing, which the same derivative formula excludes.
Lemma 4.1 is valid on the strict face.

For

\[
V(\tau)=\frac{h(\tau)}{\tau^3\sin\tau},
\qquad
R(\tau)=3\sin^2\tau-\tau\sin(2\tau)-\tau^2,
\]

direct differentiation gives

\[
V'(\tau)=-\frac{R(\tau)}{\tau^4\sin^2\tau},\qquad
R'(\tau)=4\cos\tau\,h(\tau)>0.
\]

Hence \(V\) is strictly decreasing.  Together with
\(\psi<\beta\) and \(K'/K<1/a\), the exact formula

\[
Q'(c)=\pi\left\{\frac{V(\psi(c))}{a}
-\frac{K'V(\beta(c))}{K}\right\}
\]

is strictly positive.  Thus \(Q\) is strictly increasing and has at most
one zero.

## Strict concavity

Differentiating once more gives

\[
U_b''(c)=\left(\frac{\pi}{b}\right)^2W(\tau_b(c)),
\qquad
W(\tau)=\frac{R(\tau)}{\tau^5\sin^3\tau}.
\]

The note's proof that \(W\) decreases is valid.  In detail,

\[
R-\tau\cos\tau\,h
=\sin\tau\{3h-\tau^2\sin\tau\}>0,
\]

because the expression in braces has derivative \(\tau h>0\).  Multiplying
this bound by \(5\sin\tau+3\tau\cos\tau>4\sin\tau\) proves the exact
numerator inequality equivalent to \(W'<0\).

With \(s=K/a>1\) and \(k=K'\), the boundary-speed result gives
\(0<k<s<s^2\), while paired-angle ordering gives
\(W(\beta)<W(\psi)\).  Therefore

\[
Q''(c)=\frac{\pi^2}{a^2}
\left\{\frac{k}{s^2}W(\beta(c))-W(\psi(c))\right\}<0
\quad(0<c<g).
\]

Lemma 4.2 is correct.

## Positivity at the upper endpoint

For \(u(\tau)=\sin\tau/\tau\), direct differentiation verifies

\[
\frac d{ds}\log\frac{u(\phi_s)}{u(\gamma_s)}
=\frac{L(\phi_s)-L(\gamma_s)}s,\qquad
L(\tau)=\frac{\cot\tau}{\tau}-\cot^2\tau.
\]

After multiplication by positive factors, \(L'<0\) is equivalent to

\[
\tau\tan\tau+\sin^2\tau-2\tau^2>0.
\]

The estimates
\(\tan\tau>\tau+\tau^3/3\) and
\(\sin\tau>\tau-\tau^3/6\) imply
\(\tau\tan\tau-\tau^2>\tau^4/3>
\tau^2-\sin^2\tau\), so this sign proof is sound.

Because \(x<t\), the ratio \(u(\phi_s)/u(\gamma_s)\) at \(s=x\) is
strictly smaller than at \(s=t\).  Formula (1.2) gives

\[
K'u(\gamma)
=1-\frac{\phi-\sin\phi}{\gamma}
>1-\frac{\phi-\sin\phi}{\phi}
=u(\phi).
\]

It follows that \(K'u(\beta(g))>u(\psi(g))\), namely \(Q(g)>0\).
Lemma 4.3 is correct.

## Simultaneous-wall qualification

At \(K-a=\pi\), one has \(A(0)=1\), so the critical point is \(x=0\).
Consequently

\[
g=\frac a\pi,\qquad
\beta(g)=\psi(g)=\frac\pi2.
\]

Thus the boxed strict inequality in Lemma 4.1 does not literally extend to
the upper endpoint of the closed wall; it extends as
\(\beta(c)>\psi(c)\) for \(c<g\) and equality at \(g\).  This is
nonblocking:

- \(Q'(g)>0\) still follows from \(K'/K<1/a\);
- Lemma 4.2 only asserts \(Q''<0\) on \(0<c<g\);
- \(Q(g)>0\) follows directly, because both endpoint sinc factors equal
  \(2/\pi\) and
  \[
  K'-1=
  \frac{(\gamma-\sin\gamma)-(\phi-\sin\phi)}{\sin\gamma}>0.
  \]

The audited note states this weak-endpoint closure explicitly and separately
checks \(K'>1\) for \(Q(g)>0\).  No later estimate loses strictness.

## Exact remaining payment

Strict concavity puts \(Q\) above its endpoint chord and yields

\[
\int_0^gQ(c)\,dc\ge\frac g2\{Q(0)+Q(g)\}.
\]

Substitution gives exactly the scalar \(\mathcal S\) in (5.2).  Proving
\(\mathcal S>0\) is sufficient for \(dF/da>0\), but the audited note does
not claim that proof.  In the subcase \(Q(0)<0<Q(g)\), strict monotonicity
makes \(c_-\) the unique zero; (5.3) is another sufficient payment obtained
by discarding only the positive tail.

Finally, the level equations with \(\lambda=K/a\) give
\(U_a(c)=U_K(\lambda c)\).  Changing variables in the inner integral
reproduces the exact one-radius identity (5.5), including its factor
\(1/\lambda\).

## Diagnostic replay

Wolfram Language 15.0 replay completed with exit code zero and printed
“round17ReplayOK=True”.  The evaluator sampled eight action-face points
from just above the simultaneous wall through \(a=100000\).  All sampled
records had

- \(K/a-K'>0\), \(B_K>0\), \(Q(g)>0\);
- positive exact derivative and positive chord scalar;
- zero high-precision residuals for the speed identity and derivative
  decomposition;
- positive sampled first differences of \(Q\) and negative sampled second
  differences.

At \(a=100000\), the smallest sampled derivative was
\(7.4975645679\times10^{-5}\), and the sampled chord scalar was
\(7.3562040071\times10^{-5}\).  An independent high-precision evaluation
at \(a=a_{\rm wall}+10^{-6}\) gives the corrected near-wall chord scalar
\(0.0854247133555196\ldots\), agreeing with the frozen note and evaluator.
These are correctly presented as
floating-point theorem-design evidence.  The finite-difference checks and
the eight-point sample are neither interval enclosures nor coverage proofs.

## Boundary of the PASS

This audit certifies Lemma 2.1, the exact derivative split, the
boundary-speed identity, paired-angle no-crossing argument, monotonicity and
concavity of \(Q\), upper-endpoint positivity, the exact one-radius form,
and the corrected weak interpretation at the simultaneous wall.  It does
**not** prove \(\mathcal S>0\), prove (5.3), certify the remaining
transcendental two-wall value, close the first-floor branch, close the
high-floor CST, or prove the all-dimensional theorem.
