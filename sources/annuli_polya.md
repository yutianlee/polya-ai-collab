# Source Card: Dirichlet Pólya for Annuli

Status: audited on 2026-07-12. The source statements below are verified; only the explicitly identified special-function components transfer directly to $3$D shells.

## Primary source

N. Filonov, M. Levitin, I. Polterovich, and D. A. Sher, “Pólya’s conjecture for Dirichlet eigenvalues of annuli,” *Journal of the London Mathematical Society* **113** (2026), no. 2, e70425.

- DOI and published text: [10.1112/jlms.70425](https://doi.org/10.1112/jlms.70425)
- Open preprint: [arXiv:2505.21737v2](https://arxiv.org/abs/2505.21737)
- Version audited: v2, 9 February 2026.
- Reproducibility archive named by the paper: [github.com/michaellevitin/Polya](https://github.com/michaellevitin/Polya)

## Theorem and counting convention

For

$$
A_r=\{x\in\mathbb R^2:r<|x|<1\},\qquad 0<r<1,
$$

the paper defines

$$
N_r(\lambda)=\#\{n:\lambda_n(A_r)\le\lambda^2\}.
$$

Theorem 1.1 proves, for every $r\in(0,1)$ and $\lambda>0$,

$$
N_r(\lambda)<\frac{1-r^2}{4}\lambda^2.
$$

This uses a non-strict spectral count with a strict upper inequality. The present project uses $\#\{\lambda_n<\Lambda\}$, so equality at a phase level must be translated explicitly rather than importing a floor identity verbatim.

## Cross-product spectrum

For integer angular order $m\ge0$, equation (4.1) defines

$$
L_{r,m}(x)=J_m(x)Y_m(rx)-Y_m(x)J_m(rx).
$$

Its positive roots $\ell_{r,m,k}$ give the Dirichlet eigenvalues $\ell_{r,m,k}^2$, with planar angular multiplicity

$$
\kappa_m=\begin{cases}1,&m=0,\\2,&m>0.\end{cases}
$$

With the audited Bessel branch convention,

$$
L_{r,m}(x)=-M_m(x)M_m(rx)
\sin(\theta_m(x)-\theta_m(rx)).
$$

Thus, for

$$
\Theta_{r,m}(x)=\theta_m(x)-\theta_m(rx),
$$

the positive roots satisfy $\Theta_{r,m}(\ell_{r,m,k})=\pi k$.

## Monotonicity and angular cutoff

Lemma 4.1 proves that $\Theta_{r,m}$ is strictly increasing, tends to infinity, and satisfies

$$
\Theta_{r,m}(\lambda)<\pi\qquad(0<\lambda\le m).
$$

The proof uses DLMF 10.18.8 and Nicholson’s integral 10.9.30. Corollary 4.2 gives no contributing positive radial root when $m>\lfloor\lambda\rfloor$.

The derivative proof uses only real order and Nicholson’s formula. The later phase estimates are explicitly stated for real $z\ge0$, so the half-integer substitution required in $3$D is legitimate at the special-function level.

## Global one-sided phase bounds

For $\lambda>0$ and $z\ge0$, define

$$
G_\lambda(z)=
\begin{cases}
\dfrac1\pi\left(\sqrt{\lambda^2-z^2}-z\arccos\dfrac z\lambda\right),&0\le z\le\lambda,\\
0,&z>\lambda,
\end{cases}
$$

$$
H_\mu(z)=\frac{3\mu^2+2z^2}{24\pi(\mu^2-z^2)^{3/2}}
\qquad(0\le z<\mu),
$$

$$
F_\mu(z)=
\begin{cases}
\max\{G_\mu(z)-H_\mu(z),-\tfrac14\},&0\le z<\mu,\\
-\tfrac14,&z\ge\mu,
\end{cases}
$$

and, for $0\le z\le\mu<\lambda$,

$$
\Phi_{\lambda,\mu}(z)=G_\lambda(z)-G_\mu(z).
$$

Theorem 5.1 states, for every real $z\ge0$ and $\lambda>0$,

$$
F_\lambda(z)-\frac14
<\frac1\pi\theta_z(\lambda)
<G_\lambda(z)-\frac14.
$$

For $\mu=r\lambda$ and

$$
\gamma_{\lambda,\mu}(z)
=\frac1\pi\bigl(\theta_z(\lambda)-\theta_z(\mu)\bigr),
$$

Lemma 5.2 proves the global upper bound

$$
\gamma_{\lambda,\mu}(z)
<G_\lambda(z)-F_\mu(z),
\qquad 0\le z\le\lambda.
$$

It also gives

$$
\gamma_{\lambda,\mu}(z)<G_\lambda(z)+\frac14,
$$

and, if $z<\mu$,

$$
\gamma_{\lambda,\mu}(z)
<\Phi_{\lambda,\mu}(z)+H_\mu(z).
$$

If $z\le\mu$, equation (5.8) gives the sharper two-sided comparison

$$
\Phi_{\lambda,\mu}(z)
<\gamma_{\lambda,\mu}(z)
<\Phi_{\lambda,\mu}(z)+\frac14.
$$

These statements cross the inner transition $z=\mu$ and are valid for real order. Under

$$
\lambda=k,\qquad \mu=\rho k,\qquad z=\nu=\ell+\frac12,
$$

they apply directly to the $3$D shell phase difference. No independent subtraction or unquantified Airy remainder is needed to obtain these particular one-sided bounds.

## Lattice-counting results

Definition 1.3 introduces a trapezoidal floor sum. The principal reusable unweighted results include:

- Proposition 3.1: the basic integral comparison for nonnegative concave functions;
- Theorem 3.2 and Theorem 1.4: improved bounds for decreasing concave Lipschitz functions, including an explicit negative margin;
- Theorem 3.3: a convex decreasing $\operatorname{Lip}_{1/2}$ bound when the endpoint is integral;
- Theorem 3.4: a sharper convex bound with an additional $\operatorname{Lip}_{1/3}$ subinterval;
- Lemmas 6.1–6.4: monotonicity, convexity/concavity, Lipschitz constants, and integral identities for $G_\lambda$ and $\Phi_{\lambda,\mu}$.

These results count the planar multiplicity pattern through an unweighted/trapezoidal sum. They do **not** directly prove the required $3$D estimate with weight $2\ell+1$.

### Exact estimates used by the shell low-interface split

For integers $a<b$, Definition 1.3 uses

$$
\mathbf T(g,a,b)=\frac12\lfloor g(a)\rfloor+
\sum_{m=a+1}^{b-1}\lfloor g(m)\rfloor+
\frac12\lfloor g(b)\rfloor.
$$

Proposition 3.1 states that if $g$ is concave, then

$$
\mathbf T(g,a,b)\le\int_a^b g(z)\,dz.
$$

Theorem 1.4 states that if $g$ is decreasing, concave, and $\operatorname{Lip}_c$ on an integer interval $[\alpha,\beta]$, with $0<c<1$, and if for some integer $p\in[\alpha,\beta)$,

$$
\lfloor g(\alpha)\rfloor=\lfloor g(p)\rfloor
>\lfloor g(p+1)\rfloor,
$$

then

$$
\mathbf T(g,\alpha,\beta)
\le\int_\alpha^\beta g(z)\,dz
-\frac{1-c}{2}(\beta-p).
$$

When no floor drop occurs, Proposition 3.1 supplies the same formula with the formal choice $p=\beta$ and zero improvement; Theorem 1.4 itself should not be cited with $p=\beta$.

Theorem 3.4 states that if $g$ is decreasing, convex, $\operatorname{Lip}_{1/2}$ on $[a,b]$, satisfies $g(b)=0$, and is $\operatorname{Lip}_{1/3}$ on $[t,b]$ for some $t\in[a,b]$, then

$$
\mathbf T\left(g+\frac14,a,b\right)
\le\int_a^b g(z)\,dz-\frac14\lfloor g(t)\rfloor.
$$

For $g(z)=G_K(z)$, the choice $t=K/2$ gives

$$
G_K(K/2)=\omega_0K,\qquad
\omega_0:=\frac{\sqrt3}{2\pi}-\frac16.
$$

Lemma 6.2 gives, for $0<z<\mu$,

$$
G_\mu(z)<\frac\mu3\left(1-\frac z\mu\right)^{3/2}
=\frac{(\mu-z)^{3/2}}{3\sqrt\mu}.
$$

Consequently, for any $q\le\mu$ with $0\le\mu-q<1$ and $q>0$,

$$
0\le\int_q^\mu G_\mu(z)\,dz
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}
\le\frac{2}{15\sqrt\mu}.
$$

The first upper inequality is strict when $q<\mu$; equality occurs in the degenerate case $q=\mu$. This consequence is the correct form for a shell split at a half-integer $q$. Corollary 6.3 in the paper instead starts at $\lfloor\mu\rfloor$ and must not be quoted as though the two split points always coincide.

## Computer-assisted closure

Theorem 8.1 bounds the residual analytic gap by

$$
\frac52\le\lambda\le150,
\qquad
0\le\mu\le\frac{22}{25}\lambda.
$$

Computer-assisted Theorem 8.2 verifies the remaining inequality for a larger covering region. Lemma 8.4 propagates a verified positive margin at a rational point to a rectangle or triangle using monotonicity. Section 8 avoids raw floating point by verified rational upper and lower approximations. The reported run used $227$ columns and $8{,}473$ trapezoidal-floor evaluations.

This computation certifies the paper’s planar auxiliary count, not Bessel root intervals and not the $3$D shell count. Its rectangle-covering and rational-approximation design is reusable, but a new certificate is required.

## Transfer audit for three-dimensional shells

Transfers directly:

- the cross-product phase factorization, modulo the sign convention;
- strict monotonicity of the phase difference;
- the no-root cutoff for order above spectral parameter;
- Theorem 5.1 and Lemma 5.2 for real, hence half-integer, order;
- analytic properties of $G$, $F$, $H$, and $\Phi$.

Does not transfer directly:

- planar angular multiplicity $\kappa_m$;
- the unweighted trapezoidal-floor identities;
- the lattice margins in §§3 and 7;
- the finite rational certificate in §8.

## Audit conclusion

The annulus source supplies the previously proposed global shell phase-difference enclosure, including the inner-boundary transition, at real order. The next genuinely new analytic question is whether those bounds yield a sufficiently strong $2\ell+1$-weighted lattice estimate. The project should not continue treating a standalone Airy enclosure as a prerequisite unless the weighted count demonstrates that Lemma 5.2 lacks the required margin.
