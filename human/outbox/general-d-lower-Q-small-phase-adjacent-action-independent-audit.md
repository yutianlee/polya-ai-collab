# Independent audit: lower-\(Q\) small-phase adjacent-action closure

Date: 19 July 2026  
Audited source: `human/outbox/general-d-lower-Q-small-phase-adjacent-action-closure.md`  
Replay: `computations/general_d_small_phase_adjacent_action_replay.wl`  
Verdict: **PASS**

## 1. Scope checked

The note claims only the high-floor, first-drop, lower-\(Q\), hard-sector
sublemma

\[
 0<t\leq \frac{\pi}{8}\quad\Longrightarrow\quad \Delta>E_*.
\]

It does not claim closure of the remaining phase, the other endpoint
families, the complete high-floor CST theorem, or the all-dimensional
spectral theorem.  This theorem boundary is accurate.

## 2. Original-ratio transport

With \(X=z+P\), \(Q=z+(1+\rho)P\), and
\(u(y)=\sqrt{1-y^2}\), rationalization gives exactly

\[
 R(P)=\frac{u(z)-u(X)}{u(X)-u(Q)}
 =\frac{2z+P}{\rho\{2z+(2+\rho)P\}}
  \frac{u(X)+u(Q)}{u(z)+u(X)}.
\]

After clearing the positive denominator, the derivative numerator of the
first factor is \(-2z(1+\rho)<0\).  If the second factor is denoted by
\(H\), then

\[
 \frac{H'}H=
 -\frac{X/u(X)+(1+\rho)Q/u(Q)}{u(X)+u(Q)}
 +\frac{X}{u(X)\{u(z)+u(X)\}}<0.
\]

Indeed, the magnitude of the negative term is strictly larger than
\(X/[u(X)\{u(X)+u(Q)\}]\), which is strictly larger than the positive term
because \(u(z)>u(Q)\).  Both factors are positive, so \(R'(P)<0\).
This verifies the essential point that the **original** adjacent ratio,
not merely an already reduced face expression, transports monotonically to
\(Q\to1^-\).

At that face,

\[
 X_1=\frac{1+\rho z}{1+\rho},\qquad
 \{J(z,\rho)+1\}^2
 =\frac{(1+z)(1+\rho)^2}
 {\rho\{2+\rho(1+z)\}},
\]

and the logarithmic \(z\)-derivative of the right side is

\[
 \frac{2}{(1+z)\{2+\rho(1+z)\}}>0.
\]

Since every literal tuple has \(Q<1\) and \(z>z_0(t)\), the two transports
are strict:

\[
 R(P)>J(z,\rho)>J(z_0(t),\rho).
\]

## 3. Polynomial sign audit

Squaring is reversible because both shifted sides are positive.  The exact
residual is

\[
 \Phi(z,d,\rho)=4(1+z)(1+\rho)^2
 -\rho\{2+\rho(1+z)\}(3-d\rho)^2.
\]

Its \(z\)-derivative factors as

\[
 \Phi_z=\{2-\rho+d\rho^2\}
 \{2(1+\rho)+\rho(3-d\rho)\}>0,
\]

because, for \(0<d\rho<1\),
\(\rho(1-d\rho)\leq1/(4d)\), and \(d\geq3/4\).
Furthermore

\[
 z_0(t)>\frac{4t^3}{9\pi}>
 \frac{4t^3}{\pi^3}=\frac{(1-d)^3}{2}=Z(d).
\]

For \(s=d\rho\in(0,1)\), multiplication by the positive factor \(d^2\)
produces the stated polynomial

\[
 \mathcal P(d,s)=4(1+Z)(d+s)^2
 -s\{2d+s(1+Z)\}(3-s)^2.
\]

The displayed tensor-product Bernstein expansion of \(\mathcal P_d\) was
recomputed exactly.  Its minimum coefficient is \(341/128>0\), so
\(\mathcal P\) is increasing in \(d\) on
\([3/4,1]\times[0,1]\).  At \(d=3/4\),

\[
 \mathcal P(3/4,s)=\frac3{512}q(s),
\]

where the stated quartic satisfies \(q''\geq1352\) on \([0,1]\).  The
exact strong-convexity lower bound is

\[
 q(s)\geq
 \frac{53111042695}{11341398016}>0.
\]

Thus \(\Phi(z_0,d,\rho)>0\), hence
\(J(z_0,\rho)>E_*\).  Combining this with the strict transports and
\(f-1\geq1\) proves the stated theorem.

## 4. Equality and wording audit

- \(Q=1\) is used only as a one-sided analytic limit; it is not reassigned
  as an owned spectral point.
- The strict inherited inequality \(z>z_0\) supplies the second strict
  comparison.
- The included endpoint \(t=\pi/8\) is covered by the exact positive
  quartic bound.
- The hard equality \(d\rho=1\) belongs to the automatic sector and is not
  needed here.
- One harmless overstatement was corrected during audit: the
  strong-convexity inequality was changed from “for every real \(s\)” to
  “for every \(s\in[0,1]\),” which is the domain on which
  \(q''\geq1352\) was proved and the only domain used.

## 5. Mathematica replay

Running

```powershell
wolframscript -file computations/general_d_small_phase_adjacent_action_replay.wl
```

under Mathematica 15 returned zero for every symbolic residual, reproduced
the full Bernstein coefficient matrix and its minimum \(341/128\),
reproduced all three rational quartic values, and printed

```text
roundSmallPhaseReplayOK=True
```

The replay is an exact identity audit; the sign proof is the analytic chain
above.

