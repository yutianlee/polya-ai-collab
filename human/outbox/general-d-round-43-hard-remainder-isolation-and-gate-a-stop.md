# General-dimensional spherical-shell Pólya project
## Round 43: hard-remainder isolation and the Gate-A stop

**Date:** 20 July 2026  
**Status:** analytic structural advance; Gate A exhausted, Gate B activated

## 0. Theorem boundary and decision

This note revisits only the one-sided outer-\(B\), upper-alpha endpoint

\[
 \chi=h,\qquad y_B=0,\qquad \alpha\uparrow1^-.
\]

Round 42 proved the strict sufficient reduction

\[
 \Phi_\delta^+>\mathcal T_{42},\qquad
 \mathcal T_{42}=
 \frac9{10}+B_0\min\{\zeta,H\}+Hh-\frac{p-dm}{2}.
\tag{R43.1}
\]

It did not sign \(\mathcal T_{42}\).  The exact hard owner also includes
the same-shelf, terminal-crossing, and quantitative hard-remainder data
printed in Section 1 below.  Those conditions were inherited but were not
reprinted in Round 42's abbreviated owner list.

Round 43 proves three things.

1. It gives a sharp, hand-checkable radical lower envelope for \(H\) and
   a strict elementary lower envelope for \(h\).
2. It proves that the count-phase and radial data alone cannot sign
   \(\mathcal T_{42}\), and isolates \(E<E_*\) as the indispensable live
   correlation.
3. It proves the intrinsic fixed-chart transport
   \((E_f-E_*)'(t)>0\), then identifies the unavoidable obstruction:
   synchronizing this transport with the outer count requires an
   \(f\)- or \(B\)-indexed wall analysis.  That is forbidden by the
   binding strategy.

Accordingly the final Gate-A attempt is analytically exhausted.  Gate B is
activated on this resisting face and must restore

\[
 \boxed{\mathscr S=D_A(q)+R_p+\frac{dm}{2}}
\tag{R43.2}
\]

with the exact shelf trapezoid, complete terminal surplus, cap, and inverse
fractions.  This note does not prove the endpoint, high-floor CST, the
general-dimensional branching backbone, or the all-dimensional Pólya
theorem.  It makes no change to `state/proof_obligations.yml`.

The binding methodology remains
`human/inbox/general-d_simplified_analytic_strategy.md` and
`human/inbox/general-d-strategy_r2.md`.  No ratio ladder, count-indexed
theorem family, chamber certificate, or new compact certificate is used.

## 1. Complete exact owner

Retain the Round 42 notation

\[
 x=r+p,\qquad q=x+m,\qquad \mu=q+1,\qquad
 K=\mu\sec t,
\]

\[
 d=1-\frac{2t}{\pi},\qquad
 \zeta=\frac\pi{2t}-1,
\]

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,
 \qquad A(z)=G_K(z)-G_\mu(z).
\]

At the outer wall,

\[
 G_K(q)=B-\frac14,\qquad B_0=B-1\ge1,
\tag{R43.3}
\]

and, with \(W=G_K(\mu)\),

\[
 u=G_K(q)-W,\qquad 0<h<u<\beta<\frac12,
 \qquad h=G_\mu(q),\quad \beta=b_K(q).
\tag{R43.4}
\]

Let \(f\) be the common first-shelf floor and put \(j=f-B\ge0\).  The
literal first-shelf and first-drop conditions are

\[
 [A(r)+\tfrac14]=[A(x)+\tfrac14]=f,
 \qquad [A(x+1)+\tfrac14]\ne f.
\tag{R43.5}
\]

Write

\[
 e_0=A(r)+\frac14-f,\qquad
 e_p=A(x)+\frac14-f,
\]

\[
 \Delta=e_0-e_p=A(r)-A(x),\qquad
 E=e_0+e_p=\Delta+2e_p.
\tag{R43.6}
\]

The hard residual is not merely \(p>dm\).  Its quantitative half is

\[
 \boxed{
 E<E_*:=\frac12-\frac{dm}{2p}=\frac{p-dm}{2p}.}
\tag{R43.7}
\]

The exact live domain consists of (R43.3)--(R43.7), the inherited integer
or half-integer grid, \(p\ge3\), \(p>dm\), and the activity condition.
In particular, a point satisfying the phase equation but failing (R43.5)
or (R43.7) is not a counterexample to (R43.1) on its true owner.

## 2. A sharp radical envelope

Put

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 a_p=\frac{p^2}{3(2r+p)},\qquad
 R_1=\frac{U_r-U_x}{U_x-U_q},\qquad
 H=(p+a_p)R_1.
\]

Rationalizing both differences gives the exact identity

\[
 R_1=
 \frac{p(2r+p)}{m(2x+m)}
 \frac{U_x+U_q}{U_r+U_x}.
\tag{R43.8}
\]

Define

\[
 \underline H:=
 \frac{(p+a_p)p(2r+p)}{m(2x+m)}
 \min\!\left\{\frac{U_x}{U_r},
 \sqrt{\frac{U_q}{U_r}}\right\}.
\tag{R43.9}
\]

### Lemma 2.1

\[
 \boxed{H\ge\underline H.}
\tag{R43.10}
\]

**Proof.**  Set \(a=U_r/U_x>1\), \(b=U_q/U_x<1\), and
\(Q=(1+b)/(1+a)\).  If \(ab\ge1\), then

\[
 Q-\frac1a=\frac{ab-1}{a(1+a)}\ge0.
\]

If \(ab\le1\), then

\[
 Q^2-\frac ba
 =\frac{(a-b)(1-ab)}{a(1+a)^2}\ge0.
\]

Thus \(Q\ge\min\{1/a,\sqrt{b/a}\}\), and (R43.8) proves
(R43.10). \(\square\)

There is also a strict cap bound

\[
 \boxed{h>\underline h:=\frac{U_q^3}{3\pi\mu^2}.}
\tag{R43.11}
\]

Indeed, put \(\theta=\arccos(q/\mu)\).  The difference between the two
sides of (R43.11), multiplied by \(\pi/\mu\), is

\[
 F(\theta)=\sin\theta-\theta\cos\theta
             -\frac{\sin^3\theta}{3}.
\]

Here \(F(0)=0\) and

\[
 F'(\theta)=\sin\theta
 \bigl(\theta-\sin\theta\cos\theta\bigr)>0
\qquad(0<\theta<\tfrac\pi2).
\]

Consequently

\[
 \mathcal T_{42}>
 \frac9{10}+B_0\min\{\zeta,\underline H\}
 +\underline H\,\underline h-\frac{p-dm}{2}.
\tag{R43.12}
\]

This is a useful sharp envelope, but it does not encode (R43.5)--(R43.7)
and therefore cannot close Gate A by itself.

## 3. Exact count-phase obstruction outside the hard owner

The failure of a phase-only proof can be shown analytically, without a
finite certificate.  Let \(N\to\infty\) through multiples of four and set

\[
 B_0=1,\quad q=N,\quad \mu=N+1,\quad m=1,
 \quad p=\frac N4,\quad r=\frac{3N}{4}-1,\quad x=N-1.
\tag{R43.13}
\]

Define \(\theta_N\) and \(t_N\) by

\[
 \frac N\pi(\tan\theta_N-\theta_N)=\frac74,
 \qquad
 t_N=\arccos\!\left(\frac{N+1}{N}\cos\theta_N\right).
\tag{R43.14}
\]

Then \(K=N\sec\theta_N=(N+1)\sec t_N\), so

\[
 G_K(q)=\frac74=B_0+\frac34.
\]

The standard integral comparison gives \(0<h_N<u_N<\beta_N<1/2\),
and \(p>d_Nm\) for all sufficiently large \(N\).  The inherited activity
margin is also eventually positive: its leading \(K^2\) term is of order
\(N^2\), whereas \(\pi^2/(1-\cos t_N)^2\) is only of order
\(N^{4/3}\).

Since \(\tan\theta-\theta\sim\theta^3/3\),

\[
 N^{1/3}\theta_N\longrightarrow
 \left(\frac{21\pi}{4}\right)^{1/3},
 \qquad \frac{t_N}{\theta_N}\longrightarrow1.
\tag{R43.15}
\]

It follows that \(d_N\to1\), \(\zeta_N=O(N^{1/3})\), and
\(\zeta_N/N\to0\).  Directly from (R43.13),

\[
 U_q=\sqrt{2N+1},\qquad U_x=2\sqrt N,
 \qquad U_r=\frac{\sqrt7}{4}\sqrt{N(N+8)},
\]

and hence

\[
 \frac{R_1}{\sqrt N}\longrightarrow
 \frac{\sqrt7}{4(2-\sqrt2)},\qquad
 \frac{p+a_p}{N}\longrightarrow\frac{11}{42}.
\tag{R43.16}
\]

The representation

\[
 h_N=\frac1\pi\int_0^1
 \arccos\!\left(1-\frac y{N+1}\right)dy
\]

and dominated convergence give

\[
 \sqrt N\,h_N\longrightarrow\frac{2\sqrt2}{3\pi}.
\tag{R43.17}
\]

Therefore \(H_N\asymp N^{3/2}\), so eventually
\(\min\{\zeta_N,H_N\}=\zeta_N\), and

\[
 \frac{\mathcal T_{42}}N\longrightarrow
 \frac{11\sqrt{14}}{252\pi(2-\sqrt2)}-\frac18<0.
\tag{R43.18}
\]

For the last strict sign, use \(\sqrt{14}<4\), \(\pi>3\), and
\(2-\sqrt2>1/2\): the positive term is less than
\(22/189<1/8\).

This proves that the count-phase, radial, gap, and \(p>dm\) relations do
not imply (R43.1).  It does not disprove (R43.1) on the exact hard owner.
Indeed, the same-shelf drop diverges along (R43.13).  The elementary bound

\[
 A(r)-A(x)
 \ge
 \frac{1-\cos t_N}{2\pi\mu}(x^2-r^2)
\tag{R43.19}
\]

follows from \(\arcsin y-\arcsin(y\cos t)\ge y(1-\cos t)\).
By (R43.15), its right side is of order \(N^{1/3}\), whereas a common
shelf would require \(A(r)-A(x)<1\).

## 4. The hard remainder is the load-bearing correlation

There is a much sharper finite diagnostic.  Define the outer wall exactly
by

\[
 (r,p,m,q,\mu,B_0,B)=(1,9,9,19,20,2,3),
\]

\[
 \frac{19}{\pi}(\tan\theta-\theta)=\frac{11}{4},
 \qquad t=\arccos\!\left(\frac{20}{19}\cos\theta\right).
\tag{R43.20}
\]

An 80-digit evaluation gives

\[
 \begin{aligned}
 t&\approx0.9153090531646393,&
 d&\approx0.4172961589283409,\\
 \zeta&\approx0.7161376492059593,&
 H&\approx2.7453199890763925,\\
 h&\approx0.0672747441072572,&
 u&\approx0.2974123497434613,\\
 \beta&\approx0.3034164442436875.&
 \end{aligned}
\]

It has \(0<h<u<\beta<1/2\), \(p>dm\), positive activity margin, and

\[
 [A(r)+\tfrac14]=[A(x)+\tfrac14]=4,
 \qquad [A(x+1)+\tfrac14]=3.
\]

Thus \(f=4\), \(j=1\), and the ordinary first shelf and terminal crossing
are synchronized.  But

\[
 E\approx0.3280024860904140,\qquad
 E_*\approx0.2913519205358296,
\]

so

\[
 E-E_*\approx0.0366505655545844>0,
 \qquad
 \mathcal T_{42}\approx-0.1052012866528949<0.
\tag{R43.21}
\]

This high-precision computation is diagnostic, not interval
certification.  Its logical use is limited: it shows why the quantitative
condition (R43.7) cannot be omitted.  It is not a counterexample on the
live owner.

The exact final Gate-A implication is therefore the contrapositive

\[
 \boxed{\mathcal T_{42}<0\ \Longrightarrow\ E\ge E_*}
\tag{R43.22}
\]

under the synchronized outer wall and terminal crossing.

## 5. The last intrinsic transport and its discontinuity

Fix \(r,p,m,f\), put

\[
 A_t(z)=G_{\mu\sec t}(z)-G_\mu(z),
\]

\[
 E_f(t)=A_t(r)+A_t(x)+\frac12-2f,
 \qquad E_*(t)=\frac12-\frac{d(t)m}{2p}.
\tag{R43.23}
\]

Since

\[
 \frac{\partial A_t(z)}{\partial t}
 =\frac{\tan t}{\pi}\sqrt{K^2-z^2},
\]

one has the exact derivative

\[
 \frac d{dt}(E_f-E_*)
 =\frac1\pi\left[
 \tan t\left(\sqrt{K^2-r^2}+\sqrt{K^2-x^2}\right)
 -\frac mp\right].
\tag{R43.24}
\]

### Lemma 5.1

On every fixed-\(f\) hard outer-gap chart,

\[
 \boxed{\frac d{dt}(E_f-E_*)>0.}
\tag{R43.25}
\]

**Proof.**  Since \(r,x<\mu\),

\[
 \sqrt{K^2-r^2},\sqrt{K^2-x^2}>\mu\tan t.
\]

Also \(p>dm\) gives \(m/p<1/d\).  It is enough to prove

\[
 2\mu d\tan^2t>1.
\tag{R43.26}
\]

From (R43.4),

\[
 W=B_0+\frac34-u>\frac54.
\tag{R43.27}
\]

If \(t\le\pi/3\), monotonicity of \(\tan s/s\) gives

\[
 \tan t-t=\int_0^t\tan^2s\,ds
 \le\frac t3\tan^2t.
\]

Combining this with \(W=\mu(\tan t-t)/\pi>5/4\) yields
\(2\mu d\tan^2t>15/2\).

If \(t\ge\pi/3\), put \(y=\pi/2-t\le\pi/6\).  Since
\(\tan t-t<\tan t\), (R43.27) gives

\[
 2\mu d\tan^2t>5y\cot y>5\cos y
 \ge\frac{5\sqrt3}{2}>1.
\]

Thus (R43.26) holds in both ranges, and (R43.24) is strictly positive.
\(\square\)

Lemma 5.1 is the strongest global-looking transport left by the compressed
scalar, but it is only chart-local.  When the shelf floor changes from
\(f\) to \(f+1\),

\[
 E_{f+1}(t)=E_f(t)-2.
\tag{R43.28}
\]

Meanwhile the outer face samples only the discrete walls

\[
 G_K(q)-\frac34=B_0\in\mathbb N.
\tag{R43.29}
\]

Thus the continuous transport stops exactly at the synchronized
sawtooth: comparing (R43.28) and (R43.29) globally requires an
\(f\)- or \(B\)-indexed wall family (equivalently, a chamber treatment of
the two discontinuous floors).  The binding strategy expressly forbids
that continuation.  The finite record (R43.20) shows that this is not a
cosmetic issue: every smooth geometric condition can hold while the sign
changes just outside the hard wall.

## 6. Diagnostic sharpness and replay

On the existing 406 retained exact upper-alpha/outer-\(B\) samples,

\[
 \min\frac{H}{\underline H}\approx1.0003099.
\]

The reduced right side of (R43.12) had observed binary64 minimum

\[
 0.2227224\ldots
\]

at \((r,p,m,f,B)=(1,5,1,2,2)\).  These values show that the radical
envelope is sharp enough to be useful; they do not prove a continuum sign.

The companion
`computations/general_d_round43_hard_remainder_replay.wl` checks the
algebraic radical identities, the derivative identity, the elementary
asymptotic coefficient, and the high-precision finite diagnostic.  The
separate
`computations/general_d_round43_hard_remainder_diagnostic.py` reproduces
the 406-sample theorem-design statistics.  Both are diagnostic replays,
not certificates and not substitutes for the printed proofs.

## 7. Loss ledger and workflow update

| transition | status | consequence |
|---|---|---|
| Round 42 exact \(\Phi_\delta^+\) identity to \(\mathcal T_{42}\) | inherited strict sufficient reduction | endpoint still open |
| \(H,h\) to \(\underline H,\underline h\) | proved lower envelope | sharp, but deletes the shelf sawtooth |
| count-phase family (R43.13) | analytic obstruction on a relaxed domain | proves phase/radial data alone are insufficient |
| finite record (R43.20) | diagnostic only | isolates \(E<E_*\); not a live counterexample |
| fixed-chart hard-wall transport | proved strict monotonicity | stops at the floor jump (R43.28) |
| global continuation of (R43.22) | would require forbidden \(f/B\)-indexed walls | Gate A exhausted |
| next authorized step | Gate B | restore the exact shifted-tail scalar (R43.2) |

The next round must begin from \(\mathscr S\), not from another compressed
lower bound and not from a repaired version of \(\mathcal T_{42}\).  It
must retain the exact first-shelf trapezoid, terminal surplus, cap, and
inverse fractions until an intrinsic shelf--terminal theorem is visible.
The inherited exact shelf identity

\[
 R_p=\mathcal C_p+p\left(E-\frac12\right)
\]

and \(pE_*=(p-dm)/2\) give the canonical Gate-B form

\[
 \boxed{\mathscr S=D_A(q)+\mathcal C_p+p(E-E_*).}
\tag{R43.30}
\]

Thus the first unrenamed exact target is simply

\[
 \boxed{D_A(q)+\mathcal C_p\ge p(E_*-E).}
\tag{R43.31}
\]

Here \(D_A(q)\) is the literal one-sided terminal defect and
\(\mathcal C_p\) is the exact shelf trapezoid; neither may be replaced at
the outset by \(L_T\), \(a_p\Delta\), or a new projected scalar.
If the exact pointwise route then has a certified negative point, or its
possible negative support cannot be localized without forbidden splitting,
Gate C begins with the weighted aggregate in dimension four.
