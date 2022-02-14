# Chapter (2.) Problem 2.3
from lib.trusses import *
import numpy as np


# Node coordinates
nodes = np.array([
    [0, 0],
    [120, 120],
    [240, 0],
    [120, 0]
])

# Member/element connection matrix
members = np.array([
    [1, 2],
    [1, 4],
    [2, 4],
    [2, 3],
    [3, 4]
])

#   Pre-define arrays to contain each members;
L1 = []            # length in inches
L2 = []            # length in feet
orient1 = []       # units: degrees
orient2 = []       # units: radians
n = len(nodes)     # number of nodes
m = len(members)   # number of members
A = np.repeat(2, 5)         # Cross-sectional areas (sq in)
E = np.repeat(29*10**6, 5)  # Modulus of elasticity

# Un-restrained/restrained global degrees of freedom - 1
dgu = np.array([2, 3, 5, 7])
dgf = np.array([0, 0, 1, 1, 0, 0, 1, 1])
fg = np.array([[2, 40], [3, -30]]) # External forces (kips)

Kl = []       # Each elems local [k] (global coords)
Kg = np.zeros((2*n, 2*n))  # global stiffness matrix

processTruss(n, m, nodes, members, E, A, L1,
        L2, orient1, orient2, Kg, Kl, fg, dgf)


print('\n Length in inches')
print(L1)
print('\n Length in feet')
print(L2)
print('\n Angles in degrees')
print(orient1)
print('\n Angles in radians')
print(orient2)


'''
print('\n')
print(Kl)

print('\n')
print(Kl[0])

print('\n')
print(Kl[1])

print('\n')
print(Kl[2])

print('\n')
print(Kl[3])

print('\n')
print(Kl[4])
'''

''' Test the outputs
print('\n Elements lengths (in)')
print(L1)

print('\n Elements lengths (ft)')
print(L2)

print('\n Elements orientation (deg)')
print(orient1)

print('\n Elements orientation (rad)')
print(orient2)

for i in range(5):
    p = i + 1
    print('\n')
    print('[k]el (global coordinates) for element no.:', p)
    print(Kl[i])
'''
