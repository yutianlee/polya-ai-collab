# Independent audit: Round 5 finite no-drop reductions

Date: 18 July 2026

Verdict:

\[
 \boxed{\text{PASS after three local expository corrections.}}
\]

The proof of Proposition 2.1, Corollaries 2.2--2.3, Lemma 3.1,
Theorem 4.1, and the cutoff \(n<380\) is valid. The corrections listed
in Section 8 below do not change a hypothesis, constant, certificate, or
conclusion. The Python certificate itself required no change.

## 1. Audited snapshot

The original note received for audit had SHA-256

646EDF758A0B2352DEB1437651042761CC2822D2CD31CA0A4A2CE9A2D8454198.

After the corrections in Section 8, the audited note is

human/outbox/general-d-round-05-no-drop-finite.md

with SHA-256

E0AC849A4280718EB9CB13C912CA10AA3EB34BC5F9A2EE68C2094B9A09E6A9C8.

The unchanged verifier is

scripts/general_d_no_drop_round5_verify.py

with SHA-256

E13D2B6EA0B7D11C2BC800DAF55F1E45A599B247BAD19658655F2B9B12F53574.

Both files contain zero unexpected control bytes. The verifier also
passes python -m py_compile.

## 2. Independent Arb replay

The checked-in script was run unmodified at its native 512-bit precision.
For the independent 1024-bit replay, the single assignment
ctx.prec = 512 was replaced in memory by ctx.prec = 1024 before
compilation and execution; the audited file on disk was not changed.
Both runs returned exit code zero and

PASS: Round 5 finite no-drop constants certified with Arb.

The following outward enclosures or strict lower bounds were stable at
both precisions:

\[
\begin{array}{c|c}
\text{quantity}&\text{certified value}\\ \hline
K_*&7.70755493909965\ldots\\
\frac{\pi}{2}\left(\theta_1^{-1}+\theta_2^{-1}\right)-2
 &0.7038250888116022\ldots\\
\frac{\pi}{2\theta_1}-1&0.5614277602334956\ldots\\
G_{5/2}(3/2)&0.1938689194162815\ldots\\
6\pi/c_2&37.12133909658248\ldots\\
9\pi/c_3&29.35801182129861\ldots\\
\text{lower margin in (29)}&0.1196334013605442\ldots
\end{array}
\]

The \(K_*\) bisection interval has rational width
\(6.53\cdot10^{-55}\). In particular, every transcendental comparison
used by the note is separated from its decision threshold by a large
margin.

As a consistency check on Section 6, the earlier global-exhaustion
certificate was rerun. Its central list has exactly the two
\(n=1\) pairs \((f,n)=(2,1),(3,1)\), and its 60-pair outer list has no
\(n=1\) pair. Thus the stated update \(649\mapsto647\) is exact.

## 3. Proposition 2.1 and every strict-wall case

Write

\[
 v=G_K(q),\qquad h=G_\mu(q),\qquad
 Q=[A(q)+1/4]_<,\qquad B=[v+1/4]_<.
\]

If \(q<\mu\), strict convexity of \(G_\mu\), its endpoint value
\(G_\mu(\mu)=0\), and \(0<\mu-q<1\) give

\[
 2\int_q^\mu G_\mu<h(\mu-q)<h.
\]

Since \(h\leq G_{q+1}(q)\), and

\[
 \frac{d}{dq}G_{q+1}(q)
 =\frac{\sin\vartheta-\vartheta}{\pi}<0,
\]

the cap is strictly smaller than
\(G_{5/2}(3/2)<1/5\). If \(q=\mu\), the cap is zero directly. This
separate degenerate case is now stated in the note.

For \(q\geq K/2\), every retained strict level satisfies
\(k-1/4<G_K(q)\). Its crossing is therefore strictly to the right of
\(q\), so

\[
 \theta_k<\arccos(q/K)\leq\pi/3,\qquad
 \frac{\pi}{2\theta_k}>\frac32.
\]

The strict-floor cases are:

1. Away from the lower ordinary-floor wall,
   \(Q=f\) and \(B\geq f\). Pairing \(f\) angle terms with the \(f\)
   count units gives more than \(f/2\), and the cap costs less than
   \(1/5\).
2. At the lower wall with \(q<\mu\), \(Q=f-1\), while \(h>0\) gives
   \(B\geq f\). This is stronger.
3. At the lower wall with \(q=\mu\), \(B=Q=f-1\) and the cap is zero.
   Pairing the terms gives
   \(D_A(q)>(f-1)/2\geq1/2\).

For \(q<K/2\), monotonicity in \(q\) and \(K\) gives \(K\geq K_*\).
At \(K_*\), Arb proves

\[
 \theta_1<503/500,\qquad \theta_2<11/8.
\]

The angles only decrease as \(K\) increases. The first two net levels
therefore contribute more than \(7/10\), and one net level contributes
more than \(1/2\). Every further net level is positive because
\(\theta_k<\pi/2\). The same three strict-floor cases then give,
respectively,

\[
 7/10-1/5>1/2,\qquad
 \text{a stronger bound},\qquad
 \pi/(2\theta_1)-1>1/2.
\]

Thus no equality level is passed through by continuity, and
\(D_A(q)>1/2\) holds at every stated wall.

For \(n=1\), concavity of \(A\) gives

\[
 2\int_r^{r+1}A\geq A(r)+A(r+1)\geq2f-\frac12,
\]

so \(R_1\geq-1/2\). The strict terminal reserve proves
\(\mathscr S_1>0\), including when \(q=\mu\).

## 4. Integral representation and profile error

Set \(a=K-u/s\), so

\[
 K=\frac{\kappa}{s^3},\quad
 \mu=\frac{\kappa(1-s^2)}{s^3},\quad
 z=\mu-\frac Xs
   =\frac{\kappa-(\kappa+X)s^2}{s^3}.
\]

Then

\[
 a-z=\frac{\kappa+X-u}{s},\qquad
 a+z=\frac{2\kappa-(\kappa+X+u)s^2}{s^3},
\]

and substitution in

\[
 A(z)=\frac1\pi\int_\mu^K\frac{\sqrt{a^2-z^2}}a\,da
\]

gives (16) exactly, with the displayed orientation and denominator.
Dividing its integrand by the limiting integrand gives (17).

On \(0\leq X\leq2\),

\[
 0\leq b(u)\leq1,\qquad
 0\leq a(u,X)\leq1+\kappa^{-1}\leq29/21.
\]

For \(s^2\leq1/100\),

\[
 1-a s^2\leq\sqrt{1-a s^2}\leq1,\qquad
 0\leq\frac1{1-b s^2}-1\leq\frac{100}{99}s^2.
\]

Because \(100/99<29/21\), these inequalities imply
\(|\mathcal R-1|\leq(29/21)s^2\).

At \(X_q=s\alpha<s\), the sharper bound
\(a<107/105\) gives

\[
 H_\kappa(X_q)
 \leq\frac{A(q)}{1-(107/105)s^2}<31/10.
\]

The exact derivative satisfies

\[
 0<H_\kappa'(X)
 =\frac{3c_0}{2\sqrt\kappa}
   \bigl(\sqrt{\kappa+X}-\sqrt X\bigr)<\frac12.
\]

Hence \(H_\kappa<41/10\) on \([0,2]\), and integration against the
positive limiting integrand yields

\[
 |\mathcal H_{s,\kappa}-H_\kappa|
 <\frac{29}{21}\frac{41}{10}s^2<6s^2.
\]

The bootstrap is therefore non-circular: the endpoint action controls
the limiting profile first, and that profile then controls the integral
error.

## 5. Negative-head estimate

The endpoint error and \(H_\kappa'<1/2\) give

\[
 w=H_\kappa(0)>b-\left(\frac s2+6s^2\right)=b-\zeta.
\]

If \(w\geq f+\zeta\), the estimate at \(X_q\) would give
\(A(q)>f+s/2\), contradicting \(A(q)<f\). Thus the level
\(H_\kappa(X_*)=f+\zeta\) exists with \(X_*>0\).

The exact \(t\)-profile satisfies

\[
 F(t)=\frac{3/t+t^3}{4},\qquad
 H_\kappa'=\frac{3c_0}{2}t.
\]

Since

\[
 F(t_*)=\frac{f+\zeta}{w}
 <\frac{211}{164}<\frac{163}{125}=F(3/5),
\]

and \(F\) decreases on \((0,1]\), one has \(t_*>3/5\). Therefore
\(H_\kappa'>9c_0/10\) on \([0,X_*]\). With
\(d=f+\zeta-w<47/100\),

\[
 X_*<\frac{10d}{9c_0}<\frac{19}{10}.
\]

The function \(H_\kappa\) is concave, so
\(f+\zeta-H_\kappa\) is convex and lies below the chord joining its
endpoint values \(d\) and \(0\). Thus

\[
 \int_0^{X_*}(f+\zeta-H_\kappa)
 \leq\frac{dX_*}{2}
 <\frac{5d^2}{9c_0}.
\]

On the physical head, every point beyond \(X_*\) has
\(\mathcal H_{s,\kappa}>f\). On the possible negative part,
\(\mathcal H_{s,\kappa}-f\geq H_\kappa-f-\zeta\).
Extending that nonnegative loss profile to \([0,X_*]\) proves (27) with
the correct sign:

\[
 sR_n\geq-\frac{10d^2}{9c_0}.
\]

## 6. Exact-angle lower bound

The level \(\tau=3/4\) is always present because
\(G_K(q)\geq A(q)\geq7/4\), even when
\(G_K(q)+1/4\) is an integer. If \(\theta\) is its angle and

\[
 x=\left(\frac{3\pi\tau}{K}\right)^{1/3},
\]

then \(x^3=3(\sin\theta-\theta\cos\theta)\).

First, the chord inequality
\(\sin t\geq2t/\pi\) on \([0,\pi/2]\) gives

\[
 \theta^3
 \leq\frac{9\pi^2}{8K}
 =\frac{9\pi^2}{8\kappa}s^3
 \leq\frac{3\pi^2}{7}s^3
 <3\sqrt3\,s^3.
\]

Therefore \(\theta<\sqrt3\,s\). Next,

\[
 \sin\theta-\theta\cos\theta
 \geq\frac{\theta^3}{3}-\frac{\theta^5}{30}
\]

implies

\[
 \frac{x}{\theta}
 \geq\left(1-\frac{\theta^2}{10}\right)^{1/3}
 \geq1-\frac{\theta^2}{10}
 >1-\frac{3s^2}{10}.
\]

This confirms the Taylor direction in (28). Since

\[
 \frac{\pi s}{2x}
 =\frac{\pi}{2\sqrt2}
  \left(\frac{w}{3/4}\right)^{1/3},
\]

and \(w>b-\zeta\), the displayed leading term in (28) follows.

All discarded terms have the favorable direction:

- all additional exact-angle summands are positive;
- the fractional-top term is nonnegative;
- \(Q\leq f\leq3\);
- the complete cap term satisfies
  \(2\int_q^\mu G_\mu<4\sqrt2/15<2/5\).

Their total cost is therefore less than
\((3+2/5)s=17s/5\). At \(s\leq1/10\), the remaining rational
comparisons give exactly

\[
 \frac{129}{100}\frac{997}{1000}
 -\frac{17}{50}
 -\frac{10}{9}\frac{165}{49}
   \left(\frac{47}{100}\right)^2
 =\frac{1758611}{14700000}
 >\frac1{10}.
\]

Thus Theorem 4.1 is strict and wall-safe.

## 7. Cone, cutoff, and Corollary 2.3

The endpoint-action estimate

\[
 \frac{2\kappa}{3\pi}\leq A(q)<f
\]

has the correct direction. Indeed, \(A(q)\geq A(\mu)=G_K(\mu)\). If
\(\theta=\arccos(1-s^2)\) and
\(h(\theta)=\sin\theta-\theta\cos\theta\), then
\[
 \frac{d}{ds}h(\theta(s))=2s\theta\geq2s^2,
\]
because \(\theta\geq s\).
Integration from \(s=0\) gives
\(h(\theta)\geq2s^3/3\), whence
\(G_K(\mu)\geq2Ks^3/(3\pi)=2\kappa/(3\pi)\).
Thus \(\kappa<3\pi f/2\). Combining this with
\(\delta\geq c_fn/2\) yields

\[
 s=\frac{\kappa}{\delta}
 <\frac{3\pi f}{c_fn}.
\]

For \(f=2,3\), the coefficients are respectively

\[
 \frac{48\pi}{\sqrt{65}-4}<38,\qquad
 \frac{72\pi}{\sqrt{137}-4}<38.
\]

Hence \(n\geq380\) implies the strict bound \(s<1/10\), so Theorem 4.1
excludes every negative scalar there. The conclusion \(n<380\) is
correct.

For Corollary 2.3, the scale-free shelf-curvature bound is

\[
 R_n\geq
 \frac{n^2\Delta}{3(2r+n)}
 +n\left(2\varepsilon+\Delta-\frac12\right).
\]

Multiplying (12a) by \(n\) is exactly the assertion that this right-hand
side is at least \(-1/2\). Proposition 2.1 is strict, so
\(\mathscr S_n>0\). The formula in the original note was missing the
plus sign between the two terms; this has been corrected.

## 8. Corrections made during audit

Only human/outbox/general-d-round-05-no-drop-finite.md was patched:

1. The cap proof now separates \(q=\mu\), where both the cap and \(h\)
   vanish, from \(q<\mu\), where the strict chord inequality applies.
2. The \(q=\mu,\ q\geq K/2\) wall argument now explicitly pairs all
   \(f-1\) count units with their angle terms, avoiding the ambiguous
   phrase “the first term alone.”
3. The missing plus sign in the displayed Corollary 2.3 lower bound was
   restored.

No manuscript file was touched. No mathematical conclusion changed.
