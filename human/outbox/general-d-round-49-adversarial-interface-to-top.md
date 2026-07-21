# Round 49 independent adversarial audit: interface-to-top suffix

Date: 2026-07-21

Scope: literal falsification of the Round 49 suffix target, its permitted
fallback, and the \(d=4\) weighted aggregate. This report makes no theorem
promotion and changes no proof-obligation state.

## 1. Independence boundary

The evaluator in

    computations/general_d_round49_independent_suffix_search.py

was built without importing the Prompt-A evaluator or its formula
implementation. It uses a separately coded shell action, inverse bisection,
literal strict-bracket ledger, and an alternative trigonometric moment
primitive. Prompt-A output was not inspected before the evaluator and its
initial sweep were frozen.

All finite searches below are falsification diagnostics. Directed Arb is
used at two precisions for the named negative or pressure records. Exact
analytic inequalities are used for the cumulative-majorization
counterexample.

## 2. Independently evaluated literal quantities

Write \(\mu=\rho K\), \(A=G_K-G_\mu\),

\[
 H=\frac{K-\mu}{\pi},\qquad
 \tau=A(\mu),\qquad b=\lfloor\tau\rfloor,\qquad
 R=A^{-1}(b).
\]

The direct literal computation is

\[
 \mathrm{WT}_4
 =\frac{K^4-\mu^4}{64}
 -\sum_{1\le a<K}a^2[A(a)+1/4]_<.
\]

It is independently cross-checked against the inverse-height sum

\[
 \frac{K^4-\mu^4}{64}
 -\sum_{\substack{n\ge1\\n-1/4<H}}
 S_2\!\left(\left\lceil A^{-1}(n-1/4)\right\rceil-1\right).
\]

For the suffix, the independent spatial form is

\[
 I_{\rm suf}=\int_0^Rz^2(A(z)-b)\,dz,\qquad
 P_{\rm suf}=\sum_{1\le a<R}a^2[A(a)-b+1/4]_<,
\]

\[
 \mathcal R_{\rm suf}=I_{\rm suf}-P_{\rm suf}.
\]

The supply also has the independently derived moment form

\[
 I_{\rm suf}=\frac{M_K(R)-M_\mu(R)}3,
\]

where the evaluator uses

\[
 M_R(z)=\frac{z^4\arccos(z/R)}{4\pi}
 +\frac{R^4}{4\pi}\left(\frac{3\theta}{8}
 -\frac{\sin2\theta}{4}+\frac{\sin4\theta}{32}\right),
 \quad \theta=\arcsin(z/R),\quad z<R,
\]

and the constant endpoint value \(3R^4/64\) for \(z\ge R\).
Direct differentiation verifies this primitive.

The evaluator also computes every complete suffix cell

\[
 L_k=\int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds-S_2(M_k),\qquad
 M_k=\lceil\eta(k-1/4)\rceil-1,
\]

the exact terminal term with a node only when \(\alpha>3/4\), and

\[
 \mathcal R_{\rm out}=\sum_{n=1}^{b}\left(\frac{19N_n}{48}
 +\frac{27}{128}\right).
\]

Thus suffix, fallback, and literal aggregate are evaluated through distinct
inverse-height, spatial clipped-action, and direct finite-ledger forms.

## 3. Classification rule

The packet's classification is used literally:

| class | condition | consequence |
|---|---|---|
| A | \(\mathrm{WT}_4<0\) | rejects the scoped aggregate proxy |
| B | \(\mathcal R_{\rm suf}<0\le\mathrm{WT}_4\) | rejects R49 only |
| C | \(\mathcal R_{\rm out}+\mathcal R_{\rm suf}<0\le\mathrm{WT}_4\) | rejects R49-FB only |
| D | an auxiliary strengthening fails while its parent stays nonnegative | rejects only that strengthening |
| E | positive record | diagnostic only |

No class A, B, or C record was found.

## 4. Directed class-E interface pressure record

Take the exact rational parameters

\[
 \rho=\frac1{100},\qquad
 K=\frac{2532821}{25000},\qquad
 \mu=\frac{2532821}{2500000}.
\]

Arb at 768 and 1280 bits gives strict activity and

\[
 \tau=31.74392682672249859\ldots,\qquad b=31,\qquad
 \widehat H=0.92638978366302895\ldots.
\]

The only normalized suffix cell is terminal and interface-straddling. Its
\(3/4\)-node is just inside the inner branch. The normalized support is
uniquely enclosed by

\[
\begin{aligned}
2.517673351476663788910721007538815186134201064374167257624888797
&<R\\
&<2.517673351476663788910721007538815186134201064374167257624888798.
\end{aligned}
\]

All 101 literal action walls were directed. The complete strict-bracket
ledger is

    1:32; 2-3:31; 4-5:30; 6-7:29; 8-9:28; 10-11:27;
    12-13:26; 14-15:25; 16-18:24; 19-20:23; 21-22:22;
    23-24:21; 25-27:20; 28-29:19; 30-32:18; 33-34:17;
    35-37:16; 38-40:15; 41-42:14; 43-45:13; 46-48:12;
    49-51:11; 52-54:10; 55-57:9; 58-61:8; 62-64:7;
    65-68:6; 69-72:5; 73-76:4; 77-81:3; 82-86:2;
    87-92:1; 93-101:0.

The closest wall is still strict:

\[
 A(1)+\frac14-32=7.1983438771189703\ldots\,10^{-7}>0.
\]

Consequently

\[
 P_4^<=1565242,\qquad
 W_4=1646182.4991649526223673294536489276,
\]

\[
 \boxed{\mathrm{WT}_4
 =80940.4991649526223673294536489276>0.}
\]

For the suffix, only \(a=1,2\) are below \(R\), with shifted strict counts
\((1,0)\). Both directed precisions give

\[
 I_{\rm suf}=1.63646741830352348234566850344235758\ldots,
\]

\[
 \boxed{\mathcal R_{\rm suf}
 =0.63646741830352348234566850344235758\ldots>0.}
\]

The prefix inverse counts are

    92,86,81,76,72,68,64,61,57,54,51,48,45,42,40,37,
    34,32,29,27,24,22,20,18,15,13,11,9,7,5,3.

They give \(\mathcal R_{\rm out}=191447/384\), hence

\[
 \boxed{\mathcal R_{\rm out}+\mathcal R_{\rm suf}
 =499.1963632516368568\ldots>0.}
\]

This is class E: a certified positive point, not continuum coverage.

## 5. Exact and directed class-D failures

### 5.1 Cumulative radial-prefix strengthening

The natural sufficient strengthening

\[
 C_j(B)=\int_0^{j+1/2}z^2B(z)\,dz-\sum_{a=1}^ja^2m_a\ge0
\]

is false on the strict-active shell domain. For

\[
 \rho=\frac{49}{50},\qquad K=3000,\qquad\mu=2940,\qquad b=2,\qquad j=512,
\]

elementary rational bounds on \(\pi\), \(\arccos(1-y)\), and the inner action
give \(m_a\ge17\) for \(1\le a\le512\) and

\[
 \boxed{C_{512}(B)<-\frac{40211689593925}{12531456}<0.}
\]

An independent high-precision evaluation outside the committed evaluator
gives the diagnostic parent values

\[
 C_{512}(B)=-3272556.0997618759\ldots,\qquad
 \mathrm{WT}_4=2242742955>0,
\]

\[
 \mathcal R_{\rm suf}=2139013374.97249\ldots>0.
\]

The exact rational inequality certifies the class-D failure; the displayed
parent values are diagnostic only. The record rejects radial-prefix
majorization only.

### 5.2 Separate-sign Peano strengthenings

The exact composite Peano block reassembled in every test, but its pieces
cannot be signed independently. The following records were reported by the
independent adversarial run but are not implemented in the committed
Prompt-C evaluator, so they remain reproducible floating diagnostics rather
than interval-certified evidence:

- at exact rational encodings of
  \(\rho=0.029396287166985984,\ K=62.01949782520295\),
  one obtains \(C_1=-0.27051359814779065\ldots\), while the Peano term is
  \(1.45100264974657850\ldots\) and
  \(L_1=1.18048905159878785\ldots>0\);
- at exact rational encodings of
  \(\rho=0.14465799325730092,\ K=7.014826430594176\),
  \(C_{\rm top}=-0.04813896474428446\ldots\), while the terminal Peano
  term is \(1.1603595827217185\ldots\) and the top value is
  \(1.112220617977434\ldots>0\); and
- at \(\rho=999/1000,\ K=3200\), the complete-row Peano integral is
  \(-836450856.2765\ldots\), while
  \(C_1=3999396053.2917\ldots\) and
  \(L_1=3162945197.0152\ldots>0\).

These are diagnostic class-D failures of \(C_k\ge0\), \(C_{\rm top}\ge0\),
and blanket nonnegativity of the Peano integral. They do not falsify the
exact PBLOCK identity or any parent target.

### 5.3 Round 47 cell-self-charge strengthening

At

\[
 \rho=\frac9{10},\qquad K=40,\qquad\mu=36,\qquad a=29,
\]

independent Arb computations at 384 and 768 bits give

\[
 L_{29}=-0.40027816954933858788\ldots,\qquad
 \mathcal B_{4,29}+435L_{29}<-173.91.
\]

The literal value is exactly

\[
 \mathrm{WT}_4=\mathcal R_{\rm suf}=4301>0.
\]

This remains a class-D failure of cell self-charging only.

### 5.4 Round 48 continuous quarter-node strengthening

At the frozen exact rational interface-straddling record, independent Arb
evaluation at 768 and 1408 bits gives

\[
 \int_{n-1}^n\frac{\xi(t)^3}{3}\,dt
 -p(\xi(n-1/4))=-572.6942\ldots<0,
\]

but literal strict counting gives \(N=1412\) and

\[
 \int_{n-1}^n\frac{\xi(t)^3}{3}\,dt-S_2(N)
 =956715.73609\ldots>0.
\]

The parent discrete cell and independently evaluated full suffix remain
positive. This is class D and confirms that the rejected continuous proxy
has not re-entered Round 49.

### 5.5 Pointwise tail transport

At the rational input

\[
 \rho=\frac1{150},\qquad K=\frac{28431}{200},\qquad
 \mu=\frac{9477}{10000},
\]

a high-precision diagnostic gives

\[
 D(1/2)=-0.01232549980230\ldots<0,\qquad
 \mathcal R_{\rm suf}=0.63369479224351\ldots>0.
\]

This record is floating diagnostic evidence, not a directed certificate.
The exact cumulative counterexample above already supplies a theorem-level
class-D obstruction.

## 6. Mandatory stress classes

The independent structured sweep covered all packet classes:

1. \(\tau\) just below, on, and just above integers;
2. \(B(\mu)\) approaching zero and one;
3. first normalized cells straddling the interface;
4. the shallow band \(\mu/\sqrt2<z<\mu\);
5. the seam \(z=\mu/\sqrt2\);
6. \(\widehat H\) near \(0,1/4,3/4,1\) modulo integers;
7. terminal-node appearance and disappearance;
8. integer and near-integer \(K,\mu,R\);
9. activity equality approached from the active side;
10. \(\rho\) near zero and one;
11. moderate frequency;
12. large \(K\) and large row count; and
13. the Round 47 and Round 48 route counterexamples.

Separate adversarial searches additionally included 90,806 broad
wall-biased records, 145,196 interface/terminal/thin-shell records, 78,024
rational-design records, and 61,835 dangerous right sides of suffix-owned
action walls. No class A, B, or C record occurred. Those searches are
diagnostic and do not cover the continuum.

The committed deterministic evaluator's reproducible run with seed 4902 and
60 randomized requests accepted 146 distinct records. Its smallest named
nondegenerate suffix was

\[
 1.3271254143911559\ldots\,10^{-6}>0
\]

at an immediately active \(\rho=10^{-4}\) record. The two independent suffix
forms and the two literal aggregate forms agreed to working precision.

Additional directed equality pressure included:

- an action wall just on the counted side at
  \(\rho=1/10,\ K=94861/25000\), with positive suffix
  \(0.0010334724973\ldots\);
- immediately active \(\rho=1/10000,\ K=163/50\), with positive suffix
  \(1.3695257770\ldots\,10^{-6}\);
- exact \(\tau=1\), with the interface endpoint owned by the last prefix
  cell and positive suffix \(6.6792139250\ldots\);
- exact \(R=3\), with \(a=R\) excluded and positive suffix
  \(2.3075169846\ldots\);
- exact \(A(5)+1/4=1\), with the strict count taking the lower value and
  positive \(\mathrm{WT}_4=\mathcal R_{\rm suf}=61.8490066632\ldots\); and
- exact \(\alpha=3/4\), with the terminal node excluded and a positive
  diagnostic suffix.

## 7. Endpoint and ownership audit

| face | adversarial result |
|---|---|
| \(b=0\) | prefix empty and suffix equals literal WT4 |
| \(\tau\in\mathbb Z\) | \(b=\tau\); interface endpoint stays in the last prefix cell |
| \(0<\tau-b<1\) | only normalized row 1 can contain the interface |
| \(\widehat H<3/4\) | no suffix node; positive continuous top only |
| \(\alpha=3/4\) | terminal node excluded by the literal strict inequality |
| \(K\in\mathbb Z\) | \(a=K\) excluded |
| \(\mu\in\mathbb Z\) | no extra atom or endpoint term |
| \(R\in\mathbb Z\) | \(a=R\) excluded; inverse count is \(R-1\) |
| inverse radius integer | \(M=r-1\), never \(r\) |
| action wall integer | strict bracket takes the lower value |
| formal \(R=0\) | all normalized terms vanish; not attained in the strict domain |
| activity equality | outside Round 49's strict-active domain |

No ceiling relaxation or double ownership was used.

## 8. Complete and top-cell checks

For every deterministic record, the evaluator separately prints every
complete \(L_k\), the terminal supply, its literal \(M_{\rm top}\), and
whether the top node is present. Summing those terms agrees with the spatial
clipped-action suffix. At \(\alpha=3/4\) the continuous top remains but the
node is absent. When \(q=0\), the first interface row and terminal row are
the same object and are counted once.

The Prompt-A Peano block was treated as an exact identity, not as an
independent sign theorem. Its one-crossing localization was checked against
the explicit inner curvature formula. The failures in Section 5 show that
neither separately signing its scalars nor a pointwise cumulative sign can
replace the still-unsigned weighted compensation.

## 9. Falsification table

| target | result | class |
|---|---|---|
| literal \(\mathrm{WT}_4\) | no negative found | E diagnostics only |
| R49 suffix | no negative found | E diagnostics only |
| R49-FB | no negative found | E diagnostics only |
| directed interface pressure point | all three parent quantities positive | E single-point certificate |
| cumulative radial-prefix majorization | exact negative rational bound | D |
| separate-sign Peano strengthenings | floating negative pieces; PBLOCK positive | D diagnostic |
| Round 47 cell self-charge | directed negative; literal WT4 positive | D |
| continuous quarter-node proxy | directed negative; literal cell positive | D |
| pointwise tail dominance | floating negative; suffix positive | D diagnostic |

    positive_coverage_certificate: FALSE

## 10. Dependency, loss, and no-double-counting ledger

- The independent evaluator uses only the shell action, strict bracket,
  inverse monotonicity, exact moment primitive, and finite sums.
- The two suffix forms and two WT4 forms are independent computational
  reconstructions; their agreement is a diagnostic consistency check.
- Directed records certify only the named signs and literal ownership
  ledgers.
- Finite positive sweeps lose all continuum information and prove no global
  lower bound.
- Class-D records reject only their named auxiliary strengthenings.
- Prefix and suffix height intervals are disjoint; suffix rows and terminal
  interval partition the clipped height.
- Every node belongs to one prefix, complete suffix, or terminal ledger.
- The first normalized row owns the interface; if it is terminal, it is not
  counted a second time.
- The fallback reserve is computed separately and is never added to an
  already-counted literal prefix contribution.

## 11. Adversarial verdict

No exact or directed counterexample to literal \(\mathrm{WT}_4\), R49, or
R49-FB was found. None of those targets is thereby proved.

The exact cumulative-majorization failure and the separate-sign Peano
failures block natural stronger routes, while the Round 47 and Round 48
regressions remain confined to their auxiliary proxies. The first unrepaired
implication is still the weighted compensation of the single adverse
shallow-inner curvature contribution by the literal ceiling ledger,
interface/terminal contribution, and retained positive outer/deep reserve.

    ADVERSARIAL VERDICT: STRUCTURAL PASS — FINAL SIGN OPEN
    R49: neither proved nor falsified
    R49-FB: neither proved nor falsified
    literal WT4: neither proved nor falsified
    general-dimensional theorem: unproved
    completed d=3 theorem: unchanged

No proof-obligation status change is justified.

## 12. Prompt-C files

- human/outbox/general-d-round-49-adversarial-interface-to-top.md
- computations/general_d_round49_independent_suffix_search.py
