# General dimension, Round 27: exact-surrogate hard-sector diagnostic

Date: 19 July 2026  
Status: diagnostic only; no theorem proved

## 0. Result and scope

This round returns to the exact Round 20 high-floor first-drop quantities

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

and

\[
 \Phi_\delta=L_T+a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}.
 \tag{0.1}
\]

It has three conclusions.

1. The proposed large tuple
   \((r,p,m,f,\alpha,t)=(4036,32,1,2,1/16,79/500)\) is an exact feasible
   first drop, but it is not close to a counterexample:
   \(\mathscr S\approx47.13919\) and
   \(\Phi_\delta\approx40.79765\).
2. That tuple lies in an elementary automatic sector.  Its negative values
   of the root-free scalars \(\mathcal R_J\) and
   \(\mathcal C_{\max,8}\) therefore do not obstruct a proof which splits
   off this automatic sector first.
3. A finite adversarial exact-domain scan found no negative value of
   \(\mathscr S\), raw \(\Phi_\delta\), the strengthened
   \(\Phi_+\), \(\mathcal R_J\), or \(\mathcal C_{\max,8}\) in the
   complementary hard sector.  The smallest observed
   \(\mathcal C_{\max,8}\) is the already known
   \(0.01286457\ldots\) lower-shelf family.

The scan uses ordinary floating arithmetic.  Its positive minima are not
certificates.  The general-dimensional Polya theorem and high-floor CST-H
remain open.

## 1. An exact automatic-sector split

Retain the Round 21 notation

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p\geq0,
 \qquad a_p=\frac{p^2}{3(2r+p)},
\]

\[
 d=1-\frac{2t}{\pi},\qquad m=n-p\geq1.
\]

The exact terminal defect satisfies both \(D_A(q)\geq0\) and
\(D_A(q)\geq L_T\).  Hence

\[
 L_T^+:=\max\{0,L_T\}
\]

is also a valid terminal lower bound.  Define

\[
 \Phi_+=L_T^++a_p\Delta+p(E-\tfrac12)+\frac{dm}{2}.
 \tag{1.1}
\]

Since \(L_T^+,a_p\Delta,E\geq0\), (1.1) is nonnegative whenever

\[
 p\leq dm
 \tag{1.2}
\]

or, for \(p>dm\), whenever

\[
 E\geq\frac12-\frac{dm}{2p}.
 \tag{1.3}
\]

Thus the only sector needing the correlated analytic machinery is

\[
 \boxed{
 p>dm,
 \qquad
 E<\frac12-\frac{dm}{2p}.}
 \tag{1.4}
\]

This is an algebraic split of the exact scalar, not a sampled assertion and
not a ratio ladder.

Both Round 26 sufficient-scalar counterexamples are outside (1.4).  At the
certified \(\mathcal C_8\) witness,

\[
 E\approx1.00196460,
 \qquad
 \frac12-\frac{dm}{2p}\approx0.41090588,
\]

and at the certified Round 25 \(\mathcal F\) witness,

\[
 E\approx0.27918451,
 \qquad
 \frac12-\frac{dm}{2p}\approx0.16374715.
\]

Thus neither known falsification tests the hard-sector target below.

## 2. Exact replay of the proposed large tuple

Put

\[
 r=4036,\quad p=32,\quad m=1,\quad f=2,
 \quad\alpha=\frac1{16},\quad t=\frac{79}{500}.
\]

Then

\[
 q=4069,\qquad \mu=4069+\frac1{16},
 \qquad K=\frac{\mu}{\cos t}
 \approx4120.38625733780336.
\]

A 90-digit replay gives the literal owners

\[
 n=33,\qquad (f,p)=(2,32),\qquad (B,Q)=(1,1).
\]

The full shelf and first-drop margins are

\[
 \frac{11}{4}-A(r)>0.01683433,
\]

\[
 A(r+p)-\frac74>0.01865911,
 \qquad
 \frac74-A(r+p+1)>0.02683000.
\]

The integer-owner activity margin is larger than \(1.69\times10^7\).
The sole inverse displacement is

\[
 y_1\approx21.86960472591855,
 \qquad
 \eta_1\approx0.86960472591855,
\]

so no inverse wall ambiguity is present.

The terminal ledger is

\[
 D_A(q)\approx27.82817120625015,
 \qquad
 L_T\approx24.24892333361137,
\]

\[
 D_A(q)-L_T\approx3.579247872638777.
 \tag{2.1}
\]

The shelf ledger is

\[
 R_p\approx18.86130901583900,
 \qquad
 \mathcal C_p\approx2.802916034796064,
\]

\[
 a_p\Delta\approx0.0406241656452532,
 \qquad
 \mathcal C_p-a_p\Delta
 \approx2.762291869150810.
 \tag{2.2}
\]

Consequently

\[
 \boxed{\mathscr S\approx47.13918726007211,}
\]

\[
 \boxed{\Phi_\delta\approx40.79764751828252.}
\]

The loss identity closes to about \(10^{-89}\):

\[
 \mathscr S-\Phi_\delta
 =(D_A(q)-L_T)+(\mathcal C_p-a_p\Delta).
\]

For this tuple,

\[
 E\approx1.001824780657592,
 \qquad
 \frac12-\frac{dm}{2p}\approx0.485946655063032,
\]

so (1.3) applies with a large margin.  By contrast,

\[
 \mathcal R_J\approx-1.232653692824896,
 \qquad
 \mathcal C_{\max,8}\approx-1.357650017320433.
 \tag{2.3}
\]

Equation (2.3) is useful failure information: neither root-free scalar is a
valid global target before the automatic-sector split.

The installed Mathematica 15 kernel independently loaded the definitions
from the frozen Round 20 evaluator and returned the same displayed values,
with zero printed ledger residual and
`round27FixedReplayOK=True`.

## 3. Adversarial exact-domain scan

The diagnostic program is

`computations/general_d_round27_exact_phi_hard_sector_diagnostic.py`.

Every retained record satisfies (1.4) and keeps:

- the integer owner grid \(r=1,2,\ldots\) with activity constant
  \(\gamma=3/4\);
- the half-integer owner grid \(r=3/2,5/2,\ldots\) with
  \(\gamma=2\);
- \(q=r+p+m\), \(\mu=q+\alpha\), and \(K=\mu/\cos t\);
- the complete paired shelf, strict start, first-drop, and activity
  conditions;
- ordinary floors for shelf ownership and strict floors for terminal
  ownership;
- every retained inverse angle, inverse displacement, and strict fraction;
- literal terminal walls and their distinct bad right sides;
- the exact terminal and shelf loss ledger on each evaluated record.

The deterministic grid uses both parity classes, small radii and logarithmic
landmarks through \(r=10^4\), shelf lengths through \(64\), gap labels
through \(12\), floors \(2,3,4,6\), and eight interface fractions.  A
seeded log-random supplement uses

\[
 r\leq10^6,\qquad p\leq1000,\qquad m\leq200,
 \qquad f\leq16.
\]

For each feasible tuple the program samples the hard-sector interval, all
short lists of inverse spatial walls, the ends and interior of longer wall
lists, outer and shell terminal-action walls, and both the literal and
right-hand ownership values.

The frozen replay retained

\[
 14{,}106\text{ feasible hard-sector tuples},
 \qquad
 118{,}528\text{ scalar evaluations}.
\]

It found zero negative records for each of

\[
 \mathscr S,\quad\Phi_\delta,\quad\Phi_+,
 \quad\mathcal R_J,\quad\mathcal C_{\max,8}.
\]

The broad scan minima were

\[
 \min\mathscr S\approx1.32628738,
 \qquad
 \min\Phi_\delta\approx0.87965922,
\]

near the right side of the first inverse wall for
\((r,p,m,f,\alpha)=(1,2,2,2,0)\).  The sharper Round 20 intersection,
which solves the interface fraction rather than selecting it from the scan
grid, remains

\[
 G_K(7+10^{-8})=\frac34,
 \qquad
 A(3)=\frac74,
\]

and gives the one-sided values

\[
 \mathscr S\approx1.28429678,
 \qquad
 \Phi_\delta\approx0.83780548.
 \tag{3.1}
\]

As the displacement tends to zero, these converge to the Round 20 values
\(1.28429675325\ldots\) and \(0.83780545513\ldots\).

## 4. The surviving lower target

Let

\[
 L_0=\max\{L_{\rm elastic},L_{\rm curv}\}
\]

be the exact Round 21 simultaneous shelf payment, and define

\[
\boxed{
\begin{aligned}
 \mathcal C_{\max,8}={}&(p+a_p)L_0-\frac p2+\frac{dm}{2}
 +\frac{B_0d}{2c}\\
 &+\mathcal E(\lambda)-\frac18.
\end{aligned}}
\tag{4.1}
\]

The exact-cap scalar obeys

\[
 \mathcal R_J
 =\mathcal C_{\max,8}+\left(\frac18-J\right)
 >\mathcal C_{\max,8}.
 \tag{4.2}
\]

On the hard-sector scan, the smallest observed values were

\[
 \mathcal C_{\max,8}\approx0.0128645720672,
 \qquad
 \mathcal R_J\approx0.0466499635532,
\]

at the lower shelf wall for

\[
 (r,p,m,f,\alpha)=(1,3,2,2,0.999999).
 \tag{4.3}
\]

At (4.3) the two retained payments are approximately

\[
 L_{\rm elastic}=0.09903153,
 \qquad
 L_{\rm curv}=0.15821802,
\]

so the curvature member owns the observed minimum.  The elasticity member
must nevertheless remain in (4.1): it is precisely the reserve discarded
by the false global \(\mathcal C_8\) target.

This suggests the following sharper analytic workflow.

1. Close (1.2)--(1.3) directly with \(\Phi_+\).
2. Only on (1.4), prove or falsify
   \(\mathcal C_{\max,8}\geq0\) under the complete exact shelf, activity,
   parity, and wall conditions.
3. Retain the maximum in \(L_0\).  Returning to curvature-only
   \(\mathcal C_8\) would reintroduce the certified Round 26 failure.
4. Use (4.2) only after the exact maximum has been retained.

This hybrid target avoids both known Round 26 counterexamples and is sharper
than a global \(\mathcal R_J\geq0\) or
\(\mathcal C_{\max,8}\geq0\) claim, both of which are already false by
(2.3).  The scan supports the target but does not prove it.

## 5. Reproduction

Run

```powershell
python -B computations/general_d_round27_exact_phi_hard_sector_diagnostic.py `
  --random 10000 --wall-limit 120
```

The fixed-tuple replay alone is

```powershell
python -B computations/general_d_round27_exact_phi_hard_sector_diagnostic.py `
  --fixed-only
```

Any future negative value of \(\mathscr S\) or \(\Phi_\delta\) found by
this program must be reproduced in directed-rounding interval arithmetic;
the present run found none.
