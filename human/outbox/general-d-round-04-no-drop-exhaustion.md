# General dimension, Round 4c: global exhaustion of the no-drop branch

Date: 18 July 2026

Status: rigorous global finite/exclusion theorem.  The high-floor no-drop
branch is reduced to an explicit finite box except for the two rows
\(f=2,3\).  Every escaping sequence in those rows is forced onto the
critical grazing ray \(K\asymp n^3\), \(K-\mu\asymp n\); the independently
proved critical-ray theorem has a uniform positive leading gap there, so
the two rows are finite as well, qualitatively.  A numerical cutoff in
those rows is not claimed because a quantified finite-thickness remainder
has not yet been proved.  No manuscript file is changed by this note.

## 1. Residual data

Use the notation of the preceding no-drop notes:

\[
 \delta=K-\mu,\qquad n=\lfloor\mu-r\rfloor,\qquad
 q=r+n,\qquad \alpha=\mu-q\in[0,1),
\]

and suppose

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \qquad(0\le j\le n),\qquad f\ge2.
\]

Only \(n\ge1\) needs consideration: when \(n=0\), the head reserve is
\(R_0=0\) and the completed one-interface theorem is already sufficient.

Put

\[
 b=f-\frac14,
 \qquad A(q)=b+\varepsilon,
 \qquad A(r)=b+\varepsilon _0,
 \qquad \Delta=\varepsilon _0-\varepsilon.
\]

The one-interface tail \(D_A(q)\) is nonnegative.  Hence only
\(R_n<0\) can remain.  The exact no-drop formula and the shelf-curvature
identity then imply

\[
 \varepsilon _0+\varepsilon<\frac12,
 \qquad 0\le\varepsilon<\frac14,
 \qquad 0\le\Delta<\frac12,
 \qquad A(q)<f,
 \qquad A(r)<f+\frac14.                              \tag{1}
\]

The root-free terminal theorem closes the tail if

\[
 K\ge K_{\rm nd}(n,Q)
 :=\left(\frac{Q+n/2+c_*}{C_0S_Q}\right)^3,
\]

where

\[
 C_0^3=\frac\pi{12},\qquad c_*=\frac{4\sqrt2}{15},
 \qquad S_Q=\sum_{k=1}^Q(k-\tfrac14)^{-1/3},
 \qquad Q\in\{f-1,f\}.
\]

Thus every residual tail satisfies

\[
 K<K_{\rm nd}(n,Q).                                 \tag{2}
\]

At the endpoint wall one may replace \(S_Q\) by \(S_B\), with
\(B\ge Q\), as described in the preceding terminal note.  We deliberately
retain the weaker \(B=Q\) cutoff in the global exhaustion below; every
conclusion is therefore wall-safe.

## 2. Three uniform geometric inequalities

The radius derivative representation gives

\[
 A(q)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{q^2}{a^2}}\,da
 \le \frac\delta\pi
 \sqrt{\frac{2(\delta+1)}K}.
\]

Since \(A(q)\ge b\),

\[
 \boxed{
 K\le U_f(\delta):=
 \frac{2\delta^2(\delta+1)}{\pi^2b^2}.}             \tag{3}
\]

For the inner slope \(\sigma=-A'\),

\[
 \sigma(z)=\frac1\pi\int_\mu^K
 \frac{z}{a\sqrt{a^2-z^2}}\,da
 \ge\frac{\delta z}{\pi K^2}.
\]

Integrating from \(r\) to \(q\), and using \(\Delta<1/2\), gives

\[
 \boxed{
 b\,n(2r+n)<K^2,
 \qquad b\,n(n+1)<K^2.}                             \tag{4}
\]

Finally, the convex-slope estimate from the high-floor note gives

\[
 A(0)-A(r)\le\frac{r\Delta}{2n}<\frac r{4n}.
\]

As \(A(0)=\delta/\pi\), (1) yields

\[
 \boxed{
 \frac\delta\pi<f+\frac14+\frac r{4n}.}            \tag{5}
\]

These three inequalities are necessary for every unresolved tail.

## 3. Central geometry: an explicit finite box

First suppose

\[
 r\le\frac K2.                                      \tag{6}
\]

Because \(r=K-\delta-\alpha-n\), condition (6) gives

\[
 r\le\delta+\alpha+n<\delta+n+1.
\]

Substitution in (5) proves

\[
 \delta<D_{n,f}:=
 \frac{f+\frac12+\frac1{4n}}
 {\frac1\pi-\frac1{4n}}.                           \tag{7}
\]

Equations (3)--(4) now give the purely discrete necessary condition

\[
 \boxed{
 b\,n(n+1)<U_f(D_{n,f})^2.}                         \tag{8}
\]

For fixed \(f\), the left side of (8) increases with \(n\), whereas
\(D_{n,f}\), and hence its right side, decreases.

Here is a short analytic exhaustion before the final finite check.  The
integral comparison

\[
 S_Q\ge\frac32\left((Q+\tfrac34)^{2/3}
 -(\tfrac34)^{2/3}\right)
 \ge\frac54Q^{2/3}\qquad(Q\ge7)                    \tag{9}
\]

shows that, for \(f\ge16\), (2) is impossible when \(n\le f/6\).
The normalized left side of the required cutoff comparison increases
with \(f\), the normalized right side decreases, and the endpoint
\(f=16\) is certified in the replay script.

Thus a residual pair with \(f\ge16\) has \(n>f/6\).  In this range
\(D_{n,f}<5f\).  Indeed, using \(\pi<22/7\), it is enough to check

\[
 \frac{13f}{22}-8-\frac{3}{2f}>0,
\]

which holds at \(f=16\) and increases thereafter.  Since
\(b\ge63f/64\) and \(\pi>3\),

\[
 U_f(D_{n,f})<\frac{12800}{441}f<30f.
\]

Consequently (8) implies \(n<31\sqrt f\).  Combining this with
\(n>f/6\) gives

\[
 \boxed{f<34596}                                    \tag{10}
\]

in the central branch.

The remaining comparison is finite and one-dimensional.  For every
\(50\le f\le34595\), outward Arb arithmetic proves:

1. (8) already fails at \(n=f-1\), and hence at every larger \(n\);
2. for \(Q=f-1,f\), the cutoff inequality (2) fails throughout
   \(1\le n\le f-2\).

For the second assertion it is enough to check \(n=1,f-2\), because
\(K_{\rm nd}(n,Q)-[\pi b+n+1/2]\) is convex in \(n\).  Enumerating
\(2\le f\le49\) until the monotone obstruction (8) begins gives

\[
 \boxed{
 r\le K/2\quad\Longrightarrow\quad
 2\le f\le49,\qquad1\le n\le48.}                  \tag{11}
\]

There are 649 pairs retained by these necessary inequalities; this is
not a claim that all 649 pairs are realizable.

## 4. Outer geometry and its limiting coefficient

Now suppose

\[
 r>\frac K2.                                        \tag{12}
\]

The exact head formula and \(R_n<0\) give

\[
 2\int_0^n u\sigma(r+u)\,du<\frac n2.
\]

Since \(\sigma\) is increasing,

\[
 n^2\sigma(r)
 =2\sigma(r)\int_0^n u\,du
 \le2\int_0^n u\sigma(r+u)\,du<\frac n2,
\]

so

\[
 \sigma(r)<\frac1{2n}.                              \tag{13}
\]

On the other hand,

\[
 \sigma(r)\ge
 \frac{\delta r}{\pi K\sqrt{K^2-r^2}}
 >\frac{\delta}{2\pi\sqrt{2K(\delta+n+1)}}.
\]

Combining this with (13) proves

\[
 \boxed{
 K>\frac{\delta^2n^2}
 {2\pi^2(\delta+n+1)}.}                             \tag{14}
\]

Combining (14) with (3), and putting \(d=(\delta+1)/n\), gives

\[
 b^2<4d(d+1).
\]

Therefore

\[
 \boxed{
 \delta+1>c_fn,
 \qquad
 c_f:=\frac{\sqrt{1+b^2}-1}{2}.}                   \tag{15}
\]

Let

\[
 \delta_{n,f}:=\max\{\pi b,c_fn-1\}.
\]

The right side of (14) increases with \(\delta\).  Hence every
residual outer pair obeys

\[
 \boxed{
 L_{n,f}:=
 \frac{\delta_{n,f}^2n^2}
 {2\pi^2(\delta_{n,f}+n+1)}
 <K_{\rm nd}(n,Q).}                                 \tag{16}
\]

The same argument used above gives \(n>f/6\) for \(f\ge16\).  Here
\(c_f\ge f/3\), \(c_f<f/2\), and \(c_fn-1\ge c_fn/2\).  Thus (14)
gives

\[
 K>\frac{fn^3}{405}.
\]

Using (9), \(Q\ge f-1\), \(Q\le f\), and \(n>f/6\), one also has

\[
 K_{\rm nd}(n,Q)<703\frac{n^3}{(f-1)^2}.
\]

Consequently a residual outer pair satisfies

\[
 f(f-1)^2<284715,
\]

and therefore

\[
 \boxed{f\le66.}                                    \tag{17}
\]

Once \(c_fn-1\ge\pi b\), division of (16) by \(n^3\) gives

\[
 \frac{(c_f-1/n)^2}{2\pi^2(c_f+1)}
 <
 \frac{(\frac12+(Q+c_*)/n)^3}{(C_0S_Q)^3}.          \tag{18}
\]

The left side increases with \(n\), and the right side decreases.  Its
limiting coefficients are

\[
 \gamma_f=\frac{c_f^2}{2\pi^2(c_f+1)},
 \qquad
 \beta_J=\frac1{8(C_0S_J)^3}
 =\frac3{2\pi S_J^3}.                               \tag{19}
\]

Both \(c_f\) and \(c_f^2/(c_f+1)\) increase with \(f\), while
\(\beta_J\) decreases with \(J\).  The certified comparisons

\[
 \gamma_2<\beta_2,
 \qquad \gamma_3<\beta_3,
 \qquad \gamma_4>\beta_3                            \tag{20}
\]

therefore identify the limiting alternatives exactly:

\[
 \boxed{
 \text{(16) can remain unbounded only for }f=2,3.}  \tag{21}
\]

For \(4\le f\le66\), the monotonic comparison (18) is finite.
The Arb replay gives the sharper box

\[
 \boxed{
 r>K/2,\ f\ge4
 \quad\Longrightarrow\quad
 4\le f\le8,\qquad1\le n\le39.}                  \tag{22}
\]

There are 60 pairs retained by the necessary inequalities in this box.

## 5. Exact form of every escaping ray

It remains to understand whether the two alternatives in (21) are real
noncompact obstructions.  Suppose, for contradiction, that a sequence
of unresolved tails has \(n\to\infty\).  Sections 3--4 force

\[
 f\in\{2,3\},\qquad r>K/2.                           \tag{23}
\]

For fixed \(f\), (2) gives \(K=O(n^3)\), while (14)--(15) give
\(\delta\gg n\).  A reverse action estimate supplies the missing upper
bound.  On the upper half of the radius interval \([\mu,K]\),

\[
 A(q)\ge\frac\delta{2\pi}
 \sqrt{\frac\delta{2K}}.
\]

Since \(A(q)<f\),

\[
 \delta^3<8\pi^2f^2K.                               \tag{24}
\]

It follows from (2), (14), (15), and (24) that

\[
 \boxed{
 \delta\asymp n,\qquad K\asymp n^3,
 \qquad \frac rK\to1,\qquad\frac\mu K\to1.}       \tag{25}
\]

For a directly reusable quantitative cone, define

\[
 \mathcal K_f=
 \left(\frac{f+\frac12+c_*}{C_0S_{f-1}}\right)^3,
 \qquad
 \mathcal D_f=(8\pi^2f^2\mathcal K_f)^{1/3}.
\]

Then, for \(n\ge\lceil2/c_f\rceil\), every escaping candidate satisfies

\[
 \boxed{
 \frac{c_f}{2}n\le\delta<\mathcal D_fn,
 \qquad
 \frac{c_f^2}{8\pi^2(\mathcal D_f+2)}n^3
 <K<\mathcal K_fn^3.}                              \tag{25a}
\]

Indeed, the upper \(K\)-bound follows from (2), the upper \(\delta\)-bound
from (24), and the lower \(K\)-bound from (14).  For orientation only,
the corresponding decimal cones are

\[
 \begin{array}{c|cc|cc}
 f&\delta/n\text{ lower}&\delta/n\text{ upper}
   &K/n^3\text{ lower}&K/n^3\text{ upper}\\ \hline
 2&0.253891&27.827401&1.09483\!\times10^{-4}&68.228874\\
 3&0.481543&28.015693&3.91375\!\times10^{-4}&30.943673
 \end{array}
\]

Set

\[
 \eta=1-\rho=\frac\delta K,
 \qquad
 \kappa=K\eta^{3/2}=\frac{\delta^{3/2}}{\sqrt K},
 \qquad
 N=n\sqrt\eta,
 \qquad c_0=\frac{2\sqrt2}{3\pi}.
\]

After passage to a subsequence, \((\kappa,N)\) lies in a compact
positive rectangle.  The turning expansion at the interface gives

\[
 A(q)\longrightarrow w=c_0\kappa.
\]

Condition (1) therefore gives the precise compact \(\kappa\)-ranges

\[
 \boxed{
 \begin{array}{ll}
 f=2:&\displaystyle
 \frac{21\pi}{8\sqrt2}\le\kappa\le
 \frac{3\pi}{\sqrt2},\\[6pt]
 f=3:&\displaystyle
 \frac{33\pi}{8\sqrt2}\le\kappa\le
 \frac{9\pi}{2\sqrt2}.
 \end{array}}                                      \tag{26}
\]

More fully, every limiting pair satisfies

\[
 \boxed{
 \left(\frac\kappa{\beta_{f-1}}\right)^{1/3}
 \le N\le\frac\kappa{c_f}.}                       \tag{27}
\]

The left inequality follows from the weakest cutoff
\(K<\beta_{f-1}n^3+o(n^3)\), and the right one from (15).  The dangerous
no-drop endpoint condition supplies the sharper curved boundary

\[
 H_\kappa(N)+c_0\kappa\le2f,                        \tag{28}
\]

where

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \big((\kappa+X)^{3/2}-X^{3/2}\big).
\]

Thus (26)--(28), not an unspecified \(\rho\uparrow1\) regime, are the
exact compact limiting domain left by the elementary exhaustion.

## 6. The critical-ray theorem removes noncompactness qualitatively

The critical-ray analysis in
`general-d-round-04-high-floor-cutoff.md`, Theorem 3.1 and Corollary 3.2,
applies exactly to (25)--(28).  It proves the uniform leading gap

\[
 \boxed{
 \liminf_{\eta\downarrow0}\sqrt\eta\,\mathscr S
 \ge\gamma_0:=
 \frac\pi{2\sqrt2}
 \left[\left(\frac73\right)^{1/3}-1\right]
 >\frac13.}                                        \tag{29}
\]

The bound is uniform over both compact domains in (26)--(28).  It uses
only the first complete terminal level; the fractional-top refinement
from the zero-level terminal note is compatible and can only increase
the limiting payment.  In particular, an unresolved sequence with
\(n\to\infty\) would contradict (29).

Hence the two rows \(f=2,3\) are finite in \(n\) as a matter of proof.
The argument is sequential: it does not furnish a numerical value of
the cutoff because the turning expansions used in (29) have not yet
been supplied with a uniform explicit remainder on (26)--(28).  A
uniform estimate of the form

\[
 \sqrt\eta\,\mathscr S
 \ge\gamma_0-C\sqrt\eta
\]

would make that cutoff explicit.  This note does not claim such an
estimate.

## 7. Audited conclusion

The no-drop branch now has the following rigorous status.

1. In the central region \(r\le K/2\), every unresolved pair lies in
   the explicit box \(f\le49,n\le48\).
2. In the outer region \(r>K/2\), every unresolved pair with \(f\ge4\)
   lies in the explicit box \(f\le8,n\le39\).
3. The only elementary noncompact alternatives are \(f=2,3\), with the
   exact critical scaling and compact parameter domain (25)--(28).
4. The uniform positive gap (29) rules out escape on those alternatives.
   Therefore only finitely many \((n,f,Q)\) occur globally, although the
   last two numerical \(n\)-cutoffs are not yet explicit.
5. For every fixed \((n,f,Q)\), the preceding no-drop terminal note has
   already reduced the residual problem to finitely many one-sided walls
   in a compact \((K,\mu)\)-strip.

The outward-rounded comparisons in (9)--(11), (20), and (22) are replayed
by [`general_d_no_drop_exhaustion_verify.py`](../../scripts/general_d_no_drop_exhaustion_verify.py).
At 256-bit precision it reports 138,184 central endpoint comparisons,
649 retained central necessary pairs, 980 outer comparisons, and 60
retained finite outer necessary pairs.

This is a global finite reduction of the no-drop branch, not yet a proof
of every remaining finite chamber.  The precise next task is either to
quantify the remainder in (29), producing explicit cutoffs for the two
rows \(f=2,3\), or to certify those rows directly by a separate monotone
wall argument.
