# From amplitude magnitudes to the Bloch sphere

Guided learning notes — 12 October 2026.

## Why two parameters remain

Two complex amplitudes initially contain four real numbers. Normalization removes one independent choice; unobservable global phase removes another. A pure qubit therefore needs two real parameters. Counting parameters motivates the sphere; the construction below gives its actual coordinates.

α = r₀eⁱγ₀, β = r₁eⁱγ₁; φ = γ₁ − γ₀

## Choose a representative

If α is nonzero, factor its phase eⁱγ₀ out of the entire state. Omitting this global factor leaves the first coefficient real and nonnegative, with the relative phase in the second coefficient. This is a choice of representation, not a physical operation. If α is zero, the physical state is simply |1⟩.

|ψ⟩ ∼ r₀|0⟩ + eⁱφr₁|1⟩; r₀² + r₁² = 1

## Where cosine and sine come from

Make a new flat plot with r₀ horizontally and r₁ vertically. This is NOT the complex plane: these are magnitudes of two different amplitudes. Normalization puts (r₀,r₁) on the upper-right quarter of the unit circle. Draw a radius to the point and call its angle from horizontal t. The right triangle has adjacent side r₀, opposite side r₁, and hypotenuse 1. Therefore cos t = r₀/1 and sin t = r₁/1. Trigonometry parametrizes the normalization constraint; it adds no new physical rule.

r₀ = cos t; r₁ = sin t; 0 ≤ t ≤ π/2

## Worked magnitude example

At t = 30°, r₀ = √3/2 and r₁ = 1/2. The probabilities are 3/4 and 1/4. The hypotenuse is √(3/4 + 1/4) = 1. At t = 45°, both magnitudes are 1/√2. The magnitude plot contains no relative-phase information: plus, minus, and (|0⟩+i|1⟩)/√2 all occupy that same magnitude point.

P(0) = cos²t; P(1) = sin²t

## The half-angle and the sphere

We place |0⟩ and |1⟩ at opposite poles of the Bloch sphere. The magnitude angle t runs from 0° to 90°, while the sphere polar angle θ runs from 0° to 180°, so θ = 2t. Angles in the magnitude plot and on the Bloch sphere are different. θ controls computational probabilities; φ controls relative phase. Pure states lie on the surface; this is not a spatial orbit of an electron.

|ψ⟩ = cos(θ/2)|0⟩ + eⁱφ sin(θ/2)|1⟩; 0 ≤ θ ≤ π, 0 ≤ φ < 2π

## Poles and equator

North (θ=0) is |0⟩. South (θ=π) is eⁱφ|1⟩, where φ is only global phase. Like longitude at a geographic pole, φ does not select a new point at either pole. At the equator θ=π/2, all states have 50/50 computational probabilities, yet changing φ generally changes the physical state. φ=0 gives plus, φ=π/2 gives (|0⟩+i|1⟩)/√2, and φ=π gives minus.

P(0) = cos²(θ/2); P(1) = sin²(θ/2)

## Axes

The +z and −z directions are |0⟩ and |1⟩. The +x and −x directions are plus and minus. The +y and −y directions are (|0⟩ ± i|1⟩)/√2. These describe the whole state; they are not the real and imaginary axes of an individual amplitude.

S increases φ by π/2 while preserving θ.
