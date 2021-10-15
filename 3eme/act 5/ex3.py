#!/usr/bin/env python3
# coding:utf-8
import math


def primalité(n):
    diviseur = 2
    while diviseur <= math.sqrt(n):
        if (n % diviseur) == 0:
            return False
        else:
            diviseur += 1
    return True


number = 10000
test = False
while test == False:
    number += 1
    test = primalité(number)
print(number)
