# Round 7 Adversarial Review: Uniform Small-Hole Endpoint

Role: adversarial constants, walls, and route audit
Independence: I reconstructed the argument from the already frozen Round 3
lemma packets and promoted spectral/lattice inputs. I did not read any Round 7
incumbent or clean-room proof.

## Verdict

**PASS.** Define

$$
\omega _0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
$$

and

$$
\boxed{
\rho_*:=\frac{\omega _0}{1+2C_*}
}
=0.0310668242700667014\ldots .
$$

Then the proved inputs imply the actual strict spectral inequality

$$
\boxed{
0<\rho\le\rho_*,\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3 .
}
$$

No Bessel-root certificate, ball-margin certificate, or exceptional
low-angular-order computation is needed in this endpoint sector. The putative
small-hole residual box is empty.

The load-bearing observation is not pointwise convergence to the ball. It is
the exact discrete fact that, when

$$
\mu:=\rho K\le\frac12,
$$

every shifted angular tail begins at or above the inner interface. The
already-proved high-angular shifted-tail theorem then controls every tail at
once. This range overlaps the already-proved small-hole high-energy theorem
at the exact constant $\rho_*$ above.

## 1. Inputs actually used

The argument uses only the following promoted or independently reviewed
inputs.

1. The exact strict spectral identity, with radial levels counted by
   $n\pi<\Psi_{\nu,\rho}(K)$ and angular multiplicity $2\nu=2\ell+1$.
2. The audited annulus phase transfer from the strict phase count to the
   coarse proxy
   $$
   \left\lfloor A_{\rho,K}(\nu)+\frac14\right\rfloor,
   \qquad A_{\rho,K}=G_K-G_{\rho K}.
   $$
3. `SHELL-weighted-lattice-scaffold` and
   `SHELL-high-angular-shifted-tails`: for every $r\ge0$ satisfying
   $r+1/2\ge\rho K$, the corresponding ordinary-floor tail is at most
   $2\int_{r+1/2}^K A_{\rho,K}$.
4. The frozen and independently reviewed small-hole low-interface theorem:
   for
   $$
   0<\rho<\omega_0,
   \qquad
   K(\omega_0-\rho)\ge C_*,
   $$
   every tail beginning strictly below $\rho K$ obeys the same target
   integral estimate.

The Round 3 small-hole packet originally described its conclusion as a
lattice statement because spectral completeness was then a separate gate.
That gate has since been proved. The present conclusion uses the now-proved
strict spectral identity; it does not retroactively treat the old packet
alone as a spectral theorem.

## 2. The complete low-$\mu$ range

Suppose

$$
K\le \frac1{2\rho}.
$$

Then $\mu=\rho K\le1/2$. Every shifted-tail start is

$$
x_r=r+\frac12\ge\frac12\ge\mu.
$$

Thus there are no low-interface tails. On every such tail,
$G_\mu(z)=0$ and hence $A_{\rho,K}(z)=G_K(z)$, including at the equality
$z=\mu$ because $G_\mu(\mu)=0$. The promoted FLPS convex-tail theorem applies
to every $r$. The weighted scaffold therefore gives

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le
\int_0^K2zA_{\rho,K}(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The phase proxy and exact strict spectral identity put the actual shell count
below the left-hand side. This proves the desired result throughout
$K\le1/(2\rho)$, not merely in the exact zero-count region.

This point disposes of the proposed special treatment of $\ell=0,1,2$ in
this range: all half-integer orders, starting with $\nu_0=1/2$, lie on the
already-proved high side of the interface.

## 3. The complete high-$K$ range

For $0<\rho<\omega_0$, put

$$
H(\rho):=\frac{C_*}{\omega_0-\rho}.
$$

If $K\ge H(\rho)$, the frozen small-hole theorem controls every tail with
$r+1/2<\rho K$, while the high-angular theorem controls every tail with
$r+1/2\ge\rho K$. Hence the same weighted-scaffold and strict spectral
argument proves the shell P\'olya bound for all

$$
K\ge H(\rho).
$$

The threshold is inclusive. In the frozen proof the last constant chain is
strict even at $K(\omega_0-\rho)=C_*$ because
$\lfloor x\rfloor>x-1$ and the interface-loss estimate is strict at its
uniform upper bound.

## 4. Exact overlap and equality join

For $0<\rho<\omega_0$, all denominators are positive, and

$$
\begin{aligned}
H(\rho)\le\frac1{2\rho}
&\iff
\frac{C_*}{\omega_0-\rho}\le\frac1{2\rho}\\
&\iff 2\rho C_*\le\omega_0-\rho\\
&\iff \rho\le\frac{\omega_0}{1+2C_*}=\rho_*.
\end{aligned}
$$

Because $1+2C_*>1$, one has $0<\rho_*<\omega_0$, so the high-$K$
theorem is valid at $\rho=\rho_*$. At the endpoint the two thresholds meet
exactly:

$$
\boxed{
H(\rho_*)
=\frac{1+2C_*}{2\omega_0}
=\frac1{2\rho_*}
=:K_*.
}
$$

Numerically,

$$
K_*=16.09433895313711397\ldots .
$$

Equivalently, since

$$
\frac{1+2C_*}{2}=1+\frac{8\sqrt2}{15},
$$

the join is

$$
K_*=\frac{1+8\sqrt2/15}{\omega_0}.
$$

For $\rho<\rho_*$ the two ranges overlap with positive width. For
$\rho=\rho_*$, the low-$\mu$ theorem includes $K=K_*$ and the small-hole
theorem also includes $K=K_*$. There is no open point or half-open seam.

A simpler but slightly weaker publication constant is $\rho_0=3/100$; the
exact $\rho_*$ is the maximal endpoint supplied by these two particular
analytic pieces.

## 5. Strict-wall and endpoint audit

The following possible failures were checked.

### $K=0$ and inactive angular channels

At $K=0$ the spectral count and the Weyl target are both zero. For $K>0$ the
active angular cutoff is the proved strict cutoff $\nu_\ell<K$. Terms at
$\nu_\ell=K$ are not silently included.

### The interface wall $\mu=1/2$

At $K=1/(2\rho)$, the first tail begins at
$x_r=1/2=\mu$. The high-angular theorem has the inclusive hypothesis
$x_r\ge\mu$, and $G_\mu(\mu)=0$. No divergent value of an inner-interface
auxiliary expression is used.

### The high-energy wall $K=H(\rho)$

The small-hole packet assumes a non-strict threshold
$K(\omega_0-\rho)\ge C_*$. Its final compensation remains strict at
equality, so this endpoint is included.

### The parameter wall $\rho=\rho_*$

One has $\rho_*<\omega_0$, not equality. Thus the small-hole theorem remains
inside its open $\rho<\omega_0$ hypothesis, and the exact $K_*$ join covers
the only possible seam.

### Shell eigenfrequencies

The exact count uses $n\pi<\Psi$, so an eigenfrequency at the upper spectral
wall is excluded. The phase enclosure is used only as an upper majorant; it
does not replace the strict count by an ordinary-floor identity.

### Coarse-proxy integer walls

The shifted-tail theorems are statements about the ordinary floors
$\lfloor A+1/4\rfloor$ themselves and include equality
$A+1/4\in\mathbb Z$. Moreover, if the strict phase upper bound lies below an
integer proxy wall, the strict radial count is still no larger than that
ordinary floor. No continuity argument across floor walls is needed.

### Exact zero-count wall

The independent phase estimate gives

$$
(1-\rho)K\le\pi\quad\Longrightarrow\quad N_D=0.
$$

At equality the $\ell=0$ phase is exactly $\pi$, and strict counting excludes
that radial level. This result is correct but is not load-bearing in the new
small-hole covering.

At $\rho=\rho_*$, its upper endpoint is only

$$
\frac{\pi}{1-\rho_*}
=3.242321278991314\ldots,
$$

well below $K_*=16.0943\ldots$. The entire nonzero range between these values
is handled analytically by the high-angular tails.

## 6. The apparent residual box and why it vanishes

If one combined only the exact zero region with the small-hole high-energy
theorem, one would leave

$$
\mathcal R_{\rm naive}
=\left\{(\rho,K):
0<\rho\le\rho_*,\quad
\frac{\pi}{1-\rho}<K<H(\rho)
\right\}.
$$

A crude rectangular enclosure would be

$$
0<\rho\le\rho_* ,
\qquad
\pi<K<K_*.
$$

That is not the minimal certifiable residual. Every point of
$\mathcal R_{\rm naive}$ satisfies $K<1/(2\rho)$ because
$H(\rho)\le1/(2\rho)$. It is therefore already covered by the promoted
high-angular shifted-tail theorem. Consequently

$$
\boxed{\mathcal R_{\rm actual}=\varnothing.}
$$

No small-hole parameter box should be sent to interval Bessel computation.
The subsequent compact-$\rho$ work may begin at $\rho_*$, with an inclusive
analytic overlap there.

## 7. Low angular orders and non-uniform ball convergence

For $\ell=0$ the half-order Bessel functions are elementary, and the shell
phase is exactly

$$
\Psi_{1/2,\rho}(K)=(1-\rho)K.
$$

Thus the radial eigenfrequencies in this channel are

$$
k_{n,0}(\rho)=\frac{n\pi}{1-\rho},
$$

whereas the unit-ball frequencies are $n\pi$. Therefore

$$
k_{n,0}(\rho)-n\pi
=\frac{n\pi\rho}{1-\rho}.
$$

For every fixed $n$ this tends to zero as $\rho\downarrow0$, but the
convergence is not uniform in $n$ or in $K$. Taking $n$ of order $1/\rho$
leaves an order-one frequency displacement, and taking larger $n$ makes the
displacement unbounded. Equivalently, at $K=c/\rho$ the difference of the
normalized ball and shell $\ell=0$ phases is $c/\pi$, independent of $\rho$
(the difference of the unnormalized phases is $c$).

This exact lowest-order calculation is already a counterexample to any step
that upgrades pointwise root convergence to an all-$K$ uniform comparison.
It does not threaten the proof above, which uses the exact interface split
instead of root convergence.

There is likewise no hidden finite list of $\ell=0,1,2$ exceptions:

- if $\mu\le1/2$, every order is on the high side of the interface;
- if $\mu>1/2$, then $K>1/(2\rho)\ge H(\rho)$ for
  $\rho\le\rho_*$, so the reviewed low-interface theorem already controls
  every order below the interface.

## 8. Why ball/domain monotonicity does not pay the volume loss

Let

$$
C_3=\frac{2}{9\pi},
\qquad
N_B(K)=N_D(B_1,K^2).
$$

Domain monotonicity gives

$$
N_D(A_{\rho,1},K^2)\le N_B(K)<C_3K^3.
$$

The required shell target is smaller by

$$
C_3(\rho K)^3=C_3\mu^3.
$$

The strict ball P\'olya theorem only says that the ball deficit

$$
D_B(K):=C_3K^3-N_B(K)
$$

is positive. It supplies no conclusion
$D_B(K)\ge C_3\mu^3$. Hence domain monotonicity plus ball P\'olya does not
imply the shell inequality.

This logical loss is visible numerically without making any shell claim. For
$\rho=0.9$ and $K=\pi+0.01$, the ball has already acquired its first
eigenvalue, while

$$
C_3(1-0.9^3)(\pi+0.01)^3
=0.6000634\ldots<1.
$$

Thus the monotonicity upper bound by the ball count is too large to prove the
shell target. In fact the shell count is zero here by the exact width lemma,
which illustrates the amount of information monotonicity discards.

Dirichlet bracketing gives the stronger comparison

$$
N_D(A_{\rho,1},K^2)
\le N_B(K)-N_B(\rho K).
$$

To finish from this alone one would need

$$
N_B(K)-N_B(\mu)
\le C_3(K^3-\mu^3),
$$

equivalently $D_B(K)\ge D_B(\mu)$. The ball deficit is not monotone: it rises
between spectral walls and drops when the counting function jumps.

There is an explicit failure. Let

$$
\delta=\frac1{100},
\qquad
\mu=\pi-\delta,
\qquad
K=\pi+\delta,
\qquad
\rho=\frac{\mu}{K}.
$$

The interval $(\mu,K)$ crosses the first Dirichlet ball frequency $\pi$, so

$$
N_B(K)-N_B(\mu)\ge1.
$$

But

$$
\begin{aligned}
C_3(K^3-\mu^3)
&=\frac{2}{9\pi}
\left((\pi+\delta)^3-(\pi-\delta)^3\right)\\
&=\frac{4\pi\delta}{3}
+\frac{4\delta^3}{9\pi}\\
&<\frac4{75}+\frac4{27\cdot10^6}<1,
\end{aligned}
$$

where the last line uses the elementary bounds $3<\pi<4$. Thus the failure
is exact; the displayed decimal value $0.0418880\ldots$ is only illustrative.

So the desired ball-difference estimate is false across a spectral wall.
Subtracting two one-sided ball P\'olya inequalities is therefore invalid.

Finally, the fact that a small Dirichlet hole shifts low eigenvalues at a
capacity scale can be favorable, but it is not a quantitative comparison
with the cubic volume loss and cannot replace the tail proof.

## 9. Promotion and certification recommendation

Promote the uniform small-hole endpoint with the exact constant $\rho_*$
only after the usual independent synthesis gate confirms that the cited
Round 3 packets and the now-proved strict spectral identity are the permitted
dependencies. On the mathematical content and all endpoint walls, this audit
finds no unsupported implication.

For certification planning:

- certify no box with $0<\rho\le\rho_*$;
- do not isolate $\ell=0,1,2$ roots in that sector;
- start the compact-$\rho$ residual analysis at the inclusive endpoint
  $\rho=\rho_*$;
- retain the exact strict spectral and floor-wall conventions in the compact
  computation.

This review passes `SHELL-rho-zero-endpoint`. It does not by itself pass the
remaining compact-$\rho$ obligation or the global all-$\rho$ shell theorem.
