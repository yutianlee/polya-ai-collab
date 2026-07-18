# General dimension, Round 8: high-floor no-drop root localization

Date: 18 July 2026

Status: rigorous repair and stress test of the root-localization layer for
the residual no-drop floors $f\ge 4$.  The repaired driver certifies the
complete retained $f=4$ floor: 38 integer pairs and all 114 one-sided phase
chambers.  It also certifies the localization handoff on every one of the
$156{,}160$ initial lower/open parameter boxes belonging to the full list of
$610$ retained integer pairs.

This note does **not** claim closure of all $1{,}830$ phase chambers.  The
complete scalar replay is still pending.  No manuscript file and no frozen
low-floor verifier is changed here.

## 1. Certified discrete scope

The driver

```text
scripts/general_d_no_drop_high_floor_compact_verify.py
```

first replays `general_d_no_drop_exhaustion_verify.py`.  It asserts the
following prerequisite counts before it starts any chamber computation:

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]

and hence

\[
 \#(\mathcal C\cup\mathcal O)=610.
\]

Here every pair has $f\ge4$ and $n\ge2$.  Each pair has the corner,
lower-wall, and open one-sided phases, for a final intended replay of

\[
 3\cdot610=1{,}830
\]

phase chambers.

## 2. Coverage of the whole sigma interval

Use the standard critical variables

\[
 \sigma=\sqrt{\frac{K-\mu}{K}},\qquad
 \kappa=\sigma(K-\mu),\qquad
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3}.
\]

There is no small-$\sigma$ transfer in this high-floor driver.  Instead, the
root-free cutoff and the universal lower endpoint bound give

\[
 K<K_{\rm nd}(n,Q),\qquad \kappa\ge\frac{21}{8}.
\]

Thus every residual point satisfies

\[
 K_{\rm nd}(n,Q)\sigma^3\ge\frac{21}{8}.
\]

Forty exact-rational bisections retain an overlap endpoint with the already
positive cutoff face and give the lower endpoint $\sigma_0$.

At the other end, the audited endpoint estimate gives

\[
 \kappa<\frac{3\pi f}{2}<\frac{33f}{7}=:\kappa_{\max}(f).
\]

Physicality $r\ge1/2$, hence $\mu\ge n+1/2$, implies

\[
 \frac{33f}{7}\frac{1-\sigma^2}{\sigma^3}
 \ge n+\frac12.
\]

Another forty directed bisections retain an overlap endpoint with the
impossible physical face and give $\sigma_1<1$.  Consequently the box audit
on $[\sigma_0,\sigma_1]$ covers every possible point with $0<\sigma<1$.

## 3. Why the original pilot proliferated

On a lower or open wall, the root equation is

\[
 A(q;\sigma,\kappa,\alpha)=f-\frac14,
 \qquad q=\mu-\alpha,
 \qquad 0\le\alpha\le1.
\]

At fixed $(\sigma,\alpha)$, the scaled positive integral proves strict
increase in $\kappa$.  The frozen low-floor routine therefore starts a common
$\kappa$-bisection at $21/8$.

That starting value is harmless in the low floors but inappropriate for a
wide high-$\sigma$ box.  Some such parameter boxes contain points for which the
formal value at $\kappa=21/8$ has $q\le0$, even though every relevant high-floor
root lies much higher.  The exact positive-gap series is intentionally not
evaluated there.  The old pilot therefore returned `split`, and the outer
queue repeatedly subdivided along this irrelevant $q=0$ boundary.  For
$f=4,n=2$, the first $5{,}000$ processed boxes already contained
$2{,}850$ unresolved root statuses and exceeded the cap.

## 4. Certified interior seed

For each floor define the deterministic rational candidate

\[
 \boxed{\kappa_*(f)=\frac{13}{6}\left(f-\frac14\right).}
\]

This displayed formula is **not** assumed to lie below the root.  On every
parameter box the driver first proves both

\[
 q(\sigma,\kappa_*,\alpha)>0
\]

and the directed inequality

\[
 \overline A(\sigma,\kappa_*,\alpha)
 <f-\frac14.                                      \tag{1}
\]

Only after (1) succeeds is $\kappa_*$ accepted as a common strict lower bound for
all roots in that box.  Failure returns `split`; it cannot produce a false
root enclosure.

The separate `--seed-audit` mode applies this test to the fixed initial grid
of sixteen $\sigma$ panels and eight $\alpha$ panels for both the lower and open phase of
all 610 retained pairs.  Thus it checks exactly

\[
 610\cdot2\cdot16\cdot8=156{,}160
\]

seed boxes.  At both 384 and 512 bits it proves

\[
 \min\left(f-\frac14-\overline A(\kappa_*)\right)
 >0.7133461216573367
\]

and

\[
 \min q(\kappa_*)>0.07717803029630899.
\]

The decimals are downward endpoint diagnostics printed only after the Arb
sign assertions have succeeded.  They are not used in a proof decision.

## 5. Two independent action enclosures

The localization layer intersects two independently rigorous enclosures of
(A(q)).

1. The exact gap-series evaluation gives an Arb interval
   $[L_{\rm ex},U_{\rm ex}]$.
2. The noncancelling scaled integral has a concave profile.  Composite
   trapezoid and midpoint rules give the directed enclosure
   $[L_{\rm tr},U_{\rm mid}]$.

The driver uses

\[
 \boxed{
 L=\max(L_{\rm ex},L_{\rm tr}),\qquad
 U=\min(U_{\rm ex},U_{\rm mid}).}                 \tag{2}
\]

Both parent intervals contain the same exact action, so their intersection
does also.  A nonfinite representation is simply omitted; if neither
representation succeeds, the box is split.  A disjoint intersection is a
certificate failure.

This combination matters on the wide seed boxes: the gap-series form is
usually sharp after subdivision, while the noncancelling integral avoids a
large dependency width at the initial handoff.

## 6. Root enclosure logic

Let $T=f-1/4$.  Once (1) has certified $\kappa_*$ below every root, put

\[
 a=\kappa_*,\qquad b=\kappa_{\max}(f)=\frac{33f}{7}.
\]

Twelve directed bisections use only the following implication:

\[
 U(A(m))<T\quad\Longrightarrow\quad
 m\text{ lies below every root in the parameter box}.
\]

This produces a common lower root endpoint.  For the upper endpoint, if

\[
 L(A(b))>T,
\]

twelve reverse directed bisections use

\[
 L(A(m))>T\quad\Longrightarrow\quad
 m\text{ lies above every root in the parameter box}.
\]

If the common upper test at $b$ is inconclusive, $b$ itself is retained
as a safe a priori upper enclosure for every root that exists in the box.
If $U(A(b))<T$, there is no root and the box is pruned.

No monotonicity in $\sigma$ or $\alpha$ is assumed.  The only monotonicity
used by this root bisection is the already audited strict increase in
$\kappa$ at fixed $(\sigma,\alpha)$.

The corner phase does not invoke this routine: at $\alpha=0$ the equation
$A(q)=f-1/4$ eliminates $\kappa$ exactly by the stable half-angle formula in the
shared core.

## 7. Replays completed

The formerly obstructed representative at 384 bits now reports:

| pair and phase | processed boxes | positive leaves | max depth | smallest accepted scalar endpoint |
|---|---:|---:|---:|---:|
| $f=4,n=2$, corner | 44 | 8 | 4 | $0.8967109946638809$ |
| $f=4,n=2$, lower | 5,102 | 1,616 | 10 | $0.011041079794933836$ |
| $f=4,n=2$, open | 5,726 | 1,754 | 10 | $0.00002144211613601797$ |

The 512-bit lower/open replays have the same box counts, depths, and
accepted endpoint diagnostics.

Additional 384-bit stress tests report:

| selected pair, all three phases | processed boxes | max depth | smallest accepted scalar endpoint |
|---|---:|---:|---:|
| $f=4,n=39$ | 47,270 | 14 | $0.010374015346279027$ |
| $f=8,n=25$ | 16,832 | 12 | $2.6631806869895427$ |
| $f=49,n=48$ | 18,726 | 15 | all leaves pruned before the scalar test |

Finally, the complete frozen-wrapper replay

```text
python -u scripts/general_d_no_drop_high_floor_compact_verify.py --f 4 --precision 384 --max-boxes 500000 --verbose
```

certifies every retained pair $n=2,\ldots,39$ and every phase on the
$f=4$ floor.  Its exact summary is

```text
PASS: requested residual f>=4 no-drop scope certified
precision=384; pairs=38; cases=114; boxes=618898; positive=15362;
max-depth=14; smallest=2.144211613601797e-05
```

Thus 114 of the intended 1,830 high-floor phase cases now have a completed
full-floor replay.  The remaining full-replay ledger contains 572 pairs and
1,716 phase cases.

The commands for the principal replays are

```text
python scripts/general_d_no_drop_high_floor_compact_verify.py --precision 384 --seed-audit
python scripts/general_d_no_drop_high_floor_compact_verify.py --precision 512 --seed-audit
python scripts/general_d_no_drop_high_floor_compact_verify.py --f 4 --n 2 --phase lower --precision 384 --max-boxes 50000
python scripts/general_d_no_drop_high_floor_compact_verify.py --f 4 --n 2 --phase open  --precision 384 --max-boxes 50000
```

## 8. Frozen boundary and remaining work

The high-floor wrapper has SHA-256

```text
5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F
```

at the time of this note.  The shared low-floor verifier remains unchanged
at

```text
EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE
```

The remaining obligation is operational but essential: run the other
$1{,}716$ phase chambers and audit the combined $1{,}830$-case result,
preferably in disjoint shards with a machine-checked
$(f,n,\text{phase})$ coverage ledger.  Until that replay is complete, these
results certify the root-localization method and the listed chambers, not
the entire $f\ge4$ no-drop theorem.
