#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# notes : on remarque que le développement en fraction continue de sqrt(61)
# commence par [7, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14]. On peut donc conjecturer,
# selon la remarque précédent la question 39, qu’il est périodique de période
# 11.

def pell_fermat():
    p_n_moins_2 = 7
    p_n_moins_1 = 8
    q_n_moins_2 = 1
    q_n_moins_1 = 1

    while True:
        for a_i in [4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1]:
            # on ne démarre pas du premier car on l’a calculé 5 lignes plus haut
            p = a_i*p_n_moins_1 + p_n_moins_2
            q = a_i*q_n_moins_1 + q_n_moins_2
            if p**2 - 61*(q**2) == 1:
                print(p, q)
                return (p, q)
            p_n_moins_2 = p_n_moins_1
            q_n_moins_2 = q_n_moins_1
            p_n_moins_1 = p
            q_n_moins_1 = q


pell_fermat()

# je sais, il aurait été bien plus élégant d’écrire un algorithme qui marche
# quelque soit d, mais bon, j’avais déjà assez perdu de temps sur les 20
# premières questions…

