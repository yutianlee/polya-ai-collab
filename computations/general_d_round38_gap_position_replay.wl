(* Round 38 exact symbolic replay.
   This checks algebraic and calculus identities only. It is not a sign
   certificate and it does not own strict floors or one-sided labels. *)

G[a_, z_] :=
  (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi;

(* Gap-position algebra. *)
gapRules = {
   lambda -> j + u,
   f -> B + j,
   W -> B - 1/4 - u,
   Sq -> u - chi,
   Aq -> W + Sq,
   v -> Aq + h,
   Q -> B - 1,
   Ax -> f - 1/4 + ep
   };

gapPositionResiduals = FullSimplify[
   {
    Aq - (B - 1/4 - chi),
    v - (B - 1/4 + h - chi),
    (Aq + 1/4 - Q) - (1 - chi),
    (Ax - Aq) - (j + ep + chi)
    } //. gapRules
   ];

(* Xi refinement and elasticity coefficient. *)
xiResidual = FullSimplify[
   (E - M4) - (2 ep + Delta - M4),
   Assumptions -> E == Delta + 2 ep
   ];

tau = gEl/(gEl + 2);
tauResidual = FullSimplify[2 tau/(1 - tau) - gEl];

(* Count-phase change of variables. *)
tFromZeta = Pi/(2 (1 + zeta));
xFromZeta = FullSimplify[Pi/2 - tFromZeta];
xFromZetaResidual = FullSimplify[
   xFromZeta - Pi zeta/(2 (1 + zeta))
   ];

countPhaseResidual = FullSimplify[
   zeta (3/(Pi xFromZeta) - 9/4) -
    (6 (1 + zeta)/Pi^2 - 9 zeta/4)
   ];

(* Cotangent lower-bound auxiliary derivative. *)
cotDerivativeResidual = FullSimplify[
   D[x Cos[x] - (1 - x^2) Sin[x], x] -
    (x^2 Cos[x] + x Sin[x])
   ];

(* Linear chi compensation, on the two possible minimum branches. *)
compLowResidual = FullSimplify[
   H chi + 2 (h - chi)/beta - h H -
    (h - chi) (2/beta - H)
   ];

compHighResidual = FullSimplify[
   H chi + 2 (h - chi)/beta - 2 h/beta -
    chi (H - 2/beta)
   ];

(* Minimum algebra in R38.18. *)
minimumHighResidual = FullSimplify[
   ((n - j) zeta + H (j + ep + chi)) -
    (n zeta + H ep + H chi) -
    j (H - zeta)
   ];

minimumLowResidual = FullSimplify[
   ((n - j) zeta + H (j + ep + chi)) -
    (n H + H ep + H chi) -
    (n - j) (zeta - H)
   ];

(* Interface action-gap sum. *)
interfaceSumResidual = FullSimplify[
   Sum[B0 - k + 1 - u, {k, 1, B0}] -
    B0 (B0 + 1 - 2 u)/2,
   Assumptions -> Element[B0, Integers] && B0 >= 1
   ];

(* Gamma refinement. *)
gammaResidual = FullSimplify[
   (p + ap) M4 + p Xi -
    ((p + ap) M4 + 2 p ep + p XiHat),
   Assumptions -> Xi == 2 ep + XiHat
   ];

thresholdResidual = FullSimplify[6/7 + 1/5 - 1 - 2/35];

(* Action-angle derivative used in R38.22. *)
actionAngleDerivativeResidual = FullSimplify[
   D[K/Pi (Sin[theta] - theta Cos[theta]), theta] -
    K/Pi theta Sin[theta]
   ];

(* Upper-alpha exact cap. *)
mu = q + 1;
hAlpha1 = FullSimplify[G[mu, q], Assumptions -> q > 0];
hAlpha1Closed =
  (Sqrt[2 q + 1] - q ArcCos[q/(q + 1)])/Pi;
hAlpha1Residual = FullSimplify[
   hAlpha1 - hAlpha1Closed,
   Assumptions -> q > 0
   ];

Jclosed =
  ((mu^2 + 2 q^2) ArcCos[q/mu] -
     3 q Sqrt[mu^2 - q^2])/(2 Pi);

Jraw = FullSimplify[
   2 Integrate[G[mu, z], {z, q, mu},
      GenerateConditions -> False] - Jclosed,
   Assumptions -> q > 0,
   TransformationFunctions -> {Automatic, FunctionExpand}
   ];

arcBranchIdentity = FullSimplify[
   ArcSin[zetaArc] ==
    ArcTan[zetaArc/Sqrt[1 - zetaArc^2]],
   Assumptions -> 0 < zetaArc < 1
   ];

Jcheck = FullSimplify[
   Jraw /. ArcSin[q/(q + 1)] ->
     ArcTan[q/Sqrt[(q + 1)^2 - q^2]],
   Assumptions -> q > 0
   ];

Print["gapPositionResiduals=", gapPositionResiduals];
Print["xiResidual=", xiResidual];
Print["tauResidual=", tauResidual];
Print["xFromZeta=", xFromZeta];
Print["xFromZetaResidual=", xFromZetaResidual];
Print["countPhaseResidual=", countPhaseResidual];
Print["cotDerivativeResidual=", cotDerivativeResidual];
Print["compLowResidual=", compLowResidual];
Print["compHighResidual=", compHighResidual];
Print["minimumHighResidual=", minimumHighResidual];
Print["minimumLowResidual=", minimumLowResidual];
Print["interfaceSumResidual=", interfaceSumResidual];
Print["gammaResidual=", gammaResidual];
Print["thresholdResidual=", thresholdResidual];
Print["actionAngleDerivativeResidual=", actionAngleDerivativeResidual];
Print["hAlpha1=", hAlpha1];
Print["hAlpha1Residual=", hAlpha1Residual];
Print["Jraw=", Jraw];
Print["arcBranchIdentity=", arcBranchIdentity];
Print["Jcheck=", Jcheck];

round38GapPositionReplayOK = And[
   gapPositionResiduals === {0, 0, 0, 0},
   xiResidual === 0,
   tauResidual === 0,
   xFromZetaResidual === 0,
   countPhaseResidual === 0,
   cotDerivativeResidual === 0,
   compLowResidual === 0,
   compHighResidual === 0,
   minimumHighResidual === 0,
   minimumLowResidual === 0,
   interfaceSumResidual === 0,
   gammaResidual === 0,
   thresholdResidual === 0,
   actionAngleDerivativeResidual === 0,
   hAlpha1Residual === 0,
   arcBranchIdentity === True,
   Jcheck === 0
   ];

Print["round38GapPositionReplayOK=", round38GapPositionReplayOK];
