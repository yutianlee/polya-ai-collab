# Round 11 Adversarial Referee: Ultra-Thin Complementary Action Bridge

## Verdict

**PASS.**

Assuming the frozen claim false, the referee reconstructed the inverse-action
discrepancy and attacked every curvature, Stieltjes, ceiling, floor, and
endpoint step.  No unsupported implication was found.

**First unsupported implication: none.**

The exact ledger and its focused tests also pass:

```text
python computations/round11_verify_ultrathin_bridge.py
PASS

python -m pytest computations/tests/test_round11_ultrathin_bridge.py -q
3 passed
```

## 1. Inverse-action orientation

For $F=R^2$,

$$
F''(t)>0\quad(0<t<\tau),
\qquad
F''(t)<0\quad(\tau<t<T).
$$

Therefore $g=-F'$ decreases before $\tau$ and increases after $\tau$.  This
orientation is correct: low action levels correspond to
$R(t)>\rho a$, the convex part of $F$.  The interface derivative is finite
and nonzero, so $g$ is continuous at $\tau$.

Moreover,

$$
\tau=\frac{a}{\pi\varepsilon}
\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}a\sqrt\varepsilon.
$$

At the closed threshold $a=1/(8\varepsilon^{3/2})$,

$$
\tau>
\frac{49}{1320\varepsilon}
\ge\frac{245}{66}>1.
$$

Thus $3/4$ and $1$ are strictly inside the decreasing branch, including at
$\varepsilon=1/100$.

## 2. Radial sawtooth and discrepancy

Tonelli gives, without an endpoint correction,

$$
D=\int_0^T F(t)\,dt-
\sum_{x_n<T}F(x_n)
=\int_0^T\bigl(t-\mathcal N(t)\bigr)g(t)\,dt.
$$

For $t=j+r$,

$$
u(t)=t-\mathcal N(t)=
\begin{cases}
r,&0\le r\le3/4,\\
r-1,&3/4<r<1.
\end{cases}
$$

At $r=3/4$, the new radial layer is excluded and $u=3/4$, exactly matching
the strict convention.  For $v=u-1/4$, its continuous periodic primitive
$V$ satisfies

$$
-\frac1{32}\le V\le\frac3{32}.
$$

The extrema are exact.  The possible singularity of $g$ at zero causes no
problem: $g(t)=O(t^{-1/3})$, while $u(t)=t$ there, so $u(t)g(t)$ is
integrable.

## 3. Stieltjes interface audit

On $[1,\tau]$, $dg\le0$.  Integration by parts gives

$$
\int_1^\tau vg
\ge-\frac1{32}g(1).
$$

On $[\tau,T]$, $dg\ge0$, and

$$
\int_\tau^Tvg
\ge-\frac18g(T).
$$

The raw $V(\tau)g(\tau)$ terms have opposite signs and cancel before the
estimates are applied.  No assumption that $\tau$ lies on a grid is used.

The first-cell estimate is conservative.  The exact negative area on
$(3/4,1)$ is $1/32$, while the proof charges $1/16$.  Since $g$ decreases
there,

$$
\int_0^1ug\ge-\frac1{16}g(3/4)
$$

is valid with slack.  Together with $g(1)\le g(3/4)$, this proves

$$
D\ge
\frac14F(1)-\frac3{32}g(3/4)-\frac18g(T).
$$

## 4. Endpoint constants

For $t<\tau$, writing $R(t)=a\cos\theta$ gives

$$
t=\frac a{\pi\varepsilon}
(\sin\theta-\theta\cos\theta),
\qquad
g(t)=\frac{2\pi\varepsilon a\cos\theta}{\theta}.
$$

The three estimates are correctly oriented:

$$
g(3/4)<4\varepsilon^{2/3}a^{4/3},
$$

$$
F(1)>a^2-7\varepsilon^{2/3}a^{4/3},
$$

and, from the exact regular endpoint limit,

$$
g(T)=2\pi\rho a<\frac{44}{7}a.
$$

Their substitution gives exactly

$$
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a.
$$

No endpoint coefficient or factor of two is missing.

## 5. Angular ceilings and positive reserve

At every angular wall,

$$
M_\varepsilon(x)<\frac{x}{\varepsilon}+\frac12,
$$

so

$$
\varepsilon^2M_\varepsilon(x)^2
<x^2+\varepsilon x+\frac{\varepsilon^2}{4}.
$$

Equality channels are excluded correctly.  Since $a\ge125$,

$$
N<T+\frac14<\frac a2,
\qquad
\sum_{x_n<T}R(x_n)<\frac{a^2}{2}.
$$

Hence

$$
\frac{I-P_{\mathcal A}}{a^2}
>
\frac18
-\frac{17}{4}\varepsilon^{5/3}
-\frac{22}{7}\varepsilon^{3/2}
-\frac\varepsilon4
-\frac12\varepsilon^{7/2}.
$$

The exact charged coefficient is

$$
\frac{17}{80}+\frac{11}{35}+\frac14+\frac1{200000}
=\frac{1087507}{1400000}
<\frac{57}{7}.
$$

Thus, including $\varepsilon=1/100$ and threshold equality,

$$
\frac{I-P_{\mathcal A}}{a^2}
>
\frac18-\frac{57}{700}
=\boxed{\frac{61}{1400}>0}.
$$

The ledger reproduces this reserve exactly.

## 6. Strict walls

All mandatory walls pass.

- If $x_n=T$, the radial layer is excluded.
- If $R(x_n)/\varepsilon=\ell+1/2$, the angular equality channel is
  excluded.
- If $\mathcal A(y_\ell)+1/4=n$, the $n$th proxy layer is excluded.
- The interface $t=\tau$ is handled continuously; no discrete ownership is
  assumed.
- At a strict spectral wall, the phase majorant can only overcount.
- The face $a=1/(8\varepsilon^{3/2})$ is included because the final reserve
  remains strictly positive.
- The face $a=\pi/(4\varepsilon)$ belongs to both accepted lower ranges.
- The face $\rho=99/100$ belongs to both the new endpoint and the Round 10
  seam theorem.

The accepted product and aggregate ranges cover
$0\le a\le1/(8\varepsilon^{3/2})$, and the new bridge covers the
complementary closed range.  There is no gap.

## 7. Dependency and global-union audit

The bridge proof uses only the previously proved action calculus, strict
layer cake, and phase transfer.  It does not use the desired endpoint, the
Round 9 high theorem, the false global semicircle majorant, or the compact
envelope being strengthened.  The accepted aggregate conclusion is used
only for the lower closed union, not to prove the direct bridge.  There is no
circularity.

For the all-ratio consequence:

- central residuals satisfy $K<K_0(24/25)<6000^2$;
- on $24/25\le\rho\le99/100$, the seam threshold is at most $200000$;
- on $99/100\le\rho<1$, every frequency is now proved.

Therefore $K=6000^2$ itself belongs to every relevant high-frequency zone.
The exact ratios are

$$
\frac{125^5/8}{6000^2}
=\frac{1953125}{18432}>105,
\qquad
\frac{2^{35}}{6000^2}
=\frac{134217728}{140625}>954.
$$

## Final determination

The direct complementary-action bridge, the complete endpoint

$$
\boxed{\frac{99}{100}\le\rho<1},
$$

and the global high-frequency ceiling

$$
\boxed{K\ge6000^2}
$$

all survive adversarial reconstruction.

**Final verdict: PASS.  First unsupported implication: none.**
