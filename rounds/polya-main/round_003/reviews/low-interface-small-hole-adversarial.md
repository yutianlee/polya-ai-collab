# Adversarial Review: Small-Hole Low-Interface Tails

Historical note: this review predates, and helped produce, the later fixed-$\rho$ proof for every $0<\rho<1$.

Role: A4 adversarial reviewer  
Frozen artifact: rounds/polya-main/round_003/responses/low-interface-small-hole-incumbent.md  
Verdict: **pass for the stated small-hole sector; full low-interface problem remains open**

## Bottom line

I reconstructed the proof from the definitions of the trapezoidal floor sum and the primary annulus results. The chain is valid, including:

- the case \(n=0\);
- the shared split endpoint at \(n\);
- the cases \(q=\mu\) and \(K-x_0\in\mathbb Z\);
- the \(1/4\) and \(1/3\) Lipschitz constants;
- the turning-strip integral bound;
- the floor and strict-inequality directions in the final threshold.

The result proved is

$$
\boxed{
0<\rho<\omega_0,\qquad
K(\omega_0-\rho)
\ge
\frac12+\frac{8\sqrt2}{15},
}
$$

where

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16.
$$

In this sector every low-interface coarse shifted tail satisfies its target integral inequality. Together with the previously verified high tails, this proves the coarse weighted lattice inequality in this parameter sector. It does not prove the full low-interface obligation.

The source results checked are Proposition 3.1, Theorem 3.4, Lemma 6.1, and Lemma 6.2 of the [published annulus paper](https://doi.org/10.1112/jlms.70425).

## 1. Exact tail representation and endpoint \(B\)

Fix

$$
x_0=r+\frac12<\mu=\rho K,
\qquad
b=K-x_0,
$$

and write

$$
A(z)=G_K(z)-G_\mu(z).
$$

Set

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
B=\lceil K-x_0\rceil.
$$

Both \(G_K\) and \(A\) are extended by zero after their endpoints. If

$$
h_A(t)=A(x_0+t)+\frac14,
$$

then

$$
\frac{\mathcal T_r}{2}
=
\mathbf T(h_A,0,B).
$$

This remains exact in both endpoint cases:

1. If \(K-x_0\notin\mathbb Z\), then \(B=\lfloor b\rfloor+1\), and the endpoint sample is in the zero extension.
2. If \(K-x_0\in\mathbb Z\), then \(B=b\), but \(A(K)=0\), so the endpoint contribution is
   \[
   \frac12\left\lfloor\frac14\right\rfloor=0.
   \]

Thus using \(B=\lceil K-x_0\rceil\), rather than always adding one, causes no loss or missing sample.

## 2. Split at \(n\), including \(n=0\)

Suppose first that \(n\ge1\). Additivity of the trapezoidal floor sum gives

$$
\mathbf T(h_A,0,B)
=
\mathbf T(h_A,0,n)+\mathbf T(h_A,n,B).
$$

Since \(A\le G_K\), monotonicity of the floor gives

$$
\mathbf T(h_A,n,B)
\le
\mathbf T(G_K(x_0+\cdot)+\tfrac14,n,B).
$$

At the shared endpoint \(n\), the left block contributes half the \(A\)-sample and the majorized right block contributes half the \(G_K\)-sample. Since the latter is no smaller than the \(A\)-sample, their sum is at least the original full \(A\)-sample. Therefore no endpoint correction is missing.

If \(n=0\), the first interval is degenerate and must not be fed into Proposition 3.1. Instead one directly uses

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T(G_K(x_0+\cdot)+\tfrac14,0,B).
$$

All subsequent estimates remain valid with the \(n/4\) term equal to zero.

## 3. Concave head

Since

$$
q=x_0+n\le\mu,
$$

the function \(A(x_0+t)\) is concave on \([0,n]\). Indeed, for \(z<\mu\),

$$
A''(z)
=
\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}
<0.
$$

The value at \(q=\mu\), when equality occurs, is obtained by continuity; concavity on the closed interval is unaffected by the singular second derivative at the endpoint.

Proposition 3.1 applied to \(A(x_0+t)+1/4\) gives

$$
\mathbf T(A(x_0+\cdot)+\tfrac14,0,n)
\le
\int_0^n A(x_0+t)\,dt+\frac n4.
$$

The sign and the coefficient \(n/4\) are correct.

## 4. Improved convex suffix

On \([n,B]\), define

$$
g_K(t)=G_K(x_0+t).
$$

After zero extension this function is nonnegative, decreasing, convex, globally \(1/2\)-Lipschitz, and satisfies \(g_K(B)=0\).

Let

$$
t_*=\frac K2-x_0.
$$

The assumed sector has \(\rho<\omega_0<1/2\). Since \(q\le\mu=\rho K\),

$$
n=q-x_0<t_*.
$$

Also \(t_*\le K-x_0\le B\). Hence \(t_*\in[n,B]\), including when \(n=0\).

For \(t\ge t_*\),

$$
x_0+t\ge\frac K2,
$$

and

$$
|G_K'(x_0+t)|
=
\frac1\pi\arccos\frac{x_0+t}{K}
\le\frac13.
$$

Thus the hypotheses of annuli Theorem 3.4 hold. Moreover,

$$
g_K(t_*)
=G_K(K/2)
=
\left(\frac{\sqrt3}{2\pi}-\frac16\right)K
=\omega_0K.
$$

Therefore

$$
\mathbf T(g_K+\tfrac14,n,B)
\le
\int_n^B g_K(t)\,dt
-\frac14\lfloor\omega_0K\rfloor.
$$

No integrality of \(t_*\) is required by Theorem 3.4.

## 5. Exact mismatch and the case \(q=\mu\)

Combining the two pieces and comparing with the integral of \(A\) leaves exactly

$$
\delta
=
\int_q^\mu G_\mu(z)\,dz.
$$

The point \(q\) is the largest tail-grid half-integer at or below \(\mu\). It should not be described only as “below” \(\mu\), because equality occurs when \(\mu-x_0\in\mathbb Z\).

Let

$$
d=\mu-q\in[0,1).
$$

If \(d=0\), then

$$
\delta=0.
$$

For \(d>0\), annuli Lemma 6.2 gives

$$
G_\mu(z)
<
\frac{(\mu-z)^{3/2}}{3\sqrt\mu}.
$$

Integrating gives

$$
\delta
<
\frac{2d^{5/2}}{15\sqrt\mu}.
$$

The endpoint-safe unified statement is therefore

$$
0\le\delta
\le
\frac{2d^{5/2}}{15\sqrt\mu}
<
\frac{2\sqrt2}{15}.
$$

The first comparison is non-strict precisely to cover \(q=\mu\), where both sides are zero. The final comparison is strict because \(\mu>x_0\ge1/2\), so \(1/\sqrt\mu<\sqrt2\), and \(d<1\).

This estimate comes directly from Lemma 6.2. Corollary 6.3 should not be cited literally here because it is written with lower endpoint \(\lfloor\mu\rfloor\), whereas \(q\) is a half-integer.

## 6. Discrete gain and threshold

The preceding bounds give

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta
-\frac{\lfloor\omega_0K\rfloor-n}{4}.
$$

Now

$$
\lfloor\omega_0K\rfloor>\omega_0K-1
$$

and

$$
n\le\mu-x_0=\rho K-x_0.
$$

Consequently,

$$
\begin{aligned}
\lfloor\omega_0K\rfloor-n
&>\omega_0K-1-(\rho K-x_0)\\
&=K(\omega_0-\rho)+x_0-1\\
&\ge K(\omega_0-\rho)-\frac12.
\end{aligned}
$$

At the displayed threshold,

$$
K(\omega_0-\rho)-\frac12
\ge
\frac{8\sqrt2}{15}.
$$

Therefore

$$
\lfloor\omega_0K\rfloor-n
>
\frac{8\sqrt2}{15}
>
4\delta,
$$

including when \(\omega_0K\) is itself an integer. It follows that

$$
\mathcal T_r
<
2\int_{x_0}^{K}A(z)\,dz.
$$

The simpler sector with \(\rho<1/10\) follows from the audited bound \(\omega_0>1/10\).

## 7. First-failure search

I searched the following possible failure points.

### Algebraic endpoints

- \(n=0\): valid by omitting the degenerate concave block and applying Theorem 3.4 from zero.
- \(\mu-x_0\in\mathbb Z\): then \(q=\mu\) and \(\delta=0\); the non-strict first comparison in the mismatch bound is required.
- \(K-x_0\in\mathbb Z\): then \(B=K-x_0\) and the endpoint floor is \(\lfloor1/4\rfloor=0\).
- \(\omega_0K\in\mathbb Z\): the strict estimate \(\lfloor x\rfloor>x-1\) still holds.
- \(K\) or \(\mu\) on half-integer channel walls: the argument is stated tail-by-tail and uses the exact floor definitions, so no channel is silently added.

No failure occurs in these cases.

### Parameter boundary

The threshold diverges as \(\rho\uparrow\omega_0\). The proof therefore makes no claim at \(\rho=\omega_0\) or above it. This is a genuine scope boundary, not a removable endpoint.

A non-certified numerical stress check at the exact threshold and just above it, for

$$
\rho\in\{0.01,0.05,0.09,0.099,0.105,0.108\},
$$

found no shifted-tail violation. This check is diagnostic only and is not used in the proof.

## 8. Horizontal-block obstruction

The successful proof cannot be replaced by a theorem using only monotonicity, one concave-to-convex transition, and a Lipschitz constant below \(1/2\).

Let \(\lambda=191/190\) and define

$$
f(s)=
\begin{cases}
1-\dfrac{s^2}{4},&0\le s\le1,\\[1mm]
\dfrac54-\dfrac s2,&1\le s\le\dfrac94,\\[1mm]
\dfrac12\left(\dfrac{11}{4}-s\right)^2,
&\dfrac94\le s\le\dfrac{11}{4}.
\end{cases}
$$

Put \(g(t)=f(t/\lambda)\). Then \(g\) is \(C^1\), strictly decreasing, concave then convex, vanishes at its right endpoint, and

$$
\operatorname{Lip}(g)=\frac{95}{191}<\frac12.
$$

At the integer samples,

$$
\left\lfloor g(0)+\frac14\right\rfloor=1,
\qquad
\left\lfloor g(1)+\frac14\right\rfloor=1,
\qquad
\left\lfloor g(2)+\frac14\right\rfloor=0.
$$

Thus its symmetric shifted-floor count is \(3\), whereas

$$
2\int g
=
\frac{191}{64}
<3.
$$

This is an exact counterexample to the abstract shortcut. It is not a counterexample to the shell action.

Termwise horizontal FLPS blocks can also fail for an actual shell action. Take

$$
K=11,\qquad
\mu=\frac32,\qquad
x_0=\frac12.
$$

Then

$$
\begin{aligned}
g(0)&=3.000781646931250\ldots,\\
g(1)&=2.784013897871729\ldots,\\
g(2)&=2.342233110792977\ldots.
\end{aligned}
$$

The shifted \(k=2\) block on \([0,2]\) has trapezoidal floor sum

$$
\frac12(3)+3+\frac12(2)=5.5,
$$

but

$$
\int_0^2g(t)\,dt
=5.477197398214329\ldots.
$$

The local block fails by \(0.022802601785671\ldots\). The complete tail nevertheless satisfies

$$
23
<
26.671242517616323\ldots
=2\int_0^{K-x_0}g(t)\,dt.
$$

Hence a full proof must transfer surplus between horizontal blocks.

## 9. Precise residual outside the small-hole sector

The annulus floor theorems isolate a useful remaining compensation inequality.

Let

$$
\tau=\mu-x_0,\qquad
p=\lfloor\tau\rfloor,\qquad
a_j=\left\lfloor g(j)+\frac14\right\rfloor.
$$

If \(a_0=0\), the tail is zero. Otherwise let \(M=a_0\), and let \(j_*\le p\) be the last index in the initial constant-floor plateau:

$$
a_0=\cdots=a_{j_*}=M,
$$

with \(a_{j_*}>a_{j_*+1}\) when \(j_*<p\).

Put

$$
c_\rho=\frac{\arccos\rho}{\pi},
\qquad
\eta_\rho=\frac{1-2c_\rho}{4}>0.
$$

Theorem 3.2, applied to \(g+1/4\) on \([j_*,p]\), gives

$$
\mathbf T(g+\tfrac14,j_*,p)
\le
\int_{j_*}^{p}g(t)\,dt
-\eta_\rho(p-j_*).
$$

Define

$$
D_{\rm top}
=
Mj_*-\int_0^{j_*}g(t)\,dt,
$$

$$
D_{\rm cell}
=
\int_p^{p+1}g(t)\,dt
-\frac{a_p+a_{p+1}}2,
$$

and

$$
S_{\rm cvx}
=
\int_{p+1}^{B}g(t)\,dt
-\mathbf T(g+\tfrac14,p+1,B)
\ge0.
$$

The last inequality is Theorem 3.3. The complete tail follows from the precise compensation estimate

$$
\boxed{
S_{\rm cvx}+D_{\rm cell}
+\eta_\rho(p-j_*)
\ge
D_{\rm top}.
}
$$

Theorems 3.2–3.4 do not prove this uniformly. Theorem 3.2 supplies the explicit concave margin, Theorem 3.3 gives only \(S_{\rm cvx}\ge0\), and the explicit Theorem 3.4 margin may vanish. This is the first precise horizontal inequality still missing outside the small-hole sector.

## Promotion recommendation

The small-hole result may be promoted as a separate narrow sublemma, for example:

- **SHELL-low-interface-small-hole-tails — proved_internal:** every low shifted tail is bounded by its action integral when
  \[
  0<\rho<\omega_0,\qquad
  K(\omega_0-\rho)\ge\frac12+\frac{8\sqrt2}{15}.
  \]

The following must remain open:

- the low-interface tail inequality outside that sector;
- the full SHELL-weighted-lattice-fractional obligation;
- the finite range below the threshold;
- the spectral shell theorem, pending the independent completeness/count dependency.

The two typographical defects noticed during this review were fixed in the live incumbent. Neither affected the proof.
