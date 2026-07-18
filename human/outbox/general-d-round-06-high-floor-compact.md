# General dimension, Round 6: an explicit compact box for the high-floor first-drop branch

Date: 18 July 2026  
Scope: \(F_0=f\geq2\), \(p<n\), for the exact reduced scalar  
Status: rigorous numerical finite cutoff. This is **not** a certificate of
the residual compact walls.

This note makes the qualitative compactness theorem in
human/outbox/general-d-round-05-high-floor-first-drop.md quantitative. It
excludes negative scalars on a uniform finite-thickness end and combines
that exclusion with the already proved fixed-ratio and thin high-energy
theorems. The resulting box is deliberately enormous, but every bound is
numerical and the residual integer data are genuinely finite.

Ordinary floors define the first shelf. Strict brackets define the terminal
counts \(Q,B\). No equality wall is filled by continuity.

## 1. Setup and statement

Put

\[
 \epsilon=1-\rho,\qquad s=\sqrt\epsilon,\qquad
 a=K-\mu,\qquad \kappa=sa=s^3K,
\]

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad
 \alpha=\mu-q\in[0,1),\qquad m=n-p,
\]

and

\[
 h=f-\frac14,\qquad x=r+p,\qquad
 d=d_\rho=\frac{2\arcsin\rho}{\pi}.
\]

The scalar is

\[
 \mathcal S=D_A(q)+R_p+\frac d2m,
 \qquad
 R_p=2\int_r^x A(z)\,dz-2pf.                 \tag{1}
\]

The completed one-interface theorem gives \(D_A(q)\geq0\). The first-drop
condition gives

\[
 W:=G_K(\mu)<h.                                  \tag{2}
\]

### Theorem 1.1 (uniform exact critical-end exclusion)

For every high-floor first-drop configuration \(f\geq2,\ p<n\), if

\[
 0<s\leq\frac1{10000},                            \tag{3}
\]

then, including at every ordinary-floor and strict-bracket wall, no negative
reduced scalar exists:

\[
 \boxed{\mathcal S\geq0.}                        \tag{4}
\]

More precisely, assuming \(\mathcal S<0\) makes the estimates below imply
the incompatible inequality \(s\mathcal S>1/2\). No unconditional
half-unit gap is asserted.

In particular, every negative high-floor first-drop scalar satisfies

\[
 \boxed{1-\rho=\epsilon>10^{-8}.}                 \tag{5}
\]

The proof occupies Sections 2--7.

## 2. A numerical, non-asymptotic interface pinning

For Sections 2--7, suppose for contradiction that \(\mathcal S<0\).

Use distance from the interface,

\[
 \widehat H(t)=A(\mu-t),\qquad 0\leq t\leq\mu.
\]

Let \(M\) be the unique point \(\widehat H(M)=h\). Let \(T\) be the point
\(\widehat H(T)=f\) if that level exists, and otherwise put \(T=\mu\).
The exact prefix geometry from Round 5 says that negativity implies

\[
 T>(1+d)M-d.                                      \tag{6}
\]

Also

\[
 0\leq\widehat H'(t)\leq c_\rho,\qquad
 c_\rho=\frac{\arccos\rho}{\pi}<s,\qquad
 d=1-2c_\rho>1-2s.                                \tag{7}
\]

For (7), use

\[
 \arccos(1-s^2)=2\arcsin\frac{s}{\sqrt2}<\pi s.
\]

If \(M\leq100\), then (3) and (7) give

\[
 W>h-\frac1{100}.                                 \tag{8}
\]

Suppose \(M>100\). From (6),

\[
 \frac TM>1+(1-2s)\frac{99}{100}.
\]

The right side is at least

\[
 r_0=1+\frac{4999}{5000}\frac{99}{100}.
\]

The exact shell-increment elasticity inequality gives

\[
 \frac{\widehat H(T)-W}{h-W}
 \geq\sqrt{\frac{T(2\mu-T)}{M(2\mu-M)}}
 \geq\frac{T/M}{\sqrt{2T/M-1}}.
\]

Exact rational arithmetic gives

\[
 \frac{r_0}{\sqrt{2r_0-1}}>\frac{23}{20}.         \tag{9}
\]

This argument also covers the convention in which the level \(f\) is
absent: then \(\widehat H(T)\leq f\), so
\((f-W)/(h-W)\) dominates the actual elasticity quotient. Hence (9) and
\(h=f-1/4\) give

\[
 \frac{f-W}{f-W-1/4}>\frac{23}{20},
 \qquad f-W<\frac{23}{12}.                        \tag{10}
\]

The small-\(M\) estimate (8) is stronger than (10). Thus every negative
candidate satisfying (3) obeys the uniform exact pinning

\[
 \boxed{W>f-\frac{23}{12}\geq\frac1{12}.}         \tag{11}
\]

## 3. The level \(f\) exists and the turning window is bounded

Define the exact and critical scaled profiles

\[
 \mathcal H_{s,\kappa}(X)=A\left(\mu-\frac Xs\right),
\]

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right),
 \qquad c_0=\frac{2\sqrt2}{3\pi},
 \qquad w=H_\kappa(0)=c_0\kappa.                 \tag{12}
\]

At \(X=0\), the exact non-cancelling integral representation gives

\[
 \sqrt{1-s^2}\,w\leq W\leq\frac{w}{1-s^2}.       \tag{13}
\]

Since \(f-23/12\geq f/24\) for \(f\geq2\), (11)--(13) imply

\[
 A(0)=\frac a\pi=\frac{w}{c_0\pi s}
 >\frac{(1-s^2)f}{24s}>f.                         \tag{14}
\]

Thus the level \(T\) from Section 2 is the genuine level
\(\widehat H(T)=f\).

We first bound the complete turning window without a local asymptotic
expansion. Put

\[
 \mathcal E_{a,K}(z)=\frac a\pi\sqrt{1-\frac{z^2}{K^2}}.
\]

The exact shell-envelope sandwich gives

\[
 A(z)\geq\frac23\mathcal E_{a,K}(z).              \tag{15}
\]

For \(X=\kappa u\), put \(y=s^2(1+u)\). At a physical point \(z\geq0\),
\(0\leq y\leq1\), and

\[
 \mathcal E_{a,K}\left(\mu-\frac Xs\right)
 =\frac{\sqrt2\kappa}{\pi}\sqrt{1+u}
   \sqrt{1-\frac y2}.
\]

Moreover

\[
 \frac{H_\kappa(\kappa u)}
 {\sqrt2\kappa\sqrt{1+u}/\pi}
 =\frac23(1+u)
 \left[1-\left(\frac{u}{1+u}\right)^{3/2}\right]\leq1.
\]

Consequently

\[
 \boxed{\mathcal H_{s,\kappa}(X)
 \geq\frac{2}{3\sqrt2}H_\kappa(X)}               \tag{16}
\]

throughout the physical inner interval.

Let \(X_T=sT\), write \(X_T=\kappa u_T\), and introduce

\[
 t_T=\sqrt{1+u_T}-\sqrt{u_T},\qquad
 F(t)=\frac{3/t+t^3}{4}.
\]

Then \(H_\kappa(X_T)/w=F(t_T)\). Equations (11), (13), and (16)
give

\[
 F(t_T)<\frac{3\sqrt2}{2}\,25<54.
\]

Since \(F(t)\geq3/(4t)\),

\[
 \boxed{t_T>\frac1{72},\qquad
 \frac{X_T}{\kappa}=u_T
 =\frac{(1-t_T^2)^2}{4t_T^2}<1296.}               \tag{17}
\]

This bound is uniform in \(f\).

## 4. Uniform exact-to-critical comparison

The exact non-cancelling representation is

\[
 \mathcal H_{s,\kappa}(X)=\frac1\pi\int_0^\kappa
 \frac{\sqrt{(\kappa+X-v)
 [2\kappa-(\kappa+X+v)s^2]}}
 {\kappa-vs^2}\,dv.                               \tag{18}
\]

The ratio of its integrand to the integrand defining \(H_\kappa\) is

\[
 \mathcal R(v,X)=
 \frac{\sqrt{1-\mathfrak a(v,X)s^2}}
 {1-\mathfrak b(v)s^2},
 \quad
 \mathfrak a=\frac{\kappa+X+v}{2\kappa},
 \quad \mathfrak b=\frac v\kappa.                \tag{19}
\]

On \(0\leq X\leq X_T\), (17) gives

\[
 0\leq\mathfrak b\leq1,\qquad
 0\leq\mathfrak a<649.
\]

Using \(\sqrt{1-y}\geq1-y\), (3), and
\((1-s^2)^{-1}<1001/1000\), one obtains

\[
 \boxed{
 \frac{999}{1000}<
 \frac{\mathcal H_{s,\kappa}(X)}{H_\kappa(X)}
 <\frac{1001}{1000}
 \quad(0\leq X\leq X_T).}                        \tag{20}
\]

This is a relative estimate and is therefore uniform even when \(f\)
varies.

## 5. A robust forced-slope lemma

Put \(X_M=sM\), so that

\[
 \mathcal H_{s,\kappa}(X_M)=h,\qquad
 \mathcal H_{s,\kappa}(X_T)=f.
\]

We claim

\[
 \boxed{t_T>\frac13.}                             \tag{21}
\]

If \(M\leq100\), equations (8), (13), and (20) give

\[
 F(t_T)<\frac{100}{87}\left(\frac{1000}{999}\right)^2
 <\frac65<F\left(\frac13\right),
\]

which proves (21) in this case.

Suppose \(M>100\). Negativity of \(\mathcal S\), together with
\(D_A(q)\geq0\), forces

\[
 P:=R_p+\frac d2m<0.                               \tag{22}
\]

Let \(X_x=s(\mu-x)\). A negative prefix has \(A(x)<f\). Since the exact
inner profile is increasing and concave, \(f-\mathcal H\) is nonnegative
and convex from \(X_x\) to \(X_T\), with endpoint values at most \(1/4\)
and zero. Hence

\[
 sR_p\geq-2\int_{X_x}^{X_T}(f-\mathcal H)\,dX
 \geq-\frac{X_T-X_x}{4}.                           \tag{23}
\]

Also \(sm=X_x-s\alpha\geq X_x-s\), and \(X_x\geq X_M\). From
(22)--(23),

\[
 X_T>(1+2d)X_M-2ds.
\]

After division by \(X_M=sM\), (3), (7), and \(M>100\) give

\[
 \frac{X_T}{X_M}>
 1+2(1-2s)\frac{99}{100}>\frac52.                 \tag{24}
\]

Assume, to the contrary, \(t_T\leq1/3\). From (20), \(h/f\geq7/8\),
and \(F(t_T)\geq9/4\),

\[
 F(t_M)>\frac67F(t_T)\geq\frac{27}{14}
 >F\left(\frac25\right)=\frac{1891}{1000}.
\]

Thus \(t_M<2/5\). The exact formula for \(F\) and (20) then give

\[
 \frac{t_M}{t_T}
 <\frac87\frac{1001}{999}\frac{1891}{1875}
 <\frac76.
\]

Therefore

\[
 \frac{X_T}{X_M}
 =\frac{u(t_T)}{u(t_M)}
 <\left(\frac76\right)^2
  \left(\frac{25}{21}\right)^2<2,
\]

contradicting (24). This proves (21).

## 6. Exact level-band width and prefix loss

For \(u=X/\kappa\), the exact derivative is

\[
 \mathcal H_{s,\kappa}'(X)=\frac1{\pi s}
 \left[\arccos(1-y_K)-\arccos(1-y_\mu)\right],    \tag{25}
\]

where

\[
 y_K=s^2(1+u),\qquad
 y_\mu=\frac{s^2u}{1-s^2}.
\]

For \(0\leq y<1\),

\[
 \sqrt{2y}\leq\arccos(1-y)
 \leq\frac{\sqrt{2y}}{\sqrt{1-y/2}}.             \tag{26}
\]

Equations (17), (21), and (25)--(26) imply

\[
 \mathcal H_{s,\kappa}'(X)
 \geq H_\kappa'(X)
 -\frac{\sqrt2}{\pi}\sqrt u
 \left[
 \frac1{\sqrt{1-s^2}\sqrt{1-y_\mu/2}}-1
 \right].                                         \tag{27}
\]

Here \(u<1296\), \(y_\mu<1/50000\), and the square bracket is smaller
than \(1/90000\). Also (21) gives

\[
 H_\kappa'(X)\geq\frac{\sqrt2}{3\pi}>\frac{49}{330}.
\]

Since \(\sqrt2/\pi<1/2\), (27) yields the convenient exact bound

\[
 \boxed{\mathcal H_{s,\kappa}'(X)>\frac7{50}
 \quad(X_M\leq X\leq X_T).}                      \tag{28}
\]

The action changes by exactly \(1/4\) across this band. Hence

\[
 \boxed{X_T-X_M<\frac{25}{14}.}                   \tag{29}
\]

Returning to (23), retaining the positive \(dX_x/2\) is unnecessary.
Equations (23), (29), and \(sm\geq X_x-s\) give

\[
 \boxed{sP> -\frac{25}{56}-\frac s2.}             \tag{30}
\]

## 7. Strict-wall terminal payment and completion of the transfer

At the level \(X_T\), (20)--(21) give

\[
 f<\frac{1001}{1000}\,wF(t_T)
 <\frac{1001}{1000}\,w\frac{61}{27}.
\]

Therefore

\[
 w>\frac{54000}{61061}>\left(\frac{19}{20}\right)^3. \tag{31}
\]

Equations (13) and (31) imply \(W>3/4\). Since \(q\leq\mu\),

\[
 G_K(q)\geq G_K(\mu)=W>\frac34.                   \tag{32}
\]

Thus the first complete ball level \(\tau_1=3/4\) is present strictly;
it is not inserted at a bracket wall.

Let \(\theta_1\in(0,\pi/2)\) be its exact ball angle. The exact-angle
terminal reserve is

\[
 D_A(q)\geq
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\int_q^\mu G_\mu(z)\,dz,                    \tag{33}
\]

where

\[
 Q=\left[A(q)+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<.
\]

Monotonicity gives \(B\geq Q\). Each retained angle satisfies
\(\pi/(2\theta_k)>1\). Consequently all levels after the first, and the
integer \(B-Q\), may be discarded favorably in (33), even when another
sample lies on a strict wall:

\[
 D_A(q)\geq\frac\pi{2\theta_1}-1
 -2\int_q^\mu G_\mu(z)\,dz.                       \tag{34}
\]

The cap is smaller than \(4\sqrt2/15<2/5\). Moreover

\[
 \sin\theta-\theta\cos\theta
 \geq\frac{2\theta^3}{3\pi}
 \qquad(0\leq\theta\leq\pi/2)
\]

gives

\[
 s\frac\pi{2\theta_1}
 \geq\left(\frac{\kappa\pi}{9}\right)^{1/3}
 =\left(\frac{\pi^2w}{6\sqrt2}\right)^{1/3}
 >w^{1/3}>\frac{19}{20}.                           \tag{35}
\]

Here \(\pi^2/(6\sqrt2)>1\). Thus

\[
 \boxed{sD_A(q)>\frac{19}{20}-\frac{7s}{5}.}      \tag{36}
\]

Adding (30) and (36), and using \(s\leq10^{-4}\), gives

\[
 s\mathcal S>
 \frac{19}{20}-\frac{25}{56}-\frac{19}{10^5}
 >\frac12.
\]

This contradicts the standing assumption \(\mathcal S<0\), and therefore
proves the no-negative conclusion of Theorem 1.1. The proof is wall-safe
for three separate reasons:

1. the shelf uses ordinary floors exactly as in the definition of \(p\);
2. the first ball level is forced by the strict inequality (32);
3. every other strict terminal wall is handled by (33) with the top level
   absent, while the retained net levels and \(B-Q\) remain nonnegative.

## 8. The explicit global finite box

We combine Theorem 1.1 with two already audited automatic sectors.

### 8.1 The range \(\rho\leq99/100\)

The fixed-ratio theorem uses

\[
 K_0(\rho)=
 \frac{a_\rho+2\eta_\rho C_*
 +\sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}}
 {2\eta_\rho^2}.
\]

For \(\rho\leq99/100\), the proved rational bounds are

\[
 \eta_\rho>\frac{49}{165000},\qquad
 a_\rho<623,\qquad C_*<\frac{13}{10},\qquad
 \eta_\rho<\frac13.
\]

The radicand is smaller than \(624^2\), and the complete numerator is
smaller than \(2\cdot624\). Therefore

\[
 K_0(\rho)<
 \frac{624}{(49/165000)^2}
 =\frac{16\,988\,400\,000\,000}{2401}
 <7.1\times10^9.                                  \tag{37}
\]

The strengthened fixed-ratio proof controls the reduced scalar
\(\mathcal S\), not merely a separate tail term. Therefore a negative
candidate with \(\rho\leq99/100\) satisfies (37).

### 8.2 The range \(\rho>99/100\)

Here \(0<\epsilon<1/100\). The thin high-energy theorem proves the
scalar whenever

\[
 K\epsilon^2\geq\frac{125}{8}.
\]

By Theorem 1.1 a negative candidate has
\(\epsilon=s^2>10^{-8}\). Therefore it must satisfy

\[
 K<\frac{125}{8\epsilon^2}
 <\frac{125}{8\cdot10^{-16}}
 =156\,250\,000\,000\,000\,000.                  \tag{38}
\]

The bound in (38) is larger than (37), so it is a global cutoff. Put

\[
 K_*=156\,250\,000\,000\,000\,000,
\]

\[
 N_*=156\,249\,999\,999\,999\,999,\qquad
 F_*=52\,083\,333\,333\,333\,333.               \tag{39}
\]

### Theorem 8.1 (explicit residual ranges)

If a high-floor first-drop scalar is negative, then

\[
 \boxed{
 \frac1{312\,500\,000\,000\,000\,000}<\rho
 <\frac{99\,999\,999}{100\,000\,000},\qquad
 \frac{21}{4}<K<K_* .}                            \tag{40}
\]

Its discrete data lie in the exact finite ranges

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad \frac12\leq r<K_*,\\
 2\leq n\leq N_*,\qquad 1\leq p\leq n-1,\\
 2\leq f\leq F_*,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq F_*.
 \end{gathered}}                                   \tag{41}
\]

The continuous variables additionally satisfy the exact chamber
constraints

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,\qquad
 K-\mu>\frac{7\pi}{4},                             \tag{42}
\]

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14,                               \tag{43}
\]

and the strict definitions of \(Q,B\) in (33).

To justify (40)--(41), negativity rules out \(p=0\), so \(p\geq1\),
\(n\geq2\), and \(r<\mu<K\). Hence \(\rho>1/(2K_*)\). Theorem 1.1
gives the strict upper bound for \(\rho\). Also

\[
 A(r)\geq\frac74,\qquad A(0)=\frac{K-\mu}{\pi}>A(r),
\]

which gives the lower bounds in (40) and (42). Since \(\pi>3\),

\[
 f\leq A(r)+\frac14<\frac K3+\frac14,\qquad
 B<G_K(0)+\frac14<\frac K3+\frac14.
\]

Taking integer parts below \(K_*\) gives \(f,B\leq F_*\). Finally
\(n<\mu<K_*\) gives \(n\leq N_*\), while \(q\geq x+1\) and (43) give
\(Q\leq f-1\).

Thus (40)--(43) are an explicit finite integer-data reduction, not merely
a sequential compactness assertion.

## 9. Reproducibility and exact remaining work

The verifier

scripts/general_d_high_floor_compact_verify.py

checks all numerical comparisons used above. Directed-rounding replays at
512 and 1024 bits both report:

    PASS elasticity pinning: r/sqrt(2r-1) > 23/20
    PASS small-M level localization: F(t_f)<6/5<F(1/3)
    PASS large-M t-parameter bounds: t_f>1/3
    PASS global turning window: t_f>1/72 and X_f/kappa<1296
    PASS exact/critical profile ratio: |R-1|<1/1000
    PASS exact level-band slope: H_s'(X)>7/50
    PASS conditional contradiction: a putative negative candidate
      would have s*S > 1/2 for 0<s<=1/10000
    PASS global cutoff: K < 156250000000000000
    PASS discrete bounds: f,B <= 52083333333333333;
                          n <= 156249999999999999

The remaining task is still substantial: certify the exact scalar on the
compact wall set (40)--(43), or sharpen the analytic estimates until that
wall set disappears. Direct enumeration at the present cutoff is not
feasible. Accordingly, this note claims an explicit finite cutoff and
exact residual ranges, but **does not** claim a compact-wall certificate or
closure of the high-floor branch.
