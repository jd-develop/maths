#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Listes (lists)
    Note : originellement je souhaitais faire cette partie le 23 mars, mais il faut le cours de maths sur les stats,
    effectué à la fin de l'année, pour la faire. Je ne reprendrai pas ce fichier.
"""

x_ = [20, 17, 20, 12]
n_ = [2, 1, 1, 3]


def moyenne(x, n):
    """Moyenne pondérée (valeurs dans la liste x, poids dans la liste n)"""
    return sum(
        [n[i]*x[i] for i in range(len(x))]
    ) / sum(n)

# fonction stat() manquante, cf. docstring du fichier.
