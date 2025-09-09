#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def frac_simple(x: float, accu: list[int], n: int = 3) -> list[int]:
     if n == 0:
         return [*accu]
     a_i = int(x)
     y_i = x-a_i
     if y_i==0:
         return [*accu, a_i]
     ap_ip1 = 1/y_i
     return frac_simple(ap_ip1, [*accu, a_i], n-1)


def frac_inv(frac: list[int]) -> int | float:
    if len(frac) == 1: return frac[0]
    return frac[0]+1/(frac_inv(frac[1:]))


