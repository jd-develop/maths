#!/usr/bin/env python3
# coding:utf-8
import turtle


def f(x):
    return ((2 * x) ** 2 - 12 * x) + 20


turtle.setworldcoordinates(-200, 0, 200, 400)
turtle.hideturtle()
turtle.speed(0)
turtle.getscreen().delay(0)
turtle.up()
turtle.goto(-500, 0)
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
    turtle.goto(number * 4, f(number))
    turtle.down()
    number += 0.25

turtle.up()
turtle.goto(-190, 0)
turtle.write("Terminé", font=("Courier", 30, "bold"))
print("Terminé.")
turtle.mainloop()
