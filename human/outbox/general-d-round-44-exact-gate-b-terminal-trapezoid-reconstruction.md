# General-dimensional spherical-shell Pólya project
## Round 44: exact Gate-B terminal/trapezoid reconstruction

**Date:** 20 July 2026  
**Base commit:** ce3cf00cdf82f0c9dca94177f359b8a4fbbcaab3  
**Working branch:** codex/general-d-round-44-exact-gate-b  
**Classification:** **PARTIAL SUCCESS — exact loss ledger proved; one intrinsic negative-support localization proved; final sign open**

## 0. Theorem boundary, source audit, and conflicts

This round treats only the resisting one-sided upper-$\alpha$, outer-$B$
endpoint of the hard one-level gap. It does not prove that endpoint, the full
high-floor first-drop CST theorem, the general-dimensional branching
backbone, the weighted aggregate, or the all-dimensional Pólya theorem.

The authoritative statuses remain

~~~text
SHELL-general-d-high-floor-first-drop-CST: open
SHELL-general-d-branching-backbone: derived_under_assumptions
SHELL-general-d-weighted-aggregate: proposed
TARGET-shell-general-d: proposed
~~~

The Round 38--43 branch was already merged before this work. Remote main was
verified to be exactly the required base SHA before the Round 44 branch was
created.

All mandatory Prompt A sources were read. Three source conflicts require
explicit qualification.

1. state/proof_obligations.yml still describes the Round 37 selected
   projection as the next action, while the newer independently audited
   Round 43 record says **Gate A STOP** and activates Gate B. The graph's
   authoritative open/proposed statuses agree with Round 43, but its
   narrative next-action field lags the audited workflow. The direct Round 44
   instruction selects Gate B; the proof graph is not edited.
2. The symbol $n$ is overloaded historically. Round 10 uses
   $n=\lfloor\mu-r\rfloor$, whose upper-$\alpha$ gap-side value for
   $\mu=q+\alpha$, $0<\alpha<1$, is $p+m$. At the exact geometry
   $\mu=q+1$ its literal floor is instead $p+m+1$. Rounds 38/42 and the
   Round 44 prompt reuse $n$ for the count coordinate $f-1=B_0+j$.
   These are not equal in general: the Round 43 gap-side fixture has
   $p+m=18$ but $f-1=3$. This note avoids $n$ after recording the conflict.
3. The literal strict outer-ball count at the wall is $B_0=B-1$, whereas $B$
   is a one-sided gap label. No formula below identifies those two owners.
   The exact geometry can nevertheless be evaluated at $\mu=q+1$; only the
   label remains one-sided.

The manuscript was used only to reconstruct the already promoted hinge proof
of $\mathcal C_p\ge a_p\Delta$. Neither the manuscript nor the proof graph is
edited.

## 1. Exact owner and notation

Put

$$
x=r+p,\qquad q=x+m,\qquad \mu=q+1,\qquad
K=\mu\sec t,\qquad 0<t<\frac{\pi}{2},
$$

$$
d=d_\rho=1-\frac{2t}{\pi},
\qquad
\zeta=\frac{\pi}{2t}-1,
$$

and

$$
G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
\qquad
A(z)=G_K(z)-G_\mu(z).
$$

At the outer wall,

$$
G_K(q)=B-\frac14,\qquad B_0=B-1\ge1.
$$

Define

$$
h=G_\mu(q),\qquad
u=G_K(q)-G_K(\mu),\qquad
\beta=\frac1\pi\arccos\frac qK.
$$

The owner has

$$
0<h<u<\beta<\frac12.
$$

The literal strict ball count and shell count are

$$
B_{\rm lit}
=\left[G_K(q)+\frac14\right]_< =B_0,
$$

$$
A(q)+\frac14=B-h\in(B-1,B),
\qquad
Q=\left[A(q)+\frac14\right]_< =B_0.
$$

Let $f$ be the common ordinary shelf floor and $j=f-B\ge0$. The literal
shelf and first-drop requirements are

$$
\left\lfloor A(r)+\frac14\right\rfloor
=\left\lfloor A(x)+\frac14\right\rfloor=f,
\qquad
\left\lfloor A(x+1)+\frac14\right\rfloor\ne f.
$$

Define

$$
e_0=A(r)+\frac14-f,\qquad
e_p=A(x)+\frac14-f,\qquad
E=e_0+e_p,\qquad
\Delta=e_0-e_p,
$$

$$
a_p=\frac{p^2}{3(2r+p)},\qquad
E_*=\frac{p-dm}{2p}.
$$

The hard owner is

$$
p\ge3,\qquad m\ge1,\qquad q\ge5,\qquad
p>dm,\qquad p-dm>\frac{11}{5},
$$

$$
0\le E<E_*<\frac12,
$$

together with $j\ge0$, the common shelf and literal first drop. For ambient
dimension $D\ge4$, retain the exact strict dimension-labelled activity
condition

$$
K^2>
\frac{\pi^2}{(1-\mu/K)^2}
+\frac{(D-2)^2-1}{4}.
$$

Here $r\in\mathbb N$, $r\ge1$, on the even-dimensional extension grids and
$r\in\mathbb N_0+1/2$, $r\ge3/2$, on the odd-dimensional extension grids.
The activity equality belongs to the dimension-$D$ no-mode owner.

For a dimension-uniform proof or falsification search, it is safe to enlarge
the active owner to the weakest parity-labelled conditions

$$
K^2>\frac{\pi^2}{(1-\mu/K)^2}+\gamma_{\rm grid},
\qquad
\gamma_{\rm grid}=
\begin{cases}
\frac34,&r\in\mathbb N,\ r\ge1,\\[2mm]
2,&r\in\mathbb N_0+\frac12,\ r\ge\frac32.
\end{cases}
$$

because these are the $D=4$ and $D=5$ minima. Every exact
dimension-labelled active point lies in this enlarged owner. The analytic
identities below do not use either activity threshold; both computational
searches deliberately use the enlarged owner.

The sole primary target is

$$
\boxed{\mathscr S=D_A(q)+\mathcal C_p+p(E-E_*)\ge0.}
\tag{R44.1}
$$

No projected scalar is substituted for (R44.1).

## 2. Exact shelf trapezoid and complete curvature ledger

### 2.1 Derivatives and signs

For $0<z<\mu<K$,

$$
G_a'(z)=-\frac1\pi\arccos\frac za,
\qquad
G_a''(z)=\frac1{\pi\sqrt{a^2-z^2}}.
$$

Hence

$$
A'(z)=\frac1\pi
\left(\arccos\frac z\mu-\arccos\frac zK\right)<0,
$$

$$
A''(z)=\frac1\pi
\left(
\frac1{\sqrt{K^2-z^2}}-\frac1{\sqrt{\mu^2-z^2}}
\right)<0,
$$

and

$$
(-A'')'(z)=\frac z\pi
\left(
(\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}
\right)>0.
\tag{R44.2}
$$

All signs hold on $[r,x]$, because $r\ge1$ and $x<q<\mu<K$.

### 2.2 Exact integrations by parts

The first-shelf payment is

$$
R_p=2\int_r^x A(z)\,dz-2pf.
$$

Twice integrating by parts, with $u(p-u)=0$ at both endpoints, gives

$$
\boxed{
\mathcal C_p
=-\int_0^p u(p-u)A''(r+u)\,du
=2\int_r^x A(z)\,dz-p\{A(r)+A(x)\}.}
\tag{R44.3}
$$

Since

$$
A(r)+A(x)=2f-\frac12+E,
$$

we obtain

$$
\boxed{R_p=\mathcal C_p+p\left(E-\frac12\right).}
\tag{R44.4}
$$

The monotonicity in (R44.2) gives the elementary curvature reserve

$$
\begin{aligned}
\mathcal C_p
&\ge (-A''(r))\int_0^p u(p-u)\,du\\
&=\boxed{
\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}-\frac1{\sqrt{K^2-r^2}}
\right)}>0.
\end{aligned}
\tag{R44.5}
$$

### 2.3 Line-by-line hinge reconstruction of
$\mathcal C_p\ge a_p\Delta$

Put $\sigma=-A'$. Then $\sigma(0)=0$, and $\sigma$ is increasing and convex.
Its positive-hinge representation is

$$
\sigma(z)=az+\int_{[0,\infty)}(z-s)_+\,d\nu(s),
\qquad
a\ge0,\quad \nu\ge0.
\tag{R44.6}
$$

Both $\mathcal C_p$ and

$$
\Delta=A(r)-A(x)=\int_r^x\sigma(z)\,dz
$$

are linear in $\sigma$. It is therefore enough to compute the loss on every
generator.

For the linear generator $\sigma(z)=z$,

$$
\mathcal C_p=\frac{p^3}{6},
\qquad
\Delta=p\left(r+\frac p2\right),
\qquad
\mathcal C_p-a_p\Delta=0.
\tag{R44.7}
$$

For a hinge $(z-s)_+$ with $0\le s\le r$,

$$
\mathcal C_p=\frac{p^3}{6},
\qquad
\Delta=p\left(r-s+\frac p2\right),
$$

and

$$
\boxed{
\mathcal C_p-a_p\Delta
=\frac{p^3s}{3(2r+p)}\ge0.}
\tag{R44.8}
$$

For $r<s<x$, put $L=x-s\in(0,p)$. Then

$$
\Delta=\frac{L^2}{2},
\qquad
\mathcal C_p=\frac{pL^2}{2}-\frac{L^3}{3},
$$

and

$$
\begin{aligned}
\mathcal C_p-a_p\Delta
&=\underbrace{\frac{L^2(p-L)}3}_{
\mathcal C_p-(p/3)\Delta}
+\underbrace{\frac{prL^2}{3(2r+p)}}_{
(p/3-a_p)\Delta}\\
&\ge0.
\end{aligned}
\tag{R44.9}
$$

For $s\ge x$, both contributions vanish. Thus the complete
measure-valued loss is

$$
\boxed{
\begin{aligned}
\mathcal C_p-a_p\Delta
={}&\int_{[0,r]}
\frac{p^3s}{3(2r+p)}\,d\nu(s)\\
&+\int_{(r,x)}
\left\{
\frac{L(s)^2(p-L(s))}{3}
+\frac{prL(s)^2}{3(2r+p)}
\right\}\,d\nu(s).
\end{aligned}}
\tag{R44.10}
$$

Here $L(s)=x-s$. Every displayed term is nonnegative, so

$$
\boxed{\mathcal C_p\ge a_p\Delta.}
\tag{R44.11}
$$

The Mathematica replay checks every polynomial residual in
(R44.7)--(R44.10).

## 3. Exact owner-specific terminal decompositions

### 3.1 Layer inverse and tangent remainders

Let

$$
g(s)=G_K(q+s),
\qquad
v=g(0)=B_0+\frac34.
$$

For $0<\ell<v$, define the strict superlevel inverse

$$
Y(\ell)=|\{s\ge0:g(s)>\ell\}|,
$$

and extend $Y(\ell)=0$ for $\ell\ge v$. It is decreasing and convex. For

$$
\ell_k=k-\frac14,\qquad 1\le k\le B_0,
$$

write

$$
y_k=Y(\ell_k),\qquad
c_k=-g'(y_k)=\frac{\theta_k}{\pi},\qquad
\eta_k=y_k-[y_k]_<.
$$

Away from an old inverse wall, $\eta_k\in(0,1)$. At a simultaneous wall
$y_k\in\mathbb N$, there are two selected values:

$$
\eta_k^{\rm lit}=1,\qquad \eta_k^-=0,
$$

where the second is the adverse outer-gap limit. Fix one old-level side
vector and use it consistently in both terminal decompositions below; write
its selected coordinate simply as $\eta_k\in[0,1]$. Thus every occurrence
of $D_A(q)$, $\Omega_-$, and the old-level count in a displayed identity
has the same literal or adverse ownership.

Set

$$
[y_k]_{<,\rm sel}:=y_k-\eta_k.
$$

This equals the literal strict bracket off a wall and on the literal wall;
on the adverse face it denotes the selected one-sided bracket limit.

Define the supporting tangent and its exact Bregman area by

$$
\Lambda_k(\ell)=y_k-\frac{\ell-\ell_k}{c_k},
$$

$$
\boxed{
\mathcal R_k
=2\int_{k-1}^{k}
\{Y(\ell)-\Lambda_k(\ell)\}\,d\ell\ge0.}
\tag{R44.12}
$$

The selected strict sample count at level $k$ (or its adverse one-sided
limit) is

$$
1+2[y_k]_{<,\rm sel}=2y_k+1-2\eta_k.
$$

Consequently, the exact $k$-th unit-layer contribution is

$$
\frac{\pi}{2\theta_k}-1+2\eta_k+\mathcal R_k.
\tag{R44.13}
$$

At the outer wall, $c_v=\beta$ and

$$
\Lambda_v(\ell)=\frac{v-\ell}{\beta}.
\tag{R44.14}
$$

Finally, put

$$
J=2\int_q^\mu G_\mu(z)\,dz,
$$

$$
\Omega_-=
\sum_{k=1}^{B_0}
\left(
\frac{\pi}{2\theta_k}-\frac{\pi}{2t}+2\eta_k
\right).
$$

Indeed,
$G_K(\mu)=v-u>B_0+1/4$, while
$\ell_k=k-1/4\le B_0-1/4$. Hence every old inverse lies strictly beyond
$\mu$, so $\theta_k<t$. With $\eta_k\ge0$, including the adverse one-sided
limit $\eta_k\downarrow0$, this proves

$$
\Omega_->0.
$$

Then

$$
\sum_{k=1}^{B_0}
\left(
\frac{\pi}{2\theta_k}-1+2\eta_k
\right)
=\Omega_-+B_0\zeta.
\tag{R44.15}
$$

### 3.2 Gap-side limiting owner

Approaching the wall from the gap side, the newest level is

$$
\ell_B=B-\frac14=B_0+\frac34=v,
\qquad
y_B\downarrow0.
$$

Its tangent is (R44.14), and its tangent contribution is

$$
\frac1{2\beta}-1.
$$

The shell/ball count relation is

$$
D_A(q)=D_K^+(q)+(B-Q)-J,
\qquad
B-Q=1.
$$

The $-1$ from the newest ball level is therefore cancelled exactly once by
the shell-count surplus. Define

$$
\boxed{
L_T^+=\Omega_-+B_0\zeta+\frac1{2\beta}-J.}
\tag{R44.16}
$$

The complete exact remainder is

$$
\boxed{
\begin{aligned}
\mathcal R_{\rm tan}^+
={}&\sum_{k=1}^{B_0}\mathcal R_k\\
&+2\int_{B_0}^{B_0+1}
\left\{
Y(\ell)-\frac{v-\ell}{\beta}
\right\}\,d\ell
\ge0.
\end{aligned}}
\tag{R44.17}
$$

The zero extension of $Y$ makes the endpoint tangent a supporting line even
on $[v,B_0+1]$. Thus

$$
\boxed{D_A(q)=L_T^++\mathcal R_{\rm tan}^+.}
\tag{R44.18}
$$

### 3.3 Literal-wall owner

At the literal wall, $B_{\rm lit}=B_0=Q$, so the shell/ball count surplus is
zero. The old complete levels occupy $[0,B_0]$. The remaining top layer is

$$
2\int_{B_0}^{v}Y(\ell)\,d\ell
=\frac{(v-B_0)^2}{\beta}
+2\int_{B_0}^{v}
\{Y(\ell)-\Lambda_v(\ell)\}\,d\ell.
$$

Because $v-B_0=3/4$, define

$$
\boxed{
L_T^0=\Omega_-+B_0\zeta+\frac9{16\beta}-J,}
\tag{R44.19}
$$

$$
\boxed{
\begin{aligned}
\mathcal R_{\rm tan}^0
={}&\sum_{k=1}^{B_0}\mathcal R_k\\
&+2\int_{B_0}^{v}
\left\{
Y(\ell)-\frac{v-\ell}{\beta}
\right\}\,d\ell
\ge0.
\end{aligned}}
\tag{R44.20}
$$

Therefore

$$
\boxed{D_A(q)=L_T^0+\mathcal R_{\rm tan}^0.}
\tag{R44.21}
$$

### 3.4 Exact ownership reconciliation

The old-level integrals in (R44.17) and (R44.20) are identical. On
$v\le\ell\le B_0+1$, the zero extension gives $Y(\ell)=0$. Hence

$$
\begin{aligned}
\mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0
&=2\int_v^{B_0+1}\frac{\ell-v}{\beta}\,d\ell\\
&=\frac{(B_0+1-v)^2}{\beta}
=\boxed{\frac1{16\beta}}.
\end{aligned}
\tag{R44.22}
$$

Also $L_T^0-L_T^+=1/(16\beta)$, so (R44.18) and (R44.21) decompose the same
defect. The quantity $1/(16\beta)$ is ownership reconciliation, not a new
reserve created by changing owners.

Thus the exact endpoint geometry may be evaluated at $\mu=q+1$ while a
gap-side label is retained. The shell outer-endpoint count $Q=B_0$ is
literal and unchanged. The defect $D_A(q)$ is evaluated on the same fixed
old-inverse side vector in both decompositions (literal or adverse); apart
from a possible adverse old-level choice, only $D_K^+$, $B$, and the
compensating $B-Q=1$ are outer-action one-sided bookkeeping.

### 3.5 Intrinsic top-Bregman reserve

If $z=q+Y(\ell)$ and $\theta=\arccos(z/K)$, inverse differentiation gives

$$
Y''(\ell)=
\frac{\pi^2}{\sqrt{K^2-z^2}\,\theta^3}.
$$

For $B_0\le\ell\le v$, one has $z\ge q$ and
$\theta\le\pi\beta$. Therefore

$$
Y''(\ell)\ge
\frac1{\pi\sqrt{K^2-q^2}\,\beta^3}.
$$

Taylor's formula about $v$, followed by one integration over the
length-$3/4$ top interval, yields

$$
\boxed{
\mathcal R_{\rm tan}^0\ge
\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}>0.}
\tag{R44.23}
$$

Only the top integral in (R44.20) is used; all old Bregman areas are
discarded as nonnegative.

## 4. Exact Gate-B and Round 42 ledgers

Substituting (R44.18) and (R44.21) into (R44.1) gives

$$
\boxed{
\mathscr S=L_T^++\mathcal R_{\rm tan}^+
+\mathcal C_p+p(E-E_*).}
\tag{R44.24}
$$

and

$$
\boxed{
\mathscr S=L_T^0+\mathcal R_{\rm tan}^0
+\mathcal C_p+p(E-E_*).}
\tag{R44.25}
$$

Since $E=\Delta+2e_p$, the audited Round 42 endpoint identity is exactly

$$
\boxed{
\Phi_\delta^+
=L_T^++a_p\Delta+p(E-E_*).}
\tag{R44.26}
$$

Indeed, its shelf part becomes

$$
(p+a_p)\Delta+2pe_p-\frac{p-dm}{2},
$$

which is exactly the shelf part in (R42.9). There is no notation conflict
with the audited Round 42 formula.

Subtracting (R44.26) from (R44.24), then using (R44.22), gives the complete
exact loss ledger:

$$
\boxed{
\mathscr S-\Phi_\delta^+
=\mathcal R_{\rm tan}^+
+(\mathcal C_p-a_p\Delta),}
\tag{R44.27}
$$

$$
\boxed{
\mathscr S-\Phi_\delta^+
=\frac1{16\beta}+\mathcal R_{\rm tan}^0
+(\mathcal C_p-a_p\Delta).}
\tag{R44.28}
$$

Every term on the right of (R44.28) is explicit and nonnegative. The
Mathematica replay returns zero for both scalar-ledger residuals and for the
two-owner difference.

## 5. One intrinsic sign attempt and negative-support theorem

The literal exact sign problem is

$$
\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p
\ge p(E_*-E).
\tag{R44.29}
$$

No complete continuum proof of (R44.29) was found. Nevertheless, (R44.5)
and (R44.23) give one intrinsic localization theorem for every possible
negative point, without a $B_0$-, $j$-, $f$-, ratio-, or chamber-indexed
split:

$$
\boxed{
\begin{aligned}
\mathscr S<0\quad\Longrightarrow\quad
p(E_*-E)>{}&
\Omega_-+B_0\zeta+\frac9{16\beta}-J\\
&+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}
-\frac1{\sqrt{K^2-r^2}}
\right).
\end{aligned}}
\tag{R44.30}
$$

This is the contrapositive of the lower bound obtained directly from
(R44.25), retaining the exact $\Omega_-$, phase, cap, and top triangle, and
replacing only the two exact positive remainders by their proved lower
bounds.

Using the audited phase sign and strict facts

$$
\Omega_->0,\qquad
B_0\zeta>\frac15,\qquad
\beta<\frac12,\qquad
J<\frac1{10},
$$

gives the count-free corollary

$$
\boxed{
\begin{aligned}
\mathscr S<0\quad\Longrightarrow\quad
p(E_*-E)>{}&
\frac{49}{40}
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}
-\frac1{\sqrt{K^2-r^2}}
\right).
\end{aligned}}
\tag{R44.31}
$$

Equations (R44.30)--(R44.31) are support localizations, not renamed
projected targets. They retain one intrinsic continuous inequality and do
not authorize a positive coverage certificate. None of the 34 complete-owner
records in the widened primary diagnostic entered the support permitted by
(R44.30).

What remains open is to prove that the support in (R44.30) is empty on the
entire exact owner, or to sign (R44.29) by a sharper correlated use of the
old Bregman areas and shelf geometry.

## 6. Equality and ownership audit

| face | exact owner and effect |
|---|---|
| $A(r+s)+1/4\in\mathbb Z$ | The first shelf uses the literal ordinary floor; the corresponding fractional remainder is $0$. No continuity across a floor jump is used. |
| $G_K(q)+1/4=B\in\mathbb Z$ | The literal strict ball count is $B_0=B-1$. The one-sided $B$ occurs only with the compensating $B-Q=1$. |
| $A(q)+1/4\in(B-1,B)$ | It equals $B-h$ with $0<h<1/2$, so the shell terminal count is literally $Q=B_0$. |
| old $y_k\in\mathbb Z$ | Literal ownership has $[y_k]_< =y_k-1$ and $\eta_k=1$; the adverse side has $\eta_k\downarrow0$ and loses exactly two units per collided old level. The diagnostics keep the two values separate. |
| newest $y_B=0$ | This is the outer-action jump, not an old inverse wall. It occurs once in (R44.17), and its $-1$ is cancelled once by $B-Q=1$. |
| $e_p=0$ | Equations (R44.3)--(R44.31) remain valid. The simultaneous outer-$B$/lower-shelf endpoint is already closed by audited Round 39 and is not silently re-proved. |
| $E=E_*$ | Equality belongs to the automatic sector. In (R44.25) the negative shelf term vanishes. The live owner has the strict inequality $E<E_*$. |
| curvature/elasticity switch | The exact $\mathscr S$ and hinge proof use neither branch of $M_4$; no derivative assertion is made across that exhausted projected switch. |
| $B_0=1$ | Every sum has one old level; the top triangle and (R44.23) remain literal. |
| integer grid | $r\in\mathbb N$, $r\ge1$, for even $D$. The exact activity constant is $((D-2)^2-1)/4$; the searches use the weaker parity minimum $3/4$. |
| half-integer grid | $r\in\mathbb N_0+1/2$, $r\ge3/2$, for odd $D$. The exact activity constant is $((D-2)^2-1)/4$; the searches use the weaker parity minimum $2$. |
| activity equality | It belongs to the dimension-$D$ no-mode owner. Gate B uses strict activity; the weakest-grid enlargement is stated separately. |
| $\alpha\uparrow1^-$ | Re-solve the wall as $\mu=q+\alpha$ changes, then take the limit. At the endpoint evaluate $\mu=q+1$ while retaining the old chart's one-sided label; do not identify it with the next chart's literal $\alpha=0$. |
| gap-side versus literal wall | Equations (R44.18) and (R44.21) are reconciled by (R44.22), not by continuity across a count jump. |

## 7. Falsification and replay report

### 7.1 Mathematica exact replay

The installed Wolfram runtime was used on
computations/general_d_round44_exact_gate_b_replay.wl. It returned zero for
the action derivatives, shelf weight, every hinge loss, terminal ownership
difference, remainder-tail integral, top-Bregman coefficient, both Gate-B
ledgers, and the Round 42 endpoint identity, ending in

~~~text
round43FixtureChecks=True
round44ExactGateBReplayOK=True
~~~

For the mandatory Round 43 tuple

$$
(r,p,m,f,B,j)=(1,9,9,4,3,1),
$$

the replay gives

$$
E\approx0.3280024861>E_*\approx0.2913519205,
$$

so the point is rejected exactly where required. Its signed quantities are

$$
D_A(q)\approx8.1310696768,\qquad
\mathcal C_p\approx0.8272330607,
$$

$$
\Phi_\delta^+\approx8.2410438437,\qquad
\mathscr S\approx9.2881578274>0.
$$

It also gives

$$
\mathcal R_{\rm tan}^+\approx1.0095687427,\qquad
\mathcal R_{\rm tan}^0\approx0.8035812256,
$$

whose difference agrees with $1/(16\beta)$ beyond 60 decimal places, and
checks $\mathcal C_p>0.8272>0.7569$, where the last value is the elementary
curvature reserve (R44.5).

### 7.2 Primary high-precision endpoint diagnostic

computations/general_d_round44_exact_gate_b_diagnostic.py independently
computes the direct strict sum defining $D_A(q)$, the exact trapezoid, both
terminal decompositions, every owner test, and the full ledger at 80 decimal
digits. Each outer wall is solved by 230 monotone bisections; the initial
signs and final bracket are checked.

The widened command

~~~text
python -B computations/general_d_round44_exact_gate_b_diagnostic.py \
  --r-max 12 --p-max 25 --m-max 15 --b-max 12
~~~

tested 92,455 endpoint candidates and retained 34 complete-owner records:
21 on the integer grid and 13 on the half-integer grid. It found

~~~text
negative_S_records=0
records_surviving_analytic_negative_support_localization=0
~~~

The observed minimum was

$$
(r,p,m,f,B,j)=(1,3,1,2,2,0),
$$

with ledger

$$
\begin{array}{rcl}
D_A(q)&\approx&3.053829516820198,\\
L_T^+&\approx&2.347794631703397,\\
L_T^0&\approx&2.518090276052740,\\
\mathcal R_{\rm tan}^+&\approx&0.706034885116801,\\
\mathcal R_{\rm tan}^0&\approx&0.535739240767458,\\
\mathcal C_p&\approx&0.147126401935798,\\
a_p\Delta&\approx&0.132357005317744,\\
p(E_*-E)&\approx&0.506390639855641,\\
\Phi_\delta^+&\approx&1.973760997165501,\\
\mathscr S&\approx&2.694565278900355.
\end{array}
$$

The restored reserve was approximately $0.720804281734854$. The minimum
margin against the necessary support condition (R44.30) was approximately
$2.217590566975083$. Across all retained records, the largest absolute
terminal-ledger residual was $1.30\times10^{-80}$, the largest scalar-ledger
residual was $2.54\times10^{-80}$, and the least observed gap between the
exact trapezoid and (R44.5) was approximately $0.0069051881$.

The roots were separately re-solved at
$\alpha=1-10^{-j}$ for $j=2,4,6,8,10$. At the minimum tuple the corresponding
$\mathscr S$ values were

$$
2.7137278107,\quad
2.6947571044,\quad
2.6945671972,\quad
2.6945652981,\quad
2.6945652791,
$$

converging to the exact endpoint value. The wall parameter $t$ was re-solved
at every $\alpha$; it was not held fixed.

No retained record lay exactly on an old inverse wall. The code nevertheless
implements the literal $\eta_k=1$ and adverse $\eta_k=0$ owners separately
and subtracts the corresponding two-unit direct-count jump before choosing
the adverse side.

### 7.3 Independent adversarial search

The separately authored
computations/general_d_round44_independent_gate_b_search.py used a different
proposal engine, exact-owner filter, analytic antiderivatives, and
high-precision replay. It generated 629,288 proposals and retained 296
complete owners at 90 decimal digits: 155 on the integer grid and 141 on the
half-integer grid.

It found no negative $\mathscr S$. Its minimum was again

$$
\mathscr S=
2.69456527890035502562933\ldots
$$

at $(r,p,m,f,B,j)=(1,3,1,2,2,0)$. A 120-decimal rerun retained the same 296
owners and the same minimizing tuple and value. Selected wall brackets and
the mandatory historical regressions were rechecked with 512-bit Arb
directed arithmetic. These data are diagnostic, not a coverage proof.

### 7.4 Round 27 directed regression

Both diagnostic paths preserve the Round 27 automatic-sector witness

$$
(r,p,m,f,\alpha,\mu,t)
=\left(4036,32,1,2,\frac1{16},\frac{65105}{16},\frac{79}{500}\right).
$$

The existing independent 512-bit Arb replay certifies

$$
\mathcal C_{\max,8}<-\frac43,\qquad
\mathcal R_J<-\frac65,\qquad
\mathscr S>47,\qquad
\Phi_\delta>40,
$$

and automaticSectorCertified=True. Thus negative rejected projected scalars
coexist with a large positive exact target; the fixture is excluded from the
hard owner because $E>E_*$.

All endpoint sweeps are floating/high-precision diagnostics only. Their
failure to find a negative point is neither a proof nor a positive coverage
certificate. No directed full-owner Round 44 negative certificate was found.

## 8. Independent reconstruction and audit

Prompt B's clean-room Sections 1--5 were frozen before this lead note was
available. That reconstruction independently obtained
\(B_{\rm lit}=Q=B-1\), both terminal decompositions and their complete
integrals, the \(1/(16\beta)\) reconciliation, both shelf identities, the
elementary curvature reserve, both exact Gate-B representations, and the
\(\mathscr S-\Phi_\delta^+\) ledger. Its covariance proof of
\(\mathcal C_p\ge a_p\Delta\) is independent of the lead's hinge proof. After
the freeze it checked the top-Bregman coefficient and (R44.30), finding exact
agreement. Its verdict is

~~~text
STRUCTURAL PASS — FINAL SIGN OPEN
~~~

Prompt D's final independent audit answered all ten required questions. It
confirmed the fixed old-inverse side convention, the exact ambient-\(D\)
activity owner and weakest-grid computational enlargement, every remainder
sign, the \(9/64\) coefficient, the \(49/40\) corollary, and the absence of
any reuse of an exhausted projected scalar. It reran Mathematica, the widened
92,455-candidate primary diagnostic, and the full 629,288-proposal
adversarial search. The latter two again retained 34 and 296 owners,
respectively, with no negative \(\mathscr S\); they remain non-covering
diagnostics. The audit found no unrepaired strictness or ownership error and
gave the same verdict:

~~~text
STRUCTURAL PASS — FINAL SIGN OPEN
~~~

Only after this verdict were the narrative directives, current state, gap
register, and lemma bank synchronized. The proof graph and manuscript remain
unchanged.

## 9. Proved, conditional, diagnostic, and open statements

| class | statement |
|---|---|
| **proved** | Shelf identities (R44.3)--(R44.4), all derivative signs, elementary curvature reserve (R44.5), complete hinge ledger (R44.10), both exact terminal decompositions, reconciliation (R44.22), top-Bregman reserve (R44.23), exact Gate-B/Round-42 ledgers (R44.24)--(R44.28), and the necessary negative-support localization (R44.30)--(R44.31). |
| **conditional** | Any owner point violating the strict support condition in (R44.30) has $\mathscr S\ge0$. A point inside that support still requires the exact sign (R44.29). |
| **diagnostic** | The 92,455-candidate primary sweep, 629,288-proposal adversarial search, retained owners, observed common minimum, and one-sided $\alpha$ convergence. |
| **directed historical regression** | The Round 27 automatic-sector witness only; it is not a Round 44 endpoint certificate. |
| **failed/open** | A continuum proof that (R44.30)'s possible-negative support is empty. No proof of $\mathscr S\ge0$ on the full endpoint owner is claimed. |

## 10. Gate decision and next single obligation

Round 44 meets the approved partial-success criterion: it proves the exact
owner-specific loss ledger and one intrinsic localization theorem for every
possible negative point without a forbidden split. It does not produce a
certified negative point.

~~~text
Gate A: stopped (inherited Round 43 decision)
Gate B: continues, localized by (R44.30)
Gate C: not activated
~~~

The next single proof obligation is to prove that the strict support in
(R44.30) is empty on the complete owner, using the still-retained old-level
Bregman areas and exact first-shelf geometry, or to sign (R44.29) directly
there. It must remain one intrinsic theorem and may not split by
$B_0,j,f$, ratio intervals, or chambers.

The conditional higher-$Q_N$ or Gate-C work in the prompt is not executed,
because Round 44 does not authorize either transition.

## 11. Files and commit provenance

Round 44 creates or updates the following scoped artifacts:

~~~text
human/inbox/general-d-round-44-codex-prompts.md
human/outbox/general-d-round-44-exact-gate-b-terminal-trapezoid-reconstruction.md
human/outbox/general-d-round-44-clean-room-gate-b-reconstruction.md
human/outbox/general-d-round-44-adversarial-exact-scalar-falsification.md
human/outbox/general-d-round-44-independent-audit.md
computations/general_d_round44_exact_gate_b_replay.wl
computations/general_d_round44_exact_gate_b_diagnostic.py
computations/general_d_round44_independent_gate_b_search.py
human/current_directives.md
state/current_state.md
state/gap_register.md
state/lemma_bank.md
~~~

state/proof_obligations.yml and
manuscript/spherical-shell-polya-general-d.tex remain unchanged.

The final delivery commit SHA is reported by Git and in the task handoff. A
commit cannot contain its own SHA: inserting that SHA changes the commit
object and therefore its SHA. This note records the immutable base above and
will record the pre-delivery audited artifact SHA after that commit is made;
the actual final branch SHA must remain non-self-referential in the handoff.

**Audited artifact commit SHA:** 2a0e51ecbb1534eeea94615ab94717fa126c0c5d  
**Final delivery commit SHA:** reported in the task handoff.
