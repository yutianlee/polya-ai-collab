(* Lower-Q small-phase adjacent-action closure: symbolic replay only. *)

ClearAll[
  z, P, rho, X, Q, u, RR, firstFactor, secondFactor,
  faceX, faceSquare, d, s, zz, phi, Z, poly, x,
  bernsteinCoefficient, bernsteinMatrix, expectedMatrix,
  qpoly, sstar
];

u[y_] := Sqrt[1 - y^2];
X = z + P;
Q = z + (1 + rho) P;

RR = (u[z] - u[X])/(u[X] - u[Q]);
firstFactor = (2 z + P)/(rho (2 z + (2 + rho) P));
secondFactor = (u[X] + u[Q])/(u[z] + u[X]);

adjacentRationalizationResidual = FullSimplify[
  RR - firstFactor secondFactor,
  0 < z < X < Q < 1 && P > 0 && rho > 0
];

firstFactorClearedDerivative = FullSimplify[
  D[firstFactor, P] rho (2 z + (2 + rho) P)^2,
  z > 0 && P > 0 && rho > 0
];

secondFactorLogDerivativeResidual = FullSimplify[
  D[Log[secondFactor], P] -
    (-(X/u[X] + (1 + rho) Q/u[Q])/(u[X] + u[Q]) +
      X/(u[X] (u[z] + u[X]))),
  0 < z < X < Q < 1 && P > 0 && rho > 0
];

faceX = (1 + rho z)/(1 + rho);
faceSquare = (u[z]/u[faceX])^2;

faceSquareResidual = FullSimplify[
  faceSquare -
    (1 + z) (1 + rho)^2/(rho (2 + rho (1 + z))),
  0 < z < faceX < 1 && rho > 0
];

faceLogZDerivativeResidual = FullSimplify[
  D[Log[(1 + z) (1 + rho)^2/
      (rho (2 + rho (1 + z)))], z] -
    2/((1 + z) (2 + rho (1 + z))),
  z > 0 && rho > 0
];

phi = 4 (1 + z) (1 + rho)^2 -
  rho (2 + rho (1 + z)) (3 - d rho)^2;

phiZFactorResidual = Expand[
  D[phi, z] -
    (2 (1 + rho) - rho (3 - d rho))
    (2 (1 + rho) + rho (3 - d rho))
];

zLowerAlgebraResidual = FullSimplify[
  4 #^3/(9 Pi) - 4 #^3/Pi^3 -
    4 #^3 (Pi^2 - 9)/(9 Pi^3)
] & [Symbol["tt"]];

Z = (1 - d)^3/2;
poly = Expand[
  4 (1 + Z) (d + s)^2 -
    s (2 d + s (1 + Z)) (3 - s)^2
];

normalizedPolynomialResidual = FullSimplify[
  d^2 (phi /. {z -> Z, rho -> s/d}) - poly,
  d > 0
];

pdMapped = Expand[D[poly, d] /. d -> (3 + x)/4];

bernsteinCoefficient[expr_, xv_, sv_, nx_, ns_, i_, j_] :=
  FullSimplify[
    Sum[
      Coefficient[Coefficient[expr, xv, k], sv, l]
        Binomial[i, k]/Binomial[nx, k]
        Binomial[j, l]/Binomial[ns, l],
      {k, 0, i}, {l, 0, j}
    ]
  ];

bernsteinMatrix = Table[
  bernsteinCoefficient[pdMapped, x, s, 4, 4, i, j],
  {i, 0, 4}, {j, 0, 4}
];

expectedMatrix = {
  {747/128, 411/128, 341/128, 455/128, 683/128},
  {51/8, 243/64, 417/128, 67/16, 97/16},
  {111/16, 141/32, 1493/384, 311/64, 109/16},
  {15/2, 5, 9/2, 11/2, 15/2},
  {8, 11/2, 5, 6, 8}
};

qpoly = 387 - 1272 s + 676 s^2 + 776 s^3 - 172 s^4;
sstar = 17/32;

boundaryPolynomialResidual = Expand[
  (poly /. d -> 3/4) - 3 qpoly/512
];

qExactValues = {
  qpoly /. s -> sstar,
  D[qpoly, s] /. s -> sstar,
  FullSimplify[
    (qpoly /. s -> sstar) -
      (D[qpoly, s] /. s -> sstar)^2/(2 1352)
  ]
};

roundSmallPhaseReplayOK = And[
  adjacentRationalizationResidual === 0,
  firstFactorClearedDerivative === -2 z (1 + rho),
  secondFactorLogDerivativeResidual === 0,
  faceSquareResidual === 0,
  faceLogZDerivativeResidual === 0,
  phiZFactorResidual === 0,
  zLowerAlgebraResidual === 0,
  normalizedPolynomialResidual === 0,
  bernsteinMatrix === expectedMatrix,
  Min[Flatten[bernsteinMatrix]] === 341/128,
  boundaryPolynomialResidual === 0,
  qExactValues === {
    1227605/262144,
    245/2048,
    53111042695/11341398016
  }
];

Print["adjacentRationalizationResidual=", adjacentRationalizationResidual];
Print["firstFactorClearedDerivative=", firstFactorClearedDerivative];
Print["secondFactorLogDerivativeResidual=", secondFactorLogDerivativeResidual];
Print["faceSquareResidual=", faceSquareResidual];
Print["faceLogZDerivativeResidual=", faceLogZDerivativeResidual];
Print["phiZFactorResidual=", phiZFactorResidual];
Print["zLowerAlgebraResidual=", zLowerAlgebraResidual];
Print["normalizedPolynomialResidual=", normalizedPolynomialResidual];
Print["bernsteinMatrix=", bernsteinMatrix];
Print["minimumBernsteinCoefficient=", Min[Flatten[bernsteinMatrix]]];
Print["boundaryPolynomialResidual=", boundaryPolynomialResidual];
Print["qExactValues=", qExactValues];
Print["roundSmallPhaseReplayOK=", roundSmallPhaseReplayOK];

