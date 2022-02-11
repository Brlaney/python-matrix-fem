# Chapter 2 lesson in textbook
from truss_analysis import *
import numpy as np


# Node coordinates
nodes = np.array([
    [0, 0],
    [120, 120],
    [240, 120],
    [360, 0]
])


# Member connection matrix
members = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
    [2, 4]
])


#   Pre-define arrays to contain each members;
L1 = []            # length in inches
L2 = []            # length in feet
orient1 = []       # units: degrees
orient2 = []       # units: radians
n = len(nodes)     # number of nodes
m = len(members)   # number of members
A = np.repeat(2, m)           # Cross-sectional areas of each element
E = np.repeat(29*10**6, m)    # Modulus of elasticity for each element


# External forces (lbs) in form: [global dof - 1, (+/-) value]
fg = np.array([3, -30000])
# Un-restrained global degrees of freedom - 1
dgu = np.array([2, 3, 4, 5])
# Restrained global degrees of freedom - 1
dgr = np.array([0, 1, 6, 7])
# given displacements:
dp = np.array([ [1, -0.6], [6, -0.3]])


Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)


# Calling our function
processTruss(n, m, nodes, members, E, A, L1,
        L2, orient1, orient2, Kg, Kl, fg, dgu)


print('\n Length in inches')
print(L1)
print('\n Length in feet')
print(L2)
print('\n Angles in degrees')
print(orient1)
print('\n Angles in radians')
print(orient2)


'''
for i in range(5):
    p = i + 1
    print('\n')
    print('[k]el (global coordinates) for element no.:', p)
    print(Kl[i])

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
