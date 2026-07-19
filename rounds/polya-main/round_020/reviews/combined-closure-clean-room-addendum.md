# Addendum: `k_9`, `H=6,h=4` Cell

**Theorem verdict: PASS.**

**First issue in the original review:** the sentence in Section 5.2 saying
that every cap cell other than the displayed worst event has a *larger*
exact rational reserve is false when the candidate's conservatively retained
`k_9`, `H=6,h=4` cap-74 cell is paid using its natural coarse constraints.
That cell has a smaller, but still strictly positive, reserve.  The error is
in the description of the finite payment audit, not in claims (5), (7), (9),
or (11)--(13).

This addendum was prepared without opening any excluded artifact or any
other review.  It uses only the already authenticated candidate, the
permitted zero identities and inequalities, and exact rational arithmetic.
The original report, SHA-256
`7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb`,
has not been edited.

## 1. Why the strict proxy in the original proof does cover the cell

The full zero registry proved in the original review gives

$$
j_{7/2,2}>\frac{103}{10}.
$$

Angular propagation from $\ell=3$ to $\ell=4$ therefore gives

$$
j_{9/2,2}^2
\ge j_{7/2,2}^2+4\cdot5-3\cdot4
>\left(\frac{103}{10}\right)^2+8
=\frac{11409}{100}.
\tag{B1}
$$

If the second mode in channel $\ell=4$ were counted at $K\le k_9$, then
the ball comparison and (B1) would imply

$$
K^2>\frac{11409}{100},
\qquad
K^2\le k_9^2=z_\rho^2+90,
$$

and hence

$$z_\rho^2>\frac{2409}{100}.$$

The one-dimensional channel lower bound simultaneously gives

$$
4z_\rho^2+20< K^2\le z_\rho^2+90,
$$

so

$$z_\rho^2<\frac{70}{3}.$$

These conditions contradict one another because

$$
\frac{2409}{100}-\frac{70}{3}=\frac{227}{300}>0.
\tag{B2}
$$

Thus, with the complete Round 20 zero registry, the `h=4` mode is actually
impossible at `k_9`; in particular the `H=6,h=4` cell is empty.  This is why
the strict proxy (A13)--(A14) in the original report never generated a
cap-74 jump.  The original report should have stated this explicitly instead
of subsuming the row under the phrase "all other cap cells have a larger
reserve."

## 2. Independent payment if the conservative cap is retained

There is also a direct payment that does not remove the candidate's
over-inclusive cap-74 row.  It is useful because it audits the candidate
table exactly as printed.

The weaker consequence $j_{7/2,2}>10$, followed by the same angular
propagation, gives

$$
q_{4,2}^2\ge j_{9/2,2}^2>10^2+8=108.
$$

Hence a counted $(4,2)$ mode forces

$$
K^2>108,
\qquad
K>\frac{207}{20},
\tag{B3}
$$

where the second implication is strict because

$$
108-\left(\frac{207}{20}\right)^2=\frac{351}{400}>0.
$$

The channel wall above still gives $z_\rho^2<70/3$.  At
$\rho=7/20$ one has $z_\rho=20\pi/13$, and the permitted lower enclosure
$\pi>333/106$ gives

$$
\left(\frac{20\pi}{13}\right)^2-\frac{70}{3}
>
\frac{36230}{1424163}>0.
$$

Since $z_\rho$ increases with $\rho$, a counted $(4,2)$ mode therefore
forces

$$\rho<\frac7{20}.$$

The cap is the full multiplicity sum

$$
(6+1)^2+(4+1)^2=49+25=74.
$$

Using $\pi<22/7$, (B3), and $\rho<7/20$ gives the strict payment

$$
\begin{aligned}
\mathcal W(\rho,K)
&>\frac{2}{9(22/7)}
\left(1-\left(\frac7{20}\right)^3\right)
\left(\frac{207}{20}\right)^3\\
&=\frac{52823261673}{704000000}\\
&=74+\frac{727261673}{704000000}>74.
\end{aligned}
\tag{B4}
$$

This reserve is smaller than the reserve printed for the displayed
`k_8<K\le k_9` event:

$$
\frac{835355}{577368}
-\frac{727261673}{704000000}
=\frac{1911276163447}{4618944000000}>0.
\tag{B5}
$$

Therefore the original "all larger reserve" claim must be replaced by:

> Every realizable strict-proxy jump is paid.  The candidate's additional
> conservative `k_9`, `H=6,h=4` cap-74 row is empty under the full zero
> registry; if retained under the weaker ledger, it is paid separately by
> (B4), with a positive reserve smaller than the reserve displayed in the
> original summary table.

## Final addendum decision

**PASS; first theorem issue: none.**  The first report issue is the omitted
qualification and false comparative-reserve sentence identified above.
Equations (B1)--(B2) show that the strict proxy proof already covers the
cell by impossibility, while (B3)--(B4) independently pays the printed
conservative cap.  The high staircase theorem (7) remains proved.
