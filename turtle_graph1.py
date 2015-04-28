from turtle import *

reset()

def square(length):
    """ Draws a square with the given side length """

    for i in range(4):
        forward(length)
        right(90)
def S_structure_1():
    pencolor("purple") # turtle changes to purple pen
    speed(0)
    # Draw a spiral structure from the center of the window 
    # outwards using a for loop
    for i in range(0, 400, 2):
        forward(i)
        right(89)

    # Draw another spiral structure from the outside of the window 
    # towards the center of the window using another for loop
    for i in range(401, 0, -2):
        forward(i)
        right(89)
def poly(length, angle, sides):
    if sides == 0:
        return
    else:
        forward(length)
        right(angle)
        poly(length, angle, sides-1)
def pattern(number,length):
    for i in range(number):
        square(length)
        right(360/number)
