# General-dimensional spherical-shell Pólya project
## Round 44B clean-room Gate-B reconstruction

**Date:** 20 July 2026  
**Clean-room freeze point:** Sections 1--5 were completed before any lead Round 44 note or other Round 44 artifact was opened.  
**Verdict at the freeze point:** `STRUCTURAL PASS — FINAL SIGN OPEN`

## 1. Protocol, theorem boundary, and exact owner

### 1.1 Sources read before the clean-room freeze

I read the full Round 44 prompt packet and, for mathematical source content in Sections 1--5, exactly the seven sources permitted by Prompt B:

1. `state/proof_obligations.yml` (SHA-256 `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`);
2. `human/inbox/general-d_simplified_analytic_strategy.md`;
3. `human/inbox/general-d-strategy_r2.md`;
4. `human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md`;
5. `human/outbox/general-d-round-38-gap-position-count-phase-and-face-compensation.md`;
6. `human/outbox/general-d-round-42-stronger-upper-alpha-phi-specialization.md`;
7. `human/outbox/general-d-round-43-hard-remainder-isolation-and-gate-a-stop.md`.

No lead Round 44 note, replay, diagnostic, audit, state summary, manuscript file, or other mathematical artifact was read before the end of Section 5.

The selected obligation remains

\[
\texttt{SHELL-general-d-high-floor-first-drop-CST}:\quad\texttt{open}.
\]

Nothing below promotes the general-dimensional theorem or its branching backbone.  The latter remains `derived_under_assumptions` pending its separate frozen audit.

There is one workflow conflict in the allowed sources.  The selected state entry still describes the Round 37 Gate-A next action, whereas the newer Round 43 note proves that the permitted Gate-A continuation would require a forbidden floor/count-indexed wall analysis and explicitly activates Gate B.  Prompt B itself requests the Gate-B reconstruction.  I therefore follow Round 43 for the current route while preserving the authoritative `open` status from state.  The expected state-file hash printed in the strategy and Round 38 note agrees with the file actually read.

There are two notation hazards rather than mathematical conflicts:

- In Round 10, \(B\) denotes the *literal* strict bracket \([v+1/4]_<\).  In Rounds 38, 42, and 43, \(B\) on this face is the *one-sided gap label*.  At the wall these differ by one.  I write \(B_{\rm lit}\) for the former.
- Round 42 writes \(d=1-2t/\pi\).  Here I write \(d_\rho\), reserving an ambient-dimension label \(d_{\rm amb}\) for the activity condition.

### 1.2 Strict-bracket convention

For \(s\ge0\),

\[
[s]_<:=\#\{k\in\mathbb N:k<s\}=\max\{0,\lceil s\rceil-1\}.
\]

Thus \([N]_< =N-1\) at a positive integer \(N\).  If \(y>0\), its strict fractional displacement is

\[
\eta=y-[y]_<\in(0,1],
\]

and \(\eta=1\), not \(0\), on a literal positive-integer spatial wall.

### 1.3 Exact resisting owner

Put

\[
x=r+p,\qquad q=x+m,\qquad \mu=q+1,\qquad
K=\mu\sec t,\qquad 0<t<\frac\pi2,
\]

\[
d_\rho=1-\frac{2t}{\pi},\qquad
\zeta=\frac\pi{2t}-1,
\]

and

\[
G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
\qquad A(z)=G_K(z)-G_\mu(z).
\]

The upper-alpha, outer-\(B\) endpoint is described by

\[
v:=G_K(q)=B-\frac14,\qquad B_0:=B-1\ge1,
\]

\[
h:=G_\mu(q),\qquad
\beta:=\frac1\pi\arccos\frac qK,
\qquad 0<h<u<\beta<\frac12.
\]

The literal outer-ball bracket and the shell terminal count are

\[
\boxed{
B_{\rm lit}=[v+\tfrac14]_<=[B]_< =B-1=B_0,
}
\tag{1.1}
\]

\[
A(q)+\frac14=B-h\in(B-1,B),
\qquad
\boxed{Q=[A(q)+\tfrac14]_< =B-1=B_0.}
\tag{1.2}
\]

Let \(f\) be the common first-shelf floor and \(j=f-B\ge0\).  Retain literally

\[
\left\lfloor A(r)+\frac14\right\rfloor
=\left\lfloor A(x)+\frac14\right\rfloor=f,
\qquad
\left\lfloor A(x+1)+\frac14\right\rfloor\ne f,
\tag{1.3}
\]

and define

\[
e_0=A(r)+\frac14-f,\qquad
e_p=A(x)+\frac14-f,
\]

\[
E=e_0+e_p,\qquad
\Delta=e_0-e_p=A(r)-A(x),
\qquad
a_p=\frac{p^2}{3(2r+p)},
\]

\[
E_*=\frac{p-d_\rho m}{2p}.
\tag{1.4}
\]

The exact hard owner retains

\[
p\ge3,\quad m\ge1,\quad p>d_\rho m,\quad
0\le E<E_*<\frac12,
\tag{1.5}
\]

\[
p-d_\rho m>\frac{11}{5},\qquad q\ge5,
\tag{1.6}
\]

the two grids

\[
r\in\mathbb N,\ r\ge1,
\qquad\hbox{or}\qquad
r\in\mathbb N_0+\frac12,\ r\ge\frac32,
\tag{1.7}
\]

and the dimension-labelled strict activity condition

\[
K^2>
\frac{\pi^2}{(1-\rho)^2}
+\frac{(d_{\rm amb}-2)^2-1}{4},
\qquad
\rho=\frac\mu K,
\qquad
r=\ell+\frac{d_{\rm amb}-2}{2}.
\tag{1.8}
\]

The exact Gate-B scalar is

\[
\boxed{
\mathscr S
=D_A(q)+R_p+\frac{d_\rho m}{2}
=D_A(q)+\mathcal C_p+p(E-E_*).
}
\tag{1.9}
\]

The endpoint geometry may be evaluated exactly at \(\mu=q+1\): all geometric functions and the shell count in (1.2) have a well-defined one-sided limit there.  What must remain one-sided is the chart ownership.  In particular, the label \(B\) is not the literal bracket (1.1), and this endpoint must not be reindexed as the next chart's literal \(\alpha=0\) owner.

## 2. Exact terminal layer cake and the two owner decompositions

### 2.1 Convex inverse and tangent notation

Translate the outer-ball action to

\[
g(s)=G_K(q+s),\qquad 0\le s\le K-q,
\qquad v=g(0)=B_0+\frac34.
\]

Let \(y(a)\) be its strict superlevel length:

\[
y(a)=|\{s\ge0:g(s)>a\}|,
\qquad 0<a<v,
\]

and extend \(y(a)=0\) for \(a\ge v\).  This is the decreasing convex inverse used in Round 10.  For

\[
a_k=k-\frac14,\qquad 1\le k\le B_0,
\]

write

\[
y_k=y(a_k),\qquad
c_k=-g'(y_k)=\frac{\theta_k}{\pi},
\qquad
\eta_k=y_k-[y_k]_<,
\]

at a generic old level. At a simultaneous old inverse wall
$y_k\in\mathbb N$, the literal value is $\eta_k^{\rm lit}=1$ and the
adverse outer-gap limit is $\eta_k^-=0$. Fix one old-level side vector and
use it consistently in $D_A(q)$, $\Omega_-$, and both terminal
decompositions; below $\eta_k\in[0,1]$ denotes that selected coordinate and
$[y_k]_{<,\rm sel}:=y_k-\eta_k$ its selected bracket or one-sided limit.

The angle satisfies

\[
\frac K\pi(\sin\theta_k-\theta_k\cos\theta_k)=k-\frac14.
\]

At the top endpoint,

\[
c_v=-g'(0)=\beta.
\]

Define the supporting tangents

\[
\ell_k(a)=y_k-\frac{a-a_k}{c_k},
\qquad
\ell_v(a)=\frac{v-a}{\beta}.
\tag{2.1}
\]

Convexity of the zero-extended inverse gives

\[
y(a)-\ell_k(a)\ge0\quad(k-1\le a\le k),
\qquad
y(a)-\ell_v(a)\ge0.
\tag{2.2}
\]

The selected exact count at an old inverse level, or its adverse one-sided
limit, is

\[
1+2[y_k]_{<,\rm sel}=2y_k+1-2\eta_k.
\tag{2.3}
\]

Consequently

\[
2\int_{k-1}^{k}y(a)\,da-\bigl(1+2[y_k]_<\bigr)
=\frac1{2c_k}-1+2\eta_k
+2\int_{k-1}^{k}(y-\ell_k)\,da.
\tag{2.4}
\]

Finally put

\[
\Omega_-=
\sum_{k=1}^{B_0}
\left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right),
\qquad
J=2\int_q^\mu G_\mu(z)\,dz.
\tag{2.5}
\]

### 2.2 Literal-wall decomposition

At the literal wall, only the \(B_0\) old levels occur in the strict outer-ball count.  The layer interval above them is

\[
[B_0,v],\qquad v-B_0=\frac34.
\]

Define the exact literal tangent remainder

\[
\boxed{
\begin{aligned}
\mathcal R_{\rm tan}^0
:={}&2\sum_{k=1}^{B_0}
\int_{k-1}^{k}\bigl(y(a)-\ell_k(a)\bigr)\,da\\
&+2\int_{B_0}^{v}
\bigl(y(a)-\ell_v(a)\bigr)\,da.
\end{aligned}}
\tag{2.6}
\]

Every displayed integrand is nonnegative by (2.2), so
\(\mathcal R_{\rm tan}^0\ge0\).  The top tangent triangle is exact:

\[
2\int_{B_0}^{v}\ell_v(a)\,da
=\frac{(v-B_0)^2}{\beta}
=\frac9{16\beta}.
\tag{2.7}
\]

Thus the literal translated-ball defect is

\[
D_K^0(q)=
\sum_{k=1}^{B_0}
\left(\frac\pi{2\theta_k}-1+2\eta_k\right)
+\frac9{16\beta}+\mathcal R_{\rm tan}^0.
\tag{2.8}
\]

Because every positive spatial sample after \(q\) is outside the inner ball when \(\mu=q+1\), the exact shell/ball relation is

\[
D_A(q)=D_K^0(q)+B_{\rm lit}-Q-J=D_K^0(q)-J.
\tag{2.9}
\]

Since

\[
\frac\pi{2\theta_k}-1+2\eta_k
=\left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right)+\zeta,
\]

(2.8)--(2.9) give

\[
\boxed{
L_T^0=\Omega_-+B_0\zeta+\frac9{16\beta}-J,
\qquad
D_A(q)=L_T^0+\mathcal R_{\rm tan}^0.
}
\tag{2.10}
\]

### 2.3 Gap-side limiting decomposition

On the gap side immediately before the outer-action jump, the outer ball has the additional level labelled \(B=B_0+1\), while the shell count remains \(Q=B_0\).  Its inverse displacement tends to

\[
y_B\downarrow0,\qquad a_B=B-\frac14=v,
\qquad c_B\to\beta.
\]

The limiting level contributes one endpoint count.  Its tangent calculation over the full unit layer \([B-1,B]=[B_0,B_0+1]\) is therefore

\[
\frac1{2\beta}-1
+2\int_{B_0}^{B_0+1}(y-\ell_v)\,da.
\]

The \(-1\) is canceled exactly by the gap-side count surplus
\(B-Q=1\).  Define

\[
\boxed{
\begin{aligned}
\mathcal R_{\rm tan}^+
:={}&2\sum_{k=1}^{B_0}
\int_{k-1}^{k}\bigl(y(a)-\ell_k(a)\bigr)\,da\\
&+2\int_{B_0}^{B_0+1}
\bigl(y(a)-\ell_v(a)\bigr)\,da.
\end{aligned}}
\tag{2.11}
\]

Again every integrand is nonnegative, including on \([v,B_0+1]\), where \(y=0\) and \(\ell_v\le0\).  The one-sided ball/shell relation is

\[
D_A(q)=D_K^+(q)+B-Q-J=D_K^+(q)+1-J.
\tag{2.12}
\]

It follows that

\[
\boxed{
L_T^+=\Omega_-+B_0\zeta+\frac1{2\beta}-J,
\qquad
D_A(q)=L_T^++\mathcal R_{\rm tan}^+.
}
\tag{2.13}
\]

Here \(D_K^+\) is the one-sided limiting outer-ball defect, not the literal value \(D_K^0\).  In contrast, \(D_A(q)\) is the same shell terminal defect in both (2.10) and (2.13), because its strict endpoint count remains \(Q=B_0\).

### 2.4 Exact reconciliation

The old-level integrals in (2.6) and (2.11) are identical.  Since \(y(a)=0\) for \(a\ge v\),

\[
\begin{aligned}
\mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0
&=2\int_v^{B_0+1}
\left(0-\frac{v-a}{\beta}\right)da\\
&=\frac{(B_0+1-v)^2}{\beta}
=\boxed{\frac1{16\beta}}.
\end{aligned}
\tag{2.14}
\]

At the same time,

\[
L_T^0-L_T^+
=\frac9{16\beta}-\frac8{16\beta}
=\frac1{16\beta}.
\tag{2.15}
\]

Equations (2.14)--(2.15) prove directly that the two ledgers give the same \(D_A(q)\).  The quantity \(1/(16\beta)\) is not a new reserve produced by changing owners: it moves from the literal top triangle into the right-hand Bregman part of the gap-side unit layer.

## 3. Exact shelf trapezoid, signs, and curvature ledger

### 3.1 Exact identities

On the common shelf define

\[
R_p=2\int_r^x A(z)\,dz-2pf,
\qquad
\mathcal C_p=-\int_0^p u(p-u)A''(r+u)\,du.
\tag{3.1}
\]

Two integrations by parts, using \(u(p-u)=0\) at \(u=0,p\), give

\[
\boxed{
\mathcal C_p
=2\int_r^x A(z)\,dz-p\bigl(A(r)+A(x)\bigr).
}
\tag{3.2}
\]

Since

\[
A(r)+A(x)=2f-\frac12+E,
\]

(3.1)--(3.2) yield

\[
\boxed{R_p=\mathcal C_p+p\left(E-\frac12\right).}
\tag{3.3}
\]

### 3.2 Derivative signs and the elementary reserve

On \([r,x]\), one has \(0<r\le x<q<\mu<K\), and

\[
G_a'(z)=-\frac1\pi\arccos\frac za,
\qquad
G_a''(z)=\frac1{\pi\sqrt{a^2-z^2}}.
\]

Therefore

\[
A'(z)=\frac1\pi
\left(\arccos\frac z\mu-\arccos\frac zK\right)<0,
\tag{3.4}
\]

\[
A''(z)=\frac1\pi
\left(\frac1{\sqrt{K^2-z^2}}-
      \frac1{\sqrt{\mu^2-z^2}}\right)<0,
\tag{3.5}
\]

and, putting \(\kappa=-A''\),

\[
\kappa'(z)=\frac z\pi
\left((\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}\right)>0.
\tag{3.6}
\]

Thus \(\kappa\) is positive and strictly increasing.  It follows immediately that

\[
\boxed{
\begin{aligned}
\mathcal C_p
&=\int_0^p u(p-u)\kappa(r+u)\,du\\
&\ge\kappa(r)\int_0^p u(p-u)\,du\\
&=\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}-
\frac1{\sqrt{K^2-r^2}}
\right)>0.
\end{aligned}}
\tag{3.7}
\]

### 3.3 Independent proof and full loss ledger for \(\mathcal C_p\ge a_p\Delta\)

The allowed Round 10 source states this inherited estimate but does not print its proof.  It can be reconstructed without an additional source as follows.

Set

\[
\sigma=-A',\qquad \kappa=\sigma'=-A'',
\qquad \sigma(0)=0,
\]

\[
c=\kappa(r),\qquad
\nu(u)=\kappa(r+u)-c,
\qquad
\delta_r=rc-\sigma(r)=\int_0^r(c-\kappa(s))\,ds.
\tag{3.8}
\]

Because \(\kappa\) is increasing, \(\delta_r\ge0\), and \(\nu\ge0\) is nondecreasing.  Fubini gives the exact formulas

\[
\Delta=\int_0^p\sigma(r+u)\,du
=\frac{cp(2r+p)}2-p\delta_r
+\int_0^p(p-u)\nu(u)\,du,
\tag{3.9}
\]

\[
\mathcal C_p=\frac{cp^3}{6}
+\int_0^p u(p-u)\nu(u)\,du.
\tag{3.10}
\]

With \(a_p=p^2/[3(2r+p)]\), the constant-curvature terms in
\(\mathcal C_p-a_p\Delta\) cancel exactly.  Writing the remaining weighted covariance as a double integral gives the exact nonnegative ledger

\[
\boxed{
\begin{aligned}
\mathcal C_p-a_p\Delta
={}&a_pp\,\delta_r\\
&+\left(\frac p3-a_p\right)
  \int_0^p(p-u)\nu(u)\,du\\
&+\frac1{p^2}\int_0^p\!\int_0^p
 (p-u)(p-w)(u-w)\bigl(\nu(u)-\nu(w)\bigr)
 \,du\,dw.
\end{aligned}}
\tag{3.11}
\]

Indeed \(p/3-a_p=2rp/[3(2r+p)]\ge0\), and the double-integral integrand is pointwise nonnegative because \(\nu\) is nondecreasing.  Hence

\[
\boxed{\mathcal C_p\ge a_p\Delta.}
\tag{3.12}
\]

On the present owner \(r>0\) and \(\kappa\) is strictly increasing, so already \(\delta_r>0\); the difference in (3.11) is in fact strict.  Formula (3.11), rather than the phrase “curvature slack,” records every loss in this shelf projection.

## 4. Exact Gate-B scalar ledger

From (1.9), (2.10), and (2.13), the same exact scalar has the two owner-specific representations

\[
\boxed{
\mathscr S
=L_T^++\mathcal R_{\rm tan}^+
+\mathcal C_p+p(E-E_*),
}
\tag{4.1}
\]

\[
\boxed{
\mathscr S
=L_T^0+\mathcal R_{\rm tan}^0
+\mathcal C_p+p(E-E_*).
}
\tag{4.2}
\]

The exact Round 42 endpoint identity is

\[
\Phi_\delta^+
=\frac1{2\beta}-J+\Omega_-+B_0\zeta
+(p+a_p)\Delta+2pe_p-\frac{p-d_\rho m}{2}.
\tag{4.3}
\]

Using \(E=\Delta+2e_p\) and \(pE_*=(p-d_\rho m)/2\), this simplifies, without inequality, to

\[
\boxed{
\Phi_\delta^+=L_T^++a_p\Delta+p(E-E_*).
}
\tag{4.4}
\]

Subtracting (4.4) from (4.1) gives the exact loss ledger

\[
\boxed{
\mathscr S-\Phi_\delta^+
=\mathcal R_{\rm tan}^+
+\bigl(\mathcal C_p-a_p\Delta\bigr).
}
\tag{4.5}
\]

The reconciliation (2.14) gives the literally equivalent form

\[
\boxed{
\mathscr S-\Phi_\delta^+
=\frac1{16\beta}+\mathcal R_{\rm tan}^0
+\bigl(\mathcal C_p-a_p\Delta\bigr).
}
\tag{4.6}
\]

Every term on the right of (4.5) is nonnegative, and every term in (4.6) is displayed rather than absorbed into an unnamed convexity reserve.  This proves \(\mathscr S\ge\Phi_\delta^+\), but it does not prove either scalar nonnegative.

The unprojected sign that remains is exactly

\[
\boxed{
\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p
\ge p(E_*-E).
}
\tag{4.7}
\]

No allowed clean-room source proves (4.7) on the entire owner, and I do not replace it by a renamed projected scalar.

## 5. Equality faces, ownership audit, and clean-room classification

### 5.1 Equality and one-sided ownership table

| Face | Literal value / owner | Consequence for the reconstruction |
|---|---|---|
| \(A(r+s)+1/4\in\mathbb Z\) on the first shelf | The ordinary-floor remainder at that sample is \(0\); the corresponding strict spectral level is absent. | Use the wall-safe first-shelf identity at the literal value.  Do not infer it by continuity across the shelf-floor jump. |
| \(G_K(q)+1/4=B\in\mathbb Z\) | \(B_{\rm lit}=[B]_< =B-1=B_0\); the gap-side label remains \(B\). | Literal ledger: top triangle \(9/(16\beta)\).  Gap-side ledger: limiting level \(B\), surplus \(B-Q=1\), and full unit-layer remainder. |
| \(A(q)+1/4\in(B-1,B)\) | Here it equals \(B-h\), so \(Q=B-1=B_0\). | The shell terminal count does not jump at the outer-ball wall. |
| Old inverse wall \(y_k\in\mathbb N\) | \(\eta_k=1\) literally; on the adverse side \(\eta_k\downarrow0\). | Both values are retained inside \(\Omega_-\) and the integrals (2.6), (2.11). |
| Newest inverse displacement | \(y_B\downarrow0\) only on the gap side; the literal wall excludes level \(B\). | It is an outer-action jump, not a second old-inverse jump. |
| \(e_p=0\) | Literal lower shelf wall. | Equations (3.3), (4.1)--(4.6) remain exact; no continuity across the floor jump is used. |
| \(E=E_*\) | Boundary of the automatic/remainder-rich sector, not part of the strict hard owner \(E<E_*\). | The term \(p(E-E_*)\) vanishes there; the Gate-B identities still have a direct boundary value, but no hard-owner sign is inferred by crossing the wall. |
| Curvature/elasticity switch in the inherited projection | The competing projected payments agree on the switch. | It affects how earlier work obtains \(a_p\Delta\), not the exact \(\mathcal C_p\) identity; (3.11) is global and has no switch discontinuity. |
| \(B_0=1\) | Admissible smallest old-level count; \(B=2\). | Both sums contain exactly one old level and all formulas above remain valid.  \(B_0=0\) is not in this owner. |
| Integer versus half-integer grid | (1.7), with the appropriate dimension label. | The terminal and shelf derivations are continuous in \(r\) but are asserted only on these two discrete grids. |
| Activity equality | Equality in (1.8) is owned by the dimension-labelled no-mode theorem. | The live owner uses strict activity; it is not closed by continuity from the active side. |
| Upper-alpha endpoint | Geometry is evaluated at \(\mu=q+1\), with the \(\alpha\uparrow1^-\) labels retained. | It is not the next chart's literal \(\alpha=0\) point; in particular, no count or shelf index is silently redefined. |

### 5.2 What is proved, what is inherited, and what is open

**Proved directly in this reconstruction:**

1. the exact literal count \(B_{\rm lit}=Q=B-1\);
2. the gap-side and literal terminal decompositions, including every tangent-remainder integral;
3. \(\mathcal R_{\rm tan}^+=\mathcal R_{\rm tan}^0+1/(16\beta)\) and its ownership meaning;
4. the shelf trapezoid identities, derivative signs, positivity, and elementary curvature reserve;
5. an explicit nonnegative loss ledger proving \(\mathcal C_p\ge a_p\Delta\);
6. both exact representations of \(\mathscr S\) and the two equivalent identities for \(\mathscr S-\Phi_\delta^+\);
7. the legitimacy of evaluating the endpoint geometry at \(\mu=q+1\) while retaining one-sided labels.

**Inherited but not re-proved here:** the wall-safe first-shelf reduction from \(D_A(r)\) to \(\mathscr S\), the dimension-labelled no-mode/activity owner, and the earlier reduction defining \(\Phi_\delta^+\).

**Open:** the sign (4.7), hence \(\mathscr S\ge0\), the resisting endpoint, high-floor CST, the pointwise assembly, the branching-backbone audit, and the all-dimensional theorem.

There is no unresolved algebraic conflict among the allowed sources after separating Round 10's literal \(B\) from the newer one-sided gap label.  The only genuine remaining mathematical uncertainty is the global sign (4.7).

### 5.3 Clean-room verdict

\[
\boxed{\texttt{STRUCTURAL PASS — FINAL SIGN OPEN}.}
\]

The exact owner, terminal reconciliation, shelf identities, and Gate-B loss ledger reconstruct consistently.  They expose additional nonnegative reserve beyond \(\Phi_\delta^+\), but they do not by themselves sign the exact scalar on the entire owner.

## 6. Post-freeze source addendum

Sections 1--5 were frozen before the lead artifact existed.  The SHA-256 of this file at that freeze point was

~~~text
62b417f4584c9b69ffff8808cb589124745e3227d297c0fcae8972dfe8e48696
~~~

The final post-freeze audit found an encoding-only U+0008 in (2.4), where
the intended LaTeX token was \(\backslash\mathrm{bigl}\), and a missing
backslash before \(\backslash\mathrm{qquad}\) in Section 2.3. It also made
explicit in Section 2.1 the fixed old-inverse side-vector convention already
required by the equality table: \(\eta_k=1\) literally and
\(\eta_k=0\) on the adverse limit. These repairs changed no identity,
sign, conclusion, or source dependency. The post-repair SHA-256 of the
Sections 1--5 prefix is

~~~text
0a9da60b226fd7fb034c45850cd808d20362b747806b3390bbf9dd6487f26341
~~~

Only after that freeze did I read

~~~text
human/outbox/general-d-round-44-exact-gate-b-terminal-trapezoid-reconstruction.md
~~~

in its regenerated, stable form, whose SHA-256 at comparison time was

~~~text
3149c6fabf24df9680c68807b92239114f52bde6289e2eeedd982802524b5a86
~~~

I did not read the lead replay, lead diagnostic, adversarial-search source, adversarial report, or a Round 44 audit in order to prepare Sections 1--5 or this formula comparison.  Numerical claims copied into the lead note therefore remain lead diagnostics rather than independently replayed clean-room results.

## 7. Comparison with the lead Round 44 note

### 7.1 Exact agreements

The independent reconstruction and the stable lead note agree, term for term, on every Prompt-B identity:

| Item | Clean-room formula | Lead formula | Comparison |
|---|---:|---:|---|
| literal terminal owner | \(B_{\rm lit}=Q=B_0=B-1\) | Section 1 | exact agreement |
| gap skeleton | \(L_T^+=\Omega_-+B_0\zeta+1/(2\beta)-J\) | (R44.16) | exact agreement |
| literal skeleton | \(L_T^0=\Omega_-+B_0\zeta+9/(16\beta)-J\) | (R44.19) | exact agreement |
| gap tangent remainder | old unit-layer Bregman areas plus the integral over \([B_0,B_0+1]\) | (R44.17) | identical integration domain and integrand |
| literal tangent remainder | old unit-layer Bregman areas plus the integral over \([B_0,v]\) | (R44.20) | identical integration domain and integrand |
| owner reconciliation | \(\mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0=1/(16\beta)\) | (R44.22) | exact agreement |
| shelf trapezoid | (3.2)--(3.3) | (R44.3)--(R44.4) | exact agreement |
| derivative signs and elementary reserve | (3.4)--(3.7) | (R44.2), (R44.5) | exact agreement |
| gap-side Gate-B representation | (4.1) | (R44.24) | exact agreement |
| literal Gate-B representation | (4.2) | (R44.25) | exact agreement |
| Round 42 identity | (4.4) | (R44.26) | exact agreement |
| full loss ledger | (4.5)--(4.6) | (R44.27)--(R44.28) | exact agreement |
| upper-alpha ownership | evaluate \(\mu=q+1\), retain the old chart's one-sided \(B\) | Sections 1.3 and 5.1 | exact agreement |

In particular, both derivations locate the reconciliation triangle on the same interval:

\[
2\int_v^{B_0+1}\frac{\ell-v}{\beta}\,d\ell
=\frac{(B_0+1-v)^2}{\beta}
=\frac1{16\beta}.
\]

Neither derivation treats this quantity as a reserve created by changing owners.

### 7.2 Different but equivalent shelf-loss ledgers

The two notes prove \(\mathcal C_p\ge a_p\Delta\) in different exact coordinates.

- Section 3.3 above freezes the curvature at \(r\), writes
  \(\kappa(r+u)=\kappa(r)+\nu(u)\), and resolves the loss into the
  pre-\(r\) curvature deficit, a positive coefficient times a weighted
  curvature increment, and a nonnegative double covariance integral.
- The lead note writes the convex slope \(\sigma=-A'\) as a positive
  superposition of the generators \(z\) and \((z-s)_+\), then prints the
  loss of every hinge in (R44.7)--(R44.10).

These are two decompositions of the same linear functional
\(\mathcal C_p-a_p\Delta\); their conclusions agree.  The clean-room
ledger additionally observes that the difference is strict on this shell
owner because \(r>0\) and \(\kappa=-A''\) is strictly increasing.  The
lead's weaker nonnegative statement is correct and sufficient.  This is a
difference of representation and strength, not a discrepancy.

### 7.3 Lead-only top-Bregman reserve and localization

The lead note goes beyond the Prompt-B reconstruction by proving

\[
\mathcal R_{\rm tan}^0
\ge
\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}.
\tag{7.1}
\]

This additional result checks cleanly.  In the lead notation,

\[
Y''(\ell)
=\frac{\pi^2}{\sqrt{K^2-z^2}\,\theta^3}
\ge
\frac1{\pi\sqrt{K^2-q^2}\,\beta^3}
=:c_{\rm top}
\]

on \(B_0\le\ell\le v\).  Taylor's integral remainder gives

\[
Y(\ell)-\Lambda_v(\ell)
\ge\frac{c_{\rm top}}2(v-\ell)^2.
\]

Therefore

\[
2\int_{B_0}^{v}(Y-\Lambda_v)\,d\ell
\ge c_{\rm top}\frac{(3/4)^3}{3}
=\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},
\]

which is (7.1).  Combining it with the elementary curvature reserve and
the literal exact ledger yields the lead's necessary negative-support
condition (R44.30). For its count-free \(49/40\) corollary, note that
\(G_K(\mu)=v-u>B_0+1/4\), whereas
\(a_k=k-1/4\le B_0-1/4\); hence every old inverse has
\(\theta_k<t\) and therefore \(\Omega_->0\). Combining this with
\(B_0\zeta>1/5\), \(\beta<1/2\), and \(J<1/10\) gives
\[
\Omega_-+B_0\zeta+\frac9{16\beta}-J>\frac{49}{40}.
\]

Thus the lead legitimately attains Prompt A's partial-success criterion:
every possible negative point is confined by one intrinsic inequality,
with no forbidden \(B_0\)-, \(j\)-, \(f\)-, ratio-, or chamber-indexed
split.  This new localization was absent from the frozen clean-room
Sections 1--5 because Prompt B required reconstruction rather than a new
sign attempt; its absence is not a clean-room defect.

### 7.4 Complete discrepancy list

There is no substantive algebraic or ownership discrepancy in the terminal,
shelf, or scalar identities.  The remaining differences are:

1. **Activity notation (resolved during comparison).**  Section 1.3 retains the ambient-dimension formula
   \[
   \frac{(d_{\rm amb}-2)^2-1}{4},
   \]
   The first lead draft wrote only the weakest new-dimension constants
   \(3/4\) on the integer grid and \(2\) on the half-integer grid.  Those
   are safe \(d_{\rm amb}=4\) and \(d_{\rm amb}=5\) enlargements for a
   dimension-uniform proof or search, but they are not the literal
   ambient-\(d_{\rm amb}\) activity equality.  The current stable lead note
   now states the exact dimension-labelled formula first and labels the
   two constants separately as the weakest-grid enlargement.  There is no
   remaining owner discrepancy.
2. **Historical \(n\)-overload.**  The lead explicitly records that Round
   10's \(n=\lfloor\mu-r\rfloor\) has gap-side value \(p+m\) for
   \(0<\alpha<1\), but literal endpoint value \(p+m+1\) at
   \(\mu=q+1\); neither is the later count coordinate \(f-1=B_0+j\).
   The clean-room derivation avoids \(n\) altogether after defining the
   owner. The lead's warning is useful and consistent.
3. **The \(e_p=0\) provenance statement.**  The lead additionally says the
   simultaneous lower-shelf face was closed in audited Round 39.  Round 39
   was intentionally outside the seven-source clean-room set, so that
   historical closure was not independently adjudicated here.  It is not
   used in any identity or in this verdict.
4. **Classification vocabulary.**  Prompt A permits “partial success,”
   and the lead earns it through (R44.30).  Prompt B's allowed verdict list
   does not contain that label.  Accordingly the clean-room verdict remains
   **STRUCTURAL PASS — FINAL SIGN OPEN**.  The two classifications are
   compatible: the exact structure and one intrinsic localization are
   proved, while the continuum sign of \(\mathscr S\) remains open.
5. **Computation scope.**  The lead's finite searches and replay are not
   clean-room proof premises and were not independently rerun here.  The
   lead labels them diagnostic and makes no positive coverage claim, so
   there is no classification conflict.

### 7.5 Final comparison verdict

**Lead-note reconstruction:** **PASS** on the exact owner, terminal
reconciliation, shelf ledger, and scalar identities.

**Prompt-B mathematical verdict:**  
\[
\boxed{\texttt{STRUCTURAL PASS — FINAL SIGN OPEN}.}
\]

The lead's additional top-Bregman theorem supplies a valid intrinsic
negative-support localization and keeps Gate B active.  It does not prove
that the localized support is empty, does not prove
\(\mathscr S\ge0\) on the continuum owner, and does not activate Gate C.
