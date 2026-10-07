# BTICU 2 — The Elliptic State

Gregory P. Broadbent · Sep 30, 2026 · working draft

## Status and purpose

This is the opening of BTICU 2, written before its main calculation. BTICU 0 derived the twist phase & = πΔ, the partition form cos²(&/2) : sin²(&/2), an antipodal commutator sin(&)·G(Z) between causally disconnected points, and, for heavy fields, an image term exceeding the direct term by roughly e^(πμ)/2. BTICU 1 showed that on a healthy inflating brane the twist reaches four dimensions only through heavy Kaluza–Klein modes. Both papers flagged the same unresolved issue: the identified kernel K₊ = G(Z) + G(−Z) is not the two-point function of a quantum state.

The planned physics of BTICU 2, heavy-particle production during inflation with applications to leptogenesis and dark matter, depends on which of those results survive in a consistent state. This paper therefore resolves the state problem first, using three established constructions in turn, with the possible outcomes and their consequences stated before any calculation (Section 2).

## 1. The state problem

A quantum state assigns every pair of points a Wightman function W(X, Y) = ⟨φ(X)φ(Y)⟩, which must satisfy:

- **Hermiticity:** W(Y, X) = W(X, Y)\*.
- **Positivity:** ∫∫ f(X)\* W(X, Y) f(Y) ≥ 0 for every test function f.
- **Microcausality:** the commutator W(X, Y) − W(Y, X) vanishes when X and Y are spacelike separated.

The kernel of BTICU 0, with the image term taken as the analytic continuation of G to −Z, fails Hermiticity. The reason is geometric. In the embedding space, de Sitter time increases along every future-directed timelike curve, and the antipodal map X → −X reverses it: X̄⁰ = −X⁰. The antipodal map is therefore a time reversal, and in quantum theory time reversal must act antiunitarily, through complex conjugation. (In dS₄ the antipodal map is of CT type; see the note in Section 5.) Identifying X with X̄ without that conjugation mixes a correlation with its time-reversed partner incorrectly.

The Bunch–Davies Wightman function has a property that makes this precise. For timelike separations, W(X, Y) = G(Z ∓ iε), with the sign set by the time ordering of X and Y. Since the antipodal map reverses every time ordering,

**W(X̄, Ȳ) = W(Y, X) = W(X, Y)\*,**

which is the statement that the Bunch–Davies state is invariant under the antipodal map, an antiunitary operation of CT type. All results below follow from this identity.

## 2. Outcomes fixed before the calculation

The following outcomes and consequences were stated on 30 September 2026, before any construction was carried out:

| Outcome | What the consistent state does | Consequence for BTICU |
| --- | --- | --- |
| A | Keeps the cos(&) partition, loses the antipodal commutator | The partition survives; the heavy-field enhancement probably does not; BTICU 2 changes direction |
| B | Keeps the commutator in a consistent form | The antipodal connection is physical; heavy-particle production proceeds as planned |
| C | No consistent state exists across the inflationary patch | The twist is confined to single causal diamonds; its inflationary signatures vanish |

Three constructions are to be tested in order: (1) Sanchez–Whiting, building the identified field from the ordinary de Sitter field; (2) Parikh–Savonije–Verlinde, quantising within one observer's causal diamond with CPT built in; (3) Aguirre–Gratton, an identification that begins on a definite null surface. Each result is recorded against this table, whichever outcome it supports.

## 3. Route 1: the Sanchez–Whiting construction

Start from the ordinary field φ on full de Sitter space in the Bunch–Davies state, and define the even and odd fields

φ±(X) = \[φ(X) ± φ(X̄)\] / √2.

These satisfy φ±(X̄) = ±φ±(X) as operator identities, so they are fields on dS/ℤ₂. Because they are built from a legitimate field in a legitimate state, their two-point function is automatically Hermitian and positive. It remains to compute it.

**Two-point function.** Expanding,

⟨φ±(X)φ±(Y)⟩ = ½\[W(X, Y) + W(X̄, Ȳ)\] ± ½\[W(X, Ȳ) + W(X̄, Y)\].

Applying W(Ā, B̄) = W(B, A) = W(A, B)\* from Section 1 to each pair gives W(X̄, Ȳ) = W(X, Y)\* and W(X̄, Y) = W(X, Ȳ)\*. So

**⟨φ±(X)φ±(Y)⟩ = Re G(Z) ± Re G(−Z) = G\_H(Z) ± G\_H(−Z),**

where G\_H is the symmetric (Hadamard) part. This is exactly the real part of K± from BTICU 0. On superhorizon scales it gives (1 ± cos &)·G, so **the partition cos²(&/2) : sin²(&/2) survives in a legitimate state.** For heavy fields, the sinh(πμ) quadrature term of BTICU 0 §5 also survives, since it came from the symmetric part.

**Commutator.** The same identity gives, for the ordinary commutator C(A, B) = W(A, B) − W(B, A),

C(X̄, Ȳ) = −C(X, Y),  C(X̄, Y) = −C(X, Ȳ).

Then

&#91;φ±(X), φ±(Y)\] = ½\[C(X, Y) + C(X̄, Ȳ)\] ± ½\[C(X, Ȳ) + C(X̄, Y)\] = 0

**for every pair of points, including timelike-separated ones.** Both brackets cancel term by term. The antipodal commutator sin(&)·G of BTICU 0, and its heavy-field form −cosh(πμ)·G, are absent; but so is the ordinary causal commutator.

**Interpretation.** A field whose commutator vanishes everywhere has no quantum dynamics: it cannot propagate a signal and has no particle interpretation. The Sanchez–Whiting fields φ± are therefore consistent but classical-statistical. They carry correlations with the elliptic structure, including the full partition, but they are fluctuations, not quanta. The cancellation is forced by geometry: the antipodal map reverses time orientation, so a correlation and its image contribute with opposite commutators. This is the known obstruction that led Parikh, Savonije and Verlinde to an observer-by-observer construction.

## 4. Verdict against the outcomes, and next steps

**Route 1 gives Outcome A, in a stronger form than anticipated.** The partition cos²(&/2) : sin²(&/2), and the heavy-field quadrature correlation, survive in a Hermitian, positive two-point function. The antipodal commutator does not, and neither does any commutator: the identified field is classical-statistical.

| BTICU 0 / BTICU 1 result | Status under Route 1 |
| --- | --- |
| & = πΔ, the twist phase | Survives in the correlations |
| Partition cos²(&/2) : sin²(&/2) | Survives |
| Two-point CMB null result | Unchanged |
| Antipodal commutator sin(&)·G | Absent |
| Heavy-field image dominance (sinh(πμ) term) | Survives as a classical correlation |
| Heavy-field commutator −cosh(πμ)·G | Absent |
| Folded non-Gaussianity bound | Depends on in-in dynamics, which a commuting field lacks; not supported by Route 1 |
| Brane spectrum, Higuchi bound as & ≥ π (BTICU 1) | Unaffected; these concern mode functions, not the state |

**Consequence for the planned physics.** Heavy-particle production is a quantum effect: it needs a field with a nonzero commutator and a particle interpretation. Route 1 cannot supply it. As fixed in advance, BTICU 2 therefore does not proceed to leptogenesis or dark-matter production on the basis of Route 1.

**Next steps.**

1. **Route 2 (Parikh–Savonije–Verlinde).** Implement the identification antiunitarily, through CPT, within a single observer's causal diamond, and determine whether any quantum field on dS/ℤ₂ retains a nonzero commutator together with a nonzero image term. If it does, record it as Outcome B; if the image term vanishes within every diamond, record Outcome C.
2. **Route 3 (Aguirre–Gratton).** Test an identification that begins on a definite null surface, the structure our bound in BTICU 0 already requires.
3. **The classical reading.** Independently of Routes 2 and 3, the Route 1 result is itself a candidate description: elliptic structure as a property of classical, superhorizon fluctuations rather than of quantum fields. Since inflationary perturbations become effectively classical after horizon exit, it is worth asking which observable, if any, distinguishes this reading from standard inflation.

## 5. Route 2: the CPT identification (Parikh–Savonije–Verlinde)

Parikh, Savonije and Verlinde propose that for every event in de Sitter space there is a CPT-conjugate event at its antipode. Operationally, the identification is implemented by the antiunitary operator Θ representing the antipodal map, with Θφ(X)Θ⁻¹ = φ(X̄): the field at the antipode is not an independent degree of freedom, but the image of the field at X under Θ. This builds in the complex conjugation that Section 1 showed is required.

> **Correction (30 Sept 2026): CT, not CPT, and a parity constraint.** Neiman (2014) shows that in de Sitter space of even dimension the antipodal map is of CT type: it exchanges past and future, does not complex-conjugate fields, and reverses orientation, since the Levi-Civita tensor is antipodally odd. In odd dimensions it is CPT. Parikh, Savonije and Verlinde's description of it as CPT in all dimensions is therefore incorrect for dS₄, and this paper's earlier wording followed theirs. The argument of Sections 1–5 relies only on the map being antiunitary, which a CT operation is, so the results stand. A further consequence matters physically: because the Levi-Civita tensor is an odd field on dS₄/ℤ₂, the elliptic space supports only theories that conserve parity. The Standard Model violates parity, so a literal antipodal identification of our spacetime is incompatible with known particle physics unless additional structure restores the symmetry. Neiman also notes that fields on dS₄/ℤ₂ appear quantisable only relative to an observer and their horizons, consistent with Route 2; Hackl and Neiman (Phys. Rev. D 91, 044016, 2015) and Halpern and Neiman (arXiv:1509.05890) develop this and should be read against Routes 2 and 3.

**Consistency.** The Bunch–Davies state is invariant under Θ, which is the identity W(X̄, Ȳ) = W(X, Y)\* of Section 1. The identification therefore imposes no condition the state does not already satisfy, and the Bunch–Davies state is consistent with it.

**What an observer measures.** No observer's causal region contains both a point and its antipode, since antipodal points always lie beyond each other's horizons. The flat inflationary patch has the same property: the antipodal map carries it entirely onto the complementary patch. For X and Y inside such a region, the identification relates operators there only to operators outside it, so the observer's correlations are the ordinary ones:

⟨φ(X)φ(Y)⟩ = W(X, Y),  with no image term,

and the commutator is the ordinary causal one, nonzero inside the light cone and zero outside. Each observer has a genuine quantum field with a particle interpretation.

**Agreement with recent work.** A 2026 study of free quantum fields on elliptic de Sitter space reaches the same structural conclusion from a different direction: the global Hilbert space is one-dimensional, while the Hilbert space associated with each observer is a nontrivial Fock space. Route 1's result, a global field whose commutators all vanish, is what a one-dimensional global Hilbert space permits; Route 2's result, ordinary quantum fields for each observer, is the observer's Fock space.

**What does not survive in any observer's data.** The image term G(−Z), and with it the twist phase & as a relation between correlations, the partition cos²(&/2) : sin²(&/2), the antipodal commutator, and the heavy-field dominance. These were properties of summing over images; in the CPT construction there is no such sum.

**What may survive.** The same study proposes that the Euclidean path integral on elliptic de Sitter space defines a no-boundary density matrix rather than a wavefunction, and computes its entropies. If the elliptic identification has an observable imprint, it would therefore be in the entropy or mixedness of an observer's state, not in correlation functions.

## 6. Verdict after Routes 1 and 2

**Route 2 gives Outcome C for correlations.** In the consistent quantum construction, the twist leaves no imprint on any correlation function an observer can measure, in the inflationary patch or in any causal diamond. Combined with Route 1:

| Result from BTICU 0 / 1 | Route 1 (classical field) | Route 2 (CPT, per observer) |
| --- | --- | --- |
| & = πΔ as an image phase | In correlations only | Absent |
| Partition cos²(&/2) : sin²(&/2) | Present | Absent |
| Antipodal commutator | Absent | Absent |
| Heavy-field image dominance | Classical correlation only | Absent |
| Folded non-Gaussianity bound | Not supported | Moot: no signal to bound |
| Brane spectrum; Higuchi bound as & ≥ π (BTICU 1) | Unaffected | Unaffected |

The BTICU 1 results stand because they concern the mode spectrum of a single brane, where & is the geometric phase of a mode's bulk profile, not an image correlation.

**Consequence.** No consistent construction examined so far supports heavy-particle production from the twist. As fixed in Section 2, BTICU 2 does not proceed to leptogenesis or dark-matter production. The central result of this paper is a negative one, and a clean one: in consistent quantum field theory, the elliptic identification of de Sitter space has no correlation-level signature for any observer.

**What remains open.**

1. **Route 3 (Aguirre–Gratton).** An identification beginning on a definite null surface is the one construction not yet tested, and the structure BTICU 0's bound required.
2. **Entropy.** If the identification is observable at all, the proposed no-boundary density matrix suggests it would be in the entropy of an observer's state. The question is whether that entropy differs from the Gibbons–Hawking value in any measurable way.
3. **The classical reading.** Route 1's commuting field reproduces the partition as a property of classical fluctuations. Whether that reading has any physical realisation, rather than being an artefact of the naive construction, is undecided.

## 7. Route 3: the null-boundary identification (Aguirre–Gratton)

Aguirre and Gratton propose that inflation may be past-eternal, with no initial singularity. They set cosmological boundary conditions on an infinite null surface near which spacetime is de Sitter, and their model suggests, without requiring, the identification of antipodal points. The resulting arrow of time is consistent for all observers who can communicate, while the statistical description of the whole universe is symmetric under a transformation that includes time reversal. (This section works from the published abstract and the standard geometry of the construction; the full text was not available here.)

**Geometry.** The null surface is the past boundary of the flat inflationary patch, η → −∞. Across it lies the complementary, contracting patch. With the antipodal identification, that patch is the time-reversed image of the expanding one, so each observer sees expansion away from the boundary. As in Route 2, no observer's patch contains both a point and its antipode.

**The only lever is the state on the boundary.** Within the expanding patch, the identification relates operators only to operators in the other patch, so, as in Route 2, it adds no image term to an observer's correlations. What the null-boundary construction does add is a place to specify the quantum state. There are two cases:

- **The Bunch–Davies condition on the boundary** (positive frequency as η → −∞, which is how the standard inflationary state is defined). Then every observer's correlations are the standard ones, and the result coincides with Route 2: no signature.
- **Any other state on the boundary.** A non-Bunch–Davies state imposed at η → −∞ is an excited initial state set infinitely far in the past. BTICU 0 §6 found that the folded non-Gaussianity of such a state grows without bound as the initial time recedes, and the standard literature on α-vacua reaches the same conclusion. Imposed on Aguirre and Gratton's infinitely distant boundary, it is excluded.

**Result.** Route 3 gives Outcome C: either the state on the null boundary is the standard one, and the identification has no correlation-level signature, or it is not, and it is excluded by the divergence already established in BTICU 0.

## 8. Conclusion across all three routes

| Route | Consistent? | Quantum dynamics for observers? | Image term in observers' correlations? | Outcome |
| --- | --- | --- | --- | --- |
| 1. Sanchez–Whiting | Yes | No (all commutators vanish) | Yes, as a classical correlation | A (strong form) |
| 2. CPT per observer | Yes | Yes | No | C |
| 3. Null boundary | Yes, with the standard state | Yes | No; any alternative state is excluded | C |

**The result.** In every consistent quantum construction examined, the antipodal identification of de Sitter space leaves no signature in the correlations any observer can measure. The image-sum results of BTICU 0 (& as a phase between a correlation and its image, the cos²(&/2) : sin²(&/2) partition, the antipodal commutator, the heavy-field dominance and the folded-shape signal) are properties of the naive kernel, and survive only in Route 1's commuting, classical field. BTICU 0 should carry a forward note to this effect.

**What stands.**

- **BTICU 1 in full.** Its & is the geometric phase of a brane mode's bulk profile, not an image correlation. The empty real arc on a healthy inflating brane, the ghost trade-off for a brane kinetic term, Higuchi's bound as & ≥ π, and the branch analysis are unaffected.
- **The dimension dependence of Δ**, and with it of the geometric phase, which is a property of mode functions.
- **This paper's negative result**, reached by testing outcomes stated in advance.

**Where the series goes next.** Two directions remain with genuine content. The first is the entropy of an observer's state in elliptic de Sitter space, where the proposed no-boundary density matrix could differ from the ordinary Gibbons–Hawking description. The second is BTICU 1's brane programme: the Kaluza–Klein continuum, a curved bulk, and the radion, where & appears as a geometric property that survives any choice of state.
