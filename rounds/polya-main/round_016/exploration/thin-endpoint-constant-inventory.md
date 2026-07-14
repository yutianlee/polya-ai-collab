# Round 16 thin-endpoint exact-constant inventory

## Result and scope

**PASS for the requested finite exact-algebra and dependency-direction
inventory. This is not a PASS for the analytic endpoint theorem.** The frozen
packet was authenticated before the calculation:

~~~text
state/lemma_packets/SHELL-rho-one-endpoint-round16.md
SHA-256 5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09
~~~

All displayed constants (N1)--(N3), (P4)--(P9), (H9)--(H12), (S1)--(S4),
and (C1)--(C2) pass exact rational or symbolic reconstruction. The H5 and H8
inequality directions also pass, conditional on their explicitly listed
analytic hypotheses.

If this artifact were treated as a proof of the frozen claim, the answer
would be **FAIL / not established**. On the low side, the first unverified
analytic implication is the spectral/min--max majorization leading to (P1).
On the high side, the curvature facts (H2), the improper endpoint trace, and
the Stieltjes integrations needed for (H5) are not established by finite
arithmetic. The inequality in (N3) is a whitelisted analytic input, not an
executable check. Nothing here promotes a Round 16 result.

The companion program and tests verify finite algebra only:

~~~powershell
python computations/round16_verify_endpoint.py
python -m unittest computations.tests.test_round16_endpoint
~~~

## Dependency ledger

Only the five packet-whitelisted inputs were admitted.

| Whitelisted input | Use in this inventory |
|---|---|
| CONV-strict-counting and the exact separated spectrum | The strict ceiling conventions are reconstructed. No new spectral conclusion is asserted. |
| SHELL-sturm-liouville-completeness | Not needed for the finite ledger; it remains an analytic dependency of a full proof. |
| Radial min--max operator comparison | Its required direction is recorded in the P7 chain, but is not treated as proved here. |
| SHELL-phase-enclosures plus SHELL-annulus-phase-transfer | Only the all-domain proxy inequality in (N3) is quoted. Its normalization is checked exactly. |
| Domain-free action identities (N1)--(N2) | Independently rederived below. |

No Round 6 aggregate range or conclusion entered any calculation. No Round 5
product conclusion and no Round 11 bridge, endpoint, or old
\(P_{\mathcal A}<I\) conclusion entered. The accepted Round 15 statements
occur only in the separately labelled conditional arithmetic for (C1)--(C2),
never in either proposed endpoint piece.

## N1--N3: strict layers and normalization

Put \(x_n=n-\tfrac14\) and \(z=\mathcal A(y_\ell)+\tfrac14\). For
nonnegative action,

\[
\#\{n\ge1:x_n<\mathcal A(y_\ell)\}
=\#\{n\ge1:n<z\}
=\lceil z\rceil-1=q_\ell.
\]

At a proxy wall \(z=m\in\mathbb Z\), this is \(m-1\): the equality layer
\(n=m\) is excluded. Immediately above the wall it becomes \(m\). This
reproduces the strict bracket in (N1), including \(q_\ell=0\) when the action
is extended by zero beyond \(y=a\).

The finite sums may be exchanged exactly. Since

\[
M_\varepsilon(x_n)
=\#\{\ell\ge0:\varepsilon(\ell+\tfrac12)<R(x_n)\}
\]

and

\[
\sum_{\ell=0}^{M-1}\left(\ell+\frac12\right)=\frac{M^2}{2},
\]

one obtains

\[
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\ge1\\x_n<T}}M_\varepsilon(R(x_n))^2.
\]

The strict restriction \(x_n<T\) excludes the terminal inverse layer. The
closed half-integer count is independently

\[
M_\varepsilon(x)
=\max\left\{0,
\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil\right\}.
\]

At \(x/\varepsilon=m+\tfrac12\), it equals \(m\), so the half-integer layer
\(\ell=m\) is excluded and the jump occurs only above the wall.

For the continuous normalization, scaling \(y=ar\,s\) gives

\[
\int_0^{ar} yJ_r(y)\,dy
=(ar)^3\int_0^1s\bigl(\sqrt{1-s^2}-s\arccos s\bigr)\,ds.
\]

The two exact pieces are

\[
\int_0^1s\sqrt{1-s^2}\,ds=\frac13,
\qquad
\int_0^1s^2\arccos s\,ds
=\frac13\int_0^1\frac{s^3}{\sqrt{1-s^2}}\,ds
=\frac29,
\]

so the unit moment is \(1/9\). Viewing \(J_\rho\) as zero above
\(y=\rho a\), the layer-cake identity gives

\[
I=\int_0^a y\mathcal A(y)\,dy
=\frac{a^3(1-\rho^3)}{9\pi\varepsilon}
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\]

Finally, with \(K=a/\varepsilon\) and
\(1-(1-\varepsilon)^3=\varepsilon(3-3\varepsilon+\varepsilon^2)\),

\[
\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

This checks the equality in (N3); the preceding spectral inequality in (N3)
remains the whitelisted analytic transfer.

## P4--P9: low-piece exact algebra

Write \(s=a/\pi=N+t\). Strict radial counting gives
\(N=\lceil s\rceil-1\), so for \(a>\pi\), \(N\ge1\) and \(0<t\le1\).
At \(s=m\), the unique convention is \((N,t)=(m-1,1)\). Now

\[
\begin{aligned}
\frac{D(a)}{\pi^2}
&=\frac23(N+t)^3-N(N+t)^2
  +\frac{N(N+1)(2N+1)}6\\
&=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3},
\end{aligned}
\]

which is (P4). At every wall \(a=m\pi\),

\[
P4(m-1,1)=P4(m,0),
\]

so the excluded-wall value agrees with both one-sided limits even though the
radial index jumps only to the right.

Subtracting \(\tfrac25(N+t)^2\) and completing the square gives

\[
\frac{D(a)}{\pi^2}-\frac25s^2
=\frac{N^2}{10}
+N\left[\left(t-\frac25\right)^2+\frac1{150}\right]
+f(t),
\qquad
f(t)=\frac23t^3-\frac25t^2.
\]

Here

\[
f'(t)=2t\left(t-\frac25\right).
\]

Thus \(f\) decreases on \(0<t<2/5\), increases on \(2/5<t\le1\), and has
the exact minimum

\[
f(2/5)=-\frac8{375}.
\]

The integer lower screen is increasing for \(N\ge1\), and at its first value

\[
\frac1{10}+\frac1{150}-\frac8{375}=\frac{32}{375}>0.
\]

This proves the finite algebra behind (P5)--(P6), for every integer \(N\ge1\),
without sampling.

For the P7 sufficiency calculation, put

\[
u=\frac{b_n}{\varepsilon},\quad
z=\sqrt{u^2+\frac14}-\frac12,\quad M_n=\lceil z\rceil.
\]

Because \(b_n>0\) on every included radial branch,

\[
(M_n-1)M_n<u^2,
\qquad
M_n<z+1<u+1.
\]

Consequently

\[
\varepsilon^2M_n^2
<b_n^2+\varepsilon b_n+\varepsilon^2.
\]

The semicircle summand is strictly decreasing, hence its right-endpoint sum
satisfies

\[
\sum_{n=1}^N b_n
<\int_0^{a/\pi}\sqrt{a^2-\pi^2x^2}\,dx
=\frac{a^2}{4},
\qquad N<\frac a\pi.
\]

Therefore

\[
\varepsilon^2\mathcal P_\varepsilon(a)
<S_0(a)+\frac{\varepsilon a^2}{4}
  +\frac{\varepsilon^2a}{\pi}.
\]

The volume target in low-piece variables is

\[
\frac{I(a)}{\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\]

If (P7) holds, the preceding strict upper bound is at most
\(I(a)(1-\varepsilon)\), which is strictly below the exact target numerator
by \(I(a)\varepsilon^2/3>0\). This confirms the direction and sufficiency of
(P7), conditional on the required P1 spectral majorization.

On \(a\ge\pi\) and \(a\le\pi/(4\varepsilon)\), division by \(a^2\) yields

\[
\frac{2\varepsilon a}{3\pi}\le\frac16,
\qquad
\frac{\varepsilon}{4}=\frac{\varepsilon}{4},
\qquad
\frac{\varepsilon^2}{\pi a}
\le\frac{\varepsilon^2}{\pi^2}<\frac{\varepsilon^2}{9}.
\]

The first normalized term is increasing in \(a\) and is maximized at the
optical face; the last is decreasing in \(a\) and is maximized at \(a=\pi\).
Thus the two endpoint reductions have the stated directions even though
their maxima occur at opposite ends. This is (P8). Its displayed coefficient
is strictly increasing in \(\varepsilon\) because

\[
\frac d{d\varepsilon}
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)
=\frac14+\frac{2\varepsilon}{9}>0.
\]

At the closed endpoint,

\[
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0,
\]

which is (P9). Notice that the first P8 scaling is an equality on the common
optical face, but the \(\pi>3\) estimate in the last term remains strict.
More importantly, (P5) and the \(577/2880\) reserve give strict P7 slack
there.

For \(0\le a\le\pi\), strict radial counting gives \(N=0\), including both
\(a=0\) and \(a=\pi\). At \(a=0\) both sides of the desired spectral bound
are zero; for \(0<a\le\pi\), the product count is zero while the volume side
is positive.

## H5 and H8: dependency-direction audit

### H5

With the Stieltjes conventions in the packet,

\[
D_{\rm rad}=\int_0^T w(t)g(t)\,dt.
\]

Split at the actual, possibly ungridded \(\tau\). On \((0,\tau)\), write
\(w\,dt=dW\). Subject to the required improper trace
\(\lim_{t\downarrow0}g(t)W(t)=0\), integration by parts gives

\[
\int_0^\tau g\,dW
=g(\tau)W(\tau)-\int_0^\tau W\,dg\ge0,
\]

because \(W\ge0\) and \(dg\le0\). This is the correct direction: the
decreasing side contributes a term that may be dropped only after the
improper trace is justified.

On \((\tau,T)\), use \(w=1/4+\Psi'\):

\[
\int_\tau^T wg\,dt
=\frac{F(\tau)}4
+[g\Psi]_\tau^T-\int_\tau^T\Psi\,dg.
\]

Since \(dg\ge0\), \(-1/32\le\Psi\le3/32\), and
\(g(T)\ge g(\tau)\), the last two terms obey

\[
\begin{aligned}
[g\Psi]_\tau^T-\int_\tau^T\Psi\,dg
&\ge-\frac{g(T)}{32}-\frac{3g(\tau)}{32}
     -\frac3{32}\bigl(g(T)-g(\tau)\bigr)\\
&=-\frac{g(T)}8.
\end{aligned}
\]

Substitution of \(F(\tau)=\rho^2a^2\) and \(g(T)=2\pi\rho a\) gives

\[
D_{\rm rad}\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\]

Thus the H5 dependency directions are consistent. This calculation does not
prove \(W\ge0\), the curvature signs, the one-sided behavior at \(\tau\), or
the improper trace; those remain analytic obligations. No condition
\(\tau>1\) and no first-cell shortcut was used.

### H8

For any included layer let \(r=R(x_n)>0\). From (H6),

\[
M_\varepsilon(r)
=\max\left\{0,
\left\lceil\frac r\varepsilon-\frac12\right\rceil\right\}
<\frac r\varepsilon+\frac12.
\]

The inequality is strict even when \(r/\varepsilon=m+1/2\), because the
strict wall count is exactly \(m\). Squaring nonnegative quantities gives

\[
\varepsilon^2M_\varepsilon(r)^2
<r^2+\varepsilon r+\frac{\varepsilon^2}{4}
\le r^2+\varepsilon a+\frac{\varepsilon^2}{4}.
\]

Moreover

\[
J_{\rm rad}
=\left[T+\frac14\right]_<
<T+\frac14=\frac a\pi+\frac14.
\]

At the action radial wall \(T=n-1/4\), this gives \(J_{\rm rad}=n-1\), so
the equality layer is excluded. Summing the strict per-layer bounds and then
using the strict \(J_{\rm rad}\) bound gives

\[
\varepsilon^2\sum M_\varepsilon(R(x_n))^2
<\sum F(x_n)
+\left(\frac a\pi+\frac14\right)
 \left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\]

This verifies the H8 direction and its strictness without \(a\ge125\) or a
radial-count shortcut.

## H9--H12: high-piece screens and common-face strictness

On \(a\ge\pi/(4\varepsilon)\),

\[
\frac{D_{\rm rad}}{a^2}
\ge\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
\ge\frac{\rho^2}{4}-\rho\varepsilon
=\frac{(1-\varepsilon)(1-5\varepsilon)}4=:L(\varepsilon).
\]

The second inequality is an equality at the common face. Its derivative is

\[
L'(\varepsilon)=\frac{-6+10\varepsilon}{4}<0
\quad(0<\varepsilon\le1/8),
\]

and

\[
L(1/8)=\frac{21}{256}.
\]

Expanding the exact H8 envelope gives

\[
\frac{E}{a^2}
=\frac\varepsilon\pi
+\frac{\varepsilon^2}{4\pi a}
+\frac\varepsilon{4a}
+\frac{\varepsilon^2}{16a^2}.
\]

Using \(1/a\le4\varepsilon/\pi\) term by term gives

\[
\frac{E}{a^2}
\le
\frac\varepsilon\pi+\frac{\varepsilon^2}\pi
+\frac{\varepsilon^3}{\pi^2}+\frac{\varepsilon^4}{\pi^2}
=:U(\varepsilon).
\]

Every scaling inequality here is an equality at
\(a=\pi/(4\varepsilon)\); hence the non-strict sign in (H10) is necessary.
Nevertheless

\[
U'(\varepsilon)
=\frac{1+2\varepsilon}{\pi}
+\frac{3\varepsilon^2+4\varepsilon^3}{\pi^2}>0.
\]

Using the strict bound \(\pi>3\) at \(\varepsilon=1/8\),

\[
U(1/8)
<\frac1{24}+\frac1{192}+\frac1{4608}+\frac1{36864}
=\frac{193}{4096}.
\]

Therefore

\[
\frac{D_{\rm rad}-E}{a^2}
>\frac{21}{256}-\frac{193}{4096}
=\frac{143}{4096}>0.
\]

Combining this strict second inequality with the independently strict H8
ceiling gives precisely the direction of (H12):

\[
\varepsilon^2\sum M_\varepsilon(R(x_n))^2
<\sum F(x_n)+E
<\int_0^T F(t)\,dt.
\]

At the common face, H9 and H10 scaling are both equalities, but H12 remains
strict because (i) the angular ceiling/H7 chain is strict and (ii) the
\(\pi>3\) comparison leaves the exact \(143/4096\) reserve. At the corner
\((\varepsilon,a)=(1/8,2\pi)\), the face is also the radial wall \(m=2\),
owned by \((N,t)=(1,1)\); neither source of strictness disappears.

## S1--S4 exact stretch arithmetic

The two selected finite screens are

\[
P(\varepsilon)=\frac25-\frac16-\frac\varepsilon4
-\frac{\varepsilon^2}{9},
\]

and, for a rational lower bound \(\pi>p\),

\[
Q(\varepsilon;p)
=\frac{(1-\varepsilon)(1-5\varepsilon)}4
-\frac{\varepsilon+\varepsilon^2}{p}
-\frac{\varepsilon^3+\varepsilon^4}{p^2}.
\]

Exact Fraction reduction gives:

| Face | Bound used | Product screen | Complementary screen |
|---|---:|---:|---:|
| \(\varepsilon=1/7\), \(\rho=6/7\) | \(p=3\) | \(1723/8820\) | \(139/21609\) |
| \(\varepsilon=4/27\), \(\rho=23/27\) | \(p=333/106\) | \(12719/65610\) | \(162570113/235723844196\) |
| \(\varepsilon=3/20\), \(\rho=17/20\) | \(p=333/106\) | not the selected obstruction | \(-44729/20535000\) |
| \(\varepsilon=1/6\) | \(p=333/106\) | not the selected obstruction | \(-3983743/143712144\) |

The positive S1--S2 values verify only these coarse constants. The negative
S3--S4 lower screens mean only that this selected bounding route does not
close there: they are not spectral counterexamples and do not show the true
action difference is negative.

## C1--C2 conditional arithmetic

This section is conditional bookkeeping only. The exact square and coarse
third-envelope ceiling are

\[
295^2=87025,
\qquad
64<3456=54\cdot8^2<87025.
\]

Thus the packet's prospective ceiling is arithmetically consistent with its
four conditional envelope entries. Equality \(K=295^2\) is above the stated
strict bound \(K_0(5/6)<295^2\), but using that fact as a theorem requires the
separate conditional-envelope audit required by the packet. The reduction
factor is exactly

\[
\frac{200000}{295^2}
=\frac{8000}{3481}
=2+\frac{1038}{3481}>2.
\]

Neither (C1) nor (C2) is available for promotion here.

## Closed union, walls, branches, and faces

The following is an ownership inventory, not a substitute for the analytic
proof of either piece.

1. **Two-piece topology.** For every \(0<\varepsilon\le1/8\),
   \([0,\pi/(4\varepsilon)]\cup[\pi/(4\varepsilon),\infty)=[0,\infty)\).
   Both pieces include the optical face; there is no third piece.
2. **Zero and positive energy.** \(K=0\leftrightarrow a=0\) owns equality.
   Every \(K>0\leftrightarrow a>0\) transfer must preserve a strict comparison.
3. **Zero-count branch.** \(0\le a\le\pi\), including \(a=\pi\), has \(N=0\).
   The first positive radial branch is \(a>\pi\), \(n=1\).
4. **Product radial walls.** At every \(a=m\pi\), the wall is excluded and
   \((N,t)=(m-1,1)\). The left limit has \(t\uparrow1\); the right limit is
   \((m,t)\to(m,0^+)\); P4 is continuous across them.
5. **Product angular walls.** At
   \(b_n^2/\varepsilon^2=\ell(\ell+1)\), \(M_n=\ell\); the jump to
   \(\ell+1\) is immediately above the wall. The first positive angular
   branch is \(0<b_n^2/\varepsilon^2\le2\), where \(M_n=1\).
6. **Common corner.** At \((\varepsilon,a)=(1/8,2\pi)\), the common face is
   the \(m=2\) radial wall and is owned by \((N,t)=(1,1)\).
7. **Ratio faces.** The closed lower-ratio face is
   \(\rho=7/8\leftrightarrow\varepsilon=1/8\). The limit
   \(\rho\uparrow1\leftrightarrow\varepsilon\downarrow0\) is open;
   \(\varepsilon=0\) is never inserted into a denominator or domain.
8. **Legacy test faces.** \(\varepsilon=1/100,1/25,1/10,1/8\) all lie in
   the exact monotonicity interval. They are check faces only and import no
   conclusion from the theorem in which any one previously appeared.
9. **Action radial walls.** At \(n-1/4=T\), the \(n\)-th layer is excluded,
   and \(J_{\rm rad}=n-1<T+1/4=n\).
10. **Half-integer angular walls.** At
    \(R(n-1/4)/\varepsilon=m+1/2\), (H6) gives \(M_\varepsilon=m\); the jump
    occurs only above the wall.
11. **Phase-proxy walls.** At
    \(\mathcal A(y_\ell)+1/4=m\), (N1) gives \(q_\ell=m-1\); equality is
    excluded and the jump occurs only above the wall.
12. **Action geometry.** The outer cutoff \(y=a\), inner interface
    \(y=\rho a\), and curvature interface \(t=\tau\) must all be owned.
    The H5 split is at the actual \(\tau\), whether it lies below, on, or
    above a sawtooth grid point. Since \(W\) and \(\Psi\) are continuous
    primitives, both sides of every sawtooth jump are included without a
    special first cell.
13. **Improper and terminal traces.** A full proof must justify the
    \(t\downarrow0\) trace, the \(t=T\) trace, the one-sided data at \(\tau\),
    and every dropped nonnegative Stieltjes term. The executable ledger only
    checks the resulting endpoint arithmetic.
14. **Domains and safe algebra.** In the product piece, \(n\le N<a/\pi\)
    makes every included \(b_n^2\) positive. In the action piece, \(a>0\),
    \(r\in\{\rho,1\}>0\), and \(0\le y\le ar\) put every square root and
    arccosine argument in its real domain. The inverse obligation is exactly
    \(R:[0,T]\to[0,a]\). All divisions use \(\varepsilon>0\) and \(\pi>0\),
    and every squared ceiling comparison uses nonnegative sides. The separate
    case \(a=0\) avoids the degenerate arccosine quotient.
15. **Monotonic and equality faces.** P8 increases with \(\varepsilon\);
    H9 decreases; H10 increases. H10's scaling is non-strict and is exactly
    equal on the common face. Final strictness comes from the ceiling bounds
    and the positive reserves, not from changing that sign.
16. **Conditional ratio interfaces.** The later envelope must separately
    own \(\rho=\rho_*,1/16,5/6,7/8,99/100\). None is used in the two endpoint
    pieces except the target face \(7/8\).
17. **Conditional energy interfaces.** The later audit must own
    \(K=64,3456,295^2,200000,K_0(5/6)\). The accepted threshold faces, if
    used, are equality at \(K=54/\varepsilon^2\) on
    \(0<\varepsilon\le1/6\), \(K=32/\varepsilon^2\) on
    \(0<\varepsilon\le1/8\), \(K=24/\varepsilon^2\) on
    \(0<\varepsilon\le1/10\), and \(K=20/\varepsilon^2\) on
    \(0<\varepsilon\le1/25\). They are context-only here. This inventory
    checks only \(3456\), \(295^2\), and the reduction factor.

## Six mandatory dependency replacements

All six replacements are explicit in this reconstruction.

1. **No \(\tau>1\).** H5 uses global \(W\ge0\) and splits at the actual
   ungridded \(\tau\); no special first-cell argument occurs.
2. **No \(a\ge125\).** H8 uses only the exact strict count
   \(J_{\rm rad}<a/\pi+1/4\); no count below \(a/2\) occurs.
3. **No \(\rho\ge99/100\).** H9 substitutes exactly
   \(\rho=1-\varepsilon\).
4. **New high reserve.** The only high-piece power reserve is the exact
   \(143/4096\), not \(61/1400\).
5. **New low route.** The low ledger uses the exact zero-count range and
   \(D>(2/5)a^2\), not an old three-slab estimate.
6. **No Round 6 bridge.** Only the two inclusive pieces are inventoried; no
   Round 6 aggregate conclusion or intermediate coverage is invoked or
   extended.

No hidden use of \(\varepsilon\le1/100\), \(\rho\ge99/100\), \(a\ge125\),
or an old bridge scale was found in the finite derivations. The strongest
result of this artifact is the exact finite ledger above. It proves no
analytic endpoint domain, leaves the frozen claim unproved, and makes no
state, graph, packet, or promotion change.
