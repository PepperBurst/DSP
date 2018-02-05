from aSurname4b import *

from scipy import signal as sig
import numpy as np
import matplotlib.pyplot as plt

def plot422(code, date):
    b, a = coeff422()
    title = []
    titFig = 'Figure 4220\nFrequency Response of\n'
    title.append('y(n) + 0.13y(n-1) + 0.52y(n-2) + 0.3y(n-3)\n= 0.16x(n) - 0.48x(n-1) + 0.48x(n-2) - 0.16x(n-3)')
    title.append('y(n) - 0.268y(n-2) = 0.634x(n) - 0.634x(n-2)')
    title.append('y(n) + 0.268x(n-2) = 0.634x(n) + 0.634x(n-2)')
    title.append('10y(n) - 5y(n-1) + y(n-2) = x(n) - 5x(n-1) + 10x(n-2)')
    for i in range(len(title)):
        tempFig = titFig.replace('220', str(221 + i))
        title[i] = tempFig + title[i]
        title[i] += code + ' ' + date
    xtk = np.linspace(0, np.pi, 5)
    xtkLbl = ('0', '¼π', '½π', '¾π', 'π')
    for i in range(len(b)):
        w, h = sig.freqz(b[i], a[i], whole=False)
        f, (ax1, ax2) = plt.subplots(2)
        # f.suptitle(title[i])
        ax1.set_title(title[i])
        ax1.plot(w, np.abs(h))
        ax1.set_ylabel('|H(ω)|')
        ax1.set_xticks(xtk)
        ax1.set_xticklabels(xtkLbl)
        ax1.grid()
        ax2.plot(w, np.angle(h))
        ax2.set_xlabel('ω')
        ax2.set_ylabel('θ(ω)')
        ax2.set_xticks(xtk)
        ax2.set_xticklabels(xtkLbl)
        ax2.grid()
    plt.show()

def plotlab4b(code, date):
    plot422(code, date)

if __name__ == '__main__':
    code = 'RJTRAMOS'
    date = '1/19/2018'
    plotlab4b(code, date)
