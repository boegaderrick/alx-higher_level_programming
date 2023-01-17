#!/usr/bin/python3

import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['grey', 'white', 'red', 'green']
for number in range(400):
    t.forward(number+1)
    t.right(91)
    t.pencolor(colors[number%4])
    t.pensize(1.5)
    t.speed(0)
turtle.done()
