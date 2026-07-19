# Independent audit: Round 5 first-floor global exhaustion

Date: 18 July 2026

Audited file:

- human/outbox/general-d-round-05-first-floor-global-exhaustion.md

## Verdict

\[
 \boxed{\text{PASS after four local expository repairs.}}
\]

The qualitative global-exhaustion theorem is correct. Every negative
ordinary-first-floor, first-drop scalar in the universal active region is
confined to a compact parameter set. The proof controls both possible
turning limits, including the singular ray \(\kappa\to0\), and it treats
the strict terminal wall with the correct lower-semicontinuous reserve.

I found no incorrect formula, missing escaping regime, sign error,
change-of-variables error, or overclaim about analytic wall components.
The four repairs made during this audit only expose arguments which were
already valid:

1. the active condition \(a>\pi\) makes the level one exist;
2. the fixed-ratio and thin-high-energy inputs control the reduced scalar,
   not merely the full tail;
3. the full \(0\leq Y\leq\pi^2\) window is eventually physical on the
   degenerate ray;
4. the topology behind relative compactness is stated explicitly.

The received source had SHA-256

694BCB37698255D0310657BFCCDAAE03F206E412D8C5A5C50D18D43E25F30EC8.

The repaired and audited source has SHA-256

7F5CFCE3F33E15793C56E7CAE268C1B1F7BF31DCA7B3921578FD4C23A8AC80E0.

It contains no unexpected ASCII control bytes.

## 1. Exact setup, \(p=0\), and the active boundary

With \(x=r+p\), \(m=n-p\), and
\(\alpha=\mu-q\in[0,1)\), one has

\[
 \mu-x=m+\alpha.
\]

The first ordinary floor and its first drop give

\[
 A(x)\geq\frac34,\qquad A(x+1)<\frac34.
\]

Since \(x+1\leq q\leq\mu\), monotonicity gives

\[
 W=A(\mu)=G_K(\mu)<\frac34.
\]

Thus the established interface turning bound implies
\(c_0\kappa<3/4\). If \(M\) is the \(3/4\)-level of
\(\mathscr H(t)=A(\mu-t)\), the same two endpoint inequalities give

\[
 M\leq\mu-x<M+1.
\]

The case \(p=0\) is indeed automatic: then \(R_0=0\), while \(p<n\)
gives \(m=n\geq1\), so

\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0
\]

by the completed one-interface theorem and \(d_\rho>0\).

A negative candidate with \(p\geq1\) must have \(A(x)<1\); otherwise
\(A\geq1\) on \([r,x]\) and \(R_p\geq0\). If \(T\) is the level one,
discarding positive shelf area and using
\(0\leq1-\mathscr H\leq1/4\) on the negative band gives

\[
 R_p\geq-\frac{T-(\mu-x)}2.
\]

Together with \(m=\mu-x-\alpha>\mu-x-1\) and
\(M\leq\mu-x\), a negative scalar therefore forces

\[
 T>(1+d_\rho)M-d_\rho.
\]

There is no missing-level case in the theorem's domain. The universal
active condition is

\[
 a=(1-\rho)K>\pi,
\]

and hence \(A(0)=a/\pi>1\). The level \(T\) exists even for a sequence
approaching the active boundary from above. A sequence with bounded
\(a\in[\pi,A_*]\) and \(\rho\uparrow1\) is covered by the compact-optical
theorem, so the open active boundary creates no noncompact residual.

## 2. The imported exhaustion results control the scalar

This point is essential because positivity of the full tail
\(D_A(r)\) would not by itself exclude negativity of its lower
certificate \(\mathcal S\).

Put

\[
 \delta_q=\int_q^\mu G_\mu(z)\,dz.
\]

In the fixed-ratio proof use
\(L_K=\lfloor K\eta_\rho\rfloor\), and in the thin-high-energy proof use
\(L_K=\lfloor KG_1(\rho)\rfloor\). The audited convex suffix and
one-interface identity give

\[
 D_A(q)\geq\frac{L_K}{2}-2\delta_q.
\]

The general shelf bound \(R_p\geq-p/2\) then yields

\[
 \mathcal S\geq
 \frac12\bigl(L_K+d_\rho(n-p)-p\bigr)-2\delta_q.
\]

The thresholds in the two source proofs make the parenthesis strictly
larger than \(4\delta_q\). The compact-optical theorem directly proves
\(R_p+d_\rho(n-p)/2>0\), after which \(D_A(q)\geq0\) suffices.
Thus all three automatic sectors really exclude a negative reduced
scalar.

It follows that every escaping negative sequence must satisfy

\[
 \tau=\sqrt{1-\rho}\to0,\qquad
 a\to\infty,\qquad
 \tau\kappa=(1-\rho)a<\frac{125}{8}.
\]

Since \(c_0\kappa<3/4\), \(\kappa\) is bounded and has a subsequential
limit \(\kappa_0\in[0,3/(4c_0)]\). This is the complete escape
classification: the fixed-ratio threshold is uniform away from
\(\rho=1\), the compact-optical result removes bounded \(a\), and the
thin-high-energy result removes the complementary large value of
\((1-\rho)a\).

## 3. Exact profile and uniformity

The exact radius-average identity is

\[
 A(z)=\frac1\pi\int_\mu^K\frac{\sqrt{R^2-z^2}}R\,dR.
\]

With

\[
 K=\frac{\kappa}{\tau^3},\qquad
 \mu=\frac{\kappa(1-\tau^2)}{\tau^3},\qquad
 z=\mu-\frac X\tau,\qquad R=K-\frac u\tau,
\]

one has

\[
 R^2-z^2=
 \frac{\bigl(\kappa+X-u\bigr)
       \bigl[2\kappa-(\kappa+X+u)\tau^2\bigr]}{\tau^4},
\]

where juxtaposition denotes multiplication of the two displayed factors,
as in the source formula. Substitution, including
\(dR=-du/\tau\), gives equation (15) exactly, with the correct
orientation, denominator, and no lost power of \(\tau\):

\[
 \mathcal H_{\tau,\kappa}(X)
 =\frac1\pi\int_0^\kappa
 \frac{\sqrt{\bigl(\kappa+X-u\bigr)
       \bigl[2\kappa-(\kappa+X+u)\tau^2\bigr]}}
 {\kappa-u\tau^2}\,du.
\]

At \(\tau=0\) the integral is

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \bigl((\kappa+X)^{3/2}-X^{3/2}\bigr).
\]

After cancellation of the common positive factor, the exact-to-critical
integrand ratio is

\[
 \mathcal R=
 \frac{\sqrt{1-y}}{1-z},\qquad
 y=\frac{\kappa+X+u}{2\kappa}\tau^2,\qquad
 z=\frac u\kappa\tau^2.
\]

On \(0\leq X\leq\pi^2/\kappa\),

\[
 0\leq y\leq\tau^2+\frac{\pi^2}{2a^2},
 \qquad 0\leq z\leq\tau^2.
\]

Both bounds tend uniformly to zero. Since
\(1-y\leq\sqrt{1-y}\leq1\), the positive integrands give the claimed
multiplicative convergence without subtracting two large ball actions.

The lower radius-average bound is also correct:

\[
 A(\mu-t)\geq\frac a\pi\sqrt{\frac t\mu}
 =\frac{\sqrt{\kappa X}}{\pi\sqrt{1-\tau^2}}.
\]

At the exact level one this gives

\[
 X_1\leq\frac{\pi^2(1-\tau^2)}{\kappa}.
\]

Every use of the profile is therefore within the uniform window. In the
nondegenerate case the physical endpoint
\(\tau\mu=(1-\tau^2)a/\tau\) tends to infinity. In the degenerate
\(Y=\kappa X\) scaling the physical endpoint is

\[
 Y_{\rm phys}=\kappa\tau\mu=(1-\tau^2)a^2\to\infty.
\]

Thus the entire interval \(0\leq Y\leq\pi^2\) is eventually physical;
there is no extension of equation (15) beyond \(z=0\).

As a diagnostic check only, direct double-precision evaluation of
\(G_K(z)-G_\mu(z)\) and independent Simpson integration of (15) agreed
within \(3.8\cdot10^{-14}\) and \(2.8\cdot10^{-13}\) at two unrelated
physical parameter points. The proof does not rely on this numerical
check.

## 4. Critical \(f=1\) gap

The imported critical-gap theorem was cross-checked against
general-d-round-05-critical-f1-gap.md and its independent audit.
Its exact ingredients are:

\[
 \mathcal L(w)
 =-2\int_{M_*}^{N_*}(1-H_\kappa)\,dX+\frac{M_*}{2},
 \qquad
 \mathcal Z(w)=\frac\pi{\sqrt2}w^2.
\]

Because \(1-H_\kappa\) is convex with endpoint values \(1/4\) and zero,

\[
 \mathcal L(w)\geq\frac{3M_*-N_*}{4}.
\]

With

\[
 X=\kappa u(t),\quad
 u(t)=\frac{(1-t^2)^2}{4t^2},\quad
 F(t)=\frac{3/t+t^3}{4},
\]

the level parameters \(\xi,\eta\) obey

\[
 w=\frac{3\xi}{3+\xi^4}
  =\frac{4\eta}{3+\eta^4}.
\]

Substitution gives exactly

\[
 \mathcal L+\mathcal Z\geq
 \frac\pi{\sqrt2}
 \left[
 w^2+\frac{3w}{8}\bigl(3u(\xi)-u(\eta)\bigr)
 \right].
\]

The three rational splits in the source note prove the stronger normalized
margin

\[
 \frac18+\frac{85469}{51518208}>\frac18.
\]

At \(w=3/4\), the exact strict wall has \(B=0\) and normalized zero-level
reserve \(9/16\). A sequence approaching the same wall from the
\(B=1\) side has the smaller first-complete-level reserve \(1/2\).
Losing \(1/16\) still leaves the exact rational margin
\(455/4608\). Thus the wall-safe statement used in the exhaustion note
is precisely the independently audited one.

## 5. Nondegenerate limit \(\kappa_0>0\)

Joint continuity of \(H_\kappa(X)\), together with the multiplicative
estimate, gives uniform convergence on a fixed \(X\)-interval. The exact
\(3/4\)- and \(1\)-level coordinates converge to \(M_*,N_*\). This
also holds at \(w=c_0\kappa_0=3/4\), where \(M_*=0\): the limiting
profile has positive right derivative there, so the endpoint is not a
degenerate level.

For

\[
 X_x=\tau(\mu-x),\qquad X_r=\tau(\mu-r),
\]

the exact cell inequalities give

\[
 0\leq X_x-M_j^X<\tau.
\]

The change of variables \(X=\tau(\mu-z)\) has the correct orientation:

\[
 \tau R_p=
 2\int_{X_x}^{X_r}
 \bigl(\mathcal H_{\tau,\kappa}(X)-1\bigr)\,dX.
\]

Extending a short negative interval to \(N_j^X\), or discarding the
nonnegative part beyond \(N_j^X\), can only decrease the right-hand
lower bound. Hence

\[
 \tau R_p\geq
 -2\int_{X_x}^{N_j^X}(1-\mathcal H_{\tau,\kappa})\,dX.
\]

Also

\[
 \tau m=X_x-\tau\alpha\to M_*,\qquad d_\rho\to1.
\]

This proves the exact prefix lower limit \(\mathcal L(w)\), including
the endpoint \(M_*=0\).

The terminal transfer is wall-safe. Since
\(q\geq x+1\),

\[
 Q=[A(q)+1/4]_< =0.
\]

Moreover \(0\leq\mu-q<1\), while the ball slope near the interface is
\(O(\tau)\), so

\[
 G_K(q)-G_K(\mu)\to0.
\]

If \(w<3/4\), then \(B=0\) eventually and the zero-level tangent
triangle gives

\[
 \liminf\tau D_A(q)\geq\frac\pi{\sqrt2}w^2.
\]

If \(w=3/4\), a \(B=0\) subsequence gives
\(9\pi/(16\sqrt2)\). On a \(B=1\) subsequence, the first exact-angle
level satisfies

\[
 \frac K\pi(\sin\theta_1-\theta_1\cos\theta_1)=\frac34.
\]

Using \(K=\kappa/\tau^3\),
\(\sin\theta-\theta\cos\theta=\theta^3/3+O(\theta^5)\), and
\(c_0\kappa_0=3/4\), one obtains

\[
 \frac{\theta_1}{\tau}\to\sqrt2,\qquad
 \frac{\pi\tau}{2\theta_1}\to\frac\pi{2\sqrt2}.
\]

The \(Q\)-term is zero and the one-cell inner cap is bounded, so both
vanish after multiplication by \(\tau\). The minimum of the two
one-sided terminal limits is exactly the wall-safe value used in the
critical-gap lemma. Therefore

\[
 \liminf\tau\mathcal S>\frac\pi{8\sqrt2},
\]

contradicting negativity.

## 6. Degenerate ray \(\kappa_0=0\)

With \(Y=\kappa X\),

\[
 \widehat H_\kappa(Y)
 =\frac{c_0}{\kappa^2}
 \bigl((Y+\kappa^2)^{3/2}-Y^{3/2}\bigr)
 =\frac{3c_0}{2}\int_0^1\sqrt{Y+t\kappa^2}\,dt.
\]

The limiting profile is

\[
 H_0(Y)=\frac{\sqrt2}{\pi}\sqrt Y,
\]

and the uniform additive error on \(0\leq Y\leq\pi^2\) is at most
\(c_0\kappa\). Combining this with the uniform multiplicative shell
error proves exact-profile convergence on the whole physical interval.

Since \(H_0\) is strictly increasing, the exact rescaled levels converge
to

\[
 Y_{3/4}=\frac{9\pi^2}{32},\qquad
 Y_1=\frac{\pi^2}{2}.
\]

The cell uncertainty has \(Y\)-width at most \(\kappa\tau\to0\), so
\(Y_x\to Y_{3/4}\). Multiplying the exact prefix and head by
\(\kappa\tau\) is the correct normalization:

\[
 \kappa\tau R_p
 \geq-2\int_{Y_x}^{Y_{1,j}}
 (1-\widehat{\mathcal H}_{\tau,\kappa})\,dY,
\]

while

\[
 \kappa\tau\frac{d_\rho m}{2}
 =\frac{d_\rho}{2}
 \bigl(Y_x-\kappa\tau\alpha\bigr)
 \longrightarrow\frac{Y_{3/4}}2.
\]

No factor of \(\kappa\), \(\tau\), or two is missing. Direct integration
gives

\[
 \begin{aligned}
 &-2\int_{Y_{3/4}}^{Y_1}
 \left(1-\frac{\sqrt2}{\pi}\sqrt Y\right)\,dY
 \frac{Y_{3/4}}2\\
 &\qquad=\frac{3Y_{3/4}}2-\frac{2Y_1}{3}
 =\frac{27\pi^2}{64}-\frac{\pi^2}{3}
 =\boxed{\frac{17\pi^2}{192}}.
 \end{aligned}
\]

An independent floating-point evaluation gives
\(0.873871223013121\), agreeing with
\((17\pi^2/192)=0.873871223013120\) to rounding error. Since
\(D_A(q)\geq0\), no terminal asymptotic is needed on this ray, and
negativity is again impossible.

## 7. Compactness, discrete data, and scope

The fixed-ratio threshold remains bounded as \(\rho\downarrow0\). On the
two actual shift grids \(r\geq1/2\), and \(r<\mu=\rho K\); therefore
bounded \(K\) prevents \(\rho\downarrow0\). The compact-optical result
and the two critical-limit arguments prevent \(\rho\uparrow1\) for a
negative sequence. The active condition bounds \(K\) away from zero, and
\(r<\mu<K\) bounds \(r\) once \(K\) is bounded. This justifies relative
compactness in the natural \((\rho,K,r)\) shell-parameter space.

On such a compact set:

- \(r\) ranges over finitely many points of the occurring half-grid;
- \(n=\lfloor\mu-r\rfloor\) and \(0\leq p<n\) are bounded;
- the continuous actions are bounded, so the strict brackets \(Q,B\)
  range over finite integer sets.

Thus the theorem correctly claims finite bounds for
\((r,n,p,Q,B)\). It does **not** claim that a compact real-analytic wall
set has finitely many connected components. The final paragraph makes
this distinction explicitly, so there is no illicit promotion from
relative compactness to a finite chamber certificate.

The result is consistent with the other audited branches:

- the no-drop notes concern \(p=n\) and remain a separate finite
  certification problem;
- the large-ray certificate proves a stronger explicit statement on
  \(n-p-1\in\{0,1\}\), but is not needed for this qualitative global
  compactness argument;
- the critical \(f=1\) note supplies exactly the nondegenerate terminal
  gap used here;
- the high-floor exhaustion uses the same audited scalar escape
  trichotomy and strict-wall convention.

The compact residual set is still uncertified. Therefore this PASS does
not close the full shifted-tail theorem or the general-dimensional
Pólya theorem; it validates only the stated global exhaustion of the
ordinary first-floor first-drop branch.

## 8. Cross-checked artifact hashes

- general-d-round-05-critical-f1-gap.md:  
  3CEB21D4C518935448606FAF59371C5DD7E683A31ECDAA8ACDFB3152D9337FA7
- general-d-round-05-critical-f1-gap-independent-audit.md:  
  7CF0F40226CBEBCC2237867144C00EF41FD6BBBEC92AFC58B8C57D0CA974D9F1
- general-d-round-05-high-floor-first-drop.md:  
  50C5B986C98AA07176813673C50B5D5B133418CA8AC99F5B74E452013557B0BE
- general-d-round-05-high-floor-first-drop-independent-audit.md:  
  AE6A8DA9A1011BBF4BD2E638A720C2B9840E5F2D6646859C9E13843CB9C67527
- general-d-round-04-no-drop-exhaustion.md:  
  8363D8EFE29914187D025DD152A424140855BBFC758950236291A685DA9B4BE2
- general-d-round-04-no-drop-exhaustion-independent-audit.md:  
  5F43531FDECAF6669C073AA2453E02166515C8BFDB6EA59EE9A617B88DBCC271
- general-d-round-05-no-drop-finite.md:  
  E0AC849A4280718EB9CB13C912CA10AA3EB34BC5F9A2EE68C2094B9A09E6A9C8
- general-d-round-05-no-drop-finite-independent-audit.md:  
  3208940D7DA40F43C0F80BCDBF8956A1DF159231E4FDC3A9E3F20F7C267F59B3
- general-d-round-04-first-floor-large-ray.md:  
  B5A0560F730FF9DF43885443F857C64D4CF0406601CBCB558F3672B52ED8519B
- general-d-round-04-first-floor-large-ray-independent-audit.md:  
  EA4D96F97F2240667D42DA180F7763799EF263C271009E10E51631FFDBE205F9
