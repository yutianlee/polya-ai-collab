#!/usr/bin/env python3
"""Round 45 focused support-sign diagnostics and directed route certificate.

The lead calculation is deliberately narrow.  It reuses the audited Round 44
exact evaluator, as Prompt A3 requests, and independently wraps the selected
count-free-route counterexample in an Arb wall bracket.  All owner inequalities,
the strict reverse of (R45-CF), the adjacent-action inequality, the direct
strict terminal count, and positivity of the unrenamed exact target

    S = D_A(q) + C_p + p (E-E_*)

are then evaluated on that same directed t interval.  The broad, independently
implemented search belongs to the separate Round 45C program.

This file makes no positive coverage claim.  The old-level aggregate is proved
symbolically in the companion Mathematica replay; its numerical checks here are
regressions only.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
from flint import arb, ctx, fmpq

import general_d_round44_independent_gate_b_search as r44


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DPS = 120
DEFAULT_ARB_BITS = 640


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def mp_text(value: Any, digits: int = 40) -> Any:
    if isinstance(value, mp.mpf):
        return mp.nstr(value, digits)
    if isinstance(value, dict):
        return {str(k): mp_text(v, digits) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [mp_text(v, digits) for v in value]
    return value


def candidate(r2: int, p: int, m: int, B: int, source: str) -> r44.FloatCandidate:
    t = r44.wall_float(r2 + 2 * (p + m), B)
    require(t is not None, f"missing wall root for {(r2, p, m, B)}")
    return r44.FloatCandidate(
        source=source,
        r2=r2,
        p=p,
        m=m,
        B=B,
        f=0,
        t=t,
        S=0.0,
        E=0.0,
        Estar=0.0,
        ep=0.0,
        activity=0.0,
        min_eta=0.0,
        max_eta=1.0,
    )


def round45_metrics(record: r44.HPRecord, dps: int = DEFAULT_DPS) -> dict[str, Any]:
    """Evaluate the exact support, adjacent-action, and aggregate ledgers."""

    with mp.workdps(dps):
        d = record.data
        r = mp.mpf(d["r"])
        x = mp.mpf(d["x"])
        q = mp.mpf(d["q"])
        mu = mp.mpf(d["mu"])
        K = mp.mpf(d["K"])
        t = mp.mpf(d["t"])
        p = mp.mpf(record.p)
        B0 = mp.mpf(d["B0"])
        beta = mp.mpf(d["beta"])
        h = mp.mpf(d["h"])
        u = mp.mpf(d["u"])
        W = mp.mpf(d["W"])
        zeta = mp.mpf(d["zeta"])
        J = mp.mpf(d["L_T_zero"]) * 0  # keep provenance explicit below
        # L_T^0 = Omega + B0*zeta + 9/(16 beta) - J.
        omega = mp.fsum(
            mp.pi / (2 * row["theta"]) - mp.pi / (2 * t) + 2 * row["eta_adverse"]
            for row in d["inverse_rows"]
        )
        J = omega + B0 * zeta + mp.mpf(9) / (16 * beta) - mp.mpf(d["L_T_zero"])

        Ur = mp.sqrt(mu * mu - r * r)
        Ux = mp.sqrt(mu * mu - x * x)
        Uq = mp.sqrt(mu * mu - q * q)
        R1 = (Ur - Ux) / (Ux - Uq)
        adjacent_rhs = R1 * (mp.mpf(d["j"]) + mp.mpf(d["ep"]) + h)
        adjacent_slack = mp.mpf(d["Delta"]) - adjacent_rhs
        action_drop = mp.mpf(d["j"]) + mp.mpf(d["ep"]) + h

        top = mp.mpf(9) / (64 * mp.pi * mp.sqrt(K * K - q * q) * beta**3)
        Ccurv = mp.mpf(d["curvature_reserve"])
        deficit = mp.mpf(d["p_Estar_minus_E"])
        half_loss = (p - mp.mpf(d["d"]) * record.m) / 2
        rhs30 = omega + B0 * zeta + mp.mpf(9) / (16 * beta) - J + top + Ccurv
        rhs31 = mp.mpf(49) / 40 + top + Ccurv
        M30 = deficit - rhs30
        M31 = deficit - rhs31
        cf_signed = p * R1 * h + rhs31 - half_loss

        c_old = mp.pi**2 / (K * t**3 * mp.sin(t))
        sum_delta = B0 * (B0 + 1) / 2 - B0 * u
        omega_primary = c_old * sum_delta / 2
        old_bregman_lower = mp.mpf(7) * c_old * B0 / 48
        omega_old_combined = c_old * B0 * (W / 2 - B0 / 4 + mp.mpf(1) / 48)
        combined_identity_residual = (
            omega_primary + old_bregman_lower - omega_old_combined
        )
        terminal_rhs = (
            omega_old_combined
            + B0 * zeta
            + mp.mpf(9) / (16 * beta)
            - J
            + top
            + Ccurv
        )
        terminal_adjacent_signed = p * R1 * h + terminal_rhs - half_loss
        terminal_action_drop_signed = p * R1 * action_drop + terminal_rhs - half_loss
        support_slack_identity_residual = (
            mp.mpf(d["S"])
            - (
                -M30
                + (mp.mpf(d["R_tan_zero"]) - top)
                + (mp.mpf(d["C_p"]) - Ccurv)
            )
        )

        return {
            "R1": +R1,
            "adjacent_rhs": +adjacent_rhs,
            "adjacent_slack": +adjacent_slack,
            "A_x_minus_A_q": +action_drop,
            "Omega_exact": +omega,
            "Omega_primary": +omega_primary,
            "Omega_primary_slack": +(omega - omega_primary),
            "top_bregman_lower": +top,
            "C_curv": +Ccurv,
            "deficit": +deficit,
            "RHS_S30": +rhs30,
            "RHS_S31": +rhs31,
            "M30": +M30,
            "M31": +M31,
            "CF_signed_RHS_minus_LHS": +cf_signed,
            "c_old": +c_old,
            "old_bregman_aggregate_lower": +old_bregman_lower,
            "Omega_plus_old_combined_lower": +omega_old_combined,
            "combined_identity_residual": +combined_identity_residual,
            "Rtan0_minus_old_and_top_lower": +(
                mp.mpf(d["R_tan_zero"]) - old_bregman_lower - top
            ),
            "remaining_terminal_RHS": +terminal_rhs,
            "remaining_terminal_adjacent_signed": +terminal_adjacent_signed,
            "remaining_terminal_action_drop_signed": +terminal_action_drop_signed,
            "support_slack_identity_residual": +support_slack_identity_residual,
        }


def exact_decimal_q(value: mp.mpf, digits: int, lower: bool) -> fmpq:
    scale = 10**digits
    scaled = value * scale
    integer = int(mp.floor(scaled) if lower else mp.ceil(scaled))
    return fmpq(integer, scale)


def arb_shell_action(K: arb, mu: fmpq, z: fmpq) -> arb:
    outer = r44.arb_ball_action(K, z) if K > arb(z) else arb(0)
    inner = r44.arb_ball_action(arb(mu), z) if arb(mu) > arb(z) else arb(0)
    return outer - inner


def arb_shell_cap(K: arb, mu: fmpq, z: fmpq) -> arb:
    outer = r44.arb_ball_cap(K, z) if K > arb(z) else arb(0)
    inner = r44.arb_ball_cap(arb(mu), z) if arb(mu) > arb(z) else arb(0)
    return outer - inner


def strict_cell(value: arb, proposed: int, label: str) -> int:
    """Certify value lies strictly inside its proposed strict-floor cell."""

    require(value > proposed, f"{label}: lower strict cell face unresolved: {value}")
    require(value < proposed + 1, f"{label}: upper strict cell face unresolved: {value}")
    return proposed


def directed_route_certificate(record: r44.HPRecord, digits: int = 82) -> dict[str, Any]:
    """Directed exact-owner and sign certificate for the R45-CF failure.

    The root is unique because d/dt G_{mu sec t}(q) is strictly positive:

      (sqrt(K^2-q^2)/(pi K)) * K tan(t) > 0.

    Consequently every expression evaluated on the rational t hull contains
    its exact outer-wall value.
    """

    require(record.key == (2, 6, 11, 19), "unexpected directed fixture")
    ctx.prec = DEFAULT_ARB_BITS
    r2, p, m, B = record.r2, record.p, record.m, record.B
    r_q = fmpq(r2, 2)
    x_q = r_q + p
    q_q = x_q + m
    mu_q = q_q + 1
    B0 = B - 1
    f = int(record.data["f"])
    j = f - B

    lo_q = exact_decimal_q(mp.mpf(record.data["t"]), digits, True)
    hi_q = exact_decimal_q(mp.mpf(record.data["t"]), digits, False)
    if lo_q == hi_q:
        hi_q += fmpq(1, 10**digits)

    def wall_residual(tq: fmpq) -> arb:
        tt = arb(tq)
        KK = arb(mu_q) / tt.cos()
        return r44.arb_ball_action(KK, q_q) - (fmpq(B) - fmpq(1, 4))

    F_lo = wall_residual(lo_q)
    F_hi = wall_residual(hi_q)
    require(F_lo < 0 < F_hi, "directed outer-wall bracket failed")
    t = arb(lo_q).union(arb(hi_q))
    pi = arb.pi()
    K = arb(mu_q) / t.cos()
    d = 1 - 2 * t / pi
    zeta = pi / (2 * t) - 1

    Ar = arb_shell_action(K, mu_q, r_q)
    Ax = arb_shell_action(K, mu_q, x_q)
    Ax1 = arb_shell_action(K, mu_q, x_q + 1)
    Aq = arb_shell_action(K, mu_q, q_q)
    sr, sx, sx1 = Ar + fmpq(1, 4), Ax + fmpq(1, 4), Ax1 + fmpq(1, 4)
    strict_cell(sr, f, "A(r)+1/4")
    strict_cell(sx, f, "A(x)+1/4")
    require(sx1 < f, "literal first drop is not strictly below the common shelf")
    require(sx1 > f - 1, "literal first drop skips more than one shelf")
    strict_cell(Aq + fmpq(1, 4), B0, "A(q)+1/4")

    e0, ep = sr - f, sx - f
    E = e0 + ep
    Delta = e0 - ep
    Estar = (p - d * m) / (2 * p)
    p_minus_dm = p - d * m
    require(E > 0, "E lower owner face unresolved")
    require(E < Estar, "E<E* not directed")
    require(Estar < fmpq(1, 2), "E*<1/2 not directed")
    require(p_minus_dm > fmpq(11, 5), "p-dm>11/5 not directed")

    h = r44.arb_ball_action(arb(mu_q), q_q)
    v = fmpq(B) - fmpq(1, 4)
    W = r44.arb_ball_action(K, mu_q)
    u = v - W
    beta = (arb(q_q) / K).acos() / pi
    require(h > 0, "h>0 unresolved")
    require(h < u, "h<u unresolved")
    require(u < beta, "u<beta unresolved")
    require(beta < fmpq(1, 2), "beta<1/2 unresolved")
    activity = K * K - pi * pi / (1 - t.cos()) ** 2 - fmpq(3, 4)
    require(activity > 0, "D=4 activity is not strict")

    Ur = (arb(mu_q * mu_q - r_q * r_q)).sqrt()
    Ux = (arb(mu_q * mu_q - x_q * x_q)).sqrt()
    Uq = (arb(mu_q * mu_q - q_q * q_q)).sqrt()
    R1 = (Ur - Ux) / (Ux - Uq)
    adjacent_slack = Delta - R1 * (j + ep + h)
    action_drop = Ax - Aq
    action_drop_identity_residual = action_drop - (j + ep + h)
    require(R1 > 0, "R1>0 unresolved")
    require(adjacent_slack > 0, "adjacent-action inequality not directed")
    require(action_drop_identity_residual.contains(0), "A(x)-A(q) action-drop identity")

    top = fmpq(9, 64) / (pi * (K * K - q_q * q_q).sqrt() * beta**3)
    Ccurv = fmpq(p**3, 6) / pi * (
        1 / arb(mu_q * mu_q - r_q * r_q).sqrt()
        - 1 / (K * K - r_q * r_q).sqrt()
    )
    half_loss = (p - d * m) / 2
    cf_signed = p * R1 * h + fmpq(49, 40) + top + Ccurv - half_loss
    require(cf_signed < 0, "strict reverse of R45-CF not directed")

    # Direct strict terminal count, with every spatial cell certified.
    endpoint_count = B0
    spatial_counts: list[dict[str, Any]] = []
    spatial_sum = 0
    K_upper = float(K.upper())
    max_shift = int(math.ceil(K_upper - float(str(q_q)))) + 2
    for shift in range(1, max_shift + 1):
        z_q = q_q + shift
        if K < arb(z_q):
            G = arb(0)
        else:
            require(K > arb(z_q), f"turning wall unresolved at shift {shift}")
            G = r44.arb_ball_action(K, z_q)
        midpoint = mp.mpf(record.data["K"])
        z_mp = mp.mpf(str(z_q))
        proposal = 0 if z_mp >= midpoint else int(
            mp.floor(r44.ball_action(midpoint, z_mp) + mp.mpf(1) / 4)
        )
        strict_cell(G + fmpq(1, 4), proposal, f"terminal shift {shift}")
        spatial_sum += proposal
        if proposal or shift <= 3 or shift >= max_shift - 1:
            spatial_counts.append({"shift": shift, "count": proposal, "cell": str(G + fmpq(1, 4))})
    terminal_count = endpoint_count + 2 * spatial_sum

    Dq = 2 * arb_shell_cap(K, mu_q, q_q) - terminal_count
    Cp = 2 * (arb_shell_cap(K, mu_q, r_q) - arb_shell_cap(K, mu_q, x_q)) - p * (Ar + Ax)
    S = Dq + Cp + p * (E - Estar)
    require(S > 0, "exact S positivity not directed")

    # The exact old-inverse side vector is interior: for each selected level,
    # certify q+n < Y(level)+q < q+n+1 by the decreasing action inequalities.
    side_cells: list[dict[str, Any]] = []
    for row in record.data["inverse_rows"]:
        level = fmpq(int(row["k"])) - fmpq(1, 4)
        n = int(row["count_adverse"])
        left = r44.arb_ball_action(K, q_q + n)
        if K < arb(q_q + n + 1):
            right = arb(0)
        else:
            require(K > arb(q_q + n + 1), f"old inverse turning wall unresolved for k={row['k']}")
            right = r44.arb_ball_action(K, q_q + n + 1)
        require(left > level, f"old inverse left side unresolved for k={row['k']}")
        require(right < level, f"old inverse right side unresolved for k={row['k']}")
        side_cells.append({"k": int(row["k"]), "spatial_cell": [n, n + 1], "side": "interior"})

    # Directed support exclusions and the strengthened aggregate terminal
    # diagnostic.  omega_primary is a proved lower bound, not an exact omega.
    deficit = p * (Estar - E)
    rhs31 = fmpq(49, 40) + top + Ccurv
    M31 = deficit - rhs31
    require(M31 < 0, "candidate unexpectedly enters S31 support")
    sum_delta = B0 * (B0 + 1) / 2 - B0 * u
    c_old = pi * pi / (K * t**3 * t.sin())
    omega_primary = c_old * sum_delta / 2
    old_bregman_lower = fmpq(7 * B0, 48) * c_old
    combined = c_old * B0 * (W / 2 - fmpq(B0, 4) + fmpq(1, 48))
    combine_residual = omega_primary + old_bregman_lower - combined
    require(combine_residual.contains(0), "combined aggregate algebra lost zero")
    J = 2 * r44.arb_ball_cap(arb(mu_q), q_q)
    top_phase_curv = B0 * zeta + fmpq(9, 16) / beta - J + top + Ccurv
    M30_upper = deficit - (omega_primary + top_phase_curv)
    require(M30_upper < 0, "candidate not directed outside S30 using Omega lower bound")
    remaining_signed = p * R1 * h + combined + top_phase_curv - half_loss
    remaining_action_drop_signed = p * R1 * action_drop + combined + top_phase_curv - half_loss
    require(remaining_signed > 0, "strengthened aggregate regression changed sign")
    require(remaining_action_drop_signed > remaining_signed, "action-drop strengthening changed order")

    return {
        "classification": "count_free_route_counterexample_only",
        "directed": True,
        "arb_bits": ctx.prec,
        "tuple": {"D": 4, "grid": "integer", "r": "1", "p": p, "m": m, "f": f, "B": B, "B0": B0, "j": j},
        "wall": {"t_lo": str(lo_q), "t_hi": str(hi_q), "F_lo": str(F_lo), "F_hi": str(F_hi), "unique_by_positive_derivative": True},
        "owner": {
            "p_minus_dm": str(p_minus_dm),
            "E": str(E),
            "E_star": str(Estar),
            "activity": str(activity),
            "h": str(h),
            "u": str(u),
            "beta": str(beta),
            "adjacent_slack": str(adjacent_slack),
            "A_x_minus_A_q": str(action_drop),
            "action_drop_identity_residual": str(action_drop_identity_residual),
            "old_inverse_side_vector": side_cells,
        },
        "route": {
            "CF_signed_RHS_minus_LHS": str(cf_signed),
            "M31": str(M31),
            "M30_upper_using_primary_Omega_lower": str(M30_upper),
        },
        "exact_target": {
            "terminal_count": terminal_count,
            "selected_terminal_cells": spatial_counts,
            "D_A": str(Dq),
            "C_p": str(Cp),
            "S": str(S),
        },
        "fallback": {
            "Omega_primary": str(omega_primary),
            "old_bregman_aggregate_lower": str(old_bregman_lower),
            "Omega_plus_old_combined": str(combined),
            "combined_identity_residual": str(combine_residual),
            "remaining_terminal_adjacent_signed": str(remaining_signed),
            "remaining_terminal_action_drop_signed": str(remaining_action_drop_signed),
        },
    }


def regression_payload(dps: int) -> dict[str, Any]:
    round44_min = r44.evaluate_hp(candidate(2, 3, 1, 2, "round44-minimum"), dps)
    require(round44_min.owner, f"Round44 minimum owner failed: {round44_min.reasons}")
    min_metrics = round45_metrics(round44_min, dps)
    require(abs(round44_min.S - mp.mpf("2.69456527890035502562933")) < mp.mpf("1e-22"), "Round44 S regression")
    require(min_metrics["M30"] < 0 and min_metrics["M31"] < 0, "Round44 support regression")

    round43 = r44.evaluate_hp(r44.round43_candidate(dps), dps)
    require(not round43.owner, "Round43 rejected tuple became an owner")
    require(round43.data["E"] > round43.data["Estar"], "Round43 E>E* regression")

    round27_hp = r44.round27_regression(dps)
    round27_arb = r44.round27_arb_check()
    require(round27_hp["negative_rejected_scalars"], "Round27 projected-scalar signs")
    require(round27_hp["S"] > 47, "Round27 positive exact S")

    # The coefficients are algebraic and independently replayed in WL; these
    # numerical assertions protect against a transcription regression.
    beta = mp.mpf(round44_min.data["beta"])
    reconciliation = mp.mpf(round44_min.data["R_tan_plus"]) - mp.mpf(round44_min.data["R_tan_zero"])
    require(abs(reconciliation - 1 / (16 * beta)) < mp.mpf("1e-90"), "1/(16 beta) reconciliation")
    K, q = mp.mpf(round44_min.data["K"]), mp.mpf(round44_min.data["q"])
    top = mp.mpf(9) / (64 * mp.pi * mp.sqrt(K * K - q * q) * beta**3)
    require(top > 0, "9/64 top-Bregman coefficient")

    return {
        "round44_minimum": {
            "tuple": [1, 3, 1, 2, 2, 0],
            "S": round44_min.S,
            "M30": min_metrics["M30"],
            "M31": min_metrics["M31"],
            "Omega_primary_slack": min_metrics["Omega_primary_slack"],
            "adjacent_slack": min_metrics["adjacent_slack"],
            "Rtan0_minus_old_and_top_lower": min_metrics["Rtan0_minus_old_and_top_lower"],
        },
        "round43_rejected": {
            "tuple": [1, 9, 9, 4, 3, 1],
            "owner": round43.owner,
            "reasons": round43.reasons,
            "E": round43.data["E"],
            "E_star": round43.data["Estar"],
            "S_diagnostic_only": round43.S,
        },
        "round27_automatic": {"high_precision": round27_hp, "directed": round27_arb},
        "terminal_coefficients": {
            "Rtan_plus_minus_Rtan_zero": reconciliation,
            "one_over_16beta": 1 / (16 * beta),
            "top_9_over_64_value": top,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--json", type=Path, default=None, help="optional JSON output path")
    args = parser.parse_args()
    mp.mp.dps = args.dps

    route = r44.evaluate_hp(candidate(2, 6, 11, 19, "round45-focused-CF"), args.dps)
    require(route.owner, f"focused route candidate is not an owner: {route.reasons}")
    route_metrics = round45_metrics(route, args.dps)
    require(route_metrics["CF_signed_RHS_minus_LHS"] < 0, "high-precision R45-CF reverse missing")
    require(route.S > 0, "focused route fixture should have positive exact S")
    require(route_metrics["adjacent_slack"] > 0, "adjacent-action regression")
    require(route_metrics["Omega_primary_slack"] > 0, "primary Omega bound regression")
    require(route_metrics["Rtan0_minus_old_and_top_lower"] > 0, "old/top Bregman aggregate regression")
    require(
        abs(route_metrics["support_slack_identity_residual"]) < mp.mpf("1e-90"),
        "exact S30 support-slack identity",
    )

    alpha_rows = []
    for exponent in (6, 12, 18):
        alpha = mp.mpf(1) - mp.power(10, -exponent)
        rec = r44.evaluate_hp(candidate(2, 6, 11, 19, f"alpha-{exponent}"), args.dps, alpha=alpha)
        met = round45_metrics(rec, args.dps)
        alpha_rows.append({
            "alpha": alpha,
            "owner": rec.owner,
            "reasons": rec.reasons,
            "S": rec.S,
            "CF_signed_RHS_minus_LHS": met["CF_signed_RHS_minus_LHS"],
        })

    payload = {
        "program": "general_d_round45_support_sign_diagnostic.py",
        "scope": "focused diagnostics; no positive coverage certificate",
        "route_high_precision": {
            "tuple": {"r2": route.r2, "p": route.p, "m": route.m, "B": route.B, "f": route.data["f"], "j": route.data["j"]},
            "owner": route.owner,
            "S": route.S,
            "metrics": route_metrics,
        },
        "route_directed_certificate": directed_route_certificate(route),
        "one_sided_alpha_diagnostics": alpha_rows,
        "regressions": regression_payload(args.dps),
        "classification": "R45-CF is falsified only as a sufficient route; exact S remains positive and Gate B remains open",
    }
    serializable = mp_text(payload)
    output = json.dumps(serializable, indent=2, sort_keys=True)
    print(output)
    if args.json is not None:
        args.json.write_text(output + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
