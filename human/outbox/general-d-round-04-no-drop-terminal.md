# General dimension, Round 4b: exact-angle closure sectors for \(p=n\)

Date: 18 July 2026

Status: rigorous automatic sector and chamberwise finite reduction. This
note combines the exact no-drop identity from the
[Round 4 no-drop note](general-d-round-04-no-drop.md) with the independently
audited convex-tail reserve from the
[Round 4 high-floor note](general-d-round-04-high-floor.md). It does not
claim a uniform proof of every no-drop tail.

## 1. Correlated no-drop data

Let

\[
 \mu=\rho K,\qquad
 n=\lfloor\mu-r\rfloor,\qquad
 q=r+n,
\]

and suppose the ordinary floors do not drop before the interface:

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \qquad(0\le j\le n),
 \qquad f\ge2.
 \tag{1}
\]

Put

\[
 \varepsilon=A(q)+\frac14-f\in[0,1),
 \qquad
 \varepsilon_0=A(r)+\frac14-f,
 \qquad
 \Delta=\varepsilon_0-\varepsilon,
\]

and

\[
 \sigma=-A',\qquad
 R_n=2\int_r^qA(z)\,dz-2nf.
\]

The exact no-drop formula is

\[
 \boxed{
 R_n=-\frac n2+2n\varepsilon
 +2\int_0^n u\,\sigma(r+u)\,du.}
 \tag{2}
\]

Define the exact unpaid head deficit

\[
 \boxed{
 H_n:=\max\{0,-R_n\}
 =\max\left\{0,
 \frac n2-2n\varepsilon
 -2\int_0^n u\,\sigma(r+u)\,du\right\}.}
 \tag{3}
\]

In particular,

\[
 0\le H_n\le\frac n2.
 \tag{4}
\]

The scale-free shelf-curvature estimate in the high-floor note gives the
sharper explicit majorant

\[
 \boxed{
 H_n\le H_n^{\mathrm{curv}}:=
 \max\left\{0,
 n\left(\frac12-2\varepsilon-\Delta\right)
 -\frac{n^2\Delta}{3(2r+n)}\right\}.}
 \tag{5}
\]

Indeed, its formula (9), with \(p=n\), is

\[
 R_n\ge
 \frac{n^2\Delta}{3(2r+n)}
 +n\left(2\varepsilon+\Delta-\frac12\right).
\]

Let

\[
 Q=\left[A(q)+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,
\]

where \([x]_<:=\max\{0,\lceil x\rceil-1\}\). Monotonicity of the strict
bracket and \(G_K(q)\ge A(q)\) imply

\[
 B\ge Q.
 \tag{6}
\]

The ordinary/strict endpoint convention is completely explicit:

\[
 \boxed{
 Q=
 \begin{cases}
 f-1,&\varepsilon=0,\\
 f,&0<\varepsilon<1.
 \end{cases}}
 \tag{7}
\]

Thus \(Q\ge1\) throughout this note.

## 2. Exact-angle combined certificate

For \(1\le k\le B\), let \(\theta_k\in(0,\pi/2]\) solve

\[
 \frac K\pi
 \bigl(\sin\theta_k-\theta_k\cos\theta_k\bigr)
 =k-\frac14,
 \tag{8}
\]

and put

\[
 \delta_\mu(q)=\int_q^\mu G_\mu(z)\,dz.
\]

The audited exact-angle terminal estimate is

\[
 D_A(q)\ge
 \max\left\{0,
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\delta_\mu(q)\right\}.
 \tag{9}
\]

The reduced no-drop scalar is

\[
 \mathscr S_n=D_A(q)+R_n.
\]

Combining (3) and (9) proves the following automatic sector.

### Proposition 2.1

Every no-drop tail satisfying

\[
 \boxed{
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 \ge Q+2\delta_\mu(q)+H_n}
 \tag{10}
\]

has \(\mathscr S_n\ge0\). It is enough to replace \(H_n\) in (10) by
the explicit upper bound \(H_n^{\mathrm{curv}}\) from (5).

#### Proof

The right side of the maximum in (9) is then at least \(H_n\).
Consequently \(D_A(q)\ge H_n\ge-R_n\), which proves the claim.

This criterion retains the exact endpoint fraction, the exact cap, every
strict wall, and the exact ball slopes. No independent universal bound
has yet been substituted into either side.

## 3. A root-free high-energy sector

Set

\[
 C_0=\frac\pi2\left(\frac{2}{3\pi^2}\right)^{1/3},
 \qquad
 c_*=\frac{4\sqrt2}{15},
\]

and, for \(J\ge1\), define

\[
 S_J=\sum_{k=1}^{J}\left(k-\frac14\right)^{-1/3}.
 \tag{11}
\]

The root-free terminal estimate and the one-interface turning cap give

\[
 D_A(q)\ge
 \max\{0,C_0K^{1/3}S_B-Q-c_*\}.
 \tag{12}
\]

Since \(B\ge Q\), equations (3), (5), and (12) yield two directly
checkable sufficient conditions:

\[
 \boxed{
 C_0K^{1/3}S_B
 \ge Q+c_*+H_n^{\mathrm{curv}}}
 \quad\Longrightarrow\quad
 \mathscr S_n\ge0,
 \tag{13}
\]

and the coarser purely discrete condition

\[
 \boxed{
 C_0K^{1/3}S_Q
 \ge Q+c_*+\frac n2}
 \quad\Longrightarrow\quad
 \mathscr S_n\ge0.
 \tag{14}
\]

Define the explicit no-drop cutoff

\[
 \boxed{
 K_{\mathrm{nd}}(n,Q)
 :=
 \left(
 \frac{Q+n/2+c_*}{C_0S_Q}
 \right)^3.}
 \tag{15}
\]

### Proposition 3.1

Every high-floor no-drop tail with

\[
 K\ge K_{\mathrm{nd}}(n,Q)
 \tag{16}
\]

satisfies \(\mathscr S_n\ge0\).

#### Proof

Condition (16) is exactly (14). Alternatively, (12) gives
\(D_A(q)\ge n/2\), while (2) gives \(R_n\ge-n/2\).

The cutoff can be sharpened on a fixed chamber by retaining \(B\):

\[
 K_{\mathrm{nd}}(n,Q,B)
 :=
 \left(
 \frac{Q+n/2+c_*}{C_0S_B}
 \right)^3
 \le K_{\mathrm{nd}}(n,Q).
 \tag{17}
\]

It can be sharpened further by replacing \(n/2\) with (5), or by using
the exact-angle condition (10).

## 4. Active geometry makes every fixed discrete branch finite

Write \(\delta=K-\mu\). Since

\[
 A(0)=\frac{\delta}{\pi},
\]

and \(A\) is strictly decreasing at the positive shift \(r\), (1) gives

\[
 \delta>\pi\left(f-\frac14\right).
 \tag{18}
\]

Also \(q=r+n\le\mu\). Hence every such tail satisfies

\[
 \boxed{
 K>\pi\left(f-\frac14\right)+r+n.}
 \tag{19}
\]

Combining (16) and (19) gives a purely discrete automatic test:

\[
 \boxed{
 \pi\left(f-\frac14\right)+r+n
 \ge K_{\mathrm{nd}}(n,Q)
 \quad\Longrightarrow\quad
 \mathscr S_n\ge0.}
 \tag{20}
\]

Indeed, the actual \(K\) is strictly larger than the left side of (20).
Without fixing the endpoint wall, one may require (20) for both
\(Q=f-1\) and \(Q=f\).

Conversely, every branch not closed by Proposition 3.1 lies in the
explicit compact strip

\[
 \boxed{
 \pi\left(f-\frac14\right)+r+n
 <K<K_{\mathrm{nd}}(n,Q),\qquad
 r+n\le\mu<r+n+1.}
 \tag{21}
\]

For fixed \((n,f,Q)\), (21) leaves only finitely many positive
integer/half-integer shifts:

\[
 \boxed{
 \frac12\le r<
 K_{\mathrm{nd}}(n,Q)
 -\pi\left(f-\frac14\right)-n.}
 \tag{22}
\]

It also bounds all remaining discrete terminal data. Indeed,

\[
 B\le
 \left\lfloor\frac{K}{\pi}+\frac14\right\rfloor
 <
 \frac{K_{\mathrm{nd}}(n,Q)}{\pi}+\frac14,
 \tag{23}
\]

and a terminal sample can contribute only when
\(q+j<K<K_{\mathrm{nd}}(n,Q)\). Thus only finitely many indices \(j\)
and wall levels occur in (21).

On every open chamber with these discrete data fixed, the exact no-drop
note proved

\[
 \partial_K\mathscr S_n>0,\qquad
 \partial_\mu\mathscr S_n<0.
 \tag{24}
\]

Consequently the compact strip reduces to its lower-\(K\), upper-\(\mu\)
faces and the finitely many one-sided head and terminal sample walls.
Equations (21)--(24) are therefore a genuine finite wall reduction for
each fixed \((n,f,Q)\), not merely a bounded numerical search proposal.

## 5. The endpoint wall is a separate lower-dimensional branch

Formula (7) should not be blurred by a limiting argument.

* If \(0<\varepsilon<1\), then \(Q=f\) and \(B\ge f\).
* If \(\varepsilon=0\) and \(q<\mu\), then
  \(h=G_\mu(q)>0\), so
  \[
  G_K(q)+\frac14=f+h
  \]
  and therefore \(Q=f-1\) but \(B\ge f=Q+1\). In this branch one may
  use \(S_f\), rather than \(S_{f-1}\), in (13) and (17).
* If \(\varepsilon=0\) and \(q=\mu\), then \(h=0\) and
  \(B=Q=f-1\). This is the pure-ball interface corner and must be
  retained as its own equality face.

Thus the apparently weaker \(Q=f-1\) cutoff occurs without an extra ball
level only at the codimension-two corner

\[
 A(q)=f-\frac14,\qquad q=\mu.
 \tag{25}
\]

## 6. Exact status

The combination closes the following rigorous sector:

\[
 K\ge K_{\mathrm{nd}}(n,Q),
\]

with sharper exact-angle and curvature-sensitive versions (10) and (13).
Every remaining fixed \((n,f,Q)\) branch is reduced to the finite wall
problem (21)--(24), and the strict endpoint wall is split exactly as in
Section 5.

This is not yet a global finite certificate because the pairs \((n,f)\)
are not uniformly bounded by the present argument. A full proof of the
no-drop branch still requires either:

1. a uniform comparison showing that (10) holds below the cutoff as
   well; or
2. an exhaustion argument bounding the residual pairs \((n,f)\), followed
   by the finite wall certificates supplied by (21)--(24).
