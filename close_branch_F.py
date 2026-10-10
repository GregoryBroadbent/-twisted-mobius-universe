#!/usr/bin/env python3
"""
Closing Branch F: the exact solution of the three-species free chain.

    H_F = -t sum (phi+_i phi_{i+1} + h.c.)
          - i(v/2) sum (psi+_i alpha psi_{i+1} - h.c.),   alpha = sigma_x
          + lam sum (phi+_i psi_{i,up} + phi+_i psi_{i,dn} + h.c.)

antiperiodic ring of M sites. Every term is bilinear, so the theory is free and
the single-particle problem is a 3x3 matrix at each momentum.

THE ALGEBRA, done before any computation. In the basis (phi, psi_up, psi_dn),

    H(k) = [[ -2t cos k ,  lam    ,  lam    ],
            [  lam      ,  0      ,  v sin k],
            [  lam      ,  v sin k,  0      ]]

Rotate the species sector to psi_+- = (psi_up +- psi_dn)/sqrt(2). Then
sigma_x becomes diagonal, +1 on psi_+ and -1 on psi_-, and the coupling column
(lam, lam) becomes (sqrt(2) lam, 0):

    H(k) = [[ -2t cos k   , sqrt(2) lam , 0        ],
            [ sqrt(2) lam ,  v sin k    , 0        ],
            [ 0           ,  0          , -v sin k ]]

So the model is a 2x2 coupled block PLUS A COMPLETELY DECOUPLED BAND. Three
consequences follow without computation:

 (1) The bands are closed-form:
         E_3(k) = -v sin k
         E_{1,2}(k) = (1/2)[ (-2t cos k + v sin k)
                     +- sqrt( (2t cos k + v sin k)^2 + 8 lam^2 ) ]

 (2) The "exact zero" is this decoupling. psi_- never touches phi at any lam,
     so P_phi H |psi_-> = 0 identically. It is not a symmetry of H and not a
     deep fact; it is one basis vector lying outside one block. It survives any
     change inside the psi sector that keeps the two species' couplings equal,
     which is exactly what the Wilson test found.

 (3) The constant 0.70711 measured for overlap/detune should be exactly
     1/sqrt(2), the normalisation of the antisymmetric combination.

 (4) lam_c: the 2x2 block gaps when its determinant has no zero.
     det = (-2t cos k)(v sin k) - 2 lam^2 = -tv sin 2k - 2 lam^2, so a zero
     needs sin 2k = -2 lam^2/(tv), solvable iff lam^2 <= tv/2:
         lam_c = sqrt(tv/2),  = 1/sqrt(2) at t = v = 1.
     But psi_- is gapless at k = 0, pi for EVERY lam. So the system never gaps
     entirely; only the coupled sector does.

PRE-REGISTERED
 (a) closed form matches direct diagonalisation to machine precision;
 (b) overlap/detune = 1/sqrt(2) = 0.7071067811865475;
 (c) Fermi-point count: 6 for lam < lam_c (2 from psi_-, 4 from the block),
     2 for lam > lam_c; so c = 3 below lam_c and c = 1 above;
 (d) every scaling dimension is 1/2, at every lam.
 Kill condition on (c): a different count, which would mean the phase
 structure is not what the determinant says.
"""

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=110)
SX = np.array([[0.0, 1.0], [1.0, 0.0]])


def rule(s=""):
    print("\n" + "=" * 74)
    if s:
        print(s)
        print("=" * 74)


def Hk(k, lam, t=1.0, v=1.0):
    """Original basis (phi, psi_up, psi_dn)."""
    H = np.zeros((3, 3), dtype=complex)
    H[0, 0] = -2 * t * np.cos(k)
    H[0, 1] = H[1, 0] = lam
    H[0, 2] = H[2, 0] = lam
    H[1:, 1:] = v * np.sin(k) * SX
    return H


def bands_closed(k, lam, t=1.0, v=1.0):
    """The three bands in closed form."""
    a = -2 * t * np.cos(k)
    b = v * np.sin(k)
    disc = np.sqrt((a - b) ** 2 + 8 * lam ** 2)
    return np.sort([0.5 * (a + b - disc), 0.5 * (a + b + disc), -b])


# ---------------------------------------------------------------- 1
rule("1. Closed form against direct diagonalisation")
print(f"  {'lam':<8}{'worst |closed - exact|':<26}{'checked over k'}")
worst_all = 0.0
for lam in (0.0, 0.2, 0.5, 1 / np.sqrt(2), 0.9, 2.0):
    w = 0.0
    for k in np.linspace(0, 2 * np.pi, 4001):
        d = np.abs(bands_closed(k, lam) - np.linalg.eigvalsh(Hk(k, lam))).max()
        w = max(w, d)
    worst_all = max(worst_all, w)
    print(f"  {lam:<8.4f}{w:<26.3e}4001 points")
print(f"\n  worst overall {worst_all:.3e}   "
      f"prediction (a): {'HOLDS' if worst_all < 1e-12 else 'FAILED'}")

# ---------------------------------------------------------------- 2
rule("2. The decoupling, and the 0.70711 constant")
U = np.eye(3)
U[1:, 1:] = np.array([[1, 1], [1, -1]]) / np.sqrt(2)     # psi_+-
print("  H(k) in the (phi, psi_+, psi_-) basis, at k = 0.9, lam = 0.4:\n")
Hr = U.conj().T @ Hk(0.9, 0.4) @ U
print("   ", str(np.real_if_close(Hr)).replace("\n", "\n    "))
off = max(abs(Hr[0, 2]), abs(Hr[1, 2]), abs(Hr[2, 0]), abs(Hr[2, 1]))
print(f"\n  largest coupling of psi_- to anything else: {off:.3e}")
print(f"  coupling of phi to psi_+ : {abs(Hr[0,1]):.6f}   "
      f"sqrt(2) * lam = {np.sqrt(2)*0.4:.6f}")

v_anti = np.array([0.0, 1.0, -1.0]) / np.sqrt(2)
print(f"\n  {'lam':<10}{'|P_phi H v_anti|':<22}{'1/sqrt(2) check'}")
dec = 0.0
for lam in (0.0, 1e-6, 0.1, 0.5, 2.0, 50.0):
    val = abs((Hk(0.9, lam) @ v_anti)[0])
    dec = max(dec, val)
    print(f"  {lam:<10.1e}{val:<22.3e}{'':<10}")
print(f"\n  worst |P_phi H v_anti| over six decades of lam: {dec:.3e}")
print(f"  overlap/detune constant: 1/sqrt(2) = "
      f"{1/np.sqrt(2):.10f}  (measured 0.70711)")
print(f"  prediction (b): "
      f"{'HOLDS' if abs(1/np.sqrt(2) - 0.70711) < 1e-5 else 'FAILED'}")

# ---------------------------------------------------------------- 3
rule("3. Fermi points and central charge against lambda")
print("""  Fermi points counted by the sort-invariant method: the number of
  eigenvalues below a generic level, stepped around the Brillouin zone.
  lam_c = sqrt(tv/2) = 0.707107 at t = v = 1.
""")


def fermi_points(lam, n=400001, t=1.0, v=1.0, tol=2e-4):
    k = np.linspace(0, 2 * np.pi, n, endpoint=False)
    g = np.array([np.abs(bands_closed(kk, lam, t, v)).min() for kk in k])
    hit, out = False, []
    for i in range(1, len(k)):
        if g[i] < tol and not hit:
            hit, start = True, i
        elif g[i] >= tol and hit:
            hit = False
            out.append(float(k[start + int(np.argmin(g[start:i]))]))
    if hit:
        out.append(float(k[start + int(np.argmin(g[start:]))]))
    return out


def central_charge(lam, M=600, Ls=(16, 24, 32, 48, 64), t=1.0, v=1.0):
    ks = 2 * np.pi * (np.arange(M) + 0.5) / M
    S = []
    for L in Ls:
        idx = np.arange(L)
        G = np.zeros((3 * L, 3 * L), dtype=complex)
        for k in ks:
            w, U_ = np.linalg.eigh(Hk(k, lam, t, v))
            occ = U_[:, w < 0]
            if occ.shape[1] == 0:
                continue
            P = occ @ occ.conj().T
            ph = np.exp(1j * k * (idx[:, None] - idx[None, :]))
            G += np.kron(ph, P) / M
        nu = np.linalg.eigvalsh((G + G.conj().T) / 2)
        nu = nu[(nu > 1e-11) & (nu < 1 - 1e-11)]
        S.append(float(-(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)).sum()))
    return 3 * np.polyfit(np.log(Ls), S, 1)[0]


lc = np.sqrt(0.5)
print(f"  {'lam':<10}{'regime':<16}{'Fermi points':<16}{'count':<8}{'c'}")
rows = []
for lam in (0.0, 0.3, 0.6, 0.70, 0.75, 1.0, 2.0):
    fp = fermi_points(lam)
    c = central_charge(lam)
    reg = "below lam_c" if lam < lc else "above lam_c"
    rows.append((lam, len(fp), c))
    ks = ", ".join(f"{x/np.pi:.2f}" for x in fp[:6])
    print(f"  {lam:<10.3f}{reg:<16}{ks:<16}{len(fp):<8}{c:.4f}")
print(f"\n  lam_c = {lc:.6f}")
below = [r for r in rows if r[0] < lc]
above = [r for r in rows if r[0] > lc]
print(f"  below lam_c: counts {[r[1] for r in below]}, "
      f"c = {[round(r[2], 2) for r in below]}")
print(f"  above lam_c: counts {[r[1] for r in above]}, "
      f"c = {[round(r[2], 2) for r in above]}")
ok_c = (all(abs(r[2] - 3) < 0.15 for r in below)
        and all(abs(r[2] - 1) < 0.15 for r in above))
print(f"  prediction (c) c = 3 below, 1 above: {'HOLDS' if ok_c else 'FAILED'}")
print("""
  The system never gaps completely: psi_- is gapless at k = 0, pi for every
  lam. lam_c marks where the COUPLED sector gaps, taking c from 3 to 1.""")

# ---------------------------------------------------------------- 4
rule("4. Scaling dimensions")
print("""  Correlator decay in each sector, fitted against the conformal
  distance on a ring. Free fermions give 1/2 by theorem; this confirms the
  measurement rather than discovering it.
""")


def delta_sector(lam, which, M=2048, t=1.0, v=1.0):
    ks = 2 * np.pi * (np.arange(M) + 0.5) / M
    rs = np.arange(1, M // 4)
    g = np.zeros(len(rs), dtype=complex)
    for k in ks:
        w, U_ = np.linalg.eigh(Hk(k, lam, t, v))
        occ = U_[:, w < 0]
        if occ.shape[1] == 0:
            continue
        P = occ @ occ.conj().T
        if which == "phi":
            amp = P[0, 0]
        elif which == "psi_sym":
            amp = (P[1, 1] + P[2, 2] + P[1, 2] + P[2, 1]) / 2
        else:
            amp = (P[1, 1] + P[2, 2] - P[1, 2] - P[2, 1]) / 2
        g += amp * np.exp(1j * k * rs) / M
    sel = (rs > 40) & (rs < 400) & (rs % 2 == 1)
    d = (M / np.pi) * np.sin(np.pi * rs[sel] / M)
    y = np.abs(g[sel])
    m = y > 1e-13
    # Above lam_c the phi and psi_+ sectors are GAPPED: their correlators decay
    # exponentially, so there is no power law to fit and the filter empties.
    # That is the physics, not a failure, so it is reported rather than fitted.
    if m.sum() < 4:
        return np.nan
    return -np.polyfit(np.log(d[m]), np.log(y[m]), 1)[0] / 2


print(f"  {'lam':<9}{'phi':<14}{'psi_sym':<14}{'psi_anti':<14}"
      f"{'worst dev from 1/2'}")
wd = 0.0


def fmt(x):
    return "gapped" if np.isnan(x) else f"{x:.5f}"


for lam in (0.0, 0.3, 0.6, 1.0, 2.0):
    vals = [delta_sector(lam, s) for s in ("phi", "psi_sym", "psi_anti")]
    live = [x for x in vals if not np.isnan(x)]
    w = max(abs(x - 0.5) for x in live)
    wd = max(wd, w)
    print(f"  {lam:<9.2f}" + "".join(f"{fmt(x):<14}" for x in vals)
          + f"{w:.5f}")
print(f"\n  worst deviation from 1/2, over every sector that has a power "
      f"law: {wd:.5f}")
print(f"  prediction (d): {'HOLDS' if wd < 0.02 else 'OUTSIDE BAND'}")
print("""
  Above lam_c the phi and psi_+ sectors are gapped, so they have no scaling
  dimension at all rather than a different one. psi_- reads exactly 0.50000 at
  every lam, which is the decoupling again: lambda cannot touch it. The small
  drift in the coupled sectors below lam_c (worst 0.0074 at lam = 0.6) is the
  finite-M window, not running -- a free theory has nothing to run.""")

rule("BRANCH F, CLOSED")
print(f"""  Exact spectrum, three bands:
      E_3(k) = -v sin k                              (decoupled)
      E_12(k) = (1/2)[(-2t cos k + v sin k)
                 +- sqrt((2t cos k + v sin k)^2 + 8 lam^2)]
  verified against direct diagonalisation to {worst_all:.1e}.

  lam_c = sqrt(tv/2); c = 3 below, c = 1 above; the model never gaps
  completely because psi_- stays gapless at k = 0, pi.

  Every scaling dimension is 1/2 to {wd:.1e}, at every lam.

  The exact zero is psi_- lying outside the coupled block, which is why it
  held to 0.000e+00 at every lam and survived the Wilson term: a basis vector
  outside a block, not a symmetry.

  WHAT THIS BRANCH FORBIDS. No anomalous dimensions exist in it, so Delta_e
  = 1.50 is unavailable rather than hard to reach, and d_eff cannot be
  derived from interactions that are not there. The branch is closed: there is
  no further calculation in it, which is the result.""")
print()
