# Independent audit of General-dimensional Round 33

Date: 19 July 2026

Decision: **PASS for strict monotonicity of the exact hard gap on the open
lower-\(Q\) wall and for the stated endpoint localization.  No endpoint
sign, full-\(\Psi\) monotonicity, high-floor CST closure, pointwise
assembly, or all-dimensional theorem is proved.**

Audited artifacts:

- `human/outbox/general-d-round-33-lower-Q-hard-arc-monotonicity-and-endpoint-reduction.md`
- `computations/general_d_round33_lowerQ_monotonicity_replay.wl`

## 1. Claim and scope audit

The theorem concerns the open wall

\[
 A(q)=\frac34,\qquad 0<\alpha<1,
\]

inside one fixed high-floor first-drop and activity cell.  Its monotone
quantity is only

\[
 H(\mu)=E(\mu)-E_*(\mu),
\]

not the complete projected scalar

\[
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*).
\]

The source preserves this distinction in its statement, endpoint section,
and gate decision.  In particular, it leaves the signs on the lower shelf,
the activity exit, and the \(\alpha\to1^-\) exit open.  Thus the phrase
"endpoint reduction" is literal and is not a closure claim.

## 2. Phase and action correlations

Write

\[
 h=G_\mu(q),\qquad v=G_K(q)=\frac34+h,
 \qquad W=G_K(\mu).
\]

For \(q\le z<\mu<K\), the outer phase is strictly larger than the inner
phase.  Since \(\alpha>0\), integration over a nonempty interval gives

\[
 v-W
 =\int_q^\mu\frac{\arccos(z/K)}\pi\,dz
 >\int_q^\mu\frac{\arccos(z/\mu)}\pi\,dz=h.
\]

Therefore

\[
 W<\frac34,
 \qquad
 \mu<\frac{3\pi}{4(\tan t-t)}.
\]

Both inequalities are strict on the open wall.  At the excluded corner
\(\alpha=0\), the correct equality is \(W=3/4\).  The source explicitly
rejects the false lower bracket

\[
 \frac34-\frac t\pi<W.
\]

No equivalent form of that bracket enters the proof.  In fact, the outer
integrand is larger than \(t/\pi\) on \([q,\mu)\), so an attempted bound
of \(v-W\) by \(\alpha t/\pi\) has the opposite orientation.

The first-shelf remainder is also retained correctly.  With

\[
 e_p=A(x)+\frac14-f\ge0,
\]

the lower-\(Q\) equation gives the load-bearing action gap

\[
 A(x)-A(q)=f-1+e_p\ge1.
\]

This is an owner condition, not a consequence of the bare lower-\(Q\)
geometry, and the proof does not discard it.

## 3. Derivative and factorization audit

Implicit differentiation of \(A(q)=3/4\) gives

\[
 \kappa=\frac{dK}{d\mu}
 =\frac{\sin\phi}{\sin\psi}\in(0,1).
\]

With \(c=\cos t\), \(a=1-\kappa c>0\), and

\[
 D(z)=S_\mu(z)-\kappa S_K(z),
\]

the audited derivatives are

\[
 A(z)'=-\frac{D(z)}\pi,
 \qquad
 t'=-\frac{a}{\mu\tan t},
\]

and hence

\[
 \pi H'
 =-D(r)-D(x)+\frac mp\frac{a}{\mu\tan t}.
\]

All signs agree with increasing \(\mu\): \(K\) increases and \(t\)
decreases.

Set

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 V_z=\sqrt{\mu^2-c^2z^2}.
\]

The wall relation is \(\kappa=U_q/V_q\).  Direct expansion gives the exact
identity

\[
 U_z^2-\kappa^2V_z^2
 =a(1+\kappa c)(q^2-z^2).
\]

Rationalization at \(x\) therefore yields

\[
 D(x)=
 \frac{a(1+\kappa c)(q^2-x^2)}
 {\mu(U_x+\kappa V_x)}.
\]

Since \(U_x<V_x\), \(0<\kappa<1\), and

\[
 2(1+\kappa c)-(1+\kappa)
 =1-\kappa+2\kappa c>0,
\]

the strict bound

\[
 D(x)>\frac{a(q^2-x^2)}{2\mu V_x}
\]

is correctly oriented.

## 4. Radial-gap and trigonometric audit

The exact shell slope is

\[
 \sigma(z)
 =\frac1\pi\int_c^1
 \frac{z/\mu}{\sqrt{1-s^2z^2/\mu^2}}\,ds.
\]

The integrand is strictly smaller than its \(s=1\) endpoint except on a
set of measure zero.  Thus

\[
 \sigma(z)<\frac{(1-c)z}{\pi U_z}.
\]

Combining this strict upper estimate with the non-strict action gap gives

\[
 U_x-U_q>\frac\pi{1-c}.
\]

Together with the strict bound on \(\mu\), this implies

\[
 \frac{U_x+U_q}{V_x}
 >\frac{4F(t)}
 {\sqrt{16c^2F(t)^2+9(1-c)^2\sin^2t}}
 >R(t),
\]

where \(F(t)=\tan t-t\) and

\[
 R(t)=\frac{4F(t)}
 {\sqrt{16F(t)^2+9(1-c)^2\sin^2t}}.
\]

Every strict sign is justified on \(0<\alpha<1\): in particular
\(U_q>0\), \(F(t)>0\), and \(c^2<1\).

The first trigonometric reduction is exact:

\[
 R(t)>\sin t
 \iff
 4(\sin t-t\cos t)>3(1-\cos t)\sin^2t.
\]

For \(u=\tan(t/2)\in(0,1)\), if the difference on the right is denoted by
\(Q(t)\), the precise cleared-denominator estimate is

\[
 \frac{(1+u^2)^3}{8}Q(t)
 >\frac{u^3}{15}
 \left(20-45u+32u^2+7u^4-2u^6+3u^8\right).
\]

It follows from

\[
 \arctan u<u-\frac{u^3}{3}+\frac{u^5}{5}.
\]

The polynomial exceeds

\[
 20-45u+30u^2+7u^4+3u^8,
\]

because \(-2u^6>-2u^2\).  The quadratic part has discriminant \(-375\)
and positive leading coefficient, so the entire lower polynomial is
strictly positive.

For the second comparison, \(\varepsilon=\pi/2-t\) gives

\[
 \frac{2(1-\cos t)}{\pi d(t)\tan t}
 =\frac{\sin\varepsilon\cos\varepsilon}
 {\varepsilon(1+\sin\varepsilon)}
 <\cos\varepsilon=\sin t.
\]

The strict inequality follows from \(0<\sin\varepsilon<\varepsilon\).
Consequently

\[
 D(x)>\frac{a}{d\mu\tan t}.
\]

Since \(p>dm\) and \(D(r)>0\), substitution in the exact derivative gives

\[
 \boxed{\pi H'<-D(r)<0}.
\]

## 5. Endpoint and ownership audit

The increasing-\(\mu\) orientation is correct.  Starting from \(H<0\),
strict decrease prevents the automatic seam \(H=0\) from being reached to
the right.  Also \(E\ge0\) on the first shelf, so \(H<0\) implies
\(E_*>0\), equivalently \(p>dm\).  Thus the separate boundary \(p=dm\)
cannot intervene.  These are two distinct seams and are treated as such.

The remaining exits of the same connected first-drop/activity cell are:

\[
 e_p=0,\qquad \text{activity},\qquad \alpha\to1^-.
\]

Their ownership is:

- the ordinary lower shelf \(e_p=0\) is included;
- the activity predicate is strict, so an activity exit is retained as
  the one-sided limit from the feasible activity side, not declared
  automatic;
- \(\alpha=1\) is excluded and contributes its left limit; and
- simultaneous endpoint collisions retain every feasible one-sided value.

On the lower-\(Q\) wall itself, literal strict ownership has \(Q=0\); the
audited candidate is the bad phase-right \(Q=1\) value.  Round 30's
\(0<y_1<\alpha<1\) result excludes inverse-spatial and outer-\(B\)
intersections on the open wall.  No activity-persistence statement is
made or needed.

## 6. Failure-ledger audit

The bare-wall example \(r=p=m=1\), \(\alpha=1/2\) is correctly outside
the high-floor first-drop owner domain.  At the lower-\(Q\) solution,
\(t_Q>\pi/4\), so

\[
 E_*=\frac{t_Q}{\pi}>\frac14,
 \qquad
 g=\sqrt{\frac{15}{11}}-1<\frac14.
\]

The stated curvature comparison is also valid.  Here

\[
 \mathcal K_4
 =\frac1\pi\left\{
 \frac37(1-\cos t)
 +\frac5{343}(1-\cos^3t)\right\}
 <\frac{t}{\pi}=E_*.
\]

Indeed \(1-\cos^3t<3(1-\cos t)\),
\(162/343<1\), and \(1-\cos t<t\).  Thus the example falsifies only the
bare implications \(g\ge E_*\) and \(\mathcal K_4\ge E_*\); it does not
falsify the retained-action theorem.

## 7. Mathematica replay and controls

The installed Mathematica 15 runtime was used to replay the companion
artifact.  Fresh output was

    round33Residuals={0, 0, 0, 0, 0, 0, 0, 0, 0}
    round33LowerQMonotonicityReplayOK=True

The replay checks identities only; the sign proof was audited analytically
above.  Fresh source checks found zero tabs and zero nonprinting control
bytes in both artifacts.  `git diff --check` also passed.

Artifact SHA-256 hashes:

- Round 33 source:
  `ad50eb8f0465b921c81816eca126c5a33207b203d6cf796bcb403836d905c871`
- Mathematica replay:
  `1b064f19b6d5633c0fa9615e1522a6a0d4a58d235ff6e96a06a7271a087bd841`

## 8. Final decision

**PASS** for:

- the strict upper bound \(W<3/4\) on the open lower-\(Q\) wall;
- retention of the first-drop action gap;
- the exact derivative and radial factorization;
- the two strict trigonometric comparisons;
- \(H'(\mu)<0\) throughout a feasible hard lower-\(Q\) arc; and
- localization of its increasing-\(\mu\) exit to the lower shelf,
  activity, or \(\alpha\to1^-\).

**Not proved by Round 33**:

- monotonicity or positivity of the complete projected scalar on the wall;
- positivity at any of the three endpoint families;
- activity persistence;
- closure of the remaining \(\alpha=0\), higher-\(Q\), inverse, or
  simultaneous outer-\(B\) families;
- high-floor CST, pointwise assembly, or the all-dimensional theorem.

The correct next target is the complete correlated sign on the localized
endpoint union, without introducing a new ratio partition or certificate.
