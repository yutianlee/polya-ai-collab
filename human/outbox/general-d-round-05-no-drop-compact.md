# General dimension, Round 5: compact certificate for the two low-floor no-drop rows

Date: 18 July 2026

This note closes the finite interval calculation left by the quantitative
no-drop transfer for the two exceptional rows

\[
 f\in\{2,3\},\qquad 2\le n\le379,\qquad \sigma\ge\frac1{10}.
\]

Together with the earlier analytic theorem for \(\sigma\le1/10\), the
cutoff \(n\ge380\), and the direct \(n=1\) argument, it closes the complete
\(f=2,3\) no-drop sector.  It does not certify any remaining \(f\ge4\)
finite wall.  No manuscript file is changed here.

The final low-floor certificate source is
`scripts/general_d_no_drop_low_floor_final_verify.py`.  The shared
high-floor replay core remains frozen separately at
`scripts/general_d_no_drop_compact_verify.py`; Section 9 records both
source hashes and the complete replay ledger.

## 1. Coordinates and compact localization

Write

\[
 \delta=K-\mu,\qquad
 \sigma=\sqrt{\frac{K-\mu}{K}},\qquad
 \kappa=\sigma\delta=\sigma^3K,
\]

and

\[
 q=\mu-\alpha,\qquad r=q-n,\qquad
 b=f-\frac14.
\]

Thus

\[
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3}.
\]

On an endpoint wall, \(A(q)=b\).  The endpoint action estimate gives

\[
 \frac{2\kappa}{3\pi}\le A(q)<\frac{2\kappa}{\pi}.
\]

Consequently every compatible root lies in the rational interval

\[
 \frac{21}{8}\le\kappa\le
 \begin{cases}
 66/7,&f=2,\\
 99/7,&f=3.
 \end{cases}
\]

The root-free cutoff \(K<K_{\rm nd}(n,Q)\), physicality
\(\mu\ge n+1/2\), and these \(\kappa\)-bounds give the initial compact
\(\sigma\)-interval.  When \(n>48\), the already proved central
obstruction and outer cone add \(\sigma<38/n\).  Directed bisection keeps
the excluded endpoint in the retained interval, so this initialization
cannot leave a gap.

## 2. Strict phase bookkeeping

The proof has three calls, with the equality faces interpreted using the
one-sided strict count from the indicated chamber:

\[
\begin{array}{c|c|c|c|c}
\text{phase}&\alpha&\varepsilon=A(q)+1/4-f&Q&
 \text{ball levels}\\ \hline
\text{corner}&0&0&f-1&f-1\\
\text{lower}&0<\alpha<1&0&f-1&f\\
\text{open}&0\le\alpha<1&0<\varepsilon<1/4&f&f
\end{array}
\]

At the corner, \(q=\mu\), so the inner cap is zero and the strict outer
count is \(f-1\).  At a noncorner lower wall the positive inner cap forces
the outer ball to retain at least \(f\) levels even though the shell count
is \(Q=f-1\).  The interval program includes \(\alpha=0,1\) as closed
one-sided limits, but it never changes the combinatorics on an equality
face.

## 3. Reduction of the open phase

Fix \((\mu,r)\) inside an open no-drop chamber and lower \(K\).  The full
scalar has

\[
 \partial_K\mathscr S_n
 =\frac2\pi\int_r^K\sqrt{1-z^2/K^2}\,dz>0.
\]

The first shell wall met is \(A(q)=b\): every earlier sample is strictly
to the left of \(q\), and decreasing \(K\) cannot cross an upper floor.
Hence an open negative point is dominated by the value on that lower
wall.  The certificate evaluates this endpoint with the open-side data
\(Q=f\) and \(f\) retained ball levels.

Along the deformation, \(\sigma\) decreases.  If \(\sigma=1/10\) is met
before the wall, the analytic small-\(\sigma\) theorem applies.  Its cone
hypotheses follow from the same necessary conditions used here: for
\(n>48\), the central obstruction forces \(r>K/2\); for \(n\le48\), the
bound \(K/2\ge50\delta>\delta+n+1\) does so at \(\sigma\le1/10\).
The remaining width, slope, and cutoff inequalities are precisely the
quantitative-transfer cone.  Thus the wall reduction loses no open
candidate.

After the cap cancellation the endpoint expression may equivalently be
written

\[
 2\int_r^{r+n}G_K-2\int_r^\mu G_\mu-2nf
 +\frac\pi2\sum_{k=1}^{f}\frac1{\theta_k}-f,
\]

which is the scalar enclosed by the code.

## 4. Enclosing the endpoint root

For an ordinary lower or open box put \(t=\sigma^2\),
\(y=\sigma\,\mathrm{shift}/\kappa\), and

\[
 \Phi(v)=
 \frac{\sqrt{(1-v+y)\{2-(1+v+y)t\}}}{1-vt},
 \qquad 0\le v\le1.
\]

This profile is concave.  Indeed, with

\[
 z=\frac{1-v+y}{1-vt},\qquad
 \phi(z)=\sqrt{z(2-tz)},\qquad c=1-t(1+y)\ge0,
\]

one has

\[
 z'=-\frac{c}{(1-vt)^2},\qquad
 z''=-\frac{2tc}{(1-vt)^3},\qquad
 \phi'\ge0,qquad \phi''=-\phi^{-3}<0.
\]

Therefore \(\Phi''\le0\).  A composite four-panel trapezoid is a lower
bound and the corresponding midpoint rule is an upper bound.  Arb
evaluates both outwardly.

At fixed \((\sigma,\alpha)\), the two radicand factors after
\(u=\kappa v\) are nondecreasing in \(\kappa\); the endpoint action is
strictly increasing.  Twelve directed bisection steps consequently give
a common root enclosure for every point in a parameter box.  A universal
sign is required before a root is discarded; otherwise the box is split.

At the corner the root is eliminated exactly.  If

\[
 \theta=2\arctan\frac{\sigma}{\sqrt{2-\sigma^2}},\qquad
 h=\sigma\sqrt{2-\sigma^2}-(1-\sigma^2)\theta,
\]

then \(G_K(\mu)=b\) is equivalent to

\[
 \boxed{\kappa=\frac{b\pi\sigma^3}{h}}.
\]

The half-angle formula is stable and its directed image is intersected
with the proved \(\kappa\)-interval.

## 5. Cancellation-free positive series

Some low-floor boxes are too narrow for subtracting ordinary action
enclosures.  For \(x=\mathrm{gap}/(2R)<1/2\), use instead the positive
identity

\[
 G_R(R-\mathrm{gap})=
 \frac{8Rx^{3/2}}\pi
 \sum_{m\ge0}
 \frac{\binom{2m}{m}}
 {4^m(2m+1)(2m+3)}x^m.
\]

The ratio of successive coefficients is

\[
 \frac{(2m+1)^2}{2(m+1)(2m+5)}<1.
\]

After twelve terms, the first omitted term divided by
\(1-\overline x\) therefore bounds the positive tail.  The arguments are
formed without a subtraction of nearby radii:

\[
 x_K=\frac{\sigma^2}{2}
 +\frac{\mathrm{shift}\,\sigma^3}{2\kappa},\qquad
 x_\mu=\frac{\mathrm{shift}\,\sigma^3}
 {2\kappa(1-\sigma^2)}.
\]

The exact series root and exact \(A(r)\) enclosure are used uniformly for

\[
 \bigl(f=2,\ n\ge8\bigr)
 \quad\text{or}\quad
 \bigl(f=3,\ n\ge7\bigr),
 \qquad \text{phase}\in\{\text{lower},\text{open}\},
\]

and the corner always uses its exact branch.  This changes only the
enclosure of the same action; no root equation, phase count, or pruning
inequality changes.  At an exact zero gap, the input hull is intersected
with the analytically known half-line \([0,\infty)\) before taking a
square root, so an outward one-ulp negative endpoint cannot create a
false failure.

The sole non-generic subdivision seed is \(\sigma=43/200\) in the
\((f,n,\mathrm{phase})=(2,8,\mathrm{lower})\) call.  It creates two
closed initial boxes with a shared endpoint; both are passed through the
same verifier.  The seed is therefore a queueing device, not an assumed
sign statement, and omits no parameter value.

## 6. Rigorous pruning and terminal scalar

Every early return negates a necessary condition in the favorable
direction.  These include the root-free cutoff, the active-floor test,
the universal upper/slope/width inequalities, the central obstruction
for \(n>48\), the two outer-cone inequalities, and the endpoint floor and
phase tests.

Let

\[
 \Delta=A(r)-A(q),\qquad
 \varepsilon=A(q)+\frac14-f.
\]

The shelf-curvature bound discards a box only when

\[
 2\varepsilon+\Delta+
 \frac{n\Delta}{3(2r+n)}\ge\frac12-\frac1{2n}.
\]

For every surviving leaf, define

\[
 J_R(z)=2\int_z^R G_R(u)\,du,
\]

and evaluate the exact head in gap variables,

\[
 R_n=J_K(r)-J_K(q)-J_\mu(r)+J_\mu(q)-2nf.
\]

The lower head bound is the larger of this directed enclosure and the
independent shelf-curvature lower bound.  The terminal part is bounded by

\[
 \frac\pi2\sum_{k=1}^{L}\frac1{\theta_k}-Q
 -2\int_q^\mu G_\mu(z)\,dz,
\]

where \(L=f-1,f,f\) in the corner, lower, and open phases.  Thirty-two
directed angle steps give the lower angle sum at the lower endpoint of
\(K\); the cap is enclosed from above.  A leaf is accepted only if the
resulting Arb lower endpoint is strictly positive.  Queue priorities and
printed decimal margins have no proof status.

## 7. Exhaustive enumeration

The exact proof domain is

\[
 \{2,3\}\times\{2,\ldots,379\}
 \times\{\text{corner},\text{lower},\text{open}\},
\]

so it contains

\[
 2\cdot378\cdot3=2268
\]

discrete phase cases.  Each case begins with a closed compact box and is
processed by interval subdivision.  The checked limits are 72 levels of
subdivision and 500,000 processed boxes per case; reaching either limit
is a certificate failure, not a pass.

The checked settings are:

\[
 \begin{array}{c|c}
 \text{ordinary action panels}&4\\
 \text{root steps}&12\\
 \text{angle steps}&32\\
 \text{positive-series terms}&12\\
 \text{maximum depth}&72\\
 \text{per-case box cap}&500000
 \end{array}
\]

The \(f=2\) replay uses 384-bit Arb arithmetic.  The independent \(f=3\)
replay uses 512 bits and the exact final source image described in
Section 9.

## 8. Coverage ledger

The exhaustive replay is split only for wall-clock parallelism.  The
following closed ranges form a disjoint partition after duplicate
diagnostic shards are ignored:

\[
\begin{array}{c|l|r}
f&\text{disjoint shard domain}&\text{cases}\\ \hline
2&n=2\ldots26,\ \text{all phases}&75\\
2&n=27\ldots34,\ \text{all};\ (35,\text{corner})&25\\
2&(35,\text{lower/open});\ n=36\ldots51,\ \text{all}&50\\
2&n=52\ldots67,\ \text{all};\ (68,\text{corner/lower})&50\\
2&(68,\text{open});\ n=69\ldots84,\ \text{all};\ (85,\text{corner})&50\\
2&(85,\text{lower/open});\ n=86\ldots101,\ \text{all}&50\\
2&n=102\ldots109,\ \text{all};\ (110,\text{corner})&25\\
2&(110,\text{lower/open});\ n=111\ldots177,\ \text{all}&203\\
2&n=178\ldots245,\ \text{all}&204\\
2&n=246\ldots312,\ \text{all}&201\\
2&n=313\ldots379,\ \text{all}&201\\ \hline
3&n=2\ldots26,\ \text{all phases}&75\\
3&n=27\ldots36,\ \text{all phases}&30\\
3&n=37\ldots42,\ \text{all phases}&18\\
3&n=43\ldots50,\ \text{all phases}&24\\
3&n=51\ldots58,\ \text{all phases}&24\\
3&n=59\ldots80,\ \text{all phases}&66\\
3&n=81\ldots101,\ \text{all phases}&63\\
3&n=102\ldots240,\ \text{all phases}&417\\
3&n=241\ldots379,\ \text{all phases}&417
\end{array}
\]

The row sums are \(1134\) cases for each floor and \(2268\) cases in
total.  A machine parse of the \(f=3\) case records found 1,134 raw and
1,134 unique expected keys, with no missing, extra, duplicated, or
conflicting key.  Independently expanding the \(f=2\) checkpoint domains
above produced exactly the 1,134 expected keys, again with no missing,
extra, or duplicated key.

The ledger is generated from completed case records and asserts that
each triple \((f,n,\mathrm{phase})\) occurs exactly once.  In particular,
there are no missing or duplicated proof cases in the aggregate.

## 9. Replay result and conclusion

The shared core used by the completed \(f\geq4\) replays remains frozen at
`scripts/general_d_no_drop_compact_verify.py` with SHA-256

`EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE`.

Changing that path would make its pinned wrapper and shard launcher refuse
direct replay.  The final low-floor image is therefore checked in under the
separate path `scripts/general_d_no_drop_low_floor_final_verify.py`.  It
replaces, in exactly two places (the endpoint root and \(A(r)\) paths),

```python
f == 2 and n >= 8 and box.phase in {"lower", "open"}
```

by

```python
((f == 2 and n >= 8) or (f == 3 and n >= 7)) and box.phase in {"lower", "open"}
```

and has SHA-256

`4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F`.

This is the exact executed image, not an untested prospective file: the
complete \(f=3\) replay
loaded the frozen source, asserted that exactly two old predicates were
present, made exactly these two in-memory replacements, asserted the
displayed \(4AD4\ldots\) digest, and executed that source.  For \(f=2\)
the new Boolean has exactly the old truth value, so the frozen
\(EEF8\ldots\) replay covers the identical mathematical and arithmetic
branches of the checked-in low-floor image.  Keeping the two paths distinct
therefore preserves direct reproducibility of both the low-floor and the
\(f\geq4\) certificates.

The exact \(f=2\) replay subledger is:

\[
\begin{array}{l|r|r|r|r|l}
\text{domain}&\text{cases}&\text{boxes}&\text{positive}&
 \text{depth}&\text{smallest reported positive}\\ \hline
n=2\ldots26&75&5700618&20687&31&1.7050400932\times10^{-6}\\
\text{middle prefix}&25&1969499&3995&21&6.2878459916\times10^{-5}\\
M1&50&3658642&3468&23&7.4494561070\times10^{-4}\\
M2&50&2617260&1157&23&3.4842773862\times10^{-3}\\
M3&50&1799328&16&23&12.1802306815\\
M4&50&2547464&0&24&\infty\\
\text{high prefix}&25&933321&0&24&\infty\\
R1&203&405129&0&16&\infty\\
R2&204&163694&0&11&\infty\\
R3&201&77125&0&10&\infty\\
R4&201&15069&0&8&\infty
\end{array}
\]

These rows sum to exactly 1,134 cases.  The aggregate replay results are

\[
\begin{array}{c|r|r|r|r|l}
f&\text{precision}&\text{cases}&\text{boxes}&\text{positive}&
 \text{smallest reported positive}\\ \hline
2&384&1134&19887149&29323&1.7050400932319067\times10^{-6}\\
3&512&1134&7695182&10921&2.4999770759192934\times10^{-4}\\ \hline
\text{total}&-&2268&27582331&40244&1.7050400932319067\times10^{-6}
\end{array}
\]

The observed maximum depths are 31 for \(f=2\) and 23 for \(f=3\).
No case reached depth 72 or the 500,000-box cap.  The \(f=3\) replay also
recorded 3,837,237 pruned leaves; every one of its 1,134 case rows obeys
the full-binary-tree identity

\[
 \text{boxes}=2(\text{positive leaves}+\text{pruned leaves})-1,
\]

and every stderr log is empty.  Its phase totals are

\[
\begin{array}{c|r|r|r|r|r}
\text{phase}&\text{cases}&\text{boxes}&\text{positive}&
 \text{pruned}&\text{depth}\\ \hline
\text{corner}&378&133152&5374&61391&13\\
\text{lower}&378&4422822&2521&2209079&23\\
\text{open}&378&3139208&3026&1566767&23
\end{array}
\]

The checkpoint driver did not retain a complete \(f=2\) phase split;
the exact global and disjoint-shard totals above are the proof-relevant
ledger, and no duplicate replay was made merely to reconstruct a
presentation-only statistic.  All runs use python-flint 0.8.0.  The
displayed decimal minima are diagnostics; the proof decision in every
positive leaf is the strict sign of its outward Arb lower endpoint.

Combining this finite certificate with the earlier analytic pieces gives

\[
 \boxed{
 \text{every no-drop branch with }f\in\{2,3\}
 \text{ has }\mathscr S_n>0.}
\]

Indeed, \(n=1\) is direct; \(2\le n\le379\) is divided between the
analytic \(\sigma\le1/10\) theorem and the certificate above; and
\(n\ge380\) forces \(\sigma<1/10\).  This conclusion is deliberately
limited to the two low-floor rows and supplies one finite module in the
general-dimensional shifted-tail program.
