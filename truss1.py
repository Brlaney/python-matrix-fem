# Chapter 2 lesson in textbook
# Reference ./truss_example_1.png
from lib.trusses import *
import pandas as pd
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
# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 1, 1, 0, 0])
# given displacements:
dp = np.array([ [1, -0.6], [6, -0.3]])

Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)
t1 = []
t2 = []

# Calling our function
processTruss(n, m, nodes, members, E, A, L1,
        L2, orient1, orient2, Kg, Kl, fg, dgf, t1, t2)

'''
for i in range(m):
    p = str(i + 1)
    
    filename = 'outputs/truss1/elem' + p + '.csv'
    df = pd.DataFrame(Kl[i])
    df.to_csv(filename, index=True)

print('\nMatrix [Kl]g: \n')
print(Kl)

print('\nLength of [Kl]g:', len(Kl))

print('\n Length (in)')
print(L1)
print('\n Length (ft)')
print(L2)

print('\n Angles (degrees)')
print(orient1)
print('\n Angles (radians)')
print(orient2)

print('\nSize of t1 & t2:', np.size(t1))

print('\nActual index values for each \nmember are displayed below.')
for i in range(m):
    p = i+1

    v1 = t1[i][0][0]
    v2 = t1[i][0][1]
    v3 = t1[i][0][2]
    v4 = t1[i][0][3]
    v5 = t1[i][1][0]
    v6 = t1[i][1][1]
    v7 = t1[i][1][2]
    v8 = t1[i][1][3]
    v9 = t1[i][2][0]
    v10 = t1[i][2][1]
    v11 = t1[i][2][2]
    v12 = t1[i][2][3]
    v13 = t1[i][3][0]
    v14 = t1[i][3][1]
    v15 = t1[i][3][2]
    v16 = t1[i][3][3]

    print('\nLocal to global degrees of \nfreedom for member number', p)
    print('Row 1: [', v1, '', v2, '', v3, '', v4, ']')
    print('Row 2: [', v5, '', v6, '', v7, '', v8, ']')
    print('Row 3: [', v9, '', v10, '', v11, '', v12, ']')
    print('Row 4: [', v13, '', v14, '', v15, '', v16, ']')

print('\nIndexing in code value.')
for i in range(m):
    p = i+1

    v1 = t2[i][0][0]
    v2 = t2[i][0][1]
    v3 = t2[i][0][2]
    v4 = t2[i][0][3]
    v5 = t2[i][1][0]
    v6 = t2[i][1][1]
    v7 = t2[i][1][2]
    v8 = t2[i][1][3]
    v9 = t2[i][2][0]
    v10 = t2[i][2][1]
    v11 = t2[i][2][2]
    v12 = t2[i][2][3]
    v13 = t2[i][3][0]
    v14 = t2[i][3][1]
    v15 = t2[i][3][2]
    v16 = t2[i][3][3]

    print('\nLocal to global degrees of \nfreedom for member number', p)
    print('Row 1: [', v1, '', v2, '', v3, '', v4, ']')
    print('Row 2: [', v5, '', v6, '', v7, '', v8, ']')
    print('Row 3: [', v9, '', v10, '', v11, '', v12, ']')
    print('Row 4: [', v13, '', v14, '', v15, '', v16, ']')
'''
