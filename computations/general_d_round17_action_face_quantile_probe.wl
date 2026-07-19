(*
  Diagnostic replay for the Round 17 action-face quantile reduction.

  This imports the Round 16 evaluator, constructs points on
  A(a-1)=3/4 from the simultaneous wall through a=10^5, and evaluates the
  exact action-face derivative, its quantile decomposition, and the concave
  chord scalar S.  Finite differences of Q are diagnostic only.  No interval
  arithmetic or coverage theorem is claimed.
*)

round16Probe = FileNameJoin[{
  DirectoryName[$InputFileName],
  "general_d_round16_continuous_geometric_probe.wl"
}];
Get[round16Probe];

round17DiagnosticOnly = True;

ClearAll[
  round17ActionK, round17U, round17P, round17ActionRecord,
  round17Compact
];

round17ActionK[aa_?NumericQ] := kk /. FindRoot[
  shellAction[kk, aa, aa - 1] == 3/4,
  {kk, aa + Pi, aa + 4 Sqrt[aa]},
  Method -> "Brent",
  WorkingPrecision -> 55,
  AccuracyGoal -> 38,
  PrecisionGoal -> 38
];

round17U[bb_?NumericQ, cc_?NumericQ] := If[
  cc == 0,
  1,
  With[{ang = ballAngle[bb, cc]}, Sin[ang]/ang]
];

round17P[bb_?NumericQ, ss_?NumericQ] := If[
  ss >= bb,
  0,
  (bb^2 ArcCos[ss/bb] - ss Sqrt[bb^2 - ss^2])/(2 Pi bb)
];

round17ActionRecord[aa_?NumericQ] := Module[
  {
    k, t, x, g, gamma, phi, speed, theta, beta1, beta, psi,
    bReserve, q0, qg, derivative, chord, speedResidual,
    decompositionResidual, qGrid, qValues, firstDiffs, secondDiffs
  },
  k = round17ActionK[aa];
  t = aa - 1;
  x = xx /. FindRoot[
    shellAction[k, aa, xx] == 1,
    {xx, 0, t},
    Method -> "Brent",
    WorkingPrecision -> 50,
    AccuracyGoal -> 34,
    PrecisionGoal -> 34
  ];
  g = ballAction[aa, x];
  gamma = ArcCos[t/k];
  phi = ArcCos[t/aa];
  speed = (gamma + Sin[phi] - phi)/Sin[gamma];
  theta = ballAngle[k, 3/4];
  beta1 = ballAngle[k, 1];
  beta = ArcCos[x/k];
  psi = ArcCos[x/aa];
  bReserve = round17P[k, k Cos[beta1]] - Sin[theta]/theta;
  q0 = speed Sin[beta1]/beta1 - 1;
  qg = speed Sin[beta]/beta - Sin[psi]/psi;
  derivative =
    speed (round17P[k, x] - Sin[theta]/theta) - round17P[aa, x];
  chord = speed bReserve + g/2 (q0 + qg);
  speedResidual =
    k/aa - speed - (3 Pi/4 - gamma + phi)/(aa Sin[gamma]);
  decompositionResidual = derivative - (
    speed bReserve
    + speed (round17P[k, x] - round17P[k, k Cos[beta1]])
    - round17P[aa, x]
  );
  qGrid = N[Subdivide[0, g, 20], 45];
  qValues = (
    speed round17U[k, # + 1] - round17U[aa, #]
  ) & /@ qGrid;
  firstDiffs = Differences[qValues];
  secondDiffs = Differences[firstDiffs];
  <|
    "a" -> aa,
    "K" -> k,
    "x" -> x,
    "g" -> g,
    "speed" -> speed,
    "KOverA" -> k/aa,
    "B" -> bReserve,
    "Q0" -> q0,
    "Qg" -> qg,
    "derivative" -> derivative,
    "chordScalar" -> chord,
    "speedIdentityResidual" -> speedResidual,
    "decompositionResidual" -> decompositionResidual,
    "minimumQFirstDifference" -> Min[firstDiffs],
    "maximumQSecondDifference" -> Max[secondDiffs]
  |>
];

round17Compact[rec_Association] := Map[N[#, 24] &, rec];

round17SampleA = N[
  {
    round16DoubleWallA + 10^-6,
    6, 8, 12, 30, 100, 1000, 100000
  },
  55
];
round17Records = round17ActionRecord /@ round17SampleA;
round17MinimumDerivative = First@MinimalBy[
  round17Records,
  N[#1["derivative"], 30] &
];
round17MinimumChord = First@MinimalBy[
  round17Records,
  N[#1["chordScalar"], 30] &
];

Print["round17DiagnosticOnly=", round17DiagnosticOnly];
Print["round17ActionRecords=", Length[round17Records]];
Print[
  "round17MinimumDerivative=",
  round17Compact[round17MinimumDerivative] // InputForm
];
Print[
  "round17MinimumChordScalar=",
  round17Compact[round17MinimumChord] // InputForm
];
Print[
  "round17Records=",
  Map[round17Compact, round17Records] // InputForm
];

round17ReplayOK = And[
  Length[round17Records] == 8,
  AllTrue[round17Records, N[#1["KOverA"] - #1["speed"], 30] > 0 &],
  AllTrue[round17Records, N[#1["B"], 30] > 0 &],
  AllTrue[round17Records, N[#1["Qg"], 30] > 0 &],
  AllTrue[round17Records, N[#1["derivative"], 30] > 0 &],
  AllTrue[round17Records, N[#1["chordScalar"], 30] > 0 &],
  AllTrue[
    round17Records,
    Abs[N[#1["speedIdentityResidual"], 30]] < 10^-25 &
  ],
  AllTrue[
    round17Records,
    Abs[N[#1["decompositionResidual"], 30]] < 10^-25 &
  ],
  AllTrue[
    round17Records,
    N[#1["minimumQFirstDifference"], 30] > 0 &
  ],
  AllTrue[
    round17Records,
    N[#1["maximumQSecondDifference"], 30] < 0 &
  ]
];

Print["round17ReplayOK=", round17ReplayOK];

If[!TrueQ[round17ReplayOK], Exit[2]];
