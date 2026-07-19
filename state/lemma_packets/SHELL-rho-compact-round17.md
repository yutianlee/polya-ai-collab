# Lemma Packet: Exact Round 17 Compact Residual Mask

Status: **FROZEN RESIDUAL MAP / NO NEW THEOREM**.

Round: 17.

Primary obligations: **SHELL-rho-compact** and
**COMP-certified-bessel**.

Baseline commit:
047c9ef5c4fe2329d73d3568c1ac48654dd18585.

This packet freezes the exact accepted analytic mask before any Round 17
analytic proof, clean-room reconstruction, or new certification attempt.
It records set membership and already accepted implications only. It does
not prove that the residual is empty, does not promote a new endpoint, and
does not turn a finite mask check into an analytic proof.

## 1. Constants

For \(0\le s\le1\), set

$$
G_1(s)
=\frac1\pi\left(\sqrt{1-s^2}-s\arccos s\right).
$$

Define

$$
\omega_0
=G_1\!\left(\frac12\right)
=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
C_0=1+\frac{8\sqrt2}{15},
$$

and

$$
\rho_*=\frac{\omega_0}{1+2C_*}
=\frac{\omega_0}{2C_0}.
$$

For \(0<\rho<1\), let

$$
a_\rho=\frac{2\pi\rho}{1-\rho},
\qquad
\eta_\rho=G_1\!\left(\max\left\{\rho,\frac12\right\}\right),
$$

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+
\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2.
\tag{1}
$$

On the strict domain \(\rho<\omega_0\), also define

$$
H_0(\rho)=\frac{C_*}{\omega_0-\rho}.
\tag{2}
$$

The compact ratio interval is

$$
I_{16}=\left[\rho_*,\frac78\right].
\tag{3}
$$

All frequencies below are restricted to \(K\ge0\).

## 2. Primitive accepted analytic mask

Let \(\mathcal A_{16}\) be the union of the following accepted full-count
domains, intersected with \(I_{16}\times[0,\infty)\).

| id | accepted condition | face convention | source obligation |
|---|---|---|---|
| A0 | \(\rho=\rho_*\), every \(K\) | complete closed face | SHELL-rho-zero-endpoint |
| A1 | \(\rho=7/8\), every \(K\) | complete closed face | SHELL-rho-one-endpoint |
| A2 | \(2\rho K\le1\) | equality included | high-angular tails plus weighted scaffold |
| A3 | \((1-\rho)K\le\pi\) | equality included | SHELL-thin-width-phase-zero |
| A4 | \(\rho<\omega_0\) and \(K(\omega_0-\rho)\ge C_*\) | frequency equality included; \(\rho=\omega_0\) excluded | small-hole low-interface theorem plus high-angular tails |
| A5 | \(K\ge K_0(\rho)\) | equality included | SHELL-fixed-rho-high-energy |
| A6 | \(0<1-\rho\le1/6\) and \(K(1-\rho)^2\ge54\) | both equalities included | Round 15 seam |
| A7 | \(0<1-\rho\le1/8\) and \(K(1-\rho)^2\ge32\) | both equalities included | retained Round 14 seam |
| A8 | \(0<1-\rho\le1/10\) and \(K(1-\rho)^2\ge24\) | both equalities included | retained Round 13 seam |
| A9 | \(0<1-\rho\le1/25\) and \(K(1-\rho)^2\ge20\) | both equalities included | retained Round 10 seam |
| A10 | \(K\ge295^2=87025\) | equality included | promoted Round 16 global envelope |

Within \(I_{16}\), A7 meets only the endpoint face \(\rho=7/8\), so its
intersection with the strict interior is empty. A8 and A9 have empty
intersection with all of \(I_{16}\). They are retained in the provenance
predicate because their accepted statements remain true.
A10 is redundant after the primitive branches are assembled, but it is an
accepted consequence and is retained as an independent face owner.

The old product, aggregate, and bridge theorems requiring
\(1-\rho\le1/100\) do not meet \(I_{16}\); they add no mask region.

The exact Boolean predicate is therefore

~~~text
in_A16 =
    rho_* <= rho <= 7/8
    and K >= 0
    and (
        rho == rho_*
        or rho == 7/8
        or 2*rho*K <= 1
        or (1-rho)*K <= pi
        or (rho < omega_0 and K*(omega_0-rho) >= C_*)
        or K >= K_0(rho)
        or (0 < 1-rho <= 1/6  and K*(1-rho)^2 >= 54)
        or (0 < 1-rho <= 1/8  and K*(1-rho)^2 >= 32)
        or (0 < 1-rho <= 1/10 and K*(1-rho)^2 >= 24)
        or (0 < 1-rho <= 1/25 and K*(1-rho)^2 >= 20)
        or K >= 87025
    )
~~~

The executable classifier
computations/round17_residual_mask.py implements this disjunction for
rational points. Rational comparisons are exact; transcendental comparisons
use Arb precision escalation and are accepted only after a certified sign.
If a comparison material to membership cannot be separated, the program
returns **indeterminate**; in particular, an unresolved mandatory interval
gate cannot be overridden by a true coverage disjunct. A certified-true
disjunct may settle union membership without resolving irrelevant
comparisons. The classifier never guesses a side. Named irrational threshold
faces remain part of the symbolic predicate above.

## 3. Analytic residual and certified overlay

The exact analytic residual is

$$
\mathcal D_{16}
=\bigl(I_{16}\times[0,\infty)\bigr)\setminus\mathcal A_{16}.
\tag{4}
$$

The retained certified Round 8 box is

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right].
\tag{5}
$$

It is not part of the analytic mask. The certificate and independent checker
prove \(B_0\subset\mathcal D_{16}\) and discharge the theorem on that closed
box. Consequently the currently theorem-wise uncovered set is

$$
\mathcal U_{16}=\mathcal D_{16}\setminus B_0.
\tag{6}
$$

The notation must remain distinct:

- \(\mathcal A_{16}\): accepted analytic coverage;
- \(\mathcal D_{16}\): residual after analytic coverage only;
- \(B_0\): accepted certified coverage;
- \(\mathcal U_{16}\): points not yet covered analytically or by \(B_0\).

## 4. Normalized exact residual

For \(\rho_*<\rho<7/8\), define the lower covered ceiling

$$
L(\rho)=
\max\left\{
\frac1{2\rho},
\frac{\pi}{1-\rho}
\right\},
\tag{7}
$$

and the upper covered floor

$$
U(\rho)=
\min\left(
\{K_0(\rho)\}
\cup
\{H_0(\rho):\rho<\omega_0\}
\cup
\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right).
\tag{8}
$$

The complete endpoint faces remove both ratio endpoints. Every frequency
threshold in A2--A6 is included. Hence

$$
\boxed{
\mathcal D_{16}
=
\left\{
(\rho,K):
\rho_*<\rho<\frac78,\quad
L(\rho)<K<U(\rho)
\right\}.
}
\tag{9}
$$

Both frequency inequalities in (9) are strict.

At the lower endpoint,

$$
H_0(\rho_*)=\frac1{2\rho_*},
\tag{10}
$$

because
\(\omega_0-\rho_*=2C_*\rho_*\). Thus the inclusive high-angular
and small-hole rays meet exactly. The endpoint theorem independently owns
the complete vertical face.

## 5. Exact boundary switches

### 5.1 Lower boundary

The two lower walls meet at

$$
\rho_c=\frac1{1+2\pi}.
\tag{11}
$$

Therefore

$$
L(\rho)=
\begin{cases}
\dfrac1{2\rho},&\rho\le\rho_c,\\[4pt]
\dfrac{\pi}{1-\rho},&\rho\ge\rho_c.
\end{cases}
\tag{12}
$$

Equality at \(\rho_c\) is shared. The exact bounds
\(\omega_0<1/8<7/51<\rho_c\) follow from
\(\sqrt3<7/4\), \(\pi>3\), and \(\pi<22/7\).

### 5.2 The \(H_0=K_0\) switch

On \((\rho_*,\omega_0)\), \(\eta_\rho=\omega_0\). Substituting
\(K=H_0(\rho)\) into

$$
\eta_\rho K-\sqrt{a_\rho K}-C_0=0
\tag{13}
$$

and squaring with the required positive side gives

$$
P(\rho)
=(1-\rho)\left(C_0\rho-\frac{\omega_0}{2}\right)^2
-2\pi C_*\rho(\omega_0-\rho)=0.
\tag{14}
$$

The squaring is reversible for \(\rho>\rho_*\), since

$$
C_0\rho-\frac{\omega_0}{2}>0.
\tag{15}
$$

Moreover,

$$
P''(\rho)
=2C_0^2(1-3\rho)+2C_0\omega_0+4\pi C_*>0
\qquad(\rho_*<\rho<\omega_0),
\tag{16}
$$

because \(\omega_0<1/8\). The function is strictly convex,
\(P(\rho_*)<0\), and

$$
P(\omega_0)
=(1-\omega_0)\omega_0^2 C_*^2>0.
\tag{17}
$$

Its negative sublevel set is therefore an interval containing \(\rho_*\),
so (14) has exactly one root \(\rho_{HK}\) in
\((\rho_*,\omega_0)\). Certified Arb signs give

$$
\boxed{
\frac{9407}{100000}
<\rho_{HK}<
\frac{94071}{1000000}.
}
\tag{18}
$$

This bracket is a certified locator, not a rational replacement for the
implicit exact root. Both endpoints lie in the uniqueness interval: exactly,

$$
\rho_*<\frac1{16}<\frac{9407}{100000}
<\frac{94071}{1000000}<\frac1{10}<\omega_0.
\tag{19}
$$

Here \(\rho_*<1/16\) follows from \(C_0>1\) and \(\omega_0<1/8\), while
\(1/10<\omega_0\) follows from \(15\sqrt3>8\pi\), which is certified after
squaring by \(\pi<22/7\).

At \(\rho=\rho_*\), substituting \(K=H_0(\rho_*)\) into the left side of
(13) gives \(-\sqrt{a_{\rho_*}H_0(\rho_*)}<0\), so
\(H_0(\rho_*)<K_0(\rho_*)\). As \(\rho\uparrow\omega_0\), \(H_0\) diverges
while \(K_0\) remains finite. The unique equality therefore makes \(H_0\)
the active upper branch below \(\rho_{HK}\) and \(K_0\) the active branch
above it.

### 5.3 The seam switch

The function \(K_0\) is increasing:

- \(a_\rho\) is strictly increasing;
- \(\eta_\rho\) is constant through \(\rho=1/2\) and strictly decreasing
  afterwards, since \(G_1'(s)=-\arccos(s)/\pi<0\);
- the positive root of
  \(\eta y^2-\sqrt a\,y-C_0=0\) increases with \(a\) and decreases with
  \(\eta\).

The formula interface \(\rho=1/2\) is included and continuous.

At \(\rho=5/6\),

$$
\eta_{5/6}
=\frac1\pi\int_{5/6}^1\arccos t\,dt
<\frac1{20}.
\tag{20}
$$

Indeed, the alternating cosine bound at \(9/10\) gives
\(\cos(9/10)<5/6\), so
\(\arccos(5/6)<9/10\); then use \(\pi>3\).
Since the numerator in (1) is strictly larger than \(2\sqrt{a_\rho}\),

$$
K_0(5/6)>
\frac{a_{5/6}}{\eta_{5/6}^2}
>10\pi\cdot400
>12000.
\tag{21}
$$

For \(5/6\le\rho<7/8\),

$$
\frac{54}{(1-\rho)^2}\le3456<12000<K_0(\rho).
\tag{22}
$$

Thus the Round 15 seam is the actual upper branch on that interval. It
begins inclusively at

$$
\rho=\frac56,\qquad K=54\cdot6^2=1944.
\tag{23}
$$

The complete endpoint owns the entire face \(\rho=7/8\).

Combining the switches,

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\
\dfrac{54}{(1-\rho)^2},&5/6\le\rho<7/8.
\end{cases}
\tag{24}
$$

At \(\rho_{HK}\), the first two values agree.

## 6. Residual-component inventory

The exact analytic residual is one open vertical-strip component. The
frequency slice at each interior ratio is the nonempty interval
\((L(\rho),U(\rho))\). Nonemptiness follows as follows:

- \(H_0(\rho)>1/(2\rho)\) for \(\rho>\rho_*\);
- after \(\rho_{HK}\), \(K_0\) is increasing while the high-angular wall
  decreases until the lower-wall switch;
- after \(\rho_c>1/8\),
  \(\eta_\rho<1/2\) gives
  \(K_0(\rho)>4a_\rho=8\pi\rho/(1-\rho)>
  \pi/(1-\rho)\);
- on the seam, \(54/(1-\rho)^2>\pi/(1-\rho)\).

On every compact ratio subinterval of \((\rho_*,7/8)\), the positive gap
\(U-L\) has a positive lower bound, including the downward upper-bound
switch at \(5/6\). Vertical motion followed by a path just above the
continuous lower wall connects any two points. No sampled plot is used for
this component statement.

For proof design and face ownership, split the component into the following
exact cells. A boundary listed as an analytic wall is excluded from the
residual.

| ratio cell | lower wall | upper wall | special owner or interface | first candidate mechanism |
|---|---|---|---|---|
| \((\rho_*,1/16]\) | \(1/(2\rho)\) | \(H_0\) | \(1/16\) is coarse only | sharpen small-hole tail payment |
| \((1/16,\rho_{HK})\) | \(1/(2\rho)\) | \(H_0\) | full \(H_0\) continuation | exact low-interface compression |
| \(\rho=\rho_{HK}\) | \(1/(2\rho)\) | \(H_0=K_0\) | shared upper face | match both upper proofs |
| \((\rho_{HK},\omega_0)\) | \(1/(2\rho)\) | \(K_0\) | \(H_0\) remains accepted above its own wall | fixed-ratio constant compression |
| \(\rho=\omega_0\) | \(1/(2\rho)\) | \(K_0\) | small-hole branch is open here | direct action/tail estimate |
| \((\omega_0,\rho_c)\) | \(1/(2\rho)\) | \(K_0\) | no small-hole input | strict lattice aggregation |
| \(\rho=\rho_c\) | shared lower wall | \(K_0\) | high-angular and zero-count meet | exact face match |
| \((\rho_c,1/2)\) | \(\pi/(1-\rho)\) | \(K_0\) | \(\eta_\rho=\omega_0\) | finite-radial symbolic compression |
| \(\rho=1/2\) | \(2\pi\) | \(K_0\) | \(K_0\) formula is continuous but changes derivative | pilot-centered exact lemma |
| \((1/2,5/6)\) | \(\pi/(1-\rho)\) | \(K_0\) | \(\eta_\rho=G_1(\rho)\) | monotone action deficit |
| \(\rho=5/6\) | \(6\pi\) | \(1944\) | seam begins inclusively | exact seam face |
| \((5/6,7/8)\) | \(\pi/(1-\rho)\) | \(54/(1-\rho)^2\) | endpoint face excluded from residual | bounded seam bridge |

The certified box \(B_0\) straddles \(\rho=1/2\): it occupies a terminal
sliver of the \((\rho_c,1/2)\) row, the \(\rho=1/2\) face, and an initial
sliver of the \((1/2,5/6)\) row. It is overlaid, not added to
\(\mathcal A_{16}\). Thus \(\mathcal U_{16}\) is obtained from the analytic
component by removing one already discharged closed box. Any new box
\(B_1\) must satisfy

$$
B_1\subset\mathcal D_{16},
\qquad
B_1\setminus B_0\subset\mathcal U_{16},
\tag{25}
$$

and may overlap \(B_0\) only on its assigned complete shared face.

## 7. Four-zone integration and the \(K=295^2\) face

The coarse four-zone envelope is derived from, but is not equal to, the
exact mask:

1. on \([\rho_*,1/16]\), \(H_0(\rho)\le H_0(1/16)<64\);
2. on \([1/16,5/6]\),
   \(K_0(\rho)\le K_0(5/6)<295^2\);
3. on \([5/6,7/8]\),
   \(54/(1-\rho)^2\le3456\);
4. on \([7/8,1)\), the endpoint covers every frequency.

The strict estimate

$$
K_0(5/6)<295^2
\tag{26}
$$

is independent of the seam theorem. At \(Y=295\), the accepted comparison is

$$
\eta_{5/6}Y^2-\sqrt{a_{5/6}}Y-C_0
>
\frac1{49}295^2-6\cdot295-\frac{307}{175}
=\frac{5226}{1225}>0.
\tag{27}
$$

The positive root in (1) therefore lies strictly below \(295\).

At \(K=295^2=87025\):

- the small-hole upper ray owns the first zone because \(64<87025\);
- the fixed-ratio upper ray owns the second because (26) is strict;
- the seam upper ray owns the third because \(3456<87025\);
- the complete endpoint owns the fourth.

Thus equality at the global energy face is already covered in every ratio
band. Nothing in this section proves any point of \(\mathcal D_{16}\).

## 8. Evidence classes

- **Accepted analytic coverage:** A0--A10 and only their exact domains.
- **Accepted certified coverage:** the closed box \(B_0\) only.
- **Exact mask computation:** certified sign classification of rational
  parameter points; this verifies set bookkeeping, not the spectral theorem.
- **Diagnostic numerics:** plots, decimal switch estimates, and sampled
  classifications; these select questions but prove no domain.
- **Finite symbolic ledger:** exact constant or polynomial checks; these do
  not prove the analytic hypotheses from which the constants arise.

## 9. Falsification and face ledger

Every later proof or certificate must test:

- \(\rho=\rho_*,1/16,\rho_{HK},\omega_0,\rho_c,1/2,5/6,7/8\);
- both sides of the open face \(\rho=\omega_0\);
- \(K=1/(2\rho)\) and \(K=\pi/(1-\rho)\), including their shared face;
- every active \(K=H_0(\rho)\) and \(K=K_0(\rho)\) face;
- \(K=1944,2048,3456,295^2\);
- all retained \(20,24,32,54\) seam-domain endpoints;
- the complete closed boundary of \(B_0\);
- a point in \((1/16,\omega_0)\) above \(H_0\), to prevent truncating the
  small-hole theorem at the coarse switch;
- a point in \(B_0\), which must be **certified_only**, not
  **analytic_covered**;
- any **indeterminate** classifier result, which must never be coerced to a
  Boolean answer;
- every spectral, phase, angular, radial, floor, inverse, denominator,
  radicand, and squaring wall introduced by a candidate lemma.

## 10. Frozen artifact manifest

| artifact | SHA-256 |
|---|---|
| state/proof_obligations.yml | dc2552091ff79f5ab39de896b4d97cf22ccc234f3842ee9734d54d123c5f2379 |
| state/next_round_prompts.md | 9dda7a121c16a8627f8c319af54156873fe7f33495d9e8bdd5f56dbabae8ac18 |
| state/lemma_packets/SHELL-rho-zero-endpoint.md | 023390e00afa1754c08289d6c28172ac32df1e6abff2c1230b5f610a3db10aad |
| state/lemma_packets/SHELL-low-interface-small-hole.md | 071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a |
| state/lemma_packets/SHELL-thin-width-zero-count.md | 09c0738690860b1585ab0d9b62f011b157b060b88efbe446fdb4022b180ac7b8 |
| state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md | 0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f |
| state/lemma_packets/SHELL-central-thin-seam-compression-round15.md | c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7 |
| state/lemma_packets/SHELL-rho-one-endpoint-round16.md | 5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09 |
| state/lemma_packets/SHELL-rho-compact.md | 8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7 |
| computations/round17_residual_mask.py | b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b |
| computations/tests/test_round17_residual_mask.py | de43ee6b54d57b41db647f8b2c0cb2a79609069e59d0b2a50d335730a413dcc8 |
| rounds/polya-main/round_008/certification/pilot-central-box.json | f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00 |
| rounds/polya-main/round_008/certification/pilot-central-box-check.json | 02b12e13ad329e77035d8438ec359b6be4dd35571c384543f3890d67c132e6cc |

Reproduction commands:

~~~powershell
python computations/round17_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round17_residual_mask.py -q
~~~

Expected focused result: 16 tests passed.

After this file receives its external SHA-256 freeze record, no worker may
edit it. Any correction requires a new packet and a new hash. A2 and A3 must
begin from the same frozen bytes, and A3 must not inspect A2's proof before
returning its initial verdict.
