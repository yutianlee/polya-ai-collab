# Independent audit: quantitative no-drop critical-ray transfer

Date: 18 July 2026

Audited file: `general-d-round-04-critical-ray-transfer.md`

Audited SHA-256:

```text
F9F5B4C48850D5D1A558C4F4CF97911AC6E76010F7D4276527D549085E24598F
```

## Verdict

**PASS.**  Theorem 2.1 and the resulting cutoff (n\geq72\,000) are
rigorous under the stated no-drop cone hypotheses.  The constants, signs,
turning remainders, strict-bracket wall conventions, and final rational
arithmetic all check independently.  No mathematical correction is needed.

The conclusion has exactly the scope claimed: it excludes every residual
no-drop branch with (f=2,3) and (n\geq72\,000), after the automatic
regions from the preceding exhaustion theorem have been removed.  It neither
certifies the remaining finite chambers (n<72\,000) nor treats the
first-drop branch.

The only presentation clarification found in the audit has now been inserted:
before using the chord bound in (28), the note explicitly says that
\(\theta\in(0,\pi/2)\).  Indeed \(G_K(q)\geq7/4\) and \(q\geq0\) imply
\(K/\pi=G_K(0)\geq7/4>3/4\), so the first level is reached before
\(\theta=\pi/2\).  Thus the stated chord inequality is being used on its
correct interval.  This fact was already implicit in the exact-angle lemma
and does not affect the proof.  The hash above is for this presentation-only
post-audit revision.

## 1. Audit of the imported cone

The quantities in Section 1 agree with (25a) of
`general-d-round-04-no-drop-exhaustion.md`:

\[
 c_f=\frac{\sqrt{1+b^2}-1}{2},\quad
 C_K(f)=\left(\frac{f+1/2+c_*}{C_0S_{f-1}}\right)^3,
 \quad
 C_\delta(f)=(8\pi^2f^2C_K(f))^{1/3}.
\]

The preceding proof supplies, for every still-unresolved candidate and
(n\geq\lceil2/c_f\rceil),

\[
 \frac{c_f}{2}n\leq\delta<C_\delta(f)n,
 \qquad
 \frac{c_f^2}{8\pi^2(C_\delta(f)+2)}n^3<K<C_K(f)n^3.
\]

The weak upper sign used in the audited note is safe.  The lower
(delta)-bound follows from (delta+1>c_fn), and the upper bounds come
from the failed root-free cutoff and
(delta^3<8\pi^2f^2K).  Substituting the upper (delta)-bound into the
outer lower bound for (K) gives the displayed lower cubic coefficient.
Thus no hypothesis has been silently strengthened.

The preceding exhaustion theorem already confines an unbounded residual
branch to outer geometry and (f=2,3).  Hence a residual candidate with
(n\geq72\,000) is either covered earlier or satisfies precisely the cone
assumed in Theorem 2.1.

## 2. Endpoint compactness

The radius-average identity

\[
 A(z)=\frac1\pi\int_\mu^K\sqrt{1-z^2/a^2}\,da
\]

is exact.  Since (K-q=\delta+\alpha<2\delta), the upper integrand is
less than (2s).  Conversely,

\[
 \frac{(a-q)(a+q)}{a^2}\geq\frac{a-\mu}{K},
\]

because (a-q\geq a-\mu) and ((a+q)/a^2\geq1/K).  Integration gives

\[
 \frac{2\kappa}{3\pi}\leq A(q)\leq\frac{2\kappa}{\pi}.
\]

Combining this with (b\leq A(q)<b+1),
(7/4\leq b\leq11/4), and (3<\pi<22/7) gives

\[
 \kappa>\frac{21}{8},\qquad
 \kappa<\frac{3\pi}{2}(b+1)<\frac{495}{28}<18.
\]

The weaker closed lower bound in (10) is therefore valid.

At (r), monotonicity in the radius variable gives

\[
 A(r)\geq\frac\delta\pi\sqrt{1-r^2/\mu^2}
 \geq\frac{\sqrt{\kappa N}}{\pi\sqrt{1-s^2}}.
\]

The algebra in the last equality is exact, using
(mu=K(1-s^2)).  Since (A(r)<b+1),

\[
 N<\frac{\pi^2(b+1)^2}{\kappa}
 <\left(\frac{22}{7}\right)^2
   \left(\frac{15}{4}\right)^2\frac8{21}
 =\frac{18150}{343}<53.
\]

For (f=2), the smaller case,

\[
 \frac{c_f}{2}=\frac{\sqrt{65}-4}{16}>\frac14.
\]

Consequently (delta>n/4), and (kappa<18) yields
(s=\kappa/\delta<72/n).  Thus (n\geq72\,000) indeed implies the
strict bound (s<10^{-3}).

## 3. Turning expansion and uniform remainder

The inequalities

\[
 \frac{\theta^3}{3}-\frac{\theta^5}{30}
 \leq \sin\theta-\theta\cos\theta
 \leq\frac{\theta^3}{3}
\]

follow by integrating (u\sin u), and the two arccos bounds used in
(15) are equivalent to
(2\sin(\theta/2)\leq\theta\leq2\tan(\theta/2)).  Keeping the lower
cubic term and the upper quintic term separately gives exactly

\[
 c_0Ry^{3/2}\left(1-
 \frac{y}{5(1-y/2)^{5/2}}\right)
 \leq G_R(R(1-y))
 \leq c_0Ry^{3/2}(1-y/2)^{-3/2}.
\]

For (0\leq y\leq1/100), each displayed relative error is at most (y):
the lower one has coefficient
\([5(1-y/2)^{5/2}]^{-1}<1\), while the derivative of the upper factor is
\(\frac34(1-y/2)^{-5/2}<1\).

The exact scaled radii are

\[
 K=\frac\kappa{s^3},\qquad
 \mu=\frac{\kappa(1-s^2)}{s^3},
\]

so the turning parameters in (17) are correct.  On
(0\leq X\leq54), (kappa\geq21/8) gives

\[
 y_K\leq\left(1+\frac{54}{21/8}\right)s^2<22s^2,
 \qquad
 y_\mu\leq\frac{54}{(21/8)(1-10^{-6})}s^2<22s^2.
\]

The coarse leading bounds in (19) are also safe.  For example, using
(c_0<1/3), (X\leq54), (kappa\leq18), and
(1+X/\kappa<22) gives an outer bound below (120<144), while the inner
term is below (90).

For the outer ball, relative error (22s^2) times the leading bound (144)
is (3168s^2).  For the inner ball, its natural leading term is
((1-s^2)^{-1/2}) times the displayed limiting term.  On the present
range,

\[
 (1-s^2)^{-1/2}<\frac{16}{15},\qquad
 (1-s^2)^{-1/2}-1\leq s^2.
\]

Thus its two errors are at most
(22(16/15)90s^2+90s^2=2202s^2).  The sum is
(5370s^2<5500s^2), proving (20) with room.

## 4. Transfer of the head

Differentiating the limit profile gives (21), and its maximum derivative
is (3c_0/2=\sqrt2/\pi<1/2).  Since
(X_q=s\alpha<s), combining this Lipschitz bound with (20) gives exactly

\[
 \zeta=\frac{s}{2}+5500s^2<\frac3{500}.
\]

The head change of variables (t=s(q-z)) is exact and yields

\[
 sR_n=2\int_0^N
 \bigl(\mathcal H_{s,\kappa}(X_q+t)-f\bigr)\,dt.
\]

Because (N<53), its accumulated error is less than
(2\cdot53\zeta=106\zeta).  Also (A(q)\geq b) gives
(w=H_\kappa(0)\geq b-\zeta), including the ordinary lower wall.

If (w<f), let (m=H_\kappa'(X_f)).  The algebraic parameterization in
the note gives

\[
 m\geq\frac{9c_0w}{8f}.
\]

Concavity gives (H_\kappa'\geq m) on ([0,X_f]), hence
(X_f\leq(f-w)/m).  Therefore

\[
 2\int_0^{X_f}(f-H_\kappa)
 \leq2X_f(f-w)
 \leq\frac{16f(f-w)^2}{9c_0w}.
\]

The integral as a function of its upper endpoint is minimized at (X_f).
Finally (f-w\leq1/4+\zeta) and (w\geq b-\zeta), so (26) follows
with the correct sign.

## 5. Exact-angle reserve and walls

The strict terminal bracket is
(B=[G_K(q)+1/4]_<).  Since (G_K(q)\geq A(q)\geq7/4), one always has
\(B\geq1\), including equality \(G_K(q)=7/4\), where the strict convention
gives \(B=[2]_< =1\).  Thus the level \(\tau=3/4\) is always available.

On ([0,\pi/2]), (sin u\geq2u/\pi) gives

\[
 \frac{\theta^3}{s^3}\leq\frac{9\pi^2}{8\kappa}
 <\frac{30}{7},
\]

and hence \(\theta<\sqrt3s\).  If
(x=(3\pi\tau/K)^{1/3}), the lower Taylor inequality gives

\[
 x^3\geq\theta^3(1-\theta^2/10).
\]

Using \((1-u)^{1/3}\geq1-u\) and
\(\theta^2<3s^2\) proves (29) in the displayed direction.  The identity

\[
 \frac{\pi s}{2x}
 =\frac\pi{2\sqrt2}\left(\frac{w}{3/4}\right)^{1/3}
\]

follows exactly from (w=c_0\kappa).

The exact-angle terminal theorem gives

\[
 D_A(q)\geq
 \frac\pi{2\theta}-Q-2\int_q^\mu G_\mu.
\]

Discarding the other complete levels and the nonnegative fractional-top
term is legitimate.  The no-drop endpoint convention gives
(Q=f-1) at the lower action wall and (Q=f) otherwise, so (Q\leq3)
uniformly.  Together with
(2\int_q^\mu G_\mu<c_*=4\sqrt2/15<2/5), this makes the total finite
subtraction less than ((17/5)s), exactly as in (31).

No wall is lost:

- the ordinary floor supplies (A(q)\geq b) at equality;
- the terminal strict bracket still retains its first complete level;
- at the lower ordinary-floor wall (Q) drops from (f) to (f-1),
  which only improves the estimate;
- the separate identity (D_A(r)=D_A(q)+R_n+1) at that wall supplies the
  favorable unit stated in the note.

## 6. Rational closure and diagnostics

At (zeta\leq3/500),

\[
 \frac{b-\zeta}{3/4}\geq\frac{872}{375}>
 \left(\frac{13}{10}\right)^3,
 \qquad
 c_0>\frac{49}{165}.
\]

The latter follows from (sqrt2>7/5) and (pi<22/7).  Since
(f/(f-1/4-\zeta)) decreases with (f), the maximum of (P_f) over
(f=2,3) is at (f=2).  Exact rational arithmetic gives

\[
 P_f(\zeta)<
 \frac{32(32/125)^2}{9(49/165)(218/125)}
 =\frac{180224}{400575}<\frac9{20}.
\]

The final sum replays exactly as

\[
 \frac{13}{10}\left(1-\frac3{10^7}\right)
 -\frac9{20}-\frac{318}{500}-\frac{17}{5000}
 =\frac{21059961}{100000000}>\frac15.
\]

An independent high-precision substitution also reproduces the optional
diagnostics:

```text
f=2: terminal 1.4732071149, head 0.4231317084, gap 1.0500754065
f=3: terminal 1.7127554417, head 0.4038984489, gap 1.3088569928
s=0.001: full lower margins 0.3869088842 and 0.6476641007
```

These numerical values are not used in the proof.
