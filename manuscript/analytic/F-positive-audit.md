# Clean-room audit of `F-positive.tex`

Date: 2026-07-16  
Audited file: `manuscript/analytic/F-positive.tex`  
Verdict: **PASS**

The proof was reconstructed from the definitions, without importing any
conclusion from the source.  The Dalzell identity, the integral estimate for
`G_1`, both branches of the argument, every displayed rational subtraction,
all strictness directions, and the final uniform-minimum comparison are
correct.

## 1. Domain and exact reduction

The chain
\[
0<\frac7{51}<\frac12<\frac{39}{50}<1
\]
is correct: the two internal comparisons reduce to `14 < 51` and
`25 < 39`.  Hence every denominator and inverse trigonometric expression
used in the proof is valid.

Substituting
\(b_\rho=2\pi\rho/(1-\rho)\) into the definition of \(F\) and dividing by
the positive number \(\rho\) gives exactly
\[
\frac{F(\rho)}\rho
=2\eta_\rho+d_\rho\rho
-\frac{3\pi(1+d_\rho)}{400(1-\rho)}.
\]
No factor of two or sign is lost in this reduction.

## 2. Dalzell identity and elementary constants

Multiplying the printed identity by \(1+x^2\) gives
\[
\begin{aligned}
&(1+x^2)(x^6-4x^5+5x^4-4x^2+4)-4\\
&\qquad=x^8-4x^7+6x^6-4x^5+x^4
=x^4(1-x)^4,
\end{aligned}
\]
so the rational-function identity is exact.  Its left side is strictly
positive on \((0,1)\).  Termwise integration of the polynomial quotient
gives
\[
\frac17-\frac46+1-\frac43+4=\frac{22}{7},
\]
while
\(4\int_0^1(1+x^2)^{-1}\,dx=4\arctan(1)=\pi\).
Consequently the positive integral is exactly \(22/7-\pi\), proving the
strict bound \(\pi<22/7\).

The three radical comparisons are also exact after squaring positive
quantities:
\[
2-\frac{49}{25}=\frac1{25},\qquad
3-\frac{25}{9}=\frac29,\qquad
\frac{11}{50}-\frac{49}{225}=\frac1{450}.
\]
Thus all four inequalities in Lemma 1 have the stated strict direction.

## 3. Integral bound for \(G_1\)

Differentiation confirms
\[
\frac{d}{dt}\left(t\arccos t-\sqrt{1-t^2}\right)=\arccos t.
\]
Evaluation at \(1\) and \(s\) therefore gives precisely the claimed
integral representation.

For \(y=\arccos t\),
\[
\sqrt{2(1-t)}=2\sin(y/2)\le y=\arccos t.
\]
Integration yields
\[
G_1(s)\ge \frac{2\sqrt2}{3\pi}(1-s)^{3/2}.
\]
For \(1/2\le s\le39/50\), one has \(1-s\ge11/50\), and the three strict
rational estimates give
\[
G_1(s)>
\frac{2(7/5)}{3(22/7)}\frac{11}{50}\frac7{15}
=\frac{49}{165}\frac{77}{750}
=\frac{3773}{123750}
=\frac{343}{11250}.
\]
The last reduction cancels a factor of `11`.  The use of `>` is justified:
the radical estimates and reciprocal consequence of \(\pi<22/7\) are
strict, and every factor is positive.

## 4. First branch: \(7/51\le\rho\le1/2\)

Here
\[
\eta_\rho=G_1(1/2)=\frac{\sqrt3}{2\pi}-\frac16,
\qquad 0<d_\rho\le\frac13.
\]
Also \((1-\rho)^{-1}\le2\).  Hence the negative term satisfies
\[
\frac{3\pi(1+d_\rho)}{400(1-\rho)}
\le\frac\pi{50}<\frac{11}{175}.
\]
The positive action term satisfies
\[
2\eta_\rho=\frac{\sqrt3}{\pi}-\frac13
>\frac{5/3}{22/7}-\frac13
=\frac{13}{66}.
\]
Discarding only the nonnegative term \(d_\rho\rho\) is safe.  Exact
subtraction gives
\[
\frac{13}{66}-\frac{11}{175}
=\frac{2275-726}{11550}
=\frac{1549}{11550}>0.
\]
Since \(\rho\ge7/51\) and \(11550=7\cdot1650\),
\[
F(\rho)>\frac7{51}\frac{1549}{11550}
=\frac{1549}{84150}.
\]
The strict inequality survives multiplication by the positive \(\rho\) and
replacement of \(\rho\) by its lower endpoint.

## 5. Second branch: \(1/2\le\rho\le39/50\)

The preceding `G_1` estimate gives
\[
2\eta_\rho>\frac{343}{5625}.
\]
Monotonicity of \(\arcsin\) gives
\(d_\rho\ge1/3\), and therefore \(d_\rho\rho\ge1/6\).

The comparison
\[
\left(\frac{39}{50}\right)^2=\frac{1521}{2500}
<\frac34
\]
proves \(39/50<\sqrt3/2\), so \(d_\rho<2/3\).  Together with
\((1-\rho)^{-1}\le50/11\), this gives
\[
\frac{3\pi(1+d_\rho)}{400(1-\rho)}
<\frac{5\pi}{88}<\frac5{28}.
\]
All inequality directions are safe for a lower bound on \(F/\rho\).  The
common denominator is `157500`, and the exact subtraction is
\[
\frac{343}{5625}+\frac16-\frac5{28}
=\frac{9604+26250-28125}{157500}
=\frac{7729}{157500}>0.
\]
Using \(\rho\ge1/2\) therefore yields
\[
F(\rho)>\frac{7729}{315000}.
\]

## 6. Uniform minimum and endpoints

The high-branch constant is strictly larger than the low-branch constant:
\[
\frac{7729}{315000}-\frac{1549}{84150}
=\frac{120341}{19635000}>0.
\]
Thus the smaller uniform reserve is exactly the asserted
\(1549/84150\).  Both branches include \(\rho=1/2\), and the definition
\(\eta_\rho=G_1(\max\{\rho,1/2\})\) has the same value there.  The outer
endpoints are also included by the non-strict domain estimates while the
final margins remain strict.

As an independent arithmetic replay, exact rational evaluation reproduced
\[
\frac{22}{7},\quad
\frac{343}{11250},\quad
\frac{1549}{11550},\quad
\frac{1549}{84150},\quad
\frac{7729}{157500},\quad
\frac{120341}{19635000}
\]
for the six displayed reductions above.

**Final result: PASS. No mathematical gap found.**
