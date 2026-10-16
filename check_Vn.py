# Numerical check of V_n: fit Q(sigma) = F - U/sigma = sum_n sigma^n (V_n ln sigma + W_n)
# to the exact Euclidean S^4 Green function at many small separations (least squares, high precision).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, log, matrix, qr_solve, sin, pi
from hadamard_dS import G_sphere
mp.dps = 120

def Q(mu, m2):
    sigma = mu**2/2
    F = 8*pi**2*G_sphere(mu, m2)
    U = (mu/sin(mu))**mpf(1.5)
    return F - U/sigma, sigma

def fit(m2, K=6, npts=24):
    rows, rhs = [], []
    for i in range(npts):
        mu = mpf('0.02') + mpf('0.12')*i/(npts-1)
        q, s = Q(mu, m2)
        L = log(s)
        row = []
        for n in range(K):
            row += [s**n*L, s**n]          # unknown order: V0, W0, V1, W1, ...
        rows.append(row); rhs.append(q)
    x, res = qr_solve(matrix(rows), matrix(rhs))
    return [x[2*n] for n in range(K)], [x[2*n+1] for n in range(K)]

for m2s in ['0.3', '1', '3', '4']:
    m2 = mpf(m2s)
    V, W = fit(m2)
    Vpred = [(m2-2)/2, m2*(m2-2)/8, m2*(m2-2)*(m2+2)/96]
    print('m2=%s' % m2s)
    for n in range(3):
        v = mp.re(V[n])
        print('  V%d numeric=%s  predicted=%s  diff=%s' % (n, mp.nstr(v,12), mp.nstr(Vpred[n],12), mp.nstr(abs(v-Vpred[n]),3)))
