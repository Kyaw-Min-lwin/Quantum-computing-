# Phase gates and physical equivalence

Guided learning notes — 12 October 2026.

## The phase gate

Multiplying a complex amplitude by a unit complex number rotates its arrow without changing its length. P(λ) leaves α fixed and rotates β by λ. Its matrix is diagonal: the basis states do not mix.

P(λ) = diag(1, eⁱλ); [α, β]ᵀ → [α, eⁱλβ]ᵀ

## S, T and Z

S turns the second amplitude by 90°, T by 45°, and Z by 180°. Consecutive phase shifts add angles, so T² = S, S² = Z, and Z² = I. These are rotations of complex amplitudes, not a particle moving in physical space.

S = diag(1, i); T = diag(1, eⁱπ⁄⁴); Z = diag(1, −1)

## Global versus relative phase

Global phase multiplies every amplitude by the same unit complex number. Both amplitude arrows rotate together, preserving their relative angle. S instead rotates only the second amplitude. S|0⟩ = |0⟩ exactly because i × 0 = 0; S|1⟩ = i|1⟩ differs only globally; S|+⟩ = (|0⟩ + i|1⟩)/√2 changes relative phase. A zero amplitude has no defined phase.

i|+⟩ = [i, i]ᵀ/√2, whereas S|+⟩ = [1, i]ᵀ/√2

## Why global phase is unobservable

For any outcome vector |v⟩, a common phase multiplies the overlap amplitude by that same factor. Its magnitude remains unchanged. This holds in every measurement basis. Matching computational probabilities alone is not enough to establish physical equivalence.

|⟨v|eⁱγψ⟩|² = |eⁱγ|² |⟨v|ψ⟩|² = |⟨v|ψ⟩|²

## Revealing phase with interference

H combines the two amplitudes: one output uses their sum, the other their difference. Thus H|+⟩ = |0⟩ and H|−⟩ = |1⟩. Applying H then measuring computationally implements a plus/minus-basis measurement. For S|+⟩, H produces [(1+i)/2, (1−i)/2]ᵀ, giving 50/50. Compare this with H|+⟩, which gives 0 certainly. Repeated preparations reveal the statistical difference.

H[α, β]ᵀ = [(α+β)/√2, (α−β)/√2]ᵀ
