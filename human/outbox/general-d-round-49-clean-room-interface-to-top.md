# Round 49 clean-room reconstruction: interface-to-top suffix

Date: 21 July 2026  
Role: Prompt B, clean-room derivation  
Pre-comparison verdict: **INCOMPLETE — SUBSTANTIVE STRUCTURAL PASS**

## 1. Independence boundary

The clean-room agent read the authoritative state, binding simplified
strategy, Round 47--48 independent audits, and the two certified Round 48
lemma packets. Before freezing this derivation it did not read:

- the Round 49 Prompt-A report;
- the Round 49 Prompt-A evaluator or replay;
- the Round 49 adversarial report; or
- the Round 49 adversarial evaluator.

The agent returned a read-only frozen artifact with SHA-256

    1e4a6b4f51ee5a8ee18379599d07a47084162d428ff65ac2f128b7376d6a1a3b

over its UTF-8/LF text. The rendered pre-comparison section below preserves
its mathematics and ordering. A separate file-prefix hash is recorded after
the freeze marker.

The completed \(d=3\) theorem remains proved_internal. The scoped \(d=4\)
aggregate remains proposed. The all-dimensional aggregate and
TARGET-shell-general-d remain unproved.

## 2. Domain and strict count

Let \(0<\rho<1\), \(K>0\), \(\mu=\rho K\), and

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi}
\]

on \(0\le z\le R\), with zero extension. Put \(A=G_K-G_\mu\) and

\[
 H=A(0)=\frac{K-\mu}{\pi}.
\]

Then \(A\) is continuous and strictly decreasing from \(H\) to \(0\).
For \(x\ge0\),

\[
 [x]_<:=\max\{0,\lceil x\rceil-1\}
\]

is the number of positive integers \(n<x\), including
\([m]_< =m-1\) at a positive integer \(m\).

Let \(\xi=A^{-1}\),

\[
 F(t)=\frac{\xi(t)^3}{3},\qquad
 t_n=n-\frac14,\qquad
 N_n=\lceil\xi(t_n)\rceil-1.
\]

Since

\[
 G_R(z)=\frac1\pi\int_z^R\arccos(u/R)\,du,
\]

Fubini gives

\[
 \int_0^Rz^2G_R(z)\,dz=\frac{R^4}{64}.
\]

Consequently

\[
 \int_0^HF(t)\,dt=\frac{K^4-\mu^4}{64},
\]

and strict layer exchange gives

\[
 \sum_{1\le a<K}a^2[A(a)+1/4]_<
 =
 \sum_{\substack{n\ge1\\t_n<H}}S_2(N_n).
 \tag{B2.1}
\]

Both statements retain literal ownership when \(\xi(t_n)\), \(K\), or
\(\mu\) is an integer.

## 3. Outer prefix and clipped suffix

Let

\[
 \tau=A(\mu),\qquad b=\lfloor\tau\rfloor.
\]

Since \(0<\tau<H\), every \(1\le n\le b\) is a complete full-outer cell,
including \(n=\tau\) when \(\tau\) is integral. Therefore

\[
\boxed{
 \mathrm{WT}_4
 =
 \sum_{n=1}^{b}L_n+\mathcal R_{\mathrm{suf}},}
\]

where

\[
 L_n=\int_{n-1}^{n}F-S_2(N_n)
\]

and

\[
 \mathcal R_{\mathrm{suf}}
 =
 \int_b^HF-
 \sum_{\substack{n\ge b+1\\t_n<H}}S_2(N_n).
 \tag{B3.1}
\]

The prefix is empty when \(b=0\).

Define

\[
 B(z)=(A(z)-b)_+,\quad
 \widehat H=H-b,\quad
 R=\xi(b),\quad
 \eta(s)=\xi(b+s).
\]

Then

\[
\boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^{\widehat H}\frac{\eta(s)^3}{3}\,ds
 -
 \sum_{\substack{k\ge1\\k-1/4<\widehat H}}
 S_2(\lceil\eta(k-1/4)\rceil-1),}
 \tag{B3.2}
\]

and, by counting pairs \((a,k)\),

\[
\boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^Rz^2B(z)\,dz
 -
 \sum_{1\le a<R}a^2[B(a)+1/4]_<.}
 \tag{B3.3}
\]

At the interface,

\[
 B(\mu)=\tau-b=:\beta\in[0,1).
\]

Moreover, \(R\in[\mu,K]\), \(R=\mu\) exactly when \(\tau\) is integral,
and \(R=K\) exactly when \(b=0\). Thus only the first normalized row can
contain the outer cap. If \(\beta=0\), it does not straddle. Every complete
row \(k\ge2\) is wholly inner. The nominal face \(R=0\) is impossible for a
nondegenerate shell because \(b\le\tau<H\), although the zero-support
identity is formally harmless.

## 4. Exact terminal ownership

Write

\[
 \widehat H=q+\alpha,\qquad
 q=\lfloor\widehat H\rfloor,\qquad0\le\alpha<1.
\]

For \(1\le k\le q\), set

\[
 M_k=\lceil\eta(k-1/4)\rceil-1.
\]

The only possible terminal node is at \(q+3/4\), and it is present exactly
when \(\alpha>3/4\). Hence

\[
\boxed{
\begin{aligned}
 \mathcal R_{\mathrm{suf}}
 &=
 \sum_{k=1}^{q}
 \left[
 \int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds-S_2(M_k)
 \right]+T_{\mathrm{top}},\\
 T_{\mathrm{top}}
 &=
 \int_q^{q+\alpha}\frac{\eta(s)^3}{3}\,ds
 -
 \mathbf1_{\{\alpha>3/4\}}S_2(M_*),\\
 M_*&=\lceil\eta(q+3/4)\rceil-1.
\end{aligned}}
 \tag{B4.1}
\]

At \(\alpha=3/4\), the node is excluded. At \(\alpha=0\), the top term is
zero. If \(q=0\) and \(\widehat H\le3/4\), there is no suffix node and the
suffix is the positive spatial integral.

## 5. Exact row cone and terminal row

For a complete row let

\[
 \omega_k(z)=\min\{1,\max\{0,B(z)-k+1\}\}.
\]

Then

\[
 \int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds
 =
 \int_0^Rz^2\omega_k(z)\,dz,
\]

and

\[
 S_2(M)=\int_{1/2}^{M+1/2}z^2\,dz-\frac{M}{12}.
\]

Therefore

\[
 L_k
 =
 \int_0^Rz^2
 \left(
 \omega_k-\mathbf1_{[1/2,M_k+1/2]}
 \right)dz+\frac{M_k}{12}.
 \tag{B5.1}
\]

For the top row put

\[
 \omega_*(z)=\min\{\alpha,\max\{0,B(z)-q\}\}.
\]

Its exact formula is

\[
\begin{aligned}
 T_{\mathrm{top}}
 &=
 \int_0^Rz^2
 \left(
 \omega_*(z)-
 \mathbf1_{\{\alpha>3/4\}}
 \mathbf1_{[1/2,M_*+1/2]}(z)
 \right)dz\\
 &\quad+
 \mathbf1_{\{\alpha>3/4\}}\frac{M_*}{12}.
\end{aligned}
 \tag{B5.2}
\]

Since \(\sum_{k=1}^{q}\omega_k+\omega_*=B\), the exact block is

\[
\boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^Rz^2K_B(z)\,dz
 +\frac1{12}
 \left(
 \sum_{k=1}^{q}M_k+
 \mathbf1_{\{\alpha>3/4\}}M_*
 \right),}
 \tag{B5.3}
\]

where

\[
 K_B(z)
 =
 B(z)
 -
 \sum_{k=1}^{q}\mathbf1_{[1/2,M_k+1/2]}(z)
 -
 \mathbf1_{\{\alpha>3/4\}}
 \mathbf1_{[1/2,M_*+1/2]}(z).
\]

No interface, top, ceiling, multiplicity, or \(M/12\) term is duplicated.

## 6. Independent weighted-trapezoid and Abel form

Zero extend \(B\) and put

\[
 m_a=[B(a)+1/4]_<.
\]

Because

\[
 \int_{a-1/2}^{a+1/2}z^2\,dz=a^2+\frac1{12},
\]

one has the exact identity

\[
\begin{aligned}
 \mathcal R_{\mathrm{suf}}
 &=
 \int_0^{1/2}z^2B(z)\,dz\\
 &\quad+
 \sum_{a\ge1}
 \int_{a-1/2}^{a+1/2}z^2(B(z)-m_a)\,dz
 +\frac1{12}\sum_{a\ge1}m_a.
\end{aligned}
 \tag{WT}
\]

Put \(\varepsilon_a=B(a)-m_a\). If \(m_a=0\), then
\(0\le\varepsilon_a\le3/4\); if \(m_a\ge1\), then
\(-1/4<\varepsilon_a\le3/4\). With

\[
 T_a=
 \int_{a-1/2}^{a+1/2}z^2(B(z)-B(a))\,dz,
\]

(WT) becomes

\[
\boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^{1/2}z^2B(z)\,dz
 +\sum_{a\ge1}
 \left(a^2\varepsilon_a+\frac{B(a)}{12}+T_a\right).}
 \tag{ABEL-R}
\]

Writing \(\sigma=-B'\) almost everywhere gives

\[
\begin{aligned}
 T_a
 &=
 \int_{a-1/2}^{a}
 \sigma(u)\left(\int_{a-1/2}^{u}z^2\,dz\right)du\\
 &\quad-
 \int_{a}^{a+1/2}
 \sigma(u)\left(\int_{u}^{a+1/2}z^2\,dz\right)du.
\end{aligned}
 \tag{B6.1}
\]

This is an Abel-in-radius reduction. It displays the correlated strict
sawtooth \(\varepsilon_a\) and asymmetric radial trapezoid \(T_a\);
neither has a fixed sign cell by cell.

## 7. Independently proved one-crossing theorem

On \(0<z<\mu\), put \(u=z/\mu\) and

\[
 \phi(x)=2\arcsin x-\frac{x}{\sqrt{1-x^2}}.
\]

Then

\[
 \pi Q(z)=\phi(u)-\phi(\rho u),\qquad
 Q=2\sigma-z\sigma',
\]

and

\[
 \phi'(x)=\frac{1-2x^2}{(1-x^2)^{3/2}}.
\]

For \(0<u\le1/\sqrt2\), \(\phi\) is increasing on
\([\rho u,u]\), so \(Q(z)>0\). For \(u>1/\sqrt2\), differentiate
\(q(u)=\phi(u)-\phi(\rho u)\). If \(\rho u\le1/\sqrt2\), then
\(q'(u)<0\). If \(\rho u>1/\sqrt2\), put

\[
 \psi(x)=-\phi'(x)=\frac{2x^2-1}{(1-x^2)^{3/2}}.
\]

Since

\[
 \psi'(x)=\frac{x(1+2x^2)}{(1-x^2)^{5/2}}>0,
\]

\[
 q'(u)=-\psi(u)+\rho\psi(\rho u)<0.
\]

Also \(q(1/\sqrt2)>0\) and \(q(u)\to-\infty\) as \(u\uparrow1\).
Thus \(Q\) has exactly one zero in \((\mu/\sqrt2,\mu)\), is positive
below it, and negative above it. Consequently

\[
 F''=\frac{zQ}{\sigma^3}
\]

has the corresponding one-crossing inner sign. This theorem does not by
itself sign the discrete block.

## 8. Deep-inner scope

The certified deep-inner lemma applies only to complete normalized rows
satisfying

\[
 b+k-1\ge t_*:=A(\mu/\sqrt2),
\]

including equality. It gives no sign for a partial radial cut, a
shallow/interface row, or \(T_{\mathrm{top}}\), even if part of that object
lies below \(\mu/\sqrt2\).

## 9. What \(\beta<1\) does and does not prove

Let \(\ell=\min\{1,\widehat H\}\). If \(\ell>3/4\), set

\[
 M_1=\lceil\eta(3/4)\rceil-1.
\]

The exact first-row object, complete or terminal, is

\[
 C_1=
 \int_0^Rz^2\min\{\ell,B(z)\}\,dz
 -
 \mathbf1_{\{\ell>3/4\}}S_2(M_1).
 \tag{B9.1}
\]

The inequality \(\beta=B(\mu)<1\) proves only interface confinement. It
does not alone prove \(C_1\ge0\). Indeed, for the non-shell monotone profile
with

\[
 c=\frac{301}{400},\qquad \mu_0=100,
\]

\[
 B_0(z)=
 \begin{cases}
 c,&0\le z\le100,\\
 c-(z-100)/2,&100\le z\le100+2c,\\
 0,&z\ge100+2c,
 \end{cases}
\]

one has \(B_0(\mu_0)=c<1\), \(\widehat H=c>3/4\),
\(\eta(3/4)=20001/200\), \(M_1=100\), and

\[
 \int_0^\infty z^2B_0(z)\,dz-S_2(100)
 =
 -\frac{3141007719378799}{38400000000}<0.
\]

This does not falsify the shell first-row statement; it proves that
\(\beta<1\) alone is localization, not compensation.

## 10. Exact failure of natural cumulative majorization

A natural strengthening of (WT) is

\[
 C_j(B):=
 \int_0^{j+1/2}z^2B(z)\,dz
 -
 \sum_{a=1}^{j}a^2m_a
 \ge0
 \quad(j\ge1).
 \tag{CM}
\]

(CM) is false on the exact strict-active shell domain. Take

\[
 \rho=\frac{49}{50},\qquad K=3000,\qquad\mu=2940.
\]

Activity follows from \(\pi<22/7\):

\[
 2500\pi^2+\frac34<9000000.
\]

With \(\delta=1/50\),

\[
 \tau=\frac{3000}{\pi}\int_0^\delta\arccos(1-y)\,dy.
\]

The elementary bounds

\[
 \sqrt{2y}\le\arccos(1-y)
 \le2\sqrt{\frac{y}{2-\delta}}
\]

give

\[
 \frac8\pi<\tau<\frac{80}{\pi\sqrt{99}},
\]

so \(2<\tau<3\) and \(b=2\).

For \(0\le z\le512\),

\[
 \arcsin(z/2940)-\arcsin(z/3000)
 \le
 \frac{z/147000}{\sqrt{1-(512/2940)^2}}.
\]

Using

\[
 \frac{333}{106}<\pi<\frac{22}{7},
\qquad
 \frac1{\sqrt{1-(512/2940)^2}}<\frac{41}{40},
\]

one obtains

\[
 B(512)>
 \frac{188}{11}
 -
 \frac{512^2}{294000}\frac{106}{333}\frac{41}{40}
 =
 \frac{5653835812}{336538125}
 >
 \frac{67}{4}.
\]

Hence \(m_a\ge17\) for every \(1\le a\le512\), so

\[
 \sum_{a=1}^{512}a^2m_a
 \ge17S_2(512)=762796800.
\]

Conversely, \(\arcsin x-\arcsin y\ge x-y\) gives

\[
 \sigma(z)\ge\frac{z}{147000\pi}.
\]

At \(x=1025/2\),

\[
\begin{aligned}
 \int_0^xz^2B(z)\,dz
 &\le
 \frac{20x^3-x^5/1470000}{\pi}
 -\frac{2x^3}{3}\\
 &<
 \left(20x^3-\frac{x^5}{1470000}\right)\frac{106}{333}
 -\frac{2x^3}{3}\\
 &=
 \frac{9518742846546875}{12531456}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 C_{512}(B)
 <
 -\frac{40211689593925}{12531456}<0.}
 \tag{B10.1}
\]

This is an exact analytic class-D counterexample to (CM), not a
counterexample to \(\mathcal R_{\mathrm{suf}}\), \(\mathrm{WT}_4\), or a
spectral theorem. It also shows why complete deep-inner row positivity
cannot be converted into arbitrary radial-prefix positivity.

## 11. Frozen clean-room verdict

The exact normalization, terminal ownership, row block, Abel form, and
one-crossing theorem are proved. The first attempted cumulative
majorization (CM) is exactly false. No replacement cumulative kernel
inequality controlling \(\varepsilon_a\) and \(T_a\) has been proved.

Therefore:

    PRE-COMPARISON VERDICT: INCOMPLETE
    R49: neither proved nor falsified
    R49-FB: neither proved nor falsified
    literal WT4: neither proved nor falsified
    one-crossing theorem: proved
    CM strengthening: exactly falsified
    no mathematical status change

<!-- ROUND49 CLEAN-ROOM PRE-COMPARISON FREEZE END -->

## 12. Rendered-prefix freeze hash

The SHA-256 of every byte from the start of this file through the freeze
marker line and its terminating LF is:

    f4fffae307a7258fa8dcccd4648006b49ceccf5b7e0742a5e25e4f60c5902c64

The original clean-room agent's independently frozen text hash remains the
separate value recorded in Section 1.

## 13. Post-comparison audit

### 13.1 Authorization and integrity

After the clean-room derivation was frozen, Prompt A supplied:

| artifact | SHA-256 |
|---|---|
| lead report | 7cd92a5e002c7d63c4ccbf01a57ceade6aa51b913fd1ecbddd2b76fbbed38b89 |
| lead evaluator | a1e5a09a99efd8d14c0dff56f0e07fbdb2de99d2902ae90522f643ee46c7892b |

The clean-room prefix above was not edited during comparison. Its rendered
prefix hash remains the value in Section 12; the independently supplied
agent-text hash remains the value in Section 1.

### 13.2 Line-by-line agreement

| Prompt-A result | frozen clean-room result | comparison |
|---|---|---|
| SPLIT | Sections 3--4 | Exact agreement, including \(b=0\), integral \(\tau\), and strict terminal ownership. |
| NSFX and SSFX | Section 3 | Exact agreement by independent pair counting. |
| IF | Section 3 | Exact agreement that only the first normalized row can straddle. |
| TOP | Section 4 | Exact agreement; \(\alpha=3/4\) excludes the node. |
| ROW1--ROW3 and block | Section 5 | Exact agreement on every occupancy, interval, and \(M/12\) correction. |
| one-crossing theorem | Section 7 | Formula-by-formula agreement through independent derivation. |
| deep-inner scope | Section 8 | Exact agreement that only complete rows satisfying the packet hypothesis are signed. |
| final sign | Section 11 | Agreement that R49, R49-FB, and literal WT4 remain open. |

### 13.3 Independent additions

Prompt A adds the exact composite Peano identity PBLOCK. It reduces the sign
to explicit boundary scalars and one composite curvature integral. The
clean-room derivation neither assumed nor reconstructed that identity before
freeze.

The final-review repair at the \(b=0\) inverse endpoint is compatible with
that comparison: \(\widehat F''\) alone need not be locally integrable, but
\(P_1(s)\widehat F''(s)=O(s^{2/3})\) is. The cutoff form of PBLOCK therefore
survives unchanged.

The clean-room derivation adds:

1. the exact weighted-trapezoid/Abel identity (ABEL-R);
2. an exact non-shell counterexample showing \(B(\mu)<1\) alone is not a
   first-row compensation theorem; and
3. the exact strict-active shell counterexample (B10.1) to cumulative
   majorization (CM).

The failure of (CM) does not contradict PBLOCK. It rejects one stronger
transport route only. In particular, it is not evidence that
\(\mathcal R_{\mathrm{suf}}<0\).

### 13.4 Endpoint reconciliation

Prompt A audits \(R=0\) as a formal clipped-support wall. The clean-room
derivation observes that it cannot occur for \(0<\rho<1\), because
\(b\le\tau<H\) implies \(R=\xi(b)>0\). These statements are compatible:
the formal identity has the correct zero value, while the shell domain never
reaches it.

Both derivations agree that:

- \(R=\mu\) at an integral \(\tau\);
- \(R=K\) when \(b=0\);
- an integral \(R\) is excluded from the strict spatial sum;
- a terminal node appears only for \(\alpha>3/4\); and
- the \(q=0\) interface/terminal object is one row, not two.

### 13.5 Post-comparison verdict

There is no contradiction requiring repair of either exact derivation.
Prompt A's PBLOCK and the clean-room ABEL-R identity are complementary
coordinate systems. The new theorem-strength information common to both is
the one-crossing curvature theorem. The natural cumulative-majorization
strengthening is now exactly rejected.

The final Prompt-B verdict is:

    INCOMPLETE — SUBSTANTIVE STRUCTURAL PASS
    exact suffix normalization: proved
    exact row and Abel blocks: proved
    one-crossing curvature theorem: proved
    natural cumulative majorization CM: falsified
    R49, R49-FB, and literal WT4: open
    no proof-obligation status change
