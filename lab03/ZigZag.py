""" 
file: ZigZag.py
description: Creates a Zig Zag Contraption Recursively but alternates the color
language: python3
author: glw3325 @ RIT.EDU
Gideon Wikina
"""
import turtle
def init():
    """
    Initializes turtle to be facing upward

    pre-condition: pen is down, pen is facing north
    post condition: pen is where it started
    """
    turtle.down()
    turtle.left(90)
def ZigZag(L):
    """
    Creates a Z like shape, a zig zag that goes up half the length and to the right, before going back down path to the left in order to complete the shape 

    pre-condition: pen is down, pen is facing north
    post condition: pen is where it started
    
    """
    turtle.forward(L/2)
    turtle.right(90)
    turtle.forward(L)
    turtle.back(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.back(L)
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(L/2)
def recur_ZigZag(D,L):
    """
    Almost alternates colors but the back function erases the alteration of color, cannot figure out how to fix it, 

    pre-condition: pen is down, pen is facing north
    post condition: pen is where it started
    
    """
    if D==1:
        turtle.color('blue')
        ZigZag(L)
    elif D > 1:
        if D %2 == 0:
            turtle.color('pink')
        elif D % 2 ==1:
            turtle.color('blue')
        turtle.forward(L/2)
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        turtle.left(45)
        if (D-1) %2 == 0:
            turtle.color('pink')
            recur_ZigZag(D-1, L/2)
        elif (D-1) % 2 ==1:
            turtle.color('blue')
            recur_ZigZag(D-1, L/2)
        turtle.right(45)
        turtle.right(90)
        turtle.up()
        turtle.back(L)
        turtle.down()
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        turtle.up()
        turtle.back(L)
        turtle.left(90)
        turtle.left(45) #produces a lil tilt
        turtle.down()
        if (D-1) %2 == 0:
            turtle.color('pink')
            recur_ZigZag(D-1, L/2)
        elif (D-1) % 2 ==1:
            turtle.color('blue')
            recur_ZigZag(D-1, L/2)
        turtle.right(45)
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        turtle.forward(L/2)

def main():
    # ask user for an input for depth and then does the recursion
    depth = int(input('What is the depth of the ZigZag? '))
    init()
    recur_ZigZag(depth, 100)
    turtle.done()
main()
    
