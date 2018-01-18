import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal as sig

def coeff421():
    b = []
    a = []
    b.append([1/2, 1/2 * -0.5])
    b.append([1/2, 1/2])
    b.append([1/2, 0, -1/2])
    b.append([1/2, 0, 1/2])
    b.append([1, 1/2])
    a.append([1])
    a.append([1])
    a.append([1])
    a.append([1])
    a.append([1, -1.8*np.cos(np.pi/16), 0.81])
    return b, a
