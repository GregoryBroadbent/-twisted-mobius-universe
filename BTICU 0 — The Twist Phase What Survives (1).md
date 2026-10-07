# BTICU 0 — The Twist Phase: What Survives

Gregory P. Broadbent · Sep 30, 2026

> **Forward note (30 Sept 2026).** BTICU 2 tested the results of this paper against three consistent quantum constructions of elliptic de Sitter space (Sanchez–Whiting; Parikh–Savonije–Verlinde; Aguirre–Gratton). In every construction that gives observers a genuine quantum field, the image term G(−Z) is absent from their correlations. The image-sum results below (the twist phase & as a relation between a correlation and its image, the cos²(&/2) : sin²(&/2) partition, the antipodal commutator, the heavy-field dominance and the folded non-Gaussianity bound) are therefore properties of the naive kernel. They survive only as correlations of a classical, commuting field. The mathematics of Sections 3–5 is unchanged; its physical reading is superseded by BTICU 2. The geometric phase of BTICU 1 is unaffected. Two further corrections from Neiman (2014): in dS₄ the antipodal map is of CT type, not CPT as stated by Parikh, Savonije and Verlinde and repeated in Section 8 here; and because the Levi-Civita tensor is odd under it, elliptic de Sitter space supports only parity-conserving theories. The Standard Model violates parity, so a literal antipodal identification of our spacetime would require additional structure to be compatible with known particle physics.

## Abstract

This paper opens the BTICU series (Bounce, Twist, Inflate, Cohere) and replaces an earlier research programme whose central numerical claims have been falsified or found to be unsupported. Those corrections are recorded in a separate ledger and summarised here. What survives is a small set of derived results about a single operation: the antipodal ℤ₂ identification of de Sitter space, applied to a bilocal kernel K. Writing the identified kernel as K± = G(Z) ± G(−Z), we show that the image term is related to the direct term by a phase & = πΔ, where Δ is the field's scaling dimension, fixed by its mass and by the number of expanding spatial dimensions. On superhorizon scales this gives an even/odd split of the form cos²(&/2) : sin²(&/2), and an antipodal commutator between causally disconnected points of exactly sin(&)·G(Z). For heavy fields & becomes complex, and the image term exceeds the direct term by roughly e^(πμ)/2. Applied to inflation, the two-point effect is an unobservable rescaling, while the three-point function yields a folded-shape signal that current data bound only weakly, but that excludes an identification extending into the infinite past. We identify the S¹/ℤ₂ orbifold of five-dimensional brane-world models as the established physics in which the same even/odd mechanism already decides what appears in four dimensions, and propose it as the series' next step. No numerical constant is fitted anywhere in what follows.

## 1. Introduction

### 1.1 An entry point: what SNO measured

In 2002 the Sudbury Neutrino Observatory, 1,000 tonnes of heavy water about two kilometres underground in the Creighton Mine near Sudbury, Ontario, measured the flux of ⁸B neutrinos from the Sun in three ways at once:

- **Charged current** (ν\_e + d → p + p + e⁻), sensitive to electron neutrinos only: 1.76 ± 0.05 (stat.) ± 0.09 (syst.) × 10⁶ cm⁻² s⁻¹.
- **Elastic scattering** on electrons, sensitive to all flavours but weighted towards electron neutrinos: 2.39 × 10⁶ cm⁻² s⁻¹.
- **Neutral current** (ν + d → p + n + ν), sensitive to all active flavours equally: 5.09 (+0.44 −0.43 stat., +0.46 −0.43 syst.) × 10⁶ cm⁻² s⁻¹.

The neutral-current flux, which counts every active neutrino regardless of flavour, agreed with solar-model predictions. The charged-current flux, which counts only electron neutrinos, was about a third of it. The difference, a non-electron component of 3.41 × 10⁶ cm⁻² s⁻¹, stood 5.3 standard deviations above zero. The Sun makes only electron neutrinos, so roughly two-thirds had changed flavour on the way, while the total was conserved.

The accepted explanation is neutrino mixing, enhanced by the Sun's matter density (the Large Mixing Angle solution). The one-third fraction at these energies is set by the measured mixing angle and the solar density profile. It is not a fixed or topological ratio, and nothing in this series is offered as an alternative account of it.

We begin with SNO for two reasons. It is the clearest measured example of the structure this series studies: a whole that is conserved while its distribution among sectors changes. And it is a model of method. The experiment was designed so that one reaction read the whole and another read the part, and the answer did not depend on assuming either one. The relationship between SNO and what follows is one of structure and method only; the phase & introduced below is a different phenomenon. (This replaces an earlier entry point, a reading of the Super-Kamiokande solar neutrino image as a separation of flavours, which was incorrect: its colours encode intensity, and its halo is angular resolution.)

### 1.2 Inheritance

The work collected under the IR, UV, K and MU series ("Framework C") proposed that the gauge structure SU(2)₂₀ × SU(3)₂₂, a coherence partition of 42/58, and a bilocal kernel K together accounted for most of observed physics without free parameters. On re-examination, that claim does not hold. All earlier material is therefore reclassified as research notes, and the BTICU series begins from what can be derived and checked.

The principal corrections, detailed in the accompanying ledger (BTICU0 — Correction Ledger), are these:

- **The number 42 is not a central charge.** It is the sum of the levels, 20 + 22. The central charge of SU(2)₂₀ × SU(3)₂₂ is c = 2.727 + 7.04 ≈ 9.77, and cannot exceed 11 for this group.
- **The fine-structure relation α = (47/550)² is excluded.** It misses the measured value by 0.07%, several million times the measurement uncertainty, and the choice of levels it was used to select matches α at the rate expected by chance.
- **The predicted QED coherence suppression is excluded.** A 16% reduction in g−2 and a −173 MHz Lamb shift are ruled out by existing measurements by factors of 10⁵ to 10⁹.
- **The levels do not set cosmic scales.** A pre-registered test found no feature distinguishing (20, 22) from its neighbours, and no natural exponent reproducing the cosmological hierarchy.
- **The remaining numerical "predictions" were inputs.** The lepton masses, axion relic abundance, spectral index and baryon asymmetry reported in the notes were measured values entered as inputs or fitted at the final step.
- **The 42/58 partition has no derivation.** Neither the gauge structure nor the Möbius topology produces it (Section 4).

The K-kernel itself was built independently of these choices, and its own papers record its gaps candidly. Its construction stands, and it is the object this paper studies.

The series name describes a sequence rather than a result. **Bounce** refers to whatever preceded inflation and set its initial conditions, and is treated here only as an open question. **Twist** is the ℤ₂ identification studied below. **Inflate** is the de Sitter phase in which the twist acts. **Cohere** asks which correlations the twist preserves, cancels or rotates. Only Twist and Cohere are developed in this paper.

## 2. Elliptic de Sitter space and the kernel K±

De Sitter space of dimension d + 1 is the hyperboloid X·X = 1/H² in flat (d + 2)-dimensional Minkowski space. For two points X and Y, the invariant Z = H² X·Y fixes their separation: Z > 1 is timelike, Z = 1 lightlike, and Z < 1 spacelike. In the flat slicing used for inflation, pairs with Z < −1 are those that can never come into causal contact.

The antipodal map X → −X sends Z to −Z. Identifying each point with its antipode gives elliptic de Sitter space, dS/ℤ₂ (Schrödinger's proposal, developed for quantum fields by Sanchez and Whiting and by Parikh, Savonije and Verlinde). In the flat slicing the map acts as η → −η at fixed comoving position, carrying the expanding patch onto the contracting one. Antipodal points always lie beyond each other's horizons.

A field on dS/ℤ₂ is either even or odd under the identification. For a two-point function G(Z), the identified kernels are

K±(Z) = G(Z) ± G(−Z).

We take G to be the Bunch–Davies function for a scalar of mass m,

G(Z) = \[Γ(Δ₊)Γ(Δ₋) / 16π²\] · ₂F₁(Δ₊, Δ₋; 2; (1 + Z)/2),  with Δ± = d/2 ± √(d²/4 − m²/H²),

written here for d = 3. The K papers build their kernel from de Sitter Green's functions of this type, so K± is the kernel restricted to the identified space. The quantity of interest throughout is the image term G(−Z) and its relation to G(Z).

## 3. The twist phase & = πΔ

At large separation the Bunch–Davies function is dominated by its slower-falling term, G(Z) ∝ |Z|^(−Δ), with Δ ≡ Δ₋. For Z → −∞ the argument of the hypergeometric function is real and negative, and G(Z) is real. The image term G(−Z) is evaluated at −Z → +∞, on the branch cut of ₂F₁ (the timelike region), where the prescription Z → Z ± iε gives

G(−Z ± iε) / G(Z) → e^(±iπΔ).

The image term is therefore the direct term rotated by the phase

**& = πΔ**,

which depends only on the field's mass and the dimension. Its real part, the symmetrised (Hadamard) image, gives Re G(−Z)/G(Z) → cos(&). We confirmed this against the exact hypergeometric function to ten significant figures for m²/H² from 0.03 to 2 at Z = −10⁶.

The imaginary part obeys a stronger relation. For points in the inflationary patch, the image contribution to the commutator \[φ(X), φ(Y)\] vanishes for Z > −1, and for Z < −1 equals

Im G(−Z) = sin(&) · G(Z)

at every separation, not only asymptotically. We found agreement to numerical precision for m²/H² from −0.05 to 1 and separations from Z = −0.5 to −10⁴. The identification therefore makes a field fail to commute between pairs of points that can never be in causal contact, with strength sin(&).

Two limits check the result. A massless field has Δ = 0, so & = 0 and K₊ = 2G, reproducing the factor of 2 in ⟨φ²⟩ found by Sanchez and Whiting. A conformally coupled field has Δ = 1, so & = π and K₊ = 0: the even sector cancels entirely.

**Dimension dependence.** In d spatial dimensions, Δ(d − Δ) = m²/H², so & carries the dimension explicitly. For the conformally coupled field, Δ = (d − 1)/2 and & = π(d − 1)/2:

| Spatial dimensions d | Spacetime | Conformal & | e^(i&) |
| --- | --- | --- | --- |
| 2 | dS₃ | π/2 | i |
| 3 | dS₄ | π | −1 |
| 4 | dS₅ | 3π/2 | −i |

In our universe the conformal field sits at the half-turn. The heavy-field threshold, m = (d/2)H, and the scale-invariant spectrum, k^(−d), are fixed by the same number. A related dimension dependence enters for fermions. The spatial slices of dS₄/ℤ₂ are RP³, which admit ordinary spinors, while those of dS₅/ℤ₂ are RP⁴, which admit only pin⁺ structures. This affects whether the lift of the identification to spinors can carry & = ±π/2, a question left open here.

## 4. The partition form

On superhorizon scales, Section 3 gives

K₊ = (1 + cos &)·G = 2cos²(&/2)·G,  K₋ = (1 − cos &)·G = 2sin²(&/2)·G.

The ℤ₂ identification therefore always partitions a field's long-range correlation into even and odd parts in the proportion

**cos²(&/2) : sin²(&/2).**

The form is universal; the proportion is not. It is set field by field through the mass:

| Field | m²/H² | & | Even : odd |
| --- | --- | --- | --- |
| Massless | 0 | 0 | 100 : 0 |
| Curvature perturbation | ≈ −0.05 | ≈ −0.055 | 99.92 : 0.08 |
| — | 5/4 | π/2 | 50 : 50 |
| Conformally coupled | 2 | π | 0 : 100 |

For the curvature perturbation we use Δ = (n\_s − 1)/2 ≈ −0.0175, the value implied by the measured tilt.

A second, independent count gives the same message. Comparing the modes of the twisted spatial slice RP³ with those of its double cover S³, even and odd modes tend to equal numbers as the cutoff rises: mode counting gives 50 : 50.

No universal ratio, and in particular no 42 : 58, follows from the twist. A 42 : 58 split occurs only for a field with m² ≈ 1.35 H², a choice that would make the mass, not the topology, responsible for the number. This closes the question left open by the earlier programme: the Möbius structure fixes the shape of the partition, and each field's physics fixes its value.

## 5. Heavy fields: leaving the circle

Above m = (d/2)H the scaling dimension becomes complex, Δ± = 3/2 ± iμ with μ = √(m²/H² − 9/4), and & = πΔ is no longer a real angle. The two relations of Section 3 continue analytically, and we verified both numerically for m²/H² = 3, 4, 6 and 10 at separations |Z| = 50 to 5 × 10⁴:

- **Commutator.** The image contribution equals −cosh(πμ)·G(Z) exactly, the continuation of sin(&).
- **Correlation.** The symmetrised image is the quadrature partner of G(Z), the same oscillation in log|Z| shifted by a quarter cycle, scaled by sinh(πμ). The combined envelope is constant to five significant figures.

In terms of the phase, e^(i&) leaves the unit circle and acquires a real factor e^(±πμ). The image term then dominates the direct term by approximately e^(πμ)/2:

| m²/H² | μ | Image / direct |
| --- | --- | --- |
| 3 | 0.87 | 7.6 |
| 4 | 1.32 | 32 |
| 6 | 1.94 | 219 |
| 10 | 2.78 | 3,142 |

The reason is physical. In ordinary de Sitter space, the correlation of a heavy field across a large spacelike separation is suppressed by a Boltzmann-like factor of order e^(−πμ). The antipodal image connects the same two points through a timelike separation, where no such suppression applies. In the elliptic kernel, a heavy field's long-range correlation therefore runs almost entirely through the antipode.

This gives the twist its sharpest potential signature. Heavy fields present during inflation leave oscillatory "cosmological collider" signals in squeezed bispectra, normally suppressed by e^(−πμ). If the identification held during inflation, that suppression would be lifted. The same result also sharpens the consistency problem of Section 8: a commutator of size cosh(πμ)·G between causally disconnected points is large, not a small correction.

## 6. Observables and bounds

**Two-point function: a null result.** For the curvature perturbation, cos(&) = 0.9985, so K₊ ≈ 2G and K₋ ≈ 1.5 × 10⁻³ G. Both are scale-independent rescalings, absorbed into the measured amplitude A\_s. Tensor modes are massless and rescale identically, leaving the tensor-to-scalar ratio unchanged. Because G(−Z) depends only on the invariant Z, the sky remains statistically isotropic. The identification produces no even/odd multipole asymmetry at the two-point level, and cannot account for the low-ℓ parity anomaly in the CMB.

**Three-point function: a folded signal.** In the flat slicing the antipodal map sends each mode function to its complex conjugate, so the image term mixes positive- and negative-frequency modes. In the in-in bispectrum this produces poles in k₁ + k₂ − k₃, and the effect appears in folded triangles, k₁ + k₂ ≈ k₃, as it does for excited initial states. We computed it for all three leading cubic terms of the slow-roll action (ζζ′², ζ(∂ζ)² and ζ′∂ζ∂χ), with an initial time η₀ at which the identification begins. The code reproduces Maldacena's Bunch–Davies shape to machine precision across configurations, and the squeezed limit gives (5/12)(2ε) as the consistency relation requires.

Since K₊ is not itself the two-point function of a quantum state (Section 8), we used the least-excited de Sitter-invariant state with the same superhorizon amplitude, a Bogoliubov coefficient |β| = sinh(ln 2/2) = 0.354. This stand-in captures the frequency mixing but not the antipodal commutator of Section 3, so the numbers below are indicative. With it:

- The peak folded amplitude grows linearly, f\_NL ≈ 0.44 ε · k|η₀|. A single vertex alone grows quadratically; the three vertices partly cancel.
- Projected onto Planck's orthogonal template over three decades in k, f\_ortho ≈ −ε(45 + 14ΔN), where ΔN = ln(k\_min|η₀|) counts the e-folds of identification before the largest CMB scales exited. At ε ≤ 0.0023 this is below 1, against a measured uncertainty of 24. The orthogonal constraint gives no bound.
- An idealised matched filter at the same noise level gives signal-to-noise of about 0.3, 0.9 and 2.6 at ΔN ≈ 4.6, 6.9 and 9.2 (ε = 0.0023), growing as roughly e^(ΔN/2). This implies an optimistic 2σ bound of ΔN ≲ 9 at ε = 0.0023, loosening to about 15 at ε = 10⁻⁴.

CMB transfer functions smear sharp folded features, so the true bound is weaker than this. Two conclusions are robust. An identification extending into the infinite past is excluded, since the signal diverges without an initial time. A finite identification is only weakly constrained by current data.

## 7. The S¹/ℤ₂ orbifold

The mechanism studied here, a ℤ₂ identification that sorts fields into even and odd sectors, is already part of established physics in a different setting. In the Randall–Sundrum and Hořava–Witten constructions, a fifth dimension is a circle folded by a ℤ₂, written S¹/ℤ₂, with branes at its two fixed points. A bulk field is either even or odd under the fold:

- **Even fields** have zero modes, which appear as light particles on the brane, that is, in our four dimensions.
- **Odd fields** vanish at the fixed points and have no zero mode, so they are absent at low energy.

This is the same even/odd sorting as K±, and here its consequence is the standard, testable question of which fields become visible in four dimensions. The orbifold also avoids the difficulty that complicates elliptic de Sitter space: its ℤ₂ acts on a spatial dimension and preserves the time orientation, so no antiunitary construction is required.

There is a second reason to look here. Four-dimensional de Sitter space is itself defined inside five-dimensional flat space, and the antipodal map X → −X is a flip of all five embedding coordinates. The K papers also construct their kernel, K₅, on a five-dimensional de Sitter bulk and project it to four dimensions, using Israel junction conditions and a DGP-type brane. The orbifold is therefore a natural home for the kernel, not an addition to it.

The concrete problem for BTICU 1 is to construct K₅ on S¹/ℤ₂, apply the even/odd decomposition, and determine which of its modes survive on the brane, with what masses and couplings. Unlike the elliptic case, the answer can be compared directly with the extensive existing constraints on brane-world models.

## 8. Programme and open problems

**The state problem.** K₊ as written is not the two-point function of a quantum state in the inflationary patch: it fails the Hermiticity condition W(y, x) = W(x, y)\*. The reason is that the antipodal map reverses time orientation, and in quantum theory time reversal must act antiunitarily. A consistent construction must build CPT into the identification from the start, as Parikh, Savonije and Verlinde do by restricting each observer to a single causal patch. Every result in Section 6 depends on how this is resolved; those in Sections 3 to 5, which concern the kernel as a function, do not.

**Open questions, in order of priority:**

1. Construct the CPT-consistent state on dS/ℤ₂ and recompute the bispectrum with it, including the antipodal commutator.
2. Carry the folded signal through CMB transfer functions, and into large-scale-structure bispectra, to obtain a real bound on ΔN.
3. Determine whether heavy-field collider signals lose their Boltzmann suppression in the consistent state, and compare with existing searches.
4. Settle the fermionic phase: whether the spinor lift of the identification on RP³ carries & = ±π/2.
5. Construct K₅ on S¹/ℤ₂ and identify its brane-localised modes (BTICU 1).
6. Identify what could supply the initial time η₀. This is the "Bounce" of the series, for which compact or string-gas pre-inflationary phases are candidates.

**Method.** Each BTICU result follows the procedure used in the correction ledger:

- State the claim and trace every input.
- Fix the prediction before comparing with data.
- Test against neighbouring alternatives chosen in advance.
- Report how often chance would match as well, and record null results as findings.

## References

- Allen, B. (1985). Vacuum states in de Sitter space. *Phys. Rev. D* 32, 3136.
- Arkani-Hamed, N. and Maldacena, J. (2015). Cosmological collider physics. arXiv:1503.08043.
- Brandenberger, R. and Vafa, C. (1989). Superstrings in the early universe. *Nucl. Phys. B* 316, 391.
- Higuchi, A. (1987). Forbidden mass range for spin-2 field theory in de Sitter spacetime. *Nucl. Phys. B* 282, 397.
- Holman, R. and Tolley, A. J. (2008). Enhanced non-Gaussianity from excited initial states. *JCAP* 05, 001.
- Hořava, P. and Witten, E. (1996). Heterotic and type I string dynamics from eleven dimensions. *Nucl. Phys. B* 460, 506.
- Maldacena, J. (2003). Non-Gaussian features of primordial fluctuations in single field inflationary models. *JHEP* 05, 013.
- Mottola, E. (1985). Particle creation in de Sitter space. *Phys. Rev. D* 31, 754.
- Parikh, M. K., Savonije, I. and Verlinde, E. (2003). Elliptic de Sitter space: dS/ℤ₂. *Phys. Rev. D* 67, 064005.
- Planck Collaboration (2020). Planck 2018 results. IX. Constraints on primordial non-Gaussianity. *Astron. Astrophys.* 641, A9.
- Randall, L. and Sundrum, R. (1999). A large mass hierarchy from a small extra dimension. *Phys. Rev. Lett.* 83, 3370.
- Sanchez, N. and Whiting, B. F. (1987). Quantum field theory and the antipodal identification of de Sitter space. *Nucl. Phys. B* 283, 605.
- Broadbent, G. P. (2026). BTICU0 — Correction Ledger (working document).
- SNO Collaboration (Ahmad, Q. R. et al.) (2002). Direct evidence for neutrino flavor transformation from neutral-current interactions in the Sudbury Neutrino Observatory. *Phys. Rev. Lett.* 89, 011301. arXiv:nucl-ex/0204008.
