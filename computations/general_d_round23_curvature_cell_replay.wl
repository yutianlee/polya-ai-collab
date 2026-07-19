(*
  Round 23 minimal independent replay.

  The exact/symbolic checks below audit the cap endpoint chain and the
  derivatives on a fixed curvature cell.  The final hard-family evaluation
  is explicitly diagnostic high-precision arithmetic: it checks the
  alpha -> 1 limiting pattern reported in the note, not the open sign
  obligation C8 >= 0.
*)

ClearAll["Global`*"];
$MaxExtraPrecision = 5000;

(* Exact cap endpoint and every printed rational comparison. *)
capEndpoint = (34 ArcCos[3/4] - 9 Sqrt[7])/(2 Pi);
halfAngleOK = TrueQ[FullSimplify[
   ArcCos[3/4] == 2 ArcTan[1/Sqrt[7]]
]];
atanUpperOK = TrueQ[FullSimplify[
   ArcTan[1/Sqrt[7]] <
    1/Sqrt[7] - 1/(3 7^(3/2)) + 1/(5 7^(5/2))
]];
numeratorReductionOK = TrueQ[FullSimplify[
   68 (1/Sqrt[7] - 1/(3 7^(3/2)) + 1/(5 7^(5/2))) -
     9 Sqrt[7] == 1499/(735 Sqrt[7])
]];
sqrtBoundOK = TrueQ[FullSimplify[Sqrt[7] > 37/14]];
crossDifferenceOK =
  333*27195 - 20986*424 == 157871;
rationalChainOK = And[
  TrueQ[FullSimplify[1499/(735 Sqrt[7]) < 20986/27195]],
  TrueQ[20986/27195 < 333/424],
  TrueQ[FullSimplify[333/424 < Pi/4]]
];
capEndpointOK = TrueQ[FullSimplify[capEndpoint < 1/8]];

(* Symbolic differentiation on one open cell. *)
Clear[t, muS, c0S, mS, bS, fS, constS];
wS = muS/Pi (Tan[t] - t);
wPrimeOK = TrueQ[FullSimplify[D[wS, t] == muS/Pi Tan[t]^2]];
wSecondOK = TrueQ[FullSimplify[
   D[wS, {t, 2}] == 2 muS/Pi Tan[t] Sec[t]^2
]];

c8Constant = c0S (1 - Cos[t]) + mS/2 (1 - 2 t/Pi) +
   bS (Pi/(2 t) - 1) + constS;
c8Quadratic = c8Constant + 2 (wS - (fS - 1))^2;

constantFirstOK = TrueQ[FullSimplify[
   D[c8Constant, t] ==
    c0S Sin[t] - mS/Pi - bS Pi/(2 t^2)
]];
constantSecondOK = TrueQ[FullSimplify[
   D[c8Constant, {t, 2}] == c0S Cos[t] + bS Pi/t^3
]];
quadraticFirstOK = TrueQ[FullSimplify[
   D[c8Quadratic, t] ==
    c0S Sin[t] - mS/Pi - bS Pi/(2 t^2) +
     4 (wS - (fS - 1)) D[wS, t]
]];
quadraticSecondOK = TrueQ[FullSimplify[
   D[c8Quadratic, {t, 2}] ==
    c0S Cos[t] + bS Pi/t^3 +
     4 (D[wS, t]^2 + (wS - (fS - 1)) D[wS, {t, 2}])
]];

(* Diagnostic alpha -> 1 hard-family boundary. *)
ballAction[a_, z_] :=
  (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi;
capIntegral[a_, z_] :=
  a^2/(4 Pi) ((1 + 2 (z/a)^2) ArcCos[z/a] -
    3 (z/a) Sqrt[1 - (z/a)^2]);

r0 = 1; p0 = 3; m0 = 2; f0 = 2; q0 = 6; mu0 = 7;
x0 = r0 + p0; h0 = f0 - 1/4;
aHard[tt_?NumericQ, z_] :=
  ballAction[mu0/Cos[tt], z] - ballAction[mu0, z];

tHard = t /. FindRoot[
   aHard[t, x0] == h0,
   {t, SetPrecision[1.005, 100]},
   WorkingPrecision -> 100, AccuracyGoal -> 75, PrecisionGoal -> 75
];
wHard = mu0/Pi (Tan[tHard] - tHard);
lambdaHard = h0 - wHard;
bHard = Floor[wHard + 1/4];
eHard = 2 (3/4 - lambdaHard)^2;
c0Hard = p0^2 (3 r0 + 2 p0)/(3 Pi mu0);
c8Hard = c0Hard (1 - Cos[tHard]) - p0/2 +
  m0/2 (1 - 2 tHard/Pi) +
  bHard (Pi/(2 tHard) - 1) + eHard - 1/8;
jHard = 2 capIntegral[mu0, q0];
rjCurvatureHard = c8Hard + 1/8 - jHard;

activityHard = mu0^2/Cos[tHard]^2 -
  Pi^2/(1 - Cos[tHard])^2 - 3/4;
hardDomainOK = And[
  Abs[aHard[tHard, x0] - h0] < 10^-70,
  aHard[tHard, x0 + 1] < h0,
  aHard[tHard, r0] < h0 + 1,
  activityHard > 0,
  bHard == 1,
  3/4 - 1/Sqrt[2] < lambdaHard < 3/4
];
hardValuesOK = And[
  Abs[tHard - SetPrecision[1.005008958418235, 50]] < 10^-15,
  Abs[lambdaHard - SetPrecision[0.480629613415452, 50]] < 10^-15,
  Abs[c8Hard - SetPrecision[0.012864451980857, 50]] < 10^-15,
  Abs[rjCurvatureHard - SetPrecision[0.046649621533640, 50]] < 10^-15
];

exactSymbolicOK = And[
  halfAngleOK, atanUpperOK, numeratorReductionOK, sqrtBoundOK,
  crossDifferenceOK, rationalChainOK, capEndpointOK,
  wPrimeOK, wSecondOK, constantFirstOK, constantSecondOK,
  quadraticFirstOK, quadraticSecondOK
];
round23ReplayOK = And[exactSymbolicOK, hardDomainOK, hardValuesOK];

Print["exactSymbolicOK=", exactSymbolicOK];
Print["capEndpointN=", N[capEndpoint, 30]];
Print["hardDomainOK=", hardDomainOK];
Print["tHard=", N[tHard, 30]];
Print["lambdaHard=", N[lambdaHard, 30]];
Print["C8Hard=", N[c8Hard, 30]];
Print["RJCurvatureHard=", N[rjCurvatureHard, 30]];
Print["hardValuesOK=", hardValuesOK];
Print["round23ReplayOK=", round23ReplayOK];

If[! TrueQ[round23ReplayOK], Exit[1]];
