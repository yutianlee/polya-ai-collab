# Independent audit: global no-drop exhaustion

Date: 18 July 2026

Files audited:

- `general-d-round-04-no-drop-exhaustion.md`
- `scripts/general_d_no_drop_exhaustion_verify.py`

Verdict: **PASS, with two minor presentation corrections and no
mathematical correction.**  The central and outer reductions, their
monotone endpoint exhaustions, both endpoint values of \(Q\), the exact
cone constants, and the sequential use of the critical-ray gap are valid.
The Arb replay passed unchanged at 256, 512, 768, and 1024 bits.

## 1. Residual and geometric reductions

The no-drop identity

\[
 R_n=-\frac n2+2n\varepsilon
     +2\int_0^n u\sigma(r+u)\,du
\]

shows that an unresolved branch has \(R_n<0\), and hence \(n\ge1\),
\(\varepsilon<1/4\).  The scale-free shelf estimate gives

\[
 2\varepsilon+\Delta<\frac12,
\]

which is exactly \(\varepsilon_0+\varepsilon<1/2\).  Thus all five
consequences in (1) have the stated strict directions.

For (3), monotonicity of the radius integrand gives

\[
 \sqrt{1-q^2/a^2}\le \sqrt{1-q^2/K^2}
 <\sqrt{\frac{2(\delta+1)}K},
\]

because \(K-q=\delta+\alpha<\delta+1\).  This proves the displayed
upper bound for \(A(q)\) and therefore \(K\le U_f(\delta)\).

For (4),

\[
 \sigma(z)=\frac1\pi\int_\mu^K
 \frac{z}{a\sqrt{a^2-z^2}}\,da
 \ge \frac{\delta z}{\pi K^2}.
\]

Integrating from \(r\) to \(q=r+n\), then using
\(\Delta<1/2\), \(\delta>\pi b\), and \(r\ge1/2\), gives both
inequalities in (4).  Finally, the audited convex-slope estimate

\[
 A(0)-A(r)\le \frac{r\Delta}{2n}<\frac r{4n}
\]

gives (5).  No independence assumption between \(K,\delta,r,n\) is
introduced in these steps.

## 2. Central branch

If \(r\le K/2\), then

\[
 r\le K-r=\delta+\alpha+n<\delta+n+1.
\]

Substitution in (5) gives (7); its denominator is positive because
\(n\ge1\) and \(\pi<4\).  For fixed \(f\), \(D_{n,f}\) strictly
decreases with \(n\), while \(U_f\) strictly increases with its argument.
Thus the right side of (8) decreases and its left side increases.  A
single failed geometry check therefore excludes every larger \(n\).

The integral bound (9) is correct: it is the lower left-endpoint sum for
the decreasing function \(x^{-1/3}\) over
\([3/4,Q+3/4]\).  After division by \(Q^{2/3}\), its integral expression
increases with \(Q\), so the \(Q=7\) base check suffices.  The normalized
automatic-cutoff left side increases with \(f\), since both
\(1-1/(4f)\) and \(1-1/f\) increase; its right side
\(13/12+c_*/f\) decreases.  The \(f=16\) check therefore proves
\(n>f/6\) in every residual branch with \(f\ge16\).

The estimates \(D_{n,f}<5f\), \(U_f(D_{n,f})<30f\), and
\(n<31\sqrt f\) give \(f<34596\) with the stated constants.  For fixed
\((f,Q)\),

\[
 K_{\rm nd}(n,Q)-\bigl(\pi b+n+\tfrac12\bigr)
\]

is a positive multiple of \((Q+c_*+n/2)^3\) minus a linear function,
and is therefore convex in \(n\).  Being nonpositive at \(n=1\) and
\(n=f-2\) makes it nonpositive on the whole interval.  This validates
the two-endpoint reduction in the script.  Together with the monotone
geometry obstruction at \(n=f-1\), it covers every \(n\ge1\).

## 3. Outer branch

From \(R_n<0\) and monotonicity of \(\sigma\),

\[
 n^2\sigma(r)<\frac n2,
 \qquad \sigma(r)<\frac1{2n}.
\]

For \(r>K/2\), the exact slope integral and
\(K-r=\delta+\alpha+n<\delta+n+1\) give

\[
 \sigma(r)>
 \frac{\delta}{2\pi\sqrt{2K(\delta+n+1)}}.
\]

This proves (14).  Combining it with (3) yields
\(b^2<4d(d+1)\), and solving the quadratic gives precisely

\[
 d>c_f=\frac{\sqrt{1+b^2}-1}{2}.
\]

The lower function \(\delta^2/(\delta+n+1)\) is strictly increasing for
\(\delta>0\), so evaluating it at
\(\max\{\pi b,c_fn-1\}\) proves (16).

For \(f\ge16\), the elementary estimates
\(c_f\ge f/3\), \(c_f<f/2\), \(\pi^2<10\), and
\(c_fn-1\ge c_fn/2\) give

\[
 K>\frac{c_f^2}{8\pi^2(c_f+1)}n^3
   >\frac{fn^3}{405}.
\]

Also, (9), \(f<6n\), \(Q\le f\), and \(c_*<1/2\) give

\[
 K_{\rm nd}(n,Q)<703\frac{n^3}{(f-1)^2}.
\]

Thus \(f(f-1)^2<284715\), whose largest integral solution is \(f=66\).

Once \(c_fn-1\) is active, division of (16) by \(n^3\) gives (18).
Its left side increases with \(n\), and its right side decreases.  The
active condition persists.  Consequently, after an Arb comparison
excludes a fixed \(Q\), every larger \(n\) is excluded for that \(Q\).
The script waits until this has happened separately for \(Q=f-1\) and
\(Q=f\), so its stopping rule is rigorous.

The limiting comparisons are also correctly chosen.  Since \(\gamma_f\)
increases and \(\beta_J\) decreases,

\[
 \gamma_2<\beta_2,\qquad
 \gamma_3<\beta_3,\qquad
 \gamma_4>\beta_3
\]

leave both possible \(Q\)-values unexcluded only for \(f=2,3\), and
exclude every \(Q\in\{f-1,f\}\) when \(f\ge4\).

## 4. Endpoint walls

The weak cutoff is wall-safe in all cases.

- If \(\varepsilon>0\), then \(Q=f\) and \(B\ge f\).
- If \(\varepsilon=0\) and \(q<\mu\), then \(Q=f-1\) but
  \(B\ge f\); replacing \(S_B\) by \(S_Q=S_{f-1}\) only weakens the
  terminal payment.
- If \(\varepsilon=0\) and \(q=\mu\), then \(B=Q=f-1\), so the weak
  cutoff is exact at the pure-ball corner.

The finite scans explicitly test both \(Q=f-1\) and \(Q=f\); no endpoint
wall is inferred by continuity from the other branch.

## 5. Escaping rays and critical-ray exclusion

For fixed \(f\in\{2,3\}\), (2), (14), (15), and the reverse action
estimate

\[
 A(q)\ge\frac\delta{2\pi}\sqrt{\frac\delta{2K}}
\]

give \(\delta\asymp n\), \(K\asymp n^3\), and hence
\(r/K,\mu/K\to1\).  The exact constants in (25a) follow as stated:

\[
 \mathcal K_f=
 \left(\frac{f+1/2+c_*}{C_0S_{f-1}}\right)^3,
 \qquad
 \mathcal D_f=(8\pi^2f^2\mathcal K_f)^{1/3}.
\]

The lower \(K\)-constant follows by inserting
\(\delta\ge c_fn/2\) and
\(\delta+n+1<(\mathcal D_f+2)n\) into (14).

With \(\eta=\delta/K\), the exact identities

\[
 \frac{\kappa}{N}=\frac\delta n,
 \qquad
 \frac{\kappa}{N^3}=\frac K{n^3}
\]

give (27).  The residual condition
\(A(r)+A(q)<2f\) gives (28) after taking the turning limit.  The ranges
in (26) are exactly \(w/c_0\) for \(f-1/4\le w\le f\).

There is no circular use of Corollary 3.2.  Sections 3--5 of the
exhaustion note first force every escaping sequence into
\(f=2,3\), \(K\asymp n^3\), \(\delta\asymp n\).  The compact cone then
provides a convergent scaled subsequence, to which the conditional
critical-ray gap applies:

\[
 \liminf\sqrt\eta\,\mathscr S\ge\gamma_0>\frac13.
\]

This contradicts \(\mathscr S<0\) along an unresolved sequence.  A
uniform finite-\(\eta\) remainder is not needed for this qualitative
sequential contradiction; it would be needed only to output a numerical
cutoff for the two rows.  Thus the claimed nonconstructive finiteness in
\(n\) is valid.

## 6. Arb replay and minor corrections

The unmodified verifier passed at 256, 512, 768, and 1024 bits, always
reporting

- 138,184 central endpoint comparisons;
- 649 retained central necessary pairs;
- 980 outer comparisons;
- 60 retained outer necessary pairs.

The closest audited large-range central endpoint margin was still
positive by more than \(1.409\), and the closest outer monotone-stop
margin was positive by more than \(1.383\).  The limiting comparisons
also have comfortable margins; in particular
\(\beta_3-\gamma_3>0.00188\) and
\(\gamma_4-\beta_3>0.01725\).

Two presentation corrections are advisable:

1. After introducing the residual branch, state explicitly that
   \(n\ge1\).  This already follows from \(R_0=0\), but it makes the
   denominators in (4)--(8) visibly legitimate.
2. The table following (25a) is labelled “for orientation only,” and the
   exact boxed bounds are correct.  Nevertheless, several displayed
   lower decimal bounds were rounded upward.  If the decimals are to be
   read as one-sided bounds, replace the \(f=3\) lower value
   \(0.481544\) by \(0.481543\), and replace the two lower \(K/n^3\)
   values by \(1.09483\times10^{-4}\) and
   \(3.91375\times10^{-4}\), respectively.  This has no effect on any
   proof or computation.

As optional certificate hardening, the script could assert the expected
counts 649 and 60 in addition to printing them.  Its present exhaustive
loops and box assertions are already sufficient for the stated theorem.
