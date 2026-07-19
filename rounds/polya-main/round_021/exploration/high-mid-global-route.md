# Round 21 exploration: aggregate product closure in the high--mid residual

Status: **PASS on a major face-connected sub-band; exploratory only; not
frozen or promoted**.

Date: 2026-07-15.

This note starts from the prospective residual

\[
 \mathcal D_{21}^{\mathrm{mid}}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac{39}{50},
 \quad k_{11}(\rho)<K<K_0(\rho)\right\}.
 \tag{1}
\]

It does not add another Bessel-zero staircase wall. Instead it aggregates
all radial and angular product modes at once and retains a favorable term
in the exact shell Weyl normalization that the earlier all-frequency
optical screen deliberately discarded.

The resulting analytic theorem is

\[
 \boxed{
 \frac{13}{20}\leq\rho<1,
 \qquad
 0\leq K\leq V(\rho):=
 \frac{9}{5(1-\rho)^2}}
 \quad\Longrightarrow\quad
 \boxed{
 N_D(A_{\rho,1},K^2)
 \leq\frac{2}{9\pi}(1-\rho^3)K^3.}
 \tag{2}
\]

For \(K>0\), the comparison in (2) is strict. Its exact new contribution
to (1) is the face-connected band

\[
 \boxed{
 \mathcal C_{21}^{\mathrm{prod}}
 =\left\{(\rho,K):
 \frac{13}{20}\leq\rho<\frac{39}{50},
 \quad k_{11}(\rho)<K\leq V(\rho)\right\}.}
 \tag{3}
\]

## 1. Provenance boundary

No new external source, zero table, or numerical root approximation is
used.

| input | SHA-256 | exact use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/high-optical-optimization.md` | `6e6eb668cb284ede7ab6662b772af9004158d8d7098a83d549786823804ddc16` | strict product comparison, exact product deficit, and optical scaling |
| `rounds/polya-main/round_020/exploration/high-optical-adversarial-audit.md` | `d7a92ae46d9e64cc9834e630f2db2dad16785552e66535c81b1ef7b5fd1c8b2a` | independent reconstruction and PASS verdict for those inputs |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` | product min--max comparison and strict angular/radial walls |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated shell spectrum and multiplicity \(2\ell+1\) |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` | formula and accepted ownership of the upper face \(K=K_0(\rho)\) |
| `rounds/polya-main/round_020/exploration/high-k11-extension.md` | `9faa7b75bb5b55cde24f63c613d03eb625457c9f99df03ad9a8bb563c9c22be1` | prospective lower residual face \(K=k_{11}\), used only in the subtraction |

The proof of (2) uses only the first four rows. The final two rows are used
only to identify the exact portion of the prospective residual removed by
the theorem.

## 2. Scaling and the aggregate product count

Put

\[
 \varepsilon=1-\rho,
 \qquad
 0<\varepsilon\leq\varepsilon_0:=\frac7{20},
 \qquad
 a=\varepsilon K,
 \qquad
 c:=\frac95.
 \tag{4}
\]

The frequency condition in (2) is exactly

\[
 0\leq a\leq\frac{c}{\varepsilon}.
 \tag{5}
\]

At the largest permitted width,

\[
 \frac{c}{\varepsilon_0}=\frac{36}{7}>\pi,
 \tag{6}
\]

so the nonzero radial cells are genuinely present; this is not a disguised
zero-count lemma.

The product min--max comparison replaces the shell angular potential
\(\ell(\ell+1)/r^2\) by the smaller constant
\(\ell(\ell+1)\). Its strict product count will be denoted by
\(\mathcal P_\varepsilon(a)\). For each strict radial index
\(n\pi<a\), set

\[
 b_n^2=a^2-n^2\pi^2.
\]

All angular modes satisfying

\[
 \varepsilon^2\ell(\ell+1)<b_n^2
\]

are included with their complete multiplicity \(2\ell+1\). Thus the
comparison is already a two-dimensional radial/angular lattice aggregate,
not a mode-by-mode shell-zero estimate.

Define

\[
 S_0(a)=\sum_{n\pi<a}(a^2-n^2\pi^2),
 \qquad
 I_0(a)=\frac{2a^3}{3\pi},
 \qquad
 D(a)=I_0(a)-S_0(a).
 \tag{7}
\]

The audited strict angular ceiling gives

\[
 \boxed{
 \varepsilon^2\mathcal P_\varepsilon(a)
 <S_0(a)+\frac{\varepsilon a^2}{4}
 +\frac{\varepsilon^2a}{\pi}.}
 \tag{8}
\]

The product min--max comparison gives

\[
 N_D(A_{\rho,1},K^2)\leq\mathcal P_\varepsilon(a).
 \tag{9}
\]

Every equality in the radial condition \(n\pi<a\) or angular condition
above is excluded under the strict count.

## 3. Exact deficit and the term retained here

For \(a>\pi\), use the unique strict-cell representation

\[
 \frac a\pi=N+t,
 \qquad N\geq1,
 \qquad0<t\leq1,
 \tag{10}
\]

with \((N,t)=(m-1,1)\) at \(a=m\pi\). The audited exact identity is

\[
 \frac{D(a)}{\pi^2}
 =\frac{N^2}{2}
 +N\left(t^2+\frac16\right)
 +\frac{2t^3}{3}.
 \tag{11}
\]

It implies the uniform strict bound

\[
 \boxed{
 D(a)>C_Da^2,
 \qquad
 C_D:=\frac{1382}{3125}.}
 \tag{12}
\]

The exact shell Weyl normalization is

\[
 \frac{2}{9\pi}(1-\rho^3)K^3
 =\frac1{\varepsilon^2}I_0(a)
 \left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
 \tag{13}
\]

Combining (8) with (13), the exact sufficient condition is

\[
 D(a)>
 \varepsilon\left(1-\frac{\varepsilon}{3}\right)I_0(a)
 +\frac{\varepsilon a^2}{4}
 +\frac{\varepsilon^2a}{\pi}.
 \tag{14}
\]

The earlier all-frequency low screen used the stronger condition obtained
by replacing \(1-\varepsilon/3\) with \(1\). Retaining the favorable
\(-\varepsilon^2I_0/3\) term is the sole new analytic step in this note.

## 4. Exact closure of the full low-optical band

Write

\[
 q:=\frac{106}{333},
 \qquad
 \frac1\pi<q.
 \tag{15}
\]

For \(\pi<a\leq c/\varepsilon\), division of the right side of (14) by
\(a^2\) gives

\[
 \frac{2\varepsilon a}{3\pi}
 \left(1-\frac{\varepsilon}{3}\right)
 +\frac{\varepsilon}{4}
 +\frac{\varepsilon^2}{\pi a}
 <\frac{2cq}{3}
 \left(1-\frac{\varepsilon}{3}\right)
 +\frac{\varepsilon}{4}
 +\varepsilon^2q^2.
 \tag{16}
\]

Define the refined low-screen reserve

\[
 R(\varepsilon)
 :=C_D-\frac{2cq}{3}
 \left(1-\frac{\varepsilon}{3}\right)
 -\frac{\varepsilon}{4}-\varepsilon^2q^2.
 \tag{17}
\]

Its derivative is strictly negative on the whole domain, because

\[
 \frac14-\frac{2cq}{9}
 =\frac{817}{6660}>0,
 \qquad
 R'(\varepsilon)
 =\frac{2cq}{9}-\frac14-2\varepsilon q^2<0.
 \tag{18}
\]

It is therefore enough to evaluate the largest width. Exact arithmetic
gives

\[
\begin{aligned}
 R\left(\frac7{20}\right)
 &={1382\over3125}
 -{2\over3}{9\over5}{106\over333}
  \left(1-{7\over60}\right)
 -{7\over80}
 -{49\over400}\left({106\over333}\right)^2\\
 &=\frac{27223693}{5544450000}>0.
\end{aligned}
 \tag{19}
\]

Equations (12), (16), and (19) prove (14), hence the strict comparison in
(2), for every \(\pi<a\leq c/\varepsilon\). For
\(0\leq a\leq\pi\), the strict product radial count is zero, including
the face \(a=\pi\). This proves (2) on its complete stated frequency
interval.

## 5. The new band is nonempty and lies inside the live residual

On the requested ratio strip,

\[
 \frac{13}{20}\leq\rho<\frac{39}{50}
 \quad\Longleftrightarrow\quad
 \frac{11}{50}<\varepsilon\leq\frac7{20}.
 \tag{20}
\]

The inequality \(k_{11}<V\) is equivalent to

\[
 c^2>\varepsilon^2
 \left(\pi^2+132\varepsilon^2\right).
 \tag{21}
\]

The right side increases with \(\varepsilon\). At the worst face,
\(\pi<22/7\) gives the strict reserve

\[
 c^2-\left(\frac7{20}\right)^2
 \left[\left(\frac{22}{7}\right)^2
 +132\left(\frac7{20}\right)^2\right]
 =\frac{1967}{40000}>0.
 \tag{22}
\]

Thus every vertical fiber in (3) is nonempty, including the ratio face
\(\rho=13/20\).

It also stays strictly below the inherited upper floor. Indeed,

\[
 V(\rho)<\frac{9/5}{(11/50)^2}
 =\frac{4500}{121}<64
 \tag{23}
\]

on the open upper ratio face. Throughout
\(\rho_c\leq\rho<5/6\), the accepted formula gives

\[
 K_0(\rho)>64.
 \tag{24}
\]

Since
\(\rho_c<1/7<13/20<39/50<5/6\), equations (23)--(24) prove

\[
 k_{11}(\rho)<V(\rho)<K_0(\rho)
\]

on the whole new strip. Hence (3) is an actual subset of (1), not merely
an analytic band outside the active finite window.

## 6. Exact residual subtraction and face ownership

Subtracting (3) from (1) leaves

\[
\boxed{
\begin{aligned}
 \mathcal D_{21}^{\mathrm{mid,new}}
 ={}&\left\{(\rho,K):
 \rho_c\leq\rho<\frac{13}{20},
 \quad k_{11}(\rho)<K<K_0(\rho)\right\}\\
 &\cup
 \left\{(\rho,K):
 \frac{13}{20}\leq\rho<\frac{39}{50},
 \quad V(\rho)<K<K_0(\rho)\right\}.
\end{aligned}}
 \tag{25}
\]

Every relevant face has an owner:

- \(\rho=13/20\) belongs to the new aggregate theorem;
- \(\rho=39/50\) belongs to the independently audited all-frequency
  optical theorem and was already excluded from (1);
- \(K=k_{11}\) belongs to the prospective staircase predecessor, while
  the product theorem independently covers it as well;
- \(K=V(\rho)\) is included by (2), so the new residual is strict above
  that face;
- \(K=K_0(\rho)\) belongs to the accepted fixed-ratio high-energy
  theorem;
- radial faces \(a=m\pi\) and product angular faces are excluded from the
  strict product count, while the reserve (19) remains strict.

## 7. Exact frontier of this one-screen mechanism

The clean face \(13/20\) is close to the limit of this particular
aggregate screen. The exact deficit identity itself shows that no uniform
constant larger than

\[
 C_*:=\sqrt[3]{3}-1
 \tag{26}
\]

is possible: on the first radial cell, equality in the limiting ratio is
attained at \(t=C_*\). The rational upper bound

\[
 C_*<\frac{1769}{4000}
\]

follows from

\[
 \left(1+\frac{1769}{4000}\right)^3-3
 =\frac{171609}{64000000000}>0.
 \tag{27}
\]

Consider the next clean ratio \(\rho=16/25\), so
\(\varepsilon=9/25\). Even allowing the upper bound in (27), positivity
of the refined screen forces

\[
 c<c_{\max}
 :=\frac{3}{2q(1-\varepsilon/3)}
 \left(\frac{1769}{4000}
 -\frac{\varepsilon}{4}-\varepsilon^2q^2\right)
 =\frac{250696431}{138054400}.
 \tag{28}
\]

But a nonempty band above \(k_{11}\) would require

\[
 c^2>\varepsilon^2
 \left(\pi^2+132\varepsilon^2\right).
\]

Using \(\pi>333/106\), these two requirements are incompatible, with
exact squared gap

\[
 \varepsilon^2
 \left[\left(\frac{333}{106}\right)^2
 +132\varepsilon^2\right]-c_{\max}^2
 =\frac{2365017023319254127}
 {11911885849600000000}>0.
 \tag{29}
\]

This is an obstruction only to the present one-screen product estimate,
not to a phase or shifted-tail closure of the remaining region.

A quantified next lemma is available. At \(\varepsilon=9/25\), choose
\(c=1871/1000\). It gives the strict nonempty-band reserve

\[
 c^2-\varepsilon^2
 \left[\left(\frac{22}{7}\right)^2
 +132\varepsilon^2\right]
 =\frac{4186153}{1225000000}>0.
 \tag{30}
\]

The refined screen at this \(c\) exceeds the rational ceiling in (27) by

\[
 \frac{38016757}{3696300000}<\frac1{97},
 \qquad
 \frac1{97}-\frac{38016757}{3696300000}
 =\frac{8674571}{358541100000}>0.
 \tag{31}
\]

Therefore a coupled lattice estimate that recovers \(a^2/97\) beyond the
separated radial-deficit and angular-ceiling budget at this face would
cross \(\rho=16/25\). The gain cannot come from a better uniform radial
deficit alone because of (26); it must retain angular fractional-part
gain, phase slack, or a shifted-tail compensation that (8) discards.

## 8. Verdict

The non-staircase route is an exact exploratory **PASS** on the major
face-connected band (3). It aggregates all product radial and angular
modes, retains the exact \(\varepsilon^2/3\) Weyl contribution, and
removes the complete region

\[
 \boxed{
 \frac{13}{20}\leq\rho<\frac{39}{50},
 \qquad
 k_{11}(\rho)<K\leq
 \frac{9}{5(1-\rho)^2}.}
\]

The remaining frontier is quantified by (29)--(31). Further progress
below \(13/20\) should target a coupled fractional-part or shifted-tail
gain rather than another uniform improvement of the radial deficit.

Promotion remains forbidden until a proof-free freeze, clean-room
reconstruction, exact-constant audit, adversarial review, and State Patch
audit are complete.
