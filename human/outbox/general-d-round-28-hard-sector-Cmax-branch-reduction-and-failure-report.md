# General dimension, Round 28: hard-sector Cmax branch reduction and failure report

Date: 19 July 2026  
Status: rigorous branchwise reduction; the conditional Cmax sign remains open

## 0. Scope and theorem boundary

This note attempts the Round 27 target

\[
 \mathcal C_{\max,8}\geq0
 \quad\hbox{only on}\quad
 p>dm,\qquad 0\leq E<E_*:=\frac{p-dm}{2p}.
 \tag{0.1}
\]

It proves two reductions which were not available in Round 27.

1. For every fixed discrete/interface tuple, the exact hard sector is one
   initial interval in the phase angle.  This follows from a strict
   derivative estimate using the owner activity wall.
2. After splitting the literal maximum into its curvature and elasticity
   cells, every phase cell has a finite intrinsic candidate list.  The
   curvature cell is strictly convex.  The elasticity cell is strictly
   decreasing off the quadratic top-payment cell and has at most one
   stationary minimum on that cell.  The maximum switch is unique.

The signs at the resulting candidates are **not** proved.  Thus this note
does not prove (0.1), high-floor CST, or the all-dimensional theorem.  It
ends at two exact branchwise inequalities and records the observed extremal
pattern.  No ratio partition, global \(\alpha\)-monotonicity, or compact
certificate is introduced.

## 1. Exact domain and dependencies

Work on either extension grid:

\[
 r\in\mathbb N,\ r\geq1,
 \quad\hbox{or}\quad
 r\in\mathbb N_0+\frac12,\ r\geq\frac32.
\]

Let \(p,m\in\mathbb N\), \(f\geq2\), \(0\leq\alpha<1\), and put

\[
 x=r+p,\qquad q=r+p+m,\qquad X=m+\alpha,
 \qquad \mu=q+\alpha.
\tag{1.1}
\]

For \(0<t<\pi/2\), define

\[
 K=\frac{\mu}{\cos t},\qquad
 A_t(z)=G_K(z)-G_\mu(z),\qquad h=f-\frac14.
\]

The complete first-shelf conditions are

\[
 h\leq A_t(x),\qquad A_t(x+1)<h,\qquad A_t(r)<h+1.
\tag{1.2}
\]

The strict activity condition is

\[
 \frac{\mu^2}{\cos^2t}>
 \frac{\pi^2}{(1-\cos t)^2}+\gamma,
 \qquad
 \gamma=\frac34\ \hbox{or}\ 2
\tag{1.3}
\]

on the integer or half-integer owner respectively.

Retain

\[
 c=\frac t\pi,\qquad d=1-2c,
 \qquad W=\frac\mu\pi(\tan t-t),
 \qquad \lambda=h-W>0,
\tag{1.4}
\]

\[
 B_0=[W+\tfrac14]_<,\qquad
 Z(t)=\frac d{2c}=\frac\pi{2t}-1,
\tag{1.5}
\]

and the literal top payment

\[
 \Psi(\lambda)=
 \mathbf 1_{\{0<\lambda<1\}}
 \min\{1,2(\tfrac34-\lambda)_+^2\}.
\tag{1.6}
\]

At the two shelf endpoints write

\[
 e_0=A_t(r)+\frac14-f,\qquad
 e_p=A_t(x)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p,
 \qquad a_p=\frac{p^2}{3(2r+p)}.
\tag{1.7}
\]

The two exact Round 21 lower payments are

\[
 s=\sqrt{1+\frac{p(2r+p)}{X(X+2r+2p)}},\qquad g=s-1,
\]

\[
 L_{\rm el}=g\lambda,
 \qquad
 L_{\rm curv}=k(1-\cos t),
 \qquad
 k=\frac{p(2r+p)}{2\pi\mu},
\tag{1.8}
\]

and \(L_0=\max\{L_{\rm el},L_{\rm curv}\}\).  The conditional
scalar is exactly

\[
 \boxed{
 \mathcal C_{\max,8}
 =(p+a_p)L_0-pE_*+B_0Z+\Psi(\lambda)-\frac18.}
\tag{1.9}
\]

Only the audited first-shelf/action formulas, the Round 21 elasticity and
curvature bounds, the Round 23 definition of the root-free scalar, and the
Round 27 automatic/hard split are dependencies.  No earlier conjectural
sign is used.

## 2. The hard sector is one phase interval

### Proposition 2.1 (strict hard-gap transport)

Fix \((r,p,m,f,\alpha)\).  On every feasible phase interval on which

\[
 p>d(t)m,
\tag{2.1}
\]

the hard gap

\[
 H(t):=E(t)-E_*(t)
\tag{2.2}
\]

is strictly increasing.  Consequently the exact hard sector \(H<0\), if
nonempty, is one initial phase interval.  Its right endpoint is either the
unique root \(H=0\) or an endpoint of the shelf/activity interval.

If (2.1) first becomes true inside the feasible interval, no hard sector can
begin there: at the seam \(p=dm\), one has \(E_*=0\) and hence
\(H=E\geq0\), after which \(H\) increases strictly.

### Proof

For fixed \(\mu\), direct differentiation of the ball action gives

\[
 \frac{\partial A_t(z)}{\partial t}
 =\frac{\mu\sin t}{\pi\cos^2t}
 \sqrt{1-\left(\frac{z\cos t}{\mu}\right)^2}.
\tag{2.3}
\]

Both shelf endpoints satisfy \(0<r<x<\mu\).  Therefore each square root
in (2.3) is strictly larger than \(\sin t\), and

\[
 E'(t)>2W'(t),
 \qquad W'(t)=\frac\mu\pi\tan^2t.
\tag{2.4}
\]

The activity wall (1.3), for either positive value of \(\gamma\), implies

\[
 \mu>\frac{\pi\cos t}{1-\cos t}.
\]

Hence

\[
 W'(t)>
 \frac{\sin^2t}{\cos t(1-\cos t)}
 =1+\sec t.
\tag{2.5}
\]

Now set \(\varepsilon=\pi/2-t\).  Since

\[
 \cos t=\sin\varepsilon<\varepsilon<2\varepsilon
 =\pi d,
\tag{2.6}
\]

one has \(\sec t>1/(\pi d)\).  Condition (2.1) gives

\[
 \frac{m}{p\pi}<\frac1{\pi d}.
\tag{2.7}
\]

Finally

\[
 E_*'(t)=\frac{m}{p\pi},
\]

and (2.4)--(2.7) give, with room to spare,

\[
 H'(t)=E'(t)-E_*'(t)
 >2(1+\sec t)-\frac{m}{p\pi}>0.
\tag{2.8}
\]

The seam statement follows from \(E_*=0\) and \(E\geq0\).  This proves
the proposition. \(\square\)

No sampled monotonicity is used in this proof.  In particular, the
hard-sector root used by the Round 27 diagnostic is now analytically
justified.

## 3. Exact curvature/elasticity cell reduction

For the rest of the note fix \((r,p,m,f,\alpha)\), so \(\mu,X,g,k,a_p\)
are constants.  Put \(M=p+a_p\).  On a cell where \(B_0\) and the branch
of \(\Psi\) are fixed, define

\[
 \mathcal C_{\rm el}=Mg\lambda-pE_*+B_0Z+\Psi-\frac18,
\]

\[
 \mathcal C_{\rm curv}=Mk(1-\cos t)-pE_*+B_0Z+\Psi-\frac18.
\tag{3.1}
\]

Then

\[
 \mathcal C_{\max,8}=\max\{\mathcal C_{\rm el},
 \mathcal C_{\rm curv}\}.
\tag{3.2}
\]

### Proposition 3.1 (finite phase candidates)

On every fixed exact tuple the following statements hold.

1. The switch function
   \[
    F(t)=g\lambda-k(1-\cos t)
   \]
   is strictly decreasing.  Hence there is at most one
   elasticity/curvature switch.
2. On a curvature-owned cell, \(\mathcal C_{\rm curv}\) is strictly
   convex and has at most one stationary point.
3. On an elasticity-owned cell where the top payment is zero or saturated,
   \(\mathcal C_{\rm el}\) is strictly decreasing.
4. On the open quadratic top cell, \(\mathcal C_{\rm el}\) has at most one
   stationary point, and that point is a strict minimum.

Thus the conditional sign on a fixed tuple need only be checked at:

- the shelf, activity, and hard-sector endpoints;
- the literal terminal-action walls \(W+1/4\in\mathbb Z\) and their bad
  right sides;
- the top-payment walls
  \(\lambda=3/4\), \(\lambda=3/4-1/\sqrt2\), and \(\lambda=1\);
- the unique maximum switch, if present;
- the unique curvature stationary point on each curvature cell;
- the unique quadratic elasticity stationary point, if present.

### Proof

Since \(W'=\mu\tan^2t/\pi>0\),

\[
 F'(t)=-gW'(t)-k\sin t<0.
\tag{3.3}
\]

On the quadratic top cell put

\[
 u=\frac34-\lambda=W-(f-1),
 \qquad 0<u<\frac1{\sqrt2}.
\]

There \(\Psi=2u^2\).  Direct differentiation gives

\[
 \mathcal C_{\rm curv}'
 =Mk\sin t-\frac m\pi-\frac{B_0\pi}{2t^2}+4uW',
\tag{3.4}
\]

\[
 \mathcal C_{\rm curv}''
 =Mk\cos t+\frac{B_0\pi}{t^3}
 +4\{(W')^2+uW''\}>0.
\tag{3.5}
\]

Off the quadratic cell, the final positive term in (3.5) is absent, while
the first two terms remain strictly positive.  This proves the curvature
claim.

For the elasticity branch, the derivative is strictly negative on a zero
or saturated top cell:

\[
 \mathcal C_{\rm el}'
 =-MgW'-\frac m\pi-\frac{B_0\pi}{2t^2}<0.
\tag{3.6}
\]

On the quadratic cell,

\[
 \mathcal C_{\rm el}'
 =(4u-Mg)W'-\frac m\pi-\frac{B_0\pi}{2t^2},
\tag{3.7}
\]

\[
 \mathcal C_{\rm el}''
 =4(W')^2+(4u-Mg)W''+\frac{B_0\pi}{t^3}.
\tag{3.8}
\]

While \(4u-Mg\leq0\), equation (3.7) is negative.  The coefficient
\(4u-Mg\) is strictly increasing.  Once it becomes positive, every term in
(3.8) is positive, so (3.7) is strictly increasing.  It can therefore
vanish at most once, and any root is a strict minimum.  Together with
Proposition 2.1, the literal action/top walls, and (3.3), this proves the
candidate list. \(\square\)

Mathematica 15 independently simplified the residuals in
(3.3)--(3.8) to zero.  The replay is
`computations/general_d_round28_cmax_branch_derivatives.wl`; run

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\math.exe' -script `
  computations/general_d_round28_cmax_branch_derivatives.wl
```

It prints `round28DerivativeReplayOK=True`.  The displayed
differentiations, not that software output, are the proof.

## 4. Retaining the exact paired shelf

The candidate reduction does not replace the paired shelf by endpoint
constants.  Define the exact shelf slope and cumulative action

\[
 \sigma_t(z)=\frac1\pi\left{
 \arccos\left(\frac{z\cos t}{\mu}\right)
 -\arccos\left(\frac z\mu\right)\right},
\]

\[
 \mathscr I_t(y)=\int_y^\mu\sigma_t(z)\,dz.
\tag{4.1}
\]

Then the shelf, first-drop, and start-wall conditions are exactly

\[
 \mathscr I_t(x)\geq\lambda,
 \qquad
 \mathscr I_t(x+1)<\lambda,
 \qquad
 \mathscr I_t(r)<\lambda+1,
\tag{4.2}
\]

and

\[
 e_p=\mathscr I_t(x)-\lambda,\qquad
 e_0=\mathscr I_t(r)-\lambda.
\tag{4.3}
\]

Thus the hard inequality at every candidate is the exact correlated
condition

\[
 \boxed{
 \mathscr I_t(r)+\mathscr I_t(x)-2\lambda
 <\frac{p-dm}{2p}.}
\tag{4.4}
\]

In particular, no independent worst case for \(E\), \(\Delta\),
\(\lambda\), or \(B_0\) has entered Propositions 2.1 and 3.1.

## 5. What closes automatically and the two auxiliary Cmax gates

Define the terminal-only margin

\[
 \mathcal T
 :=B_0Z-pE_*-\frac18.
\tag{5.1}
\]

Since \(ML_0\geq0\) and \(\Psi\geq0\),

\[
 \boxed{\mathcal T\geq0\quad\Longrightarrow\quad
 \mathcal C_{\max,8}\geq0.}
\tag{5.2}
\]

Therefore a counterexample must lie in the exact terminal-deficient region

\[
 B_0\left(\frac\pi{2t}-1\right)
 <pE_*+\frac18.
\tag{5.3}
\]

The conditional Cmax route now stops at the following two intrinsic gates.
They are auxiliary sufficient gates, not the primary exact-remainder route.

### Elasticity gate

Prove on the exact paired-shelf/activity domain (4.2)--(4.4) that

\[
 \boxed{
 L_{\rm el}\geq L_{\rm curv}
 \quad\Longrightarrow\quad
 B_0\left(\frac\pi{2t}-1\right)
 \geq pE_*+\frac18.}
\tag{5.4}
\]

Equation (5.4) would close every elasticity-owned hard cell by (5.2).
The search below strongly supports it, but no derivation from the full
integrals (4.2)--(4.4) has been found.  Replacing those integrals by only
the coarse bounds \(L_0\leq\Delta<E_*\) is insufficient: the certified
Round 27 global counterexample satisfies the analogous relaxed
inequalities while lying outside the hard sector because its actual
endpoint sum is large.

### Curvature gate

On a curvature-owned cell the remaining exact sign is

\[
 \boxed{
 Mk(1-\cos t)-pE_*+B_0Z+\Psi(\lambda)-\frac18\geq0}
\tag{5.5}
\]

at the finite candidate list in Proposition 3.1, subject to
(1.2)--(1.3) and (4.4).  This is the first exact inequality on the observed
low-margin face.  It still contains the full lower-shelf wall and hard
endpoint sum; it is not the false global \(\mathcal C_8\) claim.

Equations (5.4)--(5.5) are not a ratio ladder.  They are the two literal
maximum cells required by (1.8).  If either fails, the strategy requires
returning to the exact residual

\[
 \max\{0,L_T\}+a_p\Delta\geq p(E_*-E),
\]

not adding another root-free scalar.

## 6. Equality-face audit

1. **Ordinary shelf wall.**  Equality \(A_t(x)=h\) is included and gives
   \(e_p=0\).  The observed limiting family lies on this face.
2. **First-drop and start walls.**  Equalities \(A_t(x+1)=h\) and
   \(A_t(r)=h+1\) are excluded and enter only as one-sided phase
   endpoints.
3. **Hard seam.**  Equality \(E=E_*\) belongs to the Round 27 automatic
   sector.  It is included only as a limiting candidate for the conditional
   scalar.
4. **The seam \(p=dm\).**  Here \(E_*=0\), so it is automatic.  Proposition
   2.1 proves that a hard interval cannot start on its far side.
5. **Terminal action wall.**  At \(W+1/4\in\mathbb Z\), the strict bracket
   has the lower count.  Immediately to the right, \(B_0\) increases by one
   and \(\mathcal C_{\max,8}\) jumps upward by \(Z>0\).  Both literal and
   bad-right values are in the candidate list.
6. **Top-payment walls.**  The payment is continuous at its quadratic,
   zero, and saturated seams; only its derivative changes.  The literal
   values are used in (3.4)--(3.8).
7. **Maximum switch.**  Both branch formulas agree at
   \(L_{\rm el}=L_{\rm curv}\).  No derivative continuity is assumed.
8. **Interface wall.**  When \(\alpha=0\), one has \(q=\mu\) and the
   ordinary interface count remains \(n=p+m\).  The proof uses the literal
   value, not continuity across a change of \(q\).
9. **Turning walls.**  Every shelf sample in (1.2) is below
   \(\mu<K\), so no \(r+j=K\) wall occurs.  The face \(q=\mu\) is already
   owned by item 8.

## 7. Loss ledger

Propositions 2.1 and 3.1, the switch reduction, and the exact shelf rewrite
(4.1)--(4.4) discard no positive term from \(\mathcal C_{\max,8}\).

The optional implication (5.2) discards only the nonnegative quantities

\[
 (p+a_p)L_0\quad\hbox{and}\quad\Psi(\lambda).
\]

It is used only to identify an automatic subregion, not to replace the
remaining gates.

Upstream, \(\mathcal C_{\max,8}\) is still a stronger and more lossy target
than the exact Round 27 residual: it compresses the actual endpoint pair to
\(L_0\) and compresses the fractional terminal reserve to the root-free
\(B_0\) and top payment.  The known global negative witnesses show that
these upstream losses are not harmless outside the exact hard sector.

## 8. Counterexample search and extremal pattern

The diagnostic program is

`computations/general_d_round28_hard_sector_cmax_branch_diagnostic.py`.

Run

```powershell
python -B computations/general_d_round28_hard_sector_cmax_branch_diagnostic.py `
  --limit 5 --random 200000 --seed 20260728
```

For every sampled \(\alpha\), the deterministic part brackets \(t\) on a
25-point mesh and applies bounded local minimization near the best sampled
cell; this is a diagnostic search, not a certified global minimization.  The
seeded mixed-scale part ranges through both owner grids,
\(r\) up to \(10^7\), \(p\) up to \(10^4\), \(m\) up to \(10^3\), and
floors through 32.  Together with the fixed near-switch regression below,
it retained 34,421 hard-sector records, including 23,878
elasticity-owned records.  It found

\[
 \#\{\mathcal C_{\max,8}<0\}=0,
 \qquad
 \#\{\mathcal T<0\hbox{ on an elasticity cell}\}=0.
\]

A fixed near-switch regression at

\[
 (r,p,m,f,\alpha)=(50,3,1,2,3/4),
 \qquad t=0.603519618679988\ldots
\]

has elasticity ownership by a margin of about \(4.08\times10^{-4}\) and
terminal-only margin

\[
 \mathcal T\approx0.2856199439.
\]

This is the smallest elasticity-owned terminal-only margin in the combined
structured regression set used for this round.  These are floating
diagnostic results, not coverage or proof of (5.4).

The sharp curvature-owned pattern remains

\[
 (r,p,m,f,\alpha)=(1,3,2,2,1^-),
 \qquad A_t(4)=\frac74,
\tag{8.1}
\]

with

\[
 t\to1.005008958418\ldots,\qquad
 \mathcal C_{\max,8}\to0.01286445198\ldots.
\tag{8.2}
\]

At the replay point \(\alpha=0.999999999\),

\[
 E\approx0.16765667<E_*\approx0.37993619,
\]

\[
 L_{\rm el}\approx0.09903151
 <L_{\rm curv}\approx0.15821798.
\]

Thus (8.1) is strictly in the hard sector and curvature-owned.  It lies on
the included lower-shelf wall and approaches the excluded interface face
\(\alpha=1\).  No negative exact tuple was found.

## 9. Failure report and next step

The attempted conditional proof does not close.  Its remaining auxiliary
Cmax claims are (5.4) on elasticity-owned cells and (5.5) on the finite
curvature candidate set.  The observed small-margin owner is the lower
shelf, \(f=2\), \(B_0=1\), quadratic-top, curvature cell (8.1); the
elasticity cells are separated from zero in all current diagnostics, but
that separation is not yet analytic.

The companion Round 28 exact-remainder projection retains substantially
more margin than (1.9).  Its primary complete-terminal scalar is

\[
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*),
 \qquad
 M_4=\max\{\tau(E+2\lambda),K_4\},
\]

with \(\tau=(s-1)/(s+1)\) and the proved quartic curvature payment
\(K_4\).  Therefore the next primary target is the complete-terminal
cell-to-wall reduction for \(\Psi^{L_T}_{4,E}\), with Proposition 2.1
available to control its right hard seam.  This notation is distinct from
the endpoint-rewritten auxiliary \(\widetilde\Psi^{L_T}_{4,e_p}\).
Equations (5.4)--(5.5) should remain regression gates and an optional
root-free fallback; they should not displace the exact residual
\(\max(0,L_T)+a_p\Delta\geq p(E_*-E)\).  If the exact residual does not
close, the next approved routes are \(\mathscr S\) and the weighted
aggregate.  The high-floor branch and the general theorem remain open.
