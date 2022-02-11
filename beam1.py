# Reference ./beam_example_1.png
# Chapter (2.) Problem 2.3
from beam_analysis import processBeam
import numpy as np


# Node coordinates
nodes = np.array([[0], [4], [6], [11]])


# Member/element connection matrix
members = np.array([[1, 2], [2, 3], [3, 4]])


#   Pre-define arrays to contain each members;
L = []                # length in meters
n = len(nodes)         # number of nodes
m = len(members)       # number of members
E = np.repeat(1, 5)    # Modulus of elasticity kPa
I = np.repeat(1, 5)    # Moment of inertia m^4


# Un-restrained/restrained global degrees of freedom - 1
dgu = np.array([2, 3, 5, 7])
dgr = np.array([0, 1, 4, 6])
fg = np.array([[2, -100]])    # External forces (kN)
ds = np.array([])
Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)
edof = []

# Calling our function
processBeam(n, m, nodes, members, 
        E, I, L, Kg, Kl, fg, dgu, edof)


# Test the output
for i in range(m):
    p = i+1
    v1 = edof[i][0]
    v2 = edof[i][1]
    v3 = edof[i][2]
    v4 = edof[i][3]
    print('\nLocal to global degrees of \nfreedom for member number', p)
    print('[', v1[0], '', v2[0], '', v3[0], '', v4[0], ']')
