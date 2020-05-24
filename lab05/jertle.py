"""
jertle.py
python 3
glw3325
Gideon Wikina

Takes a series of defined commands in order to dictaste the manner in which the turtle performs

"""

# Notice that this program runs as is.
# It does not do anything, but that's OK.
# As you add functionality, add test functions that you call
#   instead of the main function.
# Then run main when you are ready to try some things in normal operation.
# (Remove this block of comments before submission.)

import sys
import time
import turtle

# Turtle Canvas Window Setup ######
                                  #
WORLD_SIZE = 800                  #
MARGIN = 10                       #
WINDOW_SIZE = WORLD_SIZE + MARGIN #
                                  #
###################################

SLEEP_TIME = 5

# The Set of Jertle Commands #####################################
                                                                 #
PENDOWN_CMD = "!1"  # No parameters                              #
PENUP_CMD = "!0"    # No parameters                              #
TURN_CMD = "o^"     # Parameter: angle, to the left, in degrees  #
FORWARD_CMD = "->"  # Parameter: number of units to move         #
CIRCLE_CMD = "()"   # Parameter: radius of circle                #
                                                                 #
##################################################################

### PRE-DEFINED ERROR CODES ###################################
                                                              #
ILLEGAL_COMMAND = 1  # Unrecognized command string            #
MISSING_ARGUMENT = 2 # More arguments needed for this command #
NO_ARG_END = 3       # Can't find the matching closing brace  #
                                                              #
###############################################################

def error( msg, e_code ):
    """
    A fatal error has occurred.
    Print an error message and end the program.
    :param msg: the string message to print before ending the program
    :param e_code: the integer error code with which the program exits
    """
    print( msg, file=sys.stderr )
    sys.exit( e_code )


def initialize():
    """
    Set up the turtle world.
    :return: None
    """
    turtle.setup( WINDOW_SIZE, WINDOW_SIZE )
    turtle.setworldcoordinates( -MARGIN, -MARGIN, WORLD_SIZE, WORLD_SIZE )
    turtle.up()
    turtle.goto(400,400)
    
def locate_end_of_arg(p):
    """
    Locates the end of an argument by iterating through the text until it finds a '}'

    pre-condition: text contains '}'

    post-condition: returns the index in which it found the '}'
    
    """
    for i in range(0, len(p)):
        if p[i] == '}':
            return i
def locate_beg_of_arg(p):
    """
    Locates the beginning of an argument by iterating through the text until it finds a {}'

    pre-condition: text contains '{'

    post-condition: returns the index in which it found the '{'
    
    """
    for i in range(0, len(p)):
        if p[i] == '{':
            return i
def interpret(filename):
    """
    Iterates through each line in the file and defines the command as every two characters in the line then redefines the line as the next charcter that has not been read yet until the end of the line

    Makes each jertile command achieve its desired function

    If command is not recognized, it shall print an error message 

    pre-condition: text contains '{'

    post-condition: returns the index in which it found the '{'
    
    """
    file = open(filename)
    for line in file:
        for command in line:
            command = line[:2]
            line = line [2:]
            if command == '->':
                i = locate_end_of_arg(line)
                n = float(line[1: i])
                line = line[(i+1):]
                turtle.forward(n)
            elif command == 'o^':
                turtle.left(90)
            elif command == '!0':
                turtle.penup()
            elif command == '!1':
                turtle.down()
            elif command == '()':
                i = locate_end_of_arg(line)
                n = float(line[1: i])
                line = line[(i+1):]
                turtle.circle(n)
    file.close()
                
def main():
    """
    Read Jertle program strings from a file and execute them.
    The file is provided by the user when this program runs.
    Stop when end of file is reached.
    
    :return: None
    
    """
    initialize()
    interpret('jertile.txt')
    turtle.done()

if __name__ == "__main__":
    main()

