# General dimension \(d\ge3\): round 03

Date: 18 July 2026  
Primary strategy: human/inbox/general-d_1.md  
Status: the arbitrary multi-cell tail is reduced to one exact scalar; a new
thin high-energy sector is proved; the final terminal-shelf inequality is
still open.

## 1. Exact first-shelf reduction

For an inner tail, put

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad
 d_\rho=\frac{2\arcsin\rho}{\pi}.
\]

Let

\[
 F_j=\left\lfloor A(r+j)+\frac14\right\rfloor
 \quad(0\le j\le n),
\]

and let \(p\) be the last index on the first ordinary-floor shelf, with
\(p=n\) if no drop occurs.  Define

\[
 R_p=2\int_r^{r+p}A(z)\,dz-2pF_0.
\]

The following wall-safe reduction is now proved:

\[
 \boxed{
 D_A(r)\ge D_A(q)+R_p+\frac{d_\rho}{2}(n-p).}
\]

It is valid at ordinary and strict walls because the ordinary floors occur
only on the majorizing side.  The shelf reserve has the exact form

\[
 R_p=\mathcal C_p+
 p\left(\varepsilon_0+\varepsilon_p-\frac12\right),
\]

\[
 \mathcal C_p
 =-\int_0^p u(p-u)A''(r+u)\,du\ge0,
\]

and the stronger lower bound

\[
 R_p\ge-\frac p2+2\int_0^p u\,[-A'(r+u)]\,du.
\]

The same-floor condition gives the sharpened shelf cap

\[
 p<\sqrt{r^2+\frac{2\pi\rho}{1-\rho}K}-r.
\]

Since \(D_A(q)\ge0\) by the completed one-interface theorem, every tail
with

\[
 d_\rho(n-p)\ge p
\]

is automatic.  The many-cell problem is therefore compressed to the one
scalar

\[
 \boxed{
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\ge0.}
\]

This scalar retains the positive terminal reserve that the false
one-bad-cell/one-drop pairing discarded.

## 2. The spectral active region

The dimension-dependent no-mode estimate implies, uniformly for every
\(d\ge3\),

\[
 K\le\frac{\pi}{1-\rho}
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1}^{(d)},K^2)=0.
\]

Thus the general-dimensional Pólya theorem only needs the terminal-shelf
scalar in

\[
 K>\frac{\pi}{1-\rho}.
\]

The stronger standalone shifted-tail conjecture below this wall remains
interesting, but is no longer on the spectral critical path.

## 3. New thin high-energy theorem

Let

\[
 \rho=1-\varepsilon,\qquad 0<\varepsilon\le\frac1{100}.
\]

The optimized local-plateau proof, which is an individual shifted-tail
argument before multiplicities are summed, is parity-neutral.  It proves

\[
 \boxed{
 K\ge\frac{125}{8\varepsilon^2}
 \quad\Longrightarrow\quad
 D_A(r)\ge0\quad
 \text{for every }r\in\tfrac12\mathbb N.}
\]

This improves the thin asymptotic threshold from order
\(\varepsilon^{-4}\) to order \(\varepsilon^{-2}\).  Its decisive loss
bound is

\[
 p-d_\rho(n-p)<\frac{361}{80\sqrt\varepsilon},
\]

and the exact final payment is

\[
 \frac{2829397}{3732696}
 -\frac{132}{175}
 =\frac{2428603}{653221800}>0.
\]

The dependency-free replay

computations/round9_verify_thin_plateau_constants.py

passes every rational comparison.

## 4. Active thin-product limit

With

\[
 a=(1-\rho)K,\qquad y=(1-\rho)z,
\]

the active region is \(a>\pi\), and the shell action converges to

\[
 B_a(y)=\frac{\sqrt{a^2-y^2}}{\pi}.
\]

For a first shelf of level \(m\ge1\), put
\(b=m-1/4\), \(B_a(y_b)=b\), and define

\[
 \mathcal L_{a,m}(y_0)
 =2\int_{y_0}^{y_b}B_a(y)\,dy
 -2m(y_b-y_0)+\frac{a-y_b}{2}.
\]

The complete two-case proof gives

\[
 \boxed{
 \mathcal L_{a,m}(y_0)>0,\qquad
 \mathcal L_{a,m}(y_0)\ge\frac{\pi^2}{3072a}.}
\]

For each finite optical cap \(A_*>\pi\), compactness and exact convergence
therefore prove the existence of \(\varepsilon_*(A_*)>0\) such that every
shifted tail with

\[
 \pi\le a\le A_*,\qquad
 0<\varepsilon<\varepsilon_*(A_*)
\]

is positive.  The margin behaves like \(C_m/a\) as \(a\to\infty\), so a
uniform finite-thickness transfer still needs a retained next-order or
terminal-reserve estimate.

## 5. Exact first-floor wall certificate

In the valid \(F_0=1,\ p<n\) branch, a strengthened chord-plus-terminal
certificate is strictly increasing in \(K\) at fixed \(\mu\).  Its chamber
minimum is therefore the right-hand limit at

\[
 A(r+p)=\frac34.
\]

The standalone 384-bit Arb verifier

scripts/general_d_first_shelf_wall_verify.py

certifies ten identified residual chambers.  It proves positivity on
2,560 directed-rounding boxes; a 768-bit, 5,120-box stress run also
passes.  The smallest rigorous lower endpoint is approximately
\(0.46779\).

This certificate has deliberately limited scope.  It proves those ten wall
families, but it does **not** prove that every remaining
\(F_0=1,\ p<n\) configuration belongs to them.  It also does not treat the
no-drop branch \(p=n\) or \(F_0\ge2\).

## 6. Exact remaining work

The full general-dimensional theorem still requires one of the following:

1. prove the terminal-shelf scalar uniformly in the active region; or
2. prove an exhaustive reduction to finitely many residual chambers,
   then certify them while treating \(p=n\) and \(F_0\ge2\) separately.

The principal proof notes are:

- human/outbox/general-d-round-02-shelf-reduction.md;
- human/outbox/general-d-round-02-terminal-reserve.md;
- human/outbox/general-d-inverse-double-sawtooth-round2.md;
- human/outbox/general-d-round-03-thin-product-shelf.md;
- human/outbox/general-d-round-03-thin-limit-first-shelf.md.

The separate manuscript is

manuscript/spherical-shell-polya-general-d.tex.

The Round 3 build is a clean 19-page PDF under

manuscript/build-general-d-round3/spherical-shell-polya-general-d.pdf.
The original \(d=3\) paper remains untouched.

