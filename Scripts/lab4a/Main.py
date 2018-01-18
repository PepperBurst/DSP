from aSurname4a import *

from scipy import signal as sig
import numpy as np
import matplotlib.pyplot as plt

def plot4211(code, date):
    b, a = coeff421()
    title = []
    title.append('Figure 42111\nFrequency Response of\n')
    title[-1] += 'y(n) = ½[x(n) - 0.5x(n-1)]\n'
    title[-1] += code + ' ' + date
    title.append(title[-1].replace('111', '112', 1))
    title[-1] = title[-1].replace('- 0.5', '+ ', 1)
    title.append(title[-1].replace('12', '13', 1))
    title[-1] = title[-1].replace('+ x(n-1)', '- x(n-2)', 1)
    title.append(title[-1].replace('13', '14', 1))
    title[-1] = title[-1].replace('-', '+', 1)
    title.append(title[-1].replace('14', '15', 1))
    title[-1] = title[-1].replace('y(n)', 'y(n) - 1.8cos(π/16)y(n-1) + 0.81y(n-2)')
    title[-1] = title[-1].replace('½[x(n) + x(n-2)]', 'x(n) + ½x(n-1)')
    xtk = np.linspace(0, 2*np.pi, 5)
    xtkLbl = ('0', '½π', 'π', '2½π', '2π')
    for i in range(len(b)):
        w, h = sig.freqz(b[i], a[i], whole=True)
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

def plot4212(code, date):
    b, a = coeff421()
    title = []
    title.append('Figure 42111\nFrequency Response of\n')
    title[-1] += 'y(n) = ½[x(n) - 0.5x(n-1)]\n'
    title[-1] += code + ' ' + date
    title.append(title[-1].replace('111', '112', 1))
    title[-1] = title[-1].replace('- 0.5', '+ ', 1)
    title.append(title[-1].replace('12', '13', 1))
    title[-1] = title[-1].replace('+ x(n-1)', '- x(n-2)', 1)
    title.append(title[-1].replace('13', '14', 1))
    title[-1] = title[-1].replace('-', '+', 1)
    title.append(title[-1].replace('14', '15', 1))
    title[-1] = title[-1].replace('y(n)', 'y(n) - 1.8cos(π/16)y(n-1) + 0.81y(n-2)')
    title[-1] = title[-1].replace('½[x(n) + x(n-2)]', 'x(n) + ½x(n-1)')
    xtk = np.linspace(0, np.pi, 5)
    xtkLbl = ('0', '¼π', '½π', '¾π', '2π')
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


def plotlab4a(code, date):
    # plot4211(code, date)
    # plot4212(code, date)

if __name__ == '__main__':
    code = 'RJTRAMOS'
    date = '1/18/2018'
    plotlab4a(code, date)
