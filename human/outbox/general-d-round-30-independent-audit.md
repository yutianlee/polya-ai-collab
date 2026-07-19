# General dimension, Round 30: independent audit

Date: 19 July 2026  
Verdict: PASS after correction

## 1. Audited artifacts

- human/outbox/general-d-round-30-nonconstant-K-endpoint-reductions-and-retained-E-shelf-scalar.md
  - SHA-256:
    d63d4c98e7f347f713e4fe4d67d0be2ab28137f805dd9baba8c8314e06df0ab8
- computations/general_d_round30_endpoint_derivatives.wl
  - SHA-256:
    62be931ba47872aad2877c76937e47ef67577f4ca67c63f683c77302455086ff
- computations/general_d_round30_retained_shelf_diagnostic.py
  - SHA-256:
    4e5ca455e64af0ad39572a9f02aa39ca6f6130c3b8cddbf550f348150e5f1b86

The audit was performed against these current hashes.  It did not infer any
continuum statement from the diagnostic scan.

## 2. Corrections required during audit

The pre-audit draft required the following repairs.

1. Three missing plus signs were restored in the complete terminal and
   endpoint formulas.
2. The continuous quadratic completion was changed from a strict inequality
   to a weak one; the surrounding projected inequality remains strict.
3. The \(\xi=1/2\) terminal seam was handled explicitly through its strictly
   positive top interval.
4. The inverse/top lower estimate was stated as weak before the later strict
   \(\theta<1\) comparison.
5. The endpoint proof \(L_T>T(q)\) and the unit-cap proof of
   \(T(q)>7/10\) were inserted explicitly.
6. The unsupported \(H\)-endpoint decimals were replaced by exact
   rational Taylor enclosures replayed in Mathematica.
7. Scope language was narrowed: \(\mathfrak F>0\) is the isolated
   lower-shelf obstruction, not the sole surviving high-floor endpoint
   family.
8. The seven \(\alpha=0\) patterns are now described as replayed diagnostic
   patterns, not as a proved exhaustive list.
9. A stronger proof that activity is automatic throughout the entire
   \(B=Q=1,\ 2<y_1<3\) band was added.

The verdict below applies only after these repairs.

## 3. Analytic audit

### 3.1 Whole-band activity

The chain

\[
 \theta<1,\qquad K-(q+y_1)>\frac{3\pi}{4},\qquad
 K-\mu>1+\frac{3\pi}{4}
\]

is valid.  Together with \(K>5\) and \(\pi<22/7\), it gives

\[
 K^2-\frac{\pi^2}{(1-\mu/K)^2}
 >\frac{6825}{2209}>2.
\]

This removes the activity endpoint on both inherited grids throughout the
first inverse band.

### 3.2 Included lower shelf

The exact identities

\[
 K_\mu=\frac{\sin\chi_x}{\sin\psi_x}\in(0,1),\qquad
 t_\mu<0,\qquad E_\mu<0,\qquad\lambda_\mu>0
\]

were independently differentiated.  The cap estimate \(J_\mu<K_\mu\) has
the correct direction and constants.  Hence

\[
 (L_T)_\mu>
 \frac{4K_\mu}{\pi}-J_\mu>0.
\]

The uniform estimate

\[
 L_T>\frac7{10}
\]

also checks.  The exact rational excess is

\[
 \frac{44599}{51304}
 -\frac{5936}{35964}
 -\frac7{10}
 =\frac{9812441}{2306371320}>0.
\]

The monotonic directions

\[
 E\ge E_{\min},\qquad
 \mathcal K_4\ge\mathcal K_{4,\min},\qquad
 d\ge d_{\min},\qquad L_T>T(q)
\]

are all correct, so the retained-\(E\) scalar reduction

\[
 \Psi^{L_T}_{4,E}>\mathfrak F(q,r,p,m)
\]

is valid.

### 3.3 Lower \(Q\)-wall

The intrinsic parametrization gives

\[
 K_\mu=\frac{\sin\phi}{\sin\psi}\in(0,1),\qquad t_\mu<0.
\]

Along the wall, \(A(z)\), \(E\), \(\Delta\), and \(\mathcal K_4\)
decrease, while \(\lambda\) increases.  The exact count geometry

\[
 B=1,\qquad 0<y_1<\alpha<1
\]

is correct.  Thus the open lower \(Q\)-wall has no inverse or outer-\(B\)
intersection.  Its complete terminal term satisfies

\[
 L_Q>\frac3{28}+2y_1>0,\qquad (L_Q)_\mu>0.
\]

Literal lower and upper \(Q/B\) ownership and all displayed raw jumps were
checked.  The note correctly refrains from asserting monotonicity of the
full projected scalar.

### 3.4 The \(\alpha=0\) face

The concavity argument gives

\[
 L_T>1+2\eta_1
\]

on the full stated cell, including the \(\xi=1/2\) seam and the bad
\(y_1\downarrow2^+\) limit.  The normalized curvature product, continuous
quadratic minimum, and \(R\)-supremum are correct.  The count \(B=1\)
implies \(t<13/10\), and the exact endpoint enclosures

\[
 H(4/5)<\frac{19359908900}{19876504599}<1,
\]

\[
 H(13/10)<\frac{357336260800}{634633671763}<1
\]

are valid.  The logarithmic derivative has at most one zero and that zero
is a minimum, so \(H<1\) throughout the phase interval.  Therefore the
claimed \(t\ge4/5\) closure is valid.

## 4. Replay results

Mathematica 15 returned seventeen zero symbolic residuals and twelve true
rational signs:

    round30EndpointDerivativeReplayOK=True

The finite Python diagnostic passed at both limits used in the audit:

    --limit 300:  933 retained records, 0 nonpositive
    --limit 1000: 933 retained records, 0 nonpositive

Both runs returned

\[
 \mathfrak F(5,1,3,1)
 =0.300903146691255\ldots
\]

as their smallest retained value.  The script explicitly reports
infiniteQCoverage=False and diagnosticOnly=True.

The following mechanical checks also passed:

- Python byte compilation;
- git diff --check;
- control-character scan of all three Round 30 artifacts.

## 5. Status boundary

Round 30 proves analytic face reductions.  It does not prove
\(\mathfrak F>0\) on the infinite domain, full-\(\Psi\) monotonicity on
the shelf or \(Q\)-wall, high-floor CST, pointwise assembly, or the
all-dimensional theorem.

The next proof target is the necessary-domain incompatibility or direct
positivity of \(\mathfrak F\), starting with the observed disappearance of
relaxed hard/shelf records above \(q=33\).  That disappearance remains
diagnostic until proved.

