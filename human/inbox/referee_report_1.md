# Referee report on “A Dirichlet Pólya Inequality for Three-Dimensional Spherical Shells”

## Recommendation

**Major revision.** I did not find a counterexample, a reversed inequality, or a fatal flaw in the principal analytic mechanism. In particular, the separated spectral formula, the phase-to-action reduction, the small-hole argument, the thin-shell optical argument, and the retained-remainder argument in Parts VII–IX survive detailed checking.

I nevertheless do **not** regard the current submission as ready for acceptance. The decisive finite high-staircase step is not yet presented as a closed mathematical argument independent of the old executable registry: the manuscript states that all proxy events have been exhausted and paid, but the supplied analytic packet does not display the missing event-to-payment exhaustion map. A second, smaller but still important issue is that the Bessel sign tables do not explicitly prove that the sign being tested belongs to the claimed zero index. Both points appear repairable, but both feed essential parts of the compact-middle proof.

The source package is also incomplete: the analytic-supplement TeX file is only a wrapper around ten component PDFs whose TeX sources and compiled component files were not supplied.

## 1. What I checked

I audited the following chain.

1. The spherical-harmonic decomposition and the unitary map \(R\mapsto u=rR\).
2. The Bessel cross-product determinant, root simplicity, phase monotonicity, and the exact strict phase count.
3. The passage from the Bessel phase to \(A_{\rho,K}+1/4\), including \(z=\rho K\), \(z=K\), and integer proxy walls.
4. The weighted-tail identity and both the high-interface and low-interface estimates.
5. The product comparison and the complementary-action layer cake.
6. The shifted-sawtooth Stieltjes calculation.
7. The optical low- and high-frequency screens.
8. Parts VII–IX of the analytic supplement: the exact retained-remainder identity, the global angular block estimate, and the upward-monotone scalar inequality.
9. The regional owner subtraction and the non-tiling argument.

I also checked the quoted FLPS phase and trapezoidal-floor inputs against the primary papers. The hypotheses and endpoint directions used in the manuscript agree with Theorem 5.1, Lemma 5.2, Theorems 1.4 and 3.4 of the annulus paper, and with Theorem 5.1 of the ball paper:

- [Filonov–Levitin–Polterovich–Sher, annuli, arXiv:2505.21737](https://arxiv.org/abs/2505.21737)
- [Filonov–Levitin–Polterovich–Sher, balls, arXiv:2203.07696](https://arxiv.org/abs/2203.07696)
- [DLMF §10.21, Bessel zeros and interlacing](https://dlmf.nist.gov/10.21)

For the scalar certificate I independently recomputed, using exact rational arithmetic:

- the four Bernstein coefficients in the derivative-positivity cubic;
- the secant quadrature fraction \(Q\) and the positive difference \(17/100-Q\);
- the degree-nine polynomial in the base-curve proof; and
- all ten degree-nine Bernstein coefficients.

They agree exactly with the displayed fractions in Parts VIII–IX.

## 2. Major issue: the high-staircase event exhaustion is asserted, not displayed

The crucial passage is in the main manuscript around lines 2654–2685. After defining

\[
C_z(K)=\sum_{(\ell,n)}(2\ell+1)\mathbf 1_{\{b_{\ell,n}(z)<K\}},
\]

the proof lists seventeen rational ratio splits, three \(z^2\)-splits, and six representative reserves, and concludes:

> Every realizable event is strictly paid.

That conclusion is the theorem that still needs proof. The cap tables and Packet C provide many correct ingredients, but I could not find a printed exhaustive map establishing all of the following:

1. every event of \(C_z(K)\) in \(k_6(\rho)<K\le k_{11}(\rho)\) occurs in one of the listed cases;
2. no ordering change between two fixed or moving modal walls has been omitted;
3. each post-event cap is one of the printed cap values;
4. each such cap is attached to a specific global, conditional, or exceptional payment; and
5. simultaneous events are charged with their full combined multiplicity.

Packet C proves localization implications and positive payment inequalities, and its row census says that these replace the old registry. A census, however, does not prove the logical surjectivity from all possible proxy events to the printed rows. The references to the “original exact registry” cannot fill the gap because that registry is expressly declared not to be a premise and is not reproduced as a mathematical event table.

This is not merely a request for more arithmetic. It is a missing finite-combinatorial closure lemma. Since Lemma “Closed high staircase through \(k_{11}\)” is used to identify the final residual, the gap lies on the main theorem’s dependency path.

### Required repair

Add one explicit event theorem. A satisfactory table should have one row per realizable post-event state and contain at least:

| band | ratio interval | entering mode(s) | event wall | pre-cap | post-cap | payment lemma/row | equality owner |
|---|---|---|---|---:|---:|---|---|

The proof should then establish:

- completeness from the checkpoint inventories and monotonicity in \(\ell\) and \(n\);
- disjointness or controlled overlap of the ratio cells;
- the direction of every rational split;
- the payment at the event wall, not merely at a later checkpoint; and
- the combined cap at coincident walls.

A shorter alternative is a case-free domination lemma showing that, in each band, every cap is either below the global cap or forces one of the seven conditional first-mode hypotheses, with the cap-74 case separated. That implication is suggested by Packet C, but it should be written and proved explicitly.

**Severity:** major and theorem-critical, but apparently repairable. I found no algebraic contradiction or counterexample to the asserted staircase conclusion.

## 3. Major-to-moderate issue: the Bessel sign ledger does not explicitly certify the zero index

The main manuscript gives signs of the spherical Bessel functions at half-period endpoints and rational walls, followed by asserted zero counts. The analytic supplement expands the sign arithmetic. What remains too compressed is the implication

\[
\text{endpoint signs and the sign at }w
\quad\Longrightarrow\quad
j_{\ell+1/2,n}>w
\]

for the stated value of \(n\).

A sign change only proves an odd number of zeros in an interval. To identify the second or third zero, one must also prove the exact count before the interval and uniqueness within it. The manuscript says that the derivative recurrence, “combined with angular propagation,” gives strict interlacing. Angular propagation gives a fixed-index lower comparison; it is not itself the standard adjacent-order interlacing theorem.

The intended repair is short. State and cite, or prove by Sturm theory, the exact interlacing relation

\[
j_{\nu,n}<j_{\nu+1,n}<j_{\nu,n+1},
\qquad \nu>-1,\ n\ge1,
\]

in the special half-integer cases used here. Start from the zeros of \(J_{1/2}\), and give an induction table showing the exact zero count at each half-period endpoint. Then the rational-wall sign determines on which side of the unique target zero the wall lies.

The same section should give an exact theorem/equation locator for the Lorch bound, rather than citing the entire paper. That formula supplies several first-mode exclusions and its precise strictness and range \(\nu>-1\) are material.

**Severity:** major if the paper continues to advertise the finite zero registry as self-contained; moderate if a precise standard interlacing theorem and the exact Lorch locator are added.

## 4. Reproducibility defect: the analytic supplement source is not self-contained

The file spherical-shell-polya-analytic-supplement.tex contains only ten \(\backslash\)includepdf commands. It refers to files such as

    analytic/compiled/ledger-main-visible.pdf
    analytic/compiled/compact-structural.pdf
    analytic/compiled/compact-scalar-positive.pdf

and says that the corresponding sources are in manuscript/analytic. None of those files or source directories is included in the supplied package. The attached compiled supplement PDF is readable, but the TeX source cannot reproduce it.

For a proof whose central claim is that executable certificates have been eliminated in favor of hand-visible analytic exhibits, source completeness is important. Supply:

- all ten component TeX sources;
- a top-level build file using \(\backslash\)input where possible;
- a manifest identifying which components are logical premises and which are retired cross-checks; and
- stable hashes for the source components if hashes are to be mentioned.

**Severity:** major reproducibility issue, not by itself a mathematical counterexample.

## 5. The dependency boundary remains unnecessarily ambiguous

The supplement repeatedly counts 611 “canonical ledger rows,” including superseded seam and intermediate-owner rows, while the main manuscript says that some of those rows are optional cross-checks. A referee should not have to infer the minimal proof graph from the history of an executable ledger.

Please include a one-page dependency table with columns

| result | premises | external theorem | supplement part | status |
|---|---|---|---|---|

where status is exactly one of “used in final proof” and “optional cross-check.” Remove retired modules from the theorem’s proof narrative, or place them in a clearly marked historical appendix.

**Severity:** moderate. The ambiguity does not create a contradiction, but it materially obstructs verification of the finite argument.

## 6. Strict counting convention versus the standard formulation

The manuscript defines

\[
N_<(\Lambda)=\#\{j:\lambda_j<\Lambda\}.
\]

Many formulations of Pólya’s conjecture use \(N_{\le}(\Lambda)\). Proving the result for all thresholds with the strict convention does imply the non-strict version, but the manuscript should say so explicitly:

\[
N_{\le}(\Lambda)
=\lim_{\varepsilon\downarrow0}N_<(\Lambda+\varepsilon)
\le \lim_{\varepsilon\downarrow0}L_3|\Omega|(\Lambda+\varepsilon)^{3/2}
=L_3|\Omega|\Lambda^{3/2}.
\]

This one line prevents a reader from mistaking the theorem for a weaker variant of the conjecture.

**Severity:** minor but necessary for the title and abstract.

## 7. Smaller points requiring correction or clarification

1. **Notation.** The symbol \(q_{\ell,n}\) denotes shell eigenfrequencies in the compact-middle section, while nearby \(q_\ell\) denotes floor samples. Rename one family.
2. **“Coarse” proxy.** In the compact-middle argument \(P_{\rm coarse}\) uses the strict bracket, whereas earlier \(S_{\rho,K}\) uses the ordinary floor. State the relation between them once, at the definition.
3. **First \(J_{3/2}\) wall.** The claim \(\tan 4<2\) is elementary but should be supplied with the same rational tangent bound used elsewhere.
4. **External inputs.** Cite theorem/equation numbers for every imported statement, especially Lorch’s bound and the Bessel phase theorem. The FLPS theorem numbers are already mostly given and should be made consistent in the final bibliography notes.
5. **Endpoint language.** Whenever a fixed Bessel lower wall is used, distinguish clearly between the strict lower proxy \(\beta_{\ell,n}\) and the actual zero. Equality at the proxy is not an actual spectral equality; it is excluded because the actual zero is strictly larger.
6. **Authors and status.** The manuscript currently has no author information and repeatedly discusses “status,” “trust boundaries,” hashes, and old ledgers. A research article should move most of this material to a reproducibility appendix.

## 8. Parts that appear mathematically sound

Subject to the two finite-registry issues above, the following arguments appear correct.

### 8.1 Separated spectrum and strict phase enumeration

The form-domain decomposition is correct, the direct-sum compactness argument is valid, and the cross-product determinant has the stated sign. The Lagrange identity correctly proves simplicity. Nicholson’s formula gives the needed strict decrease of \(J_\nu^2+Y_\nu^2\), hence strict increase of the phase difference. The strict count at a phase wall is handled correctly.

### 8.2 Phase enclosure and small-hole endpoint

The imported FLPS phase inequalities have the required real-order scope and include the interface \(z=\mu\). The optimized correction \(s_\mu\), the strict-to-ordinary-floor passage, and the action integral are correct. The weighted-tail scaffold and the low-interface loss estimate also check out, including \(n=0\), \(q=\mu\), and \(\rho K=1/2\).

### 8.3 Product and complementary-action arguments

The min–max direction is correct. The inverse-action geometry has the stated one-turn behavior, and the layer-cake identities preserve both radial and angular strict walls.

### 8.4 Retained-remainder theorem

This is the strongest part of the submission. The exact identity

\[
W-P=B+R_{\rm dec}+R_{\rm osc}-E_{\rm ang}
\]

is correct. The primitive minorant \(L(t)=t^2/[2(1+2t)]\) is valid. The one-layer bound

\[
r_n\le \frac43\int_{n-1}^{n-1/4}R(t)\,dt-\frac34
\]

follows from \(-A'\le1/2\), and summation gives

\[
E_{\rm ang}<\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

The scalar loss estimate, derivative positivity, rational secant majorant, and degree-nine Bernstein certificate are internally consistent and exact.

### 8.5 Optical theorem and non-tiling

Both optical screens have the correct scaling and meet at the claimed closed interface. The non-tiling proof correctly obtains uniform center separation, local finiteness, and a finite covering of one outer sphere by lower-dimensional sphere intersections, which is impossible.

## 9. Minimal revision needed for a second report

For a revised submission, I would require at least:

1. the explicit high-event exhaustion/payment theorem described in §2;
2. the exact interlacing/index proof described in §3;
3. all component TeX sources for the analytic supplement;
4. a minimal dependency graph separating premises from optional checks;
5. a one-line conversion to the standard non-strict counting convention; and
6. theorem/equation locators for every external input.

If those changes are supplied, the proof would merit a new, focused audit of the finite staircase. At present my assessment is: **the analytic strategy is credible and the global retained-remainder argument is impressive, but the finite compact-middle bridge is not yet documented at publication standard.**
