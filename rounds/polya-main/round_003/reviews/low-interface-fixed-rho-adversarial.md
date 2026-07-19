# Adversarial Review: Fixed-Rho High-Energy Low-Interface Tails

Role: A4 adversarial reviewer  
Frozen artifact: rounds/polya-main/round_003/responses/low-interface-fixed-rho-incumbent.md  
Lemma packet: state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md  
Verdict: **pass for the stated fixed-rho high-energy obligation**

## Bottom line

I reconstructed the proof from the definition of the trapezoidal floor sum and the exact statements of Proposition 3.1, Theorem 1.4, Theorem 3.4, and Lemma 6.2 in the [published annulus paper](https://doi.org/10.1112/jlms.70425). I found no counterexample or missing hypothesis.

In particular, the proof survives all requested stress cases:

- \(n=0\), where the concave block must be omitted;
- no first floor drop, where \(p=n\) and Proposition 3.1 replaces Theorem 1.4;
- an immediate first drop, where \(p=0\);
- \(q=\mu\), where the interface loss is exactly zero;
- \(\mu-q\uparrow1\);
- \(q\) on either side of \(K/2\), including \(\rho=1/2\);
- \(K\eta_\rho\) on an integer wall;
- equality \(K=K_0(\rho)\);
- the limits \(\rho\downarrow0\) and \(\rho\uparrow1\), which are not claimed uniformly.

The first-floor-plateau estimate is valid. The shell action has a uniform curvature lower bound of order \(K^{-1}\), and equality of the endpoint floors then forces the initial plateau to have length strictly less than \(\sqrt{a_\rho K}\). The algebra defining \(M\) and the quadratic formula defining \(K_0(\rho)\) are also correct, including the otherwise easy-to-miss extra \(+1\) in \(C_0\).

The result remains limited to the coarse weighted lattice proxy at fixed \(\rho\) and sufficiently high energy. It is not a finite-window certificate, a separated-spectrum completeness proof, or a full shell Pólya theorem.

## 1. Imported theorem hypotheses

For integers \(a<b\), the source defines

$$
\mathbf T(g,a,b)
=\frac12\lfloor g(a)\rfloor
+\sum_{j=a+1}^{b-1}\lfloor g(j)\rfloor
+\frac12\lfloor g(b)\rfloor.
$$

The source results used here have the following exact content.

1. Proposition 3.1: if \(g\) is concave on an integer interval, then
   $$
   \mathbf T(g,a,b)\le\int_a^b g.
   $$
2. Theorem 1.4: if \(\alpha,\beta\in\mathbb Z\), \(\alpha<\beta\), \(g\) is decreasing, concave, and \(\operatorname{Lip}_c\) on \([\alpha,\beta]\) for some \(c\in(0,1)\), and an integer \(p\in[\alpha,\beta)\) satisfies
   $$
   \lfloor g(\alpha)\rfloor
   =\lfloor g(p)\rfloor
   >\lfloor g(p+1)\rfloor,
   $$
   then
   $$
   \mathbf T(g,\alpha,\beta)
   \le\int_\alpha^\beta g
   -\frac{1-c}{2}(\beta-p).
   $$
3. Theorem 3.4: if \(a,b\in\mathbb Z\), \(g\) is decreasing, convex, and \(\operatorname{Lip}_{1/2}\) on \([a,b]\), \(g(b)=0\), and there is a real \(t\in[a,b]\) such that \(g\) is \(\operatorname{Lip}_{1/3}\) on \([t,b]\), then
   $$
   \mathbf T(g+\tfrac14,a,b)
   \le\int_a^b g-\frac14\lfloor g(t)\rfloor.
   $$

The point \(t\) in Theorem 3.4 need not be an integer. No source hypothesis has been silently discarded in the incumbent's applications.

## 2. Exact tail representation and integer split

Fix

$$
x_0=r+\frac12<\mu=\rho K,
\qquad
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
B=\lceil K-x_0\rceil.
$$

Then \(n,B\in\mathbb Z\), \(0\le n<B\), and

$$
q\le\mu<q+1.
$$

With \(A=G_K-G_\mu\), extended in the stated way, the shifted tail has the exact form

$$
\frac{\mathcal T_r}{2}
=\mathbf T(A(x_0+\cdot)+\tfrac14,0,B).
$$

Indeed, \(x_0+B\ge K\), so the terminal floor is

$$
\left\lfloor A(x_0+B)+\frac14\right\rfloor=0.
$$

This also covers the integer endpoint \(K-x_0\in\mathbb Z\), where \(x_0+B=K\) and \(A(K)=0\).

For \(n\ge1\), additivity of \(\mathbf T\) and \(A\le G_K\) give

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T(A(x_0+\cdot)+\tfrac14,0,n)
+\mathbf T(G_K(x_0+\cdot)+\tfrac14,n,B).
$$

At \(n\), the two half endpoint weights majorize the original full \(A\)-sample, so no interface endpoint is lost. If \(n=0\), the concave term is absent and direct pointwise majorization gives only the convex block. Neither Proposition 3.1 nor Theorem 1.4 is invoked on a degenerate interval.

## 3. Concave-head hypotheses and first drop

Direct differentiation gives, for \(0<z<\mu\),

$$
G_a'(z)=-\frac1\pi\arccos\frac za,
\qquad
G_a''(z)=\frac1{\pi\sqrt{a^2-z^2}},
$$

and hence

$$
A'(z)<0,
\qquad
A''(z)
=\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}<0.
$$

Thus

$$
h(t)=A(x_0+t)+\frac14
$$

is decreasing and concave on \([0,n]\), including \(q=\mu\) by continuity at the endpoint. Moreover,

$$
-A'(z)
=\frac1\pi\left(\arccos\frac zK-\arccos\frac z\mu\right)
$$

is increasing from \(0\) to

$$
c_\rho=\frac{\arccos\rho}{\pi}\in(0,\tfrac12),
$$

so \(h\in\operatorname{Lip}_{c_\rho}\), with the required constant in \((0,1)\).

If the initial floor level first drops after \(p\), then

$$
\lfloor h(0)\rfloor=\lfloor h(p)\rfloor
>\lfloor h(p+1)\rfloor,
\qquad 0\le p<n,
$$

and every hypothesis of Theorem 1.4 holds. If no drop occurs, \(p=n\), Theorem 1.4 is not applicable, and Proposition 3.1 gives the same unified formula with zero improvement:

$$
\mathbf T(h,0,n)
\le
\int_0^n A(x_0+t)\,dt+\frac n4
-\frac{1-c_\rho}{2}(n-p).
\tag{1}
$$

## 4. Attempt to break the first-floor-plateau estimate

The equality of the endpoint floors on the initial plateau and monotonicity of \(h\) imply

$$
0\le A(x_0)-A(x_0+p)<1.
\tag{2}
$$

The strict upper bound is valid even on an integer wall: two real numbers in the same half-open floor cell \([m,m+1)\) differ by strictly less than one.

Let \(\sigma=-A'\). Then

$$
\sigma'(z)
=\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}.
$$

For fixed \(z\), set

$$
F_z(a)=\frac1{\sqrt{a^2-z^2}}-\frac1a.
$$

For \(a>z\),

$$
F_z'(a)
=\frac1{a^2}-\frac{a}{(a^2-z^2)^{3/2}}<0.
$$

Since \(\mu<K\), it follows that \(F_z(\mu)\ge F_z(K)\), and therefore

$$
\sigma'(z)
\ge
\frac1\pi\left(\frac1\mu-\frac1K\right)
=\frac{1-\rho}{\pi\rho K}
=:\kappa.
\tag{3}
$$

This verifies the terse monotonicity argument in the incumbent. Since \(\sigma(0)=0\), (3) gives \(\sigma(z)\ge\kappa z\). Hence, for \(0\le x<y\le\mu\),

$$
A(x)-A(y)
=\int_x^y\sigma(z)\,dz
\ge\frac\kappa2(y^2-x^2)
\ge\frac\kappa2(y-x)^2.
\tag{4}
$$

The case \(y=\mu\) follows by taking a limit from below; the singularity in \(\sigma'\) is harmless. Applying (4) with \(x=x_0\) and \(y=x_0+p\), and using (2), yields

$$
p<\sqrt{\frac2\kappa}
=\sqrt{\frac{2\pi\rho}{1-\rho}K}
=\sqrt{a_\rho K}.
\tag{5}
$$

This remains valid in the two extreme plateau patterns:

- no drop: \(p=n\), so (5) proves that the whole sampled head has length \(O_\rho(\sqrt K)\);
- immediate drop: \(p=0\), for which (5) is automatic and Theorem 1.4 supplies its maximal head improvement.

I found no way to reverse (5). Its strictness comes from the same-floor inequality (2); the curvature comparison itself is allowed to be non-strict.

## 5. Convex-tail theorem and the point \(s\)

Set

$$
s=\max\{q,K/2\},
\qquad
t_*=s-x_0.
$$

Because \(q=x_0+n\le s<K\),

$$
n\le t_*<K-x_0\le B.
$$

Thus \(t_*\in[n,B]\). The zero-extended function

$$
g(t)=G_K(x_0+t)
$$

is decreasing, convex, and \(\operatorname{Lip}_{1/2}\) on \([n,B]\), and \(g(B)=0\). Since \(x_0+t\ge K/2\) for \(t\ge t_*\),

$$
|g'(t)|
=\frac1\pi\arccos\frac{x_0+t}{K}
\le\frac13,
$$

so \(g\) is \(\operatorname{Lip}_{1/3}\) on \([t_*,B]\). This reconstructs every hypothesis of Theorem 3.4.

The gain at \(t_*\) is controlled as follows.

- If \(0<\rho\le1/2\), then \(q\le\mu\le K/2\), so \(s=K/2\) and
  $$
  G_K(s)=K G_1(1/2)=K\eta_\rho.
  $$
- If \(1/2<\rho<1\), then both \(q\) and \(K/2\) are at most \(\mu=\rho K\), so \(s\le\rho K\). Since \(G_K\) is decreasing,
  $$
  G_K(s)\ge G_K(\rho K)=K G_1(\rho)=K\eta_\rho.
  $$

At \(\rho=1/2\), the first branch applies with equality, including \(q=K/2\).

Strictly speaking, Theorem 3.4 first gives the stronger bound

$$
\mathbf T(g+\tfrac14,n,B)
\le\int_n^B g-\frac14\lfloor G_K(s)\rfloor.
$$

Floor monotonicity gives

$$
\lfloor G_K(s)\rfloor\ge\lfloor K\eta_\rho\rfloor,
$$

which has the correct sign after multiplication by \(-1/4\). Therefore

$$
\mathbf T(g+\tfrac14,n,B)
\le\int_n^B g-\frac14\lfloor K\eta_\rho\rfloor.
\tag{6}
$$

This intermediate floor-monotonicity line is implicit in the incumbent but valid. It also handles an exact integer wall \(K\eta_\rho\in\mathbb Z\).

## 6. Interface mismatch, including \(q=\mu\)

The sum of the two block integrals is

$$
\int_{x_0}^{q}A(z)\,dz+\int_q^K G_K(z)\,dz
=\int_{x_0}^K A(z)\,dz+\delta,
$$

where

$$
\delta=\int_q^\mu G_\mu(z)\,dz.
$$

Writing \(d=\mu-q\in[0,1)\), Lemma 6.2 gives the endpoint-safe estimate

$$
0\le\delta
\le\frac{2d^{5/2}}{15\sqrt\mu}.
$$

If \(q=\mu\), both sides are zero; the first comparison must indeed be non-strict. If \(q<\mu\), the source bound is strict away from the endpoint. Since the existence of a low tail implies

$$
\mu>x_0\ge\frac12,
$$

and \(d<1\), in all cases

$$
\delta<\frac{2\sqrt2}{15}.
\tag{7}
$$

Thus the case \(\mu-q\uparrow1\) does not exhaust the uniform allowance, and \(q=\mu\) creates no hidden positive interface term.

## 7. Reconstruction of \(M\)

The head cost in (1) is

$$
H=\frac n4-\frac{1-c_\rho}{2}(n-p).
$$

With

$$
d_\rho=1-2c_\rho=\frac{2\arcsin\rho}{\pi}>0,
$$

one has

$$
4H
=n-2(1-c_\rho)(n-p)
=-d_\rho n+(1+d_\rho)p.
$$

Combining this with (6) therefore gives exactly

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
$$

where

$$
M
=\lfloor K\eta_\rho\rfloor
+d_\rho n-(1+d_\rho)p
=\lfloor K\eta_\rho\rfloor+d_\rho(n-p)-p.
\tag{8}
$$

For \(n=0\), the bookkeeping choice \(p=0\) reduces (8) to \(M=\lfloor K\eta_\rho\rfloor\), exactly as the convex-only argument requires.

Since \(p\le n\), \(d_\rho>0\), and (5) is strict,

$$
M
\ge\lfloor K\eta_\rho\rfloor-p
>\lfloor K\eta_\rho\rfloor-\sqrt{a_\rho K}
>K\eta_\rho-1-\sqrt{a_\rho K}.
\tag{9}
$$

The last inequality remains strict on an integer wall because \(\lfloor x\rfloor>x-1\) for every real \(x\), including \(x\in\mathbb Z\).

## 8. The quadratic threshold and equality \(K=K_0(\rho)\)

Let \(y=\sqrt K\). The threshold condition needed in (9) is

$$
\eta_\rho y^2-\sqrt{a_\rho}\,y\ge C_0,
\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

Because \(\eta_\rho>0\) for every fixed \(0<\rho<1\), the positive root of

$$
\eta_\rho y^2-\sqrt{a_\rho}\,y-C_0=0
$$

is

$$
y_0
=\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}.
$$

Consequently \(K\ge y_0^2=K_0(\rho)\) is exactly sufficient. At equality \(K=K_0(\rho)\), (9) still gives

$$
M>
K\eta_\rho-1-\sqrt{a_\rho K}
=C_0-1
=\frac{8\sqrt2}{15}.
$$

Combining this with (7) yields

$$
M>\frac{8\sqrt2}{15}>4\delta.
$$

The strictness is therefore preserved at the threshold itself. There is no lost equality case and no off-by-one error in \(C_0\).

## 9. Endpoint regimes and falsification summary

- **\(\rho\downarrow0\).** One has \(c_\rho\uparrow1/2\), \(d_\rho\downarrow0\), and \(a_\rho\downarrow0\), but for every fixed positive \(\rho\), \(c_\rho\in(0,1)\), \(d_\rho>0\), and the proof is valid. For sufficiently small \(\rho\), there may be no low tail at \(K=K_0(\rho)\); then this part is vacuous and the high-tail lemma covers all starts.
- **\(\rho\uparrow1\).** Both \(a_\rho\) and \(1/\eta_\rho\) diverge, so \(K_0(\rho)\) diverges. The theorem explicitly makes no uniform thin-shell claim.
- **Ordinary versus strict floors.** The proved tail estimate concerns the ordinary-floor coarse proxy. The strict positive-integer proxy and the optimized transferred proxy can inherit the bound only through the already-established pointwise domination in the weighted scaffold; this review does not convert a numerical Bessel count into a certificate.

As a supplementary counterexample search, I sampled the plateau, head, convex-tail, interface, \(M\), and direct shifted-tail inequalities at and above the stated threshold across both \(\rho<1/2\) and \(\rho>1/2\), including dedicated \(q=\mu\), \(n=0\), no-drop, immediate-drop, near-unit interface-gap, and integer-wall examples. No numerical failure appeared. This sampling is diagnostic only; the verdict rests on the analytic reconstruction above.

## Final verdict

**Pass.** The incumbent proves the packet's fixed-\(\rho\), high-energy low-interface tail statement with the displayed explicit threshold. Combined with the previously discharged high-angular tails and the weighted scaffold, it establishes the coarse weighted lattice bound for every fixed \(0<\rho<1\) once \(K\ge K_0(\rho)\).

No stronger spectral conclusion should be promoted from this review.
