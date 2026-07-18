# Clean-room adversarial audit: Ledger Packet D

**Final status: PASS on the corrected source.**

Audit date: 2026-07-16  
Audited source: manuscript/analytic/ledger-packet-D.tex  
Corrected source SHA-256: 17A08B124A6AE81B516E235046DB3ACCD4E7EDDC1C2A7CF6828FF87D6F3B7EBC  
Compiled PDF SHA-256: 608379934CD5910D7C6B12F33105B5DCCF54EC8850708012ED22D4972D2F6A44

Reference sources frozen for this audit:

- main paper, manuscript/spherical-shell-polya-proof.tex: 65B7D3AE377D6EE44CFCD5D2B93F102241C93F83E1F8DABA6DF8911B945860C3;
- Supplement S1, manuscript/spherical-shell-polya-supplement.tex: F6AB06BA835A8799082AE4832CD0B75B7AFE8FA810412FE5AA2170B03D197E4F;
- exact checker, computations/certification/verify_analytic_ledgers.py: 41691116E0E3E5453B9B209ACB93FF784724C3A95B83C94BBDF7F6760616E716.

The complete Python listing embedded in Supplement S1 was extracted and
compared with the standalone checker. It is an exact text match.

## Audit protocol and source correction

Every fraction below was recomputed independently with exact rational
arithmetic from the definitions. The project checker was not imported for
that arithmetic pass. It was replayed afterward only as a separate
consistency test and to instrument its ordered labels.

The initially frozen Packet D source had SHA-256
4F945B6FD3B29069B0E5A3E8E825B84A7CC960FB1B7413D6B6D0AF14653340C4.
The audit found one source-level strictness error and reported it before
editing:

\[
S<S_*=(13P-8r)/5
\]

does not hold when \(m=0\) and \(p=R>0\), because then
\(S=P=S_*\). From \(R=p-dm\) and \(d>5/8\), the universally valid
conclusion is \(S\le S_*\), with strictness when \(m>0\). The lead agent
authorized this correction. It is harmless to the proof: \(S\le S_*\)
gives \(Q\le Q_*\) and \(\widehat q\le q_*\), while the preceding
self-consistent inequality is already strict, so it still yields
\(P^2<H(P,r)\). Every later use requires only the non-strict comparison.

No printed rational witness or payment value required correction.

## 1. Rational constants

The alternating Machin truncations have the directions used in Packet D.
Independent subtraction gives

\[
L_\pi-\frac{333}{106}
=\frac{3418213}{41563593750}>0,
\]

\[
\frac{1571}{500}-U_\pi
=\frac{323354809}{853244937500}>0,
\qquad
\frac{22}{7}-\frac{1571}{500}=\frac3{3500}>0.
\]

Thus

\[
\frac{333}{106}<\pi<\frac{1571}{500}<\frac{22}{7}
\]

is a purely analytic enclosure with exact rational remainder control.

## 2. The twenty-two seam rows

All twenty-two displayed values recompute exactly:

| Row | Recomputed exact value | Audit |
|---:|---:|:---:|
| 1 | \(323354809/853244937500\) | \(>0\) |
| 2 | \(2/9801\) | \(>0\) |
| 3 | \(1/4900\) | \(>0\) |
| 4 | \(1/14400\) | \(>0\) |
| 5 | \(119/250\) | \(>0\) |
| 6 | \(1/1620\) | exact |
| 7 | \(8563/675000000\) | \(>0\) |
| 8 | \(804689/2025000\) | exact |
| 9 | \(497/4050000\) | \(>0\) |
| 10 | \(241/480=1/2+1/480\) | exact |
| 11 | \(637/32400\) | exact |
| 12 | \(2260740364246/708624500625\) | exact |
| 13 | \(6858037754/708624500625\) | \(>0\) |
| 14 | \(92/15\) | \(>0\) |
| 15 | \(10093/9720\), with excess \(373/9720\) | exact |
| 16 | \(373/48600\) | exact |
| 17 | \(2505132463469/2616573970125\) | \(>0\) |
| 18 | \(280000/17281\) | exact |
| 19 | \(598066/51843\) | exact |
| 20 | \(132/175\) | exact |
| 21 | \(80132733/3024175\) | \(>0\) |
| 22 | \(114694733/3024175\) | \(>0\) |

### Displacement chain

The shelf inequality gives

\[
\left(\frac{y^3P}{\kappa\rho}\right)^2
<\frac{2\pi y^2}{\kappa\rho}
\le\frac{\pi}{135}<\frac{1571/500}{135}.
\]

Together with \(S_*\le13P/5\), this proves the row 6--9 displacement
bound. The corrected \(S\le S_*\) is sufficient. Since
\(\rho\ge5/6\), the consequence

\[
\frac{x_0}{K}>\rho(1-\widehat q)
>\frac56\left(1-\frac{159}{400}\right)
=\frac{241}{480}>\frac12
\]

has the correct direction and strictness.

### Derivative proxy and scope

At fixed \(r=B=14/3\),

\[
\partial_PQ_*=\frac{13y}{5\kappa}
<\frac{13}{5}\frac{49/120}{54}
=\frac{637}{32400}.
\]

For \(a=y^2/\rho\), \(q_*=a(Q_*-1)\), differentiation gives

\[
\partial_PH
=2\pi^2(\partial_PQ_*)
\frac{1+q_*+2a}{(1-q_*)^3}.
\]

Every substitution used to reach row 12 is monotone on
\(q_*<159/400<1\), \(a\le1/5\). Row 13 gives
\(\partial_PH<16/5\). Since \(P\ge14/3\), row 14 gives

\[
\frac{d}{dP}(P^2-H(P,B))>\frac{92}{15}>0.
\]

Rows 15--17 establish a strictly positive reserve at \(P=B\). Integration
therefore excludes \(r\ge B\) and gives \(R<14/(3y)\). The argument
remains valid in the equality case \(S=S_*\), because the original
\(P^2\)-inequality is strict.

### Terminal action payment

The turning-point bound yields

\[
K\eta>\frac{280000}{17281}\frac1y.
\]

Combining \(R<14/(3y)\), \(1/y>120/49\),
\(4\delta<132/175\), and the universally strict floor inequality
\(\lfloor x\rfloor>x-1\) gives row 21 for \(R>0\). Dropping
\(-R\ge0\) gives row 22 for \(R\le0\). Thus \(R=0\) and integral
\(K\eta\) faces are covered.

## 3. The two documented source-label corrections

Both remarks in Packet D are accurate.

1. Supplemental seam row 11 is labeled “exact \(dq/dP\) cap,” but its
   checker variable equals
   \((13/5)(49/120)/54=637/32400\), the proxy for
   \(\partial_PQ_*\). The true relation is
   \(\partial_Pq_*=a\partial_PQ_*\), hence the smaller cap
   \(637/162000\). The checker inserts \(637/32400\) into the derivative
   of \(H\) in the correct \(Q_*\)-derivative role. This is a label error,
   not a mathematical error.
2. The main seam paragraph says that
   \(\pi<1571/500\), the two \(\sqrt2\) bounds, and the \(y\)-bound are
   each proved by positive rational squaring. Squaring proves the radical
   bounds, but not the \(\pi\)-bound. Packet D correctly supplies the
   alternating Machin-series proof and exact positive gap.

## 4. The eleven \(k_6\) payments

For \(T^2=az_\rho^2+b\), direct differentiation gives the sign

\[
a\pi^2(1+\rho)-b\rho^2(1-\rho)^2.
\]

After division by \(a>0\), the left side is \(>9\), while the right side
is at most \(42/16\). All moving payments are therefore strictly
increasing. Fixed-wall payments are decreasing in \(\rho\).

For each moving row I independently formed

\[
A=a\frac{(333/106)^2}{(1-r)^2}+b,\quad
B=\frac7{99}(1-r^3),\quad
\Delta=B^2A^3-C^2.
\]

The six reduced differences are:

| Wall | \(r\) | cap | \(\Delta\) |
|---|---:|---:|---:|
| \(k_1\) | \(1/8\) | 4 | \(153864824754340538785/348796101192617852928\) |
| \(k_2\) | \(3/10\) | 9 | \(1399810848073457853053/394237491401523000000\) |
| \(k_3\) | \(1/2\) | 16 | \(137027505353736631/514922437748928\) |
| \(k_4\) | \(1/2\) | 25 | \(2507119282010251109/13902905819221056\) |
| \(k_5\) | \(13/25\) | 36 | \(92672404686738742434741/709259556128000000000\) |
| \(p_1\) | \(1/5\) | 29 | \(373255772037478993002833/868931613701316000000\) |

All are positive. Since \(B A^{3/2}+C>0\), squaring introduces no
spurious branch.

The five fixed-wall reserves also recompute exactly:

| Wall | \(r\) | cap | reserve |
|---|---:|---:|---:|
| \(51/10\) | \(3/10\) | 9 | \(1387329/11000000\) |
| \(13/2\) | \(1/2\) | 16 | \(6277/6336\) |
| \(15/2\) | \(1/2\) | 25 | \(775/704\) |
| \(17/2\) | \(13/25\) | 36 | \(452843/343750\) |
| \(77/10\) | \(1/5\) | 29 | \(849901/281250\) |

For every maximum entry wall, the fixed row controls \(\rho\le r\) and
the moving row controls \(\rho\ge r\). Equality of the two wall components
at \(r\) is not assumed or needed. For \(k_1\),
\(\rho_c>1/8\) follows from \(\pi<22/7<7/2\), so its moving row applies
throughout its domain.

The main paper's separate direct \(2z\) entry payment is also valid. At
\(\rho_c\),

\[
\mathcal W(\rho_c,2z)
=\frac43+\frac{8\pi}{3}+\frac{16\pi^2}{9}
>\frac{229684}{8427}
=26+\frac{10582}{8427}>26.
\]

This analytic fact is not one of the eleven supplemental payment
predicates and therefore does not alter Packet D's row count.

## 5. Lower-\(d\) ordering and caps

The ten odd-multiplicity sums are exactly

\[
(1,4,9,10,16,17,26,29,40,45).
\]

On the open lower-\(d\) ratio interval,

\[
2\frac{333}{106}\frac{19}{18}-\frac{13}{2}
=\frac7{53}>0,
\qquad
\frac{15}{2}-\left(2\frac{22}{7}+1\right)
=\frac3{14}>0.
\]

Thus \(13/2<2z_\rho<15/2\), and the cap-10 cell is empty. These two
endpoint comparisons give the three checker predicates with the correct
directions.

## 6. The nine lower-\(d\) payments

Using the fixed-wall coefficient

\[
\frac7{99}\left(1-(7/50)^3\right),
\]

the seven independently recomputed reserves are

\[
\frac{793292}{1546875},\
\frac{486236661}{1375000000},\
\frac{333100003}{99000000},\
\frac{329797}{88000},\
\frac{3590476297}{1125000000},\
\frac{327078887}{99000000},\
\frac{8805519}{1375000}.
\]

They correspond in order to walls
\(4,51/10,13/2,15/2,77/10,17/2,9\) and caps
\(4,9,16,26,29,40,45\). Every reserve is positive.

The initial moving-wall proxy is

\[
\frac{3+6(333/106)+4(333/106)^2}{18}
=\frac{57421}{16854}
=\frac{19}{6}+\frac{675}{2809}.
\]

At \(\rho=1/19\), the \(2z\) proxy is

\[
\frac{16}{9}\left(\frac{333}{106}\right)^2
\frac{1-(1/19)^3}{(1-1/19)^3}
=\frac{173863}{8427}
=\frac{508}{27}+\frac{137795}{75843}.
\]

The moving \(2z\) payment is increasing, and the relevant domain begins
above \(1/\sqrt{337}>1/19\). The initial \(L=(2\rho)^{-1}\) payment is
decreasing in \(\rho\), so its minimum is controlled at \(\rho_c\).
The nine payments therefore cover the stated lower-\(d\) cells and
endpoints.

## 7. Supplemental row allocation

Direct label instrumentation gives the exact disjoint allocation:

- supplemental rows S1--S22: verify_seam_ledger, 22 rows;
- S23--S48: verify_k6_and_lower_d_ledgers, 26 rows, decomposed as
  \(2+6+5+10+3\);
- S49--S57: verify_lower_d_payments, 9 rows;
- S58: the cap-74 incompatibility predicate, outside Packet D and assigned
  to Packet C.

Thus Packet D owns exactly

\[
22+26+9=57
\]

of the 58 supplemental predicates, with no overlap and no omitted row in
its declared scope.

## 8. Replay and compilation

The independent arithmetic pass reported:

    PASS: independent exact Packet-D arithmetic
    seam rows: 22 moving k6: 6 fixed k6: 5 lower-d payments: 9
    supplemental allocation: 22 + 26 + 9 = 57

The canonical checker independently reported:

    PASS
    first issue: none
    core exact finite checks: 553
    core substantive checks: 488
    core bookkeeping identities: 65
    supplemental exact checks: 58
    combined registry rows: 611
    canonical registry sha256: afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1
    seam partial_P H cap: 2260740364246/708624500625
    seam partial_P H margin to 16/5: 6858037754/708624500625
    seam initial reserve: 2505132463469/2616573970125
    lower-d moving 2z lower bound: 173863/8427

The corrected TeX source compiled with bundled Tectonic 0.16.9. Tectonic
reran for references and outlines, completed with exit code 0, and produced
a six-page, 80,265-byte PDF. The second pass has no unresolved-reference,
long-table, or rerun warning.

## Conclusion

**PASS.** After correcting \(S<S_*\) to \(S\le S_*\), Packet D gives a
valid analytic replacement for its 57 supplemental predicates. All
twenty-two seam rows, the derivative argument, all eleven \(k_6\)
payment differences, all lower-\(d\) ordering/cap predicates, and all
nine lower-\(d\) payments recompute exactly and have the correct
strictness and monotonicity directions. The two documented source-label
corrections are both accurate.
