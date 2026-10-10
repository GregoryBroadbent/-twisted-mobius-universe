# BTICU 6C — The Committed Definition

Oct 10, 2026 · @Gregory Broadbent

The coupling as written in 6B §4.2 is not a possible term in any local quantum theory while φ is a boson, so the definition forks and the fork is forced rather than chosen. Two branches survive: one in which φ is a fermion and the whole theory is free, and one in which the coupling is a Yukawa and the theory interacts. They are mutually exclusive in what they can support.

The modular weight β(ℓ) is settled separately and in the same direction: it is determined by the state and the region, not supplied to the Hamiltonian.

## The fork is forced

A 2π rotation acts as the identity on bosons and as −1 on fermions, so every term in H must contain an even number of fermion operators. Equivalently, fermion parity P = (−1)^F is superselected and \[H, P\] = 0 in any admissible theory.

§4.2's coupling is λ(φ†ψ↑ + φ†ψ↓ + h.c.). With φ a boson that is one fermion operator per term — odd. The term is therefore not available, independently of whether anyone can solve it. The audit's earlier finding, that the coupling is "only Gaussian-solvable if φ is fermionic", understated this: the constraint is admissibility, not solvability.

Tested in an explicit many-body Hilbert space, with a boson mode truncated at four quanta and the fermion algebra gated first:

| φ | Coupling | Fermion operators | max ‖\[H,P\]‖ | Parity-mixing block |
| --- | --- | --- | --- | --- |
| fermionic | λ(φ†ψ + h.c.) | 2, even | 0.000e+00 | 0.000e+00 |
| bosonic | λ(φ†ψ + h.c.) | 1, odd | 2.800e+00 | 4.427e+00 |
| bosonic | g φ (ψ†σ\_z ψ) | 2, even | 0.000e+00 | 0.000e+00 |

The middle row maps the even-parity subspace into the odd one, which is the concrete form of the violation.

**The principle that forbids it is the framework's own.** Section 1.2 of the Foundation paper rests on fermions requiring 4π rather than 2π — "the twist is built into the field itself". That is precisely the statement that a 2π rotation returns −1 on a fermion. The observation the electron picture is built on is the one that rules out the coupling written for it.

## Branch F — φ fermionic, theory free

This is the branch `BTICU6C_Coupled.py` already implements. Field content: a ring of M sites, each carrying three Grassmann-odd modes φ\_i, ψ\_{i↑}, ψ\_{i↓}, indexed 3i + s.

```latex
H_F = -t\sum_i \left(\phi_i^\dagger \phi_{i+1} + \text{h.c.}\right)
 - \tfrac{iv}{2}\sum_i \left(\psi_i^\dagger \alpha\, \psi_{i+1} - \text{h.c.}\right)
 + \lambda\sum_i \left(\phi_i^\dagger \psi_{i\uparrow} + \phi_i^\dagger \psi_{i\downarrow} + \text{h.c.}\right)
```

with α = σ\_x on the species index, and the bonds crossing i = M−1 → 0 carrying a factor −1 so the ring is antiperiodic. β(ℓ) does not appear; the reason is in the weight section below.

Every term is bilinear, so the theory is a free-fermion bilinear with no interaction anywhere in it. That fixes its behaviour completely:

- The ground state is every negative-energy mode filled, and the correlator G is the projector onto filled modes. No approximation is involved.
- All scaling dimensions sit at their free values. Δ\_φ = Δ\_ψ = 1/2, and measured Δ\_φ = 0.5000 with no drift in λ once the two-Fermi-point beating is accounted for.
- The central charge is 3 at λ = 0, measured 2.955, one unit per gapless species.
- The exact zero in the φ sector is a property of the φ–ψ coupling being equal on the two species, holding to 0.000e+00 at every λ and surviving any modification confined to the ψ block. It is a statement about one matrix element, not a symmetry of H.
- The ψ sector is a doubled lattice Dirac fermion with Fermi points at k = 0 and π; σ\_x labels bands, not chirality.
- λ\_c = √(tv/2), derived from det = −tv sin 2k − 2λ².

## Branch Y — φ bosonic, coupling Yukawa

This branch keeps φ a scalar, which is presumably what the physical picture wants, and pays for it by making the coupling cubic. Field content: a ring of M sites, each carrying a real scalar φ\_i with conjugate momentum π\_i, and two Grassmann-odd modes ψ\_{i↑}, ψ\_{i↓}.

```latex
H_Y = \sum_i \left[\tfrac{1}{2}\pi_i^2 + \tfrac{1}{2}(\phi_{i+1}-\phi_i)^2 + \tfrac{1}{2}m^2\phi_i^2\right]
 - \tfrac{iv}{2}\sum_i \left(\psi_i^\dagger \alpha\, \psi_{i+1} - \text{h.c.}\right)
 + g\sum_i \phi_i \left(\psi_i^\dagger \beta\, \psi_i\right)
```

**Why β = σ\_z.** For gφ(ψ†βψ) to be a Dirac mass term, β must anticommute with α = σ\_x. Of the four candidates, σ\_y and σ\_z anticommute with σ\_x while the identity and σ\_x commute with it — the same table that decided the Wilson term. Taking β = σ\_z gives ψ†βψ = n\_{i↑} − n\_{i↓}, so the scalar couples to the species imbalance.

The term is cubic, so this is a genuine interacting theory, and that changes what is true of it:

- Not Gaussian-solvable. It needs DMRG with the boson space truncated at some n\_max, or QMC. The MPO builder and DMRG are already gated to 1e-12 against exact diagonalisation and 1e-8 against exact correlators, so the apparatus exists; the boson truncation is the new piece.
- Scaling dimensions run with g. This is the only one of the two branches in which Δ\_e ≠ 1/2 is possible at all.
- At large g the scalar condenses, ⟨φ⟩ ≠ 0 gives ψ a mass, and the fermions gap out — dynamical mass generation, in the channel β = σ\_z selects. This is structurally what the framework wants from "mass as a decoherence scar", and it is a real mechanism rather than a picture.
- Δ is only defined in the gapless phase, so the transition in g has to be located before any scaling dimension is quoted. Where that transition sits is not yet known and is the first calculation this branch needs.

## What each branch forbids

The two branches are mutually exclusive in what they can support, and the split runs straight through 6B.

|  | Branch F | Branch Y |
| --- | --- | --- |
| φ | fermionic | bosonic scalar |
| Coupling | λ(φ†ψ + h.c.), bilinear | gφ(ψ†σ\_zψ), cubic |
| Single-particle matrix K = \[\[A, C\], \[C†, B\]\] | exists | does not exist |
| Anomalous dimensions | forbidden | permitted |
| Δ\_e = 1.50 reachable | no, never | unknown, possible |
| Exactly solvable | yes | no |

**The structural problem.** 6B §4.2's formalism belongs to Branch F. A block matrix K = \[\[A, C\], \[C†, B\]\] is a single-particle object, and only a bilinear coupling has one; a cubic term has no single-particle matrix at all. But 6B's claims need Branch Y, because Δ\_e = 1.50 requires an anomalous dimension and Branch F forbids every one of them. The formalism and the claims are on opposite sides of the fork.

That is the sharpest consequence of fixing the definition, and it is not a matter of degree. In Branch F, Δ\_e = 1.50 is not approximately wrong or hard to reach — it is unavailable, because a free theory has no anomalous dimensions to carry it. Any route to 1.50 inside Branch F is reaching the number by some means other than the dynamics, which is what the weight section describes.

**So the commitment has a price either way.** Choosing F means φ is a third fermion flavour rather than a scalar substrate, and every scaling dimension is 1/2 forever; what is left to derive is not Δ\_e. Choosing Y means §4.2's block formalism, the modular-spectrum route built on it, and the d\_eff derivation that used it are all discarded and rebuilt — against a theory that has to be solved numerically rather than diagonalised.

## The weight β(ℓ) is an output

β(ℓ) is determined by the state and the region together, so it is not a quantity a construction supplies. For a free-fermion chain ρ\_A is Gaussian and the modular Hamiltonian follows from the restricted correlator alone, h\_A = log((1 − G\_A)/G\_A), with no parameter anywhere in it. Computed for a 16-site interval in a ring of 200, the nearest-neighbour amplitude of h\_A tracks the interval form (R² − x²)/2R at correlation **0.99972**, with per-point ratios between 0.970 and 1.013. The weight came out; it was not put in.

This settles why β(ℓ) is absent from both Hamiltonians above. It is also why the modular-spectrum route cannot yield a scaling dimension at any value: the entanglement spectrum is set by ln(R/a), so E₀(R) ∝ R^−Δ\_e has no power law to fit.

**The W^α conjugation.** Pillar 1 records a "core physics fix": A = W^¼ K\_φ W^¼ and B = W^¼ K\_ψ W^¼, which "produces Δ\_e = 1.50 (target achieved)". The construction has a definite length dimension and nothing else. With \[K\_φ\] = length⁻², \[K\_ψ\] = length⁻¹ and \[W\] = length⁺¹, the exponents are fixed by counting:

```latex
\Delta_e^{(\phi)} = 2 - 2\alpha, \qquad \Delta_e^{(\psi)} = 1 - 2\alpha
```

Measured against an α sweep, both hold to **0.00000** at every α tested from 0 to 0.5. Three different weight profiles with the same length dimension — the interval form, a cosine, a linear tent — give identical exponents, so the shape of β is irrelevant. Normalising W to be dimensionless removes the α dependence entirely and returns Δ\_e = 2 for every α, which identifies W's length dimension as the whole source of the tunability.

Two consequences. The solution of 2 − 2α = 1.5 is α = 0.2500, which is the recorded value; so the target is reached by arithmetic rather than by dynamics. And the two blocks differ by exactly 1 at every α, so they cannot be brought into agreement at any α at all.

**Checked against the file.** `BTICU6C_Continuum_Extrapolation.py`, which the 6C manifest names as the production-ready Pillar 1 implementation, was run unmodified. It reports Δ\_e = 0.0000 at N = 100, 150, 200 and 300, a continuum limit of −0.0000 ± 0.0570, and ghost-free at every point — with E₀ = 1.000000e-02 at every N and every R.

That constant is the `1e-2` in the positivity shift. When `min_eig < 0` the shift adds `|min_eig| + 1e-2`, so the new minimum is exactly 1e-2 by arithmetic, whatever the input. E₀ is therefore not an eigenvalue, Δ\_e = 0 follows because log E₀ is constant in log R, the ±0.0570 is the code's own heuristic `0.01 + 0.05/√N` rather than a fit error, and the reported R² values of 0.5782, 0.3394 and 0.9558 are the fit chasing floating-point jitter at the 1e-9 level.

**Why the spectrum was negative.** Two independent causes. `kinetic_phi_dense` has main diagonal −2/dℓ² and off-diagonal +1/dℓ², which is +d²/dℓ² rather than the −d²/dℓ² its docstring states, so K\_φ is negative definite — maximum eigenvalue ≤ 0 at every N and R tested. And `dellam = πR/N` runs the grid to ℓ ≈ 3.11R while β(ℓ) = (R² − ℓ²)/2R is positive only for ℓ < R, so the weight is negative across 68% of the lattice, minimum −4.24 at N = 100, R = 1. The recorded correction to Δℓ = R/N takes that to 0% negative, so it was not cosmetic.

**The ghost-free result is circular.** `is_ghost_free = (E0 > -1e-10)` passes because E₀ = 1e-2. The unshifted minimum was negative in all four cases checked, while the file reports ghost-free in all four. The line that removes the negative eigenvalues is what makes the test for negative eigenvalues pass.

**Two further implementation findings.** `kinetic_psi_dense` is not Hermitian — ‖K − K†‖ = 15.9 at N = 50 and 31.8 at N = 100 — because its spinor block is real antisymmetric; the `(K + K†)/2` step then deletes that block outright, taking its off-diagonal norm from 37.3 to 0.000000e+00 and leaving the ψ sector a diagonal multiplication operator 2β\_i/dℓ² with no derivative in it. And `C = λ W_φ @ ones(N_φ, N_ψ)` has rank 1, coupling every φ site to every ψ site, rather than the on-site coupling of §4.2.

**The exponent result holds on the real file.** With the sign corrected, the shift removed and Δℓ = R/N, the anticommutator {W, K\_φ} gives Δ\_e = 1.00000 against a dimensional prediction of 1; W^0.125 gives 1.75000, W^0.25 gives 1.50000, W^0.375 gives 1.25000, each matching 2 − 2α exactly. Across the whole α sweep the deviation from 2 − 2α is 0.00000, and across three weight profiles the spread in Δ\_e is 2.92e-13. So α = ¼ is the solution of 2 − 2α = 1.5, and β's shape contributes nothing.

**The three checks, now run** on both production builds:

1. β's shape, swapped between (R² − ℓ²)/2R, a cosine and a tent: Δ\_e moves by 2.9e-08. The exponent is dimensional.
2. The φ and ψ blocks agree exactly, both giving 2 − 2α, because `kinetic_psi_matrix` carries a 2/dℓ² diagonal — dimension L⁻², not the L⁻¹ of a Dirac operator. Substituting a properly Hermitian first-order operator gives the ψ block 1 − 2α and restores the predicted difference of exactly 1.00000 at every α.
3. The α sweep tracks 2 − 2α to 2.8e-07, so α = ¼ is the solution of an equation.

**PRODUCTION\_FIXED, read and run.** Four of the earlier build's defects are genuinely repaired in it: the K\_φ sign, the Δℓ = R/N spacing, the positivity shift — removed, so `is_ghost_free` now tests real eigenvalues and passes with a minimum of 5.70 at N = 300 — and the coupling, now local and of rank N\_φ. It reproduces Δ\_e = 1.5000 with R² = 1.0000 at N = 100, 150, 200 and 300, the ±0.0570 still coming from the heuristic error model rather than the fit.

**The exponent is still the dimension count.** Δ\_e follows 2 − 2α to 2.8e-07 across α from 0 to 0.5, and β's shape moves it by 2.9e-08. The fitted 1/N coefficient is 0.000001 and R² is 1.0000 at every N, which is not how a dynamical exponent behaves on a finite lattice.

**The ψ sector's Dirac structure is absent twice over.** `kinetic_psi_matrix` has a diagonal of 2/dℓ², so it is second-order, and that is why both blocks give 1.50 and agree to 0.00000 — the docstring's "B = W^¼ K\_ψ W^¼ produces Δ\_e = 1.50" is a statement about that diagonal. Separately, K\_ψ is still not Hermitian, with ‖K − K†‖ = 50, 100 and 200 at N = 50, 100 and 200, and the Hermitisation step deletes its off-diagonal — 65.8 to 7.1e-15 at N = 200 — leaving the block diagonal.

**The coupling contributes nothing.** \[C\] = L¹ against \[A\] = L^(2α−2), so the two blocks carry different length dimensions and the 1/dℓ² terms swamp λβ as N grows. Driving λ from 0 to 50, a hundred times the production value, moves E₀ by 2.4e-03 in relative terms; at λ = 0.5 the shift from λ = 0 is 2.4e-07. The φ–ψ coupling, which is what the construction exists to study, does not enter the number it reports.

## Making the block matrix dimensionally consistent

A block matrix \[\[A, C\], \[C†, B\]\] presumes φ and ψ share one space and one normalisation, so their kinetic operators must be of the same order and the coupling must be an energy in those units, conjugated by the same weight power. Imposing that decides things the construction had left open, and it changes the answer rather than tidying it.

**It works only in Branch F, and it moves the exponent.** Same-order kinetic operators means φ's must be first order, which holds only if φ is a fermion. Then \[D\_φ\] = \[D\_ψ\] = L⁻¹, every block carries L^(2α−1), and Δ\_e = 1 − 2α — confirmed to 0.00000 across α from 0 to 0.5 on the full K. **At α = ¼ the consistent construction gives Δ\_e = 0.50000, not 1.50.** Reaching 1.50 would require α = −0.25, a negative power of the weight.

**The coupling starts working.** With λ\_eff = λ/dℓ, the lattice energy that matches the kinetic blocks, E₀ moves by 14%, 71% and 284% as λ runs 0.1, 0.5, 2.0. Under the unmatched scalings λ/R and bare λ it stays between 0.07% and 1.4%. So the φ–ψ coupling enters the result once the dimensions match, and not before.

**With φ bosonic, no α works.** Keeping K\_φ = −d²/dℓ² alongside a first-order ψ, the two blocks differ by exactly 1.00000 at every α tested. No choice of α makes the matrix consistent. The fork reappears here as a dimensional obstruction rather than as an argument about statistics, which is independent confirmation of it.

**Positivity is the wrong test for this object.** The consistent K has E₀ = −140.36, because a first-order operator is not positive definite — and that is correct for a modular Hamiltonian. Computed from a state rather than assembled, h\_A = log((1 − G\_A)/G\_A) has an exactly symmetric spectrum: ±11.04 at L\_A = 8, ±17.86 at 12, ±24.78 at 16, ±31.75 at 20, with exactly half the eigenvalues negative at every size. This follows from ν ∈ (0,1), since log((1−ν)/ν) is positive for ν < ½ and negative for ν > ½. So `is_ghost_free = np.all(evals > -1e-10)` tests a property a modular Hamiltonian cannot have, and PRODUCTION\_FIXED passing it is evidence that its K is not one. Positivity here is a disqualification, not a qualification — which revises the earlier note above crediting that test as sound: no shift conceals anything in that build, but the property being checked is the wrong one.

## What the object is, without the name

Described on its own terms, the construction is a weighted Dirac operator on an interval: W^α D W^α, with W = diag(β(ℓ)) a weight vanishing at both endpoints, plus an on-site coupling between species. That makes it a degenerate operator in the Sturm–Liouville sense, whose boundary behaviour is the kind of thing that subject computes. It is not a modular Hamiltonian, and dropping the name removes three commitments the object was never obliged to meet.

**The three failures belonged to the name, not the object.** A modular Hamiltonian has β as an output — recovered at correlation 0.99972 from the state alone — has a spectrum set by ln(R/a) with no power law in it, and has eigenvalues straddling zero, exactly half negative at every region size. The assembled operator takes β as an input, does yield a power law, and is positive definite. Those are three ways of being a different object, not three defects.

**The observable and the Dirac structure are mutually exclusive here.** This is what unnaming it turns up, and it is the sharpest item in this section. The assembled K is positive definite — minimum eigenvalue 5.801, 5.722, 5.682 at N = 100, 200, 400, converging, with the maximum growing as N² — so evals\[0\] is a genuine ground state and E₀(R) is a well-defined observable. But that positivity comes from two things: φ's kinetic term being the Laplacian rather than a Dirac operator, and the Hermitisation step deleting ψ's Dirac structure. Restore either and the operator becomes indefinite, evals\[0\] diverges linearly in N — successive ratios 2.031, 2.015, 2.008, 2.004 on doubling — so it is the band edge rather than a ground state, and E₀(R) stops being an observable at all. The observable exists because the physics was removed.

**A replacement observable exists.** For the dimensionally consistent operator the convergent quantity is the eigenvalue nearest zero. It settles as N grows and gives an exponent against R of 0.50000 at N = 100, 200, 400 and 800 alike. So the consistent operator does have a stable spectral exponent — and it is 1 − 2α, the dimension count again. Whichever observable is chosen, the exponent is a property of how the operator was assembled rather than of a region or a dynamics.

**Why the renaming is more than tidiness.** Every check in the sections above tested whether the object satisfied its name, and those all returned no. Asking instead what the operator does returns answers: whether it is positive definite turns on one term, its band edge diverges while its near-zero spectrum converges, and its exponent is fixed by its assembly. None of those is yet a result about physics, but each is a statement about the object that can be built on, which the name-shaped questions were not.

## What §1.2 can support

The 4π observation is correct and standard, the Möbius realisation of it is ruled out by a torsion argument, and the rigorous version of "fermions without orientability" has been computed by others with a null result. So §1.2's criticism of the sphere model stands while its positive construction does not.

**The obstruction.** Realising rotations as traversals of the Möbius core needs a homomorphism π₁(SO(3)) = ℤ/2 → π₁(Möbius band) = ℤ. Setting f(g) = k for the generator, g² = e forces 2k = 0 in ℤ, so k = 0. ℤ is torsion-free and ℤ/2 is pure torsion, so only the trivial map exists, and the 2π rotation must correspond to the contractible loop rather than to the orientation-reversing circuit. This is not a missing detail. It is a correspondence between objects that admit only the zero map in that direction.

**No action exists either.** A nontrivial SO(3) action on a surface needs orbits of dimension 1 or 2. Dimension 1 would require a two-dimensional closed subgroup, and su(2) has none: su(2) is ℝ³ under the cross product, so \[X,Y\] is orthogonal to both arguments, and its component inside span(X,Y) measured 0.0e+00 for every independent pair tested. The available two-dimensional orbits are S² = SO(3)/SO(2) and ℝP² = SO(3)/O(2), and neither is a subsurface of a band with boundary. Every orbit is therefore a point and the action is trivial. The subalgebra half of this is computed; the orbit half is a standard argument rather than something run.

**Where the intuition is right, and where it parts.**

|  | Möbius core | SO(3) rotations |
| --- | --- | --- |
| Holonomy after n circuits | (−1)ⁿ | (−1)ⁿ |
| Fundamental group | ℤ | ℤ/2 |
| Two circuits, or 4π | class 2, not contractible | class 0, contractible |
| Orientation restored | yes | yes |

Both holonomies were checked and both are exact: the transverse frame on the band flips at one circuit and returns at two, and the SU(2) lift of 2π ends at −1 while 4π ends at +1. One circuit flips something and two put it back — true of both, and the whole content of the intuition. The parting is that in SO(3) two circuits also put back the loop. A 4π rotation can be continuously undone, which is observable with a belt, whereas on the band two circuits restore orientation and leave behind a loop that cannot be contracted. Restoring orientation and closing the loop are different statements, and the picture supplies the first where the physics requires the second.

**What would have to be built instead.** The object whose topology is the 4π structure is SU(2) ≅ S³, double-covering SO(3) ≅ ℝP³; a surface is the wrong dimension with the wrong fundamental group, and no repair changes either. For fermions on a genuinely non-orientable space the correct object is a pin structure, not a band: spin structures require orientability, and without it one takes pin⁺ or pin⁻. BTICU 5 already works with pin⁺, so the framework has reached the right mathematics — and what lies past that door is already on record in the audit, where Ω₅^{Pin±}(BSU(n)) = 0 gave no constraint on the Standard Model spectrum.

**Consequence for the branch choice above.** Taken as a constraint rather than as a picture, the 4π property forbids any term odd in the fermion field, and that is exactly what rules out a bosonic φ with a bilinear coupling. The principle is what forces the fork.

## What has to be decided next

**The branch.** This is a choice about what the theory is, not a calculation, and nothing downstream can be built until it is made. Branch F is already solved and its predictions are known, which means choosing it settles the programme's content immediately and not in the direction the claims went. Branch Y is unsolved, is the only branch where Δ\_e ≠ 1/2 is even possible, and costs §4.2's formalism.

**If Branch Y is chosen**, the first calculation is not Δ\_e. It is locating the transition in g where the scalar condenses and gaps the fermions, because Δ has no meaning on the massive side. The boson truncation n\_max has to be converged alongside the bond dimension, and the free limit g = 0 has a known answer to gate against.

**What is already answered**, so that it is not revisited: φ cannot be a boson with a bilinear coupling, β(ℓ) is not an input to h, and β = σ\_z is forced for a Yukawa mass term by anticommutation with α = σ\_x.
