# IRFormal1: results (de Sitter, constant scalar background)

Status key: DERIVED (symbolic), CHECKED (numerical agreement), FITTED (closed form identified numerically), OPEN, DEFERRED, SUPERSEDED (earlier result replaced; kept for the record).

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
- Note: U = (μ/sin μ)^{3/2} diverges at the antipode μ = π. The Hadamard decomposition is local; it is not a bounded global kernel on S⁴ (see 4b).

## 3. Wald entropy and horizon damping
- Correction ∝ ∂φ∂φ, so on the constant background S_Wald = S_BH everywhere (DERIVED).
- Damping factor exp(−|ΔS|/ħ) ≡ 1 identically: the horizon test passes trivially and tests nothing.
- The G₅ Wald coefficient (paper's eq. 7.1 gives 2π f φ̇²/H², derived for G₄) is OPEN and DEFERRED with the time-dependent case.

## 4. Candidate kernels and tests
### 4a. Original R3 (K vanishes at coincidence): FAILS
- W₀ ≠ 0 for generic mass (e.g. W₀ ≈ 0.905 at m² = H²).

### 4b. Subtraction H̃ = H_ren − ⟨φ²⟩_ren: REJECTED (local tests); global status SUPERSEDED
- Residual of the homogeneous equation at coincidence is nonzero at all masses: +0.0040 (m²=0.3), +0.0032 (1), −0.0203 (3), −0.0300 (4).
- Constant-mode positivity in the normal neighbourhood is mixed in sign: +0.0067 (0.3), +0.0082 (1), −0.079 (3), −0.15 (4).
- Global form: the unregularised H_ren − W₀/8π² contains U, which diverges at the antipode, so it is not a bounded kernel on S⁴ and cannot be tested in reflection positivity as stated.
- Regularised form (cutoff χ(μ), C∞, equal to 1 for μ ≤ π/4 and 0 for μ ≥ π/2): fails S⁴ reflection positivity (section 4f). This is a different kernel from the unregularised one; the rejection applies to the regularised form.

### 4c. Candidate K = G_S (inverse of −∇² + m²): R2 HOLDS (spectral), R3 as written FAILS
- Positivity: spectral weights 1/(ℓ(ℓ+3)+m²) > 0 (DERIVED); spectral sum checked against closed form to ~10⁻⁴ (CHECKED).
- Normalisation: 2π²∫G sin³μ dμ = 1/m² (CHECKED at four masses).
- Resolved earlier discrepancy: the addition theorem has (2ℓ+3)/(3 Vol) C_ℓ(cos μ), not divided by C_ℓ(1).
- Reflection positivity on S⁴ (CHECKED, product integration, section 4g): smallest eigenvalue positive on all three grids (+0.0033, +0.0029, +0.0031 at n = 6, 8, 10). The diagonal is treated by cell averaging, an approximation whose constants are Monte Carlo; the result is supported but not independently verified.

### 4d. Heat kernel K_t = e^{−tL}, L = −∇² + m²: R2 HOLDS, reworded R3 HOLDS
- Positivity by construction (CHECKED).
- Constant mode ∫K_t dV = e^{−tm²} (CHECKED; → 1 as t → 0, so K_t → δ).
- Coincidence: finite; coefficients (4πt)⁻²[1 + a₁t + a₂t² + …] with a₁ = R/6 − m² = 2 − m² and a₂ = −1/15 + (2 − m²)²/2 (CHECKED: extracted a₂ = 0.43333 at m² = 1, error ∝ t).
- a₁ = −2V₀ (for ξ = 0): structural link to the Hadamard coefficient, to be checked in general.
- Reflection positivity on S⁴: passes (section 4f, deterministic quadrature; also in 4g).
- Lorentzian positivity: FAILS for time-separated points (section 4h). The Euclidean pass does not carry over to the continued kernel.
- Free parameter t is unfixed; tying it to the horizon scale would be an assumption.

### 4h. Lorentzian (Wightman-type) pointwise positivity of the continued K_t on global de Sitter (CHECKED, pointwise)
Continuation: Euclidean S⁴ points x with x·y = cos μ continue to global dS points X = (sinh t, cosh t·ω), ω ∈ S³, with Z = X·Y (Lorentzian dot product) and the reflection being t → −t. The Wightman-type matrix is W_ij = K_t(Z_ij − iε(t_i − t_j)), Hermitian by construction. Test: minimum eigenvalue of W over random points, 60 points, three seeds, m² = 1, t_heat = 0.1, H = 1 (lorentz_K.py).

Sanity checks: the matrix on the t = 0 slice (a genuine Euclidean kernel) is positive (+0.0126 on the slice with Z = X·Y; +0.0019 for Euclidean S³ points). The control F(Z) = Z fails, as it should.

| Points | Time extent T (H⁻¹) | Minimum eigenvalue, three seeds |
|---|---|---|
| Both time halves | 0.1 | −0.003, −0.020, −0.012 |
| Both time halves | 0.2 | −0.17, −0.21, −0.13 |
| Future only (t ≥ 0) | 0.1 | +0.010, +0.0007, +0.005 |
| Future only (t ≥ 0) | 0.2 | −0.003, −0.020, −0.011 |
| Future only (t ≥ 0) | 0.5 | −0.35, −0.36, −0.22 |

- The failure is not a regulator artefact: changing ε from 0.2 to 0.001 leaves the minimum eigenvalues unchanged to about three digits.
- Result: the continued K_t is not a positive Wightman kernel once the time extent exceeds about 0.1–0.2 H⁻¹. Its pass on S⁴ (section 4f) does not carry over to Lorentzian positivity.
- Interpretation: continuing e^{−τL} gives e^{−itL}, which is unitary rather than positive, so the failure is consistent with the structure. The Euclidean test probes reflections across the equator with smooth hemisphere functions; the Lorentzian test probes time-separated configurations and is a stronger condition.
- Caveats: pointwise random sets, not smeared functions, so this is a necessary condition, not a proof. Minimum eigenvalues vary by about a factor of 10 between seeds, so the signs are the reliable content.

### 4i. Lorentzian positivity of G_S by spatial-harmonic sectors on global de Sitter (CHECKED, with a regulator caveat)
Decompose the Wightman-type kernel W(t,ω; t′,ω′) = F(Z − iε(t − t′)) into spatial S³ harmonics: each sector ℓ is the time kernel w_ℓ(t,t′) = ∫F(Z − iε(t − t′)) U_ℓ(x)√(1−x²)dx, with U_ℓ the Chebyshev polynomial of the second kind (the S³ Gegenbauer C_ℓ^{(1)}). Positivity requires each Hermitian matrix [w_ℓ(t_i,t_j)] to be positive semidefinite. Script: lorentz_GS_modes.py. Time points: 20–30 random points in |t| ≤ T, m² = 1, H = 1.

| Kernel | Sector | Time extent T | Min eigenvalue |
|---|---|---|---|
| G_S | ℓ = 0 to 4 | 0.3 | +1.5 × 10⁻⁴ (ℓ = 0) to +7 × 10⁻⁴ (ℓ = 4), ε = 0.05 |
| G_S | ℓ = 0 | 1.0 and 1.5 | +1.6 × 10⁻⁴ and +1.0 × 10⁻⁴, ε = 0.05 |
| G_S | ℓ = 0 | 0.3 | ε = 0.1: +2.1 × 10⁻⁴; ε = 0.02: +8.7 × 10⁻⁵; ε = 0.01: +6.5 × 10⁻⁵; ε = 0.005: +4.5 × 10⁻⁵ |
| K_t | ℓ = 0 | 0.1, 0.2, 0.3 | −0.020, −0.083, −0.21 |
| Control F(Z) = Z | ℓ = 0 | 0.3 | −0.84 |

- Stable under quadrature refinement (NX from 4000 to 16000) and time window (T up to 1.5).
- K_t fails robustly in ℓ = 0, consistent with 4h.
- G_S is positive in every sector tested, but its smallest eigenvalue falls as ε is reduced, roughly logarithmically. Extrapolating that trend would cross zero near ε ≈ 10⁻³. The trend is not resolved: it may be a limit of the regulator and quadrature, or the limit may be borderline. The ε → 0 limit is therefore OPEN.
- To settle it, use the exact Bunch–Davies mode functions on the global slicing instead of the iε regulator. That is the next check.

### 4e. Entropy-weighted operator L = −∇² + m² + κS_Wald(x)
- On the constant background S_Wald is constant, so this only shifts m². Untested; the mechanism needs φ̇ ≠ 0 (DEFERRED).

### 4f. Euclidean reflection positivity on S⁴ (CHECKED, deterministic quadrature)
Test: Gaussian test functions f_i(x) = exp(−|x − c_i|²/(2s²)) restricted to the positive hemisphere x₀ > 0 of S⁴ ⊂ R⁵, with s = 0.6 and four centres c_i in the hemisphere (seed 7). Quadratic form Q_ij = ∫∫ f_i(x)[K(x·y) − K(x·Θy)] f_j(y), with Θ flipping x₀. m² = 1, H = 1, t = 0.1 for K_t.

Quadrature: product Gauss rule on the hemisphere, in coordinates x = (cos χ, sin χ·u), u ∈ S³ (ψ, θ, φ). The hemisphere volume matches 4π²/3 to 10⁻⁹ at n = 8. Only K is applied to four vectors, in row chunks.

| Grid n | Hemisphere nodes | K_t smallest eigenvalue | Regularised control smallest eigenvalue |
|---|---|---|---|
| 6 | 2,592 | +0.011209 | −0.077779 |
| 8 | 8,192 | +0.011010 | −0.076557 |
| 10 | 20,000 | +0.010998 | −0.076899 |

- n = 10 spectra: K_t: 0.010998, 0.055935, 0.096336, 0.675675; regularised control: −0.076899, −0.011890, −0.006564, −0.000933.
- From n = 8 to n = 10 the smallest eigenvalues change by 0.1% (K_t) and 0.4% (control).
- Result: K_t is positive; the regularised subtraction control is negative in all four directions. G_S is tested separately (4g).
- The unregularised control is not tested (ill-defined at the antipode, 4b).
- Diagonal entries are included exactly for K_t; the regularised control is set to 0 on the diagonal, where it vanishes at coincidence.

SUPERSEDED: the earlier pointwise test (5 points) and the Monte Carlo smeared test (N = 600 and N = 2000, five seeds; K_t +0.003 to +0.057, G_S +0.003 to +0.041, control −0.053 to −0.097) used points on S³ ⊂ R⁴ with the S⁴ kernel. They are not valid as S⁴ tests and are retained only for the record in the calculation folder. Monte Carlo on S⁴ has not been run.

### 4g. G_S reflection positivity on S⁴ (CHECKED, product integration)
Same test functions as 4f but with a C∞ equatorial cutoff, h(x₀) = 0 for x₀ ≤ 0 and 1 for x₀ ≥ 0.3, so the spectral projections decay quickly. Kernels: G_S in closed form; K_t and the regularised control on the same nodes for comparison.

Diagonal treatment (product integration): each diagonal entry K_aa is replaced by the average of G_S over a 4-ball of volume w_a (the node's quadrature weight),
K_eff(r) = A₁/(4π²r²) + (1/8π²)[½ + W₀ + V₀(ln r² + B₁ − ln 2)], r = (2w_a/π²)^{1/4},
with A₁ = E[1/|u|²] ≈ 1.3331 and B₁ = E[ln|u|²] ≈ 0.0833 for u = x − y, x and y uniform in the unit 4-ball (Monte Carlo, 2×10⁷ pairs). The expansion uses G_S = 1/(4π²μ²) + (1/8π²)[½ + W₀ + V₀ ln(μ²/2)] + O(μ² ln μ).

Why not spectral truncation: summing G_S = Σ_ℓ P_ℓ/(λ_ℓ + m²) to a cutoff L gave a diagonal that grows with L. At n = 8 the smallest eigenvalue changed by 74% between L = 40 and L = 60, so the result was dominated by quadrature rather than by G_S (CHECKED, superseded by product integration).

| Grid n | Nodes | G_S smallest eig | K_t smallest eig | Regularised control smallest eig |
|---|---|---|---|---|
| 6 | 2,592 | +0.003268 | +0.009949 | −0.073320 |
| 8 | 8,192 | +0.002926 | +0.008746 | −0.067942 |
| 10 | 20,000 | +0.003099 | +0.009173 | −0.070202 |

- n = 10 spectra: G_S 0.003099, 0.014857, 0.024508, 0.195283; K_t 0.009173, 0.049255, 0.082256, 0.609720; control −0.070202, −0.010469, −0.005928, −0.000834.
- Changes from n = 8 to n = 10: G_S +5.9%, K_t +4.9%, control −3.3%. The G_S sequence is not monotone, so the value is good to about ±5%.
- Result: G_S and K_t are positive on every grid; the regularised control is negative on every grid. Signs are stable; magnitudes are not converged beyond about 5%.
- Caveats: the cell-average constants (A₁, B₁) are Monte Carlo; the cell is treated as flat; the smooth test functions differ from those in 4f, so K_t and control values are not comparable across the two tables (the 4f values at n = 10 were K_t +0.01100 and control −0.07690). The n = 10 run took about 52 minutes.

## 5. Reworded R3
"The coincidence structure of K_t is local." Status: satisfied by the heat kernel (4d). Not satisfied by the original H_ren (W₀ ≠ 0) or by G_S.

## 6. Open and deferred
- RESULT (4h): the continued K_t fails pointwise Lorentzian positivity for time-separated points. K_t is therefore not an acceptable candidate kernel for the Lorentzian theory, unless the framework's K is defined differently from the heat kernel.
- OPEN: Lorentzian positivity for G_S. Harmonic-sector test (4i) is positive in ℓ = 0–4 for T up to 1.5 and ε ≥ 0.005, but the smallest eigenvalue falls as ε → 0 and the limit is unresolved. Exact Bunch–Davies mode functions are needed.
- OPEN: identify the paper's bi-scalar K with a continued Euclidean object, and check it against 4h.
- OPEN: G_S reflection positivity on S⁴ is supported to about ±5% by product integration (4g). Verifying the cell-average diagonal independently (e.g. a finer local quadrature around each node, or a Galerkin harmonic basis) is the next check.
- OPEN: the unregularised subtraction H_ren − W₀/8π² is singular at the antipode; decide whether a global definition of the subtraction is needed or whether the regularised form is the relevant object.
- OPEN: general (all ξ) check of a₁ = −2V₀ link.
- OPEN: time-dependent background, G₅ Wald-entropy coefficient, horizon damping test (DEFERRED to paper two).
- OPEN: fix t (heat-kernel time) and the entropy-weighted extension.
- Paper text: the G₄ label and §3.4 (R3) and §5.2 (horizon) need correcting before submission.
