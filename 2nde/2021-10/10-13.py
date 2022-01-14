#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------
# EX 85 P 36
# -----------------
print("Exercice 85 page 36")


def exposant(a, n):
    p = 1
    for i in range(n):
        p = p * a
    return p


print(exposant(
    eval(input("nombre   : ")),
    eval(input("exposant : "))
))

# -----------------
# EX 2 POLYCOP FONCTIONS : CF maths/2021-10/10-08-functs.py lignes 21-22 et lignes 30-31-32
# -----------------


# -----------------
# EX 103 P 38
# -----------------
print("Exercice 103 page 38")


def syra(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    return n


def vol(n):
    t = 0
    while n != 1:
        t = t + 1
        n = syra(n)
    return t


result = eval(input("Nombre de départ : "))
# reiteration = eval(input("Nombre de réitérations : "))
# for loop in range(reiteration):
print(vol(result))

print("question 3d :")
entier_naturel = 1
plus_grand_temps_de_vol_actuel = 0
entier_naturel_avec_plus_grand_temps_de_vol_actuel = 1
while entier_naturel < 1000:
    temps_vol = vol(entier_naturel)
    if temps_vol > plus_grand_temps_de_vol_actuel:
        plus_grand_temps_de_vol_actuel = temps_vol
        entier_naturel_avec_plus_grand_temps_de_vol_actuel = entier_naturel
    entier_naturel += 1

print("Le plus grand temps de vol pour un entier naturel inférieur à 1000 est :")
print(plus_grand_temps_de_vol_actuel)
print("Pour l'entier :")
print(entier_naturel_avec_plus_grand_temps_de_vol_actuel)

# -----------------
# EX 76 P 35
# -----------------
print("Exercice 76 page 35")


def moy(a, b):
    m = (a + b) / 2
    return m


print("question 1")
nombre1, nombre2 = eval(input("Entrer deux nombres non nuls séparés d'une virgule pour déterminer leur moyenne : "))
print(moy(nombre1, nombre2))

print("question 2")


def harmo(x, y):
    """
        Moyenne harmonique
    """
    a = moy(1/x, 1/y)
    b = 1/a
    return b


nombre1, nombre2 = eval(input("Entrer deux nombres non nuls séparés d'une virgule pour déterminer leur moyenne "
                              "harmonique : "))
print(harmo(nombre1, nombre2))
