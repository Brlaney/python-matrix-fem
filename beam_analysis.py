from math import sin, cos, atan, pi, radians, dist
import numpy as np


def processBeam(n, m, nodes, members, E, I, L, Kg, Kl, fg, dgu):
    '''
      The following for loop iterates for however 
    many members are defined in the given system.
    '''
    for i in range(m):
        p = i + 1  # actual member number
        newK = np.zeros((2*n, 2*n))

        # For member number: i, map nodes: mn1 --> mn2
        mn1 = members[i][0]
        mn2 = members[i][1]

        loc1 = 2 * mn1 - 1
        loc2 = 2 * mn1
        loc3 = 2 * mn2 - 1
        loc4 = 2 * mn2

        # actual global dof number:
        localToGlobal = np.array([[loc1], [loc2], [loc3], [loc4]])

        # for properly index in programming:
        l2g = np.array([[loc1-1], [loc2-1], [loc3-1], [loc4-1]])

        x1 = nodes[mn1-1][0]  # node mn1 x1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates

        # Local elem node 1 & 2:
        n1 = (x1, 0)
        n2 = (x2, 0)

        l1 = dist(n1, n2)
        l2 = l1 / 12
        c = (2*E[i]*I[i]) / l1 ^ 3

        elementK = c * np.array([
            [c*6, -3*l1*c, -6*c, -3*l1*c],
            [-3*l1*c, 2*c*l1 ^ 2, 3*l1*c, c*l ^ 2],
            [-c*6, 3*c*l1, 6*c, 3*c*l1],
            [-3*l1*c, c*l1 ^ 2, 3*l1*c, 2*c*l ^ 2]
        ])

        print('\n Element', p, 'local to global dofs are:')
        print('\n')
        print(localToGlobal[0])
        print(localToGlobal[1])
        print(localToGlobal[2])
        print(localToGlobal[3])

        Kl.append(elementK)
        L.append(l1)
