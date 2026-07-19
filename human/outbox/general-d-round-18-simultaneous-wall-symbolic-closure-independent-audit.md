# Independent audit: Round 18 simultaneous-wall symbolic closure

Date: 19 July 2026

Audited note:

human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure.md

SHA-256:

0F56DC67EE58D20601F1C1123BD265F4323D3DC009377FDD0BABFD1E5E713585

Audited replay:

computations/general_d_round18_simultaneous_wall_symbolic_replay.wl

SHA-256:

6EB326FEB37A8591C230D07160909B678CA9A19565DB78A33CF1329B838CCD3D

## 1. Verdict

**PASS.**

The note proves, on the literal simultaneous radial/action wall,

\[
 K_*=a_*+\pi,\qquad A(a_*-1)=\frac34,
\]

that

\[
 F(K_*,a_*)=F(a_*+\pi,a_*)>\frac12.
\]

All inequality directions, strict signs, alternating-series parities,
Machin bounds, rational square brackets, inverse-level comparisons, and the
final reserve check out independently.  A fresh Wolfram 15.0 kernel replay
returned

\[
 \texttt{round18ExactChecks=True},\qquad
 \texttt{round18ReplayOK=True}.
\]

The argument-order notation is consistent with Round 16's definition
\(F(K,a)\).  The note does not claim the Round 17 action-face payment,
WP2, the whole first-floor branch, the high-floor CST, or the
all-dimensional theorem.

## 2. Imported scalar and simultaneous-wall reduction

Round 16 defines

\[
 F(K,a)=J_K(x)-J_a(x)-(z-x),
\qquad A(x)=1,\qquad G_K(z)=\frac34.
\]

On \(K=a+\pi\),

\[
 A(0)=\frac{K-a}{\pi}=1.
\]

The shell action \(A\) is strictly decreasing for positive spatial
arguments, so the inverse level \(A(x)=1\) is owned literally by
\(x=0\), including the equality face.  Also

\[
 J_b(0)=\int_0^bG_b(s)\,ds=\frac{b^2}{8}.
\]

Consequently

\[
 F(K,a)=\frac{K^2-a^2}{8}-z
 =\frac{a\pi}{4}+\frac{\pi^2}{8}-z.
\]

This is exactly (1.3).  No open-face assertion \(x>0\) has been imported.

## 3. Monotonicity, existence, and uniqueness of the wall root

For \(s<b\), direct differentiation gives

\[
 \partial_bG_b(s)=\frac1\pi\sqrt{1-\frac{s^2}{b^2}},
 \qquad
 \partial_sG_b(s)=-\frac1\pi\arccos\frac{s}{b}.
\]

At \(t=a-1\), define

\[
 \gamma=\arccos\frac{t}{a+\pi},\qquad
 \phi=\arccos\frac{t}{a}.
\]

Both the radius and spatial argument have derivative one in each term of
\(H(a)=G_{a+\pi}(a-1)-G_a(a-1)\).  Therefore

\[
 H'(a)=
 \frac{(\sin\gamma-\gamma)-(\sin\phi-\phi)}{\pi}.
\]

In the relevant \(a>1\) domain,

\[
 0<\phi<\gamma<\frac\pi2.
\]

Since \(d(\sin u-u)/du=\cos u-1<0\), the displayed derivative is strictly
negative.  Thus \(H\) is continuous and strictly decreasing and can have at
most one root of \(H=3/4\).

The endpoint certificates audited below give

\[
 H(11/2)>\frac34,\qquad H(45/8)<\frac34.
\]

The intermediate value theorem and strict monotonicity therefore prove one
and only one wall point, with the strict bracket

\[
 \frac{11}{2}<a_*<\frac{45}{8}.
\]

The diagnostic root

\[
 a_*=5.5888726293276175674102100344\ldots
\]

lies strictly inside this exact bracket, but the decimal is not used in the
proof.

## 4. Alternating arctangent and Machin audit

For

\[
 T_n(x)=\sum_{j=0}^{n-1}\frac{(-1)^jx^{2j+1}}{2j+1},
\qquad 0<x<1,
\]

the first omitted term has sign \((-1)^n\).  Hence the parities in (3.2)
are correct:

\[
 T_{2m}(x)<\arctan x<T_{2m+1}(x).
\]

In particular,

- \(T_6\) is a strict lower bound;
- \(T_5\) and \(T_7\) are strict upper bounds;
- \(T_1\) is an upper bound and \(T_2\) a lower bound.

For \(u=\arctan(1/5)\), exact tangent doubling gives

\[
 \tan(2u)=\frac5{12},\qquad
 \tan(4u)=\frac{120}{119}.
\]

With \(v=\arctan(1/239)\),

\[
 \tan(4u-v)
 =\frac{120/119-1/239}{1+(120/119)(1/239)}=1.
\]

The angle \(4u-v\) lies in \((0,\pi/2)\), so
\(4u-v=\pi/4\).  Machin's identity is therefore used with the correct
branch.

To lower-bound \(\pi/4\), the proof lower-bounds the positive
\(4\arctan(1/5)\) term by \(4T_6(1/5)\) and upper-bounds the subtracted
term by \(T_1(1/239)\).  To upper-bound \(\pi/4\), it uses
\(4T_7(1/5)\) and subtracts the lower bound \(T_2(1/239)\).  Thus

\[
 M_-<\frac\pi4<M_+
\]

has the correct directions.  Exact recomputation gives

\[
 M_--\frac{333}{4\cdot106}
 =\frac{71255393653}{3428996484375000}
 >\frac1{100000},
\]

\[
 \frac{355}{4\cdot113}-M_+
 =\frac{4525115621373289}
 {67860769651479492187500}
 >\frac1{100000000}.
\]

Therefore the self-contained rational enclosure

\[
 \frac{333}{106}<\pi<\frac{355}{113}
\]

is proved without decimal input.

## 5. Common angle formula

Put

\[
 R=\sqrt{(a+\pi)^2-(a-1)^2},\qquad
 I=\sqrt{a^2-(a-1)^2}.
\]

All quantities are positive in the bracketed domain, and

\[
 \gamma=\frac\pi2-\arctan\frac{a-1}{R},
\qquad
 \phi=\arctan\frac{I}{a-1}.
\]

Substitution into
\(\pi H=(R-(a-1)\gamma)-(I-(a-1)\phi)\) gives exactly

\[
 \pi H(a)
 =R-I-\frac{(a-1)\pi}{2}
 +(a-1)\left(
 \arctan\frac{a-1}{R}
 +\arctan\frac{I}{a-1}
 \right).
\]

Every rational arctangent argument appearing in the certificates lies
strictly in \((0,1)\); the exact replay checks all five such inequalities.

## 6. Lower endpoint sign

At \(a_-=11/2\), the exact identities are

\[
 R^2=\pi^2+11\pi+10,\qquad I^2=10.
\]

The four rational square margins in (4.2)--(4.4) recompute exactly as

\[
 \frac{15607639}{2809000000},\quad
 \frac{24758449}{3192250000},\quad
 \frac{439}{250000},\quad
 \frac{4569}{1000000},
\]

all positive.  Since the outer radicand is increasing in \(\pi>0\), these
margins and the Machin bounds imply

\[
 r_-<R<r_+,\qquad i_-<I<i_+.
\]

Each replacement in the lower certificate has the correct direction:

- \(R\) is replaced by the lower \(r_-\);
- \(-I\) is replaced by \(-i_+\);
- \(-t\pi/2\) is replaced by \(-tp_+/2\);
- \(R<r_+\) makes \(t/R>t/r_+\);
- \(I>i_-\) makes \(I/t>i_-/t\);
- both arctangents are replaced by the lower polynomial \(T_6\).

Thus \(\pi H(a_-)>C_-\) strictly.  Independent exact evaluation gives

\[
 C_--\frac{3p_+}{4}
 =0.007208254409270587\ldots>\frac1{150}.
\]

This decimal only displays the exact rational checked by the replay.
Because \(p_+>\pi\),

\[
 \pi H(a_-)>\frac{3p_+}{4}>\frac{3\pi}{4},
\]

and hence \(H(11/2)>3/4\).

## 7. Upper endpoint sign

At \(a_+=45/8\), the four square margins in (5.2)--(5.4) are exactly

\[
 \frac{9139519}{2809000000},\quad
 \frac{2030584}{199515625},\quad
 \frac{3599}{1000000},\quad
 \frac{701}{250000},
\]

all positive.  They prove

\[
 \rho_-<R<\rho_+,\qquad
 \iota_-<I<\iota_+.
\]

For the upper certificate:

- \(R\) is replaced by the upper \(\rho_+\);
- \(-I\) is replaced by \(-\iota_-\);
- \(-t\pi/2\) is replaced by \(-tp_-/2\);
- \(R>\rho_-\) makes \(t/R<t/\rho_-\);
- \(I<\iota_+\) makes \(I/t<\iota_+/t\);
- both arctangents are replaced by the upper polynomial \(T_7\).

Therefore \(\pi H(a_+)<C_+\) strictly.  The exact rational replay gives

\[
 \frac{3p_-}{4}-C_+
 =0.0017422279236491115\ldots>\frac1{600}.
\]

Since \(p_-<\pi\),

\[
 \pi H(a_+)<\frac{3p_-}{4}<\frac{3\pi}{4},
\]

which proves \(H(45/8)<3/4\).

## 8. Inverse-level comparison and the bound for \(z\)

Set

\[
 K_0=\frac{45}{8}+\pi,\qquad s_0=\frac{101}{20}.
\]

The exact square margins

\[
 \frac{336031}{28090000},\qquad
 \frac{48642129}{3192250000}
\]

give

\[
 \sigma_-<R_0<\sigma_+.
\]

The upper comparison for \(\pi G_{K_0}(s_0)\) uses:

- \(R_0<\sigma_+\);
- \(-s_0\pi/2<-s_0p_-/2\);
- \(R_0>\sigma_-\), hence
  \(s_0/R_0<s_0/\sigma_-\);
- the odd truncation \(T_5\), which is an upper arctangent bound.

Thus

\[
 \pi G_{K_0}(s_0)<C_z.
\]

The exact rational margin is

\[
 \frac{3p_-}{4}-C_z
 =0.01408718106219678\ldots>\frac1{100}.
\]

It follows that \(G_{K_0}(s_0)<3/4\).

The wall bracket gives \(K_*=a_*+\pi<K_0\).  For fixed
\(s<K\),

\[
 \partial_KG_K(s)
 =\frac1\pi\sqrt{1-\frac{s^2}{K^2}}>0.
\]

Therefore

\[
 G_{K_*}(s_0)<G_{K_0}(s_0)<\frac34.
\]

Since \(G_{K_*}(s)\) is strictly decreasing in \(s\), while
\(G_{K_*}(z)=3/4\), the inverse comparison has the stated direction:

\[
 z<s_0=\frac{101}{20}.
\]

All comparisons are strict; no inverse-wall convention or numerical root is
needed.

## 9. Final rational reserve

Using \(a_*>11/2\), \(z<101/20\), and \(\pi>0\) in the exact scalar gives

\[
 F>
 \frac{11\pi}{8}+\frac{\pi^2}{8}-\frac{101}{20}.
\]

The polynomial \(\pi^2+11\pi\) is strictly increasing for positive
\(\pi\), so the lower Machin bound yields

\[
 F-\frac12>
 \frac{p_-^2+11p_--222/5}{8}.
\]

Direct rational simplification gives

\[
 \frac{p_-^2+11p_--222/5}{8}
 =\frac{1443}{449440}>0.
\]

This proves the strict theorem \(F(K_*,a_*)>1/2\).

## 10. Equality, dependencies, and claim scope

The equality and wall conventions are consistent:

1. \(K-a=\pi\) and \(A(a-1)=3/4\) are imposed as literal equalities.
2. The radial equality owns \(x=0\); no \(x>0\) open-face conclusion is
   used.
3. Both endpoint signs and the \(z\) comparison have explicit positive
   rational margins, so no equality is accidentally admitted.
4. The inverse \(G_K(z)=3/4\) is used only with strict spatial
   monotonicity.
5. No shelf floor, strict action count, or one-sided \(q=3\) chamber label
   is transferred to the simultaneous wall.

The dependency ledger is accurate.  The note imports only Round 16's
definition and boundary reduction for \(F\); all root, angle, and rational
certificates are proved in Round 18.  Its deliberate replacements of
\(a_*,K_*,z,\pi\) are all one-sided in the favorable direction and each is
followed by an exact positive reserve.

The status and gate paragraphs are appropriately limited.  They explicitly
leave open:

- the Round 17 action-face scalar \(\mathcal S>0\), or an equivalent proof
  of \(dF/da>0\) there;
- WP2 and the hard \(B=1\) first-floor branch;
- the high-floor CST;
- the all-dimensional theorem.

Thus the simultaneous-wall theorem is not used to overclaim action-face or
global closure.

## 11. Fresh-kernel replay

The replay was launched as a new process with

C:\Program Files\Wolfram Research\Wolfram\15.0\wolfram.exe

against the audited replay file.  It exited with code zero.  A second,
independent fresh-kernel invocation through math.exe with the -noinit and
-script flags also exited with code zero and produced the same results.  The
replay printed:

\[
 \texttt{round18PiLowerMargin}
 =\frac{71255393653}{3428996484375000},
\]

\[
 \texttt{round18PiUpperMargin}
 =\frac{4525115621373289}
 {67860769651479492187500},
\]

\[
 \texttt{round18FinalMargin}=\frac{1443}{449440},
\]

\[
 \texttt{round18ExactChecks=True}.
\]

The separate high-precision diagnostic returned

\[
 a=5.58887262932761756741021003440\ldots,
\]

\[
 K=8.73046528291741080587285341768\ldots,
\qquad
 z=4.99556078793775330256532386320\ldots,
\]

\[
 F=0.62763006073459526658299059956\ldots,
\]

with all four displayed residuals numerical zero at roughly 58--59 digits
of accuracy.  The bracket, \(z\), and \(F\) diagnostic gates passed, and the
script ended with

\[
 \texttt{round18ReplayOK=True}.
\]

The floating diagnostic is correctly separated from
\(\texttt{round18ExactChecks}\) and is not a premise of the proof.

## 12. Final disposition

- Simultaneous-wall reduction: **PASS**.
- Strict monotonicity and unique root: **PASS**.
- Alternating-series parities and Machin bounds: **PASS**.
- Lower and upper endpoint certificates: **PASS**.
- Inverse-level \(z\) comparison: **PASS**.
- Final reserve \(1443/449440\): **PASS**.
- Equality and wall conventions: **PASS**.
- Dependency and loss ledger: **PASS**.
- Action-face/WP2 status language: **PASS; both remain open**.
- Fresh-kernel exact replay: **PASS**.

No change was made to the audited note or replay.
