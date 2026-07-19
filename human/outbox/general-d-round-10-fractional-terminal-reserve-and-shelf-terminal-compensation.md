# Fractional terminal reserve and shelf--terminal compensation for shifted shell tails

Date: 18 July 2026  
Round: 10, revised analytic strategy  
Status: WP1 proved; exact CST scalar derived; WP2 reduced but not closed

## 0. Scope and theorem boundary

This note starts the replacement program required by
`human/inbox/general-d_simplified_analytic_strategy.md`.

The following are completed here.

1. The fractional inverse-level reserve (T1) is proved with every strict
   spatial and action wall included.
2. Its shell specialization (T2), the local inner-cap estimate (T3), and the
   exact correlation (A(q)=v-h) are proved and normalized.
3. The exact shelf--terminal scalar and the lower surrogate obtained from
   (S1)--(S3) and (T2)--(T4) are separated explicitly.
4. In the first-floor no-drop branch, the automatic remainder-rich sector and
   the whole (B\ge2) sector are closed analytically.  The only remaining
   phases are an endpoint (B=0) inequality and a one-level (B=1)
   inequality printed in Section 3.

The following are **not** completed here.

- The first-floor no-drop branch is not yet proved in full.
- High-floor first-drop CST is not proved.
- The all-dimensional Pólya theorem is not proved.

The old ratio ladder and interval certificates remain frozen provenance.  No
result in this note deletes a previously proved module or promotes a numerical
search to proof.

Throughout,

\[
 [x]_<:=\#\{j\in\mathbb N:j<x\}
       =\max\{0,\lceil x\rceil-1\}.
\]

Thus (x-[x]_<\in(0,1]) for (x>0), and the value is (1), not (0),
when (x) is integral.

Every shifted tail considered here lies on the admissible angular grid

\[
 r\in\tfrac12\mathbb N,
 \qquad r\ge\tfrac12.
\]

Whenever spectral activity is invoked, the shift is dimension-labelled as
(r=m+(d-2)/2); the wall is therefore tested for that dimension rather than
for an unlabelled value of (r).

Fix (0<\mu<K), put (\rho=\mu/K), and define

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}
 \quad(0\le z<a),
 \qquad G_a(z)=0\quad(z\ge a),
\]

\[
 A=G_K-G_\mu,
 \qquad
 T_A(r)=[A(r)+\tfrac14]_<
 +2\sum_{j\ge1}[A(r+j)+\tfrac14]_<,
\]

\[
 D_A(r)=2\int_r^K A(z)\,dz-T_A(r).
\]

For an inner start, put

\[
 n=\lfloor\mu-r\rfloor,
 \qquad q=r+n,
 \qquad q\le\mu<q+1,
 \qquad d_\rho=\frac{2\arcsin\rho}{\pi}.
\]

Let (F_j=\lfloor A(r+j)+1/4\rfloor).  If the first ordinary-floor
shelf ends at (p), define

\[
 \varepsilon_j=A(r+j)+\frac14-F_j,
 \qquad
 \sigma=-A',
\]

\[
 R_p=2\int_r^{r+p}A(z)\,dz-2pF_0,
 \qquad
 \mathcal C_p=-\int_0^p u(p-u)A''(r+u)\,du.
\]

The proved inputs are

\[
 D_A(r)\ge D_A(q)+R_p+\frac{d_\rho}{2}(n-p),
 \tag{S1}
\]

\[
 R_p=\mathcal C_p
 +p\left(\varepsilon_0+\varepsilon_p-\frac12\right),
 \tag{S2}
\]

\[
 \mathcal C_p\ge
 \frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p).
 \tag{S3}
\]

When (p=n), assume the shelf has no drop,

\[
 F_0=F_1=\cdots=F_n=f,
\]

and put

\[
 \varepsilon_q=A(q)+\frac14-f,
 \qquad
 \chi_q=\mathbf 1_{\{A(q)+1/4=f\}}.
\]

The sharper exact no-drop identity is

\[
 D_A(r)=D_A(q)-\frac n2+2n\varepsilon_q
 +2\int_0^n u\sigma(r+u)\,du+\chi_q.
 \tag{S4}
\]

## 1. Lemma package WP1: fractional terminal reserve

### 1.1 Statement

Let (g) be nonnegative, strictly decreasing, convex, and (C^1) on
([0,L)), with (g(L)=0), and extend it by zero for (s\ge L).  Put

\[
 v=g(0),\qquad c_v=-g'(0)>0,
\]

\[
 D_g=2\int_0^L g(s)\,ds-
 \left([g(0)+\tfrac14]_<
 +2\sum_{j\ge1}[g(j)+\tfrac14]_<\right),
 \qquad B=[v+\tfrac14]_<.
\]

For (1\le k\le B), let (y_k\in(0,L)) solve

\[
 g(y_k)=k-\frac14,
\]

and put

\[
 c_k=-g'(y_k)>0,
 \qquad
 \eta_k=y_k-[y_k]_<\in(0,1].
\]

Then

\[
 \boxed{
 D_g\ge
 \sum_{k=1}^{B}
 \left(\frac1{2c_k}-1+2\eta_k\right)
 +\frac{(v-B)_+^2}{c_v}.}
 \tag{T1}
\]

For the shell terminal point (q\le\mu<q+1), define

\[
 v=G_K(q),\qquad h=G_\mu(q),
 \qquad B=[v+\tfrac14]_<,
 \qquad Q=[v-h+\tfrac14]_<,
\]

\[
 \beta=\frac{\arccos(q/K)}{\pi},
 \qquad
 \delta=\int_q^\mu G_\mu(z)\,dz.
\]

For (1\le k\le B), let (\theta_k\in(0,\pi/2)) solve

\[
 \frac K\pi(\sin\theta_k-\theta_k\cos\theta_k)
 =k-\frac14,
\]

and, crucially, use the inverse **displacement**

\[
 y_k=K\cos\theta_k-q,
 \qquad
 \eta_k=y_k-[y_k]_<.
 \tag{1.1}
\]

Then

\[
 \boxed{
 D_A(q)\ge L_T:=
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 +2\sum_{k=1}^{B}\eta_k-Q-2\delta
 +\frac{(v-B)_+^2}{\beta}.}
 \tag{T2}
\]

Using the already proved complete one-interface theorem gives the stronger
wall-safe form

\[
 \boxed{D_A(q)\ge\max\{0,L_T\}.}
 \tag{1.2}
\]

Finally, with

\[
 \alpha=\mu-q\in[0,1),
 \qquad h=G_\mu(q),
\]

one has

\[
 \boxed{0\le2\delta\le\alpha h,}
 \tag{T3}
\]

strictly on the right when (\alpha>0), together with the exact identity

\[
 \boxed{A(q)=v-h.}
 \tag{T4}
\]

### 1.2 Dependencies

- strict counting by ([\,\cdot\,]_<);
- elementary layer cake;
- convexity of an inverse of a decreasing convex function;
- the already proved one-interface nonnegativity only for the optional
  maximum in (1.2).

No certificate, ratio theorem, or asymptotic estimate is used.

### 1.3 Proof

Define the strict superlevel-length inverse

\[
 y(t)=|\{s\ge0:g(s)>t\}|.
\]

For (0<t<v), this is the ordinary inverse of (g); set (y(t)=0) for
(t\ge v), and (y(0)=L).  On ((0,v)),

\[
 y'(t)=\frac1{g'(y(t))}<0.
\]

Because (g') is nondecreasing and (y) is decreasing, (y') is
nondecreasing.  Hence (y) is convex.  At (v),

\[
 y'(v-)=-\frac1{c_v}\le0,
 \qquad y'(v+)=0,
\]

so the zero extension remains convex.

Layer cake gives

\[
 2\int_0^L g(s)\,ds=2\int_0^v y(t)\,dt.
 \tag{1.3}
\]

At level (k-1/4), a sample (j\ge0) contributes precisely when
(j<y_k).  Its exact endpoint-one/interior-two contribution is therefore

\[
 1+2[y_k]_<
 =2y_k+1-2\eta_k.
 \tag{1.4}
\]

This includes the spatial wall (y_k=m\in\mathbb N), when the equality
sample is absent and (1.4) equals (2m-1).

The supporting tangent to (y) at (t_k=k-1/4) gives

\[
 y(t)\ge y_k-\frac{t-t_k}{c_k}.
\]

Consequently

\[
 2\int_{k-1}^{k}y(t)\,dt
 \ge2y_k+\frac1{2c_k}.
\]

Subtracting (1.4) gives the (k)-th summand in (T1).  The intervals
([k-1,k]), (1\le k\le B), cover ([0,B]).  If (v\le B), the zero
extension covers the whole layer integral.  If (v>B), the tangent at
(v) gives

\[
 y(t)\ge\frac{v-t}{c_v}
 \quad(B\le t\le v),
\]

and hence

\[
 2\int_B^v y(t)\,dt\ge\frac{(v-B)^2}{c_v}.
\]

This proves (T1).

Apply (T1) to (g(s)=G_K(q+s)).  Since

\[
 -G_K'(z)=\frac{\arccos(z/K)}\pi,
\]

one has (c_v=\beta) and (c_k=\theta_k/\pi).  Let (D_K(q)) be the
translated ball defect.  Then

\[
 D_K(q)\ge
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -B+2\sum_{k=1}^{B}\eta_k
 +\frac{(v-B)_+^2}{\beta}.
 \tag{1.5}
\]

Because (q\le\mu<q+1), all samples (q+j), (j\ge1), lie outside the
inner ball.  Only the endpoint count and the cap integral change, so exactly

\[
 D_A(q)=D_K(q)+B-Q-2\delta.
 \tag{1.6}
\]

The (-B) in (1.5) cancels the (+B) in (1.6), proving (T2).  Equation
(1.2) adds the proved one-interface theorem.

For (T3), (G_\mu''(z)=1/[\pi\sqrt{\mu^2-z^2}]>0) on
((q,\mu)).  If (\alpha>0), strict convexity places (G_\mu) strictly
below the chord joining ((q,h)) to ((\mu,0)).  Thus

\[
 \delta<\frac h\alpha\int_q^\mu(\mu-z)\,dz
 =\frac{\alpha h}{2}.
\]

For (\alpha=0), both sides vanish.  Equation (T4) is the definition of
(A).

### 1.4 Equality-face audit

- If (A(q+j)+1/4\in\mathbb N), the equality level is absent.  For
  (j\ge1), (y_k=j), so (\eta_k=1) and (1.4) is exact.
- If (G_K(q)+1/4=N\in\mathbb N), then (B=N-1).  The equality level at
  (s=0) is absent; the remaining top interval is retained by
  ((v-B)^2/\beta).
- If (q+j=\mu), the one-interface constraint forces (j=0) and
  (q=\mu).  Then (h=\delta=0) and (B=Q).
- If (q+j=K), the action is zero and its strict bracket is zero.
- If (\mu-r\in\mathbb N), then (q=\mu), so the zero-cap audit applies.
- If (y_k\in\mathbb N), use (\eta_k=1), not (0).
- If (B=0), the sum is empty and (T1) is the top triangle
  (D_g\ge v^2/c_v).
- If (v<B), the zero extension on ([v,B]) is essential.  If (v=B),
  the top term vanishes exactly.

### 1.5 Loss ledger

Let

\[
 \ell_k(t)=y_k-\frac{t-(k-1/4)}{c_k},
 \qquad
 \ell_v(t)=\frac{v-t}{c_v}.
\]

The exact discarded part of (T1) is

\[
 2\sum_{k=1}^{B}\int_{k-1}^{k}(y-\ell_k)\,dt
 +2\mathbf1_{\{v>B\}}\int_B^v(y-\ell_v)\,dt\ge0.
 \tag{1.7}
\]

No fractional inverse-level term is discarded.  Equations (T2), (T4), and
(1.6) are exact apart from (1.7).  Replacing (-2\delta) by
(-\alpha h) discards exactly the positive cap slack

\[
 \alpha h-2\delta,
\]

which is strict for (\alpha>0).

### 1.6 Counterexample search

The seeded Mathematica 15.0 evaluator
`computations/general_d_fractional_terminal_probe.wl` checks (T2), (S4),
and the old/new terminal scalar using 70-digit inputs and 55-digit root
solves.  In 6,409 retained records, the smallest sampled (T1), (T2), and
(T3) slacks were approximately (0.337996), (0.337996), and
(1.09\times10^{-9}), respectively, with no negative sampled slack.  It also
reproduces an off-active point

\[
 q=\frac32,\quad \mu=\frac{58}{25},\quad K=\frac{232}{99},
\]

where the raw (T2) expression is approximately
(-0.01136862444), while (D_A(q)\approx0.006600268745).  This confirms
that the maximum in (1.2) must be retained when positivity is needed.

The computation is diagnostic only.  The proof above is analytic.

### 1.7 Failure report

There is no remaining mathematical inequality in WP1.  The audit hazards
were purely definitional and are repaired here:

1. (c_v=-g'(0)) must be defined;
2. the inverse must be zero-extended;
3. (\eta_k) uses the displacement (K\cos\theta_k-q), not the absolute
   crossing (K\cos\theta_k); and
4. raw (T2) is a lower bound, not automatically a positive reserve.

## 2. Proposition: exact and lower combined shelf--terminal scalars

### 2.1 Statement

Define the exact reduced target

\[
 \boxed{
 \mathscr S=
 D_A(q)+\mathcal C_p
 +p\left(\varepsilon_0+\varepsilon_p-\frac12\right)
 +\frac{d_\rho}{2}(n-p).}
 \tag{2.1}
\]

Then (S1)--(S2) give

\[
 D_A(r)\ge\mathscr S.
 \tag{2.2}
\]

This is the exact shelf--terminal scalar after the already proved first-shelf
reduction.  It must not be confused with the derived lower surrogate

\[
\boxed{
\begin{aligned}
 \Phi_\delta={}&
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 +2\sum_{k=1}^{B}\eta_k-Q-2\delta
 +\frac{(v-B)_+^2}{\beta}\\
 &+\frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p)
 +p\left(\varepsilon_0+\varepsilon_p-\frac12\right)
 +\frac{d_\rho}{2}(n-p).
\end{aligned}}
 \tag{2.3}
\]

One has

\[
 D_A(r)\ge\Phi_\delta.
 \tag{2.4}
\]

Two useful variants are also valid:

- replace the first line of (2.3) by its maximum with (0), using (1.2);
- replace (-2\delta) by (-\alpha h), using (T3).

All variables in (2.3) remain subject to the exact correlations

\[
 A(q)=v-h,\qquad
 q=r+n,\qquad
 0\le\alpha<1,\qquad
 Q=[v-h+\tfrac14]_<.
 \tag{2.5}
\]

For no-drop (p=n), the correct wall-safe target is instead the exact (S4)

\[
 \boxed{
 \mathscr N=
 D_A(q)-\frac n2+2n\varepsilon_q
 +2\int_0^n u\sigma(r+u)\,du+\chi_q.}
 \tag{2.6}
\]

Thus a universal CST statement without (\chi_q) is unnecessarily strong
on an endpoint wall.  CST should be restricted to first-drop/off-wall cases,
or amended by the no-drop wall term.

### 2.2 Dependencies

- (S1)--(S4), already proved in the current manuscript;
- the WP1 package in Section 1;
- no further analytic or computational premise.

### 2.3 Proof

Equations (2.1)--(2.2) are (S1) with the exact identity (S2) substituted.
Substitute (T2) for (D_A(q)) and (S3) for (\mathcal C_p) to obtain
(2.3)--(2.4).  The two variants follow from (1.2) and (T3).  Equation (2.6)
is (S4).

### 2.4 Equality-face audit

The terminal walls are audited in Section 1.4.  At a shelf floor wall,
(F_j) is the ordinary floor and (\varepsilon_j=0); (S2) remains exact.
At (p=n) and (A(q)+1/4=f), (2.6) retains (\chi_q=1).  At
(r+j=\mu) or (\mu-r\in\mathbb N), (q=\mu) and the cap vanishes.
At (r+j=K), the strict bracket is zero.

### 2.5 Loss ledger

The losses between (D_A(r)) and (\Phi_\delta) are exactly:

1. the slack in the proved first-shelf reduction (S1);
2. the hinge surplus discarded in (S3);
3. the inverse tangent gaps (1.7);
4. optionally, the cap slack (\alpha h-2\delta).

The terms (2\eta_k), (B-Q), ((v-B)_+^2/\beta), the exact cap
(2\delta), and the endpoint term (\chi_q) are not silently discarded.

### 2.6 Counterexample search

The Mathematica evaluator separately checks the exact defect, (S4), the old
surrogate without (2\eta_k), and (2.3).  In 6,409 retained
dimension-active first-floor no-drop records, Mathematica printed the largest
absolute (S4) residual as numerical zero with about (64.38) digits of
accuracy.  This is a high-precision identity replay, not a certified bound
below (10^{-64}).  No negative new surrogate was found.

Here `dOwner` means the smallest new dimension that needs the shift after the
completed (d=3) theorem is taken as the base case: integer shifts are tested
at (d=4), half-integer shifts (r\ge3/2) at (d=5), and (r=1/2) is retained
only as a (d=3) comparison point.  It is not the literal smallest possible
dimension for every shift.

The old surrogate was negative at the retained point

\[
 (\rho,K,r)\approx(0.6056801590,8.0207601251,1),
\]

where it was approximately (-0.03758).  Restoring (2\eta_1) changes the
surrogate to approximately (0.74904).  This is a diagnostic demonstration
that the fractional term is load-bearing, not a proof of global positivity.

### 2.7 Failure report

No proof of (\Phi_\delta\ge0) is claimed.  The exact missing step is a
quantitative transport from a poor shelf reserve to one or more of

\[
 B-Q,\qquad \sum\eta_k,\qquad
 \frac{(v-B)_+^2}{\beta},
\]

without worst-casing those variables independently.  The current shell
elasticity inequality is the intended transport input.

## 3. First-floor no-drop: analytic reductions

### 3.1 Statement

Assume

\[
 p=n\ge1,\qquad F_0=\cdots=F_n=1.
 \tag{3.1}
\]

Then

\[
 \varepsilon:=\varepsilon_q=A(q)-\frac34\in[0,1).
\]

The branch is proved whenever (\varepsilon\ge1/4).  It is also proved
whenever the terminal complete-level count (B\ge2).  Every remaining point
has (B\in\{0,1\}), and the two residual inequalities are exactly (3.5) and
(3.7) below.

### 3.2 Dependencies

- the exact no-drop identity (S4);
- the completed one-interface theorem (D_A(q)\ge0);
- WP1;
- the proved local cap bound
  (G_\mu(q)\le G_{q+1}(q)\le G_{5/2}(3/2)<1/5) for (q\ge3/2).

### 3.3 Proof

From (S4), if (\varepsilon\ge1/4), then

\[
 -\frac n2+2n\varepsilon\ge0,
\]

and every other term is nonnegative.

Since (n\ge1) and (r\ge1/2), one has (q\ge3/2).  The radius-average
formula

\[
 G_{q+1}(q)=\frac1\pi\int_q^{q+1}
 \sqrt{1-\frac{q^2}{a^2}}\,da
\]

shows that this quantity decreases with (q), and the already audited
endpoint estimate gives

\[
 h=G_\mu(q)\le G_{q+1}(q)\le G_{5/2}(3/2)<\frac15.
 \tag{3.2}
\]

If (B\ge2), strict counting implies (v>7/4).  Using (v-h=A(q)),

\[
 \varepsilon=v-h-\frac34>1-h>\frac45,
\]

so this sector lies inside the already proved remainder-rich case.

It remains to describe (B=0) and (B=1).

If (B=0), then (v\le3/4), whereas (v-h=A(q)\ge3/4).  Hence

\[
 v=\frac34,\qquad h=0,\qquad q=\mu,\qquad
 \varepsilon=0,\qquad Q=0,\qquad\chi_q=1.
 \tag{3.3}
\]

The (B=0) top triangle in (T1) gives

\[
 D_A(q)\ge\frac{9}{16\beta}.
 \tag{3.4}
\]

Therefore this endpoint phase is reduced to

\[
 \boxed{
 \Psi_0:=
 \frac{9}{16\beta}+1-\frac n2
 +2\int_0^n u\sigma(r+u)\,du\ge0.}
 \tag{3.5}
\]

If (B=1), let (\theta=\theta_1),

\[
 y_1=K\cos\theta-q,
 \qquad \eta=y_1-[y_1]_<.
\]

Put

\[
 L_1=\frac\pi{2\theta}+2\eta-Q-2\delta
 +\frac{(v-1)_+^2}{\beta}.
 \tag{3.6}
\]

Then (S4), (T2), and one-interface nonnegativity reduce the entire one-level
phase to

\[
 \boxed{
 \Psi_1:=
 \max\{0,L_1\}-\frac n2+2n\varepsilon
 +2\int_0^n u\sigma(r+u)\,du+\chi_q\ge0.}
 \tag{3.7}
\]

Here the exact phase data are:

\[
 \begin{array}{c|c|c}
 \text{phase}&(Q,\chi_q)&\text{conditions}\\ \hline
 \text{open}&(1,0)&0<\varepsilon<1/4,\\
 \text{lower noncorner}&(0,1)&\varepsilon=0,\ h>0,\\
 \text{corner}&(0,1)&\varepsilon=h=0\quad(B=0).
 \end{array}
 \tag{3.8}
\]

This proves the stated reductions and the (B\ge2) closure.

### 3.4 Equality-face audit

- (A(q)+1/4=1) is not obtained from the open phase by continuity.  It has
  (Q=0) and (\chi_q=1).
- (q=\mu) has (h=\delta=0).  If also (v=3/4), then (B=0) and
  (3.5) owns the corner.
- If (y_1\in\mathbb N), then (\eta=1); the equality sample is absent.
- If (v+1/4\in\mathbb N), use the literal strict (B) and the top term.
- If (r+j=K), the sample is absent.

### 3.5 Loss ledger

The (B\ge2) closure uses no terminal quantitative loss; it uses only
(D_A(q)\ge0).  Equations (3.5) and (3.7) discard the inverse tangent gaps
(1.7).  Replacing (2\delta) in (3.6) by (\alpha h) would additionally
discard (\alpha h-2\delta).  No (\eta) or (\chi_q) term is discarded.

### 3.6 Counterexample search

The current Mathematica run retained 6,409 dimension-active no-drop records.
Almost all hard records had (B=1).  At the published difficult point

\[
 (\rho,K,r)=(0.454,5.754,1/2),
\]

it reproduces

\[
 D_A(r)\approx0.5738317850,
 \qquad R_2\approx-0.3789316951,
\]

while the strengthened one-level lower scalar is only

\[
 \Psi_1\approx0.06731289939.
\]

Thus the true inequality has substantial reserve, but the tangent reduction
still loses about (0.51) there.  No negative (\Psi_1) was found.  A
separate deterministic high-precision (B=0) half-grid evaluation through
(q=80) retained 1,197 active cases and found no negative (3.5).  The root
solves are numerical, so this is neither an exact enumeration nor an interval
certificate.  These are theorem-design facts only.

### 3.7 Failure report

The first-floor theorem is still open.  Its precise residual is:

1. prove (3.5) on the endpoint corner; and
2. prove (3.7) in the open and lower-noncorner (B=1) phases.

The observed extremal pattern for (3.7) is

\[
 \varepsilon\downarrow0,
 \qquad \eta\downarrow0
 \quad\text{from the open side},
\]

with a negative head (R_n).  This is exactly the simultaneous shell-level
and ball-spatial wall configuration that must be treated correlatively.  The
next proof attempt should retain the exact ball tangent gaps (1.7), or prove
an elasticity estimate forcing (\eta), the top interval, or the shell head
to pay when both remainders approach their bad walls.

## 4. High-floor first-drop CST target

### 4.1 Statement

For a dimension-labelled shift

\[
 r=r_m=m+\frac{d-2}{2},
 \]

call the configuration active only when

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}
 +\frac{(d-2)^2-1}{4}.
 \tag{4.1}
\]

The high-floor first-drop target is:

> If (F_0=f\ge2) and (p<n), then every active configuration satisfies
> \[
> \boxed{
> D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\ge0.}
> \tag{CST-H}
> \]

No (\chi_q) term is needed because (p<n).

### 4.2 Dependencies

- (S1)--(S3);
- WP1;
- the proved shell elasticity inequality;
- the complete one-interface theorem.

### 4.3 Proof

Open.  Equation (2.3) is the current single lower scalar.  No ratio
subdivision is introduced in this note.

### 4.4 Equality-face audit

All action, inverse-spatial, interface, and outer-support walls must use the
literal strict values listed in Sections 1.4 and 2.4.  The active equality
face in (4.1) belongs to the dimension-dependent no-mode theorem.

### 4.5 Loss ledger

Before any CST-H proof, the four losses listed in Section 2.5 must be measured
at the candidate extremum.  In particular, shelf and terminal losses may not
be maximized independently.

### 4.6 Counterexample search

No new high-floor search is asserted here.  The prior broad diagnostic found
no counterexample to (D_A(r)\ge0), but that does not test the lower surrogate
(\Phi_\delta).  The Mathematica evaluator must be extended to first-drop
records before CST-H casework begins.

### 4.7 Failure report

The exact missing theorem is a quantitative elasticity-to-level transport:
a poor value of

\[
 \mathcal C_p+p(\varepsilon_0+\varepsilon_p-1/2)
\]

must force a compensating increase in (B-Q), (\sum\eta_k), the top
interval, or an exact terminal tangent gap.  This implication has not yet
been proved.

## 5. Gate decision and next round

The gate remains on the analytic CST route, for three reasons.

1. WP1 is now a complete analytic lemma.
2. The restored fractional term repairs a genuinely negative old surrogate.
3. No counterexample to the new no-drop surrogate has been found, and its
   difficult phase is sharply localized.

The next round is therefore:

1. prove the corner inequality (3.5), preferably by the zero-level triangle
   plus an exact small-angle/head comparison;
2. retain the exact tangent gaps (1.7) in the (B=1) scalar and prove (3.7),
   testing the simultaneous (\varepsilon,\eta\downarrow0) face first;
3. only after WP2 closes, extend the Mathematica evaluator to the high-floor
   first-drop surrogate and attack CST-H;
4. if the strengthened lower surrogate is falsified, switch to the exact
   reduced scalar (\mathscr S), then to the weighted aggregate WT before
   considering one compact certificate.

No manuscript rewrite is authorized yet.  The 82-page general-dimensional
manuscript remains the frozen research archive until the standalone CST note
closes its gate.

## 6. Reproduction

Mathematica was invoked through the installed Wolfram 15.0 console binary:

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\SystemFiles\Kernel\Binaries\Windows-x86-64\wolframscript.exe' `
  -noprompt -run '<<computations/general_d_fractional_terminal_probe.wl;Quit[]'
```

The script prints `diagnosticOnly=True`; its floating/high-precision results
are not proof premises.
