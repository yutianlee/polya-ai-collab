# Clean-room audit of `compact-structural.tex`

## Verdict: PASS

The exact layer-cake formulas, the retained-remainder Stieltjes identity, the
smooth minorant \(L\), and the implication

\[
\mathcal E_{\mathrm{ang}}<\mathcal H\quad\Longrightarrow\quad P<W
\]

all check out.  In particular, the strict radial and angular wall conventions
are preserved by the layer-cake rearrangement, and no endpoint or interface
term is missing in the two integrations by parts.

This is a local verdict on the deductions in this note.  It does not prove the
final inequality \(\mathcal E_{\mathrm{ang}}<\mathcal H\), which the source
correctly labels as unresolved.

## 1. Preliminary inverse facts

For \(0<z<\rho K\),

\[
-A'(z)=\frac1\pi\left(
 \arccos\frac zK-\arccos\frac z{\rho K}\right)>0,
\]

and for \(\rho K\le z<K\),

\[
-A'(z)=\frac1\pi\arccos\frac zK>0.
\]

Thus \(A\) is continuous and strictly decreasing from \(T=A(0)\) to
\(0=A(K)\), so the decreasing inverse \(R:[0,T]\to[0,K]\) exists.

Writing \(z=R(t)\), differentiation of \(F(t)=R(t)^2\) gives

\[
g(t)=-F'(t)=\frac{2z}{-A'(z)}.
\]

On the outer branch \(0<t<\tau\), this is

\[
g(t)=\frac{2\pi z}{\arccos(z/K)},
\]

which decreases as \(t\) increases.  On the inner branch, if

\[
\delta(z)=\arccos(z/K)-\arccos(z/(\rho K)),
\]

then

\[
\frac{\delta(z)}z=
\int_\rho^1\frac{ds}{s\sqrt{s^2K^2-z^2}}
\]

increases with \(z\).  Hence \(z/\delta(z)\), and therefore
\(g=2\pi z/\delta(z)\), increases when \(t\) increases and \(z\) decreases.
The one-sided values used later are

\[
F(\tau)=\rho^2K^2,
\qquad
g(\tau)=\frac{2\pi\rho K}{\arccos\rho},
\qquad
g(T)=\frac{2\pi\rho K}{1-\rho}.
\]

The outer-boundary parametrization \(z=K\cos\theta\) gives
\(A(z)\asymp\theta^3\) and \(g\asymp\theta^{-1}\); hence
\(g(t)=O(t^{-1/3})\) as \(t\downarrow0\).  This is sufficient for all
improper boundary products below.

## 2. Exact layer cake and strict walls

For a fixed half-integer \(\nu\),

\[
\left[A(\nu)+\frac14\right]_{<}
=\#\{n\ge1:n<A(\nu)+1/4\}
=\#\{n\ge1:x_n<A(\nu)\}.
\]

Because \(A\) is strictly decreasing,

\[
x_n<A(\nu)\quad\Longleftrightarrow\quad \nu<R(x_n).
\]

The inequality is strict on both sides.  Thus a radial equality
\(x_n=A(\nu)\) is excluded before and after inversion.  Moreover, any
contributing \(x_n\) satisfies \(x_n<T\), while for such an \(x_n\),
\(R(x_n)\le K\), so the original restriction \(\nu<K\) is automatic under
\(\nu<R(x_n)\).

After interchanging the two finite sums, the contribution at fixed \(n\) is

\[
\sum_{\ell+1/2<R(x_n)}(2\ell+1)=M(R(x_n))^2.
\]

At \(R(x_n)=m+1/2\), strict counting includes exactly
\(\ell=0,\ldots,m-1\), so \(M=m\).  Therefore

\[
P=\sum_{x_n<T}M(R(x_n))^2
\]

is exact at simultaneous radial--angular walls.

For the continuous identity, Tonelli's theorem applied to the subgraph gives

\[
\begin{aligned}
\int_0^T R(t)^2\,dt
&=\int_0^T\int_0^{R(t)}2z\,dz\,dt\\
&=\int_0^K2z\,\bigl|\{t\in(0,T):z<R(t)\}\bigr|\,dz\\
&=\int_0^K2zA(z)\,dz=W.
\end{aligned}
\]

Indeed, \(z<R(t)\) is equivalent to \(t<A(z)\); equality choices occur on
sets of measure zero.  The two-term identity

\[
W-P=\mathcal D_{\mathrm{rad}}-\mathcal E_{\mathrm{ang}}
\]

then follows by adding and subtracting
\(\sum_{x_n<T}R(x_n)^2\).

## 3. The shifted sawtooth

Let

\[
C(t)=\#\{n\ge1:x_n<t\},
\qquad w(t)=t-C(t),
\qquad \mathfrak W(t)=\int_0^t w(s)\,ds,
\qquad \Psi(t)=\mathfrak W(t)-t/4.
\]

On the initial interval, \(C=0\) almost everywhere and
\(\mathfrak W=t^2/2\).  On a periodic cell \(t=x_n+u\), \(0\le u\le1\),
direct integration gives

\[
\Psi(t)=\frac12(u-1/2)^2-\frac1{32}.
\]

The endpoint values from adjacent cells agree, so \(\Psi\) and
\(\mathfrak W\) are continuous even though \(w\) jumps.  Consequently

\[
-\frac1{32}\le\Psi\le\frac3{32},
\qquad \mathfrak W\ge0.
\]

## 4. First Stieltjes identity

Distributionally, \(dw=dt-dC\), where \(dC\) has a unit atom at every
\(x_n\).  Since \(F\) is continuous, the representative chosen for \(C\) at
an atom does not change the Stieltjes measure.  On \((0,T)\),

\[
\int F\,dC=\sum_{x_n<T}F(x_n).
\]

If \(T=x_n\), including the endpoint atom would still make no difference
because \(F(T)=0\).  Integration by parts therefore yields

\[
\begin{aligned}
\mathcal D_{\mathrm{rad}}
&=\int_0^T F(t)\,dt-\sum_{x_n<T}F(x_n)\\
&=\int F\,dw\\
&=[Fw]_0^T-\int_0^T w\,dF\\
&=\int_0^T w(t)g(t)\,dt.
\end{aligned}
\]

Here \(w(0)=0\), \(F(T)=0\), and \(dF=-g\,dt\).  There is no simultaneous
jump correction because \(F\) is continuous.

## 5. Exact retained-remainder decomposition

On the decreasing branch, \(d\mathfrak W=w\,dt\), so

\[
\int_0^\tau wg\,dt
=\mathfrak W(\tau)g(\tau)
-\int_{(0,\tau)}\mathfrak W\,dg.
\]

The boundary product at zero vanishes because
\(\mathfrak W(t)=t^2/2\) and \(g(t)=O(t^{-1/3})\).

On the increasing branch, \(w=1/4+\Psi'\) almost everywhere and
\(\int_\tau^Tg=F(\tau)\).  Since \(\Psi\) is continuous,

\[
\int_\tau^T wg\,dt
=\frac{F(\tau)}4+\Psi(T)g(T)-\Psi(\tau)g(\tau)
-\int_{(\tau,T)}\Psi\,dg.
\]

The function \(g\) is continuous at \(\tau\), although its monotonicity
changes there, so \(dg\) has no interface atom.  Using
\(\mathfrak W(\tau)=\tau/4+\Psi(\tau)\) cancels the two interface values
\(\Psi(\tau)g(\tau)\).

The remaining algebra is exact.  With

\[
\mathcal R_{\mathrm{dec}}
=-\int_{(0,\tau)}\mathfrak W\,dg
\]

and

\[
\mathcal R_{\mathrm{osc}}
=\left(\Psi(T)+\frac1{32}\right)g(T)
+\int_{(\tau,T)}\left(\frac3{32}-\Psi\right)dg,
\]

the identity

\[
\begin{aligned}
\Psi(T)g(T)-\int_{(\tau,T)}\Psi\,dg
={}&-\frac{g(T)}8+\frac{3g(\tau)}{32}
+\mathcal R_{\mathrm{osc}}
\end{aligned}
\]

follows from
\(\int_{(\tau,T)}dg=g(T)-g(\tau)\).  Thus

\[
\mathcal D_{\mathrm{rad}}
=\frac{F(\tau)}4-\frac{g(T)}8
+g(\tau)\left(\frac\tau4+\frac3{32}\right)
+\mathcal R_{\mathrm{dec}}+\mathcal R_{\mathrm{osc}}.
\]

On \((0,\tau)\), \(-dg\) is a positive measure and
\(\mathfrak W\ge0\), so \(\mathcal R_{\mathrm{dec}}\ge0\).  On
\((\tau,T)\), \(dg\) is positive, while
\(\Psi(T)+1/32\ge0\) and \(3/32-\Psi\ge0\); hence
\(\mathcal R_{\mathrm{osc}}\ge0\).  Substitution of the three interface
data gives exactly the displayed \(\mathcal B\) and therefore the master
identity

\[
W-P=\mathcal B+\mathcal R_{\mathrm{dec}}
              +\mathcal R_{\mathrm{osc}}-\mathcal E_{\mathrm{ang}}.
\]

## 6. Audit of the minorant \(L\)

For

\[
L(t)=\frac{t^2}{2(1+2t)},
\qquad
L'(t)=\frac{t(1+t)}{(1+2t)^2},
\]

one has \(L\ge0\).  If \(0\le t\le3/4\), then
\(\mathfrak W(t)=t^2/2\ge L(t)\).  If \(t\ge3/4\), the sawtooth bound gives

\[
\mathfrak W(t)\ge\frac t4-\frac1{32},
\]

and direct subtraction gives

\[
\frac t4-\frac1{32}-L(t)
=\frac{6t-1}{32(1+2t)}\ge0.
\]

Thus \(0\le L\le\mathfrak W\) globally.  Since \(-dg\) is positive on the
decreasing branch,

\[
0\le\mathcal R_*:=-\int_{(0,\tau)}L\,dg
\le\mathcal R_{\mathrm{dec}}.
\]

Integration by parts is valid at zero because
\(L(t)g(t)=O(t^{5/3})\), and gives

\[
\mathcal R_*=-L(\tau)g(\tau)+\int_0^\tau L'(t)g(t)\,dt.
\]

On the outer branch \(t=A(z)\), \(z\) runs from \(K\) down to \(\rho K\),
and differentiating \(F=z^2\) gives

\[
g(t)\,dt=-2z\,dz.
\]

Therefore

\[
\mathcal R_*
=-\frac{\tau^2}{2(1+2\tau)}g(\tau)
+\int_{\rho K}^{K}
2z\,\frac{A(z)(1+A(z))}{(1+2A(z))^2}\,dz,
\]

with the orientation and sign as stated in the source.

## 7. The imported implication used in Round 2

The source defines \(\mathcal H\) so that

\[
\mathcal H=\mathcal B+\mathcal R_*.
\]

Indeed, the only boundary simplification needed is

\[
\frac\tau4-\frac{\tau^2}{2(1+2\tau)}
=\frac{\tau}{4(1+2\tau)}.
\]

Now suppose \(\mathcal E_{\mathrm{ang}}<\mathcal H\).  The master identity
and the two remainder inequalities give

\[
\begin{aligned}
W-P
&=\mathcal B+\mathcal R_{\mathrm{dec}}
 +\mathcal R_{\mathrm{osc}}-\mathcal E_{\mathrm{ang}}\\
&\ge\mathcal B+\mathcal R_*-\mathcal E_{\mathrm{ang}}\\
&=\mathcal H-\mathcal E_{\mathrm{ang}}>0.
\end{aligned}
\]

Hence \(P<W\).  The implication imported by the Round 2 angular-block note
is therefore fully justified by this structural note.

## 8. Scope of the result

All deductions through the sufficient-condition corollary are analytic and
valid.  The note does not itself establish
\(\mathcal E_{\mathrm{ang}}<\mathcal H\) on the compact region.  That is a
separate proof obligation, not a gap in the structural implication.
