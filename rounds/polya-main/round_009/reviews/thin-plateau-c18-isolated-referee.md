# Isolated Referee Report: Frozen \(C=18\) Thin-Plateau Candidate

## Verdict

**PASS for the isolated-reconstruction gate.** Conditional only on the
permitted proved inputs, the packet proves

\[
0<\varepsilon\le\frac1{100},\qquad K\ge18\varepsilon^{-2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3.
\]

The equality \(K=18\varepsilon^{-2}\) is included. No step imports the old
\(64\varepsilon^{-2}\) conclusion. This report satisfies only the isolated
referee gate; the frozen promotion rule still requires the separate
adversarial audit.

I read the frozen packet and only its cited pre-Round-9 dependencies. I did
not read the Round 9 incumbent response or any other Round 9 review. I ran
the rational ledger only after reconstructing the proof and independently
re-entered its decisive fractions.

## 1. Permitted tail decomposition

Put

\[
\rho=1-\varepsilon,\quad \mu=\rho K,\quad x_0=r+\frac12<\mu,
\quad n=\lfloor\mu-x_0\rfloor,\quad q=x_0+n,
\]

\[
\beta=\mu-q\in[0,1),\quad p\in\{0,\ldots,n\},\quad
m=n-p,\quad d=\frac{2\arcsin\rho}{\pi},\quad \eta=G_1(\rho).
\]

The permitted pre-threshold result is

\[
\frac{\mathcal T_r}{2}
\le\int_{x_0}^K A_{\rho,K}(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor+dm-p,
\tag{1}
\]

\[
0\le\delta<\frac{2\sqrt2}{15},\qquad
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{2}
\]

It therefore suffices to prove \(M\ge1\), since

\[
4\delta<\frac{8\sqrt2}{15}<\frac45<1.
\tag{3}
\]

## 2. Exact trigonometric constants

For \(a=\arctan(1/5)\) and \(b=\arctan(1/239)\),

\[
\tan(2a)=\frac5{12},\qquad \tan(4a)=\frac{120}{119},
\qquad \tan(4a-b)=1.
\]

The angle range gives Machin's identity
\(\pi=16a-4b\). Alternating arctangent bounds give

\[
\pi<
16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
<\frac{355}{113},
\tag{4}
\]

with exact final gap

\[
\frac{45167474711}{189820334689453125}>0.
\]

The complementary coarse sums give
\(\pi>281476/89625>3\). Moreover,

\[
\sin\frac43
<\frac43-\frac{(4/3)^3}{6}+\frac{(4/3)^5}{120}
=\frac{3548}{3645}<\frac{99}{100}\le\rho.
\]

Since \(4/3<\pi/2\) and \(355/113<10/3\),

\[
\arcsin\rho>\frac43>\frac{2\pi}{5},
\qquad \boxed{d>\frac45}.
\tag{5}
\]

The other exact square-root bounds used below are
\(140/99<\sqrt2<3/2\).

## 3. Localization in the only dangerous branch

Let

\[
R=p-dm,\qquad U=\mu-x_0=n+\beta.
\]

If \(R>0\), then \(p>dm\), and (5) yields

\[
m<\frac54p,\qquad n<\frac94p,\qquad
U<1+\frac94p.
\tag{6}
\]

Using (2), \(K\ge18\varepsilon^{-2}\),
\(\varepsilon\le1/100\), and \(\rho\ge99/100\),

\[
\frac U{\rho K}
<\frac1{\rho K}+\frac94\sqrt{\frac{2\pi}{\varepsilon\rho K}}
\le\frac1{178200}+\frac94\sqrt{\frac\pi{891}}.
\tag{7}
\]

Set

\[
s=\frac49\left(\frac{67}{500}-\frac1{178200}\right)
=\frac{119389}{2004750}.
\]

Exact arithmetic gives

\[
s^2-\frac{355/113}{891}
=\frac{9377802773}{454149549562500}>0.
\]

Thus (4) and (7) imply

\[
\boxed{\frac U{\rho K}<\frac{67}{500}},\qquad
\boxed{t:=\frac{x_0}{\rho K}>\frac{433}{500}}.
\tag{8}
\]

These inequalities remain strict when
\(\varepsilon=1/100\) and \(K=18\varepsilon^{-2}\).

## 4. Local slope and shelf polynomial

For \(0<z<\mu\),

\[
\sigma(z):=-A'_{\rho,K}(z)
=\frac1\pi\left(\arccos\frac zK-\arccos\frac z{\rho K}\right).
\]

Writing \(a=z/K\) and integrating
\((1-u^2)^{-1/2}\) from \(a\) to \(a/\rho\) gives

\[
\sigma(z)\ge
\frac{\varepsilon z}{\pi\rho\sqrt{K^2-z^2}}.
\tag{9}
\]

In the dangerous branch \(p>0\). The same-floor relation, including on an
ordinary-floor wall, gives

\[
A(x_0)-A(x_0+p)<1.
\]

Since \(\sigma\) is increasing,
\(1>p\sigma(x_0)\). Using (9),
\(K^2-x_0^2<2K(K-x_0)\), \(K-x_0=\varepsilon K+U\), and (8),

\[
p^2<A_0\left(\frac1\varepsilon+\frac1{18}+\frac p8\right),
\qquad
A_0=2\pi^2\left(\frac{500}{433}\right)^2.
\tag{10}
\]

The exact coefficient check is

\[
A_0<
\frac{63012500000}{2394047041}
<\frac{1053}{40},
\]

\[
\frac{1053}{40}
-\frac{63012500000}{2394047041}
=\frac{431534173}{95761881640}>0.
\tag{11}
\]

Let \(x=\varepsilon^{-1/2}\ge10\) and

\[
F_x(y)=y^2-\frac{1053}{320}y
-\frac{1053}{40}\left(x^2+\frac1{18}\right).
\]

Equation (10) implies \(F_x(p)<0\). If \(p\ge53x/10\),
monotonicity in \(y\) reduces the contradiction to
\(g(x)=F_x(53x/10)\). Exactly,

\[
g(10)=\frac{203}{320}>0,\qquad
g'(10)=\frac{57151}{3200}>0,
\]

\[
\left(\frac{53}{10}\right)^2-\frac{1053}{40}
=\frac{353}{200}>0.
\]

Hence \(g'\) and \(g\) stay positive for \(x\ge10\), contradicting
\(F_x(p)<0\). Therefore

\[
\boxed{p<\frac{53}{10\sqrt\varepsilon}}.
\tag{12}
\]

## 5. Integer-floor gain and exceptional branches

The exact action identity and
\(\arccos(1-v)>\sqrt{2v}\) for \(v>0\) give

\[
\eta=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv,
\]

\[
K\eta>
\frac{12\sqrt2}{\pi\sqrt\varepsilon}
>\frac{12656}{2343\sqrt\varepsilon}.
\tag{13}
\]

Combining (12) and (13),

\[
K\eta-p>
\frac{2381}{23430\sqrt\varepsilon}
\ge\frac{2381}{2343}
=1+\frac{38}{2343}>1.
\tag{14}
\]

Since \(p\) is an integer,

\[
\boxed{\lfloor K\eta\rfloor\ge p+1}.
\tag{15}
\]

If \(K\eta\in\mathbb Z\), (14) actually forces
\(K\eta\ge p+2\).

- If \(R>0\), then (15) gives
  \(M=\lfloor K\eta\rfloor+dm-p\ge1+dm\ge1\).
- If \(R\le0\), then \(M\ge\lfloor K\eta\rfloor\ge1\); indeed (13) at
  \(\varepsilon=1/100\) gives
  \(K\eta>126560/2343=54+38/2343\).
- If \(R=0\), then \(M=\lfloor K\eta\rfloor\ge1\).
- If \(p=n>0\), then \(m=0\), \(R=p>0\), and the dangerous proof applies.
- If \(p=0\), then \(R=-dm\le0\); no division by \(p\) is used.
- If \(n=0\), then \(p=m=0\) and
  \(M=\lfloor K\eta\rfloor\ge1\).
- The first dangerous cases \(p=1,m=0\) and \(p=1,m=1\) use only the sign
  \(p>dm\), so no large-\(p\) assumption is hidden.

Thus \(M\ge1>4\delta\) in every branch. Equation (1) proves every
low-interface shifted tail. The permitted high-angular result covers the
other tails, and the weighted scaffold plus strict phase transfer proves the
target theorem.

## 6. Requested wall and endpoint audit

| Case | Result |
| --- | --- |
| \(\varepsilon=1/100\) | The shelf margin is \(203/320\); the gain margin above one is \(38/2343\). |
| \(K=18\varepsilon^{-2}\) | Equality is safe because the action bound and same-floor step remain strict. |
| \(q=\mu\) | Then \(\beta=0\), \(U=n\), and \(\delta=0\). |
| \(p=n\) | For \(p>0\), \(m=0\) and the dangerous proof applies; \(p=0\) is the \(n=0\) case. |
| \(p=0\) | \(R\le0\), so \(M\ge\lfloor K\eta\rfloor\). |
| \(n=0\) | \(p=m=0\), so \(M=\lfloor K\eta\rfloor\). |
| \(K\eta\in\mathbb Z\) | The strict gap forces \(K\eta\ge p+2\). |
| Ordinary-floor wall | Equal floors still imply \(A(x_0)-A(x_0+p)<1\); an immediate drop gives \(p=0\). |
| Spectral wall | Strict counting uses \(n\pi<\Psi(K)\), excluding endpoint eigenvalues. |
| Transferred phase wall | An integral ordinary-floor proxy can only overcount the strict phase count. |
| \(R=0\) or arbitrarily small \(R>0\) | Only the sign of \(R\) is used. |

## 7. Exact overlap and compact ceiling

\[
18\varepsilon^{-2}\le\frac1{8\varepsilon^{5/2}}
\Longleftrightarrow
144\sqrt\varepsilon\le1
\Longleftrightarrow
\boxed{\varepsilon\le\frac1{20736}}.
\tag{16}
\]

Both ranges include equality. At \(\varepsilon=1/20736\), their common
frequency is

\[
18(20736)^2
=2^{17}3^{10}
=7739670528
<2^{33},
\]

with exact gap \(850264064\) to \(2^{33}\). The aggregate lower seam is below
this point because \(\pi/(4\varepsilon^2)<18/\varepsilon^2\).

On \(1/20736\le\varepsilon\le1/100\), a possible residual satisfies

\[
K<18\varepsilon^{-2}
\le18(20736)^2<2^{33}.
\]

Together with the unchanged central residual ceiling below \(2^{35}\), this
gives the claimed compact analytic ceiling \(2^{35}\).

## Final assessment

The \(C=18\) candidate is analytically sound, endpoint-safe, and independent
of the old \(C=64\) threshold. The exact verifier
computations/round9_verify_thin_plateau_constants.py and its focused test both
pass; they corroborate, but do not replace, the reconstruction above.
