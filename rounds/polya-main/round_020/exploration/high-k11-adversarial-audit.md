# Round 20 adversarial audit: high-ratio extension through \(k_{11}\)

Status: **PASS**.

Date: 2026-07-15.

This audit assumed that the proposed implication on

\[
 \rho_c\leq\rho<\frac78,
 \qquad k_{10}(\rho)<K\leq k_{11}(\rho)
\]

was false and reconstructed the source bounds, inventory, cap ledger,
payments, endpoint ownership, and provenance independently. No edit to either
audited input was made.

## 1. Frozen inputs and byte audit

| artifact | required SHA-256 | reproduced SHA-256 | result |
|---|---|---|---|
| `sources/round20_k11_zero_bounds.md` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` | PASS |
| `rounds/polya-main/round_020/exploration/high-k11-extension.md` | `9faa7b75bb5b55cde24f63c613d03eb625457c9f99df03ad9a8bb563c9c22be1` | `9faa7b75bb5b55cde24f63c613d03eb625457c9f99df03ad9a8bb563c9c22be1` | PASS |

Both files decode as UTF-8, end in a line feed, and contain no BOM, NUL,
disallowed control byte, tab, Unicode replacement character, or trailing
horizontal whitespace. Their display-math delimiter counts agree; their
`aligned` and `array` environments are balanced.

Every local dependency hash printed in the two inputs was also reproduced:

| dependency | reproduced SHA-256 |
|---|---|
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `rounds/polya-main/round_020/exploration/high-k10-repair.md` | `0e6fdadc57cdf8e173fb1dc1dad5a1403664833ae722a81b66ba59d5b202704a` |
| `rounds/polya-main/round_020/exploration/high-k10-adversarial-audit.md` | `9ec17b81aea3d6b6899dd25dd07f0241963ca8b246544080ecea08857c697bb1` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |

## 2. Independent reconstruction of \(j_{5/2,3}>61/5\)

Set

\[
 R=\sin x-x\cos x,
 \qquad
 Q=(3-x^2)\sin x-3x\cos x.
\]

Direct differentiation reproduces

\[
 R'=x\sin x,
 \qquad Q'=xR.
\]

The signs

\[
\begin{array}{c|ccccccc}
x&\pi&3\pi/2&2\pi&5\pi/2&3\pi&7\pi/2&4\pi\\ \hline
R(x)&\pi&-1&-2\pi&1&3\pi&-1&-4\pi
\end{array}
\]

and the fixed sign of \(R'\) on each \(\pi\)-cell show that \(R\) has
exactly one zero in each of
\((\pi,3\pi/2)\), \((2\pi,5\pi/2)\), and
\((3\pi,7\pi/2)\). Since

\[
 Q(\pi)=3\pi,
 \quad Q(2\pi)=-6\pi,
 \quad Q(3\pi)=9\pi,
 \quad Q(4\pi)=-12\pi,
\]

the monotonic pieces of \(Q\) contain exactly one positive zero in each
of \((\pi,2\pi)\), \((2\pi,3\pi)\), and \((3\pi,4\pi)\). There is no
earlier positive zero because \(R,Q>0\) on \((0,\pi)\).

For \(a=61/5\) and \(\delta=4\pi-a\), the inherited enclosure
\(333/106<\pi<22/7\) gives

\[
 \frac{7\pi}{2}<a<4\pi,
 \qquad
 0<\delta<\frac\pi2,
 \qquad
 \delta>\frac{97}{265}.
\]

Exact reduction reproduces the decisive reserve

\[
 \frac{97}{265}-\frac{3a}{a^2-3}
 =\frac{111187}{966190}>0.
\]

Thus \(\tan\delta>\delta>3a/(a^2-3)\), and

\[
 Q(a)=\cos\delta\bigl((a^2-3)\tan\delta-3a\bigr)>0.
\]

The function is strictly decreasing on \((7\pi/2,4\pi)\) and is
negative at \(4\pi\), so its unique third zero lies strictly to the
right of \(a\). This proves the claimed strict bound without a numerical
zero table.

## 3. Independent reconstruction of \(j_{11/2,2}>129/10\)

Starting from \(P_0=\sin x\), \(P_1=\sin x-x\cos x\), an independent
polynomial recurrence calculation with

\[
 P_{n+1}=(2n+1)P_n-x^2P_{n-1}
\]

reproduces

\[
 P_5=(945-420x^2+15x^4)\sin x
     +(-945x+105x^3-x^5)\cos x.
\]

At \(b=129/10\), the two coefficients are exactly

\[
 A=\frac{692874243}{2000}>0,
 \qquad
 B=-\frac{14401867149}{100000}<0.
\]

Writing \(\varepsilon=b-4\pi\) and \(u=177/530\), the rational
\(\pi\)-enclosure gives \(0<\varepsilon<u<1\). The independent tangent
and coefficient-ratio calculations give

\[
 \frac38-\frac{u}{1-u^2/2}
 =\frac{90453}{4243768}>0,
\]

\[
 \frac{|B|}{A}-\frac38
 =\frac{69653091}{1710800600}>0.
\]

Consequently

\[
 P_5(b)=\cos\varepsilon(A\tan\varepsilon+B)<0.
\]

The third-zero exclusion used to interpret this sign is also valid.
Angular form comparison applied to the preceding strict bound gives

\[
 j_{11/2,3}^{,2}
 \geq j_{5/2,3}^{,2}+24
 >\frac{4321}{25}
 =b^2+\frac{643}{100}.
\]

Near zero, \(P_5(x)=x^{11}/10395+O(x^{13})>0\). Positive Bessel zeros
are simple by ODE uniqueness. Hence the negative sign at \(b\) forces an
odd number of positive zeros below \(b\), while the third-zero exclusion
allows at most two. Exactly one lies below \(b\); since \(P_5(b)<0\), the
second lies strictly above \(b\). No root-location approximation enters
this argument.

The same-index angular propagation was recomputed as

\[
 j_{p+1/2,3}^{,2}>
 \frac{3721}{25}+d_p-d_2
 =\frac{3571}{25}+d_p
 \quad(p\geq2),
\]

\[
 j_{p+1/2,2}^{,2}>
 \frac{16641}{100}+d_p-d_5
 =\frac{13641}{100}+d_p
 \quad(p\geq5).
\]

## 4. Qualified Lorch scope and shell transfer

The authenticated local source card states Lorch's strict first-zero
inequality for \(-1<\nu<\infty\) and explicitly records that the article
body is access-controlled. At \(\ell=10\), its exact half-integer
specialization is

\[
 j_{21/2,1}^{,2}>138\sqrt3-46.
\]

The target comparison is sign-safe:

\[
 138\sqrt3-46>\left(\frac{69}{5}\right)^2
 \iff 3450\sqrt3>5911,
\]

\[
 3450^2\cdot3-5911^2=767579>0.
\]

Thus \(j_{21/2,1}>69/5\). The source and extension correctly label this
as a qualified statement-level use of Lorch and use it only at radial
index one. The two higher-radial zero bounds above are internal.

The shell conclusions follow only after the separately proved
fixed-channel zero-extension min--max comparison

\[
 q_{p,n}^{\rm shell}(\rho)^2\geq j_{p+1/2,n}^{,2}.
\]

That division of labor is stated rather than attributed to Lorch.
Strict ball walls remain strict after the non-strict shell comparison.

## 5. Complete inventory and simultaneous restrictions

On the audited interval \(x=z_\rho^2>13\) and
\(K^2\leq x+132\). The inventory exclusions reconstruct as follows.

- For \(n\geq4\),
  \(q_{\ell,n}^2-K^2\geq15x+d_\ell-132>63\).
- For \(n=3,p\geq2\), if \(x\leq16\), the fixed wall gives
  \(q_{p,3}^2>3721/25>148\geq x+132\); if \(x>16\), the moving wall
  gives \(q_{p,3}^2-K^2\geq8x-126>2\).
- For \(n=2,p\geq5\), if \(x\leq34\), the fixed wall gives
  \(q_{p,2}^2>16641/100>166\geq x+132\); if \(x>34\), the moving wall
  gives \(q_{p,2}^2-K^2\geq3x-102>0\).
- For \(n=1,\ell\geq11\),
  \(q_{\ell,1}^2\geq x+d_\ell\geq x+132\geq K^2\).

Thus the displayed inventory is exhaustive:

\[
 (\ell,1),\ 0\leq\ell\leq10;
 \qquad
 (\ell,2),\ 0\leq\ell\leq4;
 \qquad
 (\ell,3),\ \ell=0,1.
\]

If any second mode is counted, \(4x+d_h<K^2\leq x+132\), hence
\(x<44\). If any third mode is counted, \(9x<K^2\leq x+132\), hence
\(x<33/2\). The ratio cutoffs are strict because

\[
 z(8/15)^2-44>
 \frac{725209}{550564}>0,
 \qquad
 z(1/4)^2-\frac{33}{2}>
 \frac{5871}{5618}>0.
\]

Therefore a second mode forces \(\rho<8/15\), and a third mode forces
\(\rho<1/4\); the defining mode is absent on each ratio face.

If \(H=10\), its strict first wall and the upper face give

\[
 x>\left(\frac{69}{5}\right)^2-132
 =\frac{1461}{25}>44,
\]

so no higher-radial mode coexists. If \(H=9\), similarly

\[
 x>\left(\frac{64}{5}\right)^2-132
 =\frac{796}{25}>\frac{33}{2},
\]

so no third mode coexists. Full multiplicity sums then reproduce the
five exceptional rows and the baseline row:

| first category | radial category | cap |
|---|---|---:|
| \(H=10\) | no second or third | 121 |
| \(H=9\) | no second or third | 100 |
| \(H=9\) | second present; no third | 125 |
| \(H=8\) | no third | 106 |
| \(H=8\) | third present | 110 |
| \(H\leq7\) | every inventoried radial mode | 93 |

These are exactly
\((H+1)^2\), plus at most \(25\) for second modes and \(4\) for third
modes. No omitted cell can exceed the listed cap.

## 6. Independent exact payment audit

For

\[
 F_{10}(\rho)=\mathcal W(\rho,k_{10}(\rho)),
\]

the derivative has the sign of

\[
 \pi^2(1+\rho)-110\rho^2(1-\rho)^2
 >9-\frac{110}{16}=\frac{17}{8}>0.
\]

Thus \(F_{10}\) is strictly increasing. The endpoint estimates
\(\rho_c<1/7\), \(z_{\rho_c}>18/5\), and
\(2/(9\pi)>7/99\) give \(F_{10}(\rho_c)>96\); the exact squared reserve
reproduces as

\[
 \left(\frac7{99}\frac{342}{343}\right)^2
 \left(\frac{3074}{25}\right)^3-96^2
 =\frac{109839239456}{4539390625}>0.
\]

Since the new band has \(K>k_{10}\), this pays the complete baseline cap
\(93\).

The five exceptional fixed-wall payments reproduce exactly:

| row | cutoff / split | lower payment | reserve over cap |
|---|---:|---:|---:|
| \(H=10\) | \(13/20\) | \(1482707121/11000000\) | \(151707121/11000000\) over 121 |
| \(H=9\), second | \(8/15\) | \(5253627904/41765625\) | \(32924779/41765625\) over 125 |
| \(H=9\), no second | \(3/5\) | \(179830784/1546875\) | \(25143284/1546875\) over 100 |
| \(H=8\), third | \(1/4\) | \(17537639/152064\) | \(810599/152064\) over 110 |
| \(H=8\), no third | \(3/7\) | \(28274969/261954\) | \(507845/261954\) over 106 |

The two ratio-localized rows are strict because both \(\rho<r\) and the
corresponding first-mode wall are strict. For the three split rows, the
fixed wall pays below the split and increasing \(F_{10}\) pays above it.
The required bridge comparisons have the independently reproduced
positive square reserves

\[
 k_{10}(13/20)^2-\left(\frac{69}{5}\right)^2
 >\frac{426449}{3441025},
\]

\[
 k_{10}(3/5)^2-\left(\frac{64}{5}\right)^2
 >\frac{8811001}{1123600},
\]

\[
 k_{10}(3/7)^2-\left(\frac{71}{6}\right)^2
 >\frac{317585}{1617984}.
\]

Both owners therefore hold on every bridge face, including the tight
\(H=8\), no-third cell. Every cap has a strict Weyl reserve.

## 7. Upper containment and strict faces

At \(\rho\leq7/8\), \(z\leq8\pi<176/7\), and hence

\[
 28^2-k_{11}^2
 >28^2-\left(\frac{176}{7}\right)^2-132
 =\frac{972}{49}>0.
\]

Thus \(k_{11}<28\). The inherited central floor exceeds \(64\) on
\(\rho_c\leq\rho<5/6\), while on the seam branch
\(U=54/(1-\rho)^2\geq1944\). Therefore \(k_{11}<U\) throughout the
subtracted high component.

The predecessor owns \(K=k_{10}\); the new proof uses \(K>k_{10}\).
The face \(K=k_{11}\) is included, but the moving lower bound for
\((11,1)\) equals that face and the strict spectral count excludes it.
The fixed-wall splits at \(x=16,34\), the ratio faces, and the three
payment bridges all have owners with positive reserves. The proof is
strict at \(\rho=\rho_c\), remains valid at \(\rho=7/8\), and the
residual subtraction correctly leaves that already-owned endpoint out.
The seam at \(5/6\) changes only the inherited upper-floor formula.

## 8. Verdict

**PASS.** The assumption that the band through \(k_{11}\) fails produces
no unsupported implication. Both internal higher-radial zero bounds, the
qualified first-zero specialization, every angular propagation, the
complete inventory, all simultaneous-mode exclusions, all five
exceptional caps and their exact payments, the baseline row, strict
faces, endpoint ownership, upper-floor containment, provenance, hashes,
and byte hygiene independently reproduce.

First issue: **none**.
