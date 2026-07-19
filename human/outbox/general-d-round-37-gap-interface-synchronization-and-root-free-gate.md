# General dimension, Round 37: gap-interface synchronization and an exact normal form

Date: 19 July 2026  
Status: exact analytic reduction proved; the residual gap sign remains open

## 0. Statement and theorem boundary

This note follows
`human/inbox/general-d_simplified_analytic_strategy.md`. It introduces no
ratio threshold, count ladder, chamber certificate, or empirical theorem
constant. Its primary result is a lossless normal form for the already
selected Round28--36 scalar. A count-free sawtooth projection is retained
only as an optional sufficient corollary.

Work in the exact high-floor first-drop hard sector:

\[
 f\geq2,\qquad q=r+p+m,\qquad \mu=q+\alpha,
 \qquad 0\leq\alpha<1,
\]

\[
 c=\frac t\pi,\qquad d=1-2c,\qquad K=\mu\sec t,
\]

and

\[
 p>dm,\qquad 0\leq E<E_*:=\frac{p-dm}{2p}.
\tag{0.1}
\]

Put

\[
 W=G_K(\mu)=f-\frac14-\lambda,
 \qquad B_0=[W+\tfrac14]_<=[f-\lambda]_<,
 \qquad \lambda>0,
\tag{0.2}
\]

and retain the Round36 terminal data

\[
 h=G_\mu(q),\qquad v=G_K(q),\qquad
 Q=[v-h+\tfrac14]_<,\qquad B=[v+\tfrac14]_<,
\tag{0.3}
\]

\[
 J=2\int_q^\mu G_\mu(z)\,dz.
\tag{0.4}
\]

The one-level-gap branch is

\[
 B=Q+1.
\tag{0.5}
\]

Round36 already closes this branch when \(p-dm\leq12/7\). The live use of
the reductions below is therefore the residual part \(p-dm>12/7\), although
the reductions themselves hold on the whole gap branch.

### Theorem 0.1 (gap-interface synchronization)

Every point with \(0<\alpha<1\) on the gap branch, together with its
one-sided outer, \(Q\), inverse, and alpha-endpoint limits, satisfies

\[
 \boxed{B_0=B-1.}
\tag{0.6}
\]

Consequently, with the intrinsic action deficit

\[
 j:=f-B\in\mathbb Z_{\geq0},
\tag{0.7}
\]

one has the single strict-floor band

\[
 \boxed{B_0=f-j-1,\qquad j\leq\lambda<j+1.}
\tag{0.8}
\]

Moreover, at every literal gap point and on the \(Q\)-, inverse-, and
upper-alpha limit faces, the newest outer level has a unique inverse
displacement

\[
 \boxed{0<y_B<\alpha<1,\qquad \eta_B=y_B.}
\tag{0.9}
\]

On the outer-\(B\) closure this weakens only to
\(0\leq y_B<\alpha<1\), with boundary value \(y_B=0\); on the collapsed
gap-side limit \(\alpha\downarrow0\), one has
\(y_B\to0\) and \(\eta_B\to0\). Thus (0.9) is not being asserted with
strict inequalities at those two closure points.

This is not a subdivision by \(B\). It eliminates the independent interface
count, synchronizes it with the action deficit, and locates the newest
fractional inverse level on every gap face.

### Proposition 0.2 (the hard gap has a positive interface count)

Every hard gap point satisfies

\[
 \boxed{B_0=Q\geq1,\qquad B\geq2.}
\tag{0.10}
\]

This is a sublevel extension of the Round34--35 lower-\(Q\) argument, proved
in Section 2.1. It removes the only possible zero-interface-count gap without
a numerical check.

### Theorem 0.3 (lossless normal form for the selected gap scalar)

Let

\[
 \mathfrak s=
 \sqrt{1+\frac{p(2r+p)}{X(X+2r+2p)}},
 \qquad X=m+\alpha,
\]

\[
 a_p=\frac{p^2}{3(2r+p)},\qquad
 \tau=\frac{\mathfrak s-1}{\mathfrak s+1},
\tag{0.11}
\]

and let

\[
 M_4=\max\{\tau(E+2\lambda),\mathcal K_4\}
\tag{0.12}
\]

be the exact Round28 projected shelf payment. Define

\[
 \Xi:=E-M_4
\tag{0.13}
\]

and

\[
 \begin{aligned}
 \Omega:={}&
 \sum_{k=1}^{B_0}
 \left(
  \frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k
 \right)\\
 &+
 \sum_{k=B_0+1}^{B}
 \left(
  \frac\pi{2\theta_k}-1+2\eta_k
 \right).
 \end{aligned}
\tag{0.14}
\]

Then

\[
 \boxed{\Xi\geq0,\qquad \Omega>0,}
\tag{0.15}
\]

the terminal top interval vanishes identically, and the selected scalar has
the exact normal form

\[
 \boxed{
 \begin{aligned}
 \Gamma_{\mathrm{gap}}
 :={}&1-J+
 \sum_{k=1}^{B}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 +a_pM_4+p(E-E_*)\\
 ={}&
 1-J+\frac{B_0d}{2c}+\Omega
 +(p+a_p)M_4+p\Xi-\frac{p-dm}{2}.
 \end{aligned}}
\tag{0.16}
\]

On the gap, \(L_T>6/7\) and the top interval is zero, so the clipping in
the Round28 scalar is inactive and

\[
 D_A(r)\geq\Phi_\delta^+
 \geq\Psi^{L_T}_{4,E}
 =\Gamma_{\mathrm{gap}}.
\tag{0.17}
\]

The identity (0.16), rather than an independently worst-cased collection of
its terms, is the next analytic object.

### Corollary 0.4 (one exact-shelf, count-free gate)

Put

\[
 g=\mathfrak s-1,\qquad
 \zeta=\frac d{2c},\qquad
 A_*=(p+a_p)g,
\tag{0.18}
\]

and let

\[
 \{\lambda\}:=\lambda-\lfloor\lambda\rfloor\in[0,1)
\tag{0.19}
\]

be the ordinary fractional part. Write \(x=r+p\), and put

\[
 R_1=
 \frac{\sqrt{\mu^2-r^2}-\sqrt{\mu^2-x^2}}
 {\sqrt{\mu^2-x^2}-\sqrt{\mu^2-q^2}}.
\tag{0.20}
\]

Define the three correlated shelf payments

\[
 \mathcal S_{\mathrm{el}}
 =(f-1)\min\{\zeta,A_*\}
 +A_*\bigl(\{\lambda\}+e_p\bigr),
\tag{0.21}
\]

\[
 \mathcal S_{\mathrm{curv}}
 =\zeta+(p+a_p)\mathcal K_4,
\tag{0.22}
\]

\[
 \mathcal S_{\mathrm{adj}}
 =(f-1)\min\{\zeta,(p+a_p)R_1\}
 +(p+a_p)R_1e_p.
\tag{0.23}
\]

Then the stronger exact endpoint scalar satisfies the single \(B\)-free
bound

\[
 \boxed{
 \Phi_\delta^+>
 \mathcal H_\Delta:=
 1-J+\max\{
 \mathcal S_{\mathrm{el}},
 \mathcal S_{\mathrm{curv}},
 \mathcal S_{\mathrm{adj}}
 \}
 +2pe_p-\frac{p-dm}{2}.}
\tag{0.24}
\]

Thus \(\mathcal H_\Delta\geq0\) is one sufficient gate with no \(B\)-,
\(Q\)-, \(B_0\)-, or \(j\)-indexed theorem and no inverse roots. It retains
the literal action fractional part, the actual lower-shelf remainder, the
quartic alternative, and the adjacent-action correlation. No sign for
\(\mathcal H_\Delta\) is asserted here.

## 1. Dependencies

Only the following promoted results are used.

1. Round10: the complete fractional terminal formula.
2. Round21: \(J<1/7\), the interface action coordinate
   \(\lambda>0\), and exact shelf elasticity.
3. Rounds27--28: the hard-sector scalar,
   \(\Delta\geq\tau(E+2\lambda)\),
   \(\Delta>\mathcal K_4\), and the implication from the selected scalar to
   the exact shifted tail.
4. Rounds34--35: the common-radial-parameter adjacent-action identity, the
   normalized domain (3.16), its transport, and the proved sign
   \(C>E_*\) on that domain.
5. Round36: \(B-Q\in\{0,1\}\), \(0\leq Q\leq B\leq f\), the exact gap
   rewrite, and all one-sided wall conventions.

All new steps below are monotonicity of the strict bracket, elementary ball
action calculus, and exact algebra.

## 2. Proof of gap-interface synchronization

The gap is impossible at the literal face \(\alpha=0\), because then
\(h=0\) and \(B=Q\). Hence \(0<\alpha<1\) on every literal gap point.

At the interface, the inner ball action vanishes:

\[
 A(\mu)=G_K(\mu)=W.
\tag{2.1}
\]

The shell action is strictly decreasing on \(0<z<\mu\). Since \(q<\mu\),

\[
 A(q)>A(\mu)=W.
\tag{2.2}
\]

The strict bracket is nondecreasing. Equations (0.2), (0.3), and (2.2)
therefore give

\[
 B_0\leq Q=B-1.
\tag{2.3}
\]

On the other hand,

\[
 v-W
 =\int_q^\mu \frac1\pi\arccos\frac zK\,dz.
\tag{2.4}
\]

The integrand lies strictly between \(0\) and \(1/2\), and
\(\mu-q=\alpha<1\). Thus

\[
 0<v-W<\frac\alpha2<\frac12<1.
\tag{2.5}
\]

If two real numbers differ by less than one, their strict integer brackets
can differ by at most one. Hence

\[
 B-B_0\leq1.
\tag{2.6}
\]

Combining (2.3) and (2.6) proves \(B_0=B-1\).

Round36 gives \(B\leq f\), so \(j=f-B\) is a nonnegative integer. Finally,

\[
 B-1=B_0=[f-\lambda]_<
\]

means, with literal strict-wall ownership,

\[
 B-1<f-\lambda\leq B.
\tag{2.7}
\]

Substituting \(B=f-j\) into (2.7) gives
\(j\leq\lambda<j+1\), including the lower endpoint and excluding the upper
endpoint exactly as required by \([N]_< =N-1\).

For the newest root, \(Q=B-1\) implies

\[
 A(q)\leq B-\frac14.
\tag{2.8}
\]

Together with \(A(q)>W\), this gives \(W<B-1/4\). The outer gap count gives
\(v>B-1/4\). Since \(G_K\) is strictly decreasing, there is a unique
\(z_B\in(q,\mu)\) with

\[
 G_K(z_B)=B-\frac14.
\]

Thus \(y_B=z_B-q\) lies in \((0,\alpha)\), its strict integer bracket is
zero, and \(\eta_B=y_B\). This proves (0.9).

At the collapsed one-sided limit \(\alpha\downarrow0\), one has \(W=v\)
and the gap-side labels satisfy \(B_0=Q=B-1\). The literal simultaneous
\(B/Q\) corner is equal-count and remains excluded.

### 2.1 Sublevel extension excluding \(B_0=0\)

Assume for contradiction that a hard gap point has \(B_0=0\). The
synchronization theorem gives

\[
 (B,Q)=(1,0).
\tag{2.9}
\]

The literal strict count \(Q=0\) implies \(A(q)\leq3/4\), while (2.2)
gives

\[
 W<A(q)\leq\frac34.
\tag{2.10}
\]

Put \(x=r+p\). Since \(A(x)=f-1/4+e_p\),

\[
 A(x)-A(q)\geq f-1+e_p\geq f-1\geq1.
\tag{2.11}
\]

These are exactly the two consequences of the syntactically stated
lower-\(Q\) wall used in the Round34 normalized-domain proof: the strict
interface bound \(W<3/4\) and the adjacent action drop
\(A(x)-A(q)\geq1\). The wall equality \(A(q)=3/4\) is not used after
those consequences are formed.

For completeness, let \(\kappa=\cos t\), so there is no conflict with the
present notation \(c=t/\pi\). The Round34 common-radial-parameter identity

\[
 -A'(z)=\frac1\pi\int_\kappa^1
 \frac{z}{\sqrt{\mu^2-s^2z^2}}\,ds
\tag{2.12}
\]

and (2.11) give the same strict adjacent-action comparison and trapezoid
upper bound as in that proof. Equation (2.10) supplies the same upper scale
bound

\[
 \mu<\frac{3\pi}{4(\tan t-t)}.
\tag{2.13}
\]

The Jensen lower quadrature, combined with the same action lower bound,
therefore places the normalized variables

\[
 z=\frac r\mu,\qquad P=\frac p\mu,\qquad M=\frac m\mu
\]

in the exact Round34 domain (3.16) and gives

\[
 \Delta>C(z,P,M,t).
\tag{2.14}
\]

Here \(z,P,M>0\), \(z+P+M=q/\mu<1\), and the hard inequality gives
\(P>dM\). Round34 transport and every phase module in Round35 depend only
on this normalized domain, not on the discarded wall equality. The proved
Round35 sign therefore applies unchanged:

\[
 C(z,P,M,t)>E_*.
\tag{2.15}
\]

Equations (2.14)--(2.15) give \(\Delta>E_*\). But
\(E-\Delta=2e_p\geq0\), so \(E>E_*\), contradicting (0.1).
Therefore \(B_0\geq1\). Since (0.6) also gives \(Q=B_0\) and
\(B=B_0+1\), Proposition 0.2 follows.

## 3. The top interval and exact inverse decomposition

The strict relation \(Q=B-1\) gives

\[
 A(q)\leq B-\frac14.
\]

Round36 proves \(0<h<1/4\) for \(\alpha>0\). Hence

\[
 v=A(q)+h<B.
\tag{3.1}
\]

Therefore

\[
 \boxed{\frac{(v-B)_+^2}{\beta}=0}
\tag{3.2}
\]

on the whole gap branch. No top payment is being discarded.

For \(1\leq k\leq B_0\), strict counting gives

\[
 k-\frac14<W=G_K(\mu).
\tag{3.3}
\]

The ball action is strictly increasing in its angle variable. Since the
interface angle is \(t\), (3.3) implies

\[
 0<\theta_k<t.
\tag{3.4}
\]

Consequently every summand in the first sum defining \(\Omega\) is
strictly positive. For \(k>B_0\), one has \(0<\theta_k<\pi/2\), so every
summand in the second sum is strictly positive as well, including an
adverse inverse side with \(\eta_k=0\). Thus \(\Omega>0\).

Finally,

\[
 \frac\pi{2t}-1
 =\frac{1-2t/\pi}{2t/\pi}
 =\frac d{2c}.
\tag{3.5}
\]

Adding and subtracting \(\pi/(2t)\) for exactly the first \(B_0\) levels
gives

\[
 \boxed{
 \sum_{k=1}^{B}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 =\frac{B_0d}{2c}+\Omega.}
\tag{3.6}
\]

This retains the newest fraction \(2y_B\); it is not bounded separately.

## 4. Exact shelf decomposition

On the first shelf \(e_p\geq0\), hence

\[
 E-\Delta=2e_p\geq0.
\tag{4.1}
\]

Round28 gives

\[
 \Delta\geq\tau(E+2\lambda),
 \qquad
 \Delta>\mathcal K_4.
\tag{4.2}
\]

By the definition (0.12),

\[
 \Delta\geq M_4.
\tag{4.3}
\]

Combining (4.1) and (4.3) proves

\[
 \boxed{\Xi=E-M_4\geq0.}
\tag{4.4}
\]

The shelf part now has the exact identity

\[
 \boxed{
 a_pM_4+pE=(p+a_p)M_4+p\Xi.}
\tag{4.5}
\]

For later comparison, \(M_4\geq\tau(E+2\lambda)\) and
\(E\geq M_4\) imply

\[
 M_4\geq\tau(M_4+2\lambda).
\]

Solving with \(\tau=g/(g+2)\) gives

\[
 \boxed{M_4\geq\max\{g\lambda,\mathcal K_4\}.}
\tag{4.6}
\]

## 5. Proof of the normal form and exact-shelf gate

On the gap, Round36 rewrites the complete terminal expression as

\[
 L_T=
 1-J+
 \sum_{k=1}^{B}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 +\frac{(v-B)_+^2}{\beta}.
\tag{5.1}
\]

Equations (3.2) and (3.6) turn this into

\[
 L_T=1-J+\frac{B_0d}{2c}+\Omega>\frac67.
\tag{5.2}
\]

Thus \(\max\{0,L_T\}=L_T\). Also

\[
 p(E-E_*)=pE-\frac{p-dm}{2}.
\tag{5.3}
\]

Substituting (4.5), (5.2), and (5.3) into the Round28 selected scalar proves
the exact normal form (0.16) and the implication chain (0.17).

For the stronger endpoint scalar, use \(E=\Delta+2e_p\) to write exactly

\[
 \begin{aligned}
 \Phi_\delta^+
 ={}&L_T+a_p\Delta+p(E-E_*)\\
 ={}&1-J+\Omega+
 \left\{B_0\zeta+(p+a_p)\Delta\right\}
 +2pe_p-\frac{p-dm}{2}.
 \end{aligned}
\tag{5.4}
\]

It remains to give three correlated lower bounds for the expression in
braces.

First, the exact Round21 shelf elasticity is

\[
 \Delta\geq g(\lambda+e_p).
\tag{5.5}
\]

By (0.8),

\[
 j=\lfloor\lambda\rfloor,\qquad B_0=f-1-j.
\tag{5.6}
\]

Set \(n=f-1\). With \(A_*=(p+a_p)g\), exact algebra gives

\[
 \begin{aligned}
 B_0\zeta+(p+a_p)\Delta
 &\geq(n-j)\zeta+
 A_*\bigl(j+\{\lambda\}+e_p\bigr)\\
 &\geq n\min\{\zeta,A_*\}
 +A_*\bigl(\{\lambda\}+e_p\bigr)
 =\mathcal S_{\mathrm{el}}.
 \end{aligned}
\tag{5.7}
\]

The last inequality follows at once by considering the sign of
\(A_*-\zeta\); it is one minimum formula, not a theorem split.

Second, Proposition 0.2 gives \(B_0\geq1\), while Round28 gives
\(\Delta>\mathcal K_4\). Hence

\[
 B_0\zeta+(p+a_p)\Delta
 >\zeta+(p+a_p)\mathcal K_4
 =\mathcal S_{\mathrm{curv}}.
\tag{5.8}
\]

Third, define the literal terminal remainder

\[
 \xi=A(q)+\frac14-Q\in(0,1].
\tag{5.9}
\]

Since \(Q=B_0=f-j-1\),

\[
 A(x)-A(q)=j+1+e_p-\xi\geq j+e_p.
\tag{5.10}
\]

The Round34 common-radial-parameter proof is valid for this actual action
drop and gives

\[
 \Delta>R_1\{A(x)-A(q)\}\geq R_1(j+e_p).
\tag{5.11}
\]

Put \(H_*=(p+a_p)R_1\). The same one-line minimum algebra used in (5.7)
now yields

\[
 \begin{aligned}
 B_0\zeta+(p+a_p)\Delta
 &>(n-j)\zeta+H_*(j+e_p)\\
 &\geq n\min\{\zeta,H_*\}+H_*e_p
 =\mathcal S_{\mathrm{adj}}.
 \end{aligned}
\tag{5.12}
\]

The term \(\Omega\) in (5.4) is strictly positive. Therefore (5.7),
(5.8), and (5.12) combine before any term is discarded:

\[
 \Omega+B_0\zeta+(p+a_p)\Delta
 >
 \max\{
 \mathcal S_{\mathrm{el}},
 \mathcal S_{\mathrm{curv}},
 \mathcal S_{\mathrm{adj}}
 \}.
\tag{5.13}
\]

Substitution in (5.4) proves (0.24).

At an integer \(\lambda\), the literal interface wall has
\(\{\lambda\}=0\) and the lower \(B_0\). On the opposite
\(\lambda\to N^-\) side, the fractional reserve tends to one while
\(B_0\) is higher. Thus \(\mathcal S_{\mathrm{el}}\) has the correct
one-sided ownership. At the literal \(Q\)-wall, \(\xi=1\), so (5.10)
also has the correct lower-count owner.

## 6. Equality-face audit

1. **Ordinary action wall.** If
   \(A(r+\ell)+1/4\in\mathbb N\), the ordinary shelf owner retains the
   literal integer. Equations (4.1)--(4.5) use the resulting
   \(e_p\geq0\) without moving to the adverse side. This includes
   \(e_p=0\) and simultaneous ordinary shelf walls.
2. **Literal interface face.** Since
   \(\mu-r=p+m+\alpha\), the condition
   \(\mu-r\in\mathbb N\) in this chart is \(\alpha=0\). There \(h=0\)
   and \(B=Q\), so no literal gap point exists.
3. **Upper alpha endpoint.** The limit \(\alpha\uparrow1^-\), equivalently
   \(q+1\uparrow\mu\), is a separate one-sided reindex limit. It is not
   identified with the literal \(\alpha=0\) point of the next chart.
4. **Outer \(B_N\) wall.** The literal wall owns the lower count. The
   formulas apply to its one-sided gap-side bad limit, exactly as in
   Round36. The newest \(y_B=0\) limit is already the outer-action jump and
   is not charged as a second inverse jump.
5. **\(Q_N\) wall.** The literal strict value is \(Q=N-1\), so it remains
   the gap owner. Its phase-right side is equal-count and is not imported.
6. **Old inverse wall.** The literal wall has \(\eta_k=1\); its adverse
   side has \(\eta_k\downarrow0\). Both are represented exactly in
   \(\Omega\).
7. **First-shelf turning wall.** A first-shelf sample
   \(r+\ell=K\) would have zero outer action and cannot carry the
   high-floor owner \(f\geq2\).
8. **Terminal turning wall.** A terminal point \(q+\ell=K\) cannot carry
   an inverse level \(k\geq1\), because \(G_K(K)=0<k-1/4\).
9. **Hard wall.** The equality \(p=dm\) belongs to the automatic sector.
   The live residual has \(p-dm>12/7\).
10. **Collapsed gap limit.** The \(\alpha\downarrow0\) gap-side labels
    obey \(B_0=Q=B-1\), but the literal simultaneous \(B/Q\) corner is
    equal-count and belongs to the separate Round36 residual class.

## 7. Loss ledger

The identity (0.16) discards no term from
\(\Gamma_{\mathrm{gap}}\):

- the terminal top interval is exactly zero;
- every complete angle and inverse fraction is retained in \(\Omega\);
- the projected shelf payment is retained in \(M_4\);
- the excess \(E-M_4\) is retained in \(\Xi\);
- the exact cap \(J\) is retained.

The passage from the exact shifted tail \(D_A(r)\) to the selected
Round28 scalar is inherited from earlier proved tangent and shelf-curvature
inequalities. If the selected scalar resists, those inherited losses must be
restored by returning to \(\mathscr S\).

The exact-shelf gate \(\mathcal H_\Delta\) starts from the stronger
\(\Phi_\delta^+\), but it discards \(\Omega\) after forming the three
correlated lower payments in (5.7), (5.8), and (5.12). It also replaces the
actual \(\Delta\) by their maximum. It does not discard \(e_p\), the
fractional action \(\{\lambda\}\), the quartic alternative, or the exact
cap \(J\).

Replacing \(J\) by \(1/7\) would discard the additional positive margin
\(1/7-J\); that replacement is not made in the primary target.

The fractional reserve \(A_*\{\lambda\}\) is not discarded. A diagnostic
continuous relaxation that replaces \(B_0\) by \(W-3/4\) while dropping
this sawtooth reserve is negative at a valid sampled gap tuple, so that
relaxation is not a theorem target.

## 8. Counterexample search

The reproducible diagnostic

`computations/general_d_round37_gap_rootfree_diagnostic.py`

tests (0.6), (0.8), the projected root-free ordering, and the actual
selected gap scalar on finite owner/wall samples inherited from the Round27
evaluator. It uses ordinary floating-point arithmetic and is theorem-design
evidence only.

No sampled violation of the proved identities or inequalities was found.
The smallest observed gate values occur near the smallest interface-count
scale and the \(\alpha\uparrow1^-\) outer-action endpoint. Small positive
\(\alpha\), large-radius \(E\downarrow0\), lower-shelf, and old inverse
patterns remain diagnostic tests rather than continuum owners. No sampled
margin is used in Sections 2--5.

The companion Mathematica file

`computations/general_d_round37_gap_interface_replay.wl`

checks the algebraic identities in the normal form and sawtooth projection.
It is an exact symbolic replay, not a sign certificate; the strict-bracket
argument is printed in Section 2 rather than hidden in the replay.

## 9. Exact failure report and next gate

The actual theorem obligation is \(D_A(r)\geq0\). In the present exact
endpoint chain it is sufficient to prove

\[
 \boxed{\Phi_\delta^+\geq0.}
\tag{9.1}
\]

The selected projected target \(\Gamma_{\mathrm{gap}}>0\) is a sufficient
subtarget, not the exact shifted tail. By the lossless identity (0.16), a
nonpositive \(\Gamma_{\mathrm{gap}}\) point would satisfy exactly

\[
 \boxed{
 p-dm\geq
 2(1-J)+\frac{B_0d}{c}
 +2\Omega+2(p+a_p)M_4+2p\Xi.}
\tag{9.2}
\]

Since \(J<1/7\), it would in particular have to satisfy

\[
 \boxed{
 p-dm>
 \frac{12}{7}+\frac{B_0d}{c}
 +2\Omega+2(p+a_p)M_4+2p\Xi.}
\tag{9.3}
\]

This is the exact residual pattern exposed by Round37. It strengthens the
bare Round36 threshold \(p-dm>12/7\) without independently worst-casing the
interface reserve, inverse fractions, curvature, and actual shelf excess.

Independently, the single count-free gate in Corollary 0.4 fails to close
only where

\[
 \boxed{
 \frac{p-dm}{2}>
 1-J+\max\{
 \mathcal S_{\mathrm{el}},
 \mathcal S_{\mathrm{curv}},
 \mathcal S_{\mathrm{adj}}
 \}+2pe_p.}
\tag{9.4}
\]

Inequality (9.4) is the exact failure condition for that sufficient gate:
equality already closes because \(\Phi_\delta^+>\mathcal H_\Delta\). It is
not asserted to describe a counterexample to \(D_A(r)\).

The next analytic pass should attack (9.1)--(9.4) on the already transported
outer, inverse, lower-shelf, and alpha-endpoint faces, preserving
\(\Omega\), \(\Xi\), \(e_p\), the fractional action, and

\[
 W=\frac\mu\pi(\tan t-t)=f-\frac14-\lambda.
\]

It must not split the problem into a sequence indexed by \(B\), \(j\), or
shell-ratio intervals.

If this exact selected face does not close, the revised strategy requires
returning to

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2},
\]

which restores the exact shelf trapezoid and terminal surplus inherited from
the earlier reduction. If that exact shifted-tail face still resists, the
next live target is the weighted aggregate with the branching bonus. No
second compact certificate is authorized.

High-floor CST, pointwise assembly, the weighted aggregate, and the
all-dimensional theorem therefore remain open.
