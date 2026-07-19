# General dimension, Round 16: continuous geometric reduction and hard-face closure

Date: 18 July 2026

Status: Round 15 identifies the exact defect on the hard open
\(B=Q=1\), first-floor no-drop chamber and moves it monotonically to the
first phase, branch, or owner-activity endpoint.  This note removes the
favorable strict-floor reserve, minimizes the remaining scalar exactly in a
continuous spatial variable, and reduces the whole endpoint problem to one
grid-free geometric inequality.  It also proves a positive rational reserve
on the suspected \(q=3,r=1,n=2\) double face.  The geometric inequality is
not yet proved, so WP2 and the all-dimensional theorem remain open.

## 1. Exact endpoint and floor-free scalar

Use

\[
 G_b(s)=\frac{\sqrt{b^2-s^2}-s\arccos(s/b)}{\pi}
 \quad(0\le s<b),
 \qquad G_b(s)=0\quad(s\ge b),
\]

and the extended tail primitive

\[
 J_b(s)=\int_s^bG_b(u)\,du\quad(0\le s<b),
 \qquad J_b(s)=0\quad(s\ge b).
 \tag{1.1}
\]

Retain the notation of Round 15:

\[
 q=r+n,\qquad a=q+\bar\alpha,\qquad
 G_K(z)=\frac34,
\]

\[
 y=z-q,\qquad M=[y]_<,\qquad
 \eta=y-M\in(0,1].
 \tag{1.2}
\]

Round 15 proves that the open-side endpoint scalar is

\[
 \Omega_{\rm end}
 =2\{J_K(r)-J_a(r)\}-(1+2n+2M),
 \tag{1.3}
\]

and that every original open point satisfies

\[
 D_{A_\alpha}(r)=\Omega(\alpha)>\Omega_{\rm end}.
 \tag{1.4}
\]

Since \(n=q-r\) and \(M=z-q-\eta\), (1.3) is exactly

\[
 \Omega_{\rm end}
 =\underbrace{2\{J_K(r)-J_a(r)\}-2(z-r)-1}
 _{\displaystyle \Omega_0(r)}+2\eta.
 \tag{1.5}
\]

Thus \(\Omega_0\) is obtained by discarding, rather than estimating, the
strictly favorable fractional reserve \(2\eta\).

## 2. Endpoint domain without discrete grid variables

Put

\[
 A(s)=G_K(s)-G_a(s).
 \tag{2.1}
\]

Every Round 15 endpoint satisfies

\[
 \boxed{
 a\ge2,\qquad K-a>\pi,\qquad
 A(a-1)\ge\frac34,\qquad z>2.}
 \tag{2.2}
\]

Indeed, \(q=r+n\ge2\) and \(a\ge q\).  The endpoint occurs no later than
the owner-dimensional activity wall, so

\[
 K-a\ge
 \frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}}>\pi,
 \qquad
 \kappa_4=\frac34,
 \quad \kappa_5=2.
 \tag{2.3}
\]

It also occurs no later than the phase wall, hence \(A(q)\ge3/4\).
Because \(a\le q+1\), one has \(a-1\le q\); since \(A\) is decreasing,
this gives \(A(a-1)\ge A(q)\ge3/4\).  Finally the original outer action at
\(q\) is greater than \(3/4\), so its inverse point obeys \(z>q\ge2\).

The domain (2.2) is an enlargement: it forgets the integer or half-integer
grid, \(q,n\), endpoint ownership, and the upper \(B=1\) action wall.  A
proof on (2.2) therefore proves all genuine endpoints.

## 3. Strict convex minimization

For real \(s\in[0,z]\), define

\[
 E_0(s)=2\{J_K(s)-J_a(s)\}-2(z-s)-1.
 \tag{3.1}
\]

The ball derivative is

\[
 G_b'(s)=-\frac1\pi\arccos\frac{s}{b}
 \quad(0<s<b).
 \tag{3.2}
\]

Consequently \(A\) is continuous and strictly decreasing on \([0,z]\),
including across \(s=a\), and

\[
 E_0'(s)=2\{1-A(s)\},
 \qquad
 E_0''(s)=-2A'(s)>0
 \tag{3.3}
\]

away from the harmless joined formula at \(s=a\).  The one-sided
derivatives agree there.

By (2.2),

\[
 A(0)=\frac{K-a}{\pi}>1,
 \qquad
 A(z)=\frac34-G_a(z)\le\frac34<1.
 \tag{3.4}
\]

There is therefore a unique \(x\in(0,z)\) such that

\[
 A(x)=1,
 \tag{3.5}
\]

and \(x\) is the global minimizer of \(E_0\).  In particular,

\[
 \Omega_0(r)=E_0(r)\ge E_0(x).
 \tag{3.6}
\]

Define the grid-free geometric functional

\[
 \boxed{
 F(K,a):=J_K(x)-J_a(x)-(z-x),
 \qquad A(x)=1,\quad G_K(z)=\frac34.}
 \tag{3.7}
\]

Then (1.4)--(1.5) and (3.6) give the proved reduction

\[
 \boxed{
 D_{A_\alpha}(r)>
 \Omega_{\rm end}
 \ge 2F(K,a)-1+2\eta.}
 \tag{3.8}
\]

Hence the single analytic lemma

\[
 \boxed{F(K,a)\ge\frac12}
 \tag{G}
\]

on (2.2) proves the hard \(B=1\) branch, with the strict reserve
\(2\eta\).  Unlike the rejected Round 11--12 scalar, (G) follows from the
exact defect after discarding only a favorable term and minimizing a convex
function.  No ratio partition or grid split is introduced.

The right endpoint in (3.4) is load-bearing.  The tempting assertion
\(A(a)<1\) is false on some large-\(q\) branch endpoints; values above one
occur.  The universally correct comparison is \(A(z)<1\).

## 4. Exact two-parameter calculus for the open lemma

For \(0\le s<b\), put

\[
 P_b(s):=\frac{\partial J_b(s)}{\partial b}
 =\frac{b^2\arccos(s/b)-s\sqrt{b^2-s^2}}{2\pi b},
 \tag{4.1}
\]

and set \(P_b(s)=0\) when \(s\ge b\).  If
\(\theta=\arccos(z/K)\), implicit differentiation of
\(G_K(z)=3/4\) gives

\[
 z_K=\frac{\sin\theta}{\theta}.
 \tag{4.2}
\]

The \(x\)-derivatives cancel because \(A(x)=1\).  Thus the exact envelope
derivatives are

\[
 \boxed{
 F_K=P_K(x)-\frac{\sin\theta}{\theta},
 \qquad F_a=-P_a(x).}
 \tag{4.3}
\]

### Lemma 4.1 (strict radial monotonicity)

Throughout (2.2),

\[
 \boxed{F_K>0.}
 \tag{4.4}
\]

Set

\[
 h(t)=\sin t-t\cos t,\qquad
 u(t)=\frac{\sin t}{t},\qquad
 p(t)=t-\sin t\cos t.
\]

Let \(w\) be the inverse point \(G_K(w)=1\), which exists because
\(K/\pi>1\), and write \(\beta=\arccos(w/K)\).  Since
\(Kh(\beta)/\pi=1\), direct substitution in (4.1) gives

\[
 P_K(w)=\frac{p(\beta)}{2h(\beta)}
 =\frac{\int_0^\beta t\sin t\,u(t)\,dt}
 {\int_0^\beta t\sin t\,dt}.
 \tag{4.5}
\]

Put \(y=h(t)\) and \(U(y)=u(h^{-1}(y))\).  Then

\[
 U_y=-\frac{h(t)}{t^3\sin t}.
\]

The function \(U\) is strictly convex.  Indeed, this is equivalent to

\[
 \frac d{dt}\frac{h(t)}{t^3\sin t}<0,
\]

which, after clearing positive factors, is

\[
 Q(t):=3\sin^2t-t\sin(2t)-t^2>0.
\]

Here \(Q(0)=0\) and

\[
 Q'(t)=4\cos t\,(\sin t-t\cos t)>0
 \qquad(0<t<\pi/2).
\]

Jensen's inequality applied to (4.5) now gives

\[
 P_K(w)>U\!\left(\frac{h(\beta)}2\right)
 >U\!\left(\frac{3h(\beta)}4\right)
 =\frac{\sin\theta}{\theta},
 \tag{4.6}
\]

because \(U\) is decreasing and the two level equations imply
\(h(\theta)=3h(\beta)/4\).  Finally \(G_K(x)=1+G_a(x)\ge1\), so
\(x\le w\); and \(P_K(s)\) is decreasing in \(s\).  Thus (4.3) and (4.6)
prove (4.4), including the possible case \(x\ge a\).

It follows that fixed-\(a\) minimization moves \(K\) to the first active
lower boundary

\[
 K=\max\{a+\pi,k(a)\},
 \qquad A_{k(a),a}(a-1)=\frac34.
 \tag{4.7}
\]

On the radial boundary \(K=a+\pi\), the closure has \(x=0\) and

\[
 F=\frac{K^2-a^2}{8}-z,
 \qquad
 \frac{dF}{da}=\frac\pi4-\frac{\sin\theta}{\theta}<0.
 \tag{4.8}
\]

The last sign is analytic.  The function

\[
 z(\theta)=\frac{3\pi\cos\theta}
 {4(\sin\theta-\theta\cos\theta)}
\]

is decreasing.  At \(c=117/100\), put

\[
 S_-=c-\frac{c^3}{6}+\frac{c^5}{120}-\frac{c^7}{5040},
 \qquad
 C_+=1-\frac{c^2}{2}+\frac{c^4}{24}
 -\frac{c^6}{720}+\frac{c^8}{40320}.
\]

The alternating remainders give \(\sin c>S_-\) and \(\cos c<C_+\).
Exact rational arithmetic gives

\[
 \frac{S_-}{C_+}-c-\frac{33}{28}
 =\frac{8867689904954607}{779709274332548525}>0,
\]

\[
 \frac{S_-}{c}-\frac{11}{14}
 =\frac{695788735359}{560000000000000}>0.
\]

Together with \(\pi<22/7\), the first inequality proves
\(\tan c-c>3\pi/8\), hence \(z(c)<2\).  Thus \(z>2\) implies
\(\theta<c\).  The second inequality gives

\[
 \frac{\sin c}{c}>
 \frac{11}{14}>\frac\pi4.
\]

Since sinc is decreasing on this interval, (4.8) follows.

On the action boundary \(A(a-1)=3/4\), let

\[
 \gamma=\arccos\frac{a-1}{K},
 \qquad
 \phi=\arccos\frac{a-1}{a}.
\]

Implicit differentiation gives

\[
 K'(a)=\frac{\gamma+\sin\phi-\phi}{\sin\gamma},
 \tag{4.9}
\]

so its exact tangential derivative is

\[
 \boxed{
 \left(P_K(x)-\frac{\sin\theta}{\theta}\right)
 \frac{\gamma+\sin\phi-\phi}{\sin\gamma}
 -P_a(x).}
 \tag{4.10}
\]

It is numerically nonnegative and tends to zero from above as
\(a\to\infty\), but (4.10) is not yet proved.  A proof of its sign and a
final elementary lower bound at the intersection of the two walls would
establish (G).  The apparent intersection is

\[
 a=5.5888726293\ldots,\qquad K=a+\pi,
 \qquad F=0.6276300607\ldots,
 \tag{4.11}
\]

leaving a numerical margin about \(0.1276\) over the target.

## 5. A rigorous closure of the suspected hard double face

Consider the one-sided \(B=1\) limit

\[
 q=3,\qquad r=1,\qquad n=2,\qquad
 \varepsilon\downarrow0,\qquad \eta\downarrow0.
 \tag{5.1}
\]

Then \(a=3\), \(M=0\), \(z=3\), and

\[
 K=3\sec\theta,
 \qquad \tan\theta-\theta=\frac\pi4.
 \tag{5.2}
\]

Put \(\lambda=(K-3)/\pi\).  Radius differentiation gives the exact
representation

\[
 A(s)=\frac1\pi\int_3^K
 \sqrt{1-\frac{s^2}{u^2}}\,du.
 \tag{5.3}
\]

The map \(t\mapsto A(\sqrt t)\) is concave.  Its chord between
\(A(0)=\lambda\) and \(A(3)=3/4\) therefore yields

\[
 2\int_1^3(A(s)-1)\,ds
 \ge -1+\frac{56}{27}
 \left(\lambda-\frac34\right).
 \tag{5.4}
\]

Convexity of \(G_K\) at its inverse point \(z=3\), whose slope is
\(-\theta/\pi\), also gives the tangent triangle

\[
 J_K(3)\ge\frac{9\pi}{32\theta}.
 \tag{5.5}
\]

Combining (5.4)--(5.5) with the exact head/terminal decomposition proves

\[
 \Omega_{\rm wall}\ge
 \frac{9\pi}{16\theta}-2
 +\frac{56}{27}
 \left\{\frac{3(\sec\theta-1)}\pi-\frac34\right\}.
 \tag{5.6}
\]

Here (5.2) has a unique solution and

\[
 \frac{107}{100}<\theta<\frac{108}{100}.
 \tag{5.7}
\]

For completeness, monotonicity of \(\tan t-t\) reduces (5.7) to its two
rational endpoint comparisons.  At \(x=107/100\), use

\[
 \sin x<S_+:=x-\frac{x^3}{6}+\frac{x^5}{120},
 \qquad
 \cos x>C_-:=1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720},
\]

and \(\pi>3141/1000\); direct rational arithmetic gives

\[
 (x+3141/4000)C_--S_+
 =\frac{37895950228428571}{2880000000000000000}>0.
\]

At \(x=108/100\), use the lower sine polynomial through \(-x^7/7!\),
the upper cosine polynomial through \(+x^8/8!\), and \(\pi<22/7\); then

\[
 S_--(x+11/14)C_+
 =\frac{619006280090323}{239257812500000000}>0.
\]

Finally

\[
 \cos\theta<
 1-\frac{(107/100)^2}{2}+\frac{(107/100)^4}{24}
 =\frac{1157199601}{2400000000}.
\]

Substitution in (5.6), using the lower bound for \(\pi\) in its numerator
and \(\pi<22/7\) in \(\lambda\), gives the exact positive reserve

\[
 \boxed{
 \Omega_{\rm wall}>
 \frac{15150166179733}{73320166719360}
 >\frac15.}
 \tag{5.8}
\]

The actual value is approximately \(0.70456\).  At literal \(y=0\), the
strict outer level belongs to \(B=0\); (5.8) correctly concerns the
one-sided \(M=0\), \(B=1\) limit and makes no wall-identification error.

## 6. Diagnostic falsification

The Mathematica evaluator
`computations/general_d_round16_continuous_geometric_probe.wl` checks the
identities, domain implications, convex slack, (5.8), the apparent cusp,
and the two-wall point.  On the 3,171 deterministic extension records it
finds no negative continuous scalar and no negative convex slack.

An independent high-precision search then exercised approximately 6.2
million feasible endpoint points through \(q\le500\), local stationary
refinements, every endpoint owner and equality face, and logarithmic probes
through \(q=10^6\).  It found no negative \(\Omega_{\rm end}\),
\(\Omega_0\), or \(F-1/2\).  Its apparent minimum of the continuous scalar
is the stable cusp

\[
 q=5,\quad r=1,\quad n=4,\quad a=6,
\]

\[
 K=9.2033393227\ldots,\qquad
 z-q=0.4000948319\ldots,\qquad
 \Omega_0=0.3420378441\ldots.
 \tag{6.1}
\]

The one-sided slopes are approximately \(-1.5661\) and \(2.6226\).
The enlarged two-parameter search for (G) found the apparent minimum in
(4.11).  These are diagnostic floating-point results, not interval
enclosures or proof premises.

## 7. Equality faces and loss ledger

1. The exact strict inverse convention is retained in (1.2).  Passing from
   \(\Omega_{\rm end}\) to \(\Omega_0\) discards \(2\eta>0\), including
   the convention \(\eta=1\) at an integral inverse wall.
2. A literal lower action wall drops \(Q\) and adds \(\chi_q\), so it gains
   two units relative to the open-side endpoint scalar, exactly as in Round
   15.
3. Branch and activity endpoints are one-sided limits.  No claim is made
   that the artificial endpoint motion stays in one shelf chamber.
4. The minimizer \(x\) may lie on either side of \(a\).  The extended
   definition (1.1), not the false condition \(A(a)<1\), covers both cases.
5. The only analytic losses after the exact Round 15 identity are the
   favorable endpoint motion, deletion of \(2\eta\), and convex minimization
   from \(r\) to \(x\).  The exact cap, no-drop head, outer terminal, and
   discrete count have not been separately bounded.

## 8. Gate decision

Round 16 replaces the three-owner endpoint sign by the single geometric
lemma (G), proves its strict radial monotonicity, and rigorously removes the
suspected small-grid double face.  The next round should prove the
action-boundary sign (4.10), then certify the two-wall value without solving
for a decimal root.  It must not return to
the rejected pre-shelf surrogate or create a ratio ladder.  If (G) is
falsified, the exact endpoint scalar (1.3) remains valid and the weighted
aggregate WT is still the designated fallback.
