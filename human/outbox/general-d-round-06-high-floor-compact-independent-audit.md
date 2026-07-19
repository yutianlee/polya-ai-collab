# Independent audit: Round 6 high-floor compact reduction

Date: 18 July 2026  
Scope: `human/outbox/general-d-round-06-high-floor-compact.md` and
`scripts/general_d_high_floor_compact_verify.py`  
Status: **PASS AFTER QUANTIFIER CORRECTION**.  The revised note proves the
no-negative conclusion for \(s\leq10^{-4}\), and hence the explicit finite
cutoff, without asserting an unconditional half-unit gap.

The source note and verifier were not edited by the auditor.  The author
revised their theorem wording and verifier labels after the first audit;
Section 9 records that correction history.

## 1. File integrity and computational replay

The final audited hashes are

```text
A7D746B4A52FA1BE05067B98396DFD5BD9F099A7BC96B8BAB07FC2F82E128787  human/outbox/general-d-round-06-high-floor-compact.md
A2C39474CE00E2460097AE076B1513BDC9A2E163FC1ED03220E177D4815F85B0  scripts/general_d_high_floor_compact_verify.py
```

Both files contain zero forbidden ASCII control bytes and zero U+FFFD
replacement characters.

Independent directed-rounding replays with `python-flint 0.8.0` exited zero
at both precisions:

```text
GENERAL_D_ARB_PREC=512   PASS (exit 0)
GENERAL_D_ARB_PREC=1024  PASS (exit 0)
```

The script uses exact `fmpq` arithmetic for rational comparisons and Arb
balls for every transcendental sign.  Its numerical comparisons are all in
the claimed direction.  The revised output now labels the final comparison
as a conditional contradiction, which is exactly what its arithmetic
certifies.

## 2. Interface pinning, including an absent (f)-level

Write

\[
 \widehat H(t)=A(\mu-t),\qquad
 V(t)=t(2\mu-t),\qquad h=f-\frac14.
\]

The first-drop wall gives (W=\widehat H(0)<h).  Also

\[
 c_\rho=\frac{\arccos\rho}{\pi}<s,
 \qquad d=1-2c_\rho>1-2s,
\]

because

\[
 \arccos(1-s^2)=2\arcsin(s/\sqrt2)<\pi s.
\]

Under the contradiction hypothesis (\mathcal S<0), the exact prefix
geometry gives

\[
 T>(1+d)M-d.
\]

If (M\leq100), the slope bound gives

\[
 h-W\leq c_\rho M<\frac1{100},
\]

so this case is stronger than the eventual (23/12) pinning.

If (M>100), then

\[
 \frac TM>
 1+(1-2s)\frac{99}{100}
 \geq 1+\frac{4999}{5000}\frac{99}{100}=:r_0.
\]

For (r=T/M>1), (T\leq\mu) implies

\[
 \frac{V(T)}{V(M)}
 \geq\frac{r^2}{2r-1}.
\]

The function (r/\sqrt{2r-1}) is increasing for (r>1), and exact
rational squaring verifies

\[
 \frac{r_0}{\sqrt{2r_0-1}}>\frac{23}{20}.
\]

The shell-increment elasticity therefore yields

\[
 \frac{\widehat H(T)-W}{h-W}>\frac{23}{20}.
\]

The direction at an absent (f)-level is correct.  In that case
(T=\mu) and (\widehat H(T)<f), so

\[
 \frac{f-W}{h-W}
 >\frac{\widehat H(T)-W}{h-W}
 >\frac{23}{20}.
\]

When the level exists the first inequality is equality.  Solving with
(h-W=f-W-1/4>0) gives

\[
 f-W<\frac{23}{12},
 \qquad W>f-\frac{23}{12}\geq\frac1{12}.
\]

Thus the elasticity direction, including the missing-level convention, is
fully justified.

## 3. Existence of the level and the global turning window

For

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 ((\kappa+X)^{3/2}-X^{3/2}),
 \qquad w=H_\kappa(0)=c_0\kappa,
\]

the noncancelling integral at (X=0) gives

\[
 \sqrt{1-s^2}\,w\leq W\leq\frac{w}{1-s^2}.
\]

Since (W>f/24), (c_0\pi=2\sqrt2/3<1), and
(1-s^2>24s) on the stated range,

\[
 A(0)=\frac{w}{c_0\pi s}
 >\frac{(1-s^2)f}{24s}>f.
\]

Hence the (f)-level really exists after the conditional interface
pinning has been obtained.

The exact envelope comparison is also in the correct direction.  With
(X=\kappa u), (y=s^2(1+u)),

\[
 \mathcal E_{a,K}(\mu-X/s)
 =\frac{\sqrt2\kappa}{\pi}\sqrt{1+u}\sqrt{1-y/2},
\]

while

\[
 \frac{H_\kappa(\kappa u)}
 {\sqrt2\kappa\sqrt{1+u}/\pi}
 =\frac23(1+u)
 \left(1-\left(\frac{u}{1+u}\right)^{3/2}\right)\leq1.
\]

The physical range has (0\leq y\leq1).  Combining this with
(A\geq(2/3)\mathcal E_{a,K}) proves

\[
 \mathcal H_{s,\kappa}(X)\geq\frac{2}{3\sqrt2}H_\kappa(X).
\]

At (X_T), this and (f/w<25) imply (F(t_T)<54), where

\[
 F(t)=\frac{3/t+t^3}{4},\qquad
 u(t)=\frac{(1-t^2)^2}{4t^2}.
\]

Since (F(t)\geq3/(4t)), one gets

\[
 t_T>\frac1{72},\qquad u_T<1296.
\]

All constants and strict inequalities in this localization check.

## 4. Exact-to-critical ratio

The exact integrand divided by the critical integrand is

\[
 \mathcal R(v,X)=
 \frac{\sqrt{1-\mathfrak a s^2}}{1-\mathfrak b s^2},
 \quad
 \mathfrak a=\frac{\kappa+X+v}{2\kappa},
 \quad \mathfrak b=\frac v\kappa.
\]

On (0\leq X\leq X_T), one has
(0\leq\mathfrak b\leq1) and (0\leq\mathfrak a<649).  Thus

\[
 \mathcal R\geq\sqrt{1-\mathfrak a s^2}
 \geq1-\mathfrak a s^2>\frac{999}{1000},
\]

and

\[
 \mathcal R\leq\frac1{1-s^2}<\frac{1001}{1000}.
\]

Integration against the positive critical integrand proves the claimed
relative profile enclosure.  There is no cancellation or dependence on
the size of (f).

## 5. Forced (t_T>1/3)

This step is valid under (\mathcal S<0).  Since (D_A(q)\geq0), that
hypothesis forces

\[
 P=R_p+\frac d2m<0.
\]

If the prefix can be negative, (A(x)<f).  The exact profile is increasing
and concave, so (f-\mathcal H) is nonnegative and convex on
([X_x,X_T]), with endpoint heights at most (1/4) and (0).  The chord
bound gives

\[
 sR_p\geq-\frac{X_T-X_x}{4}.
\]

Using (sm=X_x-s\alpha\geq X_x-s) and (X_x\geq X_M), the inequality
(P<0) gives, when (M>100),

\[
 \frac{X_T}{X_M}>
 1+2(1-2s)\frac{99}{100}>\frac52.
\]

Suppose (t_T\leq1/3).  The relative profile enclosure and
(h/f\geq7/8) give

\[
 F(t_M)>\frac67F(t_T)\geq\frac{27}{14}
 >F(2/5)=\frac{1891}{1000},
\]

so (t_M<2/5).  Moreover the exact identity

\[
 \frac{t_M}{t_T}
 =\frac{F(t_T)}{F(t_M)}
   \frac{3+t_M^4}{3+t_T^4}
\]

gives

\[
 \frac{t_M}{t_T}
 <\frac87\frac{1001}{999}\frac{1891}{1875}<\frac76.
\]

Consequently

\[
 \frac{X_T}{X_M}
 =\frac{u(t_T)}{u(t_M)}
 <\left(\frac76\right)^2
  \left(\frac{25}{21}\right)^2<2,
\]

contradicting the preceding (5/2) bound.  The small-(M) calculation

\[
 F(t_T)<\frac{100}{87}\left(\frac{1000}{999}\right)^2
 <\frac65<F(1/3)
\]

is also correct.  Hence (t_T>1/3) follows for a putative negative
candidate.

## 6. Derivative transfer and prefix loss

Differentiating the exact profile gives

\[
 \mathcal H'_{s,\kappa}(X)=\frac1{\pi s}
 [\arccos(1-y_K)-\arccos(1-y_\mu)].
\]

The inequalities

\[
 \sqrt{2y}\leq\arccos(1-y)
 \leq\frac{\sqrt{2y}}{\sqrt{1-y/2}}
\]

produce exactly the loss term displayed in equation (27) of the note.
Here (u<1296) gives (y_\mu<1/50000).  To make one implicit numerical
step explicit, for (0\leq x,z<10^{-3}),

\[
 (1-x)^{-1/2}<1+x,
 \qquad (1-z)^{-1/2}<1+z.
\]

With (x=s^2) and (z=y_\mu/2), this bounds the square bracket by

\[
 s^2+\frac{y_\mu}{2}+\frac{s^2y_\mu}{2}<\frac1{90000}.
\]

Since (\sqrt u<36), (\sqrt2/\pi<1/2), and

\[
 H_\kappa'(X)=\frac{\sqrt2}{\pi}t(X)
 >\frac{\sqrt2}{3\pi}>\frac{49}{330},
\]

the transferred derivative exceeds

\[
 \frac{49}{330}-\frac1{5000}>\frac7{50}.
\]

The level change is exactly (1/4), so

\[
 X_T-X_M<\frac{25}{14}.
\]

Combining this with the prefix chord bound and
(sm\geq X_x-s) correctly gives

\[
 sP> -\frac{25}{56}-\frac s2.
\]

## 7. Strict-wall terminal count

At (X_T), the exact/critical ratio and (t_T>1/3) give

\[
 f<\frac{1001}{1000}wF(t_T)
 <\frac{1001}{1000}w\frac{61}{27}.
\]

Using (f\geq2) yields

\[
 w>\frac{54000}{61061}>\left(\frac{19}{20}\right)^3.
\]

The lower (W/w) comparison then gives (W>3/4).  Since
(G_K(q)\geq W), the strict bracket really retains the first level:
(B\geq1), even at every other terminal wall.

The count algebra is wall-safe.  Put
(a_k=\pi/(2\theta_k)>1).  Because (B\geq Q),

\[
 \sum_{k=1}^B a_k-Q
 =(a_1-1)+\sum_{k=2}^B(a_k-1)+(B-Q)
 \geq a_1-1.
\]

Thus a strict top level may be absent without invalidating

\[
 D_A(q)\geq\frac\pi{2\theta_1}-1-2\delta_\mu(q).
\]

The standard cap estimate gives (2\delta_\mu(q)<4\sqrt2/15<2/5).
Finally,

\[
 \sin\theta-\theta\cos\theta
 \geq\frac{2\theta^3}{3\pi}
\]

at the (3/4)-level implies

\[
 s\frac\pi{2\theta_1}
 \geq\left(\frac{\kappa\pi}{9}\right)^{1/3}
 =\left(\frac{\pi^2w}{6\sqrt2}\right)^{1/3}
 >w^{1/3}>\frac{19}{20}.
\]

Therefore, still under the contradiction hypothesis,

\[
 sD_A(q)>\frac{19}{20}-\frac{7s}{5},
\]

and hence

\[
 s\mathcal S>
 \frac{19}{20}-\frac{25}{56}-\frac{19}{10^5}
 >\frac12.
\]

This contradicts (\mathcal S<0).  The terminal payment and all strict-wall
directions pass the audit.

## 8. Fixed-ratio and thin cutoffs

For (\rho\leq99/100), the previously audited fixed-ratio scalar theorem
applies at (K\geq K_0(\rho)).  The rational bounds

\[
 \eta_\rho>\frac{49}{165000},\quad
 a_\rho<623,\quad C_*<\frac{13}{10},\quad
 \eta_\rho<\frac13
\]

give

\[
 K_0(\rho)
 <\frac{624}{(49/165000)^2}
 =\frac{16988400000000}{2401}<7.1\times10^9.
\]

For (\rho>99/100), the thin high-energy scalar theorem excludes
(K\epsilon^2\geq125/8).  The contradiction proved above excludes every
negative candidate with (s\leq10^{-4}), hence a negative candidate has
(\epsilon>10^{-8}).  It follows that

\[
 K<\frac{125}{8\epsilon^2}
 <156250000000000000=:K_*.
\]

The derived integer bounds are also correct:

\[
 n\leq K_*-1,\qquad
 f,B\leq52083333333333333.
\]

Negativity excludes (p=0), so (p\geq1), (n\geq2), and
(\rho>1/(2K_*)).  The active floor gives
(A(0)>(7/4)), hence (K>7\pi/4>21/4).  The strict upper bound
(\rho<1-10^{-8}), the ranges for (r,p,Q,B), and all chamber-wall
directions in Theorem 8.1 follow.  Thus the explicit finite reduction is
valid.

## 9. Correction history and final disposition

The first audited revision stated unconditionally that every high-floor
first-drop configuration with \(s\leq10^{-4}\) satisfied

\[
 s\mathcal S>\frac12.
\]

That quantifier was too strong.  The interface pinning begins from

\[
 \mathcal S<0
 \Longrightarrow T>(1+d)M-d,
\]

so the later pinning, forced-slope, prefix, and terminal estimates are
conditional on a putative negative candidate.  Their final implication
\(s\mathcal S>1/2\) is a contradiction, not a universal positive gap.

The author corrected all four affected locations:

1. Theorem 1.1 now states the valid no-negative conclusion
   \(\mathcal S\geq0\);
2. Sections 2--7 now begin with the standing contradiction hypothesis
   \(\mathcal S<0\);
3. the final proof sentence explicitly uses the half-unit estimate to
   contradict that hypothesis;
4. both the note's replay ledger and the verifier label the computation as
   a conditional contradiction.

The pre-correction hashes, retained for traceability, were

```text
377EC4C8DC0705DDE7A280CEFD77EA9BB723F2F2FF635F691B563BD300F908F2  note
4D43DD5BD1C8AB2C5C5E0298E4540B5F1BC93629D3D9FCE91C42C5FC38EB8695  verifier
```

No analytic inequality or numerical constant changed.  I re-read the
revised quantifier flow, reran the verifier independently at 512 and 1024
bits, and repeated the control-character scan on the final hashes.

**Final verdict: PASS.**  The revised files rigorously exclude negative
high-floor first-drop scalars for \(s\leq10^{-4}\), preserve every
ordinary-floor and strict-bracket wall, and validly imply the explicit
finite ranges in Theorem 8.1.  They do not claim certification of the
residual compact walls.
