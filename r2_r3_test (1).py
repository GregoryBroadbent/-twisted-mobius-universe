# Step 4 tests for the subtracted kernel H~ = H_ren - <phi^2>_ren  (H = 1, ell = 1/H)
# Exact log coefficient: V(mu) = V0 * 2F1(h+,h-;2;(1-cos mu)/2)   (regular solution of the homogeneous ODE)
# Smooth part:          W(mu)  = 8 pi^2 G(mu) - U/sigma - V(mu) ln sigma ;  H_ren = W/(8 pi^2)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, sqrt, sin, cos, pi, log, hyp2f1, quad, diff
from hadamard_dS import G_sphere
mp.dps = 60

def pars(m2):
    nu = sqrt(mpf(9)/4 - m2)
    return mpf(3)/2 + nu, mpf(3)/2 - nu

def V_of(mu, m2):
    hp, hm = pars(m2)
    V0 = (m2 - 2)/2
    return V0 * hyp2f1(hp, hm, 2, (1 - cos(mu))/2)

def W_of(mu, m2):
    sig = mu**2/2
    U = (mu/sin(mu))**mpf(1.5)
    return 8*pi**2*G_sphere(mu, m2) - U/sig - V_of(mu, m2)*log(sig)

def Hren(mu, m2):
    return W_of(mu, m2)/(8*pi**2)

def W0_closed(m2):
    hp, hm = pars(m2)
    from mpmath import digamma, euler
    S = digamma(hp) + digamma(hm)
    return (m2-2)*(S/2 + euler - log(2)/2) - m2/2 + mpf(2)/3

def L(f, mu, m2):
    # radial operator (box - m^2) on functions of mu on S^4
    return diff(f, mu, 2) + 3*cos(mu)/sin(mu)*diff(f, mu) - m2*f(mu)

for m2s in ['0.3', '1', '3', '4']:
    m2 = mpf(m2s)
    hp, hm = pars(m2)
    c = Hren(mpf('1e-8'), m2)           # coincidence value of H_ren (ell = 1/H)
    print('--- m2 =', m2s)
    print('  W0 closed form        =', mp.nstr(mp.re(W0_closed(m2)), 12))
    print('  <phi^2>_ren*8pi^2 (numerical coincidence) =', mp.nstr(mp.re(W_of(mpf('1e-8'), m2)), 12))
    # residual of the homogeneous equation for H_ren at small separations
    for mu in ['0.5', '0.1', '0.01']:
        r = L(lambda t: Hren(t, m2), mpf(mu), m2)
        print('  L[H_ren](mu=%s) = %s    (-m2*c = %s)' % (mu, mp.nstr(mp.re(r),10), mp.nstr(mp.re(-m2*c),10)))
    # constant-mode positivity: lambda_c[H_ren] - c*Vol(S^4) >= 0 ?
    lam = 2*pi**2*quad(lambda t: Hren(t, m2)*sin(t)**3, [mpf('1e-8'), pi/2, pi - mpf('1e-8')])
    vol = 8*pi**2/3
    print('  lambda_c[H_ren] =', mp.nstr(mp.re(lam),10), '  c*Vol =', mp.nstr(mp.re(c*vol),10),
          '  lambda_c[H~] =', mp.nstr(mp.re(lam - c*vol),10))
