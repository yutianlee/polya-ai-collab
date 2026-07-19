# Independent audit: Round 7 high-floor global scalar

Date: 18 July 2026  
Verdict: **PASS**

Audited artifacts:

- `human/outbox/general-d-round-07-high-floor-global-scalar.md`;
- `scripts/general_d_high_floor_global_scalar_verify.py`.

I did not edit either audited artifact or either manuscript. The theorem has
the claimed quantifiers: for every high-floor first-drop configuration

\[
 f=F_0\geq2,\qquad p<n,\qquad \rho>\frac{99}{100},
\]

the reduced scalar

\[
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)
\]

is strictly positive. Consequently every negative high-floor first-drop
candidate has \(\rho\leq99/100\), and the previously audited fixed-ratio
theorem reduces it to

\[
 K<\frac{16\,988\,400\,000\,000}{2401}
  =7\,075\,551\,853.394\ldots<7.1\times10^9.
\]

This is a compact reduction, not a certificate of the remaining
\(\rho\leq99/100\) walls.

## 1. Artifact identity and independent replay

The audited hashes were stable:

```text
BE3264EE26546981E2A662759242A5DF960AF555633C398345A92352729BDBA1  human/outbox/general-d-round-07-high-floor-global-scalar.md
FF1BC66A520A5B01F8E61640A4477BB77A33B6DB2765C8B770113DDA6636BD8F  scripts/general_d_high_floor_global_scalar_verify.py
```

I replayed the checked-in verifier with `GENERAL_D_ARB_PREC=384`, `768`,
and `1024`. All three runs produced the same PASS ledger:

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

The Markdown and verifier each contain zero disallowed control characters,
zero form feeds, zero U+FFFD replacement characters, and zero detected
mojibake fragments.

## 2. Exact geometry and endpoint-chord prefix

Put

\[
 H(t)=A(\mu-t),\quad W=H(0)=G_K(\mu),\quad
 h=f-\frac14,\quad x=r+p,\quad m=n-p.
\]

The inner shell formula makes \(H\) increasing and concave, with

\[
 0\leq H'(t)\leq c,\qquad c=\frac{\arccos\rho}{\pi}.
\]

The first shelf gives \(H(\mu-x)\geq h\), while the first dropped sample
gives \(H(\mu-x-1)<h\). Therefore the unique point \(H(M)=h\) satisfies

\[
 M\leq t_x:=\mu-x<M+1.
\]

Since \(t_x=m+\alpha\), \(0\leq\alpha<1\), one has
\(m=t_x-\alpha>M-1\). The non-strict version used in the note is safe.
The first drop also gives \(W<h\), so
\(\delta:=h-W>0\).

After changing variables from \(z\) to \(t=\mu-z\),

\[
 R_p=2\int_{t_x}^{t_x+p}(H(t)-f)\,dt.
\]

If level \(f\) exists, take \(H(T)=f\) and \(\zeta=0\). If it is absent,
take \(T=\mu\) and

\[
 \zeta=f-H(\mu)\in(0,1/4].
\]

The latter range follows from the shelf and monotonicity of \(H\). The
entire negative part of the integrand is contained in \([M,T]\), hence

\[
 R_p\geq-2\int_M^T(f-H(t))\,dt.
\]

Since \(f-H\) is convex with endpoint values \(1/4\) and \(\zeta\), its
endpoint chord gives

\[
 2\int_M^T(f-H(t))\,dt
 \leq\left(\frac14+\zeta\right)(T-M).
\]

Combining this with \(m>M-1\) proves

\[
 P:=R_p+\frac d2m
 \geq-\left(\frac14+\zeta\right)(T-M)
       +\frac d2(M-1).
\]

The direction and factor of two are correct. Extending the negative
integration interval to \([M,T]\) can only lower the bound.

## 3. Complete audit of the \(\delta\geq1\) sector

For \(\rho>99/100\), directed evaluation at the endpoint gives

\[
 c<\frac1{20},\qquad d=1-2c>\frac9{10},\qquad
 \theta^2<\frac{21}{1000},\quad \theta=\arccos\rho.
\]

The slope bound implies \(M\geq\delta/c>20\).

The elasticity estimate

\[
 \frac{H(t_2)-W}{H(t_1)-W}
 \geq\sqrt{\frac{V(t_2)}{V(t_1)}},qquad
 V(t)=t(2\mu-t),
\]

has the correct direction. If \(r=t_2/t_1\geq1\) and \(t_2\leq\mu\),
direct minimization in \(t_1/\mu\in[0,1/r]\) gives

\[
 \frac{V(t_2)}{V(t_1)}\geq\frac{r^2}{2r-1}.
\]

When \(H(T)=f\), the increment ratio is
\(1+1/(4\delta)\leq5/4\). The function
\(r/\sqrt{2r-1}\) is increasing for \(r\geq1\), and its upper solution at
\(5/4\) is \(r=5/2\). Thus \(T/M\leq5/2\), and

\[
 P\geq\left(\frac d2-\frac38\right)M-\frac d2>1.
\]

When level \(f\) is absent, put
\(a=1/4-\zeta\in[0,1/4]\). Then

\[
 \frac{\mu/M}{\sqrt{2\mu/M-1}}
 \leq1+\frac a\delta\leq1+a.
\]

For \(R\geq1\), the upper solution of
\(r/\sqrt{2r-1}=R\) is exactly

\[
 r_*(R)=R^2+R\sqrt{R^2-1}.
\]

It remains to prove

\[
 \left(\frac12-a\right)(r_*(1+a)-1)<\frac{19}{50}.
\]

I independently expanded the stated polynomial majorant. With
\(x=\sqrt a\) and \(y=2x\), the power coefficients of
\(19/50-U(y/2)\), low degree first, are exactly

```text
19/50, -3/8, -1/4, 3/32, 3/32, 3/64, 1/64.
```

Elevation to Bernstein degree 32 gives 33 positive coefficients. The exact
minimum is \(309/396800\), at coefficient 30. Since
\(\sqrt{a(2+a)}\leq3\sqrt a/2\) on the whole interval, this proves the
strict bound and hence

\[
 P>\left(\frac d2-\frac{19}{50}\right)M-\frac d2
  >\frac9{10}>0.
\]

This includes \(a=0\), where \(M=T=\mu\) can occur. Therefore all
\(\delta\geq1\) configurations have \(P>0\), independently of \(B_0\).
In particular the strict wall \(W=3/4\) is owned.

## 4. Scaling monotonicity for \(0<\delta<1\)

Here strict bracketing gives exactly

\[
 B_0=\left[W+\frac14\right]_< =f-1,qquad
 W=f-\frac14-\delta>f-\frac54.
\]

There is no equality ambiguity because \(0<\delta<1\).

At fixed \(\rho\), the increment has scaling form

\[
 E_K(t)=H(t)-W=K E_1(t/K).
\]

Concavity and \(E_1(0)=0\) give
\(E_1(u)-uE_1'(u)\geq0\), so
\(\partial_KE_K(t)\geq0\). Thus the distance needed to reach fixed
increment \(y\) decreases as \(K\), equivalently \(W\), increases. Since
\(y=f-W\) and \(f\geq2\), the smallest possible \(W\) at fixed \(y\) is
\(W=2-y\). The reduction to \(f=2\) is in the correct direction.

For \(y\in(1/4,5/4)\), set

\[
 x=\frac yW=\frac{y}{2-y}\in\left(\frac17,\frac53\right),qquad
 t_0=\frac{3y}{c}.
\]

It is enough to prove \(E_K(t_0)>y\) at this smallest scale.

## 5. Arccos integral constants and the function \(J\)

With \(\epsilon=1-\rho\),
\(\Phi(\theta)=\sin\theta-\theta\cos\theta\), and
\(W=K\Phi(\theta)/\pi\), direct substitution gives

\[
 u_0=\frac{t_0}{\mu}
 =\frac{3y\Phi(\theta)}{\theta\rho W}.
\]

The elementary bounds have the stated strict directions:

\[
 \frac{499}{1000}\theta^2<\epsilon\leq\frac12\theta^2,qquad
 \frac{9979}{30000}\theta^3<\Phi(\theta)<\frac13\theta^3.
\]

They imply

\[
 u_0<\frac9{250}<1,qquad
 \frac{u_0}{\epsilon}>\frac{199}{100}x.
\]

Thus \(t_0<\mu\). The exact formula

\[
 E_K(t_0)=\frac\mu\pi\int_0^{u_0}
 \left[\arccos(\rho(1-u))-\arccos(1-u)\right]du
\]

has the correct normalization. Applying

\[
 \sqrt{2z}\leq\arccos(1-z)
 \leq\frac{\sqrt{2z}}{\sqrt{1-z/2}}
\]

uses the lower estimate on the first arccos and the upper estimate on the
subtracted one, preserving a lower bound. Since \(u<9/250\), the second
square-root factor is less than \(101/100\). After
\(u=\epsilon v\), the coefficient obeys

\[
 \frac{\rho W\sqrt2\,\epsilon^{3/2}}{\Phi(\theta)}
 >3\frac{99}{100}\sqrt2
   \left(\frac{499}{1000}\right)^{3/2}W
 >\frac{147}{100}W.
\]

The actual upper limit exceeds \(V=(199/100)x\). On \([0,V]\), including
the worst endpoint \(V=(199/100)(5/3)\),

\[
 \sqrt{1+\frac{99}{100}v}-\frac{101}{100}\sqrt v>0.
\]

Therefore both lowering the coefficient and truncating the retained
integral have the correct direction.

For

\[
 I(V)=\frac{200}{297}\left(\left(1+\frac{99}{100}V\right)^{3/2}-1\right)
 -\frac{101}{150}V^{3/2},
\]

one has

\[
 I''(V)=\frac{99/100}{2\sqrt{1+(99/100)V}}
        -\frac{101/100}{2\sqrt V}<0.
\]

The squared comparison is valid because every factor is positive; after
cross multiplication it has a positive constant and positive linear
coefficient. Hence

\[
 J(x)=\frac{147}{100}I\left(\frac{199}{100}x\right)-x
\]

is concave. A concave function lies above its endpoint chord. My
independent 1024-bit directed evaluation gave

```text
J(1/7) = 0.153164634686074196546466079274...,
J(5/3) = 0.140671731734148315071446542499...,
```

with radii below \(2\times10^{-306}\). Thus
\(J(1/7)>3/20\) and \(J(5/3)>7/50\). It follows that
\(E_K(t_0)>y\), so level \(f\) exists and \(T<3y/c\).

## 6. Prefix and terminal ledgers for \(0<\delta<1\)

Now \(\zeta=0\). The endpoint-chord bound, \(cM\geq\delta\),
\(cT<3(\delta+1/4)\), \(d>9/10\), and \(c<1/20\) give

\[
 cP>-\frac34\left(\delta+\frac14\right)
      +\frac7{10}\delta-\frac1{40}
 >-\frac{21}{80}.
\]

At the terminal start put

\[
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.
\]

Because \(q\leq\mu\), monotonicity of the strict bracket gives
\(B\geq B_0=f-1\). Because the ordinary shelf has already dropped at
\(x+1\leq q\), one has \(Q\leq f-1\), including action walls. For
\(1\leq k\leq f-1\),

\[
 k-\frac14\leq f-\frac54<W=G_K(\mu).
\]

The last inequality is strict exactly because \(\delta<1\). Thus every
retained ball angle satisfies \(\theta_k<\theta=\pi c\); no equality level
is inserted by continuity.

The wall-safe exact-angle reserve gives

\[
 D_A(q)>\frac{f-1}{2c}-(f-1)-\frac25.
\]

The cap factor is correct:

\[
 2\int_q^\mu G_\mu(z)\,dz
 <\frac{4\sqrt2}{15}<\frac25.
\]

All discarded extra ball levels and the fractional-top reserve are
nonnegative. Multiplication by \(c\), followed by minimization over
\(f\geq2\), gives

\[
 cD_A(q)>\frac12-\frac1{20}\frac75=\frac{43}{100}.
\]

Consequently

\[
 c\mathcal S>\frac{43}{100}-\frac{21}{80}
 =\frac{67}{400}>0.
\]

Every terminal count inequality, cap factor, and strict-wall direction
passes.

## 7. Residual cutoff

Round 7 excludes every negative candidate with \(\rho>99/100\), without a
restriction on \(K,f,n,p\). For \(\rho\leq99/100\), the already audited
fixed-ratio **scalar** theorem excludes negativity at
\(K\geq K_0(\rho)\). Its uniform bounds

\[
 \eta_\rho>\frac{49}{165000},\qquad a_\rho<623,qquad
 C_*<\frac{13}{10},\qquad \eta_\rho<\frac13
\]

make the square-root term in \(K_0\) less than 624 and the full numerator
less than \(2\cdot624\). Therefore

\[
 K_0(\rho)<\frac{624}{(49/165000)^2}
 =\frac{16\,988\,400\,000\,000}{2401}<7.1\times10^9.
\]

The imported theorem controls the reduced scalar itself, not merely the
original shifted tail, so this implication has the needed quantifier.

## 8. Final conclusion

No blocker was found. The endpoint-chord lemma, present and absent level
branches, elasticity inversion, Bernstein certificate, scaling reduction,
arccos constants, concavity endpoint argument, terminal strict counts, and
fixed-ratio cutoff all have the claimed directions and quantifiers.

**Final audit verdict: PASS.** Round 7 closes the entire
\(\rho>99/100\) high-floor first-drop sector and reduces every remaining
negative candidate to the stated \(K<7.1\times10^9\) fixed-ratio box. It
does not close that residual box.
