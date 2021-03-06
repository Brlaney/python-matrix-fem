# beam11.py
# UNITS: METRIC (meters & kN)
from lib.beams import *
import numpy as np

# Node coordinates (modeled with 3 nodes)
nodes = np.array([[0], [6], [11]])

# Member/element connection matrix
members = np.array([[1, 2], [2, 3]])

# Pre-define arrays to contain each members
n = len(nodes)        # number of nodes
m = len(members)      # number of members
L = []                # length in meters
E = np.repeat(1, 2)   # Modulus of elasticity kPa
I = np.repeat(1, 2)   # Moment of inertia m^4

Kl = []  # Will contain each elems local [k] (global coords)

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 0, 1, 0, 1])
fg = np.zeros((2*n))             # External forces (kN)
Kg = np.zeros((2*n, 2*n))        # global stiffness matrix
# ds = np.array([])              # Initial displacements

# fixed-end moment vector for members 1 and 2
fem = np.array([74, -88.9, 75.9, 2.7, 50, -41.7])

newKg = KgBeam(nodes, members, n, m, L, E, I,
            Kl, dgf, fg, Kg, fem)

print('\nLengths')
j = 1
for i in L:
  print(f'Member {j}: {i} (m)')
  j += 1

print('\nGlobal stiffness matrix [K]')
for i in range(len(newKg)):
    print('Row', i + 1, newKg[i])

Kg_inv = np.linalg.inv(newKg)

print('\nReduced global stiffness [K]')
for i in range(len(newKg)):
    print('Row', i + 1, newKg[i])

