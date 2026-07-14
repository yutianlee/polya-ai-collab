# Source Card: Round 20 Higher-Radial Bessel-Zero Bound

Status: **internal elementary proof completed on 2026-07-14**.

This card authorizes exactly

\[
 \boxed{j_{7/2,2}>10}
 \tag{Z1}
\]

and the internal angular propagation

\[
 \boxed{j_{p+1/2,2}^{\,2}>88+p(p+1)\qquad(p\geq3).}
 \tag{Z2}
\]

In particular,

\[
 j_{9/2,2}^{\,2}>108,\qquad
 j_{11/2,2}^{\,2}>118,\qquad
 j_{13/2,2}^{\,2}>130.
 \tag{Z3}
\]

No external zero table, decimal zero approximation, or numerical root
solver is used.

## 1. Provenance and exact division of labor

The only source-supplied special-function identities are the already
authenticated NIST DLMF statements used by
sources/round19_bessel_zero_bounds.md:

1. [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3),

   \[
   \mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
   \qquad x>0,
   \tag{S1}
   \]

   whose prefactor is positive; and
2. [DLMF \(\S10.49(i)\)](https://dlmf.nist.gov/10.49.i), for the
   elementary half-integer spherical-Bessel formulas.

Specializing the second identity at spherical order three gives

\[
 \mathsf j_3(x)=\frac{P(x)}{x^4},
 \qquad
 P(x)=(15-6x^2)\sin x+(x^3-15x)\cos x.
 \tag{S2}
\]

Everything after (S1)--(S2), including the complete root enumeration,
the sign test at \(10\), the angular comparison, and the shell transfer,
is internal. The exact enclosure

\[
 \frac{333}{106}<\pi<\frac{22}{7}
 \tag{P}
\]

is inherited from the authenticated Round 19 arithmetic ledger. Only
the much weaker consequences needed below are used.

## 2. A derivative chain for the numerator

Put

\[
 R(x)=\sin x-x\cos x,
 \qquad
 Q(x)=(3-x^2)\sin x-3x\cos x.
 \tag{1}
\]

Direct differentiation, with no special-function theorem, gives

\[
 R'(x)=x\sin x,\qquad
 Q'(x)=xR(x),\qquad
 P'(x)=xQ(x).
 \tag{2}
\]

Also \(R(0)=Q(0)=P(0)=0\). This nested chain is enough to enumerate
the first two positive roots of \(P\).

## 3. No positive root through \(2\pi\)

On \((0,\pi)\), \(R'>0\), so \(R>0\). On \((\pi,2\pi)\), \(R'<0\),
and

\[
 R(\pi)=\pi>0,\qquad R(3\pi/2)=-1<0.
\]

Thus \(R\) has exactly one zero

\[
 \alpha_1\in(\pi,3\pi/2)
\]

and is positive before \(\alpha_1\) and negative after it, up to
\(2\pi\). Equation (2) now shows that \(Q\) increases on
\((0,\alpha_1)\) and decreases on \((\alpha_1,2\pi)\). Since

\[
 Q(2\pi)=-6\pi<0,
\]

\(Q\) has exactly one zero

\[
 \beta_1\in(\alpha_1,2\pi).
\]

Consequently \(P\) increases on \((0,\beta_1)\) and decreases on
\((\beta_1,2\pi)\). Its right endpoint is nevertheless positive:

\[
 P(2\pi)=2\pi(4\pi^2-15)>0,
\]

where \(\pi>3\) suffices. Therefore

\[
 \boxed{P(x)>0\qquad(0<x\leq2\pi).}
 \tag{3}
\]

In particular, no cancellation hidden near the origin or in an earlier
tangent cell can supply a positive zero.

## 4. Exactly one first root in \((2\pi,5\pi/2)\)

On \((2\pi,5\pi/2)\), \(R'>0\), while

\[
 R(2\pi)=-2\pi<0,\qquad R(5\pi/2)=1>0.
\]

Hence \(R\) has exactly one zero \(\alpha_2\) in this interval. The
function \(Q\) first decreases and then increases, but both endpoint
values are negative:

\[
 Q(2\pi)=-6\pi<0,\qquad
 Q(5\pi/2)=3-(5\pi/2)^2<0.
\]

It follows that \(Q<0\) throughout this entire cell and hence \(P'<0\).
Together with (3) and

\[
 P(5\pi/2)=15-6(5\pi/2)^2<0,
\]

this proves that \(P\) has exactly one root in
\((2\pi,5\pi/2)\).

On the complementary half-cell \((5\pi/2,3\pi)\), one has

\[
 \sin x>0,\quad \cos x<0,\quad 15-6x^2<0,\quad x^3-15x>0.
\]

Both terms in (S2) are therefore negative, so

\[
 P(x)<0\qquad(5\pi/2\leq x\leq3\pi).
 \tag{4}
\]

Thus the root just found is the first positive root and there is no root
between it and \(3\pi\).

## 5. Exactly one second root in \((3\pi,7\pi/2)\)

On \((3\pi,7\pi/2)\), \(R'<0\), with

\[
 R(3\pi)=3\pi>0,\qquad R(7\pi/2)=-1<0.
\]

Thus \(R\) has exactly one zero \(\alpha_3\) in this cell. The function
\(Q\) first increases and then decreases, and its two endpoint values
are positive:

\[
 Q(3\pi)=9\pi>0,\qquad
 Q(7\pi/2)=(7\pi/2)^2-3>0.
\]

Therefore \(Q>0\), so \(P'>0\), throughout the cell. Moreover,

\[
 P(3\pi)=-3\pi(9\pi^2-15)<0,\qquad
 P(7\pi/2)=6(7\pi/2)^2-15>0.
\]

There is exactly one root in \((3\pi,7\pi/2)\). By Sections 3--4,
this root is the second positive root of \(P\).

This derivative-chain argument is also a complete tangent-cell audit:
the first root lies in the positive-tangent cell
\((2\pi,5\pi/2)\), the complementary half-cell contains none, and the
second root is the unique root in the next positive-tangent cell
\((3\pi,7\pi/2)\).

## 6. Exact sign at \(x=10\)

The enclosure (P) gives

\[
 3\pi<10<\frac{7\pi}{2}.
\]

Indeed, \(\pi<22/7<10/3\), while
\(333/106>20/7\). Put

\[
 y=10-3\pi.
\]

Then \(0<y<\pi/2\), and the lower bound in (P) gives

\[
 y<10-3\frac{333}{106}=\frac{61}{106}<\frac35.
 \tag{5}
\]

For \(0<y<3/5\), elementary calculus yields

\[
 \sin y<y<\frac35,\qquad
 \cos y>1-\frac{y^2}{2}>\frac{41}{50}.
\]

Consequently

\[
 \tan y<\frac{30}{41}<\frac{170}{117}.
 \tag{6}
\]

Since \(\sin10=-\sin y\) and \(\cos10=-\cos y\), one obtains

\[
\begin{aligned}
 P(10)
 &=585\sin y-850\cos y\\
 &=\cos y\,(585\tan y-850)<0,
\end{aligned}
\]

where \(585(170/117)=850\). Section 5 says that \(P\) is strictly
increasing across the unique second-root cell. Hence that root lies
strictly to the right of \(10\).

By (S1), the positive zeros of \(\mathsf j_3\) and \(J_{7/2}\) coincide.
This proves the fully internal bound

\[
 \boxed{j_{7/2,2}>10.}
\]

## 7. Internal angular propagation

Let \(d_p=p(p+1)\). In the unit-ball radial transform, the fixed angular
forms for \(p\geq3\) have the same min--max domain, and their potential
difference is

\[
 \frac{d_p-d_3}{r^2}\geq d_p-d_3
 \qquad(0<r\leq1).
\]

The min--max principle therefore gives, at the same radial index,

\[
 j_{p+1/2,2}^{\,2}
 \geq j_{7/2,2}^{\,2}+d_p-d_3
 >100+d_p-12=88+d_p.
\]

This is (Z2), and substituting \(p=4,5,6\) gives (Z3). This comparison
is internal form ordering; it is not attributed to DLMF.

## 8. Exact transfer to shell channels

For the shell channel frequency \(q_{p,2}(\rho)\), zero extension from
\((\rho,1)\) to \((0,1)\), followed by fixed-channel min--max, gives the
internal comparison

\[
 q_{p,2}(\rho)^2\geq j_{p+1/2,2}^{\,2}.
\]

Thus this card also authorizes

\[
 \boxed{q_{3,2}>10},
 \qquad
 \boxed{q_{p,2}^{\,2}>88+p(p+1)\quad(p\geq3).}
 \tag{7}
\]

The inequalities remain strict at every displayed rational or quadratic
wall. Equality under the strict spectral count leaves the corresponding
mode uncounted.

## 9. Scope exclusions and verdict

This card does **not** supply a shell cross-product zero, a coupled
multi-channel inequality, a third-radial bound, a multiplicity count, a
Weyl payment, or a theorem beyond the explicit consequences (Z1)--(Z3)
and (7).

**Verdict: PASS. First unsupported implication: none.** The only
external content is the two labelled DLMF identities; the zero location,
all cell exclusions, the sign at \(10\), and every propagated inequality
are reconstructed internally with exact arithmetic.
