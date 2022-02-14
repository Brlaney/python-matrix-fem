# Reference ./beam_example_1.png
# Chapter (2.) Problem 2.3
from lib.beams import processBeam
import numpy as np


# Node coordinates
nodes = np.array([[0], [4], [6], [11]])

# Member/element connection matrix
members = np.array([[1, 2], [2, 3], [3, 4]])

# Pre-define arrays to contain each members
L = []                # length in meters
n = len(nodes)        # number of nodes
m = len(members)      # number of members
E = np.repeat(1, 5)   # Modulus of elasticity kPa
I = np.repeat(1, 5)   # Moment of inertia m^4

Kl = []  # Will contain each elems local [k] (global coords)

# Un-restrained/restrained global_dof-1
dgu = np.array([2, 3, 5, 7])
dgr = np.array([0, 1, 4, 6])
fg = np.array([[2, -100]])     # External forces (kN)
Kg = np.zeros((2*n, 2*n))      # global stiffness matrix
# ds = np.array([])

t1 = []  # Will contain each elements l2g_act
t2 = []  # Will contain each elements l2g_prog

# Calling our function
processBeam(n, m, nodes, members, E, I,
            L, Kg, Kl, fg, dgu, t1, t2)

for i in range(m):
    p = str(i + 1)
    
    filename = 'outputs/beam1/elem' + p + '.csv'
    df = pd.DataFrame(Kl[i])
    df.to_csv(filename, index=True)

'''
print('\nActual index value.')
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

# print(t2)
print('np size:', np.size(t2))
print('np ndim:', np.ndim(t2))
