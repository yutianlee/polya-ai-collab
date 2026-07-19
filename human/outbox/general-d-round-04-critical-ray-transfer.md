# General dimension, Round 4d: a quantitative transfer on the no-drop critical ray

Date: 18 July 2026

Status: rigorous conditional closure of the residual no-drop rays with
first floor \(f=2,3\).  Combined with the preceding cone reduction, it gives
the explicit cutoff \(n\ge 72\,000\).  This note does not treat the residual
first-drop branch.

The proof below is independent of the numerical diagnostics in the final
section.  Ordinary floors and strict terminal brackets retain their original
wall conventions throughout.

## 1. Input from the preceding no-drop reduction

Write

\[
 \delta=K-\mu,\qquad \epsilon=\frac\delta K=1-\rho,
 \qquad b=f-\frac14,
\]

and suppose

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \qquad(0\le j\le n),\qquad f\in\{2,3\}.
 \tag{1}
\]

The root-free no-drop cutoff and its complementary chamber reduction give,
for

\[
 c_f=\frac{\sqrt{1+b^2}-1}{2},\qquad
 C_0=\left(\frac\pi{12}\right)^{1/3},\qquad
 c_*=\frac{4\sqrt2}{15},
\]

\[
 S_j=\sum_{k=1}^j(k-\tfrac14)^{-1/3},\qquad
 C_K(f)=
 \left(\frac{f+1/2+c_*}{C_0S_{f-1}}\right)^3,
\]

and

\[
 C_\delta(f)=\bigl(8\pi^2f^2C_K(f)\bigr)^{1/3},
\]

the explicit cone

\[
 \frac{c_f}{2}n\le\delta\le C_\delta(f)n,
 \qquad
 \frac{c_f^2}{8\pi^2(C_\delta(f)+2)}n^3<K<C_K(f)n^3.
 \tag{2}
\]

Here (2) is needed only after the already automatic region has been removed,
and it is valid for \(n\ge\lceil2/c_f\rceil\).  The transfer below uses just
the lower bound for \(\delta\); the endpoint floors themselves recover much
sharper compact bounds for the scaled variables.

## 2. Statement of the transfer theorem

Put

\[
 s=\sqrt\epsilon,\qquad
 \kappa=s\delta=s^3K,\qquad N=sn,
 \tag{3}
\]

and let

\[
 \mathscr S_n=D_A(q)+R_n,
 \qquad q=r+n,
 \qquad
 R_n=2\int_r^qA(z)\,dz-2nf.
 \tag{4}
\]

### Theorem 2.1

Assume (1)--(2), with \(f\in\{2,3\}\).  If

\[
 \boxed{n\ge72\,000,}
 \tag{5}
\]

then

\[
 \boxed{s\mathscr S_n>\frac15.}
 \tag{6}
\]

In particular the no-drop shifted-tail scalar is strictly positive.  The
proof of \(\mathscr S_n>0\) itself includes the lower ordinary-floor wall at
\(q\).  At that wall the separate exact identity
\(D_A(r)=\mathscr S_n+1\) has an additional favorable unit for the original
tail defect.

The rest of Sections 2--7 is the proof.

## 3. Compactness forced by the endpoint floors

Let

\[
 \alpha=\mu-q\in[0,1).
\]

From (1),

\[
 b\le A(q)<b+1,\qquad A(r)<b+1.
 \tag{7}
\]

The radius derivative of the ball action gives the exact representation

\[
 A(z)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{z^2}{a^2}}\,da\qquad(0\le z\le\mu).
 \tag{8}
\]

The cone (2) and \(f\ge2\) imply \(\delta\ge1\).  For
\(a\in[\mu,K]\),

\[
 \sqrt{1-\frac{q^2}{a^2}}
 \le \sqrt{1-\frac{q^2}{K^2}}
 \le \sqrt{\frac{2(K-q)}K}
 \le2s.
\]

Conversely,

\[
 1-\frac{q^2}{a^2}
 =\frac{(a-q)(a+q)}{a^2}
 \ge\frac{a-\mu}{K}.
\]

Inserting these two estimates in (8) yields

\[
 \frac{2\kappa}{3\pi}\le A(q)\le\frac{2\kappa}{\pi}.
 \tag{9}
\]

Equations (7)--(9), \(3<\pi<22/7\), and
\(7/4\le b\le11/4\) give the convenient common bounds

\[
 \boxed{\frac{21}{8}\le\kappa<18.}
 \tag{10}
\]

At the other endpoint, monotonicity of the integrand in (8) gives

\[
 \begin{aligned}
 A(r)
 &\ge\frac\delta\pi\sqrt{1-\frac{r^2}{\mu^2}}
 \ge\frac\delta\pi\sqrt{\frac n\mu}\\
 &=\frac{\sqrt{\kappa N}}
 {\pi\sqrt{1-s^2}}
 \ge\frac{\sqrt{\kappa N}}\pi.
 \end{aligned}
\]

Together with (7), this proves

\[
 N<\frac{\pi^2(b+1)^2}{\kappa}
 \le\frac{18150}{343}<53.
 \tag{11}
\]

Finally, \(c_f/2>1/4\) for both floors: at \(f=2\), the smaller case,

\[
 \frac{c_2}{2}=\frac{\sqrt{65}-4}{16}>\frac14.
\]

Thus (2), (3), and (10) imply

\[
 s=\frac\kappa\delta<\frac{72}{n}.
 \tag{12}
\]

Under (5), therefore,

\[
 \boxed{0<s<10^{-3}.}
 \tag{13}
\]

## 4. Uniform turning remainder on the whole head

For

\[
 h(\theta)=\sin\theta-\theta\cos\theta
 =\int_0^\theta u\sin u\,du,
\]

the elementary sine bounds give

\[
 \frac{\theta^3}{3}-\frac{\theta^5}{30}
 \le h(\theta)\le\frac{\theta^3}{3}.
 \tag{14}
\]

If \(y=1-z/R\), then

\[
 \sqrt{2y}\le\arccos(1-y)
 \le\frac{\sqrt{2y}}{\sqrt{1-y/2}}.
\]

Consequently, with \(c_0=2\sqrt2/(3\pi)\),

\[
 \begin{aligned}
 c_0Ry^{3/2}
 \left(1-\frac{y}{5(1-y/2)^{5/2}}\right)
 &\le G_R(R(1-y))\\
 &\le c_0Ry^{3/2}(1-y/2)^{-3/2}.
 \end{aligned}
 \tag{15}
\]

For \(0\le y\le1/100\), both relative errors in (15) are at most
\(y\).  This follows from the mean-value theorem for
\((1-y/2)^{-3/2}\); its derivative is smaller than (1) on this
interval.

Use the exact critical coordinate

\[
 X=s(\mu-z),\qquad z=\mu-\frac Xs,
\]

and define

\[
 \mathcal H_{s,\kappa}(X)
 :=A\left(\mu-\frac Xs\right),
 \qquad
 H_\kappa(X)
 :=\frac{c_0}{\sqrt\kappa}
 \bigl((\kappa+X)^{3/2}-X^{3/2}\bigr).
 \tag{16}
\]

The two exact turning parameters are

\[
 y_K=s^2\left(1+\frac X\kappa\right),
 \qquad
 y_\mu=\frac{s^2X}{\kappa(1-s^2)}.
 \tag{17}
\]

For \(0\le X\le54\), (10) and (13) give

\[
 0\le y_K,y_\mu\le22s^2<\frac1{100}.
 \tag{18}
\]

The leading outer and inner terms in (15) satisfy

\[
 c_0\frac{(\kappa+X)^{3/2}}{\sqrt\kappa}<144,
 \qquad
 c_0\frac{X^{3/2}}{\sqrt\kappa}<90.
 \tag{19}
\]

For the inner ball its natural leading term contains the extra factor
\((1-s^2)^{-1/2}\).  Since

\[
 0<(1-s^2)^{-1/2}-1\le s^2,
 \qquad (1-s^2)^{-1/2}<\frac{16}{15},
\]

equations (15), (18), and (19) give, uniformly on \([0,54]\),

\[
 \begin{aligned}
 \left|G_K- c_0\frac{(\kappa+X)^{3/2}}{\sqrt\kappa}\right|
 &\le3168s^2,\\
 \left|G_\mu-c_0\frac{X^{3/2}}{\sqrt\kappa}\right|
 &\le2202s^2.
 \end{aligned}
\]

Therefore

\[
 \boxed{
 \left|\mathcal H_{s,\kappa}(X)-H_\kappa(X)\right|
 \le5500s^2\qquad(0\le X\le54).}
 \tag{20}
\]

This is the required uniform finite-\(\epsilon\) turning remainder.

## 5. Uniform transfer of the no-drop head

The limit profile satisfies

\[
 0<H_\kappa'(X)
 =\frac{3c_0}{2\sqrt\kappa}
 \bigl(\sqrt{\kappa+X}-\sqrt X\bigr)
 \le\frac{3c_0}{2}<\frac12.
 \tag{21}
\]

At \(q\), put \(X_q=s\alpha\in[0,s)\).  Equations (20)--(21) imply

\[
 \left|\mathcal H_{s,\kappa}(X_q+t)-H_\kappa(t)\right|
 \le\zeta,
 \qquad
 \zeta:=\frac s2+5500s^2,
 \tag{22}
\]

for \(0\le t\le N\).  By (11), the arguments stay below (54).
Also, by (13),

\[
 \boxed{\zeta\le\frac3{500}.}
 \tag{23}
\]

The exact change of variables in the head is

\[
 sR_n=2\int_0^N
 \bigl(\mathcal H_{s,\kappa}(X_q+t)-f\bigr)\,dt.
\]

Hence (11) and (22) give

\[
 sR_n\ge
 2\int_0^N(H_\kappa(t)-f)\,dt-106\zeta.
 \tag{24}
\]

Put \(w=H_\kappa(0)=c_0\kappa\).  The lower endpoint floor and
(22) give

\[
 w\ge b-\zeta.
 \tag{25}
\]

We now bound the possible negative part of the limiting integral without
any asymptotic notation.  If \(w\ge f\), it is nonnegative.  If
\(w<f\), let \(X_f\) be the unique point with \(H_\kappa(X_f)=f\).
The integral is minimized when \(N=X_f\).

Write \(X_f=\kappa u\) and

\[
 t_f=\sqrt{1+u}-\sqrt u.
\]

Direct algebra gives

\[
 \frac f w=\frac{3/t_f+t_f^3}{4},
 \qquad H_\kappa'(X_f)=\frac{3c_0}{2}t_f.
\]

Since the first expression is at least \(3/(4t_f)\),

\[
 H_\kappa'(X_f)\ge\frac{9c_0w}{8f}.
\]

Concavity makes this a lower derivative bound on \([0,X_f]\).  Thus

\[
 2\int_0^{X_f}(f-H_\kappa(t))\,dt
 \le\frac{16f(f-w)^2}{9c_0w}.
\]

Using (25), we have proved the wall-uniform head estimate

\[
 \boxed{
 sR_n\ge-P_f(\zeta)-106\zeta,
 \qquad
 P_f(\zeta)=
 \frac{16f(1/4+\zeta)^2}{9c_0(b-\zeta)}.}
 \tag{26}
\]

## 6. Uniform transfer of the first exact terminal angle

The endpoint floor gives \(G_K(q)\ge A(q)\ge7/4\), so the first complete
ball level is present even at a strict wall.  Let \(\theta\) be its exact
angle:

\[
 \frac K\pi h(\theta)=\tau,
 \qquad \tau=\frac34.
 \tag{27}
\]

Here \(\theta\in(0,\pi/2)\): indeed
\(G_K(0)=K/\pi\ge G_K(q)ge7/4>\tau\), while \(q\ge0\).

Put

\[
 x=\left(\frac{3\pi\tau}{K}\right)^{1/3}
 =s\left(\frac{3\pi\tau}{\kappa}\right)^{1/3}.
\]

The global chord bound \(\sin u\ge2u/\pi\) first gives

\[
 \frac{\theta^3}{s^3}
 \le\frac{9\pi^2}{8\kappa}<\frac{30}{7},
 \qquad \theta<\sqrt3\,s.
 \tag{28}
\]

Using the lower Taylor bound in (14) in (27), and then (28), gives

\[
 \frac{\pi s}{2\theta}
 \ge
 \frac{\pi s}{2x}
 \left(1-\frac{3s^2}{10}\right).
 \tag{29}
\]

Since \(w=c_0\kappa\), the leading term is exactly

\[
 \frac{\pi s}{2x}
 =\frac\pi{2\sqrt2}
 \left(\frac w\tau\right)^{1/3}.
 \tag{30}
\]

The exact-angle terminal estimate, restricted to its first positive level,
is

\[
 sD_A(q)\ge
 \frac{\pi s}{2\theta}-sQ-2s\int_q^\mu G_\mu(z)\,dz.
\]

Here \(Q\le f\le3\), while the universal turning cap gives

\[
 2\int_q^\mu G_\mu(z)\,dz<c_*<\frac25.
\]

Combining this with (25), (29), and (30) proves

\[
 \boxed{
 sD_A(q)\ge
 \frac\pi{2\sqrt2}
 \left(\frac{b-\zeta}{3/4}\right)^{1/3}
 \left(1-\frac{3s^2}{10}\right)
 -\frac{17}{5}s.}
 \tag{31}
\]

## 7. Explicit arithmetic closure

The estimates used here are deliberately rational and non-sharp.  From
\(b\ge7/4\) and (23),

\[
 \frac{b-\zeta}{3/4}
 \ge\frac{872}{375}>\left(\frac{13}{10}\right)^3,
 \qquad \frac\pi{2\sqrt2}>1.
\]

Therefore the first factor in (31) is larger than \(13/10\).
Moreover

\[
 c_0=\frac{2\sqrt2}{3\pi}>\frac{49}{165}.
\]

The expression \(P_f(3/500)\) is largest at \(f=2\), and

\[
 P_f(\zeta)
 <\frac{32(32/125)^2}
 {9(49/165)(218/125)}
 =\frac{180224}{400575}<\frac9{20}.
 \tag{32}
\]

Finally, add (26) and (31), and use
\(s<1/1000\), \(\zeta\le3/500\).  One obtains

\[
 \begin{aligned}
 s\mathscr S_n
 &>\frac{13}{10}\left(1-\frac3{10^7}\right)
 -\frac9{20}-\frac{318}{500}-\frac{17}{5000}\\
 &=\frac{21059961}{100000000}>\frac15.
 \end{aligned}
\]

This proves Theorem 2.1.

## 8. Diagnostics (not used in the proof)

At the limiting value \(\zeta=0\), the lower bound obtained by retaining
the sharper derivative at the level (f) is approximately

\[
 \begin{array}{c|c|c|c}
 f&\text{first-level terminal}&\text{head-loss majorant}&\text{gap}\\
 \hline
 2&1.4732&0.4231&1.0501\\
 3&1.7128&0.4039&1.3089
 \end{array}
\]

At the proof cutoff \(s=10^{-3}\), direct floating-point substitution in
the unrounded formulas (26) and (31) gives lower margins about (0.387)
for (f=2) and (0.648) for (f=3).  These values only explain why the
coarse rational closure has room; they are not premises of the theorem.

## 9. Exact scope

The theorem supplies the missing quantitative replacement for the compactness
argument in Corollary 3.2 of the high-floor cutoff note:

* the action remainder is uniform on the entire no-drop head;
* the exact first terminal angle is transferred with a signed remainder;
* the integer cutoff is explicit;
* equality walls are included.

After the preceding reduction to \(f=2,3\) and the cone (2), every no-drop
branch with \(n\ge72\,000\) is therefore closed.  The remaining no-drop
problem is a finite collection of branches with (n<72\,000), to which the
finite wall reduction applies.  No claim about the first-drop zero-level ray
is made here.
