import numpy as np

def genSinusoid(amp, frq, phs, start, stop):
    #phase in radians
    n = np.arange(start, stop + 1)
    x = amp * np.sin((frq * np.pi * n) + phs)
    return n, x
