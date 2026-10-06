# Quantum Computing — Learning by Building

A learning journal and hands-on Python practice repository, starting with the mathematics of qubits and building toward a small quantum machine learning experiment.

The goal is to understand why the equations work, implement them with NumPy, predict results, and then test those predictions—not just follow tutorials.

## Current stage

**Lab 1: one-qubit state-vector simulator, Sections 1–3.** Topics discussed: complex amplitudes, normalization, inner products, and the I, X, Z, and H gates. Measurement sampling, multi-qubit systems, and QML are future work.

This repository contains AI-assisted reference code and notes assembled from guided lessons. It is not a claim that every exercise has been independently implemented or that the planned QML project is complete. Practice answers and experiment observations can be added as learning progresses.

## Run locally

Requires Python 3.10 or later. From the repository root:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell with `.venv\Scripts\Activate.ps1`, or on macOS/Linux with `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python labs/lab01_qubit.py
python -m unittest discover -s tests -v
```

The lab prints amplitudes and computational-basis probabilities. These are deterministic calculations, not simulated measurement shots or runs on quantum hardware.

## Contents

| File | Purpose |
| --- | --- |
| [Lab 1](labs/lab01_qubit.py) | Explained NumPy reference implementation |
| [Tests](tests/test_lab01.py) | Check normalization, gates, interference, and invalid inputs |
| [Foundations](notes/01_foundations.md) | Concepts and mathematical reasoning |
| [Practice](exercises/lab01.md) | Predict, run, explain exercises; not yet marked complete |
| [Progress](PROGRESS.md) | Honest record of covered topics and upcoming work |

## Practice workflow

1. Predict the amplitudes before running the code.
2. Run a small experiment and compare the output.
3. Explain any mismatch in your own words.
4. Add a test for the behavior you investigated.
5. Commit the experiment with a meaningful message.

## Longer-term direction

Extend to tensor products, entanglement, sampling, observables, and parameterized circuits. Then investigate a small binary classification problem with classical baselines. A QML experiment should ask a measurable question, not assume quantum advantage.
