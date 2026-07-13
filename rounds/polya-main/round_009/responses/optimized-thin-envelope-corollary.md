# Round 9 corollary: enlarged endpoint and compressed compact envelope

Assume the optimized local-plateau theorem

$$
0<\varepsilon\le\frac1{100},
\qquad
K\ge\frac{125}{8\varepsilon^2}.
\tag{1}
$$

This note records its exact consequences for the Round 8 analytic envelope.

## 1. Enlarged all-frequency endpoint

The promoted aggregate-action theorem covers

$$
K\le\frac1{8\varepsilon^{5/2}}.
\tag{2}
$$

The inclusive ranges (1)--(2) overlap if and only if

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
125\sqrt\varepsilon\le1
\iff
\varepsilon\le\frac1{15625}.
$$

At equality their common value is

$$
\frac{125^5}{8}<2^{32}.
$$

Therefore

$$
\boxed{
1-\frac1{15625}\le\rho<1,
\quad K\ge0
\Longrightarrow\text{shell Pólya}.
}
\tag{3}
$$

The lower endpoint in (3) is included.

## 2. Updated three-zone compact envelope

Let

$$
I_9=
\left[\rho_*,1-\frac1{15625}\right].
$$

The Round 8 left and central arguments are unchanged:

- on $[\rho_*,1/16]$, every possible residual has $K<64$;
- on $[1/16,99/100]$, every possible residual has
  $K<180000^2<2^{35}$.

On the updated thin zone, put $\varepsilon=1-\rho$.  Then

$$
\frac1{15625}\le\varepsilon\le\frac1{100}.
$$

The aggregate-action and optimized local-plateau theorems leave only

$$
\frac1{8\varepsilon^{5/2}}
<K<
\frac{125}{8\varepsilon^2}.
$$

The upper endpoint is decreasing in $\varepsilon$, so

$$
K
<\frac{125^5}{8}
<2^{32}.
$$

Thus all three zones lie below $2^{35}$, and

$$
\boxed{
\rho\in I_9,
\quad K\ge2^{35}
\Longrightarrow\text{shell Pólya}.
}
\tag{4}
$$

Combining (3), (4), and the already-proved small-hole endpoint also gives

$$
\boxed{
0<\rho<1,
\quad K\ge2^{35}
\Longrightarrow\text{shell Pólya}.
}
\tag{5}
$$

## 3. Scope

This corollary removes the old thin band

$$
2^{-18}<\varepsilon\le\frac1{15625}
$$

from the certificate target and reduces the global high-frequency ceiling by
a factor $2^7$.  It does not certify the remaining compact residual below
$2^{35}$, so SHELL-rho-compact, SHELL-rho-uniformity, and the final target
remain open.
