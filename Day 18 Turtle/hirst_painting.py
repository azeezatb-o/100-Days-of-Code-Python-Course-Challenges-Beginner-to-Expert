# # This commented part was used to get the colors list in the program below
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

import turtle as t
import random as r


tim = t.Turtle()
t.colormode(255)
colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.hideturtle()
# penup() erases the turtle movement (the line of turtle movement)
tim.penup()
# this goto(-300, 300) resets the starting point of the turtle on the screen
tim.goto(-300, 300)
tim.speed("fastest")


def draw_dots():
    for y in range(10):
        tim.dot(20, r.choice(colors))
        tim.forward(50)


for i in range(10):
    draw_dots()
    tim.back(500)
    tim.right(90)
    tim.forward(50)
    tim.left(90)

my_screen = t.Screen()
my_screen.exitonclick()