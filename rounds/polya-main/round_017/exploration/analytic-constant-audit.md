# Round 17 independent constant audit for Candidate C17

Status: **PASS FOR FINITE ARITHMETIC ONLY**.

First mismatch: **none**.

This audit was completed before reading any Round 17 incumbent proof, A3
reconstruction, cross-review, or judge draft. Its only mathematical inputs
were the following immutable packets:

| input | SHA-256 |
|---|---|
| state/lemma_packets/SHELL-first-angular-bands-round17-claim.md | c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77 |
| state/lemma_packets/SHELL-rho-compact-round17.md | eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e |
| state/lemma_packets/SHELL-sturm-liouville-completeness.md | 6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8 |

The executable ledger independently reconstructs a rational Machin
enclosure and proves

$$
\frac{333}{106}<\pi<\frac{22}{7}.
\tag{1}
$$

No floating-point value or sampled spectral root enters a PASS decision.

## 1. Spectral reduction whose constants were audited

Write

$$
w=1-\rho,
\qquad
z=\frac{\pi}{w},
\qquad
k_1^2=z^2+2,
\qquad
k_2^2=z^2+6.
$$

The permitted one-dimensional min--max input gives

$$
\lambda_{\ell,n}
\ge n^2z^2+\ell(\ell+1).
\tag{2}
$$

The \(\ell=0\) block is exactly the Dirichlet interval Laplacian, so
\(\lambda_{0,1}=z^2\). On the candidate band \(K\le k_2\):

- every \(n\ge2\) is excluded because
  \(4z^2-(z^2+6)=3z^2-6>21\);
- every \(\ell\ge2\) is excluded because its first lower bound is at least
  \(z^2+6=k_2^2\);
- only the first \(\ell=0,1\) modes can contribute.

The strict-count ledger is therefore

| frequency face | strict count bound |
|---|---:|
| \(K=z\) | \(0\) |
| \(z<K\le k_1\) | \(1\) |
| \(k_1<K\le k_2\) | \(1+3=4\) |

At \(K=k_1\), a possible equality in the \(\ell=1\) lower bound is excluded
by strict counting. At \(K=k_2\), the same is true for \(\ell=2\).
Cross-order coincidences do not change these upper bounds because their
multiplicities have already been added.

This section records how the constants enter the candidate proof. The
executable ledger does not itself prove the min--max theorem, spectral
completeness, or strict multiplicity formula.

## 2. First Weyl margin

Let

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

At \(K=z\),

$$
\mathcal W(\rho,z)
=\frac{2\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}.
$$

The exact derivative identity is

$$
\frac{d}{d\rho}
\frac{1+\rho+\rho^2}{(1-\rho)^2}
=\frac{3(1+\rho)}{(1-\rho)^3}>0.
\tag{3}
$$

Hence the minimum on \([\rho_c,7/8]\) is at \(\rho_c\). Since

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_{\rho_c}=\pi+\frac12,
$$

direct cancellation gives

$$
\mathcal W(\rho_c,z_{\rho_c})-1
=\frac{4\pi^2+6\pi-15}{18}
>\frac{13}{6}>0,
\tag{4}
$$

where the last comparison uses only \(\pi>3\). This is the first exact Weyl
payment. Thus the count \(1\) is strictly paid immediately above the
zero-count wall.

## 3. Second Weyl margin

For \(K=k_1\), logarithmic differentiation shows that monotonicity in
\(\rho\) reduces exactly to

$$
z^2(1+\rho)>2\rho^2.
\tag{5}
$$

On \(0\le\rho<1\), the left side is greater than \(9\) and the right side is
less than \(2\), so this function is strictly increasing. Its minimum is
again at \(\rho_c\).

The rational bounds (1) give

$$
\rho_c<\frac17,
\qquad
1-\rho_c^3>\frac{342}{343},
\qquad
z_{\rho_c}=\pi+\frac12>\frac{193}{53},
\qquad
\frac{2}{9\pi}>\frac7{99}.
$$

Every factor is positive. Squaring the proposed lower bound is therefore
reversible, and the ledger obtains

$$
\left[
\frac7{99}\frac{342}{343}
\left(\left(\frac{193}{53}\right)^2+2\right)^{3/2}
\right]^2-4^2
=
\frac{88584210264668}{53216631070729}>0.
\tag{6}
$$

Consequently

$$
\mathcal W(\rho,k_1(\rho))>4
\qquad
(\rho_c\le\rho\le7/8).
\tag{7}
$$

This is the second exact Weyl payment. Since \(\mathcal W\) increases with
\(K\), it strictly pays the count bound \(4\) throughout
\(k_1<K\le k_2\).

## 4. Exact domain and order relations

The elementary radical checks used by the branch proof are

$$
2-\left(\frac{45}{32}\right)^2
=\frac{23}{1024}>0,
\qquad
\left(\frac74\right)^2-3
=\frac1{16}>0.
$$

They imply

$$
C_0=1+\frac{8\sqrt2}{15}>\frac74,
\qquad
\omega_0<\frac18,
\qquad
\rho_*=\frac{\omega_0}{2C_0}<\frac1{16}.
$$

Using the frozen certified locator for \(\rho_{HK}\), the full relevant
order is

$$
\rho_*<\frac1{16}<\frac{9407}{100000}
<\rho_{HK}<\frac{94071}{1000000}<\frac1{10}
<\frac18<\frac7{51}
<\rho_c<\frac{53}{386}<\frac17
<\frac12<\frac56<\frac78.
\tag{8}
$$

In particular, the \(H_0\)-to-\(K_0\) switch lies strictly left of
\(\rho_c\), so \(H_0\) is never the active upper branch on Candidate C17.

For \(\rho\ge\rho_c\),

$$
\frac{\pi}{1-\rho}\ge\frac1{2\rho},
$$

with equality exactly at \(\rho_c\). Hence the frozen residual lower wall is
\(L(\rho)=z_\rho\), and the strict candidate condition \(K>z_\rho\) lies
above both accepted lower rays.

The identities

$$
k_1^2-z^2=2,
\qquad
k_2^2-k_1^2=4
$$

prove \(z<k_1<k_2\); all denominators and radicands are positive on the
stated ratio domain. Since \(1-\rho\) is positive and strictly decreasing,
\(z\), \(k_1\), and \(k_2\) are all strictly increasing in \(\rho\).

## 5. Proof that the candidate stays below every residual upper branch

### 5.1 The branch \(\rho_c\le\rho\le1/2\)

Here \(\eta_\rho=\omega_0<1/8\). The positive-root equation for \(K_0\)
gives

$$
K_0>\frac{C_0}{\eta_\rho}>14.
$$

Meanwhile

$$
7^2-k_2(1/2)^2
>
49-4\left(\frac{22}{7}\right)^2-6
=\frac{171}{49}>0.
\tag{9}
$$

Thus \(k_2<7<14<K_0\) on this complete branch.

### 5.2 The branch \(1/2\le\rho<5/6\)

The elementary action integral gives \(\eta_\rho\le w/2\), hence

$$
K_0>\frac{C_0}{\eta_\rho}
\ge\frac{2C_0}{w}.
$$

Since \(w\le1/2\),

$$
\left(\frac72\right)^2
-\left[
\left(\frac{22}{7}\right)^2+\frac32
\right]
=\frac{171}{196}>0.
\tag{10}
$$

Therefore

$$
w\,k_2=\sqrt{\pi^2+6w^2}
<\frac72<2C_0,
$$

and again \(k_2<K_0\).

### 5.3 The seam branch \(5/6\le\rho<7/8\)

Here \(w\le1/6\), and

$$
6^2-\left[
\left(\frac{22}{7}\right)^2+\frac16
\right]
=\frac{7631}{294}>0.
\tag{11}
$$

Thus

$$
w^2k_2
=w\sqrt{\pi^2+6w^2}
<1<54,
$$

so

$$
k_2<\frac{54}{w^2}.
$$

This is strict at \(\rho=5/6\), where the seam branch begins inclusively.

Finally, on the complete closed ratio band,

$$
26^2-\left[
\left(8\frac{22}{7}\right)^2+6
\right]
=\frac{1854}{49}>0.
$$

Hence \(k_2<26<87025\), so Candidate C17 never reaches the independently
accepted global-energy face.

Combining the lower and upper comparisons proves the exact bookkeeping
relation

$$
\boxed{\mathcal C_{17}\subset\mathcal D_{16}.}
\tag{12}
$$

At \(\rho=\rho_c\), the two old lower walls meet, but the candidate uses
\(K>z_\rho\). At \(\rho=1/2\), the \(K_0\) formula is continuous. At
\(\rho=5/6\), the seam becomes the active upper branch. The proposed new set
excludes \(\rho=7/8\); the complete old endpoint theorem owns that face.
The closed spectral band nevertheless proves the inequality there by the
same two Weyl margins.

## 6. Complete containment of the Round 8 box

The worst lower-wall corner of \(B_0\) is
\((\rho,K)=(1001/2000,67/10)\). From \(\pi<22/7\),

$$
\frac{67}{10}
-\frac{22/7}{999/2000}
=\frac{28531}{69930}>0.
\tag{13}
$$

The worst upper-wall corner is
\((\rho,K)=(999/2000,168/25)\). From \(\pi>333/106\),

$$
\left(
\frac{333/106}{1001/2000}
\right)^2
+6-\left(\frac{168}{25}\right)^2
=
\frac{420595320534}{1759138005625}>0.
\tag{14}
$$

The ratio faces satisfy

$$
\rho_c<\frac17<\frac{999}{2000}
<\frac{1001}{2000}<\frac78.
$$

All inequalities required at all four closed faces are therefore uniform,
and

$$
\boxed{B_0\subset\mathcal C_{17}.}
\tag{15}
$$

This is a set-containment result only. Until C17 passes every analytic
promotion gate, \(B_0\) remains certified coverage rather than analytically
absorbed coverage.

## 7. Intended first-method obstruction

Immediately above \(k_2\), the crude min--max cap must permit the first
\(\ell=2\) mode, so it jumps from

$$
1+3=4
\quad\hbox{to}\quad
1+3+5=9.
$$

At \(\rho=\rho_c\),

$$
z_{\rho_c}<\frac{51}{14},
\qquad
k_2(\rho_c)^2<\frac{3777}{196},
\qquad
\mathcal W(\rho_c,k_2)
<
\frac2{27}
\left(\frac{3777}{196}\right)^{3/2}.
$$

All quantities are positive, and the exact squared upper comparison is

$$
9^2-
\left[
\frac2{27}
\left(\frac{3777}{196}\right)^{3/2}
\right]^2
=\frac{2121156829}{50824368}>0.
\tag{16}
$$

Therefore

$$
\mathcal W(\rho_c,k_2(\rho_c))<9.
$$

By continuity, the crude cap \(9\) cannot be uniformly paid immediately
above the \(k_2\) face. This refutes only an extension of the same
cap-payment method; it is not a counterexample to the shell inequality and
does not assert that the actual count equals \(9\).

## 8. What the ledger does not prove

The exact executable checks do not prove:

1. the authenticated separated-spectrum theorem, strict multiplicities, or
   cross-order direct-sum statement;
2. the Poincare/min--max eigenvalue bound or exact \(\ell=0\) interval
   spectrum;
3. the frozen normalized residual identity and ownership of all its faces;
4. the \(K_0\) positive-root equation, \(\eta_\rho=\omega_0\) below
   \(1/2\), or \(\eta_\rho\le w/2\) above \(1/2\);
5. the calculus arguments reducing both Weyl derivatives to the displayed
   positive expressions;
6. continuity used in the first-method obstruction;
7. Machin's identity or the alternating-series remainder theorem, although
   it independently executes their exact rational consequences;
8. the analytic positivity arguments that justify reversible squaring.

Those are analytic obligations for the isolated reconstruction and
adversarial referee. A finite-ledger PASS cannot replace them.

## 9. Reproduction and artifacts

~~~powershell
python computations/round17_verify_candidate_c17_constants.py
python -m pytest computations/tests/test_round17_candidate_c17_constants.py -q
~~~

Ledger result: **PASS**, 28 exact checks, first mismatch none.

Focused tests: **6 passed**.

| artifact | SHA-256 |
|---|---|
| computations/round17_verify_candidate_c17_constants.py | b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469 |
| computations/tests/test_round17_candidate_c17_constants.py | 533620b5fadd9b7b13ff1d21ca9282bfd3d1ed778e7ecda970a3fb027ce3955c |

The verdict is **PASS for the finite constants and set arithmetic**. It does
not by itself prove or promote Candidate C17.
