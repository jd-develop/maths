#!/usr/bin/env python3
# coding:utf-8
import math
# n tq x**n < s

x, s = eval(input("Entrez x, s avec 0<x<1 : "))
if not 0 < x < 1:
    raise ValueError("La valeur de x doit être comprise entre 0 et 1 exclus.")
n, xn = 0, 1

while xn >= s:
    xn *= x
    n += 1

print(f"{n} est le premier nombre n tel que x**n < s")

# si a multiple de b avec a, b entiers naturels
a, b = eval(input("Entrez a, b entiers naturels : "))
if a < 0 or b < 0:
    raise ValueError("a et b doivent être des entiers naturels !!")
if b != 0:
    while a >= b:
        a -= b

if a == 0:
    ans = True
else:
    ans = False

print("a", "est un multiple" if ans else "n'est pas un multiple", "de b")

# plus gd multiple de a inférieur à b avec a, b entiers naturels
a, b = eval(input("Entrez a, b entiers naturels : "))
if a < 0 or b < 0:
    raise ValueError("a et b doivent être des entiers naturels.")
m = 0
if a != 0:
    while m <= b:
        m += a
    m -= a  # on est allé un cran trop loin

print(f"Plus gd multiple de a inférieur à b : {m}")

# encadrement de sqrt(2) d'amplitude <= 10**-n par balayage
n = eval(input("Entrez le nombre de décimales souhaitées pour approximation racine de 2 : "))
a, r, h = 2, 0, 1  # nb à trouver racine, racine cherchée, pas
for i in range(0, n+1):
    while r**2 <= a:
        r += h
    r -= h
    h /= 10
print(r)
print(math.sqrt(2))
