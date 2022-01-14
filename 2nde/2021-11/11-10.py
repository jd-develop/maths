#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
# -----------------
# EX 93 P 37
# -----------------

print("Exercice 93 page 37")


def toc(a):
    while a > 9:
        a = a - 9
    return a


print(f"toc(40) renvoie {toc(40)}")
print(f"toc(50) renvoie {toc(50)}")
print(f"toc(59) renvoie {toc(59)}")

# -----------------
# EX 96 P 37
# -----------------
print("Exercice 96 page 37")


def sous(n: int):
    d = n - 1
    while n % d != 0:
        d -= 1
    return d


while True:
    input_ = input("Entrez nombre entier diff de 1 : ")
    if input_ == 'exit':
        break
    print(sous(int(input_)))

# -----------------
# EX 98 P 37
# -----------------
print("Exercice 98 page 37")


def sqrt_sum(n: int = 2):
    sum_ = 0
    for a in range(1, (n+1 if n >= 2 else 3)):
        sum_ += math.sqrt(a)
    return sum_


input_ = int(input("Entrez nombre entier supérieur à 2 : "))
print(sqrt_sum(input_))

print("question 2")
a_ = 2
while sqrt_sum(a_) <= 100:
    a_ += 1
print(a_)
