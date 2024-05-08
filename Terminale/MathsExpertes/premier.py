from math import sqrt, floor


def est_premier(n: int):
    d = 3
    while d <= floor(sqrt(n)):
        if n % d == 0:
            return d, False
        d += 2
    return None, True
 
