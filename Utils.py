import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import random
from pylab import *
from scipy.interpolate import CubicSpline, splev, splrep
import math


from qiskit.aqua import run_algorithm
from qiskit.aqua.input import LinearSystemInput
from qiskit.quantum_info import state_fidelity
from qiskit.aqua.algorithms.classical import ExactLSsolver
from qiskit.quantum_info import state_fidelity
from qiskit import BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms.single_sample import HHL
from qiskit.aqua.utils import random_hermitian
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import IBMQ, Aer, BasicAer, execute


import matplotlib.artist as artists
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import math


def normalize_custom(x, C =1):
    M = x[0] ** 2 + x[1] ** 2
    x_normed = [
        1 / np.sqrt(M * C) * complex(x[0], 0),  # 00
        1 / np.sqrt(M * C) * complex(x[1], 0),  # 01
    ]
    return x_normed

def fidelity(hhl, ref):
    solution_hhl_normed = hhl / np.linalg.norm(hhl)
    solution_ref_normed = ref / np.linalg.norm(ref)
    fidelity = state_fidelity(solution_hhl_normed, solution_ref_normed)
    print("fidelity %f" % fidelity)
    return fidelity




params = {
    'problem': {'name': 'linear_system'},
    'algorithm': {'name': 'HHL'},
    'eigs': {'expansion_mode': 'suzuki',
             'expansion_order': 2,
             'name': 'EigsQPE',
             'num_ancillae': 3,
             'num_time_slices': 50 },
    'reciprocal': { 'name': 'Lookup'},
    'backend': { 'provider': 'qiskit.BasicAer',
                 'name': 'statevector_simulator'}
}

def cube_data(x):
    return pd.Series([1, x, x**2, x**3])


def lin_data(x):
    return pd.Series([1, x])

def quad_data(x):
    return pd.Series([1, x, x**2])


def dot_product(x, weights):
    # Quantum Circuit for Cosine-distance classifier
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    c = ClassicalRegister(1)
    ancilla = QuantumRegister(1, 'd')

    beta = QuantumRegister(1, 'beta')
    data = QuantumRegister(1, 'data')

    qc = QuantumCircuit(beta, data, ancilla, c)

    q = normalize_custom(weights)
    x = normalize_custom(x)
    qc.initialize(q, [beta])
    qc.initialize(x, [data])
    qc.barrier()

    qc.h(ancilla)
    qc.cswap(ancilla, data, beta)
    qc.h(ancilla)
    qc.barrier()

    qc.measure(ancilla, c)
    # print(qc)

    # QASM Simulation
    sim_backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, sim_backend, shots=8192)
    results = job.result()
    answer = results.get_counts(qc)
    print(answer)

    if len(answer) == 1:
        quantum_prob = 1
    else:
        quantum_prob = answer['0'] / (answer['0'] + answer['1'])

    P0 = quantum_prob

    return np.sqrt(2 * (P0 - 1 / 2))
