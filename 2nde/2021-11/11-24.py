#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# premier nombre n tel que x**n > s
x, s = eval(input("Entrez x, s avec x>1 : "))
n, xn = 0, 1

while xn <= s:
    xn *= x
    n += 1

print(str(n) + " est le premier nombre n tel que x^n > s")  # x^n > s
