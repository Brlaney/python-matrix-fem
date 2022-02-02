import math
import numpy as np


def distance(dx, dy):
    '''
    The distance formula, returns Length (L) 
    between two points (x1, y1) and (x2, y2).
    '''
    L1 = math.sqrt(dx**2 + dy**2)
    L2 = math.sqrt(dx**2 + dy**2) / 12

    '''
    The following 8 cases address each possible condition for dx & dy.
    First four cases: Quad-IV, III, II, & I.
    Last four cases:  theta = 90, 270, 0, 180.
    '''
    if dx > 0 and dy < 0:
        angler = 2*np.pi + math.atan(dy / dx)
        angled = 360 + math.atan(dy / dx) * (180 / np.pi)
    elif dx < 0 and dy < 0:
        angler = (3*np.pi / 2) + math.atan(dy / dx)
        angled = 270 + math.atan(dy / dx) * (180 / np.pi)
    elif dx < 0 and dy > 0:
        angler = np.pi + math.atan(dy / dx)
        angled = 180 + math.atan(dy / dx) * (180 / np.pi)
    elif dx > 0 and dy > 0:
        angler = math.atan(dy / dx)
        angled = math.atan(dy / dx) * (180 / np.pi)
    elif dx == 0 and dy > 0:
        angler = np.pi / 2
        angled = 90
    elif dx == 0 and dy < 0:
        angler = np.pi * 3 / 2
        angled = 270
    elif dx > 0 and dy == 0:
        angler = 0
        angled = 0
    elif dx < 0 and dy == 0:
        angler = np.pi
        angled = 180
    else:
        print('An error has occured. The system does not match any case.')

    return [
        round(L1, 1),
        round(L2, 1),
        round(angled, 0),
        round(angler, 2)
    ]


def process(n, m, gdof, nodes, members, E, A, L1, L2, thetas1, thetas2, Kg, fg, dg):

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
        y1 = nodes[mn1-1][1]  # node mn1 y1-coordinates
        x2 = nodes[mn2-1][0]  # node mn2 x2-coordinates
        y2 = nodes[mn2-1][1]  # node mn2 y2-coordinates

        dx = x2 - x1  # Change in x
        dy = y2 - y1  # Change in y

        properties = distance(dx, dy)

        memberLIn = [properties[0]]
        memberLFt = [properties[1]]
        thetad = [properties[2]]
        thetar = [properties[3]]

        cs = np.cos(thetad)
        sn = np.sin(thetad)
        coeff = (E[i] * A[i]) / memberLIn

        elementK = coeff * np.array([
            [cs*cs, cs*sn, -cs*cs, -sn*sn],
            [cs*sn, sn*sn, -cs*sn, -sn*sn],
            [-cs*cs, -cs*sn, cs*cs, cs*sn],
            [-cs*sn, -sn*sn, cs*sn, sn*sn]
        ])
        
        newK[l2g[0]] = elementK[0][0]
        newK[l2g[1]] = elementK[1][1]
        newK[l2g[2]] = elementK[2][2]
        newK[l2g[3]] = elementK[3][3]
        
        Kg = newK + Kg
        
        L1.append(memberLIn)
        L2.append(memberLFt)
        thetas1.append(thetad)
        thetas2.append(thetar)
        