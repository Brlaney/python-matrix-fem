# fem_tests.py
from lib.fems import unifDistr, pointLoad, triangDistr


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
 
    Calculates the member-end shear forces 
and bending moments for a member w/ w, L, 
where w is a uniformly distributed load.

If units == 0: (kN/m & m)
If units == 1: (kips & ft)
If units == 2: (kips & in)
If units == 3: (lbs & ft)
If units == 4: (lbs & in)
'''


# 
# Test 1
'''
w = 0.3     # units: (k/in)
L = 360    # units: (in)
u = 2      # units == 0

fem_vect1 = unifDistr(w, L, u)

print('\nMember-end forces:')
print(fem_vect1[0])

print('\nUnits:')
print(fem_vect1[1])
'''


# 
# Test 2
P = 50      # units: (kips)
a = 180     # units: (m)
b = 180     # units: (m)
u = 2       # units == 0

fem_vect2 = pointLoad(a, b, P, u)

print('\nMember-end forces:')
print(fem_vect2[0])

print('\nUnits:')
print(fem_vect2[1])


# 
# Test 3
'''
wl = 10  # units: (kN/m)
wr = 0   # units: (kN/m)
L = 5    # units: (m)
u = 0    # units == 0

fem_vect3 = triangDistr(wl, wr, L, u)

print('\nMember-end forces:')
print(fem_vect3[0])

print('\nUnits:')
print(fem_vect3[1])
'''
