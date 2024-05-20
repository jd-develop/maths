#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# this integrates two functions between 0 and 10
from typing import Callable


def f(x: int | float):
    return 3*x + 2


def g(x: int | float):
    return 2*(x**2) - 2*x + 6


def F(x: int | float):
    return (3/2)*(x**2) + 2*x


def G(x: int | float):
    return (2/3)*(x**3) - (x**2) + 6*x


a = 0
b = 10


def subdivision(a: int, b: int, n: int):
    return [a + k*(b-a)/n for k in range(n)]


def integrate(
        a: int, b: int, n: int,
        function: Callable[[int | float], int | float],
        primitive: Callable[[int | float], int | float] | None = None
    ):
    if primitive is not None:
        print(f"On doit trouver {primitive(b) - primitive(a)}")
    for k in range(1, n):
        subdivision_ = subdivision(a, b, k)
        sum_ = 0
        for morceau in subdivision_:
            sum_ += function(morceau)
        sum_ *= (b-a)/n
        print(sum_)
