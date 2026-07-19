# Adversarial Review: Thin-Shell Product Range and Obstruction

Role: A4 adversarial reviewer  
Frozen artifact: rounds/polya-main/round_005/responses/thin-shell-product-incumbent.md  
Lemma packet: state/lemma_packets/SHELL-thin-product-low-optical.md  
Verdict: **PASS**

## Bottom line

I independently reconstructed both logically distinct claims:

1. the positive low-optical-width estimate is a genuine theorem about the shell counting function;
2. the negative high-width statement is only a theorem about failure of the product majorant.

Both are correct. The operator comparison has the right direction, all radial and angular walls use the strict convention, the angular multiplicity is exactly \(M_n^2\), the radial margin and integral bounds are correct, and the constants close with substantial room at

$$
\varepsilon=\frac1{100},
\qquad
a=\pi,\quad4\pi,\quad\frac{\pi}{4\varepsilon}.
$$

The general wall obstruction and the separate arbitrarily thin family are valid. The lower bound on the fixed-\(\rho\) threshold is also correct and proves non-overlap. I found no blocking or nonblocking correctness issue in the corrected frozen incumbent.

## 1. Min--max direction and the exact majorant

For the shell \((1-\varepsilon,1)\), the transformed radial block is

$$
L_\ell
=-\frac{d^2}{dr^2}
+\frac{\ell(\ell+1)}{r^2}
$$

with Dirichlet endpoints. Because \(r\le1\),

$$
\frac{\ell(\ell+1)}{r^2}\ge\ell(\ell+1),
$$

so, in the form sense,

$$
L_\ell
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1).
$$

The comparison operator has eigenvalues

$$
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1),
\qquad n=1,2,\ldots.
$$

The min--max principle therefore gives

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
\tag{1}
$$

This is the direction required for an upper count: if the actual shell eigenvalue satisfies \(\lambda_{\ell,n}<K^2\), then its lower comparison value is also strictly below \(K^2\). With \(a=\varepsilon K\), this forces

$$
n\pi<a,
\qquad
\ell(\ell+1)
<
\frac{a^2-n^2\pi^2}{\varepsilon^2}.
\tag{2}
$$

Thus the set counted by the shell is a subset of the product-index set. Reversing (1) would invalidate the proof, but no reversal occurs.

## 2. Strict radial and angular walls

The number of positive integers with \(n\pi<a\) is

$$
N
=
\max\left\{
0,\left\lceil\frac a\pi\right\rceil-1
\right\}.
$$

At \(a=m\pi\), this gives \(N=m-1\); the \(n=m\) radial mode is excluded exactly as strict spectral counting requires.

For \(1\le n\le N\), put

$$
T_n^2
=
\frac{a^2-n^2\pi^2}{\varepsilon^2}.
$$

The positive root of \(x(x+1)=T_n^2\) is

$$
\alpha_n
=\sqrt{T_n^2+\frac14}-\frac12.
$$

The number of nonnegative integers satisfying the strict angular inequality is

$$
M_n
=
\#\{\ell\ge0:\ell(\ell+1)<T_n^2\}
=\lceil\alpha_n\rceil.
\tag{3}
$$

At an angular wall \(T_n^2=p(p+1)\), one has \(\alpha_n=p\) and hence \(M_n=p\). The permitted indices are exactly

$$
\ell=0,\ldots,p-1.
$$

The endpoint \(\ell=p\) is not inadvertently included. Away from a wall, (3) is the ordinary greatest-integer inversion of the increasing map \(\ell\mapsto\ell(\ell+1)\).

The exact angular multiplicity is

$$
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2.
$$

Consequently

$$
N_D(A_{1-\varepsilon,1},K^2)
\le
\mathcal P_\varepsilon(a)
:=
\sum_{n=1}^{N}M_n^2.
\tag{4}
$$

Cross-\(\ell\) degeneracies do not alter (4), because the direct-sum multiplicities add. This verifies the majorant before any analytic relaxation is made.

## 3. Angular-rounding inequalities

For \(T>0\), let

$$
\alpha=\sqrt{T^2+\frac14}-\frac12,
\qquad M=\lceil\alpha\rceil.
$$

Since \(M-1<\alpha\), one has

$$
(M-1)M<T^2,
$$

and therefore

$$
M^2<T^2+M.
$$

Also

$$
M<\alpha+1
=\sqrt{T^2+\frac14}+\frac12
<T+1.
$$

It follows that

$$
M^2<T^2+T+1.
\tag{5}
$$

For the lower side, \(\alpha>T-\tfrac12\). If \(T\ge1\),

$$
M^2\ge\alpha^2
>
\left(T-\frac12\right)^2
>
T^2-T.
$$

If \(0<T<1\), then \(T^2-T<0<M^2\). Hence the actually available lower bound is strict:

$$
M^2>T^2-T.
\tag{6}
$$

The packet records the harmless weak form \(T^2-T\le M^2\); the incumbent is entitled to use the strict summed inequality later.

With

$$
b_n=\sqrt{a^2-n^2\pi^2},
\quad
S_0=\sum b_n^2,
\quad
B=\sum b_n,
$$

(5)--(6) give

$$
\mathcal P_\varepsilon(a)
<
\frac{S_0}{\varepsilon^2}
+\frac{B}{\varepsilon}+N,
\tag{7}
$$

and, when \(N\ge1\),

$$
\mathcal P_\varepsilon(a)
>
\frac{S_0}{\varepsilon^2}
-\frac{B}{\varepsilon}.
\tag{8}
$$

When \(N=0\), both sides of (8) are zero, so only the non-strict statement holds. Every later use of (8) is at a radial wall with \(N=Q-1\ge2\). Both inequality directions and all strict signs actually used in the proof are valid.

## 4. Recalculation of \(D(a)\) and \(B(a)\)

Let

$$
I(a)=\frac{2a^3}{3\pi},
\qquad
D(a)=I(a)-S_0(a).
$$

Write

$$
\frac a\pi=N+t,\qquad0<t\le1.
$$

At a radial wall \(a=m\pi\), the strict convention gives \(N=m-1\) and \(t=1\). Since

$$
S_0
=
Na^2-\frac{\pi^2N(N+1)(2N+1)}6,
$$

direct expansion yields

$$
\boxed{
D(a)
=
\pi^2
\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
}
\tag{9}
$$

At a radial wall, the new summand has value zero, so (9) is continuous. Between walls \(N\) is constant and

$$
D'(a)
=\frac{2a^2}{\pi}-2aN
=2at>0.
$$

Thus

$$
D(a)\ge D(\pi)=\frac{2\pi^2}{3}
\qquad(a\ge\pi).
\tag{10}
$$

Moreover, \(N\ge a/\pi-1\), so

$$
D(a)\ge\frac{\pi^2N^2}{2}
\ge\frac{(a-\pi)^2}{2}.
\tag{11}
$$

For the square-root sum, the function

$$
x\longmapsto\sqrt{a^2-\pi^2x^2}
$$

is decreasing. Hence

$$
\begin{aligned}
B(a)
&\le
\int_0^{a/\pi}
\sqrt{a^2-\pi^2x^2}\,dx\\
&=\frac{a^2}{4}.
\end{aligned}
\tag{12}
$$

Finally \(N\le a/\pi\). The exact formula, its wall behavior, and both coarse bounds are correct.

## 5. Reduction to the sufficient inequality

The shell Weyl quantity is

$$
W_\varepsilon(a)
=
\frac{I(a)}{\varepsilon^2}
\left(
1-\varepsilon+\frac{\varepsilon^2}{3}
\right).
\tag{13}
$$

Substituting \(S_0=I-D\) into the upper majorant (7), the condition

$$
\frac{S_0}{\varepsilon^2}
+\frac{B}{\varepsilon}+N
\le W_\varepsilon(a)
$$

is equivalent to

$$
D
\ge
\varepsilon(I+B)
+\varepsilon^2
\left(N-\frac I3\right).
\tag{14}
$$

The term \(-\varepsilon^2I/3\) is favorable. Dropping it and using (12) and \(N\le a/\pi\) yields the stronger sufficient condition

$$
\boxed{
D(a)
\ge
\varepsilon
\left(
\frac{2a^3}{3\pi}+\frac{a^2}{4}
\right)
+\frac{\varepsilon^2a}{\pi}.
}
\tag{15}
$$

There is no sign error in this reduction. Since (7) is strict, proving the non-strict condition (15) is enough for the desired non-strict shell inequality.

## 6. Audit of the positive range and endpoint constants

### \(0\le a\le\pi\)

Here \(N=0\). The product majorant and the strict shell count are both zero. In particular:

- at \(a=0\), both sides of the target are zero;
- at \(a=\pi\), the first radial comparison mode is exactly at the endpoint and is excluded.

No limiting argument from \(a>\pi\) is needed.

### \(\pi<a\le4\pi\)

The right side of (15) is increasing in \(a\) and in \(\varepsilon\). Its maximum on this rectangle occurs at

$$
a=4\pi,\qquad\varepsilon=\frac1{100},
$$

where it equals

$$
\frac1{100}
\left(
\frac{128\pi^2}{3}+4\pi^2
\right)
+\frac4{10000}
=
\frac{7\pi^2}{15}+\frac1{2500}.
\tag{16}
$$

This is strictly smaller than \(2\pi^2/3\), while (10) gives \(D\ge2\pi^2/3\). Thus the estimate remains valid immediately above \(a=\pi\), at every intervening radial wall, and at \(a=4\pi\).

### \(4\pi\le a\le\pi/(4\varepsilon)\)

Since \(a\ge4\pi\),

$$
\frac{(a-\pi)^2}{2}\ge\frac{9a^2}{32}.
$$

After division of the right side of (15) by \(a^2\),

$$
\frac{2\varepsilon a}{3\pi}
+\frac{\varepsilon}{4}
+\frac{\varepsilon^2}{\pi a}
\le
\frac16+\frac1{400}+\frac1{40000\pi^2}
<
\frac9{32}.
\tag{17}
$$

The first bound uses \(a\le\pi/(4\varepsilon)\), the second uses \(\varepsilon\le1/100\), and the third uses \(a\ge4\pi\). Equality at

$$
a=\frac{\pi}{4\varepsilon}
$$

is allowed. At the corner \(\varepsilon=1/100\), this endpoint is \(a=25\pi\); the inequalities in (17) still have a large positive margin.

The three intervals cover the entire claimed range with no gap. Therefore the positive shell statement is proved.

## 7. General radial-wall obstruction

Fix \(0<\varepsilon<1\) and an integer

$$
Q>\frac9{4\varepsilon},
$$

and set \(a=Q\pi\). Strict radial counting gives \(N=Q-1\). From (9),

$$
D_Q
=\pi^2
\left(
\frac{Q^2}{2}+\frac Q6
\right),
\qquad
I=\frac{2\pi^2Q^3}{3}.
$$

Also

$$
B(Q\pi)
=
\pi\sum_{n=1}^{Q-1}\sqrt{Q^2-n^2}
<
\pi Q(Q-1).
$$

Using the lower majorant (8),

$$
\begin{aligned}
\varepsilon^2
\bigl(\mathcal P_\varepsilon-W_\varepsilon\bigr)
>
&\frac{2\pi^2}{3}
\varepsilon\left(1-\frac{\varepsilon}{3}\right)Q^3\\
&-\pi^2
\left(
\frac{Q^2}{2}+\frac Q6
\right)
-\varepsilon\pi Q(Q-1).
\end{aligned}
\tag{18}
$$

After division by \(\pi^2Q\), the leading positive term is

$$
\frac23\varepsilon
\left(1-\frac{\varepsilon}{3}\right)Q^2
>
\frac49\varepsilon Q^2
>
Q.
$$

The total subtracted quantity is less than

$$
\frac Q2+\frac16+\frac{Q-1}{3}
=\frac{5Q}{6}-\frac16
<Q.
$$

Here \(\varepsilon/\pi<1/3\), and the threshold forces the integer \(Q\ge3\). Thus (18) is strictly positive:

$$
\boxed{
\mathcal P_\varepsilon(Q\pi)
>W_\varepsilon(Q\pi).
}
$$

This verifies the obstruction for infinitely many exact radial walls at every fixed positive \(\varepsilon<1\).

## 8. Independent arbitrarily thin family

The family

$$
\varepsilon=\frac1Q,\qquad a=Q\pi,\qquad Q\ge4,
$$

does not satisfy the sufficient hypothesis \(Q>9/(4\varepsilon)\); it is a separate, sharper construction. For \(n=1,\ldots,Q-1\), put

$$
x_n=\pi^2Q^2(Q^2-n^2).
$$

The strict lower angular estimate gives

$$
\mathcal P
>
\sum_{n=1}^{Q-1}x_n
-\pi Q^2(Q-1).
$$

The exact difference between the polynomial sum and \(W\) is

$$
\frac{\pi^2Q^3(3Q-7)}{18}.
$$

Therefore

$$
\mathcal P-W
>
\pi Q^2
\left[
\frac{\pi Q(3Q-7)}{18}-(Q-1)
\right].
$$

Using \(\pi>3\), the bracket is greater than

$$
\frac{3Q^2-13Q+6}{6}>0
\qquad(Q\ge4).
$$

Thus the exact thin family is valid. For \(Q\ge100\), it lies within the thinness condition \(\varepsilon\le1/100\), but its optical width \(Q\pi\) is four times the positive lemma's endpoint \(Q\pi/4\). There is no contradiction with the positive result.

## 9. Audit of the \(G_1\) bound and \(K_0\)

For \(0<\varepsilon\le1/2\), \(\rho=1-\varepsilon\ge1/2\), so

$$
\eta_\rho=G_1(1-\varepsilon).
$$

Since \(G_1'(s)=-\arccos(s)/\pi\) and \(G_1(1)=0\),

$$
\eta_\rho
=
\frac1\pi
\int_0^\varepsilon\arccos(1-v)\,dv.
$$

For \(0\le v\le1/2\),

$$
\arccos(1-v)
=2\arcsin\sqrt{\frac v2}
\le
\frac{2\pi}{3}\sqrt{\frac v2}.
$$

Integration gives the slightly stronger bound

$$
\eta_\rho
\le
\frac{4}{9\sqrt2}\varepsilon^{3/2}
<
\frac{\varepsilon^{3/2}}3.
\tag{19}
$$

The explicit fixed-\(\rho\) threshold has the form

$$
K_0(\rho)
=
\left(
\frac{\sqrt{A_\rho}
+\sqrt{A_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
\qquad
A_\rho=\frac{2\pi(1-\varepsilon)}{\varepsilon}.
$$

The second square root is strictly larger than \(\sqrt{A_\rho}\), so

$$
K_0(\rho)>\frac{A_\rho}{\eta_\rho^2}.
$$

Using (19),

$$
\varepsilon K_0(1-\varepsilon)
>
\frac{18\pi(1-\varepsilon)}{\varepsilon^3}
\ge
\frac{9\pi}{\varepsilon^3}.
\tag{20}
$$

This verifies the claimed lower bound on the optical width where the existing high-energy theorem begins.

## 10. Non-overlap and the proxy/shell distinction

Let

$$
Q_0
=
\left\lfloor\frac9{4\varepsilon}\right\rfloor+1.
$$

Then \(Q_0>9/(4\varepsilon)\) and

$$
Q_0
\le
\frac9{4\varepsilon}+1.
$$

The inequality can be equality when \(9/(4\varepsilon)\) is an integer, which is why the corrected incumbent uses \(\le\). For \(0<\varepsilon\le1/2\),

$$
\pi Q_0
\le
\pi\left(\frac9{4\varepsilon}+1\right)
<
\frac{9\pi}{\varepsilon^3}
<
\varepsilon K_0(1-\varepsilon).
$$

Thus an exact product-majorant failure occurs before the current fixed-\(\rho\) theorem begins. Separately, the proved positive product range ends at

$$
a=\frac{\pi}{4\varepsilon},
$$

which is also far below the lower bound (20). The two existing positive results do not overlap.

The logical implications are

$$
N_D\le\mathcal P_\varepsilon
\quad\text{and}\quad
\mathcal P_\varepsilon>W_\varepsilon.
$$

These do **not** imply \(N_D>W_\varepsilon\). The obstruction disproves only the attempt to finish the shell theorem through

$$
N_D\le\mathcal P_\varepsilon\le W_\varepsilon.
$$

The incumbent states this distinction correctly. No shell counterexample has been produced.

## Final verdict

**PASS.** The positive range is a valid partial shell theorem, and the negative statement is a valid obstruction to this particular product majorant. Every requested wall, constant, multiplicity, and threshold check closes. The corrected endpoint wording for \(N=0\) and for \(Q_0\) is exact.

This result must be promoted only as a partial thin-shell lemma. It does not close the full \(\rho\uparrow1\) endpoint and does not falsify the shell Pólya inequality.
