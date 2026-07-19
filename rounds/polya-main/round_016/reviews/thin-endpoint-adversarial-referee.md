# Round 16 thin-endpoint adversarial referee

## Verdict

**PASS.**

**First unsupported implication: none.** Working under the hostile
assumption that the proposed endpoint was false, I reconstructed both proof
pieces from the frozen packet and its five permitted inputs. The low
min--max/product route and the high complementary-action route both close on
their inclusive domains, preserve strictness for \(K>0\), and independently
own their common face. Their closed union proves exactly

\[
\boxed{
\frac78\le \rho<1,\qquad K\ge0,\qquad
N_D(A_{\rho,1},K^2)
\le \frac{2}{9\pi}(1-\rho^3)K^3 .
}
\]

At \(K=0\) both sides are zero. For every \(K>0\), the comparison obtained
before the final non-strict theorem statement is strict.

This PASS is a mathematical referee verdict on the frozen endpoint argument,
not authorization to alter accepted state. The all-ratio \(K=295^2\)
envelope remains conditional on endpoint promotion. The compact residual and
the full shell theorem remain open.

## 1. Isolation and exact artifact hashes

I first read only the six Round 16 artifacts named in the assignment. The
packet digest matched before the proof audit. Only after that initial read did
I inspect the two packet-whitelisted dependency files recorded in Section 2.
No Round 5, Round 6, Round 11, Round 15, judge, prompt, graph-state, source,
future-round, or other review content was opened. A filename-only
rg --files query was used to locate whitelisted packets; it read no other file
content.

| Audited Round 16 artifact | Bytes | SHA-256 |
|---|---:|---|
| state/lemma_packets/SHELL-rho-one-endpoint-round16.md | 20163 | 5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09 |
| rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md | 31197 | bc99a0e82bee9f55056e2122f053418b8b6f2586fad515dd115f6d29fb6878b0 |
| rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md | 28964 | 5a4945c267c0f9d769bec6cf94ad6f7cb3d17c5af593d1837d27553cefb197d7 |
| rounds/polya-main/round_016/exploration/thin-endpoint-constant-inventory.md | 19303 | 0aeb81f3186d7e8a3ef2d9623edc6bbfd6ab04744079dbc26bcc2b90e77df933 |
| computations/round16_verify_endpoint.py | 14955 | 7be9208c5abdb233db18c15dbae87068b134121ee5efcd3825ee293f346afff5 |
| computations/tests/test_round16_endpoint.py | 6451 | 4f372a5860ea33b19a80daadbb5ddd4382fb11be5e2f8f543a4fdd223a7d219c |

The primary digest is exactly the required
5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09.

### Blacklist audit

Every proof-artifact occurrence of Round 5, Round 6, Round 11,
\(\varepsilon=1/100\), \(\rho=99/100\), \(a=125\), or an old bridge scale
is an explicit exclusion, an included test face, or part of the separately
labelled conditional envelope. None supplies an implication in the two new
proof pieces.

The decreasing semicircle *summand* used to bound \(\sum b_n\) is an
elementary quadrature estimate and is not the forbidden global pointwise
comparison \(\mathcal A\le\mathcal B\). No Round 6 aggregate conclusion, old
three-slab estimate, old endpoint, or old \(P_{\mathcal A}<I\) conclusion
entered the reconstruction.

## 2. Exact dependency log

These are the only dependency files whose content I inspected after the six
initial artifacts:

| Whitelisted dependency inspected | Bytes | SHA-256 | Purpose |
|---|---:|---|---|
| state/lemma_packets/SHELL-sturm-liouville-completeness.md | 8442 | 6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8 | Verify that the direct sum, positivity, radial simplicity, multiplicity \(2\ell+1\), finiteness, and strict separated count are all-domain statements for \(0<\rho<1\). |
| state/lemma_packets/SHELL-phase-enclosures.md | 2322 | 96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf | Verify the global phase enclosure, strict upper proxy wall, mixed-region restriction, and strict radial count. |

The five-input ledger is:

1. CONV-strict-counting and the separated shell spectrum are used only for
   \(\lambda<K^2\), the direct-sum count, and exclusion of equality walls.
2. SHELL-sturm-liouville-completeness was inspected as logged; no
   domain-sensitive endpoint estimate is imported from it.
3. The radial min--max direction is rederived directly from the common form
   domain and \(r^{-2}\ge1\); no separate file was needed.
4. SHELL-phase-enclosures plus SHELL-annulus-phase-transfer enter only through
   the all-domain proxy inequality (N3) expressly granted in the Round 16
   packet. The phase packet was inspected; no separate transfer file was
   opened.
5. The domain-free identities (N1)--(N2) are rederived below.

No Round 15 file was opened. The accepted boundary facts recorded in the
frozen Round 16 packet are used only in Section 11.

## 3. Target normalization

Put

\[
\rho=1-\varepsilon,\qquad a=\varepsilon K,\qquad
m_\varepsilon=1-\varepsilon+\frac{\varepsilon^2}{3}.
\]

Then

\[
1-\rho^3=3\varepsilon m_\varepsilon,\qquad
\frac{2}{9\pi}(1-\rho^3)K^3
=\frac1{\varepsilon^2}\frac{2a^3}{3\pi}m_\varepsilon.
\]

This owns \(a=K=0\): positivity gives a zero strict spectral count and the
volume side is zero. Every later division by \(a\) occurs only for \(a>0\).

## 4. Numbered reconstruction table

| No. | Label | Hostile reconstruction | Result |
|---:|---|---|---|
| 1 | (N1) | For \(z=\mathcal A(y_\ell)+1/4\), \([z]_< =\lceil z\rceil-1=\#\{n\ge1:n-1/4<\mathcal A(y_\ell)\}\). At \(z=m\in\mathbb Z\), layer \(m\) is excluded. Extending \(\mathcal A=0\) for \(y>a\) makes the sum finite. | PASS |
| 2 | (N2), discrete | Strict finite layer-cake interchange and \(\sum_{\ell=0}^{M-1}(\ell+1/2)=M^2/2\) give \(P_{\mathcal A}=\frac{\varepsilon^2}{2}\sum_{x_n<T}M_\varepsilon(R(x_n))^2\). The terminal layer \(x_n=T\) is excluded. | PASS |
| 3 | (N2), continuous | From \(\mathcal A(y)=\frac1{\pi\varepsilon}\int_\rho^1\sqrt{a^2-y^2/r^2}_+\,dr\), inverse-area/Tonelli gives \(\frac12\int_0^T R(t)^2dt=\int_0^a y\mathcal A(y)dy=\frac{a^3}{3\pi}m_\varepsilon\). | PASS |
| 4 | (N3) | The inequality \(N_D\le2P_{\mathcal A}/\varepsilon^2\) is exactly the permitted all-domain transfer, with the strict bracket from (N1). Row 3 gives \(2I/\varepsilon^2=\frac{2}{9\pi}(1-\rho^3)K^3\). No old \(P_{\mathcal A}<I\) is imported. | PASS as permitted input plus exact normalization |
| 5 | (P1) | On \(H_0^1(\rho,1)\), \(L_\ell\ge-d^2/dr^2+\ell(\ell+1)\), so min--max gives an upper count. The active conditions are \(n\pi<a\) and \(\ell(\ell+1)<b_n^2/\varepsilon^2\); the multiplicities sum to \(M_n^2\). | PASS |
| 6 | (P2) | With \(I_0=2a^3/(3\pi)\), \(S_0=\sum_{n=1}^N(a^2-n^2\pi^2)\), and \(D=I_0-S_0\), all sums are finite and every included radicand is positive because \(n\le N<a/\pi\). | PASS |
| 7 | (P3) | For \(a>\pi\), \(N=\lceil a/\pi\rceil-1\ge1\) and \(t=a/\pi-N\in(0,1]\). At \(a=m\pi\), uniquely \((N,t)=(m-1,1)\), not \((m,0)\). | PASS |
| 8 | (P4) | Expanding \(\frac23(N+t)^3-N(N+t)^2+N(N+1)(2N+1)/6\) gives \(N^2/2+N(t^2+1/6)+2t^3/3\). At \(a=m\pi\), \((m-1,1)\) and the right limit \((m,0+)\) both give \(m^2/2+m/6\). | PASS |
| 9 | (P5) | Row 10 makes \(D/a^2-2/5\) strictly positive for every integer \(N\ge1\), so \(D>(2/5)a^2\) for all \(a>\pi\), not merely sampled points. | PASS |
| 10 | (P6) | \(h(t)=2t^3/3-2t^2/5\) has \(h'(t)=2t(t-2/5)\), unique minimum \(-8/375\), and the integer lower screen is smallest at \(N=1\), where it equals \(32/375>0\). | PASS |
| 11 | (P7) | Strict ceiling and decreasing-sum bounds give \(\varepsilon^2\mathcal P_\varepsilon<S_0+\varepsilon a^2/4+\varepsilon^2a/\pi\). Under (P7), this is at most \(I_0(1-\varepsilon)<I_0m_\varepsilon\). The direction is correct. | PASS |
| 12 | (P8) | On \(a\le\pi/(4\varepsilon)\), \(2\varepsilon a/(3\pi)\le1/6\); on \(a\ge\pi\), \(\varepsilon^2/(\pi a)<\varepsilon^2/9\). Thus the normalized cost is at most \(1/6+\varepsilon/4+\varepsilon^2/9\), increasing in \(\varepsilon\). | PASS |
| 13 | (P9) | At \(\varepsilon=1/8\), \(2/5-(1/6+1/32+1/576)=577/2880>0\). With (P5), this proves (P7), including the low common face. | PASS |
| 14 | (H1) | Since \(J_r'(y)=-\arccos(y/(ar))\), the two action formulas and their first derivatives agree at \(y=\rho a\). The action decreases continuously from \(T=a/\pi\) to zero, so \(R:[0,T]\to[0,a]\) exists and decreases. | PASS |
| 15 | (H2) | On the outer branch, \(g=2\pi\varepsilon y/\alpha\), \(\alpha=\arccos(y/a)\), and \(y/\alpha\) increases with \(y\), so \(g\) decreases with \(t\). On the inner branch, \(\delta/y=\int_\rho^1[r\sqrt{a^2r^2-y^2}]^{-1}dr\) increases with \(y\), so \(g=2\pi\varepsilon y/\delta\) increases with \(t\). | PASS |
| 16 | (H3) | \(F(0)=a^2\), \(F(\tau)=\rho^2a^2\), \(F(T)=0\). Since \(\delta(y)=\varepsilon y/(\rho a)+O(y^3)\), \(g(T)=2\pi\rho a\). At \(t\downarrow0\), \(t\asymp\theta^3\) and \(g\asymp t^{-1/3}\), so \(g\) is integrable and \(Wg\to0\). | PASS |
| 17 | (H4) | For \(C(t)=\#\{x_n<t\}\), \(w=t-C\), and \(\Psi=W-t/4\), exact one-period integration gives \(-1/32\le\Psi\le3/32\) and \(W\ge0\). The primitives are continuous across every sawtooth jump. | PASS |
| 18 | (H5) | \(D_{\rm rad}=\int_0^T wg\). On \((0,\tau)\), \(dg\le0\) and \(W\ge0\), so \(-\int W\,dg\ge0\). On \((\tau,T)\), \(dg\ge0\) and the \(\Psi\) bounds give \(D_{\rm rad}\ge F(\tau)/4-g(T)/8=\rho^2a^2/4-\pi\rho a/4\). | PASS |
| 19 | (H6) | \(M_\varepsilon(x)=\max\{0,\lceil x/\varepsilon-1/2\rceil\}\). At \(x/\varepsilon=m+1/2\), it equals \(m\), excluding \(\ell=m\). | PASS |
| 20 | (H7) | \(J_{\rm rad}=\lceil T+1/4\rceil-1<T+1/4=a/\pi+1/4\). At \(T=n-1/4\), \(J_{\rm rad}=n-1\), excluding the equality layer. | PASS |
| 21 | (H8) | For included \(x=R(x_n)>0\), \(M_\varepsilon(x)<x/\varepsilon+1/2\), hence \(\varepsilon^2M^2<x^2+\varepsilon x+\varepsilon^2/4\le x^2+\varepsilon a+\varepsilon^2/4\). Summation and strict (H7) give the displayed strict error \(E\). | PASS |
| 22 | (H9) | From \(a\ge\pi/(4\varepsilon)\), \(\rho^2/4-\pi\rho/(4a)\ge\rho^2/4-\rho\varepsilon=(1-\varepsilon)(1-5\varepsilon)/4\). Its derivative is negative on the full domain, and its endpoint value is \(21/256\). | PASS |
| 23 | (H10) | Expanding \(E/a^2\) and applying \(1/a\le4\varepsilon/\pi\) termwise gives \(U=(\varepsilon+\varepsilon^2)/\pi+(\varepsilon^3+\varepsilon^4)/\pi^2\), with \(U'>0\). The scaling is equality, correctly non-strict, exactly at the common face. | PASS |
| 24 | (H11) | At \(\varepsilon=1/8\), strict \(\pi>3\) gives \(U<193/4096\), while (H9) gives at least \(21/256\). The exact reserve is \(143/4096>0\). | PASS |
| 25 | (H12) | \(D_{\rm rad}>E\) is precisely \(\sum F+E<\int F\). With strict (H8), this gives the full two-step strict chain. By (N2), \(P_{\mathcal A}<I\), and then (N3) proves the high piece. | PASS |
| 26 | (S1) | \(R_P(1/7)=1723/8820\) and \(R_H(1/7;3)=139/21609\), both positive. These are planning screens only. | PASS |
| 27 | (S2) | \(R_P(4/27)=12719/65610\) and \(R_H(4/27;333/106)=162570113/235723844196\), both positive. They do not move the endpoint. | PASS |
| 28 | (S3) | \(R_H(3/20;333/106)=-44729/20535000<0\). This obstructs only the chosen coarse screen, not the spectrum. | PASS |
| 29 | (S4) | \(R_H(1/6;333/106)=-3983743/143712144<0\), with the same limited interpretation. | PASS |
| 30 | (C1) | Conditional on endpoint promotion, the four recorded bands leave residual ceilings \(64\), \(K_0(5/6)<295^2\), \(3456\), and none on \([7/8,1)\). Thus the equality face \(K=295^2=87025\) is covered. | PASS, conditional only |
| 31 | (C2) | \(200000/295^2=8000/3481=2+1038/3481>2\). | PASS, conditional arithmetic only |
| 32 | Closed union | \([0,\pi/(4\varepsilon)]\cup[\pi/(4\varepsilon),\infty)=[0,\infty)\), and both proofs include the common face. There is no third interval and no imported bridge. | PASS |

## 5. The two hostile implication checks

### 5.1 Low min--max and rounding direction

On the common form domain,

\[
\int_\rho^1\left(
|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2
\right)dr
\ge
\int_\rho^1\left(
|u'|^2+\ell(\ell+1)|u|^2
\right)dr .
\]

Larger operators have no more eigenvalues below a fixed strict threshold, so
the direction is \(N_D\le\mathcal P_\varepsilon\). For
\(B=b_n/\varepsilon>0\),

\[
M_n<\sqrt{B^2+\frac14}+\frac12,\qquad
\varepsilon^2M_n^2
<b_n^2+\varepsilon b_n+\varepsilon^2 .
\]

Because \(x\mapsto\sqrt{a^2-\pi^2x^2}\) is strictly decreasing,

\[
\sum_{n=1}^N b_n<\frac{a^2}{4},\qquad N<\frac a\pi .
\]

Therefore

\[
\varepsilon^2\mathcal P_\varepsilon
<S_0+\frac{\varepsilon a^2}{4}
+\frac{\varepsilon^2a}{\pi}.
\]

Substitution of (P7) makes the right side at most
\(I_0(1-\varepsilon)\), strictly below \(I_0m_\varepsilon\). No sign
reverses, and strictness survives every radial and angular equality wall.

### 5.2 Improper trace and H5 direction

At the outer endpoint write \(y=a\cos\theta\). Then

\[
t=\frac{a}{\pi\varepsilon}
(\sin\theta-\theta\cos\theta)
\sim\frac{a\theta^3}{3\pi\varepsilon},
\qquad
g\sim\frac{2\pi\varepsilon a}{\theta}
=O(t^{-1/3}).
\]

Since \(w(t)=t\) and \(W(t)=t^2/2\) near zero,

\[
wg=O(t^{2/3}),\qquad
Wg=O(t^{5/3})\longrightarrow0.
\]

This justifies the improper integration by parts. Splitting at the actual
ungridded \(\tau\),

\[
\int_0^\tau wg
=W(\tau)g(\tau)-\int_0^\tau W\,dg
\ge W(\tau)g(\tau)
\]

because \(dg\le0\). On the increasing side, \(w=1/4+\Psi'\). Cancellation of
the \(\Psi(\tau)g(\tau)\) interface term gives

\[
D_{\rm rad}\ge
\frac{F(\tau)}4+\frac{\tau g(\tau)}4
+\Psi(T)g(T)-\int_\tau^T\Psi\,dg .
\]

Using \(\Psi(T)\ge-1/32\), \(\Psi\le3/32\), and \(dg\ge0\),

\[
D_{\rm rad}\ge
\frac{F(\tau)}4-\frac{g(T)}8
+g(\tau)\left(\frac\tau4+\frac3{32}\right)
\ge
\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\]

Both discarded terms have nonnegative signs. This works with \(\tau\) below,
on, or above every sawtooth grid point and never assumes \(\tau>1\).

## 6. Strict branches, walls, endpoints, and faces

1. **Zero and positive energy.** \(K=a=0\) gives equality \(0=0\). Every
   \(K>0\) path has a strict product or action comparison before transfer.
2. **Zero range and first product branch.** For \(0\le a\le\pi\), including
   both endpoints, no \(n\ge1\) satisfies \(n\pi<a\). The
   \(n=1,\ell=0\) branch appears only for \(a>\pi\).
3. **Every product radial wall.** At \(a=m\pi\), level \(n=m\) is excluded
   and \((N,t)=(m-1,1)\). The left limit has \(t\uparrow1\); the right limit
   has \((N,t)\to(m,0+)\); (P4) has the same value on both sides.
4. **Every product angular wall.** If
   \(b_n^2/\varepsilon^2=L(L+1)\), then \(M_n=L\), level \(\ell=L\) is
   excluded, and the jump of multiplicity \(2L+1\) occurs only above the
   wall. For \(b_n>0\), \(\ell=0\) is the first branch.
5. **Shared optical face.** Both pieces include
   \(a=\pi/(4\varepsilon)\). At
   \((\varepsilon,a)=(1/8,2\pi)\), the low convention is
   \((N,t)=(1,1)\). H9 and H10 have their allowed scaling equalities, while
   final reserves remain strict.
6. **Ratio and test faces.** The closed face \(\varepsilon=1/8\), or
   \(\rho=7/8\), is proved. The limit \(\varepsilon\downarrow0\) is open and
   \(\varepsilon=0\) is never used. The faces
   \(1/100,1/25,1/10,1/8\) lie in one monotonic proof and import no legacy
   conclusion.
7. **Action radial walls.** At \(x_n=T\), the \(n\)-th layer is excluded.
   Because \(F(T)=0\), no endpoint mass is hidden. On the high piece
   \(T\ge2\), so the first positive action layer \(x_1=3/4\) is present.
8. **Half-integer walls.** If
   \(R(x_n)/\varepsilon=m+1/2\), then \(M_\varepsilon=m\), excluding
   \(\ell=m\). The \(m=0\) branch enters only above the first wall.
9. **Phase-proxy walls.** If
   \(\mathcal A(y_\ell)+1/4=m\in\mathbb Z\), then \(q_\ell=m-1\). This is
   exactly the strict bracket required by the phase transfer.
10. **Action endpoints and interface.** At \(y=a\), \(\mathcal A=0\) and
    the proxy count is zero. At \(y=\rho a\), \(\mathcal A\),
    \(\mathcal A'\), \(R\), \(F\), and \(g\) are continuous. Curvature
    changes at the actual \(t=\tau\), not at a grid surrogate.
11. **Sawtooth placement.** \(W\) and \(\Psi\) remain continuous when
    \(\tau\) is below, on, or above any \(x_n\). The point value of \(w\) at
    a jump is immaterial; the one-sided values are \(3/4\) and \(-1/4\).
12. **Improper and terminal traces.** The \(t=0\) trace follows from the
    \(t^{-1/3}\) asymptotic. At \(T\), \(F(T)=0\) and
    \(g(T)=2\pi\rho a\). Every discarded Stieltjes term is displayed with
    its nonnegative sign.
13. **Legal domains and operations.** \(R\) has exact domain \([0,T]\) and
    range \([0,a]\). Radicands are nonnegative, arccosine arguments lie in
    \([0,1]\), open-interval denominators are positive, endpoint zeros are
    handled by limits, and every squaring compares nonnegative quantities.
14. **Monotonic reductions.** The P8 coefficient increases in
    \(\varepsilon\); the H9 lower screen decreases; the H10 upper screen
    increases. H10 is deliberately non-strict at the common face. Final
    strictness comes from \(\pi>3\) and the positive reserve.
15. **Conditional interfaces.** The separate envelope owns
    \(\rho=\rho_*,1/16,5/6,7/8,99/100\) and
    \(K=64,3456,K_0(5/6),295^2,200000\). The accepted equality thresholds
    \(54/\varepsilon^2\), \(32/\varepsilon^2\),
    \(24/\varepsilon^2\), and \(20/\varepsilon^2\) remain restricted to
    exactly the packet-recorded domains.

## 7. Six mandatory replacements

| Replacement | Audit result |
|---:|---|
| 1 | The proof uses global \(W\ge0\), the actual \(\tau\), and the improper trace. No \(\tau>1\) or first-cell exception occurs. |
| 2 | H8 uses only \(J_{\rm rad}<a/\pi+1/4\). No \(a\ge125\) or low-layer shortcut occurs. |
| 3 | H9 substitutes exactly \(\rho=1-\varepsilon\), not \(\rho\ge99/100\). |
| 4 | The high reserve is exactly \(143/4096\), not \(61/1400\). |
| 5 | The low proof uses \(0\le a\le\pi\) as the exact zero range and \(D>(2/5)a^2\), not the old three-slab estimate. |
| 6 | The two inclusive pieces alone cover \(a\ge0\). No Round 6 aggregate theorem or bridge enters. |

## 8. Independent-proof agreement and repaired editorial defects

The incumbent and clean-room proofs agree on every substantive implication.
Their independent high-side work is recognizable:

- the incumbent proves the inner curvature sign through monotonicity of the
  integral for \(\delta/y\), while the clean-room proof uses
  \(\delta''>0\) and \(y\delta'-\delta>0\);
- the incumbent derives normalization from an \(r\)-integral and Tonelli,
  while the clean-room proof uses inverse substitution and
  \(\int_0^1u^2\arccos u\,du=2/9\);
- their Stieltjes presentations organize the \(\tau\)-interface terms
  differently but reduce to the same \(F(\tau)/4-g(T)/8\) bound.

The initial audit found two non-substantive display defects:

1. thin-endpoint-clean-room.md, lines 165--166, lacked the printed plus sign
   before \(N(N+1)(2N+1)/6\) in one pre-expansion P4 display.
2. thin-endpoint-incumbent.md, line 948, contained a form-feed character in
   place of the backslash and letter f in one later fraction command.

Both defects are now repaired. The clean-room display contains
\(+N(N+1)(2N+1)/6\), and the incumbent display contains the valid fraction
command. Exact byte reversal proves that these were the only changes:

- replacing the repaired incumbent sequence by the former form-feed sequence
  reconstructs a 31,196-byte file with SHA-256
  a2ffd06dc6ca90d04eb028e397c250ad271b4e4f99f2b4841dcfb414f9e0ef39,
  exactly the pre-repair incumbent;
- removing only the inserted clean-room plus sign reconstructs a 28,963-byte
  file with SHA-256
  3381ffbc1bb7466a64dcabcc8b05427fc0a2a20d62529f177bbd1e716cd37a61,
  exactly the pre-repair clean-room artifact.

The repaired files are respectively one byte longer and have the new hashes
in Section 1. Because each in-memory reverse edit reproduces the complete
prior SHA-256, there was no other byte or semantic-text change. The repairs
remove the two editorial qualifications without changing any proof
implication. The independent mathematical proofs still agree.

The constant inventory also limits its own status correctly: it verifies
finite algebra and dependency directions but does not claim to prove
min--max, curvature, the inverse, the improper trace, Stieltjes integration,
or phase transfer.

## 9. Explicit post-repair gate

**POST-REPAIR GATE: PASS.**

1. All six audited inputs were reopened in full.
2. The packet, constant inventory, verification program, and test file retain
   exactly their pre-repair byte counts and SHA-256 values.
3. The incumbent and clean-room files have exactly the two announced new
   hashes and are each one byte longer.
4. Reversing only the intended repair in each file reproduces its exact prior
   byte count and SHA-256, proving that no other byte changed.
5. The repaired P4 displays now agree literally with the analytic derivations,
   independent constant ledger, verification program, and tests.
6. The 111 exact checks and 11 unit tests pass after repair.
7. The referee verdict remains **PASS**, and the first unsupported implication
   remains **none**.

## 10. Executable rerun

The checks were rerun with bytecode generation disabled:

~~~text
python -B computations/round16_verify_endpoint.py
PASS: 111 exact finite checks
packet_sha256=5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09
analytic_theorem_verified=false
These checks verify finite algebra, not the Round 16 analytic theorem.
~~~

~~~text
python -B -m unittest computations.tests.test_round16_endpoint -v
Ran 11 tests in 0.002s
OK
~~~

**These finite checks are not the analytic proof.** They do not establish
P1's operator comparison, N3's spectral transfer, H1--H3's inverse and
curvature, the improper \(t=0\) trace, or H5's Stieltjes integration. Those
implications were audited analytically in Sections 4--5. The finite suite
correctly prints analytic_theorem_verified=false.

## 11. Conditional-envelope audit

This section is downstream of, and does not feed into, the endpoint proof.
Using only accepted context recorded in the frozen packet,

\[
0<\rho_*<\frac1{16}<\frac56<\frac78<\frac{99}{100}<1.
\]

Positivity follows from \(\pi<3\sqrt3\). For the upper bound, \(\pi>3\) and
\(\sqrt3<7/4\) give
\(\omega_0<(\sqrt3-1)/6<1/8\), while \(1+2C_*>2\); hence
\(\rho_*<1/16\). Conditional on endpoint promotion, the recorded residuals
are exactly:

1. \([\rho_*,1/16]\): \(K<64\);
2. \([1/16,5/6]\): \(K<K_0(5/6)<295^2\);
3. \([5/6,7/8]\): \(K<54/(1-\rho)^2\le3456\);
4. \([7/8,1)\): no residual frequency.

Together with the accepted all-frequency range below \(\rho_*\), these cover
the equality face \(K=295^2=87025\) on every ratio band because
\(87025>3456>64\) and \(K_0(5/6)<87025\). To prevent a notation error: the
accepted statement is \(K_0(5/6)<295^2\); \(295^2\) is the prospective
uniform cutoff, not an equality \(K_0(5/6)=295^2\).

Consequently (C1)--(C2) are correct only as conditional consequences. The
endpoint \([7/8,1)\) is the only new all-frequency band. This report does not
promote

\[
0<\rho<1,\qquad K\ge295^2,
\]

does not replace the true residual by a rectangle, does not close
SHELL-rho-compact, SHELL-rho-uniformity, or TARGET-shell-d3, and does not
promote COMP-certified-bessel beyond diagnostic_only.

## 12. Final conclusion

No smaller fallback domain is required. Relative to the frozen packet's five
permitted inputs, the strongest exact endpoint proved is precisely

\[
\boxed{\frac78\le\rho<1,\qquad K\ge0,}
\]

with equality at \(K=0\) and strict comparison at \(K>0\). The first
unsupported implication is **none**. Exact arithmetic, strict walls, the
improper trace, H5/H8 directions, six replacements, common-face ownership,
the closed two-piece union, and conditional-envelope bookkeeping all pass.
State promotion remains a separate gate outside this report.
