# coding:utf-8
# simulation sondage
import random
import matplotlib.pyplot as plt

# réalité :
# Aymeric : 13 %
# Brunehault : 30 %
# Chilperic : 48 %
# Blanc et nul : reste


def tirage():
    votant = random.random()
    if votant < 0.13:
        vote = "Aymeric"
    elif votant < 0.43:
        vote = "Brunehault"
    elif votant < 0.91:
        vote = "Chilperic"
    else:
        vote = "Blanc ou nul"
    return vote


results = {
    "Aymeric": 0,
    "Brunehault": 0,
    "Chilperic": 0,
    "Blanc ou nul": 0
}

for i in range(1000):
    results[tirage()] += 1

x = results.keys()
y = list(results.values())

s = sum(y)
for i, value in enumerate(y):
    value *= 100/s
    y[i] = value

plt.bar(x, y)
plt.show()
