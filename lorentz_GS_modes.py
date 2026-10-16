# Lorentzian positivity of G_S (Bunch-Davies candidate) on global de Sitter, by spatial-harmonic (l) decomposition.
# Points X = (sinh t, cosh t * w), w in S^3. Z(t,t',x) = -sinh t sinh t' + cosh t cosh t' x, x = w.w' = cos(theta).
# Wightman-type kernel W(t,w; t',w') = F(Z - i eps (t - t')), F = G_S (closed form) or a control.
# Harmonic component: w_l(t,t') = int_{-1}^{1} F(Z - i eps(t-t')) U_l(x) sqrt(1-x^2) dx, U_l = Chebyshev 2nd kind = C_l^{(1)}.
# For each l, the matrix [w_l(t_i,t_j)] (Hermitian) must be positive semidefinite. Also, the sector is rank-one per harmonic
# up to positive weights, so this is the relevant test. Quadrature: Gauss-Chebyshev 2nd kind (weight sqrt(1-x^2)).
import numpy as np, sys
from scipy.special import hyp2f1, gamma, eval_chebyu
m2 = 1.0
nu = np.sqrt(9/4 - m2); hp, hm = 1.5 + nu, 1.5 - nu
def G_S(Z):
    return gamma(hp)*gamma(hm)/(16*np.pi**2)*hyp2f1(hp, hm, 2, (1+Z)/2)
def control_Z(Z): return Z.astype(complex)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
NX = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
EPS = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
T = float(sys.argv[4]) if len(sys.argv) > 4 else 0.3
LMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 6
rng = np.random.default_rng(2)
ts = rng.uniform(-T, T, N)
k = np.arange(1, NX+1)
xk = np.cos(k*np.pi/(NX+1)); wk = np.pi/(NX+1)*np.sin(k*np.pi/(NX+1))**2   # Gauss-Chebyshev 2nd kind
def wl_matrix(F, l):
    M = np.zeros((N, N), dtype=complex)
    U = eval_chebyu(l, xk)
    for i in range(N):
        t = ts[i]
        Z = -np.sinh(t)*np.sinh(ts)[None, :] + np.cosh(t)*np.cosh(ts)[None, :]*xk[:, None]     # (NX, N)
        Zeps = Z - 1j*EPS*(t - ts)[None, :]
        vals = F(Zeps)
        M[i, :] = (wk*U) @ vals
    return (M + M.conj().T)/2
for name, F in [('G_S (Bunch-Davies candidate)', G_S), ('control F(Z)=Z', control_Z)]:
    print(name)
    for l in range(LMAX+1):
        M = wl_matrix(F, l)
        ev = np.linalg.eigvalsh(M)
        print('  l=%d  min eig = %+.4e   max eig = %+.4e   herm err %.1e' % (l, ev.min(), ev.max(), np.max(np.abs(M-M.conj().T))))
