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


number = 2
test = False
primaryNumbersNumber = 0
while number <= 10000:
    if primalité(number):
        primaryNumbersNumber += 1
    number += 1
print(primaryNumbersNumber)
