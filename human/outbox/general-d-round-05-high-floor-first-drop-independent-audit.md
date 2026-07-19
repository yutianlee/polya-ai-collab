# Independent audit: Round 5 high-floor first-drop exhaustion

Date: 18 July 2026  
Files audited:

- human/outbox/general-d-round-05-high-floor-first-drop.md
- human/outbox/general-d-round-05-uniform-critical-gap.md

## Verdict

**PASS WITH REQUIRED LOCAL REPAIRS.** The qualitative exhaustion theorem
and the uniform critical-gap constant are valid. I found no missed escaping
regime and no ordinary- or strict-wall counterexample. One displayed strict
inequality in the critical-gap note is false when $M=0$, but replacing it by
a non-strict inequality leaves the final strict constant unchanged. Several
short arguments that are currently implicit should also be inserted before
the result is cited in the manuscript.

The mandatory correction is

\[
 -\mathcal L
 \le 2\int_M^N(f-H_\kappa(X))\,dX
 \le \frac{N-M}{2}
 <\frac1{4c_0}.
 \tag{A1}
\]

The first sign in display (6) of the critical-gap note is currently strict.
It is equality when $M=0$. The final sign in (A1) is still strict, so

\[
 -\mathcal L<\frac{3\pi}{8\sqrt2}
\]

and the gap $\pi/(8\sqrt2)$ are unchanged.

## 1. Exact interface and prefix geometry

This part passes exactly. With $x=r+p$, the first-drop condition gives

\[
 \lfloor A(x+1)+1/4\rfloor\le f-1,
 \qquad A(x+1)<h=f-\frac14.
\]

Since $x+1\le q\le\mu$ and $A$ decreases,

\[
 W=A(\mu)=G_K(\mu)<h.
\]

The established turning lower bound therefore gives $c_0\kappa<h$,
including at the ordinary wall $A(x)=h$.

For $H(t)=A(\mu-t)$, the $h$-level is unique and

\[
 M\le\mu-x<M+1.
\]

If the $f$-level exists, let $T$ be that level; otherwise $T=\mu$. A
negative candidate must have $A(x)<f$. Its negative shelf area is contained
between $\mu-x$ and $T$, where $0\le f-H\le1/4$, so

\[
 R_p\ge-\frac{T-(\mu-x)}2.
\]

Using $\mu-x=m+\alpha$, $0\le\alpha<1$, gives

\[
 R_p+\frac d2m\ge\frac{(1+d)M-T-d}{2}.
\]

Since $D_A(q)\ge0$, a negative reduced scalar forces

\[
 T>(1+d)M-d.
\]

No limiting or wall argument is hidden here. The case $p=0$ is harmless
because then the positive post-shelf term already precludes a negative
scalar.

## 2. Elasticity, the $T/M$ ratio, and a missing $f$-level

The radius-average identity

\[
 H(t)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{(\mu-t)^2}{R^2}}\,dR
\]

is exact. After subtracting $W=H(0)$, put

\[
 V=t(2\mu-t),\quad
 b_R=1-\frac{\mu^2}{R^2},\quad
 \phi_R(V)=\sqrt{b_R+V/R^2}-\sqrt{b_R}.
\]

Rationalization gives

\[
 \frac{V\phi_R'(V)}{\phi_R(V)}
 =\frac12\left(
 1+\frac{\sqrt{b_R}}{\sqrt{b_R+V/R^2}}
 \right)\ge\frac12.
\]

Thus $\phi_R(V)/\sqrt V$ is nondecreasing. The pointwise comparison has a
common positive factor and survives integration over $R$, proving

\[
 \frac{H(t_2)-W}{H(t_1)-W}
 \ge\sqrt{\frac{V(t_2)}{V(t_1)}}.
\]

When $M\to\infty$, write $r_*=T/M$ and $u=M/\mu$. Then

\[
 \frac{V(T)}{V(M)}
 =r_*\frac{2-r_*u}{2-u},
 \qquad 0<u\le\frac1{r_*}.
\]

For fixed $r_*>1$, this expression decreases in $u$ and is minimized at
$u=1/r_*$, with value $r_*^2/(2r_*-1)$. The note has
$\liminf r_*\ge2$, not pointwise $r_*\ge2$. Formally, apply the preceding
bound with $r_*\ge2-\eta$ eventually and then let $\eta\downarrow0$. This
proves

\[
 \liminf\frac{V(T)}{V(M)}\ge\frac43.
\]

The case in which the level $f$ is not reached is included: then $T=\mu$,
so $u=1/r_*$, exactly the minimizing endpoint, and $H(T)<f$ strengthens the
last comparison below.

Elasticity yields

\[
 \sqrt{\frac{V(T)}{V(M)}}
 \le\frac{H(T)-W}{h-W}
 \le\frac{f-W}{f-W-1/4}.
\]

Because $x\mapsto x/(x-1/4)$ decreases for $x>1/4$, this gives

\[
 \limsup(f-W)
 \le\frac1{2(2-\sqrt3)}
 =1+\frac{\sqrt3}{2}.
\]

If $M$ remains bounded, the slope bound
$H(M)-H(0)\le c_\rho M=o(1)$ gives the stronger
$f-W=1/4+o(1)$. Hence the pinning is valid even when $f$ varies.

## 3. Classification of every escaping sequence

The three imported automatic sectors do cover the reduced scalar, but the
exhaustion note should say this explicitly. A theorem proving
$D_A(r)\ge0$ does not by its statement alone exclude a negative lower
certificate $\mathcal S$.

The fixed-ratio and thin-high-energy proofs actually give the needed scalar
form. Their convex ball suffix and one-interface identity imply

\[
 D_A(q)\ge\frac12\lfloor K\eta_\rho\rfloor-2\delta,
\]

while $R_p\ge-p/2$. Therefore

\[
 \mathcal S\ge
 \frac12\bigl(
 \lfloor K\eta_\rho\rfloor+d(n-p)-p
 \bigr)-2\delta.
 \tag{A2}
\]

The thresholds in those proofs make the parenthesis exceed $4\delta$, so
they prove $\mathcal S>0$, not merely $D_A(r)\ge0$. The compact-optical
theorem directly proves positivity of
$R_p+d(n-p)/2$. Inserting (A2), or citing these scalar forms, removes the
only logical ambiguity in Section 4.

The fixed-ratio threshold is uniform on every ratio range bounded away from
$\rho=1$ and stays bounded as $\rho\downarrow0$. The active high-floor
condition gives $a>\pi(f-1/4)>\pi$. Consequently, any escaping negative
sequence must satisfy

\[
 \epsilon\to0,\qquad
 a\to\infty,\qquad
 s\kappa=\epsilon a<\frac{125}{8}.
\]

The ball turning expansion

\[
 G_R(R(1-y))=c_0Ry^{3/2}+O(Ry^{5/2})
\]

is uniform on the range used here. At the interface it gives

\[
 W=c_0\kappa+O(\kappa s^2)=c_0\kappa+o(1),
\]

because $\kappa s^2=s(s\kappa)\to0$. Combined with the interface pinning,
this proves

\[
 f-1-\frac{\sqrt3}{2}-o(1)
 \le c_0\kappa
 \le f-\frac14+o(1).
\]

In particular, $\kappa\asymp f$ with a positive lower constant already at
$f=2$.

## 4. Compact turning window

The exact estimate for $X_f$ is correct. At
$z=\mu-X_f/s$, monotonicity of the radius-average integrand gives

\[
 f=A(z)
 \ge\frac{K-\mu}{\pi}
 \sqrt{1-\frac{z^2}{\mu^2}}
 \ge\frac{\sqrt{\kappa X_f}}
 {\pi\sqrt{1-s^2}}.
\]

The last inequality uses
$0\le(\mu-z)/\mu\le1$. Hence $X_f/\kappa=O(1)$.

Before using $X_f$ globally, the note should insert the eventual
level-existence calculation

\[
 \frac{A(0)}f
 =\frac{a}{\pi f}
 =\frac{\kappa}{\pi sf}
 \asymp\frac1s
 \longrightarrow\infty.
 \tag{A3}
\]

Thus every escaping negative sequence eventually reaches the level $f$.
For bounded fixed $f$, this also follows directly from
$a=\kappa/s\to\infty$. The earlier convention $T=\mu$ remains necessary in
the pinning lemma but not in the eventual turning limit.

On $X/\kappa=O(1)$, both ball turning parameters are $O(s^2)$. Applying the
ball remainder to the outer and inner terms, including the factor
$(1-s^2)^{-1/2}$ in the inner term, gives

\[
 \sup_{0\le X\le X_f}
 \left|
 \mathcal H_{s,\kappa}(X)-H_\kappa(X)
 \right|
 =O(\kappa s^2)=o(1).
\]

On this same range,

\[
 H_\kappa'(X)=\frac{3c_0}{2}
 \left(
 \sqrt{1+X/\kappa}-\sqrt{X/\kappa}
 \right)
\]

has a universal positive lower bound. Since $f-W$ has a universal additive
bound, the mean-value estimate gives $X_f=O(1)$ uniformly, with no
fixed-$f$ assumption.

## 5. Floors tending to infinity

This branch passes without a hidden uniformity loss. The additive pinning
implies

\[
 \frac{\kappa}{f}\longrightarrow\frac1{c_0}.
\]

Equation (A3) ensures the level exists. The exact negative-area estimate and
$X_f=O(1)$ give

\[
 sR_p\ge-\frac{sT}{2}=-\frac{X_f}{2},
\]

and the post-shelf term is nonnegative. Thus the scaled prefix has a
uniform lower bound.

The root-free terminal estimate is valid simultaneously for all complete
levels:

\[
 D_A(q)\ge
 C_0K^{1/3}S_B-Q-2\int_q^\mu G_\mu,
 \qquad C_0^3=\frac\pi{12}.
\]

At a strict bracket wall as well as away from one,

\[
 B=[G_K(q)+1/4]_<
 \ge G_K(q)-\frac34
 \ge W-\frac34
 =f-O(1).
\]

Also $q\ge x+1$ and $A(x+1)<h$, so $Q\le f-1$. The interface cap is
uniformly bounded. Hence

\[
 sD_A(q)\ge
 C_0\kappa^{1/3}S_B-s(f-1)-O(s).
\]

Since $S_B\gg B^{2/3}$, the positive term is of order $f$, whereas

\[
 sf=(s\kappa)\frac f\kappa=O(1).
\]

Thus $sD_A(q)\to+\infty$. Together with the bounded-below prefix, this
excludes every escaping sequence with $f\to\infty$.

## 6. Bounded floors and finite-thickness convergence

Fix $f$ and pass to $\kappa\to\kappa_0$ in a compact subinterval of
$(0,\infty)$. The turning convergence is uniform on the compact window.

The proof of (29) is valid but should be displayed. Put

\[
 X_x=s(\mu-x),\qquad X_r=s(\mu-r).
\]

The shelf and first-drop inequalities imply

\[
 0\le A(x)-h
 <A(x)-A(x+1)
 \le c_\rho
 \longrightarrow0.
\]

Therefore $X_x\to M_0$, the $h$-level of the limiting profile. If
$X_{f,j}=sT$, then $X_{f,j}\to N_0$. Discarding only nonnegative shelf area
gives

\[
 sR_p
 =2\int_{X_x}^{X_r}
 (\mathcal H_{s,\kappa}-f)\,dX
 \ge
 -2\int_{X_x}^{X_{f,j}}
 (f-\mathcal H_{s,\kappa})\,dX.
\]

Also

\[
 sm=s(\mu-x)-s\alpha\longrightarrow M_0,
 \qquad d\longrightarrow1.
\]

This proves

\[
 \liminf s\left(R_p+\frac d2m\right)
 \ge
 -2\int_{M_0}^{N_0}
 (f-H_{\kappa_0}(X))\,dX
 \frac{M_0}{2}.
\]

The argument includes $M_0=0$.

At $q$, $s(\mu-q)=s\alpha\to0$, so
$G_K(q)\to w=c_0\kappa_0$. For each of the finitely many levels,

\[
 s\frac{\pi}{2\theta_k}
 \longrightarrow
 \frac{\pi}{2\sqrt2}
 w^{1/3}(k-1/4)^{-1/3}.
\]

The $Q$-term and interface cap are bounded and vanish after multiplication
by $s$. If $w+1/4$ is integral, the strict bracket in the limiting terminal
sum uses the smaller one-sided count. Approaching the wall from the other
side can only add a complete level. Therefore the terminal liminf is
wall-safe. The fractional-top reserve is nonnegative and is correctly
unused.

Multiplying the exact necessary inequality
$T>(1+d)M-d$ by $s$ gives

\[
 N_0\ge2M_0.
\]

Thus there is no missing endpoint, finite-thickness, or wall term in the
limiting scalar.

## 7. Uniform critical gap

The exact parameter identities

\[
 F(t)=\frac{3+t^4}{4t},\qquad
 u(t)=\frac{(1-t^2)^2}{4t^2},\qquad
 H_\kappa'(X)=\frac{3c_0}{2}t
\]

are correct. If $\mathcal L<0$, then $N>2M$. Under the contrary assumption
$t_f\le1/3$, one obtains $t_h<2/5$ and

\[
 \frac NM
 <
 \left(\frac{15128}{13125}\right)^2
 \left(\frac{25}{21}\right)^2
 =
 \frac{228856384}{121550625}
 <2.
\]

The rational arithmetic is exact. When $M=0$, the same contrary assumption
first forces $t_h<2/5$, contradicting $t_h=1$, so the ratio need not be
formed. Thus $t_f>1/3$.

It follows that $H_\kappa'>c_0/2$ throughout the level interval and

\[
 N-M<\frac1{2c_0}.
\]

With correction (A1),

\[
 -\mathcal L
 <\frac1{4c_0}
 =\frac{3\pi}{8\sqrt2}.
\]

Moreover,

\[
 \frac fw=F(t_f)<\frac{61}{27},
 \qquad
 w>\frac{27f}{61}
 \ge\frac{54}{61}
 >\frac34.
\]

Hence the strict terminal count contains the $3/4$-level and

\[
 \mathcal T(w)>\frac{\pi}{2\sqrt2}.
\]

The claimed uniform gap $\pi/(8\sqrt2)$ follows.

If $\mathcal L\ge0$, the condition $N_0\ge2M_0$ still forces $w>3/4$. For
$M_0>0$, the same parameter calculation shows that $t_f\le1/3$ would give
$N_0/M_0<2$; for $M_0=0$, one has $w=h>3/4$. Hence
$\mathcal T(w)>0$ and the limiting scalar is strictly positive in this case
as well.

## 8. Compactness, finite data, and wall wording

The preceding two sections exclude every unbounded negative sequence. The
active-width inequality prevents an inner high-floor sequence with bounded
$K$ from escaping through $\rho=1$, while $r<\mu$ prevents escape through
$\rho=0$ at bounded $K$. Thus the negative set is relatively compact in
the natural $(\rho,K,r)$ parameter space.

On a compact set, $f,n,p,Q,B$ are bounded integers. This proves the stated
finite-data conclusion. For precision, the introduction should say
**finitely many discrete data tuples**. Compactness plus finite integer data
does not, without an additional analytic-arrangement argument, automatically
prove that there are finitely many connected wall components. The theorem
itself only asserts finite bounds for $(f,n,p,Q,B)$, and that assertion is
correct.

## Exact repairs recommended before manuscript use

1. In the critical-gap note, replace the first strict sign in display (6)
   by $\le$, as in (A1).
2. In the exhaustion note, make the continuity step after
   $\liminf T/M\ge2$ explicit.
3. State the scalar automatic-sector inequality (A2), so there is no
   ambiguity between proving $D_A(r)\ge0$ and proving $\mathcal S\ge0$.
4. Insert the eventual level-existence calculation (A3) before the global
   use of $X_f$.
5. Add the two-line derivation of (29) from the exact scaled shelf integral
   and $A(x)-h\le c_\rho$.
6. Interpret “finite chambers” as finite integer data tuples unless a
   separate finiteness theorem for connected wall components is supplied.

With these local changes, the Round 5 high-floor first-drop exhaustion is
ready to be cited as a rigorous qualitative reduction to a compact residual
set. It does **not** certify that residual compact set and therefore does not
by itself close the general-dimensional theorem.

## Post-repair verification

The six repairs above were applied and independently re-read in context.
The interface-cap notation is now explicit:

\[
 \delta_q=\int_q^\mu G_\mu(z)\,dz.
\]

With \(L_K=\lfloor K\eta_\rho\rfloor\) in the fixed-ratio proof and
\(L_K=\lfloor KG_1(\rho)\rfloor\) in the thin-high-energy proof, the inserted
bound

\[
 D_A(q)\ge\frac{L_K}{2}-2\delta_q
\]

and hence (14a) agree with the two source proofs. Their thresholds give
\(L_K+d(n-p)-p>4\delta_q\), so the repaired text really proves positivity
of the reduced scalar.

The repaired prefix-limit identity has the correct orientation under
\(X=s(\mu-z)\); extending from \(X_r\) to \(sT\) or discarding the portion
beyond \(sT\) can only lower the retained negative-area bound. The endpoint
estimate \(A(x)-h<A(x)-A(x+1)\le c_\rho\) is also correct. The strict-wall
terminal convention is unchanged.

During this re-read I corrected one quantifier in the newly inserted
continuity sentence from “every \(\eta>0\)” to “every \(0<\eta<1\)”, because
the displayed assertion \(2-\eta>1\) requires that restriction. No formula
or conclusion changed.

**POST-REPAIR VERDICT: PASS.** No algebraic, notation, endpoint, or wall
error remains in the repaired passages. The input hashes certified by this
post-repair audit are:

- general-d-round-05-high-floor-first-drop.md:  
  50C5B986C98AA07176813673C50B5D5B133418CA8AC99F5B74E452013557B0BE
- general-d-round-05-uniform-critical-gap.md:  
  3823C9EF3F12C52C01B91BD758B7F3A4B90423D4E7701734658805EE53475D7C
