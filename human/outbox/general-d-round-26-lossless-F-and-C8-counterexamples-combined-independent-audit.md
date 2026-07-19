# General dimension, Round 26: combined independent audit of the lossless projection, F counterexamples, and C8 counterexample

Date: 19 July 2026  
Status: independent audit complete; all central certificates pass, with two scope/nomenclature qualifications recorded below

## 0. Audit verdict

The three Round 26 submissions were audited from their frozen source files,
with fresh arithmetic rather than imported printed values. The central
claims pass:

1. the lossless stationary projection is algebraically correct, and the
   half-integer witness with $p=6$ lies in the full shelf, parity, activity,
   stationarity, and coupled discrete-owner image while satisfying
   $\mathcal F<-1/50<0<77/50<\mathcal C _8$;
2. the separate integer-grid witness with $p=4$ lies in the exact
   shelf/parity/activity/stationary domain and satisfies
   $\mathcal F<-1/100<0<1<\mathcal C _8$;
3. the high-floor half-integer witness with $p=80$, and its nearby unique
   stationary point, satisfy $\mathcal C _8<-7$, whereas the exact-cap
   repaired scalar satisfies $\mathcal R_J>20$.

There are two qualifications, neither of which changes those conclusions.

- The $p=4$ certificate does **not** impose the extra Round 24 discrete
  minimizing-owner filter. In fact an independent check gives
  $S_x(5)-S_x(4)<-0.0386$, with $p=5$ feasible. Thus that artifact
  certifies the exact shelf/parity/activity/stationary scope stated in its
  domain list, but it must not by itself be cited as a coupled-minimizer
  certificate. The $p=6$ lossless certificate supplies precisely that
  stronger result.
- In the established Round 21--23 nomenclature, $\mathscr S$ is the exact
  reduced scalar, while $\mathcal R_J$ is the exact-cap repaired intrinsic
  lower scalar. Therefore “exact correlated scalar” in the Round 26b title
  and prose should be read as “exact-cap repaired scalar $\mathcal R_J$.”
  This audit certifies $\mathcal R_J$, not a direct evaluation of
  $\mathscr S$.

Subject to those explicit readings, the combined verdict is **PASS**.

## 1. Frozen artifacts and SHA-256 ledger

The audit used the following final source snapshots. Hashes were recomputed
with Get-FileHash -Algorithm SHA256 after the arithmetic replays.

| artifact | SHA-256 |
|---|---|
| human/outbox/general-d-round-26-lossless-stationary-projection-and-F-falsification.md | 1d13c172a3b7c8dad55656557e2598b02f24891c373cbc71d1ac788777e74f49 |
| human/outbox/general-d-round-26-exact-stationary-image-counterexample-to-F.md | fc5f36a39197eb182fe090b0d9ef8e0a451afd26ffd9cb9f30db2f01375e0aab |
| computations/general_d_round26_c8_exact_stationary_image_counterexample.py | c4aa99f95b8a27663cea65e4610df2ae29f95c3514f330fe11eee6b57790abb7 |
| human/outbox/general-d-round-26b-certified-C8-counterexample-with-positive-exact-correlated-scalar.md | 9a5279bdd0448bc3df61fc26a2e556f859adf7946ae68c8654233a7a8b940cc6 |
| computations/general_d_round26b_c8_exact_feasible_counterexample.py | 83aabf401bc342d83af395d2c5328c2d5bf45068693ab6df7aa3c86e96f4f4af |

The auditor edited no source artifact, state file, or control file.

## 2. Independent method

All certified scripts were run in fresh Python processes with
python-flint 0.8.0 at 128, 256, 512, and 1024 Arb bits. In addition, an
independent in-memory verifier reconstructed the lossless $p=6$ witness,
because that note has no companion replay script. It recomputed the exact
rational endpoints, shell actions, activity gap, owner differences,
stationary derivative, $V$, and the rational comparison defining
$p_{\max}$.

The installed Mathematica 15 kernel was used only as an algebraic
cross-check. Under $0<v<1$, $0<t<\pi/2$, and $\mu>0$, it returned zero for
each of the following residuals:

\[
 \frac{d}{dv}F_t(v)
 -\{\arccos(v\cos t)-\arccos v\},
\]

\[
 \frac{d}{dt}\mathcal C _8-D(t),
 \qquad
 \frac{d}{dt}D(t)-
 \left\{C_0\cos t+\frac{B\pi}{t^3}
 +4\bigl((W')^2+uW''\bigr)\right\},
\]

and, after substituting the stationary equation,

\[
 \mathcal C _8-\left(V-\frac p2\right).
\]

It also returned

\[
 \frac d{dp}\{p^2(3x-p)\}=3p(2x-p),
 \qquad
 \frac{d^2}{dp^2}S_x(p)=6k(x-p),
\]

and zero for the exact $\mathcal R_J-\mathcal C _8$ reserve identity. The
transcendental sign decisions below remain Arb decisions; Mathematica is
not being used as a numerical certificate.

## 3. Audit of the lossless stationary projection and coupled-owner F witness

### 3.1 Exact shelf and projection formulas

Differentiating the displayed $F_t(v)$ gives exactly

\[
 F_t'(v)=\arccos(v\cos t)-\arccos v.
\]

Since $F_t(1)=t-\tan t$, the cumulative formula for
$\mathscr I_t(\mu v)$ has the stated sign and endpoints. Moreover
$W+\delta=B+3/4$, so the two cumulative inequalities are exactly the two
complete shelf inequalities; no endpoint-only surrogate is hidden in their
use.

The parity/interface reconstruction is reversible:

\[
 q=\max\{s\in\mathcal G_\varepsilon:s\leq\mu\},\qquad
 \alpha=\mu-q,\qquad x=q-m,
\]

and substitution of $r=x-p$ in $p^2(3r+2p)=P$ gives

\[
 p^2(3x-p)=P.
\]

On the owner range $0<p<x$, its derivative is $3p(2x-p)>0$, so at most one
positive integer stationary owner is possible for the fixed intrinsic
data. The discrete scalar has $S_x''(p)=6k(x-p)=6kr>0$, validating the
strict-convexity owner test.

### 3.2 Independent replay of the exact witness

For

\[
 (B,f,m,r,p,\alpha,\mu)
 =\left(1,2,6,\frac{25}{2},6,\frac9{10},\frac{127}{5}\right)
\]

one has $x=37/2$, $q=49/2$, and the required half-integer parity. On

\[
 I=[33913/50000,16957/25000]
\]

the independent replay gave, at every tested precision,

\[
 D(33913/50000)<-0.0013354,\qquad
 D(16957/25000)>0.0012401,
\]

and direct interval differentiation gave $D'(I)>128$. Hence there is a
unique stationary root in $I$.

The weakest certified domain margins were

\[
 A_{t_{\rm lo}}(x)-\frac74>0.0083212,
\]

\[
 \frac74-A_{t_{\rm hi}}(x+1)>0.0626723,
 \qquad
 \frac{11}{4}-A_{t_{\rm hi}}(r)>0.6799815,
\]

and the half-integer activity gap exceeded $860.59$. Also
$0.031<u<0.032<1/\sqrt2$, so the point is strictly inside the literal
$B_0=1$ quadratic cell.

For the exact feasible prefix, interval evaluation gave

\[
 S_x(6)-S_x(5)
 \subset[-0.01974745,-0.01958781],
\]

\[
 S_x(7)-S_x(6)
 \subset[0.04956873,0.04978679].
\]

Together with strict convexity and feasibility of $p=6$, these signs make
$p=6$ the unique discrete minimizing owner. Thus every advertised shelf,
parity, activity, stationarity, action-cell, and coupled-owner condition is
present.

Finally,

\[
 V(I)\subset(4.54324432,4.54692812),
\]

while $P=1782$ exactly and

\[
 \left(\frac{457}{50}\right)^2
 \left(2\frac{457}{50}+3\right)
 =\frac{27776917}{15625}<1782.
\]

The interface bound $92/5$ is also larger than $457/50$. Hence
$p_{\max}>457/50$, and the rational margins prove

\[
 \mathcal F=V-\frac{p_{\max}}2<-\frac1{50},
 \qquad
 \mathcal C _8=V-3>\frac{77}{50}.
\]

**Artifact verdict: PASS without qualification.**

## 4. Audit of the separate exact stationary-image F certificate

For

\[
 (r,p,m,B,f,\alpha,\mu)
 =\left(12,4,5,1,2,\frac12,\frac{43}{2}\right),
\]

the interface identity gives $x=16$, $q=21$, and the integer grid. Every
precision replay certified a unique root in

\[
 [7257007/10^7,453563/625000]
\]

from opposite endpoint signs and $D'>136.03$ on the box. On that same box
it certified

- lower shelf margin $>0.01102$;
- first-drop margin $>0.07286$;
- strict start margin $>0.73184$;
- integer-grid activity margin $>669.89$; and
- $0<u<1/\sqrt2$ with literal $B_0=1$.

These are the complete paired shelf, start, parity/interface, activity, and
open-cell conditions. The implementation of $D$, $D'$, the stationary
$V$-identity, and the direct $\mathcal C _8$ expression agrees with the
symbolic derivation in Section 2.

The exact stationary value has $P=704$. The certified root bracket
$6.59<\psi(P)<6.6$, together with the inactive interface bound $15$, gives
the displayed continuous-owner loss. Whole-box evaluation proves

\[
 \mathcal F<-\frac1{100},
 \qquad
 \mathcal C _8>1.
\]

The additional owner-scope check is deliberately separated. At the same
fixed $(x,m,\alpha,f,t)$, the independent interval computation gives

\[
 S_x(5)-S_x(4)<-0.0386.
\]

The $p=5$ competitor is feasible: it has $r=11$ on the integer grid, all
$x$-dependent shelf and activity checks are unchanged, and its start
margin is $>0.683$. Therefore $p=4$ is not the Round 24 discrete minimizer.
This does not affect the exact stationary-domain counterexample as
formulated without that extra minimizer filter, and it does not affect the
combined Round 26 conclusion because Section 3 supplies a coupled-owner
counterexample.

**Artifact verdict: PASS for its explicit shelf/parity/activity/stationary
domain; not a coupled-minimizer certificate.**

## 5. Audit of the C8 counterexample and positive R_J accounting

### 5.1 Exact domain and direct C8 sign

For

\[
 r=\frac{57755}{2},\quad p=80,\quad m=15,\quad f=2,
 \quad\alpha=\frac12,\quad\mu=28973,
 \quad t=\frac{7801}{100000},
\]

one has

\[
 q=\frac{57945}{2},\qquad \mu=q+\frac12,
 \qquad x=\frac{57915}{2},
\]

so the interface and half-integer parity are exact. The independent
replays gave the following conservative positive margins:

\[
 A_t(x)-\frac74>0.00667018,
 \qquad
 \frac74-A_t(x+1)>0.00994425,
\]

\[
 A_t(x+1)-\frac34>0.9900557,
 \qquad
 \frac{11}{4}-A_t(r)>0.00470557,
\]

and the half-integer activity gap exceeded $8.4349\times10^8$. Because
$A_t$ decreases in its spatial argument, these inequalities cover the
entire first shelf and prove exactly one floor drop at $x+1$. The action
check gives $u=0.4629573\ldots$, $0<u<1/\sqrt2$, and literal $B_0=1$.

Direct evaluation of the displayed formula gives

\[
 \mathcal C _8
 =-7.2464375575772737\ldots<-7.
\]

This one feasible tuple already disproves the universal C8 sign. No
discrete minimizing-owner condition is needed for that logical conclusion:
if one instead minimizes over the feasible prefix at fixed intrinsic data,
the minimum is no larger than this negative value.

### 5.2 Stationary corollary

The rational point has $D(t)<-0.01$. On

\[
 [1950261/25000000,1560209/20000000]
\]

the endpoint derivatives have opposite signs and $D'>24000$. Hence the box
contains one unique stationary point. All shelf, activity, interface, and
action-cell inequalities remain strict on the box, and every precision
replay proved

\[
 \mathcal C _8(t_*)<-7.
\]

Thus C8 fails both on the full exact feasible domain and on its stationary
subdomain.

### 5.3 Exact R_J reserve identity

Writing $L_{\rm curv}=\kappa p(2r+p)/2$, the two definitions are

\[
 \mathcal C _8=(p+a_p)L_{\rm curv}-\frac p2
 +\frac{dm}{2}+\frac{B_0d}{2c}+2u^2-\frac18,
\]

\[
 \mathcal R_J=(p+a_p)L_0-\frac p2
 +\frac{dm}{2}+\frac{B_0d}{2c}+2u^2-J.
\]

Their subtraction gives the exact accounting identity

\[
 \boxed{
 \mathcal R_J=\mathcal C _8
 +(p+a_p)(L_0-L_{\rm curv})
 +\left(\frac18-J\right).}
\]

There is no missing sign, coefficient, or payment term. At the rational
point the literal maximum is the elasticity branch, with

\[
 L_0=0.4249609613\ldots,\qquad
 L_{\rm curv}=0.0772961205\ldots,
\]

and

\[
 J=0.000249340254\ldots.
\]

Consequently

\[
 (p+a_p)(L_0-L_{\rm curv})
 =27.8260114186\ldots,
\]

\[
 \frac18-J=0.1247506597\ldots,
\]

and therefore

\[
 -7.2464375575\ldots
 +27.8260114186\ldots
 +0.1247506597\ldots
 =20.7043245208\ldots>20.
\]

Fresh interval evaluation also proves $\mathcal R_J>20$ throughout the
stationary box. As a numerical diagnostic, the independently recomputed
residual

\[
 \mathcal R_J-\mathcal C _8
 -(p+a_p)(L_0-L_{\rm curv})-(1/8-J)
\]

contains zero at every tested precision, both at the rational point and on
the stationary box. The wider stationary residual is solely ordinary
interval dependency; the preceding algebra proves exact equality.

The previously audited Round 22 implication
$\Phi_\delta>\mathcal R_J$ then gives $\Phi_\delta>20$ at this witness. The
certification should, however, retain the nomenclature distinction from
Section 0: $\mathcal R_J$ is the exact-cap repaired lower scalar, not the
exact reduced scalar $\mathscr S$.

**Artifact verdict: PASS for $\mathcal C _8<0<\mathcal R_J$, with the
nomenclature qualification above.**

## 6. Precision matrix

| check | 128 bits | 256 bits | 512 bits | 1024 bits |
|---|---:|---:|---:|---:|
| lossless $p=6$ stationary/shelf/activity/owner/$V$ replay | PASS | PASS | PASS | PASS |
| general_d_round26_c8_exact_stationary_image_counterexample.py | PASS | PASS | PASS | PASS |
| general_d_round26b_c8_exact_feasible_counterexample.py | PASS | PASS | PASS | PASS |
| independent $\mathcal R_J-\mathcal C _8$ reserve accounting | PASS | PASS | PASS | PASS |

The invariant signs and rational margins are therefore not precision
artifacts.

## 7. Audited workflow consequence

The Round 26 evidence rejects two proposed sufficient targets for distinct
reasons:

\[
 \mathcal F\geq0
\]

fails even after the exact stationary integer and coupled discrete owner
are retained, because the later substitution $p\mapsto p_{\max}$ is too
lossy; and

\[
 \mathcal C _8\geq0
\]

fails already at a direct exact feasible point, because replacing $L_0$ by
its curvature branch loses about $27.826$, with the cap replacement losing
another $0.12475$.

The correct next scalar target is consequently $\mathcal R_J$ with the
literal maximum $L_0$ and exact cap $J$, or the strategy-approved weighted
aggregate. Neither counterexample reaches CST-H or the general-dimensional
Polya theorem.
