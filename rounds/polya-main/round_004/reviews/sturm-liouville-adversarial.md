# Adversarial Review: Separated Shell Spectrum

Role: A4 adversarial reviewer  
Frozen artifact: rounds/polya-main/round_004/responses/sturm-liouville-incumbent.md  
Lemma packet: state/lemma_packets/SHELL-sturm-liouville-completeness.md  
Verdict: **PASS**

## Bottom line

I reconstructed every part of the theorem from the Dirichlet form, rather than assuming completeness from a separation ansatz. I also checked the characteristic determinant against the Wronskian and phase conventions in sources/shell_weyl_bessel.md, sources/bessel_phase_enclosures.md, and sources/annuli_polya.md.

No blocking or correctness finding remains. In particular:

- the substitution \(u=rR\) is genuinely unitary and preserves both Dirichlet traces;
- the radial form identity has exactly the claimed sign and no missing boundary term;
- the global form and operator domains contain the necessary square-summability conditions;
- the growing angular multiplicity does not defeat the compact-resolvent tail estimate;
- the repository determinant has the correct sign and a \(k\)-independent normalization to the left-normalized Sturm--Liouville characteristic function;
- the positive determinant roots are simple even in pure-\(J_\nu\) or pure-\(Y_\nu\) endpoint cases;
- the removable \(k=0\) value is strictly positive, so the limiting phase level zero is not a root;
- strict phase counting uses \(n\ge1\) and excludes a root at \(K\);
- cross-\(\ell\) coincidences must be allowed, and the incumbent's explicit continuity example is valid.

One nonblocking presentational clarification is worth retaining: the incumbent explicitly discusses the case in which both endpoint values of \(J_\nu\) vanish, while the symmetric pure-\(Y_\nu\) case is only implicit in the rank argument. The latter is valid for exactly the same reason and is verified below.

## 1. Hilbert-space decomposition and endpoint traces

For

$$
\Omega=\{(r,\omega):\rho<r<1,\ \omega\in\mathbb S^2\},
$$

Fubini and spherical-harmonic Parseval give

$$
\|f\|_{L^2(\Omega)}^2
=
\sum_{\ell=0}^\infty\sum_{m=-\ell}^{\ell}
\int_\rho^1|R_{\ell m}(r)|^2r^2\,dr.
$$

For each coefficient, multiplication by \(r\),

$$
u_{\ell m}(r)=rR_{\ell m}(r),
$$

is an isometry from \(L^2((\rho,1),r^2dr)\) onto \(L^2(\rho,1)\). Completeness of the spherical harmonics also makes the full coefficient map onto the Hilbert direct sum.

On \([\rho,1]\), both \(r\) and \(1/r\) belong to \(W^{1,\infty}\). Multiplication by either is therefore bounded on \(H^1(\rho,1)\), and their endpoint values are nonzero. Consequently

$$
R(\rho)=R(1)=0
\quad\Longleftrightarrow\quad
u(\rho)=u(1)=0.
$$

Thus multiplication by \(r\) is a bounded isomorphism of \(H_0^1(\rho,1)\), including both endpoint traces. The exclusion \(\rho=0\) is essential here and is respected by the theorem.

## 2. Recalculation of the \(u=rR\) form identity

The radial derivative term is the most likely place for a missing lower-order contribution. Since \(R=u/r\),

$$
R'=\frac{u'}r-\frac{u}{r^2},
$$

and, for complex-valued \(u\),

$$
r^2|R'|^2
=|u'|^2-\frac{(|u|^2)'}r+\frac{|u|^2}{r^2}.
$$

Integration by parts gives

$$
\int_\rho^1r^2|R'|^2\,dr
=
\int_\rho^1|u'|^2\,dr
-\left[\frac{|u|^2}{r}\right]_\rho^1.
$$

Both traces vanish, so the boundary term is exactly zero:

$$
\boxed{
\int_\rho^1r^2|R'|^2\,dr
=\int_\rho^1|u'|^2\,dr.
}
$$

The angular term transforms as

$$
\ell(\ell+1)\int_\rho^1|R|^2\,dr
=
\ell(\ell+1)\int_\rho^1\frac{|u|^2}{r^2}\,dr.
$$

Therefore the block form is precisely

$$
\mathfrak a_\ell[u]
=
\int_\rho^1
\left(
|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2
\right)dr,
\qquad D(\mathfrak a_\ell)=H_0^1(\rho,1).
$$

There is no omitted \(r^{-2}\) term from the radial derivative and no incorrect sign.

## 3. Closure and the exact direct-sum domains

Finite angular truncations are orthogonal both in the \(L^2\) norm and in the displayed form. Closing them in the graph norm gives

$$
D(\mathfrak q)
\simeq
\left\{
(u_{\ell m}):
u_{\ell m}\in H_0^1(\rho,1),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\mathfrak a_\ell[u_{\ell m}]\bigr)<\infty
\right\}.
$$

This is not an unrestricted Cartesian product. Conversely, truncating a sequence satisfying the displayed sum and then approximating its finitely many radial components by compactly supported smooth functions proves density in the form norm. Hence the incumbent has both inclusions, not merely a formal calculation on separated functions.

Because \(\ell(\ell+1)/r^2\) is bounded and continuous on the closed interval,

$$
D(L_\ell)=H^2(\rho,1)\cap H_0^1(\rho,1).
$$

The operator associated with the direct-sum form consequently has the standard domain

$$
\left\{
(u_{\ell m}):
u_{\ell m}\in D(L_\ell),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\|L_\ell u_{\ell m}\|_2^2\bigr)<\infty
\right\}.
$$

The \(\sum\|u_{\ell m}\|^2\) term is redundant once membership in the ambient Hilbert direct sum is understood, but including it is correct. The incumbent does not make the common error of specifying only the block domains.

## 4. Compact-resolvent tail and completeness

For every \(u\in H_0^1(\rho,1)\), \(r\le1\) gives

$$
\mathfrak a_\ell[u]
\ge\ell(\ell+1)\|u\|_2^2.
$$

Thus

$$
\|(L_\ell+1)^{-1}\|
\le\frac1{1+\ell(\ell+1)}.
$$

Let \(P_L\) project onto all sectors with \(\ell\le L\). Each

$$
P_L(H_\Omega+1)^{-1}P_L
$$

is compact because it is a finite sum of compact radial resolvents, each repeated only \(2\ell+1\) times. On the discarded tail,

$$
\left\|
(I-P_L)(H_\Omega+1)^{-1}
\right\|
=
\sup_{\ell>L}\|(L_\ell+1)^{-1}\|
\le
\frac1{1+(L+1)(L+2)}
\longrightarrow0.
$$

The increasing multiplicity does not enter this operator norm. The full resolvent is therefore a norm limit of compact operators. Blockwise compactness alone would have been insufficient, but the incumbent supplies exactly the missing tail estimate.

Regular Dirichlet Sturm--Liouville theory gives a complete orthonormal basis in every block. The Hilbert direct sum of those bases, tensored with the \(2\ell+1\) spherical harmonics, is then a complete orthonormal basis of \(L^2(\Omega)\). Positivity follows from

$$
\mathfrak a_\ell[u]
\ge\int_\rho^1|u'|^2\,dr
\ge\frac{\pi^2}{(1-\rho)^2}\|u\|_2^2.
$$

This verifies all of parts A and B of the packet.

## 5. Determinant equivalence and sign

For \(k>0\) and \(\nu=\ell+\tfrac12\), the transformed equation has basis

$$
\sqrt r\,J_\nu(kr),\qquad \sqrt r\,Y_\nu(kr),
$$

so the original radial factor is

$$
R(r)=r^{-1/2}
\bigl(c_1J_\nu(kr)+c_2Y_\nu(kr)\bigr).
$$

Because the factors \(\rho^{-1/2}\) and \(1^{-1/2}\) are nonzero, the two Dirichlet conditions reduce exactly to

$$
\begin{pmatrix}
J_\nu(\rho k)&Y_\nu(\rho k)\\
J_\nu(k)&Y_\nu(k)
\end{pmatrix}
\begin{pmatrix}c_1\\c_2\end{pmatrix}=0.
$$

Its determinant is

$$
F_{\nu,\rho}(k)
=J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k).
$$

Thus the repository sign is correct. The annulus source uses

$$
J_\nu(k)Y_\nu(\rho k)-Y_\nu(k)J_\nu(\rho k)
=-F_{\nu,\rho}(k),
$$

so its phase factorization carries the opposite global sign. The zero set is unchanged, but the distinction matters when recording a signed factorization.

The Wronskian

$$
J_\nu(z)Y_\nu'(z)-J_\nu'(z)Y_\nu(z)
=\frac{2}{\pi z}
$$

is nonzero at every positive argument. Hence neither row of the boundary matrix is zero. When its determinant vanishes, its rank is exactly one and it has a one-dimensional nonzero nullspace. No spurious determinant root arises from a rank-zero matrix.

## 6. Wronskian normalization and common-zero cases

Define

$$
s_\ell(r,k)
=
\frac{\pi\sqrt\rho}{2}\sqrt r
\left[
J_\nu(\rho k)Y_\nu(kr)
-Y_\nu(\rho k)J_\nu(kr)
\right].
$$

The bracket vanishes at \(r=\rho\). Differentiating in \(r\), the derivative of \(\sqrt r\) therefore contributes zero there, while the Wronskian gives

$$
\partial_rs_\ell(\rho,k)
=
\frac{\pi\sqrt\rho}{2}\sqrt\rho\,k
\frac{2}{\pi\rho k}
=1.
$$

At \(r=1\),

$$
s_\ell(1,k)=\frac{\pi\sqrt\rho}{2}F_{\nu,\rho}(k).
$$

The proportionality factor is positive, independent of \(k\), and never vanishes. This is stronger than merely observing that the determinant and characteristic function have the same zero set.

The common-zero falsification cases behave as follows.

- \(J_\nu(\rho k)=J_\nu(k)=0\) is possible for special \((\rho,k)\). The two \(Y_\nu\)-values are nonzero, the boundary matrix has rank one, and the eigenfunction is the genuine pure-\(J_\nu\) solution.
- \(Y_\nu(\rho k)=Y_\nu(k)=0\) is likewise possible. The two \(J_\nu\)-values are nonzero, and the eigenfunction is the genuine pure-\(Y_\nu\) solution.
- \(J_\nu(z)=Y_\nu(z)=0\) at one positive argument is impossible by the Wronskian.

The normalization and all later simplicity arguments remain valid in both pure-column cases.

## 7. Radial simplicity versus simple determinant roots

Radial eigenspace simplicity follows immediately from ODE uniqueness: a solution satisfying the left Dirichlet condition is determined up to scale by its left derivative.

That statement alone would not exclude a multiple zero if the chosen determinant contained a vanishing prefactor. The incumbent correctly supplies an independent characteristic-function calculation. Differentiating

$$
(L_\ell-k^2)s_\ell=0
$$

with respect to \(k\) gives

$$
(L_\ell-k^2)\partial_ks_\ell=2k\,s_\ell.
$$

For

$$
W(r)
=(\partial_ks_\ell)\partial_rs_\ell
-\partial_r(\partial_ks_\ell)s_\ell,
$$

one obtains

$$
W'(r)=2k\,s_\ell(r,k)^2.
$$

The left-normalized initial data are independent of \(k\), so \(W(\rho)=0\). At a positive eigenfrequency, \(s_\ell(1,k)=0\), and therefore

$$
\partial_ks_\ell(1,k)\,\partial_rs_\ell(1,k)
=2k\int_\rho^1s_\ell(r,k)^2\,dr>0.
$$

The outer derivative cannot vanish together with the outer value, and the identity also directly shows \(\partial_ks_\ell(1,k)\ne0\). Since \(s_\ell(1,k)\) is a fixed nonzero constant times \(F_{\nu,\rho}(k)\), every positive determinant zero is simple. The sign in the incumbent's Lagrange identity is correct.

## 8. Zero energy and the removable determinant value

The energy estimate already rules out a \(k=0\) eigenfunction. The left-normalized zero-energy solution can also be solved explicitly:

$$
s_\ell(r,0)
=
\frac{\rho^{-\ell}r^{\ell+1}
-\rho^{\ell+1}r^{-\ell}}
{2\ell+1}.
$$

It satisfies \(s_\ell(\rho,0)=0\), \(\partial_rs_\ell(\rho,0)=1\), and

$$
s_\ell(1,0)
=
\frac{\rho^{-\ell}-\rho^{\ell+1}}{2\ell+1}>0.
$$

The small-argument formulas

$$
J_\nu(z)\sim\frac{(z/2)^\nu}{\Gamma(\nu+1)},
\qquad
Y_\nu(z)\sim-\frac{\Gamma(\nu)}{\pi}(z/2)^{-\nu}
$$

give

$$
\lim_{k\downarrow0}F_{\nu,\rho}(k)
=
\frac{\rho^{-\nu}-\rho^\nu}{\pi\nu}>0.
$$

The two expressions agree through

$$
s_\ell(1,0)
=\frac{\pi\sqrt\rho}{2}
\lim_{k\downarrow0}F_{\nu,\rho}(k).
$$

Thus the ordinary-Bessel cross-product has a removable, nonzero endpoint value. A rescaled spherical-Bessel determinant may instead diverge at zero, but it still does not vanish; no such rescaling may be used to manufacture a zero eigenfrequency.

## 9. Phase sign, root index, and strict endpoint convention

With the audited branch

$$
J_\nu(x)+iY_\nu(x)=M_\nu(x)e^{i\theta_\nu(x)},
$$

one has \(M_\nu(x)>0\) and

$$
F_{\nu,\rho}(k)
=
M_\nu(\rho k)M_\nu(k)
\sin\bigl(\theta_\nu(k)-\theta_\nu(\rho k)\bigr)
=M_\nu(\rho k)M_\nu(k)\sin\Psi_{\nu,\rho}(k).
$$

This confirms the repository sign. The permitted phase dependency gives

$$
\Psi_{\nu,\rho}(0+)=0,\qquad
\Psi_{\nu,\rho}'(k)>0,\qquad
\Psi_{\nu,\rho}(k)\to\infty.
$$

Although the limiting phase is zero, the modulus product diverges at the compensating rate and the determinant tends to the positive value computed above. Therefore the positive roots are

$$
\Psi_{\nu,\rho}(k_{\ell,n})=n\pi,
\qquad n=1,2,\ldots,
$$

not \(n=0,1,\ldots\).

For \(K>0\),

$$
k_{\ell,n}<K
\quad\Longleftrightarrow\quad
n\pi<\Psi_{\ell+1/2,\rho}(K).
$$

If \(\Psi(K)=m\pi\), strict spectral counting gives \(m-1\), not \(m\). If several angular channels have a root at the same \(K\), the strict inequality excludes the endpoint root in each orthogonal summand. At \(K=0\), the spectral count and the set count are both zero; the incumbent appropriately states the phase equivalence for \(K>0\), avoiding any misuse of a ceiling formula at the limiting endpoint.

## 10. Finiteness and multiplicity

Every radial eigenvalue is simple inside a fixed \(\ell\) block, while the angular eigenspace has dimension \(2\ell+1\). If a numerical eigenvalue occurs in several angular sectors, its full eigenspace is their orthogonal direct sum and

$$
\dim E_\lambda
=
\sum_{\ell:\lambda\in\sigma(L_\ell)}(2\ell+1).
$$

Since

$$
\lambda_{\ell,n}\ge\ell(\ell+1),
$$

no channel with \(\ell(\ell+1)\ge K^2\) contributes to the strict count below \(K^2\). Only finitely many \(\ell\) remain, and each regular radial block has only finitely many eigenvalues below \(K^2\). Hence

$$
N_D(\Omega,K^2)
=
\sum_{\ell=0}^{\infty}(2\ell+1)
\#\{n\ge1:k_{\ell,n}<K\}
$$

is an exact finite sum with the correct total multiplicity.

## 11. Audit of the explicit cross-\(\ell\) degeneracy example

The example compares \(\lambda_{0,2}(\rho)\) and \(\lambda_{7,1}(\rho)\). Since \(L_0\) is the ordinary Dirichlet interval Laplacian,

$$
\lambda_{0,2}(\rho)
=\frac{4\pi^2}{(1-\rho)^2}.
$$

At \(\rho=1/10\), Poincaré and \(56/r^2\ge56\) give

$$
\lambda_{7,1}
\ge\frac{100\pi^2}{81}+56
>
\frac{400\pi^2}{81}
=\lambda_{0,2}.
$$

The strict comparison is equivalent to \(56>100\pi^2/27\), which follows, for example, from \(\pi^2<10\).

At \(\rho=4/5\), use the first Dirichlet sine on the interval of length \(1/5\). Since \(56/r^2\le56/\rho^2=175/2\),

$$
\lambda_{7,1}
\le25\pi^2+\frac{175}{2}
<100\pi^2
=\lambda_{0,2}.
$$

To verify the continuity step, write \(L=1-\rho\), \(r=\rho+Lx\), and map unitarily to \(L^2(0,1)\). The fixed-domain form is

$$
\widetilde{\mathfrak a}_{\ell,\rho}[v]
=
\frac1{L^2}\int_0^1|v'|^2\,dx
+\int_0^1
\frac{\ell(\ell+1)}
{(\rho+Lx)^2}|v|^2\,dx,
\qquad D=H_0^1(0,1).
$$

On \(\rho\in[1/10,4/5]\), both coefficients vary uniformly continuously and remain bounded away from singularity. The min--max eigenvalues are therefore continuous in \(\rho\). The intermediate value theorem supplies a radius with

$$
\lambda_{7,1}(\rho)=\lambda_{0,2}(\rho).
$$

Thus the incumbent does more than avoid assuming cross-channel nondegeneracy: it correctly proves that accidental equality occurs for at least one shell. Different centrifugal potentials only order eigenvalues with the same radial index; they do not forbid coincidences across different radial indices.

## Final verdict

**PASS.** All four theorem parts in the packet are proved with the required domains, compactness mechanism, determinant normalization, zero-energy exclusion, root simplicity, multiplicity, and strict endpoint convention. The explicit cross-\(\ell\) continuity example is also valid.

The promotion must remain structural: this result completes the exact separated-spectrum and strict-count bridge, but proves no finite-window Pólya inequality, no \(\rho\)-uniform theorem, and no numerical certificate.
