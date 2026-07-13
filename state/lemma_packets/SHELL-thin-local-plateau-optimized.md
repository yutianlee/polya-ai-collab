# Lemma Packet: Optimized Uniform Thin-Shell Local Plateau

Obligation: SHELL-thin-local-plateau-optimized.

Round: 9.

This packet freezes a new proof of the high-frequency thin-shell range.  It
must not import SHELL-thin-local-plateau-high or any intermediate estimate
whose derivation already assumes $K\ge64\varepsilon^{-2}$.

## Target theorem

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{100}.
$$

Prove

$$
\boxed{
K\ge\frac{125}{8\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

The threshold equality is included.  The constant $125/8$ is not claimed to
be optimal.

## Permitted proved inputs

1. CONV-strict-counting and SHELL-sturm-liouville-completeness.
2. SHELL-phase-enclosures and the strict-to-ordinary-floor transfer.
3. SHELL-weighted-lattice-scaffold and
   SHELL-high-angular-shifted-tails.
4. The pre-threshold Round 3 low-interface decomposition contained in
   SHELL-low-interface-fixed-rho-high-energy: for a low shifted tail,

   $$
   \frac{\mathcal T_r}{2}
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   $$

   with

   $$
   M=\lfloor K\eta\rfloor+d(n-p)-p,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   $$

   and the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   $$

No conclusion of the old $64\varepsilon^{-2}$ theorem is permitted.

## Frozen scaled-loss proof

Put

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2,
\qquad
R=p-dm,
$$

and, in the dangerous branch $R>0$,

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
$$

An elementary trigonometric estimate gives

$$
d>\frac9{10},
\qquad
S<\frac{19}{9}P.
\tag{2}
$$

With $U=\rho K-x_0$ and $t=x_0/(\rho K)$, the unconditional shelf estimate,
$\kappa\ge125/8$, and $y\le1/10$ imply

$$
\frac{U}{\rho K}<\frac17,
\qquad
t>\frac67.
\tag{3}
$$

Define

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1).
\tag{4}
$$

The exact local slope and same-floor relation yield

$$
\boxed{
P^2<
H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{5}
$$

Since

$$
S=P+\frac{P-r}{d},
$$

$H$ is decreasing in $r$.  On the complete synthetic comparison path used
below, the unconditional shelf ceiling and (2) remain valid, so
$\widehat q<1/7$.  Moreover,

$$
\frac{\partial H}{\partial P}
<
\frac{673816}{1366875}
<\frac12.
\tag{6}
$$

Set

$$
B_*=\frac{361}{80}.
$$

If $r\ge B_*$, then $P\ge r$ and

$$
P^2-H(P,r)
\ge P^2-H(P,B_*)
\ge B_*^2-H(B_*,B_*).
$$

The last expression is minimized at
$y=1/10$ and $\kappa=125/8$.  There

$$
Q_*=\frac{12869}{12500},
\qquad
\widehat q_*=\frac{41}{137500},
$$

and the exact endpoint margin is

$$
B_*^2
-2\left(\frac{22}{7}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=
\frac{72581986185449}{5925464687161600}
>0.
\tag{7}
$$

This contradicts (5), proving

$$
\boxed{
R<\frac{361}{80\sqrt\varepsilon}.
}
\tag{8}
$$

The no-drop branch $p=n$ has $m=0$, hence $P=r$, and is exactly the endpoint
geometry in (7).

## Action gain and strict payment

The action height satisfies

$$
\eta=G_1(1-\varepsilon)
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
$$

Using

$$
\sqrt2>\frac{140}{99},
\qquad
\pi<\frac{1571}{500},
$$

gives

$$
\frac{2\sqrt2\,\kappa}{3\pi}
\ge\frac{125\sqrt2}{12\pi}
>\frac{2187500}{466587}.
$$

Thus, in the dangerous branch,

$$
M
>
\left(
\frac{2187500}{466587}-\frac{361}{80}
\right)\frac1y-1
\ge
\frac{2829397}{3732696}.
\tag{9}
$$

Meanwhile

$$
4\delta
<\frac{8\sqrt2}{15}
<\frac{132}{175},
$$

and the exact final margin is

$$
\frac{2829397}{3732696}-\frac{132}{175}
=
\frac{2428603}{653221800}
>0.
\tag{10}
$$

If $R\le0$, the convex gain alone gives $M>1>4\delta$.  This includes the
immediate-drop branch $p=0$ and the degenerate head $n=0$.  The same-floor
inequality and $\lfloor x\rfloor>x-1$ remain strict at ordinary-floor and
gain walls.  At the interface wall the remainder is $\delta=0$.

The exact rational ledger is independently executable at
computations/round9_verify_thin_plateau_constants.py.

## Exact endpoint overlap

Combine (1) with the already-proved aggregate-action range

$$
K\le\frac1{8\varepsilon^{5/2}}.
$$

The two ranges overlap, including equality, exactly when

$$
125\sqrt\varepsilon\le1,
$$

that is,

$$
\boxed{
0<\varepsilon\le\frac1{15625}.
}
\tag{11}
$$

At equality the common frequency is

$$
\frac{125^5}{8}<2^{32}.
$$

On the complementary thin compact strip
$1/15625\le\varepsilon\le1/100$, the possible residual satisfies

$$
K<\frac{125}{8\varepsilon^2}
\le\frac{125^5}{8}
<2^{32}.
\tag{12}
$$

Together with the unchanged central ceiling below $2^{35}$, (12) lowers the
global compact analytic ceiling from $2^{42}$ to $2^{35}$.

## Mandatory falsification cases

- $\varepsilon=1/100$ and $\varepsilon=1/15625$;
- $K=125/(8\varepsilon^2)$;
- equality of the high and aggregate-action thresholds;
- the no-drop branch $p=n$;
- the immediate-drop branch $p=0$;
- the degenerate head $n=0$;
- $R=0$ and the first dangerous value $R>0$;
- the synthetic $P'$ comparison path and its inherited shelf ceiling;
- monotonicity of $H$ in both $r$ and $P$;
- the endpoint maxima $Q_*$ and $\widehat q_*$;
- the interface wall, ordinary-floor walls, gain walls, and spectral walls;
- every inequality in (2)--(10) checked without importing the old constant
  $64$.

## Promotion rule

Promote (1) only after an isolated proof and an adversarial audit both verify
the scaled-loss argument, all exceptional branches, and all wall strictness.
Promotion strengthens the thin endpoint to (11) and the compact analytic
envelope to the ceiling $2^{35}$; it does not certify the remaining compact
residual and does not close SHELL-rho-compact.
