(* Exact symbolic replay for Round 37.  This is not a sign certificate. *)

ClearAll["Global`*"];

assumptions =
  0 < t < Pi/2 && p > 0 && r > 0 && m > 0 && alpha >= 0 &&
   alpha < 1 && lambda > 0 && stretch > 1 && a > 0 &&
   M4 >= 0 && Esum >= M4 && B0 >= 0 && n >= 0 &&
   0 <= j <= n && 0 <= delta < 1 && ep >= 0;

c = t/Pi;
d = 1 - 2 c;
zeta = d/(2 c);
g = stretch - 1;
tau = g/(g + 2);
eStar = (p - d m)/(2 p);
eMin = g lambda;

angleIdentity = FullSimplify[
   Pi/(2 t) - 1 == zeta,
   Assumptions -> assumptions
   ];

elasticSolveIdentity = FullSimplify[
   eMin (1 - tau) == 2 tau lambda,
   Assumptions -> assumptions
   ];

tauEndpointIdentity = FullSimplify[
   tau (stretch + 1) == stretch - 1,
   Assumptions -> assumptions
   ];

shelfProjectionIdentity = FullSimplify[
   a tau (eMin + 2 lambda) + p eMin ==
    (p + a) g lambda,
   Assumptions -> assumptions
   ];

hardRewriteIdentity = FullSimplify[
   p (Esum - eStar) == p Esum - (p - d m)/2,
   Assumptions -> assumptions
   ];

actionDeficitIdentity = FullSimplify[
   (f - j - 1) == B - 1,
   Assumptions -> B == f - j
   ];

xiShelfIdentity = FullSimplify[
   a M4 + p Esum == (p + a) M4 + p Xi,
   Assumptions -> assumptions && Xi == Esum - M4
   ];

inverseNormalFormIdentity = FullSimplify[
   U == B0 zeta + omega,
   Assumptions -> U == B0 zeta + omega
   ];

gammaNormalFormIdentity = FullSimplify[
   (1 - J + U + a M4 + p (Esum - eStar)) ==
    (1 - J + B0 zeta + omega +
      (p + a) M4 + p Xi - (p - d m)/2),
   Assumptions ->
    assumptions && U == B0 zeta + omega && Xi == Esum - M4
   ];

sawtoothIdentity = FullSimplify[
   (n - j) zeta + A (j + delta + ep) ==
    n zeta + j (A - zeta) + A (delta + ep),
   Assumptions -> assumptions && A > 0
   ];

sawtoothUpperBranch = FullSimplify[
   (n - j) zeta + A (j + delta + ep) >=
    n zeta + A (delta + ep),
   Assumptions -> assumptions && A >= zeta && zeta > 0
   ];

sawtoothLowerBranch = FullSimplify[
   (n - j) zeta + A (j + delta + ep) >=
    n A + A (delta + ep),
   Assumptions -> assumptions && 0 < A < zeta
   ];

terminalRemainderIdentity = FullSimplify[
   (f - 1/4 + ep) - (Q - 1/4 + xi) ==
    j + 1 + ep - xi,
   Assumptions -> Q == f - j - 1
   ];

phiEndpointIdentity = FullSimplify[
   (LT + a Delta + p (Esum - eStar)) ==
    (LT + (p + a) Delta + 2 p ep - (p - d m)/2),
   Assumptions -> assumptions && Esum == Delta + 2 ep
   ];

gammaValue =
  1 - J + B0 zeta + omega +
   (p + a) M4 + p Xi - (p - d m)/2;

failureRight =
  2 (1 - J) + 2 B0 zeta + 2 omega +
   2 (p + a) M4 + 2 p Xi;

failureIdentity = FullSimplify[
   gammaValue == (failureRight - (p - d m))/2,
   Assumptions -> assumptions
   ];

Print["angleIdentity=", angleIdentity];
Print["elasticSolveIdentity=", elasticSolveIdentity];
Print["tauEndpointIdentity=", tauEndpointIdentity];
Print["shelfProjectionIdentity=", shelfProjectionIdentity];
Print["hardRewriteIdentity=", hardRewriteIdentity];
Print["actionDeficitIdentity=", actionDeficitIdentity];
Print["xiShelfIdentity=", xiShelfIdentity];
Print["inverseNormalFormIdentity=", inverseNormalFormIdentity];
Print["gammaNormalFormIdentity=", gammaNormalFormIdentity];
Print["sawtoothIdentity=", sawtoothIdentity];
Print["sawtoothUpperBranch=", sawtoothUpperBranch];
Print["sawtoothLowerBranch=", sawtoothLowerBranch];
Print["terminalRemainderIdentity=", terminalRemainderIdentity];
Print["phiEndpointIdentity=", phiEndpointIdentity];
Print["failureIdentity=", failureIdentity];

round37GapInterfaceReplayOK = And[
   angleIdentity,
   elasticSolveIdentity,
   tauEndpointIdentity,
   shelfProjectionIdentity,
   hardRewriteIdentity,
   actionDeficitIdentity,
   xiShelfIdentity,
   inverseNormalFormIdentity,
   gammaNormalFormIdentity,
   sawtoothIdentity,
   sawtoothUpperBranch,
   sawtoothLowerBranch,
   terminalRemainderIdentity,
   phiEndpointIdentity,
   failureIdentity
   ];

Print["round37GapInterfaceReplayOK=", round37GapInterfaceReplayOK];
