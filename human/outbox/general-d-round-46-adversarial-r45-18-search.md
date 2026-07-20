# Round 46C: adversarial exact-owner search for (R45.18)

**Date:** 21 July 2026  
**Role:** Prompt C independent adversarial search  
**Working branch:** `codex/general-d-round-46-r45-18-complete-owner`  
**Result:** no R45.18 route counterexample, support-entry witness, or Gate-B trigger found  
**Logical strength:** finite diagnostic search only; no positive coverage theorem

## 1. Bottom line

The independent search found no strict reverse of (R45.18).  Across 886,225
distinct discrete proposals, including the mandatory 447,640-proposal
Round-45 box, 833 points survived a 90-decimal reconstruction of every exact
owner condition.  Their results were

| event | exact-owner count |
|---|---:|
| literal R45.18 right-minus-left \(<0\) | 0 |
| exact unprojected \(\mathscr S<0\) | 0 |
| Round-44 support margin \(M_{30}>0\) | 0 |
| Round-45 localized support margin \(M_{30}-7B_0c_0/48>0\) | 0 |
| count-free support margin \(M_{31}>0\) | 182 |

Here \(c_0=\pi^2/(Kt^3\sin t)\).  The \(M_{31}>0\) observations are diagnostics
for the previously rejected count-free support only.  They are not
`support_entry_witness` records under the packet's classification table,
which uses \(M_{30}>0\).

The smallest sampled R45.18 margin occurred at the already audited Round-44
minimum owner

\[
 (r,p,m,f,B,j)=(1,3,1,2,2,0),
\]

where a 768-bit directed replay gives

\[
 \operatorname{R45.18}
 \in 1.7091455068451735356551549621486276130
       \pm 7.21\times10^{-67}>0,
\]

\[
 \mathscr S
 \in 2.6945652789003550256293329147502804303
       \pm 7.55\times10^{-66}>0.
\]

This directed sign certifies that one point, not that it is the global
minimum.  The finite sweep is neither a proof nor a certificate covering the
countably infinite owner.

Accordingly, Prompt C makes no Gate-B status change:

```text
r45_18_route_counterexample : NOT FOUND
support_entry_witness        : NOT FOUND
gate_trigger_certificate     : NOT FOUND
positive_coverage_certificate: FALSE
```

## 2. Preflight, provenance, and independence boundary

All mandatory preflight checks passed before the search.

| item | observed |
|---|---|
| repository | `yutianlee/polya-ai-collab` |
| starting `HEAD` | `3ad6a78d9cb2b81d316bcf0c171ad7cce9f4fee1` |
| Round-45 support commit | `cdfa6a6770207f29b603e18b34526aec1cc8feab`, ancestral |
| proof-obligation SHA-256 | `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4` |
| selected obligation | `SHELL-general-d-high-floor-first-drop-CST : open` |
| audited Round-45 engine SHA-256 | `66e52bbb4e52aafd633f656723e896659f5b090392ca950b68f85a2d263afaf2` |
| Round-45 lead, clean-room, adversarial, and audit artifacts | present, tracked, unchanged from the support commit |

The program directly imports only
`general_d_round45_independent_support_search.py`.  That audited independent
engine transitively owns the Round-44 direct-count definitions.  No
Round-46 lead report, formula implementation, or evaluator was read or
imported while this search was designed and frozen.

There is one source-precedence conflict, already identified in Round 45:
the `next_action` prose in `state/proof_obligations.yml` describes the older
Round-37 route.  Its status is authoritative and remains `open`; the audited
Round-45 directive and the Round-46 packet control this local task.  No
mathematical versions were silently combined.

## 3. Exact owner and quantities evaluated

The evaluator works at the one-sided endpoint

\[
 r\in\mathbb N\cup(\mathbb N_0+\tfrac12),\quad
 x=r+p,\quad q=x+m,\quad \mu=q+1,\quad K=\mu\sec t,
\]

and solves the literal outer wall

\[
 G_K(q)=B-\frac14=B_0+\frac34,\qquad B_0=B-1\ge1.
\]

It then reconstructs the common first shelf, literal first drop, strict
parity-labelled activity, upper-\(\alpha\) label, endpoint correlation
\(0<h<u<\beta<1/2\), and

\[
 p\ge3,\quad m\ge1,\quad q\ge5,\quad
 p-d_\rho m>\frac{11}{5},\quad 0\le E<E_*<\frac12.
\]

The weakest dimension on each parity grid is used: activity constant
\(3/4\) on the integer grid and \(2\) on the half-integer grid.  Activity
equality is rejected as a no-mode owner.

For each exact owner, the terminal count is computed directly.  If \(y_k\)
is defined by

\[
 G_K(q+y_k)=k-\frac14,\qquad 1\le k\le B_0,
\]

then, on a resolved generic old-inverse side,

\[
 T_A(q)=B_0+2\sum_{k=1}^{B_0}\lfloor y_k\rfloor,
\qquad
 D_A(q)=2\{I_K(q)-I_\mu(q)\}-T_A(q),
\]

where

\[
 I_a(z)=\frac{a^2}{4\pi}
 \left[(1+2v^2)\arccos v-3v\sqrt{1-v^2}\right],
 \qquad v=\frac za.
\]

The exact shelf payment is

\[
 \mathcal C_p=
 2\{I_K(r)-I_K(x)-I_\mu(r)+I_\mu(x)\}
 -p\{A(r)+A(x)\},
\]

and the unprojected scalar is always retained:

\[
 \boxed{\mathscr S=D_A(q)+\mathcal C_p+p(E-E_*)}.
\]

The new metric is exactly the requested literal margin

\[
\begin{aligned}
\mathcal M_{46}:={}&pR_1\{A(x)-A(q)\}
+\frac{\pi^2B_0}{Kt^3\sin t}
 \left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)\\
&+B_0\zeta+\frac9{16\beta}-J
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
 \left(\frac1{\sqrt{\mu^2-r^2}}
 -\frac1{\sqrt{K^2-r^2}}\right)
-\frac{p-d_\rho m}{2}.
\end{aligned}
\]

Thus (R45.18) is precisely \(\mathcal M_{46}\ge0\).  No relaxed scalar is
substituted.

The support quantities are evaluated separately:

\[
 M_{30}=p(E_*-E)-
 \left(\Omega_-+B_0\zeta+\frac9{16\beta}-J
 +T_{\rm top}+\mathcal C_{\rm curv}\right),
\]

\[
 M_{31}=p(E_*-E)-
 \left(\frac{49}{40}+T_{\rm top}+\mathcal C_{\rm curv}\right),
\qquad
 M_{45}=M_{30}-\frac{7B_0c_0}{48}.
\]

The classifications are exactly:

| directed signs | classification |
|---|---|
| \(\mathcal M_{46}<0,\ \mathscr S\ge0\) | `r45_18_route_counterexample` |
| \(M_{30}>0\) | `support_entry_witness` only |
| \(\mathscr S<0\) | `gate_trigger_certificate` |
| any positive finite sample | diagnostic only |

## 4. Root uniqueness and directed certification

For fixed exact \((q,B)\), put

\[
 F(t)=G_{(q+1)\sec t}(q)-\left(B-\frac14\right).
\]

Direct differentiation gives

\[
 F'(t)=\frac{\sqrt{K^2-q^2}\tan t}{\pi}>0
 \qquad (0<t<\pi/2).
\]

Consequently every sign-changing rational bracket contains at most one wall
root.  The directed checker evaluates \(F(t_-)\) and \(F(t_+)\) with Arb and
requires \(F(t_-)<0<F(t_+)\).

For every old inverse root,

\[
 \frac d{dy}G_K(q+y)
 =-\frac1\pi\arccos\frac{q+y}{K}<0.
\]

The checker independently chooses rational \(y_{k,-}<y_{k,+}\), verifies

\[
 G_K(q+y_{k,-})>k-\frac14>
 G_K(q+y_{k,+}),
\]

and proves that the entire rational bracket lies in one asserted integer
cell.  It then recomputes the wall, all owner inequalities, \(D_A\),
\(\mathcal C_p\), \(\mathscr S\), \(\mathcal M_{46}\), \(M_{30}\), \(M_{31}\),
and \(M_{45}\) at 768 bits.  The executable prints every rational endpoint
and every directed action sign.

For the four displayed directed records, the resolved inverse cells are:

| record | number of roots | certified cells \([n,n+1]\) in increasing \(k\) |
|---|---:|---|
| Round-44 minimum | 1 | \([3,4]\) |
| Round-45 lead CF witness | 18 | \([59,60],[53,54],[48,49],[43,44],[39,40],[36,37],[32,33],[29,30],[26,27],[23,24],[20,21],[17,18],[14,15],[12,13],[9,10],[7,8],[4,5],[2,3]\) |
| Round-45 clean-room CF witness | 4 | \([14,15],[9,10],[6,7],[2,3]\) |
| Round-45 extended CF witness | 1 | \([35,36]\) |

All brackets are generic: literal and adverse old-inverse side vectors
coincide.  No unresolved collision is admitted to a classification.

## 5. Exact loss ledger and no double counting

Let

\[
 \Omega_{\rm lb}=\frac{c_0}{2}
 \left(\frac{B_0(B_0+1)}2-B_0u\right),
 \qquad
 R_{\rm old}=\frac{7B_0c_0}{48}.
\]

The evaluator checks the exact identity

\[
 \Omega_{\rm lb}+R_{\rm old}
 =B_0c_0\left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)
\]

and the complete loss ledger

\[
\boxed{
\begin{aligned}
 \mathscr S-\mathcal M_{46}={}&
 (\Omega_- -\Omega_{\rm lb})\\
 &+(\mathcal R_{\rm tan}^0-T_{\rm top}-R_{\rm old})\\
 &+(\mathcal C_p-\mathcal C_{\rm curv})\\
 &+p\{E-R_1(A(x)-A(q))\}.
\end{aligned}}
\tag{C46.1}
\]

This also checks the owner identity

\[
 A(x)-A(q)=j+e_p+h.
\]

At the diagnostic minimum the exact payment ledger is:

| term | value |
|---|---:|
| \(\mathcal M_{46}\) | 1.70914550684517353565515496215 |
| \(\Omega_- -\Omega_{\rm lb}\) | 0.357693753087114666898883377003 |
| \(\mathcal R_{\rm tan}^0-T_{\rm top}-R_{\rm old}\) | 0.343778046713804180463882390659 |
| \(\mathcal C_p-\mathcal C_{\rm curv}\) | 0.0216322906894788360952852006164 |
| \(p\{E-R_1(A(x)-A(q))\}\) | 0.262315681564783806516126984324 |
| **sum \(\mathscr S\)** | **2.69456527890035502562933291475** |

The maximum 90-decimal residual in (C46.1) over all 833 owners was
\(5.53\times10^{-87}\).  In each directed record its Arb enclosure contains
zero.  Thus the old Bregman areas, top Bregman interval, shelf curvature,
adjacent action, hinge, and \(1/(16\beta)\) reconciliation are not reused.
The hinge is not added as a second shelf payment, and the reconciliation is
checked but not added as a reserve.

## 6. Search design and stress coverage

### 6.1 Proposal sources

The mandatory baseline is exhaustive over

\[
 r\le16,\qquad p\le40,\qquad m\le20,\qquad B\le20
\]

on both grids, giving exactly 447,640 proposals and 81 exact owners.  It was
augmented by:

1. the audited independent Round-44 wider compact and edge proposal stream;
2. deterministic logarithmic proposals with radius up to about two million,
   \(p\) proposals up to 3000, \(m\) proposals up to 1000, and \(B\) proposals
   up to 512;
3. explicit large-\(B_0\), small-/large-\(t\), large-radius, large-\(p\), and
   \(m=1\) grids; and
4. an independent seed-4603 random stream biased toward those same faces.

The 833 surviving exact owners span

\[
 1\le r\le1{,}919{,}213,\quad
 3\le p\le86,\quad 1\le m\le64,\quad
 2\le B\le512,
\]

\[
 0.02045627668698\ldots\le t\le
 1.55235274340267\ldots.
\]

### 6.2 Stress counts

| stress | exact owners |
|---|---:|
| integer / half-integer grids | 409 / 424 |
| \(B_0=1\) | 259 |
| (B\ge32) | 104 |
| (m=1) | 713 |
| (p\ge20) | 107 |
| (r\ge10^4) | 589 |
| (t<0.1) / (t>1.4) | 408 / 68 |
| (p-d_\rho m-11/5<0.1) | 12 |
| (E_*-E<0.01) | 44 |
| (e_p<0.01) | 123 |
| shelf/drop seam distance (<0.01) | 719 |
| old inverse adverse/literal distance (<0.01) | 79 / 72 |

Every one of the 833 points lies on the exact outer-(B) wall by
construction.  No exact owner in this finite stream approached activity
within one unit; the closest sampled activity margin was
\(113.610405050078\ldots\).  This is reported as a search limitation, not as
an exclusion theorem.

Representative seam diagnostics are:

| face | tuple \((r,p,m,f,B,j)\) | distance | \(\mathcal M_{46}\) |
|---|---|---:|---:|
| \(E\uparrow E_*\) | \((5/2,4,1,2,2,0)\) | \(2.7381932843765\times10^{-4}\) | 2.16206115700720304 |
| \(e_p\downarrow0\) | \((1,6,11,20,18,2)\) | \(9.2466873432188\times10^{-4}\) | 7.81630437557192124 |
| shelf/drop wall | \((3/2,4,16,67,64,3)\) | \(4.6956921733\times10^{-6}\) | 17.7459451853738684 |
| adverse old inverse | \((1,3,16,99,96,3)\) | \(4.5230309781\times10^{-6}\) | 24.0047906396159591 |
| literal old inverse | \((1,4,10,98,96,2)\) | \(2.2714781735\times10^{-4}\) | 22.8923118278218713 |
| \(p-d_\rho m\downarrow11/5\) | \((3/2,3,6,14,13,1)\) | \(3.5283876658\times10^{-3}\) | 5.26566000176706197 |

The smallest half-integer margin was

\[
 \mathcal M_{46}=1.81423757685410753955\ldots
\]

at \((3/2,3,1,2,2,0)\).  Among sampled \(B\ge32\) owners, the minimum was
\(9.14617029468639215\ldots\) at \((1,4,5,33,32,1)\).  These are finite
diagnostics only.

### 6.3 One-sided upper-\(\alpha\) approach

For the minimum, the two independently audited R45-CF witnesses, and both
inverse-side probes, the wall equation was solved again at each
\(\alpha=1-10^{-s}\), \(s=3,6,9,12,18\).  The endpoint value of \(t\) was
never reused.  For example:

| endpoint tuple | \(\mathcal M_{46}\) at \(s=3\) | at \(s=18\) | endpoint value |
|---|---:|---:|---:|
| \((1,3,1,2,2,0)\) | 1.70941183483276173 | 1.70914550684517354 | 1.70914550684517354 |
| \((1,6,11,21,19,2)\) | 8.03366834144545801 | 8.03370213991953715 | 8.03370213991953715 |
| \((3/2,6,7,6,5,1)\) | 4.28483368915305691 | 4.28479691086959619 | 4.28479691086959619 |

Every row retained its one-sided owner.  These sequences diagnose the label
limit only; they do not transport a theorem across an owner jump.

## 7. Main results and directed regressions

### 7.1 Diagnostic extrema

| subset | tuple \((r,p,m,f,B,j)\) | \(\mathcal M_{46}\) | \(\mathscr S\) |
|---|---|---:|---:|
| all / integer / mandatory box / \(B_0=1\) | \((1,3,1,2,2,0)\) | 1.70914550684517354 | 2.69456527890035503 |
| half-integer | \((3/2,3,1,2,2,0)\) | 1.81423757685410754 | 2.97730771069662465 |
| sampled \(B\ge32\) | \((1,4,5,33,32,1)\) | 9.14617029468639215 | 51.0288281307823585 |
| largest sampled \(B\) | \((21/2,3,16,516,512,4)\) | 110.890640228805317 | 803.255980626975803 |
| smallest sampled \(t\) | \((1919213,58,1,2,2,0)\) | 162.405624609092405 | 206.586931114620496 |

The largest \(M_{30}\) and \(M_{45}\) both occur at the first row and remain
strictly negative:

\[
 M_{30}=-2.21759056697508318850\ldots,
 \qquad
 M_{45}=-2.32915494149707200907\ldots.
\]

The largest sampled \(M_{31}\) is
\(5.12492368542172175398\ldots>0\) at
\((1919213,58,1,2,2,0)\).  Again, this is not an \(M_{30}\) support entry.

### 7.2 Required R45-CF regressions

The search independently replays the two audited Round-45 CF failures and
one extended failure.  Each CF sign, R45.18 sign, and exact \(\mathscr S\) sign
is enclosed with the same 768-bit wall/inverse certificate.

| tuple | directed R45-CF margin | directed \(\mathcal M_{46}\) | directed \(\mathscr S\) |
|---|---:|---:|---:|
| \((1,6,11,21,19,2)\) | \(-0.4651636032392523637892\ldots<0\) | \(8.033702139919537153125\ldots>0\) | \(31.79344048770651383674\ldots>0\) |
| \((3/2,6,7,6,5,1)\) | \(-0.1934786069043590635724\ldots<0\) | \(4.284796910869596192875\ldots>0\) | \(10.08910315258892779809\ldots>0\) |
| \((16564,19,1,2,2,0)\) | \(-6.384079805408541740126\ldots<0\) | \(32.51383554819518087745\ldots>0\) | \(45.19657461379293313983\ldots>0\) |

Thus the previously falsified count-free route and the new R45.18 route are
not the same inequality.  The old witnesses do not falsify R45.18.

## 8. Mandatory regression ledger

All required regressions pass.

1. **Round-44 minimum.**  The direct-count engine reproduces
   \[
   \mathscr S(1,3,1,2,2,0)
   =2.6945652789003550256293329147502804303\ldots.
   \]
2. **Round-43 rejected record.**  The tuple \((1,9,9,4,3,1)\) fails only
   the hard owner, with
   \(E-E_*=0.0366505655545844013983\ldots>0\).
3. **Round-27 automatic record.**  The replay gives
   \(\mathscr S=47.13918726007210797057\ldots>47\) and
   \(E-E_*=0.51587812559455914674\ldots>0\), while both historical projected
   scalars remain negative.  These signs are checked independently at 512
   Arb bits.
4. **Old-level coefficient.**  Exact rational arithmetic gives
   \[
   \int_{-3/4}^{1/4}s^2\,ds=\frac7{48}.
   \]
5. **Top coefficient.**  The normalized coefficient reconstructs as
   \(9/64\), with maximum 90-decimal residual \(6.14\times10^{-92}\).  The
   smallest sampled \(\mathcal R_{\rm tan}^0-T_{\rm top}\) is
   \(0.45534242123579300104\ldots>0\).
6. **Ownership reconciliation.**  The maximum residual in
   \(\mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0-1/(16\beta)\) is
   \(8.37\times10^{-88}\); every directed named record encloses zero.
7. **Primary Round-38 \(\Omega_-\) bound.**  The minimum sampled slack is
   \(0.35769375308711466690\ldots>0\), and the inequality is rechecked with
   directed arithmetic on each displayed record.
8. **Round-42 adjacent action.**  The minimum sampled residual
   \(\Delta-R_1\{A(x)-A(q)\}\) is
   \(0.00912788711519350498\ldots>0\); every directed record rechecks it.
9. **Round-45 identities.**  The maximum action-drop, aggregate, and full
   loss-ledger residuals are respectively \(1.29\times10^{-84}\),
   \(1.53\times10^{-88}\), and \(5.53\times10^{-87}\).

Items 1, 4, and the algebraic coefficient identities are exact-definition or
exact-rational replays.  The displayed named signs are directed
certificates.  Extrema over the finite sample remain diagnostics.

## 9. Equality-face and side audit

| face | treatment |
|---|---|
| \(A(r+s)+1/4\in\mathbb Z\) | Strict floor convention is retained.  An unresolved shelf collision is rejected rather than transported.  No exact shelf collision was promoted. |
| \(G_K(q)+1/4=B\) | This is the rationally bracketed outer wall.  \(B\) is the one-sided old-chart label and the literal endpoint count is \(B_0=B-1\). |
| \(A(q)+1/4\in(B-1,B)\) | Recomputed directionally, giving the direct shell endpoint count \(Q=B_0\). |
| old inverse wall | One fixed componentwise side vector is used in the direct count, \(\Omega_-\), and both terminal ledgers.  All named roots are generic and cell-bracketed; exact collisions are not silently admitted. |
| newest \(y_B=0\) event | Owned once by the literal top interval and never counted as an old inverse root. |
| \(e_p=0\) | The finite search approaches from the exact hard owner; no equality point was found.  No continuity claim is made. |
| \(E=E_*\) | Assigned to the automatic sector; only strict \(E<E_*\) points are searched. |
| activity equality | Assigned to the no-mode owner and rejected here. |
| R45.18/support equality | Equality belongs to the nonnegative side; classifications require directed strict signs. |
| \(B_0=1\) | Included explicitly, with 259 exact owners. |
| both parity grids | Included with the weak dimension-labelled activity constants; 409 integer and 424 half-integer owners survived. |
| \(\alpha\uparrow1^-\) | Walls are re-solved separately at each \(\alpha\).  No endpoint value is reused and no reindexing as the next \(\alpha=0\) chart occurs. |

The absence of an exact activity, shelf, or inverse collision in the finite
stream is not a theorem about those faces.

## 10. Dependency ledger

The evaluator uses only the following audited dependencies.

1. The independent Round-45 definition engine for the exact endpoint owner,
   direct strict count, cap primitive, \(\mathcal C_p\), \(\mathscr S\),
   \(M_{30}\), \(M_{31}\), and fixed old-inverse convention.
2. The exact Round-45 action-drop identity and \(7/48\) old-level theorem,
   replayed rather than assumed numerically.
3. The primary Round-38 \(u\)-retaining \(\Omega_-\) lower bound.
4. The Round-44 \(9/64\) top Bregman reserve and exact literal terminal
   decomposition.
5. The Round-42 adjacent-action inequality, used only in the loss-ledger
   regression.
6. The Round-27, Round-43, Round-44, and Round-45 named records as regression
   data.

No asymptotic formula, new ratio ladder, \(B_0\)-indexed theorem, chamber
family, second compact certificate, or Round-46 lead result enters a sign
classification.

## 11. What is and is not established

### Directed conclusions

- The four displayed records are strict exact owners with rigorously unique
  and bracketed wall/inverse roots.
- The Round-44 minimum record has positive R45.18 margin.
- Both independent Round-45 CF counterexamples and the extended CF witness
  have positive R45.18 margin and positive exact \(\mathscr S\).
- No emitted record is a support entry or Gate trigger.

### Limitations

1. The 833 exact owners are a finite sample of an infinite discrete owner.
2. No global monotonicity or global minimizer theorem is supplied.
3. No exact activity or shelf/inverse collision was found; nearby generic
   owners do not replace an equality-face proof.
4. The positive minimum is diagnostic even though its own sign is directed.
5. This adversarial artifact neither proves nor falsifies (R45.18).  The
   analytic Prompt-A/Prompt-B work and final independent audit must make the
   packet's Gate-B decision.  This report does not authorize another
   pointwise round.

No proof-obligation status should change on the basis of Prompt C.

## 12. Reproduction, hashes, and files modified

From the repository root:

```powershell
python -B computations/general_d_round46_independent_r45_18_search.py --dps 90 --random 15000
```

The full run prints all 886,225 proposal classifications, exact-owner and
stress counts, every diagnostic extremum, all mandatory regressions, every
one-sided sequence, and complete directed rational wall/inverse brackets for
the named records.

Prompt C created only:

- `computations/general_d_round46_independent_r45_18_search.py`
- `human/outbox/general-d-round-46-adversarial-r45-18-search.md`

No lead, clean-room, state, proof-graph, manuscript, prompt, or completed d3
file was modified.
