#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def requin(c: float, p: float, r: float, n: int):
    for j in range(n):
        c, p, r = 0.5*c+0.2*p+0.2*r, 0.1*c+0.2*p+0.2*r, 0.4*c+0.6*p+0.6*r
    return c, p, r

