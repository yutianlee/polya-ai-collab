# Independent audit: high-floor no-drop root localization and shard architecture

Date: 18 July 2026

## Verdict

The verdict has three separate parts.

1. **PASS -- mathematical and interval-certificate architecture.**  The
   reduction to 610 retained pairs, the full \(\sigma\)-interval
   localization, the high-floor root enclosure, every directed
   rounding decision, and the deterministic shard partition are valid.
2. **PASS -- completed partial certificates.**  The reported complete
   \(f=4\) replay is correctly interpreted as 38 pairs and 114 phase
   chambers.  The current pinned verifier also independently passes the
   \((f,n)=(49,48)\) smoke case in all three phases.
3. **PENDING -- complete \(f\ge4\) theorem.**  The eight-shard scalar replay
   is not complete.  A shard log without its final `PASS shard=...` line is
   partial evidence only, and there is not yet a combined 1,830-row ledger.

One stale, non-proof diagnostic in the root-localization note must be
corrected: the current pinned wrapper processes 18,726, not 19,142, boxes
for \((f,n)=(49,48)\).  All those leaves are still rigorously pruned, so this
does not change a theorem or a certificate status.

## 1. Audited snapshot

The principal files have the following SHA-256 hashes.

```text
high-floor wrapper
5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F

shared compact core
EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE

shard launcher
A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092

exhaustion verifier
81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A

root-localization note
C94E0BF7CFA58F4B452AA59123C0207D3564A00EC1F6C590B40DD92AB13EC51D

shard-plan note
D179B1043D0A7F061BACB6235800ED602D8036A6C46E9B8FDB4DC5F88FF65D13
```

All four Python sources compile in memory.  They contain no NUL, carriage
return, form-feed, or U+FFFD characters.  No frozen verifier, wrapper,
launcher, or manuscript file was changed during this audit.

## 2. Exhaustion and the exact discrete ledger

The wrapper replays the outward-Arb exhaustion certificate before doing any
chamber calculation.  After removing the already proved \(n=1\) sector and
restricting to \(f\ge4\), its lists are

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]

and hence

\[
 \#(\mathcal C\cup\mathcal O)=610.
\]

An independent replay reproduced these exact counts.  The union runs from
\((4,2)\) to \((49,48)\); in particular, the complete \(f=4\) row is exactly
\(n=2,\ldots,39\), containing 38 pairs.  The exhaustion tests both possible
endpoint counts \(Q=f-1\) and \(Q=f\).  Taking the union of its central and
outer necessary lists is therefore conservative and loses neither side of
the geometric split \(r\le K/2\) or \(r>K/2\).

For each retained pair the three calls are exactly

\[
 \{\text{corner},\text{lower},\text{open}\}.
\]

They encode, respectively, the codimension-two corner, the noncorner lower
wall with its one-sided \(f\)-level ball count, and the open chamber reduced
monotonically to the same action wall while retaining the open-side count.
The closed occurrences of \(\alpha=0,1\) in the interval boxes are one-sided
limits; the actual corner is separately certified.  Thus the intended
ledger contains exactly

\[
 610\cdot3=1,830
\]

phase chambers, with no missing strict-floor face.

## 3. Full \(\sigma\)-localization

Put

\[
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3}.
\]

Every residual point has \(K<K_{\rm nd}(n,Q)\) and
\(\kappa\ge21/8\).  Therefore

\[
 K_{\rm nd}(n,Q)\sigma^3>\kappa\ge\frac{21}{8}.
\]

The lower bisection advances only when the Arb *upper* endpoint proves the
strict reverse inequality.  Its returned \(s_0\) is consequently still on
the already closed cutoff side, so retaining \(s_0\) creates overlap and
cannot create a gap.

The endpoint-action estimate gives

\[
 \kappa<\frac{3\pi f}{2}<\frac{33f}{7}=\kappa_{\max}(f).
\]

Physicality gives \(\mu\ge n+1/2\).  Hence a residual point must satisfy

\[
 \frac{33f}{7}\frac{1-\sigma^2}{\sigma^3}>n+\frac12.
\]

This exact upper function is strictly decreasing on \((0,1)\).  The upper
bisection retreats only after its Arb upper endpoint proves physicality
impossible, and it returns that first impossible point \(s_1\).  Retaining
\(s_1\) again gives overlap.  If \(s_1\le s_0\), no point can satisfy both
necessary inequalities.  Thus \([s_0,s_1]\) contains every possible
residual parameter with \(0<\sigma<1\); no small-\(\sigma\) transfer is being
assumed.

All 610 pairs have nonempty returned intervals in all three phases.  Forty
exact-rational bisections affect efficiency only: no approximate root is
ever substituted into a proof inequality.

## 4. High-floor endpoint root enclosure

For the lower and open phases the target is

\[
 T=f-\frac14,
\]

with the phase combinatorics kept one-sided.  At fixed
\((\sigma,\alpha)\), the noncancelling scaled integral proves that
\(A(q)\) is strictly increasing in \(\kappa\): after scaling the radius
integral, both radicand factors are affine increasing functions of
\(\kappa\).  No monotonicity in \(\sigma\) or \(\alpha\) is used.

The deterministic seed

\[
 \kappa_*(f)=\frac{13}{6}\left(f-\frac14\right)
\]

is not assumed to be below a root.  On each parameter box the production
routine first proves

\[
 q(\kappa_*)>0,\qquad
 \overline A(\kappa_*)<T.
\]

Because \(\mu\) decreases with \(\sigma\), increases with \(\kappa\), and
\(q=\mu-\alpha\), the endpoint test at
\((\sigma,\alpha)=(s_1,a_1)\) is the correct universal positivity test.
Failure returns `split`; it never discards a root.

The action is enclosed in two rigorous ways:

1. the positive gap series for the exact two-radius action;
2. the noncancelling concave profile, with composite trapezoids below and
   composite midpoints above.

Taking the larger lower endpoint and the smaller upper endpoint is a valid
intersection because both intervals contain the same exact action.  A
nonfinite enclosure is omitted, two failed enclosures cause subdivision,
and a disjoint intersection is a certificate failure.

The lower root bisection advances only under

\[
 \overline A(m)<T,
\]

which puts \(m\) below every root in the parameter box.  The reverse upper
bisection retreats only under

\[
 \underline A(m)>T.
\]

If the common upper endpoint is inconclusive, the a priori ceiling itself
is retained.  It is a safe outer enclosure of every root that exists in the
box.  If its upper action endpoint is below \(T\), monotonicity certifies
that no compatible root exists.  Thus every direction is conservative.

The reported complete 384- and 512-bit seed audits check

\[
 610\cdot2\cdot16\cdot8=156,160
\]

lower/open seed boxes.  Their positive margins are far from zero.  As an
independent targeted replay at 512 bits, both extreme retained pairs passed:

```text
(f,n)=(4,2):   256 boxes; min seed margin 0.7172645791935441;
               min q 0.07717803029630899
(f,n)=(49,48): 256 boxes; min seed margin 11.622780311602556;
               min q 21.176677489044884
```

The corner does not need a numerical root: the stable half-angle identity
eliminates \(\kappa\) exactly and then intersects its directed image with
the same proved a priori interval.

## 5. Directed scalar and termination logic

The high-floor wrapper changes only the domain localization and the action
enclosures.  It retains the audited core's exact phase counts, necessary
geometry prunes, shelf-curvature prune, gap-variable head, exact-angle
terminal payment, and cap subtraction.

Every early terminal status negates a strict necessary condition in the
safe direction.  In particular:

- `cutoff` requires a directed proof of \(K\ge K_{\rm nd}\);
- `active`, `upper-geometry`, `slope-geometry`, and `width-geometry`
  negate the corresponding strict residual inequalities;
- the central and outer returns are used only on their proved geometric
  sides;
- `endpoint-floor`, `endpoint-phase`, and `curvature-prune` use directed
  lower enclosures of the relevant exclusion quantities;
- a surviving leaf is accepted only when the Arb lower endpoint of the
  combined head-plus-terminal scalar is strictly positive.

The positive-series remainder is bounded by its first omitted positive
term divided by \(1-\overline x\), with \(\overline x<1/2\).  Exact-zero
gap hulls are intersected with the analytically known nonnegative half-line
before square roots.  The angle bisection evaluates the angle sum at a
directed lower endpoint of \(K\), hence in the lower-payment direction; the
inner cap is subtracted using an upper enclosure.

Twelve root steps, thirty-two angle steps, sixteen initial
\(\sigma\)-panels, eight initial \(\alpha\)-panels, depth 72, and the
500,000-box per-case cap are certificate-resolution settings, not assumed
error tolerances.  An unresolved depth or a box-cap overrun raises failure.
Printed decimal margins and heap priorities have no proof role.

## 6. Shard partition and live-log audit

The current `--plan-only` replay reproduces all eight published assignment
digests.  The residue-class rule on lexicographically sorted ordinals
\(0,\ldots,609\) is an exact partition: shards 0 and 1 have 77 pairs each,
and shards 2 through 7 have 76 pairs each.  Keeping all three phases of a
pair together gives

\[
 2\cdot231+6\cdot228=1,830
\]

case rows.  The launcher asserts that its flattened pair assignments have
610 distinct entries and equal the exhaustion union exactly.

The launcher pins the wrapper and core hashes before running.  It emits a
row only after `verify_high_case` has exhausted that phase without a depth
or box-cap failure, and prints the shard `PASS` only after all assigned rows
finish.  Its normalized coverage hash includes ordinal, floor, shelf
length, and phase.

A snapshot of the live shard-0 log had no malformed, duplicated, or
unexpected case row.  Every completed row obeyed the exact forest identity

\[
 \text{boxes}=2(\text{positive}+\text{pruned})-I,
\]

where \(I=16\) for a corner and \(I=128\) for a lower/open phase.  The log
had no final shard PASS at the audited snapshot and is therefore not counted
as completed coverage.

## 7. Completed replays and the stale smoke count

The reported full \(f=4\) output is

```text
PASS: requested residual f>=4 no-drop scope certified
precision=384; pairs=38; cases=114; boxes=618898; positive=15362;
max-depth=14; smallest=2.144211613601797e-05
```

This is correctly interpreted.  The selected pair set is exactly
\(\{(4,n):2\le n\le39\}\), and the wrapper reaches this PASS line only after
all three phases of all 38 pairs terminate.  There are 10,336 initial
forests in those 114 calls; the aggregate therefore corresponds to 314,617
terminal leaves, of which 15,362 are positive and 299,255 are rigorously
pruned.  The independently visible \((4,2)\) rows reproduce the published
44, 5,102, and 5,726 box counts.

The current pinned wrapper was independently rerun on the last retained
pair.  It gives

```text
CASE f=49 n=48 phase=corner boxes=56 positive=0 pruned=36 depth=7
CASE f=49 n=48 phase=lower  boxes=9352 positive=0 pruned=4740 depth=15
CASE f=49 n=48 phase=open   boxes=9318 positive=0 pruned=4723 depth=15
PASS: requested residual f>=4 no-drop scope certified
precision=384; pairs=1; cases=3; boxes=18726; positive=0; max-depth=15
```

The normalized three-row coverage digest is

```text
A86C355BF27E865B420BBBB140BCA06C17B865CC19EF665FDA901437DBABD8E6
```

Thus the root-localization note's table entry `19,142` is stale.  The
correct total for the pinned source is `18,726`.  The intended conclusion
-- all three smoke chambers are removed by rigorous necessary-condition
pruning before a positive scalar leaf is needed -- is unchanged.

## 8. Requirements before a global PASS

The following are essential before claiming the full \(f\ge4\) no-drop
sector.

1. Every intended shard log must end with its own `PASS shard=...` line.
2. A final parser must read exactly 1,830 unique
   \((\text{ordinal},f,n,\text{phase})\) rows, with no extra or conflicting
   row, and compare their pair projection with the exact 610-pair exhaustion
   union.
3. It should verify all per-case forest identities and record that every
   stderr log is empty.
4. The final aggregate should record the exhaustion-verifier hash shown in
   Section 1.  The current launcher pins the wrapper and core but does not
   pin the exhaustion script itself.  This is not a defect in a run made
   against the unchanged file, because every row records its exact ordinal,
   pair, and phase and the final comparison can reconstruct the union.  It
   is nevertheless important certificate hardening against assignments
   being generated from different exhaustion snapshots.
5. The current PowerShell-produced shard log is UTF-16.  A final parser must
   decode the actual log encoding rather than silently treating it as UTF-8.

Until those conditions are met, the architecture and the listed completed
chambers pass, while the combined 1,830-chamber replay remains **PENDING**.
