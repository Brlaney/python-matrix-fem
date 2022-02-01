from assemble import *

# Define empty matrices for:
nodes = []     # Node coordinates
members = []   # Member connection matrix (*see reference 1.)

lengths = []   # Each members length 
angles = []    # Each members angle of orientation (*see reference 2.)

strength = []  # Modulus of elasticity for the material of the member
a = []         # Cross-sectional areas of each member

mtr = 1        # For each member are the material properties: (1.) uniform or (2.) unique

assemble(4, 5, nodes, members, lengths, angles, strength, a, mtr)
