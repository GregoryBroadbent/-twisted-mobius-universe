# Heat kernel candidate K_t = exp(-t L),  L = -Lap + m^2  on the unit S^4 (H = 1).
# Spectral form:  K_t(mu) = sum_l exp(-t (l(l+3)+m2)) * (2l+3)/(3 Vol) * C_l^{3/2}(cos mu)
# Tests:
#  (1) positivity: all spectral weights exp(-t lambda) > 0  (R2 by construction)
#  (2) constant mode: int K_t dV = exp(-t m2)  -> 1 as t -> 0 (delta-function normalisation)
#  (3) coincidence: K_t(0) finite and equal to the Seeley-DeWitt expansion (4 pi t)^{-2}[1 + t(R/6 - m2) + O(t^2)], R = 12
#  (4) short distance: K_t(mu) ~ (4 pi t)^{-2} exp(-mu^2/(4t)) (no 1/sigma singularity, unlike G)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, cos, sin, pi, exp, gegenbauer, quad
mp.dps = 30
VolS4 = 8*pi**2/3

def K_t(mu, m2, t):
    s = mpf(0); l = 0
    while True:
        lam = l*(l+3) + m2
        w = exp(-t*lam)*(2*l+3)/(3*VolS4)*gegenbauer(l, mpf(3)/2, cos(mu))
        s += w
        if l > 10 and abs(w) < mpf(10)**(-25):
            break
        l += 1
    return s

m2 = mpf(1)
print('(1) spectral weights positive:', all(exp(-mpf('0.05')*(l*(l+3)+m2)) > 0 for l in range(2000)))
print('(2) constant mode int K_t dV vs exp(-t m2)')
for t in ['0.01', '0.1', '0.5']:
    tt = mpf(t)
    val = 2*pi**2*quad(lambda s: K_t(s, m2, tt)*sin(s)**3, [0, pi/2, pi])
    print('    t=%s  integral=%s  exp(-t m2)=%s' % (t, mp.nstr(val,10), mp.nstr(exp(-tt*m2),10)))
print('(3) coincidence K_t(0) vs Seeley-DeWitt (4pi t)^-2 [1 + t(R/6 - m2)]')
for t in ['0.02', '0.05', '0.1']:
    tt = mpf(t)
    exact = K_t(mpf('1e-12'), m2, tt)
    sd1 = (4*pi*tt)**-2*(1 + tt*(mpf(12)/6 - m2))
    print('    t=%s  K_t(0)=%s  SD to O(t)=%s  ratio=%s' % (t, mp.nstr(exact,10), mp.nstr(sd1,10), mp.nstr(exact/sd1,8)))
print('(4) short distance: K_t(mu)/[(4pi t)^-2 exp(-mu^2/4t)] at mu = sqrt(t)')
for t in ['0.02', '0.05']:
    tt = mpf(t); mu = mp.sqrt(tt)
    ratio = K_t(mu, m2, tt)/((4*pi*tt)**-2*exp(-mu**2/(4*tt)))
    print('    t=%s  ratio=%s' % (t, mp.nstr(ratio,8)))
