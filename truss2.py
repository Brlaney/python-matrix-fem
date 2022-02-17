# Chapter (2.) Problem 2.3
# Reference ./truss_example_2.png
from lib.trusses import *
import pandas as pd
import numpy as np

# Node coordinates
nodes = np.array([
    [0, 0],
    [120, 120],
    [240, 0],
    [120, 0]
])

nodes = (1/12) * np.array([[0, 0],[120, 120],[240, 0],[120, 0]])

# Member/element connection matrix
members = np.array([
    [1, 2],
    [1, 4],
    [2, 4],
    [2, 3],
    [3, 4]
])

L1 = []            # length in inches
L2 = []            # length in feet
orient1 = []       # units: degrees
orient2 = []       # units: radians
n = len(nodes)     # number of nodes
m = len(members)   # number of members
A = np.repeat(2, 5)         # Cross-sectional areas (sq in)
E = np.repeat(29*10**6, 5)  # Modulus of elasticity

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 0, 0, 1, 1])
fg = np.array([[2, 40], [3, -30]])   # External forces (kips)

Kl = []   # Each elems local [k] (global coords)
Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
t1 = []
t2 = []

processTruss(n, m, nodes, members, E, A, L1,
        L2, orient1, orient2, Kg, Kl, fg, dgf, t1, t2)

'''
for i in range(m):
    p = str(i + 1)
    
    filename = 'outputs/truss2/elem' + p + '.csv'
    df = pd.DataFrame(Kl[i])
    df.to_csv(filename, index=True)
'''

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
