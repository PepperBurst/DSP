import matplotlib.pyplot as plt
import numpy as np

def ex1296(w, code, date):
    if(w in [1, 3, 10]):
        x = np.linspace(0, 2*np.pi, 256)
        y = (1/np.pi) + ((1/2)*np.sin(w*x)) - (((2/3)*np.pi)*np.cos(2*w*x))
        plt.plot(x, y)
        title = 'Plot of y(x) = (1/π) + (1/2)sinωx - (2/3π)cos2ωx\n'
        title += code + ' ' + date
        plt.title(title)
        xlab = 'time(seconds)'
        ylab = 'y(x) = (1/π) + (1/2)sinωx - (2/3π)cos2ωx'
        xtica = np.linspace(0, 2*np.pi, 5)
        xticb = ['0', '(1/2)π', 'π', '(2/3)π', '2π']
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.xticks(xtica, xticb)
        plt.grid()
        plt.show()
    else:
        print('Enter only values 1, 3, or 10')

if __name__ == '__main__':
    #ex1296(1, 'RJTRAMOS', '1/5/2018')
