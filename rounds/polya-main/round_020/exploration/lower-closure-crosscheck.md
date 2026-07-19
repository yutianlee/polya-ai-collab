# Round 20 Lower-Ratio Closure Cross-Check

Date: 2026-07-14.

Status: **PASS / exploratory pre-freeze review only**.

This is an adversarial reconstruction of the prospective lower-ratio union.
It is not a proof-free freeze, a promotion, or a judge decision.  The Round 19
lower staircase is used only as the stated prospective ingredient; its frozen
claim remains conditional on the Round 19 review/promotion process.

## 1. Authentication and verdict

The final bytes audited here are:

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| `rounds/polya-main/round_019/exploration/residual-mask-freeze.md` | `0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9` |
| `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `rounds/polya-main/round_020/exploration/lower-next-wall.md` | `94099e852274ac697fa8c60563fbcdb0c4bb91a40c3de2c0af7556cbf7754e0a` |
| `rounds/polya-main/round_020/exploration/small-hole-wedge.md` | `f1e5ab1c3671e82257a78cd2855581f326e4df98385539a69dc4b1a295a7f43b` |
| `rounds/polya-main/round_020/exploration/lower-remaining-gap.md` | `0baea820115061f3dbd5d46c0ca48271dce2df50885c83d5cd3a83c176f6e9c6` |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` |
| `rounds/polya-main/round_003/judge/judge-003.md` | `33e292530e644896b00470a92848f2763c3c337c874a32c0f7bb79aac3b7aca9` |
| `rounds/polya-main/round_003/responses/weighted-lattice-incumbent.md` | `ef3796a9de3a394f39f34190a25b4daa97d908c123c688146dfa0b308104b375` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |
| `rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md` | `9ea72dddc15a15bae41ecb59416e316a29d6e8d85aeae3c6af20b6c6fd8080a2` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |

All declared dependency hashes match.  During this audit an endpoint defect
was caught in the pre-final form of `lower-remaining-gap.md`: its remainder
bound used a strict sign even when $q_r=\mu$, where both sides vanish.  The
final authenticated bytes above correctly state

\[
0\leq\delta_r\leq
\frac{2}{15\sqrt\mu}(\mu-q_r)^{5/2}<\frac14.
\]

The separate half-integer ledger already used $\delta_r=0$, so the defect
was not load-bearing; it is now also textually repaired.

**Verdict: PASS.  First unsupported implication: none in the prospective
lower-ratio closure.**

## 2. Exact set reconstruction

Put

\[
\rho_0=\frac1{\sqrt{337}},\qquad
d=\frac{\sqrt{337}}2,\qquad
\sigma=\frac{3\omega_0}{4},\qquad
c_7=\sqrt{114},\qquad
L(\rho)=\frac1{2\rho}.
\]

The frozen Round 18 lower residual is

\[
\mathcal R^{\rm L}
=\{\rho_*<\rho<\rho_c,\ L(\rho)<K<U(\rho)\}.
\]

The prospective Round 19 lower addition is

\[
\mathcal C_{19}^{\rm L}
=\{\rho_*<\rho<\rho_c,\ L(\rho)<K\leq d\}.
\]

It is empty for $\rho\leq\rho_0$, because
$L(\rho)\geq d$ there.  Since $d<U(\rho)$, exact subtraction gives

\[
\begin{aligned}
\mathcal D_{19}^{\rm L}
={}&\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\dot\cup
\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}.
\end{aligned}
\tag{1}
\]

The decisive order is

\[
\rho_*<\rho_0<\sigma<\rho_{HK}<\omega_0<\rho_c,
\qquad d<c_7<U(\rho).
\tag{2}
\]

Using (2), the complete post-Round-19 residual has the following exact
disjoint allocation:

\[
\boxed{
\begin{aligned}
\mathcal D_{19}^{\rm L}={}&
\underbrace{\{\rho_*<\rho\leq\rho_0,
L(\rho)<K<U(\rho)\}}_{\text{small-hole wedge}}\\
&\dot\cup
\underbrace{\{\rho_0<\rho\leq\sigma,
d<K<U(\rho)\}}_{\text{small-hole continuation}}\\
&\dot\cup
\underbrace{\{\sigma<\rho<\rho_c,
d<K\leq c_7\}}_{\text{next-wall band}}\\
&\dot\cup
\underbrace{\{\sigma<\rho<\rho_c,
c_7<K<U(\rho)\}}_{\text{remaining-gap theorem}}.
\end{aligned}}
\tag{3}
\]

The third set in (3) automatically lies below $U$, since
$U>63/4>11>c_7$.  Consequently

\[
\mathcal R^{\rm L}
=\mathcal C_{19}^{\rm L}\ \dot\cup\ \mathcal D_{19}^{\rm L}
\]

is completely covered by the prospective Round 19 face and the three Round
20 arguments.

The interface assignments in (3) are exact:

- $\rho=\rho_0$ belongs to the first piece; there $L=d$, and its fiber is
  $d<K<U$.
- $\rho=\sigma$ belongs to the small-hole continuation, whose local theorem
  permits equality in $\rho\leq\sigma$.
- $K=c_7=\sqrt{114}$ belongs to the next-wall band; the remaining-gap set is
  open there.
- For $\rho>\rho_0$, $K=d$ remains included in the Round 19 band.  At
  $\rho=\rho_0$, it is the already-covered lower face $K=L$.
- The faces $K=L(\rho)$ and $K=U(\rho)$ are excluded from the residual and
  retain their inherited owners.  The ratio faces $\rho=\rho_*$ and
  $\rho=\rho_c$ likewise retain their inherited/separate owners.

There is therefore no gap or double-uncovered equality fiber at any of the
three new interfaces.

## 3. Audit of the \(d<K\leq\sqrt{114}\) inventory

The shell-to-ball comparison is used in the correct direction and within a
fixed angular channel:

\[
k^{\rm shell}_{\ell,n}(\rho)\geq b_{\ell,n}.
\]

Extension by zero maps the shell radial form domain into the ball form
domain, while the common ball domains and Hardy's inequality justify

\[
b_{p,n}^2\geq b_{\ell,n}^2+p(p+1)-\ell(\ell+1).
\]

No Lorch statement is silently extended to a new order.  The only Lorch
seed used here is the authenticated $\ell=5$ first-zero specialization;
the $\ell=6$ delay and both radial delays are derived internally.  The
resulting strict exclusions are

\[
b_{6,1}>10,\qquad b_{3,2}>\frac{81}{8},\qquad
b_{1,3}>\frac{21}{2},
\]

and hence

\[
b_{7,1}^2>114,\quad
b_{4,2}^2>\frac{7073}{64},\quad
b_{5,2}^2>114,\quad
b_{2,3}^2>114.
\]

Together with the exact wall $k_{0,3}=3z_\rho$ and the interval Poincare
bound for $n\geq4$, this gives the exhaustive caps

| range | cap |
|---|---:|
| $d<K\leq10,\ K\leq3z_\rho$ | 45 |
| $d<K\leq10,\ K>3z_\rho$ | 46 |
| $10<K\leq81/8$ | 59 |
| $81/8<K\leq21/2$ | 66 |
| $21/2<K\leq\sqrt{7073}/8$ | 69 |
| $\sqrt{7073}/8<K\leq\sqrt{114}$ | 78 |

The moving $3z_\rho$ mode is excluded at equality and is conservatively
charged in every later row.  First modes with $\ell\geq7$, second modes
with $\ell\geq5$, third modes with $\ell\geq2$, and all $n\geq4$ are
excluded.  Thus neither the angular nor radial inventory is unbounded or
truncated without proof.

The Weyl payments recompute exactly.  From

\[
\mathcal W(\rho,c)>\frac{38}{539}c^3
\qquad(\rho<\rho_c),
\]

the successive positive margins are

\[
\frac{2908}{539},\quad
\frac{6199}{539},\quad
\frac{990435}{137984},\quad
\frac{555}{44},
\]

for caps $46,59,66,69$, and the final cap-78 squared margin is

\[
(38\cdot7073)^2\,7073-(78\cdot539\cdot512)^2
=47602399882532>0.
\]

All lower row faces are open and all upper row faces are included, so the
payment is strict on every assigned face, including $K=\sqrt{114}$.

## 4. Scope of the low-interface argument

The thresholded theorem in `SHELL-low-interface-small-hole` is not
extrapolated.  What is reused is its earlier, fully derived split.  For a
low start $x_r=r+1/2<\mu=\rho K$, put

\[
n_r=\lfloor\mu-x_r\rfloor,\qquad q_r=x_r+n_r,
\qquad p=\lfloor\omega_0K\rfloor.
\]

Because every ratio at issue satisfies $\rho<1/2$, one has
$q_r\leq\mu<K/2$, so the $K/2$ point lies in the convex block required
by the audited floor theorem.  The valid pre-threshold inequality is

\[
\frac{\mathcal T_r}{2}
\leq\int_{x_r}^{K}A_{\rho,K}(z)\,dz
+\delta_r-\frac{p-n_r}{4},
\qquad
\delta_r=\int_{q_r}^{\mu}G_\mu(z)\,dz.
\tag{4}
\]

It also holds when $n_r=0$, where the concave block is absent.  The
turning estimate gives the corrected endpoint-valid bound

\[
0\leq\delta_r\leq
\frac{2}{15\sqrt\mu}(\mu-q_r)^{5/2}<\frac14.
\tag{5}
\]

For $\rho\leq\sigma$, $\omega_0K>1$ and
$\mu\leq3\omega_0K/4$ imply

\[
\lfloor\omega_0K\rfloor
\geq\left\lfloor\mu-\frac12\right\rfloor+1,
\]

so every low tail is strict in (4).  This remains valid at
$\rho=\sigma$.  The promoted high-interface theorem controls every start
at or above $\mu$.  This proves both the small-hole wedge and its complete
$d<K$ continuation through the included ratio face $\rho=\sigma$.

## 5. Exhaustive floor-cell audit above \(\sigma\)

For the remaining range define

\[
p=\lfloor\omega_0K\rfloor,\qquad
m=\left\lfloor\mu-\frac12\right\rfloor,qquad
\mu=m+\frac12+t,\quad0\leq t<1.
\]

Here $p\geq1$.  If $0<t<1$, the low starts are exactly
$r=0,\ldots,m$, all have the same interface remainder, and

\[
\sum_{r=0}^{m}(p-n_r)=\frac{m+1}{2}(2p-m).
\]

If $t=0$, the start $x_m=\mu$ is correctly put on the high side, the
low starts are $r=0,\ldots,m-1$, $\delta_r=0$, and

\[
\sum_{r=0}^{m-1}(p-n_r)=\frac m2(2p-m-1).
\]

Thus the aggregate works whenever $m\leq2p-1$.  There are no omitted
floor cells:

- $p=0$ is impossible because $\omega_0K>1$.
- For every $p\geq2$, the exact ratio bound
  $\rho_c/\omega_0<3/2$ gives
  $\mu<2p+1/2$, hence $m\leq2p-1$.
- For $p=1$, the aggregate works exactly when $m\leq1$, equivalently
  $\mu<5/2$.
- The complement has $p=1$, $\mu\geq5/2$, and
  $K<2/\omega_0$.  Since the same ratio bound gives $\mu<3$, this is
  exactly the single floor pair $(p,m)=(1,2)$.

At $\omega_0K\in\mathbb Z$ the new value of $p$ is used.  At
$\mu\in\mathbb Z+1/2$ the interface start is high.  The face
$\mu=5/2$ belongs to the exceptional cell, while $K=2/\omega_0$ has
$p=2$ and belongs to the aggregate.  These conventions leave no floor
wall uncovered.

Strictness is also retained.  There is always a high start
$\mu\leq x_h<\mu+1<K$, because
$(1-\rho)K>60/7>1$.  Its translated $G_K$ tail is nonzero, and the
audited convex shifted-tail theorem is strict unless that function is zero.
Hence the summed proxy is strictly below the Weyl integral even when the
low aggregate itself has zero margin.

## 6. Strict proxy, cap 395, and payment above 424

For every active half-integer $z_\ell=\ell+1/2<K$, the phase enclosure
gives

\[
\gamma_{\rho,K}(z_\ell)
<A_{\rho,K}(z_\ell)+\frac14.
\]

Therefore the strict radial count obeys

\[
\#\{n\geq1:n<\gamma_{\rho,K}(z_\ell)\}
\leq
\left\lfloor A_{\rho,K}(z_\ell)+\frac14\right\rfloor.
\tag{6}
\]

At an integer phase wall the left side drops by one; at an integer proxy
wall the strict phase inequality still makes (6) an upper bound.  Channels
with $z_\ell\geq K$ have zero radial count by the sharp inherited angular
cutoff.  Thus (6) is a valid strict spectral-to-proxy bridge, not an exact
ordinary-floor identity.

On the exceptional cell, $K<2/\omega_0<367/20$.  The turning estimate at
that rational endpoint yields the verified caps

\[
(c_0,\ldots,c_{14})
=(6,5,5,4,4,3,3,3,2,2,1,1,1,1,0).
\]

For each row the exact margin is

\[
M_\ell=(4c_\ell+3)^2\,82575-(357-20\ell)^3>0;
\]

the smallest is still positive ($M_{10}=176282$).  The $\ell=14$ row
and monotonicity in $z$ force every later proxy count to zero.  Hence this
is a complete angular and radial proxy inventory, and

\[
\sum_{\ell\geq0}(2\ell+1)c_\ell=395.
\]

On the same cell, $K\geq5/(2\rho)$ and
$\rho<\rho_c<11/80$.  The exact payment is

\[
\mathcal W(\rho,K)
>\frac{160293325}{378004}
=424+\frac{19629}{378004}
>424>395.
\]

Thus the cap branch includes its lower face $\mu=5/2$ with more than 29
units of margin over the proxy cap.

## 7. Upper-floor branches

Only two inherited $U$-branches are active below $\rho_c$:

\[
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\
K_0(\rho),&\rho_{HK}\leq\rho<\rho_c.
\end{cases}
\]

The exact order

\[
\rho_0<\sigma<\rho_{HK}<\omega_0<\rho_c
\]

places the $\rho_0$ and $\sigma$ faces on the $H_0$ branch.  At
$\rho_{HK}$, $H_0=K_0$ and the inherited rule selects $K_0$.  The
$H_0$-eligibility endpoint $\rho=\omega_0$ occurs after that switch and
does not alter the active minimum.  The seam branch
$54/(1-\rho)^2$ starts only at $\rho=5/6>\rho_c$ and is inactive in the
entire set audited here.

Both active branches satisfy $U>63/4$, so no frequency band in (3) is
silently empty and no proof uses continuity across a branch switch.  The
new local theorems in fact do not need the ceiling; $U$ is used only for
exact residual ownership.

## 8. Final adversarial finding

No thresholded theorem is extrapolated, no strict count is replaced by an
ordinary-floor identity, no floor cell or equality face is lost, and no
angular or radial inventory is left unbounded.  The corrected half-integer
remainder inequality is valid at equality.  The exact disjoint union (3)
therefore closes every point of the prospective post-Round-19 lower
residual.

**PASS.  First unsupported implication: none.**
