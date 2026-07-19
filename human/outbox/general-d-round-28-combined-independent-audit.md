# General dimension, Round 28: combined independent audit

Date: 19 July 2026  
Auditor: independent Round 28 replay and theorem audit  
Status: **analytic reductions pass; continuum sign and theorem promotion remain open**

## 0. Audit verdict

The two Round 28 analytic contributions survive independent checking:

1. the exact-remainder quartic-curvature projection
   
   \[
   D_A(r)\geq\Phi_\delta^+
   \geq\Psi^{L_T}_{4,E}
   \geq\Psi^{\rm rf}_{4,E}
   \]

   is valid on the stated exact hard sector; and
2. the Cmax hard-gap transport and finite branch-candidate reductions are
   valid on their stated fixed-tuple phase cells.

No blocking algebraic, analytic, wall-ownership, or theorem-scope defect was
found in those proved statements.  In particular, the preferred target is
the actual-\(E\), complete-terminal scalar

\[
 \boxed{
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_p\max\{\tau(E+2\lambda),\mathcal K_4\}
  +p(E-E_*) .}
\tag{0.1}
\]

The root-free scalar and the conditional \(\mathcal C_{\max,8}\) analysis
are secondary only.  Neither is promoted over (0.1).

The theorem gate nevertheless remains **blocked** for the reason stated by
the authors: no continuum proof of
\(\Psi^{L_T}_{4,E}\geq0\),
\(\Psi^{\rm rf}_{4,E}\geq0\), or the conditional
\(\mathcal C_{\max,8}\geq0\) has been obtained.  Therefore this audit does
not authorize promotion of high-floor CST or of the all-dimensional Pólya
theorem.

## 1. Frozen audit objects

The final hashes checked were:

| Artifact | SHA-256 |
|---|---|
| `human/outbox/general-d-round-28-exact-remainder-quartic-curvature-projection-and-hard-face.md` | `4276bff1f182f46ffa4e25d9d7d46582659cd44ad8d264ddedc954b88a0cb027` |
| `computations/general_d_round28_endpoint_curvature_projection_diagnostic.py` | `08d21a0eb340c72c668d0a01b185091e6943339c13e5bc25fd9c9b5b4c443d9e` |
| `computations/general_d_round28_symbolic_projection_check.wl` | `83e931279afb26f3a2056f22c72312504aa929f48658a5883ee5002152a4467d` |
| `human/outbox/general-d-round-28-hard-sector-Cmax-branch-reduction-and-failure-report.md` | `10a213d16e846ac6d912a1777df0d43dd9735abca7f4ae1a2445b29180d5bf21` |
| `computations/general_d_round28_hard_sector_cmax_branch_diagnostic.py` | `d88631fad0d7adacad5acd1a1f9f06a3fe13bf92a1f626fee37175dd4a5078e7` |

The Cmax note also relies on a sixth replay which was not in the original
five-file audit list:

| Additional replay | SHA-256 |
|---|---|
| `computations/general_d_round28_cmax_branch_derivatives.wl` | `d6677ff598d7b26a0efa9cffd8c5c9abf62abbde268a96ca7e0dd448ec32746d` |

The hashes were rechecked after all executions and remained unchanged.

## 2. Exact-remainder projection audit

### 2.1 Domain and signs

On the hard sector

\[
 p>dm,
 \qquad
 0\leq E<E_*:=\frac12-\frac{dm}{2p}<\frac12,
\]

one has \(a_p>0\), \(g>0\), \(\tau=g/(g+2)>0\),
\(\lambda>0\), \(K>\mu\), and
\(0<r<r+p<\mu\).  These are exactly the signs used when inequalities are
multiplied, integrated, or maximized.  No hidden ratio or numerical
hypothesis enters the proof.

### 2.2 Elasticity rearrangement

The imported shelf elasticity is

\[
 \Delta\geq g(\lambda+e_p),
 \qquad
 e_p=\frac{E-\Delta}{2}.
\]

Substitution gives

\[
 \left(1+\frac g2\right)\Delta
 \geq g\left(\lambda+\frac E2\right).
\]

Division by \(1+g/2>0\) is legitimate and yields exactly

\[
 \Delta\geq\frac{g}{g+2}(E+2\lambda)
 =\tau(E+2\lambda).
\tag{2.1}
\]

This derivation really retains the actual \(E\); it does not substitute a
lower wall value for it.

### 2.3 Quartic curvature payment

With \(\sigma=-A'\), direct differentiation gives

\[
 \sigma'(z)=\frac1\pi\int_\mu^K
 a^{-2}\left(1-\frac{z^2}{a^2}\right)^{-3/2}\,da.
\]

For \(0\leq z<\mu\leq a\),

\[
 (1-u)^{-3/2}\geq1+\frac32u.
\]

Consequently

\[
 \sigma'(z)\geq\frac1\pi\left[
 (\mu^{-1}-K^{-1})
 +\frac{z^2}{2}(\mu^{-3}-K^{-3})\right].
\]

Integrating from \(0\) to \(z\), and then from \(r\) to \(r+p\), gives

\[
 \Delta\geq
 \frac{(\mu^{-1}-K^{-1})((r+p)^2-r^2)}{2\pi}
 +\frac{(\mu^{-3}-K^{-3})((r+p)^4-r^4)}{24\pi}
 =\mathcal K_4.
\tag{2.2}
\]

The strict sign in the source note is also correct.  The next binomial
coefficient is positive, \(K>\mu\), and the double integration includes a
positive-measure region with \(z>0\).  Thus
\(\Delta>\mathcal K_4\).

The quadratic member is exactly the earlier curvature term because

\[
 \mu^{-1}-K^{-1}=\frac{1-\cos t}{\mu},
 \qquad
 (r+p)^2-r^2=p(2r+p).
\]

### 2.4 Projection chain

Equations (2.1)--(2.2) imply

\[
 \Delta\geq
 M_4:=\max\{\tau(E+2\lambda),\mathcal K_4\}.
\]

The exact Round 27 lower scalar is

\[
 \Phi_\delta^+
 =\max\{0,L_T\}+a_p\Delta+p(E-E_*).
\]

Since \(a_p>0\), replacing only the displayed \(a_p\Delta\) gives

\[
 \Phi_\delta^+\geq\Psi^{L_T}_{4,E}.
\]

The exact pre-\(J<1/7\) terminal argument also gives

\[
 L_T>
 T_{\rm rf}:=\frac{B_0d}{2c}-J+\mathcal P(\lambda).
\]

This follows directly from the complete-level proof: levels above \(B_0\)
pay at least one, while on the \(B=B_0\) face the top interval pays the
displayed capped quadratic amount.  The fractional inverse payments are
nonnegative and need not be discarded from \(L_T\) itself.  Monotonicity of
\(x\mapsto\max\{0,x\}\) therefore proves

\[
 \Psi^{L_T}_{4,E}\geq\Psi^{\rm rf}_{4,E}.
\]

Together with the imported Round 10 inequality this verifies the complete
chain in the source note.

### 2.5 Ordering against the endpoint-rewritten auxiliary

The endpoint identity is exact:

\[
 a_p\Delta+p(E-E_*)
 =(p+a_p)\Delta+2pe_p-pE_*.
\]

Writing

\[
 R=\Delta-g(\lambda+e_p)\geq0
\]

gives

\[
 \tau(E+2\lambda)
 =g(\lambda+e_p)+\tau R.
\]

Hence \(M_4\geq\widetilde M_4\), and

\[
 \Psi^{L_T}_{4,E}-\widetilde\Psi^{L_T}_{4,e_p}
 =a_p(M_4-\widetilde M_4)+p(\Delta-\widetilde M_4)\geq0.
\]

Thus the source note correctly treats the actual-\(E\) projection as the
stronger and primary target.  The diagnostic labels for the two projections
also agree with the definitions.

## 3. Cmax branch-reduction audit

### 3.1 Hard-gap transport

For a fixed discrete/interface tuple,

\[
 \partial_tA_t(z)=
 \frac{\mu\sin t}{\pi\cos^2t}
 \sqrt{1-\left(\frac{z\cos t}{\mu}\right)^2}.
\]

Both shelf endpoints lie strictly below \(\mu\), so each square root is
strictly larger than \(\sin t\).  Therefore

\[
 E'(t)>2W'(t),
 \qquad
 W'(t)=\frac\mu\pi\tan^2t.
\]

The strict owner activity condition implies

\[
 \mu>\frac{\pi\cos t}{1-\cos t},
 \qquad
 W'(t)>1+\sec t.
\]

If \(\varepsilon=\pi/2-t\), then
\(\cos t=\sin\varepsilon<\varepsilon<2\varepsilon=\pi d\).
Thus \(\sec t>1/(\pi d)\).  On \(p>dm\),

\[
 E_*'(t)=\frac m{p\pi}<\frac1{\pi d}<\sec t.
\]

It follows that

\[
 H'(t)=E'(t)-E_*'(t)
 >2(1+\sec t)-\frac m{p\pi}>0.
\]

At \(p=dm\), \(E_*=0\) and the shelf gives \(E\geq0\), so a hard interval
cannot begin after that seam.  Proposition 2.1 and the initial-interval
orientation are therefore correct.

### 3.2 Maximum switch and branch derivatives

On a cell with fixed \(B_0\) and fixed top-payment formula, let
\(M=p+a_p\).  The switch function satisfies

\[
 F'(t)=-gW'(t)-k\sin t<0,
\]

so there is at most one elasticity/curvature switch.

On the quadratic top cell, with
\(u=W-(f-1)\in(0,1/\sqrt2)\), direct differentiation gives

\[
 \mathcal C_{\rm curv}'
 =Mk\sin t-\frac m\pi-\frac{B_0\pi}{2t^2}+4uW',
\]

\[
 \mathcal C_{\rm curv}''
 =Mk\cos t+\frac{B_0\pi}{t^3}
 +4\{(W')^2+uW''\}>0.
\]

Off the quadratic cell, the last bracket is absent but
\(Mk\cos t>0\), so strict convexity remains.

For the elasticity branch, the derivative on a constant top-payment cell is

\[
 \mathcal C_{\rm el}'
 =-MgW'-\frac m\pi-\frac{B_0\pi}{2t^2}<0.
\]

On the quadratic cell,

\[
 \mathcal C_{\rm el}'
 =(4u-Mg)W'-\frac m\pi-\frac{B_0\pi}{2t^2},
\]

\[
 \mathcal C_{\rm el}''
 =4(W')^2+(4u-Mg)W''+\frac{B_0\pi}{t^3}.
\]

While \(4u-Mg\leq0\), the first derivative is negative.  Once that
coefficient is positive, every term in the second derivative is positive.
The derivative can therefore vanish at most once, and any zero is a strict
minimum.  This validates the finite candidate list after including all cell
walls, the unique maximum switch, and the possible stationary points.

### 3.3 Exact shelf rewrite and auxiliary gates

Since \(A_t(\mu)=W\) and \(-A_t'=\sigma_t\),

\[
 A_t(y)=W+\int_y^\mu\sigma_t(z)\,dz.
\]

The shelf inequalities and endpoint remainders therefore become exactly
the three integral constraints and the two identities printed in the Cmax
note.  In particular,

\[
 E=\mathscr I_t(r)+\mathscr I_t(x)-2\lambda,
\]

so the hard inequality has not been decorrelated.

The implication

\[
 \mathcal T:=B_0Z-pE_*-\frac18\geq0
 \quad\Longrightarrow\quad
 \mathcal C_{\max,8}\geq0
\]

is valid because the omitted maximum and top payment are nonnegative.
The proposed elasticity implication and the curvature candidate inequality
remain explicitly unproved.  They are sufficient auxiliary Cmax gates, not
the primary Round 28 target.

## 4. Strict-wall and equality audit

The wall conventions are mutually consistent.

| Face | Ownership checked | Audit result |
|---|---|---|
| Ordinary lower shelf \(A_t(r+p)=f-1/4\) | ordinary floor owns equality, so \(e_p=0\) | pass |
| First-drop and shelf-start walls | equalities are excluded and used only as one-sided phase endpoints | pass |
| \(\alpha=0\), hence \(q=\mu\) | \(J=0\), while the ordinary interface count is unchanged | pass |
| \(\alpha=1\) | excluded; limiting diagnostics are labelled \(1^-\) | pass |
| Shelf sample at outer support | impossible because \(r+j\leq r+p<\mu<K\) | pass |
| Terminal sample at outer support | strict bracket is zero and the complete \(L_T\) formula owns the wall | pass |
| Inverse wall \(y_k=j\) | strict floor gives \(\eta_k=1\); the right limit has \(\eta_k\downarrow0\) | pass |
| Terminal action wall \(W+1/4\in\mathbb Z\) | strict bracket has the lower \(B_0\); immediately right, \(B_0\) rises by one and Cmax jumps upward by \(Z>0\) | pass |
| Top-payment seams | quadratic/saturated/zero formulas agree at their included seams; \(\lambda=0\) is excluded by first drop | pass |
| Hard seam \(E=E_*\) | assigned to the already proved automatic sector | pass |
| Seam \(p=dm\) | \(E_*=0\) and \(E\geq0\), hence automatic | pass |
| Maximum switch | both branch values agree; derivative continuity is not assumed | pass |

No open-side limit is substituted for a literal strict-floor value in either
analytic proof.

## 5. Strategy and theorem-scope audit

The revised strategy requires the complete fractional terminal reserve and
the exact shelf/terminal correlation to remain primary.  The frozen Round 28
artifacts comply:

1. \(\Psi^{L_T}_{4,E}\) retains every inverse fraction, \(J\), the top
   interval, and the actual \(E\).
2. \(\Psi^{\rm rf}_{4,E}\) is explicitly called a secondary fallback.
3. The endpoint-rewritten \(\widetilde\Psi\) is distinguished by notation
   and is proved no stronger than the actual-\(E\) scalar.
4. The Cmax note now explicitly restates (0.1) as the primary target and
   leaves its own two gates auxiliary/open.
5. No ratio ladder, empirical constant, or compact certificate is introduced.
6. The failure reports route a failed pointwise target back to the exact
   scalar, \(\mathscr S\), or the weighted aggregate.

The scope statements are therefore correct: Round 28 proves useful lower
reductions, not the sign needed for high-floor CST.

## 6. Fresh reproduction

The audit environment was Python 3.14.4 and Mathematica 15.0.0 for Windows.

### 6.1 Exact-remainder diagnostic

The published command

```powershell
python -B computations/general_d_round28_endpoint_curvature_projection_diagnostic.py `
  --limit 15 --random 2000 --wall-limit 60 --order 1
```

exited zero and reproduced:

- 13,400 feasible hard-sector tuples;
- 111,260 retained evaluations;
- zero negatives for \(\Phi_\delta^+\),
  \(\Psi^{L_T}_{4,E}\), and \(\Psi^{\rm rf}_{4,E}\);
- minimum sampled \(\Psi^{L_T}_{4,E}=0.879294001646920\);
- minimum sampled \(\Psi^{\rm rf}_{4,E}=0.0799707244796041\);
- 39,960 elasticity-owned evaluations, with sampled minima
  \(5.12257987218484\) and \(2.35361666325821\);
- maximum endpoint-identity residual \(1.13687\times10^{-13}\).

The two 90-digit limiting faces reproduced the values printed in the note,
including

\[
 \Psi^{L_T}_{4,E}\to0.8792928290406447\ldots
\]

at \((r,p,m,f,\alpha)=(1,2,2,2,0)\), \(y_1\downarrow2^+\), and

\[
 \Psi^{\rm rf}_{4,E}\to0.0799703657451101\ldots
\]

at \((1,3,2,2,1^-)\) on the lower shelf wall.

The two rejected compressed-scalar witnesses also reproduced as automatic:

\[
 1.00182478065751>0.485946655063032,
 \qquad
 1.0019646037938>0.410905878916475.
\]

### 6.2 Cmax diagnostic

The published command

```powershell
python -B computations/general_d_round28_hard_sector_cmax_branch_diagnostic.py `
  --limit 5 --random 200000 --seed 20260728
```

exited zero and reproduced:

- 34,421 retained hard records;
- 10,543 curvature-owned and 23,878 elasticity-owned records;
- zero negative Cmax records;
- zero negative terminal-only records among retained elasticity records;
- minimum sampled Cmax value \(0.0128644521009431\);
- fixed elasticity ownership margin approximately
  \(4.08\times10^{-4}\);
- fixed elasticity terminal-only margin \(0.285619943909518\).

These are diagnostic counts, not continuum coverage.

### 6.3 Mathematica replays

The published projection replay command exited zero and printed

```text
round28EndpointResidual=0
round28ElasticityResidual=0
round28ProjectionOrderingResidual=0
round28CurvaturePolynomialResidual=0
round28ProjectionReplayOK=True
diagnosticOnly=True
```

The additional Cmax derivative replay

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\math.exe' `
  -script computations/general_d_round28_cmax_branch_derivatives.wl
```

printed

```text
round28DerivativeResiduals={0, 0, 0, 0, 0}
round28DerivativeReplayOK=True
```

and exited zero.

## 7. Findings and required interpretation

### 7.1 Blocking theorem gate

There is one genuine blocker to theorem promotion, already disclosed by both
source notes:

> No continuum sign proof exists for the complete-terminal scalar or for the
> auxiliary conditional Cmax scalar.

Accordingly, the high-floor first-drop CST branch and the general theorem
must remain open.  This is not a defect in the proved lower projections; it
is the next mathematical obligation.

### 7.2 Artifact findings resolved during the audit

The preliminary audit found several nonanalytic reproducibility and wording
issues.  The authors corrected them before the final hashes in Section 1
were frozen, and the changed artifacts were replayed again.

1. **Cmax search scope corrected.**  The Cmax note now says, at lines
   554--556, that the deterministic pass uses a 25-point mesh plus bounded
   local minimization and is not a certified global minimization.  The
   diagnostic docstring says the same.  This matches lines 143--161 of the
   implementation.
2. **Cmax replay documented.**  The Cmax note, lines 358--368, now names
   `general_d_round28_cmax_branch_derivatives.wl`, gives a working
   `math.exe` command, and records its `True` gate.
3. **Automatic witnesses gated.**  The exact-remainder diagnostic, lines
   337--342, now computes the automatic-sector Boolean for each rejected
   compressed-scalar witness and raises an error if either witness leaves that
   sector.
4. **Projection replay gated.**  The projection Wolfram file, lines 34--41,
   now prints `round28ProjectionReplayOK=True` and exits nonzero if one of its
   four algebraic residuals is nonzero.
5. **LaTeX rendering corrected.**  All seven preliminary `,qquad` typos were
   replaced by `,\qquad`; a fresh literal search found none remaining.

One terminology-only observation remains: the Cmax equality audit calls the
immediate right value at a terminal action wall “bad-right,” even though it
correctly proves that Cmax jumps upward there by \(Z>0\).  Both values are
included, so this has no mathematical or diagnostic consequence.

## 8. Gate decision

The Round 28 analytic projection and branch-reduction lemmas may be retained
as proved inputs.  The combined audit is a **pass with no analytic blocker**
for those limited statements.

The promotion decision for high-floor CST is **no**.  The next primary task
is the complete-terminal cell-to-wall or stationary-point theorem for
\(\Psi^{L_T}_{4,E}\).  The root-free and Cmax inequalities remain auxiliary
regression/fallback targets, exactly as required by the revised strategy.
