import numpy as np

def genDiscreteSignal(amp, sigFrq, sampFrq, phs, start, stop):
    #phase in radians
    t = np.linspace(start, stop, 512)
    nMax = stop * sampFrq
    n = np.arange(0, nMax + 1)
    x = [t, n]
    sT = amp * np.cos((2 * np.pi * sigFrq * t) + phs)
    sN = amp * np.cos((2 * np.pi * (sigFrq/sampFrq) * n) + phs)
    s = [sT, sN]
    return x, s
