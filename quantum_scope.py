# ============================================================
# QuantumScope: Quantum State Measurement and Entanglement Simulator
# Microproject implementation using Qiskit and Qiskit Aer.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

SHOTS = 4000
SEED = 42
simulator = AerSimulator()


def run_circuit(circuit, shots=SHOTS):
    """Run a circuit on Qiskit Aer and return measurement counts."""
    compiled = transpile(circuit, simulator)
    result = simulator.run(
        compiled, shots=shots, seed_simulator=SEED
    ).result()
    return result.get_counts()


def print_section(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


def experiment_quantum_gates():
    """Demonstrate X, Hadamard, and CNOT gates."""
    print_section("EXPERIMENT 1: QUANTUM GATE OPERATIONS")

    x_circuit = QuantumCircuit(1, 1)
    x_circuit.x(0)
    x_circuit.measure(0, 0)

    h_circuit = QuantumCircuit(1, 1)
    h_circuit.h(0)
    h_circuit.measure(0, 0)

    cnot_circuit = QuantumCircuit(2, 2)
    cnot_circuit.x(0)
    cnot_circuit.cx(0, 1)
    cnot_circuit.measure([0, 1], [0, 1])

    for name, circuit in [
        ("X gate", x_circuit),
        ("Hadamard gate", h_circuit),
        ("CNOT gate", cnot_circuit),
    ]:
        print(f"\n{name} circuit:")
        print(circuit.draw(output="text"))
        print("Measurement counts:", run_circuit(circuit))


def experiment_superposition():
    """Prepare |+> and compare theoretical and measured probabilities."""
    print_section("EXPERIMENT 2: QUANTUM SUPERPOSITION")

    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    print("Circuit before measurement:")
    print(circuit.draw(output="text"))
    circuit.measure(0, 0)

    counts = run_circuit(circuit)
    p0 = counts.get("0", 0) / SHOTS
    p1 = counts.get("1", 0) / SHOTS

    print("Measurement counts:", counts)
    print(f"P(0): {p0:.4f} ({p0 * 100:.2f}%)")
    print(f"P(1): {p1:.4f} ({p1 * 100:.2f}%)")
    print("Theoretical probabilities: P(0) = 0.5, P(1) = 0.5")

    x = np.arange(2)
    width = 0.35
    plt.figure(figsize=(8, 5))
    plt.bar(x - width / 2, [0.5, 0.5], width, label="Theoretical")
    plt.bar(x + width / 2, [p0, p1], width, label="Simulated")
    plt.xticks(x, ["|0>", "|1>"])
    plt.ylabel("Measurement probability")
    plt.ylim(0, 1)
    plt.title("Superposition: Theoretical vs Simulated")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    return p0, p1


def experiment_entanglement():
    """Create and measure a two-qubit Bell state."""
    print_section("EXPERIMENT 3: QUANTUM ENTANGLEMENT (BELL STATE)")

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)

    print("Bell-state circuit before measurement:")
    print(circuit.draw(output="text"))

    circuit.measure([0, 1], [0, 1])
    counts = run_circuit(circuit)
    probabilities = {
        outcome: counts.get(outcome, 0) / SHOTS
        for outcome in ["00", "01", "10", "11"]
    }

    print("Measurement counts:", counts)
    for outcome, probability in probabilities.items():
        print(f"P({outcome}): {probability:.4f}")

    print("Theoretical probabilities: P(00) = 0.5, P(11) = 0.5; "
          "P(01) = P(10) = 0.")

    x = np.arange(4)
    width = 0.35
    theoretical = [0.5, 0.0, 0.0, 0.5]
    measured = [probabilities[o] for o in ["00", "01", "10", "11"]]

    plt.figure(figsize=(8, 5))
    plt.bar(x - width / 2, theoretical, width, label="Theoretical")
    plt.bar(x + width / 2, measured, width, label="Simulated")
    plt.xticks(x, ["00", "01", "10", "11"])
    plt.ylabel("Measurement probability")
    plt.ylim(0, 1)
    plt.title("Bell State: Theoretical vs Simulated")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    return counts


def experiment_state_collapse():
    """Measure the same qubit twice in the computational basis."""
    print_section("EXPERIMENT 4: MEASUREMENT AND STATE COLLAPSE")

    circuit = QuantumCircuit(1, 2)
    circuit.h(0)
    circuit.measure(0, 0)
    circuit.measure(0, 1)

    print("Repeated-measurement circuit:")
    print(circuit.draw(output="text"))

    counts = run_circuit(circuit)
    print("Two-measurement outcomes:", counts)

    # Classical bits are displayed as c1c0, so 00 and 11 indicate agreement.
    mismatches = counts.get("01", 0) + counts.get("10", 0)
    if mismatches == 0:
        print("Result: Both measurements agree in every simulated shot.")
        print("Conclusion: The first measurement collapses the qubit "
              "to a computational-basis state.")
    else:
        print("Unexpected mismatch detected; inspect the circuit.")


def main():
    print_section("QUANTUMSCOPE: QUANTUM STATE MEASUREMENT ANALYSIS")
    print(f"Simulator: Qiskit Aer | Shots per experiment: {SHOTS}")
    experiment_quantum_gates()
    experiment_superposition()
    experiment_entanglement()
    experiment_state_collapse()
    print_section("PROJECT COMPLETED")
    print("Demonstrated: quantum gates, superposition, Bell-state "
          "entanglement, measurement probabilities, graphs, and state collapse.")
    print("Note: This is a simulation on a classical computer, not a "
          "physical quantum processor.")


if __name__ == "__main__":
    main()
