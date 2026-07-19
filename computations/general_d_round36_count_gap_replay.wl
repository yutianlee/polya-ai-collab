(* Exact symbolic replay for General-d Round 36. *)

ClearAll["Global`*"];

G[R_, z_] := (Sqrt[R^2 - z^2] - z ArcCos[z/R])/Pi;

checks = <||>;

checks["zDerivative"] =
  FullSimplify[
    D[G[R, z], z] + ArcCos[z/R]/Pi,
    Assumptions -> 0 < z < R
  ] === 0;

checks["radiusDerivative"] =
  FullSimplify[
    D[G[R, z], R] - Sqrt[1 - z^2/R^2]/Pi,
    Assumptions -> 0 < z < R
  ] === 0;

checks["zConvexityIdentity"] =
  FullSimplify[
    D[G[R, z], {z, 2}] - 1/(Pi Sqrt[R^2 - z^2]),
    Assumptions -> 0 < z < R
  ] === 0;

checks["capIntegral"] =
  FullSimplify[
    Integrate[ArcCos[z/mu]/Pi, {z, q, mu},
      Assumptions -> 0 < q < mu] - G[mu, q],
    Assumptions -> 0 < q < mu
  ] === 0;

checks["outerInverseIntegral"] =
  FullSimplify[
    Integrate[ArcCos[z/K]/Pi, {z, q, q + y},
      Assumptions -> 0 < q < q + y < K] -
      (G[K, q] - G[K, q + y]),
    Assumptions -> 0 < q < q + y < K
  ] === 0;

strictBracket[x_] := Ceiling[x] - 1;

checks["outerWallLiteralOwnership"] =
  FullSimplify[
    {strictBracket[n], strictBracket[n - h]} == {n - 1, n - 1},
    Assumptions -> Element[n, Integers] && 0 < h < 1/4
  ] === True;

checks["outerWallBadOwnership"] =
  FullSimplify[
    {strictBracket[n + eps], strictBracket[n - h + eps]} == {n, n - 1},
    Assumptions -> Element[n, Integers] && 0 < eps < h < 1/4
  ] === True;

checks["qWallLiteralOwnership"] =
  FullSimplify[
    {strictBracket[n + h], strictBracket[n]} == {n, n - 1},
    Assumptions -> Element[n, Integers] && 0 < h < 1/4
  ] === True;

checks["qWallBadOwnership"] =
  FullSimplify[
    {strictBracket[n + h + eps], strictBracket[n + eps]} == {n, n},
    Assumptions ->
      Element[n, Integers] && 0 < h < 1/4 && 0 < eps < 1/4 - h
  ] === True;

checks["countGapNoJumpBranch"] =
  FullSimplify[
    strictBracket[n + u + h] - strictBracket[n + u] == 0,
    Assumptions ->
      Element[n, Integers] && 0 < u <= 1 && 0 <= h < 1/4 && u + h <= 1
  ] === True;

checks["countGapOneJumpBranch"] =
  FullSimplify[
    strictBracket[n + u + h] - strictBracket[n + u] == 1,
    Assumptions ->
      Element[n, Integers] && 0 < u <= 1 && 0 <= h < 1/4 && u + h > 1
  ] === True;

checks["alphaZeroLiteralOwnership"] =
  FullSimplify[
    {strictBracket[n], strictBracket[n]} == {n - 1, n - 1},
    Assumptions -> Element[n, Integers]
  ] === True;

checks["alphaZeroBadOwnership"] =
  FullSimplify[
    {strictBracket[n + eps], strictBracket[n + eps]} == {n, n},
    Assumptions -> Element[n, Integers] && 0 < eps < 1
  ] === True;

checks["inverseMapPreCollision"] =
  FullSimplify[
    strictBracket[n + xi - h] == n,
    Assumptions ->
      Element[n, Integers] && 0 <= h < xi < 1
  ] === True;

checks["inverseMapLiteralCollision"] =
  FullSimplify[
    strictBracket[n + xi - h] == n - 1,
    Assumptions -> Element[n, Integers] && 0 < h == xi < 1/4
  ] === True;

checks["inverseMapPostCollision"] =
  FullSimplify[
    strictBracket[n + xi - h] == n - 1,
    Assumptions ->
      Element[n, Integers] && 0 < xi < h < 1/4
  ] === True;

gapRaw = sumU + 2 sumEta - (n - 1) - J + top;
gapCorrelated = 1 - J + (sumU - n + 2 sumEta) + top;
checks["gapRewrite"] = FullSimplify[gapRaw - gapCorrelated] === 0;

equalRaw = sumU + 2 sumEta - n - J;
equalCorrelated = -J + (sumU - n + 2 sumEta);
checks["equalRewrite"] = FullSimplify[equalRaw - equalCorrelated] === 0;

checks["outerBJump"] =
  FullSimplify[1/(2 beta) - 9/(16 beta) + 1/(16 beta),
    Assumptions -> beta > 0] === 0;

checks["combinedBQJump"] =
  FullSimplify[1/(2 beta) - 9/(16 beta) - 1 - (-1 - 1/(16 beta)),
    Assumptions -> beta > 0] === 0;

checks["isolatedQJump"] = FullSimplify[-n - (-(n - 1))] === -1;

checks["inverseJump"] = FullSimplify[2 (0 - 1)] === -2;

checks["outerBCollisionActionGap"] =
  FullSimplify[(n - 1/4) - (k - 1/4) - (n - k)] === 0;

checks["qCollisionActionGap"] =
  FullSimplify[(n - 1/4 + h) - (k - 1/4) - (n - k + h)] === 0;

checks["hardShelfIdentity"] =
  FullSimplify[
    p (E - (1/2 - d m/(2 p))) - (p E - (p - d m)/2),
    Assumptions -> p > 0
  ] === 0;

checks["capMargin"] = FullSimplify[1 - 1/7 - 6/7] === 0;

checks["gapThreshold"] =
  FullSimplify[
    6/7 - delta/2 /. delta -> 12/7
  ] === 0;

checks["qWallReserve"] =
  FullSimplify[
    2 y - J > 3 h,
    Assumptions -> h > 0 && y > 2 h && J < h
  ] === True;

checks["capQuarterInputs"] =
  FullSimplify[
    q/(q + 1) >= 3/4 && 3/4 > Cos[Pi/4],
    Assumptions -> q >= 3
  ] === True;

checks["collisionBandArithmetic"] =
  FullSimplify[2 (n - k) + 1 >= 3,
    Assumptions -> Element[{n, k}, Integers] && n >= 1 && 1 <= k < n
  ] === True;

checks["collisionIntegerImplication"] =
  FullSimplify[
    Implies[j > 2 (n - k), j >= 2 (n - k) + 1],
    Assumptions -> Element[{j, n, k}, Integers]
  ] === True;

Scan[(Print[#1, "=", checks[#1]]) &, Keys[checks]];

round36CountGapReplayOK = And @@ Values[checks];
Print["round36CountGapReplayOK=", round36CountGapReplayOK];

If[! TrueQ[round36CountGapReplayOK], Exit[1]];
