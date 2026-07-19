(* ::Package:: *)

(*
  Exact symbolic/rational replay for the Round 31 retained-E shelf
  reductions.  The analytic proof is printed in the companion note.  This
  file checks identities and rational comparison margins; it does not supply
  continuum coverage by numerical sampling.
*)

ClearAll["Global`*"];

(* Full retained-E p-convexity: curvature term and normalized kernel. *)
r = x - p;
c1 = (1/M - 1/K)/(2 Pi);
c3 = (1/M^3 - 1/K^3)/(24 Pi);
cTerm = p^3/3 (c1 + c3 (x^2 + r^2));
cSecondIntegral = 1/Pi (
    p (1/M - 1/K)
    + p (r^2/2 + p^2/3) (1/(3 M^3) - 1/(3 K^3))
  );
cSecondResidual = Together[D[cTerm, {p, 2}] - cSecondIntegral];

kernelD[u_, v_] :=
  2 u/Sqrt[1 - u^2]
  + v (1 + u^2/2 + v^2/3 - (1 - u^2)^(-3/2));

uOfT = (1 - t^2)/(1 + t^2);
invSqrtOfT = (1 + t^2)/(2 t);
invThreeHalvesOfT = (1 + t^2)^3/(8 t^3);
aOfT = invThreeHalvesOfT - 1 - uOfT^2/2;
kernelBaseOfT = Together[
  2 uOfT invSqrtOfT - (1 - uOfT) aOfT
  ];
kernelFactorOfT =
  (1 - t) * (1 + t - t^2 + t^3) *
    (3 + 9 t^2 + 6 t^3 + 11 t^4 + 2 t^5 + t^6)/
  (4 t (1 + t^2)^3);
kernelFactorResidual = Together[kernelBaseOfT - kernelFactorOfT];

(* Lower-scalar Hessian and edge reductions. *)
lowerScalar = (
  7/10 +
  2/3 * p^2 * (3 x - p) * (aa + bb (x^2 + (x - p)^2)) -
  p/2 + dd (q - x)/2
  );
lowerLppExpected = 4/3 * (
  3 aa (x - p) +
  bb (2 p^3 - 6 p (x - p)^2 + 6 (x - p)^3)
  );
lowerLxxExpected = 8/3 bb p^2 (9 x - 4 p);
lowerHessianQ = (
  9 aa^2 +
  aa bb (36 p^2 - 66 p x + 54 x^2) +
  bb^2 (20 p^4 - 60 p^3 x + 204 p^2 x^2 -
      384 p x^3 + 216 x^4)
  );
lowerDerivativeResiduals = {
  Together[D[lowerScalar, {p, 2}] - lowerLppExpected],
  Together[D[lowerScalar, {x, 2}] - lowerLxxExpected],
  Together[
    Det[{{D[lowerScalar, {p, 2}], D[D[lowerScalar, p], x]},
       {D[D[lowerScalar, p], x], D[lowerScalar, {x, 2}]}}]
    + 16 p^2 lowerHessianQ/9
    ]
  };

(* q >= 1000 angle and phase comparison margins. *)
angleMargins = {
  (48/25)^3 - 99/14,
  (15337/15625)^2 - 24/25,
  3240/501 - (93/50)^3,
  21/10 - 31925/15337,
  191/6144 - 2679/125000,
  441/100 - (384/191) (2679/1250)
  };
angleMarginsExpected = {
  1413/218750,
  848569/244140625,
  672381/20875000,
  2827/153370,
  926903/96000000,
  48303/477500
  };
angleMarginResiduals = Together[angleMargins - angleMarginsExpected];

endpointRatioSquared[c_] :=
  (50 c/(11 (1 + c)^2))^2 * 10 * (28 + 11 c)/103;
endpointMargins = {
  endpointRatioSquared[43/50] - 1,
  endpointRatioSquared[10] - 1
  };
endpointMarginsExpected = {
  3396674029937/932297220063,
  162529217/182470783
  };
endpointMarginResiduals =
  Together[endpointMargins - endpointMarginsExpected];

(* Nine-step hard-sector bootstrap. *)
nLambda[lambda_] :=
  (17/10) * (43 lambda/50) * (11/10) *
    (2 - 11 (2 + lambda)/1000);
dBootstrap = (44/7) * (103/100);
rLambda[lambda_] := 103 * (32 + 11 lambda)/500;
bootstrapPairs = {
  {1, 4/25},
  {25/17, 1/5},
  {5/3, 1/4},
  {2, 7/25},
  {25/11, 3/10},
  {5/2, 1/3},
  {3, 3/8},
  {4, 9/20},
  {10, 1/2}
  };
bootstrapMargins = Map[
  Function[pair,
    nLambda[pair[[1]]]^2
      - pair[[2]]^2 dBootstrap^2 rLambda[pair[[1]]]
    ],
  bootstrapPairs
  ];
bootstrapMarginsExpected = {
  614330619919841/1225000000000000,
  395473621015143/80920000000000,
  1690109506680529/3969000000000000,
  1181252902401/390625000000,
  13049143106121/1960000000000,
  4446576884107303/1008000000000000,
  447338606701041/49000000000000,
  418992011999341/19140625000000,
  456264879163841/765625000000
  };
bootstrapMarginResiduals =
  Together[bootstrapMargins - bootstrapMarginsExpected];

round31RetainedShelfReplayOK = And[
  cSecondResidual === 0,
  kernelFactorResidual === 0,
  And @@ (# === 0 & /@ lowerDerivativeResiduals),
  And @@ (# === 0 & /@ angleMarginResiduals),
  And @@ (# > 0 & /@ angleMargins),
  And @@ (# === 0 & /@ endpointMarginResiduals),
  And @@ (# > 0 & /@ endpointMargins),
  And @@ (# === 0 & /@ bootstrapMarginResiduals),
  And @@ (# > 0 & /@ bootstrapMargins)
  ];

Print["round31ConvexityResiduals=", {
  cSecondResidual, kernelFactorResidual, lowerDerivativeResiduals
  }];
Print["round31KernelFactors=", {
  Factor[kernelBaseOfT], Factor[kernelFactorOfT]
  }];
Print["round31AngleMargins=", angleMargins];
Print["round31EndpointMargins=", endpointMargins];
Print["round31BootstrapMargins=", bootstrapMargins];
Print["round31RetainedShelfReplayOK=", round31RetainedShelfReplayOK];

If[! TrueQ[round31RetainedShelfReplayOK], Exit[1]];
