# SHELL-weighted-lattice-fractional: numerical diagnostic

This is a floating-point and symbolic diagnostic, not a certificate.

## Quantities compared

Let

\[
\nu_\ell=\ell+\tfrac12,\qquad w_\ell=2\ell+1=2\nu_\ell,
\qquad M=\max\{0,\lceil K-\tfrac12\rceil\},
\]

and sum over `ell = 0,...,M-1`, which is exactly the strict angular cutoff
`nu_ell < K`. Write `mu=rho*K` and extend `G_mu(z)` by zero
for `z>mu`.  The diagnostic compares

\[
W=\frac{2}{9\pi}(1-\rho^3)K^3,
\]

\[
S_B=\sum_\ell w_\ell\bigl(G_K(\nu_\ell)-G_\mu(\nu_\ell)\bigr),
\]

\[
S_{GF}=\sum_\ell w_\ell\bigl(G_K(\nu_\ell)-F_\mu(\nu_\ell)\bigr),
\]

and the strict-integer envelope

\[
U_{GF}=\sum_\ell w_\ell
\left(\left\lceil G_K(\nu_\ell)-F_\mu(\nu_\ell)\right\rceil-1\right).
\]

The floating phase is evaluated from

\[
\gamma_\ell=\frac1\pi\int_{\rho K}^K
\frac{dx}{x^2\bigl(j_\ell(x)^2+y_\ell(x)^2\bigr)},
\]

and the floating strict count uses

\[
q_\ell=\#\{n\ge1:n<\gamma_\ell\}
=\lceil\gamma_\ell\rceil-1.
\]

Numerical endpoint detection is tolerance-based.  Selected phase integrals were
cross-checked against independently unwrapped `scipy.special.hankel1` phases.

## Exact quarter-slack accumulation

Putting `+1/4` into every active angular channel costs exactly

\[
Q=\frac14\sum_{\ell=0}^{M-1}(2\ell+1)=\frac{M^2}{4}.
\]

Hence

\[
\frac{Q}{W}
=\frac{9\pi M^2}{8(1-\rho^3)K^3}.
\]

For a thin shell with fixed optical width `a=(1-rho)K`, so that
`rho=1-a/K`,

\[
\frac{Q}{W}\longrightarrow \frac{3\pi}{8a}.
\]

Thus the blanket quarter slack alone asymptotically exceeds the entire Weyl
term when `a < 3*pi/8`, approximately `1.1781`.

There is also the exact integral identity

\[
\int_0^\lambda 2zG_\lambda(z)\,dz=\frac{2\lambda^3}{9\pi}.
\]

Therefore `S_B` is the half-integer midpoint lattice analogue of the shell
Weyl integral.  It is not itself the strict radial count.

## Representative results

`S_gamma` denotes the weighted floating phase sum.  Positive differences mean
that the corresponding fractional sum lies above the Weyl term.

| rho | K | `(1-rho)K` | W | Q/W | `S_B-W` | `S_gamma-W` | `S_GF-W` | `U_GF` | floating N |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.20 | 20 | 16 | 561.357168 | 0.178140 | 0.448205 | 89.880625 | 97.558138 | 450 | 450 |
| 0.50 | 20 | 10 | 495.148712 | 0.201960 | 0.277954 | 67.607084 | 80.598780 | 371 | 371 |
| 0.80 | 20 | 4 | 276.151510 | 0.362120 | 0.110695 | 27.425808 | 47.594018 | 121 | 121 |
| 0.90 | 20 | 2 | 153.354630 | 0.652083 | 0.055285 | 11.364274 | 32.735415 | 0 | 0 |
| 0.995 | 100 | 0.5 | 1055.736631 | 2.368015 | 0.265616 | 9.256399 | 153.837868 | 0 | 0 |
| 0.990 | 100 | 1 | 2100.915984 | 1.189957 | 0.027020 | 20.928166 | 173.717106 | 0 | 0 |
| 0.995 | 200 | 1 | 8445.893049 | 1.184007 | 0.026875 | 40.462071 | 422.905351 | 0 | 0 |
| `1-pi/100` | 100 | pi | 6459.420402 | 0.387032 | 0.182561 | 91.926899 | 273.624581 | 9 | 0 |

The continuous `G-F` sum fails to reach the Weyl target in all these cases.
In fact, the exact floating phase sum is already above `W`; the main missing
margin is the strict fractional-part saving, not merely the enclosure error.

Indeed, with

\[
r_<(x)=x-\#\{n\ge1:n<x\},
\]

one has `0 < r_<(x) <= 1`, with `r_<(m)=1` at positive integers, and

\[
N=S_\gamma-\sum_\ell w_\ell r_<(\gamma_\ell).
\]

Replacing the strict count by a fractional phase discards this weighted
negative correction.

## Thin-shell obstruction

For half-integer orders `nu>=1/2`, Nicholson monotonicity in the order and the
explicit `nu=1/2` modulus imply `theta'_nu(x)<=1`.  Consequently

\[
\gamma_\ell\le\frac{(1-\rho)K}{\pi}.
\]

If `(1-rho)K <= pi`, every strict radial count is zero; equality for `ell=0`
is a phase endpoint and is excluded.  Thus the actual count is zero throughout
this regime, while the continuous `G-F` sum was above `W` in all sampled thin
cases.  The integerized `G-F` envelope often recovers the zero count when the
width is below `pi`; this is precisely why the continuous and integerized
surrogates must not be conflated.

For fixed width one, the data show

| K | rho | Q/W | `S_GF/W` | floating N |
|---:|---:|---:|---:|---:|
| 100 | 0.99 | 1.189957 | 1.082686 | 0 |
| 200 | 0.995 | 1.184007 | 1.050072 | 0 |
| 400 | 0.9975 | 1.181047 | 1.031275 | 0 by the preceding analytic bound |
| 800 | 0.99875 | 1.179571 | 1.018999 | 0 by the preceding analytic bound |

The blanket quarter loss tends to `3*pi/8`, while the sharper `G-F` excess
shrinks relatively but remains on the wrong side in these samples.

## Phase and angular endpoints

For `ell=0`, `gamma_0=(1-rho)K/pi` exactly.  At `rho=0.9` and
`K=10*pi`, `gamma_0=1`.  The strict floating total count immediately below,
at, and immediately above this endpoint was respectively `0, 0, 1`.  At the
endpoint,

- `W = 594.369509`;
- `S_GF = 656.303600`;
- `U_GF = 4`;
- floating strict `N = 0`.

The integer envelope counts weights `1+3`: its first two bounds are
`A_0=1.00126746` and `A_1=1.00014853`, whereas the phases are exactly `1` and
`0.99887548`.  This exposes both the strict endpoint loss and the small phase
enclosure overshoot.

There is a separate wall immediately after a new half-integer channel satisfies
the strict cutoff. For `rho=0.5`, `K=20.5` still has `M=20`; moving just above
`20.5` changes `M` to 21. The newly admitted channel has weight 41, but its
strict integer envelope and floating radial count initially remain zero. This
is why the cutoff must not be replaced by `nu_ell <= K` in the exact lemma.

## Grid observations

A non-certified grid used 100 rho values (`0.01, 0.02, ..., 0.99, 0.999`) and
2,156 K values from `0.05` through `100`. Among the 211,000 cases with at
least one active half-integer mode:

- `S_GF >= W` in all 211,000 cases; the smallest observed ratio was
  `S_GF/W = 1.02815968862`;
- `S_B >= W` in 199,557 cases;
- the strict-integer envelope `U_GF < W` in all 211,000 cases.

This grid says that the fractional `G-F` surrogate is systematically too large
on the sampled region, while strict integerization can restore substantial
margin.  It does not prove either behavior globally.

## Shifted-tail reduction diagnostic

The dimension-three identity

\[
\sum_{\ell\ge0}(2\ell+1)a_\ell
=\sum_{r\ge0}\left(a_r+2\sum_{\ell>r}a_\ell\right)
\]

reduces the coarse integer proxy

\[
a_\ell=\left\lfloor
G_K(\nu_\ell)-G_{\rho K}(\nu_\ell)+\frac14
\right\rfloor
\]

to shifted unweighted tails. The sufficient tail inequality is

\[
a_r+2\sum_{\ell>r}a_\ell
\le
2\int_{r+1/2}^{K}
\left(G_K(z)-G_{\rho K}(z)\right)\,dz.
\]

The script evaluates the integral by a closed elementary formula. On the same
211,000-case grid, it found no shifted-tail violation, including among tails
starting below the inner interface. The minimum floating margin was

\[
4.1129776513\times10^{-7}.
\]

Tails starting at or above `rho*K` are already covered analytically by the
audited FLPS convex floor-sum theorem. The numerical observation for tails
starting below `rho*K` is the diagnostic for the new concave-to-convex
sublemma; it is not a proof, and values near lattice walls require rigorous
integer and interval handling.

A second deterministic stress test sampled 5,000 parameters (3,888 with an
active half-integer channel), alternating
uniform `rho`, logarithmic sampling near zero, and logarithmic sampling near
one, with `K` ranging logarithmically from about `0.063` to `1259`. It found
no shifted-tail violation. The minimum inner-tail floating margin was
`2.54108836629e-8`. This test also remains diagnostic only.

## Reproduction

Run from the repository root:

```powershell
python computations\shell_weighted_lattice_fractional_diagnostic.py --self-test
python computations\shell_weighted_lattice_fractional_diagnostic.py --representative
python computations\shell_weighted_lattice_fractional_diagnostic.py --representative --dict
python computations\shell_weighted_lattice_fractional_diagnostic.py --grid-summary
python computations\shell_weighted_lattice_fractional_diagnostic.py --random-summary 5000 --seed 20260712
python computations\shell_weighted_lattice_fractional_diagnostic.py --rho 0.99 --K 100 --dict
python -m unittest discover -s computations\tests -p "test_*.py"
```

Runtime used for this diagnostic: Python 3.14.4, NumPy 2.4.4, SciPy 1.17.1.
