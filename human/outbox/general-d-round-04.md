# General dimension, Round 4d: terminal reserve and global chamber reduction

Date: 18 July 2026

Primary strategy: `human/inbox/general-d_1.md`

Status: substantial rigorous progress, but not a completed proof of the
positive shifted-tail theorem.  The exact dimension lift and all earlier
tail regions remain proved.  This round makes the terminal convex reserve
quantitative, proves exact no-drop identities, reduces the no-drop branch
globally to explicit finite discrete data, and quantitatively excludes its
only possible escaping thin rays.  The first-drop branch and the explicit
finite wall certificates are still incomplete.

## 1. Separate manuscript and promoted PDF

The general-dimensional paper remains separate from the original
three-dimensional paper:

- `manuscript/spherical-shell-polya-general-d.tex`;
- `output/pdf/spherical-shell-polya-general-d.pdf`.

The promoted Round 4d PDF has 30 pages.  It contains the scale-free shelf
curvature lemma, the fractional-top exact-angle terminal reserve, the
zero-level triangle, the exact no-drop identities, the high-floor automatic
sector and critical-ray theorem, the global no-drop exhaustion, and the
quantitative transfer giving the cutoff below.  Text extraction found no
unresolved references, undefined markers, or replacement characters; pages
20--30 were rendered and visually checked.  Its SHA-256 is
`FEFBB3F78663D8700DC7E5EF2E0B92D9D5B588578EA25CC28D8C952702C42B2F`.

The original file `manuscript/spherical-shell-polya-proof.tex` was not used
as the target of any general-dimensional edit in this round.

## 2. Quantitative first-shelf and terminal lemmas

The first-shelf reduction leaves the scalar

\[
 \mathscr S
 =D_A(q)+R_p+\frac{d_\rho}{2}(n-p).
\]

The Round 4 high-floor note proves, with
\(\Delta=A(r)-A(r+p)\),

\[
 \mathcal C_p\ge
 \frac{p^2}{3(2r+p)}\Delta,
 \qquad
 A(0)-A(r)\le\frac{r\Delta}{2p}.
\]

For a decreasing convex terminal profile \(g\), it proves

\[
 D_g\ge\sum_{k=1}^{B}
 \left(\frac1{2c_k}-1\right),
\]

where \(c_k\) is the exact slope at action level \(k-1/4\).  Applied to
the translated ball tail, this gives

\[
 D_A(q)\ge
 \max\left\{0,
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\int_q^\mu G_\mu(z)\,dz\right\}.
\]

The separate zero-level note strengthens this by retaining the unused
fractional top interval:

\[
 D_g\ge\sum_{k=1}^{B}
 \left(\frac1{2c_k}-1\right)
 +\frac{(g(0)-B)_+^2}{-g'(0)}.
\]

When \(B=0\), the shell terminal count vanishes and the exact bottom
triangle gives

\[
 D_A(q)\ge
 \frac{G_K(\mu)^2}{\arccos(\rho)/\pi}.
\]

Detailed proofs are in:

- `human/outbox/general-d-round-04-high-floor.md`;
- `human/outbox/general-d-round-04-zero-level-terminal.md`.

## 3. Exact no-drop branch

When the first ordinary floor does not drop before the interface,
\(p=n\) and \(F_0=\cdots=F_n=f\), the exact identities are

\[
 D_A(r)=D_A(q)+R_n+\chi_q,
\]

\[
 R_n=-\frac n2+2n\varepsilon_q
 +2\int_0^n u\,\sigma(r+u)\,du.
\]

They separate the endpoint wall exactly and show which quantitative
terminal payment is required.  The root-free exact-angle consequence gives
an explicit automatic cutoff

\[
 K\ge K_{\rm nd}(n,Q)
 =\left(\frac{Q+n/2+4\sqrt2/15}{C_0S_Q}\right)^3,
 \qquad C_0^3=\frac\pi{12}.
\]

For each fixed \((n,f,Q)\), the residual set is a compact strip with only
finitely many one-sided action walls.  See:

- `human/outbox/general-d-round-04-no-drop.md`;
- `human/outbox/general-d-round-04-no-drop-terminal.md`.

## 4. Global exhaustion of no-drop discrete data

The new exhaustion theorem proves the following necessary boxes for every
still-unresolved no-drop tail:

\[
 r\le K/2
 \quad\Longrightarrow\quad
 2\le f\le49,\qquad1\le n\le48,
\]

and

\[
 r>K/2,\ f\ge4
 \quad\Longrightarrow\quad
 4\le f\le8,\qquad1\le n\le39.
\]

The only rows that can escape the elementary bounds are \(f=2,3\).
Every escaping sequence is forced into

\[
 K-\mu\asymp n,qquad K\asymp n^3,qquad
 r/K\to1,qquad\mu/K\to1.
\]

The note supplies explicit two-sided cone constants and compact scaled
parameter ranges.  The Arb replay certifies 138,184 central endpoint
comparisons and 980 outer comparisons:

- `human/outbox/general-d-round-04-no-drop-exhaustion.md`;
- `scripts/general_d_no_drop_exhaustion_verify.py`.

The verifier reports

```text
PASS: global high-floor no-drop exhaustion certified with Arb
central box: 2 <= f <= 49, 1 <= n <= 48
outer finite box: 4 <= f <= 8, 1 <= n <= 39
only noncompact limiting floors: f=2,3
```

Independent audits found no mathematical correction in the high-floor,
fractional-top, or no-drop exhaustion results.  The Arb exhaustion replay
was repeated at 256, 512, 768, and 1024 bits with identical output.  The
audit records are:

- `human/outbox/general-d-round-04c-independent-audit.md`;
- `human/outbox/general-d-round-04-no-drop-exhaustion-independent-audit.md`.

## 5. Critical thin ray

For

\[
 \rho=1-\varepsilon,qquad
 K\sim\kappa\varepsilon^{-3/2},qquad
 X=(\mu-z)\sqrt\varepsilon,
\]

the shell action has the turning limit

\[
 H_\kappa(X)=\frac{2\sqrt2}{3\pi\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right).
\]

Writing \(w=H_\kappa(0)\), a negative leading shelf/head prefix is
strictly smaller than \(\pi/(2\sqrt2)\), while the first exact-angle
terminal level is strictly larger than the same constant.  For the only
escaping no-drop rows \(f=2,3\), the comparison has the uniform gap

\[
 \liminf_{\varepsilon\downarrow0}
 \sqrt\varepsilon\,\mathscr S
 \ge
 \frac\pi{2\sqrt2}
 \left[\left(\frac73\right)^{1/3}-1\right]
 >\frac13.
\]

The finite-thickness transfer is now quantified.  With

\[
 s=\sqrt{1-\rho},\qquad \kappa=s(K-\mu),\qquad N=sn,
\]

the endpoint floors force

\[
 \frac{21}{8}\le\kappa<18,\qquad N<53,
\]

and the exact shell profile satisfies the uniform bound

\[
 \left|\mathcal H_{s,\kappa}(X)-H_\kappa(X)\right|
 \le5500s^2\qquad(0\le X\le54).
\]

Combining this signed head transfer with the first exact terminal angle
gives, on both low-floor rows,

\[
 n\ge72\,000
 \quad\Longrightarrow\quad
 s\bigl(D_A(q)+R_n\bigr)>\frac15.
\]

Thus every residual no-drop candidate has \(n<72\,000\).  This is an
explicit finite reduction; it is not a certification of those remaining
finite wall chambers.

The same note also proves two finite automatic sectors:

- an explicit high-floor cutoff on \(\rho\le99/100\);
- for \(f\ge3\), positivity when
  \(\varepsilon(K-\mu)^4\le f^3/144\).

See:

- `human/outbox/general-d-round-04-high-floor-cutoff.md`;
- `human/outbox/general-d-round-04-critical-ray-transfer.md`;
- `human/outbox/general-d-round-04-critical-ray-transfer-independent-audit.md`.

## 6. First-floor branch

For \(F_0=1\) and \(p<n\), the exact wall reduction to
\(A(r+p)=3/4\) remains valid.  Ten previously isolated chambers are
rigorously genuine failures of the weakened envelope and rigorously
positive for the stronger true-interface certificate.

Further analytic reductions proved this round place any weakened failure
inside explicit cones.  In particular, on the \(s=0,1\) rays with
\(r\ge3/2\), \(x=r+p\ge100\), one has

\[
 1.11546\le x^{-1/3}(K-\mu)\le3.55899,
 \qquad0<x^{-1/3}p<54.828.
\]

The zero-level terminal triangle gives a positive critical-ray limiting
scalar in diagnostics, but a rigorous finite-thickness transfer and an
Arb exhaustion of the compactified ray box are still missing.  The
current proved wall reductions are recorded in
`human/outbox/general-d-round-04-chamber-exclusion.md`.

## 7. Exact remaining obligations

The all-dimensional theorem is not yet proved.  The remaining tasks are:

1. certify the finitely many residual no-drop wall chambers, including
   \(f=2,3\) with \(n<72\,000\);
2. complete the \(F_0=1\), \(p<n\) first-floor exhaustion, including the
   compactified product/transition rays;
3. prove a global cutoff or equivalent finite exhaustion for the remaining
   high-floor first-drop branch;
4. only then replace the shifted-tail conjecture by a theorem and invoke
   the already complete branching-defect identity.

No claim in this report treats these obligations as closed.
