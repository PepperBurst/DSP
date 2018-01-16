from aSurname3212d import *
from aSurname3212i import *
import numpy as  np
import matplotlib.pyplot as plt
# Recommended to type this all in console
# plt.show() was used because there is no backend used in the python console
# if using Spyder or any other iPython Console,
# plt.show() is not needed
def plotlab3a(code, date):
    n = np.arange(-10, 20 + 1)
    x = []
    x.append(1*(n==0) - 1*(n==7))
    x.append(1*(n>=0) - 1*(n>=9))
    diffY = [diff(x[0]), diff(x[1])]
    inteY = [inte(x[0]), inte(x[1])]
    title = 'Figure 3212ad\n'
    title += 'Plot of xa(n) = δ(n) − δ(n − 7)\n'
    title += code + ' ' + date
    f, axarr = plt.subplots(2)
    f.suptitle('')
    axarr[0].stem(n, x[0])
    axarr[1].stem(n, diffY[0])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xa(n)')
    axarr[1].set_ylabel('diff(xa(n))')
    title = title.replace('ad', 'ai', 1)
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x[0])
    axarr[1].stem(n, inteY[1])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xa(n)')
    axarr[1].set_ylabel('inte(xa(n))')
    title = title.replace('ai', 'bd', 1)
    title = title.replace('Plot of xa(n) = δ(n) − δ(n − 7)', 'xb(n) = u(n)−u(n−(N+1)) with N = 8')
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x[1])
    axarr[1].stem(n, diffY[0])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xb(n)')
    axarr[1].set_ylabel('diff(xb(n))')
    title = title.replace('bd', 'bi', 1)
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x[1])
    axarr[1].stem(n, inteY[1])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xb(n)')
    axarr[1].set_ylabel('inte(xb(n))')
    plt.show()

if __name__ == '__main__':
# edit your code and date here
    code = 'RJTRAMOS'
    date = '1/16/2018'
    plotlab3a(code, date)
