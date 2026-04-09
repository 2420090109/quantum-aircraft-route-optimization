from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit_optimization.applications import Maxcut
from qiskit_optimization.algorithms import MinimumEigenOptimizer
import networkx as nx

def run_qaoa():
    graph = nx.Graph()
    graph.add_edges_from([(0,1),(1,2),(2,3),(3,0)])

    maxcut = Maxcut(graph)
    qp = maxcut.to_quadratic_program()

    backend = Aer.get_backend('aer_simulator')
    qaoa = QAOA(reps=1, quantum_instance=backend)

    optimizer = MinimumEigenOptimizer(qaoa)
    result = optimizer.solve(qp)

    return result.fval
