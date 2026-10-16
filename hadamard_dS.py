# Euclidean S^4 (H=1) Green function of (-Lap + m^2), Allen-Jacobson form:
#   G(mu) = Gamma(h+)Gamma(h-)/(16 pi^2) * 2F1(h+,h-;2;(1+cos mu)/2),  h± = 3/2 ± nu, nu^2 = 9/4 - m^2
# Hadamard form: G = (1/8pi^2)[U/sigma + V ln sigma + W], sigma = mu^2/2, U = Delta^{1/2} = (mu/sin mu)^{3/2}
# Coefficients extracted numerically at high precision, then fitted in m^2.
from mpmath import mp, mpf, hyp2f1, gamma, sqrt, log, cos, sin, pi
mp.dps = 80  # needed: cancellation in U/sigma at mu ~ 1e-12

def G_sphere(mu, m2):
    nu = sqrt(mpf(9)/4 - m2)
    hp, hm = mpf(3)/2 + nu, mpf(3)/2 - nu
    return gamma(hp)*gamma(hm)/(16*pi**2) * hyp2f1(hp, hm, 2, (1+cos(mu))/2)

def Q(mu, m2):
    sigma = mu**2/2
    F = 8*pi**2*G_sphere(mu, m2)
    U = (mu/sin(mu))**mpf(1.5)
    return F - U/sigma, sigma

def coeffs(m2):
    mu1, mu2 = mpf('1e-12'), mpf('1e-13')
    q1, s1 = Q(mu1, m2)
    q2, s2 = Q(mu2, m2)
    V0 = (q1 - q2)/(log(s1) - log(s2))
    W0 = q1 - V0*log(s1)
    return V0, W0

if __name__ == '__main__':
    # sanity: short-distance normalisation F*sigma -> 1
    mu = mpf('1e-12'); print('F*sigma at small mu:', mp.nstr(8*pi**2*G_sphere(mu,mpf('0.3'))*mu**2/2, 12))
    for m2 in [mpf('0.3'), mpf(1), mpf(2), mpf(3), mpf(4), mpf('0.5')]:
        V0, W0 = coeffs(m2)
        print('m2=%s  V0=%s  W0=%s' % (m2, mp.nstr(V0,15), mp.nstr(W0,15)))
