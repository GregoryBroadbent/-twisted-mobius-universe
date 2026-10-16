# IRFormal1: results (de Sitter, constant scalar background)

Status key: DERIVED (symbolic), CHECKED (numerical agreement), FITTED (closed form identified numerically), OPEN, DEFERRED.

## 1. Setup
- Background: de Sitter, H = 1 (restored in results), constant scalar φ̄, so ∂φ̄ = 0 and V′(φ̄) = 0. Time-dependent background deferred.
- Dictionary (DERIVED): the paper's term −M_P² f(φ) G^{μν}∂φ∂φ is Horndeski G₅ with G₅ = M_P² F(φ), F′ = f, up to total derivative. The paper's label G₄ = M_P² f/2 is incorrect.
- Quadratic action for δφ (DERIVED): L₂ = −M_P² f̄ G^{μν}∂δφ∂δφ − ½V″δφ², with G^{μν} = −3H² g^{μν}.
- Kinetic normalisation: Z = −6H² M_P² f̄. Healthy requires f̄ < 0 (signature −+++). Mass m²_eff = V″/Z.
- Metric mixing: exactly zero at quadratic order on this background (every cross term needs ∂φ̄ or ∇∇φ̄; V′ = 0). Limitation restated for the time-dependent case.

## 2. Hadamard coefficients (ℓ = 1/H)
Form: G = (1/8π²)[U/σ + V ln σ + W], σ = μ²/2, U = (μ/sin μ)^{3/2}.

- V(σ) = V₀ ₂F₁(h₊, h₋; 2; (1 − cos μ)/2), with V₀ = (m² − 2)/2 (DERIVED: log coefficient solves the homogeneous equation, regular at origin).
- V₀ = (m² − 2)/2 (DERIVED, CHECKED)
- V₁ = m²(m² − 2)/8 (DERIVED, CHECKED: numerical fit agrees to ≤ 10⁻¹³)
- V₂ = m²(m² − 2)(m² + 2)/96 (DERIVED, CHECKED: agreement ≤ 10⁻⁹)
- W₀ (CHECKED): closed form (m² − 2)[½(ψ(h₊)+ψ(h₋)) + γ_E − ½ ln 2] − m²/2 + 2/3 matches numerics to 15 digits at six masses. Its constant is fixed by regularity at the antipode μ = π (the 2F1 solution is the only one regular there), so it is not a free fit.
- ℓ-dependence: W_ℓ = W₁ + V₀ ln ℓ².
- Local recursion alone fixes V_n and leaves W_n determined by one global constant (DERIVED).

## 3. Wald entropy and horizon damping
- Correction ∝ ∂φ∂φ, so on the constant background S_Wald = S_BH everywhere (DERIVED).
- Damping factor exp(−|ΔS|/ħ) ≡ 1 identically: the horizon test passes trivially and tests nothing.
- The G₅ Wald coefficient (paper's eq. 7.1 gives 2π f φ̇²/H², derived for G₄) is OPEN and DEFERRED with the time-dependent case.

## 4. Candidate kernels and tests
### 4a. Original R3 (K vanishes at coincidence): FAILS
- W₀ ≠ 0 for generic mass (e.g. W₀ ≈ 0.905 at m² = H²).

### 4b. Subtraction H̃ = H_ren − ⟨φ²⟩_ren: REJECTED
- Residual of the homogeneous equation at coincidence is nonzero at all masses: +0.0040 (m²=0.3), +0.0032 (1), −0.0203 (3), −0.0300 (4).
- Constant-mode positivity in the normal neighbourhood is mixed in sign: +0.0067 (0.3), +0.0082 (1), −0.079 (3), −0.15 (4).

### 4c. Candidate K = G_S (inverse of −∇² + m²): R2 HOLDS, R3 as written FAILS
- Positivity: spectral weights 1/(ℓ(ℓ+3)+m²) > 0 (DERIVED); spectral sum checked against closed form to ~10⁻⁴ (CHECKED).
- Normalisation: 2π²∫G sin³μ dμ = 1/m² (CHECKED at four masses).
- Resolved earlier discrepancy: the addition theorem has (2ℓ+3)/(3 Vol) C_ℓ(cos μ), not divided by C_ℓ(1).
- Lorentzian continuation of positivity: OPEN.

### 4d. Heat kernel K_t = e^{−tL}, L = −∇² + m²: R2 HOLDS, reworded R3 HOLDS
- Positivity by construction (CHECKED).
- Constant mode ∫K_t dV = e^{−tm²} (CHECKED; → 1 as t → 0, so K_t → δ).
- Coincidence: finite; coefficients (4πt)⁻²[1 + a₁t + a₂t² + …] with a₁ = R/6 − m² = 2 − m² and a₂ = −1/15 + (2 − m²)²/2 (CHECKED: extracted a₂ = 0.43333 at m² = 1, error ∝ t).
- a₁ = −2V₀ (for ξ = 0): structural link to the Hadamard coefficient, to be checked in general.
- Free parameter t is unfixed; tying it to the horizon scale would be an assumption.

### 4e. Entropy-weighted operator L = −∇² + m² + κS_Wald(x)
- On the constant background S_Wald is constant, so this only shifts m². Untested; the mechanism needs φ̇ ≠ 0 (DEFERRED).

## 5. Reworded R3
"The coincidence structure of K_t is local." Status: satisfied by the heat kernel (4d). Not satisfied by the original H_ren (W₀ ≠ 0) or by G_S.

## 6. Open and deferred
- OPEN: Lorentzian continuation of the R2 positivity for K_t and G_S.
- OPEN: general (all ξ) check of a₁ = −2V₀ link.
- OPEN: time-dependent background, G₅ Wald-entropy coefficient, horizon damping test (DEFERRED to paper two).
- OPEN: fix t (heat-kernel time) and the entropy-weighted extension.
- Paper text: the G₄ label and §3.4 (R3) and §5.2 (horizon) need correcting before submission.
