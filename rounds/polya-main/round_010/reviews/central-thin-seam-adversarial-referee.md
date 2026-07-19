# Round 10 adversarial referee: central--thin seam

## Verdict

**PASS after one dependency-boundary correction.**

No counterexample, unsupported inequality, missing branch, or unowned face
remains.  The initial global-union wording referred too tersely to the prior
compact envelope.  The packet and incumbent were corrected to permit and
reconstruct the zero endpoint, one endpoint, and left small-hole zone
directly, without using the compact-envelope conclusion being strengthened.

## 1. Constants audit

The enlarged-domain lower bound for $d$ is exact:

$$
\cos^2\frac\pi{10}
<\frac{29}{32}
<\left(\frac{24}{25}\right)^2,
\qquad
\left(\frac{24}{25}\right)^2-\frac{29}{32}
=\frac{307}{20000}>0.
$$

Thus $d>4/5$.  In the dangerous branch $R>0$ this gives

$$
S<\frac94P.
$$

The shelf estimate and the new endpoint bounds yield

$$
\widehat q
<\frac{1553}{6000}
<\frac{21}{80},
\qquad
\frac{21}{80}-\frac{1553}{6000}
=\frac{11}{3000}>0.
$$

Therefore

$$
t>\frac{59}{80},
\qquad
\frac{x_0}{K}>
\frac{24}{25}\frac{59}{80}
=\frac{177}{250}>\frac12.
$$

The local-slope derivation correctly gives

$$
P^2<
H(P,r)
=\frac{2\pi^2Q}{(1-\widehat q)^2}.
$$

The function $H$ decreases in $r$.  On the complete synthetic path with
$B=73/16$, both the original shelf ceiling and
$S(P',B)<9P'/4$ remain valid.  The exact derivative bound is

$$
\frac{\partial H}{\partial P}
<
\frac{4783063458}{3209046875}
<\frac32.
$$

At the no-drop endpoint,

$$
Q_*=\frac{8381}{8000},
\qquad
\widehat q_*=\frac{127}{64000},
$$

and the decisive margin is

$$
B^2
-2\left(\frac{1571}{500}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=\frac{6451558662413}{130552324128000}>0.
$$

Hence

$$
R<\frac{73}{16\sqrt\varepsilon}.
$$

The dangerous-branch action payment exceeds the full interface cap by

$$
\frac{7104880031}{1306443600}>0.
$$

In the branch $R\le0$,

$$
M>\frac{13533413}{466587}>1>4\delta.
$$

All exact ledger checks and the two focused tests pass.

## 2. Domain and dependency audit

The local $C=20$ theorem does not use any Round 9 estimate whose derivation
requires $\varepsilon\le1/100$.  The following are all rederived on
$0<\varepsilon\le1/25$:

- the lower bound for $d$;
- the dangerous-plateau location;
- the self-consistency denominator;
- the derivative on the full synthetic path;
- the scaled loss;
- the complete floor and interface payment.

Round 9 is used only on its valid domain:

- for the sharper $125/8$ threshold when $\varepsilon\le1/100$;
- at the shared face $\varepsilon=1/100$;
- for the all-frequency overlap when
  $\varepsilon\le1/15625$.

At $K=125/(8\varepsilon^2)$ the Round 10 theorem is not invoked unless its
separate stronger hypothesis $K\ge20/\varepsilon^2$ also holds.

The corrected packet marks the zero endpoint, one endpoint, and small-hole
left zone as corollary-only inputs.  The incumbent no longer invokes
SHELL-rho-compact-analytic-envelope as a premise.  For the left-zone
endpoint, independently,

$$
\omega_0-\frac1{16}>\frac{19}{528},
\qquad
C_*<\frac{13}{10},
$$

so

$$
H_0(1/16)<\frac{3432}{95}<64.
$$

There is no circular dependency.

## 3. Branch audit

1. If $p=n>0$, then $m=0$ and $P=r$.  This is the tested worst endpoint.
2. If $p=0$, then $R=-dm\le0$ and the easy branch applies.
3. If $n=0$, then $p=m=R=0$ and $M=L$.
4. The exact sign wall $R=0$ belongs to the easy branch.
5. Every synthetic $P'$ is no larger than the original $P$, so it inherits
   the unconditional shelf ceiling.

No branch uses the $x_0/K$ localization before it has established $R>0$.

## 4. Wall and face audit

- Equal ordinary floors imply a strict action difference smaller than one,
  including at an integer sample.
- At a gain wall, $\lfloor x\rfloor>x-1$ remains strict.
- At the interface wall, $\delta=0$.
- The strict spectral transfer is unchanged.
- Equality $\kappa=20$ is included.
- The face $\rho=24/25$ belongs to both the central and new seam zones.
- At $\rho=99/100$, the new threshold is $200000$ and the sharper Round 9
  threshold is $156250$; both zones are closed.
- At $\varepsilon=1/15625$, the aggregate and Round 9 thresholds both equal
  $125^5/8$.

No sliver is omitted and no strict-count convention changes across a face.

## 5. Central endpoint and ceiling

At $\rho=24/25$,

$$
a_\rho<13^2,
\qquad
\eta_\rho>\frac1{420},
$$

and the defining quadratic satisfies

$$
F(6000)>
\frac{1349693}{175}>0.
$$

Therefore

$$
K_0(24/25)<6000^2.
$$

The final ordering is exact:

$$
6000^2<\frac{125^5}{8}<2^{32},
\qquad
2^{35}>9\frac{125^5}{8}.
$$

The new all-ratio high-frequency ceiling is therefore $125^5/8$.  The full
all-frequency shell theorem remains open on the compact residual below that
ceiling.

## Final assessment

The incumbent proof, isolated clean-room proof, exact rational ledger,
dependency boundary, branches, walls, and seam integration all pass.  No
further mathematical correction is required before judging the Round 10
state promotion.
