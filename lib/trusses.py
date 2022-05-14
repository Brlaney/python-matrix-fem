# lib/trusses.py
from math import sin, cos, atan, pi, radians, dist
import numpy as np

def calc_theta(dx, dy):
    '''
    First 4 cases: Quad-IV, III, II, & I
    Last 4 cases:  theta = 0, 90, 180, 270
    ''' 
    if dx > 0 and dy < 0: a1 = 360+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy < 0: a1 = 270+atan(dy/dx)*(180/pi)
    elif dx < 0 and dy > 0: a1 = 180+atan(dy/dx)*(180/pi)
    elif dx > 0 and dy > 0: a1 = atan(dy/dx)*(180/pi)
    elif dx > 0 and dy == 0: a1 = 0
    elif dx == 0 and dy > 0: a1 = 90
    elif dx < 0 and dy == 0: a1 = 180
    elif dx == 0 and dy < 0: a1 = 270
    else: print('An error has occured. The system does not match any case.')
    
    a2 = radians(a1)  # Convert from deg to rad
    return [a1, a2]

def KgTruss(n, m, nodes, members, E, A, L1, L2, a1, a2, Kg, Kl, fg, dgf):
    '''
      The following for loop iterates for however 
    many members are defined in the given system.
    '''
    
    for i in range(m):
        p = i + 1    # Unique key id (starts at 1)
        newK = np.zeros((2*n, 2*n))

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
        
        b = np.array([-1,-1])
        
        # To properly index in code:
        prog_row1 = act_row1 + b
        prog_row2 = act_row2 + b
        prog_row3 = act_row3 + b
        prog_row4 = act_row4 + b
        
        kij = np.array([prog_row1, prog_row2, prog_row3, prog_row4])
        
        '''
        print(kij[0][0])
        print(kij[0][1])
        print(kij[0][2])
        print(kij[0][3])
        '''

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
        
        '''
        for j in range(len(kij)):
            j_n1 = kij[j][0]
            k_n1 = kij[j][1]
        '''
        
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
        
        L1.append(l1)
        L2.append(l2)
        a1.append(theta1)
        a2.append(theta2)
        Kl.append(elemK)
        
    # Only copy the return value Kg IF 
    # the for loop above has finished!
    newKg = np.copy(Kg)
    
    return newKg
