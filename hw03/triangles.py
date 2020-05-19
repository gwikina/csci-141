"""
file: triangles.py
description: recursively draws triangles at differentc levels
language: python3
author: glw3325 @ RIT.EDU
Gideon Wikina
"""
import turtle
def init():
    """
    sets the pen facing north

    pre-condition: pen is facing east
    Post-condition: pen is facing north
    
    """
    turtle.down()
    turtle.left(90)
def triangle(side):
    """
    draws level 1 triangle, upside down

    pre-condition: pen is facing north, pen is down
    Post-condition: pen is facing north, bottom vertice of triangle
    
    """
    turtle.left(30)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(150)
def triangle_2(side):
    """
    draws level 2 triangle, with level one triangles being drawn at it's vertices

    pre-condition: pen is facing north, pen is down
    post-condition: pen is facing north, bottom vertice of triangle
    
    """
    turtle.left(30)
    turtle.forward(side)
    turtle.right(30)
    triangle(side/2)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    triangle(side/2)
    turtle.right(90)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(150)
def triangle_3(side):
    """
    draws level 3 triangle, with level one triangles being drawn at it's vertices

    pre-condition: pen is facing north, pen is down
    post-condition: pen is facing north, bottom vertice of triangle
    
    """
    turtle.left(30)
    turtle.forward(side)
    turtle.right(30)
    triangle_2(side/2)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    triangle_2(side/2)
    turtle.right(90)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(150)
def triangle_n(side, depth):
    """
    makes a conditional for aLL depth values
    for greater than 3 - it starts off making the triangle and at the edge it recursively draws the triangle
    pre-condition: pen is facing north, pen is down
    post-condition: pen is facing north, bottom vertice of triangle
    
    """
    if depth == 1:
        triangle(side)
    if depth == 2:
        triangle_2(side)
    if depth == 3:
        triangle_3(side)
    if depth > 3:
        turtle.left(30)
        turtle.forward(side)
        turtle.right(30)
        triangle_n(side/2, depth-1)
        turtle.right(90)
        turtle.forward(side)
        turtle.left(90)
        triangle_n(side/2, depth-1)
        turtle.right(90)
        turtle.right(120)
        turtle.forward(side)
        turtle.right(150)
def main():
    """
    Initilizes and calls the function of choice

    Prompts user for inpput value
    
    """
    init()
    side_length = int(input('Enter a side length'))
    depth = int(input('Enter a number of depth '))
    triangle_n(side_length, depth)
main()
