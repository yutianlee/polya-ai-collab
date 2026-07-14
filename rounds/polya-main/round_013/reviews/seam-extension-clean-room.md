# Round 13 strict clean-room reconstruction

## Isolation boundary and verdict

I fixed the verdict **PASS** before writing this file.  Before that verdict I
read only the corrected frozen packet
`state/lemma_packets/SHELL-central-thin-seam-compression-round13.md` and the
following promoted inputs explicitly allowed by it:

- `SHELL-sturm-liouville-completeness`;
- `SHELL-phase-enclosures`;
- `SHELL-weighted-lattice-fractional` (the weighted scaffold);
- `SHELL-low-interface-fixed-rho-high-energy` (the audited decomposition).

I did not inspect any other Round 13 response, exploration, computation,
test, review, judge artifact, or proof-agent output.  In particular, no open
compact, certification, uniformity, or final-target obligation is used below.
The constants displayed as a preliminary screen in the frozen packet were
treated only as candidate navigation data; every inequality used below is
reconstructed.

The independent conclusion is

$$
0<\varepsilon\le\frac1{10},\qquad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le \frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3.
\tag{C1}
$$

Threshold equality is included.  I also verify

$$K_0(9/10)<900^2$$

and the closed all-ratio consequence for $K\ge900^2$.

## 1. Exact elementary bounds and localization

Put $y=\sqrt\varepsilon$, $\rho=1-y^2$, and
$\kappa=Ky^4$.  Throughout,

$$0<y\le\frac1{\sqrt{10}},\qquad \rho\ge\frac9{10},
\qquad \kappa\ge24.$$

Since

$$
\frac9{10}>\frac{\sqrt3}{2}
\quad\left(\frac{81}{100}>\frac34\right),
$$

monotonicity of arccosine gives

$$
\arccos\rho<\frac\pi6,qquad
d=1-\frac{2\arccos\rho}{\pi}>\frac23.
\tag{C2}
$$

Assume first that $R>0$.  Then $p>dm$, so

$$m<\frac p d<\frac32p,qquad n=p+m<\frac52p.$$

As $U=n+\beta$ and $0\le\beta<1$, the unconditional shelf estimate gives

$$
\frac{x_0}{K}
=\rho-\frac UK
>\rho-\frac52y\sqrt{\frac{2\pi\rho}{\kappa}}
-\frac{y^4}{\kappa}.
\tag{C3}
$$

The function $t(1-t)$ is increasing on $0<t\le1/10$, so
$y^2\rho\le9/100$.  Using $\pi<22/7$,

$$
y\sqrt{\frac{2\pi\rho}{\kappa}}
\le\sqrt{\frac{3\pi}{400}}
<\sqrt{\frac{33}{1400}}
<\frac{43}{280},
$$

where the last comparison is exact because

$$
\left(\frac{43}{280}\right)^2-\frac{33}{1400}
=\frac1{78400}>0.
$$

Also $y^4/\kappa\le1/2400$.  Hence

$$
\frac{x_0}{K}
>\frac9{10}-\frac{43}{112}-\frac1{2400}
=\frac{8663}{16800}
=\frac{18}{35}+\frac{23}{16800}
>\frac12.
\tag{C4}
$$

This estimate is uniform at $y=1/\sqrt{10}$ and $\kappa=24$; no sampled
monotonicity is being used.

## 2. Local slope and self-consistency

Direct differentiation gives

$$G_a'(z)=-\frac1\pi\arccos\frac za$$

for $0<z<a$, with the corresponding one-sided endpoint formula.  Thus $A$
is decreasing on $(0,\mu]$.  In the branch $R>0$ one has $p>0$, and the
plateau definition gives $h_0=h_p$.  If
$u=A(x_0)+1/4$ and $v=A(x_0+p)+1/4$, then

$$h_0\le v\le u<h_0+1,$$

even when either endpoint is an integer.  Therefore

$$0<A(x_0)-A(x_0+p)<1.\tag{C5}$$

For $x_0\le z\le x_0+p\le q\le\mu$,

$$
-A'(z)
=\frac1\pi\int_{z/K}^{z/\mu}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon z}
{\pi\rho K\sqrt{1-(z/K)^2}}.
\tag{C6}
$$

The last expression is increasing with $z$.  Integrating (C6), including
the improper one-sided limit when $x_0+p=\mu$, and using (C5), yields, with
$t=x_0/K$,

$$
P<\frac{\pi\rho\sqrt{1-t^2}}{yt}.
\tag{C7}
$$

The exact scaled relation is

$$
r=(1+d)P-dS,qquad P-r=d(S-P)=dmy.
\tag{C8}
$$

Set

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},qquad
\widehat q=\frac{y^2}{\rho}(Q-1)
=\frac{y^4+y^3S}{\rho\kappa}.
$$

Since $R>0$, (C2) gives $S<5P/2$.  The shelf bound becomes

$$P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.$$

Consequently

$$
\widehat q
<\frac{y^4}{\rho\kappa}
+\frac52y\sqrt{\frac{2\pi}{\rho\kappa}}.
\tag{C9}
$$

Here

$$
\frac{y^4}{\rho\kappa}\le\frac1{2160},
\qquad
y\sqrt{\frac{2\pi}{\rho\kappa}}
\le\sqrt{\frac\pi{108}}
<\sqrt{\frac{11}{378}}
<\frac{43}{252},
$$

and

$$
\left(\frac{43}{252}\right)^2-\frac{11}{378}
=\frac1{63504}>0.
$$

Thus

$$
0<\widehat q
<\frac1{2160}+\frac52\frac{43}{252}
=\frac{6457}{15120}
=\frac37-\frac{23}{15120}
<\frac37.
\tag{C10}
$$

Let

$$
\chi=\frac{U}{\rho K}
=\frac{y^3S+\beta y^4}{\rho\kappa}.
$$

Because $\beta<1$, $\chi<\widehat q$, and
$t=\rho(1-\chi)>\rho(1-\widehat q)>0$.  Moreover,

$$
1-t
=y^2+\frac{y^3S+\beta y^4}{\kappa}
<y^2Q,
$$

so $1-t^2<2y^2Q$.  All denominators are positive by (C4) and
(C10).  Substitution into (C7) gives

$$
P<\frac{\pi\sqrt{2Q}}{1-\widehat q},
\qquad
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}}.
\tag{C11}
$$

All quantities squared in (C11) are positive; no sign is lost.

## 3. Complete synthetic comparison path

I prove

$$\boxed{r< B:=\frac{14}{3}}.\tag{C12}$$

Suppose instead that an actual configuration has $r\ge B$.  By (C8),
$P\ge r\ge B$ and

$$S=P+\frac{P-r}{d}\le L(P),qquad
L(X):=\frac52X-7.\tag{C13}$$

Indeed, if $P>r$, use $1/d<3/2$; if $P=r$, then $S=P$ and
$P\le L(P)$ for $P\ge14/3$.  Equality in (C13) is allowed at the
no-drop endpoint $P=r=B$, where $m=0$.

For every synthetic $X\in[B,P]$, define

$$
Q_X=1+\frac{y^2}{\kappa}+\frac{yL(X)}{\kappa},qquad
h_X=\frac{y^2}{\rho}(Q_X-1),
$$

and

$$F(X)=X^2(1-h_X)^2-2\pi^2Q_X.$$

The whole path, not just its endpoint, stays in the safe region.  Since
$X\le P$ and the actual $P$ satisfies the shelf bound,

$$
h_X<\frac{y^4}{\rho\kappa}
+\frac{5y^3P}{2\rho\kappa}<\frac37,
\qquad
Xh_X'<\frac{215}{504}.
\tag{C14}
$$

At the actual endpoint, (C13) and (C11) imply

$$P^2<\frac{2\pi^2Q_P}{(1-h_P)^2},$$

and hence $F(P)<0$.

At $X=B$, $L(B)=B$.  Since $y<1/3$ and $\kappa\ge24$,

$$
Q_B
<1+\frac1{240}+\frac7{108}
=\frac{2309}{2160}<\frac{15}{14},
$$

and, because $y^2/\rho\le1/9$,

$$h_B<\frac{149}{19440}<\frac1{125}.$$

Using $\pi<22/7$ gives the exact positive endpoint reserve

$$
F(B)>
\frac{196}{9}\left(\frac{124}{125}\right)^2
-2\left(\frac{22}{7}\right)^2\frac{15}{14}
=\frac{12760228}{48234375}>0.
\tag{C15}
$$

Finally,

$$
Q_X'=\frac{5y}{2\kappa},qquad
h_X'=\frac{5y^3}{2\rho\kappa},
$$

and

$$
F'(X)
=2X(1-h_X)(1-h_X-Xh_X')-2\pi^2Q_X'.
$$

Equations (C10) and (C14), $X\ge14/3$, $y<1/3$, and
$\kappa\ge24$ show uniformly along the complete path that

$$
\begin{aligned}
F'(X)
&>2\frac{14}{3}\frac47
\left(\frac47-\frac{215}{504}\right)
-\frac{5(22/7)^2}{72}\\
&=\frac{146}{189}-\frac{605}{882}
=\frac{229}{2646}>0.
\end{aligned}
\tag{C16}
$$

Thus $F(P)\ge F(B)>0$, contradicting $F(P)<0$.  This proves (C12),
including the putative endpoint $P=r=B$.

## 4. Action payment and the local theorem

If $\theta=\arccos(1-v)$, then
$v=1-\cos\theta\le\theta^2/2$, so
$\arccos(1-v)\ge\sqrt{2v}$.  The action identity therefore gives

$$
\eta\ge\frac{2\sqrt2}{3\pi}y^3,qquad
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
\tag{C17}
$$

Use the exact elementary comparisons

$$
\frac75<\sqrt2<\frac32,qquad \pi<\frac{22}{7},
\qquad \sqrt{10}>3.
$$

If $R\le0$, then

$$
K\eta>\frac{49}{165}\frac\kappa y
>\frac{1176}{55}>21,
$$

so $M\ge\lfloor K\eta\rfloor\ge21$.

If $R>0$, (C12), the strict floor inequality
$\lfloor x\rfloor>x-1$ (also at integer $x$), and (C17) give

$$
\begin{aligned}
M
&>K\eta-1-\frac{B}{y}\\
&\ge\frac1y
\left(\frac{2\sqrt2\,\kappa}{3\pi}-\frac{14}{3}\right)-1\\
&>3\left(\frac{392}{55}-\frac{14}{3}\right)-1
=\frac{351}{55}.
\end{aligned}
\tag{C18}
$$

In both cases,

$$4\delta<\frac{8\sqrt2}{15}<\frac45<M.$$

The audited decomposition now yields for every low-interface tail

$$
\frac{\mathcal T_{r_0}}2
\le\int_{x_0}^K A(z)\,dz+\delta-\frac M4
<\int_{x_0}^K A(z)\,dz.
\tag{C19}
$$

The permitted high-angular tail theorem handles $x_0\ge\mu$.  The weighted
dimension-reduction scaffold therefore bounds the complete coarse ordinary-
floor proxy by

$$\int_0^K2zA(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3.$$

The phase enclosure and strict separated spectral count put the actual
count below this coarse proxy.  This proves (C1).

## 5. Branches, integer walls, and strict walls

- If $n=0$, the convention gives $p=m=R=0$, so the $R\le0$ payment applies.
- If $p=0$, then $R=-dm\le0$; this includes the immediate-drop branch.
- If $p=n$, then $m=0$, $R=p$, and $r=P$.  The slope proof remains valid
  up to $q\le\mu$, and the synthetic comparison explicitly excludes
  $P=r=B$.
- The sign wall $R=0$ belongs to the $R\le0$ branch.  The first discrete
  configuration with $R>0$ is covered without a lower gap because only the
  strict sign $R>0$ was used.
- At $\mu-x_0\in\mathbb Z$, one has $\beta=0$, $q=\mu$, and $\delta=0$.
  On the adjacent floor cell $0<\beta<1$; all estimates use the full closed-
  open range $0\le\beta<1$ and do not assume continuity of $n$.
- At every wall $A(x_0+j)+1/4\in\mathbb Z$, the implication
  $h_0=h_p\Rightarrow A(x_0)-A(x_0+p)<1$ remains strict because
  $h\le u<h+1$.  Thus no strict bracket was replaced by an ordinary-floor
  equality.
- At $K\eta\in\mathbb Z$, $\lfloor K\eta\rfloor>K\eta-1$ is still strict.
- The interface $x_0=\mu$ belongs to the high-angular theorem; the low side,
  including its $n=0$ cell, is covered by (C19).
- At $\nu=K$ the channel is excluded by the sharp active condition
  $\nu<K$.  At a shell eigenfrequency the radial count uses
  $n\pi<\Psi(K)$, hence the endpoint level is excluded.  The ordinary floor
  is used only as a majorant.
- The proof uses only $\kappa\ge24$, so equality
  $K=24/\varepsilon^2$ is owned.  The retained Round 10 equality
  $\kappa=20$ is invoked only on its proved range
  $\varepsilon\le1/25$.

## 6. The exact central endpoint

At $\rho=9/10$,

$$a_{9/10}=18\pi<\frac{396}{7}<64,$$

so $\sqrt a<8$.  From (C17) at $\varepsilon=1/10$,

$$
\eta_{9/10}\ge\frac1{15\pi\sqrt5}>\frac1{107},
$$

because $\sqrt5<9/4$ and
$15(22/7)(9/4)=1485/14<107$.  Also

$$
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175},
$$

using $\sqrt2<99/70$, whose squared reserve over $2$ is $1/4900$.

For $Y=\sqrt K$, the defining positive root of $K_0$ is the unique positive
root of

$$f(Y)=\eta_{9/10}Y^2-\sqrt{a_{9/10}}Y-C_0.$$

At $Y=900$,

$$
f(900)>
\frac{900^2}{107}-8(900)-\frac{307}{175}
=\frac{6897151}{18725}>0.
$$

Since $f(0)=-C_0<0$ and this upward quadratic has exactly one positive
root, that root is below $900$.  Hence

$$\boxed{K_0(9/10)<900^2}.\tag{C20}$$

The fixed-ratio theorem owns $K=K_0(9/10)$ itself; since the inequality in
(C20) is strict, it also owns $K=900^2$.

## 7. Closed global union and all mandatory faces

Using only the union inputs permitted by the frozen packet gives the
following exact residual cover:

| ratio zone | possible residual |
|---|---:|
| $0<\rho\le\rho_*$ | none (proved small-hole endpoint) |
| $[\rho_*,1/16]$ | $K<64$ |
| $[1/16,9/10]$ | $K<K_0(9/10)<900^2$ |
| $[9/10,19/20]$ | $K<9600$ by (C1) |
| $[19/20,24/25]$ | $K<15000$ by Round 12 |
| $[24/25,99/100]$ | $K<200000$ by Round 10 |
| $[99/100,1)$ | none (proved all-frequency endpoint) |

The seam bounds follow from the worst endpoint in each closed zone:

$$
\frac{24}{(1/20)^2}=9600,\qquad
\frac{24}{(1/25)^2}=15000,qquad
\frac{20}{(1/100)^2}=200000.
$$

All shared faces are owned: $\rho_*$ and $1/16$ by their two adjacent
promoted results; $9/10$ by both the central theorem and (C1); $19/20$ by
(C1) and Round 12; $24/25$ by Round 12 and the sharper Round 10 theorem;
and $99/100$ by Round 10 and the all-frequency endpoint.  Likewise $K=64$
is owned by the relevant small-hole transition result, and $K=900^2$ is
owned by (C20) on the central zone and lies above every seam threshold.

The special epsilon faces agree exactly:

- at $\varepsilon=1/100$, Round 10 applies at $\kappa=20$, while the
  separate Round 11 endpoint owns every frequency;
- at $\varepsilon=1/25$, Round 10 retains the sharper $\kappa=20$ result,
  while (C1) and Round 12 also apply at $\kappa=24$;
- at $\varepsilon=1/20$, (C1) and Round 12 both own $\kappa=24$;
- at $\varepsilon=1/10$, (C1) owns $\kappa=24$.

Thus no theorem is extrapolated beyond its domain.  Since

$$64<9600<15000<200000<900^2,$$

the closed union proves

$$
\boxed{0<\rho<1,\qquad K\ge900^2.}\tag{C21}
$$

The ceiling reduction is exactly

$$\frac{3300^2}{900^2}=\frac{121}{9}>13.$$

This does **not** enlarge the complete all-frequency endpoint beyond
$[99/100,1)$, and it does **not** close the compact residual below $900^2$.
Accordingly, the compact, certification, uniformity, and final-target
obligations must remain open.

## Final clean-room verdict

**PASS.**  The frozen Round 13 local claim, the exact central endpoint, and
the closed all-ratio high-frequency union all follow by the exact argument
above.  I found no unsupported implication and used no Round 13 proof or
computational artifact.
