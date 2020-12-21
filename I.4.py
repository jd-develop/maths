#!/usr/bin/env python3
# coding:utf-8
import turtle


def f(x):
    return ((2 * x) ** 2 - 12 * x) + 20


# number = float(input("Entrez un nombre : "))
# print(f(number))

turtle.up()
number = -10
turtle.goto(-500, -100)
turtle.down()
turtle.forward(1000)
turtle.up()
turtle.goto(0, -500)
turtle.left(90)
turtle.down()
turtle.forward(1000)
turtle.up()
for loop in range(31):
    print("f({}) = ".format(number), f(number))
    turtle.goto(number, f(number) - 100)
    turtle.down()
    number += 1

print("Terminé, cliquez pour quitter.")
turtle.exitonclick()
