# Clean-room adversarial audit: Ledger Packet C

**Final status: PASS on the corrected source.**

Audit date: 2026-07-16  
Audited source: manuscript/analytic/ledger-packet-C.tex  
Corrected source SHA-256: 131A0F84C5CD38881487DC6AA410401B068E824EE855652281A1A61756BFC776  
Compiled PDF SHA-256: 3D3C66C5E7301AF38D254474FE20E5648705B922727D154F30D8A07AAE870E3A

Reference sources frozen for this audit:

- main paper, manuscript/spherical-shell-polya-proof.tex: 65B7D3AE377D6EE44CFCD5D2B93F102241C93F83E1F8DABA6DF8911B945860C3;
- Supplement S1, manuscript/spherical-shell-polya-supplement.tex: F6AB06BA835A8799082AE4832CD0B75B7AFE8FA810412FE5AA2170B03D197E4F;
- exact checker, computations/certification/verify_analytic_ledgers.py: 41691116E0E3E5453B9B209ACB93FF784724C3A95B83C94BBDF7F6760616E716.

The Python listing embedded in Supplement S1 was extracted directly and
compared with the checker. It is an exact text match. Thus the row order
used below is the order in both the supplement and the standalone checker.

## Audit protocol and corrections

This was a clean-room audit: the displayed fractions were recomputed with
independent exact Fraction arithmetic from the definitions, rather than by
importing or calling the project checker. The project checker was replayed
only afterward as a separate consistency test. The audit arithmetic is
evidence about the typesetting; it is not a premise of the analytic proof.

The initially frozen Packet C source had SHA-256
A631D65EB8806BCC31449506F18DC4A6E011C0C4D8EBD315E04D51DA3BA7A39E.
Two defects were reported before any edit and then corrected with the lead
agent's authorization:

1. The cap-74 paragraph said that the proxy constant satisfied
   \(\beta_{4,2}^2>11409/100\). By definition
   \(\beta_{4,2}=\sqrt{11409}/10\), so its square equals \(11409/100\).
   The strict propagated inequality is instead
   \(j_{9/2,2}^2>11409/100\). The corrected text now distinguishes the
   actual Bessel zero from its strict proxy.
2. Packet C initially claimed rows C44--C56 although Packet A already owns
   C56, the bookkeeping identity \(49+25=74\). The corrected allocation is
   C44--C55, C57--C59, and C78--C98. This changes Packet C's C-family count
   from 37 to 36 and its total from 84 to 83, with no mathematical witness
   removed.

No numerical value in any localization, split, impossible-cell, or payment
table required correction.

## 1. Localization registry

The seventeen ratios are strictly ordered. Their sixteen independently
recomputed consecutive gaps are

\[
\frac1{25},\frac1{20},\frac1{20},\frac1{30},\frac1{60},
\frac1{40},\frac1{40},\frac1{60},\frac1{84},\frac1{14},
\frac1{30},\frac1{600},\frac{13}{200},\frac1{25},
\frac1{100},\frac1{60}.
\]

Also \(\rho_c<1/7<4/25\) and \(2/3<7/8\), so every ratio lies in the
declared high strip.

For a positive row I recomputed

\[
A-(n^2-1)\left(\frac{22/7}{1-r}\right)^2,
\qquad A=m(m+1)-\ell(\ell+1),
\]

and for a negative row I recomputed

\[
(n^2-1)\left(\frac{333/106}{1-r}\right)^2-A.
\]

In registry order the seventeen results are exactly

\[
\frac{320}{49},\frac{58215}{137641},\frac{27699}{44944},
\frac{2622}{1225},\frac{248}{147},\frac{2200}{2401},
\frac{120843}{179776},\frac{23677}{2809},
\frac{13302732}{2699449},\frac{2175627}{550564},
\frac{5080707}{44944},\frac{1555635}{11236},
\frac{18126190}{137641},\frac{1510851}{11236},
\frac{260740}{137641},\frac{23484}{2809},
\frac{36230}{474721}.
\]

Every fraction is positive. Since \(x_\rho\) is strictly increasing and
\(\Delta_{m;n,\ell}\) is strictly decreasing, the packet's side
implications have the correct direction: a positive witness controls the
lower side and a negative witness controls the upper side.

## 2. Algebraic splits and the five \(k_{11}\) implications

The strip chain is valid:

\[
(\pi+\tfrac12)^2<(51/14)^2=2601/196
<16<68/3<34<576<64\pi^2.
\]

Strict increase of \(x_\rho\) therefore gives one and only one point for
each split. Direct substitution gives

- \(\Delta_{11;3,1}(16)=2>0\);
- \(\Delta_{10;2,6}(68/3)=0\);
- \(\Delta_{11;2,5}(34)=0\).

The latter two equality modes are correctly excluded by the strict channel
convention. The five special implications also recompute exactly:

\[
x_{8/15}-44>\frac{725209}{550564},\qquad
x_{1/4}-\frac{33}{2}>\frac{5871}{5618},
\]

\[
(69/5)^2-132=\frac{1461}{25}
=44+\frac{361}{25}
=\frac{33}{2}+\frac{2097}{50},
\]

\[
(64/5)^2-132=\frac{796}{25}
=\frac{33}{2}+\frac{767}{50}.
\]

All inequality directions and strict-boundary conclusions agree with the
main paper and checker.

## 3. Impossible cells

For each dashed cap cell, the required lower bound exceeds the required
upper bound:

| Cell | Lower | Upper | Exact gap |
|---|---:|---:|---:|
| \(k_8,\ H=6,\ h\ge2\) | \(28\) | \(22\) | \(6\) |
| \(k_9,\ H=8\), any second mode | \(1801/36\) | \(30\) | \(721/36\) |
| \(k_9,\ H=7,\ h\ge3\) | \(169/4\) | \(26\) | \(65/4\) |

Both necessary modal inequalities are strict, so equality cannot restore
any of these cells.

## 4. Monotonicity and the five global payments

Logarithmic differentiation gives the sign asserted in the packet:

\[
\pi^2(1+\rho)-M\rho^2(1-\rho)^2.
\]

For \(m\le11\), \(M\le132\) and
\(\rho^2(1-\rho)^2\le1/16\), hence the expression is strictly greater
than \(9-132/16=3/4\). Thus every checkpoint payment
\(\mathcal W_m\) used here is strictly increasing.

The coarse lower bound
\(\mathcal W(\rho_c,K)>(38/539)K^3\) follows with the directions printed
in the packet from \(z_{\rho_c}>193/53\), \(\rho_c<1/7\), and
\(1/\pi>7/22\). The independently recomputed square gaps and payment
reserves are:

| \(m\) | cap | square gap | payment reserve |
|---:|---:|---:|---:|
| 7 | 40 | \(67049/1755625\) | \(5083656/8421875\) |
| 8 | 53 | \(1901439/28090000\) | \(656778873/269500000\) |
| 9 | 73 | \(61431/1755625\) | \(7911557/8421875\) |
| 10 | 89 | \(14211/280900\) | \(1999489/269500\) |
| 11 | 121 | \(65271/1123600\) | \(5076899/2156000\) |

All ten quantities are strictly positive.

## 5. Seven conditional payments

The common argument is valid. Counting the stated first mode gives
\(k_m(\rho)>t\), hence \(x_\rho>a^2=t^2-m(m+1)\) and
\(\rho>\rho_0=1-\pi/a\). The smallest radicand is \(89/4\), and

\[
\frac{89}{4}-\left(\frac{22}{7}\right)^2
=\frac{2425}{196}>0,
\]

so \(a>\pi\) in all seven rows. Since \(\mathcal W_m\) increases with
\(\rho\), while \(\mathcal W(\rho,t)\) decreases with \(\rho\) at fixed
\(t\), a rational \(r>\rho_0\) gives the displayed lower payment. The
condition \(r>\rho_0\) is equivalent to the correctly directed
positive-square witness

\[
L=(333/106)^2-(1-r)^2a^2>0.
\]

The seven exact \((L,P)\) pairs recompute as

| Branch | \(L\) | \(P\) |
|---|---:|---:|
| \(k_7,H=6\) | \(725209/2528100\) | \(18659/2673\) |
| \(k_8,H=7\) | \(64349/280900\) | \(213281/49500\) |
| \(k_9,H=8\) | \(4713989/2528100\) | \(14506973/1336500\) |
| \(k_{10},H=7\) | \(2105431/4494400\) | \(18539033/6336000\) |
| \(k_{10},H=8\) | \(317585/4955076\) | \(2865431/261954\) |
| \(k_{10},H=9\) | \(8811001/7022500\) | \(25143284/1546875\) |
| \(k_{11},H=9\) | \(536261/280900\) | \(58757/12375\) |

Every localization and reserve is strictly positive.

## 6. Corrected cap-74 path

The propagated actual-zero inequality is

\[
j_{9/2,2}^2>(103/10)^2+20-12
=11409/100=108+609/100.
\]

The proxy square itself is exactly \(\beta_{4,2}^2=11409/100\).
At \(k_9\), the product wall gives \(x<70/3\), whereas the zero wall gives
\(x>2409/100\). Their incompatibility gap is

\[
\frac{2409}{100}-\frac{70}{3}=\frac{227}{300}>0.
\]

The conservative fallback is also correct:

\[
x_{7/20}-\frac{70}{3}>
\frac{36230}{1424163}>0,\qquad
108-(207/20)^2=\frac{351}{400}>0,
\]

\[
\frac7{99}\left(1-(7/20)^3\right)(207/20)^3
=\frac{52823261673}{704000000}
=74+\frac{727261673}{704000000}>74.
\]

The block identity \(49+25=74\) is correct, but its executable row C56 is
owned by Packet A and is not double-counted in Packet C.

## 7. Cap-table sufficiency

The packet's global, conditional, impossible-cell, and cap-74 witnesses
cover every cap alternative used by the main paper:

- \(k_7\): cap at most 40 globally, or the \(H=6\) cap 53 conditionally;
- \(k_8\): cap at most 53 globally after the impossible cell, or cap 80
  conditionally when \(H=7\);
- \(k_9\): cap at most 73 globally, cap 81 conditionally when \(H=8\),
  with the \(H=7,h\ge3\) cell impossible and cap 74 handled separately;
- \(k_{10}\): cap 89 globally; the \(H=7,8,9\) branches are paid
  conditionally by caps 100, 97, and 100, respectively, with the required
  higher-radial exclusions following from the printed zero/product cuts;
- \(k_{11}\): cap 121 globally; \(H=9\) has cap 125 conditionally, while
  the \(H=10\) and higher-radial exclusions follow from the five printed
  \(k_{11}\) implications.

No cap comparison is used in the reverse direction, and no realizable cell
is left without a payment.

## 8. Row numbering and scope

Direct instrumentation of the two checker functions gives:

- L1--L2: ratio metadata;
- L3--L19: high-strip membership;
- L20--L36: the seventeen localization signs;
- L37--L42: three split locations and three side/equality predicates;
- L43--L47: the five \(k_{11}\) implications;
- C44--C55: twelve non-bookkeeping cap-74 predicates;
- C57--C59: three impossible cells;
- C78--C79: checkpoint monotonicity;
- C80--C84: five global payments;
- C85--C98: seven localization and seven conditional-payment predicates.

Therefore Packet C owns all 47 L-family rows and exactly 36 C-family rows,
for 83 rows total. Packet A/B owns the disjoint C-family complement
C1--C43, C56, and C60--C77, totaling 62 rows. The two sets are disjoint
and their union is C1--C98.

The five headline subfamilies contain 35 connected mathematical objects
and replace 45 predicates. The other 38 Packet C predicates are the
explicitly mapped auxiliary closure rows. These counts reconcile exactly.

## 9. Replay and compilation

The independent exact audit finished with:

    PASS: independent exact Packet-C audit
    localization signs: 17 ratios: 17 global: 5 conditional: 7
    Packet C registry rows: 83 = L47 + C36; complement C62; overlap 0

The canonical checker independently reported:

    PASS
    first issue: none
    core exact finite checks: 553
    core substantive checks: 488
    core bookkeeping identities: 65
    supplemental exact checks: 58
    combined registry rows: 611
    canonical registry sha256: afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1
    cap-74 incompatibility gap: 227/300

The corrected source was compiled with the bundled Tectonic 0.16.9 LaTeX
workflow. Tectonic reran automatically for references and long-table
widths, then completed with exit code 0. The final PDF has seven pages and
69,307 bytes. The second TeX pass contains no unresolved-reference or
long-table warning.

## Conclusion

**PASS.** After the two reported corrections, every localization sign,
split, impossible-cell gap, monotonicity argument, global payment,
conditional localization/payment, and cap-74 implication in Packet C
recomputes exactly and has the correct strictness and direction. The
83-row claim is complete, disjoint from Packet A/B, consistent with the
main paper and Supplement S1, and successfully compiled.
