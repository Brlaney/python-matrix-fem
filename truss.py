from preprocess import *
import numpy as np

# Node coordinates
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

E = np.repeat(29*10**6, 5)    # Modulus of elasticity for each element
A = np.repeat(2, 5)           # Cross-sectional areas of each element

#   Pre-define arrays to contain each members;
L1 = []            # length in inches
L2 = []            # length in feet
thetas1 = []       # units: degrees
thetas2 = []       # units: radians

n = len(nodes)     # number of nodes
m = len(members)   # number of members
gdof = n * 2       # number of global degrees of freedom

# External forces (lbs) in form: [global dof - 1, (+/-) value]
fg = np.array([3, -30000])

# Un-restrained global degrees of freedom - 1
dg = np.array([2, 3, 4, 5])

# given displacements:
dp = np.array([
    [1, -0.6],
    [6, -0.3]])

Kg = np.zeros((2*n, 2*n))  # global stiffness matrix

Kl = []  # Will contain each elems local [k] (global coords)

# Calling our function
process(n, m, gdof, nodes, members, E, A, L1,
        L2, thetas1, thetas2, Kg, Kl, fg, dg)

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


row1 = np.array([
    [827140.0624, 84422.84366, -483333.3333, 0],
    [84422.84366, 214114.7864, 0,	0],
    [-483333.3333, 0, 483333.3333, -84422.84366],
    [0,	0, -84422.84366, 214114.7864]
])
'''

'''
kr = np.array([[827140.0624, 84422.84366, -483333.3333, 0],[84422.84366, 214114.7864, 0,	0],[-483333.3333, 0, 483333.3333, -84422.84366],[0,	0, -84422.84366, 214114.7864]])

b = np.array([[0], [-30000], [0], [0]])


linalg.inv(a)

'''
