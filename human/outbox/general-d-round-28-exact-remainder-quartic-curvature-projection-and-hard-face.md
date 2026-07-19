# General dimension, Round 28: exact-remainder quartic-curvature projection and the complete-terminal hard face

Date: 19 July 2026  
Status: new analytic lower projection proved; continuum sign remains open

## 0. Scope and theorem boundary

This note starts from the exact hard sector isolated in Round 27,

\[
 p>dm,\qquad 0\leq E<E_*:=\frac12-\frac{dm}{2p}<\frac12,
\tag{0.1}
\]

and keeps the actual endpoint remainder sum \(E\) and the complete Round 10
terminal reserve.  It does not use \(\mathcal C_8\),
\(\mathcal C_{\max,8}\), or \(\mathcal R_J\), whose global signs are false.

The new result is a two-term curvature projection

\[
 \mathcal K_4=L_{\rm curv}+\hbox{an explicit positive quartic term}
\]

and the rigorous chain

\[
 D_A(r)\geq\Phi_\delta^+
 \geq\Psi^{L_T}_{4,E}
 \geq\Psi^{\rm rf}_{4,E}.
\tag{0.2}
\]

Here \(\Psi^{L_T}_{4,E}\) retains \(\max\{0,L_T\}\), all inverse
fractions, the exact cap, and the top interval.  The secondary scalar
\(\Psi^{\rm rf}_{4,E}\) replaces only the terminal part by the previously proved
exact-cap, root-free lower bound.  Neither sign is proved on the continuum.

Thus this round does **not** prove high-floor CST or the all-dimensional
theorem.  It identifies a substantially less lossy curvature-owned residual
and its exact bad-side inverse-wall face.

Work on either extension grid, with

\[
 f\geq2,\quad p,m\geq1,\quad q=r+p+m,\quad
 \mu=q+\alpha,\quad 0\leq\alpha<1,
\]

\[
 t=\arccos\rho,\quad c=\frac t\pi,\quad d=1-2c,
 \quad K=\frac\mu{\cos t},\quad X=m+\alpha.
\]

The integer owner has \(r\in\mathbb N\), \(r\geq1\), and the
half-integer owner has \(r\in\mathbb N_0+1/2\), \(r\geq3/2\).  All tuples
also satisfy the exact shelf, first-drop, and dimension-labelled activity
conditions from Round 21.

Put

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(r+p)+\frac14-f,
\]

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p,
 \qquad a_p=\frac{p^2}{3(2r+p)}.
\tag{0.3}
\]

At the interface let

\[
 W=G_K(\mu),\qquad \lambda=f-\frac14-W>0,
 \qquad B_0=[W+\tfrac14]_<,
\]

\[
 J=2\int_q^\mu G_\mu(z)\,dz.
\tag{0.4}
\]

The strict bracket is literal at every action wall.  Finally, set

\[
 g=s-1,\qquad
 s=\sqrt{1+\frac{p(2r+p)}{X(X+2r+2p)}},
 \qquad \tau=\frac{g}{g+2}=\frac{s-1}{s+1}.
\tag{0.5}
\]

## 1. Proposition: exact-remainder and quartic-curvature projection

### 1.1 Statement, including strict-wall conventions

Define the explicit quartic curvature payment

\[
\boxed{
\begin{aligned}
 \mathcal K_4={}&
 \frac{(\mu^{-1}-K^{-1})
       \bigl((r+p)^2-r^2\bigr)}{2\pi}\\
 &+\frac{(\mu^{-3}-K^{-3})
       \bigl((r+p)^4-r^4\bigr)}{24\pi}.
\end{aligned}}
\tag{1.1}
\]

Its first line is exactly the Round 21 curvature member

\[
 L_{\rm curv}
 =\frac{1-\cos t}{2\pi\mu}\,p(2r+p).
\tag{1.2}
\]

Then every exact high-floor first-drop tuple satisfies

\[
 \boxed{\Delta>\mathcal K_4}
\tag{1.3}
\]

and, simultaneously,

\[
 \boxed{\Delta\geq\tau(E+2\lambda).}
\tag{1.4}
\]

Put

\[
 M_4:=\max\{\tau(E+2\lambda),\mathcal K_4\}.
\tag{1.5}
\]

Let \(L_T\) be the complete fractional terminal lower bound of Round 10,
and define the literal top payment

\[
 \mathcal P(\lambda)=
 \mathbf1_{\{0<\lambda<1\}}
 \min\{1,2(\tfrac34-\lambda)_+^2\}.
\tag{1.6}
\]

At \(\lambda=1\), the indicator in (1.6) is zero.  The face
\(\lambda=0\) is excluded by first-drop feasibility; its limit from within
the branch is not obtained by substituting zero into the indicator.  Define

\[
 T_{\rm rf}:=\frac{B_0d}{2c}-J+\mathcal P(\lambda).
\tag{1.7}
\]

On the hard sector (0.1), set

\[
\boxed{
 \Psi^{L_T}_{4,E}
 :=\max\{0,L_T\}+a_pM_4+p(E-E_*)}
\tag{1.8}
\]

and

\[
\boxed{
 \Psi^{\rm rf}_{4,E}
 :=\max\{0,T_{\rm rf}\}+a_pM_4+p(E-E_*).}
\tag{1.9}
\]

Then

\[
 \boxed{
 D_A(r)\geq\Phi_\delta^+
 \geq\Psi^{L_T}_{4,E}
 \geq\Psi^{\rm rf}_{4,E}.}
\tag{1.10}
\]

Consequently either sign

\[
 \Psi^{L_T}_{4,E}\geq0
 \quad\hbox{or, more strongly,}\quad
 \Psi^{\rm rf}_{4,E}\geq0
\tag{1.11}
\]

on the exact hard sector would close high-floor CST.  No such sign is
asserted in this note.

### 1.2 Dependencies

Only the following proved inputs are used.

1. Round 10: \(D_A(r)\geq\Phi_\delta^+\), with
   \(D_A(q)\geq\max\{0,L_T\}\).
2. Round 21: the exact shelf elasticity
   \(\Delta\geq g(\lambda+e_p)\).
3. Round 21: the complete-level/top-interval terminal estimate, before the
   replacement \(J<1/7\), namely \(L_T>T_{\rm rf}\).
4. Round 27: the automatic/hard split (0.1).
5. The elementary derivative formula for the shell action, proved directly
   below.

No conditional \(\mathcal C_{\max,8}\) sign, root certificate, ratio owner,
or numerical premise is used.

### 1.3 Proof

First use the exact shelf relation

\[
 e_p=\frac{E-\Delta}{2}.
\]

The Round 21 elasticity inequality becomes

\[
 \Delta\geq g\left(\lambda+\frac{E-\Delta}{2}\right).
\]

Moving the \(g\Delta/2\) term to the left and dividing by
\(1+g/2>0\) gives exactly

\[
 \Delta\geq\frac{g}{g+2}(E+2\lambda)
 =\tau(E+2\lambda),
\]

which proves (1.4).  This step retains the actual \(E\); it does not replace
\(E\) by the coarser lower bound \(g\lambda\).

For the curvature gain, write \(\sigma=-A'\).  On
\(0<z<\mu<K\), direct differentiation gives

\[
 \sigma(z)=\frac1\pi
 \left(\arccos\frac zK-\arccos\frac z\mu\right),
 \qquad \sigma(0)=0,
\]

and

\[
\begin{aligned}
 \sigma'(z)
 &=\frac1\pi\left(
   \frac1{\sqrt{\mu^2-z^2}}-
   \frac1{\sqrt{K^2-z^2}}\right)\\
 &=\frac1\pi\int_\mu^K
   a^{-2}\left(1-\frac{z^2}{a^2}\right)^{-3/2}\,da.
\end{aligned}
\tag{1.12}
\]

For \(0\leq u<1\), the binomial series has positive coefficients, so

\[
 (1-u)^{-3/2}\geq1+\frac32u,
\tag{1.13}
\]

strictly when \(u>0\).  Substitution in (1.12) yields

\[
 \sigma'(z)\geq\frac1\pi\left[
 (\mu^{-1}-K^{-1})
 +\frac{z^2}{2}(\mu^{-3}-K^{-3})\right].
\tag{1.14}
\]

Integrate first from \(0\) to \(z\), using \(\sigma(0)=0\), and then from
\(r\) to \(r+p\).  The result is precisely

\[
 \Delta=\int_r^{r+p}\sigma(z)\,dz\geq\mathcal K_4.
\]

Here \(r>0\), \(p>0\), and \(K>\mu\), so the omitted binomial terms have
positive integral; hence the inequality is strict.  This proves (1.3).

Round 27 gives the exact lower scalar

\[
 \Phi_\delta^+
 =\max\{0,L_T\}+a_p\Delta+p(E-E_*).
\tag{1.15}
\]

Equations (1.3)--(1.5) therefore imply

\[
 \Phi_\delta^+\geq
 \max\{0,L_T\}+a_pM_4+p(E-E_*)
 =\Psi^{L_T}_{4,E}.
\]

The Round 21 exact-cap terminal proof gives \(L_T>T_{\rm rf}\).  Since
\(x\mapsto\max\{0,x\}\) is increasing,

\[
 \max\{0,L_T\}\geq\max\{0,T_{\rm rf}\}.
\]

This proves \(\Psi^{L_T}_{4,E}\geq\Psi^{\rm rf}_{4,E}\).  Combining with the
Round 10 implication proves (1.10).

For comparison, the exact endpoint identity is

\[
 a_p\Delta+p(E-E_*)
 =(p+a_p)\Delta+2pe_p-pE_*.
\tag{1.16}
\]

Projecting only the \(a_p\Delta\) in (1.15), as done in (1.8), is less
lossy than replacing the whole \(\Delta\) in (1.16): the term \(pE\)
continues to carry the actual shelf curvature gap.

For audit purposes, distinguish this preferred \(E\)-retaining target from
the valid but weaker endpoint-rewritten projection.  Put

\[
 \widetilde M_4:=
 \max\{g(\lambda+e_p),\mathcal K_4\}
\]

and

\[
 \widetilde\Psi^{L_T}_{4,e_p}:=
 \max\{0,L_T\}+(p+a_p)\widetilde M_4+2pe_p-pE_*.
\tag{1.16a}
\]

Equations (1.3), the original Round 21 elasticity inequality, and (1.16)
prove \(\Phi_\delta^+\geq\widetilde\Psi^{L_T}_{4,e_p}\).  Replacing
\(L_T\) by \(T_{\rm rf}\) defines
\(\widetilde\Psi^{\rm rf}_{4,e_p}\).  This projection is genuinely no
stronger than the \(E\)-retaining one.  Indeed, if

\[
 R:=\Delta-g(\lambda+e_p)\geq0,
\]

then \(E=\Delta+2e_p\) and \(\tau=g/(g+2)\) give the exact identity

\[
 \tau(E+2\lambda)=g(\lambda+e_p)+\tau R.
\]

Hence \(M_4\geq\widetilde M_4\), and

\[
 \Psi^{L_T}_{4,E}-\widetilde\Psi^{L_T}_{4,e_p}
 =a_p(M_4-\widetilde M_4)+p(\Delta-\widetilde M_4)\geq0.
\tag{1.16b}
\]

The same comparison holds for the root-free pair.  The diagnostic script
names these quantities `Psi_endpoint_LT` and `Psi_endpoint_rootfree`; it names (1.8)--
(1.9) `Psi4E_LT` and `Psi4E_rootfree`.  No minimum reported for one pair is
attributed to the other.

### 1.4 Equality-face audit

1. **Ordinary shelf-action wall.**  If
   \(A(r+j)+1/4\in\mathbb N\), the ordinary-floor remainder is zero.  In
   particular the allowed lower shelf wall has \(e_p=0\).  Equations
   (0.3), (1.4), (1.15), and (1.16) remain literal; no continuity from the
   open side is used.
2. **Interface sample wall.**  Every first-shelf point satisfies
   \(r+j\leq r+p<\mu\), because \(m\geq1\).  If \(q=\mu\), then
   \(\alpha=0\) and \(J=0\); both (1.7) and the complete \(L_T\) use that
   endpoint value.
3. **Outer support wall.**  A first-shelf point cannot equal \(K\), since it
   lies below \(\mu<K\).  If a terminal sample equals \(K\), its strict
   bracket is zero and Round 10's definition of \(L_T\) owns the wall.
4. **Integral interface wall.**  If \(\mu-r\in\mathbb N\), then
   \(\alpha=0\) and \(q=\mu\); this is the zero-cap case just audited.
5. **Inverse spatial wall.**  If an inverse displacement \(y_k\) is an
   integer, Round 10 uses \(\eta_k=1\), not zero.  The bad adjacent face is
   the one-sided limit \(y_k\downarrow j^+\), where \(\eta_k\downarrow0\).
6. **Terminal-action wall.**  \(B_0=[W+1/4]_<\) is always evaluated with the
   strict bracket.  The top payment (1.6) is literal on both its action
   walls.
7. **Automatic/hard seam.**  Equality \(E=E_*\) belongs to the automatic
   sector.  The hard sector in (0.1) is open at that seam.

### 1.5 Loss ledger

The algebra producing (1.4), (1.15), and (1.16) is exact.  The new losses
are the following.

1. In (1.13), all positive binomial terms beginning with
   \(15u^2/8\) are discarded.  Their double integral is exactly the positive
   gap \(\Delta-\mathcal K_4\).
2. In passing from \(\Delta\) to \(M_4\), the nonnegative term
   \(a_p(\Delta-M_4)\) is discarded.  The actual \(pE\) term is retained.
3. \(\Psi^{L_T}_{4,E}\) discards **nothing further** from the complete
   terminal lower bound: every inverse fraction, the exact cap \(J\), and
   the top interval remain inside \(L_T\).
4. The optional root-free scalar discards
   \(\max\{0,L_T\}-\max\{0,T_{\rm rf}\}\).  It still retains the exact cap
   \(J\); it does not replace it by \(1/8\) or \(1/7\).
5. The earlier Round 10 losses between \(D_A(r)\) and
   \(\Phi_\delta^+\) are unchanged and are not relabelled as lossless here.

This ledger explains why \(\Psi^{L_T}_{4,E}\), rather than a global
compressed intrinsic sign, is the primary next object.

### 1.6 Counterexample search

The diagnostic

`computations/general_d_round28_endpoint_curvature_projection_diagnostic.py`

inherits the Round 27 exact-domain owner/activity predicates and its
ordinary-double-precision action-wall and inverse-spatial-wall sampler.  The
command

```powershell
python -B computations/general_d_round28_endpoint_curvature_projection_diagnostic.py `
  --limit 15 --random 2000 --wall-limit 60 --order 1
```

retained 13,400 feasible hard-sector tuples and 111,260 evaluations on both
parity grids.  Structured radii extend to 10,000; the mixed log-scale sample
extends to \(r=10^6\), \(p=1000\), and \(m=200\).  It found no negative
value of \(\Phi_\delta^+\), \(\Psi^{L_T}_{4,E}\), or
\(\Psi^{\rm rf}_{4,E}\).

The smallest sampled complete-terminal projection was

\[
 \Psi^{L_T}_{4,E}\approx0.8792940016
\tag{1.17}
\]

at

\[
 (r,p,m,f,\alpha)=(1,2,2,2,0),
\]

on the bad side of the first inverse spatial wall \(y_1\downarrow2^+\).
For comparison only, the endpoint-rewritten scalar
\(\widetilde\Psi^{L_T}_{4,e_p}\) had sampled minimum
\(0.8771026922\ldots\) at the same face.  The preferred margin in (1.17)
belongs to \(\Psi^{L_T}_{4,E}\), not to that endpoint projection.

All sampled sharp records were curvature-owned.  Among 39,960
elasticity-owned evaluations, the minima were approximately

\[
 \Psi^{L_T}_{4,E}>5.12,
 \qquad \Psi^{\rm rf}_{4,E}>2.35.
\tag{1.18}
\]

Thus the diagnostic supports a curvature-first proof while reserving the
full \(\max\{0,L_T\}\), exactly as (1.8) does.

The high-precision bad-side limiting face is defined intrinsically by

\[
 G_{K_0}(7)=\frac34,\qquad
 K_0=11.0492679850480\ldots,\qquad
 \mu=q=5.
\tag{1.19}
\]

On its right side, \(\eta_1\downarrow0\), and the diagnostic gives

\[
 L_T\longrightarrow1.19566024149\ldots,\qquad
 \mathcal K_4\longrightarrow0.14711668707\ldots,
\]

\[
 \Psi^{L_T}_{4,E}\longrightarrow0.87929282904\ldots.
\tag{1.20}
\]

The stronger root-free reduction has a different sampled infimum candidate:

\[
 (r,p,m,f,\alpha)=(1,3,2,2,1^-),
\]

on the allowed lower shelf wall \(e_p=0\).  There

\[
 \Psi^{\rm rf}_{4,E}\longrightarrow0.07997036574\ldots.
\tag{1.21}
\]

The endpoint-rewritten root-free projection tends instead to
\(0.07667765667\ldots\).  Equation (1.21) is specifically the
\(E\)-retaining scalar (1.9).

These are diagnostic margins only.  The scan has no continuum coverage and
is not used in the proof of (1.10).

As mandatory regressions, the program also replays the two known feasible
compressed-scalar witnesses.  The Round 27 \(\mathcal R_J\)-negative tuple
has

\[
 E=1.0018247806\ldots>E_*=0.4859466550\ldots,
\]

and the Round 26b \(\mathcal C_8\)-negative tuple has

\[
 E=1.0019646037\ldots>E_*=0.4109058789\ldots.
\]

Both are therefore in the already proved automatic sector, not in (0.1).
At them the diagnostic values of \(\Psi^{L_T}_{4,E}\) are respectively
about \(40.79\) and \(81.08\).  Thus neither rejected global sign is being
reintroduced under a new name.

The installed Mathematica 15 kernel independently simplifies the endpoint
identity, the elasticity rearrangement, and the projection-ordering identity
to zero and prints

\[
 (1-u)^{-3/2}=1+\frac32u+\frac{15}{8}u^2+\frac{35}{16}u^3+\cdots.
\]

The replay is

`computations/general_d_round28_symbolic_projection_check.wl`.

### 1.7 Failure report

No counterexample was found, but no continuum sign proof was obtained.  The
sharpest new sufficient residual is

\[
\boxed{
 \max\{0,L_T\}
 +a_p\max\{\tau(E+2\lambda),\mathcal K_4\}
 \geq p(E_*-E)}
\tag{1.22}
\]

on the exact hard sector.  This is strictly less lossy than projecting
\(E\) and \(\Delta\) simultaneously to a single wall or curvature scalar.
It also retains the complete terminal reserve requested by the revised
strategy.

The observed extremal pattern for (1.22) is not a ratio endpoint.  It is the
intrinsic simultaneous face

\[
 \alpha=0,\qquad y_1\downarrow2^+,
 \qquad (r,p,m,f)=(1,2,2,2),
\tag{1.23}
\]

with the curvature member of (1.5) active.  The obstruction is now a
continuum cell-minimum theorem for the complete fractional terminal
expression, not a lack of numerical margin.

## 2. Concrete next lemma: complete-terminal cell-to-wall reduction

### 2.1 Statement

The next lemma to prove is the following intrinsic statement.

> **Complete-terminal cell-to-wall target.**  On every exact hard-sector
> terminal cell, the scalar \(\Psi^{L_T}_{4,E}\) in (1.8) has no
> nonpositive interior minimum.  Every nonpositive infimum therefore moves
> to a literal action wall, an interface endpoint, or the bad side of one
> inverse spatial wall.  On each such face, the exact wall equation together
> with the shelf and activity relations makes \(\Psi^{L_T}_{4,E}>0\).

This target uses intrinsic terminal cells and the curvature/elasticity
maximum (1.5).  It introduces no ratio threshold.

### 2.2 Dependencies

The intended dependencies are Proposition 1, the exact formulas for
\(L_T\), the exact shelf/activity domain, and elementary implicit
differentiation of inverse levels.  Fixed-\(x\) shelf convexity may be used
after the terminal-cell calculation, but no \(\mathcal C_8\) sign or
certificate is a premise.

### 2.3 Proof

Open.  A proof must differentiate the **complete** expression

\[
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 +2\sum_{k=1}^{B}\eta_k-Q-J
 +\frac{(v-B)_+^2}{\beta}
 +a_pM_4+p(E-E_*)
\tag{2.1}
\]

on each literal terminal cell.  The required missing step is a sign or
convexity argument showing that a nonpositive stationary point cannot occur.
No numerical derivative bound has been promoted to this proof.

### 2.4 Equality-face audit

The target must treat the literal inverse wall \(\eta_k=1\) and its bad
right side \(\eta_k\downarrow0\) separately.  It must also include
\(\alpha=0\), exclude \(\alpha=1\), retain ordinary ownership at
\(e_p=0\), use strict ownership for \(B,Q,B_0\), and assign
\(E=E_*\) to the automatic sector.

### 2.5 Loss ledger

The proposed cell-to-wall lemma is intended to operate on (2.1) exactly.
It may not replace \(J\), discard \(\eta_k\), or replace \(E\) by
\(\mathcal K_4\).  The only existing losses are those already listed in
Section 1.5.

### 2.6 Counterexample search

The 111,260-record search found no nonpositive retained value and placed the
smallest sampled \(\Psi^{L_T}_{4,E}\) at the bad-side inverse wall (1.23).
It did not solve or exhaust all interior stationary equations.  This supports
the target but proves neither its stationary-point nor its face-completeness
assertions.

### 2.7 Failure report

The exact missing calculation is the sign of the cell-stationary value of
(2.1), including the motion of every \(\eta_k\) and \(\theta_k\).  Global
monotonicity in \(\alpha\) is not available and must not be assumed.  If a
genuine negative stationary point is found, the strategy requires returning
to the exact scalar \(\mathscr S\) or the weighted aggregate \(WT\), not
adding a ratio owner or another compressed scalar.

## 3. Gate decision

The analytic CST gate remains open.  The next round should attack the
complete-terminal cell-to-wall target on the curvature branch first, because
all sampled sharp records are curvature-owned and the elasticity-owned
records have a large terminal reserve.  The root-free scalar (1.9) is a
secondary analytic fallback, not the primary compression.

No manuscript rewrite, compact certificate, or theorem promotion is
authorized by this note.  High-floor first-drop CST and the all-dimensional
Pólya theorem remain open.

## 4. Reproduction

```powershell
python -B computations/general_d_round28_endpoint_curvature_projection_diagnostic.py `
  --limit 15 --random 2000 --wall-limit 60 --order 1

& 'C:\Program Files\Wolfram Research\Wolfram\15.0\math.exe' `
  -script computations/general_d_round28_symbolic_projection_check.wl
```

Both programs label their numerical or symbolic output diagnostic-only.  The
analytic proof of Proposition 1 is printed in full above.
