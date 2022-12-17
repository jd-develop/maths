#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def u(n):
    if n == 0:
        return 4
    else:
        return 2*u(n-1)-3

    
for n_ in range(5):
    print(u(n_))
