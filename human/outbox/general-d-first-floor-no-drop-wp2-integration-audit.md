# Independent integration audit: first-floor no-drop WP2

Date: 19 July 2026

## 1. Verdict

**PASS.**  The analytic results through Round 19 form an exhaustive and
wall-safe proof of the first-floor no-drop obligation on every new active
integer and half-integer extension grid.

More precisely, the proved conclusion is

\[
 D_A(r)>0
\]

for every spectrally active first-floor no-drop shifted tail with
\(n\geq1\) on

\[
 r\in\mathbb N,\quad r\geq1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\quad r\geq\frac32.
\]

The case \(n=0\) is the previously completed one-interface theorem.  These
three statements together close WP2 on all new \(d\geq4\) extension
obligations.  The completed three-dimensional theorem remains the separate
base owner; the present chain is not used to replace it.

No uncovered \(B\)-phase, floor wall, inverse wall, branch wall, or
dimension-labelled activity wall was found.  One domain implication was
implicit in the Round 16 boundary discussion: the auxiliary condition
\(z>2\) cannot create a third fixed-\(a\) boundary.  Section 7 below supplies
a short exact proof from the rational estimates already present in Rounds 16
and 18.

This verdict is deliberately limited:

- it promotes only the first-floor no-drop WP2 branch;
- it does not prove the high-floor first-drop CST obligation;
- it does not prove the full all-dimensional Pólya theorem;
- it does not edit or promote the manuscript proof graph;
- no floating-point search is a proof premise.

The source notes and replay files were not edited during this integration
audit.

## 2. Frozen dependency set

### 2.1 Analytic sources and independent audits

| Role | Artifact | SHA-256 |
|---|---|---|
| Revised strategy | `human/inbox/general-d_simplified_analytic_strategy.md` | `610E0533F1149EFC212ECF0B1610A8A429D0480C67774AACBA86F840693F1DE4` |
| Prior one-interface owner | `human/outbox/general-d-round-02.md` | `1DE673DDDEEEFEA101B6FC5A00410A84D6733913225D688278BECA592EF23C20` |
| Exact no-drop identity and wall term | `human/outbox/general-d-round-04-no-drop.md` | `9F7D3D21CAC7D04C9C0C65F650CFF7B878D3E0310486DA5C432F433BE9A26BA6` |
| Round 10 source | `human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md` | `82A0DD0E97A975E2FA023DFA7632816D4C6D3971641801A10B1B89A812A218C9` |
| Round 10 audit | `human/outbox/general-d-round-10-fractional-terminal-reserve-independent-audit.md` | `2DF1C6AF343B43C9CCB19EBB40BE4C74CD51B2119BCAF6DAB14368D0675E6CDF` |
| Round 11 source | `human/outbox/general-d-round-11-first-floor-pre-shelf-reduction.md` | `6F221BBB6CC287E0164424615C73F1414917ED8117CFE8B6E3DC94E3B4CB57A4` |
| Round 11 audit | `human/outbox/general-d-round-11-first-floor-pre-shelf-reduction-independent-audit.md` | `4AFE2BA7EE8A907095C7FCD21C0682D4DF08A09E7A20AED9036224545B377049` |
| Round 12 endpoint-domain bookkeeping | `human/outbox/general-d-round-12-one-level-alpha-endpoint-reduction.md` | `C07FB5228715C1A595878092C81387621AB0C87241AB2576FFE80753C6A29EA9` |
| Round 12 audit | `human/outbox/general-d-round-12-one-level-alpha-endpoint-reduction-independent-audit.md` | `8854D504C26D8A574E4E51190A279362E70350421438635BA587592B390C5EF0` |
| Round 14 exact-head source | `human/outbox/general-d-round-14-exact-head-endpoint-reduction.md` | `EC81BBE42152B682882509B034B37AB783FED9B46B429388B3D00CEF43900163` |
| Round 14 audit | `human/outbox/general-d-round-14-exact-head-endpoint-reduction-independent-audit.md` | `12980E8876824BDC781F98E5F19BB7DC0AF666CAD730A96FE6F229B4503D843A` |
| Round 15 exact-terminal source | `human/outbox/general-d-round-15-exact-terminal-endpoint-reduction.md` | `82E13B290BA24C482368544BA9FF1AB03A18D282A297873B0BB8B7AE0BA6CFD0` |
| Round 15 audit | `human/outbox/general-d-round-15-exact-terminal-endpoint-reduction-independent-audit.md` | `2046EFF7CD86A701BDA8D99E2C4275BF6F9A6787BDFE6A705874FD5833543678` |
| Round 16 geometric reduction | `human/outbox/general-d-round-16-continuous-geometric-reduction-and-hard-face.md` | `0C987E8DBFD6DE9F6B3714E07349A11D556E331BB6491D1D12926AB240FB2DD5` |
| Round 16 audit | `human/outbox/general-d-round-16-continuous-geometric-reduction-independent-audit.md` | `0A8749E72893E74F4950ADE561279CEF7040BDC602699295B01D4387FAED2597` |
| Round 17 auxiliary action-face identities | `human/outbox/general-d-round-17-action-face-quantile-reduction.md` | `AE546DC4929D806B54C02623A0E69D16E84C271361949EFC3FA85B37A6D776E6` |
| Round 17 audit | `human/outbox/general-d-round-17-action-face-quantile-reduction-independent-audit.md` | `48F7ED13E1B8CB29340262C7E6C5B29243D216C4A7687BE8AF861CCFDD7820FF` |
| Round 18 simultaneous-wall source | `human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure.md` | `0F56DC67EE58D20601F1C1123BD265F4323D3DC009377FDD0BABFD1E5E713585` |
| Round 18 audit | `human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure-independent-audit.md` | `7AFD34F502A1A882D5124CD4C373C253177079CDE414DA7F89B36943C18A48A9` |
| Round 19 action-face source | `human/outbox/general-d-round-19-action-face-jensen-closure.md` | `796854BE592E9E1836B6634BA12C59709BEDD87928F71A85EACE8A94B1570C2A` |
| Round 19 audit | `human/outbox/general-d-round-19-action-face-jensen-closure-independent-audit.md` | `8E0B2640084DD7A03F84860BCFD190EFD9D8BC38F59A6FBC1F62BAD145E4B7D2` |
| Accepted \(d=3\) base manuscript | `manuscript/spherical-shell-polya-proof.tex` | `9A26F2BD5DC0F82658B93AD910B579C1F0C2F53C540A249443E3AD3263C6DD6D` |

The \(d=3\) manuscript is an accepted upstream base for this scope audit;
its proof is not re-audited here.

### 2.2 Replayed verification artifacts

| Artifact | SHA-256 |
|---|---|
| `computations/general_d_fractional_terminal_probe.wl` | `31F0B831E43052725253BA8AB7F23E6695CBB80CFE74B048D3BC0FA79ED3F066` |
| `computations/general_d_round14_exact_head_endpoint_probe.wl` | `4051788FDA83E7B7DF214BFB4075A5B5EE425D5A2093E4DDF27CA3119684218D` |
| `computations/general_d_round15_exact_terminal_endpoint_probe.wl` | `261AFEE87ABAF64E3D969BDC57EF0B39671A5A4EFBC82546A6CAAE99509B0EE5` |
| `computations/general_d_round16_continuous_geometric_probe.wl` | `BEEA443C086D31081DB19E429BC4393D137825955B82F1F23AE153105A131C4B` |
| `computations/general_d_round17_action_face_quantile_probe.wl` | `E5E99410B16DF2E8A28AB64BA88F015C15DE75C97D0F984C318A138F8DB9855E` |
| `computations/general_d_round18_simultaneous_wall_symbolic_replay.wl` | `6EB326FEB37A8591C230D07160909B678CA9A19565DB78A33CF1329B838CCD3D` |
| `computations/general_d_round19_action_face_jensen_replay.wl` | `B31239E6F34726850ED1B7CD559B6EC39EEA0596AC4C49A6859B4D444442D54B` |

The replay scripts are audit aids.  Their floating searches are not inserted
into the analytic implication chain.

## 3. Exact starting point and the \(n=0\) owner

For an inner start, put

\[
 n=\lfloor\mu-r\rfloor,\qquad q=r+n,\qquad q\leq\mu<q+1.
\]

In the first-floor no-drop branch,

\[
 p=n,\qquad F_0=\cdots=F_n=1,
\]

and

\[
 \varepsilon=A(q)-\frac34\in[0,1),\qquad
 \chi_q={\bf1}_{\{A(q)=3/4\}}.
\]

Round 4 proves the literal strict-count identity

\[
 \boxed{
 D_A(r)=D_A(q)-\frac n2+2n\varepsilon
 +2\int_0^n u\sigma(r+u)\,du+\chi_q,}
 \qquad \sigma=-A'.
 \tag{3.1}
\]

The only possible ordinary-floor equality inside a no-drop first shelf is at
the terminal sample \(q\).  Indeed, if
\(A(r+j)+1/4=1\) for \(j<n\), strict decrease of \(A\) makes the next
ordinary floor at most zero, contradicting no-drop.  This is why (3.1) needs
one wall term \(\chi_q\), not a sum of unrecorded wall corrections.

If \(n=0\), then \(q=r\), and the tail is exactly in the already proved
one-interface sector \(0\leq\mu-r<1\).  Thus the new WP2 work starts at
\(n\geq1\); no \(n=0\) case is silently omitted.

## 4. Exhaustive \((\varepsilon,B)\) branch union

At \(q\), write

\[
 v=G_K(q),\qquad h=G_\mu(q),\qquad
 B=[v+\tfrac14]_<,\qquad A(q)=v-h.
\]

Since \(r\geq1/2\) and \(n\geq1\), one has \(q\geq3/2\).  The audited
local cap bound is

\[
 h\leq G_{q+1}(q)\leq G_{5/2}(3/2)<\frac15.
 \tag{4.1}
\]

The cases are exhaustive as follows.

| Case | Exact condition | Owner | Result |
|---|---|---|---|
| Remainder-rich | \(\varepsilon\geq1/4\) | Round 10 | In (3.1), \(-n/2+2n\varepsilon\geq0\); all other terms are nonnegative. |
| Many terminal levels | \(B\geq2\) | Round 10 | Strict counting gives \(v>7/4\); then (4.1) gives \(\varepsilon=v-h-3/4>4/5\), so this is already remainder-rich. |
| Zero terminal levels | \(0\leq\varepsilon<1/4,\ B=0\) | Round 11 | Forced exact corner; proved strictly positive. |
| One terminal level, open | \(B=1,\ 0<\varepsilon<1/4\) | Rounds 14--19 | Exact endpoint move and geometric closure prove strict positivity. |
| One terminal level, lower wall | \(B=1,\ \varepsilon=0\) | Rounds 14--19 plus literal wall jumps | The wall is two units more favorable than the open-side endpoint scalar. |

To check that the table has no hidden residual, suppose
\(0\leq\varepsilon<1/4\).  The second row shows \(B<2\), while
\(B\) is a nonnegative integer; hence \(B\in\{0,1\}\).  If \(B=0\),

\[
 v\leq\frac34,\qquad v-h=A(q)\geq\frac34,
\]

so equality is forced throughout:

\[
 v=A(q)=\frac34,\quad h=0,\quad q=\mu,
 \quad\varepsilon=0,\quad Q=0,\quad\chi_q=1.
 \tag{4.2}
\]

If \(B=1\) and \(\varepsilon=0\), then \(h=0\) would force
\(v=3/4\), contradicting \(B=1\).  Thus \(h>0\), which is exactly the
lower-noncorner wall.  If \(\varepsilon>0\), the point is exactly the open
row.  There is no sixth phase.

## 5. The \(B=0\) theorem

Round 11 owns (4.2) literally, rather than as a limit from \(B=1\).  It
combines

- the zero-level terminal triangle
  \(D_A(q)\geq9\pi/(16\theta)\);
- the exact no-drop head and the favorable \(+1\) wall term;
- a pointwise lower bound for the head slope; and
- an exact Bernstein-positive quartic.

The resulting proof gives \(D_A(r)>0\) (in fact the audited estimates give a
margin greater than one).  It applies to every positive shift and therefore
also covers the comparison line \(r=1/2\).

The current Round 11 source hash is the post-audit integrated version.  Its
two changes relative to the original frozen audit target only distinguish
the exact-head-only diagnostic from the exact-head-plus-cap diagnostic and
replace an incorrect word “positive” by the wall-safe “nonnegative.”  No
formula or theorem statement changed.  These clarifications do not weaken
the \(B=0\) proof.

## 6. Lossless \(B=1\) endpoint move

The Round 11 pre-shelf sign target and its Round 12 specialization were
falsified in Round 13 and are **not** premises of this proof.  Only Round
12's endpoint-domain bookkeeping survives.  Round 14 restores the exact
no-drop head and exact cap.  Round 15 then removes the last inverse-tangent
loss and obtains an exact identity.

For an original open \(B=Q=1\) point, write

\[
 q=r+n,\qquad \mu=q+\alpha,\qquad 0\leq\alpha<1,
\]

let \(z\) be the outer inverse point \(G_K(z)=3/4\), and put

\[
 y=z-q>0,\qquad M=[y]_<,\qquad \eta=y-M\in(0,1].
\]

The literal shifted count is

\[
 T_{A_\alpha}(r)=1+2n+2M.
 \tag{6.1}
\]

This remains correct at an integral inverse wall: if \(y=m\), then
\(M=m-1\), so the equality sample is absent.  Therefore Round 15's scalar

\[
 \boxed{
 \Omega(\alpha)=2J_K(r)-2J_{q+\alpha}(r)
 -(1+2n+2M)}
 \tag{6.2}
\]

satisfies the exact identity

\[
 D_{A_\alpha}(r)=\Omega(\alpha)
 \tag{6.3}
\]

at every original open point.  It retains the outer terminal contribution,
inner cap, no-drop head, inverse displacement, and full discrete count.

The endpoint is

\[
 \bar\alpha=\min\{1,\alpha_*,\alpha_{\rm act}\},
 \tag{6.4}
\]

where \(\alpha_*\) is the lower action root and

\[
 \alpha_{\rm act}
 =K-q-\frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}}.
 \tag{6.5}
\]

Direct differentiation gives

\[
 \Omega'(\alpha)
 =-2\left.\frac{d}{da}J_a(r)\right|_{a=q+\alpha}<0.
 \tag{6.6}
\]

Every original active open point has \(\alpha<\bar\alpha\), so

\[
 D_{A_\alpha}(r)=\Omega(\alpha)>\Omega(\bar\alpha)
 =:\Omega_{\rm end}.
 \tag{6.7}
\]

The artificial path may cross shelf walls.  This causes no change in (6.7):
it compares the explicit continuous expression (6.2) with the integer
\(M,n\) frozen from the original chamber and does not assert that every
intermediate point is another admissible no-drop tail.

At the literal lower action wall \(A(q)=3/4\), the pair changes from the
open-side \((Q,\chi_q)=(1,0)\) to

\[
 (Q,\chi_q)=(0,1).
\]

The terminal endpoint count loses one unit and S4 gains one unit.  Hence the
literal defect is

\[
 \Omega(\alpha_*)+2,
 \tag{6.8}
\]

not the open-side value.  The lower wall is therefore strictly more
favorable and is fully owned once the open-side endpoint is proved.

## 7. Continuous enlargement and the missing \(z=2\) glue

At a Round 15 endpoint put \(a=q+\bar\alpha\) and
\(A=G_K-G_a\).  Every genuine endpoint lies in the enlarged domain

\[
 a\geq2,\qquad K-a>\pi,\qquad
 A(a-1)\geq\frac34,\qquad z>2.
 \tag{7.1}
\]

Round 16 rewrites

\[
 \Omega_{\rm end}
 =2\{J_K(r)-J_a(r)\}-2(z-r)-1+2\eta.
\]

The function

\[
 E_0(s)=2\{J_K(s)-J_a(s)\}-2(z-s)-1
\]

is strictly convex, with

\[
 E_0'(s)=2(1-A(s)).
\]

Its unique minimizer \(x\) satisfies \(A(x)=1\).  With

\[
 F(K,a)=J_K(x)-J_a(x)-(z-x),
\]

one obtains

\[
 \boxed{\Omega_{\rm end}\geq2F(K,a)-1+2\eta.}
 \tag{7.2}
\]

Round 16 proves \(F_K>0\).  To reduce fixed \(a\) to only the radial and
action boundaries, one must also know that \(z=2\) cannot be encountered
first.  Here is the exact check.

Let

\[
 K_0=2+\pi,\qquad
 \theta_0=\arccos\frac{2}{2+\pi},\qquad c=\frac{117}{100}.
\]

The alternating cosine lower polynomial is

\[
 C_-=1-\frac{c^2}{2}+\frac{c^4}{24}-\frac{c^6}{720}.
\]

Using the Round 18 lower bound \(\pi>333/106\), exact arithmetic gives

\[
 C_- - \frac{2}{2+333/106}
 =\frac{9374697634131}{8720000000000000}>0.
 \tag{7.3}
\]

Since \(\cos c>C_-\) and
\(2/(2+\pi)<2/(2+333/106)\), (7.3) gives

\[
 \cos c>\cos\theta_0,
 \qquad c<\theta_0.
\]

Round 16's existing exact \(c=117/100\) certificate gives

\[
 \tan c-c>\frac{33}{28}.
\]

Using \(\pi<22/7\),

\[
 \tan\theta_0-\theta_0
  >\tan c-c>\frac{33}{28}>\frac{3\pi}{8}.
\]

Because \(K_0\cos\theta_0=2\),

\[
 G_{2+\pi}(2)
 =\frac{2(\tan\theta_0-\theta_0)}{\pi}
 >\frac34.
 \tag{7.4}
\]

Finally, (7.1) gives \(K>a+\pi\geq2+\pi\), and \(G_K(2)\) is strictly
increasing in \(K\).  Thus \(G_K(2)>3/4\), so the inverse point satisfying
\(G_K(z)=3/4\) obeys \(z>2\).  The same conclusion holds on the radial
closure \(K-a=\pi\).  Therefore \(z=2\) is redundant and creates no third
boundary face.

## 8. Closure of the enlarged geometric lemma

With Section 7 in place, strict radial monotonicity reduces fixed-\(a\)
minimization to

\[
 K=a+\pi
 \qquad\text{or}\qquad
 A(a-1)=\frac34.
\]

Put

\[
 H(a)=G_{a+\pi}(a-1)-G_a(a-1).
\]

Round 18 proves that \(H\) is strictly decreasing and has exactly one root
\(H(a_*)=3/4\), with

\[
 \frac{11}{2}<a_*<\frac{45}{8}.
\]

It also proves at the simultaneous radial/action wall

\[
 \boxed{
  F(a_*+\pi,a_*)-\frac12
 >\frac{1443}{449440}>0.}
 \tag{8.1}
\]

The two boundary orientations are complementary:

1. for \(a<a_*\), the radial face is feasible and Round 16 proves
   \(dF/da<0\), so it decreases toward \(a_*\);
2. for \(a>a_*\), the action face is the lower fixed-\(a\) boundary and
   Round 19 proves \(dF/da>0\), so it increases away from \(a_*\);
3. the common endpoint is owned literally by (8.1), not by an open-face
   limit.

Hence

\[
 \boxed{F(K,a)\geq\frac12}
 \tag{8.2}
\]

throughout the enlarged endpoint domain, with a strict boundary reserve.
Combining (6.7), (7.2), (8.2), and \(\eta\in(0,1]\) gives

\[
 D_{A_\alpha}(r)
 >\Omega_{\rm end}
 \geq2F-1+2\eta
 >0
 \tag{8.3}
\]

for every original open \(B=1\) point.  Equation (6.8) then closes the
literal lower-noncorner wall as well.

Round 17 is used only for the quantile primitive, the exact boundary-speed
identity, and the endpoint sinc comparison imported by Round 19.  Its
unproved chord scalar is bypassed.  Round 19's Jensen proof and exact replay
were independently audited in the separate Round 19 audit listed above.

## 9. Dimension-labelled grids and activity owners

The branching shifts are

\[
 r_m=m+\frac{d-2}{2}.
\]

For every even \(d\geq4\), these form a subset of the integer grid
\(r\geq1\).  For every odd \(d\geq5\), they form a subset of the
half-integer grid \(r\geq3/2\).  It is therefore sufficient to prove the two
owner grids

\[
 d_{\rm own}=4,\quad \kappa_4=\frac34
 \qquad\text{and}\qquad
 d_{\rm own}=5,\quad \kappa_5=2.
 \tag{9.1}
\]

The active condition is

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}
 +\kappa_d,
 \qquad
 \kappa_d=\frac{(d-2)^2-1}{4}.
 \tag{9.2}
\]

For higher dimensions of a fixed parity, \(\kappa_d\) is larger, so their
active regions are subsets of the corresponding owner region.  Equivalently,
their activity endpoint

\[
 K-q-\frac{\pi K}{\sqrt{K^2-\kappa_d}}
\]

occurs no later than the owner endpoint (6.5).  Since \(\Omega\) decreases
in \(\alpha\), the later owner endpoint is the adverse comparison.  Proving
the owner grids therefore proves every higher-dimensional labelled shift.
Equality in (9.2) is assigned to the strengthened no-mode theorem, because
the spectral proxy count is strict.

The half-integer line \(r=1/2\) does not occur in any \(d\geq4\) branching
sequence.  It belongs to the already completed \(d=3\) base problem.  The
coarse Round 11 sufficient scalar was known to fail diagnostically on this
line, but that scalar is absent from the final chain.  Excluding
\(r=1/2\) from the new extension-grid endpoint theorem therefore creates no
general-dimensional gap.  Round 11's \(B=0\) theorem happens to include it,
but the \(B=1\) proof above need not and does not replace the \(d=3\) owner.

## 10. Strict-wall ledger

Every wall requested by the revised strategy has an owner.

1. **Ordinary first-shelf floor.**  The ordinary floor is used in the
   no-drop label.  Strict decrease prevents an interior lower equality; the
   sole possible terminal equality is recorded by \(\chi_q\).
2. **Literal lower shell-action wall.**  At \(A(q)=3/4\),
   \((Q,\chi_q)=(0,1)\), and the actual defect gains two units relative to
   the open-side scalar.  It is not identified with an open limit.
3. **Outer action wall.**  \(B=[v+1/4]_<\) is always evaluated literally.
   In particular, \(v=7/4\) still has \(B=1\); \(B\geq2\) requires
   \(v>7/4\).
4. **Inverse spatial wall.**  If \(y=m\in\mathbb N\), then
   \(M=m-1\) and \(\eta=1\).  The equality sample is absent.  The open
   cell just above the wall has \(M=m\) and \(\eta\downarrow0\), and is
   included in the continuous proof.
5. **The wall \(y=0\).**  Its literal value has \(B=0\) and is owned by
   Round 11.  The \(B=1\) side has \(y\downarrow0\) and is covered by
   (8.3); the two are not conflated.
6. **Interface/floor branch wall.**  The artificial value \(\alpha=1\) is
   only the limit from below.  At a literal \(\mu-r\in\mathbb N\), the
   definition of \(n\) changes and the new representation has
   \(\alpha=0\), \(q=\mu\), and zero cap.
7. **Interface sample.**  At \(r+j=\mu\), the inner action is literally
   zero.
8. **Outer sample.**  At \(r+j=K\), the sample is absent under the strict
   bracket.
9. **Owner activity wall.**  It is used only as a one-sided endpoint of the
   algebraic comparison; literal equality belongs to the no-mode owner.
10. **Radial/action walls.**  Round 19 is restricted to the strict action
    face \(K-a>\pi\).  Round 18 separately owns the simultaneous equality
    \(K-a=\pi\).  The critical point changes to \(x=0\) there exactly as
    required.
11. **Auxiliary inverse boundary \(z=2\).**  Section 7 proves it is
    redundant, so it leaves no unowned face.

## 11. Fresh Mathematica replay

Every current Wolfram Language artifact in Section 2.2 was run in a fresh
Wolfram 15.0 kernel with

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\math.exe' -noinit -script <file>
```

All processes exited with code zero.  The decisive outputs were:

- the Round 10/11 evaluator printed `diagnosticOnly=True`, zero sampled
  negative T1/T2/T3 slacks, 5,911 \(B=1\) extension-grid records, and the
  expected 1,197-point \(B=0\) grid diagnostic;
- Round 14 printed `round12ReplayOK=True` and
  `round14ReplayOK=True` on 3,171 hard records;
- Round 15 printed `round15ReplayOK=True`, zero negative endpoint values,
  zero negative tangent gaps, and the expected 16 failures of the deliberately
  overextended full-phase endpoint;
- Round 16 printed `round16DomainViolationCount=0`,
  `round16IdentityFailureCount=0`, and `round16ReplayOK=True`;
- Round 17 printed `round17ReplayOK=True`;
- Round 18 printed `round18ExactChecks=True` and
  `round18ReplayOK=True`;
- Round 19 printed `round19StandaloneReplay=True`,
  `round19SymbolicChecks=True`, `round19ExactReplayOK=True`,
  `round19DiagnosticChecks=True`, and `round19ReplayOK=True`.

The Round 18 and Round 19 finite rational identities were checked exactly.
The searches and sampled minima in Rounds 10--17 remain diagnostics only and
are not used in Sections 3--10.

## 12. Dependency pruning and final disposition

The final WP2 implication chain is

\[
 \begin{array}{c}
 \text{one-interface owner for }n=0,\\[2mm]
 \text{S4}+\text{Round 10 automatic sectors}+\text{Round 11 }B=0,\\[2mm]
 \text{Round 15 exact }B=1\text{ endpoint}
 \longrightarrow
 \text{Round 16 }F\text{-reduction}
 \longrightarrow
 \begin{cases}
 \text{Round 16 radial sign},\\
 \text{Round 19 action sign},\\
 \text{Round 18 simultaneous-wall value}
 \end{cases}
 \end{array}
\]

with Round 12 supplying endpoint-domain bookkeeping, Round 14 supplying the
exact-head transition, and Round 17 supplying only the identities explicitly
imported by Round 19.

The following are expressly **not** load-bearing:

- the falsified Round 11 pre-shelf sign claim;
- the falsified Round 12 endpoint sign target;
- Round 13's counterexample, except as a gate decision;
- the superseded Round 14 inverse-tangent lower scalar;
- the unproved Round 17 chord scalar;
- any sampled numerical minimum.

Final dispositions:

- Exhaustive first-floor no-drop branch union: **PASS**.
- \(n=0\) one-interface handoff: **PASS**.
- Remainder-rich and \(B\geq2\) sectors: **PASS**.
- \(B=0\) exact corner: **PASS**.
- Open and lower-wall \(B=1\) sectors: **PASS**.
- Integer and half-integer extension grids: **PASS**.
- Owner-dimensional activity walls: **PASS**.
- Strict floor, action, inverse, interface, branch, and radial walls:
  **PASS**.
- \(d=3\) exclusion from the new endpoint obligation: **PASS**.
- WP2 first-floor no-drop status: **ready for promotion by the proof-graph
  owner**.
- High-floor CST and the all-dimensional theorem: **still open**.
