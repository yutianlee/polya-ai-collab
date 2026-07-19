# General dimension, Round 9b: exact level-wall reduction for the missing \(f=1\) row

Date: 18 July 2026

Status: rigorous exact reduction and compact certificate specification.  The
reduction covers the entire ordinary first-floor tail, and hence in particular
the previously omitted no-drop row \(f=1,\ p=n\).  The two final normalized
sign inequalities have not yet been certified in this note, so no global
\(f=1\) closure is claimed here.

## 1. Setup and the missing scope

Let

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}
 \quad(0\leq z<a),
 \qquad G_a(z)=0\quad(z\geq a),
\]

and put

\[
 \mu=\rho K,
 \qquad A=G_K-G_\mu,
 \qquad [x]_<:=\max\{0,\lceil x\rceil-1\}.
\]

For a positive integer or half-integer start \(r\geq1/2\), define

\[
 T_A(r)=[A(r)+\tfrac14]_<
 +2\sum_{j\geq1}[A(r+j)+\tfrac14]_<,
 \qquad
 D_A(r)=2\int_r^K A(z)\,dz-T_A(r).
 \tag{1}
\]

The first-floor condition is

\[
 \left\lfloor A(r)+\frac14\right\rfloor=1,
 \qquad
 \frac34\leq A(r)<\frac74.
 \tag{2}
\]

The already certified ordinary first-floor argument treats the first-drop
case.  The no-drop modules in the current manuscript begin at \(f=2\).
Consequently

\[
 f=1,\qquad p=n\geq1
 \tag{3}
\]

is a genuine omitted row.  Nothing in the \(f\geq2\) finite certificate
silently contains it: its corner has \(Q=B=0\), so the root-free cutoff used
there is singular.

The action \(A\) is continuous and strictly decreasing on \([0,K]\).  On the
inner part this follows from

\[
 -A'(z)=\frac{\arccos(z/K)-\arccos(z/\mu)}\pi>0,
\]

and on the outer part \(A=G_K\).  The equality case \(A(r)=3/4\) in (2) has
\(T_A(r)=0\) and is automatic.  Hence below we assume \(A(r)>3/4\).

## 2. The first-floor tail has only one vertical level

Let \(b=3/4\), and let \(y\in(r,K)\) be the unique point such that

\[
 A(y)=b.
 \tag{4}
\]

Because \(A(r)<7/4\) and \(A\) decreases, every strict sample in (1) is
either zero or one.  More precisely,

\[
 [A(r+j)+\tfrac14]_<
 =\mathbf 1_{\{r+j<y\}}.
\]

It follows that, away from the lower level wall,

\[
 \boxed{T_A(r)=2\lceil y-r\rceil-1.}
 \tag{5}
\]

This identity does not use the interface index, the first-drop index, or the
terminal ball levels.  It therefore applies to every \(f=1\) tail, including
both \(p<n\) and \(p=n\).

## 3. Rigorous chamber-to-level-wall deformation

Fix \((\mu,r)\), and vary \(K>\mu\).  The radius derivative

\[
 \partial_KG_K(z)=\frac1\pi\sqrt{1-\frac{z^2}{K^2}}
 \quad(z<K)
\]

shows that \(A(z)\), and hence the level position \(y\), increases strictly
with \(K\).  In a chamber on which

\[
 P:=\lceil y-r\rceil
 \tag{6}
\]

is fixed, (5) is fixed and

\[
 \boxed{
 \partial_KD_A(r)
 =\frac2\pi\int_r^K\sqrt{1-\frac{z^2}{K^2}}\,dz>0.}
 \tag{7}
\]

Lower \(K\) until the lower boundary of this count chamber is reached.  At
that boundary

\[
 y-r=L:=P-1\in\mathbb Z_{\geq0}.
 \tag{8}
\]

The one-sided value inherited from the open chamber retains the count

\[
 2P-1=2L+1.
 \tag{9}
\]

Equation (7) proves that the original chamber value is bounded below by the
following open-side wall scalar:

\[
 \boxed{
 \mathcal F(r;K,\mu,y)
 :=2\int_r^K A(z)\,dz-2(y-r)-1.}
 \tag{10}
\]

The strict equality face is more favorable.  If \(L\geq1\), the sample at
\(y=r+L\) is absent and the actual wall count is \(2L-1\), exactly two less
than (9).  Thus

\[
 D_A(r)\big|_{\rm strict\ wall}=\mathcal F(r;K,\mu,y)+2
 \qquad(L\geq1).
 \tag{11}
\]

For \(L=0\), the actual count is zero and the gain over (9) is one.  In the
no-drop row (3), the endpoint sample \(q=r+n\) has ordinary floor one, so
\(A(q)\geq b\) and hence \(y\geq q\).  Therefore

\[
 L=y-r\geq n\geq1
\]

on an equality wall in that row, and the full two-unit gain (11) always
applies.

This proves the wall reduction without moving a strict count through an
equality face.  It also explains why reducing every open chamber only to the
particular wall \(A(q)=3/4\) is not valid: a radial level wall can be met
first.  The global level \(y\), rather than \(q\), is the correct deformation
coordinate.

## 4. Exact elimination of the lattice start

For fixed \((K,\mu,y)\), relax \(r\) continuously from the positive
integer/half-integer grid to \(0\leq r\leq y\).  Differentiating (10) gives

\[
 \boxed{\partial_r\mathcal F=2(1-A(r)).}
 \tag{12}
\]

Also

\[
 A(0)=\frac{K-\mu}{\pi}=\frac\delta\pi,
 \qquad \delta:=K-\mu.
 \tag{13}
\]

There are exactly two cases.

### 4.1. The lower-width case

If \(\delta\leq\pi\), then \(A(0)\leq1\), so (12) is nonnegative on
\([0,y]\).  The relaxed minimum occurs at \(r=0\).  Since

\[
 2\int_0^aG_a(z)\,dz=\frac{a^2}{4},
\]

the exact target becomes

\[
 \boxed{
 \mathcal F_0(K,\mu)
 :=\frac{K^2-\mu^2}{4}-2y-1\geq0,
 \qquad A(y)=\frac34,\qquad \delta\leq\pi.}
 \tag{14}
\]

This formula is relevant to the bare shifted-tail theorem.  In the current
spectral proof, the region \(\delta\leq\pi\) is already owned by the no-mode
theorem, but (14) gives an independent exact target if one wants the stronger
tail statement there.

### 4.2. The active-width case

If \(\delta\geq\pi\), let \(z\in[0,y)\) be the unique point satisfying

\[
 A(z)=1.
 \tag{15}
\]

At \(\delta=\pi\) one has \(z=0\).  For \(\delta>\pi\), (12) is negative
on \([0,z)\) and positive on \((z,y]\), so the relaxed minimum occurs at
\(r=z\).  With

\[
 J_R(t):=2\int_t^R G_R(v)\,dv,
\]

the exact active target is

\[
 \boxed{
 \mathcal F_1(K,\mu)
 :=J_K(z)-J_\mu(z)-2(y-z)-1\geq0,}
 \tag{16}
\]

subject to (4), (15), and \(\delta\geq\pi\).  Targets (14) and (16)
agree at \(\delta=\pi\).

Equations (5)--(16) prove the following exact reduction.

### Proposition 4.1 (first-floor level-wall reduction)

If (14) and (16) hold on their stated domains, then

\[
 D_A(r)\geq0
\]

for every positive integer or half-integer start whose ordinary first floor
is \(1\).  In particular, they close every no-drop branch \(f=1,\ p=n\).

No assertion about the signs in (14) and (16) is made yet.

## 5. Dimensionless compact form

The two targets have a compact two-parameter normalization.  Put

\[
 g(t)=G_1(t),
\]

and define the normalized shell action by the positive radius average

\[
 \boxed{
 a_\rho(t)
 :=g(t)-\rho g(t/\rho)
 =\frac1\pi\int_\rho^1
 \left(1-\frac{t^2}{v^2}\right)_+^{1/2}\,dv.}
 \tag{17}
\]

The second term is understood as zero for \(t\geq\rho\).  Formula (17),
rather than subtraction of two nearby actions, is the preferred interval
representation.

Set

\[
 x=\frac yK,
 \qquad a=a_\rho(x),
 \qquad b=\frac34.
\]

The level equation \(A(y)=b\) eliminates the scale exactly:

\[
 \boxed{K=\frac ba,\qquad y=\frac{bx}{a}.}
 \tag{18}
\]

The normalized central height is

\[
 \lambda:=A(0)
 =\frac{b(1-\rho)}{\pi a}.
 \tag{19}
\]

For any relevant tail \(y\geq r\geq1/2\), so

\[
 a\leq2bx=\frac32x.
 \tag{20}
\]

For the no-drop row \(n\geq1\), the stronger \(y\geq q\geq3/2\) gives

\[
 \boxed{a\leq\frac{x}{2}.}
 \tag{21}
\]

Since \(y>0\) and \(A\) decreases, \(A(0)>A(y)=b\).  In a division-free
form this is

\[
 1-\rho>\pi a.
 \tag{22}
\]

### 5.1. Polynomial target below the unit height

The condition \(\lambda\leq1\) is

\[
 b(1-\rho)\leq\pi a.
 \tag{23}
\]

Substituting (18) in (14), and multiplying by the positive factor
\(4a^2\), gives the continuous compact target

\[
 \boxed{
 P_0(\rho,x)
 :=b^2(1-\rho^2)-8bxa-4a^2\geq0.}
 \tag{24}
\]

For \(b=3/4\), this is

\[
 P_0=\frac9{16}(1-\rho^2)-6xa-4a^2.
\]

Thus the bare lower-width problem is a sign check on a closed subset of
\([0,1]^2\), described by (17), (20), (22), and (23).  Multiplication by
\(a^2\) removes the apparent large-\(K\) singularity.

### 5.2. Polynomial target above the unit height

The active condition \(\lambda\geq1\) is

\[
 b(1-\rho)\geq\pi a.
 \tag{25}
\]

Let \(u=z/K\).  Since \(a_\rho\) is strictly decreasing, (15) has the
unique normalized root

\[
 \boxed{a_\rho(u)=\frac ab=\frac43a,\qquad0\leq u<x.}
 \tag{26}
\]

Define the noncancelling normalized terminal area

\[
 \boxed{
 j_\rho(u):=2\int_u^1a_\rho(t)\,dt.}
 \tag{27}
\]

Then

\[
 J_K(z)-J_\mu(z)=K^2j_\rho(u),
\]

and (16), multiplied by \(a^2>0\), is exactly

\[
 \boxed{
 P_1(\rho,x,u)
 :=b^2j_\rho(u)-2ba(x-u)-a^2\geq0,}
 \tag{28}
\]

with \(u\) constrained by (26).  At \(b=3/4\),

\[
 P_1=\frac9{16}j_\rho(u)-\frac32a(x-u)-a^2.
\]

Equations (17) and (27) are positive integral formulas throughout the
closed unit cube.  Consequently (24) and (28), together with the root
relation (26), are a compact certificate problem with two free variables;
\(u\) is a monotone implicit coordinate, not a third free parameter.

## 6. Compact certificate needed by the current active proof

The independent small-\(s\) theorem in
`human/outbox/general-d-round-09-no-drop-f1-small-s.md` proves the complete
no-drop row when

\[
 s:=\sqrt{\frac{K-\mu}{K}}\leq\frac1{10}.
\]

It also proves that a residual active candidate satisfies

\[
 s>\frac1{10},
 \qquad K<\frac{33000}{7},
 \qquad 1\leq n\leq754.
 \tag{29}
\]

In the normalized variables these imply

\[
 \boxed{
 0\leq\rho<\frac{99}{100},
 \qquad a=\frac bK>\frac7{44000}.}
 \tag{30}
\]

The no-drop condition supplies (21), and the universal active region
supplies (25).  Therefore the only certificate needed to close the missing
row in the present spectral proof is (28) on the explicit compact domain

\[
 \boxed{
 \begin{gathered}
 0\leq\rho\leq\frac{99}{100},\qquad
 0<x<1,\qquad
 a=a_\rho(x)\geq\frac7{44000},\qquad
 a\leq\frac x2,\\
 \frac34(1-\rho)\geq\pi a,\qquad
 a_\rho(u)=\frac43a,\qquad0\leq u<x.
 \end{gathered}}
 \tag{31}
\]

This domain stays away from both sources of numerical degeneracy:
\(\rho=1\) and \(a=0\).  It no longer needs a discrete loop over the
754 possible values of \(n\); the exact derivative (12) has already removed
that variable.

For the stronger bare shifted-tail theorem, certify (24) on the
lower-width domain and (28) on the full active domain.  The scaled targets
remain continuous at the large-\(K\) boundary.  A stable thin chart, if
needed there, is obtained by writing

\[
 \frac{a_\rho(x)}{1-\rho}
 =\frac1\pi\int_0^1
 \left(1-\frac{x^2}{(\rho+(1-\rho)v)^2}\right)_+^{1/2}\,dv.
 \tag{32}
\]

## 7. Executable directed-Arb certificate design

A verifier for (31) can be short and auditable.

1. Subdivide the rational rectangle
   \([0,99/100]\times[0,1]\) in \((\rho,x)\).
2. Enclose \(a_\rho(x)\) by the positive radius-average formula (17).
   Split boxes crossing \(x=\rho\), so no positive-part ambiguity is used
   in a sign decision.
3. Prune a box only when it rigorously violates one of the necessary
   inequalities in (31).
4. On every surviving box, isolate the unique root \(u\) in (26) by
   directed bisection.  Monotonicity of \(a_\rho\) makes the two endpoint
   tests one-sided and exact.
5. Enclose \(j_\rho(u)\) by the positive integral (27).  An equivalent
   cancellation-free swapped form is
   \[
    j_\rho(u)=\frac2\pi
    \int_{\max\{\rho,u\}}^1
    \int_u^v\sqrt{1-\frac{t^2}{v^2}}\,dt\,dv.
   \]
   Split at \(u=\rho\) when necessary.
6. Accept a leaf only when the outward lower endpoint of \(P_1\) in (28)
   is strictly positive.  Otherwise bisect the widest normalized
   coordinate.  A depth or box cap is a certificate failure, never a pass.
7. Replay at two higher precisions and require identical coverage and empty
   standard error.  Independently verify the source hash and the exact
   union of leaf boxes.

The same engine can certify \(P_0\) without a root or a terminal integral.

## 8. Obstruction to reusing the current low-floor verifier unchanged

Simply adding `f=1` to the current \(f=2,3\) low-floor loop is not safe.

* The lower and corner phases have \(Q=0\), so the existing root-free
  cutoff divides by a zero level sum.
* The frozen constants use \(\kappa\geq21/8\), whereas the \(f=1\)
  endpoint only gives \(\kappa>9/8\).
* The existing terminal lower bound can be negative even when the exact
  scalar has a large positive reserve.

For the last point, a floating-point diagnostic wall has approximately

\[
 \begin{gathered}
 n=4,\qquad s=0.5999968,\qquad \alpha=\frac{23}{24},
 \qquad K=8.8021426,\qquad \mu=5.6334052,\\
 r=0.6750719,\qquad q=4.6750719,\qquad
 A(q)=0.75,\qquad A(r)=1.0039940.
 \end{gathered}
\]

The exact-angle lower expression used by the old verifier is about
\(-0.13586\), while the exact open-side wall scalar is about \(1.07589\).
This is not a counterexample to the shifted-tail inequality; it is a
counterexample to that lower bound being strong enough for the \(f=1\)
row.  The level-wall targets (24) and (28) retain the missing continuous
area.

## 9. Exact conclusion

The missing row has been reduced rigorously as follows:

\[
 \boxed{
 \begin{array}{c}
 f=1\text{ tail}\\
 \Downarrow\\
 \text{one global level }A(y)=3/4\\
 \Downarrow\\
 \text{one-sided level wall }y-r\in\mathbb Z\\
 \Downarrow\\
 \partial_r\mathcal F=2(1-A(r))\\
 \Downarrow\\
 P_0\geq0\text{ below }A(0)=1,
 \quad P_1\geq0\text{ above }A(0)=1.
 \end{array}}
\]

For the current active no-drop proof, the independent small-\(s\) theorem
reduces the remaining task further to the nonsingular compact domain (31).
Until a directed-Arb replay proves \(P_1>0\) there, this note is an exact
reduction and certificate plan, not a closure theorem.
