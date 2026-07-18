# Inverse-action and double-sawtooth reduction for shifted shell tails

Date: 18 July 2026

## 1. Scope and conclusion

Fix (0<\mu<K), a shift (r\in\tfrac12\mathbb N), and assume
(r<\mu).  Write

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}\mathbf 1_{z<a},
 \qquad
 A(z)=G_K(z)-G_\mu(z),
\]

and zero-extend (A) after (K).  The shifted-tail defect is

\[
 D_A(r)=2\int_r^K A(z)\,dz-
 \left([A(r)+\tfrac14]_<+2\sum_{j\ge1}[A(r+j)+\tfrac14]_<\right).
\]

This note gives two exact, wall-safe identities for (D_A(r)), an exact
Stieltjes decomposition at the curvature interface, and a sharp reduction
to one terminal phase inequality.  It does **not** prove that terminal
inequality for all parameters.  No exact-shell counterexample was found,
but qualitative monotonicity and the slope cap alone are insufficient; an
explicit counterexample is given in Section 8.

## 2. Strict counting functions

Put

\[
 h_n=n-\frac14\quad(n\ge1),
 \qquad
 C(t)=\#\{n\ge1:h_n<t\}=[t+\tfrac14]_<,
 \qquad
 w(t)=t-C(t).
\]

Thus

\[
 -\frac14<w(t)\le\frac34,
 \]

and at a wall (t=h_n) the strict convention gives

\[
 C(h_n)=n-1,
 \qquad
 w(h_n)=\frac34.
\]

For (y>0), let

\[
 M(y)=\#\{k\in\mathbb Z:|k|<y\}=2\lceil y\rceil-1,
 \qquad
 \chi(y)=M(y)-2y.
\]

Away from integers, (\chi(y)=1-2\{y\}).  At an integer wall (y=m),
strict counting gives

\[
 M(m)=2m-1,
 \qquad
 \chi(m)=-1.
\]

This value, rather than the left limit (+1), is essential at a common
radial--angular wall.

## 3. Exact inverse-action split

Let

\[
 T=A(r),
\]

and suppose first that (T>0).  Since (A) is strictly decreasing on
([r,K]), let (R:[0,T]\to[r,K]) be its decreasing inverse and set

\[
 y(t)=R(t)-r,
 \qquad
 F(t)=2y(t).
\]

Layer cake gives

\[
 2\int_r^K A(z)\,dz=\int_0^T F(t)\,dt.
\]

For each (h_n<T), the integers (j\ge0) with
(A(r+j)>h_n) are exactly those with (j<y(h_n)).  Taking weight one at
(j=0) and weight two thereafter therefore gives

\[
 [A(r)+\tfrac14]_<+2\sum_{j\ge1}[A(r+j)+\tfrac14]_<
 =\sum_{h_n<T}M(y(h_n)).
\]

Consequently

\[
 \boxed{D_A(r)=D_{\rm rad}-E_{\rm ang},}
\]

where

\[
 D_{\rm rad}=\int_0^T F(t)\,dt-\sum_{h_n<T}F(h_n),
 \qquad
 E_{\rm ang}=\sum_{h_n<T}\chi(y(h_n)).
\]

If (T=h_N), that endpoint is excluded in both sums.  Since (F(T)=0),
including it in the radial sum would be numerically harmless, but including
it in the angular sum would not be a legitimate manipulation.  The strict
form above avoids that mismatch.

## 4. Stieltjes formula and the ungridded interface

Define

\[
 q(z)=-A'(z)=\frac1\pi
 \begin{cases}
 \arccos(z/K)-\arccos(z/\mu),&r<z<\mu,\\
 \arccos(z/K),&\mu<z<K.
 \end{cases}
\]

Then

\[
 g(t)=-F'(t)=\frac{2}{q(R(t))}.
\]

On the inner branch,

\[
 q'(z)=\frac1\pi\left(\frac1{\sqrt{\mu^2-z^2}}-
 \frac1{\sqrt{K^2-z^2}}\right)>0,
\]

whereas on the outer branch

\[
 q'(z)=-\frac1{\pi\sqrt{K^2-z^2}}<0.
\]

As (R) decreases with (t), it follows that, with

\[
 \tau=A(\mu)=G_K(\mu),
\]

(g) decreases on ((0,\tau)) and increases on ((\tau,T)).  It is
continuous at (\tau).  Moreover (g(t)=O(t^{-1/3})) at (0), while

\[
 g(\tau)=\frac{2\pi}{\arccos(\mu/K)},
 \qquad
 g(T)=\frac{2\pi}{\arccos(r/K)-\arccos(r/\mu)}.
\]

Distributionally, (dw=dt-dC).  Stieltjes integration by parts, first on
([\varepsilon,T]) and then as (\varepsilon\downarrow0), gives

\[
 \boxed{D_{\rm rad}=\int_0^T w(t)g(t)\,dt.}
\]

The improper boundary term vanishes because (w(t)=t) near zero and
(g(t)=O(t^{-1/3})).

Put

\[
 \mathfrak W(t)=\int_0^t w(s)\,ds,
 \qquad
 \Psi(t)=\mathfrak W(t)-\frac t4.
\]

On (0\le t\le3/4),

\[
 \Psi(t)=\frac12(t-\tfrac14)^2-\frac1{32},
\]

and on a complete cell (t=h_n+u), (0\le u\le1),

\[
 \Psi(t)=\frac12(u-\tfrac12)^2-\frac1{32}.
\]

Hence

\[
 \mathfrak W\ge0,
 \qquad
 -\frac1{32}\le\Psi\le\frac3{32}.
\]

Splitting at the actual value (\tau), without any assumption that
(\tau) lies on the (h_n)-grid, gives the exact identity

\[
 \boxed{
 D_{\rm rad}
 =\frac{F(\tau)}4+\frac{\tau g(\tau)}4
 +\Psi(T)g(T)-\int_\tau^T\Psi\,dg
 -\int_0^\tau\mathfrak W\,dg.}
\]

Here (F(\tau)=2(\mu-r)), (dg\le0) on the first interval, and
(dg\ge0) on the second.  In particular, if

\[
 \mathcal R_{\rm out}:=-\int_0^\tau\mathfrak W\,dg\ge0,
\]

then

\[
 D_{\rm rad}\ge
 \frac{\mu-r}{2}+\mathcal R_{\rm out}
 +g(\tau)\left(\frac\tau4+\frac3{32}\right)
 +g(T)\left(\Psi(T)-\frac3{32}\right).
\]

This yields a rigorous phase-sensitive sufficient condition after
comparison with (E_{\rm ang}).  The uniform replacement
(\Psi(T)-3/32\ge-1/8) is usually far too lossy: (g(T)=2/q(r)) can be
very large even though (r\ge1/2).  Thus the bounded-variation estimate
does not close the theorem.

## 5. Exact double-sawtooth identity

Let (L=K-r) and abbreviate (A_j=A(r+j)).  Angular integration by parts
gives

\[
 \int_0^L\chi(s)q(r+s)\,ds
 =T+2\sum_{1\le j<L}A_j-2\int_0^L A(r+s)\,ds.
\]

Indeed (M(s)=2\lceil s\rceil-1) jumps by two at every positive integer,
and the endpoint (s=L) contributes nothing because (A(K)=0).  Since
([A_j+1/4]_< =A_j-w(A_j)), substitution gives

\[
 \boxed{
 D_A(r)=w(T)+2\sum_{1\le j<L}w(A_j)
 -\int_0^L\chi(s)q(r+s)\,ds.}
\]

This formula is correct at simultaneous walls.  If (A_j=h_n), then the
strict radial remainder is

\[
 w(A_j)=\frac34.
\]

For (j\ge1), replacing this by the post-wall limit (-1/4) changes the
weighted ledger by two and invalidates the identity (the change has weight
one at (j=0)).  The point representative \(\chi(j)\) does not affect the
Lebesgue integral in this formula.  It does matter in the inverse-action
sum of Section 3: at a common wall (y(h_n)=j), strict angular counting
requires \(\chi(j)=-1\), not its left limit (+1).

## 6. Convex suffix and exact boundary phase

Assume (T>3/4); otherwise the shifted tail is zero.  Then

\[
 T<A(0)=\frac{K-\mu}{\pi}
\]

implies (K-\mu>3\pi/4).  Let

\[
 J=\lceil\mu-r\rceil,
 \qquad
 \eta=\mu-r-(J-1)\in(0,1].
\]

The preceding thickness bound shows (r+J<K), so the convex suffix starts
at a genuine sample.  Define

\[
 D_J=2\int_{r+J}^K A(z)\,dz-
 \left([A_J+\tfrac14]_<+2\sum_{j>J}[A_j+\tfrac14]_<\right).
\]

Since (r+J\ge\mu), this is a translated ball-tail defect and (D_J\ge0).
Periodicity of (\chi) and the double-sawtooth identity give the exact
boundary formula

\[
 \boxed{
 D_A(r)=D_J+S_J-\int_0^J\chi(s)q(r+s)\,ds,}
\]

with

\[
 \boxed{
 S_J=w(T)+2\sum_{j=1}^{J-1}w(A_j)+w(A_J).}
\]

The weight of (w(A_J)) is one, not two: the other copy belongs to the
convex suffix (D_J).  This is exactly the terminal reserve that is lost if
one sums inner cell increments and merely appends the statement (D_J\ge0).

## 7. Complete inner cells and the sharp interface loss

On a complete integer cell write (s=k+u), (0<u<1).  Then

\[
 \chi(k+u)=1-2u.
\]

If (f) is increasing on that cell, pairing (u) with (1-u) gives

\[
 \int_0^1(1-2u)f(u)\,du
 =\int_0^{1/2}(1-2u)\bigl(f(u)-f(1-u)\bigr)\,du\le0.
\]

Point values at (u=0,1), including strict angular walls, have measure
zero and do not alter the integral.  Since (q(r+s)) is increasing for
(s<\mu-r), every cell

\[
 [k,k+1],\qquad 0\le k\le J-2,
\]

has nonpositive integral.  If (\eta=1), the final cell is also complete
and nonpositive.

On the last cell ([J-1,J]), (q) is unimodal with peak

\[
 Q=q(\mu)=\frac1\pi\arccos(\mu/K)
\]

at relative position (\eta).  Define

\[
 \beta(\eta)=
 \begin{cases}
 \frac14,&0<\eta\le\frac12,\\
 \eta(1-\eta),&\frac12\le\eta\le1.
 \end{cases}
\]

Then

\[
 \boxed{
 \int_{J-1}^{J}\chi(s)q(r+s)\,ds\le Q\beta(\eta)\le\frac Q4<\frac18.}
\]

Proof: by layer cake, every superlevel set of the unimodal function on the
cell is an interval ([a,b]) containing (\eta).  With

\[
 H(u)=\int_0^u(1-2v)\,dv=u-u^2,
\]

the contribution of such an interval is (H(b)-H(a)).  The largest such
contribution is (1/4) if (\eta\le1/2) (take ([a,b]=[0,1/2])) and is
(H(\eta)=\eta(1-\eta)) if (\eta\ge1/2) (take
([a,b]=[0,\eta])).  Integration over the superlevel parameter proves the
claim.  This coefficient is sharp among all unimodal functions bounded by
(Q); continuity is obtained by approximating the indicated step
profiles.

Combining the complete-cell signs with the exact boundary formula proves
the rigorous lower bound

\[
 \boxed{
 D_A(r)\ge D_J+S_J-Q\beta(\eta).}
\]

Therefore the remaining shell-specific terminal phase lemma is

\[
 \boxed{D_J+S_J\ge Q\beta(\eta).}\tag{TP}
\]

The simpler condition (D_J+S_J\ge q(\mu)/4) is a valid sufficient
hypothesis but is unnecessarily strong when (\eta>1/2).  It is not a
universal inequality over all shell parameters.  For example, take

\[
 r=1,\qquad \mu=2-\varepsilon,\qquad K=2+\varepsilon.
\]

Then (J=1), (\eta=1-\varepsilon), and, as
(\varepsilon\downarrow0),

\[
 D_1+S_1=O(\varepsilon),
 \qquad
 q(\mu)/4\asymp\sqrt\varepsilon.
\]

Thus the (q(\mu)/4) inequality fails for all sufficiently small
(\varepsilon).  This family lies in the already trivial zone (T<3/4); it
does not contradict the shifted-tail theorem.  The sharpened factor behaves
as

\[
 q(\mu)\beta(\eta)\asymp\varepsilon^{3/2},
\]

and correctly removes this artificial obstruction.  For reference, the
concrete exact-shell parameters (r,\mu,K)=(1,1.99,2.01) give numerically
(D_1+S_1-q(\mu)/4)\approx-0.00551).  This numerical value only illustrates
the rigorous asymptotic counterfamily.

There is one immediate automatic region.  The endpoint weights in (S_J)
sum to (2J), and every strict remainder satisfies (w>-1/4), so

\[
 S_J>-\frac J2.
\]

The refined convex ball-tail reserve already available in the project gives

\[
 D_J\ge\frac12\left\lfloor
 G_K\!\left(\max\{r+J,K/2\}\right)\right\rfloor.
\]

Consequently (TP), and hence the shifted-tail inequality, is automatic if

\[
 \left\lfloor G_K\!\left(\max\{r+J,K/2\}\right)\right\rfloor\ge J+1.
\]

Thus a valid residual family is

\[
 T>\frac34,
 \qquad
 \left\lfloor G_K\!\left(\max\{r+J,K/2\}\right)\right\rfloor\le J.
\]

This reduction is not compact: (J) can grow proportionally to (K), and the
displayed ball action can remain below (J+1).  No honest finite residual is
obtained without an additional lower bound coupling the convex suffix
reserve to the inner radial phases.

### A monotone compact two-parameter residual for each discrete block

There is nevertheless a useful shell-specific compactification.  Fix the
discrete pair (r,J), and vary (K) while holding (r,\mu) fixed inside the
block

\[
 r+J-1<\mu\le r+J.
\]

Set

\[
 \mathcal M(K)=D_J+S_J-q(\mu)\beta(\eta).
\]

On an open (K)-interval containing no sample wall, every strict bracket is
constant and

\[
 \partial_KG_K(z)=\frac1\pi\sqrt{1-\frac{z^2}{K^2}}>0.
\]

The derivative of (D_J) is positive, as are all the derivatives contributed
by the phase terms in (S_J).  The only adverse derivative is that of
(q(\mu)\beta(\eta)).  Since

\[
 \partial_Kq(\mu)
 =\frac{\mu}{\pi K\sqrt{K^2-\mu^2}},
\]

the derivative of the first phase alone satisfies

\[
 \frac{\partial_KA(r)}{\partial_Kq(\mu)}
 =\frac{\sqrt{K^2-r^2}\sqrt{K^2-\mu^2}}{\mu}
 >\frac{K^2-\mu^2}{\mu}
 >2(K-\mu)>\frac{3\pi}{2}.
\]

Here the final inequality uses (T>3/4), hence
(K-\mu>3\pi/4).  Since (\beta\le1/4), it follows that

\[
 \boxed{\mathcal M'(K)>0}
\]

between all walls.  When (K) crosses a wall from left to right, the relevant
strict remainder drops by its integer weight.  Therefore the possible
minima are the right-hand limits of the finitely many walls in a bounded
(K)-interval, together with boundary faces.  The wall families are

\[
 A(r+j)=n-\frac14\quad(0\le j<J),
 \qquad
 G_K(r+k)=n-\frac14\quad(k\ge J).
\]

The earlier refined ball reserve makes the interval bounded.  Put

\[
 \omega_0=G_1(1/2),
 \qquad x=r+J.
\]

If (K\ge2x), then

\[
 G_K(\max\{x,K/2\})=G_K(K/2)=\omega_0K.
\]

Thus every unresolved point satisfies

\[
 \boxed{
 \mu+\frac{3\pi}{4}<K<K_{\max}(r,J),
 \qquad
 K_{\max}(r,J)=\max\left\{2(r+J),\frac{J+1}{\omega_0}\right\}.}
\]

For each fixed (r,J), the remaining variables consequently lie in the
compact closure of

\[
 r+J-1<\mu\le r+J,
 \qquad
 \mu+\frac{3\pi}{4}<K<K_{\max}(r,J),
\]

and only finitely many wall levels (n) and sample indices (k) occur there.
This is a genuine monotone two-parameter wall reduction for every discrete
block.  It is **not** a global finite certificate, because no argument here
bounds the infinitely many possible pairs (r,J).

### First-shelf scalar sectors

The proof of the existing low-action ball reserve gives more than its stated
constant.  Put (x=r+J), translate the suffix as

\[
 g_*(s)=G_K(x+s),
 \qquad h=g_*(0),
\]

and suppose (x\ge K/2), so that (g_*) is (1/3)-Lipschitz.

If (0\le h\le3/4), the suffix count is zero and the tangent triangle gives

\[
 D_J=2\int_0^{K-x}g_*(s)\,ds\ge3h^2.
\]

Consequently (TP) holds whenever

\[
 3h^2\ge\frac J2+\frac18.
\]

If

\[
 \frac34<h<1,
\]

let (\ell) be defined by (g_*(\ell)=3/4).  The same scalar proof gives

\[
 D_J>
 \begin{cases}
 11/16,&\ell\le1,\\
 7\ell/4-1,&\ell>1.
 \end{cases}
\]

Since (S_J>-J/2) and (q(\mu)\beta(\eta)<1/8), this proves (TP)

* for (J=1) whenever (\ell\le1); and
* for arbitrary (J) whenever
  \[
  \ell\ge\frac{4J+9}{14}.
  \]

These conditions are fully explicit one-variable ball-shelf sectors.  In
particular, they capture long, low first shelves for which the coarse
integer reserve (\lfloor h\rfloor/2) sees no growth.  They do not cover
suffixes with several active action shelves or a short low shelf with large
(J).

For (J=1), the exact condition

\[
 D_1+S_1\ge\int_0^1\chi(s)q(r+s)\,ds
\]

is algebraically equivalent to the one-interface identity

\[
 D_A(r)=D_K(r)+n_0-2\int_r^\mu G_\mu(z)\,dz.
\]

Replacing the exact interface integral by (Q\beta(\eta)), or by (Q/4),
makes (TP) a **stronger sufficient condition**, not an equivalent
restatement.  The ball-remainder condition (D_K(r)\ge e) used when
(n_0=0) is another stronger sufficient condition.  No implication between
these two strengthened criteria is established here.

Numerical falsification searches over more than (10^6) exact-shell
parameter samples with (T>3/4), including integer and half-integer shifts,
found no violation of (TP).  A differential-evolution search over the
small blocks (1\le J\le6) found its smallest observed margin near
(r=1/2), (J=2), (K\approx4.4622), (\mu\approx1.5323), with margin
about (0.341).  These computations are diagnostic only.  A proof uniform
in the unbounded block length (J) is still missing, so (TP) must not be
cited as a theorem.

## 8. Why shape-only Stieltjes arguments cannot finish the proof

The exact shell formula for (q), not merely unimodality and the slope cap,
must enter the remaining proof.  Consider the rational piecewise-linear
action on (s\ge0)

\[
 B(s)=
 \begin{cases}
 \frac45,&0\le s\le\frac{101}{100},\\
 \frac45-\frac12(s-\frac{101}{100}),
   &\frac{101}{100}<s<\frac{261}{100},\\
 0,&s\ge\frac{261}{100}.
 \end{cases}
\]

It is nonnegative and decreasing, (0\le-B'\le1/2), and its slope magnitude
is single-peaked (zero, then (1/2), then zero).  It has only the first
action layer active at the samples (s=0,1), so its strict shifted count is

\[
 [B(0)+\tfrac14]_<+2[B(1)+\tfrac14]_< =1+2=3.
\]

But

\[
 2\int_0^\infty B(s)\,ds
 =2\left(\frac45\frac{101}{100}+\left(\frac45\right)^2\right)
 =\frac{362}{125}<3,
\]

and the defect is (-13/125).  Small smooth perturbations preserve the
negative sign and can replace the jumps in the slope by a genuine rise and
fall.  Thus monotonicity of (g), the (1/2)-slope cap, and generic
endpoint sawtooth bounds cannot prove the desired theorem.

## 9. Exact remaining obligation

The inverse-action route has reduced the global inner-tail theorem to the
following precise shell-specific statement:

> For the exact difference-of-ball action, (T>3/4),
> (J=\lceil\mu-r\rceil), and
> (\eta=\mu-r-(J-1)), prove
> \[
> D_J+w(A(r))+2\sum_{j=1}^{J-1}w(A(r+j))+w(G_K(r+J))
> \ge \frac{\arccos(\mu/K)}\pi\,\beta(\eta).
> \]

This retains the full convex suffix reserve, treats the fractional interface
sharply, and is strictly stronger than the original shifted-tail theorem
only through the controlled omission of favorable complete-inner-cell
curvature.  Any future proof must use additional quantitative structure of
the exact shell action or a quantitative ball-suffix reserve; the abstract
two-sawtooth/Stieltjes machinery alone stops here.
