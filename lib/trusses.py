# lib/trusses.py
from math import sin, cos, atan, pi, radians, dist
import numpy as np

# First 4 cases: Quad-IV, III, II, & I
# Last 4 cases:  theta = 0, 90, 180, 270
def calc_theta(dx, dy):
    if dx > 0 and dy < 0: a1 = 360+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy < 0: a1 = 270+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy > 0: a1 = 180+atan(dy/dx)*(180/pi)
    elif dx > 0 and dy > 0: a1 = atan(dy/dx)*(180/pi)
    elif dx > 0 and dy == 0: a1 = 0
    elif dx == 0 and dy > 0: a1 = 90
    elif dx < 0 and dy == 0: a1 = 180
    elif dx == 0 and dy < 0: a1 = 270
    else: print('An error has occured. The system does not match any case.')
    
    a2 = round(radians(a1), 2)  # Convert from deg to rad
    a1 = round(a1, 1)
    return [a1, a2]


# Assembles the actual global dof's index matrix
def global_dofs(mn1, mn2):
    dof1 = 2*mn1-1
    dof2 = 2*mn1
    dof3 = 2*mn2-1
    dof4 = 2*mn2

    # The actual global dof's index:
    act_row1 = np.array([[dof1, dof1],[dof1, dof2],[dof1, dof3],[dof1, dof4]])
    act_row2 = np.array([[dof2, dof1],[dof2, dof2],[dof2, dof3],[dof2, dof4]])
    act_row3 = np.array([[dof3, dof1],[dof3, dof2],[dof3, dof3],[dof3, dof4]])
    act_row4 = np.array([[dof4, dof1],[dof4, dof2],[dof4, dof3],[dof4, dof4]])
    b = np.array([-1,-1])
    
    # To properly index in code:
    prog_row1 = act_row1 + b
    prog_row2 = act_row2 + b
    prog_row3 = act_row3 + b
    prog_row4 = act_row4 + b
    
    kij = np.array([prog_row1, prog_row2, prog_row3, prog_row4])
    return kij


# The following for loop iterates for however 
# many members are defined in the given system.
def KgTruss(n, m, nodes, members, E, A, L1, L2, a1, a2, Kg, Kl, fg, dgf):
    for i in range(m):
        p = i + 1    # Unique key id (starts at 1)
        newK = np.zeros((2*n, 2*n))

        # For member number: i, map nodes: mn1 --> mn2
        mn1 = members[i][0]
        mn2 = members[i][1]

        kij = global_dofs(mn1, mn2)
        
        # Local elem n1 & n2 coordinates
        n1 = (nodes[mn1-1][0], nodes[mn1-1][1])  
        n2 = (nodes[mn2-1][0], nodes[mn2-1][1])  
       
        dx = n2[0]-n1[0]  # delta_x
        dy = n2[1]-n1[1]  # delta_y
        
        l1 = dist(n1, n2)   # Length (in)
        l2 = l1/12          # Length (ft)

        angles = calc_theta(dx, dy)

        theta1 = angles[0]   # radians
        theta2 = angles[1]   # degrees
        cs = cos(theta2)
        sn = sin(theta2)

        c = (E[i]*A[i])/l1

        elemK = c*np.array([
            [cs**2, cs*sn, -cs**2, -sn**2],
            [cs*sn, sn**2, -cs*sn, -sn**2],
            [-cs**2, -cs*sn, cs**2, cs*sn],
            [-cs*sn, -sn**2, cs*sn, sn**2]
        ])
        
        # Maps local to global
        for i in range(len(kij)):
            newK[kij[i][0][0]][kij[i][0][1]] = elemK[i][0]
            newK[kij[i][1][0]][kij[i][1][1]] = elemK[i][1]
            newK[kij[i][2][0]][kij[i][2][1]] = elemK[i][2]
            newK[kij[i][3][0]][kij[i][3][1]] = elemK[i][3]
        
        Kg_2 = np.copy(Kg) # Copy of Kg thus far
        Kg = Kg_2 + newK   # Add the newK to Kg
        
        # Round lengths only after using to calculate [K] matrix
        l1 = round(l1, 1)
        l2 = round(l2, 1)
        L1.append(l1)
        L2.append(l2)
        a1.append(theta1)
        a2.append(theta2)
        Kl.append(elemK)
        
    newKg = np.copy(Kg)
    newKg = np.round(newKg)
    return newKg


'''
If m = 0 then dgf --> x-axis
If m = 1 then dgf --> y-axis
m = i % 2
def KgReduce(dgf, newKg):
    n = len(dgf[np.where(dgf == 0)])
    idxs = np.where(dgf == 0)

    for i in range(n - 1):
        idx = idxs[0][i]
    
        newKg = np.delete(newKg, idx, axis=[0,1])

    return newKg
'''
