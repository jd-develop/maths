#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from random import random
from math import sqrt


def sample(n, p):
    """Créé un échantillon de taille n.
    Renvoie la proportion de succès avec une probabilité p de succès"""
    nb_success = 0
    for i in range(n):
        if random() <= p:
            nb_success += 1
    return nb_success / n


def simulation(great_n, small_n, p):
    compteur = 0
    liste_freq = []
    for i in range(great_n):
        f = sample(small_n, p)
        if abs(p - f) < 1/sqrt(small_n):
            compteur += 1
        liste_freq.append(f)

    # plt.close()
    plt.scatter(range(great_n), liste_freq)
    plt.grid()
    plt.xlim(0, great_n)
    plt.ylim(0, 1)
    plt.plot([0, great_n], [p, p], '--')
    plt.show()

    return compteur/great_n


print(simulation(50, 50, .5))
print(simulation(50, 100, .5))
print(simulation(50, 200, .5))


# while True:
#     print(echantillon(*eval(input("n, p : "))))
