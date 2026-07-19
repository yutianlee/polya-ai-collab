# Round 17 face-connected pilot extension

Status: **CERTIFIED PASS FOR ONE CLOSED BOX ONLY**.

This work uses the immutable Round 17 residual packet
state/lemma_packets/SHELL-rho-compact-round17.md, SHA-256
eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e.
It does not alter the packet or the accepted analytic mask.

## Chosen face and exact box

The retained Round 8 box is

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right].
$$

The sole Round 17 certification attempt uses its complete upper frequency
face and the rational closed box

$$
\boxed{
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
}
$$

Exactly,

$$
B_0\cap B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times\left\{\frac{168}{25}\right\}.
$$

Thus the intersection is the complete closed upper face of \(B_0\) and the
complete closed lower face of \(B_1\). Their interiors are disjoint. No
second neighbor, tiling, sweep, or adaptive subdivision was opened.

## Exact membership in the analytic residual

On this ratio interval the frozen packet's normalized residual is

$$
\frac{\pi}{1-\rho}<K<K_0(\rho).
$$

Indeed, the packet proves \(\rho_*<1/16\), while

$$
\frac1{16}<\frac{999}{2000},
\qquad
\rho_c=\frac1{1+2\pi}<\frac17<\frac{999}{2000},
\qquad
\frac{1001}{2000}<\frac56.
$$

The formula interface \(\rho=1/2\) lies inside the box, but \(K_0\) is
continuous there and the residual branch does not change. For the lower
wall, \(\pi<22/7\) gives the uniform strict margin

$$
(1-\rho)K-\pi
\ge
\frac{999}{2000}\frac{168}{25}-\frac{22}{7}
=\frac{9353}{43750}>0.
$$

For the upper wall, the packet proves on \(\rho>\rho_c\) that

$$
K_0(\rho)>
\frac{8\pi\rho}{1-\rho}.
$$

Using \(\pi>3\) and monotonicity of \(\rho/(1-\rho)\),

$$
K_0(\rho)-K
>
24\frac{999}{1001}-\frac{673}{100}
=\frac{1723927}{100100}>0.
$$

Both residual inequalities are strict on the complete closed box. Hence

$$
B_1\subset\mathcal D_{16},
\qquad
B_1\setminus B_0\subset\mathcal U_{16}.
$$

This is an analytic set-membership proof from the frozen mask, not a sampled
classification.

## Uniform spectral count

The Arb producer and the independent exact-rational checker use the same
root brackets retained from \(B_0\):

| channel | uniform bracket | lower sign | upper sign | sign on all of \(B_1\) |
|---:|---:|:---:|:---:|:---:|
| \(\ell=0\) | \([31/5,63/10]\) | positive | negative | negative |
| \(\ell=1\) | \([13/2,33/5]\) | positive | negative | negative |

The independent rational determinant enclosures are:

| enclosure | outward lower display | outward upper display |
|---|---:|---:|
| \(R_0\) at \(31/5\) | \(0.0384831486333\) | \(0.0446777766434\) |
| \(R_0\) at \(63/10\) | \(-0.0115570891218\) | \(-0.00525732219166\) |
| \(R_0\) on \(B_1\) | \(-0.224833683652\) | \(-0.2133936843867\) |
| \(R_1\) at \(13/2\) | \(0.0358773134892\) | \(0.0433752387620\) |
| \(R_1\) at \(33/5\) | \(-0.0191634948884\) | \(-0.0115762032280\) |
| \(R_1\) on \(B_1\) | \(-0.0903063637085\) | \(-0.0771341590509\) |

The checker makes every sign decision with exact Fraction endpoints obtained
from Machin and alternating Taylor enclosures. The decimals above are
outward displays only.

For \(w=1-\rho\), the accepted Poincare--Sturm bound is

$$
\lambda_{n,\ell}
\ge\left(\frac{n\pi}{w}\right)^2+\ell(\ell+1).
$$

The independently certified Machin enclosure implies
\(\pi>314159/100000\). At the worst width and upper frequency,

$$
\left(\frac{\pi}{1001/2000}\right)^2+6
-\left(\frac{673}{100}\right)^2
>
\frac{213651639}{2004002000}>0,
$$

so every \(\ell\ge2\) channel is empty. Likewise,

$$
\left(\frac{2\pi}{1001/2000}\right)^2
-\left(\frac{673}{100}\right)^2
>
\frac{1125298725567}{10020010000}>0,
$$

so \(\ell=0,1\) each have at most one radial root. Simplicity,
completeness, the two uniform sign changes, and the negative determinant
enclosures on all of \(B_1\) therefore give exactly one root below every
\(K\) in each of \(\ell=0,1\), with no spectral wall in the target box.
The strict multiplicity-weighted count is

$$
N_D(A_{\rho,1},K^2)=1+3=4.
$$

## Strict Weyl margin

The Weyl expression decreases with \(\rho\) and increases with \(K\), so its
true worst corner on \(B_1\) is

$$
(\rho,K)=\left(\frac{1001}{2000},\frac{168}{25}\right).
$$

Already the coarse exact upper bound \(\pi<22/7\) gives

$$
\frac{2}{9\pi}
\left(1-\left(\frac{1001}{2000}\right)^3\right)
\left(\frac{168}{25}\right)^3-4
>
\frac{39657181883797}{2685546875000}>0.
$$

The independent checker obtains the stronger exact-Fraction lower display
\(14.774446117789985\ldots\). Consequently the target inequality is strict
throughout \(B_1\).

## Independence and reproducibility

The new producer is narrowly parameterized to \(B_1\) and evaluates the
Riccati--spherical determinants with 256-bit Arb balls through the frozen
Round 8 backend. The new checker imports neither the producer nor
python-flint. It uses the previously audited Round 8 rational interval
primitives and independently reconstructs:

1. all authenticated source hashes and the immutable packet hash;
2. the exact complete-face intersection and the one-box condition;
3. both strict residual-membership inequalities;
4. every \(\ell=0,1\) determinant sign with rational Taylor bounds;
5. both Poincare--Sturm exclusions and the weighted count;
6. the Weyl lower bound at the true worst corner.

Reproduction commands:

~~~powershell
python computations/round17_pilot_extension_certificate.py --output rounds/polya-main/round_017/certification/pilot-extension-upward.json
python computations/round17_verify_pilot_extension_certificate.py --input rounds/polya-main/round_017/certification/pilot-extension-upward.json --report rounds/polya-main/round_017/certification/pilot-extension-upward-check.json
python -m pytest computations/tests/test_round17_pilot_extension_certificate.py -q
~~~

Focused result: **6 passed**. Independent certificate result: **PASS**.

| artifact | SHA-256 |
|---|---|
| computations/round17_pilot_extension_certificate.py | 38362dd192c7918a3895eb4b13a1afdd076eaae28a650eb8bed31d517314a2a7 |
| computations/round17_verify_pilot_extension_certificate.py | 40a814e2a3557363d1d958f10c38c295ac0af894e4e8b441ea7dbd0c968991df |
| computations/tests/test_round17_pilot_extension_certificate.py | 71b79d96ff8b7f30cd9b74ed433c4e8b5182fc3e0270db0ad0a5d3f0d3b912a9 |
| rounds/polya-main/round_017/certification/pilot-extension-upward.json | 858c55e832b3ca92f3b077dd7ea55f7ef6c4f7456de786c7264f178fcdf77b5b |
| rounds/polya-main/round_017/certification/pilot-extension-upward-check.json | e3bddf0b1488812e7572c318888f7f4721148b78c5e9ff98f7dabe7b19351d3f |

## Diagnostic evidence versus certification

Before the box was fixed, nearby face directions and floating displays were
used only to select a tractable question. They are not cited in the proof.
No other face was opened after choosing the upper \(K\)-face.

The certification consists only of the exact membership argument above, the
outward Arb artifact, and the independent exact-rational checker PASS. This
adds one local certified box to the overlay. It does not add a branch to
\(\mathcal A_{16}\), close a residual component, prove
\(\mathcal D_{16}=\varnothing\), promote COMP-certified-bessel, or prove the
full shell theorem.
