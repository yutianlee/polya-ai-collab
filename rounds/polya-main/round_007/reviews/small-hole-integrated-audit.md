# Round 7 Integrated Audit: Uniform Small-Hole Endpoint

Role: final independent integration audit

Obligation: `SHELL-rho-zero-endpoint`
Verdict: **PASS**

## Bottom line

The four permitted inputs in `state/lemma_packets/SHELL-rho-zero-endpoint.md`
legitimately imply

$$
0<\rho\le\rho_*,\qquad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3,
$$

where

$$
\rho_*
=\frac{\omega_0}{1+2C_*}
=\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}},
\qquad
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15}.
$$

The proof is uniform in all real $K\ge0$, includes $\rho=\rho_*$ and
$\rho K=1/2$, preserves the strict spectral convention and the ordinary
floor proxy, and leaves no small-hole box for finite Bessel certification.
No mathematical correction is required before promotion.

## Dependency legitimacy

The dependency chain is non-circular.

1. The separated shell spectrum and strict phase count are independently
   promoted.  The audited phase transfer gives
   $\gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+1/4$ for $\nu\le\rho K$, while for
   $\rho K<\nu\le K$ one has $G_{\rho K}(\nu)=0$ and the global bound gives
   the same inequality.  Hence
   $$
   \#\{n\ge1:n<\gamma_{\rho,K}(\nu)\}
   \le \left\lfloor A_{\rho,K}(\nu)+\frac14\right\rfloor,
   $$
   including both kinds of integer wall.  Together with the strict active
   cutoff $\nu<K$, this is exactly the supplied bridge $N_D\le S_{\rho,K}$.
2. `SHELL-weighted-lattice-scaffold` and
   `SHELL-high-angular-shifted-tails` were promoted as separate Round 3
   sublemmas.  The fact that the parent weighted-lattice obligation was then
   still open does not weaken these narrower results.  The multiplicity
   identity and the implication from all shifted-tail estimates to the Weyl
   integral are exact.  The high-tail theorem applies for
   $x_r\ge\rho K$, including equality; there $G_{\rho K}(z)=0$ throughout
   the tail, also at $z=\rho K$.
3. The exact narrow low-interface theorem used here is proved in
   `SHELL-low-interface-small-hole.md` and passed its cited adversarial
   audit.  Its proof covers $n=0$, the nonintegral interface cell, the
   endpoint $q=\rho K$, the terminal integer cell, and ordinary-floor walls.
   Its final strict chain is
   $$
   \lfloor\omega_0K\rfloor-n
   >K(\omega_0-\rho)-\frac12
   \ge\frac{8\sqrt2}{15}
   >4\delta,
   $$
   so its non-strict threshold
   $K(\omega_0-\rho)\ge C_*$ is genuinely included.

None of these inputs depends on the present endpoint theorem, pointwise
convergence to the ball, numerical root data, or a finite certificate.

## Exact constant and complete $K$-coverage

Since $\omega_0>0$ and $C_*>0$,

$$
0<\rho_*<\omega_0,
\qquad
1+2C_*=2+\frac{16\sqrt2}{15}.
$$

The defining identity is exactly

$$
(1+2C_*)\rho_*=\omega_0,
\qquad
\frac{\omega_0-\rho_*}{2\rho_*}=C_*.
$$

Thus, for every $0<\rho\le\rho_*$,

$$
\frac{\omega_0-\rho}{2\rho}\ge C_*,
$$

with equality only at $\rho=\rho_*$.  Equivalently,

$$
\frac{C_*}{\omega_0-\rho}\le\frac1{2\rho}
\quad\Longleftrightarrow\quad
\rho\le\rho_*.
$$

Now fix $K>0$ and put $\mu=\rho K$.

- If $\mu\le1/2$, every start satisfies
  $x_r=r+1/2\ge1/2\ge\mu$, so the inclusive high-angular theorem controls
  every tail.
- If $\mu>1/2$, then $K>1/(2\rho)$ and hence
  $$
  K(\omega_0-\rho)
  >\frac{\omega_0-\rho}{2\rho}
  \ge C_*.
  $$
  Starts with $x_r\ge\mu$ are high-angular, and starts with $x_r<\mu$ meet
  every hypothesis of the low-interface theorem.

This dichotomy covers every $K>0$.  At $K=0$, the active proxy sum is empty
and the strict spectral count is zero.  Summing the resulting tail bounds
through the scaffold and then applying the spectral bridge proves the stated
theorem.

At the endpoint the two threshold descriptions meet at

$$
K_*=\frac1{2\rho_*}
=\frac{C_*}{\omega_0-\rho_*}
=16.094338953137113974\ldots,
$$

so there is no half-open seam.

## Strict walls

- At $\mu=1/2$, $x_0=\mu$ is assigned to the inclusive high theorem; there
  are no low starts.
- At $x_r=\mu$, the high theorem is used.  Immediately below $\mu$, the low
  theorem needs only $x_r<\mu$ and no quantitative interface gap.
- At $\rho=\rho_*$ in the branch $\mu>1/2$, the constant comparison is sharp
  before multiplication by $K$, but $K>1/(2\rho_*)$ makes the required
  low-interface threshold strict.
- If $K(\omega_0-\rho)=C_*$, then
  $\mu=C_*\rho/(\omega_0-\rho)\le1/2$; thus this wall is already entirely in
  the high-angular branch.
- At a true phase wall $\gamma=m$, the strict radial count is $m-1$.  At a
  proxy wall $A+1/4=M$, the proxy uses the ordinary floor $M$.  The proof
  never identifies these two counts or replaces either convention by the
  other.
- A half-integer order at $\nu=K$ is excluded by the strict active cutoff;
  its coarse proxy term would in any case be
  $\lfloor0+1/4\rfloor=0$.

## Counterexample and rejection audit

The ancillary rejection claims in the adversarial review are correct and
are not used to fill any proof gap.

1. In the $\ell=0$ channel,
   $k_{n,0}(\rho)=n\pi/(1-\rho)$.  Thus fixed-$n$ convergence to $n\pi$ is
   not uniform in $n$ or in $K$; at $K=c/\rho$ the phase displacement is
   exactly $c$.  This invalidates an all-$K$ inference from pointwise root
   convergence.
2. Domain monotonicity only gives $N_A(K)\le N_B(K)$ and does not pay the
   missing volume $\frac{2}{9\pi}(\rho K)^3$.  The displayed example
   $\rho=0.9$, $K=\pi+0.01$ has ball count at least one while the shell target
   is $0.6000634060\ldots<1$; the shell itself is zero there by the exact
   width lemma.
3. Dirichlet bracketing gives
   $N_A(K)\le N_B(K)-N_B(\rho K)$, but the desired ball-difference bound is
   false.  With $\delta=1/100$, $\mu=\pi-\delta$ and $K=\pi+\delta$, the ball
   difference crosses the first frequency and is at least one, whereas
   $$
   \frac{2}{9\pi}(K^3-\mu^3)
   =\frac{4\pi\delta}{3}+\frac{4\delta^3}{9\pi}
   =0.0418880435\ldots<1.
   $$
   Hence subtracting two one-sided ball P\'olya estimates is indeed invalid.
4. The apparent residual box is empty: for $\rho\le\rho_*$,
   $C_*/(\omega_0-\rho)\le1/(2\rho)$, so every point below the low-interface
   high-energy threshold already has $\mu\le1/2$ and is covered by the
   all-high-tail branch.

Therefore no Bessel-root certificate, exceptional finite list of low angular
orders, or limiting argument at $\rho=0$ remains in
$0<\rho\le\rho_*$.  Certification is still a separate issue for the
intervening compact-$\rho$ region; this PASS makes no claim about that region
or the global shell theorem.

The incumbent's two occurrences of plain `mu` in prose/math formatting and
the adversarial review's isolated label `x_0` where `x_r` is meant are
cosmetic notation defects only; no formula or inference depends on them.
