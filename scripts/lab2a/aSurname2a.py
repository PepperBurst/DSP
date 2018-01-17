import numpy as np

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

def impulseTrain(signal, period, width):
    y = signal % period < width
    return y

def signal2311():
    n = []
    x = []
    n.append(np.arange(0, 25 + 1))
    x.append(np.sin(np.pi/17)*n[-1])
    n.append(np.arange(-15, 25 + 1))
    x.append(np.sin(np.pi/17)*n[-1])
    n.append(np.arange(-10, 10 + 1))
    x.append(np.sin((3*np.pi*n[-1]) + (np.pi/2)))
    n.append(np.arange(0, 50 + 1))
    x.append(np.cos((np.pi/np.sqrt(23))*n[-1]))
    return n, x
