# trusses.py
from math import sin, cos, atan, pi, radians, dist
import numpy as np


def calc_theta(dx, dy):
    # First 4 cases: Quad-IV, III, II, & I
    # Last 4 cases:  theta = 90, 180, 270, 0
    if dx > 0 and dy < 0: a1 = 360+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy < 0: a1 = 270+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy > 0: a1 = 180+atan(dy/dx)*(180/pi)
    elif dx > 0 and dy > 0: a1 = atan(dy/dx)*(180/pi)
    elif dx == 0 and dy > 0: a1 = 90
    elif dx < 0 and dy == 0: a1 = 180
    elif dx == 0 and dy < 0: a1 = 270
    elif dx > 0 and dy == 0: a1 = 0
    else: print('An error has occured. The system does not match any case.')
    
    a2 = radians(a1)  # Convert from deg to rad
    return [a1, a2]


def processTruss(n, m, nodes, members, E, A, L1, L2, orient1, orient2, Kg, Kl, fg, dgf, t1, t2):
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
        
        b = np.array([[1,1],[1,1],[1,1],[1,1]])
        
        # To properly indexing in code:
        prog_row1 = act_row1 - b
        prog_row2 = act_row2 - b
        prog_row3 = act_row3 - b
        prog_row4 = act_row4 - b

        x1 = nodes[mn1-1][0]  # node mn1 x1-coordinates
        y1 = nodes[mn1-1][1]  # node mn1 y1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates
        y2 = nodes[mn2-1][1]  # node mn2 y2-coordinates

        n1 = (x1, y1)  # Local node 1 coordinates
        n2 = (x2, y2)  # Local node 2 coordinates
       
        dx = n2[0]-n1[0]  # delta_x
        dy = n2[1]-n1[1]  # delta_y
        
        l1 = dist(n1, n2)   # Length (in)
        l2 = l1/12          # Length (ft)
        
        angles = calc_theta(dx, dy)

        theta1 = angles[0]
        theta2 = angles[1]
        cs = cos(theta2)
        sn = sin(theta2)
        c = (E[i]*A[i])/l1

        elementK = c*np.array([
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
