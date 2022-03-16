#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


def maximum(f_, a: int | float, b: int | float, p: int | float):
    """Maximum de f(x) sur l'intervalle [a, b] avec un pas de p"""
    x, y_max = a, f_(a)
    x += p
    while x <= b:
        if f_(x) > y_max:
            y_max = f_(x)
        x += p
    return y_max


def minimum(f_, a: int | float, b: int | float, p: int | float):
    """Minimum de f(x) sur l'intervalle [a, b] avec un pas de p"""
    x, y_min = a, f_(a)
    x += p
    while x <= b:
        if f_(x) < y_min:
            y_min = f_(x)
        x += p
    return y_min


def f(x):
    return -(x ** 3) + 2*(x ** 2) + 3*x + 1


Xlist = plt.np.arange(-1, 6, 10e-3)
Ylist = [f(x) for x in Xlist]
plt.plot(Xlist, Ylist)
plt.grid()
plt.show()

print(maximum(f, -1, 5, 10e-6))
print(minimum(f, -1, 5, 10e-6))
