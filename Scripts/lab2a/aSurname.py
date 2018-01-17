import numpy as np
import matplotlib.pyplot as plt


def signal2211():
    x = []
    n = []
    n.append(np.arange(1, 20 + 1))
    n.append(np.arange(-15, 15 + 1))
    n.append(np.arange(200, 250 + 1))
    n.append(np.arange(-15, 0 + 1))
    x.append(0.9*(n[0]==5))
    x.append(0.8*(n[1]==0))
    x.append(1.5*(n[2]==222))
    x.append(3.5*(n[3]==-7))
    return n, x
