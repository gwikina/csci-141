"""
* The program below constructs a contraption of two sets of one singular hexagon suroonded by six other hexagons rotated, with the second being rotated 60 degrees *

                                                Gideon Lole Wikina 
"""
import turtle
def hexagon_parts():
    """
    Draws a line and then rotates the turtle 60 degrees in order get the effect of a hexagon

    pre-condition: pen is down
    pre-condition: Turtle is facing the direction in which the first side will be drawn.
    post-condition: turtle lands 60 degrees to the left
    """
    turtle.forward(100)  
    turtle.left(60)
def draw_hexagon():
    """
    Puts the parts of a hexagon together in order to draw the hexagon

    pre-condition: hexagon_parts() is defined
    post-condition: turtle ends at bottom left corner
    """
    hexagon_parts()
    hexagon_parts()
    hexagon_parts()
    hexagon_parts()
    hexagon_parts()
    hexagon_parts()
def superHEX():
    """
    Draws part of a hexagon in the center with another hexagon surronding it

    pre-condition: Turtle is facing the direction in which the first side will be drawn.
    post-condition: turtle is pointing 60 degrees to the right
    post-condition: turtle ends at the end of the original line segment
    """
    turtle.forward(100)
    turtle.right(60)
    draw_hexagon()
def main():
    """
    Executes the desired code.

    The six sets of superHEX makes the contraption, which draws a base in conjunction with thee hexagon in order to create a hexagon within surronding hexagons

    Turtle right rotates the turtle in order to create that overlap effect

    The next set of super hexes creates the second layer for the contraption

    pre-condition: All functions are defined
    pre-condition: Turtle is facing the direction in which the first side will be drawn.
    post-condition: Turtle is rotated 60 degrees to the right
    
    """
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    turtle.right(60)
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    superHEX()
    turtle.done()
main()

