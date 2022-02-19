# Chapter (2.) Problem 2.3
# Reference beam_example_1.png
from lib.beams import *
import pandas as pd
import numpy as np


# Node coordinates (modeled with 4 nodes)
nodes = np.array([[0], [4], [6], [11]])

# Member/element connection matrix
members = np.array([[1, 2], [2, 3], [3, 4]])

# Pre-define arrays to contain each members
n = len(nodes)        # number of nodes
m = len(members)      # number of members
L = []                # length in meters
E = np.repeat(1, 5)   # Modulus of elasticity kPa
I = np.repeat(1, 5)   # Moment of inertia m^4

Kl = []  # Will contain each elems local [k] (global coords)

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 0, 1, 0, 1])
fg = np.array([[2, -100]])     # External forces (kN)
Kg = np.zeros((2*n, 2*n))      # global stiffness matrix
# ds = np.array([])              # Initial displacements

# fixed-end moment vector for members 1 and 2
fem = np.array([0, 0, 0, 0, 0, 0])

t1 = []  # Will contain each elements l2g_act
t2 = []  # Will contain each elements l2g_prog


newKg = KgBeam(nodes, members, n, m, L, E, I,
            Kl, dgf, fg, Kg, fem, t1, t2)

print(newKg)
