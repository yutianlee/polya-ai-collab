# Round 10 parametric domain inventory

## Purpose

This note records every place where the Round 9 local-plateau proof used
$\varepsilon\le1/100$, rewrites the proof as exact endpoint conditions, and
explains the selected Round 10 constants.  It is exploratory provenance;
the promoted proof is the separate incumbent response plus independent
review.

Put

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2,
\qquad
\rho=1-y^2,
$$

and, in the dangerous branch $R=p-dm>0$,

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
$$

Fix an endpoint $y_0$, a threshold $C$, a lower slope-shift bound $d_0$,
a scaled-loss target $B$, and a displacement cap $\bar q$.  Write
$\rho_0=1-y_0^2$ and let $\pi_u$ be a proved rational upper bound for $\pi$.

## Exact sufficient conditions

The scaled proof closes if the following endpoint conditions hold.

1. Dangerous geometry:

   $$
   \rho_0>
   \cos\!\left(\frac{\pi(1-d_0)}2\right).
   $$

   Then $d>d_0$ and

   $$
   S<\left(1+\frac1{d_0}\right)P.
   $$

2. Plateau location:

   $$
   \frac{y_0^4}{C\rho_0}
   +\left(1+\frac1{d_0}\right)y_0
    \sqrt{\frac{2\pi_u}{C\rho_0}}
   <\bar q<1.
   $$

   This is the endpoint form of the unconditional shelf estimate and gives
   $t>1-\bar q$.

3. Synthetic-path monotonicity: with

   $$
   a_0=\frac{y_0^2}{\rho_0},
   \qquad
   D_0=
   2\pi_u^2
   \frac{y_0}{C}\left(1+\frac1{d_0}\right)
   \frac{1+\bar q+2a_0}{(1-\bar q)^3},
   $$

   require $D_0<2B$.

4. No-drop endpoint: with

   $$
   Q_0=1+\frac{y_0^2+y_0B}{C},
   \qquad
   q_0=\frac{y_0^2}{\rho_0}(Q_0-1),
   $$

   require

   $$
   B^2>
   \frac{2\pi_u^2Q_0}{(1-q_0)^2}.
   $$

   This yields $R<B/\sqrt\varepsilon$.

5. Complete action payment:

   $$
   \frac1{y_0}
   \left(
   \frac{2(140/99)C}{3(1571/500)}-B
   \right)
   -1
   >\frac{132}{175}.
   $$

   The right side pays the full interface remainder; the left includes the
   worst ordinary-floor loss.  Positivity also closes the $R\le0$ branch.

The local-slope identity, the action lower bound, and the ordinary-floor,
gain, interface, and strict spectral wall conventions are independent of
the chosen endpoint.  They do not need extrapolation.

## Selected exact endpoint

Choose

$$
y_0=\frac15,
\quad
\varepsilon_0=\frac1{25},
\quad
\rho_0=\frac{24}{25},
\quad
C=20,
\quad
d_0=\frac45,
\quad
B=\frac{73}{16},
\quad
\bar q=\frac{21}{80}.
$$

The elementary identity

$$
\cos^2\frac\pi{10}=\frac{5+\sqrt5}{8}
$$

and $\sqrt5<9/4$ prove $d>4/5$.  The exact endpoint ledgers are

$$
\widehat q
<\frac{1553}{6000}
<\frac{21}{80},
$$

$$
\frac{\partial H}{\partial P}
<\frac{4783063458}{3209046875}
<\frac32<2B,
$$

and

$$
B^2-
2\left(\frac{1571}{500}\right)^2
\frac{8381/8000}{(1-127/64000)^2}
=\frac{6451558662413}{130552324128000}>0.
$$

The final payment margin after the full interface cap is

$$
5\left(
\frac{2800000}{466587}-\frac{73}{16}
\right)-1-\frac{132}{175}
=\frac{7104880031}{1306443600}>0.
$$

Thus the exact selected theorem is

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
$$

## Why the Round 9 constants were not merely extrapolated

If one keeps both $C=125/8$ and the Round 9 loss target $B=361/80$, the
existing payment ledger requires

$$
y<
\frac{6562093/37326960}{307/175}.
$$

That sufficient inequality already fails at $\varepsilon=1/99$, because

$$
\left(\frac{307}{175}\right)^2
-99\left(\frac{6562093}{37326960}\right)^2
=\frac{307696871393039}{17240352323040000}>0.
$$

This is an obstruction to naively reusing the old constants, not a
counterexample to the theorem.  Increasing the threshold constant to $20$
creates a large exact payment margin and permits the wider endpoint.

## Seam consequence

The selected endpoint moves the seam to $\rho_s=24/25$.  On the new strip

$$
\frac{24}{25}\le\rho\le\frac{99}{100},
$$

the high threshold is at most $200000$.  The central endpoint satisfies
$K_0(24/25)<6000^2$.  Both lie below the unchanged Round 9 thin residual
ceiling $125^5/8$, so that thin ceiling becomes the global dominant one.

The executable exact ledger is
`computations/round10_verify_seam_constants.py`.
