# Adversarial audit: repaired high-ratio step through \(k_{10}\)

Status: **PASS**.

Date: 2026-07-15.

I audited the proposed extension under the contrary hypothesis that the
claim on \(k_9<K\leq k_{10}\) is false.  I reconstructed the three new
zero bounds, the full radial/angular inventory, every coexistence
restriction and cap, every fixed or moving Weyl payment, and all strict
faces.  No numerical Bessel-zero table or root solver is used in the
argument below.

## 1. Frozen targets, bytes, and dependency identity

The two audited targets have the requested identities:

| artifact | recomputed SHA-256 |
|---|---|
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` |
| `rounds/polya-main/round_020/exploration/high-k10-repair.md` | `0e6fdadc57cdf8e173fb1dc1dad5a1403664833ae722a81b66ba59d5b202704a` |

Both files decode as UTF-8, have no BOM, NUL, DEL, or other forbidden
control byte, use LF line endings, end in a newline, and contain no tab
or trailing whitespace.  Their byte lengths are respectively 8223 and
14221.

The hashes of all five locally cited inputs also recompute exactly:

| dependency | recomputed SHA-256 |
|---|---|
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |

## 2. Independent reconstruction of the zero bounds

### 2.1 The second order-\(7/2\) zero

For spherical order three, the inherited DLMF reduction has numerator

\[
 P_3(x)=(15-6x^2)\sin x+(x^3-15x)\cos x.
\]

The derivative chain

\[
 R'=x\sin x,\qquad Q'=xR,\qquad P_3'=xQ
\]

reconstructs the root order: there is no positive root through
\(2\pi\), exactly one first root in \((2\pi,5\pi/2)\), no root from
\(5\pi/2\) to \(3\pi\), and exactly one second root in
\((3\pi,7\pi/2)\).  On the last cell \(Q>0\), hence \(P_3\) is
strictly increasing.

At \(a=103/10\), write \(y=a-3\pi\).  The enclosure
\(333/106<\pi<22/7\) gives

\[
 0<y<\frac{232}{265}<1.
\]

The alternating Taylor bounds are sign-safe on this interval.  Their
exact endpoint comparison recomputes as

\[
 \frac54\left(1-\frac{u^2}{2}+\frac{u^4}{24}
 -\frac{u^6}{720}\right)
 -\left(u-\frac{u^3}{6}+\frac{u^5}{120}\right)
 =\frac{409676235487517}{12467453135062500}>0,
\]

where \(u=232/265\).  Thus \(\tan y<5/4\).  Independently,

\[
 \frac{a(a^2-15)}{6a^2-15}-\frac32
 =\frac{5917}{621540}>0.
\]

Since \(\cos y>0\), this makes

\[
 P_3(a)=\cos y\big((6a^2-15)\tan y-a(a^2-15)\big)<0.
\]

Strict increase on the unique second-root cell therefore proves

\[
 j_{7/2,2}>\frac{103}{10}.
\]

### 2.2 Propagation at radial index two

The fixed-channel unit-ball form difference is at least
\(d_p-d_3\) for \(p\geq3\).  Min--max at the same radial index gives

\[
 j_{p+1/2,2}^2
 \geq j_{7/2,2}^2+d_p-12
 >\frac{9409}{100}+d_p.
\]

For \(p=4,5,6\), the three exact squares are

\[
 \frac{11409}{100}>\left(\frac{53}{5}\right)^2,
 \qquad
 \frac{12409}{100}>11^2,
 \qquad
 \frac{13609}{100}>\left(\frac{23}{2}\right)^2.
\]

This verifies the propagated \(q_{4,2}\) and \(q_{5,2}\) walls and the
second-zero barrier used in the next recurrence argument.

### 2.3 The repaired first order-\(15/2\) zero

For \(P_n=x^{n+1}\mathsf j_n\), the two DLMF recurrences give exactly

\[
 P_{n+1}=(2n+1)P_n-x^2P_{n-1},\qquad P_n'=xP_{n-1}.
\]

Starting with \(P_0=\sin x\) and
\(P_1=\sin x-x\cos x\), I recomputed every polynomial coefficient.
The displayed \(P_6\) and \(P_7\) in the source card agree
coefficient-for-coefficient.  At \(a_0=54/5\), the \(P_6\)
coefficients recompute to

\[
 A_6=\frac{11397242079}{15625}>0,
 \qquad
 B_6=-\frac{5033180754}{3125}<0.
\]

With \(\delta=7\pi/2-a_0\), one has \(0<\delta<1/5\) and

\[
 \tan\delta<\frac{10}{49}<\frac14<\frac{A_6}{|B_6|};
\]

the final strict comparison has numerator reserve
\(20423064546\).  Hence \(P_6(a_0)<0\).  Since
\(P_6(x)=x^{13}/135135+O(x^{15})>0\) near zero, its first positive
zero lies below \(a_0\).  The propagated bound

\[
 j_{13/2,2}^2>\frac{13609}{100}>left(\frac{23}{2}\right)^2
\]

puts its second positive zero above \(b_0=23/2\).  Therefore
\(P_6<0\) on all of \([a_0,b_0]\), so \(P_7'=xP_6<0\) there.

At \(b_0\), the recomputed coefficients are

\[
 A_7=-\frac{284564833}{16},
 \qquad
 B_7=-\frac{3153151489}{128}.
\]

For \(v=4\pi-b_0\), the rational enclosure gives
\(113/106<v<\pi/2\).  The two exact reserves are

\[
 \frac{113}{106}+\frac13\left(\frac{113}{106}\right)^3
 -\frac75
 =\frac{1248169}{17865240}>0,
\]

\[
 \frac75-\frac{|B_7|}{|A_7|}
 =\frac{169873203}{11382593320}>0.
\]

Thus \(\tan v>|B_7|/|A_7|\) and \(P_7(b_0)>0\).  Since \(P_7\)
is decreasing on \([a_0,b_0]\), it is positive throughout that
interval.  The already-audited Lorch seed
\(j_{15/2,1}>54/5\) excludes every earlier zero, so

\[
 j_{15/2,1}>\frac{23}{2}.
\]

This is an internal recurrence strengthening after the one first-zero
Lorch seed; it is not a stronger theorem attributed to Lorch.

### 2.4 The narrow order-\(19/2\) Lorch use

At angular index nine, the authenticated first-zero formula specializes
to

\[
 j_{19/2,1}^2>
 R_9=\frac{63\sqrt{165}-147}{4}.
\]

The comparison with \((64/5)^2\) reduces to
\(1575\sqrt{165}>20059\).  Both sides are positive, and the exact
squared reserve recomputes to

\[
 1575^2\cdot165-20059^2=6939644>0.
\]

This proves only \(j_{19/2,1}>64/5\), at radial index one.  No step
uses Lorch for a second zero, a shell cross-product zero, or a
shell-specific statement.  Zero extension and fixed-channel min--max
then transfer all three strict ball walls to the corresponding shell
channels without changing radial index.

## 3. Exhaustive mode inventory

On \(\rho_c\leq\rho\leq7/8\),

\[
 z\geq\pi+\frac12>\frac{193}{53},\qquad x=z^2>13,
\]

and \(K\leq k_{10}\) means \(K^2\leq x+110\).

- For \(n\geq4\), the moving bound leaves
  \(q_{\ell,n}^2-K^2\geq15x+d_\ell-110>85\).
- For \(n=3\) and \(\ell\geq2\), it leaves
  \(q_{\ell,3}^2-K^2\geq8x-104>0\).  Hence only third channels
  zero and one remain possible.
- For \((\ell,n)=(6,2)\), if \(x\leq68/3\), the ball wall gives
  \(q_{6,2}^2>13609/100>398/3\geq x+110\), with reserve
  \(1027/300\).  If \(x>68/3\), the moving wall gives
  \(q_{6,2}^2-K^2\geq3x-68>0\).  Angular ordering excludes every
  second channel \(\ell\geq6\).
- Every first channel \(\ell\geq10\) is absent because
  \(d_\ell\geq110\).  At \(\ell=10,K=k_{10}\), equality in the
  moving lower bound is still uncounted by the strict spectral count.

Thus the only possible entries are exactly

\[
 (\ell,1),\ 0\leq\ell\leq9;qquad
 (\ell,2),\ 0\leq\ell\leq5;qquad
 (\ell,3),\ \ell=0,1.
\]

No fourth or higher mode, omitted second or third channel, or angular
multiplicity remains outside this list.

## 4. Ratio restrictions, coexistence, and caps

A counted \((h,2)\) forces \(3x<110-d_h\).  Any counted third mode
forces the exact \((0,3)\) mode to be counted, hence \(x<55/4\).
Using only \(\pi>333/106\), I recomputed all four ratio reserves:

\[
\begin{array}{c|c|c}
\text{condition}&r&z(r)^2-\text{forced bound}\\ \hline
h=5&2/5&25195/33708\\
h=4&3/7&40281/179776\\
\text{any second}&1/2&23677/8427\\
\text{any third}&4/25&65185/275282
\end{array}
\]

Every reserve is positive, so a counted mode forces the strict relation
\(\rho<r\); the ratio face itself contains no such mode.

The three first-mode incompatibilities also recompute exactly:

\[
 H=9\Rightarrow x>\frac{1346}{25}>\frac{110}{3},
\]

so no second or third mode can coexist;

\[
 H=8\Rightarrow x>\frac{1081}{36}>30,
\]

so \(h\leq3\) and no third mode can coexist; and

\[
 H=7\Rightarrow x>\frac{89}{4}>\frac{55}{4},
\]

so no third mode can coexist.

With \(\sum_{\ell=0}^H(2\ell+1)=(H+1)^2\), second modes contributing
at most \((h+1)^2\), and the two possible third modes contributing at
most \(1+3=4\), the cap table independently reconstructs as

\[
\begin{array}{c|c|c}
H\text{ category}&\text{radial category}&\text{cap}\\ \hline
9&\text{none}&100\\
8&\text{none}&81\\
8&h\leq3&97\\
7&\text{none}&64\\
7&h\leq3&80\\
7&h=4&89\\
7&h=5&100\\
H\leq6&h\leq4,\ \text{no third}&74\\
H\leq6&h\leq3,\ \text{third}&69\\
H\leq6&h=4,\ \text{third}&78\\
H\leq6&h=5,\ \text{no third}&85\\
H\leq6&h=5,\ \text{third}&89
\end{array}
\]

The categories are exhaustive.  In particular, the last cap is
\(49+36+4=89\); no radial contribution or full angular multiplicity is
missing.

## 5. Exact Weyl payments

At fixed \(c>0\), \(\mathcal W(\rho,c)\) decreases strictly in
\(\rho\), and \(2/(9\pi)>7/99\).  For
\(F_9(\rho)=\mathcal W(\rho,k_9(\rho))\), differentiation leaves the
sign

\[
 \pi^2(1+\rho)-90\rho^2(1-\rho)^2
 >9-\frac{90}{16}=\frac{27}{8}>0.
\]

Thus \(F_9\) is strictly increasing.  The inequalities
\(\rho_c<11/80\) and \(z_{\rho_c}>193/53\) give the exact squared
baseline reserve

\[
 \left[\frac7{99}
 \left(1-\left(\frac{11}{80}\right)^3\right)\right]^2
 \left(90+\left(\frac{193}{53}\right)^2\right)^3-74^2
 =\frac{376406437293962706531}
 {5810254283800576000000}>0.
\]

Since the new band has \(K>k_9\), this pays every cap at most 74
strictly.

For the remaining fixed-wall rows, every displayed payment and reserve
recomputes exactly:

\[
\begin{array}{c|c|c}
\text{cap}&\frac7{99}(1-r^3)c^3&\text{reserve over cap}\\ \hline
97&17537639/171072&943655/171072\\
80&596183/6336&89303/6336\\
89&961193/9702&97715/9702\\
100&1107197/11000&7197/11000\\
78&1801858331/21484375&126077081/21484375\\
85&11011/125&386/125\\
89&1464463/15625&73838/15625
\end{array}
\]

The relevant counted first or second mode gives \(K>c\), while the
ratio localization gives \(\rho<r\).  Hence every use of this table is
strict in the required direction.

The two no-radial bridges also close.  At \(r=16/25,c=64/5\),

\[
 \frac7{99}(1-r^3)c^3-100
 =\frac{202207748}{21484375}>0,
\]

and the lower-\(\pi\) enclosure gives

\[
 k_9(r)^2-c^2>\frac{648969}{280900}>0.
\]

At \(r=3/5,c=71/6\), the corresponding reserves are

\[
 \frac{14506973}{1336500}>0,
 \qquad
 k_9(r)^2-c^2>\frac{4713989}{404496}>0.
\]

Below each split, the strict fixed zero wall pays the cap.  Above each
split, increasing \(F_9\) pays it.  Both estimates own the split face,
so neither cap 100 nor cap 81 leaves a boundary gap.

## 6. Upper containment and strict-face audit

For \(\rho\leq7/8\), \(z<176/7\), and therefore

\[
 28^2-k_{10}^2
 >28^2-\left(\frac{176}{7}\right)^2-110
 =\frac{2050}{49}>0.
\]

Thus \(k_{10}<28\).  The inherited central upper floor is greater than
64 before \(5/6\), while the seam floor is
\(54/(1-\rho)^2\geq1944\).  Hence \(k_{10}<U\) throughout the open
residual ratio range.

The face \(K=k_9\) belongs to the predecessor and is excluded from the
new band; all new moving payments use \(K>k_9\).  The face
\(K=k_{10}\) is included, but the \((10,1)\) moving lower wall is
uncounted there.  At \(x=68/3\), the strict ball wall owns the
\((6,2)\) exclusion.  All ratio faces are empty for the mode that
created their cutoff.  Both bridge faces have two valid owners.
The proof of the closed theorem remains valid at \(\rho=\rho_c\) and
\(\rho=7/8\); only the prospective residual subtraction excludes the
already-covered right endpoint.  The seam at \(5/6\) changes only the
identity of the inherited upper-floor owner.

## 7. Verdict

**PASS.**  The first unsupported implication does not exist.  The
internal proofs establish exactly

\[
 j_{7/2,2}>\frac{103}{10},\qquad
 j_{15/2,1}>\frac{23}{2},
\]

with the stated same-index angular propagation.  The only new external
specialization is the first-zero statement
\(j_{19/2,1}>64/5\), used at that exact order and radial index.  The
mode inventory, simultaneous restrictions, caps, payments, upper
containment, and every strict endpoint support the exploratory extension

\[
 \rho_c\leq\rho\leq\frac78,
 \qquad z_\rho\leq K\leq k_{10}(\rho).
\]

This is still an exploratory result and does not by itself freeze or
promote a Round 20 claim.
