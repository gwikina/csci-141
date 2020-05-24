"""
file: write_a_meme.py
description: This program writes the message, "MOVE TOM"  using specific design specifications per letter
language: python3
author: glw3325 @ RIT.EDU
Gideon Wikina
"""
import turtle
def init():
    """
    moves the turtle backward so that the message starts in a way for it to be centeres

    pre-condition: turtle begins in the center of the screen
    
    post-condition: the message is cenetered
    
    """
    turtle.up()
    turtle.back(400)
def O():
    """
    draws an O letter

    pre-condition: space() was called
    
    post-condition: turtle ends at the lower right corner of the letter
    
    """
    turtle.down()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.up()
def T():
    """
    draws a T letter

    pre-condition: space() was called
    
    post-condition: turtle ends at the lower right corner of the letter
    
    """
    turtle.up()
    turtle.forward(25)
    turtle.left(90)
    turtle.down()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.back(50)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
def M():
    """
    draws an M letter

    pre-condition: turtle is facing direction message wants to be written in
    
    post-condition: turtle ends at the lower right corner of the letter
    
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
def V():
    """
    draws a V letter

    pre-condition: space() was called
    
    pre-condition: pen is up
    
    post-condition: turtle ends at the lower right corner of the letter
    
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(150)
    turtle.down()
    turtle.forward(113)
    turtle.left(120)
    turtle.forward(113)
    turtle.back(113)
    turtle.right(60)   
def E():
    """
    draws an E letter

    pre-condition: space() was called
    
    post-condition: turtle ends at the lower right corner of the letter
    
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
def space():
    """
    creates a space for the next letter

    pre-condition: turtle starts at the lower right corner of the letter
    
    post-condition: turtle ends at the lower left corner of the next letter (forward 50 from the right lower)
    
    """
    turtle.up()
    turtle.forward(50)
def MOVE():
    """
    creates the word MOVE

    pre-condition: space() is called
    
    post-condition: turtle ends at the lower right corner of the last letter of the word
    
    """
    M()
    space()
    O()
    space()
    V()
    space()
    space()
    E()
def TOM():
    """
    creates the word TOM

    pre-condition: space() is called
    
    post-condition: turtle ends at the lower right corner of the last letter of the word
    
    """
    T()
    space()
    O()
    space()
    M()
def test_SPACE():
    """
    test that the space is working accordingly

    pre-condition: turtle starts at the lower right corner of the letter
    
    post-condition: turtle ends at the lower left corner of the next letter (forward 50 from the right lower)
    
    """
    init()
    M()
    space()
    O()
def test_MOVE():
    """
    test that the word "move" is working accordingly

    pre-condition: space() is called
    
    post-condition: turtle ends at the lower right corner of the last letter of the word
    
    """
    init()
    MOVE()
def test_TOM():
    """
    test that the word "test" is working accordingly

    pre-condition: space() is called
    
    post-condition: turtle ends at the lower right corner of the last letter of the word

    """
    init()
    TOM()
def test_WORD_SPACE():
    """
    test that the spacing between words is working accordingly

    pre-condition: turtle starts at the lower right corner of the letter
    
    post-condition: turtle ends at the lower right corner of the last letter of the word
    
    """
    init()
    MOVE()
    space()
    space()
    TOM()
def main():
    """
    This program writes the message, "MOVE TOM"  using specific design specifications per letter

    pre-condition: all methods used are defined

    post-condition: turtle ends at the lower right corner of the last letter
    
    """
    init()
    MOVE()
    space()
    space()
    TOM()
    turtle.done()
main()
