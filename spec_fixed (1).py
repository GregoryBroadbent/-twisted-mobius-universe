# Corrected addition theorem on S^4:  sum_m Y_lm(x) Y_lm*(x') = (2l+3)/(3 Vol) * C_l^{3/2}(cos mu)
# (check: at mu=0 this gives dim_l/Vol with dim_l = (l+1)(l+2)(2l+3)/6). Earlier code wrongly divided by C_l(1).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, cos, pi, gegenbauer
from hadamard_dS import G_sphere
mp.dps = 40
VolS4 = 8*pi**2/3
def G_spec(mu, m2, L):
    s = mpf(0)
    for l in range(L):
        s += (2*l+3)/(3*VolS4)/(l*(l+3)+m2) * gegenbauer(l, mpf(3)/2, cos(mu))
    return s
for m2s in ['1', '3']:
    m2 = mpf(m2s)
    for mu in ['1.0', '2.0']:
        print('m2=%s mu=%s  closed=%s  spectral(L=1500)=%s' % (m2s, mu,
              mp.nstr(mp.re(G_sphere(mpf(mu), m2)),10), mp.nstr(G_spec(mpf(mu), m2, 1500),10)))
# check the addition theorem at mu=0: sum of dims/Vol gives the heat-kernel-type identity (dim check)
print('dim check l=0..3:', [ (l+1)*(l+2)*(2*l+3)//6 for l in range(4)], ' RHS (2l+3)/3*C_l(1):',
      [mp.nstr((2*l+3)/mpf(3)*gegenbauer(l, mpf(3)/2, 1),6) for l in range(4)])
