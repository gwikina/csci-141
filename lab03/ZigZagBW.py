""" 
file: ZigZagBW.py
description: Creates a Zig Zag Contraption Recursively
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
    Creates a Z like shape, a zig zag anytime the pen gets to an endpoint of the Z recursively

    pre-condition: pen is down, pen is facing north, ZigZag is defined 
    post condition: pen is where it started, facing north
    
    """
    if D==1:
        ZigZag(L)
    elif D > 1:
        turtle.forward(L/2)
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        recur_ZigZag(D-1, L/2)
        turtle.right(90)
        turtle.back(L)
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        turtle.back(L)
        turtle.left(90)
        recur_ZigZag(D-1, L/2)
        turtle.right(90)
        turtle.forward(L)
        turtle.left(90)
        turtle.forward(L/2)
def main():
    """
    Asks the user for a depth and then computes the calculation.

    pre-condition: pen is down, pen is facing east to be initialized later
    post condition: pen is where it started
    
    """
    depth = int(input('What is the depth of the ZigZag? '))
    init()
    recur_ZigZag(depth, 100)
    turtle.done()
main()
    
