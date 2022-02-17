# fem_tests.py
from lib.fems import unifDistr, pointLoad, triangDistr


# Test 1
'''
w = 20   # units: (kN/m)
L = 5    # units: (m)
u = 0    # units == 0

fem_vect1 = unifDistributed(w, L, u)

print('\nMember-end forces:')
print(fem_vect1[0])

print('\nUnits:')
print(fem_vect1[1])
'''

# Test 2
'''
P = 100   # units: (kN/m)
a = 4     # units: (m)
b = 2     # units: (m)
u = 0     # units == 0

fem_vect2 = pointLoad(a, b, P, u)

print('\nMember-end forces:')
print(fem_vect2[0])

print('\nUnits:')
print(fem_vect2[1])
'''


# Test 3

wl = 10  # units: (kN/m)
wr = 0   # units: (kN/m)
L = 5    # units: (m)
u = 0    # units == 0

fem_vect3 = triangDistr(wl, wr, L, u)

print('\nMember-end forces:')
print(fem_vect3[0])

print('\nUnits:')
print(fem_vect3[1])

