# Round 44C: adversarial exact-scalar falsification

**Date:** 20 July 2026  
**Branch observed:** `codex/general-d-round-44-exact-gate-b`  
**Verdict:** no negative exact-owner witness found; finite positive evidence is diagnostic only  
**Gate trigger:** none

## 1. Scope, independence, and theorem boundary

This is Prompt C's independent counterexample search for only

\[
 \mathscr S=D_A(q)+\mathcal C_p+p(E-E_*).
\]

I did not read or import a Round 44 lead note, lead evaluator, or lead replay.
The executable imports no project evaluator at all.  It reconstructs the
actions, cap integrals, strict counts, owner, terminal decompositions, and
shelf trapezoid directly.  The Round 43 and Round 27 artifacts are used only
as mandatory regression data.

No statement below proves \(\mathscr S\geq0\) on a continuum.  The
general-dimensional theorem, its backbone, and
`SHELL-general-d-high-floor-first-drop-CST` remain open.

### Source-precedence clarifications

Three notation/ownership collisions were resolved explicitly.

1. Round 36 excluded the literal value \(\alpha=1\), whereas the higher
   precedence Round 44 packet expressly permits the exact limit geometry
   \(\mu=q+1\) while retaining the upper-\(\alpha\) one-sided labels.  The
   search therefore evaluates \(\mu=q+1\), not the next chart's literal
   \(\alpha=0\) owner.
2. Round 10 uses \(n=\lfloor\mu-r\rfloor\), whose upper-\(\alpha\)
   gap-side value for \(\mu=q+\alpha\), \(0<\alpha<1\), is \(p+m\).
   At the exact geometry \(\mu=q+1\), its literal floor is \(p+m+1\).
   Round 42 and the Round 44 packet instead reuse \(n\) for the synchronized
   count \(f-1=B_0+j\).
   The executable avoids the collision: it forms \(q=r+p+m\) directly and
   stores the latter quantity as `n_count`.
3. At an old inverse wall \(y_k=N\), the literal strict value is
   \([y_k]_< =N-1\), \(\eta_k=1\), but the outer-gap adverse side is
   \([y_k]^+_< =N\), \(\eta_k\downarrow0\).  The executable stores both.
   An unresolved equality is not admitted as a verified generic owner.

## 2. Independent exact-definition evaluator

Put

\[
 x=r+p,\qquad q=x+m,\qquad \mu=q+\alpha,
 \qquad K=\mu\sec t,
\]

and

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,
 \qquad A(z)=G_K(z)-G_\mu(z).
\]

The endpoint sweep uses \(\alpha=1\).  For each integer gap-side label
\(B\ge2\), the program solves

\[
 G_{\mu\sec t}(q)=B-\frac14
\]

with a signed high-precision bracket.  Selected brackets are rechecked with
512-bit directed Arb arithmetic.

### 2.1 Analytic cap and shelf integrals

The evaluator does not numerically integrate the action except for one
independent curvature regression.  It uses

\[
 I_a(z):=\int_z^aG_a(s)\,ds
 =\frac{a^2}{4\pi}
 \left[
 (1+2v^2)\arccos v-3v\sqrt{1-v^2}
 \right],\qquad v=\frac za.
\]

Thus

\[
 \mathcal C_p=
 2\{I_K(r)-I_K(x)-I_\mu(r)+I_\mu(x)\}
 -p\{A(r)+A(x)\}.
\]

This is independently cross-checked against

\[
 \int_0^p\frac{s(p-s)}\pi
 \left(
 \frac1{\sqrt{\mu^2-(r+s)^2}}
 -\frac1{\sqrt{K^2-(r+s)^2}}
 \right)ds.
\]

### 2.2 Direct strict terminal count

At the outer wall, \(B_{\rm lit}=Q=B_0=B-1\).  For
\(1\le k\le B_0\), let

\[
 \frac K\pi(\sin\theta_k-\theta_k\cos\theta_k)=k-\frac14,
 \qquad y_k=K\cos\theta_k-q.
\]

Interchanging the two finite counts gives the direct strict shell count

\[
 T_A(q)=Q+2\sum_{k=1}^{B_0}[y_k]_<.
\]

Therefore the evaluated defect is

\[
 \boxed{
 D_A(q)=2\{I_K(q)-I_\mu(q)\}
 -Q-2\sum_{k=1}^{B_0}[y_k]_<.}
\]

This is the count defining \(D_A(q)\), not a terminal tangent lower bound.
Every retained generic point has a positive distance from every integer
inverse cell boundary.  At a simultaneous exact old-inverse wall, the
program also forms the literal count and the adverse count separately; one
old collision lowers adverse \(D_A\) by exactly \(2\) relative to the
literal value.

### 2.3 Full owner gate

A high-precision point is retained only after all of the following checks.

- Integer grid \(r\in\mathbb N\), \(r\ge1\), with activity constant
  \(\gamma=3/4\), or half-integer grid
  \(r\in\mathbb N_0+1/2\), \(r\ge3/2\), with \(\gamma=2\).
- \(p\ge3\), \(m\ge1\), \(q\ge5\).
- The same ordinary floor at \(r\) and \(x\), followed by the literal first
  drop at \(x+1\).
- \(B_0=B-1\ge1\), \(j=f-B\ge0\), and
  \(f-1=B_0+j\).
- \(0\le E<E_*<1/2\), \(p>d_\rho m\), and
  \(p-d_\rho m>11/5\), where
  \(d_\rho=1-2t/\pi\).
- Strict dimension-labelled activity
  \[
  K^2-\frac{\pi^2}{(1-\cos t)^2}-\gamma>0.
  \]
- \(0<h<u<\beta<1/2\), with
  \[
  h=G_\mu(q),\quad
  u=G_K(q)-G_K(\mu),\quad
  \beta=\pi^{-1}\arccos(q/K),
  \]
  and the stronger inherited check \(u<\alpha/2\).
- Direct strict endpoint counts \(Q=B_{\rm lit}=B_0\).
- Every inverse count is assigned to a resolved literal/adverse cell.

Activity equality is rejected because it belongs to the no-mode owner.
Likewise \(E=E_*\) is rejected from this hard owner.

### 2.4 Terminal and Gate-B ledgers

With the selected inverse-side values, the program forms

\[
 \Omega_-=
 \sum_{k=1}^{B_0}
 \left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right),
 \qquad J=2I_\mu(q),
\]

\[
 L_T^+=\Omega_-+B_0\zeta+\frac1{2\beta}-J,
 \qquad
 L_T^0=\Omega_-+B_0\zeta+\frac9{16\beta}-J,
\]

and defines the exact numerical remainders

\[
 \mathcal R_{\rm tan}^+=D_A(q)-L_T^+,
 \qquad
 \mathcal R_{\rm tan}^0=D_A(q)-L_T^0.
\]

At every retained point it checks

\[
 \mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0
 =\frac1{16\beta},
\]

\[
 \Phi_\delta^+=L_T^++a_p\Delta+p(E-E_*),
\]

\[
 \mathscr S-\Phi_\delta^+
 =\mathcal R_{\rm tan}^++(\mathcal C_p-a_p\Delta)
 =\frac1{16\beta}+\mathcal R_{\rm tan}^0
  +(\mathcal C_p-a_p\Delta).
\]

It also records

\[
 \mathcal C_{\rm curv}:=
 \frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-
 \frac1{\sqrt{K^2-r^2}}
 \right)
\]

and both slacks
\(\mathcal C_p-\mathcal C_{\rm curv}\) and
\(\mathcal C_p-a_p\Delta\).

## 3. Search architecture and coverage sampled

The search is deliberately not structured like the earlier endpoint
generator.  It parameterizes a proposed point by
\((2r,p,m,B)\), solves the outer wall first, and only then discovers the
shelf floor \(f\).  A broad binary64 pass proposes records; no binary64
sign is used in the final ledger.  A stratified shortlist emphasizes:

- the smallest proposed \(\mathscr S\);
- both parity grids;
- \(B_0=1\);
- \(m=1,2\) and large \(p/m\);
- \(E_*-E\downarrow0\);
- \(e_p\downarrow0\);
- \(\eta_k\downarrow0\) and \(\eta_k\uparrow1\);
- small curvature and tangent slacks;
- compact, large-radius edge, and deterministic logarithmic random data.

The proposal ranges include \(r\) through approximately \(10^6\),
\(p\) through \(3000\), \(m\) through \(1000\), and \(B\) through
\(256\).  Exact-owner survivors happened to have

\[
 1\le r\le977187.5,\qquad
 3\le p\le32,\qquad
 1\le m\le32,\qquad
 2\le B\le96.
\]

This finite box and the shortlist are not a coverage certificate.

The deterministic run produced:

| stage | count |
|---|---:|
| distinct binary64 proposals | 629,288 |
| binary64 owner candidates | 296 |
| binary64 negative \(\mathscr S\) candidates | 0 |
| 90-decimal records rebuilt | 296 |
| exact-owner records after rebuild | 296 |
| integer-grid owners | 155 |
| half-integer-grid owners | 141 |
| \(B_0=1\) owners | 81 |
| high-precision negative owners | 0 |

The 296 records divide into 32 compact, 190 edge, and 74 logarithmic-random
survivors.

## 4. Diagnostic minima

No negative \(\mathscr S\) was found.  The observed minima are:

| subset | tuple \((r,p,m,f,B,j)\) | \(\mathscr S\) |
|---|---|---:|
| all owners | \((1,3,1,2,2,0)\) | 2.69456527890035502562933 |
| integer grid | \((1,3,1,2,2,0)\) | 2.69456527890035502562933 |
| half-integer grid | \((3/2,3,1,2,2,0)\) | 2.97730771069662464599676 |
| \(B_0=1\) | \((1,3,1,2,2,0)\) | 2.69456527890035502562933 |
| \(m=1\) | \((1,3,1,2,2,0)\) | 2.69456527890035502562933 |
| \(p\ge20\) | \((40205,26,1,2,2,0)\) | 60.9345544436144371581521 |
| largest retained \(p=32\) | \((104714,32,1,2,2,0)\) | 81.7307006111919828276211 |

Adversarial face probes remained positive:

| probe | parameters / distance | \(\mathscr S\) |
|---|---|---:|
| closest hard seam | \(r=5/2,p=4,m=1,B=2\), \(E_*-E=2.7381932843765\times10^{-4}\) | 4.15536923294885410495 |
| closest lower shelf | \(r=1,p=4,m=7,B=6\), \(e_p=0.00154660738487163\) | 12.5758306731125444223 |
| closest adverse inverse side | \(\eta_{36}=4.52303097808\times10^{-6}\) | 144.312794380275259483 |
| closest literal inverse side | \(1-\eta_{40}=2.27147817351\times10^{-4}\) | 159.438708856736012484 |

No exact old-inverse collision was encountered.  The closest adverse
distance was still more than \(10^{39}\) times the 90-decimal ambiguity
threshold used by the search.

Across the sampled owners, the observed component minima were

\[
 \min D_A(q)=3.05382951682019802727,
\]

\[
 \min\mathcal C_p=0.00321848288235667413,
\]

\[
 \min\mathcal R_{\rm tan}^+=0.70603488511680083919,
 \qquad
 \min\mathcal R_{\rm tan}^0=0.53573924076745802036.
\]

The smallest observed curvature-reserve slack was
\(4.48117922479756\times10^{-4}\), and the smallest observed
\(\mathcal C_p-a_p\Delta\) was
\(3.04072041979763\times10^{-4}\).  These are diagnostics, not uniform
lower bounds.

## 5. Complete ledger at the diagnostic minimum

The minimum record is

\[
 (r,p,m,f,B,j)=(1,3,1,2,2,0),\qquad
 x=4,\quad q=5,\quad\mu=6.
\]

Its high-precision wall root is

\[
 t=1.062253041739245313430290876278361\ldots,
 \qquad K=12.32272250535093330028502454113864\ldots.
\]

The complete owner data are:

| quantity | value |
|---|---:|
| \(d_\rho\) | 0.3237487103711907653433554960050774 |
| \(p-d_\rho m\) | 2.676251289628809234656644503994923 |
| activity margin | 113.6104050500780950717189931742609 |
| \(e_0\) | 0.2489200052579142092050058132469662 |
| \(e_p\) | 0.02832499639500714126904157636342719 |
| \(E\) | 0.2772450016529213504740473896103934 |
| \(E_*\) | 0.4460418816048015391094407506658204 |
| \(h\) | 0.1235669661456793870010622855994645 |
| \(u\) | 0.3526763091287286708879677237212936 |
| \(\beta\) | 0.3670087995426830261961793145736484 |

The unique old inverse level has

\[
 \theta_1=0.8514269471566438181228887197817985\ldots,
 \qquad
 y_1=3.119570469666465168096721597715024\ldots.
\]

Hence \([y_1]_< =3\), \(Q=1\), and the direct strict terminal count is

\[
 T_A(q)=1+2(3)=7.
\]

The complete requested scalar ledger is:

| quantity | value |
|---|---:|
| \(D_A(q)\) | 3.053829516820198027272270577811746 |
| \(L_T^+\) | 2.347794631703397188083273339144058 |
| \(L_T^0\) | 2.518090276052740006908906877115456 |
| \(\mathcal R_{\rm tan}^+\) | 0.7060348851168008391889972386676878 |
| \(\mathcal R_{\rm tan}^0\) | 0.5357392407674580203633637006962902 |
| \(\mathcal C_p\) | 0.1471264019357975642632424201048155 |
| \(a_p\Delta\) | 0.1323570053177442407615785421301234 |
| \(\mathcal C_p-a_p\Delta\) | 0.0147693966180533235016638779746921 |
| \(p(E_*-E)\) | 0.5063906398556405659061800831662812 |
| \(\Phi_\delta^+\) | 1.973760997165500862938671798107900 |
| \(\mathscr S\) | 2.694565278900355025629332914750280 |

The terminal reconciliation is numerical to 90-decimal working precision:

\[
 \frac1{16\beta}
 =0.1702956443493428188256335379713977\ldots,
\]

\[
 \mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0
 =0.1702956443493428188256335379713976\ldots.
\]

The computed residual is \(6.14\times10^{-92}\).  The Gate-B loss is

\[
 \mathscr S-\Phi_\delta^+
 =0.720804281734854162690661116642380\ldots
\]

and

\[
 \mathcal R_{\rm tan}^+
 +(\mathcal C_p-a_p\Delta)
 =0.720804281734854162690661116642380\ldots.
\]

Both displayed Gate-B ledger residuals are below
\(1.3\times10^{-91}\).

### Curvature reserve

At this point

\[
 \mathcal C_{\rm curv}
 =0.1254941112463187281679572194883795\ldots,
\]

\[
 \mathcal C_p-\mathcal C_{\rm curv}
 =0.0216322906894788360952852006164360\ldots>0.
\]

The independent weighted-curvature quadrature returns

\[
 0.1471264019357975642632424201048155096499\ldots,
\]

agreeing with \(\mathcal C_p\) to a residual of
\(3.99\times10^{-91}\).

## 6. Directed wall verification

For the diagnostic-minimum wall, rational endpoints at 60 decimal places
give

\[
\begin{aligned}
 t_-&=1.062253041739245313430290876278360676818658840575176428461595,\\
 t_+&=1.062253041739245313430290876278360676818658840575176428461596.
\end{aligned}
\]

At 512 Arb bits,

\[
 F(t_-)=-2.65169332588960\ldots\times10^{-60}<0,
 \qquad
 F(t_+)=3.77948130635646\ldots\times10^{-60}>0.
\]

This is a directed verification of the wall bracket only.  It is not
promoted into a positive certificate for \(\mathscr S\).

## 7. Mandatory regressions

### 7.1 Round 43 rejected tuple

The evaluator independently reproduces

\[
 (r,p,m,f,B,j)=(1,9,9,4,3,1),
\]

with common shelf floor \(4\), first-drop floor \(3\), and no owner failure
other than the hard remainder condition.  It gives

\[
 E=0.3280024860904139535875790815032754\ldots,
\]

\[
 E_*=0.2913519205358295521892713132069391\ldots,
\]

\[
 E-E_*=0.03665056555458440139830776829633625\ldots>0.
\]

It is therefore rejected exactly because \(E>E_*\).  Its outer wall was
also directionally bracketed:

\[
 0.915309053164639337163232467838059145837418678709093957843997
 <t<
 0.915309053164639337163232467838059145837418678709093957843998.
\]

The Arb endpoint residuals have strict signs
\(-2.71135\times10^{-60}\) and \(8.36281\times10^{-60}\).

### 7.2 Round 27 automatic-sector witness

For

\[
 (r,p,m,f,\alpha,t)=
 \left(4036,32,1,2,\frac1{16},\frac{79}{500}\right),
\]

the independent evaluator obtains

\[
 \mathcal C_{\max,8}
 =-1.357650017320433289877150582638353\ldots,
\]

\[
 \mathcal R_J
 =-1.232653692824895881798926879174007\ldots,
\]

while the direct strict count gives

\[
 D_A(q)=27.82817120625015174921353800087307\ldots,
\]

\[
 R_p=18.86130901583899514746055005075139\ldots,
\]

\[
 \boxed{\mathscr S
 =47.13918726007210797057112078239874\ldots>47.}
\]

Moreover

\[
 E-E_*=0.515878125594559146741720461365003\ldots>0,
\]

so this point is automatic/remainder-rich and is rejected from the present
hard owner.

This entire sign regression was rerun with 512-bit directed Arb arithmetic:

\[
 \mathcal C_{\max,8}<-\frac43,\qquad
 \mathcal R_J<-\frac65,\qquad
 \mathscr S>47,\qquad E-E_*>0.
\]

Thus negative rejected scalars do coexist with a large positive exact
\(\mathscr S\), as required.

### 7.3 Terminal decomposition and curvature regressions

The numerical terminal decomposition and
\(1/(16\beta)\) reconciliation are displayed in Section 5.  The exact
trapezoid/curvature-kernel agreement and the elementary curvature reserve
are displayed there as well.  All four mandatory regressions pass.

## 8. Separate one-sided \(\alpha\uparrow1\) solves

For the diagnostic-minimum discrete tuple, the wall equation was solved
again at every \(\alpha=1-10^{-s}\); the endpoint value of \(t\) was never
reused.

| \(s\) | \(\alpha\) | separately solved \(t\) | \(\mathscr S\) | \(\mathscr S-\mathscr S_{\alpha=1}\) |
|---:|---:|---:|---:|---:|
| 3 | 0.999 | 1.062345947296305655505030360191146 | 2.696483351842287785162737144719 | \(1.91807294193276\times10^{-3}\) |
| 6 | 0.999999 | 1.062253134647205623428619610340837 | 2.694567197175405237663892056073 | \(1.91827505021203\times10^{-6}\) |
| 9 | 0.999999999 | 1.062253041832153276143796846473394 | 2.694565280818630277961123288120 | \(1.91827525233179\times10^{-9}\) |
| 12 | 0.999999999999 | 1.062253041739338221393006785756455 | 2.694565278902273300881866824891 | \(1.91827525253391\times10^{-12}\) |

All four nearby points retain the owner.  As an algebraic check, the
separately solved values give the same \(K\), because the outer action
equation fixes \(K\) from \((q,B)\); \(t=\arccos(\mu/K)\) nevertheless
changes at every \(\alpha\), exactly as the prompt requires.

These convergence values use 90-decimal floating arithmetic and are
diagnostic, not directed interval conclusions.

## 9. Classification of conclusions

The arithmetic classifications are deliberately separated.

| statement | classification |
|---|---|
| 629,288-point proposal sweep and all reported minima | floating diagnostic |
| 296 exact-definition owner rebuilds | 90-decimal diagnostic with resolved strict cells |
| scalar and terminal identity residuals | high-precision algebraic replay, not a proof |
| selected minimum and Round 43 wall brackets | 512-bit directed Arb brackets |
| Round 27 rejected-scalar signs, \(\mathscr S>47\), and \(E>E_*\) | 512-bit directed Arb regression |
| no negative found | diagnostic only; not positive coverage |
| universal \(\mathscr S\ge0\) | not proved |
| `gate_trigger_certificate` | not created |

No floating negative occurred, so there was no candidate to promote into a
directed full-owner negative certificate.  In particular, this report does
not authorize a Gate-B stop and does not authorize a positive coverage
certificate.

## 10. Reproduction

Run from the repository root:

```powershell
python -B computations/general_d_round44_independent_gate_b_search.py
```

The deterministic summary begins:

```text
binary64_proposals=629288
binary64_owner_candidates=296
binary64_negative_S_candidates=0
high_precision_shortlist=296
high_precision_exact_owner_records=296
high_precision_rejected_after_exact_recheck=0
high_precision_negative_owner_records=0
high_precision_owner_counts integer=155 half_integer=141 B0_equals_1=81 compact=32 edge=190 random=74
diagnostic_only global_min r=1.0 p=3 m=1 f=2 B=2 B0=1 j=0 grid=integer S=2.69456527890035502562933
negative_owner_witness_found=False
positive_coverage_certificate=False
conclusion=finite_positive_diagnostic_only; Gate-B universal sign remains open
```

The executable then prints the full scalar ledger for the global minimum,
the closest hard seam, the closest lower shelf, both closest inverse sides,
the tightest curvature record, and a large-\(p\) record; the directed wall
and Round 27 regressions; the curvature-kernel replay; and the separate
one-sided convergence solves.

A separate 120-decimal stability rerun,

```powershell
$env:GENERAL_D_ROUND44_DPS='120'
python -B computations/general_d_round44_independent_gate_b_search.py
```

retained the same 296 exact owners, the same minimum and minimizing tuple,
and no negative owner.  Its curvature-kernel residual at the minimum was
\(2.66\times10^{-121}\).

## 11. Files and repository state

Files created by this task:

- `computations/general_d_round44_independent_gate_b_search.py`
- `human/outbox/general-d-round-44-adversarial-exact-scalar-falsification.md`

No state, manuscript, prompt, lead artifact, or other file was modified.
No commit was created.
