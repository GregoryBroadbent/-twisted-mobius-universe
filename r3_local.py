# Reworded R3: "the coincidence structure of K_t is local".
# Test: the coefficients of K_t(0) = (4 pi t)^-2 * sum_n a_n t^n must be local curvature invariants.
# On unit S^4 (H=1), scalar operator -Lap + m2 (xi = 0):
#   a0 = 1,  a1 = R/6 - m2 = 2 - m2,
#   a2 = (1/180)(Riem^2 - Ric^2) + (1/2)(R/6 - m2)^2,  with Riem^2 = 24, Ric^2 = 36  -> a2 = -1/15 + (2-m2)^2/2
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpf as F
from heat_kernel_S4 import K_t
mp.dps = 40
m2 = mpf(1)
a1 = 2 - m2
a2 = mpf(-1)/15 + (2 - m2)**2/2
print('m2 =', m2, ' predicted a1 =', a1, ' a2 =', mp.nstr(a2, 10))
for t in ['0.02', '0.01', '0.005']:
    tt = mpf(t)
    K0 = K_t(mpf('1e-15'), m2, tt)
    ser = K0*(4*mp.pi*tt)**2
    a2_num = (ser - 1 - a1*tt)/tt**2
    print('  t=%s  extracted a2 = %s   (predicted %s)' % (t, mp.nstr(a2_num, 8), mp.nstr(a2, 8)))
