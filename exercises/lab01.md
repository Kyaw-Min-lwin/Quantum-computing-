# Lab 1 — independent practice

Status: pending. The supplied lab is an AI-assisted reference. Add your own predictions, code experiments, and explanations here or in a new practice script.

## A. Represent and normalize

1. Build [1/2, i sqrt(3)/2] using NumPy. Predict the probabilities and verify them.
2. Compare `state ** 2` with `np.abs(state) ** 2`. Explain why only one gives probabilities.
3. Normalize [1, i] and [2, 2i]. Explain why the normalized arrays agree.
4. Try normalizing [0, 0]. Explain the exception rather than removing the check.

## B. Gates

1. Predict X applied to [1/2, i sqrt(3)/2]. Run it and explain both output entries.
2. Apply Z to [sqrt(3)/2, 1/2]. Compare the amplitudes and probabilities before and after.
3. Explain H's two output amplitudes as sums of contributions from the input basis states.
4. Track |0⟩ through H, then Z, then H without measuring between gates. Explain which contributions cancel at the final H.
5. Explain why U†U = I preserves normalization. Add a test using a complex input state.

## C. Debugging

1. Remove the 1/sqrt(2) factor from H in a separate experiment. What does the unitarity check report, and why?
2. Compare `H @ PLUS` and `H * PLUS`, including the shapes. Why is the latter not a qubit state?
3. Does `np.allclose(Z @ ONE, ONE)` establish physical equivalence? Explain the role of global phase.

## Record results

For each experiment: prediction → actual output → explanation → remaining question.
Do not tick the progress checklist simply because the reference code runs.
