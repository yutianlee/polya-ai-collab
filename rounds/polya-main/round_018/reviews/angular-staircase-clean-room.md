# Round 18 angular staircase: isolated clean-room review

## Verdict

**PASS.** Candidate C18 is true on the complete closed band stated in the
freeze. The fixed-channel comparison has the required direction, the only
possible modes give the proposed caps \(4,9,16,25\), every cap is paid
strictly at the proposed ratio splits, and \(k_5<U\) gives the asserted set
subtraction. **First unsupported implication: none.**

I verified before reconstruction that the SHA-256 hashes of the candidate,
candidate freeze, residual packet, residual freeze, spectral packet, Round 17
claim statement, Lorch card, and FLPS card are, respectively,
354e3bea...70e9, b4e4d71b...3f6c, 7c70440b...f11d9,
7f507b0b...c2ff, 6fde758c...bcb8, c23d8bd0...ae77,
85f9a009...ce4, and 27ec69e8...62a38, exactly as frozen.

## Independent spectral reconstruction

Write \(z=\pi/(1-\rho)\) and let \(\lambda_{\ell,n}\) be the shell eigenvalue
in angular channel \(\ell\), radial index \(n\). Since \(r^{-2}\ge1\) on the
shell, one-dimensional min--max comparison with the interval Dirichlet
operator gives

\[
 \lambda_{\ell,n}\ge n^2z^2+\ell(\ell+1).                 \tag{1}
\]

The Lorch bounds require a separate shell-to-ball argument. In the transformed
radial variable, the shell channel form is

\[
 a_\ell[u]=\int_\rho^1\bigl(|u'|^2+\ell(\ell+1)r^{-2}|u|^2\bigr)\,dr,
 \qquad u\in H_0^1(\rho,1).
\]

Extend \(u\) by zero on \((0,\rho)\). Its zero trace at \(\rho\) makes the
extension an \(H_0^1(0,1)\) function; it vanishes near the singular endpoint,
so its centrifugal integral is finite. Multiplying by any fixed
\(Y_{\ell m}/r\) places it in the same, not merely the global, ball angular
subspace. Both its \(L^2\) norm and form value are unchanged. Thus the shell
fixed-channel form domain embeds into the ball fixed-channel form domain, and
min--max, in the smaller-to-larger direction, yields

\[
 \lambda^{\rm shell}_{\ell,1}\ge
 \lambda^{\rm ball}_{\ell,1}=j_{\ell+1/2,1}^{\,2}.       \tag{2}
\]

This proves rather than assumes the channel preservation and inequality
direction. Lorch is used only with \(\nu=5/2,7/2,9/2>-1\), only for the first
positive zero of \(J_\nu\), and with its strict direction. The positive
prefactor in
\(\mathsf j_\ell(x)=\sqrt{\pi/(2x)}J_{\ell+1/2}(x)\) identifies these with
\(\ell=2,3,4\). Consequently those shell channels are absent for
\(K\le c_2=51/10\), \(K\le c_3=13/2\), and \(K\le c_4=15/2\), respectively.
No shell cross-product, higher radial zero, multiplicity, or Weyl assertion is
attributed to Lorch.

For the exact arithmetic below I reconstructed
\(157/50<\pi<22/7\). For the lower bound, Machin's identity
\(\pi/4=4\arctan(1/5)-\arctan(1/239)\), verified by the tangent addition
formula, and the alternating bounds give

\[
 \frac\pi4>4\left(\frac15-\frac1{375}\right)-\frac1{239}
 =\frac{70369}{89625}>\frac{157}{200};
\]

the last cross-product reserve is \(2675\). For the upper bound, polynomial
division and integration give the standard exact identity

\[
 0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}{7}-\pi.
\]

Now \(z\ge\pi+1/2>7/2\), so \(4z^2>z^2+30\). Hence (1) excludes every
\(n\ge2\) throughout \(K\le k_5\). It also excludes \(\ell=5\) at the closed
face \(K=k_5\), because its lower bound equals \(k_5^2\), and excludes every
\(\ell\ge6\). Strict spectral counting is essential at that equality. Thus
only the first radial modes for \(\ell=0,\ldots,4\) can occur, with full
multiplicities \(1,3,5,7,9\). Cross-order coincidences do not change the
argument: the orthogonal multiplicities add, and every eigenfrequency equal
to \(K\) is omitted simultaneously.

Set

\[
 q_m(\rho)=\max\{k_m(\rho),c_m\},\qquad m=2,3,4.
\]

Both sequences inside the maxima increase strictly, so \(q_2<q_3<q_4\).
Equations (1)--(2), including equality, give the successive strict-count caps

\[
 N_D\le4,\ 9,\ 16,\ 25
\]

on \(K\le q_2\), \(q_2<K\le q_3\), \(q_3<K\le q_4\), and \(q_4<K\le k_5\).
An interval is simply empty if its walls reverse. This max formulation also
settles every possible ordering or coincidence of \(51/10,13/2,15/2\) with
the \(k_m\) walls.

## Exact Weyl payments

Let \(W=(2/(9\pi))(1-\rho^3)K^3\). For
\(F_a(\rho)=(1-\rho^3)(z^2+a)^{3/2}\), direct differentiation shows that its
sign is the sign of

\[
 z^2(1+\rho)-a\rho^2.                                   \tag{3}
\]

For \(a=6,12,20\), this is positive on \(0\le\rho\le7/8\), since \(z^2>9\)
and \(9(1+\rho)-20\rho^2\) is at least the smaller endpoint value
\(25/16\). All differentiated quantities and denominators are positive.
Thus \(W(\rho,k_m(\rho))\) increases in \(\rho\) for \(m=2,3,4\), while
\(W(\rho,c)\) decreases in \(\rho\) for fixed \(c\).

For \(K>k_2\), the cap \(4\) is paid uniformly. Indeed
\(\rho_c<1/7\), \(1-\rho_c^3>342/343\), and
\(k_2(\rho_c)^3>73\), so

\[
 W(\rho_c,k_2)>\frac7{99}\frac{342}{343}73>4
\]

(the final numerator reserve after a common denominator is \(5562\)).

Crossing \(q_2\) means crossing both \(c_2\) and \(k_2\). For
\(\rho\le3/10\), payment at \(c_2\) follows from

\[
 \frac7{99}\frac{973}{1000}\left(\frac{51}{10}\right)^3>9,
\]

whose integer reserve is \(12{,}485{,}961\). For \(\rho\ge3/10\), use (3)
and payment at \(k_2\). At \(3/10\),
\(k_2^2>31999/1225\) and \(\sqrt{31999}>178\); hence

\[
 \frac7{99}\frac{973}{1000}\frac{5{,}695{,}822}{42{,}875}>9,
\]

with cross-product reserve \(592{,}618{,}642\). Both estimates hold at the
split, so both one-sided traces are covered.

Crossing \(q_3\) similarly crosses \(c_3,k_3\). On \(\rho\le1/2\),

\[
 \frac7{99}\frac78\left(\frac{13}{2}\right)^3
 =\frac{107653}{6336}>16
\]

with reserve \(6277\). On \(\rho\ge1/2\), (3) reduces to \(\rho=1/2\), where
\(k_3^2=4\pi^2+12>48\) and \(k_3>6\), giving
\(W>196/11>16\). Crossing \(q_4\) gives, on the two sides of \(1/2\),

\[
 \frac7{99}\frac78\left(\frac{15}{2}\right)^3
 =\frac{165375}{6336}>25
\]

(reserve \(6975\)), and, since \(k_4^2>56\) and \(k_4>37/5\),

\[
 W>\frac{101528}{3960}>25
\]

(reserve \(2528\)). Therefore every applicable count cap is strictly below
\(W\). The accepted Round 17 theorem supplies the complete closed portion
\(z\le K\le k_2\); the argument above supplies \(k_2<K\le k_5\), including
\(\rho=7/8\). This proves the exact closed C18 theorem.

## Upper floor and exact subtraction

It remains to prove, not assume, \(k_5<U\). The \(H_0\) branch ends before
\(\rho_c\): the frozen bound \(\rho_{HK}<94071/10^6\) and
\(\rho_c>7/51\) show this exactly. Thus only \(K_0\) and the seam are active
on the new ratio range.

For the \(K_0\) branch put \(x=\max\{\rho,1/2\}=\cos\theta\). From the FLPS
definition,
\(\pi G_1(x)=h(\theta)=\sin\theta-\theta\cos\theta
=\int_0^\theta t\sin t\,dt\), so
\(0<h\le\theta(1-x)\). Monotonicity of \(k_5\) lets us replace \(\rho\) by
\(x\). Since \(\theta\le\pi/3\), \(1-x\le1/2\), and
\(\sqrt{z^2+30}<z+15/z\),

\[
 \eta_\rho k_5(\rho)<\frac\pi3+\frac5{4\pi}
 <\frac{41}{28}<\frac{131}{75}<C_0.
\]

If \(S=\sqrt{K_0}\), its defining formula gives
\(\eta S^2-\sqrt a\,S-C_0=0\). Hence
\(\eta K_0=C_0+\sqrt{aK_0}>C_0\), proving \(k_5<K_0\).

For \(5/6\le\rho<7/8\), put \(t=1-\rho\le1/6\). Then
\(t^4k_5^2=t^2\pi^2+30t^4<65/216<2916=t^4U^2\), so \(k_5<U=54/t^2\).
The two one-sided arguments cover the \(5/6\) seam. Also
\(k_5<26<295^2\) on \(\rho\le7/8\), using \(z\le8\pi<176/7\), so the old
global frequency face is not crossed.

Therefore every point of
\(\mathcal C_{18}=\{\rho_c\le\rho<7/8,\ k_2<K\le k_5\}\) satisfies the
second predicate defining \(\mathcal D_{17}\), and
\(\mathcal C_{18}\subset\mathcal D_{17}\). Exact subtraction gives

\[
\mathcal D_{18}=
\{\rho_*<\rho<\rho_c,\ (2\rho)^{-1}<K<U\}
\cup
\{\rho_c\le\rho<7/8,\ k_5<K<U\}.
\]

The face \(K=k_5\) is newly owned, while \(K=k_2\), \(K=z\), \(K=U\), and
\(\rho=7/8\) retain their stated owners. The boxes \(B_0,B_1\) were already
absorbed into \(\mathcal C_{17}\), hence are not subtracted again.

Finally, the proposed counterexample walls lie outside the theorem:
\(k_5<2z\) by \(3z^2>30\), and \(k_6>k_5\). At equality, strict counting
would still exclude the corresponding \(n=2,\ell=0\) or \(\ell=6,n=1\)
lower-bound mode, but no conclusion beyond \(k_5\) is claimed.

## Closed-wall audit

The remaining mandatory walls introduce no hidden open endpoint. At
\(\rho=\rho_c\), the accepted theorem owns \(z\le K\le k_2\), and the new
proof starts with the strict inequality \(K>k_2\); the point \(K=k_2\) is
therefore neither lost nor counted twice. The estimates on both sides of
\(\rho=3/10\) and \(\rho=1/2\) are valid at the split itself, so their left
and right traces agree without a limiting argument. The spectral proof is
unchanged at \(\rho=5/6\); only the formula for \(U\) changes, and the two
strict comparisons above meet there. At \(\rho=7/8\), the complete theorem
remains valid through \(K=k_5\), while that ratio face is excluded from both
residual pieces by its old owner.

At \(K=z\) and \(K=k_2\) the accepted closed Round 17 statement applies.
At \(K=k_3\), \(K=k_4\), and \(K=k_5\), (1) excludes the channel whose
centrifugal lower wall is met exactly. At each \(K=c_m\), (2) and the strict
Lorch inequality exclude channel \(m\). Thus every such equality belongs to
the lower cap; only the strict right trace can incur the next multiplicity.
If a \(c_m\) lies below its \(k_m\), or the two happen to coincide, the
definition by \(q_m=\max\{c_m,k_m\}\) gives the same assignment and creates
no phantom subband. This explicitly covers radial indices \(n=1,2\),
orders \(\ell=0,\ldots,5\), and all remaining modes.

## Isolation statement

This verdict was reconstructed only from the eight hash-authenticated files
listed in the assignment. I did not inspect any Round 18 incumbent response,
source-audit review, computation, test, ledger, certificate, repository or Git
state/diff, judge/state synthesis, or any other review.
