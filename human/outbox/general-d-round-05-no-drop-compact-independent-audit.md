# Independent audit: compact low-floor no-drop certificate

Date: 18 July 2026

Current status:

\[
 \boxed{\text{Proof/code audit passes; }f=3\text{ replay complete, }f=2\text{ pending.}}
\]

This note audits only the two low-floor rows

\[
 f\in\{2,3\},\qquad 2\le n\le379,
\]

in the sector \(\sigma\ge1/10\).  The complementary sector is the
analytic quantitative no-drop transfer.  This is not an audit of the
remaining \(f\ge4\) finite walls.

The checked-in base snapshot audited here is

`scripts/general_d_no_drop_compact_verify.py`

with SHA-256

`EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE`.

The file has 33,458 bytes, compiles in memory, and contains no NUL,
form-feed, carriage-return, or U+FFFD characters.  The definitive
\(f=3\) replay used the exact same source with only the two series-routing
predicates widened as described in Section 6.  The executed in-memory
source had 33,512 bytes and SHA-256

`4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F`.

A final PASS for the complete certificate will be recorded only after all
\(2268\) phase cases finish without a box-limit or depth failure and the
checked-in file is confirmed to equal that executed source.

## 1. Variables and compact localization

The verifier uses

\[
 \sigma=\sqrt{\frac{K-\mu}{K}},\qquad
 \kappa=\sigma(K-\mu)=\sigma^3K,
\]

and

\[
 q=\mu-\alpha,\qquad r=q-n,\qquad
 b=f-\frac14.
\]

On every endpoint wall certified by the interval calculation,
\(A(q)=b\).  Since \(q>0\), one has
\(K-\mu>\pi b>1\).  Hence
\(K-q=(K-\mu)+\alpha<2(K-\mu)\), and the radius-average formula gives

\[
 \frac{2\kappa}{3\pi}\le A(q)<\frac{2\kappa}{\pi}.
\]

Thus the script's common a priori interval

\[
 \frac{21}{8}\le\kappa\le
 \begin{cases}66/7,&f=2,\\99/7,&f=3\end{cases}
\]

contains every compatible endpoint root.  The upper rational endpoints
are strictly larger than \(3\pi f/2\).  The lower endpoint, failed
root-free cutoff \(K<K_{\rm nd}(n,Q)\), and
\(\mu\ge n+1/2\) justify the initial lower and upper \(\sigma\)-cuts.
For \(n>48\), central geometry is already impossible and the certified
outer estimate gives the additional strict bound \(\sigma<38/n\).
Every numerical bisection used to initialize these intervals retains the
excluded endpoint on the computed box, so it cannot create a gap.

## 2. Strict phase combinatorics

The three phase calls have the following exact meaning.

\[
\begin{array}{c|c|c|c|c}
\text{phase}&\alpha&\varepsilon=A(q)+1/4-f&Q&
 \text{retained ball levels}\\ \hline
\text{corner}&0&0&f-1&f-1\\
\text{lower}&0<\alpha<1&0&f-1&f\\
\text{open}&0\le\alpha<1&0<\varepsilon<1/4&f&f
\end{array}
\]

At the corner, \(q=\mu\), the inner cap vanishes and the strict outer
count is exactly \(f-1\).  On the lower wall with \(\alpha>0\), the
inner cap is positive, so the outer ball has at least \(f\) strict
levels although the shell count is \(Q=f-1\).  In the open phase both
counts have at least \(f\) levels.  The code treats the corner separately
and uses \(Q=f-1,f-1,f\) and level counts \(f-1,f,f\), respectively.

The closed interval calculations include \(\alpha=0\) in the lower
phase and \(\alpha=1\) in the latter two phases only as one-sided limits.
The exact-angle expression and cap extend continuously to those limits.
No equality level is silently identified with the value on the other
side of a strict bracket.

## 3. Reduction of the open phase

Fix \((\mu,r)\), hence also \((q,n,\alpha)\), and lower \(K\) inside an
open no-drop chamber.  The complete scalar satisfies

\[
 \partial_K\mathcal S_n
 =\frac2\pi\int_r^K\sqrt{1-z^2/K^2}\,dz>0.
\]

The first shell lower wall encountered is \(A(q)=b\): all earlier
samples are strictly to the left of \(q\), and lowering \(K\) cannot
cross an upper floor.  Therefore a negative open point is dominated by
its open-side endpoint value.  At that endpoint the verifier keeps the
open-side conventions \(Q=f\) and \(f\) ball levels; it does not use the
value of the strict bracket on the equality face.

Along this path \(\sigma=\sqrt{1-\mu/K}\) decreases.  If it reaches
\(1/10\) before the endpoint wall, a hypothetical negative point there
is covered by the analytic \(\sigma\le1/10\) theorem (or by an earlier
necessary-condition exclusion).  Hence it is enough for this interval
certificate to test the endpoint walls with \(\sigma\ge1/10\).

There is no hidden cone assumption in that handoff.  A hypothetical
negative crossing obeys all global necessary conditions.  If \(n>48\),
the certified central obstruction forces \(r>K/2\).  If \(n\le48\),
then \(\sigma\le1/10\), \(K=\delta/\sigma^2\), and
\(\delta>\pi b\) give
\(K/2\ge50\delta>\delta+n+1\), again forcing \(r>K/2\).
The outer inequality \(\delta+1>c_fn\), supplemented by
\(\delta>\pi b\) for the few small \(n\), yields
\(\delta\ge c_fn/2\).  The failed root-free cutoff and the endpoint
action estimate give the remaining upper and lower cubic inequalities
in the quantitative-transfer cone.  Thus every negative crossing is
indeed in the scope of the analytic theorem.

## 4. Ordinary four-panel action enclosure

With \(t=\sigma^2\), \(y=\sigma\,\mathrm{shift}/\kappa\), and
\(v\in[0,1]\), the noncancelling action profile used by the script is

\[
 \Phi(v)=
 \frac{\sqrt{(1-v+y)\{2-(1+v+y)t\}}}{1-vt}.
\]

Its claimed concavity can be checked symbolically without numerical
sampling.  Put

\[
 a=1-v+y,\qquad d=1-vt,\qquad z=\frac ad,
 \qquad \phi(z)=\sqrt{z(2-tz)}.
\]

Then \(\Phi=\phi\circ z\), and physicality gives
\(c=1-t(1+y)\ge0\).  Direct differentiation yields

\[
 z'=-\frac c{d^2},\qquad z''=-\frac{2tc}{d^3},
 \qquad \phi'\ge0,qquad \phi''=-\phi^{-3}<0.
\]

Consequently \(\Phi''\le0\), with endpoint cases obtained by
continuity.  Composite trapezoids are therefore lower bounds and
composite midpoints are upper bounds.  Directed Arb evaluation of the
four panels encloses these two sums for every physical parameter point
in a box.  Clamping a radicand interval at zero only discards
nonphysical interval combinations and enlarges the enclosure of the
physical subset.

At fixed \((\sigma,\alpha)\), after the substitution \(u=\kappa v\),
the unnormalized integrand is

\[
 \frac{\sqrt{\{\kappa(1-v)+X\}
 \{\kappa(2-(1+v)t)-Xt\}}}{1-vt},
 \qquad X=\sigma\alpha.
\]

Both radicand factors are nondecreasing in \(\kappa\), and the integral
is strictly increasing.  The two directed bisections in
`root_kappa_enclosure` therefore give a common lower and upper enclosure
for every endpoint root in the parameter box.  All tests that declare a
root absent use the universal direction; an inconclusive ordinary upper
endpoint is subdivided rather than discarded.

## 5. Exact corner elimination

At the corner, \(q=\mu\) and

\[
 \cos\theta=1-\sigma^2,qquad
 \theta=2\arctan\frac{\sigma}{\sqrt{2-\sigma^2}}.
\]

Writing

\[
 h=\sigma\sqrt{2-\sigma^2}-(1-\sigma^2)\theta,
\]

the equation \(G_K(\mu)=b\) is exactly

\[
 \kappa=\frac{b\pi\sigma^3}{h}.
\]

This is the formula in the corner branch.  Its interval is intersected
with the proved a priori \(\kappa\)-range before any subsequent test.
The stable half-angle formula avoids subtracting an independently
computed arccosine argument.

## 6. Positive series and floor-independent routing

For \(x=\mathrm{gap}/(2R)<1/2\), the script uses

\[
 G_R(R-\mathrm{gap})=
 \frac{8R x^{3/2}}\pi
 \sum_{m\ge0}
 \frac{\binom{2m}{m}}
 {4^m(2m+1)(2m+3)}x^m.
\]

The implemented coefficient recurrence is exact.  Its successive
coefficient ratio is

\[
 \frac{(2m+1)^2}{2(m+1)(2m+5)}<1,
\]

so the omitted positive tail after twelve terms is at most its first
term divided by \(1-\overline x\).  The dimensionless arguments are
formed without radius subtraction:

\[
 x_K=\frac{\sigma^2}{2}
 +\frac{\mathrm{shift}\,\sigma^3}{2\kappa},
 \qquad
 x_\mu=\frac{\mathrm{shift}\,\sigma^3}
 {2\kappa(1-\sigma^2)}.
\]

Thus the difference of the two positive-series Arb values encloses the
exact shell action.  The same monotonicity in \(\kappa\) used above
justifies its root bisection.

The cancellation-free root and \(A(r)\) paths are used for

\[
 ((f=2\ \&\ n\ge8)\ \text{or}\ (f=3\ \&\ n\ge7))
 \quad\text{in the lower and open phases},
\]

plus the exact corner path.  The final routing change is exactly the same
two-line predicate in the root and \(A(r)\) calls.  Both evaluation paths
enclose the same exact action and do not change a root equation, level
count, or pruning inequality.  In particular, an open endpoint continues
to use \(Q=f\) and \(f\) one-sided ball levels.

This method switch is independent of floor combinatorics.  The displayed
series identity is an identity in \((R,\mathrm{gap})\) throughout
\(0\le x<1/2\); its coefficient and tail bounds contain no floor or
strict-bracket convention.  In the root call, \(f\) enters only through
the unchanged target \(b=f-1/4\).  In the \(A(r)\) call, \(n\) enters only
through the unchanged shift \(\alpha+n\).  Selecting the algebraically
identical enclosure by \((f,n)\) can therefore only reduce cancellation;
it cannot alter an endpoint equation or move a case between phases.

For the lower phase, the rational seed \(\sigma=43/200\) divides the
initial interval into two closed boxes with a shared endpoint.  It is a
subdivision seed, not an assumed sign lemma.  The verifier proves every
leaf on both sides.  At the seed, a 512-bit directed check gives

\[
 \underline K=550.2589\ldots>
 \overline K_{\rm nd}(8,1)=445.3922\ldots,
\]

already uniformly in \(\alpha\in[0,1]\); pointwise subdivisions also
exclude the boxes immediately above the seed through the endpoint-floor
test.  More importantly, neither fact is assumed by the code: both
closed seed boxes are sent through the ordinary leaf verifier.  No
interval is omitted at the handoff.

## 7. Endpoint handling at \(x=0\)

An Arb hull whose exact lower endpoint is zero can extend by one outward
ulp below zero.  `g_radius_x` first rejects only an interval whose upper
endpoint is negative or is at least \(1/2\), then intersects the input
with the analytically known half-line \([0,\infty)\).  Its square root
and every subsequent factor therefore enclose the exact endpoint value.
A 512-bit targeted check with \(x\in[0,10^{-3}]\) completed and the
returned action interval contained zero.  The same semipositive handling
is used for exact zero gaps in the cap and corner formulas.

## 8. Pruning directions and scalar

Every terminal status is in the favorable logical direction:

- `cutoff` uses \(K\ge K_{\rm nd}(n,Q)\);
- `active` excludes \((K-\mu)/\pi\le b\);
- `upper-geometry`, `slope-geometry`, and `width-geometry` negate the
  strict necessary residual inequalities;
- `central-box` applies only for \(n>48\) on \(r\le K/2\);
- `outer-width` and `outer-slope` negate the two strict outer necessary
  inequalities on \(r>K/2\);
- `endpoint-floor` and `endpoint-phase` use the strict residual bounds
  \(A(r)<f+1/4\) and \(A(r)+A(q)<2f\);
- `curvature-prune` is exactly Corollary 2.3 with a directed lower
  enclosure of \(\Delta=A(r)-A(q)\).

The exact head is evaluated as

\[
 R_n=J_K(r)-J_K(q)-J_\mu(r)+J_\mu(q)-2nf,
 \qquad J_R(z)=2\int_z^R G_R,
\]

using gap variables.  It is combined with the independent
shelf-curvature lower bound by taking the larger of two directed lower
endpoints.  The terminal bound uses a directed lower angle sum at
\(\underline K\), subtracts the correct \(Q\), and subtracts an upper
cap enclosure.  A leaf is accepted only when the resulting Arb lower
bound is strictly positive.  Queue priorities, printed floating-point
margins, and status counts never enter a proof decision.

## 9. Enumeration and targeted replays

The loops are exactly

\[
 2\ \text{floors}\times378\ \text{values of }n
 \times3\ \text{phases}=2268\ \text{cases}.
\]

There is no diagnostic-mode result in the proof path.  The checked-in
defaults are 384-bit Arb arithmetic, four action panels, twelve root
steps, thirty-two angle steps, maximum depth 72, and a per-case cap of
500,000 boxes.  Exceeding either limit raises `CERTIFICATE FAILURE`.

Lightweight independent replays of the audited snapshot at 512 bits
gave:

\[
\begin{array}{c|c|c|c|c}
(f,n)&\text{phases}&\text{cases}&\text{boxes}&\text{max depth}\\\hline
(2,8)&\text{corner}&1&379&9\\
(3,379)&\text{all}&3&3&0
\end{array}
\]

The corner replay had 113 positive leaves and smallest reported lower
endpoint \(0.0247282287\ldots\).  The \((3,379)\) cases were all removed
by necessary-condition pruning.  The newly widened \((2,8)\) open
series path was replayed independently at 512 bits.  Its topology was
identical to the owner's 384-bit replay: 49,909 boxes, maximum depth 17,
no positive leaves, and every leaf pruned by a rigorous
necessary-condition test before the final scalar.

At 384 bits the two newly added \(n=9\) series-root cases also pass:
the lower phase uses 206,983 boxes at maximum depth 21, while the open
phase uses 48,413 boxes at maximum depth 17.  Both have zero positive
leaves because every leaf is removed by a rigorous necessary-condition
test.

Representative replays of the final uniform \(n\ge8\) predicate at the
native 384-bit precision give:

\[
\begin{array}{c|r|r|c}
n&\text{lower boxes}&\text{open boxes}&\text{maximum depth}\\\hline
10&208243&47787&21\\
20&274625&55147&21\\
48&95331&95331&23\\
49&93971&93971&23
\end{array}
\]

All eight phase cases pass below the fixed 500,000-box cap.  The
\(n=48,49\) corner cases use 1,919 and 1,903 boxes, respectively, with
positive scalar margins.  These representatives test both sides of the
global central cutoff at \(n=48\).

### Complete \(f=3\) replay

The definitive 512-bit \(f=3\) replay used the executed-source hash
`4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F`,
with twelve root steps, four panels, thirty-two angle steps, depth 72,
and a 500,000-box per-case cap.  Because long jobs had no checkpoint
format, interrupted prefixes were retained only through their last
complete `CASE` record.  A separate parser selected the following exact,
pairwise disjoint ledger:

\[
 2{:}26, 27{:}36, 37{:}42, 43{:}50, 51{:}58,
 59{:}80, 81{:}101, 102{:}240, 241{:}379.
\]

It asserted that the selected keys are exactly
\(\{2,\ldots,379\}\times\{\text{corner,lower,open}\}\): 1,134 cases,
no duplicate, no gap, and no extra key.  Every recorded case also obeys

\[
 \text{boxes}=2(\text{positive leaves}+\text{pruned leaves})-1,
\]

which rules out an unreported capped or unresolved leaf.  All nine stderr
logs are empty.  The aggregate is

\[
\begin{array}{c|r|r|r|r|r|l}
\text{phase}&\text{cases}&\text{boxes}&\text{positive}&\text{pruned}
 &\text{depth}&\text{smallest finite lower bound}\\\hline
\text{corner}&378&133152&5374&61391&13&0.0012020968532512127\\
\text{lower}&378&4422822&2521&2209079&23&0.00030504252056230637\\
\text{open}&378&3139208&3026&1566767&23&0.00024999770759192934\\\hline
\text{total}&1134&7695182&10921&3837237&23&0.00024999770759192934
\end{array}
\]

The temporary shard driver itself has SHA-256
`9BF44A486123C4DE1FA029B46B74ED8D0EADEE3ACB76EFEAE170B892612CA1A3`;
it asserts the executed-source hash and all fixed settings before entering
the requested inclusive \(n\)-range.  The independent aggregate parser is
`scripts/_aggregate_no_drop_f3_shards.py`.

## 10. Pending final criterion

No proof or implementation blocker was found in the audited source.  The
earlier ordinary-action failures at \((2,8,\mathrm{open})\) and
\((3,7,\mathrm{lower})\) were box-cap exhaustions, not negative or
unresolved mathematical boxes.  The cancellation-free routing above
resolves both, and the complete \(f=3\) ledger now passes.  This note will
be upgraded to full PASS only after the \(f=2\) replay completes, the
combined 2,268-case aggregate is recorded, and the checked-in verifier is
confirmed byte-for-byte against the executed final source.
