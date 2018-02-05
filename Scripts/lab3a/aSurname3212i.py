import numpy as np
#This is the script for the integrator
def inte(x):
    y = np.zeros(len(x))
    for i in range(0, len(x)):
        if i is 0:
            y[0] = x[0]
        else:
            w = y[i-1]
            y[i] = w + x[i]
    return y

if __name__ == '__main__':
    # n = np.arange(0, 10)
    print('3212')
    # n
    # y = inte(x)
    # print(x)
    # print(y)
