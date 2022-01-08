#!/usr/bin/env python3
# coding:utf-8
import matplotlib.pyplot as plt


# exercice 59 page 260
def p(k):  # this is a mathematical funct
    return 2*k**3 - 132*k**2 + 2898*k + 9412


def max_():  # calculates the max of p(k) with k in [0, 23].
    #          Returns a tuple : (n, y) where y is the maximum of p(k) and n the k value where this maximum is reached.
    #          You can verify this with the MatPlotLib window that opens after this code executes and with the 01-12.png
    #          file.
    n = 0
    m = 0
    for k in range(0, 24):
        if m < p(k):
            m = p(k)
            n = k
    return n, m


print(max_())

Xlist = plt.np.arange(0, 24, 1)
Ylist = [p(x) for x in Xlist]
plt.plot(Xlist, Ylist)
plt.grid()
plt.show()
