import numpy as np

def ex3212d(x):
    x_ = np.roll(x, 1)
    x_[0] = 0
    y = x - x_
    return y

if __name__ == '__main__':
    # x = np.arange(0, 10)
    # y = ex3212d(x)
