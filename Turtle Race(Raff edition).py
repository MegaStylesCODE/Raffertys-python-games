###################################################################
#
# Author:       [redacted] Modded by Raff
# Title:        Turtle Race
# Version:      1.Raff.0
# Created:      24/04/2020
# Purpose:
# Log:
# Notes:        Edited from a tutorial
#               Part 1: https://www.youtube.com/watch?v=qOsbvj87Uos
#               Part 2: https://www.youtube.com/watch?v=AFqBlJurBnA
#
####################################################################

# Imports and other
import time
import turtle
from turtle import Turtle
from random import randint

turtles = []
turt_colours = ["snow", "cyan", "plum1", "yellow","black","red","blue","orange","green","pink"]
for i in range(10):
    t = Turtle()
    t.speed(0)
    t.color(turt_colours[i])
    t.shape("turtle")
    t.penup()
    t.goto(-250, 100 - i * 50)
    t.pendown()
    turtles.append(t)


def race():
    # MOVE TURTLES
    # while t1.xcor() < 200 and t2.xcor() < 200 and t3.xcor() < 200 and t4.xcor() < 200:
    win = False
    while not win:
        for index, t in enumerate(turtles):
            t.forward(randint(1, 5))
            if t.xcor() >= 200:
                print(f'The winner is {turt_colours[index]} turtle #{index + 1}!')
                # print("The winner is turtle #", index + 1, "!")
                win = True
                t.speed(1)
                t.right(270)  # Victory spin

                break


def screen_bg_setup():
    # TEXT ON SCREEN
    tdraw = turtle
    tdraw.color("white")
    tdraw.speed(0)
    tdraw.penup()
    tdraw.setpos(-270, 250)
    tdraw.write("TURTLE RACE Raff edition!", font=("impact", 30, "bold"))
    tdraw.penup()

    # FINISH LINE
    stamp_size = 30
    square_size = 25
    finish_line = 200

    tdraw.color("white")
    tdraw.shape("square")
    tdraw.shapesize(square_size / stamp_size)
    tdraw.penup()

    for i in range(10):
        tdraw.setpos(finish_line, (150 - (i * square_size * 2)))
        tdraw.stamp()

    for j in range(10):
        tdraw.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
        tdraw.stamp()

    tdraw.hideturtle()


def main():
    # WINDOW SETUP
    window = turtle.Screen()
    window.setup(width=0.5, height=0.7)
    window.title("TURTLE RACE (modded by raff) ")
    window.bgcolor("forestgreen")

    screen_bg_setup()
    print("Choose your color, Place your bets, And get ready!")
    countdown = 10  # Countdown from this number to 1
    for k in range(1, countdown + 1):
        print(countdown + 1 - k)
        time.sleep(1)  # Pause for 1 second
    print("Go!")

    race()

    print("End")
    window.mainloop()


main()