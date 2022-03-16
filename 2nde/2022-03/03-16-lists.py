#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Listes (lists)"""
from random import randint


def two_dice_frequency(launches):
    """Retourne une liste des fréquences des sommes de deux dés tirés au sort"""
    list_ = [0]*12
    for i in range(launches):
        dice_sum = randint(1, 6) + randint(1, 6)
        list_[dice_sum - 1] = list_[dice_sum - 1] + 1
    list_ = [x/launches for x in list_]
    return list_


print(two_dice_frequency(1000))
