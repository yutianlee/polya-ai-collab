# Round 13 central--thin seam: adversarial referee report

## Verdict

**PASS.**

I assumed the frozen Round 13 theorem was false and reconstructed the local
shifted-tail proof, both synthetic comparison routes, every exceptional
branch and strict wall, the fixed-ratio endpoint, and the closed global
union. I found no unsupported implication.

The conclusions supported by this review are

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3,
\tag{R1}
$$

including threshold equality,

$$
K_0(9/10)<900^2,
\tag{R2}
$$

and therefore

$$
0<\rho<1,\qquad K\ge900^2
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{R3}
$$

Statement (R3) is only an all-ratio high-frequency theorem. It neither
closes the compact residual below $900^2$ nor enlarges the complete
all-frequency endpoint beyond $99/100\le\rho<1$.

The first unsupported implication is: **none**.

## 1. Review boundary and frozen provenance

This review was performed from the corrected frozen packet, without using
the failed prior referee turn and without using any prospective State Patch.
I inspected the frozen packet, incumbent response, independent constant
inventory, strict clean-room reconstruction, standalone verifier and tests,
the permitted promoted packets, and the current proof graph.

The primary frozen hashes used for this verdict are:

| Artifact | SHA-256 |
| --- | --- |
| state/lemma_packets/SHELL-central-thin-seam-compression-round13.md | 5ABA49CBF7BDC6326DFBC04A4CA4A6BD15A1C9A8A35EC541AA1E30A27AB406CD |
| rounds/polya-main/round_013/responses/seam-extension-incumbent.md | 4F092A9825E16F1953E00023F702636BAB75577A4081636721C0D8197D89446C |
| rounds/polya-main/round_013/exploration/seam-extension-constant-inventory.md | E3125CC5F4567B01B6F514426DB3213FAADFDAEB478D2F8BA75E155C3B13377B |
| rounds/polya-main/round_013/reviews/seam-extension-clean-room.md | E50BC12FB51CB0A392FB088F0384E54FF6C7727639D527F59336B39847BE61CC |
| computations/round13_verify_seam_extension.py | FDE3928AC03065A1782078359CA376A217BB1F2A402D200E8130AB8DDD6B6E98 |
| computations/tests/test_round13_seam_extension.py | 294DB1A76E4E5A4F33766E1DB79E4A308982DB105956C262E61B3DAD50C44C02 |
| state/proof_obligations.yml | E21BE63F598DB7328D8AAC78FBBF620045F0732661749F485338E2767E007EF2 |

At that graph hash the promoted boundary was still Round 12. The seam and
analytic envelope were proved only through $\varepsilon=1/20$ and the
ceiling $3300^2$. SHELL-rho-compact, SHELL-rho-uniformity, and
TARGET-shell-d3 were open; COMP-certified-bessel was diagnostic_only; and
the complete thin endpoint was exactly $99/100\le\rho<1$. The graph
validator returned “Graph OK,” and every graph evidence path existed.
Thus the proof did not import the desired Round 13 conclusion.

## 2. Dangerous low-interface branch

Put

$$
y=\sqrt\varepsilon,\qquad
\rho=1-y^2,\qquad
\kappa=Ky^4.
$$

Then

$$
0<y\le\frac1{\sqrt{10}},\qquad
\rho\ge\frac9{10},\qquad
\kappa\ge24.
$$

Retain

$$
R=p-dm,\qquad
P=py,\qquad r=Ry,\qquad S=(p+m)y.
$$

Because

$$
\left(\frac9{10}\right)^2-\left(\frac{\sqrt3}{2}\right)^2
=\frac3{50}>0,
$$

monotonicity of arccosine gives

$$
d=1-\frac{2\arccos\rho}{\pi}>\frac23.
\tag{R4}
$$

If $R>0$, then $p>0$ and

$$
m<\frac pd<\frac32p,\qquad S<\frac52P.
\tag{R5}
$$

The no-drop branch $p=n>0$ has $m=0$ and is included.

Writing

$$
t=\frac{x_0}{\rho K},\qquad
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},\qquad
\widehat q=\frac{y^2}{\rho}(Q-1),
$$

the identities $U=n+\beta$ and $0\le\beta<1$, followed by the shelf
estimate and (R5), give

$$
1-t<\widehat q
<
\frac{y^4}{\kappa\rho}
+\frac52y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{R6}
$$

Both $y^4/(1-y^2)$ and $y/\sqrt{1-y^2}$ increase for $y>0$, and both
terms decrease with $\kappa$. Hence the endpoint comparison at
$y^2=1/10$, $\kappa=24$ is valid. Using
$\pi<1571/500<22/7$,

$$
\widehat q
<
\frac1{2160}+\frac52\frac{171}{1000}
=\frac{2311}{5400}
=\frac37-\frac{23}{37800}
<\frac37.
\tag{R7}
$$

Consequently

$$
\frac{x_0}{K}=\rho t
>\frac9{10}\frac47
=\frac{18}{35}
=\frac12+\frac1{70}.
\tag{R8}
$$

The outer-region slope is therefore used only after localization.

For $0<z<\mu$,

$$
\sigma(z):=-A'(z)
=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right)
$$

is positive and increasing. At $x_0=\mu t$,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{R9}
$$

Also

$$
1-\rho t=\varepsilon+\frac UK<y^2Q,
\qquad
1-\rho^2t^2<2y^2Q.
\tag{R10}
$$

On $R>0$, equality of the ordinary floors at $x_0$ and $x_0+p$ implies,
even if either shifted value is integral,

$$
0<A(x_0)-A(x_0+p)<1.
\tag{R11}
$$

Equations (R9)--(R11), monotonicity of $\sigma$, and
$t>1-\widehat q>4/7$ give, after squaring only positive quantities,

$$
\boxed{
P^2<
H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{R12}
$$

This remains strict on every ordinary-floor wall.

## 3. Complete incumbent synthetic path

The exact relation is

$$
P-r=dmy,\qquad
S=P+\frac{P-r}{d}.
\tag{R13}
$$

Thus $0<r\le P$. For fixed $P,y,\kappa,d$, $Q$ and $H$ decrease as $r$
increases because

$$
\frac{\partial H}{\partial Q}
=2\pi^2\frac{1+\widehat q+2a}{(1-\widehat q)^3}>0,
\qquad a=\frac{y^2}{\rho}.
$$

Let $B=14/3$ and suppose $r\ge B$. Fix $r=B$ along the complete path
$X\in[B,P]$:

$$
S_B(X)=X+\frac{X-B}{d}.
$$

Every point obeys the shelf ceiling because $X\le P$ and
$S_B(X)<5X/2$. Thus (R7) holds along the entire path. Moreover,

$$
\frac{dQ_B}{dX}<\frac1{30},
$$

and exact differentiation gives

$$
\frac{dH_B}{dX}
<
\frac{1572142117}{270000000}
=6-\frac{47857883}{270000000}
<6.
\tag{R14}
$$

Hence

$$
\frac d{dX}(X^2-H_B(X))
>2X-6\ge\frac{10}{3}>0.
\tag{R15}
$$

At $X=r=B$, including the possible no-drop endpoint $P=r=B$, one has
$S=B$ and

$$
Q<\frac{3839}{3600},\qquad
\widehat q<\frac{239}{32400}.
$$

The exact endpoint reserve is

$$
B^2-
\frac{2(1571/500)^2(3839/3600)}
     {(1-239/32400)^2}
=
\frac{2376966388822}{5818105805625}>0.
\tag{R16}
$$

Equations (R14)--(R16) force $P^2>H(P,B)\ge H(P,r)$, contradicting
(R12). Therefore

$$
\boxed{R<\frac{14}{3\sqrt\varepsilon}.}
\tag{R17}
$$

No sampled sign or endpoint-only extrapolation occurs.

## 4. Independent clean-room path

The clean-room artifact gives a materially different route. It first
derives directly

$$
\frac{x_0}{K}>
\frac9{10}-\frac{43}{112}-\frac1{2400}
=\frac{8663}{16800}
=\frac{18}{35}+\frac{23}{16800}
>\frac12.
\tag{R18}
$$

It obtains (R12) from the integral representation of the local slope, then
assumes $r\ge B=14/3$ and uses

$$
S\le L(P),\qquad L(X)=\frac52X-7.
$$

Along $B\le X\le P$, set

$$
F(X)=X^2(1-h_X)^2-2\pi^2Q_X,
$$

where $Q_X=1+y^2/\kappa+yL(X)/\kappa$ and
$h_X=(y^2/\rho)(Q_X-1)$. The whole path satisfies

$$
h_X<\frac37,\qquad Xh_X'<\frac{215}{504}.
$$

At $X=B$,

$$
F(B)>\frac{12760228}{48234375}>0,
\tag{R19}
$$

and throughout the path

$$
F'(X)>\frac{229}{2646}>0.
\tag{R20}
$$

The actual endpoint would require $F(P)<0$ by self-consistency, a
contradiction. This separately proves (R17), including $P=r=B$.

Artifact-level isolation passes. The clean-room file was created before
the incumbent file, expressly records its restricted inputs, uses different
localization constants, a different comparison function and synthetic
path, and different payment constants. The shared $B=14/3$ was navigation
data in the frozen packet. Its opening inventory calls the permitted
weighted scaffold “SHELL-weighted-lattice-fractional”; the repository packet
of that name contains the scaffold section actually used, and the proof uses
only that permitted dimension-reduction implication, not the larger theorem
as an extra premise. I therefore classify this as a naming imprecision, not
an isolation or dependency failure. The previously noted missing backslash
before `\qquad` in the clean-room union display was corrected before
promotion; it was presentational and did not affect the formula.

## 5. Action payment and exceptional branches

From $\arccos(1-v)\ge\sqrt{2v}$ and the exact action identity,

$$
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2},
\qquad
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
\tag{R21}
$$

Using

$$
\frac{140}{99}<\sqrt2,\qquad
\pi<\frac{1571}{500},\qquad
\frac1y\ge\sqrt{10}>\frac{79}{25},
$$

the incumbent route gives

$$
K\eta>\frac{1120000}{155529}\frac1y.
$$

On $R>0$, (R17) and $\lfloor x\rfloor>x-1$ yield

$$
M-4\delta>
\frac{170244091}{27217575}>0.
\tag{R22}
$$

On $R\le0$ the larger reserve is

$$
M-4\delta>
\frac{571612597}{27217575}>0.
\tag{R23}
$$

The clean-room route independently gives
$M>351/55$, $4\delta<4/5$, and reserve $307/55$ on the dangerous branch.

Every exceptional branch is owned:

- $p=n>0$ gives $m=0$ and $r=P$, covered by both complete paths;
- $p=0<n$ gives $R=-dn<0$, covered by the safe branch;
- $n=0$ has $p=m=R=0$, covered by the safe branch;
- $R=0$ belongs to the safe branch;
- the first discrete $R>0$ branch is covered without a positive lower gap.

Substitution of (R22)--(R23) into the promoted pre-threshold decomposition
settles every low-interface shifted tail. The promoted high-interface
theorem owns $x_0\ge\mu$. The promoted weighted scaffold and strict phase
majorant then give (R1). This is an analytic ledger, not a Bessel-root
certificate.

## 6. Integer, interface, threshold, angular, and spectral walls

1. At $\mu-x_0\in\mathbb Z$, $\beta=0$, $q=\mu$, and
   $U=n=p+m<1+p+m$ remains strict. The same bound survives as
   $\beta\to1^-$ on the adjacent cell.
2. At $q=\mu$, $\delta=0$. At $x_0=\mu$, the high-interface theorem owns
   equality; the low-side $n=0$ branch is safe.
3. At every proxy integer wall, equal ordinary floors still imply the
   strict difference (R11). A jump of $p$ selects another covered branch.
4. At $K\eta\in\mathbb Z$, $\lfloor K\eta\rfloor>K\eta-1$ remains strict.
5. All estimates assume $\kappa\ge24$, so threshold equality is included.
   The retained Round 10 equality $\kappa=20$ is used only for
   $\varepsilon\le1/25$.
6. The sharp angular cutoff is $\nu<K$; $\nu=K$ contributes no channel.
   At a shell eigenfrequency the count uses $n\pi<\Psi(K)$, so the endpoint
   eigenvalue is excluded. The ordinary floor is only a majorant.
7. The faces $\varepsilon=1/100$, $1/25$, $1/20$, and $1/10$ are covered.
   At $1/20$ the two constant-$24$ theorems overlap; at $1/25$ and
   $1/100$ the retained constant-$20$ theorem is sharper.

No step assumes continuity across an integer wall, and no strict spectral
bracket is replaced by equality.

## 7. Exact central endpoint

At $\rho=9/10$,

$$
a_\rho=18\pi<18\frac{22}{7}<8^2
$$

with margin $52/7$. The action bound gives

$$
\eta_{9/10}
\ge\frac1{15\pi\sqrt5}
>\frac1{107},
$$

because $\sqrt5<9/4$ and

$$
107-15\frac{22}{7}\frac94=\frac{13}{14}>0.
$$

Also

$$
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
$$

For

$$
f(Y)=\eta_{9/10}Y^2-\sqrt{a_{9/10}}Y-C_0,
$$

the exact comparison is

$$
f(900)>
\frac{900^2}{107}-8\cdot900-\frac{307}{175}
=\frac{6897151}{18725}>0.
\tag{R24}
$$

Since $f(0)<0$, its leading coefficient is positive, and its roots have
negative product, it has exactly one positive root. Positivity at $900$
puts that root below $900$. Formula for $K_0$ is its square, proving (R2).
The faces $K=K_0(9/10)$ and $K=900^2$ are both owned.

## 8. Five-zone closed union and face ownership

| Closed ratio zone | Input | Possible residual |
| --- | --- | ---: |
| $[\rho_*,1/16]$ | small-hole/low-ratio envelope | $K<64$ |
| $[1/16,9/10]$ | monotone fixed-ratio threshold and (R2) | $K<K_0(9/10)<900^2$ |
| $[9/10,19/20]$ | new Round 13 seam | $K<9600$ |
| $[19/20,24/25]$ | retained Round 12 seam | $K<15000$ |
| $[24/25,99/100]$ | retained Round 10 seam | $K<200000$ |

The neighboring endpoint zones are all-frequency:
$0<\rho\le\rho_*$ and $99/100\le\rho<1$.

The three seam ceilings are

$$
\frac{24}{(1/20)^2}=9600,\qquad
\frac{24}{(1/25)^2}=15000,\qquad
\frac{20}{(1/100)^2}=200000,
$$

and

$$
64<9600<15000<200000<900^2.
\tag{R25}
$$

All shared faces are owned: $\rho_*$, $1/16$, $9/10$, $19/20$,
$24/25$, and $99/100$. The residual bounds are strict, so every frequency
threshold face is proved. In particular, $K=900^2$ is above each value in
(R25) and is owned centrally by (R2). This proves (R3).

The exact reduction is

$$
\frac{3300^2}{900^2}
=\frac{121}{9}
=13+\frac49>13.
$$

Nothing assigns all-frequency coverage to a ratio below $99/100$.

## 9. Executable reproduction

I executed the Python block embedded in the incumbent Markdown. It printed:

~~~text
all exact Round 13 incumbent ledger checks passed
~~~

I then ran:

~~~text
python computations/round13_verify_seam_extension.py
python -m pytest computations/tests/test_round13_seam_extension.py -q
python -m pytest computations/tests -q
~~~

The standalone verifier reproduced both analytic routes and printed PASS.
The focused suite reported 5 passed; the full suite reported 45 passed.
It reproduced the incumbent margins

$$
\frac{23}{37800},\quad
\frac{2376966388822}{5818105805625},\quad
\frac{170244091}{27217575},
$$

the independent margins

$$
\frac{23}{16800},\quad
\frac{12760228}{48234375},\quad
\frac{229}{2646},\quad
\frac{307}{55},
$$

and the endpoint margin $6897151/18725$. These executions verify finite
exact algebra; the analytic arguments were reconstructed above.

## 10. Promotion boundary

This PASS supports strengthening SHELL-central-thin-seam-compression
through $\varepsilon=1/10$ and strengthening the analytic envelope to the
five-zone $900^2$ ceiling. It does not support closing:

- SHELL-rho-compact;
- COMP-certified-bessel;
- SHELL-rho-uniformity;
- TARGET-shell-d3.

They must remain respectively open, diagnostic_only, open, and open until
the true compact residual below $900^2$ is covered and theorem-level audits
pass. The rational verifier is not a Bessel-root certificate.

## Final adversarial finding

**PASS.** The corrected frozen local theorem, the exact endpoint
$K_0(9/10)<900^2$, the five-zone union, threshold equality, all discrete
and spectral walls, and the unchanged endpoint boundary are supported.
The first unsupported implication is **none**.
