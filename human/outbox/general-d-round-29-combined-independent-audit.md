# General dimension, Round 29: combined independent audit

Date: 19 July 2026  
Auditors: independent clean-room, constant-wall, and adversarial edge audits  
Status: **three analytic reductions pass; high-floor CST remains open**

## 0. Verdict

The following Round 29 statements pass independent audit on the inherited
high-floor extension-grid hard sector.

1. On every fixed-\(\alpha\) literal terminal count cell,
   \(\Psi^{L_T}_{4,E}\) is strictly increasing in \(t\).
2. On every fixed-\(K\), fixed-\(Q\) inverse- or outer-\(B\)-wall segment,
   the same scalar is strictly decreasing in \(\mu\).
3. On the entire primary component
   \[
    (r,p,m,f)=(1,2,2,2),\qquad B=Q=1,\qquad 2<y_1<3,
   \]
   one has
   \[
    \boxed{
    \Psi^{L_T}_{4,E}>
    \frac{371}{15840}+2\eta_1+2E>0.}
   \]

No blocking algebraic, derivative, wall-ownership, or scope error remains
after the corrections recorded below.  These results remove cell-interior
stationary points, constant-\(K\) wall-interior minima, and the first sharp
inverse cell.  They do **not** prove high-floor CST.  The nonconstant-\(K\)
shelf, \(Q\), activity, hard-sector, and \(\alpha\) endpoint intersections
remain open, as do the remaining inverse/\(B\) wall endpoints, pointwise
assembly, and the all-dimensional theorem.

## 1. Frozen audit objects

| Artifact | SHA-256 |
|---|---|
| `human/outbox/general-d-round-29-complete-terminal-phase-monotonicity-and-primary-inverse-cell-closure.md` | `e8c38fa4fdc2c9030b2d5dcde7b09861457f8e2c9e12dc8beec028cdcadac1df` |
| `computations/general_d_round29_cell_derivatives.wl` | `6d3b632077292fad4fd6ebb47dd10b87bd937d0ad6bc088aa45d8dcf42dccb0d` |
| `computations/general_d_round29_primary_face_rational_replay.py` | `d3df84adbccf841131536029ca0f71dbd56d939b9470df8cc72280909986f03b` |
| `computations/general_d_round29_adaptive_cusp_diagnostic.py` | `f18ed8219a8910016ee430914483a1b0ffb6f339aab3bad96baa24b96d32c681` |

The source hashes were rechecked after the final corrections and replays.

## 2. Phase-cell audit

For fixed \((r,p,m,f,\alpha)\), the interface radius \(\mu\) and cap \(J\)
are fixed.  The audited endpoint derivative gives

\[
 E'>2W',\qquad
 \{\tau(E+2\lambda)\}'>0,
 \qquad \mathcal K_4'>0,
 \qquad (E-E_*)'>0.
\]

Implicit differentiation of the complete inverse levels gives

\[
 \theta_k'<0,
 \qquad
 y_k'=K\tan t\,\frac{\sin\theta_k}{\theta_k}>0.
\]

Thus both \(\pi/(2\theta_k)\) and \(2\eta_k\) increase while the inverse
floor label is fixed.  The exact top triangle is also increasing, including
when \(B=0\).  Consequently the clipped terminal term is nondecreasing,
while the projected hard-gap contribution is strictly increasing.  This
proves strict cellwise monotonicity, including through the continuous top,
maximum-owner, and \(L_T=0\) seams.

The literal raw-\(L_T\) jumps were checked independently:

\[
 \Delta_{y_k\text{-wall}}L_T=-2,
 \qquad
 \Delta_{Q\text{-wall}}L_T=-1,
 \qquad
 \Delta_{B\text{-wall}}L_T=-\frac1{16\beta}.
\]

The complete scalar need not realize the full raw jump because
\(L_T\mapsto\max(0,L_T)\) can clip it.  The final note states the candidate
as the exact one-sided value and does not assume an un-clipped jump.

## 3. Constant-\(K\) wall audit

The proposition is restricted to the inherited target domain

\[
 p,m\ge1,\qquad
 r\ge1\ \text{on the integer grid},\qquad
 r\ge\frac32\ \text{on the half-integer grid},
\]

\[
 0<r<x<q\le\mu<K,\qquad 0<t<\frac\pi2.
\]

This scope makes every division by \(z\), \(\cos\chi_z\), and the radial
square roots legitimate, and gives \(q\ge3\).

For \(z=r,x\), the fixed-\(K\) action identity and radius-average formula
were rederived:

\[
 \mathfrak b_z'=\frac{t-\sin\chi_z}{\pi},
 \qquad
 \mathfrak b_z=\frac{u_z^2}{\pi}
 \int_\mu^K
 \frac{da}{a(\sqrt{a^2-z^2}+\sqrt{a^2-\mu^2})}.
\]

The angle comparison

\[
 \frac{\psi_z-\chi_z}{\cos\chi_z}
 \ge t-\sin\chi_z
\]

then proves \((\mathfrak b_z/u_z^2)'<0\).  The Round 21 elasticity ratio
has exactly the orientation needed to differentiate the elastic owner;
both it and the quartic-curvature owner strictly decrease.  The activity
and hard-sector conditions give

\[
 (E-E_*)'<-\frac{\sin\chi_r}{\pi}<0.
\]

All terminal outer data are constant on a fixed-\(K\) inverse or
outer-\(B\) wall, while \(J'(\mu)\ge0\).  Hence the complete scalar is
strictly decreasing on every fixed-\(Q\) segment.

At an isolated fixed-\(K\) \(Q\)-wall, raw \(L_T\) jumps upward by one, but
the complete scalar jumps only weakly upward by an amount in \([0,1]\).
Coincident shelf, activity, hard-sector, or \(\alpha\) endpoints retain all
feasible one-sided values.  This corrected statement is sufficient for the
left-limit candidate orientation and makes no claim on nonconstant-\(K\)
wall faces.

## 4. Primary inverse-cell audit

The rational enclosures defining the first inverse wall were checked with
positive denominators below \(\pi/2\):

\[
 \frac45<\theta_0<\frac{2\pi}{7},
 \qquad K_0>10.
\]

On the primary component these imply

\[
 \theta<\frac{2\pi}{7},\qquad v>\frac54,
 \qquad \beta<\frac25,\qquad c\le\beta.
\]

The exact cap representation gives \(J<1/9\), and the quadratic part of
the retained quartic member gives

\[
 \mathcal K_4>\frac4{15\pi}>\frac{14}{165}.
\]

Substitution into the literal complete-terminal formula yields

\[
 L_T>\frac{229}{288}+2\eta>0
\]

and then the claimed margin \(371/15840\).  The audit checked the literal
ownership at \(y_1=2,3\), the included \(\alpha=0\) face, the excluded
\(\alpha=1\) limit, the \(B=Q=1\) action walls, and the active top interval.

## 5. Independent falsification search

With seed 2900719, an independent phase scan generated 2,000 admissible
tuple instances on both inherited grids, using structured boundary values
and random large scales.  It tested 32,894 ordered same-terminal-cell
\(t\)-pairs and 9,833 centered derivatives; every sampled
\(\Psi^{L_T}_{4,E}\) slope was positive.  On 201 \(\alpha\)-slices and 199
interior phase samples, 39,612 records belonged to the primary
\(B=Q=1,\ 2<y_1<3\) component.  Every printed primary inequality passed;
the smallest sampled surplus over
\(371/15840+2\eta+2E\) was \(0.52034\).

An adversarial, non-load-bearing sweep tested 775 actual constant-\(K\)
inverse-wall paths and 58 actual outer-\(B\)-wall paths.  It retained 10,130
valid hard-sector points, 8,460 same-segment comparisons, and 1,326 centered
derivatives across both grids, boundary-heavy \(\alpha\) values,
\(p=1,\ldots,8\), \(m=1,\ldots,6\), and levels one through four.  Every
same-\(Q\), same-shelf segment decreased.  The largest sampled hard-gap
derivative was \(-0.1434\), the smallest sampled (K.13) slack was
\(0.00501\), and the smallest elasticity-ratio slack was \(0.0227\).

Separately, 250,000 angle tests found no violation of (K.6); numerical
quadrature reproduced the radius-average identity to relative error at most
\(6.9\times10^{-11}\).  These floating checks are counterexample searches,
not proof premises.

No \(B=0\) record occurred in the sampled in-scope high-floor hard sector.
A separate 100,000-point generic check found every top-triangle derivative
positive, and the first outer-action wall reproduced
\(-1/(16\beta)\) throughout \(10^{-5}\leq\beta\leq0.45\).  This checks the
Round 10 \(B=0\) top triangle without turning it into a proof premise.

The same stress test explains the explicit domain restriction.  Outside
the target grids, an auxiliary (K.13) slack can be negative at \(r=0\) or
\(r=1/2\).  No scalar counterexample was observed there, but the printed
proof does not cover those extraneous extensions and does not claim to.

## 6. Replay audit

The following commands passed on Mathematica 15.0.0 for Windows and Python
3.14.4:

```powershell
& (Get-Command wolframscript.exe).Source -file computations/general_d_round29_cell_derivatives.wl
python -B computations/general_d_round29_primary_face_rational_replay.py
python -B computations/general_d_round29_adaptive_cusp_diagnostic.py
```

The decisive outputs are:

```text
round29CellDerivativeResiduals={0,0,0,0,0,0,0,0,0,0,0,0}
round29PrimaryFaceArithmetic={0,0,0,0}
round29CellDerivativeReplayOK=True
round29PrimaryFaceRationalReplayOK=True
diagnosticOnly=True
round29AdaptiveCuspReplayOK=True
```

The adaptive cusp at

\[
 G_{K_0}(7)=\frac34,
 \qquad
 G_{K_0}(3)-G_{\mu_0}(3)=\frac74
\]

has sampled bad-side value

\[
 \Psi^{L_T}_{4,E}=0.8374553251557668\ldots.
\]

Its inverse-face and shelf-face derivatives have opposite signs.  Thus
global \(\alpha\)-monotonicity is false.  The decimals are isolated as
diagnostic-only evidence and imply no continuum theorem.

## 7. Promotion and gate decision

Promote only:

- complete-terminal phase/constant-\(K\) wall monotonicity; and
- the primary inverse-cell analytic closure.

Record the adaptive cusp as diagnostic-only with no implication edge.
Keep high-floor CST and the all-dimensional theorem open.  The next
pointwise target is a uniform treatment of the \(B=Q=1\) first inverse band
at its nonconstant-\(K\) shelf, \(Q\), activity, and simultaneous endpoint
intersections.  If that intrinsic wall theorem fails, return to the exact
scalar \(\mathscr S\) and then the weighted aggregate, rather than adding a
ratio ladder or another compressed scalar.
