# lib/deformation.py 
import numpy as np
import matplotlib.pylab as plt

'''
This is currently not functioning
'''
def plot(x, y):
    fig = plt.figure()
    plt.plot(x, y)
    plt.xlabel('X-Coordinates')
    plt.ylabel('Y-Coordinates')
    plt.axis('tight')
    return fig
