(*
  Exact replay for General dimension, Round 18.

  The proof note is
    human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure.md

  All theorem-bearing gates below are finite exact rational comparisons.
  The FindRoot block at the end is a separate high-precision diagnostic and
  is not a premise of the proof.  No interval arithmetic or subdivision is
  used or claimed.
*)

ClearAll[
  round18AtanT, round18G, round18H,
  round18PMinus, round18PPlus,
  round18MachinLower, round18MachinUpper,
  round18PiLowerMargin, round18PiUpperMargin,
  round18LowerA, round18LowerT,
  round18LowerRMinus, round18LowerRPlus,
  round18LowerIMinus, round18LowerIPlus,
  round18LowerOuterMargins, round18LowerInnerMargins,
  round18LowerHCertificate, round18LowerHMargin,
  round18UpperA, round18UpperT,
  round18UpperRMinus, round18UpperRPlus,
  round18UpperIMinus, round18UpperIPlus,
  round18UpperOuterMargins, round18UpperInnerMargins,
  round18UpperHCertificate, round18UpperHMargin,
  round18S0, round18ZRMinus, round18ZRPlus,
  round18ZOuterMargins, round18ZCertificate, round18ZMargin,
  round18FinalMargin, round18ExactChecks,
  round18DiagnosticA, round18DiagnosticK,
  round18DiagnosticZ, round18DiagnosticF,
  round18DiagnosticResiduals, round18ReplayOK
];

round18ReplayOnly = True;

round18AtanT[x_, n_Integer] := Sum[
  (-1)^j x^(2 j + 1)/(2 j + 1),
  {j, 0, n - 1}
];

(* Machin-certified rational bounds for Pi. *)
round18PMinus = 333/106;
round18PPlus = 355/113;

round18MachinLower =
  4 round18AtanT[1/5, 6] - round18AtanT[1/239, 1];
round18MachinUpper =
  4 round18AtanT[1/5, 7] - round18AtanT[1/239, 2];

round18PiLowerMargin =
  round18MachinLower - round18PMinus/4;
round18PiUpperMargin =
  round18PPlus/4 - round18MachinUpper;

(* Lower wall bracket a=11/2. *)
round18LowerA = 11/2;
round18LowerT = 9/2;
round18LowerRMinus = 7377/1000;
round18LowerRPlus = 7378/1000;
round18LowerIMinus = 3162/1000;
round18LowerIPlus = 3163/1000;

round18LowerOuterMargins = <|
  "lower" ->
    round18PMinus^2 + 11 round18PMinus + 10
      - round18LowerRMinus^2,
  "upper" ->
    round18LowerRPlus^2
      - (round18PPlus^2 + 11 round18PPlus + 10)
|>;

round18LowerInnerMargins = <|
  "lower" -> 10 - round18LowerIMinus^2,
  "upper" -> round18LowerIPlus^2 - 10
|>;

round18LowerHCertificate = (
  round18LowerRMinus - round18LowerIPlus
  - round18LowerT round18PPlus/2
  + round18LowerT * (
      round18AtanT[
        round18LowerT/round18LowerRPlus,
        6
      ]
      + round18AtanT[
        round18LowerIMinus/round18LowerT,
        6
      ]
    )
);

round18LowerHMargin =
  round18LowerHCertificate - 3 round18PPlus/4;

(* Upper wall bracket a=45/8. *)
round18UpperA = 45/8;
round18UpperT = 37/8;
round18UpperRMinus = 7447/1000;
round18UpperRPlus = 7448/1000;
round18UpperIMinus = 3201/1000;
round18UpperIPlus = 3202/1000;

round18UpperOuterMargins = <|
  "lower" ->
    (round18UpperA + round18PMinus)^2
      - round18UpperT^2 - round18UpperRMinus^2,
  "upper" ->
    round18UpperRPlus^2
      - (
        (round18UpperA + round18PPlus)^2
        - round18UpperT^2
      )
|>;

round18UpperInnerMargins = <|
  "lower" -> 41/4 - round18UpperIMinus^2,
  "upper" -> round18UpperIPlus^2 - 41/4
|>;

round18UpperHCertificate = (
  round18UpperRPlus - round18UpperIMinus
  - round18UpperT round18PMinus/2
  + round18UpperT * (
      round18AtanT[
        round18UpperT/round18UpperRMinus,
        7
      ]
      + round18AtanT[
        round18UpperIPlus/round18UpperT,
        7
      ]
    )
);

round18UpperHMargin =
  3 round18PMinus/4 - round18UpperHCertificate;

(* The z comparison at K0=45/8+Pi and s0=101/20. *)
round18S0 = 101/20;
round18ZRMinus = 7165/1000;
round18ZRPlus = 7167/1000;

round18ZOuterMargins = <|
  "lower" ->
    (round18UpperA + round18PMinus)^2
      - round18S0^2 - round18ZRMinus^2,
  "upper" ->
    round18ZRPlus^2
      - (
        (round18UpperA + round18PPlus)^2
        - round18S0^2
      )
|>;

round18ZCertificate = (
  round18ZRPlus
  - round18S0 round18PMinus/2
  + round18S0 round18AtanT[
      round18S0/round18ZRMinus,
      5
    ]
);

round18ZMargin =
  3 round18PMinus/4 - round18ZCertificate;

round18FinalMargin =
  (
    round18PMinus^2
    + 11 round18PMinus
    - 222/5
  )/8;

round18ExactChecks = And[
  round18PiLowerMargin ==
    71255393653/3428996484375000,
  round18PiUpperMargin ==
    4525115621373289/67860769651479492187500,
  round18PiLowerMargin > 1/100000,
  round18PiUpperMargin > 1/100000000,

  round18LowerOuterMargins["lower"] ==
    15607639/2809000000,
  round18LowerOuterMargins["upper"] ==
    24758449/3192250000,
  round18LowerInnerMargins["lower"] == 439/250000,
  round18LowerInnerMargins["upper"] == 4569/1000000,
  AllTrue[Values[round18LowerOuterMargins], # > 0 &],
  AllTrue[Values[round18LowerInnerMargins], # > 0 &],
  round18LowerHMargin > 1/150,

  round18UpperOuterMargins["lower"] ==
    9139519/2809000000,
  round18UpperOuterMargins["upper"] ==
    2030584/199515625,
  round18UpperInnerMargins["lower"] == 3599/1000000,
  round18UpperInnerMargins["upper"] == 701/250000,
  AllTrue[Values[round18UpperOuterMargins], # > 0 &],
  AllTrue[Values[round18UpperInnerMargins], # > 0 &],
  round18UpperHMargin > 1/600,

  round18ZOuterMargins["lower"] == 336031/28090000,
  round18ZOuterMargins["upper"] == 48642129/3192250000,
  AllTrue[Values[round18ZOuterMargins], # > 0 &],
  round18ZMargin > 1/100,

  0 < round18LowerT/round18LowerRPlus < 1,
  0 < round18LowerIMinus/round18LowerT < 1,
  0 < round18UpperT/round18UpperRMinus < 1,
  0 < round18UpperIPlus/round18UpperT < 1,
  0 < round18S0/round18ZRMinus < 1,

  round18FinalMargin == 1443/449440,
  round18FinalMargin > 0
];

Print["round18ReplayOnly=", round18ReplayOnly];
Print["round18PiLowerMargin=", round18PiLowerMargin // InputForm];
Print["round18PiUpperMargin=", round18PiUpperMargin // InputForm];
Print[
  "round18LowerBracketMargins=",
  {round18LowerOuterMargins, round18LowerInnerMargins} // InputForm
];
Print[
  "round18LowerHMargin=",
  round18LowerHMargin // InputForm
];
Print[
  "round18UpperBracketMargins=",
  {round18UpperOuterMargins, round18UpperInnerMargins} // InputForm
];
Print[
  "round18UpperHMargin=",
  round18UpperHMargin // InputForm
];
Print[
  "round18ZBracketMargins=",
  round18ZOuterMargins // InputForm
];
Print["round18ZMargin=", round18ZMargin // InputForm];
Print["round18FinalMargin=", round18FinalMargin // InputForm];
Print["round18ExactChecks=", round18ExactChecks];

(* Separate floating-point diagnostic; not part of round18ExactChecks. *)
round18G[bb_?NumericQ, ss_?NumericQ] :=
  (
    Sqrt[bb^2 - ss^2]
    - ss ArcCos[ss/bb]
  )/Pi;

round18H[aa_?NumericQ] := (
  round18G[aa + Pi, aa - 1]
  - round18G[aa, aa - 1]
);

round18DiagnosticA = aa /. FindRoot[
  round18H[aa] == 3/4,
  {
    aa,
    N[round18LowerA, 60],
    N[round18UpperA, 60]
  },
  Method -> "Brent",
  WorkingPrecision -> 60,
  AccuracyGoal -> 45,
  PrecisionGoal -> 45
];

round18DiagnosticK = round18DiagnosticA + Pi;

round18DiagnosticZ = zz /. FindRoot[
  round18G[round18DiagnosticK, zz] == 3/4,
  {
    zz,
    N[0, 60],
    N[round18DiagnosticK, 60]
  },
  Method -> "Brent",
  WorkingPrecision -> 60,
  AccuracyGoal -> 45,
  PrecisionGoal -> 45
];

round18DiagnosticF =
  (
    round18DiagnosticK^2
    - round18DiagnosticA^2
  )/8 - round18DiagnosticZ;

round18DiagnosticResiduals = <|
  "actionWall" -> round18H[round18DiagnosticA] - 3/4,
  "radialWall" ->
    (round18DiagnosticK - round18DiagnosticA)/Pi - 1,
  "inverseLevel" ->
    round18G[round18DiagnosticK, round18DiagnosticZ] - 3/4,
  "criticalAtZero" ->
    (
      round18G[round18DiagnosticK, 0]
      - round18G[round18DiagnosticA, 0]
    ) - 1
|>;

Print[
  "round18Diagnostic=",
  N[
    <|
      "a" -> round18DiagnosticA,
      "K" -> round18DiagnosticK,
      "z" -> round18DiagnosticZ,
      "F" -> round18DiagnosticF
    |>,
    30
  ] // InputForm
];
Print[
  "round18DiagnosticResiduals=",
  N[round18DiagnosticResiduals, 30] // InputForm
];

round18ReplayOK = TrueQ[round18ExactChecks] && And[
  N[round18DiagnosticA - round18LowerA, 30] > 0,
  N[round18UpperA - round18DiagnosticA, 30] > 0,
  N[round18S0 - round18DiagnosticZ, 30] > 0,
  N[round18DiagnosticF - 1/2, 30] > 0,
  Max[
    Abs[
      N[Values[round18DiagnosticResiduals], 30]
    ]
  ] < 10^-35
];

Print["round18ReplayOK=", round18ReplayOK];

If[!TrueQ[round18ReplayOK], Exit[2]];
