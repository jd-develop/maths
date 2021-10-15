#!/usr/bin/env python3
# coding:utf-8


def retourner_str(str_a_retourner: str):
    liste_retournee = []
    for letter in str_a_retourner:
        liste_retournee.insert(0, letter)
    str_retourne = ""
    for e in liste_retournee:
        str_retourne += e

    return str_retourne


def volume_pyramide(cote: float | int, hauteur: float | int):
    aire = cote**2
    return 1/3*aire*hauteur


def f(x):
    return 3*x + 1


print(retourner_str(str(input("Chaîne de caractères à retourner : "))))
print(volume_pyramide(
    eval(input("Côté de la pyramide : ")),
    eval(input("Hauteur de la pyramide : "))
))
print("x : f(x)")
for x in range(-5, 6, 2):
    print(x, ":", f(x))
