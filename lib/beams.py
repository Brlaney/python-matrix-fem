# lib/beams.py
from math import sin, cos, atan, pi, radians, dist
import numpy as np


# Assembles the global stiffness matrix [K]g for the given beam system.
def KgBeam(nodes, members, n, m, L, E, I, Kl, dgf, fg, Kg, fem):
    for i in range(m):
        newK = np.zeros((2*n, 2*n))
        p = i + 1

        # For member number: i, map nodes: mn1 --> mn2
        mn1 = members[i][0]
        mn2 = members[i][1]

        dof1 = 2*mn1-1     # Local dof1 --> global value(dof1)
        dof2 = 2*mn1       # Local dof2 --> global value(dof2)
        dof3 = 2*mn2-1     # Local dof3 --> global value(dof3)
        dof4 = 2*mn2       # Local dof4 --> global value(dof4)

        # The actual global dof's index:
        act_row1 = np.array([[dof1, dof1],[dof1, dof2],[dof1, dof3],[dof1, dof4]])
        act_row2 = np.array([[dof2, dof1],[dof2, dof2],[dof2, dof3],[dof2, dof4]])
        act_row3 = np.array([[dof3, dof1],[dof3, dof2],[dof3, dof3],[dof3, dof4]])
        act_row4 = np.array([[dof4, dof1],[dof4, dof2],[dof4, dof3],[dof4, dof4]])
        
        b = np.array([[1,1], [1,1], [1,1], [1,1]])

        # To properly index in code:
        prog_row1 = act_row1 - b
        prog_row2 = act_row2 - b
        prog_row3 = act_row3 - b
        prog_row4 = act_row4 - b

        x1 = nodes[mn1-1][0]  # node mn1 x1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates

        # Local elem node 1 & 2:
        # Beams have a y-coordinate of 0 
        n1 = (x1, 0)  
        n2 = (x2, 0)

        l1 = dist(n1, n2)
        c = 2*E[i]*I[i] / l1**3

        elemK = c * np.array([
            [6, -3*l1, -6, -3*l1],
            [-3*l1, 2*l1**2, 3*l1, l1**2],
            [-6, 3*l1, 6, 3*l1],
            [-3*l1, l1**2, 3*l1, 2*l1**2]
        ])

        # Row 1        
        j_11 = prog_row1[0][0]
        k_11 = prog_row1[0][1]
        
        j_12 = prog_row1[1][0]
        k_12 = prog_row1[1][1]
        
        j_13 = prog_row1[2][0]
        k_13 = prog_row1[2][1]
        
        j_14 = prog_row1[3][0]
        k_14 = prog_row1[3][1]
        
        newK[j_11][k_11] = elemK[0][0]
        newK[j_12][k_12] = elemK[0][1]
        newK[j_13][k_13] = elemK[0][2]
        newK[j_14][k_14] = elemK[0][3]

        # Row 2 
        j_21 = prog_row2[0][0]
        k_21 = prog_row2[0][1]

        j_22 = prog_row2[1][0]
        k_22 = prog_row2[1][1]

        j_23 = prog_row2[2][0]
        k_23 = prog_row2[2][1]

        j_24 = prog_row2[3][0]
        k_24 = prog_row2[3][1]
        
        newK[j_21][k_21] = elemK[1][0]
        newK[j_22][k_22] = elemK[1][1]
        newK[j_23][k_23] = elemK[1][2]
        newK[j_24][k_24] = elemK[1][3]

        # Row 3       
        j_31 = prog_row3[0][0]
        k_31 = prog_row3[0][1]

        j_32 = prog_row3[1][0]
        k_32 = prog_row3[1][1]

        j_33 = prog_row3[2][0]
        k_33 = prog_row3[2][1]

        j_34 = prog_row3[3][0]
        k_34 = prog_row3[3][1]
        
        newK[j_31][k_31] = elemK[2][0]
        newK[j_32][k_32] = elemK[2][1]
        newK[j_33][k_33] = elemK[2][2]
        newK[j_34][k_34] = elemK[2][3]

        # Row 4
        j_41 = prog_row4[0][0]
        k_41 = prog_row4[0][1]

        j_42 = prog_row4[1][0]
        k_42 = prog_row4[1][1]

        j_43 = prog_row4[2][0]
        k_43 = prog_row4[2][1]

        j_44 = prog_row4[3][0]
        k_44 = prog_row4[3][1]
        
        newK[j_41][k_41] = elemK[3][0]
        newK[j_42][k_42] = elemK[3][1]
        newK[j_43][k_43] = elemK[3][2]
        newK[j_44][k_44] = elemK[3][3]
        
        Kg_2 = np.copy(Kg) # Copy of Kg thus far
        Kg = Kg_2 + newK   # Add the newK to Kg
        
        # Round lengths only after using to calculate [K] matrix
        l1 = round(l1, 1)

        Kl.append(elemK)
        L.append(l1)

    # Only copy the return value Kg IF 
    # the for loop above has finished.
    newKg = np.copy(Kg)
    newKg = np.round(newKg, 4)

    return newKg
