# Reference ./beam_example_1.png
# Chapter (2.) Problem 2.3
from beam_analysis import processBeam
import numpy as np


# Node coordinates
nodes = np.array([[0], [4], [6], [11]])


# Member/element connection matrix
members = np.array([[1, 2], [2, 3], [3, 4]])


#   Pre-define arrays to contain each members;
L1 = []            # length in inches
L2 = []            # length in feet
n = len(nodes)     # number of nodes
m = len(members)   # number of members
E = np.repeat(1, 5)    # Modulus of elasticity lbs/in^2 (psi)
I = np.repeat(1, 5)    # Moment of inertia in^4


# External forces (lbs) in form: [global dof - 1, (+/-) value]
fg = np.array([
    [2, 40000],
    [3, -30000]
])


# Un-restrained/restrained global degrees of freedom - 1
dgu = np.array([2, 3, 5, 7])
dgr = np.array([0, 1, 4, 6])
fg = np.array([[2, -100]])    # External forces (kN)
ds = np.array([])


Kg = np.zeros((2*n, 2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)


# Calling our function
processBeam(n, m, nodes, members, 
        E, I, L1, Kg, Kl, fg, dgu)


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
print('\n Elements lengths (meters)')
print(L)


for i in range(5):
    p = i + 1
    print('\n')
    print('[k]el (global coordinates) for element no.:', p)
    print(Kl[i])
'''

