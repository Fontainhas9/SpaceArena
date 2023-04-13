# Space Arena! 
# The Ultimate Python Turtle Graphics Game Tutorial
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @André Fontainhas
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/
# Part 1: Getting Started

import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena! by @André Fontainhas")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

wn.mainloop()
