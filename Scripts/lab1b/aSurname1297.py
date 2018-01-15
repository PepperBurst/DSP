import matplotlib.pyplot as plt
import numpy as np

def ex1297(code, date):
    x = np.linspace(0, 5, 256)
    y = []
    for w in [1, 3, 10]:
        y.append(5 + ((5*np.exp(-x))*np.cos((w*x)+5)))
    title = 'y(x) = 5 + 5 exp(-x)*cos(wx + 0.5)\n'
    title += code + ' ' + date
    xlab = 'time(seconds)'
    ylab = 'y(x)'
    plt.plot(x, y[0])
    plt.plot(x, y[1], '+')
    plt.plot(x, y[2], 'o')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    ex1297('RJTRAMOS', '1/5/2018')
