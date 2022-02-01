from process import *
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

Kg = np.zeros(())  # global stiffness matrix

process(n, m, gdof, nodes, members, E, A, L1, L2, thetas1, thetas2, Kg)

print('\n Each members length (in.): \n', L1)
print('\n Each members length (ft.): \n', L2)
print('\n Each members theta (deg): \n', thetas1)
print('\n Each members theta (rad): \n', thetas2)
# print(K)

# Global force matrix
fg = np.array([
    [1],
    [1],
    [0],
    [-30000],
    [0],
    [0],
    [1],
    [1]])

# Global displacement matrix
dg = np.array([
    [0],
    [0],
    [1],
    [1],
    [1],
    [1],
    [0],
    [0]])
