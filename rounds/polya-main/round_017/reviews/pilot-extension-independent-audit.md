# Round 17 independent audit of the face-connected pilot extension

Status: **PASS FOR THE SINGLE CLOSED BOX \(B_1\) ONLY**.

This review is independent of the producer's sign decisions. It authenticates
the final certification report
rounds/polya-main/round_017/certification/pilot-extension-feasibility.md at
SHA-256
f19e265ce4b01994ab204097132f1f51828e3018e4efaa288f8c0ed19da81e19.
The frozen residual packet used by the certification has SHA-256
eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e.

## 1. Authenticated artifacts

The five hashes embedded in the certification report were recomputed from the
current bytes and all matched.

| artifact | independently recomputed SHA-256 |
|---|---|
| computations/round17_pilot_extension_certificate.py | 38362dd192c7918a3895eb4b13a1afdd076eaae28a650eb8bed31d517314a2a7 |
| computations/round17_verify_pilot_extension_certificate.py | 40a814e2a3557363d1d958f10c38c295ac0af894e4e8b441ea7dbd0c968991df |
| computations/tests/test_round17_pilot_extension_certificate.py | 71b79d96ff8b7f30cd9b74ed433c4e8b5182fc3e0270db0ad0a5d3f0d3b912a9 |
| rounds/polya-main/round_017/certification/pilot-extension-upward.json | 858c55e832b3ca92f3b077dd7ea55f7ef6c4f7456de786c7264f178fcdf77b5b |
| rounds/polya-main/round_017/certification/pilot-extension-upward-check.json | e3bddf0b1488812e7572c318888f7f4721148b78c5e9ff98f7dabe7b19351d3f |

The checker also authenticated the producer, itself, both Round 8 arithmetic
helpers, the frozen Round 17 packet, its external freeze record, and the
retained \(B_0\) certificate and check report.

## 2. Exact box and face geometry

The retained certified box and proposed extension are

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right],
$$

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

Exact interval intersection gives

$$
B_0\cap B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times\left\{\frac{168}{25}\right\}.
$$

This is all of the closed upper \(K\)-face of \(B_0\) and all of the closed
lower \(K\)-face of \(B_1\). The two interiors are disjoint. The Round 17
certification directory contains no second extension box.

## 3. Membership in the frozen residual

The ratio interval of \(B_1\) lies strictly between \(\rho_c\) and \(5/6\),
and it straddles only the continuous \(K_0\)-formula interface at
\(\rho=1/2\). On this cell the frozen packet gives

$$
\frac{\pi}{1-\rho}<K<K_0(\rho).
$$

For the lower wall, the minimum of \((1-\rho)K\) occurs at
\((\rho,K)=(1001/2000,168/25)\). Using \(\pi<22/7\),

$$
(1-\rho)K-\pi
\ge
\frac{999}{2000}\frac{168}{25}-\frac{22}{7}
=\frac{9353}{43750}>0.
$$

For the upper wall, the frozen packet proves
\(K_0(\rho)>8\pi\rho/(1-\rho)\) on \(\rho>\rho_c\). Since
\(\pi>3\) and \(\rho/(1-\rho)\) is increasing,

$$
K_0(\rho)-K
>
24\frac{999}{1001}-\frac{673}{100}
=\frac{1723927}{100100}>0.
$$

Thus every closed face of \(B_1\) lies strictly inside
\(\mathcal D_{16}\), and \(B_1\setminus B_0\subset\mathcal U_{16}\).

## 4. Determinants, roots, and strict count

The producer used 256-bit Arb balls. The independent checker reconstructed
the first two Riccati--spherical determinant formulas with exact rational
interval arithmetic, a Machin enclosure for \(\pi\), and alternating Taylor
enclosures for sine and cosine. Its decisive signs are:

| channel | uniform root bracket | lower face | upper face | all of \(B_1\) |
|---:|---:|:---:|:---:|:---:|
| \(\ell=0\) | \([31/5,63/10]\) | positive | negative | negative |
| \(\ell=1\) | \([13/2,33/5]\) | positive | negative | negative |

The exact-Fraction determinant intervals are separated from zero on every
listed domain. In particular, the determinant is nonzero throughout \(B_1\),
so the target box contains no spectral wall. Both bracket upper endpoints are
strictly below \(168/25\).

For \(w=1-\rho\), the accepted Poincare--Sturm estimate is

$$
\lambda_{n,\ell}\ge
\left(\frac{n\pi}{w}\right)^2+\ell(\ell+1).
$$

The independently reconstructed Machin bounds imply
\(\pi>314159/100000\). At the largest width \(1001/2000\) and the largest
frequency \(673/100\), the two decisive margins satisfy

$$
\left(\frac{\pi}{1001/2000}\right)^2+6
-\left(\frac{673}{100}\right)^2
>
\frac{213651639}{2004002000}>0,
$$

$$
\left(\frac{2\pi}{1001/2000}\right)^2
-\left(\frac{673}{100}\right)^2
>
\frac{1125298725567}{10020010000}>0.
$$

The first inequality excludes every \(\ell\ge2\) channel. The second permits
at most one radial root in each of \(\ell=0,1\). Continuity and the two uniform
sign changes supply at least one root in each displayed bracket; simplicity
and completeness then give exactly one. Because those roots lie strictly
below every \(K\) in \(B_1\), the strict multiplicity-weighted count is

$$
N_D(A_{\rho,1},K^2)=1+3=4
$$

on the complete closed box.

## 5. Strict Weyl margin

The Weyl expression decreases with \(\rho\) and increases with \(K\), so its
minimum on \(B_1\) occurs at
\((\rho,K)=(1001/2000,168/25)\). The coarse rational bound
\(\pi<22/7\) already gives

$$
\frac{2}{9\pi}
\left(1-\left(\frac{1001}{2000}\right)^3\right)
\left(\frac{168}{25}\right)^3-4
>
\frac{39657181883797}{2685546875000}>0.
$$

The exact-Fraction checker gives the stronger lower margin
\(14.774446117789985\ldots\). Hence the strict shell inequality holds
throughout \(B_1\).

## 6. Independence and reproduction

The producer imports the frozen Round 8 Arb determinant backend. The checker
imports neither python-flint nor the Round 17 producer; it reuses only the
previously audited Round 8 exact-rational interval primitives and rebuilds
all decisive signs and inequalities independently.

Fresh in-memory reproduction gave:

- the rebuilt producer dictionary exactly equal to
  pilot-extension-upward.json;
- the rebuilt checker dictionary exactly equal to
  pilot-extension-upward-check.json;
- checker status PASS and strict weighted count \(4\);
- 6 focused tests passed.

## 7. Verdict and limitations

**PASS. No unsupported implication remains in the authenticated one-box
claim.**

This result certifies \(B_1\) only. It adds certified overlay coverage and
does not add a branch to \(\mathcal A_{16}\), close \(\mathcal D_{16}\) or
\(\mathcal U_{16}\), promote COMP-certified-bessel, or prove the full shell
theorem.
