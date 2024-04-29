import qiskit
from qiskit import QuantumRegister
from qiskit.circuit import QuantumCircuit
import pylatexenc
import numpy as np
import matplotlib.pyplot as plt

qc = qiskit.QuantumCircuit(2, name='ekin')
qc.x(0)
qc.y(0)
qc.z(0)
qc.cx(0, 1)
qc.draw('mpl')
plt.show()
