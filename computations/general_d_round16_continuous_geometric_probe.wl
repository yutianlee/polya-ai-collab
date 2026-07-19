(*
  Diagnostic evaluator for the Round 16 continuous/geometric reduction.

  The script imports the audited Round 15 endpoint records, removes the
  favorable strict-floor reserve 2 eta, minimizes the resulting convex
  scalar in its real spatial variable, and checks the exact reduction to

    F = J_K(x) - J_a(x) - (z - x),   A(x) = 1.

  It also replays the suspected q=3 hard double face and the apparent
  continuous cusp.  All floating-point searches are theorem-design evidence
  only; the rational hard-face reserve is an exact arithmetic regression.
*)

round15Probe = FileNameJoin[{
  DirectoryName[$InputFileName],
  "general_d_round15_exact_terminal_endpoint_probe.wl"
}];
Get[round15Probe];

round16DiagnosticOnly = True;

ClearAll[
  extendedJ, endpointCriticalPoint, round16EndpointRecord, round16Compact,
  inverseThreeQuarterPoint
];

extendedJ[b_?NumericQ, s_?NumericQ] := ballTailIntegral[b, s];

inverseThreeQuarterPoint[k_?NumericQ] := Module[{theta},
  theta = ballAngle[k, 3/4];
  k Cos[theta]
];

endpointCriticalPoint[rec_Association] := Module[
  {k, q, a, z, xx},
  k = rec["K"];
  q = rec["q"];
  a = q + endpointAlpha[rec];
  z = k Cos[First[rec["terminal"]["angles"]]];
  xx /. FindRoot[
    shellAction[k, a, xx] == 1,
    {xx, 0, z},
    Method -> "Brent",
    WorkingPrecision -> 50,
    AccuracyGoal -> 35,
    PrecisionGoal -> 35
  ]
];

round16EndpointRecord[rec_Association] := Module[
  {k, q, r, a, z, eta, omega, omega0, x, f, emin},
  k = rec["K"];
  q = rec["q"];
  r = rec["r"];
  a = q + endpointAlpha[rec];
  z = k Cos[First[rec["terminal"]["angles"]]];
  eta = First[rec["terminal"]["etas"]];
  omega = exactFullScalarAt[rec, endpointAlpha[rec]];
  omega0 = omega - 2 eta;
  x = endpointCriticalPoint[rec];
  f = extendedJ[k, x] - extendedJ[a, x] - (z - x);
  emin = 2 f - 1;
  <|
    "K" -> k,
    "a" -> a,
    "r" -> r,
    "q" -> q,
    "z" -> z,
    "x" -> x,
    "A0" -> shellAction[k, a, 0],
    "AAtMinusOne" -> shellAction[k, a, a - 1],
    "AAtZ" -> shellAction[k, a, z],
    "eta" -> eta,
    "omegaEndpoint" -> omega,
    "continuousEndpoint" -> omega0,
    "F" -> f,
    "continuousMinimum" -> emin,
    "convexSlack" -> omega0 - emin,
    "continuousIdentityResidual" ->
      omega0 - (2 (extendedJ[k, r] - extendedJ[a, r]) - 2 (z - r) - 1)
  |>
];

round16Compact[rec_Association] := Map[N[#, 24] &, rec];

round16EndpointRecords = round16EndpointRecord /@ hardExtensionRecords;
round16MinimumContinuousRecord = First@MinimalBy[
  round16EndpointRecords,
  N[#1["continuousEndpoint"], 30] &
];
round16MinimumFRecord = First@MinimalBy[
  round16EndpointRecords,
  N[#1["F"], 30] &
];
round16MinimumSlackRecord = First@MinimalBy[
  round16EndpointRecords,
  N[#1["convexSlack"], 30] &
];
round16DomainViolationCount = Count[
  round16EndpointRecords,
  rec_ /; Or[
    N[rec["a"], 30] < 2,
    N[rec["K"] - rec["a"], 30] <= Pi,
    N[rec["A0"], 30] <= 1,
    N[rec["AAtMinusOne"], 30] < 3/4 - 10^-24,
    N[rec["AAtZ"], 30] >= 1,
    N[rec["z"], 30] <= 2
  ]
];
round16IdentityFailureCount = Count[
  round16EndpointRecords,
  rec_ /; Abs[N[rec["continuousIdentityResidual"], 30]] > 10^-24
];

(* Apparent cusp: simultaneous phase and alpha=1 wall at q=5, r=1. *)
round16CuspQ = N[5, wp];
round16CuspA = N[6, wp];
round16CuspK = kk /. FindRoot[
  shellAction[kk, round16CuspA, round16CuspQ] == 3/4,
  {kk, N[9.2, wp]},
  WorkingPrecision -> 60,
  AccuracyGoal -> 45,
  PrecisionGoal -> 45
];
round16CuspZ = inverseThreeQuarterPoint[round16CuspK];
round16CuspContinuous =
  (2 (extendedJ[round16CuspK, 1] - extendedJ[round16CuspA, 1])
   - 2 (round16CuspZ - 1) - 1);

(* Enlarged-domain apparent minimizer: K-a=Pi and A(a-1)=3/4. *)
round16DoubleWallA = aa /. FindRoot[
  shellAction[aa + Pi, aa, aa - 1] == 3/4,
  {aa, N[5.59, wp]},
  WorkingPrecision -> 60,
  AccuracyGoal -> 45,
  PrecisionGoal -> 45
];
round16DoubleWallK = round16DoubleWallA + Pi;
round16DoubleWallZ = inverseThreeQuarterPoint[round16DoubleWallK];
round16DoubleWallF =
  (extendedJ[round16DoubleWallK, 0]
   - extendedJ[round16DoubleWallA, 0]
   - round16DoubleWallZ);

(* Exact rational lower reserve for the q=3, r=1, n=2 double face. *)
round16TaylorX = 107/100;
round16CosUpper =
  1 - round16TaylorX^2/2 + round16TaylorX^4/24;
round16LambdaLower = 21/22 (1/round16CosUpper - 1);
round16HardFaceRationalReserve =
  (9 (3141/1000)/(16 (108/100)) - 2
   + 56/27 (round16LambdaLower - 3/4));
round16ExpectedHardFaceReserve =
  15150166179733/73320166719360;

round16HardTheta = th /. FindRoot[
  Tan[th] - th == Pi/4,
  {th, N[1.075, wp]},
  WorkingPrecision -> 60,
  AccuracyGoal -> 45,
  PrecisionGoal -> 45
];
round16HardK = 3 Sec[round16HardTheta];
round16HardOmega =
  2 (extendedJ[round16HardK, 1] - extendedJ[3, 1]) - 5;

Print["round16DiagnosticOnly=", round16DiagnosticOnly];
Print["round16EndpointRecords=", Length[round16EndpointRecords]];
Print["round16DomainViolationCount=", round16DomainViolationCount];
Print["round16IdentityFailureCount=", round16IdentityFailureCount];
Print[
  "round16MinimumContinuousEndpoint=",
  round16Compact[round16MinimumContinuousRecord] // InputForm
];
Print[
  "round16MinimumF=",
  round16Compact[round16MinimumFRecord] // InputForm
];
Print[
  "round16MinimumConvexSlack=",
  round16Compact[round16MinimumSlackRecord] // InputForm
];
Print[
  "round16Cusp=",
  N[<|
    "K" -> round16CuspK,
    "z" -> round16CuspZ,
    "continuous" -> round16CuspContinuous
  |>, 30] // InputForm
];
Print[
  "round16DoubleWall=",
  N[<|
    "a" -> round16DoubleWallA,
    "K" -> round16DoubleWallK,
    "z" -> round16DoubleWallZ,
    "F" -> round16DoubleWallF
  |>, 30] // InputForm
];
Print[
  "round16HardFaceRationalReserve=",
  round16HardFaceRationalReserve // InputForm
];
Print[
  "round16HardFaceNumerical=",
  N[<|
    "theta" -> round16HardTheta,
    "K" -> round16HardK,
    "omega" -> round16HardOmega
  |>, 30] // InputForm
];

round16ReplayOK = And[
  Length[round16EndpointRecords] == 3171,
  round16DomainViolationCount == 0,
  round16IdentityFailureCount == 0,
  N[round16MinimumContinuousRecord["continuousEndpoint"], 30] > 1/3,
  N[round16MinimumFRecord["F"], 30] > 1/2,
  N[round16MinimumSlackRecord["convexSlack"], 30] > -10^-24,
  17/50 < N[round16CuspContinuous, 30] < 7/20,
  N[round16DoubleWallF, 30] > 3/5,
  round16HardFaceRationalReserve === round16ExpectedHardFaceReserve,
  round16HardFaceRationalReserve > 1/5,
  N[round16HardOmega, 30] > 7/10
];

Print["round16ReplayOK=", round16ReplayOK];

If[!TrueQ[round16ReplayOK], Exit[2]];
