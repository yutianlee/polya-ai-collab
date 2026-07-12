# Bessel cross-product finite-window diagnostic

> **FLOATING-POINT DIAGNOSTIC — NOT CERTIFIED.** This report does not discharge
> `COMP-certified-bessel` or any proof obligation.

## Deterministic reproduction

```powershell
python -m pip install -r computations/requirements-diagnostic.txt
python computations/bessel_cross_product_diagnostic.py --output computations/results/bessel_cross_product_rho_half.md
python -m unittest discover -s computations/tests -p "test_*.py"
```

- Arithmetic: `mpmath 1.4.1` multiprecision floating point at `80` decimal digits.
- Target window: `rho=0.5`, `ell=0,1,2`, `0 < k < 20.0`; numerical scan starts at `k=0.000001`.
- Scan step: `0.01`; bisection target width: `1.0e-20`.
- Evaluator A: raw ordinary-Bessel cross-product.
- Evaluator B: Riccati–spherical trigonometric recurrence, rescaled to the raw normalization.

## Evaluator comparison

With `psi_ell(z)=z j_ell(z)` and `eta_ell(z)=z y_ell(z)`, the stabilized determinant is `R_ell(k)=psi_ell(rho k) eta_ell(k)-psi_ell(k) eta_ell(rho k)`, and `F_(ell+1/2,rho)(k)=2 R_ell(k)/(pi k sqrt(rho))`.

The discrepancy is `|raw-stabilized| / max(1,|raw|,|stabilized|)`.

| ell | k | raw Bessel F | stabilized-as-raw F | scaled discrepancy |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0.25 | 4.48986786717e-1 | 4.48986786717e-1 | 0.0 |
| 0 | 1.0 | 4.31634634788e-1 | 4.31634634788e-1 | 0.0 |
| 0 | 3.0 | 2.99353670575e-1 | 2.99353670575e-1 | 5.271e-82 |
| 0 | 7.0 | -4.51165519033e-2 | -4.51165519033e-2 | 1.318e-82 |
| 0 | 11.0 | -5.77463151653e-2 | -5.77463151653e-2 | 0.0 |
| 0 | 17.0 | 4.22877044551e-2 | 4.22877044551e-2 | 6.589e-83 |
| 1 | 0.25 | 5.23895983109e-1 | 5.23895983109e-1 | 5.271e-81 |
| 1 | 1.0 | 5.04802005118e-1 | 5.04802005118e-1 | 0.0 |
| 1 | 3.0 | 3.58800502167e-1 | 3.58800502167e-1 | 1.054e-81 |
| 1 | 7.0 | -2.97517737169e-2 | -2.97517737169e-2 | 1.977e-82 |
| 1 | 11.0 | -6.39737498007e-2 | -6.39737498007e-2 | 1.318e-82 |
| 1 | 17.0 | 4.44557893942e-2 | 4.44557893942e-2 | 6.589e-83 |
| 2 | 0.25 | 6.96197174263e-1 | 6.96197174263e-1 | 1.46e-78 |
| 2 | 1.0 | 6.73245507369e-1 | 6.73245507369e-1 | 3.163e-81 |
| 2 | 3.0 | 4.96803271677e-1 | 4.96803271677e-1 | 1.054e-81 |
| 2 | 7.0 | 9.3842247594e-3 | 9.3842247594e-3 | 1.647e-83 |
| 2 | 11.0 | -7.59232874844e-2 | -7.59232874844e-2 | 2.636e-82 |
| 2 | 17.0 | 4.84880229941e-2 | 4.84880229941e-2 | 0.0 |

## Small-k symbolic sanity check

The recurrence gives the formal expansion `R_ell(k) = c_ell(rho) k + O(k^3)`, where `c_ell(rho) = (rho^(-ell)-rho^(ell+1))/(2 ell+1)`.
The positive coefficients below are consistent with no near-zero sign change, but the unbounded remainder means this does not verify the unscanned interval.

| ell | c_ell(1/2) | sign |
| ---: | ---: | :---: |
| 0 | 0.5 | positive |
| 1 | 0.583333333333333333333333333333 | positive |
| 2 | 0.775 | positive |

## Approximate sign-change brackets

Each row is a floating-point sign-change/bisection result, not an interval enclosure.

| ell | radial index | approximate left | approximate right | midpoint | |R(midpoint)| |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 6.2831853071795864769189 | 6.2831853071795864769276 | 6.2831853071795865 | 1.019e-21 |
| 0 | 2 | 12.5663706143591729538491 | 12.5663706143591729538578 | 12.5663706143591730 | 1.442e-21 |
| 0 | 3 | 18.8495559215387594307707 | 18.8495559215387594307793 | 18.8495559215387594 | 4.346e-22 |
| 1 | 1 | 6.5720131990163510547998 | 6.5720131990163510548085 | 6.5720131990163511 | 2.48e-22 |
| 1 | 2 | 12.7213563474180171559086 | 12.7213563474180171559173 | 12.7213563474180172 | 1.139e-21 |
| 1 | 3 | 18.9543920958525072079760 | 18.9543920958525072079847 | 18.9543920958525072 | 1.655e-21 |
| 2 | 1 | 7.1115762381449787977458 | 7.1115762381449787977545 | 7.1115762381449788 | 6.259e-22 |
| 2 | 2 | 13.0261363626507821801793 | 13.0261363626507821801880 | 13.0261363626507822 | 9.79e-23 |
| 2 | 3 | 19.1625403296092178636782 | 19.1625403296092178636869 | 19.1625403296092179 | 1.078e-21 |

## Counting summary

| ell | approximate radial root count | angular multiplicity 2 ell + 1 | weighted contribution |
| ---: | ---: | ---: | ---: |
| 0 | 3 | 1 | 3 |
| 1 | 3 | 3 | 9 |
| 2 | 3 | 5 | 15 |
| **total** | **9** | — | **27** |

Diagnostic conclusion: the fixed-grid scan finds `9` radial roots and a dimension-three multiplicity-weighted count of `27` for the selected `ell` values below `k=20.0` (equivalently below `Lambda=400.0`).

## Limitations

- `mpmath` values are multiprecision floating-point approximations, not interval or ball values.
- Printed brackets are not outward-rounded and therefore are not rigorous enclosures.
- A fixed sign-change grid does not prove that every zero was found or that no even-multiplicity zero was missed.
- The numerical scan omits `0 < k < 0.000001`; the displayed formal small-`k` term has no controlled remainder.
- The recurrence and raw evaluator agreement is a diagnostic cross-check, not an independence proof.
- Here, `stabilized` means amplitude-rescaled; numerical stability of upward recurrence is not established beyond these low orders and this window.
- Only `rho=1/2`, `ell=0,1,2`, and the finite window `0<k<20` are explored.
- Certification still requires validated special-function evaluation, rigorous root isolation, domain coverage, and reproducible interval/ball arithmetic.
