# Round 14 central--thin seam extension: adversarial referee report

## Verdict

**PASS.** I began from the presumption that the proposed Round 14 theorem
was false and independently reconstructed the candidate proof before
comparing the three proof artifacts. I found no unsupported implication.

The audited conclusions are:

\[
\boxed{
0<\varepsilon\le \frac18,
\qquad
K\ge \frac{32}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3,}
\tag{A1}
\]

including the equality faces \(\varepsilon=1/8\) and
\(K=32/\varepsilon^2\), and, independently,

\[
\boxed{K_0(7/8)<550^2.}
\tag{A2}
\]

These imply the stated six-zone all-ratio high-frequency consequence

\[
\boxed{0<\rho<1,\qquad K\ge550^2,}
\tag{A3}
\]

including \(K=550^2\). They do **not** enlarge the complete all-frequency
endpoint beyond \([99/100,1)\), close the compact residual below \(550^2\),
promote a Bessel-root certificate, or prove the final all-frequency target.

**First unsupported implication: none.**

## 1. Frozen identities and review order

I verified the frozen identities before relying on their contents:

| artifact | verified SHA-256 |
|---|---|
| frozen packet | `19a9f76d88e6aaac0cdc772c22690fcb03e0c9ff5ac7b0761294005e0a152860` |
| incumbent proof | `f22ea932e16487fed3e149e2cc2321d2f67339d9d5711486b8e60d9145498929` |
| isolated clean-room proof | `2ab27e1265af7b8712f5f573baa1d7fc77f2ccb635925619d7f53181f1184286` |
| independent constant inventory | `b7a5ab241289289cc2af8c51f5ca9816be10d5a153ea7018ce041ed5a8252395` |
| standalone exact ledger | `8a7dd3f43bb990878ac4d54bd739d853c0887f876e744625ac4d61a2db9fcfc1` |
| focused tests | `ed0168697d144f5599ab592a246438980d65f246b054657803e3a05b0a3ba479` |

The packet itself labels all Round 14 constants as candidates. I therefore
treated only its listed pre-Round-14 results as proved inputs. I first
reconstructed the definitions, signs, local-slope argument, loss cap,
payments, endpoint root comparison, and global face ownership. I then
audited each proof artifact separately and only afterward compared their
routes and constants.

## 2. Definitions and the dangerous-branch geometry

Put

\[
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4,
\qquad
0<y\le\frac1{2\sqrt2},
\qquad
\rho=1-y^2\ge\frac78,
\qquad
\kappa\ge32.
\tag{B1}
\]

For a low-interface tail, the packet supplies

\[
n=\lfloor\mu-x_0\rfloor,
\quad q=x_0+n,
\quad \beta=\mu-q\in[0,1),
\quad m=n-p,
\quad R=p-dm,
\tag{B2}
\]

where \(\mu=\rho K\) and

\[
d=1-\frac2\pi\arccos\rho.
\]

The exact angular reserve is

\[
\left(\frac78\right)^2-\frac34=\frac1{64}>0.
\]

Thus \(\rho\ge7/8>\cos(\pi/6)\), including at \(\rho=7/8\), and hence

\[
d>\frac23.
\tag{B3}
\]

In the only dangerous branch \(R>0\), necessarily \(p>0\). With

\[
P=py,
\qquad r=Ry,
\qquad S=(p+m)y,
\]

one has exactly

\[
P-r=dmy,
\qquad
S=P+\frac{P-r}{d},
\qquad
0<r\le P,
\qquad
S<\frac52P.
\tag{B4}
\]

No argument assumes a positive lower bound for \(R\), so the first branch
with \(R>0\) is included.

## 3. Shelf displacement and localization

Define

\[
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1).
\tag{C1}
\]

Because \(S=ny\), these definitions give the useful exact identity

\[
\widehat q=\frac{n+1}{\mu}.
\tag{C2}
\]

The strict shelf estimate and (B4) yield

\[
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac52y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{C3}
\]

Both proxy terms attain their closed upper endpoint when
\(y^2=1/8\), \(\rho=7/8\), and \(\kappa=32\). Exact rational bounds give

\[
\sqrt{\frac\pi{112}}<\frac{67}{400},
\qquad
\left(\frac{67}{400}\right)^2-
\frac{1571/500}{112}=\frac3{1120000}>0,
\]

and therefore

\[
\widehat q
<\frac1{1792}+\frac52\frac{67}{400}
=\frac{3757}{8960}
<\frac{17}{40},
\tag{C4}
\]

with reserve \(51/8960\). In particular
\(1-\widehat q>23/40>0\).

Since \(U=\mu-x_0=n+\beta<n+1\), including when \(\beta=0\),

\[
\frac{x_0}{K}
>\rho(1-\widehat q)
>\frac78\frac{23}{40}
=\frac{161}{320}
=\frac12+\frac1{320}.
\tag{C5}
\]

Thus the dangerous tail is localized beyond \(K/2\) before any
outer-region slope is invoked. The clean-room route independently obtains
the same localization using

\[
\widehat q<\frac{47}{112}+\frac1{1792}
=\frac{753}{1792}<\frac{17}{40},
\]

whose exact reserve is \(43/8960\).

## 4. Strict ordinary-floor implication and self-consistency

For \(0<z<\mu\),

\[
\sigma(z)=-A'(z)
=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right)>0.
\tag{D1}
\]

Direct differentiation gives

\[
\sigma'(z)
=\frac1{\sqrt{\mu^2-z^2}}-
\frac1{\sqrt{K^2-z^2}}>0,
\]

so \(\sigma\) is increasing. In the dangerous branch, the plateau
definition gives equal ordinary floors at \(x_0\) and \(x_0+p\). Two
numbers with the same ordinary floor lie in the same half-open unit
interval, even when one is an integer. Since \(A\) is decreasing,

\[
0\le A(x_0)-A(x_0+p)<1.
\tag{D2}
\]

Writing \(t=x_0/\mu\), one obtains

\[
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{D3}
\]

Moreover

\[
1-\rho t=\varepsilon+\frac UK<y^2Q,
\qquad
1-\rho^2t^2<2y^2Q,
\qquad
t>1-\widehat q.
\tag{D4}
\]

Integrating the increasing slope across the plateau and using (D2)--(D4)
gives

\[
1>
\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
\]

Here \(P>0\), \(Q>1\), \(\pi>0\), and
\(1-\widehat q>23/40\), so every division is by a positive quantity and
squaring preserves direction. Thus

\[
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.}
\tag{D5}
\]

The constant inventory supplies an independent derivation. It uses
\(\rho(1-\widehat q)=1-y^2Q\), the strict slope comparison obtained from
the two arccosines, and

\[
1-\rho^2(1-\widehat q)^2
=2y^2Q-y^4Q^2<2y^2Q.
\]

The clean-room proof instead controls the arccos difference uniformly at
every point of \([x_0,x_0+p]\). All three derivations establish the same
strict inequality without crossing a denominator or squaring wall.

## 5. Actual-to-synthetic comparison and the full path

Let \(B=14/3\). The incumbent holds the exact parameter \(d\) fixed,
observes that the right side of (D5) decreases with \(r\), and, under the
contradictory assumption \(r\ge B\), compares it with the full path
\((P',B)\), \(B\le P'\le P\). Every path point preserves the original
shelf ceiling because \(P'\le P\), and it satisfies
\(\widehat q<17/40\).

Along this path,

\[
\frac{\partial Q}{\partial P'}
=\frac y\kappa\left(1+\frac1d\right)
<\frac{99}{3584}.
\]

Consequently the derivative of
\(2\pi^2Q/(1-\widehat q)^2\) is bounded by

\[
\frac{117036972261}{23847320000}<5,
\]

with exact reserve

\[
5-
\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0.
\]

Therefore

\[
\frac d{dP'}\left(
P'^2-\frac{2\pi^2Q}{(1-\widehat q)^2}
\right)
>2B-5=\frac{13}{3}>0.
\tag{E1}
\]

At the path's initial point \(P'=r=B\), one has \(S=B\) exactly,
including the no-drop geometry. The endpoint reserve is

\[
B^2-
2\left(\frac{1571}{500}\right)^2
\frac{1351/1280}{(1-71/8960)^2}
=\frac{49714811804}{82306584375}>0.
\tag{E2}
\]

Equations (E1)--(E2) contradict (D5) if \(r\ge B\), proving

\[
\boxed{r<\frac{14}{3},
\qquad
R<\frac{14}{3\sqrt\varepsilon}.}
\tag{E3}
\]

The constant inventory makes the actual-to-synthetic comparison explicit
through

\[
S_*(P,r)=\frac{5P-3r}{2}\ge S,
\]

and verifies that the quotient in (D5) is increasing in \(Q\) while its
synthetic version is decreasing in \(r\). This confirms every inequality
direction used by the incumbent.

The clean-room proof is materially distinct. It first derives \(P<9\)
from a separate quadratic comparison. Under \(r\ge B\), it then uses

\[
S\le\overline S(P)=\frac52P-7
\]

and studies the polynomial-form quantity

\[
\overline H(P)
=P^2(1-\overline q(P))^2-2\pi^2\overline Q(P).
\]

Its initial reserve and uniform path derivative are, respectively,

\[
\overline H(B)>
\frac{3627793}{7225344}>0,
\qquad
\overline H'(P)>
\frac{1178207}{150528}>0.
\]

This gives the same contradiction to (D5) by a different path,
different elementary bounds, and a different differentiated function.

## 6. Action payment and every plateau branch

The exact action identity and
\(\arccos(1-v)\ge\sqrt{2v}\) give

\[
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{F1}
\]

With \(K=\kappa/y^4\), \(\kappa\ge32\),
\(\sqrt2>140/99\), and \(\pi<1571/500\),

\[
K\eta>
\frac{4480000}{466587}\frac1y.
\tag{F2}
\]

The universally strict inequality \(\lfloor x\rfloor>x-1\), including
at integer \(x\), pays the complete possible floor loss.

If \(R>0\), combine (E3), (F2), and
\(1/y\ge2\sqrt2>280/99\) to obtain

\[
M>
\frac{598534207}{46192113}.
\]

Because \(4\delta<8\sqrt2/15<132/175\),

\[
M-4\delta>
\frac{98646127309}{8083619775}>0.
\tag{F3}
\]

If \(R\le0\), no localization is needed and

\[
M-4\delta>
\frac{205339021309}{8083619775}>0.
\tag{F4}
\]

The branch ownership is exhaustive:

- \(p=n>0\) gives \(m=0\), \(R=p>0\), and is covered by the complete
  dangerous path, including its no-drop endpoint;
- \(p=0<n\) gives \(R=-dn<0\) and is safe;
- \(n=0\) gives \(p=m=R=0\) and is safe;
- \(R=0\) belongs to the safe branch and is not inferred by continuity;
- the first branch with \(R>0\) is covered without a lower bound on \(R\).

Thus \(M>4\delta\) in every branch, so the supplied low-interface
decomposition gives the strict shifted-tail comparison. The promoted
high-angular shifted-tail theorem owns \(x_0\ge\mu\), and the promoted
weighted scaffold converts all shifted-tail estimates to the Weyl
integral. Directly,

\[
2\int_0^K z\,[G_K(z)-G_\mu(z)]\,dz
=\frac{2}{9\pi}(K^3-\mu^3),
\]

which closes (A1).

## 7. Integer, interface, spectral, and threshold walls

Every required wall has an owner:

1. If \(\mu-x_0\in\mathbb Z\), then \(\beta=0\), \(q=\mu\), and
   \(\delta=0\). On either adjacent cell, \(0\le\beta<1\) still gives
   \(U<n+1\). No estimate assumes \(n\) remains fixed across the wall.
2. At an ordinary-floor wall, equality of the two ordinary floors still
   implies the strict unit difference (D2). A change in \(p\) only changes
   which already-audited branch is selected.
3. At \(K\eta\in\mathbb Z\),
   \(\lfloor K\eta\rfloor>K\eta-1\) remains strict.
4. At \(x_0=\mu\), the promoted high-angular shifted-tail theorem includes
   equality. The low-side \(n=0\) case is independently safe.
5. At \(q=\mu\), \(\delta=0\), so no limiting positive error is inserted.
6. At the angular cutoff \(\nu=K\), the promoted phase/scaffold package
   has no active mode beyond the cutoff and remains valid at equality.
7. The strict spectral count uses a strict phase bracket. If the phase is
   exactly an integer multiple of \(\pi\), the endpoint mode is excluded;
   the ordinary floor is only an upper bound. No strict bracket is replaced
   by an ordinary non-strict count.
8. All radicands and denominators used above are positive on the closed
   candidate domain. The sole nontrivial squaring is performed only after
   positivity of \(P,Q,1-\widehat q\), and the other factors is established.
9. Every worst-case reduction is monotone in the asserted direction:
   \(y^4/(1-y^2)\), \(y/\sqrt{1-y^2}\), and
   \(y^2/(1-y^2)\) increase with \(y\), while the relevant proxies decrease
   with \(\kappa\). Hence the exact endpoint reductions really occur at
   \(y^2=1/8\) and \(\kappa=32\).
10. No proof step assumes \(\kappa>32\). Therefore
    \(K=32/\varepsilon^2\), including
    \((\varepsilon,K)=(1/8,2048)\), is covered directly.

The retained theorem faces are not overwritten. Round 10 owns
\(\varepsilon\le1/25\) at the sharper \(\kappa=20\) threshold; the
constant-24 results own their accepted domains; Round 13 owns
\(\varepsilon=1/10\) at \(K=2400\); and the new theorem owns
\(\varepsilon=1/8\) at \(K=2048\).

## 8. The \(\kappa=24\) route obstruction is not a counterexample

The same coarse localization architecture at \(\kappa=24\) gives only

\[
\frac{x_0}{K}>\frac{173}{384}<\frac12.
\]

This says only that the present proof route cannot enter the outer-slope
region with that constant. It provides no shell eigenvalue, no reversed
counting inequality, and no counterexample to a possible
constant-24 theorem. Neither the proofs nor this review treat it as a
disproof.

## 9. Independent central endpoint and unique-root logic

At \(\rho=7/8\), (F1) gives

\[
\eta_{7/8}\ge\frac1{24\pi}>\frac1{76}.
\]

Exact comparisons also give

\[
a_{7/8}=14\pi<44<49,
\qquad
\sqrt{a_{7/8}}<7,
\qquad
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
\tag{G1}
\]

For

\[
f(X)=\eta_{7/8}X^2-\sqrt{a_{7/8}}X-C_0,
\]

the leading coefficient is positive and the constant term is negative.
Thus its two real roots have opposite signs and the positive root is
unique. That root is exactly \(\sqrt{K_0(7/8)}\). At \(Y=550\),

\[
f(Y)>
\frac1{76}Y^2-7Y-\frac{307}{175}
=\frac{427292}{3325}>0.
\tag{G2}
\]

Since \(f(0)<0\), the unique positive root lies strictly between \(0\)
and \(550\). Squaring positive numbers preserves direction, proving (A2).
The fixed-ratio theorem owns \(K=K_0(7/8)\) itself, and
\(K=550^2\) lies strictly above that moving threshold.

## 10. Six-zone union and every moving face

Only after (A1) and (A2) are established may the global inputs be assembled.
The exact possible residual is enclosed by the following six finite zones:

| zone | closed ratio interval | possible residual only below |
|---:|---|---:|
| 1 | \([\rho_*,1/16]\) | \(64\) |
| 2 | \([1/16,7/8]\) | \(K_0(\rho)\le K_0(7/8)<550^2\) |
| 3 | \([7/8,9/10]\) | \(32/(1-\rho)^2\le3200\) |
| 4 | \([9/10,19/20]\) | \(24/(1-\rho)^2\le9600\) |
| 5 | \([19/20,24/25]\) | \(24/(1-\rho)^2\le15000\) |
| 6 | \([24/25,99/100]\) | \(20/(1-\rho)^2\le200000\) |

The fixed-ratio theorem uses \(K\ge K_0(\rho)\), so every moving face
\(K=K_0(\rho)\) is analytically owned and is not part of the residual.
The permitted monotonicity of \(K_0\) follows independently from its
positive-root equation: \(a_\rho\) increases, \(\eta_\rho\) is
nonincreasing, the positive root increases with \(a\), and it decreases
with \(\eta\). Hence the zone-2 endpoint reduction is in the correct
direction.

The shared faces have no sliver:

- \(\rho=\rho_*\) is owned by the complete small-hole theorem;
- both central analytic regimes meet at \(\rho=1/16\);
- \(\rho=7/8\) is owned by (A1), including \(K=2048\);
- \(\rho=9/10\) is owned by Round 13 at the sharper \(K=2400\);
- \(\rho=19/20\) is owned at \(K=9600\);
- \(\rho=24/25\) is owned by Round 10 at the sharper \(K=12500\);
- \(\rho=99/100\) is owned at every frequency by the complete endpoint.

The energy comparisons are exact:

\[
64<3200<9600<15000<200000<550^2=302500.
\]

Thus \(K=550^2\) is included for every \(0<\rho<1\), proving (A3).
The exact reduction from the Round 13 ceiling is

\[
\frac{900^2}{550^2}=\frac{324}{121}
=2+\frac{82}{121}>2.
\]

## 11. Isolation and route distinctness

The clean-room artifact identifies the correct frozen packet hash and
contains an explicit declaration that it inspected no Round 14 response,
exploration, computation, ledger, test, review, judge artifact, diff, agent
message, or incumbent output before its verdict. Its mathematics is also
artifact-level evidence of genuine independence:

- it proves \(\pi<22/7\) with a positive integral rather than the
  incumbent's Machin bound \(\pi<1571/500\);
- it obtains the displacement reserve \(43/8960\), not \(51/8960\);
- it derives the preliminary cutoff \(P<9\), which the incumbent does not
  use;
- it differentiates a polynomial-form affine majorant and obtains reserves
  \(3627793/7225344\) and \(1178207/150528\), rather than the incumbent's
  quotient derivative and endpoint reserves;
- it uses the coarser but independent payment reserves
  \(3229/275\) and \(20467/825\).

The independent inventory likewise records the packet as its only
Round 14 input and supplies an explicit actual-to-synthetic majorant that
checks the incumbent's inequality directions. The three artifacts agree
on the theorem and wall ownership but are not copies of one proof route.
The artifact-level isolation and distinctness gate therefore passes.

## 12. Promotion boundary and current state check

The current graph was checked before any Round 14 promotion. Its statuses
remain:

| obligation | current status |
|---|---|
| `SHELL-central-thin-seam-compression` | `proved_internal` at the accepted Round 13 boundary |
| `SHELL-rho-compact-analytic-envelope` | `proved_internal` at the accepted Round 13 boundary |
| `SHELL-rho-compact` | `open` |
| `COMP-certified-bessel` | `diagnostic_only` |
| `SHELL-rho-uniformity` | `open` |
| `TARGET-shell-d3` | `open` |

This report supports promotion of only the new seam statement, the
independent endpoint comparison, and the resulting analytic envelope and
high-frequency ceiling after the judge gate. It supplies no certified
Bessel-root coverage and no justification to promote the compact,
uniformity, or final-target obligations.

The complete all-frequency thin endpoint remains exactly

\[
\boxed{99/100\le\rho<1,\qquad K\ge0.}
\]

The exact compact residual below \(550^2\) remains open.

## 13. Executed checks

The following checks were executed against the frozen artifacts:

- embedded incumbent exact ledger: **PASS**;
- standalone Round 14 exact ledger: **PASS**;
- focused Round 14 tests: **6 passed**;
- complete computation suite: **51 passed**;
- state graph validator: **PASS**;
- independent graph audit: **49 obligation IDs**, all dependency,
  permitted-dependency, blocker, and implication references resolve; the
  dependency graph is acyclic;
- artifact-path audit: **530 references exist**, with none missing;
- protected Round 8 checker: **PASS**, including provenance verification
  and frozen packet hash
  `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.

The exact ledger is a symbolic rational consistency check, not a
Bessel-root certificate. The protected Round 8 result remains confined to
its single certified box.

## Final assessment

**PASS.** The local seam theorem (A1), the independent endpoint (A2), and
the six-zone consequence (A3) survive reconstruction of every inequality
direction, monotonic reduction, denominator, squaring, action payment,
exceptional branch, integer/interface/spectral wall, moving
\(K_0(\rho)\) face, and threshold-equality face. The clean-room route is
isolated by declaration and materially distinct in construction. The
\(\kappa=24\) localization is correctly classified as a route obstruction
only. The endpoint remains exactly \([99/100,1)\), the compact residual
remains open, and no certification or final target is promoted.

**First unsupported implication: none.**
