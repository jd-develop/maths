#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    f(x)=(x-1)(x+1)+1
    Calcule f(x) pour x=0;1;2;3;4;5;6;7;8;9.
"""

x = 0
while not x == 10:
    fx = (x - 1) * (x + 1) + 1
    print("f(" + str(x) + ") = " + str(fx))
    x += 1
