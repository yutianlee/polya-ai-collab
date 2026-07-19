# Independent audit: first-floor no-drop small-\(s\) theorem

Date: 18 July 2026

Files audited, without modification:

- `human/outbox/general-d-round-09-no-drop-f1-small-s.md`, 11,111 bytes,
  SHA-256
  `F1CEC41FD1A7807406F929E46AC2E5AE691104A9DDFBA04CF9958F0CB283A553`;
- `scripts/general_d_no_drop_f1_small_s_verify.py`, 4,260 bytes,
  SHA-256
  `AF8920ED071BE596E815B749B52904F6BA550FD30104C30D9FF6AC1CCEBB76AD`.

## Verdict

\[
 \boxed{\text{PASS.}}
\]

The analytic small-\(s\) theorem, all three strict endpoint phases, and the
central/outer finite reduction are correct.  I found no missing phase,
reversed inequality, lost factor, invalid monotonicity step, or arithmetic
error.  The frozen Arb ledger passed unchanged at every tested precision
from 128 through 2048 bits.

The exact proved scope is important.  This is a theorem for the ordinary
first-floor no-drop branch

\[
 f=1,\qquad p=n\geq1,
\]

in the universal spectral active region \(\delta=K-\mu>\pi\), under the
standing spectral convention \(r\in\tfrac12\mathbb N\).  It proves the
scalar whenever \(s=\sqrt{\delta/K}\leq1/10\), and it confines every
possible negative active candidate outside that sector to

\[
 1\leq n\leq754,\qquad s>\frac1{10},\qquad
 K<\frac{33000}{7},
\]

with the open, lower-noncorner, and corner walls kept separate.  It does
not certify those residual compact continuous chambers, and it does not
prove the standalone shifted-tail assertion below the active wall.

## 1. Exact head identity and phase coverage

Write \(A(q)=3/4+\varepsilon_q\).  Reversing the order of integration in

\[
 A(r+t)-A(q)=\int_t^n\sigma(r+u)\,du
\]

gives exactly

\[
 R_n=-\frac n2+2n\varepsilon_q
     +2\int_0^n u\sigma(r+u)\,du.
\]

Thus \(\varepsilon_q\geq1/4\) makes \(R_n\geq0\); the completed
one-interface theorem then gives \(\mathcal S_n\geq0\).  Every possibly
negative branch therefore has

\[
 \frac34\leq A(q)<1.
\]

For the strict bracket \([\,\cdot\,]_<\), the three phases in the note are
exhaustive:

1. If \(A(q)>3/4\), then \(Q=1\) and
   \(G_K(q)\geq A(q)>3/4\), so \(B\geq1\).
2. If \(A(q)=3/4\) and \(q<\mu\), then \(Q=0\) but
   \(G_\mu(q)>0\), hence \(G_K(q)>3/4\) and \(B\geq1\).
3. If \(A(q)=3/4\) and \(q=\mu\), then \(G_\mu(q)=0\), so
   \(Q=B=0\).

This also shows why neither equality face may be imported by continuity
from an adjacent phase.  The proof uses the correct strict value in each
case.

With \(X=s(\mu-z)\), \(X_q=s\alpha\), and
\(X_r=X_q+sn\), the change of variables is exact:

\[
 sR_n=2\int_{X_q}^{X_q+sn}
       \bigl(\mathcal H_{s,\kappa}(X)-1\bigr)\,dX.
\]

## 2. Finite-thickness profile comparison

Set

\[
 a=K-\frac us,
 \qquad
 z=\mu-\frac Xs,
 \qquad 0\leq u\leq\kappa.
\]

Using \(K=\kappa/s^3\) and
\(\mu=\kappa(1-s^2)/s^3\), direct factorization gives

\[
 a^2-z^2=
 \frac{(\kappa+X-u)
 [2\kappa-(\kappa+X+u)s^2]}{s^4}.
\]

Substitution in the radius integral proves the noncancelling formula in
the note.  Dividing its integrand by the \(s=0\) integrand gives exactly

\[
 \mathcal R(u,X)=
 \frac{\sqrt{1-a(u,X)s^2}}{1-b(u)s^2},
 \quad
 a(u,X)=\frac{\kappa+X+u}{2\kappa},
 \quad b(u)=\frac u\kappa.
\]

The preliminary lower bound for \(\kappa\) is also valid.  The radius
integrand is increasing in its radius variable, and

\[
 K-q=\delta+\alpha<2\delta.
\]

Consequently its value is smaller than \(2s\), and

\[
 A(q)\leq\frac{2s\delta}{\pi}
       =\frac{2\kappa}{\pi}.
\]

Since \(A(q)\geq3/4\), this gives
\(\kappa\geq3\pi/8>9/8\).

For \(0\leq X\leq3\), \(u\leq\kappa\), and \(s\leq1/10\),

\[
 a(u,X)\leq1+\frac{3}{2\kappa}\leq\frac73.
\]

The denominator in \(\mathcal R\) is at most one, while
\(\sqrt{1-y}\geq1-y\).  Hence

\[
 \mathcal R\geq1-\frac7{300}=\frac{293}{300}.
\]

At the endpoint, the numerator is at most one and
\(1-bs^2\geq1-s^2\), so

\[
 \mathcal R(u,X_q)\leq\frac1{1-s^2}\leq\frac{100}{99}.
\]

Finally,

\[
 H_\kappa'(X)=\frac{\sqrt2}{\pi\sqrt\kappa}
 (\sqrt{\kappa+X}-\sqrt X)
 \leq\frac{\sqrt2}{\pi}<\frac12.
\]

Since \(X_q\leq1/10\), these inequalities yield

\[
 \frac34\leq\frac{100}{99}
 \left(w+\frac1{20}\right),
 \qquad w\geq\frac{277}{400},
\]

exactly as stated.

## 3. Complete negative-head payment

Let \(c=293/300\) and \(y=cw\).  If \(y\geq1\), the exact action is at
least one at \(X=0\), and monotonicity of \(A\) as \(z\) decreases makes
the complete head nonnegative.

If \(y<1\), let \(X_*\) solve \(cH_\kappa(X_*)=1\).  With

\[
 t=\sqrt{1+X/\kappa}-\sqrt{X/\kappa},
\]

one obtains directly

\[
 \frac X\kappa=\frac{(1-t^2)^2}{4t^2},
 \qquad
 \frac{H_\kappa(X)}w=\frac{3/t+t^3}{4}.
\]

At \(X_*\), denoting this coordinate by \(b\),

\[
 y=\frac{4b}{3+b^4},\qquad b\geq\frac{3y}{4}.
\]

The exact rational chain is

\[
 y\geq\frac{81161}{120000}>\frac{27}{40},
 \quad b>\frac{81}{160},
 \quad
 u(b)<\frac{362483521}{671846400}<\frac{27}{50}.
\]

Also \(y<1\) gives \(w<300/293\).  From
\(c_0=2\sqrt2/(3\pi)>49/165\),

\[
 \kappa<\frac{49500}{14357},
 \qquad
 X_*<\frac{26730}{14357}<3.
\]

Thus the finite-thickness comparison applies throughout every possible
negative portion of the physical head.  If \(X_*\) lies beyond the
physical range, the actual negative interval is merely a subset; if it
lies inside, monotonicity makes the exact action nonnegative after
\(X_*\).

The function \(1-cH_\kappa\) is convex, has left height
\(1-y<13/40\), and vanishes at \(X_*\).  Its graph is below the endpoint
chord.  The chord integral contributes a factor \(1/2\), which cancels
the prefactor \(2\) in the exact formula for \(sR_n\).  Therefore there
is no missing factor in

\[
 sR_n>-\frac{26730}{14357}\frac{13}{40}
      =-\frac{34749}{57428}.
\]

## 4. Terminal payment in all three phases

In the open and lower-noncorner phases, \(B\geq1\), so retaining only
the first complete ball level in the exact-angle reserve is legitimate:

\[
 D_A(q)\geq\frac\pi{2\theta_1}-Q
 -2\int_q^\mu G_\mu(z)\,dz.
\]

The identity

\[
 \sin\theta-\theta\cos\theta
 =\int_0^\theta t\sin t\,dt
 \geq\frac{2\theta^3}{3\pi}
\]

and the level equation give

\[
 s\frac\pi{2\theta_1}
 \geq\frac\pi2
 \left(\frac{4w}{3\sqrt2\,\pi}\right)^{1/3}.
\]

Cubing the desired lower bound \(9/10\) reduces it to

\[
 \pi^2w>\frac{2187}{500}\sqrt2.
\]

The rational bounds in the note give

\[
 \pi^2w>\frac{2493}{400},\qquad
 \frac{2187}{500}\sqrt2
 <\frac{216513}{35000},
\]

and their gap is \(3249/70000>0\).  The one-interface cap is strictly
smaller than \(4\sqrt2/15\).  Since \(Q\leq1\), \(s\leq1/10\), and
\(\sqrt2<3/2\),

\[
 sD_A(q)>\frac9{10}-\frac1{10}-\frac1{25}
 =\frac{19}{25}.
\]

This deliberately uses the weaker \(Q\leq1\) bound in both phases; the
actual lower wall has \(Q=0\), so the strict wall is not crossed.

At the corner, \(q=\mu\), \(G_K(q)=3/4\), and the strict terminal count
is zero.  The zero-level triangle gives

\[
 D_A(q)\geq\frac{9\pi}{16\beta},
 \qquad \beta=\arccos(1-s^2)=2\arcsin(s/\sqrt2).
\]

The elementary inequality
\(\arcsin x\leq x/\sqrt{1-x^2}\) yields

\[
 \frac\beta s\leq\sqrt{\frac{400}{199}}<\frac{10}{7}.
\]

Thus

\[
 sD_A(q)>\frac{63\pi}{160}>\frac{189}{160}.
\]

Adding the common head cost gives exactly

\[
 \frac{19}{25}-\frac{34749}{57428}
 =\frac{222407}{1435700}>0
\]

off the corner and

\[
 \frac{189}{160}-\frac{34749}{57428}
 =\frac{1323513}{2297120}>0
\]

at the corner.

## 5. Central finite reduction

For a negative no-drop scalar, the exact identity and shelf curvature
give

\[
 A(q)<1,\qquad A(r)<\frac54.
\]

The three quoted geometric consequences specialize correctly to
\(b=3/4\):

\[
 bn(n+1)<K^2,
 \quad
 K\leq\frac{2\delta^2(\delta+1)}{\pi^2b^2},
 \quad
 \frac\delta\pi<\frac54+\frac r{4n}.
\]

If \(r\leq K/2\), then
\(r\leq K-r=\delta+\alpha+n<\delta+n+1\).  Substitution and rearrangement
give

\[
 \delta<D_n=
 \frac{3/2+1/(4n)}{1/\pi-1/(4n)}.
\]

The denominator is positive.  Moreover \(D_n\) decreases strictly with
\(n\), the function \(U(\delta)\) increases, and
\(bn(n+1)\) increases.  It therefore suffices to disprove the necessary
condition at one value and all later values follow.

Using \(\pi<22/7\) in \(D_n\) and \(\pi>3\) in \(U\) gives the directed
upper bounds

\[
 \overline D_n=
 \frac{3/2+1/(4n)}{7/22-1/(4n)},
 \qquad
 \overline U_n=\frac{32}{81}\overline D_n^2
 (\overline D_n+1).
\]

At \(n=61\), independent exact arithmetic reproduces

\[
 \overline D_{61}=\frac{4037}{843},
 \quad
 \overline U_{61}=\frac{2544997143040}{48525245667},
 \quad
 \frac34\,61\cdot62=\frac{5673}{2},
\]

and \(\overline U_{61}^2<5673/2\).  Hence every negative central
candidate has \(n\leq60\).

## 6. Outer finite reduction and compact cap

For \(r>K/2\), the established outer residual argument gives

\[
 \delta+1>c_1n,
 \qquad
 c_1=\frac{\sqrt{1+(3/4)^2}-1}{2}=\frac18.
\]

When \(n\geq16\), this implies \(\delta>n/16\).  The endpoint action
bound used in the note can be re-derived directly:

\[
 A(q)\geq A(\mu)
 =\frac1\pi\int_\mu^K\sqrt{1-\mu^2/a^2}\,da
 \geq\frac1\pi\int_\mu^K
 \sqrt{\frac{a-\mu}{K}}\,da
 =\frac{2\kappa}{3\pi}.
\]

Since every negative candidate has \(A(q)<1\),
\(\kappa<3\pi/2\).  Therefore

\[
 s=\frac\kappa\delta<\frac{24\pi}{n}
 <\frac{528}{7n}.
\]

At \(n=755\), the final rational quantity is strictly below \(1/10\)
(the exact gap is \(1/10570\)); at \(n=754\) it is still slightly above
\(1/10\).  Thus the stated outer cutoff \(n\leq754\) is sharp for this
particular rational comparison.

Every candidate not already closed has \(s>1/10\).  Combining this with
\(\kappa<3\pi/2\) gives

\[
 K=\frac\kappa{s^3}<1500\pi<\frac{33000}{7}.
\]

Since \(r\in\tfrac12\mathbb N\) and \(r<\mu<K\), the remaining shift and
sample labels are finite.  The action and terminal level indices are also
bounded, but the continuous one-sided chambers still require a separate
certificate.

## 7. Replay, independent controls, and source hygiene

The unmodified verifier was run with python-flint 0.8.0 at

\[
 128,\ 192,\ 256,\ 384,\ 512,\ 768,\ 1024,
 \text{ and }2048\text{ bits}.
\]

Every run reported

```text
PASS: f=1 no-drop small-s constants certified with Arb
noncorner margin=222407/1435700
corner margin=1323513/2297120
central n<=60; outer n<=754; K<33000/7
```

The default 384-bit run and a 512-bit run under `python -O` also passed.
The minimum-precision guard correctly rejected 127 bits with a nonzero
exit status.  A separate standard-library rational reconstruction
reproduced every displayed fraction and the central \(n=61\) comparison.
Dense independent floating diagnostics of the profile ratio, the
\(t\)-coordinate identity, and the central monotonicity found no conflict;
these diagnostics were not used as proof inputs.

Both audited files passed a control-character scan.  The theorem note has
balanced Markdown code fences and balanced `\[...\]` and `\(...\)`
delimiters, contains no tabs or replacement characters, and is UTF-8 with
LF line endings.  The four previously reported control-character defects
are absent from the hashed source above.  The verifier hash embedded in the
theorem note matches the file on disk.

## 8. Scope pins and optional exposition

Two statements should remain explicit whenever this theorem is moved into
the manuscript:

1. The small-\(s\) closure and the finite box are in the universal active
   region \(\delta>\pi\).  The complementary region is removed by the
   spectral no-mode theorem; this note does not prove a stronger standalone
   shifted-tail result there.
2. The project-wide convention \(r\in\tfrac12\mathbb N\) is used, in
   particular in the one-interface cap through
   \(q=r+n\geq3/2\).  The theorem note mentions this convention in the
   finite-reduction conclusion, but restating it with the theorem hypotheses
   would make the result safer to quote in isolation.

These are scope/exposition pins, not mathematical repairs.  Subject to
them, the Round 9 small-\(s\) theorem and its global active finite reduction
are certified.
