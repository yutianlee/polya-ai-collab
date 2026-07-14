# Round 21 scoped candidate: exact closure of D20

Date: 2026-07-15

Status: replacement candidate packet; not itself a promotion

## Supersession rule

This packet replaces
`state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md`
(SHA-256
`415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3`)
as the authenticated Round 21 candidate input.  The earlier packet omitted
the essential upper ratio wall from one displayed guard.  Its bytes remain
frozen as rejected-scope chronology; no unqualified assertion about
`rho>=rho_c` is imported here.

No finite certificate, analytic identity, residual face, or subtraction
owner changes.  The sole mathematical correction is that the lower-frequency
guard is asserted exactly on the shell ratio domain

\[
\rho_c\leq\rho<1.
\]

## Definitions and inherited residual

Let

\[
\rho_c=\frac{1}{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_{11}(\rho)=\sqrt{z_\rho^2+132},
\]

and

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

The accepted Round 20 residual is exactly

\[
\mathcal D_{20}=\left\{(\rho,K):
\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\]

All four displayed walls retain their inherited ownership: `rho=rho_c` is
included subject to the strict frequency inequalities, whereas `rho=39/50`,
`K=k_11(rho)`, and `K=U(rho)` are outside `D20`.

## Required theorem inputs

The compact theorem proves the strict shell inequality

\[
N_D(A_{\rho,1},K^2)<W(\rho,K)
\]

on the closed rectangle

\[
\frac7{51}\leq\rho\leq\frac{39}{50},
\qquad 12\leq K\leq200.
\]

The aggregate theorem proves the same strict inequality on

\[
\rho_c\leq\rho\leq\frac{39}{50},
\qquad K\geq200.
\]

The aggregate executable certificate supplies only the finite base
predicates at `K=200`.  The universal conclusion for `K>=200` belongs to the
separate analytic derivative, curvature, and two-integration argument.

## Exact guards with their full domain

The rational upper enclosure `pi<22/7` gives

\[
14\pi<44
\quad\Longrightarrow\quad
7(1+2\pi)<51
\quad\Longrightarrow\quad
\boxed{\frac7{51}<\rho_c}.
\]

For the second guard, assume exactly `rho_c<=rho<1`.  Then

\[
0<1-\rho\leq1-\rho_c,
\]

so division by the positive denominators gives

\[
z_\rho=\frac{\pi}{1-\rho}
\geq\frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72.
\]

Consequently,

\[
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132
=\frac{577}{4}>144,
\]

and therefore

\[
\boxed{k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).}
\]

The upper wall is logically necessary.  At `rho=1`, `z_rho` is undefined.
At `rho=2`, `z_rho=-pi` and the exact enclosure gives

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144,
\]

so the unqualified claim for every `rho>=rho_c` is false.

Every point of `D20` satisfies the corrected guard because
`rho<39/50<1`.

## Exact disjoint split

Define the subtraction owners

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

Then

\[
\mathcal D_{20}=\mathcal C_{21}\mathbin{\dot\cup}\mathcal T_{21}.
\]

The shared theorem face `K=200` is compact-owned, so it is never subtracted
twice.  The three possible orderings `U(rho)<200`, `U(rho)=200`, and
`U(rho)>200` are all covered by this definition.  The proposed successor is

\[
\boxed{\mathcal D_{21}=\varnothing}.
\]

## Evidence-role boundary

- The compact interval certificate owns only its 10,580-leaf finite
  rectangle and strict proxy comparisons.
- The aggregate interval certificate owns only its 1,286 base boxes and
  outward predicates at `K=200`.
- The analytic proof owns both spectral bridges, the all-frequency aggregate
  propagation, the exact guard derivations, and the residual split.
- The exact wrapper owns byte authentication, schema validation, finite
  replay, exact sign-row enumeration, and the scoped guard constants.

This packet does not promote `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, or `POLYA-program-target`.
It does not assert novelty, tiling consequences, arbitrary-radius scaling,
or a theorem beyond the exact Round 21 lemma.

## Scope corrections to frozen predecessors

The following committed artifacts contain an unqualified occurrence of the
guard.  They remain immutable, but that occurrence is rejected and replaced
by the boxed scoped statement above:

| frozen artifact | SHA-256 | accepted use after this packet |
| --- | --- | --- |
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` | historical candidate and all formulas unrelated to the rejected quantifier |
| `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md` | `0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc` | analytic reconstruction restricted to the displayed D20 ratio domain |
| `rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md` | `aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca` | compact finite-certificate audit only |
| `rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md` | `d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56` | superseded A4 cycle; retained as negative chronology |
| `rounds/polya-main/round_021/reviews/exact-d20-closure-cross-comparison-replacement.md` | `e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e` | comparison conclusions only after applying this domain correction |

Any later positive review must authenticate this packet, the final corrected
wrapper and tests, and a corrected A4 replay report.  It must reject the old
literal `k11(rho)>12 for rho>=rho_c` and must not broaden the conclusion past
`rho<1`.
