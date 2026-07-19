(*
  Round 20 diagnostic evaluator for the sole high-floor first-drop CST
  obligation in the revised general-dimensional strategy.

  This is theorem-design and falsification evidence only.  It uses
  high-precision floating arithmetic, not interval arithmetic, and must not
  be cited as a proof of either the exact reduced scalar or Phi_delta.

  It evaluates active f >= 2, p < n records on the weakest integer (d = 4)
  and half-integer (d = 5) owner grids.  The script keeps the exact coupled
  shell/terminal variables and separately reports

    exactS   = D_A(q) + R_p + d_rho (n-p)/2,
    PhiDelta = the Round-10 lower surrogate (2.3).

  Literal strict and ordinary walls are owned separately.  In particular,
  n = floor(mu-r) uses the wall-aware ordinary floor, while terminal action
  counts and inverse fractions use the strict convention.
*)

ClearAll["Global`*"];

$MaxExtraPrecision = 5000;
wp = 70;
rootWp = 60;
wallTol = 10^-35;
signTol = 10^-28;
SeedRandom[20260719, Method -> "MersenneTwister"];

strictFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, Max[0, m - 1], Max[0, Ceiling[x] - 1]]
];
ordinaryFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, Max[0, m], Max[0, Floor[x]]]
];
strictFraction[x_?NumericQ] := x - strictFloor[x];

ballAction[a_?NumericQ, z_?NumericQ] := If[
  z < a,
  (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi,
  0
];
ballTailIntegral[a_?NumericQ, z_?NumericQ] := If[
  z >= a,
  0,
  Module[{theta = ArcCos[z/a]},
    a^2/(4 Pi) (theta (1 + 2 Cos[theta]^2) - 3 Sin[theta] Cos[theta])
  ]
];
shellAction[k_?NumericQ, mu_?NumericQ, z_?NumericQ] :=
  ballAction[k, z] - ballAction[mu, z];
shellTailIntegral[k_?NumericQ, mu_?NumericQ, z_?NumericQ] :=
  ballTailIntegral[k, z] - ballTailIntegral[mu, z];

tailDefect[k_?NumericQ, mu_?NumericQ, x_?NumericQ] := Module[
  {jmax, endpoint, doubled},
  jmax = Max[0, Ceiling[k - x] + 1];
  endpoint = strictFloor[shellAction[k, mu, x] + 1/4];
  doubled = Sum[
    strictFloor[shellAction[k, mu, x + j] + 1/4],
    {j, 1, jmax}
  ];
  2 shellTailIntegral[k, mu, x] - endpoint - 2 doubled
];

ballAngle[k_?NumericQ, level_?NumericQ] := Module[
  {theta, guess},
  guess = Min[3/2, Max[10^-8, (3 Pi level/k)^(1/3)]];
  theta /. FindRoot[
    k/Pi (Sin[theta] - theta Cos[theta]) == level,
    {theta, guess}, WorkingPrecision -> rootWp,
    AccuracyGoal -> 42, PrecisionGoal -> 42
  ]
];

terminalData[k_?NumericQ, mu_?NumericQ, q_?NumericQ] := Module[
  {v, h, aq, b, qq, beta, delta, levels, angles, ys, etas, top, lt},
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
  lt = Pi/2 Total[1/angles] + 2 Total[etas] - qq - 2 delta + top;
  <|
    "v" -> v, "h" -> h, "Aq" -> aq, "B" -> b, "Q" -> qq,
    "beta" -> beta, "delta" -> delta, "alpha" -> mu - q,
    "angles" -> angles, "ys" -> ys, "etas" -> etas,
    "etaSum" -> Total[etas], "top" -> top, "LT" -> lt
  |>
];

ownerDimension[r_?NumericQ] := If[Abs[r - Round[r]] <= wallTol, 4, 5];
dimensionActiveQ[rho_?NumericQ, k_?NumericQ, r_?NumericQ] := Module[
  {d = ownerDimension[r]},
  k^2 > Pi^2/(1 - rho)^2 + ((d - 2)^2 - 1)/4
];

firstDropRecord[rho_?NumericQ, k_?NumericQ, r_?NumericQ] := Module[
  {mu, n, q, actions, floors, f, p, eps0, epsp, rp, cp, cpLower,
   dRho, td, dq, dr, exactS, exactS2, phi, phiMax, phiCap,
   reductionSlack, terminalLoss, terminalMaxLoss, shelfLoss, ledgerResidual},
  mu = rho k;
  If[!dimensionActiveQ[rho, k, r] || !(r < mu), Return[Nothing]];
  n = ordinaryFloor[mu - r];
  If[n < 1, Return[Nothing]];
  q = r + n;
  actions = Table[shellAction[k, mu, r + j] + 1/4, {j, 0, n}];
  floors = ordinaryFloor /@ actions;
  f = First[floors];
  If[f < 2, Return[Nothing]];
  p = LengthWhile[floors, # == f &] - 1;
  If[p >= n, Return[Nothing]];
  eps0 = First[actions] - f;
  epsp = actions[[p + 1]] - f;
  rp = 2 (shellTailIntegral[k, mu, r] - shellTailIntegral[k, mu, r + p]) - 2 p f;
  cp = 2 (shellTailIntegral[k, mu, r] - shellTailIntegral[k, mu, r + p])
    - p (shellAction[k, mu, r] + shellAction[k, mu, r + p]);
  cpLower = p^2/(3 (2 r + p)) (eps0 - epsp);
  dRho = 2 ArcSin[rho]/Pi;
  td = terminalData[k, mu, q];
  dq = tailDefect[k, mu, q];
  dr = tailDefect[k, mu, r];
  exactS = dq + rp + dRho/2 (n - p);
  exactS2 = dq + cp + p (eps0 + epsp - 1/2) + dRho/2 (n - p);
  phi = td["LT"] + cpLower + p (eps0 + epsp - 1/2) + dRho/2 (n - p);
  phiMax = Max[0, td["LT"]] + cpLower + p (eps0 + epsp - 1/2) + dRho/2 (n - p);
  phiCap = phi - (td["alpha"] td["h"] - 2 td["delta"]);
  reductionSlack = dr - exactS;
  terminalLoss = dq - td["LT"];
  terminalMaxLoss = dq - Max[0, td["LT"]];
  shelfLoss = cp - cpLower;
  ledgerResidual = exactS - phi - terminalLoss - shelfLoss;
  <|
    "rho" -> rho, "K" -> k, "mu" -> mu, "r" -> r,
    "dOwner" -> ownerDimension[r], "n" -> n, "q" -> q,
    "f" -> f, "p" -> p, "floors" -> floors,
    "eps0" -> eps0, "epsp" -> epsp, "dRho" -> dRho,
    "D_r" -> dr, "D_q" -> dq, "R_p" -> rp,
    "C_p" -> cp, "C_pLower" -> cpLower,
    "exactS" -> exactS, "exactS2" -> exactS2,
    "PhiDelta" -> phi, "PhiMax" -> phiMax, "PhiCap" -> phiCap,
    "reductionSlack" -> reductionSlack,
    "terminalLoss" -> terminalLoss, "terminalMaxLoss" -> terminalMaxLoss,
    "shelfLoss" -> shelfLoss, "ledgerResidual" -> ledgerResidual,
    "terminal" -> td
  |>
];

compact[Missing[__]] := Missing["NoData"];
compact[rec_Association] := Module[{td = rec["terminal"]},
  Map[N[#, 22] &,
    Join[
      KeyTake[rec, {"rho", "K", "mu", "r", "dOwner", "n", "q", "f", "p",
        "eps0", "epsp", "D_r", "D_q", "R_p", "C_p", "C_pLower",
        "exactS", "PhiDelta", "PhiMax", "PhiCap", "reductionSlack",
        "terminalLoss", "terminalMaxLoss", "shelfLoss", "ledgerResidual"}],
      KeyTake[rec, {"faceAlpha", "faceEta"}],
      <|"B" -> td["B"], "Q" -> td["Q"], "v" -> td["v"],
        "h" -> td["h"], "alpha" -> td["alpha"], "etaSum" -> td["etaSum"],
        "top" -> td["top"], "LT" -> td["LT"]|>
    ]
  ]
];
minRecord[data_List, key_String] := If[data === {}, Missing["NoData"], First@MinimalBy[data, N[#[key], 30] &]];

randomRecords = Reap[
  Do[
    Module[{rho, dPick, wall, multiplier, k, mu, maxR, shifts, rec},
      rho = RandomReal[{1/50, 49/50}, WorkingPrecision -> wp];
      dPick = RandomChoice[{4, 5}];
      wall = Sqrt[
        Pi^2/(1 - rho)^2 + ((dPick - 2)^2 - 1)/4
      ];
      multiplier = Exp[
        RandomReal[{Log[10001/10000], Log[8]}, WorkingPrecision -> wp]
      ];
      k = wall multiplier;
      mu = rho k;
      maxR = Min[30, Floor[2 (mu - 1)]/2];
      If[maxR >= 1,
        shifts = If[dPick == 4, Range[1, Floor[maxR], 1], Range[3/2, maxR, 1]];
        Do[
          rec = firstDropRecord[rho, k, r];
          If[AssociationQ[rec], Sow[rec]],
          {r, shifts}
        ]
      ]
    ],
    {sample, 1, 600}
  ]
][[2]];
randomRecords = If[randomRecords === {}, {}, First[randomRecords]];

wallRecords = Reap[
  Do[
    Module[{rho = N[rhoRat, wp], z = N[r + p, wp], guess, kval, rec},
      guess = Max[(z + 1/5)/rho, Pi (f - 1/4)/(1 - rho) + z];
      kval = Quiet@Check[
        kk /. FindRoot[
          shellAction[kk, rho kk, z] == f - 1/4,
          {kk, guess, 21 guess/20}, WorkingPrecision -> rootWp,
          AccuracyGoal -> 42, PrecisionGoal -> 42
        ],
        Missing["RootFailure"]
      ];
      If[NumericQ[kval],
        rec = firstDropRecord[rho, kval, N[r, wp]];
        If[AssociationQ[rec] && rec["f"] == f && rec["p"] == p, Sow[rec]]
      ]
    ],
    {rhoRat, Range[3/20, 17/20, 1/40]},
    {r, Join[Range[1, 6, 1], Range[3/2, 13/2, 1]]},
    {p, 1, 4},
    {f, 2, 4}
  ]
][[2]];
wallRecords = If[wallRecords === {}, {}, First[wallRecords]];

interfaceShelfRecords = Reap[
  Do[
    Module[{z = N[r + p, wp], q = N[r + n, wp], guess, kval, rho, rec},
      guess = Max[q + 1, Pi (f - 1/4) + q];
      kval = Quiet@Check[
        kk /. FindRoot[
          ballAction[kk, z] - ballAction[q, z] == f - 1/4,
          {kk, guess, 21 guess/20}, WorkingPrecision -> rootWp,
          AccuracyGoal -> 42, PrecisionGoal -> 42
        ],
        Missing["RootFailure"]
      ];
      If[NumericQ[kval],
        rho = q/kval;
        rec = firstDropRecord[rho, kval, N[r, wp]];
        If[AssociationQ[rec] && rec["f"] == f && rec["p"] == p, Sow[rec]]
      ]
    ],
    {r, Join[Range[1, 8, 1], Range[3/2, 17/2, 1]]},
    {n, 1, 10},
    {p, 1, n - 1},
    {f, 2, 5}
  ]
][[2]];
interfaceShelfRecords = If[interfaceShelfRecords === {}, {}, First[interfaceShelfRecords]];

spatialPlusRecords = Reap[
  Do[
    Module[{q = N[r + n, wp], zc = N[r + n + m, wp], kval, rho, recWall,
      recPlus, crossCount, kplus},
      kval = Quiet@Check[
        kk /. FindRoot[
          ballAction[kk, zc] == klev - 1/4,
          {kk, zc + Pi (klev - 1/4) + 1, zc + Pi (klev - 1/4) + 2},
          WorkingPrecision -> rootWp, AccuracyGoal -> 42, PrecisionGoal -> 42
        ],
        Missing["RootFailure"]
      ];
      If[NumericQ[kval],
        kplus = kval (1 + 10^-20);
        Do[
          rho = (q + N[alphaRat, wp])/kval;
          recWall = firstDropRecord[rho, kval, N[r, wp]];
          recPlus = firstDropRecord[rho, kplus, N[r, wp]];
          If[AssociationQ[recWall] && AssociationQ[recPlus] &&
              recWall["f"] >= 2 && recWall["p"] < recWall["n"] &&
              recPlus["f"] == recWall["f"] && recPlus["p"] == recWall["p"],
            crossCount = Count[recWall["terminal"]["ys"], y_ /; Abs[y - Round[y]] <= 10^-28];
            If[crossCount >= 1,
              Sow[<|"wall" -> recWall, "plus" -> recPlus,
                "crossCount" -> crossCount,
                "SRightFormal" -> recWall["exactS"] - 2 crossCount,
                "PhiRightFormal" -> recWall["PhiDelta"] - 2 crossCount,
                "SRightReplayResidual" -> recPlus["exactS"] - (recWall["exactS"] - 2 crossCount),
                "PhiRightReplayResidual" -> recPlus["PhiDelta"] - (recWall["PhiDelta"] - 2 crossCount)|>]
            ]
          ],
          {alphaRat, Range[0, 4/5, 1/5]}
        ]
      ]
    ],
    {r, Join[Range[1, 8, 1], Range[3/2, 17/2, 1]]},
    {n, 1, 12},
    {klev, 1, 3},
    {m, 1, 4}
  ]
][[2]];
spatialPlusRecords = If[spatialPlusRecords === {}, {}, First[spatialPlusRecords]];
spatialPlusMinS = If[spatialPlusRecords === {}, Missing["NoData"],
  First@MinimalBy[spatialPlusRecords, N[#["plus"]["exactS"], 30] &]];
spatialPlusMinPhi = If[spatialPlusRecords === {}, Missing["NoData"],
  First@MinimalBy[spatialPlusRecords, N[#["plus"]["PhiDelta"], 30] &]];
spatialPlusCompact[x_Association] := <|
  "wall" -> compact[x["wall"]], "plus" -> compact[x["plus"]],
  "crossCount" -> x["crossCount"],
  "SRightFormal" -> N[x["SRightFormal"], 22],
  "PhiRightFormal" -> N[x["PhiRightFormal"], 22],
  "SRightReplayResidual" -> N[x["SRightReplayResidual"], 22],
  "PhiRightReplayResidual" -> N[x["PhiRightReplayResidual"], 22]
|>;

(* Targeted intrinsic-face scan: q = 5, r = 1, n = 4, and the first
   terminal crossing lies at displacement 2 + eta.  This parametrizes the
   open side of G_K(7) = 3/4 by eta > 0, while mu = 5 + alpha. *)
faceAlphaValues = N[Union[
  {10^-20, 10^-12, 10^-6, 1/10000, 1/100, 1/10, 1/5, 2/5},
  Range[3/100, 7/100, 1/1000]
], wp];
faceEtaValues = N[Union[
  {10^-20, 10^-12, 10^-6, 1/10000, 1/20, 1/10, 1/5, 2/5},
  Range[1/1000, 3/100, 1/1000]
], wp];
faceRecords = Reap[
  Do[
    Module[{eta = etaValue, kval, rho, rec},
      kval = kk /. FindRoot[
        ballAction[kk, N[7, wp] + eta] == 3/4,
        {kk, N[11.05, wp]}, WorkingPrecision -> rootWp,
        AccuracyGoal -> 42, PrecisionGoal -> 42
      ];
      Do[
        rho = (N[5, wp] + alphaValue)/kval;
        rec = firstDropRecord[rho, kval, N[1, wp]];
        If[AssociationQ[rec] && rec["n"] == 4 && rec["q"] == 5 &&
            rec["f"] == 2 && rec["p"] == 2,
          Sow[Join[rec, <|"faceAlpha" -> alphaValue, "faceEta" -> eta|>]]
        ],
        {alphaValue, faceAlphaValues}
      ]
    ],
    {etaValue, faceEtaValues}
  ]
][[2]];
faceRecords = If[faceRecords === {}, {}, First[faceRecords]];

(* A one-dimensional refinement along the observed eta -> 0+ edge. *)
edgeEta = N[10^-20, wp];
edgeK = kk /. FindRoot[
  ballAction[kk, N[7, wp] + edgeEta] == 3/4,
  {kk, N[11.05, wp]}, WorkingPrecision -> rootWp,
  AccuracyGoal -> 45, PrecisionGoal -> 45
];
edgeFaceRecords = Reap[
  Do[
    Module[{alpha = N[alphaRat, wp], rho, rec},
      rho = (N[5, wp] + alpha)/edgeK;
      rec = firstDropRecord[rho, edgeK, N[1, wp]];
      If[AssociationQ[rec] && rec["n"] == 4 && rec["q"] == 5 &&
          rec["f"] == 2 && rec["p"] == 2,
        Sow[Join[rec, <|"faceAlpha" -> alpha, "faceEta" -> edgeEta|>]]
      ]
    ],
    {alphaRat, Range[34/1000, 42/1000, 1/10000]}
  ]
][[2]];
edgeFaceRecords = If[edgeFaceRecords === {}, {}, First[edgeFaceRecords]];

(* Intersect the eta -> 0+ edge with the lower ordinary-floor wall at the
   end of the p = 2 shelf: A(3) + 1/4 = 2. *)
edgeShelfAlpha = aa /. FindRoot[
  shellAction[edgeK, N[5, wp] + aa, N[3, wp]] + 1/4 == 2,
  {aa, N[0.0384, wp]}, WorkingPrecision -> rootWp,
  AccuracyGoal -> 45, PrecisionGoal -> 45
];
edgeShelfRho = (N[5, wp] + edgeShelfAlpha)/edgeK;
edgeShelfRecord = firstDropRecord[edgeShelfRho, edgeK, N[1, wp]];
edgeShelfRecord = Join[
  edgeShelfRecord,
  <|"faceAlpha" -> edgeShelfAlpha, "faceEta" -> edgeEta|>
];

(* Literal codimension-two wall and a reproducible open-side record. *)
hardK0 = kk /. FindRoot[
  ballAction[kk, N[7, wp]] == 3/4,
  {kk, N[11.05, wp]}, WorkingPrecision -> rootWp,
  AccuracyGoal -> 45, PrecisionGoal -> 45
];
hardRho0 = N[5, wp]/hardK0;
hardWallRecord = firstDropRecord[hardRho0, hardK0, N[1, wp]];
hardOpenScale = N[10^-20, wp];
hardKOpen = kk /. FindRoot[
  ballAction[kk, N[7, wp] + hardOpenScale] == 3/4,
  {kk, hardK0}, WorkingPrecision -> rootWp,
  AccuracyGoal -> 45, PrecisionGoal -> 45
];
hardRhoOpen = (N[5, wp] + hardOpenScale)/hardKOpen;
hardOpenRecord = firstDropRecord[hardRhoOpen, hardKOpen, N[1, wp]];
hardRightReplay = <|
  "SRightLimitFromWall" -> hardWallRecord["exactS"] - 2,
  "PhiRightLimitFromWall" -> hardWallRecord["PhiDelta"] - 2,
  "SOpenMinusLimit" -> hardOpenRecord["exactS"] - (hardWallRecord["exactS"] - 2),
  "PhiOpenMinusLimit" -> hardOpenRecord["PhiDelta"] - (hardWallRecord["PhiDelta"] - 2)
|>;

spatialOpenRecords = #["plus"] & /@ spatialPlusRecords;
allRecords = Join[
  randomRecords, wallRecords, interfaceShelfRecords, spatialOpenRecords,
  faceRecords, edgeFaceRecords, {edgeShelfRecord, hardOpenRecord}
];
integerRecords = Select[allRecords, #["dOwner"] == 4 &];
halfIntegerRecords = Select[allRecords, #["dOwner"] == 5 &];
globalMinS = minRecord[allRecords, "exactS"];
globalMinPhi = minRecord[allRecords, "PhiDelta"];

safeMax[data_List] := If[data === {}, Missing["NoData"], Max[data]];
safeMin[data_List] := If[data === {}, Missing["NoData"], Min[data]];
identityResiduals = <|
  "exactSForms" -> safeMax[Abs[N[#["exactS"] - #["exactS2"], 45]] & /@ allRecords],
  "lossLedger" -> safeMax[Abs[N[#["ledgerResidual"], 45]] & /@ allRecords],
  "terminalCorrelation" -> safeMax[
    Abs[N[#["terminal"]["Aq"] - (#["terminal"]["v"] - #["terminal"]["h"]), 45]] & /@ allRecords
  ]
|>;
minimumProvedSlacks = <|
  "firstShelfReduction" -> safeMin[N[#["reductionSlack"], 40] & /@ allRecords],
  "terminalT2" -> safeMin[N[#["terminalLoss"], 40] & /@ allRecords],
  "shelfS3" -> safeMin[N[#["shelfLoss"], 40] & /@ allRecords]
|>;
negativeCounts = <|
  "exactS" -> Count[allRecords, x_ /; N[x["exactS"], 35] < -signTol],
  "PhiDelta" -> Count[allRecords, x_ /; N[x["PhiDelta"], 35] < -signTol],
  "PhiMax" -> Count[allRecords, x_ /; N[x["PhiMax"], 35] < -signTol],
  "PhiCap" -> Count[allRecords, x_ /; N[x["PhiCap"], 35] < -signTol]
|>;
familySummary = <|
  "random" -> <|"count" -> Length[randomRecords],
    "minS" -> N[minRecord[randomRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[randomRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "ordinaryShelfWall" -> <|"count" -> Length[wallRecords],
    "minS" -> N[minRecord[wallRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[wallRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "interfaceAndShelfWall" -> <|"count" -> Length[interfaceShelfRecords],
    "minS" -> N[minRecord[interfaceShelfRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[interfaceShelfRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "terminalSpatialRight" -> <|"count" -> Length[spatialOpenRecords],
    "minS" -> N[minRecord[spatialOpenRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[spatialOpenRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "targetedHardFace" -> <|"count" -> Length[faceRecords],
    "minS" -> N[minRecord[faceRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[faceRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "hardFaceEdgeRefinement" -> <|"count" -> Length[edgeFaceRecords],
    "minS" -> N[minRecord[edgeFaceRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[edgeFaceRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "edgeAndShelfWall" -> <|"count" -> 1,
    "minS" -> N[edgeShelfRecord["exactS"], 18],
    "minPhi" -> N[edgeShelfRecord["PhiDelta"], 18]|>
|>;
paritySummary = <|
  "integerD4" -> <|"count" -> Length[integerRecords],
    "minS" -> N[minRecord[integerRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[integerRecords, "PhiDelta"]["PhiDelta"], 18]|>,
  "halfIntegerD5" -> <|"count" -> Length[halfIntegerRecords],
    "minS" -> N[minRecord[halfIntegerRecords, "exactS"]["exactS"], 18],
    "minPhi" -> N[minRecord[halfIntegerRecords, "PhiDelta"]["PhiDelta"], 18]|>
|>;

extremalCompact[rec_Association] := Module[{td = rec["terminal"]},
  Map[N[#, 24] &,
    Join[
      KeyTake[rec, {"rho", "K", "mu", "r", "dOwner", "n", "q", "f", "p",
        "faceAlpha", "faceEta", "eps0", "epsp", "D_r", "D_q", "R_p",
        "C_p", "C_pLower", "exactS", "PhiDelta", "reductionSlack",
        "terminalLoss", "shelfLoss"}],
      <|"B" -> td["B"], "Q" -> td["Q"], "v" -> td["v"], "h" -> td["h"],
        "alpha" -> td["alpha"], "etaSum" -> td["etaSum"],
        "top" -> td["top"], "LT" -> td["LT"]|>
    ]
  ]
];
extremalLossLedger = <|
  "exactSMinusPhi" -> (globalMinPhi["exactS"] - globalMinPhi["PhiDelta"]),
  "terminalTangentLoss" -> globalMinPhi["terminalLoss"],
  "shelfCurvatureLoss" -> globalMinPhi["shelfLoss"],
  "ledgerResidual" -> globalMinPhi["ledgerResidual"]
|>;
hardWallSummary = <|
  "K0" -> hardK0, "rho0" -> hardRho0,
  "wallN" -> hardWallRecord["n"], "wallQ" -> hardWallRecord["q"],
  "wallEta1" -> First[hardWallRecord["terminal"]["etas"]],
  "openAlpha" -> hardOpenRecord["terminal"]["alpha"],
  "openEta1" -> First[hardOpenRecord["terminal"]["etas"]],
  "wallExactS" -> hardWallRecord["exactS"],
  "wallPhi" -> hardWallRecord["PhiDelta"],
  "rightLimitS" -> hardRightReplay["SRightLimitFromWall"],
  "rightLimitPhi" -> hardRightReplay["PhiRightLimitFromWall"]
|>;

wallConventionChecks = <|
  "strictFloorAt2" -> (strictFloor[N[2, wp]] == 1),
  "ordinaryFloorAt2" -> (ordinaryFloor[N[2, wp]] == 2),
  "strictFractionAt2" -> (strictFraction[N[2, wp]] == 1),
  "interfaceWallOwnsN4" -> (hardWallRecord["n"] == 4 && hardWallRecord["q"] == 5),
  "spatialWallEtaIs1" -> (Abs[First[hardWallRecord["terminal"]["etas"]] - 1] <= 10^-25),
  "openSideEtaNear0" -> (0 < First[hardOpenRecord["terminal"]["etas"]] < 10^-15),
  "edgeShelfWallEpspIs0" -> (edgeShelfRecord["p"] == 2 && Abs[edgeShelfRecord["epsp"]] <= 10^-25),
  "wallActive" -> dimensionActiveQ[hardRho0, hardK0, N[1, wp]],
  "openActive" -> dimensionActiveQ[hardRhoOpen, hardKOpen, N[1, wp]]
|>;
replayOK = And[
  And @@ Values[wallConventionChecks],
  And @@ Thread[Values[negativeCounts] == 0],
  Max[Values[identityResiduals]] < 10^-35,
  Min[Values[minimumProvedSlacks]] > -10^-25,
  Abs[hardRightReplay["SOpenMinusLimit"]] < 10^-15,
  Abs[hardRightReplay["PhiOpenMinusLimit"]] < 10^-15
];

Print["WolframVersion=", $Version];
Print["diagnosticOnly=True"];
Print["theoremClaim=False"];
Print["familySummary=", familySummary // InputForm];
Print["paritySummary=", paritySummary // InputForm];
Print["negativeCounts=", negativeCounts // InputForm];
Print["minExactS=", extremalCompact[globalMinS] // InputForm];
Print["minPhiDelta=", extremalCompact[globalMinPhi] // InputForm];
Print["extremalLossLedger=", Map[N[#, 24] &, extremalLossLedger] // InputForm];
Print["hardWallSummary=", Map[N[#, 24] &, hardWallSummary] // InputForm];
Print["hardRightReplay=", Map[N[#, 24] &, hardRightReplay] // InputForm];
Print["identityResiduals=", identityResiduals // InputForm];
Print["minimumProvedSlacks=", minimumProvedSlacks // InputForm];
Print["wallConventionChecks=", wallConventionChecks // InputForm];
Print["round20ReplayOK=", replayOK];
