(*
  Exact replay for General dimension, Round 19.

  The proof note is
    human/outbox/general-d-round-19-action-face-jensen-closure.md

  The theorem-bearing gates are symbolic identities and finite exact
  rational comparisons.  The high-precision action-face point at a=8 is
  printed separately as a diagnostic.  It is not a premise of the proof.
  No interval subdivision or floating-point coverage argument is used.

  Verified fresh-kernel invocation on Windows:
    math.exe -noinit -script
      computations/general_d_round19_action_face_jensen_replay.wl
*)

ClearAll["Global`round19*"];

round19StandaloneReplay = True;

round19AtanT[x_, n_Integer] := Sum[
  (-1)^j x^(2 j + 1)/(2 j + 1),
  {j, 0, n - 1}
];

(* Self-contained Machin certificates for 333/106 < Pi < 355/113. *)
round19PMinus = 333/106;
round19PPlus = 355/113;
round19MachinLower =
  4 round19AtanT[1/5, 6] - round19AtanT[1/239, 1];
round19MachinUpper =
  4 round19AtanT[1/5, 7] - round19AtanT[1/239, 2];
round19PiLowerMargin =
  round19MachinLower - round19PMinus/4;
round19PiUpperMargin =
  round19PPlus/4 - round19MachinUpper;

(* Exact algebra of the one-radius Jensen reduction. *)
round19P = round19g + 1;
round19Q = round19s round19g;
round19Total = round19k round19P - round19g;
round19Mean =
  (
    round19k round19P^2
    - round19s round19g^2
  )/(2 round19Total);
round19H =
  (
    2 (round19k - round19s) round19g^2
    + (round19k + 3) round19g
    - round19k
  );

round19WeightIdentity = Together[
  (round19k - 1/round19s) round19Q
  + round19k (round19P - round19Q)
  - round19Total
] == 0;

round19MeanIdentity = Together[
  2 round19Total round19Mean
  - (
      round19k round19P^2
      - round19s round19g^2
    )
] == 0;

round19WeightedMeanIdentity = Together[
  2 round19Total round19Mean
  - (
      (round19k - 1/round19s) round19Q^2
      + round19k (round19P - round19Q) (
          round19P + round19Q
        )
    )
] == 0;

round19HIdentity = Together[
  4 round19Total (round19Mean - 3/4)
  - round19H
] == 0;

round19IntrinsicIIIdentity = Together[
  3 round19g - round19H
  - (
      2 (round19s - round19k) round19g^2
      + round19k (1 - round19g)
    )
] == 0;

round19DerivativeSplitIdentity = Together[
  round19k (
    round19I0Q + round19IQP - round19UAtC0
  )
  - round19I0Q/round19s
  - (
      (round19k - 1/round19s) round19I0Q
      + round19k round19IQP
      - round19k round19UAtC0
    )
] == 0;

round19GDerivativeIdentity = Together[
  (
    round19SinPsi
    - round19psi (
        round19k round19SinBeta - round19SinPsi
      )/(round19beta - round19psi)
  )/Pi
  + round19psi round19beta/(
      Pi (round19beta - round19psi)
    ) (
      round19k round19SinBeta/round19beta
      - round19SinPsi/round19psi
    )
] == 0;

round19SpeedIdentity = FullSimplify[
  Cos[round19phi]/Cos[round19gamma]
  - (
      round19gamma + Sin[round19phi] - round19phi
    )/Sin[round19gamma]
  - (
      round19aa Cos[round19phi] (
        (Tan[round19gamma] - round19gamma)
        - (Tan[round19phi] - round19phi)
      )
      - round19gamma + round19phi
    )/(round19aa Sin[round19gamma]),
  Assumptions -> {
    round19aa > 0,
    0 < round19phi < round19gamma < Pi/2,
    round19aa Cos[round19phi] == round19aa - 1
  }
] == 0;

round19u = Unique["round19u"];
round19b = Unique["round19b"];
round19h = Sin[round19u] - round19u Cos[round19u];
round19E = (
  round19h/(round19u Sin[round19u])
)^2;
round19U0 = Sin[round19u]/round19u;
round19F0 =
  Pi round19h/(
    round19b round19u^3 Sin[round19u]
  );
round19SlopeIdentity = Together[
  (
    round19U0/round19F0
    /. round19b -> 3 Pi/(4 round19h)
  ) - 3/(4 round19E)
] == 0;

round19SymbolicChecks = And[
  round19WeightIdentity,
  round19MeanIdentity,
  round19WeightedMeanIdentity,
  round19HIdentity,
  round19IntrinsicIIIdentity,
  round19DerivativeSplitIdentity,
  round19GDerivativeIdentity,
  round19SpeedIdentity,
  round19SlopeIdentity
];

(* Finite exact constants used in intrinsic inequality (i). *)
round19PhiEndpoint = 613/1000;
round19GammaEndpoint = 613/600;
round19CosPhiUpper =
  1 - round19PhiEndpoint^2/2 + round19PhiEndpoint^4/24;
round19CosPhiMargin = 9/11 - round19CosPhiUpper;
round19CosGammaLower =
  (
    1 - round19GammaEndpoint^2/2
    + round19GammaEndpoint^4/24
    - round19GammaEndpoint^6/720
  );
round19CosGammaMargin = round19CosGammaLower - 25/48;
round19SecantRatioMargin = round19PMinus - 157/50;
round19ERatioMargin = 4/49 - (3/5)^5;
round19JEndpointMargin =
  14 - 7 (22/7)^3/24 - (22/7)^2/2;

(* Finite exact constants used in intrinsic inequality (ii). *)
round19GammaWallMargin = 63/121 - 1/2;
round19KUpperSquareMargin = 675 - (176/7)^2;
round19SmallAMargin =
  (round19PMinus + 2)/40 - 1/8;
round19GRangeMargin = 1/8 - 10/81;

(*
  Exact a=8 checkpoint.  The first comparison puts the action radius
  above K0.  The next two compare the inner and outer actions at w0.
*)
round19A0 = 8;
round19T0 = 7;
round19K0 = 229/20;
round19W0 = 73/20;

round19KtMinus = 9061/1000;
round19KtPlus = 9062/1000;
round19AtMinus = 3872/1000;
round19AtPlus = 3873/1000;

round19KwMinus = 10852/1000;
round19KwPlus = 10853/1000;
round19AwMinus = 7118/1000;
round19AwPlus = 7119/1000;

round19TBracketMargins = <|
  "outerLower" ->
    round19K0^2 - round19T0^2 - round19KtMinus^2,
  "outerUpper" ->
    round19KtPlus^2 - (round19K0^2 - round19T0^2),
  "innerLower" ->
    round19A0^2 - round19T0^2 - round19AtMinus^2,
  "innerUpper" ->
    round19AtPlus^2 - (round19A0^2 - round19T0^2)
|>;

round19WBracketMargins = <|
  "outerLower" ->
    round19K0^2 - round19W0^2 - round19KwMinus^2,
  "outerUpper" ->
    round19KwPlus^2 - (round19K0^2 - round19W0^2),
  "innerLower" ->
    round19A0^2 - round19W0^2 - round19AwMinus^2,
  "innerUpper" ->
    round19AwPlus^2 - (round19A0^2 - round19W0^2)
|>;

round19ActionCertificate =
  (
    round19KtPlus - round19AtMinus
    - round19T0 round19PMinus/2
    + round19T0 (
        round19AtanT[round19T0/round19KtMinus, 7]
        + round19AtanT[round19AtPlus/round19T0, 7]
      )
  );
round19ActionMargin =
  3 round19PMinus/4 - round19ActionCertificate;

round19InnerCertificate =
  (
    round19AwPlus
    - round19W0 round19PMinus/2
    + round19W0 round19AtanT[
        round19W0/round19AwMinus,
        5
      ]
  );
round19InnerMargin =
  round19PMinus - round19InnerCertificate;

round19OuterCertificate =
  (
    round19KwMinus
    - round19W0 round19PPlus/2
    + round19W0 round19AtanT[
        round19W0/round19KwPlus,
        4
      ]
  );
round19OuterMargin =
  round19OuterCertificate - 2 round19PPlus;

round19ExactChecks = And[
  round19SymbolicChecks,

  round19PiLowerMargin ==
    71255393653/3428996484375000,
  round19PiUpperMargin ==
    4525115621373289/67860769651479492187500,
  round19PiLowerMargin > 1/100000,
  round19PiUpperMargin > 1/100000000,

  round19CosPhiMargin ==
    48282245029/264000000000000,
  round19CosGammaMargin ==
    36367360087918391/33592320000000000000,
  round19SecantRatioMargin == 2/1325,
  round19ERatioMargin > 0,
  round19JEndpointMargin == 1/147,
  round19PMinus > 25/8,
  round19GammaEndpoint < round19PMinus/2,

  round19GammaWallMargin > 0,
  round19KUpperSquareMargin == 2099/49,
  round19SmallAMargin == 3/848,
  round19GRangeMargin == 1/648,

  round19TBracketMargins["outerLower"] == 779/1000000,
  round19TBracketMargins["outerUpper"] == 271/15625,
  round19TBracketMargins["innerLower"] == 119/15625,
  round19TBracketMargins["innerUpper"] == 129/1000000,
  AllTrue[Values[round19TBracketMargins], # > 0 &],

  round19WBracketMargins["outerLower"] == 881/62500,
  round19WBracketMargins["outerUpper"] == 7609/1000000,
  round19WBracketMargins["innerLower"] == 1447/125000,
  round19WBracketMargins["innerUpper"] == 2661/1000000,
  AllTrue[Values[round19WBracketMargins], # > 0 &],

  0 < round19T0/round19KtMinus < 1,
  0 < round19AtPlus/round19T0 < 1,
  0 < round19W0/round19AwMinus < 1,
  0 < round19W0/round19KwPlus < 1,
  round19ActionMargin > 1/100,
  round19InnerMargin > 1/50,
  round19OuterMargin > 1/60
];

Print[
  "round19StandaloneReplay=",
  round19StandaloneReplay
];
Print["round19SymbolicChecks=", round19SymbolicChecks];
Print[
  "round19PiMargins=",
  {round19PiLowerMargin, round19PiUpperMargin} // InputForm
];
Print[
  "round19IntrinsicIMargins=",
  <|
    "cosPhi" -> round19CosPhiMargin,
    "cosGamma" -> round19CosGammaMargin,
    "secantRatio" -> round19SecantRatioMargin,
    "eRatioSquared" -> round19ERatioMargin,
    "JEndpoint" -> round19JEndpointMargin
  |> // InputForm
];
Print[
  "round19IntrinsicIIMargins=",
  <|
    "gammaWall" -> round19GammaWallMargin,
    "kUpperSquare" -> round19KUpperSquareMargin,
    "smallA" -> round19SmallAMargin,
    "gRange" -> round19GRangeMargin
  |> // InputForm
];
Print[
  "round19TBracketMargins=",
  round19TBracketMargins // InputForm
];
Print[
  "round19WBracketMargins=",
  round19WBracketMargins // InputForm
];
Print[
  "round19CheckpointMargins=",
  <|
    "action" -> round19ActionMargin,
    "inner" -> round19InnerMargin,
    "outer" -> round19OuterMargin
  |> // InputForm
];
Print["round19ExactReplayOK=", round19ExactChecks];

(* Separate high-precision diagnostic at a=8. *)
round19G[bb_?NumericQ, xx_?NumericQ] :=
  (Sqrt[bb^2 - xx^2] - xx ArcCos[xx/bb])/Pi;

round19PPrimitive[bb_?NumericQ, xx_?NumericQ] :=
  (
    bb^2 ArcCos[xx/bb]
    - xx Sqrt[bb^2 - xx^2]
  )/(2 Pi bb);

round19U[bb_?NumericQ, cc_?NumericQ] := Module[{angle},
  If[cc == 0, Return[1]];
  angle = uu /. FindRoot[
    bb (Sin[uu] - uu Cos[uu])/Pi == cc,
    {uu, N[10^-20, 70], N[Pi/2, 70]},
    Method -> "Brent",
    WorkingPrecision -> 50,
    AccuracyGoal -> 34,
    PrecisionGoal -> 34
  ];
  Sin[angle]/angle
];

round19DiagnosticA = N[8, 70];
round19DiagnosticK = kk /. FindRoot[
  round19G[kk, round19DiagnosticA - 1]
  - round19G[round19DiagnosticA, round19DiagnosticA - 1]
  == 3/4,
  {kk, N[round19K0, 70], N[16, 70]},
  Method -> "Brent",
  WorkingPrecision -> 60,
  AccuracyGoal -> 42,
  PrecisionGoal -> 42
];
round19DiagnosticX = xx /. FindRoot[
  round19G[round19DiagnosticK, xx]
  - round19G[round19DiagnosticA, xx]
  == 1,
  {xx, N[0, 70], N[7, 70]},
  Method -> "Brent",
  WorkingPrecision -> 60,
  AccuracyGoal -> 42,
  PrecisionGoal -> 42
];
round19DiagnosticG =
  round19G[round19DiagnosticA, round19DiagnosticX];
round19DiagnosticGamma = ArcCos[
  (round19DiagnosticA - 1)/round19DiagnosticK
];
round19DiagnosticPhi = ArcCos[
  (round19DiagnosticA - 1)/round19DiagnosticA
];
round19DiagnosticSpeed =
  (
    round19DiagnosticGamma
    + Sin[round19DiagnosticPhi]
    - round19DiagnosticPhi
  )/Sin[round19DiagnosticGamma];
round19DiagnosticS =
  round19DiagnosticK/round19DiagnosticA;
round19DiagnosticP = round19DiagnosticG + 1;
round19DiagnosticQ =
  round19DiagnosticS round19DiagnosticG;
round19DiagnosticTotal =
  (
    round19DiagnosticSpeed round19DiagnosticP
    - round19DiagnosticG
  );
round19DiagnosticMean =
  (
    round19DiagnosticSpeed round19DiagnosticP^2
    - round19DiagnosticS round19DiagnosticG^2
  )/(2 round19DiagnosticTotal);
round19DiagnosticTheta = theta /. FindRoot[
  round19DiagnosticK (
    Sin[theta] - theta Cos[theta]
  )/Pi == 3/4,
  {theta, N[10^-20, 70], N[Pi/2, 70]},
  Method -> "Brent",
  WorkingPrecision -> 60,
  AccuracyGoal -> 42,
  PrecisionGoal -> 42
];
round19DiagnosticDerivative =
  (
    round19DiagnosticSpeed (
      round19PPrimitive[
        round19DiagnosticK,
        round19DiagnosticX
      ]
      - Sin[round19DiagnosticTheta]/round19DiagnosticTheta
    )
    - round19PPrimitive[
        round19DiagnosticA,
        round19DiagnosticX
      ]
  );
round19DiagnosticJensenBound =
  (
    round19DiagnosticTotal round19U[
      round19DiagnosticK,
      round19DiagnosticMean
    ]
    - round19DiagnosticSpeed round19U[
        round19DiagnosticK,
        3/4
      ]
  );
round19DiagnosticH =
  (
    2 (
      round19DiagnosticSpeed - round19DiagnosticS
    ) round19DiagnosticG^2
    + (round19DiagnosticSpeed + 3) round19DiagnosticG
    - round19DiagnosticSpeed
  );
round19DiagnosticE = (
  (
    Sin[round19DiagnosticTheta]
    - round19DiagnosticTheta Cos[round19DiagnosticTheta]
  )/(
    round19DiagnosticTheta Sin[round19DiagnosticTheta]
  )
)^2;

round19Diagnostic = <|
  "a" -> round19DiagnosticA,
  "K" -> round19DiagnosticK,
  "x" -> round19DiagnosticX,
  "g" -> round19DiagnosticG,
  "speed" -> round19DiagnosticSpeed,
  "s" -> round19DiagnosticS,
  "qLessThanP" ->
    round19DiagnosticP - round19DiagnosticQ,
  "mean" -> round19DiagnosticMean,
  "derivative" -> round19DiagnosticDerivative,
  "JensenBound" -> round19DiagnosticJensenBound,
  "kMinusOneMinusE" ->
    round19DiagnosticSpeed - 1 - round19DiagnosticE,
  "threeGMinusH" ->
    3 round19DiagnosticG - round19DiagnosticH
|>;

round19DiagnosticChecks = And[
  N[round19DiagnosticK - round19K0, 30] > 0,
  N[1 - round19DiagnosticG, 30] > 0,
  N[round19DiagnosticP - round19DiagnosticQ, 30] > 0,
  N[round19DiagnosticDerivative, 30] > 0,
  N[round19DiagnosticJensenBound, 30] > 0,
  N[
    round19DiagnosticDerivative
    - round19DiagnosticJensenBound,
    30
  ] > 0,
  N[
    round19DiagnosticSpeed - 1 - round19DiagnosticE,
    30
  ] > 0,
  N[3 round19DiagnosticG - round19DiagnosticH, 30] > 0
];

Print[
  "round19Diagnostic=",
  N[round19Diagnostic, 30] // InputForm
];
Print["round19DiagnosticChecks=", round19DiagnosticChecks];

round19ReplayOK = And[
  TrueQ[round19ExactChecks],
  TrueQ[round19DiagnosticChecks]
];

Print["round19ReplayOK=", round19ReplayOK];

If[!TrueQ[round19ReplayOK], Exit[2]];
