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

Kg = np.zeros((2*n, 2*n))  # global stiffness matrix

# Calling our function
process(n, m, gdof, nodes, members, E, A, L1, L2, thetas1, thetas2, Kg, fg, dg)

'''
Testing the output of our process function that we 
defined in the preprocess.py script. 
'''
# print('\n Each members length (in.): \n', L1)
# print('\n Each members length (ft.): \n', L2)
# print('\n Each members theta (deg): \n', thetas1)
# print('\n Each members theta (rad): \n', thetas2)
