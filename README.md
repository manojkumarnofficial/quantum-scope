# QuantumScope: Quantum State Measurement and Entanglement Simulator

QuantumScope is a Python microproject that simulates quantum gates, superposition, entanglement, measurement probabilities, and quantum state collapse using Qiskit and Qiskit Aer.

## Features

- Demonstrates the Pauli-X, Hadamard, and CNOT gates.
- Prepares and measures a qubit in superposition.
- Creates a two-qubit Bell state to demonstrate entanglement.
- Compares theoretical and simulated measurement probabilities.
- Generates probability comparison graphs.
- Demonstrates repeated measurement and state collapse.

## Requirements

- Python 3.10 or newer is recommended.
- Qiskit
- Qiskit Aer
- NumPy
- Pandas
- Matplotlib

## Installation

Open a terminal in this project folder and run:

```bash
python -m pip install -r requirements.txt
```

## Run the project

```bash
python quantum_scope.py
```

The program prints circuit diagrams and measurement results, and displays graphs for superposition and Bell-state probabilities.

## Experiments

1. **Quantum gates:** X, Hadamard, and CNOT.
2. **Superposition:** measures the state prepared by a Hadamard gate.
3. **Entanglement:** creates and measures a Bell state.
4. **State collapse:** measures the same qubit twice in the computational basis.

## Expected observations

- The X gate changes `|0>` to `|1>`.
- A Hadamard gate applied to `|0>` produces approximately 50% `0` and 50% `1` outcomes over many shots.
- An ideal Bell-state circuit produces `00` and `11` outcomes, each with approximately 50% probability; `01` and `10` should not occur.
- Repeated measurements in the same computational basis should agree.

Counts from the simulator are sampled, so results for probabilistic states can vary slightly from run to run.

## Important note

This project uses a quantum-circuit simulator running on a classical computer. It does not execute on a physical quantum processor. Correlated Bell-state measurement results demonstrate the expected behavior of the simulated circuit; they are not, by themselves, a full experimental proof of entanglement.

## Author

Manoj

## Project type

Quantum Computing Microproject
