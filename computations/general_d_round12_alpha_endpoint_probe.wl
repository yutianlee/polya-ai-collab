(*
  Round 12 alpha-endpoint diagnostic for the revised general-dimensional
  shell strategy.

  This file is theorem-design and falsification evidence only.  It imports
  the deterministic high-precision Round 10/11 record generator, restricts
  to the hard B=1 extension-grid records, and moves the explicit Round 11
  scalar to the first phase, branch, or owner-dimensional activity endpoint.
  It is not an interval calculation and is not a proof premise.
*)

baseProbe = FileNameJoin[{
  DirectoryName[$InputFileName],
  "general_d_fractional_terminal_probe.wl"
}];
Get[baseProbe];

diagnosticOnly = True;

ClearAll[
  phaseEndpoint, activityEndpoint, endpointAlpha, openScalarAt,
  endpointRecord, endpointCompact
];

phaseEndpoint[rec_Association] := Module[
  {k, q, v, levelGap, h1, alpha0, aa},
  k = rec["K"];
  q = rec["q"];
  v = rec["terminal"]["v"];
  levelGap = v - 3/4;
  h1 = ballAction[q + 1, q];
  If[
    h1 < levelGap,
    1,
    alpha0 = rec["rho"] k - q;
    aa /. FindRoot[
      ballAction[q + aa, q] == levelGap,
      {aa, alpha0, 1},
      Method -> "Brent",
      WorkingPrecision -> 50,
      AccuracyGoal -> 35,
      PrecisionGoal -> 35
    ]
  ]
];

activityEndpoint[rec_Association] := Module[
  {k, q, dOwner, kappa},
  k = rec["K"];
  q = rec["q"];
  dOwner = rec["dOwner"];
  kappa = ((dOwner - 2)^2 - 1)/4;
  k - q - Pi k/Sqrt[k^2 - kappa]
];

endpointAlpha[rec_Association] := Min[
  phaseEndpoint[rec],
  activityEndpoint[rec]
];

openScalarAt[rec_Association, aa_?NumericQ] := Module[
  {k, q, r, n, td, hh, lambda, mn, remainder0, lhat},
  k = rec["K"];
  q = rec["q"];
  r = rec["r"];
  n = rec["n"];
  td = rec["terminal"];
  hh = ballAction[q + aa, q];
  lambda = (k - q - aa)/Pi;
  mn = n + n^2/(3 (2 r + n));
  remainder0 = -n/2
    + mn (2 n/(r + 2 n)) (lambda - 3/4);
  lhat = Pi/(2 First[td["angles"]])
    + 2 First[td["etas"]]
    - 1
    - aa hh
    + Max[td["v"] - 1, 0]^2/td["beta"];
  Max[0, lhat] + remainder0
];

endpointRecord[rec_Association] := Module[
  {phase, activity, endpoint},
  phase = phaseEndpoint[rec];
  activity = activityEndpoint[rec];
  endpoint = Min[phase, activity];
  <|
    "rho" -> rec["rho"],
    "K" -> rec["K"],
    "r" -> rec["r"],
    "dOwner" -> rec["dOwner"],
    "n" -> rec["n"],
    "q" -> rec["q"],
    "eps" -> rec["eps"],
    "B" -> rec["B"],
    "alphaOriginal" -> rec["rho"] rec["K"] - rec["q"],
    "alphaStarOrOne" -> phase,
    "alphaAct" -> activity,
    "alphaEndpoint" -> endpoint,
    "endpointScalar" -> openScalarAt[rec, endpoint],
    "phaseOnlyScalar" -> openScalarAt[rec, phase]
  |>
];

endpointCompact[rec_Association] := Map[N[#, 24] &, rec];

hardExtensionRecords = Select[
  activeRecords,
  #1["B"] == 1
    && #1["dOwner"] >= 4
    && 0 < #1["eps"] < 1/4 &
];

endpointRecords = endpointRecord /@ hardExtensionRecords;
minimumEndpointRecord = First@MinimalBy[
  endpointRecords,
  N[#1["endpointScalar"], 30] &
];
minimumPhaseOnlyRecord = First@MinimalBy[
  endpointRecords,
  N[#1["phaseOnlyScalar"], 30] &
];

negativeEndpointCount = Count[
  endpointRecords,
  rec_ /; N[rec["endpointScalar"], 35] < 0
];

Print["round12DiagnosticOnly=", diagnosticOnly];
Print["round12HardExtensionRecords=", Length[hardExtensionRecords]];
Print["round12NegativeEndpointCount=", negativeEndpointCount];
Print[
  "round12MinimumEndpoint=",
  endpointCompact[minimumEndpointRecord] // InputForm
];
Print[
  "round12MinimumPhaseOnly=",
  endpointCompact[minimumPhaseOnlyRecord] // InputForm
];

expectedCount = 3171;
expectedMinimum = N[0.03954098598463273226158050782375868317, 35];
replayOK = And[
  Length[hardExtensionRecords] == expectedCount,
  negativeEndpointCount == 0,
  Abs[
    N[minimumEndpointRecord["endpointScalar"], 35] - expectedMinimum
  ] < 10^-28
];

Print["round12ReplayOK=", replayOK];

If[!TrueQ[replayOK], Exit[2]];
