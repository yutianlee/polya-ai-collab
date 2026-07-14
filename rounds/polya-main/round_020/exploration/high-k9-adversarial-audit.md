# Round 20 adversarial audit: repaired high-ratio extension through \(k_9\)

Date: 2026-07-15.

## Verdict

**PASS. First unsupported implication: none.**

I audited the following stable target bytes twice before beginning:

| artifact | audited SHA-256 |
|---|---|
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` |

The declared dependency hashes also reproduce exactly. I treated the
prospective \(k_9\) band as false and reconstructed the proof from those
declared inputs rather than trusting the incumbent derivation.

## 1. Independent reconstruction of \(j_{7/2,2}>10\)

For

\[
 R=\sin x-x\cos x,
 \quad Q=(3-x^2)\sin x-3x\cos x,
 \quad P=(15-6x^2)\sin x+(x^3-15x)\cos x,
\]

direct differentiation gives

\[
 R'=x\sin x,
 \qquad Q'=xR,
 \qquad P'=xQ.
\]

The resulting tangent-cell enumeration is complete:

- on \((0,\pi)\), \(R>0\); on \((\pi,2\pi)\), \(R\) decreases
  through one zero, so \(Q\) increases and then decreases through one
  zero, while \(P(2\pi)=2\pi(4\pi^2-15)>0\). Hence \(P>0\) through
  \(2\pi\);
- on \((2\pi,5\pi/2)\), \(R\) crosses once from negative to positive,
  both endpoint values of \(Q\) are negative, and therefore \(P\) is
  strictly decreasing from positive to negative. This gives exactly the
  first positive root;
- on \([5\pi/2,3\pi]\), the two terms defining \(P\) are both negative,
  so there is no omitted root;
- on \((3\pi,7\pi/2)\), \(R\) crosses once from positive to negative,
  both endpoint values of \(Q\) are positive, and therefore \(P\) is
  strictly increasing from negative to positive. This gives exactly the
  second positive root.

Writing \(y=10-3\pi\), the inherited rational enclosure for \(\pi\)
gives \(0<y<61/106<3/5\). Thus

\[
 \tan y<\frac{30}{41}<\frac{170}{117},
 \qquad
 P(10)=\cos y\,(585\tan y-850)<0.
\]

Because \(10\) is in the strictly increasing second-root cell, the
second root is strictly larger than \(10\). The positive DLMF prefactor
then transfers this to \(j_{7/2,2}>10\).

For \(p\geq3\), fixed-angular min--max comparison on the unit ball gives

\[
 j_{p+1/2,2}^2
 \geq j_{7/2,2}^2+p(p+1)-12
 >88+p(p+1).
\]

Zero extension from the shell supplies the same strict lower squares for
\(q_{p,2}\). No zero table, decimal root approximation, or unlabelled
external zero fact is used.

## 2. Complete inventory through \(k_9\)

Put \(x=z^2\). On the high-ratio interval, \(x>49/4\), while
\(K\leq k_9\) gives \(K^2\leq x+90\).

- If \(n\geq3\), then
  \(q_{\ell,n}^2-K^2\geq8x+d_\ell-90>8\), so no third or higher radial
  mode occurs.
- If \(n=1\) and \(\ell\geq9\), then
  \(q_{\ell,1}^2\geq x+d_\ell\geq x+90\). Equality at
  \((\ell,K)=(9,k_9)\) remains excluded by the strict spectral count.
- If \(n=2\) and \(\ell\geq5\), combine
  \(q_{\ell,2}^2\geq4x+d_\ell\) with
  \(q_{\ell,2}^2>88+d_\ell\). For \(x\leq d_\ell-2\), the latter is
  strictly above \(x+90\). For \(x>d_\ell-2\), the former exceeds
  \(x+90\) by more than \(4d_\ell-96\geq24\). The crossing face is
  also strictly excluded.

Thus the exact possible inventory is

\[
 (\ell,1),\ 0\leq\ell\leq8;
 \qquad
 (\ell,2),\ 0\leq\ell\leq4.
\]

There is no missing radial or angular channel.

## 3. Ratio faces, simultaneous restrictions, and caps

If \((h,2)\) is counted, then

\[
 3x<90-d_h.
\]

Substitution of the lower rational enclosure \(\pi>333/106\) at the
five proposed ratio faces reproduces the positive reserves

\[
 \frac{40281}{179776},\quad
 \frac{480395}{539328},\quad
 \frac{138056}{137641},\quad
 \frac{15889}{11236},\quad
 \frac{36230}{1424163}
\]

for \(h=0,1,2,3,4\), respectively. Hence the strict cutoffs
\(3/7,3/7,5/12,2/5,7/20\) are correct and their equality faces contain
no defining second mode.

If \((8,1)\) is counted, then

\[
 x>\left(\frac{71}{6}\right)^2-90=\frac{1801}{36}>30,
\]

which excludes every second mode. If \((7,1)\) is counted, then
\(x>666/25\), excluding \(h=3,4\). These are exactly the two claimed
simultaneous-mode restrictions.

The cap table then follows from
\(\sum_{\ell=0}^{H}(2\ell+1)=(H+1)^2\) and the analogous second-radial
sum. I recomputed every entry. The largest caps by second-mode category
are

\[
 h=4:74,\qquad h=3:65,\qquad h=2:73,
 \qquad h=1:68,\qquad h=0:65,
\]

with cap \(81\) in the sole \(H=8\), no-second cell. All multiplicities
are complete.

## 4. Independent payment and wall-order check

The fixed-wall monotonicity, the lower coefficient
\(2/(9\pi)>7/99\), and the positivity of

\[
 \pi^2(1+\rho)-72\rho^2(1-\rho)^2
 >9-\frac{72}{16}>0
\]

are correct. Thus the fixed/moving split for cap \(81\) is valid.
Independent rational arithmetic reproduces

\[
 \mathcal W\left(\frac23,\frac{71}{6}\right)
 >81+\frac{835355}{577368},
 \qquad
 k_8(2/3)^2-\left(\frac{71}{6}\right)^2
 >\frac{525692}{25281}.
\]

The predecessor's no-second payments for \(H\leq7\) have the required
strict bridges and apply a fortiori because the new band has
\(K>k_8>k_7\).

For cells with a second mode, I recomputed all eleven prospective
payment fractions and every integer decomposition. They agree exactly
with equations (26)--(29). In particular, the smallest reserve is
indeed

\[
 \frac{388127}{9702}-40=\frac{47}{9702}>0.
\]

The \(h=0,H\leq4\) cell is also strict because
\(q_{0,2}=2z\), the corresponding moving payment is increasing, and

\[
 G_0(\rho_c)=\frac{16\pi^2+24\pi+12}{9}
 >\frac{153196}{5625}>26.
\]

Consequently every possible cell is paid on both sides of each fixed,
moving, ratio, and payment-split wall. Equality in a spectral lower wall
always removes rather than adds the relevant mode under the strict
count. The proof itself also extends to \(\rho=7/8\), so the inherited
endpoint-owner wording creates no dependency gap.

## 5. Upper containment

For \(\rho\leq7/8\), \(z<176/7\), and direct subtraction gives

\[
 27^2-k_9^2>\frac{335}{49}>0.
\]

Thus \(k_9<27\), which is strictly below both the inherited central
floor \(K_0>64\) and the seam floor
\(54/(1-\rho)^2\geq1944\). Hence \(k_9<U\) on the entire stated
interval, including the seam ownership change.

## 6. Claimed \(k_{10}\) method obstruction

At \(\rho_0=13/40\), exact enclosure gives

\[
 21+\frac{16699}{25281}<x_0
 <22-\frac{11462}{35721}.
\]

For the full Lorch wall

\[
 C_7^2=\frac{153\sqrt{13}-85}{4},
\]

the exact bounds in the note imply

\[
 k_9(\rho_0)^2<112<C_7^2
 <\frac{46733}{400}<117<131<k_{10}(\rho_0)^2.
\]

Before \(C_7\), the conservative inventory is exactly the cap \(74\):
first modes through \(\ell=6\) and second modes through \(\ell=4\).
The \(\ell=7\) first mode is excluded by the strict full Lorch wall,
the \(\ell=8\) first mode by \(71/6>C_7\), and all higher first modes
by angular propagation from that \(\ell=8\) bound. Second modes
\(\ell\geq5\) and all third modes are also excluded. The pre-wall
payment recomputes exactly as

\[
 \mathcal W(\rho_0,K)
 >74+\frac{28399009}{5632000}.
\]

Immediately after the information supplied by the \(C_7\) lower wall
is exhausted, the present individual-bound method must allow the full
\(\ell=7\) multiplicity \(15\), raising the safe cap to \(89\). Yet

\[
 \mathcal W(\rho_0,C_7)
 <87-\frac{420871220401}{592000000000}<87<89.
\]

Continuity therefore leaves a right neighborhood in which this cap is
unpaid. This is correctly described as a method obstruction rather than
a shell counterexample. No earlier wall at this witness was skipped.

## 7. Provenance and byte audit

All five inherited dependency hashes in the target ledger match their
current bytes. The new source card uses only the two explicitly labelled
DLMF half-integer identities, the inherited rational enclosure for
\(\pi\), and internal calculus/min--max arguments. The Lorch input used
for the obstruction is exactly the full square authorized by the
declared Round 20 source card. No source is credited with a shell zero,
coupled exclusion, cap, or Weyl payment that it does not supply.

Both target files decode as UTF-8 and contain no NUL, replacement
character, byte-order mark, tab, trailing whitespace, or control byte
other than line endings. Their display-math delimiters are balanced.

**Final verdict: PASS. First unsupported implication: none.**
