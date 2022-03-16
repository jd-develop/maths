#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Nombres aléatoires (Random numbers)"""
import random as rd
from pprint import pprint
import matplotlib.pyplot as plt

print("Nombre flottant entre 0 inclus et 1 exclu")
print(rd.random())

print("Nombre aléatoire flottant entre a inclus et b inclus, ici a=-5 et b=5")
print(rd.uniform(-5, 5))

print("Nombre entier aléatoire entre a inclus et b inclus, ici a=-5 et b=5")
print(rd.randint(-5, 5))


# calcul de la fréquence des résultats de la somme du lancer de deux dés
def two_dice_simulator(launches):
    sums = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
    }
    for i in range(launches):
        dice1 = rd.randint(1, 6)
        dice2 = rd.randint(1, 6)
        sum_ = dice1 + dice2
        sums[sum_] += 1
    for sum_ in sums:
        sums[sum_] /= launches
    return sums


simulation = two_dice_simulator(1000)
pprint(simulation)

events_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result_list = [simulation[idx] for idx in events_list]

plt.bar(events_list, result_list)
plt.show()
