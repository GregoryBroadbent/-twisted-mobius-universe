import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hadamard_dS import coeffs
from mpmath import mp, mpf, sqrt, digamma, matrix, lu_solve, nstr
mp.dps = 80
def basis(m2):
    nu = sqrt(mpf(9)/4 - m2); hp, hm = mpf(3)/2+nu, mpf(3)/2-nu
    S = digamma(hp)+digamma(hm)
    return [ (m2-2)*S/2, m2, mpf(1) ]
pts = [mpf('0.3'), mpf(1), mpf(3), mpf(4)]
data = []
for m2 in pts:
    V0, W0 = coeffs(m2)
    data.append((m2, mp.re(W0)))
A = matrix([basis(m) for m,_ in data[:3]]); b = matrix([w for _,w in data[:3]])
c = lu_solve(A, b)
print('coeffs (a,b,c) in W0 = a*(m2-2)(psi+ + psi-)/2 + b*m2 + c :', [nstr(x,12) for x in c])
for m2,w in data:
    pred = sum(ci*bi for ci,bi in zip(c, basis(m2)))
    print('m2=%s  W0=%s  fit=%s' % (m2, nstr(w,15), nstr(pred,15)))
m2 = mpf('0.5'); V0,W0 = coeffs(m2); print('check m2=0.5 W0=', nstr(mp.re(W0),15), 'fit=', nstr(sum(ci*bi for ci,bi in zip(c,basis(m2))),15))
