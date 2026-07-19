# Independent audit of General-dimensional Round 32

Date: 19 July 2026

Decision: **PASS for the stated retained-shelf closure; no promotion of
full high-floor CST, pointwise assembly, or the all-dimensional theorem.**

Audited artifacts:

- human/outbox/general-d-round-32-shelf-bootstrap-truncation-and-compact-retained-shelf-closure.md
- computations/general_d_round32_shelf_bootstrap_replay.wl
- computations/general_d_round32_truncated_Lq_certificate.py

## 1. Claim and scope audit

The audited claim has three parts:

1. every necessary included lower-shelf point with real \(q\ge35\) obeys
   the strict intrinsic bound
   \[
    m>\frac65\left(\frac\pi\psi-3\right);
   \]
2. one directed-Arb computation proves \(L_q>0\) on the exact integer and
   half-integer grids below \(q=1000\), after applying that shelf
   truncation for \(q\ge35\); and
3. the Round 31 real exclusion for \(q\ge1000\) completes the Round 30
   included retained-\(E\) lower shelf on both inherited grids.

The note does not claim that every high-floor endpoint family was reduced to
this shelf. It explicitly leaves the lower-\(Q\) hard arc, the remaining
\(\alpha\)-faces, other inverse bands, hard-sector seams, and simultaneous
inverse/outer-\(B\) endpoints open. It therefore does not claim full CST or
the all-dimensional theorem. This claim boundary is correct and is
maintained by both verification artifacts.

The closure also does not license retaining an older overlapping
first-floor finite certificate in the final proof architecture. The source
correctly requires that legacy certificate to be replaced by, or
consolidated with, the single Round 32 certificate before final assembly.

## 2. Uniform angle bounds

Write \(\theta=\theta_3\) and

\[
 \tan\theta-\theta=\frac{3\pi}{4(q+3)},\qquad
 \cos\psi=\frac{q\cos\theta}{q+3}.
\]

The audit independently checked the Taylor comparison at
\(x_0=219/400\). Positivity of all omitted tangent coefficients gives

\[
 \theta<\frac{219}{400}<\frac{11}{20}.
\]

The exact rational residual is

\[
 \frac{4764574458554919}{155648000000000000000}>0.
\]

Since \(q/(q+3)\ge35/38\), the lower sixth-order cosine bound at
\(219/400\) and the upper fourth-order bound at \(2/3\) give

\[
 \cos\psi>\cos\frac23,\qquad \psi<\frac23,
\]

with exact residual

\[
 \frac{249713778018875291}{605159424000000000000}>0.
\]

For the cubic estimate, put \(c=49/40\). The exact identity

\[
 \cos\psi=\cos\theta-\frac4\pi
 (\sin\theta-\theta\cos\theta)
\]

was reconstructed from the inverse-angle equation. The two strict bounds

\[
 \sin\theta-\theta\cos\theta<\frac{\theta^3}{3},
\]

and

\[
 \cos\theta-\cos(c\theta)
 =\int_\theta^{c\theta}\sin u\,du
 >\frac{c^2-1}{2}\theta^2
  -\frac{c^4-1}{24}\theta^4
\]

are correctly oriented. The latter follows directly from
\(\sin u>u-u^3/6\), so it does not require a numerical series premise.
The rational comparison

\[
 \frac{c^2-1}{2}
 -\frac{c^4-1}{24}\left(\frac{11}{20}\right)^2
 -\frac{424}{999}\frac{11}{20}
 =\frac{9003993307}{8183808000000}>0
\]

and \(\pi>333/106\) imply \(\psi<c\theta\). Finally,
\(\tan\theta-\theta>\theta^3/3\) and \(\pi<22/7\) give

\[
 q\psi^3<c^3\frac{99}{14}
 =13-\frac{107}{128000}<13.
\]

Every inequality in this angle chain is strict at \(q=35\), so the lower
endpoint is included without an equality exception.

## 3. Shelf-bootstrap audit

For

\[
 h(z)=\arccos\frac z{K_3}-\arccos\frac zq,
\]

direct differentiation gives

\[
 h'(z)=\frac1{\sqrt{q^2-z^2}}
       -\frac1{\sqrt{K_3^2-z^2}}>0,
\]

\[
 h''(z)=z\{(q^2-z^2)^{-3/2}
             -(K_3^2-z^2)^{-3/2}\}>0.
\]

Thus \(h\) is strictly increasing and convex. The first coarse phase
bound and the non-strict shelf condition imply

\[
 m>y:=\frac\pi\psi-3.
\]

The audit then reconstructed the load-bearing estimate

\[
 h(q-y)<\frac{2\psi}{3}.
\]

With

\[
 \alpha=\arccos(1-y/q),\qquad
 \beta=\arccos((q-y)/K_3),
\]

the nontrivial case reduces exactly to

\[
 \tan\alpha>
 \frac{\cos(2\psi/3)-\cos\psi}{\sin(2\psi/3)}.
\]

Product-to-sum and strict decrease of \(\sin u/u\) give an upper
bound \(5\psi/12\) for the right side. On the other hand,

\[
 \tan^2\alpha
 =\frac{y(2q-y)}{(q-y)^2}>\frac{2y}{q}.
\]

The cubic angle bound supplies the missing strict comparison:

\[
 q\psi^3<13
 <\frac{288}{25}\left(\frac{333}{106}-2\right)
 <\frac{288}{25}(\pi-3\psi).
\]

The middle margin is exactly \(199/1325\). Since
\(y\psi=\pi-3\psi\), this is equivalent to

\[
 \frac{2y}{q}>\left(\frac{5\psi}{12}\right)^2.
\]

No circular use of the improved shelf bound occurs: the preliminary
\(m>y\) is established before \(h(q-y)\) is used.

Now \(x=q-m<q-y\), so \(h(x)<2\psi/3\). The outer action integral is
strictly below \(3\psi\), while the convex trapezoid bound gives

\[
 \int_x^q h(z)\,dz
 \le\frac m2\{h(x)+h(q)\}<\frac{5m\psi}{6}.
\]

Consequently

\[
 G_{K_3}(q-m)-G_q(q-m)
 <\frac34+\frac\psi\pi\left(3+\frac{5m}{6}\right).
\]

Combining this strict upper bound with shelf feasibility allowed at equality
proves

\[
 \boxed{m>\frac65\left(\frac\pi\psi-3\right)}.
\]

The factor \(6/5\), all strict signs, and the use of \(0<y<m<q\) pass.

## 4. Truncated-triangle reduction

Because \(m\) is integral, the strict analytic inequality gives exactly

\[
 m\ge m_\sharp(q)
 =\left\lfloor\frac65\left(\frac\pi\psi-3\right)\right\rfloor+1
\]

for \(q\ge35\). The formula is not used below \(q=35\); there the full
boundary \(m\ge1\) is retained.

The Round 31 Hessian identity remains valid on every truncated triangle.
An interior critical point is a saddle, so the minimum lies on

\[
 p=1,\qquad r=r_0,\qquad m=m_0(q).
\]

The \(p=1\) edge is analytic: here \(x\ge1+r_0\), every curvature
factor is positive, and \(d,m>0\). Hence

\[
 L_q(1,x)>\frac7{10}-\frac12=\frac15.
\]

The other two edge restrictions are strictly convex by the audited Round 31
calculation. Therefore locating their endpoint or unique stationary
minimum is sufficient; the numerical artifact is not sampling integer
\(p\)-values.

## 5. Directed-Arb certificate audit

The Python artifact was inspected line by line and replayed afresh. Its
coverage is exact:

- \(2q=6,7,\ldots,1999\), hence 1994 grid values;
- even \(2q\) uses \(r_0=1\), and odd \(2q\) uses \(r_0=3/2\);
- \(q<35\) uses \(m_0=1\), while \(q\ge35\) uses the certified floor
  defining \(m_\sharp\);
- \(q=999.5\) is included, and \(q=1000\) is assigned to Round 31.

At 192-bit Arb precision, each inverse angle is bracketed by 100 bisections
with exact dyadic endpoints. The residual signs at both ends are
rechecked. The unique_fmpz call can succeed only when the floor of the
Arb enclosure is unique, so every \(m_\sharp\) transition is certified.

On each nontrivial edge, the code first proves an endpoint minimum or
brackets the unique derivative zero using 70 exact dyadic bisections. It
then evaluates \(L_q\) on the entire root ball. Requiring that whole Arb
value be greater than \(1/100\) is a valid directed lower-bound check.
Fixed loop limits and the final count assertion prove finite termination
and coverage. The bookkeeping used only to print the smallest record is
not a proof premise; every individual edge is checked before recording.

Fresh output:

    pythonFlintVersion=0.8.0
    arbPrecisionBits=192
    thetaBisections=100
    edgeBisections=70
    q2Range=6..1999
    qCount=1994
    certifiedEdgeCount=3988
    pEqualsOneAnalyticLowerBound=1/5
    certifiedNontrivialEdgeMargin=1/100
    rEdgeMinimumLower=[0.0136436913630499228424187731718 +/- 2.97e-32]
    mEdgeMinimumLower=[0.0133457016833499669676497170461 +/- 2.51e-32]
    globalMinimumLower=[0.0133457016833499669676497170461 +/- 2.51e-32]
    round32TruncatedLqCertificateOK=True

The reported \(r\)-edge record occurs at \(q=7\), \(m_0=1\); the
\(m\)-edge and global record occurs at \(q=999.5\), \(m_\sharp=15\).
Both directed enclosures are strictly above the rational proof margin
\(1/100\).

## 6. Symbolic replay and controls

The Mathematica artifact was replayed with the installed Mathematica 15.0
runtime. It returned

    round32Margins={
      4764574458554919/155648000000000000000,
      249713778018875291/605159424000000000000,
      9003993307/8183808000000,
      107/128000,
      199/1325
    }
    round32DerivativeResiduals={0,0,0,0}
    round32ShelfBootstrapReplayOK=True

The Python artifact compiles successfully. Fresh source checks found zero
tabs and zero nonprinting control bytes in all three artifacts.
The command git diff --check also passed.

Artifact SHA-256 hashes:

- Round 32 source:
  214bbe12af00821dd39c2598e223bc8f3c1a8fbdb19f61febed8982927380ff5
- Mathematica replay:
  ffe12b99198f9634c64d8978b5589112c5a66a4b3e9bc5be04d0e78aba915169
- directed-Arb certificate:
  85c38adafe7248c6bba2f8e4ca14d88118719c5cf26905071ff33be5b5a0e280

## 7. Equality and wall audit

PASS:

- shelf feasibility may hold with equality; the phase upper bounds remain
  strict, so the integer truncation is still valid;
- the \(q=35\) endpoint belongs to both the analytic bootstrap and the
  finite certificate;
- \(q=999.5\) and \(q=1000\) meet without a gap or overlap problem;
- the literal parity radii \(r_0=1\) and \(r_0=3/2\) are used, with no
  extension to \(r=0\) or \(r=1/2\);
- \(p=dm\) and
  \(E_{\min}=1/2-dm/(2p)\) retain their earlier automatic owner;
- ordinary-floor, interface, turning, inverse, and outer-\(B\) equality
  conventions are unchanged; and
- the certificate proves the continuous edge minima, so integer \(p\)
  points are included a fortiori.

No shell-ratio threshold, owner partition, or new seam is introduced.

## 8. Loss and counterexample regression

The loss directions are correct. The coarse phase estimate is used only
to get \(m>y\); rational angle bounds are used only for the shape estimate;
the convex trapezoid discards a positive strict-convexity reserve; and the
finite lower scalar discards both \(T(q)-7/10\) and
\(E_{\min}-\mathcal K_{4,\min}\). The weaker \(L_q\) is used only on the
finite range; Round 31 retains the exact \(E_{\min}\) for \(q\ge1000\).

The two printed scope regressions were independently re-evaluated with Arb:

    L_(79/2)(4,77/2) = [-0.00193497394458958651219863840 +/- 2.48e-30]
    L_40(4,39)        = [-0.00664273152794738881349065628 +/- 5.28e-30]

Thus the untruncated \(m=1\) edge is genuinely false near \(q=40\).
Both points are outside the proved necessary shelf domain, where the new
bootstrap forces \(m\ge3\). The truncation is therefore load-bearing and
is not merely an optimization of the certificate.

## 9. Final decision

**PASS** for:

- the real \(q\ge35\) shelf bootstrap;
- the exact integer conversion \(m\ge m_\sharp(q)\);
- the three-edge reduction of the truncated lower scalar;
- the single directed-Arb certificate on all 1994 finite grid values;
- the seam with the Round 31 real \(q\ge1000\) exclusion; and
- closure of the Round 30 included retained-\(E\) lower shelf on both
  inherited grids.

**Not proved by Round 32**:

- endpoint families outside the Round 30 included retained shelf;
- the full correlated shelf--terminal theorem;
- the weighted aggregate fallback;
- pointwise assembly; or
- the all-dimensional Pólya theorem.

The proper next step is the one correlated analytic endpoint theorem, or
the weighted aggregate if that theorem resists. A second overlapping
certificate or a shell-ratio owner ladder is not justified by this result.
