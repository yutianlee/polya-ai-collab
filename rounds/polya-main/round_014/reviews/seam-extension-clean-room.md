# Round 14 central--thin seam extension: isolated clean-room review

Packet SHA-256: `19a9f76d88e6aaac0cdc772c22690fcb03e0c9ff5ac7b0761294005e0a152860` (verified before beginning).

Isolation declaration: I did not inspect any Round 14 response, proof, exploration, computation, ledger, test, review, judge artifact, diff, agent message, or incumbent output. I inspected only the frozen Round 14 packet and, from its expressly permitted pre-Round-14 inputs, the promoted statements `SHELL-phase-enclosures` and `SHELL-sturm-liouville-completeness`. All calculations below were reconstructed independently.

**Verdict: PASS.** The seam claim with (0<\varepsilon\le 1/8), including (K=32/\varepsilon^2), is proved. Independently, (K_0(7/8)<550^2) is proved. The six-zone consequence therefore follows. **First unsupported implication: none.**

## 1. Exact elementary bounds

I use the standard positive integral certificate

\[
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\tag{35}
\]

Indeed, polynomial division and (4\arctan 1=\pi) give the equality in (35). I also use only the following square comparisons:

\[
2-\left(\frac75\right)^2=\frac1{25}>0,
\qquad
\left(\frac32\right)^2-2=\frac14>0,
\qquad
\left(\frac{47}{10}\right)^2-22=\frac9{100}>0.
\tag{36}
\]

Thus

\[
\pi<\frac{22}{7},\qquad
\frac75<\sqrt2<\frac32,\qquad
\sqrt{22}<\frac{47}{10}.
\tag{37}
\]

All quantities divided by below are positive because

\[
y>0,\quad \kappa\ge32>0,\quad \rho=1-y^2\ge\frac78>0.
\tag{38}
\]

Moreover (y\le\sqrt2/4<3/8), (y^2/\rho\le1/7), and (1/y\ge2\sqrt2>14/5). These include the faces (y=1/(2\sqrt2)) and (\kappa=32).

## 2. Angular bound and the dangerous-branch localization

Since

\[
\left(\frac78\right)^2-\left(\frac{\sqrt3}{2}\right)^2
=\frac1{64}>0,
\tag{39}
\]

we have

\[
\rho\ge\frac78>\frac{\sqrt3}{2},
\qquad
0<c=\frac{\arccos\rho}{\pi}<\frac16,
\qquad
\boxed{\frac23<d=1-2c<1}.
\tag{40}
\]

The strict lower bound remains strict at (\rho=7/8); this is the exact role of the angular reserve.

Assume now (R>0). Then (p>0), and

\[
p>dm>\frac23m,
\qquad m<\frac32p,
\qquad n=p+m<\frac52p.
\tag{41}
\]

The scaled variables satisfy the exact relations

\[
r=(1+d)P-dS,
\qquad
P-r=dmy\ge0,
\qquad
S=P+\frac{P-r}{d}.
\tag{42}
\]

Also, directly from the definitions,

\[
Q-1=\frac{n+1}{K\varepsilon},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1)=\frac{n+1}{\mu}.
\tag{43}
\]

Using (41), the strict shelf estimate, (K\ge32/y^4), and (37),

\[
\begin{aligned}
\widehat q
&<\frac{(5/2)p+1}{\rho K}\\
&<\frac52\sqrt{\frac{2\pi}{\rho K\varepsilon}}
  +\frac1{\rho K}\\
&\le \frac{5y}{8}\sqrt{\frac\pi\rho}
  +\frac{y^4}{32\rho}\\
&\le \frac{5\sqrt{22}}{56}+\frac1{1792}\\
&<\frac{47}{112}+\frac1{1792}
=\frac{753}{1792}
<\boxed{\frac{17}{40}}.
\end{aligned}
\tag{44}
\]

The last strict comparison has the exact reserve

\[
\frac{17}{40}-\left(\frac{47}{112}+\frac1{1792}\right)
=\frac{43}{8960}>0.
\tag{45}
\]

There is no hidden worst-case optimization in (44): (y^2/\rho\le1/7), (y^4/\rho\le1/56), and (\kappa\ge32) give each displayed reduction directly.

Since (U=n+\beta<n+1), (43)--(44) give the strict localization

\[
\frac{x_0}{\mu}=1-\frac U\mu>1-\widehat q>\frac{23}{40},
\]

and hence, before any local-slope estimate is used,

\[
\boxed{
\frac{x_0}{K}
=\rho\frac{x_0}{\mu}
>\frac78\frac{23}{40}
=\frac{161}{320}
=\frac12+\frac1{320}.}
\tag{46}
\]

This proves the dangerous-plateau localization on the entire closed candidate parameter domain.

## 3. The strict local slope and self-consistency inequality

For (0\le z\le\mu), direct differentiation gives

\[
G_a'(z)=-\frac1\pi\arccos\frac za,
\qquad
-A'(z)=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right).
\tag{47}
\]

For (z\in[x_0,x_0+p]\), one has (x_0+p\le q\le\mu). Put

\[
t=1-\frac z\mu=\frac{\mu-z}{\mu},
\qquad
v=1-\frac zK=\varepsilon+\rho t,
\qquad
F(w)=\arccos(1-w).
\tag{48}
\]

By (44) and (46),

\[
0\le t<\widehat q<1,
\qquad
t<v<\frac12.
\tag{49}
\]

For (0\le t<v), interpreting the lower endpoint as an improper integral when (t=0),

\[
F(v)-F(t)
=\int_t^v\frac{dw}{\sqrt{w(2-w)}}
\ge\frac{v-t}{\sqrt{2v}}
=\frac{\varepsilon(1-t)}{\sqrt{2(\varepsilon+\rho t)}}.
\tag{50}
\]

Here every radicand is positive: (v\ge\varepsilon>0). Furthermore

\[
t<\widehat q,
\qquad
\rho t=\frac{\mu-z}{K}
\le\frac UK
<\frac{n+1}{K}=\varepsilon(Q-1).
\tag{51}
\]

Consequently (47)--(51) yield, uniformly along the whole plateau,

\[
-A'(z)>
\frac{y(1-\widehat q)}{\pi\sqrt{2Q}}.
\tag{52}
\]

For (R>0), (p>0). The equality of the ordinary floors (h_0=h_p) implies

\[
A(x_0)-A(x_0+p)<1.
\tag{53}
\]

This remains strict at every integer wall: if two ordinary floors equal (h), both arguments lie in the same half-open interval ([h,h+1)), so their nonnegative difference is strictly less than one. Integrating (52) and using (53) gives

\[
1>A(x_0)-A(x_0+p)
>\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
\tag{54}
\]

Because (P>0), (Q>1), and (1-\widehat q>23/40>0), division and squaring preserve direction. Thus

\[
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.}
\tag{55}
\]

This proves (27), including all denominator and squaring conditions.

## 4. A distinct complete comparison path and (R<14/(3\sqrt\varepsilon))

I use a comparison path different from the packet's navigation path. First, (41), (44), (55), (y<3/8), and (\pi<22/7) imply

\[
Q<\frac{257}{256}+\frac{15}{512}P
\tag{56}
\]

and

\[
P^2<C\left(\frac{257}{256}+\frac{15}{512}P\right),
\qquad
C=2\frac{484}{49}\left(\frac{40}{23}\right)^2
=\frac{1548800}{25921}.
\tag{57}
\]

Let (g(P)=P^2-C(257/256+15P/512)). Exact arithmetic gives

\[
g(9)=\frac{136376}{25921}>0,
\qquad
g'(P)\ge g'(9)=\frac{421203}{25921}>0
\quad(P\ge9).
\tag{58}
\]

Therefore (57) forces

\[
P<9.
\tag{59}
\]

Set

\[
B=\frac{14}{3}.
\tag{60}
\]

Suppose for contradiction that (r\ge B). From (42), (P\ge r\ge B), and (d>2/3) gives

\[
S=P+\frac{P-r}{d}
\le \frac52P-\frac32B
=\frac52P-7
=:\overline S(P).
\tag{61}
\]

Equality in the first comparison can occur only at the no-drop endpoint (P=r=B), where (m=0) and (S=P=B). Thus (61) owns that endpoint, rather than approaching it by a limit.

For fixed (y,\rho,\kappa), define

\[
\alpha=\frac{y^2}{\kappa},
\qquad b=\frac y\kappa,
\qquad \tau=\frac{y^2}{\rho},
\]

\[
\overline Q(P)=1+\alpha+b\overline S(P),
\qquad
\overline q(P)=\tau(\overline Q(P)-1),
\]

\[
\overline H(P)
=P^2(1-\overline q(P))^2-2\pi^2\overline Q(P).
\tag{62}
\]

On (B\le P<9),

\[
\overline S(P)<\frac{31}{2},
\qquad
\overline Q(P)-1<\frac{95}{512},
\qquad
\overline q(P)<\frac{95}{3584}<\frac1{32}.
\tag{63}
\]

For (H(P,Q)=P^2[1-\tau(Q-1)]^2-2\pi^2Q), one has

\[
\frac{\partial H}{\partial Q}
=-2\tau P^2[1-\tau(Q-1)]-2\pi^2<0
\tag{64}
\]

throughout (1\le Q\le\overline Q(P)), by (63). Since (Q\le\overline Q(P)), it follows that

\[
H(P,Q)\ge\overline H(P).
\tag{65}
\]

At the no-drop endpoint (P=B),

\[
\overline Q(B)<\frac{271}{256},
\qquad
\overline q(B)<\frac{15}{1792},
\]

and hence

\[
\begin{aligned}
\overline H(B)
&>\frac{196}{9}\left(\frac{1777}{1792}\right)^2
-2\frac{484}{49}\frac{271}{256}\\
&=\frac{3627793}{7225344}>0.
\end{aligned}
\tag{66}
\]

The entire synthetic path is (P\mapsto(P,\overline S(P))), of slope (5/2), from (B) to the putative actual (P). Its derivative is controlled pointwise, not merely at its endpoint:

\[
\overline q'(P)=\frac52\tau b<\frac{15}{3584},
\qquad
P\overline q'(P)<\frac5{128},
\tag{67}
\]

and therefore

\[
\begin{aligned}
\overline H'(P)
&=2P(1-\overline q)
 \bigl[(1-\overline q)-P\overline q'\bigr]
 -5\pi^2b\\
&>2\frac{14}{3}\frac{31}{32}\frac{119}{128}
 -5\frac{484}{49}\frac3{256}\\
&=\frac{1178207}{150528}>0.
\end{aligned}
\tag{68}
\]

Thus (66)--(68) give (\overline H(P)>0), and (65) gives (H(P,Q)>0). But (55) is exactly (H(P,Q)<0), a contradiction. Hence

\[
\boxed{r<\frac{14}{3}},
\qquad
\boxed{R<\frac{14}{3\sqrt\varepsilon}}.
\tag{69}
\]

This proof covers the whole comparison path and the no-drop endpoint. It does not use the packet's suggested slope (13/3) or its unproved path fractions.

## 5. Action gain and all plateau branches

From the permitted action identity and (\arccos(1-v)\ge\sqrt{2v}),

\[
\eta\ge\frac{2\sqrt2}{3\pi}y^3.
\tag{70}
\]

Using (37), (K=\kappa/y^4), and (\kappa\ge32),

\[
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}
>\frac{49\kappa}{165y}
\ge\frac{1568}{165y}
>\frac{21952}{825}.
\tag{71}
\]

Also

\[
4\delta<\frac{8\sqrt2}{15}<\frac45.
\tag{72}
\]

For every real (x), including integer (x), (\lfloor x\rfloor>x-1). Therefore gain-floor walls never destroy the strict reserve.

If (R\le0), including the sign wall (R=0), then

\[
M=\lfloor K\eta\rfloor-R
\ge\lfloor K\eta\rfloor
>\frac{21127}{825},
\]

so, exactly,

\[
M-4\delta>\frac{21127}{825}-\frac45
=\frac{20467}{825}>0.
\tag{73}
\]

If (R>0), (69)--(71) give

\[
K\eta-R
>\left(\frac{1568}{165}-\frac{14}{3}\right)\frac1y
=\frac{266}{55y}
>\frac{3724}{275}.
\]

Consequently

\[
M>\frac{3449}{275},
\qquad
M-4\delta>\frac{3449}{275}-\frac45
=\frac{3229}{275}>0.
\tag{74}
\]

Thus

\[
\boxed{M>4\delta}
\tag{75}
\]

in every branch. In particular:

- If (p=0), then (R=-dm\le0), so the immediate-drop branch is in (73).
- If (n=0), then (p=m=R=0), so the degenerate head is in (73).
- If (p=n), then (m=0) and (R=p). The case (p=0) is safe; the case (p>0) is the dangerous branch, including the no-drop comparison in (61)--(69).
- The first branch with (R>0) is covered uniformly by (44)--(74); no lower bound on (R) was used. The wall (R=0) itself belongs to (73), so both sides meet without a gap.

## 6. Closing the local seam theorem

The permitted low-interface decomposition now gives, for every (x_0<\mu),

\[
\frac{\mathcal T_{r_0}}2
\le\int_{x_0}^K A(z)\,dz+\delta-\frac M4
<\int_{x_0}^K A(z)\,dz.
\tag{76}
\]

The promoted strict-count/phase/floor/scaffold package and the promoted high-angular shifted-tail theorem cover, respectively, the low and high interfaces. Their exact weighted-lattice conclusion from (76) is

\[
N_D(A_{\rho,1},K^2)
\le 2\int_0^K z\,[G_K(z)-G_\mu(z)]\,dz.
\tag{77}
\]

For completeness, the continuous integral in (77) is reconstructed directly. With (z=at),

\[
\int_0^a zG_a(z)\,dz
=\frac{a^3}{\pi}
\left(\int_0^1t\sqrt{1-t^2}\,dt
-\int_0^1t^2\arccos t\,dt\right)
=\frac{a^3}{9\pi},
\tag{78}
\]

because the two integrals in parentheses are (1/3) and (2/9). Hence

\[
2\int_0^K zA(z)\,dz
=\frac{2}{9\pi}(K^3-\mu^3)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{79}
\]

Combining (77)--(79), with (\rho=1-\varepsilon), proves

\[
\boxed{
0<\varepsilon\le\frac18,\qquad
K\ge\frac{32}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.}
\tag{80}
\]

No step becomes non-strict when (\kappa=32) or (\varepsilon=1/8), so both threshold-equality faces are included.

## 7. Discrete, interface, and strict-wall audit

The remaining required walls are owned as follows.

- If (\mu-x_0\in\mathbb Z), then (\beta=0), (q=\mu), and (\delta=0). The strict proxy (U=n+\beta<n+1) remains valid. On either adjacent side (0<\beta<1), the same proxy and the same estimates apply. Thus the coarse-proxy integer jump creates no gap.
- Every ordinary-floor wall is covered by the half-open-interval argument in (53). No strict bracket was replaced by an ordinary-floor identity.
- At (K\eta\in\mathbb Z), (\lfloor K\eta\rfloor>K\eta-1) is still strict, as used in (73)--(74).
- The low proof treats (x_0<\mu). The exact interface (x_0=\mu) is owned by the permitted high-angular shifted-tail theorem; from the low side it is also the uniform (n=0,\beta\downarrow0,\delta\downarrow0) face. No conclusion is inferred merely from that limit.
- At the angular cutoff (\nu=K), (G_K(K)=0), and the promoted phase theorem is expressly valid at equality. The promoted strict counting theorem counts (n\pi<\Psi(K)), not (n\pi\le\Psi(K)); at a spectral endpoint it returns (m-1), while the ordinary floor is used only as an upper bound. Thus (80) includes (K) equal to any shell eigenfrequency.
- All square roots in (44), (50), (55), and (62)--(68) have positive radicands; (d>2/3), (1-\widehat q>23/40), (Q>1), and (P>0) justify every division and the only squaring in (55).
- All worst-face reductions use explicit inequalities (y^2\le1/8), (y<3/8), (\rho\ge7/8), and (\kappa\ge32). No sampled sign, optimizer, or limiting strictness is used.

## 8. Independent proof that (K_0(7/8)<550^2)

At (\rho=7/8), the action bound (70) gives

\[
\eta_{7/8}\ge\frac1{24\pi}.
\tag{81}
\]

By (35),

\[
24\pi<\frac{528}{7}<76,
\qquad
\boxed{\eta_{7/8}>\frac1{76}}.
\tag{82}
\]

Also

\[
a_{7/8}=14\pi<44<49,
\qquad
\boxed{\sqrt{a_{7/8}}<7}.
\tag{83}
\]

For the constant (C_0), the sharper exact square certificate

\[
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0
\tag{84}
\]

gives

\[
\boxed{
C_0=1+\frac{8\sqrt2}{15}
<1+\frac8{15}\frac{99}{70}
=\frac{307}{175}.}
\tag{85}
\]

Let

\[
f(X)=\eta_{7/8}X^2-\sqrt{a_{7/8}}X-C_0.
\]

At (Y=550), (82)--(85) give the strict exact comparison

\[
f(Y)>
\frac{Y^2}{76}-7Y-\frac{307}{175}
=\frac{427292}{3325}>0.
\tag{86}
\]

Since (\eta_{7/8}>0), (C_0>0), and (f(0)=-C_0<0), (f) has exactly one positive root,

\[
X_+=
\frac{\sqrt{a_{7/8}}+
\sqrt{a_{7/8}+4\eta_{7/8}C_0}}
{2\eta_{7/8}}.
\tag{87}
\]

Equation (86) places this root strictly below (Y). Both are positive, so squaring preserves direction. Formula (17) is (K_0(7/8)=X_+^2), and therefore

\[
\boxed{K_0(7/8)<550^2.}
\tag{88}
\]

The theorem at (K=K_0(7/8)) is included by its stated (K\ge K_0) hypothesis, and (K=550^2) lies strictly above it. This argument is independent of the seam proof.

## 9. Exact theorem overlaps and the six-zone consequence

On overlaps, the sharpest promoted theorem owns the common face:

| (\varepsilon) face | (\rho) face | owner | included scaled threshold |
|---:|---:|---|---:|
| (1/100) | (99/100) | Round 11 all-frequency endpoint | every (K) |
| (1/25) | (24/25) | Round 10 | (\kappa=20), i.e. (K=12500) |
| (1/20) | (19/20) | retained constant-(24) theorem | (\kappa=24), i.e. (K=9600) |
| (1/10) | (9/10) | Round 13, not the new coarser threshold | (\kappa=24), i.e. (K=2400) |
| (1/8) | (7/8) | (80) | (\kappa=32), i.e. (K=2048) |

Thus Round 10 remains sharper on its domain, and the all-frequency endpoint remains exactly (99/100\le\rho<1).

Using the permitted monotonicity of (K_0), the exact complement of the analytic cover is enclosed by the six finite zones:

| zone | ratio interval | possible residual only below |
|---:|---|---:|
| 1 | ([\rho_*,1/16]) | (64) |
| 2 | ([1/16,7/8]) | (K_0(\rho)\le K_0(7/8)<550^2) |
| 3 | ([7/8,9/10]) | (32/(1-\rho)^2\le3200) |
| 4 | ([9/10,19/20]) | (24/(1-\rho)^2\le9600) |
| 5 | ([19/20,24/25]) | (24/(1-\rho)^2\le15000) |
| 6 | ([24/25,99/100]) | (20/(1-\rho)^2\le200000) |

The adjacent complete small-hole theorem owns (\rho=\rho_*); both adjacent analytic regimes cover (\rho=1/16). At (\rho=7/8), (80) owns (K=2048). At (\rho=9/10), Round 13 owns the sharper (K=2400), though (3200) is a valid coarse enclosure. At (\rho=19/20), the constant-(24) theorem owns (K=9600). At (\rho=24/25), Round 10 owns the sharper (K=12500). At (\rho=99/100), the complete all-frequency theorem owns the face. Hence the energy faces (64,2048,2400,3200,9600,12500,15000,200000) are all included by a displayed adjacent theorem; residual inequalities are strict.

Finally,

\[
64<3200<9600<15000<200000<550^2=302500.
\tag{89}
\]

Together with the complete small-hole side and the unchanged complete endpoint (99/100\le\rho<1), (89) proves, including equality in (K),

\[
\boxed{0<\rho<1,\qquad K\ge550^2.}
\tag{90}
\]

The exact ceiling reduction is

\[
\frac{900^2}{550^2}=\frac{324}{121}>2
\quad\text{because}\quad324-2\cdot121=82>0.
\tag{91}
\]

This is only a high-frequency all-ratio consequence. It does not enlarge the
complete all-frequency ratio endpoint beyond $99/100\le\rho<1$, and it does
not close the compact residual.

## 10. Alternative exact reserve ledger

The packet's screen fractions were not used as assumptions. The independent path above supplies the following exact certificates for every corresponding role:

| role | exact certificate |
|---|---:|
| angular | (1/64) in (39) |
| radical | ((47/10)^2-22=9/100) |
| proxy/displacement | (43/8960) in (45), then (x_0/K-1/2>1/320) |
| preliminary (P)-cutoff | (g(9)=136376/25921) |
| full-path derivative | (1178207/150528) in (68) |
| no-drop endpoint | (3627793/7225344) in (66) |
| dangerous-branch payment | (3229/275) in (74) |
| safe-branch payment | (20467/825) in (73) |
| central endpoint | (427292/3325) in (86) |

Every entry is a positive rational number attached to its explicit inequality; none is a sampled or decimal sign.

## Final verdict

**PASS.** Both boxed targets (80) and (88), all exceptional branches, all strict and equality walls, the overlap ownership, and the six-zone consequence have exact proofs. **First unsupported implication: none.**
