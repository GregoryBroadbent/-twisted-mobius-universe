# S^4 reflection positivity with product-integration treatment of the G_S self-term.
# G_S: closed form (no spectral truncation). Diagonal entries K_aa replaced by the average of G_S over the node's cell:
#   K_eff(r) = A1/(4 pi^2 r^2) + (1/8pi^2)[1/2 + W0 + V0 (ln r^2 + B1 - ln 2)],  r = (2 w_a/pi^2)^{1/4},
# A1 = E[1/|u|^2], B1 = E[ln|u|^2] over the unit 4-ball (cell_constants.py), from G_S = 1/(4pi^2 mu^2) + (1/8pi^2)[1/2 + W0 + V0 ln(mu^2/2)] + O(mu^2 ln mu).
# K_t and the regularised control use the same nodes and test functions.
import sys, time
import numpy as np
from scipy.special import hyp2f1, gamma, digamma, eval_gegenbauer
n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
m2 = 1.0; s = 0.6; t_heat = 0.1; DELTA = 0.3; LH = 40
A1 = 1.333063; B1 = 0.083292
nu = np.sqrt(9/4 - m2); hp, hm = 1.5 + nu, 1.5 - nu
VolS4 = 8*np.pi**2/3
V0 = (m2-2)/2; EG = 0.5772156649015329
W0 = (m2-2)*(0.5*(digamma(hp)+digamma(hm)) + EG - 0.5*np.log(2)) - m2/2 + 2/3

xg, wg = np.polynomial.legendre.leggauss(n)
chi = np.pi/4*(xg+1); wchi = np.pi/4*wg*np.sin(chi)**3
psi = np.pi/2*(xg+1); wpsi = np.pi/2*wg*np.sin(psi)**2
th = np.arccos(xg); wth = wg.copy()
ph = 2*np.pi*np.arange(2*n)/(2*n); wph = np.full(2*n, 2*np.pi/(2*n))
Xs, Ws = [], []
for ic, c in enumerate(chi):
    for ip, p in enumerate(psi):
        for it, t_ in enumerate(th):
            for iq, q in enumerate(ph):
                u3 = np.array([np.cos(p), np.sin(p)*np.cos(t_), np.sin(p)*np.sin(t_)*np.cos(q), np.sin(p)*np.sin(t_)*np.sin(q)])
                Xs.append(np.concatenate([[np.cos(c)], np.sin(c)*u3]))
                Ws.append(wchi[ic]*wpsi[ip]*wth[it]*wph[iq])
X = np.array(Xs); W = np.array(Ws); N = len(X)
Xr = X*np.array([-1, 1, 1, 1, 1])

def bump(x):
    out = np.zeros_like(x); m = x > 0; out[m] = np.exp(-1.0/x[m]); return out
def smooth_step(t):
    a = bump(1.0 - t); b = bump(t)
    return np.where(a+b > 0, b/np.maximum(a+b, 1e-300), 0.0)
def h_cut(x0): return smooth_step(np.clip(x0/DELTA, -1, 2))

rng = np.random.default_rng(seed)
def samp(M):
    pts = []
    while sum(len(p) for p in pts) < M:
        v = rng.normal(size=(2*M, 5)); v /= np.linalg.norm(v, axis=1, keepdims=True)
        pts.append(v[v[:, 0] > 0])
    return np.vstack(pts)[:M]
centers = samp(4)[:4]
F = np.stack([np.exp(-np.sum((X-c)**2, axis=1)/(2*s*s))*h_cut(X[:, 0]) for c in centers])
FW = F*W; V = FW.T

def Gclosed(c):
    return gamma(hp)*gamma(hm)/(16*np.pi**2)*hyp2f1(hp, hm, 2, np.clip((1+c)/2, 0, 1-1e-15))
r_cell = (2*W/np.pi**2)**0.25
Keff = A1/(4*np.pi**2*r_cell**2) + (0.5 + W0 + V0*(np.log(r_cell**2) + B1 - np.log(2)))/(8*np.pi**2)

def Kheat_c(c):
    out = np.zeros_like(c)
    for l in range(LH):
        out += np.exp(-t_heat*(l*(l+3)+m2))*(2*l+3)/(3*VolS4)*eval_gegenbauer(l, 1.5, c)
    return out

def control_reg(c):
    mu = np.arccos(np.clip(c, -1, 1)); sig = mu**2/2
    with np.errstate(all='ignore'):
        t = np.clip((mu - np.pi/4)/(np.pi/4), 0.0, 1.0)
        chi_ = 1.0 - smooth_step(t)
        U = (mu/np.sin(np.maximum(mu, 1e-300)))**1.5
        Vmu = V0*hyp2f1(hp, hm, 2, np.clip((1-c)/2, 0, 1-1e-12))
        G = Gclosed(c)
        sing = np.where(chi_ > 0, chi_*(U/sig + Vmu*np.log(sig) + W0), 0.0)
        out = G - sing/(8*np.pi**2)
    out[mu < 1e-6] = 0.0
    return out

t0 = time.time()
KV_G = np.zeros((N, 4)); KV_h = np.zeros((N, 4)); KV_c = np.zeros((N, 4))
CH = 500
for a0 in range(0, N, CH):
    a1 = min(N, a0+CH)
    Cd = np.clip(X[a0:a1] @ X.T, -1, 1); Cr = np.clip(X[a0:a1] @ Xr.T, -1, 1)
    Kd = Gclosed(Cd)
    rows = np.arange(a1-a0); Kd[rows, rows+a0] = Keff[a0:a1]
    KV_G[a0:a1] = (Kd - Gclosed(Cr)) @ V
    KV_h[a0:a1] = (Kheat_c(Cd) - Kheat_c(Cr)) @ V
    KV_c[a0:a1] = (control_reg(Cd) - control_reg(Cr)) @ V
print('n=%d (N=%d), seed=%d, volume %.9f vs %.9f, cell radius range [%.4f, %.4f]' % (n, N, seed, W.sum(), VolS4/2, r_cell.min(), r_cell.max()))
for name, KV in [('G_S (cell-averaged diagonal)', KV_G), ('K_t heat kernel, t=0.1', KV_h), ('control_reg (cutoff)', KV_c)]:
    Q = FW @ KV; ev = np.linalg.eigvalsh((Q+Q.T)/2)
    print('%-28s eigenvalues: %s' % (name, np.array2string(ev, precision=6)))
print('wall time %.1f s' % (time.time()-t0))
