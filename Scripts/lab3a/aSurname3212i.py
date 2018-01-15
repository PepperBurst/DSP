import numpy as np

def ex3212i(x):
    y = np.zeros(len(x))
    for i in range(1, len(x)):
        w = y[i-1]
        y[i] = w + x[i]
    return y

if __name__ == '__main__':
    # x = np.arange(0, 10)
    # y = ex3212i(x)
    # print(x)
    # print(y)
