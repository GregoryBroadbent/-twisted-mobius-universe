# Symbolic Hadamard recursion on de Sitter (H=1), Euclidean S^4.
# Radial ODE away from coincidence:  G'' + 3 cot(mu) G' - m2 G = 0   (G as function of geodesic distance mu)
# Ansatz: 8 pi^2 G = U/sigma + V(sigma) ln(sigma) + W(sigma),  sigma = mu^2/2
#   U = (mu/sin mu)^{3/2},  V = sum_n V_n sigma^n,  W = sum_n W_n sigma^n
# ln(sigma) = 2 ln(mu) - ln 2 ; the ODE is split by powers of ln(mu) and of mu.
import sympy as sp

mu, m2, Lm = sp.symbols('mu m2 Lm', positive=True)   # Lm stands for ln(mu)
N = 3
Vc = sp.symbols('V0:%d' % N)
Wc = sp.symbols('W0:%d' % N)

sig = mu**2/2
U = (mu/sp.sin(mu))**sp.Rational(3, 2)
V = sum(Vc[n]*sig**n for n in range(N))
W = sum(Wc[n]*sig**n for n in range(N))
lnsig = 2*sp.log(mu) - sp.log(2)
F = U/sig + V*lnsig + W

ode = sp.diff(F, mu, 2) + 3*sp.cot(mu)*sp.diff(F, mu) - m2*F
ode = ode.subs(sp.log(mu), Lm)           # now a polynomial in Lm (log terms)
ode = sp.expand(ode)

# Expand each Lm-coefficient as a Laurent series in mu
eqs = []
for p in range(0, 3):
    cp = ode.coeff(Lm, p)
    if cp == 0:
        continue
    ser = sp.expand(sp.series(cp, mu, 0, 2*N - 2).removeO())
    for k in range(-3, 2*N - 2):
        ck = sp.simplify(ser.coeff(mu, k))
        if ck != 0:
            eqs.append((p, k, sp.expand(ck)))

print('Equations by (power of ln mu, power of mu):')
for p, k, e in eqs[:10]:
    print('  Lm^%d mu^%d :' % (p, k), sp.factor(e))

# Solve the Lm^0 equations order by order (the Lm^1 equations fix V alone)
lin = [e for p, k, e in eqs]
sol = sp.solve(lin, list(Vc) + list(Wc), dict=True)
print('\nSolutions:')
for s in sol:
    for k in list(Vc) + list(Wc):
        if k in s:
            print('  %s = %s' % (k, sp.factor(s[k])))
    free = [x for x in list(Vc)+list(Wc) if x not in s]
    print('  free:', free)
