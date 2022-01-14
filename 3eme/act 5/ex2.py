#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math


def primalite(n):
    diviseur = 2
    while diviseur <= math.sqrt(n):
        if (n % diviseur) == 0:
            return False
        else:
            diviseur += 1
    return True


print(primalite(int(input("Nombre à tester:"))))
