#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from math import sqrt

Xlist = [2, 0]
Ylist = [-5, 2]
plt.plot(Xlist, Ylist)
plt.show()


def f(x):
    if x >= 0:
        return sqrt(x)
    else:
        return sqrt(-x)


Xlist = plt.np.linspace(-5, 5, 101)
Ylist = [f(x) for x in Xlist]
plt.plot(Xlist, Ylist)
plt.grid()
plt.show()


def f(x):
    return x**2


Xlist = plt.np.linspace(-5, 5, 101)
Ylist = [f(x) for x in Xlist]
plt.plot(Xlist, Ylist)
plt.grid()
plt.show()


def f(x):
    return 1/x


Xlist = plt.np.linspace(-5, 5, 101)
Ylist = [f(x) for x in Xlist]
plt.plot(Xlist, Ylist)
plt.grid()
plt.show()
