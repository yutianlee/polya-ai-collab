(* Round 41 scratch replay for the Round 40 reduced scalar.

   This file does not promote a theorem and does not own any strict wall or
   endpoint label.  It packages the final rational two-variable obstruction
   into one exact real-algebraic emptiness query. *)

ClearAll["Global`*"];

(* Put s=2t/Pi=1-d.  The analytic input is

     ellMinus < L0(t) < ellPlus,
     Aminus < (1-Cos[t])/Pi,
     2+Sin[t]^2 < Splus.

   The lower L0 bound follows from the first positive term in the partial
   fraction expansion of Tan[Pi s/2]-Pi s/2.  The upper L0 bound is the
   Round 40 tangent majorant.  The Aminus and Splus bounds use the displayed
   fourth- and fifth-order Taylor inequalities together with
   333/106 < Pi < 22/7. *)

d = 1 - s;
ellMinus = 49 s^3/(121 (1 - s^2));
ellPlus = 121 s^3/(294 (1 - s^2));

Aminus = 333 s^2/848 - 1331 s^4/16464;
tUpper = 11 s/7;
sinUpper = tUpper - tUpper^3/6 + tUpper^5/120;
Splus = 2 + sinUpper^2;

(* Branch I. *)

aLowerI = d (p + 2)/(2 (p + d (p + 2)));
aUpperI = 2 (p + 2) ellPlus/5;
HminusI = 2 d + 49 s^2/(121 (1 + s));
XminusI = (p + 2) HminusI/8;
DplusI = Splus - 2 aLowerI;

cI = 9/10 + 9 d/(16 s) - p (2 - s)/2 - d;

(* If a0=Sqrt[XminusI/YminusI] lies below aUpperI, AM--GM is
   the lower envelope.  Otherwise the envelope is evaluated at aUpperI.
   Squaring only quantities whose signs are printed in the analytic
   argument gives the following rational polynomial tests. *)

criticalI = Together[
  p^4 Aminus^2 aUpperI^4 - XminusI^2 DplusI
];

polyIA = Together[
  16 XminusI^2 p^4 Aminus^2 - cI^4 DplusI
];

eI = Together[cI + XminusI/aUpperI];

polyIB = Together[
  p^4 Aminus^2 aUpperI^2 - eI^2 DplusI
];

baseI =
  0 < s < 1 && p >= 3 && aLowerI < aUpperI;

counterI = baseI && (
  (criticalI >= 0 && cI < 0 && polyIA <= 0) ||
  (criticalI <= 0 && eI < 0 && polyIB <= 0)
);

(* Branch II.  Both the geometric lower wall and the hard p>d m wall
   give lower bounds for a.  Their maximum is represented by two ordinary
   algebraic ownership alternatives. *)

aGeomII = 4 ellMinus (p/2 + 1)/5;
aHardII = 1 -
  4 ellPlus (p (1 + d/2) + d)/(5 d);

MminusII = 5 d/(8 ellPlus);
cII = 9/10 + 7 d/(8 s) - p (3 - s)/4 - d/2;

baseII =
  0 < s < 1 && p >= 3 && (p + 3) ellMinus < 5/4;

counterII = False;

Do[
  bII = If[index == 1, aGeomII, aHardII];
  ownsII = If[index == 1, aGeomII >= aHardII, aHardII >= aGeomII];
  DplusII = Splus - 2 bII;

  slopeII = Together[
    p^4 Aminus^2 - MminusII^2 DplusII
  ];

  eII = Together[cII + MminusII (1 - bII)];

  polyIIA = Together[
    p^4 Aminus^2 bII^2 - eII^2 DplusII
  ];

  polyIIB = Together[
    p^4 Aminus^2 - cII^2 DplusII
  ];

  counterII = counterII || (
    baseII && ownsII && 0 < bII < 1 && (
      (slopeII >= 0 && eII < 0 && polyIIA <= 0) ||
      (slopeII <= 0 && cII < 0 && polyIIB <= 0)
    )
  ),
  {index, 1, 2}
];

Print["branchICounterDegrees=", {
  Exponent[Numerator[criticalI], {s, p}],
  Exponent[Numerator[polyIA], {s, p}],
  Exponent[Numerator[polyIB], {s, p}]
}];

(* This is deliberately one combined exact elimination. *)
round41RationalCounterexampleSystem = FullSimplify[
  Resolve[
    Exists[{s, p}, counterI || counterII],
    Reals
  ]
];

Print[
  "round41RationalCounterexampleSystem=",
  round41RationalCounterexampleSystem
];
Print[
  "round41RationalObstructionReplayOK=",
  round41RationalCounterexampleSystem === False
];
