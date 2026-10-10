#!/usr/bin/env python3
"""
Fermionic MPO builder (Jordan-Wigner) + GATE A: the MPO must reproduce the
exact-diagonalisation ground energy of the three-species model.

JW convention, |0> empty and |1> occupied:
    c_j   = (prod_{k<j} Z_k) sigma^-_j ,   c+_j = (prod_{k<j} Z_k) sigma^+_j
Working the strings out for a < b:
    c+_a c_b = sigma^+_a (prod_{a<k<b} Z_k) sigma^-_b
    c+_b c_a = sigma^-_a (prod_{a<k<b} Z_k) sigma^+_b
Density terms carry no string. Terms are built as product MPOs and summed,
which is correct by construction -- no finite-state-automaton bookkeeping to
get wrong -- then compressed.
"""

import numpy as np
import quimb as qu
import quimb.tensor as qtn

I2 = np.eye(2)
ZZ = np.diag([1.0, -1.0])
SP = np.array([[0.0, 0.0], [1.0, 0.0]])      # |1><0|, creates
SM = np.array([[0.0, 1.0], [0.0, 0.0]])      # |0><1|, annihilates
NN = np.diag([0.0, 1.0])


def term_hop(N, a, b, coef):
    """coef * c+_a c_b  + h.c.   as a list of product-MPO specs."""
    if a == b:
        ops = [I2] * N
        ops[a] = NN
        return [(np.real(coef), ops)]
    lo, hi = (a, b) if a < b else (b, a)
    out = []
    # c+_a c_b
    ops = [I2] * N
    for k in range(lo + 1, hi):
        ops[k] = ZZ
    if a < b:
        ops[a], ops[b] = SP, SM
    else:
        ops[b], ops[a] = SM, SP
    out.append((coef, ops))
    # h.c.
    ops2 = [I2] * N
    for k in range(lo + 1, hi):
        ops2[k] = ZZ
    if a < b:
        ops2[a], ops2[b] = SM, SP
    else:
        ops2[b], ops2[a] = SP, SM
    out.append((np.conj(coef), ops2))
    return out


def term_dens(N, a, b, coef):
    ops = [I2] * N
    if a == b:
        ops[a] = NN
    else:
        ops[a] = NN
        ops[b] = NN
    return [(coef, ops)]


def build_mpo(N, terms, cutoff=1e-14):
    """terms: list of (coef, [op per site]). Sum of product MPOs, compressed."""
    mpo = None
    for coef, ops in terms:
        m = qtn.MPO_product_operator([np.asarray(o, dtype=complex) for o in ops])
        m = m * complex(coef)
        mpo = m if mpo is None else mpo + m
        if mpo.max_bond() > 120:
            mpo.compress(cutoff=cutoff)
    mpo.compress(cutoff=cutoff)
    return mpo


# ------------------------------------------------- the three-species model
PHI_, UP_, DN_ = 0, 1, 2


def three_species_terms(L, lam, U, t=1.0, v=1.0, pbc=False, ph_sym=True):
    """
    phi : -t (c+_i c_{i+1} + h.c.)
    psi : -i (v/2) [psi+_i alpha psi_{i+1} - h.c.], alpha = sigma_x
    coup: lam (phi+_i psi_{i,up} + phi+_i psi_{i,dn} + h.c.)
    int : U (n_up - 1/2)(n_dn - 1/2)   [ph_sym] or U n_up n_dn
    Orbital index 3i + s. Open boundaries unless pbc.
    """
    N = 3 * L
    terms = []
    bonds = range(L if pbc else L - 1)
    for i in bonds:
        j = (i + 1) % L
        # phi hopping
        terms += term_hop(N, 3 * i + PHI_, 3 * j + PHI_, -t)
        # psi Dirac: alpha = sigma_x couples up_i <-> dn_j and dn_i <-> up_j
        terms += term_hop(N, 3 * i + UP_, 3 * j + DN_, -1j * v / 2)
        terms += term_hop(N, 3 * i + DN_, 3 * j + UP_, -1j * v / 2)
    for i in range(L):
        terms += term_hop(N, 3 * i + PHI_, 3 * i + UP_, lam)
        terms += term_hop(N, 3 * i + PHI_, 3 * i + DN_, lam)
        if U != 0.0:
            a, b = 3 * i + UP_, 3 * i + DN_
            if ph_sym:
                # U(n_a - 1/2)(n_b - 1/2) = U n_a n_b - U/2 n_a - U/2 n_b + U/4
                terms += term_dens(N, a, b, U)
                terms += term_dens(N, a, a, -U / 2)
                terms += term_dens(N, b, b, -U / 2)
            else:
                terms += term_dens(N, a, b, U)
    return N, terms


# ------------------------------------------------- ED reference
def ed_energy(L, lam, U, t=1.0, v=1.0, ph_sym=True):
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import eigsh
    N = 3 * L
    _, terms = three_species_terms(L, lam, U, t, v, pbc=False, ph_sym=ph_sym)
    # dense many-body build from the same term list, half filling
    st = np.array([s for s in range(1 << N) if bin(s).count("1") == N // 2],
                  dtype=np.int64)
    order = np.argsort(st); sts = st[order]; n = len(st)
    H = np.zeros((n, n), dtype=complex)
    for coef, ops in terms:
        # identify the sites with non-identity ops
        act = [(k, o) for k, o in enumerate(ops) if not np.allclose(o, I2)]
        for ia, s in enumerate(st):
            amp = complex(coef)
            s2 = s
            ok = True
            for k, o in act:
                bit = (s >> k) & 1
                if np.allclose(o, NN):
                    amp *= bit
                elif np.allclose(o, ZZ):
                    amp *= (1 - 2 * bit)
                elif np.allclose(o, SP):
                    if bit:
                        ok = False; break
                    s2 |= (1 << k)
                elif np.allclose(o, SM):
                    if not bit:
                        ok = False; break
                    s2 &= ~(1 << k)
                if amp == 0:
                    ok = False; break
            if not ok or amp == 0:
                continue
            p = np.searchsorted(sts, s2)
            if p < n and sts[p] == s2:
                H[order[p], ia] += amp
    w = np.linalg.eigvalsh((H + H.conj().T) / 2)
    return w[0], n


def dmrg_energy(N, terms, bond=200, cyclic=False):
    mpo = build_mpo(N, terms)
    dm = qtn.DMRG2(mpo, bond_dims=[20, 40, 80, bond], cutoffs=1e-11)
    dm.solve(tol=1e-10, max_sweeps=40, verbosity=0)
    return dm.energy, mpo.max_bond()


if __name__ == "__main__":
    print("=" * 72)
    print("GATE A -- the MPO must reproduce exact diagonalisation")
    print("=" * 72)
    print(f"  {'L':<5}{'N':<5}{'lam':<7}{'U':<6}{'ED E0':<16}{'DMRG E0':<16}"
          f"{'diff':<12}{'MPO bond'}")
    ok = True
    for (L, lam, U) in ((3, 0.4, 0.0), (3, 0.4, 2.0), (4, 0.4, 0.0),
                        (4, 0.4, 2.0), (4, 0.0, 1.0)):
        e_ed, dim = ed_energy(L, lam, U)
        N, terms = three_species_terms(L, lam, U, pbc=False)
        e_dm, mb = dmrg_energy(N, terms, bond=200)
        d = abs(e_ed - e_dm)
        ok &= d < 1e-12
        print(f"  {L:<5}{3*L:<5}{lam:<7.2f}{U:<6.1f}{e_ed:<16.9f}"
              f"{e_dm:<16.9f}{d:<12.2e}{mb}")
    print(f"\n  GATE A: {'PASS' if ok else 'FAIL -- the MPO is wrong'}")
