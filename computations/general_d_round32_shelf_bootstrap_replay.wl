(* Exact symbolic replay for the analytic part of Round 32. *)

ClearAll["Global`*"];

x0 = 219/400;
c0 = 49/40;
t0 = 11/20;

thetaMargin = Together[
   x0^3/3 + 2 x0^5/15 + 17 x0^7/315 - 33/532
   ];

psiMargin = Together[
   (35/38) (1 - x0^2/2 + x0^4/24 - x0^6/720)
    - (1 - (2/3)^2/2 + (2/3)^4/24)
   ];

angleComparisonMargin = Together[
   (c0^2 - 1)/2 - (c0^4 - 1) t0^2/24 - (424/999) t0
   ];

cubicMargin = Together[13 - c0^3 99/14];
tangentMargin = Together[(288/25) (333/106 - 2) - 13];

Clear[q, K, z];
h[z_] := ArcCos[z/K] - ArcCos[z/q];
hPrimeResidual = FullSimplify[
   D[h[z], z]
    - (1/Sqrt[q^2 - z^2] - 1/Sqrt[K^2 - z^2]),
   Assumptions -> K > q > z > 0
   ];
hSecondResidual = FullSimplify[
   D[h[z], {z, 2}]
    - z ((q^2 - z^2)^(-3/2) - (K^2 - z^2)^(-3/2)),
   Assumptions -> K > q > z > 0
   ];

Clear[p, xx, r, A, B, d, lowerScalar];
lowerScalar[p_, xx_] := (
   7/10 +
    (2/3) p^2 (3 xx - p) (A + B (xx^2 + (xx - p)^2)) -
    p/2 + d (q - xx)/2
   );

fixedMDerivativeResidual = Expand[
   D[lowerScalar[p, xx], p]
    - ((2/3) (2 p (3 xx - p) (A + B (xx^2 + (xx - p)^2))
         + p^2 (-(A + B (xx^2 + (xx - p)^2))
            + (3 xx - p) 2 B (p - xx))) - 1/2)
   ];

fixedRDerivativeResidual = Expand[
   D[lowerScalar[p, p + r], p]
    - ((2/3) (6 p (p + r) (A + B ((p + r)^2 + r^2))
         + p^2 (2 p + 3 r) 2 B (p + r)) - (1 + d)/2)
   ];

round32Margins = {
   thetaMargin,
   psiMargin,
   angleComparisonMargin,
   cubicMargin,
   tangentMargin
   };

round32ShelfBootstrapReplayOK = And[
   And @@ (# > 0 & /@ round32Margins),
   hPrimeResidual === 0,
   hSecondResidual === 0,
   fixedMDerivativeResidual === 0,
   fixedRDerivativeResidual === 0
   ];

Print["round32Margins=", InputForm[round32Margins]];
Print["round32DerivativeResiduals=",
  InputForm[{hPrimeResidual, hSecondResidual,
    fixedMDerivativeResidual, fixedRDerivativeResidual}]];
Print["round32ShelfBootstrapReplayOK=", round32ShelfBootstrapReplayOK];

If[! TrueQ[round32ShelfBootstrapReplayOK], Exit[1]];
