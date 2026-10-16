# IRFormal1: Hadamard coefficients for the Horndeski scalar on de Sitter (n = 0)

Status: numerical extraction with closed forms identified and checked. Not yet derived from the transport equations.

## Setup
- Background: de Sitter, H = 1 (restored in the results), constant scalar background φ̄ (time-dependent case deferred).
- Dictionary: the paper's term −M_P² f(φ) G^{μν}∂φ∂φ is a Horndeski G₅ term with G₅ = M_P² F(φ), F′ = f (up to total derivative). The paper's label G₄ = M_P² f/2 is incorrect.
- Quadratic action for δφ: L₂ = −M_P² f̄ G^{μν}∂δφ∂δφ − ½ V″(φ̄) δφ², with G^{μν} = −3H² g^{μν}.
- Kinetic normalisation: Z = −6H² M_P² f̄. Healthy requires f̄ < 0.
- Mass: m²_eff = V″(φ̄)/Z.
- Metric mixing is exactly zero at quadratic order on this background (every cross term needs ∂φ̄ or ∇∇φ̄, and V′(φ̄) = 0).

## Conventions
- Euclidean S⁴ Green function of (−∇² + m²): G = Γ(h₊)Γ(h₋)/(16π²) ₂F₁(h₊, h₋; 2; (1 + cos μ)/2), with h± = 3/2 ± ν, ν² = 9/4 − m²/H².
- Hadamard form: G = (1/8π²)[U/σ + V ln σ + W], σ = μ²/2 (ℓ = 1).
- U = Δ^{1/2} = (μ/sin μ)^{3/2}; F·σ → 1 at short distance, checked to 12 digits.
- m² = 0 excluded (zero mode, h₋ = 0).

## Results

**V₀** = ½(m²/H² − 2) = ½(m² + (ξ − 1/6)R), with R = 12H², ξ = 0.

**W₀** = (m²/H² − 2)·[ ½(ψ(h₊) + ψ(h₋)) + γ_E − ½ ln 2 ] − m²/(2H²) + 2/3

Numerical check (H = 1; numerical value and closed form agree to 12 digits):

| m²/H² | V₀ (numerical) | V₀ = (m²−2)/2 | W₀ (numerical) | W₀ (closed form) |
|---|---|---|---|---|
| 0.3 | −0.85 | −0.85 | 7.93808006777 | 7.93808006777 |
| 0.5 | −0.75 | −0.75 | 3.90611226701 | 3.90611226701 |
| 1 | −0.5 | −0.5 | 0.90533628721 | 0.90533628721 |
| 2 | 0 (≈ 10⁻²⁶) | 0 | −1/3 | −1/3 |
| 3 | 0.5 | 0.5 | −0.317617817441 | −0.317617817441 |
| 4 | 1 | 1 | 0.133091642954 | 0.133091642954 |

## Consequences
1. **§3.4 (R3) as written is incorrect.** The paper states H_ren(x,x) → 0 by normal ordering. Here W₀ ≠ 0 for generic mass (for example W₀ ≈ 0.905 at m² = H²), so the renormalised coincidence limit does not vanish.
2. **Horizon check not yet done.** On de Sitter, V₀ and W₀ are constant over the space, including the static-patch horizon. The local Rindler check therefore reduces to flat Rindler with U = 1, V = V₀, W = W₀. Still to show: the Wald damping factor → 1 at the bifurcation surface, which depends on the S_Wald difference, not on the Hadamard coefficients.
3. **Mixing:** exactly absent on this background; to be restated for the time-dependent case.

## Still to do
- Higher-order V_n and W_n from the transport equations, to cross-check the numerical method.
- Rindler limit of the Hadamard expansion at the bifurcation surface, and the damping-factor check.
- Sign of f̄ (f̄ < 0) to be stated in the paper.

## Scripts
hadamard_dS.py (numerical extraction) and fitW.py (closed-form fit) are in the same directory as this file.
