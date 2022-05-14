# truss1.py
from lib.trusses import *
import numpy as np

# Node coordinates (in)
nodes = np.array([
    [0, 0],
    [120, 120],
    [240, 120],
    [360, 0]])

# Member connection matrix
members = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
    [2, 4]])

L1 = []                      # length in inches
L2 = []                      # length in feet
a1 = []                      # units: degrees
a2 = []                      # units: radians
n = len(nodes)               # number of nodes
m = len(members)             # number of members
A = np.repeat(2, m)          # Cross-sectional areas of each element
E = np.repeat(29*10**6, m)   # Modulus of elasticity for each element

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 1, 1, 0, 0])

# External forces (lbs)
fg = np.array([2, -30000])

# Unknown global forces
fu = np.array([0, 1, 6, 7])

# given displacements
dp = np.array([[1, -0.6], [6, -0.3]])

Kl = []  # Each elems local [k] (global coords)
Kg = np.zeros((2*n, 2*n))  # global stiffness matrix

newKg = KgTruss(n, m, nodes, members, E, A, L1,
        L2, a1, a2, Kg, Kl, fg, dgf)

print('\nLengths (in)')
print(L1)
print('\nLengths (ft)')
print(L2)
print('\nAngles (degrees)')
print(a1)
print('\nAngles (radians)')
print(a2)

print('\nGlobal stiffness matrix [K]')
for i in range(len(newKg)):
    print('Row', i + 1, newKg[i])
