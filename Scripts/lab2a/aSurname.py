import numpy as np
import matplotlib.pyplot as plt

x = []
n = []

n.append(np.arange(1, 20 + 1))
n.append(np.arange(-15, 15 + 1))
n.append(np.arange(200, 250 + 1))
n.append(np.arange(-15, 0 + 1))
# print(n[0])
# print(n[-1])
x.append(0.9*(n[0]==5))
x.append(0.8*(n[1]==0))
x.append(1.5*(n[2]==222))
x.append(3.5*(n[3]==-7))

# f = []
# f_, (ax1, ax2) = plt.subplots(1, 2)
# f.append(f_)
# ax1.stem(n[0], x[0])
# plt.stem(n[0], x[0])
# ax1.set_xlabel('n')
# ax1.set_ylabel('x(n)')


# plt.show()
# f.pop().show()
input()
# plt.stem(n[0], x[0])
# plt.grid()
# plt.show()
# print(n_[0])
# print(x[0])
