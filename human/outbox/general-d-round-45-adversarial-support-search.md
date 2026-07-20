# Round 45C: adversarial exact-owner support search

**Date:** 20 July 2026

**Working branch:** `codex/general-d-round-45-support-sign`

**Classification:** directed counterexamples to the count-free sufficient route; no support-entry witness and no Gate-B trigger found

**Gate consequence:** the count-free route (R45-CF) is false, but Gate B is not stopped

## 1. Bottom line

The count-free contradiction margin is not nonnegative on the complete exact
owner.  A 640-bit directed enclosure certifies, for example, the exact owner

\[
 (r,p,m,f,B,j)=(1,6,11,21,19,2),
\]

which lies inside the mandatory baseline, with

\[
 \operatorname{CF}
 \in -0.4651636032392523637892280292332878743
       \pm 3.18\times10^{-58}<0.
\]

Its full exact scalar is nevertheless

\[
 \mathscr S
 \in 31.79344048770651383674441216942422635
       \pm 4.71\times10^{-54}>0.
\]

This is a `count_free_route_counterexample` only.  It is not a
`gate_trigger_certificate` and does not falsify the Round 44 support theorem,
the endpoint sign, CST, or the all-dimensional theorem.

The finite search found:

- no \(\mathscr S<0\) exact owner;
- no \(M_{30}>0\) support-entry witness;
- no \(M_{31}>0\) count-free-support witness; and
- 81 high-precision candidates with a negative count-free contradiction
  margin, of which representative integer-baseline, extended-integer, and
  extended-half-integer points were certified with directed arithmetic.

The positive observations are diagnostics, not coverage.  In particular,
this report does not prove support emptiness or \(\mathscr S\geq0\) on the
continuum.

## 2. Provenance and status boundary

The repository checks required by the Round 45 packet passed before the
search:

| item | observed |
|---|---|
| `main` and starting `HEAD` | `52738525ab0ee360c54f237a5a4fe314caa51e79` |
| audited Round 44 artifact ancestral | `2a0e51ecbb1534eeea94615ab94717fa126c0c5d` |
| proof-obligation SHA-256 | `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4` |
| selected obligation | `SHELL-general-d-high-floor-first-drop-CST : open` |
| Round 44 lead and final audit | present, tracked, unchanged |

No status is promoted here.  The general-dimensional branching backbone
remains `derived_under_assumptions`, the weighted aggregate and target remain
`proposed`, and the selected high-floor first-drop obligation remains `open`.

### 2.1 Source-precedence resolutions

1. The narrative `next_action` inside `state/proof_obligations.yml` lags the
   independently audited Round 44 route.  Its statuses are authoritative;
   the later Round 44 audit and the Round 45 packet control this search.
2. Round 36 excludes the literal value \(\alpha=1\), while the higher
   precedence packet requires evaluation of the endpoint geometry
   \(\mu=q+1\) with the old chart's upper-\(\alpha\), gap-side labels.  The
   evaluator follows the packet and does not reindex the point as the next
   chart's literal \(\alpha=0\) owner.
3. The old-inverse convention is fixed once per record.  At a literal old
   inverse wall the strict convention is \(\eta_k=1\); on the adverse side it
   is \(\eta_k\downarrow0\).  Every retained search point had all inverse
   roots strictly inside generic cells, so the literal and adverse vectors
   coincide there.  No unresolved collision was admitted as an exact owner.
4. The weakest parity-grid activity constants were used: \(3/4\) on the
   integer grid, corresponding to dimension four, and \(2\) on the
   half-integer grid, corresponding to dimension five.  This is the packet's
   authorized weakest-grid enlargement: every enumerated shift on either
   grid is realized in its weakest dimension.  Activity equality is rejected
   as the no-mode owner.

No incompatible mathematical version was silently combined.

## 3. Exact quantities and classification discipline

The evaluator keeps the unprojected target

\[
 \boxed{\mathscr S=D_A(q)+\mathcal C_p+p(E-E_*)}.
\]

It separately forms

\[
\begin{aligned}
 M_{30}:={}&p(E_*-E)\\
 &-\left(
 \Omega_-+B_0\zeta+\frac9{16\beta}-J
 +\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}
 +\mathcal C_{\rm curv}
 \right),
\end{aligned}
\]

\[
 M_{31}:=p(E_*-E)-
 \left(
 \frac{49}{40}
 +\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}
 +\mathcal C_{\rm curv}
 \right),
\]

where

\[
 \mathcal C_{\rm curv}
 =\frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-
 \frac1{\sqrt{K^2-r^2}}
 \right),
\]

and the signed count-free contradiction margin

\[
\begin{aligned}
 \operatorname{CF}:={}&pR_1h+\frac{49}{40}
 +\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}
 +\mathcal C_{\rm curv}
 -\frac{p-dm}{2}.
\end{aligned}
\]

Thus (R45-CF) is exactly \(\operatorname{CF}\geq0\).  The classifications
used by the executable are:

| directed sign | allowed classification |
|---|---|
| \(M_{30}>0\) | `support_entry_witness` only |
| \(M_{31}>0\) | count-free support entry only |
| \(\operatorname{CF}<0\) | `count_free_route_counterexample` only |
| \(\mathscr S<0\) | `gate_trigger_certificate` |

No projected scalar replaces \(\mathscr S\).

## 4. Independent evaluator and exact owner

The Round 45 program imports only the audited independent Round 44
definition engine, not the Round 45 lead evaluator.  It independently adds
the four Round 45 margins, their exact loss decompositions, the Round 38
primary \(\Omega_-\) bound, and the Round 42 adjacent-action replay.

For each proposed \((2r,p,m,B)\), it solves

\[
 G_{(q+1)\sec t}(q)=B-\frac14
\]

and then discovers the shelf floor.  The direct strict terminal count is

\[
 T_A(q)=Q+2\sum_{k=1}^{B_0}[y_k]_<,
 \qquad Q=B_0=B-1,
\]

so

\[
 D_A(q)=2\{I_K(q)-I_\mu(q)\}-T_A(q).
\]

No tangent lower bound is substituted for \(D_A(q)\).  The shelf curvature
is evaluated from the analytic cap primitive,

\[
 \mathcal C_p=
 2\{I_K(r)-I_K(x)-I_\mu(r)+I_\mu(x)\}
 -p\{A(r)+A(x)\}.
\]

Every high-precision owner satisfies:

- integer \(r=1,2,\ldots\) or half-integer
  \(r=3/2,5/2,\ldots\);
- \(p\ge3\), \(m\ge1\), \(q\ge5\);
- common first shelf and a literal first drop at \(x+1\);
- \(B_0=B-1\ge1\), \(j=f-B\ge0\);
- \(0\le E<E_*<1/2\) and \(p-dm>11/5\);
- strict parity-labelled activity;
- \(0<h<u<\beta<1/2\);
- the exact outer-wall bracket and direct strict endpoint count; and
- one fixed, resolved old-inverse side vector used in \(D_A(q)\),
  \(\Omega_-\), \(L_T^0\), and \(L_T^+\).

The directed witness checker encloses the wall root by rational endpoints,
encloses every inverse root with a separately signed action bracket, proves
that each inverse hull remains in its asserted integer cell, and then
recomputes every strict owner condition and scalar with Arb balls.

## 5. Search scope

The mandatory baseline was exhaustive over the specified discrete box:

\[
 r\le16,\qquad p\le40,\qquad m\le20,\qquad B\le20,
\]

using both parity grids.  It contains exactly 447,640 distinct proposals.
Focused and deterministic-random proposals then stressed \(B_0=1\), small
\(m\), large \(p\), large radius, and inverse/shelf seams.

| source | distinct proposals | exact owners | high-precision \(\operatorname{CF}<0\) candidates |
|---|---:|---:|---:|
| mandatory baseline | 447,640 | 81 | 23 |
| focused extras | 35,640 | 10 | 6 |
| deterministic random extras | 7,271 | 58 | 52 |
| **total** | **490,551** | **149** | **81** |

All 149 binary64 owner proposals survived the 90-decimal exact-definition
rebuild.  They split into 87 integer-grid and 62 half-integer-grid owners;
60 have \(B_0=1\).  Their retained diagnostic ranges were

\[
 1\le r\le19351.5,\qquad 3\le p\le19,\qquad
 1\le m\le12,\qquad 2\le B\le32.
\]

The smaller ranges of the surviving baseline owners are a consequence of
the exact owner screen, not a cutoff: \(1\le r\le4.5\),
\(3\le p\le6\), \(1\le m\le12\), and \(2\le B\le20\).

All final decimal values use 90 decimal digits.  Named classifications use a
640-bit full-owner Arb replay; the rational outer-wall endpoint signs are
also independently checked at 512 bits.

## 6. Main search results

### 6.1 Counts and extrema

| event | high-precision count |
|---|---:|
| exact owners | 149 |
| \(\mathscr S<0\) | 0 |
| \(M_{30}>0\) | 0 |
| \(M_{31}>0\) | 0 |
| \(\operatorname{CF}<0\) | 81 |

The observed full-scalar minima are

| grid | tuple \((r,p,m,f,B,j)\) | \(\mathscr S\) |
|---|---|---:|
| integer | \((1,3,1,2,2,0)\) | 2.69456527890035502562933291475 |
| half-integer | \((3/2,3,1,2,2,0)\) | 2.97730771069662464599676336623 |

These are finite diagnostics only.  The integer minimum reproduces the
audited Round 44 minimizing tuple.

The largest observed support margins remain negative:

\[
 \max M_{30}=-2.21759056697508318849657805557
\]

at \((1,3,1,2,2,0)\), and

\[
 \max M_{31}=-0.397488850662773833196764\ldots
\]

at \((r,p,m,f,B,j)=(19351.5,10,1,2,2,0)\).  Consequently no sampled point
entered either necessary support.

### 6.2 Directed count-free-route counterexamples

Three representative points were promoted from high-precision candidates to
directed classifications.  The baseline point shows that the route already
fails inside the mandatory compact box; the half-integer point verifies that
the phenomenon is not confined to one parity.

| label | tuple \((r,p,m,f,B,j)\) | grid | \(\operatorname{CF}\) | \(M_{30}\) | \(M_{31}\) | full \(\mathscr S\) |
|---|---|---|---:|---:|---:|---:|
| extended minimum | \((16564,19,1,2,2,0)\) | integer | -6.38407980540854174013 | -40.0685132772533337257 | -2.25569639835305193947 | 45.1965746137929331398 |
| mandatory baseline | \((1,6,11,21,19,2)\) | integer | -0.465163603239252363789 | -30.3752666367479963625 | -1.64750941652520571502 | 31.7934404877065138367 |
| half-integer stress | \((12632.5,17,1,2,2,0)\) | half-integer | -5.50816027924379287436 | -36.4547981593792804682 | -2.11024568770597904411 | 41.1283698813983332600 |

The full directed intervals have radii at most \(8\times10^{-50}\) for
\(\mathscr S\), \(9\times10^{-51}\) for \(M_{30}\), and
\(5\times10^{-57}\) for \(\operatorname{CF}\).  Every owner inequality is
strict in the corresponding Arb replay.

## 7. Complete payment ledgers for the route failures

The literal-wall ledger is

\[
 \mathscr S=
 \Omega_-+B_0\zeta+\frac9{16\beta}-J
 +\mathcal R_{\rm tan}^0+\mathcal C_p-p(E_*-E).
\]

Every term for the three directed route witnesses is printed below.

| term | extended integer | mandatory baseline | half-integer |
|---|---:|---:|---:|
| \(\Omega_-\) | 6.45862540335759420171 | 25.7020404491686633846 | 5.87207411244351195494 |
| \(B_0\zeta\) | 14.8537652207457032344 | 3.00471779122154879049 | 13.4978426908288790945 |
| \(9/(16\beta)\) | 17.7272905172395537603 | 1.30118232760493780092 | 16.2017701581289244770 |
| \(-J\) | -0.00186426244256941021 | -0.0551833477723593286 | -0.00213448972801410231 |
| \(L_T^0\) | 39.0378168789002817862 | 29.9527572202227906474 | 35.5695524716733014241 |
| \(\mathcal R_{\rm tan}^0\) | 5.78958511447608734818 | 1.41013343590755955447 | 5.29188059106646700074 |
| \(D_A(q)\) | 44.8274019933763691344 | 31.3628906561303502019 | 40.8614330627397684249 |
| \(\mathcal C_p\) | 0.422388915196863341394 | 0.484245907030988042916 | 0.360709517107199473669 |
| \(-p(E_*-E)\) | -0.0532162947802993359824 | -0.0536960754548244080722 | -0.0937726984486346385118 |
| **\(\mathscr S\)** | **45.1965746137929331398** | **31.7934404877065138367** | **41.1283698813983332600** |

There is no hidden projection in this table: its sum is the direct-count
\(\mathscr S\).

### 7.1 Which discarded reserves restore positivity?

For the count-free route, the executable verifies the exact bookkeeping
identity

\[
\boxed{
 \mathscr S=\operatorname{CF}
 +\left(D_A(q)-\frac{49}{40}-\mathcal R_{\rm top}\right)
 +(\mathcal C_p-\mathcal C_{\rm curv})
 +p(E-R_1h),}
\]

where

\[
 \mathcal R_{\rm top}=
 \frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}.
\]

The restoration ledger is:

| term | extended integer | mandatory baseline | half-integer |
|---|---:|---:|---:|
| \(\operatorname{CF}\) | -6.38407980540854174013 | -0.465163603239252363789 | -5.50816027924379287436 |
| \(D_A-49/40-\mathcal R_{\rm top}\) | 42.7576855404695888353 | 30.1312432874806370812 | 38.8643076161937344719 |
| \(\mathcal C_p-\mathcal C_{\rm curv}\) | 0.183192674970292365113 | 0.0146877837006710405388 | 0.153816577498619743970 |
| \(p(E-R_1h)\) | 8.63977620376159367959 | 2.11267301976445807881 | 7.61840596694977191847 |
| **sum** | **45.1965746137929331398** | **31.7934404877065138367** | **41.1283698813983332600** |

The first limitation of (R45-CF) is therefore concrete: replacing the exact
terminal defect by the count-free constant and replacing the actual shelf
payment \(pE\) by \(pR_1h\) simultaneously discard large positive reserves.
The exact terminal reserve is dominant in all three witnesses, and the
actual-\(E\) reserve is also substantial.  No parameter partition can repair
the asserted universal sign of (R45-CF); the packet requires returning to the
exact support ledger instead.

For completeness, none of the route witnesses enters the Round 44 support:
their \(M_{30}\) values are all strictly negative.  They therefore say
nothing adverse about the localized exact Gate-B route.

## 8. Old-inverse sides and seam probes

The closest sampled adverse and literal old-inverse sides were:

| probe | tuple \((r,p,m,f,B,j)\) | distance | \(\mathscr S\) | directed status |
|---|---|---:|---:|---|
| adverse | \((1,4,12,19,17,2)\) | \(\min\eta_k=0.00374091469016513104\) | 32.8959393453278892242 | exact generic cell, \(\mathscr S>0\) |
| literal | \((17074,7,1,7,7,0)\) | \(\min(1-\eta_k)=0.00129774773812522813\) | 105.571902725137093063 | exact generic cell, \(\mathscr S>0\) |

For both points the complete side vector is used consistently in the direct
count, \(\Omega_-\), and both terminal decompositions.  The directed inverse
brackets remain strictly inside their cells, so neither point is silently
treated as an exact inverse collision.

Other focused seams were:

| seam | tuple | observed distance | \(\mathscr S\) |
|---|---|---:|---:|
| lower shelf \(e_p\downarrow0\) | \((1,6,11,20,18,2)\) | \(e_p=0.000924668734321876279\) | 32.5594096195586622129 |
| hard seam \(E\uparrow E_*\) | \((5/2,4,1,2,2,0)\) | \(E_*-E=0.000273819328437651309\) | 4.15536923294885410495 |

No exact simultaneous shelf/inverse/activity collision was found.  A
near-collision is only a diagnostic probe; without an exact wall identity it
cannot stand for either one-sided collision owner.

## 9. Separate one-sided \(\alpha\uparrow1\) checks

For every reported one-sided sequence the wall equation was solved again at
each \(\alpha=1-10^{-s}\); the endpoint value of \(t\) was not reused.  The
outer action fixes the same \(K\) from \((q,B)\), but \(t=\arccos(\mu/K)\)
changes with \(\alpha\).

### 9.1 Extended integer route failure

| \(s\) | separately solved \(t\) | \(\operatorname{CF}\) | full \(\mathscr S\) |
|---:|---:|---:|---:|
| 3 | 0.0990809388892305256159473893 | -6.38467074899865536006 | 45.1970143125414953229 |
| 6 | 0.0990803329391834793448339622 | -6.38408039659119737417 | 45.1965750535062250991 |
| 9 | 0.0990803323332315836010471668 | -6.38407980599972463481 | 45.1965746142326464463 |
| 12 | 0.0990803323326256317034546711 | -6.38407980540913292302 | 45.1965746137933728531 |
| 18 | 0.0990803323326250251456051792 | -6.38407980540854174072 | 45.1965746137929331403 |

### 9.2 Mandatory-baseline route failure

| \(s\) | separately solved \(t\) | \(\operatorname{CF}\) | full \(\mathscr S\) |
|---:|---:|---:|---:|
| 3 | 1.346106471914232826279664180 | -0.465248626038319040145 | 31.7972519079372510229 |
| 6 | 1.346094454399301563968474969 | -0.465163688286281192496 | 31.7934442992322271745 |
| 9 | 1.346094442381770111978334968 | -0.465163603324299416844 | 31.7934404915180396556 |
| 12 | 1.346094442369752580509823765 | -0.465163603239337410842 | 31.7934404877103253626 |
| 18 | 1.346094442369740550960823769 | -0.465163603239252363874 | 31.7934404877065138406 |

The half-integer and both inverse-side probes were subjected to the same
five separately solved checks.  Every displayed sequence retained its exact
owner, stayed positive in full \(\mathscr S\), and converged to the endpoint
values above.  These are one-sided diagnostics, not transport across an
owner jump.

## 10. Mandatory regressions

All seven Prompt C regressions pass.

1. **Round 44 minimum.**  The independent replay gives
   \[
   \mathscr S(1,3,1,2,2,0)
   =2.6945652789003550256293329147502804303\ldots,
   \]
   agreeing with the audited value to \(4.31\times10^{-34}\) using the
   printed Round 44 truncation and much more closely with its full internal
   value.
2. **Round 43 rejected tuple.**  At
   \((1,9,9,4,3,1)\),
   \[
   E-E_*=0.03665056555458440139830776829633625\ldots>0.
   \]
   The hard-owner condition is its only rejection.
3. **Round 27 automatic witness.**  The replay gives
   \[
   \mathscr S=47.13918726007210797057112078239874\ldots,
   \qquad E-E_*=0.51587812559455914674\ldots>0,
   \]
   while the two historical projected scalars remain negative.  Their signs,
   \(\mathscr S>47\), and \(E>E_*\) are rechecked at 512 Arb bits.
4. **Ownership reconciliation.**  Across all 149 owners,
   \[
   \max\left|
   \mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0-\frac1{16\beta}
   \right|<1.90\times10^{-89}.
   \]
   Named directed enclosures contain zero.
5. **Top-Bregman coefficient.**  Reconstructing the normalized coefficient
   gives \(9/64\) with maximum 90-digit residual
   \(3.07\times10^{-92}\).  The smallest observed
   \(\mathcal R_{\rm tan}^0-\mathcal R_{\rm top}\) is
   \(0.4553424212357930010\ldots>0\), and named directed witnesses verify
   the same inequality.
6. **Primary Round 38 \(\Omega_-\) bound.**  The minimum observed slack in
   the \(u\)-retaining bound (R38.22) is
   \(0.3576937530871146669\ldots>0\).  It is also checked directionally on
   every named witness.
7. **Round 42 adjacent action.**  The minimum observed strict residual
   \[
   \Delta-R_1(j+e_p+h)
   \]
   is \(0.03078856773158031963\ldots>0\).  Each directed classification
   rechecks this strict sign as part of owner certification.

The top-Bregman reserve and old-level Bregman areas are never double counted.
Likewise, \(\mathcal C_{\rm curv}\) and the hinge lower bound are never added
as two independent shelf payments.  The \(1/(16\beta)\) reconciliation is
checked exactly once and is not added as a third reserve.

## 11. What this does and does not establish

### Directed conclusions

- (R45-CF) is false on exact owners, including one owner inside the mandatory
  baseline and owners on both parity grids.
- The displayed failures have positive full \(\mathscr S\), negative
  \(M_{30}\), and negative \(M_{31}\).  They falsify only the sufficient
  count-free route.
- The discarded exact terminal payment and actual \(E-R_1h\) payment explain
  the route failure quantitatively.

### First limitations

1. The finite sweep does not cover the continuum and cannot prove support
   emptiness, even though no sampled point has \(M_{30}>0\).
2. No exact old-inverse collision was found.  The search certifies nearby
   generic cells but does not replace a theorem for literal/adverse equality
   faces.
3. No globally directed maximizer of \(M_{30}\), \(M_{31}\), or
   \(-\operatorname{CF}\) is claimed; only named points have directed
   classification certificates.
4. The search does not derive the aggregate old-level inequality requested
   after failure of the count-free route.  That is an analytic obligation for
   the lead and clean-room attempts.

Accordingly:

```text
count_free_route_counterexample : CERTIFIED
support_entry_witness            : NOT FOUND (diagnostic only)
gate_trigger_certificate         : NOT FOUND
positive_coverage_certificate    : NOT AUTHORIZED
Gate B                           : NOT STOPPED BY THIS SEARCH
```

The exact next Gate-B task is to retain \(\Omega_-\) and all old-level
Bregman areas on the Round 44 support and derive one aggregate shelf-terminal
sign or contradiction, without a count-, floor-, ratio-, or chamber-indexed
theorem family.

## 12. Reproduction and files

From the repository root:

```powershell
python -B computations/general_d_round45_independent_support_search.py --dps 90
```

The executable prints the complete payment ledger and every inverse row for
each named route witness, the directed rational wall and inverse brackets,
all owner signs, the mandatory regressions, and the separately solved
one-sided sequences.

Files created by Prompt C:

- `computations/general_d_round45_independent_support_search.py`
- `human/outbox/general-d-round-45-adversarial-support-search.md`

No state, manuscript, lead, or clean-room file was modified.  No commit was
created.
