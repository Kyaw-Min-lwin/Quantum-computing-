# Rz, Ry and Rx: continuous single-qubit control

Guided learning notes — 12 October 2026.

## Rz: two opposite half-phase shifts

Use λ for the gate angle, distinct from the state coordinates θ and φ. Rz rotates α backward by λ/2 and β forward by λ/2. The relative phase therefore increases by λ/2 − (−λ/2) = λ. Magnitudes and θ stay fixed. Poles remain fixed physically because the only nonzero amplitude acquires a global phase.

Rz(λ) = diag(e⁻ⁱλ⁄², eⁱλ⁄²) = e⁻ⁱλ⁄² P(λ)

## Physical equivalence is stronger than matching probabilities

Rz(π/2) and S are different matrices, but their outputs for any single-qubit input differ only by the common factor e⁻ⁱπ⁄⁴. That is why they have the same physical action when applied directly to that qubit—not merely because computational probabilities match. Rz(π)|+⟩ = −i|−⟩: an equatorial half turn. Do not add another 1/√2 if it is already included in α and β.

Rz(π) = −iZ

## Ry mixes amplitudes

A positive y-axis quarter turn moves north toward +x. Starting from |0⟩, Ry(λ) gives cos(λ/2)|0⟩ + sin(λ/2)|1⟩. This supplies the first matrix column. The standard second column [−s,c]ᵀ is unit length and orthogonal to [c,s]ᵀ. Here c=cos(λ/2), s=sin(λ/2). Orthogonality alone does not uniquely fix its phase; this is the standard rotation convention.

Ry(λ) = [[c, −s], [s, c]]; [α,β]ᵀ → [cα−sβ, sα+cβ]ᵀ

## Ry examples and interference

Ry(π/2)|0⟩ = |+⟩. Apply it again: the first output contributions cancel and the second add, giving |1⟩. Unlike Rz, the off-diagonal terms can create a nonzero second amplitude from input |0⟩. Ry(π/2) is not H: it sends plus to |1⟩ while H sends plus to |0⟩. For a general point, Ry can change both θ and φ; it is not always a simple increase of θ.

Ry(π/2)|+⟩ = |1⟩; Ry(π/2)|1⟩ = −|−⟩

## Rx and the direction of rotation

The x-axis runs through plus and minus. With the right-hand convention, a positive x-axis rotation takes +z toward −y. The transferred amplitude gains −i, selecting this equatorial direction. Starting from |0⟩, Rx and Ry give equal computational probabilities for the same angle, but generally different relative phases.

Rx(λ) = [[c, −is], [−is, c]]; [α,β]ᵀ → [cα−isβ, −isα+cβ]ᵀ

## Rx examples and fixed axis

Rx(π/2)|0⟩ = (|0⟩−i|1⟩)/√2, at −y. Rx(π)|0⟩ = −i|1⟩, physically south. A state on the rotation axis stays fixed: Rx(λ)|+⟩ = (c−is)|+⟩ = e⁻ⁱλ⁄²|+⟩. Only global phase changes.

Rx(π) = −iX

## Preparing a pure state

Start at |0⟩. Ry(θ) chooses the two magnitudes; P(φ) then chooses relative phase. Together these can prepare any pure single-qubit state up to global phase. Adjustable rotation angles are the parameters later optimized in variational circuits. Learning this construction does not yet complete the QML training topic.

P(φ)Ry(θ)|0⟩ = cos(θ/2)|0⟩ + eⁱφ sin(θ/2)|1⟩

## Checkpoint pending — answer before continuing

1. Compare Ry(π/2)|0⟩ and Rx(π/2)|0⟩. 2. Explain why Ry can create an equatorial state from north while Rz cannot. 3. Explain why Rx leaves plus physically unchanged. 4. Choose θ and φ to prepare (√3/2)|0⟩ + (i/2)|1⟩ using Ry then P. Answers have not yet been submitted.

Next: tensor products → two-qubit states → controlled gates → entanglement.
