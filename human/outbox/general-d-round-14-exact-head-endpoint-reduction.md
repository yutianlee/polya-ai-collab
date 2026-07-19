# General dimension, Round 14: exact-head endpoint reduction after rejection of the pre-shelf surrogate

Date: 18 July 2026

Status: Round 13 falsifies the sign of the Round 11 pre-shelf surrogate and
therefore also falsifies the proposed Round 12 endpoint target (3.11).  This
note keeps the valid endpoint-monotonic idea but restores the exact no-drop
head and the exact inner cap.  It proves a stronger, strategy-compliant
reduction.  It does not prove the sign of the new endpoint scalar and does
not close the first-floor branch.

## 1. Statement

Let

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}
 \quad(0\le z<a),
 \qquad G_a(z)=0\quad(z\ge a),
\]

and consider a first-floor no-drop tail on one of the new extension grids

\[
 r\in\mathbb N,\quad r\ge1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\quad r\ge\frac32.
 \tag{1.1}
\]

Put

\[
 q=r+n,\qquad n\ge1,\qquad
 \mu=q+\alpha,\qquad 0\le\alpha<1,
\]

\[
 A_\alpha=G_K-G_{q+\alpha},
 \qquad
 \varepsilon(\alpha)=A_\alpha(q)-\frac34,
 \tag{1.2}
\]

and assume the hard open one-level phase

\[
 B=1,\qquad 0<\varepsilon(\alpha)<\frac14,
 \qquad (Q,\chi_q)=(1,0).
 \tag{1.3}
\]

Let \(\theta\) be the outer inverse-level angle

\[
 \frac K\pi(\sin\theta-\theta\cos\theta)=\frac34,
\]

and define

\[
 z=K\cos\theta,\qquad y=z-q,
 \qquad \eta=y-[y]_<\in(0,1],
 \tag{1.4}
\]

\[
 v=G_K(q),\qquad
 \beta=\frac{\arccos(q/K)}\pi,
 \qquad
 \delta(\alpha)=\int_q^{q+\alpha}G_{q+\alpha}(s)\,ds.
 \tag{1.5}
\]

The exact one-level terminal lower expression on the open side is

\[
 L_{\rm ex}(\alpha)=
 \frac\pi{2\theta}+2\eta-1-2\delta(\alpha)
 +\frac{(v-1)_+^2}{\beta}.
 \tag{1.6}
\]

Define the exact no-drop head

\[
 H_n(\alpha)=2\int_r^q\bigl(A_\alpha(s)-1\bigr)\,ds
 \tag{1.7}
\]

and the correlated scalar

\[
 \boxed{\Xi(\alpha)=L_{\rm ex}(\alpha)+H_n(\alpha).}
 \tag{1.8}
\]

Let \(\bar\alpha\) be the first phase, branch, or owner-dimensional
activity endpoint from Round 12:

\[
 \bar\alpha=\min\{1,\alpha_*,\alpha_{\rm act}\},
 \qquad
 G_{q+\alpha_*}(q)=v-\frac34,
 \tag{1.9}
\]

\[
 \alpha_{\rm act}=
 K-q-\frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}},
 \qquad
 \kappa_{d_{\rm own}}=
 \frac{(d_{\rm own}-2)^2-1}{4},
 \tag{1.10}
\]

where \(d_{\rm own}=4\) on the integer grid and \(d_{\rm own}=5\) on
the half-integer grid.

### Proposition 1.1 (exact-head endpoint reduction)

On the domain (1.1)--(1.3):

1. \(L_{\rm ex}(\alpha)>1/12\), so no maximum with zero is needed;
2. the exact no-drop identity and the one-level terminal theorem give
   \(D_{A_\alpha}(r)\ge\Xi(\alpha)\);
3. \(\Xi\) is strictly decreasing in \(\alpha\); and therefore

\[
 \boxed{D_{A_\alpha}(r)\ge\Xi(\alpha)>\Xi(\bar\alpha).}
 \tag{1.11}
\]

The weak inequality \(D_{A_\alpha}(r)\ge\Xi(\bar\alpha)\) is enough for
closure.  Thus the selected first-floor problem is reduced to the new exact
endpoint target

\[
 \boxed{\Xi_{\rm end}(\theta,y,n):=\Xi(\bar\alpha)\ge0.}
 \tag{1.12}
\]

Unlike the rejected Round 11--12 target, (1.12) retains the exact head
integral and the exact cap.

## 2. A uniform positive terminal head

The extension grids give \(q=r+n\ge2\).  Since \(B=1\), one has
\(v>3/4\), so the outer inverse point in (1.4) satisfies
\(z>q\ge2\).

Put \(\Phi(\theta)=\sin\theta-\theta\cos\theta\).  The inverse point is

\[
 z(\theta)=\frac{3\pi\cos\theta}{4\Phi(\theta)}.
 \tag{2.1}
\]

It is strictly decreasing on \((0,\pi/2)\), since

\[
 \frac{d}{d\theta}\frac{\cos\theta}{\Phi(\theta)}
 =-\frac{\sin^2\theta}{\Phi(\theta)^2}<0.
 \tag{2.2}
\]

At \(\theta_0=3\pi/8\), the inequality \(z(\theta_0)<2\) is equivalent
to

\[
 \tan\frac{3\pi}{8}=1+\sqrt2>\frac{3\pi}{4}.
\]

This last comparison is exact from \(\pi<22/7\) and
\(\sqrt2>19/14\).  Hence \(z>2\) implies

\[
 0<\theta<\frac{3\pi}{8},
 \qquad
 \frac\pi{2\theta}-1>\frac13.
 \tag{2.3}
\]

Next, for \(q\ge2\), the function

\[
 q\longmapsto G_{q+1}(q)
\]

is strictly decreasing.  If
\(\varphi=\arccos(q/(q+1))\), direct differentiation gives

\[
 \frac{d}{dq}G_{q+1}(q)
 =\frac{\sin\varphi-\varphi}{\pi}<0.
 \tag{2.4}
\]

Moreover

\[
 G_3(2)=\frac{\sqrt5-2\arccos(2/3)}\pi<\frac14.
 \tag{2.5}
\]

Indeed, \(\sqrt5<9/4\), while
\(\cos(3/4)\ge1-(3/4)^2/2=23/32>2/3\), so
\(\arccos(2/3)>3/4\); finally \(\pi>3\).

The local cap estimate and \(0\le\alpha\le1\) now give

\[
 0\le2\delta(\alpha)
 \le\alpha G_{q+\alpha}(q)
 \le G_{q+1}(q)<\frac14.
 \tag{2.6}
\]

Equations (1.6), (2.3), and (2.6), with \(2\eta>0\) and the top square
nonnegative, prove

\[
 \boxed{L_{\rm ex}(\alpha)>\frac13-\frac14=\frac1{12}.}
 \tag{2.7}
\]

This also proves that the nonsmooth maximum in the earlier terminal lower
bound is inactive everywhere on the new extension-grid target.

## 3. Restoration of the exact no-drop head

On the first-floor no-drop branch, the exact Round 10--11 remainder is

\[
 R_n=-\frac n2+2n\varepsilon
 +2\int_0^n u\sigma(r+u)\,du,
 \qquad \sigma=-A_\alpha'.
 \tag{3.1}
\]

Integration by parts, using
\(A_\alpha(q)=3/4+\varepsilon\), gives

\[
 \begin{aligned}
 2\int_0^n u\sigma(r+u)\,du
 &=-2nA_\alpha(q)+2\int_r^q A_\alpha(s)\,ds,\\
 R_n
 &=2\int_r^q\bigl(A_\alpha(s)-1\bigr)\,ds
 =H_n(\alpha).
 \end{aligned}
 \tag{3.2}
\]

Thus (1.7) is not a new estimate: it is the exact S4 head.  In the open
phase \(\chi_q=0\), S4 and the one-level T2 bound with the exact cap yield

\[
 D_{A_\alpha}(r)
 \ge L_{\rm ex}(\alpha)+H_n(\alpha)
 =\Xi(\alpha),
 \tag{3.3}
\]

where (2.7) justifies removal of \(\max\{0,L_{\rm ex}\}\).  No curvature
minorant, active-width lower bound for \(\Delta\), or replacement of the
head by \(\mathcal R_0\) occurs in (3.3).

## 4. Monotonicity and the endpoint

For fixed \(K,q,r,n\), the map \(a\mapsto G_a(s)\) is strictly increasing
when \(s<a\), with

\[
 \frac{\partial}{\partial a}G_a(s)
 =\frac{\sqrt{a^2-s^2}}{\pi a}>0.
 \tag{4.1}
\]

Consequently \(A_\alpha(s)=G_K(s)-G_{q+\alpha}(s)\) is strictly
decreasing in \(\alpha\) for every \(s\in[r,q)\).  Therefore

\[
 H_n(\alpha)=2\int_r^q(A_\alpha(s)-1)\,ds
 \tag{4.2}
\]

is strictly decreasing.

The cap \(\delta(\alpha)\) is strictly increasing for \(\alpha>0\): when
the ball radius grows, its action increases pointwise on the old interval
and a nonnegative terminal interval is added.  Hence \(L_{\rm ex}\) is
nonincreasing, and it is strictly decreasing away from \(\alpha=0\).
Together with the strict decrease of \(H_n\), this proves that \(\Xi\) is
strictly decreasing on \([0,1]\).

Every original active open-phase point lies below the phase root, the branch
endpoint, and the strict owner-dimensional activity wall.  Thus
\(\alpha<\bar\alpha\), and (1.11) follows by continuity, including when
\(\bar\alpha\) is used only as a one-sided limiting value.

At the literal lower-noncorner wall \(\varepsilon=0\), one has
\((Q,\chi_q)=(0,1)\).  Relative to the open-side expression, the terminal
term gains one unit because \(Q\) drops from one to zero, and S4 gains the
additional unit \(\chi_q=1\).  Hence the literal wall is strictly more
favorable than the endpoint value in (1.12).

## 5. Dependencies

The proof uses only:

1. the exact no-drop identity S4, including \(\chi_q\);
2. the one-level specialization of the audited fractional terminal theorem
   T2, with its exact cap \(2\delta\);
3. the local cap estimate T3;
4. the owner-dimensional strict no-mode wall used to define
   \(\alpha_{\rm act}\); and
5. the valid endpoint-domain bookkeeping from Round 12.

Round 13 is a gate-decision and falsification dependency, not a premise of
the inequalities proved here.

## 6. Equality-face audit

1. **Ordinary-floor wall.**  If
   \(A(r+j)+1/4\in\mathbb N\), the first shelf uses the ordinary floor and
   its remainder is zero.  Formula (3.2) is the exact S4 identity and does
   not approach this wall from an adjacent floor chamber.
2. **Interface sample.**  If \(r+j=\mu\), then
   \(G_\mu(r+j)=0\).  If \(\mu-r\in\mathbb N\), the literal endpoint has
   \(q=\mu\), \(\alpha=0\), and \(\delta=0\).
3. **Outer sample.**  If \(r+j=K\), the sample is absent under the strict
   bracket.  The integral in (1.7) is unaffected by this convention.
4. **Inverse spatial wall.**  If \(y\in\mathbb N\), then
   \(\eta=1\), not zero.  One-sided values with \(\eta\downarrow0\) are
   separate open cells and must be tested separately.
5. **Action wall.**  At \(\varepsilon=0\), the literal pair is
   \((Q,\chi_q)=(0,1)\); the two favorable jumps are retained as described
   after (4.2).
6. **Branch and activity walls.**  The values \(\alpha=1\) and
   \(\alpha=\alpha_{\rm act}\) are used only as limiting values of the
   explicit scalar.  No inadmissible equality is inserted into the original
   open chamber.

Artificial motion to \(\bar\alpha\) may cross a shelf wall.  This creates
no gap: (4.2) compares the explicit integral scalar and does not assert that
every intermediate point remains in the same discrete chamber.

## 7. Loss ledger

The reduction (1.11) makes only these losses.

1. T2 replaces the exact terminal outer defect by the inverse-level tangent
   lower bound, discarding its nonnegative tangent gaps.
2. The maximum with the proved one-interface lower bound is unnecessary on
   the extension grids because (2.7) proves the T2 expression itself
   positive.
3. Moving from \(\alpha\) to \(\bar\alpha\) discards the strictly positive
   monotonic gap \(\Xi(\alpha)-\Xi(\bar\alpha)\).
4. At the literal lower wall, using the open-side endpoint discards both
   favorable unit jumps.

The exact head \(H_n\), the exact cap \(2\delta\), \(2\eta\), the top
square, and the owner-dimensional activity endpoint are retained.  In
particular, this note makes none of the pre-shelf losses that caused the
Round 13 counterexample.

## 8. Counterexample search and gate decision

The Round 13 integer-grid counterexample has

\[
 \theta=\frac{531}{4000},\qquad q=3000,\qquad n=51,
 \qquad r=2949,
\]

and an actual open point at \(\alpha=999/1000\).  There the rejected
Round 11--12 scalar is approximately \(-1.38722\), while direct
high-precision evaluation gives

\[
 L_{\rm ex}\approx11.31324,
 \qquad H_n\approx29.90464,
 \qquad \Xi\approx41.21788.
\]

Thus restoring the exact correlated head does not merely perturb the false
surrogate; it restores more than forty units of visible margin at the
falsifying point.  These numbers are diagnostic and are not used in the
proof above.

The Mathematica evaluator
`computations/general_d_round14_exact_head_endpoint_probe.wl` also moved the
3,171 seeded hard extension-grid records from Round 12 to the exact-head
endpoint.  It found no sampled negative value.  Its smallest value was

\[
 \Xi_{\rm end}\approx0.13877007259
\]

near the earlier small-grid pattern \(r=1,n=2,q=3\).  The script separately
replayed the large-\(q\) counterexample, the exact S4 identity, and the
positive Round 14 value, and printed `round14ReplayOK=True`.  This seeded
high-precision replay is not an interval enclosure and does not establish
coverage.

The gate decision is therefore:

1. reject the sign target \(\widehat\Psi_1\ge0\) and its Round 12 endpoint
   specialization as universal sufficient lemmas;
2. retain Round 11's proved \(B=0\) theorem and Round 12's valid monotonic
   technique;
3. make (1.12), with exact head and exact cap, the next pointwise target;
4. if (1.12) is falsified, switch to the weighted aggregate WT rather than
   introduce a ratio partition or another lossy head surrogate.

## 9. Failure report

The only unproved assertion suggested by this note is

\[
 \Xi_{\rm end}(\theta,y,n)\ge0
\]

on the exact first-floor no-drop extension-grid domain.  The expected hard
face remains the small-grid phase endpoint with
\(\varepsilon\downarrow0\) and \(\eta\downarrow0\), not the large-
\(q\) example that falsifies the pre-shelf surrogate.  A new deterministic
falsification pass beyond the seeded replay must optimize
\(\Xi_{\rm end}\) itself on every one-sided inverse wall before any further
analytic split is proposed.
