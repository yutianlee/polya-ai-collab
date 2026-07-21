(* Round 48 exact symbolic replay for the certified route counterexample. *)

ClearAll[R, z, primitive, primitiveDerivative, endpointValue];

primitive[R_, z_] :=
  (3 R^4 ArcSin[z/R]
    - z Sqrt[R^2 - z^2] (3 R^2 + 2 z^2)
    + 8 z^4 ArcCos[z/R])/(32 Pi);

primitiveDerivative = FullSimplify[
  D[primitive[R, z], z] == z^3 ArcCos[z/R]/Pi,
  Assumptions -> {R > 0, 0 < z < R}
];

endpointValue = FullSimplify[
  Limit[primitive[R, z], z -> R, Direction -> "FromBelow"] == 3 R^4/64,
  Assumptions -> R > 0
];

round48CounterexampleReplayOK = And[primitiveDerivative, endpointValue];

Print["primitiveDerivative=", primitiveDerivative];
Print["endpointValue=", endpointValue];
Print["round48CounterexampleReplayOK=", round48CounterexampleReplayOK];

If[TrueQ[round48CounterexampleReplayOK], Exit[0], Exit[1]];
