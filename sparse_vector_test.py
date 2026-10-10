#!/usr/bin/env python3
"""
Sparse-vector gate for the fermionic MPO in mpo_build.py.

Tests the COMPRESSED MPO as an operator. No DMRG, no energy tolerance, no
half-filling projection. Two checks per case:

  (1) operator:  max | MPO_dense - H_sparse |  over the full 2^N space
  (2) vector:    || H_MPO v - H_sparse v ||  for v = the exact ground vector
                 of H_sparse, obtained from a sparse eigensolver

H_sparse is built here, independently of the MPO code, as a sum of Kronecker
products of the local 2x2 operators in the same (coef, op-per-site) term list.
The MPO is then built from that list by mpo_build.build_mpo, which compresses
at cutoff 1e-14. The only shared input is the term list.

Site ordering convention: site 0 is the most significant tensor factor, which
is the kron convention used here. If the MPO's dense form uses the other
ordering, check (1) fails by O(1) for every case, which is a convention error
and not an MPO error. Hermiticity of the MPO is also checked.

PRE-REGISTERED, before running
  Prediction: operator and vector errors at or below ~1e-13, set by the
              1e-14 compression cutoff and rounding.
  Pass:       for every case, operator error < 1e-12, vector error < 1e-12,
              and Hermiticity defect < 1e-12.
  Kill:       any case with an error >= 1e-12. Then mpo_build.py is not exact
              to the 1e-12 tolerance that the brief attributes to it, and that
              claim should be withdrawn until the cause is found. The earlier
              Gate A (energy agreement to 1e-8, DMRG tolerance 1e-10) cannot
              rescue it, because it tests energies, not the operator.
"""

import importlib.util
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

SRC = "/mnt/user-data/uploads/mpo_build__2_.py"   # read-only, used in place
spec = importlib.util.spec_from_file_location("mpo_build", SRC)
mb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mb)

TOL = 1e-12


def local_sparse(ops):
    """Kron of the per-site 2x2 operators, site 0 most significant."""
    out = sp.csr_matrix(np.array([[1.0 + 0j]]))
    for o in ops:
        out = sp.kron(out, sp.csr_matrix(np.asarray(o, dtype=complex)),
                      format="csr")
    return out


def H_sparse(N, terms):
    H = sp.csr_matrix((2 ** N, 2 ** N), dtype=complex)
    for coef, ops in terms:
        H = H + complex(coef) * local_sparse(ops)
    return H.tocsr()


CASES = [(3, 0.4, 0.0), (3, 0.4, 2.0), (4, 0.4, 0.0),
         (4, 0.4, 2.0), (4, 0.0, 1.0)]

print("=" * 88)
print("SPARSE-VECTOR GATE -- compressed MPO against independent sparse H")
print("=" * 88)
print(f"  {'L':<4}{'N':<4}{'lam':<6}{'U':<5}{'op err':<12}{'vec err':<12}"
      f"{'herm def':<12}{'E0 (sparse)':<16}{'bond'}")

rows = []
for (L, lam, U) in CASES:
    N, terms = mb.three_species_terms(L, lam, U, pbc=False)
    mpo = mb.build_mpo(N, terms)
    Hm = np.asarray(mpo.to_dense(), dtype=complex)
    Hs = H_sparse(N, terms)
    Hs_d = Hs.toarray()

    op_err = float(np.abs(Hm - Hs_d).max())
    herm = float(np.abs(Hm - Hm.conj().T).max())

    E, V = eigsh(Hs, k=1, which="SA", tol=1e-13)
    v = V[:, 0]
    vec_err = float(np.linalg.norm(Hm @ v - Hs @ v))

    rows.append((L, N, lam, U, op_err, vec_err, herm, E[0], mpo.max_bond()))
    print(f"  {L:<4}{N:<4}{lam:<6.2f}{U:<5.1f}{op_err:<12.2e}{vec_err:<12.2e}"
          f"{herm:<12.2e}{E[0]:<16.9f}{mpo.max_bond()}")

worst_op = max(r[4] for r in rows)
worst_vec = max(r[5] for r in rows)
worst_herm = max(r[6] for r in rows)
ok = (worst_op < TOL) and (worst_vec < TOL) and (worst_herm < TOL)

print()
print(f"  worst operator error     {worst_op:.2e}")
print(f"  worst vector error       {worst_vec:.2e}")
print(f"  worst Hermiticity defect {worst_herm:.2e}")
print(f"  tolerance                {TOL:.0e}")
print(f"\n  SPARSE-VECTOR GATE: {'PASS' if ok else 'FAIL -- MPO not exact at 1e-12'}")
