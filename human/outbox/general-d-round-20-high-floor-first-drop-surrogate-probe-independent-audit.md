# Independent audit: Round 20 high-floor first-drop probe

Date: 19 July 2026  
Verdict: **PASS as a diagnostic artifact; no theorem is proved**

## 1. Scope and source freeze

I independently read the revised strategy, the Round-10 derivation, the
frozen Round-20 note, and the complete Mathematica source.  I did not edit
the Round-20 note, source, or obligation graph.

The audited SHA-256 values are

- note: `f7d0134d9629dbf18c4e485447ae13306ef82a2404b7f21e58229f83f4624a55`;
- Mathematica source:
  `27d616054c378bf2be79ca6bbea7c3142fa822acb7a1f57030f4b144dc87d4e9`.

## 2. Independent formula reconstruction

For an inner tail, the source uses the ordinary-floor convention in

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,
\]

and defines the first shelf by

\[
 F_j=\lfloor A(r+j)+1/4\rfloor,\qquad
 p=\max\{j:F_0=\cdots=F_j\}.
\]

With $f=F_0$, direct substitution gives

\[
 R_p=2\int_r^{r+p}A-2pf
     =\mathcal C_p+p(\varepsilon _0+\varepsilon _p-1/2),
\]

where

\[
 \mathcal C_p=2\int_r^{r+p}A-p(A(r)+A(r+p)).
\]

Thus the two independently implemented forms of the exact reduced scalar are

\[
 \mathscr S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)
\]

and

\[
 \mathscr S=D_A(q)+\mathcal C_p
 +p(\varepsilon _0+\varepsilon _p-1/2)
 +\frac{d_\rho}{2}(n-p).
\]

The source's `LT` is exactly the full Round-10 terminal bound

\[
 L_T=\frac\pi2\sum_{k=1}^B\theta_k^{-1}
 +2\sum_{k=1}^B\eta_k-Q-2\delta
 +\frac{(v-B)_+^2}{\beta};
\]

in particular, it retains the fractional reserve, exact cap, and top
interval.  Substituting $L_T$ and

\[
 \mathcal C_p^{\rm low}
 =\frac{p^2}{3(2r+p)}(\varepsilon _0-\varepsilon _p)
\]

produces the printed `PhiDelta`.  Subtracting the two formulas leaves exactly

\[
 \mathscr S-\Phi_\delta
 =(D_A(q)-L_T)+(\mathcal C_p-\mathcal C_p^{\rm low}).
\]

No first-shelf reduction slack is silently included in that ledger; it is
reported separately as $D_A(r)-\mathscr S$.  The replay gives zero for both
the two-form scalar identity and the ledger residual at about 46 displayed
digits of numerical precision.

## 3. Phase, owner, and wall audit

Every record is created only after the evaluator has checked the strict
dimension-activity inequality, $r<\mu$, $n\ge1$, $f\ge2$, and $p<n$.
Integer shifts use the weakest new owner $d=4$; half-integer shifts begin at
$r=3/2$ and use $d=5$.  Higher-dimensional occurrences of a fixed shift
have the stronger activity wall.  The already completed $d=3$ half-grid is
therefore not sampled as a new owner.

The two floor functions are genuinely distinct in the source:

\[
 [m]_< =m-1,\qquad \lfloor m\rfloor=m,
 \qquad m-[m]_< =1.
\]

Consequently, at the interface fixture $\mu-r=4$, the evaluator owns
$n=4$ and $q=5$, rather than the erroneous machine-side value $n=3$.
All nine printed convention/activity checks are `True`.

The corrected terminal spatial wall is also consistent.  If

\[
 G_{K_0}(7)=3/4,\qquad q=5,
\]

then the first inverse level satisfies

\[
 G_{K_0}(q+y_1)=3/4,
\]

so $y_1=2$, not $1$.  At the wall, $\eta_1=1$.  Immediately on the
right, $y_1>2$ and $\eta_1\downarrow0$.  The exact terminal count gains
one doubled sample while the lower bound loses $2\eta_1$; hence both
$D_A(q)$ and $L_T$, and therefore both displayed scalars, jump downward
by exactly $2$.  The replay reproduces

\[
 \mathscr S_{\rm wall}\simeq3.32628619139471536,
 \quad \mathscr S_+\simeq1.32628619139471536,
\]

\[
 \Phi_{\delta,\rm wall}\simeq2.87965804728247172,
 \quad \Phi_{\delta,+}\simeq0.87965804728247172,
\]

with open-side discrepancies $3.11\times10^{-20}$ and
$3.06\times10^{-20}$.  The refined fixture additionally imposes
$G_K(3)-G_\mu(3)=7/4$, so $A(3)+1/4=2$; the ordinary floor therefore
owns $f=2,p=2,\varepsilon_p=0$, as stated.

## 4. Fresh replay

I ran the frozen source in a fresh Wolfram 15.0 kernel with `-noinit`, fed
through standard input with an explicit `Quit[]`.  It exited with code zero
and printed

- `diagnosticOnly=True` and `theoremClaim=False`;
- 19,619 retained records in total: 10,455 integer-owner and 9,164
  half-integer-owner records;
- zero negative samples for `exactS`, `PhiDelta`, `PhiMax`, and `PhiCap`;
- the common sampled minimizer
  $(r,n,q,f,p,B,Q)=(1,4,5,2,2,1,1)$, with
  $\mathscr S\simeq1.28429675325068119$ and
  $\Phi_\delta\simeq0.837805455134876165$;
- loss $0.446491298115805027$, split as terminal loss
  $0.441793677605750802$ and shelf loss
  $0.00469762051005422530$, with zero printed ledger residual;
- `round20ReplayOK=True`.

The family counts and minima, parity counts and minima, hard-wall values,
identity residuals, and previously proved slack checks all match the frozen
note.

## 5. Claim-boundary audit

The note repeatedly labels the work diagnostic, identifies the arithmetic
as high-precision floating rather than interval arithmetic, calls the wall
replay numerical, states that no counterexample was found rather than that a
bound was proved, and leaves CST-H and the general-dimensional theorem open.
The source repeats this boundary in its header and printed flags.  The
sampled positive minima are therefore suitable for theorem design and
falsification only; they are not a proof premise.

No inconsistency or omitted wall was found.  The Round-20 note and source
pass this independent audit in their explicitly diagnostic role.
