# Adversarial Audit: Multiplicity-Weighted Shell Lattice Bound

Role: A4 adversarial reviewer
Obligation: `SHELL-weighted-lattice-fractional`
Verdict: **partial scaffold verified; full obligation remains open**

## Scope

This audit reconstructs the frozen incumbent and clean-room arguments against the two lemma packets, the audited FLPS ball and annulus source cards, the primary FLPS ball theorem, and the weighted diagnostic. No state file was edited.

The two attempts agree on the decisive boundary. I find no earlier promotion-blocking error in the strict count, phase envelope, exact integral, square reduction, multiplicity reduction, high-tail transfer, or thin-width phase proof. The first unsupported implication is the shifted-tail estimate for a tail beginning below the inner interface.

## 1. Strict count and active cutoff

For (x>0),

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}
=\max\{0,\lceil x\rceil-1\}
$$

is correct. In particular,

$$
[m]_< =m-1
$$

at a positive integer (m). Thus an equality with the ordinary floor would be false at a shell eigenfrequency.

With

$$
\gamma_\ell=\frac{\Psi_{\ell+1/2,\rho}(K)}{\pi},
$$

the separated strict count is

$$
N_D(A_{\rho,1},K^2)
=\sum_{\ell\ge0}(2\ell+1)[\gamma_\ell]_<,
$$

conditional on the still-unproved shell completeness/count identity. The audited real-order no-root result gives no contribution when (K\le\nu). Therefore the active condition is strictly

$$
\nu_\ell=\ell+\frac12<K,
$$

and the number of active channels is

$$
m_K=\max\left\{0,\left\lceil K-\frac12\right\rceil\right\}.
$$

This remains correct at (K\in\frac12+\mathbb Z): the order equal to (K) is excluded. The Rayleigh cutoff (\ell(\ell+1)<K^2) is weaker and cannot replace this phase cutoff.

## 2. Optimized phase envelope

Put

$$
\mu=\rho K,
\qquad
A(\nu)=G_K(\nu)-G_\mu(\nu),
$$

with (G_\mu=0) above (\mu). For (0\le\nu<\mu), the audited bounds are

$$
\gamma<G_K-\mathcal F_\mu
=A+(G_\mu-\mathcal F_\mu)
$$

and

$$
\gamma<A+\frac14.
$$

The definition

$$
\mathcal F_\mu=\max\{G_\mu-H_\mu,-\tfrac14\}
$$

gives

$$
G_\mu-\mathcal F_\mu
=\min\{H_\mu,G_\mu+\tfrac14\}.
$$

Since (G_\mu+1/4\ge1/4), taking the better of the two strict upper bounds yields

$$
\gamma<A+\min\{H_\mu,\tfrac14\}.
$$

For (\mu\le\nu\le K), (G_\mu=0) and (\mathcal F_\mu=-1/4), hence

$$
\gamma<A+\frac14.
$$

The packet's optimized slack is therefore correct. At (\nu=\mu), (H_\mu(\mu)) must not be evaluated and the value (1/4) is the correct branch. Because the phase bound is strict, monotonicity of ([\cdot]_<) gives the endpoint-safe inequality

$$
[\gamma]_<\le[A+s_\mu]_<.
$$

The stray control character in the displayed `\frac` in the weighted lemma packet is a typographical defect only; it should be repaired before publication.

## 3. Exact integral and error budget

For

$$
G_a(\nu)=\frac1\pi
\left(\sqrt{a^2-\nu^2}-\nu\arccos\frac\nu a\right),
$$

scaling (\nu=ax) gives

$$
\int_0^a2\nu G_a(\nu)\,d\nu
=\frac{2a^3}{\pi}
\left(
\int_0^1x\sqrt{1-x^2}\,dx
-\int_0^1x^2\arccos x\,dx
\right).
$$

The two integrals are (1/3) and (2/9), so

$$
\int_0^a2\nu G_a(\nu)\,d\nu=\frac{2a^3}{9\pi}.
$$

Consequently,

$$
\int_0^K2\nu A(\nu)\,d\nu
=\frac{2}{9\pi}(K^3-\mu^3)
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The quarter cost is also exact:

$$
\frac14\sum_{\ell=0}^{m_K-1}(2\ell+1)
=\frac{m_K^2}{4}.
$$

Writing (x-[x]_<\in(0,1]), including value (1) at integer walls, reconstructs

$$
\mathcal P_\rho(K)-W_\rho(K)
=E_{\rm mp}+E_{\rm ph}-E_{\rm frac}.
$$

All signs are correct: midpoint error and phase slack are positive-side costs, while strict integerization is the required subtraction. No continuous phase sum can replace this identity.

## 4. Square reduction

The derivative identity

$$
G_a'(z)=-\frac1\pi\arccos\frac za
$$

shows that (A) is strictly decreasing. Below (\mu),

$$
A'(z)=\frac1\pi
\left(\arccos\frac z\mu-\arccos\frac zK\right)<0,
$$

and above (\mu), (A'(z)=-\pi^{-1}\arccos(z/K)<0). The one-sided derivatives agree at (\mu).

Let (R(t)) be the inverse cutoff of (A) and

$$
M(x)=\#\{\ell\ge0:\ell+\tfrac12<x\}
=\max\{0,\lceil x-\tfrac12\rceil\}.
$$

Then, with all inequalities strict,

$$
n<A(\nu_\ell)+\frac14
\iff
\nu_\ell<R(n-\tfrac14).
$$

The sum of the first (M) odd integers is (M^2), and hence

$$
\sum_{\nu_\ell<K}2\nu_\ell[A(\nu_\ell)+\tfrac14]_<
=\sum_{n-1/4<A(0)}M(R(n-\tfrac14))^2.
$$

Layer cake gives

$$
\int_0^K2\nu A(\nu)\,d\nu
=\int_0^{A(0)}R(t)^2\,dt.
$$

This is an exact reformulation, not a proof of the required staircase quadrature sign.

## 5. Multiplicity-to-tail reduction

For every finitely supported sequence (a_\ell),

$$
\sum_{\ell\ge0}(2\ell+1)a_\ell
=\sum_{r\ge0}\left(a_r+2\sum_{\ell>r}a_\ell\right).
$$

Indeed, (a_\ell) occurs once in the (r=\ell) term and (\ell) more times with coefficient two. Using ordinary floors produces a valid majorant of the strict proxy, including at integer walls.

If every shifted tail obeyed

$$
\mathcal T_r
\le2\int_{r+1/2}^K A(z)\,dz,
\tag{T_r}
$$

then summation would give

$$
\sum_\ell(2\ell+1)a_\ell
\le2\int_0^Kf_3(z)A(z)\,dz,
$$

where (f_3(z)=\#\{r:r+1/2\le z\}). Its primitive satisfies

$$
F_3(z)\le\frac{z^2}{2}.
$$

For (z<1/2), this is immediate from (F_3=0); for (z=m+1/2+s), (0\le s<1), direct calculation gives

$$
\frac{z^2}{2}-F_3(z)
=\frac12(s-\tfrac12)^2.
$$

Since (A'\le0) and (A(K)=0), both integration-by-parts inequality directions are correct:

$$
2\int_0^Kf_3A
=-2\int_0^KF_3A'
\le-\int_0^Kz^2A'
=\int_0^K2zA(z)\,dz.
$$

Thus all ((T_r)) together would prove the coarse weighted bound.

## 6. FLPS high-tail applicability

Let (x_0=r+1/2\ge\mu) and (x_0<K). On the whole nontrivial tail,

$$
A(x_0+t)=G_K(x_0+t),
\qquad0\le t\le b:=K-x_0.
$$

This translated function is nonnegative, decreasing, convex, vanishes at (b), and satisfies

$$
|g'(t)|=\frac1\pi\arccos\frac{x_0+t}{K}\le\frac12.
$$

The primary FLPS ball Theorem 5.1 has exactly these hypotheses for arbitrary real (b>0). Its left side is

$$
\left\lfloor g(0)+\frac14\right\rfloor
+2\sum_{j=1}^{\lfloor b\rfloor}
\left\lfloor g(j)+\frac14\right\rfloor,
$$

which is precisely the ordinary-floor shifted tail. If (b) is integral, its endpoint term is (\lfloor1/4\rfloor=0). If (x_0\ge K), both sides of the desired tail inequality are trivially zero.

Therefore

$$
\boxed{(T_r)\text{ is proved whenever }r+\tfrac12\ge\mu.}
$$

The source audit occasionally abbreviates the start as (r\ge\rho K); the mathematically correct condition is (r+1/2\ge\rho K). The frozen attempts use the correct condition.

## 7. Thin-width phase lemma

Nicholson's formula and positivity of (K_0) give, for half-integer (\nu\ge1/2),

$$
M_\nu(x)^2
\ge M_{1/2}(x)^2
=\frac{2}{\pi x}.
$$

Consequently,

$$
0<\theta_\nu'(x)
=\frac{2}{\pi xM_\nu(x)^2}
\le1.
$$

Integration yields

$$
0<\Psi_{\nu,\rho}(K)
\le(1-\rho)K.
$$

Thus ((1-\rho)K\le\pi) implies no positive phase level lies strictly below (\Psi). At equality, (\nu=1/2) has (\theta'_{1/2}=1), so (\Psi=\pi) exactly and strict counting excludes it; for (\nu>1/2), the Nicholson comparison is strict.

This proves the phase-level zero lemma. Promotion of the statement (N_D(A_{\rho,1},K^2)=0) still requires the separated spectral completeness/count identity, which is not among the thin-width packet's listed dependencies.

## First unsupported implication

For a tail beginning at

$$
x_0=r+\frac12<\mu,
$$

the shell action has

$$
A''(z)<0\quad(x_0<z<\mu),
\qquad
A''(z)>0\quad(\mu<z<K).
$$

FLPS Theorem 5.1 requires convexity on the entire interval and therefore cannot be applied. Subtracting two ball upper bounds through a floor is invalid, and splitting at a generally nonintegral (\mu) leaves an unproved interface/fractional margin.

Hence the first unsupported implication is

$$
\boxed{
\mathcal T_r
\le2\int_{r+1/2}^{K}A(z)\,dz
\quad\text{for }r+\tfrac12<\rho K.
}
$$

Neither frozen attempt proves it. The floating diagnostic reports no violation on its finite grid, but this does not close the gap.

## Diagnostic calibration

The diagnostic correctly labels itself non-certified and distinguishes the continuous (G-\mathcal F) surrogate, its integer envelope, the coarse (A+1/4) tail proxy, and a floating phase integral. Its self-test and six focused unit tests pass.

No diagnostic result is promotion evidence:

- `ceil` and endpoint classification operate on floating values;
- the ordinary-floor helper adds a (10^{-12}) tolerance;
- quadrature and closed-form evaluations are not interval-enclosed;
- the minimum reported low-tail margin, about (4.1\times10^{-7}), has no rigorous error budget;
- the grid is finite and ends at (K=100);
- the (G-\mathcal F) integer envelope is not the same object as the optimized envelope, while the tail scan uses the coarse (A+1/4) proxy.

The report does not claim certification, so this is a scope limitation rather than an overclaim.

## Promotion recommendation

The following may be promoted as separate, narrowly stated sublemmas after the usual state patch validation:

1. **`SHELL-weighted-lattice-scaffold` — `proved_internal`:** strict integer operator; optimized phase-envelope derivation; exact Weyl integral and error identity; exact square reduction; multiplicity-to-tail algebra; and the implication “all shifted tails imply the weighted coarse bound.”
2. **`SHELL-high-angular-shifted-tails` — `proved_internal`:** ((T_r)) for every (r+1/2\ge\rho K), with FLPS Theorem 5.1 recorded as the audited external dependency.
3. **`SHELL-thin-width-phase-zero` — `proved_internal`:** (\Psi_{\nu,\rho}(K)\le(1-\rho)K) for half-integer (\nu\ge1/2), and zero strict radial phase count when the width is at most (\pi).

The following must remain open or conditional:

1. **`SHELL-low-interface-shifted-tails` — `open`:** ((T_r)) for (r+1/2<\rho K).
2. **`SHELL-weighted-lattice-fractional` — `open`:** the low tails are missing; diagnostics cannot promote it.
3. **`SHELL-thin-width-zero-count` as a full spectral statement — `derived_under_assumptions`:** promote only after adding and discharging `SHELL-count-floor-identity` / Sturm–Liouville completeness, or weaken its statement to the proved phase-level result.
4. **`SHELL-lattice-count`, `SHELL-fixed-rho-high-energy`, and `TARGET-shell-d3` — remain `open`.**

No shell Pólya theorem is established in Round 3.
