# Adversarial review of the current-hash retained-remainder closure

## Verdict

**PASS.**  I assumed that the all-frequency retained-remainder closure was
false and reconstructed the implication chain from the strict Bessel-phase
proxy through the exact residual containment.  I found no unsupported
implication, lost wall, sign reversal, or hidden executable/interval premise.

This verdict is only for the current source hashes listed below.  It is an
internal validity verdict for the retained-remainder closure, not a literature,
novelty, or publication-readiness claim.

## Audited source identities

| source | lines | SHA-256 |
|---|---:|---|
| `manuscript/spherical-shell-polya-proof.tex` | 3660 | `aec5573938b7194a961c192afe5d5fd9a110bf28630f9ba397e25a296d947e73` |
| `manuscript/analytic/compact-structural.tex` | 535 | `1055ba25a6e7f97f2f49ef250ef7589c45d0251b8af50a5e0ff59b36c6bf722c` |
| `manuscript/analytic/compact-angular-block.tex` | 476 | `382df2f006d432902bd68582c3305e5006d701c3d24703e16760e8dca7fb12ce` |
| `manuscript/analytic/compact-scalar-positive.tex` | 675 | `811312fc8433bb89f339100f007694dd91de07ec20e4f4d691e36a1fca33fe07` |
| `manuscript/analytic/final-analytic-closure.tex` | 188 | `c0518cf17f0cbb20f92ba87e94c24bdb8873696ee6c9fa6bf134c4f5e631a7fb` |
| `manuscript/spherical-shell-polya-analytic-supplement.tex` | 245 | `16008399df3893c662f501994e1a50b5d8531f63641b6ae7b7afbc9403c289ee` |

The hashes agree with the current entries in
`manuscript/analytic/MANIFEST.md`.

## 1. Strict phase proxy

The main paper proves the exact channel count

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\ell\geq0}(2\ell+1)
 [\gamma_{\rho,K}(\ell+1/2)]_<
\]

from strict monotonicity of the Bessel phase.  The imported uniform phase
enclosure gives, for every active half-integer \(\nu<K\),

\[
 \gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+\frac14.
\]

Monotonicity of the strict positive-integer count therefore gives

\[
 N_D(A_{\rho,1},K^2)\leq
 P(\rho,K):=\sum_{\nu<K}2\nu
 \left[A_{\rho,K}(\nu)+\frac14\right]_<.
\]

This is the same strict proxy used in Parts VII--X.  At an integer proxy
wall, the equality layer is excluded.  At \(\nu=K\), the channel is inactive;
the phase proof separately shows that it contains no positive phase level.
At \(\nu=\rho K\), zero extension fixes \(G_{\rho K}(\nu)=0\), so there is
no interface ambiguity.  Coincident spectral walls add their multiplicities
inside the exact channel sum.

The only non-elementary input in this bridge is the explicitly cited analytic
Bessel-phase enclosure.  No numerical certificate is used.

## 2. Exact layer cake and retained radial identity

With \(x_n=n-1/4\), inverse action \(R\), and

\[
 M(r)=\#\{\ell\geq0:\ell+1/2<r\},
\]

finite sum interchange gives exactly

\[
 P=\sum_{\substack{n\geq1\\x_n<T}}M(R(x_n))^2,
 \qquad
 W=\int_0^T R(t)^2\,dt.
\]

The strict radial condition \(x_n<T\) and strict angular condition inside
\(M\) agree with the original proxy.  If \(x_n=T\), the omitted value would
have weight \(R(T)^2=0\); if \(R(x_n)=m+1/2\), then \(M=m\), as required.

I recomputed the shifted sawtooth at both exceptional locations:

* on the first cell \(0\leq t\leq3/4\),
  \(\mathfrak W=t^2/2\) and
  \(\Psi=\tfrac12(t-1/4)^2-1/32\);
* on every subsequent closed cell \(t=x_n+u\), \(0\leq u\leq1\),
  \(\Psi=\tfrac12(u-1/2)^2-1/32\).

Thus \(-1/32\leq\Psi\leq3/32\) includes the first cell, all grid
endpoints, and a terminal point \(T=x_n\).

For \(F=R^2\) and \(g=-F'\), the outer branch has decreasing \(g\) and the
inner branch has increasing \(g\).  At the turning interface
\(\tau=A(\rho K)\), the two formulas meet at

\[
 g(\tau)=\frac{2\pi\rho K}{\arccos\rho}.
\]

The one-sided terminal value is
\(g(T)=2\pi\rho K/(1-\rho)\).  Splitting the Stieltjes integral at
\(\tau\) cancels the uncontrolled \(\Psi(\tau)\) term exactly.  Direct
algebra then gives

\[
 W-P=\mathcal B+\mathcal R_{\rm dec}
       +\mathcal R_{\rm osc}-\mathcal E_{\rm ang},
\]

with both retained remainders nonnegative.  The boundary term at \(t=0\)
vanishes because \(\mathfrak W(t)g(t)=O(t^{5/3})\); the terminal term is
handled by \(F(T)=0\) and the displayed one-sided \(g(T)\).

The smooth minorant

\[
 L(t)=\frac{t^2}{2(1+2t)}\leq\mathfrak W(t)
\]

is valid on the first cell directly and, for \(t\geq3/4\), because

\[
 \frac t4-\frac1{32}-L(t)
 =\frac{6t-1}{32(1+2t)}\geq0.
\]

Consequently \(0\leq\mathcal R_*\leq\mathcal R_{\rm dec}\), and the
change from \(t\) back to the outer action variable has the correct
orientation: \(g(t)\,dt=-2z\,dz\).  This reconstructs

\[
 \mathcal E_{\rm ang}<\mathcal H
 \quad\Longrightarrow\quad P<W.
\]

## 3. Angular block, terminal layer, and common jumps

The exact common-jump identity is consistent with the strict representatives.
Both the radial counting function and \(h(t)=e(R(t))\) are right-continuous.
For right-continuous bounded-variation functions,

\[
 d(hp)=h\,dp+p^-\,dh.
\]

At a common wall \(t=x_n=n-1/4\),
\(p(t^-)=n-1-x_n=-3/4\).  Hence the displayed Euler identity includes the
simultaneous jump once, with the correct pre-jump multiplier; it neither
drops nor doubles a wall term.

The final bound does not silently depend on deleting the jump term or on the
complete-cell heuristic.  It follows from the separate one-layer inequality.
For each active \(x_n<T\), the left block \([n-1,x_n]\) is contained in
\([0,T]\), and the blocks are pairwise disjoint.  Since
\(0\leq q=-A'\leq1/2\),

\[
 R(t)\geq r_n+2(x_n-t),\qquad n-1\leq t\leq x_n,
\]

so

\[
 r_n\leq\frac43\int_{n-1}^{x_n}R(t)\,dt-\frac34.
\]

Strict angular counting gives, including at every half-integer wall,

\[
 m_n^2-r_n^2<r_n+\frac14.
\]

Summing the disjoint blocks and using the inverse-area identity yields

\[
 \mathcal E_{\rm ang}
 <\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

This argument covers the first radial layer, the last active layer, a
terminal equality \(T=x_{N+1}\), the turning interface, and a common
radial--angular jump without a separate continuity assumption.  On the
current middle-ratio domain,

\[
 T\geq\frac{(1-\rho)k_{11}(\rho)}\pi
 =\sqrt{1+\frac{132(1-\rho)^2}{\pi^2}}>1,
\]

so \(N\geq1\) and therefore

\[
 \mathcal E_{\rm ang}
 <M_c:=\frac{(1-\rho^2)K^2}{6}-\frac12.
\]

## 4. Scalar positivity on the unbounded frequency domain

Scaling the loss integral on \([\rho K,K]\) gives exactly

\[
 \mathcal J(\rho,K)=\frac{K^2}{2}
 \int_\rho^1\frac{s\,ds}{(1+2KG_1(s))^2}.
\]

Differentiation is exact:

\[
 \partial_K\mathcal J
 =K\int_\rho^1\frac{s\,ds}{(1+2KG_1(s))^3}.
\]

The turning lower bound
\(G_1(s)\geq2\sqrt2(1-s)^{3/2}/(3\pi)\) has the correct direction.
The beta integral equals

\[
 \frac{8\pi}{27\sqrt3}(aK)^{-2/3},
 \qquad a=\frac{4\sqrt2}{3\pi}.
\]

At \(K=12\), its cube is
\(\pi^5/(59049\sqrt3)\), and the printed rational chain to
\((88/567)^3\) is strict.  The resulting derivative minorant reduces to a
cubic \(p(\rho)\).  I independently converted that cubic to Bernstein form
on \([7/51,39/50]\); the four coefficients reproduce the source exactly:

\[
 \frac{335005}{2785671},\quad
 \frac{32947387}{196635600},\quad
 \frac{281783183}{578340000},\quad
 \frac{231517}{13500000}.
\]

All are positive, so \(\partial_K\mathcal S>0\) for every
\(K\geq k_{11}(\rho)>241/20>12\).

For the base curve, convex secants of \(\phi(z)=(1+z)^{-2}\) have the
correct majorant direction.  Recomputing the ten rational cells gives the
source value

\[
 Q=
 \frac{1305767238061446154064110434835938779253983373178558326887}
 {7706446260271137290663804190970969288616921855152043745280}
 <\frac{17}{100},
\]

with the same printed positive gap.  The endpoint estimate uses only
positive-side substitutions: a lower bound for \(k^2\) multiplies
\(C(\rho)>0\), while an upper bound for \(k\) multiplies the negative term
\(-\rho E(t)k\).  Thus neither inequality direction reverses.

Finally, I expanded the displayed factorized degree-nine polynomial and
independently converted it to the Bernstein basis on
\([7/15,14/15]\).  Every power coefficient and all ten displayed Bernstein
coefficients agree exactly with the current source and are positive.  Hence
the base gap is strictly positive on both ratio endpoints and throughout the
interval.  Upward integration proves

\[
 \mathcal H-M_c=\mathcal S>0
\]

for every finite \(K\geq k_{11}(\rho)\), with no upper cutoff.

The exact-arithmetic recomputation was an audit cross-check only.  The proof
itself contains the rational grids, convexity argument, antiderivatives,
positive gaps, and Bernstein coefficients, so no executable result is a
premise.

## 5. Exact residual containment and endpoint ownership

Packet F starts from the disjoint Round--19 decomposition
\(D_{19}=D_{\rm low}\mathbin{\dot\cup}D_{\rm high}\).  The proved lower
owner is exactly \(D_{\rm low}\).  Removing it leaves \(D_{\rm high}\).
Inside that set, removing the inclusive staircase

\[
 k_6(\rho)<K\leq k_{11}(\rho)
\]

leaves exactly

\[
 D_{20}=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
 k_{11}(\rho)<K<U(\rho)\right\}.
\]

This set calculation does not depend on an event ordering or executable
truth table.  Its faces are consistent:

* \(\rho=\rho_c\) remains in \(D_{20}\) when both frequency inequalities
  are strict;
* \(\rho=39/50\) was assigned to the inclusive optical owner;
* \(K=k_{11}(\rho)\) was assigned to the closed staircase;
* \(K=U(\rho)\) was already assigned to the inclusive high-frequency owner.

Weakening the two strict inequalities gives the immediate containment

\[
 D_{20}\subset
 \left\{\rho_c\leq\rho\leq\frac{39}{50},\quad
 K\geq k_{11}(\rho)\right\}.
\]

On that closed superset the strict chain

\[
 \mathcal E_{\rm ang}<M_c<\mathcal H,
 \qquad N_D\leq P<W,
\]

proves every point of \(D_{20}\).  The stronger theorem also proves the
\(\rho=39/50\) and \(K=k_{11}\) faces without changing their pre-existing
owners.

## 6. Hidden-premise audit

The live closure uses:

1. the stated analytic Bessel-phase theorem;
2. exact inverse-action and Stieltjes identities;
3. elementary integral and convexity inequalities;
4. displayed exact rational secants, gaps, and Bernstein coefficients; and
5. the explicit set subtraction above.

It does **not** use the retired \(10{,}580\)-box compact certificate, the
\(1{,}286\)-box aggregate certificate, Arb, a sampled minimum, numerical root
isolation, the retired \(K=200\) frequency split, or the executable
63-state classifier.  Those artifacts are mentioned only as historical or
regression material.

## First unsupported implication

None found.  Under the current hashes, the all-frequency retained-remainder
closure passes the requested adversarial audit.
