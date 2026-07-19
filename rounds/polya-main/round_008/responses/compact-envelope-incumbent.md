# Round 8 Incumbent: Compact-Ratio Analytic Envelope

## Verdict

The remaining all-ratio theorem has a completely explicit bounded analytic
reduction.  In particular,

$$
K_{\mathrm{hi}}=2^{42}
$$

is a valid uniform high-energy threshold on

$$
I_*=[\rho_*,1-2^{-18}].
$$

The useful output is not the resulting giant rectangle.  It is the union of
the three residual families $\mathcal R_L$, $\mathcal R_C$, and
$\mathcal R_T$ frozen in
`state/lemma_packets/SHELL-rho-compact.md`.  This response proves that
analytic reduction.  It does not claim that the residual families have been
certified.

## 1. Small-hole-side envelope

Let

$$
H_0(\rho)=\frac{C_*}{\omega_0-\rho}.
$$

For $\rho\le1/16<\omega_0$, two proved tail theorems apply.

If $K\le1/(2\rho)$, then $\rho K\le1/2$.  Every half-integer tail begins at
$x_r\ge1/2\ge\rho K$, so the high-angular shifted-tail theorem and weighted
scaffold prove the target.  If $K\ge H_0(\rho)$, the small-hole
low-interface theorem supplies all tails below the inner interface, while
the high-angular theorem supplies the rest.

Consequently an uncovered point can only lie in

$$
\frac1{2\rho}<K<H_0(\rho).
\tag{1}
$$

At $\rho=\rho_*$ the two endpoints agree because

$$
\rho_*=\frac{\omega_0}{1+2C_*}
\quad\Longleftrightarrow\quad
\frac1{2\rho_*}=\frac{C_*}{\omega_0-\rho_*}.
\tag{2}
$$

Thus there is no residual at the left endpoint.

The exact rational estimates

$$
\sqrt3>\frac53,
\qquad
\pi<\frac{22}{7}
$$

give

$$
\omega_0-\frac1{16}
>
\frac{35}{132}-\frac16-\frac1{16}
=\frac{19}{528}>0.
\tag{3}
$$

Also $\sqrt2<3/2$ gives $C_*<13/10$.  Since $H_0$ is increasing,

$$
H_0(\rho)
\le H_0(1/16)
<\frac{13}{10}\frac{528}{19}
<64.
\tag{4}
$$

Hence every possible small-hole-side residual has $K<64$.

## 2. Monotonicity of the fixed-ratio threshold

Write $y_0(\rho)=\sqrt{K_0(\rho)}$.  For generic $a,\eta>0$, the expression
in the fixed-ratio theorem is the positive root of

$$
\eta y^2-\sqrt a\,y-C_0=0.
\tag{5}
$$

The denominator in implicit differentiation is

$$
2\eta y-\sqrt a
=\sqrt{a+4\eta C_0}>0.
$$

It follows that

$$
\frac{\partial y}{\partial a}>0,
\qquad
\frac{\partial y}{\partial\eta}<0.
\tag{6}
$$

Now

$$
a_\rho=\frac{2\pi\rho}{1-\rho}
$$

is strictly increasing.  Direct differentiation gives

$$
G_1'(z)=-\frac{\arccos z}{\pi}<0
\qquad(0\le z<1).
\tag{7}
$$

Therefore

$$
\eta_\rho=G_1(\max\{\rho,1/2\})
$$

is nonincreasing, including across its continuous corner at $\rho=1/2$.
Equations (6)--(7) prove that $K_0(\rho)$ is strictly increasing on
$(0,1)$.

## 3. Exact central upper bound

For $\rho=99/100$,

$$
a_\rho=198\pi<792.
\tag{8}
$$

For $0\le v\le1$, the elementary inequality

$$
\arccos(1-v)\ge\sqrt{2v}
$$

follows from $1-\cos t\le t^2/2$.  Hence, with
$\varepsilon=1/100$,

$$
\eta_{99/100}
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}
>\frac1{6000}.
\tag{9}
$$

Here the last strict inequality uses $\sqrt2>1$ and $\pi<4$.  Moreover
$0<\eta<1$ and, from $\sqrt2<3/2$,

$$
C_0<\frac95.
$$

It follows from (8) that

$$
\sqrt a<30,
\qquad
\sqrt{a+4\eta C_0}<\sqrt{800}<30.
\tag{10}
$$

Combining (9)--(10) with the formula for $K_0$ gives

$$
K_0(99/100)
<180000^2
=32{,}400{,}000{,}000
<2^{35}.
\tag{11}
$$

By monotonicity, $K_0(\rho)<2^{35}$ throughout
$[1/16,99/100]$.  The strict count is zero for
$(1-\rho)K\le\pi$, and the fixed-ratio theorem applies at and above
$K_0(\rho)$.  Therefore the central residual can be confined to

$$
\frac{\pi}{1-\rho}<K<K_0(\rho)<2^{35}.
\tag{12}
$$

The inclusive closed envelope in the frozen packet is suitable for interval
boxes and does not create a coverage gap.

## 4. Thin-side envelope

Put $\varepsilon=1-\rho$.  On

$$
2^{-18}\le\varepsilon\le\frac1{100},
$$

the proved product and aggregate-action ranges cover every

$$
0\le K\le L(\varepsilon)
:=\frac1{8\varepsilon^{5/2}},
$$

while the local-plateau theorem covers every

$$
K\ge U(\varepsilon)
:=\frac{64}{\varepsilon^2}.
$$

Thus only $L(\varepsilon)<K<U(\varepsilon)$ can remain.  At the endpoint,

$$
L(2^{-18})
=\frac1{2^3(2^{-18})^{5/2}}
=2^{42}
=\frac{2^6}{(2^{-18})^2}
=U(2^{-18}).
\tag{13}
$$

This agrees with the already-proved complete endpoint theorem.  Since
$U(\varepsilon)$ decreases as $\varepsilon$ increases,

$$
U(\varepsilon)\le2^{42}
\tag{14}
$$

throughout the thin compact zone.

## 5. Uniform conclusion and exact boundary convention

The three zones cover $I_*$ with inclusive overlaps at $\rho=1/16$ and
$\rho=99/100$.  Their respective upper thresholds are less than $64$,
$2^{35}$, and $2^{42}$.  Therefore

$$
\boxed{
\rho\in I_*,\quad K\ge2^{42}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{15}
$$

Every component theorem includes its stated threshold.  The exact strict
spectral convention also makes the zero-count boundary
$(1-\rho)K=\pi$ harmless.  Thus replacing the open residuals (1), (12), and
the thin analogue by their closed envelopes for certification loses no
point and introduces no logical gap.

## 6. What this does and does not solve

This proves finiteness and exact analytic coverage.  It does not make a
naive certificate practical.  In particular, the central and thin ceilings
are too large for raw enumeration of all angular channels.  A successful
certificate must retain phase/lattice aggregation or add sharper analytic
subranges; merely interval-evaluating every Bessel determinant up to
$2^{42}$ is not a viable implementation strategy.

For orientation only, ordinary floating-point evaluation gives

$$
K_0(99/100)\approx6.90\times10^9,
$$

and at $\varepsilon=1/100$ the thin residual is approximately
$12500<K<640000$.  These values are diagnostics and play no role in the
proof.

## Status recommendation

Promote a new analytic-reduction sub-obligation only after independent
reconstruction and adversarial review.  Keep `SHELL-rho-compact` open and
`COMP-certified-bessel` at `diagnostic_only` until the residual certificate
is complete and independently checked.
