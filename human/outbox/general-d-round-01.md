# General dimension \(d\ge 3\): round 01

Date: 18 July 2026  
Primary strategy: human/inbox/general-d_1.md  
Status: the dimension lift is rigorous; the shifted-tail theorem is still open.

## 1. Outcome of this round

The general-dimensional argument now has a clean conditional closure. Put

\[
 p=d-2,\qquad a_d=\frac p2,\qquad
 r_m=m+\frac p2,\qquad
 c_{d,m}=\binom{m+p-1}{p-1}.
\]

For the strict action proxy

\[
 P_d^{<}=\sum_{\ell\ge0}\kappa_{d,\ell}
 \left[A(\ell+a_d)+\frac14\right]_{<},
\]

the exact branching identity is

\[
 P_d^{<}=\sum_{m\ge0}c_{d,m}T_A(r_m),
\qquad
 T_A(r)=
 \left[A(r)+\frac14\right]_{<}
 2\sum_{j\ge1}\left[A(r+j)+\frac14\right]_{<}.
\]

Define

\[
 D_A(r)=2\int_r^K A(z)\,dz-T_A(r).
\]

The signed branching primitive \(\Delta_d\) satisfies \(\Delta_d\le0\), and
the exact defect identity is

\[
 \boxed{
 W_d-P_d^{<}
 =
 \mathcal B_d(A)+\sum_{m\ge0}c_{d,m}D_A(r_m),
 \qquad
 \mathcal B_d(A)\ge0.}
\]

Here

\[
 W_d
 =
 \frac{1-\rho^d}{2^d\Gamma(d/2+1)^2}K^d
 =
 L_d|A_{\rho,1}^{(d)}|K^d.
\]

Thus the single dimension-free statement

\[
 \tag{ST}
 T_A(r)\le 2\int_r^K A(z)\,dz
 \qquad
 \left(r\in\tfrac12\mathbb N\right)
\]

implies the sharp Dirichlet Pólya inequality for every spherical shell and
every \(d\ge3\). The spectral separation, real-order phase estimate,
branching, signed primitive, Weyl normalization, strict-wall handling,
dilation, and no-mode region introduce no remaining dimension-dependent
analytic gap.

## 2. Repairs made to the final strategy

The signed-primitive proof needs two small endpoint repairs:

1. on \(0\le z<r_0=p/2\),
   \[
   \Delta_d(z)=-\frac{z^{p+1}}{(p+1)!};
   \]
2. because the staircase uses \(r_m\le z\), its cells are
   \([r_M,r_{M+1})\), not closed at the right endpoint.

With these conventions, the AM--GM proof is complete:

\[
 (p+1)!\Delta_d(r_M)
 =
 \prod_{j=0}^{p}(M+j)
 -
 \left(M+\frac p2\right)^{p+1}
 \le0,
\]

and at the only possible interior cell maximum,

\[
 (p+1)!\Delta_d(z_M^*)
 =
 p(z_M^*)^p
 \left(z_M^*-M-\frac{p+1}{2}\right)
 \le0.
\]

## 3. The proposed one-cell pairing is false

For \(x_j=r+j\), \(Q_j=[A(x_j)+1/4]_<\), and
\(e_j=A(x_j)+1/4-Q_j\), the correct recurrence is

\[
 D_j-D_{j+1}
 =
 C_j-\frac12+e_j+e_{j+1},
\qquad
 C_j=2\int_{x_j}^{x_j+1}A-A(x_j)-A(x_j+1).
\]

The suggestion in general-d_1.md that every negative inner-cell
increment can be paired with the next floor-drop increment is not valid.
For example,

\[
 (\rho,K,r)=(0.1,27.475,0.5),\qquad \mu=\rho K=2.7475,
\]

gives

\[
 D_0-D_1=-0.3730139470,\qquad
 D_1-D_2=0.2867845833,
\]

although the second cell is the next floor-drop cell. Their sum is
\(-0.0862293637\). No sample is on a strict-floor wall.

Moreover, at

\[
 (\rho,K,r)=(0.6,7.45,0.5),
\]

the cumulative increment through the interface/drop cell is still
\(-0.4013073106\); the first outer zero-count cell contributes
\(+0.8627561192\) and restores positivity. Therefore the correct block
target must retain the convex outer-tail reserve:

\[
 \boxed{
 D_0=\sum_{j=0}^{J-1}(D_j-D_{j+1})+D_J\ge0,}
\]

where \(J\) is the first outer-tail index and \(D_J\) needs a quantitative,
not merely nonnegative, lower bound.

These examples do not disprove (ST); they disprove only the proposed local
pairing proof.

## 4. First interface-cell progress

Assume \(0<\mu-r<1\). Let \(D_K(r)\) denote the strict ball-tail defect and
put

\[
 n_0=
 \left[G_K(r)+\frac14\right]_{<}
 -
 \left[G_K(r)-G_\mu(r)+\frac14\right]_{<},
\qquad
 \delta_\mu(r)=\int_r^\mu G_\mu(z)\,dz.
\]

Then the exact identity is

\[
 \boxed{D_A(r)=D_K(r)+n_0-2\delta_\mu(r).}
\]

The turning cap gives

\[
 2\delta_\mu(r)
 <
 \frac{4(\mu-r)^{5/2}}{15\sqrt\mu}
 <
 \frac{4\sqrt2}{15}<1.
\]

Consequently (ST) is proved in the one-interface regime if:

- \(n_0\ge1\);
- \(G_K(\max\{r,K/2\})\ge1\); or
- \(r\ge K/2\).

The last case uses a new low-action \(1/3\)-Lipschitz reserve:
if \(g\) is strictly decreasing and convex, \(g(b)=0\),
\(\operatorname{Lip}(g)\le1/3\), and \(3/4<g(0)<1\), then its strict
shifted-tail defect is \(>11/16\).

Only the bounded nine-shift residual family remains:

\[
 r<K/2,\qquad
 K<1/\omega_0,\qquad
 n_0=0,\qquad
 \omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\]

with

\[
 r\in
 \left\{\frac12,1,\frac32,2,\frac52,3,\frac72,4,\frac92\right\}.
\]

The two-variable residual reduces further. Put

\[
 B=G_K(r)+\frac14,\qquad
 q=[B]_<,\qquad
 e=B-q\in(0,1].
\]

Strict-wall exactly,

\[
 n_0=0\quad\Longleftrightarrow\quad G_\mu(r)<e.
\]

Since \(G_\mu\) lies strictly below its endpoint chord on \([r,\mu]\),

\[
 2\delta_\mu(r)<G_\mu(r)(\mu-r)<e.
\]

It is therefore sufficient to prove the one-variable ball reserve

\[
 E_r(K):=D_K(r)-e\ge0.
\]

Away from sample walls,

\[
 \pi E_r'(K)
 =
 K\left(
 \arccos\frac rK
 -\frac rK\sqrt{1-\frac{r^2}{K^2}}
 \right)
 -
 \sqrt{1-\frac{r^2}{K^2}},
\]

and \(E_r''(K)>0\) throughout the residual range. The derivative is already
positive at the relevant left endpoint, so \(E_r\) increases strictly
between walls. A first-sample wall changes both \(D_K\) and \(e\) by one
and leaves \(E_r\) continuous; a later-sample wall lowers \(E_r\) by two.
Thus only finitely many right-hand wall values remain:

\[
 G_K(r+j)=n-\frac14,
 \qquad
 n\in\{1,2,3\},\quad r+j<10.
\]

High-precision reconnaissance, not a proof, found the following smallest
wall margins:

| \(r\) | \(1/2\) | \(1\) | \(3/2\) | \(2\) | \(5/2\) | \(3\) | \(7/2\) | \(4\) | \(9/2\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\min E_r\) | .2427 | .3308 | .4095 | .4810 | .5469 | .6080 | .6653 | .7193 | 2.2724 |

For \(r\le4\), every observed minimum is the first later wall
\(G_K(r+1)=3/4\). The remaining first-interface obligation is now a small
finite interval certificate for these scalar wall values; the
\(\mu\)-dependence and the strict-wall issue are closed analytically.

## 5. Independent no-mode region

The radial min--max argument gives

\[
 N_D(A_{\rho,1}^{(d)},K^2)=0
 \quad\text{if}\quad
 K^2\le
 \frac{\pi^2}{(1-\rho)^2}
 +\frac{(d-2)^2-1}{4}.
\]

The equality face belongs to the zero-count region because the counting
convention is strict.

## 6. Artifacts and next round

A separate working paper was created at
manuscript/spherical-shell-polya-general-d.tex; the original \(d=3\)
paper was not edited. The compiled PDF is
output/pdf/spherical-shell-polya-general-d.pdf.

Next round:

1. certify the finite scalar ball-wall list in the one-interface residual;
2. replace one-cell pairing by a shelf block with a quantitative terminal
   ball reserve;
3. prove (ST) for arbitrary-length inner tails and insert it into the
   already-complete all-\(d\) assembly.
