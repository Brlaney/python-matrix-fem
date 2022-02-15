# fem.py
from lib.fixedendmoments import unifDistributed, pointLoad

'''
This script will import the fixed-end moments
function script from /lib and implement on a elem.
'''

# The following tests the output of 
# beam1's uniformly distributed load.
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

# The following tests the output of 
# beam1's point load for method 2 elem 1.
P = 100   # units: (kN/m)
a = 4     # units: (m)
b = 2     # units: (m)
u = 0     # units == 0

fem_vect2 = pointLoad(a, b, P, u)

print('\nMember-end forces:')
print(fem_vect2[0])

print('\nUnits:')
print(fem_vect2[1])
