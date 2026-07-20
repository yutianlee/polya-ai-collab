# General dimension, Round 39: outer-face floor elimination and cap sharpening

Date: 20 July 2026

Status: mixed. This note proves a sharper cap estimate, an exact intrinsic
outer-\(B\) selected-scalar reduction, a floor-elimination lemma on the
simultaneous outer-\(B\)/lower-shelf face, and a phase--stretch inequality
which closes that complete transported endpoint. The outer-\(B\),
\(\alpha\uparrow1^-\) endpoint is not signed here. The remaining one-level
gap faces, the equal-count classes, pointwise CST, the frozen audit of the
general-dimensional branching backbone, and the all-dimensional Pólya
theorem all remain open. No status in state/proof_obligations.yml is
changed by this note.

## 0. Theorem boundary, dependencies, and notation

The authoritative obligation graph is state/proof_obligations.yml, whose
expected SHA-256 is

    a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4.

The selected obligation remains
SHELL-general-d-high-floor-first-drop-CST. The exact branching backbone
remains derived_under_assumptions; this note neither audits nor promotes
it. The methodology is fixed by
human/inbox/general-d_simplified_analytic_strategy.md and
human/inbox/general-d-strategy_r2.md.

Only the following earlier results are used.

1. Round 21 supplies radius monotonicity of the cap and monotonic decrease
   of \(I_{q+1}(q)\) in \(q\).
2. Round 23 supplies the exact closed cap formula.
3. Round 28 supplies \(\Delta\geq M_4\), the elasticity member of \(M_4\),
   the quartic member \(\mathcal K_4\), and the implication from the
   selected scalar to the shifted defect.
4. Rounds 34--35 supply the common-radial-parameter adjacent-action bound.
5. Rounds 36--37 supply the hard one-level gap, the terminal inverse-level
   decomposition, and the selected projected scalar.
6. Round 38 supplies the sharp gap coordinates, \(B_0\zeta>1/5\), the
   exact \(\widehat\Xi\) refinement, the elasticity estimate, and the
   root-free old-level reserve.

Throughout,

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
 \qquad b_a(z)=\frac1\pi\arccos\frac za,
\]

\[
 A(z)=G_K(z)-G_\mu(z),\qquad x=r+p,\qquad
 q=x+m,\qquad \mu=q+\alpha,
\]

where \(r\geq1\) on the integer grid and \(r\geq3/2\) on the
half-integer grid, \(p,m\geq1\), and \(0<\alpha<1\). Put

\[
 K=\mu\sec t,\qquad 0<t<\frac\pi2,\qquad
 d=1-\frac{2t}{\pi},\qquad
 \zeta=\frac{d}{1-d}=\frac\pi{2t}-1,
\]

\[
 W=G_K(\mu)=\frac\mu\pi(\tan t-t),\qquad
 h=G_\mu(q),\qquad v=G_K(q),
\]

and

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 g=\frac{U_r}{U_x}-1,
\]

\[
 R_1=\frac{U_r-U_x}{U_x-U_q},\qquad
 a_p=\frac{p^2}{3(2r+p)},\qquad
 \beta=b_K(q).
\]

Here \(d\) is the phase deficit, not the ambient dimension; expressions
such as \(dm\) mean \(d\,m\). On the hard residual one has \(p>dm\).
The one-level gap has

\[
 B=Q+1,\qquad B_0=Q=B-1\geq1,
\]

and the Round 38 coordinates

\[
 j=f-B,\qquad \lambda=j+u,
 \qquad 0<u<\frac\alpha2,
\]

\[
 A(x)-A(q)=j+e_p+\chi.
\]

At the gap-side outer-\(B\) closure,

\[
 v=B-\frac14,\qquad \chi=h,\qquad y_B=0,
 \qquad \theta_B=\pi\beta,
\tag{0.1}
\]

where \(B\) is a one-sided gap label: the literal strict bracket at the
wall is \(B-1\).

No ratio subdivision, \(B\)- or \(j\)-indexed theorem family, new chamber,
or compact certificate is introduced below.

## 1. The residual cap is below \(1/10\)

### Lemma 1.1 (cap sharpening)

Every residual one-level gap with \(p\geq3\) satisfies

\[
 \boxed{q\geq5,\qquad J<\frac1{10}.}
\tag{R39.1}
\]

#### Proof

Since \(r,m\geq1\) and \(p\geq3\), \(q=r+p+m\geq5\); the
half-integer grid has the stronger \(q\geq11/2\). With
\(I_a(s)=\int_s^aG_a(z)\,dz\), radius monotonicity, \(\mu<q+1\), and
the Round 21 monotonicity in \(q\) give

\[
 J=2I_\mu(q)<2I_{q+1}(q)\leq2I_6(5).
\tag{1.1}
\]

For completeness, that monotonicity follows from

\[
 I_{q+1}(q)=\frac1\pi
 \int_{0\leq u\leq w\leq1}
 \sqrt{1-\left(\frac{q+u}{q+w}\right)^2}\,dw\,du,
\]

whose integrand decreases pointwise with \(q\). The exact endpoint is

\[
 2I_6(5)=
 \frac{86\arccos(5/6)-15\sqrt{11}}{2\pi}.
\tag{1.2}
\]

Now \(\arccos(5/6)=2\arctan(1/\sqrt{11})\). The alternating-series
bound

\[
 \arctan z<z-\frac{z^3}{3}+\frac{z^5}{5}
 \qquad(0<z<1)
\]

therefore gives

\[
 86\arccos(5/6)-15\sqrt{11}
 <\frac{3761}{1815\sqrt{11}}.
\tag{1.3}
\]

Since \(\sqrt{11}>33/10\) and \(\pi>333/106\),

\[
 \frac{3761}{1815\sqrt{11}}
 <\frac{7522}{11979}
 <\frac{333}{530}<\frac\pi5.
\]

The only non-immediate rational comparison is

\[
 \frac{333}{530}-\frac{7522}{11979}
 =\frac{2347}{6348870}>0.
\]

Substitution in (1.2) proves (R39.1). Every inequality is strict.
\(\square\)

### Corollary 1.2 (improved automatic threshold)

The Round 38 exact selected normal form and its nonnegative terms give

\[
 \Gamma_{\rm gap}
 >1-\frac1{10}+\frac15-\frac{p-dm}{2}
 =\frac{11}{10}-\frac{p-dm}{2}.
\tag{R39.2}
\]

Consequently every one-level gap with

\[
 \boxed{p-dm\leq\frac{11}{5}}
\tag{R39.3}
\]

is closed by the inherited implication chain. In particular, the only
possibly remaining \(p=3\) records satisfy

\[
 \boxed{dm<\frac45.}
\tag{R39.4}
\]

This strictly improves the Round 38 threshold \(74/35\). It does not by
itself close every \(p\geq3\) gap.

## 2. Exact intrinsic reduction on the outer-\(B\) face

Let

\[
 \Omega_-=
 \sum_{k=1}^{B_0}
 \left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right).
\]

On the outer-\(B\) face, (0.1) gives

\[
 \omega_B=\frac1{2\beta}-1,
 \qquad B_0=v-\frac34.
\tag{2.1}
\]

### Theorem 2.1 (exact outer-\(B\) selected scalar)

The selected projected scalar has the exact face identity

\[
 \boxed{
 \begin{aligned}
 \Gamma_{\rm OB}={}&
 \frac1{2\beta}-J+\Omega_-+
 \left(G_K(q)-\frac34\right)\zeta\\
 &+p\Delta+a_pM_4+2pe_p-\frac{p-dm}{2}.
 \end{aligned}}
\tag{R39.5}
\]

The exact action coordinates are

\[
 \boxed{A(x)-A(q)=j+e_p+h,}
\tag{R39.6}
\]

\[
 \boxed{A(x)-W=j+u+e_p=\lambda+e_p.}
\tag{R39.7}
\]

Consequently the single intrinsic continuous lower bound

\[
 \boxed{
 \begin{aligned}
 \Gamma_{\rm OB}>F_{\rm OB}:={}&
 \frac1{2\beta}-J+\Omega_-+
 \left(G_K(q)-\frac34\right)\zeta\\
 &+pR_1\{A(x)-A(q)\}
 +a_pg\{A(x)-W\}+2pe_p-\frac{p-dm}{2}
 \end{aligned}}
\tag{R39.8}
\]

holds on every finite gap-side outer-\(B\) face.

#### Proof

Round 38 gives

\[
 \Gamma_{\rm gap}
 =1-J+B_0\zeta+\Omega
 +(p+a_p)M_4+2pe_p+p\widehat\Xi-\frac{p-dm}{2},
\]

where \(\widehat\Xi=\Delta-M_4\). Substitute
\(\Omega=\Omega_-+1/(2\beta)-1\), (2.1), and

\[
 (p+a_p)M_4+p(\Delta-M_4)=p\Delta+a_pM_4.
\]

This proves (R39.5). Equations (R39.6)--(R39.7) follow directly from
\(\chi=h\), \(A(x)=f-1/4+e_p\),
\(A(q)=v-h\), \(v=B-1/4\), and \(f=B+j\).

The Round 34 adjacent-action estimate and the Round 38 elasticity estimate
are

\[
 \Delta>R_1\{A(x)-A(q)\},
 \qquad M_4\geq g\{A(x)-W\}.
\tag{2.2}
\]

Substitution proves (R39.8). More precisely, the exact loss is

\[
 \boxed{
 \begin{aligned}
 \Gamma_{\rm OB}-F_{\rm OB}
 ={}&p\bigl[\Delta-R_1\{A(x)-A(q)\}\bigr]\\
 &+a_p\bigl[M_4-g\{A(x)-W\}\bigr]>0.
 \end{aligned}}
\tag{R39.9}
\]

The first bracket is strictly positive and the second is nonnegative.
\(\square\)

This is one face inequality, not a theorem family indexed by \(B\), \(j\),
or a shell-ratio interval.

### Corollary 2.2 (root-free old-level projection)

Round 38 gives

\[
 \Omega_-\geq
 \frac{\pi^2}{2Kt^3\sin t}
 \left\{\frac{B_0(B_0+1)}2-B_0u\right\}.
\]

Using \(B_0=v-3/4\) and \(u=v-W\), define

\[
 \boxed{
 \Omega_{\rm RF}:=
 \frac{\pi^2}{2Kt^3\sin t}
 \left(v-\frac34\right)
 \left(W-\frac v2+\frac18\right).}
\tag{R39.10}
\]

Equivalently,

\[
 \boxed{
 \Omega_{\rm RF}=
 \frac{\pi(\tan t-t)}{2Wt^3\tan t}
 \left(v-\frac34\right)
 \left(W-\frac v2+\frac18\right),}
\tag{R39.11}
\]

because \(K\sin t=\mu\tan t\) and
\(\mu=\pi W/(\tan t-t)\). Let \(F_{\rm OB}^{\rm RF}\) be
(R39.8) with \(\Omega_-\) replaced by \(\Omega_{\rm RF}\). Then

\[
 \boxed{
 \Gamma_{\rm OB}>F_{\rm OB}\geq F_{\rm OB}^{\rm RF},
 \qquad
 F_{\rm OB}-F_{\rm OB}^{\rm RF}
 =\Omega_--\Omega_{\rm RF}\geq0.}
\tag{R39.12}
\]

The root-free form is an optional projection of the same face inequality;
it is not a new certificate or global scalar.

### Corollary 2.3 (exact elasticity remainder and the limit of
\(\widehat\Xi\))

Put

\[
 R_{\rm el}=\Delta-g(\lambda+e_p)\geq0,
 \qquad \tau=\frac g{g+2}.
\]

Since \(E=\Delta+2e_p\),

\[
 \boxed{
 \tau(E+2\lambda)
 =g(\lambda+e_p)+\tau R_{\rm el}.}
\tag{R39.13}
\]

As \(M_4=\max\{\tau(E+2\lambda),\mathcal K_4\}\), one has the exact
branch identity

\[
 \boxed{
 \widehat\Xi
 =\min\bigl\{(1-\tau)R_{\rm el},
                 \Delta-\mathcal K_4\bigr\}.}
\tag{R39.14}
\]

Thus no uniform strictly positive lower bound for
\(\widehat\Xi\) follows from the inherited inequalities: either displayed
branch can approach zero. The quantity must be retained exactly or
discarded only as nonnegative.

## 3. Eliminating the floor \(j\) on the lower-shelf face

Define

\[
 H_{\rm ls}(q):=G_{q+1}(q-1).
\]

### Lemma 3.1 (two-step comparison action)

For every \(q\geq5\),

\[
 \boxed{
 \frac q\pi\left\{\tan\bigl(\pi H_{\rm ls}(q)\bigr)
       -\pi H_{\rm ls}(q)\right\}<\frac74.}
\tag{R39.15}
\]

#### Proof

Set \(w=(q+1)^{-1/2}\leq1/\sqrt6\). The change of variables
\(z=q+1-2y\) gives

\[
 \pi H_{\rm ls}(q)
 =4\int_0^1\arcsin(w\sqrt y)\,dy.
\tag{3.1}
\]

For \(0\leq z\leq w<1\), the positive arcsine series gives

\[
 \arcsin z<z+\frac{z^3}{6}+\frac{3z^5}{40}
 +\frac{5z^7}{112}+\frac{z^9}{9(1-w^2)}.
\tag{3.2}
\]

Indeed, the coefficient of \(z^{2n+1}\) is
\(\binom{2n}{n}/\{4^n(2n+1)\}\); for \(n\geq4\) it is at most
\(1/(2n+1)\leq1/9\), while
\(z^{2n+1}\leq z^9w^{2n-8}\). Integrating (3.2) in
(3.1) yields

\[
 \pi H_{\rm ls}(q)<Z(w):=wC(w),
\tag{3.3}
\]

where

\[
 C(w)=\frac83+\frac4{15}w^2+\frac3{35}w^4
 +\frac5{126}w^6+\frac{8w^8}{99(1-w^2)}.
\]

The function \(C\) is increasing, and

\[
 C(w)\leq C_0:=C(1/\sqrt6)=\frac{451351}{166320}.
\tag{3.4}
\]

In particular \(Z(w)<\pi/2\). The Becker--Stark bound

\[
 \tan z<\frac{\pi^2z}{\pi^2-4z^2}
 \qquad(0<z<\pi/2)
\tag{3.5}
\]

follows, for example, from the partial fractions

\[
 \frac{\tan z}{z}
 =\sum_{n\geq1}\frac8{(2n-1)^2\pi^2-4z^2}
\]

by comparing every denominator with the first one and using the value at
\(z=0\). Explicitly, with \(a_n=(2n-1)^2\pi^2\) and \(y=4z^2\),
\[
 \frac1{a_n-y}\leq\frac{a_1}{a_n(a_1-y)},
\]
and summation proves (3.5). Also,
\(C_0<11/4\), \(\sqrt6>12/5\), and \(\pi>3\), so
\(Z(w)<55/48<3/2<\pi/2\), as asserted. Equations (3.3)--(3.5), and
\(q=(1-w^2)/w^2\), give

\[
 \frac q\pi\{\tan(\pi H_{\rm ls})-\pi H_{\rm ls}\}
 <\frac{4w(1-w^2)C(w)^3}
 {\pi\{\pi^2-4w^2C(w)^2\}}.
\tag{3.6}
\]

On \(0<w\leq1/\sqrt6\), \(w(1-w^2)\) and \(C(w)\) increase, while the
positive denominator in braces decreases. Thus the right side is at
most its endpoint bound. Using

\[
 \pi>\frac{333}{106},\qquad
 \sqrt6>\frac{2449}{1000},
\]

one obtains the exact rational estimate

\[
 \begin{aligned}
 \frac{20C_0^3}
 {(2449/1000)^3(333/106)
  \{(333/106)^2-2C_0^2/3\}}
 &={3422243005154215230806750000000\over
    1959338986699645823262372838071}\\
 &<\frac{1747}{1000}<\frac74.
 \end{aligned}
\tag{3.7}
\]

The substituted denominator is positive because
\[
 \left(\frac{333}{106}\right)^2-\frac{2C_0^2}{3}
 =\frac{578050467307991}{116555279702400}>0.
\]
The first difference in the last line has numerator
\(722204610066022432615348110037>0\) after multiplication by the
positive common denominator; the last difference is \(3/1000\).
This proves (R39.15). \(\square\)

### Theorem 3.2 (lower shelf forces \(j\geq1\))

At every simultaneous gap-side outer-\(B\)/lower-shelf endpoint,

\[
 \boxed{j=A(x)-v\geq1.}
\tag{R39.16}
\]

#### Proof

The lower-shelf equality \(e_p=0\) and outer-\(B\) equality (0.1) give

\[
 A(x)=f-\frac14,\qquad v=B-\frac14,\qquad
 A(x)-v=f-B=j.
\tag{3.8}
\]

First, \(K>q+1\). Otherwise radius monotonicity would give

\[
 v=G_K(q)\leq G_{q+1}(q)<\frac12,
\]

where the last inequality follows from
\(G_{q+1}(q)=\int_q^{q+1}b_{q+1}(z)\,dz<1/2\). This is contrary to
\(v=B-1/4\geq7/4\). Since \(m\geq1\), \(x\leq q-1\).
For

\[
 D(z)=G_K(z)-G_K(q)-G_{q+1}(z),
\]

one has

\[
 D'(z)=b_{q+1}(z)-b_K(z)<0.
\]

Radius monotonicity of the subtracted inner action and then this
monotonicity give

\[
 \begin{aligned}
 A(x)-v
 &\geq G_K(x)-G_K(q)-G_{q+1}(x)\\
 &\geq G_K(q-1)-G_K(q)-G_{q+1}(q-1)\\
 &>\beta-H_{\rm ls}(q).
 \end{aligned}
\tag{3.9}
\]

The last inequality uses
\(G_K(q-1)-G_K(q)=\int_{q-1}^q b_K(z)\,dz>\beta\).
On the outer wall,

\[
 v=G_K(q)=\frac q\pi\{\tan(\pi\beta)-\pi\beta\}
 \geq\frac74.
\tag{3.10}
\]

The function \(s\mapsto\tan(\pi s)-\pi s\) is strictly increasing on
\((0,1/2)\). Lemma 3.1 and (3.10) therefore imply
\(\beta>H_{\rm ls}(q)\). Hence (3.9) is positive. By (3.8), \(j\) is
a positive integer, so \(j\geq1\). \(\square\)

This proof does not assert the stronger diagnostic pattern \(B_0\geq2\).

## 4. The phase--stretch inequality

For this section put

\[
 z=\frac{m+\alpha}{p}>0,
 \qquad
 \gamma(z)=\frac{1+z}{\sqrt{z(z+2)}}-1,
\]

\[
 C(d,z)=\frac{1-dz}{2}-\gamma(z),
\tag{4.1}
\]

and

\[
 \mathcal H(d)=
 \left\{\left(\frac{3+d}{2}\right)^{2/3}-1\right\}^{3/2}
 -\frac d2,
\]

\[
 k(d)=\frac89(1-d^4),\qquad
 L(d)=\frac{\zeta}{\pi}(\tan t-t),\qquad
 t=\frac\pi2(1-d).
\tag{4.2}
\]

Recall that \(d\) in this section is the phase deficit
\(1-2t/\pi\), not the ambient dimension.

### Lemma 4.1 (exact stretch and phase payment)

For \(0<d<1\) and \(z>0\),

\[
 \boxed{g>\gamma(z),}
\tag{R39.17}
\]

\[
 \boxed{
 \frac{C(d,z)}{1+z}\leq\mathcal H(d)<k(d)L(d).}
\tag{R39.18}
\]

#### Proof: exact stretch

Let \(h_r=2r/p>0\). Direct normalization gives

\[
 (g+1)^2
 =1+\frac{h_r+1}{z(z+h_r+2)}.
\]

Since

\[
 \frac{h_r+1}{z+h_r+2}>\frac1{z+2},
\]

one gets

\[
 g+1>
 \sqrt{1+\frac1{z(z+2)}}
 =\frac{1+z}{\sqrt{z(z+2)}}.
\]

This proves (R39.17), with strictness supplied by \(r>0\).

#### Proof: exact maximization in \(z\)

Write \(y=1+z>1\). Then

\[
 \frac{C(d,z)}{1+z}
 =\frac{3+d}{2y}-\frac d2-\frac1{\sqrt{y^2-1}}.
\tag{4.3}
\]

The derivative has exactly one zero. If

\[
 \ell=\left(\frac{3+d}{2}\right)^{2/3},
\]

that zero satisfies \(y^2=\ell/(\ell-1)\). The expression in (4.3)
tends to \(-\infty\) as \(y\downarrow1\), its derivative is negative for
large \(y\), and evaluation at the unique critical point gives

\[
 \max_{y>1}\left\{
 \frac{3+d}{2y}-\frac d2-\frac1{\sqrt{y^2-1}}
 \right\}
 =(\ell-1)^{3/2}-\frac d2=\mathcal H(d).
\tag{4.4}
\]

This proves the first inequality in (R39.18).

#### Proof: a refined tangent majorant

For \(0<x<\pi/2\), logarithmic differentiation of the cosine product
gives the positive partial fractions

\[
 \frac{\tan x}{x}
 =\sum_{q\geq1,\ q\ {\rm odd}}
 \frac8{q^2\pi^2-4x^2}.
\tag{4.5}
\]

If

\[
 \frac{\tan x}{x}=\sum_{n\geq0}a_nx^{2n},
\]

then

\[
 a_n=\frac{8\,4^n}{\pi^{2n+2}}S_{2n+2},
 \qquad
 S_s=\sum_{q\geq1,\ q\ {\rm odd}}q^{-s}.
\]

Here \(a_0=1\), \(a_1=1/3\). For \(n\geq2\),
\(S_{2n+2}\leq S_6=\pi^6/960\), so

\[
 a_n\leq\frac{4^n}{120\pi^{2n-4}}
 <\frac{4^{n-1}}{3\pi^{2n-2}},
\]

where the strict comparison is exactly \(\pi^2<10\). Comparing positive
power-series coefficients proves

\[
 \boxed{
 \frac{\tan x}{x}<
 \frac{\pi^2+(\pi^2/3-4)x^2}{\pi^2-4x^2}.}
\tag{4.6}
\]

Set \(x=\pi d/2\), so \(t=\pi/2-x\). Inverting (4.6) and simplifying
gives

\[
 L(d)>A_\pi(d)-\frac d2,
\tag{4.7}
\]

where

\[
 A_\pi(d)=
 \frac{2(1+d)}{\pi^2\{1+(\pi^2/12-1)d^2\}}.
\]

For fixed \(d\in(0,1)\), the function

\[
 D(s)=s(1-d^2)+\frac{s^2d^2}{12}
\]

is strictly increasing. Since \(\pi<22/7\), (4.7) implies

\[
 A_\pi(d)>A_0(d):=
 \frac{2(1+d)}{
 (484/49)(1-d^2)+(484/49)^2d^2/12}.
\tag{4.8}
\]

It remains to prove

\[
 k(d)A_0(d)+\frac{1-k(d)}2d
 >R(d):=
 \left\{\left(\frac{3+d}{2}\right)^{2/3}-1\right\}^{3/2}.
\tag{4.9}
\]

Indeed, (4.7)--(4.9) give
\(kL>R-d/2=\mathcal H\).

#### Proof: rational majorant and exact Sturm check

Put \(s=(3+d)/2\). Direct differentiation gives

\[
 R''(d)=\frac1{12s^{4/3}\sqrt{s^{2/3}-1}},
\tag{4.10}
\]

which decreases on \(0\leq d\leq1\). Let
\(\varpi=(3/2)^{2/3}\). Cubing proves the hand-checkable bounds

\[
 \frac{131}{100}<\varpi<\frac{819}{625},
\]

because

\[
 \frac94-\left(\frac{131}{100}\right)^3
 =\frac{1909}{1000000}>0,
\]

\[
 \left(\frac{819}{625}\right)^3-\frac94
 =\frac{147411}{976562500}>0.
\]

These bounds give, by squaring only positive quantities,

\[
 R(0)<\frac{173}{1000},\qquad
 R'(0)<\frac{61}{250},\qquad
 R''(0)<\frac{11}{125}.
\tag{4.11}
\]

Indeed,
\[
 R(0)=(\varpi-1)^{3/2},\qquad
 R'(0)=\frac12\sqrt{\frac{\varpi-1}{\varpi}},\qquad
 R''(0)=\frac1{12\varpi^2\sqrt{\varpi-1}},
\]
so each assertion in (4.11) reduces to the rational comparisons printed
next.

For auditability, the three rational margins used here are

\[
 \left(\frac{173}{1000}\right)^2-
 \left(\frac{194}{625}\right)^3
 =\frac{352049}{15625000000}>0,
\]

\[
 \left(\frac{61}{250}\right)^2-\frac{97}{1638}
 =\frac{16249}{51187500}>0,
\]

and, using \(\sqrt{31}>167/30\),

\[
 12\left(\frac{131}{100}\right)^2\frac{167}{300}
 -\frac{125}{11}
 =\frac{274757}{2750000}>0.
\]

Here \(31-(167/30)^2=11/900>0\). Since \(R''\) decreases, Taylor's
formula with integral remainder and (4.11) give

\[
 R(d)<U(d):=
 \frac{173}{1000}+\frac{61}{250}d+\frac{11}{250}d^2.
\tag{4.12}
\]

Combining the rational denominators in the left side of (4.9) minus
\(U(d)\) gives the exact identity

\[
 kA_0+\frac{1-k}{2}d-U
 =\frac{N(d)}{1089000(-147+26d^2)},
\tag{4.13}
\]

where

\[
 \begin{aligned}
 N(d)={}&-1117641+1354752d+2145330d^2-5335616d^3\\
 &+27566184d^4-42336000d^5+12584000d^7.
 \end{aligned}
\]

The denominator in (4.13) is negative on \(0<d<1\). It remains to
show \(P=-N>0\). The following is the exact Sturm chain, with every
negative-remainder polynomial divided only by a positive constant. To
keep the integer data readable, a row
\((c_0,\ldots,c_n)\) denotes \(\sum_{k=0}^nc_kd^k\):

\[
\begin{array}{c|l}
0&(1117641,-1354752,-2145330,5335616,-27566184,42336000,0,-12584000)\\
1&(-338688,-1072665,4001712,-27566184,52920000,0,-22022000)\\
2&(-7823487,8128512,10726650,-21342464,82698552,-84672000)\\
3&(-11726056380249141,7843068351873216,5954742586885950,
177345574574315648,-266456806379687064)\\
4&(25219611280876751200044430602657,
-35459635864920823030991636127690,
-24771205744998509711668340008818,
16006699832268743776993769057776)\\
5&(-27383920392877595418804200122890271491725967,
7099375591095670807319561219432663691237486,
72404333943288278565378315334330167162120062)\\
6&(-208119691802706660649919397964320819867582742079056686616,
365882708294084144936842222694381085514751788189790273481)\\
7&(-1).
\end{array}
\tag{4.14}
\]

The endpoint signs and variation counts are

\[
\begin{array}{c|c|c}
d& (s_0,s_1,s_2,s_3,s_4,s_5,s_6,s_7)&V(d)\\ \hline
0&( +,-,-,-,+,-,-,-)&3\\
1&( +,+,-,-,-,+,+,-)&3.
\end{array}
\tag{4.15}
\]

There are no endpoint zeros:
\(P(0)=1117641\) and \(P(1)=5138991\). Sturm's theorem therefore gives
no zero of \(P\) in \((0,1)\). Since \(P(0)>0\), \(P>0\), hence
\(N<0\). Equation (4.13) is strictly positive. Together with (4.12),
this proves (4.9), then \(\mathcal H<kL\), and completes (R39.18).
\(\square\)

The Sturm calculation is a single exact polynomial sign check inside an
analytic lemma. It is printed in full and is not a compact continuum
certificate.

## 5. Closure of the outer-\(B\)/lower-shelf endpoint

### Theorem 5.1 (simultaneous endpoint closes)

Every residual \(p\geq3\) gap-side endpoint satisfying

\[
 \chi=h,\qquad y_B=0,\qquad e_p=0
\]

has

\[
 \boxed{\Gamma_{\rm OB}>0.}
\tag{R39.19}
\]

It is therefore closed by the inherited implication chain to the shifted
defect.

#### Proof

At this endpoint, (R39.5) reads

\[
 \Gamma_{\rm OB}=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +p\Delta+a_pM_4-\frac{p-dm}{2}.
\tag{5.1}
\]

Here \(\beta<1/2\), \(J<1/7\), \(\Omega_-\geq0\),
\(\Delta\geq M_4\), and

\[
 M_4\geq g(\lambda+e_p)=g(j+u).
\]

Theorem 3.2 gives \(j\geq1\), while \(u>h>0\) on this face. Deliberately
weakening the sharper cap bound to \(J<1/7\), one has

\[
 p\Delta+a_pM_4
 \geq(p+a_p)M_4
 \geq(p+a_p)g(j+u)
 >(p+a_p)g,
\]

and therefore obtains

\[
 \Gamma_{\rm OB}>
 \frac67+B_0\zeta+(p+a_p)g-\frac{p-dm}{2}.
\tag{5.2}
\]

Put \(z=(m+\alpha)/p\). Since \(m=pz-\alpha\), Lemma 4.1 gives

\[
 \Gamma_{\rm OB}>
 \frac67+B_0\zeta-pC(d,z)-\frac{d\alpha}{2}.
\tag{5.3}
\]

If \(C(d,z)\leq0\), then

\[
 \Gamma_{\rm OB}>\frac67-\frac d2>0.
\]

Suppose \(C(d,z)>0\). From (R39.18),

\[
 pC<kp(1+z)L<k\mu L=k\zeta W,
\tag{5.4}
\]

where \(p(1+z)=p+m+\alpha=\mu-r<\mu\) and
\(W=\mu(\tan t-t)/\pi\). The exact outer-wall count relation is

\[
 W=B_0+\frac34-u.
\]

Since \(B_0\geq1\), \(u>0\), and \(0<k<1\),

\[
 B_0-kW=(1-k)B_0-\frac{3k}{4}+ku
 >1-\frac{7k}{4}.
\tag{5.5}
\]

Equations (5.3)--(5.5), \(\alpha<1\), and
\(\zeta=d/(1-d)\) yield

\[
 \begin{aligned}
 \Gamma_{\rm OB}
 &>\frac67+\zeta\left(1-\frac{7k}{4}\right)-\frac d2\\
 &=\frac{\mathcal Q(d)}{126(1-d)},
 \end{aligned}
\tag{5.6}
\]

where

\[
 \mathcal Q(d)=108-241d+63d^2+196d^5.
\]

It remains only to check \(\mathcal Q>0\) on \((0,1)\). One has

\[
 \mathcal Q'(d)=980d^4+126d-241,
 \qquad
 \mathcal Q''(d)=3920d^3+126>0.
\]

Thus \(\mathcal Q'\) has a unique zero \(d_*\), the global minimum.
Indeed, \(\mathcal Q'(0)=-241<0\) and
\(\mathcal Q'(1)=865>0\).
Moreover,

\[
 \mathcal Q'(16/25)=\frac{316931}{78125}>0,
\]

so \(d_*<16/25\). At \(\mathcal Q'(d_*)=0\), elimination of
\(d_*^4\) gives

\[
 \mathcal Q(d_*)=
 \frac{540-964d_*+189d_*^2}{5}.
\]

The numerator is decreasing on \([0,1]\); hence

\[
 \mathcal Q(d_*)>
 \frac{540-964(16/25)+189(16/25)^2}{5}
 =\frac{284}{3125}>0.
\]

Therefore (5.6) is strictly positive. Both intrinsic cases for \(C\)
close, proving (R39.19). \(\square\)

The split by the sign of the continuous scalar \(C(d,z)\) is the two-line
proof of one intrinsic inequality; it is not a ratio, count, or chamber
theorem family.

## 6. Ownership and equality-face audit

| face | exact owner used in this note | status after Round 39 |
|---|---|---|
| outer-\(B\) wall | literal strict count is \(B-1\); the gap-side label is \(B^+=B\), with \(v=B-1/4\), \(\chi=h\), \(y_B=0\), and \(\eta_B=0\) | (R39.5)--(R39.14) apply; no literal-wall relabeling |
| simultaneous lower-shelf face | inherited one-sided first-shelf label, \(A(x)=f-1/4\), \(e_p=0\) | closed by Theorem 5.1 |
| outer-\(B\), \(\alpha\uparrow1^-\) | retain the one-sided gap labels and exact cap; do not reindex as the next chart | open |
| \(Q\)-wall | \(\chi=0\), newest inverse displacement active | not signed here |
| old inverse wall | literal \(\eta_k=1\), adverse side \(\eta_k\downarrow0\) | retained in \(\Omega_-\); no new chamber |
| lower alpha limit | \(\alpha\downarrow0\) only | literal \(\alpha=0\) point is the separate equal-count corner |
| integer-\(\lambda\) wall | absent for \(0<\alpha<1\) by Round 38 | no new owner needed |
| hard wall \(p=dm\) | automatic sector | outside the residual |

The action equality \(A(x)+1/4\in\mathbb Z\) used in Theorem 5.1 is
owned only by the inherited lower-shelf one-sided face. No equality
\(r+j=\mu\) or \(r+j=K\) is created by the phase--stretch reduction.
The equality \(\mu-r\in\mathbb Z\) occurs only at an alpha endpoint and
is not silently absorbed into the positive-\(\alpha\) proof. Thus the
proof of Theorem 5.1 does not double-count an action jump, inverse jump,
or alpha chart.

## 7. Loss ledger

The proof levels remain distinct:

\[
 D_A(r)\ \geq\ \mathscr S\ \geq\ \Phi_\delta^+
 \ \geq\ \Gamma_{\rm gap}.
\]

| passage | exact status | reserve retained or discarded |
|---|---|---|
| Round 38 normal form to (R39.5) | exact identity on the one-sided outer-\(B\) face | retains \(J,\Omega_-,B_0\zeta,\Delta,M_4,e_p\); rewrites \(p\widehat\Xi\) exactly |
| \(\Phi_\delta^+\to\Gamma_{\rm gap}\) | exact known difference | \(a_p\widehat\Xi\geq0\) is the projection reserve |
| (R39.5) to (R39.8) | strict proof-level lower bound | exact loss is printed in (R39.9) |
| \(F_{\rm OB}\to F_{\rm OB}^{\rm RF}\) | optional lower projection | discards exactly \(\Omega_--\Omega_{\rm RF}\geq0\) |
| (5.1) to (5.2) | strict lower bound | discards \(1/(2\beta)-1>0\), the improvement \(1/7-J>0\), \(\Omega_-\geq0\), \(p(\Delta-M_4)\geq0\), \((p+a_p)\{M_4-g(j+u)\}\geq0\), and \((p+a_p)g\{(j-1)+u\}>0\) |
| (5.2) to (5.3) | strict lower bound | uses \(g>\gamma\) and discards \(a_pg>0\) when replacing \((p+a_p)g\) by \(p\gamma\) |
| (5.4)--(5.6) | intrinsic phase/count comparison | uses \(p(1+z)=\mu-r<\mu\), \(B_0\geq1\), \(u>0\), and \(\alpha<1\); every strictness is displayed |
| \(\mathscr S\to\Phi_\delta^+\) and \(D_A(r)\to\mathscr S\) | inherited lower bounds | exact terminal/shelf and first-shelf reduction slack remain separate and are not claimed lossless |

In particular, a failure of a coarser curvature-only or floor-only scalar
does not imply a failure of (R39.5), \(\Phi_\delta^+\), \(\mathscr S\),
\(D_A\), CST, or Pólya.

## 8. Diagnostic-only falsification report

The script computations/general_d_round39_outer_face_diagnostic.py is
explicitly diagnostic_only. It uses ordinary binary64 arithmetic and
SciPy root finding; its optional 100-decimal replay uses noninterval
mpmath. Nothing in Sections 1--5 depends on a scanned minimum.

The default bounded run tested 191,360 tuples and retained 406
outer-\(B\)/upper-alpha and 89 outer-\(B\)/lower-shelf roots. It found no
negative sampled value of \(\Gamma_{\rm gap}\),
\(\mathcal H_\Delta\), the right side of (R38.20),
\(\Phi_\delta^+\), \(F_{\rm OB}\), or
\(F_{\rm OB}^{\rm RF}\). The observed minima were:

\[
\begin{array}{c|cc}
\text{quantity}&\text{upper-alpha face}&\text{lower-shelf face}\\ \hline
\Gamma_{\rm gap}&1.972206417845344&3.875980171870619\\
\mathcal H_\Delta&0.996769141298673&1.229294186117076\\
\operatorname{RHS}(\mathrm{R38.20})&1.862922153331839&3.390663242469941\\
\Phi_\delta^+&1.973760997165515&3.876040340019174\\
F_{\rm OB}&1.822847916420817&3.742721311815124\\
F_{\rm OB}^{\rm RF}&1.465154163333695&2.758219030232993.
\end{array}
\]

The 89 lower-shelf samples had \(j=1\) in 88 cases and \(j=2\) in one,
consistent with Theorem 3.2. Their sampled minimum was \(B_0=2\), but no
analytic \(B_0\geq2\) claim is made.

The search decisively rejects two tempting coarse reductions. A
100-decimal noninterval replay at

\[
 (r,p,m,f,B)=(1,4,20,171,167),
\]

\[
 \alpha=0.681904708946359872\ldots,
 \qquad t=1.52512981603719044\ldots
\]

gives

\[
 C_{\rm curv}=-0.00121562781458\ldots.
\]

All tested feasibility margins there are positive, and \(e_p=0\), so
dropping \(2pe_p\) cannot repair this curvature-only sign. The original
quantities remain far positive in the same nonrigorous replay:

\[
 \Gamma_{\rm gap}\approx266.39,
 \qquad \mathcal H_\Delta\approx4.39,
 \qquad \Phi_\delta^+\approx266.39,
 \qquad \mathscr S\approx269.50.
\]

A separate high-floor binary64 stress run retained 6,167 upper-alpha and
21,121 lower-shelf roots. It found 1,177 negative upper and 12,753
negative lower \(C_{\rm curv}\) values; the sampled minima were about
\(-6.44\) and \(-7.25\). The floor-only \(L_j\) was negative on 18,332
lower roots, with sampled minimum about \(-8.86\). In contrast,
\(F_{\rm OB}^{\rm RF}\) had no sampled negative, with observed minima
about \(6.54\) and \(5.79\); \(L_j+\Omega_{\rm RF}\) also had no sampled
negative, with lower minimum about \(3.40\). These values are theorem-
design evidence only. They show why \(\Omega_-\) cannot be discarded
from the generic upper-alpha route; they do not prove its sign.

The symbolic companion
computations/general_d_round39_outer_face_replay.wl checks the exact
outer-face rewrite, action coordinates, loss ledger, root-free identity,
elasticity remainder, cap arithmetic, and the rational arithmetic in
Lemma 3.1. It prints round39OuterFaceReplayOK=True under Mathematica 15.0
on Windows. Mathematica owns no strict floor, one-sided endpoint,
continuum sign, or Sturm argument in this note.

## 9. Round 39 outcome and Gate A/B/C decision

### Proved

1. The residual cap sharpening \(J<1/10\) and automatic threshold
   \(p-dm\leq11/5\).
2. The exact outer-\(B\) identity (R39.5), the single intrinsic bound
   \(F_{\rm OB}\), its complete loss ledger, and its optional root-free
   form.
3. The exact elasticity-remainder formula (R39.14), including the reason
   no strictly positive \(\widehat\Xi\) reserve is available uniformly.
4. The analytic comparison (R39.15) and the floor elimination \(j\geq1\)
   on the simultaneous outer-\(B\)/lower-shelf face.
5. The phase--stretch inequality (R39.17)--(R39.18), with its exact
   tangent majorant, rational reduction, and Sturm proof.
6. Complete positivity of the selected scalar on the simultaneous
   outer-\(B\)/lower-shelf endpoint.

### Structural reduction still open

The gap-side outer-\(B\), \(\alpha\uparrow1^-\) endpoint retains the exact
cap formulas

\[
 h=\frac{\sqrt{2q+1}-q\arccos(q/(q+1))}{\pi},
\]

\[
 J=\frac{((q+1)^2+2q^2)\arccos(q/(q+1))
          -3q\sqrt{2q+1}}{2\pi},
\]

and the root-free inequality \(\Gamma_{\rm OB}>F_{\rm OB}^{\rm RF}\).
No continuum sign for that endpoint is claimed. The \(Q\)-wall, old
inverse faces, lower-alpha limit, literal equal-count corners, and broader
pointwise assembly also remain open unless already owned by an earlier
promoted theorem.

### Gate decision

**Gate A remains active only for the remaining intrinsic transported
outer-\(B\), upper-alpha endpoint.** The admissible next attempt is a
single continuous inequality through \(F_{\rm OB}\) or
\(F_{\rm OB}^{\rm RF}\), retaining \(J,W,u,e_p,\Omega_-\), and the exact
one-sided labels. It must not split by \(B_0\), \(j\), or ratio intervals.
The sampled failures of \(C_{\rm curv}\) and \(L_j\) forbid using either
as the generic owner.

If that exact endpoint sign is false, or if its proof requires a forbidden
ratio/count/chamber family, **Gate A stops**. Gate B then restores

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

with the exact shelf trapezoid, terminal surplus, cap, and inverse
fractions. Gate C is activated only if a certified feasible point has
\(\mathscr S<0\), or if one intrinsic theorem cannot localize its possible
negative support. Gate C begins with the ambient dimension \(4\) weighted
aggregate and the branching bonus; no second compact certificate is
authorized.

The lower-shelf endpoint theorem is a genuine new local closure, not a
claim that high-floor CST or the all-dimensional theorem is complete.
