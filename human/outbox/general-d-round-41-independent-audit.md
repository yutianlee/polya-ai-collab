# Independent audit: General dimension, Round 41

**Date:** 20 July 2026

Audited artifacts:

- `human/inbox/general-d-strategy_r2.md`
- `human/inbox/general-d_simplified_analytic_strategy.md`
- `human/outbox/general-d-round-40-upper-alpha-midpoint-reduction.md`
- `human/outbox/general-d-round-40-independent-audit.md`
- `human/outbox/general-d-round-41-rational-branch-elimination.md`
- `computations/general_d_round41_bernstein_sign_replay.wl`
- the exploratory companion
  `computations/general_d_round41_rational_branch_obstruction.wl`

## Verdict

**NOT PASS as a strategy-authorized analytic closure. PASS only as an exact
structural reduction and computer-assisted candidate.**

The rational trigonometric enclosures, branch domains, convex/affine
envelopes, denominator directions, sign-safe squarings, wall maps, and finite
coverage in the final Round 41 note are correct. I found no exact
counterexample. A fresh Windows Mathematica run reproduced every exact
Bernstein row and ended with

```text
round41BernsteinSignReplayOK=True
```

Consequently, if the finite Bernstein certificate were admitted as a
load-bearing computer-assisted proof, it would establish

\[
 \mathcal R_I>0,\qquad
 \mathcal R_{II}>0,\qquad
 \mathcal R_*(p,m,t)>0,
\]

and hence, by the audited strict Round 40 implication,
\(\Gamma_{\rm OB}>0\) on this one endpoint.

The certificate is not authorized by the binding revised strategy, however.
It owns 4,405 load-bearing coefficient signs, while the note prints only
aggregate sign counts rather than the coefficients themselves. This is not
the short, printed, hand-checkable rational wall algebra covered by the
exception in Section 11.6 of the simplified strategy. It is a new finite
computer certificate. Exact arithmetic, fixed cells, and reproducibility
make the candidate mathematically strong, but do not turn it into the
required analytic sign table.

The final Round 41 note now classifies the result accordingly. It does not
promote \(\mathcal R_*>0\), the Round 40 endpoint, CST, the branching
aggregate, or the all-dimensional theorem. No proof-obligation or state file
was edited by this audit.

## 1. Theorem boundary and inherited strictness

Round 40 supplies the audited implication

\[
 \Gamma_{\rm OB}>\mathcal R_*(p,m,t)
\]

on the one-sided gap-side outer-\(B\), upper-alpha endpoint, with

\[
 p\geq3,\qquad m\geq1,\qquad p>dm,
 \qquad 0<t<\frac\pi2.
\]

Round 41 neither changes the owner nor reassigns the one-sided endpoint. Its
two formulas are the two analytic branches of the one maximum already
present in Round 40. The later rational \(s\)- and \(v\)-cells are
verification cells; they are not new \(B_0\)-, \(j\)-, floor-, or
shell-ratio owners.

The exact branch scalars are strictly above their rational envelopes. This
is important at the 146 zero Bernstein coefficients: nonnegativity of the
rational envelope is enough to give strict positivity of the exact scalar.
No coefficient-level strictness is silently assumed.

## 2. Global rational enclosures

With \(s=2t/\pi=1-d\), the tangent partial-fraction expansion has positive
terms and gives

\[
 \ell_-(s)=\frac{49s^3}{121(1-s^2)}<L_0(t).
\]

The inherited global tangent majorant and \(\pi<22/7\) give

\[
 L_0(t)<\ell_+(s)=\frac{121s^3}{294(1-s^2)}.
\]

The coefficient directions in

\[
 \mathsf A_-(s)=\frac{333s^2}{848}-\frac{1331s^4}{16464}
\]

are also correct: \(333/106<\pi\) lowers the positive quadratic term,
whereas \(\pi<22/7\) raises the coefficient of the subtracted quartic term.
Thus

\[
 0<\mathsf A_-(s)<\frac{1-\cos t}{\pi}.
\]

Finally, \(t<11s/7\), positivity and monotonicity of
\(x-x^3/6+x^5/120\) on \([0,11/7]\), and the Taylor upper bound for sine
give

\[
 2+\sin^2t<\mathsf S_+(s).
\]

All rational denominators have the stated signs on \(0<s<1\). The strict
directions are retained when these bounds are inserted into the two branch
scalars.

## 3. Branch I audit

The geometric-branch constraints imply

\[
 0<a_h<a<u_I,
 \qquad
 u_I=\frac{2(p+2)\ell_+}{5}.
\]

The lower replacements \(X_I>X_I^-\) and

\[
 \frac{p^2(1-\cos t)a}
 {\pi\sqrt{2+\sin^2t-2a}}>Y_I^-a
\]

have the correct direction. Since \(a_h<1/2\),
\(D_I^+>2-2a_h>1\), so no radical sign is hidden.

### 3.1 The endpoint/cubic case

The exact identity

\[
 D_0-D_I^+
 =\frac{2d}{(1+d)\{p+d(p+2)\}}>0
\]

justifies replacing \(D_I^+\) by the larger \(D_0\). The resulting
endpoint cubic is

\[
 f_s(p)=E-Cp+kp^2(p+2),
 \qquad k=K/\sqrt{D_0}>0.
\]

The identity

\[
 \left(\frac9{10}+\frac{9d}{16s}-d\right)-\frac{67}{80}
 =\frac{(4s-3)^2}{16s}
\]

gives \(E>0\), while \(0<C<1\) gives

\[
 Q=4C^2-36CE-27E^2<0.
\]

The discriminant expansion

\[
 \operatorname{Disc}_p(f_s)
 =k\{4C^3+kQ-32k^2E\}
\]

was independently checked. Exact Bernstein positivity of

\[
 Z=K^2Q^2-16C^6D_0
\]

implies \(k(-Q)>4C^3\), hence the discriminant is negative. The cubic has
one real root; \(f_s(0)=E>0\) and its positive leading coefficient force
that root to be negative. Therefore \(f_s(p)>0\) for \(p\geq0\).

### 3.2 The AM--GM case

For a hypothetical nonpositive Case-I-A envelope,
\(a_0\leq u_I\) implies

\[
 2\sqrt{X_I^-Y_I^-}\geq\frac{2X_I^-}{u_I}
 =\frac{5H_I^-}{8\ell_+}.
\]

Since \(c_I=c_I|_{p=0}-Cp\), this yields the necessary wall
\(p\geq p_0(s)\). The stronger squared polynomial

\[
 \mathsf P_{A,0}=
 \frac{(H_I^-)^2\mathsf A_-^2p^4(p+2)^2}{4}-c_I^4D_0
\]

satisfies \(\mathsf P_{I,A}\geq\mathsf P_{A,0}\), with strict inequality
in the relevant \(c_I<0\) countercase.

The charts cover the full necessary domain:

- \(p=p_0+x\), \(x\geq0\), for \(0<s\leq2/3\);
- \(p=3+x\), \(x\geq0\), for \(2/3\leq s<1\).

In each chart the polynomial is degree six in \(x\). Nonnegative
Bernstein coefficients for every coefficient polynomial in \(s\) imply
nonnegativity for all \(x\geq0\), so no cutoff in the unbounded variable is
used. The high-\(s\) rational denominator has the one negative factor
\(s-2\); the replay correctly certifies the negative of its numerator.

## 4. Branch II audit

The phase and hard inequalities yield the two strict lower walls

\[
 a>g,\qquad a>h,\qquad b=\max\{g,h\},\qquad 0<b<a<1.
\]

The directions follow respectively from \(L_0>\ell_-\) and
\(L_0<\ell_+\). Also \(M_{II}>M^-\), and
\(D_b^+=\mathsf S_+-2b>0\). Hence

\[
 \mathcal R_{II}>
 c_{II}+M^-(1-a)+Y_b^-a
\]

with no denominator-sign loss.

The phase base and \(p\geq3\) imply

\[
 (p+3)\ell_-<\frac54,
 \qquad \ell_-<\frac5{24}.
\]

Since \(\ell_-\) is strictly increasing and
\(\ell_-(2/3)-5/24=37/4840>0\), every feasible phase point has
\(0<s<2/3\).

### 4.1 Nonnegative affine slope

For hard-wall ownership,

\[
 c_{II}+M^-(1-h)=\frac9{10}+\frac{7d}{8s}>0,
\]

so that endpoint is automatic. For geometric ownership, a nonpositive
endpoint with nonnegative slope forces

\[
 c_{II}+M^-\leq0.
\]

Because its \(p\)-coefficient is \((s-3)/4<0\), this gives
\(p\geq p_C(s)\). The substitution \(p=p_C+x\), \(x\geq0\), covers the
whole necessary set, and the exact coefficient-family table proves
\(\mathsf P_g^+\geq0\).

### 4.2 Nonpositive affine slope

The actual upper wall is retained as

\[
 a<u_P=1-\frac{2\ell_-(p+4)}5,
 \qquad p<p_M=\frac5{4\ell_-}-3.
\]

Moreover \(u_P>5/12>0\). For nonpositive slope, evaluation at \(u_P\)
is a valid lower endpoint. If \(e_U<0\), the exact coefficient

\[
 \partial_pe_U=\frac{235s-29517}{58564}<0
\]

gives \(p>p_E\). The coefficient of \(p\) in \(g-h\) is positive on
\(0<s<2/3\), so hard ownership is \(p\leq p_X\) and geometric ownership
is \(p\geq p_X\).

For the hard owner, every nonempty counterinterval is mapped by

\[
 p=p_E+v(p_X-p_E),\qquad 0\leq v\leq1.
\]

The six tensor cells cover \(0\leq s\leq27/50\). On the remaining strip,

\[
 p_X-p_E=
 \frac{F(s)}
 {10s^3(235s-29517)(29047s-58329)}.
\]

Both linear factors in the denominator are negative for
\(0<s<2/3\), so the denominator is positive. Exact positivity of all six
Bernstein coefficients of \(-F\) on \([27/50,2/3]\) gives
\(p_X<p_E\); the hard counterinterval is empty there.

For the geometric owner, every actual counterpoint obeys

\[
 \max\{p_X,p_E\}<p<p_M.
\]

The \(p_X\)-chart for \(0<s\leq1/2\) and the \(p_E\)-chart for
\(1/2\leq s<2/3\) both use \(0\leq v\leq1\). They cover every actual
counterpoint, regardless of the relative order of \(p_X\) and \(p_E\),
because actual feasibility itself puts the chosen lower wall below
\(p<p_M\). The eight tensor cells cover the two charts without a seam gap.

All squarings in Branch II are made only when the unsquared constant term
is negative; \(b,u_P,p,\mathsf A_-\), and the relevant radical denominator
are positive. Therefore every squared comparison has the stated direction.

## 5. Exact replay and finite coverage

The final self-contained replay contains no `Resolve`, `Reduce`, CAD,
floating-point evaluation, random search, or numerical sampling. It uses
only exact rational arithmetic and a transparent one- and two-variable
Bernstein transform. The replay now also checks the claimed denominator
factorizations by exact positive constants and checks the exact
\(p_X-p_E\) numerator and denominator identities.

The independently reproduced sign rows are:

| target | cells or charts | degrees | exact signs \((+,0,-)\) |
|---|---|---:|---:|
| I-B \(Z\) | three \(s\)-cells | \(22\) | each \((23,0,0)\) |
| I-A, \(p_0+x\) | two \(s\)-cells | \(x:6\), \(s:32\ldots36\) | \((178,63,0)\), \((241,0,0)\) |
| I-A, \(3+x\) | one \(s\)-cell | \(x:6\), \(s:17\ldots21\) | \((146,0,0)\) |
| II geometric lower | two \(s\)-cells | \(x:6\), \(s:28\ldots30\) | \((143,63,0)\), \((206,0,0)\) |
| II hard at \(u_P\) | six tensor cells | \((36,6)\) | \((239,20,0)\), then five \((259,0,0)\) |
| II hard empty-cap | one \(s\)-cell | \(5\) | \((6,0,0)\) |
| II geometric \(p_X\)-chart | four tensor cells | \((30,6)\) | each \((217,0,0)\) |
| II geometric \(p_E\)-chart | four tensor cells | \((30,6)\) | each \((217,0,0)\) |

These rows total 4,405 coefficients: 4,259 positive, 146 zero, and none
negative. The cells are fixed in advance and their union covers every
algebraic countercase. Unbounded \(p\) is handled by nonnegative
coefficient families in \(x\geq0\); the phase branch is bounded by \(p_M\)
and mapped to \(v\in[0,1]\). Hence the computer-assisted certificate has a
finite and explicit coverage/termination proof.

## 6. Strategy-compliance decision

The fixed cells are not new theorem owners and do not create a
\(B_0\)-, \(j\)-, floor-, or ratio-indexed family. That observation is not
enough to authorize the proof. Section 4 is load-bearing and contains 4,405
coefficient signs. The note prints the transform, domains, degrees, and sign
counts, but not the coefficients whose signs are decisive.

Accordingly this is a reproducible exact computer-assisted certificate, not
the short hand-checkable rational wall lemma allowed by simplified strategy
Section 11.6. It falls on the forbidden-certificate side of the revised
strategy's Gate A criterion. The exact replay is much stronger evidence than
the earlier black-box `Resolve=False`, but it cannot be promoted as the
requested analytic/Sturm/sign-table closure.

The correct gate order is:

1. the selected \(\Gamma_{\rm OB}\to\mathcal R_*\) endpoint projection is
   analytically exhausted by Round 41;
2. make the one stronger exact pointwise attempt allowed by the revised
   strategy through \(\mathcal H_\Delta\) or directly through \(\Phi_\delta^+\),
   using Round 38 equation (R38.20);
3. activate Gate B only if that stronger sign is false or also requires a
   forbidden ratio/count/chamber split or finite certificate.

Thus the first unproved proposition in the authorized analytic chain remains
\(\mathcal R_*>0\) for this Round 40 endpoint. The computer-assisted
candidate supports it, but does not change its repository status.
