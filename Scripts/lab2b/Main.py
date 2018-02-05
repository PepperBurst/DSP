from aSurname2312 import *
from aSurname241 import *

from scipy.io import wavfile as wvf

import numpy as np
import matplotlib.pyplot as plt

def plot2312(code, date):
    amp, strAmp = 2, '2'
    frq, strFrq = 1/11, '1/11'
    phs, strPhs = 0, '0'
    n, x = genSinusoid(amp, frq, phs, -20, 20)
    f, ax = plt.subplots()
    title = 'Figure 2312\nPlot of x(n) = ampsin(π(frq)n+phs)\n'
    title += code + ' ' + date
    title = title.replace('amp', strAmp, 1)
    title = title.replace('frq', strFrq, 1)
    if phs is not 0:
        title = title.replace('+phs', strPhs, 1)
    else:
        title = title.replace('+phs', '', 1)
    f.suptitle(title)
    ax.stem(n, x)
    ax.set_xlabel('n')
    ax.set_ylabel('x(n)')
    # ax.axhline(linewidth=1, color="black")
    # ax.axvline(linewidth=1, color="black")
    ax.grid()
    plt.show()

def plot241(code, date):
    amp = 50
    phsDeg = 45
    phsRad = np.deg2rad(phsDeg)
    sigFrq = 1200
    sampFrq = 8000
    startTime = 0
    endTime = 0.007
    title = 'Figure 241\n'
    title += 'Plot of a finite-length discrete-time signal\n'
    title += code + ' ' + date
    x, s = genDiscreteSignal(amp, sigFrq, sampFrq, phsRad, startTime, endTime)
    f, (ax1, ax2) = plt.subplots(2)
    f.suptitle(title)
    ax1.plot(x[0], s[0])
    ax1.set_xlabel('t')
    ax1.set_ylabel('s(t)')
    ax1.axhline(linewidth=1, color="black")
    ax1.axvline(linewidth=1, color="black")
    ax1.grid()
    ax2.stem(x[1], s[1])
    ax2.set_xlabel('n')
    ax2.set_ylabel('s(n)')
    # ax2.axvline(linewidth=1, color="black")
    ax2.grid()
    plt.show()

def plot2511(code, date):
    n = np.arange(0, 20 + 1)
    x = (0.9)**n
    s = np.around(np.sum(x), decimals=2)
    title = 'Figure 2511\nPlot of x(n) = (0.9)n\n'
    title += code + ' ' + date
    f, ax = plt.subplots()
    f.suptitle(title)
    ax.stem(n, x)
    ax.set_xlabel('n')
    ax.set_ylabel('y(n)')
    # ax.axvline(linewidth=1, color="black")
    ax.text(10, 0.8, 'Sum of x(n) = ' + str(s), fontsize=15)
    ax.grid()
    plt.show()

def plot261(code, date, path):
    rate, data = wvf.read(path)
    title = 'Figure 261\nPlot of ' + path + '\n'
    title += code + ' ' + date
    f, ax = plt.subplots()
    f.suptitle(title)
    ax.plot(np.arange(0, len(data)), data)
    ax.set_xlabel('n')
    ax.set_ylabel('x(n)')
    ax.grid()
    f, ax = plt.subplots()
    f.suptitle('Normalized plot of\nFigure 261')
    normData = data / ((2**16)/2)
    ax.plot(np.arange(0, len(normData)), normData)
    ax.set_xlabel('n')
    ax.set_ylabel('x(n)')
    ax.grid()
    plt.show()

def plot271(code, date):
    title = 'Figure 271\nPlot of f(m, n) = 255|sinc(0.1m)sin(0.1n)|\n'
    title += code + ' ' + date
    m = np.arange(-50, 50 + 1)
    n = np.arange(-50, 50 + 1)
    mm, nn = np.meshgrid(m, n, sparse=True)
    z = 255*np.abs(np.sinc(0.1*mm)*np.sin(0.1*nn))
    plt.contourf(m,n,z)
    plt.title(title)
    plt.xlabel('m')
    plt.ylabel('n')
    plt.show()

def plotlab3b(code, date, path):
    # plot2312(code, date)
    plot241(code, date)
    # plot2511(code, date)
    # plot261(code, date, path)
    # plot271(code, date)

if __name__ == '__main__':
    code = 'RJTRAMOS'
    date = '1/17/2018'
    path = 'speech1.wav'
    plotlab3b(code, date, path)
