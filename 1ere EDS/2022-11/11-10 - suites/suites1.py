#!/ust/bin/env python3
# coding:utf-8

def u(n: int):
    """
        u_0 = 0 ; u_{n+1} = 2u_n + 1 ; n >= 0
    """
    if n < 0:
        raise TypeError("Please specify a positive integer number.")
    if n == 0:
        return 0
    else:
        return 2*u(n-1) + 1


for i in range(998):  # max before RecursionError
    print(f"u({i}): {u(i)}")
