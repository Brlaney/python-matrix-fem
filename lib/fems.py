# lib/fems.py
from math import sin, cos, atan, pi, radians, dist
import numpy as np

'''
Function inputs:

a: distance from left-end to the applied external load (P)
b: distance from the applied external load (P) to the right-end
P: magnitude of point load
u: constant integer defining system of units
w: magnitude of distributed load
L: length of member
wl: value of distributed load at left-end
wr: value of distributed load at right-end
'''

def detUnits(u):
    ''' Calculates the member-end shear forces 
    and bending moments for a member w/ w, L, 
    where w is a uniformly distributed load.

    If units == 0: (kN/m & m)
    If units == 1: (kips & ft)
    If units == 2: (kips & in)
    If units == 3: (lbs & ft)
    If units == 4: (lbs & in)
    '''
    if u == 0:
        units = ['kN', 'kN-m', 'kN', 'kN-m']
    elif u == 1:
        units = ['k', 'k-ft', 'k', 'k-ft']
    elif u == 2:
        units = ['k', 'k-in', 'k', 'k-in']
    elif u == 3:
        units = ['lbs', 'lbs-ft', 'lbs', 'lbs-ft']
    elif u == 4:
        units = ['lbs', 'lbs-in', 'lbs', 'lbs-in']
    else:
        print('Error, units were not properly specified.')

    return units


def pointLoad(a, b, P, u):
    if a == b:
        L = a + b
        v1 = P / 2
        m1 = -P * L / 8
        v2 = P / 2
        m2 = -P * L / 8
    elif a < b:
        v1 = P * b**2 * (3*a + b) / (a+b)**3
        m1 = -P * a * b**2 / (a + b)**2
        v2 = P * a**2 * (a + 3*b) / (a+b)**3
        m2 = P * a**2 * b / (a + b)**2
    elif b < a:
        v1 = P * a**2 * (a + 3*b) / (a+b)**3
        m1 = -P * a**2 * b / (a + b)**2
        v2 = P * b**2 * (3*a + b) / (a+b)**3
        m2 = P * a * b**2 / (a + b)**2
    else: 
        print('Error, please check your inputs for the function.')

    fem = np.array([v1, m1, v2, m2])
    units = detUnits(u)

    return [fem, units]


def unifDistr(w, L, u):
    v1 = w * L / 2
    m1 = -w * L**2 / 12
    v2 = w * L / 2
    m2 = -w * L**2 / 12

    fem = np.array([v1, m1, v2, m2])
    units = detUnits(u)

    return [fem, units]


def triangDistr(wl, wr, L, u):
    # Descending right triangular distributed load
    if wl > wr and wr == 0:
        w = wl
        
        v1 = 7 * w * L / 20
        m1 = - w * L**2 / 20
        v2 = 3 * w * L / 20
        m2 = w * L**2 / 30

    # Ascending right triangular distributed load
    elif wr > wl and wl == 0:
        w = wr
        
        v1 = 3 * w * L / 20
        m1 = - w * L**2 / 30
        v2 = 7 * w * L / 20
        m2 = w * L**2 / 20

    else: 
        print('Error, please check your inputs for the function.')
    
    fem = np.array([v1, m1, v2, m2])
    units = detUnits(u)
    
    return [fem, units]
