# Round 15 central--thin seam: strictly isolated clean-room review

## Verdict

**PASS.**

The sole input read was the frozen lemma packet
\( \text{state/lemma_packets/SHELL-central-thin-seam-compression-round15.md} \).
Its SHA-256 digest was independently checked before reading and was

\[
\texttt{c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7}.
\]

I first tried to break the claim at the threshold
\((y^2,\kappa)=(1/6,54)\), at the first positive-\(R\) cell, at a
\(\beta\)-jump, and on the no-drop branch.  The possible failure point is
the implication from an ordinary-floor plateau to the cap on \(R\).
It does close: a direct cosine-gap estimate gives the *actual* strict
self-consistency inequality, after which a complete fixed-\(r=B\) path
rules out \(r\ge B\).  The floor payment then closes separately for
\(R>0\) and \(R\le0\).  I also reconstructed the fixed-ratio endpoint
without using the seam claim.

**First unsupported implication:** none.

The verdict is for the two frozen analytic claims and the prospective
union conditional on the accepted inputs in the packet.  It does not
replace the further adversarial and promotion gates required by the
packet.

## 1. Exact elementary bracket used below

No decimal approximation is needed.  Machin's identity and alternating
arctangent bounds give a convenient self-contained rational bracket.  Put
\(x=1/5\), \(z=1/239\), and

\[
\begin{aligned}
 U_5&=x-\frac{x^3}{3}+\frac{x^5}{5},&
 L_5&=U_5-\frac{x^7}{7},\\
 L_{239}&=z-\frac{z^3}{3},&
 U_{239}&=L_{239}+\frac{z^5}{5}.
\end{aligned}
\]

Since
\(\pi/4=4\arctan(1/5)-\arctan(1/239)\), the alternating remainders have
the displayed signs and

\[
L_\pi:=16L_5-4U_{239}<\pi<
16U_5-4L_{239}=:U_\pi.
\]

Direct integer arithmetic gives

\[
\frac{1571}{500}-U_\pi
=\frac{323354809}{853244937500}>0,
\]

\[
L_\pi-\frac{333}{106}
=\frac{3722073235309511}{45204684279504531250}>0.
\]

Thus, in particular,

\[
\frac{333}{106}<\pi<\frac{1571}{500}.
\tag{1.1}
\]

I will also use only the following squared rational comparisons:

\[
\sqrt2>\frac75,\qquad
\sqrt2>\frac{140}{99},\qquad
\sqrt2<\frac{99}{70},
\tag{1.2}
\]

because their respective reserves are
\(1/25\), \(2/9801\), and \(1/4900\), and

\[
\frac{265}{153}<\sqrt3<\frac{97}{56},
\tag{1.3}
\]

whose squared reserves are \(2/23409\) and \(1/3136\).

## 2. Angular bound, shelf bound, and pre-slope localization

Let \(t=y^2=\varepsilon\), so \(0<t\le1/6\),
\(\rho=1-t\), and \(\kappa\ge54\).

First,

\[
2-\left(\frac75\right)^2=\frac1{25},\qquad
\left(\frac79\right)^2-\frac35=\frac2{405}.
\]

Consequently
\(\sqrt{2-\sqrt2}<7/9\), whence

\[
\cos\frac{3\pi}{8}
=\frac12\sqrt{2-\sqrt2}<\frac7{18}
\]

and

\[
\cos^2\frac{3\pi}{16}
=\frac{1+\cos(3\pi/8)}2<\frac{25}{36}.
\]

All quantities are positive, so
\(\cos(3\pi/16)<5/6\).  Since \(\rho\ge5/6\),

\[
c=\frac{\arccos\rho}{\pi}<\frac3{16},
\qquad
d=1-2c>\frac58.
\tag{2.1}
\]

This remains strict at \(t=1/6\).

From (1.1),

\[
\left(\frac{13}{5}\right)^2
-2\frac{1571}{500}=\frac{119}{250}>0.
\]

Because \(0<\rho<1\), input (P3) therefore gives

\[
p<\frac{13}{5}\sqrt{\frac Kt}.
\tag{2.2}
\]

Now consider the only new branch, \(R>0\).  Then \(r>0\),
\(0\le r\le P\), and (D7), (2.1) imply

\[
S=P+\frac{P-r}{d}
\le P+\frac85(P-r)=S_*(P,r)
<\frac{13}{5}P.
\tag{2.3}
\]

The last inequality is strict because \(r>0\).  The same weak upper
bound applies to \(S_*\) itself.  Moreover,

\[
Q-1=\frac{(n+1)t}{\kappa}
=\frac{n+1}{Kt},
\qquad
\widehat q=\frac{n+1}{\rho K}.
\tag{2.4}
\]

Using (2.2) in the definition of \(q_*\), we get, before using any
outer-slope estimate,

\[
\widehat q\le q_*
<\frac{t^2}{\rho\kappa}
+\frac{13}{5}
\sqrt{\frac{2\pi t}{\rho\kappa}}.
\tag{2.5}
\]

Both terms on the right increase with \(t\) and decrease with
\(\kappa\): this follows directly from the increase of
\(t/(1-t)\) and \(t^2/(1-t)\).  Hence their worst case is
\((t,\rho,\kappa)=(1/6,5/6,54)\).  At that point the first term is
\(1/1620\), while (1.1) and

\[
\left(\frac{763}{5000}\right)^2-\frac{1571}{67500}
=\frac{8563}{675000000}>0
\]

show that the radical is \(<763/5000\).  Thus

\[
\widehat q\le q_*<
\frac1{1620}+\frac{13}{5}\frac{763}{5000}
=\frac{804689}{2025000}
<\frac{159}{400},
\tag{2.6}
\]

where the final exact reserve is \(497/4050000\).
In particular, every denominator \(1-\widehat q\) and \(1-q_*\)
used below is positive.

Since \(x_0=\mu-(n+\beta)\), \(0\le\beta<1\), and (2.4) holds,

\[
\frac{x_0}{\mu}
=1-\frac{n+\beta}{\mu}
>1-\widehat q.
\]

Therefore (2.6) localizes the whole dangerous branch strictly before
the outer slope:

\[
\frac{x_0}{K}>
\frac56\left(1-\frac{159}{400}\right)
=\frac{241}{480}
=\frac12+\frac1{480}.
\tag{2.7}
\]

This argument uses only \(0\le\beta<1\); it is unchanged at
\(\beta=0\) and as \(\beta\to1^{-}\).

## 3. Ordinary-floor plateau implies strict self-consistency

In the branch \(R>0\), one necessarily has \(p\ge1\): if \(p=0\),
then \(R=-dm\le0\).  Hence \(n\ge1\), and the plateau definition gives
\(h_0=h_p\).  Since \(A\) is decreasing on \([x_0,\mu]\), equality of
the two ordinary floors, including when either argument lies on an
integer wall, gives the strict width-one statement

\[
A(x_0)-A(x_0+p)<1.
\tag{3.1}
\]

For \(0<z<\mu\), put

\[
\Delta(z)=\arccos\frac zK-\arccos\frac z\mu.
\]

Then

\[
A(x_0)-A(x_0+p)
=\frac1\pi\int_{x_0}^{x_0+p}\Delta(z)\,dz,
\tag{3.2}
\]

with the endpoint \(z=\mu\) allowed by continuity.  Also

\[
\Delta'(z)
=\frac1{\sqrt{\mu^2-z^2}}
-\frac1{\sqrt{K^2-z^2}}>0.
\tag{3.3}
\]

Let
\(\alpha=\arccos(x_0/K)\) and
\(\gamma=\arccos(x_0/\mu)\).  By (2.7),
\(0\le\gamma<\alpha<\pi/2\).  The cosine difference gives

\[
\frac{t x_0}{\mu}
=\cos\gamma-\cos\alpha
=\int_\gamma^\alpha\sin u\,du
<(\alpha-\gamma)\sin\alpha.
\tag{3.4}
\]

On the other hand,

\[
1-\frac{x_0}{K}
=t+\frac{n+\beta}{K}
<t+\frac{n+1}{K}=tQ,
\]

so

\[
0<\sin\alpha
<\sqrt{2tQ}.
\tag{3.5}
\]

Combining (2.4), (3.4), and (3.5) yields the direct, strict angular
gap

\[
\Delta(x_0)>
\frac{y(1-\widehat q)}{\sqrt{2Q}}.
\tag{3.6}
\]

Equations (3.1)--(3.3) now imply

\[
1>
\frac{p\,y(1-\widehat q)}{\pi\sqrt{2Q}}
=\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
\]

Every factor being squared is positive, and therefore

\[
P^2<
\frac{2\pi^2Q}{(1-\widehat q)^2}.
\tag{3.7}
\]

By (2.3), \(Q\le Q_*\) and
\(\widehat q\le q_*<159/400\).  The function

\[
u\longmapsto
\frac{u}{[1-a(u-1)]^2}
\]

has positive derivative wherever the displayed denominator is
positive.  Hence (3.7) proves the required actual-to-synthetic
implication

\[
P^2<H(P,r).
\tag{3.8}
\]

This is the strict implication that would have failed first had an
ordinary-floor wall, a sign, or the pre-slope localization been lost.

## 4. The complete synthetic path and the cap on \(R\)

Set \(B=14/3\).  Suppose for contradiction that \(r\ge B\).  Then
\(P\ge r\ge B\).  For fixed \(P\), \(Q_*\) decreases with \(r\), and
the preceding monotonicity in \(Q_*\) shows

\[
H(P,r)\le H(P,B).
\tag{4.1}
\]

It remains to control every point of the path
\(\{(P',B):B\le P'\le P\}\), not merely its initial endpoint.
The shelf bound for the actual \(P\) also bounds every \(P'\le P\),
so the proof of (2.6) gives \(q_*(P',B)<159/400\) throughout this
path.

We have

\[
a=\frac{t}{1-t}\le\frac15,
\qquad
\frac{\partial Q_*}{\partial P}
=\frac{13y}{5\kappa}
<\frac{637}{32400}.
\tag{4.2}
\]

Indeed

\[
\left(\frac{49}{120}\right)^2-\frac16
=\frac1{14400}>0,
\]

so \(y<49/120\), and (4.2) follows from \(\kappa\ge54\).
Writing \(q=a(Q_*-1)\), direct differentiation gives

\[
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q_*}{\partial P}
\frac{1+q+2a}{(1-q)^3}.
\tag{4.3}
\]

Using (1.1), (2.6), and (4.2) at every intermediate point,

\[
\frac{\partial H}{\partial P}
<
2\left(\frac{1571}{500}\right)^2
\frac{637}{32400}
\frac{1+159/400+2/5}{(1-159/400)^3}
=\frac{2260740364246}{708624500625}
<\frac{16}{5}.
\tag{4.4}
\]

The reserve in the last comparison is

\[
\frac{6858037754}{708624500625}>0.
\]

At the initial point \(P=r=B\), \(S_*=B\), so

\[
Q_*(B,B)
=1+\frac{t+By}{\kappa}
<1+\frac{1/6+(14/3)(49/120)}{54}
=\frac{10093}{9720},
\tag{4.5}
\]

and

\[
q_*(B,B)<\frac{373}{48600}.
\tag{4.6}
\]

Consequently

\[
\begin{aligned}
B^2-H(B,B)
&>
B^2-
2\left(\frac{1571}{500}\right)^2
\frac{10093/9720}{(1-373/48600)^2}\\
&=
\frac{2505132463469}{2616573970125}>0.
\end{aligned}
\tag{4.7}
\]

For \(F(P')=(P')^2-H(P',B)\), (4.4) gives on the *complete*
path

\[
F'(P')>2B-\frac{16}{5}
=\frac{92}{15}>0.
\tag{4.8}
\]

Thus (4.7) implies \(F(P)>0\).  Together with (4.1), this contradicts
(3.8).  Hence

\[
r<B,\qquad R<\frac{B}{y}
\quad\text{whenever }R>0.
\tag{4.9}
\]

All radicands on this route are positive by construction, all
denominators are bounded below by \(1-159/400\), and the only squaring
in (3.7) is between positive quantities.

## 5. Action gain, full floor payment, and (T1)

From (P4) and the permitted bound
\(\arccos(1-v)\ge\sqrt{2v}\),

\[
\eta\ge\frac{2\sqrt2}{3\pi}y^3.
\]

Therefore

\[
K\eta\ge
\frac{2\sqrt2\kappa}{3\pi}\frac1y
\ge\frac{36\sqrt2}{\pi}\frac1y
>\frac{280000}{17281}\frac1y.
\tag{5.1}
\]

The last strict inequality follows from
\(\sqrt2>140/99\), \(\pi<1571/500\), and the exact identity

\[
\frac{36(140/99)}{1571/500}
=\frac{280000}{17281}.
\]

Also

\[
\frac{280000}{17281}-B
=\frac{598066}{51843}>0,
\qquad
\frac1y>\frac{120}{49}.
\tag{5.2}
\]

On the dangerous branch, (4.9), the universal strict floor inequality
\(\lfloor x\rfloor>x-1\), and (5.1)--(5.2) give

\[
\begin{aligned}
M&=\lfloor K\eta\rfloor-R\\
&>K\eta-1-\frac{B}{y}\\
&>
\left(\frac{280000}{17281}-B\right)\frac1y-1
>\frac{132}{175}.
\end{aligned}
\tag{5.3}
\]

The final exact reserve is

\[
\left(\frac{280000}{17281}-B\right)
\frac{120}{49}-1-\frac{132}{175}
=\frac{80132733}{3024175}>0.
\]

On the safe branch \(R\le0\),

\[
M\ge\lfloor K\eta\rfloor
>K\eta-1>\frac{132}{175},
\tag{5.4}
\]

with the larger reserve

\[
\frac{280000}{17281}\frac{120}{49}
-1-\frac{132}{175}
=\frac{114694733}{3024175}>0.
\]

Finally, \(\sqrt2<99/70\) gives

\[
\delta<\frac{2\sqrt2}{15}
<\frac{33}{175}
<\frac M4.
\tag{5.5}
\]

Substitution in (P1) proves, for every low interface to which (P1)
applies,

\[
\frac{\mathcal T_{r_0}}2
<
\int_{x_0}^{K}A(z)\,dz.
\tag{5.6}
\]

The accepted weighted-lattice scaffold and accepted high-angular
shifted-tail statement apply (5.6) exactly at the remaining
interfaces.  The accepted exact separated spectrum,
strict-counting convention, and ordinary-floor transfer then give

\[
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3.
\]

Nothing in the argument uses \(\kappa>54\); the rational reserves
remain strict at \(\kappa=54\), so the equality face
\(K=54/\varepsilon^2\) is included.  This proves (T1).

### Branch and discontinuity ownership

The proof above covers all combinatorial branches without a limiting
argument:

* \(n=0\) has \(p=m=R=0\) and is covered by the safe payment (5.4).
* \(p=0\) has \(R=-dm\le0\), including the immediate-drop branch.
* \(R=0\) is assigned to (5.4).  The open side \(R>0\) is covered by
  (3.1)--(5.3), so both sides of the wall are owned.
* If \(p=n\), then \(m=0\) and \(R=p\).  The case \(p=0\) is the
  degenerate head; if \(p>0\), the same ordinary-floor equality
  \(h_0=h_p\) gives (3.1), so the no-drop branch is included in the
  dangerous proof.
* Every first \(R>0\) cell has \(p\ge1\), which is exactly the
  hypothesis used in Section 3.
* At \(\mu-x_0\in\mathbb Z\), one has \(\beta=0\) and \(q=\mu\).
  The proof uses \(0\le\beta<1\) and remains strict at \(\beta=0\);
  the adjacent cell is covered uniformly as \(\beta\to1^{-}\).
  The case \(x_0=\mu\) is precisely \(n=0\).
* Equality on any wall of
  \(\lfloor A(x_0+j)+1/4\rfloor\) preserves (3.1), because two
  numbers in the same half-open unit cell differ by strictly less
  than one.  Equality on \(K\eta\in\mathbb Z\) preserves
  \(\lfloor K\eta\rfloor>K\eta-1\).
* The angular cutoff \(\nu=K\) is owned by the accepted strict
  spectral/shifted-tail convention and by the stipulated zero
  extension of \(G_a\).  No division or square root is taken there.

Thus no branch is silently transferred through a floor wall.

## 6. Independent endpoint \(K_0(5/6)<295^2\)

This section does not use (T1), (4.9), or any seam estimate.
At \(\rho=5/6\),

\[
a_\rho=10\pi<\frac{220}{7}<36.
\tag{6.1}
\]

Indeed (1.1) gives
\(10\pi<1571/50<220/7\), with reserve \(3/350\), and
\(36-220/7=32/7\).  Hence \(\sqrt{a_\rho}<6\).

At this ratio, (P4) gives

\[
\eta_{5/6}
\ge
\frac{2\sqrt2}{3\pi}\left(\frac16\right)^{3/2}
=\frac1{9\pi\sqrt3}.
\tag{6.2}
\]

Now

\[
\left(\frac{97}{56}\right)^2-3=\frac1{3136},
\]

and

\[
49-9\left(\frac{1571}{500}\right)
\left(\frac{97}{56}\right)
=\frac{517}{28000}>0.
\tag{6.3}
\]

Equations (1.1), (6.2), and (6.3) prove
\(\eta_{5/6}>1/49\).  Also (1.2) yields

\[
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
\tag{6.4}
\]

For

\[
f(X)=\eta_{5/6}X^2-\sqrt{a_{5/6}}X-C_0
\]

we therefore have

\[
f(295)>
\frac{295^2}{49}-6(295)-\frac{307}{175}
=\frac{5226}{1225}>0.
\tag{6.5}
\]

Because \(\eta_{5/6}>0\), \(C_0>0\), the two roots of \(f\) have
opposite signs.  Its unique positive root is exactly the square-root
quantity in (P5).  Since \(295>0\) and (6.5) is strict, that root is
strictly below \(295\).  Squaring positive quantities proves

\[
K_0(5/6)<295^2=87025.
\]

This proves (T3) independently.

## 7. Overlaps, closed faces, and the prospective union

For completeness, the first low-ratio coarse bound can also be
reconstructed directly from (P5).  On \(\rho\le1/2\),
\(\eta_\rho=\omega_0\) is constant and \(a_\rho\) increases with
\(\rho\), so the positive root in (P5) increases with \(\rho\).
The exact proxies

\[
\omega_0>
\frac{265/153}{2(1571/500)}-\frac16
=\frac{52379}{480726},
\]

\[
\sqrt{a_{1/16}}
=\sqrt{\frac{2\pi}{15}}<\frac{13}{20},
\qquad
\left(\frac{13}{20}\right)^2
-\frac{2(1571/500)}{15}=\frac{107}{30000},
\]

and (6.4) give

\[
64\omega_0-8\sqrt{a_{1/16}}-C_0
>
\frac{800629}{42063525}>0.
\]

Hence \(K_0(\rho)<64\) on
\([\rho_*,1/16]\).  The interval ordering is also strict:
\(\omega_0<1/8\) follows from

\[
\frac7{24}
-\frac{97/56}{2(333/106)}
=\frac{149}{9324}>0,
\]

while \(1+2C_*=2C_0>2\); thus
\(0<\rho_*<1/16\).

On \([1/16,5/6]\), the accepted monotonicity of \(K_0\), together
with (T3), gives the second coarse enclosure.  The seam theorems then
give exactly the seven closed coarse residual zones stated in the
packet:

\[
\begin{array}{c|c}
\text{ratio zone}&\text{coarse residual upper bound}\\ \hline
[\rho_*,1/16]&64\\
[1/16,5/6]&K_0(5/6)<87025\\
[5/6,7/8]&54/(1-\rho)^2\le3456\\
[7/8,9/10]&32/(1-\rho)^2\le3200\\
[9/10,19/20]&24/(1-\rho)^2\le9600\\
[19/20,24/25]&24/(1-\rho)^2\le15000\\
[24/25,99/100]&20/(1-\rho)^2\le200000.
\end{array}
\]

These are enclosures of the exact complement, not rectangular
certificates.  Shared ratio faces are assigned to the sharper accepted
theorem as follows:

\[
\begin{array}{c|c|c}
\rho&\text{sharp owner on the face}&\text{included threshold}\\ \hline
\rho_*&(A1)&\text{all }K\\
1/16&\text{fixed-ratio theorem}&K_0(1/16)<64\\
5/6&(T1)&54(6^2)=1944\\
7/8&(A2)&32(8^2)=2048\\
9/10&(A3)&24(10^2)=2400\\
19/20&(A3)&24(20^2)=9600\\
24/25&(A4)&20(25^2)=12500\\
99/100&(A1)&\text{all }K.
\end{array}
\]

Thus the prescribed overlap order is respected:
(A4) on \(0<\varepsilon\le1/25\), then (A3) through
\(\varepsilon=1/10\), then (A2) through \(\varepsilon=1/8\), and
only then (T1) on the genuinely new
\(1/8<\varepsilon\le1/6\).  In particular,
\(\varepsilon=1/100,1/25,1/20,1/10,1/8,1/6\) and
\(\kappa=20,24,32,54\) are all closed and used only on their stated
domains.

The listed energy faces are also owned:

* \(K=54/\varepsilon^2\), and hence \(K=1944\) at \(5/6\), is
  included by (T1).
* \(K=2048,2400,9600,12500\) are the included sharp seam faces in
  the preceding table.
* \(K=3200,3456,15000\) are coarse-zone maxima; where a sharper
  theorem overlaps, respectively (A3), (A2), and (A4) owns the face.
* \(K=64\) is included on the low-ratio side because
  \(K_0<64\); elsewhere the exact fixed-ratio comparison partitions
  the face into analytic cover and residual without a gap.
* \(K=K_0(5/6)\) is included by the \(K\ge K_0\) convention, and
  \(K=295^2=87025\) is included because (T3) is strict.
  The proxy at \(K=294^2\) does not decide whether that energy is
  above \(K_0(\rho)\) at every central ratio: it is covered exactly
  where \(294^2\ge K_0(\rho)\) and otherwise remains in the exact
  residual.  At \(\rho=5/6\) it is in any case covered by (T1).
  No claim \(K_0(5/6)<294^2\) is made.
* \(K=200000\) is included in every zone, with equality in (A4) at
  \(\rho=99/100\).  The already accepted all-frequency endpoint owns
  that ratio and everything to its right.

It follows that the prospective all-ratio high-frequency ceiling is
\(K\ge200000\), and

\[
\frac{550^2}{200000}=\frac{121}{80}>1.
\]

The all-frequency endpoint remains exactly \([99/100,1)\): no step
above gives all-frequency coverage at a smaller ratio.  The exact
nonrectangular compact residual remains open.

## 8. Deliberate obstruction checks

The same exact bracket (1.1) confirms that the selected displacement
route does **not** close at \(\kappa=53\).  Namely,

\[
\frac{333}{14045}
-\left(\frac{3079}{20000}\right)^2
=\frac{10003031}{1123600000000}>0,
\]

so

\[
\sqrt{\frac{2\pi}{265}}>\frac{3079}{20000},
\]

and at the endpoint

\[
\frac1{1590}+\frac{13}{5}\frac{3079}{20000}
-\frac25
=\frac{14293}{15900000}>0.
\]

This falsifies only that attempted \(\kappa=53\) localization, not the
shell inequality at \(53\).  Likewise the selected endpoint proxies
at \(Y=294\) give only

\[
\frac{294^2}{49}-6(294)-\frac{307}{175}
=-\frac{307}{175}<0;
\]

they neither lower-bound \(K_0(5/6)\) by \(294^2\) nor give a spectral
counterexample.

## 9. Executable exact ledger

The following standalone Python fragment uses only integer rational
arithmetic and reproduces every finite comparison on which the proof
depends.

    from fractions import Fraction as F

    x, z = F(1, 5), F(1, 239)
    U5 = x - x**3 / 3 + x**5 / 5
    L5 = U5 - x**7 / 7
    L239 = z - z**3 / 3
    U239 = L239 + z**5 / 5
    Upi = 16 * U5 - 4 * L239
    Lpi = 16 * L5 - 4 * U239
    assert F(1571, 500) - Upi == F(323354809, 853244937500)
    assert Lpi - F(333, 106) == F(
        3722073235309511, 45204684279504531250
    )

    assert 2 - F(7, 5)**2 == F(1, 25)
    assert F(7, 9)**2 - F(3, 5) == F(2, 405)
    assert 2 - F(140, 99)**2 == F(2, 9801)
    assert F(99, 70)**2 - 2 == F(1, 4900)
    assert 3 - F(265, 153)**2 == F(2, 23409)
    assert F(97, 56)**2 - 3 == F(1, 3136)
    assert F(13, 5)**2 - 2 * F(1571, 500) == F(119, 250)

    assert F(763, 5000)**2 - F(1571, 67500) == F(
        8563, 675000000
    )
    q0 = F(1, 1620) + F(13, 5) * F(763, 5000)
    assert q0 == F(804689, 2025000)
    assert F(159, 400) - q0 == F(497, 4050000)

    assert F(49, 120)**2 - F(1, 6) == F(1, 14400)
    assert 6 - F(120, 49)**2 == F(6, 2401)
    D = (
        2 * F(1571, 500)**2
        * F(637, 32400)
        * (1 + F(159, 400) + F(2, 5))
        / (1 - F(159, 400))**3
    )
    assert D == F(2260740364246, 708624500625)
    assert F(16, 5) - D == F(6858037754, 708624500625)

    B = F(14, 3)
    F0 = (
        B**2
        - 2 * F(1571, 500)**2
        * F(10093, 9720)
        / (1 - F(373, 48600))**2
    )
    assert F0 == F(2505132463469, 2616573970125)
    assert 2 * B - F(16, 5) == F(92, 15)

    gain = F(280000, 17281)
    assert 36 * F(140, 99) / F(1571, 500) == gain
    assert gain - B == F(598066, 51843)
    assert (
        (gain - B) * F(120, 49) - 1 - F(132, 175)
        == F(80132733, 3024175)
    )
    assert (
        gain * F(120, 49) - 1 - F(132, 175)
        == F(114694733, 3024175)
    )

    assert F(220, 7) - F(1571, 50) == F(3, 350)
    assert 36 - F(220, 7) == F(32, 7)
    assert (
        49 - 9 * F(1571, 500) * F(97, 56)
        == F(517, 28000)
    )
    assert (
        F(295**2, 49) - 6 * 295 - F(307, 175)
        == F(5226, 1225)
    )

    omega_L = F(265, 153) / (2 * F(1571, 500)) - F(1, 6)
    assert omega_L == F(52379, 480726)
    assert (
        F(13, 20)**2 - 2 * F(1571, 500) / 15
        == F(107, 30000)
    )
    assert (
        64 * omega_L - 8 * F(13, 20) - F(307, 175)
        == F(800629, 42063525)
    )
    assert (
        F(7, 24) - F(97, 56) / (2 * F(333, 106))
        == F(149, 9324)
    )

    assert (
        F(333, 14045) - F(3079, 20000)**2
        == F(10003031, 1123600000000)
    )
    assert (
        F(1, 1590) + F(13, 5) * F(3079, 20000) - F(2, 5)
        == F(14293, 15900000)
    )
    assert (
        F(294**2, 49) - 6 * 294 - F(307, 175)
        == -F(307, 175)
    )

    assert 54 * 6**2 == 1944
    assert 32 * 8**2 == 2048
    assert 24 * 10**2 == 2400
    assert 32 * 10**2 == 3200
    assert 54 * 8**2 == 3456
    assert 24 * 20**2 == 9600
    assert 20 * 25**2 == 12500
    assert 24 * 25**2 == 15000
    assert 20 * 100**2 == 200000
    assert F(550**2, 200000) == F(121, 80)
