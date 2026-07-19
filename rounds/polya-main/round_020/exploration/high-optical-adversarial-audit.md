# Round 20 adversarial audit: optimized optical threshold

Status: **PASS**.

Date: 2026-07-15.

Audited target:

`rounds/polya-main/round_020/exploration/high-optical-optimization.md`

Audited SHA-256:

`6e6eb668cb284ede7ab6662b772af9004158d8d7098a83d549786823804ddc16`

Adversarial stance: assume that the claimed all-frequency theorem on
\(39/50\leq\rho<1\) is false, and locate the first unsupported implication.
I reconstructed the new deficit lemma, both optical screens, their complete
validity range, all strict faces, and the prospective residual subtraction.
No unsupported implication was found.

## 1. Provenance and byte audit

The four hashes declared by the target match the files on disk exactly:

| dependency | recomputed SHA-256 |
|---|---|
| `rounds/polya-main/round_020/exploration/high-global-route.md` | `bbfc40bcb7ce748b946a6fdea7728315489d7e2e7842a0ccb6789f3f34fee6c4` |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |

The repaired predecessor also names the prospective \(k_9\) proof and its
audit for the residual calculation. Their recomputed hashes are respectively
`d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1`
and
`b31a7b4d667992a4e02ffe4e5e5999cdfe611a8b67bd58ea57cdb22a4dc7f63d`.

The target and all four direct dependencies decode as UTF-8, end in a newline,
contain no carriage returns or tabs, contain no trailing horizontal whitespace,
and contain no forbidden control bytes. The target has 8,999 bytes. Thus the
audited object is unambiguous and the repair hash of the predecessor is the one
actually used.

No new Bessel-zero value, external source, or numerical table enters the new
argument. The only new mathematical input is elementary exact algebra applied
to the predecessor's already declared product and complementary-action
identities.

## 2. Scaling, split, and range

Set

\[
 \varepsilon=1-\rho,
 \qquad 0<\varepsilon\leq\varepsilon_0=\frac{11}{50},
 \qquad a=\varepsilon K,
 \qquad c=\frac{1126}{625}.
\]

Then \(39/50\leq\rho<1\) is exactly this \(\varepsilon\)-range. The two
inclusive sets \(a\leq c/\varepsilon\) and
\(a\geq c/\varepsilon\) cover every \(a\geq0\). At the worst ratio face,

\[
 \frac{c}{\varepsilon_0}=\frac{2252}{275},
 \qquad
 \frac{2252}{275}-\frac{44}{7}=\frac{3664}{1925}>0.
\]

Since \(\pi<22/7\), this common face is strictly above \(2\pi\), hence in
particular above the \(a>\pi\) domain of the new deficit lemma. No old
\(\varepsilon\leq1/8\) reserve is used.

The two threshold comparisons are also exact:

\[
 \frac{25}{32}-\frac{39}{50}=\frac1{800},
 \qquad
 \frac{32}{41}-\frac{39}{50}=\frac1{2050}.
\]

## 3. Independent reconstruction of the deficit lemma

For strict radial counting and \(a>\pi\), write uniquely

\[
 \frac a\pi=N+t,
 \qquad N\geq1,
 \qquad 0<t\leq1,
\]

using \((N,t)=(m-1,1)\) when \(a=m\pi\). The exact identity is

\[
 \frac{D(a)}{\pi^2}
 =\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
\]

Put

\[
 C=\frac{1382}{3125},
 \qquad A=\frac12-C=\frac{361}{6250},
 \qquad
 \Delta_N(t)=\frac{D(a)}{\pi^2}-C(N+t)^2.
\]

Direct subtraction, without a sampled estimate, gives

\[
 \Delta_{N+1}-\Delta_N
 =A(2N+1)+(t-C)^2+\frac16-C^2.
\]

For every \(N\geq1\),

\[
 \Delta_{N+1}-\Delta_N
 \geq3A+\frac16-C^2
 =\frac{4229603}{29296875}>0.
\]

Thus the worst integer cell is \(N=1\). Differentiation gives

\[
 \Delta_1'(t)=2(t-C)(t+1).
\]

Because \(0<C<1\), the unique minimum on \(0<t\leq1\) is \(t=C\), and
exact substitution gives

\[
 \Delta_1(C)
 =\frac23-C-C^2-\frac{C^3}{3}
 =\frac{1822532}{91552734375}>0.
\]

Therefore

\[
 \boxed{D(a)>\frac{1382}{3125}a^2\quad(a>\pi)}
\]

holds uniformly, including every spectral wall \(a=m\pi\) under the
required \(t=1\) convention. The improvement arithmetic is exact:

\[
 \frac{1382}{3125}-\frac{11}{25}
 =\frac7{3125}
 =\frac1{2000}+\frac{87}{50000}>\frac1{2000}.
\]

## 4. Reconstruction of the low optical piece

The product min--max direction is an upper bound on the shell count. If

\[
 b_n=(a^2-n^2\pi^2)^{1/2},
 \qquad
 M_n=\left\lceil
 \sqrt{(b_n/\varepsilon)^2+\frac14}-\frac12
 \right\rceil,
\]

then strict radial and angular counting gives
\(N_D\leq\mathcal P_\varepsilon=\sum M_n^2\). For \(b_n>0\), the strict
ceiling estimate

\[
 M_n<\sqrt{(b_n/\varepsilon)^2+\frac14}+\frac12
\]

and
\(\sqrt{x^2+1/4}<x+1/2\) for \(x>0\) imply

\[
 \varepsilon^2M_n^2<b_n^2+\varepsilon b_n+\varepsilon^2.
\]

The quarter-circle decreasing-sum bound and strict radial count give

\[
 \sum b_n<\int_0^{a/\pi}\sqrt{a^2-\pi^2x^2}\,dx=\frac{a^2}{4},
 \qquad N<\frac a\pi.
\]

Consequently, throughout the range in question,

\[
 \varepsilon^2\mathcal P_\varepsilon(a)
 <S_0(a)+\frac{\varepsilon a^2}{4}
 +\frac{\varepsilon^2a}{\pi}.
\]

Writing \(I_0=2a^3/(3\pi)\) and \(S_0=I_0-D\), it is enough to prove

\[
 D(a)>
 \varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
 +\frac{\varepsilon^2a}{\pi}.
 \tag{L}
\]

Indeed, (L) makes the product majorant strictly less than
\(I_0(1-\varepsilon)\), which is strictly less than
\(I_0(1-\varepsilon+\varepsilon^2/3)\).

For \(\pi<a\leq c/\varepsilon\), division of the right side of (L) by
\(a^2\), together with \(1/\pi<q=106/333\), gives the strict bound

\[
 \frac{2\varepsilon a}{3\pi}+\frac\varepsilon4
 +\frac{\varepsilon^2}{\pi a}
 <\frac{2cq}{3}+\frac\varepsilon4+\varepsilon^2q^2.
\]

Here the first term uses \(\varepsilon a\leq c\), while the last uses
\(a>\pi\), hence \(1/(\pi a)<1/\pi^2<q^2\). The low reserve has derivative

\[
 \frac{d}{d\varepsilon}R_L=-\frac14-2\varepsilon q^2<0,
\]

so its worst point is \(\varepsilon_0\). Exact substitution reproduces

\[
 R_L(C,c,\varepsilon_0)
 =\frac{39569}{2772225000}>0.
\]

The new deficit therefore proves (L), with strict slack, on the entire low
piece above \(\pi\). For \(0\leq a\leq\pi\), strict radial counting has no
level, including \(a=\pi\); hence the product count is zero. This closes the
whole low piece, including \(a=c/\varepsilon\).

The comparison with the predecessor's old limiting split is also exact:

\[
 \frac{1126}{625}-\frac{210742213}{117660000}
 =\frac{1234043}{117660000}>0.
\]

## 5. Reconstruction of the complementary-action screen

The inherited action argument is valid for every \(0<\varepsilon<1\), not
only for \(\varepsilon\leq1/8\). Let \(R\) be the decreasing inverse of
the exact action, \(F=R^2\), \(g=-F'\), \(T=a/\pi\), and let \(\tau\) be
the actual ungridded inner interface. Direct differentiation gives

\[
 g\text{ decreasing on }(0,\tau),
 \qquad
 g\text{ increasing on }(\tau,T),
\]

and

\[
 F(\tau)=\rho^2a^2,
 \qquad F(T)=0,
 \qquad g(T)=2\pi\rho a.
\]

For the strict shifted radial count, set \(w=t-C(t)\),
\(W(t)=\int_0^tw\), and \(\Psi=W-t/4\). The exact sawtooth bounds are

\[
 W\geq0,
 \qquad -\frac1{32}\leq\Psi\leq\frac3{32}.
\]

The Stieltjes identity and a split at the actual \(\tau\) give

\[
 D_{\rm rad}=\int_0^T w(t)g(t)\,dt
 =W(T)g(T)-\int_0^\tau W\,dg-\int_\tau^T W\,dg.
\]

The first Stieltjes integral on the right is nonnegative after the minus
sign because \(W\geq0\) and \(dg\leq0\). On the second interval use
\(W\leq t/4+3/32\), integrate \(t\,dg\), and then use
\(\Psi(T)\geq-1/32\). This yields

\[
\begin{aligned}
 D_{\rm rad}
 &\geq \Psi(T)g(T)+\frac{\tau g(\tau)}4
 +\frac{F(\tau)}4
 -\frac3{32}\bigl(g(T)-g(\tau)\bigr)\\
 &\geq\frac{F(\tau)}4-\frac{g(T)}8
 =\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\end{aligned}
\]

This derivation neither assumes \(\tau>1\) nor invokes an old endpoint
reserve.

For the angular ceiling, the exact half-integer count satisfies

\[
 M_\varepsilon(x)=
 \max\left\{0,\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil\right\}
 <\frac{x}{\varepsilon}+\frac12
\]

whenever that layer contributes. Since the number of strict radial layers
is \(J_{\rm rad}<T+1/4\) and \(R\leq a\), layer-cake summation bounds the
actual angular loss strictly by

\[
 E_{\rm actual}<E:=\left(\frac a\pi+\frac14\right)
 \left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\]

Thus on \(a\geq c/\varepsilon\), using \(1/a\leq\varepsilon/c\),
\(\pi<22/7\), and \(1/\pi<q\), it is sufficient that

\[
\begin{aligned}
 R_H(c,\varepsilon)={}&\frac{(1-\varepsilon)^2}{4}
 -\frac{(22/7)(1-\varepsilon)\varepsilon}{4c}\\
 &-\left(
 \varepsilon q+\frac{\varepsilon^3q}{4c}
 +\frac{\varepsilon^2}{4c}
 +\frac{\varepsilon^4}{16c^2}
 \right)>0.
\end{aligned}
\]

The lower part has derivative

\[
 -\frac{1-\varepsilon}{2}
 -\frac{11}{14c}(1-2\varepsilon)<0
 \qquad(0<\varepsilon<1/2),
\]

while the subtracted ceiling has derivative

\[
 q+\frac{3\varepsilon^2q}{4c}
 +\frac{\varepsilon}{2c}
 +\frac{\varepsilon^3}{4c^2}>0.
\]

Therefore \(R_H\) decreases on the whole required interval, so the worst
point is again \(\varepsilon_0=11/50\). Exact rational substitution gives

\[
 R_H(c,\varepsilon_0)
 =\frac{14817541}{472867032960000}>0.
\]

Although small, this reserve is exact. It proves \(D_{\rm rad}>E\), hence
\(P_{\mathcal A}<I\), including both \(\varepsilon=11/50\) and
\(a=c/\varepsilon\). The exact phase transfer then gives

\[
 N_D(A_{\rho,1},K^2)
 \leq\frac{2P_{\mathcal A}}{\varepsilon^2}
 <\frac{2I}{\varepsilon^2}
 =\frac{2}{9\pi}(1-\rho^3)K^3.
\]

## 6. Strict faces and prospective residual subtraction

The strict-face audit found no orphaned boundary:

- at \(K=a=0\), both sides are zero;
- for \(K>0\) and \(a\leq\pi\), the count is zero and the Weyl term is
  positive;
- at \(a=\pi\), the first radial threshold is excluded;
- at \(a=m\pi\), \(m\geq2\), the representation uses \(t=1\) and the
  positive deficit minimum still applies;
- product angular equality, action radial equality, half-integer equality,
  and phase-proxy integer equality add no mode under the strict brackets;
- both arguments include \(a=c/\varepsilon\), and both reserves stay
  positive there;
- \(\rho=39/50\) is included, whereas \(\rho=1\) is only the excluded
  zero-width limit.

For completeness, the exact prospective subtraction inherited through the
repaired predecessor is consistent. If the independently audited \(k_9\)
staircase were promoted, its high residual would be

\[
 \mathcal D_H^{(9)}=
 \{\rho_c\leq\rho<7/8,\ k_9(\rho)<K<U(\rho)\}.
\]

The new all-frequency theorem removes exactly the part with
\(39/50\leq\rho<7/8\), leaving

\[
 \{\rho_c\leq\rho<39/50,\ k_9(\rho)<K<U(\rho)\}.
\]

The face \(\rho=39/50\) belongs to the new theorem, \(K=k_9\) belongs to
the staircase, and \(K=U\) belongs to the inherited upper cover. Since

\[
 \rho_c<\frac17<\frac{39}{50}<\frac56,
\]

the remaining upper floor is entirely the central branch

\[
 \boxed{U(\rho)=K_0(\rho)
 \quad(\rho_c\leq\rho<39/50)}.
\]

Thus the seam branch is removed completely, with the correct endpoint
ownership. This is a conditional set subtraction only; it does not promote
either exploratory result.

## 7. Verdict

**PASS.** The strengthened uniform deficit is correct, its minimum is
strictly positive on every radial cell, both rational screen reserves
recompute exactly, and both screen monotonicities hold on the complete
\(0<\varepsilon\leq11/50\) range. The complementary-action estimate is
domain-free in \(\varepsilon\), the shared optical face and ratio endpoint
are owned, and the prospective subtraction leaves only the \(K_0\) branch.
No counterexample or unsupported implication was found. The result remains
exploratory until the repository's proof-free freeze and independent review
gates are completed.
