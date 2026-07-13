# Lemma Packet: Compact-Ratio Analytic Reduction and Certificate Domain

Obligations: `SHELL-rho-compact` and `COMP-certified-bessel`.

Round: 8.

This packet freezes the analytic covering problem before any finite
certificate is designed.  It does not assert that the residual domain has
already been certified.

## Constants and target

Let

$$
G_1(z)=\frac1\pi\left(\sqrt{1-z^2}-z\arccos z\right),
\qquad 0\le z\le1,
$$

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*:=\frac{\omega_0}{1+2C_*},
$$

and

$$
\varepsilon_*=2^{-18}.
$$

The endpoint theorems already prove the shell Pólya inequality for every
$K\ge0$ when

$$
0<\rho\le\rho_*
\qquad\hbox{or}\qquad
1-\varepsilon_*\le\rho<1.
$$

The only remaining ratio interval is

$$
I_*=[\rho_*,1-\varepsilon_*].
$$

For $\rho\in I_*$, prove

$$
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge0).
\tag{1}
$$

The two endpoints of $I_*$ are included analytically and must not be sent to
a numerical certificate.

## Permitted proved inputs

1. `SHELL-rho-zero-endpoint`, including equality at $\rho=\rho_*$.
2. `SHELL-rho-one-endpoint`, including equality at
   $\rho=1-2^{-18}$.
3. `SHELL-high-angular-shifted-tails`: if $\rho K\le1/2$, every
   half-integer tail starts at or above the inner interface, so (1) holds.
4. `SHELL-low-interface-small-hole`: for $\rho<\omega_0$, (1) holds when

   $$
   K\ge H_0(\rho):=\frac{C_*}{\omega_0-\rho}.
   \tag{2}
   $$

5. `SHELL-thin-width-zero-count`: the strict count is zero when

   $$
   (1-\rho)K\le\pi.
   \tag{3}
   $$

6. `SHELL-fixed-rho-high-energy`: with

   $$
   a_\rho=\frac{2\pi\rho}{1-\rho},
   \qquad
   \eta_\rho=G_1(\max\{\rho,1/2\}),
   \qquad
   C_0=1+\frac{8\sqrt2}{15},
   $$

   define

   $$
   K_0(\rho)=
   \left(
   \frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
        {2\eta_\rho}
   \right)^2.
   \tag{4}
   $$

   Then (1) holds for $K\ge K_0(\rho)$.
7. For $\varepsilon=1-\rho\le1/100$, the combined Round 5--6 thin-shell
   theorems prove (1) throughout

   $$
   0\le K\le L(\varepsilon):=\frac1{8\varepsilon^{5/2}}
   \tag{5}
   $$

   and throughout

   $$
   K\ge U(\varepsilon):=\frac{64}{\varepsilon^2}.
   \tag{6}
   $$

No floating-point root scan, asymptotic root table, or uncertified
quadrature is a permitted proof input.

## Required analytic reconstruction

Use the exact rational switch points

$$
\rho_L=\frac1{16},
\qquad
\rho_T=\frac{99}{100}.
$$

### Zone L: small-hole side

For

$$
\rho_*\le\rho\le\rho_L,
$$

the analytic inputs cover

$$
K\le\frac1{2\rho}
\qquad\hbox{and}\qquad
K\ge H_0(\rho).
\tag{7}
$$

Thus the only possible residual is

$$
\boxed{
\mathcal R_L=
\left\{(\rho,K):
\rho_*\le\rho\le\frac1{16},\quad
\frac1{2\rho}\le K\le H_0(\rho)
\right\}.
}
\tag{8}
$$

At $\rho=\rho_*$ the two bounds meet exactly, and the endpoint theorem
already proves every $K$.

The reconstruction must verify, using for example
$\sqrt3>5/3$, $\sqrt2<3/2$, and $\pi<22/7$, that

$$
\omega_0-\frac1{16}>\frac{19}{528},
\qquad
C_*<\frac{13}{10},
\qquad
H_0(1/16)<64.
\tag{9}
$$

Since $H_0$ is increasing, $\mathcal R_L$ lies below $K<64$.

### Zone C: central compact interval

For

$$
\frac1{16}\le\rho\le\frac{99}{100},
$$

the analytic inputs cover (3) and (4).  The only possible residual is

$$
\boxed{
\mathcal R_C=
\left\{(\rho,K):
\frac1{16}\le\rho\le\frac{99}{100},\quad
\frac{\pi}{1-\rho}\le K\le K_0(\rho)
\right\}.
}
\tag{10}
$$

The reconstruction must prove that $K_0$ is increasing.  One endpoint-safe
route is:

- $a_\rho$ is strictly increasing;
- $G_1'(z)=-\arccos(z)/\pi<0$ for $0\le z<1$, so $\eta_\rho$ is
  nonincreasing;
- $y=\sqrt{K_0}$ is the positive root of

  $$
  \eta y^2-\sqrt a\,y-C_0=0,
  $$

  hence it increases with $a$ and decreases with $\eta$.

At $\rho=99/100$, the exact estimates

$$
a_\rho=198\pi<792,
\qquad
\eta_\rho
\ge\frac{2\sqrt2}{3\pi}\left(\frac1{100}\right)^{3/2}
>\frac1{6000},
\tag{11}
$$

together with $C_0<9/5$ and $0<\eta_\rho<1$, imply

$$
\sqrt{a_\rho}<30,
\qquad
\sqrt{a_\rho+4\eta_\rho C_0}<30,
$$

and therefore

$$
K_0(99/100)<180000^2
=32{,}400{,}000{,}000<2^{35}.
\tag{12}
$$

Thus $\mathcal R_C$ lies below $K<2^{35}$.

### Zone T: thin side

Put $\varepsilon=1-\rho$.  For

$$
\frac{99}{100}\le\rho\le1-2^{-18},
\qquad
2^{-18}\le\varepsilon\le\frac1{100},
$$

the combined thin estimates cover (5) and (6).  The only possible residual
is

$$
\boxed{
\mathcal R_T=
\left\{(\varepsilon,K):
2^{-18}\le\varepsilon\le\frac1{100},\quad
\frac1{8\varepsilon^{5/2}}
\le K\le
\frac{64}{\varepsilon^2}
\right\}.
}
\tag{13}
$$

At $\varepsilon=2^{-18}$ the two frequency bounds agree:

$$
L(2^{-18})=U(2^{-18})=2^{42}.
\tag{14}
$$

Moreover

$$
U(\varepsilon)\le U(2^{-18})=2^{42}.
\tag{15}
$$

The endpoint $\varepsilon=2^{-18}$ itself is already completely analytic.

## Uniform high-energy output

Equations (9), (12), and (15) must yield the explicit global statement

$$
\boxed{
\rho\in I_*,\quad K\ge K_{\mathrm{hi}}:=2^{42}
\quad\Longrightarrow\quad (1).
}
\tag{16}
$$

Define the bounded closed planning envelope

$$
\boxed{
\mathcal E:=\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T.
}
\tag{17}
$$

This is sharper than the full rectangle $I_*\times[0,2^{42}]$, but it is
still an over-cover.  Let $\mathcal A$ be the union of all regions covered
by the permitted analytic inputs and define the actual certification target

$$
\boxed{
\mathcal D=
\bigl(I_*\times[0,\infty)\bigr)\setminus\mathcal A.
}
\tag{18}
$$

Then $\mathcal D\subseteq\mathcal E$.  The difference
$\mathcal E\setminus\mathcal D$ contains, among other points, the already
analytic endpoint and frequency-threshold faces.  Those faces are masks or
boundary owners in a cover manifest; they do not require numerical
certification.

The overlaps at $\rho=1/16$ and $\rho=99/100$ are inclusive.  A point on a
switch face may be assigned to either a neighboring certificate family or
to an analytic theorem.  Every face must have one explicit owner.

## Certificate specification required next

For every closed parameter box used to cover (18), a valid certificate must:

1. enforce the strict angular cutoff $\ell+1/2<K$;
2. isolate or exclude every zero of the exact shell determinant, or use an
   equivalent rigorously monotone Prüfer phase;
3. handle determinant, phase-integer, ordinary-floor, angular, and
   Weyl-margin walls by either exact subdivision or a proved one-sided
   monotone majorant that absorbs every wall in the box;
4. use outward-rounded interval or ball arithmetic;
5. prove the strict count convention at eigenvalue faces;
6. give shared or overlapping certified boundary faces between neighboring
   boxes;
7. emit enough exact input and interval output for an independent checker to
   recompute the count and Weyl margin.

In particular, for a closed box

$$
B=[\rho_-,\rho_+]\times[K_-,K_+],
$$

one permitted wall-safe mechanism is the monotone corner estimate

$$
N_D(A_{\rho,1},K^2)
\le
\#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}
=:C_B,
\tag{19}
$$

together with

$$
\frac{2}{9\pi}(1-\rho^3)K^3
\ge
\frac{2}{9\pi}(1-\rho_+^3)K_-^3
=:W_B.
\tag{20}
$$

The non-strict corner count in (19) safely absorbs a possible eigenvalue on
$K=K_+$.  A certified inequality $C_B\le W_B$ proves the complete box
without splitting its internal walls.

For fixed $\rho$, it is enough to verify the inequality immediately to the
right of each spectral jump.  For a two-parameter box, that reduction may
only be used after the movement of every eigenvalue wall and of the Weyl
right-hand side has been enclosed throughout the box, or after a monotone
corner estimate such as (19)--(20) has replaced the moving-wall problem.

The certificate family must include a machine-checkable exact cover
manifest.  Each entry records exact box endpoints and inclusivity, its
parent zone, analytic masks, face owners, arithmetic backend and version,
precision, angular and radial truncation proofs, certified count upper
bound, certified Weyl lower bound, and hashes of all raw artifacts.  The
independent checker must prove

$$
\mathcal E\setminus
\bigl(\mathcal A\cup\text{certified boxes}\bigr)=\varnothing
\tag{21}
$$

using exact endpoints, not a sampled grid.

## Falsification cases

- $\rho=\rho_*$ and $\rho=1-2^{-18}$;
- $\rho=1/16$, $\rho=1/2$, and $\rho=99/100$;
- $K=1/(2\rho)$ and $K=H_0(\rho)$;
- $(1-\rho)K=\pi$;
- $K=K_0(\rho)$;
- $K=L(\varepsilon)$ and $K=U(\varepsilon)$;
- $\varepsilon=2^{-18}$, where the thin residual collapses;
- a half-integer angular wall $K=\ell+1/2$;
- a determinant zero or phase integer on a box face;
- an ordinary-floor proxy wall on a box face;
- an uncovered sliver at either rational switch point;
- treating a floating-point pilot as certification of (18);
- demanding literal subdivision at every angular wall when a proved
  monotone count majorant is used instead;
- a cover manifest with an unowned face or an unproved truncation.

## Promotion rule

The analytic reduction (16)--(18) may be promoted as a separate lemma after
an independent reconstruction and adversarial wall audit.  Do not promote
`SHELL-rho-compact` itself until every point of (18) has either an explicit
analytic owner or a reproducible certificate, and an independent checker
has verified the exact global cover (21).  A deliberately
small pilot box is progress on `COMP-certified-bessel`, but remains
`diagnostic_only` until its interval proof and checker are complete.
