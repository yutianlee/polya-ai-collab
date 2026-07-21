# Round 49 Prompt-D independent audit

Date: 2026-07-21

## Verdict

    STRUCTURAL PASS — FINAL SIGN OPEN

The audit was performed only after Prompts A--C were frozen. The following
SHA-256 values were independently reproduced:

| artifact | SHA-256 |
|---|---|
| Prompt-A report | 7cd92a5e002c7d63c4ccbf01a57ceade6aa51b913fd1ecbddd2b76fbbed38b89 |
| Prompt-B report | 63c86de6d4e26cb897f3aa8853898e19e33f8e497a95d96902bd763757755dc7 |
| Prompt-C report | b4047a245ea0cfee5fc612b23899e9c02e03fa333b5b857e8fdc64c3b31d643d |
| Prompt-A evaluator | a1e5a09a99efd8d14c0dff56f0e07fbdb2de99d2902ae90522f643ee46c7892b |
| Prompt-C evaluator | 5b463a893fc3ccdf7fa8e0ba21b79f6d91bf70e08dd24fd0bdf2c9c5d9b9d658 |

The authoritative state blob and SHA-256 match the packet preflight. The
clean-room rendered-prefix freeze hash also reproduces as

    f4fffae307a7258fa8dcccd4648006b49ceccf5b7e0742a5e25e4f60c5902c64

## Repair verification

The first independent final review found two evidence-level defects. They
were repaired before this fresh re-audit:

1. At \(b=0\), \(\widehat F''(s)=O(s^{-4/3})\) need not be locally
   integrable by itself. But \(P_1(s)=s^2/2\), so
   \(P_1\widehat F''=O(s^{2/3})\) is integrable. Under an
   \(\varepsilon\)-cutoff,
   \[
   P_1(\varepsilon)\widehat F'(\varepsilon)=O(\varepsilon^{5/3}),
   \qquad
   P_1'(\varepsilon)\widehat F(\varepsilon)=O(\varepsilon),
   \]
   and the omitted supply is \(O(\varepsilon)\). PBLOCK survives unchanged.
2. Uncommitted separate-sign Peano records are now floating diagnostics.
   The displayed cumulative-majorization parent values are also diagnostic;
   only the exact rational inequality certifies the CM counterexample.

The fresh re-audit requires no further repair.

## Fifteen determinations

### 1. Exact theorem and reductions

The following are proved exactly:

- the inverse-layer identity and outer-prefix/suffix split
  \[
  \mathrm{WT}_4=\sum_{n=1}^{b}L_n+\mathcal R_{\rm suf},
  \qquad b=\lfloor A(\mu)\rfloor;
  \]
- the normalized inverse and spatial suffix forms NSFX and SSFX;
- exact interface ownership IF and terminal ownership TOP;
- ROW1--ROW3, their terminal analogue, and the exact row block RBLOCK;
- the weighted-trapezoid and Abel identities;
- the complete composite Peano identity PBLOCK; and
- the one-crossing theorem: \(Q=2\sigma-z\sigma'\) has exactly one zero in
  \((\mu/\sqrt2,\mu)\), with \(Q>0\) below it and \(Q<0\) above it.

The natural cumulative radial-prefix strengthening CM is exactly falsified.

### 2. R49

R49 is neither proved nor falsified on the complete strict-active domain.

### 3. R49-FB

The fallback is neither proved nor falsified.

### 4. Literal \(\mathrm{WT}_4\)

Literal \(\mathrm{WT}_4\) is neither proved nor falsified. No class-A
counterexample was found; finite positive searches have no continuum
implication.

### 5. Integral interface height

The split is exact at \(\tau\in\mathbb Z\). Then
\(b=\tau\), \(R=\mu\), and the cell \(n=b\) ends at the interface within
the certified full-outer scope \(n\le\tau\). No node is omitted or
duplicated. If \(b=0\), the prefix is empty and
\(\mathcal R_{\rm suf}=\mathrm{WT}_4\).

### 6. Terminal equality

At \(\alpha=3/4\), the terminal node is correctly excluded. Its node height
equals the strict support wall, while a terminal node occurs only when

\[
 q+\frac34<q+\alpha.
\]

### 7. Strict ceilings

Every strict ceiling is retained:

\[
 M_k=\lceil\eta(k-1/4)\rceil-1.
\]

An integer inverse radius \(r\) therefore contributes \(r-1\); integer
\(R\) and \(K\) are excluded from their strict spatial sums; and an integer
action wall takes the lower bracket value.

### 8. Interface row

The interface is confined exactly to the first normalized row, since

\[
 B(\mu)=\tau-b\in[0,1).
\]

When \(q=0\), the interface-row and terminal-row descriptions name the same
row and it is counted once.

### 9. Scope of the Round 48 lemmas

The certified full-outer lemma is applied only to complete cells
\(1\le n\le b\). The deep-inner lemma is used only for complete rows
satisfying

\[
 b+k-1\ge A(\mu/\sqrt2).
\]

It is never extended to a shallow, interface, partial, or terminal row.

### 10. Continuous quarter-node counterexample

The Round 48 counterexample is respected. Its directed negative continuous
margin and positive literal discrete margin are independently reproduced.
No Round 49 identity replaces literal \(S_2(M)\) by the rejected continuous
polynomial \(p(\eta)\).

### 11. Sufficiency versus equivalence

R49 and R49-FB are correctly reported as sufficient, not equivalent, to
literal \(\mathrm{WT}_4\). The fallback discards strict positive
full-outer-cell gaps. For \(b\ge1\),

\[
 \mathrm{WT}_4>
 \mathcal R_{\rm out}+\mathcal R_{\rm suf},
\]

while \(b=0\) gives equality.

### 12. Computation classification

The evidence classes are correct after repair:

- deterministic mpmath sweeps are floating-point experiments;
- the committed two-precision Arb replays certify only their named
  individual signs and ownership ledgers;
- uncommitted separate-sign Peano and parent values are diagnostics;
- the exact \(C_{512}(B)\) failure is an analytic rational proof; and
- no positive finite sweep is continuum coverage.

The required declaration is retained:

    positive_coverage_certificate: FALSE

### 13. First unrepaired implication

The first open implication is OPEN49: sign the exact PBLOCK boundary ledger,
terminal contribution, and weighted curvature term,

\[
\begin{aligned}
&\sum_{k=1}^{q}C_k
+\mathbf1_{\{\alpha>3/4\}}C_{\rm top}
+\mathbf1_{\{\alpha\le3/4\}}
  \int_q^{q+\alpha}\widehat F(s)\,ds\\
&\qquad
+\int_0^{\widehat H}P_{\rm blk}(s)\widehat F''(s)\,ds\ge0.
\end{aligned}
\]

The one-crossing theorem localizes the adverse curvature to one shallow
interval, but does not pay its weighted negative mass from the literal
boundary scalars and retained outer/deep/top reserves. CM cannot close this
step because CM is exactly false.

### 14. Proof-obligation statuses

No status changes are justified:

| obligation | status after Round 49 |
|---|---|
| SHELL-general-d-weighted-aggregate-d4 | proposed |
| SHELL-general-d-weighted-aggregate | proposed |
| SHELL-general-d-branching-backbone | derived_under_assumptions |
| TARGET-shell-general-d | proposed |
| Round 48 full-outer cell | proved_internal |
| Round 48 deep-inner cell | proved_internal |
| TARGET-shell-d3 | proved_internal |

The authoritative state file is not edited.

### 15. Next single obligation

Prove or falsify a cumulative Peano-kernel compensation theorem signing
OPEN49 uniformly on the complete strict-active domain, retaining the first
interface row, exact terminal row, literal ceiling ledger, and positive
deep-inner reserve, without reintroducing CM or a count/floor/chamber family.

## Final implication

Round 49 achieves the packet's substantive partial-success criterion through
exact suffix normalization, PBLOCK, and the proved one-crossing theorem. It
does not close Gate B: the final suffix sign remains open.

Accordingly:

    R49: neither proved nor falsified
    R49-FB: neither proved nor falsified
    literal WT4: neither proved nor falsified
    general-dimensional theorem: unproved
    completed d=3 theorem: unchanged
    proof-obligation status changes: none
