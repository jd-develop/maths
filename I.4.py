#!/usr/bin/env python3
# coding:utf-8
import turtle


def f(x):
    return ((2 * x) ** 2 - 12 * x) + 20


# number = float(input("Entrez un nombre : "))
# print(f(number))

turtle.up()
turtle.goto(-500, -200)
turtle.down()
turtle.forward(1000)
turtle.up()
turtle.goto(0, -500)
turtle.left(90)
turtle.down()
turtle.forward(1000)
turtle.up()

number = -15
for loop in range(121):
    print("f({}) = ".format(number), f(number))
    turtle.goto(number * 4, f(number) - 200)
    turtle.down()
    number += 0.25

print("Terminé, cliquez pour quitter.")
turtle.exitonclick()
