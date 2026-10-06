"""Lab 1 reference: pure one-qubit states and closed-system gates.

Arrays store amplitudes, not probabilities. This is a classical simulation.
No measurement sampling or post-measurement state update is implemented yet.
"""

import numpy as np

ATOL = 1e-10

ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)
PLUS = (ZERO + ONE) / np.sqrt(2)
MINUS = (ZERO - ONE) / np.sqrt(2)

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


def as_qubit(state):
    """Accept two finite complex amplitudes; normalization is a separate check."""
    state = np.asarray(state, dtype=complex)
    if state.shape != (2,) or not np.all(np.isfinite(state)):
        raise ValueError("Expected two finite amplitudes with shape (2,).")
    return state


def is_normalized(state):
    """The squared norm is total computational-basis probability."""
    state = as_qubit(state)
    return bool(np.isclose(np.vdot(state, state), 1, atol=ATOL, rtol=0))


def normalize(state):
    """Scale a nonzero vector to length one, keeping its amplitude ratios.

    Scaling first avoids overflow/underflow for very large/small inputs.
    This is a mathematical preparation helper, not a physical quantum gate.
    """
    state = as_qubit(state)
    scale = max(np.max(np.abs(state.real)), np.max(np.abs(state.imag)))
    if scale == 0:
        raise ValueError("The zero vector cannot be normalized.")
    scaled = state / scale
    return scaled / np.linalg.norm(scaled)


def probabilities(state):
    """Return [P(0), P(1)] without sampling or changing the input state."""
    state = as_qubit(state)
    if not is_normalized(state):
        raise ValueError("Normalize the state before calculating probabilities.")
    # abs computes magnitude; ** 2 then squares that real magnitude.
    return np.abs(state) ** 2


def is_unitary(gate):
    """Check U-dagger U = I for a finite one-qubit gate."""
    gate = np.asarray(gate, dtype=complex)
    if gate.shape != (2, 2) or not np.all(np.isfinite(gate)):
        return False
    return bool(np.allclose(gate.conj().T @ gate, I, atol=ATOL, rtol=0))


def apply_gate(gate, state):
    """Apply a unitary to a normalized qubit; return a new array.

    Do not silently renormalize: that could hide an invalid gate or state.
    """
    state = as_qubit(state)
    gate = np.asarray(gate, dtype=complex)
    if not is_normalized(state):
        raise ValueError("The input state must be normalized.")
    if not is_unitary(gate):
        raise ValueError("Expected a unitary gate with shape (2, 2).")
    return gate @ state


def main():
    np.set_printoptions(precision=6, suppress=True)
    psi = np.array([np.sqrt(3) / 2, 1j / 2], dtype=complex)
    print("psi amplitudes:", psi)
    print("psi probabilities:", probabilities(psi))
    print("<psi|psi>:", np.vdot(psi, psi))
    print("normalized [3, 4]:", normalize([3, 4]))

    for name, gate in [("I", I), ("X", X), ("Z", Z), ("H", H)]:
        print(f"{name} is unitary:", is_unitary(gate))

    # Chronological order: H, then Z, then H. No intermediate measurement.
    state = ZERO.copy()
    for name, gate in [("H", H), ("Z", Z), ("H", H)]:
        state = apply_gate(gate, state)
        print(f"After {name}: amplitudes={state}, probabilities={probabilities(state)}")
    print("Final vector equals |1>:", np.allclose(state, ONE))


if __name__ == "__main__":
    main()
