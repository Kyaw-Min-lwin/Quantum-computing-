"""Run from the repository root: python -m unittest discover -s tests -v."""

import unittest
import numpy as np
from labs.lab01_qubit import (
    ZERO, ONE, PLUS, MINUS, I, X, Z, H,
    normalize, is_normalized, probabilities, is_unitary, apply_gate,
)


class QubitTests(unittest.TestCase):
    def test_basis_and_superpositions_are_normalized(self):
        for state in (ZERO, ONE, PLUS, MINUS):
            self.assertTrue(is_normalized(state))

    def test_complex_probabilities(self):
        psi = np.array([np.sqrt(3) / 2, 1j / 2])
        np.testing.assert_allclose(probabilities(psi), [0.75, 0.25])

    def test_normalization_preserves_direction(self):
        np.testing.assert_allclose(normalize([1, 1j]), normalize([2, 2j]))
        np.testing.assert_allclose(normalize([3, 4]), [0.6, 0.8])

    def test_tiny_nonzero_vector_can_be_normalized(self):
        np.testing.assert_allclose(normalize([1e-200, 0]), ZERO)

    def test_invalid_states(self):
        for state in ([0, 0], [np.nan, 0], [np.inf, 1], [1, 0, 0]):
            with self.assertRaises(ValueError):
                normalize(state)
        with self.assertRaises(ValueError):
            probabilities([1, 1])

    def test_gates_are_unitary(self):
        for gate in (I, X, Z, H):
            self.assertTrue(is_unitary(gate))
        self.assertFalse(is_unitary(2 * I))
        self.assertFalse(is_unitary(np.ones((2, 3))))

    def test_basis_mappings(self):
        for gate, before, after in (
            (X, ZERO, ONE), (X, ONE, ZERO), (Z, PLUS, MINUS),
            (H, ZERO, PLUS), (H, ONE, MINUS),
            (H, PLUS, ZERO), (H, MINUS, ONE),
        ):
            np.testing.assert_allclose(apply_gate(gate, before), after, atol=1e-10)

    def test_phase_changes_can_preserve_probabilities(self):
        np.testing.assert_allclose(probabilities(PLUS), probabilities(Z @ PLUS))
        self.assertFalse(np.allclose(PLUS, Z @ PLUS))

    def test_interference(self):
        np.testing.assert_allclose(H @ Z @ H @ ZERO, ONE, atol=1e-10)
        np.testing.assert_allclose(H @ H @ ZERO, ZERO, atol=1e-10)

    def test_gate_validation_and_input_preservation(self):
        original = PLUS.copy()
        apply_gate(H, original)
        np.testing.assert_array_equal(original, PLUS)
        with self.assertRaises(ValueError):
            apply_gate(2 * I, ZERO)
        with self.assertRaises(ValueError):
            apply_gate(H, [1, 1])


if __name__ == "__main__":
    unittest.main()
