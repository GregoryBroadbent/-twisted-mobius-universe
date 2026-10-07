# BTICU 4 — The Twist on a Curved Bulk

Gregory P. Broadbent · Sep 30, 2026 · working draft

## Abstract

BTICU 1 found that on a healthy inflating brane in a flat five-dimensional bulk, the twist phase & = πΔ appears only as & = 0 (the massless mode) or as complex & (a Kaluza–Klein continuum beginning at m² = 9H²/4), and that every route to real & ≠ 0 carries a ghost. Here we ask whether bulk curvature changes this. For an anti-de Sitter bulk the brane spectrum is unchanged in structure: a massless mode, an empty gap, and a continuum from 9H²/4, reproducing known results. For a de Sitter bulk, the Schrödinger potential becomes a Pöschl–Teller well, and a healthy massive mode appears in the gap with 2H² < m² < 9H²/4, carrying & between π and 3π/2 and approaching the partially massless point & = π as ℓH grows. Applying the junction conditions of BTICU 1, this mode exists only when the brane has negative tension. Using the established junction structure of the brane-bending mode, its contribution to the exchange between brane sources is proportional to the brane's extrinsic curvature and changes sign with the tension; on the negative-tension branch it has the wrong sign, a scalar ghost. The pattern of BTICU 1 therefore extends to curved bulks: real, nonzero & on an inflating brane is always accompanied by a ghost. The radion step uses a published form of the junction condition rather than an independent derivation for a de Sitter bulk, and is flagged as such.

## 1. Introduction

BTICU 1 placed a de Sitter brane in a flat five-dimensional bulk with a ℤ₂ fold, the geometry of the DGP model, and found that the twist phase & = πΔ has a geometric meaning there: the phase a mode's bulk profile acquires between a point and its antipode. A healthy brane admits & only at 0 or off the unit circle. Real values 0 < & < 3π/2 appeared only with a wrong-sign brane kinetic term or on the self-accelerating branch, in both cases together with a ghost.

Two reasons motivate repeating the analysis with a curved bulk. The first is generality: a flat bulk is one choice among three, and a result that depends on it would be fragile. The second is internal consistency. The earlier research notes switched from the flat bulk of UV Paper 2 to an anti-de Sitter bulk in UV70–UV75 without resolving the conflict, as recorded in the correction ledger. Treating flat, anti-de Sitter and de Sitter bulks together settles what, if anything, depends on the choice.

We work with free bulk fields (a massless scalar, and transverse-traceless graviton modes, which obey the same radial equation), a ℤ₂ fold at the brane, and no brane kinetic term. Spectra are computed numerically and checked against exact limits. Results that reproduce published work are identified as such.

## 2. Brane spectra in a warped bulk

Each bulk is foliated by de Sitter slices,

ds² = dr² + a(r)² ds²(dS₄, unit),

with the brane at r = r\_b and Hubble rate H = 1/a(r\_b). The three warp factors are

| Bulk | a(r) | Brane Hubble rate |
| --- | --- | --- |
| Flat | r | H = 1/r\_b |
| AdS₅ (radius ℓ) | ℓ sinh(r/ℓ) | ℓH = 1/sinh(r\_b/ℓ) |
| dS₅ (radius ℓ) | ℓ sin(r/ℓ) | ℓH = 1/sin(r\_b/ℓ) ≥ 1 |

A massless bulk field separates as φ = f(r)·χ(x), with χ a brane field of mass m (in units of H). In the conformal coordinate w = ∫dr/a and with f = a^(−3/2)ψ, the radial equation becomes a Schrödinger problem,

−ψ″ + V(w)ψ = (m²/H²)ψ,  V = (a^(3/2))″ / a^(3/2),

with the ℤ₂ fold imposing the Neumann condition f′ = 0 at the brane, that is ψ′ = (3/2)(a′/a)ψ in w. The potentials are

| Bulk | V(w) |
| --- | --- |
| Flat | 9/4 |
| AdS₅ | 9/4 + 15/(4 sinh²u), u = −w > 0 |
| dS₅ | 9/4 − 15/(4 cosh²w) |

Two features are common to all three. The massless mode f = constant (ψ = a^(3/2)) solves the equation and the brane condition exactly, and is normalisable on the side of the brane containing the slicing's horizon. And V tends to 9/4 away from the brane, so the continuum always begins at m² = 9H²/4, the threshold at which & leaves the unit circle. What can differ between bulks is the gap 0 < m² < 9H²/4: flat and AdS₅ potentials lie at or above 9/4, while the dS₅ potential dips below it.

Spectra were computed by a finite-element discretisation with the Neumann condition built in and a distant Dirichlet wall to discretise the continuum. The discretised continuum therefore appears just above 9/4 (about 2.26–2.28) rather than at it.

## 3. AdS₅ bulk

Keeping the side of the brane that contains the horizon (the Randall–Sundrum-type choice), the AdS₅ potential lies everywhere above 9/4, so no state other than the massless mode can lie below the continuum.

| ℓH | Lowest eigenvalues m²/H² |
| --- | --- |
| 0.3 | 0.000, 2.278, 2.363 |
| 1 | 0.000, 2.262, 2.299 |
| 10 | 0.000, 2.264, 2.307 |

The spectrum is a massless mode, an empty gap, and the continuum. For very small ℓH the potential is steep near the brane and a finer grid is needed; at ℓH = 0.1 the uniform grid used here gives a spurious small negative lowest eigenvalue.

**This reproduces published results.** Garriga and Sasaki found this structure for a de Sitter brane in AdS₅, and a rigorous treatment of the Klein–Gordon equation near a de Sitter brane in an anti-de Sitter bulk shows that the only point spectrum is the constant massless mode, with the continuum above m = 3H/2. In the language of this series: an AdS₅ bulk behaves exactly like the flat bulk of BTICU 1. The real arc of & stays empty, and the switch to AdS₅ in the earlier notes changes nothing here.

## 4. dS₅ bulk: the gap mode

In the conformal coordinate w = ln tan(r/2ℓ), the dS₅ warp factor is a = ℓ/cosh w, and the potential V = 9/4 − 15/(4 cosh²w) is a Pöschl–Teller well. Without a brane, this well has exactly two bound states, at m² = 0 and m² = 2H²; the second is the partially massless point & = π. The brane at w\_b cuts the well, and ℓH = cosh(w\_b). For each ℓH > 1 there are therefore two brane positions, w\_b < 0 (the brane before the equator of the dS₅ slicing, r\_b < πℓ/2) and w\_b > 0 (beyond it). The region kept is w < w\_b.

**Brane before the equator (w\_b ≤ 0).** At w\_b = −2, −1 and 0 the spectrum is a massless mode, an empty gap and the continuum, as in flat and AdS₅ bulks. This agrees with the published spectrum for a de Sitter brane in a bulk with positive cosmological constant: a normalisable zero mode separated by a gap from a continuum.

**Brane beyond the equator (w\_b > 0).** The kept region now contains the bottom of the well, and a second bound state appears below the continuum:

| w\_b | ℓH | m²/H² | & = πΔ |
| --- | --- | --- | --- |
| 1.0 | 1.543 | 2.238 | 1.39π |
| 1.5 | 2.352 | 2.169 | 1.22π |
| 2.0 | 3.762 | 2.104 | 1.12π |
| 3.0 | 10.07 | 2.036 | 1.04π |
| 4.0 | 27.31 | 2.013 | 1.01π |
| 6.0 | 201.7 | 2.002 | 1.002π |

Three properties hold throughout:

- **The mode is normalisable and has positive norm,** since there is no brane kinetic term to contribute a negative weight.
- **Its mass lies above 2H².** For the graviton this satisfies Higuchi's bound, so its helicity-0 component is not a ghost. In the language of this series, & lies between π and 3π/2.
- **As ℓH grows, the mass falls towards the partially massless value m² = 2H²,** matching the second bound state of the full Pöschl–Teller well, which the kept region increasingly contains.

On its own, the spectrum would mean a de Sitter bulk lets a healthy massive graviton carry the twist phase onto the brane, the first such case in the series. Section 5 shows why it does not.

The dependence of m² on ℓH was obtained numerically; a closed form, which should follow from the hypergeometric solutions of the Pöschl–Teller equation with a Robin condition, has not been derived.

## 5. The tension and the radion

**The gap mode requires negative tension.** BTICU 1 derived, from the Israel junction condition with the sign convention checked on a static dust shell, that a ℤ₂-symmetric brane bounding the kept region r < r\_b has tension of the same sign as its extrinsic curvature K = a′/a. With the dS₅ warp factor,

K = cot(r\_b/ℓ)/ℓ,

which is positive for r\_b < πℓ/2 and negative for r\_b > πℓ/2. The gap mode of Section 4 exists only for w\_b > 0, that is r\_b > πℓ/2. **It lives exclusively on negative-tension branes.** The positive-tension branch, the one studied in the published dS₅ analysis, has no gap mode.

**The tensor sector is healthy.** The massless graviton's four-dimensional Planck mass is proportional to ∫a² dr over the kept bulk, which is positive, and the gap mode satisfies Higuchi's bound. Any ghost must therefore lie in the scalar sector, the brane-bending mode or radion.

**The scalar sector.** In the junction analysis of Garriga and Tanaka for a flat brane, generalised to de Sitter branes as in Garriga and Sasaki, the brane-bending mode ζ obeys

(□ + 4H²)ζ = (κ²/6)T,

sourced by brane matter with a sign independent of the tension, and enters the brane metric through a term proportional to Kζ g\_μν, together with derivative terms that drop out against a conserved source. The scalar part of the exchange between two brane sources is therefore proportional to

K · T (□ + 4H²)⁻¹ T.

On a positive-tension brane (K > 0) this term carries the attractive sign; it is the piece that converts the five-dimensional tensor structure into that of four-dimensional gravity. On the gap-mode branch K < 0 and the term reverses: the scalar exchange is repulsive, the signature of a field with a wrong-sign kinetic term, a ghost of Brans–Dicke type.

**Agreement with the literature.** Multi-brane studies find that radions associated with negative-tension branes have wrong-sign kinetic terms. In the two-brane de Sitter configuration reviewed by Koyama, bringing the branes close raises the massive spin-2 mode above 2H², removing its ghost, but the radion becomes a ghost instead; stabilising the radion with a bulk scalar makes that scalar a ghost. The single negative-tension brane in a dS₅ bulk follows the same pattern.

**What is and is not derived here.** The negative tension of the gap-mode branch, the positivity of the tensor sector and the Higuchi-safety of the gap mode are derived in this paper. The proportionality of the bending contribution to K is taken from the published junction structure; it has not been rederived independently for a dS₅ bulk. A complete scalar-sector junction calculation in this background would make the conclusion independent of that step.

## 6. Conclusions and open problems

| Bulk and brane | Spectrum below the continuum | Real & ≠ 0 on the brane? | Ghost |
| --- | --- | --- | --- |
| Flat, normal branch (BTICU 1) | massless mode only | no | none |
| Flat, wrong-sign brane term (BTICU 1) | massless mode plus a gap mode | yes | massless mode |
| Flat, self-accelerating branch (BTICU 1) | one light spin-2 mode | yes | helicity-0 or radion |
| AdS₅ | massless mode only | no | none |
| dS₅, positive tension | massless mode only | no | none |
| dS₅, negative tension | massless mode plus a gap mode | yes | radion (Section 5) |

The statement of BTICU 1 extends to curved bulks: **on every inflating brane examined, a healthy theory carries the twist phase only as & = 0 or off the unit circle; every configuration that puts a mode on the real arc 0 < & < 3π/2 also carries a ghost.** The de Sitter bulk comes closest, with a massive graviton that satisfies Higuchi's bound, but it requires negative tension and pays for it in the scalar sector. The switch to an anti-de Sitter bulk in the earlier notes is immaterial for this question.

**Open problems**

- **The full scalar-sector junction calculation** in a dS₅ bulk, to remove the reliance on the published form of the bending term.
- **A closed form for the gap-mode mass** as a function of ℓH, from the Pöschl–Teller solutions with the brane's Robin condition.
- **A brane kinetic term in a curved bulk,** combining Section 4 with the induced-gravity analysis of BTICU 1.
- **The heavy continuum,** which carries the complex twist phase in every case, and its correlation functions.

## References

- Charmousis, C., Gregory, R., Kaloper, N. and Padilla, A. (2006). DGP specteroscopy. *JHEP* 10, 066. arXiv:hep-th/0604086.
- Deser, S. and Waldron, A. (2001). Partial masslessness of higher spins in (A)dS. *Nucl. Phys. B* 607, 577.
- Garriga, J. and Sasaki, M. (2000). Brane-world creation and black holes. *Phys. Rev. D* 62, 043523.
- Garriga, J. and Tanaka, T. (2000). Gravity in the brane world. *Phys. Rev. Lett.* 84, 2778.
- Higuchi, A. (1987). Forbidden mass range for spin-2 field theory in de Sitter spacetime. *Nucl. Phys. B* 282, 397.
- Koyama, K. (2007). Ghosts in the self-accelerating universe. *Class. Quantum Grav.* 24, R231. arXiv:0709.2399.
- Graviton localization and Newton law for a dS₄ brane in 5D bulk. arXiv:hep-th/0205009.
- On the Klein–Gordon equation near a De Sitter brane in an Anti-de Sitter bulk. arXiv:1402.1071.
- Brane-world multigravity (review). arXiv:hep-ph/0112159.
- Broadbent, G. P. (2026). BTICU 1 — The Twist on an Inflating Brane (working document).
- Broadbent, G. P. (2026). BTICU0 — Correction Ledger (working document).

Three entries are cited by title and arXiv number only; their author lists should be confirmed before circulation.
