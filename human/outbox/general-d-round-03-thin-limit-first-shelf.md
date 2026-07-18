# General dimension, Round 3: the active thin-limit first-shelf scalar

Date: 18 July 2026

Status: proved limiting scalar; exact finite-thickness comparison proved;
uniform finite-thickness transfer remains open.

## 1. Active scaling and the scalar to be proved

Put

\[
 \varepsilon=1-\rho,\qquad
 a=\varepsilon K,\qquad
 y=\varepsilon z.
\]

The radial Dirichlet lower bound gives no spectrum below \(K^2\) when
\(K\leq\pi/\varepsilon\).  Thus a nonempty spectral problem has

\[
 a>\pi.
\]

This is the thin-variable version of the active-action condition
\(A_{\rho,K}(0)>1\).

The thin-shell action is

\[
 B_a(y)=\frac{\sqrt{a^2-y^2}}{\pi},
 \qquad 0\leq y\leq a.
\]

Fix an ordinary first-shelf level \(m\in\mathbb N\), and put

\[
 h=m-\frac14.
\]

Let \(y_p\) be the lower edge of that action shelf,

\[
 B_a(y_p)=h.
\]

For a possible shelf start \(y_0\in[0,y_p]\), the limiting scalar which
retains the first-shelf area and the terminal payment is

\[
 \boxed{
 \mathcal F_{a,m}(y_0)
 =2\int_{y_0}^{y_p}B_a(y)\,dy
 -2m(y_p-y_0)+\frac{a-y_p}{2}.}
 \tag{1}
\]

The first two terms are the scaled continuous-minus-discrete defect of a
constant floor shelf.  The last term is the limiting terminal reserve.
The relevant range is \(a\geq\pi h\); otherwise the level \(m\) cannot
occur.

Here is the exact mapping from the finite-thickness shelf reduction.  With

\[
 \mathcal A_{\varepsilon,a}(y)
 :=A_{1-\varepsilon,a/\varepsilon}(y/\varepsilon),
\]

\[
 y_0=\varepsilon r,\qquad
 y_p=\varepsilon(r+p),\qquad
 y_q=\varepsilon(r+n),
\]

and

\[
 d_\rho=\frac{2\arcsin\rho}{\pi},
\]

one has identically

\[
 \begin{aligned}
 \varepsilon\left(
 R_p(r)+\frac{d_\rho}{2}(n-p)
 \right)
 ={}&2\int_{y_0}^{y_p}\mathcal A_{\varepsilon,a}(y)\,dy
 -2m(y_p-y_0)\\
 &+\frac{d_\rho}{2}(y_q-y_p).
 \end{aligned}
 \tag{1a}
\]

Thus the complete sharp scalar satisfies

\[
 \varepsilon\mathfrak S
 =\varepsilon D_A(q)
 +2\int_{y_0}^{y_p}\mathcal A_{\varepsilon,a}
 -2m(y_p-y_0)
 +\frac{d_\rho}{2}(y_q-y_p).
 \tag{1b}
\]

At fixed optical data as \(\varepsilon\downarrow0\), one has
\(y_q\to a\), \(d_\rho\to1\), and
\(\mathcal A_{\varepsilon,a}\to B_a\).  Formula (1) is precisely the
limit of (1b) after the nonnegative terminal term
\(\varepsilon D_A(q)\) is discarded.  For a uniform finite-thickness
argument, however, that terminal term should be retained.

## 2. Uniform positivity theorem

### Theorem 2.1

For every \(a\geq\pi\), every \(m\in\mathbb N\) for which
\(a\geq\pi(m-1/4)\), and every \(y_0\in[0,y_p]\),

\[
 \boxed{\mathcal F_{a,m}(y_0)>0.}
 \tag{2}
\]

More quantitatively,

\[
 \boxed{
 \mathcal F_{a,m}(y_0)\geq
 \frac{\pi^2}{3072a}.}
 \tag{3}
\]

### Proof

Scale once more by

\[
 R=\frac a\pi,\qquad x=\frac y\pi,
 \qquad b_R(x)=\sqrt{R^2-x^2}.
\]

Then

\[
 x_p=\sqrt{R^2-h^2}
\]

and \(f=\mathcal F_{a,m}/\pi\) is

\[
 f(x_0)=2\int_{x_0}^{x_p}b_R(x)\,dx
 -2m(x_p-x_0)+\frac{R-x_p}{2}.
 \tag{4}
\]

Differentiation gives

\[
 f'(x_0)=2\bigl(m-b_R(x_0)\bigr).
 \tag{5}
\]

There are two cases.

#### Case 1: \(R\geq m\)

The unique minimum occurs at

\[
 x_m=\sqrt{R^2-m^2},
 \qquad b_R(x_m)=m.
\]

The function \(b_R\) is strictly concave.  Hence its integral over
\([x_m,x_p]\) is bounded below by the endpoint trapezoid.  Since the
endpoint values are \(m\) and \(m-1/4\),

\[
 2\int_{x_m}^{x_p}(b_R-m)\,dx
 \geq-\frac{x_p-x_m}{4}.
\]

Consequently

\[
 f(x_m)\geq\frac{2R+x_m-3x_p}{4}.
 \tag{6}
\]

To prove positivity, square the positive quantities.  With
\(C=9h^2-m^2\),

\[
 \begin{aligned}
 (2R+x_m)^2-9x_p^2
 &=C-4R(R-x_m)\\
 &\geq C-4m^2\\
 &=4m^2-\frac92m+\frac9{16}
 \geq\frac1{16}.
 \end{aligned}
 \tag{7}
\]

Here \(R(R-x_m)\leq m^2\) follows from
\((R-x_m)(R+x_m)=m^2\), and the last quadratic is increasing for
\(m\geq1\).  Therefore \(2R+x_m>3x_p\).  Moreover the conjugate
denominator is at most \(6R\), so (6)--(7) give

\[
 f(x_m)\geq\frac1{384R}.
 \tag{8}
\]

#### Case 2: \(h\leq R<m\)

Now \(b_R<m\) everywhere, so (5) shows that the minimum occurs at
\(x_0=0\).  Write

\[
 t=R-h\in\left[0,\frac14\right],
 \qquad x_p=\sqrt{t(2h+t)}.
\]

The endpoint trapezoid on \([0,x_p]\) gives

\[
 f(0)\geq\frac R2-(1-t)x_p.
 \tag{9}
\]

It remains to prove \(R\geq2(1-t)x_p\).  The difference of the squares is

\[
 P(h,t)=(h+t)^2-4(1-t)^2t(2h+t).
 \tag{10}
\]

For \(h\geq3/4\) and \(0\leq t\leq1/4\), this expression is increasing
in \(h\).  At \(h=3/4\), it is exactly

\[
 P\left(\frac34,t\right)
 =9\left(\frac14-t\right)^2+2t^3(1-2t)>0.
 \tag{11}
\]

This proves (9) is positive.  It also gives a quantitative bound.  If
\(t\leq1/8\), the first term in (11) is at least \(9/64\); if
\(t\geq1/8\), the second is at least \(1/512\).  Thus \(P\geq1/512\).
The conjugate denominator in (9) is at most \(3R/2\), and hence

\[
 f(0)\geq\frac1{3072R}.
 \tag{12}
\]

Equations (8) and (12), together with (5), prove (2)--(3).

## 3. There is no scale-free margin

The bound (3) has the correct qualitative scale: the limiting scalar has
no positive lower bound independent of \(a\).  For fixed \(m\), put again
\(h=m-1/4\).  Direct expansion of (4) at its minimizing point gives

\[
 \frac{\mathcal F_{a,m}^{\min}}{\pi}
 =\frac{C_m}{R}+O(R^{-3}),
 \qquad
 C_m=\frac{48m^2-36m+5}{192}>0.
 \tag{13}
\]

In particular, the reserve is only of order \(a^{-1}\) as
\(a\to\infty\).  Any finite-thickness transfer must therefore control its
error on the same scale; a fixed \(O(\varepsilon)\) error is not enough
uniformly in optical width.

## 4. Exact finite-thickness action and sharp comparisons

The finite-thickness action introduced above has an exact scaled form.
With the integrand understood as zero for \(s<y\),

\[
 \boxed{
 \mathcal A_{\varepsilon,a}(y)
 =\frac1{\pi\varepsilon}
 \int_{a(1-\varepsilon)}^a
 \sqrt{1-\frac{y^2}{s^2}}_+\,ds.}
 \tag{14}
\]

For \(0\leq y\leq a(1-\varepsilon)\), the function

\[
 s\longmapsto\sqrt{1-y^2/s^2}
\]

is increasing and strictly concave.  The endpoint trapezoid and Jensen's
inequality therefore give the exact two-sided comparison

\[
 \boxed{
 \frac a{2\pi}
 \left(
 \sqrt{1-\frac{y^2}{a^2(1-\varepsilon)^2}}
 +\sqrt{1-\frac{y^2}{a^2}}
 \right)
 \leq\mathcal A_{\varepsilon,a}(y)
 \leq
 \frac a\pi
 \sqrt{1-\frac{y^2}{a^2(1-\varepsilon/2)^2}}.}
 \tag{15}
\]

Equivalently, the lower bound is the average of two explicit product
profiles,

\[
 \mathcal A_{\varepsilon,a}(y)
 \geq
 \frac12B_a(y)
 +\frac1{2(1-\varepsilon)}B_{a(1-\varepsilon)}(y).
 \tag{16}
\]

On the outer strip \(a(1-\varepsilon)\leq y\leq a\), (14) instead gives

\[
 \mathcal A_{\varepsilon,a}(y)
 =\frac1\varepsilon G_a(y)
 \geq
 \frac{a-y}{2a\varepsilon}B_a(y).
 \tag{17}
\]

These are exact finite-\(\varepsilon\) lower comparisons.  They retain the
radius curvature which is lost by replacing the shell with a flat product.

## 5. Why a naive perturbation of the limiting proof is not uniform

Away from the moving turning edge, Taylor expansion of (14) gives

\[
 \mathcal A_{\varepsilon,a}(y)
 =B_a(y)
 -\frac{a\varepsilon}{2\pi}
 \frac{(y/a)^2}{\sqrt{1-(y/a)^2}}
 +O\left(
 \frac{a\varepsilon^2}{(1-(y/a)^2)^{3/2}}
 \right).
 \tag{18}
\]

At a fixed action level \(B_a(y)=h\), the first correction has size
\(\asymp\varepsilon a^2/h\), whereas the reserve (13) has size
\(\asymp a^{-1}\).  For fixed \(m\), a direct perturbative transfer can
therefore cover at most a regime of the form

\[
 \varepsilon a^3\ll1.
 \tag{19}
\]

This is not a uniform thin-endpoint argument.

The obstruction is real, not an artifact of (18).  At the inner interface,

\[
 \frac{\mathcal A_{\varepsilon,a}(a(1-\varepsilon))}
 {B_a(a(1-\varepsilon))}
 \longrightarrow\frac23
 \qquad(\varepsilon\downarrow0).
 \tag{20}
\]

More generally, at \(y=a(1-\tau\varepsilon)\), with fixed
\(0<\tau\leq1\), this ratio tends to \(2\tau/3\).  Thus there is no
uniform comparison
\(\mathcal A_{\varepsilon,a}\geq(1-o(1))B_a\) across the entire moving
outer strip.

The transition begins when the thin-model distance of the shelf wall from
the turning point,

\[
 a-y_p\sim\frac{\pi^2h^2}{2a},
\]

is comparable with the outer-strip width \(a\varepsilon\), namely when

\[
 \varepsilon a^2\asymp h^2.
 \tag{21}
\]

Accordingly, the next finite-thickness theorem must retain (14) in the
outer transition region.  A single regular next-order correction to
\(B_a\) cannot be uniform.  The exact comparison (15)--(17) is the right
starting point for an inner/outer matched shelf scalar: use (15) on the
concave inner part, (17) or the exact \(G_a/\varepsilon\) profile on the
outer part, and keep the strict wall at which the finite action equals
\(m-1/4\).

## 6. Separate finite-thickness certificate found in this round

For later use, let \(r<\mu\),

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,
\]

and suppose the first ordinary floor level is \(m=1\).  Let \(p\) be the
last index on that first shelf, put

\[
 a_0=A(r),\qquad a_p=A(r+p),\qquad a_q=A(q),
\]

and

\[
 c_\rho=\frac{\arccos\rho}{\pi},
 \qquad
 \kappa=\frac{1-\rho}{\pi\rho K}.
\]

Concavity on the inner branch and the global \(c_\rho\)-Lipschitz bound
give the rigorous area certificate

\[
 \begin{aligned}
 2\int_r^K A
 \geq{}&p(a_0+a_p)+\frac{\kappa p^3}{6}\\
 &+(n-p)(a_p+a_q)+\frac{\kappa(n-p)^3}{6}
 +\frac{a_q^2}{c_\rho}.
 \end{aligned}
 \tag{22}
\]

If all strict samples after \(r+p\) vanish, the strict count is at most
\(1+2p\), so the right side of (22) being at least \(1+2p\) proves that
tail.  This vanishing is automatic when the ordinary first shelf drops
before the interface (\(p<n\)); it also covers terminal one-cell chambers
with \(p=n\) and \(A(q+1)\leq3/4\).  Without this extra hypothesis the
one-interface tail beginning at \(q\) must be retained rather than replaced
by the triangle \(a_q^2/c_\rho\).

The curvature terms are essential even in this scoped certificate.  The
same formula without them is false in the active region: take

\[
 r=\frac12,\quad n=p=4,\quad A(0)=1.0001,
\]

and \(\rho\) just to the right of the unique value
\(\rho_*\approx0.6346531466\) for which \(A(9/2)=3/4\).  For example,
at \(\rho=\rho_*+10^{-6}\), one has \(A(9/2)>3/4\),
\(A(11/2)<3/4\), and the curvature-free right side minus the strict
count \(9\) is about \(-0.00948\).  This is not a shifted-tail
counterexample--the true area has ample reserve--but it rules out that
tempting shortened certificate.

The finite-thickness global proof is therefore narrowed to proving a
curvature-retaining scalar such as (22), or its exact analogue, through
the transition regime (21).
