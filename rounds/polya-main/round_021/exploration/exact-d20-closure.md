# Round 21 exact cover of the prospective Round 20 residual

Status: **PROSPECTIVE INCUMBENT / NOT PROMOTED**.

Verdict: **PASS, conditional on promotion of the authenticated Round 20
candidate**.

First issue: **none found**.

This verdict has one deliberately narrow meaning.  If the authenticated
Round 20 candidate is eventually accepted and its displayed
\(\mathcal D_{20}\) becomes the actual successor residual, then the two
independently audited Round 21 certificates prove the strict Pólya
inequality at every point of that residual.  The corresponding prospective
Round 21 residual is empty.  This note does **not** prove, accept, or promote
the Round 20 candidate, and it does not use that candidate as a spectral
lemma.

## 1. Authentication before synthesis

All supplied artifacts were hashed as raw bytes before their mathematical
contents were used.  The observed SHA-256 digests are:

| role | artifact | observed SHA-256 | result |
|---|---|---|---|
| prospective residual claim | `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` | match |
| external claim freeze | `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` | match |
| aggregate analytic route | `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md` | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` | match |
| aggregate verifier | `computations/round21_verify_aggregate_tail.py` | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` | match |
| aggregate tests | `computations/tests/test_round21_verify_aggregate_tail.py` | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` | match |
| aggregate theorem report | `rounds/polya-main/round_021/certification/aggregate-tail-global.md` | `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` | match |
| aggregate adversarial audit | `rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md` | `aa12d25d71091cfd01a116bc2777afa8669248a13441be391cf3da0b48c9a894` | match |
| compact verifier | `computations/round21_certify_compact_proxy.py` | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` | match |
| compact tests | `computations/tests/test_round21_certify_compact_proxy.py` | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` | match |
| compact theorem report | `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md` | `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` | match |
| compact adversarial audit | `rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md` | `aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca` | match |

The upstream inputs used by the two routes also remain at their authenticated
digests:

| artifact | SHA-256 | scope used here |
|---|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum, multiplicity, and strict phase-count bridge |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | the one-sided phase enclosure and the displayed definition of \(G_a\) |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | spectral bridge/cutoff for the compact route and exact dimension reduction for the aggregate route |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` | accepted one-tail decomposition, curvature, convex-tail gain, and interface loss |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | only the qualified trapezoidal-floor and inner-interface integral bounds used by the aggregate route |

No Round 20 incumbent proof, Round 20 Bessel-zero card, sampled root,
floating-point spectral count, or formula for \(K_0\) enters either Round 21
spectral theorem.

As a reproduction check, the authenticated aggregate verifier passed at 192
bits on 1,286 outward ratio boxes.  The authenticated compact verifier passed
at 256 bits on 10,580 exact rational leaves, with exact coverage and
nonoverlap, and reproduced certificate digest
`96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`.
These replay facts support the certificate evidence; the analytic bridges
below explain what that evidence proves.

## 2. Conditional target and the two Round 21 theorems

Write

\[
 \rho_c=\frac1{1+2\pi},\qquad
 z_\rho=\frac{\pi}{1-\rho},\qquad
 k_{11}(\rho)=\sqrt{z_\rho^2+132},
\]

and

\[
 W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

The frozen but unpromoted Round 20 candidate proposes exactly

\[
 \boxed{
 \mathcal D_{20}=
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac{39}{50},\quad
 k_{11}(\rho)<K<K_0(\rho)=U(\rho)
 \right\}.}
 \tag{1}
\]

For this note, (1) is only the authenticated definition of a **prospective**
residual.  The Round 20 claim and freeze expressly say that it is not yet a
proved or promoted residual.

The two Round 21 theorem statements are independent of the truth of the
Round 20 candidate:

\[
 \boxed{
 \frac7{51}\leq\rho\leq\frac{39}{50},\quad
 12\leq K\leq200
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1},K^2)<W(\rho,K).}
 \tag{C}
\]

and

\[
 \boxed{
 \rho_c\leq\rho\leq\frac{39}{50},\quad K\geq200
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1},K^2)<W(\rho,K).}
 \tag{T}
\]

Here (C) is the compact coarse-proxy theorem.  The aggregate certificate
first proves \(\mathcal B(\rho,K)>0\) on the domain in (T); the authenticated
analytic route then transfers that positivity to the strict spectral
inequality in (T).

## 3. Independent reconstruction of the compact bridge

Put

\[
 \nu_\ell=\ell+\frac12,\qquad
 A_{\rho,K}(\nu)=G_K(\nu)-G_{\rho K}(\nu),
\]

where, with its accepted zero extension,

\[
 G_a(\nu)=\frac1\pi\left(
 \sqrt{a^2-\nu^2}-\nu\arccos\frac\nu a\right)
 \quad(0\leq\nu\leq a),
 \qquad G_a(\nu)=0\quad(\nu>a).
\]

For \([x]_<:=\#\{n\in\mathbb N:n<x\}\), completeness and the strict
phase-count convention give

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\nu_\ell<K}2\nu_\ell
 [\gamma_{\rho,K}(\nu_\ell)]_<.
\]

The authenticated phase enclosure gives, in every active channel,

\[
 \gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+\frac14.
\]

Inclusion of the corresponding sets of positive integers, including at an
integer wall, therefore yields

\[
 N_D(A_{\rho,1},K^2)
 \leq P_{\rm coarse}(\rho,K)
 :=\sum_{\nu_\ell<K}2\nu_\ell
 \left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<.
 \tag{2}
\]

This step never replaces a strict count with an ordinary floor.  At
\(x=m\in\mathbb N\), one has \([x]_< =m-1\), not \(m\).

For \(a>\nu\), direct differentiation gives

\[
 \partial_aG_a(\nu)=\frac1\pi
 \sqrt{1-\frac{\nu^2}{a^2}}\geq0.
\]

The derivative tends to zero at the zero-extension interface.  It follows
that \(A_{\rho,K}(\nu)\), and hence the strict proxy, decreases weakly with
\(\rho\).  At fixed \(\rho\), for \(\nu<K\),

\[
 \partial_K A_{\rho,K}(\nu)=
 \begin{cases}
 \dfrac{\sqrt{K^2-\nu^2}}{\pi K},
     &\rho K\leq\nu<K,\\[6pt]
 \dfrac{\sqrt{K^2-\nu^2}-
 \sqrt{\rho^2K^2-\nu^2}}{\pi K},
     &\nu<\rho K,
 \end{cases}
\]

which is positive.  At a new active-channel face \(K=\nu_\ell\), the
formal new summand is \(2\nu_\ell[1/4]_< =0\), so no cutoff jump breaks the
monotonicity.  On the other hand, \(W\) decreases in \(\rho\) and increases
in \(K\).  Therefore, on every exact rational box
\(B=[\rho_-,\rho_+]\times[K_-,K_+]\),

\[
 P_{\rm coarse}(\rho,K)
 \leq P_{\rm coarse}(\rho_-,K_+),
 \qquad
 W(\rho,K)\geq W(\rho_+,K_-).
 \tag{3}
\]

At the proxy corner, the verifier uses outward Arb to prove an integer upper
bound \(\widehat P_B\) on every strict count.  At the opposite corner, it
uses an outward lower enclosure \(W_{B,-}\), and accepts the leaf only under
the certain strict comparison

\[
 W_{B,-}-\widehat P_B>0.
\]

The exact rational partition tiles the whole closed rectangle in (C),
including every edge and vertex.  Combining (2), (3), and the certain leaf
comparison gives the strict chain

\[
 N_D\leq P_{\rm coarse}\leq\widehat P_B
 <W_{B,-}\leq W.
 \tag{4}
\]

This reconstructs the analytic meaning of the compact certificate and proves
(C), subject only to the authenticated accepted packets in its stated scope.
The third packet is not used here as an unproved weighted-floor theorem; only
its spectral bridge and cutoff are used.

## 4. Independent reconstruction of the aggregate bridge

Use the route notation

\[
 \mu=\rho K,\qquad
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 d_\rho=\frac{2\arcsin\rho}{\pi},
\]

\[
 b=\frac{2\pi\rho}{1-\rho},\qquad
 C=bK,\qquad
 R=\rho K+\frac12,
\]

and

\[
 \mathcal I(C,R)=\frac12\left[
 R\sqrt{R^2+C}
 +C\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right)
 -R^2\right].
\]

After summing all low-interface errors before taking a sign, the authenticated
route proves a discrete reserve implication

\[
 \mathcal Q(\rho,K)\geq0
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1},K^2)<W(\rho,K).
 \tag{5}
\]

The strictness comes from the strict shelf-length bound in the aggregate
sum; it remains strict in the \(\tau=0\) interface cell.  The floor-free
reserve is

\[
\begin{aligned}
 \mathcal B(\rho,K)={}&
 \left(\mu-\frac12\right)(K\eta_\rho-1)
 +\frac{d_\rho}{2}
 \left(\mu-\frac32\right)
 \left(\mu-\frac12\right)\\
 &-(1+d_\rho)\mathcal I(C,R)
 -\frac{8(\mu+1/2)}{15\sqrt\mu}.
\end{aligned}
 \tag{6}
\]

When \(K\eta_\rho>1\), the exact bounds on the number of low tails, the
triangular count, the interface remainder, and the strict inequality
\(\lfloor K\eta_\rho\rfloor>K\eta_\rho-1\) yield

\[
 \mathcal B(\rho,K)\geq0
 \quad\Longrightarrow\quad
 \mathcal Q(\rho,K)>0.
 \tag{7}
\]

Thus (6)--(7) and (5) give a strict theorem once \(\mathcal B\) is proved
positive.

It remains to justify why a finite base-frequency certificate controls every
\(K\geq200\).  Let

\[
 S=\sqrt{R^2+C},\qquad I(K)=\mathcal I(bK,\rho K+1/2).
\]

Differentiation at fixed \(\rho\) gives

\[
 I_K=\rho(S-R)+\frac b2
 \operatorname{arsinh}\!\left(\frac R{\sqrt C}\right),
\]

and

\[
 I_{KK}=ho^2\left(\frac RS-1\right)
 +\frac{\rho b}{2S}
 +\frac{b(2\rho K-1)}{8KS}.
 \tag{8}
\]

Because \(S>R>\rho K>0\), the first term in (8) is negative, the last term
is strictly less than \(\rho b/(4S)\), and hence

\[
 I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}.
 \tag{9}
\]

For

\[
 E(K)=-\frac8{15}\left(\sqrt\mu+rac1{2\sqrt\mu}\right),
\]

one has

\[
 E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}>0
 \qquad(\mu>3/2).
\]

Therefore, on \(K\geq200\),

\[
 \mathcal B_{KK}
 >F(\rho):=
 2\rho\eta_\rho+d_\rho\rho^2
 -\frac{3(1+d_\rho)b}{800}.
 \tag{10}
\]

The outward certificate proves, on the larger rational ratio interval
\([7/51,39/50]\), all three strict base signs

\[
 \mathcal B(\rho,200)>0,qquad
 \mathcal B_K(\rho,200)>0,qquad
 F(\rho)>0,
 \tag{11}
\]

together with \(\mu>3/2\) and \(200\eta_\rho>1\).  The exact partition is
split at \(\rho=1/2\), where the two formulas for \(\eta_\rho\) agree.  By
(10)--(11), \(\mathcal B_K\) is strictly increasing on \([200,\infty)\),
then \(\mathcal B\) is strictly increasing there, and therefore
\(\mathcal B(\rho,K)>0\) for every \(K\geq200\).  The two standing
conditions also persist as \(K\) increases.  Equations (5)--(7) now prove
(T), including the complete face \(K=200\).

## 5. The two exact containment inequalities

The compact certificate begins at the rational face \(\rho=7/51\).  The
standard strict bound \(\pi<22/7\) gives

\[
 1+2\pi<1+\frac{44}{7}=\frac{51}{7}.
\]

Both sides are positive, so reciprocation reverses the inequality:

\[
 \boxed{\frac7{51}<\rho_c.}
 \tag{12}
\]

For completeness, \(\pi>3\) also gives
\(\rho_c<1/7<39/50\), so all named ratio faces occur in the asserted order.

For \(\rho_c\leq\rho<1\), positivity of the denominators gives
\(z_\rho\geq z_{\rho_c}\), and exactly

\[
 z_{\rho_c}
 =\frac{\pi}{1-1/(1+2\pi)}
 =\pi+\frac12>\frac72.
\]

Consequently

\[
 k_{11}(\rho)^2=z_\rho^2+132
 >\frac{49}{4}+132
 =\frac{577}{4}>144,
\]

so

\[
 \boxed{k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).}
 \tag{13}
\]

No decimal approximation is used in (12)--(13).

## 6. Exact union and empty successor residual

Let \((\rho,K)\in\mathcal D_{20}\).  By (1), (12), and (13),

\[
 \frac7{51}<\rho<\frac{39}{50},
 \qquad K>k_{11}(\rho)>12.
 \tag{14}
\]

The trichotomy \(K<200\), \(K=200\), or \(K>200\) is exhaustive.  Its
exact theorem and bookkeeping behavior is:

| Boolean cell inside prospective \(\mathcal D_{20}\) | compact predicate \(12\leq K\leq200\) | aggregate predicate \(K\geq200\) | strict theorem available | unique subtraction owner |
|---|---:|---:|---|---|
| \(K<200\) | true by (14) | false | (C) | compact |
| \(K=200\) | true | true | both (C) and (T) | compact |
| \(K>200\) | false | true | (T) | aggregate |

Thus, with the seam deliberately assigned to the compact owner, define

\[
 \mathcal C_{21}:=\mathcal D_{20}\cap\{K\leq200\},
 \qquad
 \mathcal T_{21}:=\mathcal D_{20}\cap\{K>200\}.
\]

Then

\[
 \boxed{
 \mathcal D_{20}=\mathcal C_{21}\,\dot\cup\,\mathcal T_{21},
 \qquad
 \mathcal C_{21}\subset\operatorname{Dom}(C),
 \qquad
 \mathcal T_{21}\subset\operatorname{Dom}(T).}
 \tag{15}
\]

The theorem overlap at \(K=200\) is intentional evidence that there is no
analytic seam gap; the half-open bookkeeping choice in (15) prevents a
double subtraction.  Therefore, conditional on (1) becoming the accepted
Round 20 residual,

\[
 \boxed{
 \mathcal D_{21}^{\rm prospective}
 :=\mathcal D_{20}\setminus
 (\mathcal C_{21}\cup\mathcal T_{21})
 =\varnothing.}
 \tag{16}
\]

Every point removed in (16) satisfies the **strict** Pólya inequality, not
merely a non-strict comparison.

## 7. Exact face ownership

The distinction between theorem overcoverage and residual ownership is
essential.  In the table below, a frequency-face row retains the ratio
conditions from (1), and a ratio-face row retains the strict frequency
conditions from (1), unless the row explicitly says that the face is outside
the residual.  With that convention, the complete face table is:

| face | membership in prospective \(\mathcal D_{20}\) | theorem coverage | residual/bookkeeping owner |
|---|---|---|---|
| \(\rho=7/51\) | excluded because \(7/51<\rho_c\) | compact certificate includes it | none; rational certificate guard face only |
| \(\rho=\rho_c\) | allowed when \(k_{11}(\rho_c)<K<U(\rho_c)\) | compact for \(K\leq200\), aggregate for \(K\geq200\) | Round 21 split in (15), conditional on Round 20 acceptance |
| \(\rho=39/50\) | excluded by the strict upper ratio face in (1) | the relevant closed faces of both certificates include it | proposed Round 20 optical theorem owns it; Round 21 does not subtract it again |
| \(K=12\) | impossible by \(K>k_{11}>12\) | compact certificate includes it | none; compact guard face only |
| \(K=k_{11}(\rho)\) | excluded by the strict lower frequency face in (1) | not needed for (15) | proposed closed Round 20 staircase owns it |
| \(12<K<200\) | included exactly when \(k_{11}(\rho)<K<U(\rho)\) | compact | compact |
| \(K=200\) | included exactly when \(k_{11}(\rho)<200<U(\rho)\) | both compact and aggregate | compact by the convention in (15) |
| \(200<K<U(\rho)\) | included | aggregate | aggregate |
| \(K=K_0(\rho)=U(\rho)\) | excluded by the strict upper frequency face in (1) | no Round 21 coverage is needed | inherited upper face; not part of the residual |
| \(K>U(\rho)\) | excluded | the certificates may overcover according to the \(K=200\) split | none in the residual subtraction |

At intersections of faces, the same Boolean rules apply.  In particular,
\((\rho_c,200)\) is included only when it also satisfies the two strict
frequency inequalities in (1), and is then assigned to the compact owner;
\((39/50,200)\) is never in \(\mathcal D_{20}\), even though both theorem
domains contain it.

## 8. Why \(K_0=U\) has no further role

The equality \(K_0(\rho)=U(\rho)\) on the ratio interval in (1) is part of
the authenticated prospective Round 20 bookkeeping.  Neither Round 21
theorem depends on the formula, branch structure, size, or monotonicity of
that function.  The cover needs only the fact that a point presented as a
member of \(\mathcal D_{20}\) satisfies the strict upper condition
\(K<U(\rho)\).

For any fixed \(\rho\), all possible positions of that upper face are already
handled:

| position of \(U(\rho)\) relative to 200 | exact effect on the prospective fiber |
|---|---|
| \(U(\rho)<200\) | every residual point has \(K<200\), hence is compact-covered |
| \(U(\rho)=200\) | strictness \(K<U\) again puts every residual point in \(K<200\); the seam itself is excluded |
| \(U(\rho)>200\) | the fiber splits exactly into \(K\leq200\) and \(K>200\), covered as in (15) |

If a fiber were empty, it would be covered vacuously.  Thus no comparison
between \(U\) and 200, and no estimate on \(K_0\), is a missing premise.
The symbol \(K_0=U\) now serves only to name the prospective residual's
excluded upper face.

## 9. Theorem, certificate evidence, and source boundaries

Three logical levels must not be conflated.

1. The frozen Round 20 candidate supplies only the conditional set (1).  It
   supplies no spectral fact to either Round 21 proof.  Until Round 20 passes
   its remaining review, judge, and State Patch gates, (16) is prospective
   and cannot be promoted.
2. The compact and aggregate analytic bridges turn specified inequalities
   into strict spectral theorems.  Those bridges use only the authenticated
   packets and source-card scopes listed in Section 1.
3. The executable certificates supply rigorous outward interval evidence for
   the finitely many strict signs and exact partitions required by those
   bridges.  Their tests and adversarial audits validate implementation,
   authentication, precision gates, wall behavior, and coverage; a test
   count or an audit verdict by itself is not a theorem.

In particular, the displayed decimal margins are diagnostic only.  The
compact proof decision is the certain Arb inequality on each exact leaf.
The aggregate proof decisions are the certain Arb signs in (11), followed by
the exact derivative argument (8)--(10).  No grid sampling, decimal rounding,
or agent agreement is used as the mathematical sign proof.

## 10. Mandatory falsification cases

The following cases were treated as proof-breaking checks, not optional
diagnostics:

| falsification attempt | required outcome |
|---|---|
| any supplied artifact digest differs | reject this synthesis and refreeze the affected obligation |
| Round 20 is not accepted, or its residual bytes change | retain **NOT PROMOTED**; recompute the containment for the new residual |
| reverse reciprocation in (12), or weaken the strict \(\pi<22/7\) input | reject the lower-ratio containment |
| fail to establish \(k_{11}(\rho)>12\) uniformly from \(\rho_c\) | reject the compact containment because a lower-frequency gap may remain |
| use only \(K<200\) and \(K>200\) | reject: the face \(K=200\) is missing |
| assign \(K=200\) to both residual owners | reject the bookkeeping as a double subtraction, although both theorems remain true there |
| include \(\rho=39/50\), \(K=k_{11}\), or \(K=U\) in (1) | reject: each contradicts an authenticated strict face |
| replace \([x]_<\) by an ordinary floor at an integer wall | reject the compact spectral bridge |
| include a channel with \(\nu_\ell=K\) as spectrally active | reject the compact cutoff handling |
| reverse either corner monotonicity or skip \(\nu=\rho K\) | reject the compact leaf implication |
| accept an Arb interval overlapping zero, or use the display decimal for a proof decision | reject the relevant certificate |
| treat sampled positivity of \(\mathcal B\) as global positivity | reject the aggregate tail theorem |
| omit \(\mu>3/2\), \(K\eta_\rho>1\), the \(\rho=1/2\) branch, or a sign reversal in (8)--(10) | reject the aggregate bridge |
| assume an unproved relation between \(U\) and 200 | reject that step as unnecessary source expansion; use the exhaustive table in Section 8 instead |
| import a Round 20 Bessel-zero proof or broaden `annuli_polya.md` beyond its qualified scope | reject for source-scope leakage |

All of these checks pass for the authenticated bytes reviewed here.  Hence
the conditional coverage verdict is **PASS; first issue: none**.  Promotion
remains forbidden until Round 20 itself is accepted and the combined Round 21
claim completes its own independent review and state-synchronization gates.
