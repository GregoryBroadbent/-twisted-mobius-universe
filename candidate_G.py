# Candidate kernel: K = G_S, the full Euclidean Green function (inverse of -Lap + m^2), with NO subtraction.
# Tests:
#  (a) spectral identity: G(mu) = sum_l (2l+3)/(3 Vol S^4) * C_l^{3/2}(cos mu)/C_l^{3/2}(1) / (l(l+3)+m^2)
#      -> every spectral weight is positive, so G is a positive-definite kernel (R2 holds exactly)
#  (b) constant-mode normalisation: 2 pi^2 * int_0^pi G sin^3 dmu = 1/m^2 (since -Lap 1 = 0)
#  (c) R3: G diverges at coincidence (1/sigma), so the test is whether that divergence is only the
#      local singular structure, i.e. G - U/(8pi^2 sigma) - V ln sigma is smooth (W continuous at 0).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, sin, cos, pi, quad, gegenbauer, nsum
from hadamard_dS import G_sphere
mp.dps = 40
VolS4 = 8*pi**2/3

def G_spec(mu, m2, L=3000):
    s = mpf(0)
    for l in range(L):
        w = (2*l+3)/(3*VolS4) / (l*(l+3)+m2)
        s += w * gegenbauer(l, mpf(3)/2, cos(mu)) / gegenbauer(l, mpf(3)/2, 1)
    return s

print('(a) spectral identity vs closed-form Green function')
for m2s in ['1', '3']:
    m2 = mpf(m2s)
    for mu in ['1.0', '2.0']:
        a = G_sphere(mpf(mu), m2)
        b = G_spec(mpf(mu), m2, L=1500)
        print('   m2=%s mu=%s  closed=%s  spectral(1500 terms)=%s' % (m2s, mu, mp.nstr(mp.re(a),10), mp.nstr(mp.re(b),10)))

print('(b) constant-mode normalisation: 2 pi^2 int G sin^3 dmu  vs  1/m^2')
for m2s in ['0.3', '1', '3', '4']:
    m2 = mpf(m2s)
    val = 2*pi**2*quad(lambda t: mp.re(G_sphere(t, m2))*sin(t)**3, [mpf('1e-12'), pi/2, pi-mpf('1e-12')])
    print('   m2=%s  integral=%s   1/m2=%s' % (m2s, mp.nstr(val,12), mp.nstr(1/m2,12)))
