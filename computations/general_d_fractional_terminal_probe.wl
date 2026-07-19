(*
  Diagnostic evaluator for the revised general-dimensional shell strategy.

  This file is theorem-design and falsification evidence only.  It does not
  use interval arithmetic and must not be cited as a proof.  Its purposes are
  to evaluate D_A, the exact no-drop identity (S4), and the old/new versions
  of the terminal inverse-action lower bound at high precision.
*)

ClearAll["Global`*"];

$MaxExtraPrecision = 4000;
wp = 70;
rootWp = 55;
wallTol = 10^-30;
SeedRandom[20260718, Method -> "MersenneTwister"];

(* Numerical wall ownership used only by this diagnostic.  Values resolved
   within wallTol of an integer are assigned by the literal strict/ordinary
   conventions before evaluating the corresponding branch. *)
strictFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, Max[0, m - 1], Ceiling[x] - 1]
];

ordinaryFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, m, Floor[x]]
];

ballAction[a_?NumericQ, z_?NumericQ] := If[
  z < a,
  (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi,
  0
];

ballTailIntegral[a_?NumericQ, x_?NumericQ] := If[
  x >= a,
  0,
  Module[{theta = ArcCos[x/a]},
    a^2/(4 Pi) (theta (1 + 2 Cos[theta]^2) - 3 Sin[theta] Cos[theta])
  ]
];

shellAction[k_?NumericQ, mu_?NumericQ, z_?NumericQ] :=
  ballAction[k, z] - ballAction[mu, z];

shellTailIntegral[k_?NumericQ, mu_?NumericQ, x_?NumericQ] :=
  ballTailIntegral[k, x] - ballTailIntegral[mu, x];

tailDefect[k_?NumericQ, mu_?NumericQ, x_?NumericQ] := Module[
  {jmax, endpoint, doubled},
  jmax = Ceiling[k - x] + 1;
  endpoint = strictFloor[shellAction[k, mu, x] + 1/4];
  doubled = Sum[
    strictFloor[shellAction[k, mu, x + j] + 1/4],
    {j, 1, jmax}
  ];
  2 shellTailIntegral[k, mu, x] - endpoint - 2 doubled
];

ballAngle[k_?NumericQ, level_?NumericQ] := Module[
  {theta, guess, localWp},
  localWp = Min[rootWp, Max[35, Floor[Precision[k]] - 8]];
  guess = (3 Pi level/k)^(1/3);
  theta /. FindRoot[
    k/Pi (Sin[theta] - theta Cos[theta]) == level,
    {theta, guess},
    WorkingPrecision -> localWp,
    AccuracyGoal -> Min[30, localWp - 10],
    PrecisionGoal -> Min[30, localWp - 10]
  ]
];

strictFraction[y_?NumericQ] := y - strictFloor[y];

terminalData[k_?NumericQ, mu_?NumericQ, q_?NumericQ] := Module[
  {v, h, aq, b, qq, beta, delta, levels, angles, ys, etas,
   top, ballLower, exactBall, oldRaw, newRaw, exact, t3Slack},
  v = ballAction[k, q];
  h = ballAction[mu, q];
  aq = v - h;
  b = strictFloor[v + 1/4];
  qq = strictFloor[aq + 1/4];
  beta = ArcCos[q/k]/Pi;
  delta = ballTailIntegral[mu, q];
  levels = Table[j - 1/4, {j, 1, b}];
  angles = ballAngle[k, #] & /@ levels;
  ys = k Cos[#] - q & /@ angles;
  etas = strictFraction /@ ys;
  top = Max[v - b, 0]^2/beta;
  ballLower = Pi/2 Total[1/angles] - b + 2 Total[etas] + top;
  exactBall = tailDefect[k, 0, q];
  oldRaw = Pi/2 Total[1/angles] - qq - 2 delta + top;
  newRaw = oldRaw + 2 Total[etas];
  exact = tailDefect[k, mu, q];
  t3Slack = (mu - q) h - 2 delta;
  <|
    "v" -> v, "h" -> h, "Aq" -> aq, "B" -> b, "Q" -> qq,
    "beta" -> beta, "delta" -> delta, "angles" -> angles,
    "etas" -> etas, "ballLower" -> ballLower, "exactBall" -> exactBall,
    "T1Slack" -> exactBall - ballLower,
    "oldRaw" -> oldRaw, "newRaw" -> newRaw,
    "newWithOneInterface" -> Max[0, newRaw], "exactDq" -> exact,
    "T2Slack" -> exact - newRaw, "T3Slack" -> t3Slack
  |>
];

(* Smallest dimension that needs this shift after the completed d=3 theorem
   is taken as the base case.  r=1/2 is retained as a d=3 comparison point. *)
extensionOwnerDimensionForShift[r_?NumericQ] := Which[
  Abs[r - Round[r]] < 10^-30, 4,
  r >= 3/2, 5,
  True, 3
];

dimensionActiveQ[rho_?NumericQ, k_?NumericQ, r_?NumericQ] := Module[
  {d = extensionOwnerDimensionForShift[r]},
  k^2 > Pi^2/(1 - rho)^2 + ((d - 2)^2 - 1)/4
];

firstFloorNoDropRecord[rho_?NumericQ, k_?NumericQ, r_?NumericQ] := Module[
  {mu, n, q, floors, aq, eps, rn, td, actual, s4, chi, residual,
   lambda, mn, round11R0, round11Lhat, round11Psi1},
  mu = rho k;
  If[!(r < mu), Return[Nothing]];
  n = Floor[mu - r];
  If[n < 1, Return[Nothing]];
  q = r + n;
  floors = Table[ordinaryFloor[shellAction[k, mu, r + j] + 1/4], {j, 0, n}];
  If[!AllTrue[floors, # == 1 &], Return[Nothing]];
  aq = shellAction[k, mu, q];
  eps = aq - 3/4;
  chi = If[Abs[eps] <= wallTol, 1, 0];
  rn = 2 (shellTailIntegral[k, mu, r] - shellTailIntegral[k, mu, q]) - 2 n;
  td = terminalData[k, mu, q];
  actual = tailDefect[k, mu, r];
  s4 = td["exactDq"] + rn + chi;
  residual = actual - s4;
  lambda = (k - mu)/Pi;
  mn = n + n^2/(3 (2 r + n));
  round11R0 = -n/2 + mn (2 n/(r + 2 n)) (lambda - 3/4);
  round11Lhat = If[
    td["B"] == 1,
    Pi/(2 First[td["angles"]]) + 2 First[td["etas"]] - td["Q"]
      - (mu - q) td["h"] + Max[td["v"] - 1, 0]^2/td["beta"],
    Missing["NotB1"]
  ];
  round11Psi1 = If[
    td["B"] == 1,
    Max[0, round11Lhat] + round11R0 + chi,
    Missing["NotB1"]
  ];
  <|
    "rho" -> rho, "K" -> k, "r" -> r,
    "dOwner" -> extensionOwnerDimensionForShift[r],
    "dimensionActive" -> dimensionActiveQ[rho, k, r],
    "n" -> n, "q" -> q, "eps" -> eps, "chi" -> chi,
    "B" -> td["B"], "lambda" -> lambda,
    "actualDr" -> actual, "s4Residual" -> residual,
    "Rn" -> rn, "exactDq" -> td["exactDq"],
    "oldScalar" -> td["oldRaw"] + rn + chi,
    "newScalarRaw" -> td["newRaw"] + rn + chi,
    "newScalar" -> td["newWithOneInterface"] + rn + chi,
    "etaSum" -> Total[td["etas"]],
    "T1Slack" -> td["T1Slack"], "T2Slack" -> td["T2Slack"],
    "T3Slack" -> td["T3Slack"], "round11R0" -> round11R0,
    "round11Lhat" -> round11Lhat, "round11Psi1" -> round11Psi1,
    "terminal" -> td
  |>
];

(* Randomized, high-precision theorem-design sweep near the spectral wall. *)
records = Reap[
  Do[
    Module[{rho, wall, multiplier, k, mu, rmax, shifts, rec},
      rho = RandomReal[{1/40, 39/40}, WorkingPrecision -> wp];
      wall = Pi/(1 - rho);
      multiplier = Exp[
        RandomReal[{Log[5001/5000], Log[7/2]}, WorkingPrecision -> wp]
      ];
      k = wall multiplier;
      mu = rho k;
      rmax = Floor[2 (mu - 1)]/2;
      If[rmax >= 1/2,
        shifts = Range[1/2, Min[rmax, 25], 1/2];
        Do[
          rec = firstFloorNoDropRecord[rho, k, r];
          If[AssociationQ[rec], Sow[rec]],
          {r, shifts}
        ]
      ]
    ],
    {sample, 1, 2400}
  ]
][[2]];

records = If[records === {}, {}, First[records]];
activeRecords = Select[records, TrueQ[#dimensionActive] &];

minRecord[data_List, key_String] := If[
  data === {},
  Missing["NoData"],
  First@MinimalBy[data, N[#[key], 30] &]
];

compact[Missing["NoData"]] := Missing["NoData"];
compact[rec_Association] := KeyTake[
  Map[N[#, 24] &, rec],
  {"rho", "K", "r", "dOwner", "n", "q", "eps", "chi", "B", "lambda", "actualDr",
   "Rn", "exactDq", "oldScalar", "newScalarRaw", "newScalar", "etaSum",
   "T1Slack", "T2Slack", "T3Slack", "round11R0", "round11Lhat",
   "round11Psi1", "s4Residual"}
];

Print["WolframVersion=", $Version];
Print["diagnosticOnly=True"];
Print["records=", Length[records], "; dimensionActiveRecords=", Length[activeRecords]];
Print["minActual=", compact[minRecord[activeRecords, "actualDr"]] // InputForm];
Print["minOldScalar=", compact[minRecord[activeRecords, "oldScalar"]] // InputForm];
Print["minNewScalarRaw=", compact[minRecord[activeRecords, "newScalarRaw"]] // InputForm];
Print["minNewScalar=", compact[minRecord[activeRecords, "newScalar"]] // InputForm];
Print["minT1Slack=", compact[minRecord[activeRecords, "T1Slack"]] // InputForm];
Print["minT2Slack=", compact[minRecord[activeRecords, "T2Slack"]] // InputForm];
Print["minT3Slack=", compact[minRecord[activeRecords, "T3Slack"]] // InputForm];
Print[
  "negativeSlackCounts=", <|
    "T1" -> Count[activeRecords, rec_ /; N[rec["T1Slack"], 40] < -10^-35],
    "T2" -> Count[activeRecords, rec_ /; N[rec["T2Slack"], 40] < -10^-35],
    "T3" -> Count[activeRecords, rec_ /; N[rec["T3Slack"], 40] < -10^-35]
  |> // InputForm
];

Do[
  subset = Select[activeRecords, #B == bclass &];
  Print[
    "B=", bclass, "; count=", Length[subset],
    "; minNewScalar=", compact[minRecord[subset, "newScalar"]] // InputForm
  ],
  {bclass, 0, 3}
];

subset = Select[activeRecords, #B >= 4 &];
Print[
  "B>=4; count=", Length[subset],
  "; minNewScalar=", compact[minRecord[subset, "newScalar"]] // InputForm
];

maxS4Residual = If[
  activeRecords === {},
  Missing["NoData"],
  Max[Abs[N[#s4Residual, 40]] & /@ activeRecords]
];
Print["maxAbsS4Residual=", maxS4Residual // InputForm];

extensionB1Records = Select[
  activeRecords,
  #B == 1 && #dOwner >= 4 &
];
extensionHardB1Records = Select[extensionB1Records, 0 <= #eps < 1/4 &];
Print[
  "round11ExtensionB1Count=", Length[extensionB1Records],
  "; hardCount=", Length[extensionHardB1Records],
  "; minRound11Psi1=",
  compact[minRecord[extensionB1Records, "round11Psi1"]] // InputForm,
  "; minHardRound11Psi1=",
  compact[minRecord[extensionHardB1Records, "round11Psi1"]] // InputForm
];

fixedProbes = {
  {N[227/500, wp], N[2877/500, wp], N[1/2, wp]},
  {
    N[47978754634158649050590383922099135816/10^38, wp],
    N[635436263679497503886750564561225473881/10^38, wp],
    N[1, wp]
  },
  {
    N[60568015903591743143152825723518617451/10^38, wp],
    N[802076012509844460396379872690886259079/10^38, wp],
    N[1, wp]
  }
};

Do[
  fixedRecord = firstFloorNoDropRecord @@ probe;
  Print[
    "fixedProbe=", N[probe, 24] // InputForm,
    "; record=", If[AssociationQ[fixedRecord], compact[fixedRecord], fixedRecord] // InputForm
  ],
  {probe, fixedProbes}
];

(* A known off-active example showing why the completed one-interface
   maximum max(0,T2) must be retained when T2's raw expression is negative. *)
offActiveTerminal = terminalData[N[232/99, wp], N[58/25, wp], N[3/2, wp]];
Print[
  "offActiveRawT2=", N[offActiveTerminal["newRaw"], 24] // InputForm,
  "; offActiveExactDq=", N[offActiveTerminal["exactDq"], 24] // InputForm
];

(* The B=0 corner is codimension one and is almost surely missed by a
   random sweep.  Evaluate deterministic high-precision half-grid interface
   starts q=mu.  This remains a diagnostic, not an exact or interval proof. *)
cornerRecords = Reap[
  Do[
    Module[{q, kval, theta, guess, rho, nmax, r, rec},
      q = N[q2/2, wp];
      guess = Min[6/5, Max[1/20, (9 Pi/(4 q))^(1/3)]];
      theta = th /. FindRoot[
        3 Pi Cos[th]/(4 (Sin[th] - th Cos[th])) == q,
        {th, guess}, WorkingPrecision -> rootWp,
        AccuracyGoal -> 38, PrecisionGoal -> 38
      ];
      kval = 3 Pi/(4 (Sin[theta] - theta Cos[theta]));
      rho = q/kval;
      nmax = Floor[q - 1/2];
      Do[
        r = q - n;
        rec = firstFloorNoDropRecord[rho, kval, r];
        If[AssociationQ[rec] && TrueQ[rec["B"] == 0] && TrueQ[rec["dimensionActive"]],
          Sow[Append[rec, "cornerCrude" -> 9/(16 (ArcCos[rho]/Pi)) + 1 - n/2]]
        ],
        {n, 1, nmax}
      ]
    ],
    {q2, 3, 160}
  ]
][[2]];

cornerRecords = If[cornerRecords === {}, {}, First[cornerRecords]];
Print[
  "B0GridCount=", Length[cornerRecords],
  "; B0MaxN=", If[cornerRecords === {}, Missing["NoData"], Max[#n & /@ cornerRecords]],
  "; B0MinActual=", compact[minRecord[cornerRecords, "actualDr"]] // InputForm,
  "; B0MinNewScalar=", compact[minRecord[cornerRecords, "newScalar"]] // InputForm,
  "; B0MinCrude=", If[
    cornerRecords === {}, Missing["NoData"],
    N[(First@MinimalBy[cornerRecords, N[#cornerCrude, 30] &])["cornerCrude"], 24]
  ] // InputForm
];
