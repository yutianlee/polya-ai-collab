(* Round 48 exact algebra replay for the full outer inverse-action cell. *)

ClearAll[alpha, beta, r, h, n, v, s2, past, future, q];

alpha = 3/4;
beta = 1/4;
s2[n_] := n (n + 1) (2 n + 1)/6;

past = Integrate[(alpha - v) (r + v/h)^2/h, {v, 0, alpha},
  Assumptions -> {r >= 0, h > 0}];
future = Integrate[(beta - v) r^2/h, {v, 0, beta},
  Assumptions -> {r >= 0, h > 0}];

pastFormula =
  alpha^2 r^2/(2 h) + alpha^3 r/(3 h^2) + alpha^4/(12 h^3);

kernelCoefficients = FullSimplify[
  past - future == r^2/(4 h) + 9 r/(64 h^2) + 27/(1024 h^3),
  Assumptions -> {r >= 0, h > 0}
];

pastIntegral = FullSimplify[past == pastFormula,
  Assumptions -> {r >= 0, h > 0}];

q[n_, r_] := r^3/3 - s2[n] + r^2/2 + 9 r/16 + 27/128;

lowerFace = FullSimplify[
  q[n, n] == 19 n/48 + 27/128,
  Assumptions -> n >= 0
];

positiveDerivative = FullSimplify[
  D[q[n, r], r] == r^2 + r + 9/16 && r^2 + r + 9/16 > 0,
  Assumptions -> r >= 0
];

hHalfDirection = FullSimplify[
  r^2/(4 h) + 9 r/(64 h^2) + 27/(1024 h^3) >=
    r^2/2 + 9 r/16 + 27/128,
  Assumptions -> {r >= 0, 0 < h <= 1/2}
];

e[r_, d_] :=
  ((r - d + 1/2)^4 - (r - d)^4)/8 +
  ((r + 3 d)^4 - r^4)/(16 d);

cleanDerivative = FullSimplify[
  D[e[r, d], d] ==
    21 r^2/8 + 15 r d + 231 d^2/16 - 3 r/8 + 3 d/8 - 1/16,
  Assumptions -> {r >= d >= 1/2}
];

cleanLowerFace = FullSimplify[
  e[r, 1/2] == r^3 + 3 r^2/2 + 7 r/4 + 5/8,
  Assumptions -> r >= 1/2
];

cleanReserve = FullSimplify[
  (5 n/12 + 5/24) - (19 n/48 + 27/128) == (8 n - 1)/384,
  Assumptions -> n >= 1
];

cleanNZero = FullSimplify[
  (r^3/3 + r^2/2 + 7 r/12 + 5/24 /. r -> 1/2) == 2/3 &&
  2/3 - 27/128 == 175/384
];

Print["pastIntegral=", pastIntegral];
Print["kernelCoefficients=", kernelCoefficients];
Print["lowerFace=", lowerFace];
Print["positiveDerivative=", positiveDerivative];
Print["hHalfDirection=", hHalfDirection];
Print["cleanDerivative=", cleanDerivative];
Print["cleanLowerFace=", cleanLowerFace];
Print["cleanReserve=", cleanReserve];
Print["cleanNZero=", cleanNZero];

round48OuterCellReplayOK = And[
  pastIntegral,
  kernelCoefficients,
  lowerFace,
  positiveDerivative,
  hHalfDirection,
  cleanDerivative,
  cleanLowerFace,
  cleanReserve,
  cleanNZero
];

Print["round48OuterCellReplayOK=", round48OuterCellReplayOK];

If[TrueQ[round48OuterCellReplayOK], Exit[0], Exit[1]];
