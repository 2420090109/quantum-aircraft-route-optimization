from qaoa_model import run_qaoa
from classical_model import run_classical

def main():
    print("Running Classical Optimization...")
    classical_result = run_classical()

    print("Running Quantum Optimization...")
    quantum_result = run_qaoa()

    print("Results:")
    print("Classical:", classical_result)
    print("Quantum:", quantum_result)

if __name__ == "__main__":
    main()
