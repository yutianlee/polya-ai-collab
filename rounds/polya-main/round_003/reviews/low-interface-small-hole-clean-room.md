# Clean-room review: low-interface shifted tails in the small-hole sector

Historical note: this review validates the small-hole stepping-stone. A later independently reviewed incumbent closes the fixed-$\rho$ high-energy sector for every $0<\rho<1$.

## Independence and verdict

This is a clean-room reconstruction of `state/lemma_packets/SHELL-low-interface-small-hole.md`. I did not read the incumbent response or any new Round 3 response/review. I used the committed lemma packet, the already-audited source cards, and the exact published statements of FLPS Proposition 3.1, Theorem 3.4, Lemma 6.1, and Lemma 6.2. No state file was edited.

**Verdict: pass.** The theorem

$$
0<\rho<\omega_0,\qquad
K(\omega_0-\rho)\ge \frac12+\frac{8\sqrt2}{15},\qquad
x_0=r+\frac12<\rho K
$$

implies

$$
\mathcal T_r<2\int_{x_0}^{K}A_{\rho,K}(z)\,dz,
$$

and hence implies the stated non-strict inequality. All hypotheses of Theorem 3.4 are satisfied. There is no unsupported implication inside this shifted-tail lemma.

The endpoint $q=\mu$ requires one explicit correction: the first estimate for the interface loss is non-strict there because both sides are zero. The live packet now records this correctly. The final uniform estimate remains strict and the threshold constant is unchanged.

## 1. Parameters and elementary constants

Write

$$
\mu=\rho K,\qquad
x_0=r+\frac12,\qquad
A(z)=G_K(z)-G_\mu(z),
$$

and

$$
\omega_0=G_1(1/2)
=\frac{\sqrt3}{2\pi}-\frac16.
$$

The audited source gives $\omega_0>1/10$. It is also immediate that $\omega_0<1/2$. Hence $\rho<\omega_0$ implies

$$
\mu=\rho K<\frac K2.
$$

The advertised simpler sector is genuinely sufficient: if

$$
0<\rho<\frac1{10},\qquad
K\left(\frac1{10}-\rho\right)\ge C_*,
$$

then $\rho<\omega_0$ and

$$
K(\omega_0-\rho)>K(1/10-\rho)\ge C_*.
$$

## 2. Endpoint bookkeeping

For a low tail $x_0<\mu$, set

$$
n=\lfloor\mu-x_0\rfloor,\qquad
q=x_0+n,\qquad
B=\lceil K-x_0\rceil.
$$

Then $n,B\in\mathbb Z$, and

$$
q\le\mu<q+1.
$$

Because $\mu<K$,

$$
n\le\mu-x_0<K-x_0\le B,
$$

so the integrality of $n$ and $B$ gives $n<B$. Also

$$
x_0+B\ge K,
$$

and the zero extension of $G_K$ gives

$$
G_K(x_0+B)=0.
$$

Since $x_0$ is a half-integer, $q$ is exactly the largest half-integer in the tail grid not exceeding $\mu$. No replacement by $\lfloor\mu\rfloor$ is valid in general.

Finally, a low tail forces

$$
\mu>x_0\ge\frac12,
$$

so $\mu>1/2$ strictly.

## 3. Reconstruction of the split weights

Define

$$
a_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor,
\qquad
b_j=\left\lfloor G_K(x_0+j)+\frac14\right\rfloor.
$$

Since $0\le A\le G_K$, one has $0\le a_j\le b_j$. All terms with $j\ge B$ vanish. Therefore

$$
\frac{\mathcal T_r}{2}
=\frac12a_0+\sum_{j=1}^{B-1}a_j.
$$

If $n\ge1$, the proposed split equals

$$
\begin{aligned}
&\mathbf T(A(x_0+\cdot)+\tfrac14,0,n)
+\mathbf T(G_K(x_0+\cdot)+\tfrac14,n,B)\\
&=\frac12a_0+
\sum_{j=1}^{n-1}a_j
+\frac12(a_n+b_n)
+\sum_{j=n+1}^{B-1}b_j
+\frac12b_B.
\end{aligned}
$$

Here $b_B=0$, $(a_n+b_n)/2\ge a_n$, and $b_j\ge a_j$ for $j>n$. Thus this expression majorizes $\mathcal T_r/2$ with exactly the correct half-weights at the interface.

If $n=0$, there is no concave block. Directly,

$$
\frac{\mathcal T_r}{2}
\le \frac12b_0+\sum_{j=1}^{B-1}b_j+\frac12b_B
=\mathbf T(G_K(x_0+\cdot)+\tfrac14,0,B).
$$

No degenerate invocation of Proposition 3.1 is needed.

## 4. Concave head

On $0<z<\mu$,

$$
A''(z)
=\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}<0.
$$

Hence $A$ is concave on $[x_0,q]$, including the endpoint case $q=\mu$ by continuity. For $n\ge1$, Proposition 3.1 applied to

$$
h(t)=A(x_0+t)+\frac14
$$

gives

$$
\mathbf T(h,0,n)
\le\int_0^n h(t)\,dt
=\int_{x_0}^{q}A(z)\,dz+\frac n4.
$$

This accounts for the full positive $n/4$ cost of the quarter shift on the concave block.

## 5. Every hypothesis of Theorem 3.4

On $[n,B]$, put

$$
g(t)=G_K(x_0+t),
$$

using the zero extension for $x_0+t\ge K$. The endpoints $n,B$ are integers and $n<B$. Moreover:

1. **Non-negativity and terminal value.** $g\ge0$ and $g(B)=0$.
2. **Monotonicity.** For $x<K$,
   $$
   G_K'(x)=-\frac1\pi\arccos\frac xK\le0,
   $$
   and the zero extension is constant after $K$.
3. **Convexity.** For $x<K$,
   $$
   G_K''(x)=\frac1{\pi\sqrt{K^2-x^2}}>0.
   $$
   Since $G_K'(x)\to0$ as $x\uparrow K$, adjoining the constant zero branch preserves convexity.
4. **Global $\operatorname{Lip}_{1/2}$.** Since $0\le\arccos(x/K)\le\pi/2$ for $x\ge0$,
   $$
   |G_K'(x)|\le\frac12.
   $$
5. **Location of the improved-Lipschitz point.** Set
   $$
   t_*=\frac K2-x_0.
   $$
   Because
   $$
   x_0+n=q\le\mu=\rho K<K/2,
   $$
   one has $n<t_*$. Also $t_*\le K-x_0\le B$, so $t_*\in[n,B]$.
6. **$\operatorname{Lip}_{1/3}$ on $[t_*,B]$.** There $x_0+t\ge K/2$, and hence
   $$
   |G_K'(x_0+t)|
   \le\frac1\pi\arccos\frac12
   =\frac13.
   $$
7. **Value at the improvement point.** Direct substitution gives
   $$
   g(t_*)=G_K(K/2)=\omega_0K.
   $$

Thus Theorem 3.4 applies exactly and yields

$$
\mathbf T(g+\tfrac14,n,B)
\le\int_n^B g(t)\,dt
-\frac14\lfloor\omega_0K\rfloor.
$$

The same verification applies with the left endpoint $0$ when $n=0$.

## 6. Exact interface integral

For $n\ge1$, combining the head and tail integrals gives

$$
\int_{x_0}^{q}A(z)\,dz
+\int_q^{K}G_K(z)\,dz.
$$

Since $A=G_K-G_\mu$ below $\mu$ and $A=G_K$ above $\mu$, this equals

$$
\int_{x_0}^{K}A(z)\,dz
+\delta,
\qquad
\delta:=\int_q^\mu G_\mu(z)\,dz.
$$

For $n=0$, one has $q=x_0$, and the same identity follows from

$$
\int_{x_0}^{K}G_K(z)\,dz
=\int_{x_0}^{K}A(z)\,dz
+\int_{x_0}^{\mu}G_\mu(z)\,dz.
$$

Consequently both cases give

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta
-\frac{\lfloor\omega_0K\rfloor-n}{4}.
$$

## 7. Interface-loss bound, including (q=\mu)

Lemma 6.2 gives, for $q<z<\mu$,

$$
G_\mu(z)
<\frac{(\mu-z)^{3/2}}{3\sqrt\mu}.
$$

If $q<\mu$, integration yields

$$
\delta
<\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}.
$$

If $q=\mu$, the integration interval is empty and

$$
\delta=0
=\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}.
$$

Thus the uniform statement valid in both cases is

$$
0\le\delta
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}.
$$

Since $0\le\mu-q<1$ and $\mu>1/2$, one still has the strict final estimate

$$
\boxed{\delta<\frac{2\sqrt2}{15}.}
$$

For $q=\mu$ this is simply $0<2\sqrt2/15$; for $q<\mu$ it follows from the strict pointwise estimate, $\mu-q<1$, and $1/\sqrt\mu<\sqrt2$.

## 8. Strict threshold constants

Since $x_0\ge1/2$,

$$
n\le\mu-x_0\le\rho K-\frac12.
$$

For every real number $x$,

$$
\lfloor x\rfloor>x-1.
$$

Therefore

$$
\begin{aligned}
\lfloor\omega_0K\rfloor-n
&>\omega_0K-1-\left(\rho K-\frac12\right)\\
&=K(\omega_0-\rho)-\frac12.
\end{aligned}
$$

At the claimed closed threshold,

$$
K(\omega_0-\rho)
\ge\frac12+\frac{8\sqrt2}{15},
$$

so

$$
\lfloor\omega_0K\rfloor-n
>\frac{8\sqrt2}{15}
>4\delta.
$$

The first inequality remains strict even when the parameter threshold is attained, because $\lfloor x\rfloor>x-1$ is strict. The second is strict by the uniform interface bound. Hence

$$
\delta-\frac{\lfloor\omega_0K\rfloor-n}{4}<0,
$$

and finally

$$
\boxed{
\mathcal T_r
<2\int_{x_0}^{K}A_{\rho,K}(z)\,dz.
}
$$

## 9. Scope of the conclusion

The small-hole low-tail theorem is proved. Together with the already-separated high-tail lemma, it controls all shifted tails in this sector and therefore closes the coarse weighted-floor lattice inequality through the established multiplicity scaffold.

This does not establish spectral completeness, the finite spectral window, or any sector with $\rho\ge\omega_0$. Those remain separate obligations. No further unsupported implication occurs inside `SHELL-low-interface-small-hole` itself.
