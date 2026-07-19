# Independent audit: Round 11 first-floor pre-shelf reduction

Date: 18 July 2026

Audited source:

`human/outbox/general-d-round-11-first-floor-pre-shelf-reduction.md`

Audited SHA-256:

`C28636372F8307198E62EA7236B40441982C19604688AB3AF4EC772AE449FFDA`

Post-audit integrated source SHA-256:

`6F221BBB6CC287E0164424615C73F1414917ED8117CFE8B6E3DC94E3B4CB57A4`

The integrated source differs from the frozen audit target only by applying
items 3 and 4 of Section 8: it distinguishes the exact-head-only diagnostic
from the exact-head-plus-cap diagnostic and changes “positive amount” to the
correct wall-safe “nonnegative amount.”  No formula or theorem statement was
changed.

Diagnostic evaluator replayed:

`computations/general_d_fractional_terminal_probe.wl`

Evaluator SHA-256:

`31F0B831E43052725253BA8AB7F23E6695CBB80CFE74B048D3BC0FA79ED3F066`

## 1. Verdict

**PASS, with the nonblocking precision and dependency caveats recorded in
Section 8 below.**

The analytic statements proved in the note are correct:

1. Lemma 2.1 has the stated direction and constant.
2. Equations (3.1)--(3.5) give a valid sufficient lower bound for the exact
   no-drop remainder.
3. Proposition 4.1 is a valid implication on the new extension grids.  The
   note correctly does not claim that its sufficient scalar is nonnegative.
4. Theorem 5.1 proves the full strict (B=0) corner, including the
   (r=1/2) line.
5. The equality-face and loss ledgers are mathematically accurate apart from
   the harmless strict/non-strict wording caveat in Section 8.
6. The deterministic Mathematica replay and the fixed (r=1/2) probe
   reproduce the reported counts, minimum, and negative value of (4.5).

This verdict does **not** prove (4.5), close the remaining (B=1) sector, or
promote the general-dimensional theorem.  It certifies the reduction and the
new (B=0) theorem only.

## 2. Scope and ownership audit

The extension-grid domain (1.2a) is correct once the completed (d=3)
theorem is taken as the base:

\[
 r\in\mathbb N,\ r\geq1 \quad(d_{\rm owner}=4),
 \qquad
 r\in\mathbb N_0+\frac12,\ r\geq\frac32
 \quad(d_{\rm owner}=5).
\]

Every higher-dimensional integer or half-integer shift is contained in one
of these two grids.  The only lower half-integer line is (r=1/2), already
owned by (d=3).  Thus restricting the new Proposition 4.1 obligation to
(1.2a) creates no gap in the dimension-lifting program.

The activity wall gives

\[
 \lambda=\frac{(1-\rho)K}{\pi}>1
\]

in every relevant owner dimension: the additive term in (1.1) is zero in
(d=3) and positive in (d\geq4).  Theorem 5.1 needs only (r>0), through
(n/q<1), and therefore legitimately includes (r=1/2).

The branch bookkeeping is also complete.  Since (r\geq1/2) and (n\geq1),
(q\geq3/2), so the quoted cap bound
(h<G_{5/2}(3/2)<1/5) applies.  If (B\geq2), strict counting gives
(v>7/4), not (v\geq7/4), and consequently

\[
 \varepsilon=v-h-\frac34>1-h>\frac45.
\]

Thus the (B\geq2) sector really is inside the already closed
(\varepsilon\geq1/4) sector.

## 3. Lemma 2.1 and the remainder reduction

For (0<z<\mu), direct differentiation gives

\[
 \sigma'(z)=\frac1{\pi\sqrt{\mu^2-z^2}}
 -\frac1{\pi\sqrt{K^2-z^2}}\geq0,
\]

\[
 \sigma''(z)=\frac z\pi\left((\mu^2-z^2)^{-3/2}
 -(K^2-z^2)^{-3/2}\right)\geq0.
\]

Hence (\sigma) is increasing and convex and (\sigma(0)=0).  The chord
bound and monotonicity give, with the directions used in the note,

\[
 \int_0^r\sigma\leq\frac r2\sigma(r),
 \qquad
 \int_r^{r+n}\sigma\geq n\sigma(r).
\]

Substitution of
(A(r)=3/4+\varepsilon+\Delta) therefore gives exactly

\[
 \Delta\geq
 \frac{2n}{r+2n}\left(\lambda-\frac34-\varepsilon\right).
\]

On the residual range (0\leq\varepsilon<1/4), its right side is strictly
positive from (\lambda>1).  In fact strict positivity also follows on the
full first-floor branch from
(\lambda-3/4-\varepsilon=A(0)-A(q)>0).

For the no-drop shelf,

\[
 \varepsilon_0=\varepsilon+\Delta,
 \qquad \varepsilon_n=\varepsilon.
\]

Thus S2 and S3 give exactly (3.1).  Its coefficient of (\Delta) is

\[
 M_n=n+\frac{n^2}{3(2r+n)}>0.
\]

Replacing (\Delta) by its lower bound therefore preserves the direction.
Moreover

\[
 \mathcal H'(\varepsilon)
 =2n\left(1-\frac{M_n}{r+2n}\right)>0,
\]

because (M_n<4n/3<2n\leq r+2n).  Since
(\varepsilon\geq0), replacing (\mathcal H(\varepsilon)) by
(\mathcal H(0)) gives exactly (3.5), with no reversed inequality or lost
wall term.

## 4. Proposition 4.1, equality faces, and losses

For (B=1), T2 gives the terminal expression with the exact cap
(-2\delta).  T3 says (2\delta\leq\alpha h), so
(-2\delta\geq-\alpha h).  Therefore

\[
 D_A(q)\geq\max\{0,\widehat L_1\}
\]

with precisely (4.4).  Combining this with the exact S4 identity and (3.5)
produces (4.5), including the favorable (\chi_q).  Proposition 4.1 is an
implication; no unsupported sign assertion is made.

The literal strict-wall data in (4.7) are correct:

- (0<\varepsilon<1/4) gives (Q=1,\chi_q=0);
- (\varepsilon=0,h>0) gives (Q=0,\chi_q=1,B=1);
- (\varepsilon=h=0) gives (Q=0,\chi_q=1,B=0).

At (y_1\in\mathbb N), the strict fraction is (\eta=1), not zero.  At
(v+1/4\in\mathbb N), the equality level is absent, so (B) and the top
square are evaluated literally.  At a shelf wall, the ordinary remainder is
zero; at (r+j=\mu), (G_\mu=0); and at (r+j=K), the strict action count
is zero.  The note does not replace any of these values by an adjacent
one-sided limit.

The loss ledger is complete and has the correct signs:

1. S3 discards its nonnegative curvature/hinge surplus.
2. The positive coefficient (M_n) permits the replacement
   (\Delta\mapsto\Delta_*(\varepsilon)).
3. Monotonicity discards
   (\mathcal H(\varepsilon)-\mathcal H(0)\geq0).
4. T3 discards (\alpha h-2\delta\geq0), while T2 discards the
   nonnegative inverse-tangent gaps.

The maximum in (4.3) merely takes the stronger of two established lower
bounds.  The terms (2\eta), ((v-1)_+^2/\beta), and (\chi_q) all remain.

## 5. Theorem 5.1: corner and active-angle audit

If (B=0), then (v\leq3/4).  Since
(A(q)=v-h\geq3/4) and (h\geq0), equality is forced throughout:

\[
 v=A(q)=\frac34,\qquad h=0,\qquad q=\mu.
\]

The strict bracket then gives (Q=0) and S4 gives (\chi_q=1).  Thus (5.2)
owns the exact corner rather than a limit from (B=1).

With (c=\cos\theta=q/K) and
(\Phi=\sin\theta-\theta\cos\theta), the identities (5.4) are exact.  For

\[
 H(\theta)=\frac{1-\cos\theta}{\Phi(\theta)},
\]

the derivative numerator is

\[
 \sin\theta\,[\Phi-\theta(1-\cos\theta)]
 =\sin\theta(\sin\theta-\theta)<0.
\]

The Taylor constants used at (\theta_0=2/\sqrt3) were independently
reduced to exact fractions:

\[
 1-\frac{4/3}{6}+\frac{(4/3)^2}{120}
 -\frac{(4/3)^3}{5040}=\frac{6737}{8505},
\]

\[
 1-\frac{4/3}{2}+\frac{(4/3)^2}{24}
 -\frac{(4/3)^3}{720}+\frac{(4/3)^4}{40320}
 =\frac{10313}{25515},
\]

and the lower cosine truncation is (491/1215).  The displayed squared
numerator is also exact:

\[
 (11312\cdot8505)^2-3(15202\cdot3645)^2
 =44{,}853{,}838{,}881{,}300>0.
\]

It follows in the stated direction that
(\lambda(2/\sqrt3)<1); since (H) decreases and the active point has
(\lambda>1), one gets (0<\theta<2/\sqrt3).  Equations (5.6) and (5.7)
then follow, including the strict constant (4/9).

## 6. Theorem 5.1: slope, integral, and quartic audit

At the corner (q=\mu), for (s\in[1-t,1]),

\[
 \pi\sigma(qs)=\arccos(sc)-\arccos s
 =\int_0^\theta\frac{s\sin u}
 {\sqrt{1-s^2\cos^2u}}\,du.
\]

Because
(\sqrt{1-s^2\cos^2u}\leq\sqrt{1-s^2c^2}), the lower bound in (5.8) has
the correct direction.  The endpoint (s=1,u=0) is interpreted by its
continuous/improper limit; it creates no contribution or inequality issue.

With (r=q-n), the change of variables gives

\[
 \int_{1-t}^1(s-1+t)s\,ds=\frac{t^2(3-t)}6,
\]

so the last line of (5.9) and every factor of (2,3,\pi) are correct.  The
denominator (D) is the largest denominator on that interval, hence using
(1/D) is again a lower bound.

The estimates

\[
 \frac1q<\frac{10}{9\pi}\theta^3,
 \qquad
 D^2<\theta^2\left(1+\frac{20x}{9\pi}\right)
\]

follow from (c>2/5), (t=n/q), and (x=n\theta).  Substitution in (5.9)
gives exactly the coefficient (8/(27\pi)) in (5.12).  The zero-level
triangle is

\[
 \frac{v^2}{\beta}
 =\frac{(3/4)^2}{\theta/\pi}
 =\frac{9\pi}{16\theta},
\]

so (5.13) retains the correct terminal constant and the exact wall bonus
(+1).

For (u=\sqrt{1+20x/(9\pi)}), exact algebra gives

\[
 \frac{400u}{\pi}f(x)
 =24u^4-90u^3-48u^2+315u+24.
\]

The degree-four Bernstein coefficients of (P(1+7z/4)) independently
recompute as

\[
 225,\quad\frac{3915}{16},\quad\frac{2809}{16},\quad
 \frac{3285}{128},\quad\frac{225}{8}.
\]

For (u=11/4+v), direct expansion gives

\[
 P=\frac{225}{8}+\frac{45}{8}v+\frac{597}{2}v^2
 +174v^3+24v^4.
\]

Both certificates are strictly positive on their stated domains.  Hence
(f(x)>0) for every (x\geq0), and Theorem 5.1 proves the stronger margin
(D_A(r)>1), in particular (D_A(r)>0).

## 7. Mathematica replay and independent fixed-probe evaluation

The supplied evaluator was replayed with Wolfram 15.0 for Windows.  It
reported exactly

\[
 \#\{\text{dimension-active records}\}=6409,
 \qquad
 \#\{B=1\text{ extension-grid records}\}=5911,
\]

and the minimum Round-11 scalar on that diagnostic set was

\[
 0.0820415151912213230\ldots
\]

at (r=1,n=2,q=3).  Thus the counts and rounded value in Section 6 are
faithful to the deterministic evaluator.  They remain diagnostics, exactly
as the note says.

At the fixed parameters (6.1), an independent 80-digit direct evaluation
gave

\[
 \mu=2.612316,\qquad
 K^2-\frac{\pi^2}{(1-\rho)^2}
 =0.00192527327161702547\ldots>0,
\]

so the point is (d=3)-active.  The first-floor samples are

\[
 A(1/2)=0.9916701780731465\ldots,
\quad A(3/2)=0.9213365760696208\ldots,
\quad A(5/2)=0.7503130654416735\ldots,
\]

and therefore (F_0=F_1=F_2=1).  Further,

\[
 B=Q=1,\quad\chi_q=0,\quad
 \varepsilon=0.0003130654416735176163\ldots,
\]

\[
 \widehat L_1=0.4460868663636386866\ldots,
\qquad
 \mathcal R_0=-0.4567269449639904527\ldots,
\]

and hence

\[
 \widehat\Psi_1=-0.01064007860035176606\ldots.
\]

The reported negative value and its open (B=1) classification are
correct.  Direct quadrature and literal strict counting independently give

\[
 D_A(1/2)=0.5738317850006371137\ldots>0.
\]

For clarity about the quoted stronger scalar, the exact quantities split as

\[
 R_n=-0.3789316951037799263\ldots,
\]

\[
 \alpha h-2\delta
 =0.0001577281252282904793\ldots.
\]

Restoring the exact head remainder while retaining the cap-relaxed
(\widehat L_1) gives

\[
 \widehat L_1+R_n
 =0.06715517125985876034\ldots>0.
\]

The note's quoted number

\[
 0.06731289938508705082\ldots
\]

is also correct, but it is the stronger Round-10 scalar that restores both
the exact head remainder **and** the exact cap:

\[
 \widehat L_1+(\alpha h-2\delta)+R_n.
\]

This distinction does not affect any proof or sign conclusion.  In
particular, undoing the head relaxation alone already changes the sign to
positive.

## 8. Exact caveats and suggested cleanup

These are nonblocking; none invalidates Lemma 2.1, Proposition 4.1, or
Theorem 5.1.

1. **Lemma 2.1's final justification uses the contextual hard range.**
   The lemma is stated only as “Under (1.1)--(1.4),” while its last sentence
   cites (\varepsilon<1/4), established in the preceding residual split
   rather than in (1.1)--(1.4).  Either add
   (0\leq\varepsilon<1/4) to the lemma statement or justify positivity by
   (A(0)-A(q)>0).  The boxed lower inequality itself is valid as written.

2. **The dependency list is analytically complete but not literally complete
   for the scope/status assertions.**  Excluding (r=1/2) as a new
   obligation also invokes the completed (d=3) theorem and the
   dimension-shift ownership rule.  These are stated immediately before the
   list, but if “uses only” is read literally they should be added as a
   fourth scope dependency.  Neither is a premise of Proposition 4.1's
   algebra or Theorem 5.1's proof.

3. **The label on (0.06731289939\ldots) is compressed.**  As detailed in
   Section 7, that value restores both the exact head and exact cap.  The
   exact-head-only value with (4.4) is
   (0.06715517126\ldots).  Both are positive, so the intended diagnostic
   message remains correct.

4. **One loss is nonnegative rather than everywhere positive.**  Loss-ledger
   item 3 calls
   \(\mathcal H(\varepsilon)-\mathcal H(0)\) a “positive amount.”  It is
   zero on the literal lower wall \(\varepsilon=0\), and strictly positive
   only for \(\varepsilon>0\).  Replace “positive” by “nonnegative” (or add
   “positive off the lower wall”).  The inequality and equality ownership
   are unaffected.

5. **The (r=1/2) counterexample remains numerical evidence.**  The source
   explicitly calls the replay non-interval and diagnostic.  Accordingly,
   the sentence “Thus (4.5) is not a valid universal sign target” should be
   read within that diagnostic scope unless a directed-rounding or interval
   certificate is later added.  Independent 80-digit evaluation and the
   sizeable negative margin reproduce the claim, and no theorem in the note
   depends on it.

6. **Endpoint convention in (5.8).**  At (s=1,u=0), the displayed
   integrand is represented by a removable/improper endpoint limit.  A short
   phrase to that effect would make the proof maximally literal, but no
   estimate changes.

## 9. Final disposition

- Extension-grid ownership: **PASS**.
- Dependencies and open-status language: **PASS with the scope-ledger caveat
  above**.
- Lemma 2.1 and (3.1)--(3.5): **PASS**.
- Proposition 4.1: **PASS as a sufficient reduction; sign still open**.
- Equality and loss ledgers: **PASS**.
- Theorem 5.1, including all constants and the Bernstein certificate:
  **PASS**.
- Mathematica counts and minimum: **PASS as diagnostics**.
- Fixed (r=1/2) negative value: **reproduced; PASS as diagnostic evidence**.

After this audit was frozen, its two exact wording corrections in items 3 and
4 were applied to the integrated Round-11 source; the hashes above distinguish
the frozen and corrected files.
