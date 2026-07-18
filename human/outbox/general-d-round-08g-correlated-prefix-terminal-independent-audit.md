# General dimension, Round 8G: independent audit — FINAL PASS

Date: 2026-07-18

Status: **FINAL PASS**.

This is an independent audit of the provisional Round 8G proof note and its verifier.  The audited claim is only the high-floor first-drop band

\[
 \frac{23}{25}\leq \rho\leq \frac{1847}{2000}.
\]

Together with frozen Round 8F, this covers the larger-ratio region.  It does not certify the explicitly retained fixed-ratio wall below \(\rho=23/25\).

## 1. Frozen artifacts and source integrity

The audited artifacts are:

- `human/outbox/general-d-round-08g-correlated-prefix-terminal.md`, 15,781 bytes, SHA-256 `C45D339383FD4E6921C3C60D058E14628846DF57E7F7808D62B373AB2476DE90`;
- `scripts/general_d_round_08g_correlated_prefix_verify.py`, 17,434 bytes, SHA-256 `873D9E4259DC0827C8917EB8CD04C169303B8D973C332CD2A75DA5038FC19F34`.

The final note differs from the earlier 15,778-byte artifact only by the insertion of one missing backslash before `qquad` at each of lines 150, 378, and 648.  As a byte-level check, deleting exactly those three backslashes in memory reconstructs SHA-256 `B3FD67EDE7BF7B8666ED94DC06F43AD7AD19A693378C7637352AA4C1576BDE66`, the earlier hash, and reconstructs the earlier byte count exactly.  A negative-lookbehind scan finds zero remaining unescaped `qquad` tokens.

The verifier compiles from source.  Before importing any Round 8F implementation it rehashes and pins:

- `scripts/general_d_high_floor_signed_prefix_verify.py`: `066A64BE535AFE212B107928D7845E9BC27D210D144A9E99FDE16DCCDF5A866C`;
- `human/outbox/general-d-round-08f-signed-prefix-terminal.md`: `ABAFE9A9C0B57607CA0945313D0C0A7B1602D6067D84587F14C274898EF7D196`.

Both current hashes equal the embedded pins.

## 2. Exact correlated prefix and the \(\gamma\) wall

Write

\[
 c=\frac{\theta}{\pi},\qquad
 \Phi=\sin\theta-\theta\cos\theta,\qquad
 \beta=\frac{123}{1000}-c,
\]

and

\[
 R(\theta)=\frac{\theta\cos\theta}{\Phi},\qquad
 \gamma(\theta)=\beta R(\theta).
\]

At the endpoint with the smallest \(c\), namely \(\rho=1847/2000\), the independently evaluated gap is

\[
 c-\frac{123}{1000}=0.00231531202199959\ldots>0.
\]

Hence \(\beta<0\) strictly on the whole band.  The multiplication direction in the common-prefix step is therefore correct: from \(M\leq\mu\), multiplication by \(\beta<0\) gives \(\beta M\geq\beta\mu\), and the strict prefix estimate yields

\[
 cP>\gamma W-\frac{cd}{2}.
\]

No sign is lost in this substitution.

Direct differentiation gives

\[
 R'(\theta)
 =\frac{\sin\theta\cos\theta-\theta}{\Phi^2}<0,
 \qquad
 \gamma'(\theta)=-\frac{R(\theta)}{\pi}+\beta R'(\theta).
\]

The verifier encloses this derivative on 64 complete rational \(\rho\)-panels and proves the strict upper wall \(\gamma'<-49/10\) on every panel.  The union of its directed enclosures is

\[
 [-5.59580090175,-4.98627997162].
\]

Thus \(\gamma\) decreases as \(\theta\) increases, so its minimum is at \(\rho=23/25\).  There

\[
 \gamma+\frac9{100}
 >0.000255526635797,
\]

and therefore

\[
 -\frac9{100}<\gamma<0
\]

strictly throughout the audited band.  The accompanying endpoint walls

\[
 \theta^2<\frac{163}{1000},\qquad c<\frac{641}{5000}
\]

also have positive numerical gaps: \(0.000819950939979\ldots\) and \(0.0000115663020501\ldots\), respectively.

## 3. Active width and all terminal strata

For

\[
 \lambda(\theta)=\frac{\Phi}{1-\cos\theta},
\]

one has

\[
 \lambda'(\theta)
 =\frac{\sin\theta\,(\theta-\sin\theta)}{(1-\cos\theta)^2}>0.
\]

The minimum is therefore at \(\rho=1847/2000\), where the independent value is \(0.261778019217802\ldots>229/875\).  Since the inherited active interval gives \(W>\lambda(W+\delta)\) and \(W+\delta\geq7/4\), it follows strictly that

\[
 W>\frac{229}{500}.
\]

The alternatives \(B_0\geq1\), \(B_0=Q=0\), and \(B_0=0,Q=1\) are exhaustive because \(Q\leq B_0+1\).  Every direction in their reductions checks:

- For \(B_0\geq1\), the use of \(W\leq B_0+3/4\) is in the lower-bound direction because \(\gamma<0\).  The \(B_0\)-coefficient satisfies
  \[
  \frac12-c+\gamma>\frac{1409}{5000}>0,
  \]
  so the minimum is at \(B_0=1\).
- For \(B_0=Q=0\), the derivative in \(W\) is bounded by
  \[
  2W+\gamma>\frac{413}{500}>0,
  \]
  so the lower width wall may be used.
- For \(B_0=0,Q=1\), \(W\in(3/4-c,3/4]\) and the reduced quadratic is concave in \(W\); it is therefore enough to test both endpoints.  Both endpoint functions decrease in \(c\) and increase in \(\gamma\), so \(c<641/5000\) and \(\gamma>-9/100\) are inserted in the correct directions.

The resulting proof floors are exact `fmpq` computations:

| quantity | exact lower floor | decimal value |
|---|---:|---:|
| \(B_0\)-coefficient | \(1409/5000\) | \(0.2818\) |
| \(Q=0\) derivative | \(413/500\) | \(0.826\) |
| \(B_0\geq1\) terminal ledger | \(1280143/75000000\) | \(0.0170685733\ldots\) |
| \(B_0=Q=0\) ledger | \(3021981/25000000\) | \(0.12087924\) |
| \(B_0=0,Q=1\), upper endpoint | \(7978381/25000000\) | \(0.31913524\) |
| \(B_0=0,Q=1\), lower endpoint | \(157119/500000\) | \(0.314238\) |

All are strictly positive.  The verifier additionally replays the correlated quantities on 256 complete rational panels.  Those directed panel minima are extra consistency checks, not replacements for the exact rational proof floors.  This separation is explicit in both the note and code.

## 4. Retained ratio, level distance, and series domains

For \(\epsilon=1-\rho\), define

\[
 \kappa(\theta)=\frac{\Phi}{\theta\rho\epsilon}.
\]

With

\[
 \frac{d}{d\theta}(\theta\rho\epsilon)
 =\rho\epsilon+\theta\sin\theta(2\rho-1),
\]

the verifier encloses the exact quotient-rule numerator

\[
 \theta\sin\theta\,(\theta\rho\epsilon)
 -\Phi\{\rho\epsilon+\theta\sin\theta(2\rho-1)\}
\]

on 64 full panels.  Its smallest directed lower bound is \(0.000190444285561\), so \(\kappa\) is strictly increasing in \(\theta\).  Its minimum is at \(\rho=1847/2000\), where

\[
 \kappa-\frac{18}{25}>1.6195058963\times10^{-5}.
\]

The improved small argument is valid on the full band:

\[
 u_0
 <\frac{29}{10}\frac59\frac{163/1000}{23/25}
 =\frac{4727}{16560}
 <\frac{143}{500}.
\]

The retained scale is \((261/125)x\).  Since \(x\leq5/3\), its largest value is \(87/25\), and \(\epsilon\leq2/25\).  Thus the subtracted-copy series variable obeys

\[
 z\leq\frac{174}{625}<1,
\]

while the separate first-copy expansion has \(z\leq224/625<1\).  Both power-series uses are therefore inside their convergence domains.

For

\[
 S(z)=\sum_{n\geq0}
 \frac{\binom{2n}{n}}{8^n(2n+1)}z^n,
\]

the coefficient ratio

\[
 \frac{(2n+1)^2}{4(n+1)(2n+3)}<1
\]

shows that the positive coefficients decrease.  Retaining through \(a_3=5/896\) and summing the remaining geometric majorant gives the exact quadratic coefficient

\[
 \frac3{160}
 +\frac5{896}\frac{174/625}{1-174/625}
 =\frac{21117}{1010240}
 <\frac{21}{1000}.
\]

Its integrated ceiling is consequently \((21/1000)(2/7)=3/500\), as used in the proof.

The Taylor lower bound for \(C_\rho\) is also directed correctly.  The auxiliary quotient

\[
 \frac{(1/2-t/24)^{3/2}}{1/3-t/30+t^2/840}
\]

decreases for \(0\leq t\leq163/1000\); after differentiation, the relevant sign is controlled by \(t^2-20t-168<0\).  Evaluation at the upper endpoint gives

\[
 C_\rho>1.37424804127147\ldots>\frac{137}{100}.
\]

The inherited concavity reduction to \(x\in\{1/7,5/3\}\) is used without changing its hypotheses.  The verifier uses 64 full \(\rho\)-panels and both \(x\)-endpoints, for 128 directed endpoint checks.  It proves positivity of the retained integral before replacing \(C_\rho\) by its lower floor, so that replacement is in the safe direction.  The smallest replayed values are

\[
 \text{level-distance margin}>0.0214999332585,
 \qquad
 \text{retained integral}>0.211576376293.
\]

## 5. The small-\(\delta\) interval

With \(L=29/10\), the coefficient of \(\delta\) is

\[
 \frac{3-L}{4}-c.
\]

It is strictly negative because \(c>123/1000\).  Hence on \(0<\delta<1\) the lower endpoint is obtained at \(\delta=1\).  The remaining scalar

\[
 \frac54-\frac{5L}{16}-\frac83c+c^2
\]

decreases over the relevant \(c\)-range, and substitution of \(c=641/5000\) gives the exact strict floor

\[
 \frac{1373893}{75000000}>0.
\]

Thus the small-\(\delta\) reduction has the correct endpoint and strict sign.

## 6. Fixed-ratio cutoff and integer rounding

The endpoint directions give

\[
 \eta>\frac1{147},\qquad \eta<\frac19,
 \qquad a<23\pi<\frac{8165}{113}.
\]

The inherited upper wall \(C_*<13/10\) gives

\[
 a+2\eta C_*<\frac{368894}{5085}<73
\]

and therefore

\[
 K_0(\rho)<73\cdot147^2=1\,577\,457.
\]

Here the separate inherited lower wall \(C_*>1/2\) is what makes the square-root term in the fixed-ratio threshold strictly smaller than the displayed left side.

All subsequent strict-to-integer conversions are conservative:

\[
 \rho>\frac1{3\,154\,914},\qquad
 2r\leq3\,154\,913,
\]

\[
 n\leq1\,577\,456,
 \qquad
 f,B\leq525\,819.
\]

No equality case is admitted by rounding a strict real inequality in the wrong direction.

## 7. Directed arithmetic audit

Every panel endpoint is an exact rational.  The imported `interval_ball` routine constructs an Arb midpoint-radius enclosure and then explicitly checks containment of both rational endpoints.  Positive signs are asserted from strict positive lower endpoints, and negative signs from strict negative upper endpoints.  Positive odd half-powers are computed as a square root times an integer power, so no branch ambiguity is introduced.  Exact scalar ledgers and cutoff arithmetic use `fmpq`, not binary floating point; floating-point conversions occur only when printing already-certified margins.

The verifier states the residual limitation in its final output, so the certificate does not silently claim the unresolved region

\[
 \frac1{3\,154\,914}<\rho<\frac{23}{25},
 \qquad
 \frac{21}{4}<K<1\,577\,457.
\]

## 8. Independent four-precision replay

Each run used a fresh process with `GENERAL_D_ARB_PREC` set before startup.  All four runs exited 0, emitted zero stderr characters, reported the requested precision, printed the certification line, and printed the residual disclaimer.

Terminal-prefix results:

| precision | exit | stderr chars | \(\gamma'\) enclosure union | \(\gamma+9/100\) | \(B_0\) coefficient | \(B_0\) ledger |
|---:|---:|---:|---:|---:|---:|---:|
| 384 | 0 | 0 | \([-5.59580090175,-4.98627997162]\) | 0.000255526635797 | 0.281907873981 | 0.0172635643784 |
| 512 | 0 | 0 | \([-5.59580090175,-4.98627997162]\) | 0.000255526635797 | 0.281907873981 | 0.0172635643779 |
| 768 | 0 | 0 | \([-5.59580090175,-4.98627997162]\) | 0.000255526635797 | 0.281907873981 | 0.0172635643784 |
| 1024 | 0 | 0 | \([-5.59580090175,-4.98627997162]\) | 0.000255526635797 | 0.281907873981 | 0.0172635643779 |

Remaining terminal minima:

| precision | \(Q=0\) derivative | \(Q=0\) ledger | \(Q=1\) upper | \(Q=1\) lower |
|---:|---:|---:|---:|---:|
| 384 | 0.826096309901 | 0.120924743146 | 0.319220429717 | 0.314297954935 |
| 512 | 0.826096309901 | 0.120924743146 | 0.319220429717 | 0.314297954935 |
| 768 | 0.826096309901 | 0.120924743146 | 0.319220429717 | 0.314297954935 |
| 1024 | 0.826096309901 | 0.120924743146 | 0.319220429717 | 0.314297954935 |

Retained-ratio and level-distance minima:

| precision | \(\kappa\)-derivative numerator | \(\kappa-18/25\) | level-distance margin | retained integral |
|---:|---:|---:|---:|---:|
| 384 | 0.000190444285561 | \(1.6195058963\times10^{-5}\) | 0.0214999332585 | 0.211576376293 |
| 512 | 0.000190444285561 | \(1.6195058963\times10^{-5}\) | 0.0214999332594 | 0.211576376293 |
| 768 | 0.000190444285561 | \(1.6195058963\times10^{-5}\) | 0.0214999332585 | 0.211576376293 |
| 1024 | 0.000190444285561 | \(1.6195058963\times10^{-5}\) | 0.0214999332585 | 0.211576376293 |

The small changes in the last printed digits are harmless outward-enclosure variation.  Every strict lower margin remains far above zero at every tested precision.

## 9. Verdict

**FINAL PASS.**  The exact negative-prefix substitution, all monotonicity directions, terminal-stratum exhaustion, exact rational floors, retained-series estimates, concavity endpoint reduction, small-\(\delta\) reduction, cutoff arithmetic, integer rounding, and directed Arb implementation agree.  The four independent executions are stable and clean.  No analytic, implementation, reproduction, or scope defect remains in the audited Round 8G artifacts.
