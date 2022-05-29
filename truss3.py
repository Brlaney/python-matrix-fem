# truss3.py
from lib.trusses import *
import numpy as np

# Node coordinates (in)
nodes = np.array([
    [0, 0],
    [240, 480],
    [480, 0],
    [240, 180]])

# Member connections
members = np.array([
    [1, 2],
    [1, 4],
    [1, 3],
    [4, 2],
    [2, 3],
    [4, 3]])

L1 = []                     # length in inches
L2 = []                     # length in feet
a1 = []                     # units: degrees
a2 = []                     # units: radians
n = len(nodes)              # number of nodes
m = len(members)            # number of members
A = np.repeat(1, m)         # Cross-sectional areas (sq in)
E = np.repeat(1, m)         # Modulus of elasticity

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 1, 0, 1, 1])

# External forces (lbs)
fg = np.array([[2, -50], [3, 25]])

# Given displacements (in)
dp = np.array([[0, -0.01], [1, -0.025]])

# Global stiffness matrix
Kg = np.zeros((2*n, 2*n))  

# Used for each elems local [k] (global coords)
Kl = []  

newKg = KgTruss(n, m, nodes, members, E, A, L1,
        L2, a1, a2, Kg, Kl, fg, dgf)

print('\nLengths (in)\n', L1)
print('\nLengths (ft)\n', L2)
print('\nAngles (degrees)\n', a1)
print('\nAngles (radians)\n', a2)

print('\nGlobal stiffness matrix [K]')
for i in range(len(newKg)):
    print('Row', i + 1, newKg[i])

count = np.count_nonzero(dgf == 1)
print(f'\nNumber of un-restrained global dofs: {count}')

print(newKg)
