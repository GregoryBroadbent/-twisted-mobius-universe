"""
Bunch-Davies mode functions on global dS4 (H=1), S^3 slicing, and checks against the
closed-form Bunch-Davies / S^4 Green function G_S. No i-epsilon regulator is used for
the mode sum itself.

Metric: ds^2 = -dt^2 + cosh^2(t) dOmega_3^2.  Harmonic degree l on S^3, L = l(l+2).
Mode eq:  f'' + 3 tanh(t) f' + (m^2 + L/cosh^2 t) f = 0.
Ansatz:   f_l(t) = N_l * cosh(t)^l * 2F1(a,b;c;z),  z = (1 - i sinh t)/2,
          a = l + 3/2 + nu,  b = l + 3/2 - nu,  c = l + 2,  nu = sqrt(9/4 - m^2).
Regular at z = 0 (sinh t = -i, the lower-half-plane cap): the Bunch-Davies choice.
Normalisation: a^3 (f conj(f') - conj(f) f') = i  (canonical commutator).
Wightman function: W(t,t',g) = sum_l f_l(t) conj(f_l(t')) (l+1)/(2 pi^2) U_l(cos g),
U_l = Chebyshev-2nd-kind = C_l^(1).
Closed form (Euclidean S^4 Green function, continued): G(Z) = Gamma(h+)Gamma(h-)/(16 pi^2)
  * 2F1(h+,h-;2;(1+Z)/2),  h+- = 3/2 +- nu,  Z = X.Y (Lorentzian embedding dot).
"""
import mpmath as mp
mp.mp.dps = 30
M2 = mp.mpf(1)
NU = mp.sqrt(mp.mpf(9)/4 - M2)
HP, HM = mp.mpf(3)/2 + NU, mp.mpf(3)/2 - NU

def f_unnorm(l, t):
    z = (1 - 1j*mp.sinh(t))/2
    a, b, c = l + mp.mpf(3)/2 + NU, l + mp.mpf(3)/2 - NU, l + 2
    return mp.cosh(t)**l * mp.hyp2f1(a, b, c, z)

_norm = {}
def f_mode(l, t):
    if l not in _norm:
        f0 = f_unnorm(l, mp.mpf(0))
        fp0 = mp.diff(lambda s: f_unnorm(l, s), 0)
        w = 2*mp.im(f0*mp.conj(fp0))          # Wronskian of unnormalised mode at t=0 (a=1)
        _norm[l] = 1/mp.sqrt(w)               # |N|^2 * w = 1 with a(0)=1  -> Wronskian = i
    return _norm[l]*f_unnorm(l, t)

def wronskian(l, t):
    f = f_mode(l, t); fp = mp.diff(lambda s: f_mode(l, s), t)
    return mp.cosh(t)**3 * (f*mp.conj(fp) - mp.conj(f)*fp)

def U(l, x):
    th = mp.acos(x)
    return mp.sin((l+1)*th)/mp.sin(th) if abs(mp.sin(th)) > 1e-25 else (l+1)*mp.mpf(1)

def G_closed(Z):
    return mp.gamma(HP)*mp.gamma(HM)/(16*mp.pi**2) * mp.hyp2f1(HP, HM, 2, (1+Z)/2)

def W_modes(t, tp, g, L):
    s = mp.mpf(0)
    x = mp.cos(g)
    for l in range(L+1):
        s += f_mode(l, t)*mp.conj(f_mode(l, tp))*(l+1)/(2*mp.pi**2)*U(l, x)
    return s

if __name__ == "__main__":
    print("nu =", NU, " h+ =", HP, " h- =", HM)
    print("Wronskian checks (should be i):")
    for l in (0, 1, 3):
        for t in (mp.mpf('-0.7'), mp.mpf('0.4'), mp.mpf('1.3')):
            print(f"  l={l} t={float(t):+.2f}  W = {mp.nstr(wronskian(l,t),12)}")
    print("\nEqual-time check: W(t,t,g) mode sum (L terms) vs closed form G(Z), Z = cosh^2 t cos g - sinh^2 t")
    for t in (mp.mpf(0), mp.mpf('0.5'), mp.mpf('1.0')):
        for g in (mp.mpf('1.0'), mp.mpf('2.0')):
            Z = mp.cosh(t)**2*mp.cos(g) - mp.sinh(t)**2
            cf = G_closed(Z)
            row = [f"L={L}: {mp.nstr(mp.re(W_modes(t,t,g,L)),12)}" for L in (50, 150)]
            print(f"  t={float(t):.1f} g={float(g):.1f}  Z={float(Z):+.4f}  G_closed={mp.nstr(cf,12)}  " + "  ".join(row))
