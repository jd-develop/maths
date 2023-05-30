# coding:utf-8
import matplotlib.pyplot as plt
import random


def sum_2_dices():
    return random.randint(1, 6) + random.randint(1, 6)


def histogram(n):
    results = [0]*13
    for i in range(n):
        results[sum_2_dices()] += 1
    return results


x = [i for i in range(1, 13)]


def hist(n: int):
    y = histogram(n)[1:]
    plt.bar(x, y)

    n = str(n)
    n_ = ""
    chars = 0
    for i in range(len(n)-1, -1, -1):
        chars += 1
        n_ = n[i] + n_
        if chars % 3 == 0:
            n_ = " " + n_
    plt.title(f"{n_} lancés")
    plt.show()


hist(10)
hist(50)
hist(100)
hist(1000)
hist(10000)
hist(1000000)
