# Round 14 seam-extension constant inventory

## Verdict and isolation

**PASS.**  The local seam theorem closes for

\[
0<\varepsilon\le \frac18,
\qquad \kappa=K\varepsilon ^2\ge32,
\]

including both equality faces.  Independently,
\(K_0(7/8)<550^2\) closes, and the six-zone residual envelope has no
unowned ratio, energy, or moving-\(K_0(\rho)\) face.

The only Round 14 input inspected was
`state/lemma_packets/SHELL-central-thin-seam-compression-round14.md`, whose
SHA-256 is
`19a9f76d88e6aaac0cdc772c22690fcb03e0c9ff5ac7b0761294005e0a152860`.
Everything else used below is one of the pre-Round-14 proved inputs permitted
there.

## 1. Elementary exact ledger

The rational bounds used throughout are

\[
\frac{140}{99}<\sqrt2<\frac{99}{70},
\qquad \pi<\frac{1571}{500}.
\tag{1.1}
\]

The radical bounds follow by squaring:

\[
2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0.
\tag{1.2}
\]

For completeness, the bound for \(\pi\) does not rely on decimal
evaluation.  Machin's identity

\[
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}
\]

follows from \(\tan(4\arctan(1/5))=120/119\), the tangent subtraction
formula, and the fact that the resulting angle lies in \((0,\pi/2)\).
The alternating arctangent series gives

\[
\frac\pi4<
4\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}\right)
-\left(\frac1{239}-\frac1{3\cdot239^3}\right)
=\frac{167535764926}{213311234375},
\]

and direct rational subtraction gives

\[
\frac{1571}{2000}-
\frac{167535764926}{213311234375}
=\frac{323354809}{3412979750000}>0.
\tag{1.3}
\]

Put \(y=\sqrt\varepsilon\), so

\[
0<y\le\frac1{2\sqrt2},\quad
\rho=1-y^2\ge\frac78,\quad
K=\frac\kappa{y^4},\quad \kappa\ge32.
\tag{1.4}
\]

Because

\[
\left(\frac78\right)^2-\left(\frac{\sqrt3}{2}\right)^2
=\frac1{64}>0,
\]

one has \(\rho>\cos(\pi/6)\), hence

\[
c=\frac{\arccos\rho}{\pi}<\frac16,
\qquad d=1-2c>\frac23=:d_0.
\tag{1.5}
\]

This identifies the advertised angular reserve \(1/64\).

## 2. Dangerous geometry, shelf, displacement, and localization

Assume first that \(R=p-dm>0\).  With

\[
P=py,\qquad r=Ry,\qquad S=(p+m)y=ny,
\]

the exact relation is

\[
r=P-d(S-P),\qquad
S=P+\frac{P-r}{d},\qquad 0<r\le P.
\tag{2.1}
\]

Moreover \(p>dm\), so (1.5) gives

\[
m<\frac32p,\qquad n=p+m<\frac52p,\qquad S<\frac52P.
\tag{2.2}
\]

Define

\[
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1).
\tag{2.3}
\]

Since \(S=ny\) and \(\mu=\rho\kappa/y^4\), this is exactly

\[
\widehat q=\frac{n+1}{\mu}.
\tag{2.4}
\]

The proved shelf estimate becomes

\[
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
\tag{2.5}
\]

The radical occurring in the displacement estimate satisfies

\[
D^2:=\frac{2\pi y^2}{\rho\kappa}
\le\frac\pi{112}
<\frac{1571/500}{112}
<\left(\frac{67}{400}\right)^2,
\]

where the last comparison has the exact reserve

\[
\left(\frac{67}{400}\right)^2-
\frac{1571/500}{112}
=\frac3{1120000}>0.
\tag{2.6}
\]

Here \(y^2/(1-y^2)\) is increasing, so the worst case really is
\(y^2=1/8,\rho=7/8,\kappa=32\).  Equations (2.2)--(2.5) therefore give

\[
\widehat q
<\frac{y^4}{\rho\kappa}
+\frac52y\sqrt{\frac{2\pi}{\rho\kappa}}
\le\frac1{1792}+\frac52D
<\frac1{1792}+\frac{67}{160}
=\frac{3757}{8960}<\frac{17}{40}=:\overline q,
\tag{2.7}
\]

with displacement reserve

\[
\frac{17}{40}-\frac{3757}{8960}=\frac{51}{8960}>0.
\tag{2.8}
\]

Writing \(\mu-x_0=n+\beta\), \(0\le\beta<1\), (2.4) yields

\[
x_0>\mu-(n+1)=\mu(1-\widehat q).
\]

Consequently, before any local outer-region slope is used,

\[
\frac{x_0}{K}>
\rho(1-\widehat q)>
\frac78\left(1-\frac{17}{40}\right)
=\frac{161}{320}=\frac12+\frac1{320}.
\tag{2.9}
\]

In particular \(1-\widehat q>0\), uniformly and strictly, including at
\(y=1/(2\sqrt2)\) and \(\kappa=32\).

## 3. Ordinary-floor plateau and the self-consistency inequality

Let \(u_j=A(x_0+j)+1/4\).  The definition of the first shelf gives
\(\lfloor u_0\rfloor=\lfloor u_p\rfloor=N\).  Since \(A\) is decreasing,

\[
0\le A(x_0)-A(x_0+p)=u_0-u_p<1.
\tag{3.1}
\]

The final inequality is strict even on every ordinary-floor wall: always
\(u_0<N+1\) and \(u_p\ge N\); if either value is integral the conclusion
does not change.

For \(0<z<\mu\), put

\[
\sigma(z)=-A'(z)=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right).
\]

It is increasing.  At \(z=x_0\), set
\(\alpha=\arccos(x_0/K)\) and
\(\beta=\arccos(x_0/\mu)\).  Both lie in \([0,\pi/2)\), and

\[
\cos\beta-\cos\alpha
=\frac{\varepsilon x_0}{\rho K}
< (\alpha-\beta)\sin\alpha.
\]

Thus, in the dangerous branch (where \(p>0\)), (3.1) gives

\[
1>\int_{x_0}^{x_0+p}\sigma(z)\,dz
>\frac{p\varepsilon x_0}
{\pi\rho\sqrt{K^2-x_0^2}}.
\tag{3.2}
\]

Every factor squared here is positive.  Using
\(x_0>\rho K(1-\widehat q)\), squaring (3.2), and dividing only by
positive quantities gives

\[
P^2y^2<
\frac{\pi^2\{1-\rho^2(1-\widehat q)^2\}}
{(1-\widehat q)^2}.
\tag{3.3}
\]

The key exact identity is

\[
\rho(1-\widehat q)=1-y^2Q.
\tag{3.4}
\]

By (2.7), its left side is positive; hence \(0<y^2Q<1\).  Therefore

\[
1-\rho^2(1-\widehat q)^2
=2y^2Q-y^4Q^2<2y^2Q.
\]

Dividing by \(y^2>0\) proves the required strict self-consistency bound

\[
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.}
\tag{3.5}
\]

This proves the sign of every denominator and justifies every squaring in
the argument.

## 4. Actual-to-synthetic comparison and the complete path

Define

\[
S_*(P,r)=\frac{5P-3r}{2},\quad
Q_*(P,r)=1+\frac{y^2}{\kappa}+\frac{yS_*(P,r)}{\kappa},
\quad q_*(P,r)=\frac{y^2}{\rho}(Q_*(P,r)-1),
\]

and

\[
H(P,r)=\frac{2\pi^2Q_*(P,r)}{(1-q_*(P,r))^2}.
\tag{4.1}
\]

From (2.1) and \(d>2/3\),

\[
S=P+\frac{P-r}{d}\le P+\frac32(P-r)=S_*(P,r).
\tag{4.2}
\]

Equality is possible only at the no-drop geometry \(m=0\), where
\(P=r=S\).  For fixed \(a=y^2/\rho\), the function

\[
F(Q)=\frac{2\pi^2Q}{[1-a(Q-1)]^2}
\]

has derivative

\[
F'(Q)=\frac{2\pi^2\{(1-q)+2aQ\}}{(1-q)^3}>0
\quad(q=a(Q-1)<1).
\]

The same shelf calculation as (2.7), using
\(S_*(P,r)\le(5/2)P\), proves \(q_*(P,r)<17/40\).  Hence (3.5) and
(4.2) give the genuine actual-to-synthetic comparison

\[
P^2<H(P,r).
\tag{4.3}
\]

Now set \(B=14/3\) and suppose for contradiction that \(r\ge B\).
Then \(P\ge r\ge B\), and monotonicity in the second argument gives

\[
H(P,r)\le H(P,B).
\tag{4.4}
\]

Every point \((t,B)\), \(B\le t\le P\), is legitimate: \(t\le P\)
preserves the shelf (2.5), while
\(0<S_*(t,B)\le(5/2)t\), so the complete synthetic path retains
\(q_*(t,B)<17/40\) and all denominators remain positive.

Along this path, with \(q=q_*(t,B)\),

\[
\frac{d}{dt}H(t,B)
=\frac{5\pi^2y}{\kappa}
\frac{1+q+2y^2/\rho}{(1-q)^3}.
\tag{4.5}
\]

Here \(y^2/\rho\le1/7\),
\(y/\kappa\le1/(64\sqrt2)<99/8960\), and the right side is increasing
in both \(q\) and \(y^2/\rho\).  Thus

\[
H_t(t,B)<
5\left(\frac{1571}{500}\right)^2\frac{99}{8960}
\frac{1+17/40+2/7}{(23/40)^3}
=\frac{117036972261}{23847320000}<5,
\tag{4.6}
\]

with exact derivative reserve

\[
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0.
\tag{4.7}
\]

Therefore

\[
\frac d{dt}\{t^2-H(t,B)\}>2B-5=\frac{13}{3}.
\tag{4.8}
\]

At \(t=B\), monotonicity in \(y\) and \(1/\kappa\), followed by
\(1/\sqrt2<99/140\), gives

\[
Q_*(B,B)<1+\frac1{256}+\frac7{96}\frac{99}{140}
=\frac{1351}{1280},
\qquad
q_*(B,B)<\frac{71}{8960}.
\]

Consequently

\[
H(B,B)<
2\left(\frac{1571}{500}\right)^2
\frac{1351}{1280}\left(\frac{8960}{8889}\right)^2
=\frac{5228219077088}{246919753125},
\]

and the exact endpoint reserve is

\[
B^2-H(B,B)>
\frac{49714811804}{82306584375}>0.
\tag{4.9}
\]

Equations (4.8)--(4.9) imply \(P^2>H(P,B)\), contradicting
(4.3)--(4.4).  Hence, along the entire domain and including the no-drop
endpoint geometry,

\[
\boxed{r<\frac{14}{3}},
\qquad
\boxed{R<\frac{14}{3\sqrt\varepsilon}}.
\tag{4.10}
\]

## 5. Action payments

The exact action identity and the permitted elementary inequality give

\[
\eta\ge\frac1\pi\int_0^{y^2}\sqrt{2v}\,dv
=\frac{2\sqrt2}{3\pi}y^3.
\]

Using \(\kappa\ge32\) and (1.1),

\[
K\eta\ge\frac{2\sqrt2\kappa}{3\pi y}
>\frac1y\frac{4480000}{466587}.
\tag{5.1}
\]

Also \(1/y\ge2\sqrt2>280/99\), and

\[
\frac{4480000}{466587}-\frac{14}{3}
=\frac{2302594}{466587}>0.
\tag{5.2}
\]

In the dangerous branch, (4.10) and
\(\lfloor x\rfloor>x-1\), valid also at integer \(x\), yield

\[
M=\lfloor K\eta\rfloor-R
>\left(\frac{2302594}{466587}\right)\frac{280}{99}-1.
\]

Since \(8\sqrt2/15<132/175\), the exact dangerous-payment reserve is

\[
\left(\frac{2302594}{466587}\right)\frac{280}{99}-1-\frac{132}{175}
=\frac{98646127309}{8083619775}>0.
\tag{5.3}
\]

If \(R\le0\), including the wall \(R=0\), then
\(M\ge\lfloor K\eta\rfloor\), and the stronger safe reserve is

\[
\frac{4480000}{466587}\frac{280}{99}-1-\frac{132}{175}
=\frac{205339021309}{8083619775}>0.
\tag{5.4}
\]

Thus in every branch

\[
M>\frac{8\sqrt2}{15}>4\delta
\qquad
\left(0\le\delta<\frac{2\sqrt2}{15}\right).
\tag{5.5}
\]

The audited decomposition therefore gives, for every low-interface tail,

\[
\frac{\mathcal T_{r_0}}2
\le\int_{x_0}^K A(z)\,dz+\delta-\frac M4
<\int_{x_0}^K A(z)\,dz.
\tag{5.6}
\]

The proved high-angular theorem owns every tail with \(x_0\ge\mu\).
The weighted scaffold then bounds the complete coarse ordinary-floor proxy
by the Weyl integral.  Finally, the strict phase enclosure and strict
spectral count are no larger than that proxy, including at proxy integers
and eigenfrequency walls.  Hence

\[
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3
\]

for every \(0<\varepsilon\le1/8\) and
\(K\ge32/\varepsilon^2\), including \(\kappa=32\).

## 6. Exceptional branches and analytic walls

All exceptional cases have an explicit owner:

- **Degenerate head \(n=0\):** by definition \(p=m=R=0\); (5.4) pays it.
- **Immediate drop \(p=0\):** \(R=-dm\le0\); it is a safe branch.
- **No drop \(p=n\):** \(m=0\), so \(r=P=S\).  This is precisely the
  endpoint geometry retained in (4.2) and ruled out at \(r\ge B\) by
  (4.9).
- **The wall \(R=0\):** it is paid directly by (5.4); \(R<0\) and
  \(R>0\) have separate proofs, so no continuity inference is used.
- **The first branch with \(R>0\):** it satisfies all strict estimates in
  Sections 2--5; no lower positive size of \(R\) is assumed.
- **\(\mu-x_0\in\mathbb Z\):** here \(\beta=0\), \(q=\mu\), and
  \(\delta=0\).  On the other side \(\beta\to1^-\); only
  \(0\le\beta<1\) and the uniform strict bound for \(\delta\) were used.
- **Low/high interface \(x_0=\mu\):** equality is owned by the proved
  high-angular shifted-tail theorem.  The approach from below has \(n=0\)
  and is covered by the degenerate safe branch.
- **Angular cutoff \(\nu=K\):** strict spectral counting has no active
  channel there; the scaffold sum is over \(\nu<K\).
- **Ordinary-floor and coarse-proxy walls:** (3.1) remains strict at every
  ordinary-floor wall.  If the coarse proxy is integral, the strict phase
  count is still bounded by its ordinary floor.
- **Gain wall \(K\eta\in\mathbb Z\):** the universally strict inequality
  \(\lfloor x\rfloor>x-1\) used in (5.3)--(5.4) remains valid.
- **Spectral walls:** the separated count uses \(n\pi<\Psi(K)\); at
  equality the endpoint mode is excluded.
- **Denominator and squaring walls:** (2.7) gives
  \(1-\widehat q>23/40\), and the same is true for every synthetic path
  point.  All quantities squared in (3.2) are positive.  No zero
  denominator or direction-reversing square occurs.
- **Worst-case reductions:** \(y^2/(1-y^2)\), \(y\sqrt{1-y^2}\) where it
  occurs, \(Q_B\), and \(y^2/\rho\) are increasing on
  \(0<y^2\le1/8\); all relevant expressions decrease with \(\kappa\).
  Thus every stated endpoint reduction really lands at
  \(y^2=1/8,\kappa=32\).  The endpoint reserves remain strict there.
- **Threshold face:** no limit from \(\kappa>32\) was used; all arguments
  hold directly at \(K=32/\varepsilon^2\).

The retained overlap faces are also exact.  Round 10 owns
\(0<\varepsilon\le1/25\) at \(\kappa=20\); Round 13 (and, on its
smaller domain, Round 12) owns \(\varepsilon\le1/10\) at \(\kappa=24\).
Thus \(\varepsilon=1/10\) is owned at \(K=2400\), not merely at
\(K=3200\).  At \(\varepsilon=1/20\) the constant-24 threshold is
\(9600\); at \(\varepsilon=1/25\), Round 10 owns \(K=12500\); and at
\(\varepsilon=1/100\), equivalently \(\rho=99/100\), the proved
all-frequency endpoint owns every \(K\).  At \(\varepsilon=1/8\), the new
theorem owns \(K=2048\).

## 7. Independent central endpoint

At \(\rho=7/8\), the action estimate simplifies to

\[
\eta_{7/8}\ge\frac1{24\pi}>\frac1{76},
\tag{7.1}
\]

because \(\pi<1571/500<19/6\).  Also

\[
a_{7/8}=14\pi<49,
\qquad \sqrt{a_{7/8}}<7,
\qquad
C_0=1+\frac{8\sqrt2}{15}<1+\frac{132}{175}=\frac{307}{175}.
\tag{7.2}
\]

For \(X=550\), exact substitution gives

\[
\frac1{76}X^2-7X-\frac{307}{175}
=\frac{427292}{3325}>0.
\tag{7.3}
\]

The polynomial

\[
f(X)=\eta_{7/8}X^2-\sqrt{a_{7/8}}X-C_0
\]

has one negative and one positive root, since its leading coefficient is
positive and the product of its roots is \(-C_0/\eta_{7/8}<0\).  Its
positive root is exactly

\[
X_+=\frac{\sqrt{a_{7/8}}+
\sqrt{a_{7/8}+4\eta_{7/8}C_0}}{2\eta_{7/8}},
\qquad K_0(7/8)=X_+^2.
\]

Equations (7.1)--(7.3) give \(f(550)>0\), whereas \(f(0)<0\); uniqueness
of the positive root yields

\[
\boxed{K_0(7/8)<550^2}.
\tag{7.4}
\]

The fixed-ratio theorem includes \(K=K_0(7/8)\), and (7.4) puts
\(K=550^2\) strictly inside its proved range.

## 8. Six-zone residual envelope and face ownership

Using the permitted monotonicity of \(K_0(\rho)\), the exact residual
envelope is:

| zone | closed ratio interval | exact analytic owner and possible residual |
|---|---|---|
| 1 | \([\rho_*,1/16]\) | the small-hole inputs leave only \(K<64\) |
| 2 | \([1/16,7/8]\) | fixed-ratio theorem owns every \(K\ge K_0(\rho)\); hence residual \(K<K_0(\rho)\le K_0(7/8)<550^2\) |
| 3 | \([7/8,9/10]\) | the new seam owns \(K\ge32/(1-\rho)^2\); residual \(K<32/(1-\rho)^2\le3200\) |
| 4 | \([9/10,19/20]\) | Round 13 owns \(K\ge24/(1-\rho)^2\); residual \(K<24/(1-\rho)^2\le9600\) |
| 5 | \([19/20,24/25]\) | the retained constant-24 theorem leaves only \(K<15000\) |
| 6 | \([24/25,99/100]\) | Round 10 leaves only \(K<200000\) |
| endpoint | \([99/100,1)\) | the proved all-frequency theorem owns every \(K\) |

The moving face \(K=K_0(\rho)\) in zone 2 is owned at equality by the
fixed-ratio theorem; it is not part of the residual.  At \(\rho=1/16\),
both adjacent analytic constructions apply and the face may be assigned to
zone 2 without a sliver.  At \(\rho=\rho_*\) and \(99/100\), the adjacent
all-frequency endpoint theorems own the face.

The remaining shared faces use the sharper theorem:

- \(\rho=7/8\): the new seam owns \(K=2048\) and above;
- \(\rho=9/10\): Round 13 owns \(K=2400\) and above (hence also the
  coarser \(K=3200\) face);
- \(\rho=19/20\): the constant-24 theorem owns \(K=9600\);
- \(\rho=24/25\): Round 10 owns \(K=12500\) (hence also \(K=15000\));
- \(\rho=99/100\): the all-frequency endpoint owns \(K=200000\) and all
  other energies.

Likewise, \(K=64\) is outside the strict zone-1 residual,
\(K=K_0(7/8)\) is fixed-ratio-owned, and \(K=550^2\) is included.  The
exact ceiling comparison is

\[
64<3200<9600<15000<200000<550^2=302500.
\tag{8.1}
\]

Therefore every \(0<\rho<1\) is analytically covered when
\(K\ge550^2\), including equality.  The exact reduction from the earlier
ceiling is

\[
\frac{900^2}{550^2}=\frac{324}{121}>2
\quad\left(\frac{324}{121}-2=\frac{82}{121}\right).
\tag{8.2}
\]

This is only the claimed high-frequency analytic cover.  It neither
enlarges the complete all-frequency endpoint beyond \([99/100,1)\) nor
closes the compact residual below \(550^2\).

## 9. Key exact reserves

The decisive reserves, all strictly positive, are

\[
\frac1{64},\quad
\frac3{1120000},\quad
\frac{51}{8960},\quad
\frac{2199627739}{23847320000},\quad
\frac{49714811804}{82306584375},
\]

\[
\frac{98646127309}{8083619775},\qquad
\frac{205339021309}{8083619775},\qquad
\frac{427292}{3325}.
\]

No sampled sign, floating-point optimization, or finite parameter sweep is
used anywhere in this inventory.
