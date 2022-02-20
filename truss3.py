# truss example 3
# import pandas as pd
from lib.trusses import *
import numpy as np
import time

start_time = time.time() # Starting time

# Node coordinates
nodes = np.array([
    [0, 0],
    [240, 480],
    [480, 0],
    [240, 180]])

# Member connection matrix
members = np.array([
    [1, 2],
    [1, 4],
    [1, 3],
    [4, 2],
    [2, 3],
    [4, 3]])

L1 = []                       # length in inches
L2 = []                       # length in feet
a1 = []                       # units: degrees
a2 = []                       # units: radians
n = len(nodes)                # number of nodes
m = len(members)              # number of members
A = np.repeat(1, m)           # Cross-sectional areas of each element
E = np.repeat(1, m)           # Modulus of elasticity for each element

# External forces (lbs) in form: [global dof - 1, (+/-) value]
fg = np.array([[2,-50], [3,25]])

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0,0,1,1,1,0,1,1])
dp = np.array([[0,-0.01], [1,-0.025]])  # given displacements (in)
Kg = np.zeros((2*n,2*n))  # global stiffness matrix
Kl = []  # Will contain each elems local [k] (global coords)


newKg = KgTruss(n, m, nodes, members, E, A, L1,
        L2, a1, a2, Kg, Kl, fg, dgf)


print('\nLength in inches')
print(L1)
print('\nLength in feet')
print(L2)
print('\nAngles in degrees')
print(a1)
print('\nAngles in radians')
print(a2)

print('\nGlobal stiffness matrix')
print(newKg)

end_time = time.time() # End time when code finishes
final_time = end_time - start_time
final_r = round(final_time, 7)
print('\nTime elapsed:', final_r)
