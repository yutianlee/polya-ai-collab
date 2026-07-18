# General dimension, Round 7: a global scalar on the thin high-floor side

Date: 18 July 2026  
Scope: high-floor first-drop configurations
\(F_0=f\geq2\), \(p<n\), and \(\rho>99/100\)  
Status: rigorous exclusion of the whole stated ratio range.  Together with
the already audited fixed-ratio reduction on \(\rho\leq99/100\), this
replaces the former \(1.5625\times10^{17}\) high-floor cutoff by the
fixed-ratio cutoff below \(7.1\times10^9\).  It does **not** certify the
remaining fixed-ratio compact walls.

Ordinary floors define the first shelf.  Strict brackets define every
terminal count.  In particular, no equality wall is filled by continuity.

## 1. Exact setup

Put

\[
 \mu=\rho K,\qquad
 c=\frac{\arccos\rho}{\pi},\qquad
 d=\frac{2\arcsin\rho}{\pi}=1-2c,
\]

and let

\[
 H(t)=A(\mu-t),\qquad 0\leq t\leq\mu,
 \qquad W=H(0)=G_K(\mu).
\]

The profile \(H\) is increasing and concave, and

\[
 0\leq H'(t)\leq c.                                      \tag{1}
\]

For the first ordinary-floor shelf write

\[
 h=f-\frac14,\qquad x=r+p,\qquad m=n-p,
\]

and let \(M\) be the unique point \(H(M)=h\).  The first-drop condition
gives

\[
 M\leq\mu-x<M+1.                                        \tag{2}
\]

If the level \(f\) exists, let \(T\) satisfy \(H(T)=f\).  If it is absent,
put \(T=\mu\) and

\[
 \zeta=f-H(T)\in(0,1/4].
\]

In the existing reduced scalar

\[
 \mathcal S=D_A(q)+P,
 \qquad
 P=R_p+\frac d2m,
\]

the completed one-interface theorem gives \(D_A(q)\geq0\).  Round 5 used
the exact but deliberately coarse bound

\[
 P\geq\frac{(1+d)M-T-d}{2}.                             \tag{3}
\]

That bound by itself is not sufficient.  For example, the floating-point
configuration

\[
 \rho=0.99,\qquad W=0.188656241095\ldots,\qquad f=2
\]

has \(T=\mu\), \(B_0=0\), and the right side of (3) is approximately
\(-6.48\).  This is only a counterexample to the coarse lower bound, not to
the exact scalar.

## 2. Endpoint-chord prefix

The needed repair retains the endpoint height of the negative shelf
deficit.

### Lemma 2.1 (endpoint-chord prefix)

With \(\zeta=0\) when the level \(f\) exists and with \(\zeta\) as above
when it is absent,

\[
 \boxed{
 P\geq-\left(\frac14+\zeta\right)(T-M)
       +\frac d2(M-1).}                                \tag{4}
\]

### Proof

Put \(t_x=\mu-x\).  By (2), \(t_x\geq M\), while

\[
 m=t_x-\alpha\geq t_x-1\geq M-1,
 \qquad \alpha=\mu-q\in[0,1).
\]

After changing variables from \(z\) to \(t=\mu-z\), discard the
nonnegative part of the shelf integral.  This gives

\[
 R_p\geq-2\int_M^T(f-H(t))\,dt.                         \tag{5}
\]

Because \(H\) is concave, \(f-H\) is convex.  Its endpoint heights on
\([M,T]\) are \(1/4\) and \(\zeta\).  A convex function lies below its
endpoint chord, so

\[
 2\int_M^T(f-H(t))\,dt
 \leq\left(\frac14+\zeta\right)(T-M).
\]

Adding \(dm/2\geq d(M-1)/2\) proves (4).  If the level is absent, the
shelf condition itself gives \(H(\mu)\geq h\), hence
\(0<\zeta\leq1/4\).  No wall limit is used.

## 3. The sector with no complete interface level

Define the strict interface count

\[
 B_0=\left[W+\frac14\right]_<,
 \qquad
 \delta=h-W>0.                                         \tag{6}
\]

If \(B_0=0\), then \(W\leq3/4\), including equality, and therefore

\[
 \delta=f-\frac14-W\geq f-1\geq1.                     \tag{7}
\]

The ratio assumption gives the convenient strict bounds

\[
 c<\frac1{20},\qquad d>\frac9{10}.                     \tag{8}
\]

Equation (1) gives

\[
 M\geq\frac\delta c\geq\frac1c>20.                   \tag{9}
\]

We use the already proved shell-increment elasticity.  With

\[
 V(t)=t(2\mu-t),
\]

it says

\[
 \frac{H(t_2)-W}{H(t_1)-W}
 \geq\sqrt{\frac{V(t_2)}{V(t_1)}}.                    \tag{10}
\]

If \(r=t_2/t_1\geq1\) and \(t_2\leq\mu\), then

\[
 \frac{V(t_2)}{V(t_1)}
 \geq\frac{r^2}{2r-1}.                                \tag{11}
\]

Suppose first that the level \(f\) exists.  Equations (7), (10), and
(11) give

\[
 \frac{T/M}{\sqrt{2T/M-1}}
 \leq1+\frac1{4\delta}\leq\frac54,
\]

and hence \(T/M\leq5/2\).  The endpoint chord (4) now gives

\[
 P\geq
 \left(\frac d2-\frac38\right)M-\frac d2
 >\frac3{40}\,20-\frac12=1.                           \tag{12}
\]

Now suppose that the level is absent.  Put

\[
 a=\frac14-\zeta\in[0,1/4].
\]

Then (10)--(11), with \(T=\mu\), give

\[
 \frac{\mu/M}{\sqrt{2\mu/M-1}}
 \leq1+\frac a\delta\leq1+a.                         \tag{13}
\]

For \(R\geq1\), the upper root of
\(r/\sqrt{2r-1}=R\) is

\[
 r_*(R)=R^2+R\sqrt{R^2-1}.
\]

The following elementary inequality is the only finite algebraic check in
this case:

\[
 \boxed{
 \left(\frac12-a\right)\bigl(r_*(1+a)-1\bigr)
 <\frac{19}{50}
 \qquad(0\leq a\leq1/4).}                             \tag{14}
\]

Indeed, put \(x=\sqrt a\in[0,1/2]\).  Since
\(\sqrt{a(2+a)}\leq3\sqrt a/2\), the left side of (14) is at most

\[
 U(x)=\left(\frac12-x^2\right)
 \left(2x^2+x^4+\frac32x(1+x^2)\right).
\]

After \(y=2x\), all degree-32 Bernstein coefficients of
\(19/50-U(y/2)\) are positive; the smallest is

\[
 \frac{309}{396800}.
\]

The exact rational replay is in the verifier cited below.  Equations
(4), (9), (13), and (14) yield

\[
 P>\left(\frac d2-\frac{19}{50}\right)M-\frac d2
 >\frac7{100}\,20-\frac12=\frac9{10}.                \tag{15}
\]

Thus every \(B_0=0\) configuration has \(P>0\), including the complete
absent-level face and the strict wall \(W=3/4\).  No terminal estimate is
needed.

## 4. A scale-free bound for the last action quarter

The preceding proof in fact handles every configuration with
\(\delta\geq1\), regardless of \(B_0\).  It remains only to treat

\[
 0<\delta<1.                                           \tag{16}
\]

Then the strict convention in (6) gives exactly

\[
 B_0=f-1,
 \qquad
 W=f-\frac14-\delta>f-\frac54\geq\frac34.             \tag{17}
\]

Put

\[
 y=f-W=\delta+\frac14\in\left(\frac14,\frac54\right).
\]

We prove the uniform level-distance estimate

\[
 \boxed{T<\frac{3y}{c}.}                              \tag{18}
\]

This estimate also proves that the level \(f\) exists.

Let

\[
 \theta=\arccos\rho,\qquad
 \Phi(\theta)=\sin\theta-\theta\cos\theta,
 \qquad W=K\frac{\Phi(\theta)}\pi.
\]

For fixed \(\rho\), the increment

\[
 E_K(t)=H(t)-W
\]

has the scaling form \(E_K(t)=K E_1(t/K)\), where \(E_1\) is increasing,
concave, and vanishes at zero.  Therefore

\[
 \partial_KE_K(t)=E_1(u)-uE_1'(u)\geq0,
 \qquad u=t/K.                                        \tag{19}
\]

At fixed \(y\), the distance to the level \(W+y\) is consequently largest
at the smallest admissible \(W\).  Since \(W=f-y\geq2-y\), it suffices to
prove (18) for

\[
 f=2,\qquad W=2-y.                                   \tag{20}
\]

Set \(t_0=3y/c=3\pi y/\theta\), \(\epsilon=1-\rho\), and
\(u_0=t_0/\mu\).  The elementary bounds

\[
 \theta^2<\frac{21}{1000},\qquad
 \frac{499}{1000}\theta^2<\epsilon\leq\frac12\theta^2,
\]

\[
 \frac{9979}{30000}\theta^3
 <\Phi(\theta)<\frac13\theta^3                     \tag{21}
\]

follow from \(\sin s\leq s\),
\(\sin s\geq s-s^3/6\), and \(\rho>99/100\).  They imply

\[
 u_0=\frac{3y\Phi(\theta)}{\theta\rho W}<\frac9{250},\qquad
 \frac{u_0}{\epsilon}>
 \frac{199}{100}\frac yW.                            \tag{22}
\]

Thus \(t_0<\mu\).  The exact increment formula is

\[
 E_K(t_0)=\frac\mu\pi\int_0^{u_0}
 \left[
 \arccos\bigl(\rho(1-u)\bigr)-\arccos(1-u)
 \right]du.                                           \tag{23}
\]

Use

\[
 \sqrt{2z}\leq\arccos(1-z)
 \leq\frac{\sqrt{2z}}{\sqrt{1-z/2}}.
\]

After \(u=\epsilon v\), equations (21)--(22) give

\[
 E_K(t_0)>
 \frac{147}{100}W\int_0^V
 \left[
 \sqrt{1+\frac{99}{100}v}
 -\frac{101}{100}\sqrt v
 \right]dv,                                          \tag{24}
\]

where

\[
 V=\frac{199}{100}\frac yW.
\]

Here the coefficient follows from

\[
 \frac{\rho W\sqrt2\,\epsilon^{3/2}}{\Phi(\theta)}
 >\frac{147}{100}W,
\]

and the factor \(101/100\) is valid because
\(u\leq u_0<9/250\).  The displayed integrand is positive throughout the
retained interval.

Define

\[
 I(V)=\frac{200}{297}
 \left(\left(1+\frac{99}{100}V\right)^{3/2}-1\right)
 -\frac{101}{150}V^{3/2}.                             \tag{25}
\]

With \(x=y/W=y/(2-y)\), one has

\[
 \frac17<x<\frac53.
\]

The function

\[
 J(x)=\frac{147}{100}I\left(\frac{199}{100}x\right)-x
\]

is concave.  Indeed \(I''<0\), since

\[
 \frac{(99/100)^2}{1+(99/100)V}
 <\frac{(101/100)^2}{V}.
\]

Directed evaluation of the two endpoints gives

\[
 J(1/7)>\frac3{20},\qquad
 J(5/3)>\frac7{50}.                                  \tag{26}
\]

Concavity and (24)--(26) show \(E_K(t_0)>Wx=y\).  Hence the level \(f\)
occurs before \(t_0\), proving (18).

## 5. Terminal payment and exclusion of \(\delta<1\)

Since the level exists, (4), (9), and (18) give

\[
\begin{aligned}
 cP
 &\geq-\frac{cT}{4}
   +\left(\frac14+\frac d2\right)cM-\frac{cd}{2}\\
 &>-\frac34\left(\delta+\frac14\right)
   +\frac7{10}\delta-\frac1{40}
 >-\frac{21}{80}.                                    \tag{27}
\end{aligned}
\]

At the terminal start \(q\), let

\[
 B=\left[G_K(q)+\frac14\right]_<,
 \qquad Q=\left[A(q)+\frac14\right]_<.
\]

The first drop gives \(Q\leq f-1\), while \(q\leq\mu\) gives
\(B\geq B_0=f-1\).  For \(1\leq k\leq f-1\), let \(\theta_k\) be the
exact ball angle at level \(k-1/4\).  Equation (17) is strict, so

\[
 k-\frac14\leq f-\frac54<W=G_K(\mu),
 \qquad \theta_k<\theta=\pi c.                       \tag{28}
\]

The wall-safe exact-angle reserve and the cap bound therefore give

\[
 D_A(q)>
 \frac{f-1}{2c}-(f-1)-\frac25.
\]

Multiplying by \(c\), using \(f\geq2\) and \(c<1/20\), yields

\[
 cD_A(q)>\frac12-\frac1{20}\frac75
 =\frac{43}{100}.                                    \tag{29}
\]

Finally, (27)--(29) give the strict global margin

\[
 \boxed{
 c\mathcal S>\frac{43}{100}-\frac{21}{80}
 =\frac{67}{400}>0.}                                 \tag{30}
\]

Thus no negative high-floor first-drop scalar exists when
\(\rho>99/100\).

## 6. Consequence for the residual box

The formerly audited critical-end transfer only excluded
\(1-\rho\leq10^{-8}\), which led, after the thin high-energy cutoff, to

\[
 K<156\,250\,000\,000\,000\,000.
\]

The present theorem removes the entire range \(\rho>99/100\), without a
condition on \(K,f,n,p\), or any terminal wall.  Hence every remaining
negative high-floor first-drop candidate lies in

\[
 \rho\leq\frac{99}{100}.
\]

The already audited fixed-ratio estimate then gives

\[
 \boxed{K<\frac{16\,988\,400\,000\,000}{2401}
 <7.1\times10^9.}                                    \tag{31}
\]

This is a reduction by more than seven orders of magnitude.  It is still
a compact reduction rather than a certificate of the remaining
\(\rho\leq99/100\) walls.

## 7. Reproducibility

The verifier

```text
scripts/general_d_high_floor_global_scalar_verify.py
```

uses exact rational arithmetic for the Bernstein and algebraic
comparisons and Arb directed rounding for the transcendental endpoint
checks.  At both 512 and 1024 bits it reports:

```text
PASS ratio constants: c<1/20, d>9/10, theta^2<21/1000
PASS absent-level Bernstein bound: one panel, degree 32, 33 coefficients,
  minimum coefficient 309/396800
PASS scaled-profile constants: u0<9/250 and coefficient>147/100
PASS profile concavity and endpoint margins:
  J(1/7)>3/20, J(5/3)>7/50
PASS delta>=1 margins: P>1 (level present), P>9/10 (absent)
PASS delta<1 margin: c*S>67/400
```

The theorem proved here is exactly the no-negative conclusion on
\(\rho>99/100\).  The verifier does not sample the scalar and makes no
claim about the residual fixed-ratio compact walls.
