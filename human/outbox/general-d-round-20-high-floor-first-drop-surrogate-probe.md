# General dimension, Round 20: high-floor first-drop scalar probe

Date: 19 July 2026  
Status: diagnostic only; no theorem proved

## 1. Scope

This round follows WP4 of
`human/inbox/general-d_simplified_analytic_strategy.md`.  It tests the sole
remaining high-floor first-drop CST obligation without introducing a ratio
partition.

For an active inner tail, let

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,
\]

let \(f=F_0\ge2\), and let \(p<n\) be the endpoint of the first ordinary-floor
shelf.  The two quantities tested separately are

\[
 \mathscr S
 =D_A(q)+R_p+\frac{d_\rho}{2}(n-p)
 \tag{1.1}
\]

and the Round-10 lower surrogate

\[
\begin{aligned}
 \Phi_\delta={}&L_T
 +\frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p)
 +p\left(\varepsilon_0+\varepsilon_p-\frac12\right)
 +\frac{d_\rho}{2}(n-p),
\end{aligned}
\tag{1.2}
\]

where \(L_T\) is the full fractional terminal lower bound, including
\(2\sum\eta_k\), the exact cap \(-2\delta\), and the top interval.

The exact numerical loss ledger is

\[
 \boxed{
 \mathscr S-\Phi_\delta
 =\bigl(D_A(q)-L_T\bigr)
 +\left(
 \mathcal C_p-
 \frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p)
 \right).}
 \tag{1.3}
\]

Thus the terminal tangent loss and the shelf-curvature loss are measured on
the same correlated record.

The computation in this note is a falsification and theorem-design search.
It uses high-precision floating arithmetic, not interval arithmetic.  None of
the positive sampled minima below is a proof of \(\mathscr S\ge0\) or
\(\Phi_\delta\ge0\).

## 2. Grid ownership and strict walls

The evaluator uses the weakest new owner for each parity grid:

- integer shifts are tested with \(d=4\);
- half-integer shifts \(r\ge3/2\) are tested with \(d=5\).

For a fixed shift, higher-dimensional occurrences impose a stronger activity
wall, so their active parameter sets are contained in the corresponding
owner set.  Every retained record satisfies

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}
 +\frac{(d-2)^2-1}{4}.
\]

The literal conventions are implemented independently:

\[
 [m]_< =m-1,\qquad \lfloor m\rfloor=m,
 \qquad m-[m]_< =1.
\]

In particular, \(n=\lfloor\mu-r\rfloor\) uses the wall-aware ordinary floor.
An exploratory version used the machine decision `Floor[mu-r]`; at a
numerically reconstructed interface wall this could incorrectly replace
\(n=4,q=5\) by \(n=3,q=4\).  That defect was corrected before the official
replay.  The official wall checks all returned `True`.

The terminal spatial wall is also treated one-sidedly.  If an inverse
displacement crosses an integer \(m\), then its strict fraction is \(1\) at
the wall and tends to \(0\) immediately on the right.  Consequently both
the exact terminal defect and \(L_T\) can drop by \(2\).  Random interior
sampling alone is therefore not an adequate wall audit.

During exploration this face was once described in prose as
\(G_K(6)=3/4\).  An independent reconstruction showed that the printed
radius instead satisfies \(G_K(7)=3/4\): the relevant displacement is
\(y_1=2\), not \(1\).  The fixture, equations, and prose were corrected
before this note was frozen, and the corrected script was independently
replayed.

## 3. Search families

The final replay retained 19,619 active \(f\ge2,p<n\) records:

| family | records | smallest sampled \(\mathscr S\) | smallest sampled \(\Phi_\delta\) |
|---|---:|---:|---:|
| seeded active random sweep | 5,008 | 2.01297315751931 | 1.59035047851150 |
| exact ordinary shelf-end walls | 2,587 | 1.42493888170748 | 0.964388605885839 |
| simultaneous interface and shelf walls | 2,800 | 1.35916880184832 | 0.905436182286586 |
| right sides of terminal spatial walls | 7,914 | 1.32628619139472 | 0.879658047282472 |
| targeted \((\alpha,\eta_1)\) hard-face grid | 1,263 | 1.28475884825004 | 0.838266074055529 |
| refined \(\eta_1\downarrow0\) edge | 45 | 1.28432088338623 | 0.837829508207466 |
| edge/shelf-wall intersection | 1 | 1.28429675325068 | 0.837805455134876 |
| repeated fixed open-side replay | 1 | larger than the final minimum | larger than the final minimum |

There were 10,455 integer-owner records and 9,164 half-integer-owner records.
Their parity minima were

\[
\begin{array}{c|cc}
 &\min\mathscr S&\min\Phi_\delta\\ \hline
 d=4\text{ integer grid}
 &1.284296753250681&0.837805455134876\\
 d=5\text{ half-integer grid}
 &1.359168801848322&0.905436182286586.
\end{array}
\]

No negative value was found for \(\mathscr S\), raw \(\Phi_\delta\), the
variant replacing \(L_T\) by \(\max\{0,L_T\}\), or the weaker cap variant
replacing \(-2\delta\) by \(-\alpha h\).

## 4. The terminal spatial wall and its open side

The smallest broad wall record occurs near

\[
 r=1,\quad n=4,\quad q=5,\quad f=2,\quad p=2,
 \quad B=Q=1.
\]

Let \(K_0\) be the high-precision root

\[
 G_{K_0}(7)=\frac34,
\qquad
 K_0\approx11.04926798504801089907798018,
\]

and put \(\rho_0=5/K_0\).  The inverse level \(G_{K_0}(5+y_1)=3/4\)
then has \(y_1=2\).  At the literal wall, \(\eta_1=1\), and the evaluator
gives

\[
 \mathscr S_{\rm wall}
 \approx3.32628619139471535777421547,
\]

\[
 \Phi_{\delta,{\rm wall}}
 \approx2.87965804728247171951100733.
\]

The right-hand limits subtract exactly \(2\):

\[
 \mathscr S_{+}
 \approx1.32628619139471535777421547,
\qquad
 \Phi_{\delta,+}
 \approx0.879658047282471719511007329.
\]

Solving instead

\[
 G_K(7+10^{-20})=\frac34,
 \qquad \mu=5+10^{-20},
\]

replayed these right limits with discrepancies about \(3.11\times10^{-20}\)
and \(3.06\times10^{-20}\), respectively.  This is a numerical
one-sided replay, not an interval assertion.

## 5. Refined sampled extremum

The local \((\alpha,\eta_1)\) sweep showed that the hard pattern is not the
interface wall \(\alpha=0\).  It moves to the intersection of

1. the open side of the terminal spatial wall, \(\eta_1\downarrow0\); and
2. the lower ordinary-floor wall at the end of the first shelf,
   \(\varepsilon_p=0\).

The final record was defined reproducibly by

\[
 G_K(7+10^{-20})=\frac34,
 \qquad
 G_K(3)-G_\mu(3)=\frac74.
 \tag{5.1}
\]

It has

\[
\begin{aligned}
 K&\approx11.04926798504801089908941446,\\
 \mu&\approx5.038422037895470733530728519,\\
 \rho&\approx0.455996003057715497651833649,\\
 r&=1,\quad n=4,\quad q=5,\quad f=2,\quad p=2,\\
 \eta_1&=10^{-20},\qquad \varepsilon_p=0
 \quad\text{under the literal ordinary-floor convention}.
\end{aligned}
\]

Both sampled minima occur at this same record:

\[
 \boxed{\mathscr S
 \approx1.284296753250681192749170321,}
 \tag{5.2}
\]

\[
 \boxed{\Phi_\delta
 \approx0.837805455134876165477100445.}
 \tag{5.3}
\]

The exact numerical loss ledger at the record is

\[
 \mathscr S-\Phi_\delta
 \approx0.446491298115805027272069875,
\]

with

\[
 D_A(q)-L_T
 \approx0.441793677605750801968771600,
\]

and

\[
 \mathcal C_p-
 \frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p)
 \approx0.004697620510054225303298275.
\]

Thus about 99 percent of the surrogate loss at the observed extremum comes
from the terminal inverse-tangent estimate, not from (S3).  Nevertheless the
raw surrogate remains about \(0.838\) above zero in this search.

## 6. Replay checks

The official replay used

`15.0.0 for Microsoft Windows (64-bit) (May 19, 2026)`.

It printed numerical zero, with roughly 46 reported digits of accuracy, for

1. the equality of the two formulas for \(\mathscr S\);
2. the loss identity (1.3); and
3. the terminal correlation \(A(q)=v-h\).

This wording does not reinterpret a Mathematica precision tag as a certified
error bound.

Across all retained records, the smallest sampled slacks in the already
proved inequalities were approximately

\[
 D_A(r)-\mathscr S\ge0.103846723590005,
\]

\[
 D_A(q)-L_T\ge0.266144498959558,
\]

and the S3 slack was nonnegative, with exact zero attained in degenerate
\(p=0\) records.  All aggregate checks ended with
`round20ReplayOK=True`.

## 7. Failure report and next analytic target

No counterexample to either \(\mathscr S\ge0\) or
\(\Phi_\delta\ge0\) was found.  This does not close CST-H.

The search replaces the vague high-floor compact residual by a precise
theorem-design face:

\[
 (r,n,q,f,p,B,Q)=(1,4,5,2,2,1,1),
 \qquad
 \eta_1\downarrow0,
 \qquad
 \varepsilon_p=0,
 \qquad
 \alpha\approx0.0384220.
\]

The next analytic attempt should attack (1.2) on this intrinsic face and
prove that moving away from it increases the scalar, or derive a uniform
positive lower bound that has this face as its boundary test.  It should not
introduce a ratio ladder.  If the tangent surrogate cannot be controlled
globally, (1.1) retains an additional observed reserve of about \(0.446\) at
the hard face and is the next strategy-approved target.

The general-dimensional Pólya theorem remains open.

## 8. Reproduction

The diagnostic source is

`computations/general_d_round20_high_floor_first_drop_probe.wl`.

Run it with

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\SystemFiles\Kernel\Binaries\Windows-x86-64\wolframscript.exe' `
  -noprompt -run '<<computations/general_d_round20_high_floor_first_drop_probe.wl;Quit[]'
```

The local WolframScript installation emits a nonfatal missing-configuration
warning after the kernel output.  The replay result is printed before that
warning.
