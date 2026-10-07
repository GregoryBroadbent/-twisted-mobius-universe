#!/usr/bin/env python3
"""
BTICU 6C: Weight Power Sweep
Find the optimal power α such that A = W^α K W^α gives Δ_e ≈ 1.50

Generalizes Method 2: α=0.5 gives √W K √W (we got Δ_e=1.0)
                      α=0 gives K only (we got Δ_e=2.0)
Interpolate to find α for Δ_e = 1.5
"""

import numpy as np
from datetime import datetime

class WeightPowerSweep:
    """Sweep weight power α to find optimal physics."""

    def __init__(self, N=100, R=1.0, lam=0.5):
        self.N = N
        self.R = R
        self.lam = lam
        self.dellam = R / N

    def modular_weight(self, l):
        return (self.R**2 - l**2) / (2 * self.R)

    def build_kinetic_operators(self):
        """Build K_φ and K_ψ with corrected signs."""
        l_vals = np.arange(self.N) * self.dellam
        beta_vals = self.modular_weight(l_vals)
        beta_interior = beta_vals[1:-1]

        N_interior = len(beta_interior)
        dellam_sq = self.dellam ** 2

        # K_φ (correct signs)
        K_phi = np.diag(2.0/dellam_sq * np.ones(N_interior)) + \
                np.diag(-1.0/dellam_sq * np.ones(N_interior-1), 1) + \
                np.diag(-1.0/dellam_sq * np.ones(N_interior-1), -1)

        # K_ψ (Dirac)
        K_psi = np.zeros((2*N_interior, 2*N_interior), dtype=complex)
        for i in range(N_interior):
            K_psi[i, i] = 2.0 / dellam_sq
            K_psi[N_interior + i, N_interior + i] = 2.0 / dellam_sq

        sigma_y_coupling = 1.0 / self.dellam
        for i in range(N_interior-1):
            K_psi[i, N_interior + i + 1] = -1j * sigma_y_coupling / 2.0
            K_psi[i + 1, N_interior + i] = 1j * sigma_y_coupling / 2.0
            K_psi[N_interior + i, i + 1] = 1j * sigma_y_coupling / 2.0
            K_psi[N_interior + i + 1, i] = -1j * sigma_y_coupling / 2.0

        W_phi = np.diag(beta_interior)
        W_psi = np.diag(np.repeat(beta_interior, 2))

        return K_phi, K_psi, W_phi, W_psi, beta_interior

    def test_weight_power(self, alpha, R=1.0):
        """Test A = W^α K W^α for given power α."""
        K_phi, K_psi, W_phi, W_psi, beta_interior = self.build_kinetic_operators()

        # Raise weights to power α
        W_phi_alpha = np.diag(np.diag(W_phi) ** alpha)
        W_psi_alpha = np.diag(np.diag(W_psi) ** alpha)

        # A = W^α K W^α (conjugation with power α)
        A = W_phi_alpha @ K_phi @ W_phi_alpha
        B = W_psi_alpha @ K_psi @ W_psi_alpha

        N_interior = len(beta_interior)
        N_psi = 2 * N_interior

        # Coupling
        C = np.zeros((N_interior, N_psi), dtype=complex)
        for i in range(N_interior):
            beta_i = beta_interior[i]
            C[i, i] = self.lam * beta_i
            C[i, N_interior + i] = self.lam * beta_i

        # Full K
        K = np.zeros((N_interior + N_psi, N_interior + N_psi), dtype=complex)
        K[:N_interior, :N_interior] = A
        K[:N_interior, N_interior:] = C
        K[N_interior:, :N_interior] = C.T.conj()
        K[N_interior:, N_interior:] = B

        K = (K + K.conj().T) / 2

        # Eigenvalue analysis
        evals = np.linalg.eigvalsh(K)
        min_eig = evals[0]
        is_positive = np.all(evals > -1e-10)

        return min_eig, is_positive, K

    def extract_delta_e(self, alpha):
        """Extract Δ_e for given weight power α."""
        R_vals = np.array([0.1, 0.2, 0.3, 0.5, 1.0])
        E0_vals = []

        for R_test in R_vals:
            solver_test = WeightPowerSweep(N=self.N, R=R_test, lam=self.lam)
            min_eig, is_pos, _ = solver_test.test_weight_power(alpha, R=R_test)

            if is_pos:
                E0_vals.append(max(min_eig, 1e-15))
            else:
                return None  # Not positive-definite

        # Log-log fit
        log_R = np.log(R_vals)
        log_E0 = np.log(np.array(E0_vals))
        coeffs = np.polyfit(log_R, log_E0, deg=1)
        delta_e = -coeffs[0]

        return delta_e

    def sweep_and_find_optimal(self):
        """Sweep α and find which gives Δ_e ≈ 1.50."""
        print("\n" + "="*70)
        print("BTICU 6C: WEIGHT POWER SWEEP")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        print(f"\nGoal: Find α such that A = W^α K W^α gives Δ_e ≈ 1.50")
        print(f"Parameters: N={self.N}, R={self.R}, λ={self.lam}")

        # Sweep α from 0 to 1
        alpha_vals = np.linspace(0, 1, 21)
        delta_e_vals = []

        print(f"\n{'α':<8} {'Δ_e':<10} {'Error':<10} {'Status':<20}")
        print("-"*70)

        for alpha in alpha_vals:
            delta_e = self.extract_delta_e(alpha)

            if delta_e is None:
                print(f"{alpha:<8.2f} {'N/A':<10} {'N/A':<10} {'✗ not pos-def':<20}")
                delta_e_vals.append(None)
            else:
                error = abs(delta_e - 1.50)
                if error < 0.01:
                    status = "✓✓ EXCELLENT"
                elif error < 0.05:
                    status = "✓ GOOD"
                elif error < 0.2:
                    status = "≈ CLOSE"
                else:
                    status = "✗ FAR"

                delta_e_vals.append(delta_e)
                print(f"{alpha:<8.2f} {delta_e:<10.4f} {error:<10.4f} {status:<20}")

        # Find best match
        print("\n" + "="*70)
        print("BEST MATCH")
        print("="*70)

        valid_results = [(a, d) for a, d in zip(alpha_vals, delta_e_vals) if d is not None]
        best_alpha, best_delta_e = min(valid_results, key=lambda x: abs(x[1] - 1.50))

        print(f"\nOptimal weight power: α = {best_alpha:.3f}")
        print(f"  Δ_e = {best_delta_e:.4f}")
        print(f"  Error from target (1.50): {abs(best_delta_e - 1.50):.4f}")

        if abs(best_delta_e - 1.50) < 0.05:
            print(f"\n✓ EXCELLENT MATCH!")
            print(f"  Use A = W^{best_alpha:.3f} K W^{best_alpha:.3f} in production code")
        elif abs(best_delta_e - 1.50) < 0.2:
            print(f"\n≈ Close match. Consider fine-tuning α or λ.")
        else:
            print(f"\n✗ No α in [0,1] gives Δ_e ≈ 1.50")
            print(f"  This suggests a more complex structure is needed")
            print(f"  (e.g., different coupling, boundary conditions, or normalization)")

        print("\n" + "="*70)
        return best_alpha, best_delta_e


if __name__ == "__main__":
    sweep = WeightPowerSweep(N=100, R=1.0, lam=0.5)
    best_alpha, best_delta_e = sweep.sweep_and_find_optimal()
