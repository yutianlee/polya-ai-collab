# Round 15 central--thin seam extension: adversarial referee report

## Verdict

**PASS.** I began from the assumption that the proposed Round 15 theorem
was false. I reconstructed the incumbent, clean-room, and constant-inventory
arguments separately before comparing them, and found no unsupported
implication.

The audited conclusions are

\[
\boxed{
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3,}
\tag{A1}
\]

including \(\varepsilon=1/6\) and
\(K=54/\varepsilon^2\), and, independently,

\[
\boxed{K_0(5/6)<295^2=87025.}
\tag{A2}
\]

Together with the accepted inputs, these imply the seven-zone consequence

\[
\boxed{0<\rho<1,\qquad K\ge200000,}
\tag{A3}
\]

including \(K=200000\). They do **not** prove the full all-frequency shell
theorem, enlarge the complete endpoint beyond \([99/100,1)\), turn the exact
residual into a rectangle, or promote a Bessel-root certificate.

**First unsupported implication: none.**

## 1. Frozen identities and audit order

The six supplied hashes match byte for byte:

| artifact | verified SHA-256 |
|---|---|
| frozen packet | `c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7` |
| incumbent proof | `3d9c78583f14cfa59a989b248e376d78fc2f4b580ac5f6a2c3825885faff658f` |
| isolated clean-room proof | `824670a5a5183d30f58d663bf672b9069042e61c53157b2ea153db90f9cab2c7` |
| independent constant inventory | `959a120a1c9e0b7107eefd152f28d96948d67c3bc91de297fe4f8d31a4a3e5e1` |
| standalone exact verifier | `14d03a2f7d935962af72a0abc159e2f7036a6dccd9539eb7d023c7b1abb63ca7` |
| focused tests | `21032410d48161e3fdda06cdc9fafdd27d74b4d5e6eed9e28bc0dc961bb7bf3a` |

The packet labels every Round 15 screen as unproved. I therefore treated
only its accepted pre-Round-15 inputs as lemmas. I first audited the local
claim directly, then the fixed-ratio endpoint, then the prospective union.
Only after those reconstructions did I compare the incumbent with the
clean-room and inventory routes.

## 2. Scaling, angular factor, and dangerous geometry

Put

\[
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4,
\qquad
0<y\le\frac1{\sqrt6},
\qquad
\rho=1-y^2\ge\frac56,
\qquad
\kappa\ge54.
\tag{B1}
\]

The elementary angular comparisons are in the correct direction:

\[
2-\left(\frac75\right)^2=\frac1{25}>0,
\qquad
\left(\frac79\right)^2-\frac35=\frac2{405}>0.
\]

They give
\(\sqrt{2-\sqrt2}<7/9\), hence

\[
\cos\frac{3\pi}{8}<\frac7{18},
\qquad
\cos^2\frac{3\pi}{16}<\frac{25}{36},
\qquad
\cos\frac{3\pi}{16}<\frac56\le\rho.
\]

Since arccos is decreasing,

\[
c=\frac{\arccos\rho}{\pi}<\frac3{16},
\qquad
\boxed{d=1-2c>\frac58.}
\tag{B2}
\]

The comparison is strict even at \(\rho=5/6\).

For the low-interface decomposition, let

\[
n=\lfloor\mu-x_0\rfloor,
\quad
q=x_0+n,
\quad
\beta=\mu-q\in[0,1),
\quad
m=n-p,
\quad
R=p-dm.
\tag{B3}
\]

In the only dangerous branch \(R>0\), one has \(p>0\). With

\[
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y,
\]

the exact map is

\[
P-r=dmy,
\qquad
S=P+\frac{P-r}{d},
\qquad
0<r\le P.
\tag{B4}
\]

Consequently

\[
S\le P+\frac85(P-r)
=S_*(P,r)=\frac{13P-8r}{5}
<\frac{13}{5}P.
\tag{B5}
\]

The last inequality uses \(r>0\). The preceding weak inequality retains
the no-drop geometry \(m=0\), where \(P=r=S\). Thus neither the no-drop
branch nor the first positive-\(R\) cell is lost in the synthetic map.

The shelf factor is also reconstructed rather than assumed. From the
strict Machin bound \(\pi<1571/500\),

\[
\left(\frac{13}{5}\right)^2-2\frac{1571}{500}
=\frac{119}{250}>0,
\]

so the supplied shelf estimate implies

\[
p<\frac{13}{5}\sqrt{\frac K\varepsilon},
\qquad
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
\tag{B6}
\]

## 3. Actual displacement and pre-slope localization

Define the actual quantities

\[
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho},
\qquad
\widehat q=a(Q-1).
\tag{C1}
\]

Because \(S=ny\) and \(\mu=\rho\kappa/y^4\), there is an exact identity

\[
\widehat q
=\frac{y^4+y^3S}{\rho\kappa}
=\frac{n+1}{\mu}.
\tag{C2}
\]

Writing \(t=x_0/\mu\), the strict cell relation
\(\mu-x_0=n+\beta<n+1\) gives

\[
1-t<\widehat q.
\tag{C3}
\]

This remains strict when \(\beta=0\) and uniformly as
\(\beta\to1^-\).

Equations (B5)--(B6) yield

\[
\widehat q
<\frac{y^4}{\rho\kappa}
+\frac{13}{5}y\sqrt{\frac{2\pi}{\rho\kappa}}.
\tag{C4}
\]

Both terms increase with \(y\) and decrease with \(\kappa\): the relevant
positive functions are \(y^4/(1-y^2)\) and
\(y/\sqrt{1-y^2}\). The closed proxy maximum is therefore at
\(y^2=1/6\), \(\rho=5/6\), and \(\kappa=54\). At that point

\[
\frac{y^4}{\rho\kappa}=\frac1{1620},
\qquad
y\sqrt{\frac{2\pi}{\rho\kappa}}=\sqrt{\frac\pi{135}}.
\]

Positive squaring and \(\pi<1571/500\) give

\[
\sqrt{\frac\pi{135}}<\frac{763}{5000},
\qquad
\left(\frac{763}{5000}\right)^2-
\frac{1571}{67500}
=\frac{8563}{675000000}>0.
\]

Thus

\[
\widehat q
<\frac1{1620}+\frac{13}{5}\frac{763}{5000}
=\frac{804689}{2025000}
<\frac{159}{400},
\tag{C5}
\]

with exact reserve

\[
\frac{159}{400}-\frac{804689}{2025000}
=\frac{497}{4050000}>0.
\]

Before any outer-region slope is used, (C3)--(C5) imply

\[
\boxed{
\frac{x_0}{K}=\rho t
>\frac56\left(1-\frac{159}{400}\right)
=\frac{241}{480}
=\frac12+\frac1{480}.}
\tag{C6}
\]

This is a strict localization on the complete dangerous domain, including
the endpoint \((\varepsilon,\kappa)=(1/6,54)\).

## 4. Ordinary floors and actual self-consistency

For \(0<z<\mu\), differentiation of the action gives

\[
\sigma(z)=-A'(z)
=\frac1\pi\left(
\arccos\frac zK-\arccos\frac z\mu
\right)>0,
\]

and

\[
\sigma'(z)
=\frac1\pi\left(
\frac1{\sqrt{\mu^2-z^2}}-
\frac1{\sqrt{K^2-z^2}}
\right)>0.
\tag{D1}
\]

In the dangerous branch, the plateau definition gives equal ordinary
floors at \(x_0\) and \(x_0+p\). Two numbers in the same half-open unit
cell differ by strictly less than one, even if one lies on an integer
wall. Since \(A\) decreases,

\[
A(x_0)-A(x_0+p)<1.
\tag{D2}
\]

At \(x_0=\mu t\),

\[
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{D3}
\]

Moreover,

\[
1-\rho t
=\varepsilon+\frac{\mu-x_0}{K}
<y^2Q,
\qquad
1-\rho^2t^2<2y^2Q.
\tag{D4}
\]

All radicands here are positive because \(0<\rho t=x_0/K<1\).
Integrating the increasing \(\sigma\) over the plateau and using
\(t>1-\widehat q>0\) gives

\[
1>
\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
\]

Every factor divided by or squared is positive. Hence the strict actual
self-consistency inequality is

\[
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.}
\tag{D5}
\]

The clean-room proof independently reaches (D5) through the cosine
difference

\[
\cos\gamma-\cos\alpha
< (\alpha-\gamma)\sin\alpha,
\]

with \(\alpha=\arccos(x_0/K)\) and
\(\gamma=\arccos(x_0/\mu)\). That route also checks positivity before
squaring and confirms that (D5) is not an artifact of the incumbent's
integral lower bound.

## 5. Actual-to-synthetic comparison and the complete path

Define

\[
Q_*=1+\frac{y^2}{\kappa}+\frac{yS_*}{\kappa},
\qquad
q_*=a(Q_*-1),
\qquad
H(P,r)=\frac{2\pi^2Q_*}{(1-q_*)^2}.
\tag{E1}
\]

The actual-to-synthetic direction is correct. Equation (B5) gives
\(Q\le Q_*\) and \(\widehat q\le q_*\), while the same shelf calculation
as in Section 3 gives \(q_*<159/400\) at every relevant point. For fixed
\(a\ge0\),

\[
\frac{d}{dQ}
\frac{2\pi^2Q}{[1-a(Q-1)]^2}
=2\pi^2
\frac{1+a(Q-1)+2a}{[1-a(Q-1)]^3}>0.
\tag{E2}
\]

Therefore (D5) implies

\[
\boxed{P^2<H(P,r).}
\tag{E3}
\]

Set \(B=14/3\) and suppose, for contradiction, that \(r\ge B\). Since
\(Q_*\) decreases with \(r\), (E2) gives

\[
H(P,r)\le H(P,B).
\tag{E4}
\]

The entire path \((P',B)\), \(B\le P'\le P\), is admissible. The
original shelf bound for \(P\) bounds every \(P'\le P\), and

\[
0<S_*(P',B)<\frac{13}{5}P'
\]

keeps \(q_*<159/400\) and all denominators positive at every intermediate
point. This is a path argument, not an endpoint sample.

The strict rational endpoint bound

\[
y<\frac{49}{120},
\qquad
\left(\frac{49}{120}\right)^2-\frac16
=\frac1{14400}>0
\]

and \(\kappa\ge54\) give

\[
a\le\frac15,
\qquad
\frac{\partial Q_*}{\partial P'}
=\frac{13y}{5\kappa}<\frac{637}{32400}.
\]

Consequently, uniformly on the complete path,

\[
\frac{\partial H}{\partial P'}
<
2\left(\frac{1571}{500}\right)^2
\frac{637}{32400}
\frac{1+159/400+2/5}{(1-159/400)^3}
=\frac{2260740364246}{708624500625}
<\frac{16}{5},
\tag{E5}
\]

with reserve

\[
\frac{16}{5}-
\frac{2260740364246}{708624500625}
=\frac{6858037754}{708624500625}>0.
\]

Thus

\[
\frac d{dP'}\bigl(P'^2-H(P',B)\bigr)
>2B-\frac{16}{5}=\frac{92}{15}>0.
\tag{E6}
\]

At the initial point \(P'=r=B\), one has \(S_*=B\), including the
no-drop endpoint. The strict proxies

\[
Q_*(B,B)<\frac{10093}{9720},
\qquad
q_*(B,B)<\frac{373}{48600}
\]

give

\[
B^2-H(B,B)>
\frac{2505132463469}{2616573970125}>0.
\tag{E7}
\]

Equations (E4), (E6), and (E7) contradict (E3). Hence

\[
\boxed{r<\frac{14}{3},
\qquad
R<\frac{14}{3\sqrt\varepsilon}.}
\tag{E8}
\]

No denominator, radicand, squaring sign, or intermediate path point is
missing from this contradiction.

## 6. Action gain, complete floor payment, and branches

The supplied action identity and
\(\arccos(1-v)\ge\sqrt{2v}\) yield

\[
\eta\ge\frac{2\sqrt2}{3\pi}y^3,
\qquad
K\eta\ge\frac{2\sqrt2\kappa}{3\pi y}.
\tag{F1}
\]

Using \(\kappa\ge54\), \(\sqrt2>140/99\), and
\(\pi<1571/500\),

\[
K\eta>
\frac{280000}{17281}\frac1y.
\tag{F2}
\]

The gain remaining after the complete plateau-loss cap is

\[
\frac{280000}{17281}-\frac{14}{3}
=\frac{598066}{51843}>0.
\tag{F3}
\]

Positive squaring also gives

\[
\frac1y>\frac{120}{49},
\qquad
6-\left(\frac{120}{49}\right)^2
=\frac6{2401}>0.
\tag{F4}
\]

If \(R>0\), the universally strict inequality
\(\lfloor x\rfloor>x-1\), including integer \(x\), and (E8) give

\[
M=\lfloor K\eta\rfloor-R
>
\left(\frac{280000}{17281}-\frac{14}{3}\right)\frac1y-1.
\]

Since

\[
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
\]

the full dangerous-branch reserve is

\[
\boxed{
M-4\delta>
\left(\frac{598066}{51843}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{80132733}{3024175}>0.}
\tag{F5}
\]

If \(R\le0\), including \(R=0\), then
\(M\ge\lfloor K\eta\rfloor\), and the larger reserve is

\[
\boxed{
M-4\delta>
\frac{280000}{17281}\frac{120}{49}
-1-\frac{132}{175}
=\frac{114694733}{3024175}>0.}
\tag{F6}
\]

The branch split is exhaustive:

- \(p=n>0\) gives \(m=0\), \(R=p>0\), and is included at the
  \(P=r\) endpoint of the complete dangerous path.
- \(p=0<n\) gives \(R=-dn<0\), so the immediate-drop branch is safe.
- \(n=0\) has \(p=m=R=0\), so the degenerate head is safe.
- \(R=0\) is assigned directly to (F6), not obtained by continuity.
- The first discrete cell with \(R>0\) uses no positive lower bound on
  \(R\).

Thus \(M>4\delta\) in every plateau branch. Substitution in the permitted
decomposition yields the strict low-interface shifted-tail comparison.
The accepted high-interface, high-angular, strict-floor transfer, exact
spectrum, and multiplicity scaffold then give (A1).

## 7. Discrete, interface, spectral, and threshold walls

Every required wall has an explicit owner.

1. At \(\mu-x_0\in\mathbb Z\), \(\beta=0\), \(q=\mu\), and
   \(\delta=0\). On the neighboring cell, only \(0\le\beta<1\) and
   \(n+\beta<n+1\) are used; no estimate freezes \(n\) across the jump.
2. At \(x_0=\mu\), the accepted high-interface theorem owns equality,
   while the low-side \(n=0\) branch is independently safe.
3. At every ordinary-floor wall, equal floors retain the strict unit-width
   implication. A change in \(p\) merely selects another covered branch.
4. At \(K\eta\in\mathbb Z\),
   \(\lfloor K\eta\rfloor>K\eta-1\) remains strict and the whole possible
   unit loss has already been paid.
5. The displacement reserve puts every denominator strictly above zero.
   The action radicands are positive, and all squarings occur between
   positive quantities.
6. The angular cutoff \(\nu=K\) and strict spectral walls are owned by the
   accepted phase and shifted-tail package. Equality of a phase with a
   spectral endpoint is never silently counted by an ordinary non-strict
   floor.
7. The monotone worst-case reductions genuinely occur at
   \(y^2=1/6\) and \(\kappa=54\). No proof step assumes
   \(\kappa>54\), so threshold equality is included.

The requested epsilon faces are also correctly partitioned. The complete
endpoint owns \(\varepsilon=1/100\); the accepted constant-20 theorem is
sharpest at \(1/25\); the accepted constant-24 theorem is sharpest at
\(1/20\) and \(1/10\); the accepted constant-32 theorem is sharpest at
\(1/8\); and (A1) owns \(1/6\) at \(\kappa=54\). Constants
\(20,24,32\) are not extrapolated beyond their accepted domains.

## 8. Independent fixed-ratio endpoint

This argument does not use (A1) or the plateau-loss cap. At \(\rho=5/6\),

\[
a_{5/6}=10\pi<\frac{220}{7}<36,
\qquad
36-\frac{220}{7}=\frac{32}{7}>0,
\]

and therefore

\[
\sqrt{a_{5/6}}<6.
\tag{G1}
\]

At \(\varepsilon=1/6\), (F1) becomes

\[
\eta_{5/6}\ge\frac1{9\pi\sqrt3}.
\]

The exact comparisons

\[
\sqrt3<\frac{97}{56},
\qquad
49-9\left(\frac{1571}{500}\right)
\left(\frac{97}{56}\right)
=\frac{517}{28000}>0
\]

give

\[
\eta_{5/6}>\frac1{49}.
\tag{G2}
\]

Likewise,

\[
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
\tag{G3}
\]

For

\[
f(X)=\eta_{5/6}X^2-\sqrt{a_{5/6}}X-C_0,
\]

one obtains

\[
f(295)>
\frac{295^2}{49}-6(295)-\frac{307}{175}
=\frac{5226}{1225}>0.
\tag{G4}
\]

The leading coefficient is positive and the constant term is negative, so
the two roots have opposite signs and the positive root is unique. That
root is exactly \(\sqrt{K_0(5/6)}\) from the accepted formula. Since
\(f(0)<0<f(295)\), it lies strictly below \(295\), proving (A2). The
fixed-ratio theorem includes its exact threshold \(K=K_0(5/6)\), and the
strict comparison places \(K=295^2\) in the proved range.

## 9. The two failed proxies are not counterexamples

The proposed \(\kappa=53\) obstruction is classified correctly. From the
strict lower bound \(\pi>333/106\),

\[
\frac{333}{14045}
-\left(\frac{3079}{20000}\right)^2
=\frac{10003031}{1123600000000}>0,
\]

so

\[
\sqrt{\frac{2\pi}{265}}>\frac{3079}{20000}.
\]

At the selected endpoint envelope,

\[
\frac1{1590}+\frac{13}{5}\frac{3079}{20000}
=\frac25+\frac{14293}{15900000}>\frac25.
\tag{H1}
\]

This shows only that this coarse displacement envelope cannot establish
the needed localization at \(\kappa=53\). It supplies neither a reversed
count nor a spectral counterexample.

Similarly,

\[
\frac{294^2}{49}-6(294)-\frac{307}{175}
=-\frac{307}{175}<0
\tag{H2}
\]

shows only that the selected one-sided proxies do not certify \(Y=294\).
It does not determine the true sign at \(294\) and does not prove
\(K_0(5/6)\ge294^2\).

## 10. Seven-zone union and exact face ownership

Only after (A1) and (A2) are established may the accepted analytic cover
be assembled. Its coarse residual enclosures are

| zone | closed ratio interval | possible residual only below |
|---:|---|---:|
| 1 | \([\rho_*,1/16]\) | \(64\) |
| 2 | \([1/16,5/6]\) | \(K_0(\rho)\le K_0(5/6)<87025\) |
| 3 | \([5/6,7/8]\) | \(54/(1-\rho)^2\le3456\) |
| 4 | \([7/8,9/10]\) | \(32/(1-\rho)^2\le3200\) |
| 5 | \([9/10,19/20]\) | \(24/(1-\rho)^2\le9600\) |
| 6 | \([19/20,24/25]\) | \(24/(1-\rho)^2\le15000\) |
| 7 | \([24/25,99/100]\) | \(20/(1-\rho)^2\le200000\) |

The nonmonotone adjacent coarse values \(3456,3200\) are intentional:
the accepted constant-32 theorem is sharper at and beyond \(\rho=7/8\).
The maximum of the seven ceilings is exactly \(200000\), so equality at
the proposed global ceiling is covered in every ratio zone.

The ratio and energy faces have no sliver:

- \(\rho=\rho_*\) is owned at every frequency by the complete small-hole
  theorem; the two accepted central regimes meet at \(\rho=1/16\), and
  the fixed-ratio bound owns \(K=64\).
- At \(\rho=5/6\), (A1) includes
  \(K=54\cdot6^2=1944\). The fixed-ratio theorem independently owns
  \(K=K_0(5/6)\), and (A2) owns \(K=295^2=87025\). The failed
  \(294^2\) proxy is not promoted; at this seam point, \(K=294^2\) is
  nevertheless far above the (A1) threshold.
- At \(\rho=7/8\), the accepted constant-32 theorem owns the sharper
  \(K=32\cdot8^2=2048\), and therefore also the coarser new-seam face
  \(K=3456\).
- At \(\rho=9/10\), the accepted constant-24 theorem owns the sharper
  \(K=24\cdot10^2=2400\), and hence the coarse \(K=3200\) face.
- At \(\rho=19/20\), the constant-24 theorem includes \(K=9600\).
- At \(\rho=24/25\), the constant-20 theorem owns the sharper
  \(K=12500\), and therefore the coarse \(K=15000\) face.
- At \(\rho=99/100\), the complete endpoint owns every frequency,
  including \(K=200000\).

At central ratios where \(K=294^2\) lies below the moving
\(K_0(\rho)\), that point remains in the exact residual; where it lies
above, the fixed-ratio theorem owns it. This is the correct
nonrectangular classification and makes no uniform \(294^2\) claim.

The resulting exact residual after promotion must be represented as

\[
\mathcal D_{15}
=(I_{15}\times[0,\infty))\setminus\mathcal A_{15},
\qquad
I_{15}=[\rho_*,99/100],
\tag{I1}
\]

where \(\mathcal A_{15}\) contains the full accepted analytic cover and
all owned moving and fixed faces. The seven coarse ceilings enclose
\(\mathcal D_{15}\); they do **not** identify it with
\(I_{15}\times[0,200000)\). Many points below \(200000\) are already
analytic, while any unresolved point must retain its exact piecewise face
data.

The high-frequency improvement is exact:

\[
\frac{550^2}{200000}=\frac{121}{80}
=1+\frac{41}{80}>1.
\tag{I2}
\]

The complete all-frequency endpoint remains exactly \([99/100,1)\).

## 11. Isolation and cross-comparison

The clean-room artifact declares the frozen packet to be its sole input
before verdict. Its mathematics provides artifact-level evidence of route
independence:

- it uses a different Machin truncation and obtains different exact
  rational margins for the \(\pi\) bracket;
- it writes \(Q-1=(n+1)\varepsilon/\kappa\) and
  \(\widehat q=(n+1)/(\rho K)\) explicitly;
- it derives the angular gap through a cosine-difference integral rather
  than the incumbent's lower bound for \(\sigma(x_0)\);
- it reconstructs the low-ratio \(K_0<64\) face independently;
- its embedded indented exact ledger is separate from the incumbent's
  fenced ledger.

The incumbent, clean-room, and inventory agree on the actual-to-synthetic
map, derivative direction, complete path, endpoint reserve, action
payments, branch ownership, and global faces. Their agreement occurs after
independent derivations and is not being used as a substitute for proof.

## 12. Promotion boundary and accepted graph

The accepted graph was inspected in its pre-Round-15 state. It currently
records:

| obligation | accepted status before any Round 15 patch |
|---|---|
| `SHELL-central-thin-seam-compression` | `proved_internal` at the Round 14 boundary \(\varepsilon\le1/8\), \(\kappa\ge32\) |
| `SHELL-rho-compact-analytic-envelope` | `proved_internal` with \(I_{14}\) and \(K\ge550^2\) |
| `SHELL-rho-compact` | `open` |
| `COMP-certified-bessel` | `diagnostic_only` |
| `SHELL-rho-uniformity` | `open` |
| `TARGET-shell-d3` | `open` |

This report supports promotion, after the judge gate, only of (A1), (A2),
the seven-zone analytic envelope, and the all-ratio high-frequency
consequence (A3). It supplies no reason to promote the compact,
uniformity, computation-parent, or final-target obligations. The exact
compact residual (I1) remains open.

## 13. Executed checks

The following checks were executed against the frozen artifacts:

- embedded incumbent exact ledger: **PASS**;
- embedded clean-room indented exact ledger: **PASS**;
- standalone Round 15 exact verifier: **PASS**;
- focused Round 15 tests: **7 passed**;
- complete computation suite: **58 passed**;
- Python compilation of the verifier and focused tests: **PASS**;
- state graph validator: **PASS**;
- independent graph audit: **49 obligation IDs**, all dependency,
  permitted-dependency, blocker, and implication references resolve, and
  the dependency graph is acyclic;
- artifact-path audit: **566 references** over **141 distinct paths**, all
  present;
- protected Round 8 checker: **PASS**, including all seven certificate
  checks, provenance verification, certificate SHA-256
  `f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00`,
  and frozen-packet SHA-256
  `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.

The Round 15 exact ledgers are symbolic rational consistency checks, not
Bessel-root certificates. The protected Round 8 result remains confined to
its one certified closed box.

## Final assessment

**PASS.** The proposed seam theorem, independent fixed-ratio endpoint, and
seven-zone consequence survive reconstruction of the actual-to-synthetic
map, every inequality direction, strict endpoint, complete path,
denominator, radicand, squaring wall, action payment, exceptional branch,
integer/interface/spectral wall, moving threshold, and shared face. The
\(\kappa=53\) and \(Y=294\) failures are route obstructions only. The
complete endpoint stays \([99/100,1)\), the exact nonrectangular compact
residual remains open, and no finite-window or final-theorem obligation is
promoted by this review.

**First unsupported implication: none.**
