from aSurname2a import *
import numpy as np
import matplotlib.pyplot as plt

def plot2211(code, date):
    n, x = signal2211()
    title = []
    title.append('Figure 22111\nImpulse Signal\n')
    title[-1] += code + ' ' + date
    title.append(title[-1].replace('22111', '22112'))
    title.append(title[-1].replace('22112', '22113'))
    title.append(title[-1].replace('22113', '22114'))
    for i in range(len(n)):
        f, ax = plt.subplots()
        f.suptitle(title[i])
        ax.stem(n[i], x[i])
        ax.set_xlabel('n')
        ax.set_ylabel('x(n)')
        ax.grid()
    plt.show()

def plot2213(code, date):
    n = np.arange(0, 50 + 1)
    x = impulseTrain(n, 5, 1)
    title = 'Figure 2213\nImpulse Train with period = 5\n'
    title += code + ' ' + date
    f, ax = plt.subplots()
    f.suptitle(title)
    ax.stem(n, x)
    ax.set_xlabel('n')
    ax.set_ylabel('x(n)')
    ax.grid()
    plt.show()

def plot2311(code, date):
    n, x = signal2311()
    title = []
    title.append('Figure23111\nPlot of x(n) = sin(π/17)n\n')
    title[-1] += code + ' ' + date
    title.append(title[-1].replace('23111', '23112'))
    title.append(title[-1].replace('23112', '23113'))
    title[-1] = title[-1].replace('sin(π/17)n', 'sin(3πn + π/2)')
    title.append(title[-1].replace('23113', '23114'))
    title[-1] = title[-1].replace('sin(3πn + π/2)', 'cos(nπ/√23)')
    for i in range(len(n)):
        f, ax = plt.subplots()
        f.suptitle(title[i])
        ax.stem(n[i], x[i])
        ax.set_xlabel('n')
        ax.set_ylabel('x(n)')
        ax.grid()
    plt.show()

def plotlab2a(code, date):
    plot2211(code, date)
    # plot2213(code, date)
    # plot2311(code, date)

if __name__ == '__main__':
    code = 'AMETRAN'
    date = '1/18/2018'
    plotlab2a(code, date)
