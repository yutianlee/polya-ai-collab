# Replacement adversarial audit: aggregate low-interface route

Date: 2026-07-15.

## Authentication

The corrected route has SHA-256
`61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0`,
as requested.  Its four declared inputs also authenticate exactly:

| artifact | SHA-256 |
|---|---|
| `SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| `SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

## Verdict

**PASS.  No unsupported implication found.**

The new completeness packet closes the sole proof gap identified in the
first audit.  It proves, with the correct strict endpoint convention and
multiplicity,

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\ell\geq0}(2\ell+1)
   [\gamma_{\rho,K}(\nu_\ell)]_<.
\]

The authenticated phase enclosure in the weighted-lattice packet gives
\(\gamma_{\rho,K}(\nu)<U_{\rho,K}(\nu)\), while
\(U_{\rho,K}(\nu)\leq A_{\rho,K}(\nu)+1/4\).  Monotonicity of the strict
positive-integer count, together with the accepted angular cutoff, therefore
gives exactly

\[
 N_D(A_{\rho,1},K^2)
 \leq\sum_{\nu_\ell<K}2\nu_\ell
 [A_{\rho,K}(\nu_\ell)+\tfrac14]_<
 =\mathcal P_{\rm coarse}.
\]

This remains valid when a phase is an integer: the completeness packet uses
\(n\pi<\Psi(K)\), so that channel contributes one fewer than the ordinary
floor, exactly as required.

## Analytic recheck

The corrected note leaves the aggregate algebra unchanged, and it rechecks
cleanly:

- At \(\tau=0\), the low-tail count is \(R=J\); at \(\tau>0\), it is
  \(R=J+1\).  In both cases \(n_r=J-r\),
  \(\sum n_r=J(J+1)/2\), and every split point is
  \(q_r=\mu-\tau\).
- The common interface loss is
  \(\delta_\tau\leq2\tau^{5/2}/(15\sqrt\mu)\), with exact zero at
  \(\tau=0\).
- Curvature gives
  \(p_r^2+2x_rp_r<C\), hence the strict bound
  \(p_r<P_C(x_r)\).  Since \(P_C''>0\), midpoint
  Hermite--Hadamard has the stated direction
  \(P_C(r+1/2)\leq\int_r^{r+1}P_C\), yielding
  \(\sum p_r<\mathcal I(C,R)\) with the displayed antiderivative.
- If \(S=\sum_{r<R}M_r\) and
  \(U=8R\tau^{5/2}/(15\sqrt\mu)\), then
  \(S>\mathcal Q+U\) and \(4R\delta_\tau\leq U\).  Thus
  \(\mathcal Q\geq0\Rightarrow S>4R\delta_\tau\).  This verifies the
  factors \(4\) from \(-M_r/4\) and \(8=4\cdot2\) from the interface
  estimate.  Summing (10) and multiplying by \(2\) gives the strict
  low-tail aggregate comparison, including \(\tau=0\).
- The accepted high-tail theorem, dimension reduction, and integration by
  parts then give the strict coarse-proxy comparison.  The newly accepted
  count bridge transfers it to \(N_D\), so (13) is now fully authorized.
- The floor-free comparison remains strict:
  \(\lfloor K\eta_\rho\rfloor>K\eta_\rho-1\),
  \(\partial_R\mathcal I=P_C(R)>0\), and
  \[
  J(J+1)-(\mu-\tfrac32)(\mu-\tfrac12)
   =(1-\tau)(2J+\tau)\geq0.
  \]
  Consequently \(\mathcal Q>\mathcal B\), so
  \(\mathcal B\geq0\Rightarrow\mathcal Q>0\Rightarrow\) strict Pólya.

## Diagnostic reproduction (nonproof)

The newly defined value
\(\rho_c=1/(1+2\pi)=0.137302561698\ldots\) makes every diagnostic row
reproducible.  Direct high-precision evaluation of (15) gives:

| \(\rho\) | printed threshold \(K\) | \(\mathcal B(\rho,K-1)\) | \(\mathcal B(\rho,K)\) |
|---:|---:|---:|---:|
| \(\rho_c\) | 63 | -0.5770452493 | 0.2050167402 |
| \(1/5\) | 70 | -0.8026442748 | 0.5276784288 |
| \(3/10\) | 78 | -2.3354404490 | 0.1619074876 |
| \(2/5\) | 84 | -3.6189378753 | 0.5678134703 |
| \(1/2\) | 90 | -2.1700553776 | 4.5393777336 |
| \(3/5\) | 117 | -6.9085332818 | 3.9933381094 |
| \(13/20\) | 132 | -12.4392131998 | 1.4715417555 |
| \(39/50\) | 187 | -6.3533747851 | 22.2771336062 |

Thus all eight corrected integer crossing values are consistent with the
displayed reserve.  Repeating the specified grid calculation with 1,001
equally spaced ratio samples and every integer \(K=200,\ldots,2000\) gives

\[
 \min_{\rm grid}\mathcal B
 =381.4130992366\ldots
\]

at \((\rho,K)=(\rho_c,200)\), consistent with the printed `381.4`.
These computations are diagnostic only; they do not prove persistence,
inter-sample positivity, or the unbounded-frequency tail, exactly as the
note now states.

The proposed global region \(K\geq200\) remains outside this PASS until its
separate outward finite-rectangle certificate and analytic tail proof are
completed.  No patch to the corrected aggregate note is required.
