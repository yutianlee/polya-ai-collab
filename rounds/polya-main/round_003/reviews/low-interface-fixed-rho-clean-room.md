# Clean-room review: fixed-\(\rho\) high-energy low-interface tails

## Verdict

**PASS.** The boxed low-interface tail estimate in `SHELL-low-interface-fixed-rho-high-energy.md` follows from the stated versions of Proposition 3.1, Theorem 1.4, Theorem 3.4, and Lemma 6.2. The first-drop, no-drop, immediate-drop, and \(n=0\) branches all close. The curvature estimate, the margin algebra, and the displayed positive-root formula for \(K_0(\rho)\) are correct. I found no unsupported implication in the proof of the exact boxed tail statement.

This reconstruction used only the two named lemma packets and the two permitted source cards. It did not use numerical sampling or any incumbent response/review.

## 1. Elementary facts about the action

For \(0<z<a\), direct differentiation gives

\[
G_a'(z)=-\frac1\pi\arccos\frac za,
\qquad
G_a''(z)=\frac1{\pi\sqrt{a^2-z^2}}.
\]

Also \(G_a(az)=aG_1(z)\). On \([0,\mu]\), with \(A=G_K-G_\mu\), set

\[
\sigma(z)=-A'(z)
=\frac1\pi\left(\arccos\frac zK-\arccos\frac z\mu\right).
\]

Then \(A\) is decreasing and concave there, because

\[
A''(z)=\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}<0.
\]

Moreover

\[
\sigma'(z)=\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}>0,
\]

so \(\sigma\) increases from \(0\) to

\[
\sigma(\mu)=\frac{\arccos(\mu/K)}\pi=c_\rho.
\]

Thus \(A+1/4\) really is decreasing, concave, and \(\operatorname{Lip}_{c_\rho}\) on every head interval used in the proof. Since \(0<\rho<1\), one has \(0<c_\rho<1/2<1\), as required by Theorem 1.4.

The zero extension of \(G_K\) is decreasing and convex on \([0,\infty)\): its left derivative tends to zero at \(K\), matching the derivative of the zero extension. It is globally \(\operatorname{Lip}_{1/2}\), and it is \(\operatorname{Lip}_{1/3}\) on \([K/2,\infty)\), since

\[
|G_K'(z)|=\frac1\pi\arccos(z/K)\le\frac13
\quad(K/2\le z\le K).
\]

## 2. The integer split, including \(n=0\)

Let

\[
n=\lfloor\mu-x_0\rfloor,\qquad q=x_0+n,
\qquad B=\lceil K-x_0\rceil.
\]

The low-interface hypothesis gives \(x_0<\mu<K\), hence

\[
q\le\mu<q+1,\qquad 0\le n<B,
\qquad x_0+B\ge K.
\]

In particular \(B\) is a positive integer and all samples with index at least \(B\) contribute zero, because \(A=0\) at and beyond \(K\) and \(\lfloor1/4\rfloor=0\). Therefore

\[
\frac{\mathcal T_r}{2}
=\frac12\left\lfloor A(x_0)+\frac14\right\rfloor
+\sum_{j=1}^{B-1}\left\lfloor A(x_0+j)+\frac14\right\rfloor.
\]

For \(n\ge1\), splitting the two trapezoidal sums at \(n\) gives the correct majorant. At the shared sample \(j=n\), if

\[
a=\left\lfloor A(q)+\frac14\right\rfloor,
\qquad b=\left\lfloor G_K(q)+\frac14\right\rfloor,
\]

then \(b\ge a\), so the two half endpoint weights contribute \((a+b)/2\ge a\), which majorizes the full original sample. Every later sample is also majorized because \(A\le G_K\).

When \(n=0\), there is no head and no shared full-weight sample. Directly replacing \(A\) by \(G_K\) in the single trapezoidal tail gives

\[
\frac{\mathcal T_r}{2}
\le \mathbf T\left(G_K(x_0+\cdot)+\frac14,0,B\right).
\]

Thus the separate \(n=0\) formula is necessary and correct.

## 3. First floor drop and no-drop branch

Assume \(n\ge1\), let \(h(t)=A(x_0+t)+1/4\), and write \(m_j=\lfloor h(j)\rfloor\). The sequence \((m_j)\) is nonincreasing.

If its first departure from \(m_0\) occurs at \(p+1\), then \(0\le p<n\) and

\[
\lfloor h(0)\rfloor=\lfloor h(p)\rfloor
>\lfloor h(p+1)\rfloor.
\]

All hypotheses of Theorem 1.4 hold on the integer interval \([0,n]\). It yields

\[
\mathbf T(h,0,n)
\le \int_0^n h(t)\,dt
-\frac{1-c_\rho}{2}(n-p).
\]

If there is no drop on \(0,\ldots,n\), the proof sets \(p=n\) and uses Proposition 3.1, not Theorem 1.4. This gives the same displayed formula with zero improvement. Consequently both genuine branches give

\[
\mathbf T(h,0,n)
\le \int_0^n A(x_0+t)\,dt+\frac n4
-\frac{1-c_\rho}{2}(n-p).
\]

This also covers the immediate-drop case \(p=0\). For \(n=0\), taking \(p=0\) only as bookkeeping produces a zero head contribution; no concave theorem is being applied to a degenerate interval.

## 4. Quantitative no-shelf estimate

In every branch, including the formal no-drop choice \(p=n\), one has \(m_0=m_p\). Since \(h(0)\ge h(p)\) and two real numbers with the same ordinary floor differ by less than one,

\[
0\le A(x_0)-A(x_0+p)<1.
\]

The strict inequality remains true at floor walls; if the larger value itself is an integer, monotonicity plus equality of floors can only reduce the possible difference.

For \(0<z<\mu\), the function

\[
z\longmapsto
\frac1{\sqrt{\mu^2-z^2}}-\frac1{\sqrt{K^2-z^2}}
\]

is increasing. Hence

\[
\sigma'(z)\ge
\frac1\pi\left(\frac1\mu-\frac1K\right)
=\frac{K-\mu}{\pi K\mu}
=:\kappa=\frac{1-\rho}{\pi\rho K}.
\]

Since \(\sigma(0)=0\), it follows that \(\sigma(z)\ge\kappa z\). For \(0\le x<y\le\mu\), by continuity at \(y=\mu\) if needed,

\[
A(x)-A(y)=\int_x^y\sigma(z)\,dz
\ge\frac\kappa2(y^2-x^2)
\ge\frac\kappa2(y-x)^2.
\]

Taking \(x=x_0\) and \(y=x_0+p\le q\le\mu\) gives

\[
\frac\kappa2p^2<1,
\qquad
p<\sqrt{\frac2\kappa}
=\sqrt{\frac{2\pi\rho}{1-\rho}K}
=\sqrt{a_\rho K}.
\]

This is valid for \(p=n\) (no drop), \(p=0\) (immediate drop), and \(q=\mu\).

## 5. Theorem 3.4 at \(s=\max\{q,K/2\}\)

Let

\[
g(t)=G_K(x_0+t),\qquad
s=\max\{q,K/2\},\qquad t_*=s-x_0.
\]

Because \(q=x_0+n\), \(q\le\mu<K\), and \(K/2<K\),

\[
n\le t_*<K-x_0\le B.
\]

Thus \(t_*\in[n,B]\), including when \(n=0\). On \([n,B]\), \(g\) is nonnegative, decreasing, convex, \(\operatorname{Lip}_{1/2}\), and \(g(B)=0\). Since \(x_0+t\ge s\ge K/2\) for \(t\ge t_*\), it is \(\operatorname{Lip}_{1/3}\) on \([t_*,B]\). The exact source-card statement of Theorem 3.4 permits any \(t\in[a,b]\); \(t_*\) need not be an integer.

The lower bound at the improved-Lipschitz point is also correct. If \(\rho\le1/2\), then \(q\le\mu\le K/2\), so \(s=K/2\). If \(\rho>1/2\), then both \(q\) and \(K/2\) are at most \(\rho K\), so \(s\le\rho K\). Scaling and monotonicity therefore give in both cases

\[
g(t_*)=G_K(s)
\ge K G_1\!\left(\max\{\rho,1/2\}\right)
=K\eta_\rho.
\]

Theorem 3.4 first gives a gain \(-\tfrac14\lfloor g(t_*)\rfloor\). Since the floor is monotone, weakening that gain to \(-\tfrac14\lfloor K\eta_\rho\rfloor\) is valid, including when \(K\eta_\rho\) is an integer. Hence

\[
\mathbf T\left(G_K(x_0+\cdot)+\frac14,n,B\right)
\le\int_n^B G_K(x_0+t)\,dt
-\frac14\lfloor K\eta_\rho\rfloor.
\]

## 6. Assembly and the algebra for \(M\)

Put \(L=\lfloor K\eta_\rho\rfloor\). The two integral blocks satisfy

\[
\int_0^n A(x_0+t)\,dt
+\int_n^B G_K(x_0+t)\,dt
=\int_{x_0}^K A(z)\,dz+\delta,
\]

where

\[
\delta=\int_q^\mu G_\mu(z)\,dz.
\]

The same identity holds for \(n=0\), with the first integral absent and \(q=x_0\).

The remaining head and tail terms are

\[
\frac n4-\frac{1-c_\rho}{2}(n-p)-\frac L4.
\]

Writing \(d_\rho=1-2c_\rho\), direct expansion gives

\[
\begin{aligned}
L-n+2(1-c_\rho)(n-p)
&=L+(1-2c_\rho)n-(2-2c_\rho)p\\
&=L+d_\rho n-(1+d_\rho)p\\
&=L+d_\rho(n-p)-p.
\end{aligned}
\]

Thus, exactly as claimed,

\[
\frac{\mathcal T_r}{2}
\le\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=L+d_\rho(n-p)-p.
\]

For \(n=0\), \(p=0\) and this reduces to \(M=L\), so the unified formula does not hide a lost head term.

Since

\[
d_\rho=1-\frac{2\arccos\rho}{\pi}
=\frac{2\arcsin\rho}{\pi}>0
\]

and \(n-p\ge0\), the no-shelf estimate yields

\[
M\ge L-p
>L-\sqrt{a_\rho K}
>K\eta_\rho-1-\sqrt{a_\rho K}.
\]

Both strict inequalities are sound: the first uses \(p<\sqrt{a_\rho K}\), and the second uses \(\lfloor x\rfloor>x-1\), including at integer \(x\).

## 7. Interface loss and the explicit threshold

Here \(q\ge x_0\ge1/2>0\), so the stated consequence of Lemma 6.2 applies. Also \(0\le\mu-q<1\). A low-interface tail has \(\mu>x_0\ge1/2\), hence \(\mu>1/2\). Therefore

\[
0\le\delta
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}
<\frac{2\sqrt2}{15}.
\]

If \(q=\mu\), this is simply \(\delta=0\); if \(q<\mu\), strictness follows already from \(\mu-q<1\) and \(\mu>1/2\).

To check the threshold, put \(y=\sqrt K\). The desired inequality is

\[
\eta_\rho y^2-\sqrt{a_\rho}\,y-C_0\ge0.
\]

Because \(\eta_\rho>0\), its unique positive root is

\[
y_+=\frac{\sqrt{a_\rho}
+\sqrt{a_\rho+4\eta_\rho C_0}}{2\eta_\rho}.
\]

Thus \(K_0(\rho)=y_+^2\) is exactly the displayed threshold, and every \(K\ge K_0(\rho)\) satisfies

\[
K\eta_\rho-\sqrt{a_\rho K}\ge C_0.
\]

With \(C_0=1+8\sqrt2/15\), one obtains even at \(K=K_0(\rho)\)

\[
M> K\eta_\rho-1-\sqrt{a_\rho K}
\ge\frac{8\sqrt2}{15}
>4\delta.
\]

Substitution in the assembled estimate proves the strict inequality

\[
\frac{\mathcal T_r}{2}<\int_{x_0}^K A(z)\,dz,
\]

and hence the stated non-strict target.

## 8. Endpoint and falsification audit

- **\(n=0\):** the head is absent; Theorem 3.4 applies on \([0,B]\), \(p=0\), and \(M=L\).
- **No floor drop:** Proposition 3.1 is used with \(p=n\); Theorem 1.4 is not misapplied at \(p=n\). The curvature estimate still controls the full shelf length.
- **Immediate drop:** \(p=0\) satisfies Theorem 1.4 exactly and the shelf estimate is trivial.
- **\(q=\mu\):** \(\delta=0\); all derivative inequalities extend to the head endpoint by continuity.
- **\(0<\mu-q<1\):** Lemma 6.2 supplies precisely the needed half-integer split loss; no replacement by \(\lfloor\mu\rfloor\) occurs.
- **Either side of \(K/2\):** the maximum defining \(s\) ensures both \(t_*\ge n\) and the \(1/3\)-Lipschitz tail.
- **\(\rho=1/2\):** \(s=K/2\) and the lower bound for \(g(t_*)\) is equality.
- **A floor wall:** monotonicity of the ordinary floor validates the split and the gain; \(\lfloor x\rfloor>x-1\) remains strict when \(x\) is integral.
- **\(K=K_0(\rho)\):** strictness is retained through the shelf and floor estimates, so threshold equality is covered.
- **\(K-x_0\in\mathbb Z\):** \(x_0+B=K\) and \(g(B)=0\); otherwise \(x_0+B>K\) and the zero extension gives the same endpoint.
- **\(\rho\downarrow0\) or \(\rho\uparrow1\):** the theorem is pointwise for each fixed \(0<\rho<1\). Both \(a_\rho\) and \(\eta_\rho\) are positive there, so \(K_0(\rho)\) is finite; no uniform endpoint claim is made.
- **Strict versus ordinary counting:** for every positive input, the strict positive-integer count is at most the ordinary floor, and the optimized slack is at most \(1/4\). Thus the coarse ordinary-floor tail is a legitimate majorant; integer walls only improve the strict proxy.

The later weighted consequence still uses its separately named high-angular tail result and dimension-reduction scaffold. Within the present clean-room scope, the low-interface input supplied to that reduction is fully proved.
