# Round 19 two-sided staircase: independent exact-constant audit

Date: 2026-07-14

Role: A4 exact-constant auditor

Candidate baseline: `5814b335a108d3af25aadde312dcc9581172e9f6`

Verdict: **PASS** for the finite exact-arithmetic audit.

First failed finite obligation: **none**.

This verdict has a deliberately narrow meaning.  The executable authenticates
the frozen candidate and all six permitted dependencies, and it proves the
decisive finite comparisons, payments, inventories, face truth tables, and set
subtraction without floating-point arithmetic.  It cannot certify functional
analysis, elementary real analysis, or the truth of an external source
statement.  Those analytic assumptions are isolated in section 10.  Thus this
PASS is the independent exact-constant audit required by the freeze; it does
not replace the separately required isolated analytic reconstruction.

## 1. Isolation and provenance

I began from the named freeze record and first authenticated the candidate as

`state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md`

with SHA-256

`87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db`.

Before the initial verdict I read only that candidate, the freeze record, and
the following six whitelisted inputs.  Every hash matched.

| permitted input | expected and observed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `rounds/polya-main/round_019/exploration/residual-mask-freeze.md` | `0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |

The named freeze record itself was also byte-locked at

`7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff`.

I did not inspect either incumbent proof, any Round 19 crossing ledger or
prior constant computation, the source-audit or clean-room reviews, any
cross-review, or a judge draft.

## 2. Exact arithmetic policy

The verifier uses integers and Python `Fraction` objects only.  Its test suite
parses the source and rejects any floating-point literal.  All comparisons
with a square root are made only after recording positivity and squaring.

The enclosure

\[
\frac{333}{106}<\pi<\frac{22}{7}
\]

is independently recertified using Machin's identity

\[
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}
\]

and adjacent rational partial sums of the alternating arctangent series.  The
resulting rational interval lies strictly inside the displayed enclosure.  In
particular, the lower and upper excesses checked by the program are

\[
\frac{33576162533984009852391922109981794528004735231}
{403464465426118743450846031748369336128234863281250}>0
\]

and

\[
\frac{10182316936852813198451920111950074552337051872654}
{8052513532356858401347231369496367871761322021484375}>0.
\]

Using opposite endpoints of this interval independently is conservative.  For
example, a lower bound for a fixed-frequency payment is

\[
\mathcal W(\rho,t)>
\frac{2(1-\rho^3)t^3}{9(22/7)},
\]

whereas at a moving wall \(k_q=\sqrt{z_\rho^2+q}\) the program uses

\[
A=\frac{2(1-\rho^3)}{9(22/7)},\qquad
S=\frac{(333/106)^2}{(1-\rho)^2}+q
\]

and proves \(A^2S^3>C^2\) after checking \(A,S,C>0\).  No decimal
approximation decides a sign.

## 3. Spectral comparison ledger

The permitted separated-spectrum packet gives the strict convention

\[
N_D(A_{\rho,1},K^2)
=\sum_{\ell\ge0}(2\ell+1)\#\{n:k_{\ell,n}<K\}.
\]

The elementary one-dimensional min--max comparison gives

\[
k_{\ell,n}^2\ge
\left(\frac{n\pi}{1-\rho}\right)^2+\ell(\ell+1),
\tag{3.1}
\]

with equality \(k_{0,n}=n z_\rho\) for \(\ell=0\).  Thus the first-mode
moving walls are \(k_m\), and the second \(\ell=1\) wall is \(p_1\).

For completeness, the required fixed-channel shell-to-ball comparison has
the following form-domain proof.  In the transformed radial variable
\(u=rR\), a shell test function lies in \(H_0^1(\rho,1)\).  Extend it by
zero to \((0,\rho]\).  Its zero trace at \(\rho\) makes the extension an
element of \(H_0^1(0,1)\); it vanishes near zero, so the centrifugal term is
finite.  Tensoring with the same spherical harmonic preserves the fixed
\(\ell\) subspace, and the ball and shell Rayleigh quotients agree on the
extension.  The shell fixed-channel form domain is therefore isometric to a
subspace of the ball fixed-channel form domain.  Min--max at the same radial
index gives

\[
k^{\rm shell}_{\ell,n}(\rho)\ge j_{\ell+1/2,n}.
\tag{3.2}
\]

This argument does not use unlabelled domain monotonicity and does not change
\(\ell\) or \(n\).

Likewise, Hardy's inequality puts all relevant ball radial forms on the same
domain, and

\[
q_{\ell+1}[u]-q_\ell[u]
=2(\ell+1)\int_0^1\frac{|u|^2}{r^2}\,dr
\ge2(\ell+1)\lVert u\rVert_2^2.
\]

Hence min--max, again at fixed \(n\), yields

\[
j_{\ell+3/2,n}^2
\ge j_{\ell+1/2,n}^2+2(\ell+1).
\tag{3.3}
\]

The executable does not prove the Sobolev and min--max statements in this
section; it verifies every numerical consequence used below.

## 4. Zero bounds and radical arithmetic

The four Lorch specializations reduce to the exact positive certificates

\[
\frac{105}{4}-\left(\frac{51}{10}\right)^2=\frac6{25},
\]

\[
81^2\cdot5-178^2=1121,
\qquad
66^2\cdot15-247^2=4331,
\]

and

\[
507^2\cdot77-4264^2=1611077.
\]

The associated radical denominators are positive because
\(\sqrt5>1\), \(\sqrt{15}>2\), and \(\sqrt{77}>5\).  These certify the
first-mode thresholds \(51/10,13/2,15/2,17/2\) in channels
\(\ell=2,3,4,5\).

The permitted second-zero card gives

\[
2\pi<\frac{77}{10}<\frac{5\pi}{2},\qquad
\frac{5\pi}{2}-\frac{77}{10}
>\frac{163}{1060}>\frac{10}{77},
\]

so \(j_{3/2,2}>77/10\).

Two additional elementary bounds are needed and were reconstructed rather
than imported.

First, the positive zeros of the spherical \(j_1\) solve \(\tan x=x\).
There is no root in \((0,\pi)\), and exactly one in
\((\pi,3\pi/2)\).  Since

\[
\pi<4<\frac{3\pi}{2},\qquad
y=\frac{3\pi}{2}-4>\frac14,
\]

we have \(\tan4=\cot y<1/y<4\); hence \(j_{3/2,1}>4\).

Second,

\[
\mathsf j_2(x)
=\frac{(3-x^2)\sin x-3x\cos x}{x^3}.
\]

On \((0,\pi/2)\), the numerator has derivative
\(x(\sin x-x\cos x)>0\) and starts at zero.  It is visibly positive on
\((\pi/2,\sqrt3)\).  For \(x>\sqrt3\), away from tangent poles, its
zeros solve

\[
R(x):=\tan x+\frac{3x}{x^2-3}=0.
\]

At every such zero, exact substitution reduces the derivative numerator to

\[
(x^2-3)^2+9x^2-3(x^2+3)=x^4>0.
\]

Thus every zero is an upward crossing.  The seven cells

\[
(0,\pi/2),\ (\pi/2,\sqrt3),\ (\sqrt3,\pi),\
(\pi,3\pi/2),\ (3\pi/2,2\pi),\
(2\pi,5\pi/2),\ (5\pi/2,3\pi)
\]

contain respectively \(0,0,0,0,1,0,1\) positive zeros.  This follows from
the endpoint signs, the positive-tangent halves, and the upward-crossing
property; it includes every tangent half-period before the second root.
Finally,

\[
\frac{5\pi}{2}<9<3\pi,\qquad
3\pi-9>\frac{45}{106}>\frac9{26}.
\]

Writing \(y=3\pi-9\),
\(R(9)=-\tan y+9/26<0\).  The unique zero in the last cell is therefore
strictly to the right of 9:

\[
\boxed{j_{5/2,2}>9}.
\]

Equations (3.2)--(3.3) now give the decisive remainder exclusions

\[
\left(\frac{17}{2}\right)^2+12
=\frac{337}{4}=d^2,
\]

with a strict first inequality inherited from \(j_{11/2,1}>17/2\), and

\[
9^2+6-d^2=\frac{11}{4}>0.
\]

Thus first modes with \(\ell\ge6\) and second modes with \(\ell\ge3\)
are absent through \(K=d\).  Also
\((3\pi)^2>d^2\), so every \(n\ge3\) mode is absent.

## 5. Derivatives and uniform substitutions

For fixed \(K\), \(\mathcal W(\rho,K)\) decreases strictly with \(\rho\).
At a moving wall \(k_q=\sqrt{z_\rho^2+q}\), clearing the positive
denominators in the logarithmic derivative reduces its sign exactly to

\[
D_q(\rho)
=\pi^2(1+\rho)-q\rho^2(1-\rho)^2.
\tag{5.1}
\]

The program verifies the polynomial reduction separately for
\(q=0,2,6,12,20,30,42\).  Since

\[
\rho^2(1-\rho)^2\le\frac1{16},\qquad
\pi^2>9>\frac{42}{16},
\]

all these moving payments increase strictly with \(\rho\).  No denominator
or sign is discarded.

The other two extremal substitutions are

\[
\mathcal W(\rho,2z_\rho)
=\frac{16\pi^2}{9}\frac{1+\rho+\rho^2}{(1-\rho)^2},
\]

whose rational factor has derivative
\(3(1+\rho)/(1-\rho)^3>0\), and

\[
\mathcal W(\rho,L(\rho))
=\frac{\rho^{-3}-1}{36\pi},
\]

whose derivative is \(-1/(12\pi\rho^4)<0\).

## 6. High-ratio staircase

The first-mode multiplicities are

\[
1,3,5,7,9,11,13,
\]

and their cumulative sums through \(\ell=5\) are

\[
1,4,9,16,25,36.
\]

For \(\ell=2,3,4,5\), entry requires
\(K>\max\{k_\ell,c_\ell\}\).  On the low side of the proposed ratio
split, the fixed threshold pays; on the high side, the increasing moving
threshold pays.  The following table gives exact positive margins.  In the
last column the displayed integer is the numerator of
\(A^2S^3-C^2\); its denominator is positive.

| entry | cap | split | fixed-payment margin | moving squared-margin numerator |
|---|---:|---:|---:|---:|
| \(\ell=2\) | 9 | \(3/10\) | \(1387329/11000000\) | `1399810848073457853053` |
| \(\ell=3\) | 16 | \(1/2\) | \(6277/6336\) | `137027505353736631` |
| \(\ell=4\) | 25 | \(1/2\) | \(775/704\) | `2507119282010251109` |
| \(\ell=5\) | 36 | \(13/25\) | \(452843/343750\) | `92672404686738742434741` |

At the first two entries, the exact lower margins are

\[
\mathcal W(\rho_c,z_{\rho_c})-1
>\frac{40567}{16854}>0
\]

and, after positive squaring at \(k_1\),

\[
A^2S^3-4^2
=\frac{122885180711351123434093163}
{73312671539055414127495744}>0.
\]

The second \(\ell=0\) entry can raise the maximum count only to 26.  At
the left endpoint,

\[
\mathcal W(\rho_c,2z_{\rho_c})-26
>\frac{10582}{8427}>0,
\]

and this payment increases with \(\rho\).  Since \(p_1>2z\), a second
\(\ell=1\) entry automatically includes the preceding one.  It can occur
below \(k_6\) only for \(\rho<1/5\); at the fixed threshold \(77/10\),

\[
\mathcal W\left(\frac15,\frac{77}{10}\right)-29
>\frac{849901}{281250}>0.
\]

The proposed inventories are exhaustive.  At \(\rho=1/4\), directed
exact bounds give

\[
\left(\frac{17}{2}\right)^2-k_6^2
>\frac{22385}{1764}>0,
\qquad
(2z)^2-k_6^2
>\frac{29874}{2809}>0.
\]

Hence on \([\rho_c,1/4]\) the only possible modes are first modes
\(0\le\ell\le4\) and second modes \(\ell=0,1\); on
\([1/4,7/8]\) all second modes are absent and only first modes
\(0\le\ell\le5\) can occur.  The extra \(\ell=1,n=2\) exclusion at
\(\rho=1/5\) has square margin

\[
p_1^2-k_6^2>\frac{1125635}{179776}>0.
\]

Finally \(k_6<3z\) has margin
\(8z^2-42>103800/2809\) at the coarsest lower bound.  Thus no omitted
radial index enters.  Equality at any spectral wall is excluded by
\(k_{\ell,n}<K\), including simultaneous cross-order coincidences; the
multiplicities add immediately above the face.  This proves every high
staircase cap through the included face \(K=k_6\), conditional only on the
analytic comparisons in section 3.

## 7. Lower-ratio staircase

The fixed thresholds have the exact order

\[
4<\frac{51}{10}<\frac{13}{2}<\frac{15}{2}
<\frac{77}{10}<\frac{17}{2}<9<d,
\]

where \(4\cdot9^2<337<19^2\).  Throughout the lower band,

\[
\frac{13}{2}<2z_\rho<\frac{15}{2}.
\]

The verifier's exact endpoint margins are \(252/1007\) on the left and
\(3/14\) on the right.  Thus the nominal \(K>2z\) row below \(13/2\)
is empty, while both one-sided traces are active between \(13/2\) and
\(15/2\).  At \(K=2z\), the second radial mode is still excluded.

The full count reconstructed from strict entries is

\[
\begin{aligned}
1
&+3\,\mathbf1_{K>4}
+5\,\mathbf1_{K>51/10}
+7\,\mathbf1_{K>13/2}
+9\,\mathbf1_{K>15/2}\\
&+11\,\mathbf1_{K>17/2}
+\mathbf1_{K>2z}
+3\,\mathbf1_{K>77/10}
+5\,\mathbf1_{K>9}.
\end{aligned}
\]

It reproduces, including every equality face, the caps

\[
1,4,9/10,16/17,26,29,40,45
\]

in the candidate table.  The executable checks 50 exact table cases, using
three positions of \(2z\) and explicitly including \(K=2z\).

For each fixed threshold, the worst ratio is the limiting right face
\(\rho_c\).  The exact positive lower margins are:

| threshold | cap | rational lower margin |
|---:|---:|---:|
| \(4\) | 4 | \(40610428/79079627\) |
| \(51/10\) | 9 | \(224639392167/632637016000\) |
| \(13/2\) | 16 | \(17044071001/5061096128\) |
| \(15/2\) | 26 | \(18990895547/5061096128\) |
| \(77/10\) | 29 | \(183841479851/57512456000\) |
| \(17/2\) | 40 | \(16755137701/5061096128\) |
| \(9\) | 45 | \(4056483573/632637016\) |

For the first band, strict \(K>L\) and the moving-\(L\) formula give the
same positive cap-1 margin \(40567/16854\).  For either split row above
\(2z\),

\[
\mathcal W(\rho,2z)-17
>\frac{1531}{2809}>0,
\]

so it pays both 10 and 17.

The remaining-mode exclusions in section 4 leave exactly first modes
\(0\le\ell\le5\) and possible second modes \(0\le\ell\le2\), whose
total multiplicity is

\[
36+(1+3+5)=45.
\]

It remains valid at the included upper face \(K=d\).  The crossings of
\(L\) with \(9,17/2,77/10,15/2,13/2,51/10,4\) occur, in increasing
ratio order, at

\[
\frac1{18},\frac1{17},\frac5{77},\frac1{15},
\frac1{13},\frac5{51},\frac18.
\]

Together with \(L=d\) at \(\rho=1/\sqrt{337}\), these eight faces account
for every empty or degenerate lower subband.

## 8. Comparisons with the inherited upper floor

Write \(C_0=1+8\sqrt2/15\).  The identities

\[
1+2C_*=2C_0,
\qquad
\rho_*=\frac{\omega_0}{2C_0}
\]

give

\[
H_0(\rho_*)=\frac{C_0}{\omega_0}.
\]

Moreover, on the low-ratio \(K_0\) branch, \(\eta=\omega_0\) and the
displayed positive-root formula gives \(K_0\ge C_0/\omega_0\).  The
directed elementary bounds

\[
\frac{13}{132}<\omega_0<\frac18,
\quad C_0>\frac{131}{75},
\quad d<\frac{19}{2}
\]

give

\[
C_0-d\omega_0>
\frac{131}{75}-\frac{19}{16}
=\frac{671}{1200}>0.
\]

Since \(H_0\) increases, this proves

\[
d<U(\rho)\qquad(\rho_*<\rho<\rho_c)
\]

on both active low-ratio branches, including the shared \(H_0=K_0\) face.
It also proves \(\rho_*<1/\sqrt{337}\).

For \(k_6<U\), let
\(f(K)=\eta K-\sqrt{aK}-C_0\); \(K_0\) is its unique positive root.
On \([\rho_c,1/2]\),
\(\eta<1/8\), \(k_6<10\), and \(10/8<C_0\), hence
\(f(k_6)<0\).  On \([1/2,5/6)\),
\(\eta\le\omega_0<1/8\), \(k_6<20\), while
\(a\ge2\pi>6\) and \(k_6\ge2\pi>6\).  Thus
\(\sqrt{ak_6}>6>20/8>\eta k_6\), again giving \(f(k_6)<0\).
Finally, on \([5/6,7/8)\), exact coarse bounds give
\(k_6<27\) and

\[
U(\rho)=\frac{54}{(1-\rho)^2}\ge1944>27.
\]

Therefore

\[
k_6(\rho)<U(\rho)
\qquad(\rho_c\le\rho<7/8).
\]

The ratio order is also exact:

\[
\rho_*<\frac1{\sqrt{337}}
<\frac{9407}{100000}<\rho_{HK}
<\frac{94071}{1000000}<\omega_0<\rho_c
<\frac15<\frac14<\frac3{10}<\frac12
<\frac{13}{25}<\frac56<\frac78.
\]

The strict middle comparison has rational margin
\(13/132-94071/10^6=145657/33000000\).

## 9. Exact subtraction and faces

The inherited residual is

\[
\begin{aligned}
\mathcal D_{18}={}&
\{\rho_*<\rho<\rho_c,\ L<K<U\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_5<K<U\}.
\end{aligned}
\]

The comparisons in section 8 prove both proposed additions are subsets.
Subtracting the lower addition removes the closed frequency interval
\((L,d]\) only when \(\rho>1/\sqrt{337}\).  At
\(\rho=1/\sqrt{337}\), \(L=d\) and the addition is empty, so the full
strict slice \(L<K<U\) remains.  Subtracting the high addition removes
\((k_5,k_6]\).  Therefore

\[
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le1/\sqrt{337},\ L<K<U\}\\
&\cup\{1/\sqrt{337}<\rho<\rho_c,\ d<K<U\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6<K<U\}.
\end{aligned}
\]

The verifier checks this identity on 63 vertical/frequency face cells,
including every equality and both one-sided traces.  It separately checks 19
mandatory frequency-face semantics.  The upper candidate faces \(K=d\) and
\(K=k_6\) are included and therefore absent from the remainder; the inherited
\(K=U\) face is excluded from the residual.  The \(\rho=\rho_*\) and
\(\rho=7/8\) endpoint slices remain covered, while \(\rho=\rho_c\) belongs
to the high component.

The ten admissible Boolean cases satisfying
\(B_0\cup B_1\subset\mathcal A_{18}\), hence
\((B_0\cup B_1)\cap\mathcal D_{18}=\varnothing\), were also exhausted.
They confirm that neither box is subtracted again.

## 10. What the executable does not prove

The following are explicit analytic assumptions, not hidden numerical steps:

1. Machin's identity and the alternating-series remainder theorem.  The
   rational partial sums and all comparisons after those facts are exact.
2. The separated shell spectrum, multiplicity \(2\ell+1\), radial
   simplicity, and strict endpoint convention in the permitted spectral
   packet.
3. The one-dimensional Poincare/min--max inequality (3.1) and the exact
   \(\ell=0\) frequencies.
4. The Sobolev form-domain extension and fixed-channel min--max argument
   (3.2).  The argument is reconstructed in section 3, but Python does not
   certify Sobolev traces or min--max.
5. Hardy's inequality and the ball angular-shift min--max argument (3.3),
   including preservation of radial index.
6. The truth and declared scope of the five externally permitted Bessel-zero
   statements.  The audit verifies all displayed specializations and radical
   comparisons, not the inaccessible body of Lorch's paper.
7. The elementary spherical-Bessel identities and real-variable tangent
   monotonicity used in section 4.  The half-period inventory and all endpoint
   arithmetic are exact in the executable.
8. The inherited residual predicate, the active \(U\) branches, uniqueness
   and equality at \(\rho_{HK}\), and prior absorption of \(B_0,B_1\).
9. Monotonicity of \(G_1\) on \([1/2,1)\), obtained analytically by
   differentiating its displayed formula.

The first implication that the executable alone cannot establish is item 1
in program order (the real-analysis justification of the Machin enclosure).
The first spectral implication it cannot establish is item 2.  Neither is a
failed finite obligation; both are declared proof boundaries.

## 11. Executable result and tests

Commands:

```powershell
python computations/round19_verify_two_sided_staircase.py --self-check --manifest
python -m pytest computations/tests/test_round19_verify_two_sided_staircase.py -q
```

Results at freeze time:

- verifier: **PASS**, 245 exact checks, first failed obligation `null`;
- provenance: candidate, freeze record, and exactly six whitelisted inputs
  authenticated;
- lower cap truth table: 50 cases;
- residual face truth table: 63 cases;
- absorbed-box truth table: 10 cases;
- mandatory frequency faces: 19;
- focused tests: **24 passed**;
- no floating-point literals in the verifier.

Output hashes before this report was added:

| output | SHA-256 |
|---|---|
| `computations/round19_verify_two_sided_staircase.py` | `4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23` |
| `computations/tests/test_round19_verify_two_sided_staircase.py` | `58c8254fac42f5e41702a305be32df2d294af98ae3bacc464e9efeac7e1f45e8` |

**Final finite-audit verdict: PASS; first failed obligation: none.**
