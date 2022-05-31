#!/usr/bin/env python3
# coding:utf-8
from random import random


# ex 34p342
def chat():
    return random() < 0.28


def rep_chat(n):
    s = 0
    for loop in range(n):
        s += int(chat())
    return s


for _ in range(10):
    print(rep_chat(1000))


# ex 37p342
def coin(n: int):
    s = 0
    for loop in range(n):
        if random() < 0.5:
            s += 1
    return s / n


print(coin(10))
print(coin(1000))
print(coin(10000))
print(coin(1000000))
