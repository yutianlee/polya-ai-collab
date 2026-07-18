# Independent audit: Round 8E refined cap and absent-level chord

Date: 18 July 2026  
Status: **FINAL PASS**

Audited frozen targets:

- `human/outbox/general-d-round-08e-refined-cap-terminal.md`  
  corrected SHA-256 `38DE6AE72ACE3674096A9231A590ADCA1C2CE958BAFA777370AF65A3C2A9EB66`;
- `scripts/general_d_high_floor_refined_cap_verify.py`  
  SHA-256 `3360878C89DB842FD8695C74C211A3562DBFC84C3E1B4D3CA291DC36BCED39C5`.

I did not edit either target, the manuscript, or a shared no-drop
verifier.  After the mathematical audit, the parent agent applied only
the one-token proof-note correction confirmed in Section 1.  The
verifier checks before import that its Round 8D dependency has SHA-256

`8E025183DC6F2AFCE4E51F404F5AC7830185FCA1B22B2DF0184D1204E4D91BF6`.

That dependency in turn checks the Round 8C helper hash

`267900ED39C17C02D1BBDEB17B5F36AB616601DEE8127D98E50A9646BCEDCAB5`.

Both dependency files currently have exactly those hashes.

The audited mathematical conclusion is

\[
 f\geq2,\qquad p<n,\qquad \frac{927}{1000}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Round 8E proves the closed splice band
\(927/1000\leq\rho\leq93/100\), and the already audited Round 8D
theorem owns \(\rho\geq93/100\).  The shared endpoint is covered by
both results.  This is a ratio exclusion and compact reduction only; it
does not certify a residual fixed-ratio wall below \(927/1000\).

## 1. Resolved editorial finding

The initially audited proof note, at SHA-256
`AB721172AFA13C4C372C9F28357681200F70B22B400783089CB4CD1FF58D6684`,
had exactly one transcription defect.  In displayed equation (13),

```text
b(a)^2-left(\frac12-a\right)^2...
```

must read

```text
b(a)^2-\left(\frac12-a\right)^2...
```

The one-token replacement `-left` by `-\left` has now been applied.  The
corrected note has SHA-256
`38DE6AE72ACE3674096A9231A590ADCA1C2CE958BAFA777370AF65A3C2A9EB66`.
It is exactly one UTF-8 byte longer: 12,818 bytes rather than 12,817.
Replacing that single corrected occurrence back in memory reproduces
the original SHA-256 exactly, and the stale token now occurs zero times.
Therefore no other byte or claim changed.  The correction does not
change any formula, constant, inequality direction, or verifier output.

## 2. Ownership of \(p=0\) and the refined cap

If \(p=0\), then \(R_0=0\).  The completed one-interface theorem gives
\(D_A(q)\geq0\), while \(d_\rho>0\) and \(n\geq1\).  Hence

\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0.
\]

Consequently a nonpositive candidate must have \(p\geq1\).  Because
\(p<n\) and \(p,n\) are integral, \(n\geq2\), and therefore

\[
 q=r+n\geq\frac52.
\]

The terminal-cap proof treats the equality phase separately.  If
\(q=\mu\), the integral is zero.  If \(q<\mu<q+1\), strict convexity,
strict radius monotonicity, and \(0<\mu-q<1\) give

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_\mu(q)(\mu-q)<G_{q+1}(q).
\]

For \(H(q)=G_{q+1}(q)\), with
\(q/(q+1)=\cos\vartheta\), direct differentiation gives

\[
 H'(q)=\frac{\sin\vartheta-\vartheta}{\pi}<0.
\]

Thus \(q\geq5/2\) implies

\[
 2\int_q^\mu G_\mu<G_{7/2}(5/2)<\frac16.
\]

An independent 768-bit Arb evaluation gave the directed lower margin

\[
 \frac16-G_{7/2}(5/2)
 >0.0038491515051152111790.
\]

No equality phase or \(p=0\) face is filled by continuity.

## 3. Refined absent-level chord and common prefix

Write

\[
 L(a)=\left(\frac12-a\right)
 \left(2a+a^2+(1+a)\sqrt{a(2+a)}\right),
 \qquad 0\leq a\leq\frac14,
\]

and

\[
 b(a)=\frac{377}{1000}-a+\frac32a^2+a^3.
\]

Here

\[
 b'(a)=-1+3a+3a^2\leq b'(1/4)=-\frac1{16}<0,
 \qquad b(1/4)=\frac{1891}{8000}>0.
\]

I reconstructed the sign-safe squared gap independently.  Its exact
power coefficients in \(a\) are

\[
 b(a)^2-\left(\frac12-a\right)^2(1+a)^2a(2+a)
 =\frac{142129}{10^6}-\frac{627}{500}a
 +\frac{2881}{1000}a^2-\frac{123}{500}a^3-a^4.
\]

After \(a=y/4\), a separate exact degree-48 Bernstein conversion gives
49 positive coefficients.  The minimum occurs at index 44 and equals

\[
 \frac{7422203}{77832000000}>0.
\]

Because both \(b(a)\) and the radical term are nonnegative, the
squaring step is direction-safe and proves
\(L(a)<377/1000\), including both endpoints.

For \(\delta\geq1\), define

\[
 \beta=\frac{123}{1000}-c.
\]

On the present-level face, \(1/8>123/1000\) gives

\[
 cP>\beta\delta-\frac{cd}{2}.
\]

On the absent-level face, the refined chord gives

\[
 P>\beta M-\frac d2.
\]

Once \(\beta>0\), the wall-safe slope estimate
\(M\geq\delta/c\) has the correct direction and gives the same strict
prefix.  No multiplication or squaring step reverses an inequality.

## 4. Ratio endpoint and active width

At \(\rho=927/1000\), independent directed evaluation gives

\[
 (\arccos\rho)^2<\frac{37}{250},\qquad
 \frac{\arccos\rho}{\pi}<\frac{49}{400}
 <\frac{123}{1000}.
\]

The corresponding directed lower gaps at 768 bits are

\[
 0.0001882543400194846044\ldots,
 \qquad
 0.0001216480479108230065\ldots.
\]

Both transcendental left sides decrease with \(\rho\), so these bounds
cover the complete splice band.  In particular
\(\beta\geq1/2000>0\).

The active-width identity is

\[
 W>\lambda_\rho(W+\delta),\qquad
 \lambda_\rho=\frac{\pi G_1(\rho)}{1-\rho}
 >\frac{2\sqrt2}{3}\sqrt{1-\rho}.
\]

On the new band, \(1-\rho\geq7/100\).  Since all quantities being
squared are positive and

\[
 \frac89\frac7{100}-\left(\frac{249}{1000}\right)^2
 =\frac{1991}{9000000}>0,
\]

one has \(\lambda_\rho>249/1000\).  Finally
\(W+\delta=f-1/4\geq7/4\) yields the strict bound

\[
 W>\frac{1743}{4000}.
\]

## 5. Every \(\delta\geq1\) terminal stratum

The strict counts satisfy

\[
 B\geq B_0,\qquad Q\leq B_0+1.
\]

Hence the partition into \(B_0\geq1\), \(B_0=Q=0\), and
\(B_0=0,Q=1\) is exhaustive.  The strict convention assigns
\(W=3/4\) to \(B_0=0\), assigns \(A(q)=3/4\) to \(Q=0\), and assigns
\(\delta=1\) to this ledger.

For \(B_0\geq1\), the exact-angle reserve and the refined cap give

\[
 cD_A(q)>B_0\left(\frac12-c\right)-\frac{7c}{6}.
\]

Both the \(B_0\)- and \(\delta\)-coefficients are positive.  Minimizing
at \(B_0=\delta=1\), then at \(c=49/400\), gives

\[
 c\mathcal S>rac{623}{1000}-\frac{11}{3}c+c^2
 \geq\frac{90643}{480000}>0.
\]

For \(B_0=Q=0\), the lower expression is

\[
 F_0(c,W)=\left(\frac{123}{1000}-c\right)
 \left(\frac74-W\right)-\frac c2+c^2+W^2.
\]

On the whole face,

\[
 \partial_WF_0=2W-\left(\frac{123}{1000}-c\right)>0,
 \qquad
 \partial_cF_0=W-\frac94+2c<0.
\]

Using the unattained lower infimum \(W=1743/4000\) and
\(c=49/400\) is therefore conservative and gives

\[
 c\mathcal S>\frac{2308663}{16000000}>0.
\]

For \(B_0=0,Q=1\), strict ownership gives

\[
 \frac34-c<W\leq\frac34.
\]

The lower expression is concave in \(W\), so its infimum lies at an
endpoint.  Both endpoint polynomials decrease in \(c\), and at
\(c=49/400\) they give

\[
 \begin{aligned}
 W=\frac34:&\quad
 \frac{1371}{2000}-\frac52c+c^2
 =\frac{63081}{160000}>0,\\
 W=\frac34-c:&\quad
 \frac{1371}{2000}-\frac{2377}{1000}c-c^2
 =\frac{303449}{800000}>0.
 \end{aligned}
\]

The open lower endpoint is used only as an infimum.  Thus all strict
count walls and all three terminal strata are covered.

## 6. The \(0<\delta<1\) face

Strict bracketing gives

\[
 B_0=f-1,\qquad y=\delta+\frac14\in\left(\frac14,\frac54\right).
\]

The previously audited scale reduction takes the worst case to
\(f=2\), and the concavity reduction leaves

\[
 x=\frac yW\in\left[\frac17,\frac53\right].
\]

For \(t_0=3y/c\) and \(u_0=t_0/\mu\), the endpoint bounds give

\[
 u_0<\frac{740}{2781}<\frac{267}{1000}<1.
\]

The strict estimates
\(\Phi>\rho\theta^3/3\) and
\(1-\rho<\theta^2/2\) give
\(u_0/(1-\rho)>2x\), so retaining \(0\leq v\leq2x\) has the correct
direction.

For the subtracted arccos series,

\[
 z\leq\frac{73}{300},\qquad
 \frac{3/160}{1-73/300}=\frac{45}{1816},\qquad
 \frac{45}{1816}\frac27=\frac{45}{6356}.
\]

For the positive first copy, \(z\leq949/3000<1\).  Thus both series
uses remain inside their convergence domains, and the signs used for
truncation are correct.

The Taylor quotient for

\[
 C_\rho=\frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}
\]

is decreasing on \(0\leq\theta^2\leq37/250\); its derivative sign is
controlled by \(84+10t-t^2/2>0\).  Directed endpoint evaluation gives
\(C_\rho>173/125\).  My independent 768-bit lower margin was

\[
 C_\rho^{\rm lower}-\frac{173}{125}
 >0.0012485426522728956537.
\]

The frozen verifier encloses all 64 closed rational ratio panels.  For
both \(x=1/7\) and \(x=5/3\), it separately proves positivity of the
retained integral before replacing \(C_\rho\) by its rational lower
bound.  Across the four requested precision runs, its conservative
reported minima were

\[
 \mathcal I_\rho^{\mathrm E}(2x)>0.2040442323,
 \qquad
 \frac{173}{125}\mathcal I_\rho^{\mathrm E}(2x)-x
 >0.0085053826.
\]

As a separate coverage check, I reimplemented the formula and used 128
closed rational panels at 768 bits.  All 256 panel/endpoint tests passed,
with directed lower bounds

\[
 \mathcal I_\rho^{\mathrm E}(2x)>0.2040524292091421,
 \qquad
 \frac{173}{125}\mathcal I_\rho^{\mathrm E}(2x)-x
 >0.008733581721549382.
\]

Concavity fills the entire \(x\)-interval and proves \(T<3y/c\).
The endpoint-chord estimate and the cap then give

\[
 cP>-c-\frac3{16}-\frac{cd}{2},
 \qquad
 cD_A(q)>\frac12-\frac{7c}{6}.
\]

Their sum is

\[
 c\mathcal S>\frac5{16}-\frac83c+c^2.
\]

This polynomial decreases on the certified interval and equals
\(403/480000>0\) at \(c=49/400\).  The open small-\(\delta\) face and
the closed \(\delta=1\) ledger meet without a gap.

## 7. Residual cutoff and exact integer ranges

For \(0<\rho<927/1000\), monotonicity and directed endpoint evaluation
give

\[
 \frac1{169}<\eta_\rho<\frac19.
\]

The independent directed lower margin at the upper ratio endpoint was

\[
 G_1(927/1000)-\frac1{169}
 >0.0000238367060868269907.
\]

Also

\[
 a_\rho<\frac{658170}{8249},\qquad
 a_\rho+2\eta_\rho C_*
 <\frac{29724887}{371205}<81.
\]

Writing \(X=a_\rho+2\eta_\rho C_*\), the comparison of the square root
is sign-safe because \(X>0\) and

\[
 X^2-\left(a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2\right)
 =\eta_\rho^2(4C_*^2-1)>0.
\]

Therefore

\[
 K_0(\rho)<81\cdot169^2=2\,313\,441.
\]

For a nonpositive candidate, \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\).  Strict inequalities followed by half-integrality or
integrality give exactly

\[
 \frac1{4\,626\,882}<\rho<\frac{927}{1000},
 \qquad \frac{21}{4}<K<2\,313\,441,
\]

\[
 1\leq2r\leq4\,626\,881,qquad
 2\leq n\leq2\,313\,440,qquad
 1\leq p\leq n-1,
\]

\[
 2\leq f\leq771\,147,qquad
 0\leq Q\leq f-1,qquad Q\leq B\leq771\,147.
\]

The bounds \(K-\mu>7\pi/4\), \(K>21/4\), and the final \(f,B\)
ranges use strict decrease from \(A(0)\) and \(\pi>3\); no real
endpoint is rounded in the wrong direction.

## 8. Verifier replay and verdict

I replayed the exact frozen verifier with python-flint 0.8.0 at 384,
512, 768, and 1024 bits.  All four runs returned exit code zero.  Each
run reported the expected Round 8D dependency hash, 128 successful
full-panel endpoint evaluations, the exact five terminal ledgers, the
cutoff \(2\,313\,441\), and the conservative integer ranges.

I found no phase-ownership gap, missing strict-count wall, reversed
inequality, unsafe squaring step, uncovered panel, series-domain error,
or cutoff-rounding error.  The verifier and the intended mathematics of
the proof note therefore **PASS**.  The focused byte-for-byte follow-up
in Section 1 confirms that the sole editorial defect was corrected and
that the corrected target is now a clean final artifact.
