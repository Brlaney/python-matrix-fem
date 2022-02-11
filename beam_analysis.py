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

        loc1 = 2 * mn1 - 1    # Local dof1 --> global value(loc1)
        loc2 = 2 * mn1        # Local dof2 --> global value(loc2)
        loc3 = 2 * mn2 - 1    # Local dof3 --> global value(loc3)
        loc4 = 2 * mn2        # Local dof4 --> global value(loc4)

        # The actual global dof's index:
        l2g_act_row1 = np.array([[loc1, loc1],[loc1, loc2],[loc1, loc3],[loc1, loc4]])
        l2g_act_row2 = np.array([[loc2, loc1],[loc2, loc2],[loc2, loc3],[loc2, loc4]])
        l2g_act_row3 = np.array([[loc3, loc1],[loc3, loc2],[loc3, loc3],[loc3, loc4]])
        l2g_act_row4 = np.array([[loc4, loc1],[loc4, loc2],[loc4, loc3],[loc4, loc4]])
        
        # To properly indexing in code:
        l2g_prog_row1 = np.array([[loc1-1, loc1-1],[loc1-1, loc2-1],[loc1-1, loc3-1],[loc1-1, loc4-1]])
        l2g_prog_row2 = np.array([[loc2-1, loc1-1],[loc2-1, loc2-1],[loc2-1, loc3-1],[loc2-1, loc4-1]])
        l2g_prog_row3 = np.array([[loc3-1, loc1-1],[loc3-1, loc2-1],[loc3-1, loc3-1],[loc3-1, loc4-1]])
        l2g_prog_row4 = np.array([[loc4-1, loc1-1],[loc4-1, loc2-1],[loc4-1, loc3-1],[loc4-1, loc4-1]])

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

        t1.append([l2g_act_row1, l2g_act_row2, l2g_act_row3, l2g_act_row4])
        t2.append([l2g_prog_row1, l2g_prog_row2, l2g_prog_row3, l2g_prog_row4])
        Kl.append(elemK)
        L.append(l1)
