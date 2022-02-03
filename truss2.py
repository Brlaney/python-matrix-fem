''' 
Chapter 2.
Problem 2.3
'''
from preprocess import *
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

# Each elements material properties & geometry
E = np.repeat(29*10**6, 5)  # Modulus of elasticity
A = np.repeat(2, 5)         # Cross-sectional areas (sq in)

#   Pre-define arrays to contain each members;
L1 = []            # length in inches
L2 = []            # length in feet
thetas1 = []       # units: degrees
thetas2 = []       # units: radians

n = len(nodes)     # number of nodes
m = len(members)   # number of members
gdof = n * 2       # number of global degrees of freedom

# External forces (lbs) in form: [global dof - 1, (+/-) value]
fg = np.array([
    [2, 40000],
    [3, -30000]
])

# Un-restrained global degrees of freedom - 1
dgu = np.array([2, 3, 6, 7])

# Restrained global degrees of freedom - 1
dgr = np.array([0, 1, 4, 5])

# given displacements:
# dp = np.array([])

Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)


# Calling our function
process(n, m, gdof, nodes, members, E, A, L1,
        L2, thetas1, thetas2, Kg, Kl, fg, dgu)

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
print(thetas1)

print('\n Elements orientation (rad)')
print(thetas2)

for i in range(5):
    p = i + 1
    print('\n')
    print('[k]el (global coordinates) for element no.:', p)
    print(Kl[i])
'''
