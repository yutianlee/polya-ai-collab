# Simplification review of Sections 4.7 and 4.8

## Verdict

**A stronger compact theorem eliminates the aggregate branch entirely.**

Parts VII--IX already prove, without using the declared upper cutoff
\(K\leq200\), that
\[
 N_D(A_{\rho,1},K^2)
 \leq P_{\rm coarse}(\rho,K)<W(\rho,K)
\]
for
\[
 \rho_c\leq\rho\leq\frac{39}{50},
 \qquad K\geq k_{11}(\rho).
\]
The proof is upward monotone in \(K\); \(200\) occurs only in the historical
definition of the compact region, not in an estimate.

Consequently the exact residual
\[
 \mathcal D_{20}
 =\left\{\rho_c\leq\rho<\frac{39}{50},\
 k_{11}(\rho)<K<U(\rho)\right\}
\]
is contained in one analytic theorem domain.  The full discrete
\(\mathcal Q\)-bridge, continuous \(\mathcal B\)-propagation, split at
\(K=200\), and the names
\(\mathcal C_{21},\mathcal T_{21},\mathcal D_{21}\) are not needed in the
logical proof of the spherical-shell theorem.

This review applies to:

- **manuscript/spherical-shell-polya-proof.tex**, SHA-256
  **84D079A9FD3A6001C7F00A528F7EAF40799D6850E87537BDC3819A98A9F6D982**;
- Section 4.7, main lines 3674--4039;
- Section 4.8, main lines 4041--4079.

No main-manuscript or support-source edit was made.  The stronger theorem
should be stated explicitly and independently audited before the aggregate
branch is actually removed.

## 1. Critical audit: where is \(K\leq200\) used?

### Part VII: structural reduction

The only displayed \(K\leq200\) restriction in
**compact-structural.tex** is the historical region declaration at lines
75--86.  None of the subsequent arguments uses it.

- Lines 53--58 define the action for every \(0<\rho<1\), \(K>0\).
- Lines 88--148 prove the action and inverse-curvature properties for every
  such pair.
- Lines 161--235 prove the exact layer cake and angular defect globally.
- Lines 270--360 prove the exact retained-remainder identity globally.
- Lines 367--423 construct the global primitive minorant.
- Lines 428--460 prove
  \[
  \mathcal E_{\rm ang}<\mathcal H
  \Longrightarrow P_{\rm coarse}<W
  \]
  without an upper bound on \(K\).

The sentence at lines 425--426 that the expression is smooth on the compact
residual is descriptive.  Every formula is pointwise smooth for finite
\(K>0\); no compactness theorem or uniform upper-\(K\) estimate is used.

**Conclusion for Part VII:** global in \(K>0\).

### Part VIII: angular blocks

The main angular estimate is explicitly global.

- **compact-angular-block.tex**, lines 56--90, proves
  \(0\leq q\leq1/2\) for every \(0<\rho<1\), \(K>0\).
- Lines 288--330 prove the strict one-layer estimate, including every common
  radial--angular wall.
- Lines 332--380 state and prove
  \[
  \mathcal E_{\rm ang}
  <\frac{(1-\rho^2)K^2}{6}-\frac N2
  \]
  for every \(0<\rho<1\), \(K>0\) with \(N\geq1\).
- The restricted region appears only at lines 392--398.
- Lines 400--406 verify \(N\geq1\) from
  \[
  T\geq\frac{(1-\rho)k_{11}(\rho)}{\pi}
  =\sqrt{1+\frac{132(1-\rho)^2}{\pi^2}}>1.
  \]
  This calculation remains valid, with the same strictness, for every
  \(K\geq k_{11}(\rho)\).

Thus for the unbounded domain
\[
\rho_c\leq\rho\leq39/50,\qquad K\geq k_{11}(\rho),
\]
Part VIII gives
\[
\mathcal E_{\rm ang}
<M_c(\rho,K):=
\frac{(1-\rho^2)K^2}{6}-\frac12.
\]

**Conclusion for Part VIII:** global for \(K\geq k_{11}\).

### Part IX: scalar positivity

This is the decisive check.  In **compact-scalar-positive.tex**, the spectral
number \(200\) occurs as an upper cutoff only in the declared region at lines
57--61.  The occurrence \(17/200\) at line 467 is a rational coefficient, not
a spectral cutoff.

Every proof step uses only a lower bound on \(K\):

1. Lines 124--195 prove the exact \(\mathcal J_K\) identity for \(K>0\) and
   the uniform loss estimate for every \(K>12\).  The beta-integral bound
   decreases as \(K\) increases.
2. Lines 197--288 prove
   \[
   \partial_K\mathcal S(\rho,K)>0.
   \]
   The proof uses only \(K>12\) and
   \(\rho\in[\rho_c,39/50]\).  The final sign is the positive Bernstein
   polynomial at lines 253--286; it contains no upper-\(K\) term.
3. Lines 293--321 prove from
   \(K\geq k_{11}(\rho)\) that
   \[
   K>\frac{241}{20}>12.
   \]
   This lower bound becomes stronger, not weaker, as \(K\) increases.
4. Lines 332--410 prove the uniform boundary-layer loss estimate using the
   same lower bound.  No upper cutoff appears.
5. Lines 413--635 concern only the base curve
   \(K=k_{11}(\rho)\).  Lines 527--635 prove
   \[
   \mathcal S\bigl(\rho,k_{11}(\rho)\bigr)>0
   \]
   throughout the closed ratio interval.
6. Lines 637--642 integrate the positive \(K\)-derivative upward from the
   base curve.  That integration has no mathematical endpoint at \(200\).

Therefore, for every finite \(K\geq k_{11}(\rho)\),
\[
\mathcal S(\rho,K)
\geq\mathcal S\bigl(\rho,k_{11}(\rho)\bigr)>0.
\]
At \(K>k_{11}\) the first comparison is itself strict; at
\(K=k_{11}\) strictness is supplied by the base theorem.

No appeal to topological compactness is hidden here: the monotonicity is a
pointwise differential inequality and is integrated over the finite segment
\([k_{11}(\rho),K]\).

**Conclusion for Part IX:** the stated theorem strengthens from
\(k_{11}\leq K\leq200\) to all \(K\geq k_{11}\).

## 2. The genuinely simplifying new lemma

The useful new statement is not a new estimate but the correct unbounded
form of the already proved scalar theorem.

### Upward-closed scalar-gap lemma

For
\[
\rho_c\leq\rho\leq\frac{39}{50},
\qquad K\geq k_{11}(\rho),
\]
one has
\[
\mathcal S(\rho,K)>0.
\]

Its proof is exactly:
\[
\mathcal S_K>0
\quad\text{for }K>12,
\qquad
k_{11}(\rho)>\frac{241}{20}>12,
\qquad
\mathcal S(\rho,k_{11}(\rho))>0.
\]

Combining this with Parts VII and VIII gives the stronger module theorem.

### Global middle-ratio analytic theorem

For
\[
\rho_c\leq\rho\leq\frac{39}{50},
\qquad K\geq k_{11}(\rho),
\]
one has
\[
N_D(A_{\rho,1},K^2)
\leq P_{\rm coarse}(\rho,K)<W(\rho,K).
\]

Indeed, with
\[
M_c=\frac{(1-\rho^2)K^2}{6}-\frac12,
\]
Parts VIII and IX give
\[
\mathcal E_{\rm ang}<M_c<\mathcal H.
\]
Part VII gives
\(\mathcal E_{\rm ang}<\mathcal H\Rightarrow P_{\rm coarse}<W\), and the
main phase reduction at lines 2031--2037 gives
\(N_D\leq P_{\rm coarse}\).

This theorem is the one new lemma that substantially simplifies the proof.
It removes an entire analytic branch rather than merely renaming its
intermediate quantities.

### Equality-face audit

The stronger theorem preserves every relevant face.

- \(\rho=\rho_c\) and \(\rho=39/50\) are included in the scalar base theorem.
- \(K=k_{11}(\rho)\) is included by strict base positivity.
- Radial--angular coincidence walls are included by the strict Part VIII
  rounding convention.
- There is no new upper-frequency face.

The theorem may overlap earlier proof regions.  That is harmless.  For the
existing exact owner ledger, one may apply it only to the open residual
\(\mathcal D_{20}\), leaving \(K=k_{11}\), \(K=U\), and
\(\rho=39/50\) with their current owners.

### Risk

**Low mathematical risk; medium process risk until restated and re-audited.**
The current theorem declarations still say \(K\leq200\).  A reader should not
be expected to infer the extension from a proof written under a restricted
definition.  Before deleting the aggregate branch:

1. restate the Part IX theorem on \(K\geq k_{11}\);
2. restate the Part VIII-to-IX compact theorem on the same domain;
3. add a short audit that checks the six items above;
4. update the historical region declarations in
   **compact-structural.tex**, lines 75--86, and
   **compact-angular-block.tex**, lines 392--417, so the module statements
   match what their proofs establish;
5. update the support-master dependency summary at
   **spherical-shell-polya-analytic-supplement.tex**, lines 40--47;
6. compile both volumes and recheck all references.

No new inequality, table, or numerical verification is required.

## 3. Consequences for the compact \(\mathcal E_{\rm ang}\)--\(\mathcal H\)
argument

### Current main range

Main lines 3684--3738.

### Safe main compression

Retain the strengthened theorem statement and the single displayed chain
\[
N_D\leq P_{\rm coarse},\qquad
\mathcal E_{\rm ang}<M_c<\mathcal H,\qquad
\mathcal E_{\rm ang}<\mathcal H\Longrightarrow P_{\rm coarse}<W.
\]
Then cite:

- Part VII:
  **compact-structural.tex**, lines 270--460;
- Part VIII:
  **compact-angular-block.tex**, lines 288--380 and 400--406;
- Part IX:
  **compact-scalar-positive.tex**, lines 124--288 and 527--642.

The \(T>1\) calculation now belongs naturally in the support reference.  The
main paper needs only one sentence saying that the strict chain includes the
closed ratio/base faces and all proxy walls.

The quantities \(\mathcal E_{\rm ang}\) and \(\mathcal H\) may remain unnamed
outside this one chain.  Defining
\(M_c\) is useful because it makes the two independent support inequalities
visibly composable.

### Risk

**Low.**  This removes duplicated assembly, not a proof step.  Do not weaken
either strict inequality or change \(K\geq k_{11}\) to \(K>k_{11}\); the
closed base face is already proved.

## 4. The \(\mathcal Q/\mathcal B\) branch

### Current main ranges

- definitions of \(\mathcal B\): lines 3740--3766;
- discrete arithmetic, \(\mathcal Q\), and its proof: lines 3768--3914;
- analytic aggregate tail: lines 3916--3971.

### Recommendation

Remove this entire block from the logical proof after the stronger
middle-ratio theorem is formalized.  It is no longer necessary to compress
\(\mathcal Q\) or merge the \(\mathcal B\)-lemmas: no point of
\(\mathcal D_{20}\) reaches that branch.

The material can be:

- retained in the analytic supplement as an independent alternative proof
  and quantitative tail theorem;
- moved to an appendix;
- or removed from the review version if manuscript length is the priority.

Parts X--XIII would then be optional mathematics, not dependencies of the
spectral theorem.

### Circularity warning if the alternative branch is retained

The current **aggregate-tail-analytic.tex** is not self-contained with respect
to the discrete bridge:

- lines 111--148 define \(\mathcal Q\) and import the implication
  \(\mathcal Q\geq0\Rightarrow N_D<W\) from the main manuscript;
- lines 150--185 reproduce only \(\mathcal Q>\mathcal B\);
- lines 388--395 again identify the discrete implication as a main input.

Thus main lines 3768--3911 cannot be moved behind a Part XIII citation unless
their complete shelf/midpoint, low-tail, high-tail, and multiplicity proof is
first relocated into the supplement.  This warning matters only if the
aggregate theorem is kept as an independent result; the simplified Pólya
proof can omit the branch altogether.

### Optional quantitative lemma

If the aggregate result is retained, the existing inequalities imply the
stronger statement
\[
P_{\rm coarse}<W-\frac12\mathcal B.
\]
Indeed, main lines 3854--3858 and 3861--3889 give
\[
P_{\rm coarse}<W-\frac12\mathcal Q,
\]
and lines 3896--3911 give \(\mathcal Q>\mathcal B\).  This packages the
aggregate proof cleanly, but it is no longer the best simplification of the
main theorem: the global middle-ratio theorem makes the aggregate branch
unnecessary.

### Risk

- **Low** to remove the branch after the strengthened Part IX theorem is
  stated and audited.
- **High** to remove it before that formal theorem exists, because the current
  printed compact statement stops at \(200\).
- **High** to move it to the current aggregate supplement by citation alone,
  because that creates a proof cycle.

## 5. Continuous \(\mathcal B\)-propagation

The propagation at main lines 3926--3970 is mathematically sound, but becomes
redundant.  Its canonical support is:

- **F-positive.tex**, lines 173--246;
- **BK-positive.tex**, lines 1--15 and its exact case proofs;
- **B-positive.tex**, lines 81--89 and 381--483;
- **aggregate-tail-analytic.tex**, lines 187--346.

If retained as an independent theorem, its main statement can be reduced to
\[
\mathcal B(\rho,200)>60,\qquad
\mathcal B_K(\rho,200)>0,\qquad
\mathcal B_{KK}(\rho,K)>\frac{1549}{84150},
\]
and hence
\[
\mathcal B(\rho,K)>
60+\frac{1549}{168300}(K-200)^2.
\]
The auxiliary names \(b,\overline R,S,F\) and the derivative calculation can
remain in the supplement.  At \(K=200\), strictness comes from the separate
base value, not from the vanishing integral term.

For the simplified spherical-shell proof, however, the safest and shortest
choice is to classify all of this as an optional independent tail theorem.

## 6. \(\mathcal D_{20}\) ownership

### Current main ranges

- exact residual: lines 3661--3664;
- exact closure proposition: lines 3973--4008;
- Proposition **compact-middle**: lines 4010--4039.

### Canonical support ranges

- **ledger-packet-F.tex**, lines 74--119: exact \(D_{20}\) subtraction;
- lines 121--142: the five delicate interfaces;
- lines 144--169: the now-unnecessary \(K=200\) split;
- **final-analytic-closure.tex**, lines 158--200: duplicate split assembly.

### Safe simplification

From the exact residual formula,
\[
\mathcal D_{20}
\subset
\left\{(\rho,K):
\rho_c\leq\rho\leq\frac{39}{50},\
K\geq k_{11}(\rho)\right\}.
\]
The inclusion is strict on the upper ratio and lower frequency faces, but the
new theorem is proved on the closed superset.  Therefore one sentence applies
the global middle-ratio theorem to every point of \(\mathcal D_{20}\).

The following main material is then unnecessary:

- the unused calculation \(k_{11}>12\) at lines 3979--3985;
- \(\mathcal C_{21},\mathcal T_{21},\mathcal D_{21}\);
- the case split at \(K=200\);
- the statement that \(K=200\) is compact-owned;
- Part XIV as a proof dependency.

The exact closure proposition and Proposition **compact-middle** can be merged:
the earlier owners leave exactly \(\mathcal D_{20}\), the global theorem owns
that residual, and \(K=0\) is the already stated equality case.

### What must remain main-visible

1. The exact residual with
   \(\rho_c\leq\rho<39/50\) and
   \(k_{11}(\rho)<K<U(\rho)\).
2. The direct inclusion of that residual in the new closed theorem domain.
3. The inherited owners of
   \(\rho=39/50\), \(K=k_{11}(\rho)\), and \(K=U(\rho)\), if the existing
   owner ledger is retained.
4. The inclusion of \(\rho=\rho_c\) subject to the two strict frequency
   inequalities.
5. \(N_D=W=0\) at \(K=0\).

There is no equality face at \(K=200\) after this simplification.

### Risk

**Low.**  Direct set inclusion is simpler than the present split and cannot
lose a \(K=200\) point.  The main risk is editorial: do not reassign the
already owned boundary faces inadvertently merely because the stronger
theorem also proves them.

## 7. Section 4.8 dependencies

### Current main range

Main lines 4041--4079.

### Required dependencies after simplification

Only two groups remain:

1. Parts I--VI: exact analytic owner subtraction leading to
   \(\mathcal D_{20}\);
2. Parts VII--IX: the global middle-ratio theorem.

Parts X--XIII (aggregate base and propagation) and Part XIV (the \(K=200\)
split) cease to be logical dependencies.  They may remain clearly labeled as
optional independent results.

The support master currently says at lines 40--47 that Parts X--XIV are in the
theorem's dependency chain.  That sentence must be revised if the global
middle-ratio route is adopted; otherwise the prose would retain a dependency
which the proof no longer uses.

The six-row census table at main lines 4048--4061 may move to the supplement.
Its canonical proof is in:

- **ledger-global-coverage-audit.md**, lines 7--16;
- lines 69--92: normalized allocation;
- lines 104--122 and 143--160: duplicate reassignments;
- lines 163--192: disjoint union.

A sufficient main dependency paragraph is:

1. Parts I--VI give the normalized exact owner subtraction.
2. Parts VII--IX prove the global middle-ratio analytic theorem.
3. Executable and interval programs are optional regression checks, not
   premises.

If the number \(611\) remains in the main paper, retain the qualifier
“normalized”: the raw proof packets deliberately repeat 10 lower-\(d\)
identities and 36 optical general identities before canonical assignment.

### Risk

**Low mathematical risk** in moving the table.  Preserve a precise supplement
cross-reference so that the owner census remains auditable.

## 8. Recommended compressed main structure

The 405 current source lines can be reduced to roughly 45--75 lines:

1. **Global middle-ratio analytic theorem.**
   State the domain \(K\geq k_{11}\) and the strict result.
2. **One-display proof.**
   Put \(M_c=(1-\rho^2)K^2/6-1/2\) and cite
   \[
   \mathcal E_{\rm ang}<M_c<\mathcal H,
   \qquad
   \mathcal E_{\rm ang}<\mathcal H\Rightarrow P_{\rm coarse}<W,
   \qquad N_D\leq P_{\rm coarse}.
   \]
3. **Residual closure.**
   Cite the exact owner subtraction and note
   \(\mathcal D_{20}\) is contained in the theorem domain.
4. **Compact-middle conclusion.**
   Preserve the inherited faces and \(K=0\).
5. **Dependency remark.**
   List Parts I--IX and classify computations and the aggregate alternative as
   non-premises.

This proof graph is strictly shorter:
\[
\text{phase reduction}
\longrightarrow
\text{global compact analytic theorem}
\longrightarrow
\text{exact }\mathcal D_{20}\text{ inclusion}
\longrightarrow
\text{compact-middle theorem}.
\]

## 9. No-go simplifications

1. Do not delete the aggregate branch before the unbounded Part IX theorem is
   explicitly stated and audited; the current printed statement ends at
   \(200\).
2. Do not claim the extension merely from the word “monotone.”  Record that
   the derivative proof needs only \(K>12\), and that
   \(k_{11}>241/20>12\).
3. Do not omit strict base positivity at \(K=k_{11}\).
4. Do not weaken the strict angular rounding convention at proxy walls.
5. Do not cite the current aggregate supplement as a self-contained
   replacement for the main \(\mathcal Q\)-bridge.
6. Do not use the stronger theorem to silently change the existing owners of
   \(\rho=39/50\), \(K=k_{11}\), or \(K=U\).
7. Do not continue to describe Parts X--XIV as proof dependencies after the
   aggregate branch and \(K=200\) split are removed.

## Final recommendation

Promote the strengthened upward-closed scalar theorem first.  It is already
proved by the existing derivative and base-curve arguments; only the theorem
domain and audit need to be updated.  Then use Parts VII--IX to state one
global middle-ratio theorem and close \(\mathcal D_{20}\) by direct inclusion.

This is materially better than compressing the aggregate route: it removes
the full \(\mathcal Q\)-bridge, all \(\mathcal B\)-propagation, and the artificial
\(K=200\) ownership interface without introducing a new estimate or losing any
equality face.
