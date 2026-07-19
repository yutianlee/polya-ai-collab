(*
  Diagnostic evaluator for the Round 14 exact-head endpoint scalar.

  This imports the Round 10--12 high-precision record generator, moves each
  hard B=1 extension-grid record to the Round 12 endpoint, and evaluates the
  Round 14 scalar with the exact cap and exact no-drop head.  It also replays
  the large-q counterexample to the rejected Round 11--12 surrogate.

  This is floating-point theorem-design evidence only.  It is not an
  interval calculation and is not a proof premise.
*)

round12Probe = FileNameJoin[{
  DirectoryName[$InputFileName],
  "general_d_round12_alpha_endpoint_probe.wl"
}];
Get[round12Probe];

round14DiagnosticOnly = True;

ClearAll[
  exactOpenTerminalAt, exactHeadAt, exactEndpointScalarAt,
  exactEndpointRecord, round14Compact
];

exactOpenTerminalAt[rec_Association, aa_?NumericQ] := Module[
  {k, q, td, delta, top},
  k = rec["K"];
  q = rec["q"];
  td = rec["terminal"];
  delta = ballTailIntegral[q + aa, q];
  top = Max[td["v"] - 1, 0]^2/td["beta"];
  Pi/(2 First[td["angles"]])
    + 2 First[td["etas"]]
    - 1
    - 2 delta
    + top
];

exactHeadAt[rec_Association, aa_?NumericQ] := Module[
  {k, q, r, n, mu},
  k = rec["K"];
  q = rec["q"];
  r = rec["r"];
  n = rec["n"];
  mu = q + aa;
  2 (shellTailIntegral[k, mu, r] - shellTailIntegral[k, mu, q]) - 2 n
];

exactEndpointScalarAt[rec_Association, aa_?NumericQ] :=
  exactOpenTerminalAt[rec, aa] + exactHeadAt[rec, aa];

exactEndpointRecord[rec_Association] := Module[
  {aa, terminal, head},
  aa = endpointAlpha[rec];
  terminal = exactOpenTerminalAt[rec, aa];
  head = exactHeadAt[rec, aa];
  <|
    "rho" -> rec["rho"],
    "K" -> rec["K"],
    "r" -> rec["r"],
    "dOwner" -> rec["dOwner"],
    "n" -> rec["n"],
    "q" -> rec["q"],
    "epsOriginal" -> rec["eps"],
    "alphaOriginal" -> rec["rho"] rec["K"] - rec["q"],
    "alphaEndpoint" -> aa,
    "exactTerminalEndpoint" -> terminal,
    "exactHeadEndpoint" -> head,
    "exactEndpointScalar" -> terminal + head
  |>
];

round14Compact[rec_Association] := Map[N[#, 24] &, rec];

round14EndpointRecords = exactEndpointRecord /@ hardExtensionRecords;
round14MinimumRecord = First@MinimalBy[
  round14EndpointRecords,
  N[#1["exactEndpointScalar"], 30] &
];
round14NegativeCount = Count[
  round14EndpointRecords,
  rec_ /; N[rec["exactEndpointScalar"], 35] < 0
];

(* Exact-parameter construction from the Round 13 falsification note. *)
round13Theta = N[531/4000, wp];
round13K = 3 Pi/(4 (Sin[round13Theta] - round13Theta Cos[round13Theta]));
round13R = N[2949, wp];
round13Q = N[3000, wp];
round13N = 51;
round13Alpha = N[999/1000, wp];
round13Mu = round13Q + round13Alpha;
round13Rho = round13Mu/round13K;
round13Record = firstFloorNoDropRecord[round13Rho, round13K, round13R];
round13Endpoint = endpointAlpha[round13Record];
round13Floors = Table[
  ordinaryFloor[
    shellAction[round13K, round13Mu, round13R + j] + 1/4
  ],
  {j, 0, round13N}
];

round13Replay = <|
  "theta" -> round13Theta,
  "K" -> round13K,
  "rho" -> round13Rho,
  "r" -> round13R,
  "n" -> round13N,
  "q" -> round13Q,
  "alphaOriginal" -> round13Alpha,
  "alphaEndpoint" -> round13Endpoint,
  "allFirstFloor" -> AllTrue[round13Floors, # == 1 &],
  "round11OriginalScalar" -> round13Record["round11Psi1"],
  "round12EndpointScalar" -> openScalarAt[round13Record, round13Endpoint],
  "exactDefect" -> round13Record["actualDr"],
  "s4Residual" -> round13Record["s4Residual"],
  "round14OriginalScalar" -> exactEndpointScalarAt[round13Record, round13Alpha],
  "round14EndpointScalar" -> exactEndpointScalarAt[round13Record, round13Endpoint]
|>;

Print["round14DiagnosticOnly=", round14DiagnosticOnly];
Print["round14HardExtensionRecords=", Length[hardExtensionRecords]];
Print["round14NegativeEndpointCount=", round14NegativeCount];
Print[
  "round14MinimumEndpoint=",
  round14Compact[round14MinimumRecord] // InputForm
];
Print["round13Replay=", round14Compact[round13Replay] // InputForm];

round14ReplayOK = And[
  Length[hardExtensionRecords] == 3171,
  round14NegativeCount == 0,
  TrueQ[round13Replay["allFirstFloor"]],
  N[round13Replay["round12EndpointScalar"], 30] < -1,
  N[round13Replay["exactDefect"], 30] > 45,
  Abs[N[round13Replay["s4Residual"], 30]] < 10^-25,
  N[round13Replay["round14EndpointScalar"], 30] > 41
];

Print["round14ReplayOK=", round14ReplayOK];

If[!TrueQ[round14ReplayOK], Exit[2]];
