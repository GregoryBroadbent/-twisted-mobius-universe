# BTICU 3 — The Elliptic Observer's Entropy

Gregory P. Broadbent · Sep 30, 2026 · working draft

## Status and purpose

BTICU 2 found that in every consistent quantum construction of elliptic de Sitter space, dS/ℤ₂, the antipodal identification leaves no trace in the correlations any observer can measure. It left one place open: the state itself. On ordinary de Sitter space, the Euclidean path integral over the sphere prepares a pure no-boundary wavefunction. On the elliptic space it cannot, and Dulac and Wei (2026) propose that it instead defines a no-boundary density matrix for each observer's region, whose entropy they compute for a two-dimensional free fermion.

This paper asks what that entropy says about the twist. It works from their construction and results, derives the structure behind them in the language of this series, extracts the excess entropy relative to ordinary de Sitter space, and asks whether any of it is observable.

## 1. The observer's partition function

Euclidean de Sitter space is the sphere S^(d+1) of radius 1/H. In static coordinates adapted to an observer,

X⁰ = (1/H) cos θ sin(Hτ),  X^(d+1) = (1/H) cos θ cos(Hτ),  X^i = (1/H) sin θ · n^i,

where τ is the observer's Euclidean time, periodic with period 2π/H, and n is a unit vector on the sphere of directions S^(d−1). The antipodal map X → −X acts as

**τ → τ + π/H,  n → −n:**

a shift by half the Euclidean time period, combined with the antipodal map on the sphere of directions, which is spatial parity P for the observer. It has no fixed points, so the quotient RP^(d+1) is smooth.

Writing each partition function as a trace over the observer's states, with K the static-patch Hamiltonian (the generator of τ):

**Z(S^(d+1)) = Tr e^(−2πK/H),  Z(RP^(d+1)) = Tr(e^(−πK/H) · P).**

The first is the familiar statement that the de Sitter observer is thermal at the Gibbons–Hawking temperature H/2π. The second is its elliptic counterpart, given for d = 1 by Dulac and Wei: the identification halves the Euclidean time circle and inserts a parity twist. Halving the circle alone would mean a temperature of H/π, twice the Gibbons–Hawking value; the parity twist is what prevents that reading, as Section 2 shows.

## 2. The parity grading

For a free scalar field, the observer's modes are labelled by a frequency ω and an angular momentum ℓ on the sphere of directions, and the parity P acts on each quantum as (−1)^ℓ. Each mode then contributes to the two partition functions as

|  | Ordinary de Sitter, Z(S^(d+1)) | Elliptic de Sitter, Z(RP^(d+1)) |
| --- | --- | --- |
| Even ℓ | 1 / (1 − e^(−2πω/H)) | 1 / (1 − e^(−πω/H)) |
| Odd ℓ | 1 / (1 − e^(−2πω/H)) | 1 / (1 + e^(−πω/H)) |

The twist grades the observer's spectrum by parity:

- **Even modes** carry Boltzmann weights e^(−πωn/H), as if at temperature H/π, twice the Gibbons–Hawking value.
- **Odd modes** carry weights (−1)^n e^(−πωn/H), alternating in sign with the number of quanta n.

The negative weights mean that e^(−πK/H)·P is not a density matrix: it has negative eigenvalues. As Dulac and Wei note, the full static patch cannot be assigned a state, not even as a limit. Only regions strictly smaller than the static patch have genuine no-boundary density matrices, obtained from the path integral with a cut along that region.

This is the state-level form of the even/odd sorting that ran through BTICU 0 and BTICU 1. There it appeared as a partition of correlations (removed by BTICU 2) and as the brane fold's selection of modes. Here it is a grading of the observer's spectrum, in which the even sector looks thermal at double temperature and the odd sector has no thermal reading at all. It is not the cos²(&/2) : sin²(&/2) partition, and no fixed ratio follows from it.

## 3. The excess entropy

For the free Dirac fermion (central charge c = 1) in two-dimensional de Sitter space with unit radius, take an interval of angular size Δφ on the t = 0 slice. The two entanglement entropies are:

- **Ordinary de Sitter** (the pure Bunch–Davies state on the circle, the standard conformal-field-theory result): S = (1/3) ln\[(2/ε) sin(Δφ/2)\].
- **Elliptic de Sitter** (Dulac and Wei's no-boundary density matrix, for Δφ < π): S = (1/3) ln\[(2/ε) tan(Δφ/2)\].

Here ε is the ultraviolet cutoff. It cancels in the difference, which is finite and universal:

**ΔS = S\_elliptic − S\_ordinary = (1/3) ln sec(Δφ/2).**

| Interval Δφ | ΔS |
| --- | --- |
| π/6 | 0.012 |
| π/3 | 0.048 |
| π/2 | 0.116 |
| 2π/3 | 0.231 |
| 5π/6 | 0.451 |
| → π | diverges |

Three properties follow directly:

- **Always positive.** The elliptic region always carries more entanglement than the same region in ordinary de Sitter space.
- **Small for small regions.** For Δφ ≪ 1, ΔS ≈ Δφ²/24, so the excess is quadratically suppressed for regions much smaller than the horizon.
- **Divergent as the region approaches the whole slice.** The elliptic slice has length π, so Δφ → π is the full space. The divergence is the entropy-level statement that the elliptic space has no global pure state, matching its one-dimensional global Hilbert space (BTICU 2).

The Rényi entropies of both states obey S^(n) = ½(1 + 1/n)·S, so the same excess appears, rescaled, at every replica index.

## 4. Interpretation and observability

**What the excess means.** The elliptic no-boundary density matrix is closely related to crosscap states in conformal field theory, whose lattice analogues are "entangled antipodal pair" states: every degree of freedom is maximally entangled with its antipode. The excess ΔS is the entanglement a region carries with its own antipodal image. In ordinary de Sitter space a region is entangled only with its complement; in the elliptic space part of that complement is the region itself, seen through the twist. This is the one place where the twist survives in consistent quantum field theory: not as a correlation between observable quantities, but as a property of the state.

**Is it observable?** Not with current or foreseeable cosmological data, for three reasons:

1. **Entropy is not a correlation.** Entanglement entropy of quantum fields is not measured directly by telescopes. Cosmological observations give correlation functions, which BTICU 2 showed are unchanged.
2. **The excess is small where observers live.** For regions much smaller than the horizon, ΔS ≈ Δφ²/24 in two dimensions; the suppression is expected to persist in four.
3. **The large excess sits at the horizon scale,** where an observer's region approaches the edge of their static patch and the density-matrix interpretation itself breaks down.

The elliptic identification is therefore, as far as this analysis reaches, observationally indistinguishable from ordinary de Sitter space, while differing in the entanglement structure of its quantum state. That is a genuine physical difference, of the kind discussed in quantum-gravity approaches to de Sitter space, but not a cosmological prediction.

## 5. Four dimensions: the conformally coupled scalar

**Method.** For a free field the no-boundary density matrix of a region A is Gaussian, so its entropy is fixed by the two-point functions of φ and its conjugate momentum π restricted to A. On RP⁴ these follow from the sphere by the method of images. At t = 0 the Euclidean time reflection flips the sign of π at the image point, giving the crosscap structure

⟨φφ⟩\_elliptic = X + X·R,  ⟨ππ⟩\_elliptic = P − P·R,

where X and P are the ordinary Bunch–Davies correlators and R is the antipodal map on the slice. For a conformally coupled scalar, the t = 0 slice of de Sitter space is a unit three-sphere carrying the conformal vacuum (normal-mode frequencies n + 1). We discretised the polar angle χ of the three-sphere, decomposed into angular momenta ℓ on the S² (where R acts as χ → π − χ with a factor (−1)^ℓ), and took A to be a cap of geodesic radius χ₀ in units of the de Sitter radius. Checks:

- The lattice reproduces the spectrum n + 1 to 0.2% or better.
- The excess entropy is finite: the sum over ℓ converges exponentially, and the ultraviolet cutoff cancels, as in two dimensions.
- Lattice convergence at χ₀ ≈ 0.79: ΔS = 0.03746, 0.03751, 0.03752 for 100, 200 and 400 points.

**Expectation stated before the scan.** Treating the image as a perturbation, and using the scalar's dimension Δ = 1, the excess was expected to scale as χ₀⁴, faster than two dimensions.

**Result.**

| Cap radius χ₀ | Even-ℓ sectors | Odd-ℓ sectors | Total ΔS |
| --- | --- | --- | --- |
| 0.068 | 3.60 × 10⁻⁴ | −1.0 × 10⁻⁶ | 3.59 × 10⁻⁴ |
| 0.130 | 1.38 × 10⁻³ | −1.5 × 10⁻⁵ | 1.36 × 10⁻³ |
| 0.256 | 5.44 × 10⁻³ | −2.2 × 10⁻⁴ | 5.22 × 10⁻³ |
| 0.506 | 2.25 × 10⁻² | −3.7 × 10⁻³ | 1.89 × 10⁻² |
| 0.757 | 5.78 × 10⁻² | −2.2 × 10⁻² | 3.56 × 10⁻² |

- **The even sectors scale as χ₀²**, with fitted exponent 2.04–2.06 for small caps and coefficient ΔS ≈ 0.08 χ₀². They dominate.
- **The odd sectors scale as χ₀⁴**, with fitted exponent 4.0, and contribute negatively: the odd-parity part of the elliptic region is less entangled than in ordinary de Sitter space.
- **So the quadratic suppression persists in four dimensions.** The prior expectation of χ₀⁴ was wrong for the total, though correct for the odd sectors alone. For comparison, the two-dimensional result is ΔS ≈ r²/6 for an interval of half-length r.

**A positivity limit.** In the odd sectors the restricted correlators approach, and above a cap radius of about 0.75 detectably violate, the uncertainty bound that any quantum state must satisfy (violations exceed 10⁻⁹ there and grow rapidly; below it any violation is under 10⁻⁹, at the level of numerical precision). The no-boundary density matrix of this field is therefore well defined only for caps somewhat less than half the static-patch radius (π/2). This is the parity grading of Section 2 appearing inside a subregion: the odd sector, whose weights alternate in sign, is where positivity fails. Values beyond χ₀ ≈ 0.75 are not entropies of a state and are not reported.

### 5.1 The even-sector coefficient and other masses

**Mechanism.** Three controlled variations of the conformal case, at caps χ₀ ≈ 0.025–0.14 on an 800-point lattice, isolate the source of the χ₀² term:

- Scaling the image term by one half halves ΔS: the excess is linear in the image.
- Keeping only the image in ⟨φφ⟩ (setting the momentum image to zero) reproduces the full result to three digits.
- Keeping only the momentum image gives ΔS/χ₀² ≈ 0.0000–0.0002: it contributes only at higher order.

The image changes ⟨φ²⟩ by an amount that is nearly constant across a small cap, δ⟨φ²⟩ = G(Z = −1), the field's correlation with its own antipode. The data therefore point to an area-law form

**ΔS ≈ κ · A · δ⟨φ²⟩,  with A the area of the cap's boundary and δ⟨φ²⟩ = H² Γ(Δ₊)Γ(Δ₋)/(16π²),**

which is the structure of the boundary (contact) term to which free-scalar entanglement entropy is known to be sensitive. Section 5.2 derives κ.

**The conformal coefficient.** For the conformal scalar, A = 4πχ₀²/H² and Γ(Δ₊)Γ(Δ₋) = 1, so ΔS ≈ κχ₀²/(4π). The coefficient converges slowly with lattice size (roughly as 1/N). Extrapolating ΔS/χ₀² from 400, 800 and 1,400 points, and then to small caps, gives

ΔS/χ₀² → 0.0833 ± 0.0003,  so κ ≈ 1.047 ± 0.004.

This is numerically consistent with ΔS = χ₀²/12, equivalently κ = π/3, a value obtained here first as a fit and then derived independently in Section 5.2.

**Other masses: a test of the mechanism.** If the area-law form holds with a universal κ, then for any scalar the ratio of its coefficient to the conformal one must equal Γ(Δ₊)Γ(Δ₋). This prediction was stated before the runs. The Bunch–Davies state for each mass was constructed from the Euclidean hemisphere (regularity at the pole), a method checked to reproduce the conformal frequencies n + 1 exactly. At χ₀ ≈ 0.1 on a 1,000-point lattice:

| m²/H² | Predicted ratio Γ(Δ₊)Γ(Δ₋) | Measured ratio | Measured / predicted |
| --- | --- | --- | --- |
| 0.5 | 8.92 | 8.60 | 0.963 |
| 1.0 | 3.37 | 3.32 | 0.984 |
| 2.0 (conformal) | 1 | 1 | — |
| 3.0 | 0.412 | 0.415 | 1.009 |
| 6.0 | 0.0573 | 0.0581 | 1.015 |

The prediction holds to within 4% across a range of 150 in the coefficient, with a small systematic trend (light fields slightly below, heavy fields slightly above) consistent with finite-cap corrections at χ₀ = 0.1. Two consequences:

- **Light fields carry the largest excess.** As m → 0, Γ(Δ₋) ≈ 3H²/m², so the excess grows as 1/m².
- **Heavy fields carry exponentially little.** For m > 3H/2, Γ(Δ₊)Γ(Δ₋) = |Γ(3/2 + iμ)|² falls roughly as e^(−πμ). In a consistent state, the antipodal effect of heavy fields is Boltzmann-suppressed, the opposite of the naive kernel's heavy-field dominance in BTICU 0 §5.

### 5.2 A derivation of κ

A constant shift of ⟨φ²⟩ over the cap lives entirely in the ℓ = 0 sector, so the coefficient can be derived there. In the small-cap limit the cap is a flat ball of radius R = χ₀/H, and corrections are of relative order χ₀².

**Step 1: the ℓ = 0 sector is a one-dimensional boundary problem.** Write φ₀₀(r) for the ℓ = 0 component of the field and set u = r·φ₀₀. For a massless scalar in 3 + 1 dimensions, the ℓ = 0 Hamiltonian is exactly

H₀ = ½ ∫₀^∞ dr (π\_u² + u′²),  with u(0) = 0,

a free massless field on a half-line with a Dirichlet boundary at the centre. The cap becomes the interval \[0, R\] attached to that boundary.

**Step 2: its modular Hamiltonian is known.** For an interval adjacent to the boundary of a two-dimensional boundary conformal field theory in its vacuum, the modular Hamiltonian is local:

K₀ = 2π ∫₀^R β(r) · ½(π\_u² + u′²) dr,  β(r) = (R² − r²)/(2R).

**Step 3: the image shift is a gradient shift.** A constant δ⟨φ²⟩ = c in four dimensions gives δ⟨u(r)u(r′)⟩ = 4πc·r r′ in the ℓ = 0 sector (the 4π from the angular normalisation), so δ⟨u′²⟩ = 4πc, a constant, while δ⟨π\_u²⟩ is of order r² and contributes only at higher order.

**Step 4: the first law.** To first order, δS = δ⟨K₀⟩:

δS = 2π · ½ · 4πc · ∫₀^R β(r) dr = 4π²c · R²/3 = **(π/3) · (4πR²) · c.**

So κ = π/3 ≈ 1.0472, against the extrapolated numerical value 1.047 ± 0.004. The derivation was found after the numerical value was known, but it uses no numerical input. With δ⟨φ²⟩ = H²Γ(Δ₊)Γ(Δ₋)/(16π²),

**ΔS ≈ A H² Γ(Δ₊)Γ(Δ₋) / (48π),**

which for the conformal scalar is ΔS ≈ χ₀²/12. Because a cap much smaller than both H⁻¹ and m⁻¹ sees an effectively conformal vacuum, κ is the same for every scalar mass at leading order, as the mass test in 5.1 found.

**Why a naive argument gives zero.** Applying the conformal modular Hamiltonian in four dimensions directly, with either the canonical or the improved stress tensor, a constant δ⟨φ²⟩ appears to cost nothing: it has no gradient. The ℓ = 0 reduction shows why that is incorrect for the actual state. The change of variables u = rφ turns a constant shift of ⟨φ²⟩ into a constant shift of ⟨u′²⟩, which the modular Hamiltonian does weigh. This is the free-scalar sensitivity to ⟨φ²⟩ at the entangling region that 5.1 anticipated, here obtained as a calculation.

### 5.3 Fermions and gauge fields: predictions

The scalar's χ₀² term is a first-order effect that relies on the ⟨φ²⟩ contact structure. Fields without it should behave differently. Two general facts fix the expectation:

- **The image leaves no first-order energy for conformal fields.** The image's contribution to ⟨T\_μν⟩ is smooth and invariant under the full de Sitter group (the antipodal map commutes with it), so it is proportional to g\_μν; for a conformal field it must also be traceless, so it vanishes. With a local conformal modular Hamiltonian and no contact term, δS = δ⟨K⟩ = 0 at first order.
- **The leading term is then second order** in the image correlator, scaling as R^(4Δ), where Δ is the field's scaling dimension.

Two existing results check this rule:

| Case | Δ | Predicted leading power | Found |
| --- | --- | --- | --- |
| Two-dimensional Dirac fermion (Dulac and Wei) | 1/2 | R² | ΔS ≈ Δφ²/24, so R² |
| Four-dimensional scalar, odd-ℓ sectors (no ℓ = 0 contact) | 1 | R⁴ | exponent 4.0 |

On that basis:

- **Dirac fermion in four dimensions** (Δ = 3/2): ΔS ∝ χ₀⁶ at leading order, with sign and coefficient undetermined. The fermion requires a pin structure on the elliptic space; RP⁴ admits pin⁺ structures, so the construction exists for that choice.
- **Maxwell field** (field strength with Δ = 2): the second-order rule gives χ₀⁸. Gauge fields do carry their own boundary (edge-mode) contribution, set by the normal electric field on the entangling surface. A constant image shift cannot feed it at first order, because the total electric flux through a closed surface vanishes without charge, which removes the constant mode. So the edge term is expected to enter only at higher order as well, but this is an argument, not a calculation.

These are predictions, stated before any fermion or gauge-field computation.

### 5.4 Attempted test of the fermion prediction

Before building a four-dimensional Dirac lattice, the fermionic image construction was calibrated against the one exact result available, Dulac and Wei's two-dimensional Dirac fermion, S = (1/3) ln\[(2/ε) tan(Δφ/2)\], an excess of +(1/3) ln sec(Δφ/2) over global de Sitter space.

**The model.** A half-filled tight-binding ring of L = 402 sites with antiperiodic boundary conditions, which realises the c = 1 Dirac fermion. Its global vacuum reproduces the ordinary result. The antipodal image was implemented by analogy with the scalar's crosscap structure (field and momentum images of opposite sign): a fermion at x is paired with a creation operator at the antipode, through a shift by half the ring combined with a staggered sign. The operator was required to be a Hermitian involution that commutes with the vacuum correlations, so that the resulting Gaussian state is legitimate.

**Result.** The construction gives a valid state, and its excess entropy matches the exact magnitude to four digits at every interval tested, but with the **opposite sign**:

| Δφ/π | Lattice ΔS | Dulac–Wei ΔS |
| --- | --- | --- |
| 0.100 | −0.00409 | +0.00409 |
| 0.498 | −0.11423 | +0.11423 |
| 0.900 | −0.62005 | +0.62002 |

The lattice entropy is therefore (1/3) ln\[(2/ε) sin(Δφ/2) cos(Δφ/2)\], not the tan form. Dulac and Wei identify this sin·cos structure as the one produced by an incompatible pairing of crosscap state and twist operator, which they exclude because it violates crossing symmetry on RP². A number-conserving alternative (image without particle–hole pairing, with chirality exchange) was also tried; it fails positivity for larger intervals and does not reproduce either form.

**A structural identity behind the sign.** In the global vacuum, the mutual information between an interval A and its antipodal image Ā is I(A:Ā) = (2/3) ln sec(Δφ/2) for the Dirac fermion, from the standard two-interval formula. Both results are then exact shifts by half of it:

- **Dulac–Wei (path integral):** S = S(A) + ½ I(A:Ā).
- **Lattice pairing construction:** S = S(A) − ½ I(A:Ā) = ½ S(A ∪ Ā). On the lattice this holds to five digits at every interval tested (for example 2.04047 against 2.04047 at 60 sites), so the construction literally folds A onto its image and halves the entropy of the pair.

The ℤ₂ therefore offers two signs for the same folding, as it did throughout the series (even and odd sectors, pin⁺ and pin⁻, the crosscap states C₊ and C₋), and the Euclidean path integral selects the one in which a region becomes more entangled through its own image. The same relation does not describe the four-dimensional scalar: there ΔS exceeds ½ I(A:Ā) by two to four orders of magnitude in every ℓ sector, because the scalar's excess is first order in the image correlator (the contact term of 5.2), while mutual information is second order. The half-mutual-information form is an observed identity for the two-dimensional fermion, not a general law. The open problem is now specific: identify what selects the sign in the Hamiltonian construction. Whether the scalar's negative odd-sector contributions reflect the same sign question is also worth checking with a two-dimensional scalar calibration.

**Toward a scalar calibration: the compact boson (set-up and an obstacle).** The planned check was the compact boson in elliptic dS₂, calibrated against Dulac and Wei at the free-fermion radius. Two findings from the literature and the geometry change that plan:

- **The geometry is tractable.** For n = 2, the replica surface of RP² branched along A is a Klein bottle. Its orientation double cover is the torus branched over A's endpoints and their antipodes, four points on the equator with cross-ratio x = sin²(Δφ/2). The compactification radius R enters only through the crosscap zero modes: momentum alone for C₊, winding alone for C₋, exchanged by T-duality. In the decompactification limit the zero-mode sum grows with R, so the entropy acquires a log R dependence. That is the zero-mode sensitivity seen in the failed harmonic-chain calibration, now with a clear origin.
- **The calibration point is not available.** Two-interval studies (Calabrese, Cardy and Tonni; Coser, Tonni and Calabrese on spin structures) and work on boundary entanglement spectra show that the massless Dirac fermion matches the compact boson at the free-fermion radius only after its spin structures are summed (the ℤ₂-gauged Dirac fermion), not as a single fermion. On a non-orientable surface the same issue arises with pin structures. Dulac and Wei's result therefore cannot be used directly to fix the boson's normalisation.

The boson calculation remains well defined, and its R-dependence follows from the crosscap zero modes. Its absolute sign, which is the question at issue, needs the R-independent conformal factor of the Klein-bottle cover, which must be computed independently rather than borrowed from the fermion.

**Status.** The construction that works for the scalar does not carry over directly to fermions: the natural analogue yields a legitimate state with the right magnitude and the wrong sign. Until the fermionic crosscap is derived from the Euclidean path integral itself, for example from a transfer matrix on the Möbius-band geometry, rather than by analogy, the four-dimensional Dirac calculation cannot be trusted. **The χ₀⁶ prediction of Section 5.3 remains untested.** The scalar results are not affected: there the equal-time correlators follow directly from the image sum of the Green's function, without an analogy step, although the same kind of two-dimensional calibration would strengthen them.

## 6. Next steps

1. **Four dimensions.** Done for the conformally coupled scalar (Section 5): the quadratic suppression persists, and positivity limits the construction to caps below about χ₀ ≈ 0.75. Section 5.1 identifies the mechanism (an area law sourced by the image's δ⟨φ²⟩, κ ≈ 1.047, confirmed across scalar masses). Section 5.2 derives κ = π/3 from the ℓ = 0 sector. The fermion test is blocked (Section 5.4): derive the fermionic crosscap from the Euclidean path integral, calibrate it against the exact two-dimensional result, then test χ₀⁶ for the four-dimensional Dirac fermion; the Maxwell prediction follows after. Parked, 30 Sept 2026: the sign of the excess (which branch of the ℤ₂ folding the path integral selects) is left open, with its set-up in Section 5.4; it does not affect the brane programme of BTICU 1, which depends on mode functions rather than the elliptic state.
2. **The parity grading for fermions.** On RP³ ordinary spinors exist, and the spinor lift of the twist may change the odd-sector weights of Section 2.
3. **The gravitational version.** Dulac and Wei note that the gravitational analogue, contributions of RP^(d+1) geometries to the gravitational no-boundary density matrix, has not been realised. That question belongs to quantum gravity rather than to this series, and is recorded here only as context.

## References

- Calabrese, P. and Cardy, J. (2004). Entanglement entropy and quantum field theory. *J. Stat. Mech.* P06002.
- Dulac, R. and Wei, Z. (2026). No boundary density matrix in elliptic de Sitter dS/ℤ₂. *JHEP* 05, 022. arXiv:2512.00704.
- Gibbons, G. W. and Hawking, S. W. (1977). Cosmological event horizons, thermodynamics, and particle creation. *Phys. Rev. D* 15, 2738.
- Ivo, V., Li, Y.-Z. and Maldacena, J. (2025). The no boundary density matrix. *JHEP* 02, 124. arXiv:2409.14218.
- Maldacena, J. and Pimentel, G. L. (2013). Entanglement entropy in de Sitter space. *JHEP* 02, 038. arXiv:1210.7244.
- Parikh, M. K., Savonije, I. and Verlinde, E. (2003). Elliptic de Sitter space: dS/ℤ₂. *Phys. Rev. D* 67, 064005.
- Wei, Z. and Yoneta, Y. (2024). Crosscap quenches and entanglement evolution. arXiv:2412.18610.
- Broadbent, G. P. (2026). BTICU 2 — The Elliptic State (working document).
