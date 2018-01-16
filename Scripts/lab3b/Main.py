from aSurnameFilters import *
import numpy as  np
import matplotlib.pyplot as plt
#Plot of all graphs
#There will be a total of 6 plots
def plotlab3b(code, date):
    n = np.arange(-10, 10 + 1)
    x = 1*(n==0)
    y = [s1(x), s2(x), s2(s1(x)), s1(s2(x))]
    # we are using object oriented programming
    # in using the figure plots in
    # matplot matplotlib
    title = 'Figure 3312a\n'
    title += 'Impulse response of s1(n)\n'
    title += code + ' ' + date
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, y[0])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('x(n)')
    axarr[1].set_ylabel('s1(n)')
    title = title.replace('3312a', '3312b', 1)
    title = title.replace('s1(n)', 's2(n)', 1)
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, y[1])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xa(n)')
    axarr[1].set_ylabel('inte(xa(n))')
    title = title.replace('3312b', '3312c', 1)
    title = title.replace('s2(n)', 's2(s1(n))')
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, y[2])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xb(n)')
    axarr[1].set_ylabel('diff(xb(n))')
    title = title.replace('3312c', '3312d', 1)
    title = title.replace('s2(s1(n))', 's1(s2(n))')
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, y[3])
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('xb(n)')
    axarr[1].set_ylabel('inte(xb(n))')
    n = np.arange(0, 128 + 1)
    x = 1*(n==0)
    title = title.replace('3312d', '351', 1)
    title = title.replace('s1(s2(n))', 'y(n) + 0.8y(n − 2) = 0.2x(n) + 0.4x(n − 1) + 0.2x(n − 2)')
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, fil351(x))
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('x(n)')
    axarr[1].set_ylabel('y(n)')
    n = np.arange(-10, 100 + 1)
    x = 1*(n==0)
    title = title.replace('351', '352', 1)
    title = title.replace('y(n) − 1.8 cos(π/16)y(n − 1) + 0.81y(n − 2) = x(n) + 1/2x(n − 1)',
        'y(n) + 0.8y(n − 2) = 0.2x(n) + 0.4x(n − 1) + 0.2x(n − 2)')
    f, axarr = plt.subplots(2)
    f.suptitle(title)
    axarr[0].stem(n, x)
    axarr[1].stem(n, fil352(x))
    axarr[0].grid()
    axarr[1].grid()
    axarr[1].set_xlabel('n')
    axarr[0].set_ylabel('x(n)')
    axarr[1].set_ylabel('y(n)')
    plt.show()

if __name__ == '__main__':
# edit your code and date here
    code = 'RJTRAMOS'
    date = '1/16/2018'
    plotlab3b(code, date)
    path = 'music.wav'
    musicFilter(path)
