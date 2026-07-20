(* Round 42 algebra-only replay for the stronger upper-alpha endpoint.

   This file checks exact substitutions and loss identities only.  It owns
   no strict bracket, endpoint label, or sign of the open target T42. *)

ClearAll["Global`*"];

countRules = {n -> f - 1, f -> B + j, B0 -> B - 1};
countResidual = FullSimplify[n - (B0 + j) //. countRules];

M = Min[zeta, H];

minimumResidual = FullSimplify[
  B0 zeta + H (j + ep + h) -
   ((B0 + j) M + H (ep + h)) -
   (B0 (zeta - M) + j (H - M))
];

phi = 1/(2 beta) - J + omegaMinus + B0 zeta +
  (p + ap) delta + 2 p ep - (p - d m)/2;

t42 = 9/10 + B0 M + H h - (p - d m)/2;

adjacentResidual = (p + ap) (delta - R1 (j + ep + h));
capResidual = 1/(2 beta) - J - 9/10;

lossResidual = FullSimplify[
  phi - t42 -
   (capResidual + omegaMinus + adjacentResidual +
    B0 (zeta - M) + j H + (H + 2 p) ep),
  Assumptions -> H == (p + ap) R1
];

stageOneLower = (B0 + j) M + H (ep + h);
stageOneLossResidual = FullSimplify[
  B0 zeta + (p + ap) delta - stageOneLower -
   (adjacentResidual + B0 (zeta - M) + j (H - M)),
  Assumptions -> H == (p + ap) R1
];

stageTwoLossResidual = FullSimplify[
  (1/(2 beta) - J + omegaMinus + stageOneLower + 2 p ep -
     (p - d m)/2) - t42 -
   (capResidual + omegaMinus + j M + (H + 2 p) ep)
];

round42StrongerPhiReplayOK = And[
  countResidual === 0,
  minimumResidual === 0,
  lossResidual === 0,
  stageOneLossResidual === 0,
  stageTwoLossResidual === 0
];

Print["countResidual=", countResidual];
Print["minimumResidual=", minimumResidual];
Print["lossResidual=", lossResidual];
Print["stageOneLossResidual=", stageOneLossResidual];
Print["stageTwoLossResidual=", stageTwoLossResidual];
Print["round42StrongerPhiReplayOK=", round42StrongerPhiReplayOK];
