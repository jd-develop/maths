#!/usr/bin/env python3
# coding:utf-8
# no imports

def f(x):
    return ((2 * x) ** 2 - 12 * x) + 20

# number = float(input("Entrez un nombre : "))
# print(f(number))

number = -10
for loop in range(21):
    print("f({}) = ".format(number), f(number))
    number += 1
    
