# General dimension, Round 37: independent audit

Date: 19 July 2026  
Status: **PASS** for the stated analytic reductions; the residual gap sign,
high-floor CST, and the all-dimensional theorem remain open

## 0. Scope and verdict

This audit independently checked the current versions of

- `human/outbox/general-d-round-37-gap-interface-synchronization-and-root-free-gate.md`;
- `computations/general_d_round37_gap_interface_replay.wl`;
- `computations/general_d_round37_gap_rootfree_diagnostic.py`.

The source follows
`human/inbox/general-d_simplified_analytic_strategy.md`: it introduces no
ratio ladder, count-indexed theorem family, or new compact certificate.  Its
primary result is the lossless normal form for the already selected
Round28--36 one-level-gap scalar.  The count-free
\(\mathcal H_\Delta\) inequality is correctly presented only as a
sufficient gate.

The proof is correct within its stated scope.  In particular:

1. the strict-floor argument really forces \(B_0=B-1=Q\);
2. the possible hard branch \(B_0=0\) is excluded analytically, not
   diagnostically;
3. the terminal top interval is exactly zero on the gap;
4. the \(\Omega/\Xi\) representation is lossless for
   \(\Gamma_{\mathrm{gap}}\);
5. all three shelf payments used in \(\mathcal H_\Delta\) are valid
   correlated lower bounds before their maximum is taken;
6. the failure inequalities (9.2)--(9.4) have the claimed implication
   direction.

No sign proof for the remaining continuum face is contained in this round.

## 1. Proof audit

### 1.1 Interface-count synchronization

On a literal gap point, \(\alpha>0\), hence \(q<\mu\).  Strict decrease of
the shell action gives

\[
 W=A(\mu)<A(q),
\]

so monotonicity of the strict bracket yields

\[
 B_0\leq Q=B-1.
\]

Also

\[
 v-W=\int_q^\mu\frac1\pi\arccos\frac zK\,dz
\]

lies strictly between zero and \(\alpha/2<1\).  Strict integer brackets of
two real numbers separated by less than one differ by at most one, so
\(B-B_0\leq1\).  Combining the two inequalities gives exactly

\[
 \boxed{B_0=B-1=Q.}
\]

Substitution in \(B_0=[f-\lambda]_<\), with literal ownership at an
integer, gives

\[
 j=f-B=\lfloor\lambda\rfloor,
 \qquad j\leq\lambda<j+1.
\]

There is no continuity substitution at a strict action wall.

### 1.2 Newest inverse level and the top interval

The count \(Q=B-1\) implies \(A(q)\leq B-1/4\), while
\(A(q)>W\) and the outer count gives \(v>B-1/4\).  Strict decrease of
\(G_K\) therefore puts the newest level root strictly between \(q\) and
\(\mu\) at every literal gap point and on the \(Q\)-, inverse-, and
upper-alpha faces:

\[
 0<y_B<\alpha<1,
 \qquad \eta_B=y_B.
\]

On the outer-\(B\) closure the allowed boundary value is \(y_B=0\), and
on the collapsed \(\alpha\downarrow0\) gap-side limit one has
\(y_B,\eta_B\to0\).  The current theorem statement explicitly weakens the
strict assertion at exactly these two closures.

Round36 gives \(0<h<1/4\).  Hence

\[
 v=A(q)+h<B,
\]

so \((v-B)_+^2/\beta=0\) identically.  The top term is not discarded.

For \(k\leq B_0\), strict counting gives
\(k-1/4<W=G_K(\mu)\), hence \(\theta_k<t\).  For \(k>B_0\), one still
has \(0<\theta_k<\pi/2\).  Consequently every displayed summand in
\(\Omega\) is positive on the open face, and the adverse one-sided inverse
limits remain nonnegative in their fractional part while retaining a
strict angle contribution.  Adding and subtracting \(\pi/(2t)\) for
exactly the first \(B_0\) levels proves

\[
 \sum_{k=1}^B
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 =\frac{B_0d}{2c}+\Omega.
\]

### 1.3 Exclusion of \(B_0=0\)

If a hard gap had \(B_0=0\), synchronization would give
\((B,Q)=(1,0)\).  Literal strict ownership permits
\(A(q)=3/4\), so the correct relations are

\[
 W<A(q)\leq\frac34,
 \qquad
 A(r+p)-A(q)\geq f-1+e_p\geq1.
\]

These are precisely the two consequences of the syntactically stated
lower-\(Q\) wall used in the Round34 normalized-domain derivation.  The
common-radial-parameter identity and the strict trapezoid upper bound give
the same lower scale estimate, while \(W<3/4\) gives the same upper scale
estimate.  Thus the tuple satisfies every condition of Round34 domain
(3.16), and the Jensen lower quadrature gives

\[
 \Delta>C(z,P,M,t).
\]

Here \(z,P,M>0\), \(z+P+M=q/\mu<1\), and hard-sector feasibility gives
\(P>dM\).  Round34 transport and every phase module in Round35 depend only
on this normalized domain, not on the equality \(A(q)=3/4\).  Therefore

\[
 C>E_*,\qquad \Delta>E_*.
\]

Since \(E-\Delta=2e_p\geq0\), this contradicts \(E<E_*\).  The scope
extension is therefore valid and proves

\[
 \boxed{B_0=Q\geq1,\qquad B\geq2}
\]

throughout the hard gap.  The source correctly avoids the notation clash
between Round34's \(\cos t\) and the present \(c=t/\pi\).

### 1.4 Lossless shelf normal form

Round28 proves simultaneously

\[
 \Delta\geq\tau(E+2\lambda),
 \qquad \Delta>\mathcal K_4.
\]

Thus \(\Delta\geq M_4\).  Together with
\(E-\Delta=2e_p\geq0\), this gives

\[
 \Xi=E-M_4\geq0
\]

and the exact identity

\[
 a_pM_4+pE=(p+a_p)M_4+p\Xi.
\]

Moreover, \(E\geq M_4\) and
\(M_4\geq\tau(E+2\lambda)\) imply

\[
 M_4\geq\tau(M_4+2\lambda),
\]

which is equivalent to \(M_4\geq(\mathfrak s-1)\lambda\).  Hence

\[
 M_4\geq\max\{(\mathfrak s-1)\lambda,\mathcal K_4\}.
\]

Combining this shelf identity with the exact inverse decomposition and the
zero top term proves (0.16) without loss.  Since \(J<1/7\) and
\(\Omega>0\), \(L_T>6/7\); the clipping is therefore literally inactive.
The implication chain to \(D_A(r)\) has the correct direction.

### 1.5 The \(\mathcal H_\Delta\) max-gate

Starting from the stronger endpoint scalar, the exact identity

\[
 \Phi_\delta^+
 =1-J+\Omega+
 \{B_0\zeta+(p+a_p)\Delta\}
 +2pe_p-\frac{p-dm}{2}
\]

is correct.  Each proposed payment is a lower bound for the single
expression in braces:

1. **Elasticity.**  With \(n=f-1\),
   \(j=\lfloor\lambda\rfloor\), and
   \(B_0=n-j\), the exact bound
   \(\Delta\geq(\mathfrak s-1)(\lambda+e_p)\) gives
   \(\mathcal S_{\mathrm{el}}\) by the elementary two-slope minimum
   identity.
2. **Quartic curvature.**  The proved \(B_0\geq1\) and strict
   \(\Delta>\mathcal K_4\) give
   \(\mathcal S_{\mathrm{curv}}\).
3. **Adjacent action.**  Writing
   \(\xi=A(q)+1/4-Q\in(0,1]\) gives
   \(A(r+p)-A(q)\geq j+e_p\).  The Round34 weighted radial identity
   yields \(\Delta>R_1\{A(r+p)-A(q)\}\), and the same minimum identity
   gives \(\mathcal S_{\mathrm{adj}}\).

Because \(\Omega>0\), the correlated expression is strictly larger than
the maximum of these three valid lower bounds.  This proves
\(\Phi_\delta^+>\mathcal H_\Delta\).  No inference assumes that the three
payments hold on disjoint chambers.

### 1.6 Failure inequalities

Equation (9.2) is the direct rearrangement of the lossless normal form for
a hypothetical \(\Gamma_{\mathrm{gap}}\leq0\).  Replacing
\(2(1-J)\) by the strictly smaller \(12/7\) gives the strict necessary
condition (9.3).  Equation (9.4) is the exact strict failure condition for
the sufficient \(\mathcal H_\Delta\) gate.  At
\(\mathcal H_\Delta=0\), the strict inequality
\(\Phi_\delta^+>\mathcal H_\Delta\) already closes the point, exactly as
the current source states.

## 2. Equality-face audit

The source assigns every relevant strict wall consistently.

1. At an ordinary shelf wall the ordinary-floor remainder is literal and
   nonnegative, including \(e_p=0\).
2. The literal condition \(\mu-r\in\mathbb Z\) is \(\alpha=0\), where
   \(h=0\) and no gap point exists.
3. The limit \(\alpha\uparrow1^-\) is a separate one-sided reindex limit,
   not the literal \(\alpha=0\) point of the next chart.
4. At an outer \(B_N\) wall, the theorem uses the one-sided gap label;
   the new \(y_B\downarrow0\) is not charged as an old inverse jump.
5. At a \(Q_N\) wall, the literal owner is \(Q=N-1\); its phase-right
   equal-count side is excluded.
6. At an old inverse wall, the literal value is \(\eta_k=1\) and the
   adverse side is \(\eta_k\downarrow0\); both occur explicitly in
   \(\Omega\).
7. A first-shelf point at \(K\) cannot carry \(f\geq2\), and a terminal
   point at \(K\) cannot carry a positive inverse level.
8. At an integer \(\lambda\), \(\{\lambda\}=0\) and the literal lower
   \(B_0\) are used.  On the opposite one-sided limit the fractional part
   tends to one while \(B_0\) is higher.
9. The hard wall \(p=dm\) remains in the automatic sector.  The current
   live gap has \(p-dm>12/7\).
10. At the collapsed \(\alpha\downarrow0\) gap-side limit,
    \(B_0=Q=B-1\); the literal simultaneous corner is equal-count and is
    not claimed here.

## 3. Loss audit

The identity (0.16) is lossless relative to the selected Round28 gap
scalar.  It retains the exact cap, every complete angle and inverse
fraction, \(M_4\), and the full excess \(E-M_4\).  Its only inherited
losses are those already present between the exact shifted tail and the
Round28 selected scalar.

The optional \(\mathcal H_\Delta\) gate starts from the stronger
\(\Phi_\delta^+\).  It discards \(\Omega\) only after constructing three
correlated shelf payments and replaces their common source by their
maximum.  It retains \(e_p\), \(\{\lambda\}\), the quartic alternative,
and \(J\).  No replacement \(J\mapsto1/7\) occurs in the primary gate.

These losses are correctly reported as losses of a sufficient reduction,
not as losses proved harmless for the unresolved sign.

## 4. Exact replay

The installed Mathematica kernel was run with

```powershell
& 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' `
  -file computations/general_d_round37_gap_interface_replay.wl
```

and returned

```text
angleIdentity=True
elasticSolveIdentity=True
tauEndpointIdentity=True
shelfProjectionIdentity=True
hardRewriteIdentity=True
actionDeficitIdentity=True
xiShelfIdentity=True
inverseNormalFormIdentity=True
gammaNormalFormIdentity=True
sawtoothIdentity=True
sawtoothUpperBranch=True
sawtoothLowerBranch=True
terminalRemainderIdentity=True
phiEndpointIdentity=True
failureIdentity=True
round37GapInterfaceReplayOK=True
```

This is an exact algebraic replay.  It is not a sign certificate and does
not replace the printed strict-floor or radial-parameter proofs.

## 5. Diagnostic-only counterexample search

The broadened finite search was run with

```powershell
python -B computations/general_d_round37_gap_rootfree_diagnostic.py `
  --limit 10 --random 500 --wall-limit 50
```

It retained 5,191 residual-gap evaluations and printed

```text
min F_J=0.18341669989839
min F_7=0.125826990904636
min actual_projection=1.843398101707
min H_Delta=0.952564418267364
min Phi_delta_plus=1.84388318733303
nonpositive counts: F_J=0 F_7=0 actual=0 H_Delta=0 Phi=0
B0ZeroCount=0
round37InterfaceSynchronizationOK=True
scanCertification=diagnostic_only
```

The sample includes both parity grids, action and inverse walls inherited
from the Round27 sampler, \(\alpha\) down to \(10^{-6}\),
\(\alpha\uparrow1^-\), and radii through \(10^8\).  Ordinary floating-point
sampling has no continuum coverage, directed-rounding guarantee, or finite
coverage proof.  Therefore none of these positive values is a theorem
premise.  In particular, `B0ZeroCount=0` is only a regression check; the
analytic proof of Proposition 0.2 is load-bearing.

The diagnostic robustness path was also checked.  It evaluates \(R_1\) by
rationalizing both square-root differences,

\[
 R_1=
 \frac{(x^2-r^2)(U_x+U_q)}{(q^2-x^2)(U_r+U_x)},
\]

which is algebraically identical to (0.20) and is stable at large radius.
It then explicitly verifies that the common exact shelf source
\(B_0\zeta+(p+a_p)\Delta\) dominates each of
\(\mathcal S_{\mathrm{el}}\), \(\mathcal S_{\mathrm{curv}}\), and
\(\mathcal S_{\mathrm{adj}}\) before checking their maximum against
\(\Phi_\delta^+\).  These are diagnostic regression assertions, not new
proof premises.

The source and both scripts were also checked for embedded carriage returns,
control bytes, and tab characters; none was present.

## 6. Theorem boundary

Round37 proves synchronization, the positive-interface-count reduction, the
lossless selected-scalar normal form, and the count-free sufficient gate.
It does **not** prove

\[
 \Gamma_{\mathrm{gap}}>0,
 \qquad \Phi_\delta^+\geq0,
 \qquad D_A(r)\geq0
\]

on the complete residual gap continuum.  Consequently the residual
one-level-gap branch, the other Round36 face classes, high-floor CST,
pointwise assembly, the weighted aggregate, and the all-dimensional
Pólya theorem all remain open.
