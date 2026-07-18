# General dimension, Round 5: a uniform first-drop critical gap

Date: 18 July 2026

Status: rigorous strengthening of the critical-ray theorem.  The earlier
argument gave a strict but non-quantified comparison for the first-drop
branch.  The estimate below gives a uniform positive gap for every floor
\(f\ge2\).  It is a limiting theorem; a global exact-shell conclusion still
requires a uniform finite-thickness transfer and an exhaustion showing that
every escaping first-drop sequence enters this scaling.

## 1. Critical profile and prefix

Put

\[
 c_0=\frac{2\sqrt2}{3\pi},\qquad
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right),
 \qquad w=H_\kappa(0)=c_0\kappa.
\]

Fix an ordinary first-floor value \(f\ge2\), set
\(h=f-1/4\), and suppose the first shelf drops before the interface.
Let

\[
 H_\kappa(M)=h,\qquad H_\kappa(N)=f,qquad 0\le M<N.
\]

The worst limiting first-drop prefix is

\[
 \mathcal L=-2\int_M^N(f-H_\kappa(X))\,dX+\frac M2.
 \tag{1}
\]

As in the earlier critical-ray proof, write \(X=\kappa u\) and

\[
 t=\sqrt{1+u}-\sqrt u\in(0,1].
\]

Then

\[
 \frac{H_\kappa(X)}w=F(t):=\frac{3/t+t^3}{4}
 =\frac{3+t^4}{4t},qquad
 u(t)=\frac{(1-t^2)^2}{4t^2},qquad
 H_\kappa'(X)=\frac{3c_0}{2}t.
 \tag{2}
\]

Let \(t_h,t_f\) be the parameters at \(M,N\), respectively.  Thus
\(0<t_f<t_h\le1\).

## 2. Improved forced-slope lemma

### Lemma

If \(\mathcal L<0\), then

\[
 \boxed{t_f>\frac13.}
 \tag{3}
\]

### Proof

Since \(0\le f-H_\kappa\le1/4\) on \([M,N]\), equation (1) implies

\[
 \frac M2<2\int_M^N(f-H_\kappa)\,dX
 \le\frac{N-M}{2}.
\]

Hence

\[
 N>2M.
 \tag{4}
\]

Assume instead that \(t_f\le1/3\).  The function \(F\) is strictly
decreasing on \((0,1]\), and

\[
 F(t_f)\ge\frac{3}{4t_f}\ge\frac94.
\]

Because \(h/f\ge7/8\),

\[
 F(t_h)=\frac hfF(t_f)\ge\frac{63}{32}.
\]

But

\[
 F\left(\frac25\right)=\frac{1891}{1000}<\frac{63}{32},
\]

so \(t_h<2/5\).  Moreover,

\[
 \frac{t_h}{t_f}
 =\frac fh\frac{3+t_h^4}{3+t_f^4}
 \le\frac87\frac{1891}{1875}
 =\frac{15128}{13125}.
\]

Consequently

\[
 \frac{N}{M}=\frac{u(t_f)}{u(t_h)}
 =\left(\frac{t_h}{t_f}\right)^2
  \left(\frac{1-t_f^2}{1-t_h^2}\right)^2
 <\left(\frac{15128}{13125}\right)^2
  \left(\frac{25}{21}\right)^2
 =\frac{228856384}{121550625}<2.
\]

This contradicts (4).  The same argument automatically excludes the
degenerate value \(M=0\): under the contrary hypothesis it first forces
\(t_h<2/5\), hence \(M>0\).  This proves (3).

## 3. Uniform terminal overpayment

The level difference and (2)--(3) give

\[
 \frac14=H_\kappa(N)-H_\kappa(M)
 >\frac{c_0}{2}(N-M),
\]

and therefore

\[
 N-M<\frac1{2c_0}.
 \tag{5}
\]

Equations (1) and (5) imply

\[
 -\mathcal L
 \le 2\int_M^N(f-H_\kappa)\,dX
 \le\frac{N-M}{2}
 <\frac1{4c_0}
 =\frac{3\pi}{8\sqrt2}.
 \tag{6}
\]

Also \(t_f>1/3\) gives

\[
 \frac fw=F(t_f)<F\left(\frac13\right)=\frac{61}{27},
 \qquad
 w>\frac{27f}{61}\ge\frac{54}{61}>\frac34.
 \tag{7}
\]

Thus the first complete exact-angle terminal level is present.  The
wall-safe critical terminal estimate gives

\[
 \mathcal T(w)
 \ge\frac\pi{2\sqrt2}
 \left(\frac{w}{3/4}\right)^{1/3}
 >\frac\pi{2\sqrt2}.
 \tag{8}
\]

Combining (6)--(8) proves the uniform gap

\[
 \boxed{
 \mathcal L+\mathcal T(w)>
 \frac\pi{8\sqrt2}.}
 \tag{9}
\]

The fractional-top term is nonnegative and was not used.  In particular,
the bound is uniform in the floor \(f\ge2\), the critical parameter
\(\kappa\), and all limiting first-drop configurations.

## 4. Scope

The new constant in (9) removes the non-uniformity in the previous
first-drop critical comparison.  To promote it to an exact-shell theorem one
still has to prove two statements:

1. every unbounded residual high-floor first-drop sequence is forced into
   the critical turning coordinates (or into an already automatic sector);
2. the exact action and exact terminal angle approach their critical forms
   with an error smaller than \(\pi/(8\sqrt2)\), uniformly on the resulting
   compact scaled domain.

No finite chamber is asserted to be closed merely by the limiting argument.
