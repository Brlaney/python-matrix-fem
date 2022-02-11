from math import sin, cos, atan, pi, radians, dist
import numpy as np


def lAndAng(p1, p2):
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
    if dx > 0 and dy < 0:
        a1 = 360+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy < 0:
        a1 = 270+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy > 0:
        a1 = 180+atan(dy/dx)*(180/pi)
    elif dx > 0 and dy > 0:
        a1 = atan(dy/dx)*(180/pi)
    elif dx == 0 and dy > 0:
        a1 = 90
    elif dx < 0 and dy == 0:
        a1 = 180
    elif dx == 0 and dy < 0:
        a1 = 270
    elif dx > 0 and dy == 0:
        a1 = 0
    else:
        print('An error has occured. The system does not match any case.')
    
    # Convert from deg to rad
    a2 = radians(a1)

    return [L1, L2, a1, a2]


def processTruss(n, m, nodes, members, E, A, L1, L2, orient1, orient2, Kg, Kl, fg, dgu):
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

        # actual global dof number:
        localToGlobal = np.array([
            [dof1],
            [dof2],
            [dof3],
            [dof4]])

        # for properly index in programming:
        l2g = np.array([
            [dof1-1],
            [dof2-1],
            [dof3-1],
            [dof4-1]])

        x1 = nodes[mn1-1][0]  # node mn1 x1-coordinates
        y1 = nodes[mn1-1][1]  # node mn1 y1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates
        y2 = nodes[mn2-1][1]  # node mn2 y2-coordinates

        # Local elem node 1 & 2:
        n1 = (x1, y1)
        n2 = (x2, y2)

        properties = lAndAng(n1, n2)

        l1 = properties[0]
        l2 = properties[1]
        t1 = properties[2]
        t2 = properties[3]
        cs = cos(t2)
        sn = sin(t2)
        coeff = (E[i]*A[i])/l1

        elementK = coeff * np.array([
            [cs*cs, cs*sn, -cs*cs, -sn*sn],
            [cs*sn, sn*sn, -cs*sn, -sn*sn],
            [-cs*cs, -cs*sn, cs*cs, cs*sn],
            [-cs*sn, -sn*sn, cs*sn, sn*sn]
        ])

        '''
        print('\n Element', p, 'local to global dofs are:')
        print('\n')
        print(localToGlobal[0])
        print(localToGlobal[1])
        print(localToGlobal[2])
        print(localToGlobal[3])
        '''

        L1.append(l1)
        L2.append(l2)
        orient1.append(t1)
        orient2.append(t2)
        Kl.append(elementK)
