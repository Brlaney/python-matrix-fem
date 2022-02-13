from math import sin, cos, atan, pi, radians, dist
import numpy as np

def processBeam(n, m, nodes, members, E, I, L, Kg, Kl, fg, dgu, t1, t2):
    '''
      Applies the stiffness method to solve for member end shears (V)
    and member end bending moments (M) along with vertical displacements
    (dy) and rotation angle (dM) at each node.
    '''
    for i in range(m):
        p = i + 1  # actual member number
        newK = np.zeros((2*n, 2*n))

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
        
        # To properly indexing in code:
        prog_row1 = np.array([[dof1-1, dof1-1],[dof1-1, dof2-1],[dof1-1, dof3-1],[dof1-1, dof4-1]])
        prog_row2 = np.array([[dof2-1, dof1-1],[dof2-1, dof2-1],[dof2-1, dof3-1],[dof2-1, dof4-1]])
        prog_row3 = np.array([[dof3-1, dof1-1],[dof3-1, dof2-1],[dof3-1, dof3-1],[dof3-1, dof4-1]])
        prog_row4 = np.array([[dof4-1, dof1-1],[dof4-1, dof2-1],[dof4-1, dof3-1],[dof4-1, dof4-1]])

        x1 = nodes[mn1-1][0]  # node mn1 x1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates

        # Local elem node 1 & 2:
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

        t1.append([act_row1, act_row2, act_row3, act_row4])
        t2.append([prog_row1, prog_row2, prog_row3, prog_row4])
        Kl.append(elemK)
        L.append(l1)
