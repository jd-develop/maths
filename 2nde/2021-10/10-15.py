#!/usr/bin/env python3
# coding:utf-8
import math
# -----------------
# EX 98 P 37
# -----------------


def square_roots(n):
    """
        sqrt(1) + sqrt(2) + ... + sqrt(n)
    """
    if not n >= 2:
        return "n doit être supérieur ou égal à 2"
    s = 0
    for i in range(1, n+1):
        s += math.sqrt(i)
    return s


print(square_roots(
    eval(input("Entrer nombre n pour additionner les racines carrés de tous les nombres entre 1 et n : "))
))

s100 = 0
numbr = 1
while s100 < 100:
    numbr += 1
    s100 = square_roots(numbr)

print("Le plus petit nombre tel que la somme précédemment définie soit supérieure à 100 est", str(numbr))
