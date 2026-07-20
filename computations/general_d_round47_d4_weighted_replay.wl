(* Exact symbolic replay for the Round 47 d=4 launch identities. *)
ClearAll["Global`*"];

deltaCell[a_, x_] := -a/6 + a x (1 - x)/2 - x^3/6;
xstar[a_] := Sqrt[a (a + 1)] - a;
cellMinimum[a_] := a (a + 1)/(12 (a + 1/2 + Sqrt[a (a + 1)]));

checks = <|
  "L1StationaryEquation" -> FullSimplify[
    D[-deltaCell[a, x], x] /. x -> xstar[a], Assumptions -> a >= 1],
  "L1ExactMinimum" -> FullSimplify[
    -deltaCell[a, xstar[a]] - cellMinimum[a], Assumptions -> a >= 1],
  "L1StrictCoarseGap" -> FullSimplify[
    cellMinimum[a] - a/24, Assumptions -> a >= 1],
  "L3Formal" -> Expand[
    (2 ia - qa - 2 s) - (2 ia1 - qa1 - 2 (s - qa1)) -
      (2 (ia - ia1) - qa - qa1)],
  "L4Coefficient" -> FullSimplify[
    Sum[j, {j, 1, a}] - a (a + 1)/2, Assumptions -> a >= 1],
  "ComponentCoefficient" -> FullSimplify[
    Sum[j, {j, u, k}] - (k (k + 1) - (u - 1) u)/2,
    Assumptions -> k >= u >= 1]
|>;

Print[InputForm[checks]];
If[
  checks["L1StationaryEquation"] === 0 &&
  checks["L1ExactMinimum"] === 0 &&
  checks["L3Formal"] === 0 &&
  checks["L4Coefficient"] === 0 &&
  checks["ComponentCoefficient"] === 0 &&
  TrueQ[FullSimplify[checks["L1StrictCoarseGap"] > 0, Assumptions -> a >= 1]],
  Print["ROUND47_D4_SYMBOLIC_REPLAY: PASS"],
  Print["ROUND47_D4_SYMBOLIC_REPLAY: FAIL"]
];
