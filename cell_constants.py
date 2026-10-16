# Cell-average constants for the G_S self-term on a 4-ball of unit radius.
# A1 = E[1/|u|^2], B1 = E[ln |u|^2] for u = x - y, x, y uniform in the unit 4-ball (Monte Carlo, 2e7 pairs).
import numpy as np
rng = np.random.default_rng(1)
def ball(M):
    g = rng.normal(size=(M, 4)); g /= np.linalg.norm(g, axis=1, keepdims=True)
    r = rng.uniform(size=(M, 1))**0.25
    return g*r
tot1 = 0.0; totl = 0.0; cnt = 0
for _ in range(20):
    x = ball(10**6); y = ball(10**6)
    d2 = np.sum((x-y)**2, axis=1)
    tot1 += np.sum(1/d2); totl += np.sum(np.log(d2)); cnt += len(d2)
print('A1 = %.6f' % (tot1/cnt), ' B1 = %.6f' % (totl/cnt), ' samples', cnt)
