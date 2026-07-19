# Round 12 adversarial referee: enlarged central--thin seam

## Verdict

**PASS.**  I audited the frozen packet, the incumbent proof, the independent
constant inventory, the executable exact ledger, and the isolated clean-room
reconstruction under the assumption that the proposed enlarged seam was
false.  I found no counterexample, reversed inequality, missing branch,
circular dependency, or unowned threshold face.

The first unsupported implication is **none**.

The audited local conclusion is

$$
0<\varepsilon\le\frac1{20},
\qquad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3,
$$

including threshold equality.  The central comparison

$$
K_0(19/20)<3300^2
$$

and the closed all-ratio consequence

$$
0<\rho<1,
\qquad K\ge3300^2
$$

also pass.  This remains a high-frequency theorem; it does not close the
compact residual below the new ceiling.

## 1. Sources, isolation, and dependency boundary

The isolated review states that it inspected only the frozen Round 12 packet
and the pre-Round-12 packets explicitly permitted there.  Its construction
supports that provenance statement.  It does not reproduce either Round 12
response route:

- the incumbent proves the scaled loss bound with $B=23/5$ by monotonicity in
  $r$ and a derivative estimate along a fixed-$r$ synthetic path;
- the independent inventory uses different bounds for $d$, displacement,
  the path derivative, and action payment, again with $B=23/5$;
- the clean-room proof obtains the distinct bound $B=5$ by first proving
  $P<10$ and then excluding the complete rectangle
  $5\le r\le P<10$, without using the incumbent derivative argument.

The only common ingredients are the frozen claim and the prior facts that the
packet deliberately supplied.  I find no indication that the clean-room
proof imported a Round 12 response, exploration, computation, or review.

The local theorem uses only the strict separated spectrum, phase enclosure,
weighted shifted-tail scaffold, high-angular theorem, and the audited
pre-threshold Round 3 low-interface decomposition and shelf estimate.  Every
estimate whose domain changed is rederived on
$0<\varepsilon\le1/20$ and $\kappa=K\varepsilon^2\ge24$.  In particular,
no intermediate Round 10 estimate valid only for
$\varepsilon\le1/25$ is extrapolated.

The fixed-ratio theorem, the accepted Round 10 theorem, the small-hole
endpoint, and the Round 11 all-frequency endpoint enter only the central
comparison or final union.  The desired enlarged seam and the compact
analytic envelope are not premises of the local proof.  Thus strengthening
the seam and then the envelope is acyclic.

## 2. Strict spectral and weighted reduction

The clean-room proof independently reconstructs the spectral-to-tail
interface.  If the strict phase count is denoted by $[\gamma(\nu)]_<$ and

$$
\gamma(\nu)<A(\nu)+\frac14,
$$

then

$$
[\gamma(\nu)]_<
\le\left\lfloor A(\nu)+\frac14\right\rfloor.
$$

The direction is still correct when the right-hand argument is an integer:
strictness makes the true count at most one less, while the ordinary floor is
retained only as an upper proxy.  With

$$
q_\ell=\left\lfloor A(\ell+\tfrac12)+\frac14\right\rfloor,
\qquad
\mathcal T_r=q_r+2\sum_{\ell>r}q_\ell,
$$

the identity

$$
\sum_{\ell\ge0}(2\ell+1)q_\ell=\sum_{r\ge0}\mathcal T_r
$$

has the correct multiplicities.  The clean-room integration-by-parts check
also has the correct direction: the half-integer counting primitive satisfies
$F_3(z)\le z^2/2$, while $-dA\ge0$.  Consequently the shifted-tail bounds
give

$$
\sum_{\ell\ge0}(2\ell+1)q_\ell
\le\int_0^K2zA(z)\,dz
=\frac{2}{9\pi}(K^3-(\rho K)^3).
$$

No equality for the strict spectral count is inserted at a phase or
eigenvalue wall.

## 3. Curvature, $d$, displacement, and local-slope direction

For $0<z<\mu=\rho K$,

$$
\sigma(z)=-A'(z)
=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right),
$$

and

$$
\sigma'(z)
=\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}>0.
$$

This is the required orientation.  The permitted shelf estimate comes from
the stronger curvature lower bound

$$
\sigma'(z)\ge\frac{1-\rho}{\pi\rho K},
$$

combined with the strict same-floor difference.  It is independent of the
old high-energy threshold and is therefore a valid imported input.

The incumbent proves

$$
d=1-\frac{2\arccos\rho}{\pi}>\frac{39}{50}
$$

by showing
$1-\cos(11\pi/100)>1/20$ with the alternating cosine bound.  The use of that
bound is legitimate because $0<11\pi/100<1$.  The inventory and clean-room
proofs instead use

$$
\cos^2\frac\pi8=\frac{2+\sqrt2}{4}
<\left(\frac{19}{20}\right)^2
$$

to obtain the independent estimate $d>3/4$.  Both directions are strict at
$\rho=19/20$.

In the dangerous branch $R=p-dm>0$, these estimates imply respectively

$$
S<(89/39)P
\quad\hbox{or}\quad
S<(7/3)P.
$$

The incumbent displacement calculation gives

$$
\widehat q<\frac{159019}{592800}<\frac{27}{100},
\qquad
\frac{x_0}{K}>\frac{1387}{2000}>\frac12.
$$

The independent inventory gives

$$
\widehat q<\frac{4169}{15200}<\frac{11}{40},
\qquad
\frac{x_0}{K}>\frac{551}{800}>\frac12.
$$

The clean-room proof takes a third route, bounding $U/K$ directly and
obtaining $U/K<9/20$ and $x_0/K>1/2$.  Each localization is established only
after entering $R>0$ and before using the outer-region slope.

For the incumbent variables

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1),
$$

one has

$$
1-\rho t=\varepsilon+\frac UK<y^2Q.
$$

The clean-room identities are even more explicit:

$$
Q=1+\frac{n+1}{K\varepsilon},
\qquad
\widehat q=\frac{n+1}{\mu},
\qquad
1-\varepsilon Q=\frac{\mu-n-1}{K}>0.
$$

They verify every denominator and squaring condition.  In all routes,
equal ordinary floors give

$$
A(x_0)-A(x_0+p)<1
$$

even when either endpoint value is integral.  Monotonicity of $\sigma$ and
the exact arccosine integral then yield

$$
\boxed{
P^2< H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.}
$$

No inequality direction or factor of $y$, $\rho$, or $\kappa$ is missing.

## 4. Incumbent and inventory synthetic-path audit

Write $a=y^2/\rho$.  Since

$$
S=P+\frac{P-r}{d},
$$

the exact derivative is

$$
\frac{\partial H}{\partial Q}
=2\pi^2\frac{1+\widehat q+2a}{(1-\widehat q)^3}>0.
$$

Thus $H$ decreases with $r$ at fixed $P,y,\kappa,d$, and along a path with
fixed $r$,

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac y\kappa\left(1+\frac1d\right)
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
$$

Suppose $r\ge B=23/5$.  On every synthetic point
$P'\in[B,P]$, the identity

$$
S'=P'+\frac{P'-B}{d}
$$

preserves both the appropriate $S'/P'$ bound and the original shelf ceiling,
because $P'\le P$.  Hence none of the displacement or denominator bounds is
lost between the endpoint and the actual plateau.

For the incumbent constants, the complete path satisfies

$$
\frac{\partial H}{\partial P'}
<\frac{541142250}{362174827}<\frac32.
$$

At the no-drop endpoint $P'=r=B$, where $S=B$,

$$
B^2-H(B,B)
>\frac{4189934997169}{10140435204025}>0.
$$

Therefore $P'^2-H(P',B)$ is strictly increasing and the assumed
$r\ge B$ contradicts self-consistency.  This proves

$$
R<\frac{23}{5\sqrt\varepsilon}.
$$

The independent inventory reaches the same loss bound with the distinct
caps $\widehat q<11/40$ and

$$
\frac{\partial H}{\partial P'}
<\frac{18122825063}{11584775000}<\frac85,
$$

and its independent endpoint margin is

$$
\frac{2196261729217}{5173691430625}>0.
$$

Both arguments include the entire synthetic path and the no-drop endpoint;
neither infers an endpoint extremum from sampled signs.

## 5. Clean-room $B=5$ rectangle audit

The clean-room argument does not rely on the preceding path derivative.
First, its direct bound $\widehat q<1/2$ and

$$
Q<1+\frac1{480}+\frac{7P}{288}
$$

turn self-consistency into

$$
P^2<\frac{481}{6}+\frac{35P}{18}.
$$

At $P=10$, the left side minus the right side is $7/18>0$, and that
difference is increasing for $P\ge10$.  Hence $P<10$.

If $r\ge5$, the complete possible rectangle is

$$
5\le r\le P<10.
$$

Throughout it,

$$
S\le P+\frac{P-5}{d}<\frac{50}{3},
$$

with the no-drop endpoint $P=r=5$, $S=5$ explicitly retained.  Exact
rational estimates then give

$$
Q-1<\frac{2533}{15840}<\frac4{25},
\qquad
\widehat q<\frac4{475},
$$

and therefore

$$
H(P,r)
<2\frac{484}{49}\frac{29}{25}\frac{41}{40}
=\frac{143869}{6125}<25.
$$

This contradicts $P^2\ge25$ everywhere in the assumed rectangle.  Thus

$$
R<\frac5{\sqrt\varepsilon}.
$$

This argument covers every intermediate pair $5\le r\le P<10$ and is a
genuinely separate verification of the plateau-loss mechanism.

## 6. Action payment and every exceptional branch

The exact action identity gives

$$
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
$$

For the incumbent route,

$$
K\eta>\frac{392}{55y}.
$$

After the possible unit floor loss and the bound
$R<23/(5y)$, the dangerous branch satisfies

$$
M>\frac{253}{25},
\qquad
M-4\delta>\frac{233}{25}>0.
$$

The safe branch satisfies the stronger margin

$$
M-4\delta>\frac{739}{25}>0.
$$

The independent inventory reproduces positive payment margins

$$
\frac{2402239573}{244958175}
\quad\hbox{and}\quad
\frac{7410273373}{244958175}.
$$

For the clean-room route,

$$
K\eta\ge\frac{16\sqrt2}{\pi y},
\qquad
\frac{16\sqrt2}{\pi}-5>\frac{117}{55}.
$$

Together with $R<5/y$ this gives $M>413/55$, safely above the full
interface loss.  In the branch $R\le0$, already
$\lfloor K\eta\rfloor\ge1>4\delta$.

The branch ownership is complete:

1. If $p=n>0$, then $m=0$ and $P=r$; all three dangerous-branch proofs
   include this no-drop geometry.
2. If $p=0<n$, then $R=-dn<0$ and the safe branch applies without division
   by $p$.
3. If $n=0$, the prescribed convention gives $p=m=R=0$, again in the safe
   branch.
4. The exact wall $R=0$ belongs to $R\le0$.
5. The first branch with $R>0$ is covered uniformly; none of the estimates
   divides by $R$ or assumes it is integral.

## 7. Floor, interface, threshold, and spectral walls

- The definition $n=\lfloor\mu-x_0\rfloor$ gives $0\le\beta<1$ even at an
  integer wall, so $U<1+p+m$ remains strict.
- Equal ordinary floors imply a difference strictly below one.  This remains
  true if either sampled action is integral.
- The universal inequality $\lfloor x\rfloor>x-1$ is strict even at a gain
  wall $x\in\mathbb Z$.
- The low/high interface is closed: $x_0<\mu$ uses the low decomposition,
  while $x_0=\mu$ is owned by the high-angular theorem.  At $q=\mu$ the
  interface remainder is $\delta=0$.
- Every use of the new threshold is non-strict in
  $\kappa\ge24$, while decisive floor, action, localization, or endpoint
  comparisons retain strict slack.  Thus
  $K=24/\varepsilon^2$ is included.
- The retained Round 10 theorem continues to own
  $\kappa=20$ on $0<\varepsilon\le1/25$; the new theorem does not weaken it.
- The strict phase and spectral transfers are unchanged at eigenfrequency,
  proxy-integer, and angular-cutoff walls.  The active cutoff is $\nu<K$, so
  the channel $\nu=K$ is excluded exactly.

The mandatory parameter faces $\varepsilon=1/100$, $1/25$, and $1/20$ and
the ratio faces $\rho=99/100$, $24/25$, and $19/20$ are all included by at
least one adjacent theorem.  On every overlap the previously sharper theorem
is retained.

## 8. Exact central endpoint

At $\rho=19/20$,

$$
a_\rho=38\pi<\frac{836}{7}<11^2,
\qquad
\eta_\rho>\frac{14000}{4199283},
\qquad
C_0<\frac{307}{175}.
$$

If

$$
F(Y)=\eta_\rho Y^2-\sqrt{a_\rho}\,Y-C_0,
$$

then its unique positive zero is $\sqrt{K_0(\rho)}$.  At $Y=3300$,

$$
F(3300)
>
\frac{14000}{4199283}3300^2
-11\cdot3300-\frac{307}{175}
=\frac{32985481}{7422975}>0.
$$

Since $F(0)<0$ and the two roots have opposite signs, the positive root lies
strictly below $3300$.  Hence $K_0(19/20)<3300^2$.  The fixed-ratio theorem
itself includes $K=K_0(19/20)$; the comparison locates that face strictly
below the new global ceiling.

## 9. Closed global union

The required zones fit without a gap:

1. The small-hole endpoint owns $0<\rho\le\rho_*$.  Every possible residual
   on $[\rho_*,1/16]$ has $K<64$.
2. On $[1/16,19/20]$, the permitted monotonicity gives
   $K_0(\rho)\le K_0(19/20)<3300^2$.
3. On $[19/20,24/25]$, the new theorem applies.  Its threshold there is at
   most $24\cdot25^2=15000$.
4. On $[24/25,99/100]$, the sharper Round 10 theorem applies.  Its threshold
   is at most $20\cdot100^2=200000$.
5. The Round 11 endpoint owns every frequency on $[99/100,1)$.

Both finite seam ceilings are strictly below
$3300^2=10890000$.  The shared faces $\rho_*$, $1/16$, $19/20$, $24/25$,
and $99/100$ are closed on at least one side, and $K=3300^2$ itself lies
strictly above every relevant analytic threshold.  This proves the stated
all-ratio high-frequency theorem, but leaves the compact residual below
$3300^2$ open.

## 10. Exact ledger and tests

The permanent standard-library rational ledger now executes all three finite
chains:

- the independent-inventory $d>3/4$, $B=23/5$ route;
- the incumbent $d>39/50$, $B=23/5$ route;
- the clean-room $d>3/4$, $B=5$ rectangle route;
- the common exact central endpoint and seam comparisons.

The final verification results are:

```text
computations/round12_verify_enlarged_seam.py          PASS
computations/tests/test_round12_enlarged_seam.py      4 passed
computations/tests                                    40 passed
```

These are exact finite-constant checks, not a Bessel-root certificate.

## Final assessment

The incumbent proof, independent constant inventory, isolated clean-room
proof, exact dual/path/rectangle ledgers, dependency boundary, exceptional
branches, wall ownership, central comparison, and closed global union all
pass.  No mathematical or provenance correction is required before the
Round 12 judge gate.
