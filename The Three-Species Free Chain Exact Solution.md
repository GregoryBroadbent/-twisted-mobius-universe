# The Three-Species Free Chain: Exact Solution

Oct 10, 2026 · @Gregory Broadbent

The coupled three-species chain defined by BTICU 6C's field content diagonalises in closed form. Rotating the species sector to ψ± = (ψ↑ ± ψ↓)/√2 separates it into a 2×2 coupled block and a band that touches nothing, giving all three dispersions exactly and settling three quantities that had only been measured numerically: the exact zero, the constant 0.70711, and the critical coupling.

A free three-band tight-binding chain is elementary, and nothing here is presented as new. What follows is the calculation for this particular model and what it does and does not contain.

## The model

An antiperiodic ring of M sites, each carrying three Grassmann-odd modes φ\_i, ψ\_{i↑}, ψ\_{i↓}, indexed 3i + s.

```latex
H = -t\sum_i \left(\phi_i^\dagger \phi_{i+1} + \mathrm{h.c.}\right)
 - \frac{iv}{2}\sum_i \left(\psi_i^\dagger \alpha\, \psi_{i+1} - \mathrm{h.c.}\right)
 + \lambda\sum_i \left(\phi_i^\dagger \psi_{i\uparrow} + \phi_i^\dagger \psi_{i\downarrow} + \mathrm{h.c.}\right)
```

with α = σ\_x acting on the species index, and the bonds crossing i = M−1 → 0 carrying a factor −1 so that the ring is antiperiodic and zero modes stay off half filling.

φ is Grassmann-odd by necessity rather than by choice: a term linear in fermion operators is not invariant under a 2π rotation, which acts as −1 on fermions, so λ(φ†ψ + h.c.) is admissible only if φ is itself a fermion. φ is therefore a third fermion flavour, not a scalar substrate.

Every term is bilinear. The many-body problem reduces to a single-particle matrix at each momentum, the ground state is every negative-energy mode filled, and the correlator is the projector onto those modes. No approximation enters anywhere.

In the basis (φ, ψ↑, ψ↓) the single-particle Hamiltonian is

```latex
H(k) = \begin{pmatrix} -2t\cos k & \lambda & \lambda \\ \lambda & 0 & v\sin k \\ \lambda & v\sin k & 0 \end{pmatrix}
```

The ψ block is v sin(k)·σ\_x, a doubled lattice Dirac fermion with Fermi points at both k = 0 and k = π. Throughout what follows t = v = 1 where a number is quoted.

## Diagonalisation

Rotate the species sector to ψ± = (ψ↑ ± ψ↓)/√2. This diagonalises σ\_x, giving +1 on ψ₊ and −1 on ψ₋, and turns the coupling column (λ, λ) into (√2λ, 0):

```latex
H(k) = \begin{pmatrix} -2t\cos k & \sqrt{2}\lambda & 0 \\ \sqrt{2}\lambda & v\sin k & 0 \\ 0 & 0 & -v\sin k \end{pmatrix}
```

The model is therefore a 2×2 coupled block plus a band that touches nothing. φ couples to the symmetric combination at strength √2λ and to the antisymmetric combination not at all.

The three dispersions follow at once. The decoupled band is linear in sin k, and the coupled pair are the eigenvalues of the 2×2:

```latex
E_3(k) = -v\sin k
```

```latex
E_{1,2}(k) = \frac{1}{2}\left[\left(-2t\cos k + v\sin k\right) \pm \sqrt{\left(2t\cos k + v\sin k\right)^2 + 8\lambda^2}\,\right]
```

**Verification.** The closed form was compared against direct numerical diagonalisation of H(k) at 4001 momenta spanning the Brillouin zone, for each of six couplings including λ\_c itself.

| λ | Worst \|closed − numerical\| |
| --- | --- |
| 0.0000 | 2.2e-16 |
| 0.2000 | 8.9e-16 |
| 0.5000 | 8.9e-16 |
| 0.7071 | 8.9e-16 |
| 0.9000 | 8.9e-16 |
| 2.0000 | 1.8e-15 |

The block structure was checked directly as well: at k = 0.9 and λ = 0.4 the φ–ψ₊ entry measures 0.565685, which is √2λ to six figures, while the largest coupling of ψ₋ to anything else is 6.5e-18.

## The decoupled mode

Three quantities that had been measured numerically follow from ψ₋ lying outside the coupled block.

**The exact zero.** P\_φ H ψ₋ = 0 identically, measured as 0.000e+00 at λ = 0, 10⁻⁶, 0.1, 0.5, 2 and 50. This is a basis vector sitting outside a block, not a symmetry of H. Two consequences that were previously puzzling become straightforward: the zero survives any modification confined to the ψ sector that keeps the two species' couplings equal — which is why adding a Wilson term left it at 0.000e+00 even at r = 0.5 where the ℤ₂ species symmetry is plainly broken — and it is a statement about one matrix element rather than about the Hamiltonian. The zero is both more robust and less significant than it appeared.

**The constant 0.70711.** The ratio of overlap to detuning measured 0.70711, constant over six decades of detuning. It is exactly 1/√2 = 0.7071067812, the normalisation of the antisymmetric combination. Nothing dynamical enters it.

**The critical coupling.** The 2×2 block has determinant

```latex
\det = (-2t\cos k)(v\sin k) - 2\lambda^2 = -tv\sin 2k - 2\lambda^2
```

so a zero mode in the coupled sector requires sin 2k = −2λ²/(tv), which has a solution only when λ² ≤ tv/2. Hence

```latex
\lambda_c = \sqrt{tv/2}
```

equal to 1/√2 ≈ 0.707107 at t = v = 1. Note that λ\_c and the constant above coincide numerically at t = v = 1 for unrelated reasons — one is a normalisation, the other a determinant condition — and they separate as soon as t ≠ v.

Above λ\_c the coupled block is gapped. The decoupled band is not: E₃ = −v sin k vanishes at k = 0 and k = π for every λ. **The model therefore never gaps completely at any coupling strength.** λ\_c marks where the coupled sector gaps, not where the model does.

## Phase structure and scaling dimensions

Below λ\_c there are six Fermi points: four from the coupled block, at the solutions of sin 2k = −2λ²/(tv), and two from the decoupled band at k = 0, π. Above λ\_c only the decoupled band survives, leaving two. Central charges were measured from the entanglement entropy against ln L at L = 16 to 64.

| λ | Regime | Fermi points | c |
| --- | --- | --- | --- |
| 0.00 | below λ\_c | 6 | 2.963 |
| 0.30 | below λ\_c | 6 | 2.964 |
| 0.60 | below λ\_c | 6 | 2.970 |
| 0.70 | below λ\_c | 6 | 3.100 |
| 0.75 | above λ\_c | 2 | 0.988 |
| 1.00 | above λ\_c | 2 | 0.988 |
| 2.00 | above λ\_c | 2 | 0.988 |

So c = 3 below λ\_c and c = 1 above it, one unit per gapless Dirac pair. The row at λ = 0.70 reads 3.100 rather than 2.96 because it sits just below λ\_c, where the block's Fermi points are close to merging at 0.72π and 0.78π and the finite-M correlator has not converged. That is expected next to a transition rather than a feature of the model.

**Scaling dimensions.** Measured from correlator decay against the conformal distance on a ring of 2048 sites, fitted over separations 40 to 400.

| λ | φ | ψ₊ | ψ₋ |
| --- | --- | --- | --- |
| 0.00 | 0.50000 | 0.50000 | 0.50000 |
| 0.30 | 0.49977 | 0.49861 | 0.50000 |
| 0.60 | 0.49623 | 0.49264 | 0.50000 |
| 1.00 | gapped | gapped | 0.50000 |
| 2.00 | gapped | gapped | 0.50000 |

Every dimension is ½, as a free theory requires. Two features are worth naming. ψ₋ reads exactly 0.50000 at every λ, because λ cannot reach it — the decoupling again. And above λ\_c the φ and ψ₊ sectors have no scaling dimension at all rather than a different one, since a gapped sector's correlator decays exponentially and has no power law to fit.

The drift in the coupled sectors below λ\_c, worst 0.0074 at λ = 0.6, is the finite-M fitting window. It is not a running dimension: a free theory has nothing to run, and the same estimators were calibrated against the Bethe ansatz for the t–V chain to 0.003 before being used here.

## What the model cannot support

Stated as a boundary rather than an absence, since the solution is complete and the limits are therefore exact rather than provisional.

There is no anomalous dimension anywhere in the model, because there is no interaction. Δ\_e = 1.50 is not hard to reach in it — it is unavailable. An effective dimension d\_eff cannot be derived from interactions that are not present. And λ, the only free parameter, changes the phase structure and the gap but not a single scaling dimension.

The model also does not contain a scalar. φ is a third fermion flavour, forced by rotational invariance once the coupling is bilinear, so the 1D substrate of the electron picture is not what this Hamiltonian describes. Anything resting on φ being a scalar needs the Yukawa form instead, which is a different and unsolved theory.

What the solution does provide is the free baseline. An interacting version cannot be shown to do anything until there is an exact free result to compare it against, and that is now in hand.

## How each number was computed

All computations are single-particle: a 3×3 matrix per momentum, with many-body quantities built from the projector onto filled modes.

| Quantity | Method |
| --- | --- |
| Closed-form check | Analytic bands against numerical diagonalisation of H(k) at 4001 momenta, six values of λ. |
| Exact zero | P\_φ H ψ₋ evaluated directly, λ over six decades to 50. |
| Block structure | H(k) conjugated into the (φ, ψ₊, ψ₋) basis; off-block entries read off. |
| λ\_c | Determinant condition solved analytically, confirmed against where the Fermi-point count drops. |
| Fermi points | Local minima of min\|E(k)\| reaching zero over 400001 momenta — not sign changes of sorted bands, which touch zero rather than crossing it. |
| Central charge | Entanglement entropy of the restricted correlator at L = 16 to 64, M = 600, fitted as S = (c/3) ln L. |
| Scaling dimensions | Correlator decay against the conformal distance on a ring of 2048, separations 40 to 400, odd only. |

The scaling-dimension estimator was calibrated against the Bethe ansatz for the half-filled t–V chain before use, worst error 0.003 for V ≤ 1.5.
