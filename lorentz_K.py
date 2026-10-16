# Lorentzian (Wightman-type) pointwise positivity for the continued heat kernel on global de Sitter.
# Continuation: Euclidean S^4 point x with x.y = cos(mu) continues to the dS embedding point X with Z = X.Y (Lorentzian dot).
# Points: X = (sinh t, cosh t * w), w in S^3, t in [-T, T]. Z_ij = -t0_i t0_j + sum_k X_ik X_jk.
# Wightman-type kernel: W_ij = F(Z_ij - i eps (t_i - t_j)); Hermitian by construction since F has real coefficients.
# Test: min eigenvalue of W (Hermitian) must be >= 0 for a positive kernel. Controls: F(Z)=Z must fail.
import numpy as np
m2 = 1.0; t_heat = 0.1; L = 60
VolS4 = 8*np.pi**2/3
lam = np.array([l*(l+3) for l in range(L)], dtype=float)
kap = np.exp(-t_heat*(lam+m2))*np.array([(2*l+3)/(3*VolS4) for l in range(L)])

def gegen_complex(l_max, z):
    C = [np.ones_like(z), 3*z]
    for l in range(2, l_max):
        C.append((2*z*(l+0.5)*C[-1] - (l+1)*C[-2])/l)
    return C
def K_heat(z):
    C = gegen_complex(L, z)
    out = np.zeros_like(z, dtype=complex)
    for l in range(L): out += kap[l]*C[l]
    return out
def F_control(z): return z.astype(complex)

def run(F, eps, sign, N, T, seed):
    rng = np.random.default_rng(seed)
    t = rng.uniform(-T, T, N)
    w = rng.normal(size=(N, 4)); w /= np.linalg.norm(w, axis=1, keepdims=True)
    X = np.column_stack([np.sinh(t), np.cosh(t)[:, None]*w])
    Z = -np.outer(X[:, 0], X[:, 0]) + X[:, 1:] @ X[:, 1:].T
    W = F(Z - sign*1j*eps*(t[:, None]-t[None, :]))
    W = (W + W.conj().T)/2
    ev = np.linalg.eigvalsh(W)
    return ev.min(), np.max(np.abs(W - W.conj().T))

print('K_t(1) =', K_heat(np.array([1.0+0j]))[0].real)
for eps in [0.05, 0.2]:
    for sign in [+1, -1]:
        mn, herm = run(K_heat, eps, sign, N=60, T=1.0, seed=5)
        cmn, _ = run(F_control, eps, sign, N=60, T=1.0, seed=5)
        print('eps=%.2f sign=%+d  K_t min eig = %+.4e   control F(Z)=Z min eig = %+.4e   (hermitian err %.1e)' % (eps, sign, mn, cmn, herm))
