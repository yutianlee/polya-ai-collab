# Round 20 exploratory proof-set integrity audit

Date: 2026-07-14.

Status: **independent pre-freeze integrity audit**. This report does not
freeze, promote, or amend any mathematical claim.

## 1. Authenticated scope

The bytes actually audited were:

| artifact | independently recomputed SHA-256 |
|---|---|
| `rounds/polya-main/round_020/exploration/small-hole-wedge.md` | `f1e5ab1c3671e82257a78cd2855581f326e4df98385539a69dc4b1a295a7f43b` |
| `rounds/polya-main/round_020/exploration/lower-next-wall.md` | `94099e852274ac697fa8c60563fbcdb0c4bb91a40c3de2c0af7556cbf7754e0a` |
| `rounds/polya-main/round_020/exploration/lower-remaining-gap.md` | `0baea820115061f3dbd5d46c0ca48271dce2df50885c83d5cd3a83c176f6e9c6` |
| `rounds/polya-main/round_020/exploration/lower-closure-crosscheck.md` | `ffde9721e1b0f238ea74e1af069041498deb15481f950618a85c6b5f236624b7` |
| `rounds/polya-main/round_020/exploration/high-next-wall.md` | `d7bb58554cf7505bc18415415b1ab21fa233b1707d9685b0a48bb58bbb2ab8a2` |
| `rounds/polya-main/round_020/exploration/high-lorch-extension.md` | `30aea82a3278683bdaf0c8d98b24b82276568d5d42435841833d79f4670f811c` |
| `rounds/polya-main/round_020/exploration/high-closure-crosscheck.md` | `9ad5b481ec147896a2861e3e55441e4a4114b3517a8fdbabb00451016eaf0403` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |

Every dependency hash printed in these artifacts matches its current file.
The high cross-check hash is the post-repair value shown above; its current
bytes contain neither the earlier form-feed characters nor the earlier
malformed Bessel exponent.

All eight files are valid UTF-8 with LF line endings. An independent byte
scan found no control byte other than tab/newline, no DEL byte, and no
trailing whitespace. Display-math delimiters and Markdown fences are
balanced. No existing file was changed during this audit.

## 2. Source scope and exact-order algebra

The [SIAM publisher abstract](https://epubs.siam.org/doi/10.1137/0524050)
identifies \(j_{\nu,1}\) as the first positive zero of \(J_\nu\), gives
\(-1<\nu<\infty\), and prints the strict inequality

\[
 j_{\nu,1}^{\,2}>
 \frac{24(\nu+1)^2}
 {1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}-2(\nu^2-1).
 \tag{1}
\]

This independently confirms the statement-level payload in the source
card. The article body remains access-controlled, so neither the card nor
this audit claims a proof-level reconstruction of Lorch. The
[DLMF identity 10.47.3](https://dlmf.nist.gov/10.47.E3) supplies only the
positive-factor spherical/ordinary Bessel identification.

For \(\nu=\ell+1/2\), rationalization reconstructs

\[
 R_\ell=
 \frac{3(2\ell+3)\sqrt{(\ell+2)(\ell+6)}
       -2\ell^2+\ell+6}{4},
 \qquad j_{\ell+1/2,1}^2>R_\ell.
 \tag{2}
\]

The three declared reductions and their sign-safe certificates recompute:

\[
\begin{array}{c|c|c}
\ell&R_\ell&\text{strict rational consequence}\\ \hline
6&45\sqrt6-15&j_{13/2,1}>39/4\\
7&(153\sqrt{13}-85)/4&j_{15/2,1}>54/5\\
8&57(\sqrt{35}-1)/2&j_{17/2,1}>71/6,
\end{array}
\]

\[
240^2\!\cdot6-587^2=1031,\quad
3825^2\!\cdot13-13789^2=61604,\quad
1026^2\!\cdot35-6067^2=35171.
\]

Only the first two bounds are used through \(k_8\); the third is used in
the separate \(k_9\) method audit. Lorch is not used for a shell
cross-product zero, a second radial zero, a variational comparison, a
multiplicity, or a Weyl payment.

The separate internal shell transfers have the correct direction and keep
the same radial index:

\[
 q_{\ell,n}^{\rm shell}(\rho)^2\ge j_{\ell+1/2,n}^2,
 \qquad
 j_{p+1/2,n}^2\ge
 j_{\ell+1/2,n}^2+p(p+1)-\ell(\ell+1)
 \quad(p\ge\ell).
 \tag{3}
\]

A strict sourced lower bound remains strict after either non-strict form
comparison.

## 3. Lower-ratio reconstruction

Put

\[
 \rho_0=\frac1{\sqrt{337}},\qquad
 d=\frac{\sqrt{337}}2,\qquad
 \sigma=\frac{3\omega_0}{4},\qquad
 c_7=\sqrt{114},\qquad
 L(\rho)=\frac1{2\rho}.
\]

The accepted Round 19 lower residual is exactly

\[
\begin{aligned}
 \mathcal D_{19}^{\rm L}={}&
 \{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
 &\mathbin{\dot\cup}
 \{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}.
 \tag{4}
\end{aligned}
\]

The endpoint \(\rho=\rho_0\) belongs to the first set because
\(L(\rho_0)=d\) and the Round 19 candidate fiber there is empty.

### 3.1 Small-hole tail

The note reconstructs the pre-threshold split instead of extrapolating the
thresholded conclusion of `SHELL-low-interface-small-hole`. For a low
start \(x_r=r+1/2<\mu=\rho K\), set

\[
 n_r=\lfloor\mu-x_r\rfloor,\qquad q_r=x_r+n_r,\qquad
 p=\lfloor\omega_0K\rfloor.
\]

The audited split is

\[
 \frac{\mathcal T_r}{2}
 \le \int_{x_r}^{K}A_{\rho,K}(z)\,dz
 +\delta_r-\frac{p-n_r}{4},
 \qquad
 \delta_r=\int_{q_r}^{\mu}G_\mu(z)\,dz.
 \tag{5}
\]

Only \(\rho<1/2\), not \(\rho<\omega_0\), is needed for
\(q_r\le\mu<K/2\). The turning estimate gives the endpoint-valid bound

\[
 0\le\delta_r\le
 \frac{2}{15\sqrt\mu}(\mu-q_r)^{5/2}<\frac14.
 \tag{6}
\]

For \(\rho\le\sigma\), \(K>d\), and \(\rho K>1/2\), the exact
\(\omega_0d>1\) and \(\rho K\le3\omega_0K/4\) imply

\[
 \lfloor\omega_0K\rfloor
 \ge \left\lfloor\rho K-\frac12\right\rfloor+1
 \ge n_r+1.
 \tag{7}
\]

Thus every low tail is strict and the accepted convex theorem handles
every high start. This proves

\[
 \{\rho_*<\rho\le\rho_0,\ L<K<U\}
 \quad\text{and}\quad
 \{\rho_0<\rho\le\sigma,\ d<K<U\}.
 \tag{8}
\]

Equality at \(\rho=\sigma\) is valid in (7); the first set owns
\(\rho=\rho_0\), so no ratio slice is lost.

### 3.2 Finite next-wall band

The elementary spherical-Bessel recurrences independently reproduce

\[
 b_{6,1}>10,\qquad b_{3,2}>\frac{81}{8},\qquad
 b_{1,3}>\frac{21}{2}.
 \tag{9}
\]

The displayed \(\mathsf j_6,\mathsf j_3,\mathsf j_2\) sine/cosine
polynomials, tangent-cell signs, and zero numbering are correct.
Propagation through (3) gives

\[
 b_{7,1}^2>114,\quad b_{4,2}^2>7073/64,\quad
 b_{5,2}^2>114,\quad b_{2,3}^2>114.
 \tag{10}
\]

The six exhaustive caps through the included \(K=c_7\) face are

\[
45,\ 46,\ 59,\ 66,\ 69,\ 78.
\]

First modes above \(\ell=6\), second modes above \(\ell=4\), third modes
above \(\ell=1\), and every \(n\ge4\) mode are excluded. The exact moving
\(k_{0,3}=3z_\rho\) wall is split in the first row and conservatively
charged thereafter.

All Weyl payments recompute. In particular,

\[
 \mathcal W(\rho,c)>\frac{38}{539}c^3
 \quad(\rho<\rho_c),
\]

and the final cap-78 margin is

\[
 (38\cdot7073)^2 7073-(78\cdot539\cdot512)^2
 =47602399882532>0.
\]

Thus this note proves

\[
 \{\rho_0<\rho<\rho_c,\ d<K\le c_7\}.
 \tag{11}
\]

### 3.3 Remaining floor cells

For \(\sigma<\rho<\rho_c\) and \(K>c_7\), put

\[
 p=\lfloor\omega_0K\rfloor,\qquad
 m=\left\lfloor\rho K-\frac12\right\rfloor.
\]

Away from a half-integer interface, summing (5) over all low starts gives

\[
 \sum_r(p-n_r)=\frac{m+1}{2}(2p-m).
 \tag{12}
\]

At \(\rho K\in\mathbb Z+1/2\), the interface start is correctly assigned
to the high side, every remainder vanishes, and the sum is

\[
 \sum_r(p-n_r)=\frac m2(2p-m-1).
 \tag{13}
\]

Both ledgers work when \(m\le2p-1\). The exact
\(\rho_c/\omega_0<3/2\) proves this for every \(p\ge2\). For \(p=1\), the
only missed cell is

\[
 \mathcal B=\{\sigma<\rho<\rho_c,\ K>c_7,\
 \rho K\ge5/2,\ K<2/\omega_0\}.
 \tag{14}
\]

The face \(\rho K=5/2\) belongs to \(\mathcal B\); the face
\(K=2/\omega_0\) has \(p=2\) and belongs to the aggregate branch.

On \(\mathcal B\), the strict-phase proxy caps for
\(\ell=0,\ldots,14\) recompute as

\[
 (6,5,5,4,4,3,3,3,2,2,1,1,1,1,0).
\]

All fifteen exact margins are positive; the smallest is
\(M_{10}=176282\). Monotonicity after the zero row makes the inventory
exhaustive, its full multiplicity is \(395\), and

\[
 \mathcal W(\rho,K)>
 \frac{160293325}{378004}
 =424+\frac{19629}{378004}>395.
 \tag{15}
\]

Thus the aggregate and exceptional branches prove

\[
 \{\sigma<\rho<\rho_c,\ c_7<K<U(\rho)\}.
 \tag{16}
\]

### 3.4 Exact lower union

The exact residual allocation is

\[
\begin{aligned}
&\{\rho_*<\rho\le\rho_0,\ L<K<U\},\\
&\{\rho_0<\rho\le\sigma,\ d<K<U\},\\
&\{\sigma<\rho<\rho_c,\ d<K\le c_7\},\\
&\{\sigma<\rho<\rho_c,\ c_7<K<U\}.
\end{aligned}
\tag{17}
\]

The first set owns \(\rho_0\), the second owns \(\sigma\), and the third
owns \(K=c_7\). Together with the Round 19 \(L<K\le d\) face when it is
nonempty, (17) equals the whole lower part of (4). Therefore the
prospective Round 20 union genuinely leaves no residual for any
\(\rho<\rho_c\); the accepted outside-residual cover supplies the
complementary frequencies and \(0<\rho\le\rho_*\).

## 4. High-ratio reconstruction

The accepted high residual entering Round 20 is

\[
 \mathcal D_{19}^{\rm H}
 =\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
 \tag{18}
\]

The internal form comparison is

\[
 q_{\ell,n}^2\ge n^2z_\rho^2+\ell(\ell+1),
 \qquad q_{0,n}=nz_\rho.
 \tag{19}
\]

For \(K\le k_7\), (19), \(z_\rho>7/2\), and the internal
\(j_{5/2,2}>9\) argument give the exhaustive inventory

\[
 (\ell,1),\ 0\le\ell\le6;\qquad (0,2),(1,2).
 \tag{20}
\]

Every counted second mode forces \(\rho<3/10\). The fixed/moving splits
pay the complete caps \(25,26,29,36,40,49,53\), including every
simultaneous angular/radial case. The displayed rational payments and
large squared bridge reserves recompute. Hence the first new piece is

\[
 \{\rho_c\le\rho<7/8,\ k_6<K\le k_7\}.
 \tag{21}
\]

For \(K\le k_8\), (3) and (19) exclude every \(n\ge3\) mode, every first
mode with \(\ell\ge8\), and every second mode with \(\ell\ge4\). The
complete possible inventory is

\[
 (\ell,1),\ 0\le\ell\le7;\qquad
 (\ell,2),\ 0\le\ell\le3.
 \tag{22}
\]

The exact radial localizations are

\[
\begin{array}{c|c}
\text{counted category}&\text{necessary ratio range}\\ \hline
\text{some second mode}&\rho<3/8\\
(2,2)&\rho<1/3\\
(3,2)&\rho<3/10.
\end{array}
\]

A counted \((6,1)\) is incompatible with \((2,2)\) and \((3,2)\). The
cap table is exhaustive; its largest entries by first-mode row are
\(80,53,52,41\). The fixed-wall payments, increasing \(k_7\) payment,
and bridges at \(1/2\) and \(3/5\) all recompute with strict reserves.
No cap crosses a spectral wall without adding its full multiplicity.

The upper-floor comparison is also correct:

\[
 k_8<27<64<K_0
\]

before the seam, while the seam floor is at least \(1944\). Thus

\[
 k_8(\rho)<U(\rho)\qquad(\rho_c\le\rho<7/8),
 \tag{23}
\]

and the second new piece is

\[
 \{\rho_c\le\rho<7/8,\ k_7<K\le k_8\}.
 \tag{24}
\]

The face \(K=k_7\) belongs to (21), \(K=k_8\) belongs to (24), and strict
counting excludes the next angular entry on each moving upper face.
\(\rho_c\) is included; \(\rho=7/8\) retains its inherited owner.
Exact subtraction therefore leaves

\[
 \boxed{\mathcal D_{20}^{\rm H}
 =\{\rho_c\le\rho<7/8,\ k_8(\rho)<K<U(\rho)\}.}
 \tag{25}
\]

The cap-74 witness toward \(k_9\) is correctly labelled a method
obstruction, not a counterexample or part of the proved claim.

## 5. Verdict

The source payload is correctly scoped; exact-order algebra, form
directions, zero enumerations, inventories, multiplicities, Weyl
payments, floor cells, and equality owners all survive reconstruction.
The lower union closes the whole prospective residual below \(\rho_c\),
and the high union reaches the included \(k_8\) face with residual (25).
These remain exploratory conclusions: proof-free freezing, isolated
reconstruction, adversarial review of the frozen claim, and a judge are
still required before promotion.

**PASS.**
