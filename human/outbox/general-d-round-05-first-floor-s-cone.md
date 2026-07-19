# General dimension, Round 5: the ordinary first-floor cone \(s\ge 2\)

Date: 18 July 2026  
Scope: the ordinary first-floor branch on the true interface
\(A(r+p)=3/4\), in the closed universal active region, for

\[
 r\ge \frac12,\qquad p\ge0,\qquad s=n-p-1\ge2,
 \qquad K-\mu\ge\pi.
\]

Status: **proved in the universal active region**.  The proof is continuous
in the geometric parameters, so it covers both the integer and half-integer
starting grids needed in general dimension.  There is no residual subcone
in this active scope.  The complementary below-active region is owned by
the no-mode theorem for the spectral application; this note does not prove
the stronger standalone shifted-tail assertion there.

The directed-rounding verifier is

`scripts/general_d_first_floor_s_cone_verify.py`.

Its SHA-256 digest is

`D5BC93C60128AB23615720244AC6AD1FA88277B5EDFB98930E8BB22BEC23AE53`.

## 1. True-interface certificate

Write

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi},
 \qquad A=G_K-G_\mu,
\]

and set

\[
 x=r+p,\qquad q=r+n=x+s+1,
 \qquad \mu=q+\alpha,\qquad 0\le\alpha\le1.
\]

The endpoint \(\alpha=1\) is included as a closed chamber limit.  On the
first-floor wall put

\[
 a=A(r),\qquad A(x)=\frac34,\qquad
 u=A(q),\qquad h=G_K(\mu),\qquad
 c=\frac1\pi\arccos\frac\mu K.
\]

The complete strict tail count has post-crossing wall value \(1+2p\).
The concave inner trapezoids and the convex outer tangent triangle give
the wall-safe lower certificate

\[
 \mathcal C=
 p\left(a+\frac34\right)
 +(s+1)\left(\frac34+u\right)
 +\alpha(u+h)+\frac{h^2}{c}-(1+2p).
 \tag{1}
\]

This is the true-interface certificate, not a terminal-envelope
relaxation.  The usual monotonicity in \(K\) shows that the post-crossing
limit at \(A(x)=3/4\) is the correct minimum; at the wall itself the strict
bracket can only lower the discrete count.

Let

\[
 \beta=s+1+\alpha=\mu-x\ge3.
\]

Concavity of \(A\) on \([x,\mu]\) gives

\[
 (s+1)\left(\frac34+u\right)+\alpha(u+h)
 \ge \beta\left(\frac34+h\right).
\]

Indeed, the concave chord at \(q=x+s+1\) says

\[
 \beta u\ge \alpha\frac34+(s+1)h.
\]

Consequently

\[
 \boxed{
 \mathcal C\ge
 p\left(a-\frac54\right)
 +\beta\left(\frac34+h\right)
 +\frac{h^2}{c}-1.}
 \tag{2}
\]

This is the decisive simplification specific to the cone \(s\ge2\): all
dependence on \(s\) and \(\alpha\) is absorbed into the single length
\(\beta\ge3\).

## 2. Scale-free wall variables

Define

\[
 g(z)=\frac{\sqrt{1-z^2}-z\arccos z}{\pi},
 \qquad
 \rho=\frac\mu K,\quad \xi=\frac xK,\quad \eta=\frac rK,
\]

and

\[
 w=g(\xi)-\rho g(\xi/\rho),
 \qquad e=\rho-\xi,\qquad \epsilon=1-\rho.
\]

The radius-integral identity is

\[
 w=\frac1\pi\int_\rho^1
 \sqrt{1-\frac{\xi^2}{R^2}}\,dR.
 \tag{3}
\]

Since \(G_K(Kz)=K g(z)\), the wall equation is simply

\[
 Kw=\frac34,qquad K=\frac3{4w}.
 \tag{4}
\]

It follows that

\[
 \beta=Ke=\frac{3e}{4w},qquad
 K-\mu=K\epsilon=\frac{3\epsilon}{4w},
 \tag{5}
\]

and

\[
 p=K(\xi-\eta)=\frac{3(\xi-\eta)}{4w},
 \qquad h=K g(\rho)=\frac{3g(\rho)}{4w}.
 \tag{6}
\]

Thus the two chamber constraints used below are

\[
 e\ge4w \quad(\beta\ge3),
 \qquad
 3\epsilon\ge4\pi w \quad(K-\mu\ge\pi).
 \tag{7}
\]

The second inequality is the active-region constraint in this branch.

## 3. Exact control of the \(p\)-term

For fixed radius \(R\), the ratio

\[
 \frac{\sqrt{1-r^2/R^2}}{\sqrt{1-x^2/R^2}}
\]

decreases with \(R\).  Averaging over the wall integral and using
\(A(x)=3/4\) yields

\[
 a\ge\frac34Q,
 \qquad
 Q=\sqrt{\frac{1-\eta^2}{1-\xi^2}}.
 \tag{8}
\]

After multiplying (2) by \(16w^2/9\), the contribution of the first term
therefore satisfies

\[
 \frac{16w^2}{9}p\left(a-\frac54\right)
 \ge \frac w3(\xi-\eta)(3Q-5).
 \tag{9}
\]

Put

\[
 M(\xi)=\min_{0\le\eta\le\xi}
 (\xi-\eta)(3Q-5).
\]

Two elementary bounds are used.

### Global bound

For every \(0\le\xi<1\),

\[
 \boxed{M(\xi)\ge-2(1-\xi).}
 \tag{10}
\]

Let \(D=(\xi-\eta)/(1-\xi)\).  The condition \(\eta\ge0\) gives

\[
 Q\ge\frac{D+1}{\sqrt{2D+1}}.
\]

It remains to show

\[
 D\left(5-\frac{3(D+1)}{\sqrt{2D+1}}\right)\le2.
\]

For \(D\le2/5\) this is immediate.  For \(D\ge2/5\), squaring the
equivalent nonnegative inequality reduces it to

\[
 9D^4-32D^3+24D^2+12D-4>0.
 \tag{11}
\]

The verifier checks exact positive Bernstein coefficients on

\[
 [2/5,1/2],\ [1/2,1],\ [1,3/2],\ [3/2,2],\ [2,3],\ [3,4],
\]

and the tail \(D\ge4\) is positive term by term.

### Near-tip bound

For \(\xi\ge9/10\),

\[
 \boxed{M(\xi)\ge-(1-\xi).}
 \tag{12}
\]

If \(Q\ge5/3\), the assertion is immediate.  Otherwise

\[
 \eta^2>1-\frac{25}{9}(1-\xi^2)\ge\frac{17}{36}>\frac49,
\]

so \(\eta>2/3\), and hence

\[
 \frac{\xi+\eta}{1+\xi}>\frac45.
\]

Therefore \(Q^2\ge1+4D/5\).  For \(D\le1/5\) the desired bound is
trivial.  For \(D\ge1/5\), squaring reduces it to

\[
 \frac{36}{5}D^3-16D^2+10D-1>0.
 \tag{13}
\]

Exact Bernstein coefficients are positive on

\[
 [1/5,1/2],\ [1/2,1],\ [1,6/5],\ [6/5,2],\ [2,3],
\]

and the tail \(D\ge3\) is again positive term by term.

## 4. The reduced scale-free certificate

Combining (2), (4)--(10), and (6) gives

\[
 \frac{16w^2}{9}\mathcal C\ge J_2,
\]

where, writing \(g=g(\rho)\),

\[
 \begin{aligned}
 J_2
 &=-\frac23w(1-\xi)+ew+eg+\frac{g^2}{c}-\frac{16}{9}w^2\\
 &=w\left(\frac e3-\frac{2\epsilon}{3}\right)
   +eg+\frac{g^2}{c}-\frac{16}{9}w^2.
 \end{aligned}
 \tag{14}
\]

In the near-tip range \(\xi\ge9/10\), (12) gives the sharper lower bound

\[
 \frac{16w^2}{9}\mathcal C\ge J_1,
\]

with

\[
 J_1=w\left(\frac{2e}{3}-\frac\epsilon3\right)
   +eg+\frac{g^2}{c}-\frac{16}{9}w^2.
 \tag{15}
\]

No discontinuous switch between (14) and (15) occurs in the compact
verification: that calculation uses \(J_2\) only.  The sharper \(J_1\)
is reserved for the disjoint analytic cap \(\rho>49/50\).

## 5. Domain reductions

Set

\[
 t=\frac e\epsilon=\frac{\rho-\xi}{1-\rho}.
\]

At fixed \(\rho\), \(w(t)\) is increasing and concave, while
\(w(t)/t\) is decreasing.

First, \(\rho\le11/20\) is impossible under \(e\ge4w\).  At the physical
endpoint \(\xi=0\), one has

\[
 \frac{w(t)}t=\frac{\epsilon^2}{\pi\rho}>\frac\epsilon4,
\]

and the decreasing-ratio property makes the same strict inequality hold
at every earlier \(t\).

For \(11/20\le\rho\le39/50\), take \(t_0=3/\pi\).  A 4096-panel
directed Arb check proves

\[
 w(t_0)>\frac{3\epsilon}{4\pi}.
 \tag{16}
\]

If \(t\le t_0\), then \(w/t>\epsilon/4\), contradicting \(e\ge4w\).
If \(t\ge t_0\), monotonicity of \(w\) contradicts the active inequality
in (7).  Hence every simultaneous active, \(s\ge2\) point has

\[
 \rho>\frac{39}{50}.
 \tag{17}
\]

Also, (3) gives

\[
 w\ge\frac\epsilon\pi\sqrt{1-(\xi/\rho)^2}.
\]

Together with the active inequality, this implies

\[
 \frac\xi\rho\ge\frac{\sqrt7}{4}>\frac{33}{50}.
 \tag{18}
\]

## 6. The two analytic pieces

### 6.1 The universal region \(t\ge4\)

If \(e\ge4\epsilon\), (14), the positivity of \(eg+g^2/c\), and the
active bound \(w\le3\epsilon/(4\pi)\) give

\[
 \begin{aligned}
 J_2
 &\ge \frac23\epsilon w-\frac{16}{9}w^2\\
 &\ge \epsilon w\left(\frac23-\frac4{3\pi}\right)>0.
 \end{aligned}
 \tag{19}
\]

The directed value of the last coefficient is approximately
\(0.242253485088\).  This argument is valid for every \(\rho\), not just
near one.

### 6.2 The cap \(\rho>49/50\), \(0\le t<4\)

Here

\[
 \xi=1-(1+t)\epsilon>\frac9{10},
\]

so (15) applies.  Put

\[
 \rho_0=\frac{49}{50},\qquad \epsilon_0=\frac1{50},
\]

and define

\[
 G_0=\frac{2\sqrt{2\rho_0}}{3\pi},\qquad
 H_0=\frac{2\rho_0}{3},\qquad
 B_0=\frac{2\sqrt2}{3\pi\sqrt{\rho_0}},
\]

\[
 L(t)=(1+t)^{3/2}-t^{3/2}.
\]

The radius-integral formulas imply

\[
 g(\rho)\ge G_0\epsilon^{3/2},
 \qquad
 \frac{g(\rho)}c\ge H_0\epsilon,
 \qquad
 w\le B_0L(t)\epsilon^{3/2}.
 \tag{20}
\]

For the middle inequality, if \(\theta=\arccos\rho\), then

\[
 \frac gc=\rho\left(\frac{\tan\theta}{\theta}-1\right)
 \ge\frac{\rho\theta^2}{3}
 \ge\frac{2\rho\epsilon}{3}.
\]

For the last inequality, use (3) and

\[
 \frac{\sqrt{(R-\xi)(R+\xi)}}R
 \le\sqrt{\frac{2(R-\xi)}\rho}
\]

before integrating exactly in \(R\).

For \(0\le t\le1/2\), the function

\[
 (1-2t)L(t)
\]

is decreasing and at most one.  Dividing (15) by
\(\epsilon^{5/2}\) and using (20) gives

\[
 \frac{J_1}{\epsilon^{5/2}}
 \ge G_0H_0-\frac{B_0}{3}
 -\frac{16}{9}\sqrt{\epsilon_0}\,B_0^2L(1/2)^2
 >0.0421933580845.
 \tag{21}
\]

For \(1/2\le t<4\), the linear \(w\)-term in (15) is nonnegative,
\(eg\) contributes at least \(G_0\epsilon^{5/2}/2\), and \(L(t)\le
L(4)\).  Hence

\[
 \frac{J_1}{\epsilon^{5/2}}
 \ge G_0H_0+\frac{G_0}{2}
 -\frac{16}{9}\sqrt{\epsilon_0}\,B_0^2L(4)^2
 >0.108941570080.
 \tag{22}
\]

This closes the entire cap analytically.

## 7. Moving-boundary certificate on the compact strip

It remains to prove (14) for

\[
 \frac{39}{50}\le\rho\le\frac{49}{50},
 \qquad 0\le t\le4,
\]

subject to (7).  A direct rectangular enclosure loses the correlation
\(e\ge4w\).  The verifier instead follows its true moving boundary.

For fixed \(\rho\), regard \(w\) as a function of \(e\), so
\(\xi=\rho-e\).  With

\[
 \chi(z)=\frac{\arccos z}{\pi},
\]

one has

\[
 w_e=\chi(\xi)-\chi(\xi/\rho)>0,
\]

and

\[
 w_{ee}=\frac1{\pi\sqrt{1-\xi^2}}
 -\frac1{\pi\sqrt{\rho^2-\xi^2}}<0.
 \tag{23}
\]

Thus \(w\) is strictly increasing and concave.  Define

\[
 F(e)=e-4w(e).
\]

Crucially,

\[
 F(0)=-4g(\rho)<0,
\]

not zero.  Since \(F\) is strictly convex, its nonpositive set is an
initial interval.  Whenever the verifier proves \(F>0\) at the right
endpoint, there is exactly one beta-entry root \(e_\beta\), and

\[
 e\ge4w \quad\Longleftrightarrow\quad e\ge e_\beta.
\]

At that exact root, \(e_\beta=4w\), and (14) becomes

\[
 \boxed{
 J_b=\frac{g^2}{c}+eg-\frac{\epsilon e}{6}-\frac{e^2}{36}.}
 \tag{24}
\]

This substitution is made before interval evaluation, avoiding a
dependency copy of \(w\).

It remains to propagate positivity to the right.  Differentiating (14)
at fixed \(\rho\) gives

\[
 J_2'=w_e\left(\frac e3-\frac{2\epsilon}{3}
 -\frac{32w}{9}\right)+\frac w3+g.
 \tag{25}
\]

Concavity and \(w(0)=g\) imply

\[
 0<w_e\le\frac{w-g}{e}.
\]

Writing \(z=g/w\) and

\[
 X=\frac13-\frac{2\epsilon}{3e}-\frac{32w}{9e},
\]

(25) has the rigorous lower bound

\[
 \boxed{
 \frac{J_2'}w\ge
 \frac13+z+(1-z)\min(0,X).}
 \tag{26}
\]

The compact verifier proves both

\[
 J_b>0
 \quad\text{and}\quad
 \frac{J_2'}w>0
\]

on every accepted panel.  Therefore \(J_2>0\) from the beta-entry wall
through the whole active interval.

For certification, \(w\) decreases with \(\rho\) at fixed \(t\) and
increases with \(t\) at fixed \(\rho\); \(g(\rho)\) and \(c(\rho)\)
decrease with \(\rho\).  Hence endpoint hulls enclose every quantity on a
\((\rho,t)\)-rectangle.  The code:

1. isolates a common enclosure of \(e_\beta\) by 36 rational bisections;
2. isolates the active upper root for \(\rho<4/5\), and safely overcovers
   by \(t\le4\) for \(\rho\ge4/5\);
3. checks (24) by directed Arb bounds;
4. adaptively subdivides only in \(t\) to prove (26);
5. subdivides the outer \(\rho\)-panel if any of these steps is unresolved.

The transition \(\rho=4/5\) is inserted as an exact rational panel edge.
All subdivision coordinates are rational.  Binary floating point is used
only for printed diagnostics and never for a sign decision.

## 8. Replay record

Run

```text
python scripts/general_d_first_floor_s_cone_verify.py --precision 384
```

The 384-bit replay reports

```text
PASS exact domain reductions:
  rho>39/50 in the simultaneous active, beta>=3 wall domain
  u=x/mu>=sqrt(7)/4>33/50
PASS exact eta-minimization lemmas:
  global M(xi)>=-2(1-xi)
  local xi>=9/10 bound M(xi)>=-(1-xi)
PASS analytic rho>49/50 cap constants:
  e>=4epsilon margin coefficient ~0.242253485088
  0<=e/epsilon<=1/2 margin ~0.0421933580845
  1/2<=e/epsilon<4 margin ~0.10894157008

PASS compact ratio sector
  rho-panels=507, rho-splits=253, empty=0, positive=254
  derivative-boxes=2422, max-rho-depth=12, max-t-depth=5
  smallest beta-boundary J_2 lower endpoint ~5.57124666798e-09
  smallest normalized derivative lower endpoint ~0.0010973528439
```

The same certificate was replayed independently at 256 and 512 bits.
Both runs had the same panel counts and strictly positive lower endpoints.

## 9. Conclusion and exact scope

The low-\(\rho\) exclusion (17), the universal region (19), the analytic
cap (21)--(22), and the moving-boundary compact certificate (24)--(26)
cover every possible active point.  Hence

\[
 \boxed{\mathcal C>0}
\]

for the full continuous ordinary first-floor wall cone \(\beta\ge3\),
equivalently \(s\ge2\), inside \(K-\mu\ge\pi\).  In particular, this
proves all required active half-grid cases \(r\ge1/2\), every integer
\(p\ge0\), and every chamber parameter \(0\le\alpha\le1\).

There is no residual within this active cone.  Combined with the no-mode
theorem below the universal active wall, this closes the entire ordinary
first-floor branch needed for the general-dimensional spectral theorem.
It does not prove a standalone below-active shifted-tail theorem or claim
closure of branches outside the ordinary first-floor sector.
