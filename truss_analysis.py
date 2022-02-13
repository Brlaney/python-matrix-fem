from math import sin, cos, atan, pi, radians, dist
import numpy as np


def distAndAngle(p1, p2):
    '''
      The distance formula, returns Length (L) 
    between two points (x1, y1) and (x2, y2).
    '''
    L1 = dist(p1, p2)
    L2 = L1 / 12
    
    # Change in x & y
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    '''
      The following 8 cases address 
    each possible condition for dx & dy.
    First four cases: Quad-IV, III, II, & I.
    Last four cases:  theta = 90, 270, 0, 180.
    '''
    if dx > 0 and dy < 0: a1 = 360+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy < 0: a1 = 270+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy > 0: a1 = 180+atan(dy/dx)*(180/pi)
    elif dx > 0 and dy > 0: a1 = atan(dy/dx)*(180/pi)
    elif dx == 0 and dy > 0: a1 = 90
    elif dx < 0 and dy == 0: a1 = 180
    elif dx == 0 and dy < 0: a1 = 270
    elif dx > 0 and dy == 0: a1 = 0
    else: print('An error has occured. The system does not match any case.')
    
    # Convert from deg to rad
    a2 = radians(a1)

    return [L1, L2, a1, a2]


def processTruss(n, m, nodes, members, E, A, L1, L2, orient1, orient2, Kg, Kl, fg, dgu, t1, t2):
    '''
      The following for loop iterates for however 
    many members are defined in the given system.
    '''
    for i in range(m):
        # newK = np.zeros((2*n, 2*n))
        p = i + 1    # Unique key id (starts at 1)

        # For member number: i, map nodes: mn1 --> mn2
        mn1 = members[i][0]
        mn2 = members[i][1]

        dof1 = 2*mn1-1
        dof2 = 2*mn1
        dof3 = 2*mn2-1
        dof4 = 2*mn2

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
        y1 = nodes[mn1-1][1]  # node mn1 y1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates
        y2 = nodes[mn2-1][1]  # node mn2 y2-coordinates

        # Local elem node 1 & 2:
        n1 = (x1, y1)
        n2 = (x2, y2)

        props = distAndAngle(n1, n2)

        l1 = props[0]
        l2 = props[1]
        theta1 = props[2]
        theta2 = props[3]
        cs = cos(theta2)
        sn = sin(theta2)
        c = (E[i]*A[i])/l1

        elementK = c * np.array([
            [cs**2, cs*sn, -cs**2, -sn**2],
            [cs*sn, sn**2, -cs*sn, -sn**2],
            [-cs**2, -cs*sn, cs**2, cs*sn],
            [-cs*sn, -sn**2, cs*sn, sn**2]
        ])

        t1.append([act_row1, act_row2, act_row3, act_row4])
        t2.append([prog_row1, prog_row2, prog_row3, prog_row4])
        L1.append(l1)
        L2.append(l2)
        orient1.append(theta1)
        orient2.append(theta2)
        Kl.append(elementK)
