# Independent audit: Round 4b high-floor cutoff and Round 4c terminal reserve

Date: 18 July 2026

Files audited:

- `general-d-round-04-high-floor-cutoff.md`
- `general-d-round-04-zero-level-terminal.md`

Verdict: **PASS, with three localized presentation corrections.**  I found
no false inequality, reversed sign, incorrect constant, or wall-convention
failure in Proposition 2.2, Theorem 3.1, Corollary 3.2, the zero-level
triangle, or the fractional-top convex reserve.  The critical-ray result is
an asymptotic theorem on the stated scaling, not a uniform finite-
\(\varepsilon\) closure; the note already says this correctly.

## 1. High-floor cutoff note

### Section 1 / Proposition 1.1: PASS

Lines 78--135 are arithmetically consistent.  In particular,

\[
 G_1(0.99)>\frac{2\sqrt2}{3\pi}(0.01)^{3/2}
 >\frac{49}{165000},
\]

the displayed radicand is less than \(624^2\), and the omitted numerator
step is

\[
 \frac{623+2(1/3)(13/10)+624}{2}<624.
\]

Also

\[
 3\left(2358517285-\frac14\right)
 -\frac{16988400000000}{2401}
 =\frac{8217}{9604}.
\]

Thus \(a>\pi(f-1/4)>\overline K\) really implies \(K>K_0(\rho)\).

### Lemma 2.1: PASS after one missing sentence is supplied

The endpoint reduction in lines 187--197 is valid, but the replay in
lines 205--270 silently switches from an arbitrary \(y_0\) to the
minimizing \(y_0\).  To make the proof self-contained, insert before line
205:

> At \(s=y_b\), differentiation with respect to \(y_0\) gives
> \(2(f-B_a(y_0))\).  Hence the minimum is attained at
> \(y_0=\sqrt{a^2-\pi^2f^2}\) if \(R=a/\pi\ge f\), and at \(y_0=0\) if
> \(h\le R<f\).

With that sentence, (9) and (10) are bounds for the actual minimum and
therefore prove (7) for every \(y_0\).  The constants check:

\[
 \frac{\frac32h^2-f^2}{4}-\frac{f^2}{36}
 =\frac{112f^2-216f+27}{1152},
\]

and in the second case rationalization actually gives the stronger
\(P/(4R)\), so the stated \(P/(6R)\) is safe.  The inequality
\(P\ge h^2-2h-1/4\) follows from
\(4t(1-t)^2(2h+t)\le2h+1/4\).

High-precision endpoint sampling for \(f=3,4,10,100\) and
\(R/h\) from \(1+10^{-7}\) to \(10^6\) gave a minimum ratio
\(\mathcal L/(f^2/(4a))>7.51\); this was used only as falsification.

### Proposition 2.2: PASS

The radius-average estimate (6) has the correct direction: after writing
the radius as \(at/\varepsilon\), the averaged integrand
\(\sqrt{1-(y/(at))^2}\) is concave in \(t\), so its integral is at least
its endpoint trapezoid and at most its value at \(t=1\).

The localization in lines 320--337 is valid.  From (11),
\(a>\pi h\), \(h\ge11f/12\), and \(f\ge3\), one gets
\(\varepsilon<1/100\); furthermore

\[
 1-\rho^2<2\varepsilon
 \le \frac{f^3}{72a^4}
 <\frac{\pi^2h^2}{a^2},
\]

which is equivalent to \(y_b<a\rho\).

The loss integral (15) is correct: the denominator is at least
\(\lambda=\pi h/a\), and extending the \(t\)-integral to \([0,1]\)
gives the factor \(1/3\).  The numerical coefficient is

\[
 \frac{20000}{9801}\frac4{99}
 =\frac{80000}{970299}<\frac1{11}.
\]

The terminal-coordinate bound (18) follows from
\(y_q\ge a\rho-\varepsilon\) and \(s\ge0\).  The two losses in (20) are
each at most \(f^2/(24a)\), and the final arithmetic is

\[
 \frac14-\frac1{1584}-\frac1{12}>\frac18.
\]

All inequalities are compatible with an ordinary lower shelf wall and
with the strict terminal bracket.

### Critical scaling, Theorem 3.1: PASS

The turning limit (22), the interface height \(w=c_0\kappa\), and the
angle constant in (24) agree exactly.  Cubing the coefficient identity
reduces it to

\[
 \frac{c_0}{2\sqrt2}=\frac1{3\pi}.
\]

The finite \(Q\)-term and cap vanish after multiplication by
\(\sqrt\varepsilon\).  At a limiting action wall, choosing
\(B=[w+1/4]_<\) gives the smaller complete-level sum and is therefore
wall-safe.

The algebra in (26) is correct.  If the prefix (27) is negative, then
\(N>2M\).  Under \(w\le3/4\), the estimates imply

\[
 \frac{u_f}{u_h}
 \le\left(\frac76\right)^2
 \left(\frac{400}{351}\right)^2<2,
\]

and under \(t_f\le1/4\) they imply

\[
 \frac{u_f}{u_h}
 <\left(\frac65\right)^2
 \left(\frac{100}{91}\right)^2<2.
\]

Thus both conclusions in (29) follow.  Since
\(H_\kappa'(X)\ge(3c_0/2)(1/4)\) on \([M,N]\), the width and loss bounds
in (30) have the correct strict direction.  The first terminal level then
strictly exceeds the same constant \(1/(3c_0)=\pi/(2\sqrt2)\).

In the no-drop branch, \(M=0\) and \(w\ge h\).  If \(w<f\), then
\(F(t_f)\le8/7\), hence \(t_f>1/4\), so the same loss bound applies.
Closed-form numerical sweeps over \(2\le f\le100\) found no violation;
the smallest sampled terminal-minus-negative-prefix margin was greater
than \(1.30\).

### Corollary 3.2: PASS on its stated scaling

No-drop gives \(w\ge h\ge7/4\), so the first complete level gives

\[
 \mathcal T(w)\ge\frac\pi{2\sqrt2}(7/3)^{1/3}.
\]

Subtracting the universal prefix loss \(\pi/(2\sqrt2)\) proves (31a),
including at the strict wall \(w=7/4\).  The rational comparisons in
lines 720--722 imply \(\gamma_0>1/3\).

**Presentation correction:** lines 724--728 do not follow from Corollary
3.2 alone.  They additionally use the exhaustion theorem in
`general-d-round-04-no-drop-exhaustion.md`, which reduces every escaping
no-drop sequence to \(f=2,3\), \(K\asymp n^3\), and
\(K-\mu\asymp n\).  Add that cross-reference or make the sentence
explicitly conditional.  With that cited reduction, the sequential
compactness conclusion is valid; it still supplies no explicit cutoff,
as the note correctly states.

## 2. Zero-level and fractional-top note

### Zero-level proposition: PASS

Lines 64--95 are exact.  The strict convention gives
\(B=0\iff G_K(q)\le3/4\), so all shell brackets vanish.  On
\([\mu,K]\), convexity gives

\[
 G_K(z)\ge v-c(z-\mu).
\]

The tangent zero is at \(\mu+v/c\le K\), because the tangent at \(K\)
cannot exceed \(G_K(K)=0\).  Integrating its positive triangle yields
\(v^2/c\).  Combining this with \(R_p\ge-p/2\) gives exactly condition
(3), with the correct sign and factor \(1/2\).  The equality wall
\(G_K(q)=3/4\) is handled correctly by the strict bracket.

### Fractional-top convex reserve: PASS

For the decreasing inverse \(y(t)\), convexity of \(g\) implies convexity
of \(y\), and
\(y'(v-)=-1/c_v\).  The tangent at \(t=v\) therefore gives

\[
 2\int_B^v y(t)\,dt\ge\frac{(v-B)^2}{c_v}
\]

when \(v>B\), with no overlap with the complete intervals \([0,B]\).
When \(v\le B\), the positive part correctly removes the term.  Inserting
this in the one-interface identity gives (5): the \(-B\) in the
complete-level sum cancels the \(+B\) in \(B-Q\), while the fractional
term remains.

**Wall clarification:** formula (25a) of the high-floor note must remain
restricted to non-wall limits.  At a wall \(w=m-1/4\), the lower-side
fractional contribution is \(9\pi/(16\sqrt2)\), while activation of the
new complete level from the upper side contributes
\(\pi/(2\sqrt2)\).  The latter is smaller.  Thus lines 519--521 are
correct, but the safe wall value is the lower of the two one-sided total
expressions, not the literal substitution of the strict \(B\) into
(25a).

For complete self-containment, formula (5) should restate that
\(B=[G_K(q)+1/4]_<\) and that \(\theta_k\) is the ball-level angle.  This
is a notation clarification only.

## 3. Final audit status

- Proposition 2.2: **PASS** after explicitly supplying the omitted
  \(y_0\)-minimization sentence in Lemma 2.1.
- Theorem 3.1: **PASS** as a critical-scaling theorem.
- Corollary 3.2: **PASS**, conditional only on its stated scaling; cite
  the separate exhaustion theorem for the global finiteness sentence.
- Zero-level triangle and condition (3): **PASS**.
- Fractional-top reserve and terminal certificate: **PASS**, with the
  stated one-sided convention at level walls.

