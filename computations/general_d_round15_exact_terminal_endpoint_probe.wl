(*
  Diagnostic evaluator for the exact-terminal endpoint scalar in Round 15.

  Round 14 retains the exact no-drop head and inner cap but still uses the
  tangent lower bound for the outer B=1 ball tail.  This script restores that
  last term exactly.  It is high-precision theorem-design evidence only: it
  is not interval arithmetic and does not prove the endpoint sign.
*)

round14Probe = FileNameJoin[{
  DirectoryName[$InputFileName],
  "general_d_round14_exact_head_endpoint_probe.wl"
}];
Get[round14Probe];

round15DiagnosticOnly = True;

ClearAll[
  exactOuterTerminalAt, exactFullScalarAt, exactFullEndpointRecord,
  fullPhaseEndpoint, endpointOwner, round15Compact
];

fullPhaseEndpoint[rec_Association] := Module[
  {aa, k, q, gap},
  k = rec["K"];
  q = rec["q"];
  gap = rec["terminal"]["v"] - 3/4;
  aa /. FindRoot[
    ballAction[q + aa, q] == gap,
    {aa, 0, k - q},
    Method -> "Brent",
    WorkingPrecision -> 50,
    AccuracyGoal -> 35,
    PrecisionGoal -> 35
  ]
];

exactOuterTerminalAt[rec_Association, aa_?NumericQ] := Module[
  {k, q, y, mu},
  k = rec["K"];
  q = rec["q"];
  y = k Cos[First[rec["terminal"]["angles"]]] - q;
  mu = q + aa;
  2 ballTailIntegral[k, q]
    - 2 ballTailIntegral[mu, q]
    - 1
    - 2 strictFloor[y]
];

exactFullScalarAt[rec_Association, aa_?NumericQ] :=
  exactOuterTerminalAt[rec, aa] + exactHeadAt[rec, aa];

endpointOwner[rec_Association] := Module[
  {phase, activity, endpoint, tol = 10^-20},
  phase = phaseEndpoint[rec];
  activity = activityEndpoint[rec];
  endpoint = endpointAlpha[rec];
  Which[
    Abs[endpoint - activity] < tol && activity < phase - tol, "activity",
    Abs[endpoint - 1] < tol && 1 < activity - tol, "branch",
    True, "phase"
  ]
];

exactFullEndpointRecord[rec_Association] := Module[
  {aa, aaPhase, xi, omega, y},
  aa = endpointAlpha[rec];
  aaPhase = fullPhaseEndpoint[rec];
  xi = exactEndpointScalarAt[rec, aa];
  omega = exactFullScalarAt[rec, aa];
  y = rec["K"] Cos[First[rec["terminal"]["angles"]]] - rec["q"];
  <|
    "rho" -> rec["rho"],
    "K" -> rec["K"],
    "r" -> rec["r"],
    "dOwner" -> rec["dOwner"],
    "n" -> rec["n"],
    "q" -> rec["q"],
    "y" -> y,
    "M" -> strictFloor[y],
    "eta" -> First[rec["terminal"]["etas"]],
    "alphaOriginal" -> rec["rho"] rec["K"] - rec["q"],
    "alphaEndpoint" -> aa,
    "alphaFullPhase" -> aaPhase,
    "endpointOwner" -> endpointOwner[rec],
    "round14XiEndpoint" -> xi,
    "exactOuterTangentGap" -> omega - xi,
    "exactFullEndpoint" -> omega,
    "floorFreeEndpoint" -> omega - 2 First[rec["terminal"]["etas"]],
    "exactFullPhaseEndpoint" -> exactFullScalarAt[rec, aaPhase]
  |>
];

round15Compact[rec_Association] := Map[N[#, 24] &, rec];

round15EndpointRecords = exactFullEndpointRecord /@ hardExtensionRecords;
round15MinimumRecord = First@MinimalBy[
  round15EndpointRecords,
  N[#1["exactFullEndpoint"], 30] &
];
round15NegativeCount = Count[
  round15EndpointRecords,
  rec_ /; N[rec["exactFullEndpoint"], 35] < 0
];
round15NegativeGapCount = Count[
  round15EndpointRecords,
  rec_ /; N[rec["exactOuterTangentGap"], 35] < 0
];
round15NegativeFullPhaseCount = Count[
  round15EndpointRecords,
  rec_ /; N[rec["exactFullPhaseEndpoint"], 35] < 0
];
round15MinimumFullPhaseRecord = First@MinimalBy[
  round15EndpointRecords,
  N[#1["exactFullPhaseEndpoint"], 30] &
];
round15MinimumFloorFreeRecord = First@MinimalBy[
  round15EndpointRecords,
  N[#1["floorFreeEndpoint"], 30] &
];
round15OwnerCounts = Counts[round15EndpointRecords[[All, "endpointOwner"]]];
round15OwnerMinima = AssociationMap[
  Function[owner,
    First@MinimalBy[
      Select[round15EndpointRecords, #1["endpointOwner"] == owner &],
      N[#1["exactFullEndpoint"], 30] &
    ]
  ],
  Keys[round15OwnerCounts]
];
round15SmallestRecords = Take[
  SortBy[round15EndpointRecords, N[#1["exactFullEndpoint"], 30] &],
  UpTo[12]
];

round15Round13Endpoint = exactFullScalarAt[
  round13Record,
  round13Endpoint
];

Print["round15DiagnosticOnly=", round15DiagnosticOnly];
Print["round15HardExtensionRecords=", Length[round15EndpointRecords]];
Print["round15NegativeEndpointCount=", round15NegativeCount];
Print["round15NegativeTangentGapCount=", round15NegativeGapCount];
Print["round15NegativeFullPhaseCount=", round15NegativeFullPhaseCount];
Print["round15OwnerCounts=", round15OwnerCounts // InputForm];
Print[
  "round15MinimumEndpoint=",
  round15Compact[round15MinimumRecord] // InputForm
];
Print[
  "round15MinimumFullPhaseEndpoint=",
  round15Compact[round15MinimumFullPhaseRecord] // InputForm
];
Print[
  "round15MinimumFloorFreeEndpoint=",
  round15Compact[round15MinimumFloorFreeRecord] // InputForm
];
Print[
  "round15OwnerMinima=",
  Map[round15Compact, round15OwnerMinima] // InputForm
];
Print[
  "round15SmallestEndpoints=",
  Map[round15Compact, round15SmallestRecords] // InputForm
];
Print[
  "round15Round13ExactEndpoint=",
  N[round15Round13Endpoint, 30] // InputForm
];

round15ReplayOK = And[
  Length[round15EndpointRecords] == 3171,
  round15NegativeCount == 0,
  round15NegativeGapCount == 0,
  round15NegativeFullPhaseCount == 16,
  N[round15MinimumFullPhaseRecord["exactFullPhaseEndpoint"], 30] < -2/5,
  N[round15MinimumRecord["exactFullEndpoint"], 30] > 1/2,
  N[round15MinimumFloorFreeRecord["floorFreeEndpoint"], 30] > 1/3,
  N[round15Round13Endpoint, 30] > 45
];

Print["round15ReplayOK=", round15ReplayOK];

If[!TrueQ[round15ReplayOK], Exit[2]];
