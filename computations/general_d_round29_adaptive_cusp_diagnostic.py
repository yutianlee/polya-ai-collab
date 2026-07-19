#!/usr/bin/env python3
"""High-precision diagnostic for the Round 29 wall--wall cusp.

The cusp is the intersection of the included lower shelf e_p=0 with the
bad side of the inverse wall y_1=2 for

    (r,p,m,f)=(1,2,2,2), q=5.

The analytic Round 29 proof does not depend on the decimal output here.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 100


def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    return radius / mp.pi * (mp.sin(theta) - theta * mp.cos(theta))


def integral(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    cosine, sine = mp.cos(theta), mp.sin(theta)
    return radius**2 / (4 * mp.pi) * (
        theta * (1 + 2 * cosine**2) - 3 * sine * cosine
    )


def projected_scalar(mu: mp.mpf, outer: mp.mpf, eta: mp.mpf) -> tuple[mp.mpf, ...]:
    r, p, m, f, q, x = map(mp.mpf, (1, 2, 2, 2, 5, 3))
    t = mp.acos(mu / outer)
    c = t / mp.pi
    d = 1 - 2 * c
    theta_1 = mp.findroot(
        lambda theta: outer / mp.pi * (mp.sin(theta) - theta * mp.cos(theta))
        - mp.mpf(3) / 4,
        (mp.mpf("0.8"), mp.mpf("0.95")),
    )
    beta = mp.acos(q / outer) / mp.pi
    v = action(outer, q)
    cap = 2 * integral(mu, q)
    terminal = mp.pi / (2 * theta_1) + 2 * eta - 1 - cap + (v - 1) ** 2 / beta

    shell_r = action(outer, r) - action(mu, r)
    shell_x = action(outer, x) - action(mu, x)
    E = shell_r + shell_x + mp.mpf(1) / 2 - 2 * f
    E_star = mp.mpf(1) / 2 - d * m / (2 * p)
    lam = f - mp.mpf(1) / 4 - action(outer, mu)
    X = mu - x
    stretch = mp.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p)))
    tau = (stretch - 1) / (stretch + 1)
    elastic = tau * (E + 2 * lam)
    curvature = (
        (mu**-1 - outer**-1) * (x**2 - r**2) / (2 * mp.pi)
        + (mu**-3 - outer**-3) * (x**4 - r**4) / (24 * mp.pi)
    )
    owner = max(elastic, curvature)
    a_p = p**2 / (3 * (2 * r + p))
    psi = max(mp.mpf(0), terminal) + a_p * owner + p * (E - E_star)
    return psi, terminal, E, E_star, elastic, curvature, lam, t, theta_1, beta, cap


def main() -> None:
    outer = mp.findroot(lambda radius: action(radius, mp.mpf(7)) - mp.mpf(3) / 4, (11, 11.1))
    mu = mp.findroot(
        lambda radius: action(outer, mp.mpf(3)) - action(radius, mp.mpf(3)) - mp.mpf(7) / 4,
        (5, 5.1),
    )
    alpha = mu - 5
    values = projected_scalar(mu, outer, mp.mpf(0))
    psi, terminal, E, E_star, elastic, curvature, lam, t, theta_1, beta, cap = values

    def inverse_face(radius: mp.mpf) -> mp.mpf:
        # K is fixed by y_1=2.  The bad-side inverse fraction is eta=0.
        return projected_scalar(radius, outer, mp.mpf(0))[0]

    def shelf_outer(radius: mp.mpf) -> mp.mpf:
        return mp.findroot(
            lambda K: action(K, mp.mpf(3)) - action(radius, mp.mpf(3)) - mp.mpf(7) / 4,
            (outer, outer + mp.mpf("0.2")),
        )

    def shelf_face(radius: mp.mpf) -> mp.mpf:
        K = shelf_outer(radius)
        theta = mp.findroot(
            lambda angle: K / mp.pi * (mp.sin(angle) - angle * mp.cos(angle))
            - mp.mpf(3) / 4,
            (mp.mpf("0.8"), mp.mpf("0.95")),
        )
        eta = K * mp.cos(theta) - 7
        return projected_scalar(radius, K, eta)[0]

    inverse_derivative = mp.diff(inverse_face, mu)
    shelf_derivative = mp.diff(shelf_face, mu, direction=1)

    print("ROUND 29 ADAPTIVE WALL--WALL CUSP (DIAGNOSTIC ONLY)")
    for name, value in (
        ("K0", outer),
        ("mu0", mu),
        ("alpha0", alpha),
        ("t0", t),
        ("theta1", theta_1),
        ("beta", beta),
        ("lambda", lam),
        ("J", cap),
        ("L_T_bad_right", terminal),
        ("E", E),
        ("E_star", E_star),
        ("elastic_projected", elastic),
        ("curvature_K4", curvature),
        ("Psi4E_LT_bad_right", psi),
        ("inverse_face_alpha_derivative", inverse_derivative),
        ("shelf_face_alpha_right_derivative", shelf_derivative),
    ):
        print(f"{name}={mp.nstr(value, 70)}")

    if not (curvature > elastic and psi > 0 and inverse_derivative < 0 < shelf_derivative):
        raise ArithmeticError("Round 29 cusp gates failed")
    print("diagnosticOnly=True")
    print("round29AdaptiveCuspReplayOK=True")


if __name__ == "__main__":
    main()
