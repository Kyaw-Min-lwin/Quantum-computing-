# Foundations: intuition to code

## 1. Complex numbers and phase

A complex number z = a + bi is a point (a, b), or an arrow from the origin, on the complex plane. Its magnitude is sqrt(a² + b²). Its angle is its phase. Multiplication by i rotates the arrow 90 degrees counterclockwise: 1 → i → -1 → -i → 1.

Polar form describes the same arrow by length r and angle θ: z = r(cos θ + i sin θ) = r exp(iθ). Euler's identity exp(iθ) = cos θ + i sin θ places exp(iθ) on the unit circle. Python writes the imaginary unit as `1j`, not an undefined variable `j`.

## 2. Amplitudes are not probabilities

A pure qubit is |ψ⟩ = α|0⟩ + β|1⟩. In the computational basis its array is [α, β]. Each entry is a complex amplitude. The Born rule gives P(0) = |α|² and P(1) = |β|².

For z = a + bi, |z|² = conjugate(z) × z = a² + b². In particular i² = -1, but |i|² = 1. In code use `np.abs(state) ** 2`, not `state ** 2`.

When coherent alternatives contribute to the same outcome, their amplitudes add before taking a squared magnitude. They can reinforce or cancel. Do not apply this rule indiscriminately to classical alternatives or paths whose distinguishing information has been recorded.

## 3. Normalization and inner products

The two exhaustive, mutually exclusive measurement outcomes must have probabilities adding to one: |α|² + |β|² = 1. This is also ⟨ψ|ψ⟩ = 1: the state has unit length.

A bra is a conjugate transpose, not just a transpose. `np.vdot(a, b)` conjugates the first vector and sums component products. A self-inner-product is non-negative real; an inner product between different states can be complex. For normalized |φ⟩, the probability of the corresponding rank-one projective outcome is |⟨φ|ψ⟩|².

To normalize a nonzero vector, divide by its norm. For [1, i], the norm is sqrt(2), and the multiplying factor is 1/sqrt(2). The zero vector has no direction and cannot be normalized. This rescaling is a mathematical helper, not a deterministic physical gate for arbitrary inputs.

## 4. Relative phase and measurement basis

|+⟩ = (|0⟩ + |1⟩)/sqrt(2) and |-⟩ = (|0⟩ - |1⟩)/sqrt(2) both give 50/50 computational-basis probabilities. They are nevertheless different, orthogonal states. Their relative phase differs. Multiplying *every* amplitude by the same unit complex number gives a global phase and does not change the physical state.

A probability of 1/2 does not promise exactly half the outcomes in a finite experiment. Estimating the original state's probabilities requires repeated preparation followed by measurement. Repeated ideal measurements on the same already-collapsed qubit are not fresh preparations.

## 5. Gates and NumPy

For U = [[a, b], [c, d]], U[α, β] = [aα + bβ, cα + dβ]. The first column is U|0⟩; the second is U|1⟩. The input coefficients weight those columns. Each row tells how contributions combine into one output amplitude.

Use `gate @ state` for matrix-vector multiplication. `gate * state` uses elementwise multiplication and broadcasting, and does not apply the gate. A NumPy state of shape (2,) is a one-dimensional array, not a literal (2, 1) column matrix.

| Gate | Action on [α, β] | Meaning |
| --- | --- | --- |
| I | [α, β] | Leave unchanged |
| X | [β, α] | Exchange computational amplitudes |
| Z | [α, -β] | Flip the second amplitude's phase |
| H | [(α+β)/sqrt(2), (α-β)/sqrt(2)] | Mix amplitudes so interference can occur |

For H|+⟩, the two contributions to output 0 are each 1/2 and add to 1. The contributions to output 1 are +1/2 and -1/2 and cancel. For H|-⟩, cancellation occurs at output 0 instead. Therefore H turns the relative-phase difference into distinguishable computational outcomes.

Chronological H, Z, H is written H @ Z @ H @ state: the rightmost operation acts first. Starting at |0⟩ gives |+⟩, then |-⟩, then |1⟩. There is no intermediate measurement in this calculation.

## 6. Why unitarity matters

A closed-system gate obeys U†U = I, where `U.conj().T` is U†. Then the new squared length is ⟨ψ|U†U|ψ⟩ = ⟨ψ|ψ⟩ = 1. Individual outcome probabilities can change; their total remains one. Unitary operations also preserve overlaps and are reversible.

Do not automatically normalize after every gate to hide errors: a bad matrix might otherwise appear acceptable. Test the gate itself. Measurement and noise require a broader description than a single unitary on the qubit and are later topics.

`np.allclose` compares numerical vectors, allowing rounding error. It is not a general physical-state equivalence test: |ψ⟩ and -|ψ⟩ are physically equivalent even though their entries differ.
