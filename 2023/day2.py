import sys
import re

# Part One

""" sum = 0
for case in range(100):
    good = True
    full = sys.stdin.readline().rstrip()
    line = full.split(":")
    for draw in line[1].split(";"):
        red, blue, green = 0,0,0
        for balls in draw.split(","):
            num = balls.split()[0]
            color = balls.split()[1]
            if color == "red":
                red += int(num)
            elif color == "green":
                green +=  int(num)
            elif color == "blue":
                blue += int(num)
        if red > 12 or green > 13 or blue > 14:
            good = False
    if good == True:
        sum += case + 1
print(sum) """

sum = 0
for case in range(100):
    full = sys.stdin.readline().rstrip()
    game = full.split(":")
    mred, mgreen, mblue = 0,0,0
    for draw in game[1].split(";"):
        red, blue, green = 0,0,0
        for balls in draw.split(","):
            num = balls.split()[0]
            color = balls.split()[1]
            if color == "red":
                red += int(num)
            elif color == "green":
                green +=  int(num)
            elif color == "blue":
                blue += int(num)
        if red != 0 and red > mred:
            mred = red
        if green != 0 and green > mgreen:
            mgreen = green
        if blue != 0 and blue > mblue:
            mblue = blue
    sum += mred * mgreen * mblue
print(sum)